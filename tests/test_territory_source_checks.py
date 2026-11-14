"""Territorial source geography does not imply identical tax treatment."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "scripts"))
import skill_checks


def sources(label, host):
    return "## Sources\n\n| Source | URL | Read on |\n|---|---|---|\n| " + label + " | https://" + host + "/law | 2026-11-14 |\n"


class TerritorySourceChecks(unittest.TestCase):
    def test_parent_jurisdiction_sources_are_not_foreign(self):
        examples = {
            "AX": ("vero.fi", "www.finlex.fi", "www.suomenpankki.fi"),
            "BQ": ("wetten.overheid.nl", "lokaleregelgeving.overheid.nl", "zoek.officielebekendmakingen.nl"),
            "HM": ("www.legislation.gov.au", "legislation.act.gov.au"),
            "NF": ("www.legislation.gov.au", "www.ato.gov.au", "legislation.nsw.gov.au"),
        }
        for jurisdiction, hosts in examples.items():
            for host in hosts:
                with self.subTest(jurisdiction=jurisdiction, host=host):
                    self.assertEqual(skill_checks.check_source_hosts("skills/example/scope.md", sources("Official legislation", host), {"jurisdiction": jurisdiction}), [])

    def test_caribbean_tax_authority_uses_its_own_official_host(self):
        for host in ("www.belastingdienst-cn.nl", "english.belastingdienst-cn.nl"):
            with self.subTest(host=host):
                self.assertEqual(skill_checks.check_source_hosts("skills/caribbean-netherlands/bq-abb.md", sources("Belastingdienst Caribisch Nederland", host), {"jurisdiction": "BQ"}), [])

    def test_australian_authority_words_fit_its_external_territories(self):
        text = "ATO administers this obligation. ATO guidance applies. Ask ATO. Check ATO. ATO evidence."
        for jurisdiction in ("CX", "CC", "HM", "NF"):
            with self.subTest(jurisdiction=jurisdiction):
                self.assertEqual(skill_checks.check_jurisdiction_body("skills/example/scope.md", text, {"jurisdiction": jurisdiction}), [])
        self.assertTrue(skill_checks.check_jurisdiction_body("skills/example/scope.md", text, {"jurisdiction": "GE"}))

    def test_third_country_and_secondary_sources_still_fail(self):
        for jurisdiction, host in (("AX", "www.ato.gov.au"), ("BQ", "vero.fi"), ("HM", "www.finlex.fi"), ("NF", "wetten.overheid.nl"), ("GE", "www.legislation.gov.au")):
            with self.subTest(jurisdiction=jurisdiction, host=host):
                self.assertTrue(skill_checks.check_source_hosts("skills/example/scope.md", sources("Official legislation", host), {"jurisdiction": jurisdiction}))
        for jurisdiction in ("AX", "BQ", "HM", "NF"):
            with self.subTest(jurisdiction=jurisdiction):
                self.assertTrue(skill_checks.check_source_hosts("skills/example/scope.md", sources("Tax summary", "taxsummaries.pwc.com"), {"jurisdiction": jurisdiction}))

    def test_authority_lookalikes_and_mislabelled_hosts_still_fail(self):
        for host in ("belastingdienst-cn.nl.example.com", "fake-belastingdienst-cn.nl", "www.vero.fi"):
            with self.subTest(host=host):
                problems = skill_checks.check_source_hosts("skills/caribbean-netherlands/bq-abb.md", sources("Belastingdienst Caribisch Nederland", host), {"jurisdiction": "BQ"})
                self.assertTrue(any("row names an authority" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
