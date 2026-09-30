# Chapter 26 exercises — Recovery with the Reflog

Attempt each exercise before you open `solutions/ch26-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed).

## Level 1 — Guided

**1.1 Read the reflog.** Run `git reflog`. Which entry is `HEAD@{0}`? What does the text after the second colon describe?

**1.2 Make and lose a branch.** Create a branch `experiment`, commit a change on it, switch to `main` and delete the branch with `git branch -D experiment`. Write down the hash Git prints.

## Level 2 — Partially guided

**2.1 Recover it.** Use the hash from 1.2 to create `experiment-restored`. Check the log.

**2.2 Recover it without the hash.** Repeat 1.2, but this time ignore the printed hash. Find the commit with `git reflog` and recover it with `HEAD@{n}`.

## Level 3 — Independent

**3.1 Detached HEAD.** Run `git switch --detach HEAD~1`, make a commit, and switch back to `main`. Read the warning in full. What does it tell you to do?

**3.2 Rescue it.** Use `git reflog` to find the commit from 3.1 and save it on a new branch.

## Level 4 — Professional scenario

**4.1 Bad reset.** You ran `git reset --hard HEAD~2` and realised that you needed those commits. Write the exact commands that recover them, and say what you would check before running the last one.

## Level 5 — Troubleshooting

**5.1** A learner cloned a repository yesterday and cannot find a colleague's deleted branch in their reflog. Why not?

**5.2** A learner edited a file for an hour and never committed. They ask the reflog for it. What do you tell them?

**5.3** A learner says: "Git says HEAD detached and I have made five commits, but I want to keep them." What is the safest single command, and what should it be given as a name and target?
