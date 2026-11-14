---
name: ny-estimated-tax
description: "Work out and pay New York estimated tax for 2026 on Form IT-2105 for an individual, usually a self-employed New York resident. Covers who must pay (at least $300 of New York State, New York City or Yonkers tax after withholding and credits, or any MCTMT), the four 2026 installment dates (April 15, June 15, September 15, 2026 and January 15, 2027), the required annual payment (90% of 2026 tax, or 100% of 2025 tax, 110% when 2025 New York AGI or MCTD self-employment earnings were over $150,000), the estimated MCTMT at 0.60% and 0.34% once a zone's earnings exceed $150,000, the Yonkers 16.75% surcharge, the annualized method and the Form IT-2105.9 penalty. Trigger on \"IT-2105\", \"NY estimated tax\", \"New York quarterly tax\", \"NYC estimated tax\", \"IT-2105.9\", \"NY underpayment penalty\". Corporate, partnership, fiduciary and PTET estimates are out of scope."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ny-estimated-tax"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# New York estimated tax for individuals (Form IT-2105), tax year 2026

> **Source-cited draft.** Built from the 2026 Form IT-2105 instructions (IT-2105-I) and the 2025 Form IT-2105.9 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Pay New York estimated tax for 2026 if, after withholding, partnership or S corporation payments and credits, you expect to owe **at least $300** of New York State, New York City or Yonkers tax, or **any** MCTMT. Pay in four equal parts on **15 April, 15 June, 15 September 2026 and 15 January 2027**. To avoid the penalty, withholding plus estimates must reach the smaller of **90%** of the 2026 tax or **100%** of the tax on the 2025 return (**110%** if 2025 New York AGI, or MCTD self-employment earnings, was over **$150,000**, $75,000 if married filing separately). For 2026 the MCTMT applies only when a zone's net earnings from self-employment exceed **$150,000** (it was $50,000 for 2025).

## Scope and who this is for

In scope: individuals paying New York State, New York City and Yonkers income tax and the MCTMT in advance for tax year 2026 on Form IT-2105, the required annual payment, the installment amounts, and the underpayment penalty on Form IT-2105.9. The figures that make up the tax itself (rates, deductions, credits) belong to the return skill and are linked, not restated, except the MCTMT figures printed on the estimated tax worksheet.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Computing the 2026 state and city tax itself | `ny-it-201-resident-return` |
| New York City UBT estimates (Form NYC-5UBTI) | `nyc-ubt` |
| MCTMT rules beyond the estimate (zones, allocation, employers) | `ny-mctmt` |
| Federal estimated tax | `us-quarterly-estimated-tax` |
| Pass-through entity tax estimates | `ny-pte-tax-ptet` |
| Corporations (CT-400), partnerships, estates and trusts | refer |

## Ask the client first

1. **The 2025 New York return** (Form IT-201 or IT-203): the total of New York State, New York City, Yonkers and MCTMT tax shown, the New York AGI, and whether it covered a full 12 months.
2. **Expected 2026 income**, and whether it arrives evenly or late in the year (the annualized method helps uneven income).
3. **Where the client lives** (New York City, Yonkers, rest of state) and where the business is carried on (MCTD Zone 1, Zone 2 or outside), with the expected net earnings from self-employment in each zone.
4. **Expected 2026 withholding** from any job, and any estimated tax paid for the client by a partnership or S corporation.
5. **Any 2025 overpayment** applied to 2026.
6. **Filing status**, because the $150,000 test is $75,000 for married filing separately.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Estimated income tax required when New York State, New York City or Yonkers tax owed after withholding and credits is at least | $300 | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Estimated MCTMT required when expected MCTMT is | any amount | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| MCTMT Zone 1 rate (the five New York City counties), on all Zone 1 earnings once they exceed $150,000 | .60% (.0060) | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| MCTMT Zone 2 rate (Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester), on all Zone 2 earnings once they exceed $150,000 | .34% (.0034) | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| MCTMT threshold per person, per zone (must be exceeded) | $150,000 | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Required annual payment, current-year route | 90% of the 2026 tax | [IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Required annual payment, prior-year route | 100% of the tax on the 2025 return | [IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Prior-year route for higher incomes: 110% when 2025 New York AGI (or MCTD self-employment earnings) was more than | $150,000 ($75,000 married filing separately) | [IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Yonkers resident surcharge on the estimate | 16.75% of the net New York State tax | [IT-2105-I (2026), line 22a](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Installment dates | 15 April, 15 June, 15 September 2026 and 15 January 2027 | [IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Underpayment penalty rate, periods from 15 April 2025 to 15 April 2026 (2025 tax year) | 9.5% | [IT-2105.9-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it2105_9i.pdf) |

### Steps

1. **Estimate the 2026 tax** for each column of the IT-2105 worksheet: New York State, New York City, Yonkers and MCTMT. Use the 2026 rate schedules and worksheets in `ny-it-201-resident-return` (the same 2026 rates are printed in IT-2105-I, page 10). Subtract expected credits, including the IT-219 UBT credit for city residents ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
2. **MCTMT column.** For each zone, take the expected net earnings from self-employment allocated to it (federal Schedule SE, Part 1, line 6, for that business). If a zone's earnings do not exceed $150,000, there is no MCTMT for that zone. If they do, apply the zone rate to **all** of them, not only the excess. Test each spouse separately, even on a joint return. No credit reduces the MCTMT ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
3. **Yonkers residents:** the surcharge is 16.75% of the New York State column (line 22a). Yonkers nonresidents with Yonkers wages or business earnings estimate the nonresident earnings tax (see `ny-it-201-resident-return`).
4. **Net it down:** subtract expected withholding, estimated tax paid on Forms IT-2663 or IT-2664, and estimated tax paid for the client by a partnership or S corporation. If less than $300 of income tax is left in every column and no MCTMT is expected, no estimates are required.
5. **Required annual payment:** the smaller of (a) 90% of the 2026 tax and (b) 100% of the tax shown on the 2025 return, raised to 110% when 2025 New York AGI or MCTD self-employment earnings were over $150,000 ($75,000 married filing separately). The prior-year route needs a 2025 return covering a full 12 months ([IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
6. **No-liability rule:** no penalty applies to a New York resident (or a nonresident or part-year resident with New York source income) who had no tax liability for a full 12-month 2025 tax year ([IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)). The older version of this skill said a first-year filer should use "a prior-year safe harbour of zero"; the rule is this no-liability exception, which needs a full 12-month 2025 year with no liability.
7. **Installments:** one quarter of the required payment on each date, less any 2025 overpayment applied to the first installment. Enter each amount rounded to the nearest dollar on the voucher.
8. **Late start:** if the requirement is first met after 31 March and before 1 June, start 15 June 2026; after 31 May and before 1 September, start 15 September 2026; after 31 August, pay 15 January 2027. A large mid-year change in income should use the annualized income installment method (Form IT-2105.9-I) ([IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
9. **January skip:** filing the 2026 return and paying the full balance by 31 January 2027 removes the 15 January 2027 installment ([IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
10. **Farmers and fishermen** (two-thirds or more of 2025 or 2026 federal gross income from farming or fishing) have one installment: 66⅔% of the 2026 tax by 15 January 2027, or file the 2026 return by 1 March 2027 and pay in full ([IT-2105-I (2026), page 1](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
11. **Changes during the year:** re-estimate on the amended estimated tax worksheet (IT-2105-I, page 14) and adjust the remaining installments.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Income tax due after withholding under $300 in every column, no MCTMT expected | No estimates required |
| Any MCTMT expected | Estimates required for the MCTMT, even if income tax is under $300 |
| Zone earnings exactly $150,000 | Not over the threshold: no MCTMT for that zone |
| Zone earnings $150,001 or more | MCTMT on the whole zone amount |
| Earnings in both zones | Test and compute each zone separately; tax can be owed in both |
| 2025 New York AGI over $150,000 ($75,000 married filing separately) | Prior-year route is 110%, not 100% |
| 2025 return covered less than 12 months | Only the 90% current-year route or the annualized method |
| No tax liability for a full 12-month 2025 year | No underpayment penalty |
| Income earned mainly late in the year | Annualized income installment method on Form IT-2105.9; file the form with the return |
| UBT for a New York City business | Separate estimates on Form NYC-5UBTI (`nyc-ubt`), not on IT-2105 |
| Nonresident or part-year resident with New York income | Same form; tax estimate from the IT-203 method (`ny-residency-leaving-new-york`) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| 2025 New York AGI | Assume over $150,000 and use 110% for the prior-year route; ask |
| Zone where the business is carried on | Ask for the county; do not include MCTMT until known, and flag |
| New York City residence | Do not estimate city tax until residence is confirmed |
| 2025 return figures | Use the 90% current-year route only |
| Pattern of income during the year | Equal installments; flag the annualized method for the reviewer |

### Telling estimate payments apart in the bank feed

| Pattern on the statement | What it is |
| --- | --- |
| NYS DTF, NY STATE TAX, TAX.NY.GOV PAYMENT, IT-2105 around 15 April, 15 June, 15 September, 15 January | New York estimated tax |
| IRS, EFTPS, federal estimated | Federal estimated tax, not New York |
| NYC DOF or NYC Finance around the same dates | New York City UBT estimate (`nyc-ubt`) or property tax, not IT-2105 |
| NY sales tax, NYS penalty or interest, IT-201 balance | Not an estimate; flag the return balance for the reviewer |

## Worked cases

The clients are invented. The rates and thresholds are from the sources above and the 2026 rate schedules in IT-2105-I.

**Case 1, a decision: the 90% route or the 100% route?** A single Manhattan freelancer expects 2026 New York AGI of USD 120,000 and taxable income of USD 112,000 (standard deduction USD 8,000), with no withholding and no credits. Zone 1 net earnings are USD 130,000, under the USD 150,000 threshold, so no MCTMT. New York AGI is over USD 107,650, so the state tax comes from worksheet 7: rate-schedule tax USD 6,040.65 plus the recapture 0.2470 x USD 567.35 = USD 140.14, total USD 6,180.79. City tax: USD 1,813 + 3.876% x USD 62,000 = USD 4,216.12. Total 2026 tax USD 10,396.91; 90% is USD 9,357.21. The 2025 return showed USD 9,500 of tax, with 2025 New York AGI of USD 140,000 (not over USD 150,000), so the prior-year route is 100% = USD 9,500.

Decision: the required payment is the smaller, USD 9,357.21 (USD 2,339.30 a quarter). But the 90% route holds only if the 2026 estimate is right; the 100% route is fixed. Paying USD 2,375 a quarter (USD 9,500) costs USD 142.79 more and removes the risk if 2026 income comes in higher. Recommend the prior-year route unless the client is confident in the estimate.

```oa-check
name: NY 2026 estimated tax, 90% against 100% route, Manhattan freelancer
inputs:
  ny_agi: 120000
  taxable_income: 112000
  prior_year_tax: 9500
  prior_year_agi: 140000
steps:
  - rate_schedule_tax: 4191 + 0.059 * (taxable_income - 80650)
  - flat_tax: taxable_income * 0.059
  - phase_in: round((ny_agi - 107650) / 50000, 4)
  - state_tax: rate_schedule_tax + (flat_tax - rate_schedule_tax) * phase_in
  - city_tax: 1813 + 0.03876 * (taxable_income - 50000)
  - total_tax: state_tax + city_tax
  - current_route: total_tax * 0.9
  - prior_route: prior_year_tax * 1.00
  - required: min(current_route, prior_route)
  - quarterly: required / 4
expected:
  rate_schedule_tax: 6040.65
  state_tax: 6180.79
  city_tax: 4216.12
  total_tax: 10396.91
  current_route: 9357.21
  required: 9357.21
  quarterly: 2339.30
```

**Case 2, MCTMT and the 110% rule.** A single Brooklyn consultant expects 2026 state and city tax of USD 16,920 and Zone 1 net earnings from self-employment of USD 180,000. That exceeds USD 150,000, so the MCTMT is 0.60% of the whole USD 180,000 = USD 1,080, and estimates are required for it. Total 2026 tax USD 18,000; 90% is USD 16,200. The 2025 return showed USD 14,000 of tax with New York AGI of USD 200,000, over USD 150,000, so the prior-year route is 110% = USD 15,400. Required annual payment: USD 15,400, or USD 3,850 a quarter. With the 2025 threshold of USD 50,000 the same earnings would also have owed MCTMT; with Zone 1 earnings of USD 140,000 in 2026 there would be none.

```oa-check
name: NY 2026 estimated tax with MCTMT and the 110% prior-year route
inputs:
  income_tax: 16920
  zone1_earnings: 180000
  prior_year_tax: 14000
  prior_year_agi: 200000
steps:
  - mctmt: zone1_earnings * 0.006 * min(max(zone1_earnings - 150000, 0), 1)
  - total_tax: income_tax + mctmt
  - current_route: total_tax * 0.9
  - prior_route: prior_year_tax * 1.1
  - required: min(current_route, prior_route)
  - quarterly: required / 4
expected:
  mctmt: 1080.00
  total_tax: 18000.00
  current_route: 16200.00
  prior_route: 15400.00
  required: 15400.00
  quarterly: 3850.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NY-ET-1 | Corporation (Form CT-400) | Refer: corporate estimated tax rules differ |
| R-NY-ET-2 | Partnership, estate or trust estimates, or MCTMT paid on behalf of partners | Refer |
| R-NY-ET-3 | PTET estimated payments | Use `ny-pte-tax-ptet` |
| R-NY-ET-4 | Penalty waiver or abatement request | Refer: a procedural matter for a professional |
| R-NY-ET-5 | Annualized method with irregular income across all four columns | Compute only with the reviewer; file Form IT-2105.9 with the return |
| R-NY-ET-6 | No reliable estimate of 2026 tax and no 2025 return | Do not guess a required payment; ask for the figures |

## Filing and payment

- **How to pay:** online through an Individual Online Services account by bank debit (ACH), with no voucher; or Form IT-2105 with a check or money order payable in U.S. funds to NYS Income Tax; or by credit card through the Department's vendor ([IT-2105-I (2026), page 2](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)). Do not send a voucher without a payment.
- **Due dates:** 15 April, 15 June and 15 September 2026, and 15 January 2027; a date on a weekend or legal holiday moves to the next workday.
- **2025 overpayment** elected as a credit: apply it to the first installment and pay the rest.
- **After the year:** report all payments on the 2026 Form IT-201 or IT-203. If the payments fell short, compute the penalty on Form IT-2105.9 or let the Department bill it. The penalty runs from each installment date until paid, at the rate the Department sets each quarter (the federal short-term rate plus 5.5 points, at least 7.5%); for 2025 periods it was 9.5% ([IT-2105.9-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it2105_9i.pdf)).

## Completion checklist

- Each column (state, city, Yonkers, MCTMT) estimated from the 2026 rates, with credits subtracted.
- MCTMT tested per person, per zone, against USD 150,000, and computed on the whole zone amount when over.
- Withholding, IT-2663 and IT-2664 payments and partnership payments subtracted.
- 2025 New York AGI compared with USD 150,000 (USD 75,000 married filing separately) to pick 100% or 110%.
- The required payment set at the smaller route, and the risk of the 90% route explained.
- Installment dates and amounts given to the client, and the January skip rule noted.
- Annualized method flagged where income is uneven.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Instructions for Form IT-2105 (2026). Read for who must pay ($300, any MCTMT), the MCTMT rates (0.60%, 0.34%) and $150,000 threshold, the 2026 installment dates, the late-start table, the January 31 rule, farmers and fishermen, the 90%, 100% and 110% routes with the $150,000 and $75,000 tests, the no-liability rule, payment methods, line 22a (16.75%) and the page 10 rate schedules. | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| Instructions for Form IT-2105.9 (2025). Read for the penalty rate formula (federal short-term rate plus 5.5 points, at least 7.5%), the 9.5% rate for 2025 periods and the annualized worksheets. | https://www.tax.ny.gov/pdf/current_forms/it/it2105_9i.pdf | 2026-11-13 |

Not yet confirmed: the 2026 Form IT-2105.9 instructions are not published, so the penalty rate for periods after 15 April 2026 is not stated; the 2026 tax figures behind each column come from IT-2105-I (2026) because the 2026 Form IT-201 instructions are not yet published.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ny-estimated-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ny-estimated-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
