---
name: cameroon-income-tax
description: Use this skill whenever asked about Cameroon personal income tax (IRPP) for salaried or self-employed individuals. Trigger on phrases like "how much income tax do I pay in Cameroon", "IRPP", "impot sur le revenu", "CNPS contributions", "PAYE Cameroon", "IGS", "Impot General Synthetique", "Centre de Gestion Agree", "CGA", "barème IRPP", "Credit Foncier", "FNE", "monthly salary tax Cameroon", "net taxable income", "minimum tax", or any question about filing or computing income tax for a salaried or self-employed client in Cameroon. Also trigger when preparing or reviewing a monthly PAYE return, the annual recapitulative declaration, the DIPE employer summary, computing CNPS social security, or advising on the IGS/actual-earnings turnover regimes. This skill covers the progressive IRPP scale (CAC-inclusive), CNPS branches, Credit Foncier/FNE, council tax and CRTV royalty, the IGS small-business regime, filing deadlines, and penalties. ALWAYS read this skill before touching any Cameroon income tax work.
version: 0.1
jurisdiction: CM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon Income Tax -- IRPP

## Section 1 -- Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Cameroon (Republic of Cameroon) |
| Tax | Personal Income Tax -- Impot sur le Revenu des Personnes Physiques (IRPP) |
| Currency | XAF only (Central African CFA franc) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Code General des Impots (General Tax Code), as amended by the 2025 Finance Law |
| Surcharge | Additional Council Tax (Centimes Additionnels Communaux / CAC) = 10% on the base income tax (already folded into the headline scale below) |
| Tax authority | Direction Generale des Impots (DGI), Cameroon -- https://impots.cm |
| Social security body | Caisse Nationale de Prevoyance Sociale (CNPS) -- https://www.cnps.cm |
| Filing portal | DGI online declaration platform (impots.cm) |
| Monthly PAYE deadline | 15th of the month following salary payment [PwC tax administration] |
| Annual declaration deadline | 31 July / 30 September / 31 October depending on taxpayer class (see 5.10) [PwC] |
| Validated by | Live status: https://openaccountants.com/skills/cameroon-income-tax |
| Validation date | Live status: https://openaccountants.com/skills/cameroon-income-tax |
| Skill version | 0.1 |

### IRPP Rate Brackets (2025) -- CAC-inclusive scale

**IRPP Rate Brackets (2025)**  _([PwC -- https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income])_

| Net taxable income band (XAF / year) | Rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 2,000,000 | 11% | XAF 220,000 |
| 2,000,001 -- 3,000,000 | 16.5% | XAF 385,000 |
| 3,000,001 -- 5,000,000 | 27.5% | XAF 935,000 |
| Over 5,000,000 | 38.5% | -- |

- **Progressive scale application basis** — Progressive scale applied to overall annual net taxable income, rounded down to the nearest XAF 1,000. The headline rates already include the 10% CAC surcharge (statutory base scale 10/15/25/35% + 10% CAC = 11/16.5/27.5/38.5%).  _([PwC -- https://taxsummaries.pwc.com/republic-of-cameroon/individual/taxes-on-personal-income])_
- **Cumulative check** — 2,000,000 x 11% = 220,000; + 1,000,000 x 16.5% = 165,000 -> 385,000; + 2,000,000 x 27.5% = 550,000 -> 935,000. Above 5,000,000, tax = 935,000 + 38.5% of the excess over 5,000,000.  _([PwC])_

### Schedular / special rates

**Schedular / special rates**  _([PwC -- taxes-on-personal-income])_

| Income type | Overall rate (CAC-inclusive) | Source |
| --- | --- | --- |
| Income from stocks/shares (dividends, investment income) | 16.5% (15% + CAC) | [PwC -- taxes-on-personal-income] |
| Other non-commercial / business / professional net profits (actual-earnings regime) | 33% (30% + CAC) | [PwC -- taxes-on-personal-income] |
| Minimum tax (turnover-based, non-salaried, regime-dependent) | 2.2% or 5.5% of turnover | [PwC -- taxes-on-personal-income] |

- **Minimum tax non-application** — Minimum tax does NOT apply to salaried workers or taxpayers under the IGS/discharge system.  _([PwC])_

### Salary income determination

- **Residency scope** — Residents (fiscal domicile in Cameroon) are taxed on worldwide income.  _([PwC -- income-determination])_
- **Net salary base** — Net salary base = gross salary, less a standard 30% lump-sum deduction for professional expenses, less mandatory social contributions (CNPS employee portion).  _([PwC -- income-determination])_

[RESEARCH GAP -- reviewer to confirm] the exact mechanics, ordering, and any cap on the 30% professional-expense deduction against the current General Tax Code; the 30% figure is the standard PwC-reported figure but the statutory wording/cap was not transcribed.

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

- **Minimum viable** — For a salaried client: gross annual (or monthly) salary, residency status, and CNPS contribution records. For a self-employed client: full-year bank statement (CSV, PDF, or pasted text) plus annual VAT-exclusive turnover and chosen tax regime.
- **Recommended** — Monthly payslips, employer DIPE/recapitulative summary, CNPS statements, prior-year annual declaration, VAT registration evidence, CGA membership certificate (if self-employed).
- **Ideal** — Complete income and expenditure account, asset register, evidence of council tax / CRTV withholding, Credit Foncier and FNE deduction records, provisional/instalment payment confirmations.
- **Refusal if minimum is missing** — SOFT WARN. No salary figure or no bank statement at all = hard stop. Bank statement without supporting documents = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify that all figures are supported by valid documentation and that the regime (IGS vs actual-earnings) is correctly determined."

### Refusal Catalogue

- **R-CM-1** — Income type / regime unknown. "Cameroon IRPP applies different scales to salary, investment income, and business profit, and different regimes (IGS vs actual-earnings) to the self-employed. This skill cannot compute tax without knowing the income type and, for the self-employed, the annual turnover. Please confirm before proceeding."  _(R-CM-1)_
- **R-CM-2** — Companies and partnerships. "This skill covers individuals (salaried and sole-trader/self-employed) only. Companies pay corporate income tax (IS) and file separately. Escalate to a Cameroon-qualified practitioner."  _(R-CM-2)_
- **R-CM-3** — Non-resident / expatriate withholding. "Non-resident and expatriate taxation (withholding on Cameroon-source income, treaty relief) has different rules and is out of scope. Escalate to a Cameroon-qualified practitioner."  _(R-CM-3)_
- **R-CM-4** — Capital gains / property disposals. "Capital gains and property-transfer taxation require specialised analysis. Out of scope. Escalate."  _(R-CM-4)_
- **R-CM-5** — Arrears / enforcement. "Client has outstanding tax arrears or is subject to DGI enforcement. Penalties (10%/month late filing, 1.5%/month interest, and 30%-100%/150% bad-faith assessment uplifts) are severe. Do not advise. Escalate immediately."  _(R-CM-5)_
- **R-CM-6** — VAT return requested. "This skill covers IRPP only. Cameroon standard VAT is 19.25% (17.5% + 10% CAC) and is computed separately. [PwC overview]"  _(R-CM-6)_

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

- **Applicability note** — These deductions apply ONLY to self-employed taxpayers under the actual-earnings (regime du reel) regime. Salaried taxpayers rely on the standard 30% lump-sum professional-expense deduction; IGS taxpayers pay a synthetic tax on turnover and do not itemise.  _([PwC income-determination; openhubdigital 2025 Finance Law])_

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
| TAXE COMMUNALE, REDEVANCE COMMUNALE | Council tax (poll) | Flat band -- up to XAF 2,520/mo (Section 2 other-taxes) |
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

## Section 4 -- Worked Examples

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

Classification: Annual IRPP = XAF 2,098,470. Council tax band XAF 2,520/mo and CRTV up to XAF 13,000 apply separately.

### Example 3 -- Dividend / investment income (schedular flat rate)

Input line:
`15/03/2025 ; AFRILAND VIREMENT RECU ; DIVIDENDE SARL XYZ ; +5,000,000 ; XAF`

Reasoning:
Investment income from shares is taxed at the flat schedular overall rate of 16.5% (15% + CAC), not the progressive salary scale. 5,000,000 x 16.5% = 825,000.

Classification: Investment-income IRPP = XAF 825,000 (flat). Do NOT run through the progressive scale.

### Example 4 -- Self-employed under IGS, CGA member

Input: Self-employed (salon), annual VAT-exclusive turnover XAF 12,000,000. Member of an approved Centre de Gestion Agree (CGA).

Reasoning:
- Turnover XAF 12,000,000 is below XAF 50,000,000, so the taxpayer falls under the IGS (Impot General Synthetique) synthetic regime, not actual-earnings. [openhubdigital 2025 Finance Law]
- Worked figure from the authority example: turnover XAF 12,000,000 -> IGS XAF 500,000; as a CGA member the rate is halved to XAF 250,000. [cga.inov.cm IGS 2025 example]
- IGS is declared and paid quarterly within 15 days of each quarter-end.
- [RESEARCH GAP -- reviewer to confirm] the full IGS rate/band table (published only as an image in the secondary source) against the 2025 Code General des Impots (impots.cm/en/node/1212) or the 2025 Finance Law circular.

Classification: Annual IGS = XAF 250,000 (CGA-reduced), paid quarterly. Minimum tax does not apply under IGS.

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

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and Scope

- **Residency and Scope** — Residents (fiscal domicile in Cameroon) are taxed on worldwide income; non-residents are out of scope for this skill (R-CM-3).  _([PwC -- income-determination])_

### 5.2 Salary IRPP Base

- **Salary IRPP Base** — Net taxable salary = gross salary - 30% lump-sum professional-expense deduction - mandatory CNPS employee contributions, rounded down to the nearest XAF 1,000, then the progressive scale in Section 1.  _([PwC -- income-determination; taxes-on-personal-income])_

[RESEARCH GAP -- reviewer to confirm] the exact statutory mechanics and any cap on the 30% deduction.

### 5.3 Progressive Scale (CAC-inclusive)

- **Progressive Scale application** — Apply 11% / 16.5% / 27.5% / 38.5% per Section 1. The rates already include the 10% CAC surcharge.  _([PwC])_

### 5.4 Schedular Income

**Schedular Income**

| Income type | Treatment |
| --- | --- |
| Salary | Progressive scale (Section 1) |
| Dividends / investment income from shares | Flat 16.5% (15% + CAC) [PwC] |
| Non-commercial / business / professional profit (actual-earnings) | Flat 33% (30% + CAC) [PwC] |

### 5.5 Minimum Tax

- **Minimum Tax** — For non-salaried taxpayers under actual-earnings, minimum tax is 2.2% or 5.5% of turnover depending on the applicable regime. It does NOT apply to salaried workers or IGS taxpayers.  _([PwC])_

### 5.6 Social Security -- CNPS (Caisse Nationale de Prevoyance Sociale)

- **CNPS ceiling** — Monthly contribution ceiling for the pension branch: XAF 750,000/month (XAF 9,000,000/year), raised from XAF 300,000 by Presidential Decree.  _([PwC -- other-taxes; CNPS])_

**CNPS Branches Table**

| Branch | Employee | Employer |
| --- | --- | --- |
| Old-age / invalidity / death pension | 4.2% (capped at XAF 750,000/mo) | 4.2% (capped at XAF 750,000/mo) |
| Family allowances (general regime) | 0% | 7% (capped at XAF 750,000/mo) -- agricultural 5.65%, private teachers 3.7% |
| Occupational accidents / risk (class A/B/C) | 0% | 1.75% - 5% by industry risk class (uncapped on gross) |
| **TOTAL CNPS (general regime, lowest risk class)** | **4.2%** | **12.95%** (4.2% + 7% + 1.75%) |
| **TOTAL CNPS (general regime, highest risk class)** | **4.2%** | **16.2%** (4.2% + 7% + 5%) |
| Voluntary insurance (self-employed / optional pension) | 8.4% of declared income | n/a |

- **Employer total check** — Lowest class 4.2 + 7 + 1.75 = 12.95%; highest class 4.2 + 7 + 5 = 16.2%. Employee total = 4.2% (pension only). Sources: employee 4.2% / ceiling XAF 750,000 [PwC -- other-taxes]; employer pension 4.2%, family 7%, occupational 1.75-5% [Rivermate -- rivermate.com/guides/cameroon/taxes]; equal employer/employee pension split [CNPS -- cnps.cm].  _([PwC -- other-taxes]; [Rivermate]; [CNPS -- cnps.cm])_

[RESEARCH GAP -- reviewer to confirm] the exact per-branch employer split and occupational-risk class rates against CNPS regulatory texts (cnps.cm/en/medias/textes-reglementaires1.html); secondary sources are consistent but CNPS did not publish per-branch percentages directly.

### 5.7 Housing Fund and Employment Fund

**Housing Fund and Employment Fund**  _([PwC -- other-taxes])_

| Fund | Employee | Employer | Source |
| --- | --- | --- | --- |
| Credit Foncier du Cameroun (CFC, housing) | 1% | 1.5% | [PwC -- other-taxes] |
| Fonds National de l'Emploi (FNE, employment) | 0% | 1% | [PwC -- other-taxes] |

- **Computation basis** — Both are computed on taxable salary.  _([PwC -- other-taxes])_

### 5.8 Other Individual Withholdings

**Other Individual Withholdings**  _([PwC -- other-taxes])_

| Levy | Amount | Source |
| --- | --- | --- |
| Local Council Tax (Taxe Communale, poll component) | Flat XAF 2,520/month on salaries above XAF 500,000 (top band) | [PwC -- other-taxes] |
| CRTV audiovisual royalty (RAV) | Up to XAF 13,000 for gross salaries above XAF 1,000,000 (graduated) | [PwC -- other-taxes] |

### 5.9 Self-Employed Regimes (2025 Finance Law)

The 2025 Finance Law consolidated the prior layered regimes. Thresholds on annual turnover: [openhubdigital -- updates-to-tax-assessment-regimes-in-cameroons-2025-finance-law]

**Self-Employed Regimes Table**  _([openhubdigital -- updates-to-tax-assessment-regimes-in-cameroons-2025-finance-law])_

| Regime | Annual turnover (XAF) |
| --- | --- |
| IGS (Impot General Synthetique) -- flat synthetic tax | below 50,000,000 |
| Actual-earnings (regime du reel) | 50,000,000 and above (also taxpayers with DGI-approved investment programs > XAF 100,000,000) |

- **IGS mechanics** — IGS is computed on annual VAT-exclusive turnover at graduated rates and declared/paid quarterly within 15 days of each quarter-end. CGA (Centre de Gestion Agree) members get the rate halved.  _([cga.inov.cm -- IGS 2025])_

[RESEARCH GAP -- reviewer to confirm] the IGS rate/band table (image-only in source) against the 2025 CGI or Finance Law circular. The prior layered thresholds (flat below 10M, simplified 10M-50M, real >=50M) are noted as superseded; [RESEARCH GAP -- reviewer to confirm] the exact current wording in the 2025 CGI.

### 5.10 Filing Deadlines

**Filing Deadlines Table**

| Item | Detail | Source |
| --- | --- | --- |
| Year-end | 31 December | [PwC -- tax-administration] |
| Monthly PAYE return (salary) | Filed and paid by 15th of the month following salary payment; employer withholds and remits | [PwC] |
| Annual recapitulative -- senior citizens + public/semi-public employees | 31 July | [PwC] |
| Annual recapitulative -- private-sector employees (Large Taxpayers Unit + specialised centres) | 30 September | [PwC] |
| Annual recapitulative -- other individual taxpayers | 31 October | [PwC] |
| Employer annual income summary (DIPE / etat recapitulatif) | 15 March | [PwC] |
| Regularisation/balance -- Large Taxpayers' Unit | 15 March | [PwC] |
| Regularisation/balance -- Medium-sized & Specialised Centres | 15 April | [PwC] |
| Regularisation/balance -- Divisional Tax Centres | 15 May | [PwC] |
| IGS (self-employed) | Quarterly, within 15 days of each quarter-end | [cga.inov.cm] |
| Record retention | 10 years | [PwC -- tax-administration] |

### 5.11 Penalties

**Penalties Table**

| Penalty | Amount | Source |
| --- | --- | --- |
| Late filing / late declaration | 10% per month, capped at 30% of tax due | [PwC -- tax-administration] |
| Late payment interest | 1.5% per month of tax due | [PwC -- tax-administration] |
| Assessment-related (good/bad faith) | 30% to 100%/150% under the General Tax Code | [PwC; hallelaw 2025 guide] |

[RESEARCH GAP -- reviewer to confirm] the exact bad-faith multiplier in the 2025 Code General des Impots.

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office / Mixed-Use Utilities (actual-earnings)

- **Home Office / Mixed-Use Utilities** — Apportion electricity (ENEO), water (Camwater), internet by business-use proportion. Must be a dedicated, documented basis. Conservative default: 0% deduction until reviewer confirms the basis.

### 6.2 Vehicle Business Use (actual-earnings)

- **Vehicle Business Use** — Only the business-use proportion of fuel, insurance, and maintenance is deductible; requires a usage log. Conservative default: 0% business use until a log is provided.

### 6.3 Phone / Telecom Mixed Use

- **Phone / Telecom Mixed Use** — Business portion only (Orange, MTN, Camtel). Conservative default: 0% until business percentage confirmed.

### 6.4 CNPS Occupational-Risk Class

- **CNPS Occupational-Risk Class** — Employer occupational-accident rate is 1.75%-5% depending on the industry risk class (A/B/C). Flag for reviewer: confirm the client's assigned risk class; default to 1.75% if unknown and flag.

### 6.5 IGS vs Actual-Earnings Boundary

- **IGS vs Actual-Earnings Boundary** — Turnover near XAF 50,000,000 must be confirmed (VAT-exclusive) before choosing a regime. CGA membership halves IGS -- confirm a valid certificate before applying the reduction. Flag for reviewer.

### 6.6 30% Professional Deduction Mechanics

- **30% Professional Deduction Mechanics** — The standard 30% lump-sum salary deduction figure is from PwC; confirm cap/ordering against the CGI. Flag for reviewer.

### 6.7 Entertainment / Gifts

- **Entertainment / Gifts** — Treated as blocked in this skill; confirm any statutory partial allowance with the reviewer before deducting.

## Section 7 -- Excel Working Paper Template

CAMEROON IRPP -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
Taxpayer type: Salaried / Self-employed (IGS) / Self-employed (actual-earnings)
Residency: Resident / Non-resident (STOP if non-resident)

A. SALARIED COMPUTATION (skip if self-employed)
  A1. Gross annual salary                          ___________
  A2. Less 30% professional deduction (A1 x 30%)   ___________
  A3. Less CNPS employee 4.2% (cap base 9,000,000) ___________
  A4. Net taxable (A1 - A2 - A3), round down 1,000 ___________
  A5. IRPP per progressive scale (Section 1)       ___________
  A6. Council tax (up to 2,520/mo)                 ___________
  A7. CRTV royalty (up to 13,000)                  ___________
  A8. Credit Foncier employee 1% (A1 x 1%)         ___________

B. INVESTMENT INCOME (flat 16.5%)
  B1. Dividend / share income                      ___________
  B2. IRPP (B1 x 16.5%)                            ___________

C. SELF-EMPLOYED -- IGS (turnover < 50,000,000)
  C1. Annual VAT-exclusive turnover                ___________
  C2. IGS per band table [RESEARCH GAP]            ___________
  C3. CGA member? halve C2 -> IGS due              ___________

D. SELF-EMPLOYED -- ACTUAL-EARNINGS (turnover >= 50,000,000)
  D1. Turnover (VAT-exclusive)                     ___________
  D2. Less deductible business expenses            ___________
  D3. Net profit (D1 - D2)                         ___________
  D4. IRPP (flat 33%, or scale per reviewer)       ___________
  D5. Minimum tax (2.2% or 5.5% of turnover)       ___________
  D6. Tax due = max(D4, D5)                        ___________

E. TOTAL TAX (pass to deterministic engine)        ___________

REVIEWER FLAGS:
  [ ] Taxpayer type and residency confirmed?
  [ ] CNPS ceiling applied correctly (9,000,000/yr base)?
  [ ] 30% professional deduction mechanics confirmed?
  [ ] IGS band table confirmed against 2025 CGI?
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

## Section 10 -- Reference Material

### Key References

**Key References Table**

| Topic | Reference |
| --- | --- |
| Progressive IRPP scale + CAC | Code General des Impots; [PwC -- taxes-on-personal-income] |
| Salary income determination (30% deduction) | [PwC -- income-determination] |
| Other individual levies (council tax, CRTV, CFC, FNE) | [PwC -- other-taxes] |
| CNPS social security | CNPS (cnps.cm); [PwC -- other-taxes]; [Rivermate] |
| Self-employed regimes (IGS / actual-earnings, 2025 Finance Law) | [openhubdigital -- 2025 Finance Law]; [cga.inov.cm -- IGS 2025] |
| Filing deadlines and administration | [PwC -- tax-administration] |
| Penalties | [PwC -- tax-administration]; [hallelaw 2025 guide] |
| VAT (context) | Standard 19.25% (17.5% + CAC); [PwC overview] |
| Minimum wage (SMIG) | See below |
| Primary authorities | DGI -- https://impots.cm ; CNPS -- https://www.cnps.cm |

### Minimum Wage (SMIG) -- context only

**SMIG Table**

| Sector | Monthly SMIG (XAF) | Source |
| --- | --- | --- |
| Non-agricultural private sector (headline) | 60,000 | [remotepeople; Rivermate -- secondary] |
| Agricultural private sector | 45,000 | [Rivermate -- secondary] |
| State employees baseline | 43,969 (raised from 41,875, Feb 2024) | [Rivermate -- secondary] |

[RESEARCH GAP -- reviewer to confirm] the headline XAF 60,000 SMIG against the labour-ministry SMIG decree (EOR/secondary sources only above).

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
Expected: IGS XAF 500,000 halved to XAF 250,000 (paid quarterly). [RESEARCH GAP on full band table.]

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

- NEVER apply the progressive salary scale to investment income (use flat 16.5%) or to IGS turnover
- NEVER compute final tax figures as definitive -- always label as estimated and pass to the deterministic engine
- NEVER apply CNPS 4.2% on a base above the XAF 9,000,000/year ceiling
- NEVER add the 10% CAC again on top of the 11/16.5/27.5/38.5% scale -- it is already included
- NEVER apply minimum tax to salaried workers or IGS taxpayers
- NEVER itemise business expenses for a salaried taxpayer -- only the 30% lump-sum deduction applies
- NEVER halve IGS without a verified CGA membership certificate
- NEVER treat a non-resident as worldwide-taxed without confirming residency (escalate per R-CM-3)
- NEVER allow fines, penalties, drawings, or income tax itself as a deduction
- NEVER skip the round-down to the nearest XAF 1,000 on the net taxable income
- NEVER rely on a [RESEARCH GAP] figure for a filed return without reviewer confirmation against the 2025 CGI

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
