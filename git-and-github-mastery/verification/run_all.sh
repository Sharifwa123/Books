#!/usr/bin/env bash
# Re-run every recorded chapter transcript in the named shell and compare with the expected output.
# Layout: verification/<chapter>/session-<name>.txt  +  expected-<name>.<shell>.txt
set -u
cd "$(dirname "$0")"
rc=0; n=0
for exp in */expected-*.bash.txt */expected-*.zsh.txt; do
  [ -f "$exp" ] || continue
  dir=$(dirname "$exp"); base=$(basename "$exp" .txt); base=${base#expected-}
  shell=${base##*.}; name=${base%.*}
  if ! command -v "$shell" >/dev/null 2>&1; then echo "SKIP  $exp ($shell not installed)"; continue; fi
  n=$((n+1))
  python3 ../tools/run_session.py "$shell" "$dir/session-$name.txt" --check "$exp" || { echo "FAIL  $exp"; rc=1; }
done
echo "transcripts checked: $n"
[ -f ch08-markdown/render_check.py ] && { python3 ch08-markdown/render_check.py || rc=1; }
exit $rc
