# Appendix K — Git Recovery Decision Tree

Start at the top and answer each question honestly. Every leaf names the chapter that has the recorded steps. **Before any move that changes history, make a safety branch: `git branch backup`.** Read the state first: `git status`, `git log --oneline --graph --all`.

```text
Something went wrong. What is it?
|
+-- A command printed an error message
|     -> look it up in Appendix C, then Chapter 78<!--ref:trouble-->
|
+-- I lost work
|     |
|     +-- I never committed it (only edited)
|     |     -> it may still be in the editor's history or a stash: `git stash list`; otherwise it cannot be recovered by Git
|     |
|     +-- I committed it, then moved or deleted the branch or ran reset --hard
|     |     -> `git reflog`, find the commit, `git branch rescue COMMIT`   (Chapter 26<!--ref:reflog-->, Chapter 79<!--ref:playbooks-->)
|     |
|     +-- I deleted a branch and the reflog does not show it
|           -> `git fsck --lost-found` lists unreachable commits   (Chapter 30<!--ref:objects-->, Chapter 80<!--ref:challenges-->)
|
+-- I made a mistake in a commit
|     |
|     +-- not pushed yet
|     |     +-- last commit only -> `git commit --amend`   (Chapter 25<!--ref:undo-->)
|     |     +-- several messy commits -> `git reset --soft BASE` and commit again   (Chapter 76<!--ref:scenarios-->)
|     |
|     +-- already pushed, others may have it
|           -> `git revert COMMIT` (for a merge: `-m 1`), then push   (Chapter 25<!--ref:undo-->, Chapter 79<!--ref:playbooks-->)
|
+-- I am in the middle of something
|     +-- merge with conflicts   -> resolve, `git add`, `git commit`; or `git merge --abort`   (Chapter 22<!--ref:conflicts-->)
|     +-- rebase stopped         -> resolve and `--continue`, or `git rebase --abort`   (Chapter 79<!--ref:playbooks-->)
|     +-- cherry-pick or am stopped -> `--abort` restores the state before   (Chapter 28<!--ref:tools-->)
|     +-- detached HEAD          -> `git switch -c NAME` to keep commits, or `git switch main`   (Chapter 78<!--ref:trouble-->)
|
+-- I committed on the wrong branch
|     -> `git branch NEW`, then `git reset --hard origin/BRANCH` on the wrong one   (Chapter 79<!--ref:playbooks-->)
|
+-- A push was rejected
|     -> `git fetch`, read `git log main..origin/main`, merge or rebase, push   (Chapter 23<!--ref:remotes-->, Chapter 78<!--ref:trouble-->)
|        never `--force` on a shared branch; use `--force-with-lease` only on your own
|
+-- A secret was committed
      |
      +-- not pushed -> drop the commits or rewrite locally; still revoke if it was ever shared   (Chapter 33<!--ref:gitsec-->)
      +-- pushed -> REVOKE the secret first; then decide whether a history rewrite is worth it   (Chapter 79<!--ref:playbooks-->)
```

## K.1 Rules that hold at every leaf

1. Revoke a leaked secret before anything else.
2. Prefer undoing forwards (revert, a new commit) to rewriting when others have the commits.
3. Tell your team before you rewrite shared history.
4. After any recovery, run `git status` and `git log --oneline --graph --all` to confirm the result.
