# Chapter 20 solutions

## Level 1
**1.1** The graph shows `add-tea` one commit ahead of `main`, with `HEAD -> add-tea`.

**1.2** On `main` there is no tea line; on `add-tea` there is. Git rewrites the working tree to match the branch you switch to.

## Level 2
**2.1** `git switch -c fix-typo`, `git branch -m fix-typo tidy-menu`, `git switch main`, `git branch -d tidy-menu`. It succeeded because `tidy-menu` had no commits of its own.

**2.2** It refuses because `add-tea` has a commit that no other branch contains; deleting it would leave that commit unreachable.

**2.3** `feature/add-tea` works; `bad name` fails with `fatal: 'bad name' is not a valid branch name`.

## Level 3
`git switch -c add-hours-page`, create and commit `hours.html`, `git switch main`, `ls` (no `hours.html`), `git switch add-hours-page`, `ls` (present).

## Level 4
**4.1** `git branch -a` and `git log --oneline --all --graph` to see all branches and commits; `git reflog` to see where `HEAD` has been. Likely explanations: the commits are on another branch (switch to it), or they were made in a detached HEAD and are on no branch (create a branch at the commit's hash before doing anything else).

## Level 5
**5.1** Safe: commit the changes (they become part of the current branch); or `git stash` them and `git stash pop` after switching. Unsafe: discarding them with a forced checkout or `git restore .`, which permanently loses the uncommitted edit.

**5.2** The commits exist but belong to no branch, so they are unreachable except through the reflog. The learner should have created a branch (`git switch -c rescue`) before switching away. Recover with `git reflog`, find the hash, and `git branch rescue <hash>` (Chapter 26<!--ref:reflog-->).

**5.3** Git printed `Deleted branch experiment (was <hash>)`. That hash is the tip of the deleted branch, and `git branch experiment <hash>` recreates it, as long as the commit has not been cleaned up (Chapter 26<!--ref:reflog-->).
