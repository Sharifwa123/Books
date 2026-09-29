#!/usr/bin/env bash
# Git compares bytes: changing only line endings (LF -> CRLF) marks every line as changed;
# a file without a final newline gets the special note in diffs. Isolated from host Git config.
set -u
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_AUTHOR_NAME=T GIT_AUTHOR_EMAIL=t@example.invalid GIT_COMMITTER_NAME=T GIT_COMMITTER_EMAIL=t@example.invalid
W=$(mktemp -d); cd "$W"; git init -q -b main; rc=0
ok(){ echo "PASS  $1"; }; bad(){ echo "FAIL  $1"; rc=1; }
printf 'one\ntwo\n' > f.txt; git add f.txt; git commit -qm base
printf 'one\r\ntwo\r\n' > f.txt
STAT=$(git diff --stat | head -1)
echo "$STAT" | grep -q '4 ++--' && ok "LF->CRLF only: diff --stat reports 2 insertions and 2 deletions ($STAT)" || bad "stat: $STAT"
git diff --quiet && bad "diff should not be empty" || ok "diff is non-empty although visible text is identical"
git checkout -q -- f.txt
printf 'one\ntwo' > f.txt; git add f.txt; git commit -qm nonl
printf 'one\ntwo\n' > f.txt
git diff | grep -q '^\\ No newline at end of file' && ok "missing final newline produces '\\ No newline at end of file'" || bad "no-newline note"
cd /; rm -rf "$W"; exit $rc
