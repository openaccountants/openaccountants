---
name: italy-references
jurisdiction: IT
tax_year: 2026
last_updated: 2026-11-14
version: 2.0
description: Open-source projects that handle Italian tax data (Modello Redditi PF foreign assets, bonuses and deductions, FatturaPA e-invoices), with their licences checked, and which Italy skill to load instead for the tax rules themselves.
category: integration
tier: 2
type: router
---

# Italy: related open-source projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. This file lists open-source code that works with Italian tax data, so a developer or an AI can find it, and routes every tax question to the Italy skill that owns the rule. It carries no rates or deadlines of its own.

## The method, step by step

1. **Decide whether the question is about code or about tax.** A question about a tax rule, rate, deadline or form goes to the Italy skill named in step 3, not to these projects. These projects are tools; their outputs must be checked against the skill and the official source it names.
2. **Pick the project by job.**

| Project | Repository | Licence (read on the repository today) | What it does | Use with |
| --- | --- | --- | --- | --- |
| De-CAF | https://github.com/vjt/decaf | MIT | Builds Modello Redditi PF sections RW, RT and RL from foreign broker data (Interactive Brokers, Schwab): IVAFE, gains on securities, forex FIFO, ECB exchange rates | `it-cross-border`, `italy-crypto-tax`, `it-income-tax` |
| BonusPerMe | https://github.com/nogarasimone/bonusperme | AGPL-3.0 or later (the LICENSE file names the GNU Affero General Public License, version 3 or later) | Finds national and regional bonuses, deductions and subsidies from ISEE, income and family make-up; the project says it is updated to the 2026 budget law | `it-irpef-employees`, `italy-tax-optimization` |
| FatturaElettronica.NET | https://github.com/FatturaElettronica/FatturaElettronica.NET | BSD-style (the LICENSE.txt permits redistribution with or without modification on conditions) | Reads, writes and validates FatturaPA XML, ordinary and simplified | `italy-einvoice` |
| FatturaHub | https://github.com/lenny76/FatturaHub | MIT | Self-hosted manager for received e-invoices (XML and XML.p7m): import, index, search | `italy-einvoice`, `italy-bookkeeping` |

3. **Route the tax rule.** E-invoice format, SdI, stamp duty: `italy-einvoice`. Foreign assets, residence, withholding: `it-cross-border`. Employee and investment IRPEF: `it-irpef-employees`. Self-employed IRPEF: `it-income-tax`. Planning and bonuses: `italy-tax-optimization`. Books and registers: `italy-bookkeeping`.
4. **Check the licence before reuse.** AGPL-3.0 and MIT code can be combined with OpenAccountants' AGPL code; BSD-style code can too, keeping its notice. Read the project's own licence file again before copying code: licences can change.

## When to refuse or refer

- Do not take a rate, threshold or deadline from a project's code or README as authority: load the Italy skill and its official source.
- Do not treat a project's output as a filed return. Returns are filed through the Agenzia delle Entrate's services, by the taxpayer or an intermediary.
- Licence questions beyond the plain text of the licence file (dual licensing, patents, commercial use): refer to a lawyer.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| De-CAF repository. Read for its scope (RW, RT, RL, IVAFE) and its MIT licence | https://github.com/vjt/decaf | 2026-11-14 |
| BonusPerMe repository. Read for its scope and its LICENSE file (GNU Affero General Public License, version 3 or later) | https://github.com/nogarasimone/bonusperme | 2026-11-14 |
| FatturaElettronica.NET repository. Read for its scope (FatturaPA read, write, validate) and its LICENSE.txt (BSD-style terms) | https://github.com/FatturaElettronica/FatturaElettronica.NET | 2026-11-14 |
| FatturaHub repository. Read for its scope (received e-invoice manager) and its MIT licence | https://github.com/lenny76/FatturaHub | 2026-11-14 |

Not yet confirmed: whether each project's tax logic is current for 2026 (not tested here; check outputs against the skills named above).
