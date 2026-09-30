---
key: releases
number: 66
tag: Core
first_read: part
status: draft
requires: [tags, ghrepo]
ledger: [R321, R322, R323]
---
# Chapter 66 — Releases [Core]

**In this chapter**

- what a release is, and how it differs from a tag
- version numbers and Semantic Versioning
- release notes, by hand and generated
- source archives and attached files
- automating a release

> **How to read this chapter.** GitHub statements come from GitHub's documentation (`github/docs` at commit `2eaab0b`, 29 September 2026); they were **not run on a live account**. The Git side (tags, sorting, notes from history, source archives) and the structure of the release-notes configuration file were recorded on Git 2.43.0 in Bash and zsh, and re-run in CI on newer Git. The rules of Semantic Versioning are from its specification, read from its public repository.

**Before you start.** Chapter 29<!--ref:tags--> (tags) and Chapter 39<!--ref:ghrepo--> (repositories on GitHub).

---

## 66.1 A tag is a name; a release is an announcement

Chapter 29<!--ref:tags--> taught that a tag names one commit. GitHub's documentation: "Releases are deployable software iterations you can package and make available for a wider audience to download and use. Releases are based on Git tags, which mark a specific point in your repository's history. A tag date may be different than a release date since they can be created at different times."

So a **release** is a page on GitHub built around a tag, with a title, notes and downloadable files. Anyone with read access can view and compare releases, but "only people with write permissions to a repository can manage releases". Releases do **not** exist in Git itself: a plain `git clone` gets the tags but not the release page, the notes or the attached files (Chapter 36<!--ref:whatgh-->).

GitHub automatically provides "links to download a zip file and a tarball containing the contents of the repository at the point of the tag's creation". Your own files (a compiled program, a package) can be attached to a release; the documentation gives limits on the number and size of such **assets**, which change, so read them when you need them.

> **Checked against GitHub's documentation (R321).** "About releases" and "Managing releases in a repository".

---

## 66.2 Version numbers

A release needs a name people can compare. The most common scheme is **Semantic Versioning**. Its specification (version 2.0.0) says: "Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes".

It adds that "Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version", and that "Major version zero (0.y.z) is for initial development. Anything MAY change at any time."

Semantic Versioning is about a **public API**, the promises your project makes to the people using it. For a program with no API, or for a book, projects choose other schemes (dates, for example); no scheme is required. Whatever you choose, **write it down and keep to it**.

A Git habit that goes with it: name the tag `v` plus the version (`v1.2.0`). The recording below made four tags. Notice that plain `git tag` lists them alphabetically, which puts `v1.10.0` before `v1.2.0`; the sort option `version:refname` compares the numbers the way a person does:

```text
$ git init -q proj && cd proj
$ printf 'app\n' > app.txt && git add app.txt && git commit -q -m "First working version"
$ git tag -a v1.0.0 -m "Version 1.0.0"
$ printf 'fix\n' >> app.txt && git commit -q -am "Fix crash on empty input"
$ git tag -a v1.0.1 -m "Version 1.0.1"
$ printf 'search\n' >> app.txt && git commit -q -am "Add search"
$ git tag -a v1.2.0 -m "Version 1.2.0"
$ printf 'export\n' >> app.txt && git commit -q -am "Add export"
$ git tag -a v1.10.0 -m "Version 1.10.0"
$ git tag
v1.0.0
v1.0.1
v1.10.0
v1.2.0
$ git tag --sort=-version:refname
v1.10.0
v1.2.0
v1.0.1
v1.0.0
```

*Recorded in Bash; `ch66-releases/expected-relnotes.bash.txt`.*

The `-a` made **annotated** tags (Chapter 29<!--ref:tags-->), which carry a message and are the natural choice for releases.

---

## 66.3 Release notes

Release notes tell users what changed. Two sources:

- **By hand.** Write a description when you create the release. If you @mention people in it, "the published release will include a **Contributors** section with an avatar list of all the mentioned users".
- **Generated.** "Automatically generated release notes include a list of merged pull requests, a list of contributors to the release, and a link to a full changelog." You can click **Generate release notes** while creating a release, and you can customise the result with a file `.github/release.yml` in which you "specify in YAML the pull request labels and authors you want to exclude" and can "create new categories and list the pull request labels to be included in each of them". The documented options include `changelog.exclude.labels`, `changelog.exclude.authors` and, per category, a required `title` and required `labels`, where `*` is "a catch-all for pull requests that didn't match any of the previous categories".

Git alone can give a rough draft, from the history between two tags:

```text
$ git log --format='- %s' v1.0.1..v1.10.0
- Add export
- Add search
```

*Recorded in Bash; `ch66-releases/expected-relnotes.bash.txt`.*

That is the raw material: the subjects of the commits since the last release. It is only as good as your commit messages (Chapter 19<!--ref:commits-->).

A minimal configuration file, written and read back with PyYAML (Chapter 53<!--ref:yaml-->):

```text
$ mkdir -p .github
$ printf 'changelog:\n  exclude:\n    labels:\n      - ignore-for-release\n  categories:\n    - title: Breaking changes\n      labels:\n        - breaking-change\n    - title: Other changes\n      labels:\n        - "*"\n' > .github/release.yml
$ python3 ../rel.py .github/release.yml
excluded labels: ['ignore-for-release']
Breaking changes <- ['breaking-change']
Other changes <- ['*']
```

*Recorded in Bash; `ch66-releases/expected-relnotes.bash.txt`.*

The script only checks that the structure matches the option names in the documentation; it does **not** show what GitHub would generate.

> **Checked against GitHub's documentation (R322).** "Automatically generated release notes" (option names and behaviour). The recording checks the file's structure only.

---

## 66.4 Source archives

The zip and tarball that GitHub adds to a release are **source archives**: the files of the tagged commit, without the `.git` folder. Git can make the same kind of archive locally (Chapter 30<!--ref:objects--> listed the files of an archive):

```text
$ git describe --tags
v1.10.0
$ git archive --format=tar --prefix=proj-1.10.0/ v1.10.0 | tar -t
proj-1.10.0/
proj-1.10.0/app.txt
$ git archive --format=tar.gz -o ../proj-1.10.0.tar.gz v1.10.0 && gzip -t ../proj-1.10.0.tar.gz && echo "archive ok"
archive ok
```

*Recorded in Bash; `ch66-releases/expected-relnotes.bash.txt`.*

`git describe --tags` names the current commit by the nearest tag, here exactly `v1.10.0`. The archive listing shows the files under a folder that carries the project and version (`--prefix`), which is a common habit so that unpacking does not scatter files. The `gzip -t` test only checks that the compressed file is not damaged.

Whether the archives that GitHub makes include Git LFS files is an option that administrators can choose, according to the documentation. What is **not** in a source archive: the history, and any files you attach separately.

Chapter 63<!--ref:secpractice--> covered checksums for what you publish. For anything people will run, publish a checksum, and consider attestations.

---

## 66.5 A release checklist

1. **Everything you want is merged** into the default branch, and CI is green (Chapter 52<!--ref:cicd-->).
2. **Choose the version** by your scheme.
3. **Create the tag** on the right commit (Chapter 29<!--ref:tags-->). A tag on the wrong commit is a release of the wrong code.
4. **Write the notes**: by hand, generated or both. Mention breaking changes first.
5. **Attach your files** and publish a checksum for each.
6. **Mark pre-releases** as such when they are not final. The GitHub command-line tool (Chapter 73<!--ref:ghcli-->) can do this: the documentation's example is `gh release create v1.3.2 --title "v1.3.2 (beta)" --notes "..." --prerelease`.
7. **Check the result** as a user would: download and try it.
8. **If it fixes a security problem**, publish a security advisory as well (Chapter 62<!--ref:ghsec-->); the documentation recommends it.

**Editing and immutability.** You can edit a release later. The documentation describes an option, **immutable releases**: if enabled, you "cannot add, replace, or delete assets after a release is published", and you "cannot move or delete its tag while the release exists"; titles and notes can still be edited. It recommends creating releases as **drafts** first, attaching all files, and then publishing. Semantic Versioning says the same in spirit: a released version must not change.

---

## 66.6 Automating releases

A workflow (Chapter 54<!--ref:actions-->) can create a release when a tag is pushed: the trigger is a push of a tag, and a step calls the GitHub command-line tool or the API. The Releases API also exists for scripts. Two cautions:

- The workflow needs permission to write releases, so give it exactly that and no more (Chapter 60<!--ref:wfsec-->). The precise permission name was **not** checked for this chapter; look it up in the current documentation.
- Automation makes mistakes fast: a wrong tag becomes a wrong public release in seconds. Keep a human check, such as a draft release that a person publishes.

Chapter 67<!--ref:ossproject--> puts the whole lifecycle together in a project of your own.

---

## Checkpoint

## What You Learned

- A release is a GitHub page built on a tag; Git itself has tags, not releases.
- Semantic Versioning: MAJOR for incompatible changes, MINOR for compatible features, PATCH for compatible fixes; a released version does not change.
- `git tag --sort=version:refname` sorts versions correctly.
- Release notes can be written by hand or generated, and configured by `.github/release.yml`.
- Source archives contain the files of a tag without history; `git archive` makes one locally.
- Publish checksums for what people run; consider immutable releases and drafts.

## New Vocabulary

**Release**, **release notes**, **Semantic Versioning**, **asset**, **source archive**, **pre-release** (see the glossary).

## Commands Learned

`git tag --sort=version:refname`, `git describe --tags`, `git archive --prefix`, `git log --format=... tagA..tagB`.

## Common Mistakes

1. **Tagging the wrong commit.**
2. **Changing a published release's files.**
3. **Sorting tags alphabetically and thinking `v1.10.0` is older than `v1.2.0`.**
4. **Publishing a program without a checksum.**
5. **Fully automating a release with no human check.**

## Practice

Do the exercises in [`exercises/ch66-exercises.md`](../../../exercises/ch66-exercises.md).

## Self-Test

1. What is the difference between a tag and a release?
2. What does each part of MAJOR.MINOR.PATCH mean?
3. Why does `git tag` list `v1.10.0` before `v1.2.0`, and what fixes it?
4. What is in a source archive, and what is not?
5. What does an immutable release forbid?

## Before Moving On

You are ready for Chapter 67<!--ref:ossproject--> if you can:

- [ ] choose the next version number after a change
- [ ] draft release notes from history
- [ ] make a source archive with Git

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Tag sorting, notes from history, `git describe`, `git archive`, `release.yml` structure | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, PyYAML 6.0.1; CI on newer Git | R322, R323 (local side) |
| Releases are based on tags; permissions; source archives; generated notes; immutability; asset limits exist | Checked against `github/docs` (commit `2eaab0b`); **not run on a live account** | R321, R322 |
| Semantic Versioning rules | Read from the specification in its public repository (version 2.0.0) | R323 |
| The permission name for a release-creating workflow | **Not checked** | none |

## Where this leads

Chapter 67<!--ref:ossproject--> builds a small open-source library with everything from this Part: layout, documentation, licence, versioning and releases.
