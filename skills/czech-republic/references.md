---
name: czech_republic-references
jurisdiction: CZ
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Czech Republic — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT, Apache-2.0, GPL-3.0, and AGPL-3.0 content can all be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## OSVČ Kalkulačka

- Repository: [fertek/osvc-kalkulacka](https://github.com/fertek/osvc-kalkulacka)
- License: verify before reuse
- Language: Czech
- Scope: OSVČ (self-employed / osoby samostatně výdělečně činné) DPFO income tax calculator with social and health insurance contribution computation. Verifies results against official EPO XML exports from the Finanční správa.
- Why it matters: Focuses on the self-employed tax return workflow, which is the most complex individual filing scenario in CZ. Validation against EPO XML adds confidence in the calculations.
- Integration approach:
  - Reference for OSVČ tax computation, social/health insurance bases, and paušální výdaje (flat-rate expense) percentages.
  - Treat as reference-only until the license is confirmed.

## Czech Income Tax Calculator

- Repository: [zakjan/czech-income-tax-calculator](https://github.com/zakjan/czech-income-tax-calculator)
- License: AGPL-3.0
- Stars: 28
- Language: Czech / English
- Scope: Czech income tax calculator web application.
- Why it matters: AGPL-3.0 licensed with meaningful community adoption (28 stars). Directly compatible with OpenAccountants.
- Integration approach:
  - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
  - Use as a validation reference for Czech PIT brackets, slevy na dani (tax credits), and nezdanitelné části základu daně (non-taxable portions).

## Odoo Czech VAT Filing Addon

- Repository: [tompta1/odoo-addon-czech-vat-filing](https://github.com/tompta1/odoo-addon-czech-vat-filing)
- License: MIT
- Language: Czech / English
- Scope: Czech VAT filing XML generation for DPHDP3, DPHKH1, and DPHSHV declarations with official Ministry of Finance XSD validation.
- Why it matters: MIT-licensed implementation of the official Czech VAT XML schemas (DPHDP3 for VAT return, DPHKH1 for kontrolní hlášení, DPHSHV for souhrnné hlášení). XSD validation against MF schemas provides strong correctness guarantees.
- Integration approach:
  - MIT is fully compatible. XML schema logic and VAT declaration structure directly usable.
  - Reference for Czech VAT return field mapping, kontrolní hlášení structure, and Finanční správa submission formats.
