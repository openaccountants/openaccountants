---
name: bd-formation
description: >
  Use this skill whenever asked how to register or start a business in Bangladesh as a freelancer or
  small business. Trigger on phrases like "register TIN Bangladesh", "trade licence Bangladesh", "how
  to start freelancing Bangladesh legally", "sole proprietorship Bangladesh", "RJSC company", "BIN VAT
  registration". Covers TIN and trade-licence registration, the sole proprietor / partnership / company
  choice, VAT (BIN) registration, and the e-commerce DBID. ALWAYS read before any Bangladesh formation.
version: 1.0
jurisdiction: BD
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Bangladesh Business Formation — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Solo vehicle | Sole proprietorship (trade licence + TIN) |
| Multi-owner | Partnership (registered under the Partnership Act) |
| Company | Private Ltd via RJSC (Registrar of Joint Stock Companies) |
| Core registrations | **TIN** (NBR, etaxnbr.gov.bd) + **trade licence** (city corporation / pourashava / union parishad) |
| VAT | **BIN** (Business Identification Number) registration with NBR if over the VAT threshold |
| E-commerce | DBID (Digital Business Identification) for online sellers |
| Quality tier | Research-verified — pending sign-off by a Bangladeshi practitioner |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| Vehicle unknown | Sole proprietorship for a solo freelancer |
| VAT registration | Required once over the threshold; voluntary below |
| Filer status | Recommend TIN + annual e-Return (avoids higher TDS) |

## Section 2 — Steps for a solo freelancer (Tier 1)
1. **Get a TIN** from the NBR (etaxnbr.gov.bd) using your NID — registers you as a taxpayer.
2. **Obtain a trade licence** from the local authority (city corporation / pourashava / union parishad) for the business name/activity.
3. **Open a business bank account** (needed for export remittances / encashment certificates).
4. **VAT (BIN):** register with the NBR if turnover exceeds the VAT-registration threshold (see bangladesh-vat).
5. **E-commerce:** obtain a **DBID** if selling online.
6. **File the annual e-Return** to stay a filer (lower TDS, access to services).

## Section 3 — Sole proprietor vs partnership vs company
| Factor | Sole proprietor | Partnership | Private Ltd (RJSC) |
|---|---|---|---|
| Setup | Trade licence + TIN | Partnership deed | RJSC incorporation |
| Liability | Personal | Shared | Limited |
| Reporting | Tax return only | Tax return | RJSC financial statements + audit |
| Best for | Solo freelancer | Partners | Scaling/investors |

## Section 10 — Prohibitions
- NEVER skip the trade licence for a registered business activity.
- NEVER omit VAT (BIN) registration once over the threshold.
- NEVER state thresholds without verifying current NBR/local rules.

## Disclaimer
Informational only; not advice. Verify registration steps and thresholds with the NBR, RJSC, and local authority. All outputs must be reviewed and signed off by a qualified Bangladeshi practitioner. Maintained at [openaccountants.com](https://www.openaccountants.com).
