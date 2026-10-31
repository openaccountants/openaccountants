---
name: turkey-references
jurisdiction: TR
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Turkey — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. AGPL-3.0, MIT, and Apache-2.0 are all compatible licenses. Projects below can be incorporated with attribution.

## vergihesaplayici.com

- Repository: [ozgurg/vergihesaplayici.com](https://github.com/ozgurg/vergihesaplayici.com)
- License: AGPL-3.0
- Language: Turkish
- Stars: 66
- Releases: 276
- Scope: Full Turkish tax calculator covering gelir vergisi (income tax), damga vergisi (stamp tax), and other tax types. Actively maintained with comprehensive bracket tables and rate updates tracked across tax years.
- Integration: Same license family (AGPL-3.0). Income tax bracket tables, calculation logic, and rate history directly usable. Strong validation reference for Turkish gelir vergisi computations.

## fatura (GİB e-Arşiv)

- Repository: [mlevent/fatura](https://github.com/mlevent/fatura)
- License: MIT
- Language: Turkish (PHP)
- Stars: 165
- Scope: GİB e-Arşiv portal integration for generating e-invoice (e-Fatura) and e-SMM (serbest meslek makbuzu) documents programmatically. Handles authentication, invoice creation, and cancellation via the official GİB API.
- Integration: MIT — fully compatible. Reference for e-invoice workflows, GİB API structure, and e-Arşiv document formats. Useful for validating e-Fatura compliance rules in the VAT skill.

## borsapy

- Repository: [saidsurucu/borsapy](https://github.com/saidsurucu/borsapy)
- License: Apache-2.0
- Language: Python / English
- Stars: 629
- Scope: Python library for Turkish financial markets data (Borsa İstanbul). Includes fund classification with tax categories, equity data, and market analytics relevant to capital gains and investment income taxation.
- Integration: Apache-2.0 — compatible. Fund tax category mappings and financial instrument classifications useful for investment income and capital gains tax treatment in Turkey.

## gelir-vergisi-kesintisi-hesaplama

- Repository: [berkaygure/gelir-vergisi-kesintisi-hesaplama](https://github.com/berkaygure/gelir-vergisi-kesintisi-hesaplama)
- License: verify before reuse
- Language: TypeScript / Turkish
- Scope: Turkish income tax withholding (gelir vergisi kesintisi) calculator implementing current bracket tables for cumulative withholding calculations throughout the tax year.
- Integration: Reference for income tax withholding bracket tables and cumulative calculation methodology. Useful for validating payroll-related gelir vergisi computations. Verify license before incorporating code.

## vergi-hesapla (Midas)

- Repository: [umuterturk/vergi-hesapla](https://github.com/umuterturk/vergi-hesapla)
- License: AGPL-3.0
- Stars: 17
- Language: Turkish
- Scope: "Midas Vergi Hesaplama Sitesi" — comprehensive Turkish tax calculation website covering multiple tax types with modern UI. Updated April 2026.
- Integration: AGPL-3.0 — same license family, fully compatible. Additional validation reference for Turkish tax computations.

## E-VİZÖR

- Repository: [arch-yunus/E-VIZOR](https://github.com/arch-yunus/E-VIZOR)
- License: MIT
- Stars: 4
- Language: Turkish
- Scope: AI + blockchain-based autonomous mali müşavirlik (financial advisory) platform. OCR-based document processing, smart tax calculation, and immutable financial records. Updated May 2026.
- Integration: MIT — fully compatible. Reference for AI-based Turkish tax document processing workflows and mali müşavirlik automation patterns.

## hamitaksln Gelir Vergisi 2025

- Repository: [hamitaksln/hamitaksln.github.io](https://github.com/hamitaksln/hamitaksln.github.io)
- License: verify before reuse
- Stars: 27
- Language: Turkish
- Scope: 2025 Gelir Vergisi Hesaplama (Income Tax Calculation) web tool. Simple calculator implementing the current year's tax brackets.
- Integration: Reference for validating 2025 bracket accuracy. Verify license before code reuse.
