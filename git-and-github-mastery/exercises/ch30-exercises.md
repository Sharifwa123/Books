# Chapter 30 exercises — Inside Git: The Object Model

Attempt each exercise before you open `solutions/ch30-solutions.md`. Use a new, empty repository (`git init obj-demo`). Do not edit files inside `.git`.

## Level 1 — Guided

**1.1 A blob by hand.** Run `echo 'White loaf: 2.80' | git hash-object -w --stdin`. Then run `git cat-file -t`, `-s` and `-p` on the hash. What are the three answers?

**1.2 Where is it?** Run `find .git/objects -type f`. How is the path related to the hash?

## Level 2 — Partially guided

**2.1 Same content twice.** Store the same line again. Does the number of files change? Why?

**2.2 Compute it yourself.** Use `printf` and `sha1sum` to compute the hash of `blob 17\0White loaf: 2.80\n`. Compare it with Git's.

## Level 3 — Independent

**3.1 Follow a commit.** Commit a `menu.md` and a `drinks/hot.md`. Follow the chain by hand: `git cat-file -p HEAD`, then the tree it names, then a blob.

**3.2 What is a branch?** Create a branch. Print `.git/HEAD` and `.git/refs/heads/<branch>`. How many characters are in the branch file?

## Level 4 — Professional scenario

**4.1 Tags at object level.** Create one lightweight and one annotated tag on the same commit. Use `git cat-file -t` on each. Explain the difference and how `git rev-parse <tag>^{commit}` treats them.

## Level 5 — Troubleshooting

**5.1** A colleague says "I deleted the branch, so the commits are gone from the disk". Explain what is really true, and how you would check.

**5.2** After `git gc`, a learner counts objects and sees `count: 0`. They fear the data is lost. What happened?

**5.3** A learner wants to write a script that reads `.git/refs/heads/main` to find the current commit. What is the safer command, and why?
