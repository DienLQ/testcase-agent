"""Static instruction/config contracts, not live retrieval or token tests."""
from pathlib import Path
import json
import unittest
ROOT = Path(__file__).resolve().parents[1]
class SelectiveSrsTests(unittest.TestCase):
    def setUp(self):
        self.text = (ROOT / 'config/testcase-workflow.md').read_text(encoding='utf-8')
    def test_old_full_read_removed(self):
        self.assertNotIn('Read the PRD, SRS and template using file tools.', self.text)
        self.assertNotIn('Read the existing output and original inputs first.', self.text)
    def test_budgets(self):
        for marker in ['Maximum 6 SRS search calls', 'At most 12 SRS range-read calls', '2400 requested SRS lines', '200 requested lines per call']:
            self.assertIn(marker, self.text)
    def test_bounded_fallback(self):
        self.assertIn('do not fall back to a whole-file read', self.text)
        self.assertIn('not included in the 2400-line', self.text)
    def test_mapping(self):
        cfg = json.loads((ROOT / 'config/features.json').read_text(encoding='utf-8'))
        for f in cfg['features']:
            for key in ['srs_sections', 'srs_keywords']:
                self.assertIsInstance(f[key], list)
                self.assertTrue(all(isinstance(x, str) and x.strip() for x in f[key]))
    def test_update_selective(self):
        update = self.text.split('# Workflow: update', 1)[1].split('# Boundaries', 1)[0]
        self.assertIn('Selective SRS retrieval', update)
    def test_template_metadata(self):
        template = (ROOT / 'templates/testcase-template.md').read_text(encoding='utf-8')
        self.assertIn('SRS sections and ranges read:', template)
        self.assertIn('Status: DRAFT - NOT VALIDATED', template)
    def test_fixed_template_companion(self):
        self.assertIn('<output-stem>.sources.md', self.text)
        self.assertIn('without changing template columns/headings', self.text)
    def test_no_token_guarantee(self):
        self.assertIn('NOT hard token limits', self.text)
        self.assertIn('never invent token usage', self.text)
if __name__ == '__main__':
    unittest.main()
