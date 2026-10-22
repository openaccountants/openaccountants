"""scripts/check-examples.py recomputes oa-check blocks and fails on a wrong expected value."""

import importlib.util
import os
import tempfile
import unittest
from decimal import Decimal

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("check_examples", os.path.join(REPO_ROOT, "scripts", "check-examples.py"))
ce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ce)

GOOD = """# Example

```oa-check
name: Malta sole trader, profit 40,000 (2026 bands)
inputs:
  profit: 40000
steps:
  - band_15: (min(profit, 14500) - 9100) * 0.15
  - band_25: (min(profit, 19500) - 14500) * 0.25
  - band_35: (profit - 19500) * 0.35
  - tax: band_15 + band_25 + band_35
expected:
  tax: 9235.00
```
"""


class CheckExamplesTest(unittest.TestCase):
    def _write(self, text):
        fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
        fh.write(text)
        fh.close()
        self.addCleanup(os.unlink, fh.name)
        return fh.name

    def test_correct_example_passes(self):
        found, failures = ce.check_file(self._write(GOOD))
        self.assertEqual(found, 1)
        self.assertEqual(failures, [])

    def test_wrong_expected_fails_with_actual(self):
        found, failures = ce.check_file(self._write(GOOD.replace("9235.00", "9000.00")))
        self.assertEqual(found, 1)
        self.assertEqual(len(failures), 1)
        self.assertIn("expected 9000.00 got 9235.00", failures[0])

    def test_tolerance_is_respected(self):
        text = GOOD.replace("name: Malta", "tolerance: 1\nname: Malta").replace("9235.00", "9235.60")
        _found, failures = ce.check_file(self._write(text))
        self.assertEqual(failures, [])

    def test_helpers_and_decimal_rounding(self):
        names = {"x": Decimal("1234.565")}
        self.assertEqual(ce.evaluate("round(x, 2)", names), Decimal("1234.57"))
        self.assertEqual(ce.evaluate("pct(x, 15)", names), Decimal("185.18475"))
        self.assertEqual(ce.evaluate("clamp(x, 0, 1000)", names), Decimal("1000"))

    def test_unsafe_expression_is_rejected(self):
        with self.assertRaises(ce.CheckError):
            ce.evaluate("__import__('os').system('true')", {})
        with self.assertRaises(ce.CheckError):
            ce.evaluate("x ** 2", {"x": Decimal(2)})

    def test_file_without_blocks_passes(self):
        found, failures = ce.check_file(self._write("# Nothing to check\n"))
        self.assertEqual((found, failures), (0, []))

    def test_unknown_name_is_reported(self):
        text = GOOD.replace("band_15 + band_25 + band_35", "band_15 + bandX")
        _found, failures = ce.check_file(self._write(text))
        self.assertEqual(len(failures), 1)
        self.assertIn("unknown name 'bandX'", failures[0])


if __name__ == "__main__":
    unittest.main()
