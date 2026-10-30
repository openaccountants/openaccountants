---
name: im-income-tax
description: "Use this skill for Isle of Man personal income tax for resident individuals in the 2026/27 tax year (6 April 2026 to 5 April 2027). It covers residence (the six-month statutory test and the 90-day four-year practice), the GBP 17,000 personal allowance (GBP 34,000 for a jointly assessed couple) and its taper above GBP 100,000, the 10% and 21% rates and the GBP 6,500 / GBP 13,000 lower-rate band, additional allowances, deductions relieved at 10% and their limits, the GBP 220,000 / GBP 440,000 tax cap election, independent and joint taxation, returns, payment dates, payment on account, penalties and late-payment interest, and double taxation relief. Trigger on: Manx income tax, Isle of Man tax return, ITIP, tax cap election, IOM personal allowance, payment on account Isle of Man. Out of scope: non-residents (im-non-resident-income-tax), National Insurance (im-payroll-social), companies (im-corporate-income-tax), VAT (isle-of-man-vat)."
jurisdiction: IM
tax_year: 2026
last_updated: 2026-10-30
version: 0.3
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Isle of Man: personal income tax for residents (2026/27) v0.3

This skill covers income tax on resident individuals in the Isle of Man for the 2026/27 year of assessment, which runs from 6 April 2026 to 5 April 2027. The law is the Income Tax Act 1970 (AT 3 of 1970), with the rates and the lower-rate threshold set by Treasury order under section 1(3A). The authority is the Income Tax Division of the Treasury. Amounts are in pounds sterling (GBP).

Read [im-non-resident-income-tax](im-non-resident-income-tax.md) for individuals who are not resident, [im-payroll-social](im-payroll-social.md) for ITIP payroll deductions and National Insurance, [im-corporate-income-tax](im-corporate-income-tax.md) for companies and [isle-of-man-vat](../isle-of-man/isle-of-man-vat.md) for VAT.

**What changed for 2026/27.** Budget 2026 (17 February 2026, Practice Note PN 227/26) raised the personal allowance from GBP 14,750 to GBP 17,000 (GBP 29,500 to GBP 34,000 for a jointly assessed couple), the TT Homestay Allowance from GBP 2,350 to GBP 2,500 and the nursing expenses limit from GBP 12,500 to GBP 15,000. The 10% and 21% rates, the GBP 6,500 / GBP 13,000 threshold, the taper and the GBP 220,000 tax cap are unchanged.

## Who this applies to

- **Residents are taxed on worldwide income** and declare it on the annual return (Income Tax Division, Income tax returns and penalties; Double taxation relief page).
- **Statutory six-month test.** A person in the Island who has resided there, at one time or several times, for six months in any one year is chargeable as a resident for the year starting on 6 April (Income Tax Act 1970 s.10).
- **Intent to settle.** A person who arrives with a view or intent of establishing residence is resident from the date of arrival; a person who leaves permanently is non-resident from the date of departure (s.10; Practice Note PN 144/07 paras 4 and 5). New residents register on form R25.
- **The 90-day practice.** The Division also treats as resident a person whose visits over four or more consecutive tax years exceed an average of 90 days a year. Residence then starts in the fifth year, or from the first year if that pattern was intended from the start. Days of arrival and departure are not counted, and days spent in the Island for exceptional circumstances beyond the person's control are left out (PN 144/07 paras 7 and 8).
- **Temporary absence.** A person ordinarily resident who leaves only for occasional residence elsewhere stays chargeable as a resident (s.9). A person abroad for a complete tax year is non-resident for that year; a person abroad for two complete tax years or more is treated as permanently non-resident (PN 144/07 para 10; Leaving the Island page).
- **Married couples and civil partners** are taxed independently unless they elect for joint taxation. In the year of marriage or civil partnership each is treated as single; the election can take effect from the next tax year. A jointly assessed couple is jointly and severally liable (Marriage/civil partnership page; s.65A).
- **No capital gains tax or inheritance tax** applies in the Island (Moving to the Island page).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Personal allowance, single | GBP 17,000 | 2026/27 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/rates-and-allowances/ ; PN 227/26 |
| Personal allowance, jointly assessed couple | GBP 34,000 | 2026/27 | same |
| Allowance taper | reduced by GBP 1 for every GBP 2 of total income above GBP 100,000 (GBP 200,000 joint); nil at GBP 134,000 (GBP 268,000 joint) | 2026/27 | same; Budget 2026 page; ITA 1970 s.35(11), (12) |
| Lower (standard) rate | 10% on the first GBP 6,500 of taxable income (GBP 13,000 joint) | 2026/27 | rates page; PN 227/26 |
| Higher rate | 21% on taxable income above the threshold | 2026/27 | rates page; PN 227/26 |
| Single parent additional allowance | GBP 6,400 | 2026/27 | rates page; PN 227/26 |
| Co-habiting couple's maximum addition | GBP 6,400 | 2026/27 | PN 227/26 |
| Blind person allowance; disabled person allowance | GBP 2,900 each | 2026/27 | rates page; PN 227/26 |
| Mortgage and loan interest limit | GBP 5,000 (doubled for a jointly assessed couple) | 2026/27 | rates page |
| Charitable donations limit | GBP 7,000 | 2026/27 | rates page |
| Private medical insurance limit | GBP 1,800 | 2026/27 | rates page |
| Nursing expenses limit | GBP 15,000 | 2026/27 | rates page; PN 227/26 |
| Benefit in kind exemption (not car benefit) | GBP 600 | 2026/27 | rates page |
| TT Homestay Allowance | GBP 2,500 | 2026/27 | rates page; PN 227/26 |
| Income tax cap (election) | GBP 220,000 individual; GBP 440,000 jointly assessed couple | elections from 2025/26 onwards | ITA 1970 s.2ZB(1A); rates page |
| Payment on account factor | 105% of the previous year's liability less tax deducted at source | 2026/27 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/payment-on-account/ |
| Late return penalties | GBP 100; a further GBP 200 if still outstanding 6 months after the due date | 2026/27 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/income-tax-returns-and-penalties/ |
| Late payment interest | 5% | as stated on 30 October 2026 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/personal-tax/personal-tax-frequently-asked-questions/ |

## The base

### Step 1: total income

Income tax is charged on income from property, professions, trade, employment, pensions, annuities and any other source (s.1(1)). Every source is assessed on a current-year basis: 2026/27 is taxed on the income of the year ending 5 April 2027 (Moving to the Island page). Benefits in kind are taxable, with a GBP 600 exemption that does not cover car benefit (rates page). Rental income received under the TT Homestay Scheme during the TT period is reduced by the GBP 2,500 allowance, subject to its conditions (PN 227/26 para 2).

### Step 2: personal allowance and taper

Deduct GBP 17,000 (GBP 34,000 for a jointly assessed couple). If total income exceeds GBP 100,000 (GBP 200,000 joint), reduce the allowance by half the excess, rounding a remaining deduction up to the nearest pound (s.35(11), (12), (14); rates page). In the year residence starts or ends, the allowance is apportioned by time resident, and the GBP 100,000 / GBP 200,000 taper starting points are reduced pro rata (s.35(13); Receiving Isle of Man source income page).

Add any additional allowance the person qualifies for: single parent or eligible co-habiting couple with a child (GBP 6,400), blind person or disabled person (GBP 2,900) (rates page; Tax relief page; return guides GN1 and GN1S).

### Step 3: tax at the two rates

Charge 10% on taxable income up to GBP 6,500 (GBP 13,000 joint) and 21% on the balance (s.1(2); rates page).

### Step 4: deductions relieved at 10%

Interest paid on mortgages or loans, charitable donations and deeds of covenant, private medical insurance and nursing expenses are relieved at the lower rate of 10% only, as a reduction of the total tax liability (Tax relief page; Practice Note 172/12). The limits are GBP 5,000 for mortgage and loan interest (GBP 10,000 joint), GBP 7,000 for charitable donations, GBP 1,800 for private medical insurance and GBP 15,000 for nursing expenses (rates page). So relief for interest is 10% x min(interest paid, GBP 5,000). The lender's certificate of interest goes in with the return (Tax relief page).

Other deductions listed by the Division are personal pension contributions, superannuation, professional subscriptions, and tools and clothing (Tax relief page). The pension contribution limits are in Practice Note 201/18.

### Step 5: tax cap

A resident may elect for income tax to be capped at GBP 220,000 a year (GBP 440,000 for a jointly assessed couple) for five or ten consecutive tax years (s.2ZA(1), s.2ZB(1A)). The Assessor approves an election only if the tax otherwise payable in each year would exceed the cap (s.2ZA(3)). An election received on or before 5 April applies from the following 6 April. A new resident may elect within 60 days of starting residence for the rest of that year plus four (or nine) further years (s.2ZA(5), (6)). The cap amount for every year of an election is the amount that applied in its first year, and the full cap is payable each year even if actual tax would be lower (GN 51 paras 3.2 and 4.3). Where the election turns out to have cost more tax over its whole period than no election, the individual may apply to be assessed as if it had not been made (s.2ZA(10), (11)). The election is made in writing to the Assessor, or on form R264 (s.2ZA(2); GN 51 para 4.2). An approved election does not remove the duty to file the annual return (s.2ZA(9)).

### Step 6: credits

Deduct tax already paid through ITIP (payroll), subcontractor deductions, payments on account and double taxation relief (Assessments page; GN3 section 5.1).

## Deadlines and filing

- **Return.** Returns are issued shortly after 5 April and are due by 6 October following the end of the tax year (s.62(1); Income tax returns and penalties page). For 2026/27 the return is due by 6 October 2027. A person served with a notice must make a return within 6 months of service (s.62(4)). File online through Online Tax Services or on paper at the Income Tax Division, Government Offices, Bucks Road, Douglas. Both members of a jointly assessed couple sign the return.
- **Suspension.** A person whose income is consistently below the personal allowance may have the duty to file suspended by letter from the Division (Income tax returns and penalties page).
- **Payment.** The statutory due date is 6 January following the tax year (6 January 2028 for 2026/27). Tax is due 30 days after the assessment where the assessment is issued after 6 December following the tax year, or when the person has left the Island or died (GN3 section 5.1; FAQ page).
- **Payment on account.** A person whose previous-year liability was not settled by ITIP or subcontractor deductions (for example rent, bank interest, dividends, non-Manx pensions or self-employment) receives a payment-on-account notice at 105% of that liability less tax at source. It is due on 6 January in the tax year it relates to (6 January 2027 for 2026/27), or within 30 days if raised later. A person may apply to postpone part of it; interest runs from the original due date on any postponed amount that proves to be due (Payment on account page; GN3).
- **Leaving the Island.** Complete form R26. The final resident return covers 6 April to the date of departure and is due within 6 months of departure; tax on the final assessment is payable within 30 days (Leaving the Island page).
- **New residents** register on form R25 as soon as possible after arriving (Moving to the Island page).

## Penalties and interest

- **Late return:** GBP 100 if the return is not in by the due date, and a further GBP 200 if it is still outstanding 6 months after the due date. Paying the penalty does not remove the duty to file (Income tax returns and penalties page). For a leaver the GBP 100 applies if the return is not in within 6 months of departure and the further GBP 200 if not in within 12 months (Leaving the Island page).
- **Default assessment:** if no return is made, the Division raises an assessment on best judgement from previous assessments and third-party information; any refund waits until the return is filed (Assessments page).
- **Late payment interest:** charged from the day after the due date to the day before payment; the Division states the rate as currently 5% (GN3 section 7; FAQ page).

## Cross-border points

- **Double taxation relief.** Relief for foreign tax is limited to the lower of the foreign tax and the Manx tax on that income (ITA 1970 s.57; Guidance Note GN5). With no treaty, relief needs evidence of the foreign tax and proof that all reasonable steps were taken to minimise it. With a treaty, the treaty decides (Double taxation relief page).
- **UK treaty.** The 2018 UK-Isle of Man agreement has effect for Manx income tax from 6 April 2019. Under it, an Isle of Man resident's UK dividends (other than property income dividends, which the UK may tax up to 15%), interest and pensions are taxable only in the Island. UK rental income may be taxed in the UK first, with relief in the Island (Double taxation relief page; SI 2018/1347 Articles 6, 10, 11 and 17). For employment, see the three conditions of Article 14(2) in [im-non-resident-income-tax](im-non-resident-income-tax.md).
- **Dual residence.** A person can be resident in both the Island and another country under each country's law and must file in both. The treaty tie-breaker (permanent home, centre of vital interests, habitual abode, then mutual agreement) settles treaty residence only (Double taxation relief page; SI 2018/1347 Article 4(2)).
- **Non-residents** pay 21% on Manx income with no allowance: see [im-non-resident-income-tax](im-non-resident-income-tax.md).

## Worked examples

### Example 1: single resident employee, income GBP 50,000

A single resident has employment income of GBP 50,000 in 2026/27 and no deductions. The allowance is GBP 17,000, so taxable income is GBP 33,000. The first GBP 6,500 is taxed at 10% (GBP 650) and the remaining GBP 26,500 at 21% (GBP 5,565). Tax is GBP 6,215, against which ITIP deducted through payroll is credited.

```oa-check
name: IM resident single, total income 50,000 (2026/27)
inputs:
  income: 50000
  allowance: 17000
  band: 6500
steps:
  - taxable: max(income - allowance, 0)
  - lower: min(taxable, band) * 0.10
  - higher: max(taxable - band, 0) * 0.21
  - tax: lower + higher
expected:
  taxable: 33000.00
  lower: 650.00
  higher: 5565.00
  tax: 6215.00
```

### Example 2: allowance taper, income GBP 120,000, with mortgage interest

A single resident has total income of GBP 120,000. The excess over GBP 100,000 is GBP 20,000, so the allowance falls by GBP 10,000 to GBP 7,000. Taxable income is GBP 113,000: GBP 650 at 10% plus GBP 106,500 at 21% (GBP 22,365), GBP 23,015 in all. The person paid GBP 6,000 of mortgage interest. Relief is limited to GBP 5,000 at 10%, so GBP 500 comes off the liability, leaving GBP 22,515.

```oa-check
name: IM resident single, taper at 120,000 and capped interest relief (2026/27)
inputs:
  income: 120000
  allowance_full: 17000
  taper_start: 100000
  band: 6500
  interest_paid: 6000
  interest_cap: 5000
steps:
  - allowance: max(allowance_full - max(income - taper_start, 0) / 2, 0)
  - taxable: income - allowance
  - lower: min(taxable, band) * 0.10
  - higher: max(taxable - band, 0) * 0.21
  - tax_before_relief: lower + higher
  - interest_relief: min(interest_paid, interest_cap) * 0.10
  - tax: tax_before_relief - interest_relief
expected:
  allowance: 7000.00
  taxable: 113000.00
  tax_before_relief: 23015.00
  interest_relief: 500.00
  tax: 22515.00
```

## Ask the client first

1. Where did you live during 2026/27, and how many days were you in the Island in each of the last four tax years? Did you arrive or leave during the year?
2. Are you married or in a civil partnership, and do you have a joint taxation election in place?
3. What income did you have from each source, inside and outside the Island, and what foreign tax was paid on it?
4. Do you pay mortgage or loan interest, pension contributions, medical insurance, nursing costs or charitable donations?
5. Is your Manx tax likely to exceed GBP 220,000 a year, and do you have a tax cap election?
6. Did you receive a payment-on-account notice for 2026/27, and how much tax was deducted through ITIP?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 1970 (AT 3 of 1970), consolidated text [62], ss.1, 2ZA, 2ZB, 9, 10, 35, 35C, 62 | https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1970/1970-0003/1970-0003_62.pdf | 2026-10-30 |
| Income Tax Division, Rates and allowances (current and historic, 2026/27) | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/rates-and-allowances/ | 2026-10-30 |
| Income Tax Division, Budget 2026 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/budget/ | 2026-10-30 |
| Practice Note PN 227/26, Budget 2026 income tax and National Insurance proposals (17 February 2026) | https://www.gov.im/media/1391759/pn-227-26-budget.pdf | 2026-10-30 |
| Practice Note PN 144/07, Tax residence in the Isle of Man | https://www.gov.im/media/97083/pn14407taxresidenceintheisl.pdf | 2026-10-30 |
| Guidance Note GN 51, Income tax cap | https://www.gov.im/media/1384454/gn51-income-tax-cap-uploaded-270624.pdf | 2026-10-30 |
| Guidance Note GN3, Basis of assessment and payment on account (17 December 2024) | https://www.gov.im/media/1390241/gn3-basis-of-assessment-and-payment-on-account-uploaded-23925.pdf | 2026-10-30 |
| Income Tax Division, Income tax returns and penalties | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/income-tax-returns-and-penalties/ | 2026-10-30 |
| Income Tax Division, Payment on account | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/payment-on-account/ | 2026-10-30 |
| Income Tax Division, Assessments | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/assessments/ | 2026-10-30 |
| Income Tax Division, Personal tax frequently asked questions | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/personal-tax/personal-tax-frequently-asked-questions/ | 2026-10-30 |
| Income Tax Division, Tax relief | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/tax-relief/ | 2026-10-30 |
| Income Tax Division, Marriage/civil partnership | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/marriagecivil-partnership/ | 2026-10-30 |
| Income Tax Division, Moving to the Island: new residents | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/moving-to-the-island-new-residents/ | 2026-10-30 |
| Income Tax Division, Leaving the Island | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/leaving-the-island/ | 2026-10-30 |
| Income Tax Division, Receiving Isle of Man source income | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/receiving-isle-of-man-source-income/ | 2026-10-30 |
| Income Tax Division, International agreements and double taxation relief | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/international-agreements-and-double-taxation-relief/ | 2026-10-30 |
| UK-Isle of Man Double Taxation Agreement 2018, SI 2018/1347, Articles 4, 6, 10, 11, 14, 17 | https://www.legislation.gov.uk/uksi/2018/1347/pdfs/uksi_20181347_en.pdf | 2026-10-30 |

Not yet confirmed: the 2026 statutory document that raises the s.35 allowance to GBP 17,000 / GBP 34,000 (the consolidated Income Tax Act 1970 read on 30 October 2026 still prints the 2025/26 figures in s.35(9) and (10), as substituted by SD 2025/0060; the 2026/27 figures here come from the Division's rates page and PN 227/26, and legislation.gov.im blocked automated search for the 2026 order); the statutory basis and order setting the 5% late-payment interest rate; personal pension and superannuation contribution limits (PN 201/18 not read); the conditions for the co-habiting couple addition and the TT Homestay Allowance (PN 219/22 not read).

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
