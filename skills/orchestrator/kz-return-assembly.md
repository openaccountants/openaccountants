---
name: kz-return-assembly
description: >
  Final orchestrator that assembles the complete Kazakhstan filing package for a Kazakhstan-resident
  self-employed person (ИП). Trigger on phrases like "assemble my Kazakhstan return", "what do I file
  in Kazakhstan", "Form 910 filing", "ИП отчётность Казахстан". Consumes outputs from kz-simplified-regime
  or kz-income-tax, kz-social-contributions, and kazakhstan-vat, and produces the filing checklist,
  forms, and deadlines. Computes nothing itself.
version: 0.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-06-12
category: orchestrator
depends_on:
  - kz-freelance-intake
tier: 2
---

# Kazakhstan Return Assembly — Orchestrator v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is
The capstone for a Kazakhstan-resident ИП. It sequences the upstream skills, picks the right forms by regime, and produces a single pre-filing package. It does not compute tax — it assembles.

## Section 1 — Which forms apply

| Regime | Main tax form | Frequency |
|---|---|---|
| Simplified declaration | **Form 910.00** | Half-yearly (by 15 Aug / 15 Feb; pay by 25 Aug / 25 Feb) — verify |
| General regime (ИП) | **Form 220.00** | Annual (by 31 March following year) — verify |
| With employees / withholding | **Form 200.00** | Quarterly |
| VAT-registered | **Form 300.00** | Quarterly |

## Section 2 — Assembly order
1. **Intake** (kz-freelance-intake) → confirm regime, VAT status, residency.
2. **Tax base** → kz-simplified-regime (4% turnover) **or** kz-income-tax (10% net).
3. **Social payments** → kz-social-contributions (ОПВ, ОПВР, СО, ВОСМС).
4. **VAT** → kazakhstan-vat (if registered).
5. **Reconcile** turnover across forms; confirm МРП-indexed thresholds.
6. **Submit** via the **e-Salyq / cabinet.salyk.kz** Taxpayer Cabinet with a digital signature (ЭЦП).

## Section 3 — Pre-filing checklist
- [ ] Regime confirmed (simplified / general)
- [ ] Turnover within the regime ceiling
- [ ] Social payments (ОПВ/ОПВР/СО/ВОСМС) computed and within caps
- [ ] VAT return filed if registered
- [ ] Correct form (910.00 / 220.00 / 200.00 / 300.00) and deadline
- [ ] Filed via Taxpayer Cabinet with valid ЭЦП

## Section 10 — Prohibitions
- NEVER file without confirming the regime and the matching form.
- NEVER state a deadline as final without verifying the 2026 calendar on cabinet.salyk.kz.
- NEVER present the package as filed-ready without a qualified accountant's review.

## Disclaimer
Informational only; not advice. Verify forms and deadlines with the КГД. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant before filing. Maintained at [openaccountants.com](https://www.openaccountants.com).
