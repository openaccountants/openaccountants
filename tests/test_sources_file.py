"""SOURCES.md is not a skill, and the linker only links an exact match."""
import importlib.util
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skill_checks  # noqa: E402
import yaml  # noqa: E402


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


linker = load("link-rates-from-sources")
URL = "https://example.gov/q"
SRC = (f'| {URL} | T | F | 2026 | 2026-10-31 | fetch | Limit :: CHF 120,000 :: "mindestens 120 000 Franken"'
       '<br>Bad :: EUR 5 :: "nothing here" |\n')


def skill(row):
    return f"## Rates, bands and thresholds\n\n| Item | Amount | Source |\n| --- | --- | --- |\n{row}\n"


class NotASkill(unittest.TestCase):
    def test_helper(self):
        self.assertTrue(skill_checks.is_not_skill("skills/germany/SOURCES.md"))
        self.assertTrue(skill_checks.is_not_skill("README.md"))
        self.assertFalse(skill_checks.is_not_skill("de-payroll.md"))

    def test_every_walker_names_it(self):
        for name in ("build-index", "validate-guides", "check-examples", "detect-contradictions",
                     "build-agent-skills", "build-packages", "check-sync-integrity"):
            self.assertIn("sources.md", (ROOT / "scripts" / f"{name}.py").read_text(encoding="utf-8").lower(), name)

    def test_sync_integrity_skips_it(self):
        self.assertTrue(load("check-sync-integrity").is_pack_readme("skills/germany/SOURCES.md"))

    def test_ingest_filter_still_sends_it(self):
        """The doorbell sends every skills/*.md. The platform must skip it (later work)."""
        text = (ROOT / ".github/workflows/ingest-to-platform.yml").read_text(encoding="utf-8")
        self.assertIn('startswith("skills/") and endswith(".md")', text)
        self.assertIn("skills/**", yaml.safe_load(text)[True]["push"]["paths"])


class Linker(unittest.TestCase):
    def run_it(self, row):
        return linker.link_text(skill(row), linker.parse_sources(SRC))

    def test_links_on_figure_and_label(self):
        text, linked, bad = self.run_it("| Limit | CHF 120,000 |  |")
        self.assertEqual((linked, bad), (["Limit"], []))
        self.assertIn(f"| {URL} |", text)
        self.assertIn("CHF 120,000", text)

    def test_keeps_existing_note(self):
        self.assertIn(f"See art. 9, {URL}", self.run_it("| Limit | CHF 120,000 | See art. 9 |")[0])

    def test_wrong_figure_is_not_linked_or_edited(self):
        row = "| Limit | CHF 130,000 |  |"
        text, linked, bad = self.run_it(row)
        self.assertEqual(text, skill(row))
        self.assertEqual(linked, [])
        self.assertIn("figure differs", bad[0][1])

    def test_unknown_label(self):
        self.assertEqual(self.run_it("| Other | CHF 120,000 |  |")[2][0][1], "no stored label")

    def test_quote_must_hold_figure(self):
        self.assertIn("does not hold", self.run_it("| Bad | EUR 5 |  |")[2][0][1])


if __name__ == "__main__":
    unittest.main()
