# Chapter 15 solutions

## Level 1
**1.1** (a) untracked (`Untracked files`); (b) staged (`Changes to be committed: new file`); (c) clean (`nothing to commit, working tree clean`); (d) modified (`Changes not staged for commit`).

**1.2** `.git/HEAD` contains `ref: refs/heads/main` (or your branch name). The branch file contains the 40-character hash of the latest commit.

## Level 2
**2.1** Untracked: working tree only. Staged: index (and working tree). Committed: repository (working tree and index match it). Modified after a commit: working tree only.

**2.2** `a.txt` is staged (`Changes to be committed`); `b.txt` is untracked. After `git commit`, `a.txt` is committed and `b.txt` is still untracked.

## Level 3
Any analogy that keeps the three steps apart is right. Example: "Saving is writing on a page; staging is putting the page in the folder that will be posted; committing is posting it, with a label."

## Level 4
**4.1** Saving only changes the working tree. Git records changes only when you stage them into the index (`git add`) and commit them into the repository (`git commit`). Until then the change is not part of any snapshot and could be lost. They should run `git add` for the files they want and then `git commit -m "..."`.

## Level 5
**5.1** The file was modified but not staged, so the index (which defines the commit) held nothing new. Fix: `git add menu.html` and commit again, or use `git commit -am "Update menu"` for tracked files (Chapter 19<!--ref:commits-->).

**5.2** They deleted the repository (the history). The project files (the working tree) still exist. If a copy of the repository exists elsewhere (a clone or a remote), they can restore it from there; otherwise the history is gone and they can start again with `git init`.
