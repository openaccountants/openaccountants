---
name: romania-references
jurisdiction: RO
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Romania — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT, Apache-2.0, GPL-3.0, and AGPL-3.0 content can all be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## Declarații ANAF

- Repository: [IncrementalCommunity/declaratii-anaf](https://github.com/IncrementalCommunity/declaratii-anaf)
- License: AGPL-3.0
- Stars: 14
- Language: Romanian
- Scope: ANAF declaration validation and PDF generation for key Romanian tax forms including D100 (impozit pe venit), D106 (contribuții sociale), D112 (declarație privind obligațiile de plată), D390 (declarație recapitulativă TVA), and D394 (declarație informativă TVA).
- Why it matters: AGPL-3.0 licensed with direct coverage of the most important ANAF declaration forms. Validation logic ensures compliance with ANAF's submission requirements.
- Integration approach:
  - AGPL-3.0 is the same license family as OpenAccountants. Content can be incorporated with attribution.
  - Use as a reference for ANAF declaration XML/PDF structure, field validation rules, and form-specific computation logic.

## PFASimplu

- Repository: [ClimenteA/PFASimplu](https://github.com/ClimenteA/PFASimplu)
- License: verify before reuse
- Stars: 35
- Language: Romanian
- Scope: Simplified accounting application for Romanian PFA (Persoană Fizică Autorizată) and II (Întreprindere Individuală) entities.
- Why it matters: Addresses the most common small-business/freelancer entity types in Romania (PFA and II). The 35 stars suggest meaningful adoption in the Romanian developer community.
- Integration approach:
  - Reference for PFA/II bookkeeping workflows, norma de venit vs sistem real (lump-sum vs actual income), and ANAF reporting requirements for sole traders.
  - Treat as reference-only until the license is confirmed.

## Taxe PFA

- Repository: [taxepfa/taxepfa.github.io](https://github.com/taxepfa/taxepfa.github.io)
- License: MIT
- Stars: 38
- Contributors: Active (last update March 2026)
- Language: TypeScript / Romanian
- Scope: Complete PFA (sole trader) tax calculator implementing 2024 rates: CAS (pension) 25%, CASS (health) 10%, income tax 10%. Handles tiered CAS thresholds (12× vs 24× minimum wage), CASS calculation, deductible expenses, multi-currency support (EUR/USD/GBP→RON via BNR rates), and VAT threshold tracking.
- Why it matters: MIT-licensed, 38 stars, very actively maintained. Implements the exact PFA tax logic Romanian freelancers need: the CAS threshold system (no CAS under 12× min wage, 12× base between 12–24× min wage, 24× base above), CASS always applies, and 10% flat income tax after deductions.
- Integration approach:
  - MIT is fully compatible. Tax rate constants (CAS 25%, CASS 10%, income tax 10%), threshold logic, and deductible expense handling directly usable.
  - Reference for Romanian PFA net income computation and VAT registration threshold tracking.

## ANAF VAT Verification

- Repository: [itrack/anaf](https://github.com/itrack/anaf)
- License: MIT
- Stars: 151
- Language: Romanian / English (PHP)
- Scope: PHP library for the ANAF VAT verification REST API, implementing Art. 316 Cod Fiscal (TVA la încasare status, split TVA, inactive taxpayer checks).
- Why it matters: MIT-licensed with strong adoption (151 stars). Provides programmatic access to ANAF's taxpayer verification service, which is essential for Romanian B2B invoicing compliance.
- Integration approach:
  - MIT is fully compatible. API integration patterns and Art. 316 verification logic directly usable.
  - Reference for ANAF REST API endpoints, TVA status checks, and Romanian fiscal code validation.

## DUKIntegrator

- Repository: [mihaikelemen/DUKIntegrator](https://github.com/mihaikelemen/DUKIntegrator)
- License: MIT
- Language: Romanian / English
- Scope: Dockerised ANAF DUKIntegrator for declaration validation. Wraps ANAF's official Java-based validation tool in a container for automated validation workflows.
- Why it matters: MIT-licensed containerised version of ANAF's official declaration validator. Useful for automated testing and CI/CD validation of generated declarations.
- Integration approach:
  - MIT is fully compatible. Docker setup and validation workflow patterns directly usable.
  - Reference for ANAF declaration validation requirements, error codes, and submission pre-checks.
