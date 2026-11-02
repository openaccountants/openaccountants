---
name: er-vat-gst
description: "Eritrea has no VAT or GST. This covers sales and excise tax under Proclamation 64/1994 as amended by Proclamation 117/2001: the 5%, 10% and 12% rates, exempt supplies, excise schedule, raw material rebate, monthly declarations and penalties. Covers tax year 2026 in Eritrea from the gazette text. Use for questions such as: does Eritrea have VAT, sales tax rate in Eritrea, excise on beer in Eritrea, sales tax on accounting services."
jurisdiction: ER
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea VAT / GST

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The newest income tax text we could open is Legal Notice 119/2012 and the newest sales tax text is Proclamation 117/2001. The Ministry of Justice list dated 2023 shows no later amendment to either. Nothing dated 2023 to 2026 could be opened, so check with the Inland Revenue Department that no later change exists.

## Who this applies to

Producers, importers and service providers named in Proc 64/1994 art 4. Eritrea has no VAT or GST: the tax is a sales tax with no general input credit, only the raw material rebate. No registration threshold appears in the texts read.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Listed goods (Schedule A) | 5% | Food, raw materials, medicines and others listed; local or imported | Proc 117/2001 art 2, new art 5(1)(a), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf |
| Other goods | 12% | Not in Schedule A or D | same |
| Listed services (Schedule B) | 5% | Contractors, salons, tailoring, repairs, training, printing, internet | same |
| Listed services (Schedule C) | 10% | Legal, audit and accounting, lodging, consultancy, rentals, garages, software | same |
| Any other service | 10% | Not in B, C or E, unless regulations say otherwise | same |
| Benzene, gas oil | 0.45 and 0.10 Nakfa a litre | Sales tax | same |
| Exempt | 0 | Schedule D goods; Schedule E services such as water, electricity, banking, insurance, education, transport, medical | same |
| Mineral water excise | 15% or 0.20 a litre | Whichever higher | Proc 117/2001 Schedule F, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf |
| Soft drinks excise | 15% or 0.30 a litre | Whichever higher | same |
| Beer excise | 100% or 3.00 a litre; draft 2.15 | Whichever higher | same |
| Wine excise | 50% or 2.00 a litre | Whichever higher | same |
| Spirits excise | 50% or 3.00 a litre | Whichever higher | same |
| Cigarettes excise | 100% or 100.00 a kg | Whichever higher | same |
| Chewing tobacco, snuff excise | 100% or 20.00 a kg | Whichever higher | same |
| Cars excise | 25%; 35% over 1,800 cc | Automobiles | same |
| Land Rover, Land Cruiser, jeep excise | 35% |  | same |

## The base

Sales tax base (art 6): local goods, the wholesale price of the producer plus any excise paid; imports, cost, insurance and freight plus customs duty and any excise paid; local services, the service charge. Excise on imports starts from cost, insurance and freight (art 11). A local producer may deduct sales tax paid on raw materials from sales tax on finished goods, in proportion to actual use, with any excess refunded, if books are acceptable (art 9; Legal Notice 22/1995). Tax on pure alcohol used as raw material is not refunded. Construction contractors pay 5% after deducting raw material cost, or on the service charge for a service-only contract (Legal Notice 22/1995).

## Deadlines and filing

Monthly declaration on the prescribed form, with payment, within one month of the sale (arts 8, 14; Legal Notice 22/1995). Importers pay at clearance. Wholesalers and producers give a monthly list of purchasers with address, licence number and identification number in the next month. Producers keep a daily production record, signed monthly. Tax on closure is due within one month. The Department can assess within five years of the declaration (art 13). Steps: complete the Schedule form, deliver it with payment to the Inland Revenue Department, keep the receipt.

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Not declaring and paying | 20% of tax assessed | Proc 64/1994 art 18(1) |
| Late payment | 5% a month or part, up to 50% | art 18(2) |
| No acceptable sales books | 20% of tax assessed | art 18(3) |

A producer in default can be barred from removing goods until excise is paid (art 12).

## Cross-border points

Goods re-exported are exempt (Legal Notice 22/1995 art 16 list). No reverse charge exists in the texts read.

## Two worked examples that recompute

**Case 1: accountancy fee of 10,000 Nakfa.** Schedule C, 10%: 1,000.

```oa-check
name: Service fee
inputs:
  fee: 10000
steps:
  - tax: fee * 0.10
expected:
  tax: 1000.00
```

**Case 2, a decision: is keeping acceptable books worth it for a producer?** Sales 100,000 at 12%, raw material tax paid 3,000. With acceptable books net tax is 9,000; without the rebate it is 12,000.

```oa-check
name: Raw material rebate
inputs:
  sales: 100000
  input: 3000
steps:
  - gross: sales * 0.12
  - net: gross - input
  - saving: gross - net
expected:
  net: 9000.00
  saving: 3000.00
```

## Ask the client first

- Goods or services, and which schedule?
- Produced locally or imported?
- Excise item, and quantity?
- Books acceptable to the Department?
- Re-export or exempt use?

## Sources

| Source | URL | Read on |
|---|---|---|
| Sales and Excise Tax Proclamation 64/1994, arts 4 to 18 read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-64-1994/eritrean-proc-64-1994.pdf | 2026-11-01 |
| Proclamation 117/2001, operative text and schedules read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf | 2026-11-01 |
| Sales and Excise Tax Regulations, Legal Notice 22/1995, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-22-1995/eritrean-notice-22-1995.pdf | 2026-11-01 |
| Legal Notice 51/2001, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-51-2001/eritrean-notice-51-2001.pdf | 2026-11-01 |
| Ministry of Justice, thematic list of domestic legislations, section 16 read | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-01 |

Scans were read by OCR and the key rate pages checked by eye. The Library of Congress item pages show a security check, which we did not pass; the PDFs came straight from its public file host. Scanned gazettes use "Birr" in 1994 and "Nakfa" in later amendments.

Not yet confirmed: Old guide items dropped as unsupported: 4% goods rate and "Legal Notice 64/1994" (it is Proclamation 64/1994). Notice 51/2001 repealed arts 3 and 11 of Legal Notice 22/1995, and the effect on the construction and service lists above was not settled. Exact article numbers within Notice 22/1995 for the purchaser list. No published 2026 amendment, circular or form could be opened; the Ministry of Finance site did not connect. No official portal or online filing page could be opened either.

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
