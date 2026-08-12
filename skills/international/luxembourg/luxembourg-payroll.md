---
name: luxembourg-payroll
description: Use this skill whenever asked about Luxembourg payroll processing for employed persons. Trigger on phrases like "Luxembourg payroll", "retenue d'impot Luxembourg", "wage withholding Luxembourg", "fiche de retenue", "tax card Luxembourg", "tax class 1 1a 2", "CCSS contributions", "centre commun de la securite sociale", "pension contribution Luxembourg", "assurance dependance", "dependency insurance", "Mutualite des Employeurs", "MDE", "accident insurance Luxembourg", "sante au travail", "SSM Luxembourg", "salaire social minimum", "social minimum wage Luxembourg", "CIS CISSM CIM tax credit", "solidarity surcharge Luxembourg", "fonds pour l'emploi", "MyGuichet payroll", "extrait de compte salaire", "net salary Luxembourg", "gross to net Luxembourg", "PAYE Luxembourg", or any question about computing employee pay, wage withholding tax, or social security contributions for Luxembourg-based employees. This skill covers monthly wage withholding tax (PAYE via the tax card), CCSS social security (employee and employer), the dependency-insurance abatement, employer-only funds (accident, occupational health, Mutualite des Employeurs), the social minimum wage, tax credits (CIS, CISSM, CIM) and filing obligations. ALWAYS read this skill before processing any Luxembourg payroll.
version: 0.1
jurisdiction: LU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg Payroll

## Luxembourg Payroll Skill v0.1

**Tier 2 (research-verified).** The 2025 income tax scale (post "Entlaaschtungs-Pak" +2.5 index-bracket adjustment), the solidarity surcharge and the CIS/CISSM/CIM tax credits are confirmed against PwC Worldwide Tax Summaries. The CCSS contribution rate table (sickness 2.80%+2.80%, pension 8%+8%, dependency 1.40%, accident base 0.700%, Mutualite des Employeurs 0.07-2.64%, sante au travail 0.14%) is taken directly from the official CCSS *Avis aux employeurs - Taux de cotisation au 01.01.2025* (notice of 17.01.2025) and is firm. The min/max contribution base and the May 2025 indexation are corroborated from Orbitax and WAT Fiduciary. The live CCSS HTML "parametres sociaux" page and several Big-4 newsletter pages returned HTTP 403 to automated fetch, so the official CCSS PDF and Orbitax/WAT were used to corroborate the May 2025 figures. Figures carry **[RESEARCH GAP — reviewer to confirm]** markers where the primary authority figure could not be pinned to a single fixed published value (notably class 1a withholding mechanics and the exact statutory penalty for late annual-statement filing).

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Luxembourg (Grand Duchy of Luxembourg / Groussherzogtum Letzebuerg) |
| Currency | EUR only |
| Standard pay frequency | Monthly (overwhelmingly the norm) |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | PAYE-style monthly wage withholding (retenue d'impot sur les salaires); employer withholds income tax + solidarity surcharge each pay period from the ACD official tables, based on the employee's tax class and electronic tax card |
| Tax authority | Administration des contributions directes (ACD / Luxembourg Inland Revenue); wage withholding declared and paid via MyGuichet.lu (guichet.public.lu) |
| Social security authority | Centre commun de la securite sociale (CCSS, ccss.public.lu) -- single collector of all social contributions |
| Key legislation | Loi modifiee du 4 decembre 1967 concernant l'impot sur le revenu (LIR) and the Reglement grand-ducal fixing the withholding scale (bareme); Code de la securite sociale (CSS); Reglement grand-ducal du 26 mars 2014 (electronic salary-statement filing). 2025 income tax scale adjusted under the law of 20 December 2024 ("Entlaaschtungs-Pak", +2.5 index brackets) |
| Filing portal | MyGuichet.lu (wage withholding + annual salary statement); CCSS / SECUline (social declarations) |
| Income tax-free band (tax class 1, 2025) | EUR 0 -- 13,230 at 0% (PwC LU 2025) |
| Social-contribution ceiling (max base = 5x SSM) | EUR 13,188.96/month (1 Jan 2025, index 944.43) -> EUR 13,518.68/month (from 1 May 2025, index 968.04); annual max approx EUR 162,224 (CCSS Avis 17.01.2025; Orbitax) |
| Social-contribution floor (min base = SSM unskilled) | EUR 2,637.79/month (Jan 2025) -> EUR 2,703.74/month (May 2025) (CCSS Avis 17.01.2025) |
| Validated by | Pending -- requires sign-off by a Luxembourg reviewer (expert-comptable / fiduciaire) |
| Skill version | 0.1 |

**Headline contribution rates (2025)**  _(CCSS Avis aux employeurs 17.01.2025)_

| Branch | Employee | Employer |
| --- | --- | --- |
| Pension (assurance pension) | 8.00% | 8.00% (+ 8.00% State; total 24.00%) |
| Sickness -- in kind (prestations en nature) | 2.80% | 2.80% |
| Sickness -- cash (majoration prestations en especes) | 0.25% | 0.25% |
| Dependency / long-term care (assurance dependance) | 1.40% | -- (employee only) |
| Accident insurance (assurance accident) | -- | 0.700% base (bonus-malus 0.595%--1.050%) |
| Occupational health (sante au travail, STM) | -- | 0.14% (private sector using the multi-sector service) |
| Mutualite des Employeurs (MDE) | -- | 0.07% / 0.99% / 1.48% / 2.64% by absenteeism risk class |
| Family benefits (prestations familiales) | -- | 1.70% (**PUBLIC-sector employers ONLY**; 0% private sector) |
| **Typical employee deduction (ex-tax)** | **~12.45%** (8.00 + 2.80 + 0.25 + 1.40) | -- |
| **Typical private-sector employer on-cost (ex-tax, MDE Class 2)** | -- | **~12.88%** (8.00 + 2.80 + 0.25 + 0.700 + 0.14 + 0.99) |

- **Dependency contribution base note** — The dependency contribution (1.40%, employee only) is levied on gross income after an abatement of 1/4 of the SSM and has no floor or ceiling — its base differs from every other branch. See Section 3.

## Section 2 -- Income Tax Withholding (Monthly PAYE via the Tax Card)

The employer withholds income tax each pay period under the wage-withholding provisions of the LIR (retenue d'impot sur les salaires), reading the withholding from the **official monthly/daily withholding tax tables (bareme) published by the ACD** based on the employee's **tax class** and the data on the **electronic withholding tax card (fiche de retenue d'impot)**. Since 01.01.2022 employees no longer hand a paper card to the employer; the ACD transmits the card data electronically. The withholding includes the solidarity surcharge. (Source: guichet.public.lu retenue-impot.)

### Tax Classes (2025)

**Tax Classes table**

| Tax class | Who (broadly) |
| --- | --- |
| 1 | Single, no children |
| 1a | Single parents; persons aged 65+; certain widow(er)s (higher tax-free allowance, ~EUR 26,460 for 2025) |
| 2 | Married / civil-partnership couples taxed jointly, using income-splitting |

The withholding tables differ by class. This skill enumerates the **class 1** marginal scale from the research data; class 1a applies a higher tax-free allowance and class 2 broadly applies the class-1 scale to half of joint income ("splitting"). **[RESEARCH GAP — reviewer to confirm the exact class 1a tax-free allowance (~EUR 26,460 is reported by secondary summaries) and the class 1a / class 2 withholding-table mechanics against the ACD bareme; only the class 1 marginal scale is enumerated below.]** (Source: PwC LU 2025.)

### 2025 Income Tax Scale -- Tax Class 1 (marginal rates)

**2025 Income Tax Scale -- Tax Class 1**  _(Source: PwC Worldwide Tax Summaries (Luxembourg, Individual, Taxes on personal income). Post "Entlaaschtungs-Pak" +2.5 index-bracket adjustment of 1 January 2025.)_

| Taxable Income (EUR) | Marginal Rate |
| --- | --- |
| 0 -- 13,230 | 0% |
| 13,230 -- 15,435 | 8% |
| 15,435 -- 17,640 | 9% |
| 17,640 -- 19,845 | 10% |
| 19,845 -- 22,050 | 11% |
| 22,050 -- 24,255 | 12% |
| 24,255 -- 26,550 | 14% |
| 26,550 -- 28,845 | 16% |
| 28,845 -- 31,140 | 18% |
| 31,140 -- 33,435 | 20% |
| 33,435 -- 35,730 | 22% |
| 35,730 -- 38,025 | 24% |
| 38,025 -- 40,320 | 26% |
| 40,320 -- 42,615 | 28% |
| 42,615 -- 44,910 | 30% |
| 44,910 -- 47,205 | 32% |
| 47,205 -- 49,500 | 34% |
| 49,500 -- 51,795 | 36% |
| 51,795 -- 54,090 | 38% |
| 54,090 -- 117,450 | 39% |
| 117,450 -- 176,160 | 40% |
| 176,160 -- 234,870 | 41% |
| 234,870+ | 42% (top marginal) |

### Solidarity Surcharge (contribution au fonds pour l'emploi)

- **Solidarity surcharge standard rate** — 7% % of income tax due (Standard)  _(Source: PwC Worldwide Tax Summaries)_
- **Solidarity surcharge step-up threshold and rate** — 9% where taxable income exceeds EUR 150,000 (tax classes 1 and 1a) or EUR 300,000 (tax class 2)  _(Source: PwC Worldwide Tax Summaries)_
- **Top effective marginal rate** — The surcharge funds the Fonds pour l'emploi. The top effective marginal rate is therefore approximately 45.78% (42% x 1.09).  _(Source: PwC Worldwide Tax Summaries)_

### No Valid Tax Card

- **No valid tax card rule** — If no valid withholding tax card exists, the employer must apply the highest rate: tax class 1, at a rate that cannot be lower than 33%.  _(Source: guichet.public.lu retenue-impot.)_

### Tax Credits Applied Through Withholding

**Tax Credits table**  _(Source: PwC Worldwide Tax Summaries; guichet.public.lu (CISSM).)_

| Credit | Amount | Notes |
| --- | --- | --- |
| Employee tax credit (CIS -- credit d'impot salarie) | EUR 0 -- 600/year, income-dependent | Granted via the tax card; offset against withholding |
| Social minimum wage tax credit (CISSM -- credit d'impot salaire social minimum) | EUR 81/month for gross EUR 1,800 -- 3,000; degressive from EUR 3,000 to EUR 3,600 (formula 81/600 x (3,600 - gross)); EUR 0 above EUR 3,600 | Set so an unskilled-minimum-wage earner has nil tax in all classes for 2025 |
| Single-parent tax credit (CIM -- credit d'impot monoparental) | EUR 750 -- 3,504/year, income-dependent | Tax class 1a |

### PAYE Computation Method

- **PAYE computation steps** — 1. Read the employee's tax class and any noted deductions/credits from the electronic tax card transmitted by the ACD. 2. Determine taxable income for the period (gross emoluments less the deductible employee social contributions and any card-noted deductions). 3. Look up the withholding from the ACD official monthly/daily withholding table (bareme) for that class; this implicitly applies the class scale (class 1 scale above) and adds the solidarity surcharge (7%, or 9% above the EUR 150,000 / 300,000 thresholds). 4. Offset the CIS / CISSM / CIM credits shown on the card. 5. If no valid card exists, withhold at class 1, minimum 33%.
- **Zero band as tax-free allowance** — The 0% band (to EUR 13,230 for class 1) is the tax-free allowance — there is no separate personal allowance on top of it.

## Section 3 -- Social Security -- Employee Deductions (CCSS)

The CCSS is the single collector of all Luxembourg social contributions. The employee bears four branches; the CCSS invoices the employer the combined employee + employer amount, and the employer deducts the employee share from wages. (Source: CCSS Avis aux employeurs 17.01.2025.)

### Employee Contribution Rates (2025)

**Employee Contribution Rates table**  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

| Branch | Rate | Base | Ceiling |
| --- | --- | --- | --- |
| Pension (assurance pension) | 8.00% | Gross remuneration | Max base 5 x SSM (see below) |
| Sickness -- in kind (prestations en nature) | 2.80% | Gross remuneration | Same max base as pension |
| Sickness -- cash (majoration prestations en especes) | 0.25% | Gross remuneration (only insured persons entitled to cash sick pay) | Same max base as pension |
| Dependency / long-term care (assurance dependance) | 1.40% | Gross income less an abatement of 1/4 of the SSM | NO floor or ceiling |

- **Combined employee deduction calc** — Combined employee sickness rate = 2.80% + 0.25% = 3.05%. Total employee deduction (excluding tax) on income within the ceiling = 8.00% + 3.05% + 1.40% = ~12.45% (the 1.40% dependency portion is on a different, uncapped, post-abatement base).  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

### The Dependency-Insurance Abatement (material)

**Dependency abatement table**  _(Source: CCSS Avis aux employeurs 17.01.2025; PwC LU Other taxes.)_

| Period | Monthly abatement (1/4 of SSM) |
| --- | --- |
| 1 Jan 2025 (index 944.43) | EUR 659.45 |
| From 1 May 2025 (index 968.04) | EUR 675.94 |

- **No floor/ceiling on dependency** — The dependency contribution has no minimum and no maximum ceiling — it applies to the full (post-abatement) income even above the 5 x SSM cap that limits the other branches.  _(Source: CCSS Avis aux employeurs 17.01.2025; PwC LU Other taxes.)_

### Social-Contribution Ceiling (Max Base) and Floor (Min Base)

**Ceiling and Floor table**  _(Sources: CCSS Avis 17.01.2025; Orbitax (May 2025); WAT Fiduciary.)_

| Parameter | 1 Jan 2025 (index 944.43) | From 1 May 2025 (index 968.04) |
| --- | --- | --- |
| Maximum monthly base (5 x SSM) | EUR 13,188.96 | EUR 13,518.68 |
| Minimum monthly base (= SSM unskilled) | EUR 2,637.79 | EUR 2,703.74 |
| Annual maximum base | approx EUR 162,224 (12 x 13,518.68) | approx EUR 162,224 (12 x 13,518.68) |

- **Indexation effective date rule** — The 2.5% automatic wage indexation took effect 1 May 2025 (index moved 944.43 -> 968.04). Use the Jan 2025 set for Jan--Apr 2025 pay periods and the May 2025 set from May 2025 onward.  _(Sources: CCSS Avis 17.01.2025; Orbitax (May 2025); WAT Fiduciary.)_

## Section 4 -- Social Security -- Employer Contributions (CCSS + Employer-Only Funds)

The employer matches the employee on pension and sickness, and additionally pays accident insurance, occupational health and the Mutualite des Employeurs — all employer-only. (Source: CCSS Avis aux employeurs 17.01.2025.)

### Employer Contribution Rates (2025)

**Employer Contribution Rates table**  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

| Branch | Rate | Base | Ceiling | Notes |
| --- | --- | --- | --- | --- |
| Pension (assurance pension) | 8.00% | Gross remuneration | 5 x SSM | Mirrors employee (+ 8.00% State; total 24.00%) |
| Sickness -- in kind | 2.80% | Gross remuneration | 5 x SSM | Mirrors employee |
| Sickness -- cash | 0.25% | Gross remuneration | 5 x SSM | Mirrors employee (cash-benefit majoration) |
| Accident insurance (assurance accident) | 0.700% base | Gross remuneration | 5 x SSM | Employer-only; base 0.700% adjusted by a bonus-malus factor (see below) |
| Occupational health (sante au travail, STM) | 0.14% | Gross remuneration | 5 x SSM | Employer-only; private-sector employers using the multi-sector occupational health service (STM) |
| Mutualite des Employeurs (MDE) | 0.07% / 0.99% / 1.48% / 2.64% | Gross remuneration | 5 x SSM | Employer-only; by financial-absenteeism risk class (see below) |
| Family benefits (prestations familiales) | 1.70% | Gross remuneration | 5 x SSM | PUBLIC-sector employers ONLY; private-sector employers pay 0% (state-funded) |

- **Employer exclusions** — The employer does NOT pay the dependency (long-term care) contribution — that 1.40% is employee only. Private-sector employers do NOT pay the 1.70% family-benefits contribution.

### Accident Insurance Bonus-Malus (2025)

**Bonus-malus table**  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

| Bonus-malus factor | Effective rate |
| --- | --- |
| 0.85 | 0.595% |
| 1.00 (default) | 0.700% |
| 1.10 | 0.770% |
| 1.30 | 0.910% |
| 1.50 | 1.050% |

- **Default bonus-malus factor** — Use 0.700% with factor 1.00 as the default unless the employer's notified factor is known.  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

### Mutualite des Employeurs (MDE) -- Absenteeism Classes (2025)

**MDE Absenteeism Classes table**  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

| Class | Financial absenteeism | Rate (2025) |
| --- | --- | --- |
| Class 1 | < 0.65% | 0.07% |
| Class 2 | < 1.60% | 0.99% |
| Class 3 | < 2.50% | 1.48% |
| Class 4 | >= 2.50% | 2.64% |

- **Class assignment** — The actual class is assigned by the CCSS based on the employer's financial-absenteeism rate.  _(Source: CCSS Avis aux employeurs 17.01.2025.)_

### Typical Private-Sector Employer On-Cost (MDE Class 2, accident factor 1.00)

- **On-cost calculation** — Pension 8.00% + Sickness 3.05% + Accident 0.700% + Occupational health 0.14% + MDE 0.99% = ~12.88% of gross within the ceiling (family benefits 1.70% is not included — it is public-sector only).

Note: figures vary with the MDE class and the accident bonus-malus factor — both are employer-specific. The State also pays an additional 8.00% pension contribution that is not an employer payroll cost.

## Section 5 -- Social Minimum Wage (SSM) and Reference Items

### Social Minimum Wage (salaire social minimum, SSM) -- full-time monthly gross

**SSM table**  _(Sources: CCSS Avis 17.01.2025; WAT Fiduciary (May 2025).)_

| Category | 1 Jan 2025 (index 944.43) | From 1 May 2025 (index 968.04) |
| --- | --- | --- |
| Unskilled, aged 18+ (non qualifie) | EUR 2,637.79 | EUR 2,703.74 |
| Skilled, aged 18+ (qualifie, approx +20%) | EUR 3,165.31 | EUR 3,244.48 |
| Aged 17-18 (80% of SSM) | EUR 2,110.23 | [RESEARCH GAP — reviewer to confirm May 2025 figure] |
| Aged 15-17 (75% of SSM) | EUR 1,978.34 | [RESEARCH GAP — reviewer to confirm May 2025 figure] |

- **SSM index base and min contribution base** — SSM = EUR 279.30 at index 100; cost-of-living index 944.43 at 01.01.2025, rising to 968.04 from 01.05.2025 (+2.5%). The minimum social-contribution base equals the SSM unskilled.  _(Sources: CCSS Avis 17.01.2025; WAT Fiduciary (May 2025).)_

### Other Reference Items

**Other Reference Items table**

| Item | Amount | Notes / Source |
| --- | --- | --- |
| Employee tax credit (CIS) | EUR 0 -- 600/year | Income-dependent; via tax card (PwC) |
| Social minimum wage tax credit (CISSM) | EUR 81/month (gross EUR 1,800 -- 3,000); degressive to EUR 0 at EUR 3,600 | Formula 81/600 x (3,600 - gross) between EUR 3,000 and 3,600 (PwC; Guichet.lu) |
| Single-parent tax credit (CIM) | EUR 750 -- 3,504/year | Tax class 1a (PwC) |
| Class 1a tax-free allowance (2025) | ~EUR 26,460 | [RESEARCH GAP — reported by secondary summaries; verify against ACD bareme] |

Statutory leave, the 13th month and overtime premia are not enumerated in the research data for this skill. [RESEARCH GAP — reviewer to confirm Luxembourg statutory annual leave, public holidays, sick-pay continuation rules and any 13th-month / bonus treatment before relying on them.]

## Section 6 -- Conservative Defaults

When an input is ambiguous, apply the conservative default and flag for the reviewer rather than guessing.

- **Accident insurance rate** — 0.700% (base, bonus-malus factor 1.00). Use the unadjusted base rate unless the employer's specific factor from the Accident Insurance Association is known.
- **Mutualite des Employeurs class** — New/unrated employers are placed by CCSS into a class based on financial absenteeism; if unknown, model a mid class rather than assuming the lowest (0.07%). Replace with the employer's actual notified class.
- **Family benefits (prestations familiales) 1.70%** — Apply only for PUBLIC-sector employers; for private-sector payroll set to 0% (state-funded).
- **Occupational health (sante au travail) 0.14%** — Apply only if the private-sector employer uses the multi-sector occupational health service (STM); employers with their own/in-house or sector service may differ.
- **Which 2025 index / parameter set** — Use the 1 Jan 2025 set (index 944.43; SSM 2,637.79; ceiling 13,188.96; abatement 659.45) for Jan--Apr 2025; the 1 May 2025 set (index 968.04; SSM 2,703.74; ceiling 13,518.68; abatement 675.94) from 1 May 2025.
- **Tax class** — If the tax card is not available, do not guess — flag for the card. If no valid card exists, the employer must withhold at the least favourable basis (class 1, min 33%). Trigger R-LU-P-1.
- **Dependency base** — Apply 1.40% on gross less the 1/4-SSM abatement with no floor or ceiling — do not apply the 5 x SSM cap to dependency.
- **Solidarity surcharge** — 7% of income tax due; step up to 9% only above EUR 150,000 (class 1/1a) or EUR 300,000 (class 2) taxable income.
- **Reliefs / deductions** — Compute withholding on gross less only the deductible employee social contributions and card-noted items. Do not assume discretionary deductions.

### Required Inputs

**Minimum viable** — for each employee: gross monthly remuneration, the tax class from the fiche de retenue d'impot (electronic tax card), pay frequency, and the period being run. The employer's matricule employeur (CCSS registration number).

**Recommended** — date of hire (CCSS entry declaration), whether the employer is public or private sector (for the 1.70% family-benefits contribution), the MDE absenteeism class, the accident bonus-malus factor, any card-noted CIS/CISSM/CIM credits, prior-month cumulative figures, and any non-cash benefits.

**Ideal** — full employee register, the CCSS monthly contribution statements/invoices, prior MyGuichet.lu withholding declarations, and prior-year salary-statement data for reconciliation.

### Luxembourg-Specific Refusal Catalogue

- **R-LU-P-1 — No tax card** — Trigger: the employee's tax class / fiche de retenue d'impot is not available. Message: "Wage withholding requires the employee's electronic tax card (fiche de retenue d'impot) data; without it the tax class and credits cannot be applied. Obtain the card data before running tax withholding — otherwise the employer must withhold at class 1, minimum 33%."
- **R-LU-P-2 — Self-employed / non-salaried** — Trigger: the worker is self-employed (independant) or a company director not on a salary. Message: "Self-employed and non-salaried persons are not run through employer wage withholding; their social security and tax are handled separately. Use the Luxembourg income-tax / self-employed skill."
- **R-LU-P-3 — Cross-border / frontalier / posted worker** — Trigger: a cross-border worker (frontalier), an A1/E101 certificate, or a totalisation question. Message: "Cross-border social security coordination (EU Reg. 883/2004, A1 certificates) and frontalier tax treatment require specialist advice."
- **R-LU-P-4 — Impatriate / expat regime** — Trigger: a high-earner claiming the impatriate tax regime or the inpatriate premium. Message: "The Luxembourg impatriate regime and inpatriate premium have specific conditions and affect withholding; route through a Luxembourg reviewer."
- **R-LU-P-5 — Benefits in kind / equity** — Trigger: company car, accommodation, stock options or other benefits in kind. Message: "Benefit-in-kind valuation (company car, housing, equity) affects taxable income and contributions; route through a Luxembourg reviewer."
- **R-LU-P-6 — Termination / severance** — Trigger: severance, ex-gratia, or redundancy lump sum. Message: "Termination payments have specific tax and social treatment; do not run through standard wage withholding."

## Section 8 -- Transaction / Payment Pattern Library

Match by case-insensitive substring. French / Luxembourgish / German variants treated as their English equivalent. Most specific match wins.

### 8.1 Salary credits (to the employee's account)

**Salary credits table**

| Pattern | Classification |
| --- | --- |
| SALAIRE, TRAITEMENT, PAIE, LOHN, GEHALT, SALARY | Net salary payment |
| EMPLOYEUR [name] VIREMENT, WAGES, SALAIRE NET | Net salary payment |
| 13E MOIS, 13EME MOIS, GRATIFICATION | 13th-month / bonus (if applicable; taxable, contributory) |
| HEURES SUPPLEMENTAIRES, UEBERSTUNDEN, OVERTIME | Overtime pay |
| PRIME, BONUS | Bonus (taxable, contributory) |

### 8.2 Employer statutory debits (to the authorities)

**Employer statutory debits table**

| Pattern | Classification |
| --- | --- |
| CCSS, CENTRE COMMUN, SECURITE SOCIALE, SECU | CCSS combined social contributions (pension + sickness + dependency + accident + occupational health + MDE) |
| RETENUE IMPOT, RTS, ACD, CONTRIBUTIONS DIRECTES, MYGUICHET | Wage withholding tax (income tax + solidarity surcharge) to the ACD via MyGuichet.lu |
| FONDS POUR L'EMPLOI, SOLIDARITE | Solidarity surcharge component (part of the withholding remittance) |
| MUTUALITE DES EMPLOYEURS, MDE | Mutualite des Employeurs (within the CCSS invoice) |
| ASSURANCE ACCIDENT, AAA | Accident insurance (within the CCSS invoice) |
| ASSURANCE DEPENDANCE | Dependency / long-term care (within the CCSS invoice) |
| SANTE AU TRAVAIL, STM | Occupational health (within the CCSS invoice) |

### 8.3 Net wage disbursement (employer's bank)

**Net wage disbursement table**

| Pattern | Classification |
| --- | --- |
| VIREMENT SALAIRES, PAIE, LOHNLAUF, SALARY RUN, PAYROLL BATCH | Salary disbursement to employees |
| MASSE SALARIALE | Payroll run |

### 8.4 Exclusions / not payroll

**Exclusions table**

| Pattern | Classification |
| --- | --- |
| VIREMENT INTERNE, OWN TRANSFER, EIGENUEBERTRAGUNG | Internal movement -- exclude |
| DIVIDENDE, DIVIDEND | Out of scope -- exclude |
| PRET, DARLEHEN, LOAN | Loan principal -- exclude |
| INTERETS, ZINSEN, INTEREST | Interest -- exclude |

## Section 9 -- Worked Examples

All figures use the 1 May 2025 parameter set (index 968.04) unless stated: SSM unskilled EUR 2,703.74; max base EUR 13,518.68/month; dependency abatement EUR 675.94/month. Tax withholding shown is illustrative (tax class 1, before/after card-noted credits) — exact monthly withholding comes from the ACD bareme using the tax card, so a Luxembourg reviewer must confirm. Employer on-cost assumes a private-sector employer with MDE Class 2 (0.99%) and accident factor 1.00 (0.700%).

### Example 1 — Unskilled minimum-wage employee (monthly EUR 2,703.74, class 1)

Bank statement line (employer): `30.05.2025 ; VIREMENT SALAIRES -- A. WEBER ; DEBIT ; Salaire mai ; -2,376.59 ; EUR`

Reasoning: Gross EUR 2,703.74. Employee social contributions: pension 8.00% = EUR 216.30; sickness 3.05% = EUR 82.46; dependency 1.40% on (2,703.74 − 675.94 abatement) = 1.40% × 2,027.80 = EUR 28.39. Employee social total = 216.30 + 82.46 + 28.39 = EUR 327.15. For tax, the CISSM credit is designed so an unskilled-minimum-wage earner has nil tax in all classes for 2025 — illustrative withholding ≈ EUR 0 after CISSM/CIS. Net ≈ 2,703.74 − 327.15 = EUR 2,376.59 (illustrative).

**Example 1 table**  _(Example 1 table)_

| Item | Base | Rate | Amount (EUR) |
| --- | --- | --- | --- |
| Gross | -- | -- | 2,703.74 |
| Employee pension | 2,703.74 | 8.00% | 216.30 |
| Employee sickness | 2,703.74 | 3.05% | 82.46 |
| Employee dependency | 2,027.80 (post-abatement) | 1.40% | 28.39 |
| Wage withholding (after CISSM/CIS) | -- | illustrative | ~0.00 |
| **Net pay (illustrative)** | -- | -- | **~2,376.59** |

### Example 2 — Mid earner (monthly EUR 4,500, class 1)

Bank statement line (employee credit): `30.06.2025 ; EMPLOYEUR SARL VIREMENT ; CREDIT ; Salaire juin ; +3,5xx.xx ; EUR`

Reasoning: Gross EUR 4,500, within the ceiling. Employee pension 8.00% = EUR 360.00; sickness 3.05% = EUR 137.25; dependency 1.40% × (4,500 − 675.94) = 1.40% × 3,824.06 = EUR 53.54. Employee social total = 360.00 + 137.25 + 53.54 = EUR 550.79. Gross is above EUR 3,600 so no CISSM; a small CIS may apply via the card. Annual taxable ≈ 12 × (4,500 − 550.79) ≈ EUR 47,390; class-1 income tax + 7% solidarity, divided across the year. Withholding here is illustrative — the exact monthly figure comes from the ACD bareme using the tax card. [RESEARCH GAP — exact monthly withholding requires the ACD class-1 withholding table; only the marginal scale is enumerated.]

**Example 2 table**  _(Example 2 table)_

| Item (monthly) | Base | Rate | Amount (EUR) |
| --- | --- | --- | --- |
| Gross | -- | -- | 4,500.00 |
| Employee pension | 4,500.00 | 8.00% | 360.00 |
| Employee sickness | 4,500.00 | 3.05% | 137.25 |
| Employee dependency | 3,824.06 (post-abatement) | 1.40% | 53.54 |
| Wage withholding (income tax + 7% solidarity) | -- | per bareme | illustrative |
| **Net pay** | -- | -- | 3,949.21 − withholding |

### Example 3 — High earner above the ceiling (monthly EUR 16,000, class 1)

Bank statement line (employer debit, CCSS): `05.07.2025 ; CENTRE COMMUN SECURITE SOCIALE ; DEBIT ; Cotisations juin ; -4,1xx.xx ; EUR`

Reasoning: Monthly EUR 16,000 exceeds the max base EUR 13,518.68. Capped branches (pension, sickness, accident, occupational health, MDE) apply only to EUR 13,518.68. Dependency has no ceiling and is on the full post-abatement income: 1.40% × (16,000 − 675.94) = 1.40% × 15,324.06 = EUR 214.54.

Employer on-cost = 1,081.49 + 412.32 + 94.63 + 18.93 + 133.83 = EUR 1,741.20. The employee dependency (EUR 214.54) is on the full EUR 15,324.06 post-abatement, not the capped EUR 13,518.68. The employer pays no dependency and (private sector) no family benefits.

**Example 3 table**  _(Example 3 table)_

| Item (monthly) | Base | Rate | Amount (EUR) |
| --- | --- | --- | --- |
| Employee pension | 13,518.68 (capped) | 8.00% | 1,081.49 |
| Employee sickness | 13,518.68 (capped) | 3.05% | 412.32 |
| Employee dependency | 15,324.06 (**uncapped**, post-abatement) | 1.40% | 214.54 |
| Employer pension | 13,518.68 (capped) | 8.00% | 1,081.49 |
| Employer sickness | 13,518.68 (capped) | 3.05% | 412.32 |
| Employer accident | 13,518.68 (capped) | 0.700% | 94.63 |
| Employer occupational health | 13,518.68 (capped) | 0.14% | 18.93 |
| Employer MDE (Class 2) | 13,518.68 (capped) | 0.99% | 133.83 |
| **Employer on-cost (CCSS, ex-State, private sector)** | -- | -- | **1,741.20** |

### Example 4 — Index boundary (Jan--Apr 2025 vs May 2025)

Reasoning: For a Jan--Apr 2025 pay period, use the index 944.43 set: SSM unskilled EUR 2,637.79, max base EUR 13,188.96, dependency abatement EUR 659.45. From the May 2025 pay period, switch to the index 968.04 set (EUR 2,703.74 / EUR 13,518.68 / EUR 675.94). For an unskilled-minimum-wage employee, the Jan gross is EUR 2,637.79 and the May gross is EUR 2,703.74 — a 2.5% indexation uplift (2,637.79 × 1.025 = 2,703.74). Always confirm which pay period you are running before selecting the parameter set.

### Example 5 — CCSS combined remittance

Bank statement line (employer debit): `10.07.2025 ; CCSS CENTRE COMMUN ; DEBIT ; Facture cotisations juin ; -3,4xx.xx ; EUR`

Reasoning: The CCSS issues a monthly account statement (extrait de compte) invoicing the employer the combined employee + employer social contributions. The employer deducts the employee share from wages and remits the full invoiced amount; the balance is payable within 10 days of the statement's issue. Classify as a CCSS social-contribution remittance (a mix of expense — the employer share — and liability — the withheld employee share), not an employee salary payment. Late payment carries default interest of 0.6% per full calendar month. Source: CCSS recouvrement / facturation.

### Example 6 — Wage withholding remittance via MyGuichet.lu

Bank statement line (employer debit): `09.04.2025 ; ACD RETENUE IMPOT ; DEBIT ; RTS Q1 / mars ; -8xx.xx ; EUR`

Reasoning: This is the wage withholding tax (income tax + solidarity surcharge) withheld from employees, declared and paid via MyGuichet.lu on the Declaration de la retenue d'impot sur remunerations et des credits d'impot bonifies. Remittance frequency depends on monthly withholding: monthly if >= EUR 750; quarterly if EUR 75 -- 749; annually if < EUR 75. The declaration and payment are due by the 10th of the month following the period (e.g. by 10 April for March / Q1). Classify as a wage-withholding remittance, not an expense to the employee. Source: guichet.public.lu retenue-impot.

## Section 10 -- Tier 1 Rules (deterministic)

- **2025 income tax scale (tax class 1)** — 0% up to EUR 13,230, then progressive marginal rates 8% to 42%, with the top 42% rate from EUR 234,870 (post "Entlaaschtungs-Pak" +2.5 index-bracket adjustment of 1 Jan 2025)  _(PwC Worldwide Tax Summaries.)_
- **Solidarity surcharge** — 7% of the income tax due, rising to 9% where taxable income exceeds EUR 150,000 (classes 1/1a) or EUR 300,000 (class 2). Top effective marginal rate ≈ 45.78%  _(PwC.)_
- **Income tax withheld at source** — Income tax is withheld at source (monthly PAYE) by the employer from the ACD official tables based on the employee's tax class (1, 1a, 2) and electronic tax card; the employer offsets the CIS, CISSM and CIM credits. If no valid card exists, withhold at class 1, minimum 33%.  _(LIR; guichet.public.lu retenue-impot.)_
- **Pension contribution 2025** — 8.00% employee + 8.00% employer (+ 8.00% State = 24.00% total)  _(CCSS Avis aux employeurs 17.01.2025.)_
- **Sickness/health 2025** — in-kind 2.80% employee + 2.80% employer; cash-benefit majoration 0.25% employee + 0.25% employer (so 3.05% each side combined)  _(CCSS Avis 17.01.2025.)_
- **Dependency (long-term care)** — 1.40% employee only (no employer share), on gross after an abatement of 1/4 of the SSM (EUR 659.45/month Jan 2025; EUR 675.94 from May 2025), with NO floor or ceiling  _(CCSS Avis 17.01.2025; PwC LU Other taxes.)_
- **Accident insurance and occupational health** — Accident insurance: base 0.700% employer only, adjusted by a bonus-malus factor (0.595% at 0.85 up to 1.050% at 1.50). Occupational health 0.14% employer only (private sector using STM).  _(CCSS Avis 17.01.2025.)_

**Mutualite des Employeurs (MDE) 2025 by absenteeism class**  _(CCSS Avis 17.01.2025.)_

| Class | Rate |
| --- | --- |
| Class 1 | 0.07% |
| Class 2 | 0.99% |
| Class 3 | 1.48% |
| Class 4 | 2.64% |

- **Family benefits (prestations familiales)** — 1.70% employer only, PUBLIC-sector employers ONLY; private-sector employers pay 0% (state-funded)  _(CCSS Avis 17.01.2025.)_
- **Social-contribution maximum base (ceiling) = 5 x SSM** — EUR 13,188.96/month (1 Jan 2025, index 944.43) then EUR 13,518.68/month (from 1 May 2025, index 968.04); annual max approx EUR 162,224. Ceiling does NOT apply to dependency.  _(CCSS Avis 17.01.2025; Orbitax.)_
- **Minimum contribution base = SSM unskilled (aged 18+)** — EUR 2,637.79/month (1 Jan 2025) then EUR 2,703.74/month (1 May 2025). Skilled SSM is ~+20% (EUR 3,165.31 then EUR 3,244.48).  _(CCSS Avis 17.01.2025; WAT Fiduciary.)_
- **CCSS invoicing and remittance** — The CCSS invoices the employer the combined employee + employer contributions monthly (extrait de compte); the employer deducts the employee share and remits the full amount, payable within 10 days of the statement's issue.  _(CCSS recouvrement.)_
- **Wage withholding remittance frequency** — Monthly if monthly withholding >= EUR 750; quarterly if EUR 75--749; annually if < EUR 75; declared and paid via MyGuichet.lu by the 10th of the month following the period.  _(guichet.public.lu retenue-impot.)_
- **Tax credits** — CIS EUR 0--600/year; CIM EUR 750--3,504/year (class 1a); CISSM EUR 81/month for gross EUR 1,800--3,000, degressive to zero at EUR 3,600  _(PwC; Guichet.lu.)_
- **Employer registration** — File the declaration d'exploitation with the CCSS within 8 days of the first employee's entry; declare each new hire (declaration d'entree) and each departure (declaration de sortie) within 8 days.  _(guichet.public.lu; CCSS.)_
- **Annual salary statement** — Transmit the electronic salary statement (extrait de compte salaire / certificat de salaire) of all salaries paid and tax withheld to the ACD before 1 March of the year following the tax year (RGD 26.03.2014).  _(guichet.public.lu extrait-compte-salaire.)_
- **Two 2025 parameter sets** — Use index 944.43 figures for Jan--Apr 2025 and index 968.04 figures from 1 May 2025.  _(Section 10 item 17)_

## Section 11 -- Tier 2 Catalogue (reviewer judgement)

Items requiring professional judgement; apply the default and flag the question.

### 11.1 Tax class and card

Default: require the tax card data; do not guess the class. If no valid card, class 1 min 33%. Question: "What tax class (1, 1a or 2) does the employee's fiche de retenue d'impot show, and are any deductions/credits noted?" — R-LU-P-1.

### 11.2 Class 1a / class 2 withholding mechanics

Default: flag for the payroll engine / ACD bareme. Question: "Is this employee class 1a or 2? The withholding-table mechanics differ from class 1." [RESEARCH GAP — only the class 1 scale and a ~EUR 26,460 class 1a allowance estimate are enumerated.]

### 11.3 Public vs private sector (family benefits)

Default: private sector (no 1.70% family-benefits contribution). Question: "Is the employer a public-sector body? Only public-sector employers pay the 1.70% prestations familiales contribution."

### 11.4 MDE absenteeism class

Default: model a mid class until the CCSS-assigned class is known. Question: "What MDE absenteeism class has the CCSS assigned the employer?" Swings employer cost between 0.07% and 2.64%.

### 11.5 Accident bonus-malus factor

Default: 0.700% with factor 1.00. Question: "What accident bonus-malus factor (0.85--1.50) has the Accident Insurance Association notified?"

### 11.6 Occupational health (sante au travail)

Default: 0.14% if the employer uses the multi-sector service (STM). Question: "Which occupational-health service is the employer affiliated to? STM = 0.14%; in-house/sector services may differ."

### 11.7 Index / parameter set

Default: Jan 2025 set for Jan--Apr; May 2025 set from 1 May 2025. Question: "Which 2025 pay period — before or from 1 May 2025?"

### 11.8 Solidarity surcharge step-up

Default: 7%. Question: "Does taxable income exceed EUR 150,000 (class 1/1a) or EUR 300,000 (class 2)?" — if so, 9%.

### 11.9 CIS / CISSM / CIM credits

Default: apply only credits shown on the tax card. Question: "Are CIS, CISSM or CIM credits noted on the card?"

### 11.10 Benefits in kind / impatriate regime

Default: treat cash gross only; flag benefits. Question: "Any company car, housing, equity, or impatriate-regime entitlement?" — R-LU-P-4 / R-LU-P-5. [RESEARCH GAP — benefit-in-kind valuation rules not detailed here.]

### 11.11 Cross-border / frontalier

Default: domestic Luxembourg contributions and withholding. Question: "Is the employee a frontalier or holding an A1/E101 certificate?" — R-LU-P-3.

### 11.12 Penalty / interest on late remittance

Default: flag exposure. Question: "Were any CCSS entry/exit declarations, CCSS payments, or wage-withholding payments late?" See Section 15.

## Section 12 -- Excel Working Paper Template

Per `payroll-workflow-base`. One row per employee per pay period. Suggested columns:

**Excel working paper column definitions**  _(payroll-workflow-base)_

| Col | Header | Notes |
| --- | --- | --- |
| A | Employee name | -- |
| B | Matricule (social security number) | 13-digit Luxembourg national ID |
| C | Tax class | 1 / 1a / 2 (from tax card) |
| D | Pay period | e.g. 2025-06 |
| E | Gross remuneration | Period gross |
| F | Capped base | min(gross, EUR 13,518.68/month for May 2025; EUR 13,188.96 Jan--Apr) |
| G | Dependency base | gross − 1/4 SSM abatement (EUR 675.94 May 2025; EUR 659.45 Jan--Apr); **no cap, no floor** |
| H | Employee pension 8.00% | F × 8.00% |
| I | Employee sickness 3.05% | F × 3.05% |
| J | Employee dependency 1.40% | **G × 1.40%** (post-abatement, uncapped) |
| K | Wage withholding (income tax + solidarity − credits) | per tax card / ACD bareme |
| L | Net pay | E − H − I − J − K |
| M | Employer pension 8.00% | F × 8.00% |
| N | Employer sickness 3.05% | F × 3.05% |
| O | Employer accident | F × 0.700% × bonus-malus factor |
| P | Employer occupational health 0.14% | F × 0.14% (if STM) |
| Q | Employer MDE | F × class rate (Class 2 = 0.99%) |
| R | Employer family benefits 1.70% | F × 1.70% (**public sector only**; else 0) |
| S | Total employer cost | E + M + N + O + P + Q + R |

Summary sheet rolls up: total wage withholding (→ ACD via MyGuichet.lu), total CCSS contribution bundle (employee + employer, → CCSS), and total employer cost. Note column J's base (G, post-abatement, uncapped) differs from the capped base F used everywhere else; the employer pays no dependency, and (private sector) no family benefits.

## Section 13 -- Luxembourg Bank Statement / Terminology Reading Guide

BGL BNP Paribas, Banque et Caisse d'Epargne de l'Etat (Spuerkeess), Banque Internationale a Luxembourg (BIL) and Banque Raiffeisen typically use semicolon or comma delimiters and DD/MM/YYYY dates. EUR only. Statements often mix French, German and Luxembourgish narratives.

**Language variants (treat as English equivalent)**

| French / German / Luxembourgish | English |
| --- | --- |
| Salaire / Traitement / Lohn / Gehalt | Salary |
| Paie / Masse salariale / Lohnlauf | Payroll run |
| Securite sociale / CCSS / Centre commun | Social security (CCSS bundle) |
| Retenue d'impot / RTS / Lohnsteuer | Wage withholding tax |
| Fonds pour l'emploi / Solidarite | Solidarity surcharge (employment fund) |
| Assurance dependance / Pflegeversicherung | Dependency / long-term care insurance |
| Assurance accident / Unfallversicherung | Accident insurance |
| Sante au travail / Arbeitsmedizin | Occupational health |
| Mutualite des Employeurs / MDE | Employer mutual insurance |
| Prestations familiales | Family benefits |
| Heures supplementaires / Ueberstunden | Overtime |

"ACD" / "Administration des contributions directes" / "Contributions directes" / "MyGuichet" = the tax authority (wage withholding). "CCSS" / "Centre commun de la securite sociale" / "Securite sociale" = the single social-contribution collector (pension, sickness, dependency, accident, occupational health, MDE — and, for public-sector employers, family benefits — all in one invoice / extrait de compte).

- **IBAN prefix** — LU = Luxembourg  _(Section 13)_

## Section 14 -- Onboarding Fallback

### 14.1 Worker type

Inference: employment contract = employee. Fallback: "Is this an employee on payroll or a self-employed / non-salaried person?" If self-employed → R-LU-P-2.

### 14.2 Tax card

Fallback: "Do you have the employee's fiche de retenue d'impot (electronic tax card) data with the tax class?" If not → R-LU-P-1 (else class 1, min 33%).

### 14.3 Pay frequency

Inference: monthly by default. Fallback: "Monthly pay confirmed?"

### 14.4 Gross remuneration

Fallback: "Monthly gross salary, and any 13th month / bonus / benefits in kind?"

### 14.5 Employer sector and rates

Fallback: "Is the employer public or private sector? What MDE absenteeism class and accident bonus-malus factor applies? (defaults: private sector / mid MDE class / accident factor 1.00)"

### 14.6 Index / period

Inference: current calendar year. Fallback: "Which 2025 pay period — before or from 1 May 2025? (parameters differ)"

### 14.7 Registration

Fallback: "Is the employer registered with the CCSS (matricule employeur, declaration d'exploitation) and has the new hire's declaration d'entree been filed within 8 days?"

### 14.8 Cross-border

Fallback: "Is the employee a frontalier (commuting from FR/BE/DE) or holding an A1 certificate?" — R-LU-P-3 if cross-border.

## Section 15 -- Filing Obligations and Penalties

### Forms and Deadlines

**Forms and Deadlines**  _(Forms and Deadlines)_

| Form | Purpose | Deadline |
| --- | --- | --- |
| Fiche de retenue d'impot (electronic tax card) | Determines the employee's tax class and deductions/credits; transmitted electronically by the ACD to the employer | Transmitted by the ACD; if absent, withhold class 1 min 33% |
| Declaration de la retenue d'impot sur remunerations et des credits d'impot bonifies (via MyGuichet.lu) | Employer declares and pays income tax + solidarity surcharge withheld and reimbursable tax credits | **By the 10th** of the month following the period (monthly if >= EUR 750/mo; quarterly if EUR 75--749; annually if < EUR 75) |
| Extrait de compte salaire / certificat de salaire (annual salary statement) | Electronic transmission to the ACD of all salaries paid and tax withheld during the year (XML or online assistant on MyGuichet.lu); employee also receives an annual salary certificate | **Before 1 March** of the year following the tax year (RGD 26.03.2014) |
| Declaration d'exploitation (employer registration with CCSS) | Obtain the employer registration number (matricule employeur) | **Within 8 days** of the first employee's entry |
| Declaration d'entree (start of employment) | Notify the CCSS of each new hire so they are affiliated to social security | **Within 8 days** of hiring |
| Declaration de sortie (end of employment) | Notify the CCSS when an employee leaves | **Within 8 days** of departure |
| Monthly CCSS account statement (extrait de compte) | CCSS computes total social contributions (employee + employer) and invoices the employer | Balance payable **within 10 days** of the statement's issue |

### Penalties and Interest

**Penalties and Interest**  _(Penalties and Interest)_

| Item | Detail |
| --- | --- |
| Late payment of social contributions (CCSS) | **Default interest of 0.6% per full calendar month** (fractions of a month disregarded), running from the 1st day of the month following the due date; after 4 unpaid monthly statements the CCSS begins enforced recovery. (CCSS recouvrement.) |
| Late declaration of start of employment (>30 days late) | **EUR 50 per month of delay, capped at EUR 2,500.** (guichet.public.lu declaration-entree.) |
| Late / non-filing of annual salary statement with the ACD (after 1 March) | Additional tax charge (majoration) for late/non-filing, or a fine, set under the relevant LIR / RGD provisions. **[RESEARCH GAP — not published as a single fixed figure; reviewer to confirm against the ACD.]** |
| Late payment / non-declaration of withholding tax to the ACD | Late-payment interest and surcharges (majorations) under the LIR; the responsible **employer is personally liable** for withholding tax not correctly deducted/remitted. (LIR; guichet.public.lu.) |

## Section 16 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (wage withholding + CCSS) | **This skill (luxembourg-payroll.md)** |
| Resident/employee personal income tax | luxembourg-income-tax.md |
| Social contributions detail | luxembourg-social-contributions.md |
| Luxembourg VAT returns | luxembourg-vat-return.md |
| Employer corporate tax | luxembourg-corporate-tax.md |
| Cross-border / frontalier / A1 / treaty | cross-border skill |

### Key Handoff Points

Payroll → Bookkeeping: Gross wages and all employer contributions (pension, sickness, accident, occupational health, MDE, plus family benefits if public sector) are expenses; wage withholding and the employee social share are liabilities until remitted to the ACD / CCSS.

Payroll → Income Tax: Employment income and withholding feed the employee's annual income tax assessment and the employer's annual salary statement (extrait de compte salaire) to the ACD.

Payroll → Self-employed: Self-employed and non-salaried persons are handled outside payroll.

## Section 17 -- Reference Material and Test Suite

### Sources

1. Centre commun de la securite sociale (CCSS) — Avis aux employeurs - Taux de cotisation au 01.01.2025 pour salaries (official notice, 17.01.2025): https://ccss.public.lu/dam-assets/publications/2025/ccss-20250117-avis-80-99-fr-de.pdf
2. CCSS — Social parameters: https://ccss.public.lu/en/parametres-sociaux.html
3. PwC Worldwide Tax Summaries — Luxembourg, Individual, Taxes on personal income (2025 scale, tax classes, solidarity surcharge): https://taxsummaries.pwc.com/luxembourg/individual/taxes-on-personal-income
4. PwC Worldwide Tax Summaries — Luxembourg, Individual, Other taxes (social security rates, ceiling, dependency contribution): https://taxsummaries.pwc.com/luxembourg/individual/other-taxes
5. Guichet.lu (ACD) — Withholding tax on salaries (fiche de retenue, declaration/payment deadlines, form): https://guichet.public.lu/en/entreprises/ressources-humaines/remuneration/fiche-retenue-impot/retenue-impot.html
6. Guichet.lu (ACD) — Filing salary and pension statements (annual statement, 1 March deadline): https://guichet.public.lu/en/entreprises/ressources-humaines/remuneration/fiche-retenue-impot/extrait-compte-salaire-pension.html
7. Orbitax — Luxembourg Minimum and Maximum Social Security Contribution Basis Amounts Increased from May 2025: https://orbitax.com/news/country/article/Luxembourg-Minimum-and-Maximum-59351
8. WAT Fiduciary — Social parameters Luxembourg 05/2025 (May 2025 SSM, ceiling, index 968.04): https://watfiduciary.lu/en/social/social-parameters-luxembourg-05-2025/
9. FEDIL — Social parameters applicable as from January 1st 2025: https://fedil.lu/en/publications/social-parameters-applicable-as-from-january-1st-2025/
10. Guichet.lu — Making a declaration of start of employment to the social security (8-day rule, EUR 50/month penalty): https://guichet.public.lu/en/entreprises/ressources-humaines/securite-sociale/declaration-entree.html

### Known Gaps

1. Class 1a tax-free allowance (~EUR 26,460 for 2025) and the class 1a / class 2 withholding-table mechanics are reported by secondary summaries; verify against the ACD bareme.
2. Only the class 1 marginal scale is enumerated; exact monthly withholding amounts require the ACD class-by-class withholding tables.
3. The accident bonus-malus factor (0.595%--1.050%) and the MDE absenteeism class are employer-specific and assigned by the relevant institutions; replace defaults with the employer's notified rates.
4. The occupational-health rate (0.14%) assumes the multi-sector service (STM); employers with their own/sector service may differ.
5. Family benefits 1.70% applies to public-sector employers only; private-sector payroll sets it to 0%.
6. The 17-18 (80%) and 15-17 (75%) SSM rates are given for Jan 2025; the May 2025 equivalents are not enumerated in the research data.
7. The exact statutory penalty for late/non-filing of the annual salary statement (additional tax vs fine) is not published as a single fixed figure.
8. A separate state pension reform raised the pension contribution rate for 2026 (from 8% to 8.05% per party); this is out of scope for 2025 and must NOT be applied to 2025 payroll.
9. The live CCSS HTML "parametres sociaux" page and several Big-4 newsletter pages returned HTTP 403 to automated fetch; figures are anchored to the official CCSS 17.01.2025 PDF and corroborated by Orbitax/WAT — a reviewer should confirm against the CCSS table before filing.

### Test Suite

A correct implementation should pass each of these checks (May 2025 / index 968.04 parameter set unless noted):

1. 0% band: A class-1 employee with annual taxable income within EUR 13,230 has EUR 0 income tax before the solidarity surcharge.
2. Unskilled minimum wage nil tax: An unskilled-SSM earner (EUR 2,703.74/month) has nil wage tax in all classes for 2025 after the CISSM/CIS credits.
3. No valid card: With no valid tax card, withholding is at class 1, minimum 33%.
4. Employee social rate: A within-ceiling employee deducts pension 8.00% + sickness 3.05% + dependency 1.40% (on the post-abatement base) — the dependency base is not the gross.
5. Dependency abatement: Dependency base = gross − EUR 675.94 (May 2025); e.g. on EUR 4,500 → 1.40% × 3,824.06 = EUR 53.54.
6. Dependency uncapped: On EUR 16,000/month, dependency is 1.40% × (16,000 − 675.94) = EUR 214.54 — computed on the full post-abatement income, not the EUR 13,518.68 ceiling.
7. Ceiling on other branches: On EUR 16,000/month, pension is 8.00% × 13,518.68 (capped) = EUR 1,081.49 — not 8.00% × 16,000.
8. Employer on-cost (Ex.3): 1,081.49 + 412.32 + 94.63 + 18.93 + 133.83 = EUR 1,741.20 (private sector, MDE Class 2, accident 0.700%).
9. No employer dependency: The employer pays EUR 0 dependency; it is employee-only.
10. No private-sector family benefits: A private-sector employer pays EUR 0 family benefits; the 1.70% is public-sector only.
11. Accident employer-only: Accident base 0.700% (factor 1.00 default) is paid by the employer only; employee EUR 0.
12. MDE classes: Class 1 = 0.07%, Class 2 = 0.99%, Class 3 = 1.48%, Class 4 = 2.64%.
13. Solidarity surcharge: 7% of income tax due; step to 9% only above EUR 150,000 (class 1/1a) / EUR 300,000 (class 2) taxable income.
14. Index boundary: Jan--Apr 2025 uses SSM EUR 2,637.79 / max base EUR 13,188.96 / abatement EUR 659.45 (index 944.43); from May 2025 uses EUR 2,703.74 / EUR 13,518.68 / EUR 675.94 (index 968.04).
15. Withholding frequency: Monthly withholding >= EUR 750 → monthly; EUR 75--749 → quarterly; < EUR 75 → annually; due by the 10th of the following month via MyGuichet.lu.
16. CCSS combined remittance: The CCSS invoices employee + employer combined (extrait de compte); the employer remits the full amount within 10 days; late payment = 0.6%/month default interest.
17. CCSS entry deadline: A new hire must be declared (declaration d'entree) within 8 days; >30 days late = EUR 50/month, max EUR 2,500.
18. Annual salary statement: The extrait de compte salaire for tax year 2025 is due before 1 March 2026.

## PROHIBITIONS

- NEVER run wage withholding without the employee's tax card (fiche de retenue d'impot) data — without a valid card the employer must withhold at class 1, minimum 33%; trigger R-LU-P-1.
- NEVER compute the dependency contribution on gross — it is on gross less the 1/4-SSM abatement (EUR 675.94/month from May 2025; EUR 659.45 Jan--Apr) and has NO floor or ceiling.
- NEVER apply the 5 x SSM ceiling to the dependency contribution — only pension, sickness, accident, occupational health, MDE and (public-sector) family benefits are capped.
- NEVER charge the employer a dependency contribution — the 1.40% is employee only.
- NEVER charge a private-sector employer the 1.70% family-benefits contribution — it is public-sector only.
- NEVER compute capped-branch contributions on earnings above the ceiling (EUR 13,518.68/month from May 2025; EUR 13,188.96 Jan--Apr 2025).
- NEVER mix the two 2025 parameter sets — use index 944.43 for Jan--Apr 2025 and index 968.04 from May 2025.
- NEVER omit the employer-only funds (accident 0.700%, occupational health 0.14%, MDE by class) on top of employer pension and sickness.
- NEVER apply the 2026 pension rate (8.05%/party) to 2025 — that change takes effect 1 January 2026 and is out of scope.
- NEVER forget the solidarity surcharge (7%, or 9% above EUR 150,000 / 300,000) on top of the income tax due.
- NEVER miss the wage-withholding remittance (by the 10th of the following month via MyGuichet.lu), the CCSS payment (within 10 days of the statement), the CCSS entry declaration (within 8 days of hiring) or the annual salary statement (before 1 March) — penalties apply.
- NEVER run a self-employed / non-salaried person through employer payroll — trigger R-LU-P-2.
- NEVER present payroll computations as definitive — always label as estimated and direct to a Luxembourg reviewer (expert-comptable / fiduciaire).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable or fiduciaire in Luxembourg) before implementation.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
