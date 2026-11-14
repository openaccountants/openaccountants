import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location(
    "coverage_report", os.path.join(HERE, "..", "scripts", "coverage-report.py"))
cr = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cr)

README = """---
jurisdiction: XX
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable:
  TP: no documentation regime
covered_by:
  XB: moving-to-xx
partial:
  SC: self-employed only
---

# XX
"""


class PartialDomainsTest(unittest.TestCase):
    def test_partial_block_is_read(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "README.md"), "w") as fh:
                fh.write(README)
            applicable, na, covered, partial = cr.read_pack_readme(d)
        self.assertEqual(applicable, ["IT-IND", "IT-CORP", "VAT", "SC", "PR", "TP", "XB"])
        self.assertEqual(na, {"TP": "no documentation regime"})
        self.assertEqual(covered, {"XB": "moving-to-xx"})
        self.assertEqual(partial, {"SC": "self-employed only"})

    def test_no_readme(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(cr.read_pack_readme(d), (None, {}, {}, {}))

    def test_inline_partial_list_preserves_all_declared_gaps(self):
        text = README.replace("partial:\n  SC: self-employed only", "partial: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]")
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "README.md"), "w") as fh:
                fh.write(text)
            _, na, covered, partial = cr.read_pack_readme(d)
        self.assertEqual(set(partial), set(cr.DOMAIN_CODES))
        self.assertEqual(na, {"TP": "no documentation regime"})
        self.assertEqual(covered, {"XB": "moving-to-xx"})

    def test_yaml_list_layout_does_not_change_coverage(self):
        for declaration in [
            "partial:\n  - SC\n  - VAT",
            "partial: [\n  'SC',\n  \"VAT\"\n] # declared gaps",
        ]:
            with self.subTest(declaration=declaration), tempfile.TemporaryDirectory() as d:
                with open(os.path.join(d, "README.md"), "w") as fh:
                    fh.write(README.replace("partial:\n  SC: self-employed only", declaration))
                self.assertEqual(set(cr.read_pack_readme(d)[3]), {"SC", "VAT"})

    def test_empty_partial_list_does_not_add_gaps(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "README.md"), "w") as fh:
                fh.write(README.replace("partial:\n  SC: self-employed only", "partial: []"))
            self.assertEqual(cr.read_pack_readme(d)[3], {})

    def test_absent_partial_key_does_not_add_gaps(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "README.md"), "w") as fh:
                fh.write(README.replace("partial:\n  SC: self-employed only\n", ""))
            self.assertEqual(cr.read_pack_readme(d)[3], {})

    def test_invalid_partial_declarations_do_not_silently_report_no_gaps(self):
        for declaration in [
            "partial: SC", "partial: [SC, TYPO]", "partial: [SC, false]",
            "partial:\n  TYPO: gap", "partial: [SC,", "partial: [SC]\npartial: []",
            "partial:", "partial: null",
        ]:
            with self.subTest(declaration=declaration), tempfile.TemporaryDirectory() as d:
                with open(os.path.join(d, "README.md"), "w") as fh:
                    fh.write(README.replace("partial:\n  SC: self-employed only", declaration))
                with self.assertRaisesRegex(ValueError, "README.md"):
                    cr.read_pack_readme(d)

    def test_real_malta_report_keeps_partial_domains_in_writing(self):
        # The rule, not a snapshot of Malta's progress: a domain the README declares
        # partial still counts as missing, and a pack with any partial domain is not complete.
        row = next(row for row in cr.build_report()["rows"] if row["code"] == "MT")
        self.assertTrue(set(row["partial"]) <= set(row["missing"]))
        if row["partial"]:
            self.assertFalse(row["complete"])
            self.assertEqual(row["state"], "needs_writing")


if __name__ == "__main__":
    unittest.main()
