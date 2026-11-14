---
name: nd-estimated-tax
description: 'Compute North Dakota 2026 individual estimated income tax on actual 2026 FormND-1ES: all four duty
  tests, net-tax definition, current/prior safe harbors, withholding, installments, marital/new-resident exceptions
  and payment evidence. Covers latest 2025-2026 ND-1UT filing-cycle mechanics with explicitfinal 2026 formgap. Trigger
  on ND estimated tax, ND-1ES, quarterly payments, annualization and ND-1UT interest.'
jurisdiction: US-ND
tax_year: 2026
last_updated: '2026-11-14'
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: '0.3'
type: computation
category: state-tax
---

# North Dakota individual estimated tax, 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. Circular 230 section 10.37: this is a sourced working-paper method, not an opinion or permission to file. Resolve taxpayer facts, source gaps and professional review before acting.

**Answer first.** Use all four tests on the actual 2026 ND-1ES. A first-year/no-prior-return taxpayer is not automatically required to pay estimates merely because the current-year tax is large. Net tax liability means tax after allowable credits **before withholding and estimates**; subtract withholding once when computing the payment gap. [2026 instructions/worksheet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); [NDCC 57-38-62(1),(4),(5)](https://ndlegis.gov/cencode/t57c38.pdf).

## Scope and who this is for

Individual ND-1ES payments for calendar 2026, including self-employed individuals, disregarded SMLLC owners, individual pass-through owners and employees with insufficient ND withholding. `nd-income-tax` owns state tax rates/modifications and the projected net-tax result; `us-quarterly-estimated-tax` owns the federal requirement and federal annualization method. Corporate, entity-level pass-through and fiduciary estimates have separate forms/rules; do not use individual vouchers for them.

This skill owns the operational ND-1ES workflow. The read final ND-1UT is tax 2025, filed in 2026; its line/rounding examples below are labelled **2025-2026 filing cycle**, not a claim that final 2026 ND-1UT exists. [Latest checked final ND-1UT](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf).

## Ask the client first

1. Is this an individual, which tax year/fiscal period, which filing status, and full-year/nonresident/part-year? When did ND-source income begin?
2. Is federal estimated income tax required, whether or not the taxpayer actually paid it? Obtain the federal worksheet and annualized-method election if used.
3. What is prior-year ND net tax, was a return required, and did a move into ND occur during that prior year? Capture marital-status changes.
4. What current ND net tax does `nd-income-tax` project after credits, and what ND withholding is expected? Keep federal withholding separate.
5. What estimates, prior overpayment allocations, late payments and extension payments actually posted, with dates and confirmation numbers?
6. Is farming, uneven income, a short/fiscal year or a waiver/notice involved? Obtain the timing records and supporting federal schedules.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount / rule and condition | Official authority |
| --- | --- | --- |
| Federal gateway | Federal estimated tax must be required; actual payment is irrelevant to that duty test | [p 1 condition 1](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf) |
| Prior-year test | 2025 net tax liability at least USD 1,000; no required 2025 NDreturn means zero for this test | [p 1 condition 2; worksheet 12](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf) |
| Current balance test | Expected 2026 net tax less ND withholding at least USD 1,000 | [p 1 condition 3; worksheet 10](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf) |
| Insufficient withholding | Withholding less than the smaller of 90% current net tax or 100% prior net tax; substitute 66 2/3% for a qualified farmer | [p 1 condition 4; worksheet 11-14](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf) |
| Regular calendar payments | One-fourth of the minimum annual payment by April 15, June 15, September 15,2026 and January 15,2027; next-business-day relief for weekend/legal holiday | [p 1 payment dates](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); [57-38-63](https://ndlegis.gov/cencode/t57c38.pdf) |
| Fiscal/short years | Fiscal dates are 15th day of months 4/6/9 and following month 1; statute has separate final-payment and short-period exceptions | [57-38-63](https://ndlegis.gov/cencode/t57c38.pdf); [p 1](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf) |
| Estimated underpayment interest |12% annually, from each installment due date to payment or ordinary return due date, whichever earlier; statute excludes the ordinary late-payment penalty provisions for estimates | [p 1](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); [57-38-62(3)](https://ndlegis.gov/cencode/t57c38.pdf) |

All four duty tests must hold. Exactly USD 1,000 meets a threshold; “more than” and “exceeds” in the old draft were wrong. Withholding satisfying the annual safe harbor removes the gap. The state prior-year test is 100%, with no federal-style high-income step-up. Never apply a federal safe-harbor percentage to the ND prior tax. [Conditions 1-4](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); [57-38-62](https://ndlegis.gov/cencode/t57c38.pdf).

### Worksheet, exceptions and payment allocation

1. Worksheet 1 takes projected federal taxable income from the federal owner. Apply supported state additions/subtractions in 2/4 to get 5; current ND tax comes from the state owner/2026 schedule, then credits 7 give **net tax 8**. No duplicated federal deductions or state bracket table here.
2. Withholding 9 reduces net tax 8 for the current-balance test 10. If below the threshold, stop. Test prior net tax 12 separately; if below threshold, stop. For ordinary eligible prior-year cases, choose the lesser of worksheet 11 and 12 for 13, then subtract withholding 9, floor at zero, to get 14. Do not subtract withholding before taking a percentage and then subtract it again.
3. **Prior-year exclusions.** NDCC 57-38-62(1)(b)(1) bars the prior-year alternative for an individual who moved into ND during the preceding tax year. The 2026 form specifically calls out a 2025 move with no earlier ND-source income. Use the current-year path for the statutory new-resident exclusion; escalate a fact pattern apparently supported by the form but barred by the broader statutory text, rather than quietly choosing the lower figure. No prior filing requirement means prior liability zero and the separate duty-test exemption, not an automatic current-year-only payment duty.
4. **Marriage transitions.** Separate-to-joint combines the prior separate net liabilities. Joint-to-separate reconstructs the prior taxes as if separate returns were required. Current separate filers make separate vouchers for their own incomes. [57-38-62(1)(b)(2)-(3)](https://ndlegis.gov/cencode/t57c38.pdf); [81-03-04-02(4)](https://ndlegis.gov/information/acdata/pdf/81-03-04.pdf); [married instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf).
5. **Nonresident/part-year.** For current projections,2026 ND-1ES 15-19 use tax on full taxable income, ND-source adjusted income and adjusted federal AGI; ratio 18 is rounded to **two decimals** and capped at 1. The final 2025 ND-1NR uses four decimals; do not transplant its ratio rounding. If ND-source income first begins after the first due date, divide the required estimate equally across the remaining due dates as instructed. Use the source-date statement and actual form; this is not a blanket deferral for existing residents with lumpy income. [p 1 and worksheet 15-19](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); `nd-cross-border-tax`.
6. **Farmers and annualization.** A federally qualified farmer may use the regular payments or the full required amount by January 15,2027; return filing remains at the ordinary date. NDAC 81-03-04-02(3)(a) separately waives state estimate interest when the qualifying farmer timely files/pays the federal return by the rule's March 1 date; it does not require early state filing/payment. Subsection(3)(c) recognizes the federal annualized method with the required state payments based on it. Obtain the federal annualization workpaper, calculate the ND base at each cutoff and carry the applicable exceptions to ND-1UT. Do not use the old draft's uncapped cumulative arithmetic as an installment calculator or assume fisherman eligibility from a federal rule. [Farmer](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf); [81-03-04-02(3)](https://ndlegis.gov/information/acdata/pdf/81-03-04.pdf).
7. Keep a dated payment ledger. The read ND-1UT normally allocates withholding evenly unless actual withholding timing is established. Prior-year overpayment defaults to the first required installment unless a different period was elected. Apply a quarter's payment to that quarter first; an excess offsets earlier outstanding underpayments starting with the earliest. Recompute interest in separate segments for partial/late payments; never charge overlapping interest on both the original and carried-forward shortfall. [lines 8-16 instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf); [57-38-62(6)](https://ndlegis.gov/cencode/t57c38.pdf); [81-03-04-03](https://ndlegis.gov/information/acdata/pdf/81-03-04.pdf).

### ND-1UT reconciliation, labelled 2025-2026 filing cycle

Complete Part 1 exceptions before Part 2. ItemsA/B/C/D cover qualified farmers, federal annualization, federal fourth-quarter exception and partial-year source timing. Attach the federal 2210 annualized worksheet forB and the source-timing statement forD. In Part 2, net tax 1, current percentage 2, withholding 3, balance 4, prior liability 5 and required payment 6 lead to quarterly required 7/payments 8 and the 9-15 carryovers. IfC applies, the last required quarter is zero; follow the stated federal timely-file/pay condition for that cycle. [both pages](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf).

Part 3 line 16b counts days;16c divides by 365 and rounds to three decimals;16d multiplies by the annual rate and again rounds to three decimals;16e multiplies by the applicable underpayment. Line 17 sums the quarter amounts and goes to ND-1 line 37. The final 2026 schedule and its dates/rounding must be checked before using this line map on a 2026 return. This schedule interest is distinct from ordinary delinquency/extension interest owned by `nd-income-tax`.

The old regulation still prints a USD 500 withholding-shortfall interest waiver in 81-03-04-02(3)(d); the current statute/form has the broader USD 1,000 tests. It is not a replacement threshold for 2026. A discretionary reasonable-cause waiver or absence of an electronic-payment mandate is not asserted without current authority.

## Boundary and exception table

| Situation | Result |
| --- | --- |
| No prior ND filing requirement, or prior net tax below threshold | No compulsory estimates under the prior-liability gateway; voluntary payment remains possible |
| Only federal safe harbor met | Check federal duty and all independent ND conditions; neither jurisdiction's dollar amount automatically satisfies the other |
| Income concentrated late | Test federal/state annualization; do not copy the old fixed factors/cumulative figures without the actual worksheet cap/recapture logic |
| Farm averaging, waiver request, historical amendment or disputed new-resident exception | Specialist computation; retain complete timing/election evidence |
| Entity/fiduciary estimates | Separate Form 40/58/60/38 workflow; individual-owner vouchers do not replace entity obligations |

## Worked cases

**Case 1, preserve the threshold decision.** The former Bismarck freelancer has USD 120,000 projected business profit and USD 97,500 projected state taxable income. For 2026 the state owner supplies rounded net tax USD 935, with prior net tax USD 1,420 and no withholding. Current balance is below the mandatory threshold, so estimates are not required. Voluntarily reserving the full projected state tax means four payments USD 233.75; that is a cash-flow choice, not a statutory minimum of USD 215 from the old 2025 illustration. Rates and federal deduction calculations remain in their owners. [worksheet 10/12/14](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf).

```oa-check
name: Below threshold versus voluntary full-tax reserve
inputs:
  current_net_tax_from_owner: 935
  withholding: 0
  payment_count: 4
steps:
  - balance: current_net_tax_from_owner - withholding
  - voluntary_each: max(balance, 0) / payment_count
expected:
  balance: 935
  voluntary_each: 233.75
```

**Case 2, high-income safe-harbor decision.** Preserve the old arithmetic inputs as **supplied net-tax figures**, not its unsupported claim that a particular wage/profit/FTI combination produces that tax. Current net tax USD 6,775, prior USD 5,900, withholding USD 4,800 and an established federal estimate requirement give current test USD 6,097.50 versus prior USD 5,900. The prior route wins; annual gap USD 1,100 and ordinary quarterly payment USD 275. Increasing withholding to USD 5,900 removes the gap. If the prior-year alternative is legally unavailable, use the current-year route: gap USD 1,297.50, quarterly USD 324.375 before voucher rounding. [worksheet 11-14](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf).

```oa-check
name: Prior-year route versus current-year route after withholding
inputs:
  current_net_tax: 6775
  prior_net_tax: 5900
  withholding: 4800
steps:
  - current_target: current_net_tax * 0.9
  - prior_target: prior_net_tax
  - ordinary_target: min(current_target, prior_target)
  - annual_gap: max(ordinary_target - withholding, 0)
  - ordinary_quarter: annual_gap / 4
  - current_only_gap: max(current_target - withholding, 0)
  - current_only_quarter: current_only_gap / 4
expected:
  current_target: 6097.50
  annual_gap: 1100
  ordinary_quarter: 275
  current_only_gap: 1297.50
  current_only_quarter: 324.375
```

### Other preserved numeric cases

- Prior net USD 4,000, current USD 6,800, withholding USD 1,200: current test USD 6,120 versus USD 4,000; annual gap USD 2,800, four USD 700 payments. This corrects the old inconsistent definition of “net tax” after withholding.
- Prior USD 1,500/current USD 2,000/no withholding: required annual USD 1,500 and four USD 375 payments, assuming all duty tests hold. For a USD 375 shortfall outstanding 92 days, the read 2025-2026 ND-1UT rounding gives round(92/365,3)=0.252; round(0.252×0.12,3)=0.030; interest USD 11.25. The old “three months” shorthand is replaced by actual days and form rounding.
- Fargo uneven-income scenarios (old USD 140,000 case and USD 185,000 contract case) remain annualization referrals with their original timing records retained in the workpaper. Send cumulative income to the federal annualization/state-tax owners; do not reuse old rounded tax amounts USD 178/810/1,786 or an amount above the annual required cap as if independently verified 2026 payments.

## When to refuse or refer

| Code | Preserve the boundary |
| --- | --- |
| R-NDES-01 | Estates/trusts: separate fiduciary rules |
| R-NDES-02 | Entity-level partnership/S-corporation/PTET obligations: separate from individual owner estimates |
| R-NDES-03 | Corporate estimates: `nd-corporate-tax` |
| R-NDES-04 | Disputed nonresident/part-year source allocation: `nd-cross-border-tax`, then form-specific review |
| R-NDES-05 | Farm averaging/qualified-farmer election: specialist workpaper |
| R-NDES-06 | Historical/amended quarters: obtain that year's source forms |
| R-NDES-07 | Discretionary waiver request: establish current legal basis and signed taxpayer facts; no guaranteed relief |

## Filing and payment

The official 2026 form permits electronic check or debit/credit-card payment through the agency's **Make A Payment** route at tax.nd.gov. Select the correct individual tax, year and estimate payment type; save the confirmation and independently check account posting. Do not assert that login is universally required, guess a processor percentage, or promise future-debit scheduling not shown in the read instructions. Do not mail a voucher when paying electronically.

For check/money order, complete the applicable installment voucher with taxpayer/spouse identification, address and amount. Make payable to **ND State Tax Commissioner**; put the last four SSN digits and **2026 ND-1ES** on the check. Mail with voucher to **Office of State Tax Commissioner, PO Box 5622, Bismarck,ND 58506-5622**. A standard-routing U.S./Canadian-bank check in U.S.dollars is required by the instructions. Keep the voucher, mailing proof and cancelled check. [p 1 payment instructions and vouchers](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf).

On the read 2025-2026 ND-1, line 26 is withholding;27 is estimates plus extension payments and elected prior overpayment; ordinary balance/refund and ND-1UT interest are separate. Estimates do not file ND-1, and a filing extension does not erase installment interest. [pp 15-16](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [line 17](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf).

## Completion checklist

- Four duty tests, statutory net-tax definition and exact threshold equality checked.
- Prior-year/new-resident/marriage restrictions resolved before selecting the lower route.
- Withholding deducted once; income/credit projection supplied by its owner.
- Annualization/farmer/partial-year exceptions documented, payment dates and overpayments reconciled.
- Correct year/voucher/payment posted; final 2026 ND-1UT rechecked before return filing.


## Sources

| Source and actual read scope | URL | Read on |
| --- | --- | --- |
| 2026 Form ND-1ES. Read for all instructions and worksheet for duty tests, net-tax definition, payment timing, mailing and interest; rates read only to check owner inputs. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28709-form-nd-1es-2026.pdf | 2026-11-14 |
| NDCC chapter 57-38. Read 57-38-04,57-38-62/63 and relevant neighbouring definitions; individual estimated duty, prior-year exclusions and sourcing. | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-14 |
| NDAC 81-03-04. Read 81-03-04-02/03 including farmer/annualized waivers, marital transitions and carryforward designation. | https://ndlegis.gov/information/acdata/pdf/81-03-04.pdf | 2026-11-14 |
| 2025 Schedule ND-1UT, 2025-2026 filing cycle. Read for both pages, exceptions, payment allocation, actual-day interest and rounding; not final 2026 form authority. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28704-schedule-nd-1ut-2025.pdf | 2026-11-14 |
| 2025 ND-1 booklet, 2025-2026 filing cycle. Read for residency/reciprocity pp 4-6, filing/extension pp 7-8, return lines pp 11-16 and state modifications; final 2026 lines not confirmed. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf | 2026-11-14 |
| 2025 Schedule ND-1NR, 2025-2026 filing cycle. Read for all columns, lines 1-23 and allocation instructions; four-decimal ratio. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28724-schedule-nd-1nr-2025.pdf | 2026-11-14 |

Not yet confirmed: final2026ND-1UT line numbers/rounding and final2026ND-1 payment lines; current discretionary waiver procedure, electronic mandate/fees/scheduling, detailed farm-averaging and disputed prior-year move treatment. Old lumpy-income arithmetic and claims that no prior return always forces estimates are not usable guidance.
