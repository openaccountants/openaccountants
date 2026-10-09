"""Public attribution must not infer authorship from retired reviewer metadata."""
import tempfile
import unittest
from pathlib import Path
from unittest import mock
from openaccountants_mcp import server
from openaccountants_mcp.public_guide_content import attribution, sanitize_markdown


class PublicAttributionTests(unittest.TestCase):
    def test_prompt_does_not_request_retired_reviewer_credit(self):
        prompt = server.tax_return("MT", "2026")
        self.assertNotIn("verified by", prompt)
        self.assertIn("applicable period and official sources", prompt)

    def test_reviewer_never_becomes_author(self):
        for tier in (1, 2, None):
            row = attribution({"tier": tier, "reviewed_by": "Reviewer CPA"})
            self.assertIsNone(row["authored_by"])
            self.assertEqual(row["publisher"], "OpenAccountants")
            self.assertIn("Founded by Michael Cutajar", row["founder_credit"])
            self.assertNotIn("verified_by", row)

    def test_actual_author_preserved_separately_from_founder(self):
        row = attribution({"authored_by": "Actual Author", "author_profile": "https://example.com/author"})
        self.assertEqual(row["authored_by"], "Actual Author")
        self.assertEqual(row["author_profile"], "https://example.com/author")
        self.assertIsNone(attribution({"authored_by": "Michael Cutajar and the OpenAccountants team"})["authored_by"])

    def test_sanitizer_preserves_legal_rules_and_periods(self):
        body = """---
name: sample
tax_year: 2026
tier: 1
reviewed_by: Reviewer CPA
---
# Sample
Reviewed by: Reviewer CPA
Records must be verified by Commissioner.
The schedule is reviewed against the evidence by the tax office.
Rate: 15% for 2026 [official](https://example.gov/tax).
"""
        result = sanitize_markdown(body)
        self.assertNotIn("Reviewer CPA", result)
        self.assertNotIn("tier:", result)
        self.assertIn("publisher: OpenAccountants", result)
        self.assertIn("Records must be verified by Commissioner.", result)
        self.assertIn("The schedule is reviewed against the evidence by the tax office.", result)
        self.assertIn("Rate: 15% for 2026 [official](https://example.gov/tax).", result)
        self.assertEqual(sanitize_markdown("Use the accountant-reviewed UK VAT Guide."), "Use the UK VAT Guide.")
        self.assertEqual(sanitize_markdown("Use the accountant-reviewed [uk-vat](https://example.com/guide) Guide."), "Use the [uk-vat](https://example.com/guide) Guide.")
        self.assertEqual(sanitize_markdown("Use accountant-reviewed company accounts when following this Guide."), "Use accountant-reviewed company accounts when following this Guide.")

    def test_served_legacy_guide_retains_content_and_actual_author(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package = root / "malta"
            package.mkdir()
            path = package / "sample.md"
            original = """---
name: sample
jurisdiction: MT
tax_year: 2026
tier: 1
reviewed_by: Reviewer CPA
authored_by: Actual Author
---
# Sample
Reviewed by: Reviewer CPA
## Rates
Rate: 15% for 2026 [official](https://example.gov/tax).
"""
            path.write_text(original)
            with mock.patch.object(server, "PACKAGES_DIR", root):
                server._index.cache_clear()
                try:
                    listed = server.list_skills()["skills"][0]
                    result = server.get_skill("sample")
                    sections = server.get_skill_sections("sample")
                    self.assertNotIn("quality_tier", listed)
                    self.assertNotIn("verified_by", result)
                    self.assertEqual(result["authored_by"], "Actual Author")
                    self.assertNotIn("Reviewer CPA", str(result) + str(sections))
                    self.assertIn("15% for 2026", result["markdown"])
                    self.assertIn("Founded by Michael Cutajar", result["markdown"])
                    self.assertEqual(path.read_text(), original)
                finally:
                    server._index.cache_clear()
