# Appendix H — Professional Repository Checklist

Use this list to review a repository before you share it, or to review someone else's. It combines Chapters 42<!--ref:readme-->, 43<!--ref:settings-->, 64<!--ref:oss-->, 65<!--ref:licences--> and 66<!--ref:releases-->.

## H.1 First impression

- [ ] The repository has a clear name and a one-sentence description.
- [ ] The README says what it is, how to try it, how to get help and how to contribute, and its examples are true (Chapter 42<!--ref:readme-->).
- [ ] Topics or labels help people find it.
- [ ] There is a picture or a short demonstration only if it adds value, with a text alternative.

## H.2 Files

- [ ] `LICENSE` exists and is **a deliberate choice of the owner** (Chapter 65<!--ref:licences-->); the README says which licence applies.
- [ ] `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` (only if you can enforce it) and `SECURITY.md` exist (Chapters 64<!--ref:oss--> and 62<!--ref:ghsec-->).
- [ ] `.gitignore` matches the tools in use; no generated or secret files are tracked (Chapter 18<!--ref:tracking-->).
- [ ] Issue and pull request templates guide reporters (Chapters 44<!--ref:issues--> and 45<!--ref:pr-->).
- [ ] Nothing large or binary is committed without a reason; large files use the right tool (Chapter 31<!--ref:bigrepos-->).

## H.3 History and branches

- [ ] Commit messages explain why, in the imperative, and each commit is one logical change (Chapter 19<!--ref:commits-->).
- [ ] The default branch is protected and every change arrives by pull request (Chapter 50<!--ref:protect-->).
- [ ] Finished branches are deleted; long-lived branches have a reason.

## H.4 Automation

- [ ] A pipeline runs the tests on each pull request, and the same script runs locally (Chapters 52<!--ref:cicd--> and 77<!--ref:capstone-->).
- [ ] Workflows have least-privilege permissions and pinned actions (Chapter 60<!--ref:wfsec-->).
- [ ] Dependency updates are automated and reviewed (Chapter 62<!--ref:ghsec-->).

## H.5 Releases

- [ ] Versions follow a stated scheme (Chapter 66<!--ref:releases-->).
- [ ] Each release is an annotated tag with notes; artifacts have checksums.
- [ ] A hotfix path exists: branch from the tag, fix, new patch version (Chapter 76<!--ref:scenarios-->).

## H.6 People

- [ ] Issues get an answer, even if the answer is "not now".
- [ ] `good first issue` labels are kept honest (Chapter 64<!--ref:oss-->).
- [ ] There are at least two people who can administer the repository or organization (Chapter 68<!--ref:orgs-->).
