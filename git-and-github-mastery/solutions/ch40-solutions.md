# Chapter 40 solutions

## Level 1
**1.1** It corresponds to the "history" of a single file on the page.

**1.2** No. The archive contains only the files of the commit, under the folder name given by `--prefix`.

## Level 2
**2.1** The comparison (compare) view.

**2.2** A release page presents a specific point in history, and a tag is the fixed name for a point in history; the platform builds the page on top of the tag (details in Chapter 66<!--ref:releases-->).

## Level 3
**3.1** Files: `git ls-tree HEAD`; branches: `git branch --all`; tags: `git tag`; history: `git log`; compare: `git diff <a> <b>`; blame: `git blame <file>`; download: `git archive`; clone address: `git remote -v` or `git config --get remote.origin.url`.

**3.2** In a clone: commits, branches, tags, `.gitignore`, workflow files (they are files in the repository). Not in a clone: issues, pull requests, the wiki (kept separately by the platform).

## Level 4
**4.1** Answers vary. The point is to name, for each item, the Git command from section 40.2, and to record differences between the real page and this chapter.

## Level 5
**5.1** The archive is a snapshot of the files without the `.git` folder, so it is not a repository. Clone the repository to get the history.

**5.2** The interface has probably changed, or the tutorial is old. Look for the idea (for example, the word or icon for "history"), check the tutorial's date, and consult the platform's current documentation.

**5.3** The feature may be switched off for that repository, the colleague's role or plan may not include it, or the repository may not use it. It is not necessarily deleted.
