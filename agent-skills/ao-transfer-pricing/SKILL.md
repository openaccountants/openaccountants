---
name: ao-transfer-pricing
description: "Angola transfer pricing for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about transfer pricing in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ao-transfer-pricing"
  jurisdiction: "AO"
  tax_year: "2026"
  last_updated: "2026-11-01"
---

# Angola Transfer Pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Large taxpayers on the general regime of Imposto Industrial: the 2026 calendar requires the dossier from Grandes Contribuintes. The portal asks for year, annual income and whether special relations exist.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Dossier filing | 30 June 2026, general regime, Grandes Contribuintes | 2026 | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Income threshold | Not stated in the pages opened | 2026 | unverified: text of the transfer pricing rules not opened |

## The base

The arm's length rule text and methods were not opened. The worked figures show arithmetic only.

## Deadlines and filing

30 June 2026 (https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf). Steps: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; Menu de Servicos, Declaracoes, Dossier de Precos de Transferencia, Entregar; fill Exercicio, Proveitos Anuais and Possui relacoes especiais, Confirmar; complete the editable fields; save, validate, submit.

## Penalties and interest

Unverified.

## Cross-border points

Imposto Industrial on the adjustment follows the sector rate in [Corporate income tax](ao-corporate-income-tax.md).

## Two worked examples that recompute

**General rate.**

```oa-check
name: Adjustment at 25%
inputs:
  charged: 2000000
  market: 1500000
steps:
  - adjustment: charged - market
  - tax: adjustment * 0.25
expected:
  adjustment: 500000.0
  tax: 125000.0
```

**Bank at 35%.**

```oa-check
name: Adjustment at 35%
inputs:
  adjustment: 500000
steps:
  - tax: adjustment * 0.35
expected:
  tax: 175000.0
```

## Ask the client first

- On the Grandes Contribuintes list?
- Annual income?
- Related parties and transactions?
- Sector rate?

## Sources

| Source | URL | Read on |
|---|---|---|
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT quick guide, transfer pricing dossier (read in part: steps) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/dossier-de-precos-de-transferencias/guia-rapido-declaracao-de-dossier-de-precos-de-transferencia.pdf | 2026-11-01 |

Not yet confirmed: Who else must file, thresholds, methods, penalties: the rules themselves were not opened.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-01. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ao-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ao-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
