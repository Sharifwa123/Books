# Chapter 25 exercises — Undoing Things Safely

Attempt each exercise before you open `solutions/ch25-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed). Run `git status` before every command.

## Level 1 — Guided

**1.1 Discard an edit.** Change a price in `menu.md` without committing. Look at it with `git diff`, then discard it with `git restore menu.md`. How do you know it worked?

**1.2 Unstage.** Edit the file, `git add` it, then unstage it with `git restore --staged`. Read `git status --short` at each step.

## Level 2 — Partially guided

**2.1 Take back an old version.** Use `git restore --source=HEAD~2 menu.md`. What does the file contain? What does `git status --short` say? Undo the experiment.

**2.2 Soft reset.** Make a commit, then `git reset --soft HEAD~1`. Where is the change now? Commit it again with a better message.

## Level 3 — Independent

**3.1 The three resets.** Make two commits. Run `git reset --soft HEAD~1`, recommit; `git reset HEAD~1`, recommit; `git reset --hard HEAD~1`. Fill in a table: what happened to the log, the index and the file each time?

**3.2 Recover.** After the hard reset in 3.1, use `git reflog` to find the lost commit and `git reset --hard HEAD@{1}` to bring it back.

## Level 4 — Professional scenario

**4.1 A bad commit on a shared branch.** A colleague already pulled your commit "Add a mystery pie". Remove its effect without rewriting history. Show the log and explain why `reset` would be wrong.

## Level 5 — Troubleshooting

**5.1** A learner edited a file for an hour, then ran `git reset --hard` "to tidy up". Can the edit be recovered with Git? Why not, and what should they have done first?

**5.2** A learner ran `git restore menu.md` and the changes disappeared. They ask you to recover them. What do you say?

**5.3** A learner ran `git reset --hard HEAD~3` and now wants the three commits back. What is the first command you tell them to run?
