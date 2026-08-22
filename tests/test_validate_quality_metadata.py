"""Synthetic tests for canonical guide quality-metadata validation."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate-guides.py"
SPEC = importlib.util.spec_from_file_location("validate_guides", SCRIPT)
validate_guides = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_guides)


def errors_for(tier=None, reviewed_by=None, verified_by=None):
    errors = []
    validate_guides.check_quality_metadata(
        "skills/example.md",
        {"tier": tier, "reviewed_by": reviewed_by, "verified_by": verified_by},
        errors,
    )
    return errors


class QualityMetadataValidationTests(unittest.TestCase):
    def test_rejects_missing_or_invalid_tier(self) -> None:
        self.assertIn("missing required", errors_for()[0])
        self.assertIn("must be 1 or 2", errors_for("3")[0])

    def test_tier_one_requires_a_real_reviewer(self) -> None:
        for placeholder in (None, "", "pending", "pending_review", "n/a", "tbd"):
            with self.subTest(placeholder=placeholder):
                self.assertIn("tier 1 requires", errors_for("1", placeholder)[0])

    def test_tier_one_accepts_current_and_legacy_reviewer_fields(self) -> None:
        self.assertEqual(errors_for("1", reviewed_by="Alex Example, CPA"), [])
        self.assertEqual(errors_for("1", verified_by="Alex Example, CPA"), [])

    def test_tier_two_allows_research_review_but_not_verification(self) -> None:
        self.assertEqual(errors_for("2", reviewed_by="Alex Example, CPA"), [])
        self.assertEqual(errors_for("2", verified_by="pending"), [])
        self.assertIn(
            "must not claim accountant verification",
            errors_for("2", verified_by="Alex Example, CPA")[0],
        )


if __name__ == "__main__":
    unittest.main()
