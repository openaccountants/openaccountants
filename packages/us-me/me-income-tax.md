---
name: me-income-tax
description: "Maine 2026 resident wages and sole-proprietor income: AGI modifications, final deduction, exemption phaseouts, bands, surcharge and 1040ME estimates. Load us-tax-workflow-base first."
version: "0.2"
jurisdiction: US-ME
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: state-tax
type: computation
---

# Maine individual income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Ordinary Maine resident taxable income is taxed at 5.8%, 6.75% and 7.15%, plus a 2% surcharge above the applicable 2026 threshold. The revised final-return standard deductions differ from the amounts used for payroll withholding. [2026 rates, revised May 20](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf); [36 M.R.S.5111(7)](https://legislature.maine.gov/statutes/36/title36sec5111.html).

## Scope

Full-year resident wage earners and sole proprietors, including ordinary interest, rents and gains brought through federal AGI. Residency exceptions, nonresident/part-year computations, complex retirement and K-1 adjustments are partial boundaries. Corporate and payroll owners are `me-corporate-tax` and `me-payroll`. Load `us-form-1040-individual-return`, `us-schedule-c-and-se-computation`, `us-self-employed-health-insurance`, `us-self-employed-retirement`, `us-section-179-and-bonus-depreciation` and `us-qbi-deduction` for their federal computations; do not repeat their figures here.

## Ask the client first

1. Domicile, permanent homes, Maine days, move dates, military status and other-state workdays/returns?
2. Federal filing status, completed federal AGI, wage/sole-proprietor/K-1/rental/gain statements, ages, blindness and dependent status?
3. Bond issuers, Social Security/railroad benefits, pension payer/type, retirement age/distribution code and state asset-basis schedules?
4. Federal itemized expenses, Maine adjustments, other-state tax and credit evidence, dependent/childcare/property records?
5. Maine withholding and estimates, prior-year liability and length, unusual income events and extensions?

## The method, step by step

1. **Confirm the resident route.** Maine domicile generally establishes residence, subject to statutory safe harbors. A nondomiciliary with a permanent Maine abode and more than 183 days is also resident, except the Armed Forces exception. Apply the complete exceptions in [36 M.R.S.5102(5)](https://legislature.maine.gov/statutes/36/title36sec5102.html); do not resolve residence by counting days alone.
2. **Reconcile federal AGI to Maine AGI.** Add other-state municipal-bond interest excluded federally. Subtract qualifying U.S.-obligation interest and Social Security/railroad benefits only to the extent included in AGI, observing related-expense limits. Federal Schedule C expenses, allowable home-office, half-SE-tax, health-insurance and retirement deductions already reflected in AGI are not deducted again. QBI is below AGI. Maine bonus/production-property and research adjustments require a separate state schedule, not an assumption that federal treatment carries over. [36 M.R.S.5122(1),(2)](https://legislature.maine.gov/statutes/36/title36sec5122.html).
3. **Separate pensions.** Qualifying military/uniformed-service retirement is fully subtracted under section 5122(2)(M-2). Other qualifying pension/IRA income, including public pensions, uses a maximum 2026 deduction of **$49,824 per eligible recipient**, reduced by all taxable and nontaxable Social Security/railroad benefits, never below zero and never above eligible income in AGI. Early-distribution, primary-recipient and federal penalty restrictions apply. Nonmilitary deductions phase out using **federal AGI**, not Maine AGI, under M-3. The indexed 2026 phaseout starts were not confirmed; stop before a high-income pension calculation. The old $25,000 cap and blanket public-pension exemption are superseded. [5122(2)(M-2),(M-3)](https://legislature.maine.gov/statutes/36/title36sec5122.html); [2026 estimates line 2](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_fillable.pdf); [5403(11)](https://legislature.maine.gov/statutes/36/title36sec5403.html).
4. **Compute deductions and exemptions.** Start with the final standard amount below, including applicable age/blind additions, or substantiated Maine itemized deductions. Maine itemized deductions other than medical/dental are capped at **$37,100**; medical/dental are outside that cap. Apply the deduction phaseout to the chosen deduction. Personal exemption is **$5,300** for each eligible taxpayer/spouse; a person claimed as another's dependent cannot claim their own, and an MFS spouse exemption has statutory conditions. Apply its separate phaseout. Taxable income = max(0, Maine AGI - allowed deduction - allowed personal exemptions). [2026 schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf); [5124-C](https://legislature.maine.gov/statutes/36/title36sec5124-C.html); [5126-A](https://legislature.maine.gov/statutes/36/title36sec5126-A.html); [deduction worksheet](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_item_stand_%20ded_phaseout_wksht_0.pdf); [exemption worksheet](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_pers_exempt_phaseout_wksht.pdf).
5. **Compute tax, credits and settlement.** Apply the band formula, then the 2% surcharge to taxable income above the status threshold. Substantiate each credit before applying it, then subtract Maine withholding and estimates. Other-state credit needs the other completed return and actual tax liability after credits, not that state's withholding. [5111](https://legislature.maine.gov/statutes/36/title36sec5111.html); [FAQ 27, other-jurisdiction credit](https://www.maine.gov/revenue/faq/individual-income-tax). Payroll withholding is a payment, not the final tax.

## Rates, bands and thresholds

The following formulas use **Maine taxable income T**, before credits. Quoted base-tax amounts are the official schedule amounts, not independently rounded marginal sums. [2026 final schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf).

| Status | First band | Middle band | Top band | Add 2% above | Authority |
| --- | --- | --- | --- | --- | --- |
| Single | T below $27,400: .058T | $27,400 to below $64,850: $1,589 + .0675(T-27,400) | $64,850+: $4,117 + .0715(T-64,850) | $1,000,000 | [2026 schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf) |
| MFS | Same ordinary bands as single | Same | Same | **$750,000** | [2026 schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf) |
| HOH | T below $41,100: .058T | $41,100 to below $97,300: $2,384 + .0675(T-41,100) | $97,300+: $6,178 + .0715(T-97,300) | $1,500,000 | [2026 schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf) |
| MFJ/qualifying surviving spouse | T below $54,850: .058T | $54,850 to below $129,750: $3,181 + .0675(T-54,850) | $129,750+: $8,237 + .0715(T-129,750) | $1,500,000 | [2026 schedule](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf) |

| Deduction/phaseout item | Single | MFS | HOH | MFJ/qualifying surviving spouse | Authority |
| --- | --- | --- | --- | --- | --- |
| Final 2026 basic standard deduction | $15,700 | $15,700 | $23,550 | $31,400 | [MRS 2026](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf) |
| Deduction phaseout starts, Maine AGI | $102,250 | $102,250 | $153,400 | $204,550 | [MRS 2026](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_item_stand_%20ded_phaseout_wksht_0.pdf) |
| Deduction reduction range | $75,000 | $75,000 | $112,500 | $150,000 | [MRS 2026](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_item_stand_%20ded_phaseout_wksht_0.pdf) |
| Exemption phaseout starts, Maine AGI | $341,000 | $204,575 | $375,050 | $409,150 | [MRS 2026](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_pers_exempt_phaseout_wksht.pdf) |
| Exemption reduction range | $125,000 | $62,500 | $125,000 | $125,000 | [MRS 2026](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_pers_exempt_phaseout_wksht.pdf) |

For either phaseout, reduction fraction = min(1, max(0,(Maine AGI - start)/range)); allowed amount = original amount x (1 - fraction). Additional standard deduction per qualifying age/blind condition is $1,650 for married/qualifying surviving spouse and $2,050 for unmarried taxpayers; check spouse eligibility and multiple conditions. [final rates and deduction notes](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf); [2026 deduction worksheet](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_item_stand_%20ded_phaseout_wksht_0.pdf); [2026 exemption worksheet](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_pers_exempt_phaseout_wksht.pdf).

## Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Depreciation / business income | Current section 5122(1)(WW) adds the net increase attributable to federal bonus depreciation; production-property and research modifications have separate rules and later recapture. Reconcile state basis. Federal home-office, insurance, retirement and Schedule C computation remains with the named owners. |
| Property-tax fairness | 2026 statutory maximum is $1,500 below age 65 and $2,000 age 65+, subject to eligibility/income rules; maximum is not an automatic credit. [2026 changes, PTFC](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf). Final worksheet and detailed eligibility not yet confirmed. |
| Earned-income / childcare / dependent credits | Retained as topics requiring current worksheets; the old blanket 12% EIC claim is not verified for 2026. Do not compute from it. |
| Nonresident, part-year or spouse-status difference | Schedule NR/NRH and resident credit can interact. Stop the full-year computation; obtain the actual allocation and current instructions. |
| Entity election or complex K-1 | Maine enacted an elective PTE program from 2026. Resolve entity election/owner modifications and credits separately; this skill does not prepare that election. [2026 changes, PTE program](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf). |
| Different tax year | Load that year's rates and forms; a 2026 metadata tag does not validate prior-year amounts or final form lines. |

## Worked cases

### Resident wage earner

Single, under 65, not blind or a dependent, $60,000 federal and Maine AGI, no adjustments/itemization/credits and $2,800 withheld. Taxable income is $39,000. The official middle-band formula yields $2,372, leaving $428 illustrated overpayment, before final return rounding.

```oa-check
name: ME resident wages 2026
inputs:
  agi: 60000
  withheld: 2800
steps:
  - taxable: max(0, agi - 15700 - 5300)
  - tax: 1589 + (taxable - 27400) * 0.0675
  - overpayment: withheld - tax
expected:
  taxable: 39000
  tax: 2372
  overpayment: 428
```

### Married filing separately at the surcharge boundary

An MFS taxpayer has $800,000 Maine AGI, no other adjustments. Both deduction and exemption are fully phased out. Taxable income remains $800,000. Ordinary tax is $56,680.225 and the surcharge adds $1,000, for $57,680.225 before whole-dollar return rounding. Using the single $1 million threshold would miss the surcharge.

```oa-check
name: ME MFS surcharge 2026
inputs:
  agi: 800000
steps:
  - deduction: 15700 * (1 - min(1, max(0, (agi - 102250) / 75000)))
  - exemption: 5300 * (1 - min(1, max(0, (agi - 204575) / 62500)))
  - taxable: agi - deduction - exemption
  - ordinary: 4117 + (taxable - 64850) * 0.0715
  - surcharge: max(0, taxable - 750000) * 0.02
  - tax: ordinary + surcharge
expected:
  deduction: 0
  exemption: 0
  taxable: 800000
  ordinary: 56680.225
  surcharge: 1000
  tax: 57680.225
```

## When to refuse or refer

Refer contested domicile/safe harbors, nonresident/part-year and multistate allocations, high-income pension phaseout, complex K-1/PTE, asset-basis/NOL, amended returns, trusts/estates and corporate or insurance returns. Keep unknown credit or adjustment amounts explicitly unresolved rather than estimating them.

## Filing and payment

Use Form 1040ME through the Maine Tax Portal. The 2026 forms page lists Schedule 1A additions, 1S subtractions, 2 itemized deductions, A tax adjustments/childcare, CP voluntary contributions/park passes, separate PTFC/STFC and NR/NRH. These correct the old schedule map. Final return/instruction downloads were still inactive labels when read; do not assert final line numbers. [2026 form index](https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2026).

The ordinary calendar-year due date is April 15 following the tax year, subject to weekend/holiday relief; confirm the published 2027 filing calendar. Maine grants an automatic six-month filing extension without requiring a federal extension. It does not extend payment: paying at least 90% by the original deadline avoids late-payment penalty, while interest applies to unpaid tax. [FAQ 2 and 4](https://www.maine.gov/revenue/faq/individual-income-tax).

2026 estimates apply when expected tax after credits/withholding is at least $1,000 **and prior-year tax is at least $1,000**. Ordinary safe harbor is the lesser of prior-year 100% (12-month year) or current 90%, but an unusual event producing at least $500,000 more nonwithheld Maine taxable income than the corresponding prior-year installment period has its own 90% rule. Regular installments are April 15, June 15, September 15, 2026 and January 15, 2027. Farming/fishing and annualization need the special instructions. [1040ES-ME 2026 instructions 1-6](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_fillable.pdf).

## Completion checklist

Confirm resident route and source year; reconcile federal AGI; preserve state-basis and pension records; apply both phaseouts separately; calculate the status-specific surcharge; support credits and payments; resolve final 2026 forms/calendar and every listed gap before filing.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 2026 individual schedule revised May 20; read for all bands, deductions, exemptions and surcharge. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/2026-05/ind_tax_rate_sched_2026_rev.pdf | 2026-11-13 |
| 36 M.R.S.5111; read for current ordinary rates and subsection 7, with neighboring repealed surcharge. | https://legislature.maine.gov/statutes/36/title36sec5111.html | 2026-11-13 |
| 36 M.R.S.5102; read for resident definitions and complete safe harbors. | https://legislature.maine.gov/statutes/36/title36sec5102.html | 2026-11-13 |
| 36 M.R.S.5122; read for bond/benefit modifications, pension conditions, bonus and production-property additions. | https://legislature.maine.gov/statutes/36/title36sec5122.html | 2026-11-13 |
| 36 M.R.S.5124-C; read for 2026 deduction and neighboring 2025/2027 rules. | https://legislature.maine.gov/statutes/36/title36sec5124-C.html | 2026-11-13 |
| 36 M.R.S.5126-A; read for dependent/spouse conditions and phaseout. | https://legislature.maine.gov/statutes/36/title36sec5126-A.html | 2026-11-13 |
| 2026 deduction worksheet; read for phaseout starts/ranges and itemized cap. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_item_stand_%20ded_phaseout_wksht_0.pdf | 2026-11-13 |
| 2026 exemption worksheet; read for phaseout starts/ranges. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_pers_exempt_phaseout_wksht.pdf | 2026-11-13 |
| 2026 1040ES-ME, revised July; read for threshold, safe harbor, unusual-event restriction, dates and pension cap. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/26_1040es_fillable.pdf | 2026-11-13 |
| 2026 individual form index; read for active estimates and inactive final-return/instruction labels; current schedule titles. | https://www.maine.gov/revenue/tax-return-forms/individual-income-tax-2026 | 2026-11-13 |
| MRS individual FAQ, revised April 13; read for extension, due date and other-jurisdiction credit. | https://www.maine.gov/revenue/faq/individual-income-tax | 2026-11-13 |
| MRS 2026 enacted changes; read for PTFC maxima, PTE program and enacted adjustment boundaries. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/legischange26.pdf | 2026-11-13 |
| 36 M.R.S.5403; read for pension indexing requirement. | https://legislature.maine.gov/statutes/36/title36sec5403.html | 2026-11-13 |

Not yet confirmed: final 2026 return/instruction lines and 2027 filing-calendar relief; indexed 2026 pension phaseout starts; full credit worksheets/eligibility (including EIC, childcare and PTFC); specialized nonresident/PTE/asset-basis computations. No 2025 amount is silently projected into 2026.
