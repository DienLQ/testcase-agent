"""Hand-authored structural fixtures; not agent-generated product test cases."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_output.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

def fixture():
    return """# Test Cases
## Metadata
- Status: DRAFT - NOT VALIDATED
## Test Cases
| ID | Requirement / Source | Title | Type | Preconditions | Steps | Expected Result | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TC-001 | REQ-001 | Sample case | Positive | Ready | Act | Result | N/A |
## Assumptions / Open Questions
- None
## Change Log
- Fixture
"""

class ValidatorTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(v.validate(fixture()), ([], 1))
    def test_empty(self):
        self.assertTrue(v.validate('')[0])
    def test_duplicate(self):
        row = '| TC-001 | REQ-001 | Sample case | Positive | Ready | Act | Result | N/A |'
        self.assertTrue(any('duplicate' in e for e in v.validate(fixture().replace(row, row+'\n'+row))[0]))
    def test_placeholder(self):
        self.assertTrue(any('placeholder' in e for e in v.validate(fixture()+'\n{{todo}}')[0]))
    def test_empty_cell(self):
        self.assertTrue(any('empty field' in e for e in v.validate(fixture().replace('| Ready |', '|  |'))[0]))
    def test_escaped_pipe(self):
        self.assertEqual(v.validate(fixture().replace('REQ-001', r'REQ \| 001'))[0], [])
    def test_missing_heading(self):
        self.assertTrue(v.validate(fixture().replace('## Change Log', 'Changes'))[0])
    def test_no_cases(self):
        self.assertTrue(any('No test cases' in e for e in v.validate('\n'.join(l for l in fixture().splitlines() if not l.startswith('| TC-')))[0]))
    def test_bad_id(self):
        self.assertTrue(any('invalid ID' in e for e in v.validate(fixture().replace('TC-001', 'CASE1'))[0]))
    def test_bad_separator(self):
        self.assertTrue(any('separator' in e for e in v.validate(fixture().replace('| --- |', '| x |', 1))[0]))

if __name__ == '__main__':
    unittest.main()
