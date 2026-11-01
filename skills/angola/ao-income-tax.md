---
name: ao-income-tax
description: "Angola personal income tax (IRT) for tax year 2026, built from Lei 14/25 (the 2026 State Budget law), the tax codes and the AGT Portal do Contribuinte. Use when someone asks about personal income tax (IRT) in Angola: rates, who is liable, what is taxed, the deadlines on the AGT Calendario Fiscal 2026, the portal menu path for filing, and the penalties the opened sources state. Covers companies, individuals and employers as stated in the scope section. Figures that could not be read in an official source are marked unverified on their row and listed at the end. Trigger phrases: Angola tax, AGT, Portal do Contribuinte, kwanza, Kz."
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

# Angola Personal Income Tax (IRT) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals, resident or not, whose income comes from services provided directly or indirectly to persons or entities with domicile, seat, effective management or a permanent establishment in Angola (AGT IRT page). IRT is one of Angola's separate taxes: it covers work and self-employment, not rent or investment income.

- **Group A:** employees, public servants, members of company bodies.
- **Group B:** self-employed people in the professions list annexed to the code.
- **Group C:** industrial and commercial activities presumed by the minimum profits table (Tabela dos Lucros Minimos).

Exempt: foreign diplomatic staff with reciprocity; foreign staff of international organisations and, with AGT's prior written recognition, of NGOs; people with 50% or greater disability and war wounded; registered veterans. Payroll mechanics are in [Payroll social](ao-payroll-social.md).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Monthly band 1: above Kz 0 to 150,000 | Exempt | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 2: above Kz 150,000 to 200,000 | Kz 12,500 fixed + 16% of excess over 150,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 3: above Kz 200,000 to 300,000 | Kz 31,250 fixed + 18% of excess over 200,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 4: above Kz 300,000 to 500,000 | Kz 49,250 fixed + 19% of excess over 300,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 5: above Kz 500,000 to 1,000,000 | Kz 87,250 fixed + 20% of excess over 500,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 6: above Kz 1,000,000 to 1,500,000 | Kz 187,250 fixed + 21% of excess over 1,000,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 7: above Kz 1,500,000 to 2,000,000 | Kz 292,250 fixed + 22% of excess over 1,500,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 8: above Kz 2,000,000 to 2,500,000 | Kz 402,250 fixed + 23% of excess over 2,000,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 9: above Kz 2,500,000 to 5,000,000 | Kz 517,250 fixed + 24% of excess over 2,500,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 10: above Kz 5,000,000 to 10,000,000 | Kz 1,117,250 fixed + 24.5% of excess over 5,000,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Monthly band 11: above Kz 10,000,000 with no ceiling | Kz 2,342,250 fixed + 25% of excess over 10,000,000 | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Group B and C, income subject to withholding | 6.5%. Lei 28/20 art 16(2) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw4x/mjm3/~edisp/minfin1237855.pdf |
| Group B and C, income not subject to withholding | 25%. Lei 28/20 art 16(3) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw4x/mjm3/~edisp/minfin1237855.pdf |
| Group C, FY2025 turnover Kz 10,000,000 or less | 6.5% on sales and services not subject to withholding. Lei 14/25 art 21(1) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Group C agriculture, forestry, livestock, fishing above that turnover | 10%. Lei 14/25 art 21(4) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf |
| Self-billing withholding (auto-facturacao) | 2% by Group B payers or 6.5% by Group C payers as the code words it, non-final, on the whole self-invoice, paid within 5 days. Lei 28/20 art 10(4) | 2026 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw4x/mjm3/~edisp/minfin1237855.pdf |

The Annex I table is reproduced as published. The fixed amounts jump at band edges: Kz 200,000 gives Kz 20,500, Kz 200,001 gives Kz 31,250.18. Do not smooth them.

## The base

- **Group A:** all pay in money or kind, less compulsory social security contributions and items not subject or exempt.
- **Group B:** paid by someone with accounts: the value of the service. Paid by someone without accounts: worked out by the taxpayer. With organised accounts, the Imposto Industrial general regime rules apply. With simplified accounts or a purchase and sales register, the taxpayer deducts up to 30% of costs incurred. With none of these, no costs are deducted (Lei 28/20 art 8).
- **Group C:** the minimum profits table figure. With organised accounts, regardless of turnover, the Imposto Industrial general regime rules apply (Lei 14/25 art 21(2)). The rule that moved Group C to actual sales at 4 times the table maximum (CIRT art 9(2)) is suspended by Lei 14/25 art 41(2).
- **Below the charge:** INSS benefits, family allowance up to 5% of base pay, food and transport allowances up to Kz 30,000 a month each, documented travel reimbursement (AGT IRT page).

## Deadlines and filing

| Obligation | 2026 date | Source |
|---|---|---|
| Group A: payroll map and tax withheld | Monthly: 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 31 Dec | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Groups B and C: tax withheld by the payer | Same monthly dates | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Payers: annual Modelo 2 for Groups A, B, C | 27 Feb | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Group B: tax on income not subject to withholding | 27 Feb | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Group B: Modelo 1 | 31 Mar | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Group C: tax not subject to withholding, and annual return | 31 Mar | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |
| Self-billing withholding | 5 days from invoice or income | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf |

Portal steps: log in at https://portaldocontribuinte.minfin.gov.ao with the NIF as user ID and the password, then select the taxpayer account; go to Menu de Servicos, Declaracoes, IRT, Entregar, and choose the declaration. Complete, press Validar, then Submeter. Employees with only employment income have tax withheld by the employer; a personal filing duty for them is on the unconfirmed list.

## Penalties and interest

Failing to hand over withheld IRT, or handing over less than was deducted: a fine equal to the tax missing, plus criminal proceedings where a crime is presumed (Lei 14/25 art 21(5), https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf). Debts for periods to 31 October 2025 had interest forgiven if tax and fine were paid by the end of June 2026; regimes of special taxation, final court decisions and FY2025 obligations falling due in 2026 are excluded (art 33). Group C: missing the art 9 duty adds a fine of 25% of the tax on the minimum profits table (Lei 28/20 art 9(3)).

## Cross-border points

Non-residents are within IRT on income from services to Angolan payers. Crew of vessels or aircraft of Angolan-based companies, and managers and directors of Angolan companies, always have Angolan-source income. Treaties: see [cross-border](ao-cross-border.md).

## Two worked examples that recompute

**Employee.** Taxable pay after social security Kz 388,000: band 4.

```oa-check
name: Group A, taxable Kz 388,000
inputs:
  pay: 388000
steps:
  - tax: 49250 + (pay - 300000) * 0.19
expected:
  tax: 65970.0
```

**Decision: payer with accounts or without.** Fee Kz 1,000,000 and costs Kz 400,000. Withheld at 6.5% on the service value; if not withheld, 25% after deducting 30% of costs, for a taxpayer with simplified accounts or a register. Withholding costs Kz 155,000 less here.

```oa-check
name: Group B fee, withheld or not
inputs:
  fee: 1000000
  costs: 400000
steps:
  - withheld: fee * 0.065
  - not_withheld: (fee - costs * 0.30) * 0.25
  - gap: not_withheld - withheld
expected:
  withheld: 65000.0
  not_withheld: 220000.0
  gap: 155000.0
```

## Ask the client first

- Which group: employee, listed profession or trader?
- Is the payer an entity with accounts or simplified accounts?
- Does the taxpayer keep accounts, simplified accounts or a register?
- FY2025 turnover (Group C)?
- Monthly pay broken into base, allowances and social security?
- Any exemption status?

## Sources

| Source | URL | Read on |
|---|---|---|
| Lei 14/25 (OGE 2026), Diario da Republica I Serie 244, 30 Dec 2025: arts 21 to 23, 33, 35, 41, 43, Anexo I | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw41/mje2/~edisp/minfin5216784.pdf | 2026-11-01 |
| AGT, Calendario Fiscal 2026, Regime Geral page (read in part: image of Regime Geral page) | https://portaldocontribuinte.minfin.gov.ao/pdfs/CALENDARIO_FISCAL_2026.pdf | 2026-11-01 |
| Lei 28/20, CIRT amendments: arts 9, 10, 16 | https://www.ucm.minfin.gov.ao/cs/groups/public/documents/document/aw4x/mjm3/~edisp/minfin1237855.pdf | 2026-11-01 |
| Lei 18/14, CIRT: art 9 only | https://portal.inss.gov.ao/wp-content/uploads/2021/10/Lei_18_14.pdf | 2026-11-01 |
| AGT, IRT page (whole page read; undated) | https://portaldocontribuinte.minfin.gov.ao/impostos-e-taxas/imposto-sobre-rendimentos-do-trabalho | 2026-11-01 |

Not yet confirmed: Whether employees must ever file a personal return (old version: not required); the minimum profits table for 2026; the 2021 Group C changes after Lei 28/20 apart from those in Lei 14/25; the portal's undated text still shows the old Kz 100,000 domestic and farm worker limit.
