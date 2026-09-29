#!/usr/bin/env python3
"""Split an example URL into its parts using Python's standard library (a local, offline demonstration)."""
import os, sys
from urllib.parse import urlsplit, parse_qs
u = "https://example.org:8443/menu/cakes?sort=price&page=2#top"
p = urlsplit(u)
lines = [f"URL:      {u}", f"scheme:   {p.scheme}", f"host:     {p.hostname}", f"port:     {p.port}", f"path:     {p.path}",
         f"query:    {p.query}   -> {parse_qs(p.query)}", f"fragment: {p.fragment}"]
text = "\n".join(lines) + "\n"
if "--check" in sys.argv:
    exp = open(os.path.join(os.path.dirname(__file__), "expected-url.txt")).read()
    if exp != text: print("DIFF\n" + text); sys.exit(1)
    print("OK url_parts"); sys.exit(0)
sys.stdout.write(text)
