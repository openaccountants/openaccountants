---
name: luxembourg-payroll
description: "Luxembourg payroll for employees for tax year 2026: monthly wage withholding (retenue d'impôt sur les salaires) from the electronic tax card using the ACD monthly scale built on the art. 118 LIR scale (23 bands, 0% to 42%) for tax classes 1, 1a and 2; the employment fund surcharge (7%, or 9% above EUR 150,000 in classes 1 and 1a and EUR 300,000 in class 2); the CIS, CI-CO2 and CISSM credits paid through payroll; CCSS contributions (pension 8.5% + 8.5%, sickness, dependency 1.4% after a quarter-SSM abatement, accident 0.65%, Mutualité des employeurs classes, occupational health); the 1 January and 1 June 2026 parameter sets; withholding and CCSS deadlines and penalties. Trigger on: Luxembourg payroll, gross to net Luxembourg, fiche de retenue, RTS, retenue d'impôt salaires, CCSS cotisations 2026, MDE classe, salaire social minimum 2026. Out of scope: luxembourg-income-tax, luxembourg-social-contributions, lu-cross-border, lu-corporate-tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/luxembourg-payroll"
  jurisdiction: "LU"
  tax_year: "2026"
  last_updated: "2026-10-27"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Luxembourg payroll: wage withholding and CCSS contributions (2026) v0.3

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to run a payroll, file or pay without review by a qualified professional in Luxembourg.

What matters for 2026:

- **Pension contribution is 8.5% for the employee and 8.5% for the employer** (17% in total, up from 16% in 2025). Source: CCSS notice to employers of 16 January 2026.
- **Accident insurance base rate fell to 0.65%** (from 0.70%), and the Mutualité des employeurs classes are now 0.23% / 0.95% / 1.56% / 2.66%.
- **Two parameter sets in 2026.** From 1 January: social minimum wage (SSM) EUR 2,703.74, ceiling EUR 13,518.68. From 1 June (index 992.24): SSM EUR 2,771.33, ceiling EUR 13,856.63.
- **The tax scale did not change.** The art. 118 LIR scale first applied for 2025 still applies in 2026, and so do the withholding scales built on it (grand-ducal regulation of 20 December 2024, Mémorial A 590).
- **CI-CO2 for employees rose to EUR 216 a year** (EUR 192 in 2025), by the budget law of 19 December 2025 (art. 154quater LIR).

This skill covers what the employer computes and pays each month. For the employee's annual tax computation, classes and deductions use `luxembourg-income-tax`. For the full contribution rules (self-employed, voluntary insurance, non-periodic pay) use `luxembourg-social-contributions`. For frontier workers, non-resident classes and the impatriate regime use `lu-cross-border`.

## Who this applies to

- **Employers** paying salaries for work done under an employment contract (art. 95 LIR). The employer must withhold income tax at each payment (art. 136(1) and (3) LIR) and is personally liable for tax withheld and for tax it should have withheld (art. 136(4) LIR).
- **Employees** whose pay Luxembourg has the right to tax, holding an electronic tax card (fiche de retenue d'impôt). Since 1 January 2022 the employee no longer hands the card to the employer; the ACD makes it available electronically (Guichet.lu).
- **No valid card:** the employer must withhold as for class 1, at a rate of at least 33% (Guichet.lu, retenue d'impôt).
- **Tax classes (art. 119 LIR):**
  - Class 1: anyone not in class 1a or class 2.
  - Class 1a: widowed persons, persons who get the child tax reduction, and persons who had completed their 64th year at the start of the tax year, unless they are in class 2.
  - Class 2: spouses or partners taxed jointly (arts. 3 and 3bis), and people widowed, divorced or separated in the three preceding years (with conditions).
- **Out of this skill:** household employers taxed at the 10% flat rate (art. 137(5) LIR), temporary agency workers on EUR 25 an hour or less (7.5% flat rate, art. 137(5a)), the self-employed, and non-resident classes (art. 157bis, see `lu-cross-border`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income tax scale | 23 bands: 0% to EUR 13,230, then 8% rising to 42% above EUR 234,870 | 2025 and 2026 | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf (art. 118) |
| Class 1a | Scale on income reduced by a quarter of its shortfall to EUR 79,380 | 2026 | LIR art. 120bis, same URL |
| Class 2 | Twice the tax on half the income (splitting) | 2026 | LIR art. 121, same URL |
| Monthly withholding, class 1 | 0% to EUR 1,185 a month; 39% band from EUR 4,595 to 9,870 (formula 0.39 x R - 1,052.775); 42% from EUR 19,660 | 2025 and 2026 | https://legilux.public.lu/eli/etat/leg/rgd/2024/12/20/a590/jo (annex, calcul automatisé) |
| Monthly withholding, class 1a | 0% to EUR 2,290 a month; 10% from EUR 2,295; 39% band from EUR 4,405 to 9,870 (formula 0.39 x R - 1,246.23); 42% from EUR 19,660; above R of EUR 12,585 add I x 0.09 - 73.78 instead of 7% | 2025 and 2026 | same URL |
| Monthly withholding, class 2 | 0% to EUR 2,290 a month; 20% band from EUR 5,280 to 5,655 (formula 0.20 x R - 687.65); 42% from EUR 39,235 | 2025 and 2026 | same URL |
| Employment fund surcharge | 7% of the tax; 9% above adjusted taxable income of EUR 150,000 (classes 1, 1a) or EUR 300,000 (class 2) | since 2013 | https://impotsdirects.public.lu/fr/az/f/fond_empl.html |
| Surcharge in the monthly scale | 7% up to monthly R of EUR 12,585 (classes 1 and 1a) or EUR 25,085 (class 2); above that, add I x 0.09 - 77.65 (class 1) or I x 0.09 - 155.30 (class 2) | 2025 and 2026 | https://legilux.public.lu/eli/etat/leg/rgd/2024/12/20/a590/jo (annex, calcul automatisé) |
| No valid tax card | Class 1, at least 33% | 2026 | https://guichet.public.lu/fr/entreprises/ressources-humaines/remuneration/fiche-retenue-impot/retenue-impot.html |
| Lump-sum deductions built into the scale | Expenses EUR 540 a year (art. 107); special expenses EUR 480 a year (art. 113); one twelfth each month (art. 138(2)) | 2026 | LIR, same URL as above |
| CIS (employee tax credit) | EUR 600 a year on gross EUR 11,266 to 40,000; then 600 - (gross - 40,000) x 0.015; nil from EUR 80,000 | 2026 | LIR art. 154quater |
| CI-CO2 for employees | EUR 216 a year up to gross EUR 40,000; then 216 - (gross - 40,000) x 0.0054; nil from EUR 80,000 (EUR 192 and 0.0048 in 2025) | 2026 | LIR art. 154quater; https://impotsdirects.public.lu/fr/az/c/credit-impot-salaries/cis2026.html |
| CIM (single-parent credit, class 1a by art. 119 no. 2 b, on request, paid through payroll) | EUR 3,504 a year below adjusted taxable income of EUR 60,000; 3,504 - (income - 60,000) x 0.0612 up to EUR 105,000; EUR 750 above; reduced by 50% of allowances the child receives above EUR 2,712 a year (family benefits and orphan pensions excluded) | 2026 | LIR art. 154ter |
| CISSM (minimum wage credit) | EUR 81 a month on monthly gross EUR 1,800 to 3,000; 81 / 600 x (3,600 - gross) from 3,000 to 3,600; nil from 3,600 | 2026 | LIR art. 139quater |
| Pension | 8.50% employee, 8.50% employer | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Pension, State share | The State pays one third of pension contributions (art. 239 CSS); the global rate is 25.5% for 2026 to 2032 (art. 238 CSS), so the State pays 8.50% on top. Not an employer cost | 2026 | https://legilux.public.lu/eli/etat/leg/code/securite_sociale/20260101 |
| Sickness, benefits in kind | 2.80% employee, 2.80% employer | 2026 | same URL |
| Sickness, cash benefit surcharge | 0.25% employee, 0.25% employer (only insured persons entitled to cash sickness benefit) | 2026 | same URL |
| Dependency insurance | 1.40%, employee only, on pay less a quarter of the SSM; no minimum or ceiling | 2026 | same URL |
| Dependency abatement | EUR 675.93 a month (1 January 2026); EUR 692.83 from 1 June 2026 | 2026 | same URL (1 January); https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf (1 June) |
| Accident insurance | 0.65% employer only at bonus-malus factor 1.00 (0.5525% at 0.85 up to 0.975% at 1.50) | 2026 | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf |
| Mutualité des employeurs (MDE) | Class 1 0.23%, class 2 0.95%, class 3 1.56%, class 4 2.66% (employer only, by financial absenteeism rate) | 2026 | same URL |
| Occupational health (STM) | 0.14%, private employers using the multi-sector service | 2026 | same URL |
| Family benefits | 1.70%, public sector employers only | 2026 | same URL |
| SSM, unskilled, 18 and over | EUR 2,703.74 a month (1 January 2026); EUR 2,771.33 from 1 June 2026 | 2026 | https://ccss.public.lu/fr/parametres-sociaux.html |
| Contribution minimum | Equal to the SSM; 80% at 17 to 18 and 75% at 15 to 17: EUR 2,162.99 and EUR 2,027.80 from 1 January 2026, EUR 2,217.06 and EUR 2,078.49 from 1 June 2026 | 2026 | CCSS notices of 16 January and 14 August 2026 |
| Contribution ceiling (5 x SSM) | EUR 13,518.68 a month (1 January 2026); EUR 13,856.63 from 1 June 2026 | 2026 | https://ccss.public.lu/fr/parametres-sociaux.html; https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf |

The ceiling from 1 June 2026 is **EUR 13,856.63**. The CCSS computes it as five times the unrounded SSM (279.30 x 9.9224 x 5). Five times the rounded SSM gives EUR 13,856.65, which is not the CCSS figure. The same pattern holds in January: 5 x 2,703.74 = 13,518.70, but the CCSS publishes 13,518.68.

## The taxable base

**Contributions base.** Pension, sickness, accident, MDE, occupational health and family benefits are charged on gross pay, but not below the minimum and not above the ceiling for the month. Dependency is charged on gross pay less the abatement, with no minimum or ceiling. If the employee works fewer than 150 hours in the month for that employer, the abatement is prorated on hours declared over 173 (CCSS notice, note 2).

**Withholding base, step by step.**

1. Start from gross pay for the month, including benefits in kind.
2. Deduct the employee's pension and sickness contributions (including the 0.25% cash surcharge), exempt pay, and the employee's own contributions to a supplementary pension scheme (regulation of 20 December 2024, art. 3(1)). Art. 110 no. 1 LIR makes only sickness and pension contributions deductible, so the **dependency contribution is not deducted**. The result is the semi-net pay.
3. Deduct the deduction shown on the tax card (art. 139 LIR; regulation of 20 December 2024, art. 3(1) no. 3).
4. Round down to a multiple of EUR 5. This is R. The monthly scale in Mémorial A 590 is set on monthly pay "arrondi au multiple inférieur de 5 EUR".
5. Apply the monthly formula for the class: rate x R minus the deduction for the band. Round down to 10 cents. This is I.
6. Add the employment fund surcharge: I x 1.07 up to the monthly threshold, else I + (I x 0.09 - 77.65) in class 1. Round down to 10 cents (regulation of 20 December 2024, art. 3(4), and its annex).
7. Subtract the monthly CIS and CI-CO2 (annual amount / 12, rounded up to the cent, art. 154quater(2) LIR), the CISSM where due, and the CIM where the card carries it. The employer pays these to the employee through payroll and offsets them against tax withheld; if the credits exceed the tax, the employer pays the excess to the employee (arts. 139quater, 154ter and 154quater LIR; regulation of 20 December 2024, art. 3(5) and (6)).

The monthly scale already includes one twelfth of the EUR 540 and EUR 480 lump sums (art. 138(2) LIR), so do not deduct them again.

**CIS on monthly pay.** The ACD's current worked example applies the CIS and CI-CO2 bands to monthly gross x 12 and pays one twelfth each month (gross EUR 3,500: CIS EUR 47.50 a month). The law also sets the monthly cut-offs directly: no CIS or CI-CO2 below EUR 78 or from EUR 6,667 a month (art. 154quater(2) LIR).

**Non-periodic pay (bonus, 13th month).** Do not run it through the monthly formula.

1. Take the bonus less the employee's pension and sickness contributions charged on it. Round down to a multiple of EUR 5 if it relates to a monthly pay period (EUR 50 for a yearly period, EUR 0.20 for a daily one) (regulation of 20 December 2024, art. 3(3)).
2. If annual ordinary pay is EUR 60,000 or less and the bonus is under EUR 5,600: withholding = bonus x the percentage in the table "Taux de la retenue sur les rémunérations non périodiques" in Mémorial A 590, read at the employee's class and the ordinary-pay step at or below the employee's pay (regulation, arts. 1(1) no. 3 and 2(2)).
3. Otherwise (annual ordinary pay over EUR 60,000, or a bonus of EUR 5,600 or more): withholding = tax from the annual wage scale on (annual ordinary pay + bonus) minus tax from the same scale on annual ordinary pay alone (art. 141(1) LIR; regulation, art. 2(2)). The annual wage scale already includes the employment fund surcharge (regulation, art. 1(2)). Annual ordinary pay is the current ordinary pay converted to a year (art. 141(3) LIR), less the full annual deduction on the tax card (regulation, art. 3(3)).
4. Round the withholding down to EUR 0.10 for a monthly period (regulation, art. 3(4)).

Non-periodic pay up to EUR 3,000 a year in total is left out of the gross that sets the CISSM (art. 139quater(2) LIR). Extraordinary pay under art. 132 LIR (for example severance above the exempt amount) has its own rules in art. 141(2) and is outside this skill.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Employer registration with the CCSS | Within 8 days of the first employee starting | Guichet.lu, déclaration d'entrée |
| Declaration of entry (each new employee) | Within 8 days of the start | Guichet.lu, déclaration d'entrée |
| Declaration of exit (each leaver) | Within 8 days of the end of the contract; the exit date is the last day of the working relationship or of the legal notice period | CCSS, engager du personnel |
| Monthly pay and hours declaration to the CCSS | Each month, for the previous month | CCSS, rémunération |
| CCSS account statement | Issued two months after the month charged (March contributions on the May statement); pay within 10 days of issue | CCSS, facturation |
| Withholding declaration and payment (MyGuichet.lu) | Monthly withholding of EUR 750 or more: by the 10th of the next month. EUR 75 to 750: quarterly, by the 10th after the quarter. Under EUR 75: yearly, by 10 January | Guichet.lu, retenue d'impôt |
| Electronic salary statements (extraits de compte salaire) | Before 1 March of the following year (2026 pay: before 1 March 2027) | Guichet.lu, extrait de compte salaire |

## Penalties and interest

- **Late CCSS payment:** default interest of 0.6% per full calendar month, from the first day of the month after the due date. Parts of a month are ignored (CCSS, facturation).
- **Unpaid CCSS statements:** after 4 unpaid monthly statements, the CCSS starts forced recovery (CCSS, facturation).
- **Late declaration of entry:** past the 30-day tolerance, a fine of EUR 50 per month late, up to EUR 2,500 (Guichet.lu).
- **Late withholding declaration:** the tax office can add a supplement of up to 10% of the tax and set a periodic penalty (astreinte) against the taxpayer or the person liable for the tax (ACD, prélèvements supplémentaires).
- **Late payment of tax:** interest of 0.6% per month at the full rate (ACD, prélèvements supplémentaires).
- **Wrong withholding:** the employer is personally liable for tax it withheld and tax it should have withheld (art. 136(4) LIR).

## Cross-border points

- Non-residents (including frontier workers from France, Belgium and Germany) get a non-resident tax card. The withholding method is the same, but the class follows art. 157bis LIR and the art. 157ter option. See `lu-cross-border`.
- Days worked abroad can move part of the pay out of Luxembourg tax under a treaty. Apply what the tax card shows and see `lu-cross-border` for the day thresholds.
- Social security follows EU Regulation 883/2004. A person who works 25% or more in the state of residence can fall under that state's system; the telework framework agreement raises the limit for telework to under 50%. With an A1 for another state, do not charge CCSS contributions. See `lu-cross-border` and `luxembourg-social-contributions`.
- Impatriates: the art. 115 no. 13b exemption changes the taxable base. See `lu-cross-border`.

## Worked examples

Both examples use July 2026 pay, so the 1 June 2026 parameters apply: ceiling EUR 13,856.63 (not reached) and dependency abatement EUR 692.83. The employer is in the private sector, uses the STM, has accident factor 1.00 (0.65%) and MDE class 2 (0.95%). The employee works full time, has no extra card deductions and no benefits in kind.

### Example 1: class 1 employee on EUR 6,000 a month

**Contributions.** Pension 8.5% = 510.00. Sickness 2.8% = 168.00. Cash surcharge 0.25% = 15.00. Dependency 1.4% x (6,000 - 692.83) = 1.4% x 5,307.17 = 74.30. Employee contributions: 767.30.

**Withholding.** Semi-net = 6,000 - 510 - 168 - 15 = 5,307.00. Rounded down to EUR 5: R = 5,305. Class 1, 39% band: 0.39 x 5,305 - 1,052.775 = 1,016.175, rounded down to 10 cents = 1,016.10. R is under EUR 12,585, so the surcharge is 7%: 1,016.10 x 1.07 = 1,087.227, rounded down to 1,087.20. The printed monthly scale in Mémorial A 590 shows the same figure at EUR 5,305 (class 1: 1,087.2).

**Credits.** Presumed annual gross = 72,000. CIS = 600 - (72,000 - 40,000) x 0.015 = 120 a year, 10.00 a month. CI-CO2 = 216 - 32,000 x 0.0054 = 43.20 a year, 3.60 a month. No CISSM (gross is over EUR 3,600). Net withholding = 1,087.20 - 13.60 = 1,073.60.

**Net pay** = 6,000 - 767.30 - 1,073.60 = **EUR 4,159.10**.

**Employer cost.** Pension 510.00 + sickness 168.00 + cash surcharge 15.00 + accident 39.00 + occupational health 8.40 + MDE 57.00 = 797.40. Total cost = **EUR 6,797.40**.

```oa-check
name: LU class 1, EUR 6,000 a month, July 2026
inputs:
  gross: 6000
  abatement: 692.83
  ceiling: 13856.63
steps:
  - base: min(gross, ceiling)
  - pension_ee: base * 0.085
  - sick_ee: base * 0.028
  - cash_ee: base * 0.0025
  - dependency: round((gross - abatement) * 0.014, 2)
  - ee_contrib: pension_ee + sick_ee + cash_ee + dependency
  - semi_net: gross - pension_ee - sick_ee - cash_ee
  - r: floor(semi_net / 5) * 5
  - tax_raw: floor((0.39 * r - 1052.775) * 10) / 10
  - tax_surcharged: floor(tax_raw * 1.07 * 10) / 10
  - cis_month: ceil((600 - (gross * 12 - 40000) * 0.015) / 12 * 100) / 100
  - co2_month: ceil((216 - (gross * 12 - 40000) * 0.0054) / 12 * 100) / 100
  - withholding: tax_surcharged - cis_month - co2_month
  - net_pay: gross - ee_contrib - withholding
  - er_contrib: base * 0.085 + base * 0.028 + base * 0.0025 + base * 0.0065 + base * 0.0014 + base * 0.0095
  - employer_cost: gross + er_contrib
expected:
  ee_contrib: 767.30
  r: 5305
  tax_surcharged: 1087.20
  withholding: 1073.60
  net_pay: 4159.10
  er_contrib: 797.40
  employer_cost: 6797.40
```

### Example 2: class 2 employee on the same pay

Contributions do not depend on the tax class, so they are the same: 767.30 for the employee and 797.40 for the employer. The semi-net and R are also the same: R = 5,305.

**Withholding.** Class 2, 20% band (EUR 5,280 to 5,655): 0.20 x 5,305 - 687.65 = 373.35, rounded down to 10 cents = 373.30. R is under EUR 25,085, so the surcharge is 7%: 373.30 x 1.07 = 399.431, rounded down to 399.40 (the printed scale at EUR 5,305 shows 399.4 for class 2). CIS and CI-CO2 are the same as in Example 1 (13.60). Net withholding = 399.40 - 13.60 = 385.80.

**Net pay** = 6,000 - 767.30 - 385.80 = **EUR 4,846.90**. Class 2 leaves the employee EUR 687.80 a month better off than class 1 on the same gross. Employer cost is unchanged at EUR 6,797.40.

The edge case: when both spouses taxed jointly earn salaries, art. 137(2)(b) LIR leaves the withholding on the second salary to a grand-ducal regulation, and the tax card shows the result. Use the card; never apply the full class 2 table to both jobs.

```oa-check
name: LU class 2, EUR 6,000 a month, July 2026
inputs:
  gross: 6000
  abatement: 692.83
steps:
  - pension_ee: gross * 0.085
  - sick_ee: gross * 0.028
  - cash_ee: gross * 0.0025
  - dependency: round((gross - abatement) * 0.014, 2)
  - ee_contrib: pension_ee + sick_ee + cash_ee + dependency
  - r: floor((gross - pension_ee - sick_ee - cash_ee) / 5) * 5
  - tax_raw: floor((0.20 * r - 687.65) * 10) / 10
  - tax_surcharged: floor(tax_raw * 1.07 * 10) / 10
  - credits: 10.00 + 3.60
  - withholding: tax_surcharged - credits
  - net_pay: gross - ee_contrib - withholding
  - gain_vs_class_1: net_pay - 4159.10
expected:
  tax_raw: 373.30
  tax_surcharged: 399.40
  withholding: 385.80
  net_pay: 4846.90
  gain_vs_class_1: 687.80
```

## Ask the client first

1. What does the employee's electronic tax card show: class, any tax rate, extra deductions, and the CIS entry? No card means class 1 at 33% or more.
2. Which pay month? Before 1 June 2026 use SSM 2,703.74, ceiling 13,518.68 and abatement 675.93; from 1 June use 2,771.33, 13,856.63 and 692.83.
3. Which MDE class and accident bonus-malus factor has the employer been notified? Is it public or private sector, and does it use the STM?
4. Does the employee live outside Luxembourg, work days abroad, or hold an A1 for another state?
5. Is there pay beyond basic salary: bonus, 13th month, benefits in kind, a company car?
6. Does the employee work full time? Part-time pay changes the CISSM and the dependency abatement.

## Sources

| Source | URL | Read on |
|---|---|---|
| LIR, consolidated text in force on 1 January 2026 (ACD): arts. 107, 110, 113, 118 to 121, 136 to 139quater, 154ter, 154quater | https://impotsdirects.public.lu/dam-assets/fr/legislation/LIR/texte-coordonn-en-vigueur-au-1er-janvier-2026-ver-08052026.pdf | 2026-10-23 |
| Règlement grand-ducal of 20 December 2024 publishing the withholding scales (Mémorial A 590 of 24 December 2024): arts. 1 to 4, monthly scale, non-periodic pay rates, automated-calculation formulas; applies from tax year 2025, in force | https://legilux.public.lu/eli/etat/leg/rgd/2024/12/20/a590/jo | 2026-10-23 |
| ACD, barèmes de l'impôt (no newer scale than 2025 published) | https://impotsdirects.public.lu/fr/baremes.html | 2026-10-23 |
| ACD, formulas for automated computation, 2025 scales (informational copy of the Mémorial annex) | https://impotsdirects.public.lu/dam-assets/fr/baremes/bareme-2025-format-excel.xlsx | 2026-10-23 |
| ACD, calcul d'une rémunération mensuelle nette (worked example at 1 January 2025: EUR 5 rounding, CIS on monthly gross x 12) | https://impotsdirects.public.lu/fr/salpens/calcul_rem.html | 2026-10-23 |
| ACD, CIS and CI-CO2 from tax year 2026 | https://impotsdirects.public.lu/fr/az/c/credit-impot-salaries/cis2026.html | 2026-10-23 |
| ACD, fonds pour l'emploi | https://impotsdirects.public.lu/fr/az/f/fond_empl.html | 2026-10-23 |
| ACD, prélèvements supplémentaires (late filing supplement, interest) | https://impotsdirects.public.lu/fr/az/p/prelev.html | 2026-10-23 |
| CCSS, avis aux employeurs, taux de cotisation au 01.01.2026 (16 January 2026) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf | 2026-10-23 |
| CCSS, avis aux employeurs, minima et maximum cotisables au 01.06.2026 (14 August 2026; dependency abatement EUR 692.83) | https://ccss.public.lu/dam-assets/publications/2026/ccss-20260814-avis-80-99.pdf | 2026-10-23 |
| CCSS, paramètres sociaux (rates 2014 to 2026; SSM, minimum and ceiling from 1 June 2026) | https://ccss.public.lu/fr/parametres-sociaux.html | 2026-10-23 |
| CCSS, facturation (statement, 10 days, 0.6% interest) | https://ccss.public.lu/fr/employeurs/secteur-prive/facturation.html | 2026-10-23 |
| CCSS, engager du personnel (declaration of exit within 8 days) | https://ccss.public.lu/fr/employeurs/secteur-prive/engager-personnel.html | 2026-10-27 |
| Code de la sécurité sociale, arts. 238 and 239 (pension financing, State share) | https://legilux.public.lu/eli/etat/leg/code/securite_sociale/20260101 | 2026-10-27 |
| CCSS, rémunération (monthly declaration of pay and hours) | https://ccss.public.lu/fr/employeurs/secteur-prive/remuneration.html | 2026-10-23 |
| Guichet.lu, retenue d'impôt sur les salaires | https://guichet.public.lu/fr/entreprises/ressources-humaines/remuneration/fiche-retenue-impot/retenue-impot.html | 2026-10-23 |
| Guichet.lu, extrait de compte salaire ou pension | https://guichet.public.lu/fr/entreprises/ressources-humaines/remuneration/fiche-retenue-impot/extrait-compte-salaire-pension.html | 2026-10-23 |
| Guichet.lu, déclaration d'entrée | https://guichet.public.lu/fr/entreprises/ressources-humaines/securite-sociale/declaration-entree.html | 2026-10-23 |

Not yet confirmed: the monthly social minimum wage for skilled workers (qualifié, SSM plus 20%) from 1 January and 1 June 2026; the CCSS notices and parameters page publish only the unskilled SSM, and no official 2026 figure for the skilled rate was found. Also whether the 0.6% monthly late-payment interest on the ACD page applies to late withholding payments in the same way as to assessed tax (the page speaks of tax due on an assessment).

> Contributed by Ryan Duguid.

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `luxembourg-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/luxembourg-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
