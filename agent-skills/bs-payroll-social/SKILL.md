---
name: bs-payroll-social
description: "Bahamas employer payroll and National Insurance (NIB) for 2026. There is no income tax and no PAYE, so payroll means NIB contributions on insurable wages at the rates in force since 1 July 2024 (employee 4.65%, employer 6.65%, combined 11.30%; self-employed 10.30%; voluntarily insured 6.50%), the reduced employer-only 2.0% for pensioners in work, and the employer's duty to deduct and pay both shares. Trigger on Bahamas payroll, NIB contributions, National Insurance Board Bahamas, C10 form, employer NIB rate. Built from the National Insurance (Contributions) (Amendment) Regulations 2024; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bs-payroll-social"
  jurisdiction: "BS"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Bahamas payroll and National Insurance

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers paying wages in The Bahamas in 2026, and self-employed and voluntarily insured persons paying their own NIB. Tax year: calendar 2026. Authority: National Insurance Board (NIB). Amounts are BSD.

There is no income tax in The Bahamas, so no income tax is withheld from wages: NIB is the only payroll deduction set by law. The individual's position (no income tax, business licence) is in `bs-income-tax`.

## Rates, bands and thresholds

| Category | Employee | Employer | Total | Source |
|---|---|---|---|---|
| Employed persons (general) | 4.65% (computed from the Fifth Schedule rates and the 1.5 point increase) | 6.65% | 11.30% | National Insurance (Contributions) (Amendment) Regulations 2024, reg. 4 (new reg. 23(1A)) and reg. 9 (Fifth Schedule): https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf |
| Fifth Schedule base before the increase | 3.9% | 5.9% | 9.8% | same |
| Increase from 1 July 2024 | 0.75 points | 0.75 points | 1.5 points, shared equally | same |
| Employed, earning under 50% of the ceiling and in receipt of retirement benefit | 0% | 2.0% | 2.0% | same |
| Employed, 65 or over and in receipt of retirement benefit | 0% | 2.0% | 2.0% | same |
| Persons employed during the summer | 0% | 2.0% | 2.0% | same |
| Self-employed under 65, not receiving retirement benefit | 10.30% (computed from the Fifth Schedule rates and the 1.5 point increase) | | 10.30% | Regs 2024, reg. 5 (new reg. 30(1A)): 8.8% plus 1.5 points: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf |
| Voluntarily insured | 6.50% (computed from the Fifth Schedule rates and the 1.5 point increase) | | 6.50% | Regs 2024, reg. 7 (new reg. 35(1A)): 5.0% plus 1.5 points: https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf |
| Insurable wage ceiling | BSD 810 a week | Effective July 2024; contributions stop at the ceiling; no later ceiling shown on the NIB page read | NIB, contributions: https://www.nib-bahamas.com/contributions |
| Payment deadline | Received by NIB by the 15th of the month after the month the contributions were due | Monthly | same |
| Contribution week | Monday to Sunday | One contribution a week per worker, paid by the principal employer | same |
| Retirement benefit recipients aged 60 to 64 earning under half the ceiling | 2.0%, employer only (employed); 2.0% (self-employed) | | same |
| Income tax withheld | None | | | No income tax Act, Bahamas legislation index: https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html |

## The base

1. Insurable wage: the wage earned in each contribution week (Monday to Sunday), capped at BSD 810 a week. Commission earners: the average weekly or monthly wage of the previous year, or the actual wage for the period; daily or piece workers: the lower of the basic wage for similar work and the actual cash paid (NIB).
2. Employee share 4.65%, employer share 6.65% of the insurable wage; the employer deducts the employee share from pay (reg. 19(1) as amended: for each employee at the end of every month).
3. Pensioner categories: the employer pays 2.0% and the employee nothing.
4. Self-employed persons pay 10.30% on insurable income themselves; voluntary contributors 6.50%.
5. Deduct from the first pay, including probation. Contributions not deducted when due cannot be recovered from later pay; the employer alone owes the arrears (NIB).
6. A late contribution paid within 12 months after the end of the year it fell due counts as paid on time for retirement and invalidity benefit (reg. 16 as replaced).

## Deadlines and filing

- Employers register with NIB before paying wages and pay monthly so that payment reaches NIB by the 15th of the following month.
- Self-employed persons register (form R1) and pay monthly.

## Penalties and interest

The NIB late payment surcharge and interest were not confirmed from a source opened today; see Not yet confirmed. Do not advise a client in NIB arrears or under enforcement: refer to a Bahamian accountant.

## Cross-border points

- Foreign employees working in The Bahamas are employed persons for NIB in the same way; no income tax applies to them either.
- Any social security agreement and work permit questions: refer.

## Two worked examples that recompute

### Three employees at BSD 600 a week

A small business pays three employees BSD 600 a week each, below the BSD 810 weekly ceiling.

```oa-check
name: BS NIB three employees at 600 a week, 2026
inputs:
  weekly_wage: 600
  staff: 3
steps:
  - employee_week: weekly_wage * 0.0465
  - employer_week: weekly_wage * 0.0665
  - combined_week_each: employee_week + employer_week
  - combined_week_all: combined_week_each * staff
  - employer_year_all: employer_week * staff * 52
expected:
  employee_week: 27.90
  employer_week: 39.90
  combined_week_each: 67.80
  combined_week_all: 203.40
  employer_year_all: 6224.40
```

Each employee has BSD 27.90 a week deducted; the employer adds BSD 39.90 a week each, BSD 6,224.40 a year for all three.

### Decision: employee or self-employed contractor at BSD 31,200 a year

The same person earns BSD 31,200 (BSD 600 a week).

- **Employee:** employee pays 4.65% = BSD 1,450.80; employer pays 6.65% = BSD 2,074.80; total NIB BSD 3,525.60.
- **Self-employed:** the person pays 10.30% = BSD 3,213.60 and the business pays nothing.

The business saves BSD 2,074.80, and the person pays BSD 1,762.80 more. Whether someone is really self-employed is a question of fact under the National Insurance Act; labelling does not decide it.

```oa-check
name: BS NIB employee vs self-employed, 31200
inputs:
  annual: 31200
steps:
  - employee_share: annual * 0.0465
  - employer_share: annual * 0.0665
  - employed_total: employee_share + employer_share
  - self_employed: annual * 0.103
  - business_saving: employer_share
  - person_extra: self_employed - employee_share
expected:
  employee_share: 1450.80
  employer_share: 2074.80
  employed_total: 3525.60
  self_employed: 3213.60
  person_extra: 1762.80
```

## Ask the client first

1. Number of employees and each one's weekly wage.
2. Ages, and does anyone receive an NIB retirement benefit (2.0% employer-only categories)?
3. Any summer-only workers?
4. Is the employer registered with NIB, and are contributions up to date?
5. Self-employed or voluntarily insured persons: insurable income for 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| National Insurance (Contributions) (Amendment) Regulations 2024, S.I. 37 of 2024, in force 1 July 2024: read for the Fifth Schedule rates by category and the 1.5 point increases for employed, self-employed and voluntary contributors | https://laws.bahamas.gov.bs/cms/images/LEGISLATION/AMENDING/2024/2024-0037S/2024-0037S.pdf | 2026-11-14 |
| NIB, contributions page (opened with Firecrawl because it is built by script): read for the BSD 810 weekly ceiling, the 15th day deadline, the contribution week, the rates and the retiree 2.0% rows | https://www.nib-bahamas.com/contributions | 2026-11-14 |
| Bahamas legislation, Acts by year: read to confirm there is no income tax Act and no 2026 National Insurance amendment | https://laws.bahamas.gov.bs/cms/legislation/acts_only/acts-by-year.html | 2026-11-14 |
| Bahamas legislation, subsidiary legislation by year 2024 to 2026: read to find the 2024 contributions regulations and that no later contributions regulations are listed | https://laws.bahamas.gov.bs/cms/legislation/subsidiary/subsidiary-by-year.html | 2026-11-14 |

Not yet confirmed: whether the ceiling changes from July 2026 (old file: BSD 830 a week; the NIB page read still shows BSD 810 effective July 2024) and the monthly ceiling (old: BSD 3,510); the C10 form name; the NIB late payment surcharge and interest; fines for failing to register an employer (old file: up to BSD 5,000).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bs-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bs-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
