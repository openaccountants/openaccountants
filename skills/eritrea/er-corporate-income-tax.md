---
name: er-corporate-income-tax
description: "Corporate income tax for bodies under Income Tax Proclamation 62/1994 as amended: the 30% rate, deductions, losses, withholding on payments abroad, mining and petroleum rates, filing and penalties. Covers tax year 2026 in Eritrea from the gazette text. Use for questions such as: what is the company tax rate in Eritrea, Eritrea withholding on royalties, Eritrea loss carry forward, mining tax in Eritrea."
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

# Eritrea Corporate Income Tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The newest income tax text we could open is Legal Notice 119/2012 and the newest sales tax text is Proclamation 117/2001. The Ministry of Justice list dated 2023 shows no later amendment to either. Nothing dated 2023 to 2026 could be opened, so check with the Inland Revenue Department that no later change exists.

## Who this applies to

Any incorporated body with income originating in Eritrea (Proc 62/1994 arts 2(2), 2(8), 20). Every body is category A (Legal Notice 119/2012). Mining and petroleum sit under their own proclamations.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Company rate | 30% | Any incorporated body, from 1 January 2002; replaced the 25% to 35% scale; the 20% reinvested profit rate was deleted | Proc 116/2001 art 4, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Royalty | 10% of gross | Paid by the recipient within one month | Proc 62/1994 art 22(4), https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf |
| Services from abroad | 10% of gross | Payer withholds | same |
| Dividends received from Eritrean bodies | Exempt | Art 31(5) | same |
| Bank interest received by persons | Exempt | Art 31(4) | same |
| Loss carry-forward | 5 years | Lost if ownership changes by over 25% | Proc 116/2001 art 5, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf |
| Mining | 38% | Mining licence holder; plus 5% of gross deductible if reinvested | Proc 69/1995 tax article, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-69-1995/eritrean-proc-69-1995.pdf |
| Petroleum | 35% | Petroleum operations; 15% on interest | Proc 109/2000, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-109-2000/eritrean-proc-109-2000.pdf |
| Depreciation, building | 5% | Of original cost | Legal Notice 20/1995, https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf |
| Depreciation, machinery | 16% then 12% | First year, then seven subsequent years | same |
| Depreciation, furniture | 10% | Of original cost | same |
| Depreciation, vehicles | 20% | Of original cost | same |

## The base

Taxable income is gross income less expenses wholly, necessarily and exclusively for the business (art 24). Interest is deductible only on loans from approved credit institutions (art 25). Gains are not given a separate rate in the proclamation; the income definition covers every sort of revenue (art 2(8)).

## Deadlines and filing

Declare and pay within 4 months of the end of the accounting period, with balance sheet and profit and loss (art 26(1)(a)). Payments abroad: withhold, declare and pay within one month of paying the fee (art 26(2)(b)). The year follows the Eritrean fiscal year unless the Department allows another. Steps: prepare accounts, fill the declaration, deliver with payment to the Inland Revenue Department, keep the receipt. Appeal within 30 days with a deposit (art 55). Mining tax is due within 90 days after year end (Proc 69/1995).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Not declaring on time | 20% of tax finally assessed | Proc 62/1994 art 63 |
| Late payment | 5% a month, up to 50% | art 64 |
| No acceptable books | 20% of tax finally assessed | art 65 |
| No receipt | 125% of the amount, at least 500 Nakfa | Proc 138/2003 art 2 |

## Cross-border points

Dividends and interest paid abroad have no 5% or 10% withholding rate in the texts read. The law taxes income of Eritrean origin. We found no transfer pricing rule in the texts read.

## Two worked examples that recompute

**Case 1: profit of 100,000 Nakfa.** 30% is 30,000.

```oa-check
name: Company profit 100000
inputs:
  profit: 100000
steps:
  - tax: profit * 0.30
expected:
  tax: 30000.00
```

**Case 2, a decision: use a loss after a share sale?** Profit 200,000 and prior loss 80,000. With ownership unchanged tax is 36,000. After a 30% ownership change the loss is lost and tax is 60,000.

```oa-check
name: Loss kept or lost
inputs:
  profit: 200000
  loss: 80000
steps:
  - kept: (profit - loss) * 0.30
  - lost: profit * 0.30
  - cost: lost - kept
expected:
  kept: 36000.00
  lost: 60000.00
  cost: 24000.00
```

## Ask the client first

- Incorporated body or sole trader?
- Sector: mining, petroleum, other?
- Accounting year?
- Losses, and any ownership change over 25%?
- Payments abroad and their type?
- Loans from which lender?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Proclamation 62/1994, read in full (scan, OCR) | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-62-1994/eritrean-proc-62-1994.pdf | 2026-11-01 |
| Proclamation 116/2001, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-116-2001/eritrean-proc-116-2001.pdf | 2026-11-01 |
| Proclamation 138/2003, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-138-2003/eritrean-proc-138-2003.pdf | 2026-11-01 |
| Income Tax Regulations, Legal Notice 20/1995, arts 7 to 20 and penalties read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-20-1995/eritrean-notice-20-1995.pdf | 2026-11-01 |
| Legal Notice 119/2012, read in full | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-notice-119-2012/eritrean-notice-119-2012.pdf | 2026-11-01 |
| Mining income tax Proclamation 69/1995, tax articles read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-69-1995/eritrean-proc-69-1995.pdf | 2026-11-01 |
| Petroleum income tax Proclamation 109/2000, rate and interest articles read | https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-109-2000/eritrean-proc-109-2000.pdf | 2026-11-01 |
| Ministry of Justice, thematic list of domestic legislations, section 16 read | https://mojeritrea.net/wp-content/uploads/2023/05/Thematic-Categorization-of-Domestic-Legislations-of-the-State-of-Eritrea.pdf | 2026-11-01 |

Scans were read by OCR and the key rate pages checked by eye. The Library of Congress item pages show a security check, which we did not pass; the PDFs came straight from its public file host. Scanned gazettes use "Birr" in 1994 and "Nakfa" in later amendments.

Not yet confirmed: Old guide items dropped as unsupported: 33% rate, 5% dividend and 10% interest withholding to non-residents, and "Proclamation 24/2011". Later change to mining tax under the Mining Law amendment listed by the Ministry of Justice was not read. Whether the 2% rehabilitation tax on companies in Proc 17/1991 survives Proc 66/1994 was not read. No published 2026 amendment, circular or form could be opened; the Ministry of Finance site did not connect. No official portal or online filing page could be opened either.

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
