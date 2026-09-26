"""build-index.py restamps the llms.txt counts sentence on a default build."""

from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build_index = _load("build_index_for_counts_tests", "build-index.py")

COUNTS = {"guides": 2019, "jurisdictions": 245, "accountant_reviewed": 168}
SENTENCE = (
    "> Tax Guides. 1,998 Guides across 245 jurisdictions in this repository, "
    "171 of them accountant-reviewed and signed off by named Partners."
)


class StampLlmsCountsTests(unittest.TestCase):
    def _write(self, text: str) -> Path:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8", newline="", delete=False)
        self.addCleanup(lambda: Path(tmp.name).unlink(missing_ok=True))
        with tmp:
            tmp.write(text)
        return Path(tmp.name)

    def test_restamps_figures_and_keeps_line_endings(self) -> None:
        path = self._write("# llms\r\n\r\n" + SENTENCE + "\r\n")
        self.assertTrue(build_index.stamp_llms_counts(COUNTS, path=path))
        text = path.read_bytes().decode("utf-8")
        self.assertIn("2,019 Guides across 245 jurisdictions in this repository, 168 of them accountant-reviewed", text)
        self.assertNotIn("1,998", text)
        self.assertEqual(text.count("\r\n"), 3)

    def test_unchanged_figures_do_not_rewrite(self) -> None:
        path = self._write(SENTENCE + "\n")
        before = path.stat().st_mtime_ns
        self.assertFalse(build_index.stamp_llms_counts({"guides": 1998, "jurisdictions": 245, "accountant_reviewed": 171}, path=path))
        self.assertEqual(path.stat().st_mtime_ns, before)

    def test_missing_sentence_warns_instead_of_failing(self) -> None:
        path = self._write("no counts sentence here\n")
        err = io.StringIO()
        with redirect_stderr(err):
            self.assertFalse(build_index.stamp_llms_counts(COUNTS, path=path))
        self.assertIn("expected 1", err.getvalue())
        self.assertEqual(path.read_text(encoding="utf-8"), "no counts sentence here\n")


if __name__ == "__main__":
    unittest.main()
