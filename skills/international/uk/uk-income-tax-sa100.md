---
name: uk-income-tax-sa100
description: "UK Income Tax for individuals who file the SA100 Self Assessment return, tax year 2026-27 (6 April 2026 to 5 April 2027), with 2025-26 figures for returns filed now. Covers the GBP 12,570 Personal Allowance and its taper above GBP 100,000, the frozen bands and the 20%, 40% and 45% rates, the Welsh rates, the six Scottish bands for 2026-27, the starting rate for savings and the Personal Savings Allowance, the dividend allowance and rates, Marriage Allowance, the High Income Child Benefit Charge, who must file, registration by 5 October, the 31 October and 31 January deadlines, penalties and late payment interest. Trigger on: SA100, personal allowance taper, income tax bands 2026-27, Scottish income tax, marriage allowance, child benefit charge, register for self assessment, late tax return penalty. Out of scope: uk-self-employment-sa103, uk-rental-sa105, uk-capital-gains-sa108, uk-national-insurance, uk-statutory-residence-test, uk-dividends, uk-scottish-income-tax, uk-payments-on-account."
version: 2.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Income Tax for individuals: the SA100 Self Assessment return (2026-27)

Source-cited draft: not reviewed by an accountant, not for filing. Built by Michael Cutajar and the OpenAccountants team.

The UK tax year runs from 6 April to 5 April. The year in force is 2026-27 (6 April 2026 to 5 April 2027). The returns being filed now are for 2025-26, due online by 31 January 2027. Where a figure differs between the two years, both are given. Rules already enacted for 2027-28 are flagged so nobody applies them early.

This skill sets out the income tax computation and the filing rules. It points to the other UK skills and does not repeat them:

- Sole trader profits, the trading allowance and Class 4 figures: `uk-self-employment-sa103`.
- Rental profits, finance costs and the property allowance: `uk-rental-sa105`.
- Capital gains: `uk-capital-gains-sa108`.
- National Insurance: `uk-national-insurance`.
- Residence and split years: `uk-statutory-residence-test` (and `uk-non-resident-sa109` for the SA109 pages).
- Dividend planning and director pay: `uk-dividends`.
- Scottish taxpayer status tests and S codes in depth: `uk-scottish-income-tax`.
- Payments on account in depth: `uk-payments-on-account`.

## Who this applies to

- **UK residents** are charged on their income for the tax year. A person who is not resident is outside this skill: use `uk-statutory-residence-test` and `uk-non-resident-sa109`. The Personal Allowance needs the residence conditions in ITA 2007 s.56 ([ITA 2007 s.35](https://www.legislation.gov.uk/ukpga/2007/3/section/35)).
- **Which rates apply to wages, pensions, self-employment and rent (non-savings income)** depends on where the main home is:
  - England and Northern Ireland: the UK main rates.
  - Wales: the Welsh rates. HMRC shows them equal to the England rates for 2026-27. A Welsh taxpayer has a tax code starting with C ([Welsh Income Tax](https://www.gov.uk/welsh-income-tax)).
  - Scotland: the Scottish rates and six bands. A Scottish taxpayer has a tax code starting with S ([Scottish Income Tax](https://www.gov.uk/scottish-income-tax)).
- **Savings interest and dividends** are taxed at UK rates wherever the person lives in the UK. GOV.UK: "You'll pay the same tax as the rest of the UK on dividends and savings interest" ([Scottish Income Tax](https://www.gov.uk/scottish-income-tax)).
- **Main home test.** The main home is usually where the person lives and spends most time. With no clear main home, count days in Scotland (or Wales) against days elsewhere in the UK; where a person is at midnight decides the day. The status applies for the whole tax year ([Scottish Income Tax](https://www.gov.uk/scottish-income-tax)).
- **Who must send a return.** For the last tax year, a person must send a return if they were a sole trader with income over GBP 1,000 before expenses, a partner in a partnership, had Capital Gains Tax to pay, had to pay the High Income Child Benefit Charge and do not pay it through PAYE, or are an off-payroll worker repaying a student or postgraduate loan. Untaxed income (rent, tips, savings interest, dividends, foreign income) can also need a return ([who must send a tax return](https://www.gov.uk/self-assessment-tax-returns/who-must-send-a-tax-return)).
- **Dividends.** Dividends taxable above the allowances can be reported by tax code change if under GBP 10,000. Dividends over GBP 10,000 need a Self Assessment return ([tax on dividends](https://www.gov.uk/tax-on-dividends)).
- Anyone HMRC has sent a notice to file must file, whatever their income (TMA 1970 s.8).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Personal Allowance (ITA 2007 s.35(1); FA 2021 s.5 as amended by FA 2026 s.10) | GBP 12,570, frozen to 2030-31 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/10 |
| Personal Allowance taper (ITA 2007 s.35(2)) | Reduced by half the adjusted net income over GBP 100,000; nil at GBP 125,140 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/35 |
| Basic rate limit (ITA 2007 s.10(5); FA 2021 s.5 as amended by FA 2026 s.10) | GBP 37,700, frozen to 2030-31 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/10 |
| Higher rate limit (ITA 2007 s.10(5A)) | GBP 125,140 (2 x 12,570 + 100,000) | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/10 |
| Main rates, England and NI: basic, higher, additional (FA 2026 s.2) | 20%, 40%, 45% | 2026-27 (same in 2025-26) | https://www.legislation.gov.uk/ukpga/2026/11/section/2 |
| Bands with the standard allowance, England, Wales and NI | 0% to 12,570; 20% 12,571 to 50,270; 40% 50,271 to 125,140; 45% over 125,140 | 2025-26 and 2026-27 | https://www.gov.uk/income-tax-rates |
| Welsh rates, 2026-27 (Government of Wales Act 2006 s.116D; Welsh rate resolution NDM9117, agreed 27 January 2026) | Welsh rate 10p in each band, so the same bands and rates as England (20%, 40%, 45%) | 2026-27 | https://record.senedd.wales/Motion/9117 |
| Scottish starter rate (ITA 2007 s.11A; Scottish Rate Resolution S6M-20844, agreed 19 February 2026: 19% on the first GBP 3,967 above the allowance) | 19% on GBP 12,571 to 16,537 (2025-26: 12,571 to 15,397) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish basic rate (S6M-20844: above GBP 3,967 up to 16,956 above the allowance) | 20% on GBP 16,538 to 29,526 (2025-26: 15,398 to 27,491) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish intermediate rate (S6M-20844: above GBP 16,956 up to 31,092) | 21% on GBP 29,527 to 43,662 (2025-26: 27,492 to 43,662) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish higher rate (S6M-20844: above GBP 31,092 up to 62,430) | 42% on GBP 43,663 to 75,000 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish advanced rate (S6M-20844: above GBP 62,430 up to 125,140) | 45% on GBP 75,001 to 125,140 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Scottish top rate (S6M-20844) | 48% over GBP 125,140 (same in 2025-26) | 2026-27 | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 |
| Savings rates (FA 2026 s.3(2)) | 20%, 40%, 45% | 2026-27 (same in 2025-26) | https://www.legislation.gov.uk/ukpga/2026/11/section/3 |
| Savings rates enacted for 2027-28 (FA 2026 s.5) | 22%, 42%, 47%; not for 2026-27 | 2027-28 | https://www.legislation.gov.uk/ukpga/2026/11/section/5 |
| Starting rate limit for savings (ITA 2007 s.12(3); FA 2026 s.9) | GBP 5,000 at 0%, frozen 2026-27 to 2030-31 | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/9 |
| Starting rate entry point | Other taxable income under GBP 17,570; each GBP 1 over the Personal Allowance cuts the GBP 5,000 by GBP 1 | 2026-27 | https://www.gov.uk/apply-tax-free-interest-on-savings |
| Personal Savings Allowance (ITA 2007 s.12B) | GBP 1,000 basic rate; GBP 500 higher rate; nil additional rate | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/12B |
| Dividend allowance (dividend nil rate band, ITA 2007 s.13A) | GBP 500 | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A |
| Dividend ordinary, upper, additional rates (ITA 2007 s.8 as amended by FA 2026 s.4) | 10.75%, 35.75%, 39.35% (2025-26: 8.75%, 33.75%, 39.35%) | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/4 |
| Marriage Allowance transferable amount (ITA 2007 s.55B(4)-(5)) | 10% of the Personal Allowance rounded up to GBP 10: GBP 1,260; tax cut up to GBP 252 | 2025-26 and 2026-27 | https://www.gov.uk/marriage-allowance |
| High Income Child Benefit Charge (ITEPA 2003 s.681C) | 1% of Child Benefit per GBP 200 of adjusted net income over GBP 60,000; 100% at GBP 80,000 | 2024-25 onwards | https://www.legislation.gov.uk/ukpga/2003/1/section/681C |
| Late payment interest | Bank of England base rate plus 4%; 7.75% from 9 January 2026 | Current | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

The resolution limits are amounts of income above the Personal Allowance; with the standard GBP 12,570 allowance they give the bands in the table, which match HMRC's [Scottish Income Tax](https://www.gov.uk/scottish-income-tax) page. The 2025-26 main bands come from GOV.UK's previous tax years page, which states the 2025-26 Personal Allowance was GBP 12,570 and the higher rate started on income over GBP 50,270 ([Income Tax rates: previous tax years](https://www.gov.uk/income-tax-rates/previous-tax-years)).

## The taxable base

**Step 1: total income, split into three kinds.** Non-savings income (employment, pensions, self-employment profit from `uk-self-employment-sa103`, property profit from `uk-rental-sa105`), then savings income (interest), then dividends. ISA interest and dividends are not taxable. HMRC splits joint account interest equally unless told otherwise ([savings interest](https://www.gov.uk/apply-tax-free-interest-on-savings)).

**Step 2: reliefs deducted from income**, such as trading losses and pension contributions paid gross.

**Step 3: adjusted net income (ITA 2007 s.58).** Take total taxable income less those reliefs, then also deduct grossed-up Gift Aid and grossed-up relief-at-source pension contributions ([adjusted net income](https://www.gov.uk/guidance/adjusted-net-income)). Adjusted net income drives the Personal Allowance taper and the Child Benefit charge.

**Step 4: the Personal Allowance.** GBP 12,570, reduced by half of the adjusted net income over GBP 100,000. A result that is not a whole pound rounds up (ITA 2007 s.35(2)-(3)). The allowance is nil at GBP 125,140 or more. Between GBP 100,000 and GBP 125,140 the effective marginal rate on non-savings income is 60% in England, Wales and NI.

**Step 5: extend the bands.** Grossed-up relief-at-source pension contributions and Gift Aid extend the basic rate limit (and the higher rate limit) by the gross amount. This is how higher rate relief is given.

**Step 6: tax the income in the statutory order.**
- Non-savings income first, at the main, Welsh or Scottish rates.
- Savings next. The starting rate for savings (0% on up to GBP 5,000) applies only to savings that would otherwise fall in the basic rate band, and the GBP 5,000 shrinks by each pound of other income above the Personal Allowance (ITA 2007 s.12). Then the Personal Savings Allowance: GBP 1,000 if no income is higher rate income, GBP 500 if some is but none is additional rate income, nil if any is additional rate income (ITA 2007 s.12B). Interest counts when deciding the band. Above those, savings are taxed at 20%, 40% or 45%.
- Dividends last. Dividends inside any unused Personal Allowance are tax-free. The next GBP 500 is taxed at the dividend nil rate. The nil rate band still uses up the basic and higher rate bands; it is not a deduction (ITA 2007 s.13A). The rest is taxed at 10.75%, 35.75% or 39.35% for 2026-27. GOV.UK's example: wages GBP 29,570 and dividends GBP 3,000 give 20% on GBP 17,000 of wages, nothing on GBP 500 of dividends and 10.75% on GBP 2,500 ([tax on dividends](https://www.gov.uk/tax-on-dividends)). Dividend planning sits in `uk-dividends`.

**Step 7: tax reducers.** Marriage Allowance is a reducer for the recipient. The lower earner gives up GBP 1,260 of Personal Allowance and the partner's tax falls by up to GBP 252. Conditions: married or in a civil partnership (not just living together); neither partner, after the transfer, is liable above the basic rate (in Scotland, above the intermediate rate); and neither claims Married Couple's Allowance (ITA 2007 s.55B(2), s.55C(1)). The claim helps the couple only when the transferor's income is below the Personal Allowance, as GOV.UK puts it. Claims can be backdated to 6 April 2022 and renew each year until cancelled. It cannot be combined with Married Couple's Allowance ([Marriage Allowance](https://www.gov.uk/marriage-allowance); [ITA 2007 s.55B](https://www.legislation.gov.uk/ukpga/2007/3/section/55B)).

**Step 8: add charges.** The High Income Child Benefit Charge applies when the person or their partner gets Child Benefit and the person's adjusted net income is over GBP 60,000. The charge is the appropriate percentage of the Child Benefit: (adjusted net income minus GBP 60,000) divided by GBP 200, capped at 100%. The percentage and the pounds both round down to whole numbers. If both partners are over GBP 60,000, the partner with the higher adjusted net income pays. "Partner" includes someone the person lives with as if married ([ITEPA 2003 s.681C](https://www.legislation.gov.uk/ukpga/2003/1/section/681C); [Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge)).

The 2026-27 position on how the charge is paid: an employee or pensioner can pay it through PAYE, using HMRC's online service, if they need no return for another reason and act on or before 31 January after the tax year. Otherwise the charge goes through Self Assessment. Example from GOV.UK: for 2025-26, after 31 January 2027 the charge must be paid through Self Assessment. Someone who registered for Self Assessment only for the charge can phone HMRC to leave Self Assessment and pay through PAYE. Opting out of Child Benefit payments avoids the charge and keeps National Insurance credits ([Child Benefit charge](https://www.gov.uk/child-benefit-tax-charge)).

**Step 9: take off tax already paid** (PAYE, tax deducted from interest, payments on account) to reach the balance due.

**Losses.** Trading losses and property losses follow their own rules in `uk-self-employment-sa103` and `uk-rental-sa105`. Capital losses stay inside `uk-capital-gains-sa108`.

**Not for 2026-27.** From 2027-28 FA 2026 brings in property rates of 22%, 42% and 47% (s.7) and savings rates of 22%, 42% and 47% (s.5). Do not apply them to 2025-26 or 2026-27 ([FA 2026 s.7](https://www.legislation.gov.uk/ukpga/2026/11/section/7)).

## Deadlines and filing

| Event | 2025-26 return (filed now) | 2026-27 return |
|---|---|---|
| Tell HMRC you need to file (TMA 1970 s.7: 6 months after the tax year) | 5 October 2026 | 5 October 2027 |
| Paper return (TMA 1970 s.8(1D)(a)) | 11:59pm, 31 October 2026 | 31 October 2027 |
| Online return, if the balance is to be collected through the tax code | 11:59pm, 30 December 2026 | 30 December 2027 |
| Online return (TMA 1970 s.8(1D)(b)) | 11:59pm, 31 January 2027 | 31 January 2028 |
| Balancing payment, and first payment on account for the next year | 31 January 2027 | 31 January 2028 |
| Second payment on account | 31 July 2027 | 31 July 2028 |

Sources: [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines); [register for Self Assessment](https://www.gov.uk/register-for-self-assessment); [TMA 1970 s.7](https://www.legislation.gov.uk/ukpga/1970/9/section/7); [TMA 1970 s.8](https://www.legislation.gov.uk/ukpga/1970/9/section/8).

- **Who must register by 5 October:** someone who needs to file for the previous year and has not sent a return before, or registered before but did not need to send one for 2024-25.
- **Notice to file sent late.** If HMRC's notice to file is given after 31 October, the return (paper or online) is due 3 months from the notice date; if it is given between 1 August and 31 October, the online deadline stays 31 January and a paper return is due 3 months from the notice (TMA 1970 s.8(1F)-(1G)). HMRC confirms the date by email or letter ([register for Self Assessment](https://www.gov.uk/register-for-self-assessment)).
- **When the tax is due after a late notice.** If the person registered by 5 October but HMRC's notice came after 31 October, the balance is due 3 months from the notice. If the person registered after 5 October, the tax is still due by 31 January 2027 ([TMA 1970 s.59B(3)-(4)](https://www.legislation.gov.uk/ukpga/1970/9/section/59B); [deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines)).
- HMRC must receive the return and the money by the deadline. A return is still due if the full-year profit is not yet known.
- **Payments on account** are each half of last year's Self Assessment bill, unless last year's bill was under GBP 1,000 or more than 80% of the tax was paid at source. Detail and SA303 claims: `uk-payments-on-account`.
- Online returns are filed through HMRC online services or commercial software. Sole traders and landlords inside Making Tax Digital for Income Tax keep quarterly updates on top; see `uk-self-employment-sa103`.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Return late, day 1 | GBP 100 (FA 2009 Sch 55 para 3) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/3 |
| Return still late after 3 months | GBP 10 a day for up to 90 days, so up to GBP 900 (Sch 55 para 4) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/4 |
| Return still late after 6 months | The greater of 5% of the tax due and GBP 300 (Sch 55 para 5) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/5 |
| Return still late after 12 months | A further greater of 5% and GBP 300; higher if information is deliberately withheld (Sch 55 para 6) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/6 |
| Tax paid late | 5% of the tax unpaid at 30 days, 6 months and 12 months (FA 2009 Sch 56) | https://www.gov.uk/self-assessment-tax-returns/penalties |
| Registered after 5 October and tax not paid by 31 January | Failure to notify penalty, based on the tax still unpaid | https://www.gov.uk/self-assessment-tax-returns/penalties |
| Late payment interest | Base rate plus 4% from 6 April 2025; 7.75% from 9 January 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Repayment interest | Base rate minus 1%, floor 0.5%; 2.75% from 9 January 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

**Making Tax Digital for Income Tax.** Sole traders and landlords who must use Making Tax Digital from 6 April 2026 (qualifying income over GBP 50,000 in 2024-25) get new penalties from the 2026-27 tax year in place of the late filing and late payment penalties above; interest is unchanged. The 2025-26 return due 31 January 2027 stays on the old penalties ([MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax); [MTD: who and when](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)).

| MTD failure, 2026-27 tax year | Penalty | Source |
|---|---|---|
| Late tax return | One penalty point per missed deadline; at 4 points, GBP 200, and GBP 200 for each later missed deadline. No points for late quarterly updates in 2026-27 (FA 2021 Sch 24) | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax |
| Tax paid late | Nothing up to 15 days; 3% of the tax owed at day 15 and 3% at day 30, plus 10% a year from day 31 (FA 2021 Sch 26; SI 2025/589). In the first year of the new penalties, nothing applies if the tax is paid or a payment plan is set up within 30 days. Payments on account are outside this penalty. 2027-28: 4% and 4% | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax |

A penalty is due within 30 days of the notice. An appeal needs a reasonable excuse. Interest moves with the Bank of England base rate, so check the HMRC page on the day you compute it.

## Cross-border points

- **Residence decides the scope.** Use `uk-statutory-residence-test` for the test and split years, and `uk-non-resident-sa109` for the SA109 pages. Do not compute a non-resident or a split year with this skill alone.
- **Personal Allowance for non-residents** depends on the residence conditions in ITA 2007 s.56. Marriage Allowance still works if a partner lives abroad, as long as they get a Personal Allowance ([Marriage Allowance](https://www.gov.uk/marriage-allowance)).
- **Foreign income and foreign tax credit relief:** `uk-foreign-tax-and-withholding`. The foreign income and gains regime for new arrivals: `uk-non-dom`.
- **Moving between Scotland, Wales and the rest of the UK.** The new rates are backdated to 6 April of the year of the move. Status follows where the person lived longest in the tax year ([Scottish Income Tax](https://www.gov.uk/scottish-income-tax); [Welsh Income Tax](https://www.gov.uk/welsh-income-tax)).
- **Leaving the UK:** see `uk-to-uae-relocation-tax` and `uk-to-italy-flat-tax-relocation` for exit planning.

## Worked examples

### Example 1: employee with side business and dividends, England, 2026-27

Sarah lives in England. In 2026-27 she earns a salary of GBP 40,000 (PAYE deducted GBP 5,486), makes a sole trader profit of GBP 20,000 and receives UK dividends of GBP 5,000. Her adjusted net income is GBP 65,000, under GBP 100,000, so she keeps the full GBP 12,570 allowance.

Non-savings income is GBP 60,000. After the allowance, GBP 47,430 is taxable. The first GBP 37,700 is taxed at 20% (GBP 7,540) and the remaining GBP 9,730 at 40% (GBP 3,892). Her dividends sit on top, wholly in the higher rate band. The first GBP 500 is at the dividend nil rate. The other GBP 4,500 is taxed at 35.75%: GBP 1,608.75. Total income tax is GBP 13,040.75. After PAYE, GBP 7,554.75 is due through Self Assessment. In 2025-26 the same dividends would have cost GBP 1,518.75 at 33.75%, so the rise costs her GBP 90. Class 4 National Insurance on the profit is extra: see `uk-national-insurance`.

```oa-check
name: GB 2026-27, England, salary 40000, profit 20000, dividends 5000
inputs:
  salary: 40000
  profit: 20000
  dividends: 5000
  paye: 5486
steps:
  - non_savings: salary + profit
  - taxable_ns: non_savings - 12570
  - basic: min(taxable_ns, 37700) * 0.20
  - higher: (taxable_ns - 37700) * 0.40
  - div_taxed: dividends - 500
  - div_tax: div_taxed * 0.3575
  - total_tax: basic + higher + div_tax
  - due_sa: total_tax - paye
  - div_tax_2025_26: div_taxed * 0.3375
  - rise: div_tax - div_tax_2025_26
expected:
  taxable_ns: 47430
  basic: 7540
  higher: 3892
  div_tax: 1608.75
  total_tax: 13040.75
  due_sa: 7554.75
  rise: 90
```

### Example 2: Personal Allowance taper and the Child Benefit charge, England, 2026-27

Tom lives in England and earns GBP 112,000 of salary in 2026-27. He pays GBP 4,000 into a personal pension under relief at source, so the gross contribution is GBP 5,000. His partner earns less. The family received GBP 1,406 of Child Benefit in the year (take the figure from the award, not an estimate).

Adjusted net income is GBP 112,000 minus GBP 5,000 = GBP 107,000. That is GBP 7,000 over GBP 100,000, so the allowance falls by GBP 3,500 to GBP 9,070. The gross contribution extends his basic rate band to GBP 42,700. Taxable income is GBP 102,930. GBP 42,700 at 20% is GBP 8,540. The other GBP 60,230 at 40% is GBP 24,092. Income tax is GBP 32,632.

His adjusted net income is GBP 47,000 over GBP 60,000. That gives 235%, capped at 100%, so the Child Benefit charge is the full GBP 1,406. Total is GBP 34,038 before PAYE. A further gross pension contribution of GBP 7,000 would bring adjusted net income to GBP 100,000 and restore the full allowance; the charge would stay at 100% while adjusted net income is GBP 80,000 or more.

```oa-check
name: GB 2026-27, England, PA taper with relief-at-source pension and HICBC
inputs:
  salary: 112000
  pension_net: 4000
  child_benefit: 1406
steps:
  - pension_gross: pension_net / 0.8
  - ani: salary - pension_gross
  - pa: max(0, 12570 - ceil(max(0, ani - 100000) / 2))
  - brb: 37700 + pension_gross
  - taxable: salary - pa
  - basic: min(taxable, brb) * 0.20
  - higher: (taxable - brb) * 0.40
  - income_tax: basic + higher
  - pct: min(100, floor(max(0, ani - 60000) / 200))
  - hicbc: floor(child_benefit * pct / 100)
  - total: income_tax + hicbc
expected:
  pension_gross: 5000
  ani: 107000
  pa: 9070
  taxable: 102930
  income_tax: 32632
  pct: 100
  hicbc: 1406
  total: 34038
```

## Ask the client first

- Which tax year: the 2025-26 return being filed now, or 2026-27? The dividend rates differ.
- Where was your main home in the year: England or NI, Wales, or Scotland? Did you move during the year, or spend time outside the UK?
- Have you filed a return before, and did you file for 2024-25? This decides the 5 October registration duty.
- All income by kind: P60 and P11D, self-employment and rental income before expenses, interest outside ISAs, dividends outside ISAs, pensions, foreign income.
- Pension contributions (relief at source or net pay) and Gift Aid. They change adjusted net income, the taper and the Child Benefit charge.
- Married or in a civil partnership, and both partners' incomes? Does anyone in the household get Child Benefit, and how much?

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act 2026 (c. 11) s.2, main rates 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/2 | 2026-10-24 |
| Finance Act 2026 s.3, default and savings rates 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/3 | 2026-10-24 |
| Finance Act 2026 s.4, dividend ordinary and upper rates | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-10-24 |
| Finance Act 2026 s.5, savings rates 2027-28 | https://www.legislation.gov.uk/ukpga/2026/11/section/5 | 2026-10-24 |
| Finance Act 2026 s.7, property rates 2027-28 | https://www.legislation.gov.uk/ukpga/2026/11/section/7 | 2026-10-24 |
| Finance Act 2026 s.9, starting rate limit for savings | https://www.legislation.gov.uk/ukpga/2026/11/section/9 | 2026-10-24 |
| Finance Act 2026 s.10, basic rate limit and Personal Allowance freeze | https://www.legislation.gov.uk/ukpga/2026/11/section/10 | 2026-10-24 |
| Income Tax Act 2007 s.10, basic and higher rate limits | https://www.legislation.gov.uk/ukpga/2007/3/section/10 | 2026-10-24 |
| Income Tax Act 2007 s.12, starting rate for savings | https://www.legislation.gov.uk/ukpga/2007/3/section/12 | 2026-10-24 |
| Income Tax Act 2007 s.12A and s.12B, savings nil rate and savings allowance | https://www.legislation.gov.uk/ukpga/2007/3/section/12B | 2026-10-24 |
| Income Tax Act 2007 s.13A, dividend nil rate | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-10-24 |
| Income Tax Act 2007 s.35, Personal Allowance and taper | https://www.legislation.gov.uk/ukpga/2007/3/section/35 | 2026-10-24 |
| Income Tax Act 2007 s.55B and s.55C, Marriage Allowance | https://www.legislation.gov.uk/ukpga/2007/3/section/55B | 2026-10-24 |
| ITEPA 2003 s.681C, High Income Child Benefit Charge | https://www.legislation.gov.uk/ukpga/2003/1/section/681C | 2026-10-24 |
| Taxes Management Act 1970 s.7, notice of liability | https://www.legislation.gov.uk/ukpga/1970/9/section/7 | 2026-10-24 |
| Taxes Management Act 1970 s.8, return filing dates | https://www.legislation.gov.uk/ukpga/1970/9/section/8 | 2026-10-24 |
| Taxes Management Act 1970 s.59B, payment dates | https://www.legislation.gov.uk/ukpga/1970/9/section/59B | 2026-10-24 |
| Scottish Parliament, Scottish Rate Resolution 2026-27 (S6M-20844), agreed 19 February 2026, 93 for, 29 against | https://www.parliament.scot/chamber-and-committees/votes-and-motions/S6M-20844 | 2026-10-24 |
| Senedd, Welsh rate resolution 2026-27 (NDM9117), 10p in each band | https://record.senedd.wales/Motion/9117 | 2026-10-24 |
| Senedd Record of Proceedings, 27 January 2026, item 5: motion agreed, 26 for, 13 against, 13 abstentions | https://record.senedd.wales/Plenary/15728 | 2026-10-24 |
| Finance Act 2021 Sch 24 and Sch 26, points-based and late payment penalties | https://www.legislation.gov.uk/ukpga/2021/26/schedule/26 | 2026-10-24 |
| SI 2025/589, Schedule 26 penalty percentages | https://www.legislation.gov.uk/uksi/2025/589/made | 2026-10-24 |
| Finance Act 2009 Sch 55 paras 3 to 6, late filing penalties | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-24 |
| Finance Act 2009 Sch 56 para 3, late payment penalties | https://www.legislation.gov.uk/ukpga/2009/10/schedule/56/paragraph/3 | 2026-10-24 |
| GOV.UK, Income Tax rates and Personal Allowances | https://www.gov.uk/income-tax-rates | 2026-10-24 |
| GOV.UK, Income Tax rates: previous tax years (2025-26) | https://www.gov.uk/income-tax-rates/previous-tax-years | 2026-10-24 |
| GOV.UK, Scottish Income Tax (2026-27 and 2025-26 bands) | https://www.gov.uk/scottish-income-tax | 2026-10-24 |
| Scottish Government, Scottish Income Tax rates and bands 2026 to 2027 | https://www.gov.scot/publications/scottish-income-tax-rates-and-bands/pages/2026-to-2027/ | 2026-10-24 |
| GOV.UK, Welsh Income Tax (2026-27) | https://www.gov.uk/welsh-income-tax | 2026-10-24 |
| Welsh Government, written statement on Draft Budget 2026-27 Welsh taxes (10p in each band) | https://www.gov.wales/written-statement-draft-budget-2026-27-welsh-taxes | 2026-10-24 |
| GOV.UK, tax on savings interest | https://www.gov.uk/apply-tax-free-interest-on-savings | 2026-10-24 |
| GOV.UK, tax on dividends | https://www.gov.uk/tax-on-dividends | 2026-10-24 |
| GOV.UK, Marriage Allowance | https://www.gov.uk/marriage-allowance | 2026-10-24 |
| GOV.UK, High Income Child Benefit Charge | https://www.gov.uk/child-benefit-tax-charge | 2026-10-24 |
| GOV.UK, adjusted net income | https://www.gov.uk/guidance/adjusted-net-income | 2026-10-24 |
| GOV.UK, Self Assessment: who must send a return, deadlines, penalties | https://www.gov.uk/self-assessment-tax-returns | 2026-10-24 |
| GOV.UK, register for Self Assessment | https://www.gov.uk/register-for-self-assessment | 2026-10-24 |
| GOV.UK, find out if and when you need to use Making Tax Digital for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-24 |
| GOV.UK, penalties for Making Tax Digital for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-24 |
| HMRC, interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |

Not yet confirmed: the Personal Savings Allowance amounts for 2027-28 are not published. The Welsh Government's own Welsh rates page (gov.wales/welsh-rates-income-tax) still describes 2023-24 and was not used.

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
