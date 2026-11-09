---
name: al-sales-tax
description: Use this skill whenever asked about Alabama sales tax, Alabama use tax, Alabama sales tax nexus, ADOR sales tax filing, self-administered city taxes in Alabama, or Alabama grocery food taxation. Trigger on phrases like "Alabama sales tax", "AL sales tax", "ADOR", "Code of Ala. §40-23", "Alabama local tax", "Alabama grocery tax", "self-administered cities Alabama", or any request involving Alabama state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
version: 2.2
jurisdiction: US-AL
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
domain: vat-gst
type: rates-card
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AL Sales Tax

> **Source-cited draft.** Built from ALDOR's Sales Tax authority page, Sales and Use Tax Incentives page, the food-rate reduction notice (Act 2023-554) and the remote-seller registration FAQ, read 2026-10-28. No accountant has reviewed it. Do not advise a client from it without review by a qualified Alabama professional.

See also: `us-sales-tax` (load first), `al-cross-border` (remote sellers), `al-corporate-income-tax`.

## Who this applies to

- **Every retailer** selling tangible personal property at retail in Alabama: the tax applies to "gross proceeds from sale of all taxable items for consumption or other use to consumers ... within Alabama" (ALDOR Sales Tax page, Application). The sales and use tax law is found in Chapter 23, Title 40, Code of Alabama 1975 (ALDOR Sales and Use Tax Incentives page).
- **Remote and out-of-state sellers:** economic nexus over the $250,000 retail-sales threshold, collect from October 1, 2018 (ALDOR remote-seller FAQ).
- **Local tax administration:** "Some of the local sales taxes are collected by ALDOR, third party administrators, and others are self-administered" (ALDOR Sales Tax page) -- a seller may need to register with self-administered cities individually.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| State general rate | "4% of gross proceeds of sale of tangible personal property" | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Amusement/entertainment | 4% of gross receipts from public places of amusement or entertainment | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Food (SNAP definition) | 2% of gross proceeds of sale of food, as defined in 7 U.S.C. § 2011 | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Food rate history | Reduced from 4% to 3% on September 1, 2023, and to 2% on September 1, 2024, under Act 2023-554 | current | [ALDOR food-rate notice](https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-reduced-on-food-beginning-september-1-2023/) |
| Manufacturing machinery | 1.5% of selling price of machinery used in mining or manufacturing tangible personal property | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Farm machinery | 1.5% of net trade difference of new or used farm machines, machinery and equipment | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Automotive | 2% of net trade difference of new or used automotive vehicles, truck trailers, semi-trailers or house trailers | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Vending-machine food products | 3% of retail selling price | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Local sales taxes | Counties and municipalities may levy local sales taxes "ranging in rate between .10% to 5%" | current | [ALDOR Sales Tax page](https://www.revenue.alabama.gov/tax-types/sales-tax/) |
| Remote-seller economic nexus | Over $250,000 of total retail sales delivered into Alabama the previous calendar year | current | [ALDOR remote-seller FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/) |

**Food note:** under Act 2023-554, "the state sales and use tax rates on food will be reduced from 4 percent to 3 percent on September 1, 2023" and "will be further reduced to 2 percent on September 1, 2024, if there is sufficient growth in the state Education Trust Fund" (ALDOR notice). The current ALDOR Sales Tax page lists the food rate as 2%. "Food has the same meaning as defined in 7 U.S.C. § 2011, for the purposes of the federal Supplemental Nutrition Assistance Program (SNAP)" -- hot foods and hot food products ready for immediate consumption are not SNAP food, so they stay at the general rate. "The city and county sales and use tax rates on food will be equal to their general sales tax rate in effect as of June 15, 2023" (ALDOR notice).

## The taxable base

- **General tangible personal property:** 4% state on gross proceeds of retail sales for consumption or use in Alabama (ALDOR Sales Tax page).
- **Food (unprepared, SNAP-definition):** 2% state after the Act 2023-554 reductions; local governments tax food at their general rate in effect on June 15, 2023 (ALDOR notice).
- **Prepared/hot food, candy, soft drinks, alcoholic beverages, tobacco:** not SNAP food -- the general rate applies (ALDOR notice carve-outs).
- **Exemptions confirmed on archived ALDOR pages (Sales and Use Tax Incentives):** pollution-control equipment (§§40-23-4(a)(16), 40-23-62(3)); raw materials "used by manufacturers or compounders as an ingredient or component part" (§§40-23-1(a)(9)b, 40-23-60(4)b); quality-control testing withdrawals and donations to charitable entities (§40-23-1(e), Regulation 810-6-5-.26).
- Taxability of clothing, canned/downloaded software, SaaS, digital goods and professional services is unconfirmed. The prior draft's transaction-pattern table carried these as taxable/not taxable without archived sources and is now.

## Deadlines and filing

- State returns are filed with ALDOR (My Alabama Taxes portal); self-administered cities are filed separately with each city, and ALDOR-administered locals with the state (ALDOR Sales Tax page on the administration split). Current form IDs and filing frequencies are unconfirmed here, confirm with ALDOR.

## Penalties and interest

- The prior draft carried late-filing 10% of tax due and fraud 50% of deficiency; these percentages are not tied to an archived primary source -- see Not yet confirmed.
- Confirm current penalty and interest provisions (Title 40 / Chapter 23) with ALDOR before advising.

## Cross-border points

- **Economic nexus:** "All remote sellers directly selling over the $250,000 threshold of total retail sales delivered into Alabama the previous calendar year are required to collect and remit taxes on sales into Alabama beginning on October 1, 2018" (ALDOR remote-seller FAQ). A small-seller exception applies to remote sellers "who do not have annual sales of products and services into the state of more than $250,000" -- and does not apply to sellers with a physical presence in Alabama.
- **Threshold computation:** "should only include retail sales made directly by the seller, whether taxable or non-taxable," excluding wholesale sales for resale with an Alabama resale certificate and sales through a participating SSUT marketplace (ALDOR FAQ).
- Below-threshold sellers "may still apply to participate in the simplif[ied] sellers use tax program" (ALDOR FAQ).
- Sourcing (destination-based) and Alabama's Streamlined Sales Tax status are unconfirmed.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used; specific local rates are not confirmed, so local tax is discussed qualitatively.

**Example 1: general retail sale, state rate only**

A seller (hypothetical) sells $1,000 of tangible personal property in Alabama; the state tax is 4% of $1,000 = $40. Local tax, if any, is additional and must be read from ALDOR's local rate lookup.

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

$200 (hypothetical) of unprepared groceries: the state food rate is 2%, so $4 state tax. Local governments tax food at their general rate in effect on June 15, 2023, so local tax is additional and must be confirmed per jurisdiction.

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

**Example 3: economic nexus test (prose only -- not a counted worked example)**

A remote seller (hypothetical) with $300,000 of retail sales delivered into Alabama in the previous calendar year and no physical presence exceeds the $250,000 threshold, so the seller must register and collect (ALDOR FAQ; threshold in the rates table above).

## Ask the client first

- What products or services are sold (food at 2% state vs. general 4%; machinery at 1.5%; vehicles at 2%)?
- Are Alabama retail sales (direct, taxable or not) over $250,000 in the previous calendar year?
- Any physical presence in Alabama (locations, employees, inventory)? The small-seller exception does not apply.
- Which self-administered cities have nexus -- separate registration and filing may be required?
- Are exemption certificates on file (resale, pollution control, ingredient/component)?

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR Sales Tax page (authority, rates: 4% general, 2% food, 1.5% manufacturing and farm machinery, 2% automotive, 3% vending food, local .10%–5%, administration split) | https://www.revenue.alabama.gov/tax-types/sales-tax/ | 2026-10-28 |
| ALDOR Sales and Use Tax Incentives page (state rate 4%, manufacturing/farm 1.5%, automotive 2%, exemptions with Code sections) | https://revenue.alabama.gov/taxes-fees/sales-use-tax/ | 2026-10-28 |
| ALDOR notice: State Sales and Use Tax Rate Reduced on Food Beginning September 1, 2023 (Act 2023-554, 4%→3%→2% phase-down, SNAP food definition, local food rates) | https://www.revenue.alabama.gov/notice-state-sales-and-use-tax-rate-reduced-on-food-beginning-september-1-2023/ | 2026-10-28 |
| ALDOR FAQ: Are all remote sellers required to register in Alabama? ($250,000 threshold, October 1, 2018, threshold computation, SSUT) | https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/ | 2026-10-28 |

Not yet confirmed: the local rate range previously carried as "0%–7%" and the maximum combined rate previously carried as "~11.00%" (the archived ALDOR page says counties and municipalities may levy between .10% and 5%; the maximum combined figure is not on an archived page); city-by-city combined rates (Birmingham/Montgomery/Huntsville/Mobile/Tuscaloosa previously carried as ~9%–10%); the number of self-administered cities (previously carried as ~200+; the administration split is confirmed but not the count); destination-based sourcing and Alabama's Streamlined Sales Tax membership; marketplace-facilitator rules; the late-filing penalty (previously carried as 10% of tax due) and the fraud penalty (previously carried as 50% of deficiency) -- confirm against the statute; the taxability of clothing, canned/downloaded software, SaaS, digital goods, professional services, rentals of tangible personal property, prescription drugs and farm-equipment exemptions (previously carried in a transaction-pattern table without archived sources); filing frequencies and current return form IDs.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
