---
name: luxembourg-income-tax
description: Use this skill whenever asked about Luxembourg personal income tax for self-employed individuals (indépendants) and individuals. Trigger on phrases like "how much tax do I pay in Luxembourg", "déclaration d'impôt", "Form 100", "modèle 100", "tax class", "classe d'impôt", "barème", "revenu imposable", "solidarity surcharge", "employment fund", "fonds pour l'emploi", "CCSS contributions", "cotisations sociales", "self-employed tax Luxembourg", "indépendant", "advance tax payments", "avances trimestrielles", "salaire social minimum", or any question about filing or computing Luxembourg income tax for a self-employed or individual client. Also trigger when preparing or reviewing a Form 100 / Form 163 return, computing deductible business expenses, estimating social contributions, or advising on quarterly advance payments. This skill covers the 23-band progressive PIT scale (0%–42%), the employment-fund (solidarity) surcharge, tax classes 1/1a/2, CCSS social contributions (employee, employer, self-employed), Form 100 structure, advance payments, penalties, and interaction with VAT and the social-security ceiling. ALWAYS read this skill before touching any Luxembourg income tax work.
version: 0.2
jurisdiction: LU
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
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
| Tax year | Calendar year (1 January -- 31 December) [LIR art. 1(2)](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Primary legislation | Loi modifiée du 4 décembre 1967 concernant l'impôt sur le revenu (LIR / Income Tax Law) |
| Supporting legislation | Code de la sécurité sociale (social contributions); LIR art. 118 as amended by the law of 20 December 2024 (scale applicable from tax year 2025, unchanged in the LIR text in force on 1 January 2026) |
| Direct-tax authority | Administration des contributions directes (ACD) |
| Social-security authority | Centre commun de la sécurité sociale (CCSS); health fund Caisse nationale de santé (CNS); pension fund Caisse nationale d'assurance pension (CNAP) |
| Filing portal | MyGuichet.lu (guichet.public.lu) |
| Annual return | Form 100 (modèle 100) -- déclaration pour l'impôt sur le revenu des personnes physiques [ACD, formulaires personnes physiques](https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html) |
| Filing deadline | 31 December of the year following the income year; income year 2026 due 31 December 2027 [ACD, délais de dépôt](https://impotsdirects.public.lu/fr/az/d/delais/depot.html) |
| Verified by | Pending -- requires sign-off by a Luxembourg-qualified tax adviser / expert-comptable |
| Verification date | Pending |
| Skill version | 0.2 |

### Tax Rate Brackets -- Progressive Scale (barème) for tax years 2025 and 2026, Tax Class 1

**Progressive Scale Tax Class 1 (LIR art. 118; taxable income rounded down to a multiple of EUR 50 first, art. 126(2))**  _([LIR, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf))_

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

- **Tax-free threshold** — The first EUR 13,230 of taxable income (class 1) is taxed at 0%. There is no separate flat personal allowance; the 0% band IS the allowance.  _(LIR art. 118)_

### Employment-Fund (Solidarity) Surcharge

**Employment-Fund Surcharge table**  _([ACD, Fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html))_

| Adjusted taxable income | Surcharge on PIT (classes 1 and 1a) | Surcharge on PIT (class 2) |
| --- | --- | --- |
| Up to threshold | 7% | 7% |
| Above EUR 150,000 (class 1/1a) / EUR 300,000 (class 2) | 9% | 9% |

- **Surcharge application** — Applied on top of the PIT computed from the scale above. The rate is 7%, or 9% where adjusted taxable income exceeds EUR 150,000 (classes 1 and 1a) or EUR 300,000 (class 2), since tax year 2013.  _([ACD, Fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html))_

### Tax Classes

**Tax Classes table**  _(LIR arts. 119 to 121)_

| Class | Who | Treatment |
| --- | --- | --- |
| Class 1 | Single / individually taxed, no dependent child | Full progressive scale, no splitting -- least favourable |
| Class 1a | Single with a child giving a child tax reduction, widowed, or aged 64 or over at the start of the tax year (art. 119 no. 2) | More favourable scale |
| Class 2 | Spouses taxed jointly (art. 3), partners taxed jointly (art. 3bis), and people widowed, divorced or separated in the three preceding years (art. 119 no. 3) | Tax = twice the tax on half the income (art. 121) -- most favourable |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown tax class | Class 1 (single, no children) -- highest, most conservative outcome (see Section 1A) |
| Solidarity surcharge rate | 7% on PIT (9% only if taxable income > EUR 150,000 class 1/1a or > EUR 300,000 class 2) |
| Social-contribution ceiling | EUR 13,518.68/month from 1 January 2026 and EUR 13,856.63/month from 1 June 2026 (CCSS); use the figure for the month |
| Employer MDE class / accident coefficient | MDE class II–III and accident coefficient 1.0 (0.75%) where firm-specific data unknown |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT status | Assume VAT is charged (turnover above EUR 50,000) unless the client confirms the franchise scheme |

### Section 1A -- Why default to Class 1

Classes 1a and 2 give more favourable treatment via splitting and abatements. Defaulting to class 1 avoids overstating reliefs and gives the highest (most conservative) tax estimate for a single individual. Never silently assume class 2 or 1a -- it materially understates tax.

### Required Inputs

**Minimum viable** -- bank statement for the full income year in CSV, PDF, or pasted text, plus confirmation of tax class (1 / 1a / 2) and status (self-employed indépendant filing by assessment, or employee). For employees not filing a full return, confirm whether a Form 163 annual adjustment applies.

**Recommended** -- all sales invoices, purchase invoices/receipts, CCSS contribution statements, prior year Form 100 or tax assessment (bulletin d'impôt), VAT registration status (registered / franchise scheme).

**Ideal** -- complete income and expenditure account (compte de résultat), asset register with depreciation schedule, quarterly advance-payment confirmations, employment income (fiche de retenue / tax card) details, family situation (dependent children, age, marital/partnership status).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Form 100 working paper was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that expenses were incurred in the production of income (frais d'obtention / dépenses d'exploitation)."

### Refusal Catalogue

- **R-LU-1 -- Tax class unknown** — Tax class (classe d'impôt 1, 1a, or 2) determines how the progressive scale and the solidarity-surcharge threshold are applied. This skill defaults to class 1 (most conservative) but flags the result. Confirm class before relying on the figure.
- **R-LU-2 -- Companies, partnerships, holding structures** — This skill covers individuals and sole-trader/liberal-profession indépendants only. Sociétés (SARL, SA), SOPARFI holdings, and partnerships file separate returns (corporate income tax / municipal business tax / net wealth tax). Escalate to a Luxembourg tax adviser.
- **R-LU-3 -- Non-resident / cross-border (frontalier) taxation** — Non-resident and cross-border (French/German/Belgian frontalier) taxation, the 34-day treaty thresholds and the 90% rule for assimilation to resident treatment are out of scope here. Use `lu-cross-border`.
- **R-LU-4 -- Capital gains / property disposals** — Capital gains (plus-values) on real estate or substantial shareholdings have separate rules and rates. Escalate to a Luxembourg tax adviser.
- **R-LU-5 -- Impatriate / expat regimes** — The impatriate regime (art. 115 no. 13b) is covered by `lu-cross-border`. The participative premium (prime participative) and stock-option/profit-sharing schemes have specific conditions and are out of scope. Escalate to a Luxembourg tax adviser.
- **R-LU-6 -- Arrears / enforcement** — Client has outstanding tax arrears or is subject to ACD enforcement. Late-payment interest runs at 0.6% per month and a late-filing surcharge of up to 10% can be set. Do not advise -- escalate immediately.  _([ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html))_
- **R-LU-7 -- VAT return requested** — This skill covers personal income tax (Form 100 / Form 163) only. For Luxembourg VAT, use the dedicated VAT skill. Standard VAT rate 17%, intermediate 14%, reduced 8%, super-reduced 3%. The small-business franchise (no VAT charged) applies up to EUR 50,000 of annual turnover from 1 January 2025, with a 10% tolerance to EUR 55,000 for the year in which the threshold is crossed; the next year the franchise is lost (LTVA arts. 57 to 57quater).  _([AED, taux nationaux](https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html); [AED, régime de franchise SME](https://pfi.public.lu/fr/professionnel/tva/sme.html))_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**What the patterns rest on.** The bank-text patterns are matching aids, not law. Every treatment in the tables follows one of these LIR rules (consolidated text at 1 January 2026): an expense is deductible only if it is caused exclusively by the business (art. 45(1)); household and lifestyle spending, gifts (libéralités), income tax and fines are never deductible (art. 12 nos. 1 to 4); depreciable assets are written off over their useful life (art. 32) unless they cost EUR 870 or less or last one year or less (art. 34); compulsory social contributions are special expenses (art. 110). A merchant name alone never decides business use: where a row says "business purpose", the client must confirm it.

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
| AIDE, SUBVENTION, GRANT | Check nature | Check nature | A public subsidy tied directly to buying an asset reduces that asset's acquisition price (ACD circular L.I.R. n° 34/1); an operating subsidy is business income |

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
| CFL, TRAIN, BUS, TAXI, BOLT, UBER | Local transport | Deductible if business purpose | Home-to-work travel is limited by LIR art. 46 no. 9 and its grand-ducal regulation; do not book it here |
| CARBURANT, ESSENCE, SHELL, ARAL, FUEL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, VIGNETTE | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DÉJEUNER, DINNER, RÉCEPTION, CLIENT MEAL | Entertainment/representation | Deductible only with a documented business purpose (art. 45(1)); otherwise NOT deductible | The LIR sets no fixed percentage. Lifestyle spending tied to the client's social position is not deductible even if it helps the business (art. 12 no. 1); the client's own share of a meal is private |
| PERSONNEL, COURSES, CACTUS, AUCHAN, DELHAIZE, GROCERIES | Personal expenses | NOT deductible | Private living costs (art. 12 no. 1) |
| AMENDE, PÉNALITÉ, FINE, PENALTY, STRAFE | Fines/penalties | NOT deductible | LIR art. 12 no. 4 |
| ACD PAIEMENT, IMPÔT, INCOME TAX, AVANCE IMPÔT | Tax payments | NOT deductible | Income tax and net wealth tax (art. 12 no. 3a) |
| PRÉLÈVEMENT PRIVÉ, DRAWINGS, RETRAIT PERSO | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (Depreciate)

**Capital Items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, ORDINATEUR, MACBOOK, COMPUTER | Computer hardware | EUR 870 or less per item: write off in the year of purchase (art. 34); above: depreciate over useful life (art. 32) | Linear or declining balance |
| IMPRIMANTE, PRINTER, SCANNER | Office equipment | Same EUR 870 test, then depreciate | Linear or declining balance |
| MOBILIER, FURNITURE, BUREAU, CHAISE | Furniture/fittings | Same EUR 870 test, then depreciate | Linear or declining balance |
| VOITURE, CAR, VÉHICULE (business) | Motor vehicle | Depreciate, business % only | Linear or declining balance |

> **Note.** The LIR and the ACD publish no table of rates per asset type. The rate follows from the useful life (durée usuelle d'utilisation) of the asset, set in years from its kind and conditions of use (art. 32(2)). See Section 6.5 for the method and the fixed limits.

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
Client payment for services. Freelancer is VAT-registered, so EUR 1,170 includes 17% standard VAT. Net = EUR 1,170 / 1.17 = EUR 1,000.00. EUR 170.00 is VAT collected (excluded from income -- it is a liability to the authorities). ([AED, taux nationaux](https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html): standard rate 17%)

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
Client entertainment (frais de représentation). The LIR has no fixed deductible percentage for representation costs. The test is art. 45(1): the expense is deductible only if the business alone caused it. Art. 12 no. 1 blocks lifestyle spending linked to the client's economic or social position, even when it helps the business. So ask who attended and why. If the client documents a named business contact and a business purpose, deduct the cost; if not, it is private.

**Classification:** NOT deductible until the client documents the guest and the business purpose; then deductible as an operating expense.

### Example 4 -- Self-Employed Social Contribution (CCSS)

**Input line:**
`10/01/2025 ; BCEE DOMICILIATION ; CCSS COTISATIONS ; INDÉPENDANT T4 2024 ; -2,909.34 ; EUR`

**Reasoning:**
CCSS social contribution for a self-employed person. Social contributions are deductible -- but as a **special expense (dépense spéciale)**, not as an operating expense in the income-and-expenditure account. They reduce taxable income at the return level. Art. 110 no. 2 allows a self-employed person's compulsory health, accident and pension contributions; the dependency-insurance contribution is not on that list, so take it out of the deduction. (LIR art. 110)

**Classification:** Social-contribution deduction = EUR 2,909.34. Do NOT include in operating expenses.

### Example 5 -- Equipment Purchase (Capital Item)

**Input line:**
`03/06/2025 ; BGL ACHAT CARTE ; APPLE STORE LUXEMBOURG ; MACBOOK PRO ; -1,899.00 ; EUR`

**Reasoning:**
Capital asset (immobilisation). The price is above EUR 870, so the art. 34 immediate write-off does not apply. Capitalise it and depreciate it over its useful life (art. 32). The acquisition price excludes input VAT the client can deduct, and includes VAT the client cannot deduct (ACD circular L.I.R. n° 34/1). If the client documents a useful life of 4 years and is not VAT-registered, the linear charge is 1,899.00 / 4 = EUR 474.75 a year. The declining-balance rate would be capped at the lower of 3 x 25% and 30%, so 30%.

**Classification:** Capitalise EUR 1,899.00 (net of deductible VAT if registered). Depreciate over the documented useful life. Do NOT expense in full.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BIL VIREMENT ; VIREMENT INTERNE - ÉPARGNE ; ; -2,000.00 ; EUR`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

### Example 7 -- Income Tax Estimate (Class 1, single freelancer)

**Scenario:** Single freelancer, class 1, taxable income (after social-contribution and operating-expense deductions) = EUR 45,000.

**Reasoning:**
Apply the class-1 scale (art. 118, the same for 2025 and 2026). From Section 1, the cumulative tax at the top of the EUR 44,910 band is EUR 5,646.60. The remaining EUR 90.00 (45,000 − 44,910) falls in the 32% band: 90 × 32% = EUR 28.80. PIT = EUR 5,646.60 + EUR 28.80 = **EUR 5,675.40**. Solidarity surcharge at 7% (income below EUR 150,000) = EUR 5,675.40 × 7% = EUR 397.28. **Total = EUR 6,072.68.** (LIR art. 118; ACD, Fonds pour l'emploi)

**Classification:** PIT EUR 5,675.40 + surcharge EUR 397.28 = EUR 6,072.68 (estimate -- pass to the deterministic engine for the official figure).

### 5.1 Deductibility of Business Expenses

- **Deductibility of Business Expenses** — An expense is deductible only if it is caused exclusively by the business (art. 45(1)); expenses linked to exempt income are not deductible (art. 45(2)). Mixed-use expenses must be apportioned on a reasonable, documented basis. Household and lifestyle costs, gifts (libéralités), income tax, net wealth tax and fines are never deductible (art. 12 nos. 1 to 4). Pay to the operator or to a spouse taxed jointly with them is not an expense (art. 48 no. 3).  _([LIR, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf), arts. 12, 45, 48)_
- **Representation costs and gifts** — The LIR sets no fixed percentage. Client meals and receptions are deductible only where the business alone caused them (art. 45(1)). Spending driven by the client's social or economic position is private even if it helps the business (art. 12 no. 1). Gratuitous gifts (libéralités) are not deductible (art. 12 no. 2).  _([LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf), arts. 12 and 45)_

### 5.2 Revenue Recognition

- **Revenue Recognition** — All business income is professional income (bénéfice commercial / bénéfice provenant de l'exercice d'une profession libérale). For VAT-registered clients, report net of VAT. Under the small-business franchise scheme, no VAT is charged and gross is reported. VAT collected on sales is NOT income.

### 5.3 Progressive Scale and Solidarity Surcharge

- **Progressive Scale and Solidarity Surcharge** — PIT is progressive over 23 bands from 0% to 42% (Section 1). On top of the PIT computed, the employment-fund (solidarity) surcharge applies: 7% of the PIT, rising to 9% where taxable income exceeds EUR 150,000 (classes 1 and 1a) or EUR 300,000 (class 2).  _(LIR art. 118; [ACD, Fonds pour l'emploi](https://impotsdirects.public.lu/fr/az/f/fond_empl.html))_

### 5.4 Tax Classes

- **Tax Classes** — Three classes (Section 1): class 1 (single, full scale), class 1a (single with a child tax reduction / widowed / aged 64 or over at the start of the year, more favourable), class 2 (spouses or partners taxed jointly, and the widowed, divorced or separated within three years; twice the tax on half the income, most favourable). Never apply a class without confirmation; default to class 1.  _(LIR arts. 119 to 121)_

### 5.5 Social Contributions -- Employee

**Social Contributions Employee table, 2026**  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

| Contribution | Employee Rate | Base | Capped at ceiling? |
| --- | --- | --- | --- |
| Pension / old-age (assurance pension) | 8.50% (half of the 17% total in 2026; 16% total in 2025) | gross remuneration | Yes |
| Health -- benefits in kind (CNS, prestations en nature) | 2.80% (half of 5.60%) | gross remuneration | Yes |
| Health -- cash benefits (CNS, prestations en espèces) | 0.25% (half of 0.50%) | gross remuneration | Yes |
| Dependency / long-term care (assurance dépendance) | 1.40% | gross income less the monthly abatement | **No -- uncapped** |
| **Employee total** | **12.95%** | -- | -- |

- **Dependency contribution abatement** — The dependency contribution is charged after a monthly abatement of a quarter of the social minimum wage: EUR 675.93 from 1 January 2026 and EUR 692.83 from 1 June 2026. For an employee working under 150 hours in the month, the abatement is prorated on hours declared over 173. The contribution is NOT subject to the ceiling. (Component check: 8.50 + 2.80 + 0.25 + 1.40 = 12.95%.) For the full rules use `luxembourg-social-contributions`.  _([CCSS notice of 16 January 2026](https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf); [CCSS notice of 14 August 2026](https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf))_

### 5.6 Social Contributions -- Employer

**Social Contributions Employer table, 2026**  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

| Contribution | Employer Rate | Notes |
| --- | --- | --- |
| Pension / old-age | 8.50% | half of the 17% total |
| Health -- benefits in kind | 2.80% | half of 5.60% |
| Health -- cash benefits | 0.25% | half of 0.50% |
| Accident insurance (AAA) | 0.65% | multiplied by the employer's bonus-malus factor (0.70% in 2025) |
| Occupational health (santé au travail / STM) | 0.14% |  |
| Employers' mutual insurance (MDE) | class 1 0.23% / 2 0.95% / 3 1.56% / 4 2.66% | class set by the employer's financial absenteeism rate |
| **Employer subtotal (excl. MDE), accident factor 1.0** | **12.34%** | (8.50 + 2.80 + 0.25 + 0.65 + 0.14) |
| **Employer total at MDE class 2** | **13.29%** | (12.34 + 0.95) |

- **Firm-specific defaults** — The accident factor and MDE class are firm-specific; assume factor 1.0 and MDE class 2 where unknown, and flag it.  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

### 5.7 Social Contributions -- Self-Employed (Indépendants)

**Social Contributions Self-Employed table, 2026**  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

| Contribution | Self-Employed Rate | Notes |
| --- | --- | --- |
| Pension (both shares borne by the indépendant) | 17.00% | capped at ceiling (16% in 2025) |
| Health -- benefits in kind | 5.60% | capped at ceiling |
| Health -- cash benefits | 0.50% | capped at ceiling; whether it applies depends on the person's cash-benefit cover (see `luxembourg-social-contributions`) |
| Dependency / long-term care | 1.40% | on income less the monthly abatement; uncapped |
| Accident insurance | 0.65% x factor | capped at ceiling |
| **Total before accident insurance** | **24.50%** | (17.00 + 5.60 + 0.50 + 1.40) |

Base = net professional income, between the SSM (floor) and 5x the SSM (ceiling: EUR 13,518.68 a month from 1 January 2026, EUR 13,856.63 from 1 June 2026).  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

### 5.8 Social-Contribution Ceiling (Plafond Cotisable)

**Social-Contribution Ceiling table, 2026**  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

| Period | Index | SSM unskilled, monthly | Monthly ceiling (5x SSM) |
| --- | --- | --- | --- |
| 1 Jan – 31 May 2026 | 968.04 | EUR 2,703.74 | EUR 13,518.68 |
| From 1 June 2026 | 992.24 | EUR 2,771.33 | EUR 13,856.63 |

- **Ceiling basis** — Ceiling = 5x the social minimum wage (salaire social minimum, SSM), which changed with the 1 June 2026 indexation. Use the figure for the month; for a full-year estimate, weight 5 months and 7 months.  _([CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html))_

### 5.9 Social Minimum Wage (SSM) and Tax Credits

**Tax credit table (LIR text in force on 1 January 2026)**

| Tax credit | Amount | Notes | Source |
| --- | --- | --- | --- |
| Employee tax credit (CIS) | EUR 300 + (gross - 936) x 0.029 for gross EUR 936 to 11,265; EUR 600 for EUR 11,266 to 40,000; EUR 600 - (gross - 40,000) x 0.015 for EUR 40,001 to 79,999; nil from EUR 80,000 | once per employee; not combined with the CII or the pensioner credit | LIR art. 154quater |
| Employee CO2 tax credit (CI-CO2 salarié) | EUR 216 for gross EUR 936 to 40,000; EUR 216 - (gross - 40,000) x 0.0054 for EUR 40,001 to 79,999; nil from EUR 80,000 | paid with the CIS | LIR art. 154quater |
| Self-employed tax credit (CII) | same bands as the CIS, applied to net profit | requires compulsory social-security affiliation for that profit | LIR art. 152ter |
| Self-employed CO2 tax credit (CI-CO2 indépendant) | same bands as the CI-CO2 salarié, applied to net profit | deducted from the tax; paid out if the tax is too low | LIR art. 152ter |
| Minimum-wage tax credit (CISSM) | EUR 81.00/month for monthly gross EUR 1,800–3,000; 81/600 x (3,600 - gross) between EUR 3,000 and 3,600; nil from EUR 3,600 | prorated for part-time; paid through payroll | LIR art. 139quater |
| Single-parent tax credit (CIM) | EUR 3,504 below adjusted taxable income EUR 60,000; 3,504 - (income - 60,000) x 0.0612 between EUR 60,000 and 105,000; EUR 750 above EUR 105,000 | reduced by 50% of maintenance received for the child | LIR art. 154ter |

Source for all rows: [LIR, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf).

### 5.10 Wage-Tax Withholding (Employees)

- **Wage-Tax Withholding** — The employer withholds wage tax (retenue sur traitements et salaires) per the tax card (fiche de retenue, on the RTS scale) plus social contributions monthly. The tax class on the card determines the scale applied. Employees and pensioners not taxed by assessment may ask for an annual adjustment (décompte annuel, LIR art. 145) on Form 163 R (residents) or Form 163 NR (non-residents), by 31 December of the following year. Anyone taxed by assessment files Form 100 instead.  _([ACD, décompte annuel](https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html); [LIR art. 145](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf))_

### 5.11 Filing, Advances, and Penalties

**Filing, Advances, and Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Annual return | Form 100 (modèle 100), online via MyGuichet.lu with LuxTrust, or the PDF form | [ACD, formulaires personnes physiques](https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html) |
| Filing deadline | 31 December of the year following the income year; income year 2026 due 31 December 2027 | [ACD, délais de dépôt](https://impotsdirects.public.lu/fr/az/d/delais/depot.html) |
| Annual adjustment (employees and pensioners) | Form 163 R / 163 NR, by 31 December of the year following | [ACD, décompte annuel](https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html) |
| Quarterly advances (avances) | 10 March, 10 June, 10 September, 10 December of the tax year; each is in principle a quarter of the tax from the last assessment, after withholding credits | [LIR art. 135(1) and (2)](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Final payment | Balance due by the end of the month after the month the assessment notice (bulletin d'impôt) is received; late-payment interest runs from then, and also on a late advance | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Late-filing surcharge (majoration) | up to 10% of the tax due; a penalty payment (astreinte) after a final deadline; estimated assessment if no return | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Late-payment interest | 0.6% per month from the end of the month after the assessment notice is received; 0.1% or 0.2% a month under an agreed payment plan | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |

### 5.12 VAT Interaction

**VAT Interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (registered) | NOT income -- exclude from professional income |
| Input VAT recovered (registered) | NOT an expense -- exclude from operating expenses |
| Input VAT blocked/non-deductible | IS an expense -- include the blocked VAT |
| Franchise-scheme client (turnover ≤ EUR 50,000) | No VAT charged; record purchases gross |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross is cost |

- **VAT franchise threshold and rates** — From 1 January 2025 the small-business franchise applies up to EUR 50,000 of annual turnover. A business that crosses it keeps the franchise to the end of that year if turnover stays within EUR 55,000 (10% tolerance), and loses it the next year (LTVA arts. 57 to 57quater). Rates: standard 17%, intermediate 14%, reduced 8%, super-reduced 3%.  _([AED, régime de franchise SME](https://pfi.public.lu/fr/professionnel/tva/sme.html); [AED, taux nationaux](https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html))_

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

**Conservative default:** 0% business use until a mileage log is provided. Depreciate the vehicle under Section 6.5 and deduct only the business share.

### 6.3 Phone / Internet Mixed Use

- Business-use portion only; client must provide a reasonable estimate

**Conservative default:** 0% deduction until business percentage confirmed.

### 6.4 Representation / Entertainment Costs

- The LIR sets no fixed deductible percentage for representation costs (frais de représentation)
- Deductible only where the business alone caused the cost (art. 45(1)); lifestyle spending tied to the client's position is private (art. 12 no. 1); gratuitous gifts are not deductible (art. 12 no. 2)
- This skill blocks them until the client documents the guest and the business purpose

**Flag for reviewer:** Check the documentation for each representation cost claimed.

### 6.5 Depreciation of Capital Assets (Amortissement)

- **Linear (default).** Annual charge = cost (less any estimated salvage value) / useful life in years. The useful life is set in years from the kind and conditions of use of the asset (art. 32(1) and (2)). The LIR and the ACD publish no table of rates per asset type, so the rate is 100% / useful life (a 4-year life gives 25%, a 5-year life 20%).
- **Deferred linear (on request with the return).** The client may claim less than the linear charge in a year and carry the unclaimed part forward; the balance is deducted in the last year of the useful life. Not available with the forfait for operating expenses (art. 32(1a); ACD circular L.I.R. n° 32/1).
- **Declining balance.** Allowed for tangible assets other than buildings, where the owner is also the user. The fixed rate on book value may not exceed 3 times the linear rate or 30%, whichever is lower (4 times and 40% for equipment used only for scientific or technical research). It needs the bookkeeping entries set by grand-ducal regulation. Switching from declining balance to linear is allowed; switching from linear to declining balance is not (art. 32(3) to (5)).
- **Immediate write-off.** An asset with a useful life of one year or less, or an asset costing EUR 870 or less per item where the owner is also the user, may be written off in full in the year of acquisition (art. 34). Not for assets taken over with a business transfer.
- **Building components.** Lifts, central heating, sanitary, lighting, air-conditioning and IT/internet cabling of a business building may be depreciated separately at up to 10% linear; declining balance is not allowed on buildings (ACD circular L.I.R. n° 32/2).
- **Acquisition price.** Includes incidental costs (transport, assembly, customs) and excludes deductible input VAT; a public subsidy tied directly to the purchase reduces it (ACD circular L.I.R. n° 34/1).
- **Extraordinary loss.** An extraordinary write-down is allowed for extraordinary technical or economic loss (art. 31).

**Flag for reviewer:** Check the useful life the client has documented for each asset, and whether the first-year charge is time-apportioned.

### 6.6 Self-Employed Combined Social Rate

- 2026: 24.50% before accident insurance (Section 5.7); accident insurance 0.65% x factor on top

**Flag for reviewer:** Confirm whether the 0.50% cash-benefit rate applies to the client.

### 6.7 Split-Year Social Parameters

- The SSM and contribution ceiling change on 1 June 2026; Jan–May and June–Dec figures differ

**Flag for reviewer:** Confirm whether the period split materially affects the estimate for clients near the ceiling.

## Section 7 -- Excel Working Paper Template

```
LUXEMBOURG INCOME TAX -- FORM 100 WORKING PAPER
Income Year: 2026
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
  B13. Depreciation (amortissement, arts. 32/34)    ___________
  B14. Other allowable expenses                      ___________
  B15. TOTAL operating expenses                      ___________

C. NET PROFESSIONAL PROFIT (A4 - B15)                ___________

D. OTHER INCOME
  D1. Employment income (wage tax already withheld)  ___________
  D2. Rental income                                  ___________
  D3. Investment income                              ___________
  D4. TOTAL other income                             ___________

E. SPECIAL EXPENSES / DEDUCTIONS (dépenses spéciales)
  E1. CCSS contributions paid (excl. dependency)     ___________
  E2. Other deductible special expenses              ___________
  E3. TOTAL special expenses                         ___________

F. TAXABLE INCOME (C + D4 - E3)                       ___________

G. TAX COMPUTATION (pass to deterministic engine)
  G1. PIT from 2026 scale (Section 1)                ___________
  G2. Solidarity surcharge (7% / 9%)                 ___________
  G3. Tax credits (CII / CI-CO2 / CIS / CIM)         ___________
  G4. Advance payments made                          ___________
  G5. Tax due / refund (G1 + G2 - G3 - G4)           ___________

REVIEWER FLAGS:
  [ ] Tax class confirmed (1 / 1a / 2)?
  [ ] VAT registration / franchise scheme confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Useful life documented; art. 34 EUR 870 test applied?
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
1. Tax class: 1 (single), 1a (single with child / widowed / 64 or over at 1 January), or 2 (married/partnered joint)?
2. Status: fully self-employed (indépendant) or employee (or both)?
3. VAT: do you charge VAT, or are you under the franchise (turnover up to EUR 50,000)?
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
| Income tax law (barème, classes, deductions) | LIR -- Loi modifiée du 4 décembre 1967 | [LIR, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Social contributions | Code de la sécurité sociale; CCSS | [CCSS, paramètres sociaux](https://ccss.public.lu/fr/parametres-sociaux.html) |
| Scale for 2025 and 2026 | LIR art. 118 as amended by the law of 20 December 2024 | [LIR, consolidated text at 1 January 2026](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf) |
| Annual return | Form 100 (modèle 100), MyGuichet.lu | [ACD, formulaires personnes physiques](https://impotsdirects.public.lu/fr/formulaires/pers_physiques.html) |
| Employee annual adjustment | Form 163 R / 163 NR (décompte annuel) | [ACD, décompte annuel](https://impotsdirects.public.lu/fr/formulaires/decompte_annuel.html) |
| Direct tax authority | Administration des contributions directes (ACD) | [ACD](https://impotsdirects.public.lu) |
| Social-security authority | Centre commun de la sécurité sociale (CCSS); CNS; CNAP | [CCSS](https://ccss.public.lu) |
| Penalties | Late filing up to 10%; penalty payment; interest 0.6%/month | [ACD, prélèvements supplémentaires](https://impotsdirects.public.lu/fr/az/p/prelev.html) |
| Depreciation | LIR arts. 28 to 34; ACD circulars L.I.R. n° 32/1, 32/2, 34/1 | [LIR](https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf); [circular 32/2](https://impotsdirects.public.lu/dam-assets/fr/legislation/legi22/lir-32-2-du-3052022.pdf); [circular 34/1](https://impotsdirects.public.lu/dam-assets/fr/legislation/circulaires/circulaire-lir-n-34-1-du-19-juin-1998.pdf) |
| VAT franchise and rates | LTVA arts. 39, 40, 57 to 57quater | [AED, régime de franchise SME](https://pfi.public.lu/fr/professionnel/tva/sme.html); [AED, taux nationaux](https://pfi.public.lu/fr/professionnel/tva/taxe-valeur-ajoutee/taux-nationaux-applicables.html) |

### Key Numbers at a Glance (2026)

| Item | Value | Source |
| --- | --- | --- |
| PIT tax-free threshold (class 1) | EUR 13,230 | LIR art. 118 |
| Top marginal rate | 42% above EUR 234,870 | LIR art. 118 |
| Solidarity surcharge | 7% (9% above adjusted taxable income EUR 150,000 class 1/1a; EUR 300,000 class 2) | ACD, Fonds pour l'emploi |
| Employee social total | 12.95% | CCSS, paramètres sociaux |
| Employer social total (excl. MDE, accident factor 1.0) | 12.34% | CCSS, paramètres sociaux |
| Self-employed total before accident insurance | 24.50% | CCSS, paramètres sociaux |
| Social ceiling | EUR 13,518.68/month (Jan to May 2026); EUR 13,856.63/month (from 1 June 2026) | CCSS, paramètres sociaux |
| SSM unskilled | EUR 2,703.74/month (Jan to May 2026); EUR 2,771.33/month (from 1 June 2026) | CCSS, paramètres sociaux |
| VAT franchise threshold | EUR 50,000 turnover (tolerance to EUR 55,000 in the year crossed) | AED, régime de franchise SME |
| Dependency abatement | EUR 675.93/month (from 1 January 2026); EUR 692.83/month (from 1 June 2026) | CCSS notices of 16 January and 14 August 2026 |
| Immediate write-off limit | EUR 870 per item (owner-user) | LIR art. 34 |

### Caveats and Open Items

- Employer accident insurance (0.65% in 2026) is multiplied by a firm-specific bonus-malus factor, and the MDE class depends on the employer's absenteeism. Exact employer cost varies by employer.
- Social parameters change on 1 June 2026 (indexation): SSM, ceiling and dependency abatement differ between January to May and June to December.
- The LIR and the ACD publish no depreciation rate per asset type; the rate follows from the useful life the client documents (Section 6.5).
- Not yet confirmed: whether a first-year depreciation charge must be time-apportioned for months held (the LIR text does not say); the VAT rates page of the AED was last updated 28 December 2023, and the consolidated LTVA on Legilux could not be read for 2026.

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
Expected (January to May 2026): capped contributions (pension 8.5% + health 2.8% + 0.25% = 11.55% × 4,000) = EUR 462.00; dependency 1.4% × (4,000 − 675.93) = EUR 46.54. Total employee SSC = EUR 508.54.

#### Test 6 -- Dependency contribution uses abatement and is uncapped.

Input: Monthly professional income EUR 5,000 in March 2026.
Expected: dependency base = 5,000 − 675.93 = EUR 4,324.07; × 1.4% = EUR 60.54. In October 2026 the base is 5,000 − 692.83 = EUR 4,307.17; × 1.4% = EUR 60.30. (No ceiling applied to dependency.)

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
- NEVER quote the self-employed 24.50% without adding accident insurance and checking whether the 0.50% cash-benefit rate applies
- NEVER treat CCSS contributions as an operating expense -- they are a special-expense deduction
- NEVER include VAT collected on sales in income for VAT-registered clients
- NEVER expense a capital asset in full -- capitalise and depreciate per the LIR
- NEVER invent a useful life -- take it from the client's asset facts, then apply the art. 32 caps (declining balance at most 3x linear and 30%)
- NEVER allow personal living costs, fines, penalties, or income tax itself as a deduction
- NEVER apply the dependency-insurance ceiling -- that contribution is uncapped
- NEVER mix the January to May and June 2026 social ceilings without noting the split

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
