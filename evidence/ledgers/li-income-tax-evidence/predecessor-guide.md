---
name: li-income-tax
description: >
  Prepare 2026 Liechtenstein individual wealth-and-income tax workpapers. Use for
  ordinary resident taxation, family-status tariff selection, deemed wealth yield,
  the separate minimum-income exemption, state tax, municipality surcharge, business loss screening and
  reconciliation of payroll withholding. Establish residence, family/election facts,
  taxable net wealth, income categories, deductions and the municipality's actual
  annual rate before computing. The Guide replaces approximate summary brackets
  with the statutory formulas and separates the tariff allowance from deductible
  expenses. It does not complete asset valuations, all deductions, lump-sum pension
  taxation, trusts, expenditure taxation, treaties, exact filing calendars or live
  filing, and remains pending local accountant review.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.2
---

# Liechtenstein individual income and wealth tax v0.2

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Who this applies to

SteG article 6 makes individuals with domestic domicile or habitual abode subject to unlimited wealth/income taxation, subject to the specific exceptions and relief rules. Foreign residents have the specified domestic wealth/income categories; article 7 controls start/end dates. This ordinary-resident 2026 workpaper is not a residence/treaty or special-regime determination. Current source is the [Tax Act consolidated 1 July 2026][law]; selected provisions and read limits are below.

## Establish the tax unit, income and wealth bases

1. Establish family status, children, residence periods and the applicable assessment route. Article 8 ordinarily combines spouses/registered partners living in an unseparated relationship; its separate-assessment election and child-income rules are distinct. SteV article 6 requires the joint written separate-assessment application/withdrawal by 31 December of the relevant year and at least five years' separate assessment. Do not select the joint tariff merely from one person's marital label. [SteG, articles 8 and 18][law]; [SteV, article 6][ordinance]
2. Reconcile assets, values and liabilities. Article 9 addresses taxable wealth; articles 10–12 contain exclusions, debt allocation and valuation rules. Foreign property/PE and partly domestic wealth need the actual allocation rules. A negative wealth base or deduction for every worldwide debt is not assumed. Trusts, foundations, valuation disputes and substitute wealth taxation remain specialist cases.
3. For ordinary taxable net wealth, apply the 4% Sollertrag under articles 5 and 14(2)(l), then include that deemed yield in taxable income. Article 15(1) prevents separately taxing actual returns on wealth already subjected to that wealth-tax mechanism. Do not add the same taxed asset's interest/dividend again solely because it appears in a bank statement. The 4% figure is now statutory for 2026, not an annual Finance Act assumption. [SteG, articles 5 and 14–15][law]; [Act 2024/483, commencement II(2)][amendment]
4. Reconcile employment, self-employment, property, pensions and other receipts under articles 14–16, with their exclusions and actual deduction conditions. Article 15's private-asset gain exclusions do not decide a business-asset or separate property-gain case. Article 16 governs expenses, losses and personal deductions. The table allowance below is embedded in the formula; it must not be deducted a second time from the input base.
5. Retain the final established taxable income **x**, including the applicable deemed wealth yield, before selecting the state formula. Articles 18, 21 and 22 contain part-year/special-income/foreign-relief rules; do not apply the simple full-year examples indiscriminately.

## 2026 state formulas

Before using the tariff, screen the separate **Existenzminimum exemption** in SteG article 15(2)(i). For an unlimited-liability resident, article 14 income that does not exceed the applicable minimum is exempt. If only part of the income is domestically taxable, test total income; for liability lasting less than a year, annualise that total. This test is not a further deduction from taxable income and is distinct from the zero band and fixed tariff subtraction. [SteG, articles 15(2)(i) and 19][law]

SteV article 8 sets these monthly gross minima, with the amended base amounts first applying to tax year 2025 and continuing in the current 2026 text:

| Established category | CHF per month | CHF for a full twelve months |
|---|---:|---:|
| Single | 2,100 | 25,200 |
| Qualifying single parent | 2,600 | 31,200 |
| Jointly assessed spouses/registered partners | 3,200 | 38,400 |
| Separately assessed spouses/registered partners in the same household, or factual cohabiting partners | 1,600 each | 19,200 each |
| Each child aged up to 5, additional | 300 | 3,600 |
| Each child aged 6–11, additional | 450 | 5,400 |
| Each child aged 12 or older, additional | 600 | 7,200 |

Establish the actual family/child category, article 14 total income including relevant deemed wealth yield, and liability period before deciding eligibility. Resolve changing family circumstances or disputed attribution separately; do not replace this gross-income test with post-deduction taxable income **x**. [SteV, article 8 and its amendment notes][ordinance]

For income not exempt under that screen, the following reproduces article 19(1). Values are CHF taxable income **x**, not gross salary. “Subtract” is the fixed amount in the statutory formula, not another itemised deduction. The tariff's basic allowance is embedded in its zero band and formula. Qualifying single-parent status is the statutory family-law category, not any adult living alone with a child. Special capital/substitute wealth taxation has different rules.

### Ordinary tariff, article 19(1)(a)

| Taxable income x | State tax |
|---|---|
| Up to 15,855 | 0 |
| 15,856–21,140 | 1% × x − 159 |
| 21,141–42,280 | 3% × x − 581 |
| 42,281–73,990 | 4% × x − 1,004 |
| 73,991–105,700 | 5% × x − 1,744 |
| 105,701–137,410 | 6% × x − 2,801 |
| 137,411–169,120 | 6.5% × x − 3,488 |
| 169,121–211,400 | 7% × x − 4,334 |
| 211,401 or more | 8% × x − 6,448 |

### Qualifying single parent, article 19(1)(b)

| Taxable income x | State tax |
|---|---|
| Up to 23,783 | 0 |
| 23,784–31,710 | 1% × x − 238 |
| 31,711–63,420 | 3% × x − 872 |
| 63,421–110,985 | 4% × x − 1,506 |
| 110,986–158,550 | 5% × x − 2,616 |
| 158,551–206,115 | 6% × x − 4,202 |
| 206,116–253,680 | 6.5% × x − 5,232 |
| 253,681–317,100 | 7% × x − 6,501 |
| 317,101 or more | 8% × x − 9,672 |

### Joint spouses, article 19(1)(c)

| Combined taxable income x | State tax |
|---|---|
| Up to 31,710 | 0 |
| 31,711–42,280 | 1% × x − 317 |
| 42,281–84,560 | 3% × x − 1,163 |
| 84,561–147,980 | 4% × x − 2,008 |
| 147,981–211,400 | 5% × x − 3,488 |
| 211,401–274,820 | 6% × x − 5,602 |
| 274,821–338,240 | 6.5% × x − 6,976 |
| 338,241–422,800 | 7% × x − 8,667 |
| 422,801 or more | 8% × x − 12,895 |

Source for every threshold/rate/subtraction: [SteG, article 19][law]. Exact rounding/input treatment and special assessments still need the current return instructions; do not interpolate across the printed whole-franc band endpoints.

## Municipality, business losses and payroll credits

Article 75 sets the municipality surcharge as a percentage **of state tax**, fixed annually by the municipality, legally between 150% and 250%. This is not 150%–250% of taxable income. Obtain the actual municipality/year rate; the earlier 150%–180% headline is not a statutory limit or verified 2026 municipality list. Article 75(2) excludes an added surcharge on source withholding under article 25. Do not add a municipality percentage to the wage-tax deduction itself. [SteG, article 75][law]

For an ordinary assessment with a verified surcharge m:

    municipality tax = state tax × m
    combined tax before credits = state tax + municipality tax

For business losses under article 16(2)(b)(3), assess prior unused loss evidence and the ordinary 70% current-taxable-income cap; the year of definitive business cessation has a separate exception. A multiplication using an assumed loss register is not proof of entitlement. Corporate modified-equity deduction rules must not simply be imported into a personal computation. [SteG, article 16][law]

Resident wages also have payroll withholding; use [li-payroll-social](li-payroll-social.md) for its distinct base and instructions. Article 29 credits withholding in an ordinary assessment and addresses excess amounts. Preserve wage certificates and all prepayments, relief and final assessment data before deciding a balance/refund; a payroll percentage is not the final state/municipality tariff. [SteG, articles 24–29][law]

## Filing, payment and sanctions

Article 94 requires truthful, complete, signed filing even without a personal form/notice. Confirm the municipality/authority's allocated 2027 due date for 2026 income; the earlier approximate April headline is not used as a verified deadline. Obtain the current return and deduction/election instructions and supporting account, asset, family and foreign-income evidence.

Article 114 generally requires payment within 30 days of legal maturity, subject to its exceptions; the actual assessment/delivery and special-departure facts matter. SteV article 45 sets late interest at 4%, while the precise start/base and actual notice must be established. Article 135's procedural fines require its post-reminder intentional/negligent breach, with ordinary CHF 1,000 and serious/repeat CHF 10,000 maxima. These are not automatic filing charges. Exact extension, interest and appeals/correction procedures remain incomplete. [SteG, articles 94, 113–114 and 135][law]; [SteV, article 45][ordinance]

## Worked controls

Amounts, deduction entitlement, wealth values and municipality rates are case assumptions. All examples exclude special incomes, foreign relief and rounding differences.

### Minimum-income exemption screen

Assume an unlimited-liability single resident for the full year, no child addition and CHF 24,000 total article 14 income after including every relevant source and deemed wealth yield. The CHF 25,200 annual minimum exceeds that established total by CHF 1,200. Article 15(2)(i) therefore exempts this income; do not compute a positive tariff liability merely because a post-deduction figure falls above the zero band. The arithmetic below checks the threshold and headroom; statutory eligibility is an express case assumption.

```oa-check
name: Liechtenstein assumed full-year single minimum-income screen
inputs:
  statutory_monthly_gross_minimum: 2100
  months_in_full_year: 12
  established_total_article_14_income: 24000
steps:
  annual_gross_minimum: statutory_monthly_gross_minimum * months_in_full_year
  income_below_minimum: annual_gross_minimum - established_total_article_14_income
expected:
  annual_gross_minimum: 25200
  income_below_minimum: 1200
```

### Ordinary state tax with deemed wealth income

Assume a full-year ordinary-tariff resident, CHF 80,000 established income after all relevant adjustments other than wealth yield, and CHF 500,000 established taxable net wealth. The 4% yield gives CHF 20,000, so x is CHF 100,000 and state tax CHF 3,256. Assume an independently verified case-only municipality surcharge of 150%; combined tax before credits is CHF 8,140.

```oa-check
name: Liechtenstein assumed ordinary tax with deemed wealth yield
inputs:
  established_other_taxable_income: 80000
  established_taxable_net_wealth: 500000
  statutory_yield: 0.04
  selected_state_rate: 0.05
  selected_fixed_subtraction: 1744
  assumed_verified_municipality_surcharge: 1.50
steps:
  deemed_wealth_income: established_taxable_net_wealth * statutory_yield
  combined_taxable_income: established_other_taxable_income + deemed_wealth_income
  state_tax: combined_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  deemed_wealth_income: 20000
  combined_taxable_income: 100000
  state_tax: 3256
  municipality_tax: 4884
  combined_tax_before_credits: 8140
```

### Joint state formula and surcharge

Assume established joint assessment, CHF 200,000 combined taxable income including wealth yield and a verified case-only 180% municipality surcharge. This is not a statement of a particular municipality's actual rate.

```oa-check
name: Liechtenstein assumed joint state formula and municipality tax
inputs:
  established_joint_taxable_income: 200000
  selected_state_rate: 0.05
  selected_fixed_subtraction: 3488
  assumed_verified_municipality_surcharge: 1.80
steps:
  state_tax: established_joint_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  state_tax: 6512
  municipality_tax: 11721.60
  combined_tax_before_credits: 18233.60
```

### Qualifying single-parent formula

Assume established statutory eligibility, CHF 150,000 final taxable income and a case-only 200% municipality surcharge. Do not infer eligibility from this calculation.

```oa-check
name: Liechtenstein assumed qualifying single parent formula
inputs:
  established_taxable_income: 150000
  selected_state_rate: 0.05
  selected_fixed_subtraction: 2616
  assumed_verified_municipality_surcharge: 2
steps:
  state_tax: established_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  state_tax: 4884
  municipality_tax: 9768
  combined_tax_before_credits: 14652
```

### Assumed ordinary business-loss cap

Assume CHF 100,000 relevant positive business income, CHF 90,000 established unused prior losses and no definitive cessation or other special case. Ordinary loss use is CHF 70,000 and CHF 20,000 losses remain. This is not the complete taxable-income calculation.

```oa-check
name: Liechtenstein assumed ordinary individual business loss cap
inputs:
  established_relevant_positive_income: 100000
  established_opening_unused_losses: 90000
  statutory_use_fraction: 0.70
steps:
  ordinary_loss_limit: established_relevant_positive_income * statutory_use_fraction
  losses_used: min(established_opening_unused_losses, ordinary_loss_limit)
  relevant_income_after_loss: established_relevant_positive_income - losses_used
  losses_remaining: established_opening_unused_losses - losses_used
expected:
  ordinary_loss_limit: 70000
  losses_used: 70000
  relevant_income_after_loss: 30000
  losses_remaining: 20000
```

## Ask and refer

Obtain residence/family/election facts, the municipality/year rate, all assets/debts and values, income and benefits, assessed losses, actual deductions, foreign taxes and withholding/prepayment certificates. Refer partial-year migration, foreign relief, special pension/capital receipts, foundations/trusts, expenditure taxation, wealth substitutions, business disposals and contested classifications. All deductions/valuation methods, actual annual calendar, specialist law and named accountant review remain open; IT-IND coverage stays partial.

## Sources

Read 24 October 2026, selected provisions only:

- [SteG, consolidated 1 July 2026][law], articles 5–8, selected 9–16, 18–19, 24–29, 75, 94, 113–114 and 135. The full asset/deduction/foreign-relief/special-regime chain has not been audited.
- [SteV, consolidated 1 July 2026][ordinance], article 6 election, article 8 minimum-income exemption and article 45 interest; full current return/election procedures remain to be reconciled.
- [Act 2024/483][amendment], article 5 and commencement II(2); its article 19 schedule was compared with the current consolidation, not assumed from the prior approximate summary.

[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[amendment]: https://www.gesetze.li/chrono/pdf/2024483000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
