---
name: sweden-references
jurisdiction: SE
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Sweden — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT and AGPL-3.0 content can be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## Kammaren Tax Engine

- Repository: [Baltsar/kammaren-tax-engine](https://github.com/Baltsar/kammaren-tax-engine)
- License: AGPL-3.0
- Language: Swedish / English
- Scope: Deterministic Swedish tax engine for income year 2026, including income tax, employer fees, municipal tax rates, and 3:12 rules for closely held companies.
- Why it matters: This appears to be the most carefully tested Swedish tax engine found so far. It states that its income tax output is verified against Skatteverket's official 2026 tax table row by row.
- Integration approach:
  - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
  - Use as a validation reference and source for Swedish income tax, municipal tax, employer fees, and 3:12 rule modelling.
  - Tax constants and formulas verified row-by-row against SKV 433 Table 30 — strong validation target.

## KryptoSkatt

- Repository: [bambapappa/kryptoskatt](https://github.com/bambapappa/kryptoskatt)
- License: MIT
- Language: Swedish
- Scope: Swedish cryptocurrency tax calculator that computes capital gains and losses using the average cost method and generates K4 and T2 supporting schedules.
- Why it matters: It is Sweden-native, MIT licensed, and focused on practical declaration outputs for Skatteverket.
- Integration approach:
  - Reference for crypto-specific K4/T2 handling and Skatteverket-facing report structure.
  - Potentially useful as a future compatible workflow for crypto transaction imports.

## K4Skatt

- Repository: [duga3/K4Skatt](https://github.com/duga3/K4Skatt)
- License: MIT
- Language: English / Swedish
- Scope: Generates Swedish K4 tax forms and SRU files from Interactive Brokers trade data, including options, assignments, exercises, and pre-calculated trades.
- Why it matters: Practical bridge between broker exports and Skatteverket-compatible SRU files.
- Integration approach:
  - Reference for investment disposal workflows, K4 structure, and SRU output expectations.
  - Consider future OpenAccountants export compatibility for K4 working papers.

## K4SRU

- Repository: [ebtcap/K4SRU](https://github.com/ebtcap/K4SRU)
- License: verify before reuse
- Language: Swedish
- Scope: Generates K4 SRU files that can be uploaded to Skatteverket and produces Excel review files.
- Why it matters: Strong practical focus on declaration upload files, review outputs, foreign currency accounts, and Skatteverket import workflows.
- Integration approach:
  - Reference for SRU file structure, K4 import process, and review-paper conventions.
  - Treat as reference-only until the license is confirmed.

## Older / Narrower References

- [jonasgroth/swe-income-tax](https://github.com/jonasgroth/swe-income-tax) — MIT JavaScript income tax calculator, useful historically but old.
- [jonas-johansson/SwedishEconomySDK](https://github.com/jonas-johansson/SwedishEconomySDK) — C# Swedish income tax SDK with examples validated against Skatteverket, useful as an additional reference.
- [tessin/SKV260](https://github.com/tessin/SKV260) — .NET library for electronic reporting of Swedish control statements to Skatteverket.
