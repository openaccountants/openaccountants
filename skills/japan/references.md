---
name: japan-references
jurisdiction: JP
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Japan — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. MIT content can be incorporated with attribution. All projects below are license-compatible.

## Shinkoku

- Repository: [kazukinagata/shinkoku](https://github.com/kazukinagata/shinkoku)
- License: MIT
- Language: Japanese
- Scope: AI-agent plugin for Japanese tax filing automation, including bookkeeping, income tax, consumption tax, settlement workflows, e-Tax guidance, and browser-assisted filing through the National Tax Agency's 確定申告書等作成コーナー.
- Why it matters: This is the strongest known Japan-native open-source project in the same problem space as OpenAccountants. It is built around agent skills, uses official Japanese tax terminology, and covers practical workflows beyond pure tax formulas.
- Integration approach:
  - Reference Shinkoku for Japan-specific workflow design, terminology, e-Tax process shape, bookkeeping patterns, and validation ideas.
  - Keep OpenAccountants outputs review-first and accountant-facing.
  - Consider future compatibility with Shinkoku's data model or command workflow for users who want a deeper Japan-native tool.

## Current OpenAccountants Usage

The Japan package already credits Shinkoku in `README.md` because parts of the Japan workflow were informed by that project. Future Japan updates should check Shinkoku first before inventing new e-Tax, bookkeeping, consumption tax, or incorporation workflow patterns.
