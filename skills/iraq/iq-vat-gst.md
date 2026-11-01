---
name: iq-vat-gst
version: 0.2
description: "Iraq has no VAT or GST. Selective sales tax for tax year 2026: 10% hotels, 300% tobacco and alcohol, 15% cars and tickets, telecom status unverified, payment timing. Written for tax year 2026 from the Iraqi law and General Commission for Taxes pages. Use for questions about federal Iraq; the Kurdistan Region runs its own administration. Trigger phrases: Iraq tax, Iraqi dinar tax, General Commission for Taxes, GCT Baghdad."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq VAT / GST

Tax year: 2026. Iraq has no VAT or GST. It has sales taxes on listed items.

## Who this applies to

Hotels and restaurants of excellent and first class, importers of cars, cigarettes and alcohol, local producers of those, airlines and travel offices, and telecom providers, in federal Iraq. There is no VAT registration threshold, reverse charge or input credit in these instruments.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Excellent and first-class hotels and restaurants, all services | 10% | 2026 | https://tax.mof.gov.iq/uploads/pdf/Law/%D9%82%D8%B1%D8%A7%D8%B1%2036%20%D9%84%D8%B3%D9%86%D8%A9%201997.pdf |
| Cigarettes, all tobacco products, alcohol, imported or local | 300% of value | 2026 | https://tax.mof.gov.iq/uploads/Najwan/law/%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D9%81%D8%B1%D8%B6%20%D9%88%20%D8%AC%D8%A8%D8%A7%D9%8A%D8%A9%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA%20-%20Copy%202.pdf |
| Car imports, on customs declaration value | 15% | 2026 | same |
| Air tickets on Iraqi Airways and national carriers | 15% | 2026 | same |
| unverified: mobile and internet services, Instructions 5 of 2015 set 20%; 2026 status disputed | 20% | 2026 | unverified |

## The base

Hotels: value of all services, on invoices showing the tax. Cars and imported tobacco: value on the customs declaration, collected at border tax units. Tickets: ticket price. These are final revenue with no credit in the instructions.

## Deadlines and filing

- Hotels and restaurants: pay GCT within the first 10 days of the following month (Decision 36 of 1997). GCT's form computes monthly tax; keep the registers.
- Importers: pay at the border unit.
- Local producers, airlines and travel offices, telecom: pay every 3 months, with a report certified by the accountant on the GCT form, in the first half of the month after the quarter.

## Penalties and interest

Hotels: overdraft bank interest on tax not remitted, and the management bears uncollected tax and interest. GCT's form charges late interest per day.

## Cross-border points

Telecom service counts as supplied in Iraq even when its installations are abroad (Instructions 5, art. 2). Foreign currency hotel bills convert at the Central Bank's rate. Customs changes under Cabinet Decision 957 were reported for 2026 but no official text was opened; see Sources.

## Two worked examples that recompute

First-class hotel, bill IQD 1,000,000.

```oa-check
name: Hotel bill
inputs:
  bill: 1000000
steps:
  - tax: bill * 0.10
expected:
  tax: 100000
```

Decision: import cigarettes at declared IQD 10m, or a car at the same value. The cigarettes carry IQD 28.5m more tax.

```oa-check
name: Cigarettes against car
inputs:
  value: 10000000
steps:
  - cigarettes: value * 3
  - car: value * 0.15
  - gap: cigarettes - car
expected:
  gap: 28500000
```

## Ask the client first

- What is supplied or imported?
- Hotel or restaurant grade?
- Imported or locally produced?
- Federal Iraq or Kurdistan Region?

## Sources

## Sources

| Source | URL | Read on |
|---|---|---|
| Sales Tax Instructions 5 of 2015 (scan, read in full by OCR) | https://tax.mof.gov.iq/uploads/Najwan/law/%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D9%81%D8%B1%D8%B6%20%D9%88%20%D8%AC%D8%A8%D8%A7%D9%8A%D8%A9%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA%20-%20Copy%202.pdf | 2026-11-01 |
| Decision 36 of 1997 and Instructions 2 of 1997, hotels and restaurants | https://tax.mof.gov.iq/uploads/pdf/Law/%D9%82%D8%B1%D8%A7%D8%B1%2036%20%D9%84%D8%B3%D9%86%D8%A9%201997.pdf | 2026-11-01 |

Not yet confirmed: Current status of the 20% telecom tax: press reports say it was cancelled in 2022, revived in 2025 or 2026, and a Communications fee was annulled in 2026; no official text opened. Telecom services 5% in the old skill: no official source. Cabinet Decision 957 customs changes: no official text. Whether the 2015 rates still stand in 2026: no later instrument found, none ruled out.

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
