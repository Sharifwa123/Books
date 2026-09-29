#!/usr/bin/env python3
"""Append rows to research/research-ledger.csv from a JSON list on stdin (ids are assigned automatically).
Each entry: {kt, topic, claim, source, cls, scope, local, note, stab, date}. cls in {Not applicable, Locally tested, Needs re-verification, Time-sensitive (unverified)}."""
import csv, json, os, sys
p = os.path.join(os.path.dirname(__file__), "..", "research", "research-ledger.csv")
R = list(csv.DictReader(open(p))); H = list(R[0].keys())
n = max(int(r["id"][1:]) for r in R)
STATUS = {"Not applicable": "N/A: general concept, no product-specific claim", "Locally tested": "LOCALLY TESTED; official source NOT consulted",
          "Needs re-verification": "UNVERIFIED - official source blocked or not yet consulted", "Time-sensitive (unverified)": "UNVERIFIED - time-sensitive; official source blocked"}
out = []
for e in json.load(sys.stdin):
    n += 1; d = dict.fromkeys(H, ""); cls = e["cls"]
    d.update(id=f"R{n:03d}", knowledge_type=e.get("kt", "Stable knowledge"), topic=e["topic"], claim_to_verify=e["claim"], official_source=e.get("source", ""),
             evidence_class=cls, verification_scope=e.get("scope", "none"), local_test_ref=e.get("local", ""), notes=e.get("note", ""),
             stability=e.get("stab", "Stable"), needs_reverification="no" if cls == "Not applicable" else "yes", status=STATUS[cls],
             date_verified=(e.get("date", "2026-09-29") if cls == "Locally tested" else ""))
    if cls.startswith("Time-sensitive"):
        for k in ("account_type", "repo_visibility", "org_context", "permissions", "plan_limitations", "feature_availability"): d[k] = "TO RECORD"
    R.append(d); out.append(d["id"])
w = csv.DictWriter(open(p, "w", newline=""), fieldnames=H); w.writeheader(); w.writerows(R)
print("added", ", ".join(out))
