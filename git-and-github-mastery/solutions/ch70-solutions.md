# Chapter 70 solutions

## Level 1
**1.1** A codespace is a development environment hosted in the cloud, in a container on a virtual machine. Configuration as code means the environment is described by files committed to the repository, so everyone who creates a codespace gets the same setup.

**1.2** In `.devcontainer/devcontainer.json` (or `.devcontainer.json` in the root). A second configuration goes in its own subfolder: `.devcontainer/SUBDIRECTORY/devcontainer.json`.

## Level 2
**2.1** For example `git add .devcontainer && git commit -m "Add dev container"`, then `git ls-files` lists `.devcontainer/devcontainer.json`.

**2.2** `python3 -m json.tool` reports an error, because strict JSON does not allow comments. The chapter says the documentation's examples are `jsonc` (JSON with comments) and dev container tools accept them, so remove the comments to check with a strict tool or use a `jsonc`-aware tool.

## Level 3
**3.1** In the file: the linter and the language version (everyone needs them). In your own settings, dotfiles or Settings Sync: the colour theme and the shell aliases.

**3.2** For example: "Stop codespaces you are not using, delete the ones you no longer need, push your work before deleting, and remember that a codespace times out after 30 minutes of inactivity by default, but that it still exists until it is deleted. Check the billing page for the quota."

## Level 4
**4.1** A sensible proposal: a `.devcontainer/devcontainer.json` using an image (or a Dockerfile), a `postCreateCommand` that installs dependencies, and only shared tools. Test first by creating a codespace from a clean branch. Cautions: no secrets in the file, only trusted repositories, forwarded ports private, and a note that the configuration is reviewed like code.

## Level 5
**5.1** Commit and push your work to the remote repository (or publish it to a new one) before deleting; work in a deleted codespace is deleted too.

**5.2** Anyone on the internet can reach a public forwarded port without authentication. It reverts to private when the port is removed and re-added, or when the codespace restarts; organization owners can also restrict public ports.
