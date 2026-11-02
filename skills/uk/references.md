---
name: uk-references
jurisdiction: GB
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# United Kingdom — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## HMRC Tax Kalculator

- Repository: [hmrc/tax-kalculator](https://github.com/hmrc/tax-kalculator)
- License: Apache-2.0
- Language: English / Kotlin
- Stars: 16
- Scope: Kotlin Multiplatform take-home pay calculator covering income tax, National Insurance, and student loan repayments. Official HMRC repository.
- Why it matters: This is actual HMRC code — the tax authority's own open-source implementation.
- Integration: Apache-2.0 flows into AGPL-3.0. Logic and calculation patterns can be adapted with attribution.

## SavingTool HMRC Income Tax

- Repository: [SavingTool/hmrc-income-tax](https://github.com/SavingTool/hmrc-income-tax)
- License: MIT
- Language: English / TypeScript
- Stars: 22
- Scope: TypeScript library for UK income tax, National Insurance (employee and employer), and student loan calculations. Supports Scottish rates. Updated for 2026/27.
- Why it matters: Clean, well-tested, actively maintained. Covers both employee and employer-side payroll calculations.
- Integration: MIT. Freely usable with attribution.

## HMRC PAYE Estimator

- Repository: [hmrc/paye-estimator](https://github.com/hmrc/paye-estimator)
- License: Apache-2.0
- Language: Scala / JavaScript
- Stars: 3
- Scope: Scala.js library for PAYE tax estimation. Official HMRC repository.
- Why it matters: Another official HMRC open-source tool, useful for validation.
- Integration: Apache-2.0. Compatible.

## BittyTax

- Repository: [BittyTax/BittyTax](https://github.com/BittyTax/BittyTax)
- License: check
- Language: English / Python
- Scope: Cryptocurrency tax calculator implementing UK HMRC rules — Same-Day, Bed & Breakfast, Section 104 Pool, capital gains computation. PDF report generation.
- Why it matters: Comprehensive implementation of UK CGT share-matching rules. Useful reference if OpenAccountants covers investment income.
- Integration: Reference for UK capital gains tax rules and HMRC crypto guidance.
