---
name: denmark-references
jurisdiction: DK
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Denmark — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT-licensed projects below can be incorporated with attribution.

## tesoro

- Repository: [libo/tesoro](https://github.com/libo/tesoro)
- License: MIT
- Stars: 24
- Language: Ruby
- Scope: Danish capital gains tax calculator for stock/investment portfolios. Implements the two-tier aktieindkomst (share income) taxation system with progressive rates: 27% up to progressionsgrænsen (DKK 58,900 in 2023) and 42% above. Supports married/unmarried filing with combined progressive threshold for married couples (2×).
- Why it matters: Clean implementation of SKAT's aktieindkomst progressive system with historical threshold data from 2014–2023. MIT license.
- Integration approach: Capital gains rate structure (27%/42% split) and progressive thresholds incorporated into the income tax skill.

## skattefar

- Repository: [ob-vest/skattefar](https://github.com/ob-vest/skattefar)
- License: MIT
- Stars: 0 (new, May 2026)
- Language: TypeScript
- Scope: Danish tax calculator "for mere mortals" — aims to simplify SKAT's complex system into understandable components.
- Integration approach: Reference for Danish tax calculation UX and bracket structure.

## etrade-skat-tools

- Repository: [mpdn/etrade-skat-tools](https://github.com/mpdn/etrade-skat-tools)
- License: MIT
- Stars: 2
- Language: TypeScript
- Scope: Tooling for reporting stock plan sales from E-Trade to Danish SKAT. Handles currency conversion (USD→DKK) using Nationalbanken rates, calculates gains using FIFO, and formats for SKAT reporting.
- Integration approach: Reference for foreign stock income reporting to SKAT, FIFO methodology, and Nationalbanken FX rate sourcing.
