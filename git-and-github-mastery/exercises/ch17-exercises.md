# Chapter 17 exercises — Seeing Changes and History

Attempt each exercise before you open `solutions/ch17-solutions.md`. Use the `bakery-menu` repository built in section 17.1 (type the commands yourself), and your `sunrise-bakery` project.

## Level 1 — Guided

**1.1 Rebuild the menu history.** Type the commands of section 17.1 to create `bakery-menu` with three commits. *Expected result:* `git log --oneline` shows three commits.

**1.2 Four log formats.** Run `git log`, `git log --oneline`, `git log --stat` and `git log -p -1`. In one line each, say what each adds.

## Level 2 — Partially guided

**2.1 The four comparisons.** Change the price of the white loaf in `menu.md`, save, and run `git diff`, `git diff --staged` and `git diff HEAD`. Then stage the file and run all three again. Fill in a table with what each printed, and explain it with the picture of Chapter 15<!--ref:model-->.

**2.2 Name it three ways.** Show the commit before the newest using `HEAD~1`, using `HEAD^` and using its short hash from `git log --oneline`. Prove that all three are the same commit with `git rev-parse`.

## Level 3 — Independent

**3.1** In `sunrise-bakery`, make two commits that each change a different file. Then use `git log`, `git show` and `git diff` (with two revisions) to produce a report of the difference between the first commit and the last, and write down the command you used.

## Level 4 — Professional scenario

**4.1** Before a release, your manager asks: "What exactly changed on the website since Monday's version?" Describe the commands you would run to answer, in order, and how you would choose the two revisions. (Chapter 29<!--ref:tags--> will give you a neater way to name "Monday's version".)

## Level 5 — Troubleshooting

**5.1** A learner edits a file, runs `git add`, then `git diff`, sees nothing and decides "Git lost my change". What is happening, and which command shows the change?

**5.2** A colleague's `git log` output stops at the first screen and seems to hang. What is happening, and how do they get out?

**5.3** A learner reads a diff with a line `-- White loaf: 2.50` and another `+- White loaf: 2.80` and is confused by the two dashes. Explain each character.
