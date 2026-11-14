---
name: barbados-vat
description: "Barbados Value Added Tax for 2026, for registrants preparing or reviewing VAT returns in TAMIS. Covers the 17.5% standard rate, 7.5% on accommodation in direct tourism services, 22% on telecommunications services, zero-rating and exempt supplies, the BBD 200,000 registration threshold (BBD 16,666.67 a month) in force since 1 January 2016, promoters of public entertainment, input tax rules, imports and reverse charge. Trigger on Barbados VAT, BRA VAT, VAT return Barbados, 17.5% Barbados, 22% telecoms VAT. Built from BRA pages; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/barbados-vat"
  jurisdiction: "BB"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Barbados VAT v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons registered for VAT under the Value Added Tax Act, Cap. 87, in 2026, administered by the Barbados Revenue Authority (BRA) through TAMIS. A "person" includes an individual, company, partnership, joint venture, trustee and unincorporated bodies such as clubs and cooperatives. Amounts are BBD.

- **In:** standard registrants filing periodic VAT returns.
- **Out (refer):** excise tax, tourism levy, special tourism concessions, partial exemption beyond simple apportionment.

### Refusals

- **R-BB-1:** below the threshold and not registered: no VAT return.
- **R-BB-2:** tourism concessions or hotel incentive certificates: refer.
- **R-BB-3:** mixed taxable and exempt supplies: apportion and flag for review.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Standard rate | 17.5% | Standard supplies | BRA, VAT rates: https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates |
| Accommodation in direct tourism services | 7.5% | Accommodation services | same |
| Telecommunications services | 22% | Telecoms | same |
| Zero rate | 0% | Zero-rated items list | same |
| Registration threshold | BBD 200,000 a year, or BBD 16,667 a month | In force since 1 January 2016 (BBD 80,000 from December 2010 to December 2015) | same |
| Must register | Annual income of BBD 200,000 or more; monthly revenue over BBD 16,666.67; promoters of public entertainment | Documents: incorporation forms 1, 3, 4, 9, 33 for companies; business name forms for others | BRA, who must register for VAT: https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT |
| Exempt supplies | No VAT; no recovery of input tax attributable to them | | BRA, exempt supplies: https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Exempt-Supplies |

## The base

- **Output tax** on taxable supplies at 17.5%, 7.5% or 22%; zero-rated supplies at 0% with recovery.
- **Input tax**: recoverable with a valid tax invoice on purchases for taxable supplies; none on purchases for exempt supplies; apportion common costs.
- **Imports**: VAT at customs on CIF value plus duty (earlier version; see Not yet confirmed).
- **Imported services**: self-assess at 17.5% (earlier version; see Not yet confirmed).
- **Out of scope**: wages, NIS, PAYE, loan repayments, transfers.

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 17.5% |
| Unknown VAT status of a purchase | No credit |
| Unknown counterparty location | Domestic |
| Entertainment, private vehicles, personal use | No credit (earlier version's blocked list, see Not yet confirmed) |

### Supplier patterns (kept)

| Pattern | Treatment |
|---|---|
| Republic Bank, CIBC FirstCaribbean, RBC, Scotiabank, Sagicor (fees, interest) | Financial services: treat as exempt pending review |
| BRA, NIS, government fees | Exclude |
| Barbados Light and Power | Check the bill for VAT |
| Flow, Digicel (telecoms) | 22% VAT on telecommunications; credit if business |
| Google, Microsoft, Adobe, Zoom, Anthropic, OpenAI (non-resident) | Imported service, self-assess (see Not yet confirmed) |
| Salaries, NIS, PAYE, own transfers | Exclude |

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Register in TAMIS with the documents BRA lists | On reaching the threshold, or as a promoter of public entertainment |
| 2 | Issue tax invoices | Each taxable supply |
| 3 | File the VAT return for each filing period in TAMIS and pay | Filing periods are two months (for example 1 December to 31 January as period 1); due date see Not yet confirmed |

## Penalties and interest

Not confirmed on the pages read; see Not yet confirmed.

## Cross-border points

- Exports are zero-rated (earlier version); keep export evidence.
- Non-resident digital and professional services: self-assess (see Not yet confirmed).

## Two worked examples that recompute

### Example 1: Two-month return, hotel with rooms and a restaurant

Room revenue BBD 400,000 at 7.5% = BBD 30,000; restaurant sales BBD 200,000 at 17.5% = BBD 35,000; output BBD 65,000. Input VAT with valid invoices BBD 22,000. VAT payable BBD 43,000.

```oa-check
name: BB VAT 2026 hotel return, accommodation and restaurant
inputs:
  rooms: 400000
  restaurant: 200000
  input_vat: 22000
steps:
  - vat_rooms: rooms * 0.075
  - vat_restaurant: restaurant * 0.175
  - output: vat_rooms + vat_restaurant
  - payable: output - input_vat
expected:
  vat_rooms: 30000
  vat_restaurant: 35000
  output: 65000
  payable: 43000
```

### Example 2: Must a consultant register? Revenue BBD 190,000 or BBD 210,000

At BBD 190,000 the consultant is BBD 10,000 under the BBD 200,000 threshold (monthly average BBD 15,833.33, under BBD 16,666.67). At BBD 210,000 the consultant must register (monthly BBD 17,500), and BBD 210,000 of standard-rated fees would carry BBD 36,750 of VAT.

```oa-check
name: BB VAT 2026 registration test both ways
inputs:
  threshold: 200000
  low: 190000
  high: 210000
steps:
  - gap_low: threshold - low
  - monthly_low: round(low / 12, 2)
  - monthly_high: high / 12
  - vat_high: high * 0.175
expected:
  gap_low: 10000
  monthly_low: 15833.33
  monthly_high: 17500
  vat_high: 36750
```

### Short cases kept from the earlier version

- Domestic sale BBD 11,750 VAT-inclusive at 17.5%: net BBD 10,000, VAT BBD 1,750.
- Hotel room BBD 1,075 VAT-inclusive at 7.5%: net BBD 1,000, VAT BBD 75.
- Export: zero-rated, inputs recoverable.
- Bank charges: treat as exempt pending review; no input credit.

## Ask the client first

1. Registered for VAT, and which filing period?
2. Sales by rate: 17.5%, 7.5% accommodation, 22% telecoms, zero-rated, exempt.
3. Imports and imported services in the period.
4. Purchases with valid tax invoices, and any for exempt supplies.
5. Credit brought forward.

## Sources

| Source | URL | Read on |
|---|---|---|
| BRA, VAT rates: read for the 0%, 7.5%, 17.5% and 22% rates and the threshold history | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates | 2026-11-14 |
| BRA, who must register for VAT: read for the registration tests and documents | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT | 2026-11-14 |
| BRA, exempt supplies: read for the no-recovery rule | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Exempt-Supplies | 2026-11-14 |
| BRA, VAT filing periods: read for the two-month periods table | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/What-are-the-VAT-Filing-Periods | 2026-11-14 |

Not yet confirmed: the return due date (earlier version: 21st of the month after the period); the zero-rated list (earlier version: exports, basic food items, prescription drugs) and the exempt list (financial services, residential rent, education, medical, insurance); the 7.5% rate scope beyond accommodation; blocked inputs (entertainment, personal vehicles); import VAT base and reverse charge on imported services; the 21-day registration deadline; penalties and interest; the earlier version's description of hotel accommodation as the only reduced rate (BRA lists 22% on telecoms too).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `barbados-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/barbados-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
