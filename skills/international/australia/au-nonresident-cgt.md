---
name: au-nonresident-cgt
description: "Use this skill for any non-resident selling Australian assets. Trigger on: \"non-resident CGT Australia\", \"TAP test Australia\", \"taxable Australian property\", \"FRCGW\", \"foreign resident capital gains withholding\", \"15% withholding Australia\", \"12.5% withholding Australia\", \"clearance certificate ATO\", \"sell Australian shares non-resident\", \"sell Australian property non-resident\", \"Australian CGT non-resident seller\", \"no CGT discount non-resident Australia\". Covers the TAP test, 30% flat rate, FRCGW withholding (15%, no threshold, from 1 January 2025), clearance certificates. For Australian residents see au-capital-gains."
version: 1.1
jurisdiction: AU
tax_year: 2025
tax_year_notes: "2025-26; FRCGW figures apply to contracts signed from 1 January 2025"
last_updated: 2026-08-20
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Nonresident Cgt

## Section 1 — Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Australia |
| Applies to | Non-residents of Australia disposing of Australian assets |
| CGT rate (non-resident) | **30% flat rate** on net gain (no 50% discount available) |
| Key test | Taxable Australian Property (TAP) test |
| Withholding | 15% of the market value (usually sale price) on ALL Australian real property sales from 1 Jan 2025 — no minimum threshold |
| Primary legislation | ITAA 1997 Div 855; TAA 1953 Sch 1 Subdiv 14-D |
| Tax authority | ATO (ato.gov.au) |
| Verified by | Pending — Australian CPA/CA sign-off required |

## Section 2 — The Core Rule

Non-residents are only subject to Australian CGT on **Taxable Australian Property (TAP)**. Non-TAP assets sold by non-residents: **no Australian CGT**.

## Section 3 — The TAP Test: What Qualifies as TAP

**TAP test asset types table**

| Asset type | TAP? |
| --- | --- |
| Australian real property (land, buildings) | **Always TAP** |
| Mining, quarrying, prospecting rights in Australia | **Always TAP** |
| Shares in a company where >50% of market value derives from Australian real property interests | **TAP (indirect interest)** |
| Units in a trust where >50% of MV derives from Australian real property interests | **TAP (indirect interest)** |
| Options/rights to acquire any of the above | TAP |
| Assets used in Australian permanent establishment of a non-resident | TAP |
| Shares in an Australian company where assets are predominantly operating business, IP, goodwill, cash | **NOT TAP** |
| Portfolio shares (<10% interest in a listed company) | Generally NOT TAP regardless of asset composition |

- **Critical question for company shares** — Look through to the company's balance sheet. If >50% of the market value of the company's assets consists of Australian real property interests → TAP. If the company is an operating business with IP, goodwill, equipment, receivables → likely NOT TAP.

## Section 4 — CGT Rate for Non-Residents

**CGT rate for non-residents table**

| Item | Non-resident treatment |
| --- | --- |
| CGT rate | 30% (top individual rate, not graduated) |
| 50% general discount | **NOT available** to non-residents (removed 8 May 2012) |
| SBCGT concessions | Available if all basic conditions met (including active asset test) |
| Main residence exemption | Generally not available to non-residents (unless Australian citizen/PR in specific circumstances) |
| Cost base calculation | Same as residents |

## Section 5 — Foreign Resident Capital Gains Withholding (FRCGW)

- **FRCGW obligation** — For contracts signed on or after 1 January 2025, the purchaser must withhold **15% of the market value (usually the sale price)** on **every** Australian real property sale — the previous AUD $750,000 de-minimis threshold was removed — unless the vendor produces an ATO clearance certificate (residents) or a variation notice (non-residents). _(TAA 1953 Sch 1 Subdiv 14-D, as amended by Treasury Laws Amendment (2024 Tax and Other Measures No. 1) Act 2024 (No. 135, 2024) Sch 1)_
- **Prior regimes (for older contracts)** — Contracts signed 1 July 2017 – 31 December 2024: 12.5% where the property was valued at AUD $750,000 or more. Contracts signed 1 July 2016 – 30 June 2017: 10% at AUD $2,000,000 and above. The **contract date**, not settlement date, picks the regime.
- **FRCGW nature** — This is a payment on account (not a final tax). Actual tax liability is computed in the non-resident's Australian tax return.
- **Scope note** — FRCGW attaches to taxable Australian real property and indirect Australian real property (IARP) interests (and options/leases over them). Transactions on an approved stock exchange are excluded. Vendor declarations can apply for non-listed share/unit transactions.

**FRCGW rate table (contracts signed from 1 January 2025)**

| Item | Value |
| --- | --- |
| Threshold | **None** — applies to all in-scope property regardless of value |
| Withholding rate | **15%** of market value (usually the sale price) |
| Who withholds | The buyer (purchaser) |
| Remittance deadline | At or before settlement |

**Example**: Non-resident signs a contract in March 2026 to sell shares that are an indirect Australian real property interest (TAP) for AUD $10M. Buyer withholds AUD $1.5M (15%). Net gain is, say, AUD $8M. Australian tax at 30% = AUD $2.4M. The $1.5M already withheld is applied — balance payable AUD $0.9M via Australian tax return.

## Section 6 — Clearance Certificate

- **Clearance certificate for resident sellers** — If the seller is an Australian resident (not a foreign resident), the seller must apply for a clearance certificate from the ATO to confirm residency, relieving the buyer of the withholding obligation. Because the $750,000 threshold was removed for contracts from 1 January 2025, **every Australian resident selling real property needs a clearance certificate** — including on the sale of a family home — or the buyer must withhold 15% at settlement and the seller waits for the next tax return to recover it.
- **Timing** — Certificates are valid for 12 months, so vendors should apply early (before listing). Most issue quickly, but the ATO advises some can take up to 28 days.
- **Variation for non-resident sellers** — If the seller IS a non-resident but believes 15% over-collects (e.g. the gain is small or nil, losses apply, or the asset is not TAP), the seller can apply for a variation notice specifying a reduced rate. The variation must be given to the purchaser before settlement.

Applications: via ATO online services (individuals) or the Tax/BAS Agent portal.

## Section 7 — Filing Obligations for Non-Residents

- **Filing requirement** — A non-resident who sells TAP must lodge an Australian non-resident individual tax return for the year of disposal (even if no tax is payable after losses/concessions). Due date: 31 October following the end of the financial year (or later with a tax agent).
- **TFN requirement** — Australian Tax File Number (TFN) is required. Non-residents can apply via ATO.

## Section 8 — Interaction with Tax Treaties

- **DTA coverage and Article 13** — Australia has double tax agreements (DTAs) with 45+ countries. Article 13 of most DTAs follows the OECD Model — gains on shares may be taxed by the country of residence of the seller UNLESS the shares derive principally from Australian real property (aligns with the TAP domestic test).
- **Treaty outcome mirrors domestic TAP rules** — Under most treaties, the outcome mirrors the domestic TAP rules: if TAP → Australia taxes; if not TAP → Australia does not tax (residence country taxes).

Always check the saving clause and specific treaty wording.

## Section 9 — Sources

- ITAA 1997 Division 855 (non-resident CGT)
- Tax Administration Act 1953, Schedule 1, Subdivision 14-D (FRCGW)
- Treasury Laws Amendment (2024 Tax and Other Measures No. 1) Act 2024 (No. 135, 2024), Schedule 1 — FRCGW rate to 15% and threshold removed for acquisitions from 1 January 2025
- ATO: ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview (QC 48972, updated 22 June 2026)
- ATO: Australian residents and clearance certificates (same section)

> **Working paper only.** The TAP classification requires analysis of the company's asset composition by market value — not book value. Engage a qualified Australian tax adviser for transaction-specific advice.

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
