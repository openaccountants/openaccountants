---
name: bd-return-assembly
description: >
  Final orchestrator that assembles the complete Bangladesh filing package for a Bangladesh-resident
  self-employed person. Trigger on phrases like "assemble my Bangladesh return", "what do I file NBR",
  "file my e-Return Bangladesh", "Bangladesh freelancer filing", "Tax Day Bangladesh". Consumes outputs
  from bd-it-freelancer-tax / bangladesh-pit, bangladesh-vat, and bd-social-contributions, and produces
  the filing checklist, forms, and deadlines. Computes nothing itself.
version: 0.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-06-12
category: orchestrator
depends_on:
  - bd-freelance-intake
tier: 2
domain: income-tax
---

# Bangladesh Return Assembly — Orchestrator v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is
The capstone for a Bangladesh-resident freelancer/sole proprietor. It sequences the upstream skills, selects forms, and produces a single pre-filing package via the NBR e-Return. It computes nothing.

## Section 1 — What you file
| Item | Where | When (verify) |
|---|---|---|
| Individual income tax return (e-Return) | NBR — etaxnbr.gov.bd | By **Tax Day** (typically 30 November for individuals) |
| Minimum tax | With the return | If a TIN holder over the threshold (৳3,000–৳5,000 by location) |
| VAT return (Mushak-9.1) | NBR (if VAT-registered) | Monthly |
| Export cash incentive claim | Through the bank | On remittance |

## Section 2 — Assembly order
1. **Intake** (bd-freelance-intake) → confirm export vs domestic, TIN, VAT, residency.
2. **Tax base** → bd-it-freelancer-tax (export, now taxable post-June-2024) and/or bangladesh-pit (slabs, investment rebate).
3. **VAT** → bangladesh-vat if registered.
4. **Social** → bd-social-contributions (voluntary Universal Pension; usually no mandatory contribution).
5. **Reconcile** remittances (encashment certificates) with declared income; gather TDS certificates for credit; apply the investment rebate.
6. **File** the e-Return via etaxnbr.gov.bd by Tax Day.

## Section 3 — Pre-filing checklist
- [ ] Export income matched to bank encashment certificates
- [ ] Domestic income on the correct slabs; expenses documented
- [ ] Investment tax rebate claimed
- [ ] TDS credits claimed; minimum tax considered
- [ ] VAT returns filed (if registered)
- [ ] e-Return filed by Tax Day

## Section 10 — Prohibitions
- NEVER assume the lapsed IT/ITES exemption when computing export income.
- NEVER omit minimum tax for a TIN holder over the threshold.
- NEVER state Tax Day / thresholds as final without verifying the current NBR calendar.

## Disclaimer
Informational only; not advice. Verify forms and deadlines with the NBR. All outputs must be reviewed and signed off by a qualified Bangladeshi tax practitioner before filing. Maintained at [openaccountants.com](https://www.openaccountants.com).
