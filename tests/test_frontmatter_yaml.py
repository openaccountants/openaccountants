from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from frontmatter_yaml import FrontmatterError, load_frontmatter  # noqa: E402


class FrontmatterYamlTests(unittest.TestCase):
    def test_valid_block_sequence_parses(self) -> None:
        metadata = load_frontmatter(
            "name: example\n"
            "description: Example guide.\n"
            "jurisdiction: GB\n"
            "depends_on:\n"
            "  - workflow-base\n"
        )
        self.assertEqual(["workflow-base"], metadata["depends_on"])

    def test_inline_dash_after_mapping_key_is_rejected(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "sequence entries"):
            load_frontmatter("name: example\ndepends_on: - workflow-base\n")

    def test_unquoted_colon_space_is_rejected(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "mapping values"):
            load_frontmatter(
                "name: example\n"
                "description: Form 990 in the United States: how I do it\n"
            )

    def test_duplicate_key_is_rejected(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "duplicate key 'tier'"):
            load_frontmatter("name: example\ntier: 1\ntier: 2\n")

    def test_root_must_be_mapping(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "root must be a mapping"):
            load_frontmatter("- name: example\n")

    def test_norway_code_must_be_quoted(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "jurisdiction.*bool"):
            load_frontmatter("name: norway-example\njurisdiction: NO\n")
        metadata = load_frontmatter(
            'name: norway-example\njurisdiction: "NO"\n'
        )
        self.assertEqual("NO", metadata["jurisdiction"])

    def test_depends_on_must_be_string_list(self) -> None:
        with self.assertRaisesRegex(FrontmatterError, "non-empty strings"):
            load_frontmatter("name: example\ndepends_on: [workflow-base, false]\n")


if __name__ == "__main__":
    unittest.main()
