---
name: algeria-income-tax
description: Use this skill whenever asked about Algeria personal income tax (IRG -- Impôt sur le Revenu Global) for employees and self-employed individuals. Trigger on phrases like "how much IRG do I pay", "barème IRG", "Algeria income tax", "IFU", "impôt forfaitaire unique", "G50", "G12", "G12 bis", "CNAS", "CASNOS", "auto-entrepreneur Algérie", "DZD tax", "salaire net", "self-employed tax Algeria", "déclaration revenu global", or any question about filing or computing income tax for an Algerian employee, sole trader, or micro-operator. Also trigger when preparing or reviewing an IRG payroll computation, an IFU turnover declaration, social contribution (CNAS/CASNOS) calculations, or advising on filing deadlines. This skill covers the IRG progressive scale, schedular/investment rates, the IFU micro regime, CNAS/CASNOS social contributions, the SNMG minimum wage, filing forms and deadlines, and penalties. ALWAYS read this skill before touching any Algerian income tax work.
version: 0.1
jurisdiction: DZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Algeria Income Tax (IRG) -- Employee & Self-Employed

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Algeria (People's Democratic Republic of Algeria) |
| Tax | Personal income tax -- IRG (Impôt sur le Revenu Global) |
| Currency | Algerian Dinar (DZD / DA) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Code des Impôts Directs et Taxes Assimilées (CIDTA) |
| Supporting legislation | CIDTA Art. 282 ter (IFU); Loi de Finances 2025; Loi de Finances 2026 (selected measures) |
| Tax authority | Direction Générale des Impôts (DGI) -- mfdgi.gov.dz |
| Social security (employees) | CNAS |
| Social security (self-employed) | CASNOS |
| Filing portal | DGI / Jibaya'tic |
| Annual return deadline | 30 April of the following year (FY2025 extended to 30 June) |
| Validated by | Pending -- requires sign-off by an Algerian tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Algeria DOES levy a personal income tax

Unlike several Gulf jurisdictions, Algeria operates a full personal income tax (IRG) with a progressive scale topping out at 35%, plus mandatory social contributions (CNAS for employees, CASNOS for the self-employed) and a turnover-based micro regime (IFU). Residents are taxed on worldwide income; non-residents on Algeria-sourced income only. *(Source: PwC Worldwide Tax Summaries -- Algeria, Individual -- Taxes on personal income, reviewed 14 Jul 2025: https://taxsummaries.pwc.com/algeria/individual/taxes-on-personal-income)*

### IRG Progressive Scale (2025) -- Annual Taxable Income

**IRG Progressive Scale (2025) -- Annual Taxable Income**  _(Source: PwC -- Algeria, Individual, reviewed 14 Jul 2025: https://taxsummaries.pwc.com/algeria/individual/taxes-on-personal-income)_

| Annual taxable income (DZD) | Rate | Cumulative tax at top of band |
| --- | --- | --- |
| 0 -- 240,000 | 0% | DZD 0 |
| 240,001 -- 480,000 | 23% | DZD 55,200 |
| 480,001 -- 960,000 | 27% | DZD 184,800 |
| 960,001 -- 1,920,000 | 30% | DZD 472,800 |
| 1,920,001 -- 3,840,000 | 33% | DZD 1,106,400 |
| > 3,840,000 | 35% | -- |

**Cumulative tax derivation (arithmetic, recomputed):**
- 23% × 240,000 = 55,200
- 55,200 + (27% × 480,000 = 129,600) = 184,800
- 184,800 + (30% × 960,000 = 288,000) = 472,800
- 472,800 + (33% × 1,920,000 = 633,600) = 1,106,400

- **Salary exemption** — Monthly salaries ≤ DZD 30,000 are exempt from IRG.  _(Source: PwC -- Income determination: https://taxsummaries.pwc.com/algeria/individual/income-determination)_
- **Isolation / special-conditions exemption** — PIT exemption of up to 70% of basic salary for special living/isolation conditions (since 1 Jan 2021).  _(Source: PwC -- Income determination, same URL.)_

### Schedular / Investment Income Rates (2025)

**Schedular / Investment Income Rates (2025)**  _(Source: PwC -- Income determination: https://taxsummaries.pwc.com/algeria/individual/income-determination)_

| Income type | Rate | Notes |
| --- | --- | --- |
| Dividends | 15% | Residents & non-residents |
| Interest | 10% |  |
| Capital gains | 15% residents / 20% non-residents |  |
| Equity compensation | 35% (top marginal) |  |
| Business income (real regime) | Up to 35% (progressive) |  |

### Rental / Property Income (annual gross ≤ DZD 1,800,000)

**Rental / Property Income (annual gross ≤ DZD 1,800,000)**  _(Source: PwC -- Income determination, same URL.)_

| Property type | Withholding rate |
| --- | --- |
| Residential | 7% |
| Unfurnished commercial/professional | 15% |
| Bare land | 15% |
| Agricultural land | 10% |
| Income > DZD 1,800,000 | Provisional 7%, creditable against final annual tax |

### IFU -- Impôt Forfaitaire Unique (Micro Regime)

**IFU -- Impôt Forfaitaire Unique (Micro Regime)**  _(Eligibility source: CIDTA Art. 282 ter and DGI IFU page: https://www.mfdgi.gov.dz/fr/professionnels/services-pro/regime-forfaitaire-unique/ifu)_

| Field | Value |
| --- | --- |
| Eligibility | Annual turnover ≤ DZD 8,000,000 (CIDTA Art. 282 ter) |
| Rate -- production & sale of goods | 5% **[RESEARCH GAP -- reviewer to confirm: official mfdgi.gov.dz IFU page blocked on fetch; 5%/12% split from secondary Algerian tax sources]** |
| Rate -- services & other activities | 12% **[RESEARCH GAP -- reviewer to confirm, same as above]** |
| Minimum annual IFU tax | DZD 20,000 (raised from 10,000 by Loi de Finances 2025) *(Source: IMF Country Report 25/271: https://www.imf.org/-/media/files/publications/cr/2025/english/1dzaea2025002-source-pdf.pdf)* -- **[RESEARCH GAP: some blogs cite DZD 30,000; prefer 20,000 (IMF) and confirm in the 2025 Finance Law text]** |
| Auto-entrepreneur ceiling | DZD 5,000,000 turnover; reduced IFU rate 0.5% **[RESEARCH GAP -- reviewer to confirm, secondary sources only]** |

- **2025 change** — New taxpayers are exempt from provisional PIT instalments during their first year of activity (effective 1 Jan 2025).  _(Source: PwC -- Tax administration: https://taxsummaries.pwc.com/algeria/individual/tax-administration)_

### Social Contributions -- Quick Rates

**Social Contributions -- Quick Rates**  _(Source: PwC -- Other taxes, reviewed 14 Jul 2025: https://taxsummaries.pwc.com/algeria/individual/other-taxes; CASNOS rate from secondary corroboration -- see Section 5.)_

| Regime | Who | Rate |
| --- | --- | --- |
| CNAS (employee share) | Employees | 9% of gross |
| CNAS (employer share) | Employers | 26% of gross |
| CNAS total | -- | 35% of gross |
| CASNOS | Self-employed | 15% of declared base |

### SNMG (Minimum Wage)

**SNMG (Minimum Wage)**

| Year | Monthly SNMG | Source |
| --- | --- | --- |
| 2025 | DZD 20,000 | In force since June 2020, unchanged through 2025 *(observalgerie.com; acf-dz.com)* |
| 2026 | DZD 24,000 | Presidential Decree n°26-01 dated 7 Jan 2026, effective 1 Jan 2026 *(https://www.acf-dz.com/nouveau-salaire-national-minimum-garantie-snmg-2026/)* |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | STOP -- residency determines worldwide vs Algeria-sourced scope |
| Unknown regime (IRG real vs IFU) | STOP -- do not compute without confirming turnover and regime |
| Unknown whether spouse/dependent allowances apply | Apply NO discretionary allowance ([RESEARCH GAP figures], see Section 5.2) |
| Unknown business-use % (vehicle, phone, premises) | 0% deduction |
| Unknown expense deductibility | Not deductible |
| Unknown CNAS vs CASNOS status | STOP -- employee vs self-employed determines the social regime |
| Salary ≤ DZD 30,000/month | IRG-exempt -- compute social contributions only |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement and/or payslip (bulletin de paie) for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) residency, (b) employment vs self-employment, and (c) for self-employed, annual turnover (to determine IFU vs real regime).

**Recommended** -- payslips for all months, CNAS/CASNOS contribution records, prior-year IRG assessment or G50/G12 declarations, sales invoices (self-employed), confirmation of dependents/marital status.

**Ideal** -- complete income and expenditure account, asset register, all G50 monthly declarations, IFU G12/G12 bis filings, proof of provisional instalments.

**Refusal if minimum is missing -- SOFT WARN.** No statement or payslip at all = hard stop. Statement without supporting documents = proceed with reviewer warning: "This computation was produced from a bank statement / payslip alone. The reviewer must verify the IRG base, social contribution deductions, and any allowances against the CIDTA and the 2025 Finance Law."

### Refusal Catalogue

- **R-DZ-1** — Residency unknown. "Residency determines whether worldwide or only Algeria-sourced income is taxable. This skill cannot compute IRG without confirming residency. Please confirm before proceeding."
- **R-DZ-2** — Companies and partnerships. "This skill covers individual IRG, IFU micro-operators, and employee payroll only. Companies file IBS (corporate tax) separately. Escalate to an Algerian tax professional."
- **R-DZ-3** — Non-resident / expat with treaty relief. "Non-resident taxation and double-tax-treaty relief require specialised analysis. Out of scope. Escalate to an Algerian tax professional."
- **R-DZ-4** — Hydrocarbons / mining-sector income. "The hydrocarbons sector has a distinct fiscal regime. Out of scope. Escalate to a specialist."
- **R-DZ-5** — Arrears / enforcement. "Client has outstanding tax or social-contribution arrears (CNAS 10% + 3%/month, CASNOS 5% + 1%/month, IFU surcharges up to 25%). Do not advise. Escalate to an Algerian tax professional immediately."
- **R-DZ-6** — VAT (TVA) return requested. "This skill covers income tax (IRG/IFU) and related social contributions only. For Algerian VAT (TVA, standard 19%), use a dedicated VAT skill."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement / ledger transaction matches a pattern below, apply the treatment directly. Patterns use the local terminology (French/Arabic transliteration) common on Algerian bank statements. Match by case-insensitive substring on the counterparty name or description. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALAIRE, PAIE, RÉMUNÉRATION, EMPLOYEUR [name] | Employment income (IRG salary base) | Subject to monthly barème IRG after 9% CNAS |
| HONORAIRES, PRESTATION, FACTURE [nº], CLIENT | Business income | Self-employed -- IFU turnover or real-regime revenue |
| VIREMENT REÇU, VERSEMENT, DÉPÔT | Potential income | Check direction and counterparty |
| STRIPE, PAYPAL, WISE, PAYONEER PAYOUT | Business income | Platform payout -- match to invoices |
| LOYER REÇU, LOCATION | Rental income | Schedular property rate (see Section 1) |
| DIVIDENDES | Investment income | 15% withholding |
| INTÉRÊTS, PRODUITS FINANCIERS | Investment income | 10% withholding |
| REMBOURSEMENT IMPÔT, RISTOURNE DGI | EXCLUDE | Tax refund, not income |
| SUBVENTION, AIDE ÉTAT | Check nature | Capital grants EXCLUDE; revenue grants = income |

### 3.2 Expense Patterns (Debits) -- Deductible (real regime / IFU does NOT deduct expenses)

**3.2 Expense Patterns (Debits) -- Deductible (real regime / IFU does NOT deduct expenses)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LOYER LOCAL, BAIL COMMERCIAL | Business premises rent | Deductible (real regime) | Dedicated business premises |
| ASSURANCE PRO, RC PROFESSIONNELLE | Professional insurance | Deductible (real regime) |  |
| COMPTABLE, EXPERT-COMPTABLE, HONORAIRES COMPTA | Accountancy fees | Deductible (real regime) |  |
| AVOCAT, NOTAIRE, FRAIS JURIDIQUES | Legal fees | Deductible (real regime) | Must be business-related |
| FOURNITURES BUREAU, PAPETERIE | Office supplies | Deductible (real regime) |  |
| PUBLICITÉ, MARKETING, GOOGLE ADS, META ADS | Advertising | Deductible (real regime) |  |
| FRAIS BANCAIRES, COMMISSION BANCAIRE | Bank charges | Deductible (real regime) | Business account only |
| HÉBERGEMENT WEB, NOM DE DOMAINE, SAAS, ABONNEMENT LOGICIEL | IT / software | Deductible (real regime) | Capitalise if a durable asset |

**IFU note:** under the IFU micro regime, tax is a flat percentage of *turnover* -- business expenses are NOT separately deductible. The deductible patterns below apply only to operators taxed under the *real regime* (régime réel).

### 3.3 Expense Patterns (Debits) -- Utilities (apportion if mixed use)

**3.3 Expense Patterns (Debits) -- Utilities (apportion if mixed use)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| SONELGAZ | Electricity/gas | T2 | 100% if dedicated premises; apportion if home |
| SEAAL, ADE | Water | T2 | Apportion if home premises |
| ALGÉRIE TÉLÉCOM, IDOOM, DJEZZY, MOBILIS, OOREDOO | Telecoms | T2 | Business-use portion only; default 0% if mixed |

### 3.4 Expense Patterns (Debits) -- NOT Deductible

**3.4 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, REPAS CLIENT, RÉCEPTION | Entertainment / meals | Confirm with reviewer | Deductibility limited -- [RESEARCH GAP: CIDTA entertainment limits, reviewer to confirm] |
| COURSES, SUPERMARCHÉ, ARDIS, UNO | Personal / groceries | NOT deductible | Private living costs |
| AMENDE, PÉNALITÉ, CONTRAVENTION | Fines/penalties | NOT deductible | Public policy |
| IMPÔT, IRG, IBS, PAIEMENT DGI | Tax payments | NOT deductible | Tax cannot reduce income |
| PRÉLÈVEMENT PERSONNEL, RETRAIT ESPÈCES (personnel) | Drawings | NOT deductible | Not an expense |

### 3.5 Social & Tax Movements (special handling)

**3.5 Social & Tax Movements (special handling)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNAS, COTISATION SÉCURITÉ SOCIALE | Social contribution | Employee 9% reduces IRG base; remit with G50 |
| CASNOS | Self-employed contribution | 15% of declared base; annual |
| G50, VERSEMENT DGI MENSUEL | Withholding remittance | Monthly IRG + CNAS remittance -- not an expense |
| ACOMPTE PROVISIONNEL, INSTALMENT IRG | Provisional instalment | Credit against final liability, not an expense |
| TVA, PAIEMENT TVA | VAT payment | EXCLUDE -- VAT liability, not expense |

### 3.6 Exclusions (Neither Income nor Expense)

**3.6 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VIREMENT INTERNE, COMPTE PROPRE, ENTRE COMPTES | EXCLUDE | Own-account transfer |
| REMBOURSEMENT PRÊT, ÉCHÉANCE CRÉDIT | EXCLUDE (principal) | Loan principal movement |

### 3.7 Algerian Banks -- Statement Format Reference

**3.7 Algerian Banks -- Statement Format Reference**

| Bank | Common patterns | Notes |
| --- | --- | --- |
| BNA (Banque Nationale d'Algérie) | VIREMENT, PRÉLÈVEMENT, FRAIS | PDF; French descriptions, date DD/MM/YYYY |
| CPA (Crédit Populaire d'Algérie) | VRT, PRLV, COMMISSION | PDF; counterparty in libellé field |
| BEA (Banque Extérieure d'Algérie) | VIREMENT, DÉPÔT, RETRAIT | PDF; common for businesses |
| BADR / BDL | VRT, PRLV, FRAIS | PDF; agricultural/development focus |
| Al Salam / AGB (private) | VIREMENT, CARTE, FRAIS | PDF/CSV; cleaner counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- Monthly Salary IRG (employee)

**Input line:**
`28/03/2025 ; BNA VIREMENT ; EMPLOYEUR SARL ATLAS ; SALAIRE MARS ; +120,000.00 ; DZD`

**Reasoning:**
Gross monthly salary DZD 120,000. Employee CNAS 9% is deducted first to reach the IRG base.
- CNAS 9% × 120,000 = DZD 10,800
- IRG taxable base = 120,000 − 10,800 = DZD 109,200/month
- The monthly barème IRG is the annual scale ÷ 12. Annualised base = 109,200 × 12 = DZD 1,310,400.
- Annual IRG on 1,310,400: 55,200 (band 2) + 129,600 (band 3) + 30% × (1,310,400 − 960,000 = 350,400) = 55,200 + 129,600 + 105,120 = **DZD 289,920/year** ⇒ **DZD 24,160/month**.

**Classification:** IRG base = DZD 109,200/month; IRG ≈ DZD 24,160/month; net ≈ 120,000 − 10,800 − 24,160 = **DZD 85,040**. *(Salary > DZD 30,000 so not exempt. Source: PwC scale + income-determination.)* **[RESEARCH GAP: any spouse/dependent allowance not applied -- see Section 5.2.]**

### Example 2 -- Exempt Low Salary

**Input line:**
`28/03/2025 ; CPA VIREMENT ; EMPLOYEUR ; SALAIRE ; +28,000.00 ; DZD`

**Reasoning:**
Monthly salary DZD 28,000 ≤ DZD 30,000 threshold ⇒ **IRG-exempt**. Social contributions still apply: CNAS 9% × 28,000 = DZD 2,520. Net = 28,000 − 2,520 = DZD 25,480.

**Classification:** IRG = DZD 0. CNAS employee = DZD 2,520. *(Source: PwC -- Income determination, DZD 30,000 exemption.)*

### Example 3 -- IFU Micro-Operator (sale of goods)

**Input line (annual turnover total from statement):**
Aggregate business credits for 2025 = DZD 6,000,000, activity = retail (sale of goods).

**Reasoning:**
Turnover DZD 6,000,000 ≤ DZD 8,000,000 ⇒ eligible for IFU. Sale of goods rate = 5%.
- IFU = 5% × 6,000,000 = **DZD 300,000**.
- Above the DZD 20,000 minimum, so the computed amount applies.

**Classification:** IFU = DZD 300,000 (declare on G12 bis). *(Eligibility: CIDTA Art. 282 ter. Rate 5% [RESEARCH GAP -- confirm sector split]. Minimum DZD 20,000 from IMF CR 25/271.)*

### Example 4 -- IFU Micro-Operator (services)

**Input line:**
Aggregate service revenue for 2025 = DZD 1,500,000, activity = consulting (services).

**Reasoning:**
Turnover ≤ DZD 8,000,000 ⇒ IFU eligible. Services rate = 12%.
- IFU = 12% × 1,500,000 = **DZD 180,000**.
- Above DZD 20,000 minimum ⇒ DZD 180,000 applies.

**Classification:** IFU = DZD 180,000. *(Rate 12% [RESEARCH GAP -- confirm].)*

### Example 5 -- CASNOS Self-Employed Contribution

**Input line:**
`30/06/2025 ; BEA PRÉLÈVEMENT ; CASNOS ; COTISATION ANNUELLE ; -36,000.00 ; DZD`

**Reasoning:**
CASNOS contribution at 15% of declared base. If declared base = DZD 240,000 (annualised at the 2025 SNMG of DZD 20,000/month), then 15% × 240,000 = **DZD 36,000**.

**Classification:** CASNOS contribution = DZD 36,000 (annual; due no later than 30 June). *(Rate 15% and SNMG floor from secondary corroboration -- see Section 5; SNMG DZD 20,000 from observalgerie/acf-dz.)* **[RESEARCH GAP -- confirm exact CASNOS base on the official CASNOS site.]**

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BNA VIREMENT INTERNE ; COMPTE ÉPARGNE ; ; -200,000.00 ; DZD`

**Reasoning:**
Transfer between own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Residency and Scope

- **Residency and scope** — Residents are taxed on worldwide income; non-residents only on Algeria-sourced income.  _(Source: PwC -- Taxes on personal income.)_

### 5.2 IRG Salary Mechanics and Allowances

- **CNAS-first deduction mechanic** — Gross salary less the employee 9% CNAS contribution gives the IRG taxable base.  _(CNAS 9% from PwC -- Other taxes. The "deduct CNAS first" mechanic is standard payroll practice -- [RESEARCH GAP: confirm exact order against CIDTA salary rules.])_
- **Monthly barème IRG** — The monthly barème IRG = annual progressive scale ÷ 12.
- **Salary exemption threshold** — Salaries ≤ DZD 30,000/month are exempt.  _(Source: PwC -- Income determination.)_

**[RESEARCH GAP -- reviewer to confirm]:** secondary Algerian payroll sources cite a reduction of ~DZD 1,500/month for a non-earning spouse and a per-dependent allowance (≈DZD 12,000/dependent). The PwC authoritative deductions page does NOT confirm these. Do NOT apply them until confirmed against the CIDTA. *(Secondary: https://almawarid.app/blog/comment-calculer-lirg-en-algerie-en-2025-tranches-taux-et-exemples/)*

### 5.3 Deductible vs Non-Deductible (real regime)

- **Deductible/non-deductible items** — Only alimony, mortgage interest, and taxes paid are confirmed deductible for individuals; childcare, education, healthcare, life insurance, and charity are NOT deductible.  _(Source: PwC -- Deductions: https://taxsummaries.pwc.com/algeria/individual/deductions)_

### 5.4 IFU Regime

- **Eligibility** — Annual turnover ≤ DZD 8,000,000 (CIDTA Art. 282 ter), covering industrial, commercial, non-commercial/liberal, artisanal activities and craft cooperatives.  _(Source: DGI IFU page.)_
- **IFU rates** — 5% (production/sale of goods), 12% (services/other). **[RESEARCH GAP -- confirm sector split against the 2025 Finance Law.]**
- **Minimum annual tax** — DZD 20,000  _(IMF CR 25/271; raised from 10,000 in 2025. **[RESEARCH GAP -- some sources say 30,000.]**)_
- **IFU expense treatment** — Under IFU, business expenses are NOT separately deductible -- tax is a flat % of turnover.

### 5.5 Schedular Withholding Rates

- **Schedular withholding rates** — Dividends 15%, interest 10%, capital gains 15% (resident) / 20% (non-resident).  _(Source: PwC -- Income determination.)_

### 5.6 CNAS -- Employee Social Contributions

**CNAS -- Employee Social Contributions total**  _(Source: PwC -- Other taxes, 14 Jul 2025.)_

| Share | Rate of gross |
| --- | --- |
| Employee | 9% |
| Employer | 26% |
| **Total** | **35%** |

**Arithmetic check:** 9% + 26% = 35%. ✓

Coverage: retirement, illness/maternity, unemployment, work accidents. No upper contribution ceiling is confirmed by PwC; the floor is the SNMG. *(Source: PwC -- Other taxes.)*

**Branch breakdown (secondary -- almawarid.app)**  _(almawarid.app)_

| Branch | Employer | Employee |
| --- | --- | --- |
| Social insurance (health/maternity) | 12.5% | 1.5% |
| Retirement | 10.5% | 6.75% |
| Work accidents | 1.25% | -- |
| Unemployment (FNAC) | 1.5% | 0.5% |
| Balance / other | ~0.25% | ~0.25% |

**[RESEARCH GAP -- reviewer to confirm]:** the published sub-rows total ~25.75% employer / 9.25% employee; the exact per-branch allocation reconciling precisely to 26% / 9% must be confirmed against the AAPI official page (https://aapi.dz/en/regimes-sociaux-en/). The headline 26% / 9% / 35% totals are PwC-confirmed; only the per-branch split is uncertain.

### 5.7 CASNOS -- Self-Employed Social Contributions

- **CASNOS rate** — Rate: 15% of declared contribution base (split ~7.5% health / ~7.5% retirement). **[RESEARCH GAP -- secondary sources only; confirm on the official CASNOS site.]**  _(Source: https://noteasy-dz.com/en/employment-and-social-security-self-employed-regime/ and search corroboration.)_
- **Minimum base and payment** — Minimum base: the SNMG. Minimum contribution ≈ 15% × annual SNMG. Payment: annual, due from 1 January, payable no later than 30 June.  _(Source: https://noteasy-dz.com/en/employment-and-social-security-self-employed-regime/ and search corroboration.)_
- **CASNOS late penalty** — Late penalty: 5% surcharge + 1% per additional month of delay.  _(Source: https://noteasy-dz.com/en/employment-and-social-security-self-employed-regime/ and search corroboration.)_

### 5.8 SNMG (Minimum Wage)

**5.8 SNMG (Minimum Wage)**

| Year | Monthly SNMG |
| --- | --- |
| 2025 | DZD 20,000 *(observalgerie.com; acf-dz.com)* |
| 2026 | DZD 24,000 *(Presidential Decree n°26-01, 7 Jan 2026; acf-dz.com)* |

- **2026 hourly rate** — 2026 hourly rate DZD 138.46 (40h/week ⇒ 173.33h/month).  _(Source: acf-dz.com.)_

### 5.9 Filing Forms & Deadlines

**5.9 Filing Forms & Deadlines**  _(Tax-form sources: PwC -- Tax administration: https://taxsummaries.pwc.com/algeria/individual/tax-administration; DGI IFU page; mfdgi IRG salaries page: https://www.mfdgi.gov.dz/fr/particuliers/irg-traitements-et-salaires)_

| Obligation | Form | Deadline |
| --- | --- | --- |
| Annual individual income tax return (revenu global) | série G | 30 April (FY2025 extended to 30 June) |
| Monthly withholding declaration & remittance (payroll IRG + CNAS) | G50 | Within 20 days following the month of payment |
| IFU provisional turnover declaration | G12 | 30 June |
| IFU final/definitive turnover declaration | G12 bis | 20 January of following year |
| Employer annual payroll declaration | G29 | Within prescribed timeframe |
| CNAS monthly contribution remittance | -- | Within first 10 days of following month *(secondary -- almawarid.app)* |
| CNAS annual salary declaration (DAS) | DAS | 31 January *(secondary -- almawarid.app)* |

- **Taxable period and statute of limitations** — Taxable period: calendar year. Statute of limitations: 4 years.  _(Source: PwC -- Tax administration.)_

**2026 note:** EY reports Algeria extended the FY2025 annual income tax and transfer-pricing filing deadline. *(Source: https://taxnews.ey.com/news/2026-0907-algeria-extends-filing-deadline-for-2025-annual-income-tax-and-transfer-pricing-declarations)*

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 IFU vs Real Regime Election

Turnover near the DZD 8,000,000 ceiling, or mixed goods/services activities, require judgement on regime and rate split.
**Flag for reviewer:** confirm turnover total, activity classification, and whether the auto-entrepreneur sub-regime (≤ DZD 5,000,000, 0.5% [RESEARCH GAP]) applies.

### 6.2 Spouse / Dependent Allowances

Secondary sources cite a spouse reduction (~DZD 1,500/month) and per-dependent allowance (~DZD 12,000). Not confirmed by PwC.
**Conservative default:** apply NO allowance until confirmed against the CIDTA.

### 6.3 Home / Mixed-Use Premises (real regime)

Apportion electricity (SONELGAZ), water (SEAAL/ADE), and telecoms by genuine business-use percentage.
**Conservative default:** 0% until documented.

### 6.4 Vehicle Business Use (real regime)

Only the business-use % of fuel, insurance, and depreciation is deductible; requires a usage log.
**Conservative default:** 0% business use until a log is provided.

### 6.5 Entertainment / Client Meals

Deductibility is limited under the CIDTA. **[RESEARCH GAP -- confirm exact limit.]**
**Flag for reviewer** before allowing any deduction.

### 6.6 Isolation / Special-Conditions Exemption

Up to 70% of basic salary may be PIT-exempt for special living/isolation conditions.
**Flag for reviewer:** confirm eligibility and the exempt portion. *(Source: PwC -- Income determination.)*

### 6.7 Schedular Income Interaction

Rental, dividend, and interest income carry separate withholding; confirm whether final or creditable against the annual return.

## Section 7 -- Excel Working Paper Template

```
ALGERIA INCOME TAX -- IRG / IFU WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Regime: Employee (IRG payroll) / Self-employed real / IFU micro

PART A -- EMPLOYEE IRG (monthly)
  A1. Gross monthly salary (DZD)                  ___________
  A2. Less CNAS employee 9% (A1 × 0.09)           ___________
  A3. IRG taxable base (A1 - A2)                  ___________
  A4. If A1 <= 30,000 -> IRG = 0 (exempt)         ___________
  A5. Annualised base (A3 × 12)                   ___________
  A6. Annual IRG (apply progressive scale)        ___________
  A7. Monthly IRG (A6 / 12)                       ___________
  A8. Net pay (A1 - A2 - A7)                      ___________
  [Spouse/dependent allowance: RESEARCH GAP - 0 until confirmed]

PART B -- SELF-EMPLOYED IFU
  B1. Annual turnover (DZD)                        ___________
  B2. Eligible? (B1 <= 8,000,000)  Y / N           ___________
  B3. Activity: goods (5%) / services (12%)        ___________
  B4. IFU = B1 × rate                              ___________
  B5. Minimum IFU (DZD 20,000)                     ___________
  B6. IFU due = max(B4, B5)                        ___________

PART C -- SELF-EMPLOYED REAL REGIME
  C1. Gross business income                        ___________
  C2. Less deductible expenses (real regime only)  ___________
  C3. Net taxable income (C1 - C2)                 ___________
  C4. IRG (apply progressive scale)                ___________

PART D -- SOCIAL CONTRIBUTIONS
  D1. CNAS employee 9% (employee)                  ___________
  D2. CNAS employer 26% (employer)                 ___________
  D3. CASNOS 15% of declared base (self-employed)  ___________

PART E -- FILING
  E1. G50 monthly remittance (within 20 days)      ___________
  E2. G12 provisional (30 June)                    ___________
  E3. G12 bis final (20 January)                   ___________
  E4. Annual return (30 April / FY2025: 30 June)   ___________

REVIEWER FLAGS:
  [ ] Residency confirmed?
  [ ] Regime confirmed (IRG real / IFU / employee)?
  [ ] Turnover <= 8,000,000 for IFU verified?
  [ ] IFU rate split (5%/12%) confirmed vs 2025 Finance Law?
  [ ] IFU minimum (20,000 vs 30,000) confirmed?
  [ ] Spouse/dependent allowances confirmed vs CIDTA?
  [ ] CNAS per-branch split confirmed vs AAPI?
  [ ] CASNOS base confirmed vs official CASNOS site?
  [ ] Isolation/special-conditions exemption checked?
```

## Section 8 -- Bank Statement Reading Guide

### Algerian Bank Statement Formats

**Algerian Bank Statement Formats**

| Bank | Format | Key fields | Notes |
| --- | --- | --- | --- |
| BNA | PDF | Date, Libellé, Débit, Crédit, Solde | French; date DD/MM/YYYY |
| CPA | PDF | Date, Libellé, Montant, Solde | Counterparty in libellé |
| BEA | PDF | Date, Opération, Débit, Crédit | Common for businesses |
| BADR / BDL | PDF | Date, Libellé, Mouvement, Solde | Development/agricultural |
| AGB / Al Salam (private) | PDF/CSV | Date, Counterparty, Amount | Cleaner counterparty names |

### Key Algerian Banking / Tax Terms

**Key Algerian Banking / Tax Terms**

| Term (FR/AR translit.) | English | Classification hint |
| --- | --- | --- |
| VIREMENT / VRT | Transfer | Check direction for income/expense |
| PRÉLÈVEMENT / PRLV | Direct debit | Regular expense (utility, CASNOS) |
| SALAIRE / PAIE | Salary | Employment income (IRG base) |
| HONORAIRES | Professional fees | Business income |
| FRAIS / COMMISSION | Charges / fees | Deductible (real regime) |
| LOYER | Rent | Premises expense or rental income |
| COTISATION | Contribution | CNAS / CASNOS |
| RETRAIT / ESPÈCES | Cash withdrawal | Ask what cash was spent on |
| SOLDE | Balance | Running balance |

## Section 9 -- Onboarding Fallback

If the client provides a statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items and [RESEARCH GAP] figures as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ALGERIA INCOME TAX
1. Are you tax-resident in Algeria (worldwide income) or non-resident?
2. Are you an employee (CNAS) or self-employed (CASNOS)?
3. If self-employed, what was your annual turnover (DZD)?
4. If self-employed, do you trade in goods (5% IFU) or services (12% IFU), or are you on the real regime?
5. Marital status and number of dependents?
6. Monthly gross salary (if employed)?
7. Do you qualify for the isolation/special-conditions exemption?
8. Do you have rental, dividend, or interest income?
9. CNAS/CASNOS contributions paid during the year?
10. Any provisional IRG instalments paid?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| IRG progressive scale | CIDTA; PwC -- Taxes on personal income (14 Jul 2025) |
| Salary exemption (DZD 30,000) | PwC -- Income determination |
| Schedular rates (dividends/interest/CG) | PwC -- Income determination |
| Deductions (alimony, mortgage, tax) | PwC -- Deductions |
| IFU eligibility (DZD 8,000,000) | CIDTA Art. 282 ter; DGI IFU page |
| IFU minimum (DZD 20,000) | IMF Country Report 25/271 |
| CNAS 9% / 26% / 35% | PwC -- Other taxes |
| CASNOS 15% | noteasy-dz.com; AAPI (secondary) |
| SNMG 2025 / 2026 | observalgerie.com; acf-dz.com; Decree n°26-01 |
| Filing forms & deadlines | PwC -- Tax administration; DGI mfdgi.gov.dz |
| FY2025 deadline extension | EY Tax News 2026-0907 |

### Related Business Taxes (context only)

**Related Business Taxes (context only)**

| Tax | Rate | Source |
| --- | --- | --- |
| IBS (corporate) -- manufacturing | 19% | PwC -- Corporate, taxes on corporate income |
| IBS -- building/public works/tourism | 23% | PwC -- Corporate |
| IBS -- trade & services (other) | 26% | PwC -- Corporate |
| IBS minimum (nil returns) | DZD 10,000/year | PwC -- Corporate |
| TVA (VAT) standard | 19% (reduced 9%, zero 0%) | PwC -- Other taxes |
| TAP (professional activity tax) | ~1.5% historically | **[RESEARCH GAP -- being phased toward local levies; confirm in 2025 Finance Law]** |

### Penalties (secondary -- confirm against CIDTA)

**Penalties (secondary -- confirm against CIDTA)**

| Breach | Penalty | Source |
| --- | --- | --- |
| IRG instalment late payment | 10% surcharge per late instalment | cirtait.com (secondary) **[RESEARCH GAP]** |
| G29 employer payroll failure | 5% of annual payroll (Art. 194-8 CIDTA, mod. Art. 16 LF 2025) | cirtait.com **[RESEARCH GAP]** |
| IFU late filing (> 2 months) | 25% surcharge; 25% on administration-assessed tax if no declaration | fatoura.app **[RESEARCH GAP]** |
| Non-payment failure, fixed | DZD 2,500 (≤1mo); 5,000 (1–2mo); 10,000 (>2mo) | cirtait.com **[RESEARCH GAP]** |
| CNAS late payment | 10% + 3%/month | almawarid.app **[RESEARCH GAP]** |
| CASNOS late payment | 5% + 1%/month | noteasy-dz.com |

### Test Suite

**Test 1 -- Employee, mid salary.**
Input: Gross DZD 120,000/month, no special exemptions.
Expected: CNAS employee = 10,800; IRG base = 109,200; annualised 1,310,400; annual IRG = 55,200 + 129,600 + (30% × 350,400 = 105,120) = 289,920; monthly IRG = 24,160; net ≈ 85,040.

**Test 2 -- Exempt low salary.**
Input: Gross DZD 28,000/month.
Expected: IRG = 0 (≤ 30,000). CNAS employee = 2,520. Net = 25,480.

**Test 3 -- IFU goods.**
Input: Turnover DZD 6,000,000, sale of goods.
Expected: IFU = 5% × 6,000,000 = 300,000 (> 20,000 minimum). Goods rate [RESEARCH GAP].

**Test 4 -- IFU services.**
Input: Turnover DZD 1,500,000, services.
Expected: IFU = 12% × 1,500,000 = 180,000 (> 20,000 minimum). Services rate [RESEARCH GAP].

**Test 5 -- IFU below minimum.**
Input: Turnover DZD 300,000, services.
Expected: 12% × 300,000 = 36,000 > 20,000 ⇒ IFU = 36,000. (If 12% × turnover had been below 20,000, the DZD 20,000 minimum would apply.)

**Test 6 -- CASNOS at SNMG floor.**
Input: Self-employed, declared base at 2025 SNMG (annual 240,000).
Expected: CASNOS = 15% × 240,000 = 36,000/year, due by 30 June. [RESEARCH GAP on base.]

**Test 7 -- Top-bracket annual IRG.**
Input: Annual taxable income DZD 4,000,000 (real regime).
Expected: 1,106,400 (through 3,840,000) + 35% × (4,000,000 − 3,840,000 = 160,000 = 56,000) = **DZD 1,162,400**.

## PROHIBITIONS

- NEVER compute IRG without confirming residency.
- NEVER apply the IRG scale to a salary ≤ DZD 30,000/month -- it is exempt.
- NEVER deduct business expenses under the IFU micro regime -- IFU is a flat % of turnover.
- NEVER apply spouse/dependent allowances until confirmed against the CIDTA (currently [RESEARCH GAP]).
- NEVER state the IFU 5%/12% split or the DZD 20,000 minimum as final without reviewer confirmation against the 2025 Finance Law.
- NEVER allow fines, penalties, or income tax itself as a deduction.
- NEVER include VAT (TVA) collected in business income.
- NEVER treat CNAS/CASNOS contributions or provisional instalments as ordinary expenses.
- NEVER present any [RESEARCH GAP] figure as authoritative.
- NEVER present tax calculations as definitive -- always label as estimated, pending professional review.

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
