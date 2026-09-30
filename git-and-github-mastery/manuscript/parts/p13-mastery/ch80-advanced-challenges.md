---
key: challenges
number: 80
tag: Deep
first_read: later
status: draft
requires: [playbooks]
ledger: [R353]
---
# Chapter 80 — Advanced Challenges [Deep]

**In this chapter**

- six challenges that combine what you learned: multiple repositories, history surgery, large-repository tricks, workflow design, automated bisecting and rescue of unreachable commits
- for each: a setup you type, a task, and a way to check your result
- **solutions are in a separate file**, `solutions/ch80-solutions.md`; try first

> **How to read this chapter.** This is a **Deep** chapter for people who finished the core path. Every challenge has a **reference solution that was run and recorded** in Bash and zsh (Git 2.43.0, `git-filter-repo` 2.47.0) and is re-run in CI on newer Git; the recordings are kept with the book's verification files and are not printed here, so that the challenges stay challenges. Setups use local repositories only: nothing needs GitHub. The one paper challenge (workflow design) has no recording. Expect your commit names and some wording to differ from the reference.

**Before you start.** Chapters 79<!--ref:playbooks-->, 31<!--ref:bigrepos-->, 28<!--ref:tools--> and 30<!--ref:objects-->. Work in an empty sandbox folder. Do not look at the solutions file until you have tried for a while.

---

## Challenge 1. Update a submodule pointer

**Idea.** A project can contain another repository as a **submodule**; the outer project records *which commit* of the inner one it uses (Chapter 31<!--ref:bigrepos-->).

**Setup.** Type these lines (they create the inner repository `lib`, with two versions, and an outer project `app`):

```shell
git init -q --bare lib.git
git clone -q lib.git libwork
cd libwork
printf 'version 1\n' > lib.txt
git add lib.txt && git commit -q -m "lib 1" && git push -q origin main
cd ..
git init -q app
cd app
git -c protocol.file.allow=always submodule add -q ../lib.git vendor/lib
git commit -q -m "Add lib as a submodule"
cd ../libwork
printf 'version 2\n' > lib.txt
git commit -q -am "lib 2" && git push -q origin main
cd ../app
```

(`protocol.file.allow=always` is needed only because this sandbox uses a local file path; Chapter 31<!--ref:bigrepos--> explains why it is not a permanent setting.)

**Task.** Make `app` use version 2 of `lib`, and record that decision in a commit of `app`.

**Check.** `cat vendor/lib/lib.txt` prints `version 2`, `git status` in `app` is clean, and `git log` in `app` has a commit that records the change.

---

## Challenge 2. Split a folder into its own repository

**Idea.** A monorepo (one repository for many things) contains a `site` folder that deserves its own repository, **with its history**.

**Setup.**

```shell
git init -q mono && cd mono
mkdir site tools
printf 'a\n' > site/index.html && printf 't\n' > tools/build.sh
git add -A && git commit -q -m "Start"
printf 'b\n' >> site/index.html && git commit -q -am "Change site"
printf 't2\n' >> tools/build.sh && git commit -q -am "Change tools"
printf 'c\n' >> site/index.html && git commit -q -am "Change site again"
cd ..
```

**Task.** Produce a **new repository** that contains only the contents of `site` at its top level, with only the commits that touched it. Do not modify `mono`.

**Check.** In the new repository `ls` shows `index.html` and nothing else, and the number of commits (`git rev-list --count HEAD`) is 3, not 4.

**Hint.** Chapters 33<!--ref:gitsec--> and 79<!--ref:playbooks--> used a tool that rewrites history; work on a **clone**.

---

## Challenge 3. Clone only what you need

**Idea.** A large repository takes long to download. Git can fetch less history and check out fewer files (Chapter 31<!--ref:bigrepos-->).

**Setup.**

```shell
git init -q big && cd big
mkdir docs src
for i in 1 2 3 4 5 6; do printf "$i\n" > src/f$i.txt; printf "$i\n" > docs/d$i.md; git add -A; git commit -q -m "Commit $i"; done
cd ..
```

**Task.** Make a clone of `big` that has **one commit** of history and **only the `docs` folder** in its working tree.

**Check.** `git rev-list --count HEAD` prints 1, and `ls` shows only `docs`.

**Hint.** For a local repository, shallow cloning needs a `file://` address (Chapter 31<!--ref:bigrepos-->).

---

## Challenge 4. Design a workflow (on paper)

**Situation.** A team of six maintains a small web application and a documentation site. They release monthly and sometimes need urgent fixes. New contributors join often, and the application handles customers' data.

**Task.** Write a one-page **workflow design** with these parts: (1) branch and merge rules; (2) what the automated checks are and when they run; (3) branch protection and review rules; (4) how releases are made and numbered; (5) how a hotfix is made; (6) how secrets and dependencies are handled; (7) what a new contributor reads first. Use only ideas from this book and say which chapter each comes from.

**Check.** Use the rubric in the solutions file: each of the seven parts must be present, consistent with the others, and justified in a sentence.

---

## Challenge 5. Find the first bad commit automatically

**Idea.** A file `state.txt` was correct once and is wrong now, somewhere in fourteen commits. Binary search finds the change without reading them all (Chapter 28<!--ref:tools-->).

**Setup.**

```shell
git init -q hunt && cd hunt
printf 'ok\n' > state.txt && git add state.txt && git commit -q -m "Start"
for i in 1 2 3 4 5 6 7 8; do printf "$i\n" >> notes.txt; git add notes.txt; git commit -q -m "Note $i"; done
printf 'broken\n' > state.txt && git commit -q -am "Change state"
for i in 9 10 11 12; do printf "$i\n" >> notes.txt; git add notes.txt; git commit -q -m "Note $i"; done
cd ..
```

**Task.** Write a **test script** that succeeds when `state.txt` contains exactly the line `ok`, and use Git to find the first commit for which it fails, **without checking out commits by hand**.

**Check.** Git names the commit "Change state". Then return the repository to its normal state.

**Watch out.** A careless test can pass when it should fail: think about what your test matches.

---

## Challenge 6. Rescue a commit that no branch points to

**Idea.** Work was committed on a branch and the branch was deleted before merging. No branch and no tag points to the commit, and you do not remember its message.

**Setup.**

```shell
git init -q lost && cd lost
printf 'x\n' > a.txt && git add a.txt && git commit -q -m "Base"
git switch -q -c temp
printf 'y\n' >> a.txt && git commit -q -am "Precious work"
git switch -q main
git branch -D temp
```

**Task.** Find the commit **without using the reflog**, look at its message, and give it a branch named `rescued`.

**Check.** `git log -1 rescued` shows "Precious work".

**Hint.** Chapter 30<!--ref:objects--> explained that objects exist whether or not a name points to them; one Git command lists objects that nothing reaches.

---

## Scoring yourself

| Challenge | You did it if… |
|---|---|
| 1 | the outer project records the new inner commit in its own commit |
| 2 | the new repository has three commits and only the site's files |
| 3 | one commit, only `docs` |
| 4 | all seven parts present, consistent, justified |
| 5 | Git named the right commit through an automated test |
| 6 | the commit is reachable from `rescued` |

If you needed the solutions for more than two challenges, revisit Chapters 31<!--ref:bigrepos-->, 28<!--ref:tools-->, 30<!--ref:objects--> and 79<!--ref:playbooks-->, then try again with a different idea.

---

## Checkpoint

## What You Learned

- A submodule records a commit of another repository; updating it is a commit in the outer project.
- History surgery (a subdirectory filter) works on a clone and changes commit names.
- Shallow clones and sparse checkouts cut the cost of a large repository.
- A test that can pass wrongly is worse than none; `git bisect run` automates the search.
- Unreachable objects can still be found until garbage collection removes them.

## New Vocabulary

No new terms.

## Commands Learned

No new commands.

## Common Mistakes

1. **Rewriting history in the original repository** instead of a clone.
2. **Writing a test that matches too loosely** (a word inside another word).
3. **Leaving `git bisect` running** and forgetting to reset.
4. **Assuming a deleted branch's commits are gone.**
5. **Skipping the "paper" design and jumping to commands.**

## Practice

The challenges are the practice. The exercises file for this chapter adds three extension tasks: [`exercises/ch80-exercises.md`](../../../exercises/ch80-exercises.md).

## Self-Test

1. Why do a shallow clone of a local repository need a `file://` address?
2. What does the outer project record about a submodule?
3. Why must the test in challenge 5 match a whole line?
4. What kind of objects does `git fsck --lost-found` report?
5. Why work on a clone in challenge 2?

## Before Moving On

You are ready for Chapter 81<!--ref:assessment--> if you can:

- [ ] complete at least four challenges without the solutions
- [ ] explain why each solution works

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The reference solutions of challenges 1, 2, 3, 5 and 6 | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, git-filter-repo 2.47.0; CI on newer Git (recordings kept in `verification/ch80-challenges`, not printed) | R353 |
| Challenge 4 (paper) | Assessed with a rubric, not run | none |

## Where this leads

Chapter 81<!--ref:assessment--> is the final assessment, in two levels.
