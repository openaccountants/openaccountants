---
name: cameroon-income-tax
description: Use this skill whenever asked about Cameroon personal income tax (IRPP) for salaried or self-employed individuals. Trigger on phrases like "how much income tax do I pay in Cameroon", "IRPP", "impot sur le revenu", "CNPS contributions", "PAYE Cameroon", "IGS", "Impot General Synthetique", "Centre de Gestion Agree", "CGA", "barème IRPP", "Credit Foncier", "FNE", "monthly salary tax Cameroon", "net taxable income", "minimum tax", or any question about filing or computing income tax for a salaried or self-employed client in Cameroon. Also trigger when preparing or reviewing a monthly PAYE return, the annual recapitulative declaration, the DIPE employer summary, computing CNPS social security, or advising on the IGS/actual-earnings turnover regimes. This skill covers the progressive IRPP scale (CAC-inclusive), CNPS branches, Credit Foncier/FNE, council tax and CRTV royalty, the IGS small-business regime, filing deadlines, and penalties. ALWAYS read this skill before touching any Cameroon income tax work.
version: 0.2
jurisdiction: CM
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

# Cameroon income tax (IRPP) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. Law: Code General des Impots (CGI), Edition 2026, as amended by Law 2025/012 of 17 December 2025 (Finance Law 2026). Companies are in `cameroon-corporate-income-tax`; non-residents in `cameroon-cross-border`.

## Who this applies to

Individuals with fiscal domicile in Cameroon pay IRPP on worldwide income (CGI art. 25). Fiscal domicile means a home or main stay in Cameroon, a salaried or other professional activity there unless shown to be accessory, or the centre of economic interests. People domiciled abroad pay on Cameroon-source gains.

Salaried, passive-income and non-professional taxpayers are covered by art. 93 undecies. Traders and professionals fall under IGS or the real regime (art. 93 quater):

- IGS: turnover excluding tax under XAF 50,000,000 (commercial, industrial, craft, agro-pastoral) or under XAF 30,000,000 (liberal professions).
- Real regime: at or above those limits. Going over a limit moves the taxpayer to the real regime at once; a real-regime taxpayer who falls below stays for two probation years (art. C 39).

## Rates, bands and thresholds

| Item | Rate or amount | Source |
|---|---|---|
| Salary scale, up to XAF 2,000,000 | 10% (11% with CAC) | CGI art. 69(1), 71: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| XAF 2,000,001 to 3,000,000 | 15% (16.5% with CAC) | same |
| XAF 3,000,001 to 5,000,000 | 25% (27.5% with CAC) | same |
| Over XAF 5,000,000 | 35% (38.5% with CAC) | same |
| Communal surcharge (CAC) | 10% of the tax | same |
| Professional expenses, salary | 30% of gross, capped at XAF 4,800,000 a year | CGI art. 34: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Business, agricultural, property and listed non-commercial income | Art. 17 rate of 30% (33% with CAC) | CGI art. 17, 69(2), 71: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Minimum on those incomes | 2% of turnover, 2.2% with CAC | CGI art. 69(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Listed non-commercial income, art. 56(2) d, e, f, h | Final 10%; art. 56(2) g: 5% | CGI art. 69(3): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Investment income | Final 15% (16.5% with CAC) | CGI art. 70(1), 71: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Dividends from a company with turnover up to XAF 3 billion | 10% (11% with CAC) | CGI art. 70(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Passive income paid to a tax haven | 30% | CGI art. 70(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Instalment, real regime and IGS | 2% of monthly turnover plus CAC (2.2%) | CGI art. 21, 91; Arrete 00001 of 5 Jan 2026 art. 2: https://www.impots.cm/sites/default/files/documents/arr%C3%AAt%C3%A9%20RTS%202026%20VF.pdf |
| Withholding, not on active taxpayer file | 10% | same |
| Liberal professions and public orders under XAF 5,000,000 | 5.5% | Arrete art. 3: https://www.impots.cm/sites/default/files/documents/arr%C3%AAt%C3%A9%20RTS%202026%20VF.pdf |
| Gain on a building | Final 5%; 10% if paid in cash | CGI art. 90: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| IGS class 1, under XAF 500,000 | XAF 20,000 | CGI art. C 40: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Class 2, to under 1 million | XAF 30,000 | same |
| Class 3, to under 1.5 million | XAF 40,000 | same |
| Class 4, to under 2 million | XAF 50,000 | same |
| Class 5, to under 2.5 million | XAF 60,000 | same |
| Class 6, to under 5 million | XAF 150,000 | same |
| Class 7, to under 10 million | XAF 300,000 | same |
| Class 8, to under 20 million | XAF 500,000 | same |
| Class 9, to under 30 million | XAF 1,000,000 | same |
| Class 10, to under 50 million | XAF 2,000,000 | same |
| IGS reduction for CGA members | 50% | CGI art. C 38(2), C 40(4): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Credit Foncier | Employee 1%; employer 1.5% | CGI annex law art. 6: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| National Employment Fund (FNE) | 1% employer | same |
| CRTV audiovisual fee, monthly pay over XAF 1,000,000 | XAF 13,000 | CGI annex law art. 3: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CNPS pension | Unverified: 4.2% employee, 4.2% employer, ceiling XAF 750,000 a month. cnps.cm did not open | n/a |
| CNPS family and work risk | Unverified: 7% and 1.75% to 5% employer; voluntary 8.4% | n/a |
| Development tax, employees, base pay over XAF 500,000 a month | XAF 30,000 a year; lower bands from XAF 3,000 start at XAF 62,000 | CGI art. C 86: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Minimum wage | Unverified: XAF 60,000 non-agricultural, 45,000 agricultural, 43,969 State | n/a |

## The base

Net salary = gross pay and benefits, less the capped 30%, less compulsory CNPS retirement contributions (CGI art. 32 to 34). Benefits in kind use the art. 33 scale on taxable gross pay: housing 15%, electricity 4%, water 2%; see art. 33 for other benefits. Tax = scale on net income, plus 10% CAC. Do not add CAC to the CAC-inclusive rates.

Art. 31 exempts, among others, special allowances for job costs that are used as intended and not excessive, family allowances, and work accident benefits.

Dividends are taxed on the gross amount (art. 44). Salaried taxpayers do not itemise expenses. Rental, business and other categories follow art. 45 to 58. A person transporting passengers through a digital platform is taxed on 20% of the gross per trip (art. 58).

## Deadlines and filing

| Duty | Deadline | Source |
|---|---|---|
| Professional annual return | 15 March (art. 74) | CGI |
| Balance of business IRPP | 15 March (art. 91) | CGI |
| Annual income statement from payer to recipient | 15 March (art. 74 bis(5)) | CGI |
| Recap return: senior personalities, public and parapublic staff | 31 July (art. 74 bis) | CGI |
| Recap return: staff of large, medium and specialised-centre employers | 30 September | CGI |
| Recap return: other individuals | 31 October | CGI |
| Monthly instalment | 15th of next month (art. 21) | CGI |
| Salary tax withheld by employer | 15th of next month (art. 82) | CGI |
| IGS return and payment | 15 April, or within 15 days of each quarter end on option (art. C 41) | CGI |
| Statistical and fiscal return (DSF) for IGS | 15 May | CGI |
| Credit Foncier and FNE | First 20 days of next month (annex law art. 7) | CGI |

**How to file the annual recap return.** The official flow was not traced page by page, so no portal steps are given. The law says: file with the tax centre of residence or online on the administration's form (art. 74 bis(2)); give income by category, tax already withheld, and the balance; pay any balance with the return by mobile phone, transfer, telepayment or cash at a bank counter (art. 74 bis(3)). An overpayment is refunded or credited on request after validation (art. 74 bis(4)).

## Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late filing or payment of self-assessed tax | 10% a month, capped at 30% of tax | CGI LPF art. L 106 |
| Late payment interest | 1.5% a month | same |
| Understatement interest | 1.5% a month, capped at 50% | LPF art. L 95, L 98 |
| Understatement penalty | 30% good faith, 100% bad faith, 150% fraud | LPF art. L 96 |
| Spontaneous payment after audit | 15% | LPF art. L 96(2) |
| No return after formal notice | Assessment plus 100%; 150% on repeat | LPF art. L 97 |
| Fine, no return after notice | XAF 200,000, 100,000 or 50,000 by tax office | LPF art. L 97(2) |
| IGS unpaid | Closure of premises plus 50% | CGI art. C 45 |

## Cross-border points

Treaties override art. 25. Non-residents pay on Cameroon-source income; pay for work done in Cameroon is taxable (art. 30). Pensions count as Cameroon income if the payer is established there. See `cameroon-cross-border`.

## Two worked examples that recompute

The CNPS amount is an input; its rate is unverified.

```oa-check
name: Salary 12,000,000, 30 percent below the cap, 2026
inputs:
  gross: 12000000
  cnps: 378000
steps:
  - prof: min(gross * 0.30, 4800000)
  - net: gross - prof - cnps
  - base_tax: 850000 + (net - 5000000) * 0.35
  - total: base_tax * 1.10
expected:
  net: 8022000
  total: 2098470
```

```oa-check
name: Salary 20,000,000, 30 percent capped, 2026
inputs:
  gross: 20000000
  cnps: 378000
steps:
  - prof: min(gross * 0.30, 4800000)
  - net: gross - prof - cnps
  - base_tax: 850000 + (net - 5000000) * 0.35
  - total: base_tax * 1.10
expected:
  prof: 4800000
  net: 14822000
  total: 4716470
```

## Further worked examples

All examples use XAF. Salary IRPP base = gross - 30% professional deduction - CNPS employee 4.2% (capped), then rounded down to nearest XAF 1,000, then the progressive scale in Section 1 (220,000 / 385,000 / 935,000 cumulative checkpoints).

### Example 1 -- Salaried employee, mid-range salary

Input: Resident employee, gross annual salary XAF 6,000,000. No other income.

Reasoning:
- 30% professional deduction: 6,000,000 x 30% = 1,800,000.
- CNPS employee pension 4.2%; annual salary 6,000,000 is below the XAF 9,000,000 ceiling, so 4.2% x 6,000,000 = 252,000.
- Net taxable = 6,000,000 - 1,800,000 - 252,000 = 3,948,000 (already a multiple of 1,000).
- IRPP: first 2,000,000 -> 220,000; next 1,000,000 -> 165,000 (cumulative 385,000); remaining 948,000 @ 27.5% = 260,700.
- Total IRPP = 385,000 + 260,700 = 645,700.

Classification: Annual IRPP = XAF 645,700 (before council tax / CRTV / housing-fund withholdings).

### Example 2 -- Salaried employee above the CNPS ceiling

Input: Resident employee, gross annual salary XAF 12,000,000.

Reasoning:
- 30% professional deduction: 12,000,000 x 30% = 3,600,000.
- CNPS employee pension is capped at XAF 9,000,000/year base: 4.2% x 9,000,000 = 378,000 (NOT 4.2% x 12,000,000).
- Net taxable = 12,000,000 - 3,600,000 - 378,000 = 8,022,000.
- IRPP: cumulative to 5,000,000 = 935,000; excess = 8,022,000 - 5,000,000 = 3,022,000 @ 38.5% = 1,163,470.
- Total IRPP = 935,000 + 1,163,470 = 2,098,470.

Classification: Annual IRPP = XAF 2,098,470. Development tax XAF 30,000 a year at most and CRTV up to XAF 13,000 apply separately.

### Example 3 -- Dividend / investment income (schedular flat rate)

Input line:
`15/03/2025 ; AFRILAND VIREMENT RECU ; DIVIDENDE SARL XYZ ; +5,000,000 ; XAF`

Reasoning:
Investment income from shares is taxed at the flat rate of 16.5% (15% + CAC), or 11% if the payer has turnover of XAF 3 billion or less (art. 70(2)), not the progressive salary scale. 5,000,000 x 16.5% = 825,000.

Classification: Investment-income IRPP = XAF 825,000 (flat). Do NOT run through the progressive scale.

### Example 4 -- Self-employed under IGS, CGA member

Input: Self-employed (salon), annual VAT-exclusive turnover XAF 12,000,000. Member of an approved Centre de Gestion Agree (CGA).

Reasoning:
- Turnover XAF 12,000,000 is below XAF 50,000,000, so the taxpayer falls under the IGS (Impot General Synthetique) synthetic regime, not actual-earnings.
- CGI art. C 40 class 8 (10 to under 20 million): IGS XAF 500,000; as a CGA member the rate is halved to XAF 250,000.
- IGS is due in one payment by 15 April, or quarterly under art. C 41 and C 42.

Classification: Annual IGS = XAF 250,000 (CGA-reduced). Minimum tax does not apply under IGS.

### Example 5 -- SaaS subscription (deductible, actual-earnings)

Input line:
`01/04/2025 ; SGC PRLV ; MICROSOFT 365 ; ABONNEMENT AVRIL ; -15,000 ; XAF`

Reasoning:
Recurring software subscription, wholly for the business. Deductible operating expense for a self-employed taxpayer under the actual-earnings regime. If VAT-registered, deduct the VAT-exclusive amount (15,000 / 1.1925 = 12,579) and recover the input VAT separately.

Classification: Deductible business expense = XAF 15,000 (or VAT-exclusive XAF 12,579 if registered). Not relevant to IGS or salaried taxpayers.

### Example 6 -- Internal transfer (exclude)

Input line:
`15/05/2025 ; BICEC VIREMENT ; COMPTE PROPRE EPARGNE ; ; -2,000,000 ; XAF`

Reasoning:
Transfer between own accounts. Neither income nor expense. Exclude entirely.

Classification: EXCLUDE.


## Ask the client first

1. Is fiscal domicile in Cameroon?
2. Salary, business, or both?
3. Turnover excluding tax, and is the activity a liberal profession? This decides the XAF 30 or 50 million limit.
4. Is there a valid CGA certificate?
5. For dividends, what is the paying company's turnover?

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown taxpayer type (salaried vs self-employed) | STOP -- do not apply a scale without knowing income type |
| Unknown residency | Treat as resident (worldwide income) only after confirmation; otherwise STOP |
| Unknown turnover (self-employed regime) | STOP -- IGS vs actual-earnings turns on turnover |
| Unknown CNPS occupational-risk class | Use lowest published rate 1.75% and flag for reviewer |
| Unknown whether expense is professional | Not deductible (rely on the 30% lump sum only) |
| Unknown CGA membership (self-employed) | Assume NOT a CGA member (no IGS halving) |
| Unknown VAT status | Standard 19.25% VAT-registered |


## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** : For a salaried client: gross annual (or monthly) salary, residency status, and CNPS contribution records. For a self-employed client: full-year bank statement (CSV, PDF, or pasted text) plus annual VAT-exclusive turnover and chosen tax regime.
- **Recommended** : Monthly payslips, employer DIPE/recapitulative summary, CNPS statements, prior-year annual declaration, VAT registration evidence, CGA membership certificate (if self-employed).
- **Ideal** : Complete income and expenditure account, asset register, evidence of council tax / CRTV withholding, Credit Foncier and FNE deduction records, provisional/instalment payment confirmations.
- **Refusal if minimum is missing** : SOFT WARN. No salary figure or no bank statement at all = hard stop. Bank statement without supporting documents = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify that all figures are supported by valid documentation and that the regime (IGS vs actual-earnings) is correctly determined."

### Refusal Catalogue

- **R-CM-1** : Income type / regime unknown. "Cameroon IRPP applies different scales to salary, investment income, and business profit, and different regimes (IGS vs actual-earnings) to the self-employed. This skill cannot compute tax without knowing the income type and, for the self-employed, the annual turnover. Please confirm before proceeding."
- **R-CM-2** : Companies and partnerships. "This skill covers individuals (salaried and sole-trader/self-employed) only. Companies pay corporate income tax (IS) and file separately. Escalate to a Cameroon-qualified practitioner."
- **R-CM-3** : Non-resident / expatriate withholding. "Non-resident and expatriate taxation (withholding on Cameroon-source income, treaty relief) has different rules and is out of scope. Escalate to a Cameroon-qualified practitioner."
- **R-CM-4** : Capital gains / property disposals. "Capital gains and property-transfer taxation require specialised analysis. Out of scope. Escalate."
- **R-CM-5** : Arrears / enforcement. "Client has outstanding tax arrears or is subject to DGI enforcement. Penalties (10%/month late filing, 1.5%/month interest, and 30%-100%/150% bad-faith assessment uplifts) are severe. Do not advise. Escalate immediately."
- **R-CM-6** : VAT return requested. "This skill covers IRPP only. Cameroon standard VAT is 19.25% (17.5% + 10% CAC) and is computed separately."


## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Cameroon statements are predominantly in French; match by case-insensitive substring on the libelle (description) or counterparty. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits / Credit on Bank Statement)

**Income Patterns**

| Pattern (FR/EN) | Treatment | Notes |
| --- | --- | --- |
| VIREMENT RECU, PAIEMENT CLIENT, REGLEMENT FACTURE | Business turnover | If VAT-registered, extract VAT-exclusive amount (gross / 1.1925) |
| HONORAIRES, PRESTATION, CONSULTATION | Business turnover | Professional fees -- typical self-employed |
| SALAIRE, PAIE, VIREMENT SALAIRE, EMPLOYEUR [name] | Salary income | Goes to salary IRPP computation, NOT business turnover |
| ORANGE MONEY, MTN MOMO, MOBILE MONEY (received) | Business turnover (if business) | Confirm business vs personal mobile-money inflow |
| STRIPE, PAYPAL, WISE PAYOUT | Business turnover | Platform payout -- match to invoices; VAT-exclusive if registered |
| LOYER RECU, REVENU LOCATIF | Rental income | Separate category -- not business turnover |
| DIVIDENDE, INTERETS, COUPON | Investment income | Taxed at flat 16.5% schedular rate (see Section 1) |
| REMBOURSEMENT IMPOT, RISTOURNE DGI | EXCLUDE | Tax refund -- not income |

### 3.2 Expense Patterns (Debits / Debit) -- Deductible for actual-earnings business

**Deductible Expense Patterns**

| Pattern (FR/EN) | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LOYER BUREAU, LOYER COMMERCIAL | Office rent | Deductible | Dedicated business premises |
| ASSURANCE PRO, RESPONSABILITE CIVILE | Professional insurance | Deductible |  |
| EXPERT-COMPTABLE, COMPTABLE, HONORAIRES COMPTABLES | Accountancy fees | Deductible |  |
| AVOCAT, NOTAIRE, FRAIS JURIDIQUES | Legal fees | Deductible | Must be business-related |
| FOURNITURES BUREAU, PAPETERIE | Office supplies | Deductible |  |
| PUBLICITE, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| FORMATION, SEMINAIRE, CONFERENCE | Training | Deductible | Must relate to current business |
| FRAIS BANCAIRES, COMMISSION BANCAIRE, AGIOS | Bank charges | Deductible | Business account only |
| ABONNEMENT, LOGICIEL, SAAS, MICROSOFT 365, ADOBE | Software subscription | Deductible | Recurring = operating expense |
| ELECTRICITE, ENEO, EAU, CAMWATER | Utilities | Deductible (business %) | Apportion if home/mixed use -- default 0% if mixed |
| ORANGE, MTN, CAMTEL (telecom) | Telecoms | Deductible (business %) | Business portion only |

- **Applicability note** : These deductions apply ONLY to self-employed taxpayers under the actual-earnings (regime du reel) regime. Salaried taxpayers rely on the standard 30% lump-sum professional-expense deduction; IGS taxpayers pay a synthetic tax on turnover and do not itemise.

### 3.3 Expense Patterns (Debits) -- NOT Deductible

**Not Deductible Expense Patterns**

| Pattern (FR/EN) | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, REPAS, RECEPTION, CADEAU CLIENT | Entertainment/gifts | NOT deductible | Treat as blocked; flag for reviewer |
| PERSONNEL, COURSES, SUPERMARCHE, MARCHE | Personal expenses | NOT deductible | Private living costs |
| AMENDE, PENALITE, CONTRAVENTION | Fines/penalties | NOT deductible | Public policy |
| IMPOT, IRPP, PAIEMENT DGI | Tax payments | NOT deductible | Income tax cannot reduce income |
| PRELEVEMENT PERSONNEL, RETRAIT ESPECES (personnel) | Drawings | NOT deductible | Not an expense |

### 3.4 Statutory Withholdings / Contributions (special handling)

**Statutory Withholdings**

| Pattern (FR/EN) | Treatment | Notes |
| --- | --- | --- |
| CNPS, COTISATION SOCIALE, PREVOYANCE SOCIALE | Social contribution | Employee portion reduces salary IRPP base (Section 3 social table) |
| CREDIT FONCIER, CFC | Housing fund | Employee 1% / employer 1.5% (Section 4) |
| FNE, FONDS NATIONAL EMPLOI | Employment fund | Employer 1% only |
| TAXE COMMUNALE, REDEVANCE COMMUNALE | Council tax (poll) | Development tax: up to XAF 30,000 a year (art. C 86) |
| RAV, REDEVANCE CRTV, AUDIOVISUEL | CRTV royalty | Up to XAF 13,000 graduated (Section 2 other-taxes) |
| TVA, PAIEMENT TVA | EXCLUDE | VAT liability payment, not an expense |

### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions**

| Pattern (FR/EN) | Treatment | Notes |
| --- | --- | --- |
| VIREMENT INTERNE, COMPTE PROPRE | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRET, ECHEANCE CREDIT (principal) | EXCLUDE | Loan principal movement |

### 3.6 Cameroon Banks / Channels -- Statement Format Reference

**Banks/Channels Statement Format Reference**

| Channel | Common Patterns | Notes |
| --- | --- | --- |
| Afriland First Bank | VIREMENT, RETRAIT, COMMISSION, AGIOS | PDF; French libelle; date DD/MM/YYYY |
| SGC (Societe Generale Cameroun) | VIR, PRLV, CB, FRAIS | PDF/CSV; counterparty in libelle |
| BICEC | VIREMENT, PRELEVEMENT, COMMISSION | PDF; shorter descriptions |
| Ecobank Cameroun | TRANSFER, PAYMENT, CHARGES | PDF/CSV; mixed FR/EN |
| Orange Money / MTN MoMo | TRANSFERT, PAIEMENT MARCHAND, RETRAIT | Mobile-money statement export; confirm business vs personal |


## Tier 2 catalogue

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office / Mixed-Use Utilities (actual-earnings)

- **Home Office / Mixed-Use Utilities** : Apportion electricity (ENEO), water (Camwater), internet by business-use proportion. Must be a dedicated, documented basis. Conservative default: 0% deduction until reviewer confirms the basis.

### 6.2 Vehicle Business Use (actual-earnings)

- **Vehicle Business Use** : Only the business-use proportion of fuel, insurance, and maintenance is deductible; requires a usage log. Conservative default: 0% business use until a log is provided.

### 6.3 Phone / Telecom Mixed Use

- **Phone / Telecom Mixed Use** : Business portion only (Orange, MTN, Camtel). Conservative default: 0% until business percentage confirmed.

### 6.4 CNPS Occupational-Risk Class

- **CNPS Occupational-Risk Class** : Employer occupational-accident rate is 1.75%-5% depending on the industry risk class (A/B/C). Flag for reviewer: confirm the client's assigned risk class; default to 1.75% if unknown and flag.

### 6.5 IGS vs Actual-Earnings Boundary

- **IGS vs Actual-Earnings Boundary** : Turnover near XAF 50,000,000 must be confirmed (VAT-exclusive) before choosing a regime. CGA membership halves IGS -- confirm a valid certificate before applying the reduction. Flag for reviewer.

### 6.6 30% Professional Deduction Mechanics

- **30% Professional Deduction Mechanics** : CGI art. 34: 30% of gross, capped at XAF 4,800,000 a year.

### 6.7 Entertainment / Gifts

- **Entertainment / Gifts** : Treated as blocked in this skill; confirm any statutory partial allowance with the reviewer before deducting.


## Section 7 -- Excel Working Paper Template

CAMEROON IRPP -- WORKING PAPER
Tax Year: 2026
Client: ___________________________
Taxpayer type: Salaried / Self-employed (IGS) / Self-employed (actual-earnings)
Residency: Resident / Non-resident (STOP if non-resident)

A. SALARIED COMPUTATION (skip if self-employed)
  A1. Gross annual salary                          ___________
  A2. Less 30% professional deduction (A1 x 30%)   ___________
  A3. Less CNPS employee 4.2% (cap base 9,000,000) ___________
  A4. Net taxable (A1 - A2 - A3), round down 1,000 ___________
  A5. IRPP per progressive scale (Section 1)       ___________
  A6. Development tax (up to 30,000/yr)             ___________
  A7. CRTV royalty (up to 13,000)                  ___________
  A8. Credit Foncier employee 1% (A1 x 1%)         ___________

B. INVESTMENT INCOME (flat 16.5%)
  B1. Dividend / share income                      ___________
  B2. IRPP (B1 x 16.5%)                            ___________

C. SELF-EMPLOYED -- IGS (turnover < 50,000,000)
  C1. Annual VAT-exclusive turnover                ___________
  C2. IGS per art. C 40 class table             ___________
  C3. CGA member? halve C2 -> IGS due              ___________

D. SELF-EMPLOYED -- ACTUAL-EARNINGS (turnover >= 50,000,000)
  D1. Turnover (VAT-exclusive)                     ___________
  D2. Less deductible business expenses            ___________
  D3. Net profit (D1 - D2)                         ___________
  D4. IRPP (33% with CAC)                          ___________
  D5. Minimum tax (2.2% of turnover)               ___________
  D6. Tax due = max(D4, D5)                        ___________

E. TOTAL TAX (pass to deterministic engine)        ___________

REVIEWER FLAGS:
  [ ] Taxpayer type and residency confirmed?
  [ ] CNPS ceiling applied correctly (9,000,000/yr base)?
  [ ] 30% professional deduction mechanics confirmed?
  [ ] IGS band table confirmed against 2026 CGI?
  [ ] CGA membership certificate verified?
  [ ] Occupational-risk class confirmed?
  [ ] Investment income kept at flat 16.5% (not progressive)?
  [ ] Entertainment / personal items excluded?

## Section 8 -- Bank Statement Reading Guide

### Cameroon Bank / Channel Formats

**Cameroon Bank / Channel Formats**

| Channel | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Afriland First Bank | PDF | Date, Libelle, Debit, Credit, Solde | French; date DD/MM/YYYY |
| SGC (Societe Generale) | PDF, CSV | Date, Libelle, Montant, Solde | Counterparty in libelle |
| BICEC | PDF | Date, Libelle, Debit, Credit | Shorter descriptions |
| Ecobank Cameroun | PDF, CSV | Date, Description, Amount, Balance | Mixed FR/EN |
| Orange Money / MTN MoMo | CSV/PDF export | Date, Type, Montant, Solde | Confirm business vs personal |

### Key Cameroon Banking / Tax Terms (French)

**Key Cameroon Banking / Tax Terms**

| Term (FR) | English | Classification Hint |
| --- | --- | --- |
| Virement / VIR | Transfer | Check direction for income/expense |
| Prelevement / PRLV | Direct debit | Regular expense (utility, subscription) |
| Solde | Balance | Running balance column |
| Debit / Credit | Debit / Credit | Credit = potential income |
| Agios / Frais bancaires | Bank charges | Deductible (actual-earnings) |
| Salaire / Paie | Salary | Salary income -> progressive scale |
| Honoraires | Professional fees | Business turnover |
| Loyer | Rent | Received = rental income; paid = office rent (if commercial) |
| CNPS | Social security | Employee 4.2% reduces salary base |
| TVA | VAT | Exclude from income/expense (liability) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- CAMEROON IRPP
1. Are you a tax resident of Cameroon (fiscal domicile here)?
2. Income type: salaried, self-employed, or both?
3. If salaried: gross annual (or monthly) salary, and is CNPS withheld by your employer?
4. If self-employed: annual VAT-exclusive turnover? (determines IGS vs actual-earnings)
5. Are you a member of an approved Centre de Gestion Agree (CGA)?
6. Are you VAT-registered (standard 19.25%)?
7. Do you have investment income (dividends/interest from shares)?
8. Any rental income?
9. What is your CNPS occupational-risk class (employer rate 1.75%-5%)?
10. Any capital assets, home-office use, or vehicle used for business?


## Test suite and prohibitions

### Test Suite

Test 1 -- Salaried mid-range.
Input: Resident, gross salary XAF 6,000,000, no other income.
Expected: 30% deduction 1,800,000; CNPS 252,000; net 3,948,000; IRPP = 385,000 + 948,000 x 27.5% (260,700) = XAF 645,700.

Test 2 -- Salaried above CNPS ceiling.
Input: Resident, gross salary XAF 12,000,000.
Expected: 30% deduction 3,600,000; CNPS capped 9,000,000 x 4.2% = 378,000; net 8,022,000; IRPP = 935,000 + 3,022,000 x 38.5% (1,163,470) = XAF 2,098,470.

Test 3 -- Investment income flat rate.
Input: Dividend income XAF 5,000,000.
Expected: 5,000,000 x 16.5% = XAF 825,000. NOT run through the progressive scale.

Test 4 -- IGS, CGA member.
Input: Self-employed salon, turnover XAF 12,000,000, CGA member.
Expected: IGS XAF 500,000 halved to XAF 250,000 .

Test 5 -- Bracket boundary.
Input: Net taxable income exactly XAF 5,000,000.
Expected: cumulative tax = XAF 935,000 (220,000 + 165,000 + 550,000); no 38.5% applies at the boundary.

Test 6 -- Lowest band.
Input: Net taxable income XAF 1,500,000.
Expected: 1,500,000 x 11% = XAF 165,000.

Test 7 -- Employer CNPS total (lowest risk).
Input: Monthly salary at/below ceiling, lowest occupational-risk class.
Expected: employer total = 4.2% + 7% + 1.75% = 12.95%; employee total = 4.2%.

## PROHIBITIONS

- NEVER apply the progressive salary scale to investment income (use the flat rate) or to IGS turnover
- NEVER compute final tax figures as definitive -- always label as estimated and pass to the deterministic engine
- NEVER apply CNPS 4.2% on a base above the XAF 9,000,000/year ceiling
- NEVER add the 10% CAC again on top of the 11/16.5/27.5/38.5% scale -- it is already included
- NEVER apply minimum tax to salaried workers or IGS taxpayers
- NEVER itemise business expenses for a salaried taxpayer -- only the 30% lump-sum deduction applies
- NEVER halve IGS without a verified CGA membership certificate
- NEVER treat a non-resident as worldwide-taxed without confirming residency (escalate per R-CM-3)
- NEVER allow fines, penalties, drawings, or income tax itself as a deduction
- NEVER skip the round-down to the nearest XAF 1,000 on the net taxable income
- NEVER rely on a unverified figure for a filed return without reviewer confirmation against the 2026 CGI


## Sources

| Source | URL | Read on |
|---|---|---|
| CGI Edition 2026 (DGI): arts. 17, 21, 25, 30 to 34, 44, 56, 58, 69 to 74 bis, 82, 90 to 93 undecies, C 38 to C 46, C 86, L 95 to L 98, L 106, Credit Foncier and CRTV annex laws | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-01 |
| Arrete 00001/MINFI/DGI of 5 Jan 2026 on withholding: arts. 1 to 9 | https://www.impots.cm/sites/default/files/documents/arr%C3%AAt%C3%A9%20RTS%202026%20VF.pdf | 2026-11-01 |
| CNPS site | https://www.cnps.cm | 2026-11-01 (refused: 403 to fetch, no page text in browser) |

Not yet confirmed: CNPS rates and ceiling (site did not open); minimum wage; 10-year record retention and the XAF 1,000 rounding of net income carried from the old skill; whether the 25% rate of art. 17 bis reaches individuals under art. 69(2) (the text cites art. 17 only); how art. C 41 (one payment or quarterly option) and art. C 42(2) (quarterly) fit together; the Finance Law 2026 circular, a scan not read; DGI's portal steps for the IRPP declaration; the old rule on quarterly regularisation dates by tax centre.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network : accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

