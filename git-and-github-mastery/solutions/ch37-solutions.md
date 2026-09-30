# Chapter 37 solutions

## Level 1
**1.1** Answers vary. A good answer chooses an address that will last and can be read, and a username that is neutral and professional.

**1.2** Both. Git writes the name and the email into every commit as text.

## Level 2
**2.1** Usually fine, if you choose: favourite language, your employer (if allowed), a general location. Usually not: your phone number and precise home details. A photo is your choice; consider who can see it.

**2.2** `https://github.com/ada-bakes/sunrise-bakery` (or the same with `.git` at the end when used as a Git address).

## Level 3
**3.1** Use the address that you are willing to publish. The risk of the other is that it appears in every public commit and stays in history (Chapter 30<!--ref:objects-->). The platform may offer a special no-reply address (unverified, Chapter 38<!--ref:ghauth-->).

**3.2** Answers vary: pin complete, well-described work that shows different skills.

## Level 4
**4.1** For example: separate accounts (or clearly separated identities) as the employer allows; separate email addresses; set `user.email` per repository with `git config` inside work repositories (Chapter 14<!--ref:config--> showed the scopes); never mix credentials; follow the employer's rules.

## Level 5
**5.1** Commits are permanent and identified by their contents, including the email (Chapter 30<!--ref:objects-->), so changing it means rewriting history and force-pushing, and copies elsewhere remain (Chapter 33<!--ref:gitsec-->). Set `user.email` before the first public commit.

**5.2** The email in the commits does not match a confirmed email address on the account, so the platform cannot link them (unverified).

**5.3** The graph counts platform activity by its own rules and says nothing about quality; the learner can point to what the repositories contain and their descriptions instead.
