---
name: ne-payroll-social
description: "Niger payroll and social contributions for 2026: the monthly salary tax (impôt sur les traitements et salaires, ITS) scale in force from 1 January 2026, the family-charge reductions in force from 21 August 2026, and the CNSS contribution rates, annual ceiling, contribution base, employer affiliation and declaration rules as published by the Caisse Nationale de Sécurité Sociale. Built from the 2026 finance ordinance (Ordonnance 2025-44), its first rectification (Ordonnance 2026-45) and the CNSS's own pages. Use it to compute ITS on a known taxable monthly salary and CNSS contributions on an annual salary, and to plan CNSS declarations. The ITS taxable base, how the family reductions are applied, the ITS remittance date, the apprenticeship tax, the minimum contribution base and late penalties sit on visible holds. Two executable cases. Not yet approved by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ne-payroll-social"
  jurisdiction: "NE"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Niger payroll and social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Tax year 2026.** The ITS scale was replaced "A compter du 1er janvier 2026" by Ordonnance 2025-44. The family-charge reductions were replaced "A compter de la signature" of Ordonnance 2026-45, signed 21 August 2026. The CNSS figures are those the CNSS publishes; the decrees that set them were not read.

## Who this applies to

Every public or private employer that uses one or more workers within the meaning of article 1 of the Labour Code, working in Niger, must affiliate to the CNSS. Affiliation takes effect from the first hiring of a salaried worker [CNSS, Affiliation employeur](https://cnss.ne/employeur/affiliation-employeur/). The employer owes both the employer and the employee contributions: it deducts the employee share from pay and pays the whole to the CNSS [CNSS, Déclaration de salaire](https://cnss.ne/employeur/declaration-de-salaire/).

The CNSS runs three branches for salaried workers under article 2 of Law 2012-045 of 25 September 2012 (Labour Code): family benefits, occupational risks (work accidents and occupational diseases), and old-age, invalidity and survivors' pensions [CNSS, Missions et valeurs](https://cnss.ne/missions-valeurs/).

The employer also withholds ITS, a progressive tax computed by monthly bands [CGI art. 150 as replaced by Ordonnance 2025-44 art. 11, PDF page 7](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44). Who is liable to ITS, residence rules and exempt pay were not in the texts read.

## Rates, bands and thresholds

**ITS monthly scale from 1 January 2026** (bands of taxable monthly pay in XOF; each band's rate applies to the part of pay inside that band):

| Band of monthly taxable pay | Rate | Official source |
|---|---|---|
| 0 to 25,000 | 1% | [Ordonnance 2025-44 art. 11, CGI art. 150, PDF page 7](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) |
| 25,001 to 50,000 | 2% | same |
| 50,001 to 100,000 | 6% | same |
| 100,001 to 150,000 | 13% | same |
| 150,001 to 300,000 | 25% | same |
| 300,001 to 400,000 | 30% | same |
| 400,001 to 700,000 | 32% | same |
| 700,001 to 1,000,000 | 34% | same |
| Above 1,000,000 | 35% | same |

**Family-charge reductions (abattements) from 21 August 2026**, by number of family charges as defined in CGI art. 148:

| Family charges | Reduction | Official source |
|---|---|---|
| 0 | 0% | [Ordonnance 2026-45 art. 6, CGI art. 149(1), scan page 5](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) |
| 1 | 7% | same |
| 2 | 12% | same |
| 3 | 17% | same |
| 4 | 22% | same |
| 5 | 25% | same |
| 6 | 27% | same |
| 7 | 30% | same |

What the reduction percentage is applied to, and the reductions for 1 January to 20 August 2026, are in CGI articles not read: they are held.

**CNSS contributions, as published by the CNSS:**

| Item | Rate or amount | Official source |
|---|---|---|
| Family benefits branch | 8.40% (employer) | [CNSS, Missions et valeurs](https://cnss.ne/missions-valeurs/) |
| Work accidents and occupational diseases | 1.75% (employer) | same |
| Pensions | 11.50% in total: 6.25% employer, 5.25% employee | same |
| Total CNSS | 21.65% (16.40% employer, derived: 8.40% plus 1.75% plus 6.25%; 5.25% employee) | same |
| Ceiling | Pay counts only up to XOF 6,000,000 a year per employee | [CNSS, Immatriculation travailleur](https://cnss.ne/employeur/immatriculation-travailleur/) |
| ANPE levy | 0.5% borne by the employer for the Agence Nationale pour la Promotion de l'Emploi, collected under the same conditions as CNSS contributions | [CNSS, Missions et valeurs](https://cnss.ne/missions-valeurs/) |

## The base

### ITS, step by step

1. Establish the employee's **taxable monthly pay**. The rules that take gross pay to taxable pay (exempt items, deductions, benefits in kind) are in CGI articles not read: obtain them before computing. This Guide takes taxable monthly pay as an input.
2. Apply the band rates in the ITS table to each slice of taxable pay. The scale is written in whole francs ("De 25 001 A 50 000"); treating the bands as continuous gives the same result for whole-franc pay.
3. Add the band amounts to get the gross ITS for the month.
4. For pay from 21 August 2026, establish the number of family charges (CGI art. 148) and the reduction from the table. How the reduction is applied is held, so stop and refer before reducing the tax. Spouses each fill in the administration's form allocating family charges and hand it to their own employer [CGI art. 149(2), Ordonnance 2026-45 art. 6, scan page 5](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026).

### CNSS, step by step

1. **Base.** All pay and earnings, including allowances, bonuses, gratuities and other cash or in-kind benefits paid by the employer, excluding allowances that reimburse business expenses [CNSS, Immatriculation travailleur](https://cnss.ne/employeur/immatriculation-travailleur/). The CNSS adds that not all pay elements are included [CNSS, Paiement de cotisation](https://cnss.ne/employeur/paiement-de-cotisation/); its full list was not published there.
2. **Minimum.** The CNSS page says the pay taken into account can never be lower than the guaranteed minimum wage (SMIG), and states that minimum as XOF 30,047. The current SMIG decree was not read and the old Guide gave a different figure, so the minimum amount is held (see `## Sources`).
3. **Ceiling.** Count pay only up to XOF 6,000,000 a year per employee. The CNSS publishes the ceiling as an annual figure; a monthly equivalent is not published on the pages read, so compute annually or confirm the monthly rule first.
4. **Rates.** Apply 16.40% employer and 5.25% employee to the capped base. The ANPE levy of 0.5% is collected with the contributions; its base is not stated on the page read.

### New hires

If the new employee is already registered with the CNSS, ask for the insurance booklet (livret d'assurance) and enter the hiring date in it. If not, apply for registration on the CNSS form, using the birth certificate [CNSS, Immatriculation travailleur](https://cnss.ne/employeur/immatriculation-travailleur/).

## Deadlines and filing

| Obligation | Rule | Source |
|---|---|---|
| CNSS affiliation | From the first hire of a salaried worker | [CNSS, Affiliation employeur](https://cnss.ne/employeur/affiliation-employeur/) |
| CNSS quarterly nominative declaration | Within the first 30 days of each quarter, for each employee in the past quarter: total pay up to the ceiling and time worked (Decree 2005-64 of 11 March 2005, statutes of the CNSS, art. 34, as quoted by the CNSS) | [CNSS, Déclaration de salaire](https://cnss.ne/employeur/declaration-de-salaire/) |
| CNSS monthly statement, 20 or more employees | Employers with 20 or more employees also send, with the monthly payment of contributions, a statement of total pay within the ceiling | same |
| Forms | The CNSS supplies the forms; each payment is supported by a nominative list and a pay declaration | same |
| ITS remittance | Held: the due date and form were not in the texts read | none read |

The payment calendar for employers with fewer than 20 employees is not stated on the CNSS pages read; it is held.

## Penalties and interest

CNSS and ITS late-payment and late-declaration penalties were not read and are held. Do not quote a figure from memory.

## Cross-border points

The CNSS covers workers carrying out their activity in Niger [CNSS, Affiliation employeur](https://cnss.ne/employeur/affiliation-employeur/). Social-security agreements, the treatment of expatriate and seconded staff, and ITS on non-residents were not read and are held. The CGI applies subject to ratified international conventions [CGI preamble art. 1(2), Ordonnance 2025-44 art. 10, PDF page 3](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44).

## Two worked examples that recompute

**1. ITS on two monthly salaries (no family charges).** Employee A's taxable pay for October 2026 is XOF 200,000; employee B's is XOF 1,200,000. Neither has family charges (reduction 0%). A: 1% of 25,000 is 250; 2% of 25,000 is 500; 6% of 50,000 is 3,000; 13% of 50,000 is 6,500; 25% of 50,000 is 12,500; ITS XOF 22,750. B runs through all nine bands: 250 + 500 + 3,000 + 6,500 + 37,500 + 30,000 + 96,000 + 102,000 + 70,000 = XOF 345,750.

```oa-check
name: Niger ITS 2026 monthly scale, taxable pay 200,000 and 1,200,000
inputs:
  pay_a: 200000
  pay_b: 1200000
steps:
  a1: min(pay_a, 25000) * 0.01
  a2: max(min(pay_a, 50000) - 25000, 0) * 0.02
  a3: max(min(pay_a, 100000) - 50000, 0) * 0.06
  a4: max(min(pay_a, 150000) - 100000, 0) * 0.13
  a5: max(min(pay_a, 300000) - 150000, 0) * 0.25
  itsa: a1 + a2 + a3 + a4 + a5
  b1: min(pay_b, 25000) * 0.01
  b2: max(min(pay_b, 50000) - 25000, 0) * 0.02
  b3: max(min(pay_b, 100000) - 50000, 0) * 0.06
  b4: max(min(pay_b, 150000) - 100000, 0) * 0.13
  b5: max(min(pay_b, 300000) - 150000, 0) * 0.25
  b6: max(min(pay_b, 400000) - 300000, 0) * 0.30
  b7: max(min(pay_b, 700000) - 400000, 0) * 0.32
  b8: max(min(pay_b, 1000000) - 700000, 0) * 0.34
  b9: max(pay_b - 1000000, 0) * 0.35
  itsb: b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9
expected:
  itsa: 22750
  itsb: 345750
```

**2. CNSS for the year with the ceiling.** Employee C earns XOF 7,200,000 in 2026 and employee D XOF 4,800,000, all within the contribution base. C is capped at XOF 6,000,000: employer 16.40% is 984,000 and employee 5.25% is 315,000. D is under the ceiling: employer 787,200 and employee 252,000. Edge: the cap saves the employer XOF 196,800 on C's pay above the ceiling. The ANPE levy is left out because its base is not stated.

```oa-check
name: Niger CNSS 2026 annual contributions with the XOF 6,000,000 ceiling
inputs:
  pay_c: 7200000
  pay_d: 4800000
  ceiling: 6000000
  employer_rate: 0.164
  employee_rate: 0.0525
steps:
  base_c: min(pay_c, ceiling)
  base_d: min(pay_d, ceiling)
  employer_c: base_c * employer_rate
  employee_c: base_c * employee_rate
  employer_d: base_d * employer_rate
  employee_d: base_d * employee_rate
  employer_saving_c: (pay_c - base_c) * employer_rate
expected:
  base_c: 6000000
  employer_c: 984000
  employee_c: 315000
  employer_d: 787200
  employee_d: 252000
  employer_saving_c: 196800
```

## Ask the client first

- How many employees are there (20 or more changes the CNSS monthly statement), and when was the first hire?
- For each employee: gross pay, every allowance and benefit in kind, and which allowances reimburse business expenses.
- The taxable monthly pay under the ITS base rules, and the number of family charges with the allocation form for spouses.
- Is each employee already registered with the CNSS?
- Is any employee seconded from abroad or a non-resident?
- Which months fall before and after 21 August 2026?

## Sources

| Official source | What was read | Read on |
|---|---|---|
| [Ministry of Finance, Ordonnance 2025-44 of 31 December 2025, 2026 finance ordinance](https://finances.gouv.ne/index.php/lois-de-finances/file/1303-ordonnance-n-2025-44) | PDF downloaded through the page's public download form (SHA-256 a841c4fa...2f42e) and read: art. 10 (CGI preamble art. 1), PDF page 3; art. 11 opening and CGI art. 150 scale, pages 4 and 7; arts. 43 and 44 and signature, page 47 | 2026-11-17 |
| [Ministry of Finance, Ordonnance 2026-45 of 21 August 2026, first rectification](https://finances.gouv.ne/index.php/actualites/publications-du-ministere/file/1351-ordonnance-n-2026-45-premiere-rectification-de-la-loi-de-finances-2026) | Scanned PDF downloaded through the public download form (SHA-256 5e8a3a25...8fae); art. 6 (CGI art. 149) on scan page 5 and art. 25 with signature on page 48, read as page images | 2026-11-17 |
| [CNSS, Missions et valeurs](https://cnss.ne/missions-valeurs/) | Whole page read for branches, resources, 6,000,000 annual ceiling, 21.65% split, ANPE 0.5% | 2026-11-17 |
| [CNSS, Immatriculation travailleur](https://cnss.ne/employeur/immatriculation-travailleur/) | Whole page read for registering new hires, contribution base, SMIG floor sentence, 6,000,000 annual ceiling | 2026-11-17 |
| [CNSS, Déclaration de salaire](https://cnss.ne/employeur/declaration-de-salaire/) | Whole page read for employer as debtor, nominative list, quoted art. 34 of Decree 2005-64 | 2026-11-17 |
| [CNSS, Affiliation employeur](https://cnss.ne/employeur/affiliation-employeur/) | Whole page read for who must affiliate, from the first hire | 2026-11-17 |
| [CNSS, Paiement de cotisation](https://cnss.ne/employeur/paiement-de-cotisation/) | Whole page read for base is all pay, not every element included | 2026-11-17 |

Not yet confirmed: the ITS taxable base (gross to taxable pay, exempt items, benefits in kind); how the family-charge reduction is applied and the art. 148 definition of family charges; the reductions for 1 January to 20 August 2026; the ITS remittance date and form (the old Guide's "15th of the following month" for both ITS and CNSS); CNSS payment frequency for employers with fewer than 20 employees; the minimum contribution base (the CNSS page states XOF 30,047 as the SMIG; the old Guide's XOF 42,000 came from a private payroll blog and is not used; the current SMIG decree was not read); whether the XOF 6,000,000 ceiling is applied monthly as one twelfth; the decrees fixing the CNSS rates (the CNSS's published figures are used; the old Guide's employer total of "about 15.4% to 16.4%" is replaced by 16.40%); the ANPE levy base; the apprenticeship tax rate (the old Guide's "about 3%"; the 2026 rectification only names the tax); CNSS and ITS penalties; social-security agreements and expatriates. Not yet approved by an accountant.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ne-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ne-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
