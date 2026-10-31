---
name: israel-references
jurisdiction: IL
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Israel — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT and Apache-2.0 content can be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## Skills IL — Tax and Finance

- Repository: [skills-il/tax-and-finance](https://github.com/skills-il/tax-and-finance)
- License: MIT
- Language: Hebrew / English
- Scope: AI agent skills for Israeli tax: payroll calculator, VAT reporting, invoice organizer, withholding tax, pension advisor.
- Why it matters: This is the closest project to the OpenAccountants format for Israel. It provides structured, machine-readable skill files covering the major Israeli tax obligations. Multiple Israel skills in this package were adapted from this project.
- Integration approach:
  - MIT is fully compatible with AGPL-3.0 — content can be incorporated with attribution.
  - Already used as the primary source for freelancer operations, tax withholding, income tax returns, corporate tax strategy, employee tax refunds, cryptocurrency tax reporting, and customs duty skills.
  - Monitor for updates to rates, thresholds, and new skill coverage.

## Income Tax Form 134 Calculator

- Repository: [tomerip/income_tax_t134](https://github.com/tomerip/income_tax_t134)
- License: Apache-2.0
- Language: Hebrew / Python
- Scope: Automates the calculation of Israel Tax Authority Form 134 (טופס 134 — בקשה להקטנת מקדמות), used to request a reduction in advance tax payments (Mikdamot).
- Why it matters: Form 134 is one of the most common freelancer interactions with the ITA. Having an automated calculation reference helps validate Mikdamot reduction logic.
- Integration approach:
  - Apache-2.0 is compatible with AGPL-3.0 — content can be incorporated with attribution.
  - Use as a validation reference for Mikdamot calculation logic in `il-income-tax-returns.md` and `il-freelancer-ops.md`.
  - Cross-check bracket and advance payment formulas against this implementation.

## Tax Forms Generator (Form 1325)

- Repository: [talmiller2/tax_forms_generator](https://github.com/talmiller2/tax_forms_generator)
- License: verify before reuse (14 stars)
- Language: Python / Hebrew
- Scope: Generates Israeli capital gains Form 1325 (דוח רווח הון מניירות ערך) from Interactive Brokers data exports.
- Why it matters: Form 1325 is required for reporting securities capital gains. This project bridges broker data exports to ITA-compatible form output — directly relevant to `il-crypto-tax.md` and capital gains sections of `il-income-tax-returns.md`.
- Integration approach:
  - Treat as reference-only until the license is confirmed as compatible.
  - Reference for Form 1325 field mappings, IB data parsing logic, and NIS conversion methodology.
  - Potential future workflow: OpenAccountants capital gains working papers → Form 1325 output.

## Israel Tax Calculator

- Repository: [israeltaxcalculator/israeltaxcalculator.github.io](https://github.com/israeltaxcalculator/israeltaxcalculator.github.io)
- License: verify before reuse (9 stars)
- Language: JavaScript / Hebrew
- Scope: Web-based Israeli tax calculator covering income tax brackets, Nekudot Zikui (credit points), and National Insurance (Bituach Leumi) contributions.
- Why it matters: Provides a quick-reference implementation of bracket calculations and credit point logic that can be used to validate OpenAccountants bracket tables.
- Integration approach:
  - Treat as reference-only until the license is confirmed as compatible.
  - Use as a cross-validation source for income tax bracket boundaries, credit point values, and Bituach Leumi rate tiers.
  - Compare output against `il-income-tax-returns.md` bracket tables for consistency checks.
