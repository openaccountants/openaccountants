---
name: ky-vat-gst
description: "Cayman Islands indirect tax for 2026. There is no VAT, GST or sales tax, no registration, no returns and no reverse charge. What applies instead is import duty under the Customs Tariff Act (2026 Revision), 22% on most goods with 0%, 12%, 17%, 27% and 42% lines and specific duties such as beer at CI$1.95 a litre, and the 13% tourist accommodation tax on room charges to tourists. Trigger on Cayman VAT, Cayman GST, Cayman sales tax, Cayman import duty, Cayman customs duty, Cayman hotel tax. Built from Cayman legislation; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ky-vat-gst"
  jurisdiction: "KY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Cayman Islands: no VAT, and the duties that apply instead

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Businesses and individuals buying, selling or importing in the Cayman Islands in 2026, and anyone asked to "do the Cayman VAT return".

**There is no VAT, GST or general sales tax.** No such Act is in the current legislation list, so there is no registration, threshold, return, input credit or reverse charge on imported services. Never prepare a VAT return for a Cayman business. Local sales and services carry no consumption tax; goods carry import duty at the border, and hotel and other tourist accommodation carries the accommodation tax.

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| VAT, GST, sales tax | None | No such Act in the current legislation list | Cayman legislation, current by title: https://legislation.gov.ky/cms/legislation/current/by-title.html |
| Import duty, general rate | 22% | Rate shown on most tariff lines (for example yogurt 0403.10.00, portable computers 8471.30.00, office furniture 9403.30.00) | Customs Tariff Act (2026 Revision), Schedule: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2012/2012-0001/2012-0001_2026%20Revision.pdf |
| Import duty, nil | 0% | Lines shown at 0%, for example electric motor vehicles for personal use 8703.80.10 | same |
| Import duty, aerated waters and non-alcoholic drinks | 27% | For example 2202.10.20, 2202.90.10 | same |
| Import duty, higher lines | 42% | For example cigarette paper 4813.00.00, lighter fuel containers 3606.10.00 | same |
| Other ad valorem rates | 12%, 17%, 29.50% on particular lines | Read the line for the item | same |
| Beer | CI$1.95 a litre | 2203.00.00, specific duty | same |
| Tourist accommodation tax | thirteen per cent of the charges for each tourist | Paid by the proprietor; timeshare owners, their guests and exchangers: US$10 a room a day | Tourist Accommodation (Taxation) Act (2013 Revision), s. 3: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168_2013%20Revision.pdf |
| Accommodation tax return and payment | Within 28 days after the end of the month of supply | Copies of the tourist statements go to the Collector of Taxes with the payment | same, s. 7 |
| Accommodation tax default surcharge | 20% of the tax due for the month | Statements not submitted or tax not paid in full by the deadline | same, s. 8 |
| Value for duty, uninsured goods | Notional insurance of 1% of cost and freight | Value is the normal open-market price at entry, including freight and insurance to the import point | Customs and Border Control Act (2024 Revision), s. 44: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0034/2018-0034_2024%20Revision.pdf |
| Customs entry | Before or within 7 days of landing, from the date of report | | same, s. 17(1) |
| Returning resident allowance | Up to CI$1,000 for 1 July to 31 August 2026 and 23 November 2026 to 7 January 2027; otherwise up to CI$800 from 1 September 2026 | Personal and household goods accompanying the passenger, at the Director's discretion | Customs Tariff (Amendment of Schedule 2) Order 2026, SL 33 of 2026, para 2: https://gov.ky/documents/35692/0/CustomsTariff%28AmendmentofSchedule2%29Order2026_MADE.pdf/6764b881-1563-1c4f-4eac-d526acaf3136?t=1782940267024 |
| Departure tax | CI$26 a traveller by air or non-cruise vessel; CI$6 a cruise ship tourist | Collected by the carrier's agent | Travel (Departure Tax and Environmental Protection Fee) Act (2026 Revision), s. 4: https://gov.ky/documents/35692/0/Travel%2B%28Departure%2BTax%2Band%2BEnvironmental%2BProtection%2BFee%29%2BAct%2B%282026%2BRevision%29%2C.pdf/8ce52143-7c33-aeb3-eb13-4b2e8d46aee0?t=1770926366494 |

## The base

### Import duty

1. Classify the goods to the tariff line (heading and subheading) in the Customs Tariff Act Schedule.
2. Read the rate on that line: a percentage, or a specific amount per unit (litre, kilogram, number).
3. Apply it to the value for duty, or to the quantity for a specific duty. The value is the normal open-market price between independent parties, including freight and insurance to the import point; for uninsured goods add a notional 1% of cost and freight (s. 44). Convert the invoice at the exchange rate in force on arrival.
4. Enter the goods before or within 7 days of landing (s. 17) and pay Customs and Border Control on entry. Duty paid is a cost; nothing is recoverable later because there is no VAT credit system.

Duty concessions in development agreements and other exemptions: flag for a practitioner. A drawback scheme exists for the marine industry (Marine Industry (Import Duty and Tonnage Tax) (Drawback) Act): refer.

### Accommodation tax

The proprietor pays 13% of the room charges made to each tourist, meaning a person not ordinarily resident who stays up to six months. The proprietor keeps records and gives each departing tourist a statement (s. 4). Copies of the month's statements and the tax go to the Collector of Taxes within 28 days after the month ends (s. 7); a late or short month bears a 20% surcharge (s. 8). The Department of Tourism publishes the return forms and asks for a nil return for vacant months.

### Bank-statement patterns

| Pattern | Treatment |
|---|---|
| CUSTOMS, CBC, DUTY | Import duty: cost of the goods; no VAT to split out |
| Supplier invoices from Cayman businesses | Whole amount is cost; no tax line to reclaim |
| Hotel or rental income | Gross; 13% accommodation tax is due on tourist charges |
| Foreign SaaS (Google, Microsoft, AWS) | No Cayman tax; no reverse charge |

### Conservative defaults

| Unknown | Default |
|---|---|
| Duty rate on an import | No default: classify the goods to the exact tariff line first (rates run from 0% to 42% and some duties are per unit) |
| Guest status | Tourist (13% applies) unless shown to be ordinarily resident |

## Deadlines and filing

- Import duty: paid on entry of the goods.
- Customs entry: before or within 7 days of landing; duty paid on entry.
- Accommodation tax: statements and payment within 28 days after the end of the month of supply.
- Departure tax: collected by the carrier's agent at departure.
- No VAT returns exist.

## Penalties and interest

Accommodation tax: 20% surcharge on the month's tax if statements are not submitted or the tax not paid in full by the 28-day deadline (s. 8); the Collector can assess missing amounts. Customs penalties were not read for this version; refer any dispute.

## Cross-border points

- Exports carry no Cayman tax.
- Imported services carry no Cayman tax.
- Returning residents: duty relief on accompanying personal and household goods up to CI$800 (CI$1,000 in the two 2026 holiday periods), at the Director's discretion; merchandise is outside the allowance.

## Two worked examples that recompute

### Office equipment import, CI$10,000

```oa-check
name: KY import duty office equipment 10000
inputs:
  value: 10000
  rate: 0.22
steps:
  - duty: value * rate
  - landed: value + duty
  - vat: 0
expected:
  duty: 2200
  landed: 12200
  vat: 0
```

Duty is CI$2,200 and is a cost. There is no VAT to add or reclaim.

### Decision: guesthouse charges to tourists vs residents

A guesthouse bills CI$500 to a tourist and CI$500 to a Cayman resident on a work trip from another island.

```oa-check
name: KY accommodation tax tourist vs resident
inputs:
  charge: 500
steps:
  - tax_tourist: charge * 0.13
  - tax_resident: charge * 0
  - difference: tax_tourist - tax_resident
expected:
  tax_tourist: 65
  tax_resident: 0
  difference: 65
```

The tax applies only to tourists, so the proprietor needs evidence of each guest's status; without it, treat the guest as a tourist.

## Ask the client first

1. Is the question about selling locally, importing goods, or accommodation?
2. For imports: what are the goods (tariff heading), value and quantity?
3. For accommodation: are guests tourists or ordinarily resident, and is it a timeshare?
4. Any duty concession or development agreement?

## Sources

| Source | URL | Read on |
|---|---|---|
| Cayman legislation, current by title: read to confirm no VAT, GST or sales tax Act is in force | https://legislation.gov.ky/cms/legislation/current/by-title.html | 2026-11-14 |
| Customs Tariff Act (2026 Revision, revised as at 31 December 2025): read for the Schedule rates (22% on most lines, 0%, 12%, 17%, 27%, 29.50%, 42%, beer CI$1.95 a litre) | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2012/2012-0001/2012-0001_2026%20Revision.pdf | 2026-11-14 |
| Customs and Border Control Act (2024 Revision): read for s. 17 (7-day entry) and s. 44 (value for duty, 1% notional insurance) | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0034/2018-0034_2024%20Revision.pdf | 2026-11-14 |
| Customs Tariff (Amendment of Schedule 2) Order 2026, SL 33 of 2026: read for the CI$800 and CI$1,000 returning resident allowance | https://gov.ky/documents/35692/0/CustomsTariff%28AmendmentofSchedule2%29Order2026_MADE.pdf/6764b881-1563-1c4f-4eac-d526acaf3136?t=1782940267024 | 2026-11-14 |
| Travel (Departure Tax and Environmental Protection Fee) Act (2026 Revision): read for s. 4, CI$26 and CI$6 | https://gov.ky/documents/35692/0/Travel%2B%28Departure%2BTax%2Band%2BEnvironmental%2BProtection%2BFee%29%2BAct%2B%282026%2BRevision%29%2C.pdf/8ce52143-7c33-aeb3-eb13-4b2e8d46aee0?t=1770926366494 | 2026-11-14 |
| Tourist Accommodation (Taxation) Act (2013 Revision): read for ss. 2 to 4, 7 and 8, the thirteen per cent rate, timeshare rule, tourist definition, records, the 28-day deadline and the 20% surcharge | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168_2013%20Revision.pdf | 2026-11-14 |

Not yet confirmed: the 2% temporary import rate in Act 2 of 2025 (not among the provisions commenced on 1 October 2025); the environmental tax on motor vehicles from 1 October 2025 (CI$1,000 or CI$2,000 by CIF value as reported; the order, SL 36 of 2025, was not read); the 15% building materials rate and Sister Islands waivers announced to 31 December 2030; the accommodation tax interest rate; the old ranges "food 15% to 22%", "motor vehicles 29.5%, luxury 42%" (vehicle lines were not checked line by line); fuel duties per gallon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ky-vat-gst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ky-vat-gst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
