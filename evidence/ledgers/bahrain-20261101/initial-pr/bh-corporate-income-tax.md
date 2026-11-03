---
name: bh-corporate-income-tax
description: "Company taxation in Bahrain, tax year 2026: no general corporate income tax, the 46% tax on hydrocarbon companies under Legislative Decree No. 22 of 1979, and the 15% Domestic Minimum Top-up Tax for multinational groups with revenue of EUR 750 million or more. Use for questions like does a company pay tax in Bahrain, Bahrain corporate tax rate, does DMTT apply to us, or Bahrain oil company tax."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies in Bahrain. Only two regimes tax business profits: the hydrocarbon income tax and the DMTT. Purely domestic businesses with no operations outside Bahrain are outside the DMTT. A draft corporate income tax law went to the legislature on 29 December 2025 (see bh-cross-border-tax); this skill states the law in force for 2026.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General corporate income tax | None | 2026 | https://www.lloc.gov.bh/Legislation/id/L2279 |
| Hydrocarbon income tax | 46% of net profits from extraction or refinement of hydrocarbons | 2026 | same |
| DMTT Minimum Rate | 15% effective rate on adjusted (GloBE) income, Fiscal Years starting on or after 1 January 2025 | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |
| DMTT Revenue Test | EUR 750 million or more in 2 of the 4 preceding Fiscal Years | 2026 | same |
| Transitional CbCR safe harbour, de minimis | Bahrain revenue under EUR 10 million and profit before tax under EUR 1 million; periods in bh-transfer-pricing | 2026 | same |
| Withholding on dividends, interest, royalties | None: neither income tax law has a withholding provision | 2026 | same |
| DMTT Tax Return | 15 months after the last day of the Reporting Fiscal Year (ER art. 66(A)) | 2026 | same |

## The base

Hydrocarbon tax: net profits from the sale of crude oil, refined products and natural gas attributable to operations in Bahrain. DMTT: adjusted financial (GloBE) income of in-scope constituent entities. bh-transfer-pricing holds the safe harbour tests.

## Deadlines and filing

In-scope constituent entities register with the NBR. The DMTT return date is in the table.

## Penalties and interest

See bh-transfer-pricing for DMTT penalties.

## Cross-border points

See bh-cross-border-tax.

## Two worked examples that recompute

Hydrocarbon company with net profits of BHD 1,000,000.

```oa-check
name: Hydrocarbon tax
inputs:
  profit: 1000000
steps:
  - tax: profit * 0.46
expected:
  tax: 460000.00
```

Decision: does the DMTT bite? Group revenue of EUR 800 million in two of the last four years passes the test. A Bahrain entity at a 10% effective rate on BHD 1,000,000 has a 5 point gap; any substance carve-out is taken as nil here.

```oa-check
name: DMTT top-up, no carve-out
inputs:
  income: 1000000
  etr: 0.10
steps:
  - gap: 0.15 - etr
  - topup: income * gap
expected:
  topup: 50000.00
```

## Ask the client first

- Any exploration, production or refining of hydrocarbons in Bahrain?
- Member of a multinational group? Consolidated revenue for each of the last four Fiscal Years?
- Bahrain revenue and profit before tax on the CbC report?
- Fiscal Year start date?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law, Legislative Decree No. 22 of 1979, read for bh-cross-border-tax, not reopened (page body did not load by script on 2026-11-01) | https://www.lloc.gov.bh/Legislation/id/L2279 | 2026-10-29 |
| DMTT Law and Regulations, read for bh-transfer-pricing and bh-cross-border-tax, not reopened (NBR returned 403 by script and browser on 2026-11-01) | https://www.nbr.gov.bh/laws_regulations/dmtt | 2026-10-29 |

Not yet confirmed: DMTT instalments and advance payments during 2025 (prior version, dates never confirmed); the permanent safe harbours and five-year exclusion for newly internationalised groups (prior version); whether the draft corporate income tax law has been enacted.

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
