"""Check an exact public-file allowlist, local links, and common credential patterns."""
import json
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
allowed = set(json.loads((root / 'PUBLIC_FILES.json').read_text(encoding='utf-8'))['files'])
skip = {'.git', '__pycache__', '.venv'}
patterns = {
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'GitHub credential': re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{25,}\b'),
    'cloud credential': re.compile(r'\b(?:AKIA|ASIA|AKID)[A-Za-z0-9]{16,}\b'),
    'Google credential': re.compile(r'\bAIza[A-Za-z0-9_-]{30,}\b'),
}
present = set()
errors = []
for path in root.rglob('*'):
    relative = path.relative_to(root)
    if not path.is_file() or any(part in skip for part in relative.parts):
        continue
    name = relative.as_posix()
    present.add(name)
    if name not in allowed:
        errors.append(f'File outside approved publication scope: {name}')
        continue
    if path.stat().st_size > 25000:
        errors.append(f'Unexpected file size: {name}')
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'Unexpected binary file: {name}')
        continue
    for label, pattern in patterns.items():
        if pattern.search(text): errors.append(f'{label}: {name}')
    if path.suffix == '.md':
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            local = target.split('#', 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f'Broken local link: {name}')
for missing in sorted(allowed - present):
    errors.append(f'Approved file missing: {missing}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'Publication checks passed: {len(allowed)} explicitly approved files.')
print('This check does not certify the separately deployed product.')
