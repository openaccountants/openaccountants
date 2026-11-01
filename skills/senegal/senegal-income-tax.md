---
name: senegal-income-tax
description: "Use for Senegal personal income tax (IR/IRPP) for tax year 2026: bands, family reduction, 900,000 abatement, CGU, TRIMF, filing and penalties."
version: 0.2
jurisdiction: SN
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

# Senegal personal income tax

Everything here follows the CGI edition of January 2025. The 2026 finance law, Loi n. 2025-19, amends none of these articles.

## Who this applies to

Individuals with a tax home in Senegal are taxed on worldwide income; others on Senegal-source income, subject to treaties (CGI art. 48). A tax home means a permanent home or main stay, a non-incidental professional activity, or the centre of economic interests in Senegal. Companies, capital gains on property and non-resident planning: refer out.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Band 1 | 0% to XOF 630,000 | Taxable income rounded down to the thousand (art. 173) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Band 2 | 20%, 630,001 to 1,500,000 | Not per part | same |
| Band 3 | 30%, 1,500,001 to 4,000,000 | | same |
| Band 4 | 35%, 4,000,001 to 8,000,000 | | same |
| Band 5 | 37%, 8,000,001 to 13,500,000 | | same |
| Band 6 | 40%, 13,500,001 to 50,000,000 | | same |
| Band 7 | 43% above 50,000,000 | Tax never exceeds 43% of taxable income (art. 174) | same |
| Dividends withholding | 10% | Shares of companies liable to IS (art. 173.2) | same |
| Bond income | 13%; 6% | 6% for bonds issued in Senegal, term at least 5 years | same |
| Lots | 15% | | same |
| Other investment income, directors' fees, deposits | 16%; 8% | 8% for deposit and current accounts at the listed institutions | same |
| Bearer or registered cash bonds interest | 20% | Final | same |
| Securities gains via Senegal manager | 25% | Otherwise declared by the beneficiary | same |
| Employment abatement | 30%, cap 900,000 | Replaces pension contributions and job costs; not for pensions (art. 182) | same |
| Diplomatic posting abatement | 10%; 20% outside the CFA zone | State agents only (art. 182) | same |
| Foreign pension relief | 80% of the tax | Art. 180 | same |
| Service withholding | 5% | Invoice at least 25,000; suppliers not on real profit regimes (art. 200) | same |
| Rent withholding | 5% | Gross rent before tax (art. 201) | same |
| Private clinic practitioners | 10%, final | Non-employed medical staff (art. 212 ter) | same |
| CGU, services | 5%, minimum 30,000 | Individuals, turnover with tax at most 50,000,000 (arts. 135, 141) | same |
| CGU, traders and producers | 2%, minimum 25,000 | Same | same |
| CGF on rents | 1, 1.5 or 2 months of gross rent, minimum 30,000 | Bands to 12M, to 18M, above; gross rents up to 30M | https://www.dgid.sn/loi-reglement |
| TRIMF per year | 900; 3,600; 4,800; 12,000; 18,000; 36,000 | Gross income under 600k; under 1M; under 2M; under 7M; under 12M; 12M and over (art. 282) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |

Family reduction, applied to the tax (art. 174). This is not an income-splitting quotient.

| Parts | Rate | Minimum | Maximum | Source |
|---|---|---|---|---|
| 1 | 0% | 0 | 0 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| 1.5 | 10% | 100,000 | 300,000 | same |
| 2 | 15% | 200,000 | 650,000 | same |
| 2.5 | 20% | 300,000 | 1,100,000 | same |
| 3 | 25% | 400,000 | 1,650,000 | same |
| 3.5 | 30% | 500,000 | 2,030,000 | same |
| 4 | 35% | 600,000 | 2,490,000 | same |
| 4.5 | 40% | 700,000 | 2,755,000 | same |
| 5 | 45% | 800,000 | 3,180,000 | same |

Parts: single, divorced or widowed with no child 1; married no child 1.5; single or divorced with 1 child 1.5; married or widowed with 1 child 2; add 0.5 per child. Add 0.5 where only one spouse has taxable income (art. 174.3). Maximum 5. Non-residents: maximum 1.5 (art. 176). Single persons with no dependent child get 1.5 if a child died, on a 40% war or accident pension, or after adoption (art. 175). Dependent children: minors, disabled, or under 25 and studying (art. 177). The situation is taken at 1 January of the tax year, or of the income year if better (art. 178).

## The base

1. Start from gross pay plus benefits in kind. 2. Take the 30% abatement capped at 900,000. 3. Round down to the thousand and apply the bands. 4. Take the family reduction. 5. Cap at 43% of taxable income. TRIMF is separate.

CGU covers income tax on commercial profits, minimum tax, CEL, VAT, CFCE and drinks licence (art. 134). It excludes non-commercial professions, property sale, letting or management, and art. 51 persons (art. 136). Opt out by 31 January; the option is total and irrevocable (art. 138). Artisans get a 15% income reduction, as do simplified-regime taxpayers in an approved management centre, on the art. 172 terms.

Bank and payslip patterns for sorting records:

#### 1 Income Patterns (Credits)

**Income Patterns (Credits) Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, BULLETIN, VIREMENT SALAIRE, employer name | Employment income (IRPP base) | Gross before withholding; goes through the barème |
| HONORAIRES, PRESTATION, FACTURE, CONSULTANCE | Self-employment / BNC income | Business income - confirm CGU vs réel regime |
| LOYER, LOYER PERÇU, RENT RECEIVED | Rental income | See the base  |
| DIVIDENDE, DIVIDENDS | Investment income | Withheld at the art. 173 rate |
| INTÉRÊTS, INTERESTS | Investment income | Flag for reviewer |
| ORANGE MONEY, WAVE, FREE MONEY (business receipts) | Self-employment income | Mobile-money business receipts - match to invoices |
| STRIPE / PAYPAL / WISE PAYOUT | Self-employment income | Platform payout - match to underlying invoices |
| REMBOURSEMENT IMPÔT, TAX REFUND | EXCLUDE | Refund of prior-year tax, not income |

#### 2 Expense Patterns (Debits) - Deductible (business, before abattement) [self-employed réel only]

**Deductible Expense Patterns Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LOYER BUREAU, OFFICE RENT | Office rent | Deductible | Dedicated business premises |
| HONORAIRES COMPTABLE, EXPERT-COMPTABLE, AUDIT | Accountancy fees | Deductible |  |
| AVOCAT, NOTAIRE (business) | Legal fees | Deductible | Must be business-related |
| FOURNITURES, PAPETERIE | Office supplies | Deductible |  |
| PUBLICITÉ, GOOGLE ADS, META ADS, MARKETING | Advertising | Deductible |  |
| FRAIS BANCAIRES, COMMISSION BANCAIRE | Bank charges | Deductible | Business account only |
| INTERNET, ABONNEMENT (business) | Connectivity | Deductible | Business-use portion only |

#### 3 Expense Patterns (Debits) - Not Deductible

**Not Deductible Expense Patterns Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, REPAS, DÉJEUNER, RÉCEPTION | Entertainment / meals | Not deductible | Private / blocked |
| COURSES, SUPERMARCHÉ, AUCHAN, EXCLUSIVE | Personal | Not deductible | Private living costs |
| AMENDE, PÉNALITÉ, CONTRAVENTION | Fines/penalties | Not deductible | Public policy |
| IMPÔT, IRPP, PAIEMENT DGID | Tax payments | Not deductible | Income tax cannot reduce income |
| RETRAIT, PRÉLÈVEMENT PERSO, GAB | Drawings / cash | Not deductible | Ask what cash was used for |

#### 4 Statutory Withholdings & Exclusions

**Statutory Withholdings & Exclusions Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IPRES, RETRAITE, PENSION (employee share) | Covered by the 30% abatement (art. 182) | See above |
| CSS, SÉCURITÉ SOCIALE | Employer-only (employee 0%) - EXCLUDE from employee deduction | See above |
| TRIMF | Minimum personal tax withheld | See above |
| CFCE | Employer-only payroll tax - EXCLUDE from employee | See above |
| VIREMENT INTERNE, COMPTE PROPRE | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRÊT, PRÊT | EXCLUDE | Loan principal movement |

#### 5 Senegalese Banks / Payment Rails - Statement Reference

**Banks / Payment Rails Table**

| Institution | Common patterns | Notes |
| --- | --- | --- |
| CBAO (Attijariwafa) | VIREMENT, PRÉLÈVEMENT, COMMISSION | PDF; description holds counterparty |
| SGBS (Société Générale Sénégal) | VIR, PRLV, FRAIS | PDF/CSV |
| Ecobank Sénégal | TRANSFER, DD, CHARGE | PDF |
| BICIS / UBA / Bank of Africa | VIREMENT, CHÈQUE, AGIOS | PDF |
| Orange Money / Wave / Free Money | PAIEMENT, TRANSFERT, RETRAIT | Mobile money - separate from bank; business vs personal must be confirmed |


**Carried from the earlier version, not checked against the law.** Kept so no working rule is lost. Any figure here is unverified unless it also appears in the tables above; the tables win.

Required records. Minimum: bank statement or payslips for the full year, plus tax home, family situation and employment or self-employment status. Better: payroll summary (gross, IR and TRIMF withheld, IPRES and CSS), last year's assessment, cadre status. Ideal: income statement, invoices, asset register, benefits schedule, rental detail, CGU declaration. No income document at all: stop. Income document without records: proceed and warn the reviewer that parts, cadre status and every deduction still need support.

| Unknown | Default |
| -- | -- |
| Family situation | Stop: do not take the family reduction without marital status and children |
| Tax home | Stop until confirmed; non-residents go to review |
| Cadre status | IPRES general scheme only until confirmed |
| Business use of vehicle, phone, home | 0% until a documented share is given |
| Expense category | Not deductible |
| Benefit in kind value | Flag for reviewer; the art. 166 scale was not worked through |
| Turnover near the CGU limit | Confirm activity and regime before computing |

Refuse and refer:
- R-SN-1: family situation unknown. Ask for marital status and children before computing.
- R-SN-3: non-resident or dual-resident cases beyond the cross-border points above. Refer to a Senegalese expert-comptable.
- R-SN-4: companies and partnerships. They pay corporate tax; use sn-corporate-income-tax.
- R-SN-6: capital gains and property disposals. Refer.

Self-employed on the real regime: net business profit, income less wholly business expenses, feeds the bands. Non-commercial professions, property income and several employers stay outside CGU. Only the business share of phone, internet and premises counts. Never deductible: entertainment and personal meals, living costs, fines and penalties, IR itself, drawings.

Reviewer flags: cadre classification and ceiling base; each benefit in kind and any travel allowance exemption; home office share; CGU against real regime near the limit, and whether opting for real helps.

Rental income: the old version took a 30% standard deduction from gross rent. unverified: confirm against the CGI before use.

| unverified: benefit | Old notional value, FCFA a month (PwC, not official) |
| -- | -- |
| unverified: accommodation | 13,500 to 33,500 |
| unverified: domestic staff | 35,600 to 92,500 |
| unverified: utilities | 10,500 to 30,200 |
| unverified: company car | 26,000 to 77,500 |
| unverified: telephone | 67,000 |
| unverified: statutory travel allowance | Exempt up to 26,000 |

Payslip and bank terms:

### Key Senegalese / French payroll & banking terms

**Payroll & Banking Terms Table**

| Term | English | Classification hint |
| --- | --- | --- |
| SALAIRE BRUT | Gross salary | IRPP base (before deductions) |
| SALAIRE NET | Net salary | After tax + social withholdings |
| VIREMENT / VIR | Transfer | Check direction for income/expense |
| PRÉLÈVEMENT / PRLV | Direct debit | Regular expense |
| AGIOS / FRAIS / COMMISSION | Bank charges | Deductible (business account) |
| IPRES | Pension contribution | Not deducted; the abatement replaces it (art. 182) |
| CSS | Social security | Employer-only (employee 0%) |
| TRIMF | Minimum personal tax | Withheld; separate from barème |
| CFCE | Employer payroll tax | Employer-only (exclude from employee) |
| ABATTEMENT | Lump-sum deduction | 30%, capped 900,000 |
| LOYER | Rent | Income (received) or expense (paid) |
| HONORAIRES | Professional fees | Self-employment income |
| ORANGE MONEY / WAVE / FREE MONEY | Mobile money | Confirm business vs personal |
| RETRAIT / GAB | Cash withdrawal | Ask what cash was used for |

Working paper lines: gross pay; benefits in kind; 30% abatement capped; taxable income rounded down; tax from bands; parts; family reduction; 43% cap test; TRIMF; IR withheld; balance. Reviewer ticks: parts evidenced, cadre status, benefits confirmed, CGU tested.

If the client cannot answer yet: sort the records with the patterns above, mark review items pending, apply the defaults and give the working paper with flags, then ask: tax home; family situation; employee, real regime or CGU; cadre status; benefits in kind; rent, dividends or interest; turnover and goods or services; IPRES and CSS withheld; TRIMF withheld; other employers or income.

## Deadlines and filing

| Item | Date | Source |
|---|---|---|
| Annual return | Before 1 May (art. 60); calendar says 30 April | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Instalments on real regimes | 15 February, 30 April, each one third of last year's tax (art. 214). Nothing for people whose only income has suffered withholding (art. 213) | same |
| Balance | 15 June (art. 214) | same |
| Salary withholding | First 15 days of next month; real simplified and CGU employers: first 15 days of January, April, July and October for the past quarter (art. 185) | same |
| Annual salary and third-party statements | 31 January, Etat 1024 (art. 191) | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf |
| CGU declaration | Before 1 March (art. 147) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| CGU payment, tax up to 100,000 | Once, before 1 March (art. 145) | same |
| CGU payment, above 100,000 | One third each in first 15 days of March and May (art. 144) | same |
| CGF | Declare before 1 February; pay in three equal parts by end February, April and June, or once by end February (art. 79) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |

How to file:
1. Log in to Mon Espace Perso if an individual or a business with turnover of at most 100 million; otherwise SENTAX where your tax centre has moved to it. CME1, CME2 and CPR must use SENTAX from 1 October 2026; paper is refused.
2. In SENTAX open Teledeclaration, then Declarations a effectuer.
3. Work through the six steps: presentation, entry, attachments, detailed annexes, preview, confirmation.
4. Open Telepaiement, select the amounts, pick the bank account, confirm. A permanent bank authorisation must be set up first.
5. Keep the record from Historique. Box numbers for the IR return are not published on these pages.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late payment | 5%, plus 0.5% per further month or part (art. 665) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Local taxes late | 10% (art. 665) | same |
| General breach | 200,000 (art. 667) | same |
| Register not kept | 1,000,000 per year (art. 667) | same |
| No compliant accounts | 5,000,000 (art. 668) | same |

Employers who withhold and do not pay over are pursued personally (art. 190). Pay records stay until the end of the 11th following year (art. 184).

## Cross-border points

Non-residents with Senegal-source income: maximum 1.5 parts. People without a habitual residence file a note naming a Senegal representative (art. 60). Foreign pensions: art. 180. Treaties override art. 48; the list is at https://www.dgid.sn/conventions-fiscales. Check the treaty text.

## Two worked examples that recompute

Example 1: single employee, XOF 500,000 a month, 1 part. Gross 6,000,000; abatement capped at 900,000; base 5,100,000; tax 1,309,000.

```oa-check
name: Single employee, 1 part
inputs:
  gross: 6000000
steps:
  - abatement: min(gross * 0.30, 900000)
  - base: gross - abatement
  - b2: (1500000 - 630000) * 0.20
  - b3: (4000000 - 1500000) * 0.30
  - b4: (base - 4000000) * 0.35
  - tax: b2 + b3 + b4
expected:
  tax: 1309000.00
```

Example 2, a decision: the same employee is married with two children and the only earner, so 3 parts. The reduction is 25% of 1,309,000, or 327,250, below the 400,000 minimum, so the minimum decides. Tax is 909,000.

```oa-check
name: Married, 2 children, sole earner, 3 parts
inputs:
  tax_before: 1309000
steps:
  - pct: tax_before * 0.25
  - reduction: max(pct, 400000)
  - tax: tax_before - reduction
expected:
  tax: 909000.00
```

## Ask the client first

- Tax home in Senegal, and any treaty country.
- Marital status, children, and whether the spouse has taxable income.
- Employee, sole trader, or professional.
- Turnover with tax, and activity type (CGU or real).
- Rental income, gross.
- Foreign pensions or investment income.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): articles cited in this skill read in the PDF text | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-01 |
| DGID, Lois et reglements: rates table and recent measures (Loi 2025-17) read | https://www.dgid.sn/loi-reglement | 2026-11-01 |
| Loi n. 2025-19, finance law for 2026 (scan, read by OCR, all 64 pages searched): no CGI amendment found; art. 19 adds a cashew export duty | https://budget.sec.gouv.sn/documents/public_download/69556841-a9d4-4658-8c1e-fe230a2a028a/telechargement | 2026-11-01 |
| DGID calendar of annual filings: full table read | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-01 |
| DGID SENTAX user guide v1.1, 2026: contents and steps read | https://www.dgid.sn/storage/uploads/guide-utilisateur-espace-connecte-1790609363.pdf | 2026-11-01 |
| DGID communique: SENTAX for CME1, CME2 and CPR from 1 October 2026: full text read | https://www.dgid.sn/storage/uploads/communique-ouverture-de-la-plateforme-sentax-aux-contribuables-du-cme1-cme2-et-du-cpr-1790699194.pdf | 2026-11-01 |
| DGID Entreprises page: portal descriptions read | https://www.dgid.sn/entreprises | 2026-11-01 |

Not yet confirmed: The text of Loi 2025-17 was not opened; only DGID's summary of it was read, so any CGI change it made beyond that summary is not reflected. Benefit-in-kind scale (old version relied on PwC, carried above; art. 166 not worked through); statutory travel allowance; 30% rental deduction; IPM, IPRES and CSS rates (sites unreachable, see senegal-social-contributions); property gains; real regime expense rules for individuals; IR return box numbers; old claims that income from land is taxed at 20% and wages at 11% found no support in art. 173.

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
