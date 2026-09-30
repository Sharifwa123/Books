---
key: ghauth
number: 38
tag: Core
first_read: full
status: draft
requires: [ghaccount, gitsec]
ledger: [R232, R233, R234, R235, R236]
---
# Chapter 38 — Authentication in Depth [Core]

**In this chapter**

- how Git proves to a platform who you are: HTTPS or SSH
- SSH key pairs: making one, and what to protect
- tokens, credential managers and two-factor sign-in, in principle
- signing commits with an SSH key
- a checklist for a safe setup

> **How to read this chapter.** The **Git and SSH side** was run and tested: addresses, key generation, and signing. Everything that happens **on the platform's website** (adding a key to an account, creating a token, two-factor settings) is checked against GitHub's own documentation (the `github/docs` repository at commit `2eaab0b`, 29 September 2026), and was **not** run on a live account, so menus and buttons are described by their idea.

**Before you start.** Chapter 37<!--ref:ghaccount-->, Chapter 33<!--ref:gitsec-->, Chapter 32<!--ref:custom--> (credential helpers) and Chapter 6<!--ref:accounts-->. The recordings ran in Bash and zsh on Git 2.43.0 with OpenSSH 9.6 and were re-run in CI on Git 2.55.0.

---

## 38.1 Two questions

When Git talks to a hosted repository, two questions arise:

1. **Who are you?** (authentication)
2. **What may you do here?** (authorisation: can you read this repository, can you push to it?)

This chapter is about the first question. The second is settled by the repository's settings (Chapter 49<!--ref:collab-->).

**Authentication** (introduced in Chapter 6<!--ref:accounts-->) is proving who you are to a system, for example with a password, a key or a one-time code. **Authorisation**, by contrast, is what the system then allows you to do.

Git offers two ways to reach a hosted repository, and the difference shows in the address.

---

## 38.2 HTTPS or SSH

The same repository can have two kinds of address (Chapter 36<!--ref:whatgh--> introduced the first). Switching between them is one command:

```text
$ cd bakery-menu
$ git remote add origin https://github.com/example-owner/sunrise-bakery.git
$ git remote -v
origin	https://github.com/example-owner/sunrise-bakery.git (fetch)
origin	https://github.com/example-owner/sunrise-bakery.git (push)
```

*Recorded in Bash; `ch38-auth/expected-urls.bash.txt`.*

```text
$ git remote set-url origin git@github.com:example-owner/sunrise-bakery.git
$ git remote -v
origin	git@github.com:example-owner/sunrise-bakery.git (fetch)
origin	git@github.com:example-owner/sunrise-bakery.git (push)
$ git remote set-url origin https://github.com/example-owner/sunrise-bakery.git
$ git config --get remote.origin.url
https://github.com/example-owner/sunrise-bakery.git
```

*Recorded in Bash; `ch38-auth/expected-urls.bash.txt`.*

| | HTTPS address | SSH address |
|---|---|---|
| Looks like | `https://github.com/owner/repo.git` | `git@github.com:owner/repo.git` |
| You prove yourself with | a username with a token or password, usually stored by a credential helper | a **key pair** |
| Works through | ordinary web connections | the SSH protocol (some networks block it) |
| Good for | getting started; restricted networks | daily work once set up |

`git remote set-url` changes an address without touching anything else (Chapter 23<!--ref:remotes-->). Both forms reach the same repository.

> **Checked against GitHub's documentation (R232).** "About authentication to GitHub" says that you can reach repositories from the command line in two ways, HTTPS and SSH, and that "the method of authenticating is determined based on whether you choose an HTTPS or SSH remote URL". On HTTPS you "must authenticate with a personal access token": "when Git prompts you for your password, enter your personal access token", and "password-based authentication for Git has been removed in favor of more secure authentication methods". Unless you use a credential helper, Git prompts every time. HTTPS works "even if you are behind a firewall or proxy". Which method GitHub currently recommends first is not stated as one choice: the documentation offers both, and it may change.

---

## 38.3 SSH keys

An SSH **key pair** is two files that belong together, made by one command.

A **key pair** (Chapter 6<!--ref:accounts--> introduced the idea) is two linked cryptographic keys: a **private key**, which you keep secret, and a **public key**, which you can share freely. Something proved with the private key can be checked with the public key; the public key cannot practically be used to work out the private key.

Make a pair for the demonstration. `-t ed25519` chooses a modern key type, `-C` adds a label, `-f` names the file, and `-q` keeps the tool quiet. (`-N ""` sets **no passphrase**, *only* so that this recording can run without asking; see the caution below.)

```text
$ mkdir -p ~/.ssh
$ chmod 700 ~/.ssh
$ ssh-keygen -q -t ed25519 -f ~/.ssh/id_demo -N "" -C "ada@example.org"
$ ls ~/.ssh
id_demo  id_demo.pub
```

*Recorded in Bash; `ch38-auth/expected-ssh-key.bash.txt`.*

Two files: `id_demo` (private) and `id_demo.pub` (public). Look at their permissions, the first line of each, and the type:

```text
$ ls -l ~/.ssh/id_demo ~/.ssh/id_demo.pub | cut -c1-10
-rw-------
-rw-r--r--
$ head -n 1 ~/.ssh/id_demo | tr -d '-'
BEGIN OPENSSH PRIVATE KEY
$ cut -d' ' -f1,3 ~/.ssh/id_demo.pub
ssh-ed25519 ada@example.org
$ ssh-keygen -l -f ~/.ssh/id_demo.pub | cut -d' ' -f1,4
256 (ED25519)
```

*Recorded in Bash; `ch38-auth/expected-ssh-key.bash.txt`.*

- The private key is readable and writable **only by you** (`-rw-------`). The tool sets that, and SSH refuses to use a private key that other users can read.
- The private file's first line announces what it is: `BEGIN OPENSSH PRIVATE KEY` (the recording removes the dashes that surround it). Anyone who gets the whole file can pretend to be you. Because the block is so recognisable, automatic scanners look for that line, and this book's own checks reject it in the text.
- The public file is one line: the key type (`ssh-ed25519`), the key itself (not shown), and the label. That line is what you give to a service.
- The key is `256 (ED25519)`.

> **⚠️ CAUTION.** **Protect the private key with a passphrase** in real use: a passphrase encrypts the file, so that a stolen copy is useless without it. The demonstration used none, for convenience only. Never put a private key in a repository, an email or a chat (Chapter 33<!--ref:gitsec-->). If you think a private key was exposed, remove its public half from every service that trusts it, and make a new pair.

**On the platform.** To use the key you add the **public** line to your account's settings, and the platform then accepts connections that prove possession of the matching private key. A helper program called an *agent* can hold an unlocked key in memory for a while, so that you do not type the passphrase every time.

> **Checked against GitHub's documentation (R233).** To use SSH you generate a key pair, add the private key to the SSH agent, and add the **public** key to your account. The documentation's example generates an `ed25519` key, and says to use `rsa -b 4096` "if you are using a legacy system that doesn't support the Ed25519 algorithm"; hardware-backed `ed25519-sk` keys are covered too. To test: `ssh -T git@github.com`, check that the fingerprint matches GitHub's published one, and expect the reply "Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access." A key unused for a year is deleted automatically. How the agent is started differs by operating system; follow GitHub's current instructions for yours.

---

## 38.4 Tokens

A **token** is a long random string that works like a password for a program. Platforms use them so that you can give a tool limited access without giving away your account password.

> **New term: access token.** A secret string that a program presents instead of a password. It can be limited to certain actions and to a certain time, and can be revoked without changing the account password.

Good habits, whichever platform you use:

- Give a token **only the permissions it needs**, for **as short a time** as workable.
- Treat it as a password: never commit it (Chapter 33<!--ref:gitsec-->), never paste it into a shared place.
- If it leaks, **revoke it first** (Chapter 33<!--ref:gitsec-->).
- Let a credential helper store it, rather than typing it into every command. Chapter 32<!--ref:custom--> showed the mechanism, and warned that the simple `store` helper keeps it in **plain text**.

> **Checked against GitHub's documentation (R234).** "Managing your personal access tokens" says GitHub currently supports two types, **fine-grained** personal access tokens and **classic** ones, and recommends fine-grained tokens "whenever possible". A fine-grained token is limited to one user or organization, can be limited to specific repositories, and has specific permissions. Both types "are tied to the user who generated them". GitHub recommends setting an expiration, and after it a token "is automatically revoked"; an expired or revoked token cannot be restored. A valid token pushed to a public repository or gist "will be automatically revoked". Token names, limits and pages change; check the current page before creating one.

---

## 38.5 Credential managers

A **credential manager** is a credential helper (Chapter 32<!--ref:custom-->) that stores passwords and tokens in a protected place provided by the operating system, or asks you to sign in through a browser and then remembers the result. Installers for Git often include one.

> **Checked in part against GitHub's documentation (R235).** "Caching your GitHub credentials in Git" recommends two ways: the GitHub CLI (`gh auth login`, choosing HTTPS), and **Git Credential Manager**, which manages authentication "including 2FA" so that you need not create and store a token by hand, and which on macOS stores credentials in the keychain. Which helpers ship with Git for Windows, macOS and Linux, and how each stores secrets, was not tested here (Chapter 32<!--ref:custom--> lists the helpers in Git's own documentation).

---

## 38.6 Two-factor sign-in, passkeys and recovery

A password alone is the weakest form of protection: it can be guessed, stolen or reused. **Two-factor authentication** (2FA) asks for a second proof besides the password: a code from an app, a hardware key, or a device that you hold. **Passkeys** are a newer way to sign in with a key held by your device instead of a password.

- **Turn on 2FA before anything else** on an account that owns your code.
- **Keep the recovery codes** somewhere safe and *separate* from the device. Losing both the second factor and the codes can lock you out for good.
- Use a **password manager**, and a different password for every service (Chapter 6<!--ref:accounts-->).
- Never approve a sign-in prompt that you did not start.

> **Checked against GitHub's documentation (R236).** "About authentication to GitHub" lists the ways to sign in to the website: username and password (or a social login with Google or Apple), two-factor authentication, which it calls recommended, and a passkey. With 2FA on, you enter a code from a time-based one-time password (TOTP) app or one sent as a text message; you can add a security key or GitHub Mobile as further methods. A **passkey** gives "a secure, passwordless login" and "satisfies both password and 2FA requirements". GitHub asks you to keep recovery codes ("one-time codes for account recovery if you can't access your two-factor authentication method") and recommends "two or more authentication methods". The same page says GitHub recommends a password manager for the password.

---

## 38.7 Signing commits with an SSH key

Chapter 33<!--ref:gitsec--> signed a commit with GPG and said that Git can also sign with an SSH key. Here it is, using a demonstration key. The setup names the signing format, the key, and a file of **allowed signers** (who is allowed to sign, and with which public key), so that Git can *check* signatures too:

```text
$ cd bakery-menu
$ mkdir -p ~/.ssh
$ ssh-keygen -q -t ed25519 -f ~/.ssh/id_sign -N "" -C "ada@example.org"
$ printf 'ada@example.org %s\n' "$(cut -d' ' -f1,2 ~/.ssh/id_sign.pub)" > ~/.ssh/allowed_signers
$ git config gpg.format ssh
$ git config user.signingkey ~/.ssh/id_sign.pub
$ git config gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
```

*Recorded in Bash; `ch38-auth/expected-ssh-sign.bash.txt`.*

Then one signed commit and one unsigned commit:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -q -S -am "Add tea (signed with an SSH key)"
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -q -am "Add coffee (unsigned)"
```

*Recorded in Bash; `ch38-auth/expected-ssh-sign.bash.txt`.*

Ask Git for the result, using `%G?` again:

```text
$ git log --format='%G? %GS: %s' -3
N : Add coffee (unsigned)
G ada@example.org: Add tea (signed with an SSH key)
N : Add coconut cake
```

*Recorded in Bash; `ch38-auth/expected-ssh-sign.bash.txt`.*

`G` means that the signature is good and that the signer is in the allowed-signers file. `N` means no signature. Verify the signed commit explicitly:

```text
$ git verify-commit HEAD~1 2>&1 | sed 's/ with ED25519 key.*//; s/^Good "git" signature for/Good signature for/'
Good signature for ada@example.org
```

*Recorded in Bash; `ch38-auth/expected-ssh-sign.bash.txt`.*

(The recording removes the key's fingerprint from that line, because it is different for every key.)

**What a platform adds.** Hosting platforms can show a mark next to signed commits when they can match the signature to a key on an account. That mark says that *some key on the account* made the signature. It is not a certificate of good code.

> **Checked against GitHub's documentation (R236).** "About commit signature verification" says a commit or tag with a signature that is cryptographically verifiable, whether GPG, SSH or S/MIME, is marked "Verified" (or "Partially verified"); by default the statuses are Verified, Unverified and no status for an unsigned commit, and "vigilant mode" is off by default. It calls SSH signatures "the simplest to generate", and says you can even upload an existing authentication key to use as a signing key. A GPG key can expire or be revoked, which SSH does not offer. Once verified when pushed, a signature stays verified within the repository's network. As this chapter said above, the mark is about *who signed*; it does not say the code is good.

---

## 38.8 A checklist for a safe setup

1. Use a **unique, strong password** from a password manager, and **turn on 2FA**. Store the recovery codes safely.
2. Choose **SSH** (a key pair *with a passphrase*) or **HTTPS with a credential manager**; do not store tokens in plain text.
3. Give each token the **fewest permissions** and a **short life**.
4. Keep private keys and tokens **out of every repository** (Chapter 33<!--ref:gitsec-->).
5. Test the connection before you rely on it, following the platform's current guide.
6. **Revoke** anything that you no longer use, and anything that may have leaked.
7. Optionally, **sign your commits** (Chapter 33<!--ref:gitsec-->, section 38.7).

---

## Checkpoint

## What You Learned

- Authentication proves who you are; authorisation decides what you may do.
- A hosted repository has an HTTPS address and an SSH address; `git remote set-url` switches between them.
- An SSH key pair has a private key (secret, mode `-rw-------`) and a public key (shared); protect the private key with a passphrase.
- A token works like a password for programs; give it minimal permissions and a short life, and revoke it if it leaks.
- Two-factor sign-in, a password manager and stored recovery codes protect an account that owns your code.
- Git can sign commits with an SSH key and verify them with an allowed-signers file.

## New Vocabulary

- **Access token**: a secret string that a program presents instead of a password.

## Commands Learned

`git remote set-url`, `ssh-keygen -t ed25519`, `git config gpg.format ssh`, `git config user.signingkey`, `git config gpg.ssh.allowedSignersFile`, `git verify-commit`.

## Common Mistakes

1. **Creating a key without a passphrase and leaving it that way.**
2. **Committing a private key or a token.**
3. **Giving a token more permissions or a longer life than needed.**
4. **Turning on 2FA and losing the recovery codes.**
5. **Reading the "signed" mark as proof that the code is safe.**

## Practice

Do the exercises in [`exercises/ch38-exercises.md`](../../../exercises/ch38-exercises.md). Use only demonstration keys, and delete them afterwards.

## Self-Test

1. What is the difference between authentication and authorisation?
2. What does `git remote set-url` change?
3. Which of the two key files may be shared, and which must not be?
4. Why does SSH insist on `-rw-------` for the private key?
5. Why give a token few permissions and a short life?

## Before Moving On

You are ready for Chapter 39<!--ref:ghrepo--> if you can:

- [ ] tell an HTTPS address from an SSH address and switch between them
- [ ] make a key pair and say which file is secret
- [ ] name three habits that protect an account and its tokens
- [ ] sign a commit with an SSH key and read `%G?`

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| HTTPS and SSH address forms; `remote set-url` | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R232 |
| Key generation, file permissions, key type | Locally tested with OpenSSH 9.6 (CI: the runner's OpenSSH) | R233 |
| SSH commit signing and verification with an allowed-signers file | Locally tested (as above) | R236 |
| Tokens, credential managers, 2FA, passkeys, the platform's key settings and "Verified" marks | Checked against `github/docs` (commit `2eaab0b`); not run on a live account | R232-R236 |

## Where this leads

Chapter 39<!--ref:ghrepo--> creates your first repository and pushes to it, using one of the methods above. Chapter 60<!--ref:wfsec--> returns to tokens inside automation, and Chapter 62<!--ref:ghsec--> to the platform's own protections.
