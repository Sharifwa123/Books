# Chapter 72 exercises — Deployment Pipelines

Attempt each exercise before you open `solutions/ch72-solutions.md`. Exercises 2.1 and 2.2 use your terminal only; no server or account is needed.

## Level 1 — Guided

**1.1 Steps.** List the seven steps of the pipeline in section 72.2 in order.

**1.2 Targets.** Match each to a deployment step: static website, container, VPS.

## Level 2 — Partially guided

**2.1 Switch.** Create two release folders and a `current` link. Point the link at the first release, read a file through it, switch to the second and read again.

**2.2 Roll back.** Roll back to the first release and show that both release folders still exist.

## Level 3 — Independent

**3.1 A health check.** Write a shell command that succeeds only if `current/index.txt` exists and contains the word "Bakery". Show it succeeding.

**3.2 Two environments.** Design `staging` and `production` for the Sunrise Bakery site: what deploys automatically, what needs approval, and why the same artifact goes to both.

## Level 4 — Professional scenario

**4.1 Secrets review.** A colleague stores one all-powerful key as a repository secret and prints it in the log "to debug". Write the review using the deployment-secret rules and Chapter 60<!--ref:wfsec-->.

## Level 5 — Troubleshooting

**5.1** The new release is live and broken, and the previous release folder was deleted by a clean-up script. What went wrong in the design, and how would you avoid it?

**5.2** A database change came with the release. Why might a rollback of files not be enough?
