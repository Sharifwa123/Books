#!/usr/bin/env bash
# Run every Git verification with the git on PATH; store results per Git version.
set -u
here=$(cd "$(dirname "$0")" && pwd)
ver=$(git --version | awk '{print $3}')
out="$here/results/git-$ver"; mkdir -p "$out"
echo "Git $ver -> $out"
"$here/verify-git-basics.sh"       > "$out/basics.txt" 2>&1
"$here/verify-config-and-lfs.sh"   > "$out/config-and-lfs.txt" 2>&1
"$here/verify-investigations.sh"   > "$out/investigations.txt" 2>&1
# docs check must point at THAT version's docs (DOCS=... env); skipped if not provided
if [ -n "${DOCS:-}" ]; then python3 "$here/verify-against-docs.py" > "$out/docs.txt" 2>&1; else echo "DOCS not set: docs check skipped" > "$out/docs.txt"; fi
for f in basics config-and-lfs investigations docs; do
  printf "%-16s PASS=%s FAIL=%s\n" "$f" "$(grep -cE '^(PASS|OBSERVED)' "$out/$f.txt")" "$(grep -c '^FAIL ' "$out/$f.txt")"
done
