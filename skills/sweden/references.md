---
name: sweden-references
jurisdiction: SE
last_updated: 2026-11-16
version: 1.1
description: Primary source references and related open-source projects for this jurisdiction.
tier: 2
type: router
tax_year: 2026
category: orchestrator
---

# Sweden source and skill routing v1.1

Built from the law. Not yet approved.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this index to select the Swedish job and its primary authority for income year 2026. This is a router, not a tax calculation or permission to reuse software/content. The historical project leads below are preserved for research continuity, not used as legal sources.

## Ask the client first

Identify the taxpayer/entity, residence, income or financial year, job and the output required. Obtain the transaction documents and any actual accountant approval separately.

## The method, step by step

1. For employee or sole-trader income load [se-employee-income-tax](se-employee-income-tax.md) or [se-income-tax](se-income-tax.md), then the relevant source provisions.
2. For private disposals use [se-capital-gains](se-capital-gains.md); for cryptoasset transactions use [sweden-crypto-tax](sweden-crypto-tax.md). A project calculator does not establish cost, classification or a filing position.
3. For employer withholding and benefits use [sweden-payroll](sweden-payroll.md) and [se-benefits-and-allowances](se-benefits-and-allowances.md); for self-employed contributions use [se-social-contributions](se-social-contributions.md).
4. For companies, close-company owners, VAT, transfer pricing or crossing the border load [se-corporate-tax](se-corporate-tax.md), [se-closely-held-company-312](se-closely-held-company-312.md), [sweden-vat-return](sweden-vat-return.md), [se-transfer-pricing](se-transfer-pricing.md) or [se-cross-border](se-cross-border.md), as applicable.
5. For posting/close use [sweden-bookkeeping](sweden-bookkeeping.md), then [sweden-financial-statements](sweden-financial-statements.md) for its annual-report scope. Select the BFN edition by financial-year commencement.
6. Handoff the selected skill, applicable year, taxpayer facts, source excerpts, unresolved questions and working paper. A calculator result never replaces the official rule or named professional approval.

## When to refuse or refer

Do not choose a figure from GitHub projects, merge code, assume a licence, publish an approval label or file a return from this index. Missing source access, uncertain legal scope and unverified licensing require the specific source/permission before use. Do not extend an archived validation claim to the present year or current repository version.

## Historical project leads, unverified and non-operative

Everything in the following archive, including the blanket compatibility statement, licence descriptions, rankings, validation claims and suggested integrations, is a retained historical research claim. None has been newly verified or adopted as an instruction, legal authority or reuse permission. Confirm each repository's current licence, file-level rights, version and test evidence before any reuse. The archive is not part of the routing method above.

OpenAccountants is AGPL-3.0. MIT and AGPL-3.0 content can be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

### Kammaren Tax Engine

- Repository: [Baltsar/kammaren-tax-engine](https://github.com/Baltsar/kammaren-tax-engine)
- License: AGPL-3.0
- Language: Swedish / English
- Scope: Deterministic Swedish tax engine for income year 2026, including income tax, employer fees, municipal tax rates, and 3:12 rules for closely held companies.
- Why it matters: This appears to be the most carefully tested Swedish tax engine found so far. It states that its income tax output is verified against Skatteverket's official 2026 tax table row by row.
- Integration approach:
  - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
  - Use as a validation reference and source for Swedish income tax, municipal tax, employer fees, and 3:12 rule modelling.
  - Tax constants and formulas verified row-by-row against SKV 433 Table 30 : strong validation target.

### KryptoSkatt

- Repository: [bambapappa/kryptoskatt](https://github.com/bambapappa/kryptoskatt)
- License: MIT
- Language: Swedish
- Scope: Swedish cryptocurrency tax calculator that computes capital gains and losses using the average cost method and generates K4 and T2 supporting schedules.
- Why it matters: It is Sweden-native, MIT licensed, and focused on practical declaration outputs for Skatteverket.
- Integration approach:
  - Reference for crypto-specific K4/T2 handling and Skatteverket-facing report structure.
  - Potentially useful as a future compatible workflow for crypto transaction imports.

### K4Skatt

- Repository: [duga3/K4Skatt](https://github.com/duga3/K4Skatt)
- License: MIT
- Language: English / Swedish
- Scope: Generates Swedish K4 tax forms and SRU files from Interactive Brokers trade data, including options, assignments, exercises, and pre-calculated trades.
- Why it matters: Practical bridge between broker exports and Skatteverket-compatible SRU files.
- Integration approach:
  - Reference for investment disposal workflows, K4 structure, and SRU output expectations.
  - Consider future OpenAccountants export compatibility for K4 working papers.

### K4SRU

- Repository: [ebtcap/K4SRU](https://github.com/ebtcap/K4SRU)
- License: verify before reuse
- Language: Swedish
- Scope: Generates K4 SRU files that can be uploaded to Skatteverket and produces Excel review files.
- Why it matters: Strong practical focus on declaration upload files, review outputs, foreign currency accounts, and Skatteverket import workflows.
- Integration approach:
  - Reference for SRU file structure, K4 import process, and review-paper conventions.
  - Treat as reference-only until the license is confirmed.

### Older / Narrower References

- [jonasgroth/swe-income-tax](https://github.com/jonasgroth/swe-income-tax) : MIT JavaScript income tax calculator, useful historically but old.
- [jonas-johansson/SwedishEconomySDK](https://github.com/jonas-johansson/SwedishEconomySDK) : C# Swedish income tax SDK with examples validated against Skatteverket, useful as an additional reference.
- [tessin/SKV260](https://github.com/tessin/SKV260) : .NET library for electronic reporting of Swedish control statements to Skatteverket.

## Sources

| Source and scope | URL | Read on |
|---|---|---|
| Read for the Swedish statutory income-tax source and taxpayer/asset scope; the selected skill supplies the relevant provisions | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-11-16 |
| Read for 2026 official rates and the distinction from third-party calculator claims | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-11-16 |
| Read for official K1/K2/K3 guides and financial-year applicability | https://www.bfn.se/informationsmaterial/vagledningar/ | 2026-11-16 |

Not yet confirmed: every historical project's current licence, attribution/reuse permission, maintenance, tax coverage, formula accuracy, claimed official-table validation and integration compatibility, including the blanket MIT/AGPL compatibility assertion. These claims are non-operative research leads, not source evidence. This router contains no operative rates, deadlines or worked tax cases, so the router shape requires no oa-check.
