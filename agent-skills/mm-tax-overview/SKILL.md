---
name: mm-tax-overview
description: "Overview of Myanmar's tax system for FY 2026-27 (1 April 2026 to 31 March 2027). Taxes are set each year by the Union Taxation Law (2026 edition in force 1 April 2026) and run by the Internal Revenue Department. Individual income tax 0% to 25% with a 4.8 million kyat salary exemption, company tax 22% (17% for listed companies), capital gains 10%, commercial tax (5% general, in place of VAT), specific goods tax, social security, stamp duty. Use to orient any Myanmar tax question and pick the right Myanmar skill."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mm-tax-overview"
  jurisdiction: "MM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Myanmar Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone with a Myanmar tax question for FY 2026-27. The financial year runs 1 April to 31 March; the FY 2025-26 reporting period ran from 1 April 2025 to 31 March 2026 (IRD notice of 28 April 2026). Rates are set yearly by the Union Taxation Law; for FY 2026-27 the Union Taxation Law 2026 (in force 1 April 2026). Taxes are administered by the Internal Revenue Department (IRD), Ministry of Finance and Revenue; currency is the kyat.

| Tax | Skill |
|---|---|
| Individual income tax, salary, rent, capital gains | [mm-income-tax](mm-income-tax.md) |
| Company income tax | [mm-corporate-income-tax](mm-corporate-income-tax.md) |
| Commercial tax (instead of VAT or GST) | [myanmar-ct](myanmar-ct.md) |
| Payroll and social security | [mm-payroll-social](mm-payroll-social.md) |
| Company formation | [myanmar-company-formation-entity-choice](myanmar-company-formation-entity-choice.md) |
| Specific goods tax, customs duty, stamp duty | Not covered: refer |

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Individual income tax | 0% to 25% in 6 brackets after reliefs; salary up to 4.8 million kyats a year exempt | FY 2026-27 | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf |
| Company income tax | 22% of net profit; 17% for Yangon Stock Exchange listed companies | FY 2026-27 | same |
| Capital gains | 10% (individuals and companies outside oil and gas); exempt if assets sold in the year total 10 million kyats or less | FY 2026-27 | same |
| Rental income | 10% after reliefs, separately | FY 2026-27 | same |
| Commercial tax | 5% general rate; 3% hotels and tourism, gold, construction for sale; 15% internet; 0% exports; threshold 50 million kyats | FY 2026-27 | same |
| New MSME exemption | Net profit up to 20 million kyats a year exempt for 3 years | FY 2026-27 | same |
| Social security | Employer 2% plus 1% injury, worker 2% (workers 60 or under at entry) | 2026 | https://www.ssb.gov.mm/Portal/assets/attachment/Contribution_Calculation%28Formula%29.pdf |
| Annual returns (income tax, salary statement, CT) | Within 3 months after year end: 30 June | FY 2026-27 | https://www.ird.gov.mm/announcement-lists/96 |

## The base

- **Residence.** Resident citizens and resident foreigners (183 days) are taxed on worldwide income; non-resident foreigners on Myanmar income with no reliefs (Income Tax Law s 3).
- **Companies** formed in Myanmar are taxed on worldwide net profit at 22%; reliefs do not apply.
- **Commercial tax** is a turnover tax on goods, imports and services, with set-off of CT paid on inputs under the regulations; there is no VAT or GST.
- **Specific goods tax** applies to listed goods (tobacco, liquor, vehicles, fuel, gems and others) in price tiers, separately from CT.

## Deadlines and filing

- Monthly: CT within 10 days after month end; salary tax withheld; SSB by the 15th.
- Quarterly: CT return within one month after the quarter; advance income tax within 10 days after the quarter.
- Annually: income tax return, annual salary statement and annual CT return by 30 June.
- Capital gains: within 30 days of the sale.
- Filing in person, by post or through the e-Filing Management System; Large and Medium Taxpayer Offices file electronically.

## Penalties and interest

Late returns: the greater of 5% of tax owing plus 1% a month and K 100,000 (IRD notice of 28 April 2026). Advance tax short paid: 10%. CT defaults: 10% fines under the Commercial Tax Law s 21. SSB late payment: 10% per 30 days.

## Cross-border points

Citizens residing abroad pay 10% on foreign non-salary income and the lesser of brackets or 2% on foreign salary. Non-residents claim treaty relief on Form IRD (IT)-11-Q1 (Notification 108/2023). Exports bear 0% CT (electricity 8%, crude oil 5%). Imports bear 5% CT on landed value, collected by Customs.

## Two worked examples that recompute

**Example 1. Landlord, rent 30,000,000 kyats a year, no other income.** Basic relief 20% = 6,000,000; tax 10% of 24,000,000 = 2,400,000. Rent is under 50 million, so no commercial tax.

```oa-check
name: Myanmar rental income 30m kyats
inputs:
  rent: 30000000
steps:
  - relief: min(rent * 0.20, 10000000)
  - income_tax: (rent - relief) * 0.10
  - ct: 0
  - total: income_tax + ct
expected:
  income_tax: 2400000.00
  total: 2400000.00
```

**Example 2 (decision). Sell shares worth 9,500,000 kyats this year or 12,000,000 kyats (gain 3,000,000)?** If total assets sold in the year are 10 million kyats or less, the gain is exempt even if there is one. Selling 9,500,000: tax nil. Selling 12,000,000 with a gain of 3,000,000: tax 10% = 300,000, paid within 30 days. The figure that decides is the 10 million kyat total value per year.

```oa-check
name: Myanmar capital gains 10 million exemption
inputs:
  value_small: 9500000
  value_large: 12000000
  gain_large: 3000000
steps:
  - tax_small: 0
  - tax_large: gain_large * 0.10
  - over_threshold: value_large - 10000000
expected:
  tax_large: 300000.00
  over_threshold: 2000000
```

## Ask the client first

1. Individual, company, cooperative or foreign business?
2. Citizen, resident foreigner (183 days) or non-resident?
3. Which income: salary, business, rent, capital gains, foreign income?
4. Sales of goods or services, and are they over 50 million kyats a year?
5. Any specific goods, oil and gas, SEZ or MIC investment?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Union Taxation Law 2026, English (IRD) | Read for the in-force date and the income tax, capital gains, rental, MSME and commercial tax rates | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf | 2026-11-14 |
| IRD notice to file returns (28 April 2026) | Read for the April to March year, 30 June due date, filing methods and penalty | https://www.ird.gov.mm/announcement-lists/96 | 2026-11-14 |
| SSB contribution calculation sheet | Read for the SSB rates | https://www.ssb.gov.mm/Portal/assets/attachment/Contribution_Calculation%28Formula%29.pdf | 2026-11-14 |
| Income Tax Law (IRD English text) | Read for residence and the 30-day capital gains payment | https://www.ird.gov.mm/storage/laws/68b55a57275e0-Income%20Tax%20Law%20(1).pdf | 2026-11-14 |

Not yet confirmed: stamp duty rates (the IRD individual page mentions 4% on property purchases valued by the valuation committee and lease rates, but the Stamp Act schedule was not opened); specific goods tax rates by tier; customs duty; the list of double taxation agreements.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mm-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mm-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
