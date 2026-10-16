# Creative Pulse

**Creative content review with traceable findings.**

Creative Pulse helps content teams inspect and compare video and image-text
creatives before publication. This repository is the public submission companion
for **AI Builder Cup 2026 — Media, Content & Digital Experiences**.

## Publication scope

This repository provides a high-level service scaffold and evaluator documentation.
The product's analysis and reasoning implementation is maintained separately.
There is no product inference code, model configuration, internal instruction
text, training material, or application source snapshot in this repository.

Evaluate the actual product using the hosted prototype and demonstration video.
This scaffold cannot reproduce Creative Pulse's analysis or recommendations.

## Submission links

| Artifact | Status |
| --- | --- |
| Repository | [creative-pulse](https://github.com/xiaojiu1414/creative-pulse) |
| Evaluation prototype | URL pending |
| Dedicated judge account | Pending; see [access instructions](docs/evaluator-access.md) |
| 3–4 minute demo video | Link pending |
| Pitch deck in the prescribed template | Link pending |

## Repository contents

```text
app.py                       Local HTTP entry scaffold
backend.py                   Abstract service boundary; no connected implementation
docs/                        Product overview, architecture, access and evaluation guides
tests/test_scaffold.py       HTTP contract checks for the scaffold
scripts/check_publication.py Checks the explicit public-file allowlist and local links
PUBLIC_FILES.json            Exact list of files approved for this release
```

## Run the scaffold

Python 3.12+ is sufficient. No third-party dependencies, cloud credentials, GPU,
or external API calls are required.

```bash
python3 app.py
```

Open `http://127.0.0.1:8080/healthz`. The health response explicitly identifies
this service as a scaffold. `POST /api/reviews` accepts an `asset_reference`
field but returns **501 / backend_not_included** with the default adapter.
It never substitutes fabricated analysis results for the separate service.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_publication.py
```

The files above demonstrate the application boundary. They are not the
functional prototype required by the competition.

## Evaluation documentation

- [High-level architecture](docs/architecture.md)
- [Evaluator walkthrough](docs/evaluator-guide.md)
- [Dedicated judge access](docs/evaluator-access.md)
- [Google integration status](docs/google-cloud-integration.md)
- [Submission checklist](docs/submission-checklist.md)
- [Publication scope](docs/publication-scope.md)
- [Scaffold validation](docs/validation-report.md)
