---
name: lc-vat
description: "Saint Lucia VAT for 2026. Covers the 12.5% standard rate (section 10), the tourism rates of 7% for tourism accommodation and 10% for restaurant food and drink, water sports, tours and attractions (SI 188 of 2020), registration within 10 working days once taxable supplies exceed EC$400,000 in 12 months or are expected to in 365 days, the three-month test (over EC$100,000 with the year expected over EC$400,000), special registrations, and the return within 21 calendar days, nil returns included. Trigger phrases include Saint Lucia VAT, St Lucia VAT registration, VAT 12.5% Saint Lucia."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lc-vat"
  jurisdiction: "LC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Saint Lucia VAT

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Value Added Tax in Saint Lucia for 2026 under the Value Added Tax Act (Revised Laws of Saint Lucia 2023, Attorney General Chambers) and the tourism rate order. Covers rates, registration and returns. Amounts are EC$. VAT on services bought from abroad is in [lc-imported-services-vat](lc-imported-services-vat.md). Input recovery, exemptions, imports of goods, payment mechanics and the Health and Citizen Security Levy are outside this skill.

## Ask the client first

1. Taxable supplies in the last 12 months, the last 3 months, and a supportable forecast for the next 365 days.
2. Is the person an auctioneer, a promoter of public entertainment or a licensee or proprietor of a place of public entertainment, the State or a local authority?
3. Is it a related person or acting together with another person making taxable supplies?
4. What is supplied: tourism accommodation, restaurant food and drink, water sports, tours, attractions, other?
5. Prices inclusive or exclusive of VAT; the tax period.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Standard rate | 12.5% of the value of taxable supplies and imports, except zero-rated supplies (s.10(1)) | [VAT Act s.10](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-10) |
| Tourism accommodation service | 7% | [VAT (Tourism) order, SI 188 of 2020, para.3](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-3-01) |
| Restaurant food and beverages (alcohol included), water sports, tours within Saint Lucia, heritage sites and attractions | 10% | same |
| Registration, 12-month test | Taxable supplies over EC$400,000 in any period of 12 or fewer months: apply within 10 working days of its end (s.12(1)(a)) | [VAT Act s.12](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-12) |
| Registration, forward test | Reasonable grounds to expect over EC$400,000 in a 365-day period: apply within 10 working days of its start (s.12(1)(b)) | same |
| Registration, three-month test | Over EC$100,000 in 3 months and those months plus the next 9 expected over EC$400,000: apply within 10 working days after the 3rd month (s.12(10), (11)) | same |
| Public entertainment | Apply at least 5 working days before the event if supplies in 12 months including it are expected over EC$400,000 (s.12(9)) | same |
| Return | Within 21 calendar days after each tax period, whether or not tax is payable (s.37(1)) | [VAT Act s.37](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-37) |

### Steps

1. **Test** taxable supplies (valued under s.20) against the three tests; the Comptroller may add a related person's supplies (s.12(2)).
2. **Exceptions:** no registration duty where the excess came only from ceasing or shrinking the activity or replacing old capital goods (s.12(4)). A nonresident counts only supplies made in Saint Lucia (s.12(8)).
3. **Special triggers:** auctioneers on becoming an auctioneer (s.12(7)); the State and local authorities from the start of a taxable activity (s.12(6)); public entertainment under s.12(9).
4. **Rate:** 12.5% unless zero-rated or a tourism rate applies; inside an inclusive price the tax is price x 12.5/112.5.
5. **Return** within 21 calendar days after the period, nil returns included.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Old brochures quoting a lower threshold | Superseded; the Act (as amended by Act 5 of 2016) says EC$400,000 | [VAT Act s.12](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-12) |
| Supplies of exactly EC$400,000 | "Exceeded" is not met by 400,000; check the other tests | same |
| Hotel charging room, restaurant and spa | Room 7%, restaurant 10%, other items at their own rate; do not apply 7% to the whole bill | [SI 188 of 2020](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-3-01) |
| Tour operator buying transport from a third party | Indirect transport supplies by a tour operator are excluded from the 10% tour rate | same |
| Filing the return | Does not prove payment; keep the two separate | [VAT Act s.37](https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-37) |

## Worked cases

### Case 1: standard rate both ways and a hotel bill

A standard-rated supply of EC$8,000: VAT 1,000, total 9,000; the VAT inside 9,000 inclusive is 1,000. A hotel bill of 2,000 for rooms and 500 for restaurant meals carries 140 and 50.

```oa-check
name: Saint Lucia VAT 12.5%, tax fraction and tourism rates
inputs:
  net: 8000
  rooms: 2000
  meals: 500
steps:
  - vat: net * 0.125
  - gross: net + vat
  - fraction: gross * 0.125 / 1.125
  - room_vat: rooms * 0.07
  - meal_vat: meals * 0.10
expected:
  vat: 1000
  gross: 9000
  fraction: 1000
  room_vat: 140
  meal_vat: 50
```

### Case 2 (decision): register now under the three-month test?

A business made taxable supplies of EC$120,000 in three months and has a supported forecast of 300,000 for the next nine. 120,000 is 20,000 over 100,000 and 420,000 is 20,000 over 400,000, so both parts are met: apply within 10 working days after the third month. With a forecast of 260,000 the year totals 380,000, under 400,000; the three-month test is not met, but keep checking the 12-month and forward tests.

```oa-check
name: Saint Lucia three-month registration test
inputs:
  three_months: 120000
  next_nine: 300000
  low_nine: 260000
steps:
  - over_quarter: three_months - 100000
  - year_total: three_months + next_nine
  - over_year: year_total - 400000
  - low_year: three_months + low_nine
expected:
  over_quarter: 20000
  year_total: 420000
  over_year: 20000
  low_year: 380000
```

## When to refuse or refer

- Input deductions, apportionment, zero-rating and exemption lists, refunds.
- Payment due dates and penalties: not read for this skill.
- The Health and Citizen Security Levy and any post-2023 amendment.

## Filing and payment

1. Apply for registration within the deadline of the test met (s.12).
2. File the return for each tax period within 21 calendar days after it ends, even if nil (s.37(1)), subject to s.38.
3. Keep registration evidence, supply classification and separate rate calculations; reconcile output VAT to invoices.

## Completion checklist

- All three tests and special triggers checked.
- 12.5%, 7% or 10% applied by supply.
- Return within 21 days.

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Act s.10, Revised Laws 2023: read for the 12.5% rate | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-10 | 2026-11-14 |
| VAT Act s.12: read for the EC$400,000 and EC$100,000 tests, 10 working days, related persons, exceptions, auctioneers, the State, nonresidents and public entertainment | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-12 | 2026-11-14 |
| VAT Act s.37: read for the 21-day return, nil returns included | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-37 | 2026-11-14 |
| VAT (Tourism) order SI 188 of 2020, para.3: read for the 7% and 10% rates and the tour operator transport exclusion | https://attorneygeneralchambers.com/laws-of-saint-lucia/value-added-tax-act/section-3-01 | 2026-11-14 |

Not yet confirmed: amendments after the 2023 revision (none found on the Attorney General Chambers pages); the payment due date and penalties; the Health and Citizen Security Levy.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lc-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lc-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
