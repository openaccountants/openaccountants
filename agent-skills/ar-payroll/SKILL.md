---
name: ar-payroll
description: "Arkansas 2026 employer payroll: state wage withholding, AR4EC, registration, deposits, annual reconciliation and state unemployment insurance wage base, rates and quarterly reports."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-payroll"
  jurisdiction: "US-AR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Arkansas payroll withholding and unemployment insurance, 2026

> **Built from the law. Not yet approved.** Written by Codex; no accountant has reviewed this version. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Compute wage withholding with DFA's current 2026 formula, whose top marginal rate is 3.7%. A contributing new employer's UI rate is 2.0% on the first $7,000 per worker in 2026. Keep the withholding and UI accounts separate. [DFA formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf); [Division's dated 2026 rates](https://reemployment.arkansas.gov/calculating-taxable-wages/). Federal payroll amounts have their home in `us-form-941-940-payroll`; they are not restated here.

## Scope

Arkansas employees, ordinary wage-withholding employers and contributing unemployment-insurance employers. Withholding depends on work in Arkansas; UI uses its separate localization and coverage rules. Governmental/nonprofit reimbursable employers, farm/domestic exceptions, acquired businesses and multistate payroll need the boundary review below.

## Ask the client first

1. Each worker's employee/contractor status, actual work state, residence, and any qualifying military-spouse or Texarkana certificate?
2. Pay frequency, Arkansas taxable wages, AR4EC exemptions and additional withholding?
3. Withholding account ID, DFA-assigned monthly/annual filing status, and prior monthly average withholding?
4. UI account number, assigned 2026 rate notice, new/successor status and any special assessments?
5. Per-worker calendar-year wages before this pay period, including predecessor wages where applicable?
6. Industry, legal entity and nonprofit/governmental, domestic, agricultural or multistate circumstances?

## The method, step by step

### Rates, bands and thresholds

| Item and condition | 2026 value | Official source |
| --- | --- | --- |
| Ordinary formula standard deduction, before annual tax | $2,470 | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| AR4EC annual credit per claimed withholding exemption | $29 | [DFA formula p.3](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| Net annual taxable income $0-$5,599 | 0% | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $5,600-$11,199 | 2% minus $111.98 | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $11,200-$15,999 | 3% minus $223.97 | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $16,000-$26,399 | 3.4% minus $287.97 | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $26,400-$94,700 | 3.7% minus $367.16 | [DFA formula p.2](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $94,701-$97,600 transition | 3.7%, adjustment starts at $369.90 and drops $10 per $100 band (derived: difference between consecutive bands on the table), ending $89.90 | [DFA formula pp.2-3](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| $97,601 and over | 3.7% minus $79.90 | [DFA formula p.3](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| UI calendar-year wage base, per employee | $7,000 | [Division 2026 notice](https://reemployment.arkansas.gov/calculating-taxable-wages/) |
| New contributing employer total UI rate | 2.0%: 1.8% base plus 0.2% administrative assessment | [Division 2026 notice](https://reemployment.arkansas.gov/calculating-taxable-wages/) |
| Experienced UI rates, including deficit rates | 0.2%-10.1%; use assigned notice | [Division 2026 notice](https://reemployment.arkansas.gov/calculating-taxable-wages/) |
| Annual withholding filer eligibility, only after DFA notice | Under $1,000 annual withholding | [DFA instructions p.7](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf) |
| Mandatory electronic withholding filing | Average $20,000 or more per month | [DFA instructions p.7](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf) |

1. **Register the withholding wage account.** In [ATAP](https://atap.arkansas.gov), select business registration and the withholding-wage tax account; AR-1R is DFA's combined paper registration alternative. Record the assigned account ID. Obtain a signed AR4EC or AR4ECSP. Use no exemptions if no certificate is supplied; retain the certificate. [DFA instructions pp.2, 6-7](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf).
2. **Register UI separately.** Ordinary coverage begins with one or more workers for some portion of ten or more days in a calendar year. Acquisition of a covered business, domestic cash wages of $1,000 in a quarter and agricultural cash wages of $20,000 in a quarter or ten workers in twenty weeks are separate coverage routes; special exclusions still apply. [Handbook pp.7-8](https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf). Follow the Tax21 employer-account link on the [official employer page](https://reemployment.arkansas.gov/employer-services/). Supply the DWS-ARK-201 liability details; the handbook requires submission no later than the last day of the second month in which the unit meets the employer definition. Keep the liability determination and assigned account number. [Handbook pp.7-9](https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf).
3. **Annualize taxable period wages.** Multiply by pay periods: monthly 12, semimonthly 24, biweekly 26, weekly 52 or daily 260. Subtract $2,470. Below $100,001 use the $50 midpoint of the $100 range; at $100,001 or more use exact income. Apply the matching formula row above, round annual gross tax to dollars, subtract $29 per AR4EC exemption, then divide by pay periods. Do not allow negative withholding. Check a low-income certificate/table before using the ordinary formula for an employee eligible for that alternative. [Formula pp.2-4](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf).
4. **Compute UI per worker.** Taxable wages this quarter = the lesser of covered quarter wages and the remaining $7,000 annual base, never negative. Multiply by the assigned total contribution rate. Report all covered wages, including excess wages, on the quarterly wage detail. Do not add the 0.2% assessment again to the published 2.0% new-employer total. The older handbook's new-employer base language is superseded by the Division's dated 2026 notice. [2026 notice](https://reemployment.arkansas.gov/calculating-taxable-wages/); [handbook p.21](https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf).
5. **File and pay withholding.** Select the correct withholding account and reporting period in ATAP, enter tax withheld and reconcile it to payroll. New registrations are monthly: AR941M and payment by the 15th of the next month, including a zero voucher. Only move to AR941A annual filing after DFA notice; that return/payment is due January 31 after year end. Retain the submission and payment confirmations. [Instructions pp.2, 7](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf).
6. **File and pay UI.** In Tax21 select quarterly contribution/wage report, enter employee identifying details and total/excess/taxable wages, verify the assigned rate, submit and pay the balance. Save the report, confirmation and debit record. Ordinary quarterly report/payment due dates are April 30, July 31, October 31 and January 31 following Q4, including no-wage reports while liable. Use DWS-ARK-223 to correct prior wage reports rather than mixing old wages into the current quarter. [Handbook pp.20-21](https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf); [wage-report specifications](https://reemployment.arkansas.gov/employer-services/wage-report-specifications/).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Texarkana residence, military spouse or exempt wages | Verify actual eligibility and certificate; do not treat all Arkansas wages as exempt. See `ar-income-tax` and DFA instructions pp.4-5. |
| Acquired business, ownership transfer, PEO or shared control | UI experience/successor rules may override a new-employer rate or restart assumption; refer with acquisition documents. |
| Nonprofit or government reimbursable UI account | Contributing-rate examples do not apply; handbook pp.18-19 has reimbursement/advance rules. |
| Multi-state worker | UI localization differs from income-tax residence. Review handbook p.13 and actual work/base/direction before assigning Arkansas wages. |
| Low-income or supplemental wage calculation | Use the current applicable DFA table/certificate, not an old 3.9% flat-rate instruction. |

## Worked cases

**Case 1: monthly ordinary withholding.** An invented employee earns $2,127 monthly and claims two AR4EC exemptions. Annual gross $25,524 less $2,470 = $23,054, midpoint $23,050. Annual gross tax $23,050 x 3.4% - $287.97 = $495.73, rounded $496. Subtract $58 credits and divide $438 by 12: $36.50 per month. This deliberately reproduces DFA's published formula example.

```oa-check
name: AR ordinary monthly withholding 2026
inputs:
  period_pay: 2127
  periods: 12
  exemptions: 2
steps:
  - annual_net: period_pay * periods - 2470
  - midpoint: floor(annual_net / 100) * 100 + 50
  - annual_gross_tax: round(midpoint * 0.034 - 287.97)
  - period_tax: max(annual_gross_tax - exemptions * 29, 0) / periods
expected:
  annual_net: 23054
  midpoint: 23050
  annual_gross_tax: 496
  period_tax: 36.50
```

**Case 2: choose the correct remaining UI base.** A new contributing employer has already paid a worker $6,000 in 2026 and now pays $3,000. Only $1,000 remains taxable. UI is $20, compared with $60 if the cap were wrongly ignored. The whole $3,000 still appears in total wages.

```oa-check
name: AR UI decision annual cap reached
inputs:
  previous_wages: 6000
  quarter_wages: 3000
steps:
  - taxable: min(quarter_wages, max(7000 - previous_wages, 0))
  - ui: taxable * 0.02
  - incorrect_uncapped: quarter_wages * 0.02
  - overstatement: incorrect_uncapped - ui
expected:
  taxable: 1000
  ui: 20
  incorrect_uncapped: 60
  overstatement: 40
```

## When to refuse or refer

Refer classification disputes, tax-rate protests, successorship, reimbursable accounts and uncertain multistate localization. Do not use the dated employer-instructions booklet's 3.9% wage-rate statement: the current formula and Act 2 supersede it. Do not estimate an experienced employer's assigned rate from the range.

## Filing and payment

Reconcile monthly withholding to W-2 statements. Furnish/file W-2 and ARW3 by January 31; monthly filers submit AR3MAR annual reconciliation by February 28, separately from December's voucher. Weekend/holiday withholding deadlines move to the next business day. [DFA instructions pp.1-3, 8-9](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf).

Withholding nonpayment penalty in the instructions is 5% per month, capped at 35%, plus 10% annual interest. UI delinquent contributions carry 1.5% monthly interest. A late contributing wage report costs the greater of $10 or 5% within 20 days, then the greater of $20 or 10%; estimated/incomplete reports can attract the greater of $30 or 15%. [DFA instructions pp.7-8](https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf); [UI handbook pp.20-21](https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf).

## Completion checklist

- Both account IDs and the assigned UI notice retained.
- Wages, AR4EC, midpoint and annual credit reconciled.
- Per-worker annual UI base tracked; no duplicate assessment.
- Zero reports, annual reconciliation and payment confirmations retained.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DFA 2026 withholding formula. Read for all four pages, effective date, rate rows, midpoint, credits and example. | https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf | 2026-11-13 |
| DFA 2026 employer instructions. Read for pp.1-9 registration, wage scope, exemptions, monthly/annual statuses, filing, year-end and penalties; 3.9% rate text superseded by current formula. | https://www.dfa.arkansas.gov/wp-content/uploads/withholdInstructions_2026.pdf | 2026-11-13 |
| Division of Reemployment, Calculating Taxable Wages, October 6 2026. Read for complete 2026 rate notice, wage base and administrative assessment. | https://reemployment.arkansas.gov/calculating-taxable-wages/ | 2026-11-13 |
| Division employer services. Read for 2026 rate table, deficit tiers and Tax21 entry point. | https://reemployment.arkansas.gov/employer-services/ | 2026-11-13 |
| Division employer handbook. Read for pp.7-9 employer coverage/registration, p.13 localization, pp.18-21 reimbursable boundaries, wage reports, deadlines and penalties; old rate language not used. | https://reemployment.arkansas.gov/wp-content/uploads/2026/08/Employer_Handbook_20220811.pdf | 2026-11-13 |

| Division wage-report specifications. Read for Tax21 filing/payment and DWS-ARK-223 correction instructions. | https://reemployment.arkansas.gov/employer-services/wage-report-specifications/ | 2026-11-13 |

Not yet confirmed: final 2026 low-income withholding tables and supplemental-wage flat-rate update; employer-specific assigned rate/assessments; whether any triggered assessment applies beyond the published total in a particular notice. These gaps require the applicable certificate/table or notice before using those branches.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
