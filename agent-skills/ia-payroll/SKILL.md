---
name: ia-payroll
description: "Compute and administer Iowa wage withholding and employer unemployment insurance in 2026. Covers IA W-4 inputs, the 2026 withholding formula, new/employer UI rates and USD 20,400 wage base, separate registration, quarterly reports, wage statements and payment schedules. Trigger on Iowa payroll, withholding, MyIowaUI or unemployment tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ia-payroll"
  jurisdiction: "US-IA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Iowa employer withholding and unemployment insurance, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers; a qualified professional must review the facts, computations and filings. Circular 230 section 10.37: apply the law to established facts, consider relevant circumstances and do not rely on audit risk or assume facts that have not been supplied.

**Answer first.** Iowa wage withholding uses the official 2026 formula and the employee's IA W-4, not a flat percentage of gross wages. Employer UI is separate: the 2026 taxable wage base is USD 20,400 per employee, new non-construction employers pay 1%, and new construction employers pay 5.4%. Experienced employers use their assigned rate. [IDR formula](https://revenue.iowa.gov/media/53/download?inline=); [IWD 2026 UI rates](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes).

## Scope

Iowa employers with wages subject to state withholding and/or Iowa UI. Withholding is employee income tax held by the employer; UI is an employer contribution. Federal payroll, FICA, FUTA and Form 941/940 figures belong to `us-form-941-940-payroll`. Owner self-employment tax belongs to `us-schedule-c-and-se-computation`.

## Ask the client first

1. Legal entity, FEIN, first Iowa payroll date, acquisition/successor status and existing state account numbers.
2. Employee residence and actual work locations; military, nonresident or reciprocity claims.
3. IA W-4 year, marital category, spouse's earned income, allowance **amount**, additional withholding and valid exemption.
4. Pay frequency, taxable wages and benefits, year-to-date UI wages by employee.
5. Construction classification, annual UI rate notice and prior account experience.
6. Assigned withholding payment frequency, prior payments/returns, wage statements and account balances.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, 2026 | Official source |
| --- | --- | --- |
| Withholding calculation rate, after payroll deduction | 3.8% | [2026 formula steps 1-4](https://revenue.iowa.gov/media/53/download?inline=) |
| Payroll deduction D, annual pay period: other or joint with earning spouse; HOH; joint with no earning spouse/qualifying surviving spouse | USD 13,000; USD 19,500; USD 26,000, for 2024-or-later IA W-4; use actual pay-period table, not federal deduction | [2026 formula pp. 1-2](https://revenue.iowa.gov/media/53/download?inline=) |
| Legacy IA W-4, 2023 or earlier | Convert allowance count to annual credit amount at USD 40 per allowance; use the legacy marital-status deduction table | [2026 formula steps 1B and 3B](https://revenue.iowa.gov/media/53/download?inline=) |
| UI taxable wage base | First USD 20,400 wages per employee in calendar 2026 | [IWD handbook, wage base](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes) |
| New non-construction UI employer | 1.000% | [IWD 2026 new-employer rules](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes) |
| New construction UI employer | 5.400% | [IWD 2026 new-employer rules](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes) |
| Experienced private UI employers, Table D ranks 1-9 | 0%, 0.1%, 0.2%, 0.3%, 0.5%, 0.9%, 2.0%, 2.8%, 5.4%; use notice-assigned rank/rate | [IWD Table D](https://workforce.iowa.gov/employers/unemployment-insurance/ui-tax-and-audit/unemployment-insurance-taxes) |
| Withholding quarterly payer | Less than USD 6,000 annual withholding | [IDR payment frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |
| Withholding monthly payer | USD 6,000 through USD 120,000 annual withholding | [IDR payment frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |
| Withholding semimonthly payer | More than USD 120,000 annual withholding | [IDR payment frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |

### Registration, withholding and UI computation

1. Obtain the FEIN, then register an Iowa withholding account through the IDR registration route to GovConnectIowa. Separately register UI at MyIowaUI within 30 days after first Iowa wages or acquisition; out-of-state employers register as soon as Iowa wages are paid. IWD determines liability, including successor, agricultural, domestic, nonprofit and reimbursable-employer rules. Ordinary covered wages are not exempt merely because payroll is small. [IDR](https://revenue.iowa.gov/taxes/tax-guidance/withholding-tax/iowa-withholding-tax-information); [IWD employing units](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/employing-units); [coverage conditions](https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/employers-covered-under-law).
2. Obtain IA W-4 and new-hire information within the required reporting period; missing IA W-4 means zero allowance amount. Determine residence/work sourcing and valid exemption separately, rather than treating a federal exemption as conclusive Iowa exemption.
3. For 2024-or-later IA W-4, follow the four 2026 formula steps: T1 = taxable wages G minus the appropriate pay-period deduction D; T2 = T1 x 0.038; T3 = T2 minus annual allowance amount W divided by pay periods P; T4 adds requested additional withholding A. Apply the formula's low-wage/rounding instructions and table for the precise payroll period. D is a **withholding** allowance for computation and must not be imported as the annual-return deduction. For pre-2024 forms use steps 1B and 3B instead of treating the old allowance count as dollars.
4. Compute UI taxable wages employee by employee as the smaller of current covered wages and the unused annual base, not below zero. Multiply by the notice-assigned contribution rate. A new employer uses the applicable new-construction/non-construction rate, not the experienced-employer rank-4 rate of 0.3%. Do not deduct employer UI from employee net pay.
5. File UI wage detail and contribution reports in MyIowaUI, including zero-employment quarters while the account is active. Report total wages and taxable wages separately. Reconcile payroll totals, employee IDs, UI base rollforwards and payment confirmations; store authorized-agent access separately from employer credentials.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Illinois resident or multistate worker | Confirm reciprocal exemption and proper certificates; other nonresident sourcing needs review |
| Military/spouse or withholding exemption | Obtain facts and the valid state certificate; no automatic conclusion from residency alone |
| Nonprofit/government/agriculture/domestic | Distinct UI coverage or reimbursement rules; standard new-private-employer rate is not assumed |
| Acquired business or mixed construction activities | Experience/NAICS classification can change assigned rate; obtain agency determination |
| Employee exceeds annual UI base | Continue reporting gross covered wages, but cap additional taxable wages |

## Worked cases

**Case 1.** An invented employee with a current IA W-4 marked Other has a single annual regular payroll of USD 60,000, allowance amount USD 40 and no additional withholding. Using the annual D of USD 13,000, withholding before any software-specific rounding is (60,000 - 13,000) x 3.8% - 40 = USD 1,746. A new non-construction employer's UI is USD 20,400 x 1% = USD 204; employee withholding and employer UI are separate liabilities.

```oa-check
name: Iowa annual payroll withholding and new-employer UI
inputs:
  annual_taxable_wages: 60000
  withholding_deduction: 13000
  annual_allowance_amount: 40
steps:
  - withholding: max((annual_taxable_wages - withholding_deduction) * 0.038 - annual_allowance_amount, 0)
  - ui_taxable: min(annual_taxable_wages, 20400)
  - employer_ui: ui_taxable * 0.01
expected:
  withholding: 1746
  ui_taxable: 20400
  employer_ui: 204
```

**Case 2, boundary decision.** An invented new construction employer pays USD 8,000 this quarter to an employee with USD 18,000 of prior-year-to-date covered wages. The unused base is USD 2,400, so taxable wages are USD 2,400 and UI is USD 129.60. Applying 5.4% to all USD 8,000 would charge USD 432, overstating liability by USD 302.40. Obtain the year-to-date ledger before deciding to tax the entire payment.

```oa-check
name: Iowa construction UI base-exhaustion decision
inputs:
  quarter_wages: 8000
  prior_ytd_wages: 18000
  base: 20400
steps:
  - remaining: max(base - prior_ytd_wages, 0)
  - taxable: min(quarter_wages, remaining)
  - correct_ui: taxable * 0.054
  - uncapped_ui: quarter_wages * 0.054
  - overstatement: uncapped_ui - correct_ui
expected:
  remaining: 2400
  taxable: 2400
  correct_ui: 129.60
  uncapped_ui: 432
  overstatement: 302.40
```

## When to refuse or refer

Refer worker classification, interstate UI localization, successor experience, reimbursable status, agriculture/domestic special coverage, contested rate notices and unusual supplemental/retirement payments. Do not reuse federal payroll amounts or another state's wage base.

## Filing and payment

Withholding quarterly returns are due the last day of the following month. Quarterly payers pay with that return. Monthly payers make payments for the first two months by the 15th of the next month and settle the third month with the quarterly return. Semimonthly payers pay days 1-15 by the 25th of that month and days 16-end by the 10th of the next month, then file the quarterly reconciliation by its normal due date. State wage statements containing Iowa withholding are electronically due February 15; apply applicable next-business-day rules. [IDR frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates).

UI contributions and payroll reports are due the last day of the month following the quarter, moved to the next business day for weekends/holidays under [871-23.8](https://www.legis.iowa.gov/docs/iac/chapter/02-04-2026.871.23.pdf). Thus nominal April 30, July 31, October 31 and January 31 must be checked against the year calendar. File in MyIowaUI, retain acceptance and separately confirm payment posted to the correct quarter.

IDR withholding penalties follow [421.27](https://www.legis.iowa.gov/docs/code/2026/421.27.pdf), with separate late-file/pay rules and applicable interest. IWD has its own UI delinquency penalties and interest; obtain the UI statement and applicable current law before calculating those amounts. An IDR income-tax interest notice does not establish UI interest.

## Completion checklist

- Both state registrations and liability determinations retained.
- IA W-4 version, pay period, category and allowance amount used correctly.
- UI notice and annual-base rollforward checked employee by employee.
- Quarterly returns, intermediate deposits and wage statements reconciled.
- Electronic acceptance and payment posting saved for each agency/account.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IDR withholding information. Read for employer duty, registration, IA W-4, zero-allowance default, exemption and new-hire procedures. | https://revenue.iowa.gov/taxes/tax-guidance/withholding-tax/iowa-withholding-tax-information | 2026-11-13 |
| IDR 2026 withholding formula. Read for 2026 payroll deductions by period and IA W-4 category, 3.8% rate and four-step formula; read pp. 1-3. | https://revenue.iowa.gov/media/53/download?inline= | 2026-11-13 |
| IDR filing frequencies. Read for quarterly/monthly/semimonthly payment thresholds, deposit dates and February 15 wage-statement filing. | https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates | 2026-11-13 |
| IWD UI tax tables. Read for 2026 Table D experienced rates and distinction from new-employer minimum. | https://workforce.iowa.gov/employers/unemployment-insurance/ui-tax-and-audit/unemployment-insurance-taxes | 2026-11-13 |
| IWD UI employer handbook tax section. Read for 2026 USD 20,400 base, new employer rates and annual notice. | https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/unemployment-insurance-taxes | 2026-11-13 |
| IWD employing units. Read for separate UI registration, report/pay workflow and zero quarters. | https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/employing-units | 2026-11-13 |
| IWD employers covered under law. Read for ordinary, agricultural, domestic, nonprofit and successor liability boundaries. | https://workforce.iowa.gov/employers/unemployment-insurance/unemployment-insurance-employer-handbook/employers-covered-under-law | 2026-11-13 |
| Iowa Administrative Code 871 chapter 23. Read for rule 23.8 quarterly return/payment dates and next-business-day rule. | https://www.legis.iowa.gov/docs/iac/chapter/02-04-2026.871.23.pdf | 2026-11-13 |
| Iowa Code 421.27. Read for IDR withholding late filing/payment rules. | https://www.legis.iowa.gov/docs/code/2026/421.27.pdf | 2026-11-13 |

Not yet confirmed: full 2026 UI penalty/interest schedule, reimbursable-employer computation, multistate localization and successor-rate determinations; detailed withholding formula rounding/low-wage handling and special supplemental-pay cases must be read in the complete official formula before software implementation. The worked annual withholding case has exact whole-dollar arithmetic and does not depend on that unconfirmed rounding rule.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
