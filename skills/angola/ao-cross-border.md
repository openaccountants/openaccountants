---
name: ao-cross-border
description: "Angola cross-border tax for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about cross-border tax in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz."
jurisdiction: AO
category: cross-border
tax_year: 2026
last_updated: 2026-11-01
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Angola Cross-Border Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Payments between Angola and abroad: investment income under IAC, non-resident work under IRT, imported services under IVA. IAC is due from the income holder; the payer assesses Section B income, and assesses Section A where the holder has no Angolan residence or establishment.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Section A: interest on loans, credit, late payment | 15% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-aplicacao-de-capitais |
| Section B: dividends, royalties, bond interest, other, general | 10% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-aplicacao-de-capitais |
| Section B, listed on a regulated market, or compensation for suspended activity | 5% | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-aplicacao-de-capitais |
| IAC rate after Lei 14/25 | Art 41(3) revokes art 27(3) of the IAC Code, with the new rate set at 10%. Which income it reaches was not read in the code | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Dividend exemption | Angolan company holding 25% or more for over a year before distribution | 2026 | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-aplicacao-de-capitais |
| Reduced rates under incentive packages | Dividends and royalties 2.5% or 0%; interest 10% or 2.5% in certain cases (old version) | 2026 | unverified: no official text opened |

## The base

IAC on amounts paid or made available. Section A also has exempt trade credit interest and life policy loan interest.

## Deadlines and filing

| Obligation | 2026 date | Source |
|---|---|---|
| IAC, Sections A and B, operations of prior month | 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| IAC annual declaration | 30 Jan | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| CEOC on foreign exchange for services and transfers | Same monthly dates | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |

Tax residence certificate: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; Menu de Servicos, Cadastro de Contribuinte, Emitir Certificado. Third parties check it at Verificar Certificado, Residencia Fiscal.

## Penalties and interest

Unverified for IAC.

## Cross-border points

This section is the skill: see the rates and [VAT](ao-vat-gst.md) for imported services. The AGT site has a double tax agreement guide; the treaty list was not opened.

## Two worked examples that recompute

**Dividend abroad.**

```oa-check
name: Dividend at 10%
inputs:
  dividend: 1000000
steps:
  - tax: dividend * 0.10
  - net: dividend - tax
expected:
  tax: 100000.0
  net: 900000.0
```

**Decision: dividend or loan interest.** Same Kz 1,000,000 out.

```oa-check
name: Dividend or Section A interest
inputs:
  amount: 1000000
steps:
  - dividend_tax: amount * 0.10
  - interest_tax: amount * 0.15
  - gap: interest_tax - dividend_tax
expected:
  dividend_tax: 100000.0
  interest_tax: 150000.0
  gap: 50000.0
```

## Ask the client first

- Type of income?
- Recipient resident where, with what holding and period?
- Listed instrument?
- Treaty in force?
- Investment incentive?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| AGT, IAC page (whole page read; undated) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-aplicacao-de-capitais | 2026-11-01 |
| AGT quick guide, tax residence certificate (read in part: menu step) | https://portaldocontribuinte.minfin.gov.ao/pdfs/guia-rapido/acordos-dupla-tributacao/guia-rapido-adt-certificado-de-residencia-fiscal.pdf | 2026-11-01 |

Not yet confirmed: Whether section A interest stays at 15% after Lei 14/25 art 41(3); treaty list and rates; CEOC rate; incentive rates; non-resident service withholding.
