---
name: ag-medical-benefits
description: >
  Antigua and Barbuda Medical Benefits Scheme (MBS) contributions for 2026. Covers the
  published rate categories (3.5% employee and 3.5% employer from 16 to under 60, 2.5%
  and 0% from 60 to under 70, nothing from 70, employer only 7% for wages under EC$400 a
  month or EC$100 a week), the self-employed rates of 5% and 2.5%, the R3A submission and
  the payment channels, kept apart from social security. Trigger phrases include Antigua
  medical benefits, MBS contributions, R3A, Antigua payroll medical benefits.
version: 1.0
jurisdiction: AG
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Antigua and Barbuda Medical Benefits Scheme contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions to the Antigua and Barbuda Medical Benefits Scheme (MBS) in 2026, from the Scheme's published monthly contribution rate categories. Covers employees and employers by age and earnings, the self-employed, and the R3A submission and payment channels. Amounts are EC$. Social security is a separate scheme with its own rates and ceiling: [ag-social-security](ag-social-security.md). The Scheme's table does not say that the social security ceiling applies to MBS, so do not import it.

## Ask the client first

1. Is the person employed or self-employed?
2. Date of birth (the categories change at 16, 60 and 70).
3. Pay frequency and actual wages or earnings for the period.
4. For an employee: are monthly wages under EC$400, or weekly wages under EC$100?
5. Any exemption document held?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Employed, over 16 and not yet 60 | Employee 3.5%, employer 3.5% of wages | [MBS contribution rates](https://www.mbs.gov.ag/v2/contribution-rates/) |
| Employed, 60 but not yet 70 | Employee 2.5%, employer 0% | same |
| Employed, 70 and over | Employee 0%, employer 0% | same |
| Employed, less than EC$400 monthly | Employee 0%, employer 7% | same |
| Employed, less than EC$100 weekly | Employee 0%, employer 7% | same |
| Self-employed, aged 16 but not yet 60 | 5% of earnings | same |
| Self-employed, 60 but not yet 70 | 2.5% of earnings | same |
| Self-employed, 70 and over | 0% | same |

### Steps

1. **Category.** Place each person in one category by employment status and age; for employees check the low-earnings test.
2. **Compute** the employee and employer shares on actual wages. No ceiling is published.
3. **Keep apart** from social security: separate columns, separate liability account, separate return and payment.
4. **Submit** the R3A and pay at the Nevis Street cashier, by cheque in the dropbox, online through the listed banks or by local EFT to the Scheme's account.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee aged exactly 16 | The table says "over 16" for employees but "aged 16" for the self-employed; not resolved, ask the Scheme | [MBS contribution rates](https://www.mbs.gov.ag/v2/contribution-rates/) |
| Employee aged 60 to 69 earning under EC$400 a month | Age and low-earnings categories overlap; priority not published, ask the Scheme | same |
| High earner | No MBS ceiling is published; do not apply the social security EC$6,500 cap | same |
| Combined payroll deduction for both schemes | Not enough evidence that each agency was paid; reconcile each separately | [MBS business account services](https://www.mbs.gov.ag/v2/services/business-account-services/) |

## Worked cases

### Case 1: ordinary employee and a low earner

An employee aged 35 earns EC$4,000 a month: employee 140, employer 140, total 280. A second employee aged 35 earns EC$350 a month: employee 0, employer 7% = 24.50.

```oa-check
name: MBS monthly, 4,000 ordinary and 350 low earner
inputs:
  pay: 4000
  low_pay: 350
steps:
  - employee: pay * 0.035
  - employer: pay * 0.035
  - total: employee + employer
  - low_employer: low_pay * 0.07
expected:
  employee: 140
  employer: 140
  total: 280
  low_employer: 24.5
```

### Case 2 (decision): which age category applies?

An employee earns EC$4,000 a month and turns 60. Before 60: employee 140 and employer 140. From 60: employee 2.5% = 100 and employer 0. Keeping the under-60 rates would cost the employer 140 a month and the employee 40 a month too much. Update the category from the date of birth before running payroll.

```oa-check
name: MBS employee at 4,000, under 60 against 60 to 69
inputs:
  pay: 4000
steps:
  - under60_employee: pay * 0.035
  - under60_employer: pay * 0.035
  - over60_employee: pay * 0.025
  - over60_employer: pay * 0
  - employee_saving: under60_employee - over60_employee
expected:
  under60_employee: 140
  under60_employer: 140
  over60_employee: 100
  over60_employer: 0
  employee_saving: 40
```

## When to refuse or refer

- Overlapping categories (age and low earnings) and the exact age-16 rule for employees: ask the Scheme.
- The definition of wages, exemptions, deadlines, penalties and the birthday-period treatment: the Medical Benefits Act and regulations were not read; refer.
- Benefit claims: out of scope.

## Filing and payment

1. Complete the R3A for the period.
2. Pay and submit at the Nevis Street cashier (Monday to Friday 8am to 3:30pm), the English Harbour office, the cheque-only dropbox, the ACB banking app, Community First Co-operative Credit Union, CIBC FirstCaribbean, or local EFT to the Medical Benefits Scheme account at Antigua Commercial Bank ([MBS business account services](https://www.mbs.gov.ag/v2/services/business-account-services/)).
3. Keep the R3A, the receipt and the allocation evidence; reconcile the MBS liability account each month.

## Completion checklist

- Each person in one category by status, age and earnings.
- No social security ceiling applied.
- R3A submitted and payment allocated.
- MBS reconciled separately from social security.

## Sources

| Source | URL | Read on |
|---|---|---|
| MBS contribution rates page: read for the employed, self-employed and low-earnings categories and their percentages | https://www.mbs.gov.ag/v2/contribution-rates/ | 2026-11-14 |
| MBS business account services page: read for the R3A submission, cashier hours and the payment channels including EFT | https://www.mbs.gov.ag/v2/services/business-account-services/ | 2026-11-14 |

Not yet confirmed: the payment deadline for MBS contributions; penalties and interest; whether any ceiling applies; the priority between overlapping age and low-earnings categories and the employee age-16 rule; the Medical Benefits Act and regulations behind the published table (not opened); the date the published table took effect (the page is undated).
