---
key: platforms
number: 12
tag: Core
first_read: full
status: draft
requires: [distributed]
ledger: [R140, R141]
---
# Chapter 12 — Git, GitHub, GitLab, Bitbucket [Core]

**In this chapter**

- the single most important distinction in this book: the tool versus the platform
- what Git is, and what it is not
- what a hosting platform adds, using GitHub as the main example
- how GitLab and Bitbucket relate, and how to choose without declaring a winner
- names, trademarks and independence

**Before you start.** Chapter 11<!--ref:distributed-->: you know what a repository is, and that a shared repository is a convention, not a requirement.

> **Independent publication.** This book is an independent educational work by Sharif Issah Tingane, issued under the SHARIF TECHNOLOGIES name. It is not affiliated with, endorsed by, sponsored by, or published by Git, GitHub, GitLab, Bitbucket, Microsoft, or any company mentioned. Names of products and companies are trademarks of their respective owners and are used here only to identify them.

> **Verification pending [R140].** Descriptions of products and companies in this chapter are general and have not yet been checked against each product's own documentation. Products change quickly; the chapter avoids statements about specific features, prices or ownership for that reason. Check current official sources before relying on any product detail.

---

## 12.1 Two different things with similar names

Almost every beginner confuses the following two words at first, and the confusion causes real errors, so this chapter is placed before you install anything.

> **Git is the version-control system.**
>
> **GitHub is an online platform built around Git repositories and around collaboration on software.**

Read them twice. They are **two different things, made by different people, that do different jobs**, and you can use either without the other.

> **New term: Git.** A free, open-source distributed version-control system. It is a program that runs on your own computer and keeps the history of a project in a repository.

> **New term: hosting platform.** An online service that stores shared copies of repositories for you, and adds features for working together around them.

> **New term: GitHub.** A widely used hosting platform for Git repositories, with features for collaboration such as tracking issues, reviewing proposed changes and automating tasks.

A picture that helps: **Git is a camera. GitHub is a photo-sharing website.** The camera takes and keeps your photographs, on your own device, whether or not you ever share one. The website stores copies of photos so that other people can see them, comment on them and gather them into albums. You can use the camera without the website. The website is useless without photographs, and the *photographs are made by the camera*.

| | **Git** | **GitHub** |
|---|---|---|
| What it is | A program | An online service |
| Where it runs | On your computer | On the platform's servers, reached through your browser and through Git itself |
| What it stores | The history of your project | Shared copies of projects, plus discussion around them |
| Needs the internet? | No, for almost everything | Yes |
| Who provides it | The open-source Git project | A company |
| Can you use one without the other? | Yes | It exists to host Git repositories |

---

## 12.2 What lives where

Beginners often look for a feature in the wrong place. Use this table to know whether something belongs to the tool or to the platform.

| Concept | Belongs to |
|---|---|
| Recording a version (a *commit*), reading history, comparing versions | **Git**, on your computer |
| Branches, merging, tags | **Git** |
| Copying history to or from another repository (*push*, *pull*, *fetch*) | **Git** (the other repository may be on a platform) |
| Issues, discussions, project boards | **The platform** |
| Pull requests and reviews | **The platform** (Chapter 45<!--ref:pr-->) |
| Automated workflows (*Actions*) | **The platform** (Chapter 54<!--ref:actions-->) |
| Profiles, organizations, stars, followers | **The platform** |
| Web pages for a project | **The platform** |

> **Verification pending [R140].** Which features a given platform offers, under which names and conditions, is exactly the sort of statement that must come from its current documentation. Part V and Part VI verify each one before describing it.

**Why this matters.** When you type a Git command, you are using the tool, and it will work with any repository that Git understands, whoever hosts it. When you click a button on a website or write a workflow file, you are using the platform's features. Knowing which is which tells you where to look for help, and what still works when the platform is down or you change platform.

---

## 12.3 Git without any platform

A team does not need a hosting platform to use Git. The tool works entirely on your computer. It can also exchange history with a second repository that sits *anywhere*: on a memory stick, on a colleague's laptop, on a server you run yourself, or in a folder on the same machine. This has been tested: a folder on the same computer, prepared as a shared repository, worked as the "meeting place" for pushing and fetching history in the book's test environment on two versions of Git.

> **Checked against the documentation [R141].** The test is recorded in the script `research/git-verification/verify-git-basics.sh` in the companion repository (bare-repository checks), and the Git 2.56.0 manual for `git init` documents the `--bare` option ("Create a bare repository"). Both the test and the manual concern the tool, not any hosting platform.

Chapter 23<!--ref:remotes--> will let you repeat this experiment with two repositories on your own computer and no account at all. Then, in Part V, you will connect the same repository to GitHub, and you will see that only the *address* changes.

---

## 12.4 Other platforms

GitHub is not the only hosting platform. Others, such as **GitLab** and **Bitbucket**, also host Git repositories and add their own collaboration features.

> **New term: GitLab.** A hosting platform for Git repositories, with collaboration and automation features, that can be used as a service or run on a team's own servers.
>
> **New term: Bitbucket.** A hosting platform for Git repositories from a different company, with its own collaboration features.

Because they all host Git repositories, **your Git skills transfer**: the commands to record, compare, branch and merge are identical. What differs is the platform's own features and vocabulary. (GitHub calls a proposal to merge changes a *pull request*. Some other platforms use a different name for the same idea; check the platform's documentation.)

### 12.4.1 Choosing a platform

There is no universal winner. When a team chooses, it weighs questions such as:

1. **Where must the code live?** Some organizations must keep code on servers they control.
2. **What features does the team need?** Issue tracking, review, automated tests and deployment differ in style and depth.
3. **Who else is here?** If you want to contribute to open-source projects, you go where they are.
4. **Cost and limits.** Plans, limits and prices change; consult the current official pages.
5. **Integrations.** The tools you already use.
6. **Privacy and legal duties.** Where data is stored, and who may see it.

Every one of these is a question about *the platform*. None of them changes how you use Git.

---

## 12.5 Other version-control tools

Git is not the only version-control tool, either. Other tools exist, both centralised (in the sense of Chapter 11<!--ref:distributed-->) and distributed. This book does not teach them. If you meet a project that uses one, the *concepts* of Part II still apply: history, versions, differences, merging, and the distinction between centralised and distributed designs.

**Git versus GitHub versus GitLab versus Bitbucket, in one sentence each:**

- **Git**: the tool that keeps the history.
- **GitHub, GitLab, Bitbucket**: three platforms that host shared copies of Git repositories and add collaboration features.

---

## 12.6 Avoiding the common confusions

| You may hear | The accurate version |
|---|---|
| "I pushed it to Git." | "I pushed it to a repository (for example on GitHub)." Git is the tool; the repository is the destination. |
| "Git is owned by GitHub." | Not so: Git and GitHub are different things from different sources. (See the verification notice.) |
| "I need GitHub to use Git." | No: Git works locally and with any repository. |
| "GitHub *is* version control." | GitHub is a platform that hosts Git repositories; the version control is done by Git. |
| "I lost my repository because GitHub is down." | Your local copy is complete (Chapter 11<!--ref:distributed-->); only sharing is affected. |

---

## Checkpoint

## What You Learned

- Git is the version-control system; GitHub is an online platform built around Git repositories and collaboration.
- Git runs on your computer and works without a network; a platform stores shared copies and adds features such as issues, reviews and automation.
- Features such as pull requests and Actions belong to the platform, not to Git.
- Git can exchange history with any repository, hosted anywhere or nowhere in particular.
- GitLab and Bitbucket are other platforms for Git repositories; Git skills transfer among them.
- Choosing a platform is a decision about features, location, cost and community, not about how Git works.

## New Vocabulary

- **Git**: a free, open-source distributed version-control system that runs on your computer.
- **Hosting platform**: an online service that stores shared copies of repositories and adds collaboration features.
- **GitHub**: a widely used hosting platform for Git repositories.
- **GitLab**: another hosting platform for Git repositories.
- **Bitbucket**: another hosting platform for Git repositories, from a different company.

## Commands Learned

None.

## Common Mistakes

1. **Saying "Git" when you mean the platform, or the reverse.**
2. **Thinking you need a platform account to use Git.**
3. **Looking for platform features (pull requests, Actions) in Git's documentation.**
4. **Believing a Git repository belongs to a platform.** The history is yours.
5. **Choosing a platform by habit, without weighing the questions in section 12.4.1.**

## Practice

Do the exercises in [`exercises/ch12-exercises.md`](../../../exercises/ch12-exercises.md).

## Self-Test

1. Complete the sentence: "Git is …, and GitHub is …".
2. Name two things that belong to Git and two that belong to a platform.
3. Can you use Git without GitHub? Explain.
4. What changes, and what stays the same, if a team moves from one platform to another?
5. Why is "I pushed it to Git" an imprecise sentence?

## Before Moving On

You are ready for Part III if you can:

- [ ] explain the difference between Git and GitHub to a friend, using your own analogy
- [ ] say where a pull request "lives" (tool or platform)
- [ ] name two other hosting platforms
- [ ] explain why your local Git copy is complete without any platform

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Descriptions of Git, GitHub, GitLab and Bitbucket; what belongs to tool versus platform | Time-sensitive; unverified (no feature, price or ownership claim is made) | R140 |
| A Git repository needs no hosting platform; a local shared repository works as a meeting place | Locally tested on Git 2.43.0 and the CI runner's Git (bare-repository checks). Some concept and option statements for this row were also checked in the Git 2.56.0 manual (git-init); the ledger row says which. | R141 |

## Where this leads

Part III begins with Chapter 13<!--ref:install-->: installing and checking Git on your computer, using the terminal from Chapter 7<!--ref:terminal-->. Chapter 23<!--ref:remotes--> returns to the "tool versus platform" idea with a hands-on experiment, and Part V (starting at Chapter 36<!--ref:whatgh-->) introduces GitHub properly.
