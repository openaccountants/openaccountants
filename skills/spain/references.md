---
name: spain-references
jurisdiction: ES
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Spain — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects listed below have compatible licenses and their content can be incorporated with proper attribution.

## Declaración de la Renta España

- Repository: [joseconti/declaracion-renta-espana](https://github.com/joseconti/declaracion-renta-espana)
- License: GPL-3.0 (compatible with AGPL-3.0)
- Language: Spanish
- Stars: 143
- Scope: AI skill for Spanish IRPF 2025. Built from 3,214 pages of official source material: the AEAT Manual Práctico de Renta 2025 (1,903 pages) plus the four foral territory manuals (Navarra 308, Álava 243, Gipuzkoa 214, Bizkaia 546).
- Why it matters: Deepest known open-source treatment of Spanish IRPF, especially foral territories (País Vasco, Navarra). Native Spanish developers processing official AEAT documentation in their own language.
- Integration: GPL-3.0 flows into AGPL-3.0. Content can be adapted with attribution. Especially useful for foral territory rules that OpenAccountants may be thinner on.

## La Renta

- Repository: [paumrch/larenta](https://github.com/paumrch/larenta)
- License: MIT
- Language: Spanish
- Stars: 73
- Scope: Interactive IRPF 2025 guide with 377 deductions across all autonomous communities, structured data, and an assistant that matches deductions to user situations.
- Why it matters: Clean structured data on all Spanish deductions with official AEAT sources.
- Integration: Already credited in OpenAccountants. MIT content freely usable.

## Hacienda CLI

- Repository: [jatorre/hacienda-cli](https://github.com/jatorre/hacienda-cli)
- License: check before integration
- Language: Spanish
- Scope: CLI that authenticates with AEAT's electronic office (Cl@ve / certificate), downloads fiscal data, uploads XML declarations, and validates against official XSD schemas. Designed for AI agents to generate and submit Modelo 100 XML.
- Why it matters: Bridges the gap between "working papers" and "actual filing." Defines the XML structure and field dictionary for Modelo 100 that an AI agent needs to produce machine-readable output.
- Integration: Reference for understanding AEAT's XML schema, field codes, and the EDFI import process. If license permits, workflow patterns can inform the `spain-return-assembly.md` skill.

## What to pull in

1. **Foral territory rules** from declaracion-renta-espana — País Vasco (Álava, Bizkaia, Gipuzkoa) and Navarra have completely separate IRPF regimes with different brackets, deductions, and filing authorities. These are the biggest gap in the current OpenAccountants Spain package.
2. **Deduction updates** from larenta — cross-reference the 377 deductions against the current `es-irpf-deductions.md` to catch any we're missing or that changed for 2025.
3. **XML field mapping** from hacienda-cli — understanding the Modelo 100 XML structure makes the return assembly skill more precise about what fields the asesor fiscal actually needs to fill.
