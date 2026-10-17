# Submission package

## Public resources

| Material | Location |
| --- | --- |
| Working prototype | [Creative Pulse](https://creative.segpulse.cn/) |
| Demonstration video | [Google Drive video](https://drive.google.com/file/d/1m5DuoPHrOL2D1xbw7a2gBtiSbTjlrpa1/view?usp=sharing) |
| Repository | [creative-pulse](https://github.com/xiaojiu1414/creative-pulse) |

The pitch deck is supplied as a separate competition artifact. Dedicated
evaluator credentials are provided through the restricted submission access
instructions.

## Project description

Creative Pulse helps brand teams, creators, and agencies review video and
image-text creatives before publication. Format-specific reports connect
judgments and revision recommendations to source evidence. Reviewers can
compare selected creatives with pulse and explore campaign-level content
patterns.

The deck describes Next.js and FastAPI for the review experience, Dagster for
asynchronous orchestration, Qwen 3.5 Omni for generative reasoning, Kaggle GPU
tasks for auxiliary measurement, Tencent COS for media and results, and
PostgreSQL for application state. Google Cloud migration is listed as future
development.

## Supporting documentation

- [Product overview](product-overview.md)
- [Architecture](architecture.md)
- [Evaluator walkthrough](evaluator-guide.md)
- [Deployment and integrations](google-cloud-integration.md)
- [Scaffold validation](validation-report.md)

## Public repository boundary

This companion provides an upper-layer scaffold and product documentation.
Product implementations, internal instructions, account details, and the
credential-bearing deck are kept outside the published files.
