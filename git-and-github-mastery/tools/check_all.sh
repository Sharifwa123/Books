#!/usr/bin/env bash
# Run every static check. Fails if generated planning files are stale.
set -u
cd "$(dirname "$0")/.."
rc=0
python3 tools/build_planning.py || rc=1
if ! git diff --quiet -- planning; then echo "STALE: generated planning files differ from committed (run tools/build_planning.py and commit)"; git --no-pager diff --stat -- planning; rc=1; fi
for c in check_refs resolve_refs check_transcripts check_md_examples check_links check_ledger check_secrets check_manuscript; do
  [ -f tools/$c.py ] || continue
  echo "== $c"; python3 tools/$c.py || rc=1
done
exit $rc
