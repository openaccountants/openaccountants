---
name: mozambique-income-tax
description: Use this skill whenever asked about Mozambique personal income tax (IRPS) for employees, self-employed individuals, and small businesses. Trigger on phrases like "how much IRPS do I pay", "Modelo 10", "income tax return Mozambique", "IRPS rates", "PAYE Mozambique", "INSS contributions", "ISPC simplified regime", "first category income", "second category income", "imposto sobre o rendimento", "rendimento colectável", "self-employed tax Mozambique", "pagamentos por conta", or any question about filing or computing IRPS for a resident or non-resident individual. Also trigger when preparing or reviewing a Modelo 10 return, computing INSS payroll deductions, applying the progressive IRPS scale, or advising on the 2026 Law 11/2025 reform. This skill covers IRPS rate brackets, income categories, personal/dependent deductions, INSS social security, ISPC, sector minimum wages, filing deadlines, penalties, and the Law 11/2025 reform. ALWAYS read this skill before touching any Mozambique income tax or payroll work.
version: 0.2
jurisdiction: MZ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Personal Income Tax (IRPS) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). The governing 2026 texts could not be read: Boletim da Republica I Serie n.o 248 of 29 Dec 2025 (Leis 9/2025 ISPC, 10/2025 IVA, 11/2025 IRPS, 12/2025 IRPC) is listed on the AT site, at.gov.mz and inss.gov.mz refused both direct fetch and a real browser on 2026-11-01, and the gazette files have no archive copy. Every row below that rests on an older text says so.

## Who this applies to

Individuals with income taxed under the Codigo do IRPS (Lei 33/2007, amended by Lei 11/2025 from 1 Jan 2026): employees (first category), business and professional income (second category) and other categories. Resident status decides worldwide or Mozambique-source taxation. The pre-2026 180-day test in CIRPS art. 21 is the one AT's archived page states; it does not apply to 2026 if the reported repeal holds, so confirm residence before computing. Out of scope: companies (IRPC), megaprojects and capital gains.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---|---|---|
| IRPS band to MZN 42,000 | 10%, parcela a abater 0 | 2026, band table read on pre-2026 AT page; Lei 11/2025 not read | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS |
| IRPS band MZN 42,001 to 168,000 | 15%, parcela a abater 2,100 | 2026, band table read on pre-2026 AT page; Lei 11/2025 not read | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS |
| IRPS band MZN 168,001 to 504,000 | 20%, parcela a abater 10,500 | 2026, band table read on pre-2026 AT page; Lei 11/2025 not read | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS |
| IRPS band MZN 504,001 to 1,512,000 | 25%, parcela a abater 35,700 | 2026, band table read on pre-2026 AT page; Lei 11/2025 not read | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS |
| IRPS band over MZN 1,512,000 | 32%, parcela a abater 141,540 | 2026, band table read on pre-2026 AT page; Lei 11/2025 not read | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS |
| Withholding on payments to non-residents, professional income and isolated acts | 20% (CIRPS art. 57 as described by AT) | pre-2026 text | https://web.archive.org/web/20250505220931/http://www.at.gov.mz/por/content/download/89600/780512/file/C%C3%B3digo%20do%20Imposto%20Sobre%20o%20Rendimento%20de%20Pessoas%20Singulares%20(CIRPS%20).pdf |
| Withholding by entities with organised accounts on capital income and independent work | 20% (RCIRPS art. 32) | pre-2026 text | https://web.archive.org/web/20260131062421/http://www.at.gov.mz/por/Processos-Fiscais/Imposto-sobre-o-Rendimento-de-Pessoas-Singulares-IRPS |
| Rental income | 20% on gross, less 30% maintenance allowance (CIRPS art. 65) | pre-2026 text | https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS |
| Minimum for collection or refund | MZN 500 (Lei 20/2013, art. 62) | pre-2026 text | https://web.archive.org/web/20250505220931/http://www.at.gov.mz/por/content/download/89600/780512/file/C%C3%B3digo%20do%20Imposto%20Sobre%20o%20Rendimento%20de%20Pessoas%20Singulares%20(CIRPS%20).pdf |


## The base

Tax = taxable income x band rate, less parcela a abater, then less deductions from the tax and credits (CIRPS arts. 54, 59, 61 as described by AT). AT's table gives 35,700 for the 25% band; the earlier skill's 37,500 was wrong, and 35,700 makes the bands continuous (https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS).

Second-category income before 2026: organised accounts above MZN 2,500,000 turnover; below that, coefficients of 0.2 on sales of goods and on accommodation, restaurants and drinks, and 0.3 on other income (https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS). The 2026 position is unconfirmed; see Sources. Dismissal compensation due under the law with just cause is not taxed (CIRPS art. 6(d), same page).

### Transaction Pattern Library
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

Deterministic pre-classifier. Match by case-insensitive substring on the counterparty/description as it appears on the bank statement (Portuguese terms common in MZ). Most specific match wins. If none match, fall through to the rates and base above. Terms are in Portuguese as they appear in Mozambican statements.

#### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| SALÁRIO, ORDENADO, VENCIMENTO, REMUNERAÇÃO | 1st category (employment) | PAYE income | Subject to monthly withholding |
| SUBSÍDIO (regular) | 1st category | Employment income | Regular subsidies in IRPS base; meal subsidy excluded from INSS base |
| HONORÁRIOS, PRESTAÇÃO DE SERVIÇOS, FACTURA, RECIBO | 2nd category (business/professional) | Self-employment income | Organized accounting required |
| COMISSÃO, COMISSÕES | 2nd category | Commission income | E-money agent commissions: reported 2026 change, unread |
| RENDA RECEBIDA, ARRENDAMENTO | Property/rental income | See Rates table | Withholding rate pre-2026 |
| JUROS RECEBIDOS, JUROS | Investment income | Check 2026 treatment | Interest income |
| DIVIDENDOS | Investment income | Check 2026 treatment | Dividend income |
| REEMBOLSO IMPOSTO, RESTITUIÇÃO AT | EXCLUDE | Not income | Tax refund from prior year |

#### 3.2 Expense Patterns (Debits) -- 2nd Category, Fully Deductible

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

#### 3.3 Expense Patterns (Debits) -- Mixed Use (Apportion, Tier 2)

**3.3 Expense Patterns (Debits) -- Mixed Use (Apportion, Tier 2)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EDM, ELECTRICIDADE DE MOÇAMBIQUE | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| ÁGUA, FIPAG | Water | T2 if home office | Apportion |
| TMCEL, VODACOM, MOVITEL | Phone/telecoms | T2 | Business-use portion only; default 0% if mixed |
| COMBUSTÍVEL, GASOLINA, GASÓLEO, GALP, PUMA, TOTAL | Vehicle fuel | T2 | Business % only; requires mileage log |

#### 3.4 Expense Patterns (Debits) -- NOT Deductible

**3.4 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMOÇO, JANTAR, ENTRETENIMENTO | Entertainment | NOT deductible | Personal/entertainment |
| SUPERMERCADO, SHOPRITE, GROCERIES, PESSOAL | Personal expenses | NOT deductible | Private living costs |
| MULTA, COIMA, PENALIDADE | Fines/penalties | NOT deductible | Public policy |
| IRPS, PAGAMENTO IMPOSTO, AT PAGAMENTO | Tax payments | NOT deductible | Income tax cannot reduce income |
| LEVANTAMENTO, ATM (personal), RETIRADA | Drawings | NOT deductible | Not an expense |

#### 3.5 Statutory Items (Special Boxes, Not Box 2)

**3.5 Statutory Items (Special Boxes, Not Box 2)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, SEGURANÇA SOCIAL | INSS contribution | Employer remits both shares; rates unverified |
| PAGAMENTO POR CONTA, PPC | Advance payment | Credit against final IRPS, not an expense |
| TRANSFERÊNCIA INTERNA, CONTA PRÓPRIA | EXCLUDE | Own-account transfer |
| EMPRÉSTIMO, REEMBOLSO EMPRÉSTIMO | EXCLUDE | Loan principal movement |

#### 3.6 Mozambican Banks -- Statement Format Reference

**3.6 Mozambican Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BCI (Banco Comercial e de Investimentos) | TRANSFERÊNCIA, DÉBITO DIRECTO, LEVANTAMENTO | PDF/CSV; date DD/MM/YYYY |
| Millennium BIM | TRF, DD, PAGAMENTO, COMPRA POS | PDF/CSV; merchant in description |
| Standard Bank Moçambique | TRANSFER, DEBIT ORDER, POS | PDF; English/Portuguese mix |
| Absa Bank Moçambique | TRANSFER, DEBIT ORDER, FEE | PDF/CSV |
| Banco Único / Nedbank | TRANSFERÊNCIA, ENCARGOS | PDF |

### Tier 2 Catalogue (Reviewer Judgement Required)
#### 6.1 Home Office Apportionment (2nd category)

- **Home office apportionment** , Apportion electricity (EDM), water (FIPAG), internet by business-use proportion of the home. Must be a genuinely dedicated workspace. Conservative default: 0% until reviewer confirms arrangement.

#### 6.2 Vehicle Business Use (2nd category)

- **Vehicle business use** , Only the business-use percentage of fuel and running costs is deductible; mileage log required. Conservative default: 0% until log provided.

#### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** , Business portion only (TMCEL / Vodacom / Movitel). Conservative default: 0% until business percentage confirmed.

#### 6.4 INSS Payment Deadline Conflict

RSSO art. 14 sets the window: 20th of the reference month to the 10th of the next. Use the 10th. See mozambique-social-contributions.

#### 6.5 ISPC vs Organized Accounting (2026 transition)

- **ISPC vs organized accounting** , Secondary commentary reports that Law 11/2025 ends the simplified and exemption regimes for IRPS; the law was not read. Flag for reviewer: confirm the taxpayer's current regime status against AT before applying ISPC for any 2026 period.

#### 6.6 Residency Reclassification (2026)

- **Residency reclassification** , Secondary commentary reports a new residence test under Law 11/2025; the law was not read. Flag for reviewer: confirm residency under the new test for any 2026 computation.

#### 6.7 Survival of Personal/Dependent Deductions (2026)

Whether the MZN 1,800 personal deduction and dependent deductions survive Law 11/2025 is not confirmed. Flag for reviewer before relying on them for 2026.

### Excel Working Paper Template
> Kept from the old skill. Any rate, floor, base rule or reform point in this section is unverified until the texts under "Not yet confirmed:" are read. Do not apply it as a current figure.

```
MOZAMBIQUE IRPS -- WORKING PAPER (MZN)
Tax Year: 2026
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
  Non-resident: tax = C × 20% (pre-2026 text)
  D1. Gross IRPS                                    ___________

E. COLLECTION DEDUCTIONS (resident only)
  E1. Personal deduction (amount unverified)       ___________
  E2. Dependent deduction (per table)              ___________
  E3. Double-taxation relief credit                ___________
  E4. TOTAL collection deductions                  ___________

F. IRPS PAYABLE (D1 - E4, not below 0)            ___________
  F1. Less: PAYE withheld / pagamentos por conta   ___________
  F2. IRPS due / refund                            ___________

G. INSS (employment)
  G1. Employee share (rate unverified)             ___________
  G2. Employer share (rate unverified)             ___________
  G3. Total remitted by employer                   ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Income category confirmed?
  [ ] Dependent count confirmed?
  [ ] Home office / vehicle / telecoms % confirmed?
  [ ] ISPC/exemption regime status confirmed for 2026?
  [ ] Personal/dependent deductions confirmed for the tax year?
  [ ] Entertainment / personal items excluded?
  [ ] Meal subsidy excluded from INSS base?
```

### Bank Statement Reading Guide
#### Mozambican Bank Statement Formats

**Mozambican Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BCI | PDF, CSV | Data, Descrição, Débito, Crédito, Saldo | Most common; Portuguese descriptions |
| Millennium BIM | PDF, CSV | Data Valor, Descrição, Montante, Saldo | POS shows merchant |
| Standard Bank Moçambique | PDF | Date, Description, Amount, Balance | English/Portuguese mix |
| Absa Bank Moçambique | PDF, CSV | Date, Narrative, Amount, Balance |  |
| Banco Único / Nedbank | PDF | Data, Movimento, Valor, Saldo |  |

#### Key Mozambican / Portuguese Banking Terms

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

### Onboarding Fallback
If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library above.
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply the conservative defaults in the Tier 2 catalogue.
4. Generate the working paper above with clear flags.
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

## Deadlines and filing

1. Employers: Modelo 11 records the worker's family situation; withhold monthly and pay by the end of the 20th of the following month.
2. Employers: give each worker the income statement by 20 January; file Modelo 20H by March.
3. Individual: complete Modelo 10 on e-Declaracao (https://edeclaracao.at.gov.mz/), with proof of income and withholding. From January to 31 March if only first-category income; to 30 April otherwise (RCIRPS art. 44).
4. Pay by 31 May of the following year.
5. Second-category taxpayers: three equal advance payments by 20 June, September and November, totalling 80% of the prior-year tax share (CIRPS art. 66, RCIRPS art. 33).

All from AT's page, pre-2026: https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS. Box-level steps for Modelo 10 are not on an opened official page.

## Penalties and interest

Late payment bears juros de mora from the due date and taxpayer-caused under-assessment bears juros compensatorios. The percentages and fixed fines were not read; do not state them. Source pre-2026: https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS

## Cross-border points

Non-residents are taxed only on Mozambique-source income (AT booklet: https://web.archive.org/web/20250505220931/http://www.at.gov.mz/por/content/download/89600/780512/file/C%C3%B3digo%20do%20Imposto%20Sobre%20o%20Rendimento%20de%20Pessoas%20Singulares%20(CIRPS%20).pdf). International double-taxation relief is a deduction from the tax. Treaty rates are out of scope.

## Two worked examples that recompute

**Resident, MZN 600,000.** 25% band: 150,000 less 35,700 is 114,300, before deductions from the tax.

```oa-check
name: Resident, income MZN 600,000
inputs:
  income: 600000
steps:
  - tax: income * 0.25 - 35700
expected:
  tax: 114300.00
```

**Decision: scale or flat 20%, income MZN 600,000.** Residence is a fact, not a choice, but it moves the tax by MZN 5,700: 114,300 on the scale against 120,000 flat, and deductions apply only on the scale.

```oa-check
name: Scale against flat 20 percent
inputs:
  income: 600000
steps:
  - scale: income * 0.25 - 35700
  - flat: income * 0.20
  - gap: flat - scale
expected:
  gap: 5700.00
```


## Ask the client first

- Residence for 2026, and which facts support it.
- Income categories and amounts.
- Dependants.
- For business income: turnover, accounts kept, past ISPC status.
- Tax withheld and advance payments made.
- Foreign income and foreign tax paid.

## Sources

| Source | URL | Read on |
|---|---|---|
| AT, Taxas IRPS (archive copy of 7 Dec 2025, pre-2026 page) | https://web.archive.org/web/20251207064302/https://www.at.gov.mz/por/Comercio-Internacional/Procedimento-Fiscais/Taxas-IRPS | 2026-11-01 |
| AT, Perguntas Frequentes IRPS (archive copy of 5 Dec 2025; whole page read) | https://web.archive.org/web/20251205212815/http://www.at.gov.mz/por/Perguntas-Frequentes2/IRPS | 2026-11-01 |
| AT, IRPS Regulation page, RCIRPS (archive copy of 31 Jan 2026; arts. 31 to 33 and filing articles read) | https://web.archive.org/web/20260131062421/http://www.at.gov.mz/por/Processos-Fiscais/Imposto-sobre-o-Rendimento-de-Pessoas-Singulares-IRPS | 2026-11-01 |
| AT, 100 Questoes sobre o CIRPS, 2014 (archive copy of 5 May 2025; questions on residence, withholding and deductions read) | https://web.archive.org/web/20250505220931/http://www.at.gov.mz/por/content/download/89600/780512/file/C%C3%B3digo%20do%20Imposto%20Sobre%20o%20Rendimento%20de%20Pessoas%20Singulares%20(CIRPS%20).pdf | 2026-11-01 |
| AT, Legislacao Fiscal list naming BR 248 supplements (archive copy of 20 Feb 2026; list read, the gazette files were not archived) | https://web.archive.org/web/20260220064207/https://www.at.gov.mz/por/Legislacao/Legislacao-Fiscal/Leis | 2026-11-01 |

Not yet confirmed: Law 11/2025 text, so these remain unchecked against it: the new residence test, abolition of the simplified regime, the end of the filing waiver for employees, 10% final withholding on digital services and e-money agent commissions, the capital gains regime (art. 54-A) and organised accounts for the second category, all reported only by secondary commentary; personal and dependent deductions (old skill 1,800 and 600/900/1,200/1,800; AT's 2014 booklet gives 1,500 'por exemplo'); rental, withholding and non-resident rates after the reform; juros de mora and RGIT fines; municipal personal tax amounts; sector minimum wages from July 2025 and any 2026 update.

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
