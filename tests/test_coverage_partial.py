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


if __name__ == "__main__":
    unittest.main()
