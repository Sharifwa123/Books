# Chapter 14 solutions

## Level 1
**1.1** Something like `global	file:/home/you/.gitconfig	you@example.org`.

**1.2** `git config user.email` prints `lab@example.org`; `git config --get-all user.email` prints your global address first, then `lab@example.org`.

**1.3** The first prints `temp@example.invalid`; the second prints the stored value. `-c` changes nothing on disk.

## Level 2
**2.1** After `git config --local --unset user.email`, the global value is effective again. When no value exists at any scope, the command prints nothing and its exit code is 1.

**2.2** With the global file replaced by nothing, there is no `user.email` unless a local one exists, so the command prints nothing (exit code 1) if the repository has none.

## Level 3
A working configuration: `git config --global includeIf.gitdir:~/work/.path ~/.gitconfig-work` with `~/.gitconfig-work` containing a `[user]` section with the work email. In a repository under `~/work/`, `git config --show-origin user.email` names `.gitconfig-work`; elsewhere it names `.gitconfig`.

## Level 4
**4.1** Compare the settings that the two machines actually use: on each, `git config --list --show-origin --show-scope` (or `--get-all` for a name), and look at `commit.gpgsign`, `gpg.format`, `user.signingkey`. Change the setting at the *narrowest scope that affects only the build server*: its system file or the local `.git/config` of the build repository, not your global file.

## Level 5
**5.1** (1) `git config --show-origin --get commit.gpgsign` to see whether signing is on and where it is set; (2) `git config --list --show-origin --show-scope | grep -i -E "gpg|sign"` for related settings; (3) check whether a system or included file sets it. Safest way to commit meanwhile: `git -c commit.gpgsign=false commit -m "Update"`, which changes nothing on disk.

**5.2** The `pull.*` settings (`pull.rebase`, `pull.ff`); compare with `git config --show-origin --get-all pull.rebase` and `pull.ff` on both computers.

**5.3** Any of `commit.gpgsign`, `user.name`/`user.email`, `core.editor`, `init.defaultBranch`, `core.autocrlf`. Make the script explicit: pass `-c` options for what it needs, set `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1` so that no inherited settings apply, and supply the identity itself.
