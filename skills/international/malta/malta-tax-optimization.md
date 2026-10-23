---
name: malta-tax-optimization
description: "Use this skill when asked how a self-employed individual or small business owner in Malta can lawfully reduce or time income tax for basis year 2026 (year of assessment 2027). Covers the 10% part-time final tax and its EUR 12,000 cap, joint and parent rate tables, the sole trader or company choice (35% with shareholder refunds, the elective 15% final tax), deductions people miss (article 14 test, home for the elderly fees, the car cost cap), wear and tear timing, losses, provisional tax, VAT registration choice, pension tax credits, and the anti-avoidance rule in article 51. Trigger on: reduce tax Malta, tax planning Malta, save tax Malta, pay less tax Malta, deductions I'm missing, part-time 10% Malta, incorporate in Malta, pension tax credit Malta. Links the computation skills instead of repeating them."
version: 1.1
jurisdiction: MT
tax_year: 2026
last_updated: 2026-10-23
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Tax Optimization

## Malta Tax Optimization: Self-Employed Skill v1.1

Built by Michael Cutajar and the OpenAccountants team. **Source-cited draft: not reviewed by an accountant.**

Tax year 2026: basis year 2026, year of assessment 2027. This skill lists the lawful levers and points to the skill that computes each one. It does not repeat the rate tables or the computations:

- individual rates, residence, part-time and rental final taxes: `malta-income-tax`
- provisional tax: `mt-estimated-tax`
- companies, refunds and the 15% election: `mt-corporate-tax`
- rent: `mt-rental-income`; property and share gains: `mt-capital-gains`, `selling-a-company-in-malta`
- related-party pricing: `malta-transfer-pricing`; moving to Malta: `moving-to-malta-tax-residence`
- VAT: `malta-vat-return`; social security: `malta-ssc`

## Section 1: Quick Reference

| Field | Value | Source |
| --- | --- | --- |
| Country | Malta | |
| Tax year | Calendar basis year 2026, assessed in year of assessment 2027 | Income Tax Act, Cap. 123 |
| Individual return due | 30 June 2027 for basis year 2026 | S.L. 372.16 rule 2(c)(ii) |
| Top individual rate | 35% above EUR 60,000 (all resident tables) | Cap. 123 art. 56(1), as replaced by Act III of 2026 |
| Single table, basis year 2026 | 0% to EUR 12,000; 15% to EUR 16,000; 25% to EUR 60,000; 35% above | Cap. 123 art. 56(1)(b)(i) |
| Married joint table (no qualifying child), basis year 2026 | 0% to EUR 15,000; 15% to EUR 23,000; 25% to EUR 60,000; 35% above | Cap. 123 art. 56(1)(a)(i) |
| Part-time final tax | 10% on part-time self-employed profit up to EUR 12,000 | Cap. 123 art. 90A; S.L. 123.39 rule 3(2) |
| Company rate | 35%; six-sevenths refund to shareholders on Malta trading profit in most cases | Cap. 123 art. 56(6); Cap. 372 art. 48(4A) |
| Anti-avoidance | Article 51: artificial or fictitious schemes are disregarded; schemes whose sole or main purpose is a tax advantage can be nullified by order | Cap. 123 art. 51 |
| Interest on late tax | 0.6% a month or part month, capped at the tax | Cap. 372 art. 44(2A) |

The full rate tables, including the four new child tables for 2026, are in `malta-income-tax`. Every rate above is from that skill's sources and from the Acts read on 2026-10-23.

## Section 2: Income Splitting and Structuring

### The part-time 10% final tax (article 90A, S.L. 123.39)

| Point | Rule | Source |
| --- | --- | --- |
| Who | A Malta resident in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice. A spouse living with a qualifying spouse is included. | S.L. 123.39 rule 2; art. 90A(9) |
| Rate and cap | 10% final tax on part-time self-employed profit up to EUR 12,000. Profit above EUR 12,000 goes into the return at normal rates. | art. 90A(11); rule 3(2) |
| Conditions | Part-time work registered with Jobsplus; at most two part-time employees; proper books; work for someone other than the full-time employer; VAT registration unless not required or exempt. | rule 4 |
| Payment | By 30 April after the basis year (30 April 2027 for 2026 profit), with a statement of accounts | Cap. 372 art. 42(4)(a) |
| Risk | If the tax is not paid on time and the Commissioner sends a notice, all the part-time income is taxed at normal rates. The Commissioner can refuse the regime where the work is the person's normal activity. | art. 90A(8), (10) |

Planning point: profit above EUR 12,000 is not lost, it is taxed at the person's normal marginal rate. Timing of invoices only helps if the business genuinely reports on an accruals basis and the work is genuinely done in the later year. Do not move income artificially (article 51).

### Rate tables and family status (article 56)

- Married couples are taxed jointly by default under article 49. They may elect separate returns (article 49A), or the responsible spouse may opt for a separate computation (article 50), in which case each spouse uses the single or parent tables. Compare both before filing; `malta-income-tax` has the tables.
- For basis year 2026 the married and parent tables with qualifying children give wider 0% bands (for example EUR 22,500 for a married couple with two or more qualifying children). Each table has conditions on custody, age and nationality. Check every condition before relying on a table.

### Employing a family member

A salary to a spouse or child is deductible only if it meets the article 14(1) test (wholly and exclusively incurred in producing the income) and is not barred by article 26. Rule 4(1) of the Income Tax (Deductions) Rules, S.L. 123.07, limits the deduction for emoluments to emoluments "duly accounted for", meaning run through FSS payroll. The work must be real, the pay must match the work, and the employment must be registered. See `malta-payroll`.

### Sole trader or company

| Factor | Sole trader | Private limited company |
| --- | --- | --- |
| Rate on profit | 0% to 35% on the individual tables | 35% at company level |
| Profit paid out as dividend | Not applicable | Shareholder registered for refunds can claim six-sevenths of the tax on Malta trading profit, leaving 5% Malta tax overall (Cap. 372 art. 48(4A)(a)) |
| Profit kept in the company | Taxed in the year earned | 35% until a dividend triggers a refund claim |
| Elective 15% final tax | Not available | Available from basis year 2026 under S.L. 123.217; binds for five years of assessment; no refund; floor rules apply |
| Compliance | Return and provisional tax | Annual accounts (audit unless micro-exempt), company return through a tax practitioner, annual return at MBR |

The refund route, the 15% election and the Malta-resident individual shareholder rules (article 43(6) and article 12(1)(c)(iii)) are worked through in `mt-corporate-tax`. Formation steps and costs: `malta-formation`. Accounts and audit: `malta-financial-statements`.

## Section 3: Deductions Most People Miss

Every deduction below must pass article 14(1) ("wholly and exclusively incurred in the production of the income") and must not be barred by article 26 (private or domestic spending, capital spending, recoverable amounts, voluntary payments). Mixed-use items are apportioned. Default to 0% business use until the client documents it.

| Deduction | Rule | Source |
| --- | --- | --- |
| Home office share | Business share of rent, utilities and internet for a room used for the business. A room also used privately fails the "wholly and exclusively" test on the private share. | Cap. 123 art. 14(1), 26 |
| Professional subscriptions, training, bank and payment fees, professional indemnity insurance, software subscriptions | Deductible when incurred in producing the income | Cap. 123 art. 14(1) |
| Bad debts | Deductible when proved to the Commissioner to have become bad in the year; a general provision is not | Cap. 123 art. 14(1)(d) |
| Scientific research | Deductible under article 14(1)(h); capital research spending is spread over six years | Cap. 123 art. 14(1)(h) |
| Research, development and innovation at 175% | In the Act (article 14(1)(ha), Act III of 2026), marked applicable from year of assessment 2027, but it only starts on a date the Minister sets by Gazette notice, with rules to define the activities. Do not claim it until the notice and rules exist. | Cap. 123 art. 14(1)(ha) |
| Fees for a private home for the elderly or disabled, or a respite centre | Lower of the amount paid and EUR 4,500, from year of assessment 2027 (basis year 2026). The home must report the payment to MTCA. | Cap. 123 art. 14D |
| Car cost cap | For a car costing more than EUR 14,000, wear and tear is computed as if it cost EUR 14,000. Lease payments on a car listed above EUR 14,000 are cut in the same ratio. | S.L. 123.07 rule 3 |

Entertainment: the Income Tax Act has no specific rule. Treat client entertainment as private unless the article 14(1) test is clearly met, and flag it.

Social security Class 2: the Income Tax Act contains no deduction for social security contributions. `malta-income-tax` treats Class 2 as a memo item. Confirm on the current MTCA return before claiming it.

## Section 4: Capital Allowances (Wear and Tear)

**Legislation:** Cap. 123 art. 14(1)(f); Deduction for Wear and Tear of Plant and Machinery Rules, S.L. 123.01.

### Timing of purchases

Rule 7(a) of S.L. 123.01: an asset acquired on any day other than the first day of the year is treated "as if the asset had been used for the whole year". Rule 7(b): no allowance in the year of sale or scrapping. So an asset bought and in use by 31 December 2026 gets a full year's allowance in basis year 2026. The purchase must be genuine and the asset in business use.

### Minimum years (S.L. 123.01 Schedule, straight line on cost)

| Asset | Minimum years | Maximum annual rate |
| --- | --- | --- |
| Computers and electronic equipment; computer software | 4 | 25% |
| Motor vehicles; other machinery | 5 | 20% |
| Catering equipment; air-conditioners; medical equipment; communication and broadcasting equipment | 6 | about 16.67% |
| Furniture, fixtures, fittings and soft furnishings; lifts; other plant | 10 | 10% |
| Electrical and plumbing installations and sanitary fittings | 15 | about 6.67% |

Industrial buildings and structures: at most 2% of cost a year, plus an initial deduction of 10% in the year first used (Cap. 123 art. 14(1)(j)).

Allowances are only given where proper records of cost are kept (rule 5) and are cut to the business-use share (rule 11). S.L. 123.01 has no de minimis amount for writing off small items in one year.

### Asset disposal

A sale or scrapping triggers a balancing statement under article 24: proceeds above the written-down value are a balancing charge; below it, a balancing allowance.

## Section 5: Loss Utilization

**Legislation:** Cap. 123 art. 14(1)(g).

| Point | Rule |
| --- | --- |
| Same year | A trading loss is set against other income and capital gains of the same year |
| Carry-forward | What is left is carried forward against later years' total income in succession, with no time limit |
| Carry-back | None |
| Final tax income | A loss cannot be set against income going to the final tax account |
| Group relief | Companies only: see `mt-corporate-tax` |

Losses must come from genuine commercial activity. A manufactured loss is open to article 51.

## Section 6: Timing Strategies

| Strategy | Detail | Source |
| --- | --- | --- |
| Asset purchase before year end | Full year's wear and tear in the year of acquisition | S.L. 123.01 rule 7(a) |
| Provisional tax reduction | If 2026 tax will be lower than the benchmark, file the P.T. reduction form and pay less | S.L. 372.18 rule 10 |
| Pay provisional tax on time | 20% by 30 April, 30% by 31 August, 50% by 21 December 2026. Late instalments carry additional tax of 0.6% a month or part month | S.L. 372.18 rules 4, 5, 14 |
| Part-time cap | Keep part-time records clean so profit up to EUR 12,000 stays at 10% | S.L. 123.39 rule 3(2) |
| Pension contributions before 31 December | The tax credit is given only for contributions paid in the basis year and cannot be carried forward | Cap. 123 art. 57(3) |

Detail on provisional tax: `mt-estimated-tax`.

## Section 7: VAT Choice

| Strategy | Detail | Source |
| --- | --- | --- |
| Article 11 small enterprise | Available where turnover in the preceding calendar year was not more than EUR 35,000. Charges no VAT and recovers none. Suits sales to consumers or VAT-exempt customers. | VAT Act, Cap. 406, art. 11 |
| Article 10 registration | Charges 18% and recovers input VAT. Suits B2B sales (customers recover the VAT) or high-input businesses. | Cap. 406 art. 10 |
| Capital goods | Equipment, tools and office furniture at EUR 1,160 or more, and all immovable property, are capital goods: input VAT is adjusted over 5 or 20 years if use changes | S.L. 406.12 |

Registration rules, deadlines and the EUR 100,000 Union threshold are in `malta-vat-return`.

## Section 8: Social Security

Class 2 is charged under the Social Security Act, Cap. 318, on the previous year's net earnings, at 15% in the middle band with a weekly minimum and maximum. The 2026 weekly amounts were not found in the law on legislation.mt; take them from MTCA's 2026 table. See `malta-ssc` before quoting a figure.

Planning points:

- A full-time employee with part-time self-employment pays Class 1 through the employer; check the Class 2 position on mtca.gov.mt (`malta-ssc`).
- Class 2 above the maximum adds nothing. Below the band the flat minimum applies.

## Section 9: Investment and Retirement

| Relief | Rule | Source |
| --- | --- | --- |
| Personal retirement scheme tax credit | 25% of qualifying contributions, up to EUR 750 a year. Each spouse may claim. Not carried forward. | MTCA tax return booklet 2026 (basis year 2025); Cap. 123 art. 57 |
| Voluntary occupational pension scheme | 25% of the employee's qualifying contributions, up to EUR 750 a year | MTCA tax return booklet 2026; S.L. 123.175 |
| Pension income exemption, age 61 and over | Basis year 2026: 100% of pension income under art. 4(1)(d), up to EUR 37,104. Basis year 2025: 80%, up to EUR 13,309 | Pensions (Tax Exemption) Rules, S.L. 123.204 rule 3 (L.N. 53 of 2026) |
| Pensioner rebate | From year of assessment 2027, a pensioner using the exemption and taxed on the married table gets a rebate of (chargeable income less 15,000) × 15%, capped at EUR 540 | S.L. 123.204 rule 4 |

Article 57 of the Act states 15% and EUR 150 "or such other amount as may be prescribed". The 25% and EUR 750 figures are from MTCA's booklet for basis year 2025. Confirm the 2026 figures before quoting them.

Malta Enterprise runs grant and tax-credit schemes for small businesses (for example Micro Invest). Their rates and caps change by call and are not in the Income Tax Act. Read the current Malta Enterprise guidelines before quoting a figure.

## Section 10: Red Lines

| Risk | Detail | Source |
| --- | --- | --- |
| Anti-avoidance | Malta has a general anti-avoidance rule. An artificial or fictitious scheme is disregarded. A scheme whose sole or main purpose is a tax advantage can be nullified by the Commissioner's order. Companies also face the ATAD rules in S.L. 123.187. | Cap. 123 art. 51 |
| Family employment | Must be real work, paid at a matching rate, run through FSS payroll | Cap. 123 art. 14(1); S.L. 123.07 rule 4 |
| Capital items expensed | Capital spending is barred by article 26; claim it through wear and tear | Cap. 123 art. 26 |
| Undeclared income | Omission additional tax of 1.5% a month of the endangered tax, up to 60 months, reduced if corrected early | Cap. 123 Schedule, items 5 to 9 |
| Late return (individual) | EUR 10 within 6 months, rising to EUR 500 after 60 months (Table A) | Cap. 123 Schedule, item 2 |

## Section 11: Annual Tax Planning Calendar (basis year 2026)

| Month | Action |
| --- | --- |
| January | Receive FS3s for 2025 by 31 January. Review 2026 provisional tax benchmark. |
| April | **30 April 2026**: first provisional tax instalment (20%). Part-time 10% tax and 15% rental tax for 2025 due. |
| June | **30 June 2026**: individual return for basis year 2025 (check MTCA's online extension). |
| August | **31 August 2026**: second provisional tax instalment (30%). |
| September to November | Estimate 2026 profit. File the P.T. reduction form if tax will fall. Plan asset purchases. |
| December | **21 December 2026**: third provisional tax instalment (50%). Buy and start using planned assets. Pay pension contributions. |
| 2027 | 30 April 2027: part-time 10% tax on 2026 profit. 30 June 2027: return for basis year 2026. |

Sources: S.L. 372.16; S.L. 372.18; Cap. 372 art. 42(4); S.L. 372.14 rule 21.

## Section 12: Worked Examples

All figures are invented. Rates are from the 2026 single table and the rules cited above.

### Example 1: part-time 10% final tax against declaring the profit

A single person, a full-time employee registered with Jobsplus, has chargeable employment income of EUR 30,000 in 2026. She also has EUR 10,000 of part-time design profit from her own clients, registered with Jobsplus, with no employees. Every part-time condition is met.

- With the 10% final tax: EUR 10,000 × 10% = EUR 1,000, paid by 30 April 2027.
- If she declared the profit instead: tax on EUR 40,000 is 40,000 × 25% − 3,400 = EUR 6,600; tax on EUR 30,000 alone is EUR 4,100. The extra tax would be EUR 2,500.
- The 10% route saves EUR 1,500.

```oa-check
name: Part-time 10% final tax against progressive rates, single, basis year 2026
inputs:
  employment: 30000
  part_time_profit: 10000
  cap: 12000
steps:
  - final_tax: min(part_time_profit, cap) * 0.10
  - tax_with_profit: (employment + part_time_profit) * 0.25 - 3400
  - tax_without_profit: employment * 0.25 - 3400
  - extra_if_declared: tax_with_profit - tax_without_profit
  - saving: extra_if_declared - final_tax
expected:
  final_tax: 1000
  tax_with_profit: 6600
  tax_without_profit: 4100
  extra_if_declared: 2500
  saving: 1500
```

### Example 2: a car bought in December, with the EUR 14,000 cap

A self-employed consultant, single, chargeable income well inside the 25% band, buys a car for EUR 30,000 on 15 December 2026 and starts using it at once. A mileage log shows 80% business use.

- The cost is capped at EUR 14,000 (S.L. 123.07 rule 3). Minimum life is 5 years.
- Allowance for 2026: 14,000 ÷ 5 × 80% = EUR 2,240. Rule 7(a) gives the full year even though the car was bought in December.
- Without the cap it would have been 30,000 ÷ 5 × 80% = EUR 4,800.
- Tax value of the 2026 allowance at 25%: EUR 560. Had she bought in January 2027, the first allowance would fall in basis year 2027.

```oa-check
name: Car wear and tear with the EUR 14,000 cap, 80% business use, bought December 2026
inputs:
  cost: 30000
  cap: 14000
  years: 5
  business_share: 0.80
  marginal_rate: 0.25
steps:
  - allowed_cost: min(cost, cap)
  - allowance_2026: allowed_cost / years * business_share
  - uncapped_allowance: cost / years * business_share
  - tax_value: allowance_2026 * marginal_rate
expected:
  allowed_cost: 14000
  allowance_2026: 2240
  uncapped_allowance: 4800
  tax_value: 560
```

## Section 13: Ask the Client First

1. Are you in full-time employment registered with Jobsplus, a pensioner, or a full-time student? Is the side work registered and for different customers?
2. Married or single in 2026? Children, their ages, custody, and nationality of each spouse?
3. Expected 2026 profit, and will profits be paid out or kept in the business?
4. What did your last self-assessment show (the provisional tax benchmark)?
5. Which assets will you buy, when, and what share is business use?
6. Turnover in 2025 and so far in 2026, and who are your customers (businesses or consumers)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Cap. 123 (arts. 14, 14D, 26, 51, 56, 57, 90A, Schedule) | https://legislation.mt/eli/cap/123/eng/pdf | 2026-10-23 |
| Income Tax Management Act, Cap. 372 (arts. 42, 44, 48) | https://legislation.mt/eli/cap/372/eng/pdf | 2026-10-23 |
| Deduction for Wear and Tear of Plant and Machinery Rules, S.L. 123.01 | https://legislation.mt/eli/sl/123.1/eng/pdf | 2026-10-23 |
| Income Tax (Deductions) Rules, S.L. 123.07 | https://legislation.mt/eli/sl/123.7/eng/pdf | 2026-10-23 |
| Pensions (Tax Exemption) Rules, S.L. 123.204 (L.N. 53 of 2026) | https://legislation.mt/eli/sl/123.204/eng/pdf | 2026-10-23 |
| Voluntary Occupational Pension Scheme Rules, S.L. 123.175 | https://legislation.mt/eli/sl/123.175/eng/pdf | 2026-10-23 |
| MTCA, Completing your tax return, basis year 2025 (pension tax credits) | https://mtca.gov.mt/docs/default-source/documents/personal-tax/individual/tax-return-booklet-individuals/mtca-tax-booklet-2026-eng-17-03.pdf?sfvrsn=5ca02b73_1 | 2026-10-23 |
| VAT Act, Cap. 406 (arts. 10, 11) | https://legislation.mt/eli/cap/406/eng/pdf | 2026-10-23 |
| VAT capital goods regulations, S.L. 406.12 | https://legislation.mt/eli/sl/406.12/eng/pdf | 2026-10-23 |
| Act III of 2026 (2026 rate tables, art. 14D amount, art. 14(1)(ha)) | https://legislation.mt/getpdf/69d8ed326fe5fd3994d17430 | 2026-10-23 |

Rates and dates also rely on the sources listed in `malta-income-tax`, `mt-corporate-tax`, `mt-estimated-tax` and `malta-vat-return`.

Not yet confirmed:
- The 2026 personal retirement scheme and occupational pension tax credit figures (the 25% and EUR 750 are from MTCA's booklet for basis year 2025).
- Whether Class 2 social security contributions are deductible on the 2026 return.
- Whether the Gazette notice and rules starting the 175% deduction in art. 14(1)(ha) have been issued.
- 2026 Class 2 weekly amounts (see `malta-ssc`).
- Current Malta Enterprise scheme rates and caps.
- Budget 2027 is presented on 26 October 2026; nothing from it is reflected here.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
