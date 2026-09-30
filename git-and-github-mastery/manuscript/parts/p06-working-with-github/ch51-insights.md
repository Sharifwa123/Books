---
key: insights
number: 51
tag: Deep
first_read: later
status: draft
requires: [ghrepo, pr]
ledger: [R277, R278]
---
# Chapter 51 — Insights [Deep]

**In this chapter**

- what the repository's graphs show: pulse, contributors, traffic, commits, code frequency, network
- what each graph counts, and what it does **not** mean
- how to reproduce the counting with Git
- which graphs exist for which repositories

> **How to read this chapter.** This is a **Deep** chapter and can be read later. The Git counting was run and recorded. Statements about GitHub are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. The dependency graph belongs to Chapter 62<!--ref:ghsec-->, where it is covered with the security features.

**Before you start.** Chapter 39<!--ref:ghrepo-->, Chapter 45<!--ref:pr--> and Chapter 17<!--ref:history_view-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 51.1 What insights are for

Repository **insights** are graphs and lists that summarise activity. If you maintain a project they help you see who is using it and how it is changing. They are **summaries of counts**, and a number is only as meaningful as its rules. This chapter names each graph, says what its documentation says it counts, and shows the same counting in plain Git so that you know what the numbers are made of.

---

## 51.2 The graphs

| Graph | What GitHub's documentation says it shows |
|---|---|
| **Pulse** | "A list of open and merged pull requests, open and closed issues, and a graph showing the commit activity for the top 15 users who committed to the default branch" in a chosen period |
| **Contributors** | The top 100 contributors; "merge commits and empty commits aren't counted as contributions for this graph" |
| **Traffic** | Views, unique visitors, full clones (not fetches), visitors from the past 14 days, referring sites and popular content |
| **Commits** | All commits in the past year, excluding merge commits: the top graph by week, the bottom by day of the week |
| **Code frequency** | Content additions and deletions for each week in the repository's history |
| **Network** | The branch history of the whole repository network, including forks: "up to 100 of the most recently pushed-to branches" |

Some details that change how to read them:

- Traffic is visible to "anyone with push access", updates full clones and visitor information hourly and referring sites and popular content daily, and "all data in the traffic graph uses the UTC+0 timezone".
- "Certain contributor, commit, and code frequency insights are only available for repositories that have fewer than 10,000 commits."
- Your commits count in the contributors graph only if they are merged into the default branch, and you are among the top 100 (Chapter 37<!--ref:ghaccount--> explains that a commit must also match your account by email).
- The graph is **not a measure of skill**. It counts what it counts.

> **Checked against GitHub's documentation (R277).** "About repository graphs", "Viewing a project's contributors", "Using Pulse to view a summary of repository activity", "Analyzing changes to a repository's content", "Understanding connections between repositories" and "Viewing traffic to a repository". The quotations above are from these pages.

**Which repositories have which graphs.** The documentation says that on the Free plan some graphs (Pulse, Contributors, Traffic, Commits, Code frequency, Network) "are available only in public repositories", while all graphs are available in public and private repositories on paid plans; the traffic page also names Free plans for organizations. Plans and their names change (Chapter 43<!--ref:settings-->): check the current page.

---

## 51.3 What the counts are made of

Three effects change a count without any change in the work.

**Merge commits and empty commits.** A merge commit records a merge, and an empty commit changes no file. The contributors graph ignores both. In Git you can count with and without merges. A small repository was built with one person who committed under two different email addresses, plus a merge and an empty commit:

```text
$ cd bakery-menu
$ git rev-list --count HEAD
6
$ git shortlog -sne HEAD
     5	Ada Learner <ada@example.org>
     1	Ada L. <ada@old-mail.example>
$ git shortlog -sne --no-merges HEAD
     4	Ada Learner <ada@example.org>
     1	Ada L. <ada@old-mail.example>
$ printf 'Ada Learner <ada@example.org> Ada L. <ada@old-mail.example>\n' > .mailmap
$ git shortlog -sne --no-merges HEAD
     5	Ada Learner <ada@example.org>
$ git log --shortstat --format='%h %s' --no-merges
da81f52 Trigger the checks again
1fdaf40 Raise the price of the white loaf

 1 file changed, 1 insertion(+), 1 deletion(-)
77deeab Add tea

 1 file changed, 1 insertion(+)
8b83a9e Add rolls

 1 file changed, 1 insertion(+)
a325a15 Add the menu

 1 file changed, 3 insertions(+)
```

*Recorded in Bash; `ch51-insights/expected-counting.bash.txt`.*

Read it in order. `git rev-list --count HEAD` finds six commits. `git shortlog -sne` counts the five by Ada with her main email and one under an older address, **as two people**, and the merge counted for Ada. Adding `--no-merges` drops the merge (five commits by Ada become four). The `git log --shortstat` list shows that the empty commit `Trigger the checks again` has **no changed lines**: it would count in the shortlog but do nothing in the code.

**The same person, two identities.** Git counts an identity by name and email as written in each commit (Chapter 14<!--ref:config-->). The same person under two addresses appears as two contributors, until a `.mailmap` file (documented in Git's `gitmailmap`) joins them: a line `Proper Name <proper@email> Commit Name <commit@email>` "allows mailmap to replace both the name and the email of a commit matching both the specified commit name and email address". With the mailmap, all five commits count for one Ada.

**Lines are not value.** The code-frequency graph is additions and deletions per week, as `--shortstat` shows per commit. A deletion of a thousand lines of dead code and an addition of a thousand lines of a generated file both make a tall bar.

> **Checked against Git documentation and the recorded run (R278).** The counting options (`shortlog -sne`, `--no-merges`, `--shortstat`) are shown running on Git 2.43.0 and re-run in CI. The `.mailmap` line format is from Git 2.56.0's `gitmailmap` manual. What the platform counts is as described in R277; the recording reproduces the *rules* in Git, not GitHub's own computation.

---

## 51.4 Using insights well

1. **Ask a question first**: "who reviews our pull requests?", "is anyone using this?", "did the last release change traffic?". Then choose the graph.
2. **Read the period and the rules** before the shape.
3. **Do not use them to rank people.** They count commits, not judgement, review, design, documentation or support.
4. **Do not compare repositories** by these numbers unless the rules are the same.
5. **Check the sample.** A fork's traffic is separate; a private repository on a plan without a graph shows nothing.

---

## Checkpoint

## What You Learned

- Insights are summaries of counts, each with its own rules and period.
- The contributors graph ignores merge commits and empty commits and shows the top 100.
- Traffic needs push access, updates on a schedule, and uses UTC.
- The same person under two identities counts twice until a `.mailmap` joins them.
- A graph is not a measure of skill.

## New Vocabulary

None: this chapter uses the terms *contributor* and *commit* from earlier chapters.

## Commands Learned

`git rev-list --count`, `git shortlog -sne`, `git shortlog --no-merges`, `git log --shortstat`, `.mailmap`.

## Common Mistakes

1. **Reading a graph as a performance review.**
2. **Forgetting that merge and empty commits are excluded.**
3. **Counting one person twice** because of two email addresses.
4. **Expecting every graph on every plan.**
5. **Ignoring the time period and UTC.**

## Practice

Do the exercises in [`exercises/ch51-exercises.md`](../../../exercises/ch51-exercises.md).

## Self-Test

1. Which commits does the contributors graph ignore?
2. Who can see the traffic graph?
3. Why can one person appear as two contributors?
4. How would you count commits by author without merges?

## Before Moving On

You are ready for Chapter 52<!--ref:cicd--> if you can:

- [ ] say what a graph counts before reading its shape
- [ ] reproduce a count with `git shortlog`
- [ ] explain why the numbers are not a measure of skill

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `shortlog`, `--no-merges`, `--shortstat`, `.mailmap` joining identities | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git; `.mailmap` format checked in Git 2.56.0's manual | R278 |
| What each graph shows, limits, traffic rules, plan availability | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R277 |

## Where this leads

Chapter 52<!--ref:cicd--> begins the automation part of the book. Chapter 62<!--ref:ghsec--> covers the dependency graph and other security views.
