"""The agent-skills tree is what people install into their AI. Its descriptions decide
whether the AI ever opens a skill, so they must be real sentences, and every file must
say where today's figures live."""
from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


build = _load("build_agent_skills_for_tests", "build-agent-skills.py")

BODY = """# Malta rental income

This Guide covers a Malta-resident individual with residential rental income choosing between the flat rate and progressive rates.

## Section 1
| Field | Value |
"""


class DescriptionTests(unittest.TestCase):
    def test_keeps_a_real_trigger_description(self) -> None:
        meta = {"description": 'Use for Malta rental income. Trigger on "Malta rent tax", "15% final tax".'}
        self.assertEqual(build.derive_description(meta, BODY, "mt-rental"), meta["description"])

    def test_replaces_a_broken_description_with_the_opening_and_says_skill(self) -> None:
        desc = build.derive_description({"description": "---"}, BODY, "mt-rental")
        self.assertTrue(desc.startswith("Use when asked about Malta rental income. This skill covers"))
        self.assertNotIn("Guide", desc)

    def test_caps_length(self) -> None:
        desc = build.derive_description({"description": "x" * 2000}, BODY, "mt-rental")
        self.assertLessEqual(len(desc), 1000)


class SkillFileTests(unittest.TestCase):
    def test_skill_md_has_frontmatter_body_and_live_figures_section(self) -> None:
        meta = {"description": "Use for Malta rental income. Trigger on Malta rent tax questions.", "jurisdiction": "MT",
                "tax_year": 2026, "last_updated": "2026-10-02", "authored_by": "Michael Cutajar and the OpenAccountants team"}
        out = build.skill_md("mt-rental", meta, BODY)
        self.assertTrue(out.startswith("---\nname: mt-rental\n"))
        self.assertIn('  jurisdiction: "MT"', out)
        self.assertIn("# Malta rental income", out)
        self.assertIn("## Today's figures and who stands behind this skill", out)
        self.assertIn("`get_skill` with slug `mt-rental`", out)
        self.assertIn("https://www.openaccountants.com/skills/mt-rental", out)

    def test_readme_stats_block_has_two_states(self) -> None:
        built = {
            "a": {"authored_by": "Michael Cutajar and the OpenAccountants team", "reviewed_by": None},
            "b": {"authored_by": None, "reviewed_by": "Jane Doe, CPA"},
            "c": {"authored_by": None, "reviewed_by": None},
        }
        text = "intro\n<!-- oa-skills-stats:start -->\nold\n<!-- oa-skills-stats:end -->\nrest"
        out = build.stamp_readme(text, built, ["MT", "NL"], reviewed=1)
        self.assertIn("**3 skills** across **2 jurisdictions**", out)
        self.assertIn("1 are accountant-reviewed (a named accountant in `metadata.reviewed_by`); the other 2 are source-cited drafts.", out)
        self.assertTrue(out.startswith("intro\n") and out.endswith("\nrest"))
        # Without the tier count, a named reviewer is the fallback signal.
        self.assertIn("1 are accountant-reviewed", build.stamp_readme(text, built, ["MT"]))


class TreeTests(unittest.TestCase):
    def test_index_matches_folders(self) -> None:
        index_path = ROOT / "agent-skills" / "index.json"
        if not index_path.exists():
            self.skipTest("agent-skills not built in this checkout")
        index = json.loads(index_path.read_text(encoding="utf-8"))
        folders = {p.name for p in (ROOT / "agent-skills").iterdir() if p.is_dir()}
        names = {s["name"] for s in index["skills"]}
        self.assertEqual(index["count"], len(names))
        self.assertTrue(names <= folders, f"index lists skills with no folder: {sorted(names - folders)[:5]}")


if __name__ == "__main__":
    unittest.main()
