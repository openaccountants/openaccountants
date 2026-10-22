"""validate-guides.py warns on tax skills without a sourced `## Sources` section and on stale figures."""

import importlib.util
import os
import sys
import unittest
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
spec = importlib.util.spec_from_file_location("validate_guides", os.path.join(REPO_ROOT, "scripts", "validate-guides.py"))
vg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vg)


class SourcesCheckTest(unittest.TestCase):
    def test_non_tax_skill_is_ignored(self):
        self.assertIsNone(vg.check_sources("skills/foundation/bookkeeping-workflow-base.md", "# no sources"))

    def test_tax_skill_without_section_warns(self):
        self.assertEqual(vg.check_sources("skills/international/malta/malta-income-tax.md", "# Body\n\n## Rates\n"),
                         "no `## Sources` section")

    def test_section_without_url_warns(self):
        text = "## Sources\n\n- Income Tax Act, article 56\n\n## Next\n"
        self.assertEqual(vg.check_sources("skills/international/malta/malta-income-tax.md", text),
                         "`## Sources` section has no URL")

    def test_section_with_url_passes(self):
        text = "## Sources\n\n| Source | URL | Read on |\n|---|---|---|\n| ITA | https://legislation.mt/x | 2026-10-22 |\n"
        self.assertIsNone(vg.check_sources("skills/international/malta/malta-income-tax.md", text))

    def test_url_after_next_heading_does_not_count(self):
        text = "## Sources\n\nSee below.\n\n## Links\n\nhttps://example.org\n"
        self.assertEqual(vg.check_sources("skills/international/malta/malta-vat-return.md", text),
                         "`## Sources` section has no URL")


class StalenessCheckTest(unittest.TestCase):
    today = date(2026, 10, 22)

    def test_fresh_passes(self):
        self.assertIsNone(vg.check_staleness({"last_updated": "2026-10-01", "tax_year": "2026"}, self.today))

    def test_old_last_updated_warns(self):
        self.assertIn("days old", vg.check_staleness({"last_updated": "2025-01-01", "tax_year": "2026"}, self.today))

    def test_old_tax_year_warns(self):
        self.assertIn("tax_year 2024", vg.check_staleness({"last_updated": "2026-10-01", "tax_year": "2024"}, self.today))

    def test_previous_year_is_fine(self):
        self.assertIsNone(vg.check_staleness({"last_updated": "2026-10-01", "tax_year": "2025"}, self.today))


if __name__ == "__main__":
    unittest.main()
