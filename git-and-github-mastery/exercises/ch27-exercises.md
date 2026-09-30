# Chapter 27 exercises — Rebase

Attempt each exercise before you open `solutions/ch27-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed). Only rebase **local** work.

## Level 1 — Guided

**1.1 Diverge.** Create `add-tea` with one commit. On `main`, add `hours.md` and commit. Show the graph with `git log --oneline --all --graph`.

**1.2 Rebase.** Switch to `add-tea` and run `git rebase main`. Show the graph again. What changed?

## Level 2 — Partially guided

**2.1 Hashes.** Write down the hash of "Add tea" before and after the rebase. Why are they different?

**2.2 Finish.** Switch to `main` and run `git merge add-tea`. What kind of merge is it?

## Level 3 — Independent

**3.1 A rebase conflict.** Make both branches change the same line. Start the rebase, read `git status`, and abort it. Prove that the branch is unchanged.

**3.2 Resolve it.** Repeat, but resolve the conflict and finish with `git rebase --continue`.

## Level 4 — Professional scenario

**4.1 Tidy before sharing.** Make three small commits on a local branch. Combine them into one with `git rebase -i HEAD~3` (change `pick` to `squash` on lines 2 and 3). Check the log and the combined message.

## Level 5 — Troubleshooting

**5.1** A learner rebased a branch that a colleague had already pulled. What will the colleague see, and what should the learner have done instead?

**5.2** A learner finished a rebase and now realises that the result is wrong. Where can they find the state from before the rebase?

**5.3** During a rebase, `git status` says `both modified: menu.md`. The learner edits the file and runs `git rebase --continue`, and Git refuses. What did they forget?
