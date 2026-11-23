---
name: australia-references
jurisdiction: AU
last_updated: 2026-11-24
version: 1.2
description: Primary source references and related open-source projects for this jurisdiction.
tier: 2
---

# Australia — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT, Apache-2.0, GPL-3.0, and AGPL-3.0 content can all be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## PolicyEngine Australia

- Repository: [PolicyEngine/policyengine-au](https://github.com/PolicyEngine/policyengine-au)
- License: AGPL-3.0
- Language: English
- Scope: Full Australian tax-benefit microsimulation model covering personal income tax, Medicare levy, HECS-HELP repayment thresholds, and superannuation rules.
- Why it matters: Comprehensive, actively maintained microsimulation with detailed modelling of Australian tax and transfer policy. Strong validation source for PIT brackets, offsets, and levy calculations.
- Integration approach:
  - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
  - Use as a validation reference for income tax brackets, Medicare levy surcharge thresholds, HECS-HELP repayment rates, and superannuation contribution caps.

## Aussie Tax Helper

- Repository: [kazimurtaza/aussie-tax-helper](https://github.com/kazimurtaza/aussie-tax-helper)
- License: Apache-2.0
- Stars: 6
- Language: English
- Scope: ATO 2024-25 tax calculator with work-from-home deduction comparison (Fixed Rate method vs Actual Cost method).
- Why it matters: Practical focus on the WFH deduction methods that are a common pain point for individual filers. Apache-2.0 is license-compatible.
- Integration approach:
  - Reference for WFH deduction logic and ATO rate tables.
  - Apache-2.0 permits incorporation with attribution.

## Quick Tax Calc

- Repository: [zorfling/quick-tax-calc](https://github.com/zorfling/quick-tax-calc)
- License: verify before reuse
- Language: English
- Scope: ATO individual tax rates calculator.
- Why it matters: Lightweight reference for Australian individual income tax rate schedules.
- Integration approach:
  - Reference for tax bracket calculations and rate verification against ATO published tables.
  - Treat as reference-only until the license is confirmed.

## AU Tax Legislation Corpus

- Repository: [ryanduguid/au-tax-legislation-corpus](https://github.com/ryanduguid/au-tax-legislation-corpus)
- License: MIT
- Language: English
- Scope: Builds a provenance-rich corpus of in-force Commonwealth tax legislation (ITAA 1936/1997, GST Act, TAA 1953, FBTAA and related Acts) from the Federal Register of Legislation, with exact compilation identifiers attached to every extract.
- Why it matters: Guides in this pack cite sections of the ITAA 1997/1936 and TAA 1953. This corpus lets a retrieval system verify each citation against the in-force compilation text rather than trusting secondary summaries.
- Integration approach:
  - MIT permits incorporation with attribution.
  - Use as the primary-source verification layer when reviewing or updating any Australian guide's legislative citations.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

## Aus Accounting MCP (v0.12.0)

- Repository: [ryanduguid/australian-accounting: aus-accounting-mcp](https://github.com/ryanduguid/australian-accounting/tree/main/apps/aus-accounting-mcp)
- Release: [aus-accounting-mcp/v0.12.0](https://github.com/ryanduguid/australian-accounting/releases/tag/aus-accounting-mcp/v0.12.0) · [PyPI 0.12.0](https://pypi.org/project/aus-accounting-mcp/0.12.0/) · [MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.ryanduguid%2Faus-accounting&version=latest) · [Glama](https://glama.ai/mcp/servers/ryanduguid/australian-accounting)
- License: AGPL-3.0-or-later
- Language: English
- Scope: Local stdio MCP server for Australian accounting workflows: ATO small business benchmark reviews, Payday Super timing and evidence packs, Division 7A review, GST coding and BAS reconciliation review, 102 bounded tax and super worksheets (when paired with `australian-tax-calculators` 1.2.0), and cited retrieval from a user's local Markdown folder.
- Why it matters: Complements the Australian skill pack with deterministic local calculation and review tools over MCP (including a `.mcpb` Desktop bundle) without sending client figures to an external calculator service.
- Integration approach:
  - AGPL-3.0-or-later is in the same license family as OpenAccountants.
  - Pair with OpenAccountants Australian skills when an AI workflow needs verified deterministic worksheets alongside legislative guidance.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

## Australian Tax Calculators (v1.2.0)

- Repository: [ryanduguid/australian-accounting: australian-tax-calculators](https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators)
- Release: [australian-tax-calculators/v1.2.0](https://github.com/ryanduguid/australian-accounting/releases/tag/australian-tax-calculators/v1.2.0)
- License: AGPL-3.0-or-later
- Language: English
- Scope: Standalone local Rust CLI providing 102 bounded Australian tax and superannuation calculation worksheets covering income tax, PAYG withholding, super caps, Division 7A, Division 293/296, CGT, FBT, GST, fuel tax credits, LCT, WET, ASIC fees, and state land tax, stamp duty, FHOG and payroll tax, with explicit statutory scope and refusal boundaries.
- Why it matters: Direct validation and calculation companion for the Australian tax skills; every worksheet outputs structured workings, cited statutory parameters and explicit refusals for out-of-scope inputs.
- Integration approach:
  - AGPL-3.0-or-later is in the same license family as OpenAccountants.
  - Use to cross-check worked examples across the Australian tax and superannuation skills, or invoke locally via CLI or `aus-accounting-mcp` 0.12.0.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

## Payday Super Checker

- Repository: [ryanduguid/australian-accounting: payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)
- License: MIT
- Language: English
- Scope: Checks Australian super contributions against the payday-super deadlines (7 business days from payday, from 1 July 2026) and estimates SG charge exposure on late contributions.
- Why it matters: Direct validation companion to `au-super-guarantee`. The payday-super regime change is the highest-stakes AU payroll change of 2026, and deadline arithmetic (business days, fund-receipt basis) is easy to get wrong.
- Integration approach:
  - MIT permits incorporation with attribution.
  - Use to sanity-check worked examples in `au-super-guarantee` and `australia-payroll`.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).

## ATO Benchmark Compare

- Repository: [ryanduguid/australian-accounting: ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)
- License: MIT
- Language: English
- Scope: Compares profit and loss figures against the ATO small business benchmarks locally, with the working shown.
- Why it matters: The ATO uses industry benchmarks to select small businesses for review; comparing a sole trader's expense ratios before lodgment is a practical risk screen that complements `au-sole-trader-schedule`.
- Integration approach:
  - MIT permits incorporation with attribution.
  - Reference for adding a benchmark-screen step to sole trader workflows.
- Disclosure: maintained by an OpenAccountants contributor (ryanduguid).
