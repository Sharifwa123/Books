# Chapter 66 solutions

## Level 1
**1.1** A tag is a name for a commit and exists in Git, so a clone gets it. A release is a GitHub page built on a tag, with notes and attached files; it does not exist in a plain clone. Also: a tag date may differ from the release date.

**1.2** (a) 1.4.3, (b) 1.5.0, (c) 2.0.0, following Semantic Versioning.

## Level 2
**2.1** The second output, `git tag --sort=-version:refname`, puts the newest first (`v1.10.0`, then `v1.2.0`). Plain `git tag` sorts alphabetically, so in an oldest-first reading it wrongly lists `v1.10.0` before `v1.2.0`.

**2.2** `git archive --format=tar.gz --prefix=proj-1.0.0/ -o ../proj-1.0.0.tar.gz v1.0.0`, then `tar -tzf ../proj-1.0.0.tar.gz` and `gzip -t ../proj-1.0.0.tar.gz`.

## Level 3
**3.1** `git log --format='- %s' v1.0.0..v1.1.0`, then tidy the lines into groups.

**3.2** For example: `changelog:`, then `categories:`, an item with `title: Bug fixes` and `labels: [bug]`, and a second item with `title: Other changes` and `labels: ["*"]`; read back with a YAML parser or `cat`.

## Level 4
**4.1** Do not move the tag of a published release: people may already have used it. Publish a new patch version that contains the fix, and say in its notes what it corrects. With immutable releases enabled, the documentation says you cannot move or delete the tag while the release exists. Preparing releases as drafts first helps to catch such a mistake before publication.

## Level 5
**5.1** Releases are a GitHub feature, not part of Git; a clone contains tags but not the release page, notes or attached files. They are on the repository's Releases page (or through the Releases API).

**5.2** No. `git tag` sorts alphabetically; use `--sort=version:refname` to sort by version number.
