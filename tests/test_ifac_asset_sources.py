"""Issuer-linked IFAC assets are official audit sources, not all Azure blobs."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts"))
import domains
import skill_checks


ASSET = "https://ifacweb.blob.core.windows.net/publicfiles/2023-10/IAASB-2022-Handbook-Volume-1.pdf"
PATH = "skills/kenya/audit-quality-assurance-aqa.md"
FM = {"jurisdiction": "KE", "domain": "audit-assurance"}


def source(url):
    return "## Sources\n\n| Source | URL | Read on |\n|---|---|---|\n| ISA 220 (Revised), paragraphs 13-41 | " + url + " | 2026-11-14 |\n"


class IfacAssetSources(unittest.TestCase):
    def test_issuer_linked_asset_passes_audit_source_admission(self):
        text = source(ASSET)
        self.assertTrue(domains.host_is_official(domains.url_host(ASSET), "audit-assurance"))
        self.assertEqual(skill_checks.check_source_hosts(PATH, text, FM), [])
        self.assertEqual(skill_checks.source_evidence_regressions("", text, PATH, FM), [])

    def test_other_azure_accounts_and_lookalikes_stay_unofficial(self):
        for host in ("blob.core.windows.net", "other.blob.core.windows.net",
                     "ifacweb.blob.core.windows.net.example.com"):
            with self.subTest(host=host):
                self.assertFalse(domains.host_is_official(host, "audit-assurance"))
                self.assertTrue(skill_checks.source_evidence_regressions("", source("https://" + host + "/x.pdf"), PATH, FM))

    def test_asset_permission_does_not_extend_to_other_domains(self):
        for domain in ("tax", "financial-reporting", "practice-management"):
            with self.subTest(domain=domain):
                self.assertFalse(domains.host_is_official(domains.url_host(ASSET), domain))


if __name__ == "__main__":
    unittest.main()
