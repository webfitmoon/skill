import json
import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "analyze_terms.py"
FIXTURE = Path(__file__).parent / "fixtures" / "draft.md"


class AnalyzeTermsTest(unittest.TestCase):
    def test_counts_priority_terms_compounds_and_competitors(self):
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(FIXTURE),
                "--keyword",
                "작가 홈페이지 제작",
                "--top",
                "5",
            ],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        result = json.loads(completed.stdout)

        self.assertEqual(result["priority_terms"]["작가"], 3)
        self.assertEqual(result["priority_terms"]["홈페이지"], 3)
        self.assertEqual(result["priority_terms"]["제작"], 2)
        self.assertEqual(result["priority_compounds"]["작가 홈페이지"], 2)
        self.assertEqual(result["priority_compounds"]["홈페이지 제작"], 2)
        self.assertIn("활동", result["top_other_terms"])


if __name__ == "__main__":
    unittest.main()

