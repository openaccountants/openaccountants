---
name: uk-dividends
description: "UK income tax on dividends for individuals, tax year 2026-27 (6 April 2026 to 5 April 2027), with the 2025-26 rates for returns filed now. Covers the GBP 500 dividend allowance (dividend nil rate), the 10.75%, 35.75% and 39.35% dividend rates from 6 April 2026 (8.75% and 33.75% before), how dividends sit on top of other income, salary versus dividends for owner-directors with Class 1 National Insurance and corporation tax, lawful dividends out of distributable profits (Companies Act 2006 s.830), the s.455 charge on loans to participators, foreign dividends and credit relief, dividend waivers, reporting on the SA100 and payments on account. Trigger on: dividend tax UK, dividend allowance, director dividends, salary vs dividends, 10.75%, 35.75%, SA100 dividends, dividend voucher, illegal dividend. Out of scope: uk-income-tax-sa100, uk-national-insurance, uk-corporation-tax, uk-foreign-tax-and-withholding, uk-scottish-income-tax, uk-payments-on-account."
version: 1.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-26
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
source_checked: 2026-10-26
depends_on:
  - uk-income-tax-sa100
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Dividends: income tax on dividends and director pay (2026-27)

> Source-cited draft: not reviewed by an accountant.

## Who this applies to

- Individuals who receive dividends from UK or foreign companies, including owner-directors of their own limited company.
- Dividend rates apply UK-wide. Scottish taxpayers pay the UK dividend rates; their Scottish bands apply only to non-savings income. See `uk-scottish-income-tax`.
- Not taxable: dividends inside an ISA. Dividends inside a pension wrapper are not taxed on the individual.
- The rest of the income tax computation (Personal Allowance, bands, other income) sits in `uk-income-tax-sa100`. National Insurance sits in `uk-national-insurance`. The company's own tax sits in `uk-corporation-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Dividend allowance (dividend nil rate, ITA 2007 s.13A and s.8(A1)) | GBP 500 at 0% | 2025-26 and 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/13A |
| Dividend ordinary rate (basic rate band) | 10.75% (8.75% in 2025-26) | 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/8 |
| Dividend upper rate (higher rate band) | 35.75% (33.75% in 2025-26) | 2026-27 | https://www.legislation.gov.uk/ukpga/2026/11/section/4 |
| Dividend additional rate (over GBP 125,140) | 39.35%, unchanged | 2026-27 | https://www.legislation.gov.uk/ukpga/2007/3/section/8 |
| Personal Allowance; basic rate band | GBP 12,570; GBP 37,700 | 2026-27 | https://www.gov.uk/tax-on-dividends |
| s.455 charge on loans to participators | Tied to the dividend upper rate: 35.75% | 2026-27 | https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note |
| Employer (secondary) Class 1 NIC | 15% above GBP 5,000 a year (GBP 96 a week) | 2026-27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Employee primary threshold; employee rates | GBP 12,570 a year (GBP 242 a week); 8%, 2% above the upper earnings limit | 2026-27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Lower earnings limit | GBP 6,708 a year (GBP 129 a week) | 2026-27 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 |
| Corporation tax | 19% on profits of GBP 50,000 or less, 25% over GBP 250,000, marginal relief between | FY2026 | https://www.gov.uk/corporation-tax-rates |
| Reporting line | Dividends over GBP 10,000 need a Self Assessment return | 2026-27 | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |

Finance Act 2026 s.4 substituted 10.75% for 8.75% and 35.75% for 33.75% in ITA 2007 s.8, with effect for 2026-27 and later years. The additional rate stays 39.35%.

## The taxable base

**Order of taxation.** Income is taxed in this order: non-savings income (salary, pensions, trading and property profit), then savings interest, then dividends. Dividends sit on top. Someone with GBP 45,000 of salary has GBP 5,270 of basic rate band left (GBP 50,270 less GBP 45,000) before dividends reach the upper rate.

**The allowance is a rate, not a deduction.** The first GBP 500 of dividends is taxed at the dividend nil rate. Those GBP 500 still count as income and still use up the basic or higher rate band (ITA 2007 s.13A). The allowance is per person. It cannot be carried forward or transferred to a spouse. Dividends inside any unused Personal Allowance are tax-free before the allowance is used.

**Computation.**
1. Total income from all sources.
2. Personal Allowance against non-savings income first.
3. Non-savings rates, then savings rates (see `uk-income-tax-sa100`).
4. Dividends: GBP 500 at 0%, then 10.75% inside the basic rate band, 35.75% inside the higher rate band, 39.35% above GBP 125,140.

**Personal Allowance taper.** Dividends count towards adjusted net income. Above GBP 100,000 the allowance falls by GBP 1 for every GBP 2 and is gone at GBP 125,140 (see `uk-income-tax-sa100`). Dividends also count for the High Income Child Benefit Charge and student loan repayments.

**What counts as a dividend.** Cash dividends from UK companies, interim or final; keep the voucher. Accumulation units, scrip dividends, dividends in specie, REIT property income distributions and corporate bond returns: see Not yet confirmed.

**Lawful dividends.** A company may make a distribution only out of profits available for the purpose: its accumulated, realised profits not already distributed or capitalised, less its accumulated, realised losses not written off (Companies Act 2006 s.830(1)-(2)). A loss-making company with no reserves cannot pay a dividend. A shareholder who knows, or has reasonable grounds to believe, that a distribution breaks these rules must repay it (s.847). An owner-director normally knows. Check the reserves in the latest accounts, or in interim accounts, before each dividend.

**Owner-directors: salary versus dividends.** Salary and employer NIC are deductible for corporation tax. Dividends are paid from profit after corporation tax and carry no NIC.

| Route | Company | Director |
|---|---|---|
| Salary | Deductible; employer NIC 15% above GBP 5,000 | Income tax 20%/40%/45%; employee NIC 8% above GBP 12,570, 2% above the upper earnings limit |
| Dividend | Not deductible; paid after 19% to 25% corporation tax | 0% on GBP 500, then 10.75%/35.75%/39.35%; no NIC |

- A common pattern: salary of GBP 12,570, with no income tax or employee NIC, and employer NIC of 15% x (12,570 - 5,000) = GBP 1,135.50, both deductible. Then dividends from the profit left after corporation tax.
- Salary of GBP 5,000 avoids employer NIC. Salary below the lower earnings limit (GBP 6,708) gives no State Pension qualifying year.
- Employment Allowance does not help a company whose only employee paid above the secondary threshold is a director (https://www.gov.uk/claim-employment-allowance/eligibility).
- Tax on GBP 1 of profit at the margin, ignoring allowances (salary route: 1 - (1 - income tax - employee NIC) / 1.15; dividend route: 1 - (1 - CT) x (1 - dividend rate)):

| Director's band | Salary | Dividend, company at 19% | Dividend, company at 25% |
|---|---|---|---|
| Basic | 37.39% | 27.71% | 33.06% |
| Higher | 49.57% | 47.96% | 51.81% |
| Additional | 53.91% | 50.87% | 54.51% |

  At 25% corporation tax, a higher or additional rate director pays more by dividend than by salary on the marginal pound. Re-run the comparison each year for each client.
- Salary must be paid under a proper employment arrangement through PAYE. Detail on NIC: `uk-national-insurance`; on marginal relief and associated companies: `uk-corporation-tax`.

**Loans to participators (s.455).** If a close company lends to a participator, such as a director-shareholder, the company owes a charge equal to the dividend upper rate for the tax year the loan is made: 35.75% for loans made in 2026-27 (CTA 2010 s.455(2)). Relief is given when the loan is repaid, released or written off, on a claim within 4 years from the end of the financial year of the repayment or write-off (CTA 2010 s.458). How a written-off loan is taxed on the individual: see Not yet confirmed.

**Dividend waivers.** A shareholder can waive a dividend. HMRC can challenge waivers that move income to a spouse or family member. Ask before relying on one; the rules are not set out here (see Not yet confirmed).

## Deadlines and filing

| Situation | What to do | Source |
|---|---|---|
| Dividends GBP 500 or less | Nothing to report | https://www.gov.uk/tax-on-dividends |
| Dividends over GBP 500 up to GBP 10,000, no Self Assessment | Tell HMRC after 5 April and before 5 October: ask for a tax code change or use the helpline | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |
| Dividends over GBP 10,000 | File an SA100. If you do not usually send one, register by 5 October after the tax year | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |
| Already in Self Assessment | Report on the SA100 | https://www.gov.uk/tax-on-dividends/how-to-report-tax-on-dividends |

- **SA100 boxes.** UK dividends in box 4, other dividends (such as from unit trusts) in box 5. Foreign dividends of GBP 500 or less in box 6, with any foreign tax in box 7; otherwise use the SA106 Foreign pages (SA100 2026 form).
- **Dates for 2026-27.** Paper return 31 October 2027; online return and balancing payment 31 January 2028; first payment on account for 2027-28 also 31 January 2028; second 31 July 2028. For the 2025-26 return the dates are one year earlier. See `uk-income-tax-sa100`.
- **Payments on account.** Dividend tax collected through Self Assessment feeds the payments on account for the next year: each is half of last year's bill, unless that bill was under GBP 1,000 or more than 80% of the tax was paid at source. A director whose dividends rise in 2026-27 faces a larger balancing payment and larger payments on account in January 2028. See `uk-payments-on-account`.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Return late, day 1 | GBP 100 | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/3 |
| Still late after 3 months | GBP 10 a day for up to 90 days | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55/paragraph/4 |
| Still late after 6 months, and again after 12 months | The greater of 5% of the tax due and GBP 300, each time | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 |
| Tax paid late | 5% of the tax unpaid at 30 days, 6 months and 12 months | https://www.legislation.gov.uk/ukpga/2009/10/schedule/56/paragraph/3 |
| Late payment interest | Base rate plus 4%; 7.75% from 9 January 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

Taxpayers inside Making Tax Digital for Income Tax move to points-based and new late payment penalties from 2026-27; see `uk-income-tax-sa100`. A shareholder who must repay an unlawful dividend under Companies Act 2006 s.847 does so to the company; that is a company law liability, not a tax penalty. Interest moves with the Bank of England base rate; check the HMRC page on the day.

## Cross-border points

- **Foreign dividends.** Report the gross amount before foreign tax,. Use SA100 box 6 and box 7 if they total GBP 500 or less; otherwise SA106.
- **Credit relief.** Foreign tax is credited against UK tax on the same income, up to the lower of the foreign tax and the UK tax on that income. Unilateral relief applies even without a treaty (TIOPA 2010 s.9). Credit is capped at the treaty rate; reclaim any excess from the foreign tax authority, not HMRC. No credit is due on dividends inside the GBP 500 allowance, because no UK tax is paid on them. Example: a higher rate taxpayer with GBP 3,950 of US dividends and GBP 593 of US tax pays UK tax of (3,950 - 500) x 35.75% = GBP 1,233.38, less a credit of GBP 593: GBP 640.38.
- **Treaty rates** (including the US rate and Form W-8BEN): `uk-foreign-tax-and-withholding`.
- **Non-residents.** Their UK tax position sits in `uk-non-resident-sa109`.

## Worked examples

### Example 1: employee with dividends straddling the higher rate threshold, 2026-27

Priya lives in England. She earns GBP 45,000 of salary and receives GBP 10,000 of UK dividends from shares she holds outside an ISA. She has no other income.

Her Personal Allowance covers GBP 12,570 of salary, so GBP 32,430 of salary is taxable and uses that much of the GBP 37,700 basic rate band. GBP 5,270 of the band is left for dividends. The first GBP 500 of dividends is at the nil rate but uses band. The next GBP 4,770 is taxed at 10.75%: GBP 512.78. The remaining GBP 4,730 sits in the higher rate band at 35.75%: GBP 1,690.98. Dividend tax is GBP 2,203.76. Her dividends are GBP 10,000, which is not over GBP 10,000, so she can ask HMRC for a tax code change by 5 October 2027 instead of filing a return, unless she is already in Self Assessment.

```oa-check
name: GB 2026-27, salary 45000 and dividends 10000, England
inputs:
  salary: 45000
  dividends: 10000
  personal_allowance: 12570
  basic_band: 37700
  dividend_allowance: 500
steps:
  - band_left: basic_band - (salary - personal_allowance)
  - nil_slice: min(dividend_allowance, dividends)
  - basic_slice: max(min(dividends, band_left) - nil_slice, 0)
  - higher_slice: dividends - nil_slice - basic_slice
  - basic_tax: round(basic_slice * 0.1075, 2)
  - higher_tax: round(higher_slice * 0.3575, 2)
  - dividend_tax: basic_tax + higher_tax
expected:
  band_left: 5270
  basic_slice: 4770
  higher_slice: 4730
  basic_tax: 512.78
  higher_tax: 1690.98
  dividend_tax: 2203.76
```

### Example 2: owner-director, salary GBP 12,570 and the rest as dividends, 2026-27

A company with one director, who is its only employee, makes GBP 60,000 of profit before paying her. Its accounting period falls inside the financial year from 1 April 2026 and it has no associated companies. It has distributable reserves that cover the dividend. She takes a salary of GBP 12,570 and the whole post-tax profit as dividends, and has no other income.

Employer NIC is 15% of (12,570 - 5,000): GBP 1,135.50. Employment Allowance is not available. Taxable profit is 60,000 - 12,570 - 1,135.50 = GBP 46,294.50. That is GBP 50,000 or less, so corporation tax is 19%: GBP 8,795.96. Dividends are GBP 37,498.54, all within the GBP 37,700 basic rate band because the salary is covered by the Personal Allowance. Dividend tax is (37,498.54 - 500) x 10.75% = GBP 3,977.34. Total tax is GBP 13,908.80, 23.18% of the profit, and she takes home GBP 50,068.54 before dividend tax. Her dividends exceed GBP 10,000, so she files an SA100 and pays GBP 3,977.34 by 31 January 2028; payments on account for 2027-28 follow unless an exception applies.

```oa-check
name: GB 2026-27, director salary 12570 plus dividends, company profit 60000
inputs:
  profit: 60000
  salary: 12570
  secondary_threshold: 5000
  dividend_allowance: 500
  basic_band: 37700
steps:
  - employer_nic: (salary - secondary_threshold) * 0.15
  - taxable_profit: profit - salary - employer_nic
  - corporation_tax: round(taxable_profit * 0.19, 2)
  - dividends: taxable_profit - corporation_tax
  - dividend_tax: round((min(dividends, basic_band) - dividend_allowance) * 0.1075, 2)
  - total_tax: corporation_tax + employer_nic + dividend_tax
  - extracted: salary + dividends
  - share_of_profit_pct: round(total_tax / profit * 100, 2)
expected:
  employer_nic: 1135.50
  taxable_profit: 46294.50
  corporation_tax: 8795.96
  dividends: 37498.54
  dividend_tax: 3977.34
  total_tax: 13908.80
  extracted: 50068.54
  share_of_profit_pct: 23.18
```

## Ask the client first

- Which tax year: the 2025-26 return being filed now (8.75% and 33.75%) or 2026-27 (10.75% and 35.75%)?
- All other income for the year, by kind, and whether adjusted net income goes over GBP 100,000.
- For an own company: the company's profit, accounting period, associated companies, and the reserves in the latest accounts.
- Whether any dividends came from foreign companies, and how much foreign tax was taken off.
- Whether the client is already in Self Assessment, and last year's bill (for payments on account).
- Any director's loan balance or dividend waiver.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 2007 s.8, dividend rates as amended | https://www.legislation.gov.uk/ukpga/2007/3/section/8 | 2026-10-26 |
| Income Tax Act 2007 s.13A, dividend nil rate | https://www.legislation.gov.uk/ukpga/2007/3/section/13A | 2026-10-24 |
| Finance Act 2026 s.4, dividend ordinary and upper rates | https://www.legislation.gov.uk/ukpga/2026/11/section/4 | 2026-10-24 |
| Companies Act 2006 s.830, distributions only out of profits | https://www.legislation.gov.uk/ukpga/2006/46/section/830 | 2026-10-26 |
| Companies Act 2006 s.847, consequences of unlawful distribution | https://www.legislation.gov.uk/ukpga/2006/46/section/847 | 2026-10-26 |
| GOV.UK, Tax on dividends and how to report | https://www.gov.uk/tax-on-dividends | 2026-10-24 |
| HMRC technical note, change to tax rates for property, savings and dividend income | https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-and-dividend-income/change-to-tax-rates-for-property-savings-and-dividend-income-technical-note | 2026-10-26 |
| GOV.UK, Rates and thresholds for employers 2026 to 2027 | https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027 | 2026-10-24 |
| GOV.UK, Employment Allowance eligibility | https://www.gov.uk/claim-employment-allowance/eligibility | 2026-10-23 |
| GOV.UK, Corporation Tax rates | https://www.gov.uk/corporation-tax-rates | 2026-10-26 |
| CTA 2010 s.455 and s.458, loans to participators | https://www.legislation.gov.uk/ukpga/2010/4/section/455 | 2026-10-26 |
| TIOPA 2010 s.9, unilateral relief | https://www.legislation.gov.uk/ukpga/2010/8/section/9 | 2026-10-23 |
| SA100 2026 form, dividend boxes | https://assets.publishing.service.gov.uk/media/69c14d07cfa346b9d4704a8d/SA100-2026.pdf | 2026-10-23 |
| Finance Act 2009 Sch 55 and Sch 56, penalties | https://www.legislation.gov.uk/ukpga/2009/10/schedule/55 | 2026-10-24 |
| HMRC, interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |

Not yet confirmed: when s.455 tax falls due and the timing for relief interest (CTA 2010 s.455(3), s.458(4)-(5)); income tax on the individual when a participator loan is written off (carried from v1.2: taxed as a dividend; ITTOIA 2005 s.415 not read); dividend waivers (v1.2 said: deed before the dividend is declared, unconditional, settlements rules under ITTOIA 2005 s.624; not re-read); UK withholding on dividends paid to non-residents; v1.2 treatments not re-read: notional distributions on accumulation units are taxable; scrip dividends taxed at the cash equivalent; dividends in specie at market value; returns of capital are not income; corporate bond returns are savings interest; UK REIT property income distributions are property income at 20%/40%/45% with no dividend allowance; GBP conversion at the payment-date rate; foreign withholding rates other than the US (see `uk-foreign-tax-and-withholding`).

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
