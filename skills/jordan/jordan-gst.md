---
name: jordan-gst
description: "Use this skill to prepare, review or classify a Jordan General Sales Tax (GST) return for tax year 2026. Jordan charges GST at 16% under Law No. 6 of 1994, administered by the Income and Sales Tax Department (ISTD), with zero-rated and exempt schedules and reduced rate lists at 10%, 5%, 4% and 2%. Covers registration, the two-month period, payment within the following month, input tax, refunds, bank statement patterns, penalties and late charges. Special Sales Tax runs monthly and is separate. Trigger phrases: Jordan GST, Jordan VAT, ISTD return, Jordan sales tax, Jordanian indirect tax. Read this skill before any Jordan GST work; do not use it for income tax."
version: 2.1
jurisdiction: JO
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Jordan GST

## Who this applies to

A person selling taxable goods or services who reaches the registration limit, a person importing taxable goods or services for business whatever the amount, and voluntary registrants. Default for an unknown rate on a sale: 16%. Default for an unknown purchase: not deductible. Default for an unknown counterparty: domestic.

Minimum input: bank statement for the period, from Arab Bank, Housing Bank, Jordan Ahli Bank, Cairo Amman, Bank al Etihad or any other Jordanian bank. Better: sales invoices and purchase invoices.

Refuse and refer: Aqaba Special Economic Zone operations (ISTD has a separate Aqaba return), and alcohol, tobacco, fuel or other Special Sales Tax goods, where the special tax is computed first.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Standard rate | 16% | Import or supply of any good or service, art. 6(a) | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf |
| Zero rate | 0% | Schedule 2 goods, sales to free zones, exports, sales to exempt bodies, art. 7(a) | same |
| Exempt | No GST, no input | Schedule 3, art. 7(b) | https://www.istd.gov.jo/AR/List/%D8%AC%D8%AF%D8%A7%D9%88%D9%84_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D8%A9_%D8%B9%D9%84%D9%89__%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA |
| Reduced lists | 10%, 5%, 4%, 2% | Goods named on ISTD lists; look up the item, never guess | https://www.istd.gov.jo/AR/List/%D8%A7%D9%84%D9%86%D8%B3%D8%A8_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9 |
| Registration limit | unverified | Set by regulation. Reported JOD 75,000 commercial or agricultural, JOD 50,000 industrial, JOD 30,000 services; page not opened | unverified |
| Importer | No limit | Register within 30 days of first import, unless personal use | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf |
| Tourist refund | JOD 50 to JOD 500 | Non-resident's goods on departure | same |

## The base

Sale price the buyer must pay. A zero-rated or exempt item sold tied to a taxable item takes GST (art. 7(c)); a taxable good tied to an exempt financial service stays taxable on its own value (art. 7(d)).

Input tax deducted: tax on returns, bad debts, purchases and imports for business other than Schedule 4 items, and pre-registration stock. Schedule 4 lists non-deductible items (https://www.istd.gov.jo/AR/List/%D8%AC%D8%AF%D8%A7%D9%88%D9%84_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D8%A9_%D8%B9%D9%84%D9%89__%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA). Older list of blocked items, to check against Schedule 4: entertainment and hospitality, private motor vehicles, non-business items, purchases tied to exempt supplies, gifts above limits. Partial exemption by turnover with ISTD approval is not confirmed.

Imports: GST on CIF plus customs duties, collected by Jordan Customs, recoverable if for taxable supplies. Services from a non-resident: importing a service is taxable under art. 6(a); self-assess 16% and claim input if used for taxable supplies. Pay at the earliest of one month from paying the fee, customs release of the item carrying the service, or six months from receiving the service; the Director may let a registered importer defer.

Supplier patterns for bank statements:

| Pattern | Treatment | Notes |
|---|---|---|
| ARAB BANK, HOUSING BANK, ISKAN BANK, JORDAN AHLI, CAIRO AMMAN, BANK AL ETIHAD, CAPITAL BANK | EXCLUDE | Financial service |
| INTEREST, LOAN | EXCLUDE | Out of scope |
| ISTD, INCOME AND SALES TAX | EXCLUDE | Tax payment |
| CUSTOMS, JORDAN CUSTOMS | Check for import GST | Duty excluded; GST recoverable |
| SSC, SOCIAL SECURITY CORPORATION | EXCLUDE | Social contribution |
| JEPCO, EDCO, IDECO | Check bill | Electricity |
| MIYAHUNA, WAJ | Check bill | Water |
| ZAIN JORDAN, ORANGE JORDAN, UMNIAH | Check bill | Invoice rate governs; old 4% not confirmed |
| GOOGLE, MICROSOFT, ADOBE, AWS, ZOOM, SLACK, SALESFORCE | Reverse charge 16% | Non-resident service |

Return layout: output tax by rate, zero-rated sales, exempt sales; input on domestic purchases, on imports, adjustments; net is output less input plus credit brought forward. Box numbers: see the form (https://www.istd.gov.jo/Ar/List/%D8%A7%D9%84%D8%A7%D9%82%D8%B1%D8%A7%D8%B1%D8%A7%D8%AA_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9).

## Deadlines and filing

| Step | Rule | Source |
|---|---|---|
| Period | Two months; the Director sets each registrant's start and end | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf |
| Special Sales Tax | Monthly | same |
| Nil return | Required for every period | same |
| Payment | Within the month after the period; Director may add up to one month | same |
| Invoice | Tax invoice under executive instructions | same |

With calendar pairs: Jan-Feb by 31 Mar, Mar-Apr by 31 May, May-Jun by 31 Jul, Jul-Aug by 30 Sep, Sep-Oct by 30 Nov, Nov-Dec by 31 Jan.

File via ISTD e-services with the tax number, submit the General Sales Tax return, then pay. Screens are not confirmed. Monthly filing above JOD 1,000,000, from the old skill, is not in the law as read.

## Penalties and interest

Late payment: 0.4% (four per thousand) per week or part of a week; the old skill's 4% was wrong. Late return, late registration up to 60 days, and other listed breaches: JOD 100 to JOD 500. Evasion carries heavier penalties, including fines and prison.

Refunds: exports, tax collected in error, and input credits unused for over two months. The day limit did not OCR clearly.

## Cross-border points

Exports and sales to free zones are zero-rated with input kept. Goods leaving a free zone into Jordan take GST. Foreign SaaS is reverse charged as above. Credit notes reduce output tax on returned sales. Exempt financial services carry no output tax and no input.

## Two worked examples that recompute

Simple: JOD 1,000 net standard sale, and an import with CIF 10,000 and duty 1,000.

```oa-check
name: Standard sale and import
inputs:
  sale: 1000
  cif: 10000
  duty: 1000
steps:
  - output: sale * 0.16
  - importgst: (cif + duty) * 0.16
expected:
  output: 160.00
  importgst: 1760.00
```

Edge: UK consulting JOD 1,420 used for taxable sales. Output and input both JOD 227.20, net nil. JOD 1,000 paid three weeks late costs JOD 12.

```oa-check
name: Reverse charge and late charge
inputs:
  fee: 1420
  due: 1000
  weeks: 3
steps:
  - output: fee * 0.16
  - net: output - output
  - late: due * 0.004 * weeks
expected:
  output: 227.20
  net: 0.00
  late: 12.00
```

## Ask the client first

- Registered or not, and the period the Director set.
- Sales for the past 12 months by sector.
- Any imports.
- Exempt or zero-rated sales.
- Aqaba, free zone or development zone presence.
- Special Sales Tax goods.

Never allow input on exempt supplies. Never treat imports as zero-rated. Confirm the period before filing.

## Sources

| Source | URL | Read on |
|---|---|---|
| General Sales Tax Law No. 6 of 1994 as amended, ISTD scan read by OCR: rate, registration, return, deduction, refund and penalty articles read | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf | 2026-11-01 |
| ISTD, GST schedules list, file names read | https://www.istd.gov.jo/AR/List/%D8%AC%D8%AF%D8%A7%D9%88%D9%84_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%B9%D8%A7%D9%85%D8%A9_%D8%B9%D9%84%D9%89__%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA | 2026-11-01 |
| ISTD, sales tax rates search, first page read | https://www.istd.gov.jo/AR/List/%D8%A7%D9%84%D9%86%D8%B3%D8%A8_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9 | 2026-11-01 |
| ISTD, tax return forms list, first page read | https://www.istd.gov.jo/Ar/List/%D8%A7%D9%84%D8%A7%D9%82%D8%B1%D8%A7%D8%B1%D8%A7%D8%AA_%D8%A7%D9%84%D8%B6%D8%B1%D9%8A%D8%A8%D9%8A%D8%A9 | 2026-11-01 |

Not yet confirmed: registration limits; any amendment after the 2022 ISTD file; the old 8% rate and 4% telecom rate (ISTD lists 10%, 5%, 4% and 2%, no 8%; list contents read on the first page only); old examples such as bread, rice, sugar, milk, medical, education and residential rent, which need the schedules; monthly filing above JOD 1,000,000; national e-invoicing timing; the Arabic invoice rule. Article numbers come from OCR.

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
