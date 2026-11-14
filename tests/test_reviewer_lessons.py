from __future__ import annotations

import importlib.util
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import skill_checks as sc  # noqa: E402

spec = importlib.util.spec_from_file_location("validate_lessons", REPO_ROOT / "scripts" / "validate-guides.py")
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)


def table(rows, header="| Source | URL | Read on |"):
    return "## Sources\n\n" + header + "\n|---|---|---|\n" + "\n".join(rows) + "\n"


class ReadDates(unittest.TestCase):
    def test_bulk_stamp_warns_but_scoped_rows_pass(self):
        bare = [f"| Page {i} | https://a.gov/{i} | 2026-10-30 |" for i in range(6)]
        scoped = [f"| Act, art. {i} | https://a.gov/{i} | 2026-10-30 |" for i in range(6)]
        self.assertTrue(sc.check_read_date_evidence("x.md", table(bare), {}))
        self.assertEqual(sc.check_read_date_evidence("x.md", table(scoped), {}), [])

    def test_future_and_status_only(self):
        self.assertIn("future", sc.check_read_date_evidence("x.md", table(["| A | https://a.gov | 2999-01-01 |"]), {})[0])
        self.assertTrue(sc.check_read_date_evidence("x.md", table(["| A | https://a.gov | 2026-10-30, HTTP 200 |"]), {}))

    def test_honest_failure_and_law_dates_pass(self):
        text = table([
            "| A | https://a.gov | 2026-10-30 (refused with HTTP 403; not read) |",
            "| Law in force 2027-01-01 | https://a.gov/b | 2026-10-30 |",
        ])
        self.assertEqual(sc.check_read_date_evidence("x.md", text, {}), [])


class Columns(unittest.TestCase):
    def test_misfilled(self):
        self.assertTrue(sc.check_sources_columns("x.md", table(["| A | 2026-10-30 | https://a.gov |"]), {}))

    def test_good_rows_and_reference_links(self):
        text = table(["| A | https://a.gov | 2026-10-30 |", "| B | [Act][law] | 2026-10-30 |"])
        self.assertEqual(sc.check_sources_columns("x.md", text, {}), [])


class Hosts(unittest.TestCase):
    def test_secondary_authority_and_foreign(self):
        fm = {"jurisdiction": "FR"}
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| Rates | https://taxsummaries.pwc.com/a | 2026-10-30 |"]), fm))
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| HMRC manual | https://example.com/a | 2026-10-30 |"]), fm))
        self.assertTrue(sc.check_source_hosts("fr-x.md", table(["| Law | https://www.boe.es/a | 2026-10-30 |"]), fm))

    def test_neighbour_and_treaty_pass(self):
        self.assertEqual(sc.check_source_hosts("mc-x.md", table(["| Law | https://legifrance.gouv.fr/a | 2026-10-30 |"]), {"jurisdiction": "MC"}), [])
        self.assertEqual(sc.check_source_hosts("fr-x.md", table(["| Treaty | https://www.boe.es/a | 2026-10-30 |"]), {"jurisdiction": "FR"}), [])

    def test_french_guiana_uses_french_official_sources(self):
        path = str(REPO_ROOT / "skills/french-guiana/gf-income-tax.md")
        fm = {"jurisdiction": "GF"}
        source = table(["| DGFiP law | https://www.impots.gouv.fr/a | 2026-11-11 |"])
        self.assertEqual(sc.check_source_hosts(path, source, fm), [])
        self.assertTrue(sc.check_source_hosts(path, table(["| Rates | https://www.boe.es/a | 2026-11-11 |"]), fm))
        self.assertEqual(sc.check_jurisdiction_body(path, "# Guyane\n" + "DGFiP " * 9, fm), [])

    def test_australian_external_territories_use_australian_sources(self):
        for code, folder in (("CX", "christmas-island"), ("CC", "cocos-keeling-islands")):
            path = str(REPO_ROOT / f"skills/{folder}/{code.lower()}-income-tax.md")
            fm = {"jurisdiction": code}
            source = table(["| ITAA 1997 | https://www.legislation.gov.au/a | 2026-11-14 |"])
            self.assertEqual(sc.check_source_hosts(path, source, fm), [])
            self.assertTrue(sc.check_source_hosts(path, table(["| Rates | https://www.ird.govt.nz/a | 2026-11-14 |"]), fm))
            self.assertEqual(sc.check_jurisdiction_body(path, "# Territory\n" + "ATO " * 9, fm), [])

    def test_cook_islands_may_cite_new_zealand_dates(self):
        path = str(REPO_ROOT / "skills/cook-islands/ck-company-registry-reporting.md")
        fm = {"jurisdiction": "CK"}
        self.assertEqual(sc.check_source_hosts(path, table(["| Holiday dates | https://www.govt.nz/a | 2026-11-14 |"]), fm), [])
        self.assertTrue(sc.check_source_hosts(path, table(["| Rates | https://www.ato.gov.au/a | 2026-11-14 |"]), fm))


class SourceEvidencePriority(unittest.TestCase):
    def rates(self, row):
        return "## Rates, bands and thresholds\n\n| Item | Rate | Source |\n|---|---|---|\n" + row + "\n"

    def test_new_or_edited_unsourced_row_blocks_but_legacy_row_does_not(self):
        old = self.rates("| Fictional rate | 10% | missing |")
        self.assertEqual(sc.source_evidence_regressions(old, old + "\nOther prose."), [])
        self.assertEqual(len(sc.source_evidence_regressions(old, old.replace("10%", "12%"))), 1)
        self.assertEqual(len(sc.source_evidence_regressions("", old)), 1)

    def test_same_inherits_a_real_source_but_cannot_invent_one(self):
        linked = self.rates("| Fictional rate | 10% | https://authority.gov/rates |\n| Another | 12% | same |")
        self.assertEqual(sc.source_evidence_regressions("", linked), [])
        self.assertEqual(len(sc.source_evidence_regressions("", linked.replace("https://authority.gov/rates", "missing"))), 2)

    def test_known_secondary_citation_blocks_but_unknown_official_host_does_not(self):
        bad = table(["| Rates | https://taxsummaries.pwc.com/example | 2026-11-12 |"])
        self.assertTrue(sc.source_evidence_regressions("", bad))
        self.assertEqual(sc.source_evidence_regressions(bad, bad + "\nOther prose."), [])
        self.assertEqual(sc.source_evidence_regressions("", bad.replace("taxsummaries.pwc.com", "new-authority.gov")), [])

    def test_style_alone_cannot_block_a_tax_pr(self):
        self.assertFalse(validate.is_pr_error("no_em_dash", "tax", True, False))
        self.assertTrue(validate.is_pr_error("sources_read_dates", "tax", True, False))


class Jurisdiction(unittest.TestCase):
    def path(self, tail):
        return str(REPO_ROOT / "skills" / tail)

    def test_indiana_with_rupees(self):
        body = "---\nname: x\n---\n# x\n" + "₹1,00,000 is one lakh. " * 5
        problems = sc.check_jurisdiction_body(self.path("us/states/in/in-income-tax.md"), body, {"jurisdiction": "IN"})
        self.assertEqual(len(problems), 2)

    def test_home_currency_and_portuguese_irs_pass(self):
        body = "# x\n" + "₹1,00,000 " * 9
        self.assertEqual(sc.check_jurisdiction_body(self.path("india/in-x.md"), body, {"jurisdiction": "IN"}), [])
        self.assertEqual(sc.check_jurisdiction_body(self.path("portugal/pt-x.md"), "IRS " * 9, {"jurisdiction": "PT"}), [])

    def test_idaho_cannot_be_labelled_as_indonesia(self):
        path = self.path("us/states/id/id-income-tax.md")
        self.assertEqual(sc.check_jurisdiction_path(path, "", {"jurisdiction": "ID"}),
                         ["path says US-ID, frontmatter says ID"])
        self.assertEqual(sc.check_jurisdiction_path(path, "", {"jurisdiction": "US-ID"}), [])
        self.assertEqual(sc.check_jurisdiction_path(self.path("indonesia/id-x.md"), "", {"jurisdiction": "ID"}), [])

    def test_path_identity_blocks_every_changed_skill_type(self):
        for scope in ["tax", "general", "other"]:
            for metadata_only in [True, False]:
                self.assertTrue(validate.is_pr_error("jurisdiction_path", scope, True, metadata_only))
        self.assertFalse(validate.is_pr_error("jurisdiction_body", "tax", True, False))


class FalklandRegistry(unittest.TestCase):
    def test_falkland_pack_has_a_named_coverage_route(self):
        import json
        rows = json.loads((REPO_ROOT / "scripts/data/jurisdictions.json").read_text())
        record = next(row for row in rows if row["code"] == "FK")
        self.assertEqual(record["name"], "Falkland Islands")
        self.assertEqual(record["region"], "americas")
        self.assertEqual(record["dir"], "skills/falkland-islands")


class Years(unittest.TestCase):
    def test_earlier_year_in_url(self):
        text = table(["| Rates 2026 | https://a.gov/tax-rates-2024 | 2026-10-30 |"])
        self.assertTrue(sc.check_year_matches_link("x.md", text, {"tax_year": 2026}))

    def test_publication_year_and_span_pass(self):
        text = table([
            "| Rates 2026 | https://a.gov/rev-proc-2025-32 | 2026-10-30 |",
            "| Rates 2026 | https://a.gov/tax-rates-2025-26 | 2026-10-30 |",
        ])
        self.assertEqual(sc.check_year_matches_link("x.md", text, {"tax_year": 2026}), [])


class MergeRecord(unittest.TestCase):
    LOSER = "---\nname: l\n---\n## Rates\n\n## Penalties\n"
    BODY = "Folds loser-x.\n\n## Moved\n\n| Item | From |\n|---|---|\n| Rates | body |\n\n## Not moved\n\n| Item | Why |\n|---|---|\n| Penalties | duplicate |\n"

    def test_full_record_passes(self):
        self.assertEqual(sc.merge_record_problems("loser-x", self.LOSER, self.BODY), ([], []))

    def test_missing_sections_error(self):
        errors, _ = sc.merge_record_problems("loser-x", self.LOSER, "Merged loser-x, no content lost.")
        self.assertEqual(len(errors), 2)

    def test_unlisted_heading_warns(self):
        body = self.BODY.replace("| Penalties | duplicate |", "| Trigger words | duplicate |")
        errors, warnings = sc.merge_record_problems("loser-x", self.LOSER, body)
        self.assertEqual(errors, [])
        self.assertIn("Penalties", warnings[0])

    def test_validator_wiring(self):
        errors, warnings = [], []
        validate.check_merge_records(errors, warnings, pr_body="nothing", deleted={"skills/x/loser-x.md"}, old_text=lambda _: self.LOSER)
        self.assertEqual(len(errors), 3)
        errors, warnings = [], []
        # On a pull_request run Actions sets GITHUB_EVENT_PATH, so pr_body=None
        # would pick up the real PR body. Clear it to test the no-PR path.
        with mock.patch.dict(os.environ):
            os.environ.pop("GITHUB_EVENT_PATH", None)
            validate.check_merge_records(errors, warnings, pr_body=None, deleted={"skills/x/loser-x.md"})
        self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main()
