---
name: mi-estimated-tax
description: "Work out whether a Michigan individual must pay 2026 estimated income tax on Form MI-1040ES, how much each installment should be, and what the MI-2210 underpayment penalty and interest are. Estimates are required when more than $500 is expected to be owed with the 2026 MI-1040, unless withholding covers 90% of the 2026 tax, 100% of the 2025 tax, or 110% of the 2025 tax when 2025 AGI was over $150,000 ($75,000 married filing separately). Installments are due 15 April, 15 June and 15 September 2026 and 15 January 2027. Penalty 10% (minimum $10) for paying too little or late, 25% (minimum $25) for not paying, plus interest at 1 point above the adjusted prime rate. Covers sole proprietors, freelancers and wage earners with too little withholding, uneven income, farmers and fishermen, and joint filers. Trigger on \"Michigan estimated tax\", \"MI-1040ES\", \"Michigan quarterly payments\", \"MI-2210\", \"Michigan underpayment penalty\", \"MCL 206.301\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-estimated-tax"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Michigan estimated income tax for individuals (MI-1040ES), tax year 2026

> **Source-cited draft.** Built from the 2026 MI-1040ES (Michigan Estimated Income Tax for Individuals) and its additional instructions, the 2026 Michigan Income Tax Withholding Guide, the Treasury 2026 rate notice and the 2025 City of Detroit Form 5118 instructions (for the Treasury interest rate), read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Pay Michigan estimated tax for 2026 if you expect to owe **more than $500** when you file the 2026 MI-1040, unless your withholding will be at least **90%** of the 2026 tax, **100%** of the 2025 tax, or **110%** of the 2025 tax if 2025 AGI was over **$150,000** ($75,000 married filing separately). The four installments are due **15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027**. Paying too little or late costs 10% of the shortfall (at least $10); not paying at all costs 25% (at least $25); interest runs at 1 point above the adjusted prime rate (8.48% a year to 30 June 2026).

## Scope and who this is for

In scope: an individual (or married couple filing jointly) with a 2026 Michigan income tax liability, resident or not (the estimate rules apply to both), who has income without enough Michigan withholding: sole proprietors, single-member LLC owners, freelancers, landlords, investors and wage earners with side income.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Computing the 2026 Michigan tax itself | `mi-income-tax` |
| City of Detroit estimates (Form 5123, threshold $100) | `mi-detroit-individual-return` |
| Federal estimated tax (Form 1040-ES) | `us-quarterly-estimated-tax` |
| Corporate income tax and flow-through entity tax estimates | `mi-corporate-income-tax` |
| Estates and trusts (MI-1041ES) | Refused |

## Ask the client first

1. **Expected 2026 Michigan income**: federal AGI, Schedule 1 adjustments, retirement subtraction, exemptions (see `mi-income-tax`).
2. **Expected 2026 Michigan withholding** (W-2 box 17, pension withholding) and expected refundable credits (homestead, home heating, Michigan EITC).
3. **The 2025 MI-1040 total tax** and whether the 2025 return covered 12 months.
4. **2025 federal AGI** (for the $150,000 test).
5. **Is at least two-thirds of gross income from farming, fishing or seafaring?**
6. **Is income uneven during the year** (seasonal business, a large Q3 contract, a Q4 capital gain)?
7. **Filing status for 2026**, and whether a married couple plans to file separately.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Estimates required if the balance expected on the 2026 MI-1040 is more than | $500 | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Withholding that avoids estimates: share of the 2026 tax | 90% | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Same, qualified farmers, fishermen and seafarers | 66 and 2/3% | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Withholding that avoids estimates: share of the 2025 tax | 100% | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Same, if 2025 AGI was more than $150,000 ($75,000 married filing separately) | 110% | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Installment due dates | 15 April 2026, 15 June 2026, 15 September 2026, 15 January 2027 | [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Penalty for paying too little or late | 10% of the tax due, minimum $10 | [2026 MI-1040ES additional instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Penalty for not making required estimated payments | 25% of the tax due, minimum $25 | [2026 MI-1040ES additional instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Interest | 1 point above the adjusted prime rate, reset 1 January and 1 July, by the day | [2026 MI-1040ES additional instructions](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf) |
| Interest rate, 1 January to 30 June 2026 | 8.48% a year (0.0002324 daily) | [2025 Form 5118 instructions, line 22b (Treasury rate)](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf) |
| Michigan rate for 2026 | 4.25% | [Treasury notice, 15 April 2026](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year) |
| Personal exemption for 2026 | $5,900 | [2026 Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |

### Step 1: is an estimate needed?

1. Estimate the 2026 Michigan tax (taxable income times 4.25%; see `mi-income-tax`), less nonrefundable credits.
2. Subtract expected Michigan withholding and refundable credits.
3. If the result is $500 or less, no estimates are required (voluntary payments are allowed).
4. If it is more than $500, check whether withholding alone will reach 90% of the 2026 tax, or 100% (110% above $150,000 AGI) of the 2025 tax. If so, no estimates are required.
5. Two-thirds farming, fishing or seafaring income: estimates are not needed if the person meets the qualifications on the MI-1040ES; otherwise 66 and 2/3% replaces 90%.

### Step 2: the required annual payment

Required annual payment = the smaller of (a) 90% of the 2026 tax and (b) 100% of the 2025 tax (110% if 2025 AGI was over $150,000, or $75,000 married filing separately). Option (b) needs a 2025 return covering 12 months. The figure for (a) is an estimate; (b) is known, so it is the safer choice unless 2026 income has clearly fallen.

### Step 3: the installments

Each installment = (required annual payment - expected withholding) divided by 4, on the four due dates. The whole amount may be paid with the first voucher on 15 April 2026. If income changes during the year, adjust the next installment; a client not yet paying estimates whose income first arises in a later period pays from that period: change between 1 January and 31 March, pay by 15 April 2026; 1 April to 31 May, by 15 June 2026; 1 June to 31 August, by 15 September 2026; later, by 15 January 2027.

### Step 4: uneven income

Where income arrives late in the year, the MI-2210 lets the required installments follow the income actually earned by each period (the annualized method, like federal Form 2210 Schedule AI): annualize the income to the end of each period, compute the tax on it, and take the cumulative share of the required payment for that period (22.5%, 45%, 67.5% and 90% under the 90% rule). It avoids a penalty for early quarters in which little was earned. The 2026 MI-2210 periods and factors were not re-read: check them on the form before using this method.

### Step 5: penalty and interest (MI-2210)

For each installment paid late or short: penalty 10% of the shortfall (at least $10), or 25% (at least $25) if no estimate was made; plus interest from the installment date to the date paid, at the daily Treasury rate. The penalty and interest are added to the balance on the MI-1040; the MI-2210 computes them, or Treasury bills them.

### Paying

- **Electronic:** Michigan Treasury eServices (www.michigan.gov/iit): direct debit (eCheck) from a checking or savings account, or a credit or debit card. No voucher is mailed.
- **By post:** check payable to "State of Michigan", the last four digits of the Social Security number and "2026 MI-1040ES" written on it, with that installment's voucher, to Michigan Department of Treasury, P.O. Box 30774, Lansing, MI 48909. Do not staple or combine with other payments.
- **Married filing separately:** separate vouchers and payments for each spouse; do not use preprinted vouchers that carry both numbers. A full Social Security number is needed on every voucher.

Source: [2026 MI-1040ES](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Sole proprietor with no withholding | Estimates almost always due once the expected tax passes $500 |
| Wage earner with correct MI-W4 | Usually none |
| Wage earner with side Schedule C income | Run step 1 |
| Retiree with no Michigan pension withholding | Estimates if the tax after the retirement subtraction passes $500 |
| First year in business, no 2025 Michigan return | Only the 90% current-year test is available |
| Mid-year change in withholding | Recompute the remaining installments; earlier ones stand |
| Large Q4 gain | Annualized method usually avoids penalty on earlier quarters |
| Detroit resident or worker | A separate city estimate (Form 5123) if more than $100 will be owed |
| Nonresident with Michigan income | The same rules apply |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| 2025 Michigan tax | Use the 90% current-year test only; ask for the 2025 MI-1040 |
| 2025 federal AGI | Assume over $150,000 if the 2025 tax suggests it; ask |
| Expected withholding | Zero |
| Filing status | As filed for 2025 |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| No estimates paid and a 2026 balance over $500 expected | 25% penalty per missed installment, plus interest |
| Income much higher than 2025 | Paying 100% (or 110%) of 2025 avoids penalty but leaves a large April 2027 balance |
| Married couple switching to separate returns | Separate vouchers; split prior payments |

## Worked cases

**Case 1, steady sole proprietor.** A single sole proprietor expects 2026 federal AGI of $120,000, with no Michigan withholding and one exemption. Expected 2026 tax: ($120,000 - $5,900) x 4.25% = $4,849.25. 2025 Michigan tax was $4,200 and 2025 AGI was $110,000 (not over $150,000). Required annual payment: the smaller of 90% x $4,849.25 = $4,364.33 and $4,200, so $4,200. Four installments of $1,050.

```oa-check
name: MI 2026 estimates, single sole proprietor
inputs:
  expected_agi: 120000
  exemption_amount: 5900
  rate: 0.0425
  prior_year_tax: 4200
  prior_year_agi: 110000
  withholding: 0
steps:
  - current_tax: (expected_agi - exemption_amount) * rate
  - prior_factor: 1 + 0.1 * min(max(prior_year_agi - 150000, 0), 1)
  - required: min(current_tax * 0.9, prior_year_tax * prior_factor)
  - installment: (required - withholding) / 4
expected:
  current_tax: 4849.25
  required: 4200
  installment: 1050
```

**Case 2, a decision: prior-year or current-year route for a high earner whose income fell.** A married couple filing jointly had 2025 AGI of $180,000 and 2025 Michigan tax of $7,000. For 2026 they expect $6,000 of tax and no withholding. Prior-year route: 110% x $7,000 = $7,700 (2025 AGI was over $150,000). Current-year route: 90% x $6,000 = $5,400. The current-year route needs $2,300 less in 2026, paid as four installments of $1,350; the risk is that 2026 income comes in higher than expected and the 90% test is missed. Recommend the current-year route with a review before the 15 September 2026 installment.

```oa-check
name: MI 2026 estimates, high earner, current-year against prior-year route
inputs:
  prior_year_tax: 7000
  prior_year_agi: 180000
  expected_tax: 6000
steps:
  - prior_route: prior_year_tax * 1.1
  - current_route: expected_tax * 0.9
  - required: min(prior_route, current_route)
  - installment: required / 4
  - cash_saved_in_2026: prior_route - current_route
expected:
  prior_route: 7700
  current_route: 5400
  required: 5400
  installment: 1350
  cash_saved_in_2026: 2300
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| MI-EST-R-01 | Estate or trust estimates (MI-1041ES) | Refuse |
| MI-EST-R-02 | Flow-through entity tax estimates | Refer to `mi-corporate-income-tax` |
| MI-EST-R-03 | Corporate income tax estimates | Refer to `mi-corporate-income-tax` |
| MI-EST-R-04 | Business income apportioned between Michigan and other states | Refer |
| MI-EST-R-05 | Part-year resident whose Michigan tax needs Schedule NR | Refuse: the tax itself is out of scope |
| MI-EST-R-06 | City estimates other than Detroit | Refuse |
| MI-EST-R-07 | A tax year other than 2026 | Refuse |
| MI-EST-R-08 | Composite returns for nonresident members | Refuse |
| MI-EST-R-09 | A request to waive the penalty for reasonable cause | Refer: draft the statement for review; interest is not waived |

## Filing and payment

Pay each installment by its due date through Treasury eServices or by post with the voucher (see "Paying" above). No reminder notices are sent. Report the total paid on the 2026 MI-1040 (due 15 April 2027) and attach the MI-2210 if a penalty applies or the annualized method is used.

## Completion checklist

- Expected 2026 tax computed with the $5,900 exemption and 4.25% rate.
- $500 test run after withholding and refundable credits.
- 2025 tax and 2025 AGI used for the 100% or 110% test.
- Installment schedule set for 15 April, 15 June, 15 September 2026 and 15 January 2027.
- Separate vouchers for spouses filing separately.
- Detroit Form 5123 estimate considered for Detroit residents and workers.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 MI-1040ES, Michigan Estimated Income Tax for Individuals, with additional instructions. Read for the $500 test, 90%, 66 and 2/3%, 100% and 110% (AGI over $150,000 or $75,000), the four due dates, the period chart, payment methods and address, and the 10% / 25% penalties and interest basis. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf | 2026-11-13 |
| 2025 City of Detroit Form 5118 instructions (Michigan Treasury). Read for the Treasury interest rate of 8.48% to 30 June 2026. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/City-IIT/TY2025/5118-Instr.pdf | 2026-11-13 |
| Treasury notice: 4.25% rate for 2026 (15 April 2026). Read for the 2026 rate. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year | 2026-11-13 |
| 2026 Michigan Income Tax Withholding Guide (Form 446). Read for the $5,900 exemption. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf | 2026-11-13 |

Not yet confirmed: the interest rate from 1 July 2026 (the old file said 7.85%; not re-read); the 2026 MI-2210 itself, including its annualization periods and factors; the farmer and fisherman alternative dates (the old file said a single payment by 15 January or filing by 1 March; not re-read); card fees; MCL 206.301, 205.23 and 205.24 themselves (legislature.mi.gov returned errors, so the rules were read from the MI-1040ES).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-estimated-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-estimated-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
