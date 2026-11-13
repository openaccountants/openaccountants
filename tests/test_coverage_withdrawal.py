"""Committed country withdrawals require the exclusion decision and exact old blobs."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("withdrawal_integrity", ROOT / "scripts/check-sync-integrity.py")
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)

class WithdrawalTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(tmp.name).resolve()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Fixture maintainer")
        self.git("config", "user.email", "fixture@example.test")
        self.path = "skills/venezuela/fixture.md"
        self.write(self.path, "---\nname: fixture\njurisdiction: VE\ntier: 2\nlast_updated: 2026-11-12\nversion: 1.0\n---\n\n# Fixture\n")
        self.base = self.commit("base")
        self.blob = self.git("rev-parse", self.base + ":" + self.path).strip()
        (self.repo / self.path).unlink()
        self.entry = {"code": "VE", "folder": "venezuela", "decided_by": "Fixture maintainer",
                      "decided_on": "2026-11-12", "reason": "Explicit whole-country coverage withdrawal",
                      "files": [{"path": self.path, "previous_blob": self.blob}]}
        self.write("scripts/data/sanctioned.yml", "countries:\n  - code: VE\n    folder: venezuela\n")
        self.save_manifest()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, capture_output=True, text=True, check=True).stdout

    def write(self, path, text):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", message)
        return self.git("rev-parse", "HEAD").strip()

    def save_manifest(self):
        self.write("docs/coverage-withdrawals.json", json.dumps({"withdrawals": [self.entry]}))

    def audit(self, mode="audit", committed=True):
        head = self.commit("withdraw") if committed else None
        findings, count = check.run_integrity_check(self.repo, self.base, head, mode, strict_metadata=True)
        self.assertEqual(count, 1)
        return findings

    def assert_blocked(self, **kwargs):
        self.assertIn("source-removal-needs-review", {f.code for f in self.audit(**kwargs) if f.severity == "error"})

    def test_exact_committed_withdrawal_is_a_review_notice(self):
        findings = self.audit()
        self.assertEqual({f.code for f in findings}, {"declared-coverage-withdrawal"})
        self.assertEqual({f.severity for f in findings}, {"notice"})

    def test_exporter_sync_never_gets_the_audit_exception(self):
        self.assert_blocked(mode="sync")

    def test_uncommitted_deletion_still_requires_review(self):
        self.assert_blocked(committed=False)

    def test_wrong_old_blob_is_blocked(self):
        self.entry["files"][0]["previous_blob"] = "0" * 40
        self.save_manifest()
        self.assert_blocked()

    def test_country_not_excluded_is_blocked(self):
        self.write("scripts/data/sanctioned.yml", "countries: []\n")
        self.assert_blocked()

    def test_missing_decision_is_blocked(self):
        del self.entry["decided_by"]
        self.save_manifest()
        self.assert_blocked()

    def test_invalid_decision_date_is_blocked(self):
        self.entry["decided_on"] = "later"
        self.save_manifest()
        self.assert_blocked()

    def test_unlisted_file_is_blocked(self):
        self.entry["files"] = []
        self.save_manifest()
        self.assert_blocked()

    def test_duplicate_file_entries_are_blocked(self):
        self.entry["files"] *= 2
        self.save_manifest()
        self.assert_blocked()

    def test_malformed_manifest_is_blocked(self):
        self.write("docs/coverage-withdrawals.json", "not JSON")
        self.assert_blocked()

    def test_rename_is_still_blocked(self):
        self.write("skills/other/renamed.md", self.git("show", self.base + ":" + self.path))
        self.assert_blocked()

if __name__ == "__main__":
    unittest.main()
