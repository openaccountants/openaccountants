---
name: ky-vat-gst
description: >
  Cayman Islands indirect tax for 2026. There is no VAT, GST or sales tax, no
  registration, no returns and no reverse charge. What applies instead is
  import duty under the Customs Tariff Act (2026 Revision), 22% on most goods
  with 0%, 12%, 17%, 27% and 42% lines and specific duties such as beer at
  CI$1.95 a litre, and the 13% tourist accommodation tax on room charges to
  tourists. Trigger on Cayman VAT, Cayman GST, Cayman sales tax, Cayman import
  duty, Cayman customs duty, Cayman hotel tax. Built from Cayman legislation;
  not reviewed by an accountant.
version: 1.0
jurisdiction: KY
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: vat-gst
type: situation-rules
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

## The base

### Import duty

1. Classify the goods to the tariff line (heading and subheading) in the Customs Tariff Act Schedule.
2. Read the rate on that line: a percentage, or a specific amount per unit (litre, kilogram, number).
3. Apply it to the value for duty, or to the quantity for a specific duty.
4. Pay Customs and Border Control on entry. Duty paid is a cost; nothing is recoverable later because there is no VAT credit system.

Duty concessions in development agreements and other exemptions: flag for a practitioner. A drawback scheme exists for the marine industry (Marine Industry (Import Duty and Tonnage Tax) (Drawback) Act): refer.

### Accommodation tax

The proprietor pays 13% of the room charges made to each tourist, meaning a person not ordinarily resident who stays up to six months. The proprietor keeps records and gives each departing tourist a statement (s. 4).

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
| Duty rate on an import | 22% until the line is checked |
| Guest status | Tourist (13% applies) unless shown to be ordinarily resident |

## Deadlines and filing

- Import duty: paid on entry of the goods.
- Accommodation tax: the Act requires records and a statement to each tourist; the payment schedule is not confirmed in this version.
- No VAT returns exist.

## Penalties and interest

Customs and accommodation tax penalties were not read for this version; refer any dispute.

## Cross-border points

- Exports carry no Cayman tax.
- Imported services carry no Cayman tax.
- Goods brought in by visitors and residents are subject to the same tariff, subject to allowances not confirmed here.

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
| Tourist Accommodation (Taxation) Act (2013 Revision): read for ss. 2 to 4, the thirteen per cent rate, timeshare rule, tourist definition and records | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0168/1964-0168_2013%20Revision.pdf | 2026-11-14 |

Not yet confirmed: the value for duty (the old files said CIF value; the Customs and Border Control Act was not read); the old ranges "food 15% to 22%", "motor vehicles 29.5%, luxury 42%" (vehicle lines were not checked line by line); the accommodation tax payment date and penalties; visitor and returning resident allowances; fuel duties per gallon.
