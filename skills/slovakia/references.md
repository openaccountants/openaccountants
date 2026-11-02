---
name: slovakia-references
jurisdiction: SK
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Slovakia — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT, Apache-2.0, GPL-3.0, and AGPL-3.0 content can all be incorporated with attribution. Projects below are license-compatible unless noted otherwise.

## Priznanie Digital

- Repository: [priznanie-digital/priznanie-digital](https://github.com/priznanie-digital/priznanie-digital)
- License: MIT
- Stars: 18
- Contributors: 40
- Language: Slovak / English
- Scope: Full DPFO typ B (Daň z príjmov fyzickej osoby — personal income tax return, type B for self-employed) web application for Slovak freelancers (SZČO — samostatne zárobkovo činná osoba). Supports paušálne výdavky (flat-rate expenses), nezdaniteľné časti základu dane (non-taxable amounts), daňový bonus na dieťa (child tax bonus), and generates XML for electronic filing via slovensko.sk.
- Why it matters: Active project (last push April 2026) with 40 contributors, which is exceptional community involvement for a country-specific tax tool. MIT-licensed and covers the most common freelancer filing scenario in Slovakia.
- Integration approach:
  - MIT is fully compatible. Tax computation logic, deduction rules, and XML generation patterns directly usable.
  - Strong reference for Slovak DPFO typ B calculations, SZČO social/health insurance contributions, paušálne výdavky percentages, and slovensko.sk electronic filing format.
  - The large contributor base suggests the calculations are well-tested against real returns.
