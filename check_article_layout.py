#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify the article 2-column layout contract across every blog page.

The layout comes from
  .article-page .container { display: grid; grid-template-columns: 1fr 320px; }
A CSS grid only positions the DIRECT children of the grid element, so two
things must both hold or the right-hand 320px column breaks:

  1. <aside class="article-sidebar"> must be a DIRECT child of that container.
     If an element with class "article-main" appears anywhere in the aside's
     ancestor chain - or its immediate parent is not a container/blog-layout -
     the sidebar drops below the article body and the 320px column stays empty.

  2. That container must have EXACTLY TWO direct children (the article body
     wrapper and the aside). Extra children get auto-placed into the narrow
     320px rail: a featured image or a CTA meant to be full-width ends up
     squeezed beside the body copy.

Rule 1 caught blog-canton-fair-guide.html, whose <aside> sat inside a stray
div.article-grid wrapper (that class has no CSS rule anywhere in the project),
which dragged the sidebar below the body text. Rule 2 is a guard for the
neighbouring variant: a container holding three or more direct children, where
the sidebar is itself placed correctly but a sibling steals a grid cell.

Usage: python check_article_layout.py
"""
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr", "path", "circle"}
COMMENT = re.compile(r"<!--.*?-->", re.S)
SCRIPT = re.compile(r"<script.*?</script>", re.S)
STYLE = re.compile(r"<style.*?</style>", re.S)
TAG = re.compile(r"<(/?)([a-zA-Z0-9]+)([^>]*?)(/?)>")

# the full-width sibling that sits beside the sidebar
BODY_CLASSES = ("article-main", "blog-post-body", "article-content")


def clean(html):
    return STYLE.sub("", SCRIPT.sub("", COMMENT.sub("", html)))


def cls(attrs):
    m = re.search(r'class="([^"]*)"', attrs)
    return m.group(1).strip() if m else ""


class Node(object):
    __slots__ = ("tag", "cls", "parent", "kids")

    def __init__(self, tag, cls, parent):
        self.tag, self.cls, self.parent, self.kids = tag, cls, parent, []

    def label(self):
        return self.tag + ("." + self.cls.replace(" ", ".") if self.cls else "")

    def find_sidebar(self):
        if self.tag == "aside" and "article-sidebar" in self.cls.split():
            return self
        for k in self.kids:
            hit = k.find_sidebar()
            if hit is not None:
                return hit
        return None


def parse(html):
    root = Node("root", "", None)
    stack = [root]
    for m in TAG.finditer(html):
        closing, tag, attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if tag in VOID or selfclose:
            continue
        if not closing:
            n = Node(tag, cls(attrs), stack[-1])
            stack[-1].kids.append(n)
            stack.append(n)
        else:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i].tag == tag:
                    del stack[i:]
                    break
    return root


def chain(node):
    out = []
    n = node.parent
    while n is not None and n.tag != "root":
        out.append(n.label())
        n = n.parent
    out.reverse()
    return out


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "blog", "*.html")))
    ok, broken, odd, missing = [], [], [], []

    for f in files:
        rel = os.path.relpath(f, ROOT).replace("\\", "/")
        root = parse(clean(io.open(f, encoding="utf-8").read()))
        sb = root.find_sidebar()
        if sb is None:
            missing.append(rel)
            continue

        anc = chain(sb)
        parent_cls = anc[-1] if anc else ""
        nested = any("article-main" in a for a in anc) or not (
            "container" in parent_cls or "blog-layout" in parent_cls)
        if nested:
            broken.append("%-58s %s" % (rel, " > ".join(anc)))
            continue

        kids = sb.parent.kids
        if len(kids) != 2:
            odd.append("%-58s container.%s has %d children: %s"
                       % (rel, sb.parent.cls or "-", len(kids),
                          ", ".join(k.label() for k in kids)))
            continue
        other = [k for k in kids if k is not sb][0]
        if not any(c in other.cls.split() for c in BODY_CLASSES):
            odd.append("%-58s sidebar sibling is '%s', expected one of %s"
                       % (rel, other.label(), "/".join(BODY_CLASSES)))
            continue

        ok.append("%-58s %s" % (rel, " > ".join(anc)))

    print("articles scanned: %d" % len(files))
    print()
    print("LAYOUT OK - sidebar in right column, container has exactly 2 children  (%d)" % len(ok))
    for r in ok:
        print("   ", r)
    print()
    print("LAYOUT BROKEN - sidebar nested inside .article-main, renders below  (%d)" % len(broken))
    for r in broken:
        print("   ", r)
    print()
    print("CONTAINER SHAPE BROKEN - extra children land in the 320px rail  (%d)" % len(odd))
    for r in odd:
        print("   ", r)
    print()
    if missing:
        print("NO article-sidebar AT ALL  (%d)" % len(missing))
        for r in missing:
            print("   ", r)
        print()
    print("RESULT: %s" % ("ALL LAYOUTS OK"
                          if not broken and not missing and not odd else "ISSUES FOUND"))


if __name__ == "__main__":
    main()
