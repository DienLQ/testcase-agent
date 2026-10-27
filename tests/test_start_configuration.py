"""Static package contract checks, NOT live command/model execution."""
from pathlib import Path
import json
import unittest
ROOT = Path(__file__).resolve().parents[1]
class StartConfigurationTests(unittest.TestCase):
    def test_registry_and_paths(self):
        config = json.loads((ROOT / 'config/features.json').read_text(encoding='utf-8'))
        self.assertEqual(config['version'], 1)
        self.assertIsInstance(config['features'], list)
        self.assertTrue((ROOT / 'templates/testcase-template.md').is_file())
        ids = set()
        for f in config['features']:
            self.assertRegex(f['id'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
            self.assertNotIn(f['id'], ids)
            ids.add(f['id'])
            self.assertIn('prd', f)
            for key in ['prd', 'srs', 'template', 'prd_guide', 'prd_json']:
                if key not in f:
                    continue
                path = Path(f[key])
                self.assertFalse(path.is_absolute())
                self.assertNotIn('..', path.parts)
                self.assertTrue((ROOT / path).is_file())
            for item in f.get('supporting_inputs', []):
                path = Path(item['path'])
                self.assertFalse(path.is_absolute())
                self.assertNotIn('..', path.parts)
                self.assertTrue((ROOT / path).is_file())

    def test_clean_skeleton_has_no_configured_feature(self):
        config = json.loads((ROOT / 'config/features.json').read_text(encoding='utf-8'))
        self.assertEqual(config['features'], [])
        self.assertFalse((ROOT / 'docs/shared/SRS.md').exists())
        feature_items = [p.name for p in (ROOT / 'docs/features').iterdir() if not p.name.startswith('.')]
        output_items = [p.name for p in (ROOT / 'output').iterdir() if not p.name.startswith('.')]
        self.assertEqual(feature_items, [])
        self.assertEqual(output_items, [])

    def test_agent_contract(self):
        adapter = (ROOT / '.github/agents/testcase.agent.md').read_text(encoding='utf-8')
        self.assertIn('config/testcase-workflow.md', adapter)
        text = (ROOT / 'config/testcase-workflow.md').read_text(encoding='utf-8')
        for marker in ['start <feature name>', 'config/features.json', 'test-cases-v001.md', 'PARTIAL', 'Concurrent generation is not supported']:
            self.assertIn(marker, text)
    def test_generic_prompt(self):
        text = (ROOT / 'prompts/01-generate-feature.md').read_text(encoding='utf-8')
        self.assertIn('start <feature-id>', text)
        self.assertNotIn('PRD:', text)
if __name__ == '__main__':
    unittest.main()
