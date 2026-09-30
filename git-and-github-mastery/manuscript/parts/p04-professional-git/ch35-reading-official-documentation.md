---
key: readdocs
number: 35
tag: Core
first_read: part
status: draft
requires: [install, model]
ledger: [R221, R222, R223]
---
# Chapter 35 — Reading Official Documentation [Core]

**In this chapter**

- where Git's own documentation lives
- how to read a command synopsis
- how to read an error message
- how to check that what you read matches the version you have
- how to treat a source, including this book

**Before you start.** Chapter 13<!--ref:install--> and Chapter 15<!--ref:model-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on Git 2.55.0.

This chapter closes Part IV. Everything so far was taught by running commands. From now on you will meet commands and features that this book does not cover, and Git and GitHub both change over time. The skill that lasts is being able to look up the answer yourself, and to judge whether it applies to you.

---

## 35.1 Documentation comes in layers

| Layer | What it is | Good for |
|---|---|---|
| **The built-in usage text** | `git <command> -h` prints a short summary of the options | a quick reminder of an option's spelling |
| **The reference manual** | one page per command (`git help <command>`, or `man git-<command>`) | the exact meaning of each option |
| **Guides and tutorials** | longer explanations of concepts and workflows | learning an idea from the start |
| **Release notes** | what changed in each version | finding out when something changed |
| **The platform's documentation** | for GitHub and similar services, the documents that the platform publishes | features of the service, which are separate from Git |

Two of these you can read **without the internet**, and they always match the version that you have installed. That makes them the first place to look.

> **Checked against the documentation (R221).** The `git help` manual page (Git 2.56.0) says the `man` program is used by default; `-m`/`--man`, `-i`/`--info` and `-w`/`--web` choose the format; the `help.format` setting sets the default (`man`, `info`, or `web`/`html`); and with `--web` "a web browser will be used", chosen by `help.browser` or `web.browser`. `git help -a` lists all available commands and `git help -g` lists the concept guides. Whether your system has the manual pages installed, and what Git for Windows opens, depends on your installation: try `git help commit` and read what happens. (The test computer had its manual pages removed, so the message for that case is the one in the recording.)

---

## 35.2 The version you have

Before you trust any page, know which Git you have:

```text
$ git --version
git version <version>
```

*Recorded in Bash; `ch35-docs/expected-synopsis.bash.txt`.*

(The recording shows `<version>` in place of the number, because the number depends on your computer. In your terminal you will see it in full, such as the versions named in Chapter 13<!--ref:install-->.) Documentation that says "since version 2.x" or "new in..." is only useful when you know your own number. Documents on the web usually carry a version too, often selectable in a menu; look for it, and use the one that matches.

The same applies to any tutorial, video or answer that you find: **check its date and the version it describes.** Advice about Git that is five years old can be wrong now, because the defaults and the messages change. This book has met that several times: the same command printed different advice text on Git 2.43.0 and on 2.55.0 (Chapter 20<!--ref:branching-->, Chapter 27<!--ref:rebase-->, Chapter 33<!--ref:gitsec-->).

---

## 35.3 Reading a synopsis

Every command's usage text starts with a **synopsis**: a compact description of how to write the command. For example, the first lines for `git tag`:

```text
$ git tag -h | head -n 6
usage: git tag [-a | -s | -u <key-id>] [-f] [-m <msg> | -F <file>] [-e]
               <tagname> [<commit> | <object>]
   or: git tag -d <tagname>...
   or: git tag [-n[<num>]] -l [--contains <commit>] [--no-contains <commit>]
               [--points-at <object>] [--column[=<options>] | --no-column]
               [--create-reflog] [--sort=<key>] [--format=<format>]
```

*Recorded in Bash; `ch35-docs/expected-synopsis.bash.txt`.*

The notation is a convention that Git's documentation follows:

| Symbol | Meaning |
|---|---|
| `git tag` | Literal text that you type exactly |
| `[ ... ]` | **Optional**: you may leave it out |
| `<name>` | A **placeholder**: replace it with your own value |
| `a \| b` | **Alternatives**: choose one |
| `...` | The item before it may be **repeated** |
| `or:` | A different way of using the same command |

*(The synopsis grows as Git grows. On Git 2.55.0 the first form has one more optional part, `[(--trailer <token>[(=|:)<value>])...]`, which the 2.43.0 recording above does not have. Round brackets group alternatives, so `(=|:)` means "either `=` or `:`". This is a live example of why you must read the documentation for your own version.)*

Read the first form: `git tag`, optionally one of `-a`, `-s` or `-u <key-id>`, optionally `-f`, optionally a message with `-m <msg>` (or from a file with `-F <file>`), optionally `-e`; then the required `<tagname>`; then optionally a `<commit>` or `<object>`. That is what you used in Chapter 24<!--ref:stash--> and Chapter 29<!--ref:tags-->: `git tag -a v1.0 -m "..."`, with an optional commit at the end. The second form, `git tag -d <tagname>...`, deletes one or more tags.

> **Checked against the documentation (R222).** Git's `CodingGuidelines` (Git 2.56.0), section "Synopsis Syntax", states the notation: three dots mean "one or more" (`<file>...`); square brackets mean optional (`[<file>...]` is zero or more); a vertical bar separates alternatives (`[-q | --quiet]`); parentheses group (`[(<rev>|<range>)...]`); and placeholders are lowercase words in angle brackets. The table above agrees with these rules.

After the synopsis, the reference manual explains each option, gives examples, and often lists related commands ("See also"). Read the description of one option at a time, with a scratch repository open beside it, and *try it*. That is the method of this whole book.

---

## 35.4 Reading an error message

Git's messages often tell you the fix. A mistyped command:

```text
$ git comit
git: 'comit' is not a git command. See 'git --help'.

The most similar command is
	commit
```

*Recorded in Bash; `ch35-docs/expected-synopsis.bash.txt`.*

Git says what it did not understand, points to help, and suggests the most similar command. Read the **whole message**, top to bottom, before you search the web. Most Git errors follow the same pattern as the ones in this book:

1. **What happened** (`fatal:`, `error:`).
2. **Why** (often on the same line).
3. **What you can do** (lines that start with `hint:`, or indented suggestions).

In this book's examples, `error:` usually marks something that Git refused, and `fatal:` marks a command that Git could not carry on with; the exact rules were not checked in the official documentation. Advice lines (`hint:`) can be switched off; the recordings in this book show several of them (Chapter 24<!--ref:stash--> and others).

---

## 35.5 Reading a platform's documentation

Hosting platforms publish their own documents about their own features: accounts, repositories, pull requests, automation and security settings. Three cautions:

- **They describe the service as it is now, not as it was.** Interfaces and limits change (Chapter 36<!--ref:whatgh-->).
- **They may depend on your plan or account type.** A feature described on a page may not be available to you.
- **They are not Git's documentation.** Whether something is a Git feature or a platform feature decides where to look (Chapter 12<!--ref:platforms--> introduced the difference).

> **Verification pending [R223].** This book's own statements about GitHub could not be checked against the official documentation while writing Part IV, because the documentation site was not reachable from the test environment. Every such statement is marked *Verification pending* and recorded in the research ledger. When you meet a GitHub fact in this book, check it against GitHub's current documentation before you rely on it.

---

## 35.6 How to treat a source, including this book

When you read a claim, ask:

1. **Who says so?** An official document, an experienced author, or a stranger?
2. **How does it know?** Did the author run the command, or repeat what they remember?
3. **For which version, and on what date?**
4. **Can I test it in a scratch repository?** Almost always, yes.

This book tries to answer those questions for you. Each chapter ends with a table that says how its claims were checked: *locally tested* means that the commands were run, and for which Git version; *not verified* means that no official source was consulted. Pending markers show what still needs checking. That is a promise about method, not a promise that the book is free of errors. **When the book and the official documentation disagree, trust the documentation for your version, and tell the author.**

---

## Checkpoint

## What You Learned

- Documentation has layers: built-in usage text, the reference manual, guides, release notes, and a platform's own pages.
- The built-in text and manual match the version you have installed.
- Know your Git version (`git --version`) and check the version and date of any source.
- A synopsis uses `[ ]` for optional, `<name>` for a placeholder, `|` for alternatives and `...` for repetition.
- Read error messages fully: what happened, why, and what to do.
- Platform documentation describes the service, changes over time, and may depend on your plan.

## New Vocabulary

- **Synopsis**: the compact description of how to write a command.

## Commands Learned

`git --version`, `git <command> -h`, `git help <command>`.

## Common Mistakes

1. **Trusting an old answer without checking its version.**
2. **Reading only the first line of an error message.**
3. **Confusing a Git feature with a platform feature.**
4. **Reading a manual page without trying the command.**
5. **Trusting any source without asking how it knows.**

## Practice

Do the exercises in [`exercises/ch35-exercises.md`](../../../exercises/ch35-exercises.md).

## Self-Test

1. What is the quickest way to see the options of `git tag`?
2. In `git tag -d <tagname>...`, what do the angle brackets and the three dots mean?
3. Why does the version of Git matter when you read documentation?
4. What three parts do most Git error messages have?
5. Name two cautions for platform documentation.

## Before Moving On

You are ready for Chapter 36<!--ref:whatgh--> if you can:

- [ ] find and read the usage text of any Git command
- [ ] read a synopsis, including optional and repeated parts
- [ ] state your Git version and where to check it
- [ ] say what to check before you trust a source

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git --version`, `git tag -h`, the "most similar command" message | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R221 |
| Synopsis notation as it reads in usage text | Locally tested (usage text); definition checked in `CodingGuidelines` | R222 |
| `git help` options and `help.format` | Checked against the `git help` manual page; not run (no manual pages installed on the test computer) | R221 |
| How manual pages open on each system; platform documentation | **Not verified** | R223 |

## Where this leads

Part V begins with Chapter 36<!--ref:whatgh-->: what a hosting platform is, and what it is not. Every platform fact in it will be marked until it can be checked against the official documentation.
