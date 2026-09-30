# Chapter 76 exercises — Professional Scenarios 1–12

Attempt each exercise before you open `solutions/ch76-solutions.md`. Work in a sandbox folder with a local bare repository as the remote, as in the recordings. **Do not practise history rewriting on a repository that matters.**

## Level 1 — Guided

**1.1 Choose the tool.** For each situation choose amend, revert, squash (soft reset) or cherry-pick: (a) a typo in your last unpushed commit message; (b) a bad commit already on the shared `main`; (c) three messy commits on your private branch; (d) a fix on a hotfix branch that `main` also needs.

**1.2 Read first.** Which three commands do the scenarios use to read the state before and after a change?

## Level 2 — Partially guided

**2.1 Scenario 1.** Reproduce scenario 1 in your sandbox: fix on a branch, push, merge from a second clone, fast-forward your `main`, delete the branch locally and on the remote.

**2.2 Scenario 4.** Reproduce the deleted-branch recovery. What would change if you waited a very long time before recovering?

## Level 3 — Independent

**3.1 A new scenario.** Write your own thirteenth scenario in the same layout (situation, goal, steps, what happened, if it goes wrong) using only commands from the book, and run it.

**3.2 Conflict by design.** Create a conflict on purpose, resolve it, and then create it again and abort the merge. Compare the two histories.

## Level 4 — Professional scenario

**4.1 A leaked key.** A colleague says: "I deleted the key file in a new commit, so we are safe." Write your reply, in order of actions, using scenario 8.

## Level 5 — Troubleshooting

**5.1** `git branch -d` says the branch is not fully merged, but you believe it is. Give two ways to check, and say when `-D` is acceptable.

**5.2** After a hotfix cherry-pick, `main` still shows the old price. List three causes.
