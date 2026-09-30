---
key: ghrepo
number: 39
tag: Core
first_read: full
status: draft
requires: [ghauth, remotes]
ledger: [R237, R238, R239, R240]
---
# Chapter 39 — Your First GitHub Repository [Core]

**In this chapter**

- two ways to get a project onto GitHub: start there, or start on your computer
- what the platform's "create a repository" choices mean
- connecting an existing repository, and the "unrelated histories" surprise
- cloning, and the daily cycle of push, fetch and pull
- **Project 3**: publish the Sunrise Bakery website

> **How to read this chapter.** The **Git** commands here were run against local bare repositories that behave like a new, empty remote. What the **website** offers is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026), but was **not** run on a live account, so the chapter names the *choices* and not the exact position of buttons.

**Before you start.** Chapter 38<!--ref:ghauth--> (a way to sign in), Chapter 23<!--ref:remotes--> and Chapter 36<!--ref:whatgh-->. The recordings ran in Bash and zsh on Git 2.43.0 and were re-run in CI on Git 2.55.0.

---

## 39.1 Two routes

There are two ways to connect a local project and a hosted repository:

| Route | You begin with | Then |
|---|---|---|
| **A. Start on the platform** | an empty hosted repository | you **clone** it, work, and push |
| **B. Start on your computer** | a repository that already has commits | you create an **empty** hosted repository, add it as a remote, and push |

Both end in the same place: a local repository and a hosted one that follow each other. In terms of Chapter 23<!--ref:remotes-->, the hosted repository is `origin`.

---

## 39.2 Creating the hosted repository

On the platform you create a repository from a web form, choosing a name and a few options.

> **Checked against GitHub's documentation (R237).** "Creating a new repository" and the quickstart describe the form: choose the plus icon in the upper-right corner of any page and then **New repository**; choose an owner and a name ("the repository name must not exceed 100 characters, and can only contain ASCII letters, digits, and the characters `.`, `-`, and `_`"), an optional description, and a visibility. The optional items are a README, a `.gitignore` file and a software licence. The choices, in the words of this book:
>
> - **Owner and name.** The owner is you or an organization (Chapter 37<!--ref:ghaccount-->); the name becomes part of every address (Chapter 36<!--ref:whatgh-->).
> - **Visibility.** *Public* ("accessible to everyone on the internet") or *private* ("only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members"; organizations that are part of an enterprise can also have *internal* repositories). Decide deliberately. A public repository, and everything in its history, can be copied by anyone (Chapter 33<!--ref:gitsec-->).
> - **A README.** A file that describes the project (Chapter 42<!--ref:readme-->).
> - **A `.gitignore`.** A starter list of files to ignore (Chapter 18<!--ref:tracking-->).
> - **A licence.** The terms under which others may reuse your work (Chapter 65<!--ref:licences-->).

**The important consequence** is this: if you tick any of the "add a file" options, the platform makes the *first commit* itself. Your hosted repository is then **not empty**. That matters for Route B (section 39.4), and GitHub's documentation says the same: "If you're importing an existing repository to GitHub, don't choose any of these options, as you may introduce a merge conflict." It also describes an "empty repository" as one that "contains no files" and is "often made if you don't initialize the repository with a README when creating it", and shows its quick-setup page with the clone address.

---

## 39.3 Route A: clone, work, push

Start with an *empty* hosted repository. Here a bare repository, `new-repo.git`, stands in for it. Clone it, make the first commit, and push:

```text
$ git clone new-repo.git fresh
Cloning into 'fresh'...
warning: You appear to have cloned an empty repository.
done.
```

*Recorded in Bash; `ch39-firstrepo/expected-first-clone.bash.txt`.*

Git warns that the repository is empty, which is expected (Chapter 23<!--ref:remotes--> showed the same). Add a README, commit and publish:

```text
$ cd fresh
$ printf '# Sunrise Bakery\n\nFresh bread every morning.\n' > README.md
$ git add README.md
$ git commit -m "Add a README"
[main (root-commit) 3034e23] Add a README
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
$ git push -u origin main
To /home/learner/new-repo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

*Recorded in Bash; `ch39-firstrepo/expected-first-clone.bash.txt`.*

`git push -u origin main` created the branch on the remote and made your `main` follow it. Check the state:

```text
$ git status -sb
## main...origin/main
$ git log --oneline
3034e23 (HEAD -> main, origin/main) Add a README
```

*Recorded in Bash; `ch39-firstrepo/expected-first-clone.bash.txt`.*

`## main...origin/main` says that `main` follows `origin/main` and that neither is ahead or behind. Your project is now on the "remote". If the remote were a hosting platform, this is the moment when the files would appear on its web page.

**What if the hosted repository already has a README?** Then you would clone it (a normal `git clone <address>`), and the README would come with you. Route A works either way.

---

## 39.4 Route B: connect an existing repository

You have a project with history, and want to publish it. Create an **empty** hosted repository (no README, no `.gitignore`, no licence: nothing that makes a first commit). The platform's own instructions usually offer three lines to copy. In Git terms they are: name your branch `main`, add the remote, push.

```text
$ cd bakery-menu
$ git branch -M main
$ git remote add origin ../new-repo.git
$ git push -u origin main
To ../new-repo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

*Recorded in Bash; `ch39-firstrepo/expected-connect-existing.bash.txt`.*

`git branch -M main` renames the current branch to `main` if it has another name (here it already was `main`, so nothing changed). Then the address is added and the branch is pushed with `-u`. Check that the branch follows the remote, and ask the remote directly what it has:

```text
$ git branch -vv
* main 81f772e [origin/main] Add coconut cake
$ git ls-remote --heads origin
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/heads/main
```

*Recorded in Bash; `ch39-firstrepo/expected-connect-existing.bash.txt`.*

The remote's `main` is at commit `81f772e`, the same as yours. Nothing else is needed.

### The surprise: "unrelated histories"

Suppose that you had ticked "add a README" when you created the hosted repository. Then it holds a commit of its own, which your project does not have. Watch what happens when you push:

```text
$ cd bakery-menu
$ git remote add origin ../hub-with-readme.git
$ git push -u origin main
To ../hub-with-readme.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '../hub-with-readme.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

*Recorded in Bash; `ch39-firstrepo/expected-unrelated.bash.txt`.*

The push is **rejected**: the remote has work that you do not have. It is the same message as in Chapter 23<!--ref:remotes-->, and the same advice applies: bring the remote's work in first. But this time:

```text
$ git fetch -q origin
$ git pull --no-rebase origin main
From ../hub-with-readme
 * branch            main       -> FETCH_HEAD
fatal: refusing to merge unrelated histories
```

*Recorded in Bash; `ch39-firstrepo/expected-unrelated.bash.txt`.*

`fatal: refusing to merge unrelated histories`. The two repositories were started **separately**; they have no commit in common, so Git will not join them unless you say that you mean it. Say so with `--allow-unrelated-histories`:

```text
$ git pull --no-rebase --allow-unrelated-histories --no-edit origin main
From ../hub-with-readme
 * branch            main       -> FETCH_HEAD
Merge made by the 'ort' strategy.
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

*Recorded in Bash; `ch39-firstrepo/expected-unrelated.bash.txt`.*

Git makes a merge commit that joins the two. Look at the graph, and push:

```text
$ git log --oneline --graph
*   68c8568 (HEAD -> main) Merge branch 'main' of ../hub-with-readme
|\
| * 36b17f4 (origin/main) Initial commit
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
$ git push -u origin main
To ../hub-with-readme.git
   36b17f4..68c8568  main -> main
branch 'main' set up to track 'origin/main'.
```

*Recorded in Bash; `ch39-firstrepo/expected-unrelated.bash.txt`.*

*(On Git 2.55.0 the decoration reads `(origin/main, origin/HEAD)`: after the `git fetch`, that newer version also records which branch is the remote's default. Git 2.43.0 did not do this for a remote that you added by hand, and it is a good example of why the same commands can print slightly different things.)*

The graph has two separate roots, one that the platform made ("Initial commit") and yours, joined by the merge commit. That is fine, and it is the price of starting both ends independently.

**How to avoid it.** For Route B, create the hosted repository **empty**. If you did tick the README box, this recovery works, but the history keeps its odd shape.

---

## 39.5 The daily cycle

Once connected, the cycle is the one from Chapter 23<!--ref:remotes--> and Chapter 34<!--ref:workflows-->:

1. `git fetch` (or `git pull`) to see and bring in what others did.
2. Work on a branch; commit in small steps.
3. `git push` to publish.

`git status` compares with what you last fetched (Chapter 23<!--ref:remotes-->), so fetch first when you want to know the truth.

---

## 39.6 Looking at the result

After the first push, open the repository's page in a browser and check three things:

- **Is everything there** that should be, and **nothing** that should not be? (Read the file list as a stranger would; Chapter 33<!--ref:gitsec-->.)
- **Is the visibility what you intended?**
- **Is the default branch the one you expect?**

> **Checked against GitHub's documentation (R238).** The quickstart says the contents of the README "are automatically shown on the front page of your repository". What else the repository page shows is covered in Chapter 40<!--ref:ghtour-->.

---

## 39.7 Project 3: publish the Sunrise Bakery website

> **Project 3.** *Goal:* publish your Sunrise Bakery repository (Chapters 19<!--ref:commits--> and 24<!--ref:stash-->) to a hosted repository, and prove that it round-trips. *Time:* about 40 minutes. *You need:* the `sunrise-bakery` repository with several commits, a clean `git status`, and either a platform account with a way to sign in (Chapter 38<!--ref:ghauth-->) **or**, if you have none, a bare repository on your own computer (`git init --bare sunrise-bakery.git`) that plays the same role.

1. **Check first.** Run `git status` and `git log --oneline`. Read the file list with `git ls-files` and confirm that it holds nothing private (Chapter 33<!--ref:gitsec-->).
2. **Create an empty hosted repository** named `sunrise-bakery`, with **no** README, `.gitignore` or licence. Choose *private* for now.
3. **Connect and push.** `git branch -M main`, `git remote add origin <address>`, `git push -u origin main`. Read the output.
4. **Verify the remote.** `git ls-remote --heads origin`: does the hash equal `git rev-parse main`?
5. **Prove the round trip.** In a different folder, `git clone <address> sunrise-check`. Compare the two with `git log --oneline` in each.
6. **Change and sync.** In the clone, edit a file, commit and push. In the original, `git fetch`, look at `git status`, then `git pull`.
7. **Reflect.** Which parts of this were Git, and which were the platform?

*Expected result:* the hosted (or local bare) repository has your full history; the clone has the same commits; a change made in the clone reaches the original through fetch and pull.

*Checkpoint questions:* What would have happened if you had ticked "add a README" in step 2? How would you have recovered? Why is *private* a sensible first choice?

---

## Checkpoint

## What You Learned

- Route A: create an empty hosted repository, clone it, work, push. Route B: create an empty hosted repository, add it as `origin`, push.
- Ticking "add a README" (or similar) makes the platform create a first commit, so the hosted repository is not empty.
- Pushing to a non-empty remote with unrelated history is rejected; `git pull --allow-unrelated-histories` joins the histories with a merge commit.
- `git push -u origin main` sets the upstream; `git ls-remote --heads origin` shows what the remote has.
- Check the repository page after the first push: files, visibility and default branch.

## New Vocabulary

No new terms. This chapter uses **remote**, **origin** and **upstream branch** from Chapter 23<!--ref:remotes-->.

## Commands Learned

`git branch -M main`, `git push -u origin main`, `git ls-remote --heads`, `git status -sb`, `git pull --allow-unrelated-histories`.

## Common Mistakes

1. **Ticking "add a README" when connecting an existing project.**
2. **Making a repository public without checking what is in the history.**
3. **Copying the platform's three lines without reading them.**
4. **Forgetting `-u` on the first push.**
5. **Assuming that the web page shows your latest work without pushing.**

## Practice

Do the exercises in [`exercises/ch39-exercises.md`](../../../exercises/ch39-exercises.md), including Project 3 (section 39.7). Every exercise can be done with local bare repositories.

## Self-Test

1. What are the two routes to a hosted repository?
2. Why should the hosted repository be empty in Route B?
3. What does `refusing to merge unrelated histories` mean?
4. What does `git push -u origin main` do?
5. What should you check on the repository page after the first push?

## Before Moving On

You are ready for Chapter 40<!--ref:ghtour--> if you can:

- [ ] publish an existing repository to an empty remote
- [ ] clone a remote, commit and push
- [ ] explain and resolve the unrelated-histories rejection
- [ ] say what to check after publishing

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Clone of an empty remote, first push, `status -sb` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0; local bare repository | R239 |
| Connecting an existing repository; `ls-remote --heads` | Locally tested (as above) | R239 |
| Rejected push and `unrelated histories`; the merge that joins them | Locally tested (as above) | R240 |
| The website's create form, its options and defaults, and the repository page | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R237, R238 |

## Where this leads

Chapter 40<!--ref:ghtour--> walks through the repository page. Chapter 42<!--ref:readme--> improves the repository's front page, and Chapter 45<!--ref:pr--> turns the shared repository into a place where changes are proposed and reviewed.
