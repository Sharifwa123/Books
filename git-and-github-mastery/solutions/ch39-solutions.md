# Chapter 39 solutions

## Level 1
**1.1** `warning: You appear to have cloned an empty repository.` The remote has no commits yet.

**1.2** `main` follows `origin/main`, and neither is ahead of the other: they are in sync.

## Level 2
**2.1** `ls-remote` shows the hash of the remote's `main`; it equals `git rev-parse main` when the push succeeded.

**2.2** An empty remote has no commit that yours lacks, so the push is a plain fast-forward from nothing. A remote with its own first commit has a history that yours does not contain.

## Level 3
**3.1** `! [rejected] main -> main (fetch first)`, with advice to pull first.

**3.2** The first pull says `fatal: refusing to merge unrelated histories`; with `--allow-unrelated-histories` Git creates a merge commit. The graph has two roots joined by the merge commit, and the push then succeeds.

## Level 4
**4.1** Git steps: `branch -M`, `remote add`, `push -u`, `clone`, `fetch`, `pull`. Platform steps: creating the empty repository, choosing visibility, signing in, and looking at the web page.

## Level 5
**5.1** `rejected ... (fetch first)`, then `refusing to merge unrelated histories` on a plain pull. Either pull with `--allow-unrelated-histories` and push, or (if nothing valuable is on the platform yet) start again with an empty hosted repository.

**5.2** The push may have failed (read its output), or the web page shows a different branch, or the page is cached; check `git ls-remote` and the branch selector.

**5.3** Revoke or change the password first; the file stays in history even if it is removed later (Chapter 33<!--ref:gitsec-->). Then consider making the repository private and rewriting history.
