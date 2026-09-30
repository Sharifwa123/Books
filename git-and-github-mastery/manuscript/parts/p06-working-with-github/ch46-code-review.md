---
key: review
number: 46
tag: Core
first_read: full
status: draft
requires: [pr]
ledger: [R263, R264, R265]
---
# Chapter 46 — Code Review [Core]

**In this chapter**

- why changes are reviewed, and what a review looks for
- how to comment, suggest a change and submit a decision
- what happens to a suggestion when the author applies it
- how to behave as a reviewer, and how to receive a review

> **How to read this chapter.** The Git side (a co-author trailer, and how Git counts co-authors) was run and recorded. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. The advice on etiquette is **this book's**, and is labelled as such.

**Before you start.** Chapter 45<!--ref:pr-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 46.1 Why review

> **New term: code review.** Reading someone else's proposed change, before it is merged, to find mistakes, share knowledge and decide whether it is ready.

GitHub's documentation says reviewing pull requests "is one of the main ways people collaborate", and that when you review a peer's work "you help catch issues early, share knowledge, and decide whether a change is ready to merge".

A review is **not** an exam of the author. It is a second pair of eyes on a change that the author has read so many times that they no longer see it. Reviews also spread knowledge: after a review, at least two people know how that part works.

---

## 46.2 What a reviewer looks for

A simple order, from most important to least. This is the book's checklist, not a rule of the platform.

1. **Purpose.** Does the change do what the description and the linked issue say? (The pull request page's sidebar shows linked issues and milestones, and GitHub's documentation suggests reading them to understand the purpose.)
2. **Correctness.** Would it work for the cases that matter, including the unusual ones?
3. **Safety.** Does it add a secret, a risky permission or a suspicious dependency? (Chapter 33<!--ref:gitsec-->; GitHub's documentation mentions *dependency review*, which shows how a pull request changes dependencies, and *code scanning* alerts on the proposed changes.)
4. **Tests and checks.** Do the automated checks pass, and is the new behaviour covered? (Chapter 54<!--ref:actions-->.)
5. **Clarity.** Could the next person understand it?
6. **Style.** Last, and mostly left to automatic tools.

**Size matters.** A review of ten lines is careful; a review of two thousand lines is a skim. Ask for a smaller change when it is too big (Chapter 45<!--ref:pr-->).

---

## 46.3 How to comment

> **Checked against GitHub's documentation (R263).** "Giving reviews" says anyone with read access can review and comment, and lists three things a reviewer can do: "leave general feedback on the overall pull request", "comment on specific lines to ask questions or explain concerns", and "suggest exact changes that the author can apply with a single click". "Reviewing proposed changes" recommends reviewing "one file at a time": examine each file, leave comments on specific changes, mark the file as **Viewed** to collapse it, and use the **progress bar** in the header to see how many files you have viewed. Comments on the Files changed tab can be single lines, several lines, or whole files, and they support the usual formatting, @mentions, emoji and references. A reply by email is added to the conversation and is not part of a review.

Every comment should be **specific and actionable**:

- Say *where* (the line) and *what* (the problem or question).
- Say *why*, if it is not obvious.
- Separate *must fix* from *could improve*. A common habit is to write "nit:" before a small preference the author may ignore.

---

## 46.4 Submitting a decision

When you finish, you submit the review with one of three decisions.

| Decision | Meaning, in the documentation's words |
|---|---|
| **Comment** | "Leaves general feedback without explicitly approving or requesting changes." |
| **Approve** | "Signals that the changes are ready to merge." |
| **Request changes** | "Flags feedback that the author should address before the pull request merges." |

> **Checked against GitHub's documentation (R264).** The three decisions and their wording are from "Giving reviews". Whether an approval is *required* before merging depends on the repository's rules (Chapter 50<!--ref:protect-->).

A decision is a **statement about the change at the moment you review it**. If the author pushes new commits, look again before you approve.

---

## 46.5 Suggestions, and what they do to history

A reviewer can propose an exact replacement for a line. The author can apply it with one click, and this makes a real **commit** on the pull request's branch.

> **Checked against GitHub's documentation (R265).** "Incorporating feedback in your pull request" says a person with write access can apply a suggested change directly, or add several suggestions to a batch; "applying one suggested change or a batch of suggested changes creates a single commit on the compare branch of the pull request"; "each person who suggested a change included in the commit will be a co-author of the commit", and "the person who applies the suggested changes will be a co-author and the committer". If a suggestion is out of scope, you can open an issue that tracks it and links back. The page on commits with several authors says the platform reads `Co-authored-by: NAME <EMAIL>` lines added after a blank line at the end of the commit message, and that for the commit to count as a contribution the address should be one associated with the person's account.

That trailer is only text in the commit message, so **Git** can read it. Here a typo is fixed after a reviewer's suggestion, with the reviewer credited:

```text
$ cd bakery-menu
$ grep -n slise menu.md
4:- Coconut cake (slise): 4.00
$ sed -i 's/slise/slice/' menu.md
$ git diff
diff --git a/menu.md b/menu.md
index 462ca3a..bc206a1 100644
--- a/menu.md
+++ b/menu.md
@@ -1,4 +1,4 @@
 # Sunrise Bakery menu

 - White loaf: 2.80
-- Coconut cake (slise): 4.00
+- Coconut cake (slice): 4.00
$ git commit -q -am "Fix the typo in the cake line" -m "Co-authored-by: Sam Reviewer <sam@example.org>"
$ git log -1 --format=%B
Fix the typo in the cake line

Co-authored-by: Sam Reviewer <sam@example.org>

$ git log -1 --format='%(trailers:key=Co-authored-by,valueonly)'
Sam Reviewer <sam@example.org>

$ git shortlog -sne --group=author --group=trailer:co-authored-by HEAD
     2	Ada Learner <ada@example.org>
     1	Sam Reviewer <sam@example.org>
```

*Recorded in Bash; `ch46-review/expected-suggestion.bash.txt`.*

`git log --format=%B` shows the message with the trailer at the end. `%(trailers:key=Co-authored-by,valueonly)` extracts it. `git shortlog` with `--group=author --group=trailer:co-authored-by` counts Ada twice (she authored the first commit and this one) and the reviewer once. Git does not decide who counts as an author: it counts the words you wrote.

---

## 46.6 Being a good reviewer

This section is the book's advice.

1. **Review the change, not the person.** "This loop reads past the end of the list" is about the code; "you always forget the end" is about the author.
2. **Ask before assuming.** "Was there a reason to use two loops here?" leaves room for a reason you cannot see.
3. **Explain the reason.** Give one line of why, and a link if there is a guideline.
4. **Praise what is good.** It is information too: it tells the author what to keep doing.
5. **Be timely.** A pull request waiting for days blocks the author and grows stale.
6. **Know when to stop.** Approve when the change is good enough and safe, not when it is what you would have written.

---

## 46.7 Receiving a review

1. **Thank first, then read twice.** Feedback on your work feels personal. Read all of it before you answer.
2. **Assume good intent.** Most comments are meant to help.
3. **Answer every comment**: do it, or say why not.
4. **Push new commits to the same branch.** The pull request updates itself (Chapter 45<!--ref:pr-->).
5. **Do not argue by silence.** If you disagree, say so and give your reason; if you still disagree, ask a maintainer to decide.
6. **Keep unrelated requests for another issue**, as the documentation suggests for out-of-scope feedback.

---

## Checkpoint

## What You Learned

- A review finds mistakes early, spreads knowledge and decides readiness.
- Reviewers comment on lines and files, and finish with Comment, Approve or Request changes.
- A suggestion applied from the page becomes one commit on the pull request branch, with the suggesters credited as co-authors.
- `Co-authored-by:` is plain text in the message, which Git can read and count.
- Good review is specific, kind and timely; good reception is answering every point.

## New Vocabulary

**Code review** (introduced above).

## Commands Learned

`git log --format='%(trailers:key=Co-authored-by,valueonly)'`, `git shortlog -sne --group=author --group=trailer:co-authored-by`.

## Common Mistakes

1. **Reviewing a huge change in one pass.**
2. **Vague comments** such as "this is wrong".
3. **Approving without reading.**
4. **Taking feedback as an attack.**
5. **Pushing new commits after an approval and assuming it still stands.**

## Practice

Do the exercises in [`exercises/ch46-exercises.md`](../../../exercises/ch46-exercises.md).

## Self-Test

1. Name the three review decisions and what each means.
2. What does applying a suggestion from the page create, and who is credited?
3. Where is a co-author recorded in a commit?
4. Why should you look again after new commits are pushed?
5. Write one comment that is specific and kind.

## Before Moving On

You are ready for Chapter 47<!--ref:projects--> or Chapter 49<!--ref:collab--> if you can:

- [ ] review a small change with a checklist
- [ ] write comments that are specific and actionable
- [ ] receive a review and answer every point

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A `Co-authored-by` trailer is text in the message; `%(trailers)` and `shortlog --group=trailer` read it | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R265 (Git side) |
| Review comments, decisions, suggestions, co-authors | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R263-R265 |
| Reviewer checklist and etiquette | **The book's own advice**, not sourced rules | R263 |

## Where this leads

Chapter 49<!--ref:collab--> covers who may review and merge, forks, and code owners. Chapter 50<!--ref:protect--> covers making reviews mandatory.
