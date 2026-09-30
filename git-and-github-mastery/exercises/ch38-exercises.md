# Chapter 38 exercises — Authentication in Depth

Attempt each exercise before you open `solutions/ch38-solutions.md`. Use only **demonstration keys** in a scratch folder, and delete them afterwards. OpenSSH must be installed (`ssh-keygen`).

## Level 1 — Guided

**1.1 Two addresses.** In a practice repository, add `https://github.com/example-owner/sunrise-bakery.git` as `origin`, then switch it to `git@github.com:example-owner/sunrise-bakery.git` with `git remote set-url`. Show both with `git remote -v`.

**1.2 Make a key.** Run `ssh-keygen -t ed25519 -f ./demo_key -C "demo"` and give a passphrase when asked. Which two files appeared?

## Level 2 — Partially guided

**2.1 Which is which?** Use `ls -l` on both files. Which has restricted permissions, and why?

**2.2 Read the public key.** Print the public file. Which parts does the line have, and which of the two files may you share?

## Level 3 — Independent

**3.1 Sign with SSH.** Configure `gpg.format ssh`, `user.signingkey` (the `.pub` file) and an allowed-signers file. Make one signed and one unsigned commit and compare them with `git log --format='%G? %s'`.

**3.2 Verify.** Run `git verify-commit` on the signed commit. What does it say?

## Level 4 — Professional scenario

**4.1 A leaked key.** A colleague pasted a private key into a public chat. Write the steps, in order, that they should take, and say what you would check afterwards.

**4.2 A token policy.** Write five rules for a small team about creating and using access tokens.

## Level 5 — Troubleshooting

**5.1** A learner says: "My SSH key works, so I do not need 2FA." Explain why that is wrong.

**5.2** `ssh` refuses a private key with the message that its permissions are too open. What should the learner do, and why does SSH care?

**5.3** A learner committed a token by mistake and wants to "just delete the file". What is the correct first step (Chapter 33<!--ref:gitsec-->)?
