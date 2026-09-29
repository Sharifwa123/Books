#!/usr/bin/env bash
# Config scopes / environment influence / rebase todo help text / Git LFS basics — executed in isolation.
# Records the Git version. Each block prints PASS/FAIL. Needs git-lfs installed for the LFS block (else SKIP).
set -u
unset GIT_CONFIG_GLOBAL GIT_CONFIG_SYSTEM   # set explicitly per test below
W=$(mktemp -d); cd "$W"
ok(){ echo "PASS  $1"; }; bad(){ echo "FAIL  $1"; }
chk(){ if eval "$2" >/dev/null 2>&1; then ok "$1"; else bad "$1"; fi; }
echo "git version: $(git --version)"
export GIT_AUTHOR_NAME=T GIT_AUTHOR_EMAIL=t@example.invalid GIT_COMMITTER_NAME=T GIT_COMMITTER_EMAIL=t@example.invalid

# --- isolated scopes: point system and global at files we control
SYS="$W/sys.gitconfig"; GLO="$W/glo.gitconfig"; : > "$SYS"; : > "$GLO"
export GIT_CONFIG_SYSTEM="$SYS" GIT_CONFIG_GLOBAL="$GLO"
git init -q -b main repo && cd repo
git config --system demo.level system; git config --global demo.level global
chk "global overrides system" '[ "$(git config demo.level)" = global ]'
git config --local demo.level local
chk "local overrides global" '[ "$(git config demo.level)" = local ]'
chk "--show-scope reports local as winner" 'git config --show-scope --get demo.level | grep -q "^local"'
chk "--get-all lists all three values in order" '[ "$(git config --get-all demo.level | tr "\n" ,)" = "system,global,local," ]'
chk "--show-origin shows file path" 'git config --show-origin --get demo.level | grep -q "file:"'
git config extensions.worktreeConfig true; git config --worktree demo.level worktree
chk "worktree scope overrides local (with extensions.worktreeConfig)" '[ "$(git config demo.level)" = worktree ]'
chk "--show-scope reports worktree" 'git config --show-scope --get demo.level | grep -q "^worktree"'
# includeIf
echo "[demo]
  included = yes" > "$W/work.gitconfig"
git config --global includeIf."gitdir:$W/repo/".path "$W/work.gitconfig"
chk "includeIf gitdir applies inside matching repo" '[ "$(git config demo.included)" = yes ]'
# environment can change behaviour
git config --global commit.gpgsign true; git config --global gpg.format ssh; git config --global gpg.ssh.program /bin/false
echo x > f; git add f
chk "inherited commit.gpgsign=true makes a plain commit FAIL when signer is broken" '! git commit -qm test'
chk "-c commit.gpgsign=false overrides for one command" 'git -c commit.gpgsign=false commit -qm test'
chk "GIT_CONFIG_GLOBAL=/dev/null isolates from global" '[ -z "$(GIT_CONFIG_GLOBAL=/dev/null git config commit.gpgsign)" ]'
git config --system demo.sysonly yes
chk "system-only key is visible normally" '[ "$(git config demo.sysonly)" = yes ]'
chk "GIT_CONFIG_NOSYSTEM=1 hides the system scope (even when GIT_CONFIG_SYSTEM is set)" '[ -z "$(GIT_CONFIG_NOSYSTEM=1 git config demo.sysonly)" ]'
# --- rebase todo help text lists commands (runtime evidence, independent of docs prose)
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
git commit -q --allow-empty -m a; git commit -q --allow-empty -m b; git commit -q --allow-empty -m c
TODO=$(GIT_SEQUENCE_EDITOR='cat' git rebase -i HEAD~2 2>&1; git rebase --abort 2>/dev/null)
for c in pick reword edit squash fixup exec break drop label reset merge; do
  chk "rebase -i todo help mentions '$c'" 'echo "$TODO" | grep -qE "^# ?(#? )?[a-z], $c|# $c <|# $c"'
done
# --- Git LFS
if git lfs version >/dev/null 2>&1; then
  echo "LFS: $(git lfs version)"
  cd "$W" && git init -q -b main lfsrepo && cd lfsrepo
  chk "lfs install --local" 'git lfs install --local'
  chk "lfs track adds .gitattributes line" 'git lfs track "*.psd" && grep -q "filter=lfs" .gitattributes'
  head -c 2048 /dev/urandom > design.psd; git add .gitattributes design.psd; git commit -qm lfs
  chk "committed blob is a small LFS pointer" '[ "$(git cat-file -p HEAD:design.psd | head -1)" = "version https://git-lfs.github.com/spec/v1" ]'
  chk "lfs ls-files lists tracked file" 'git lfs ls-files | grep -q design.psd'
else echo "SKIP  git-lfs not installed"; fi
cd /; rm -rf "$W"
