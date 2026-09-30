---
key: assessment
number: 81
tag: Core
first_read: later
status: draft
requires: [playbooks]
ledger: [R354]
---
# Chapter 81 — Final Mastery Assessment [Core]

**In this chapter**

- a practical assessment in a sandbox, in two levels: **Proficient** (the Core material) and **Mastery** (adds tasks from the Deep material)
- a checking script that tells you which tasks you completed
- a rubric and an answer key, kept **separate** in `solutions/ch81-solutions.md`

> **How to read this chapter.** You do the tasks on your own computer, in a sandbox that a script creates. **Nothing needs GitHub**: a local bare repository stands in for the remote. The setup and checking scripts are in `companion/assessment/`. The book's author ran the setup, the checker before any work (0 of 15), a reference solution, and the checker after (15 of 15), in Bash and zsh on Git 2.43.0 and in CI on newer Git; the reference solution is **not** part of the companion files. The checker checks **results**, not the way you reached them, and it can be wrong about unusual but valid solutions: if you think your answer is right and the checker disagrees, read the check in the script and decide for yourself. **This is a self-assessment, not a certificate.**

**Before you start.** You should have finished Parts I to XII of the book, or be ready to look things up while working. The assessment is **open book**: reading the manual is allowed and expected, as at work. Set aside two hours for the Proficient level and another hour for the Mastery tasks.

---

## 81.1 Prepare the sandbox

Run the setup script (`sh` runs it with the shell; the folder can be changed with `ASSESS_DIR`). Here is what it prints, and what the checker says before you have done anything:

```text
$ sh "$STARTER/../assessment/setup.sh"
Assessment sandbox ready in /home/learner/assessment/work
$ sh "$STARTER/../assessment/check.sh"
== Proficient level
FAIL P1 identity set in this repository
FAIL P2 branch feature/tea with a commit adding tea
FAIL P3 branch feature/tea pushed to the remote
FAIL P4 debug.log ignored and not shown by status
FAIL P5 conflict resolved on branch combined
FAIL P6 bad commit reverted on main and pushed
FAIL P7 annotated tag v1.1.0 at the tip of main, pushed
FAIL P8 deleted branch precious recovered
FAIL P9 SECURITY.md and CONTRIBUTING.md on main
FAIL P10 workflow file with permissions, jobs and pinned actions
== Mastery level (extra)
FAIL M1 secret removed from all history, local and remote
FAIL M2 first bad commit found and written down
FAIL M3 shallow, sparse clone in slim
FAIL M4 release notes for v1.0.0..v1.1.0
FAIL M5 webhook signature computed
Proficient: 0 of 10. Mastery extras: 0 of 5.
Proficient level not yet reached (9 of 10 needed).
```

*Recorded in Bash; `ch81-assessment/expected-assess.bash.txt`.*

The setup created, under `assessment/` in your home folder:

- `remote.git`, a bare repository that plays the shared remote;
- `work`, your clone, where you do the tasks. It has an untracked `debug.log`, a branch that has been deleted, and a history with hidden problems.

Run the checker as often as you like: `sh companion/assessment/check.sh` (from the book's folder; use the path where you keep the companion files). To start again, run the setup script again: **it deletes and recreates `assessment/`**.

---

## 81.2 Proficient level: ten tasks

Do all tasks in `assessment/work` unless stated. You need **9 of 10**.

**P1. Identity.** Set your name and email **for this repository only** (not globally).

**P2. A feature branch.** Create a branch `feature/tea` from `main`, add the line `- Tea: 1.50` to `menu.md`, and commit it with a clear message.

**P3. Publish it.** Push `feature/tea` to `origin`.

**P4. Ignore the noise.** `debug.log` must stop appearing in `git status`, without deleting the file. Make the change with a file that Git tracks.

**P5. A conflict.** The remote has two branches, `edit-a` and `edit-b`, which changed the same line of `README.md` differently. Create a local branch `combined` that starts at `origin/edit-a` and merges `origin/edit-b`. Resolve the conflict so that the file has **no conflict markers** and still has a line that begins `Opening hours`. Commit the merge.

**P6. Undo a bad commit on the shared branch.** The last commit on `main`, "Set prices to zero", is wrong and already public. Undo its effect **without rewriting history**, and push. The commit itself must stay in the history.

**P7. Release.** After your other work on `main` is finished, create an **annotated** tag `v1.1.0` on the tip of `main` and push the tag.

**P8. Recover a deleted branch.** A branch named `precious` was deleted from `work` before it was merged. Bring it back with the same content, without asking anyone.

**P9. Community files.** Add `SECURITY.md` and `CONTRIBUTING.md` (each with real content) to `main` and push.

**P10. A workflow file.** Add `.github/workflows/ci.yml` to `main` (nothing runs it here; it is checked as a file). It must have a trigger, a `permissions` block, at least one job, and **every `uses:` line pinned to a full 40-character commit name**. You may reuse the commit name given in Chapter 60<!--ref:wfsec-->.

**Order of work.** P6, P9 and P10 change `main`, and P7 tags the tip, so tag last. Push `main` when you finish.

---

## 81.3 Mastery level: five more tasks

The Mastery level needs **all ten Proficient tasks and 4 of these 5**. Work in `assessment/work` unless stated; the answer files go in `assessment/work`.

**M1. Remove the secret from history.** A file `secrets.env` was committed early on. Remove it from **all history** in `work` **and** from the remote. **Do this last**, after your other work is pushed: rewriting works from a fresh copy of the remote's branches, so a branch that exists only on your computer would be lost. Push every branch you want to keep (`combined`, `precious`) and the tag first. (Chapter 79<!--ref:playbooks--> describes the tool and its side effects, and what it cannot undo.)

**M2. Find the culprit.** `state.txt` said `ok` once and says `broken` now. Find the **first commit** that broke it **with an automated test**, not by reading commits, and write its subject line (only that) into a file `bisect-answer.txt`. Leave the repository on `main` afterwards.

**M3. A small clone.** Make a clone of the remote in `assessment/slim` (a sibling of `work`, not inside it) with **one commit** of history and **without the `src` folder**, but with `docs`.

**M4. Release notes.** Write `RELEASE_NOTES.md` listing, one per line, the subject of every commit between `v1.0.0` and `v1.1.0`.

**M5. A signature.** A webhook delivery has the payload `Order 42 shipped` and the secret `bakery-test-secret` (both made up). Compute its HMAC-SHA-256 hexadecimal digest and put it alone in a file `signature.txt`. (Chapter 74<!--ref:api-->.)

---

## 81.4 How to use your result

| Result | What it means |
|---|---|
| Proficient not reached (fewer than 9 of 10) | Revisit the chapters of the failed tasks (the answer key names them), then run the setup again and retry |
| Proficient reached | You can use Git and GitHub's workflow at a professional level for everyday work |
| Mastery reached | You can also handle advanced repository tasks; keep practising on real projects |

Whatever your result, **the best next step is to use these skills on a real project**, with real reviews and real mistakes. The book's Appendix N lists sources to keep learning.

---

## Checkpoint

## What You Learned

- You can be checked on results: a branch, a tag, a file, a history.
- Doing the tasks in an order that does not undo earlier ones (tag last, rewrite history last) is part of the skill.
- The checker cannot judge understanding; the answer key and your own explanations can.

## New Vocabulary

No new terms.

## Commands Learned

No new commands.

## Common Mistakes

1. **Tagging before finishing `main`.**
2. **Rewriting history before pushing branches you want to keep.**
3. **Setting the identity globally when the task asks for this repository.**
4. **Trusting a test that can pass wrongly (see Chapter 80<!--ref:challenges-->).**
5. **Reading the answer key before trying.**

## Practice

The assessment is the practice. The exercises file adds three reflection tasks: [`exercises/ch81-exercises.md`](../../../exercises/ch81-exercises.md).

## Self-Test

1. Which tasks change `main`, and in which order should they be done?
2. Why must M1 be done last?
3. Why does the checker not tell you *how* you solved a task?
4. What does P6 forbid?
5. How do you start the assessment again?

## Before Moving On

You have finished the book if you can:

- [ ] complete the Proficient level with at most one failed task
- [ ] explain every solution to a beginner
- [ ] name the next real project where you will practise

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The setup and the checker (0 of 15 before, 15 of 15 after the reference solution) | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, git-filter-repo 2.47.0, OpenSSL, PyYAML; CI on newer Git | R354 |
| That the checker judges every valid solution correctly | **Not established**; only one reference solution was tried | none |

## Where this leads

This is the last chapter. The appendices give references and checklists; the glossary and the sources log (Appendix N) close the book.
