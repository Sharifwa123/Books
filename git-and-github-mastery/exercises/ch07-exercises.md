# Chapter 7 exercises — The Terminal Without Fear

Attempt each exercise before you open `solutions/ch07-solutions.md`. **Work only inside `sharif-git-lab`**, and run `pwd` before any `rm`.

## Level 1 — Guided

**1.1 Build the tree.** Open a terminal. Use `pwd` to see where you are. Create `sharif-git-lab`, enter it, and create `sunrise-bakery/css` and `sunrise-bakery/images` with one `mkdir -p`. Use `ls` to check. *Expected result:* `ls sunrise-bakery` prints `css` and `images`.

**1.2 A file.** Inside `sunrise-bakery`, use `echo` and `>` to make `README.md` that contains `Sunrise Bakery`, then use `>>` to add a second line. Show it with `cat`. *Expected result:* two lines.

## Level 2 — Partially guided

**2.1 Copy, rename, remove.** Copy `README.md` to `copy.md`, rename `copy.md` to `notes.txt`, then delete `notes.txt`. Run `ls` after each step and say what it shows. Hint: `cp`, `mv`, `rm`.

**2.2 Hidden.** Create `.draft`, prove that `ls` does not show it and `ls -a` does. Then explain in one sentence what this has to do with `.git`.

## Level 3 — Independent

**3.1** Without looking back, create a folder `experiments` inside `sharif-git-lab` containing three empty files `a.txt`, `b.txt`, `c.md`. List only the `.txt` files with one command using a wildcard. Then remove the folder's contents and the folder, using only commands from this chapter.

## Level 4 — Professional scenario

**4.1** A colleague sends you this line to "tidy" your project: `rm -rf ~/projects/*/build *.log`. You do not know every part. Write what you would do before running anything, using the habits in section 7.10. You do not need to understand `-rf` fully; say what you would find out first.

## Level 5 — Troubleshooting

**5.1** Each line is what a learner typed and the reply. Say what is wrong and how to fix it.
(a) `mkdir Sunrise Bakery` and later `cd Sunrise Bakery` says: `cd: too many arguments` (Bash) or a similar message.
(b) `cd sharif-git-lab/Sunrise-Bakery` says: `No such file or directory`, although the folder is called `sunrise-bakery`.
(c) After installing a tool, typing its name says `command not found`, but the installer said it succeeded.
(d) `echo Fresh bread > README.md` was meant to *add* a line, but now `README.md` has one line only.

**5.2** You run `hello-sunrise` (from section 7.8.3) and it works. You close the terminal, open a new one, and it says `command not found`. Why? How would you make it permanent? (Do not try to change any system files now; describe the idea.)
