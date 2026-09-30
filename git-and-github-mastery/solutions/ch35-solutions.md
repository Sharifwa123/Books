# Chapter 35 solutions

## Level 1
**1.1** `git version 2.x.y` (your own number). You can also see it in an installer, a package manager listing, or a "Programs" page, depending on your system.

**1.2** For example `git tag [-a | -s | -u <key-id>] [-f] [-m <msg> | -F <file>] [-e] <tagname> [<commit> | <object>]` (your version may show a slightly different line).

## Level 2
**2.1** Optional: `-a`/`-s`/`-u`, `-f`, `-m`/`-F`, `-e`, and the final commit or object. Required: `<tagname>`. Placeholders: `<key-id>`, `<msg>`, `<file>`, `<tagname>`, `<commit>`, `<object>`.

**2.2** `...` means that the item may be repeated: `git tag -d v0.1 v0.2` deletes both.

## Level 3
**3.1** Answers vary. For example, `git switch -c <branch>` creates and switches; `git restore --staged <file>` unstages.

**3.2** It depends on the system. On a system without manual pages, Git says so; then rely on `-h` and on the platform's or Git's online documentation for your version.

## Level 4
**4.1** Check: the date of the post; the Git version it describes; whether the command changes or deletes anything; who wrote it and how they know. Then run it in a scratch copy of the repository first, never in the real one.

## Level 5
**5.1** The error message itself: `git: 'comit' is not a git command`, with `The most similar command is commit`.

**5.2** A different Git version (messages and advice change), a different configuration (Chapter 14<!--ref:config-->), or a different operating system or shell (Chapter 7<!--ref:terminal-->).

**5.3** Ask whether it works on any Git repository without an account (then it is Git), or whether it exists only on the website or through the platform's own tool (then it is the platform). Chapter 12<!--ref:platforms--> gave the distinction.
