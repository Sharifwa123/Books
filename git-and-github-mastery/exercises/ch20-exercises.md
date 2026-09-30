# Chapter 20 exercises — Branching

Attempt each exercise before you open `solutions/ch20-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed) or your `sunrise-bakery` project. Check `git status` before every switch.

## Level 1 — Guided

**1.1 Create, switch, commit.** Create the branch `add-tea` with `git branch add-tea`, switch to it with `git switch add-tea`, change `menu.md` to add tea, and commit. Show the history with `git log --oneline --all --graph`. *Expected result:* `add-tea` is one commit ahead of `main`.

**1.2 The files change.** Switch to `main` and `cat menu.md`; switch back and `cat` again. Describe what changed and why.

## Level 2 — Partially guided

**2.1 One step.** Delete `add-tea` after merging is not yet possible (Chapter 21<!--ref:merging-->). Instead, create `fix-typo` with a single command, rename it to `tidy-menu`, and delete it safely. Which command did you use to delete it, and why did it succeed?

**2.2 Provoke the protection.** Try `git branch -d add-tea`. Read the message. What does it protect you from?

**2.3 Naming.** Try to create branches called `bad name` and `feature/add-tea`. Which worked? Write down the message for the one that failed.

## Level 3 — Independent

**3.1** In `sunrise-bakery`, create a branch `add-hours-page`, add a new file `hours.html`, commit, switch back to `main`, and show that `hours.html` is not there. Then switch back and show that it is.

## Level 4 — Professional scenario

**4.1** A colleague says: "I made three commits, switched to `main`, and my work has vanished." You know branches better than that. Write the checks and commands you would use to find the work, and the two most likely explanations. (Chapter 26<!--ref:reflog--> gives the full recovery tools.)

## Level 5 — Troubleshooting

**5.1** `git switch main` prints `error: Your local changes to the following files would be overwritten by checkout`. List two safe ways out and one unsafe way, with the consequences.

**5.2** `git status` says `HEAD detached at 3f2a9c1`. A learner makes two commits and then runs `git switch main`. Where are the two commits now, and what should the learner have done first?

**5.3** A learner ran `git branch -D experiment`, then realised the work was needed. What did Git print when it deleted the branch, and how can that help?
