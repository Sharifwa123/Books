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

> **⚠️ How to read this chapter.** Everything here is about how a web service *looks and behaves*. The official documentation could not be reached while this chapter was written, and the steps were not run on a live account, so **every statement about GitHub is *Verification pending*.** The Git side (your name and email in commits) was tested in Chapter 14<!--ref:config-->. Use this chapter as a checklist of *what to look for*, and confirm each point on your own screen and in GitHub's current documentation.

**Before you start.** Chapter 36<!--ref:whatgh--> and Chapter 6<!--ref:accounts--> (accounts, passwords and trust in general). No commands in this chapter are new.

---

## 37.1 What an account is

An **account** on a platform is a stored identity: a **username**, one or more **email addresses**, a way to prove that you are you (a password and more, Chapter 38<!--ref:ghauth-->), and settings. Everything you do on the platform (a repository, a comment, a pull request) is attributed to it.

> **Verification pending [R228].** The steps to create an account (the page, the fields, the email confirmation and the checks that the service performs), the account types that exist (personal, organisation and others), and the current rules for usernames were not verified.

**Before you sign up, decide three things:**

1. **Which email address?** Use one that you will keep for years, and that you can read. Recovery (Chapter 38<!--ref:ghauth-->) depends on it.
2. **Which username?** It becomes part of every address of your repositories (Chapter 36<!--ref:whatgh-->: `github.com/<username>/<repository>`). Choose one that you will not be embarrassed by in five years, and consider whether it should be tied to your real name. Employers and clients may look at it.
3. **Personal or work?** If a workplace or school will ask you to use its own arrangements, ask before you create an account in their name, and keep personal projects separate from theirs.

---

## 37.2 Your Git identity and your account

In Chapter 14<!--ref:config--> you set `user.name` and `user.email`. Git writes them into every commit **as text**, and Git itself never checks them (Chapter 33<!--ref:gitsec-->).

The platform, however, **can connect** a commit to an account by its **email address**: if the email in a commit matches an address that an account has confirmed, the platform may show that account as the author of the commit. If the email matches no account, the commit still exists, but it will not be linked to a profile.

> **Verification pending [R229].** How the platform matches commit emails to accounts, and its option to hide your real email address and use a special "no-reply" address instead, were not verified. Both matter: a commit's email is **public** wherever the repository is public, and it stays in the history (Chapter 30<!--ref:objects-->).

**A safe habit:** decide, *before* you make your first public commit, which email you are willing to publish, and set it with `git config` (Chapter 14<!--ref:config-->). Changing it later does not change commits that already exist.

---

## 37.3 The profile

A **profile** is your public page. Typical parts (all to be checked):

| Part | What it is |
|---|---|
| Name, picture, short description | What visitors see first |
| Repositories | The public repositories that you own |
| **Pinned repositories** | A few that you choose to show at the top |
| **Profile README** | A special repository, named the same as your username, whose README is displayed on the profile |
| **Contribution graph** | A calendar of activity |
| Organisations | Groups that you belong to (Chapter 68<!--ref:orgs-->) |

> **Verification pending [R230].** The list above, the exact rule for a profile README, what the contribution graph counts (and does not count), and what is public by default were not verified. A common misunderstanding is worth remembering even before you check: **a graph of activity is not a measure of skill**. It counts what the platform counts, on its rules, and quiet weeks are normal.

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

> **Verification pending [R231].** The features of organisations, the roles, and what depends on the plan were not verified.

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
- A profile is public by default (to be checked); show only what you want visitors to see.
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
| Account creation, usernames, profile parts, the contribution graph, email matching, organisations | **Not verified** (official documentation not reachable; no live account) | R228-R231 |

## Where this leads

Chapter 38<!--ref:ghauth--> covers signing in and protecting the account. Chapter 39<!--ref:ghrepo--> creates your first repository, and Chapter 68<!--ref:orgs--> returns to organisations.
