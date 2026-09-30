# Chapter 66 exercises — Releases

Attempt each exercise before you open `solutions/ch66-solutions.md`. Exercises 2.1 to 2.2 use only your terminal.

## Level 1 — Guided

**1.1 Tag or release.** State two differences between a Git tag and a GitHub release.

**1.2 Next version.** The current version is 1.4.2. Give the next version after (a) a bug fix, (b) a new backward-compatible feature, (c) a change that breaks existing users.

## Level 2 — Partially guided

**2.1 Sorting.** In a sandbox repository, make annotated tags `v1.2.0` and `v1.10.0`. Run `git tag` and `git tag --sort=-version:refname`. Which output puts the newest first?

**2.2 An archive.** Make a `tar.gz` source archive of a tag with a prefix folder, list what is inside and test it with `gzip -t`.

## Level 3 — Independent

**3.1 A draft of notes.** For your sandbox, write release notes from the commit subjects between two tags, using `git log --format`.

**3.2 A config file.** Write a `.github/release.yml` with one category for the label `bug` and one catch-all category, and read it back.

## Level 4 — Professional scenario

**4.1 A wrong tag.** You published a release and then notice the tag points to a commit that is missing the last fix. Explain what you would do, given that a released version must not change. Consider what an immutable release would forbid.

## Level 5 — Troubleshooting

**5.1** After `git clone`, your colleague cannot see the release notes or the attached files. Why, and where are they?

**5.2** `git tag` lists `v1.10.0` before `v1.2.0`. Is something broken?
