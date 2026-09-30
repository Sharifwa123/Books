# Chapter 78 solutions

## Level 1
**1.1** Read the first and last lines; run `git status`; do not run the first fix you find; look before you change anything; make a safety copy when in doubt; change one thing at a time.

**1.2** (a) Git found no repository in this folder or its parents. (b) Git has no name and email to record. (c) The two histories share no commit. (d) Another Git process is running or left a lock file.

## Level 2
**2.1** Any three from the handbook; for each show the message, and the safe fix (for example `git config --global user.name ...` for the identity error).

**2.2** After a merge fix the history has a merge commit; after a rebase fix it is linear. Both leave the remote with all commits; the rebase rewrites only your unpushed commits.

## Level 3
**3.1** Answers vary; a good entry has message, meaning, cause, diagnosis, safe fix, dangerous fix, prevention, and a recording.

**3.2** `checkout -f`: destructive (throws away uncommitted changes). `stash`: safe. `push --force-with-lease`: risky but safer than `--force`; only on your own branch. `branch -d`: safe (refuses if unmerged). `clean -fd`: destructive (deletes untracked files and folders); use `-n` first to preview.

## Level 4
**4.1** "`--force` overwrites the remote branch with your version, so commits that only the remote had are no longer on the branch. Ana's commits still exist in her clone and possibly in the remote's reflog; she can push them back from her clone, or you can recover them from the reflog. In future, fetch and merge or rebase instead of forcing, and protect `main` so that force pushes are blocked."

## Level 5
**5.1** `.gitignore` does not affect files that are already tracked. Run `git rm --cached notes.txt` and commit; the file stays on disk.

**5.2** Create a branch at your current position: `git switch -c keep-my-work`. The commits are then on that branch.
