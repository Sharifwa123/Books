---
key: terminal
number: 7
tag: Core
first_read: full
status: draft
requires: [files, text]
ledger: [R116, R125, R126, R127, R128, R129, R130]
---
# Chapter 7 — The Terminal Without Fear [Core]

**In this chapter**

- what a terminal, a shell, a prompt and a command are
- the environments you will meet: Command Prompt, PowerShell, Git Bash, Bash and zsh, and why this book uses one primary path
- your first fifteen commands, run in a safe practice folder
- how to read error messages, and why they are your friends
- spaces, quotes, wildcards, variables and the `PATH`, the ideas behind the famous error "command not found"

**Before you start.** Chapter 2<!--ref:files--> (paths, hidden files, permissions) and Chapter 4<!--ref:text--> (bytes, line endings). You will use the practice folder `sharif-git-lab` from Chapter 2<!--ref:files-->.

Nothing in this chapter can harm your computer if you follow one rule, which is repeated where it matters: **only create and delete things inside `sharif-git-lab`.**

---

## 7.1 The idea

Until now you have given your computer instructions by pointing and clicking. There is a second way: typing sentences.

> **New term: terminal.** A window in which you type commands and read the replies as text. (Also called a terminal emulator or console.)

> **New term: shell.** The program that runs inside the terminal, reads what you type, and asks the operating system to carry it out.

> **New term: command.** One instruction typed to the shell, ended by pressing the Enter key.

> **New term: prompt.** The short piece of text the shell prints when it is waiting for you to type. It often ends with `$`, `%` or `>`.

An analogy: the terminal is the telephone handset; the shell is the person who answers and understands what you say; the command is your request. The shell answers in plain text.

**Why bother?** Four reasons, all of which matter for Git:

1. **Precision.** A typed command says exactly what you want, with no hunting through menus.
2. **Repeatability.** You can save a list of commands and run it again, or share it.
3. **Speed for repeated work.** One line can act on a hundred files.
4. **Git's home.** Git began as a set of commands. Most of its power, and all of its documentation, use the terminal. Graphical Git tools are wrappers around the same commands, and they hide what is really happening.

**Nothing happens until you press Enter.** You can type, edit and change your mind. And you can almost always stop a running command by holding the Control key and pressing `C` (written Ctrl+C).

---

## 7.2 Terminal, shell, and the environments you will meet

The words "terminal" and "shell" are used loosely, and different systems supply different shells. The differences are the reason for this section.

| Environment | What it is | Where you meet it |
|---|---|---|
| **Command Prompt** (`cmd`) | The traditional Windows command shell | Windows |
| **PowerShell** | A newer, more powerful Windows shell with its own command names | Windows (and available elsewhere) |
| **Git Bash** | A terminal that provides a **Bash** shell and a set of Unix-style tools on Windows; it is installed together with **Git for Windows** | Windows, after installing Git |
| **Bash** | A very widely used shell for Linux and, historically, macOS | Linux, macOS, Git Bash |
| **zsh** | Another shell in the same family as Bash, with many small differences | macOS (see the note below), and Linux |

> **New term: Bash.** A widely used shell, the one this book uses for its examples.
>
> **New term: Git Bash.** A program for Windows that provides a Bash shell and Unix-style commands, installed with Git for Windows.

> **Git is not Git Bash.** *Git* is the version-control program, the subject of this book. *Git Bash* is a separate shell that is bundled with the Windows installer so that Windows users can type the same commands as everyone else. You can run Git from Command Prompt, PowerShell, Git Bash, zsh or Bash. They are different things that happen to be installed together.

> **Verification pending [R126].** The description of Git Bash and its installation with Git for Windows is from general knowledge; it has not yet been checked against the Git for Windows documentation.

### 7.2.1 The book's primary path

To spare you from learning several dialects at once, this book uses **one primary environment**:

| Your computer | Use this | Notes |
|---|---|---|
| **Windows** | **Git Bash** | Installed with Git for Windows (see below) |
| **macOS** | The **Terminal** application | Its default shell is believed to be zsh; the commands in this chapter work the same in Bash and zsh, and differences are marked |
| **Linux** | Your distribution's **terminal** | Usually Bash |

> **Verification pending [R128].** That macOS's Terminal starts zsh by default is from general knowledge and awaits confirmation from Apple's documentation. If your Terminal shows a Bash prompt instead, everything in this chapter still works.

**Windows: getting Git Bash now.** Git Bash arrives with Git for Windows, which Chapter 13<!--ref:install--> installs. You can install Git for Windows *now* to get Git Bash and follow this chapter exactly; installing Git early is harmless. If you would rather wait, you can follow this chapter in PowerShell or Command Prompt using the equivalence table in section 7.11, and then redo the tour in Git Bash after Chapter 13<!--ref:install-->. Git Bash is the environment the rest of the book assumes.

### 7.2.2 What the two tested shells do differently

Every example in this chapter was run in **Bash 5.2** and in **zsh 5.9**, in real interactive sessions, and the recordings are checked automatically. For the basics they behave the same. The few places where they differ are called out in the text, always with real output. Where Windows shells materially differ, the equivalent commands are given in section 7.11, marked as not run.

---

## 7.3 The anatomy of a command

A command is a sentence: a verb and, usually, some details.

```text
ls -l notes.txt
```

| Part | In the example | Meaning |
|---|---|---|
| **Program** (the command name) | `ls` | What to do: list files |
| **Option** (also called a *flag*) | `-l` | *How* to do it: use the long, detailed format |
| **Argument** | `notes.txt` | *What* to do it to |

Parts are separated by **spaces**, so spaces matter. Names are **case-sensitive** in Bash and zsh: `ls` works, `LS` does not.

> **The `$` in this book.** In the examples, a line that starts with `$ ` shows a command that you type, *without the `$`*. The `$` stands for the prompt. Lines below it, with no `$`, are what the computer printed. Your own prompt will look different: it may show your user name, the computer's name or the current folder.

> **New term: option (flag).** A word, usually starting with a dash, that changes how a command behaves.
>
> **New term: argument.** The thing that a command acts on, such as a file name.

---

## 7.4 Open a terminal and start in the practice folder

> **UI-VERSION NOTE.** How to open a terminal depends on your system and its version. On macOS and Linux, search your applications for "Terminal". On Windows, after Git for Windows is installed, search for "Git Bash". If you cannot find it, search your system's help for "open a terminal".

When a terminal opens, you are normally in your **home folder** (Chapter 2<!--ref:files-->). The recordings in this chapter start there and use the fictional user name `learner`, so your paths will differ: `/home/learner` will be your own home folder, and on Windows Git Bash shows Windows drives in a Unix style such as `/c/Users/yourname`.

---

## 7.5 Your first tour

Work through this tour by typing each command yourself, one at a time, and comparing your result with the recording. **Type each command exactly, then press Enter.**

### 7.5.1 Where am I? (`pwd`)

> **New term: pwd.** Short for "print working directory": prints the current directory, that is, where you are in the folder tree.

```text
$ pwd
/home/learner
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

`/home/learner` is an **absolute path** (Chapter 2<!--ref:files-->) and it is the home folder of this practice user.

### 7.5.2 Make a folder and step into it (`mkdir`, `cd`)

> **New term: mkdir.** Short for "make directory": creates a new folder.
>
> **New term: cd.** Short for "change directory": moves you into another folder, making it the current directory.

```text
$ mkdir sharif-git-lab
$ cd sharif-git-lab
$ pwd
/home/learner/sharif-git-lab
$ ls
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

`mkdir sharif-git-lab` printed nothing: **most commands print nothing when they succeed.** Silence usually means success. `cd sharif-git-lab` moved us in, `pwd` confirmed it, and `ls` (list) printed nothing because the folder is empty.

### 7.5.3 Build the bakery tree (`mkdir -p`, `ls`)

The option `-p` means "create the parent folders too, and do not complain if they exist". One command builds the whole tree from Chapter 3<!--ref:editors-->:

```text
$ mkdir -p sunrise-bakery/css sunrise-bakery/images
$ ls
sunrise-bakery
$ ls sunrise-bakery
css  images
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

Here the second `ls` names a folder, `sunrise-bakery`, as its argument, so it lists what is *inside* it: `css` and `images`. **In your own terminal `ls` prints its names in columns, as here; in this book's tables and lists the same names are sometimes shown one per line.**

### 7.5.4 Make a file (`echo`, `>`, `>>`, `cat`)

```text
$ cd sunrise-bakery
$ pwd
/home/learner/sharif-git-lab/sunrise-bakery
$ echo "Sunrise Bakery" > README.md
$ cat README.md
Sunrise Bakery
$ echo "Fresh bread every morning." >> README.md
$ cat README.md
Sunrise Bakery
Fresh bread every morning.
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

- `echo` prints the words you give it.
- `>` **redirects** that output into a file instead of the screen, *replacing whatever the file held*. The file `README.md` did not exist, so it was created.
- `cat` prints a file's contents to the screen ("concatenate", but you will use it to *show* files).
- `>>` redirects too, but **appends** to the end instead of replacing.

> **⚠️ CAUTION.** A single `>` overwrites the file *without asking* and without a trash to recover from. Use `>>` when you mean "add to the end". Before using `>` on an existing file, be sure you do not need what is in it.

### 7.5.5 Copy and rename (`cp`, `mv`)

```text
$ cp README.md README-copy.md
$ ls
README-copy.md	README.md  css	images
$ mv README-copy.md notes.txt
$ ls
README.md  css	images	notes.txt
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

`cp source destination` makes a copy; `mv source destination` moves, and **renaming is moving to a new name in the same place**, which is why there is no separate "rename" command. After `mv`, `README-copy.md` is gone and `notes.txt` exists, containing the same text.

### 7.5.6 Hidden files (`touch`, `ls -a`)

> **New term: touch.** Creates an empty file, or updates a file's "last changed" time if it already exists.

```text
$ touch .hidden-note
$ ls
README.md  css	images	notes.txt
$ ls -a
.  ..  .hidden-note  README.md	css  images  notes.txt
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

`touch .hidden-note` created a file whose name starts with a dot. Plain `ls` does not list it. `ls -a` ("all") shows it, together with two special entries: `.` (this folder) and `..` (the parent), which you met in Chapter 2<!--ref:files-->. This is exactly how Git's hidden `.git` folder will behave.

### 7.5.7 The long listing (`ls -l`)

```text
$ ls -l notes.txt
-rw-r--r-- 1 learner learner 42 <date> notes.txt
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

Read it from left to right: the ten characters `-rw-r--r--` are the **permissions** (Chapter 2<!--ref:files-->): a leading `-` means an ordinary file, then read/write for the owner, and read-only for others. `1` is a count of links, `learner learner` are the owner and group, **`42` is the size in bytes**, `<date>` stands for the date and time, and last comes the name. The size is 42 because the file holds `Sunrise Bakery` plus a line break (15 bytes) and `Fresh bread every morning.` plus a line break (27 bytes). This is Chapter 4<!--ref:text--> in action.

> **Verification pending [R116].** The permission string above was produced by real tools on Linux. The exact form of `ls -l` differs a little between systems.

### 7.5.8 Moving around (`cd ..`, `cd -`, `cd ~`)

```text
$ cd ..
$ pwd
/home/learner/sharif-git-lab
$ cd -
/home/learner/sharif-git-lab/sunrise-bakery
$ cd ~
$ pwd
/home/learner
$ cd sharif-git-lab/sunrise-bakery
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

- `cd ..` goes up one level to the parent folder.
- `cd -` jumps back to the folder you were in before, and prints it.
- `cd ~` goes to your home folder from anywhere. `~` is shorthand for your home folder.
- `cd sharif-git-lab/sunrise-bakery` used a **relative path** (from the home folder) to get back.

In zsh, `cd -` prints the folder with `~` abbreviating the home folder (`~/sharif-git-lab/sunrise-bakery`). It is the same folder, written differently.

### 7.5.9 Deleting, carefully (`rm`, `rmdir`)

> **⚠️ CAUTION. There is no trash bin in the terminal.** `rm` deletes immediately and permanently. Before you press Enter on any `rm`, read the command aloud and check where you are (`pwd`) and what the name matches (`ls`). Never run a command that you copied from a website or a chat if you do not understand every word.

```text
$ rm notes.txt
$ ls
README.md  css	images
$ rm css
rm: cannot remove 'css': Is a directory
$ rmdir css
$ rmdir images
$ ls
README.md
```

*Recorded in Bash; `ch07-terminal/expected-main.bash.txt`.*

- `rm notes.txt` removed the file. No message: success.
- `rm css` **refused**, because `css` is a folder, and printed the error `Is a directory`. That refusal is a safety feature: it stopped you from deleting a folder by reflex.
- `rmdir` removes an **empty** folder, and only an empty one. Non-empty folders are not removed by `rmdir` (so it is a safe way to remove folders you have finished with). There is an option that deletes a folder and everything in it. This book will not use it until Git recovery gives you a safety net, and you should treat it as the most dangerous ordinary command that you will meet.

---

## 7.6 Reading error messages

Errors are the shell explaining, in words, what it could not do. Read them slowly, from the start. One real one appeared above (`Is a directory`). More are recorded below, from a session in which the first four commands were deliberately wrong. Bash first:

```text
$ mkdir sharif-git-lab
$ cd sharif-git-lab
$ cd nowhere
bash: cd: nowhere: No such file or directory
$ ls missing-folder
ls: cannot access 'missing-folder': No such file or directory
$ cat missing-file.txt
cat: missing-file.txt: No such file or directory
$ frobnicate
bash: frobnicate: command not found
```

*Recorded in Bash; `ch07-terminal/expected-errors.bash.txt`.*

Now the same four mistakes in zsh:

```text
$ mkdir sharif-git-lab
$ cd sharif-git-lab
$ cd nowhere
cd: no such file or directory: nowhere
$ ls missing-folder
ls: cannot access 'missing-folder': No such file or directory
$ cat missing-file.txt
cat: missing-file.txt: No such file or directory
$ frobnicate
zsh: command not found: frobnicate
```

*Recorded in zsh; `ch07-terminal/expected-errors.zsh.txt`.*

| Message | Plain meaning | Usual cause |
|---|---|---|
| `No such file or directory` (Bash: `cd: nowhere: ...`; zsh: `cd: no such file or directory: nowhere`) | The path you gave does not exist | A typo, the wrong current folder, or a missing folder |
| `command not found` | The shell has no program of that name | A typo, or the program is not installed, or is not on the `PATH` (section 7.8) |
| `Is a directory` | You used a file-only command on a folder | Use the folder version, or the right option |
| `Permission denied` (not recorded here) | The operating system refused because of permissions | See Chapter 2<!--ref:files-->; you may need a different account or a different location |

**The habit:** read the *first* line, find the name it complains about, and check that name against what you meant to type. Most errors are typos.

Note how **the wording differs by shell** although the meaning is the same. Books, forum answers and your own screen may therefore show different words for the same mistake. When you search for help, search for the *meaning*.

---

## 7.7 Spaces, quotes and wildcards

Because spaces separate the parts of a command, a folder with a space in its name is awkward. This recording shows the classic mistake, and its repair:

```text
$ mkdir my folder
$ ls
folder	my
$ rmdir my folder
$ mkdir "my folder"
$ ls
'my folder'
$ rmdir "my folder"
```

*Recorded in Bash; `ch07-terminal/expected-errors.bash.txt`.*

`mkdir my folder` made **two** folders, `my` and `folder`, because the space split the command into two arguments. Putting the name in **quotes** keeps it together, and `mkdir "my folder"` made one. This is why Chapter 2<!--ref:files--> advised names without spaces. (`rmdir my folder` removed both empty folders: the same splitting applied.)

**Wildcards** let one pattern match many names. `*` stands for "any characters". Here `ls *.md` matched the two Markdown files but not `c.txt`:

```text
$ touch a.md b.md c.txt
$ ls *.md
a.md  b.md
```

*Recorded in Bash; `ch07-terminal/expected-errors.bash.txt`.*

A wildcard that matches nothing behaves differently in the two shells:

```text
$ ls *.xyz
ls: cannot access '*.xyz': No such file or directory
```

*Recorded in Bash; `ch07-terminal/expected-errors.bash.txt`.*

In zsh the same command says:

```text
$ ls *.xyz
zsh: no matches found: *.xyz
```

*Recorded in zsh; `ch07-terminal/expected-errors.zsh.txt`.*

Bash passes the pattern on unchanged and `ls` complains that no such file exists; zsh refuses earlier, at the pattern.

---

## 7.8 Variables, the environment and the `PATH`

### 7.8.1 Variables

A **variable** is a named place that holds text. Set one with `name=value` (no spaces around the equals sign), and read it by putting a `$` before the name.

> **New term: variable.** A named piece of text that the shell remembers, which you can use in later commands.

```text
$ name="Sunrise Bakery"
$ echo "$name"
Sunrise Bakery
$ echo '$name'
$name
$ echo $name
Sunrise Bakery
```

*Recorded in Bash; `ch07-terminal/expected-vars.bash.txt`.*

- `echo "$name"` printed the value, because double quotes let `$name` be replaced by its value. **Single quotes do not**, so `'$name'` printed the literal text `$name`. The unquoted `echo $name` also worked here, but *unquoted* variables are split at spaces, so **use double quotes whenever a value may contain spaces.**

### 7.8.2 The environment

By default a variable belongs only to the shell that made it. A variable becomes part of the **environment**, visible to programs that the shell starts, only if you `export` it. The recording proves it by starting a second, separate shell (`sh -c`) and asking it to print each variable:

```text
$ export SHOP=sunrise
$ sh -c 'echo "shop is: $SHOP"'
shop is: sunrise
$ UNEXPORTED=hidden
$ sh -c 'echo "unexported is: [$UNEXPORTED]"'
unexported is: []
```

*Recorded in Bash; `ch07-terminal/expected-vars.bash.txt`.*

`SHOP` was exported, so the child saw it; `UNEXPORTED` was not, so the child saw nothing (the empty brackets).

> **New term: environment variable.** A variable that has been exported, so that programs started from the shell can read it.

Some environment variables exist from the start. `HOME` holds your home folder; `~` is its shorthand:

```text
$ echo $HOME
/home/learner
$ echo ~
/home/learner
```

*Recorded in Bash; `ch07-terminal/expected-vars.bash.txt`.*

This is how programs, including Git, learn things about the computer and the user, and why **the same command can behave differently on two computers**: their environments differ. Chapter 14<!--ref:config--> shows the environment changing the behaviour of Git itself.

### 7.8.3 The `PATH`

When you type `ls`, how does the shell know where the program is? It searches a list of folders held in an environment variable called **`PATH`**, in order, and runs the first program with that name that it finds.

> **New term: PATH (environment variable).** An environment variable that lists the folders in which the shell looks for programs when you type a command name.

The recording creates a tiny program called `hello-sunrise` in a folder called `bin`, then tries to run it by name:

```text
$ mkdir bin
$ printf '#!/bin/sh\necho "Hello from the Sunrise Bakery tool"\n' > bin/hello-sunrise
$ chmod +x bin/hello-sunrise
$ hello-sunrise
bash: hello-sunrise: command not found
$ PATH="$PWD/bin:$PATH"
$ hello-sunrise
Hello from the Sunrise Bakery tool
$ command -v hello-sunrise
/home/learner/bin/hello-sunrise
```

*Recorded in Bash; `ch07-terminal/expected-vars.bash.txt`.*

Read what happened:

1. `hello-sunrise` alone failed with `command not found`, although the program exists. The shell searched every folder in `PATH`, and `bin` is not among them.
2. `PATH="$PWD/bin:$PATH"` put our folder at the front of the list (`$PWD` holds the current directory).
3. Now the same command works, and `command -v hello-sunrise` shows *where the shell found it*.

The zsh recording differs only in the wording of the error: `zsh: command not found: hello-sunrise`.

**This is the reason behind one of the most common beginner errors.** After you install a program, typing its name gives `command not found` (or, in Windows shells, a message that the name "is not recognized") when the program's folder is not on the `PATH`, or when the terminal was opened before the installation. The cure is to fix the `PATH`, or to close and reopen the terminal. Chapter 13<!--ref:install--> will show how to check.

> **Verification pending [R129].** The exact wording of the "not recognized" message in Windows shells has not been checked; it is not recorded here.

---

## 7.9 Getting help

- Many programs print a summary if you add `--help`. This is a convention, not a rule; some programs use `-h`, some use neither.
- Git has its own built-in help, which Chapter 13<!--ref:install--> and Chapter 35<!--ref:readdocs--> introduce.
- When you do not know a command's name, describe what you want in a search and read the official documentation of the tool.

---

## 7.10 Habits that keep you safe

1. **Read before you press Enter.** Say the command to yourself in words.
2. **Check where you are** (`pwd`) and what is there (`ls`) before deleting or overwriting.
3. **Copy commands only when you understand them.** A command pasted from the web can do anything you can do, including harm.
4. **Stay in the practice folder** while learning.
5. **Use the Up arrow to recall** the previous command, and **Tab to complete** names. Most shells support both; they save typing and prevent typos.
6. **When something is wrong, stop and read the message.**

> **Security note.** A common attack is a web page or message that tells you to "just paste this command". Treat a pasted command like an installer from a stranger (Chapter 1<!--ref:computer-->): if you do not understand it, do not run it.

---

## 7.11 Windows without Git Bash: equivalents

If you are using PowerShell or Command Prompt, these are the equivalents of the commands in this chapter. **They are not recorded or checked**; the Windows environments could not be run in the book's test environment.

> **Verification pending [R127].** The Windows commands in this table are from general knowledge and have not been executed or checked against Microsoft's documentation. Check each on your own machine; the `--help`-style summary for Command Prompt is `command /?`, and PowerShell has `Get-Help`. Appendix M will contain a verified version.

| Task | Git Bash / Bash / zsh | PowerShell | Command Prompt |
|---|---|---|---|
| Where am I? | `pwd` | `Get-Location` (alias `pwd`) | `cd` (with no argument) |
| List files | `ls` | `Get-ChildItem` (alias `ls`) | `dir` |
| Change folder | `cd folder` | `Set-Location folder` (alias `cd`) | `cd folder` |
| Make a folder | `mkdir folder` | `New-Item -ItemType Directory folder` (alias `mkdir`) | `mkdir folder` |
| Show a file | `cat file` | `Get-Content file` (alias `cat`) | `type file` |
| Copy | `cp a b` | `Copy-Item a b` (alias `cp`) | `copy a b` |
| Move / rename | `mv a b` | `Move-Item a b` (alias `mv`) | `move a b` or `ren a b` |
| Delete a file | `rm file` | `Remove-Item file` (alias `rm`) | `del file` |
| Show a variable | `echo $HOME` | `$env:USERPROFILE` | `echo %USERPROFILE%` |

The book's later chapters use Git commands, which are identical in every shell. Only the ordinary file commands differ.

---

## 7.12 What you now have

You can now move around the computer, create, copy, move and delete things in the practice folder, read error messages, quote a name with spaces, and explain `PATH`. That is enough to run every Git command in Part III.

---

## Checkpoint

## What You Learned

- A terminal is a window for typing commands; the shell is the program that reads them; the prompt shows it is waiting.
- This book's primary environment is Bash (Git Bash on Windows); Git is not Git Bash.
- A command has a program, options and arguments, separated by spaces and case-sensitive.
- `pwd`, `ls`, `cd`, `mkdir`, `echo`, `cat`, `cp`, `mv`, `touch`, `rm`, `rmdir` and the redirections `>` and `>>`.
- Most commands print nothing on success; errors are readable messages, worded differently by different shells.
- Quotes keep spaces in one argument; wildcards match many names.
- Variables, the environment and `PATH` explain "command not found" and why behaviour can differ between computers.
- There is no trash bin: deleting is permanent.

## New Vocabulary

- **Terminal**: a window for typing commands and reading replies.
- **Shell**: the program that reads your commands and has them carried out.
- **Command**: one instruction typed to the shell.
- **Prompt**: the text the shell shows when it waits for input.
- **Bash**: a widely used shell; this book's primary shell.
- **Git Bash**: a Bash environment for Windows, installed with Git for Windows.
- **Option (flag)**: a word that changes how a command behaves.
- **Argument**: what a command acts on.
- **Variable**: a named piece of text the shell remembers.
- **Environment variable**: an exported variable that started programs can read.
- **PATH (environment variable)**: the list of folders searched for programs.

## Commands Learned

`pwd`, `ls`, `ls -a`, `ls -l`, `cd`, `cd ..`, `cd -`, `cd ~`, `mkdir`, `mkdir -p`, `echo`, `cat`, `cp`, `mv`, `touch`, `rm`, `rmdir`, `export`, `command -v`, and the redirections `>` and `>>`.

## Common Mistakes

1. **Typing the `$` prompt symbol** as part of the command.
2. **Spaces in names** without quotes, splitting one name into two.
3. **Using `>` when `>>` was meant**, overwriting a file.
4. **Deleting from the wrong folder.** Check `pwd` first.
5. **Forgetting that names are case-sensitive.**
6. **Expecting output from a command that succeeded silently.**
7. **Opening a terminal before installing a program**, then seeing `command not found`; open a new terminal.

## Practice

Do the exercises in [`exercises/ch07-exercises.md`](../../../exercises/ch07-exercises.md). They all happen inside `sharif-git-lab`.

## Self-Test

1. What is the difference between a terminal and a shell?
2. Split `mkdir -p sunrise-bakery/css` into program, option and argument.
3. What is the difference between `>` and `>>`?
4. A command prints nothing. Did it fail?
5. Why does `mkdir my folder` create two folders, and how do you create one?
6. A program you installed gives `command not found`. Give two possible causes.
7. Is Git the same thing as Git Bash?

## Before Moving On

You are ready for Chapter 8<!--ref:markdown--> if you can:

- [ ] open a terminal and say what your shell is
- [ ] create the `sunrise-bakery` tree with two commands and list it
- [ ] copy, rename and delete a file, saying `pwd` first
- [ ] explain what `PATH` is
- [ ] read the first line of an error message and find the name it complains about

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Behaviour and output of every command and error shown, in Bash 5.2 and zsh 5.9, including the differences in error wording, `cd -`, and unmatched wildcards | Locally tested: interactive sessions via a pseudo-terminal, recorded in `verification/ch07-terminal/expected-*.txt`, re-run in CI on the runner's Bash and zsh; GNU manuals not yet consulted | R125 |
| Exported versus unexported variables; `PATH` lookup; `command -v` | Locally tested (as above) | R130 |
| `ls -l` permission string | Locally tested on Linux | R116 |
| Git Bash is installed with Git for Windows and is not Git | Needs re-verification | R126 |
| PowerShell and Command Prompt equivalents | Needs re-verification; not executed | R127 |
| macOS Terminal defaults to zsh | Needs re-verification | R128 |
| Wording of Windows "not recognized" messages | Needs re-verification; not recorded | R129 |

## Where this leads

Chapter 8<!--ref:markdown--> teaches Markdown, the plain text format for READMEs. Chapter 13<!--ref:install--> installs Git and checks it from the terminal you now know how to use. Chapter 14<!--ref:config--> returns to environment variables, showing how the environment changes what Git does.
