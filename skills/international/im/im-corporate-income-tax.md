---
name: im-corporate-income-tax
description: "Use this skill for Isle of Man income tax on companies and other corporate taxpayers for 2026/27 and accounting periods ending in it. It covers who is taxed (resident companies on worldwide income, non-resident companies on Manx income), the 0% standard rate, the 10% rate for banking business and for Manx retail business with taxable income over GBP 500,000, the 20% rate for Manx land and property and petroleum extraction, the separate 15% Domestic Top-up Tax for large groups, the loans to participators charge, withholding on payments to non-residents, the pay and file return due 12 months and 1 day after the period end, late return penalties, interest and economic substance questions. Trigger on: Isle of Man company tax, Manx corporate tax, 0% company IOM, R1C return, loans to participators, Domestic Top-up Tax Isle of Man. Out of scope: individuals (im-income-tax, im-non-resident-income-tax), payroll (im-payroll-social), UK treaty related parties (im-related-party-uk-treaty), VAT (isle-of-man-vat), formation (im-company-formation)."
jurisdiction: IM
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Isle of Man: corporate income tax (2026/27)

The Isle of Man taxes companies under the Income Tax Act 1970 (AT 3 of 1970). The rates are set by Treasury order under section 1(3A) and (3B), approved by Tynwald. Companies are taxed on an accounting period basis under the "pay and file" system that started on 6 April 2007. The authority is the Income Tax Division of the Treasury. Amounts are in pounds sterling (GBP).

Related skills: [im-income-tax](im-income-tax.md) for resident individuals and the dividends they receive, [im-non-resident-income-tax](im-non-resident-income-tax.md) for non-resident individuals, [im-related-party-uk-treaty](im-related-party-uk-treaty.md) for UK treaty related-party pricing, [im-payroll-social](im-payroll-social.md) for ITIP and National Insurance on staff, [im-company-formation](im-company-formation.md) for incorporation, and [isle-of-man-vat](../isle-of-man/isle-of-man-vat.md) for VAT.

## Who this applies to

- **Corporate taxpayers.** All companies are corporate taxpayers. The term also covers entities such as foundations and associations (Income Tax Division, Business and Corporations page).
- **Resident and non-resident companies.** A resident corporate taxpayer is taxed on its worldwide income. A non-resident corporate taxpayer is taxed on its Manx-source income only. Both are taxed at the same rates (Business and Corporations page; ITA 1970 s.2(1)(a) and (b)).
- **1931 Act and 2006 Act companies** are taxed the same way. Income tax law makes no distinction between them (New Manx Vehicles page).
- **Limited liability companies** formed under the Limited Liability Companies Act 1996: the profits are treated as the members' income for income tax (Companies Registry, Limited Liability Companies page). Use the individual skills for the members.
- **Large multinational groups.** An Isle of Man entity of a group with consolidated revenue of EUR 750 million or more in at least two of the four preceding fiscal years is also within Domestic Top-up Tax, a separate tax from income tax (Pillar 2 page; Global Minimum Tax (Pillar Two) Order 2024).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate, resident and non-resident companies | 0% | 2026/27 | PN 227/26 para 1, https://www.gov.im/media/1391759/pn-227-26-budget.pdf ; https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/corporate-tax-rates/ |
| Banking business income (deposit taking by a licensed bank) | 10% | 2026/27 | PN 227/26 para 1; corporate tax rates page; PN 124/06 |
| Retail business in the Island, taxable income from that business over GBP 500,000 (then all of it) | 10% | 2026/27 | PN 227/26 para 1; https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/ ; PN 181/13 paras 1 and 4 |
| Income from land and property in the Isle of Man | 20% | 2026/27 | PN 227/26 para 1; Business and Corporations page |
| Petroleum extraction activities or rights (from 6 April 2024) | 20% | 2026/27 | PN 227/26 para 1; ITA 1970 s.119BA |
| One-year rate on banking and retail income (history only) | 15% | 2024/25 only | corporate tax rates page |
| Domestic Top-up Tax, in-scope groups | 15% minimum effective rate on Isle of Man profits | fiscal years starting on or after 1 January 2025 | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/pillar-2-global-minimum-tax/ ; PN 227/26 |
| Domestic Top-up Tax de minimis | average Isle of Man revenue under EUR 10 million and average income under EUR 1 million | same | Pillar 2 page |
| Loans to participators charge | the individual higher rate for the year of the loan: 21% for 2026/27 | 2026/27 | ITA 1970 s.A108(3); PN 227/26 |
| Return and payment due | the day after 12 months from the end of the accounting period | all periods | ITA 1970 s.A66(3); GN58 |
| First late return penalty | GBP 250 | all periods | ITA 1970 s.112A; GN38 para 5.1.1 (SD 460/07) |
| Second late return penalty (not filed 18 months after period end) | GBP 500, on top of the first | all periods | ITA 1970 s.112B; GN38 para 5.1.1 |
| Interest on overdue tax | 5% a year | from 1 February 2009, no later change | ITA 1970 s.111A and endnote 956 (SD 961/08); PN 154/09 |
| Withholding on dividends and loan interest paid by a 0% company | 0% | current | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/withholding-tax/ |
| Withholding on Manx rent paid by a company to a non-resident company | 20% | from 6 April 2015 | withholding tax page |

## The taxable base

### Step 1: sort income by source

Rates attach to the source of income, not to the company as a whole. A company can have income at 0%, 10% and 20% in the same period (ITA 1970 s.1(3B)(a); corporate tax rates page).

- **20% income.** Taxable income from land and property in the Island. The Division lists property development, residential and commercial rental or letting, contract car parking, landfill, and mining and quarrying. From 6 April 2024 the same rate applies to petroleum extraction activities or rights (Business and Corporations page). Section 119BA treats income from searching for or extracting petroleum in the Island and its territorial sea, and from rights to that petroleum, as income from petroleum extraction activities or rights.
- **10% income, banking.** For a company holding a banking licence, income from deposit taking is taxed at 10%: all income from re-investing or using client deposits, the ancillary fees (cheque books, transaction, account and card fees, foreign exchange charges, money transmission), and income from the minimum regulatory capital. Income from funds other than client deposits (for example group-funded lending, leasing, syndicated loans) and from capital above the regulatory minimum is taxed at 0% (PN 124/06).
- **10% income, retail.** Income from retail business in the Island is taxed at 10% where the company's taxable income from that business is more than GBP 500,000 (Business and Corporations page). It is a cliff, not a band: once the retail taxable income passes GBP 500,000, all of it is taxed at 10%; at GBP 500,000 or less, all of it is at 0%. Only the retail element is counted and taxed; other income keeps its own rate. The GBP 500,000 limit is reduced proportionately where associated companies also carry on retail business in the Island, and where the accounting period is shorter than 12 months. The computation splits retail profit from other income unless the limit will clearly never be met (PN 181/13 paras 1, 3 and 4).
- **0% income.** Everything else.

### Step 2: apportion across a rate change

Rates are set for years of assessment from 6 April to 5 April, but companies are assessed on their accounting period. Where a rate changes inside a period, profits may need to be apportioned so the right rate applies to each part (corporate tax rates page). The 2026/27 rates are the same as 2025/26, so a period straddling 6 April 2026 needs no split for rate purposes (PN 227/26 para 1).

An accounting period for the return cannot exceed 12 months. A longer period of account is split into two returns (GN58).

### Step 3: loans to participators

If a corporate taxpayer lends or advances money to an individual liable to Manx income tax who is a participator, an officer, or an associate of either, other than in the ordinary course of a money-lending business, an amount is assessed on the company as if it were income tax for the accounting period of the loan. The amount is the loan multiplied by the individual higher rate for the year of assessment in which the loan is made (ITA 1970 s.A108(2), (3)). For 2026/27 that rate is 21% (PN 227/26 para 1). The Division's Business and Corporations page still says 22%. That was the higher rate from 6 April 2024; it has been 21% since 6 April 2025, and the Act ties the charge to the rate in force, so use 21%. The charge does not apply to a loan at a normal commercial rate by a company whose ordinary business includes lending and which is authorised by a financial regulator to lend (s.A108(5)). The amount charged is not deductible (s.A108(6)). Sections B108 to J108 deal with repayment and release.

### Step 4: distributions

There is no company-level charge on distributions now. The Distributable Profits Charge was repealed for accounting periods starting on or after 6 April 2008. The Attribution Regime for Individuals that replaced it was abolished for accounting periods starting after 6 April 2012 (Distributable Profits Charge page; Attribution Regime for Individuals page). A Manx-resident individual shareholder is taxed on dividends received: see [im-income-tax](im-income-tax.md). The Division publishes a composite distribution voucher for companies to give shareholders (Pay and File page).

### Step 5: Domestic Top-up Tax

For in-scope groups, Domestic Top-up Tax brings the effective rate on Isle of Man profits to 15% (PN 227/26, note to para 1). It follows the OECD GloBE rules closely, it is separate from income tax, and the entity still pays income tax in the normal way. Each Isle of Man entity has its own liability; the allocation inside the group follows articles 17 and 18 of the 2024 Order. An Isle of Man ultimate or intermediate parent may also owe Multinational Top-up Tax (an income inclusion rule) on low-taxed profits outside the Island (Pillar 2 page).

For fiscal years beginning on or after 1 January 2026 the Global Minimum Tax (Pillar Two) (Amendment) Order 2026 (SD 2026/0127, approved by Tynwald on 23 July 2026) brings in the OECD Side-by-Side Package: a Side-by-Side Safe Harbour (so far only the United States regime is recognised) and a Substance-based Tax Incentive Safe Harbour. It does not stop the Island charging Domestic Top-up Tax on the Isle of Man profits of an in-scope group, wherever the ultimate parent is (Pillar 2 update, 24 June 2026; Order articles 2 and 3).

## Deadlines and filing

- **Return.** Every corporate taxpayer delivers a return of its whole income for each accounting period by the due day: the day after the end of 12 months from the end of the period (ITA 1970 s.A66(1), (3)). The return includes a computation of the tax payable (s.A66(4)), the economic substance information the Assessor asks for (s.A66(4A)), and Pillar 2 information (s.A66(4B)). Example: a period ending 31 December 2026 is due on 1 January 2028.
- **Payment.** Tax is due on the same day as the return. The computation in the return is treated as the assessment, so no separate assessment notice is issued (GN58; Pay and File page).
- **Online filing.** Returns for accounting periods ending on or after 5 April 2015 must be filed online, by the company or its tax agent, unless the company is exempt or the Assessor grants an exemption (ITA 1970 s.B66; Online Filing page). Guidance Note GN58 covers periods ending on or after 31 December 2019. The R1C form has Pillar 2 questions for periods ending on or after 31 December 2024 (Pillar 2 page).
- **Companies with no income** still deliver the return and pick the reason in it: dormant, non-income-producing asset holding, flat management or registered charity (GN58).
- **Domestic Top-up Tax.** In-scope groups appoint a Domestic Filing Entity (form P1) and register through the Pillar 2 online service. The registration deadline is set by article 29 of the Order: ordinarily 12 months after the start of the first in-scope fiscal year, earlier for an entity being wound up or leaving the Island, and not earlier than 1 January 2026. Penalties can be charged for late registration (Pillar 2 page; Pillar 2 update, 5 November 2025). The Domestic Filing Entity must enrol for the online service even where an agent does the work. The first Domestic and Multinational Top-up Tax returns are due by 31 March 2027 for groups with a fiscal year ending 31 December 2025; the Division expects the online return function in November 2026 (Pillar 2 update, 13 October 2026).

## Penalties and interest

- **Late return.** A company that has not delivered its return by the day after 12 months from the period end is liable to a civil penalty (ITA 1970 s.112A). A further penalty applies if the return is still missing on the day after 18 months from the period end (s.112B). The Treasury sets the amounts by order (s.112E): GBP 250 and GBP 500, GBP 750 in all (GN38 para 5.1.1, citing the Income Tax (Corporate Taxpayers) (Civil Penalties) Order 2007, SD 460/07). The amounts go up where the company was liable to a penalty for each of the two preceding accounting periods (s.112F).
- **Reasonable excuse and mitigation.** No penalty arises with a reasonable excuse. Lack of funds is not one, and relying on someone else is not one either (s.112D). The Assessor or the Commissioners may reduce a penalty, but may not take into account lack of funds, absence of lost tax, or good faith (s.112C). The penalty is not deductible (s.112H(5)).
- **Criminal offence.** Failing to deliver the return within 24 months of the period end is an offence: a fine up to level 5 or up to 6 months' custody, or both. An officer who consented or was neglectful is also liable (s.112I).
- **Interest.** Tax charged carries interest at the prescribed rate from the date it is due until payment (s.111A(1), (1A)(c)). The consolidated Act notes the prescribed rate as 5% a year (endnote 956, SD 961/08). Interest is not deductible (s.111A(3)).

## Cross-border points

- **Non-resident companies** pay tax only on Manx-source income, at the same rates as resident companies (Business and Corporations page).
- **Payments to non-residents.** A company paying a non-resident looks at the type of payment, its own tax rate and the recipient (Withholding Tax page). The Division's table shows:
  - to a non-resident company: Manx rent 20% (from 6 April 2015); all other payments 0%;
  - to a non-resident individual: dividends 0%; loan interest 0%, but 20% where the paying company has Manx land and property income taxed at 20%; directors' fees 0%, but tax is due in certain cases where duties are performed in the Island.
  The same table shows 20% on Manx rent and other Manx income paid to non-resident individuals. That figure predates the current 21% non-resident rate. For payments to individuals follow [im-non-resident-income-tax](im-non-resident-income-tax.md), which uses 21% under notice N15.
- **UK treaty.** For transfer pricing with UK associated enterprises see [im-related-party-uk-treaty](im-related-party-uk-treaty.md).
- **Economic substance.** Part 6A of the Income Tax Act 1970 holds the economic substance rules. They were extended to partnerships and LLCs by a change Tynwald approved on 16 June 2021. The return asks for the substance information (s.A66(4A)). The joint Guernsey, Isle of Man and Jersey guidance (version 2, 22 November 2019) is issued under s.80M (Economic Substance page).
- **Pillar Two.** The Island applies a domestic top-up tax and an income inclusion rule from fiscal years starting on or after 1 January 2025. A group entity that leaves the Island or winds up has cessation obligations from 1 January 2025 (form P4) (Pillar 2 page).

## Worked examples

### Example 1: trading company that also lets a Douglas office

A resident 2006 Act company has a 31 December 2026 year end. Its trading profit is GBP 400,000 and it has net rental income of GBP 50,000 from an office it owns in Douglas. The trading profit is taxed at 0% and the rental income at 20%. Tax is GBP 10,000. The return and the payment are due on 1 January 2028.

```oa-check
name: IM company, 0% trading profit plus 20% Manx rental income (period ending 31 Dec 2026)
inputs:
  trading_profit: 400000
  manx_rental_income: 50000
steps:
  - tax_trading: trading_profit * 0
  - tax_rental: manx_rental_income * 0.20
  - tax: tax_trading + tax_rental
expected:
  tax_trading: 0.00
  tax_rental: 10000.00
  tax: 10000.00
```

### Example 2: bank with a loan to a director, filed late

A licensed bank has banking income of GBP 1,200,000 and other income of GBP 80,000 taxed at 0% for the year to 31 March 2027. In June 2026 it lent GBP 30,000 interest-free to a Manx-resident director, outside its ordinary lending business, so the commercial-rate exclusion does not apply. Tax on banking income at 10% is GBP 120,000. The loans to participators charge is 21% of GBP 30,000, GBP 6,300. The total of GBP 126,300 is due on 1 April 2028. The return goes in on 15 October 2028, after the 18-month point (1 October 2028), so both late return penalties apply: GBP 750. Interest runs on the unpaid tax from 1 April 2028.

```oa-check
name: IM bank, 10% banking income, loans to participators charge, late penalties (year to 31 Mar 2027)
inputs:
  banking_income: 1200000
  other_income: 80000
  loan_to_director: 30000
  higher_rate: 0.21
  first_penalty: 250
  second_penalty: 500
steps:
  - tax_banking: banking_income * 0.10
  - tax_other: other_income * 0
  - ltp_charge: loan_to_director * higher_rate
  - tax_due: tax_banking + tax_other + ltp_charge
  - penalties: first_penalty + second_penalty
expected:
  tax_banking: 120000.00
  ltp_charge: 6300.00
  tax_due: 126300.00
  penalties: 750.00
```

### Example 3: Manx retailer just over the GBP 500,000 limit

A resident company with no associated companies runs shops in the Island. For the year to 31 December 2026 its taxable income from the retail business is GBP 520,000 and it also has GBP 30,000 of non-retail investment income. Because retail taxable income is over GBP 500,000, all GBP 520,000 is taxed at 10%, not just the GBP 20,000 above the limit: tax GBP 52,000. The investment income stays at 0%. Had retail taxable income been GBP 500,000, the tax would be nil (PN 181/13 para 4, examples 2 and 3).

```oa-check
name: IM retailer, 10% on all retail income once over GBP 500,000 (year to 31 Dec 2026)
inputs:
  retail_income: 520000
  investment_income: 30000
steps:
  - tax_retail: retail_income * 0.10
  - tax_other: investment_income * 0
  - tax: tax_retail + tax_other
expected:
  tax_retail: 52000.00
  tax: 52000.00
```

## Ask the client first

1. Where is the company incorporated and where is it managed? Is it a 1931 Act or 2006 Act company, an LLC or a foreign company?
2. Which income sources does it have: banking, Manx retail (and how much taxable income from it), Manx land and property, petroleum, or other?
3. What is the accounting period end, and when were the last two returns filed?
4. Has the company lent or advanced money to any shareholder, director or their family during the period?
5. Is it part of a group with consolidated revenue of EUR 750 million or more?
6. Does it carry on a relevant activity for economic substance, and what does it pay to non-residents (rent, interest, directors' fees)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 1970 (AT 3 of 1970), consolidated text [62], ss.1, 2, A66, B66, A108, 111A, 112A to 112I, 119BA, Part 6A | https://legislation.gov.im/cms/images/LEGISLATION/PRINCIPAL/1970/1970-0003/1970-0003_62.pdf | 2026-10-30 |
| Practice Note PN 227/26, Budget 2026 income tax and National Insurance proposals (17 February 2026), para 1 | https://www.gov.im/media/1391759/pn-227-26-budget.pdf | 2026-10-30 |
| Income Tax Division, Business and Corporations | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/ | 2026-10-30 |
| Income Tax Division, Corporate Tax Rates | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/corporate-tax-rates/ | 2026-10-30 |
| Practice Note PN 124/06, Budget 2006: Banking Business (21 February 2006) | https://www.gov.im/media/511816/pn12406.pdf | 2026-10-30 |
| Practice Note PN 181/13, retail business 10% rate | https://www.gov.im/media/365703/pn18113.pdf | 2026-10-30 |
| Practice Note PN 222/24, Budget 2024 (2024/25 15% rate, petroleum) | https://www.gov.im/media/1382355/pn-222-24-budget-2024.pdf | 2026-10-30 |
| Practice Note PN 154/09, Interest and Repayment Supplement: Change of Rate (30 January 2009) | https://www.gov.im/media/97344/pn154.pdf | 2026-10-30 |
| Pillar 2 update: Registration deadline (5 November 2025) | https://www.gov.im/media/1390706/pillar-2-update-registration-deadline.pdf | 2026-10-30 |
| Pillar 2 update: Side-by-Side Package of measures (24 June 2026) | https://www.gov.im/media/1393642/pillar-2-update-side-by-side-measures.pdf | 2026-10-30 |
| Pillar 2 update: Compulsory enrolment for Pillar 2 online service (13 October 2026) | https://www.gov.im/media/1394700/pillar-2-update-compulsory-enrolment-for-pillar-2-online-service.pdf | 2026-10-30 |
| Global Minimum Tax (Pillar Two) (Amendment) Order 2026, SD 2026/0127 | https://www.gov.im/media/1394545/global-minimum-tax-pillar-two-amendment-order-2026.pdf | 2026-10-30 |
| Income Tax Division, Pay and File | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/pay-and-file/ | 2026-10-30 |
| Income Tax Division, Online Filing | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/online-filling/ | 2026-10-30 |
| Income Tax Division, Withholding Tax | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/withholding-tax/ | 2026-10-30 |
| Income Tax Division, Distributable Profits Charge | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/distributable-profits-charge/ | 2026-10-30 |
| Income Tax Division, Attribution Regime for Individuals | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/attribution-regime-for-individuals/ | 2026-10-30 |
| Income Tax Division, New Manx Vehicles (2006 Act Companies) | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/business-and-corporations/new-manx-vehicles-2006-act-companies/ | 2026-10-30 |
| Income Tax Division, Pillar 2 Global Minimum Tax | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/pillar-2-global-minimum-tax/ | 2026-10-30 |
| Income Tax Division, Economic Substance | https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/economic-substance/ | 2026-10-30 |
| Guidance Note GN38, The Pay and File Income Tax System for Companies (November 2009), section 5.1.1 | https://www.gov.im/media/365163/gn38_november_09_final_02112009.pdf | 2026-10-30 |
| Guidance Note GN58, Company Income Tax Return (version 3.0, 31 December 2024) | https://www.gov.im/media/1386923/gn58-company-income-tax-return-20241231_compressed.pdf | 2026-10-30 |
| Companies Registry, Limited Liability Companies | https://www.gov.im/categories/business-and-industries/companies-registry/registries/limited-liability-companies/ | 2026-10-30 |

Not yet confirmed: the text of the Treasury order fixing the 2026/27 company rates (the rates here come from PN 227/26 and the Division's pages, which agree); the current text of SD 460/07 and the higher amounts for successive defaults under s.112F (the GBP 250 and GBP 500 come from GN38, issued 2009); the statutory test of company residence; the exact formula for reducing the GBP 500,000 retail limit for associated companies; the voluntary election by a 0% company to pay 10% (the old version of this skill listed it; the only official mention found is GN41 section 4.4 under the abolished Attribution Regime); loss relief, capital allowances and group relief (ITA 1980 Schedule 2); the Domestic Top-up Tax computation, payment dates and return due dates after the first year in the Global Minimum Tax (Pillar Two) Order 2024 (Order not read).

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
