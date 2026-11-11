"""Line 11 of validate-guides.py: a file the website would never receive fails on the PR.

Both cases come from one contribution (IFRS 18, 10 Nov 2026): the file was named
`IFRS 18` with no `.md`, so delivery skipped it without a word, and once renamed it
was 130 KB, over the website's limit, so it was refused after the merge.
"""

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


vg = _load("validate_guides_deliverable", "validate-guides.py")
deliver = _load("deliver_to_platform_deliverable", "deliver-to-platform.py")

IFRS_DIR = "skills/global/financial-reporting/ifrs"
SKILL = "---\nname: ifrs18-presentation\ndescription: x\ntier: 2\n---\n\n# IFRS 18\n"


def problems(files, sizes=None):
    """Messages for {path: text} added or edited by a PR; sizes default to the text's bytes."""
    sizes = sizes or {}
    return vg.deliverable_problems(
        list(files), read=files.get,
        size=lambda rel: sizes.get(rel, len((files.get(rel) or "").encode())),
    )


class FileNameTest(unittest.TestCase):
    def test_a_file_without_md_fails_and_names_the_rename(self):
        found = problems({f"{IFRS_DIR}/IFRS 18": SKILL})
        self.assertEqual(len(found), 1)
        self.assertIn("not a `.md` file", found[0])
        self.assertIn(f"Rename `{IFRS_DIR}/IFRS 18` to `{IFRS_DIR}/ifrs18-presentation.md`", found[0])

    def test_the_rename_falls_back_to_the_file_name(self):
        found = problems({f"{IFRS_DIR}/IFRS 18": "no frontmatter here"})
        self.assertIn(f"to `{IFRS_DIR}/ifrs-18.md`", found[0])
        # A display name is not a slug, so it is not offered as a file name.
        titled = problems({f"{IFRS_DIR}/IFRS 18": "---\nname: IFRS 18 Presentation\n---\n"})
        self.assertIn(f"to `{IFRS_DIR}/ifrs-18.md`", titled[0])

    def test_other_extensions_fail_too(self):
        for name in ("ifrs18.txt", "ifrs18.docx", "ifrs18.markdown"):
            with self.subTest(name=name):
                self.assertEqual(len(problems({f"{IFRS_DIR}/{name}": SKILL})), 1)

    def test_a_skill_named_with_spaces_or_capitals_fails(self):
        found = problems({f"{IFRS_DIR}/IFRS 18.md": SKILL})
        self.assertEqual(len(found), 1)
        self.assertIn("lowercase letters, digits and hyphens", found[0])
        self.assertIn(f"to `{IFRS_DIR}/ifrs18-presentation.md`", found[0])

    def test_well_named_and_non_skill_files_pass(self):
        self.assertEqual(problems({
            f"{IFRS_DIR}/ifrs18-presentation.md": SKILL,
            "skills/malta/README.md": "# Malta\n",
            "skills/malta/references.md": "# References\n",
            "skills/REGISTER.csv": "slug\n",
            "skills/REGISTER.md": "# Register\n",
            "docs/Some Notes": "outside skills/",
        }), [])


class SizeTest(unittest.TestCase):
    def test_a_130_kb_skill_fails_with_size_limit_and_what_to_do(self):
        rel = f"{IFRS_DIR}/ifrs18-presentation.md"
        found = problems({rel: SKILL}, sizes={rel: 130_577})
        self.assertEqual(len(found), 1)
        self.assertIn("130,577 bytes", found[0])
        self.assertIn("112,640 bytes", found[0])
        self.assertIn("Split it into a base skill and a child skill that depends on it", found[0])

    def test_the_limit_itself_passes(self):
        rel = f"{IFRS_DIR}/ifrs18-presentation.md"
        self.assertEqual(problems({rel: SKILL}, sizes={rel: vg.PLATFORM_MAX_SKILL_BYTES}), [])
        self.assertEqual(len(problems({rel: SKILL}, sizes={rel: vg.PLATFORM_MAX_SKILL_BYTES + 1})), 1)

    def test_a_large_readme_is_not_a_skill(self):
        self.assertEqual(problems({"skills/malta/README.md": "x"}, sizes={"skills/malta/README.md": 500_000}), [])


class ModeTest(unittest.TestCase):
    def test_a_pr_gets_errors_and_the_full_run_gets_warnings(self):
        files = {f"{IFRS_DIR}/IFRS 18": SKILL}
        errors, warnings = [], []
        vg.check_deliverable(errors, warnings, list(files), read=files.get, size=lambda rel: 10)
        self.assertEqual((len(errors), warnings), (1, []))

    def test_the_tree_on_main_never_errors(self):
        errors, warnings = [], []
        vg.check_deliverable(errors, warnings, None)
        self.assertEqual(errors, [])


class SameRuleAsDeliveryTest(unittest.TestCase):
    def test_is_delivered_skill_matches_the_delivery_script(self):
        for rel in (
            f"{IFRS_DIR}/ifrs18-presentation.md", f"{IFRS_DIR}/IFRS 18", "skills/malta/README.md",
            "skills/malta/references.md", "skills/REGISTER.md", "skills/_templates/skill.md",
            "skills/malta/templates/x.md", "library/malta/x.md",
        ):
            with self.subTest(rel=rel):
                self.assertEqual(vg.is_delivered_skill(rel), deliver.is_skill(rel))


if __name__ == "__main__":
    unittest.main()
