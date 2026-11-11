---
name: nz-income-tax-ir3-worked-examples
description: Worked examples for nz-income-tax-ir3 (New Zealand income tax, IR3, self-employed). The two recomputing examples from the parent skill, moved here word for word so each file stays under the size limit. MUST load alongside nz-income-tax-ir3.
version: 2.2
jurisdiction: NZ
tax_year: 2026
tax_year_notes: "Label 2026 means the tax year starting 1 April 2026 (2026-27, Inland Revenue's 2027 income year), whose annual rates are at Bill stage. Returns for 2024-25 and 2025-26 are also covered."
last_updated: 2026-11-05
depends_on:
  - nz-income-tax-ir3
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: income-tax
---

# New Zealand income tax (IR3): worked examples

Moved word for word from `nz-income-tax-ir3`. Load that skill first.

## Two worked examples that recompute

These are invented fixtures. Every result needs the inputs confirmed first. Rates come from the tables above.

### Example 1: self-employed consultant, 2025-26

A sole trader, GST-registered for the whole year, confirms net income of NZD 68,000 at Box 30 on GST-exclusive figures. That includes NZD 5,000 gross schedular income, with NZD 1,000 tax deducted shown on the Summary of Income. There are no losses, no imputation credits and no overseas tax. They met every section LC 13 condition for all 12 months, and paid NZD 4,800 provisional tax. The 2025-26 return is filed by 28 August 2026.

```oa-check
name: NZ 2025-26 self-employed RIT, balance and next-year standard method
inputs:
  net_income: 68000
  schedular_tax: 1000
  provisional_paid: 4800
  months: 12
steps:
  - taxable_income: max(net_income, 0)
  - tax: 8270.50 + (taxable_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - after_ietc: max(tax - ietc, 0)
  - rit: after_ietc - schedular_tax
  - balance: rit - provisional_paid
  - standard_2026_27: floor(rit * 1.05)
  - instalment: standard_2026_27 / 3
expected:
  tax: 12620.50
  ietc: 260
  rit: 11360.50
  balance: 6560.50
  standard_2026_27: 11928
  instalment: 3976
```

Decision: 2025-26 RIT is more than NZD 5,000, so section RC 3(3) does not remove a 2026-27 obligation and that RIT sets the standard amount. Whether provisional tax is payable for 2026-27 still turns on that year's RIT (section RC 3(1)(a)). The 105% limb applies because the return was not outstanding under an extension at the instalment date. Had the return still been outstanding at 28 August 2026 under an agent extension, the first instalment would use 110% of 2024-25 RIT, which is a Needs Input.

Same client, but entitled to and receiving WFF for 3 months. The condition fails for those months, so the credit falls to 9 months.

```oa-check
name: NZ 2025-26 IETC with 9 eligible months
inputs:
  net_income: 68000
  schedular_tax: 1000
  months: 9
steps:
  - tax: 8270.50 + (net_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - rit: max(tax - ietc, 0) - schedular_tax
expected:
  ietc: 195
  rit: 11425.50
```

Same client, entitled to WFF for those 3 months but not receiving it. From 30 March 2025 section LC 13(1)(d) fails only on entitlement and receipt together, so all 12 months count.

```oa-check
name: NZ 2025-26 IETC with WFF entitlement but no receipt
inputs:
  net_income: 68000
  schedular_tax: 1000
  months_entitled_and_receiving: 0
steps:
  - months: 12 - months_entitled_and_receiving
  - tax: 8270.50 + (net_income - 53500) * 0.30
  - abatement: 0.13 * max(floor(net_income) - 66000, 0)
  - ietc: max(520 - abatement, 0) * months / 12
  - rit: max(tax - ietc, 0) - schedular_tax
expected:
  months: 12
  ietc: 260
  rit: 11360.50
```

A separate refund case. Tax after the worksheet floors is NZD 1,000, refundable withholding at Box 21A is NZD 1,500 and provisional tax paid is NZD 200.

```oa-check
name: NZ RIT nil with excess credits kept for settlement
inputs:
  after_imputation: 1000
  credits: 1500
  provisional_paid: 200
steps:
  - rit: max(after_imputation - credits, 0)
  - excess_credits: max(credits - after_imputation, 0)
  - to_pay_or_refund: rit - excess_credits - provisional_paid
expected:
  rit: 0
  excess_credits: 500
  to_pay_or_refund: -700
```

Decision: RIT is nil, not NZD (500), so it adds nothing to the NZD 5,000 test or the standard amount. The refund is NZD 700, on the assumption that the NZD 1,500 is a credit within section LA 6(1).

A separate levy case, outside RIT. A self-employed person worked more than 30 hours a week in 2025-26 and earned NZD 35,000 in all, NZD 5,000 of it as an employee.

```oa-check
name: NZ 2025-26 earners' levy with and without purchased weekly compensation
inputs:
  employee_earnings: 5000
  agreed_annual_higher: 40000
  agreed_annual_lower: 20000
steps:
  - no_agreement: round(1.45 * (49365 - employee_earnings) / 100, 2)
  - agreement_higher: round(1.45 * (1.25 * agreed_annual_higher) / 100, 2)
  - agreement_lower: round(1.45 * (1.25 * agreed_annual_lower) / 100, 2)
expected:
  no_agreement: 643.29
  agreement_higher: 725.00
  agreement_lower: 362.50
```

Decision: with no agreement, regulation 6 gives NZD 643.29. With an agreement, regulation 7 replaces it, even where the result is lower, as at NZD 20,000 agreed.

A vehicle line and a receipt line from the same client. The vehicle is a petrol car doing 18,000 km with 60% business use from a logbook term, and actual vehicle costs are NZD 14,000. A bank credit of NZD 11,500 is tested in both GST cases.

```oa-check
name: NZ 2025-26 vehicle method comparison and GST both cases
inputs:
  total_km: 18000
  business_share: 0.6
  actual_costs: 14000
  receipt: 11500
steps:
  - tier_1_km: min(total_km, 14000)
  - tier_2_km: max(total_km - 14000, 0)
  - kilometre_method: tier_1_km * business_share * 1.20 + tier_2_km * business_share * 0.37
  - logbook_method: actual_costs * business_share
  - no_evidence_cap: actual_costs * min(business_share, 0.25)
  - receipt_gst_verified: receipt - receipt * 3 / 23
  - receipt_zero_rated: receipt
expected:
  kilometre_method: 10968
  logbook_method: 8400
  no_evidence_cap: 3500
  receipt_gst_verified: 10000
  receipt_zero_rated: 11500
```

Decision: the kilometre method gives the larger deduction here, but only if this is the election year for the vehicle under section DE 2B. Otherwise the person is on the costs method. Either election cannot be revoked and holds until the end of the income year of disposal. Under both methods the 60% comes from the logbook term. With no records, no logbook term and no kilometre election, the deduction is the lesser of actual use and 25%, so NZD 3,500 at most. With a kilometre election and no records or logbook term, the share is Needs Input. The receipt is NZD 10,000 only if GST at 15% is verified.

### Example 2: mixed salary and self-employed, 2024-25

An employee earned NZD 19,000 salary and NZD 31,000 net self-employed income, so net income is NZD 50,000 at Box 31 of the 2025 return. Total PAYE on payslips was NZD 2,574.12. Earners' levy at the 2024-25 rate is NZD 304.00. They met every LC 13 condition all year. No other credits apply.

```oa-check
name: NZ 2024-25 mixed income RIT with composite rates and IETC
inputs:
  salary: 19000
  self_employed: 31000
  total_paye: 2574.12
steps:
  - net_income: salary + self_employed
  - tax: 7345.12 + (net_income - 48000) * 0.2164
  - a_floored: max(520 - 0.13 * max(floor(net_income) - 44000, 0), 0)
  - a_printed: 520 - 0.13 * max(floor(net_income) - 44000, 0)
  - b: max(520 - 0.13 * max(floor(net_income) - 66000, 0), 0)
  - ietc_floored: round((a_floored * 121 + b * 244) / 365, 2)
  - ietc_printed: round((a_printed * 121 + b * 244) / 365, 2)
  - earners_levy: min(salary, 142283) * 0.016
  - tax_deducted: total_paye - earners_levy
  - rit_floored: tax - ietc_floored - tax_deducted
  - rit_printed: tax - ietc_printed - tax_deducted
  - levy_left_in_floored: tax - ietc_floored - total_paye
  - levy_left_in_printed: tax - ietc_printed - total_paye
  - standard_floored: floor(rit_floored * 1.05)
  - standard_printed: floor(rit_printed * 1.05)
expected:
  tax: 7777.92
  a_floored: 0
  a_printed: -260
  b: 520
  ietc_floored: 347.62
  ietc_printed: 261.42
  earners_levy: 304
  tax_deducted: 2270.12
  rit_floored: 5160.18
  rit_printed: 5246.38
  levy_left_in_floored: 4856.18
  levy_left_in_printed: 4942.38
  standard_floored: 5418
  standard_printed: 5508
```

Decision: show both figures, because the floor is held. RIT is NZD 5,160.18 floored and NZD 5,246.38 on the printed boxes, and both are more than NZD 5,000. Crediting total PAYE instead of tax deducted gives NZD 4,856.18 or NZD 4,942.38, the wrong answer on the threshold either way. The standard amount is NZD 5,418 or NZD 5,508. Whether provisional tax was payable for 2024-25 still turns on 2023-24 RIT (section RC 3(3)), which the file does not show.

Same client, but a WFF entitlement ended on 30 September 2024, so they are eligible from 1 October 2024: 6 whole months, or 182 days, all in the second period. WFF entitlement excluded April to September 2024 under the rule in force before 30 March 2025, whether received or not. October 2024 to March 2025 remains eligible.

```oa-check
name: NZ 2024-25 part-year IETC by statute and by worksheet
inputs:
  net_income: 50000
  days_second_period: 182
  eligible_months: 6
steps:
  - a_floored: max(520 - 0.13 * max(floor(net_income) - 44000, 0), 0)
  - a_printed: 520 - 0.13 * max(floor(net_income) - 44000, 0)
  - b: max(520 - 0.13 * max(floor(net_income) - 66000, 0), 0)
  - by_statute: round(b * days_second_period / 365, 2)
  - by_worksheet_floored: round((a_floored * 121 + b * 244) / 365 * eligible_months / 12, 2)
  - by_worksheet_printed: round((a_printed * 121 + b * 244) / 365 * eligible_months / 12, 2)
  - difference_floored: by_statute - by_worksheet_floored
  - difference_printed: by_statute - by_worksheet_printed
expected:
  by_statute: 259.29
  by_worksheet_floored: 173.81
  by_worksheet_printed: 130.71
  difference_floored: 85.48
  difference_printed: 128.58
```

Decision: show all 3 figures. Sections LC 14 and LC 15 use days, and that figure does not depend on the floor because a has no days here. The IR3G 2025 worksheet uses months, and its figure depends on the floor. Do not choose by default.

### Bank line fixtures

Layouts are carried from the prior version and untested. Each treatment assumes the conditions stated.

| Line | Case | Treatment |
| --- | --- | --- |
| `03/01/2025,,PAYMENT FROM ACME LTD,,11500.00,` (ANZ) | IT consultant | NZD 10,000 if registered and GST at 15% is verified; NZD 11,500 if not registered or the supply carried no GST |
| `10/08/2025,SHELL SELECT QUEENSTOWN,120.00,,` (Westpac) | Photographer, 8,400 of 14,000 km business, logbook term | NZD 72. With no records, no logbook term and no kilometre election: lesser of actual use and 25%, so NZD 30 at most, on a GST-exclusive basis if registered. With a kilometre election and no records or logbook term: Needs Input |
| `15/03/2025,SCHEDULAR PAYMENT BUILDCO LTD,-,4000.00,` (ASB) | Plumber | At a verified 20%: gross NZD 5,000, credit NZD 1,000. At a verified 15%: gross NZD 4,705.88, credit NZD 705.88. Rate unknown: Needs Input |
| `28/02/2025,TT,STRIPE PAYOUT,CODE,REF,2185.00,` (BNZ) | Marketing consultant | Gross up from the Stripe statement: the prior example's NZD 2,254 and NZD 69 are illustrative, GST-exclusive if registered |
| `20/05/2025,PAYPAL TRANSFER USD,,,1850.00,` (Kiwibank) | Freelance writer | Income is the NZD amount at the rate rule under Foreign currency, not the bank credit by default |
| `01/09/2025,,WINDCAVE SETTLEMENT,,8500.00,` (ANZ) | E-commerce seller, NZD 95,000 of annual supplies | NZD 7,391.30 if GST at 15% is verified. Red flag: verify registration under GST Act s 51 |

## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| Income Tax Act 2007 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/ | 2026-11-05 | Version as at 4 September 2026, read in part: sections and Schedules 1, 3 and 4 as cited, including sections DB 18AA, DE 2B to DE 12, EL 1 to EL 13 and RC 37 to RC 40 |
| Income Tax Act 2007, version as at 30 March 2025 | https://www.legislation.govt.nz/act/public/2007/97/en/2025-03-30/ | 2026-11-05 | Read in part: sections DH 1 to DH 8 and DH 10; section LC 13(1) |
| Income Tax Act 2007, version as at 30 June 2024 | https://www.legislation.govt.nz/act/public/2007/97/en/2024-06-30/ | 2026-11-05 | Read in part: section CB 6A; section LC 13(1) |
| Tax Administration Act 1994 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/ | 2026-11-05 | Version as at 1 October 2026, read in part: sections 22, 24F to 24H, 33, 37, 92A, 120A to 120L, 139A to 141K, 183A and 183F |
| Goods and Services Tax Act 1985 | https://www.legislation.govt.nz/act/public/1985/141/en/latest/ | 2026-11-05 | Read in part: sections 8, 19N, 20 and 51; section 19F not read |
| Accident Compensation Act 2001 | https://www.legislation.govt.nz/act/public/2001/49/en/latest/ | 2026-11-05 | Read in part: sections 168B, 208, 209, 211, 219, 220 and 222 |
| Taxation (Budget Measures) Act 2024 | https://www.legislation.govt.nz/act/public/2024/19/en/latest/ | 2026-11-05 | Read in part: sections 7 and 37 |
| Taxation (Annual Rates for 2023-24, Multinational Tax, and Remedial Matters) Act 2024 | https://www.legislation.govt.nz/act/public/2024/11/en/latest/ | 2026-11-05 | Read in part: sections 8, 47 and 48 |
| Taxation (Annual Rates for 2024-25, Emergency Response, and Remedial Measures) Act 2025 | https://www.legislation.govt.nz/act/public/2025/9/en/latest/ | 2026-11-05 | Read in part: sections 2(1), 3 and 105; section 5 through the ITA amendment note |
| Taxation (Annual Rates for 2025-26, Compliance Simplification, and Remedial Measures) Act 2026 | https://www.legislation.govt.nz/act/public/2026/8/en/latest/ | 2026-11-05 | Read in part: section 3; section 137 through the ITA amendment note |
| Taxation (Budget Measures) Act 2025 | https://www.legislation.govt.nz/act/public/2025/26/en/latest/ | 2026-11-05 | Subpart DI insertion, in part |
| Taxation (Budget Measures) Act 2026 | https://www.legislation.govt.nz/act/public/2026/25/en/latest/ | 2026-11-05 | Contents only, read for scope; no finding here rests on it |
| Accident Compensation (Earners' Levy) Regulations 2025 (SL 2025/18) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/ | 2026-11-05 | Read in full for regulations 4 to 9 |
| Accident Compensation (Work Account Levies) Regulations 2025 (SL 2025/17) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/17/en/latest/ | 2026-11-05 | Read in part: regulations 6, 7, 9 and 11 to 15 and the Schedules' layout |
| Accident Compensation (Work Account Levies) Amendment Regulations 2026 (SL 2026/30) | https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2026/30/en/latest/ | 2026-11-05 | Read in part for the rate schedules |
| Government Bill 344-1 | https://www.legislation.govt.nz/bill/government/2026/344/en/latest/ | 2026-11-05 | Read in part: clause 3, clauses 116 and 131 and the explanatory note |
| Parliament, bill page | https://www3.parliament.nz/en/pb/sc/committees-press-releases/taxation-annual-rates-for-2026-27-fbt-simplification-foreign-investment-funds-and-remedial-measures-bill/ | 2026-11-05 | Read for committee stage, the dissolution note and submissions |
| Inland Revenue, Tax rates for individuals | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | 2026-11-05 | Read in full for both rate tables |
| Inland Revenue, IR3G 2026 and IR3G 2025 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3g/ir3g-2026.pdf | 2026-11-05 | Read in part: questions cited, including Question 22 of the 2026 guide and Question 23 of the 2025 guide, by local extraction |
| Inland Revenue, IR3 2026 and 2025, IR3B, IR3R | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ir3/ir3-2026.pdf | 2026-11-05 | Read in part: box layout and the IR3B expense notes including Box 9, by local extraction |
| Inland Revenue, ACC earners' levy rates | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates | 2026-11-05 | Read in full for rates and maxima by year |
| Inland Revenue, Interest on overpayments and underpayments | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments | 2026-11-05 | Read in full for the rate table, the NZD 100 wording and deductibility |
| Inland Revenue, Kilometre rates 2025-2026 | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses/kilometre-rates-2025-2026 | 2026-11-05 | Read in full for rates; the 2024-2025 page likewise |
| Inland Revenue, schedular rate page | https://www.ird.govt.nz/income-tax/withholding-taxes/schedular-payments/getting-schedular-payments/work-out-and-declare-my-tax-rate-for-schedular-payments | 2026-11-05 | Read in full for chosen-rate limits |
| Inland Revenue, IETC page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc | 2026-11-05 | Read in part for income limits and the month rule |
| Inland Revenue, IR3 page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/what-happens-at-the-end-of-the-tax-year/individual-income-tax-return---ir3 | 2026-11-05 | Read in part for who files and the June note |
| Inland Revenue, IR3 in myIR | https://www.ird.govt.nz/myir-help/what-you-can-do/how-to-file-an-ir3-individual-income-tax-return-in-myir | 2026-11-05 | Read in part for the filing steps |
| Inland Revenue, provisional tax | https://www.ird.govt.nz/income-tax/provisional-tax | 2026-11-05 | Read in part for who pays |
| Inland Revenue, standard option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/standard-option | 2026-11-05 | Read in part for the default and the 105% wording |
| Inland Revenue, ratio option | https://www.ird.govt.nz/income-tax/provisional-tax/provisional-tax-options/ratio-option | 2026-11-05 | Read in part for the interest statement |
| Inland Revenue, interest on provisional tax | https://www.ird.govt.nz/income-tax/provisional-tax/interest-on-provisional-tax | 2026-11-05 | Read in part for the NZD 100 wording |
| Inland Revenue, first year in business | https://www.ird.govt.nz/income-tax/provisional-tax/paying-tax-in-your-first-year-in-business | 2026-11-05 | Read in part for the early payment discount and rates |
| Inland Revenue, home business page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/using-your-home-for-your-business | 2026-11-05 | Read in part for the formula and apportionment |
| Inland Revenue, vehicle page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/claiming-vehicle-expenses | 2026-11-05 | Read in part for methods and records |
| Inland Revenue, entertainment page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/entertainment-expenses | 2026-11-05 | Read in part for the 50% examples |
| Inland Revenue, meal page | https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/meal-expenses | 2026-11-05 | Read in part for meal rules |
| Inland Revenue, late filing penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties | 2026-11-05 | Read in part for the first charge |
| Inland Revenue, late payment penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties | 2026-11-05 | Read in part for the penalty steps |
| Inland Revenue, shortfall penalties | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/shortfall-penalties | 2026-11-05 | Read in part for section 141K as stated |
| Inland Revenue, currency conversion | https://www.ird.govt.nz/managing-my-tax/overseas-currency-conversion-to-nz-dollars | 2026-11-05 | Read in part for accepted rates |
| Inland Revenue, residency page | https://www.ird.govt.nz/international-tax/individuals/tax-residency-status-for-individuals | 2026-11-05 | Read in part for the day tests |
| Inland Revenue, overseas income page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/types-of-individual-income/overseas-income | 2026-11-05 | Read in part for worldwide income |
| Inland Revenue, rental income page | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it | 2026-11-05 | Read in part for reporting |
| Inland Revenue, rental deductions page | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-property-deductions | 2026-11-05 | Read in part for the basis and the exclusions |
| Inland Revenue, property interest rules | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions/property-interest-rules | 2026-11-05 | Read in part for the 2024-25 limit |
| Inland Revenue, how interest deductions are affected | https://www.ird.govt.nz/property/renting-out-residential-property/residential-rental-income-and-paying-tax-on-it/rental-expense-deductions/property-interest-rules/how-interest-deductions-are-affected | 2026-11-05 | Read in part for the 80% wording |
| Inland Revenue, bright-line test | https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test | 2026-11-05 | Read in part for the 2-year test |
| Inland Revenue, property sold before 1 July 2024 | https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/property-sold-before-1-july-2024 | 2026-11-05 | Read in part for the earlier periods |
| Inland Revenue, hobby page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/types-of-individual-income/hobbies-and-businesses/is-your-hobby-a-business | 2026-11-05 | Read in part for the hobby tests |
| Inland Revenue, self-employed or employee | https://www.ird.govt.nz/roles/employees/self-employed-or-employee | 2026-11-05 | Read in part for the employment tests |
| Inland Revenue, attribution page | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/how-income-is-taxed/attribution-rule-for-income-from-personal-services | 2026-11-05 | Read in part for the threshold |
| Inland Revenue, registering for GST | https://www.ird.govt.nz/gst/registering-for-gst | 2026-11-05 | Read in part for the threshold wording |
| Inland Revenue, square metre rate 2026 | https://www.ird.govt.nz/updates/news-folder/2026/square-metre-rate-for-home-office-calculations-2026 | 2026-11-05 | Read in full for the published rates |
| Inland Revenue, Provisional tax guide IR289 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir289/ir289.pdf | 2026-11-05 | Read in part for methods, interest and the early payment discount, by local extraction |
| Inland Revenue, Entertainment expenses guide IR268 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir268/ir268-2024.pdf | 2026-11-05 | Read in part for the 50% examples and records, by local extraction |
| Inland Revenue, Self-employed or an employee guide IR336 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir336/ir336-2020.pdf | 2026-11-05 | Read in part for the no single test wording, by local extraction |
| Inland Revenue, Bright-line property tax guide IR1229 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1229/bright-line-property-tax.pdf | 2026-11-05 | Read in part for the 2-year test, by local extraction |
| Operational Statement OS 19/03 | https://www.taxtechnical.ird.govt.nz/operational-statements/os-1903-square-metre-rate-for-the-dual-use-of-premises | 2026-11-05 | Read in full for the square metre rate method, with the PDF |
| Operational Statement OS 19/04a | https://www.taxtechnical.ird.govt.nz/operational-statements/os-1904-a-commissioner-s-statement-on-using-a-kilometre-rate-for-business-running-of-a-motor-vehicle | 2026-11-05 | Read in full for the kilometre method, with the PDF |
| OS 19/04 (KM 2026) Instrument | https://www.taxtechnical.ird.govt.nz/operational-statements/2026/os-19-04-km-2026 | 2026-11-05 | Read in full for the 2025-26 rates |
| OS 19/04 (KM 2025) | https://www.taxtechnical.ird.govt.nz/operational-statements/2025/os-19-04-km-2025 | 2026-11-05 | Read in full for the 2024-25 rates |
| Approval FX 21/01 | https://www.taxtechnical.ird.govt.nz/determinations/foreign-currency/approvals/fx-21-01 | 2026-11-05 | Read in full for approved sources and methods, with the PDF |
| ACC, Calculate your levies | https://www.acc.co.nz/for-business/received-an-invoice/calculate-your-levies | 2026-11-05 | Read in full by Firecrawl, because direct access was blocked, for the minimum and maximum table |
| ACC, CoverPlus invoice | https://www.acc.co.nz/for-business/received-an-invoice/explaining-your-invoice/coverplus-invoice | 2026-11-05 | Read in full by Firecrawl, because direct access was blocked, for the minimum and maximum table |

### Source conflicts

- **IETC 2024-25 part year.** ITA ss LC 14 and LC 15 use days ÷ 365. The IR3G 2025 worksheet and the prior version use months ÷ 12. Both are shown.
- **IETC 2024-25 floor.** Section LC 13(2) says 'positive amount'. Sections LC 14 and LC 15 set formulas under the heading 'Amount of credit formula: section LC 13(2)' and do not repeat 'positive'. The IR3G 2025 worksheet prints no floor at Boxes D and I, and the guide's NZD 48,000 wording fits a floor. At NZD 50,000 net income the credit is NZD 347.62 floored and NZD 261.42 on the printed boxes, and Example 2 RIT is NZD 5,160.18 or NZD 5,246.38. Both are shown and this file picks neither.
- **WFF condition wording.** ITA s LC 13(1)(d) and (e) have needed entitlement and receipt together since 30 March 2025, and Inland Revenue's IETC page says the same. IR3G 2026 still says 'not entitled'. This file follows the Act.
- **RIT as a credit.** ITA s YA 1 makes RIT the positive amount, if any. IR3G 2026 calls Box 14 'your residual income tax' and lets it be a credit. This file treats RIT as nil and carries the excess separately; the refund is the same. The YA 1 list names no section LS credit, but the worksheet subtracts overpaid PIE tax at Box 11. This file follows the worksheet there, and a reviewer confirms RIT where Box 35C decides the NZD 5,000 threshold.
- **Kilometre election with no share evidence.** ITA s DE 4(1)(c) takes a person who elected the kilometre rate method out of section DE 4, and section DE 12(3)(c) takes the business proportion from sections DE 5 to DE 11, so the Act gives no figure for a person with no records or logbook term. OS 19/04a, paragraph 20, says section DE 4(2) limits deductions to a maximum of 25% in the absence of a logbook or actual records, if that percentage can be justified. This file treats the share as Needs Input, never goes above 25% and leaves the amount to the reviewer.
- **Early payment discount application date.** ITA s RC 38(1)(d) says on or before the last date for filing under TAA s 37(5). Inland Revenue's first year page and IR289 say the date the return has to be filed. IR3G 2026 says by 31 March of the following year. This file follows the Act.
- **Initial provisional tax wording.** ITA s YA 1 requires that in the tax year the person stopped deriving income from employment and then started to derive income from a taxable activity. IR3G 2026 omits the employment limb and IR289 includes it. This file follows the Act.
- **Reassessment interest.** ITA s EF 5(1) allocates deductible interest to the income year in which it is paid. Inland Revenue's interest page says interest on a reassessment is deductible only in the income year after the year of reassessment. This file follows the Act.
- **IR3G 2026 agent date.** Page 7 prints 'until 31 March 2026' for the 2026 return. TAA s 37 gives 31 March 2027. This file follows the Act.
- **GST threshold wording.** GST Act s 51 says 'has exceeded' or 'will exceed'. Inland Revenue says 'at least NZD 60,000'. This file follows the Act.
- **Interest minimum.** TAA s 183F(1)(b) and (d) say NZD 100 or less, as do IR289 and the provisional tax interest page. Inland Revenue's main interest page says 'amounts under NZD 100'. This file follows the Act.
- **Attribution threshold.** ITA s GB 27(2)(c) reads NZD 78,100. Inland Revenue's page, updated 18 March 2021, reads NZD 70,000. This file does not apply the rule; the Act is the higher source.
- **Sibling guides.** `nz-acc-levies` calls both the earners' and work levies deductible (section 6.2) and this file holds the earners' levy. It shows Working Safer at about NZD 0.08 with no primary source here. It labels tax year 2025 as 1 April 2025 to 31 March 2026, the opposite of the prior version of this file. `nz-provisional-tax` says AIM is 'under' NZD 5,000,000; the Act says 'NZD 5,000,000 or less'. `nz-provisional-tax` also ties the standard route's interest position to on-time payment, which TAA s 120KE does not, and states a first-year exemption more widely than the initial provisional tax definition. `nz-acc-levies` levies a person below the minimum on the minimum, with no employee earnings offset (SL 2025/18 reg 6). `nz-tax-residency` says '183 days or more'; ITA s YD 1(3) says 'more than 183 days'. `nz-gst-return` reuses code R-NZ-1 and states the threshold as 'NZD 60,000 taxable supplies in any 12-month period'; `new-zealand-gst` does too. Rates in `new-zealand-crypto-tax` match this file. The bright-line text in `nz-capital-gains` matches section CB 6A.

### Other legacy topics

- **Company income.** Only salary and dividends from the company appear in an IR3. Structure first: R-NZ-2. Shareholder-employee salary with no PAYE is at Question 20.
- **Attribution.** ITA s GB 27 can attribute personal services income to a person. Reviewer. See the conflict above.
- **Working for Families.** Calculations are out of this file. The IETC interaction is under Independent earner tax credit.
- **Tier 2 cases.** Hobby or business, employee or self-employed: Inland Revenue says no single test decides (IR336), and a person can be both. Reviewer.
- **Known gaps.** Company income tax; non-resident income and NRWT; bright-line gain computation; Working for Families calculations; GST return computation; KiwiSaver employer contribution calculations.
- **Excluded jurisdictions.** The prior version names no fixed excluded jurisdiction.

Not yet confirmed: the annual taxing Act for 2026-27 (Government Bill 344-1 only, and its commentary was not read); 2026-27 kilometre and square metre rates; the Working Safer levy rate and instrument (NZD 0.08 per NZD 100 in the prior version, not read in a primary source); whether a self-employed person's earners' levy is deductible; whether each 2024-25 IETC period credit is floored at nil, and the 2024-25 part-year route; the amount for a client with a kilometre election and no share evidence; ACC Levy Guidebook 2026-27 (blocked at source); classification unit rates in the guidebook; the training expense rule; the statutory source for the next working day practice; bank formats and narrations, untested.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | November 2026 | Converted to the upstream template. Primary-source check. Corrected penalties, the IETC basis, the GST test, the schedular default, entertainment, vehicle cap, home office, rental, filing dates and the PAYE credit. Added refusals, an operational hold, Bill and enactment standing, and evidence files. Repaired after an independent check: vehicle evidence, the residential deduction basis, the IETC floor held, and the instruments read |
| 2.1 | November 2026 | ACC levy rates and caps by year (2025-26 and 2026-27); ACC earner levy removed from RIT and the computation flow |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; NZ bank formats (ANZ, BNZ, ASB, Westpac, Kiwibank); transaction pattern library; Windcave/PayNow patterns; worked examples; prohibitions and disclaimer added |
| 1.0 | 2025 | Initial version |
