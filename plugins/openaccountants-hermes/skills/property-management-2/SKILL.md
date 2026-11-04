---
name: property-management-2
description: "A short working routine for UK rental income of individual landlords in tax year 2026/27 (6 April 2026 to 5 April 2027), reported on the SA105 UK property pages or through Making Tax Digital. Covers gross rent, repairs versus improvements, replacement of domestic items, the residential finance cost restriction and its 20% tax reduction, the GBP 1,000 property allowance, Rent-a-Room (GBP 7,500), former furnished holiday lets after the April 2025 abolition, MTD thresholds (GBP 50,000 from April 2026, GBP 30,000 from April 2027) and the separate property rates of 22%, 42% and 47% enacted for 2027/28. Trigger phrases: landlord tax UK, mortgage interest rental, section 24, SA105 quick, rental profit 2026/27, property income rates 2027. Out of scope, see siblings: the full SA105 box map, losses, joint ownership and Form 17 (uk-rental-sa105), non-resident landlords (uk-non-resident-sa109), company-owned property (uk-corporation-tax)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/property-management-2"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Property Management in United Kingdom: Rental Income Tax (SA105)

> Source-cited draft: not reviewed by an accountant.

This skill is a short routine for computing UK rental profit and tax for individual landlords. Tax year in force: **2026/27** (6 April 2026 to 5 April 2027). Returns filed now are for 2025/26, where the same rules and rates apply. Changelog v1.1 (2026-10-23): figures moved to 2026/27 with the year named; finance cost restriction credited to ITTOIA 2005 s.272A and ss.274A to 274C; MTD thresholds and the enacted 2027/28 property rates added; worked example completed; accountant attribution removed; Sources table added. The full method, box map, losses and joint ownership are in `uk-rental-sa105`.

## Who this is for

Individual landlords letting UK residential property and reporting on SA105 with their SA100, or through MTD for Income Tax. Not covered: non-resident landlords beyond a pointer (`uk-non-resident-sa109`), and property held in a company (`uk-corporation-tax`).

## Before you start, ask the client

- Is the property jointly owned, and in what shares?
- Is the landlord UK resident? (Non-residents fall under the Non-resident Landlord Scheme.)
- Did any "repair" restore the property, or improve it beyond its original condition?
- Were any furniture or appliances replaced this year, and were they first purchases or replacements?
- What is the landlord's other income? (It decides the rate band and caps the finance cost reduction.)
- Is gross rental income above or below GBP 1,000? Is qualifying income (self-employment plus property) above the MTD thresholds?

## The method, step by step

1. **Total gross rental income** for the tax year: rent, deposits retained in the year, and platform payouts. Leave out refundable deposits still held and capital receipts.
2. **Sort every cost:** revenue expense, repair, capital improvement (not deductible against rent), or replacement of a domestic item.
3. **Residential finance costs are not deducted** (ITTOIA 2005 s.272A). Instead the landlord gets a tax reduction of **20%** of the lowest of: finance costs (plus any brought forward), property profits, and adjusted total income above the Personal Allowance. Unused costs carry forward. The reduction cannot create a refund.
4. **Property allowance:** GBP 1,000 a year. It replaces all expenses (never both), cannot create a loss, and cannot be used with the finance cost reduction or on Rent-a-Room income.
5. **Rent-a-Room:** for a room in the landlord's own home, up to GBP 7,500 a year is tax-free (GBP 3,750 if the income is shared).
6. **Former furnished holiday lets:** the FHL regime was abolished for income tax from 6 April 2025. These properties now sit in the ordinary property business: finance costs move to the 20% reduction, and FHL losses carried forward are set against the property business.
7. **Tax** the profit at the landlord's 2026/27 rates (20%, 40%, 45% for England, Wales and Northern Ireland; Scotland in `uk-scottish-income-tax`), then deduct the finance cost reduction.

## The traps

- Deducting mortgage interest as an expense instead of taking the 20% reduction.
- Treating an improvement as a repair, or a like-for-like repair as capital.
- Claiming the original purchase of a domestic item: only a replacement qualifies.
- Combining the property allowance with expenses, with the finance cost reduction, or with Rent-a-Room.
- Applying the 2027/28 property rates to 2026/27: they start on 6 April 2027.

## Rates, thresholds and deadlines

| What | Value | Year | Source |
| --- | --- | --- | --- |
| Personal Allowance; basic, higher, additional rates | GBP 12,570; 20% to GBP 50,270, 40% to GBP 125,140, 45% above | 2026/27 | https://www.gov.uk/income-tax-rates |
| Property allowance | GBP 1,000 | 2026/27 | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income |
| Rent-a-Room threshold | GBP 7,500 (GBP 3,750 if shared) | 2026/27 | https://www.gov.uk/rent-room-in-your-home/the-rent-a-room-scheme |
| Residential finance costs | Not deductible; tax reduction at 20% | 2026/27 | https://www.legislation.gov.uk/ukpga/2005/5/section/272A ; https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies |
| FHL regime | Abolished from 6 April 2025 | 2025/26 onward | https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/abolition-of-the-furnished-holiday-lettings-tax-regime |
| Property rates | Property basic 22%, higher 42%, additional 47% | 2027/28 (enacted) | https://www.legislation.gov.uk/ukpga/2026/11/section/7 |
| Finance cost reduction from 2027/28 | At the property basic rate, 22% (announced) | 2027/28 | https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-dividend-income/changes-to-tax-rates-for-property-savings-dividend-income |
| Self Assessment deadlines | Paper 31 October, online 31 January after the tax year (2025/26: 31 October 2026 and 31 January 2027) | 2025/26 return | https://www.gov.uk/self-assessment-tax-returns/deadlines |
| MTD for Income Tax | Qualifying income over GBP 50,000 in 2024/25: from 6 April 2026; over GBP 30,000 in 2025/26: from 6 April 2027; over GBP 20,000 in 2026/27: from 6 April 2028 | 2026/27 to 2028/29 | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax |

## Worked example

A landlord with a GBP 30,000 salary (which uses her Personal Allowance) lets one flat in England in 2026/27. Rent GBP 12,000. Mortgage interest GBP 4,000. Agent fees GBP 1,200. Insurance GBP 300. Repairs GBP 800.

Profit is rent less agent fees, insurance and repairs: GBP 9,700. The mortgage interest is not deducted. All the profit falls in her basic rate band, so tax at 20% is GBP 1,940. The finance cost reduction is 20% of the lowest of GBP 4,000 (finance costs), GBP 9,700 (property profit) and GBP 27,130 (adjusted total income of GBP 39,700 less the GBP 12,570 Personal Allowance): 20% of GBP 4,000, GBP 800. Tax on the rental profit: GBP 1,140.

For comparison only: the same figures in 2027/28 at the enacted 22% property basic rate, with the announced 22% reduction, give GBP 2,134 less GBP 880, GBP 1,254.

```oa-check
name: Basic rate landlord, finance cost reduction (2026/27)
inputs:
  rent: 12000
  mortgage_interest: 4000
  agent_fees: 1200
  insurance: 300
  repairs: 800
  salary: 30000
  personal_allowance: 12570
steps:
  - profit: rent - agent_fees - insurance - repairs
  - tax_before_reduction: profit * 0.20
  - ati_above_pa: salary + profit - personal_allowance
  - reduction_base: min(mortgage_interest, profit, ati_above_pa)
  - reduction: reduction_base * 0.20
  - tax_due: tax_before_reduction - reduction
  - tax_2027_28: profit * 0.22 - reduction_base * 0.22
expected:
  profit: 9700.00
  tax_before_reduction: 1940.00
  ati_above_pa: 27130.00
  reduction: 800.00
  tax_due: 1140.00
  tax_2027_28: 1254.00
```

## Sources

| Source | URL | Read on |
|---|---|---|
| GOV.UK, Income Tax rates 2026/27 | https://www.gov.uk/income-tax-rates | 2026-10-23 |
| ITTOIA 2005 s.272A (restriction of residential finance costs) | https://www.legislation.gov.uk/ukpga/2005/5/section/272A | 2026-10-23 |
| ITTOIA 2005 s.274A (tax reduction for finance costs) | https://www.legislation.gov.uk/ukpga/2005/5/section/274A | 2026-10-23 |
| GOV.UK, Changes to tax relief for residential landlords: how it is worked out | https://www.gov.uk/guidance/changes-to-tax-relief-for-residential-landlords-how-its-worked-out-including-case-studies | 2026-10-23 |
| GOV.UK, Tax-free allowances on property and trading income | https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income | 2026-10-23 |
| GOV.UK, Rent a Room Scheme | https://www.gov.uk/rent-room-in-your-home/the-rent-a-room-scheme | 2026-10-23 |
| GOV.UK, Abolition of the furnished holiday lettings tax regime | https://www.gov.uk/government/publications/furnished-holiday-lettings-tax-regime-abolition/abolition-of-the-furnished-holiday-lettings-tax-regime | 2026-10-23 |
| Finance Act 2026 s.7 (property rates for 2027/28) | https://www.legislation.gov.uk/ukpga/2026/11/section/7 | 2026-10-23 |
| HM Treasury, Changes to tax rates for property, savings and dividend income | https://www.gov.uk/government/publications/changes-to-tax-rates-for-property-savings-dividend-income/changes-to-tax-rates-for-property-savings-dividend-income | 2026-10-23 |
| GOV.UK, Self Assessment deadlines | https://www.gov.uk/self-assessment-tax-returns/deadlines | 2026-10-23 |
| GOV.UK, Find out if and when you need to use MTD for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-23 |

Not yet confirmed: the legislation that moves the finance cost reduction to 22% for 2027/28 (HM Treasury says it "will be provided"; ITTOIA s.274A read on 2026-10-23 shows no Finance Act 2026 change); whether the Scottish and Welsh property rates for 2027/28 follow the same figures.

*This is a working paper aid, not a filed return. Review and sign off before filing with HMRC.*

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `property-management-2` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/property-management-2. If neither is available, confirm every figure against the official source pages cited above before relying on it.
