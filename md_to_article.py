#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a blog markdown draft into the site's article-page HTML and
splice it into an existing article file, preserving the page shell
(navbar, style, footer, CTA, social block).

Usage:
  python md_to_article.py <draft.md> <target.html> [options]

Options:
  --title "..."        H1 title
  --desc "..."         meta description
  --keywords "a, b"    meta keywords
  --category "..."     article category label
  --read "N min read"  read time label
  --date "Sep 1, 2026" display date
  --iso 2026-09-01     ISO date for schema
  --image ../assets/x.webp
  --alt "..."          featured image alt
  --caption "..."      featured image caption
"""
import io, os, re, sys, argparse


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:48] or "section"


def inline(text):
    """Markdown inline formatting to HTML. ASCII only."""
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def fix_links(html):
    """Rewrite root-absolute site links for a page living in /blog/."""
    def repl(m):
        url = m.group(2)
        if url.startswith("/blog/"):
            return '<a href="%s">' % url.replace("/blog/", "", 1) + m.group(1) + "</a>"
        if url.startswith("/"):
            return '<a href="../%s">' % url[1:] + m.group(1) + "</a>"
        return m.group(0)
    return re.sub(r'<a href="([^"]*)">([^<]*)</a>', lambda m: repl(m) if m.group(1).startswith("/") else m.group(0), html)


def md_table(rows):
    """rows: list of raw '| a | b |' lines. Returns HTML table."""
    cells = [ [c.strip() for c in r.strip().strip("|").split("|")] for r in rows ]
    head = cells[0]
    body = [r for r in cells[1:] if not all(set(c) <= set("-: ") for c in r)]
    out = ['<div class="table-wrap">', "<table>", "<thead><tr>"]
    for c in head:
        out.append("<th>%s</th>" % inline(c))
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def md_to_html(md):
    """Convert the draft body into (toc_items, html)."""
    lines = md.split("\n")
    out, toc = [], []
    para, listbuf, tablebuf = [], [], []
    num = 0
    open_section = False
    skip_meta = True

    def flush():
        nonlocal para, listbuf, tablebuf
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para)))
            para = []
        if listbuf:
            out.append("<ul>" + "".join("<li>%s</li>" % inline(x) for x in listbuf) + "</ul>")
            listbuf = []
        if tablebuf:
            out.append(md_table(tablebuf))
            tablebuf = []

    for raw in lines:
        line = raw.rstrip()
        s = line.strip()

        # meta lines are dropped unconditionally, wherever they sit in the draft
        if re.match(r"^Meta\s+(title|description|keywords|slug|url)\s*:", s, re.I):
            continue

        if skip_meta:
            if s.startswith("---"):
                continue
            if s.startswith("# "):
                skip_meta = False
                continue
            if not s:
                continue
            skip_meta = False

        if not s:
            flush()
            continue
        if s.startswith("---"):
            flush()
            continue

        if s.startswith("## "):
            flush()
            if open_section:
                out.append("</section>")
            num += 1
            title = s[3:].strip()
            sid = slugify(title)
            toc.append((sid, "%d. %s" % (num, title)))
            out.append('<section id="%s">\n<h2><span class="section-num">%02d</span> %s</h2>' % (sid, num, title))
            open_section = True
            continue
        if s.startswith("### "):
            flush()
            out.append("<h3>%s</h3>" % inline(s[4:].strip()))
            continue
        if s.startswith("# "):
            continue
        if s.startswith("|"):
            tablebuf.append(s)
            continue
        if s.startswith("- ") or s.startswith("* "):
            listbuf.append(s[2:].strip())
            continue
        if re.match(r"^\d+\. ", s):
            listbuf.append(re.sub(r"^\d+\. ", "", s))
            continue
        if s.startswith(">"):
            flush()
            out.append('<div class="article-tip">%s</div>' % inline(s.lstrip("> ").strip()))
            continue
        para.append(s)

    flush()
    if open_section:
        out.append("</section>")
    return toc, "\n".join(out)


def build_article(args, toc, body, sidebar_html):
    toc_html = "\n".join('<li><a href="#%s">%s</a></li>' % (sid, t) for sid, t in toc)
    return """<article class="article-page">
 <div class="container">
 <div class="article-main">

  <header class="article-header">
  <div class="article-meta-top">
   <span class="article-category">%(category)s</span>
   <span class="article-read-time">%(read)s</span>
   <span class="article-date">%(date)s</span>
  </div>
  <h1 class="article-title">%(title)s</h1>
  <p class="article-excerpt">%(excerpt)s</p>
  </header>

  <div class="blog-image">
  <img src="%(image)s" alt="%(alt)s" style="width:100%%;border-radius:12px;max-height:450px;object-fit:cover;" loading="lazy" />
  </div>
  <p class="photo-caption">%(caption)s</p>

  <div class="article-toc">
  <strong>Table of Contents</strong>
  <ul>
  %(toc)s
  </ul>
  </div>

  <div class="article-content">
%(body)s

  <div class="author-box">
   <img style="max-height:450px;object-fit:cover;" src="../assets/22.webp" alt="Karsa - China Sourcing Agent" class="author-avatar" loading="lazy" />
   <div class="author-details">
   <strong>Karsa Loong</strong>
   <span>China Sourcing Expert</span>
   </div>
  </div>
  <p>Karsa has been helping e-commerce sellers and businesses source products from China since 2016, serving clients from 23+ countries.</p>
  </div>

 %(sidebar)s

 </div>
 </div>
</article>""" % {
        "category": args.category,
        "read": args.read,
        "date": args.date,
        "title": args.title,
        "excerpt": args.excerpt,
        "image": args.image,
        "alt": args.alt,
        "caption": args.caption,
        "toc": toc_html,
        "body": body,
        "sidebar": sidebar_html,
    }


TABLE_CSS = """.table-wrap { overflow-x:auto; margin:26px 0; }
.article-content table { width:100%; border-collapse:collapse; font-size:0.92rem; }
.article-content th { background:#F4F7FC; text-align:left; padding:12px 14px; font-weight:600; color:#1a2340; border-bottom:2px solid #E5E9F0; }
.article-content td { padding:11px 14px; border-bottom:1px solid #E5E9F0; color:#333; }
.article-content tbody tr:hover { background:#FAFBFE; }
.article-content table strong { color:#1a2340; }
"""


DEFAULT_SIDEBAR = """<aside class="article-sidebar">
 <div class="sidebar-card">
  <h4>Need a China Sourcing Quote?</h4>
  <p style="font-size:0.9rem;color:#555;line-height:1.6;">Send us your product, target quantity, and destination. We will verify factories, negotiate factory-direct pricing, and calculate landed cost before you commit.</p>
  <a href="https://wa.me/8619898484442" target="_blank" class="btn btn-primary btn-sm" style="margin-top:8px;display:inline-block;"><i class="fab fa-whatsapp"></i> WhatsApp Karsa</a>
 </div>
 <div class="sidebar-card">
  <h4>Related Services</h4>
  <ul style="list-style:none;padding:0;margin:0;">
   <li style="margin-bottom:8px;"><a href="../landing/product-sourcing-agent.html" style="color:#0057FF;font-size:0.85rem;">Product Sourcing Service</a></li>
   <li style="margin-bottom:8px;"><a href="../landing/quality-control-china.html" style="color:#0057FF;font-size:0.85rem;">Quality Control Service</a></li>
   <li style="margin-bottom:8px;"><a href="../landing/shipping-from-china.html" style="color:#0057FF;font-size:0.85rem;">Shipping from China</a></li>
  </ul>
 </div>
 <div class="sidebar-card">
  <h4>Related Articles</h4>
  <ul class="related-list">
   <li><a href="blog-how-to-import-from-china.html">How to Import from China: The Complete Process</a></li>
   <li><a href="blog-hidden-costs-importing-china.html">The Hidden Costs of Importing from China</a></li>
   <li><a href="blog-import-china-tariff-guide-2026.html">China Import Tariff Guide 2026</a></li>
   <li><a href="blog-verify-chinese-factory-audit-checklist.html">How to Verify a Chinese Factory</a></li>
  </ul>
 </div>
</aside>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("target")
    ap.add_argument("--title", required=True)
    ap.add_argument("--desc", required=True)
    ap.add_argument("--excerpt", default=None)
    ap.add_argument("--keywords", required=True)
    ap.add_argument("--category", default="Sourcing Guides")
    ap.add_argument("--read", default="14 min read")
    ap.add_argument("--date", required=True)
    ap.add_argument("--iso", required=True)
    ap.add_argument("--image", default="../assets/02.webp")
    ap.add_argument("--alt", required=True)
    ap.add_argument("--caption", default="")
    ap.add_argument("--sidebar-file", default=None,
                    help="Path to an HTML snippet file used as the article sidebar. "
                         "If omitted, a generic sourcing sidebar is used.")
    ap.add_argument("--cta-head", default="Ready to Start Your China Sourcing Project?")
    ap.add_argument("--cta-text",
                    default="Send us your product details and target quantity. We will tell you what we would do, including when the answer is that the product is not worth sourcing.")
    args = ap.parse_args()
    args.excerpt = args.excerpt or args.desc

    if args.sidebar_file:
        sidebar_html = io.open(args.sidebar_file, encoding="utf-8").read().strip()
    else:
        sidebar_html = DEFAULT_SIDEBAR

    md = io.open(args.draft, encoding="utf-8").read()
    toc, body = md_to_html(md)
    body = fix_links(body)
    article = build_article(args, toc, body, sidebar_html)

    html = io.open(args.target, encoding="utf-8").read()

    url = "https://www.youna-global.com/blog/" + os.path.basename(args.target)
    kws = [k.strip() for k in args.keywords.split(",") if k.strip()]

    # --- head meta ---
    html = re.sub(r"<title>.*?</title>", "<title>%s</title>" % args.title, html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content=".*?" />',
                  '<meta name="description" content="%s" />' % args.desc, html, count=1, flags=re.S)
    html = re.sub(r'<meta name="keywords" content=".*?" />',
                  '<meta name="keywords" content="%s" />' % args.keywords, html, count=1, flags=re.S)
    html = re.sub(r'<meta property="og:title" content=".*?" />',
                  '<meta property="og:title" content="%s" />' % args.title, html, count=1, flags=re.S)
    html = re.sub(r'<meta property="og:description" content=".*?" />',
                  '<meta property="og:description" content="%s" />' % args.desc, html, count=1, flags=re.S)
    html = re.sub(r'<meta property="article:published_time" content=".*?" />',
                  '<meta property="article:published_time" content="%s" />' % args.iso, html, count=1, flags=re.S)
    html = re.sub(r'<meta name="twitter:title" content=".*?" />',
                  '<meta name="twitter:title" content="%s" />' % args.title, html, count=1, flags=re.S)
    html = re.sub(r'<meta name="twitter:description" content=".*?" />',
                  '<meta name="twitter:description" content="%s" />' % args.desc, html, count=1, flags=re.S)

    # --- og:image / twitter:image sync to the featured image (keeps cards consistent) ---
    og_image = args.image.replace("../", "https://www.youna-global.com/")
    html = re.sub(r'<meta property="og:image" content=".*?" />',
                  '<meta property="og:image" content="%s" />' % og_image, html, count=1, flags=re.S)
    html = re.sub(r'<meta name="twitter:image" content=".*?" />',
                  '<meta name="twitter:image" content="%s" />' % og_image, html, count=1, flags=re.S)

    # --- schema: BlogPosting ---
    blogposting = """<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "BlogPosting",
"headline": "%s",
"description": "%s",
"image": "%s",
"author": { "@type": "Person", "name": "Karsa", "url": "https://www.youna-global.com/about.html" },
"publisher": {
 "@type": "Organization",
 "name": "Youna Global",
 "logo": { "@type": "ImageObject", "url": "https://www.youna-global.com/assets/LOGO2.png" }
},
"datePublished": "%s",
"dateModified": "%s",
"mainEntityOfPage": "%s",
"keywords": [
%s
]
}
</script>""" % (args.title, args.desc,
                args.image.replace("../", "https://www.youna-global.com/"),
                args.iso, args.iso, url,
                ",\n".join(' "%s"' % k for k in kws))

    html = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "BlogPosting".*?</script>',
                  lambda m: blogposting, html, count=1, flags=re.S)

    # --- schema: BreadcrumbList ---
    crumb = """<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "BreadcrumbList",
"itemListElement": [
 { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.youna-global.com/" },
 { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.youna-global.com/blog.html" },
 { "@type": "ListItem", "position": 3, "name": "%s" }
]
}
</script>""" % args.title.replace('"', "'")
    html = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "BreadcrumbList".*?</script>',
                  lambda m: crumb, html, count=1, flags=re.S)

    # --- table css (inject before the media query) ---
    if ".table-wrap" not in html:
        html = re.sub(r"(@media \(max-width:640px\))", TABLE_CSS + r"\1", html, count=1)

    # --- article body ---
    html = re.sub(r'<article class="article-page">.*?</article>',
                  lambda m: article, html, count=1, flags=re.S)

    # --- closing CTA (configurable) ---
    html = re.sub(r"(<section class=\"cta-section\">.*?<h2>).*?(</h2>)",
                  r"\1%s\2" % args.cta_head, html, count=1, flags=re.S)
    html = re.sub(r"(<div class=\"cta-text\">.*?<p>).*?(</p>)",
                  r"\1%s\2" % args.cta_text,
                  html, count=1, flags=re.S)

    io.open(args.target, "w", encoding="utf-8", newline="\n").write(html)
    bad = [i + 1 for i, l in enumerate(html.split("\n")) if any(ord(c) > 127 for c in l)]
    print("written: %s" % args.target)
    print("sections: %d  |  non-ascii lines: %d" % (len(toc), len(bad)))
    if bad:
        print("NON-ASCII AT:", bad[:10])


if __name__ == "__main__":
    main()
