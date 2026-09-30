# Chapter 34 exercises — Git Workflows

Attempt each exercise before you open `solutions/ch34-solutions.md`. Use a bare repository as the shared remote and two clones, `alice` and `bob`, on one computer (Chapter 23<!--ref:remotes-->).

## Level 1 — Guided

**1.1 Start a feature.** As Alice, create `add-tea`, commit a change, and publish the branch with `git push -u origin add-tea`.

**1.2 Look at it.** As Bob, run `git fetch` and `git branch -r`. What is new, and did anything in Bob's own branches change?

## Level 2 — Partially guided

**2.1 Review it.** As Bob, run `git diff main origin/add-tea`. What would you check before you approve?

**2.2 Merge it.** Bob merges with `--no-ff` and pushes `main`. How does the graph show that a branch existed?

## Level 3 — Independent

**3.1 Clean up.** Delete the branch on the remote, then, as Alice, run `git fetch --prune` and `git branch -vv`. What does `[origin/add-tea: gone]` mean?

**3.2 Finish.** As Alice, switch to `main`, pull, and delete the local branch with `git branch -d`. Why did `-d` succeed?

## Level 4 — Professional scenario

**4.1 Write a workflow.** A team of four builds a bakery website, releases every week, and has decent tests. Write the rules of a workflow for them in eight lines or fewer: where work starts, how it is reviewed, how it is merged, how releases are marked.

## Level 5 — Troubleshooting

**5.1** A branch has lived for six weeks. Merging it produces conflicts in twelve files. Explain why, and how the team could avoid it.

**5.2** A team lets everybody commit straight to `main`, and `main` is often broken. Name two changes that would help.

**5.3** A new hire asks: "Do we use Git Flow?" The team has never named its workflow. What would you tell them, and what would you do?
