"""Sanctioned countries: the data file, the validate-guides.py guard (line 10) and the coverage report."""

import importlib.util
import os
import subprocess
import sys
import tempfile
import io
from unittest.mock import patch
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import sanctioned  # noqa: E402


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


vg = _load("validate_guides_sanctioned", "validate-guides.py")

SIX = {"RU", "BY", "CU", "IR", "KP", "SY"}  # broad embargo, 6 Nov 2026
UN_ELEVEN = {"AF", "CF", "CD", "HT", "IQ", "LB", "LY", "SO", "SS", "SD", "GW"}  # UN Security Council, 8 Nov 2026
LISTED = SIX | UN_ELEVEN | {"VE"}  # Venezuela excluded by Michael, 12 Nov 2026
TARGETED = {"MM"}  # US or EU sanctions only: stay covered


def skill(jurisdiction):
    return f"---\nname: x\ndescription: x\njurisdiction: {jurisdiction}\ntier: 2\nlast_updated: 2026-11-06\n---\n\n# X\n"


def guard(files):
    """Errors from check_sanctioned for {path: text} added or edited by a PR."""
    errors = []
    vg.check_sanctioned(errors, list(files), read=files.get)
    return errors


class DataFileTest(unittest.TestCase):
    def test_listed_codes_and_folders(self):
        self.assertEqual(sanctioned.codes(), LISTED)
        self.assertEqual(set(sanctioned.folders()),
                         {"russia", "belarus", "cuba", "iran", "north-korea", "syria",
                          "afghanistan", "central-african-republic", "dr-congo", "haiti", "iraq", "lebanon",
                          "libya", "somalia", "south-sudan", "sudan", "guinea-bissau", "venezuela"})

    def test_decision_recorded(self):
        data = sanctioned.load()
        self.assertEqual(data["decided_on"], "2026-11-12")
        self.assertEqual(data["decided_by"], "Michael 6 Nov 2026 (six), 8 Nov 2026 (eleven), 12 Nov 2026 (Venezuela)")
        for name in ("Myanmar",):
            self.assertIn(name, data["stay_live"])

    def test_targeted_sanction_countries_are_not_listed(self):
        self.assertFalse(sanctioned.codes() & TARGETED)

    def test_no_folder_left_in_the_tree(self):
        for folder in sanctioned.folders():
            for root in ("skills", "library"):
                self.assertFalse((REPO_ROOT / root / folder).exists(), f"{root}/{folder} still exists")

    def test_registry_has_no_sanctioned_entry(self):
        import json
        data = json.loads((SCRIPTS / "data" / "jurisdictions.json").read_text(encoding="utf-8"))
        self.assertFalse({row["code"] for row in data} & LISTED)


class GuardTest(unittest.TestCase):
    def test_folder_is_refused(self):
        for path in ("skills/iran/ir-vat.md", "skills/North-Korea/kp-tax.md", "library/belarus/figures.json",
                     "skills/russia/README.md", "evidence/research/belarus-2026/research.md",
                     "evidence/ledgers/syria/x.md", "skills/Venezuela/venezuela-payroll.md", "library/venezuela/figures.json"):
            errors = guard({path: skill("GLOBAL")})
            self.assertEqual(len(errors), 1, path)
            self.assertIn("sanctioned country", errors[0])
            self.assertIn("scripts/data/sanctioned.yml", errors[0])

    def test_jurisdiction_is_refused_in_any_folder(self):
        for code in ("RU", "by", "CU", "IR", "KP", "SY", "RU-MOW", '"IR"', "[DE, SY]", "VE", "ve", "VE-DC"):
            errors = guard({"skills/global/cross-border/x.md": skill(code)})
            self.assertEqual(len(errors), 1, code)
            self.assertIn("its jurisdiction", errors[0])

    def test_malformed_frontmatter_cannot_hide_the_code(self):
        text = "---\nname: x\njurisdiction: KP\nbad: a: b\n---\n\n# X\n"
        self.assertEqual(len(guard({"skills/global/x.md": text})), 1)

    def test_library_json_jurisdiction(self):
        self.assertEqual(len(guard({"library/global/figures.json": '{"jurisdiction": "BY", "figures": []}'})), 1)
        self.assertEqual(guard({"library/germany/figures.json": '{"jurisdiction": "DE", "figures": []}'}), [])

    def test_other_countries_pass(self):
        files = {f"skills/x/{c.lower()}.md": skill(c) for c in TARGETED | {"DE", "MT", "GLOBAL", "INTL", "US-NY"}}
        files["skills/myanmar/mm-vat.md"] = skill("MM")
        files["skills/jordan/jo-vat.md"] = skill("JO")
        files["skills/cyprus/cy-vat.md"] = skill("CY")
        self.assertEqual(guard(files), [])

    def test_mentions_in_the_body_are_fine(self):
        text = skill("LT") + "\nThe Lithuania-Belarus treaty, and goods from Iran or Russia.\n"
        self.assertEqual(guard({"skills/lithuania/lt-cross-border.md": text}), [])

    def test_paths_outside_guarded_roots_are_ignored(self):
        self.assertEqual(guard({"docs/research/iran.md": "x", "scripts/data/sanctioned.yml": "x",
                                "packages/belarus/README.md": "x"}), [])

    def test_whole_tree_is_clean(self):
        errors = []
        vg.check_sanctioned(errors)
        self.assertEqual(errors, [])


@unittest.skipUnless(subprocess.run(["git", "--version"], capture_output=True).returncode == 0, "git needed")
class PullRequestModeTest(unittest.TestCase):
    """validate-guides.py --changed-only on a real repository: an added or edited file
    fails, a deletion passes."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.repo = Path(os.path.realpath(tmp.name))
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.com")
        self.git("config", "user.name", "t")
        self.write("skills/cuba/cu-vat.md", skill("CU"))
        self.write("library/README.md", "x")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        self.git("checkout", "-q", "-b", "pr")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, capture_output=True, text=True, check=True).stdout

    def write(self, rel, text):
        path = self.repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_guard(self):
        old = vg.REPO_ROOT
        vg.REPO_ROOT = str(self.repo)
        try:
            errors = []
            vg.check_sanctioned(errors, vg.added_or_edited_vs_main(), read=vg._read_or_none)
            return errors
        finally:
            vg.REPO_ROOT = old

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "pr")

    def test_deleting_passes(self):
        self.git("rm", "-q", "skills/cuba/cu-vat.md")
        self.commit()
        self.assertEqual(self.run_guard(), [])

    def test_editing_fails(self):
        self.write("skills/cuba/cu-vat.md", skill("CU") + "\nmore\n")
        self.commit()
        self.assertEqual(len(self.run_guard()), 1)

    def test_adding_a_library_file_fails(self):
        self.write("library/iran/figures.json", "{}")
        self.commit()
        errors = self.run_guard()
        self.assertEqual(len(errors), 1)
        self.assertIn("Iran (IR)", errors[0])

    def test_moving_into_a_sanctioned_folder_fails(self):
        self.write("skills/global/x.md", skill("GLOBAL"))
        self.commit()
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        (self.repo / "skills" / "syria").mkdir()
        self.git("mv", "skills/global/x.md", "skills/syria/x.md")
        self.commit()
        self.assertEqual(len(self.run_guard()), 1)

    def test_other_files_pass(self):
        self.write("skills/germany/de-vat.md", skill("DE"))
        self.commit()
        self.assertEqual(self.run_guard(), [])


class CoverageTest(unittest.TestCase):
    def test_listed_apart_never_as_a_pack_to_finish(self):
        cr = _load("coverage_report_sanctioned", "coverage-report.py")
        report = cr.build_report()
        self.assertFalse({r["code"].split("-")[0] for r in report["rows"]} & LISTED)
        listed = {c["code"]: c["state"] for c in report["not_covered_sanctioned"]}
        self.assertEqual(set(listed), LISTED)
        self.assertEqual(set(listed.values()), {"Not covered (sanctioned)"})
        self.assertIn("Not covered (sanctioned", "\n".join(cr.summary_lines(report)))

    def test_countries_page_lists_them(self):
        builder = _load("build_country_index_sanctioned", "build-country-index.py")
        # Check freshly generated output; the checked-in derived snapshot may
        # precede this source policy until the rebuild bot follows the merge.
        with patch("pathlib.Path.write_text") as write, patch("sys.stdout", new_callable=io.StringIO):
            builder.main()
        text = write.call_args.args[0]
        section = text.split("## Not covered (sanctioned)", 1)[1]
        for c in sanctioned.countries():
            self.assertIn(f"| {c['name']} | Not covered (sanctioned) |", section)
            self.assertNotIn(f"]({c['folder']}/)", text)


if __name__ == "__main__":
    unittest.main()
