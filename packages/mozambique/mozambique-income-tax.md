---
name: mozambique-income-tax
description: Use this skill whenever asked about Mozambique personal income tax (IRPS) for employees, self-employed individuals, and small businesses. Trigger on phrases like "how much IRPS do I pay", "Modelo 10", "income tax return Mozambique", "IRPS rates", "PAYE Mozambique", "INSS contributions", "ISPC simplified regime", "first category income", "second category income", "imposto sobre o rendimento", "rendimento colectável", "self-employed tax Mozambique", "pagamentos por conta", or any question about filing or computing IRPS for a resident or non-resident individual. Also trigger when preparing or reviewing a Modelo 10 return, computing INSS payroll deductions, applying the progressive IRPS scale, or advising on the 2026 Law 11/2025 reform. This skill covers IRPS rate brackets, income categories, personal/dependent deductions, INSS social security, ISPC, sector minimum wages, filing deadlines, penalties, and the Law 11/2025 reform. ALWAYS read this skill before touching any Mozambique income tax or payroll work.
version: 0.1
jurisdiction: MZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Personal Income Tax (IRPS)

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Mozambique (República de Moçambique) |
| Tax | IRPS -- Imposto sobre o Rendimento das Pessoas Singulares (personal income tax) |
| Currency | Metical (MZN / MT) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Código do IRPS (CIRPS); reformed by Law No. 11/2025 of 29 December 2025 (in force 1 Jan 2026) |
| Tax authority | Autoridade Tributária de Moçambique (AT) -- at.gov.mz |
| Social security | Instituto Nacional de Segurança Social (INSS) -- inss.gov.mz |
| Annual return form | Modelo 10 (declaração anual de rendimentos) |
| Filing portal | eDeclaração -- edeclaracao.at.gov.mz |
| Filing deadline | 31 March (employment-only) / 30 April (all other cases) of following year |
| Validated by | Pending -- requires sign-off by a Mozambican tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

Regime note. The 2025 tax year and earlier follow the long-standing CIRPS. Law No. 11/2025 (29 Dec 2025) enters into force 1 January 2026: it does not change the rate brackets but redefines residency, abolishes simplified/exemption regimes, ends the employee filing waiver, and adds digital-service withholding. See Section 11. Source: DLA Piper Africa / SAL & Caldeira — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code

### IRPS Rate Brackets (Resident -- 2025, continuing under 2026 reform)

**IRPS Rate Brackets (Resident -- 2025, continuing under 2026 reform)**  _(PwC Worldwide Tax Summaries — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income (last reviewed 04 Mar 2026); AT IRPS rate page — https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS (AT page returned a TLS error to the fetcher; PwC corroborates the same schedule).)_

| Annual taxable income (MZN) | Rate | Deductible amount (parcela a abater, MZN) | Cumulative tax at bracket top (MZN) |
| --- | --- | --- | --- |
| 0 -- 42,000 | 10% | 0 | 4,200 |
| 42,000 -- 168,000 | 15% | 2,100 | 23,100 |
| 168,000 -- 504,000 | 20% | 10,500 | 90,300 |
| 504,000 -- 1,512,000 | 25% | 37,500 | 340,500 |
| Over 1,512,000 | 32% | 141,540 | -- |

- **IRPS calculation mechanism** — tax = (annual income × bracket rate) − deductible amount (parcela a abater) for the bracket  _(PwC Worldwide Tax Summaries — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income)_

[RESEARCH GAP — reviewer to confirm] The published deductible amounts for the 25% bracket (MZN 37,500) and 32% bracket (MZN 141,540) do not produce perfectly continuous brackets (strict continuity would require 35,700 and 143,340 respectively). The published "parcela a abater" values are the figures AT applies and are used in this skill as authoritative; reviewer to verify against the official CIRPS schedule. The cumulative-tax column above is computed using the published deductible amounts.

- **Non-residents withholding rate** — 20% percent (flat withholding on Mozambique-source income (including employment))  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income)_

### INSS Social Security Contributions

**INSS Social Security Contributions**  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/other-taxes ; INSS — https://www.inss.gov.mz/duvidas/)_

| Party | Rate of monthly salary |
| --- | --- |
| Employee | 3% |
| Employer | 4% |
| **Total** | **7%** |

- **INSS base** — Base: all salaries, wages, regular bonuses and other regular income; meal subsidy excluded. No contribution ceiling identified from authoritative sources (state explicitly: no ceiling found). Employer withholds the employee's 3% and remits the full 7%.  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/other-taxes ; INSS — https://www.inss.gov.mz/duvidas/)_

Arithmetic check: employee 3% + employer 4% = total 7%. ✓

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP -- residency determines whole-scale vs 20% flat; do not compute |
| Unknown income category (1st vs 2nd) | STOP -- ask before classifying |
| Unknown whether item is "regular income" for INSS | Treat as INSIDE the INSS base (only meal subsidy is confirmed excluded) |
| Unknown number of dependents | 0 dependents (no dependent deduction) |
| Unknown ISPC vs organized accounting | Organized accounting (ISPC abolished from 2026 — see Section 5) |
| Unknown expense business-use % (2nd category) | 0% deduction |
| Unknown INSS payment deadline | Use the earlier INSS-site date (10th of following month) — see Section 6 |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- residency status (resident / non-resident), income category (1st = employment, 2nd = business/self-employment), and either a payroll summary (employment) or a bank statement for the full tax year (self-employment), plus number of dependents.

Recommended -- monthly PAYE withholding records, INSS contribution records, all invoices/receipts (2nd category), prior-year Modelo 10 or assessment.

Ideal -- complete income and expenditure account with organized accounting, advance-payment (pagamentos por conta) confirmations, double-taxation relief documentation.

Refusal if minimum is missing -- SOFT WARN. No income evidence at all = hard stop. Bank statement without invoices (2nd category) = proceed with reviewer warning: "This computation was produced from bank statement alone. The reviewer must verify that all deductions are supported by organized-accounting records."

### Refusal Catalogue

- **R-MZ-1 -- Residency unknown** — Residency determines whether the progressive 10%–32% scale or the flat 20% non-resident rate applies, and Law 11/2025 redefined residency from 2026. This skill cannot compute IRPS without residency status. Confirm before proceeding.
- **R-MZ-2 -- Companies / IRPC** — This skill covers individuals (IRPS) only. Corporate income tax (IRPC) is a separate regime. Escalate to a Mozambican tax professional.
- **R-MZ-3 -- Non-resident complex source rules** — Non-resident source-of-income and treaty questions require specialised analysis. Out of scope. Escalate to a Mozambican tax professional.
- **R-MZ-4 -- Capital gains** — Capital gains under the new autonomous regime (Art. 54-A, from 2026) require specialised analysis. Escalate to a Mozambican tax professional.
- **R-MZ-5 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to AT enforcement. Default interest (juros de mora) accrues immediately and statutory fines apply. Do not advise. Escalate immediately.
- **R-MZ-6 -- VAT (IVA) requested** — This skill covers IRPS only. Mozambique VAT (IVA) is a separate skill.
- **R-MZ-7 -- 2026 mechanics not yet regulated** — Law 11/2025 grants the government 180 days to issue implementing regulations. Some 2026 mechanics (e.g. survival of personal/dependent deductions) are pending. Flag and escalate for any 2026 computation that depends on unregulated detail.

## Section 3 -- Transaction Pattern Library

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears on the bank statement (Portuguese terms common in MZ). Most specific match wins. If none match, fall through to Tier 1 rules (Section 5). Terms are in Portuguese as they appear in Mozambican statements.

### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| SALÁRIO, ORDENADO, VENCIMENTO, REMUNERAÇÃO | 1st category (employment) | PAYE income | Subject to monthly PAYE 0%–32% |
| SUBSÍDIO (regular) | 1st category | Employment income | Regular subsidies in IRPS base; meal subsidy excluded from INSS base |
| HONORÁRIOS, PRESTAÇÃO DE SERVIÇOS, FACTURA, RECIBO | 2nd category (business/professional) | Self-employment income | Organized accounting required |
| COMISSÃO, COMISSÕES | 2nd category | Commission income | E-money agent commissions: 10% final WHT from 2026 (Section 11) |
| RENDA RECEBIDA, ARRENDAMENTO | Property/rental income | Same scale | Rental income on the IRPS scale |
| JUROS RECEBIDOS, JUROS | Investment income | Same scale | Interest income |
| DIVIDENDOS | Investment income | Same scale | Dividend income |
| REEMBOLSO IMPOSTO, RESTITUIÇÃO AT | EXCLUDE | Not income | Tax refund from prior year |

### 3.2 Expense Patterns (Debits) -- 2nd Category, Fully Deductible

**3.2 Expense Patterns (Debits) -- 2nd Category, Fully Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RENDA ESCRITÓRIO, ARRENDAMENTO COMERCIAL | Office rent | Deductible | Dedicated business premises |
| CONTABILISTA, CONTABILIDADE, TOC | Accountancy fees | Deductible | Organized accounting is mandatory (2nd category) |
| ADVOGADO, JURÍDICO, NOTÁRIO (business) | Legal fees | Deductible | Must be business-related |
| MATERIAL ESCRITÓRIO, PAPELARIA | Office supplies | Deductible |  |
| PUBLICIDADE, MARKETING, GOOGLE ADS, META | Marketing/advertising | Deductible |  |
| COMISSÃO BANCÁRIA, ENCARGOS, MANUTENÇÃO CONTA | Bank charges | Deductible | Business account only |
| FORMAÇÃO, CURSO, SEMINÁRIO | Training | Deductible | Must relate to current activity |
| SOFTWARE, ASSINATURA, MICROSOFT, GOOGLE WORKSPACE | Software subscription | Deductible | Recurring operating expense |

### 3.3 Expense Patterns (Debits) -- Mixed Use (Apportion, Tier 2)

**3.3 Expense Patterns (Debits) -- Mixed Use (Apportion, Tier 2)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EDM, ELECTRICIDADE DE MOÇAMBIQUE | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| ÁGUA, FIPAG | Water | T2 if home office | Apportion |
| TMCEL, VODACOM, MOVITEL | Phone/telecoms | T2 | Business-use portion only; default 0% if mixed |
| COMBUSTÍVEL, GASOLINA, GASÓLEO, GALP, PUMA, TOTAL | Vehicle fuel | T2 | Business % only; requires mileage log |

### 3.4 Expense Patterns (Debits) -- NOT Deductible

**3.4 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMOÇO, JANTAR, ENTRETENIMENTO | Entertainment | NOT deductible | Personal/entertainment |
| SUPERMERCADO, SHOPRITE, GROCERIES, PESSOAL | Personal expenses | NOT deductible | Private living costs |
| MULTA, COIMA, PENALIDADE | Fines/penalties | NOT deductible | Public policy |
| IRPS, PAGAMENTO IMPOSTO, AT PAGAMENTO | Tax payments | NOT deductible | Income tax cannot reduce income |
| LEVANTAMENTO, ATM (personal), RETIRADA | Drawings | NOT deductible | Not an expense |

### 3.5 Statutory Items (Special Boxes, Not Box 2)

**3.5 Statutory Items (Special Boxes, Not Box 2)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, SEGURANÇA SOCIAL | INSS contribution | Employer remits 7% (3% employee + 4% employer) |
| PAGAMENTO POR CONTA, PPC | Advance payment | Credit against final IRPS, not an expense |
| TRANSFERÊNCIA INTERNA, CONTA PRÓPRIA | EXCLUDE | Own-account transfer |
| EMPRÉSTIMO, REEMBOLSO EMPRÉSTIMO | EXCLUDE | Loan principal movement |

### 3.6 Mozambican Banks -- Statement Format Reference

**3.6 Mozambican Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BCI (Banco Comercial e de Investimentos) | TRANSFERÊNCIA, DÉBITO DIRECTO, LEVANTAMENTO | PDF/CSV; date DD/MM/YYYY |
| Millennium BIM | TRF, DD, PAGAMENTO, COMPRA POS | PDF/CSV; merchant in description |
| Standard Bank Moçambique | TRANSFER, DEBIT ORDER, POS | PDF; English/Portuguese mix |
| Absa Bank Moçambique | TRANSFER, DEBIT ORDER, FEE | PDF/CSV |
| Banco Único / Nedbank | TRANSFERÊNCIA, ENCARGOS | PDF |

## Section 4 -- Worked Examples

All amounts in MZN. IRPS computed as: annual tax = annual income × bracket rate − parcela a abater, then subtract personal/dependent collection deductions (Section 2/Section 5). Figures recomputed end-to-end.

### Example 1 -- Resident employee, mid-range salary

Input line:
`25/03/2025 ; BCI TRANSFERÊNCIA ; EMPRESA XYZ LDA ; SALÁRIO MARÇO ; +50,000.00 ; MZN`

Reasoning:
Monthly gross salary MZN 50,000 → annualised MZN 600,000 (1st category). Falls in the 504,000–1,512,000 (25%) bracket.
Gross IRPS = 600,000 × 25% − 37,500 = 150,000 − 37,500 = 112,500.
Less personal deduction (single/married taxpayer) MZN 1,800 → 112,500 − 1,800 = 110,700 annual IRPS.
INSS employee contribution = 3% × 50,000 = MZN 1,500/month.

Classification: 1st category. Annual gross IRPS MZN 112,500; after MZN 1,800 personal deduction, MZN 110,700. INSS employee MZN 1,500/month. (Personal deduction per PwC — https://taxsummaries.pwc.com/mozambique/individual/deductions.)

### Example 2 -- Resident employee, lower salary, two dependents

Input line:
`25/03/2025 ; MILLENNIUM BIM ; ORGANIZAÇÃO ABC ; ORDENADO ; +14,000.00 ; MZN`

Reasoning:
Gross salary MZN 14,000/month → annual MZN 168,000 (1st category). At the top of the 42,000–168,000 (15%) bracket.
Gross IRPS = 168,000 × 15% − 2,100 = 25,200 − 2,100 = 23,100.
Less personal deduction MZN 1,800; less 2-dependent deduction MZN 900 → 23,100 − 1,800 − 900 = 20,400 annual IRPS.
INSS employee = 3% × 14,000 = MZN 420/month.

Classification: 1st category. Annual IRPS MZN 20,400 after deductions. INSS employee MZN 420/month.

### Example 3 -- Non-resident consultant

Input line:
`10/04/2025 ; STANDARD BANK ; CLIENTE INTERNACIONAL ; HONORÁRIOS ; +200,000.00 ; MZN`

Reasoning:
Payment to a non-resident for Mozambique-source services. Non-residents are taxed at a flat 20% withholding on MZ-source income (PwC). The progressive scale and personal deductions do NOT apply.
IRPS withheld = 200,000 × 20% = 40,000.

Classification: Non-resident, flat 20%. IRPS MZN 40,000. No personal deductions.

### Example 4 -- Self-employed (2nd category), deductible expense

Input line:
`05/05/2025 ; BCI DÉBITO ; CONTABILISTA LDA ; HONORÁRIOS CONTABILIDADE ; -8,000.00 ; MZN`

Reasoning:
Accountancy fee for a 2nd-category (business/professional) taxpayer with organized accounting (mandatory). Fully deductible against business income.

Classification: 2nd category deductible expense MZN 8,000.

### Example 5 -- INSS contribution remittance

Input line:
`08/04/2025 ; MILLENNIUM BIM ; INSS ; CONTRIBUIÇÃO MARÇO ; -3,500.00 ; MZN`

Reasoning:
For a MZN 50,000 monthly payroll: total INSS = 7% × 50,000 = MZN 3,500 (employee 3% = 1,500 + employer 4% = 2,000). Employer remits the full 7%. Per the INSS site the remittance window runs from the 20th of the current month to the 10th of the following month; PwC states the 15th — flag the discrepancy (Section 6).

Classification: INSS remittance MZN 3,500 (1,500 employee + 2,000 employer). Statutory, not a Box-2 business expense.

### Example 6 -- Internal transfer (exclude)

Input line:
`15/05/2025 ; BCI TRANSFERÊNCIA ; CONTA PRÓPRIA - POUPANÇA ; ; -20,000.00 ; MZN`

Reasoning:
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

Classification: EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency Determines the Regime

- **Residency determines the regime** — Resident: progressive 10%–32% scale on worldwide income; personal/dependent deductions apply. Non-resident: flat 20% withholding on Mozambique-source income; no progressive scale, no personal deductions. From 2026 (Law 11/2025) residency no longer hinges on the >180-day test — see Section 11.  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income)_

### 5.2 The Progressive Scale (resident)

- **Progressive scale computation** — Annual tax = annual taxable income × bracket rate − parcela a abater (Section 1 table). For monthly PAYE, annualise the salary, compute annual tax, then divide as withholding (employer remits by the 20th of the following month — Section 7).  _(PwC; AT IRPS process page — https://www.at.gov.mz/por/Processos-Fiscais/Imposto-sobre-o-Rendimento-de-Pessoas-Singulares-IRPS)_

### 5.3 Income Categories

**5.3 Income Categories**  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income)_

| Category | Scope | Notes |
| --- | --- | --- |
| 1st (Primeira) | Dependent/employment income | Monthly PAYE 0%–32% |
| 2nd (Segunda) | Business and professional/self-employed income | Organized accounting mandatory (Law 11/2025) |
| Other | Capital/investment, rental, commissions, independent work | Same 10%–32% scale |

### 5.4 Personal / Dependent Collection Deductions

**5.4 Personal / Dependent Collection Deductions**  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/deductions)_

| Item | Annual deduction (MZN) |
| --- | --- |
| Each taxpayer (married or single) | 1,800 |
| 1 dependent | 600 |
| 2 dependents | 900 |
| 3 dependents | 1,200 |
| 4+ dependents | 1,800 |

- **Double-taxation relief credit** — Double-taxation relief credit is also available.  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/deductions)_

[RESEARCH GAP — reviewer to confirm] These are legacy values and may be revised by the pending Law 11/2025 regulations; not yet confirmed for 2026.

### 5.5 The Wholly-and-Exclusively Test (2nd category)

- **Wholly-and-exclusively test** — A business expense is deductible only if incurred for the business activity, supported by organized accounting. Mixed-use expenses must be apportioned reasonably and documented.

### 5.6 Non-Deductible Items

**5.6 Non-Deductible Items**

| Item | Reason |
| --- | --- |
| Entertainment / personal meals | Private |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| IRPS itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |

### 5.7 INSS (Social Security)

- **INSS rules** — Employee 3% + employer 4% = 7% of monthly salary (Section 1). Base excludes the meal subsidy. No ceiling identified. Employer withholds the 3% employee share and remits the full 7%. Worker registration: within 30 days of the start of the employment relationship. Foreign employees may apply for exemption from registration if contributing to a comparable scheme in their home country.  _(PwC — https://taxsummaries.pwc.com/mozambique/individual/other-taxes ; INSS — https://www.inss.gov.mz/duvidas/)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Apportionment (2nd category)

- **Home office apportionment** — Apportion electricity (EDM), water (FIPAG), internet by business-use proportion of the home. Must be a genuinely dedicated workspace. Conservative default: 0% until reviewer confirms arrangement.

### 6.2 Vehicle Business Use (2nd category)

- **Vehicle business use** — Only the business-use percentage of fuel and running costs is deductible; mileage log required. Conservative default: 0% until log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business portion only (TMCEL / Vodacom / Movitel). Conservative default: 0% until business percentage confirmed.

### 6.4 INSS Payment Deadline Conflict

[RESEARCH GAP — reviewer to confirm] The INSS official site states the remittance window runs from the 20th of the current month to the 10th of the following month; PwC states contributions are due by the 15th of the following month. The INSS site is the primary authority — default to the 10th and flag for the reviewer to resolve against INSS legislation. Sources: INSS — https://www.inss.gov.mz/duvidas/ ; PwC — https://taxsummaries.pwc.com/mozambique/individual/other-taxes

### 6.5 ISPC vs Organized Accounting (2026 transition)

- **ISPC vs organized accounting** — ISPC (simplified) and exemption regimes are abolished for IRPS from 2026 (Law 11/2025). Affected taxpayers move to organized accounting. Flag for reviewer: confirm the taxpayer's current regime status against AT before applying ISPC for any 2026 period.

### 6.6 Residency Reclassification (2026)

- **Residency reclassification** — Law 11/2025 may make foreign workers resident regardless of days present (Section 11). Flag for reviewer: confirm residency under the new test for any 2026 computation.

### 6.7 Survival of Personal/Dependent Deductions (2026)

Whether the MZN 1,800 personal deduction and dependent deductions survive Law 11/2025 is not confirmed. Flag for reviewer before relying on them for 2026.

## Section 7 -- Excel Working Paper Template

```
MOZAMBIQUE IRPS -- WORKING PAPER (MZN)
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Income category: 1st (employment) / 2nd (business) / Other
Number of dependents: ____

A. INCOME
  A1. Employment income (1st category, annual)   ___________
  A2. Business/professional income (2nd cat.)     ___________
  A3. Rental income                                ___________
  A4. Investment income (interest/dividends)       ___________
  A5. TOTAL annual income                          ___________

B. ALLOWABLE EXPENSES (2nd category only)
  B1. Office rent                                  ___________
  B2. Accountancy / legal fees                     ___________
  B3. Office supplies / software                    ___________
  B4. Marketing / advertising                       ___________
  B5. Bank charges                                  ___________
  B6. Training                                      ___________
  B7. Utilities (home office %)                     ___________
  B8. Vehicle (business %)                          ___________
  B9. Telecoms (business %)                         ___________
  B10. TOTAL allowable expenses                     ___________

C. TAXABLE INCOME (A5 - B10)                       ___________

D. IRPS COMPUTATION (pass to deterministic engine)
  Resident: tax = (C × bracket rate) − parcela a abater
  Non-resident: tax = C × 20%
  D1. Gross IRPS                                    ___________

E. COLLECTION DEDUCTIONS (resident only)
  E1. Personal deduction (MZN 1,800)               ___________
  E2. Dependent deduction (per table)              ___________
  E3. Double-taxation relief credit                ___________
  E4. TOTAL collection deductions                  ___________

F. IRPS PAYABLE (D1 - E4, not below 0)            ___________
  F1. Less: PAYE withheld / pagamentos por conta   ___________
  F2. IRPS due / refund                            ___________

G. INSS (employment)
  G1. Employee 3% of monthly salary                ___________
  G2. Employer 4% of monthly salary                ___________
  G3. Total 7% remitted by employer                ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Income category confirmed?
  [ ] Dependent count confirmed?
  [ ] Home office / vehicle / telecoms % confirmed?
  [ ] INSS payment deadline resolved (10th vs 15th)?
  [ ] ISPC/exemption regime status confirmed for 2026?
  [ ] Personal/dependent deductions confirmed for the tax year?
  [ ] Entertainment / personal items excluded?
  [ ] Meal subsidy excluded from INSS base?
```

## Section 8 -- Bank Statement Reading Guide

### Mozambican Bank Statement Formats

**Mozambican Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BCI | PDF, CSV | Data, Descrição, Débito, Crédito, Saldo | Most common; Portuguese descriptions |
| Millennium BIM | PDF, CSV | Data Valor, Descrição, Montante, Saldo | POS shows merchant |
| Standard Bank Moçambique | PDF | Date, Description, Amount, Balance | English/Portuguese mix |
| Absa Bank Moçambique | PDF, CSV | Date, Narrative, Amount, Balance |  |
| Banco Único / Nedbank | PDF | Data, Movimento, Valor, Saldo |  |

### Key Mozambican / Portuguese Banking Terms

**Key Mozambican / Portuguese Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERÊNCIA / TRF | Transfer | Check direction for income/expense |
| DÉBITO DIRECTO / DD | Direct debit | Regular expense (utility, subscription) |
| SALÁRIO / ORDENADO / VENCIMENTO | Salary | 1st category employment income |
| HONORÁRIOS | Professional fees | 2nd category income |
| LEVANTAMENTO | Cash withdrawal | Ask what cash was spent on |
| ENCARGOS / COMISSÃO BANCÁRIA | Bank charges | Deductible (2nd category) |
| JUROS | Interest | Interest income or bank charge |
| COMPRA POS | Card purchase | Expense -- check merchant |
| INSS / SEGURANÇA SOCIAL | Social security | Statutory contribution |
| SUBSÍDIO REFEIÇÃO | Meal subsidy | Excluded from INSS base |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions:

```
ONBOARDING QUESTIONS -- MOZAMBIQUE IRPS
1. Residency: resident or non-resident in Mozambique?
2. Income category: employment (1st), business/self-employed (2nd), or other?
3. Number of dependents?
4. For self-employed: do you keep organized accounting? Are you (or were you) under ISPC?
5. Home office: dedicated space? If yes, what % of the home?
6. Vehicle: used for business? What % is business use? Mileage log?
7. Phone/internet: what % is business use?
8. INSS: are you registered? Are contributions up to date?
9. Any foreign income / double-taxation relief to claim?
10. Any advance payments (pagamentos por conta) or PAYE already withheld?
```

## Section 10 -- Reference Material

### Key References

**Key References**

| Topic | Reference |
| --- | --- |
| IRPS rates | Código do IRPS; PwC — https://taxsummaries.pwc.com/mozambique/individual/taxes-on-personal-income |
| AT rate page | https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS (TLS error to fetcher) |
| Personal/dependent deductions | PwC — https://taxsummaries.pwc.com/mozambique/individual/deductions |
| INSS contributions & rules | PwC — https://taxsummaries.pwc.com/mozambique/individual/other-taxes ; INSS — https://www.inss.gov.mz/duvidas/ |
| Filing & administration | AT IRPS FAQ — https://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS ; PwC — https://taxsummaries.pwc.com/mozambique/individual/tax-administration |
| Law 11/2025 reform | DLA Piper — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code ; PwC PT Inforfisco — https://www.pwc.pt/pt/pwcinforfisco/flash/mocambique/mocambique-irps-alteracoes-cirps.html ; EY — https://www.ey.com/pt_mz/technical/tax-alerts/alteracoes-do-codigo-do-irps-em-mocambique ; Law text — https://www.lexlink.eu/conteudo/geral/mocambique/4123555/lei-no-112025/147/por-tema |

### Filing -- Forms & Deadlines (2025 regime)

**Filing -- Forms & Deadlines (2025 regime)**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year | PwC |
| Annual return | Modelo 10 (declaração anual de rendimentos) | AT IRPS process page |
| Filing — employment only | 1 Jan → **31 March** of following year | AT IRPS FAQ — https://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS |
| Filing — all other cases | 1 Jan → **30 April** of following year | AT IRPS FAQ |
| IRPS payment | **31 May** of following year | AT IRPS FAQ |
| Self-employed advance payments | 3 equal instalments: **20 June, 20 September, 20 November** | AT IRPS process page |
| Employer PAYE remittance | By the **20th** of the following month | PwC — https://taxsummaries.pwc.com/mozambique/individual/tax-administration |
| Online platform | eDeclaração — https://edeclaracao.at.gov.mz/ | AT |

### Penalties (IRPS)

**Penalties (IRPS)**  _(AT IRPS FAQ — https://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS)_

| Item | Detail |
| --- | --- |
| Late payment | Juros de mora (default interest) accrues immediately from the due date |
| Taxpayer-caused under-assessment | Juros compensatórios (compensatory interest) |
| Statutory interest rates / fixed fines (RGIT) | **[RESEARCH GAP — reviewer to confirm]** — exact juros de mora % and fixed fines under the Regime Geral das Infracções Tributárias were not obtainable from an authoritative fetched source; do not state numbers without verification |

### INSS Penalties

**INSS Penalties**

| Item | Detail | Source |
| --- | --- | --- |
| Non-payment / late submission | Fine of **1 to 3 minimum salaries × number of workers** on the declaration | INSS — https://www.inss.gov.mz/duvidas/ |
| Failure to register a worker | **1 to 5 minimum salaries** | INSS — https://www.inss.gov.mz/duvidas/ |

### Sector Minimum Wages (2025, effective 1 July 2025, retroactive)

Set by Ministerial Diplomas Nos. 87–94/2025 (approved 22 Sep 2025). There is no single national minimum — it is sector-based.

**Sector Minimum Wages table**  _(DLA Piper Africa / SAL & Caldeira — https://www.dlapiperafrica.com/pt/mozambique/insights/2025/Approval-of-New-Minimum-Wages-2025 ; Club of Mozambique — https://clubofmozambique.com/news/mozambique-minimum-wages-increase-2-9-to-9-depending-on-sector-with-retroactive-effect-from-1-july/)_

| Sector | 2025 monthly minimum (MZN) |
| --- | --- |
| Agriculture, livestock, hunting, forestry | 6,688.00 |
| Maritime/industrial/semi-industrial fishing | 6,726.88 |
| Kapenta fishing | 4,991.09 |
| Mineral extraction — large companies | 15,176.66 |
| Mineral extraction — medium enterprises | 8,008.00 |
| Mineral extraction — micro/small (incl. salt) | 6,538.44 |
| Manufacturing (excl. bread & cashew) | 10,147.50 |
| Bread manufacturing | 7,200.00 |
| Cashew industry | 6,653.21 |
| Electricity/gas/water — large companies | 12,275.00 |
| Electricity/gas/water — small/medium | 9,960.62 |
| Construction | 8,400.00 |
| Non-financial services | 10,310.00 |
| Hotels/tourism | 9,700.00 |
| Private security | 8,465.00 |
| Fuel retail | 9,739.00 |
| Banking & insurance | 19,043.61 |
| Microfinance & micro-insurance | 16,764.47 |

### Municipal Personal Tax (Imposto Pessoal Autárquico)

Small annual flat tax that varies by municipality (e.g., Maputo cited ~MZN 510 for 2024 per PwC). [RESEARCH GAP — reviewer to confirm] current-year value per municipality. Source: PwC.

### Test Suite

Input: Resident, annual employment income 600,000, single (no dependents).
Expected: 25% bracket → 600,000 × 25% − 37,500 = 150,000 − 37,500 = 112,500 gross IRPS; less personal deduction 1,800 = 110,700.

Input: Resident, annual 168,000, 2 dependents.
Expected: 15% bracket → 168,000 × 15% − 2,100 = 25,200 − 2,100 = 23,100; less 1,800 personal − 900 (2 dependents) = 20,400.

Input: Resident, annual 42,000, single.
Expected: 10% bracket → 42,000 × 10% − 0 = 4,200; less 1,800 = 2,400.

Input: Resident, annual 2,000,000, single.
Expected: 32% bracket → 2,000,000 × 32% − 141,540 = 640,000 − 141,540 = 498,460; less 1,800 = 496,660.

Input: Non-resident, 200,000.
Expected: 200,000 × 20% = 40,000. No personal deductions.

Input: Monthly salary 50,000.
Expected: Employee 3% = 1,500; employer 4% = 2,000; total 7% = 3,500 remitted by employer. (1,500 + 2,000 = 3,500. ✓)

Input: Salary 30,000 + meal subsidy 4,000.
Expected: INSS base = 30,000 (meal subsidy excluded). Employee 3% = 900; employer 4% = 1,200; total = 2,100.

## Section 11 -- Law No. 11/2025 (IRPS reform, in force 1 January 2026)

Key changes (verify final regulations, due within 180 days of the law):

1. Residency redefined. The >180-day physical-presence test is removed. Residency now turns on having one's main residence, main professional activity, or centre of economic interests in Mozambique; ship/aircraft crew of MZ entities; and MZ nationals on foreign assignment not fully taxed abroad. Effect: many foreign workers become resident regardless of days present.
2. Simplified & exemption regimes abolished for IRPS → affected taxpayers move to organized accounting (see ISPC, Section 5/Section 6).
3. Filing waiver removed for employees with PAYE-only income — from 2026 such employees must also file the Modelo 10.
4. Digital services / e-money agent commissions: 10% final (liberatory) withholding on income from digital services and electronic-money agent commissions (including by non-residents); broadened taxable base for digital services performed/used in Mozambique.
5. Capital gains: new autonomous regime (Art. 54-A) taxed on the 10%–32% scale.
6. Second-category taxpayers: must keep organized accounting.

Sources: DLA Piper Africa / SAL & Caldeira — https://www.dlapiperafrica.com/en/mozambique/insights/2026/Changes-to-the-Personal-Income-Tax-Code ; PwC PT Inforfisco — https://www.pwc.pt/pt/pwcinforfisco/flash/mocambique/mocambique-irps-alteracoes-cirps.html ; EY — https://www.ey.com/pt_mz/technical/tax-alerts/alteracoes-do-codigo-do-irps-em-mocambique ; Law text — https://www.lexlink.eu/conteudo/geral/mocambique/4123555/lei-no-112025/147/por-tema

## Section 12 -- Open Items (figures NOT confirmed from authoritative fetched sources)

[RESEARCH GAP — reviewer to confirm] each of the following before publishing a number:

1. ISPC threshold (MZN 2,500,000 turnover), 3% rate, and fixed amount (MZN 75,000) — commonly published but not reconfirmed from a fetched AT page this session (AT TLS error). Verify on the AT ISPC page — https://www.at.gov.mz/por/Processos-Fiscais/Imposto-Simplificado-para-Pequenos-Contribuintes-ISPC . Note ISPC is abolished for IRPS from 2026.
2. AT official IRPS rate/process pages could not be fetched directly (certificate error); bracket data corroborated by PwC — confirm against AT when accessible.
3. Exact IRPS penalty/interest rates (juros de mora %, fixed fines under RGIT) — not obtained; verify before publishing numbers.
4. INSS payment deadline conflict — INSS site says by the 10th of the following month; PwC says by the 15th. Resolve against INSS legislation.
5. Whether the MZN 1,800 personal deduction / dependent deductions survive Law 11/2025 — not confirmed for 2026.
6. Municipal personal tax (Imposto Pessoal Autárquico) — varies by municipality (Maputo ~MZN 510 for 2024 per PwC); confirm current-year value.

## PROHIBITIONS

- NEVER apply the progressive scale without confirming residency — non-residents pay a flat 20%
- NEVER apply personal/dependent deductions to a non-resident
- NEVER include the meal subsidy in the INSS contribution base
- NEVER state a total INSS rate other than 7% (3% employee + 4% employer)
- NEVER include IRPS itself, fines, drawings, or personal expenses as deductions
- NEVER apply the ISPC simplified regime to a 2026 period without confirming it survived Law 11/2025 (it is abolished)
- NEVER invent juros de mora / RGIT penalty rates — they are a RESEARCH GAP
- NEVER assume the >180-day residency test for 2026 — Law 11/2025 replaced it
- NEVER present tax calculations as definitive — always label as estimated and pending reviewer sign-off
- NEVER rely on the published parcela-a-abater continuity without the reviewer note in Section 1

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
