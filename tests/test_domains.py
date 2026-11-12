"""docs/domains.yml: a skill's `domain:` picks the date rule (check a) and the official
hosts (check m, scripts/build-library.py). Tax keeps exactly the rules it had before."""

import datetime
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
import domains  # noqa: E402
import skill_checks  # noqa: E402


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO_ROOT, "scripts", filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_guides = _load("validate_guides_domains", "validate-guides.py")
build_library = _load("build_library_domains", "build-library.py")
check_examples = _load("check_examples_domains", "check-examples.py")
coverage = _load("coverage_report_domains", "coverage-report.py")

#: scripts/build-library.py's OFFICIAL_HOSTS before the list moved to docs/domains.yml.
#: The tax allow-list must stay exactly this: no host added, none dropped.
TAX_HOSTS_BEFORE = {
    "boe.es", "seg-social.es", "ipyme.org", "gesetze-im-internet.de", "recht.bund.de",
    "bundesfinanzministerium.de", "bundesgesundheitsministerium.de", "bundesregierung.de",
    "bundesjustizamt.de", "deutsche-rentenversicherung.de", "minijob-zentrale.de",
    "gkv-spitzenverband.de", "existenzgruendungsportal.de", "urssaf.fr", "legislation.mt",
    "revenue.ie", "irishstatutebook.ie", "oireachtas.ie", "skatturinn.is", "stjornarradid.is",
    "normattiva.it", "inps.it", "svs.at", "chinhphu.vn", "zimra.co.zw", "inegi.org.mx",
}

#: The website's skills.domain vocabulary (its skills_domain_check constraint).
WEBSITE_VALUES = {
    "income-tax", "vat-gst", "payroll", "bookkeeping", "e-invoicing", "formation",
    "financial-statements", "transfer-pricing", "tax-optimization", "crypto", "cross-border",
    "corporate-tax", "estate-wealth-tax", "references", "sector-guidance", "tooling",
}


def legacy_tax_year_current(fm):
    """Tax dating with the explicit period-label check, independent of domain routing."""
    year = fm.get("tax_year")
    if year is None or str(year).strip() == "":
        return ["no tax_year"]
    if str(year).strip() == str(skill_checks.CURRENT_TAX_YEAR):
        return []
    if fm.get("tax_year_notes"):
        if skill_checks._current_tax_period(year, fm["tax_year_notes"]):
            return []
        return [f"tax_year {year}: tax_year_notes must name an adjacent-year period starting in {year} and including {skill_checks.CURRENT_TAX_YEAR}"]
    return [f"tax_year {year} is not {skill_checks.CURRENT_TAX_YEAR} and no tax_year_notes"]


IFRS_PATH = "skills/global/financial-reporting/ifrs/ifrs18-presentation.md"
IFRS_FM = {
    "name": "ifrs18-presentation",
    "jurisdiction": "GLOBAL",
    "domain": "financial-reporting",
    "type": "situation-rules",
    "standard": "IFRS 18 Presentation and Disclosure in Financial Statements",
    "effective_date": "2027-01-01",
    "tier": 2,
    "version": "0.1",
    "last_updated": "2026-11-06",
}
IFRS_SOURCES = (
    "| IFRS Foundation, IFRS 18, paragraphs on the operating category | "
    "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/ | 2026-11-06 |\n"
    "| EU endorsement of IFRS 18 | https://eur-lex.europa.eu/eli/reg/2023/1803/oj | 2026-11-06 |\n"
)


def ifrs_skill(sources=IFRS_SOURCES, extra_fm=""):
    """A whole IFRS skill (test fixture, not a skill): the worked example in CONTRIBUTING.md."""
    fm = "".join(f"{k}: {v!r}\n" if isinstance(v, str) else f"{k}: {v}\n" for k, v in IFRS_FM.items())
    return f"""---
{fm}description: Test fixture. How IFRS 18 sorts income and expenses into categories.
{extra_fm}---

# IFRS 18 presentation v0.1

## Scope

Entities reporting under IFRS Accounting Standards, for annual periods beginning on or after 1 January 2027.

## Ask the client first

1. Is the entity's main business activity investing in assets or providing financing to customers?

## The method, step by step

Classify each income and expense item in the statement of profit or loss into the operating,
investing or financing category, then subtotal operating profit.

## Worked cases

```oa-check
name: Operating profit, no investing income
inputs:
  revenue: 1000
  cost_of_sales: 600
  other_operating: 150
steps:
  - operating_profit: revenue - cost_of_sales - other_operating
expected:
  operating_profit: 250
```

```oa-check
name: Operating profit with dividend income classified in investing
inputs:
  revenue: 1000
  cost_of_sales: 600
  other_operating: 150
  dividends: 40
steps:
  - operating_profit: revenue - cost_of_sales - other_operating
  - before_financing: operating_profit + dividends
expected:
  operating_profit: 250
  before_financing: 290
```

## When to refuse or refer

Refer an entity whose main business activity is investing or financing.

## Sources

| Source | URL | Read on |
|---|---|---|
{sources}
Not yet confirmed: none.

## Talk to a verified accountant

Text.
"""


def run(path, text):
    return skill_checks.run_checks(path, text, skill_checks.read_frontmatter(text))


class DomainsFile(unittest.TestCase):
    def setUp(self):
        self.data = domains.load()

    def test_the_domains_michael_named_are_active(self):
        for domain_id in ("tax", "financial-reporting", "audit-assurance", "bookkeeping", "payroll",
                          "practice-management", "advisory"):
            self.assertEqual(self.data["domains"][domain_id]["status"], "active", domain_id)

    def test_every_domain_has_the_fields(self):
        for domain_id, domain in self.data["domains"].items():
            for key in ("label", "status", "examples", "date_field", "official_sources"):
                self.assertTrue(domain.get(key), f"{domain_id}: {key}")
            self.assertIn(domain["status"], ("active", "proposed"))
            for other in domain["official_sources"].get("also") or []:
                self.assertIn(other, self.data["domains"], f"{domain_id} also names {other}")

    def test_date_fields(self):
        self.assertEqual(domains.date_fields(domains.get("tax")), ["tax_year"])
        for domain_id in ("financial-reporting", "audit-assurance"):
            self.assertEqual(domains.date_fields(domains.get(domain_id)), ["standard", "effective_date"])
        for domain_id in ("bookkeeping", "payroll", "practice-management", "advisory"):
            self.assertEqual(domains.date_fields(domains.get(domain_id)), ["checked_on"])

    def test_copyright_notes_on_the_standards(self):
        for domain_id in ("financial-reporting", "audit-assurance"):
            note = domains.get(domain_id)["copyright_note"].lower()
            self.assertIn("paragraph", note)
            self.assertIn("never reproduce", note)

    def test_tax_sub_domains_are_the_coverage_domains(self):
        codes = [s["code"] for s in domains.get("tax")["sub_domains"]]
        self.assertEqual(codes, coverage.DOMAIN_CODES)

    def test_website_values_are_the_website_vocabulary(self):
        self.assertEqual(self.data["website_values"], WEBSITE_VALUES)

    def test_no_em_dash(self):
        with open(domains.DOMAINS_FILE, encoding="utf-8") as fh:
            self.assertNotIn("\u2014", fh.read())

    def test_unreadable_file_is_checked_as_before(self):
        missing = os.path.join(tempfile.gettempdir(), "no-such-domains.yml")
        with self.assertRaises(domains.DomainsError):
            domains.load(missing)
        self.assertEqual(domains.resolve("financial-reporting", missing), ("unreadable", None))


class TaxUnchanged(unittest.TestCase):
    """Tax keeps exactly the rules it had before docs/domains.yml."""

    def test_tax_allow_list_is_the_old_one(self):
        self.assertEqual(set(domains.official_hosts("tax")), TAX_HOSTS_BEFORE)
        self.assertEqual(set(build_library.OFFICIAL_HOSTS), TAX_HOSTS_BEFORE)

    def test_standard_setters_are_not_official_for_tax(self):
        for url in ["https://www.ifrs.org/x", "https://asc.fasb.org/x", "https://www.iaasb.org/x",
                    "https://eur-lex.europa.eu/x", "https://resource.cdn.icai.org/x.pdf"]:
            self.assertFalse(build_library.official_host(url), url)
            self.assertFalse(build_library.official_host(url, "tax"), url)
            self.assertFalse(build_library.official_host(url, "payroll"), url)

    def test_date_rule_by_domain_value(self):
        for fm in ({"tax_year": 2025}, {"tax_year": 2026}, {}, {"tax_year": 2025, "tax_year_notes": "2025-26"}):
            for domain in (None, "tax", "income-tax", "vat-gst", "payroll", "bookkeeping",
                           "financial-statements", "tooling", "nonsense", "sustainability-reporting"):
                case = dict(fm, **({"domain": domain} if domain else {}))
                self.assertEqual(skill_checks.check_tax_year_current("skills/malta/mt-x.md", "", case),
                                 legacy_tax_year_current(case), case)

    def test_a_tax_file_name_wins_over_any_domain(self):
        fm = dict(IFRS_FM, name="germany-vat-return", jurisdiction="DE", tax_year=2025)
        for path in ("skills/germany/germany-vat-return.md", "skills/germany/de-trade-tax.md",
                     "skills/kenya/ke-payroll-calendar.md"):
            for domain in ("financial-reporting", "advisory", "payroll"):
                case = dict(fm, domain=domain, checked_on="2026-11-01")
                self.assertEqual(skill_checks.applied_domain(path, case), (None, "names-tax"))
                self.assertEqual(skill_checks.check_tax_year_current(path, "", case),
                                 ["tax_year 2025 is not 2026 and no tax_year_notes"])
                self.assertEqual(skill_checks.check_rates_rows_sourced(path, "no table", case), ["no rates table"])
                self.assertIn("names a tax", skill_checks.check_domain_known(path, "", case)[0])

    def test_hosts_check_unchanged_for_tax(self):
        table = "## Sources\n\n| Source | URL | Read on |\n|---|---|---|\n| Law | https://example.com/a | 2026-10-30 |\n"
        for domain in (None, "tax", "income-tax", "payroll"):
            fm = {"jurisdiction": "FR", **({"domain": domain} if domain else {})}
            self.assertEqual(skill_checks.check_source_hosts("skills/france/fr-x.md", table, fm), [])

    def test_files_unchanged_since_main_are_checked_as_before(self):
        """Every skill file still byte-identical to main before this change (a frozen list of
        fingerprints) gets no domain rule, no new warning and the old date rule. Files edited or
        added later are not in the list, so a new contribution in any domain cannot break this."""
        with open(os.path.join(REPO_ROOT, "tests", "data", "domains-baseline.txt"), encoding="utf-8") as fh:
            baseline = {line.strip() for line in fh if line.strip() and not line.startswith("#")}
        self.assertEqual(len(baseline), 2396)
        matched = 0
        for path in skill_checks._build_index.guide_files():
            if not path.startswith("skills/"):
                continue
            with open(os.path.join(REPO_ROOT, path), "rb") as fh:
                data = fh.read()
            if hashlib.sha1(path.encode() + b"\0" + data).hexdigest()[:16] not in baseline:
                continue
            matched += 1
            text = data.decode("utf-8", errors="replace")
            fm = skill_checks.read_frontmatter(text)
            self.assertEqual(skill_checks.applied_domain(path, fm)[0], None, path)
            self.assertEqual(skill_checks.check_domain_known(path, text, fm), [], path)
            self.assertEqual(skill_checks.check_tax_year_current(path, text, fm), legacy_tax_year_current(fm), path)
        self.assertGreater(matched, 0)

    def test_no_domain_rule_means_the_old_date_rule(self):
        """Live tree, any file: without an active non-tax domain, check (a) is the old rule."""
        for path in skill_checks._build_index.guide_files():
            if not path.startswith("skills/"):
                continue
            with open(os.path.join(REPO_ROOT, path), encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            fm = skill_checks.read_frontmatter(text)
            if fm and skill_checks.applied_domain(path, fm)[0] is None:
                self.assertEqual(skill_checks.check_tax_year_current(path, text, fm), legacy_tax_year_current(fm), path)

    def test_pr_error_checks_keep_date_and_approval_rules_but_style_warns(self):
        self.assertEqual(validate_guides.PR_ERROR_CHECKS, {
            "tax_year_current", "sources_read_dates", "two_oa_checks", "version_numeric",
            "tier_honest",
        })

    def test_staleness_unchanged_for_tax(self):
        today = datetime.date(2026, 11, 6)
        fields = {"tax_year": "2023", "last_updated": "2026-11-01"}
        self.assertIn("two or more years behind", validate_guides.check_staleness(fields, today))
        self.assertIsNone(validate_guides.check_staleness(fields, today, dated_by_tax_year=False))


class IfrsSkill(unittest.TestCase):
    def test_ifrs_skill_passes_every_check(self):
        text = ifrs_skill()
        problems = {name: p for name, p in run(IFRS_PATH, text).items() if p}
        self.assertEqual(problems, {})

    def test_its_examples_recompute(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
            fh.write(ifrs_skill())
        try:
            found, failures = check_examples.check_file(fh.name)
        finally:
            os.unlink(fh.name)
        self.assertEqual((found, failures), (2, []))

    def test_no_tax_year_is_demanded(self):
        fm = dict(IFRS_FM)
        self.assertNotIn("tax_year", fm)
        self.assertEqual(skill_checks.check_tax_year_current(IFRS_PATH, "", fm), [])

    def test_standard_and_effective_date_are_demanded(self):
        fm = {k: v for k, v in IFRS_FM.items() if k not in ("standard", "effective_date")}
        problems = skill_checks.check_tax_year_current(IFRS_PATH, "", fm)
        self.assertEqual(len(problems), 2)
        self.assertTrue(problems[0].startswith("no standard (domain financial-reporting"))
        self.assertTrue(problems[1].startswith("no effective_date"))
        self.assertFalse(any("tax_year" in p for p in problems))
        bad = dict(IFRS_FM, effective_date="January 2027")
        self.assertEqual(skill_checks.check_tax_year_current(IFRS_PATH, "", bad),
                         ["effective_date 'January 2027' is not a YYYY-MM-DD date"])

    def test_a_future_effective_date_is_fine(self):
        fm = dict(IFRS_FM, effective_date=datetime.date(2027, 1, 1))  # YAML reads a bare date as a date
        self.assertEqual(skill_checks.check_tax_year_current(IFRS_PATH, "", fm), [])

    def test_unofficial_hosts_warn(self):
        text = ifrs_skill(IFRS_SOURCES + "| Firm guide | https://kpmg.com/ifrs18 | 2026-11-06 |\n"
                          "| Summary | https://www.iasplus.com/ifrs18 | 2026-11-06 |\n")
        problems = skill_checks.check_source_hosts(IFRS_PATH, text, skill_checks.read_frontmatter(text))
        self.assertIn("secondary host cited: kpmg.com", problems[0])
        self.assertIn("not an official source for domain financial-reporting", problems[1])
        self.assertIn("iasplus.com", problems[1])

    def test_standard_setters_are_official(self):
        for host in ("www.ifrs.org", "eifrs.ifrs.org", "fasb.org", "asc.fasb.org",
                     "eur-lex.europa.eu", "www.frc.org.uk", "socpa.org.sa", "www.icai.org", "www.sec.gov"):
            self.assertTrue(domains.host_is_official(host, "financial-reporting"), host)
        for host in ("www.iaasb.org", "www.ifac.org", "pcaobus.org"):
            self.assertTrue(domains.host_is_official(host, "audit-assurance"), host)
        self.assertFalse(domains.host_is_official("www.iasplus.com", "financial-reporting"))

    def test_professional_bodies_and_advisers_are_not_setters(self):
        for domain_id in ("financial-reporting", "audit-assurance", "practice-management"):
            for host in ("www.icaew.com", "www.accaglobal.com", "www.aicpa-cima.com"):
                self.assertFalse(domains.host_is_official(host, domain_id), (domain_id, host))
        self.assertFalse(domains.host_is_official("www.efrag.org", "financial-reporting"))
        self.assertTrue(domains.host_is_official("www.efrag.org", "sustainability-reporting"))

    def test_rates_table_is_optional(self):
        self.assertEqual(skill_checks.check_rates_rows_sourced(IFRS_PATH, "no table", IFRS_FM), [])

    def test_validate_guides_has_no_error_for_it(self):
        fm = skill_checks.read_frontmatter(ifrs_skill())
        self.assertNotEqual(skill_checks.scope_of(IFRS_PATH, fm), "tax")


class OtherDomains(unittest.TestCase):
    def test_checked_on(self):
        path = "skills/global/methods/engagement-letters.md"
        recent = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
        fm = {"domain": "practice-management", "checked_on": recent}
        self.assertEqual(skill_checks.check_tax_year_current(path, "", fm), [])
        self.assertEqual(skill_checks.check_tax_year_current(path, "", {"domain": "advisory"}),
                         ["no checked_on (domain advisory is dated by checked_on, docs/domains.yml)"])
        future = (datetime.date.today() + datetime.timedelta(days=3)).isoformat()
        self.assertEqual(skill_checks.check_tax_year_current(path, "", {"domain": "advisory", "checked_on": future}),
                         [f"checked_on {future} is in the future"])

    def test_checked_on_window(self):
        path = "skills/global/methods/engagement-letters.md"
        self.assertEqual(domains.get("practice-management")["max_age_days"], 365)
        today = datetime.date.today()
        edge = (today - datetime.timedelta(days=365)).isoformat()
        old = (today - datetime.timedelta(days=366)).isoformat()
        self.assertEqual(skill_checks.check_tax_year_current(path, "", {"domain": "practice-management", "checked_on": edge}), [])
        self.assertEqual(skill_checks.check_tax_year_current(path, "", {"domain": "advisory", "checked_on": "2019-01-01"}),
                         ["checked_on 2019-01-01 is more than 365 days old (domain advisory, max_age_days in docs/domains.yml)"])
        self.assertEqual(len(skill_checks.check_tax_year_current(path, "", {"domain": "advisory", "checked_on": old})), 1)

    def test_domain_date_rule_is_a_pr_error_when_the_text_changes(self):
        pr_error = validate_guides.is_pr_error
        # A non-tax domain's date rule fails the PR, whatever the scope, once the text changed.
        self.assertTrue(pr_error("tax_year_current", "other", False, False))
        self.assertTrue(pr_error("tax_year_current", "general", False, False))
        self.assertFalse(pr_error("tax_year_current", "other", False, True))  # frontmatter-only relabel
        # The fixed core now applies in every domain.
        self.assertTrue(pr_error("two_oa_checks", "other", False, False))
        self.assertFalse(pr_error("domain_known", "tax", True, False))
        # Tax: exactly as before.
        self.assertTrue(pr_error("tax_year_current", "tax", True, False))
        self.assertFalse(pr_error("tax_year_current", "tax", True, True))
        self.assertTrue(pr_error("tier_honest", "tax", True, True))
        self.assertTrue(pr_error("tax_year_current", "general", True, False))

    def test_payroll_and_bookkeeping_apply_once_they_carry_checked_on(self):
        path = "skills/germany/de-payslip-contents.md"
        self.assertEqual(skill_checks.applied_domain(path, {"domain": "payroll"}), (None, "website"))
        domain, status = skill_checks.applied_domain(path, {"domain": "payroll", "checked_on": "2026-11-01"})
        self.assertEqual((domain["id"], status), ("payroll", "active"))
        domain, _ = skill_checks.applied_domain("skills/france/fr-chart-of-accounts.md",
                                                {"domain": "bookkeeping", "checked_on": "2026-11-01"})
        self.assertEqual(domain["id"], "bookkeeping")


class UnknownDomain(unittest.TestCase):
    def test_unknown_domain_warns_and_is_checked_as_before(self):
        fm = {"domain": "forensic-accounting", "tax_year": 2025}
        warning = skill_checks.check_domain_known("skills/global/methods/x.md", "", fm)
        self.assertEqual(len(warning), 1)
        self.assertIn("propose it there", warning[0])
        self.assertIn("docs/domains.yml", warning[0])
        self.assertIn("Propose a domain: forensic-accounting", warning[0])
        self.assertEqual(skill_checks.check_tax_year_current("skills/global/methods/x.md", "", fm),
                         ["tax_year 2025 is not 2026 and no tax_year_notes"])

    def test_proposed_domain_warns_and_is_checked_as_before(self):
        fm = {"domain": "sustainability-reporting", "standard": "IFRS S2", "effective_date": "2024-01-01"}
        self.assertIn("proposed", skill_checks.check_domain_known("skills/global/x/ifrs-s2.md", "", fm)[0])
        self.assertEqual(skill_checks.check_tax_year_current("skills/global/x/ifrs-s2.md", "", fm), ["no tax_year"])

    def test_known_values_do_not_warn(self):
        for value in sorted(WEBSITE_VALUES) + ["tax", "financial-reporting", "audit-assurance", ""]:
            self.assertEqual(skill_checks.check_domain_known("skills/global/x/ifrs15-revenue.md", "", {"domain": value}), [], value)

    def test_domain_known_is_a_warning_outside_the_register(self):
        self.assertIn(("r", "domain_known", skill_checks.check_domain_known), skill_checks.LESSON_CHECKS)
        self.assertNotIn("domain_known", skill_checks.CHECK_NAMES)
        self.assertNotIn("domain_known", validate_guides.PR_ERROR_CHECKS)


class LibraryByDomain(unittest.TestCase):
    URL = "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18/"

    def entry(self, pack_id, **extra):
        return {"pack_id": pack_id, "item": "IFRS 18 effective date", "value": "1 January 2027",
                "source_url": self.URL, "quote": "1 January 2027", "year": 2027, **extra}

    def test_standard_setter_figure_by_domain(self):
        pack = {"checked_at": "2026-11-06", "entries": [
            self.entry("xx.ifrs18.effective", domain="financial-reporting"),
            self.entry("xx.ifrs18.tax"),
            self.entry("xx.ifrs18.unknown", domain="forensic-accounting"),
        ]}
        figures, _sources, problems = build_library.build_country("XX", pack, "no-such-folder")
        self.assertEqual([f["id"] for f in figures["figures"]], ["xx.ifrs18.effective"])
        self.assertEqual(figures["figures"][0]["domain"], "financial-reporting")
        self.assertIn("allow-list for tax", problems[0])
        self.assertIn("not an active domain", problems[1])

    def test_tax_figure_shape_unchanged(self):
        pack = {"checked_at": "2026-11-06", "entries": [
            {"pack_id": "ie.x", "item": "x", "value": "EUR 1", "source_url": "https://www.revenue.ie/x",
             "quote": "EUR 1", "year": 2026}]}
        figures, _sources, problems = build_library.build_country("IE", pack, "no-such-folder")
        self.assertEqual(problems, [])
        self.assertEqual(list(figures["figures"][0]), ["id", "item", "value", "tax_year", "source_url", "quote", "read_on", "used_by"])


if __name__ == "__main__":
    unittest.main()
