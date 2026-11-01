---
name: ao-payroll-social
description: "Angola p for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about p in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz, a."
jurisdiction: AO
category: payroll
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Angola Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers with staff in Angola: withholding IRT on Group A pay and declaring to INSS. Bands are in [Income tax](ao-income-tax.md). Self-employed social protection is on the unconfirmed list.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Employer INSS | 8% of gross remuneration (old version) | 2026 | unverified: Decreto Presidencial 227/18 text not opened; INSS contribution pages require login |
| Employee INSS | 3% of gross remuneration (old version) | 2026 | unverified: same source not opened |
| Retired employee INSS | 8% (old version) | 2026 | unverified: same source not opened |
| Food allowance not subject to IRT | Up to Kz 30,000 a month | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-rendimentos-do-trabalho |
| Transport allowance not subject to IRT | Up to Kz 30,000 a month | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-rendimentos-do-trabalho |
| Family allowance not subject to IRT | Up to 5% of monthly base pay, private sector | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-rendimentos-do-trabalho |
| IRT exempt pay | Up to Kz 150,000 a month. Lei 14/25 art 21(3) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |

## The base

IRT base: all pay less compulsory social security contributions and items not subject or exempt. Food and transport above the limits are taxable. No ceiling on the INSS base was stated in the old version; that is unverified.

## Deadlines and filing

| Obligation | 2026 date | Source |
|---|---|---|
| Payroll map and IRT withheld, Group A | 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Annual Modelo 2 | 27 Feb | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| INSS declaration and payment | Monthly; 10th of the following month in the old version is unverified | INSS pages closed |

Steps: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; Menu de Servicos, Declaracoes, IRT, Entregar, Mapa de Remuneracoes; Criar Novo Mapa; pick Nome/Conta, Periodo, Motivo, Confirmar; add workers by Adicionar Linha or Upload de Ficheiro (Excel, CSV or XML, template at Template do ficheiro); Gravar, Validar, Submeter. Above 150 lines, validation runs as a batch and the form moves to Validado when it passes.

## Penalties and interest

Failing to hand over withheld IRT, or handing over less than was deducted: a fine equal to the tax missing, plus criminal proceedings where a crime is presumed (Lei 14/25 art 21(5), https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf). Debts for periods to 31 October 2025 had interest forgiven if tax and fine were paid by the end of June 2026; regimes of special taxation, final court decisions and FY2025 obligations falling due in 2026 are excluded (art 33).

## Cross-border points

Non-resident staff are within IRT on Angolan service income. Treaties: [cross-border](ao-cross-border.md).

## Two worked examples that recompute

**Employee with allowances.** Salary Kz 300,000, food 40,000, transport 30,000; social security deducted Kz 9,000 as declared.

```oa-check
name: Monthly withholding
inputs:
  salary: 300000
  food: 40000
  transport: 30000
  ss: 9000
steps:
  - taxable_food: max(food - 30000, 0)
  - taxable_transport: max(transport - 30000, 0)
  - base: salary + taxable_food + taxable_transport - ss
  - tax: 49250 + (base - 300000) * 0.19
expected:
  base: 301000.0
  tax: 49440.0
```

**Band edge.** Kz 200,000 and Kz 210,000 fall either side of the Annex I fixed-amount jump.

```oa-check
name: Annex I jump at Kz 200,000
inputs:
  low: 200000
  high: 210000
steps:
  - tax_low: 12500 + (low - 150000) * 0.16
  - tax_high: 31250 + (high - 200000) * 0.18
  - rise: tax_high - tax_low
expected:
  tax_low: 20500.0
  tax_high: 33050.0
  rise: 12550.0
```

## Ask the client first

- Gross pay broken into base, food, transport, family allowance?
- Social security deducted?
- Number of staff (over 150 lines goes to batch)?
- Pensioners on payroll?
- Payment month?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT, IRT page (whole page read; undated) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-rendimentos-do-trabalho | 2026-11-01 |
| AGT quick guide, monthly payroll map (read in part: steps) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/irt/novos-guias/guia-rapido-mapa-mensal-de-remuneracoes-de-irt.pdf | 2026-11-01 |

Not yet confirmed: All INSS rates, base and due date: Decreto Presidencial 227/18 was not opened and portal.inss.gov.ao contribution pages sit behind a login. Coverage (family, pension, unemployment) and self-employed rates (Decreto Legislativo Presidencial 2/22 seen only in search results).
