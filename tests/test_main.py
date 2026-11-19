import tempfile
import unittest
from pathlib import Path
from main import is_ignored, analyze

class DockerContextTests(unittest.TestCase):
    def test_negation_reincludes_file(self):
        patterns = ["*.log","!keep.log"]
        self.assertTrue(is_ignored("debug.log",patterns))
        self.assertFalse(is_ignored("keep.log",patterns))
    def test_analyzes_files_and_ignore_rules(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".dockerignore").write_text("*.tmp\n",encoding="utf-8")
            (root / "app.py").write_text("hello",encoding="utf-8")
            (root / "cache.tmp").write_text("ignored",encoding="utf-8")
            result = analyze(root)
            self.assertEqual(result["included_count"],2)
            self.assertIn("cache.tmp",result["ignored"])

if __name__ == "__main__":
    unittest.main()
