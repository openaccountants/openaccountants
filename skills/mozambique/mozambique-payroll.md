---
name: mozambique-payroll
description: Use this skill whenever asked about Mozambique payroll processing for employed persons. Trigger on phrases like "Mozambique payroll", "IRPS withholding", "IRPS Moçambique", "INSS deduction", "segurança social Moçambique", "PAYE Mozambique", "Form 19", "Modelo 19", "M/19", "tax withholding Mozambique", "salário líquido Moçambique", "net salary Mozambique", "employer INSS Mozambique", "salário mínimo Moçambique", "minimum wage Mozambique", "MAIBOR penalty", "gross to net Mozambique", "non-resident 20% Mozambique", "Lista Nominal", or any question about computing employee pay, income-tax withholding, or social-security contributions for Mozambique-based employees. This skill covers IRPS (income tax) monthly withholding by the employer, INSS social security (employee 3% + employer 4%), the monthly PAYE table, non-resident flat withholding, minimum wage by sector, and filing obligations to the Autoridade Tributária (AT) and INSS. ALWAYS read this skill before processing any Mozambique payroll.
version: 0.2
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Payroll v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). The governing 2026 texts could not be read: Boletim da Republica I Serie n.o 248 of 29 Dec 2025 (Leis 9/2025 ISPC, 10/2025 IVA, 11/2025 IRPS, 12/2025 IRPC) is listed on the AT site, at.gov.mz and inss.gov.mz refused both direct fetch and a real browser on 2026-11-01, and the gazette files have no archive copy. Every row below that rests on an older text says so.

## Who this applies to

Employers paying employees in Mozambique. Employers withhold on dependent-work income under a ministerial table (RCIRPS art. 31). Annual bands live in mozambique-income-tax.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---|---|---|
| IRPS payment by employer | by the end of the 20th of the following month | pre-2026 text | https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS |
| Income statement to workers | by 20 January | pre-2026 text | same |
| Modelo 20H | by March | pre-2026 text | same |
| INSS payment window | 20th to 10th, RSSO art. 14 | in force on read copy | https://web.archive.org/web/20260411210933/https://www.inss.gov.mz/wp-content/uploads/2024/04/Decreto-51-2017-de-9-de-Outubro-Regulamento-da-Seguranca-Social-Obrigatoria.pdf |
| Monthly IRPS withholding table | unverified, set by Diploma Ministerial, not opened | unverified | unverified |
| INSS rates | unverified, see mozambique-social-contributions | unverified | unverified |


## The base

Withholding is an advance on annual IRPS. The worker's Modelo 11 sets the family situation used for the table (AT FAQ). The old skill's RSM-sourced monthly floor of MZN 20,249.99 and band figures are not kept as fact; AT's 2014 booklet shows a MZN 20,250 salary with no final tax, under old deductions.

### Transaction / Payment Pattern Library (deterministic)
Classify bank-statement lines deterministically. Match case-insensitively; longest / most-specific pattern wins.

#### Salary credits (money arriving in an employee account)

**Salary credits table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARIO`, `ORDENADO`, `VENCIMENTO`, `PAGAMENTO SALARIO` | Net salary payment |
| `TRANSF.* [empresa]`, `CREDITO SALARIO` | Net salary payment |
| `SUBSIDIO REFEICAO`, `SUBS. ALIMENTACAO` | Meal subsidy (excluded from INSS base) |
| `13.* MES`, `SUBSIDIO NATAL` | Year-end / Christmas subsidy (irregular , outside INSS base) |
| `REEMBOLSO INSS`, `DEVOLUCAO INSS` | INSS refund/adjustment , not income |

#### Employer debits (money leaving the employer account)

**Employer debits table**

| Pattern | Classification |
| --- | --- |
| `AT`, `IRPS`, `RETENCAO IRPS`, `MODELO 19`, `M/19` | IRPS PAYE remitted to the AT (liability settlement) |
| `INSS`, `SEGURANCA SOCIAL`, `CONTRIBUICAO INSS` | INSS contribution (employer 4% + employee 3%) |
| `PAGAMENTO SALARIOS`, `FOLHA SALARIAL`, `PROCESSAMENTO` | Net wages disbursed to employees |
| `IRPC`, `IMPOSTO RENDIMENTO PESSOAS COLECTIVAS` | Corporate income tax , route to a corporate skill, not payroll |

### Tier 2 Catalogue (reviewer judgement required)
**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| --- | --- |
| Full monthly PAYE per-cell deduction matrix (income × dependents) | Published PDF rendered only partial cell values |
| Exact 25%/32% annual deduction constants | Published bracket edges do not tie under subtract method |
| Reconciliation of 0% monthly floor vs annual assessment for sub-floor earners | Monthly table and annual scale diverge |
| Residency determination under Lei 11/2025 | 180-day test removed; now facts-and-circumstances |
| INSS applicability to non-residents / expats | Depends on foreign-scheme coverage proof |
| Exact statutory penalty amounts (late M/19, late INSS) | Not cleanly extractable from primary law |
| Whether a given bonus is "regular" (INSS base) or "irregular" (excluded) | Fact-specific characterisation |
| 2026 INSS rate revision (if any) | Current authoritative figure is the 2024 INSS Note, still in force per  |

### Excel Working Paper Template
Suggested layout (one row per employee per month):

**Excel Working Paper Template columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Resident? (Y/N) | input (drives table choice) |
| C | Dependents (0-4+) | input (drives PAYE cell) |
| D | Gross monthly salary (MZN) | input (regular remuneration) |
| E | Employee INSS 3% | `=D*3%` |
| F | Employer INSS 4% | `=D*4%` |
| G | Below PAYE floor? | `=IF(D<=20249.99,TRUE,FALSE)` |
| H | Annual taxable (resident) | `=MAX(0,(D-E)*12)` |
| I | Annual IRPS (resident) | nested IF on H using  deductions (,/2,100/10,500/37,500/141,540) |
| J | Monthly IRPS (resident est.) | `=IF(B="N", D*20%, IF(G, 0, I/12))` |
| K | Employee deductions | `=E+J` |
| L | Net pay | `=D-K` |
| M | Total employer cost | `=D+F` |

- **Resident annual-IRPS formula (column I)** , =IF(H<=42000, H*0.10, IF(H<=168000, H*0.15-2100, IF(H<=504000, H*0.20-10500, IF(H<=1512000, H*0.25-37500, H*0.32-141540))))

> The column-J `IF(G,0,...)` 0%-floor shortcut and the resident annual-÷12 estimate are stand-ins for the **operative monthly PAYE matrix**, which must replace them once the full per-cell table is transcribed. **[RESEARCH GAP , reviewer to confirm.]**

### Bank Statement / Terminology Reading Guide
**Terminology reading guide**

| Portuguese term | English / meaning |
| --- | --- |
| Salário / Ordenado / Vencimento | Salary / wage |
| Folha salarial / Processamento de salários | Payroll / payroll run |
| Retenção na fonte | Withholding at source |
| IRPS | Personal income tax (Imposto sobre o Rendimento das Pessoas Singulares) |
| IRPC | Corporate income tax (Imposto sobre o Rendimento das Pessoas Colectivas) |
| INSS | National Social Security Institute |
| Segurança social | Social security |
| Modelo 19 / M/19 | IRPS PAYE form |
| Lista Nominal | Annual employee nominal roster |
| Subsídio de refeição / alimentação | Meal subsidy (excluded from INSS base) |
| Subsídio de férias | Holiday pay (irregular , excluded from INSS base) |
| Subsídio de Natal / 13.º mês | Christmas / 13th-month subsidy (irregular) |
| Dependentes | Dependents (drives PAYE cell) |
| Salário mínimo | Minimum wage |
| Autoridade Tributária (AT) | Tax authority |
| MAIBOR | Maputo Interbank Offered Rate (drives late-payment interest) |

### Onboarding Fallback
If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of folhas salariais and INSS/AT (M/19) receipts to back-solve the rates and PAYE cells actually applied.
2. **Unknown dependents** → default **0 dependents**, FLAG; confirm before first remittance.
3. **Unknown residency** → gather presence / economic-interest evidence under Lei 11/2025; do not assume the resident table without it.
4. **Unknown sector / min-wage band** → use the relevant 2025 sectoral figure only as a sanity check, never as the contractual wage; obtain the employee's contract.
5. **Expat employee** → confirm whether foreign-scheme coverage is proven before deciding INSS applicability; request the INSS exemption confirmation if claimed.
6. **Full monthly PAYE matrix needed** → obtain the official AT table /  matrix before computing 10%-20% band withholding precisely.

### Test Suite
Each test recomputes end-to-end. Resident IRPS via the annual table (÷12) per the estimation method; INSS employee 3% / employer 4%, no ceiling.

Agriculture min-wage earner. Salary 6,688/mo, resident, 0 deps. Expected: IRPS PAYE 0.00 (below floor); employee INSS 200.64; net 6,487.36; employer cost 6,955.52.

Financial-sector min-wage earner. Salary 19,043.61/mo, resident. Expected: IRPS PAYE 0.00 (below 20,250 floor); employee INSS 571.31; net 18,472.30.

Mid earner (20% band). Salary 30,000/mo, resident, 0 deps. Annual taxable 349,200.00; annual IRPS 59,340.00; monthly IRPS 4,945.00; net 24,155.00.

Higher earner (25% band). Salary 60,000/mo, resident. Annual taxable 698,400.00; annual IRPS 137,100.00; monthly IRPS 11,425.00; net 46,775.00.

Top-band earner (32%). Salary 150,000/mo, resident. Annual taxable 1,746,000.00; annual IRPS 417,180.00; monthly IRPS 34,765.00; net 110,735.00.

Non-resident flat 20%. MZ-source 60,000/mo, non-resident. WHT 12,000.00; net 48,000.00.

Employer cost. Salary 30,000/mo. Employer INSS 4% 1,200.00; total employer cost 31,200.00.

INSS total check. Employee 3% + employer 4% = 7% combined.

Bracket continuity (low bands). At 42,000 → IRPS 4,200.00; at 168,000 → IRPS 23,100.00 (subtract constants tie out).

Currency refusal. Salary stated in USD with no MZN conversion → REFUSE and request a Metical figure.

## Deadlines and filing

1. Collect Modelo 11.
2. Withhold under the table on each payment.
3. Pay IRPS by the 20th of the next month.
4. Pay INSS in the window; see mozambique-social-contributions.
5. By 20 January give each worker the income statement.
6. By March file Modelo 20H. Form numbers for the monthly IRPS guide and the Lista Nominal date in the old skill are unverified.

## Penalties and interest

Interest and fines: mozambique-income-tax and mozambique-social-contributions.

## Cross-border points

Payments to non-residents: see mozambique-income-tax.

## Two worked examples that recompute

**Annualised estimate, salary MZN 50,000.** Illustration only, not the table: with an employee share of 3% (unverified), annual income after it is 582,000, tax 109,800, or MZN 9,150 a month.

```oa-check
name: Annualised estimate
inputs:
  pay: 50000
steps:
  - net: (pay - pay * 0.03) * 12
  - tax: net * 0.25 - 35700
  - month: tax / 12
expected:
  month: 9150.00
```

**Employer cost at 4% (unverified).** MZN 52,000.

```oa-check
name: Employer cost
inputs:
  pay: 50000
steps:
  - cost: pay + pay * 0.04
expected:
  cost: 52000.00
```


## Ask the client first

- Monthly pay and components.
- Resident or not.
- Modelo 11 dependants.
- Sector.
- Foreign worker status.

## Sources

| Source | URL | Read on |
|---|---|---|
| AT, Perguntas Frequentes IRPS (archive copy of 5 Dec 2025; whole page read) | https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS | 2026-11-01 |
| AT, IRPS Regulation page, RCIRPS (archive copy of 31 Jan 2026; arts. 31 to 33 and filing articles read) | https://web.archive.org/web/20260131062421/http://www.at.gov.mz/por/Processos-Fiscais/Imposto-sobre-o-Rendimento-de-Pessoas-Singulares-IRPS | 2026-11-01 |
| Decreto 51/2017, RSSO, on inss.gov.mz (archive copy of 11 Apr 2026; arts. 14, 15, penalties and default interest read) | https://web.archive.org/web/20260411210933/https://www.inss.gov.mz/wp-content/uploads/2024/04/Decreto-51-2017-de-9-de-Outubro-Regulamento-da-Seguranca-Social-Obrigatoria.pdf | 2026-11-01 |
| AT, 100 Questoes sobre o CIRPS, 2014 (archive copy of 5 May 2025; questions on residence, withholding and deductions read) | https://web.archive.org/web/20250505220931/http://www.at.gov.mz/por/content/download/89600/780512/file/C%C3%B3digo%20do%20Imposto%20Sobre%20o%20Rendimento%20de%20Pessoas%20Singulares%20(CIRPS%20).pdf | 2026-11-01 |
| AT, Legislacao Fiscal list naming BR 248 supplements (archive copy of 20 Feb 2026; list read, the gazette files were not archived) | https://web.archive.org/web/20260220064207/https://www.at.gov.mz/por/Legislacao/Legislacao-Fiscal/Leis | 2026-11-01 |

Not yet confirmed: Monthly withholding table for each dependant count; Lei 11/2025 effects on payroll; form M/19; Lista Nominal 30 April; sector minimum wages from July 2025; INSS note 246/INSS/GAB-DG/432/2024; deductibility of the employee INSS share.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
