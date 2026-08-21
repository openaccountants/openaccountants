---
name: senegal-income-tax
description: Use this skill whenever asked about Senegal personal income tax (IRPP — Impôt sur le Revenu des Personnes Physiques) for employees and self-employed individuals. Trigger on phrases like "how much tax do I pay in Senegal", "IRPP", "impôt sur le revenu Sénégal", "barème IRPP", "quotient familial", "TRIMF", "Contribution Globale Unique", "CGU", "IPRES", "CSS", "CFCE", "déclaration de revenus", "abattement 30%", "net salary Senegal", "salaire net", "self-employed tax Senegal", or any question about filing or computing income tax for an individual resident in Senegal. Also trigger when preparing or reviewing an annual IRPP return, computing the family quotient, the 30% lump-sum deduction, social contributions, or payroll withholding (PAYE). This skill covers the progressive IRPP barème, the family-quotient parts system, TRIMF, social security (IPRES/CSS/CFCE), CGU for small businesses, filing deadlines, and benefits-in-kind. ALWAYS read this skill before touching any Senegal income tax work. Figures use West African CFA franc (XOF / FCFA).
version: 0.1
jurisdiction: SN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Senegal Personal Income Tax (IRPP) —

## Senegal Personal Income Tax (IRPP) — Skill v0.1

> **Tier 2 — research-verified, pending accountant sign-off.** This skill was assembled from secondary sources (PwC Worldwide Tax Summaries — Senegal, the DGID, and Senegalese payroll references) and cross-checked against the Code Général des Impôts (CGI). Several figures could not be reconciled to a single authoritative text and are marked **[RESEARCH GAP — reviewer to confirm]**. Do not file on the basis of this skill without a Senegalese chartered accountant (Expert-Comptable / member of ONECCA) confirming the flagged items.

## Section 1 — Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Senegal (Republic of Senegal) |
| Tax | Personal income tax — IRPP (Impôt sur le Revenu des Personnes Physiques) |
| Currency | West African CFA franc (XOF / FCFA) only |
| Tax year | Calendar year (1 January – 31 December) |
| Primary legislation | Code Général des Impôts (CGI), Articles 173–174 (barème), amended by the 2022 supplementary finance law |
| Self-employed synthetic tax | Contribution Globale Unique (CGU), CGI Article 141+ |
| Tax authority | Direction Générale des Impôts et des Domaines (DGID) — www.dgid.sn / impotsetdomaines.gouv.sn |
| Social security | IPRES (pensions); CSS (Caisse de Sécurité Sociale) |
| Filing portal | DGID e-services (www.dgid.sn) |
| Annual IRPP filing deadline | Before 1 May of the following year (PwC, tax administration page) |
| Validated by | Pending — requires sign-off by a Senegalese Expert-Comptable (ONECCA) |
| Validation date | Pending |
| Skill version | 0.1 |

### IRPP Progressive Scale — Barème (tax year 2025)

**IRPP Progressive Scale — Barème (tax year 2025)**  _(CGI Article 174 (post-2022 reform); cross-checked against AfricaPaieRH and AfroTools guides (https://africapaierh.com/juridique/cotisations-sociales-et-impots-au-senegal/ ; https://afrotools.com/fr/blog/guide-irpp-senegal-2026/))_

| Annual taxable income per part (FCFA) | Rate | Cumulative tax at top of band (FCFA) |
| --- | --- | --- |
| 0 – 630,000 | 0% | 0 |
| 630,001 – 1,500,000 | 20% | 174,000 |
| 1,500,001 – 4,000,000 | 30% | 924,000 |
| 4,000,001 – 8,000,000 | 35% | 2,324,000 |
| 8,000,001 – 13,500,000 | 37% | 4,359,000 |
| Over 13,500,000 | 40% | — |

- **Cumulative-tax arithmetic (verified)** — Band 2: 870,000 × 20% = 174,000 → cumulative 174,000; Band 3: 2,500,000 × 30% = 750,000 → cumulative 924,000; Band 4: 4,000,000 × 35% = 1,400,000 → cumulative 2,324,000; Band 5: 5,500,000 × 37% = 2,035,000 → cumulative 4,359,000  _(CGI Article 174 (post-2022 reform))_

> **[RESEARCH GAP — reviewer to confirm] — Top bracket conflict.** PwC's Senegal page (last reviewed 31 Mar 2026, https://taxsummaries.pwc.com/senegal/individual/taxes-on-personal-income) shows a **7-band** schedule topping out at **43%** (bands 13,500,001–50,000,000 @ 40% and 50,000,000+ @ 43%). This conflicts with the 6-band / 40% structure consistently reported by Senegalese payroll/tax sources and with CGI Article 174 as cited. The **6-band / 40%** structure above is used here; the PwC 43% top band must be reconciled against the current CGI text before any figure above 13,500,000 FCFA/part is published.

> **[RESEARCH GAP — reviewer to confirm] — First (0%) threshold.** Senegalese sources consistently give **630,000 FCFA** (post-reform); PwC and Rivermate give 600,000. The 630,000 figure is used here pending confirmation.

### Conservative Defaults

**Conservative Defaults Table**

| Ambiguity | Default |
| --- | --- |
| Unknown family situation (parts) | STOP — do not apply the quotient without marital status + number of children |
| Unknown residency | Treat as **non-resident → out of scope** until residency confirmed (see R-SN-3) |
| Unknown whether cadre (executive) | Apply IPRES Régime Général only (no RC supplement) until confirmed |
| Unknown business-use % (vehicle, phone) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown taxable benefit-in-kind value | Use the PwC notional scale (Section 11), flag for reviewer |
| Income above 13,500,000 FCFA/part | STOP — top-band rate unresolved (40% vs 43%); escalate |
| Self-employed turnover ≤ 50,000,000 FCFA | Consider CGU eligibility (Section 7); confirm activity type |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement and/or payslips (bulletin de paie) for the full tax year, plus confirmation of (a) tax residency in Senegal, (b) family situation (marital status + number of dependent children → parts), and (c) employment vs self-employment status.

**Recommended** — full payroll summary (gross, IPRES/CSS withheld, IRPP withheld, TRIMF withheld), prior-year IRPP assessment, IPRES/CSS contribution statements, and confirmation of cadre (executive) status.

**Ideal** — complete income statement, all invoices/receipts, asset register, benefits-in-kind schedule, rental-income detail, and CGU declaration (if self-employed under CGU).

**Refusal if minimum is missing — SOFT WARN.** No income document at all = hard stop. Income document without supporting records = proceed with a reviewer warning: "This IRPP computation was produced from bank statement / payslips alone. The reviewer must verify the family-quotient parts, the cadre/non-cadre IPRES treatment, and that all deductions are supported."

### Refusal Catalogue

- **R-SN-1 — Family situation unknown** — "The family quotient (number of parts) is essential to compute IRPP. This skill cannot compute tax without marital status and number of dependent children. Please confirm before proceeding."  _(R-SN-1)_
- **R-SN-2 — Income above the unresolved top band** — "Taxable income per part exceeds 13,500,000 FCFA. The top IRPP rate is unresolved in research (40% per CGI Art. 174 vs 43% per PwC). Escalate to a Senegalese Expert-Comptable to confirm the rate before computing."  _(R-SN-2)_
- **R-SN-3 — Non-resident / dual-resident** — "Non-resident and dual-resident taxation follow different rules (and withholding regimes). Out of scope. Escalate to a Senegalese Expert-Comptable."  _(R-SN-3)_
- **R-SN-4 — Companies / partnerships** — "This skill covers individuals (employees, sole traders, CGU). Companies pay corporate tax (Impôt sur les Sociétés) and file separate returns. Out of scope."  _(R-SN-4)_
- **R-SN-5 — Penalties / enforcement** — "Senegalese late-filing/late-payment penalty rates were not obtainable from an authoritative source in this research (see Section 9). Do not quote penalty figures. Escalate to a Senegalese Expert-Comptable who can read CGI Livre IV."  _(R-SN-5)_
- **R-SN-6 — Capital gains / property disposals** — "Capital gains and real-estate disposal taxation require specialised analysis. Out of scope. Escalate."  _(R-SN-6)_

## Section 3 — Transaction Pattern Library

Deterministic pre-classifier. When a bank-statement / payslip line matches a pattern, apply the treatment directly. Match by case-insensitive substring on the description as it appears (French / Wolof-influenced terms common). If none match, fall through to Tier 1 rules (Section 5).

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits) Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, BULLETIN, VIREMENT SALAIRE, [employer] | Employment income (IRPP base) | Gross before withholding; goes through the barème |
| HONORAIRES, PRESTATION, FACTURE, CONSULTANCE | Self-employment / BNC income | Business income — confirm CGU vs réel regime |
| LOYER, LOYER PERÇU, RENT RECEIVED | Rental income | 30% standard deduction applies (Section 5.6) |
| DIVIDENDE, DIVIDENDS | Investment income | Proportional rate may apply (Section 5.7) — flag |
| INTÉRÊTS, INTERESTS | Investment income | Flag for reviewer |
| ORANGE MONEY, WAVE, FREE MONEY (business receipts) | Self-employment income | Mobile-money business receipts — match to invoices |
| STRIPE / PAYPAL / WISE PAYOUT | Self-employment income | Platform payout — match to underlying invoices |
| REMBOURSEMENT IMPÔT, TAX REFUND | EXCLUDE | Refund of prior-year tax, not income |

### 3.2 Expense Patterns (Debits) — Deductible (business, before abattement) [self-employed réel only]

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

### 3.3 Expense Patterns (Debits) — Not Deductible

**Not Deductible Expense Patterns Table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, REPAS, DÉJEUNER, RÉCEPTION | Entertainment / meals | Not deductible | Private / blocked |
| COURSES, SUPERMARCHÉ, AUCHAN, EXCLUSIVE | Personal | Not deductible | Private living costs |
| AMENDE, PÉNALITÉ, CONTRAVENTION | Fines/penalties | Not deductible | Public policy |
| IMPÔT, IRPP, PAIEMENT DGID | Tax payments | Not deductible | Income tax cannot reduce income |
| RETRAIT, PRÉLÈVEMENT PERSO, GAB | Drawings / cash | Not deductible | Ask what cash was used for |

### 3.4 Statutory Withholdings & Exclusions

**Statutory Withholdings & Exclusions Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IPRES, RETRAITE, PENSION (employee share) | Deductible from gross before abattement | See Section 5.2 |
| CSS, SÉCURITÉ SOCIALE | Employer-only (employee 0%) — EXCLUDE from employee deduction | Section 6 |
| TRIMF | Minimum personal tax withheld | Section 6 (TRIMF table) |
| CFCE | Employer-only payroll tax — EXCLUDE from employee | Section 6 |
| VIREMENT INTERNE, COMPTE PROPRE | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRÊT, PRÊT | EXCLUDE | Loan principal movement |

### 3.5 Senegalese Banks / Payment Rails — Statement Reference

**Banks / Payment Rails Table**

| Institution | Common patterns | Notes |
| --- | --- | --- |
| CBAO (Attijariwafa) | VIREMENT, PRÉLÈVEMENT, COMMISSION | PDF; description holds counterparty |
| SGBS (Société Générale Sénégal) | VIR, PRLV, FRAIS | PDF/CSV |
| Ecobank Sénégal | TRANSFER, DD, CHARGE | PDF |
| BICIS / UBA / Bank of Africa | VIREMENT, CHÈQUE, AGIOS | PDF |
| Orange Money / Wave / Free Money | PAIEMENT, TRANSFERT, RETRAIT | Mobile money — separate from bank; business vs personal must be confirmed |

## Section 4 — Family Quotient (Quotient Familial — Parts)

**Family Quotient Table**  _(AfroTools IRPP guide (https://afrotools.com/fr/blog/guide-irpp-senegal-2026/); DGID parts simulator (https://www.dgid.sn/simulateur-part/))_

| Family situation | Parts |
| --- | --- |
| Single, no children | 1 |
| Married, no children | 2 |
| Married + 1 child | 2.5 |
| Married + 2 children | 3 |
| Married + 3 children | 3.5 |
| Married + 4 children | 4 |
| Maximum | 5 |

- **Dependent child part increment** — Each dependent child = +0.5 part. Maximum total 5 parts.  _(AfroTools IRPP guide)_

> **[RESEARCH GAP — reviewer to confirm] — Family-relief cap.** Secondary sources cite a maximum family-charge saving of approximately **300,000 FCFA/year** and a "~10% per additional part" framing (https://www.justanswer.com/social-security/...). This cap is secondary and unverified; confirm the plafonnement against the CGI before applying any ceiling to the quotient benefit. The reduction can never produce a refund.

### 5.1 IRPP computation order (employment income)

- **Computation order steps** — 1. Start from gross annual remuneration (salary + taxable benefits-in-kind, Section 11). 2. Deduct mandatory employee social contributions (IPRES employee share — Section 6). 3. Apply the 30% lump-sum deduction (abattement), capped at 900,000 FCFA (Section 5.2). 4. Result = annual net taxable income. 5. Divide by the number of parts (Section 4) → income per part. 6. Apply the barème (Section 1) to income per part → tax per part. 7. Multiply tax per part by number of parts → IRPP before family-relief cap. 8. Apply any family-relief cap [RESEARCH GAP] and confirm result is not negative. 9. Add TRIMF (Section 6) separately — it is a distinct minimum tax, not part of the barème.

### 5.2 The 30% lump-sum deduction (abattement)

- **Abattement rules** — 30% of employment income (representing professional expenses), capped at 900,000 FCFA. Applied after deducting employee IPRES/CSS contributions. A separate 30% standard deduction applies to gross rental income.  _(CGI; DGID flyer (via https://africapaierh.com/juridique/cotisations-sociales-et-impots-au-senegal/); https://afrotools.com/fr/blog/guide-irpp-senegal-2026/)_

### 5.3 Deductible social contributions

- **Deductible social contributions rule** — Only the employee share of IPRES is deductible from gross before the abattement. Employee CSS = 0% (CSS is employer-only). CFCE is employer-only. See Section 6.

### 5.4 Self-employment income

- **Self-employment income treatment** — Sole traders / professionals under the réel regime: net business profit (income less wholly-business expenses, Section 3.2) feeds the IRPP barème via the quotient. Small traders/service providers with turnover ≤ 50,000,000 FCFA may instead fall under the CGU synthetic tax (Section 7). BNC (non-commercial professional) income, rental income, or multiple employers → standard IRPP, must file an annual return (Section 8).

### 5.5 Non-deductible expenses

**Non-deductible expenses table**

| Expense | Reason |
| --- | --- |
| Entertainment / personal meals | Private |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax (IRPP) itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |

### 5.6 Rental income

- **Rental income treatment** — Gross rental income less a 30% standard deduction. Net feeds the IRPP. Income from land may attract a proportional rate — see 5.7 and flag for reviewer.  _(https://afrotools.com/fr/blog/guide-irpp-senegal-2026/)_

### 5.7 Proportional rates by income type

> **[RESEARCH GAP — reviewer to confirm].** PwC reports proportional rates layered alongside the progressive IRPP by income nature: wages/salaries 11%, dividends 10%, income from land 20%, other income 25% (https://taxsummaries.pwc.com/senegal/individual/taxes-on-personal-income). In practice the salary computation now runs through the single progressive barème above. Whether all proportional rates still apply post-reform must be confirmed before relying on them.

## Section 6 — Social Security & Payroll Levies

All figures below confirmed by PwC (https://taxsummaries.pwc.com/senegal/individual/other-taxes) and the official DGID flyer (parsed via https://africapaierh.com/juridique/cotisations-sociales-et-impots-au-senegal/); the two sources agree.

### 6.1 IPRES — Retirement (pension)

**IPRES Table**  _(PwC (https://taxsummaries.pwc.com/senegal/individual/other-taxes); DGID flyer (https://africapaierh.com/juridique/cotisations-sociales-et-impots-au-senegal/))_

| Regime | Employer | Employee | Total | Monthly ceiling (base) |
| --- | --- | --- | --- | --- |
| Régime Général (RG) | 8.4% | 5.6% | **14.0%** | 432,000 FCFA/month (5,184,000/yr) |
| Régime Complémentaire / Cadre (RC) | 3.6% | 2.4% | **6.0%** | 1,296,000 FCFA/month (15,552,000/yr) — executives/cadres only |

- **Total-column arithmetic (verified)** — RG 8.4% + 5.6% = 14.0%. RC 3.6% + 2.4% = 6.0%. RC applies in addition to RG for cadres only.

### 6.2 CSS — Caisse de Sécurité Sociale (employer-only)

**CSS Table**  _(PwC (https://taxsummaries.pwc.com/senegal/individual/other-taxes); DGID flyer)_

| Branch | Rate | Payer | Monthly ceiling (base) |
| --- | --- | --- | --- |
| Prestations familiales (family benefits) | 7.0% | Employer only | 63,000 FCFA |
| Accident du travail / maladie professionnelle | 1%, 3% or 5% (by industry risk) | Employer only | 63,000 FCFA |

- **Employee CSS rate** — Employee CSS contribution = 0%.

### 6.3 Health insurance (IPM / employment medical coverage)

> **[RESEARCH GAP — reviewer to confirm] — exact split and caps.** PwC: ~6% on a base of 60,000–250,000 FCFA/month, split between employer and employee; secondary sources cite employer cap ~30,000 FCFA/month and employee portion ~10,000 FCFA/month. "Non-work-related illness" coverage: 2%–7.5% shared employer/employee, base up to 250,000 FCFA/month (PwC, https://taxsummaries.pwc.com/senegal/individual/other-taxes). Confirm the exact split before computing.

### 6.4 CFCE — Contribution Forfaitaire à la Charge de l'Employeur

- **CFCE rate** — 3.0% percent (of gross taxable salary, employer only (payroll tax))  _(DGID flyer (https://africapaierh.com/juridique/cotisations-sociales-et-impots-au-senegal/))_

### 6.5 TRIMF — Taxe Représentative de l'Impôt du Minimum Fiscal

A flat minimum personal tax due by every resident receiving salary/pension (unless exempt), withheld monthly. Scale depends only on salary level. Monthly amounts (Horus payroll knowledge base, https://helpdesk.horus-solutions.org/kb/faq.php?id=14):

**TRIMF Table**  _(Horus payroll knowledge base (https://helpdesk.horus-solutions.org/kb/faq.php?id=14))_

| Monthly salary base (FCFA) | TRIMF (monthly, FCFA) |
| --- | --- |
| < 50,000 | 0 |
| 50,000 – 83,332 | 300 |
| 83,333 – 166,665 | 400 |
| 166,666 – 583,332 | 500 |
| 583,333 – 999,999 | 1,500 |
| 1,000,000 + | 3,000 |

> **[RESEARCH GAP — reviewer to confirm] — TRIMF annual scale.** These appear to be monthly figures (annualised they correspond to the commonly cited annual TRIMF scale topping out around 18,000–36,000 FCFA/year). The exact annual scale and top amount could not be pinned to a single authoritative DGID table. Multiply by TRIMF shares (1 for employee + 1 for a non-working spouse). Confirm against the CGI/DGID barème before publishing annual figures.

## Section 7 — Self-Employed / Small Business: Contribution Globale Unique (CGU)

**CGU Table**  _(CGI Article 141+; https://kof-experts.sn/2024/04/26/the-unified-global-contribution-ugc-in-senegal/?lang=en ; DGID (http://www.impotsetdomaines.gouv.sn/fr/faire-une-declaration-pour-la-contribution-globale-unique))_

| Item | Detail |
| --- | --- |
| Eligibility threshold | Annual turnover (all taxes included) ≤ **50,000,000 FCFA** — same for goods delivery and for services |
| Excludes | BNC (non-commercial-profit) activities; real-estate sale/rental/management |
| Replaces 6 levies | IR on industrial/commercial profits (BIC), minimum fiscal tax (IMF), local economic contribution (CEL)/patente, beverage-licence duty, VAT, and the employer payroll contribution (CFCE) |
| Minimum payable — traders/goods | **25,000 FCFA** |
| Minimum payable — service providers | **30,000 FCFA** |
| Rate | Progressive by bracket (CGI Art. 141) — **[RESEARCH GAP — bracket schedule not captured]**; obtain from the DGID CGU simulator (http://www.impotsetdomaines.gouv.sn/fr/simulateur/cgu) |
| Annual declaration | To the managing tax centre by **end of February** |
| Opt-out to réel / réel simplifié | Notify by **31 January** |
| Payment (≤ 100,000 FCFA total) | One instalment before **1 March** |
| Payment (> 100,000 FCFA) | Two instalments on **15 March** and **15 May**, each = one-third of tax due |

## Section 8 — Filing & Payment Deadlines

- **Filing and payment deadlines** — Tax year: calendar year. Annual IRPP return: all individuals subject to PIT must file before 1 May of each year (some local sources say "before 30 April" — effectively the same). Salary-only earners whose tax is fully withheld at source by the employer are generally exempt from filing. PAYE / withholding: employers withhold IRPP + TRIMF + employee IPRES monthly on gross remuneration (incl. benefits-in-kind and bonuses); remitted to DGID/CSS/IPRES typically by ~the 15th of the following month [RESEARCH GAP — confirm exact remittance date against the DGID calendar]. CGU: see Section 7.  _(https://taxsummaries.pwc.com/senegal/individual/tax-administration ; Rivermate (https://rivermate.com/guides/senegal/taxes))_

## Section 9 — Penalties

> **[RESEARCH GAP — reviewer to confirm] — penalties not sourced.** Specific Senegalese late-filing / late-payment penalty rates and interest (majorations / intérêts de retard) were not obtainable from an authoritative source in this research (PwC's tax-administration page omits them). Do not invent or quote penalty figures. They must be extracted directly from the Senegalese Code Général des Impôts, Livre IV (procédures fiscales). Reference copy: https://senegal.eregulations.org/media/t-code-general-impots[1].pdf. Escalate any penalty question to a Senegalese Expert-Comptable (see R-SN-5).

### 10.1 Cadre (executive) status — IPRES RC

- **Cadre status IPRES RC rule** — The IPRES Régime Complémentaire (RC) 2.4% employee / 3.6% employer supplement applies only to cadres (executives). Conservative default: apply RG only (no RC) until cadre status is confirmed. Flag for reviewer: confirm cadre classification and the correct ceiling base.

### 10.2 Family quotient parts

- **Family quotient parts Tier 2 rule** — Number of parts depends on marital status and dependent children (Section 4). Conservative default: STOP — do not compute without confirmed parts. Flag for reviewer: confirm number of dependent children and the (unverified) family-relief cap.

### 10.3 Benefits-in-kind valuation

- **Benefits-in-kind valuation rule** — Taxable benefits use the PwC notional scale (Section 11). Flag for reviewer: confirm each benefit and whether the statutory travel allowance exemption applies.

### 10.4 Proportional vs progressive rates

- **Proportional vs progressive rates rule** — Whether the proportional rates (Section 5.7) still apply post-reform is unresolved. Flag for reviewer: confirm treatment for dividends, land income, and "other" income.

### 10.5 Home office / mixed-use expenses (self-employed réel)

- **Home office mixed-use expenses rule** — Only the business-use portion of phone, internet, and premises is deductible. Conservative default: 0% until a documented business percentage is provided.

### 10.6 CGU vs réel regime

- **CGU vs réel regime determination rule** — Turnover near the 50,000,000 FCFA threshold, or activities that exclude CGU (BNC, real estate), require a regime determination. Flag for reviewer: confirm eligibility and whether opting into réel is beneficial.

## Section 11 — Benefits-in-Kind Notional Values

**Benefits-in-Kind Notional Values Table**  _(PwC (https://taxsummaries.pwc.com/senegal/individual/income-determination))_

| Benefit | Notional value (FCFA/month) |
| --- | --- |
| Accommodation | 13,500 – 33,500 |
| Domestic staff | 35,600 – 92,500 |
| Utilities | 10,500 – 30,200 |
| Company car | 26,000 – 77,500 |
| Telephone | 67,000 |
| Statutory travel allowance | **Exempt up to 26,000 FCFA/month** |

## Section 12 — Worked Examples

All examples use the 6-band barème (Section 1), the 30% abattement capped at 900,000, and IPRES employee shares (Section 6). Arithmetic recomputed end-to-end. TRIMF added separately. Family-relief cap not applied (unverified — flagged).

### Example 1 — Single, no children (1 part), cadre, gross 6,000,000 FCFA/yr

**Payslip line:**
`31/03/2025 ; CBAO ; VIREMENT SALAIRE ; SOCIÉTÉ ABC SARL ; +500,000.00 ; FCFA` (×12 = 6,000,000/yr)

**Reasoning:**
- IPRES RG employee: 5.6% × min(6,000,000, 5,184,000) = 5.6% × 5,184,000 = **290,304**
- IPRES RC employee (cadre): 2.4% × min(6,000,000, 15,552,000) = 2.4% × 6,000,000 = **144,000**
- Total IPRES employee = 290,304 + 144,000 = **434,304**
- Gross less social = 6,000,000 − 434,304 = **5,565,696**
- Abattement = min(30% × 5,565,696, 900,000) = min(1,669,708.8, 900,000) = **900,000** (capped)
- Net taxable = 5,565,696 − 900,000 = **4,665,696**
- Parts = 1 → income per part = 4,665,696
- Barème: cumulative at 4,000,000 = 924,000; excess 665,696 × 35% = 232,993.6 → tax per part = **1,156,993.6**
- × 1 part = **IRPP ≈ 1,156,994 FCFA**
- TRIMF: monthly base 500,000 FCFA → 500 FCFA/month × 12 = **6,000 FCFA/yr** (annual scale unverified — flagged)

**Result:** IRPP ≈ 1,156,994 FCFA + TRIMF 6,000 FCFA.

### Example 2 — Married + 2 children (3 parts), cadre, gross 9,000,000 FCFA/yr

**Reasoning:**
- IPRES RG employee: 5.6% × 5,184,000 = **290,304**
- IPRES RC employee: 2.4% × 9,000,000 = **216,000**
- Total IPRES employee = **506,304**
- Gross less social = 9,000,000 − 506,304 = **8,493,696**
- Abattement = min(30% × 8,493,696, 900,000) = min(2,548,108.8, 900,000) = **900,000** (capped)
- Net taxable = 8,493,696 − 900,000 = **7,593,696**
- Parts = 3 → income per part = 7,593,696 / 3 = **2,531,232**
- Barème: cumulative at 1,500,000 = 174,000; excess 1,031,232 × 30% = 309,369.6 → tax per part = **483,369.6**
- × 3 parts = **IRPP ≈ 1,450,109 FCFA** (before any family-relief cap — flagged)
- TRIMF: monthly base 750,000 FCFA → 1,500 FCFA/month × 12 = **18,000 FCFA/yr** (annual scale unverified — flagged)

**Result:** IRPP ≈ 1,450,109 FCFA + TRIMF 18,000 FCFA.

### Example 3 — Single, low earner (1 part), non-cadre, gross 1,800,000 FCFA/yr

**Reasoning:**
- IPRES RG employee: 5.6% × min(1,800,000, 5,184,000) = 5.6% × 1,800,000 = **100,800**
- No RC (non-cadre).
- Gross less social = 1,800,000 − 100,800 = **1,699,200**
- Abattement = min(30% × 1,699,200, 900,000) = min(509,760, 900,000) = **509,760**
- Net taxable = 1,699,200 − 509,760 = **1,189,440**
- Parts = 1 → income per part = 1,189,440
- Barème: cumulative at 630,000 = 0; excess (1,189,440 − 630,000) = 559,440 × 20% = **111,888**
- × 1 part = **IRPP ≈ 111,888 FCFA**
- TRIMF: monthly base 150,000 FCFA → 400 FCFA/month × 12 = **4,800 FCFA/yr** (annual scale unverified — flagged)

**Result:** IRPP ≈ 111,888 FCFA + TRIMF 4,800 FCFA.

### Example 4 — Self-employed trader, CGU regime

**Input:** Sole trader, annual turnover 18,000,000 FCFA (all taxes included), goods retail.

**Reasoning:**
- Turnover 18,000,000 ≤ 50,000,000 → CGU-eligible (goods). Not BNC, not real estate.
- CGU replaces BIC/IMF/CEL/patente/beverage-licence/VAT/CFCE.
- Tax = progressive CGU bracket on turnover — **[RESEARCH GAP — bracket schedule not captured]**; compute via DGID CGU simulator.
- **Minimum payable = 25,000 FCFA** (goods trader).
- Declaration by end of February; if total > 100,000 FCFA → two instalments (15 March, 15 May).

**Result:** CGU due = simulator output, but **not less than 25,000 FCFA**. Do NOT run this trader through the IRPP barème.

### Example 5 — Internal transfer (exclude)

**Input line:**
`15/05/2025 ; SGBS ; VIREMENT INTERNE — COMPTE ÉPARGNE ; ; -2,000,000.00 ; FCFA`

**Reasoning:** Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Result:** EXCLUDE.

### Example 6 — Rental income (30% deduction)

**Input line:**
`05/02/2025 ; ECOBANK ; LOYER PERÇU — APPT DAKAR ; LOCATAIRE D. NDIAYE ; +400,000.00 ; FCFA` (×12 = 4,800,000/yr)

**Reasoning:**
- Gross rent = 4,800,000 FCFA/yr.
- 30% standard deduction = 1,440,000 → net rental = **3,360,000 FCFA**.
- Net feeds IRPP (combined with other income, divided by parts). Income from land may attract a proportional rate (Section 5.7) — **flag for reviewer**.

**Result:** Net rental 3,360,000 FCFA into the IRPP base; proportional-rate treatment flagged.

## Section 13 — Excel Working Paper Template

```
SENEGAL IRPP -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency in Senegal: Yes / No
Family situation: Single / Married, children: ____  -> Parts: ____
Cadre (executive)? Yes / No

A. GROSS EMPLOYMENT INCOME
  A1. Salary                                      ___________
  A2. Taxable benefits-in-kind (Sec 11)           ___________
  A3. TOTAL GROSS                                 ___________

B. DEDUCTIBLE SOCIAL CONTRIBUTIONS (EMPLOYEE)
  B1. IPRES RG employee 5.6% (cap base 5,184,000) ___________
  B2. IPRES RC employee 2.4% (cadre only)         ___________
  B3. TOTAL IPRES employee (B1 + B2)              ___________

C. INCOME AFTER SOCIAL (A3 - B3)                  ___________

D. 30% ABATTEMENT = min(30% x C, 900,000)         ___________

E. NET TAXABLE INCOME (C - D)                      ___________

F. OTHER INCOME (net rental after 30%, etc.)       ___________

G. TOTAL NET TAXABLE (E + F)                        ___________

H. PARTS (Section 4)                                ___________
I. INCOME PER PART (G / H)                          ___________

J. BARÈME TAX PER PART (Section 1)                  ___________
K. IRPP BEFORE FAMILY CAP (J x H)                   ___________
L. FAMILY-RELIEF CAP  [RESEARCH GAP -- confirm]     ___________
M. IRPP AFTER CAP                                   ___________

N. TRIMF (Section 6.5, monthly x 12)               ___________
O. TOTAL PERSONAL TAX (M + N)                       ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Parts confirmed (marital status + children)?
  [ ] Cadre status confirmed (IPRES RC)?
  [ ] Income per part <= 13,500,000 (else top-band rate unresolved)?
  [ ] Family-relief cap confirmed against CGI?
  [ ] TRIMF annual scale confirmed?
  [ ] Benefits-in-kind valued and confirmed?
  [ ] Proportional rates (dividends/land/other) confirmed?
  [ ] Penalties NOT quoted (research gap)?
```

## Section 14 — Bank Statement / Payslip Reading Guide

### Key Senegalese / French payroll & banking terms

**Payroll & Banking Terms Table**

| Term | English | Classification hint |
| --- | --- | --- |
| SALAIRE BRUT | Gross salary | IRPP base (before deductions) |
| SALAIRE NET | Net salary | After tax + social withholdings |
| VIREMENT / VIR | Transfer | Check direction for income/expense |
| PRÉLÈVEMENT / PRLV | Direct debit | Regular expense |
| AGIOS / FRAIS / COMMISSION | Bank charges | Deductible (business account) |
| IPRES | Pension contribution | Employee share deductible before abattement |
| CSS | Social security | Employer-only (employee 0%) |
| TRIMF | Minimum personal tax | Withheld; separate from barème |
| CFCE | Employer payroll tax | Employer-only (exclude from employee) |
| ABATTEMENT | Lump-sum deduction | 30%, capped 900,000 |
| QUOTIENT FAMILIAL / PARTS | Family quotient | Divides taxable income |
| LOYER | Rent | Income (received) or expense (paid) |
| HONORAIRES | Professional fees | Self-employment income |
| ORANGE MONEY / WAVE / FREE MONEY | Mobile money | Confirm business vs personal |
| RETRAIT / GAB | Cash withdrawal | Ask what cash was used for |

## Section 15 — Onboarding Fallback

If the client provides income documents but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 13) with clear flags.
5. Present the following questions:

```
ONBOARDING QUESTIONS -- SENEGAL IRPP
1. Are you tax-resident in Senegal?
2. Family situation: single, married? Number of dependent children?
3. Employment status: employee, self-employed (réel), or CGU small business?
4. Are you a cadre (executive) for IPRES purposes?
5. Any benefits-in-kind (housing, car, phone, domestic staff, utilities)?
6. Any rental income? Any dividends or interest?
7. If self-employed: annual turnover (all taxes included)? Goods or services?
8. Total IPRES / CSS withheld in the tax year (per payslips)?
9. TRIMF withheld in the tax year?
10. Any other employers or other income sources?
```

## Section 16 — Reference Material & Test Suite

### Key references

**Key References Table**

| Topic | Reference |
| --- | --- |
| IRPP progressive scale | CGI Articles 173–174 (post-2022 reform) — cross-checked AfricaPaieRH / AfroTools |
| 30% abattement (cap 900,000) | DGID flyer (via AfricaPaieRH); PwC deductions page |
| Family quotient (parts) | AfroTools IRPP guide; DGID parts simulator (https://www.dgid.sn/simulateur-part/) |
| TRIMF | Horus payroll KB (https://helpdesk.horus-solutions.org/kb/faq.php?id=14) — annual scale flagged |
| IPRES / CSS / CFCE rates | PwC "other taxes"; DGID flyer (both agree) |
| Benefits-in-kind | PwC income-determination page |
| CGU (synthetic tax) | CGI Art. 141+; DGID CGU pages; KOF Experts guide |
| Filing deadline | PwC tax-administration page |
| Penalties | **[RESEARCH GAP]** — CGI Livre IV (eregulations PDF) |
| Minimum wage (SMIG) | **[RESEARCH GAP]** — see below |

### Minimum wage (SMIG) — informational only

> **[RESEARCH GAP — reviewer to confirm].** Conflicting secondary figures: ~**64,223 FCFA/month** (hourly ~370.526 FCFA) after a 5–10% private-sector increase decree (https://www.sikafinance.com/...); other sources cite ~58,900 FCFA/month or ~52,500 FCFA. Base instrument historically Decree No. 2018-1048 (11 June 2018) for SMIG (non-agricultural) and SMAG (agricultural). Most plausibly ~64,000 FCFA/month for 2025 after revaluation, but confirm against the official Ministère du Travail decree. SMAG (agricultural) is lower. Not used in any IRPP computation here.

### Test Suite

**Test 1 — Single, no children, cadre, gross 6,000,000.**
Expected: IPRES employee 434,304; net taxable 4,665,696; income per part 4,665,696; IRPP ≈ 1,156,994; TRIMF 6,000/yr (scale flagged).

**Test 2 — Married + 2 children (3 parts), cadre, gross 9,000,000.**
Expected: IPRES employee 506,304; net taxable 7,593,696; per part 2,531,232; tax per part 483,369.6; IRPP ≈ 1,450,109 (pre-cap); TRIMF 18,000/yr (scale flagged).

**Test 3 — Single, non-cadre, gross 1,800,000.**
Expected: IPRES employee 100,800; abattement 509,760 (not capped); net taxable 1,189,440; IRPP ≈ 111,888; TRIMF 4,800/yr (scale flagged).

**Test 4 — CGU trader, turnover 18,000,000 (goods).**
Expected: CGU regime; minimum payable 25,000 FCFA; do NOT use IRPP barème; CGU bracket rate flagged as research gap.

**Test 5 — Rental income 4,800,000 gross.**
Expected: 30% deduction 1,440,000; net rental 3,360,000 into IRPP base; proportional-rate treatment flagged.

**Test 6 — Income per part above 13,500,000.**
Expected: STOP (R-SN-2) — top-band rate unresolved (40% vs 43%); escalate, do not compute.

**Test 7 — Cumulative-tax consistency.**
Expected: band cumulatives 174,000 / 924,000 / 2,324,000 / 4,359,000 reproduce exactly from band widths × rates (Section 1).

## PROHIBITIONS

- **Prohibitions list** — NEVER apply the barème without a confirmed family-quotient parts figure. NEVER compute tax for income per part above 13,500,000 FCFA — the top rate (40% vs 43%) is unresolved. NEVER quote a Senegalese late-filing / late-payment penalty figure — they are unsourced (research gap). NEVER apply the IPRES RC supplement to a non-cadre. NEVER treat the 30% abattement as uncapped — it is capped at 900,000 FCFA. NEVER deduct employee CSS — the employee CSS rate is 0%. NEVER deduct CFCE from the employee — it is employer-only. NEVER run a CGU-eligible small trader through the IRPP barème. NEVER allow entertainment, fines, drawings, or income tax itself as a deduction. NEVER present any flagged [RESEARCH GAP] figure as definitive — escalate to a Senegalese Expert-Comptable.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Senegalese Expert-Comptable / ONECCA member, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
