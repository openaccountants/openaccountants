---
name: tn-payroll
description: "Apply Tennessee 2026 payroll: no state income withholding but employer UI on $7,000 per employee. Covers ordinary 2.7% new-employer rate and industry exceptions, Table 6, registration, modern Employer e-Services wage reports, amendments and payment. Trigger on TN payroll or Tennessee unemployment premiums."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tn-payroll"
  jurisdiction: "US-TN"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Tennessee payroll and unemployment insurance, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Tennessee has no earned-income withholding, but covered employers pay unemployment premiums on each employee's first $7,000 of 2026 wages. Use the actual notice rate; the ordinary new-employer rate is 2.7% with NAICS industry exceptions.

## Scope and who this is for

Tennessee state withholding and employer unemployment insurance. `us-form-941-940-payroll` owns federal payroll, deposits and Forms 941/940. Other-state withholding, UI localization, worker status, workers compensation and new-hire reporting require separate analysis. Hall investment income tax was repealed from January 1,2021; it is not a payroll obligation.

## Ask the client first

1. Where does each worker physically work, where do they reside, and what interstate assignments exist?
2. What worker/owner status, employer coverage, NAICS sector and first employment dates apply?
3. What does the current premium notice show, including effective dates and new versus experience-rated status?
4. What are the quarterly and year-to-date covered wages for each employee, including predecessor payroll?
5. Does the employer already have a UI number and Employer e-Services logon, and are prior returns and payments reconciled?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| State earned-income withholding | None | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057595051-GEN-34-Income-Tax-Withholding) |
| 2026 UI employee annual base | $7,000 | [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html) |
| New employer ordinary rate | 2.7% for other industries; industry-sector exceptions require the actual rate notice | [official text](https://lwdsupport.tn.gov/hc/en-us/articles/202843724-How-is-my-premium-rate-determined) |
| New-employer experience transition | 36 consecutive months ending December 31; eligible experience rate begins the next July 1 | [official text](https://lwdsupport.tn.gov/hc/en-us/articles/202843724-How-is-my-premium-rate-determined) |
| 2026 premium schedule | Table 6 effective both January 1 and July 1; reserve ratio and notice determine actual rate | [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html) |

1. Confirm UI coverage and localization. Absence of Tennessee income tax is not an exemption from UI. Federal employment classification and Tennessee UI coverage are separate tests.
2. Use [Employer e-Services](https://jobs4tnui.tn.gov) from [the official modernization page](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/modernization-project.html). TNPAWS/TPU have been replaced for premium/wage reporting and payments. A new employer chooses **Register my business**, creates credentials and answers the required business questions. An existing employer chooses **Sign Up for an Online Account**, using FEIN and a Letter ID beginning L from the benefit system within the preceding 15 months; request a replacement letter if absent. Source: [official text](https://lwdsupport.tn.gov/hc/en-us/articles/41503856211475-Employer-Registration).
3. Obtain the notice rather than guessing an industry rate. New employers initially use sector reserve experience; the agency identifies the 2.7% rate for all other industries and specific manufacturing sectors 31/32/33. Experienced employers use the reserve-ratio system, with the trust-fund-selected table capable of changing semiannually. Both halves of 2026 use Table 6. Source: [official text](https://lwdsupport.tn.gov/hc/en-us/articles/202843724-How-is-my-premium-rate-determined), [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html).
4. Compute current taxable wages per employee = min (current covered wages, max (7,000 - previous 2026 covered wages,0)); add employees and multiply by the applicable notice rate. If the notice changes, apply the correct effective period. Report gross covered wages even after the base is used up. Source: [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html).
5. In e-Services **Summary**, choose **File a Wage Report**, or **View Wage Reports**, then **File Now**. Enter the wage table or upload an abbreviated ICESA/58-character file. Resolve rejection errors, inspect employee identifiers, names and wages, review the summary, digitally sign and submit. Save confirmation; complete the separate premium payment and reconcile the account. Source: [official text](https://lwdsupport.tn.gov/hc/en-us/articles/41492672876947-Filing-And-Amending-Wage-Reports).
6. Amend through **View Wage Reports**, select the quarter and **View or Amend Return**. Give the reason/explanation; wage decreases or removal of employees require documentation and staff approval. Retain confirmation and verify the adjusted balance. Source: [official text](https://lwdsupport.tn.gov/hc/en-us/articles/41492672876947-Filing-And-Amending-Wage-Reports).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| No Tennessee withholding | Still run federal payroll and Tennessee UI; consider withholding in the worker's other state. |
| NAICS exception/new notice differs from 2.7% | The notice controls; do not use a universal new-employer rate. |
| Worker has already exceeded $7,000 | No further UI taxable wages for that year, subject to predecessor/localization rules. |
| Wage decrease amendment | Await staff approval; submission alone does not update the report. |
| Business ceases operations | Close/inactivate the account properly and clear required reports; a missed return triggers delinquency notices. |

Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057595051-GEN-34-Income-Tax-Withholding), [official text](https://lwdsupport.tn.gov/hc/en-us/articles/202843724-How-is-my-premium-rate-determined), [official text](https://lwdsupport.tn.gov/hc/en-us/articles/41492672876947-Filing-And-Amending-Wage-Reports), [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/modernization-project.html).

## Worked cases

**Case 1.** A new employer whose notice confirms the ordinary 2.7% rate pays one employee $20,000 and another $5,000 in 2026 covered wages. Taxable wages are $7,000+$5,000=$12,000; UI is **$324**, an employer expense. State income withholding is zero.

```oa-check
name: TN2026 ordinary new employer UI
inputs:
  worker_a: 20000
  worker_b: 5000
  notice_rate: 0.027
steps:
- base: min(worker_a,7000) + min(worker_b,7000)
- ui: base * notice_rate
expected:
  base: 12000
  ui: 324
```

**Case 2, cap decision.** At a confirmed 2.7% rate, $3,000 current-quarter pay after $6,500 prior pay leaves $500 taxable and **$13.50** UI. With prior pay $2,000 instead, all $3,000 is taxable and **$81** UI. Preserve the full wage report in either branch.

```oa-check
name: TN cap decision both prior wage histories
inputs:
  current: 3000
  prior_high: 6500
  prior_low: 2000
steps:
- high_base: min(current,max(7000-prior_high,0))
- low_base: min(current,max(7000-prior_low,0))
- high_tax: high_base * 0.027
- low_tax: low_base * 0.027
expected:
  high_base: 500
  low_base: 3000
  high_tax: 13.5
  low_tax: 81
```


## When to refuse or refer

Refer NAICS disputes, missing rate notices, predecessor/successor and interstate localization, worker classification, public/nonprofit reimbursement and account appeals. Do not deduct an employer premium from employee net pay.

## Filing and payment

Quarterly wage reports are due at the end of the month after the quarter, including April 30, July 31, October 31 and January 31. The agency describes delinquency notices followed by pending assessment and a further cure period; do not wait for those notices to report. Source: [official text](https://lwdsupport.tn.gov/hc/en-us/articles/360001003928-What-is-delinquent-cycle). Confirm premium-payment due dates and weekend/holiday handling against the account notice; those were not independently established in the opened material. Use the modern e-Services payment function and retain the effective payment date and confirmation. Sources: [official text](https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/modernization-project.html), [official text](https://lwdsupport.tn.gov/hc/en-us/articles/41503856211475-Employer-Registration).

## Completion checklist

- Use Employer e-Services and the actual current premium notice.
- Reconcile gross/excess/taxable wages per employee.
- Retain wage-report submission and payment confirmations.
- Confirm any decreasing amendment has been approved.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR GEN 34. Read for no earned-income withholding and Hall repeal. | https://revenue.support.tn.gov/hc/en-us/articles/360057595051-GEN-34-Income-Tax-Withholding | 2026-11-13 |
| TDLWD 2026 rate page. Read for 2026$7,000 row, Table 6 for both half-years and rate mechanics. | https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/ui-tax-rates.html | 2026-11-13 |
| TDLWD premium determination. Read for new-employer sector treatment, ordinary 2.7% and 36 month transition; updatedFebruary 2026. | https://lwdsupport.tn.gov/hc/en-us/articles/202843724-How-is-my-premium-rate-determined | 2026-11-13 |
| TDLWD employer registration. Read for new/existing employer enrollment, FEIN/Letter ID and current e-Services routes. | https://lwdsupport.tn.gov/hc/en-us/articles/41503856211475-Employer-Registration | 2026-11-13 |
| TDLWD filing/amending wage reports. Read for manual/file input, summary, digital signature, confirmation and amendment approval. | https://lwdsupport.tn.gov/hc/en-us/articles/41492672876947-Filing-And-Amending-Wage-Reports | 2026-11-13 |
| TDLWD modernization. Read for replacement of TNPAWS/TPU, payments and account access. | https://www.tn.gov/workforce/employers/tax-and-insurance-redirect/unemployment-insurance-tax/modernization-project.html | 2026-11-13 |
| TDLWD delinquent cycle. Read for end-of-next-month report due date and assessment sequence. | https://lwdsupport.tn.gov/hc/en-us/articles/360001003928-What-is-delinquent-cycle | 2026-11-13 |

Not yet confirmed: 2026 numeric industry-exception rates and the full Table 6 rate chart could not be read. Actual employer notice required. Premium-payment deadlines, weekend/holiday handling, late premium monetary penalties/interest, and domestic/farm/public/nonprofit coverage thresholds are not confirmed here.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tn-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tn-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
