#!/usr/bin/env python3
"""Validate the Sunrise Bakery starter files: HTML tags balanced, links between pages resolve, SVG is well-formed XML."""
import glob, os, re, sys, xml.dom.minidom
from html.parser import HTMLParser
base = os.path.join(os.path.dirname(__file__), "..", "..", "companion", "sunrise-bakery-starter")
VOID = {"meta", "link", "img", "br", "hr", "input"}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st = []; s.err = []; s.refs = []
    def handle_starttag(s, t, a):
        a = dict(a)
        if t not in VOID: s.st.append(t)
        for k in ("href", "src"):
            if k in a and not re.match(r"^[a-z]+:|#", a[k]): s.refs.append(a[k])
    def handle_endtag(s, t):
        if not s.st or s.st.pop() != t: s.err.append(t)
bad = 0
for f in sorted(glob.glob(os.path.join(base, "*.html"))):
    p = P(); p.feed(open(f, encoding="utf-8").read())
    if p.err or p.st: print("BAD tags", os.path.basename(f), p.err, p.st); bad += 1
    for r in p.refs:
        if not os.path.exists(os.path.join(base, r)): print("BROKEN link", os.path.basename(f), r); bad += 1
xml.dom.minidom.parse(os.path.join(base, "images", "logo.svg"))
print("starter files ok" if not bad else f"{bad} problems"); sys.exit(1 if bad else 0)
