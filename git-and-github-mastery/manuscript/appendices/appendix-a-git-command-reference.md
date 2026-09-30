# Appendix A — Git Command Reference

This appendix lists the Git commands used in the book, with one line each and the chapter where each is taught. Every command here appeared in a recorded session in the chapter named. **Options change between Git versions**: the book was recorded on Git 2.43.0 and re-run on newer versions in CI; for anything else, use `git help COMMAND`. Commands are grouped by task. "Safe" means the command does not destroy uncommitted work or rewrite shared history; "Careful" means it can.

## Set-up and configuration

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git --version` | prints the installed version | safe | 13<!--ref:install--> |
| `git config --global user.name "N"` and `user.email "E"` | sets who you are for commits | safe | 14<!--ref:config--> |
| `git config --list --show-origin` | shows every setting and its file | safe | 14<!--ref:config--> |
| `git config --local KEY VALUE` | sets a value for one repository | safe | 14<!--ref:config--> |
| `git help COMMAND` | opens the manual page | safe | 35<!--ref:readdocs--> |
| `git config alias.NAME "..."` | makes a shortcut | safe | 32<!--ref:custom--> |

## Starting and copying

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git init` | makes a repository in the current folder | safe | 16<!--ref:firstrepo--> |
| `git init --bare` | makes a repository with no working files (a shared "remote") | safe | 23<!--ref:remotes--> |
| `git clone URL [DIR]` | copies a repository, with its history | safe | 23<!--ref:remotes--> |
| `git clone --depth 1 file://PATH` | copies only the latest commit | safe | 31<!--ref:bigrepos--> |
| `git sparse-checkout set DIR` | checks out only some folders | safe | 31<!--ref:bigrepos--> |

## Looking

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git status` (`-s`, `-sb`) | shows what changed and the branch | safe | 18<!--ref:tracking--> |
| `git log` (`--oneline`, `--graph`, `--all`, `--format=...`) | shows history | safe | 17<!--ref:history_view--> |
| `git log -S'text'` | finds commits that add or remove text | safe | 17<!--ref:history_view--> |
| `git diff` (`--staged`, `A..B`, `A...B`, `--stat`) | shows differences | safe | 17<!--ref:history_view--> |
| `git show REV` (`REV:PATH`) | shows one commit or one file at a commit | safe | 17<!--ref:history_view--> |
| `git blame FILE` | shows who last changed each line | safe | 17<!--ref:history_view--> |
| `git shortlog -sn` | counts commits per author | safe | 51<!--ref:insights--> |
| `git grep PATTERN` | searches tracked files | safe | 17<!--ref:history_view--> |
| `git describe --tags` | names a commit by the nearest tag | safe | 29<!--ref:tags--> |
| `git ls-files` | lists tracked files | safe | 18<!--ref:tracking--> |

## Recording changes

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git add PATH` (`-A`) | stages changes | safe | 19<!--ref:commits--> |
| `git commit -m "msg"` (`-a`, `-s`, `--amend`) | records staged changes | amend is careful | 19<!--ref:commits--> |
| `git rm PATH` (`--cached`) | removes a file (or stops tracking it) | careful | 18<!--ref:tracking--> |
| `git mv OLD NEW` | renames a tracked file | safe | 18<!--ref:tracking--> |
| `git restore PATH` (`--staged`) | discards changes or unstages | discarding is careful | 25<!--ref:undo--> |

## Branches and merging

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git branch` (`-a`, `-vv`, `-d`, `-D`) | lists, creates or deletes branches | `-D` is careful | 20<!--ref:branching--> |
| `git switch BRANCH` (`-c` to create, `--detach`) | changes branch | safe | 20<!--ref:branching--> |
| `git merge BRANCH` (`--no-ff`, `--ff-only`, `--squash`, `--abort`) | joins branches | safe until you commit | 21<!--ref:merging--> |
| `git checkout --ours FILE` | takes your side in a conflict | careful | 22<!--ref:conflicts--> |
| `git rebase BRANCH` (`--abort`, `--continue`) | replays commits on another base | rewrites | 27<!--ref:rebase--> |
| `git cherry-pick -x COMMIT` | copies a commit | safe | 27<!--ref:rebase--> |
| `git stash push -m "msg"`, `git stash pop`, `git stash list` | sets work aside | safe | 24<!--ref:stash--> |
| `git worktree add PATH BRANCH` | a second working folder | safe | 31<!--ref:bigrepos--> |

## Working with remotes

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git remote -v`, `add`, `set-url` | manages remotes | safe | 23<!--ref:remotes--> |
| `git fetch` (`--prune`) | downloads without merging | safe | 23<!--ref:remotes--> |
| `git pull` (`--ff-only`, `--rebase`, `--no-rebase`) | fetch then merge or rebase | can merge | 23<!--ref:remotes--> |
| `git push` (`-u`, `--tags`, `--delete`) | uploads | safe if not forced | 23<!--ref:remotes--> |
| `git push --force-with-lease` | uploads over a moved branch, if it is still what you saw | careful | 27<!--ref:rebase--> |
| `git push --force --mirror` | overwrites every ref on the remote | dangerous | 79<!--ref:playbooks--> |
| `git ls-remote` | lists refs on a remote | safe | 23<!--ref:remotes--> |

## Undoing and recovering

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git revert COMMIT` (`-m 1` for merges) | makes a commit that undoes another | safe | 25<!--ref:undo--> |
| `git reset --soft`, `--mixed`, `--hard` | moves the branch, optionally changing the index and files | `--hard` is dangerous | 25<!--ref:undo--> |
| `git reflog` | lists where `HEAD` has been | safe | 26<!--ref:reflog--> |
| `git bisect start`, `good`, `bad`, `run`, `reset` | finds the commit that broke something | safe | 28<!--ref:tools--> |
| `git fsck --lost-found` | finds unreachable objects | safe | 30<!--ref:objects--> |
| `git clean -n` then `-fd` | removes untracked files | `-fd` is dangerous | 78<!--ref:trouble--> |

## Tags, releases and archives

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git tag -a NAME -m "msg"`, `git tag -n1`, `--sort=version:refname` | annotated tags | safe | 29<!--ref:tags--> |
| `git archive --prefix=P/ -o FILE REV` | makes an archive without history | safe | 66<!--ref:releases--> |

## Inside Git and other tools

| Command | What it does | Safety | Chapter |
|---|---|---|---|
| `git cat-file -t|-p OBJECT`, `git hash-object` | look at objects | safe | 30<!--ref:objects--> |
| `git gc`, `git maintenance` | tidy storage | careful with `--prune` | 30<!--ref:objects-->, 32<!--ref:custom--> |
| `git submodule add|update` | nested repositories | careful | 31<!--ref:bigrepos--> |
| `git subtree` | nested history in a folder | careful | 31<!--ref:bigrepos--> |
| `git lfs track` | large-file support (separate tool) | safe | 31<!--ref:bigrepos--> |
| `git filter-repo` | rewrites history (separate tool) | dangerous | 33<!--ref:gitsec-->, 79<!--ref:playbooks--> |
| `git format-patch`, `git am`, `git apply` | patches as files | safe (`am` can conflict) | 28<!--ref:tools--> |
| `git check-ref-format --branch NAME` | tests a branch name | safe | 20<!--ref:branching--> |
| `git interpret-trailers`, `--format='%(trailers:...)'` | reads message trailers | safe | 64<!--ref:oss--> |
| `git commit -S`, `git verify-commit` | signed commits | safe | 33<!--ref:gitsec--> |
