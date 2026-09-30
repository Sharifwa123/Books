# Chapter 75 solutions

## Level 1
**1.1** In the `.github` folder of the repository, on the default branch.

**1.2** One username, package name or project name per external funding platform with up to four custom URLs; and one organisation plus up to four sponsored developers on GitHub Sponsors.

## Level 2
**2.1** For example: `github: [ada-example]`, `patreon: ada-example` and `custom: ["https://example.org/support"]`, written with `printf` into `.github/FUNDING.yml`, then `cat`.

**2.2** With PyYAML: `python3 -c "import yaml,sys; d=yaml.safe_load(open('.github/FUNDING.yml')); print({k:(len(v) if isinstance(v,list) else 1) for k,v in d.items()})"`.

## Level 3
**3.1** GitHub's own parser and rules are what matter, and a different tool may reject what one tool accepts. A tolerant parser does not prove the file is valid for GitHub.

**3.2** For example: `team` (a name), useful to write rulesets that require review by that team's owners; and `criticality` (low, medium, high), useful to write a stricter ruleset for high-criticality repositories. Properties are metadata that rulesets can target.

## Level 4
**4.1** For example: (1) A person is accountable for every change, whatever produced it. (2) Tell the reviewer when a tool produced a significant part. (3) Never put secrets or private data in prompts. (4) Do not submit what you cannot explain or have no right to submit. (5) The same tests and reviews apply to all changes.

## Level 5
**5.1** That the file is named `FUNDING.yml` and is in the `.github` folder on the default branch; that the sponsor button is enabled in the repository settings by someone with admin permissions; that the entries follow the documented syntax and limits.

**5.2** Do not install it yet. Read what it asks for, who publishes it and whether the publisher is verified, and ask whether a narrower option exists (least privilege).
