"""Static package contracts only; not semantic or live Copilot validation."""
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class PreconditionsTests(unittest.TestCase):
    def guide(self):
        return (ROOT/'config/preconditions-standard.md').read_text(encoding='utf-8')
    def test_agent_entry(self):
        s=(ROOT/'config/testcase-workflow.md').read_text(encoding='utf-8')
        self.assertIn('V1.6 two-question Preconditions contract',s)
        self.assertIn('config/preconditions-standard.md',s)
    def test_exact_two_questions(self):
        s=self.guide()
        for x in ['UP Content installation on ThinQ App:', 'Device firmware supporting the UP Content:']:
            self.assertIn(x,s)
        self.assertIn('exactly these two lines',s)
        self.assertIn('Do not add explanations or a third line inside Preconditions.',s)
    def test_allowed_decisions(self):
        s=self.guide()
        for x in ['Required', 'Not required', 'TBD']:
            self.assertIn(x,s)
        self.assertIn('Silence is not evidence for `Not required`.',s)
    def test_source_based_decisions(self):
        s=self.guide()
        self.assertIn('configured PRD, selectively retrieved SRS',s)
        self.assertIn('missing exact firmware version',s)
        self.assertIn('Never invent an installation mechanism, firmware version',s)
    def test_install_action_separation(self):
        self.assertIn('Installation case: UP Content is not installed initially',self.guide())
    def test_setting_action_separation(self):
        self.assertIn('Setting-change case: establish/verify the initial value',self.guide())
    def test_negative_state(self):
        self.assertIn('Negative case: preserve Off, not-installed, unsupported, locked, error',self.guide())
    def test_no_invented_navigation(self):
        self.assertIn('Do not use `same as above`',self.guide())
    def test_readiness(self):
        self.assertIn('SETUP-CLARIFICATION-REQUIRED',self.guide())
        self.assertIn('READY-FOR-HUMAN-REVIEW',self.guide())
    def test_analysis_mapping(self):
        s=(ROOT/'templates/analysis-template.md').read_text(encoding='utf-8')
        self.assertIn('Per-case Setup Readiness',s)
        self.assertIn('UP Content installation decision',s)
        self.assertIn('Supported-firmware decision',s)
        self.assertIn('Decision evidence',s)
    def test_review_gate(self):
        s=(ROOT/'templates/review-template.md').read_text(encoding='utf-8')
        self.assertIn('Preconditions Gate',s)
        self.assertIn('Exactly two Preconditions entries',s)
        self.assertIn('Supported-firmware decision is source-supported',s)
    def test_template_unchanged(self):
        import hashlib
        content=(ROOT/'templates/testcase-template.md').read_bytes().replace(b'\r\n',b'\n')
        self.assertEqual(hashlib.sha256(content).hexdigest(), 'a1104f44017950e31ff1e9f766a3b75644561419addf88535e32afa9359f32f0')
    def test_migration_preserves_input(self):
        s=(ROOT/'docs/UPGRADE-V1.4.md').read_text(encoding='utf-8')
        self.assertIn('MERGE',s)
        self.assertIn('No new columns',s)
    def test_v16_migration(self):
        s=(ROOT/'docs/UPGRADE-V1.6.md').read_text(encoding='utf-8')
        self.assertIn('MERGE',s)
        self.assertIn('exactly two lines',s)
        self.assertIn('Silence never proves `Not required`',s)
    def test_examples_labelled(self):
        s=(ROOT/'examples/preconditions-fictional.md').read_text(encoding='utf-8')
        self.assertIn('synthetic examples',s)
        self.assertIn('NOT ThinQ navigation',s)
        self.assertIn('UP Content installation on ThinQ App: Not required',s)
        self.assertIn('Device firmware supporting the UP Content: TBD',s)
if __name__=='__main__':
    unittest.main()
