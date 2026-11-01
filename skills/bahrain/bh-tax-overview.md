---
name: bh-tax-overview
description: "Tax overview for Bahrain, tax year 2026: which taxes exist, who runs them, and which skill in this pack holds each figure. Covers the absence of personal and general corporate income tax, the 46% hydrocarbon tax, the 15% DMTT for large multinational groups, VAT and social insurance. Use for questions like does Bahrain have income tax, what taxes apply in Bahrain, or who is the tax authority in Bahrain."
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

# Bahrain Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking which taxes apply in Bahrain in 2026, business or individual. Each figure lives in the skill named below.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Personal income tax | None: the Income Tax Law taxes only bodies corporate, establishments and companies (art. 1(a)). See bh-income-tax | 2026 | https://www.lloc.gov.bh/Legislation/id/L2279 |
| Hydrocarbon income tax | 46%. See bh-corporate-income-tax | 2026 | same |
| DMTT Minimum Rate, in-scope groups only | 15%. See bh-corporate-income-tax | 2026 | https://www.nbr.gov.bh/laws_regulations/dmtt |
| VAT mandatory registration | BHD 37,500 annual taxable supplies | 2026 | https://web.archive.org/web/20250422040914/https://www.nbr.gov.bh/vat_registration |
| VAT standard rate | unverified: 10% per bahrain-vat, no NBR page opened | 2026 | unverified |
| Social insurance | unverified: see bh-payroll-social | 2026 | unverified |

## The base

- Income tax reaches hydrocarbon companies only. The DMTT reaches in-scope multinational group members. Others pay no tax on profits in 2026.
- A draft corporate income tax law went to the legislature on 29 December 2025 (see bh-cross-border-tax). It is not treated as law here.
- Currency: Bahraini dinar (BHD). The NBR administers VAT, excise and the DMTT. The Social Insurance Organization (SIO) runs social insurance.
- Standard fiscal year: calendar year unless an entity adopts a different one.
- No general residence-based income tax; the DMTT applies by reference to constituent entities located in Bahrain.

## Deadlines and filing

VAT: the NBR's example has a quarter ending 31 March due on 30 April, so the return is due by the end of the following month. Monthly returns need an application and NBR approval. Social insurance: within the first 15 days of the following month (bh-payroll-social). DMTT: see bh-transfer-pricing.

## Penalties and interest

Held in bh-payroll-social and bahrain-vat.

## Cross-border points

See bh-cross-border-tax.

## Two worked examples that recompute

Local trading company with BHD 100,000 profit, no hydrocarbon activity, not in a multinational group: income tax is nil.

```oa-check
name: Local company, no profits tax
inputs:
  profit: 100000
steps:
  - tax: profit * 0
expected:
  tax: 0.00
```

Decision: register for VAT? Turnover of BHD 40,000 is above BHD 37,500, so registration is mandatory.

```oa-check
name: VAT threshold test
inputs:
  turnover: 40000
  threshold: 37500
steps:
  - excess: max(turnover - threshold, 0)
expected:
  excess: 2500.00
```

## Ask the client first

- Individual or company?
- Any hydrocarbon activity?
- Part of a multinational group with revenue of EUR 750 million or more?
- Annual taxable supplies?
- Any employees, and their nationality?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law, Legislative Decree No. 22 of 1979, read for bh-cross-border-tax, not reopened (page body did not load by script on 2026-11-01) | https://www.lloc.gov.bh/Legislation/id/L2279 | 2026-10-29 |
| DMTT Law and Regulations, read for bh-transfer-pricing and bh-cross-border-tax, not reopened (NBR returned 403 by script and browser on 2026-11-01) | https://www.nbr.gov.bh/laws_regulations/dmtt | 2026-10-29 |
| NBR, VAT registration page, threshold paragraph (archive copy of 22 Apr 2025) | https://web.archive.org/web/20250422040914/https://www.nbr.gov.bh/vat_registration | 2026-11-01 |
| NBR, when to file VAT, examples paragraph (archive copy of 25 Aug 2026) | https://web.archive.org/web/20260825060528/https://www.nbr.gov.bh/VAT/vat_return_filing/when_to_file | 2026-11-01 |

Not yet confirmed: the VAT standard rate from an NBR page; the fiscal year rule; excise rates; whether the draft corporate income tax law has been enacted.

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
