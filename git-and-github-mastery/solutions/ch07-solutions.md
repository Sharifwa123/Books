# Chapter 7 solutions

## Level 1
**1.1** `pwd` shows your home folder. Then: `mkdir sharif-git-lab`, `cd sharif-git-lab`, `mkdir -p sunrise-bakery/css sunrise-bakery/images`, `ls sunrise-bakery`.

**1.2** `cd sunrise-bakery`, `echo "Sunrise Bakery" > README.md`, `echo "Fresh bread every morning." >> README.md`, `cat README.md`.

## Level 2
**2.1** `cp README.md copy.md` (ls shows both), `mv copy.md notes.txt` (ls shows `notes.txt` and no `copy.md`), `rm notes.txt` (gone; no message).

**2.2** `touch .draft`; `ls` omits it; `ls -a` lists `.draft`. Git's data lives in a hidden `.git` folder, invisible in ordinary listings for the same reason.

## Level 3
**3.1** `mkdir experiments`, `cd experiments`, `touch a.txt b.txt c.md`, `ls *.txt` (prints `a.txt b.txt`), then `rm a.txt b.txt c.md`, `cd ..`, `rmdir experiments`.

## Level 4
**4.1** Do not run it. Find out what each part means by reading the documentation for `rm`; run `ls` (not `rm`) with the same wildcards to see exactly what they would match; check `pwd`; ask the colleague why; and run it only on a copy or in a practice folder. The general rule: a delete command with wildcards must be previewed with a harmless command first.

## Level 5
**5.1** (a) The space split the name into two arguments; quote the name (`cd "Sunrise Bakery"`) or, better, avoid spaces in names. (b) Names are case-sensitive: `Sunrise-Bakery` is not `sunrise-bakery`; check with `ls` and match the case. (c) The program's folder is not on `PATH`, or the terminal was opened before the installation; open a new terminal and check `PATH` (Chapter 13<!--ref:install-->). (d) A single `>` replaced the file; use `>>` to append.

**5.2** A variable set with `PATH="..."` lives only in that shell session; a new terminal starts with the default environment. To make it permanent you would put the setting in a startup file that the shell reads when it starts (the file's name depends on the shell), or install programs into a folder that is already on `PATH`. Chapter 13<!--ref:install--> shows how Git's installer handles this.
