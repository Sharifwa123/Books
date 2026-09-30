---
key: config
number: 14
tag: Core
first_read: full
status: draft
requires: [install]
ledger: [R148, R149, R150, R151]
---
# Chapter 14 — Configuration Scopes and Environments [Core]

**In this chapter**

- what a Git *setting* is, and the four *scopes* (levels) at which it can be stored
- how to see which value Git is really using, and where it came from
- how one command can override a setting for a moment
- how the environment of your computer changes what Git does
- why the same command can behave differently on another computer, shown with a real failure
- how to test Git commands in a clean, isolated environment

**Before you start.** Chapter 13<!--ref:install-->: you have used `git config --global` to set your name, email and default branch. Chapter 7<!--ref:terminal--> introduced environment variables, which return here.

Every command with output in this chapter was run for real, in Bash and in zsh, on Git 2.43.0, and re-run in CI on a newer Git. The recordings use the fictional user Ada Learner.

---

## 14.1 What a setting is

Git does not behave the same way for everybody, because it is *configurable*. Your name and email, the name of the first branch, which editor to open, how to treat line endings, whether to sign commits: each is a **setting**.

> **New term: configuration (setting).** A named value that changes how Git behaves. A setting has a name of the form `section.name` (for example `user.email`) and a value.

You read and change settings with the command you met in Chapter 13<!--ref:install-->:

```text
git config user.email
git config user.email "ada@example.org"
```

The first form **reads** the value; the second **writes** it. But a setting can be stored in several *places*, and that is the subject of this chapter.

---

## 14.2 Four scopes

> **New term: scope.** The level at which a setting is stored, which decides how widely it applies.

Git reads settings from up to four places, from the widest to the narrowest.

| Scope | Applies to | Where it is stored | Written with |
|---|---|---|---|
| **System** | Every user of this computer | A file that belongs to the Git installation (its location depends on how Git was installed) | `git config --system` (usually needs administrator permission) |
| **Global** | You, in every repository | A file in your home folder, `.gitconfig` | `git config --global` |
| **Local** | One repository | The file `.git/config` inside that repository | `git config --local` (the default when you are inside a repository and give no scope) |
| **Worktree** | One working tree of a repository (Chapter 31<!--ref:bigrepos-->) | A separate file, and only when enabled | `git config --worktree` |

> **Checked against the documentation (R148).** The `git config` manual (Git 2.56.0) lists the files: the system file `$(prefix)/etc/gitconfig`; the user files `$XDG_CONFIG_HOME/git/config` and `~/.gitconfig` (with `$HOME/.config/` used when `XDG_CONFIG_HOME` is not set), "also called 'global'", both read if both exist; the repository file `$GIT_DIR/config`; and the optional `$GIT_DIR/config.worktree`, which is "only searched when `extensions.worktreeConfig` is present". The files are read in that order, "with last value found taking precedence". "By default, options are only written to the repository specific configuration file", and `git config` "will only ever change one file at a time". Where the system file lives on Windows and macOS was not tested: the documentation gives only the build-time `$(prefix)/etc/gitconfig`.

The rule for *conflicts* is simple and worth memorising: **the narrower scope wins.** If `user.email` is set globally and again locally, Git uses the local one in that repository. In order of increasing priority: system, global, local, worktree.

### 14.2.1 See it work: local beats global

The recording below starts with a global email, creates a repository, adds a different local email, and reads the value each time. Read each result, and compare with the rule:

```text
$ git config --global user.name "Ada Learner"
$ git config --global user.email "ada@example.org"
$ git init -b main scopes-demo
Initialized empty Git repository in /home/learner/scopes-demo/.git/
$ cd scopes-demo
$ git config user.email
ada@example.org
$ git config --local user.email "ada.work@example.net"
$ git config user.email
ada.work@example.net
$ git config --show-origin --show-scope user.email
local	file:.git/config	ada.work@example.net
$ git config --get-all user.email
ada@example.org
ada.work@example.net
```

*Recorded in Bash; `ch14-config/expected-scopes.bash.txt`.*

- The global value, `ada@example.org`, was used until a local value existed.
- After the local value was set, `git config user.email` printed the **local** one.
- `--show-origin --show-scope` told us *where* the winning value came from: scope `local`, file `.git/config`.
- `--get-all` showed **both** values, from all scopes, in order from widest to narrowest. Git uses the last.

### 14.2.2 Removing settings, and what "unset" looks like

```text
$ git config --global --unset user.email
$ git config --local --unset user.email
$ git config user.email; echo "exit code: $?"
exit code: 1
```

*Recorded in Bash; `ch14-config/expected-scopes.bash.txt`.*

After both values were removed, `git config user.email` printed nothing at all, and its **exit code** was 1. (Chapter 7<!--ref:terminal--> noted that most commands print nothing on success. Here the silence means *no value*, and the exit code says so.) A Git that has no email will later refuse to create a commit, or guess an address from your computer's name, which is why Chapter 13<!--ref:install--> asked you to set one.

---

## 14.3 The system scope, simulated

The system scope needs administrator permission to change, so to *see* it safely, the next recording builds a stand-in. It writes a small file into the home folder and points Git at it with the environment variable `GIT_CONFIG_SYSTEM`. (You will not need to do this in your own work; it is a way to observe how the scopes stack.)

```text
$ printf '[demo]\n\tlevel = system\n' > "$HOME/system.gitconfig"
$ export GIT_CONFIG_SYSTEM="$HOME/system.gitconfig"
$ git init -b main levels-demo
Initialized empty Git repository in /home/learner/levels-demo/.git/
$ cd levels-demo
$ git config demo.level
system
$ git config --global demo.level global
$ git config demo.level
global
$ git config --show-scope --get-all demo.level
system	system
global	global
$ git config --local demo.level local
$ git config demo.level
local
$ git config --show-scope --get-all demo.level
system	system
global	global
local	local
```

*Recorded in Bash; `ch14-config/expected-levels.bash.txt`.*

Each `git config demo.level ...` command changed a different scope, and each time the value Git used moved to the narrowest one. The `--show-scope --get-all` lines show the whole stack: `system`, then `global`, then `local`.

```text
$ git config --show-origin --get-all demo.level
file:/home/learner/system.gitconfig	system
file:/home/learner/.gitconfig	global
file:.git/config	local
```

*Recorded in Bash; `ch14-config/expected-levels.bash.txt`.*

`--show-origin` names the files: the system file, the global file `~/.gitconfig`, and the local file `.git/config`.

> **Deep.** The fourth scope, *worktree*, exists for repositories with several working trees (Chapter 31<!--ref:bigrepos-->). It must be switched on with `extensions.worktreeConfig`. The recording shows that once it is on, its value wins over the local one:
>
> ```text
> $ git config extensions.worktreeConfig true
> $ git config --worktree demo.level worktree
> $ git config demo.level
> worktree
> $ git config --show-scope --get-all demo.level
> system	system
> global	global
> local	local
> worktree	worktree
> ```
>
> *Recorded in Bash; `ch14-config/expected-levels.bash.txt`.*

---

## 14.4 Overriding for one command, or for one shell

Sometimes you want a different value for a moment without changing any file.

**One command: `-c`.** Put `-c name=value` between `git` and the command:

```text
$ git config --global user.email "ada@example.org"
$ git -c user.email="temporary@example.invalid" config user.email
temporary@example.invalid
```

*Recorded in Bash; `ch14-config/expected-scopes.bash.txt`.*

The temporary value was used for that command only. It changed no file.

**One shell, or one command: environment variables.** Git reads environment variables (Chapter 7<!--ref:terminal-->) that change *where* it looks for settings:

| Variable | Effect |
|---|---|
| `GIT_CONFIG_GLOBAL` | Use this file instead of `~/.gitconfig` for the global scope. `/dev/null` means "no global settings". |
| `GIT_CONFIG_SYSTEM` | Use this file instead of the system file. |
| `GIT_CONFIG_NOSYSTEM` | If set to `1`, ignore the system file. |

The first recording line below hides the global settings for a single command; the next shows they were untouched:

```text
$ GIT_CONFIG_GLOBAL=/dev/null git config user.email; echo "exit code: $?"
exit code: 1
$ git config user.email
ada@example.org
```

*Recorded in Bash; `ch14-config/expected-scopes.bash.txt`.*

The exit code 1 shows that with no global file, `user.email` had no value; afterwards, the ordinary command sees the global file again. The last recording of the scope demonstration shows that `GIT_CONFIG_NOSYSTEM=1` removes the system scope from the stack even though `GIT_CONFIG_SYSTEM` was set:

```text
$ GIT_CONFIG_NOSYSTEM=1 git config --show-scope --get-all demo.level
global	global
local	local
worktree	worktree
```

*Recorded in Bash; `ch14-config/expected-levels.bash.txt`.*

**Precedence, summarised.** For one command Git combines: system, then global, then local, then worktree, then `-c` on the command line, in that increasing order of priority. (A few settings can also be overridden by their own environment variables.) `-c` and the environment variables are the tools to use when you need an *exact*, reproducible environment, which is the subject of section 14.7.

> **Checked against the documentation (R149).** The `git` manual (Git 2.56.0) says of `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_SYSTEM`: they "take the configuration from the given files instead from global or system-level configuration files", and can be set to `/dev/null` to skip reading the files of that level. `GIT_CONFIG_NOSYSTEM` is a Boolean that skips the system-wide file, and the manual says it can be used with `$HOME` and `$XDG_CONFIG_HOME` "to create a predictable environment for a picky script", which is how the recordings are made.

---

## 14.5 Why the same command behaves differently on another computer

This is the reason for the whole chapter. Two people run the same Git command on the same repository and get different results. The commonest cause is **settings that one of them inherited**, from a system file, a global file or an included file, that the other does not have.

Here is a real failure, reproduced on purpose. A computer's global settings say: sign every commit, use an SSH key for signing, and use a program that does not exist for the job. (Signing commits is explained in Chapter 33<!--ref:gitsec-->; you do not need it now. Many employers set this up for their staff, and a laptop that has been configured that way can surprise its owner.)

```text
$ git config --global user.name "Ada Learner"
$ git config --global user.email "ada@example.org"
$ git init -b main signing-demo
Initialized empty Git repository in /home/learner/signing-demo/.git/
$ cd signing-demo
$ echo "Sunrise Bakery" > README.md
$ git add README.md
$ git config --global commit.gpgsign true
$ git config --global gpg.format ssh
$ git config --global gpg.ssh.program false
$ git commit -m "Add README"
fatal: either user.signingkey or gpg.ssh.defaultKeyCommand needs to be configured
$ git status --short
A  README.md
```

*Recorded in Bash; `ch14-config/expected-signing.bash.txt`.*

Look at what happened. The learner typed an ordinary `git commit -m "Add README"`. Nothing in that command mentions signing, yet Git stopped with:

```text
fatal: either user.signingkey or gpg.ssh.defaultKeyCommand needs to be configured
```

The file was staged (`A  README.md`) but *not* committed. The cause was not in the command, the repository, or the file; it was an **inherited setting**. The next lines show how to find it and how to get past it:

```text
$ git config --show-origin --get commit.gpgsign
file:/home/learner/.gitconfig	true
$ git -c commit.gpgsign=false commit -m "Add README"
[main (root-commit) c3f6cc7] Add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
$ git log --oneline
c3f6cc7 (HEAD -> main) Add README
$ GIT_CONFIG_GLOBAL=/dev/null git config commit.gpgsign; echo "exit code: $?"
exit code: 1
```

*Recorded in Bash; `ch14-config/expected-signing.bash.txt`.*

Two things solved the puzzle:

1. `git config --show-origin --get commit.gpgsign` said that the value `true` came from the global file, `~/.gitconfig`. That is the *diagnostic habit*: ask Git where a value comes from.
2. `git -c commit.gpgsign=false commit ...` showed that the command works when the setting is overridden for one command.

The last line, with `GIT_CONFIG_GLOBAL=/dev/null`, showed that with no global file the setting does not exist. (You would then decide whether to change the global file, or to keep signing and configure a key properly.)

> **Note on the error text (R150).** The error text shown is what Git 2.43.0 printed in this exact configuration. Other configurations produce other messages. The same recording is re-run in CI on Git 2.55.0, and a difference in Git's wording would show up there as a failing check.

### 14.5.1 Settings that commonly differ between computers

| Setting | Effect when it differs |
|---|---|
| `commit.gpgsign`, `user.signingkey` | Commits are signed, or fail to be (as above) |
| `core.autocrlf`, `core.eol` | Line endings are converted differently (Chapter 4<!--ref:text-->) |
| `pull.rebase`, `pull.ff` | `git pull` merges, rebases or refuses (Chapter 23<!--ref:remotes-->) |
| `init.defaultBranch` | The first branch is `main` on one computer and `master` on another |
| `core.editor` | A different editor opens for commit messages |
| `credential.helper` | Passwords and tokens are remembered differently (Chapter 38<!--ref:ghauth-->) |
| `alias.*` | Commands mean something different because of a personal shortcut (Chapter 32<!--ref:custom-->) |
| `include.path`, `includeIf` | Extra files change any of the above (section 14.6) |

### 14.5.2 A diagnostic routine

When Git behaves unexpectedly:

1. Say exactly what happened (the command and the message).
2. List where the relevant settings come from: `git config --show-origin --show-scope --get-all <name>`.
3. Reproduce with a clean environment (section 14.7) to see whether a setting is responsible.
4. Change the setting at the scope where it belongs, not everywhere.

---

## 14.6 Conditional includes [Deep]

A configuration file can *include* another, and the include can apply only inside certain folders. That is how a person keeps one email address for work projects and another for personal ones.

> **Deep.** Here the global file includes a work file only for repositories under `~/work/`. The same command prints different values in two repositories:
>
> ```text
> $ git config --global user.name "Ada Learner"
> $ git config --global user.email "ada@example.org"
> $ mkdir -p work/project personal/project
> $ printf '[user]\n\temail = ada@work.example.net\n' > ~/.gitconfig-work
> $ git config --global includeIf.gitdir:~/work/.path ~/.gitconfig-work
> $ cat ~/.gitconfig
> [user]
> 	name = Ada Learner
> 	email = ada@example.org
> [includeIf "gitdir:~/work/"]
> 	path = /home/learner/.gitconfig-work
> $ cd work/project
> $ git init -q
> $ git config user.email
> ada@work.example.net
> ```
>
> *Recorded in Bash; `ch14-config/expected-include.bash.txt`.*

The `includeIf "gitdir:~/work/"` line means: for repositories whose `.git` folder is under `~/work/`, also read the given file. Inside `work/project`, `git config user.email` printed the work address, and `--show-origin` proved that it came from `.gitconfig-work`; in `personal/project`, the global address applied.

> **Checked against the documentation (R151).** The `git config` manual (Git 2.56.0) documents `includeIf` with the conditions `gitdir`, `gitdir/i` (case-insensitive), `onbranch`, `hasconfig:remote.*.url` and `worktree`. For `gitdir`, a pattern ending in `/` gets `**` added ("it matches 'foo' and everything inside, recursively"), a pattern that does not start with `~/`, `./` or `/` gets `**/` put in front, and `../` "is not special and will match literally". Both the symlink and the real path of a directory match. Behaviour of `gitdir:` patterns for unusual paths (for example on Windows) was not tested.

---

## 14.7 Testing in a clean environment

Everything above suggests a rule for anyone who writes instructions, scripts or tests that involve Git, including this book's author: **do not test in your own environment. Test in an isolated one.** Your global settings, your system file and your environment variables all leak into your tests, so a command that "works for me" might depend on a setting that nobody else has.

A clean environment for one command needs three things:

1. **A private home folder**, so that `~/.gitconfig` is not yours.
2. **`GIT_CONFIG_GLOBAL=/dev/null`** and **`GIT_CONFIG_NOSYSTEM=1`** (or an explicit `GIT_CONFIG_SYSTEM` file you control), so that no outside settings apply.
3. **Explicit settings for everything the test needs** (name, email, default branch).

Every recording in this book is made this way. A test harness starts a fresh home for each recording, points system settings at nothing, and sets the few settings the example needs, so that the recordings show *Git's* behaviour and not one particular laptop's. When you write a script for your team, do the same, or someone's inherited settings will one day break it.

---

## 14.8 Settings you will meet later

Do not change these now, but recognise their names when they appear.

- `core.editor`: the editor Git opens (Chapter 19<!--ref:commits-->).
- `core.autocrlf` and `.gitattributes`: line-ending conversion (Chapter 32<!--ref:custom-->).
- `core.excludesFile`: your personal ignore list (Chapter 18<!--ref:tracking-->).
- `pull.rebase` and `pull.ff`: what `git pull` does (Chapter 23<!--ref:remotes-->).
- `alias.<name>`: your own shortcuts (Chapter 32<!--ref:custom-->).
- `commit.gpgsign`, `gpg.format`, `user.signingkey`: signing (Chapter 33<!--ref:gitsec-->).
- `credential.helper`: remembering logins (Chapter 38<!--ref:ghauth-->).

> **Security note.** Never copy a block of Git settings from a stranger's web page or a "dotfiles" repository without reading it. A setting can run a program (for example an editor, a credential helper or an alias that starts with `!`), so a copied file can do anything you can do.

---

## Checkpoint

## What You Learned

- A Git setting is a named value; it can live in the system, global, local or worktree scope, and the narrower scope wins.
- `git config <name>` reads the effective value; `--show-origin --show-scope --get-all` shows every value and where it came from.
- Writing defaults to the local file inside a repository; `--global` and `--system` write to the wider scopes.
- `-c name=value` overrides a setting for one command; `GIT_CONFIG_GLOBAL`, `GIT_CONFIG_SYSTEM` and `GIT_CONFIG_NOSYSTEM` change which files are read.
- An inherited setting can change what a command does, so the same command can fail on another computer; the diagnostic habit is to ask where a value came from.
- Conditional includes give different settings in different folders.
- Test Git commands in an isolated environment.

## New Vocabulary

- **Configuration (setting)**: a named value that changes how Git behaves.
- **Scope**: the level (system, global, local or worktree) at which a setting is stored.
- **Override**: to replace a setting's value for one command or one shell.

## Commands Learned

`git config <name>`, `git config --local|--global|--system|--worktree <name> <value>`, `git config --unset`, `git config --show-origin`, `git config --show-scope`, `git config --get-all`, `git -c name=value <command>`, and the environment variables `GIT_CONFIG_GLOBAL`, `GIT_CONFIG_SYSTEM`, `GIT_CONFIG_NOSYSTEM`.

## Common Mistakes

1. **Setting a value at the wrong scope**, then wondering why another repository behaves differently.
2. **Assuming your settings are everyone's.** A friend's computer has different ones.
3. **Not checking where a value came from** when behaviour is unexpected.
4. **Copying configuration from the internet** without reading it.
5. **Testing scripts in your own environment.**

## Practice

Do the exercises in [`exercises/ch14-exercises.md`](../../../exercises/ch14-exercises.md).

## Self-Test

1. Name the four scopes, from widest to narrowest.
2. `user.email` is set globally and locally. Which does Git use, and how can you prove where the winning value came from?
3. What does the exit code 1 of `git config user.email` tell you?
4. How do you override a setting for a single command?
5. A colleague's commit fails with a signing error that yours does not. What is your first diagnostic step?
6. Why should tests of Git commands run in an isolated environment?

## Before Moving On

You are ready for Chapter 15<!--ref:model--> if you can:

- [ ] list the scope and file of a setting with one command
- [ ] set a value locally and see it override the global value
- [ ] override a setting for one command with `-c`
- [ ] explain how an inherited setting can break a command

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Scopes, precedence, `--show-origin`, `--show-scope`, `--get-all`, unset behaviour and exit codes; worktree scope with `extensions.worktreeConfig` | Both: run in Bash 5.2 and zsh 5.9 on Git 2.43.0 and re-run in CI on a newer Git; checked against the Git 2.56.0 manual | R148 |
| `-c`, `GIT_CONFIG_GLOBAL`, `GIT_CONFIG_SYSTEM`, `GIT_CONFIG_NOSYSTEM` | Same; variables checked in the `git` manual | R149 |
| The inherited-signing failure and its message | Locally tested; the message is version- and configuration-specific | R150 |
| `includeIf "gitdir:"` | Locally tested; conditions and matching rules checked in the Git 2.56.0 manual | R151 |

## Where this leads

Chapter 15<!--ref:model--> describes the parts of Git that these settings and the following commands act on: the working tree, the index, the repository and HEAD. Chapter 32<!--ref:custom--> returns to settings that change Git's behaviour permanently: aliases, hooks, attributes and credential helpers. Chapter 33<!--ref:gitsec--> explains commit signing, the setting that broke a commit in section 14.5.
