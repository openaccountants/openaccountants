---
name: ct-corporate-tax
description: "Use for Connecticut corporate income/capital base tax, CT-1120, surtax, estimated payments and state modifications."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ct-corporate-tax"
  jurisdiction: "US-CT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Connecticut corporation business tax

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal computations belong to linked federal owner skills.

**Answer first.** An ordinary taxable corporation compares 7.5% tax on Connecticut net income with capital-base tax at **0.16% for income year 2026**, subject to the $250 minimum. A qualifying large or combined filer adds the 10% surtax; credits and payments follow. The live DRS overview still illustrates the **2025 0.21%** capital rate, so use the year-specific statute, not that stale illustration. [Section 12-219(a)](https://www.cga.ct.gov/current/pub/chap_208.htm); [DRS corporate information](https://portal.ct.gov/drs/corporation-tax/tax-information).

## Scope

Ordinary Connecticut corporation business tax, Form CT-1120, including wage-business corporations. A combined unitary group uses CT-1120CU and specialist allocation work. `us-form-1120-c-corp` owns federal taxable income, federal deductions/rates and federal payroll-tax effects; `ct-income-tax` owns individual/sole-proprietor tax and the retained optional pass-through credit discussion. `ct-sales-tax` and `ct-payroll` own their respective state jobs. This skill does not treat every LLC as a corporation.

## Ask the client first

1. Federal classification, year end, group membership, CT registration, operations/property/payroll and economic-nexus facts.
2. Federal Form 1120 income before NOL/special deductions, state additions/subtractions and depreciation history.
3. Connecticut apportionment receipts/factors, capital balances, exclusions and prior NOL vintages.
4. Federal total-income line 11, combined filing status, approved credits and carryforwards.
5. Prior/current tax, estimates/payments, extension, notices and filing software access.

## The method, step by step

1. **Establish the taxable filer and nexus.** A corporation carrying on business or having the right to carry on business in Connecticut generally registers and files. The DRS overview distinguishes in-state activity, the right to carry on business and economic presence. Federal protections and unitary-combination issues require the actual activity facts; do not infer exemption merely from no office or no profits. [DRS filing/nexus instructions](https://portal.ct.gov/drs/corporation-tax/tax-information).
2. **Bridge federal income to Connecticut income.** The final 2025 instructions for the **2025-2026 filing cycle** begin with federal Form 1120 line 28, before NOL and special deductions. State additions include deductible income taxes, specified other-state bond interest, related-party interest/intangible expenses (subject to statutory exceptions), 100% of section 168(k) depreciation and 80% of section 179 deductions; prescribed prior-year addbacks are recovered 25% in each of four succeeding years. State subtractions and capital-gain/loss adjustments require the schedules. Do not reuse federal taxable income after deductions as the state base. [2025 CT-1120 instructions, Schedules D/E/I/J](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120-instructions_1225.pdf); [DRS net-income calculation](https://portal.ct.gov/drs/corporation-tax/tax-information).
3. **Apply 2026 conformity changes before completing the bridge.** DRS's actual 2026 developments decouple from IRC section 168(n) and delay section 174A domestic research deductions by one year, with specified pre-2026 and retroactive-election adjustments. Do not assume the federal 2025 legislation automatically flows through. The complete project-by-project transition calculation and relief eligibility are **Not yet confirmed** here; retain research expenditure vintages and refer those cases. [2026 corporation business tax developments](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2026-developments).
4. **Apportion and use Connecticut NOLs.** Compute the Connecticut receipts/apportionment schedules appropriate to the industry/group before the NOL deduction. An NOL may offset no more than 50% of pre-NOL income. Losses from income years 2000-2024 carry forward twenty successive years; losses for years beginning on/after January 1, 2025 carry forward thirty. Ordinary income apportionment uses the statutory sales-factor rules, but special industries and combined groups require their own schedules, not one copied percentage. [DRS apportionment and NOL sections](https://portal.ct.gov/drs/corporation-tax/tax-information).
5. **Compare net-income and capital-base tax**, then apply surtax and credit limitations below. Maintain a separate capital-base workpaper: average capital, surplus/reserves, qualifying stock deductions and applicable apportionment. It is not simply ending-year cash or net income. Certain financial service companies, RICs and REITs have special capital-base treatment. [Schedules A-C](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120-instructions_1225.pdf); [Section 12-219](https://www.cga.ct.gov/current/pub/chap_208.htm).
6. **File and pay electronically.** CT-1120/CT-1120CU is generally due on the fifteenth day of the month after the federal return due date: May 15 for a calendar-year filer, normally the fifth month after year end; June 30 year ends use October 15. A 2026 calendar-year return therefore ordinarily falls due May 15, 2027, shifted to the next business day when necessary. File CT-1120 EXT for a filing extension, which does not extend payment. All corporate returns must be electronic; myconneCT does not support filing CT-1120CU but accepts its payments. Retain the e-file acceptance and payment confirmation. [DRS filing/due-date instructions](https://portal.ct.gov/drs/corporation-tax/tax-information).

### Rates, bands and thresholds

| Component | 2026 rate/amount and operation | Official source |
|---|---|---|
| Net-income tax | 7.5% of Connecticut taxable net income | [corp](https://portal.ct.gov/drs/corporation-tax/tax-information) |
| Capital-base tax | 1.6 mills = 0.16% (derived: 1.6 mills per dollar); statutory 2027 rate 1.1 mills and 2028 onward zero | [corplaw](https://www.cga.ct.gov/current/pub/chap_208.htm) |
| Minimum / capital ceiling | $250 minimum; capital-base tax at most $1 million before surtax | [corplaw](https://www.cga.ct.gov/current/pub/chap_208.htm) |
| Surtax | 10% for federal Form 1120 line 11 total income at least $100 million, or combined unitary filers; not imposed on the $250 minimum | [corp](https://portal.ct.gov/drs/corporation-tax/tax-information) |
| Surtax period | Applies for income year 2026; official sources differ on the future terminal year, as recorded below | [corp](https://portal.ct.gov/drs/corporation-tax/tax-information), [2026 supplement](https://www.cga.ct.gov/2026/sup/chap_208.htm) |
| Ordinary credit limit | Generally 50.01% of tax; credit-specific exceptions apply and credits cannot defeat the $250 minimum | [corp](https://portal.ct.gov/drs/corporation-tax/tax-information), [corpi](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120-instructions_1225.pdf) |
| Estimates | Required where current-year tax exceeds $1,000 | [corpes](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120es_0126.pdf) |

**Estimated payments.** Actual 2026 CT-1120ES uses cumulative targets: the smaller of prior-year tax **before credits** times 30%, 70%, 80%, 100%, or current-year tax **after credits** times 27%, 63%, 72%, 90%, less previous installments. Check short-year, initial-year and annualized exceptions rather than assuming every corporation qualifies for the prior-year method. Calendar-year 2026 ordinary installments fall March 16 (March 15 is Sunday), June 15, September 15 and December 15, 2026. This is not four equal 25% payments. Mandatory electronic payments apply unless DRS grants waiver Form DRS-EWVR. [2026 CT-1120ES, all four pages](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120es_0126.pdf).

**Penalties, amendments and records.** Current DRS instructions state late/unpaid tax interest at 1% per month or fraction, and a late-payment penalty of 10% of unpaid tax or $50, whichever is greater. An extension filer meeting the 90%-paid-by-original-date and balance-by-extended-date conditions may avoid the payment penalty, while interest remains. A no-tax late return can still attract $50. CT-1120X corrects the corporate return; DRS generally allows three years from the original due date or extended due date if an extension was granted. Special fraud, listed-transaction and federal-adjustment cases need the specific rule. [DRS penalties and amended returns](https://portal.ct.gov/drs/corporation-tax/tax-information).

## Worked cases

**Case 1, income base wins.** An ordinary standalone corporation has $100,000 Connecticut taxable net income after adjustments/apportionment, a $500,000 computed apportioned capital base, federal total income below $100 million, no credits and $7,000 paid. Income tax is $7,500; capital tax is $800; the larger is $7,500, so $500 remains. No surtax applies on these facts.

```oa-check
name: CT corporate income comparison
inputs:
  net_income: 100000
  capital_base: 500000
  payments: 7000
steps:
  - income_tax: net_income * .075
  - capital_tax: min(capital_base * .0016, 1000000)
  - base_tax: max(income_tax, capital_tax, 250)
  - balance: base_tax - payments
expected:
  income_tax: 7500
  capital_tax: 800
  base_tax: 7500
  balance: 500
```

**Case 2, capital base and minimum.** With $1,000 net income and $300,000 capital base, income tax is $75 and capital tax $480; tax before any surtax/credits is $480. A non-surtax corporation with neither positive base still owes $250. Assume no special financial-company treatment.

```oa-check
name: CT corporate capital and minimum
inputs:
  net_income: 1000
  capital_base: 300000
steps:
  - income_tax: net_income * .075
  - capital_tax: capital_base * .0016
  - tax: max(income_tax, capital_tax, 250)
  - zero_base_minimum: max(0, 250)
expected:
  income_tax: 75
  capital_tax: 480
  tax: 480
  zero_base_minimum: 250
```

**Case 3, unequal estimates.** A qualifying prior-year filer has $20,000 prior-year tax before credits and $10,000 current-year tax after credits. The smaller cumulative targets are $2,700, $6,300, $7,200 and $9,000; installment amounts are $2,700, $3,600, $900 and $1,800 if prior installments are paid as required. The remaining annual balance is handled with the return.

```oa-check
name: CT corporate cumulative estimates
inputs:
  prior: 20000
  current: 10000
steps:
  - first: min(prior * .3, current * .27)
  - second: min(prior * .7, current * .63) - first
  - third: min(prior * .8, current * .72) - first - second
  - fourth: min(prior, current * .9) - first - second - third
expected:
  first: 2700
  second: 3600
  third: 900
  fourth: 1800
```

## When to refuse or refer

Refer economic-nexus protections, unitary membership, special-industry apportionment, related-party exceptions, research-expenditure transition, credit monetization and contested tax positions. Do not turn this ordinary standalone workflow into a combined return without the requisite schedules.

## Sources

| Source | Read scope | Read date |
|---|---|---|
| [DRS Corporation Business Tax Information](https://portal.ct.gov/drs/corporation-tax/tax-information) | Read for nexus, filing/deadlines, surtax extension, net-income bridge, NOLs, credit limits, penalties and amendments; capital illustration identified as 2025. | 2026-11-13 |
| [CGA Chapter 208](https://www.cga.ct.gov/current/pub/chap_208.htm) | Read for section 12-219 year-specific capital rate/minimum/ceiling and adjacent exceptions. | 2026-11-13 |
| [2025 CT-1120 instructions](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120-instructions_1225.pdf) | Read for all five pages, Schedules A-J, minimum/surtax/credit rules and filing instructions for 2025-2026 filing cycle. | 2026-11-13 |
| [2026 CT-1120ES](https://portal.ct.gov/-/media/drs/forms/2025/corp/ct-1120es_0126.pdf) | Read for all four pages, threshold, cumulative targets, payment dates and electronic waiver. | 2026-11-13 |
| [DRS 2026 developments](https://portal.ct.gov/drs/miscellaneous-taxes/other-tax-page/state-tax-developments/2026-developments) | Read for corporate section 168(n), section 174A and transition provisions. | 2026-11-13 |

| [CGA 2026 Chapter 208 supplement](https://www.cga.ct.gov/2026/sup/chap_208.htm) | Read for sections 12-214/12-219 surtax terminal year and capital-rate/mimimum adjacent clauses, contrasted with DRS overview. | 2026-11-13 |

## Not yet confirmed

- Final 2026 CT-1120/CT-1120CU annual forms and exact line mapping are not yet confirmed; final 2025 instructions are expressly the 2025-2026 filing cycle baseline.
- Section 174A/168(n) transition schedules, retroactive elections, relief conditions and special-industry/combined calculations need dedicated workpapers. The 2026 DRS notice establishes the changes, but this skill supplies no invented transition deduction.
- Credit-specific exceptions, amended/federal-adjustment special limitation periods and capital-base exclusions require the taxpayer's exact facts and current schedules.


Not yet confirmed: the DRS overview describes a surtax extension through income year 2028, while the fetched 2026 statutory supplement sections 12-214/12-219 still say income years before January 1, 2028. Both establish the 2026 surtax used here. The future terminal year needs reconciliation to the latest enacted act before a 2028 position; no 2028 surtax conclusion is supplied. [CGA 2026 supplement, read 2026-11-13 for sections 12-214 and 12-219 and neighboring clauses](https://www.cga.ct.gov/2026/sup/chap_208.htm).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ct-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ct-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
