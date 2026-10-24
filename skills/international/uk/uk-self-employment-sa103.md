---
name: uk-self-employment-sa103
description: "UK sole trader trading profits on the Self Assessment self-employment pages (SA103S short, SA103F full) for tax year 2026-27 (6 April 2026 to 5 April 2027), with the 2025-26 figures for returns due by 31 January 2027. Covers who is taxed on trading profits, allowable expenses, the GBP 1,000 trading allowance, cash basis as the default from 2024-25, the tax year basis and the five-year spreading of transition profits, capital allowances (AIA GBP 1 million, 14% main pool from 6 April 2026, 40% first-year allowance), simplified expenses (55p a mile from 2026-27), trade losses and the sideways relief cap, Class 4 NIC, Making Tax Digital for Income Tax from 6 April 2026, filing deadlines, penalties and interest. Trigger: 'sole trader tax', 'SA103', 'allowable expenses', 'trading allowance', 'cash basis', 'basis period reform', 'transition profit', 'MTD for Income Tax'. Out of scope: partnerships (SA104), companies (uk-corporation-tax), NIC detail (uk-national-insurance), payments on account (uk-payments-on-account), Scottish rates (uk-scottish-income-tax)."
version: 3.3
jurisdiction: GB
category: international
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK self-employment: sole trader profits on the SA103 (2026-27, with 2025-26)

> **Source-cited draft.** Drafted from the Income Tax (Trading and Other Income) Act 2005, the Income Tax Act 2007, the Finance Acts 2022, 2024 and 2026, the Capital Allowances Act 2001, the Social Security Contributions and Benefits Act 1992 and HMRC pages, all read on 2026-10-24. No accountant has reviewed it. Do not file from it without review by a qualified UK professional.

This skill computes the taxable trading profit of an individual who trades on their own account, and the Class 4 NIC on it. The income tax on that profit is worked out with the rest of the person's income in `uk-income-tax-sa100` (or `uk-scottish-income-tax` for Scottish taxpayers). Payments on account are in `uk-payments-on-account`; Class 2, Class 4 and voluntary contributions in full are in `uk-national-insurance`.

Tax year: 6 April to 5 April. Authority: HM Revenue and Customs (HMRC). Currency: pound sterling (GBP).

## Who this applies to

- **Sole traders.** An individual carrying on a trade, profession or vocation alone. Partners use the partnership pages (SA104), not this skill. A limited company is taxed under `uk-corporation-tax`.
- **UK residents** are taxed on the profits of their trade wherever it is carried on (ITTOIA 2005 s 6(1)).
- **Non-residents** are taxed only on profits of a trade carried on wholly or partly in the UK, on the UK part (ITTOIA 2005 s 6(2)). A trade of dealing in or developing UK land is taxed wherever it is carried on (s 6(1A)).
- **Split year.** In a split year the overseas part is treated as non-resident (s 6(2A)); see `uk-statutory-residence-test`.
- **Short or full pages.** For 2025-26 the full pages (SA103F) are needed if turnover was GBP 90,000 or more (SA103F notes 2026); below that the short pages (SA103S) can be used if no other full-page condition applies.
- **Small side income.** If gross trading income from all trades is GBP 1,000 or less, the trading allowance covers it in full (see below) and no return is needed for it unless another reason applies.

Who is out: partnerships, companies, employees taxed through PAYE, and landlords (property income goes on the SA105, `uk-rental-sa105`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Trading allowance (full relief if gross trading income does not exceed it; otherwise elect to deduct it instead of expenses) | GBP 1,000 | 2025-26 and 2026-27 | ITTOIA 2005 ss 783AD, 783AE, 783AH: https://www.legislation.gov.uk/ukpga/2005/5/section/783AD |
| Cash basis | Default for sole traders from 2024-25; election under s 25C to use accruals (GAAP) | 2024-25 onwards | ITTOIA 2005 ss 24A, 25C (inserted by FA 2024 Sch 10): https://www.legislation.gov.uk/ukpga/2024/3/schedule/10 |
| Annual Investment Allowance | GBP 1,000,000 a year | 2025-26 and 2026-27 | CAA 2001 s 51A(5): https://www.legislation.gov.uk/ukpga/2001/2/section/51A |
| Main pool writing-down allowance | 14% from 6 April 2026 (18% before; hybrid rate for a period spanning the date) | 2026-27 (18% for 2025-26) | FA 2026 s 28: https://www.legislation.gov.uk/ukpga/2026/11/section/28 |
| Special rate pool writing-down allowance | 6% | 2025-26 and 2026-27 | https://www.gov.uk/work-out-capital-allowances/rates-and-pools |
| First-year allowance, new and unused main-rate plant (not cars, not second-hand, not special rate) | 40% | Expenditure on or after 1 January 2026 | CAA 2001 ss 45U, 52 (FA 2026 s 29): https://www.legislation.gov.uk/ukpga/2026/11/section/29 |
| Simplified expenses: cars and goods vehicles, first 10,000 business miles | 55p a mile (45p before 6 April 2026) | 2026-27 (45p for 2025-26) | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Simplified expenses: cars and goods vehicles over 10,000 miles; motorcycles | 25p; 24p a mile | 2025-26 and 2026-27 | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Simplified expenses: working from home (25-50 / 51-100 / 101+ hours a month) | GBP 10 / 18 / 26 a month | 2025-26 and 2026-27 | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Simplified expenses: private use of business premises (1 / 2 / 3+ people) | GBP 350 / 500 / 650 a month | 2025-26 and 2026-27 | https://www.gov.uk/simpler-income-tax-simplified-expenses/print |
| Transition profit spreading (basis period reform) | 20% a year in 2023-24 to 2026-27; balance in 2027-28 | 2026-27 is year 4 of 5 | FA 2022 Sch 1 para 72: https://www.legislation.gov.uk/ukpga/2022/3/schedule/1 |
| Cap on sideways loss relief and other Step 2 reliefs | Greater of GBP 50,000 and 25% of adjusted total income | 2025-26 and 2026-27 | ITA 2007 s 24A(5): https://www.legislation.gov.uk/ukpga/2007/3/section/24A |
| Personal allowance; basic rate band (rest of UK) | GBP 12,570; 20% to GBP 50,270, 40% to GBP 125,140, 45% above | 2025-26 and 2026-27 | https://www.gov.uk/income-tax-rates |
| Class 4 NIC | 6% on profits GBP 12,570 to 50,270; 2% above | 2025-26 and 2026-27 | SSCBA 1992 s 15(3): https://www.legislation.gov.uk/ukpga/1992/4/section/15 |
| Class 2 NIC | Not payable; treated as paid at profits of GBP 7,105 or more (2026-27; GBP 6,845 for 2025-26); voluntary GBP 3.65 a week (GBP 3.50 for 2025-26) | 2025-26 and 2026-27 | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions |
| MTD for Income Tax: qualifying income (turnover from self-employment plus property) | Over GBP 50,000 in 2024-25: from 6 April 2026. Over GBP 30,000 in 2025-26: from 6 April 2027. Over GBP 20,000 in 2026-27: from 6 April 2028 | 2026-27 onwards | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax |
| Late payment interest | Bank of England base rate plus 4%; 7.75% from 9 January 2026 | Current | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

## The taxable base

**1. Profits of the tax year.** From 2024-25, tax is charged on the profits of the tax year itself (ITTOIA 2005 s 7(1), as amended by FA 2022 Sch 1). If the accounting year does not end on or between 31 March and 5 April, apportion the profits of the two accounting periods that overlap the tax year, normally by days (BIM81201). If the later accounts are not ready by the filing date, use provisional figures and amend.

**2. Transition profits.** A trader whose accounting date was not 31 March to 5 April had a transition profit in 2023-24. It is spread: 20% is taxed in each of 2023-24, 2024-25, 2025-26 and 2026-27, and the balance in 2027-28 (FA 2022 Sch 1 para 72). The trader can elect to bring more forward (para 73). If the trade ceases first, the whole balance is taxed in the year of cessation (para 72(6)). The spread amount is trading profit for income tax and for Class 4 NIC (SSCBA 1992 s 15(1)(b)), but it is a separate component that is left out of net income for later steps of the income tax calculation (para 75), so it does not by itself taper the personal allowance.

**3. Cash basis or accruals.** The cash basis is the default for sole traders from 2024-25 (ITTOIA 2005 s 24A). Income counts when received and expenses when paid. A trader can elect for generally accepted accounting practice instead (s 25C), for example a business with high stock or one that needs accruals accounts for a lender. Some trades cannot use the cash basis (s 25B; GOV.UK cash basis page): for example Lloyd's underwriters, farmers with a herd basis election, and businesses that have claimed business premises renovation allowance in the last 7 years. Under the cash basis, equipment bought to keep and use in the business is deducted as a normal expense; cars still go through capital allowances. From 2024-25 the old cash basis limits on interest (GBP 500) and on sideways loss relief are gone (FA 2024 Sch 10 paras 7 and 8).

**4. Allowable expenses.** A deduction is allowed only for an expense incurred wholly and exclusively for the trade (ITTOIA 2005 s 34). For a mixed-use cost, deduct the identifiable business part. Not allowed: private spending, the trader's own drawings and pay, income tax and NIC, fines, most entertaining, and (under accruals) capital expenditure, which gets capital allowances instead.

**5. Trading allowance (GBP 1,000).** If gross trading income from all trades is GBP 1,000 or less, it is not taxed (ITTOIA 2005 s 783AE). If it is more, the trader can elect for partial relief: deduct GBP 1,000 instead of actual expenses and capital allowances (s 783AH). Neither allowance can be used in a year with any trading or property income from a company the person or someone connected to them owns or controls, a partnership in which they or a connected person are partners, or their employer or their spouse's or civil partner's employer.

**6. Simplified expenses.** Flat rates can replace actual costs for business vehicles, working from home (25 hours a month or more) and private use of business premises (rates in the table). A vehicle on simplified mileage cannot also get capital allowances, and once used for a vehicle the flat rate stays for as long as it is used in the business.

**7. Capital allowances (accruals basis, or cars under either basis).**
- AIA: 100% of plant and machinery spending up to GBP 1,000,000 a year, scaled for a period that is not 12 months. Cars never qualify.
- Main-rate first-year allowance: 40% on new and unused main-rate plant bought on or after 1 January 2026; the rest goes to the main pool. Open to sole traders.
- Writing-down allowances: main pool 14% from 6 April 2026 (18% before), special rate pool 6%. A basis period straddling 6 April 2026 uses a hybrid rate: 18 x days before plus 14 x days after, over the days in the period, rounded up to 2 decimal places (FA 2026 s 28(4)-(5)).
- Reduce the claim for private use of an asset by a sole trader.

**8. Losses (ITA 2007 Part 4).**
- s 64: set the loss against general income of the loss year, the previous year, or both. Claim by the first anniversary of the 31 January filing date for the loss year.
- s 72: a loss in the first 4 tax years of trading can be carried back against general income of the 3 previous years, earliest first.
- s 83: carry forward against later profits of the same trade, without time limit.
- s 89: terminal loss on cessation, carried back against profits of the same trade for the final year and 3 previous years.
- The s 64 and s 72 deductions against other income (with some other reliefs) are capped at the greater of GBP 50,000 and 25% of adjusted total income (s 24A). The cap does not apply to losses set against profits of the same trade.

**9. Class 4 NIC.** 6% of profits between GBP 12,570 and GBP 50,270, and 2% above (SSCBA 1992 s 15(3)). Profits of a trade carried on wholly outside the UK are excluded (s 15(1)(c)). Class 2 is no longer payable; voluntary Class 2 is open to those with profits under the small profits threshold. Detail and exceptions: `uk-national-insurance`.

## Deadlines and filing

- **Register.** Tell HMRC by 5 October after the end of the tax year in which the trade started (for 2025-26: 5 October 2026).
- **Return.** Self Assessment return with the SA103 pages: paper by 31 October, online by 31 January after the tax year (TMA 1970 s 8(1D)). For 2025-26: 31 October 2026 paper, 31 January 2027 online. For 2026-27: 31 October 2027 and 31 January 2028. If the notice to file is issued late, the deadline is 3 months from the notice.
- **Pay.** Balancing payment by 31 January after the tax year (TMA 1970 s 59B(4)). Payments on account fall on 31 January in the tax year and 31 July after it; see `uk-payments-on-account`.
- **Making Tax Digital for Income Tax.** Mandatory from 6 April 2026 for sole traders and landlords whose qualifying income (turnover from self-employment plus gross property income, before expenses) on the 2024-25 return was over GBP 50,000. It extends to qualifying income over GBP 30,000 on the 2025-26 return from 6 April 2027, and over GBP 20,000 on the 2026-27 return from 6 April 2028. In MTD the trader keeps digital records, sends quarterly updates by 7 August, 7 November, 7 February and 7 May, and files the tax return through MTD software by 31 January. Exemptions exist, for example for the digitally excluded. Partnerships come in later on a date not yet set.

## Penalties and interest

**Annual Self Assessment return (FA 2009 Sch 55), outside MTD:**
- GBP 100 on the day after the deadline.
- After 3 months: GBP 10 a day for up to 90 days (maximum GBP 900).
- After 6 months: the greater of 5% of the tax due and GBP 300.
- After 12 months: another greater of 5% and GBP 300 (higher where information is deliberately withheld).

**Late payment (FA 2009 Sch 56), outside MTD:** 5% of the tax unpaid at 30 days, again at 6 months and again at 12 months.

**MTD for Income Tax (from the year the trader joins):**
- Late submission is points based: one point per missed deadline; at 4 points a GBP 200 penalty, and GBP 200 for each further missed deadline. For 2026-27 there are no penalties for late quarterly updates; a late tax return still earns a point.
- Late payment: nothing if paid within 15 days. For 2026-27: 3% of the tax owed at day 15, plus 3% of the tax still owed at day 30, plus 10% a year charged daily from day 31 (for up to 2 years). For 2027-28 the two percentages become 4%. In the first MTD year, a payment 16 to 30 days late carries no penalty. Payments on account are outside these penalties.

**Interest.** Late payment interest runs from the due date at base rate plus 4%: 7.75% from 9 January 2026. Repayment interest is base rate minus 1% with a 0.5% floor.

**Failure to notify.** Registering after 5 October and not paying all tax by 31 January can bring a failure to notify penalty based on the tax unpaid.

## Cross-border points

- **UK resident with a foreign trade.** All profits are taxable in the UK (ITTOIA 2005 s 6(1)). A trade carried on wholly outside the UK gives relevant foreign income (s 7(5)) and is outside Class 4 NIC (SSCBA 1992 s 15(1)(c)). Foreign tax on the same profits is relieved by credit; see `uk-foreign-tax-and-withholding`. New UK arrivals may use the foreign income and gains regime; see `uk-non-dom`.
- **Non-resident trading in the UK.** Only the profits of the part of the trade carried on in the UK are taxable (s 6(2)), except a trade of dealing in or developing UK land, which is taxed in full (s 6(1A)). Hub skill: `uk-non-resident-sa109`.
- **Arriving or leaving mid-year.** Check for a split year (`uk-statutory-residence-test`); profits of the overseas part follow the non-resident rule.
- **Social security abroad.** Whether UK Class 4 or foreign contributions apply depends on residence and any social security agreement; see `uk-national-insurance`.

## Worked examples

### Example 1: Sole trader on the cash basis, turnover GBP 48,000 (2026-27)

Priya is a self-employed graphic designer in Manchester. In 2026-27 she receives GBP 48,000 from clients and pays GBP 9,000 of allowable expenses (software, phone, accountant, insurance). She drives 6,000 business miles in her own car and uses the flat rate. She has no other income and uses the cash basis.

- Mileage: 6,000 x 55p = GBP 3,300 (all within the first 10,000 miles).
- Profit: 48,000 - 9,000 - 3,300 = GBP 35,700. The trading allowance would give only 48,000 - 1,000 = GBP 47,000, so actual expenses are better.
- Taxable income: 35,700 - 12,570 = GBP 23,130, all at 20% = GBP 4,626.00.
- Class 4 NIC: 23,130 x 6% = GBP 1,387.80.
- Total: GBP 6,013.80, due by 31 January 2028 if she has no payments on account.
- MTD: her qualifying income is turnover, not profit. If her 2025-26 turnover was over GBP 30,000, she must use MTD from 6 April 2027.

```oa-check
name: Sole trader, cash basis, turnover 48,000, 2026-27
inputs:
  turnover: 48000
  expenses: 9000
  business_miles: 6000
  personal_allowance: 12570
steps:
  - mileage: min(business_miles, 10000) * 0.55 + max(business_miles - 10000, 0) * 0.25
  - profit: turnover - expenses - mileage
  - profit_with_trading_allowance: turnover - 1000
  - taxable: profit - personal_allowance
  - income_tax: min(taxable, 37700) * 0.20
  - class4: (min(profit, 50270) - 12570) * 0.06
  - total: income_tax + class4
expected:
  mileage: 3300
  profit: 35700
  profit_with_trading_allowance: 47000
  taxable: 23130
  income_tax: 4626.00
  class4: 1387.80
  total: 6013.80
```

### Example 2: 30 September year end, apportionment and transition profit (2026-27)

Tom has run a plumbing business for years with accounts to 30 September. His accounts show a taxable profit (after capital allowances) of GBP 60,000 for the year to 30 September 2026 and GBP 72,000 for the year to 30 September 2027. His 2023-24 transition profit was GBP 25,000, spread at 20% a year. He has no other income and lives in England.

- Year to 30 September 2026: the part from 6 April to 30 September 2026 is 178 of 365 days: 60,000 x 178 / 365 = GBP 29,260.27.
- Year to 30 September 2027: the part from 1 October 2026 to 5 April 2027 is 187 of 365 days: 72,000 x 187 / 365 = GBP 36,887.67.
- Profit of the tax year 2026-27: GBP 66,147.95.
- Transition profit for 2026-27 (year 4 of 5): 25,000 x 20% = GBP 5,000. The last GBP 5,000 is taxed in 2027-28.
- Total trading profit: GBP 71,147.95. His net income without the transition part is under GBP 100,000, so the full personal allowance stays.
- Income tax: 37,700 x 20% = GBP 7,540.00; (71,147.95 - 50,270) x 40% = GBP 8,351.18; total GBP 15,891.18.
- Class 4 NIC (the transition profit counts): (50,270 - 12,570) x 6% = GBP 2,262.00; (71,147.95 - 50,270) x 2% = GBP 417.56; total GBP 2,679.56.
- Total: GBP 18,570.74.
- Edge case: the 2027 accounts must be final, or provisional figures used, before the 31 January 2028 deadline. Changing his year end to 31 March would end the apportionment.

```oa-check
name: Sole trader, 30 September year end with transition profit, 2026-27
inputs:
  profit_ye_sep_2026: 60000
  profit_ye_sep_2027: 72000
  days_in_2026_27_from_first: 178
  days_in_2026_27_from_second: 187
  days_in_year: 365
  transition_profit: 25000
  personal_allowance: 12570
steps:
  - part_first: profit_ye_sep_2026 * days_in_2026_27_from_first / days_in_year
  - part_second: profit_ye_sep_2027 * days_in_2026_27_from_second / days_in_year
  - tax_year_profit: part_first + part_second
  - transition_part: transition_profit * 0.20
  - total_profit: tax_year_profit + transition_part
  - taxable: total_profit - personal_allowance
  - basic_tax: min(taxable, 37700) * 0.20
  - higher_tax: (min(taxable, 112570) - 37700) * 0.40
  - income_tax: basic_tax + higher_tax
  - class4_main: (min(total_profit, 50270) - 12570) * 0.06
  - class4_upper: max(total_profit - 50270, 0) * 0.02
  - class4: class4_main + class4_upper
  - total: income_tax + class4
expected:
  part_first: 29260.27
  part_second: 36887.67
  tax_year_profit: 66147.95
  transition_part: 5000
  total_profit: 71147.95
  basic_tax: 7540.00
  higher_tax: 8351.18
  income_tax: 15891.18
  class4_main: 2262.00
  class4_upper: 417.56
  class4: 2679.56
  total: 18570.74
```

## Ask the client first

1. What is your accounting year end, and do you still have transition profit being spread from 2023-24?
2. What was your turnover from self-employment and gross property income on your 2024-25 and 2025-26 returns? (This decides when MTD applies.)
3. Do you use the cash basis or traditional (accruals) accounting, and do you hold stock?
4. What did you buy for the business this year (equipment, vans, cars), when, new or used, and how much is private use?
5. Did the business make a loss in this or an earlier year, and do you have other income to set it against?
6. Were you UK resident for the whole tax year, and do you trade anywhere outside the UK?

## Sources

| Source | URL | Read on |
|---|---|---|
| ITTOIA 2005 s 6 (territorial scope) | https://www.legislation.gov.uk/ukpga/2005/5/section/6 | 2026-10-24 |
| ITTOIA 2005 s 7 (profits of the tax year) | https://www.legislation.gov.uk/ukpga/2005/5/section/7 | 2026-10-24 |
| ITTOIA 2005 s 25 (GAAP where cash basis does not apply) | https://www.legislation.gov.uk/ukpga/2005/5/section/25 | 2026-10-24 |
| ITTOIA 2005 s 34 (wholly and exclusively) | https://www.legislation.gov.uk/ukpga/2005/5/section/34 | 2026-10-24 |
| ITTOIA 2005 ss 783A, 783AD, 783AE, 783AH (trading allowance) | https://www.legislation.gov.uk/ukpga/2005/5/section/783AD | 2026-10-24 |
| Finance Act 2024 Sch 10 (cash basis default, ss 24A, 25B, 25C) | https://www.legislation.gov.uk/ukpga/2024/3/schedule/10 | 2026-10-24 |
| Finance Act 2022 Sch 1 paras 65 to 75 (transition profits) | https://www.legislation.gov.uk/ukpga/2022/3/schedule/1 | 2026-10-24 |
| Finance Act 2026 s 28 (main pool 14%, hybrid rate) | https://www.legislation.gov.uk/ukpga/2026/11/section/28 | 2026-10-24 |
| Finance Act 2026 s 29 (40% first-year allowance, CAA 2001 s 45U) | https://www.legislation.gov.uk/ukpga/2026/11/section/29 | 2026-10-24 |
| CAA 2001 s 51A (AIA GBP 1,000,000) | https://www.legislation.gov.uk/ukpga/2001/2/section/51A | 2026-10-24 |
| ITA 2007 s 24A (cap on reliefs) | https://www.legislation.gov.uk/ukpga/2007/3/section/24A | 2026-10-24 |
| ITA 2007 s 64 (loss against general income) | https://www.legislation.gov.uk/ukpga/2007/3/section/64 | 2026-10-24 |
| ITA 2007 s 72 (early trade losses) | https://www.legislation.gov.uk/ukpga/2007/3/section/72 | 2026-10-24 |
| ITA 2007 s 83 (carry-forward) | https://www.legislation.gov.uk/ukpga/2007/3/section/83 | 2026-10-24 |
| ITA 2007 s 89 (terminal loss) | https://www.legislation.gov.uk/ukpga/2007/3/section/89 | 2026-10-24 |
| SSCBA 1992 s 15 (Class 4) | https://www.legislation.gov.uk/ukpga/1992/4/section/15 | 2026-10-24 |
| TMA 1970 s 8 (return deadlines) | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-10-24 |
| TMA 1970 s 59B (balancing payment) | https://www.legislation.gov.uk/ukpga/1970/9/section/59B | 2026-10-24 |
| FA 2009 Sch 55 (late filing penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-24 |
| FA 2009 Sch 56 (late payment penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/56 | 2026-10-24 |
| HMRC Business Income Manual BIM81201 (tax year basis, apportionment) | https://www.gov.uk/hmrc-internal-manuals/business-income-manual/bim81201 | 2026-10-24 |
| GOV.UK, Get help with basis period reform | https://www.gov.uk/guidance/get-help-with-basis-period-reform | 2026-10-24 |
| GOV.UK, Cash basis | https://www.gov.uk/simpler-income-tax-cash-basis/print | 2026-10-24 |
| GOV.UK, Tax-free allowances on property and trading income | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income | 2026-10-24 |
| GOV.UK, Simplified expenses | https://www.gov.uk/simpler-income-tax-simplified-expenses/print | 2026-10-24 |
| GOV.UK, Annual Investment Allowance | https://www.gov.uk/capital-allowances/annual-investment-allowance | 2026-10-24 |
| GOV.UK, 40% first-year allowance | https://www.gov.uk/capital-allowances/40-first-year-allowance | 2026-10-24 |
| GOV.UK, Capital allowances rates and pools | https://www.gov.uk/work-out-capital-allowances/rates-and-pools | 2026-10-24 |
| GOV.UK, Income Tax rates and Personal Allowances (current and previous) | https://www.gov.uk/income-tax-rates | 2026-10-24 |
| GOV.UK, Self-employed National Insurance rates | https://www.gov.uk/self-employed-national-insurance-rates | 2026-10-24 |
| HMRC, Rates and allowances: National Insurance contributions | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions | 2026-10-24 |
| GOV.UK, Find out if and when you need to use MTD for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-24 |
| GOV.UK, Work out your qualifying income for MTD for Income Tax | https://www.gov.uk/guidance/work-out-your-qualifying-income-for-making-tax-digital-for-income-tax | 2026-10-24 |
| GOV.UK, Penalties for MTD for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-24 |
| GOV.UK, Self Assessment deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-10-24 |
| GOV.UK, Self Assessment penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-24 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |
| HMRC, Self-employment (full) notes 2025-26 (SA103F Notes 2026) | https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf | 2026-10-24 |

Not yet confirmed: the 2026-27 SA103S and SA103F forms and box numbers (not published when read); the legislation fixing the GBP 20,000 MTD threshold from April 2028 (GOV.UK states the threshold, but an earlier version of the page said legislation was still to be introduced); the MTD exemption list in full; the s 74A to 74D limits for non-active traders; how the 40% first-year allowance applies to a cash basis trader (equipment is deducted as an expense there, so the allowance matters mainly under accruals and for cars, which it excludes); the full list of trades excluded from the cash basis under ITTOIA 2005 s 25B (only the GOV.UK summary was read).

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
