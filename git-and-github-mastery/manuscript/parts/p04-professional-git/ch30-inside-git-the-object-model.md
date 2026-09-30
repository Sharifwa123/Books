---
key: objects
number: 30
tag: Deep
first_read: later
status: draft
requires: [commits, branching]
ledger: [R199, R200, R201, R202]
---
# Chapter 30 — Inside Git: The Object Model [Deep]

**In this chapter**

- how Git stores your files: **blobs**, **trees**, **commits** and **tags**
- why a hash identifies content
- how branches and tags are just small files
- what a packfile is, and what `git gc` does
- `git fsck`, dangling objects, and `git archive`

> **Deep.** This chapter is marked **[Deep]**. You can use Git well without it. It explains *why* Git behaves as it does, and it makes the reflog (Chapter 26<!--ref:reflog-->), rebase (Chapter 27<!--ref:rebase-->) and the security chapter (Chapter 33<!--ref:gitsec-->) much easier to understand.

**Before you start.** Chapter 15<!--ref:model-->, Chapter 19<!--ref:commits--> and Chapter 20<!--ref:branching-->. Every command here was run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0. The examples inspect the `.git` folder; the file layout described is what these versions do. Git's own documentation calls the internals subject to change, so do not write programs that depend on the layout.

---

## 30.1 A database of named things

Chapter 15<!--ref:model--> showed that a commit is a snapshot. Underneath, Git is a **content-addressed database**: you give it content, it gives you back a name (a hash), and you can ask for the content by that name.

> **New term: object.** Any item in Git's database. Git has four kinds: blob, tree, commit and tag.

Ask Git to store a line of text. `git hash-object` computes the name without storing; `-w` writes it:

```text
$ git init obj-demo
Initialized empty Git repository in /home/learner/obj-demo/.git/
$ cd obj-demo
$ echo 'White loaf: 2.80' | git hash-object --stdin
28adfbf9397e4db31a26821309402a09c1b6b943
$ echo 'White loaf: 2.80' | git hash-object -w --stdin
28adfbf9397e4db31a26821309402a09c1b6b943
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

The name `28adfbf9397e4db31a26821309402a09c1b6b943` is a **hash** of the content. The same content always gives the same name, on any computer. With `-w`, the object was stored:

```text
$ find .git/objects -type f
.git/objects/28/adfbf9397e4db31a26821309402a09c1b6b943
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

The stored object is a file in `.git/objects`, in a folder named after the **first two** characters of the hash (`28`), with the rest as the file name. Ask what kind of object it is, how big, and what it contains:

```text
$ git cat-file -t 28adfbf
blob
$ git cat-file -s 28adfbf
17
$ git cat-file -p 28adfbf
White loaf: 2.80
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

> **New term: blob.** An object that holds the contents of one file, and nothing else: no name, no folder, no date. (The word is short for "binary large object".)

The blob is 17 bytes: the sixteen visible characters plus the newline. Storing **the same content again** does not make a second copy:

```text
$ echo 'White loaf: 2.80' | git hash-object -w --stdin
28adfbf9397e4db31a26821309402a09c1b6b943
$ find .git/objects -type f | wc -l
1
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

The count is still one file. Two files with identical content, anywhere in your project or its history, share one blob.

### The name is computed, not chosen

The hash is not random. It is the SHA-1 checksum of a short header, the word `blob`, a space, the size in bytes, and a zero byte, followed by the content. You can compute it yourself with an ordinary tool:

```text
$ printf 'blob 17\0White loaf: 2.80\n' | sha1sum
28adfbf9397e4db31a26821309402a09c1b6b943  -
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

The result is the same name that Git produced. The last line of the recording shows which hash function this repository uses:

```text
$ git rev-parse --show-object-format
sha1
```

*Recorded in Bash; `ch30-objects/expected-blob.bash.txt`.*

> **Checked against the documentation (Git 2.56.0, R202).** SHA-1 is the default object format in the versions tested. Git's own document on planned breaking changes, in its section on Git 3.0, says that "the default hash function for new repositories will be changed from "sha1" to "sha256"", and gives as the reason that "SHA-1 has been deprecated by NIST in 2011" (it also plans the "reftable" reference format and the default branch name `main` for new repositories). Those are *plans* for a future version, not a description of today's default. A SHA-256 repository "cannot be read by older versions of Git", and the project's transition document says that SHA-256 was picked in late 2018 as SHA-1's successor. So: treat "SHA-1" as the current default, expect it to change, and never write a script that depends on the length of a hash.

---

## 30.2 Trees and commits

A blob has no file name. The names live in **trees**.

> **New term: tree.** An object that lists the contents of one folder: for each entry a mode, a type (blob or another tree), a hash and a name.

Build a small project with a folder in it, and commit:

```text
$ git init obj-demo
Initialized empty Git repository in /home/learner/obj-demo/.git/
$ cd obj-demo
$ printf 'White loaf: 2.80\nRolls (six): 3.00\n' > menu.md
$ mkdir drinks
$ printf 'Tea: 1.50\n' > drinks/hot.md
$ git add .
$ git commit -m "Add menu and drinks"
[main (root-commit) 762af16] Add menu and drinks
 2 files changed, 3 insertions(+)
 create mode 100644 drinks/hot.md
 create mode 100644 menu.md
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

Look at the commit **object** itself:

```text
$ git cat-file -p HEAD
tree 3f1f9623d71be5d01728beffeab8c162cc97e3ca
author Ada Learner <ada@example.org> 1767603960 +0000
committer Ada Learner <ada@example.org> 1767603960 +0000

Add menu and drinks
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

A commit has four things: the hash of a **tree** (the whole project at that moment), the **author** and **committer** (with a timestamp, in seconds since 1970, and a time zone), and the **message**. A commit that had a parent would also have a `parent` line naming it. This first commit has none.

Then look at the tree that the commit names:

```text
$ git cat-file -p 'HEAD^{tree}'
040000 tree 8214205a3a9ec4a01ff1c38afed63b0fa8265355	drinks
100644 blob 5cf2ab8b14d0142893464d70f752b9b4d25797a3	menu.md
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

Two entries: `menu.md` is a blob (mode `100644`, an ordinary file), and `drinks` is another **tree** (mode `040000`, a folder). The shortcut `git ls-tree HEAD` shows the same thing, and `-r` walks into folders:

```text
$ git ls-tree HEAD
040000 tree 8214205a3a9ec4a01ff1c38afed63b0fa8265355	drinks
100644 blob 5cf2ab8b14d0142893464d70f752b9b4d25797a3	menu.md
$ git ls-tree -r HEAD
100644 blob 45f2c5990d976c063458edad8ee69ecb26749412	drinks/hot.md
100644 blob 5cf2ab8b14d0142893464d70f752b9b4d25797a3	menu.md
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

You can read one file from any commit with `commit:path`:

```text
$ git cat-file -p HEAD:drinks/hot.md
Tea: 1.50
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

The **index** (Chapter 15<!--ref:model-->) is a list of the same kind, the tree that the *next* commit will use:

```text
$ git ls-files --stage
100644 45f2c5990d976c063458edad8ee69ecb26749412 0	drinks/hot.md
100644 5cf2ab8b14d0142893464d70f752b9b4d25797a3 0	menu.md
```

*Recorded in Bash; `ch30-objects/expected-commit.bash.txt`.*

So a commit points to a tree, a tree points to blobs and other trees, and each name is the hash of what it names. A change to any file changes its blob's hash, so the tree's hash, so the commit's hash. That is why a commit hash identifies the **whole** project *and its entire history*: each commit contains its parent's hash, so a change anywhere back in time would change every hash after it. (This is also why rebasing creates new commits, Chapter 27<!--ref:rebase-->.)

---

## 30.3 Refs: names for commits

Branches, tags and `HEAD` are not objects. They are **refs**: small files that contain a hash or the name of another ref.

> **New term: ref.** A name that points to an object, stored as a small file under `.git/refs` (or, in some cases, in a packed list). Branches, tags and remote-tracking branches are refs.

Make a commit, an annotated tag, and a branch:

```text
$ git init obj-demo
Initialized empty Git repository in /home/learner/obj-demo/.git/
$ cd obj-demo
$ printf 'White loaf: 2.80\n' > menu.md
$ git add menu.md
$ git commit -m "Add menu"
[main (root-commit) d2c521c] Add menu
 1 file changed, 1 insertion(+)
 create mode 100644 menu.md
$ git tag -a v1.0 -m "First menu"
$ git switch -c experiment
Switched to a new branch 'experiment'
```

*Recorded in Bash; `ch30-objects/expected-refs.bash.txt`.*

Now read the files:

```text
$ cat .git/HEAD
ref: refs/heads/experiment
$ cat .git/refs/heads/main
d2c521ce41194be46021aef2f83e2fe37d6fe9f8
$ cat .git/refs/tags/v1.0
da7d3cd54643668fae087fd3eb73361482a60fa2
```

*Recorded in Bash; `ch30-objects/expected-refs.bash.txt`.*

`.git/HEAD` says `ref: refs/heads/experiment`: `HEAD` points to a branch (Chapter 26<!--ref:reflog--> called the alternative a detached `HEAD`). `.git/refs/heads/main` is a file with **41 characters**: the commit's hash, and a newline. **That is all a branch is.** Creating a branch writes one small file; deleting one removes it. This is why branches in Git are cheap. (After `git gc`, Git may move these files into one file, `.git/packed-refs`. This was checked by hand for this chapter but not recorded; it is one more reason to ask `git rev-parse` rather than read the files.)

`git show-ref` lists them all:

```text
$ git show-ref
d2c521ce41194be46021aef2f83e2fe37d6fe9f8 refs/heads/experiment
d2c521ce41194be46021aef2f83e2fe37d6fe9f8 refs/heads/main
da7d3cd54643668fae087fd3eb73361482a60fa2 refs/tags/v1.0
```

*Recorded in Bash; `ch30-objects/expected-refs.bash.txt`.*

Both branches point to the same commit. The tag has a **different** hash, because an annotated tag is an object of its own (the fourth kind):

```text
$ git cat-file -t v1.0
tag
$ git cat-file -p v1.0
object d2c521ce41194be46021aef2f83e2fe37d6fe9f8
type commit
tag v1.0
tagger Ada Learner <ada@example.org> 1767604020 +0000

First menu
```

*Recorded in Bash; `ch30-objects/expected-refs.bash.txt`.*

> **New term: tag object.** The object that an annotated tag creates: it names another object (usually a commit), a type, a tag name, the tagger and a message. A lightweight tag has no object of its own; it is a ref straight to the commit.

Three ways to ask "what does this name point to?":

```text
$ git rev-parse main v1.0 'v1.0^{commit}'
d2c521ce41194be46021aef2f83e2fe37d6fe9f8
da7d3cd54643668fae087fd3eb73361482a60fa2
d2c521ce41194be46021aef2f83e2fe37d6fe9f8
```

*Recorded in Bash; `ch30-objects/expected-refs.bash.txt`.*

The tag `v1.0` resolves to the tag object, and `v1.0^{commit}` follows it through to the commit. This is why `git ls-remote` listed annotated tags twice in Chapter 29<!--ref:tags-->.

---

## 30.4 Loose objects and packfiles

Each object you create starts as a **loose object**: one file. Git also has a compact format, the **packfile**, which stores many objects in one file and stores similar versions as *differences*.

> **New term: packfile.** A single file in which Git stores many objects compactly, using differences between similar objects. Git creates packfiles when it tidies (`git gc`) and when it sends or receives objects over a network.

Three commits have been made. Count the objects, then let Git tidy:

```text
$ git init obj-demo
Initialized empty Git repository in /home/learner/obj-demo/.git/
$ cd obj-demo
$ printf 'White loaf: 2.80\n' > menu.md
$ git add menu.md
$ git commit -m "Add menu"
[main (root-commit) d2c521c] Add menu
 1 file changed, 1 insertion(+)
 create mode 100644 menu.md
$ printf 'White loaf: 2.90\n' > menu.md
$ git commit -am "Raise the price"
[main 4e686c1] Raise the price
 1 file changed, 1 insertion(+), 1 deletion(-)
$ printf 'White loaf: 3.00\n' > menu.md
$ git commit -am "Raise the price again"
[main 2171d29] Raise the price again
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch30-objects/expected-storage.bash.txt`.*

```text
$ git count-objects -v | grep -E '^(count|in-pack|packs):'
count: 9
in-pack: 0
packs: 0
```

*Recorded in Bash; `ch30-objects/expected-storage.bash.txt`.*

`count` is the number of **loose** objects: nine (three commits, three trees, three blobs). `in-pack` and `packs` say that none are packed yet. Now run garbage collection:

```text
$ git gc -q
$ git count-objects -v | grep -E '^(count|in-pack|packs):'
count: 0
in-pack: 9
packs: 1
```

*Recorded in Bash; `ch30-objects/expected-storage.bash.txt`.*

> **New term: garbage collection.** Git's housekeeping: `git gc` packs loose objects into packfiles and removes objects that nothing refers to any more (after a safety period).

The nine loose files became nine objects inside **one** pack. The history is unchanged:

```text
$ git log --oneline
2171d29 (HEAD -> main) Raise the price again
4e686c1 Raise the price
d2c521c Add menu
$ git cat-file -p HEAD~2:menu.md
White loaf: 2.80
```

*Recorded in Bash; `ch30-objects/expected-storage.bash.txt`.*

Git runs this kind of housekeeping on its own from time to time, so you rarely need to.

> **Checked against the documentation (Git 2.56.0, R201).** `git gc` "will call `prune --expire 2.weeks.ago`": unreachable objects younger than **two weeks** are kept (the setting is `gc.pruneExpire`). Git also runs a light-weight `git gc --auto` "from time to time" from some commands: it packs the loose objects when there are "approximately more than" **6700** of them (`gc.auto`), and consolidates packs when there are more than **50** (`gc.autoPackLimit`). Chapter 26<!--ref:reflog--> gives the reflog's own expiry periods (90 and 30 days) and the practical rule: recover soon.

---

## 30.5 Checking and exporting

`git fsck` checks that the database is consistent. A healthy repository prints nothing and exits with status 0:

```text
$ git init obj-demo
Initialized empty Git repository in /home/learner/obj-demo/.git/
$ cd obj-demo
$ printf 'White loaf: 2.80\n' > menu.md
$ git add menu.md
$ git commit -m "Add menu"
[main (root-commit) d2c521c] Add menu
 1 file changed, 1 insertion(+)
 create mode 100644 menu.md
$ printf 'Rolls (six): 3.00\n' >> menu.md
$ git commit -am "Add rolls"
[main ee9eec6] Add rolls
 1 file changed, 1 insertion(+)
$ git fsck 2>/dev/null; echo "exit status: $?"
exit status: 0
```

*Recorded in Bash; `ch30-objects/expected-fsck.bash.txt`.*

(Here `2>/dev/null` hides the progress messages, which do not matter to us. `echo "exit status: $?"` prints the exit status.)

After a `git reset --hard` (Chapter 25<!--ref:undo-->), the commit that was dropped is still in the database, but no branch or tag leads to it. `fsck` can find such objects. The option `--no-reflogs` ignores the reflog, so that the commit really counts as unreachable:

```text
$ git reset --hard HEAD~1
HEAD is now at d2c521c Add menu
$ git fsck --no-reflogs 2>/dev/null
dangling commit ee9eec6763a660d81626c783ad78359f8920c2ff
```

*Recorded in Bash; `ch30-objects/expected-fsck.bash.txt`.*

> **New term: dangling object.** An object in the database that no ref leads to. Such objects will be removed by garbage collection eventually.

`dangling commit ee9eec6...` is the "Add rolls" commit we reset away. This is how commits can be recovered even without the reflog, until `gc` removes them.

Finally, `git archive` exports a commit as a plain archive, without the `.git` folder. This is handy for sharing a snapshot:

```text
$ git archive --format=tar HEAD | tar -t
menu.md
```

*Recorded in Bash; `ch30-objects/expected-fsck.bash.txt`.*

The archive (piped to `tar -t`, which lists its contents) holds only the files of the commit.

---

## 30.6 What this explains

| You have seen... | ...because |
|---|---|
| Two identical files take space once | Same content, same blob hash |
| Commits are cheap; branches are cheaper | A commit is a few small objects; a branch is a 41-byte file |
| Rebase gives new hashes | A commit's hash includes its parent's hash and its tree |
| `reset --hard` does not delete commits at once | The objects stay until `gc` removes unreachable ones |
| A secret committed once stays in history | The blob is reachable from every commit that has it; Chapter 33<!--ref:gitsec--> |

---

## Checkpoint

## What You Learned

- Git is a content-addressed database of four kinds of object: blobs (file contents), trees (folders), commits and tags.
- An object's name is the SHA-1 hash of a header and its content in these versions of Git, so identical content is stored once.
- A commit names a tree, its parent(s), an author, a committer and a message.
- Branches, tags and `HEAD` are refs: small files that contain a hash or another ref's name.
- Objects begin as loose files; `git gc` packs them and eventually removes unreachable objects.
- `git fsck` checks the database and lists dangling objects; `git archive` exports a snapshot.

## New Vocabulary

- **Object**: any item in Git's database (blob, tree, commit or tag).
- **Blob**: an object holding the contents of one file.
- **Tree**: an object listing the contents of a folder.
- **Ref**: a name that points to an object, stored as a small file.
- **Tag object**: the object created by an annotated tag.
- **Packfile**: one file storing many objects compactly.
- **Garbage collection**: housekeeping that packs objects and removes unreachable ones.
- **Dangling object**: an object no ref leads to.

## Commands Learned

`git hash-object`, `git cat-file -t`, `git cat-file -s`, `git cat-file -p`, `git ls-tree`, `git ls-files --stage`, `git show-ref`, `git rev-parse`, `git count-objects -v`, `git gc`, `git fsck`, `git archive`.

## Common Mistakes

1. **Editing files inside `.git` by hand.**
2. **Assuming a branch is a copy of the files.**
3. **Thinking `git gc` is needed in daily work.**
4. **Trusting "unreachable means deleted".**
5. **Assuming the hash algorithm will never change.**

## Practice

Do the exercises in [`exercises/ch30-exercises.md`](../../../exercises/ch30-exercises.md).

## Self-Test

1. What is a blob, and what does it *not* contain?
2. Why is the same content stored only once?
3. What is inside `.git/refs/heads/main`?
4. What is the difference between a lightweight and an annotated tag, at the object level?
5. What does `git fsck --no-reflogs` report after a `git reset --hard`, and why?

## Before Moving On

You are ready for Chapter 31<!--ref:bigrepos--> if you can:

- [ ] name the four kinds of object
- [ ] explain how a commit leads to files
- [ ] read `.git/HEAD` and a branch file
- [ ] describe what `git gc` does

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| `hash-object`, `cat-file`, loose storage, hash = SHA-1 of header plus content | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 (the hash was also recomputed with `sha1sum`). Some concept and option statements for this row were also checked in the Git 2.56.0 manual (git-cat-file, git-hash-object); the ledger row says which. | R199 |
| Commit, tree, `ls-tree`, index, refs, tag objects | Locally tested (as above). Some concept and option statements for this row were also checked in the Git 2.56.0 manual (git-ls-tree, gitrepository-layout); the ledger row says which. | R200 |
| Packfiles, `gc`, `fsck`, dangling objects, `archive` | Locally tested (as above) | R201 |
| Default hash function and the planned change in Git 3.0; `gc` grace period and automatic `gc` thresholds | Checked against the Git 2.56.0 documentation (`BreakingChanges`, `technical/hash-function-transition`, `config/gc`) | R201, R202 |

## Where this leads

Chapter 31<!--ref:bigrepos--> deals with very large repositories, where these storage facts matter. Chapter 32<!--ref:custom--> customises Git, Chapter 33<!--ref:gitsec--> shows why history is hard to scrub, and Chapter 35<!--ref:readdocs--> shows how to read the official documentation that describes these internals.
