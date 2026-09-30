# Chapter 43 solutions

## Level 1
**1.1** The stand-in repository `demo.wiki.git` has its own history (the commit that created `Home.md`), and your clone has a copy of it. A real wiki's history is separate from the code repository's.

**1.2** Visibility, your role, the plan, and the settings of the repository and its organisation.

## Level 2
**2.1** The pull brings the commit that added `Recipes.md`; it is an ordinary fetch and merge.

**2.2** No: the documentation says only changes pushed to the wiki's default branch are made live.

## Level 3
**3.1** For example: outside readers benefit from a wiki that people without write access can be allowed to edit; but changes to a `docs` folder are reviewed by pull request and versioned with the code. Any two sound reasons from the trade-off are accepted.

**3.2** For example: confirm a clone has all branches and tags; export what is not in Git (issues, wiki); tell the collaborators; check for forks that will be deleted; confirm you can restore within 90 days if needed.

## Level 4
**4.1** Check for secrets in the whole history (Chapter 33<!--ref:gitsec-->); know that Actions history and logs become visible to everyone; know that private forks are detached; then remove or rotate any secret before the change.

## Level 5
**5.1** The documentation source names the tab "Security and quality" or "Security" depending on a feature flag. It is not a problem: it is the same tab.

**5.2** Some deleted repositories can be restored within 90 days. A repository that was part of a fork network that is not empty cannot be restored unless every other repository in the network is deleted or detached.
