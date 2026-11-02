---
name: kz-payroll
description: >
  Use this skill whenever asked about Kazakhstan payroll, salary taxes, or employer contributions
  for staff. Trigger on phrases like "Kazakhstan payroll", "salary tax Kazakhstan", "ОПВ ОСМС СО",
  "employer contributions Kazakhstan", "зарплатные налоги Казахстан", "ИПН с зарплаты". Covers
  individual income tax withholding, the pension contributions (ОПВ/ОПВР), social contributions (СО),
  mandatory medical insurance (ОСМС/ВОСМС), and social tax under the 2026 Tax Code. ALWAYS read this
  before any Kazakhstan payroll work.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - social-contributions-workflow-base
---

# Kazakhstan Payroll & Salary Taxes — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Item | Who pays | Rate (verify under 2026 Tax Code) |
|---|---|---|
| Individual income tax (ИПН) | Employee (withheld) | 10% |
| Mandatory pension (ОПВ) | Employee | 10% of salary |
| Employer pension contribution (ОПВР) | Employer | ~2.5% in 2025, scheduled to rise (verify 2026) |
| Social contributions (СО) | Employer | ~3.5% |
| Mandatory medical — employee (ВОСМС) | Employee | 2% |
| Mandatory medical — employer (ОСМС) | Employer | 3% |
| Social tax (СН) | Employer | ~9.5%, reduced by СО paid (verify) |
| Currency / indexation | — | KZT; MRP (МРП) ₸4,325, min wage (МЗП) ₸85,000 for 2026 (verify) |

| Field | Value |
|---|---|
| Tax authority | State Revenue Committee (КГД, kgd.gov.kz) |
| Reporting | Form 200.00 (quarterly) |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| Standard ИПН deduction (1 MZP) applicability | Apply the 14 MRP / 1 MZP monthly deduction only on the employee's main place of work |
| Contribution caps | Apply the statutory upper income cap (e.g. 50× min wage) per contribution — verify the 2026 cap |
| Employee vs ИП contractor | If the worker is a registered ИП invoicing the company, payroll does NOT apply — flag misclassification risk |

## Section 2 — Computation order (Tier 1)
1. **ОПВ 10%** is withheld from gross and is **deductible before ИПН**.
2. **ВОСМС 2%** withheld; also reduces the ИПН base.
3. Apply the **standard deduction** (1 minimum wage / 14 MRP per month, main job only).
4. **ИПН 10%** on the remaining base, withheld.
5. Employer pays, on top: **ОПВР, СО, ОСМС 3%, social tax** (social tax reduced by СО).

## Section 3 — Worked Example
Gross ₸500,000/month, main job:
- ОПВ 10% = ₸50,000; ВОСМС 2% = ₸10,000.
- Base after ОПВ + ВОСМС + 1 MZP deduction (₸85,000) = 500,000 − 50,000 − 10,000 − 85,000 = ₸355,000.
- ИПН 10% = ₸35,500. **Net to employee ≈ ₸404,500.**
- Employer on top: ОПВР, СО, ОСМС 3%, social tax (verify exact rates).

## Section 10 — Prohibitions
- NEVER apply the 1 MZP standard deduction to a second job.
- NEVER skip ОПВ-before-ИПН ordering.
- NEVER treat a registered ИП contractor as payroll — but flag disguised employment.
- NEVER state employer rates as final without verifying the 2026 Tax Code values.

## Disclaimer
Informational only; not advice. Kazakhstan contribution rates and caps changed under the 2026 Tax Code — verify all rates with the КГД. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant before use. Maintained at [openaccountants.com](https://www.openaccountants.com).
