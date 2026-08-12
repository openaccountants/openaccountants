---
name: ca-nonresident-cgt
description: "Canada non-resident capital gains: Section 116 clearance certificate, Part XIII withholding, taxable Canadian property (TCP), notional assessment. Trigger on: \"non-resident selling Canadian property\", \"Section 116 Canada\", \"clearance certificate CRA\", \"TCP taxable Canadian property\", \"withholding on sale Canada\", \"non-resident selling Canadian shares\", \"Part XIII withholding Canada\", \"NR4 Canada\"."
version: 1.0
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CA Nonresident Cgt

## Core rule

- **Taxation of non-residents on TCP** — Non-residents of Canada are taxed on capital gains from Taxable Canadian Property (TCP). Gains from non-TCP assets: no Canadian tax.

## Taxable Canadian Property (TCP)

**Taxable Canadian Property (TCP)**

| Asset | TCP? |
| --- | --- |
| Canadian real property | **Always TCP** |
| Property used in a Canadian business (inventory, equipment) | TCP |
| Shares in a **private corporation** where > 50% of FMV derives from Canadian real property in any of the preceding 60 months | TCP |
| Shares in a **public corporation** listed on a designated exchange | **Not TCP** (general rule) |
| Shares in a Canadian-controlled private corporation (CCPC) — operating business | TCP if the 50% real property test is met; otherwise not TCP |
| Options to acquire TCP | TCP |
| Partnership interests where > 50% of FMV is Canadian real property | TCP |

## Section 116 — Clearance Certificate

When a non-resident disposes of TCP, they must notify the CRA and obtain a **clearance certificate** under ITA §116:

1. **Notify CRA**: within 10 days of the sale (or before the sale if withholding obligation applies)
2. **CRA issues a certificate**: confirming the amount of tax payable on the gain
3. **Buyer's withholding obligation**: If the seller does NOT produce a clearance certificate, the **buyer** must withhold and remit **25%** (or 50% for certain property) of the **gross proceeds** to the CRA

The withholding is on gross proceeds — not the gain. This can be extremely punishing on low-gain transactions.

- **Notify CRA deadline** — Within 10 days of the sale (or before the sale if withholding obligation applies)  _(ITA §116)_
- **Buyer withholding rate on gross proceeds if no clearance certificate** — 25% percent (or 50% for certain property, applied to gross proceeds)  _(ITA §116)_

## Tax rate for non-residents on TCP gains

Non-residents pay Canadian income tax on TCP gains at the same rates as residents, applied to the included portion of the gain (50% inclusion rate — see `ca-capital-gains`).

Combined federal + provincial top rates on the included portion: approximately 26%–27% (federal) + varying provincial rates.

## Filing requirement

- **Filing requirement for non-residents disposing of TCP** — Non-residents who dispose of TCP must file a Canadian non-resident tax return (T1 or T2 as applicable) for the year of disposition. A non-resident individual files Form T1 — Income Tax and Benefit Return noting non-resident status.

## Part XIII withholding on dividends

- **Part XIII withholding on dividends to non-residents** — 25% percent (reduced by treaty — typically 15% for portfolio, 5% for 10%+ corporate shareholders under most DTAs; separate from capital gains rules above)  _(ITA §212–218 (Part XIII))_

## Sources

- Income Tax Act (Canada), §2(3) (non-resident taxable in Canada), §115 (non-resident income from Canadian sources), §116 (clearance certificates), §212–218 (Part XIII)
- CRA: canada.ca/en/revenue-agency/services/tax/international-non-residents/information-been-moved/disposing-of-certain-canadian-property.html

> Working paper only. The TCP classification for shares requires analysis of the corporation's assets. A §116 clearance certificate must be obtained BEFORE settlement or the buyer faces withholding liability. Engage a qualified Canadian tax adviser.

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
