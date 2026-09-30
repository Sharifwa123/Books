# Chapter 28 solutions

## Level 1
**1.1** `git cherry-pick drinks~1` on `main`; the graph shows a new "Add tea" on `main`, and the original still on `drinks`.

**1.2** The copy has a different parent, and a commit's hash includes its parent, so it is a new commit.

## Level 2
**2.1** `main` now has copies of both commits; `drinks` still has the originals. The two are not linked.

**2.2** The file starts with `From <hash>`, the author, the date, and `Subject: [PATCH] Add tea`.

## Level 3
**3.1** `git apply --check` prints nothing when the patch would apply; `git am` creates the commit with the original author and message.

**3.2** Each step checks out a commit halfway through the remaining range. After the last answer, Git names the first bad commit. `git bisect reset` returns to the branch.

## Level 4
**4.1** About three steps for five commits; about ten steps for 1000 (log2(1000) is roughly 10).

## Level 5
**5.1** The commit depended on an earlier commit that was not copied. Cherry-pick only copies the change of the one commit; pick the earlier one first, or use a merge.

**5.2** `git bisect reset`.

**5.3** No. The check found a problem, such as a mismatch with the current files, and applying anyway could fail halfway or change the wrong thing. Fix the cause first.
