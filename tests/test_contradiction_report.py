from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "detect-contradictions.py"
SPEC = importlib.util.spec_from_file_location("detect_contradictions", SCRIPT_PATH)
assert SPEC and SPEC.loader
detect_contradictions = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(detect_contradictions)


class ContradictionReportTests(unittest.TestCase):
    def test_jurisdiction_has_no_empty_duplicate_heading(self) -> None:
        report = detect_contradictions.render_report({"US": ([], [], [], {})})
        headings = [line for line in report.splitlines() if line.startswith("## ")]

        self.assertEqual(
            headings,
            [
                "## US — HIGH confidence (0)",
                "## US — MEDIUM confidence (0)",
                "## US — Copy drift (skills/ vs packages/) (0)",
                "## US — Stats",
            ],
        )


if __name__ == "__main__":
    unittest.main()
