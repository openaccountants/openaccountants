---
name: alabama-sales-tax
description: "Use this skill whenever asked about Alabama sales tax, Alabama use tax, Alabama sales tax nexus, ADOR sales tax filing, self-administered city taxes in Alabama, or Alabama grocery food taxation. Trigger on phrases like \"Alabama sales tax\", \"AL sales tax\", \"ADOR\", \"Code of Ala. §40-23\", \"Alabama local tax\", \"Alabama grocery tax\", \"self-administered cities Alabama\", or any request involving Alabama state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/alabama-sales-tax"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama Sales Tax

> **Source-cited draft.** Built from ALDOR's State Sales and Use Tax Rates page, Sales Tax page, Sales and Use Tax Incentives page, the food-rate notices (Acts 2023-554, 2025-305 and 2026-604) and the remote-seller registration FAQ, read 2026-11-13. No accountant has reviewed it. Do not advise a client from it without review by a qualified Alabama professional.

See also: `us-sales-tax` (load first), `alabama-cross-border` (remote sellers), `al-corporate-income-tax`.

## Who this applies to

- **Every retailer** selling tangible personal property at retail in Alabama: the tax applies to "gross proceeds from sale of all taxable items for consumption or other use to consumers ... within Alabama" (ALDOR Sales Tax page, Application). The sales and use tax law is found in Chapter 23, Title 40, Code of Alabama 1975 (ALDOR Sales and Use Tax Incentives page).
- **Remote and out-of-state sellers:** economic nexus over the $250,000 retail-sales threshold, collecting from October 1, 2018; eligible remote sellers may instead join the Simplified Sellers Use Tax (SSUT) program at a flat 8% (ALDOR remote-seller FAQ).
- **Local tax administration:** "Some of the local sales taxes are collected by ALDOR, third party administrators, and others are self-administered" (ALDOR Sales Tax page), so a seller may need to register with self-administered cities and counties individually.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| State general rate | 4% | 2026 | [ALDOR State Sales and Use Tax Rates](https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/) |
| Food/grocery (SNAP definition, 7 U.S.C. § 2011) | 2% from September 1, 2025 (3% from September 1, 2023 to August 31, 2025) | 2026 | [ALDOR State Sales and Use Tax Rates](https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/) |
| Food: temporary suspension of the state rate (Act 2026-604) | State tax on food suspended May 1, 2026 to June 30, 2026; city and county food rates not affected | 2026 | [ALDOR notice, temporary suspension on food](https://www.revenue.alabama.gov/notice-temporary-suspension-of-state-sales-and-use-tax-on-food/) |
| Automotive vehicles, truck trailers, semi-trailers, house trailers | 2% (of net trade difference) | 2026 | [ALDOR State Sales and Use Tax Rates](https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/) |
| Manufacturing and mining machinery | 1.5% | 2026 | same |
| Farm machinery | 1.5% (of net trade difference) | 2026 | same |
| Vending machines, food products | 3% | 2026 | same |
| Vending machines, all other | 4% | 2026 | same |
| Amusement sales and use | 4% | 2026 | same |
| Manufactured home set-up materials and related supplies | 2% | 2026 | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Simplified Sellers Use Tax (§ 40-23-193(a)) | 8% flat | 2026 | [ALDOR State Sales and Use Tax Rates](https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/) |
| Rental or leasing tax (§ 40-12-222): general / automotive / linens and garments | 4% / 1.5% / 2% | 2026 | same |
| Local sales taxes | Counties and municipalities may levy local sales taxes "ranging in rate between .10% to 5%" | 2026 | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Remote-seller economic nexus | Over $250,000 of total retail sales delivered into Alabama the previous calendar year | 2026 | [ALDOR remote-seller FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/) |

**Food note.** Act 2023-554 cut the state food rate from 4% to 3% on September 1, 2023 and allowed a further cut to 2% on September 1, 2024 only if the Education Trust Fund grew enough (ALDOR 2023 notice). It did not: "Alabama's sales and use tax rate on food will remain at three percent on September 1, 2024" (ALDOR 2024 notice). Under Act 2025-305 the state rate fell from 3% to 2% on September 1, 2025 (ALDOR 2025 notice). Act 2026-604 then suspended the state portion on food for May 1 to June 30, 2026; retailers still report qualifying food sales in gross proceeds and deduct them on the state return (ALDOR 2026 notice). "Food has the same meaning as defined in 7 U.S.C. § 2011, for the purposes of the federal Supplemental Nutrition Assistance Program (SNAP)"; alcoholic beverages, tobacco, hot foods and hot food products ready for immediate consumption are not SNAP food, so the general rate applies to them. City and county food rates were frozen at their general rate in effect on June 15, 2023, and a local government may cut its food rate in 25 percent steps (ALDOR 2023 notice).

## The taxable base

- **General tangible personal property:** 4% state on gross proceeds of retail sales for consumption or use in Alabama (ALDOR Sales Tax page).
- **Food (SNAP definition):** 2% state from September 1, 2025, with the state portion suspended May 1 to June 30, 2026; local tax still applies at the local food rate.
- **Hot or prepared food, alcoholic beverages, tobacco:** not SNAP food, so the general rate applies (ALDOR food notices).
- **Exemptions on the ALDOR Sales and Use Tax Incentives page:** pollution-control equipment (§§40-23-4(a)(16), 40-23-62(3)); raw materials "used by manufacturers or compounders as an ingredient or component part" (§§40-23-1(a)(9)b, 40-23-60(4)b); quality-control testing withdrawals and donations to charitable entities (§40-23-1(e), Regulation 810-6-5-.26).
- **SSUT sellers:** the 8% flat tax is collected on all sales of taxable products and services into Alabama unless the buyer gives a resale certificate, an Alabama exemption certificate or an Alabama direct pay permit; it cannot replace tax collected by a licensing official on vehicles, boats, trailers and manufactured homes (ALDOR remote-seller FAQ).

## Deadlines and filing

- State returns are filed with ALDOR (My Alabama Taxes portal); self-administered cities are filed separately with each city, and ALDOR-administered locals with the state (ALDOR Sales Tax page on the administration split). Filing frequencies and return form IDs: see Not yet confirmed.

## Penalties and interest

- Penalty and interest percentages for sales tax are not stated on the pages read; confirm current provisions (Title 40) with ALDOR before advising. See Not yet confirmed.

## Cross-border points

- **Economic nexus:** "All remote sellers directly selling over the $250,000 threshold of total retail sales delivered into Alabama the previous calendar year are required to collect and remit taxes on sales into Alabama beginning on October 1, 2018" (ALDOR remote-seller FAQ). A small-seller exception does not apply to sellers with a physical presence in Alabama.
- **Threshold computation:** "should only include retail sales made directly by the seller, whether taxable or non-taxable," excluding wholesale sales for resale with an Alabama resale certificate and sales through an SSUT-participating marketplace (ALDOR FAQ).
- **SSUT program:** Act 2015-448 lets an eligible seller (selling into Alabama from outside the state, with no physical presence and not otherwise required to collect) collect, report and remit a flat 8% sellers use tax on all sales into Alabama; sellers below the threshold may still join (ALDOR FAQ).
- **Marketplace facilitators:** from January 1, 2019, a facilitator that does not collect on qualifying Alabama retail sales must report those sales and notify customers (§40-2-11(7)(b), ALDOR FAQ).

## Worked examples

Client facts in these examples are hypothetical. Only rates from the table above are used; local rates vary by address, so local tax is discussed qualitatively.

**Example 1: general retail sale, state rate only**

A seller sells $1,000 of tangible personal property in Alabama; the state tax is 4% of $1,000 = $40. Local tax, if any, is additional and must be read from ALDOR's local rate lookup.

```oa-check
name: AL sales tax, general state rate
inputs:
  price: 1000
  state_rate: 0.04
steps:
  - tax: price * state_rate
expected:
  tax: 40.00
```

**Example 2: SNAP-definition groceries, state food rate**

$200 of unprepared groceries sold in October 2026: the state food rate is 2%, so $4 state tax. (Had the sale been between May 1 and June 30, 2026, the state portion would be nil.) Local tax is additional at the local food rate.

```oa-check
name: AL sales tax, food rate
inputs:
  price: 200
  state_food_rate: 0.02
steps:
  - tax: price * state_food_rate
expected:
  tax: 4.00
```

**Example 3: remote seller in the SSUT program**

A remote seller with no Alabama presence and $300,000 of retail sales delivered into Alabama last year is over the $250,000 threshold and must collect. It joins SSUT and makes $12,500 of taxable sales into Alabama in a month: it collects the flat 8%, with no local rate lookup.

```oa-check
name: AL simplified sellers use tax, flat 8 percent
inputs:
  prior_year_al_sales: 300000
  threshold: 250000
  month_taxable_sales: 12500
  ssut_rate: 0.08
steps:
  - over_threshold: prior_year_al_sales - threshold
  - ssut_due: month_taxable_sales * ssut_rate
expected:
  over_threshold: 50000.00
  ssut_due: 1000.00
```

## Ask the client first

- What products or services are sold (food at 2% state versus the general 4%; machinery at 1.5%; vehicles at 2%)?
- Any food sales between May 1 and June 30, 2026 (state portion suspended)?
- Were Alabama retail sales (direct, taxable or not) over $250,000 in the previous calendar year? Is the seller in the SSUT program?
- Any physical presence in Alabama (locations, employees, inventory)? The small-seller exception does not apply.
- Which self-administered cities have nexus? Separate registration and filing may be required.
- Are exemption certificates on file (resale, pollution control, ingredient/component)?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR State Sales and Use Tax Rates, read for 4% general, 2% food from 9/1/2025, 3% food 9/1/2023 to 8/31/2025, 2% automotive, 1.5% manufacturing and farm machinery, vending 3%/4%, amusement 4%, SSUT 8%, rental rates | https://www.revenue.alabama.gov/sales-use/state-sales-use-tax-rates/ | 2026-11-13 |
| 2 | ALDOR Sales Tax page, read for authority, application, manufactured home set-up 2%, local .10% to 5%, administration split | https://www.revenue.alabama.gov/tax-types/sales-tax/ | 2026-11-13 |
| 3 | ALDOR Sales and Use Tax Incentives page, read for Chapter 23, Title 40; exemptions with Code sections | https://revenue.alabama.gov/taxes-fees/sales-use-tax/ | 2026-11-13 |
| 4 | ALDOR notice: State Sales and Use Tax Rate Reduced on Food Beginning September 1, 2023, read for Act 2023-554, SNAP definition, local food rates | https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-reduced-on-food-beginning-september-1-2023/ | 2026-11-13 |
| 5 | ALDOR notice: State Sales and Use Tax Rate on Food Remains at Three Percent, read for September 1, 2024 | https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-on-food-remains-at-three-percent/ | 2026-11-13 |
| 6 | ALDOR notice: State Sales and Use Tax Rate Reduced on Food Beginning September 1, 2025, read for Act 2025-305 | https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-reduced-on-food-beginning-september-1-2025/ | 2026-11-13 |
| 7 | ALDOR notice: Temporary Suspension of State Sales and Use Tax on Food, read for Act 2026-604, May 1 to June 30, 2026 | https://www.revenue.alabama.gov/notice-temporary-suspension-of-state-sales-and-use-tax-on-food/ | 2026-11-13 |
| 8 | ALDOR FAQ: Are all remote sellers required to register in Alabama?, read for $250,000 threshold, October 1, 2018, threshold computation, SSUT 8%, marketplace facilitators | https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/ | 2026-11-13 |

Not yet confirmed: the maximum combined state and local rate and city-by-city combined rates (an earlier draft carried "~11%" and ~9% to 10% for the large cities without a source); the number of self-administered cities (an earlier draft carried ~200+); destination-based sourcing and Alabama's Streamlined Sales Tax status; the late-filing and fraud penalty percentages for sales tax (an earlier draft carried 10% of tax due and 50% of the deficiency); the taxability of clothing, canned or downloaded software, SaaS, digital goods, professional services and prescription drugs (an earlier draft carried these without sources); sales tax filing frequencies and return form IDs; the dates of any 2026 back-to-school sales tax holiday.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `alabama-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/alabama-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
