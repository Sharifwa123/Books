#!/usr/bin/env python3
"""Cross-reference and consistency checks. Exit code 1 on any problem.
Checks:
 1. toc_data ordering (prerequisites earlier), unique keys, Core chapters never require Deep chapters.
 2. planning/chapter-map.json matches toc_data (i.e. build_planning.py was run).
 3. Every 'Ch N Title' mention in non-superseded planning/manuscript docs matches the chapter map.
 4. exercises/registry.csv chapter keys/numbers valid; research ledger ids unique.
 5. Manuscript files: any {ch:key} token resolves to a real key.
"""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
root = os.path.join(os.path.dirname(__file__), "..")
errs = []
keys = [c[1] for c in T.C]; pos = {k: i for i, k in enumerate(keys)}
if len(keys) != len(set(keys)): errs.append("duplicate chapter keys")
tag = {c[1]: c[3] for c in T.C}
for c in T.C:
    for r in c[5]:
        if r not in pos: errs.append(f"{c[1]}: unknown prerequisite {r}")
        elif pos[r] >= pos[c[1]]: errs.append(f"{c[1]}: prerequisite {r} appears later")
        elif tag[c[1]] == "Core" and tag[r] == "Deep": errs.append(f"Core {c[1]} requires Deep {r}")
cm = json.load(open(os.path.join(root, "planning", "chapter-map.json")))
for i, c in enumerate(T.C, 1):
    if cm.get(c[1], {}).get("number") != i: errs.append(f"chapter-map stale for {c[1]} (run tools/build_planning.py)")
by_num = {v["number"]: v["title"] for v in cm.values()}
pat = re.compile(r"\bCh (\d+) ([A-Z][A-Za-z0-9,()&' -]+)")
for base, _, files in os.walk(root):
    if any(s in base for s in (".git", "results")): continue
    for f in files:
        if not f.endswith(".md"): continue
        p = os.path.join(base, f); text = open(p, errors="replace").read()
        if text.startswith("> **SUPERSEDED") or text.startswith("> **Note:** chapter numbers"): continue
        scan = re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", text, flags=re.S))  # ignore code spans/blocks
        for m in re.finditer(r"\{ch:([a-z_0-9]+)\}", scan):
            if m.group(1) not in pos: errs.append(f"{p}: unknown {{ch:{m.group(1)}}}")
        for m in pat.finditer(text):
            num, t = int(m.group(1)), m.group(2).strip()
            real = by_num.get(num)
            if real is None: errs.append(f"{p}: Ch {num} does not exist"); continue
            if not (t.startswith(real) or real.startswith(t.split(" | ")[0].strip())):
                errs.append(f"{p}: 'Ch {num} {t}' but chapter {num} is '{real}'")
with open(os.path.join(root, "exercises", "registry.csv")) as f:
    for r in csv.DictReader(f):
        if r["chapter_key"] not in pos: errs.append(f"registry: bad chapter_key {r['chapter_key']}")
        elif int(r["chapter_no"]) != pos[r["chapter_key"]] + 1: errs.append(f"registry: stale chapter_no for {r['exercise_id']}")
ids = [r["id"] for r in csv.DictReader(open(os.path.join(root, "research", "research-ledger.csv")))]
if len(ids) != len(set(ids)): errs.append("ledger: duplicate ids")
print("chapters:", len(keys), "| ledger rows:", len(ids), "| problems:", len(errs))
for e in errs: print(" -", e)
sys.exit(1 if errs else 0)
