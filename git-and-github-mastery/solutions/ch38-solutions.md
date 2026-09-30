# Chapter 38 solutions

## Level 1
**1.1** The first `remote -v` shows the `https://...` address twice (fetch and push); after `set-url` it shows `git@github.com:example-owner/sunrise-bakery.git` twice.

**1.2** `demo_key` (private) and `demo_key.pub` (public).

## Level 2
**2.1** The private key has `-rw-------` (only you can read and write it). If others could read it, they could impersonate you, so SSH refuses to use it.

**2.2** One line: the key type (`ssh-ed25519`), the key data, and the label. Only the `.pub` file may be shared.

## Level 3
**3.1** The signed commit shows `G` (good, signer in the allowed-signers file); the unsigned one shows `N`.

**3.2** It prints that the signature is good and names the signer's principal.

## Level 4
**4.1** 1) Remove the matching public key from every service that trusts it. 2) Create a new key pair (with a passphrase) and register the new public key. 3) Check the services' access logs for uses that were not theirs. 4) Tell the people who need to know. 5) Ask the chat's administrator to delete the message (a deleted message may already have been copied).

**4.2** Examples: give each token the fewest permissions; give it an expiry; one token per purpose; store tokens in a credential manager or a secret store, never in the repository; revoke tokens that are unused or exposed; review the list of tokens regularly.

## Level 5
**5.1** An SSH key proves possession of a file on one computer. If the account's password is stolen or phished, someone can sign in on the website and change keys or settings. 2FA protects the account itself.

**5.2** Restrict the permissions (for example `chmod 600 <keyfile>`). SSH refuses keys that others can read, because those keys are no longer secret.

**5.3** Revoke or rotate the token at its source first. Deleting the file leaves the token in history (Chapter 33<!--ref:gitsec-->).
