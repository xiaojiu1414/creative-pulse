# Scaffold validation

This report covers the upper-layer scaffold only. It does not establish model
performance, product quality, Google integration, or hosted availability.

Verified on October 16, 2026: all five scaffold tests passed, and the publication
check passed for the 14 approved files.

Verification commands:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_publication.py
```

The five service checks cover an explicitly labeled health response, the 501
response for an unconfigured backend, malformed input, an unknown route, and
an oversized request. They require no network listener or external service.

The publication check enforces the exact approved file list, checks local
Markdown links, and looks for common credential patterns. Those checks do not
replace manual content review. Actual product evaluation is separate.
