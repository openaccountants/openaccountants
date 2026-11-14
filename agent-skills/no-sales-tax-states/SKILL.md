---
name: no-sales-tax-states
description: "The five US states with no general statewide sales tax (Alaska, Delaware, Montana, New Hampshire, Oregon) and the taxes they charge instead, for tax year 2026. Covers Alaska local sales taxes collected through the Alaska Remote Seller Sales Tax Commission, the Delaware gross receipts tax on sellers, the Montana 8% lodging facility sales and use tax and local resort taxes, the New Hampshire 8.5% Meals and Rooms (Rentals) Tax, and the Oregon Corporate Activity Tax of $250 plus 0.57% above $1 million. Trigger on \"no sales tax states\", \"Alaska sales tax\", \"Delaware gross receipts tax\", \"Montana resort tax\", \"New Hampshire meals tax\", \"Oregon CAT\", \"tax-free shopping\". Load us-sales-tax for the general framework and us-sales-tax-nexus-50-state-matrix for nexus in the other states."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/no-sales-tax-states"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# States with no general sales tax: Alaska, Delaware, Montana, New Hampshire and Oregon, tax year 2026

> **Source-cited draft.** Built from the five states' own revenue pages, the Alaska Remote Seller Sales Tax Commission and the Montana Code, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Five states have no general statewide sales tax. "No sales tax" does not mean no tax: Alaska towns and boroughs charge their own sales tax, Delaware taxes the seller's gross receipts, Montana charges 8% on lodging and lets resort communities levy a local tax, New Hampshire charges 8.5% on meals, rooms and car rentals, and Oregon charges a Corporate Activity Tax of $250 plus 0.57% on commercial activity over $1 million. A seller based in one of these states still collects in every other state where it has nexus.

## Scope and who this is for

In scope: what a seller or buyer owes in Alaska, Delaware, Montana, New Hampshire and Oregon in place of a sales tax, for 2026 periods. Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The US sales and use tax framework (use tax, sourcing, marketplaces, exemption certificates) | `us-sales-tax` |
| Economic nexus in the 45 sales tax states and DC | `us-sales-tax-nexus-50-state-matrix` |
| Alaska local rates, caps and ARSSTC filing in detail | `ak-sales-tax` |
| Income tax nexus for out-of-state sellers | `us-pl-86-272-income-tax-nexus` |

## Ask the client first

1. Which of the five states is the client in: selling into, operating in, or buying from?
2. For Alaska: the delivery address (borough and city) of each sale and total Alaska sales in 2025 and 2026.
3. For Delaware: the business activity (retailer, wholesaler, manufacturer, professional services, and so on) and monthly gross receipts.
4. For Montana: whether it rents lodging, and whether it sells inside a resort community (Big Sky, Whitefish, West Yellowstone and others).
5. For New Hampshire: whether it sells meals, rooms or motor vehicle rentals.
6. For Oregon: total Oregon commercial activity for the year.
7. Where the buyer lives, for use tax back home.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Alaska: state sales tax | None; local jurisdictions may levy their own | [ARSSTC, business sellers](https://arsstc.org/business-sellers/) |
| Alaska: remote seller threshold for ARSSTC members | $100,000 statewide gross sales, current or prior calendar year | [ARSSTC threshold notice](https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf) |
| Alaska: 200-transaction test | Removed from 1 January 2025 | [ARSSTC threshold notice](https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf) |
| Delaware: gross receipts tax rate range, on the seller | .0945% to 1.9914% by business activity | [Delaware Division of Revenue, gross receipts tax](https://revenue.delaware.gov/business-tax-forms/gross-receipts-tax/) |
| Montana: lodging facility sales and use tax | 8% combined (4% use tax plus 4% sales tax) | [Montana DOR, lodging facility tax](https://revenue.mt.gov/taxes/miscellaneous/lodging-facility) |
| New Hampshire: Meals and Rooms (Rentals) Tax | 8.5% on meals, rooms and motor vehicle rentals | [NH DRA, Meals and Rooms FAQ](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/meals-rooms-rentals-tax) |
| Oregon: Corporate Activity Tax | $250 plus 0.57% of taxable Oregon commercial activity over $1 million | [Oregon DOR, Corporate Activity Tax](https://www.oregon.gov/dor/programs/businesses/pages/corporate-activity-tax.aspx) |

### Per state

1. **Alaska.** No state tax. Boroughs and cities levy their own sales tax; Anchorage and the city of Fairbanks levy none. Remote sellers register with ARSSTC once Alaska sales pass $100,000, counting marketplace sales; ARSSTC collects for its member jurisdictions. Non-member jurisdictions are handled one by one. Many members cap the taxable amount per item. Local rates and caps live in `ak-sales-tax`.
2. **Delaware.** No sales tax on the buyer. The seller pays gross receipts tax on its receipts at the rate for its activity, within the .0945% to 1.9914% range. It is a cost of the business: it is not added to an invoice as "sales tax".
3. **Montana.** No general sales tax. Lodging is taxed at 8% statewide. Resort communities may levy a local resort tax under Mont. Code 7-6-1501 to 7-6-1507; the rate and base are set locally, so check the community.
4. **New Hampshire.** No tax on retail goods or general services. The 8.5% Meals and Rooms (Rentals) Tax is assessed on patrons of restaurants and hotels and on motor vehicle rentals; the operator collects it.
5. **Oregon.** No sales tax anywhere. A business with taxable Oregon commercial activity over $1 million pays the CAT on the excess. Oregon says the CAT "is not a transactional tax, such as a retail sales tax".
6. **Use tax back home.** A buyer who brings goods home from a no-sales-tax state may owe use tax in their own state (see `us-sales-tax`).
7. **The seller's own nexus elsewhere.** A seller based in these states collects in each other state where it has nexus (see `us-sales-tax-nexus-50-state-matrix`).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Remote seller ships to Juneau, Kodiak or Sitka | Local tax applies through ARSSTC once over $100,000 statewide; check the item cap in `ak-sales-tax` |
| Remote seller ships to Anchorage or the city of Fairbanks | No local general sales tax |
| Grocery food, prescription drugs, clothing in Alaska | Varies by jurisdiction; check the ARSSTC rate sheet |
| Delaware retailer advertises "tax-free" | True for the buyer; the retailer still pays gross receipts tax |
| Delaware rate dispute over activity class | Refer (R-NOST-3) |
| Montana hotel or short-term rental | 8% lodging facility sales and use tax |
| Montana rental car | A separate rental vehicle tax; rate not re-read (see "Not yet confirmed:") |
| Sale in a Montana resort community | Local resort tax; rate set by the community |
| Online seller ships into a Montana resort community | Whether the local resort tax reaches a remote seller is not settled in the sources read: check with the community |
| NH store sells a laptop, SaaS, digital goods or a service | No tax |
| NH restaurant, hotel, Airbnb or car rental | 8.5% |
| Oregon business under $1 million commercial activity | No CAT |
| Oregon hotel | State and local lodging taxes apply (rate not re-read) |
| Oregon seller with customers in other states | Collects where it has nexus; Oregon's position does not help elsewhere |
| Oregon CAT shown as a line item on an invoice | Do not present it as a sales tax: it is a tax on the business (check ORS 317A before itemizing) |
| Massachusetts resident buys in New Hampshire | Massachusetts use tax may apply (see `ma-sales-tax`) |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| "Alaska has no sales tax" said to a remote seller | Local tax applies once over the ARSSTC threshold |
| "Delaware is tax-free" in a business plan | Gross receipts tax applies to the seller |
| Oregon commercial activity near $1 million | CAT registration and payment |
| NH seller of prepared food treats it as untaxed | 8.5% Meals and Rooms Tax |
| Buyer told a no-tax purchase is free of all tax | Use tax may apply at home |

## Worked cases

**Case 1, Oregon CAT.** An Oregon business has taxable Oregon commercial activity of $3,000,000 in 2026. CAT = $250 + 0.57% x ($3,000,000 - $1,000,000) = $250 + $11,400 = $11,650. With commercial activity of $900,000, it owes no CAT.

```oa-check
name: Oregon CAT on 3,000,000 of commercial activity (2026)
inputs:
  commercial_activity: 3000000
  threshold: 1000000
steps:
  - excess: max(commercial_activity - threshold, 0)
  - cat: 250 + excess * 0.0057
expected:
  excess: 2000000
  cat: 11650.00
```

**Case 2, a decision: where to book a three-night stay.** A guest compares a $200-a-night hotel in New Hampshire with the same price in Montana. New Hampshire: $600 x 8.5% = $51. Montana: $600 x 8% = $48, before any local resort tax if the hotel is in a resort community. Outside a resort community, Montana is $3 cheaper.

```oa-check
name: Three nights at 200, New Hampshire against Montana (2026)
inputs:
  nightly: 200
  nights: 3
steps:
  - room_total: nightly * nights
  - nh_tax: room_total * 0.085
  - mt_tax: room_total * 0.08
  - difference: nh_tax - mt_tax
expected:
  room_total: 600
  nh_tax: 51.00
  mt_tax: 48.00
  difference: 3.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-NOST-1 | Compliance for a specific Alaska jurisdiction outside ARSSTC | Refer to that jurisdiction; use `ak-sales-tax` for members |
| R-NOST-2 | Oregon CAT subtractions, exclusions and quarterly estimates | Refer to a CPA |
| R-NOST-3 | Delaware gross receipts tax classification dispute | Refer |
| R-NOST-4 | Montana resort tax for a remote seller | Refer to the resort community |

## Filing and payment

| State | Return | Where |
| --- | --- | --- |
| Alaska (local) | ARSSTC return for member jurisdictions; others as each requires | [ARSSTC](https://arsstc.org/business-sellers/) |
| Delaware | Gross receipts tax return | [Delaware Division of Revenue](https://revenue.delaware.gov/business-tax-forms/gross-receipts-tax/) |
| Montana | Lodging facility sales and use tax return (Form LFT) | [Montana DOR](https://revenue.mt.gov/taxes/miscellaneous/lodging-facility) |
| New Hampshire | Meals and Rooms return, online through Granite Tax Connect | [NH DRA](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/meals-rooms-rentals-tax) |
| Oregon | CAT annual return and quarterly estimates | [Oregon DOR](https://www.oregon.gov/dor/programs/businesses/pages/corporate-activity-tax.aspx) |

Return due dates and frequencies were not re-read for 2026: see the "Not yet confirmed:" line.

## Completion checklist

- Each sale placed in the right state and, for Alaska and Montana, the right local jurisdiction.
- Alaska statewide sales tested against $100,000, counting marketplace sales.
- Delaware activity class identified.
- Oregon commercial activity tested against $1 million.
- Buyer told about use tax at home where relevant.
- Nexus in the other states checked.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ARSSTC threshold notice. Read for the $100,000 statewide threshold and the removal of the 200-transaction test from 1 January 2025. | https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf | 2026-11-13 (via `ak-sales-tax`) |
| ARSSTC business sellers. Read for registration and filing for member jurisdictions. | https://arsstc.org/business-sellers/ | 2026-11-13 (via `ak-sales-tax`) |
| Delaware Division of Revenue, gross receipts tax. Read for "rates currently range from .0945% to 1.9914%" and that the tax is on the seller. | https://revenue.delaware.gov/business-tax-forms/gross-receipts-tax/ | 2026-11-13 |
| Montana DOR, lodging facility sales and use tax. Read for "a combined 8% lodging facility sales and use tax: Use Tax 4% Sales Tax 4%". | https://revenue.mt.gov/taxes/miscellaneous/lodging-facility | 2026-11-13 |
| Mont. Code 7-6-1502. Read for the resort community taxing authority. | https://archive.legmt.gov/bills/mca/title_0070/chapter_0060/part_0150/section_0020/0070-0060-0150-0020.html | 2026-11-13 |
| NH DRA, Meals and Rooms (Rentals) Tax FAQ. Read for the 8.5% on meals, rooms and motor vehicle rentals. | https://www.revenue.nh.gov/resource-center/frequently-asked-questions/meals-rooms-rentals-tax | 2026-11-13 |
| Oregon DOR, Corporate Activity Tax. Read for "$250 plus 0.57 percent of taxable Oregon commercial activity of more than $1 million" and "not a transactional tax". | https://www.oregon.gov/dor/programs/businesses/pages/corporate-activity-tax.aspx | 2026-11-13 |

Not yet confirmed: the Delaware rate for each business activity (the old file's retailer 0.7468%, grocer 0.0945%, restaurant 0.6758%, wholesaler 0.3985%, manufacturer 0.0945%, professional 0.3944% were not re-read; the Division's rate sheet did not open); the Montana resort tax maximum rate (old file: up to 3%) and rental vehicle tax (old file: 4%); the Oregon state lodging tax rate (old file: 1.5%); individual Alaska local rates (see `ak-sales-tax`); return due dates and frequencies for all five states (old file: Delaware 20th of the following month, New Hampshire 15th, Oregon CAT 15 April).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `no-sales-tax-states` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/no-sales-tax-states. If neither is available, confirm every figure against the official source pages cited above before relying on it.
