# Chapter 33 solutions

## Level 1
**1.1** `git show HEAD~1:.env` prints `API_KEY=not-a-real-key`. The deleting commit did not remove it from the earlier commit.

**1.2** It lists the commit that added the key and the commit that removed it, because `-S` finds commits that change the number of occurrences of the text.

## Level 2
**2.1** `git status --short` does not list `.env`; `git check-ignore -v .env` prints the file, line and pattern of the rule that ignores it.

**2.2** A plain `git add` refuses with a hint; `git add -f` stages the file anyway. `.gitignore` guards against accidents only; it does not stop anyone who forces.

## Level 3
**3.1** Both commits that touched `.env` were removed, and the commits that came after them (if any) got new hashes; earlier commits keep their hashes.

**3.2** Copies that other people already have (clones, forks, downloads), copies held by a hosting platform (caches, pull requests), and the fact that the secret itself is still valid.

## Level 4
**4.1** 1) Revoke the token. 2) Check the service's logs for misuse. 3) Tell the team (following your organization's rules). 4) Rewrite history if needed, agreed with everyone who shares the repository. 5) Add a prevention. Revoking comes first because it is the only step that makes the leaked value useless.

**4.2** `gpg --batch --passphrase '' --quick-gen-key "Name <email>" default default never`, `git config user.signingkey <email>`, `git commit -S`, and `git log --format='%G? %s'` shows `G` for the signed commit and `N` for the unsigned one.

## Level 5
**5.1** Deleting a file adds a commit; the secret stays in the earlier commit and on the remote. First revoke or rotate the secret; then consider a rewrite.

**5.2** Their local branch still has the old commits, and the remote now has different ones with the same content, so Git sees diverged histories. They must not simply merge or force-push the old history back; they should agree with the team how to reset their branch to the new history.

**5.3** A `G` shows that the commit was signed with a key that Git could check, and that the commit was not changed afterwards. It does not show that the person is trustworthy or that the code is safe.
