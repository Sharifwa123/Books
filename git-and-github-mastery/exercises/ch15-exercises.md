# Chapter 15 exercises — Git's Core Model

Attempt each exercise before you open `solutions/ch15-solutions.md`. Use a new practice repository.

## Level 1 — Guided

**1.1 Watch the states.** In `sharif-git-lab`, run `mkdir model-lab`, `cd model-lab`, `git init`. Create `notes.md` with `echo "Hello" > notes.md`. After each of these steps run `git status` and write down the state of `notes.md`: (a) after creating it; (b) after `git add notes.md`; (c) after `git commit -m "Add notes"`; (d) after `echo "More" >> notes.md`. *Expected result:* untracked, staged, clean, modified.

**1.2 Look inside.** Run `cat .git/HEAD`, then `cat .git/refs/heads/main` (use the branch name that `HEAD` shows). Write down what each contains.

## Level 2 — Partially guided

**2.1 The three places.** Draw the working tree, the index and the repository. Put `notes.md` at each stage of exercise 1.1 into the place(s) where its changes are.

**2.2 Staging on purpose.** Create two files, `a.txt` and `b.txt`. Stage only `a.txt` and run `git status`. Which state is each file in? Commit and check again.

## Level 3 — Independent

**3.1** Without the chapter open, explain to a friend the difference between saving a file, staging it and committing it, using an analogy of your own.

## Level 4 — Professional scenario

**4.1** A colleague says: "I saved my changes, so they are in Git." Write a four-sentence reply that uses the words working tree, index and repository, and explain what they need to do to record the change.

## Level 5 — Troubleshooting

**5.1** A learner edited `menu.html`, ran `git commit -m "Update menu"` and Git said `no changes added to commit`. Which state was the file in, why did the commit refuse, and what is the fix?

**5.2** A learner deleted the `.git` folder of their project "to tidy up" and now `git status` says `fatal: not a git repository`. What did they delete, what still exists, and what could they do?
