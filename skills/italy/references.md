---
name: italy-references
jurisdiction: IT
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Italy — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses.

## De-CAF (Modello Redditi PF)

- Repository: [vjt/decaf](https://github.com/vjt/decaf)
- License: MIT
- Language: Italian
- Scope: Generates Modello Redditi PF (quadri RW, RT, RL) from foreign broker data (Interactive Brokers, Schwab). Handles IVAFE, capital gains on securities, forex FIFO, and BCE exchange rates.
- Integration: MIT. Foreign investment reporting logic, IVAFE calculation, and Modello Redditi field mapping directly usable.

## BonusPerMe

- Repository: [nogarasimone/bonusperme](https://github.com/nogarasimone/bonusperme)
- License: AGPL-3.0
- Language: Italian (7 languages)
- Scope: Identifies 40+ national and regional Italian bonuses, tax deductions, and subsidies based on ISEE, income, and family composition. Updated to Legge di Bilancio 2026.
- Integration: Same license (AGPL-3.0). Deduction/benefit eligibility rules and structured data directly usable.

## FatturaElettronica.NET

- Repository: [FatturaElettronica/FatturaElettronica.NET](https://github.com/FatturaElettronica/FatturaElettronica.NET)
- License: BSD
- Language: Italian / C#
- Scope: Read/write/validate Italian electronic invoices (fattura elettronica) in the official SDI XML format. Supports ordinary and simplified invoices.
- Integration: BSD is permissive. XML schema knowledge and validation rules useful for Italian invoicing workflows.

## FatturaHub

- Repository: [lenny76/FatturaHub](https://github.com/lenny76/FatturaHub)
- License: check
- Language: Italian
- Scope: Self-hosted web manager for Italian electronic invoices (FatturaPA). Imports passive invoices (XML/XML.p7m), indexes them, and makes them searchable.
- Integration: Reference for Italian SDI invoice processing patterns.
