# Chapter 34 solutions

## Level 1
**1.1** `git switch -c add-tea`, edit and commit, `git push -u origin add-tea`.

**1.2** `origin/add-tea` is new; Bob's own branches did not change, because `fetch` only updates remote-tracking branches.

## Level 2
**2.1** That the change does what the message says, that it touches only what it should, that nothing sensitive is included (Chapter 33<!--ref:gitsec-->), and that it fits the project's style.

**2.2** The graph has a merge commit joining two lines: the branch and `main`.

## Level 3
**3.1** `git push origin --delete add-tea` on the remote; `fetch --prune` removes `origin/add-tea`; `[origin/add-tea: gone]` says that the branch which the local one followed no longer exists on the remote.

**3.2** `git branch -d` succeeds because the branch's commits are contained in `main` (Chapter 21<!--ref:merging-->).

## Level 4
**4.1** An example: every change on a short branch named for its purpose; open a review request when ready; at least one teammate reviews; merge into `main` with `--no-ff` only when tests pass; never commit straight to `main`; delete merged branches; tag `vYYYY.MM.DD` (or a version number) on `main` for each weekly release; hotfixes follow the same rules and are tagged too. Answers vary, as long as they are short and everyone could state them.

## Level 5
**5.1** The branch drifted while `main` moved, so many files changed on both sides. Keep branches short, merge or rebase `main` into the branch often, and split large changes into smaller ones.

**5.2** Protect `main` so that changes arrive only through reviewed merges, and run automated tests before merging (Chapter 54<!--ref:actions-->).

**5.3** Say that the team has no named workflow, and describe what it does in a few lines. Then write those lines down (for example in `CONTRIBUTING.md`) so that the next new person can read them.
