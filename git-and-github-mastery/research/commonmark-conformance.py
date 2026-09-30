#!/usr/bin/env python3
"""Runs the official CommonMark specification examples (commonmark/commonmark-spec, spec.txt) through markdown-it-py, the renderer
used for the Markdown examples in Chapter 8, and reports how many produce the HTML that the specification gives.
Whitespace differences between tags are ignored. Exit status 1 if any example differs. Needs: markdown-it-py, network access."""
import re, sys, urllib.request
from markdown_it import MarkdownIt
URL = "https://raw.githubusercontent.com/commonmark/commonmark-spec/master/spec.txt"
t = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "book-verification/1.0"}), timeout=60).read().decode()
ver = re.search(r"^version: '([^']+)'", t, flags=re.M).group(1)
ex = re.findall(r"^`{32} example.*?\n(.*?)^\.\n(.*?)^`{32}$", t, flags=re.S | re.M)
md = MarkdownIt("commonmark")
squash = lambda s: re.sub(r"\s+", "", s)
bad = [i for i, (src, html) in enumerate(ex, 1) if squash(md.render(src.replace("→", "\t"))) != squash(html.replace("→", "\t"))]
print(f"CommonMark spec {ver}: {len(ex)} examples, {len(ex) - len(bad)} match, {len(bad)} differ {bad[:20]}")
sys.exit(1 if bad else 0)
