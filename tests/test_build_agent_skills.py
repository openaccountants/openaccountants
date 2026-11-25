"""The agent-skills tree is what people install into their AI. Its descriptions decide
whether the AI ever opens a skill, so they must be real sentences, and every file must
say where today's figures live."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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
        self.assertIn("1 are accountant-reviewed (a named accountant in `metadata.reviewed_by`); the other 2 are tier 2 (checked against the law, or sourced from the law).", out)
        self.assertTrue(out.startswith("intro\n") and out.endswith("\nrest"))
        # Without the tier count, a named reviewer is the fallback signal.
        self.assertIn("1 are accountant-reviewed", build.stamp_readme(text, built, ["MT"]))


class TreeTests(unittest.TestCase):
    def test_long_australian_slugs_keep_live_links_in_installable_wrappers(self) -> None:
        slugs = (
            "foreign-currency-forex-realisation-gains-and-losses-under-division-775",
            "leaving-australia-residency-the-cgt-departure-choice-and-what-follows-you",
        )
        source = ROOT / "skills" / "australia"
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            with patch.object(build, "OUT_DIR", out), patch.object(
                build, "iter_source_files", return_value=[source / f"{slug}.md" for slug in slugs]
            ):
                self.assertEqual(build.build(set(), check_only=False), 0)

            index = json.loads((out / "index.json").read_text(encoding="utf-8"))
            entries = {Path(entry["path"]).stem: entry for entry in index["skills"]}
            self.assertEqual(entries.keys(), set(slugs))
            self.assertEqual(index["count"], len(slugs))
            for slug in slugs:
                with self.subTest(slug=slug):
                    name = entries[slug]["name"]
                    self.assertLessEqual(len(name), 64)
                    self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                    wrapper = (out / name / "SKILL.md").read_text(encoding="utf-8")
                    meta, body = build.split_frontmatter(wrapper)
                    self.assertEqual(meta["name"], name)
                    self.assertEqual(meta["metadata"]["openaccountants_url"], f"{build.SITE}/skills/{slug}")
                    self.assertIn(f"`get_skill` with slug `{slug}`", body)

                    src_meta, src_body = build.split_frontmatter(
                        (source / f"{slug}.md").read_text(encoding="utf-8")
                    )
                    payload = body.rsplit("\n\n## Today's figures and who stands behind this skill", 1)[0]
                    self.assertEqual(payload.strip(), build.sanitize(src_body.strip()))
                    for field in ("authored_by", "reviewed_by", "review_status", "trust_label"):
                        expected = str(src_meta.get(field) or "").strip() or None
                        self.assertEqual(meta["metadata"].get(field), expected)
                    self.assertEqual(entries[slug]["reviewed_by"], src_meta.get("reviewed_by"))

    def test_repeated_canonical_slug_keeps_first_but_alias_collision_fails(self) -> None:
        slug, alias = next(iter(build.AGENT_SKILL_NAMES.items()))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first.md"
            repeat = root / "repeat.md"
            other = root / "other.md"
            first.write_text(f"---\nname: {slug}\njurisdiction: AU\n---\n\n# First\n")
            repeat.write_text(first.read_text())
            other.write_text(f"---\nname: {alias}\njurisdiction: AU\n---\n\n# Other\n")
            with patch.object(build, "REPO_ROOT", root), patch.object(
                build, "publication_catalogue", return_value=([], {}, {}, [])
            ):
                out = root / "duplicates"
                with patch.object(build, "OUT_DIR", out), patch.object(
                    build, "iter_source_files", return_value=[first, repeat]
                ):
                    self.assertEqual(build.build(set(), check_only=False), 0)
                index = json.loads((out / "index.json").read_text(encoding="utf-8"))
                self.assertEqual([entry["path"] for entry in index["skills"]], ["first.md"])

                for candidates in ([first, other], [other, first]):
                    with self.subTest(candidates=candidates):
                        out = root / "collision"
                        with patch.object(build, "OUT_DIR", out), patch.object(
                            build, "iter_source_files", return_value=candidates
                        ):
                            with self.assertRaisesRegex(ValueError, "Agent Skills name.*already in use"):
                                build.build(set(), check_only=False)
                        self.assertFalse(out.exists())

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
