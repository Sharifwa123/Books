---
key: gitsec
number: 33
tag: Core
first_read: part
status: draft
requires: [tracking, remotes, reflog, accounts]
ledger: [R213, R214, R215, R216, R217]
---
# Chapter 33 — Git Security [Core]

**In this chapter**

- why a secret committed once is a secret leaked
- keeping secrets out of a repository in the first place
- what removing a secret from history does, and does not, achieve
- signing commits, and what a signature proves
- the risks of forced pushes, and of code you did not write
- an incident checklist

**Before you start.** Chapter 18<!--ref:tracking--> (`.gitignore` and the demonstration of a committed secret), Chapter 26<!--ref:reflog-->, Chapter 23<!--ref:remotes--> and Chapter 6<!--ref:accounts-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on Git 2.55.0. **Every secret in this book is made up** (`not-a-real-key`).

---

## 33.1 The core lesson

Chapter 30<!--ref:objects--> showed that Git keeps every version of every file, and that a commit's name depends on everything before it. That is what makes Git reliable. It is also why **a secret that was ever committed stays in the history**, even after you delete the file.

> **New term: secret.** Any value that gives access if someone else has it: a password, a token, an API key, a private key, or a file that contains them.

Here a made-up key is committed in a file called `.env`, and then removed in the next commit:

```text
$ cd bakery-menu
$ printf 'API_KEY=not-a-real-key\n' > .env
$ git add .env
$ git commit -m "Add config"
[main 50ff373] Add config
 1 file changed, 1 insertion(+)
 create mode 100644 .env
$ git rm -q .env
$ git commit -m "Remove the env file"
[main 1cadcfd] Remove the env file
 1 file changed, 1 deletion(-)
 delete mode 100644 .env
```

*Recorded in Bash; `ch33-security/expected-history-rewrite.bash.txt`.*

The latest commit removes the file. The history keeps it:

```text
$ git log --oneline
1cadcfd (HEAD -> main) Remove the env file
50ff373 Add config
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git show HEAD~1:.env
API_KEY=not-a-real-key
$ git log --all --oneline -S"not-a-real-key"
1cadcfd (HEAD -> main) Remove the env file
50ff373 Add config
```

*Recorded in Bash; `ch33-security/expected-history-rewrite.bash.txt`.*

`git show HEAD~1:.env` prints the key from the earlier commit, and `git log -S` (Chapter 24<!--ref:stash-->) finds both commits that touch it. Anyone who has a copy of this repository has the secret. Deleting the file changed nothing about that.

> **⚠️ CAUTION.** If a real secret reaches a repository that anyone else can read, assume that it is **compromised**. The first step is **not** to clean the history. It is to **revoke or rotate the secret** (make it stop working, and issue a new one) at the place that issued it. Only then is cleaning worth considering.

---

## 33.2 Keeping secrets out

Prevention is much cheaper than cleanup.

**Keep secrets in files that Git ignores.** A `.env` file is a common place for settings. Put its name in `.gitignore` (Chapter 18<!--ref:tracking-->):

```text
$ cd bakery-menu
$ printf '.env\n' > .gitignore
$ printf 'API_KEY=not-a-real-key\n' > .env
$ git status --short
?? .gitignore
$ git check-ignore -v .env
.gitignore:1:.env	.env
```

*Recorded in Bash; `ch33-security/expected-ignore.bash.txt`.*

The file exists, but `git status` does not list it, and `git check-ignore -v` names the rule that hides it. Git even refuses a normal `git add`:

```text
$ git add .env
The following paths are ignored by one of your .gitignore files:
.env
hint: Use -f if you really want to add them.
hint: Turn this message off by running
hint: "git config advice.addIgnoredFile false"
```

*Recorded in Bash; `ch33-security/expected-ignore.bash.txt`.*

*(On newer Git versions, 2.55.0 was tested, the last two hint lines are replaced by one: `hint: Disable this message with "git config set advice.addIgnoredFile false"`. The refusal is the same.)*

But **`-f` overrides the rule**, and nothing stops you:

```text
$ git add -f .env
$ git status --short
A  .env
?? .gitignore
```

*Recorded in Bash; `ch33-security/expected-ignore.bash.txt`.*

So `.gitignore` is a safety net for mistakes, not a lock. Add a few more habits:

- **Read `git status` and `git diff --staged` before every commit** (Chapter 19<!--ref:commits-->).
- **Keep example files without real values** (for example `.env.example`) in the repository, and the real one out of it.
- **A hook** can check for obvious secrets before a commit (Chapter 32<!--ref:custom-->), but it can be skipped, so it does not replace the habits above.
- **Give each token the least power that works**, and a short life. A stolen token with little power does little harm.

> **Checked against GitHub's documentation (R214).** GitHub's secret-scanning documentation says it "scans your entire Git history on all branches of your repository for hardcoded credentials", raises an alert, and advises: "rotate the affected credential immediately"; removing a secret from the history "is time-intensive and often unnecessary if you've already revoked the credential". **Push protection** "blocks pushes that contain secrets before they reach your repository", including command-line pushes; for repositories it "is disabled by default" and "requires GitHub Secret Protection to be enabled", while push protection *for users* "is enabled by default" and stops you from pushing secrets to public repositories. On branches, GitHub's documentation says a protected-branch rule blocks force pushes and deletion by default. Which plans include each feature is time-sensitive and was not checked. Chapter 62<!--ref:ghsec--> covers it.

---

## 33.3 If it already happened

The order of steps matters.

1. **Revoke or rotate the secret** at its source. Do this first, and do it even if you think nobody saw it. From this point the leaked value is useless.
2. **Find out where it went**: which branches, which remotes, which forks or copies, and which builds or logs.
3. **Only then, remove it from history** if you need to. Removal does not un-leak the secret. Its purpose is to stop it from spreading and to make the repository clean.

For step 3, Git's own older command for rewriting history (`git filter-branch`) has a long list of problems, and Git's documentation recommends a separate tool, **git-filter-repo**. It is not part of Git; it is a script that you install separately (this book used version 2.47.0, from the Python package index). In the example below, it removes every trace of `.env`:

```text
$ git filter-repo --path .env --invert-paths --force
Parsed 5 commits
New history written in <n> seconds; now repacking/cleaning...
Repacking your repo and cleaning out old unneeded objects
HEAD is now at 81f772e Add coconut cake
Completely finished after <n> seconds.
```

*Recorded in Bash; `ch33-security/expected-history-rewrite.bash.txt`.*

It reported the commits it processed, and then it rewrote history. Look at the result:

```text
$ git log --oneline
81f772e (HEAD -> main) Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git log --all --oneline -S"not-a-real-key"
```

*Recorded in Bash; `ch33-security/expected-history-rewrite.bash.txt`.*

The two commits that touched `.env` are **gone**, not just the file. The old ones, and the ones after them, all have **new hashes** (here there were none after them, and the earlier ones are unchanged because they come before the change). The key is no longer found in any commit (the search prints nothing):

```text
$ git log --all --oneline -S"not-a-real-key"
```

*Recorded in Bash; `ch33-security/expected-history-rewrite.bash.txt`.*

> **Checked against the documentation (R215).** The `git filter-branch` manual page (Git 2.56.0) opens with a WARNING: the command "has a plethora of pitfalls", its "safety and performance issues cannot be backward compatibly fixed", "its use is not recommended", and it asks readers to "use an alternative history filtering tool such as git filter-repo". The `git-filter-repo` manual (version 2.47.0) says the tool aborts "if run from a repo that is not a fresh clone", and that by default it removes the `origin` remote (its `--force` option disables that check). The tool here was run only on a repository with no remote; on a repository with a remote, the rewritten history has to be pushed, which is a forced push (section 33.5).

What a rewrite does **not** do:

- It does **not** remove copies that other people already have: clones, forks, and downloads.
- It does **not** remove the secret from a hosting platform's caches, or from pull requests or other places that the platform keeps. Whether and how the platform removes it is time-sensitive and was not verified.
- It does **not** make the secret safe again. Only step 1 does.

That is why the order is **revoke first**.

---

## 33.4 Signing commits

Anyone can write any name and email into a commit (Chapter 14<!--ref:config-->). Nothing in Git stops you from committing as someone else. A **signature** adds proof that the commit was made by the holder of a particular key.

> **New term: signed commit.** A commit that carries a cryptographic signature made with the author's private key, so that others can check it against the matching public key.

The recording uses **GPG** (a widely installed signing tool) with a key created just for the demonstration. One commit is signed with `-S`, and one is not:

```text
$ cd bakery-menu
$ gpg --batch --passphrase '' --quick-gen-key "Ada Learner <ada@example.org>" default default never 2>/dev/null; echo "key created: $?"
key created: 0
$ git config user.signingkey "ada@example.org"
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -q -S -am "Add tea (signed)"
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -q -am "Add coffee (unsigned)"
```

*Recorded in Bash; `ch33-security/expected-sign.bash.txt`.*

Ask Git whether the signatures are good, with the format code `%G?`:

```text
$ git log --format='%G? %GS: %s' -3
N : Add coffee (unsigned)
G Ada Learner <ada@example.org>: Add tea (signed)
N : Add coconut cake
```

*Recorded in Bash; `ch33-security/expected-sign.bash.txt`.*

`G` means a good signature, made by the key of `Ada Learner`. `N` means no signature. (Other letters exist for bad or unverifiable signatures. Only `G` and `N` were run here.)

Two things a signature proves, and two that it does not:

- It **proves** that the holder of the key made the commit, and that the commit was not changed afterwards.
- It does **not** prove that the person is who they say (that depends on how you came to trust the key), and it does not prove that the code is safe.

Chapter 14<!--ref:config--> showed the other side: what happens if signing is switched on but the key is unavailable. Git can also sign with an SSH key; Chapter 38<!--ref:ghauth--> runs that (with a demonstration key). The way hosting platforms show a "verified" mark was **not** run.

> **Checked against GitHub's documentation (R216).** GitHub marks a commit or tag with a verifiable GPG, SSH or S/MIME signature "Verified" (or "Partially verified"); the default statuses are Verified, Unverified and none for an unsigned commit; and "vigilant mode" is off by default. SSH-key signing on the Git side is in Chapter 38<!--ref:ghauth-->, with the platform side.

---

## 33.5 Force pushes

Chapter 23<!--ref:remotes--> showed a rejected push and warned against forcing it. Here is the reason.

A **forced push** (`git push --force`) makes the remote branch match yours, even if that discards commits that others have pushed. It is what you must do after rewriting history that is already shared (Chapter 27<!--ref:rebase-->, section 33.3). Consequences:

- Other people's work can be **lost** from the shared branch.
- Everyone who already has the old history now has a history that **conflicts** with the new one.
- Hosting platforms can **protect** branches against forced pushes. (Whether and how was not verified for this chapter; see Chapter 62<!--ref:ghsec-->.)

Rules of thumb: never force-push to a shared branch without agreement; use a forced push only on your own branches; and prefer `git revert` (Chapter 25<!--ref:undo-->) for shared history.

---

## 33.6 Code you did not write

Whenever you clone a repository, install a package, or copy a script, you run or trust **someone else's code**.

- **Hooks** (Chapter 32<!--ref:custom-->) and scripts in a cloned repository run with your permissions. Read them first.
- **Submodules** (Chapter 31<!--ref:bigrepos-->) pull code from another address. Git refuses local-path submodules by default, as the recording in that chapter showed.
- **Dependencies** (packages) can change, or be replaced by malicious versions. Pin versions, and review what you add. (Ways to do this on a hosting platform are in Chapter 62<!--ref:ghsec-->.)

> **Verification pending [R217].** This section states general good practice, not tested facts. **No real-world incident is named in this chapter**: none was researched and verified from a primary source, and the book does not repeat incidents from memory. If a later revision adds incident examples, each must be verified and cited.

---

## 33.7 Incident checklist: "I committed a secret"

1. **Stop.** Do not try to hide it by deleting the file.
2. **Revoke or rotate** the secret at its source.
3. **Check for misuse**: look at the service's access logs for uses that were not yours.
4. **Find every copy**: branches, remotes, forks, clones, builds, and pasted messages.
5. **Decide whether to rewrite history.** If you do, agree it with everyone who shares the repository, use a maintained tool, and expect to force-push.
6. **Tell the people who need to know**, following your organization's rules.
7. **Add a prevention**: `.gitignore`, an example file, a hook or a scanner, and a note in the project's documentation.

---

## Checkpoint

## What You Learned

- A committed secret stays in history after the file is deleted; the first response is to revoke it.
- `.gitignore` keeps mistakes out, but `git add -f` overrides it; read what you stage.
- `git-filter-repo` can rewrite history to remove a file entirely; the rewrite does not remove copies that others have, and does not make the secret safe.
- A signed commit proves which key made it (`%G?` shows `G` for good, `N` for none); it does not prove trust or safety.
- A forced push overwrites shared history and can lose others' work.
- Hooks, submodules and dependencies are other people's code running with your permissions.

## New Vocabulary

- **Secret**: a value that gives access if someone else has it.
- **Signed commit**: a commit carrying a cryptographic signature that others can verify.

## Commands Learned

`git log -S`, `git show <commit>:<path>`, `git check-ignore -v`, `git add -f`, `git filter-repo --path <path> --invert-paths`, `git commit -S`, `git log --format=%G?`.

## Common Mistakes

1. **Cleaning the history before revoking the secret.**
2. **Believing that deleting a file removes its history.**
3. **Using `git add -f` to get past a `.gitignore` warning.**
4. **Force-pushing a shared branch.**
5. **Running a hook or script that was not read first.**

## Practice

Do the exercises in [`exercises/ch33-exercises.md`](../../../exercises/ch33-exercises.md). Use only made-up secrets.

## Self-Test

1. A file with a secret was deleted in the last commit. Is the secret safe? Why not?
2. What is the first step after committing a real secret?
3. What does `git check-ignore -v .env` show?
4. What does `%G?` print for a good signature, and for an unsigned commit?
5. Name two things that rewriting history does *not* fix.

## Before Moving On

You are ready for Chapter 34<!--ref:workflows--> if you can:

- [ ] explain why deleting a committed secret is not enough
- [ ] state the order: revoke, find, then clean
- [ ] keep a `.env` file out of a repository
- [ ] say what a signature proves and what it does not

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A deleted secret is still in history; `git log -S` finds it | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R213 |
| `.gitignore`, `check-ignore`, `add` refusal and `-f` | Locally tested (as above). Some concept and option statements for this row were also checked in the Git 2.56.0 manual (gitignore); the ledger row says which. | R213 |
| `git filter-repo` removes a path from all history (no remote); `filter-branch` not recommended | Locally tested with git-filter-repo 2.47.0 (also installed in CI); warning text and fresh-clone rule checked in the manuals | R215 |
| GPG-signed commit shows `G`; unsigned shows `N` | Locally tested with GnuPG and a throw-away key | R216 |
| Platform secret scanning, push protection, protected branches, "Verified" marks | Checked against `github/docs` (commit `2eaab0b`); plans and prices not checked; not run on a live account | R214, R216 |
| SSH-key signing | Run in Chapter 38<!--ref:ghauth--> (Git side only) | R236 |
| Supply-chain and incident guidance | General practice, **not tested**; no incident named | R217 |

## Where this leads

Chapter 34<!--ref:workflows--> shows how teams organise their branches. Chapter 38<!--ref:ghauth--> covers tokens and SSH keys on the platform, and Chapter 62<!--ref:ghsec--> returns to secret scanning, protected branches and dependency security, once their facts are verified.
