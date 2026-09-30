# Chapter 49 solutions

## Level 1
**1.1** Read, Triage, Write, Maintain, Admin.

**1.2** `origin` points to `fork.git` for fetch and push.

## Level 2
**2.1** `git remote -v` now lists `origin` and `upstream`, each with fetch and push.

**2.2** The graph shows `upstream/main` one commit ahead of your `main`, then after the fast-forward and push all of `main`, `origin/main` and `upstream/main` on the same commit.

## Level 3
**3.1** `git merge --ff-only upstream/main` refuses (it cannot fast-forward because the histories diverged). It teaches why the fork's `main` should stay a mirror of the upstream, and why changes go on branches.

**3.2** `* @example-owner` and `menu.md @ada` (the documentation says "the last matching pattern takes the most precedence"). The file may live in `.github/`, the root or `docs/`; a pull request uses the copy on its **base branch**.

## Level 4
**4.1** Maintainer: Maintain (or Admin if they must manage security). Developers: Write. Designer: Triage. Visitor: Read. Least privilege.

## Level 5
**5.1** The `CODEOWNERS` file is missing from the `release` branch; a pull request uses the version from its base branch, and each file applies to one branch.

**5.2** That repository keeps using its own templates: if a repository defines valid issue templates in its own `.github/ISSUE_TEMPLATE`, none of the default folder's contents are used.
