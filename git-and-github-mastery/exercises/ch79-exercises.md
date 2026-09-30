# Chapter 79 exercises — Recovery Playbooks

Attempt each exercise before you open `solutions/ch79-solutions.md`. Work in a sandbox with a local bare repository as the remote. **Only practise history rewriting on a repository that you can throw away.**

## Level 1 — Guided

**1.1 Order.** Put the actions of Playbook 1 in the right order: rewrite history, revoke the key, stop tracking the file, tell colleagues to re-clone.

**1.2 Name the tool.** Which playbook uses the reflog, and what does `HEAD@{1}` mean there?

## Level 2 — Partially guided

**2.1 Playbook 2.** Make two commits, reset hard two commits back, and recover them with the reflog. Show the log before and after.

**2.2 Playbook 5.** Commit on `main` by mistake and move the commit to a new branch without losing it. Show both logs.

## Level 3 — Independent

**3.1 Playbook 3.** Create a merge that you regret, push it, and revert it with `-m 1`. Then try to merge the same branch again. What do you observe? Explain it with the chapter.

**3.2 Playbook 4.** Cause a rebase conflict and abort it. Then cause it again and resolve it with `--continue`. Compare the histories.

## Level 4 — Professional scenario

**4.1 Incident report.** A token was pushed to `main` on Monday and found on Wednesday. Write the incident report: timeline, actions in order, what the rewrite could and could not achieve, what you asked colleagues to do, and prevention.

## Level 5 — Troubleshooting

**5.1** After a history rewrite a colleague pulls and pushes, and the secret reappears. Explain why, and what they should have done.

**5.2** `git reset --hard 'HEAD@{1}'` did not bring your commits back. Give three possible reasons.
