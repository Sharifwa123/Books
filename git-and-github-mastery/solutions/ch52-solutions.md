# Chapter 52 solutions

## Level 1
**1.1** CI: committing often to a shared repository and having every change built and tested automatically. CD: using automation to publish and deploy software updates, usually after building and testing.

**1.2** For example: `if grep -q "$(printf '\t')" menu.md; then echo FAIL; exit 1; fi; echo PASS`. On a clean file the exit code is 0.

## Level 2
**2.1** A line such as `- Coffee: two pounds` is printed and the script stops with exit code 1.

**2.2** The `exit 1` in the failing stage ends the script, so later stages do not run.

## Level 3
**3.1** Cheap, fast checks (such as a line-length lint) go first, so mistakes are reported quickly.

**3.2** `false && echo yes` prints nothing (the first command failed, so the second is skipped); `true && echo yes` prints `yes`. A shell continues a chain only after success, which is the same idea as stopping a pipeline at the first failed stage.

## Level 4
**4.1** For example: lint (HTML validator, no errors), test (links resolve, form has required fields), build (produce the site folder), deploy (publish the folder), each failing on a non-zero exit code.

## Level 5
**5.1** Make the checks faster (run cheap checks first, cut what is not needed) and keep them trustworthy; a fast, reliable pipeline is waited for.

**5.2** A flaky check. It teaches people to ignore red, so real failures are missed.
