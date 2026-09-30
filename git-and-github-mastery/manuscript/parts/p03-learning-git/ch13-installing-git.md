---
key: install
number: 13
tag: Core
first_read: full
status: draft
requires: [terminal, accounts, platforms]
ledger: [R142, R143, R144, R145, R146, R147]
---
# Chapter 13 — Installing Git [Core]

**In this chapter**

- how to find out whether Git is already on your computer
- how to install it on Windows, macOS and Linux, and how to choose safe answers to the installer's questions
- how to prove that the installation worked, and what to do when it did not
- the three settings every new Git user makes first
- how to ask Git for help

**Before you start.** Chapter 7<!--ref:terminal--> (a terminal, commands, `PATH`), Chapter 6<!--ref:accounts--> (why installing from a trusted source matters) and Chapter 12<!--ref:platforms--> (Git is not GitHub). From this chapter on, the book's commands are for you to type: open your terminal now.

Every command in this chapter that is followed by output was run for real, in Bash and in zsh, and the recordings are checked automatically. The installation *steps* for Windows and macOS could not be run in the book's test environment, and are marked as such.

---

## 13.1 What you are installing

Git is a program (Chapter 12<!--ref:platforms-->). Installing it puts the program on your computer and makes the command `git` available in your terminal. There is no account to create and nothing to register.

On **Windows**, the installer that Chapter 7<!--ref:terminal--> described is called *Git for Windows*. It installs Git together with **Git Bash**, the terminal environment in which this book's examples run. On **macOS** and **Linux**, you already have a suitable terminal, and Git is installed as one more program.

---

## 13.2 First, check whether Git is already there

Open your terminal (Git Bash on Windows, Terminal on macOS, your terminal on Linux) and type:

```text
$ git --version
git version <version>
$ command -v git
/usr/bin/git
```

*Recorded in Bash; `ch13-install/expected-install.bash.txt`.*

*Recorded on Linux. The first line shows your Git's version, so your number will differ; recordings in this book mark it `<version>` when they must not depend on it. The second command, `command -v`, asks the shell where it found the program (Chapter 7<!--ref:terminal-->); the path will look different on your computer.*

- If you see a line starting `git version`, Git is installed. Note the version, and you may skip to section 13.6.
- If you see `command not found` (or a message that `git` is "not recognized"), Git is not installed, or its folder is not on your `PATH` (Chapter 7<!--ref:terminal-->). Continue with the section for your system.

> **Partly checked [R145].** The recordings show the behaviour of Git 2.43.0 and of the CI runner's Git on Linux, and Git's manual (2.56.0) confirms that `git --version` prints the version of the Git program. The PowerShell wording of the "not recognized" message is documented by Microsoft (Chapter 7<!--ref:terminal-->); the Command Prompt wording has not been checked.

---

## 13.3 Before you install: three rules

1. **Use the official source.** Get Git from the project's own download page, from your operating system's official package manager, or from your organization's approved source, as Chapter 1<!--ref:computer--> advised. Do not use a link from a message, an advertisement, or a "free tools" website.
2. **Expect an administrator prompt.** Installing a program for all users changes system folders (Chapter 1<!--ref:computer-->). The prompt is legitimate *if you just started the installation*. Refuse an administrator prompt that appears when you did not.
3. **Read each installer screen.** Do not click "Next" without looking. The questions matter (section 13.4), and you learn what your tools do.

---

## 13.4 Windows

> **Checked against the installer's source (R142).** The Git for Windows installer is built from a script in the `git-for-windows/build-extra` repository (fetched from its `main` branch; the copy's hash is in `research/sources-manifest.csv`). It has a page for each decision in the table. **Editor:** "Choosing the default editor used by Git"; the installer's own text says Vim "is the default editor of Git for Windows only for historical reasons, and it is highly recommended to switch to a modern GUI editor instead". **First branch:** "Let Git decide" (using the default branch name of that installer build, `master` in the script) or "Override the default branch name for new repositories", with "main", "trunk" and "development" named as common choices. **PATH:** "Git from the command line and also from 3rd-party software", marked "(Recommended)". **Line endings:** three choices; "Checkout Windows-style, commit Unix-style line endings" is described as "the recommended setting on Windows" for cross-platform projects (it sets `core.autocrlf` to `true`), "Checkout as-is, commit Unix-style line endings" as the recommended one on Unix (`input`), and "Checkout as-is, commit as-is" as "not recommended for cross-platform projects". **Credentials:** a page offers "Git Credential Manager". The installer was not run here, and its pages can change, so the section describes the decisions and not the screens.

1. Open the official Git download page (search for "Git for Windows" and check that the address belongs to the Git project) and download the installer for your version of Windows.
2. Run the installer, and accept the administrator prompt.
3. The installer asks a series of questions. The important ones, and sensible answers for a learner, are:

| Decision | What it means | Recommended for this book |
|---|---|---|
| **Which text editor Git should open** | Git opens an editor when you write a long commit message (Chapter 19<!--ref:commits-->) | An editor you already know (Chapter 3<!--ref:editors-->). Avoid an editor that is hard to exit if you have never used it. |
| **Name of the first branch** | New repositories start with a branch of this name (Chapter 20<!--ref:branching-->) | `main` |
| **How Git is added to your PATH** | Whether `git` works from every terminal, or only in Git Bash | The option that lets you run Git from the command line *and* from other software, so it also works in PowerShell and Command Prompt |
| **Line endings** | How Git converts line endings between Windows (CRLF) and other systems (LF) (Chapter 4<!--ref:text-->) | Read the choices; for cross-platform work the installer recommends "Checkout Windows-style, commit Unix-style line endings" (LF in the repository). Chapter 14<!--ref:config--> returns to this. |
| **The terminal to use with Git Bash** | The window program that displays Git Bash | Either choice works for this book |
| **Credential helper** | Whether Git remembers logins securely (Chapter 38<!--ref:ghauth-->) | Keep the offered default |

Accept the defaults for every decision you do not understand. All of them can be changed later, and none of them can harm your computer.

4. When the installer finishes, **open a new terminal**: search for *Git Bash* and start it. (A terminal opened *before* the installation does not see the new `PATH`; Chapter 7<!--ref:terminal-->.)
5. Type `git --version`.

> **UI-VERSION NOTE.** Installer pages and option names change. If a decision is not in the table, search the installer's help or the official Git for Windows documentation for its name.

---

## 13.5 macOS and Linux

### macOS

> **Checked in part (R143).** The Homebrew package collection has a formula named `git` ("Distributed revision control system", homepage git-scm.com) that at the time of checking built Git 2.56.0 from the project's source tarball. How macOS offers developer tools on first use of `git`, and the Git project's own download page, were **not** checked.

Git may already be present on a Mac; the check in section 13.2 will tell you. If it is not, there are two kinds of source, in order of preference: the one your operating system offers (some systems offer to install developer tools when you first type `git`), and the Git project's own list of installation methods on its download page. Follow the official page for your version, and read what it says before running anything it gives you.

### Linux

Linux systems install programs with a **package manager** (Chapter 1<!--ref:computer-->). On Debian-family systems such as Ubuntu, the package manager is `apt`, and the installation command has this form:

```bash
sudo apt-get install git
```

`sudo` runs the command with administrator permission, and the system may ask for your password. The book's test environment (Ubuntu 24.04) confirmed that this form is valid: the package manager's simulation option (`apt-get install -s git`) reported that Git was already the newest version available, with the package version `1:2.43.0-1ubuntu7.3`. In that label, `2.43.0` is Git's own version; the `1:` prefix and the `-1ubuntu7.3` suffix belong to the distribution's packaging. Distribution packages often lag behind the newest Git release.

> **Verification pending [R144].** Other distributions use other package managers, whose commands were not run. Use your distribution's own documentation, and check the result with `git --version`.

---

## 13.6 Proving that it worked

Whichever way you installed it, check from a new terminal window:

```text
$ git --version
git version <version>
$ command -v git
/usr/bin/git
```

*Recorded in Bash; `ch13-install/expected-install.bash.txt`.*

You need to see `git version` followed by numbers. Three problems account for nearly every failure:

| What you see | Probable cause | What to do |
|---|---|---|
| `command not found` / "not recognized" | The terminal was open during the installation, or `git` is not on the `PATH` | Close the terminal, open a new one, try again. Then check the installation choices (section 13.4). |
| An older version than expected | An older Git earlier on the `PATH` | Run `command -v git` (or `where git` in Command Prompt) to see which one runs |
| A `git` that does something odd | A different program with the same name earlier on the `PATH` | Same check: which program is it? |

If a command finds a program in an unexpected place, the *first* `PATH` entry that contains it wins (Chapter 7<!--ref:terminal-->).

---

## 13.7 Your first three settings

Git records **who** made each version, so before you make your first one you must tell Git your name and email address. You also decide the name of the first branch in new repositories. This is done with `git config`, which Chapter 14<!--ref:config--> explains in depth. For now, type these three commands, replacing the example name and address with your own:

```text
$ git config --global user.name "Ada Learner"
$ git config --global user.email "ada@example.org"
$ git config --global init.defaultBranch main
$ git config --global --list
user.name=Ada Learner
user.email=ada@example.org
init.defaultbranch=main
```

*Recorded in Bash; `ch13-install/expected-install.bash.txt`.*

*Recorded in Bash and zsh (identical), with the fictional user Ada Learner. Nothing is printed after each `git config` command: silence means success (Chapter 7<!--ref:terminal-->). The last command lists what you set. Git lower-cases the setting names in this list: `init.defaultbranch`.*

- `user.name` and `user.email` are written into every commit you make. Use the name and address you are happy for others to see.
- `init.defaultBranch` is the name given to the first branch of every new repository. This book uses `main`.
- `--global` means "for my user account on this computer, in every repository". Chapter 14<!--ref:config--> explains the other scopes.

> **Security note.** An email address written into commits is public if you later share the repository publicly. Some hosting platforms let you use a privacy-preserving address for this purpose; decide before you publish. (That statement is about platforms and is verified in Chapter 37<!--ref:ghaccount-->.)

> **Checked against the documentation (R146).** Git's `user.name` and `user.email` documentation (Git 2.56.0) says the two variables "determine what ends up in the `author` and `committer` fields of commit objects", that the environment variables `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL` and `EMAIL` override them, and that the `name` forms "conventionally refer to some form of a personal name". `init.defaultBranch` "allows overriding the default branch name e.g. when initializing a new repository". The privacy statement is general advice and is not in Git's documentation.

---

## 13.8 Asking Git for help

Git has help built in, in three styles:

1. `git help <command>` opens the **manual page** for a command, for example `git help commit`. On systems where manual pages are installed, it shows the full reference.
2. `git <command> -h` prints a short **summary** of a command's options. It does not depend on manual pages.
3. `git help -a` lists the commands, and `git help -g` lists the conceptual guides.

```text
$ git status -h 2>&1 | head -3
usage: git status [<options>] [--] [<pathspec>...]

    -v, --[no-]verbose    be verbose
```

*Recorded in Bash; `ch13-install/expected-install.bash.txt`.*

*Recorded on Linux. The command `git status -h` prints a usage summary; here the output was shortened to its first three lines with `head -3`, and the `2>&1` joins Git's two output streams so that `head` sees them both. Later lines list the options.*

> **Checked against the documentation (R147).** The `git help` manual page (Git 2.56.0) says the `man` program is used by default, `-a` lists all available commands and `-g` the concept guides. In the book's test environment the manual pages were **not installed**, so `git help <command>` printed a notice about that instead of the manual. That is a fact about that machine, not about Git. On your computer the manual pages are usually available; if they are not, `-h` and the official online documentation (Chapter 35<!--ref:readdocs-->) still work.

---

## 13.9 Keeping Git up to date

Git is updated regularly, and updates repair problems. Update it the way you installed it: with the package manager, or by running the newer installer. Nothing in your repositories is affected, because the way Git stores history is stable. Chapter 35<!--ref:readdocs--> shows how to check the documentation for the version you have.

---

## Checkpoint

## What You Learned

- Installing Git puts the `git` program on your computer; no account is needed.
- Check for Git first with `git --version`; `command not found` means it is missing or not on the `PATH`.
- Install from the official source, expect (only) a legitimate administrator prompt, and read each installer screen.
- On Windows the installer also provides Git Bash; sensible choices are a familiar editor, `main` as the first branch name, and Git available from the command line.
- Verify from a new terminal window; most failures are a stale terminal or a `PATH` problem.
- Set `user.name`, `user.email` and `init.defaultBranch` with `git config --global`.
- Git's help comes as manual pages (`git help`), short summaries (`git <command> -h`) and online documentation.

## New Vocabulary

- **git config**: the command that reads and changes Git's settings.
- **Global setting**: a Git setting that applies to your user account in every repository.

## Commands Learned

`git --version`, `command -v git`, `git config --global user.name`, `git config --global user.email`, `git config --global init.defaultBranch`, `git config --global --list`, `git <command> -h`, `git help`.

## Common Mistakes

1. **Not opening a new terminal after installing.**
2. **Downloading Git from a source that is not official.**
3. **Clicking through installer screens** without reading them.
4. **Skipping `user.name` and `user.email`**, then finding commits recorded under an unwanted identity (Chapter 14<!--ref:config-->).
5. **Confusing the version of the package manager's entry with Git's own version.**
6. **Assuming `git help` works without manual pages installed.**

## Practice

Do the exercises in [`exercises/ch13-exercises.md`](../../../exercises/ch13-exercises.md).

## Self-Test

1. How do you check whether Git is installed?
2. You installed Git while a terminal was open, and `git --version` says the command is not found. What is the likeliest reason, and what do you do?
3. Why must you set `user.name` and `user.email`?
4. What does `--global` mean?
5. Name two ways to get help for `git commit` without using the internet.

## Before Moving On

You are ready for Chapter 14<!--ref:config--> if you can:

- [ ] show `git --version` in your own terminal
- [ ] say where the `git` program was found (`command -v git`)
- [ ] have set your name, email and default branch
- [ ] explain the difference between `git help commit` and `git commit -h`

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `git --version`, `command -v git`, and the three `git config` commands and the listed result; behaviour of the `-h` summary | Locally tested in Bash 5.2 and zsh 5.9 on Git 2.43.0; re-run in CI on the runner's Git | R145, R146 |
| Installer decisions and recommended answers for Windows | Checked against the installer script's source; installer not run | R142 |
| macOS installation methods | Homebrew formula checked; Apple's developer-tools prompt and the Git download page not checked | R143 |
| `apt` install form on Debian-family systems; other distributions | Locally tested for Ubuntu 24.04 (simulation); other distributions unverified | R144 |
| Manual pages not installed in the test environment | Locally observed; environment-specific | R147 |

## Where this leads

Chapter 14<!--ref:config--> explains where Git's settings live, in which order they apply, and why the same command can behave differently on another computer. Chapter 15<!--ref:model--> then describes the parts of Git that the commands work on, and Chapter 16<!--ref:firstrepo--> uses them.
