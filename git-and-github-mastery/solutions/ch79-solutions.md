# Chapter 79 solutions

## Level 1
**1.1** Revoke the key; stop tracking the file; rewrite history (only if needed); tell colleagues to discard their clones and clone again.

**1.2** Playbook 2. `HEAD@{1}` is where `HEAD` pointed before the most recent move, here the tip before the reset.

## Level 2
**2.1** After `git reset --hard HEAD~2` the log lacks the two commits; `git reflog` lists them; `git reset --hard 'HEAD@{1}'` restores them.

**2.2** `git branch NEW`, then `git reset --hard origin/main`; the log of `main` lacks the commit and the log of `NEW` has it.

## Level 3
**3.1** The revert removes the branch's changes, but a second merge of the same branch brings none of them back, because Git regards the branch's earlier commits as merged. The way out is to revert the revert first (Git's howto "Revert a faulty merge").

**3.2** After the abort the branch is as before; after `--continue` the branch's commit sits on top of `main` with a linear history.

## Level 4
**4.1** A good report has: timeline (pushed Monday, found Wednesday); revoke and rotate first, and check the service's logs for use in that period; stop tracking and ignore; decide whether to rewrite (large effort, incomplete: clones, forks, cached views, pull requests); if so, coordinate, force-push, ask everyone to re-clone, contact Support for cached views; prevention with push protection and secret scanning.

## Level 5
**5.1** Their old clone still has the old commits. `git pull` merged the old history with the new, and `git push` sent the old commits back. They should have discarded the clone and cloned again.

**5.2** The reflog entry index was not the one you thought (use `git reflog` and pick the right entry); the commits were never committed (only edited); the reflog entries expired or were pruned; you are in another clone.
