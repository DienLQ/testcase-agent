from pathlib import Path
import json
import unittest
ROOT=Path(__file__).resolve().parents[1]
class QualityTests(unittest.TestCase):
    def test_guides(self):
        for p in ['config/prd-reading-guide.md','config/quality-workflow.md','templates/analysis-template.md','templates/review-template.md']:
            self.assertTrue((ROOT/p).is_file())
    def test_pipeline(self):
        s=(ROOT/'config/testcase-workflow.md').read_text(encoding='utf-8')
        for v in ['V1.3 mandatory quality pipeline','Preflight ALL','<output-stem>.analysis.md','<output-stem>.review.md']:
            self.assertIn(v,s)
    def test_registry_supports_clean_skeleton(self):
        c=json.loads((ROOT/'config/features.json').read_text(encoding='utf-8'))
        self.assertEqual(c['features'], [])
        for f in c['features']:
            for k in ['prd_guide','prd_json']:
                if k not in f:
                    continue
                self.assertTrue((ROOT/f[k]).is_file())
    def test_safety(self):
        s=(ROOT/'config/prd-reading-guide.md').read_text(encoding='utf-8')
        self.assertIn('Do not decode base64',s)
        self.assertIn('PARTIAL',s)
    def test_models(self):
        s=(ROOT/'templates/analysis-template.md').read_text(encoding='utf-8')
        for v in ['State Transitions','Decision Rules','Partitions and Boundaries','Traceability']:
            self.assertIn(v,s)
    def test_review(self):
        self.assertIn('NOT independent validation',(ROOT/'templates/review-template.md').read_text(encoding='utf-8'))
if __name__=='__main__':
    unittest.main()
