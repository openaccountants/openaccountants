"""Golden cases for deterministic and fail-closed duplicate handling."""

from __future__ import annotations

import contextlib
import io
import runpy
import tempfile
import unittest
from pathlib import Path

from openaccountants_mcp import server


def _skill(name: str, title: str, jurisdiction: str = "XX") -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"jurisdiction: {jurisdiction}\n"
        "category: international\n"
        "tier: 2\n"
        "last_updated: 2026-01-02\n"
        "---\n\n"
        f"# {title}\n\nBody for {title}.\n"
    )


#: Same guidance, different quality stamps — the class the whole-file hash
#: could not tell apart from a real conflict.
TWIN_METADATA_A = """---
name: twin
jurisdiction: AA
category: international
tier: 2
last_updated: 2026-01-02
---

# Twin

Identical guidance in both copies.
"""

TWIN_METADATA_B = """---
name: twin
jurisdiction: AA
category: international
tier: 1
reviewed_by: Alex Example, CPA
last_updated: 2026-03-09
---

# Twin

Identical guidance in both copies.
"""


class DuplicateSlugTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.packages = Path(self._tmp.name)
        self._original_packages = server.PACKAGES_DIR
        server.PACKAGES_DIR = self.packages
        server._index.cache_clear()

    def tearDown(self) -> None:
        server.PACKAGES_DIR = self._original_packages
        server._index.cache_clear()
        self._tmp.cleanup()

    def _write(self, relpath: str, content: str) -> None:
        path = self.packages / relpath
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_metadata_only_difference_is_not_treated_as_divergence(self) -> None:
        """Divergence is judged on the guidance, not on frontmatter stamps.

        Hashing whole file bytes made a differing tier/reviewed_by/last_updated
        stamp indistinguishable from genuinely different tax law, so
        metadata-only twins were dropped as if their content conflicted.
        """
        self._write("country-a/twin.md", TWIN_METADATA_A)
        self._write("country-b/twin.md", TWIN_METADATA_B)

        self.assertIn("twin", server._index())
        report = server._duplicate_report()
        self.assertEqual(report["ambiguous_slugs"], 0)
        self.assertEqual(report["identical_aliases"], 1)

    def test_dropped_slugs_are_logged_and_surfaced_by_start(self) -> None:
        """A dropped slug must not be silent: nine jurisdictions' core skills
        vanished while start() still answered and list_skills() just reported a
        smaller total."""
        self._write("country-a/collision.md", _skill("collision", "Country A", "AA"))
        self._write("country-b/collision.md", _skill("collision", "Country B", "BB"))

        with self.assertLogs(server.log, level="WARNING") as captured:
            server._catalogue()
        logged = " | ".join(captured.output)
        self.assertIn("collision", logged)
        self.assertIn("country-a/collision.md", logged)
        self.assertIn("country-b/collision.md", logged)

        response = server.start()

        self.assertIn("warning", response)
        self.assertIn("collision", response["warning"])

    def test_byte_identical_aliases_collapse_to_sorted_path(self) -> None:
        content = _skill("shared-skill", "Shared")
        self._write("z/shared.md", content)
        self._write("a/shared.md", content)

        record = server._index()["shared-skill"]

        self.assertEqual(record["relpath"], "a/shared.md")
        self.assertEqual(record["last_updated"], "2026-01-02")
        self.assertEqual(server._duplicate_report()["identical_aliases"], 1)

    def test_cache_clear_refreshes_the_complete_catalogue(self) -> None:
        self._write("a/first.md", _skill("first", "First"))
        self.assertIn("first", server._index())
        self._write("b/second.md", _skill("second", "Second"))

        self.assertNotIn("second", server._index())
        server._index.cache_clear()
        self.assertIn("second", server._index())

    def test_safe_resolve_rejects_a_symlink_escape(self) -> None:
        with tempfile.TemporaryDirectory() as outside_dir:
            outside = Path(outside_dir) / "outside-skill.md"
            outside.write_text("outside", encoding="utf-8")
            link = self.packages / "escape.md"
            try:
                link.symlink_to(outside)
            except OSError as exc:
                self.skipTest(f"symlink creation is unavailable: {exc}")
            with self.assertRaisesRegex(ValueError, "Path escapes allowed root"):
                server._safe_resolve(self.packages, "escape.md")

    def test_catalogue_rejects_a_symlink_before_reading_outside_content(self) -> None:
        with tempfile.TemporaryDirectory() as outside_dir:
            outside = Path(outside_dir) / "outside-skill.md"
            outside.write_text(_skill("outside", "Outside"), encoding="utf-8")
            link = self.packages / "escape.md"
            try:
                link.symlink_to(outside)
            except OSError as exc:
                self.skipTest(f"symlink creation is unavailable: {exc}")

            self.assertNotIn("outside", server._index())
            self.assertEqual(server._duplicate_report()["rejected_paths"], ["escape.md"])

    def test_duplicate_report_module_is_quiet_when_imported(self) -> None:
        script = Path(server.__file__).resolve().parent / "duplicate_slug_report.py"
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            namespace = runpy.run_path(str(script), run_name="duplicate_report_import")

        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("main", namespace)

    def test_hand_authored_us_federal_copy_has_documented_precedence(self) -> None:
        self._write("us-ca/federal.md", _skill("federal-skill", "Generated", "US-CA"))
        self._write("us-federal/federal.md", _skill("federal-skill", "Federal", "US"))

        record = server._index()["federal-skill"]

        self.assertEqual(record["relpath"], "us-federal/federal.md")
        self.assertEqual(server._duplicate_report()["federal_precedence"], 1)

    def test_divergent_generated_copies_are_omitted_and_fail_closed(self) -> None:
        self._write("country-a/collision.md", _skill("collision", "Country A", "AA"))
        self._write("country-b/collision.md", _skill("collision", "Country B", "BB"))
        self._write("country-c/safe.md", _skill("safe", "Safe", "CC"))

        self.assertNotIn("collision", server._index())
        self.assertIn("safe", server._index())
        self.assertNotIn("collision", {s["slug"] for s in server.list_skills()["skills"]})
        self.assertNotIn(
            "collision",
            {r["slug"] for r in server.search_skills("Body")["results"]},
        )
        with self.assertRaisesRegex(ValueError, "packaged copies differ"):
            server.get_skill("collision")

        self.assertEqual(
            server._duplicate_report(),
            {
                "skill_files": 3,
                "slugs": 2,
                "duplicate_slugs": 1,
                "identical_aliases": 0,
                "federal_precedence": 0,
                "ambiguous_slugs": 1,
                "rejected_paths": [],
                "ambiguous": [
                    {
                        "slug": "collision",
                        "paths": [
                            "country-a/collision.md",
                            "country-b/collision.md",
                        ],
                    }
                ],
            },
        )


if __name__ == "__main__":
    unittest.main()
