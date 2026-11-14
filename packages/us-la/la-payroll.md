---
name: la-payroll
description: "Louisiana 2026 employer state withholding and unemployment insurance: L-4, 3.09% formula, registration, deposit frequencies, quarterly/annual returns, $7,000 UI wage base and assigned rates."
version: "0.1"
jurisdiction: US-LA
category: payroll
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: payroll
type: computation
---

# Louisiana payroll withholding and unemployment insurance, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Louisiana's 2026 wage-withholding formula uses 3.09% after the applicable payroll deduction. Contributing UI employers use the first $7,000 of each worker's 2026 wages and the assigned rate notice. New employers receive an industry-based rate; there is no one statewide new-employer rate to invent. [2026 formula](https://dam.ldr.la.gov/taxforms/R-1210-1-26.pdf); [2026 UI table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf); [LWC employer FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp).

## Scope

Ordinary employers paying wages for Louisiana services and Louisiana residents where state withholding applies, plus covered contributing employers under the separate state unemployment system. Multistate localization, employee/contractor status, farm/domestic coverage and governmental/nonprofit reimbursement require their own facts. Federal payroll taxes and figures belong to `us-form-941-940-payroll`.

## Ask the client first

1. Entity, first wages, work/residence locations, worker duties/classification and any acquired business or predecessor?
2. Current LDR withholding and LWC UI account notices, assigned payment frequency and 2026 UI rate/NAICS industry?
3. Each worker's completed Louisiana L-4, pay frequency, taxable wages, year-to-date wages and additional withholding election?
4. Multi-state, agricultural/domestic, nonprofit/public-employer facts and liability/reimbursement determinations?
5. Quarter payroll register, prior remittances, W-2 state fields, last wage date, amendments and agency account balances?

## The method, step by step

1. **Register separately.** Establish the LDR withholding account and obtain the agency's payment-frequency assignment. LWC says every Louisiana employing unit must submit a liability/nonliability application; retain its employer account and rate determination. Do not use a withholding account number to report UI. [LDR registration FAQ](https://revenue.louisiana.gov/tax-professionals/general-resources/withholding-faqs/); [LWC employer FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp).
2. **Determine state wages and L-4 deduction.** LDR applies withholding to resident/nonresident employees' Louisiana services, and to resident services elsewhere when another state's withholding does not apply as described in its instructions. Obtain Louisiana Form R-1300/L-4; do not substitute federal W-4 settings. Classify supplemental, exempt and multistate payments before using the ordinary wage formula. [LDR withholding scope](https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/); [R-1306 January 2026](https://dam.ldr.la.gov/taxforms/1306-1-26.pdf).
3. **Calculate ordinary wage withholding.** With S = state-taxable wages per pay period and N = periods/year, W = max(0, S - D/N) x0.0309, plus any documented additional withholding. If no payroll deduction is claimed, W=Sx0.0309. D is $12,875 for one deduction/single/MFS, or $25,750 for the qualifying two-deduction joint/HOH/surviving-spouse setting. Use the actual L-4 claim. Annual periods are 1, monthly12, semimonthly24, biweekly26, weekly52 and daily365. Round payroll cents consistently with the official examples. These **withholding deductions differ from the final income-return deductions** in `la-income-tax`. [R-1210 January 2026](https://dam.ldr.la.gov/taxforms/R-1210-1-26.pdf); [R-1306 formula and examples](https://dam.ldr.la.gov/taxforms/1306-1-26.pdf).
4. **Accumulate UI wages per employee.** Obtain the covered-employment determination and assigned rate. For an ordinary contributing employee, quarter taxable wages = min(current covered wages, max(0, 7000 - earlier-year taxable wages)). Compute employer UI with the assigned percentage, keeping total covered wages in the quarterly report even when the annual taxable cap is exhausted. Do not use the prior year's $7,700 cap for 2026. [LWC 2026 rate table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf); [quarterly wage-report FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp).
5. **Reconcile and file two systems.** Reconcile withholding to deposits, L-1 and annual W-2/L-3; reconcile UI covered wages, taxable wages, assigned rate and payment separately. Submit corrections to the affected period and retain both acceptance/payment records. Reporting all part-time/temporary employees is required where covered. [LDR corrections FAQ](https://revenue.louisiana.gov/tax-professionals/general-resources/withholding-faqs/); [LWC reporting FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp).

### Rates, bands and thresholds

| 2026 item | Amount or instruction | Authority |
| --- | --- | --- |
| Ordinary withholding percentage | 3.09% after payroll deduction | [2026 formula](https://dam.ldr.la.gov/taxforms/R-1210-1-26.pdf) |
| Payroll annual deduction | $12,875 one deduction; $25,750 qualifying two deductions | [2026 formula](https://dam.ldr.la.gov/taxforms/R-1210-1-26.pdf); [R-1306](https://dam.ldr.la.gov/taxforms/1306-1-26.pdf) |
| UI taxable wage base | $7,000 per employee per calendar year | [2026 rate table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf) |
| Experience-rated UI range | 0.09%-6.20%, use assigned notice | [2026 rate table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf) |
| New-employer UI rate | Industry/NAICS average assigned by LWC | [LWC FAQ rate determination](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp) |
| Withholding payment-frequency bands | Average monthly withholding below $500 quarterly; $500 to below $5,000 monthly; $5,000+ semimonthly, subject to assigned notice | [LDR withholding page](https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/) |

## Worked cases

### Official weekly withholding example

A worker is paid $700 weekly and properly claims one Louisiana payroll deduction. Annual deduction divided by 52 is $247.5962; the balance at 3.09% gives $13.98 withholding. Using the final income-return deduction would fail the published payroll example.

```oa-check
name: LA weekly payroll example 2026
inputs:
  wages: 700
steps:
  - withholding: round(max(0, wages - 12875 / 52) * 0.0309, 2)
expected:
  withholding: 13.98
```

### UI cap and biweekly withholding are separate calculations

A worker has $6,000 earlier-year UI-taxable wages, then earns $4,600 this biweekly pay period. The valid L-4 claims two deductions. Withholding is $111.54. Only $1,000 remains taxable for UI; an **assumed assigned rate of 1.0% for this example**, not the new-employer default, gives $10 employer UI. Later covered wages remain reportable but no additional taxable wages arise after the cap.

```oa-check
name: LA biweekly withholding and UI cap
inputs:
  wages: 4600
  prior_ui_taxable: 6000
  assumed_assigned_rate: 0.01
steps:
  - withholding: round(max(0, wages - 25750 / 26) * 0.0309, 2)
  - ui_taxable: min(wages, max(0, 7000 - prior_ui_taxable))
  - ui_tax: ui_taxable * assumed_assigned_rate
expected:
  withholding: 111.54
  ui_taxable: 1000
  ui_tax: 10
```

## When to refuse or refer

Stop rate calculation without L-4 or the UI determination/rate notice. Refer classification, localization, acquisition/successor rates, farm/domestic exclusions, reimbursable employers, unusual compensation and agency assessments. Never use the corporate/individual income rate as payroll withholding or a single guessed UI rate.

## Filing and payment

LDR requires electronic withholding returns/payments unless exempted. File L-1 for each assigned quarter, including zero-withholding periods. R.S.47:114 sets quarterly returns due the last day of the following month; payment frequency is separately assigned, so do not wait until quarter-end to deposit monthly/semimonthly liabilities. The annual L-3/W-2 reconciliation is due January 31, or within 30 days after final wages where applicable, through LDR's electronic channel. Amend each affected quarter, complete final reconciliation, then close the account. Confirm actual deposit dates in LaTAP before scheduling. [LDR withholding page](https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/); [R.S.47:114](https://www.legis.la.gov/legis/Law.aspx?d=101103); [LDR FAQ](https://revenue.louisiana.gov/tax-professionals/general-resources/withholding-faqs/).

LWC quarterly wage reports and contributions are due April 30, July 31, October 31 and January 31 following the relevant quarter; annual domestic filers have a separate January 31 schedule. Report electronically via LWC's employer wage-report channel. Its FAQ states payment received after 1pm Central is processed the next banking business day; allow time and retain confirmation. Obtain the assigned calendar's weekend/holiday adjustment rather than guessing a portal deadline. [LWC employer FAQ](https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp).

## Completion checklist

Save liability/accounts and L-4s, reconcile ordinary withholding to the official formula, track per-worker annual UI wages, use the assigned rate and deposit calendar, reconcile both returns to payments, and retain annual reconciliation and amendment evidence.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| R-1210 January 2026; read for p.1 complete formula, definitions and both worked examples. | https://dam.ldr.la.gov/taxforms/R-1210-1-26.pdf | 2026-11-13 |
| R-1306 January 2026; read for pp.1-2 employer formula, deduction/pay-frequency definitions and example calculations; wage-table ranges were not used as independent figures. | https://dam.ldr.la.gov/taxforms/1306-1-26.pdf | 2026-11-13 |
| LDR withholding page; read for employer scope, electronic filing, frequency bands, L-1/L-3 and closure sections. | https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ | 2026-11-13 |
| LDR withholding FAQ; read for registration, agency frequency assignment, amendments and closing account. | https://revenue.louisiana.gov/tax-professionals/general-resources/withholding-faqs/ | 2026-11-13 |
| R.S.47:114; read for quarterly/annual deadlines and neighbouring return/receipt requirements. | https://www.legis.la.gov/legis/Law.aspx?d=101103 | 2026-11-13 |
| LWC 2026 rate table; read for p.1 complete positive/negative reserve-ratio table and wage-base heading. | https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf | 2026-11-13 |
| LWC employer taxes FAQ; read for liability application, new-industry rates, quarterly wages/report deadlines and payment timing. | https://www.laworks.net/FAQs/FAQ_UI_EmployerTaxes.asp | 2026-11-13 |

Not yet confirmed: ordinary employer UI coverage thresholds/localization exceptions and account-specific assigned rate; precise monthly/semimonthly LDR deposit-day calendar, special/supplemental compensation, and final 2026 L-3 file specifications. LDR currently links an L-1 instruction revised January2027; it was read as a later revision but is not used to backdate 2026 instructions. Follow the actual assigned notice and confirm these gaps before submitting affected payroll.
