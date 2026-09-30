# Chapter 45 solutions

## Level 1
**1.1** The base branch is where the change is going (usually `main`); the compare branch is the topic branch that holds the commits.

**1.2** The three-dot form (`main...add-tea`) shows only the line the branch added. The two-dot form also shows the change made on `main`, reversed.

## Level 2
**2.1** Merge: two topic commits plus a merge commit, joined. Squash: one new commit, the topic commits absent. Rebase: two commits in a straight line after the other change on the base.

**2.2** A commit's hash covers its parent, so putting the commits on a new base gives them new hashes (Chapter 27<!--ref:rebase-->).

## Level 3
**3.1** `git init --bare hub.git`; push a branch; `git -C hub.git update-ref refs/pull/1/head <commit>`; then in a clone `git fetch origin pull/1/head:pr-1` and `git switch pr-1`.

**3.2** `git -C hub.git config receive.hideRefs refs/pull`, then `git push origin HEAD:refs/pull/1/head` prints `! [remote rejected] HEAD -> refs/pull/1/head (deny updating a hidden ref)`.

## Level 4
**4.1** Squash and merge: many noisy commits become one. The risk (from the documentation) is that if the contributor keeps working on the same head branch, later pull requests can include commits already squashed into the base, causing repeated conflicts; start the next change from a fresh branch off the updated base.

## Level 5
**5.1** A two-dot diff compares the two tips, so it includes changes made on the base after the branch diverged. The page shows the three-dot comparison: `git diff main...topic`.

**5.2** Revert the pull request (the platform creates a new pull request that reverts the merge commit), or revert commits yourself with `git revert` (with `-m 1` for a merge commit). Prefer the command line when the platform's revert conflicts or the pull request was not merged on the platform.
