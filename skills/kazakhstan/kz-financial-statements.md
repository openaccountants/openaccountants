---
name: kz-financial-statements
description: >
  Use this skill whenever asked about financial statements and accounting reporting in Kazakhstan.
  Trigger on phrases like "Kazakhstan financial statements", "финансовая отчётность Казахстан",
  "do I file accounts as ИП", "IFRS Kazakhstan", "НСФО", "ТОО reporting". Explains that individual
  entrepreneurs (ИП) generally do NOT file formal financial statements, what small/medium/large
  entities (ТОО) must prepare under the National Standard or IFRS, and filing with the Depository of
  Financial Statements. ALWAYS read this before any Kazakhstan financial-reporting work.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan Financial Statements & Reporting — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| ИП (sole proprietor) | Generally **no** formal financial statements — keeps tax records and files the tax return (see kz-bookkeeping, kz-simplified-regime) |
| Small entities (ТОО) | National Financial Reporting Standard (НСФО / NFRS) — simplified |
| Medium/large & public-interest entities | IFRS (МСФО) |
| Filing | Depository of Financial Statements (web portal of the Ministry of Finance) for entities required to publish |
| Standards body | Ministry of Finance; Tax authority КГД for tax filings |
| Currency | KZT |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| ИП asking about "financial statements" | Explain ИП files tax forms, not statutory statements |
| Entity size unknown | Default ТОО to NFRS (small) until size confirmed |

## Section 2 — Who prepares what (Tier 1)
- **ИП / self-employed:** no statutory financial statements. Obligations are the **tax return** (Form 910.00 simplified or 220.00 general) plus the tax registers in kz-bookkeeping. This is the key point for most freelancers.
- **Small ТОО:** the **National Financial Reporting Standard (НСФО)** — a simplified balance sheet + income statement.
- **Medium / large / public-interest entities (banks, listed, large):** **IFRS (МСФО)**, audited.

## Section 3 — Filing & audit
- Entities meeting the public-interest / size criteria submit financial statements to the **Depository of Financial Statements** and may require a **statutory audit** — verify the size thresholds for the obligation.
- Tax reporting (to the КГД) is separate from financial-statement publication.

## Section 4 — Worked example
A solo IT freelancer registered as an ИП on the simplified regime: prepares **no** financial statements — files **Form 910.00** half-yearly plus social payments. If they later incorporate a ТОО, NFRS statements begin.

## Section 10 — Prohibitions
- NEVER tell an ИП they must file statutory financial statements (they file tax forms).
- NEVER apply IFRS to a small ТОО by default — NFRS unless size requires IFRS.
- NEVER state audit/size thresholds without verifying current law.

## Disclaimer
Informational only; not advice. Verify entity-size thresholds, standard choice, and audit/filing obligations with the Ministry of Finance / КГД. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant. Maintained at [openaccountants.com](https://www.openaccountants.com).
