#!/usr/bin/env python3
"""Honesty checks for research/research-ledger.csv.
 - unverified rows must not carry a verification date;
 - 'Officially verified' rows must name a URL or a source_location, a date and a scope;
 - GitHub (time-sensitive) rows may not be marked verified without the six condition fields filled in;
 - evidence_class must be one of the allowed values."""
import csv, os, sys
p = os.path.join(os.path.dirname(__file__), "..", "research", "research-ledger.csv")
OK = {"Officially verified (docs only)", "Locally tested", "Both officially verified and locally tested",
      "Time-sensitive (unverified)", "Needs re-verification", "Not applicable", "Time-sensitive (verified)"}
errs = []
for r in csv.DictReader(open(p)):
    i, c = r["id"], r["evidence_class"]
    if c not in OK: errs.append(f"{i}: unknown evidence_class {c!r}")
    if c in ("Time-sensitive (unverified)",) and r["date_verified"]: errs.append(f"{i}: unverified row has a date")
    if c.startswith(("Officially verified", "Both")):
        if not (r["url"] or r["source_location"]): errs.append(f"{i}: verified row without source")
        if not r["date_verified"]: errs.append(f"{i}: verified row without date")
        if not r["verification_scope"] or r["verification_scope"] == "none": errs.append(f"{i}: verified row without scope")
    if c == "Time-sensitive (verified)":
        for k in ("account_type", "repo_visibility", "org_context", "permissions", "plan_limitations", "feature_availability"):
            if not r[k] or r[k] == "TO RECORD": errs.append(f"{i}: verified GitHub row missing {k}")
        if not r["url"] or not r["date_verified"]: errs.append(f"{i}: verified GitHub row needs url and date")
print("ledger problems:", len(errs))
for e in errs: print(" -", e)
sys.exit(1 if errs else 0)
