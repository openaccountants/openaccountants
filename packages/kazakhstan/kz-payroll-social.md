---
name: kz-payroll-social
description: "Kazakhstan 2026 payroll component checklist: route employee deductions and employer costs to their owning computations and reconcile remittances."
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax

version: 0.1
type: router
category: international
---

# Kazakhstan payroll and social component routing v0.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Scope

A component-level payroll and social-payment checklist. The computation homes are `kz-payroll` for salary ИПН/net pay and `kz-social-contributions` for ОПВ, ОПВР, СО, ОСМС and СН. This replaces the old approximate combined-load card, preserving every component through explicit handoffs. Employee money withheld and employer money paid are separate.

## Ask the client first

- Employee/ИП/self-employed status, residence and payroll period?
- Gross eligible pay and contribution exemptions/caps?
- Employer legal form and regime?
- Prior payments, declared income and tax-agent deduction evidence?

## The method, step by step

1. Load `kz-payroll` and its current resident progressive ИПН computation; do not use a flat salary shortcut after the annual threshold.
2. Load `kz-social-contributions` for employee ОПВ and its monthly cap; employee ВОСМС; employer ОПВР phase-in/birth exemptions; СО; employer ОСМС; and the legal-entity versus fixed-ИП social-tax base.
3. Keep historical 2025 rates separate from 2026. The old combined approximate payroll load is not a legal rate. The old social-tax offset does not apply in 2026. The index and minimum wage are in `kz-tax-overview`; validate inputs there rather than copying old values.
4. Reconcile employee net pay and employer total cost. Route remittance dates and beneficiary/cap evidence to `kz-social-contributions`, withholding/quarterly reporting to `kz-payroll`, then acceptance/payment checks to `kz-return-assembly`. Do not count employer costs as employee deductions.

## Worked cases

Case 1: hypothetical gross KZT 500,000, employee pension 50,000, health 10,000 and reviewed ИПН 31,025 give net KZT 408,975. An employer charge of KZT 71,150 is paid on top, so total employer cost is KZT 571,150. All component inputs must come from the owning computations.

```oa-check
name: Separate withheld and employer-funded components
inputs:
  gross: 500000
  pension: 50000
  employee_health: 10000
  pit: 31025
  employer_charges: 71150
steps:
  - net: gross - pension - employee_health - pit
  - employer_cost: gross + employer_charges
expected:
  net: 408975
  employer_cost: 571150
```

Case 2: hypothetical payroll deductions/fund remittances are KZT 60,000 employee funds plus KZT 71,150 employer funds. Total fund obligations are KZT 131,150; KZT 100,000 already allocated leaves KZT 31,150, before separately accounting for ИПН.

```oa-check
name: Fund remittance reconciliation
inputs:
  employee_funds: 60000
  employer_funds: 71150
  allocated: 100000
steps:
  - total: employee_funds + employer_funds
  - remaining: total - allocated
expected:
  total: 131150
  remaining: 31150
```

## When to refuse or refer

Refer foreign/EAEU staff, exempt service/disability/pension cases, unified-payment elections, multiple payers or disputed employment status. Never apply an approximate combined percentage, invent a missing component, duplicate employee/employer costs or treat the presence of a professional review disclaimer as approval.

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 363, 438–445 and 555–561 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for Social Code arts. 243–251 | https://www.gov.kz/org/astana-uzsp/documents/details/1060115?lang=ru | 2026-11-14 |
| Read for Health Fund employer/employee/ИП rates and caps | https://www.gov.kz/org/minfin/press/article/details/235407?lang=ru | 2026-11-14 |

Not yet confirmed: A universal combined payroll-load percentage: the old roughly 23%–24% claim was not a reliable legal rule. All current component rates, caps, 2026 phase-in, birth/exemptions, minimum wage and remittance dates are preserved in the explicitly linked computation homes.
