# Appendix J — Deployment Checklist

Companion to Chapter 72<!--ref:deploy-->. A deployment is a change to a system that people use; treat it with more care than a commit.

## J.1 Before

- [ ] The exact commit to deploy has passed the pipeline (tests and checks), and it is the same artifact that was tried on staging.
- [ ] The artifact is versioned and reproducible (a tag; Chapter 66<!--ref:releases-->); it has a checksum.
- [ ] I know how to **roll back**, and I have practised it (Chapter 72<!--ref:deploy-->).
- [ ] Database or data changes are planned to work with both the old and the new version.
- [ ] Deployment secrets are environment secrets with least privilege, short-lived where possible (Chapter 60<!--ref:wfsec-->).
- [ ] Approval is required for production (an environment protection rule; Chapter 58<!--ref:wfadvanced-->).
- [ ] Someone is available to watch and to react.

## J.2 During

- [ ] Deploy to a new folder or instance; switch only when it is ready (release directories; Chapter 72<!--ref:deploy-->).
- [ ] Run a health check right after the switch.
- [ ] Watch logs and errors for the agreed time.

## J.3 After

- [ ] If the check fails: roll back first, investigate second.
- [ ] Record what was deployed, when, and by whom (the release, the run, the approval).
- [ ] Keep the previous release for the agreed time, then clean up.
- [ ] Write down anything that surprised you.

## J.4 Static sites (Chapter 69<!--ref:pages-->)

- [ ] No `http://` references; no root-absolute paths on a project site; `.nojekyll` if the files need no build.
- [ ] Nothing sensitive in the site or in what it links to.
- [ ] Custom domain records copied from the current documentation; HTTPS enforced.
