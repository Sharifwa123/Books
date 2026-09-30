# Chapter 22 exercises — Merge Conflicts

Attempt each exercise before you open `solutions/ch22-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed). Start every exercise with a clean `git status`.

## Level 1 — Guided

**1.1 Cause a conflict.** Create `raise-bread` and change the white loaf price to 3.00; commit. On `main`, change the same line to 2.90; commit. Run `git merge raise-bread`. *Expected result:* `CONFLICT (content): Merge conflict in menu.md`.

**1.2 Read the state.** Run `git status` and `git diff --name-only --diff-filter=U`. Which words tell you the merge is unfinished?

## Level 2 — Partially guided

**2.1 Read the markers.** Run `cat menu.md`. Which price is on the `HEAD` side, and which is on the `raise-bread` side?

**2.2 Resolve.** Edit the file so the loaf costs 2.95 and no marker remains, stage it, and commit. Check the graph with `git log --oneline --graph`.

## Level 3 — Independent

**3.1 Abort.** Cause the conflict again on a fresh copy and leave it with `git merge --abort`. Prove with `git status`, `cat` and `git log --oneline --graph --all` that nothing changed.

**3.2 Show the ancestor.** Set `git config merge.conflictStyle diff3`, cause the conflict again, and find the line that shows the original price.

## Level 4 — Professional scenario

**4.1 Two files.** Make the same kind of conflict in two files at once. Resolve one, leave the other, and use `git status` to prove that the merge is not finished. Then finish it.

## Level 5 — Troubleshooting

**5.1** A learner commits a merge and later notices `<<<<<<< HEAD` inside `menu.md`. What went wrong, and how do they repair it?

**5.2** A learner ran `git merge --abort` but Git says `There is no merge to abort`. What are two possible reasons?
