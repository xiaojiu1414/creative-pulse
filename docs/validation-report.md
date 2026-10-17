# Scaffold validation

## Service checks

The five local service tests cover:

- An explicitly labeled scaffold health response.
- The 501 response for an unconfigured backend.
- Rejection of malformed input.
- An unknown route.
- Rejection of an oversized request.

All five tests passed on October 16, 2026. The executable scaffold and test
sources are unchanged by the October 17 documentation update.

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_publication.py
```

The publication check covers the exact 15-file allowlist, local Markdown links,
and common credential patterns.

## Public resource checks

On October 17, 2026, anonymous HTTP requests returned:

| Resource | Observed response |
| --- | --- |
| Prototype entry | HTTP 200 at the Creative Pulse login screen |
| Demonstration-video share page | HTTP 200 at the Google Drive file viewer |

These observations cover the public entry pages. Local scaffold tests describe
HTTP behavior, not model performance or product benchmark results.
