# Chapter 28 exercises — Cherry-pick, Bisect and Patches

Attempt each exercise before you open `solutions/ch28-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed).

## Level 1 — Guided

**1.1 Cherry-pick.** Create a branch `drinks` with two commits (tea, coffee). On `main`, cherry-pick only the first. Show the graph.

**1.2 Compare hashes.** Write down the hash of "Add tea" on `drinks` and on `main`. Why do they differ?

## Level 2 — Partially guided

**2.1 The second commit.** Cherry-pick the coffee commit too. Read the log. What is the relation between `main` and `drinks` now?

**2.2 Make a patch.** Commit a change on a branch, run `git format-patch -1 HEAD`, and read the first eight lines of the file.

## Level 3 — Independent

**3.1 Apply a patch.** On `main`, run `git apply --check` on your patch, then `git am`. Check the log and the author.

**3.2 Bisect by hand.** Make five commits, one of which adds a bad line. Use `git bisect start`, `git bisect bad`, `git bisect good <commit>`, and at each step check the file and answer `git bisect good` or `git bisect bad`. Finish with `git bisect reset`.

## Level 4 — Professional scenario

**4.1 Automate it.** Repeat 3.2 with `git bisect run sh -c '! grep -q Mystery menu.md'`. How many steps did it take? How many would 1000 commits need?

## Level 5 — Troubleshooting

**5.1** A learner cherry-picked a commit that used a function added in the previous commit, and the result does not work. What went wrong?

**5.2** A learner ran `git bisect start` yesterday and forgot to reset. `git status` says `HEAD detached`. What should they run?

**5.3** `git apply --check` prints an error. Should the learner run `git apply` anyway? Why not?
