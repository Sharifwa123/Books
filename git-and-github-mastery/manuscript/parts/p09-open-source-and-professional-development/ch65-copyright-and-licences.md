---
key: licences
number: 65
tag: Core
first_read: part
status: draft
requires: [oss]
ledger: [R317, R318, R319, R320]
---
# Chapter 65 — Copyright and Licences [Core]

**In this chapter**

- copyright and a licence: two different things
- why public code is not automatically reusable
- the common software licences, compared by their conditions
- Creative Commons licences for text
- how to state a licence in a repository

> **This book is not legal advice.** It explains how licences are described and what their texts say. Copyright law differs between countries, and a licence's effect on a particular situation is a legal question that this book does not answer. If a decision matters (a company, a product, a dispute), ask a qualified person.
>
> **How this chapter was checked.** GitHub statements come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026). Licence summaries come from the *choosealicense.com* data maintained by GitHub and from the SPDX licence list, version 3.29.0, both read from their public repositories. The Creative Commons wording is from the SPDX copy of the legal code. **The official licence pages (gnu.org, apache.org, mozilla.org, opensource.org, creativecommons.org) could not be read from the test computer**, so the summaries are secondary sources and are marked so. Nothing here was run on a live account.

**Before you start.** Chapter 64<!--ref:oss-->.

---

## 65.1 Two different things

**Copyright** is a legal right that a creator has over a creative work, such as a program or a book, so that others may not copy or change it without permission. **A licence** is the permission: a document in which the rights holder says what others *may* do, under which conditions.

GitHub's documentation puts the consequence plainly: "You're under no obligation to choose a license. However, without a license, the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work."

So a repository with no licence file is **not** free to reuse. It is only visible.

**What GitHub itself allows.** The same page adds a note: if you publish source code in a public repository, "according to the Terms of Service, other users of GitHub have the right to view and fork your repository." That is permission to view and fork **on GitHub**. It says nothing about copying the code into your own product.

> **Checked against GitHub's documentation (R317).** "Licensing a repository" and "Adding a license to a repository".

---

## 65.2 The seven distinctions

Chapter 64<!--ref:oss--> said that seeing is not permission. Keep these apart every time you read a project:

1. **Ownership**: who owns the work?
2. **Reading**: may I read it?
3. **Downloading**: may I download a copy?
4. **Redistribution**: may I pass it on to others?
5. **Modification**: may I change it?
6. **Commercial use**: may I use it to make money?
7. **Code reuse**: may I put its code into my own project, and who owns my project afterwards?

Each answer is separate: being allowed to read says nothing about copying, and being allowed to copy says nothing about selling. A licence answers these questions in writing. If the answer is not written anywhere, do not assume "yes".

---

## 65.3 The common software licences

The licences below are described from the *choosealicense.com* data (secondary source), which lists for each licence its **permissions**, **conditions** and **limitations**. All of them permit commercial use, modification, distribution and private use; they differ in their conditions. SPDX gives each an identifier.

| Licence | SPDX identifier | Kind | Conditions listed |
|---|---|---|---|
| MIT License | `MIT` | permissive | include the copyright and licence notice |
| BSD 2-Clause "Simplified" | `BSD-2-Clause` | permissive | include the copyright and licence notice |
| BSD 3-Clause "New" or "Revised" | `BSD-3-Clause` | permissive | as BSD 2-Clause, plus no use of the holder's name to promote derived products without permission |
| Apache License 2.0 | `Apache-2.0` | permissive | include notices; document changes |
| Mozilla Public License 2.0 | `MPL-2.0` | weak copyleft | make source of the licensed **files** and changes to them available under the same licence; keep notices |
| GNU Lesser General Public License v3.0 | `LGPL-3.0-only` | copyleft (library) | source of the licensed work and modifications under the same licence or the GNU GPLv3; keep notices; document changes |
| GNU General Public License v3.0 | `GPL-3.0-only` | strong copyleft | complete source of the work and modifications, **including larger works that use it**, under the same licence; keep notices; document changes |

Three ideas help to read the table:

- **Permissive** licences ask little: keep the notice. Code under them can end up inside closed products.
- **Copyleft** licences require that what you build from the code is shared under the same licence when you distribute it. "Strong" reaches the larger work; "weak" reaches only the licensed files.
- **Patents.** The choosealicense data lists `patent-use` among the permissions of Apache-2.0, MPL-2.0, LGPL-3.0 and GPL-3.0, and does not list it for MIT and BSD. What that means in law is a question for a lawyer.

All these licences also list **limitations**: they give the software "as is", with no **warranty**, and no **liability** for the author.

**A detail about names.** SPDX's list marks the identifier `GPL-3.0` as *deprecated*; the current identifiers are `GPL-3.0-only` and `GPL-3.0-or-later`. Use the current one.

**What a licence file looks like.** GitHub's documentation: "Most people place their license text in a file named `LICENSE.txt` (or `LICENSE.md` or `LICENSE.rst`) in the root of the repository." A detectable licence is shown at the top of the repository page, and "As a best practice, we encourage you to include the license file with your project." The MIT licence's own instructions (from choosealicense) say to replace the year and the name with those of the copyright holders: **use your own name**, and copy the text from an official source, never from memory.

> **Checked against sources (R318, R319).** choosealicense.com data (GitHub-maintained; a secondary source) and the SPDX licence list 3.29.0 (identifiers, deprecation). **Not established:** the exact wording of each official licence page, and how any of them applies to your situation.

---

## 65.4 Creative Commons: licences for text and pictures

Software licences are written for code. For books, articles, pictures and teaching materials, **Creative Commons** offers a family of licences built from four **elements**. The SPDX copy of the legal code states: "License Elements means the license attributes listed in the name of a Creative Commons Public License". The elements you will see:

| Element | Short | Meaning in one line |
|---|---|---|
| Attribution | BY | credit the creator as the licence says |
| ShareAlike | SA | share adaptations under the same (or a compatible) licence |
| NonCommercial | NC | no use "primarily intended for or directed towards commercial advantage or monetary compensation" |
| NoDerivatives | ND | no adapted versions (not covered in the text read for this chapter) |

The SPDX identifiers are, for example, `CC-BY-4.0`, `CC-BY-SA-4.0`, `CC-BY-NC-SA-4.0` and `CC0-1.0` (the last one is a dedication with no conditions). The definition of NonCommercial quoted above is from the legal code, which adds that exchanging material "by digital file-sharing or similar means is NonCommercial provided there is no payment of monetary compensation in connection with the exchange." How that applies to *your* use is a legal question.

Two cautions from the sources:

- The list of licences GitHub can detect includes the Creative Commons family, and the SPDX list does not mark the Creative Commons licences as approved by the Open Source Initiative. Whether a NonCommercial licence counts as "open source" depends on the definition used, and Chapter 64<!--ref:oss-->'s three-way split (public, source-available, open source) shows why the words matter.
- Creative Commons is said to advise against using its licences for software (the source read for this chapter is only the choosealicense summary, so treat this as unconfirmed). Use a software licence for code and a Creative Commons licence for text.

**This book's own licence.** A book has text and code samples, which may need different licences. **That decision has not been made in this draft**, and the book carries no licence statement until it is. Nobody may assume one from this chapter.

> **Checked against sources (R320).** SPDX's copy of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International legal code (definitions of License Elements and NonCommercial; ShareAlike condition), and the SPDX list. The official Creative Commons pages were not readable.

---

## 65.5 Using other people's code and text

A checklist for someone who wants to reuse something:

1. **Find the licence** (a `LICENSE` file, the README, the repository page).
2. **No licence? Ask** the owner. Do not copy.
3. **Read the conditions** in the table above and in the file itself.
4. **Comply**: keep the required notices; if the licence is copyleft, understand what you must share.
5. **Record** where the code came from and under what licence, in your repository (a `NOTICE` or `THIRD-PARTY` file is a common habit, not a requirement).
6. **Check compatibility** if you combine code under different licences: some combinations are not allowed. This is a legal question; ask.
7. **Do not remove** copyright notices.

A checklist for someone who wants to **share** their own work:

1. Decide what you want others to be able to do, and what you must have the right to license (work made for an employer, or with contributors, may not be yours alone; Chapter 64<!--ref:oss--> on sign-off).
2. Choose a licence from a maintained list, using current official texts.
3. Add the licence file at the root, and state the licence in the README.
4. Ask contributors to agree that their contributions come under the same terms; many projects say so in `CONTRIBUTING.md`.

---

## Checkpoint

## What You Learned

- Copyright gives the creator rights; a licence is the written permission. Without a licence, all rights are reserved.
- Public and viewable is not reusable; GitHub's terms allow viewing and forking on GitHub only.
- Permissive licences ask little; copyleft licences require sharing under the same licence; strong and weak copyleft differ in reach.
- SPDX identifiers name licences; prefer the current identifiers.
- Creative Commons licences suit text; they are built from elements such as BY, SA and NC.
- This book is not legal advice, and its own licence is not yet decided.

## New Vocabulary

**Copyright**, **licence**, **permissive licence**, **copyleft**, **SPDX identifier**, **Creative Commons** (see the glossary).

## Commands Learned

No new commands.

## Common Mistakes

1. **Treating a public repository as free to reuse.**
2. **Copying a licence text from memory or from a random site.**
3. **Putting someone else's name (or none) in the copyright line.**
4. **Using a text licence for software or the reverse.**
5. **Assuming NonCommercial is obvious.**

## Practice

Do the exercises in [`exercises/ch65-exercises.md`](../../../exercises/ch65-exercises.md).

## Self-Test

1. What is the difference between copyright and a licence?
2. What does GitHub's documentation say applies when a repository has no licence?
3. Name one permissive and one copyleft licence and one difference in their conditions.
4. What does the `SA` element mean?
5. Why is this chapter not legal advice?

## Before Moving On

You are ready for Chapter 66<!--ref:releases--> if you can:

- [ ] explain why a public repository may not be reused
- [ ] find a project's licence
- [ ] tell permissive from copyleft

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| No licence means default copyright applies; GitHub's terms allow view and fork; licence file placement | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R317 |
| Permissions, conditions and limitations of the listed licences | Secondary source: choosealicense.com data (GitHub-maintained); official texts not read | R318 |
| SPDX identifiers and the deprecation of `GPL-3.0` | SPDX licence list 3.29.0, fetched from its public repository | R319 |
| Creative Commons elements, NonCommercial and ShareAlike wording | SPDX copy of the CC BY-NC-SA 4.0 legal code; official pages not read | R320 |
| Whether Creative Commons advises against software use | Unconfirmed (secondary source only) | R099 |

## Where this leads

Chapter 66<!--ref:releases--> turns a state of the project into a named, downloadable version.
