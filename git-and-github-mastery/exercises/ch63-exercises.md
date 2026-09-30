# Chapter 63 exercises — Repository Security Practice

Attempt each exercise before you open `solutions/ch63-solutions.md`. Exercise 2.1 needs a Linux terminal (or `shasum -a 256` on macOS).

## Level 1 — Guided

**1.1 Levels.** Name the three levels at which Actions secrets can be stored and one use of each.

**1.2 Statuses.** What are the default commit signature statuses on GitHub?

## Level 2 — Partially guided

**2.1 A checksum.** Make a small file, compute its SHA-256, save it, verify it, change the file and verify again. What does the second check print?

**2.2 Which key?** List two advantages of a GitHub App token over a personal access token for a workflow.

## Level 3 — Independent

**3.1 A weak link.** Explain why publishing a checksum next to a download on the same page proves less than publishing an attestation.

**3.2 Signed but bad.** A commit is marked Verified. Give a reason it can still be a bad change.

## Level 4 — Professional scenario

**4.1 A production key.** A deployment needs a cloud credential. Decide where to store it, who may approve its use, and what else you would do to limit damage. Use the chapter.

## Level 5 — Troubleshooting

**5.1** A downloaded release fails its checksum. Give three possible causes and the first thing you do.

**5.2** A commit you signed shows Unverified. Give two things to check.
