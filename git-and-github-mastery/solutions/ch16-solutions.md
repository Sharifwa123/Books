# Chapter 16 solutions

## Level 1
**1.1** Your `git log --oneline` shows three lines, newest first, each a short hash and your message.

**1.2** Branch (`main`) received the commit; `(root-commit)` marks the first commit, which has no parent; the short hash names the commit; the summary says how many files and lines changed.

## Level 2
**2.1** `git status` lists `README.md`, `contact.html`, `css/`, `images/`, `index.html`, `menu.html`. `git add .` then `git commit -m "Add the Sunrise Bakery starter site"`.

**2.2** Commit before staging: `nothing added to commit but untracked files present`; fix: `git add`. Nothing to commit: `nothing to commit, working tree clean`; fix: none needed (no change). Modification not staged: `no changes added to commit`; fix: `git add <file>` or `git commit -am`.

## Level 3
Edit and save `index.html`, `git status` (shows `modified`), `git add index.html`, `git commit -m "Update the home page heading"`, `git log --oneline`.

## Level 4
**4.1** Stage the source files. Do not stage `passwords.txt` (a secret: anything committed stays in history, Chapter 33<!--ref:gitsec-->). The large photographs need a decision: they are binary and heavy; leave them out until you understand ignoring (Chapter 18<!--ref:tracking-->) and large files (Chapter 31<!--ref:bigrepos-->).

## Level 5
**5.1** The file was modified but not staged, so the index holds nothing new. Fix: `git add <file>` and commit again, or `git commit -am "Update"` (works for files Git already tracks).

**5.2** Git now treats the whole home folder as a project. Since the repository is new and holds no commits, remove only the hidden `.git` folder in the home folder (check `pwd` and `ls -a` first); this deletes the (empty) history, not your files. Never delete anything else.

**5.3** The messages do not say what changed, so history cannot be read or searched. In future write a short sentence that says what the change does (Chapter 19<!--ref:commits-->).
