---
name: ghana-pit
description: >
  Use this skill to prepare or review Ghana personal income tax for tax year 2026: employees under PAYE, self-employed people, partners, landlords and investors. It covers residence, the resident bands before and after the Income Tax (Amendment) Act, 2026 (Act 1178) took effect on 1 September 2026, the 25% non-resident rate, personal reliefs, the Modified Taxation Scheme with its GHS 750,000 limit, quarterly instalments, the 30 April return, the ETAX portal and forms DT 103 and DT 104, and interest and penalties. Trigger on "Ghana income tax", "PAYE Ghana", "GRA return", "tax reliefs Ghana", "self-employed Ghana", "Modified Taxation Scheme", "presumptive tax", or any Ghana personal tax request. Employer payroll operation sits in gh-payroll-social; company tax sits in gh-corporate-income-tax.
version: 1.1
jurisdiction: GH
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - foundation
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Personal Income Tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026 (calendar year, 1 January to 31 December). Currency: Ghana cedi (GHS). Authority: Ghana Revenue Authority (GRA). Law: Income Tax Act, 2015 (Act 896) as amended, latest by Act 1178; Revenue Administration Act, 2016 (Act 915).

## Who this applies to

Individuals with employment, business or investment income. A resident is taxed on worldwide income; a non-resident on income from Ghana ([GRA](https://gra.gov.gh/domestic-tax/personal-income-tax/)).

An individual is resident for a year of assessment if they are (Act 896 s.101(1)):

- a citizen, other than one with a permanent home abroad who lives in it for the whole year;
- present in Ghana for 183 days or more in any twelve-month period that starts or ends in that year;
- a Government of Ghana employee or official posted abroad during the year; or
- a citizen temporarily absent for not more than 365 continuous days who has a permanent home in Ghana.

An individual resident under the 183-day test is resident from the start of that 183-day period (s.102(2)). Employer duties are in [gh-payroll-social](gh-payroll-social.md). Companies are in [gh-corporate-income-tax](gh-corporate-income-tax.md).

## Rates, bands and thresholds

Resident bands from 1 September 2026 (Act 1178):

| Annual chargeable income (GHS) | Monthly (GHS) | Rate | Tax year | Official URL |
|---|---|---|---|---|
| First 7,056 | First 588 | 0% | 2026, from 1 Sep | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf |
| Next 960 | Next 80 | 5% | 2026, from 1 Sep | same |
| Next 1,200 | Next 100 | 10% | 2026, from 1 Sep | same |
| Next 34,800 | Next 2,900 | 17.5% | 2026, from 1 Sep | same |
| Next 192,000 | Next 16,000 | 25% | 2026, from 1 Sep | same |
| Next 363,984 | Next 30,332 | 30% | 2026, from 1 Sep | same |
| Exceeding 600,000 | Exceeding 50,000 | 35% | 2026, from 1 Sep | same |

Resident bands to 31 August 2026 (in force from 1 January 2024, archived GRA page):

| Annual chargeable income (GHS) | Monthly (GHS) | Rate | Tax year | Official URL |
|---|---|---|---|---|
| First 5,880 | First 490 | 0% | 2024 to 31 Aug 2026 | https://web.archive.org/web/20260607073723/https://gra.gov.gh/domestic-tax/tax-types/paye/ |
| Next 1,320 | Next 110 | 5% | same period | same |
| Next 1,560 | Next 130 | 10% | same period | same |
| Next 38,000 | Next 3,166.67 | 17.5% | same period | same |
| Next 192,000 | Next 16,000 | 25% | same period | same |
| Next 366,240 | Next 30,520 | 30% | same period | same |
| Above the bands (605,000 a year, 50,416.67 a month by addition) | same | 35% | same period | same |

The archived page labels the top band "Exceeding 600,000" and "Exceeding 50,000", but its own cumulative columns reach 605,000 and 50,416.67. The cumulative columns are used here.

Other rates and thresholds:

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Non-resident individual | 25% flat | Chargeable income | 2026 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Gain on an investment asset, election | 25% | Individual may elect instead of bands (Act 1094 s.13, First Schedule para 1(3)) | 2026 | same |
| Gift outside business or employment, election | 25% | Individual may elect (First Schedule para 1(4)) | 2026 | same |
| Modified Taxation Scheme, presumptive on turnover | 3% of turnover | Turnover above GHS 20,000, up to GHS 750,000 | 2026 | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf |
| Presumptive by instalment | Fixed amount by income level and activity | Average turnover over three years not above GHS 20,000 | 2026 | https://gra.gov.gh/domestic-tax/tax-types/individual/modified-taxation-scheme/ |
| Marriage or responsibility relief | GHS 1,200 a year | Spouse, or at least two children | 2026 | https://gra.gov.gh/domestic-tax/personal-tax-relief/ |
| Child education relief | GHS 600 per child a year | Up to three children at a registered institution in Ghana; both parents cannot claim for one child | 2026 | same |
| Disability relief | 25% of income | Business or employment income only | 2026 | same |
| Old age relief | GHS 1,500 a year | Age 60 or over | 2026 | same |
| Aged dependent relative relief | GHS 1,000 a year | Relative 60 or over, up to two, not spouse or child; no double claim | 2026 | same |
| Educational relief | GHS 2,000 a year | Training for professional, technical or vocational skills | 2026 | same |
| Mortgage interest relief | Qualifying interest | Principal private residence, one building only | 2026 | same |
| Late payment interest | 125% of the Bank of Ghana policy rate, compounded monthly | Each month or part of a month | 2026 | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |

Reliefs are renewed every year; an employee only gets one with a current relief card ([GRA checklist](https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf)).

## The base

1. Work out income from each source separately: employment, business, investment ([GRA](https://gra.gov.gh/domestic-tax/personal-income-tax/)).
2. Employment income includes salary, wages, leave pay, fees, commissions, gratuities, overtime, bonuses, and benefits in cash or in kind. It excludes final withholding payments, reimbursed business expenses, equal-terms medical cover and redundancy pay.
3. Business income includes service fees, trading stock proceeds, gains on business assets and business gifts. Deduct business expenses, capital allowances and unrelieved losses of the previous five years ([Act 1094 s.3](https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf)).
4. Investment income includes dividends, interest, annuities, rent, royalties, gains on investment assets, investment gifts and lottery winnings. Final withholding payments are left out.
5. From employment income deduct SSNIT at 5.5% of basic salary, provident fund up to 16.5% of basic salary, mortgage interest on one home, and worthwhile-cause donations ([GRA PAYE](https://gra.gov.gh/domestic-tax/tax-types/paye/)).
6. Deduct personal reliefs. Apply the bands to arrive at tax, then credit tax withheld, instalments, and foreign tax credit.

Foreign tax credit: a resident other than a partnership may claim it, calculated separately for each income source, capped at the average Ghanaian rate on that foreign income ([Act 896 s.112](https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf)).

Modified Taxation Scheme: for resident individuals with business income only, from Ghana only, not VAT registered ([GRA FAQ](https://gra.gov.gh/modified-taxation/)). Presumptive options are closed to professionals with formal qualifications (lawyers, engineers, accountants), owners of several businesses or outlets, partners in registered partnerships, and those who opt out. They use the Modified Cash Basis or ordinary tax instead ([GRA](https://gra.gov.gh/domestic-tax/tax-types/individual/modified-taxation-scheme/)). The Modified Cash Basis taxes profit after allowable expenses.

## Deadlines and filing

| Obligation | Date | Form | Official URL |
|---|---|---|---|
| Estimate of tax | With the first instalment; can be revised | DT 104, revision DT 104A | https://gra.gov.gh/domestic-tax/personal-income-tax/ |
| Instalments, calendar basis period | 31 March, 30 June, 30 September, 31 December | Portal payment | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf |
| Annual return | 30 April 2027 for 2026 (four months after year end) | DT 103 | same |
| Rent income tax | Within 30 days of receipt, 8% residential, 15% other | Tax office | https://gra.gov.gh/domestic-tax/tax-types/rent-income-tax/ |
| Gain on realising an asset | Within 30 days of realisation | DT 111 | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf |
| Gift outside business or employment | Within 21 days of receipt | DT 112 | https://gra.gov.gh/domestic-tax/tax-types/gift-tax/ |
| Vehicle income tax, commercial operators | 15 January, 15 April, 15 July, 15 October | Sticker, or *222# | https://gra.gov.gh/domestic-tax/tax-types/vehicle-income-tax/ |

Each instalment is estimated tax, less tax already paid or withheld this year, divided by instalments left (s.121(3)).

**Who need not file (Act 896 s.125):** a resident with no tax payable, or whose tax relates only to employment income under PAYE, and a non-resident with no tax payable. The Commissioner-General can still ask for a return. Everyone else files, including those with several sources, business or rent income.

**Filing a DT 103 on ETAX ([GRA ITAS FAQs](https://gra.gov.gh/itas-faqs/)):**

1. Go to www.etax.gra.gov.gh. First time: Account Activation, enter TIN or Ghana Card PIN, confirm phone or email by one-time code, set a password. Update the profile; this is mandatory for new accounts.
2. Open the personal income tax return for the year. Part of it is pre-filled. Check every pre-filled figure.
3. Enter income by source, deductions, reliefs and tax already paid. Attach withholding certificates (s.124(2)(b)).
4. Submit. The individual signs the declaration that the return is complete and accurate (Act 915 s.28). A paid preparer signs too (s.29). ETAX gives an acknowledgement.
5. Start payment in ETAX and pay through Ghana.gov by Mobile Money, card, *222# or at a bank. Mobile Money, cash, transfer and card credit instantly; a third-party cheque takes up to three working days.

An extension to file must be requested before the due date and does not move the payment date (Act 915 s.30). Tax extensions to pay are capped at twelve months in total (s.47).

**Modified Taxation Scheme:** register in the MTS Taxpayer App, at a GRA office, through a field officer or a trade association, with Ghana Card, GhanaPost GPS address, phone number and sales information. Pay by *880# or the app. At year end, file actual sales in the app ([GRA](https://gra.gov.gh/domestic-tax/tax-types/individual/modified-taxation-scheme/)).

## Penalties and interest

| Failure | Consequence | Official URL |
|---|---|---|
| Late return | GHS 500 plus GHS 10 a day (500 and 10 currency points; one point is GHS 1) | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf |
| Late payment | Interest under Rates above (s.71) | same |
| Estimate under 90% of correct tax | Interest on the shortfall from the first instalment date to the return date (s.70) | same |
| No proper records | 75% of the tax for the period if deliberate; otherwise the lesser of that and GHS 250, each month | same |
| False statement | 100% of the shortfall without reasonable excuse; 30% otherwise | https://gra.gov.gh/domestic-tax/tax-offences-and-penalties/ |

Keep documents at least six years (Act 915 s.27).

## Cross-border points

- Non-residents pay 25% on Ghana income; payments subject to final withholding are not taxed again ([GRA WHT](https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/)).
- Withholding rates and treaties are in [gh-cross-border](gh-cross-border.md).
- Residents report worldwide income and claim foreign tax credit (s.112).

## Two worked examples that recompute

**Example 1: employee, September 2026 onward.** Basic GHS 8,000, allowances GHS 4,000. SSNIT 5.5% of 8,000 is 440. Chargeable income is 11,560. Tax on the first 3,668 of bands is 521.50; the remaining 7,892 at 25% is 1,973. Monthly PAYE is GHS 2,494.50. Under the old bands the same pay gave GHS 2,488.50 because the 17.5% band was wider.

```oa-check
name: Employee 12,000 a month, bands from 1 September 2026
inputs:
  basic: 8000
  allowances: 4000
steps:
  - ssnit: basic * 0.055
  - chargeable: basic + allowances - ssnit
  - low: 80 * 0.05 + 100 * 0.10 + 2900 * 0.175
  - band25: (chargeable - 3668) * 0.25
  - tax: low + band25
expected:
  chargeable: 11560.00
  tax: 2494.50
```

**Example 2: which should I use, presumptive 3% or ordinary tax?** A resident sole trader who is not a listed professional has turnover GHS 400,000 and profit GHS 120,000, using the annual bands from 1 September 2026. Presumptive tax is 3% of 400,000, GHS 12,000. Ordinary tax on 120,000: GHS 6,258 up to 44,016, plus 25% of 75,984, GHS 18,996, total GHS 25,254. Presumptive saves GHS 13,254. On this turnover ordinary tax is cheaper only if profit is below about GHS 66,984, before reliefs. Compute both.

```oa-check
name: Presumptive 3% against ordinary bands, turnover 400,000
inputs:
  turnover: 400000
  profit: 120000
steps:
  - presumptive: turnover * 0.03
  - low: 960 * 0.05 + 1200 * 0.10 + 34800 * 0.175
  - ordinary: low + (profit - 44016) * 0.25
  - saving: ordinary - presumptive
expected:
  presumptive: 12000.00
  ordinary: 25254.00
  saving: 13254.00
```

## Ask the client first

1. Resident or not: citizenship, days in Ghana, permanent home.
2. Income sources, and whether any tax was withheld as a final payment.
3. Employee only, or also business, rent or investment income.
4. For business: turnover, profession, number of outlets, VAT status.
5. Relief cards held for 2026.
6. Months of 2026 before and after 1 September, for any income earned across both periods.

Where facts are unclear, keep these defaults and flag them: unclear allowance, treat as chargeable; undocumented SSNIT, use 5.5% of stated basic; weak expense evidence, do not deduct; foreign income of a resident, include and check treaty relief; undeclared rent, treat as chargeable.

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA notice, Income Tax (Amendment) Act, 2026 (Act 1178), whole notice | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf | 2026-11-01 |
| GRA, PAYE page (2026 bands, bonus, overtime, casual rules read) | https://gra.gov.gh/domestic-tax/tax-types/paye/ | 2026-11-01 |
| GRA PAYE page, archived copy of 7 Jun 2026 on web.archive.org (band table for 2024 rates), page read in full | https://web.archive.org/web/20260607073723/https://gra.gov.gh/domestic-tax/tax-types/paye/ | 2026-11-01 |
| Income Tax Act, 2015 (Act 896), OCR of scan; ss 33, 101, 102, 112, 121, 124, 125 read | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf | 2026-11-01 |
| Income Tax (Amendment) Act, 2023 (Act 1094), whole act | https://gra.gov.gh/wp-content/uploads/2023/04/INCOME-TAX-AMENDMENT-ACT-2023-ACT-1094.pdf | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |
| GRA, Personal Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/personal-income-tax/ | 2026-11-01 |
| GRA, Personal Tax Relief page, page read in full | https://gra.gov.gh/domestic-tax/personal-tax-relief/ | 2026-11-01 |
| GRA, Modified Taxation Scheme page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/individual/modified-taxation-scheme/ | 2026-11-01 |
| GRA, Tax Offences and Penalties page, page read in full | https://gra.gov.gh/domestic-tax/tax-offences-and-penalties/ | 2026-11-01 |
| GRA, Withholding Tax page (rates table, last edited 2022), page read in full | https://gra.gov.gh/domestic-tax/tax-types/withholding-tax/ | 2026-11-01 |
| GRA, ITAS FAQs, page read in full | https://gra.gov.gh/itas-faqs/ | 2026-11-01 |
| GRA, Employee Taxes and Pensions Year End Checklist, whole document | https://gra.gov.gh/wp-content/uploads/2025/11/Taxpayer-Checklist.pdf | 2026-11-01 |
| GRA, Rent Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/rent-income-tax/ | 2026-11-01 |
| GRA, Gift Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/gift-tax/ | 2026-11-01 |
| GRA, Vehicle Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/vehicle-income-tax/ | 2026-11-01 |

Not yet confirmed: (1) The full text of Act 1178 was not on an official site opened; only the GRA notice was read, so how a 2026 annual return spreads the old and new bands across the year is not confirmed. A self-employed person should get that answered by GRA before filing. (2) Example 2 uses the new annual table as if it applied to the whole year, for comparison only. (3) Whether relief amounts changed after the GRA page was last edited in 2022. (4) Life insurance premium relief and an additional aged band, both in the old version of this skill, appear on no official page read. (5) The GHS 200 a month child relief in the old version conflicts with the GRA page and was dropped. (6) GRA page gives a 15% rate for individual gains and gift tax; Act 1094 says 25%, and the statute is followed. (7) The instalment amounts for presumptive instalment taxpayers.

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
