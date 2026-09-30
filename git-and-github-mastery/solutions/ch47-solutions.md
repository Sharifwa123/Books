# Chapter 47 solutions

## Level 1
**1.1** Table: which items are unassigned? Board: what is in progress? Roadmap: what is planned for next month?

**1.2** Date (target ship date), number (complexity), single select (priority), text (a note), iteration (a weekly block).

## Level 2
**2.1** (a) `label:bug status:"In progress"`; (b) `label:bug,support`; (c) `assignee:@me last-updated:5days` (with a status if wanted).

**2.2** `no:label no:assignee repo:octocat/game`.

## Level 3
**3.1** Answers vary. For example statuses Todo, In progress, Done; fields Priority (single select) and Target date; views: Backlog (table, `status:todo`), Board (board, no filter), Roadmap (roadmap, grouped by iteration).

## Level 4
**4.1** The public can see the project, its fields, README and status updates. Items from private repositories appear hidden to people without access to those repositories. Avoid secrets, private customer names and unannounced details in titles, fields and updates.

## Level 5
**5.1** When you filter a view and add an item, the filtered metadata is applied to the new item.

**5.2** The built-in workflow that sets Done when an issue or pull request is closed; check that it is enabled.
