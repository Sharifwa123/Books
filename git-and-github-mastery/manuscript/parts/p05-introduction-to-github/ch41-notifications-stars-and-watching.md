---
key: notify
number: 41
tag: Core
first_read: part
status: draft
requires: [ghtour]
ledger: [R244, R245, R246]
---
# Chapter 41 — Notifications, Stars and Watching [Core]

**In this chapter**

- how the platform decides to tell you about activity
- the difference between **watching**, **starring** and **following**
- how to keep the volume of notifications under control
- how long notifications are kept

> **How to read this chapter.** This chapter is about a service, not about Git, so it has **no recorded commands**. Its statements are checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026). No live account was used, so buttons are named by their idea and by the label the documentation gives, and labels can change. Nothing in it changes what is in your Git repository.

**Before you start.** Chapter 40<!--ref:ghtour--> (the parts of a repository page) and Chapter 37<!--ref:ghaccount--> (your account and its email addresses).

---

## 41.1 Three different actions

Three actions look alike and do different things.

| Action | What it means | Effect |
|---|---|---|
| **Watch** a repository | "Tell me about activity here." | You are *subscribed* to updates, so you receive notifications. |
| **Star** a repository | "Save this, and show appreciation." | The repository is added to your list of stars. It does **not**, by itself, send you notifications. |
| **Follow** a person or an organisation | "Show me their public activity." | Their public activity appears on your personal dashboard. |

> **New term: notification.** A message from the platform that something happened in a place you are subscribed to: a comment, a mention, a review request, the result of an automatic check. It arrives in an *inbox* on the website, in a mobile app, by email, or by some mix of these.

> **Checked against GitHub's documentation (R244).** "Notifications are updates that you receive for specific activity that you are subscribed to." The documentation lists what you can subscribe to: a conversation in a specific issue, pull request or gist; all activity in a repository; activity of automatic checks (GitHub Actions); and, if enabled, chosen kinds of events in a repository. Of starring it says: "Starring makes it easy to find a repository or topic again later," and that it "shows appreciation to the repository maintainer"; the stars page lists what you have starred, and adding `/stargazers` to a repository's address shows who has starred it. Following people, it says, puts "their public activity" on your personal dashboard, and following can also lead the platform to recommend repositories.

---

## 41.2 What subscribes you without asking

You do not have to press **Watch** to receive notifications. According to GitHub's documentation you are subscribed to a conversation by default when you:

- are assigned to an issue or pull request;
- open an issue or pull request;
- comment on a thread;
- have your username @mentioned (or a team you belong to is mentioned);
- change the state of a thread, for example by closing an issue or merging a pull request;
- subscribe manually with **Watch** or **Subscribe**.

By default you also watch automatically the repositories that you create under your personal account, and, unless you switch it off in your notification settings, repositories and teams that you join.

> **New term: subscription.** An arrangement that says "send me notifications about this conversation or repository". You can end it with **Unsubscribe**. If you unsubscribe and later somebody mentions you, or a team you are on, you start to receive notifications from that conversation again.

**Why this matters.** A busy project can produce hundreds of messages a day. Most people who feel overwhelmed have not chosen to watch everything: they were subscribed by taking part.

---

## 41.3 Watching, in levels

A repository's **Watch** control is not on or off. The documentation describes these choices:

| Level | You receive |
|---|---|
| Only when you take part or are mentioned | Notifications for conversations you are in, and mentions |
| All activity | Everything in the repository, including new issues and pull requests |
| Ignore | Nothing, not even mentions |
| Custom | Only the kinds of event you choose (for example issues, pull requests, releases), where the platform offers it |

The documentation adds a warning about **Ignore**: "you won't be notified if you're @mentioned", and it does not recommend ignoring a repository for that reason. Choosing **only when participating or mentioned** is the safer way to quieten a repository.

Two limits are stated: you can watch **at most 10,000 repositories**, and a page (`github.com/watching`) lists everything you watch, with an **Unwatch all** option for one owner's repositories.

**A good starting rule.** Watch *all activity* only in the few repositories that you maintain or that your work depends on. Everywhere else, take part or be mentioned.

---

## 41.4 The inbox

The **notifications inbox** (at `github.com/notifications`) is the website's list of your notifications. GitHub's documentation lists these ways to work through it:

- **Done** removes a notification from the inbox; `is:done` finds the ones you finished.
- **Save** flags a notification for later; `is:saved` finds them.
- Mark as read or unread.
- **Unsubscribe** ends the subscription and removes the notification.
- Each notification shows a **reason** label, such as `mention`, `subscribed` or `review requested`, and you can filter by it: `reason:review-requested` shows pull requests waiting for your review.
- You can group by repository or by date and create your own **custom filters**, for example one that shows only the notifications from a project you contribute to in which you are mentioned.

> **Retention.** "Notifications that are not marked as Saved are kept for 3 months. Notifications marked as Saved are kept indefinitely." Email is a second copy: your email client keeps messages for as long as your mail provider does.

---

## 41.5 Where notifications go

You choose the *places* separately for the two big groups, **participating** and **watching**, in your notification settings. The documentation names three places: the inbox on the website, the inbox in the mobile app (which stays in step with the website), and email, which needs a verified email address. If you turn off the web and mobile option for both groups, the inbox stays empty. If you turn off email for both groups, your mail stays quiet.

Depending on the organisation that owns a repository, you can also send its notifications to a different address, for example work mail for work repositories, and your organisation may require the address to be verified for its domain. Every notification email carries **headers** that name the repository and the reason, which you can use to filter mail in your email program.

> **⚠️ CAUTION.** A notification email can contain the text of a private conversation, and it goes to whatever address you chose. Use an address you control, and be careful about forwarding rules.

---

## 41.6 Keeping the volume under control

1. **Decide what you need to act on**, and set *only participating and mentions* everywhere else.
2. **Review `github.com/watching` now and then**, and unwatch what no longer matters.
3. **Use the inbox as a to-do list**: **Done** when handled, **Save** what must wait.
4. **Filter, do not read everything.** Start with `reason:mention` and `reason:review-requested`.
5. **Choose an email address for each purpose**, so that mail rules can sort by it.

Stars, by contrast, cost nothing in attention: a star does not subscribe you. If you want to *hear* about a project's releases without every conversation, use the custom watch level where it is offered.

---

## Checkpoint

## What You Learned

- Watching subscribes you to a repository's activity; starring saves it and shows appreciation; following shows a person's public activity on your dashboard.
- Taking part in a conversation subscribes you to it automatically.
- Watch levels range from "participating and mentions" through "all activity" to "ignore" (which also hides mentions).
- The inbox offers Done, Save, filters and reason labels; unsaved notifications are kept for three months.
- Delivery to the website, the mobile app and email is set separately.

## New Vocabulary

**Notification**, **subscription** (introduced above).

## Commands Learned

None: this chapter is about the platform and not about Git.

## Common Mistakes

1. **Thinking that a star is a subscription.**
2. **Watching all activity everywhere**, then ignoring the inbox.
3. **Choosing "Ignore" to quieten a repository**, and missing a mention.
4. **Sending notifications to an address other people can read.**
5. **Treating the inbox as an archive** when unsaved items disappear after three months.

## Practice

Do the exercises in [`exercises/ch41-exercises.md`](../../../exercises/ch41-exercises.md).

## Self-Test

1. Name three things that subscribe you to a conversation without pressing Watch.
2. What is the difference between starring and watching?
3. Why does the documentation not recommend ignoring a repository?
4. How long are notifications kept, and what changes that?
5. Which query shows the pull requests where your review was requested?

## Before Moving On

You are ready for Chapter 42<!--ref:readme--> if you can:

- [ ] explain watch, star and follow in one sentence each
- [ ] say what subscribed you to a conversation
- [ ] choose a watch level for a repository on purpose

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Subscriptions, default subscriptions, inbox actions, retention | Checked against `github/docs` (commit `2eaab0b`); no live account | R244, R245 |
| Watch levels, limits, delivery places | Checked against `github/docs`; labels may change | R245 |
| Stars, following, stargazers | Checked against `github/docs` | R246 |

## Where this leads

Chapter 42<!--ref:readme--> makes a repository's front page useful to the people who arrive there. Chapter 44<!--ref:issues--> and Chapter 45<!--ref:pr--> are where most notifications come from.
