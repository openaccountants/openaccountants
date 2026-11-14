---
name: vc-vat
description: >
  Saint Vincent and the Grenadines VAT for 2026. Covers the 16% standard rate, 11% on
  accommodation rooms, zero rating and exemption, registration for businesses with
  annual sales of EC$300,000 and for every public entertainment promoter and hotelier
  (guest houses and apartments included), returns and payment by the 15th of the next
  month, 1.5% monthly interest, the tax fraction, and the separate EC$8 a night Climate
  Resiliency Levy. Trigger phrases include SVG VAT, St Vincent VAT 16%, VAT
  registration St Vincent, accommodation VAT 11%.
version: 1.0
jurisdiction: VC
tax_year: 2026
last_updated: 2026-11-14
category: international
type: situation-rules
domain: vat-gst
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Vincent and the Grenadines VAT

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Value Added Tax in Saint Vincent and the Grenadines for 2026, as published by the Inland Revenue Department (IRD). Covers rates, registration, returns and output tax arithmetic. Amounts are EC$. The VAT Act PDF on the IRD site is the 2009 revised issue and is not used for current figures. Input credits, imports, refunds and exemption lists are outside this skill. Company tax: [vc-corporate-income-tax](vc-corporate-income-tax.md).

## Ask the client first

1. Annual sales, and whether the business is a public entertainment promoter or a hotelier, guest house or apartment.
2. What is supplied: rooms, food, tours, other goods and services; any zero-rated or exempt supplies?
3. Prices inclusive or exclusive of VAT?
4. Room nights for transient visitors (Climate Resiliency Levy).
5. Tax period and VAT collected.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Standard rate | 16% | [IRD taxes page](https://ird.gov.vc/index.php/taxes) |
| Accommodation (rooms) | 11% | same |
| Zero-rated | 0% | same |
| Exempt | No rate | same |
| Registration | Businesses grossing EC$300,000 in sales a year; all promoters of public entertainment; all hoteliers including guest houses and apartments | same |
| Return and payment | On or before the 15th of the month after the tax period | same |
| Interest | 1.5% a month | same |
| Climate Resiliency Levy | EC$8 per night per room for transient visitors at any visitor accommodation; due by the 15th of the next month | same |

### Steps

1. **Register** if sales reach EC$300,000 a year, or at once if a promoter of public entertainment or any hotelier, whatever the turnover.
2. **Classify** each supply: rooms 11%, other taxable supplies 16%, zero-rated 0%, exempt.
3. **Output tax:** net x rate; inside an inclusive price, price x 16/116 (or 11/111).
4. **Return and pay** by the 15th of the following month; June's return and payment are due 15 July.
5. **Climate Resiliency Levy:** EC$8 per room per night on top, remitted by the 15th.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Guest house with sales well below the general figure | Must register: all hoteliers register whatever their sales | [IRD taxes page](https://ird.gov.vc/index.php/taxes) |
| Hotel package with room and meals | Room 11%, meals 16%; split the price | same |
| Sales of exactly EC$300,000 | The IRD wording ("grossing in sales of $300,000") does not settle the boundary; treat as registrable until the Act is checked | same |
| Exempt against zero-rated | Different treatments; keep them apart in the records | same |
| Older VAT Act text | 2009 revised issue; not a current rate authority | [VAT Act PDF](https://ird.gov.vc/images/pdf/VAT_Act_Cap_445.pdf) |

## Worked cases

### Case 1: standard and room rates both ways

A standard-rated charge of EC$1,000: VAT 160, total 1,160. A room charge of 1,000: VAT 110, total 1,110. Inside 2,900 inclusive of 16% VAT the tax is 400.

```oa-check
name: SVG VAT 16% and 11%, and the tax fraction
inputs:
  net: 1000
  gross_std: 2900
steps:
  - std_vat: net * 0.16
  - room_vat: net * 0.11
  - fraction_vat: gross_std * 0.16 / 1.16
expected:
  std_vat: 160
  room_vat: 110
  fraction_vat: 400
```

### Case 2 (decision): split a hotel package or charge one rate?

A 3-night package is 1,500 net: rooms 1,000 and meals 500. Split correctly, VAT is 110 + 80 = 190. Charging 11% on the whole package gives 165, understating VAT by 25. The Climate Resiliency Levy adds 3 x 8 = 24 for one room.

```oa-check
name: SVG hotel package split, rooms 1,000 and meals 500
inputs:
  rooms: 1000
  meals: 500
  nights: 3
steps:
  - split_vat: rooms * 0.11 + meals * 0.16
  - single_rate_vat: (rooms + meals) * 0.11
  - understatement: split_vat - single_rate_vat
  - levy: nights * 8
expected:
  split_vat: 190
  single_rate_vat: 165
  understatement: 25
  levy: 24
```

## When to refuse or refer

- The exact registration tests (forecast, aggregation, deadline) and the current Act text.
- Input credits, imports, imported services, deposits, service charges and refunds.
- Penalty amounts (the IRD page names penalties without amounts).

## Filing and payment

1. Register with the IRD.
2. File and pay by the 15th of the month after each tax period ([IRD taxes page](https://ird.gov.vc/index.php/taxes)).
3. Reconcile sales by rate to invoices, credits and adjustments to the return; keep filing and payment confirmations.

## Completion checklist

- Registration duty checked, hoteliers and promoters included.
- 16% or 11% by supply; packages split.
- Filed and paid by the 15th; levy remitted.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD taxes page: read for the VAT rates (16%, 11%, 0%, exempt), who registers, the 15th of the month deadline, 1.5% interest and the Climate Resiliency Levy of EC$8 a night | https://ird.gov.vc/index.php/taxes | 2026-11-14 |
| VAT Act Cap. 445 PDF on the IRD site (scanned, OCR of pages 1 and 2): read for its revision (Issue 1/2009, amendments to Act 1 of 2008), so not used for current figures | https://ird.gov.vc/images/pdf/VAT_Act_Cap_445.pdf | 2026-11-14 |

Not yet confirmed: the VAT Act as amended (registration tests, deadlines, exempt and zero-rated lists); penalty amounts; whether the EC$300,000 test is "equal to or more" or "more than".
