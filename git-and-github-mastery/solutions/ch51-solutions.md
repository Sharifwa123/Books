# Chapter 51 solutions

## Level 1
**1.1** Pulse: recent activity summary; Contributors: top 100 contributors; Traffic: views, visitors, clones, referrers; Commits: commits over the past year; Code frequency: additions and deletions per week; Network: branch history including forks.

**1.2** The recording in section 51.3 shows the form of the output.

## Level 2
**2.1** The merge commit is counted by the first command and not by the second.

**2.2** `git shortlog` counts it; `git log --shortstat` shows no changed-lines line for it.

## Level 3
**3.1** Two lines appear until `.mailmap` contains `Ada Learner <ada@example.org> Ada L. <ada@old-mail.example>`; then they merge into one.

**3.2** (a) Traffic (full clones); (b) Contributors or Commits; (c) Network; (d) Pulse (choose the period).

## Level 4
**4.1** The graph counts commits by identity, ignores merge and empty commits, shows only the top 100, and cannot see review, design, documentation or support. Offer instead: review counts, time to first response, or a written summary of each person's work agreed with them.

## Level 5
**5.1** The commits may not be merged into the default branch; the commit email may not match an account (Chapter 37<!--ref:ghaccount-->); or the person is not among the top 100, or is counted under another identity.

**5.2** All data in the traffic graph uses UTC+0, regardless of location, so days are cut at UTC midnight.
