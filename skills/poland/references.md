---
name: poland-references
jurisdiction: PL
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Poland — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## Pitly

- Repository: [volodymyr-kovtun/Pitly](https://github.com/volodymyr-kovtun/Pitly)
- License: MIT
- Language: Polish / English
- Stars: 42
- Scope: PIT-38 tax calculator for Polish investors using foreign brokers (Interactive Brokers, Trading 212). Converts trades and dividends to PLN using NBP exchange rates, applies FIFO capital gains, handles dividend withholding credits under PL-US treaty, and generates ready-to-file PIT-38 field values.
- Why it matters: Solves the exact pain point of Polish investors who need to file PIT-38 manually. Well-structured API with clear field mappings to the official form.
- Integration: MIT. Logic for NBP rate conversion, FIFO matching, and PIT-38 field generation can be adapted.

## kloPIT

- Repository: [SkeLLLa/klopit](https://github.com/SkeLLLa/klopit)
- License: AGPL-3.0
- Language: Polish / English
- Scope: Browser-based PIT-38 calculator. Imports broker CSV, fetches NBP rates, applies FIFO, fills PIT-38 and PIT/ZG fields. Runs entirely client-side.
- Why it matters: Same license family as OpenAccountants. Clean implementation of Polish tax law references (ustawa o PIT).
- Integration: AGPL-3.0. Directly compatible. Calculation logic and legal references can be incorporated.

## pit8c

- Repository: [iyazerski/pit8c](https://github.com/iyazerski/pit8c)
- License: MIT
- Language: English / Polish
- Stars: 6
- Scope: Python CLI that transforms raw broker reports into PIT-8C declarations. Handles FIFO trade matching, currency conversion, and PDF report generation.
- Why it matters: Covers PIT-8C (investment income reporting) which complements PIT-38 (capital gains tax).
- Integration: MIT. Freely usable.

## pit-38 (pbialon)

- Repository: [pbialon/pit-38](https://github.com/pbialon/pit-38)
- License: MIT
- Language: Polish / English
- Stars: 18
- Scope: Python scripts for PIT-38 calculation covering both stocks and cryptocurrency. Supports multiple broker formats.
- Why it matters: Handles crypto-specific PIT-38 workflows alongside traditional investments.
- Integration: MIT. Freely usable.
