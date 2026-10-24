---
name: no-individual-residence
description: >
  Screen Norwegian individual residence on arrival and emigration, prepare
  rolling-presence records and distinguish domestic residence from a treaty
  claim. Income-specific, exit, statutory and independent review remain open.
jurisdiction: "NO"
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Norway individual residence screening v0.1

## Who this applies to

Use this draft for individuals moving to or from Norway or making repeated visits. It complements the existing [Norway–Switzerland exit corridor](norway-to-switzerland-wealth-tax-exit.md); it does not reverify that corridor or compute exit tax.

## Arrival: rolling presence tests

The authority identifies residence where presence exceeds **183 days in twelve months** or **270 days in thirty-six months**. Whole and part days count, visits need not be consecutive and their purpose does not change the count. Test rolling windows rather than isolated calendar-year averages. [Global tax liability][arrival]

Where the first-year stay exceeds 183 days, the guidance starts residence from the first day. If the relevant days span two income years, it describes residence from 1 January of the second year. Under the 270-day route, it describes residence from 1 January of the year the threshold is exceeded. Preserve the actual chronology before selecting an effective date. [Global tax liability][arrival]

The page distinguishes global income/wealth liability from limited liability that can remain without residence. Exactly meeting a threshold is not exceeding it, but the other route and any existing residence must still be assessed. [Global tax liability][arrival]

## Departure: permanent relocation is not the only condition

The emigration guidance requires permanent residence abroad, no more than **61 days in Norway** in the relevant year and no qualifying Norwegian home available to the individual or related parties. Partial days count. For prior residence under ten years, it describes cessation when all required conditions are satisfied. [Tax emigration guidance][departure]

For ten years or more, continued liability covers the departure year and at least three following years, with the day/home conditions required during those following years. The guidance discusses holiday homes and a qualifying five-year property exception; ownership of any property is not automatically fatal or automatically acceptable. Establish the property's use and legal availability. [Tax emigration guidance][departure]

Claim cessation through the tax return's emigration section. Moving registration and a foreign address alone do not prove an accepted tax-emigration result. The exact historical-residence computation, home exceptions, effective dates and special cases still need statutory review. [Tax emigration guidance][departure]

## Treaty residence and evidence

Domestic residence can continue while a treaty restricts Norway's taxing rights. Apply the actual residence article, supported by foreign fiscal-residence confirmation for the relevant treaty and period. The authority still makes its own treaty assessment; a certificate does not conclusively determine the result. [Tax-liability guidance][treaty]

The guidance requires the treaty-residence claim in each relevant year's return and keeps return obligations where domestic residence continues. Income and wealth provisions must be checked separately: some treaties do not cover wealth. Do not assume that a foreign treaty-residence finding eliminates every Norwegian tax or filing obligation. [Tax-liability guidance][treaty]

## Preparation workpaper

This is our evidence framework, not a substitute for the legal residence test:

1. Identify prior Norwegian residence periods and whether earlier tax emigration was accepted.
2. Reconcile passports, travel bookings, work records and accommodation to every whole/part day.
3. Build both rolling-window schedules, preserving overlapping periods without duplicate days.
4. Record the relocation date, permanent foreign arrangements and Norwegian/foreign home availability.
5. Identify relevant family/related-party housing rights and actual property use.
6. Inventory Norwegian and foreign income, assets, debts and any potential exit event.
7. Obtain treaty evidence, claims, assessments and authority decisions for each relevant year.

A spreadsheet should show the counting assumptions and evidence gaps. Do not infer approved emigration or treaty residence merely from its arithmetic.

## Worked examples

### 1. Repeated visits exceed the longer window

Assume 80, 90 and 110 non-overlapping Norwegian presence days all fall in one relevant thirty-six-month window. Total 280 exceeds 270 by ten. This tests that presence limb only; actual dates and the applicable effective-year rule must be established separately.

```oa-check
name: Norway assumed rolling thirty six month presence
inputs:
  first_period_days: 80
  second_period_days: 90
  third_period_days: 110
  presence_threshold: 270
steps:
  total_days: first_period_days + second_period_days + third_period_days
  excess_days: total_days - presence_threshold
expected:
  total_days: 280
  excess_days: 10
```

### 2. Long-residence emigration window

Assume relocation in 2026 after at least ten years of prior residence and all required following-year conditions are satisfied. The three following years are 2027–2029; 2030 is the year after that window. This does not approve cessation or calculate exit tax, and no automatic status change should be booked from this arithmetic alone.

```oa-check
name: Norway assumed long residence departure year schedule
inputs:
  relocation_year: 2026
  following_years: 3
steps:
  last_following_year: relocation_year + following_years
  year_after_window: last_following_year + 1
expected:
  last_following_year: 2029
  year_after_window: 2030
```

## Ask the client first

- What previous residence and tax-emigration decisions apply?
- What are the exact travel, work and relocation dates?
- Which homes were available to the individual and related parties, and how were they used?
- What foreign fiscal-residence evidence and treaty claims exist?
- What income, assets, debts, disposals and transfers require separate tax analysis?

## Sources and review limits

Official Tax Administration text retrieved in the search index on 23 October 2026:

- [Global tax liability][arrival].
- [Tax emigration][departure].
- [Tax liability and treaty residence][treaty].

Not yet confirmed: current Taxation Act section 2-1 and full amendments, precise home/family and historical-residence cases, each treaty and modifications, exit rules, income/wealth source and credit rules, live forms and procedural deadlines. Independent review and professional attestation remain outstanding. Cross-border and country coverage remain partial.

[arrival]: https://www.skatteetaten.no/en/person/to-from-norway/from/tax-when-you-move-abroad/global-tax-liability/
[departure]: https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/utland/skattemessig-emigrasjon/
[treaty]: https://www.skatteetaten.no/en/person/taxes/get-the-taxes-right/abroad/tax-residence-in-norway-when-moving-to-or-from-norway/
