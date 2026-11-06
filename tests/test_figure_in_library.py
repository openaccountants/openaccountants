"""Check q, figure_in_library: a rates row must not state a different number for a library figure."""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import skill_checks  # noqa: E402

URL = "https://www.revenue.ie/en/gains-gifts-and-inheritance/cat/index.aspx"
FIGURES = [
    {
        "id": "ie.cat.group-a",
        "item": "CAT Group A tax-free threshold: gifts and inheritances a child takes from a parent.",
        "value": "EUR 400,000",
        "tax_year": 2026,
        "source_url": URL,
        "quote": "Group A: EUR 400,000",
        "read_on": "2026-10-02",
        "used_by": [],
    },
    {
        "id": "ie.cat.rate",
        "item": "CAT rate on the amount above the tax-free threshold.",
        "value": "33%",
        "tax_year": 2026,
        "source_url": URL,
        "quote": "33%",
        "read_on": "2026-10-02",
        "used_by": [],
    },
]


def skill(*rows):
    table = "| Item | Amount | Year | Source |\n|---|---|---|---|\n" + "".join(f"| {r} |\n" for r in rows)
    return "---\nname: ie-cat\n---\n\n## Rates, bands and thresholds\n\n" + table + "\n## Sources\n"


class FigureInLibrary(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        folder = os.path.join(self.tmp.name, "ireland")
        os.makedirs(folder)
        with open(os.path.join(folder, "figures.json"), "w", encoding="utf-8") as fh:
            json.dump({"country": "ireland", "code": "IE", "figures": FIGURES}, fh)
        self._dir, self._cache = skill_checks.LIBRARY_DIR, dict(skill_checks._library_cache)
        skill_checks.LIBRARY_DIR = self.tmp.name
        skill_checks._library_cache.clear()

    def tearDown(self):
        skill_checks.LIBRARY_DIR = self._dir
        skill_checks._library_cache.clear()
        skill_checks._library_cache.update(self._cache)
        self.tmp.cleanup()

    def run_check(self, text, path="skills/ireland/ie-cat.md"):
        return skill_checks.check_figure_in_library(path, text, {})

    def test_match_passes(self):
        text = skill(f"Group A threshold | EUR 400,000 | 2026 | {URL}", "Rate above the threshold | 33% | 2026 | same")
        self.assertEqual(self.run_check(text), [])

    def test_same_number_written_differently_passes(self):
        text = skill(f"Group A threshold | EUR 400,000.00 | 2026 | {URL}")
        self.assertEqual(self.run_check(text), [])

    def test_mismatch_warns(self):
        text = skill(f"Group A threshold | EUR 420,000 | 2026 | {URL}")
        problems = self.run_check(text)
        self.assertEqual(len(problems), 1)
        self.assertIn("ie.cat.group-a", problems[0])
        self.assertIn("EUR 400,000", problems[0])

    def test_mismatch_through_same_warns(self):
        text = skill(f"Group A threshold | EUR 400,000 | 2026 | {URL}", "CAT rate above the threshold | 30% | 2026 | same")
        problems = self.run_check(text)
        self.assertEqual(len(problems), 1)
        self.assertIn("ie.cat.rate", problems[0])

    def test_named_id_must_hold_the_exact_value(self):
        self.assertEqual(self.run_check(skill("Group A (`ie.cat.group-a`) | EUR 400,000 | 2026 | see Sources")), [])
        problems = self.run_check(skill("Group A (`ie.cat.group-a`) | EUR 400,000.00 | 2026 | see Sources"))
        self.assertIn("names ie.cat.group-a", problems[0])

    def test_other_page_is_not_compared(self):
        text = skill("Group A threshold | EUR 420,000 | 2026 | https://www.irishstatutebook.ie/eli/2026/act/1/en/html")
        self.assertEqual(self.run_check(text), [])

    def test_other_item_on_the_same_page_is_not_compared(self):
        text = skill(f"Small gift exemption, per donor per year | EUR 3,000 | 2026 | {URL}")
        self.assertEqual(self.run_check(text), [])

    def test_other_year_is_not_compared(self):
        text = skill(f"Group A threshold | EUR 335,000 | 2024 | {URL}")
        self.assertEqual(self.run_check(text), [])

    def test_row_with_several_amounts_is_not_compared(self):
        text = skill(f"Group A threshold | EUR 420,000 from 7 Oct; EUR 400,000 before | 2026 | {URL}")
        self.assertEqual(self.run_check(text), [])

    def test_no_library_passes(self):
        text = skill(f"Group A threshold | EUR 420,000 | 2026 | {URL}")
        self.assertEqual(self.run_check(text, path="skills/latvia/lv-cat.md"), [])
        self.assertEqual(self.run_check(text, path="docs/x.md"), [])

    def test_announced_value_passes_and_other_values_still_warn(self):
        bill = "https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/memo/b9826d-memo.pdf"
        announced = {
            "id": "ie.cat.group-a.announced",
            "item": "CAT Group A tax-free threshold from 7 October 2026, as proposed by the Finance Bill.",
            "value": "EUR 420,000",
            "tax_year": "gifts and inheritances taken on or after 7 October 2026",
            "source_url": bill,
            "quote": "the Group A threshold increases from €400,000 to €420,000",
            "read_on": "2026-11-06",
            "status": "announced, Finance Bill not yet enacted",
            "used_by": [],
        }
        with open(os.path.join(self.tmp.name, "ireland", "figures.json"), "w", encoding="utf-8") as fh:
            json.dump({"country": "ireland", "code": "IE", "figures": FIGURES + [announced]}, fh)
        skill_checks._library_cache.clear()
        self.assertEqual(self.run_check(skill(f"Group A threshold | EUR 400,000 | 2026 | {URL}")), [])
        self.assertEqual(self.run_check(skill(f"Group A threshold | EUR 420,000 | 2026 | {URL}")), [])
        self.assertEqual(self.run_check(skill("Group A (`ie.cat.group-a`) | EUR 420,000 | 2026 | see Sources")), [])
        self.assertEqual(self.run_check(skill("Group A (`ie.cat.group-a.announced`) | EUR 400,000 | 2026 | see Sources")), [])
        problems = self.run_check(skill(f"Group A threshold | EUR 410,000 | 2026 | {URL}"))
        self.assertEqual(len(problems), 1)
        self.assertIn("ie.cat.group-a", problems[0])
        problems = self.run_check(skill("Group A (`ie.cat.group-a`) | EUR 410,000 | 2026 | see Sources"))
        self.assertIn("names ie.cat.group-a", problems[0])

    def test_in_lesson_checks(self):
        self.assertIn(("q", "figure_in_library", skill_checks.check_figure_in_library), skill_checks.LESSON_CHECKS)
        self.assertNotIn("figure_in_library", skill_checks.CHECK_NAMES)


class BuildLibraryStatus(unittest.TestCase):
    """scripts/build-library.py publishes status and a per-entry read_on, and nothing else new."""

    def setUp(self):
        import importlib.util
        path = os.path.join(os.path.dirname(__file__), "..", "scripts", "build-library.py")
        spec = importlib.util.spec_from_file_location("build_library", path)
        self.bl = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.bl)

    def entry(self, pack_id, **extra):
        return {"pack_id": pack_id, "item": "Group A threshold", "value": "EUR 420,000",
                "source_url": URL, "quote": "Group A €420,000", "year": 2026, **extra}

    def test_status_and_read_on_are_published(self):
        pack = {"checked_at": "2026-10-02", "entries": [
            self.entry("ie.cat.group-a", value="EUR 400,000"),
            self.entry("ie.cat.group-a.announced", status="announced, Finance Bill not yet enacted", read_on="2026-11-06"),
        ]}
        figures, _sources, problems = self.bl.build_country("IE", pack, "no-such-folder")
        self.assertEqual(problems, [])
        in_force, announced = figures["figures"]
        self.assertNotIn("status", in_force)
        self.assertEqual(in_force["read_on"], "2026-10-02")
        self.assertEqual(announced["status"], "announced, Finance Bill not yet enacted")
        self.assertEqual(announced["read_on"], "2026-11-06")
        self.assertEqual(list(announced), ["id", "item", "value", "tax_year", "source_url", "quote", "read_on", "status", "used_by"])

    def test_unknown_status_or_id_without_suffix_is_skipped(self):
        pack = {"checked_at": "2026-10-02", "entries": [
            self.entry("ie.cat.group-a.announced", status="rumoured"),
            self.entry("ie.cat.group-a", status="announced, Finance Bill not yet enacted"),
        ]}
        figures, _sources, problems = self.bl.build_country("IE", pack, "no-such-folder")
        self.assertEqual(figures["figures"], [])
        self.assertEqual(len(problems), 2)


class ValueInText(unittest.TestCase):
    def test_whole_figures_only(self):
        self.assertTrue(skill_checks.value_in_text("EUR 1,000", "a cap of EUR 1,000."))
        self.assertFalse(skill_checks.value_in_text("EUR 1,000", "a cap of EUR 1,000,000"))
        self.assertFalse(skill_checks.value_in_text("5%", "at 5.5% of tax"))
        self.assertFalse(skill_checks.value_in_text("20%", "120% of cost"))
        self.assertTrue(skill_checks.value_in_text("20%", "first EUR 44,000 at 20%, balance"))


if __name__ == "__main__":
    unittest.main()
