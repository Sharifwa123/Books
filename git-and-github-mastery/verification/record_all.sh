#!/usr/bin/env bash
# Re-record every session transcript (both shells) with the tools installed here. Review `git diff` afterwards:
# any change in recorded output must be understood before it is committed.
set -u
cd "$(dirname "$0")"
for sess in */session-*.txt; do
  dir=$(dirname "$sess"); name=$(basename "$sess" .txt); name=${name#session-}
  for shell in bash zsh; do
    command -v "$shell" >/dev/null || { echo "skip $shell"; continue; }
    python3 ../tools/run_session.py "$shell" "$sess" > "$dir/expected-$name.$shell.txt"
  done
done
echo "recorded $(ls */expected-*.txt | wc -l) files"
