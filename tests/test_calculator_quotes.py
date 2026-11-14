"""scripts/check-calculator-quotes.py finds each calculator's quoted line in its skill, the way the app does."""

import contextlib
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("check_calculator_quotes",
                                              os.path.join(REPO_ROOT, "scripts", "check-calculator-quotes.py"))
cq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cq)

# The same fixture the app's quote-match.test.ts uses, so the two matchers are held to one behaviour.
SKILL = "\n".join([
    "## Rates, bands and thresholds",
    "",
    "| Item | Rate | Year | Source |",
    "| --- | --- | --- | --- |",
    "| Vpb on taxable amount up to and including EUR 200,000 (Wet Vpb art. 22) | **19%** | 2026 | [Wet Vpb](https://wetten.overheid.nl) |",
    "| above EUR 200,000 | 25.8% | 2026 | art. 22 |",
    "| CPP employee rate | 5.95% | 2026 | CRA |",
    "| Cap | $1,000,000 | 2026 | |",
    "- **Zone 2** — EUR 12 349 – 17,799: (914.51 × y + 1,400) × y",
    "",
    "Example 1: ‘business is 100% of income’, so 16% x 15,070 = 2,411",
])
LINES = cq.normalise_lines(SKILL)


class NormaliseText(unittest.TestCase):
    def test_whitespace_case_emphasis_links(self):
        self.assertEqual(cq.normalise_text("  **Levy**   |  2%  of   [taxable income](https://x)  "), "levy | 2% of taxable income")
        self.assertEqual(cq.normalise_text("__a__ `b` *c*"), "a b c")

    def test_thousands_separators(self):
        self.assertEqual(cq.normalise_text("EUR 12,345.67"), "eur 12345.67")
        self.assertEqual(cq.normalise_text("EUR 12 345"), "eur 12345")
        self.assertEqual(cq.normalise_text("EUR 12 345"), "eur 12345")
        self.assertEqual(cq.normalise_text("1,234,567"), "1234567")

    def test_keeps_decimals_and_short_groups(self):
        self.assertEqual(cq.normalise_text("0.0595"), "0.0595")
        self.assertEqual(cq.normalise_text("1, 2, 3"), "1, 2, 3")
        self.assertEqual(cq.normalise_text("12,34"), "12,34")

    def test_dashes(self):
        want = cq.normalise_text("$0 - $18,200")
        for d in ["--", "–", "—", "−", " -- ", "-"]:
            self.assertEqual(cq.normalise_text(f"$0{d}$18,200"), want)

    def test_quote_marks_and_pipes(self):
        self.assertEqual(cq.normalise_text("the quarter’s “income”"), cq.normalise_text("the quarter's \"income\""))
        self.assertEqual(cq.normalise_text("|a|b |  c|"), "| a | b | c |")


class QuoteFound(unittest.TestCase):
    def test_table_row_with_other_typography(self):
        self.assertTrue(cq.quote_found("Vpb on taxable amount up to and including EUR 200,000 (Wet Vpb art. 22) | 19% | 2026", LINES))
        self.assertTrue(cq.quote_found("EUR 12,349 -- 17,799: (914.51 × y + 1,400) × y", LINES))
        self.assertTrue(cq.quote_found("Example 1: 'business is 100% of income', so 16% x 15,070", LINES))

    def test_changed_figure_is_missing(self):
        self.assertFalse(cq.quote_found("above EUR 200,000 | 25.9% | 2026", LINES))
        self.assertFalse(cq.quote_found("Vpb on taxable amount up to and including EUR 250,000", LINES))

    def test_never_splits_a_number(self):
        self.assertTrue(cq.quote_found("employee rate | 5.95%", LINES))
        self.assertFalse(cq.quote_found("rate | 5.9", LINES))
        self.assertFalse(cq.quote_found("Cap | $1,000", LINES))
        self.assertTrue(cq.quote_found("Cap | $1,000,000", LINES))
        self.assertFalse(cq.quote_found("5.95% | 2026", cq.normalise_lines("| x | 15.95% | 2026 |")))

    def test_ellipsis_within_one_line_in_order(self):
        self.assertTrue(cq.quote_found("up to and including EUR 200,000 ... 19% | 2026", LINES))
        self.assertFalse(cq.quote_found("19% ... up to and including EUR 200,000", LINES))
        self.assertFalse(cq.quote_found("CPP employee rate … $1,000,000", LINES))

    def test_multi_line_in_order(self):
        self.assertTrue(cq.quote_found("Item | Rate | Year | Source\nCPP employee rate | 5.95%", LINES))
        self.assertFalse(cq.quote_found("CPP employee rate | 5.95%\nItem | Rate | Year | Source", LINES))

    def test_empty_quote(self):
        self.assertFalse(cq.quote_found("  ", LINES))
        self.assertFalse(cq.quote_found("...", LINES))


def skill_file(name, body):
    return f"---\nname: {name}\njurisdiction: XX\n---\n\n{body}\n"


class Repo(unittest.TestCase):
    """A fake repo in a temp dir: skills/ and calculators/engines/<engine>/rules.json."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("skills/xx/xx-rates.md", skill_file("xx-rates", SKILL))
        self.write("skills/xx/README.md", "# not a skill\n")
        self.rules("xx_tax", [
            {"name": "RATE", "slug": "xx-rates", "section": "Rates", "quote": "CPP employee rate | 5.95%"},
            {"name": "NO_QUOTE", "slug": "xx-rates", "section": "Rates", "quote": ""},
        ])

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def rules(self, engine, rules):
        self.write(f"calculators/engines/{engine}/rules.json", json.dumps({"engine": engine, "rules": rules}))

    def run_main(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}):
            code = cq.main(argv, root=self.root)
        return code, out.getvalue()

    def test_all_found(self):
        code, out = self.run_main([])
        self.assertEqual(code, 0, out)
        self.assertIn("Every quoted line is still in its skill", out)

    def test_broken_quote_reported_with_engine_rule_slug_and_quote(self):
        self.rules("yy_tax", [{"name": "CAP", "slug": "xx-rates", "section": "Rates", "quote": "Cap | $2,000,000"}])
        code, out = self.run_main([])
        self.assertEqual(code, 1)
        self.assertIn("calculator `yy_tax` quotes; keep the line word for word, or update the calculator in the app repo first", out)
        self.assertIn("`CAP`", out)
        self.assertIn("`xx-rates`", out)
        self.assertIn("> Cap | $2,000,000", out)
        self.assertNotIn("`xx_tax`", out)

    def test_missing_skill_is_broken(self):
        self.rules("zz_tax", [{"name": "X", "slug": "gone-skill", "section": "S", "quote": "anything"}])
        code, out = self.run_main([])
        self.assertEqual(code, 1)
        self.assertIn("no skill under skills/ has this name", out)

    def test_frontmatter_is_not_skill_text(self):
        self.rules("zz_tax", [{"name": "X", "slug": "xx-rates", "section": "S", "quote": "jurisdiction: XX"}])
        self.assertEqual(self.run_main([])[0], 1)

    def test_step_summary_written(self):
        summary = self.root / "summary.md"
        with contextlib.redirect_stdout(io.StringIO()), patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary)}):
            cq.main([], root=self.root)
        self.assertIn("## Calculator quotes", summary.read_text())

    def git(self, *args):
        subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True)

    def init_git_with_base(self):
        self.write("skills/xx/xx-other.md", skill_file("xx-other", "| A | 1% |"))
        self.rules("oo_tax", [{"name": "A", "slug": "xx-other", "section": "S", "quote": "A | 2%"}])  # already broken
        self.git("init", "-q", "-b", "main")
        self.git("-c", "user.email=t@t", "-c", "user.name=t", "add", "-A")
        self.git("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "base")
        self.git("update-ref", "refs/remotes/origin/main", "HEAD")
        self.git("checkout", "-q", "-b", "pr")

    def commit(self):
        self.git("-c", "user.email=t@t", "-c", "user.name=t", "add", "-A")
        self.git("-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "pr")

    def run_changed(self):
        with patch.dict(os.environ, {"BASE_REF": "main"}):
            return self.run_main(["--changed-only"])

    def test_changed_only_ignores_untouched_skills(self):
        self.init_git_with_base()
        code, out = self.run_changed()
        self.assertEqual(code, 0, out)
        self.assertIn("changes no skill files", out)

    def test_changed_only_catches_an_edit_that_drops_the_line(self):
        self.init_git_with_base()
        self.write("skills/xx/xx-rates.md", skill_file("xx-rates", SKILL.replace("5.95%", "6.10%")))
        self.commit()
        code, out = self.run_changed()
        self.assertEqual(code, 1, out)
        self.assertIn("`xx_tax`", out)
        self.assertNotIn("`oo_tax`", out)  # broken on main, but its skill is not in this PR

    def test_changed_only_passes_a_harmless_edit(self):
        self.init_git_with_base()
        self.write("skills/xx/xx-rates.md", skill_file("xx-rates", SKILL + "\n\nA new paragraph."))
        self.commit()
        self.assertEqual(self.run_changed()[0], 0)

    def test_changed_only_catches_a_deleted_skill(self):
        self.init_git_with_base()
        (self.root / "skills/xx/xx-rates.md").unlink()
        self.commit()
        code, out = self.run_changed()
        self.assertEqual(code, 1, out)
        self.assertIn("no skill under skills/ has this name", out)


if __name__ == "__main__":
    unittest.main()
