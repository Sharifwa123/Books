# Chapter 31 solutions

## Level 1
**1.1** Two lines: the original folder on `main` and the new folder on `hotfix`, both at the same commit.

**1.2** The graph shows the new commit on `hotfix`, ahead of `main`: one shared history.

## Level 2
**2.1** Yes: removing a worktree removes the folder, not the branch.

**2.2** One commit, marked `grafted`.

## Level 3
**3.1** After `--unshallow` all commits appear; `--is-shallow-repository` changes from `true` to `false`.

**3.2** After `set docs`, `ls` shows `docs` and the top-level files but not `src`; after `disable`, `src` is back.

## Level 4
**4.1** Three lines: `version`, `oid sha256:...` and `size`. The real file is stored by LFS outside the normal history.

**4.2** Git prints `fatal: transport 'file' not allowed`. The override is for one command in a controlled demonstration; a permanent setting would remove a protection against malicious repositories reading local files.

## Level 5
**5.1** Run `git worktree prune`, which removes records of worktree folders that no longer exist. (This command was not run for the book; check `git worktree --help`.) Next time, use `git worktree remove`.

**5.2** The history was cut off at the shallow boundary; `blame` cannot see beyond it. Run `git fetch --unshallow`.

**5.3** The video was already committed, and it stays in the history; LFS only handles files committed after tracking begins.
