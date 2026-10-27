---
name: luxembourg-social-contributions
description: "Luxembourg social security contributions (cotisations sociales) for tax year 2026, collected by the CCSS: employee and employer shares for sickness (2.80% + 0.25% cash surcharge each side), pension (8.50% each side, 17% in total from 1 January 2026), dependency (1.40%, employee only, no ceiling, after a quarter-SSM abatement), accident (0.65% times the bonus-malus factor), Mutualité des employeurs classes 1 to 4, occupational health 0.14% and family benefits 1.70% (public sector only); the SSM floor and 5x SSM ceiling for 1 January and 1 June 2026; self-employed contributions on professional income with the provisional SSM base; entry, exit and wage declarations, the monthly account statement and 10-day payment, 0.6% monthly late interest and fines. Trigger on: CCSS cotisations 2026, Luxembourg social security rates, independant cotisations, MDE classe, maximum cotisable, dependance abattement. Out of scope: luxembourg-payroll (wage tax withholding), luxembourg-income-tax, lu-cross-border, lu-corporate-tax."
version: 0.4
jurisdiction: LU
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg social security contributions (2026)

## Luxembourg Social Security Contributions (Cotisations Sociales) Skill v0.4

What matters for 2026:

- **Pension is 8.50% for the employee and 8.50% for the employer** (17% in total, 16% in 2025). Source: CCSS notice to employers of 16 January 2026 and the CCSS social parameters page.
- **Accident base rate is 0.65%** (0.70% in 2025). The Mutualité des employeurs classes are 0.23% / 0.95% / 1.56% / 2.66%.
- **Two parameter sets in 2026.** From 1 January (index 968.04): SSM EUR 2,703.74, ceiling EUR 13,518.68, dependency abatement EUR 675.93. From 1 June (index 992.24): SSM EUR 2,771.33, ceiling EUR 13,856.63, abatement EUR 692.83.

This skill covers contributions. For wage tax withholding and the full gross-to-net use `luxembourg-payroll`. For income tax use `luxembourg-income-tax`. For frontier workers and which country insures a person use `lu-cross-border`.

## Who this applies to

- **Employees in Luxembourg.** The employer must file an entry declaration with the CCSS within 8 days of hiring. Insurance covers sickness, pension, dependency and accident. The employer withholds the employee share and pays both shares to the CCSS.
- **Employers.** Private-sector employers pay sickness, pension, accident, Mutualité des employeurs (MDE) and, if they use the multisector occupational health service (STM), occupational health. Family benefits contributions (1.70%) apply only to the public sector.
- **Self-employed people (indépendants).** They pay their own contributions to sickness, pension, accident and dependency. MDE membership is optional for them.
- **Partners and managers of companies.** A manager or director (gérant, administrateur) who is treated as self-employed for social security pays as an indépendant, even if paid through a payslip. Their salary and any profit paid to them by the same company are added together.
- **Helping spouse or partner.** The self-employed person's professional income is split into two equal parts. The helper's part is capped at 2 x SSM; the excess goes back to the main insured person.

Out of scope: voluntary insurance, farmers, public-sector special schemes, and the rules on which country insures a cross-border worker.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Sickness, benefits in kind (soins de santé) | 2.80% employee + 2.80% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Sickness, cash benefits surcharge (prestations en espèces) | 0.25% employee + 0.25% employer, only for people entitled to sick pay | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Pension | 8.50% employee + 8.50% employer (17% total; 16% in 2025) | 2026 | https://ccss.public.lu/fr/parametres-sociaux.html |
| Dependency (long-term care) | 1.40%, insured person only, no floor and no ceiling | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Dependency abatement (1/4 SSM), 1 January to 31 May | EUR 675.93 a month | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Dependency abatement, from 1 June | EUR 692.83 a month | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |
| Family benefits | 1.70% employer, public sector only | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Occupational health (santé au travail) | 0.14% employer, only for private employers using the STM | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Accident, base rate | 0.65% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Accident, by bonus-malus factor 0.85 / 1.00 / 1.10 / 1.30 / 1.50 | 0.5525% / 0.65% / 0.715% / 0.845% / 0.975% | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| MDE class 1 (financial absence rate under 0.65%) | 0.23% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| MDE class 2 (under 1.60%) | 0.95% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| MDE class 3 (under 2.50%) | 1.56% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| MDE class 4 (2.50% or more) | 2.66% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| SSM, unqualified, 18 and over (minimum base), 1 January | EUR 2,703.74 a month (index 968.04) | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Minimum base, age 17 to 18 (80% SSM) / 15 to 17 (75% SSM), 1 January | EUR 2,162.99 / EUR 2,027.80 | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Maximum base (5 x SSM), 1 January | EUR 13,518.68 a month | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| SSM, unqualified, 18 and over, from 1 June | EUR 2,771.33 a month (index 992.24) | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |
| Minimum base, age 17 to 18 / 15 to 17, from 1 June | EUR 2,217.06 / EUR 2,078.49 | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |
| Maximum base (5 x SSM), from 1 June | EUR 13,856.63 a month | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |
| SSM at index 100 | EUR 279.30 | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |

The CCSS computes the ceiling as five times the unrounded SSM (279.30 x 9.6804 x 5 = 13,518.68). Use the published figures.

## The taxable base

**Employees.** The base is the gross pay the employer declares each month. The CCSS table of what counts for which branch:

| Pay element | Sickness cash | Sickness in kind | MDE | Pension | Accident | Dependency | Occupational health |
|---|---|---|---|---|---|---|---|
| Base pay | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Monthly cash supplements (commissions, performance bonus paid monthly) | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Overtime pay, without the overtime premium | No | Yes | No | No | No | Yes | No |
| Gratuities, profit shares, cash and in-kind benefits | No | Yes | No | Yes | Yes | Yes | Yes |
| Short-time and bad-weather unemployment | Yes | Yes | Yes | Yes | No | Yes | No |

So a one-off bonus carries 2.80% sickness, not 3.05%, and no MDE.

- The overtime premium (40%) is not declared.
- Statutory pay in lieu of notice is contributable, one month of declaration per month of notice. Other leaving payments are not contributable.
- Floor and ceiling: the minimum base (SSM) and the maximum base (5 x SSM) apply to every branch except dependency.
- Dependency: the base is gross pay less the abatement (EUR 675.93, or EUR 692.83 from 1 June). If the person works fewer than 150 hours a month for an employer, the abatement is cut in proportion to hours declared over 173.
- Hours: since 1 January 2020 the employer declares the exact hours paid, not a flat 173.

**Residents: dependency on income beyond pay.** Dependency is not limited to wages or professional income. Its base also covers replacement income and income from assets (art. 376 CSS). For a resident taxpayer, the ACD (not the CCSS) charges 1.40% on the net income in categories 6 to 8 of art. 10 of the income tax law (income from capital, rental income and miscellaneous net income), counting each category only when it is positive (art. 378(1) and (2) CSS). The ACD also charges it on pensions and annuities under art. 96 of that law, except supplementary pension scheme benefits and pensions paid under Book III CSS or a statutory scheme. It applies only to residents who are within the dependency insurance's beneficiary group (art. 352 CSS, art. 378(3)). A yearly contribution of EUR 24.79 or less is treated as nil (art. 378(4)). The contribution is not income tax and is not deductible for income tax (art. 378(5)). Source: Code de la sécurité sociale, consolidated at 1 January 2026, arts. 376 and 378.

**Self-employed.** The base is professional income: commercial profit, profit from a liberal profession, a self-employed manager's pay, replacement income (such as sick pay) and professional income earned abroad by someone insured in Luxembourg. With several activities, all income is added together.

- In the first year, the CCSS bills provisionally on the SSM, unless the person gives a better estimate. For a side activity next to a job, the provisional base is one third of the SSM.
- The final base is the income on the ACD tax assessment. The CCSS then recalculates. In later years it bills on the last known income.
- The floor (SSM) and ceiling (5 x SSM) apply to sickness, pension and accident. Dependency has no floor and no ceiling.
- No dependency abatement for the self-employed. The quarter-SSM abatement covers only the groups listed in art. 377(4) CSS (employees, apprentices, seafarers and others); self-employed people under art. 1(4) CSS are not on that list, so dependency is 1.40% of the full professional income.
- If the self-employed person is entitled to cash sick pay, sickness carries the 0.50% surcharge on top of 5.60% (art. 29(2) CSS), and the self-employed person bears all of it (art. 32 CSS).
- Accident: the bonus-malus factor applies to every contributor, including the self-employed, who form risk class 15 (règlement grand-ducal of 8 February 2016, arts. 2 and 3).
- Who sets the factor: a new employer pays the base accident rate (0.65%) from the start of activity. Afterwards the Association d'assurance accident (AAA) sets each employer's bonus-malus factor and tells the employer; the CCSS applies it (CCSS employer registration page; CCSS rate notice of 16 January 2026, note 5).
- Someone above the ceiling because of several activities can ask for a refund of the excess.

## Deadlines and filing

| Obligation | Deadline | How |
|---|---|---|
| Employer registration (déclaration d'exploitation) | Within 8 days after the first employee starts (Guichet.lu) | CCSS form (déclaration d'exploitation) |
| Entry declaration (déclaration d'entrée) | Within 8 days of hiring | SECUline (DECAFF), MyGuichet.lu or paper form |
| Exit declaration (déclaration de sortie) | Within 8 days of the end of the contract | SECUline (DECAFF), MyGuichet.lu or paper form |
| Monthly wage declaration (DECSAL) | Each month for the previous month. The pre-printed wage list for month N is sent early in month N+1 and must be returned within 10 days | SECUline, MyGuichet.lu or paper list |
| Payment (employers and self-employed) | Within 10 days of the account statement (extrait de compte), even if disputed | Bank transfer or direct debit |

The account statement runs two months behind. March contributions appear on the May statement. A self-employed person pays with their 13-digit national number followed by "60" as the reference.

## Penalties and interest

- **Late payment interest.** Contributions not paid by the due date carry interest of 0.6% for each full calendar month, starting on the 1st day of the 1st month after the due date. Part months are ignored.
- **Enforced collection.** For employers, the CCSS starts enforced collection after 4 unpaid monthly statements. For the self-employed, the CCSS sends a warning at 3 months of arrears and a formal notice by registered letter at 4 months (pay within 15 days or follow the payment plan).
- **Payment plans.** A self-employed person can ask for a payment plan. Each month's instalment plus current contributions is due by the 25th. No plan is granted once enforced collection has started.
- **Late entry declaration.** After a 30-day tolerance, EUR 50 for each month late, up to EUR 2,500 (Guichet.lu).
- **Other employer failures.** An employer who files late or wrongly (exit declaration, wage declaration, any other information) or pays contributions late can be fined up to EUR 2,500 (amende d'ordre, art. 445 CSS). For a missing wage declaration the CCSS also estimates the salary, normally from the last one declared.

## Cross-border points

- Which country insures a person working in more than one EU/EEA state or Switzerland is decided under the EU coordination rules, not by this skill. Use `lu-cross-border`, which covers frontier workers, A1 certificates and the telework agreements.
- A self-employed person insured in Luxembourg pays on professional income earned abroad too.
- Workers from outside the EU, EEA and Switzerland get their social security number through the Directorate of Immigration before the entry declaration can be filed.

## Worked examples

**Example 1. Private-sector employee, EUR 5,000 a month, March 2026.** The 1 January parameters apply. The employer uses the STM, has bonus-malus factor 1.00 and is in MDE class 1. Pay is under the ceiling, so the full EUR 5,000 is the base. Employee: sickness 2.80% (EUR 140.00), cash surcharge 0.25% (EUR 12.50), pension 8.50% (EUR 425.00), dependency 1.40% of (5,000 - 675.93) = EUR 60.54. Employee total EUR 638.04. Employer: sickness EUR 140.00, cash surcharge EUR 12.50, pension EUR 425.00, occupational health 0.14% (EUR 7.00), accident 0.65% (EUR 32.50), MDE 0.23% (EUR 11.50). Employer total EUR 628.50. No family benefits: private sector.

```oa-check
name: LU employee EUR 5,000 a month, March 2026, MDE class 1
inputs:
  gross: 5000
  ceiling: 13518.68
  abatement: 675.93
steps:
  - base: min(gross, ceiling)
  - sick_ee: base * 0.028
  - cash_ee: base * 0.0025
  - pension_ee: base * 0.085
  - dependency: round((gross - abatement) * 0.014, 2)
  - employee_total: sick_ee + cash_ee + pension_ee + dependency
  - employer_total: base * (0.028 + 0.0025 + 0.085 + 0.0014 + 0.0065 + 0.0023)
expected:
  employee_total: 638.04
  employer_total: 628.50
```

**Example 2. Employee above the ceiling, EUR 15,000 a month, July 2026.** The 1 June parameters apply: ceiling EUR 13,856.63 and abatement EUR 692.83. The employer uses the STM, has bonus-malus factor 1.10 (0.715%) and is in MDE class 2 (0.95%). Every branch except dependency is capped at EUR 13,856.63. Employee: sickness and cash surcharge 3.05% of 13,856.63 = EUR 422.63, pension 8.50% = EUR 1,177.81, dependency 1.40% of (15,000 - 692.83) with no cap = EUR 200.30. Employee total EUR 1,800.74. Employer: 3.05% + 8.50% + 0.14% + 0.715% + 0.95% = 13.355% of 13,856.63 = EUR 1,850.55.

```oa-check
name: LU employee EUR 15,000 a month, July 2026, above ceiling
inputs:
  gross: 15000
  ceiling: 13856.63
  abatement: 692.83
steps:
  - base: min(gross, ceiling)
  - health_ee: base * (0.028 + 0.0025)
  - pension_ee: base * 0.085
  - dependency: round((gross - abatement) * 0.014, 2)
  - employee_total: health_ee + pension_ee + dependency
  - employer_total: base * (0.028 + 0.0025 + 0.085 + 0.0014 + 0.00715 + 0.0095)
expected:
  employee_total: 1800.74
  employer_total: 1850.55
```

## Ask the client first

1. Employee, self-employed, or a company manager treated as self-employed?
2. Which month is the pay for? Before or after 1 June 2026 changes the ceiling, minimum and abatement.
3. Private or public sector, and does the employer use the STM for occupational health?
4. The employer's bonus-malus factor (from the AAA) and MDE class.
5. Is any of the pay a one-off bonus, benefit in kind or overtime?
6. For the self-employed: first year or not, is it a side activity next to a job, and the last income on the ACD assessment.

## Sources

| Source | URL | Read on |
|---|---|---|
| CCSS, notice to employers, contribution rates and minima/maximum at 1 January 2026 (16 January 2026) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf | 2026-10-27 |
| CCSS, notice to employers, minima and maximum at 1 June 2026 (14 August 2026) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf | 2026-10-27 |
| CCSS, social parameters (rates 2014 to 2026) | https://ccss.public.lu/fr/parametres-sociaux.html | 2026-10-27 |
| CCSS, employers: pay to declare and contributable bases | https://ccss.public.lu/fr/employeurs/secteur-prive/remuneration.html | 2026-10-27 |
| CCSS, employers: hiring, entry and exit declarations | https://ccss.public.lu/fr/employeurs/secteur-prive/engager-personnel.html | 2026-10-27 |
| CCSS, employers: billing, payment and late interest | https://ccss.public.lu/fr/employeurs/secteur-prive/facturation.html | 2026-10-27 |
| CCSS, employers: registration | https://ccss.public.lu/fr/employeurs/secteur-prive/immatriculation-employeur.html | 2026-10-27 |
| CCSS, self-employed: professional income | https://ccss.public.lu/fr/independants/cotisations-sociales/revenu-professionnel.html | 2026-10-27 |
| CCSS, self-employed: contribution base and recalculation | https://ccss.public.lu/fr/independants/cotisations-sociales/assiette-cotisation-adaptation.html | 2026-10-27 |
| CCSS, self-employed: billing and payment | https://ccss.public.lu/fr/independants/cotisations-sociales/facturation.html | 2026-10-27 |
| CCSS, self-employed: payment plans | https://ccss.public.lu/fr/independants/cotisations-sociales/demander-delai-paiement.html | 2026-10-27 |
| Code de la sécurité sociale, consolidated at 1 January 2026 (arts. 1, 29, 32, 352, 376, 377, 378, 445; RGD of 8 February 2016 on bonus-malus) | https://legilux.public.lu/eli/etat/leg/code/securite_sociale/20260101 | 2026-10-27 |
| Guichet.lu, entry declaration and late fine | https://guichet.public.lu/fr/entreprises/ressources-humaines/securite-sociale/declaration-entree.html | 2026-10-27 |

Not yet confirmed: the State's own pension share and the text of the pension reform law of 18 December 2025 (Legilux not readable today; the 17% total is from the CCSS); the amount the CCSS actually charges for a late exit or missing wage declaration within the art. 445 CSS cap of EUR 2,500; a calendar deadline date for the monthly wage declaration beyond the 10-day return of the wage list; the reference period the AAA uses to set the bonus-malus factor (the old version's 1 April Y-2 to 31 March Y-1 came from secondary sources; the AAA page was down on 27 October 2026); bank statement descriptions for CCSS debits (old version's pattern table, not from an official source).

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

> Contributed by Ryan Duguid.
