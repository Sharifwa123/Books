# Chapter 61 solutions

## Level 1
**1.1** Checks (detailed; created by GitHub Apps including Actions) and commit statuses (simple; created by external services and integrations).

**1.2** Checks.

## Level 2
**2.1** Yes: GitHub's documentation says required status checks can be checks or commit statuses, so a result from any system that reports it through the API can be required.

**2.2** The checks can be run on your own computer and the CI system can be replaced by rewriting a short configuration file.

## Level 3
**3.1** Answers depend on your system. A good answer states where the code runs, the cost model, the operating systems available and how secrets are scoped, each with a link to current documentation.

## Level 4
**4.1** For example: Which operating systems do we need? What will it cost for our usage? Where will secrets live? Which of our pipeline steps are scripts and which are service-specific? How do we report results to pull requests and which checks are required?

## Level 5
**5.1** Check that the external system reports a status with exactly the required name, and that it reports for the commit of the pull request's head. Also check that the integration has the permission to set statuses.
