---
name: ao-vat-gst
description: "Angola VAT (IVA) for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about VAT (IVA) in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz."
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

# Angola VAT (IVA) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Persons and entities that independently carry on economic activity, importers, anyone wrongly charging IVA on an invoice, buyers of services from non-residents with no Angolan establishment, public bodies acting outside their authority, and parties, unions and religious bodies making taxable supplies. Taxable: supplies of goods and services in Angola for consideration, and imports.

The AGT page still describes the 2020 regimes (USD 250,000 limit, 3% transitional). Do not apply them: Lei 14/25 art 23(2) refers to the current exclusion and simplified regimes, whose limits the old version gave as below and which remain unverified.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 14% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado |
| Industrial equipment, import or transfer by the manufacturer | 5% after AGT procedure proving industrial nature and purpose. Lei 14/25 art 23(1) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Cabinda, imports and goods | AGT page: 2%. Old version: 1%, and 2% for port and water services. The two disagree | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado |
| Simplified regime | 7% on turnover (old version) | 2026 | unverified: Lei 14/23 code text not opened |
| Simplified range | Kz 25,000,000 to 350,000,000 (old version) | 2026 | unverified: Lei 14/23 code text not opened |
| General regime above | Kz 350,000,000 (old version) | 2026 | unverified: Lei 14/23 code text not opened |
| Hotel and restaurant | 7% subject to conditions (old version) | 2026 | unverified: no official text opened |
| Certain food and farm inputs | 5% (old version); the AGT page lists Annex I foods as exempt | 2026 | unverified: no current annex opened |
| Mobile payment platforms authorised by BNA | Exempt from IVA and stamp duty. Lei 14/25 art 35 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Captive VAT: oil investors, State | 100% of invoiced IVA withheld by buyer; public enterprises excepted | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado |
| Captive VAT: BNA, banks, insurers, telecoms | 50% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado |

## The base

Output tax on supplies less input tax invoiced, paid on import, or self-assessed on supplies from unrepresented foreign suppliers. Exempt on the AGT page: Annex I foods, medicines, disability aids, books, residential rent, transactions under SISA, games subject to special tax, public passenger transport, financial intermediation, health insurance and life cover, recognised education, medical services, ambulances, medical equipment for health establishments, Annex II oil products.

## Deadlines and filing

| Obligation | 2026 date | Source |
|---|---|---|
| General: Modelo 7, annexes, payment | 15th of every month. The calendar does not state which period each date covers | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| General: SAF-T upload | 31 Jan, 28 Feb, 31 Mar, 30 Apr, 31 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 31 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Simplified: return and payment | 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Change of regime when turnover passes the limit | End of the month after the operation. Lei 14/25 art 23(2) | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |

The AGT page still says IVA is due by the end of the following month. The 2026 calendar shows the 15th.

Steps: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; Menu de Servicos, Declaracoes, IVA, Entregar, Declaracao de IVA; Criar nova Declaracao, Continuar; pick Tipo de Declaracao and Periodo, Continuar; fill Informacoes Gerais, mark taxable operations and the Mapas Anexos, Guardar; fill Apuramento do Imposto (fields 2, 2.1, 2.2, 2.3 fill automatically and can be raised), Guardar; submit with Submeter and print the Nota de Liquidacao.

## Penalties and interest

AGT may change the regime itself when a taxpayer does not (Lei 14/25 art 23(3)). Penalty percentages for late returns and payment are unverified.

## Cross-border points

Services from non-residents with no Angolan establishment: the buyer accounts for the tax. Imports: Customs assesses. Exempt imports include those of goods exempt domestically and re-imports in the same state.

## Two worked examples that recompute

**General regime month.**

```oa-check
name: Monthly IVA
inputs:
  sales: 10000000
  input_vat: 600000
steps:
  - output: sales * 0.14
  - payable: output - input_vat
expected:
  output: 1400000.0
  payable: 800000.0
```

**Decision: is the 5% procedure worth starting?** Manufacturer buying Kz 10,000,000 of industrial equipment.

```oa-check
name: 14% or 5% on industrial equipment
inputs:
  price: 10000000
steps:
  - standard: price * 0.14
  - reduced: price * 0.05
  - gap: standard - reduced
expected:
  standard: 1400000.0
  reduced: 500000.0
  gap: 900000.0
```

## Ask the client first

- Prior year turnover and imports?
- Registered at the large taxpayers office?
- Cabinda operations?
- Customer type (captive VAT at 100% or 50%)?
- Goods or services, and exempt lines?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT, IVA page (whole page read; undated, regime text is out of date, still describes 2020 rules) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-valor-acrescentado | 2026-11-01 |
| AGT quick guide, IVA periodic return (read in part: steps) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/iva/novos-guias/guia-rapido-declaracao-periodica-do-regime-geral-do-iva.pdf | 2026-11-01 |

Not yet confirmed: Republished IVA Code (Lei 14/23), not opened: current regime limits, 7% simplified rate and its input deduction, hotel 7% and food 5% rows, Cabinda rate, which period the 15th covers (old version mentioned the 15th of the second following month), penalties.
