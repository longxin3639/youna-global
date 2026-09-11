#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-process a blog article page produced by md_to_article.py.

md_to_article.py rewrites the head meta, the JSON-LD BlogPosting and
BreadcrumbList blocks, the article body and the closing CTA. It does NOT
touch a handful of shell fields that are still article-specific, and it has
no support for inline figures or a FAQPage block. This script closes that
gap so the publish pipeline is repeatable:

  python article_post.py blog/blog-xxx.html --url-slug blog-xxx.html \
      --h1 "Display H1" --breadcrumb "Short Crumb" \
      --section "Trade Shows" --tag "Canton Fair" \
      --figure "before_marker||src||alt||caption" \
      --faq

Run md_to_article.py first, then this script. Both are idempotent enough to
re-run in order if a draft changes.

Options:
  --url-slug   bare file name; canonical, og:url and JSON-LD use it
  --h1         display H1 (the converter reuses --title for the H1, which is
               usually the shorter meta title; pass the longer H1 here)
  --breadcrumb visible breadcrumb label
  --section    <meta property="article:section">
  --tag        <meta property="article:tag"> (repeatable)
  --figure     'marker||src||alt||caption'; the figure is inserted directly
               before the first occurrence of marker (raw HTML substring)
  --faq        build a FAQPage JSON-LD from the rendered FAQ section
  --faq-head   H3-answered section heading text (default 'Frequently Asked Questions')
"""
import argparse
import html as htmllib
import io
import re

SITE = "https://www.youna-global.com"
IMG_BLOCK = """   <div class="blog-image">
   <img style="max-height:450px;object-fit:cover;" src="%s" alt="%s" loading="lazy" />
   </div>
   <p class="photo-caption">%s</p>
"""


def strip_tags(s):
    s = re.sub(r"<[^>]+>", "", s)
    return htmllib.unescape(s).strip()


def jesc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def set_field(html, pattern, value, label, expect=1):
    new, n = re.subn(pattern, lambda m: value, html, count=1, flags=re.S)
    if n != expect:
        raise SystemExit("FAILED to set %s (matched %d)" % (label, n))
    return new


def build_faq(section_html):
    qa = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", section_html, re.S)
    if not qa:
        raise SystemExit("FAILED: no H3/P question-answer pairs found in FAQ section")
    items = []
    for q, a in qa:
        items.append(
            ' {\n'
            ' "@type": "Question",\n'
            ' "name": "%s",\n'
            ' "acceptedAnswer": { "@type": "Answer", "text": "%s" }\n'
            ' }' % (jesc(strip_tags(q)), jesc(strip_tags(a)))
        )
    return (
        '<script type="application/ld+json">\n'
        '{\n'
        '"@context": "https://schema.org",\n'
        '"@type": "FAQPage",\n'
        '"mainEntity": [\n'
        + ",\n".join(items) +
        '\n]\n'
        '}\n'
        '</script>'
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--url-slug", required=True)
    ap.add_argument("--h1", required=True)
    ap.add_argument("--breadcrumb", required=True)
    ap.add_argument("--section", default=None)
    ap.add_argument("--tag", action="append", default=[])
    ap.add_argument("--figure", action="append", default=[])
    ap.add_argument("--faq", action="store_true")
    ap.add_argument("--faq-head", default="Frequently Asked Questions")
    args = ap.parse_args()

    url = "%s/blog/%s" % (SITE, args.url_slug)
    html = io.open(args.target, encoding="utf-8").read()

    html = set_field(html, r'<link rel="canonical" href="[^"]*" />',
                     '<link rel="canonical" href="%s" />' % url, "canonical")
    html = set_field(html, r'<meta property="og:url" content="[^"]*" />',
                     '<meta property="og:url" content="%s" />' % url, "og:url")
    html = set_field(html, r'<span style="color:#888;">.*?</span>',
                     '<span style="color:#888;">%s</span>' % args.breadcrumb,
                     "breadcrumb label")
    html = set_field(html, r'<h1 class="article-title">.*?</h1>',
                     '<h1 class="article-title">%s</h1>' % args.h1, "H1")
    if args.section:
        html = set_field(html, r'<meta property="article:section" content="[^"]*" />',
                         '<meta property="article:section" content="%s" />' % args.section,
                         "article:section")
    if args.tag:
        found = re.findall(r'<meta property="article:tag" content="[^"]*" />', html)
        if not found:
            raise SystemExit("FAILED: no article:tag meta found in shell")
        block = "\n".join(' <meta property="article:tag" content="%s" />' % t
                          for t in args.tag)
        html = html.replace(found[0], block, 1)
        for old in found[1:]:
            html = html.replace("\n" + old, "", 1).replace(old + "\n", "", 1)

    for spec in args.figure:
        parts = spec.split("||")
        if len(parts) != 4:
            raise SystemExit("bad --figure spec: %s" % spec)
        marker, src, alt, caption = parts
        if marker not in html:
            raise SystemExit("FAILED: figure marker not found: %s" % marker)
        html = html.replace(marker, IMG_BLOCK % (src, alt, caption) + marker, 1)

    if args.faq:
        m = re.search(r'<section id="[^"]*">\s*<h2>.*?%s</h2>(.*?)</section>'
                      % re.escape(args.faq_head), html, re.S)
        if not m:
            raise SystemExit("FAILED: FAQ section not found")
        faq = build_faq(m.group(1))
        if '"@type": "FAQPage"' in html:
            raise SystemExit("FAILED: FAQPage already present")
        anchor = "</script>"
        idx = html.find('<script type="application/ld+json">')
        while True:
            nxt = html.find(anchor, idx)
            body = html[idx:nxt]
            if '"BreadcrumbList"' in body:
                html = html[:nxt + len(anchor)] + "\n" + faq + html[nxt + len(anchor):]
                break
            idx = html.find('<script type="application/ld+json">', nxt)
            if idx == -1:
                raise SystemExit("FAILED: could not place FAQPage after BreadcrumbList")

    bad = [i + 1 for i, l in enumerate(html.split("\n")) if any(ord(c) > 127 for c in l)]
    io.open(args.target, "w", encoding="utf-8", newline="\n").write(html)
    print("post-processed: %s" % args.target)
    print("figures added: %d  |  faq: %s  |  non-ascii lines: %d"
          % (len(args.figure), args.faq, len(bad)))
    if bad:
        print("NON-ASCII AT:", bad[:10])


if __name__ == "__main__":
    main()
