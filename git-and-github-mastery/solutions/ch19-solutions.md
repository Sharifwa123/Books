# Chapter 19 solutions

## Level 1
**1.1** Before: `... stuff`; after: `... Add the lemon tart to the menu`; the hash is different because the message is part of what the hash is calculated from.

**1.2** `git show --stat --oneline HEAD` lists both `menu.md` and `notes.txt` under one commit.

## Level 2
**2.1** `git add menu.md && git commit -m "Raise the price of rolls"`, then `git add hours.md && git commit -m "Add the opening hours"`. The stat shows one file per commit.

**2.2** `git commit --allow-empty -m "Subject" -m "Body paragraph"` (or with a real change). A blank line separates subject from body.

**2.3** `git commit --author="Grace Baker <grace@example.net>" -m "..."`; the fuller format shows `Author:` and `Commit:` as different people.

## Level 3
**3.1** Sample rewrites: `Fix the broken link to the menu page`; `Add a draft of the weekend menu`; `Raise the price of rolls to 3.20`; `Correct the address on the contact page`; `Add the coconut cake to the menu` (and a separate commit for the CSS change, since the original mixes two things).

## Level 4
**4.1** A good proposal: subject in the imperative, about 50 characters, body explains why; one logical change per commit; review with `git status` and `git diff --staged`; amend only unshared commits; do not commit secrets or generated files. Git rules: the structure (first line/body separation matters to tools), that amend creates a new commit. Conventions: length, tense, footer format, the definition of "logical change".

## Level 5
**5.1** Amend created a new commit with a different hash. The colleague still has the old one, so the two histories now diverge from the same starting point. Advice: do not rewrite shared commits; if it has happened, tell the colleague and agree which version is kept (Chapter 23<!--ref:remotes--> and Chapter 27<!--ref:rebase-->).

**5.2** `git reflog` lists the old commit, and `git show <old-hash>` shows it. Chapter 26<!--ref:reflog--> shows how to recover it.

**5.3** `-a` stages every change to every tracked file, including the unrelated one. Avoid it by staging only what belongs (`git add <file>`) and checking `git status` and `git diff --staged` before committing.
