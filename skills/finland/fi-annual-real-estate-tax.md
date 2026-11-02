---
name: fi-annual-real-estate-tax
description: >
  Compute Finland's 2026 annual real-estate tax for owners of land and buildings,
  including separate land/building ownership, co-owners and nonresident owners.
  Determine liability on 1 January, establish the preceding year's statutory
  valuation, classify each component and apply the municipality's adopted rate.
  Covers ordinary residential and commercial property, building replacement
  values, age reductions, land target-value transitions, unbuilt sites, Åland
  deviations, corrections and payment. Trigger on kiinteistövero, property-tax
  decision, building value, annual tax, municipal real-estate rate or property
  information corrections. Transfer tax on buying property and income tax on
  rent or gains are separate computations in the companion skills.
version: 0.1
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland annual real-estate tax v0.1

## Who this applies to

The owner or qualifying owner-equivalent holder on **1 January 2026** owes the whole year's annual property tax. A later sale does not transfer that public-law liability even if the parties allocate its cost in the contract. A building owner on leased land owes building tax and the landowner owes land tax. Allocate co-owned property to each owner's share. A housing-company shareholder does not separately own the underlying building: the company is assessed. [Real Estate Tax Act 654/1992 §§2,5–9][law].

Forests, agricultural land and the other §3–4 exempt components are excluded, but a building or its site does not automatically share the agricultural/forest exemption. Identify each taxable component, municipality, use and owner. Power generation, mines and other special industrial valuations need their specific statutory calculations. [Act §§2–4,14–15][law].

## Rates, bands and thresholds

| Component or valuation rule | Ordinary mainland rule | Official source |
|---|---|---|
| General land rate | Municipal rate within 1.30–2.00% | Act §11 [text][law] |
| General building rate | Municipal rate within 0.93–2.00% | Act §11 [text][law] |
| Permanent residential building | Municipal rate within 0.41–1.00% | Act §12 [text][law] |
| Other residential building | Municipal rate within 0.93–2.00% | Act §13 [text][law] |
| Qualifying unbuilt residential site | Separate rate 2–6%; specified metropolitan municipalities at least general land rate +3 percentage points, maximum 6% | Act §§12a–12b [text][law] |
| Helsinki 2026 example rates | Land 1.30%, general building 0.93%, permanent residence 0.41%, other residence 0.93%, unbuilt site 4.30% | [Council decision 5 November 2025 §262][helsinki] |
| Annual age reductions | Wooden residential/office 1.25%, stone 1%; wooden commercial/industrial 5%, stone 4%; other structure 10% | Valuation Act 1142/2005 §30 [text][valuation] |
| Value floor while in use | Residential building 30%, other ordinary building/structure 20% of replacement value | Valuation Act §30 [text][valuation] |
| Ordinary small-house replacement unit | EUR 770.58/m² before adjustments; older wooden exceptions EUR 614.75 before 1960 / EUR 695.54 for 1960–69 | Regulation 1073/2025 §5 [text][building] |
| Collection floor | Tax below EUR 10 not imposed | Act §22 [text][law] |

These are legal ranges, not a default municipal rate. Obtain the property's actual **2026** municipal decision/rate from the assessment or [Vero municipality tables][rates]. Åland has its own permitted lower bounds below.

## The base

### Establish the correct value year

The 2026 tax uses the **31 December 2025** taxable value, not the purchase price and not 2026 replacement-cost parameters. Apply Valuation Act chapter 5 and the annual 2025 valuation instruments: building Regulation **1073/2025**, whose §22 expressly applies to 2025 values, and land decision **VH/5812/00.01.00/2025**. The later land decision issued 7 October 2026 concerns 2026 values used for 2027 annual tax. Do not select it merely because it is the latest linked page. [Act §15][law]; [Regulation §22][building]; [2025 land decision §6][land].

### Land

Identify the mapped zone unit value and whether it is per square metre of land or building right. Apply the municipality's map/assessment instructions for use, building rights, infrastructure, location and any comparable-zone fallback where no zone is assigned. Do not substitute the negotiated purchase price for the statutory zone. Apply the unused-building-right reduction under Valuation Act §29(3) where the conditions hold. [Valuation Act §29][valuation]; [land decision §1][land].

For a standard rural site, weight the first 3,000 m² at 100% of the zone unit, next 2,000 at 50%, next 5,000 at 25%, excess over 10,000 at 10%; retain the decision's alternative 2,000 m² first tier for existing sites to which it applies. Zoned industrial/storage large sites use 100% through 20,000 m², 50% to 50,000 and 25% thereafter. The resulting unit zone price is at least EUR 1/m². Target value is **75%** of the 2025 zone value. If 2024 taxable value is below that target, raise it by 30% where below 80% of target, otherwise 20%, capped at target and floored at EUR 0.75/m². Corrections of an erroneous base/zone/building-right quantity do not get the transition cap. Apply a proven lower fair value under §5 where appropriate. [2025 land decision §§2–5][land].

### Buildings

Classify each building and measure whole square/cubic metres under Regulation §§2–3: external floor area includes cellars and insulated attic rooms but excludes balconies, canopies and space under 160 cm; designated office/storage/parking internal areas use the specific rule. Apply the relevant unit table **with all feature adjustments**, then age reductions, completion percentage, material damage and major renovation corrections. The standard unit already represents the regulatory replacement basis; do not multiply it by 75% again. [Regulation §§1–21][building]; [Valuation Act §30][valuation].

For a small house under §§4–6, begin with the unit above. Over 60 through 120 m² reduce the unit by EUR 1.316 for each m² over 60; above 120 m² the unit reduction is EUR 78.96. Missing water/sewer reduces EUR 49.65/m², central heating EUR 56.27/m², electricity EUR 29.70/m². Qualifying unfinished storage cellar has the separate EUR 264.38/m² unit. Use separate areas rather than both valuing the cellar at the main unit and adding it again. [Regulation §§4–6][building].

Apartment blocks use §§7–8, including lift, average dwelling size and storey adjustments. Leisure homes use §§9–12, with winter usability, veranda and equipment additions; an atypical substantially upgraded leisure property can fall under small-house rules. Separate insulated outbuildings/garages use EUR 502.18/m²; light uninsulated ones EUR 261.49/m², or EUR 204.94/m² if built before 1970. [Regulation §§7–13][building].

For commercial property select the statutory row: offices EUR 1,067.84/m² **before** height, shape, storage/parking, lift and air-conditioning adjustments in §15; shops EUR 329.02/m³ **before** volume, storage, height and storey adjustments in §17; industrial/workshop/storage buildings EUR 128.40/m³ **before** height, heating/water, ventilation/lighting, storey and volume adjustments in §19. Retain each measured feature and the corresponding regulation row in the workpaper; a base unit alone is not the final value. For a materially different building standard §20 allows a reasoned adjustment of at most 30%; mixed uses can require separate valuation of substantial parts. A building/structure to which the listed groups cannot apply uses 75% of comparable construction cost under §21, subject to its listed public-building table. [Regulation §§14–21][building].

Subtract **straight-line** annual age reduction from replacement value, with the statutory in-use floor. Major improvements can reduce the effective age allowance; exceptional damage can support a greater reduction. Apply Valuation Act §32's combined fair-value ceiling with evidence; do not reduce only one chosen component while ignoring the combined property. [Valuation Act §§30,32][valuation].

### Rate classification and final tax

Use the permanent-residence building rate where at least half the floor area is used for permanent residence under §12; qualifying ancillary buildings follow it. Land keeps the general land rate. Apply the other-residence rate under §13 where its conditions hold, including the business-lodging exception. An unbuilt site's separate rate requires all §12a conditions: qualifying residential zoning in force more than a year, over half building rights residential, no residence built/started, road access, water/sewer availability, no relevant building prohibition and the stated common ownership. Being empty alone is insufficient. Multiply each established component value by its municipal category rate, sum, and allocate the taxpayer's ownership. [Act §§9,11–13][law].

Åland Act **1993:15 §§1–2a** incorporates national assessment/valuation with regional changes: the rates referred to in national §§11–14 can be as low as **0.00%**; the §13 other-residence rate is capped at 0.90% and at permanent-residence rate +0.90 percentage points, with its exclusively-rented leisure-home exception. Use the actual Åland municipality's adopted rate, not the mainland minimum. Special wind-power provisions are separate. [Åland Act][aland].

## Deadlines and filing

Check every owner's 2026 decision and report missing/incorrect **2025** property details by **14 April 2026**. Changes occurring during 2026 belong to spring 2027 reporting. If all prefilled information is correct, no correction is required. Each co-owner has a duty; spouses follow Vero's shared-property correction instructions. After a correction, wait for the replacement assessment before paying the superseded amount and reconcile the new dates. [Act §§16–18][law]; [Vero 2026 decision procedure][decision].

Assessment ends on the taxpayer's own date, no later than 31 October. Tax **EUR 170 or more** is split into two instalments. For an assessment ending June 2026, ordinary dates are 6 August/6 October; July: 7 September/6 November; August: 6 October/7 December; September: 6 November/7 January 2027; October: 7 December/8 February 2027. Corporate May completion has 6 July/7 September. Use the actual decision and property-tax reference. After assessment completion use the claim-for-adjustment route stated on the decision; do not treat an income-tax return amendment as the property correction. [Vero payment calendar][payment]; [Act §§22,24–26][law].

## Penalties and interest

For late details increasing tax **before assessment ends**, the late fee is EUR 50 individual/estate or EUR 100 other taxpayer, once per tax year. A tax increase for an omitted/incorrect base is ordinarily 10% of added tax, with the 2–50% routes according to the breach and minimum EUR 75 individual/estate or EUR 150 other. The same omission cannot attract both that late fee and tax increase. Apply waiver/hearing conditions; ordinary age depreciation is not a deduction from a penalty. Overdue payment bears **9.5% for days in 2026**, with 2027's annual rate separately confirmed. [Act §25][law]; [Vero sanction guidance][penalty]; [payment guidance][payment].

## Cross-border points

A nonresident owner still owes Finnish annual tax on Finnish property held at the year's beginning. Foreign real estate is outside this Finnish real-estate tax but can create foreign property tax and Finnish income-tax reporting/relief questions. Finland's annual real-estate tax is not automatically a creditable foreign **income** tax; determine treaty tax coverage and the income computation separately. Tax on a purchase uses the [transfer-tax skill](fi-property-transfer-tax.md); rent and disposal gains use [individual](fi-income-tax.md) or [corporate income tax](fi-corporate-income-tax.md). [Act §§1–5][law].

## Two worked examples that recompute

### 1. Residential building and separate land

Assume Helsinki, sole owner on 1 January, a 100 m² ordinary wooden small house completed in 2005, all ordinary equipment, no cellar/renovation/damage and 20 years' age reduction for 2025 value. Unit EUR 770.58 less 40 × EUR 1.316 = EUR 717.94; replacement EUR 71,794; 25% age reduction leaves EUR 53,845.50. Assume correctly established land value EUR 50,000. At Helsinki's 0.41% building / 1.30% land rates, component tax rounded to cents is EUR 220.77 + 650 = EUR 870.77. The assumed 20-year age and land value must be evidenced in a real case.

```oa-check
name: Finland residential replacement value to annual property tax
inputs:
  floor_area: 100
  base_unit: 770.58
  size_start: 60
  size_reduction_per_m2: 1.316
  age_years: 20
  annual_age_rate: 0.0125
  residential_floor: 0.30
  land_value: 50000
  building_rate: 0.0041
  land_rate: 0.013
steps:
  adjusted_unit: base_unit - (floor_area - size_start) * size_reduction_per_m2
  replacement: floor_area * adjusted_unit
  building_value: replacement * max(residential_floor, 1 - age_years * annual_age_rate)
  building_tax: round(building_value * building_rate, 2)
  land_tax: land_value * land_rate
  annual_tax: building_tax + land_tax
expected:
  adjusted_unit: 717.94
  replacement: 71794
  building_value: 53845.5
  building_tax: 220.77
  land_tax: 650
  annual_tax: 870.77
```

### 2. Land transition and unbuilt-site rate

Assume a Helsinki site satisfies every §12a condition, 2025 mapped value EUR 100,000 and 2024 taxable value EUR 50,000, with no error correction, area minimum or fair-value override. Target EUR 75,000; prior value below 80% of target means a 30% rise to EUR 65,000, below target. At 4.30% annual tax is EUR 2,795 for the sole owner.

```oa-check
name: Finland land value transition to unbuilt site tax
inputs:
  mapped_2025_value: 100000
  target_fraction: 0.75
  prior_2024_taxable_value: 50000
  transition_increase: 0.30
  unbuilt_rate: 0.043
steps:
  target_value: mapped_2025_value * target_fraction
  transition_value: min(target_value, prior_2024_taxable_value * (1 + transition_increase))
  annual_tax: transition_value * unbuilt_rate
expected:
  target_value: 75000
  transition_value: 65000
  annual_tax: 2795
```

## Ask the client first

- Who owned or held each land/building component on 1 January 2026, and in what shares?
- Which municipality, mapped valuation zone, building rights and 2024/2025 values apply?
- What floor/volume, use, construction year, material, equipment, completion and renovation records exist?
- Does permanent residence, unbuilt-site classification or an exemption apply to each component?
- What decision, correction, assessment end date and payments already exist?
- Is there Åland property, a separate building owner or a supported lower fair-value claim?

## Sources

| Official source | Provisions / parameters | Read date |
|---|---|---|
| [Real Estate Tax Act 654/1992][law] | §§1–18,22–26 | 2026-10-26 |
| [Valuation Act 1142/2005][valuation] | Chapter 5, especially §§29–30,32; preceding-year values | 2026-10-26 |
| [Regulation 1073/2025][building] | §§1–22, building values for 2025 used in 2026 tax | 2026-10-26 |
| [Land decision VH/5812/00.01.00/2025][land] | §§1–6, 2025 zone/transition rules | 2026-10-26 |
| [Helsinki 2026 council decision][helsinki] | §262, actual municipal rates | 2026-10-26 |
| [Åland Act 1993:15][aland] | §§1–2a, national incorporation and deviations, read in browser | 2026-10-26 |
| [Vero 2026 decision procedure][decision], [payment calendar][payment], [sanctions][penalty] | Corrections, dates, instalments, fees and 2026 interest | 2026-10-26 |

Not yet confirmed: case-specific municipal zone inputs and actual building features. These are required taxpayer inputs, not assumed national constants. Power plants, extraction rights and other specialist valuations are outside the ordinary scope.

[law]: https://www.finlex.fi/fi/lainsaadanto/1992/654
[valuation]: https://www.finlex.fi/fi/lainsaadanto/2005/1142
[building]: https://www.finlex.fi/fi/lainsaadanto/2025/1073
[land]: https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47235/verohallinnon-paatos--rakennusmaan-verotusarvon-laskentaperusteista4/
[helsinki]: https://paatokset.hel.fi/en/node/242314
[aland]: https://www.regeringen.ax/alandsk-lagstiftning/alex/199315
[rates]: https://www.vero.fi/en/individuals/property/real-estate-tax/value-of-real-estate-and-real-estate-tax-rates/
[decision]: https://www.vero.fi/en/individuals/property/real-estate-tax/
[payment]: https://www.vero.fi/en/individuals/property/real-estate-tax/paying-real-estate-tax/
[penalty]: https://www.vero.fi/en/individuals/property/real-estate-tax/real-estate-tax-decision/late-filing-penalty-fees-and-punitive-tax-increases-in-real-estate-taxation/

> Contributed by Michael Cutajar.

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
