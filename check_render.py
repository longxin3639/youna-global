#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Serve the site locally and fetch every internal link of a page over HTTP.

Catches what a static path check cannot: case-sensitivity, directory-index
behaviour, and anything the static check missed. Run it before handing a new
article to the user for git push.

Usage: python check_render.py blog/blog-xxx.html [more.html ...]
"""
import http.server
import io
import os
import re
import socketserver
import sys
import threading
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8123


def start_server():
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=ROOT, **k)
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    return httpd


def fetch(base, path):
    # hrefs come in two flavours on this site: raw ("assets/WhatsApp LOGO.png")
    # and percent-encoded ("assets/.../Pet%20Supplies/x.webp"). Always decode
    # first, then encode once, otherwise an already-encoded path gets encoded a
    # second time ("%20" -> "%2520") and every such link is a false 404.
    url = base + "/" + urllib.parse.quote(urllib.parse.unquote(path))
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            return r.status, len(r.read())
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception as e:
        return "ERR", str(e)


def main():
    httpd = start_server()
    base = "http://127.0.0.1:%d" % PORT
    rc = 0
    try:
        for page in sys.argv[1:]:
            html = io.open(os.path.join(ROOT, page), encoding="utf-8").read()
            links = set()
            for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
                u = m.group(1)
                if u.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:", "//")):
                    continue
                u = u.split("#")[0].split("?")[0]
                if not u:
                    continue
                links.add(os.path.normpath(os.path.join(os.path.dirname(page), u)).replace("\\", "/"))
            print("== %s ==" % page)
            status, size = fetch(base, page)
            print("  page: %s (%s bytes)" % (status, size))
            if status != 200:
                rc = 1
            bad = []
            for l in sorted(links):
                s, _ = fetch(base, l)
                if s != 200:
                    bad.append("%s -> %s" % (l, s))
            print("  internal targets fetched: %d | failures: %d" % (len(links), len(bad)))
            for b in bad:
                print("   FAIL %s" % b)
                rc = 1
    finally:
        httpd.shutdown()
    print("RENDER CHECK %s" % ("PASSED" if rc == 0 else "FAILED"))
    return rc


if __name__ == "__main__":
    sys.exit(main())
