---
key: tags
number: 29
tag: Core
first_read: part
status: draft
requires: [remotes, history_view]
ledger: [R196, R197, R198]
---
# Chapter 29 — Tags and Versioning [Core]

**In this chapter**

- tagging an older commit, and listing tags
- version numbers, and *semantic versioning* as a convention
- why tags sort oddly, and how to fix the order
- `git describe`
- sharing tags with a remote, and deleting them there

**Before you start.** Chapter 24<!--ref:stash--> (which introduced tags) and Chapter 23<!--ref:remotes-->. The recordings use `bakery-menu` and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

Chapter 24<!--ref:stash--> made a tag on the newest commit. This chapter uses tags properly: to mark releases, on any commit, and to share them.

---

## 29.1 Tag any commit

A tag does not have to be on the commit you are standing on. Give the commit's hash at the end, and you can mark history retrospectively. Here the very first commit gets `v0.1.0`, the current one gets `v1.0.0`, and a third tag marks the commit before it as a *release candidate*:

```text
$ git tag -a v0.1.0 8a52ffe -m "First draft of the menu"
$ git tag -a v1.0.0 -m "First public menu"
$ git tag v1.0.0-rc.1 HEAD~1
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

`-a` makes an **annotated** tag (Chapter 24<!--ref:stash-->) and `-m` gives its message. Without `-a`, as in the third command, the tag is **lightweight**.

Show the tags, and the commit that a tag names:

```text
$ git show v0.1.0 --stat --oneline
tag v0.1.0

First draft of the menu
8a52ffe (tag: v0.1.0) Add the menu
 menu.md | 4 ++++
 1 file changed, 4 insertions(+)
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

`git show` prints the tag's own details first (the tag name, the message), then the commit it points to. Tags marking a release are almost always **annotated**: the tagger, date and message are part of the record.

---

## 29.2 Version numbers

Names such as `v0.1.0` and `v1.0.0` follow a convention called **semantic versioning**.

> **New term: semantic versioning.** A convention for numbering releases as `MAJOR.MINOR.PATCH`: the first number changes when the change is *incompatible* with earlier versions, the second when features are *added* in a compatible way, and the third for compatible bug *fixes*. A hyphen and a label, as in `1.0.0-rc.1`, mark a pre-release.

> **Checked against the specification (Semantic Versioning 2.0.0, R198).** The specification says: "Given a version number MAJOR.MINOR.PATCH, increment the MAJOR version when you make incompatible API changes, the MINOR version when you add functionality in a backward compatible manner, the PATCH version when you make backward compatible bug fixes". A pre-release "MAY be denoted by appending a hyphen and a series of dot separated identifiers", and "pre-release versions have a lower precedence than the associated normal version" (`1.0.0-alpha < 1.0.0`). The specification also says of the letter `v`: `v1.2.3` "is not a semantic version", but prefixing one with a `v` is "a common way ... to indicate it is a version number", and it even uses `git tag v1.2.3 -m "Release version 1.2.3"` as its example. The tag names in this chapter are *examples of the convention*, not a requirement of Git: Git accepts any name (Chapter 20<!--ref:branching--> listed the rules for names).

A leading `v` (as in `v1.0.0`) is common but not part of the number.

---

## 29.3 Listing and ordering

Plain `git tag` lists tags **alphabetically**, which is not always version order:

```text
$ git tag
v0.1.0
v1.0.0
v1.0.0-rc.1
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

The pre-release `v1.0.0-rc.1` appears *after* `v1.0.0`, but a release candidate comes *before* the release. `--sort=version:refname` sorts the numbers as versions ("1.9" before "1.10"), but by itself it does not fix that pre-release problem:

```text
$ git tag --sort=version:refname
v0.1.0
v1.0.0
v1.0.0-rc.1
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

A setting names the suffix that marks a pre-release, and then it sorts correctly:

```text
$ git -c versionsort.suffix=-rc tag --sort=version:refname
v0.1.0
v1.0.0-rc.1
v1.0.0
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

`-c versionsort.suffix=-rc` sets that option for one command only (Chapter 14<!--ref:config-->). To make it permanent, use `git config versionsort.suffix -rc`.

---

## 29.4 `git describe`

`git describe` names the current commit in terms of the nearest tag:

```text
$ git describe
v1.0.0
$ git describe --tags 8a52ffe
v0.1.0
```

*Recorded in Bash; `ch29-tags/expected-versions.bash.txt`.*

At a tagged commit it prints just the tag. The second command asks about another commit (the first one), and finds the tag `v0.1.0` on it. Both tags here were annotated, so both were found.

On a commit *after* the tag, `git describe` adds the number of commits since the tag and a short hash. Two commits were added after `v1.0`:

```text
$ cd bakery-menu
$ git tag -a v1.0 -m "First public menu"
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -qam "Add tea"
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -qam "Add coffee"
$ git describe
v1.0-2-g398a33e
```

*Recorded in Bash; `ch29-tags/expected-describe-after.bash.txt`.*

`v1.0-2-g398a33e` reads: tag `v1.0`, **2** commits after it, and `g` (for "git") followed by the abbreviated hash of the current commit. `--abbrev=4` shortens the hash:

```text
$ git describe --abbrev=4
v1.0-2-g398a
```

*Recorded in Bash; `ch29-tags/expected-describe-after.bash.txt`.*

By default `git describe` only looks at **annotated** tags (Git's documentation: "By default (without `--all` or `--tags`) `git describe` only shows annotated tags"). A lightweight tag is ignored until you say `--tags`:

```text
$ git tag v1.1-light
$ git describe
v1.0-2-g398a33e
$ git describe --tags
v1.1-light
```

*Recorded in Bash; `ch29-tags/expected-describe-after.bash.txt`.*

`--always` prints a bare abbreviated hash when no tag can be used, and `--dirty` adds a mark if the working tree has uncommitted changes (there were none here):

```text
$ git describe --always --dirty
v1.0-2-g398a33e
```

*Recorded in Bash; `ch29-tags/expected-describe-after.bash.txt`.*

---

## 29.5 Sharing tags

Tags are **local** until you push them (Chapter 23<!--ref:remotes-->). Even after `git push`, tags stay behind. To see this, a bare repository `hub.git` acts as the remote, and the branch is pushed first (with `-q`, quietly). Then a tag is made, another lightweight one too, and only one is sent:

```text
$ git remote add origin ../hub.git
$ git push -q origin main
$ git tag -a v1.0.0 -m "First public menu"
$ git tag v0.9-lightweight
$ git push origin v1.0.0
To ../hub.git
 * [new tag]         v1.0.0 -> v1.0.0
```

*Recorded in Bash; `ch29-tags/expected-remote.bash.txt`.*

`git push origin v1.0.0` sent one tag. To see what the remote has, ask it directly:

```text
$ git ls-remote --tags origin
1d32143cf5c3f7fd0d2bc2c5b7494e76ae07ac2b	refs/tags/v1.0.0
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v1.0.0^{}
```

*Recorded in Bash; `ch29-tags/expected-remote.bash.txt`.*

`git ls-remote --tags origin` lists the tags on the remote without downloading anything. Each line is a hash and a name. `v1.0.0` appears twice: the first line (`1d32143...`) is the **tag object** (the annotated tag itself); the second, ending in `^{}`, is the **commit** it points to. (A lightweight tag would appear once.) The lightweight tag `v0.9-lightweight` is **not** on the remote, because it was not pushed.

To push all your tags at once:

```text
$ git push origin --tags
To ../hub.git
 * [new tag]         v0.9-lightweight -> v0.9-lightweight
$ git ls-remote --tags origin
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v0.9-lightweight
1d32143cf5c3f7fd0d2bc2c5b7494e76ae07ac2b	refs/tags/v1.0.0
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v1.0.0^{}
```

*Recorded in Bash; `ch29-tags/expected-remote.bash.txt`.*

Now the lightweight tag is there too, pointing straight at a commit. Be careful with `--tags`: it sends *every* local tag, including ones you may have made by mistake.

---

## 29.6 Deleting a tag

Deleting a tag locally does **not** delete it on the remote:

```text
$ git tag -d v0.9-lightweight
Deleted tag 'v0.9-lightweight' (was 81f772e)
$ git ls-remote --tags origin
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v0.9-lightweight
1d32143cf5c3f7fd0d2bc2c5b7494e76ae07ac2b	refs/tags/v1.0.0
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v1.0.0^{}
```

*Recorded in Bash; `ch29-tags/expected-remote.bash.txt`.*

The local tag is gone, but the remote still lists `v0.9-lightweight`. Remove it there explicitly:

```text
$ git push origin --delete v0.9-lightweight
To ../hub.git
 - [deleted]         v0.9-lightweight
$ git ls-remote --tags origin
1d32143cf5c3f7fd0d2bc2c5b7494e76ae07ac2b	refs/tags/v1.0.0
81f772ee32b93d8fcf80dbb34ab74053b69d97a2	refs/tags/v1.0.0^{}
```

*Recorded in Bash; `ch29-tags/expected-remote.bash.txt`.*

`- [deleted]` confirms it.

> **⚠️ CAUTION.** Deleting a tag that other people may have already fetched does not remove it from *their* repositories, and re-using the name for a different commit causes confusion. Treat published tags as permanent: if a release is wrong, make a new tag (`v1.0.1`) rather than moving the old one.

> **Checked against GitHub's documentation (R196).** "About releases" says releases "are based on Git tags", that a tag's date "may be different" from the release date, and that GitHub "will automatically include links to download a zip file and a tarball containing the contents of the repository at the point of the tag's creation". Chapter 66<!--ref:releases--> covers them in full.

---

## Checkpoint

## What You Learned

- A tag can name any commit, given by hash: `git tag -a v0.1.0 <hash> -m "..."`.
- Semantic versioning (`MAJOR.MINOR.PATCH`) is a convention, not a Git rule.
- `git tag` lists alphabetically; `--sort=version:refname` sorts as versions, and `versionsort.suffix` places pre-releases correctly.
- `git describe` names a commit after the nearest tag.
- Tags are not sent by an ordinary push: use `git push origin <tag>` or `--tags`; `git ls-remote --tags` shows the remote's tags.
- Deleting a tag remotely needs `git push origin --delete <tag>`.

## New Vocabulary

- **Semantic versioning**: the convention of `MAJOR.MINOR.PATCH` version numbers.

## Commands Learned

`git tag -a <name> <commit> -m`, `git tag --sort=version:refname`, `git describe`, `git push origin <tag>`, `git push origin --tags`, `git push origin --delete <tag>`, `git ls-remote --tags`.

## Common Mistakes

1. **Expecting `git push` to send tags.**
2. **Using `--tags` and pushing tags made by mistake.**
3. **Deleting a tag locally and assuming it is gone from the remote.**
4. **Moving or re-using a published tag.**
5. **Trusting alphabetical order as version order.**

## Practice

Do the exercises in [`exercises/ch29-exercises.md`](../../../exercises/ch29-exercises.md).

## Self-Test

1. How do you tag a commit that is not the current one?
2. What do the three numbers in `1.4.2` mean under semantic versioning?
3. Why did `git tag` list `v1.0.0-rc.1` after `v1.0.0`?
4. Why does `git ls-remote --tags` show `v1.0.0` twice?
5. How do you remove a tag from a remote?

## Before Moving On

You are ready for Chapter 33<!--ref:gitsec--> if you can:

- [ ] tag an older commit
- [ ] push a tag and see it on the remote
- [ ] delete a tag locally and remotely
- [ ] explain why published tags should not move

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Tagging older commits, listing, `--sort`, `versionsort.suffix`, `describe` on tagged commits | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R196 |
| Pushing, listing (`ls-remote`) and deleting tags on a remote | Locally tested (as above), with a local bare repository | R197 |
| Semantic versioning rules (`MAJOR.MINOR.PATCH`, pre-release precedence, the `v` prefix) | Checked against the Semantic Versioning 2.0.0 specification text | R198 |
| `describe` after a tag (`<tag>-<n>-g<hash>`), `--abbrev`, `--tags`, `--always`, `--dirty`; `versionsort.suffix` | Locally tested (as above); checked against the `git describe` and `versionsort.suffix` documentation (Git 2.56.0) | R198 |

## Where this leads

Chapter 33<!--ref:gitsec--> covers signing commits and tags. Chapter 66<!--ref:releases--> shows how a hosting platform builds releases on top of tags, and Chapter 34<!--ref:workflows--> shows how teams use tags.
