#!/usr/bin/env python3
"""WARNING-ONLY review aid: find glossary terms used in a chapter BEFORE the chapter that introduces them.
Ordinary words used informally (allowlist below) are ignored. Output is a to-do list for the beginner-accessibility review."""
import csv, glob, os, re, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
num = {c[1]: i + 1 for i, c in enumerate(T.C)}
ALLOW = {"file", "folder", "computer", "path", "storage", "memory", "network", "server", "client", "local", "remote", "account", "command", "character", "web", "internet"}
terms = []
for r in csv.DictReader(open(os.path.join(root, "glossary", "glossary-master.csv"))):
    base = re.sub(r"\s*\(.*?\)", "", r["term"]).strip()
    terms.append((base.lower(), r["first_chapter_key"], r["term"]))
hits = 0
for f in sorted(glob.glob(os.path.join(root, "manuscript", "parts", "*", "ch*.md"))):
    m = re.search(r"^number: (\d+)", open(f).read(), re.M); n = int(m.group(1))
    text = re.sub(r"```.*?```", "", open(f).read(), flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    text = re.sub(r"^#+ .*$", "", text, flags=re.M)
    body = text.split("## Checkpoint")[0].lower()
    for base, first, full in terms:
        if num[first] > n and base not in ALLOW and len(base) > 2:
            for mm in re.finditer(r"\b" + re.escape(base) + r"\b", body):
                ctx = body[max(0, mm.start() - 40):mm.end() + 40].replace("\n", " ")
                print(f"Ch{n} uses '{base}' before Ch{num[first]} defines it: ...{ctx}..."); hits += 1; break
print(f"term-order warnings: {hits}")
