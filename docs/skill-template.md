# Frontmatter spec — the canonical reference

**This section is THE frontmatter spec for every skill/skill file in this repo.** Other docs (`CLAUDE.md`, `CONTRIBUTING.md`) link here rather than restating it. CI enforces it: `scripts/validate-guides.py` hard-fails on malformed frontmatter, a missing `name`/`description`, a non-integer `tax_year`, a missing or invalid `tier` (must be 1 or 2), a missing or malformed `last_updated` (YYYY-MM-DD), and a missing `jurisdiction` (except in a small allowlist of jurisdiction-agnostic directories, where it warns).

## Required keys

| Key | Format | Notes |
|-----|--------|-------|
| `name` | slug, `[country-or-topic]-[domain]` | e.g. `malta-income-tax` |
| `description` | 80-100 words | What it covers, entity types, jurisdiction, tax year, plus trigger phrases the AI should match |
| `jurisdiction` | ISO code | `MT`, `GB`, `DE`, `US`, `US-CA`, `GLOBAL`, `INTL`, `EU-27`. Required even when the folder path implies it. Quote `"NO"` because YAML 1.1 otherwise reads Norway's code as boolean `false` |
| `category` | one of the vocabulary below | Domain the skill covers |
| `tax_year` | **bare integer**, e.g. `2025` | The **coverage start year**. Ranges, fiscal calendars, and qualifiers ("2025-26", "YA 2026", "2567 (2024)") go in the body text, never here. CI errors on anything that is not an integer 2015-2035 |
| `tier` | `1` or `2` | Legacy machine field. `1` = checked by an accountant other than the author (`reviewed_by:` names them); `2` = not independently checked (team-built or Accountant-authored). The three attribution states are described under `trust_label` below |
| `last_updated` | `YYYY-MM-DD` | Date the content was last checked/edited. It must never move backwards |

## Optional keys

| Key | Format | Notes |
|-----|--------|-------|
| `tax_year_notes` | quoted string | The human-readable tax-year label when a bare year can't express it: `"2025-26"`, `"FY 2026-27 (AY 2027-28)"`, `"2025 (with confirmed 2026 figures noted)"`. The platform does not store this key, so the daily export drops it when it re-renders a skill. Put the year label in the body text, such as a "Tax year" row in the quick-reference table, so it survives |
| `authored_by` | `Name` or `Name, Credential` | The named accountant who wrote the skill (Accountant-authored state). Team rewrites carry `Michael Cutajar and the OpenAccountants team`. Pair it with the matching `trust_label` |
| `trust_label` | one of three values | `Built by Michael Cutajar and the OpenAccountants team` (team-built, source-cited, no named accountant); `Accountant-authored` (a named accountant approved on openaccountants.com wrote it, not yet independently checked); `Checked by <Name>` (an accountant other than the author checked the complete skill). Every skill is in exactly one state |
| `reviewed_by` | `Name` or `Name, Credential` | The accountant other than the author who checked the complete skill, e.g. `Christopher Aryee, CPA`. Goes with `review_status: current`, `trust_label: Checked by <Name>` and `tier: 1` |
| `verified_by` | retired | Do not add; the export removes it. Three legacy files still carry `verified_by: pending` until their next export |
| `depends_on` | YAML list of slugs | Workflow base or country skill this loads on top of |
| `version` | numeric dotted value, e.g. `0.1` | Content version, bumped on substantive change when present. Keep any body-heading version in step |

## Platform-written keys

The daily export from openaccountants.com (see [WEBSITE-SYNC.md](WEBSITE-SYNC.md)) writes these keys when it renders a skill. Do not add or edit them in a PR: the platform owns their values and rewrites them on the next export. Leave them in place when you edit a skill that already carries them. `trust_label` is the attribution state the website shows; `tier` is the legacy machine field; `review_status` records whether the current text still carries its check. `scripts/validate-guides.py` ignores keys it does not know, so a key outside this document is undefined, not validated.

| Key | Values seen | Notes |
|-----|-------------|-------|
| `review_status` | `current` or `pending_review` | `current` means the text as it stands was checked by the accountant in `reviewed_by`. A substantive edit sets the skill back to `pending_review` until it is checked again |
| `license` | `AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)` | Written verbatim by the export. [LICENSING.md](../LICENSING.md) is the licence reference |
| `authored_by` | see Optional keys | The export writes `Michael Cutajar and the OpenAccountants team` on team rewrites, or the accountant's name on Accountant-authored skills |
| `trust_label` | see Optional keys | The export writes the state it computes from the platform: `Built by Michael Cutajar and the OpenAccountants team`, `Accountant-authored`, or `Checked by <Name>` |

The export has also written `drafted_by` and `approved_by` (61 skills, values `OpenAccountants` and `pending`), `validation_status` (5) and `validated` (4). Treat them the same way: leave them alone and do not add them to new files.

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

## Template

---

```yaml
---
name: [country-or-topic]-[domain]
description: >
  [One paragraph: what this skill covers, entity types, jurisdiction, tax year.
  Include trigger phrases the AI should match. Be specific about scope.]
jurisdiction: XX   # REQUIRED — MT, GB, DE, US, US-CA, GLOBAL, INTL, EU-27, etc.
category: international   # see the category vocabulary above
tax_year: 2025             # bare integer = coverage start year
tax_year_notes: "2025-26"  # optional; the export drops it, so repeat the label in the body
tier: 2                    # legacy: 1 = checked by a second accountant | 2 = not independently checked
last_updated: 2026-07-04   # YYYY-MM-DD
version: 0.1
depends_on:
  - [workflow-base-or-country-skill]
# Do not add verified_by (retired). authored_by, trust_label, reviewed_by and
# review_status are written by the platform export; see Platform-written keys.
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

The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
