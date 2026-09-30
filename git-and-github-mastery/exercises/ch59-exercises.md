# Chapter 59 exercises — Self-Hosted Runners, Concurrency and Limits

Attempt each exercise before you open `solutions/ch59-solutions.md`. These exercises are on paper, with shell arithmetic on your computer.

## Level 1 — Guided

**1.1 Two kinds.** List two differences between a GitHub-hosted runner and a self-hosted runner.

**1.2 A matrix size.** With shell arithmetic, compute the number of jobs of a matrix with 3 versions, 3 systems and 2 architectures. Is it within the documented limit?

## Level 2 — Partially guided

**2.1 Over the limit.** How many values of a fourth variable would make that matrix exceed 256 jobs?

**2.2 Write a block.** Write a `concurrency` block whose group is the workflow name plus the branch, and that cancels in-progress runs.

## Level 3 — Independent

**3.1 A deployment.** Explain why `cancel-in-progress: true` may be wrong for a production deployment, and what you would set instead.

**3.2 A risk list.** List four risks of a self-hosted runner on a machine that also holds your SSH keys.

## Level 4 — Professional scenario

**4.1 A request.** A colleague wants a self-hosted runner for a public open-source repository "to save minutes". Write a reply from this chapter: what the documentation says, and one alternative.

## Level 5 — Troubleshooting

**5.1** A run was cancelled and nobody cancelled it. Give two possible reasons from this chapter.

**5.2** A workflow file grew until runs stopped starting. Which limit, and what does the documentation suggest?
