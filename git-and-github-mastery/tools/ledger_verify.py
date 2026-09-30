#!/usr/bin/env python3
"""Update existing research-ledger rows after checking them against an official source.
Reads a JSON list on stdin. Each entry: {id, cls, url, scope, local?, docs?, note?, reverify?}
cls is 'docs' (Officially verified (docs only)), 'both' (Both officially verified and locally tested) or
'local' (Locally tested). url is the source(s), recorded in the url column; the hash of each fetched file is in
research/sources-manifest.csv."""
import csv, json, os, sys, time
p = os.path.join(os.path.dirname(__file__), "..", "research", "research-ledger.csv")
R = list(csv.DictReader(open(p))); H = list(R[0].keys())
by = {r["id"]: r for r in R}
CLS = {"docs": ("Officially verified (docs only)", "VERIFIED against official source text (fetched copy hashed in research/sources-manifest.csv)"),
       "both": ("Both officially verified and locally tested", "VERIFIED against official source text and locally tested"),
       "local": ("Locally tested", "LOCALLY TESTED; official source NOT consulted")}
today = time.strftime("%Y-%m-%d", time.gmtime())
entries = json.load(sys.stdin)
for e in entries:
    r = by[e["id"]]; c, st = CLS[e["cls"]]
    r["evidence_class"] = c; r["status"] = st; r["date_verified"] = today
    r["url"] = e["url"]; r["verification_scope"] = e["scope"]
    if e.get("local"): r["local_test_ref"] = (r["local_test_ref"] + "; " if r["local_test_ref"] else "") + e["local"]
    if e.get("docs"): r["docs_check_ref"] = e["docs"]
    if e.get("note"): r["notes"] = e["note"]
    r["needs_reverification"] = "yes" if e.get("reverify") else "no"
    if e["cls"] != "local" and r.get("source_location", "") == "": r["source_location"] = "official source repository via raw.githubusercontent.com"
w = csv.DictWriter(open(p, "w", newline=""), fieldnames=H); w.writeheader(); w.writerows(R)
print("updated", len(entries), "rows")
