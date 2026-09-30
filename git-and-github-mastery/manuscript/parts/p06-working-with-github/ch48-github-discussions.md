---
key: discussions
number: 48
tag: Deep
first_read: later
status: draft
requires: [issues]
ledger: [R268, R269]
---
# Chapter 48 — GitHub Discussions [Deep]

**In this chapter**

- what Discussions are, and how they differ from Issues
- categories and their formats
- moderating: answers, locking, closing, converting
- when to use a discussion, an issue or a pull request

> **How to read this chapter.** This is a **Deep** chapter about a service, so it has **no recorded commands** and can be read later. Everything is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. A discussion is stored by the platform and is **not** in your Git repository.

**Before you start.** Chapter 44<!--ref:issues-->.

---

## 48.1 What Discussions are

> **New term: discussion.** An open-ended conversation about a project, kept by the platform in a forum-like section, for questions, ideas, announcements and polls, separate from the tracker of issues.

GitHub's documentation says Discussions let a project's community "engage in conversations about the project's direction and future in an open-ended format", so that maintainers, contributors and visitors "can gather in a central location, without third-party tools". You can share announcements, plan and decide with community input, ask and answer questions ("mark them answered as you respond to them"), and "gauge community opinion using polls".

There are **repository** discussions, for topics specific to one repository, and **organization** discussions, for conversations across repositories. Anyone with access can take part, "however, an administrator must enable Discussions for the repository or organization first". So, like other features in Chapter 43<!--ref:settings-->, it may simply be absent.

---

## 48.2 Discussions, issues or pull requests?

The documentation draws the line like this. Use a discussion for big-picture ideas, brainstorming and developing "a project's specific details before committing it to an issue, which can then be scoped". It suggests discussions when you are in the discovery phase, want feedback from a wider community, want to keep bug fixes, feature requests and general conversations separate, or want to measure interest with polls. **Issues** are for "specific details of a project such as bug reports and planned improvements". **Pull requests** are for comments "directly on proposed changes".

| You have | Use |
|---|---|
| A question about how to use the project | A discussion (Q&A category) |
| An idea that is still vague | A discussion (Ideas category) |
| A bug you can describe and reproduce | An issue |
| A specific task someone will do | An issue |
| A change to the files | A pull request |

The habit that ties them together: when a conversation reaches a decision that needs action, **open an issue** and link the discussion.

> **Checked against GitHub's documentation (R268).** Quotations in this section are from "About Discussions" and "Best practices for community conversations on GitHub". The last habit is the documentation's: "Opening an issue to take action based on the conversation, where applicable".

---

## 48.3 Categories

Discussions are filed in **categories**, which the documentation says maintainers can customise. Each category has a unique name and emoji pairing and a description, and "each repository or organization can have up to 25 categories". You can group categories into sections. The default categories:

| Category | Purpose | Format |
|---|---|---|
| Announcements | Updates and news from maintainers | Announcement |
| General | Anything relevant to the project | Open-ended discussion |
| Ideas | Ideas to change or improve the project | Open-ended discussion |
| Polls | Polls with multiple options | Polls |
| Q&A | Questions for the community to answer | Question and Answer |
| Show and tell | Creations, experiments, tests | Open-ended discussion |

The **format** decides what a discussion can do: only the Question and Answer format has a "mark as answer" step, and polls have voting.

---

## 48.4 Moderation

> **Checked against GitHub's documentation (R269).** With triage permission on the repository, a person can help moderate: mark comments as answers, lock discussions that are no longer useful or damaging to the community, and convert issues to discussions "when an idea is still in the early stages of development". Locking is appropriate "when the entire conversation is not constructive or violates your community's code of conduct" or to make an announcement that should not receive comments. You can also close a discussion, pin discussions "to give topics more visibility", and use repository labels to organise them. Before opening a discussion, check for **contributing guidelines** in the repository.

Moderating is the same craft as everywhere else in this book: be specific, be kind, and prefer removing a conversation from the spotlight (lock, close) to deleting it.

---

## Checkpoint

## What You Learned

- Discussions are open-ended conversations kept by the platform; an administrator must enable them.
- Use a discussion for questions and undecided ideas, an issue for specific work, a pull request for a change.
- Categories (up to 25) have formats: announcement, open-ended, poll, question and answer.
- Moderators can mark answers, pin, lock, close and convert.

## New Vocabulary

**Discussion** (introduced above).

## Commands Learned

None: this chapter is about the platform and not about Git.

## Common Mistakes

1. **Reporting a reproducible bug as a discussion.**
2. **Leaving a decided conversation without an issue for the action.**
3. **Assuming the feature is on.**
4. **Ignoring the contributing guidelines.**

## Practice

Do the exercises in [`exercises/ch48-exercises.md`](../../../exercises/ch48-exercises.md).

## Self-Test

1. Who must switch Discussions on?
2. Which category format allows marking an answer?
3. When does an idea belong in an issue instead?
4. Give one reason to lock a discussion.

## Before Moving On

You are ready for Chapter 49<!--ref:collab--> if you can:

- [ ] choose between discussion, issue and pull request
- [ ] name the default categories
- [ ] say what a moderator can do

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| What Discussions are, when to use them | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R268 |
| Categories, formats, moderation | Checked against `github/docs` | R269 |

## Where this leads

Chapter 49<!--ref:collab--> covers who can do what in a repository, and Chapter 64<!--ref:oss--> how open-source projects run their community conversations.
