---
name: er-tax-overview
description: "A map of Eritrean taxes: income tax, sales and excise tax, stamp duty, farm tax, the diaspora tax and customs, the authority, currency and where each rule lives in the pack. Covers tax year 2026 in Eritrea from the gazette text. Use for questions such as: what taxes are there in Eritrea, who collects tax in Eritrea, Eritrea top tax rate, stamp duty in Eritrea."
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

# Eritrea Tax Overview

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The newest income tax text we could open is Legal Notice 119/2012 and the newest sales tax text is Proclamation 117/2001. The Ministry of Justice list dated 2023 shows no later amendment to either. Nothing dated 2023 to 2026 could be opened, so check with the Inland Revenue Department that no later change exists.

## Who this applies to

Anyone needing the map first. Detail lives in the linked skills. Currency is the Nakfa (ERN). The Inland Revenue Department under the Minister of Finance administers tax (Proc 62/1994 art 2).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Top personal rate | 30% | Over 3,500 a month; see [Income tax](er-income-tax.md) | Proc 116/2001 art 2, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Company rate | 30% | See [Corporate income tax](er-corporate-income-tax.md) | Proc 116/2001 art 4, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| VAT or GST | None | Sales tax at 5%, 10%, 12%; see [VAT or GST](er-vat-gst.md) | Proc 117/2001, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf |
| Diaspora tax | 2% of net income | Citizens abroad | Proc 67/1995, UK translation, https://assets.publishing.service.gov.uk/media/5a7f32ff40f0b6230268e0c6/Eritrea-Appendix-I-II-III-V-Dec-2015.pdf |
| Stamp duty late penalty | 10% of duty | Stamps affixed under 50 Nakfa; paid against receipt at 50 or more where regulations say | Proc 180/2017, https://shabait.com/2017/03/15/proclamation-no-180-2017/ |
| Rural farm and livestock tax | Set by Legal Notice | Effective 1 December 2016; replaced earlier rules | Ministry of Information notice, https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ |

## The base

Income is taxed by origin in Eritrea (Proc 62/1994 art 2(8)), by separate schedule: employment, rent, business, commercial farming (art 6).

## Deadlines and filing

Employment monthly; business 1, 2 or 4 months after year end; sales tax monthly. See each skill.

## Penalties and interest

Generally 20% for not declaring, 5% a month up to 50% for late payment, 20% for no books (Proc 62/1994 arts 63 to 65).

## Cross-border points

Eritrean-origin income is taxed; citizens abroad pay the 2% tax. Customs is under Proc 112/2000 (Ministry of Justice list), not covered here.

## Two worked examples that recompute

**Case 1: top rate check.** A 100,000 profit company pays 30,000.

```oa-check
name: Company
inputs:
  profit: 100000
steps:
  - tax: profit * 0.30
expected:
  tax: 30000.00
```

**Case 2, a decision: sole trader or company at 100,000 profit?** Bands against the flat rate.

```oa-check
name: Sole trader against company
inputs:
  income: 100000
steps:
  - band_1: min(income, 2400) * 0.02
  - band_2: (min(income, 14400) - min(income, 2400)) * 0.10
  - band_3: (min(income, 30000) - min(income, 14400)) * 0.20
  - band_4: (min(income, 42000) - min(income, 30000)) * 0.25
  - band_5: (income - min(income, 42000)) * 0.30
  - tax: band_1 + band_2 + band_3 + band_4 + band_5
  - company: income * 0.30
  - saving: company - tax
expected:
  tax: 24768.00
  saving: 5232.00
```

The person pays 24,768 and a company 30,000, before any dividend, which is exempt (art 31(5)).

## Ask the client first

- Which tax?
- Person or company?
- Resident in Eritrea or a citizen abroad?
- Sector?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Proclamation 62/1994, read in full (scan, OCR) | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-01 |
| Proclamation 116/2001, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf | 2026-11-01 |
| Proclamation 117/2001, operative text and schedules read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-117-2001/eritrean-proc-117-2001.pdf | 2026-11-01 |
| UK Government translation of Proclamations 17/1991 and 67/1995, annexes 1 and 2 read | https://assets.publishing.service.gov.uk/media/5a7f32ff40f0b6230268e0c6/Eritrea-Appendix-I-II-III-V-Dec-2015.pdf | 2026-11-01 |
| Stamp Duty Proclamation 180/2017 (Ministry of Information), arts on rate and penalty read | https://shabait.com/2017/03/15/proclamation-no-180-2017/ | 2026-11-01 |
| Ministry of Information notice on farm and livestock income tax, read in full | https://shabait.com/2016/12/02/legal-notice-on-farm-and-livestock-income-tax/ | 2026-11-01 |
| Ministry of Justice, thematic list of domestic legislations, section 16 read | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-01 |

Scans were read by OCR and the key rate pages checked by eye. The Library of Congress item pages show a security check, which we did not pass; the PDFs came straight from its public file host. Scanned gazettes use "Birr" in 1994 and "Nakfa" in later amendments.

Not yet confirmed: Fiscal year dates (the old guide said calendar year; the texts read say only "Eritrean fiscal year"). Stamp duty schedule rates, farm tax rates and customs were not extracted. No published 2026 amendment, circular or form could be opened; the Ministry of Finance site did not connect. No official portal or online filing page could be opened either.

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
