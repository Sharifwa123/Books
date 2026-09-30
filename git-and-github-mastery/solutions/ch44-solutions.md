# Chapter 44 solutions

## Level 1
**1.1** `git ls-files .github` prints `.github/ISSUE_TEMPLATE/bug.yml`.

**1.2** A title that states the problem; what you did, expected and saw; where; and evidence (with no secrets).

## Level 2
**2.1** `git commit -am "Change" -m "Fixes #12"` stores the words in the message; `git log --oneline --grep='#12'` lists the commit.

**2.2** `Fixes octo-org/octo-repo#100`.

## Level 3
**3.1** For example: "Rolls price is 3.00 in menu.md but 3.20 in the shop page".

**3.2** For example `bug`, `documentation`, `question`. Few labels stay meaningful, and everybody uses them the same way.

## Level 4
**4.1** Answers vary. A bug form might have: what happened (required textarea), what you expected (required textarea), version (input), and a checkbox confirming that no secrets are included. A question form might have just the question and what you have already tried.

## Level 5
**5.1** The pull request may not have targeted the default branch (keywords are ignored for other branches); or the keyword was not in a supported form or was not followed by a valid issue reference.

**5.2** Issue templates must be on the default branch; a template on another branch is not available. Merge it into the default branch.
