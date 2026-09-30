# Chapter 36 solutions

## Level 1
**1.1** For example: "Git is a program on your computer that records the history of your files." "GitHub is an online service that hosts Git repositories and adds features for working together."

**1.2** Two lines, one `(fetch)` and one `(push)`, both showing the address that was added.

## Level 2
**2.1** Scheme `https`, host `github.com`, owner `example-owner`, repository name `sunrise-bakery` (with `.git` at the end).

**2.2** Nothing has been pushed or fetched, so no remote-tracking branch exists yet, and `main` follows none (Chapter 23<!--ref:remotes-->). `git remote add` only records the address.

## Level 3
**3.1** Git: commit, branch, tag, `.gitignore`. Platform features: pull request, issue, release page (a release page is built on a Git tag, but the page is the platform's).

**3.2** A clone copies the repository's files, commits, branches and tags. It does not copy issues, pull requests or other things that the platform stores itself.

## Level 4
**4.1** For example: "GitHub hosts Git repositories; it does not replace Git. Every command in the book, such as commit, branch, merge and undo, ran on a computer with no account. GitHub adds a shared place and features for collaborating, but you still use Git to make and combine changes."

## Level 5
**5.1** Issues are stored by the platform, not in the Git repository, so a clone does not include them.

**5.2** The hosted copy may not be the only place that is missing files (a mistake pushed there is copied too); the account or repository can be removed or become unavailable; the service's terms and features can change. A backup plan keeps independent copies.

**5.3** The interface changes over time, and the tutorial may be old or written for a different plan. Check the tutorial's date and compare with GitHub's current documentation.
