# Chapter 71 solutions

## Level 1
**1.1** A package is software packaged for installation by a tool; a registry is the place where packages are stored and downloaded from; a package manager is the tool that installs them.

**1.2** Only `@ada/wordcount`: GitHub's npm registry supports only scoped names, and names and scopes must be lowercase.

## Level 2
**2.1** `package.json` with `"name": "@ada/wordcount"` and `.npmrc` with the line `@ada:registry=https://npm.pkg.github.com`, then `git add package.json .npmrc` and `git commit`.

**2.2** For example `printf '//npm.pkg.github.com/:_authToken=not-a-real-token\n' > ~/.npmrc`, and then `git grep -n '_authToken' || echo "no token in the repository"` prints the message.

## Level 3
**3.1** For example: `if git grep -q '_authToken'; then echo "token found"; exit 1; fi`.

**3.2** Granular: the package belongs to an account or organization and has its own access and visibility, so you can publish without a repository. Repository-scoped: the package inherits the repository's permissions and visibility, so there is one place to manage access.

## Level 4
**4.1** A sensible design: trigger on a tag push (or a published release) on the default branch; authenticate with the workflow's short-lived `GITHUB_TOKEN` with only the permission needed to write packages; require review and protect the branch so only reviewed changes alter the workflow; pin any third-party action to a commit; risks include publishing from the wrong tag, a compromised action, and publishing secrets inside the package.

## Level 5
**5.1** A package inherits a repository's permissions automatically only if the repository is linked before publishing; linking later from the package settings leaves the existing permissions unchanged.

**5.2** Revoke the token first; create a new one with the fewest scopes; remove it from the file and from history if you wish (Chapter 33<!--ref:gitsec-->), move the token to a user-level file or a workflow secret; check where else it was used.
