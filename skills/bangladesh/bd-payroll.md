---
name: bd-payroll
description: "Bangladesh 2026 salary tax withholding workflow: annual estimate, current individual relief, average-rate deduction, in-year corrections and remittance evidence, with employer fund duties kept separate."
version: 1.1
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - social-contributions-workflow-base
tier: 2
domain: payroll
type: computation
---

# Bangladesh salary withholding v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Employers paying Bangladesh employment income. Covers the salary-tax estimate/deduction working paper, not every payroll labour-law entitlement. A solo proprietor without staff has no employee payroll merely by making drawings.

## Ask the client first

- Employee residence/citizenship, period and taxpayer category.
- Annual salary, benefits, bonuses and other relevant employment details.
- Verified eligible investments/reliefs and prior/current source deductions.
- Pay dates, treasury challans, withholding-return status and fund obligations.

## The method, step by step

### Withholding rate

| Item | Rate and conditions | Official source |
|---|---|---|
| Employment-income payment | Average tax rate on estimated annual employment income; adjust current-year shortfall/excess as allowed | Income Tax Act section 86: https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html |

1. Estimate annual employment income and applicable tax using [PIT](bangladesh-pit.md), including current aggregate salary relief, bands, rebate conditions and minimum tax. Do not reuse the old basic threshold or separate salary-component exemptions.
2. Section 86 requires deduction at payment at the average tax rate on estimated employment income. Keep the annual estimate, applicable base and pay-period calculation together; do not apply the highest marginal band to all salary (https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html).
3. Reforecast for bonus, benefit, joiner/leaver or corrected evidence. Section 86(4) permits an in-year increase/decrease for a deduction shortfall/excess. A statutory reduced/no-deduction certificate is a separate mechanism; do not simply stop withholding on an employee's assertion.
4. Record salary expense, employee withholding payable, net salary and any separate employee PF deduction. Use [payroll/social](bd-payroll-social.md) for mandatory PF/Progoti, WPPF and gratuity conditions; use [social contributions](bd-social-contributions.md) for voluntary individual choices. Do not infer that all employer benefits are voluntary.
5. Deposit deducted tax to the government and retain the challan/reference and employee allocation. Prepare the withholding return required by current law and reconcile payroll, bank payments, treasury deposits and certificates. Before submission load the applicable current withholding rules/return instructions for the exact deposit date, reporting frequency, portal and fields; the old approximate fortnight/monthly-return wording is not verified.
6. Give the reviewer the annual estimate, deduction history, in-year corrections, deposit evidence and unresolved reporting items. A payroll calculation is not proof that withholding was remitted or the required return was filed.

## Worked cases

### Ordinary employee annual estimate

Illustrative general-category resident annual salary 600,000 and no other relevant amounts. Under the PIT salary exclusion, employment income after exclusion is 400,000 and ordinary band tax is 0; an automatic positive deduction merely because gross pay exceeds the threshold would be wrong. No special income/minimum-tax regime is assumed. Figures are derived from the PIT provisions.

```oa-check
name: Annual salary after current aggregate relief
inputs:
  annual_salary: 600000
steps:
  - exclusion: min(annual_salary / 3, 500000)
  - ordinary_income: annual_salary - exclusion
  - band_tax: min(max(ordinary_income - 400000, 0), 300000) * 0.10
expected:
  exclusion: 200000
  ordinary_income: 400000
  band_tax: 0
```

### Edge: in-year under-deduction correction

A reviewed revised annual withholding estimate is 36,000; 20,000 has already been deducted and 4 equal remaining pay periods are assumed. Remaining deduction is 16,000, or 4,000 per period. The annual estimate is an input established from the employee's facts, not a tax rate invented here.

```oa-check
name: Salary withholding shortfall spread over remaining equal periods
inputs:
  annual_estimate: 36000
  already_deducted: 20000
  remaining_periods: 4
steps:
  - remaining: annual_estimate - already_deducted
  - per_period: remaining / remaining_periods
expected:
  remaining: 16000
  per_period: 4000
```

## When to refuse or refer

Refer foreign/non-resident employees, disputed employment status, unsupported relief, leaver/negative-adjustment treatment and unresolved filing/deposit rules. Never mark payroll tax paid without treasury evidence or assume drawings are wages.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for salary average-rate deduction, in-year adjustment and reduced/no-deduction certificate conditions, section 86 | https://bdlaws.minlaw.gov.bd/act-1429/section-51916.html | 2026-11-14 |
| Read for salary cap amendment, Sixth Schedule paragraph 27 | https://bdlaws.minlaw.gov.bd/act-1718/section-59129.html | 2026-11-14 |
| Read for ordinary individual bands and thresholds, Finance Act schedule 2 | https://bdlaws.minlaw.gov.bd/upload/act/2026-08-17-10-27-29-%E0%A6%A4%E0%A6%AB%E0%A6%B8%E0%A6%BF%E0%A6%B2_Act-No-96.pdf | 2026-11-14 |
| Read for investment rebate formula and qualifications section 78 | https://bdlaws.minlaw.gov.bd/act-1429/section-51908.html | 2026-11-14 |

Not yet confirmed: Current withholding-tax rules for deposit deadlines, reporting frequency, live e-TDS portal/form fields and employee-certificate process. Those must be resolved before a payroll filing is signed off; the old approximate two-week remittance and monthly-return assertion is not an instruction.
