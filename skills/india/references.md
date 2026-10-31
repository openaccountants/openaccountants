---
name: india-references
jurisdiction: IN
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# India — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## taxcalcindia

- Repository: [amrajacivil/taxcalcindia](https://github.com/amrajacivil/taxcalcindia)
- License: MIT
- Language: English
- Scope: Python package for Indian income tax calculation. Supports old and new regimes, salary/business/capital gains income, common deductions (80C, 80D, HRA, professional tax), and slab-wise breakdown.
- Integration: MIT. Tax slab logic, regime comparison, and deduction computation directly usable.

## Aikar (आयकर)

- Repository: [debjitl45/aikar](https://github.com/debjitl45/aikar)
- License: MIT
- Language: English / Hindi
- Stars: 5
- Scope: Python library for Indian income tax and capital gains tax calculation. Covers old/new regimes, equity/debt/gold capital gains, and ITR form selection guidance.
- Integration: MIT. Capital gains computation (STCG/LTCG) and regime comparison logic directly usable.

## indian-financial-calculators

- Repository: [Ammar-32-dev/indian-financial-calculators](https://github.com/Ammar-32-dev/indian-financial-calculators)
- License: MIT
- Language: English / TypeScript
- Scope: Income tax calculator for FY 2025-26 with dual regime comparison, age-based calculations, deduction optimization suggestions, and enhanced rebate calculations up to INR 12 lakh.
- Integration: MIT. UI patterns for regime comparison and rebate logic usable.

## india-compliance

- Repository: [resilient-tech/india-compliance](https://github.com/resilient-tech/india-compliance)
- License: GPL-3.0
- Stars: 235
- Language: Python / JavaScript (ERPNext/Frappe framework)
- Scope: Indian GST and TDS compliance module for ERPNext. Contains:
  - **GST rate templates** (`gst_india/data/tax_defaults.json`): Item tax templates for GST 0%, 1%, 3%, 5%, 6%, 7.5%, 12%, 18%, 28% with CGST/SGST/IGST/RCM account structures, plus sales and purchase tax templates for in-state, out-state, reverse charge, and composition scenarios.
  - **HSN code master** (`gst_india/data/hsn_codes.json`): ~1,200 four-digit HSN codes with commodity descriptions. Does not include rate mappings.
  - **TDS rate tables** (`income_tax_india/data/tds_details.json`): Comprehensive TDS rates for FY 2026-27 under Income Tax Act 2025 (Section 393 series), covering 35+ payment categories with rates by entity type (Individual, Company, No PAN) and thresholds.
  - **TDS rate tables (legacy)** (`income_tax_india/data/tds_details_old.json`): TDS rates under Section 194 series for FY 2023-24 through FY 2025-26, covering 194C, 194D, 194DA, 194H, 194I(a/b), 194JA, 194JB, 194, 193, 194A, 194B, 194BB, 194EE, 194F, 194G, 194LA, 192A, 194LBB, 194IA, 194Q, 206C(1H).
  - **GSTR-1/GSTR-3B utilities**: Excel templates (`gstr1_excel_template_v2.1.xlsx`, `gstr3b_excel_utility_v5.7.xlsx`) for return preparation.
  - **E-invoice and e-way bill constants**: Configuration and validation logic for e-invoice and e-way bill generation.
- Integration: GPL-3.0. Rate tables and HSN data used to enrich `india-gst.md` and `in-tds-freelance.md` skills. Data verified against the codebase as of May 2026.
