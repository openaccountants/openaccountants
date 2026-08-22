"""Regression tests for fail-closed MCP quality metadata."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from openaccountants_mcp import server


class SkillQualityTests(unittest.TestCase):
    def test_tier_one_with_named_reviewer_is_accountant_verified(self) -> None:
        meta = {"tier": 1, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "accountant-verified")

    def test_legacy_verified_by_field_still_supports_tier_one(self) -> None:
        meta = {"tier": "1", "verified_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "accountant-verified")

    def test_tier_two_remains_research_even_with_reviewer_name(self) -> None:
        meta = {"tier": 2, "reviewed_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_tier_one_without_real_reviewer_fails_closed(self) -> None:
        for reviewer in (None, "", "pending", "pending_review", "none", "n/a", "-"):
            with self.subTest(reviewer=reviewer):
                meta = {"tier": 1, "reviewed_by": reviewer}
                self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_reviewer_name_does_not_replace_missing_tier(self) -> None:
        meta = {"verified_by": "Alex Example, CPA"}

        self.assertEqual(server._quality_tier(meta), "research-verified")

    def test_invalid_tier_values_fail_closed(self) -> None:
        for tier in (0, 3, "one", "draft"):
            with self.subTest(tier=tier):
                meta = {"tier": tier, "reviewed_by": "Alex Example, CPA"}
                self.assertEqual(server._quality_tier(meta), "research-verified")


class IndexVerifierExposureTests(unittest.TestCase):
    """A non-tier-1 row must not publish a reviewer name in ``verified_by``.

    The ``_quality_tier`` tests above do not cover this: deleting the
    conditional in ``_index`` that nulls the field leaves every one of them
    passing while the server still hands callers a tier 2 guide's reviewer as
    its verifier.
    """

    GUIDE = """---
name: {slug}
tier: {tier}
jurisdiction: MT
reviewed_by: Alex Example, CPA
---

# {slug}
"""

    def _row_for(self, slug: str, tier: int) -> dict:
        """Build a one-guide packages tree and return that guide's index row."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        package = Path(tmp.name) / "malta"
        package.mkdir(parents=True)
        (package / f"{slug}.md").write_text(
            self.GUIDE.format(slug=slug, tier=tier), encoding="utf-8"
        )
        self.addCleanup(server._index.cache_clear)
        with mock.patch.object(server, "PACKAGES_DIR", Path(tmp.name)):
            server._index.cache_clear()
            return server._index()[slug]

    def test_tier_two_row_does_not_expose_its_reviewer(self) -> None:
        row = self._row_for("tier-two-guide", 2)

        self.assertEqual(row["quality_tier"], "research-verified")
        self.assertIsNone(row["verified_by"])

    def test_tier_one_row_still_publishes_its_verifier(self) -> None:
        row = self._row_for("tier-one-guide", 1)

        self.assertEqual(row["quality_tier"], "accountant-verified")
        self.assertEqual(row["verified_by"], "Alex Example, CPA")


if __name__ == "__main__":
    unittest.main()
