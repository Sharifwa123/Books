---
key: orgs
number: 68
tag: Deep
first_read: later
status: draft
requires: [collab]
ledger: [R325, R326, R327]
---
# Chapter 68 — Organizations and Enterprise Concepts [Deep]

**In this chapter**

- the three kinds of account: user, organization, enterprise
- members, owners and teams
- repository roles and base permissions in an organization
- plans, and the difference between Enterprise Cloud and Enterprise Server

> **How to read this chapter.** This is a **Deep** chapter and can be read later; you can use GitHub for years without an organization. Everything here comes from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026) and **was not run on a live account**. Organization settings screens are not described. **Prices, included quantities and plan contents are not stated in this book, because they change**; read the current plans page for your account.

**Before you start.** Chapter 49<!--ref:collab--> (repository roles and collaborators).

---

## 68.1 Three kinds of account

GitHub's documentation lists "three types of accounts": **user accounts**, **organization accounts** and **enterprise accounts**.

- **User account.** "Every person who uses GitHub signs in to a user account." It can own repositories, packages and projects, and actions on GitHub are attributed to it. There are two sorts of user account: **personal accounts** (you signed up yourself) and accounts created for you by an enterprise, with some settings managed by the enterprise. Accounts "are intended for humans, but you can create accounts to automate activity", which the documentation calls a **machine user**.
- **Organization account.** "Organizations are shared accounts where a large number of people can collaborate across many projects at once." Like a user account, an organization can own repositories, packages and projects. **"You cannot sign in to an organization."** Each person signs in to their own user account, and the actions they take on organization resources are attributed to that user account. A user can belong to several organizations.
- **Enterprise account.** It "allows central management of multiple organizations" for policy and billing. Unlike organizations, enterprise accounts "cannot directly own resources like repositories, packages, or projects": the organizations inside the enterprise own them.

Chapter 37<!--ref:ghaccount--> was about the first kind. This chapter is about the second and the third.

> **Checked against GitHub's documentation (R325).** "Types of GitHub accounts" and "About organizations".

---

## 68.2 Why an organization

A personal account is the right place for your own projects. An organization fits when a **group** shares ownership: a team, a company, a club, a community project. Reasons the documentation gives:

- **Roles.** "You can invite people to join your organization, then give these organization members a variety of roles that grant different levels of access to the organization and its data." Only organization owners and security managers can manage the organization's settings; all members can collaborate in repositories and projects.
- **Teams.** "You can create nested teams that reflect your group's structure, with cascading access permissions and mentions."
- **Settings and policy.** For example "restricting the types of repositories that members can create".
- **Security.** "You can enforce security requirements and review the organization's audit log."
- **Continuity.** Repositories owned by an organization do not belong to one person's account. The documentation's first best practice is to **assign multiple owners**, so that the organization does not depend on one person; a repository under one personal account depends on that one person.

Further best practices in the documentation: use teams; keep teams visible "whenever possible and reserving secret teams for sensitive situations".

**A note on size.** The documentation warns that "If an organization exceeds 100,000 members, some UI experiences and API functionality may be degraded."

---

## 68.3 Repository roles in an organization

Chapter 49<!--ref:collab--> introduced repository roles. In an organization, the documentation lists them "from least access to most access":

| Role | Recommended for |
|---|---|
| Read | non-code contributors who want to view or discuss the project |
| Triage | contributors who need to manage issues and pull requests without write access |
| Write | contributors who actively push to the project |
| Maintain | project managers who need to manage the repository without access to sensitive or destructive actions |
| Admin | people who need full access, including sensitive and destructive actions such as managing security or deleting a repository |

The roles can be given to organization members, to **outside collaborators** (people who are not members but are given access to some repositories) and to teams. The documentation's rule is the one from Chapter 60<!--ref:wfsec-->: choose the role that fits "without giving people more access to the project than they need". Organization owners "have admin access to every repository owned by the organization".

**Base permissions.** Owners can set a level that applies to **all members** for **all** the organization's repositories. It does not apply to outside collaborators. By default, "members of an organization will have Read permissions to the organization's public repositories". If someone with admin access to a repository grants a member a higher level, "the higher level of access overrides the base permission". Changes affect new and existing members. Internal repositories have "a minimum visibility level of read, even if the base permission has been set to none".

**A warning worth repeating.** "When someone adds a deploy key to a repository, any user who has the private key can read from or write to the repository (depending on the key settings), even if they're later removed from the organization."

> **Checked against GitHub's documentation (R326).** "Repository roles for an organization" and "Setting base permissions for an organization". Custom repository roles exist for some plans and were not examined.

---

## 68.4 Plans, and Enterprise Cloud versus Server

GitHub "offers free and paid plans"; some plans "are available only to personal accounts, while other plans are available only to organization and enterprise accounts". Plans differ in features for private repositories, included Actions minutes and storage, support and controls such as required reviewers and protected branches in private repositories. **This book does not list quantities or prices.** Two facts help to read the plans page:

- **Public repositories** have a full feature set on the free plans; the limits mostly concern **private** repositories.
- The enterprise product "includes two deployment options": **Enterprise Cloud**, "hosted by GitHub in the cloud", and **Enterprise Server**, which is "self-hosted". The documentation you read has versions for each; the documentation's own advice is to select the version that reflects your plan.

Enterprise features named in the documentation include central management of policy and billing for many organizations, enterprise-managed user accounts, and additional controls such as audit-log streaming and an IP allow list. Their details belong to an administrator's course, not to this book.

> **Checked against GitHub's documentation (R327).** "GitHub's plans". Specific figures were deliberately left out.

---

## 68.5 Starting an organization

The documentation has a page called "Creating a new organization from scratch"; its steps and screens were **not read** for this book, so follow the current page. Decisions to make first, on paper:

1. **Name and purpose.** The name appears in every URL.
2. **Owners.** At least two, as advised.
3. **Base permission.** Start low (Read or none) and grant more through teams.
4. **Teams.** One per group of people who need the same access.
5. **Repository creation policy.** Who may create which kind of repository?
6. **Two-factor authentication** for members (Chapter 38<!--ref:ghauth-->).
7. **Security defaults** (Chapter 62<!--ref:ghsec-->).

Do the exercises on paper first; creating an organization on a live account is a step outside this chapter (gate D of the book's plan: an authenticated person must do it).

---

## Checkpoint

## What You Learned

- User accounts sign in; organizations cannot be signed in to; enterprise accounts manage many organizations.
- Organizations give roles, teams, policies and continuity.
- Repository roles: Read, Triage, Write, Maintain, Admin; base permissions apply to members, not outside collaborators.
- Assign several owners; use teams; keep access minimal.
- Plans and quantities change; Enterprise Cloud is hosted and Enterprise Server is self-hosted.

## New Vocabulary

**Organization**, **enterprise account**, **machine user**, **outside collaborator**, **base permission**, **team** (see the glossary).

## Commands Learned

No new commands.

## Common Mistakes

1. **Keeping a team's repositories under one person's account.**
2. **A single owner.**
3. **Giving every member Admin.**
4. **Assuming base permissions apply to outside collaborators.**
5. **Trusting a plan list from a book instead of the current page.**

## Practice

Do the exercises in [`exercises/ch68-exercises.md`](../../../exercises/ch68-exercises.md).

## Self-Test

1. Can you sign in to an organization?
2. What can an enterprise account not own directly?
3. Name the five repository roles in order.
4. Who does the base permission not apply to?
5. Why assign more than one owner?

## Before Moving On

You are ready for Chapter 69<!--ref:pages--> if you can:

- [ ] explain the three account types
- [ ] design a small team structure on paper

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Account types; organization features; best practices | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R325 |
| Repository roles and base permissions | Same | R326 |
| Plans and enterprise deployment options | Same; quantities and prices deliberately not stated | R327 |

## Where this leads

Chapter 69<!--ref:pages--> publishes a static website from a repository.
