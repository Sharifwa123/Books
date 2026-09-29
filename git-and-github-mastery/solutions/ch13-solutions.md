# Chapter 13 solutions

## Level 1
**1.1** and **1.2** depend on your computer. On Linux the path is typically `/usr/bin/git`; on other systems it differs.

**1.3** Your three settings appear as `user.name=...`, `user.email=...`, `init.defaultbranch=main`.

## Level 2
**2.1** `-m, --message <message>`: add a message from the command line instead of opening an editor.

**2.2** (a) `git help merge`: the full manual. (b) `git merge -h`: a summary that needs no manual pages. (c) the online documentation, because it can be switched between versions (Chapter 35<!--ref:readdocs-->).

## Level 3
**3.1** Git records the name and email in every commit so that each change can be attributed; without them Git refuses to commit or guesses from the computer's name. `--global` means the setting applies to your user account in every repository, not only one.

## Level 4
**4.1** A good checklist: (1) download Git only from the project's official page or the company's approved software source; (2) accept the administrator prompt only when you started the installer; (3) read each installer screen; (4) open a *new* terminal; (5) `git --version` prints a version; (6) run the three `git config --global` commands for name, email and default branch; (7) if `git` is not found, close and reopen the terminal, then check the `PATH`; (8) do not download installers from links in messages.

## Level 5
**5.1** A terminal reads the `PATH` when it starts. A terminal that was open during the installation still has the old `PATH`, so it cannot find `git`. Close it and open a new one.

**5.2** Another, older Git is earlier on the `PATH` and is found first. `command -v git` (or `where git` on Windows) shows which program runs; remove or reorder the older one, or run the new one by its full path.
