# Creative Pulse

**From Content to Creative Decisions.**

Creative Pulse helps brand teams, creators, and agencies understand what a
creative communicates, inspect the evidence behind a judgment, and decide what
to revise before publication. It supports video and image-text content,
source-linked reports, multi-creative comparison with pulse, and campaign-level
content exploration.

This is the public submission companion for **SegPulse** in the
**AI Builder Cup 2026 — Media, Content & Digital Experiences** track.

## Explore the product

| Resource | Link |
| --- | --- |
| Working prototype | [creative.segpulse.cn](https://creative.segpulse.cn/) |
| Demonstration video | [Watch on Google Drive](https://drive.google.com/file/d/1m5DuoPHrOL2D1xbw7a2gBtiSbTjlrpa1/view?usp=sharing) |
| Submission repository | [creative-pulse](https://github.com/xiaojiu1414/creative-pulse) |

The prototype opens at a login screen. Evaluators can use the dedicated account
supplied privately with the competition submission, then follow the
[product walkthrough](docs/evaluator-guide.md). The pitch deck is distributed
separately because it contains restricted account details.

## Review workflow

- Inspect format-specific judgments and their source frames, moments, images,
  and text.
- Compare selected creatives and ask follow-up questions in pulse.
- Explore campaign themes, term associations, and related creatives.
- Use the supporting evidence to discuss specific revision decisions.

See the [product overview](docs/product-overview.md) and
[architecture](docs/architecture.md).

## Publication scope

This repository contains an upper-layer HTTP scaffold and evaluator
documentation. The product analysis and reasoning service is maintained
separately. The scaffold cannot reproduce Creative Pulse's analysis or
recommendations; the hosted prototype and video demonstrate the product.

The [publication boundary](docs/publication-scope.md) keeps product internals
and access secrets outside the release. `PUBLIC_FILES.json` lists the approved
files.

## Run the scaffold

Python 3.12+ is sufficient. No third-party dependencies, cloud credentials, GPU,
or external API calls are required.

```bash
python3 app.py
```

Open `http://127.0.0.1:8080/healthz`. The health response identifies the service
as a scaffold. `POST /api/reviews` accepts an `asset_reference` field and returns
**501 / backend_not_included** with the default adapter.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_publication.py
```

## Documentation

- [Product overview](docs/product-overview.md)
- [Architecture](docs/architecture.md)
- [Evaluator walkthrough](docs/evaluator-guide.md)
- [Dedicated evaluator access](docs/evaluator-access.md)
- [Deployment and integrations](docs/google-cloud-integration.md)
- [Submission package](docs/submission-checklist.md)
- [Publication scope](docs/publication-scope.md)
- [Scaffold validation](docs/validation-report.md)
