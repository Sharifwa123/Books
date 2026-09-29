# Chapter 21 exercises — Merging

Attempt each exercise before you open `solutions/ch21-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed) or your `sunrise-bakery` project. Check that `git status` is clean before every merge.

## Level 1 — Guided

**1.1 Fast-forward.** Create `add-tea`, add a tea line to `menu.md`, commit, switch to `main` and run `git merge add-tea`. *Expected result:* the output says `Fast-forward`, and no merge commit exists.

**1.2 Which branch moved?** After exercise 1.1, run `git log --oneline --all --graph`. Which branch pointers moved, and which did not?

## Level 2 — Partially guided

**2.1 Three-way merge.** Create `add-tea` with one commit. On `main`, add a new file `hours.md` and commit. Merge `add-tea` into `main` with `git merge --no-edit add-tea`. Find the merge commit with `git log --merges`.

**2.2 Parents.** Run `git show --stat HEAD` on the merge commit from 2.1. How many parents does it show, and which commits are they?

## Level 3 — Independent

**3.1 Force a merge commit.** Repeat 1.1 on a fresh branch, but use `--no-ff`. Compare the graph with the one from 1.2.

**3.2 Squash.** Make a branch with two commits that create a new file. Squash-merge it into `main`, check `git status --short`, then commit. Explain why the graph shows no link to the branch.

## Level 4 — Professional scenario

**4.1 Choose a style.** Your team wants one history entry per feature and does not care about a feature's work-in-progress commits. Which merge style fits, and what is lost? Then show the commands.

## Level 5 — Troubleshooting

**5.1** After a squash merge, `git branch -d feature` prints that the branch is not fully merged. Is the work lost? How can you check before you use `-D`?

**5.2** A learner runs `git merge main` while on `add-tea`, expecting `main` to receive the tea line. What actually happened, and how do they get the result they wanted?
