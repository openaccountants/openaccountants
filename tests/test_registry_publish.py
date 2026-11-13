"""Publication must use the exact approved file and the real hosted identity."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("registry_prepare", ROOT / "scripts/prepare-registry-publish.py")
prepare = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)


class RegistryPublishTests(unittest.TestCase):
    def setUp(self):
        self.source = json.loads((ROOT / "mcp/server.json").read_text())
        self.value = copy.deepcopy(self.source)
        self.value["description"] = "Tax skills with official sources and approval shown per skill."

    def validate(self, value, approved=None):
        raw = json.dumps(value) + "\n"
        return prepare.validate_manifest(raw, approved or hashlib.sha256(raw.encode()).hexdigest(), self.source)

    def test_accepts_approved_truthful_copy_without_another_version_constant(self):
        self.assertEqual(self.validate(self.value), self.value)

    def test_rejects_an_unapproved_file(self):
        with self.assertRaisesRegex(ValueError, "exact approved"):
            self.validate(self.value, "0" * 64)

    def test_rejects_an_invalid_approval_hash(self):
        with self.assertRaisesRegex(ValueError, "SHA256"):
            self.validate(self.value, "yes")

    def test_rejects_wrong_identity_version_endpoint_or_package(self):
        for key, value in [("name", "io.github.someone/other"), ("version", "wrong"), ("remotes", [{"type": "streamable-http", "url": "https://example.com"}]), ("packages", [{"identifier": "other"}]), ("repository", {"url": "https://example.com"})]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.validate({**self.value, key: value})

    def test_rejects_blank_overlong_or_banned_claims(self):
        for text in ["", " " * 3, "x" * 101, "Verified by licensed accountants", "CERTIFIED", "accountant-verified", "accountant–verified"]:
            with self.subTest(description=text), self.assertRaises(ValueError):
                self.validate({**self.value, "description": text})

    def test_publishing_stays_manual_on_founders_main_with_no_stored_secret(self):
        flow = yaml.safe_load((ROOT / ".github/workflows/publish-mcp-registry.yml").read_text())
        self.assertEqual(set(flow.get("on", flow.get(True))), {"workflow_dispatch"})
        job = flow["jobs"]["publish"]
        self.assertIn("github.ref == 'refs/heads/main'", job["if"])
        self.assertIn("github.actor == 'michaelcutajar1995'", job["if"])
        self.assertIn("github.repository == 'openaccountants/openaccountants'", job["if"])
        self.assertEqual(job["permissions"], {"contents": "read", "id-token": "write"})
        for step in job["steps"]:
            self.assertNotIn("${{ inputs.", step.get("run", ""))
        text = (ROOT / ".github/workflows/publish-mcp-registry.yml").read_text()
        self.assertNotIn("secrets.", text)


if __name__ == "__main__":
    unittest.main()
