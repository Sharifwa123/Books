# Chapter 55 exercises — Expressions, Contexts and Conditionals

Attempt each exercise before you open `solutions/ch55-solutions.md`. Exercises 1 and 2 need only your computer.

## Level 1 — Guided

**1.1 The three values.** In `bakery-menu`, on a branch `feature-tea` with a tag `v1.0`, run the Git commands that give the full ref, the short branch name and the commit SHA of `HEAD`. Which `github` property is each?

**1.2 A tag ref.** Run `git rev-parse --symbolic-full-name v1.0`. What form does a tag ref have?

## Level 2 — Partially guided

**2.1 List all refs.** Run `git for-each-ref --format='%(refname)'`. Which lines would a workflow triggered by pushing a tag see in `github.ref`?

**2.2 Read a condition.** Say in words when this job runs: `if: ${{ github.ref == 'refs/heads/main' }}`. Then say what happens if the condition is written `github.ref == 'main'`.

## Level 3 — Independent

**3.1 Write conditions.** Write an `if` for each: (a) run only when the event is `push`; (b) run a cleanup step whatever the earlier steps did, unless the run was cancelled; (c) run a step only after a previous failure.

**3.2 Types.** Say what `'Main' == 'main'`, `1 == '1'` and `null == 0` evaluate to, according to the loose-equality rules in section 55.1, and check them against the documentation.

## Level 4 — Professional scenario

**4.1 Explain a bug.** A step's output `count` is `'10'`. The condition `steps.x.outputs.count > 9` behaves unexpectedly. Explain from section 55.1 what to do.

## Level 5 — Troubleshooting

**5.1** A step that uses `github.actor_name` prints nothing and the workflow does not fail. Explain.

**5.2** A team put `if: ${{ always() }}` on the step that checks out the code. Why does the documentation warn against this?
