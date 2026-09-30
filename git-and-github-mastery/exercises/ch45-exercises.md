# Chapter 45 exercises — Pull Requests

Attempt each exercise before you open `solutions/ch45-solutions.md`. Exercises 1 to 4 need only your computer; 5 needs an account and a repository you may change.

## Level 1 — Guided

**1.1 Base and compare.** In your own words, say what the base branch and the compare branch are.

**1.2 Two diffs.** In `bakery-menu`, create a branch `add-tea` with one new line. Then make one commit on `main` that changes a different line. Run `git diff --stat main...add-tea` and `git diff --stat main..add-tea`. Which shows only what the branch introduced?

## Level 2 — Partially guided

**2.1 Three strategies.** From one starting commit, make three branches. Merge the same two-commit topic into them with `--no-ff`, with `--squash`, and by rebasing and fast-forwarding. Draw the three `git log --oneline --graph` results.

**2.2 New hashes.** After the rebase, compare the hashes of the two topic commits with their hashes before. Why did they change?

## Level 3 — Independent

**3.1 A pull request reference.** Make a bare repository as a stand-in server, create a reference `refs/pull/1/head` with `git update-ref`, fetch it into a local branch, and switch to it.

**3.2 A hidden reference.** Set `receive.hideRefs` to `refs/pull` in the bare repository and try to push to `refs/pull/1/head`. What message do you get?

## Level 4 — Professional scenario

**4.1 Choose a strategy.** A project has ten contributors who each open pull requests with many "fix typo" and "try again" commits. The team wants a clean history. Which strategy would you recommend, and what is the risk if a contributor keeps working on the same branch afterwards?

## Level 5 — Troubleshooting

**5.1** A reviewer says the pull request page shows changes that you did not make, but `git diff main..topic` on your computer shows them too. Explain, and give the command that matches the page.

**5.2** A merged pull request broke the site. You want to undo it. Name two ways from section 45.5 and when to prefer each.
