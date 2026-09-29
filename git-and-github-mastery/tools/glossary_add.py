#!/usr/bin/env python3
"""Append entries to glossary/glossary-master.csv from a JSON list on stdin.
Each entry: {term, simple, technical, example, related, first}. Refuses duplicates (case-insensitive)."""
import csv, json, os, sys
p = os.path.join(os.path.dirname(__file__), "..", "glossary", "glossary-master.csv")
rows = list(csv.DictReader(open(p)))
have = {r["term"].lower() for r in rows}
new = json.load(sys.stdin)
with open(p, "a", newline="") as f:
    w = csv.writer(f)
    for e in new:
        if e["term"].lower() in have: print("SKIP duplicate:", e["term"]); continue
        w.writerow([e["term"], e["simple"], e["technical"], e["example"], e["related"], e["first"]]); have.add(e["term"].lower())
print("glossary entries:", len(have))
