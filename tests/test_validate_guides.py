from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validate_guides = _load("validate_guides", "validate-guides.py")
build_index = _load("build_index_for_validator_tests", "build-index.py")


GOOD = """---
name: synthetic-guide
description: Synthetic guide used by the validator tests.
jurisdiction: MT
category: international
tier: 2
tax_year: 2025
last_updated: 2026-01-02
---

# Synthetic guide

Body.
"""

#: `depends_on: - x` is the shape the tolerant regex reader accepts and PyYAML
#: rejects, and the one 681 generated files carried.
# The flat `depends_on: - x` is now a GRANDFATHERED legacy form (663 files carry
# it; normalize_legacy_depends_on folds it into a real list before the strict
# parse). Malformed-for-testing therefore uses a shape with no legacy excuse:
# an unquoted colon inside a scalar.
MALFORMED = GOOD.replace("tier: 2\n", 'tier: 2\nqualifier: bad: colon soup\n')
LEGACY_FLAT_DEPENDS = GOOD.replace("tier: 2\n", "tier: 2\ndepends_on: - workflow-base\n")

#: A doc that opens on a horizontal rule, not frontmatter.
PLAIN_DOC = "# Notes\n\n---\n\nSome prose.\n"


class _Trees:
    """A `bi` stand-in: the real parsers, but a guide list the test controls."""

    def __init__(self, guides) -> None:
        self._guides = sorted(guides)
        self.extract_frontmatter = build_index.extract_frontmatter
        self.parse_known_keys = build_index.parse_known_keys

    def guide_files(self):
        return list(self._guides)


class _ValidatorCase(unittest.TestCase):
    def _tree(self, files) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root

    def _check_guides(self, files):
        root = self._tree(files)
        errors, warnings = [], []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                validate_guides.check_guides(_Trees(files), errors, warnings)
        return errors

    def _check_packages(self, files, guide_files=()):
        root = self._tree(files)
        errors = []
        with mock.patch.object(validate_guides, "REPO_ROOT", str(root)):
            with contextlib.redirect_stdout(io.StringIO()):
                validate_guides.check_packages_frontmatter(_Trees(guide_files), errors)
        return errors


class StrictFrontmatterTests(_ValidatorCase):
    """The strict loader in check_guides had no test at all, so deleting it
    left `unittest discover` green while the primary validator reverted to the
    tolerant regex reader."""

    def test_valid_guide_passes(self) -> None:
        self.assertEqual(self._check_guides({"skills/good.md": GOOD}), [])

    def test_malformed_yaml_is_an_error(self) -> None:
        errors = self._check_guides({"skills/bad.md": MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])

    def test_duplicate_keys_are_an_error(self) -> None:
        doubled = GOOD.replace("tier: 2\n", "tier: 2\ntier: 1\n")

        errors = self._check_guides({"skills/doubled.md": doubled})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])


class MisplacedFrontmatterTests(_ValidatorCase):
    """`---` must be at byte 0. Otherwise extract_frontmatter returns None and
    text.startswith("---") is false, so the file counted as a doc and bypassed
    the strict check entirely: exit 0 with skipped += 1."""

    def test_byte_order_mark_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/bom.md": "\ufeff" + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_leading_blank_line_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/blank.md": "\n" + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_leading_space_before_frontmatter_is_rejected(self) -> None:
        errors = self._check_guides({"skills/space.md": " " + MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("first bytes", errors[0])

    def test_a_doc_opening_on_a_horizontal_rule_is_still_skipped(self) -> None:
        self.assertEqual(self._check_guides({"skills/notes.md": PLAIN_DOC}), [])


class GeneratedPackagesTreeTests(_ValidatorCase):
    """packages/** was validated by nothing: build-index.py's GUIDE_TREES stops
    at skills/ plus the hand-authored packages/us-federal, and sync-mcp.yml
    mirrors the rest to the MCP repo on every push to main."""

    def test_malformed_generated_frontmatter_is_an_error(self) -> None:
        errors = self._check_packages({"packages/albania/albania-income-tax.md": MALFORMED})

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("invalid YAML frontmatter", errors[0])

    def test_legacy_flat_depends_on_is_grandfathered(self) -> None:
        # 663 existing files predate the strict sweep with this exact shape;
        # failing the whole tree on shipped history helps nobody. Only this one
        # key is folded — see normalize_legacy_depends_on.
        self.assertEqual(
            self._check_packages({"packages/albania/albania-income-tax.md": LEGACY_FLAT_DEPENDS}), []
        )

    def test_valid_generated_frontmatter_passes(self) -> None:
        self.assertEqual(
            self._check_packages({"packages/albania/albania-income-tax.md": GOOD}), []
        )

    def test_readmes_and_us_federal_are_not_double_reported(self) -> None:
        errors = self._check_packages(
            {
                "packages/us-federal/hand-authored.md": MALFORMED,
                "packages/albania/README.md": MALFORMED,
            },
            guide_files=["packages/us-federal/hand-authored.md"],
        )

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
