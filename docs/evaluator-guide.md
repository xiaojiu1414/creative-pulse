# Evaluator guide

## Actual prototype

The final prototype URL, video, and dedicated judge account are pending. Complete
the [access instructions](evaluator-access.md) before submission.

Suggested walkthrough, to verify on the final deployment:

1. Open the supplied demo workspace containing demonstration media.
2. Open a completed creative review and inspect its findings and source locations.
3. Select multiple creatives and compare them using pulse.
4. Ask a follow-up about a possible revision and inspect the supporting findings.
5. Explore the campaign-level content overview.

Document the exact workspace, creative display names, permitted actions, and
reasonable input limits after checking this flow on the final evaluation URL.
Use content cleared for demonstration and do not expose customer data.

## Local repository

`app.py` is an HTTP scaffold, not the running product. Its default review route
returns 501 and no analysis output. Local checks establish only that the public
entry and unconfigured service boundary behave as documented.

## Availability

Keep the evaluation prototype, its dependencies, and repository accessible
throughout evaluation. A local scaffold test does not establish hosted uptime.
