# Chapter 16 exercises — Your First Repository

Attempt each exercise before you open `solutions/ch16-solutions.md`. Work in `sharif-git-lab` and run `pwd` before `git init`.

## Level 1 — Guided

**1.1 Project 1.** Do all eight steps of section 16.5 (the study-notes repository). *Expected result:* `git status` is clean and `git log --oneline` lists three commits.

**1.2 Read the output.** Write down, in your own words, what each part of your first commit's output means: the branch, `(root-commit)`, the short hash, the summary line.

## Level 2 — Partially guided

**2.1 Project 2 (start).** Put `sunrise-bakery` under version control as in section 16.6. Before you run `git add .`, run `git status` and list every file it shows. *Expected result:* one commit called "Add the Sunrise Bakery starter site" containing six files.

**2.2 Make the mistakes on purpose.** In a scratch repository, reproduce three of the messages in section 16.7 (commit before staging; nothing to commit; modification not staged). For each, write down the message and the fix.

## Level 3 — Independent

**3.1** In `sunrise-bakery`, change the heading in `index.html` (for example to "Fresh bread and rolls every morning"), save it, and record the change as a second commit using only the commands you know. Then show the history with `git log --oneline`.

## Level 4 — Professional scenario

**4.1** A friend wants to start version-controlling a folder that contains source files, a folder of large photographs and a file called `passwords.txt`. Using what you know so far, say which files you would stage now and which you would leave out, and why. (Chapter 18<!--ref:tracking--> will give you the tool to keep them out permanently.)

## Level 5 — Troubleshooting

**5.1** A learner runs `git commit -m "Update"` and sees `no changes added to commit (use "git add" and/or "git commit -a")`. They insist that they saved the file. Explain what has happened and give two ways to fix it.

**5.2** A learner ran `git init` in their home folder by mistake and now `git status` lists hundreds of untracked files. Explain the problem and how to undo it safely.

**5.3** Two commits both have the message "stuff". Explain why this is a problem, and what you would do about it in future.
