---
name: brazil-references
jurisdiction: BR
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Brazil — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## irpf-investidor

- Repository: [staticdev/irpf-investidor](https://github.com/staticdev/irpf-investidor)
- License: MIT
- Language: Portuguese
- Stars: ~30
- Scope: Calculates costs for stocks, ETFs, and FIIs (real estate funds) for the IRPF Bens e Direitos declaration. Handles B3 CEI data, emoluments, and settlement fees.
- Integration: MIT. Cost basis calculation logic and B3 data parsing directly usable.

## ir_investidor

- Repository: [barbolo/ir_investidor](https://github.com/barbolo/ir_investidor)
- License: MIT
- Language: Portuguese
- Stars: 51
- Scope: Automatic income tax calculation for variable income investors. Supports stocks, options, FIIs (normal and day-trade). Runs locally via Docker.
- Integration: MIT. Investment income tax rules and day-trade vs swing-trade logic can be adapted.

## consolidador-cei

- Repository: [danilofrp/consolidador-cei](https://github.com/danilofrp/consolidador-cei)
- License: GPL-3.0
- Language: Portuguese
- Stars: 20
- Scope: Consolidates B3 CEI statements for IRPF. Generates declaration of assets (bens e direitos) reports and monthly profit/loss tracking.
- Integration: GPL-3.0 flows into AGPL-3.0. Report structure and consolidation logic usable with attribution.

## Leão Faminto API

- Repository: [jeancsanchez/leaofaminto-api-kt](https://github.com/jeancsanchez/leaofaminto-api-kt)
- License: check
- Language: Portuguese / Kotlin
- Scope: API to calculate taxes on stock exchange operations and assist with annual IRPF declaration. Supports B3 brokers, day-trade/swing-trade, FIIs, US stocks/REITs.
- Integration: Reference for Brazilian investment tax computation patterns.
