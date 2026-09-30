---
key: projects
number: 47
tag: Deep
first_read: later
status: draft
requires: [issues, pr]
ledger: [R266, R267]
---
# Chapter 47 — GitHub Projects [Deep]

**In this chapter**

- what a project is and how it differs from an issue list
- the three layouts: table, board and roadmap
- fields, including iterations
- filters, and how they combine
- built-in automation, and who can see a project

> **How to read this chapter.** This is a **Deep** chapter about a service, so it has **no recorded commands** and can be read later. Everything is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026); no live account was used. Names of buttons and menu items are the documentation's and can change. A project is a platform feature and is **not in your Git repository**.

**Before you start.** Chapter 44<!--ref:issues--> and Chapter 45<!--ref:pr-->.

---

## 47.1 What a project is

> **New term: project.** On GitHub, an adaptable table, board or roadmap built from your issues and pull requests, used to plan and track work across one or many repositories.

GitHub's documentation defines it as "an adaptable table, board, and roadmap that integrates with your issues and pull requests on GitHub to help you plan and track your work effectively at the user or organization level". Items come from issues and pull requests, and information "is synced automatically ... This integration works both ways": if you change an assignee in the project, the issue shows the change too.

Compare with the issue list of one repository (Chapter 44<!--ref:issues-->): an issue list is *one repository's* backlog with labels and milestones; a project can gather items from *several* repositories, add **custom fields**, and show the same items in several **views**.

> **Checked against GitHub's documentation (R266).** "About Projects" for the definition and the two-way sync above. A project can also hold **draft issues** (items that are not yet issues), which can be converted to issues later.

---

## 47.2 Three layouts

| Layout | What it looks like | Good for |
|---|---|---|
| **Table** | A high-density spreadsheet-style list; fields are columns | Sorting, grouping and editing many items at once |
| **Board** | Columns of cards (a kanban board), for example by status | Seeing the flow of work: Todo, In progress, Done |
| **Roadmap** | A timeline of items on dates or iterations | Planning releases and seeing what is scheduled when |

The documentation says you can "view your project as a high-density table layout, as a kanban board, or a timeline-style roadmap", and that you can save views and share them with your team. Each view can filter, sort, slice and group.

---

## 47.3 Fields

Beyond the built-in data of an issue (assignee, milestone, labels), a project can hold **custom fields**. The documentation lists examples:

- a **date** field for target ship dates;
- a **number** field for the complexity of a task;
- a **single select** field for priority (Low, Medium, High);
- a **text** field for a quick note;
- an **iteration** field to plan work "week-by-week, including support for breaks".

A project can have "up to 50 fields", including the built-in ones.

> **New term: iteration.** A block of time, such as a week or two weeks, in which a team plans to finish a set of items. In GitHub Projects an iteration is a kind of field, so items can be grouped and filtered by iteration.

Iterations "can be set to any length of time, can include breaks, and can be individually edited". You can filter by name, or by `@current`, `@previous` and `@next`. When you first create an iteration field, three iterations are created automatically.

---

## 47.4 Filters

You narrow a view with **filters**. The documentation gives these forms:

| You type | You get |
|---|---|
| `assignee:octocat` | items assigned to that person |
| `label:bug` | items with the `bug` label |
| `status:done` | items whose Status field is Done |
| `label:bug status:"In progress"` | items matching **both** (filters combine with AND) |
| `label:bug,support` | items with **either** label (commas mean OR *within one field*) |
| `assignee:octocat assignee:stevecat` | items assigned to **both** people |
| `assignee:@me status:todo last-updated:5days` | your Todo items not updated in five days |
| `no:label no:assignee repo:octocat/game` | a triage view: items with no label and no assignee |

When you filter a view and then add an item, "the filtered metadata will be applied to new item". If you filter by `status:"In progress"` and add an item, the new item has that status.

> **Checked against GitHub's documentation (R267).** The qualifiers, the AND and OR rules, the `no:` filter and the behaviour of new items are from "Filtering projects"; the iteration filters are from "About iteration fields".

---

## 47.5 Automation

The documentation says projects include **built-in workflows** that update the **Status** of items on events: for example set Todo when an item is added, close issues when their status changes, or set Done when an issue is closed. Two are on by default: items are set to **Done** when their issue or pull request is closed, and when their pull request is merged. You can also automatically **archive** items that meet criteria, automatically **add** items from a repository that match a filter, and use the API and GitHub Actions for more control (Chapter 54<!--ref:actions-->).

---

## 47.6 Who can see a project

A project's visibility is separate from its items. GitHub's documentation: public projects can be viewed by "everyone on the internet"; private projects only by users "granted at least read access". **Only the project's visibility is affected**: to see an item, someone must still have access to the repository it belongs to, and items from a private repository appear as hidden to people without access. Project admins and organization owners control visibility.

> **⚠️ CAUTION.** Do not put secrets or private details in a project's title, README, status updates or custom fields of a public project: everything in it is visible to the world, even if your repositories are private.

---

## 47.7 Habits that keep a project useful

The documentation's best practices, in short: use @mentions, assignees and links to communicate; break large issues into smaller ones (sub-issues), which "leads to smaller pull requests, which are easier to review"; use the project description and README, and post status updates ("On track", "At risk"); and create views for different questions (filter by status, group by priority, sort by date, slice by assignee). A project nobody updates is worse than none, so give it an owner.

---

## Checkpoint

## What You Learned

- A project is a table, board or roadmap over issues and pull requests, synced both ways.
- Custom fields (date, number, single select, text, iteration) add metadata.
- Filters combine with AND; commas mean OR within one field.
- Built-in workflows update Status; two are on by default.
- Project visibility is separate from repository access.

## New Vocabulary

**Project**, **iteration** (introduced above).

## Commands Learned

None: this chapter is about the platform and not about Git.

## Common Mistakes

1. **Using a project as a second place to type the same information.**
2. **Too many fields**, so nobody fills them in.
3. **Assuming a public project exposes private repository items.**
4. **Leaving a project without an owner.**

## Practice

Do the exercises in [`exercises/ch47-exercises.md`](../../../exercises/ch47-exercises.md).

## Self-Test

1. Name the three layouts and one use for each.
2. What does `label:bug,support` show?
3. Which two built-in workflows are on by default?
4. Who can see the items from a private repository in a public project?

## Before Moving On

You are ready for Chapter 48<!--ref:discussions--> if you can:

- [ ] choose a layout for a question
- [ ] write a filter that combines conditions
- [ ] say what a project shows and does not show

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Definition, layouts, fields, best practices, visibility, built-in workflows | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R266 |
| Filter syntax and iteration filters | Checked against `github/docs` | R267 |

## Where this leads

Chapter 48<!--ref:discussions--> covers open-ended conversation, and Chapter 54<!--ref:actions--> shows how workflows can act on projects.
