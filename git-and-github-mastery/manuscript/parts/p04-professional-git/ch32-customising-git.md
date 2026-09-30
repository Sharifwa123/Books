---
key: custom
number: 32
tag: Deep
first_read: later
status: draft
requires: [config, objects]
ledger: [R208, R209, R210, R211, R212]
---
# Chapter 32 — Customising Git [Deep]

**In this chapter**

- **aliases**: your own short names for commands
- **hooks**: scripts that Git runs at certain moments
- **attributes**: per-file rules such as line endings
- **credential helpers**: how Git remembers passwords, and the risk in that
- **rerere**: teach Git to remember how you resolved a conflict

> **Deep.** This chapter is marked **[Deep]**. You can skip it on a first read. It changes how Git behaves for you, and each feature works best once you know the plain behaviour well.

**Before you start.** Chapter 14<!--ref:config--> (scopes) and Chapter 30<!--ref:objects-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on Git 2.55.0.

---

## 32.1 Aliases

An **alias** is a shortcut that you define in your configuration (Chapter 14<!--ref:config-->).

> **New term: alias.** A name you define in Git's configuration as a shortcut for another command, with its options.

Four aliases: three shortenings of Git commands and one that runs a shell command (a leading `!`):

```text
$ cd bakery-menu
$ git config --global alias.st "status --short"
$ git config --global alias.lg "log --oneline --graph --all"
$ git config --global alias.last "log -1 --stat"
$ git config --global alias.hello '!echo hello from a shell alias'
$ printf -- '- Tea: 1.50\n' >> menu.md
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

Use them like built-in commands:

```text
$ git st
 M menu.md
$ git commit -qam "Add tea"
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

```text
$ git lg
* 31cb2c3 (HEAD -> main) Add tea
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

```text
$ git last
commit 31cb2c3316e22b96397393788023fb0b98ff2c6d (HEAD -> main)
Author: Ada Learner <ada@example.org>
Date:   Mon Jan 5 09:14:00 2026 +0000

    Add tea

 menu.md | 1 +
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

```text
$ git hello
hello from a shell alias
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

`git help st` explains an alias, and the configuration lists all of them:

```text
$ git help st
'st' is aliased to 'status --short'
$ git config --get-regexp '^alias\.'
alias.st status --short
alias.lg log --oneline --graph --all
alias.last log -1 --stat
alias.hello !echo hello from a shell alias
```

*Recorded in Bash; `ch32-custom/expected-alias.bash.txt`.*

Aliases are stored with `--global` in your user configuration, so they follow you across repositories. Keep them few and simple. A short alias for a command you type all the time is useful; an alias that hides what Git does makes your own history harder to read, and makes your instructions to other people unclear. **In this book, every command is typed in full.**

---

## 32.2 Hooks

A **hook** is a script that Git runs automatically at a fixed moment: before a commit, after a merge, before a push.

> **New term: hook.** A script in the `.git/hooks` folder (or in a configured folder) that Git runs at a specific moment, for example before it creates a commit. A hook that exits with a failure status stops the operation.

This hook, `pre-commit`, refuses a commit if `menu.md` contains the word `TODO`. It is a small shell script, written with `printf`, and made executable:

```text
$ cd bakery-menu
$ printf '#!/bin/sh\nif grep -q TODO menu.md; then\n  echo "pre-commit: remove the TODO before committing"\n  exit 1\nfi\n' > .git/hooks/pre-commit
$ chmod +x .git/hooks/pre-commit
```

*Recorded in Bash; `ch32-custom/expected-hook.bash.txt`.*

Now try to commit a file with a TODO in it:

```text
$ printf 'TODO fix the price\n' >> menu.md
$ git commit -am "Add a note"; echo "exit status: $?"
pre-commit: remove the TODO before committing
exit status: 1
```

*Recorded in Bash; `ch32-custom/expected-hook.bash.txt`.*

The hook printed its message and exited with status 1, so **no commit was made**: the change is still waiting, and the log is unchanged:

```text
$ git status --short
 M menu.md
$ git log --oneline
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch32-custom/expected-hook.bash.txt`.*

If you *must* skip a hook, `--no-verify` does so:

```text
$ git commit --no-verify -am "Add a note"
[main 08f6ccc] Add a note
 1 file changed, 1 insertion(+)
$ git log --oneline
08f6ccc (HEAD -> main) Add a note
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch32-custom/expected-hook.bash.txt`.*

Hooks are a real convenience (checking formatting, running tests, catching secrets before they are committed, Chapter 33<!--ref:gitsec-->) with three limits:

1. They are **not copied when someone clones** the repository. Git does not send hooks, for safety:

```text
$ git clone -q . ../copy
$ test -e ../copy/.git/hooks/pre-commit && echo "hook copied" || echo "hook not copied"
hook not copied
```

*Recorded in Bash; `ch32-custom/expected-hook.bash.txt`.*

2. They can be skipped (`--no-verify`), so they are a help and not a security barrier. Anything that must be enforced needs a check on the server too (Chapter 54<!--ref:actions-->).
3. They run **code on your computer**. Never copy a hook from a source that you do not trust.

> **Verification pending [R209].** Git has many hook types (before and after commit, merge, push, and others), and there are server-side hooks that hosting platforms do not offer in the same way. Only `pre-commit` was run. The official list was not checked.

---

## 32.3 Attributes: rules per file

A file named `.gitattributes` gives rules for files that match a pattern. It is part of the project, so it is shared with everyone. Here: text files ending in `.md` are text with LF line endings, and `.bin` files are binary:

```text
$ cd bakery-menu
$ printf '*.md text eol=lf\n*.bin binary\n' > .gitattributes
$ git add .gitattributes
$ git commit -m "Add attributes"
[main 8776a78] Add attributes
 1 file changed, 2 insertions(+)
 create mode 100644 .gitattributes
```

*Recorded in Bash; `ch32-custom/expected-attributes.bash.txt`.*

Ask Git which attributes apply to a file:

```text
$ git check-attr -a menu.md
menu.md: text: set
menu.md: eol: lf
```

*Recorded in Bash; `ch32-custom/expected-attributes.bash.txt`.*

```text
$ git check-attr -a logo.bin
logo.bin: binary: set
logo.bin: diff: unset
logo.bin: merge: unset
logo.bin: text: unset
```

*Recorded in Bash; `ch32-custom/expected-attributes.bash.txt`.*

`binary` is a shortcut that switches off text handling: `text`, `diff` and `merge` become unset. Line endings were the subject of Chapter 4<!--ref:text-->: Windows files often end lines with two characters (CR and LF), Linux and macOS with one (LF). With the `.gitattributes` rule above, a file with Windows endings is *stored* with LF:

```text
$ printf 'one\r\ntwo\r\n' > notes.md
$ git add notes.md
warning: in the working copy of 'notes.md', CRLF will be replaced by LF the next time Git touches it
$ git ls-files --eol notes.md
i/lf    w/crlf  attr/text eol=lf      	notes.md
```

*Recorded in Bash; `ch32-custom/expected-attributes.bash.txt`.*

The warning says exactly this: the working copy has CRLF (`w/crlf`), the copy that Git stores in the index has LF (`i/lf`), and the attribute in force is `text eol=lf`. `git ls-files --eol` shows this for any file, which is the quickest way to debug a line-ending problem.

> **Verification pending [R210].** The wording of the warning can differ between Git versions. The old `core.autocrlf` setting and how it interacts with `.gitattributes` were not run in this chapter.

---

## 32.4 Credential helpers

When Git talks to a remote that needs a password or a token (Chapter 23<!--ref:remotes-->, Chapter 38<!--ref:ghauth-->), it asks a **credential helper** to supply it, or to remember it.

> **New term: credential helper.** A program that Git asks to look up, store or delete a username and password (or token) for a remote address.

Git ships a simple helper called `store`, which writes credentials to a file. It is used here only to *show how the mechanism works*, with a made-up credential (`not-a-real-password`), and a file in the home folder:

```text
$ git config --global credential.helper 'store --file ~/creds'
$ printf 'protocol=https\nhost=example.org\nusername=ada\npassword=not-a-real-password\n\n' | git credential approve
$ cat ~/creds
https://ada:not-a-real-password@example.org
```

*Recorded in Bash; `ch32-custom/expected-credential.bash.txt`.*

`git credential approve` tells the helper to remember a credential. Then the file `~/creds` has this content: **the password, in plain text, in a URL.** Anyone who can read the file can read the password.

> **⚠️ CAUTION.** The `store` helper keeps passwords and tokens **unencrypted** on disk. Do not use it for real credentials. Use the helper that your operating system or your Git installer provides, which keeps secrets in the system's protected store (the names differ between systems, and this chapter did not test them). Chapter 33<!--ref:gitsec--> covers credentials in depth.

`git credential fill` asks the helper for a credential, the way Git does internally:

```text
$ printf 'protocol=https\nhost=example.org\n\n' | git credential fill
protocol=https
host=example.org
username=ada
password=not-a-real-password
```

*Recorded in Bash; `ch32-custom/expected-credential.bash.txt`.*

And `git credential reject` tells the helper to forget it. The file is empty afterwards:

```text
$ printf 'protocol=https\nhost=example.org\nusername=ada\npassword=not-a-real-password\n\n' | git credential reject
$ cat ~/creds; echo "creds file is now empty"
creds file is now empty
```

*Recorded in Bash; `ch32-custom/expected-credential.bash.txt`.*

> **Verification pending [R211].** The credential helpers that ship with Git for Windows, macOS and Linux, and how each stores secrets, were not tested. Only `store` was run, and only with a made-up credential.

---

## 32.5 rerere: remember conflict resolutions

Chapter 22<!--ref:conflicts--> and Chapter 27<!--ref:rebase--> showed that you can resolve the same conflict more than once (for example, when you repeat a merge or rebase). `rerere` stands for "**re**use **re**corded **re**solution".

> **New term: rerere.** A Git feature that records how you resolved a conflict and, when the same conflict appears again, applies your earlier resolution automatically.

Turn it on for the repository, then create the familiar conflict (both branches change the price of the loaf) and merge:

```text
$ cd bakery-menu
$ git config rerere.enabled true
$ git switch -c raise-bread
Switched to a new branch 'raise-bread'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 3.00\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -qam "Raise the white loaf to 3.00"
$ git switch -q main
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.90\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -qam "Raise the white loaf to 2.90"
$ git merge raise-bread
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
Recorded preimage for 'menu.md'
Automatic merge failed; fix conflicts and then commit the result.
```

*Recorded in Bash; `ch32-custom/expected-rerere.bash.txt`.*

Notice the new line: `Recorded preimage for 'menu.md'`. Git kept a copy of the conflicted file. Resolve it as usual, and commit:

```text
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.95\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git add menu.md
$ git commit -m "Merge raise-bread, settling on 2.95"
Recorded resolution for 'menu.md'.
[main a87e5b1] Merge raise-bread, settling on 2.95
```

*Recorded in Bash; `ch32-custom/expected-rerere.bash.txt`.*

`Recorded resolution for 'menu.md'.` Git now knows *how you fixed it*. Undo the merge, to simulate a repeated merge, and try again:

```text
$ git reset --hard HEAD~1
HEAD is now at 5dc50d3 Raise the white loaf to 2.90
$ git merge raise-bread
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
Resolved 'menu.md' using previous resolution.
Automatic merge failed; fix conflicts and then commit the result.
```

*Recorded in Bash; `ch32-custom/expected-rerere.bash.txt`.*

The conflict is reported again (`CONFLICT (content)`), but then: **`Resolved 'menu.md' using previous resolution.`** Look at the file:

```text
$ git status --short
UU menu.md
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.95
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
$ git rerere status
```

*Recorded in Bash; `ch32-custom/expected-rerere.bash.txt`.*

The file already holds 2.95, without markers. The status still says `UU` (unmerged), because Git leaves the final decision to you: check the result, `git add menu.md` and commit.

`rerere` is most useful when you rebase the same branch many times, or when you keep merging in a long-lived branch.

---

## 32.6 What is not covered

- **Merge strategies and drivers** (`git merge -s` and `-X`, custom merge drivers).
- **`git maintenance`**, the scheduled housekeeping (Chapter 30<!--ref:objects--> showed `git gc`).
- **Server-side hooks**, and the many other hook types.

> **Verification pending [R212].** None of these was run for this chapter. They must be tested, or dropped, before the chapter is finished.

---

## Checkpoint

## What You Learned

- Aliases are shortcuts defined in configuration; a leading `!` runs a shell command.
- A hook is a script that runs at a fixed moment; a failing `pre-commit` stops the commit; hooks are not cloned and can be skipped with `--no-verify`.
- `.gitattributes` sets per-file rules such as `text eol=lf` and `binary`; `git check-attr` and `git ls-files --eol` show what applies.
- A credential helper stores and returns passwords; the `store` helper keeps them in plain text.
- `rerere` remembers a conflict resolution and applies it when the same conflict returns.

## New Vocabulary

- **Alias**: a configured shortcut for a Git command.
- **Hook**: a script that Git runs at a specific moment.
- **Credential helper**: a program that stores and supplies credentials.
- **rerere**: a feature that reuses recorded conflict resolutions.

## Commands Learned

`git config alias.<name>`, `git help <alias>`, `git commit --no-verify`, `git check-attr`, `git ls-files --eol`, `git credential approve|fill|reject`, `git config rerere.enabled true`, `git rerere status`.

## Common Mistakes

1. **Aliases that hide what Git does.**
2. **Relying on a hook to enforce a rule.**
3. **Copying a hook from an untrusted source.**
4. **Storing real credentials with `credential.helper store`.**
5. **Committing a resolution that `rerere` applied without reading it.**

## Practice

Do the exercises in [`exercises/ch32-exercises.md`](../../../exercises/ch32-exercises.md).

## Self-Test

1. What does a leading `!` mean in an alias?
2. Why is a hook not a security barrier?
3. What does `git ls-files --eol` tell you?
4. Why is `credential.helper store` unsafe for real passwords?
5. What does `rerere` record, and when does it act?

## Before Moving On

You are ready for Chapter 33<!--ref:gitsec--> if you can:

- [ ] define and use an alias
- [ ] write a simple `pre-commit` hook and bypass it
- [ ] read `git check-attr` and `git ls-files --eol`
- [ ] explain the risk of the `store` helper

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Aliases, including a `!` alias and `git help <alias>` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R208 |
| `pre-commit` blocks a commit; `--no-verify`; hooks not cloned | Locally tested (as above) | R209 |
| `.gitattributes`, `check-attr`, `ls-files --eol`, CRLF warning | Locally tested (as above) | R210 |
| `credential approve/fill/reject` with the `store` helper | Locally tested (as above), made-up credential only | R211 |
| `rerere` recording and reuse | Locally tested (as above) | R208 |
| Other hook types, merge strategies, `maintenance`, OS credential helpers | **Not tested** | R212 |

## Where this leads

Chapter 33<!--ref:gitsec--> returns to secrets and credentials. Chapter 54<!--ref:actions--> shows how automation on a server covers what a local hook cannot enforce.
