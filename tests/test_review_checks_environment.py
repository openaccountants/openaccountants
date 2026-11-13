"""Run the real workflow check step against staged content, without GitHub or AI."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class ReviewChecksEnvironmentTests(unittest.TestCase):
    def test_staged_checks_report_findings_and_recompute_examples(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/skill-review.yml").read_text())
        steps = workflow["jobs"]["review"]["steps"]
        checkout = next(s for s in steps if s.get("uses", "").startswith("actions/checkout@"))
        self.assertIn("mcp", checkout["with"]["sparse-checkout"].split())
        staging = next(s for s in steps if s.get("name") == "Stage the PR as data")["run"]
        self.assertIn('cp -R skills library docs scripts mcp "$D/tree/"', staging)
        checks = next(s for s in steps if s.get("name", "").startswith("Mechanical checks"))["run"]
        with tempfile.TemporaryDirectory() as tmp:
            review = Path(tmp) / "oa-review"
            tree = review / "tree"
            for directory in ("scripts", "mcp"):
                shutil.copytree(ROOT / directory, tree / directory,
                                ignore=shutil.ignore_patterns("__pycache__", ".venv", "dist"))
            rel = "skills/us/states/al/al-sales-tax.md"
            target = tree / rel
            target.parent.mkdir(parents=True)
            # A real skill with a deliberately wrong result in PR data. Main
            # remains unchanged; neither the PR nor PYTHONPATH supplies code.
            target.write_text((ROOT / rel).read_text().replace("tax: 40.00", "tax: 41.00"))
            (review / "changed.txt").write_text(rel + "\n")
            env = {**os.environ, "RUNNER_TEMP": tmp, "GITHUB_WORKSPACE": str(ROOT),
                   "PYTHONPATH": "/untrusted/python/path"}
            result = subprocess.run(["bash", "-c", checks], cwd=ROOT, env=env,
                                    text=True, capture_output=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stderr)
            proposed = (review / "checks.txt").read_text()
            baseline = (review / "checks-main.txt").read_text()
            self.assertNotIn("Traceback", proposed + baseline)
            self.assertIn("tax_year_current", proposed)
            self.assertIn("1 failures", proposed)
            self.assertIn("(check-examples exit 1", proposed)
            self.assertIn("tax_year_current", baseline)


if __name__ == "__main__":
    unittest.main()
