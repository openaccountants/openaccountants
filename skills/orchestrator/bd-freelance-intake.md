---
name: bd-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with their Bangladesh taxes AND mentions freelancing, self-employment, sole proprietorship, IT/ITES exports, or being a business individual in Bangladesh. Trigger on phrases like "help me with my Bangladesh taxes", "I'm a freelancer in Bangladesh", "I do IT export from Bangladesh", "file my NBR return", "I'm self-employed in Bangladesh". REQUIRED entry point for the Bangladesh self-employed workflow — downstream skills (bd-it-freelancer-tax, bangladesh-pit, bd-social-contributions, bangladesh-vat, bd-return-assembly) depend on it. Upload-first; Bangladesh-resident individuals only.
version: 0.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-06-12
category: orchestrator
tier: 2
---

# Bangladesh Self-Employed Intake — Orchestrator v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is
Intake orchestrator for Bangladesh-resident self-employed individuals (freelancers, IT/ITES exporters, sole proprietors). Collects facts, parses documents, confirms, hands off a structured package. Computes nothing.

## Step 1 — Refusal sweep (route correctly)
1. **Foreign clients (IT/ITES export) or domestic income?** → bd-it-freelancer-tax vs bangladesh-pit.
2. **Income above the tax-free threshold (~৳350,000)?** → whether a return/tax is due (minimum tax may still apply if you have a TIN and cross thresholds).
3. **Do you have a TIN / file an e-Return?** → registration status.
4. **VAT-registered / turnover over the VAT threshold?** → bangladesh-vat.
5. **Resident this year (≥182 days, or 90 days + 365 over 4 years)?** → non-residents escalate.

Defaults if unanswered: resident sole proprietor, assume IT/ITES income now taxable (post-June-2024), encourage TIN + e-Return.

## Step 2 — Collect
- Bank statements for the full tax year (1 Jul–30 Jun), incl. foreign remittances.
- Platform statements (Upwork/Fiverr/direct invoices); remittance proof / cash-incentive records.
- TIN, prior e-Return, trade licence.

## Step 3 — Infer & confirm
- Separate **export income** (banking-channel remittances → bd-it-freelancer-tax) from **domestic income** (→ bangladesh-pit).
- Note any ICT/ITES **cash incentive** on remittances.
- Confirm VAT exposure and minimum-tax position.

## Step 4 — Hand off
- **IT/freelance exporter:** bd-it-freelancer-tax + bangladesh-pit (slabs) → bd-return-assembly.
- **Domestic business:** bangladesh-pit + bangladesh-vat (if registered) + bd-social-contributions (voluntary pension) → bd-return-assembly.

## Disclaimer
Intake only; computes no tax. All downstream outputs must be reviewed and signed off by a qualified Bangladeshi tax practitioner before filing. Maintained at [openaccountants.com](https://www.openaccountants.com).
