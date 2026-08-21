---
name: luxembourg-income-tax
description: Use this skill whenever asked about Luxembourg personal income tax for self-employed individuals (indépendants) and individuals. Trigger on phrases like "how much tax do I pay in Luxembourg", "déclaration d'impôt", "Form 100", "modèle 100", "tax class", "classe d'impôt", "barème", "revenu imposable", "solidarity surcharge", "employment fund", "fonds pour l'emploi", "CCSS contributions", "cotisations sociales", "self-employed tax Luxembourg", "indépendant", "advance tax payments", "avances trimestrielles", "salaire social minimum", or any question about filing or computing Luxembourg income tax for a self-employed or individual client. Also trigger when preparing or reviewing a Form 100 / Form 163 return, computing deductible business expenses, estimating social contributions, or advising on quarterly advance payments. This skill covers the 23-band progressive PIT scale (0%–42%), the employment-fund (solidarity) surcharge, tax classes 1/1a/2, CCSS social contributions (employee, employer, self-employed), Form 100 structure, advance payments, penalties, and interaction with VAT and the social-security ceiling. ALWAYS read this skill before touching any Luxembourg income tax work.
version: 0.1
jurisdiction: LU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg Income Tax -- Self-Employed and Individuals

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Luxembourg (Grand Duchy of Luxembourg) |
| Tax | Personal Income Tax (impôt sur le revenu des personnes physiques) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) [Guichet.lu] |
| Primary legislation | Loi modifiée du 4 décembre 1967 concernant l'impôt sur le revenu (LIR / Income Tax Law) |
| Supporting legislation | Code de la sécurité sociale (social contributions); Loi du 12 juillet 2024 + budget/index-adjustment laws applying the 2.5 index-bracket adjustment to the 2025 PIT scale |
| Direct-tax authority | Administration des contributions directes (ACD) |
| Social-security authority | Centre commun de la sécurité sociale (CCSS); health fund Caisse nationale de santé (CNS); pension fund Caisse nationale d'assurance pension (CNAP) |
| Filing portal | MyGuichet.lu (guichet.public.lu) |
| Annual return | Form 100 (modèle 100) -- déclaration pour l'impôt sur le revenu des personnes physiques [Guichet.lu] |
| Filing deadline | 31 December of the year following the income year; income year 2025 due 31 December 2026, filing window opens 7 April 2026 [Guichet.lu] |
| Verified by | Pending -- requires sign-off by a Luxembourg-qualified tax adviser / expert-comptable |
| Verification date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets -- 2025 Progressive Scale (barème), Tax Class 1

**2025 Progressive Scale Tax Class 1**  _([PwC])_

| Taxable Income (EUR) | Marginal Rate | Cumulative Tax at Top of Band (EUR) |
| --- | --- | --- |
| 0 -- 13,230 | 0% | 0.00 |
| 13,230 -- 15,435 | 8% | 176.40 |
| 15,435 -- 17,640 | 9% | 374.85 |
| 17,640 -- 19,845 | 10% | 595.35 |
| 19,845 -- 22,050 | 11% | 837.90 |
| 22,050 -- 24,255 | 12% | 1,102.50 |
| 24,255 -- 26,550 | 14% | 1,423.80 |
| 26,550 -- 28,845 | 16% | 1,791.00 |
| 28,845 -- 31,140 | 18% | 2,204.10 |
| 31,140 -- 33,435 | 20% | 2,663.10 |
| 33,435 -- 35,730 | 22% | 3,168.00 |
| 35,730 -- 38,025 | 24% | 3,718.80 |
| 38,025 -- 40,320 | 26% | 4,315.50 |
| 40,320 -- 42,615 | 28% | 4,958.10 |
| 42,615 -- 44,910 | 30% | 5,646.60 |
| 44,910 -- 47,205 | 32% | 6,381.00 |
| 47,205 -- 49,500 | 34% | 7,161.30 |
| 49,500 -- 51,795 | 36% | 7,987.50 |
| 51,795 -- 54,090 | 38% | 8,859.60 |
| 54,090 -- 117,450 | 39% | 33,570.00 |
| 117,450 -- 176,160 | 40% | 57,054.00 |
| 176,160 -- 234,870 | 41% | 81,125.10 |
| 234,870+ | 42% | -- |

- **Tax-free threshold** — The first EUR 13,230 of taxable income (class 1) is taxed at 0% -- this is Luxembourg's tax-free threshold after the 2.5 index-bracket inflation adjustment for 2025. There is no separate flat personal allowance; the 0% band IS the allowance.  _([PwC])_

### Employment-Fund (Solidarity) Surcharge

**Employment-Fund Surcharge table**  _([PwC])_

| Taxable Income | Surcharge on PIT (classes 1 and 1a) | Surcharge on PIT (class 2) |
| --- | --- | --- |
| Up to threshold | 7% | 7% |
| Above EUR 150,000 (class 1/1a) / EUR 300,000 (class 2) | 9% | 9% |

- **Surcharge application** — Applied on top of the PIT computed from the scale above.  _([PwC])_

### Tax Classes

**Tax Classes table**  _([PwC])_

| Class | Who | Treatment |
| --- | --- | --- |
| Class 1 | Single / individually taxed, no dependent child | Full progressive scale, no splitting -- least favourable |
| Class 1a | Single with dependent child, widowed, or aged 65+ | More favourable scale |
| Class 2 | Married / partnered opting for joint taxation | Income-splitting -- most favourable |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown tax class | Class 1 (single, no children) -- highest, most conservative outcome (see Section 1A) |
| Solidarity surcharge rate | 7% on PIT (9% only if taxable income > EUR 150,000 class 1/1a or > EUR 300,000 class 2) |
| Social-contribution ceiling | Use May 2025 ceiling EUR 13,518.68/month for full-year estimates; note Jan–Apr 2025 was EUR 13,188.96 |
| Employer MDE class / accident coefficient | MDE class II–III and accident coefficient 1.0 (0.75%) where firm-specific data unknown |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration status | Assume registered (turnover > EUR 50,000) unless confirmed under the franchise scheme |

### Section 1A -- Why default to Class 1

Classes 1a and 2 give more favourable treatment via splitting and abatements. Defaulting to class 1 avoids overstating reliefs and gives the highest (most conservative) tax estimate for a single individual. Never silently assume class 2 or 1a -- it materially understates tax. [PwC]

### Required Inputs

**Minimum viable** -- bank statement for the full income year in CSV, PDF, or pasted text, plus confirmation of tax class (1 / 1a / 2) and status (self-employed indépendant filing by assessment, or employee). For employees not filing a full return, confirm whether a Form 163 annual adjustment applies.

**Recommended** -- all sales invoices, purchase invoices/receipts, CCSS contribution statements, prior year Form 100 or tax assessment (bulletin d'impôt), VAT registration status (registered / franchise scheme).

**Ideal** -- complete income and expenditure account (compte de résultat), asset register with depreciation schedule, quarterly advance-payment confirmations, employment income (fiche de retenue / tax card) details, family situation (dependent children, age, marital/partnership status).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Form 100 working paper was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that expenses were incurred in the production of income (frais d'obtention / dépenses d'exploitation)."

### Refusal Catalogue

- **R-LU-1 -- Tax class unknown** — Tax class (classe d'impôt 1, 1a, or 2) determines how the progressive scale and the solidarity-surcharge threshold are applied. This skill defaults to class 1 (most conservative) but flags the result. Confirm class before relying on the figure.
- **R-LU-2 -- Companies, partnerships, holding structures** — This skill covers individuals and sole-trader/liberal-profession indépendants only. Sociétés (SARL, SA), SOPARFI holdings, and partnerships file separate returns (corporate income tax / municipal business tax / net wealth tax). Escalate to a Luxembourg tax adviser.
- **R-LU-3 -- Non-resident / cross-border (frontalier) taxation** — Non-resident and cross-border (French/German/Belgian frontalier) taxation, treaty relief, and the 90% rule for assimilation to resident treatment have specific rules. Out of scope. Escalate to a Luxembourg tax adviser.
- **R-LU-4 -- Capital gains / property disposals** — Capital gains (plus-values) on real estate or substantial shareholdings have separate rules and rates. Escalate to a Luxembourg tax adviser.
- **R-LU-5 -- Impatriate / expat regimes** — The impatriate regime, the participative premium (prime participative), and stock-option/profit-sharing schemes have specific conditions. Escalate to a Luxembourg tax adviser.
- **R-LU-6 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to ACD enforcement. Late-payment interest runs at 0.6% per month and a late-filing surcharge of up to 10% plus a fine up to EUR 25,000 may apply. Do not advise -- escalate immediately.  _([taxx.lu])_
- **R-LU-7 -- VAT return requested** — This skill covers personal income tax (Form 100 / Form 163) only. For Luxembourg VAT, use the dedicated VAT skill. Standard VAT rate 17%, intermediate 14%, reduced 8%, super-reduced 3%; registration compulsory above EUR 50,000 turnover.  _([Expatica])_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Luxembourg statements mix French, German, and English terms. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | Working-Paper Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + VIREMENT, VIR, ÜBERWEISUNG, TRANSFER, PAIEMENT FACTURE | Gross professional income | Business income | If VAT-registered, extract net (excl. 17% VAT) |
| HONORAIRES, FEES, PROFESSIONAL FEES, PRESTATIONS | Gross professional income | Business income | Professional/liberal-profession fees |
| STRIPE PAYOUT, STRIPE TRANSFER | Gross professional income | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Gross professional income | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Gross professional income | Business income | International platform payout |
| UPWORK, FIVERR, MALT, TOPTAL | Gross professional income | Business income | Freelance platform -- net of platform commission |
| SALAIRE, TRAITEMENT, GEHALT, PAYROLL, EMPLOYER [name] | Employment income (separate category) | Employment income | NOT self-employment -- wage tax already withheld at source |
| LOYER REÇU, RENT RECEIVED, MIETE | Rental income (separate category) | Rental income | Revenus de location -- separate income category |
| INTÉRÊTS, INTEREST, ZINSEN | Investment income (separate category) | Investment income | Interest income |
| DIVIDENDE, DIVIDEND | Investment income (separate category) | Investment income | Dividend income |
| REMBOURSEMENT IMPÔT, ACD REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund from prior year |
| AIDE, SUBVENTION, GRANT | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue/operating grants = business income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible Operating Expenses

**Fully Deductible Operating Expenses table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LOYER BUREAU, OFFICE RENT, MIETE BÜRO | Office rent | Fully deductible | Dedicated business premises |
| ASSURANCE RC PRO, PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Fully deductible |  |
| EXPERT-COMPTABLE, FIDUCIAIRE, COMPTABLE, ACCOUNTANT, AUDIT | Accountancy fees | Fully deductible |  |
| AVOCAT, LAWYER, NOTAIRE (business), LEGAL | Legal fees | Fully deductible | Must be business-related |
| FOURNITURES, OFFICE SUPPLIES, PAPETERIE | Office supplies | Fully deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS, PUBLICITÉ | Marketing/advertising | Fully deductible |  |
| FORMATION, CPD, COURSE, SÉMINAIRE, CONFERENCE | Training/CPD | Fully deductible | Must relate to current business |
| COTISATION PROFESSIONNELLE, ORDRE, CHAMBRE | Professional subscriptions | Fully deductible |  |
| FRAIS BANCAIRES, BANK FEE, KONTOFÜHRUNG | Bank charges | Fully deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, COMMISSION | Payment processing fees | Fully deductible |  |
| POSTE, POST LUXEMBOURG (business), POSTAGE | Postage | Fully deductible | Business correspondence |
| DOMAINE, HOSTING, CLOUDFLARE, AWS, OVH | IT infrastructure | Fully deductible | Recurring = expense; one-off high-value = capitalise |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Fully deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Fully deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Fully deductible |  |
| LICENCE LOGICIEL (perpetual, high value) | Capital item | Depreciate over useful life | Flag for reviewer -- see Tier 2 |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ENOVOS, CREOS, LEO, ELECTRICITÉ, EAU | Electricity/water | T2 if home office | 100% if dedicated office; proportional if home |
| POST TELECOM, TANGO, ORANGE LU, INTERNET | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, GSM, FORFAIT MOBILE | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LUXAIR, RYANAIR, LUFTHANSA, FLIGHT, VOL | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| CFL, TRAIN, BUS, TAXI, BOLT, UBER | Local transport | Deductible if business purpose | Public transport in LU is free; commercial fares apply abroad |
| CARBURANT, ESSENCE, SHELL, ARAL, FUEL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, VIGNETTE | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DÉJEUNER, DINNER, RÉCEPTION, CLIENT MEAL | Entertainment/representation | Restricted -- flag for reviewer | Representation costs are restricted under the LIR; treat as blocked by default |
| PERSONNEL, COURSES, CACTUS, AUCHAN, DELHAIZE, GROCERIES | Personal expenses | NOT deductible | Private living costs |
| AMENDE, PÉNALITÉ, FINE, PENALTY, STRAFE | Fines/penalties | NOT deductible | Public policy |
| ACD PAIEMENT, IMPÔT, INCOME TAX, AVANCE IMPÔT | Tax payments | NOT deductible | Income tax cannot reduce income |
| PRÉLÈVEMENT PRIVÉ, DRAWINGS, RETRAIT PERSO | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (Depreciate)

**Capital Items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, ORDINATEUR, MACBOOK, COMPUTER | Computer hardware | Depreciate (amortissement) | [RESEARCH GAP -- reviewer to confirm LIR depreciation rate] |
| IMPRIMANTE, PRINTER, SCANNER | Office equipment | Depreciate | [RESEARCH GAP -- reviewer to confirm LIR depreciation rate] |
| MOBILIER, FURNITURE, BUREAU, CHAISE | Furniture/fittings | Depreciate | [RESEARCH GAP -- reviewer to confirm LIR depreciation rate] |
| VOITURE, CAR, VÉHICULE (business) | Motor vehicle | Depreciate, business % only | [RESEARCH GAP -- reviewer to confirm LIR depreciation rate] |

> **Note.** The research data for this skill does not include statutory LIR depreciation (amortissement) rates. Do NOT invent rates. Capitalise the asset, flag the line, and require the reviewer to apply the correct useful-life / method under the LIR.

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIREMENT INTERNE, OWN ACCOUNT, ENTRE COMPTES | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRÊT, LOAN REPAYMENT, CRÉDIT | EXCLUDE | Loan principal movement |
| CCSS, COTISATIONS SOCIALES, SOCIAL SECURITY | Social-contribution deduction | Deductible as a special expense, NOT an operating expense (see Section 5) |
| TVA, VAT PAYMENT, PAIEMENT TVA | EXCLUDE | VAT liability payment, not an expense |
| AVANCE TRIMESTRIELLE, PROVISIONAL, ACOMPTE IMPÔT | Advance tax paid (credit against liability) | Not an expense -- credit against final assessment |

### 3.9 Luxembourg Banks -- Statement Format Reference

**Bank Format Reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BCEE (Spuerkeess) | VIREMENT, DOMICILIATION, CARTE, FRAIS | PDF/CSV; FR/DE descriptions; date DD/MM/YYYY |
| BIL (Banque Internationale à Luxembourg) | VIR, PRÉLÈVEMENT, PAIEMENT CARTE | PDF/CSV; counterparty in description |
| BGL BNP Paribas | VIREMENT, DOMICILIATION, ACHAT CARTE | PDF/CSV |
| ING Luxembourg | TRANSFER, DIRECT DEBIT, CARD PAYMENT | CSV/PDF; English labels common |
| Revolut / Wise (Business) | PAYMENT, TRANSFER, CONVERSION, FEE | CSV; clean counterparty names; multi-currency -- use EUR amounts |

### Example 1 -- Client Payment (VAT-registered freelancer)

**Input line:**
`15/03/2025 ; BCEE VIREMENT ; STUDIO KREBS SARL ; PAIEMENT FACT 2025-003 ; +1,170.00 ; EUR`

**Reasoning:**
Client payment for services. Freelancer is VAT-registered, so EUR 1,170 includes 17% standard VAT. Net = EUR 1,170 / 1.17 = EUR 1,000.00. EUR 170.00 is VAT collected (excluded from income -- it is a liability to the authorities). [Expatica: standard VAT 17%]

**Classification:** Gross professional income = EUR 1,000.00. VAT EUR 170.00 excluded.

### Example 2 -- SaaS Subscription (Fully Deductible)

**Input line:**
`01/04/2025 ; BIL PRÉLÈVEMENT ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD AVR ; -29.99 ; EUR`

**Reasoning:**
Monthly SaaS subscription, recurring operating expense, fully deductible. For a VAT-registered freelancer the net amount (excl. recoverable input VAT) is the expense; if under the franchise scheme, the gross amount is the cost.

**Classification:** Deductible operating expense = EUR 29.99 (or net if input VAT recoverable).

### Example 3 -- Entertainment / Representation (Restricted)

**Input line:**
`22/04/2025 ; BGL CARTE ; RESTAURANT CLAIRELUNE ; DÉJEUNER CLIENT ; -85.00 ; EUR`

**Reasoning:**
Client entertainment (frais de représentation). Representation costs are restricted under the LIR. By default this skill treats them as blocked -- no deduction without reviewer confirmation of the deductible portion under current LIR rules. [RESEARCH GAP -- reviewer to confirm the statutory deductible percentage for representation costs.]

**Classification:** NOT deductible by default. Flag for reviewer.

### Example 4 -- Self-Employed Social Contribution (CCSS)

**Input line:**
`10/01/2025 ; BCEE DOMICILIATION ; CCSS COTISATIONS ; INDÉPENDANT T4 2024 ; -2,909.34 ; EUR`

**Reasoning:**
CCSS social contribution for a self-employed person. Social contributions are deductible -- but as a **special expense (dépense spéciale)**, not as an operating expense in the income-and-expenditure account. They reduce taxable income at the return level. [PwC; Guichet.lu]

**Classification:** Social-contribution deduction = EUR 2,909.34. Do NOT include in operating expenses.

### Example 5 -- Equipment Purchase (Capital Item)

**Input line:**
`03/06/2025 ; BGL ACHAT CARTE ; APPLE STORE LUXEMBOURG ; MACBOOK PRO ; -1,899.00 ; EUR`

**Reasoning:**
Capital asset (immobilisation). Must be capitalised and depreciated over its useful life under the LIR, NOT expensed in full. The research data for this skill does not include statutory depreciation rates, so the annual charge cannot be computed here.

**Classification:** Capitalise EUR 1,899.00. [RESEARCH GAP -- reviewer to confirm LIR depreciation method and rate.] Do NOT expense in full.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BIL VIREMENT ; VIREMENT INTERNE - ÉPARGNE ; ; -2,000.00 ; EUR`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

### Example 7 -- Income Tax Estimate (Class 1, single freelancer)

**Scenario:** Single freelancer, class 1, taxable income (after social-contribution and operating-expense deductions) = EUR 45,000.

**Reasoning:**
Apply the 2025 class-1 scale. From Section 1, the cumulative tax at the top of the EUR 44,910 band is EUR 5,646.60. The remaining EUR 90.00 (45,000 − 44,910) falls in the 32% band: 90 × 32% = EUR 28.80. PIT = EUR 5,646.60 + EUR 28.80 = **EUR 5,675.40**. Solidarity surcharge at 7% (income below EUR 150,000) = EUR 5,675.40 × 7% = EUR 397.28. **Total = EUR 6,072.68.** [PwC]

**Classification:** PIT EUR 5,675.40 + surcharge EUR 397.28 = EUR 6,072.68 (estimate -- pass to the deterministic engine for the official figure).

### 5.1 Deductibility of Business Expenses

- **Deductibility of Business Expenses** — An expense is deductible only if incurred in the production of business income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Private living costs are never deductible.  _(LIR (Loi du 4 décembre 1967), provisions on dépenses d'exploitation / frais d'obtention)_

### 5.2 Revenue Recognition

- **Revenue Recognition** — All business income is professional income (bénéfice commercial / bénéfice provenant de l'exercice d'une profession libérale). For VAT-registered clients, report net of VAT. Under the small-business franchise scheme, no VAT is charged and gross is reported. VAT collected on sales is NOT income.

### 5.3 Progressive Scale and Solidarity Surcharge

- **Progressive Scale and Solidarity Surcharge** — PIT is progressive over 23 bands from 0% to 42% (Section 1). On top of the PIT computed, the employment-fund (solidarity) surcharge applies: 7% of the PIT, rising to 9% where taxable income exceeds EUR 150,000 (classes 1 and 1a) or EUR 300,000 (class 2).  _(LIR barème (2025, 2.5 index-bracket adjustment); [PwC])_

### 5.4 Tax Classes

- **Tax Classes** — Three classes (Section 1): class 1 (single, full scale), class 1a (single with dependent child / widowed / 65+, more favourable), class 2 (married/partnered joint taxation with income-splitting, most favourable). Never apply a class without confirmation; default to class 1.  _([PwC])_

### 5.5 Social Contributions -- Employee

**Social Contributions Employee table**  _([Guichet.lu; PwC])_

| Contribution | Employee Rate | Base | Capped at ceiling? |
| --- | --- | --- | --- |
| Pension / old-age (assurance pension) | 8.00% | gross remuneration | Yes |
| Health -- benefits in kind (CNS, prestations en nature) | 2.80% | gross remuneration | Yes |
| Health -- cash benefits (CNS, prestations en espèces) | 0.25% | gross remuneration | Yes |
| Dependency / long-term care (assurance dépendance) | 1.40% | gross income less EUR 675.94/month abatement | **No -- uncapped** |
| **Employee total** | **12.45%** | -- | -- |

- **Dependency contribution abatement** — The dependency contribution applies the EUR 675.94/month abatement (EUR 8,045.32/year for 2025) and is NOT subject to the ceiling. (Component check: 8.00 + 2.80 + 0.25 + 1.40 = 12.45%.)  _([PwC])_

### 5.6 Social Contributions -- Employer

**Social Contributions Employer table**  _([Guichet.lu])_

| Contribution | Employer Rate | Notes |
| --- | --- | --- |
| Pension / old-age | 8.00% |  |
| Health -- benefits in kind | 2.80% |  |
| Health -- cash benefits | 0.25% |  |
| Accident insurance (AAA) | 0.75% | × bonus/malus coefficient 0.85–1.5 by risk class |
| Occupational health (santé au travail / STM) | 0.14% |  |
| Employers' mutual insurance (MDE) | class I 0.72% / II 1.22% / III 1.46% / IV 2.84% | class set by prior-year financial absenteeism rate (I <0.65%, II <1.60%, III <2.50%, IV >2.50%) |
| **Employer subtotal (excl. MDE), accident coeff 1.0** | **11.94%** | (8.00 + 2.80 + 0.25 + 0.75 + 0.14) |
| **Employer total at MDE class II** | **13.16%** | (11.94 + 1.22) |

- **Firm-specific defaults** — The accident coefficient and MDE class are firm-specific; assume coefficient 1.0 and MDE class II–III where unknown. Approximate employer total social cost is roughly 12–15% of gross. [RESEARCH GAP -- the live CCSS schedule (ccss.public.lu) returned HTTP 403; cross-check MDE class rates against the current CCSS schedule.]  _([Guichet.lu; Rivermate])_

### 5.7 Social Contributions -- Self-Employed (Indépendants)

**Social Contributions Self-Employed table**  _([Baloise; PwC])_

| Contribution | Self-Employed Rate | Notes |
| --- | --- | --- |
| Pension (16% = 8% employee + 8% employer, both borne by the indépendant) | 16.00% | capped at ceiling |
| Health -- benefits in kind | 5.60% | capped at ceiling |
| Health -- cash benefits | 0.50% | capped at ceiling |
| Dependency / long-term care | 1.40% | on income less EUR 675.94/month abatement; uncapped |
| **Component sum (this skill's figures)** | **23.50%** | (16.00 + 5.60 + 0.50 + 1.40) |

> **[RESEARCH GAP -- reviewer to confirm.]** The research data states a self-employed **total of ~24.5%**, but its own component breakdown (pension 16% + health-in-kind 5.6% + health-cash 0.5% + dependency 1.4%) sums to **23.5%** -- a 1.0 percentage-point discrepancy that the source itself flags ("confirm exact health split with CCSS"). Accident insurance may also apply on top. Do NOT publish a single self-employed rate to a client without the reviewer confirming the exact CCSS combined rate and whether accident cover is added. Base = net professional income, capped at 5× the social minimum wage (max monthly EUR 13,518.68 from May 2025; annual EUR 162,224.16); dependency uncapped. [Baloise; PwC]

### 5.8 Social-Contribution Ceiling (Plafond Cotisable)

**Social-Contribution Ceiling table**  _([Orbitax])_

| Period | Monthly ceiling | Annual (May 2025 onward) |
| --- | --- | --- |
| 1 Jan – 30 Apr 2025 | EUR 13,188.96 | -- |
| From 1 May 2025 | EUR 13,518.68 | EUR 162,224.16 |

- **Ceiling basis** — Ceiling = 5× the social minimum wage (salaire social minimum, SSM). Changed mid-year with the 1 May 2025 indexation. Default to the May 2025 figure for full-year estimates; note the split-year nuance.  _([Orbitax])_

### 5.9 Social Minimum Wage (SSM) and Tax Credits

**SSM table**  _([Orbitax])_

| Item | Jan 2025 | May 2025 | Source |
| --- | --- | --- | --- |
| SSM unskilled (18+), monthly | EUR 2,637.79 | EUR 2,703.74 | [Orbitax] |
| SSM skilled (qualifié), monthly (+20%) | EUR 3,165.35 | EUR 3,244.48 | [All Eyes On Me] |

**Tax credit table**  _([PwC])_

| Tax credit | Amount | Notes | Source |
| --- | --- | --- | --- |
| Employee tax credit (CIS -- crédit d'impôt salarié) | EUR 0–600/year by income | granted from ~EUR 936 gross annual; phased out above ~EUR 80,000 | [PwC] |
| Minimum-wage tax credit (CISSM) | EUR 81.00/month for monthly gross EUR 1,800–3,000; degressive 81/600 × (3,600 − gross) between EUR 3,000–3,600 | prorated for part-time; ensures a worker on the unskilled SSM has no PIT in all classes | [PwC] |
| Single-parent tax credit (CIM) | EUR 750–3,504/year |  | [PwC; Guichet.lu] |

### 5.10 Wage-Tax Withholding (Employees)

- **Wage-Tax Withholding** — The employer withholds wage tax (retenue sur traitements et salaires) per the tax card (fiche de retenue, on the RTS scale) plus social contributions monthly. The tax class on the card determines the scale applied. Employees not required to file a full return may file Form 163 (décompte annuel) to claim refunds.  _([PwC; Guichet.lu])_

### 5.11 Filing, Advances, and Penalties

**Filing, Advances, and Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Annual return | Form 100 (modèle 100), electronic via MyGuichet.lu | [Guichet.lu] |
| Filing deadline | 31 December of the year following the income year; income year 2025 due 31 Dec 2026 (window opens 7 Apr 2026) | [Guichet.lu] |
| Annual adjustment (employees) | Form 163, by 31 December of the year following | [Guichet.lu] |
| Self-employed quarterly advances (avances) | 10 March, 10 June, 10 September, 10 December of the tax year | [Expatica; Guichet.lu] |
| Final payment | Balance due within 1 month of the assessment notice (bulletin d'impôt) | [Guichet.lu] |
| Late-filing surcharge (majoration) | up to 10% of the tax due; plus a fine (astreinte/amende) up to EUR 25,000 | [taxx.lu] |
| Late-payment interest | 0.6% per month (7.2% per annum) on tax unpaid by the due date | [taxx.lu] |

### 5.12 VAT Interaction

**VAT Interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income -- exclude from professional income |
| Input VAT recovered (registered) | NOT an expense -- exclude from operating expenses |
| Input VAT blocked/non-deductible | IS an expense -- include the blocked VAT |
| Franchise-scheme client (turnover ≤ EUR 50,000) | No VAT charged; record purchases gross |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross is cost |

- **VAT registration threshold and rates** — VAT registration is compulsory above EUR 50,000 annual turnover (franchise threshold raised to EUR 50,000 from 1 Jan 2025). Rates: standard 17%, intermediate 14%, reduced 8%, super-reduced 3%.  _([Expatica])_

### 6.1 Home Office Deduction

- Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total rooms or floor area)
- Apply that percentage to rent, electricity, water, internet, maintenance
- Must be a genuinely dedicated workspace -- a dual-use room does NOT qualify
- Retain the calculation in the client's records

**Conservative default:** 0% deduction until reviewer confirms the arrangement.

**Flag for reviewer:** Confirm room count / floor-area basis and that the workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible
- Client must maintain a mileage log (business vs total kilometres)
- Depreciation on the vehicle is on a useful-life basis × business %

**Conservative default:** 0% business use until a mileage log is provided. [RESEARCH GAP -- reviewer to confirm LIR depreciation rate for vehicles.]

### 6.3 Phone / Internet Mixed Use

- Business-use portion only; client must provide a reasonable estimate

**Conservative default:** 0% deduction until business percentage confirmed.

### 6.4 Representation / Entertainment Costs

- Representation costs (frais de représentation) are restricted under the LIR
- This skill blocks them by default

**Flag for reviewer:** Confirm the statutory deductible percentage. [RESEARCH GAP -- reviewer to confirm.]

### 6.5 Depreciation of Capital Assets (Amortissement)

- All business assets must be capitalised and depreciated over their useful life
- The research data does not include statutory LIR depreciation rates

**Flag for reviewer:** Apply the correct LIR method (linear / declining-balance) and useful life. [RESEARCH GAP -- reviewer to confirm rates.]

### 6.6 Self-Employed Combined Social Rate

- The exact self-employed combined CCSS rate (and whether accident insurance is added) is not settled in the research data (Section 5.7)

**Flag for reviewer:** Confirm the combined rate against the live CCSS schedule before quoting it.

### 6.7 Split-Year Social Parameters

- The SSM and contribution ceiling changed on 1 May 2025; Jan–Apr and May–Dec figures differ

**Flag for reviewer:** Confirm whether the period split materially affects the estimate for clients near the ceiling.

## Section 7 -- Excel Working Paper Template

```
LUXEMBOURG INCOME TAX -- FORM 100 WORKING PAPER
Income Year: 2025
Client: ___________________________
Tax Class: 1 / 1a / 2        Status: Self-employed (indépendant) / Employee

A. PROFESSIONAL INCOME (bénéfice)
  A1. Client payments (net of VAT if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)       ___________
  A3. Other business income                          ___________
  A4. TOTAL professional income                      ___________

B. OPERATING EXPENSES (dépenses d'exploitation)
  B1. Office rent                                    ___________
  B2. Professional insurance                         ___________
  B3. Accountancy / legal / fiduciaire fees          ___________
  B4. Office supplies                                ___________
  B5. Software subscriptions                         ___________
  B6. Marketing / advertising                        ___________
  B7. Bank charges / payment processing fees         ___________
  B8. Training / CPD / professional subs             ___________
  B9. Travel (flights, hotels, transport)            ___________
  B10. Telecoms (business % of phone/internet)       ___________
  B11. Home office (% of utilities/rent)             ___________
  B12. Vehicle expenses (business %)                 ___________
  B13. Depreciation (amortissement) [reviewer rate]  ___________
  B14. Other allowable expenses                      ___________
  B15. TOTAL operating expenses                      ___________

C. NET PROFESSIONAL PROFIT (A4 - B15)                ___________

D. OTHER INCOME
  D1. Employment income (wage tax already withheld)  ___________
  D2. Rental income                                  ___________
  D3. Investment income                              ___________
  D4. TOTAL other income                             ___________

E. SPECIAL EXPENSES / DEDUCTIONS (dépenses spéciales)
  E1. CCSS social contributions paid                 ___________
  E2. Other deductible special expenses              ___________
  E3. TOTAL special expenses                         ___________

F. TAXABLE INCOME (C + D4 - E3)                       ___________

G. TAX COMPUTATION (pass to deterministic engine)
  G1. PIT from 2025 scale (Section 1)                ___________
  G2. Solidarity surcharge (7% / 9%)                 ___________
  G3. Tax credits (CIS / CISSM / CIM)                ___________
  G4. Advance payments made                          ___________
  G5. Tax due / refund (G1 + G2 - G3 - G4)           ___________

REVIEWER FLAGS:
  [ ] Tax class confirmed (1 / 1a / 2)?
  [ ] VAT registration / franchise scheme confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Depreciation rates applied per LIR?
  [ ] Self-employed CCSS combined rate confirmed?
  [ ] Social ceiling / SSM split-year handled?
  [ ] CCSS as special expense (not operating expense)?
  [ ] Representation costs treatment confirmed?
```

### Luxembourg Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BCEE (Spuerkeess) | PDF, CSV | Date, Libellé/Description, Débit, Crédit, Solde | Most common; FR/DE descriptions |
| BIL | PDF, CSV | Date valeur, Libellé, Montant, Solde | Counterparty in description |
| BGL BNP Paribas | PDF, CSV | Date, Opération, Débit, Crédit, Solde | Card transactions show merchant |
| ING Luxembourg | PDF, CSV | Date, Description, Amount, Balance | English labels common |
| Revolut / Wise Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency -- use EUR |

### Key Luxembourg / French / German Banking Terms

**Banking Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| VIREMENT / VIR / ÜBERWEISUNG | Transfer | Check direction for income/expense |
| DOMICILIATION / PRÉLÈVEMENT / LASTSCHRIFT | Direct debit | Regular expense (utility, subscription) |
| ORDRE PERMANENT / DAUERAUFTRAG | Standing order | Regular expense (rent, loan) |
| CARTE / KARTE / ACHAT CARTE | Card payment | Expense -- check merchant |
| CRÉDIT / GUTSCHRIFT | Credit | Potential income |
| FRAIS / SPESEN | Bank charges | Deductible operating expense |
| INTÉRÊTS / ZINSEN | Interest | Interest income or bank charge |
| RETRAIT / ATM | Cash withdrawal | Ask what cash was spent on |
| CCSS | Social-security body | Social-contribution deduction (special expense) |
| ACD / AED | Tax authorities | Tax payment / refund -- not income/expense |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- LUXEMBOURG INCOME TAX
1. Tax class: 1 (single), 1a (single with child / widowed / 65+), or 2 (married/partnered joint)?
2. Status: fully self-employed (indépendant) or employee (or both)?
3. VAT: registered (turnover > EUR 50,000) or franchise scheme?
4. Home office: dedicated room or shared space? If dedicated, what % of floor area?
5. Vehicle: do you use a car for business? What % is business use? Mileage log kept?
6. Phone/internet: what % is business use?
7. CCSS social contributions: total amount paid in the income year?
8. Advance tax payments: total paid in the year (10 Mar / Jun / Sep / Dec)?
9. Any other income (employment, rental, dividends, interest)?
10. Any capital assets purchased during the year (for depreciation)?
11. Dependent children / family situation (affects class 1a/2 and CIM credit)?
```

## Section 10 -- Reference Material

### Key Legislation and Authority References

**Key Legislation and Authority References**  _(LIR -- Loi modifiée du 4 décembre 1967; Code de la sécurité sociale; CCSS)_

| Topic | Reference | Source |
| --- | --- | --- |
| Income tax law (barème, classes, deductions) | LIR -- Loi modifiée du 4 décembre 1967 | [PwC] |
| Social contributions | Code de la sécurité sociale; CCSS | [Guichet.lu] |
| 2025 scale (2.5 index-bracket adjustment) | Loi du 12 juillet 2024 + budget/index laws | [PwC] |
| Annual return | Form 100 (modèle 100), MyGuichet.lu | [Guichet.lu] |
| Employee annual adjustment | Form 163 (décompte annuel) | [Guichet.lu] |
| Direct tax authority | Administration des contributions directes (ACD) | [Guichet.lu] |
| Social-security authority | Centre commun de la sécurité sociale (CCSS); CNS; CNAP | [Guichet.lu] |
| Penalties | Late filing up to 10% + fine up to EUR 25,000; interest 0.6%/month | [taxx.lu] |

### Key Numbers at a Glance (2025)

**Key Numbers at a Glance (2025)**  _([PwC]; [Guichet.lu]; [Orbitax]; [Expatica]; [Baloise])_

| Item | Value | Source |
| --- | --- | --- |
| PIT tax-free threshold (class 1) | EUR 13,230 | [PwC] |
| Top marginal rate | 42% above EUR 234,870 | [PwC] |
| Solidarity surcharge | 7% (9% above EUR 150,000 class 1/1a; EUR 300,000 class 2) | [PwC] |
| Employee social total | 12.45% | [Guichet.lu; PwC] |
| Employer social total (excl. MDE, coeff 1.0) | 11.94% | [Guichet.lu] |
| Self-employed component sum | 23.50% (research states ~24.5% total -- see Section 5.7 gap) | [Baloise; PwC] |
| Dependency abatement | EUR 675.94/month (EUR 8,045.32/year) | [PwC] |
| Social ceiling (from 1 May 2025) | EUR 13,518.68/month (EUR 162,224.16/year) | [Orbitax] |
| SSM unskilled (from 1 May 2025) | EUR 2,703.74/month | [Orbitax] |
| VAT registration threshold | EUR 50,000 turnover | [Expatica] |

### Caveats and Open Items (from research)

- Employer accident insurance (0.75%) is modulated by a firm-specific bonus/malus coefficient (0.85–1.5); MDE class (0.72%/1.22%/1.46%/2.84%) depends on prior-year absenteeism. Exact employer cost varies by employer. The live CCSS schedule (ccss.public.lu/en/parametres-sociaux.html) returned HTTP 403 and could not be fetched; cross-check the MDE class rates against the current CCSS schedule. [RESEARCH GAP -- reviewer to confirm against CCSS.]
- Social parameters changed at 1 May 2025 (indexation): SSM and ceiling differ between Jan–Apr and May–Dec.
- The self-employed health split (5.60% in-kind + 0.50% cash) and the ~24.5% headline come from an insurer source (Baloise) plus PwC component rates, not a single official CCSS table; the components sum to 23.5%. [RESEARCH GAP -- reviewer to confirm.]
- One secondary source cited a different first-bracket figure (EUR 12,438) reflecting a pre-2025 or class-specific scale; the EUR 13,230 figure (PwC, post-2.5-index-adjustment class-1 scale) is used here.
- The 42% top-rate threshold appears as EUR 234,870 in the detailed PwC table and as EUR 200,004 / EUR 234,900 in some summaries; EUR 234,870 is the working figure. [RESEARCH GAP -- verify against the official ACD barème before relying on it for high incomes.]
- Statutory LIR depreciation (amortissement) rates are NOT in the research data. [RESEARCH GAP -- reviewer to confirm.]

### Test Suite

#### Test 1 -- Single freelancer, mid-range income.

Input: Class 1, taxable income EUR 45,000.
Expected: PIT = EUR 5,675.40 (cum. EUR 5,646.60 at EUR 44,910 + EUR 90 × 32% = EUR 28.80). Surcharge 7% = EUR 397.28. Total = EUR 6,072.68.

#### Test 2 -- Single freelancer at top of 0% band.

Input: Class 1, taxable income EUR 13,230.
Expected: PIT = EUR 0.00. Surcharge = EUR 0.00. Total = EUR 0.00 (threshold fully within the 0% band).

#### Test 3 -- Single, EUR 60,000.

Input: Class 1, taxable income EUR 60,000.
Expected: PIT = EUR 11,164.50 (cum. EUR 8,859.60 at EUR 54,090 + EUR 5,910 × 39% = EUR 2,304.90). Surcharge 7% = EUR 781.52 (EUR 781.515 rounded). Total = EUR 11,946.02.

#### Test 4 -- Higher-rate surcharge threshold.

Input: Class 1, taxable income EUR 150,000.
Expected: PIT = EUR 46,590.00 (cum. EUR 33,570.00 at EUR 117,450 + EUR 32,550 × 40% = EUR 13,020.00). Surcharge 7% (income not above EUR 150,000) = EUR 3,261.30. Total = EUR 49,851.30. Above EUR 150,000 the surcharge steps up to 9%.

#### Test 5 -- Employee monthly social contributions.

Input: Employee, monthly gross EUR 4,000 (below ceiling).
Expected: capped contributions (pension 8% + health 2.8% + 0.25% = 11.05% × 4,000) = EUR 442.00; dependency 1.4% × (4,000 − 675.94) = EUR 46.54. Total employee SSC = EUR 488.54.

#### Test 6 -- Dependency contribution uses abatement and is uncapped.

Input: Annual professional income EUR 60,000.
Expected: dependency base = 60,000 − 8,045.32 = EUR 51,954.68; × 1.4% = EUR 727.37. (No ceiling applied to dependency.)

#### Test 7 -- VAT extraction on income (registered).

Input: Client payment EUR 1,170 gross, standard 17% VAT.
Expected: net income = EUR 1,000.00; VAT EUR 170.00 excluded.

#### Test 8 -- CCSS classified as special expense, not operating expense.

Input: CCSS payment EUR 2,909.34 placed in the operating-expense column.
Expected: Move to special-expense deduction (E1). Do NOT include in operating expenses.

## PROHIBITIONS

- NEVER apply a rate table without knowing the tax class -- default to class 1 and flag
- NEVER compute final tax figures as definitive -- always pass taxable income to the deterministic engine and label outputs as estimated
- NEVER omit the employment-fund (solidarity) surcharge on PIT
- NEVER apply the 9% surcharge below EUR 150,000 (class 1/1a) or EUR 300,000 (class 2)
- NEVER publish a single self-employed CCSS rate without reviewer confirmation (component sum 23.5% vs stated ~24.5%)
- NEVER treat CCSS contributions as an operating expense -- they are a special-expense deduction
- NEVER include VAT collected on sales in income for VAT-registered clients
- NEVER expense a capital asset in full -- capitalise and depreciate per the LIR
- NEVER invent depreciation (amortissement) rates -- they are a research gap; flag for the reviewer
- NEVER allow personal living costs, fines, penalties, or income tax itself as a deduction
- NEVER apply the dependency-insurance ceiling -- that contribution is uncapped
- NEVER mix the Jan–Apr and May 2025 social ceilings without noting the split

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
