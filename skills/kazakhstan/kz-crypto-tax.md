---
name: kz-crypto-tax
description: >
  Use this skill whenever asked about taxation of cryptocurrency and digital mining in Kazakhstan.
  Trigger on phrases like "Kazakhstan crypto tax", "crypto mining tax Kazakhstan", "майнинг налог
  Казахстан", "AIFC crypto", "digital asset tax Kazakhstan", "плата за цифровой майнинг". Covers the
  digital-mining fee on electricity, taxation of mining income, the AIFC (Astana) regulated-exchange
  framework, and how individuals' gains on digital assets are taxed under the 2026 Tax Code. ALWAYS
  read this before any Kazakhstan crypto work.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan Cryptocurrency & Digital Mining Tax — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | Kazakhstan |
| Topic | Digital mining + digital-asset taxation |
| Currency | KZT (₸); many amounts indexed to MRP (МРП) = ₸4,325 for 2026 (verify against the 2026 budget law) |
| Individual income tax (ИПН) | Flat 10% |
| Mining electricity fee | Plata za tsifrovoy mayning (плата за цифровой майнинг) — a per-kWh charge on power used for mining, banded by the electricity price (verify current ₸/kWh band table) |
| Regulated trading | Only via exchanges licensed in the Astana International Financial Centre (AIFC / МФЦА); trading outside the AIFC is restricted |
| Tax authority | State Revenue Committee (КГД, kgd.gov.kz); AIFC for licensing |
| Legislation | Tax Code of Kazakhstan (2026); Law "On Digital Assets in the Republic of Kazakhstan" |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| Whether the user is a licensed miner | Assume unlicensed → flag licensing requirement |
| Trading venue unknown | Assume non-AIFC → flag the restriction |
| Cost basis of disposed crypto unknown | Cannot compute gain — request acquisition records |
| Mining electricity band unknown | Flag for reviewer; do not guess the ₸/kWh fee |

## Section 2 — Legal & Regulatory Status

- **Two categories of digital assets:** *secured* (backed/tokenised real assets) and *unsecured* (e.g. Bitcoin). Issuance and "white-listed" trading are channelled through the **AIFC**.
- **Mining is legal but licensed.** Miners must be registered/licensed and buy power within the regulated framework; a dedicated **digital-mining fee** applies to the electricity consumed.
- **Exchange/trading** of unsecured digital assets by residents is intended to run through **AIFC-licensed exchanges**; peer-to-peer/offshore trading sits in a grey/restricted zone — flag it.

## Section 3 — Taxation (Tier 1)

### Mining income
- Income from mining (whether realised in crypto or fiat) is **business income** → corporate income tax (КПН, 20%) for entities or individual income tax (ИПН, 10%) for individuals, on the net result.
- The **digital-mining fee** on electricity is a **separate** charge on top of income tax, scaled to the price paid per kWh (cheaper power → higher fee). Verify the current band table.

### Individuals' gains on digital assets
- A gain on **disposal** of a digital asset (sale proceeds − documented acquisition cost) is **taxable income** for an individual at **ИПН 10%**, declared in the annual individual declaration. Losses and undocumented cost basis → flag.
- Crypto-to-crypto and timing rules under the 2026 Tax Code: **verify** (treat disposal-for-value as the taxable event by default).

## Section 4 — Worked Examples

**Example 1 — Individual sells BTC.** Buys BTC for ₸4,000,000, sells for ₸6,000,000. Gain ₸2,000,000 × 10% ИПН = **₸200,000**, declared in the annual return. (Requires acquisition proof.)

**Example 2 — Home miner.** Mines and sells coins for ₸3,000,000 in the year; documented costs ₸1,200,000. Net ₸1,800,000 taxed at ИПН 10% = ₸180,000, **plus** the digital-mining fee on the electricity consumed (separate). Licensing required.

## Section 10 — Prohibitions
- NEVER assert that offshore/P2P crypto trading by residents is unrestricted — it is channelled through the AIFC.
- NEVER compute a gain without documented acquisition cost.
- NEVER omit the digital-mining fee for miners — it is separate from income tax.
- NEVER state a specific ₸/kWh mining fee or VAT treatment without verifying the current 2026 figures.
- NEVER present a figure as final — direct the client to a Kazakhstan accountant.

## Disclaimer
This skill is informational only and not tax, legal, or financial advice. Kazakhstan's digital-asset and mining rules are evolving (new Tax Code 2026, AIFC rules) — verify current rates, the digital-mining fee bands, and licensing status with the КГД and AIFC. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant before filing. The most up-to-date version is maintained at [openaccountants.com](https://www.openaccountants.com).
