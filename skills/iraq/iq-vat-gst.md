---
name: iq-vat-gst
version: 0.3
description: "Federal Iraq consumption-tax source extracts for hotels, listed imports and tickets, with explicit holds on current law and unsupported VAT-absence conclusions. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq VAT and Sales Tax 0.3

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Historical selective-sales-tax extracts only. Decision 36/1997 and the bundled Instructions 7/1997 as amended by Instructions 4/2005 concern excellent and first-class hotels/restaurants. Instructions 5/2015 concern listed imports, local production, mobile/internet services and national-carrier tickets. Their existence does not establish whether a different VAT, registration, reverse-charge or input-credit obligation exists in 2026.

## Rates, bands and thresholds

**IQ-CURRENT and IQ-SALES-CURRENT apply to every row. These are source-version amounts, not a 2026 rate list.**

| Historical instrument and condition | Amount | Official URL |
|---|---|---|
| Decision 36/1997 first clause and Instructions 7/1997 art. 1, excellent/first-class hotels and restaurants, value of all services | 10% | https://tax.mof.gov.iq/uploads/pdf/Law/%D9%82%D8%B1%D8%A7%D8%B1%2036%20%D9%84%D8%B3%D9%86%D8%A9%201997.pdf |
| Instructions 5/2015 art. 4(3), imported cigarettes/tobacco and alcohol, customs-declaration goods value; local producer collection separately addressed in art. 4(3)(b) | 300% | https://tax.mof.gov.iq/uploads/Najwan/law/%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D9%81%D8%B1%D8%B6%20%D9%88%20%D8%AC%D8%A8%D8%A7%D9%8A%D8%A9%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA%20-%20Copy%202.pdf |
| Same instrument art. 4(1), imported cars, customs-declaration goods value | 15% | same |
| Same instrument arts. 1(6),(9), 4(2), tickets for Iraqi Airways / other national carriers, domestic or international journeys | 15% | same |
| unverified: mobile/internet present rate and later cancellation/reintroduction chain | Held | unverified |

## The base

Historical hotel instructions art. 3 require an invoice showing service amounts and sales tax, with amounts recorded for GCT. Article 4, as replaced in 2005, converts foreign-currency service charges at the Central Bank's announced market exchange rate. The 2015 instrument uses customs-declaration value for the specified imports. “Final revenue” wording does not prove the absence of an input-credit right in every law. Current customs valuation and duties are held separately.

## Deadlines and filing

Historical hotel instructions art. 3 remits in the first ten days of the following month and art. 7 requires records subject to GCT control. Instructions 5/2015 art. 4 collects the specified imports at border tax units; its national-carrier/travel-office and local-producer clauses require a quarterly report certified by the competent accountant, on the GCT form, signed by the taxpayer or legal representative, in the first half of the following month. These source extracts do not establish present forms, registration, submission channel, receipt or payment reference. Do not file from this incomplete workflow.

## Penalties and interest

Historical hotel instructions art. 6 makes management responsible for the commercial banks' overdraft-rate interest on collected tax not remitted within art. 3's period, and for tax plus that interest if tax was not collected. The present interest rate, calculation convention, relief and other penalties remain held; no numerical interest calculation is supplied.

## Cross-border points

The 2015 text art. 2 treats the specified mobile/internet service as provided in Iraq even if the necessary installations are abroad. This is a historical scope clause, not confirmation of the present telecom levy. Foreign-currency hotel conversion is above. Customs changes, digital supplies and Kurdistan Region treatment require separate source checks.

## Two worked examples that recompute

Historical arithmetic only, after independently establishing the instrument and classification. These examples do not determine 2026 liability or customs duty.

First-class hotel service amount IQD 1m under the historical decision gives IQD 100,000 sales tax.

```oa-check
name: Historical hotel example
inputs:
  services: 1000000
steps:
  - tax: services * 0.10
expected:
  tax: 100000
```

Classification decision: at the same IQD 10m customs-declaration value, the historical tobacco and car percentages differ by IQD 28.5m. Do not select a product classification by description alone; match the import documents.

```oa-check
name: Historical import classification sensitivity
inputs:
  value: 10000000
steps:
  - tobacco: value * 3
  - car: value * 0.15
  - difference: tobacco - car
expected:
  tobacco: 30000000
  car: 1500000
  difference: 28500000
```

## Ask the client first

- Federal Iraq or Kurdistan Region, and transaction date?
- Exact goods/service, hotel grade or carrier licence?
- Importer, producer, airline, travel office or service provider?
- Invoice, customs declaration, currency and value?
- Current authority notice, registration and prior filings?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Instructions 5/2015: all three PDF pages visually read, arts. 1–5 and gazette publication date | https://tax.mof.gov.iq/uploads/Najwan/law/%D8%AA%D8%B9%D9%84%D9%8A%D9%85%D8%A7%D8%AA%20%D9%81%D8%B1%D8%B6%20%D9%88%20%D8%AC%D8%A8%D8%A7%D9%8A%D8%A9%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D9%85%D8%A8%D9%8A%D8%B9%D8%A7%D8%AA%20-%20Copy%202.pdf | 2026-11-01 |
| Decision 36/1997 and Instructions 7/1997 plus amendment 4/2005: all three PDF pages visually read; defective text layer was not used as quotation authority | https://tax.mof.gov.iq/uploads/pdf/Law/%D9%82%D8%B1%D8%A7%D8%B1%2036%20%D9%84%D8%B3%D9%86%D8%A9%201997.pdf | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT / IQ-SALES-CURRENT** full later-amendment chain and continued 2026 force of the hotel, tobacco/alcohol, car and ticket instruments; **IQ-SALES-TELECOM** later mobile/internet cancellation/reintroduction and current charge, including the unsupported legacy percentage; **IQ-VAT-ABSENCE** no evidence sufficient to assert a general absence of VAT/GST, registration, reverse charge, invoicing, staged collection or input credits in 2026; **IQ-SALES-WORKFLOW** current registrations, forms, channels, confirmations, payment references, penalties and interest; **IQ-CUSTOMS** current duties, valuation and Cabinet Decision 957. Old “no VAT / no credit / no registration” answers are superseded research holds, never operative instructions.

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
