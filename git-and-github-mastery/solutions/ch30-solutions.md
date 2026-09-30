# Chapter 30 solutions

## Level 1
**1.1** `blob`, `17`, and the text `White loaf: 2.80`.

**1.2** The file is `.git/objects/28/adfbf...`: the folder is the first two characters of the hash, the file name is the rest.

## Level 2
**2.1** No: identical content has the same hash, so it is the same object.

**2.2** `printf 'blob 17\0White loaf: 2.80\n' | sha1sum` prints the same hash as `git hash-object`.

## Level 3
**3.1** The commit shows `tree <hash>`; `git cat-file -p <hash>` lists the entries (`menu.md` as a blob, `drinks` as a tree); `git cat-file -p <blob-hash>` prints the file.

**3.2** `.git/HEAD` says `ref: refs/heads/<branch>`; the branch file has 41 characters: 40 for the hash and a newline.

## Level 4
**4.1** The lightweight tag is a ref straight to the commit, so `git cat-file -t` prints `commit`; the annotated tag is its own object and prints `tag`. `<tag>^{commit}` gives the commit hash for both.

## Level 5
**5.1** Deleting a branch removes only the ref (the small file). The commits stay in the database until they are unreachable *and* garbage collection removes them. Check with `git reflog` or `git fsck --no-reflogs`.

**5.2** `count` counts loose objects. After `gc`, the objects are in a pack, so `in-pack` rose instead. Nothing was lost.

**5.3** `git rev-parse main` (or `git rev-parse HEAD`). Files in `.git` may change format: refs can be stored in a packed list instead of as separate files.
