---
key: ghaccount
number: 37
tag: Core
first_read: full
status: draft
requires: [whatgh, accounts]
ledger: [R228, R229, R230, R231]
---
# Chapter 37 — Account and Profile [Core]

**In this chapter**

- what a GitHub account is, and how to choose a username
- how your Git identity and your account connect
- what a profile shows, and who can see it
- what to keep off a profile
- organisations, briefly

> **How to read this chapter.** Everything here is about how a web service *behaves*. The statements are checked against GitHub's own documentation (the open `github/docs` repository at commit `2eaab0b`, 29 September 2026) and its `site-policy` repository (commit `b9578b5`), and are labelled with the ledger row that records the check. No step was run on a live account, and what the screens look like was not seen, so buttons and menus are described by their idea, not their position. The Git side (your name and email in commits) was tested in Chapter 14<!--ref:config-->.

**Before you start.** Chapter 36<!--ref:whatgh--> and Chapter 6<!--ref:accounts--> (accounts, passwords and trust in general). No commands in this chapter are new.

---

## 37.1 What an account is

An **account** on a platform is a stored identity: a **username**, one or more **email addresses**, a way to prove that you are you (a password and more, Chapter 38<!--ref:ghauth-->), and settings. Everything you do on the platform (a repository, a comment, a pull request) is attributed to it.

> **Checked against GitHub's documentation (R228).** "Creating an account on GitHub" says that to get started you need "a personal account and a verified email address", that you sign up at `github.com/signup` (or with the supported social logins Google or Apple), and that without a verified email address "you won't be able to complete some basic GitHub tasks, such as creating a repository". It recommends two-factor authentication. "Types of GitHub accounts" names three kinds of account: user accounts, organisation accounts and enterprise accounts; a *personal account* is the kind you get by signing up yourself, and the same page calls accounts created for automation *machine users*. GitHub's username policy says names "are available on a first-come, first-served basis", that requests to reclaim a name because it looks inactive are not accepted, and that name squatting is prohibited. The exact character rules for a username were not found in these pages; the sign-up form states them.

**Before you sign up, decide three things:**

1. **Which email address?** Use one that you will keep for years, and that you can read. Recovery (Chapter 38<!--ref:ghauth-->) depends on it.
2. **Which username?** It becomes part of every address of your repositories (Chapter 36<!--ref:whatgh-->: `github.com/<username>/<repository>`). Choose one that you will not be embarrassed by in five years, and consider whether it should be tied to your real name. Employers and clients may look at it.
3. **Personal or work?** If a workplace or school will ask you to use its own arrangements, ask before you create an account in their name, and keep personal projects separate from theirs.

---

## 37.2 Your Git identity and your account

In Chapter 14<!--ref:config--> you set `user.name` and `user.email`. Git writes them into every commit **as text**, and Git itself never checks them (Chapter 33<!--ref:gitsec-->).

The platform, however, **can connect** a commit to an account by its **email address**: if the email in a commit matches an address that an account has confirmed, the platform may show that account as the author of the commit. If the email matches no account, the commit still exists, but it will not be linked to a profile.

> **Checked against GitHub's documentation (R229).** "Email addresses" says GitHub "uses your commit email address to associate commits with your account", and that to have commits attributed to you and shown in your contribution graph you must use "an email address that is connected to your account", or the `noreply` address provided in your email settings. For commits pushed from the command line the address comes from your Git configuration; to use the `noreply` address there, set it with `git config`. To use it for web-based edits, choose **Keep my email address private** in the settings. There is also an option to block command-line pushes that expose your personal address. "Any commits you made prior to changing your commit email address are still associated with your previous email address." The book adds one thing the documentation does not say: a commit's email is public wherever the repository is public, and stays in the history (Chapter 30<!--ref:objects-->).

**A safe habit:** decide, *before* you make your first public commit, which email you are willing to publish, and set it with `git config` (Chapter 14<!--ref:config-->). Changing it later does not change commits that already exist.

---

## 37.3 The profile

A **profile** is your public page. Its parts, as GitHub's documentation lists them:

| Part | What it is |
|---|---|
| Name, picture, short description | What visitors see first |
| Repositories | The public repositories that you own |
| **Pinned repositories** | A few that you choose to show at the top |
| **Profile README** | A special repository, named the same as your username, whose README is displayed on the profile |
| **Contribution graph** | A calendar of activity |
| Organisations | Groups that you belong to (Chapter 68<!--ref:orgs-->) |

> **Checked against GitHub's documentation (R230).** "About your profile" lists the profile README, personal information (picture, name and bio), contribution activity, pinned items and a status. A **profile README** is shown when "you've created a repository with a name that matches your GitHub username", the repository is public, it contains a `README.md` in its root, and that file has some content. **Pinned** items are "up to six repositories and gists, combined". The **contribution graph** ("Contributions on your profile" and its reference page) records contributions with times in UTC, shows only public-repository activity by default (you can choose to show private activity in anonymised form), and counts actions such as creating a repository or forking always, and opening an issue or pull request, reviewing, and making a commit *sometimes*. A commit counts only if its email is associated with your account, it was made in a standalone repository (not a fork), and it is on the default branch or `gh-pages`, and you are a collaborator or organisation member, or have forked it, or have opened a pull request or issue there. A setting exists to "make profile private and hide activity". A graph of activity is not a measure of skill: it counts what the platform counts, on its rules, and quiet weeks are normal.

**Practical advice.**

- Pin the repositories that show your best and most complete work, not the newest.
- Write a short description of who you are and what you are learning, in plain language.
- Everything on a public profile can be read by anybody, including people that you do not know, and it may be copied and remembered (Chapter 33<!--ref:gitsec-->).

---

## 37.4 What to keep off a profile

- Your home address, phone number, or your daily schedule.
- Private email addresses that you do not want to receive mail on.
- Anything that identifies children or other people without their agreement.
- Names of clients or employers that you have not been allowed to share.
- Secrets of any kind (Chapter 33<!--ref:gitsec-->).

Treat a profile as a **shop window**: it should show what you want visitors to see, and nothing else.

---

## 37.5 Organisations

An **organisation** is a shared account that owns repositories and has **members** with roles, so that a team, a school class, or a project does not depend on one person's account. Chapter 68<!--ref:orgs--> covers them. For now, note that a repository can live under a person or under an organisation, and that this changes its address (`github.com/<owner>/<repository>`) and who can manage it.

> **Checked against GitHub's documentation (R231).** "Types of GitHub accounts" says organisations are "shared accounts where a large number of people can collaborate across many projects at once"; that "you cannot sign in to an organization", because each person signs in to their own user account and actions are attributed to it; that members can have different roles; that owners and security managers manage settings; and that teams are nested sub-groups of members. Which organisation features depend on the plan was not checked.

---

## 37.6 A checklist for your first account

1. Choose the email address and the username on paper first.
2. Create the account through the platform's own site (type the address yourself; do not follow a link from a message).
3. Confirm your email address when asked.
4. Turn on stronger sign-in protection *now* (Chapter 38<!--ref:ghauth-->).
5. Decide which email address commits will publish, and set `git config user.email` accordingly (Chapter 14<!--ref:config-->).
6. Fill in only the profile fields that you are happy to make public.
7. Sign out and sign in again, to prove that you can.

> **⚠️ CAUTION.** Do not create the account from a shared or borrowed computer without signing out, and never share the password. A platform account that owns your code is worth protecting.

---

## Checkpoint

## What You Learned

- An account is a stored identity; everything you do on the platform is attributed to it.
- A username appears in every repository address, so choose it deliberately.
- The platform can link a commit to an account by email; a commit's email is public in a public repository and stays in the history.
- A profile shows what you choose to share; GitHub offers a setting to make it private, and the graph shows only public activity by default. Show only what you want visitors to see.
- An organisation owns repositories for a group.

## New Vocabulary

No new terms. This chapter uses **account** from Chapter 6<!--ref:accounts-->.

## Commands Learned

None. `git config user.email` from Chapter 14<!--ref:config--> is the Git side of your identity.

## Common Mistakes

1. **Choosing a username in a hurry.**
2. **Publishing a private email address in public commits.**
3. **Treating the contribution graph as a score.**
4. **Putting personal details on a public profile.**
5. **Skipping stronger sign-in protection at the start.**

## Practice

Do the exercises in [`exercises/ch37-exercises.md`](../../../exercises/ch37-exercises.md). They need no live account.

## Self-Test

1. Name three things to decide before creating an account.
2. How can a commit be linked to an account?
3. Why should you choose the commit email before the first public commit?
4. Name three things to keep off a public profile.
5. Why is the contribution graph not a measure of skill?

## Before Moving On

You are ready for Chapter 38<!--ref:ghauth--> if you can:

- [ ] explain the link between `user.email` and an account
- [ ] name what to decide before creating an account
- [ ] say what should stay off a profile
- [ ] describe what an organisation is for

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Git writes `user.name` and `user.email` into commits as text (Chapter 14<!--ref:config-->) | Locally tested in Chapter 14<!--ref:config--> | n/a here |
| Account creation, usernames, profile parts, the contribution graph, email matching, organisations | Checked against `github/docs` and `site-policy`; screens not seen (no live account) | R228-R231 |

## Where this leads

Chapter 38<!--ref:ghauth--> covers signing in and protecting the account. Chapter 39<!--ref:ghrepo--> creates your first repository, and Chapter 68<!--ref:orgs--> returns to organisations.
