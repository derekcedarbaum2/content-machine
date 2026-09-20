import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "scripts/validate.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class DistributionTests(unittest.TestCase):
    def test_shipped_plugin(self):
        self.assertEqual(module.validate(ROOT), [])

    def test_missing_skill_and_broken_link_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("skills", "templates", ".claude-plugin"):
                shutil.copytree(ROOT / folder, root / folder)
            (root / "skills/draft/SKILL.md").unlink()
            (root / "README.md").write_text("[missing](missing.md)\n")
            errors = module.validate(root)
            self.assertTrue(any("Missing skill: draft" in e for e in errors))
            self.assertTrue(any("missing.md" in e for e in errors))
