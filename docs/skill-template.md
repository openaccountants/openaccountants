# How to write a skill: the standard

**This file is the one standard for every skill in this repository.** It applies to every writer, human or AI (Claude, ChatGPT, Codex, Gemini or anything else), and to every accountant who contributes. `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md` and `OWNERS.md` point here. If another document says something different, this file wins; fix the other document in the same PR.

The repository is treated as tax law. Every figure must be traceable to the law that sets it.

## The ten rules

1. **Primary sources only.** Every rate, threshold, deadline and penalty comes from the law itself (the official gazette or law register) or the tax authority's own pages, fetched by you, for the tax year the skill covers. Never cite PwC, KPMG, Deloitte, EY, taxsummaries, blogs, law-firm notes or another AI. A secondary source may help you find the law; it is never the citation.
2. **The statute wins.** If a tax authority page disagrees with the current law text, follow the law, cite it, and note the outdated page.
3. **When a site blocks scripts,** open it in a normal browser tab and read it there. Never solve a CAPTCHA or human check. If a site refuses every connection, use an Internet Archive (web.archive.org) copy captured in the current year and say so in the Sources table.
4. **Cite the article.** Every row of the rates table names the act and article (e.g. "ZKPO art. 20") and links the official text.
5. **Read dates.** The `## Sources` table records the date each source was read.
6. **Nothing unconfirmed goes in.** If you cannot confirm a figure or rule from an official source, leave it out of the skill and list it on the "Not yet confirmed:" line at the end of `## Sources`.
7. **Tax skills use the deep-tax shape** (below): nine sections in order, a rates table, and exactly two worked examples whose `oa-check` blocks recompute in CI.
8. **Current tax year.** `tax_year` is the year the figures apply to. A skill with an old `tax_year` makes its pack partial. When a law changes mid-year, give both periods with their dates.
9. **Independent review before merge.** Someone other than the writer (a person or a separate AI agent with no shared context) re-reads the cited law, checks every figure, recomputes both examples, fixes what is wrong, and posts a PR comment: figures checked, fixes made with sources, items still not confirmed. Only then does the PR merge, as a source-cited draft (`tier: 2`).
10. **Accountant sign-off is the only route to tier 1.** A licensed accountant reviews the whole skill and sets `tier: 1`, `reviewed_by` and `reviewed_on`. No one else sets these keys.

## Updating an existing skill

- Rewrite in place; keep the slug.
- `version` and `last_updated` only go up. Set `version` one step above main's, and keep any version in the body heading the same (CI `compare` fails otherwise).
- Keep a team byline or `trust_label` as it is. Remove a named outside reviewer only when the content they reviewed has changed (a changed skill loses its review and returns to source-cited draft).
- Fix contradictions you find in sibling skills in their own PR, not as a bonus edit.

## Pack README

Each jurisdiction folder has a `README.md` (see [pack-readme-template.md](pack-readme-template.md)). A domain whose skills still carry an old tax year, or leave out a group of taxpayers or a core computation most clients need, gets a `partial:` entry with the reason in double quotes. Remove the entry only when the gap is closed. Niche regimes, special VAT schemes and treaty-rate tables are named out of scope in the README; they do not make a domain partial.

## Checks before you open a PR

```
python3 scripts/check-examples.py <skill.md>
python3 scripts/validate-guides.py --no-index-check
python3 scripts/coverage-report.py --json
```

Edit `skills/**` only. Never edit `packages/`, `index.json` or `llms-full.txt`, and do not add or edit the platform-written keys listed below or the `openaccountants-cta-block`.

# Frontmatter spec

**This section is THE frontmatter spec for every skill/skill file in this repo.** Other docs (`CLAUDE.md`, `CONTRIBUTING.md`) link here rather than restating it. CI enforces it: `scripts/validate-guides.py` hard-fails on malformed frontmatter, a missing `name`/`description`, a non-integer `tax_year`, a missing or invalid `tier` (must be 1 or 2), a missing or malformed `last_updated` (YYYY-MM-DD), and a missing `jurisdiction` (except in a small allowlist of jurisdiction-agnostic directories, where it warns).

## Required keys

| Key | Format | Notes |
|-----|--------|-------|
| `name` | slug, `[country-or-topic]-[domain]` | e.g. `malta-income-tax` |
| `description` | 80-150 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false` |
| `category` | one of the vocabulary below | Domain the skill covers |
| `tax_year` | **bare integer**, e.g. `2025` | The **coverage start year**. Ranges, fiscal calendars, and qualifiers ("2025-26", "YA 2026", "2567 (2024)") go in the body text, never here. CI errors on anything that is not an integer 2015-2035 |
| `tier` | `1` or `2` | `1` = **accountant-reviewed** (a named licensed accountant fully reviewed and signed off); `2` = **source-cited draft** (drafted from primary sources, awaiting review). These are the only two quality states |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`, `"2025 (with confirmed 2026 figures noted)"`. The platform does not store this key, so the daily export drops it when it re-renders a skill. Put the year label in the body text, such as a "Tax year" row in the quick-reference table, so it survives |
| `verified_by` | legacy | Do not add to new skills. The platform is retiring it; accountant review uses `reviewed_by` and `reviewed_on` (rule 10) |
| `reviewed_by` | `Name, Credential` | Set only by a licensed accountant who reviewed the whole skill, with `reviewed_on` (`YYYY-MM-DD`) and `tier: 1` |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change when present. Keep any body-heading version in step |

## Platform-written keys

The daily export from openaccountants.com (see [WEBSITE-SYNC.md](WEBSITE-SYNC.md)) writes these keys when it renders a skill. Do not add or edit them in a PR: the platform owns their values and rewrites them on the next export. Leave them in place when you edit a skill that already carries them. None of them is a quality state; `tier` remains the only quality field, and `review_status` records where the accountant review stands. `scripts/validate-guides.py` ignores keys it does not know, so a key outside this document is undefined, not validated.

| Key | Values seen | Notes |
|-----|-------------|-------|
| `review_status` | `current` or `pending_review` | Whether the current text carries a professional review. A substantive edit sets the skill back to `pending_review` until it is reviewed again |
| `license` | `AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)` | Written verbatim by the export. [LICENSING.md](../LICENSING.md) is the licence reference |
| `authored_by` | `OpenAccountants team` | Present when the platform team, not a named accountant or GitHub contributor, authored the current revision |
| `trust_label` | `By OpenAccountants` | Display attribution for the website. Not a review claim |

The export has also written `drafted_by`, `approved_by`, `validation_status` and `validated` on some skills (`grep -rl "^drafted_by:" skills/` lists them). Treat them the same way: leave them alone and do not add them to new files.

## Sync integrity rules

`last_updated` and a numeric `version` are monotonic content metadata: an edit
must not decrease either value. A substantive body change should advance the
date, the version, or both, and a heading such as `v1.1` must agree with the
frontmatter version.

These values are not synchronization tokens. The platform exporter must still
compare its stored Git blob hash with the current repository blob before it
rewrites an existing `skills/**` file. See [WEBSITE-SYNC.md](WEBSITE-SYNC.md)
for the fail-closed compare-and-swap contract and pre-push command.

## Category vocabulary (the real one)

This is the vocabulary actually in use across the repo's guides (by count), not an aspirational list. Use these for new files:

| Category | What it means | Approx. usage |
|----------|---------------|---------------|
| `international` | Country-level tax computation (income tax, VAT, SSC) | ~757 |
| `foundation` | Universal workflow base (domain-agnostic) | ~198 |
| `orchestrator` | Router / intake / assembly files | ~110 |
| `federal` | US federal tax | ~104 |
| `payroll` | Withholding, social security, payslips | ~82 |
| `tax-optimization` | Legal tax reduction strategies, timing, deductions | ~64 |
| `cross-border` | Multi-jurisdiction coordination, treaties, WHT | ~54 |
| `transfer-pricing` | TP documentation, arm's length, CbCR | ~43 |
| `state-tax` | US state tax | ~40 |
| `formation` | Entity types, registration, compliance | ~39 |
| `financial-statements` | Annual accounts, reporting, audit | ~39 |
| `bookkeeping` | Chart of accounts, P&L, balance sheet | ~39 |
| `invoicing` | E-invoicing format, validation, transmission | ~30 |
| `crypto` | Cryptocurrency and digital asset taxation | ~30 |
| `vertical` | Industry-specific accounting patterns | ~28 |
| `integration` | Platform export formats, column mappings | ~20 |

Legacy synonyms still present in older files — do **not** use for new files: `federal-tax` (use `federal`), `state` / `us-states` (use `state-tax`), `financial-reporting` (use `financial-statements`), plus stragglers `template`, `pattern(s)`, `intelligence`.

## General template (accounting packs only)

Bookkeeping, e-invoicing, financial statements and tax optimisation skills use this general template. **Tax skills (IT-IND, IT-CORP, VAT, SC, PR, TP, XB) use the deep-tax shape further down, not this.**

---

```yaml
---
name: [country-or-topic]-[domain]
description: >
  [One paragraph: what this skill covers, entity types, jurisdiction, tax year.
  Include trigger phrases the AI should match. Be specific about scope.]
jurisdiction: XX   # REQUIRED — MT, GB, DE, US, US-CA, GLOBAL, INTL, EU-27, etc.
category: international   # see the category vocabulary above
tax_year: 2026             # bare integer = the year the figures apply to
tax_year_notes: "2025-26"  # optional; the export drops it, so repeat the label in the body
tier: 2                    # 1 = accountant-reviewed | 2 = source-cited draft
last_updated: 2026-07-04   # YYYY-MM-DD
version: 0.1
depends_on:
  - [workflow-base-or-country-skill]
---
```

# [Skill Name] v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Jurisdiction is required.** Set `jurisdiction:` in frontmatter even when the folder path implies it (e.g. `skills/international/malta/` → still use `jurisdiction: MT`). Sync to openaccountants.com skips files without a resolvable jurisdiction. See [WEBSITE-SYNC.md](WEBSITE-SYNC.md).

## What this file is

**This file is a content skill that loads on top of a workflow base** (e.g. `us-tax-workflow-base`, `crypto-tax-workflow-base`, `bookkeeping-workflow-base`).

[Describe: what it computes, where it fits in the pipeline, what it does NOT cover.
Reference the upstream skills it depends on and the downstream skills that consume its output.]

**Tax year coverage.** This skill is current for **tax year 2025-26** as of its currency date.

**The reviewer is the customer of this output.** Per the base, this skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- [What forms and schedules]
- [What entity types — sole prop, SMLLC, etc.]
- [What line items or computations]

This skill does NOT cover:

- [What's out of scope — reference which other skills handle it]

---

## Section 2 — Filing requirements

[Who must file, thresholds, deadlines. Cite the state statute or IRC section.]

---

## Section 3 — Rates and thresholds

[All dollar amounts, percentages, phase-outs for the tax year.
Each figure must have a primary source citation.]

| Item | Amount | Source |
|------|--------|--------|
| [Rate/threshold] | [$X] | [Statute § or Notice] |

---

## Section 4 — Computation rules

[Step-by-step computation logic. This is the core of the skill.
Write it so Claude can execute it mechanically.]

### Step 1 — [Name]

[Rule with citation]

### Step 2 — [Name]

[Rule with citation]

---

## Section 5 — Edge cases and special rules

[Unusual situations, exceptions, elections, safe harbors.
Each with a citation.]

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All input figures trace to source documents
- [ ] Rates and thresholds match the tax year
- [ ] Computation follows the steps in Section 4
- [ ] Edge cases from Section 5 are checked
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## The deep-tax shape (GOAL.md, 22 October 2026)

Every tax skill (IT-IND, IT-CORP, VAT, SC, PR, TP, XB) has these sections, in this order, so an AI reading any two jurisdictions finds the same things in the same places:

1. **Who this applies to.** Residence and scope rules; who is in and who is out.
2. **Rates, bands and thresholds.** A table: item, amount, tax year, official source URL. No figure without a source.
3. **The base.** What is taxed, what is deductible or exempt, how losses work.
4. **Deadlines and filing.** Registration, returns, payments, instalments, what form, where it is filed.
5. **Penalties and interest.** Late filing, late payment, under-declaration; the figures, sourced.
6. **Cross-border points.** Non-residents, treaties, withholding, exit rules that touch this domain.
7. **Two worked examples that recompute.** One simple, one with an edge case. Each has the prose walk-through for the reader and, under it, an `oa-check` block that CI recomputes with `scripts/check-examples.py`:

   ```oa-check
   name: Sole trader, profit EUR 40,000 (2026 bands)
   inputs:
     profit: 40000
   steps:
     - band_15: (min(profit, 14500) - 9100) * 0.15
     - band_25: (min(profit, 19500) - 14500) * 0.25
     - band_35: (profit - 19500) * 0.35
     - tax: band_15 + band_25 + band_35
   expected:
     tax: 9235.00
   ```

   Arithmetic only: inputs, named steps, `+ - * /`, and `min max abs round floor ceil pct clamp`. Decimal maths; a value matches within `tolerance` (default 0.01). A wrong expected value fails the PR.
8. **Ask the client first.** The three to six facts that change the answer.
9. **Sources.** A `## Sources` section, last in the file, listing every official page the figures came from, with the date it was read:

   ```markdown
   ## Sources

   | Source | URL | Read on |
   |---|---|---|
   | Income Tax Act, Cap. 123, art. 56 | https://legislation.mt/eli/cap/123/eng | 2026-10-22 |
   | MTCA, 2026 tax rates | https://mtca.gov.mt/... | 2026-10-22 |
   ```

   `scripts/validate-guides.py` warns when a tax skill has no `## Sources` section with a URL, and when `last_updated` is over a year old or `tax_year` is two or more years behind. Both become errors once the backlog is cleared. Sources live in the body, not in a frontmatter key, because the platform export re-renders frontmatter and drops keys it does not store.

Bookkeeping, e-invoicing, financial statements and tax optimisation skills keep the general template and belong to the Accounting packs milestone.
