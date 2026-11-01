---
name: algeria-income-tax
description: "Use this skill whenever asked about Algeria personal income tax (IRG - Impôt sur le Revenu Global) for employees and self-employed individuals. Trigger on phrases like 'how much IRG do I pay', 'barème IRG', 'Algeria income tax', 'IFU', 'impôt forfaitaire unique', 'G50', 'G12', 'G12 bis', 'CNAS', 'CASNOS', 'auto-entrepreneur Algérie', 'DZD tax', 'salaire net', 'self-employed tax Algeria', 'déclaration revenu global', or any question about filing or computing income tax for an Algerian employee, sole trader, or micro-operator. Also trigger when preparing or reviewing an IRG payroll computation, an IFU turnover declaration, social contribution (CNAS/CASNOS) calculations, or advising on filing deadlines. This skill covers the IRG progressive scale, schedular/investment rates, the IFU micro regime, CNAS/CASNOS social contributions, the SNMG minimum wage, filing forms and deadlines, and penalties. ALWAYS read this skill before touching any Algerian income tax work."
version: 0.2
jurisdiction: DZ
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

# Algeria Income Tax (IRG): Employee and Self-Employed v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026 (calendar year). Amounts in Algerian dinars (DA or DZD). Primary authority: Direction Generale des Impots (DGI).

## Who this applies to

Residents and non-residents earning salary, business, professional, rental or investment income in Algeria, and micro-operators under the Impot Forfaitaire Unique (IFU). Companies file IBS and are outside this skill. Hydrocarbons, arrears cases and treaty relief go to a local professional. For TVA use `algeria-vat`; for contributions use `algeria-social-contributions`; for monthly payroll use `algeria-payroll`.

## Rates, bands and thresholds

| Annual taxable income (DA) | Rate | Tax year | Official URL |
|---|---|---|---|
| Up to 240,000 | 0% | 2026 | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| 240,001 to 480,000 | 23% | 2026 | same |
| 480,001 to 960,000 | 27% | 2026 | same |
| 960,001 to 1,920,000 | 30% | 2026 | same |
| 1,920,001 to 3,840,000 | 33% | 2026 | same |
| Over 3,840,000 | 35% | 2026 | same |

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Salary exemption | Up to 30,000 DA a month: no IRG | CIDTA arts. 5 and 68 | 2026 | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| Abatement | 40% of the tax, minimum 1,000, maximum 1,500 DA a month | Taken off the tax, not the income | 2026 | same |
| Second abatement, 30,001 to 35,000 DA | IRG = first-abatement IRG x 137/51 - 27,925/8 | Ordinary employees | 2026 | same |
| Second abatement, disabled workers and pensioners, 30,001 to 42,500 DA | IRG = first-abatement IRG x 93/61 - 81,213/41 | Disabled workers and retirees | 2026 | same |
| Non-monthly bonuses, arrears | 10% | Treated as a separate monthly payment | 2026 | same |
| Occasional teaching, research, invigilation | 10% final | Vacataire work on top of a main job | 2026 | same |
| Other occasional intellectual work | 15% final | CIDTA art. 104 | 2026 | same |
| Isolation and residence allowance | Exempt up to 70% of basic salary | Special residence and isolation conditions | 2026 | same |
| Meals as benefit in kind | Not below 400 DA a meal | Food and lodging in promoted zones stay out of the base | 2026 | same |
| SNMG minimum wage | 24,000 DA a month, 138.46 DA an hour | 40 hours a week, 173.33 hours a month; Decree 26-01 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf |

**Other income and regimes**

| Item | Amount | Conditions | Tax year | Official URL |
|---|---|---|---|---|
| Dividends and similar income | 10% final | CIDTA art. 104-II-4-a as rewritten by LF 2026 art. 11; was 15% in the old skill | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| Gains on shares | 15% final | CIDTA art. 104-II-5-b, LF 2025 art. 8 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf |
| Gains on shares reinvested | 5% | Written commitment to reinvest by 31 Dec of the next year; breach costs the difference plus 25% | 2026 | same |
| Sale of only home | 50% tax reduction | Sole property and main home | 2026 | same |
| Property with unknown cost | Cost set at 40% of sale price | CIDTA art. 78, LF 2026 art. 9 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| Rent, housing | 7% of gross | Annual gross up to 1,800,000 DA | 2026 | https://web.archive.org/web/20261012151216/https://www.mfdgi.gov.dz/fr/particuliers/irg-revenu-foncier-provenant-des-proprietes-baties-et-non-baties-louees |
| Rent, unfurnished commercial or professional | 15% of gross | Same ceiling; also contracts with companies | 2026 | same |
| Rent, bare land | 15% of gross | Same ceiling | 2026 | same |
| Rent, agricultural land | 10% of gross | Same ceiling | 2026 | same |
| Rent above 1,800,000 DA | 7% provisional, credited against final IRG | Filed on G n° 51; 25% abatement on housing rent, not for company contracts | 2026 | same |
| IFU ceiling | 8,000,000 DA turnover | Individuals, art and craft cooperatives, professional civil companies; art. 282 ter, LF 2025 art. 22 | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf |
| IFU, production and sale of goods | 5% | CIDTA art. 282 sexies | 2026 | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu |
| IFU, other activities and professions | 12% | CIDTA art. 282 sexies; mixed activity pro rata | 2026 | same |
| IFU, auto-entrepreneur | 0.5%, ceiling 5,000,000 DA | CIDTA art. 282 ter and sexies, LF 2023 art. 51 | 2026 | same |
| IFU, digital platforms and network sales | 5% final withholding | Held by the company | 2026 | same |
| IFU minimum | 30,000 DA a year | Art. 365 bis, LF 2025 art. 29; was 20,000 in the old skill; paid in full by 30 June | 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf |
| IFU minimum, auto-entrepreneur | 10,000 DA a year | Same article | 2026 | same |
| Professional activity tax (TAP) | Removed | DGI circular of 13 Feb 2024 | 2026 | https://web.archive.org/web/20250219180444/http://mfdgi.gov.dz/fr/a-propos/actu-fr/circulaire-relative-a-la-suppression-de-la-taxe-sur-l-lactivite-professionnelle-tap |
| Interest | unverified: 10% in the old skill | Not read in the law | 2026 | unverified |


## The base

Residents are taxed on worldwide income and non-residents on Algerian income: this is the old skill's rule, and the CIDTA text was not opened, so treat it as unverified.

Salary: start from pay plus accessories and benefits in kind, deduct pension withholdings and the employee social share, then apply the bands monthly (CIDTA arts. 69 to 73, 104). Exempt items include mission costs, zone allowances, family allowances, redundancy pay and court-ordered pensions (https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires).

IFU: tax is on turnover, with no expense deduction. Excluded from IFU: property development, import for resale, wholesale, dealers, private clinics and labs, classified hotels and restaurants, precious metals, public works, plus from 2025 alcohol outlets, tobacco leaf, caterers, venue hire, large-format retail, vehicle and equipment hire, travel, advertising, training and insurance agents (https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf, art. 22; https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu). IFU continues for the first year the ceiling is passed and the next year (art. 282 ter). Exempt: disabled persons' associations, theatre troupes, qualifying traditional artisans; start-up label holders for 4 years plus 1 on renewal; ANADE, ANGEM and CNAC promoters for a period, still paying the minimum.

Records under IFU: purchase and sales registers stamped by the tax office, or a daily journal for services.

### Carried from the earlier version, not checked against the law

Patterns, defaults and refusal rules kept so no work is lost. Any figure here is unverified unless it also appears in the tables above; the tables win.

#### Required Inputs

**Minimum viable**: bank statement and/or payslip (bulletin de paie) for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) residency, (b) employment vs self-employment, and (c) for self-employed, annual turnover (to determine IFU vs real regime).

**Recommended**: payslips for all months, CNAS/CASNOS contribution records, prior-year IRG assessment or G50/G12 declarations, sales invoices (self-employed), confirmation of dependents/marital status.

**Ideal**: complete income and expenditure account, asset register, all G50 monthly declarations, IFU G12/G12 bis filings, proof of provisional instalments.

**Refusal if minimum is missing: SOFT WARN.** No statement or payslip at all = hard stop. Statement without supporting documents = proceed with reviewer warning: "This computation was produced from a bank statement / payslip alone. The reviewer must verify the IRG base, social contribution deductions, and any allowances against the CIDTA and the Finance Laws 2025 and 2026."

#### Refusal Catalogue

- **R-DZ-1**: Residency unknown. "Residency determines whether worldwide or only Algeria-sourced income is taxable. This skill cannot compute IRG without confirming residency. Please confirm before proceeding."
- **R-DZ-2**: Companies and partnerships. "This skill covers individual IRG, IFU micro-operators, and employee payroll only. Companies file IBS (corporate tax) separately. Escalate to an Algerian tax professional."
- **R-DZ-3**: Non-resident / expat with treaty relief. "Non-resident taxation and double-tax-treaty relief require specialised analysis. Out of scope. Escalate to an Algerian tax professional."
- **R-DZ-4**: Hydrocarbons / mining-sector income. "The hydrocarbons sector has a distinct fiscal regime. Out of scope. Escalate to a specialist."
- **R-DZ-5**: Arrears / enforcement. "Client has outstanding tax or social-contribution arrears (CNAS 10% + 3%/month, CASNOS 5% + 1%/month, IFU surcharges up to 25%). Do not advise. Escalate to an Algerian tax professional immediately."
- **R-DZ-6**: VAT (TVA) return requested. "This skill covers income tax (IRG/IFU) and related social contributions only. For Algerian VAT (TVA, standard 19%), use a dedicated VAT skill."


This is the deterministic pre-classifier. When a bank statement / ledger transaction matches a pattern below, apply the treatment directly. Patterns use the local terminology (French/Arabic transliteration) common on Algerian bank statements. Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

#### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: SALAIRE, PAIE, RÉMUNÉRATION, EMPLOYEUR [name] | Employment income (IRG salary base) | Subject to monthly barème IRG after 9% CNAS |
| HONORAIRES, PRESTATION, FACTURE [nº], CLIENT | Business income | Self-employed: IFU turnover or real-regime revenue |
| VIREMENT REÇU, VERSEMENT, DÉPÔT | Potential income | Check direction and counterparty |
| STRIPE, PAYPAL, WISE, PAYONEER PAYOUT | Business income | Platform payout: match to invoices |
| unverified: LOYER REÇU, LOCATION | Rental income | Schedular property rate (see Section 1) |
| DIVIDENDES | Investment income | 10% final (see the rates table) |
| unverified: INTÉRÊTS, PRODUITS FINANCIERS | Investment income | 10% withholding |
| REMBOURSEMENT IMPÔT, RISTOURNE DGI | EXCLUDE | Tax refund, not income |
| SUBVENTION, AIDE ÉTAT | Check nature | Capital grants EXCLUDE; revenue grants = income |

#### 3.2 Expense Patterns (Debits): Deductible (real regime / IFU does NOT deduct expenses)

**3.2 Expense Patterns (Debits): Deductible (real regime / IFU does NOT deduct expenses)**

| Pattern | Category | Treatment | Notes |
| -- | -- | -- | -- |
| LOYER LOCAL, BAIL COMMERCIAL | Business premises rent | Deductible (real regime) | Dedicated business premises |
| ASSURANCE PRO, RC PROFESSIONNELLE | Professional insurance | Deductible (real regime) |  |
| COMPTABLE, EXPERT-COMPTABLE, HONORAIRES COMPTA | Accountancy fees | Deductible (real regime) |  |
| AVOCAT, NOTAIRE, FRAIS JURIDIQUES | Legal fees | Deductible (real regime) | Must be business-related |
| FOURNITURES BUREAU, PAPETERIE | Office supplies | Deductible (real regime) |  |
| PUBLICITÉ, MARKETING, GOOGLE ADS, META ADS | Advertising | Deductible (real regime) |  |
| FRAIS BANCAIRES, COMMISSION BANCAIRE | Bank charges | Deductible (real regime) | Business account only |
| HÉBERGEMENT WEB, NOM DE DOMAINE, SAAS, ABONNEMENT LOGICIEL | IT / software | Deductible (real regime) | Capitalise if a durable asset |

**IFU note:** under the IFU micro regime, tax is a flat percentage of *turnover*: business expenses are NOT separately deductible. The deductible patterns below apply only to operators taxed under the *real regime* (régime réel).

#### 3.3 Expense Patterns (Debits): Utilities (apportion if mixed use)

**3.3 Expense Patterns (Debits): Utilities (apportion if mixed use)**

| Pattern | Category | Tier | Notes |
| -- | -- | -- | -- |
| unverified: SONELGAZ | Electricity/gas | T2 | 100% if dedicated premises; apportion if home |
| unverified: SEAAL, ADE | Water | T2 | Apportion if home premises |
| unverified: ALGÉRIE TÉLÉCOM, IDOOM, DJEZZY, MOBILIS, OOREDOO | Telecoms | T2 | Business-use portion only; default 0% if mixed |

#### 3.4 Expense Patterns (Debits): NOT Deductible

**3.4 Expense Patterns (Debits): NOT Deductible**

| Pattern | Category | Treatment | Notes |
| -- | -- | -- | -- |
| RESTAURANT, REPAS CLIENT, RÉCEPTION | Entertainment / meals | Confirm with reviewer | Deductibility limited: (unverified) |
| COURSES, SUPERMARCHÉ, ARDIS, UNO | Personal / groceries | NOT deductible | Private living costs |
| AMENDE, PÉNALITÉ, CONTRAVENTION | Fines/penalties | NOT deductible | Public policy |
| IMPÔT, IRG, IBS, PAIEMENT DGI | Tax payments | NOT deductible | Tax cannot reduce income |
| PRÉLÈVEMENT PERSONNEL, RETRAIT ESPÈCES (personnel) | Drawings | NOT deductible | Not an expense |

#### 3.5 Social & Tax Movements (special handling)

**3.5 Social & Tax Movements (special handling)**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| unverified: CNAS, COTISATION SÉCURITÉ SOCIALE | Social contribution | Employee 9% reduces IRG base; remit with G50 |
| unverified: CASNOS | Self-employed contribution | 15% of declared base; annual |
| unverified: G50, VERSEMENT DGI MENSUEL | Withholding remittance | Monthly IRG remittance: not an expense |
| ACOMPTE PROVISIONNEL, INSTALMENT IRG | Provisional instalment | Credit against final liability, not an expense |
| TVA, PAIEMENT TVA | VAT payment | EXCLUDE: VAT liability, not expense |

#### 3.6 Exclusions (Neither Income nor Expense)

**3.6 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| -- | -- | -- |
| VIREMENT INTERNE, COMPTE PROPRE, ENTRE COMPTES | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRÊT, ÉCHÉANCE CRÉDIT | EXCLUDE (principal) | Loan principal movement |

#### 3.7 Algerian Banks: Statement Format Reference

**3.7 Algerian Banks: Statement Format Reference**

| Bank | Common patterns | Notes |
| -- | -- | -- |
| BNA (Banque Nationale d'Algérie) | VIREMENT, PRÉLÈVEMENT, FRAIS | PDF; French descriptions, date DD/MM/YYYY |
| CPA (Crédit Populaire d'Algérie) | VRT, PRLV, COMMISSION | PDF; counterparty in libellé field |
| BEA (Banque Extérieure d'Algérie) | VIREMENT, DÉPÔT, RETRAIT | PDF; common for businesses |
| BADR / BDL | VRT, PRLV, FRAIS | PDF; agricultural/development focus |
| Al Salam / AGB (private) | VIREMENT, CARTE, FRAIS | PDF/CSV; cleaner counterparty names |

```
ALGERIA INCOME TAX: IRG / IFU WORKING PAPER
Tax Year: 2026
Client: ___________________________
Residency: Resident / Non-resident
Regime: Employee (IRG payroll) / Self-employed real / IFU micro

PART A: EMPLOYEE IRG (monthly)
  A1. Gross monthly salary (DZD)                  ___________
  A2. Less CNAS employee 9% (A1 × 0.09)           ___________
  A3. IRG taxable base (A1 - A2)                  ___________
  A4. If A3 <= 30,000 -> IRG = 0 (exempt)         ___________
  A5. Annualised base (A3 × 12)                   ___________
  A6. Annual IRG (apply progressive scale)        ___________
  A7. Monthly tax before abatement (A6 / 12)      ___________
  A8. Abatement: 40% of A7, min 1,000, max 1,500  ___________
  A9. Monthly IRG (A7 - A8, then second abatement if in band) ___________
  A10. Net pay (A1 - A2 - A9)                     ___________
  [Spouse/dependent allowance: (unverified)

PART B: SELF-EMPLOYED IFU
  B1. Annual turnover (DZD)                        ___________
  B2. Eligible? (B1 <= 8,000,000)  Y / N           ___________
  B3. Activity: goods (5%) / services (12%)        ___________
  B4. IFU = B1 × rate                              ___________
  B5. Minimum IFU (DZD 30,000; auto-entrepreneur 10,000) ___________
  B6. IFU due = max(B4, B5)                        ___________

PART C: SELF-EMPLOYED REAL REGIME
  C1. Gross business income                        ___________
  C2. Less deductible expenses (real regime only)  ___________
  C3. Net taxable income (C1 - C2)                 ___________
  C4. IRG (apply progressive scale)                ___________

PART D: SOCIAL CONTRIBUTIONS
  D1. CNAS employee 9% (employee)                  ___________
  D2. CNAS employer 26% (employer)                 ___________
  D3. CASNOS 15% of declared base (self-employed)  ___________

PART E: FILING
  E1. G50 monthly remittance (within 20 days)      ___________
  E2. G12 provisional (30 June)                    ___________
  E3. G12 bis final (20 January)                   ___________
  E4. Annual return G n° 1 (30 June)               ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Regime confirmed (IRG real / IFU / employee)?
  [ ] Turnover <= 8,000,000 for IFU verified?
  [ ] IFU rate split (5%/12%) confirmed against the turnover mix?
  [ ] Spouse/dependent allowances confirmed vs CIDTA?
  [ ] CNAS per-branch split confirmed vs AAPI?
  [ ] CASNOS base confirmed vs official CASNOS site?
  [ ] Isolation/special-conditions exemption checked?
```

#### 6.1 IFU vs Real Regime Election

Turnover near the DZD 8,000,000 ceiling, or mixed goods/services activities, require judgement on regime and rate split.
**Flag for reviewer:** confirm turnover total, activity classification, and whether the auto-entrepreneur sub-regime (≤ DZD 5,000,000, 0.5% (unverified)) applies.

#### 6.2 Spouse / Dependent Allowances

Secondary sources cite a spouse reduction (~DZD 1,500/month) and per-dependent allowance (~DZD 12,000). Not confirmed by unverified note.
**Conservative default:** apply NO allowance until confirmed against the CIDTA.

#### 6.3 Home / Mixed-Use Premises (real regime)

Apportion electricity (SONELGAZ), water (SEAAL/ADE), and telecoms by genuine business-use percentage.
**Conservative default:** 0% until documented.

#### 6.4 Vehicle Business Use (real regime)

Only the business-use % of fuel, insurance, and depreciation is deductible; requires a usage log.
**Conservative default:** 0% business use until a log is provided.

#### 6.5 Entertainment / Client Meals

Deductibility is limited under the CIDTA. (unverified)
**Flag for reviewer** before allowing any deduction.

#### 6.6 Isolation / Special-Conditions Exemption

Up to 70% of basic salary may be PIT-exempt for special living/isolation conditions.
**Flag for reviewer:** confirm eligibility and the exempt portion. *(Source: unverified note: Income determination.)*

#### 6.7 Schedular Income Interaction

Rental, dividend, and interest income carry separate withholding; confirm whether final or creditable against the annual return.

#### Algerian Bank Statement Formats

**Algerian Bank Statement Formats**

| Bank | Format | Key fields | Notes |
| -- | -- | -- | -- |
| BNA | PDF | Date, Libellé, Débit, Crédit, Solde | French; date DD/MM/YYYY |
| CPA | PDF | Date, Libellé, Montant, Solde | Counterparty in libellé |
| BEA | PDF | Date, Opération, Débit, Crédit | Common for businesses |
| BADR / BDL | PDF | Date, Libellé, Mouvement, Solde | Development/agricultural |
| AGB / Al Salam (private) | PDF/CSV | Date, Counterparty, Amount | Cleaner counterparty names |

#### Key Algerian Banking / Tax Terms

**Key Algerian Banking / Tax Terms**

| Term (FR/AR translit.) | English | Classification hint |
| -- | -- | -- |
| VIREMENT / VRT | Transfer | Check direction for income/expense |
| PRÉLÈVEMENT / PRLV | Direct debit | Regular expense (utility, CASNOS) |
| SALAIRE / PAIE | Salary | Employment income (IRG base) |
| HONORAIRES | Professional fees | Business income |
| FRAIS / COMMISSION | Charges / fees | Deductible (real regime) |
| LOYER | Rent | Premises expense or rental income |
| COTISATION | Contribution | CNAS / CASNOS |
| RETRAIT / ESPÈCES | Cash withdrawal | Ask what cash was spent on |
| SOLDE | Balance | Running balance |

- NEVER compute IRG without confirming residency.
- NEVER apply the IRG scale to a salary ≤ DZD 30,000/month: it is exempt.
- NEVER deduct business expenses under the IFU micro regime: IFU is a flat % of turnover.
- NEVER apply spouse/dependent allowances until confirmed against the CIDTA (currently (unverified)).
- NEVER use the old DZD 20,000 IFU minimum: it is 30,000 DA, or 10,000 DA for auto-entrepreneurs.
- NEVER allow fines, penalties, or income tax itself as a deduction.
- NEVER include VAT (TVA) collected in business income.
- NEVER treat CNAS/CASNOS contributions or provisional instalments as ordinary expenses.
- NEVER present any (unverified) figure as authoritative.
- NEVER present tax calculations as definitive: always label as estimated, pending professional review.

## Deadlines and filing

| Obligation | Form | Deadline | Official URL |
|---|---|---|---|
| Annual income return | Serie G n° 1 | 30 June (CIDTA art. 99, LF 2025 art. 7); 2025 income extended to 30 July 2026 | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf |
| Employer annual salary statement | Serie G n° 29 | 30 April, with each employee's NIN (LF 2026 art. 8) | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| Employer monthly IRG payment | G n° 50 | First 20 days of the next month | same |
| IFU employer IRG | G n° 50 ter | 20 of the month after the quarter | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu |
| IFU forecast | Serie G n° 12 | 30 June; 2026 forecast extended to 30 July 2026 | https://web.archive.org/web/20260626065530/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-g12-previsionnelle-2026 |
| IFU final | Serie G n° 12 bis | 20 January of next year | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu |
| Registration | Serie G n° 8 | 30 days from starting | same |
| Rent, above ceiling | G n° 51 | With provisional payment | https://web.archive.org/web/20261012151216/https://www.mfdgi.gov.dz/fr/particuliers/irg-revenu-foncier-provenant-des-proprietes-baties-et-non-baties-louees |
| Wealth tax | Online portal | Every 4 years, by 30 April (art. 281 undecies) | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |

How to file an IFU forecast: (1) get Serie G n° 12 from the DGI downloads area or your tax centre; (2) enter forecast turnover at the inspection or proximity tax centre for your place of tax; (3) pay all of it by 30 June, or 50% then, 25% from 1 to 15 September and 25% from 1 to 15 December on the same form; the minimum cannot be split; (4) keep the copy stamped by the receiver; (5) file G n° 12 bis by 20 January with actual turnover and net income, paying any top-up. New taxpayers file only G n° 12 bis, by 20 January after the start year (CPF art. 3 bis).

How to file G n° 1: (1) get the form from the DGI; (2) file at the tax office of your home by 30 June; (3) list each income type; employees with other income take a credit equal to notional IRG on main salary (https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires). Box numbers are unverified: follow the form.

Provisional instalments: new taxpayers skip them in the first year; overpayments are credited or refunded on request within 4 years (art. 355, LF 2026 art. 26).

## Penalties and interest

| Failure | Result | Official URL |
|---|---|---|
| No G n° 50 or payment | 10%, 25% after a month's formal notice (art. 134-2) | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires |
| No G n° 29 | 5% of annual payroll | same |
| Late rent or IFU payment | 10%, then 3% a month from one month, capped at 25% (art. 402-1) | https://web.archive.org/web/20261012151216/https://www.mfdgi.gov.dz/fr/particuliers/irg-revenu-foncier-provenant-des-proprietes-baties-et-non-baties-louees |
| Late IFU declaration | 10% up to 1 month, 20% beyond (page predates LF 2025) | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu |
| Late nil IFU final | 2,500, 5,000 or 10,000 DA by delay | same |
| No G n° 8 | 30,000 DA (art. 194) | same |
| Office assessment | Tax increased by 25% (art. 192, LF 2026 art. 17) | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf |
| Tax fraud | 2 to 5 years; 5 to 10 years and 5,000,000 to 10,000,000 DA if organised (art. 303) | same |


## Cross-border points

Pensions paid to people domiciled abroad follow the monthly scale. Artists domiciled abroad bear 15% on fees, with exceptions (https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires). Pay from an employer with no Algerian tax home: the employee computes and pays the tax. Treaty relief is out of scope; refer it.

## Two worked examples that recompute

**Example 1, simple.** Gross 120,000 DA. Employee share 9% = 10,800; taxable 109,200; annualised 1,310,400; scale gives 289,920, or 24,160 a month; abatement capped at 1,500; IRG 22,660; net 86,540.

```oa-check
name: Employee, gross 120,000 DA a month
inputs:
  gross: 120000
steps:
  - cnas: gross * 0.09
  - base: gross - cnas
  - annual: base * 12
  - tax_year: (min(annual,480000)-240000)*0.23 + (min(annual,960000)-480000)*0.27 + (annual-960000)*0.30
  - before: tax_year / 12
  - abate: clamp(before * 0.40, 1000, 1500)
  - irg: before - abate
  - net: gross - cnas - irg
expected:
  irg: 22660.00
  net: 86540.00
```

**Example 2, decision: IFU or real regime at 7,000,000 DA for a consultant.** IFU costs 12% x 7,000,000 = 840,000 DA with no deductions. Under the real regime with profit P, the scale applies; tax equals IFU at P = 3,032,727 DA. Below that profit the real regime is cheaper before bookkeeping costs; above it IFU wins.

```oa-check
name: IFU against real regime at 7,000,000 DA turnover
inputs:
  turnover: 7000000
  profit: 3032727.27
steps:
  - ifu: turnover * 0.12
  - real: 472800 + (profit - 1920000) * 0.33
expected:
  ifu: 840000.00
  real: 840000.00
```

## Ask the client first

1. Resident or not?
2. Employee, self-employed real regime, IFU or auto-entrepreneur?
3. Turnover, and goods or services?
4. Gross monthly pay, and disabled or retired status?
5. Rental, dividend or share-sale income?
6. Any excluded IFU activity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi de finances pour 2026, JO n° 88 of 31 Dec 2025 (read: fiscal articles 5 to 29, 53 to 60); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2025/F2025088.pdf | 2026-11-01 |
| Loi de finances pour 2025, JO n° 84 of 26 Dec 2024 (read: arts. 7, 8, 22, 23, 26 to 29); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2024/F2024084.pdf | 2026-11-01 |
| Presidential Decree 26-01 of 7 Jan 2026, JO 2026 n° 1 (read: arts. 1 and 2); read for the rates and steps cited | https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026001.pdf | 2026-11-01 |
| DGI, IRG traitements et salaires, archived copy of 1 Sep 2026 (page cites LF 2026); read for the rates and steps cited | https://web.archive.org/web/20260901165005/https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires | 2026-11-01 |
| DGI, IRG revenus fonciers, archived copy of 12 Oct 2026; read for the rates and steps cited | https://web.archive.org/web/20261012151216/https://www.mfdgi.gov.dz/fr/particuliers/irg-revenu-foncier-provenant-des-proprietes-baties-et-non-baties-louees | 2026-11-01 |
| DGI, IFU regime page, archived copy of 19 Feb 2025; dated 24 Oct 2023, so LF 2025 overrides it; read for the rates and steps cited | https://web.archive.org/web/20250219043244/https://mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu | 2026-11-01 |
| DGI, circular notice on removing TAP, 13 Feb 2024, archived copy; read for the rates and steps cited | https://web.archive.org/web/20250219180444/http://mfdgi.gov.dz/fr/a-propos/actu-fr/circulaire-relative-a-la-suppression-de-la-taxe-sur-l-lactivite-professionnelle-tap | 2026-11-01 |
| DGI notice extending the 2025 annual declarations, archived copy of 8 Oct 2026; read for the rates and steps cited | https://web.archive.org/web/20261008093610/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-des-declarations-annuelles-2025 | 2026-11-01 |
| DGI notice extending G12 for 2026, archived copy of 26 Jun 2026; read for the rates and steps cited | https://web.archive.org/web/20260626065530/https://www.mfdgi.gov.dz/about-us-ar/actu-ar/prorogation-g12-previsionnelle-2026 | 2026-11-01 |

mfdgi.gov.dz and cnas.dz refused every direct and Chrome connection on 2026-11-01; DGI pages are Internet Archive copies, marked as such.

Not yet confirmed: interest withholding rate (10% in the old skill); property capital gains rate; non-resident capital gains rate (20% in the old skill); equity compensation rate; spouse and dependent reductions; entertainment deduction limits; deductions list for individuals; 4-year limitation period; the current text of CIDTA, because the 2026 codes page could not be opened (mfdgi.gov.dz refuses connections, so archived copies were used, and the code PDFs are not archived); whether any complementary finance law for 2026 changes these figures; whether the 30,000 DA gate is tested on gross or on taxable pay, since the DGI page says "revenus" and the formula only joins up on taxable pay; IFU late-declaration rates after LF 2025, since the DGI page predates it.

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
