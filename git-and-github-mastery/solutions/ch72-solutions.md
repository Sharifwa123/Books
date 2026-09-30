# Chapter 72 solutions

## Level 1
**1.1** Trigger; build and test; package; approve; deploy; check; keep the previous version.

**1.2** Static website: copy files to a host. Container: build an image, push it to a registry and run it. VPS: copy files or a container and restart services on the server you administer.

## Level 2
**2.1** `mkdir -p server/releases/v1 server/releases/v2`, write a file in each, `ln -sfn releases/v1 server/current`, `cat server/current/index.txt`, then `ln -sfn releases/v2 server/current` and `cat` again.

**2.2** `ln -sfn releases/v1 server/current`, then `ls -1 server/releases` shows `v1` and `v2`.

## Level 3
**3.1** `grep -q Bakery server/current/index.txt && echo "health check: ok"`.

**3.2** Staging deploys automatically after tests pass; production needs an approval from a required reviewer, and may be limited to the default branch. The same artifact goes to both, so what was tested on staging is exactly what is released.

## Level 4
**4.1** For example: "This key can do everything, so a leak is a disaster; use the fewest permissions the deployment needs and, where possible, a short-lived credential. Store it as an environment secret so an approval gates its use. Never print it: log redaction is not guaranteed, and if it appears in a log we must delete the log and rotate the key."

## Level 5
**5.1** The design did not keep the previous version. Keep at least the previous release folder (and practise the rollback), and make clean-up scripts keep the release that is live and the one before it.

**5.2** Files can be switched back, but a database that has already been changed (columns removed, data converted) may not accept the old version's code. Plan database changes to work with both versions, or make them reversible.
