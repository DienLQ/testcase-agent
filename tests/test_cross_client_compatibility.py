"""Static contracts for the shared Copilot/Codex workflow and thin adapters."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents' / 'skills' / 'up-testcase'


class CrossClientCompatibilityTests(unittest.TestCase):
    def test_agents_md_routes_generation_only(self):
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('$up-testcase', text)
        self.assertIn('start <feature name>', text)
        self.assertIn('Do not invoke the generation workflow', text)
        self.assertIn('config/testcase-workflow.md', text)

    def test_both_adapters_load_one_shared_workflow(self):
        shared = ROOT / 'config' / 'testcase-workflow.md'
        self.assertTrue(shared.is_file())
        text = shared.read_text(encoding='utf-8')
        self.assertIn('single source of truth', text)
        self.assertIn('# Workflow: generate', text)
        self.assertIn('# Workflow: update', text)
        for adapter in [ROOT / '.github' / 'agents' / 'testcase.agent.md', SKILL / 'SKILL.md']:
            adapter_text = adapter.read_text(encoding='utf-8')
            self.assertIn('config/testcase-workflow.md', adapter_text)

    def test_skill_manifest_is_finished(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\nname: up-testcase\n'))
        self.assertNotIn('[TODO', text)
        self.assertIn('config/testcase-workflow.md', text)
        self.assertIn('selective-SRS', text)
        self.assertNotIn('.github/agents/testcase.agent.md` — canonical', text)

    def test_skill_ui_metadata(self):
        text = (SKILL / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
        self.assertIn('display_name: "UP Testcase"', text)
        self.assertIn('$up-testcase', text)

    def test_configured_structured_inputs_exist(self):
        config = json.loads((ROOT / 'config' / 'features.json').read_text(encoding='utf-8'))
        for feature in config['features']:
            self.assertTrue((ROOT / feature['prd_json']).is_file())
            for item in feature.get('supporting_inputs', []):
                self.assertTrue((ROOT / item['path']).is_file())

    def test_validator_uses_documented_name(self):
        self.assertTrue((ROOT / 'scripts' / 'validate_output.py').is_file())
        self.assertFalse((ROOT / 'scripts' / 'validate_ouput.py').exists())


if __name__ == '__main__':
    unittest.main()
