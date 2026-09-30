---
key: history
number: 10
tag: Core
first_read: later
status: draft
requires: [problem]
ledger: [R136, R137, R138]
---
# Chapter 10 — A Short History of Version Control [Core]

**In this chapter**

- the stages people went through in solving the problem of Chapter 9<!--ref:problem-->
- why the answers changed, stage by stage
- where Git came from, and why it became so widely used
- how to read a claim about history critically

**Before you start.** Chapter 9<!--ref:problem-->: the six difficulties of changing files and the eight requirements of a version-control system. This chapter is optional on a first read (its tag is Core, but the First-Read Path skips it); return to it when you are curious about *why* Git is designed as it is.

> **Verification pending [R136, R137, R138].** History is a matter of record, and this chapter has not yet been checked against the primary sources (the projects' own documentation, the archives of the communities involved, and the published accounts of the people who made these tools). Every named system, every date, and every statement of cause in this chapter is given from general knowledge and is marked for re-verification. The *structure* of the story, that each stage solved a problem left by the one before, is the part to remember. This chapter deliberately contains **no exact dates and no quotations**, so that nothing in it can be wrong in a way that matters until it is verified.

---

## 10.1 Why history helps

Design decisions look arbitrary until you know the problem they answered. Git's commands, its vocabulary and even its odd corners (Chapters 19<!--ref:commits-->, 20<!--ref:branching-->, 27<!--ref:rebase-->) make far more sense if you know what came before. The history of version control is a story of one question asked again and again: **how can many people change the same files, safely, without losing anyone's work?**

---

## 10.2 Stage one: people and copies

The first version control is the one in Chapter 9<!--ref:problem-->: folders and file names, dated copies and careful habits. It works for one person and a small project. It fails when the project grows or a second person joins. Nothing in this stage is a *system*: everything depends on people following a convention.

## 10.3 Stage two: tools for a single computer

The first software answer kept the history of **individual files** on **one computer**. You told the tool "I am about to change this file", it locked the file so nobody else could, you edited it, and you told the tool you had finished, which stored the new version and released the lock. Old versions could be recovered.

> **New term: lock.** A marker that stops other people from changing a file until you release it.

Locking prevents the collision of section 9.2.1 by making sure that only one person can edit a file at a time. Its cost is obvious: **people wait for each other.** If the person with the lock goes on holiday, no one else can change the file.

## 10.4 Stage three: a central server

The next idea moved the history to **one shared server** that everyone connected to. The server held the single official history; each person "checked out" a working copy, edited it, and sent changes back. Tools of this kind also tracked *whole projects* rather than single files, and many of them replaced strict locking with a smarter rule: two people may edit the same file at once, and when they send their changes, the server tries to **merge** them, complaining only if the two edits truly touch the same lines.

> **New term: merge.** To combine two sets of changes into one.

These **centralised** systems were a large step forward. They gave a project one official history, a record of who changed what, and the ability to work in parallel. Chapter 11<!--ref:distributed--> examines them closely, because Git's design is best understood as a reaction to their limits.

Their limits were practical:

- Almost every action needed a connection to the server. On a train, on a slow network, or when the server was down, you could not look at history or record your work.
- A mistake on the server, or a lost server, could damage or lose the *only* copy of the complete history.
- Working on an experimental idea without disturbing others was awkward, because *branches* (parallel lines of work) were slow or costly in many such tools.

## 10.5 Stage four: everyone has everything

The answer to those limits was **distributed** version control: instead of one server holding the history and everyone else holding a snapshot, **every person holds the complete history on their own computer**. You can look at the past, record your own work, and work on an experiment, all without a network. Sharing then becomes a matter of *exchanging* history between copies. Several systems took this approach; Git is the best known.

> **Verification pending [R136].** The naming of particular systems in each stage, and their order, are from general knowledge and are omitted here on purpose until they can be checked against the projects' own histories.

---

## 10.6 Where Git came from

Git's beginning was practical. According to general accounts, it was written in the mid-2000s by the leader of the Linux kernel project, for the needs of the kernel's own very large community of developers, when the tool they had been using was no longer available to them. Its goals, reported in those accounts, matched the requirements of section 9.4: **speed**, a **simple design**, strong support for **thousands of parallel branches**, being **fully distributed**, and being able to handle **very large projects**, all while keeping history safe from silent damage.

> **Partly checked [R137].** Git's own published history was read for this book: the first commit in the `git/git` repository is dated 7 April 2005 and is authored by Linus Torvalds, with the message *Initial revision of "git", the information manager from hell*. That fixes the creator and the year. The **reason** (the earlier tool becoming unavailable) and the **list of goals** are still from general accounts and have not been checked against the Git project's documentation or the kernel community's records, so do not quote them as fact.

Two features of that origin will keep appearing in this book:

1. **Git assumes that many people, some of them strangers, contribute in parallel.** That is why branches are cheap (Chapter 20<!--ref:branching-->) and why Git records not just changes but *who* made them.
2. **Git cares about integrity.** It is built so that history cannot be altered without being noticed (Chapter 30<!--ref:objects-->).

---

## 10.7 Why Git became widely used

Popularity is never the result of a single cause. General accounts usually list several that reinforced one another:

| Reason | Effect |
|---|---|
| Fast, and works offline | Daily work does not wait for a network |
| Cheap branching and merging | Trying ideas and combining work became routine |
| Free to use and open | No cost, no single owner to depend on |
| Reliable integrity | People trust their history |
| Hosting platforms built around Git | Sharing and collaboration became easy; a network effect followed |
| Widespread use itself | Tools, teaching material and job requirements assumed Git |

> **Verification pending [R138].** The list of reasons is a synthesis of general accounts, not a measured result. The claim that Git is "widely used" should be supported by named, dated surveys before publication, and will be.

---

## 10.8 Reading historical claims critically

You will meet strong claims about tools: "X is dead", "Y is the future". A few habits will keep you accurate.

1. **Ask for a date.** Tool landscapes change; a claim without a date has no meaning.
2. **Separate the tool from the platform.** A statement about a hosting platform is not a statement about the tool, and the reverse (Chapter 12<!--ref:platforms-->).
3. **Prefer primary sources.** The tool's own documentation and the people who wrote it are better sources than summaries.
4. **Watch for causal certainty.** "Because of X, Y happened" is almost always a simplification.

---

## Checkpoint

## What You Learned

- Version control developed in stages: dated copies, single-computer file tools with locks, central servers, and distributed systems.
- Each stage solved a limit of the one before: waiting for locks, dependence on a central server, and the cost of working in parallel.
- Git was created for a very large, distributed community and aims at speed, a simple design, cheap branching, distribution, scale and integrity.
- Popularity had several reinforcing causes.
- Historical claims should be dated and traced to primary sources.

## New Vocabulary

- **Lock**: a marker that stops others from changing a file until it is released.
- **Merge**: to combine two sets of changes into one.

## Commands Learned

None.

## Common Mistakes

1. **Treating a tool's popularity as proof that it suits your project.**
2. **Confusing a tool with a platform built on it.**
3. **Quoting undated claims about "the best" tool.**

## Practice

Do the exercises in [`exercises/ch10-exercises.md`](../../../exercises/ch10-exercises.md).

## Self-Test

1. Why does file locking prevent collisions, and what is its cost?
2. Name two limits of a central-server system that a distributed system removes.
3. What does "distributed" mean in version control?
4. Give two ways to check a claim about the history of a tool.

## Before Moving On

You are ready for Chapter 11<!--ref:distributed--> if you can:

- [ ] describe the four stages in your own words
- [ ] say what problem each stage solved and what problem it left
- [ ] explain why "everyone has the whole history" helps when the network is down

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The staged account of version control (copies; locking tools; central servers; distributed systems) | Needs re-verification; no system or date is stated | R136 |
| Git's origin, creator, reasons and design goals | Needs re-verification | R137 |
| Why Git became widely used | Needs re-verification; synthesis of general accounts | R138 |

## Where this leads

Chapter 11<!--ref:distributed--> compares the centralised and distributed designs in detail. Chapter 12<!--ref:platforms--> separates Git from the platforms built around it.
