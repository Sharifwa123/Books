# Chapter 51 exercises — Insights

Attempt each exercise before you open `solutions/ch51-solutions.md`. Exercises 1 to 3 need only your computer.

## Level 1 — Guided

**1.1 Six graphs.** Name the six graphs in the table of section 51.2 and say in one line what each shows.

**1.2 Count.** In `bakery-menu`, run `git rev-list --count HEAD` and `git shortlog -sne HEAD`.

## Level 2 — Partially guided

**2.1 Without merges.** Make a topic branch, merge it with `--no-ff`, and compare `git shortlog -sne HEAD` with `git shortlog -sne --no-merges HEAD`. What changed?

**2.2 An empty commit.** Add an empty commit with `git commit --allow-empty -m "..."`. Does `git shortlog` count it? Does `git log --shortstat` show changed lines for it?

## Level 3 — Independent

**3.1 Two identities.** Make one commit with `-c user.name="Ada L." -c user.email="ada@old-mail.example"`. Show that `shortlog -sne` lists two people. Then create a `.mailmap` that joins them and run it again.

**3.2 Which graph?** Choose the graph that best answers each question: (a) are people cloning the repository? (b) who committed most last year? (c) which branches exist in the forks? (d) what happened last week?

## Level 4 — Professional scenario

**4.1 A report.** A manager asks you to rank the team by the contributors graph. Write a short reply that explains, from this chapter, why you will not, and what you can offer instead.

## Level 5 — Troubleshooting

**5.1** A contributor's commits are missing from the contributors graph, although they merged pull requests. Give two possible reasons from this chapter and Chapter 37<!--ref:ghaccount-->.

**5.2** The traffic graph shows a visit on a day when nobody visited in the reader's local time. Explain.
