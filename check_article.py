#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static checks for a published blog article page.

Run after md_to_article.py + article_post.py, before handing the file to the
user for git push. Checks:
  1. every application/ld+json block parses
  2. div / section / article open-close balance
  3. non-ASCII characters anywhere (site convention is pure ASCII)
  4. every internal href/src resolves to a file that exists on disk
  5. no leftover meta leakage (Meta title:, Meta description: in the body)
  6. external links use real <a href>, not escaped text

Usage: python check_article.py blog/blog-xxx.html
"""
import io
import json
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))


def check(path):
    full = os.path.join(ROOT, path)
    html = io.open(full, encoding="utf-8").read()
    problems = []

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    types = []
    for i, b in enumerate(blocks):
        try:
            data = json.loads(b)
            types.append(data.get("@type"))
        except Exception as e:
            problems.append("JSON-LD block %d does not parse: %s" % (i + 1, e))

    for tag in ("div", "section", "article", "aside"):
        o = len(re.findall(r"<%s[\s>]" % tag, html))
        c = len(re.findall(r"</%s>" % tag, html))
        if o != c:
            problems.append("<%s> unbalanced: %d open / %d close" % (tag, o, c))

    body = html.split("</head>", 1)[-1]
    bad = sorted({c for c in html if ord(c) > 127})
    if bad:
        problems.append("non-ASCII characters present: %r" % bad[:10])

    if re.search(r"^Meta (title|description|keywords|slug|url)\s*:", body, re.M | re.I):
        problems.append("draft meta lines leaked into the body")

    if re.search(r"&lt;a href=", html):
        problems.append("escaped anchor text found (&lt;a href=)")

    missing = []
    for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
        u = m.group(1)
        if u.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "//")):
            continue
        u = u.split("#")[0].split("?")[0]
        if not u:
            continue
        # hrefs may be percent-encoded - e.g. src="goods%20%20%281%29.webp"
        # points at a file literally named "goods  (1).webp". Decode before
        # touching the disk, otherwise every such link is a false 404.
        dec = urllib.parse.unquote(u)
        if dec.startswith("/"):
            # root-absolute links resolve against the site root, not the page dir
            target = os.path.normpath(os.path.join(ROOT, dec.lstrip("/")))
        else:
            target = os.path.normpath(os.path.join(os.path.dirname(full), dec))
        if not os.path.exists(target):
            missing.append(u)
    if missing:
        problems.append("broken internal links: %s" % sorted(set(missing)))

    print("== %s ==" % path)
    print("schema types: %s" % types)
    print("hash checks: external links %d | internal links %d"
          % (len(re.findall(r'href="https?://', html)),
             len(re.findall(r'(?:href|src)="(?!https?:|mailto:|#|//)', html))))
    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    rc = 0
    for p in sys.argv[1:]:
        rc |= check(p)
    sys.exit(rc)
