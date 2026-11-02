---
name: ao-tax-overview
description: "Angola tax overview for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about tax overview in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz."
jurisdiction: AO
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Angola Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing the map of Angolan taxes. Calendar year, kwanza (AOA), authority Administracao Geral Tributaria (AGT).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Top IRT rate | 25% on Group A above Kz 10,000,000 a month | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| IRT exempt | Kz 150,000 a month | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Corporate rate | 25%; 10% farming type; 35% banks, insurers, telecoms, oil | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |
| IVA | 14%. Detail in [VAT](ao-vat-gst.md) | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado |

## The base

Separate codes: IRT on work, Imposto Industrial on profits (residents; non-residents on Angolan income), IAC on capital income, IVA on consumption, plus Imposto Predial, Imposto de Selo, IEC, IVM, CEOC, IEJ.

## Deadlines and filing

Full dates in each skill. Headline: IVA general 15th monthly; IRT Group A end of month; Imposto Industrial general 29 May 2026 (https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf).

## Penalties and interest

See each skill.

## Cross-border points

See [cross-border](ao-cross-border.md).

## Two worked examples that recompute

**Company and shareholder.**

```oa-check
name: Profit then dividend
inputs:
  profit: 1000000
steps:
  - cit: profit * 0.25
  - dividend: profit - cit
  - iac: dividend * 0.10
  - net: dividend - iac
expected:
  cit: 250000.0
  net: 675000.0
```

**Decision: pay as salary or dividend?** Kz 300,000 monthly, ignoring social security.

```oa-check
name: Salary or dividend
inputs:
  pay: 300000
steps:
  - salary_tax: 31250 + (pay - 200000) * 0.18
  - dividend_iac: (pay * 0.75) * 0.10
  - salary_net: pay - salary_tax
  - dividend_net: pay * 0.75 - dividend_iac
expected:
  salary_net: 250750.0
  dividend_net: 202500.0
```

## Ask the client first

- Person or company?
- Sector?
- Resident?
- Turnover?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT, Imposto Industrial page (whole page read; undated, may lag the law) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial | 2026-11-01 |
| AGT, IVA page (whole page read; undated, regime text is out of date, still describes 2020 rules) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado | 2026-11-01 |

Not yet confirmed: VAT return frequency for the simplified regime is monthly on the calendar; everything marked unverified in sibling skills.
