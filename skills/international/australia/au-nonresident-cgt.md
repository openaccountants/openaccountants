---
name: au-nonresident-cgt
description: "Use this skill for any non-resident selling Australian assets. Trigger on: \"non-resident CGT Australia\", \"TAP test Australia\", \"taxable Australian property\", \"FRCGW\", \"foreign resident capital gains withholding\", \"15% withholding Australia\", \"12.5% withholding Australia\", \"clearance certificate ATO\", \"sell Australian shares non-resident\", \"sell Australian property non-resident\", \"Australian CGT non-resident seller\", \"no CGT discount non-resident Australia\". Covers the TAP test, the foreign resident rate scale, FRCGW withholding (15%, no threshold, from 1 January 2025), clearance certificates. For Australian residents see au-capital-gains."
version: 1.2
jurisdiction: AU
tax_year: 2025
last_updated: 2026-09-16
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
| CGT rate (non-resident individual) | The foreign resident rate scale applies to the net gain: 30c to $135,000, then 37c to $190,000, then 45c. No 50% discount, and no Medicare levy. Confirm the scale for the income year at [ATO, Tax rates: foreign resident](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-foreign-residents) |
| Key test | Taxable Australian Property (TAP) test |
| Withholding | 15% of the sale price for contracts signed from 1 January 2025, with no value threshold. 12.5% and a $750,000 threshold applied to contracts from 1 July 2017 to 31 December 2024 |
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

- **FRCGW obligation** — For contracts signed from 1 January 2025, the purchaser must withhold 15% of the sale price on Australian real property, with no value threshold. Contracts from 1 July 2017 to 31 December 2024 attracted 12.5% where the value was $750,000 or more. [ATO, Foreign residents capital gains withholding variations](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-residents-and-variations).
- **FRCGW nature** — This is a payment on account (not a final tax). Actual tax liability is computed in the non-resident's Australian tax return.

**FRCGW threshold table**

| FRCGW threshold | None, for contracts signed from 1 January 2025 |
| --- | --- |
| Withholding rate | 15% of the sale price |
| Who withholds | The buyer (purchaser) |
| Remittance deadline | Day of settlement |

**Example** (synthetic): a foreign resident individual sells taxable Australian property for AUD $10M under a contract signed after 1 January 2025. The purchaser withholds 15%, being AUD $1.5M, unless a clearance certificate or variation applies. Suppose the net gain is AUD $8M. Australian tax on the foreign resident scale is $60,850 plus 45c for each dollar above $190,000, giving $60,850 + 0.45 x $7,810,000 = AUD $3,575,350. Crediting the $1.5M withheld leaves AUD $2,075,350 payable through the Australian tax return. Do not apply a flat 30% to a gain of this size.

## Section 6 — Clearance Certificate

- **Clearance certificate for resident sellers** — If the seller is an Australian resident (not a foreign resident), the seller can apply for a clearance certificate from the ATO to confirm residency, relieving the buyer of the withholding obligation.
- **Variation for non-resident sellers** — If the seller IS a non-resident but believes no tax is payable (e.g. asset is not TAP, or gain is nil due to losses), the seller can apply for a variation to reduce the withholding amount.

Applications: via ATO online portal (myGov / Tax Agent portal). Processing time: 14-28 days typically.

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
- ATO: ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax
- ATO: Foreign resident capital gains withholding (ato.gov.au/FRCGW)

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
