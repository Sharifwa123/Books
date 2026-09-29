---
key: problem
number: 9
tag: Core
first_read: full
status: draft
requires: [files, editors, terminal]
ledger: [R134, R135]
---
# Chapter 9 — The Problem of Changing Files [Core]

**In this chapter**

- the "final_v2_REAL" problem, shown with real files
- six separate difficulties that appear whenever files change over time or are shared
- what people try (copies, backups, cloud folders, tracked changes) and where each falls short
- what a better system would have to do
- the definition of version control, and the vocabulary that goes with it

**Before you start.** Chapter 2<!--ref:files--> (files, folders), Chapter 3<!--ref:editors--> (text files) and Chapter 7<!--ref:terminal--> (typing commands). This chapter is a story with recorded evidence: the commands are shown so you can repeat them in your practice folder, and each has real recorded output.

---

## 9.1 A very ordinary afternoon

The Sunrise Bakery keeps its prices in a small file, `menu.txt`. Over a few weeks, four people touch it. Somebody raises the price of rolls. Somebody raises the price of bread. Someone adds a cake. Each person, wanting to be careful, saves a copy instead of overwriting the old one.

Here is what the folder looks like afterwards. The files were created with commands (you will meet the same commands again in this chapter's exercises), and `ls` lists the result:

```text
$ mkdir menu-history
$ cd menu-history
$ printf 'Bread: 2.50\nRolls: 3.00\n' > menu.txt
$ printf 'Bread: 2.50\nRolls: 3.20\n' > menu_v2.txt
$ printf 'Bread: 2.80\nRolls: 3.20\n' > menu_final.txt
$ printf 'Bread: 2.80\nRolls: 3.00\n' > menu_final_v2.txt
$ printf 'Bread: 2.80\nRolls: 3.20\nCake: 4.00\n' > menu_final_REAL.txt
$ ls
menu.txt  menu_final.txt  menu_final_REAL.txt  menu_final_v2.txt  menu_v2.txt
```

*Recorded in Bash; `ch09-problem/expected-names.bash.txt`.*

Five files, all of them "the menu". Take a moment with this list and try to answer three questions.

1. **Which is the latest?** `menu_final.txt`? `menu_final_v2.txt`? `menu_final_REAL.txt`? The names claim to know, but they contradict themselves: "final" cannot be followed by a "v2", and "REAL" implies that the other finals were fake.
2. **What is the difference between two of them?** You would have to open both and compare them line by line.
3. **Why did someone change it?** Nothing here says.

The computer can help with the second question. The command `diff` compares two text files and prints the differences:

```text
$ diff menu_final.txt menu_final_v2.txt
2c2
< Rolls: 3.20
---
> Rolls: 3.00
$ diff menu_final.txt menu_final_REAL.txt
2a3
> Cake: 4.00
```

*Recorded in Bash; `ch09-problem/expected-names.bash.txt`.*

Read the first result. The line `2c2` means "line 2 in the first file was **c**hanged into line 2 in the second". The `<` line is from the first file and the `>` line from the second: the rolls cost 3.20 in `menu_final.txt` but 3.00 in `menu_final_v2.txt`. The second result, `2a3`, means "after line 2, a line was **a**dded": the cake.

So the *mechanics* of comparing are solved. What is missing is a system that keeps the versions, names them for you, remembers which came from which, and records why. That is the problem this chapter is about.

---

## 9.2 Six difficulties

Whenever information changes over time, and more so when several people change it, the same six difficulties appear. Learn to recognise them, because everything in Git answers one of them.

| # | Difficulty | Example |
|---|---|---|
| 1 | **Which is the current one?** | Five files named "menu". |
| 2 | **What changed?** | You must compare by eye or with a tool, each time. |
| 3 | **Why did it change?** | The reason lives in someone's memory, or nowhere. |
| 4 | **Can I go back?** | Overwrite a file and the old contents are gone. |
| 5 | **How do we work at the same time?** | Two people edit, and one erases the other's work. |
| 6 | **Who did what, and when?** | No reliable record of authorship. |

### 9.2.1 The collision, recorded

The fifth difficulty is the most damaging, so here it is, reproduced. A shared folder holds `menu.txt`. Alice and Bob each take a private copy. Alice adds a cake; Bob raises the price of bread. Each then copies their version back to the shared folder.

```text
$ mkdir shared alice bob
$ printf 'Bread: 2.50\nRolls: 3.00\n' > shared/menu.txt
$ cp shared/menu.txt alice/menu.txt
$ cp shared/menu.txt bob/menu.txt
$ printf 'Bread: 2.50\nRolls: 3.00\nCake: 4.00\n' > alice/menu.txt
$ printf 'Bread: 2.80\nRolls: 3.00\n' > bob/menu.txt
$ cp alice/menu.txt shared/menu.txt
$ cat shared/menu.txt
Bread: 2.50
Rolls: 3.00
Cake: 4.00
```

*Recorded in Bash; `ch09-problem/expected-collision.bash.txt`.*

Read this carefully. After Alice copied her file back, the shared menu had the cake. Then Bob copied his file back, and the shared menu became:

```text
$ cp bob/menu.txt shared/menu.txt
$ cat shared/menu.txt
Bread: 2.80
Rolls: 3.00
```

*Recorded in Bash; `ch09-problem/expected-collision.bash.txt`.*

**The cake has vanished.** Nothing reported an error. Bob's copy did not know about Alice's change, so when it was copied over the shared file it silently replaced Alice's work. Alice's version still exists in her private folder, but the *shared* file (the one everyone trusts) has lost her change, and nobody was warned.

Nobody did anything wrong. The system had no way to notice, because a plain file has no memory of what it used to contain, and a plain copy has no idea that someone else changed the original meanwhile. **The lesson is not "be more careful". The lesson is that carefulness does not scale.** With two people it is one mistake away; with twenty it is certain.

---

## 9.3 What people try

Before looking for a proper solution, notice the things people usually do, and why each is not enough.

### 9.3.1 Copies with names

What we saw in section 9.1: `menu_v2.txt`, `menu_final.txt`. This gives you *some* history, at the cost of confusion. It does not record why or by whom, it multiplies files, and it relies on everyone using the same naming scheme without exception. It does not help at all with the collision.

### 9.3.2 Backups

> **New term: backup.** A copy of your files kept elsewhere so that they can be restored after loss or damage.

A backup protects against losing the *whole* thing (a stolen laptop, a failed disk). Some backup programs keep old versions too. But backups are usually made on a **schedule**, not when you finish a meaningful piece of work, so their versions are arbitrary moments ("Tuesday 3 a.m.") rather than meaningful ones ("added the cake to the menu"). Backups carry no explanations, and they do not combine two people's changes.

### 9.3.3 Shared and synchronised folders

> **New term: synchronised (cloud) folder.** A folder whose contents are copied automatically between several computers, or between a computer and a service on the internet, so they stay the same.

These are very useful, and they solve difficulty 1 (there is one current copy) and part of 5 (people can see each other's changes). But note what they synchronise: *the latest state, including mistakes*. If you delete a file or save nonsense, the mistake is copied everywhere within moments. Some services keep old versions for a time, but they generally keep them by *time*, not by *meaning*, they do not ask you to explain a change, and when two people change the same file at once they typically have to keep two conflicting copies for a person to sort out by hand.

> **Verification pending [R134].** Statements in this section about what backup and synchronisation tools generally do are given in general terms, because products differ and change. No product is named. They will be checked against representative vendors' documentation before publication.

### 9.3.4 Tracked changes inside one file

Word processors can record edits inside a document ("track changes"). That is a real help for one document, edited by a few people, but it works file by file, needs the word-processor format that Chapter 3<!--ref:editors--> showed is not plain text, and cannot describe a *project* of many files that change together (a page, its stylesheet and its logo).

### 9.3.5 The summary

| Approach | Solves | Leaves unsolved |
|---|---|---|
| Copies with names | Some history | Confusion; no reasons; collisions |
| Backups | Loss of everything | Meaningful versions; explanations; combining changes |
| Synchronised folders | One shared copy | Copies mistakes; conflicts by hand; no reasons |
| Tracked changes | Edits in one document | Many-file projects; plain text |

---

## 9.4 What a better system would need to do

Write the requirements down, and you have written the outline of version control.

1. **Remember every version**, automatically kept, never accidentally overwritten.
2. **Name and explain each version**: who made it, when, and *why*, in the author's own words.
3. **Show what changed** between any two versions, line by line.
4. **Go back** to any earlier version, and recover from mistakes.
5. **Handle many files together**: a change to a page and its stylesheet is one change.
6. **Let people work at the same time**, in parallel, and then **combine** their work, and say clearly when two changes truly collide.
7. **Work without a network**, and keep the whole history on your own computer.
8. **Be trustworthy**: it should be impossible for history to be altered *silently* or to be damaged without detection.

Git was designed to meet these requirements. Requirement 6 is the subject of Chapters 20<!--ref:branching--> to 22<!--ref:conflicts-->; requirement 7 is why Chapter 11<!--ref:distributed--> introduces "distributed" systems; requirement 8 is why Chapter 30<!--ref:objects--> looks inside Git.

---

## 9.5 Version control, defined

> **New term: version.** One particular state of a file or project at a point in time.

> **New term: history.** The recorded sequence of versions of a project, with the reasons and authors for each.

> **New term: version control.** A system that records the history of a project's files, so that you can see what changed, who changed it and why, return to earlier versions, and let many people work together. It is also called *source control* or *revision control*.

**Version control is a tool for working with change over time.** It is not a backup, although it makes a good part of one; it is not a file-sharing service, although services are built on it; and it is not only for programmers. Anyone who keeps a set of files that change (a novel, a thesis, the notes of a club) benefits.

**When you might not need it.** A single file that never changes, or a set of large binary files that people replace wholesale (raw video, say) gain less, because line-by-line comparison is impossible (Chapter 3<!--ref:editors-->). Version control still *keeps* such files, but its best features work on text.

**How the rest of the book uses this.** Part III teaches Git step by step. You will record versions, read them, compare them, go back, work in parallel and combine. When you do, come back to the six difficulties in section 9.2: each Git feature answers one of them.

---

## 9.6 Try it yourself

> **Try it.** Reproduce sections 9.1 and 9.2.1 in your practice folder. Open your terminal, go to `sharif-git-lab`, and type the commands from the two recordings, one at a time. Compare each result with the recording. (Use `cd` to enter the folder they create, and remember that `ls` may sort the file names differently on your system: upper-case letters sort before lower-case ones in the recording, and your computer may do otherwise.)
>
> *Expected result:* the same five files; the same two `diff` reports; and the shared `menu.txt` ending without the cake line.
>
> If `diff` is not available in your terminal, note that fact; it does not affect the rest of the book.

---

## Checkpoint

## What You Learned

- Copies with names, backups, synchronised folders and tracked changes each address part of the problem, but none records meaningful, explained versions of a whole project.
- Six difficulties recur: which is current, what changed, why, can I go back, how do we work together, and who did what.
- Copying a file over a shared file can silently erase someone else's work; carefulness does not scale.
- A better system must remember versions, explain them, show differences, go back, handle many files together, let people work in parallel, work offline and be trustworthy.
- Version control is a system that records a project's history and supports these needs.

## New Vocabulary

- **Backup**: a copy of files kept elsewhere so they can be restored after loss.
- **Synchronised (cloud) folder**: a folder whose contents are kept the same across computers or a service.
- **Version**: one particular state of a file or project at a point in time.
- **History**: the recorded sequence of versions of a project, with reasons and authors.
- **Version control**: a system that records a project's history so that changes can be seen, reversed and combined.

## Commands Learned

`diff` (compares two text files line by line). Also used again: `mkdir`, `cd`, `printf`, `cp`, `cat`, `ls`.

## Common Mistakes

1. **Believing "be more careful" solves collisions.** The problem is structural.
2. **Treating a synchronised folder as version control.** It copies mistakes as quickly as improvements.
3. **Naming files `final`.** The name is a promise that will be broken.
4. **Assuming a backup contains meaningful versions.** It contains moments.
5. **Assuming version control is only for code.** Any text that changes benefits.

## Practice

Do the exercises in [`exercises/ch09-exercises.md`](../../../exercises/ch09-exercises.md).

## Self-Test

1. Name the six difficulties of changing files.
2. In the collision of section 9.2.1, why did no error appear?
3. Give two things a synchronised folder does *not* record.
4. Why is a backup different from version control?
5. What does the `2a3` in a `diff` report mean?
6. State three requirements a version-control system must meet.

## Before Moving On

You are ready for Chapter 10<!--ref:history--> if you can:

- [ ] explain the collision story to someone else in your own words
- [ ] name at least three things a backup or synchronised folder does not do
- [ ] define version control without using the word "control"
- [ ] read a simple `diff` report

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The listing of five files, the `diff` outputs, and the shared-folder collision (Alice's addition silently lost) | Locally tested: interactive Bash 5.2 and zsh 5.9 recordings, re-run in CI (`verification/ch09-problem`) | R135 |
| General descriptions of backups, synchronised folders and tracked changes | Needs re-verification: general statements about product classes, no product named | R134 |

## Where this leads

Chapter 10<!--ref:history--> tells, briefly, how people tried to solve this problem before Git. Chapter 11<!--ref:distributed--> explains the two great designs of version-control systems. Chapter 13<!--ref:install--> installs Git, and Chapter 16<!--ref:firstrepo--> creates your first version-controlled project.
