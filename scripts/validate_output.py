#!/usr/bin/env python3
"""Optional structural check for the bundled STARTER template only; no AI/API calls."""
import argparse
from pathlib import Path
import re
import sys

COLUMNS = ['ID', 'Requirement / Source', 'Title', 'Type', 'Preconditions', 'Steps', 'Expected Result', 'Notes']
HEADINGS = ['# Test Cases', '## Metadata', '## Test Cases', '## Assumptions / Open Questions', '## Change Log']


def cells(line):
    return [part.strip() for part in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def validate(text):
    errors = []
    for heading in HEADINGS:
        if heading not in text.splitlines():
            errors.append('Missing heading: ' + heading)
    if 'Status: DRAFT - NOT VALIDATED' not in text:
        errors.append('Missing draft status')
    if re.search(r'\{\{.*?\}\}', text):
        errors.append('Unfilled template placeholders')
    section = text.split('## Test Cases', 1)[-1].split('\n## ', 1)[0]
    rows = [cells(line) for line in section.splitlines() if line.strip().startswith('|')]
    if not rows or rows[0] != COLUMNS:
        errors.append('Starter table header does not match')
    if len(rows) < 2 or any(not re.fullmatch(r':?-{3,}:?', c) for c in rows[1]) or len(rows[1]) != len(COLUMNS):
        errors.append('Missing or invalid table separator')
    cases = rows[2:] if len(rows) >= 2 else []
    if not cases:
        errors.append('No test cases')
    seen = set()
    for n, row in enumerate(cases, 1):
        if len(row) != len(COLUMNS):
            errors.append(f'Row {n}: expected {len(COLUMNS)} cells, got {len(row)}')
            continue
        if not re.fullmatch(r'TC-\d{3,}', row[0]):
            errors.append(f'Row {n}: invalid ID')
        if row[0] in seen:
            errors.append(f'Row {n}: duplicate ID {row[0]}')
        seen.add(row[0])
        if any(not value for value in row):
            errors.append(f'Row {n}: empty field; use TBD or N/A explicitly')
    return errors, len(cases)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        text = args.file.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 2
    errors, count = validate(text)
    if errors:
        print('STRUCTURE FAIL')
        for error in errors:
            print('- ' + error)
        return 1
    print(f'STRUCTURE PASS: {count} cases. Content correctness and coverage NOT checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
