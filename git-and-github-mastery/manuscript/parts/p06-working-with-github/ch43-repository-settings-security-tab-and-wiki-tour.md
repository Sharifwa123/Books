---
key: settings
number: 43
tag: Core
first_read: part
status: draft
requires: [ghtour]
ledger: [R250, R251, R252, R253]
---
# Chapter 43 — Repository Settings, Security Tab and Wiki Tour [Core]

**In this chapter**

- what lives in a repository's **Settings**, and which changes are hard to undo
- what the **Security** tab is for, and why its label varies
- the **wiki**, which turns out to be a Git repository
- the **Deployments** view, and why views depend on plan, visibility and role

> **How to read this chapter.** The wiki part was run and recorded with local repositories. Everything about GitHub is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used, and labels can change. The chapter is a **tour**: later chapters cover each feature in depth.

**Before you start.** Chapter 40<!--ref:ghtour--> (the parts of a repository page) and Chapter 39<!--ref:ghrepo-->. The recording ran in Bash and zsh on Git 2.43.0 and was re-run in CI on newer Git versions.

---

## 43.1 Who sees what

Not everybody sees the same tabs. What appears on a repository depends on four things:

- the **visibility** (public, private, or, for enterprise organisations, internal);
- your **role** on the repository (Chapter 49<!--ref:collab-->);
- the **plan** of the owner (some features exist only on paid plans);
- the **settings** of the repository and of its organisation.

If a section named in this chapter is missing on your screen, do not assume a mistake. Check these four things first.

---

## 43.2 Settings

**Settings** is where a repository's administrators change how the repository behaves. GitHub's documentation describes many changes there. The ones a beginner should know, with what the documentation says about each:

| Setting | What it does | What to know |
|---|---|---|
| **Visibility** | Public or private (and internal in enterprise organisations) | Changing it has consequences. Making a repository private detaches public forks into a new network; making it public makes its Actions history and logs visible to everyone. |
| **Features** | Switches issues, wiki, discussions, projects and other sections on or off | If you switch issues off and on again, "any issues that were previously added will be available". |
| **Default branch** | The branch that the page shows and that new clones check out | Your account also has a setting for the default branch name of *new* repositories. |
| **Danger zone** | Change visibility, transfer or delete | Deleting is not always undoable, see below. |

> **Checked against GitHub's documentation (R250).** "Setting repository visibility" lists consequences of a change: for example, making a repository private detaches public forks into a new network, and making one public means "Actions history and logs will be visible to everyone". "Disabling issues" says previously added issues are available again if you re-enable them. The default branch name for *new* repositories is set in your account settings. "Deleting a repository" says that deleting permanently deletes team permissions and that this "cannot be undone"; deleting a public repository does not delete its forks, but deleting a private one deletes all its forks. "Some deleted repositories can be restored within 90 days", but not one that was part of a fork network that is not empty. A transfer gives the new owner immediate administration, and for a transfer to another personal account the new owner gets a confirmation email; the invitation expires after one day.

> **⚠️ CAUTION.** Settings changes are made on the platform, and **Git will not record them**: your history does not show that a repository was made public, or which feature was switched off. Treat the danger zone the way you treat `git reset --hard` (Chapter 25<!--ref:undo-->): stop, read, and be sure. Before deleting, make sure that at least one clone has all the history you need (Chapter 23<!--ref:remotes-->).

---

## 43.3 The Security tab

A repository page has a tab for security features: where alerts about leaked secrets, vulnerable dependencies and code problems are collected. GitHub's documentation gives the tab a name that **depends on a feature flag**: in its own source the label is written as "Security and quality" when the flag `security-and-quality-tab` is on, and "Security" otherwise. So two people can see different names for the same tab. That is the best example in this book of why the chapters teach ideas and not labels (Chapter 40<!--ref:ghtour-->).

> **Checked against GitHub's documentation (R251).** The documentation source defines the tab's label as "Security and quality" or "Security" depending on a flag. Secret-scanning alerts appear on this tab ("GitHub generates an alert on your repository's ... tab"). What each security feature does, and which plans include it, is covered in Chapter 62<!--ref:ghsec-->; this chapter does not describe them.

---

## 43.4 The wiki

Every repository can have a **wiki**: a section for long-form documentation. GitHub's documentation says a README "quickly tells what your project can do", while a wiki is for "additional documentation" such as "how to use it, how you designed it, or its core principles".

The interesting fact for a Git learner is in the documentation of editing: "Wikis are part of Git repositories, so you can make changes locally and push them to your repository using a Git workflow." A wiki is **a second Git repository**, with its own history, that lives beside the code repository. Its address is the repository's address with `.wiki` before `.git`. The documentation gives the pattern `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.wiki.git`, and says it can be cloned once an initial page exists.

To see this without a platform, the recording below uses a local bare repository as the wiki, in the same way that Chapter 23<!--ref:remotes--> used one as a remote:

```text
$ git clone -q bakery-menu.wiki.git bakery-wiki
$ cd bakery-wiki
$ ls
Home.md
$ git log --oneline
3ecec76 (HEAD -> main, origin/main, origin/HEAD) Create the Home page
$ printf '# Recipes\n\nHow we bake the white loaf.\n' > Recipes.md
$ git add Recipes.md
$ git commit -q -m "Add the Recipes page"
$ git push -q origin main
$ git log --oneline
34279fc (HEAD -> main, origin/main, origin/HEAD) Add the Recipes page
3ecec76 Create the Home page
$ git -C ../bakery-menu.wiki.git log --oneline main
34279fc (HEAD -> main) Add the Recipes page
3ecec76 Create the Home page
```

*Recorded in Bash; `ch43-settings/expected-wiki.bash.txt`.*

The page `Home.md` came with the clone. A new page `Recipes.md` was added with an ordinary `git add`, `git commit` and `git push`, and the wiki repository's own log shows both commits. Nothing about the code repository changed: the two histories are separate.

> **Checked against GitHub's documentation (R252).** Points from the wiki pages: every repository has a wiki section; it can be edited on GitHub or locally; "only changes pushed to the default branch will be made live" (branches are allowed); by default only people with write access can edit, though everyone can be allowed in a public repository; a wiki in a public repository is public and one in a private repository is visible only to people with access; "search engines will only index wikis with 500 or more stars that you configure to prevent public editing"; and wikis have "a soft limit of 5,000 total files", beyond which GitHub recommends GitHub Pages. The recorded commands show only the Git side, with a local stand-in for the platform.

**A wiki or a `docs` folder?** A wiki has its own history and permissions, so people without write access to the code can be allowed to improve it, and its changes are not reviewed by pull request. A `docs` folder in the code repository is reviewed like code and versioned with it. Choose on that trade-off. (This is the book's advice, not a rule of the platform.)

---

## 43.5 Deployments and environments

If a repository deploys anything (Chapter 58<!--ref:wfadvanced-->), the platform keeps a **Deployments** page. GitHub's documentation says it shows currently active deployments in each environment, the full history, the commit that triggered each deployment, the connected workflow logs, the deployment address if one exists, and the pull request and branch behind it. You open it from the right-hand sidebar of the repository's front page.

> **Checked against GitHub's documentation (R253).** "Viewing your repository's deployment history" lists what the page shows, and says administrators can pin up to ten environments. Environments on the Free plan can only be configured for public repositories; "organizations with Team and users with Pro can configure environments for private repositories". Creating environments and their rules is Chapter 58<!--ref:wfadvanced-->'s subject.

---

## Checkpoint

## What You Learned

- What a repository shows depends on visibility, role, plan and settings.
- Settings changes such as visibility, transfer and deletion happen on the platform and are not recorded in Git; deletion may be restorable for 90 days, but not always.
- The name of the security tab can differ between accounts.
- A wiki is a separate Git repository (`<repository>.wiki.git`); only changes pushed to its default branch go live.
- The Deployments page shows the history of deployments to environments.

## New Vocabulary

**Wiki** (introduced above).

## Commands Learned

`git clone <wiki address>`, `git push` (to a wiki, exactly as to any remote).

## Common Mistakes

1. **Changing visibility without reading the consequences.**
2. **Deleting a repository before checking that a clone holds the history.**
3. **Assuming a missing tab is an error.**
4. **Putting private notes in a public repository's wiki.**
5. **Expecting the code repository's history to show settings changes.**

## Practice

Do the exercises in [`exercises/ch43-exercises.md`](../../../exercises/ch43-exercises.md).

## Self-Test

1. Name four things that decide which tabs you see.
2. Why is a wiki "a second Git repository"?
3. What is the risk of switching a repository from public to private, and of deleting it?
4. Why might two people see different names for the security tab?

## Before Moving On

You are ready for Chapter 44<!--ref:issues--> if you can:

- [ ] say what settings changes Git does not record
- [ ] clone and push to a wiki-style repository
- [ ] explain why a missing tab is not necessarily a mistake

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Clone, edit and push to a wiki-style local repository; separate histories | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R252 (Git side) |
| Settings consequences, deletion, transfer, features | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R250 |
| Security tab label depends on a flag | Checked in the documentation source | R251 |
| Wiki rules and limits | Checked against `github/docs` | R252 |
| Deployments page, environments by plan | Checked against `github/docs` | R253 |

## Where this leads

Chapter 44<!--ref:issues--> covers the first collaboration feature in depth. Chapter 62<!--ref:ghsec--> returns to the security features, and Chapter 58<!--ref:wfadvanced--> to environments and deployments.
