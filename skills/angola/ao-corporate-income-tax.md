---
name: ao-corporate-income-tax
description: "Angola c for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about c in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz, o."
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

# Angola Corporate Income Tax (Imposto Industrial) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies, cooperatives, foundations, associations, autonomous funds and public enterprises with seat or effective management in Angola; entities without legal personality; non-residents earning income in Angola; undivided estates and companies before final registration. Shipping and air companies are exempt where Angolan companies get the same treatment in their home state.

**General regime:** tax based on declaration and financial statements. **Simplified regime:** taxpayers in the VAT non-subject regime. The turnover limit (old version: Kz 25,000,000) is unverified. Investment income goes to [IAC, see cross-border](ao-cross-border.md).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| General rate | 25% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |
| Agriculture, aquaculture, beekeeping, poultry, fishing, forestry, livestock, exclusively | 10% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |
| Banking, insurance, telecoms operators and Angolan oil companies | 35% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |
| Provisional payment, general regime | 2% of total sales in the first six months | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |
| Withholding on services | 6.5% on payments for services, credited against final tax (old version) | 2026 | unverified: no official text opened for the rate under the II code |

## The base

Taxable profit from the return and financial statements under the code and the Plano Geral de Contabilidade. 2026 changes (Lei 14/25 art 22): farm and livestock community infrastructure costs (water, power, access roads) amortise over the 5 following years after AGT verification; mobile financial service platforms amortise over up to 8 years with justification. Simplified taxpayers filing electronically deduct 10% of software, licence and accountant costs. Records are kept 5 years.

## Deadlines and filing

| Obligation | 2026 date | Source |
|---|---|---|
| Withholding on services paid last month | 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Simplified with accounts: Modelo 1 and final tax (electronic row) | 27 Feb | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Simplified with accounts: Modelo 1 and final tax (presented row) | 30 Apr | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Simplified without accounts: simplified return or register, final tax | 30 Apr | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| General regime: Modelo 1 and final tax | 29 May | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Provisional payment | 31 Aug | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Move from simplified to general regime by request | 27 Feb | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Cessation | General 60 days, simplified 30 days | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial |

Electronic filing is compulsory for general and simplified regimes; AGT staff assist those without the means (Lei 14/25 art 22(1)).

Steps: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; Menu de Servicos, Declaracoes, II, Entregar; fill the Modelo 1 with its annexes; press Validar; press Submeter a AGT and Confirmar; print the Declaracao and the Nota de Liquidacao for payment. Attach the income statement by nature, cash flow, balance sheet and trial balances before and after adjustments, signed by the responsible accountant. Provisional: Declaracoes, II, Entregar, Liquidacao Provisoria. Withholding: Declaracoes, II, Entregar, Mapa Retencao Fonte.

## Penalties and interest

Debts for periods to 31 October 2025: see the interest forgiveness in Lei 14/25 art 33, which ended with payment by end June 2026. Late filing and late payment percentages for Imposto Industrial are unverified.

## Cross-border points

Non-residents are taxed on income obtained in Angola. Dividends, interest and royalties: [cross-border](ao-cross-border.md). Related parties: [transfer pricing](ao-transfer-pricing.md).

## Two worked examples that recompute

**General company.** Profit Kz 10,000,000, first half sales Kz 40,000,000.

```oa-check
name: General regime with provisional payment
inputs:
  profit: 10000000
  h1_sales: 40000000
steps:
  - tax: profit * 0.25
  - provisional: h1_sales * 0.02
  - balance: tax - provisional
expected:
  tax: 2500000.0
  provisional: 800000.0
  balance: 1700000.0
```

**Decision: is the activity exclusively agricultural?** The 10% rate needs income exclusively from the listed activities. On the same profit the gap is Kz 1,500,000.

```oa-check
name: 10% or 25%
inputs:
  profit: 10000000
steps:
  - general: profit * 0.25
  - agri: profit * 0.10
  - gap: general - agri
expected:
  general: 2500000.0
  agri: 1000000.0
  gap: 1500000.0
```

## Ask the client first

- Sector: general, exclusively farming type, or bank, insurer, telecoms, oil?
- Regime, and whether VAT status is non-subject?
- Accounts kept?
- First half sales?
- Services paid to others in the year?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT, Imposto Industrial page (whole page read; undated, may lag the law) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-industrial | 2026-11-01 |
| AGT quick guide, II annual return (read in part: steps) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/imposto-industrial/novos-guias/guia-rapido-declaracao-anual-do-regime-geral-de-ii-sector-nao-financeiro.pdf | 2026-11-01 |
| AGT quick guide, II provisional assessment (read in part: menu step) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/imposto-industrial/novos-guias/guia-rapido-liquidacao-provisoria-de-ii.pdf | 2026-11-01 |
| AGT quick guide, II withholding map (read in part: menu step) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/imposto-industrial/novos-guias/guia-rapido-mapa-retencao-na-fonte-de-ii.pdf | 2026-11-01 |

Not yet confirmed: Simplified regime turnover threshold; the old general regime threshold Kz 25,000,000; the 6.5% services withholding article; loss carry-forward; penalties. The AGT page says provisional 2% is on total sales; the old version said sales not subject to withholding: check the code text.
