---
name: aw-social-contributions
description: "Aruba social contributions for tax year 2026. Covers the AOV and AWW premiums (15.5% in total, 10.5% employer and 5% employee) and the AZV health premium (10.5% in total, 8.9% employer and 1.6% employee) up to the Afl. 85,000 premium-income ceiling, the premium-income base after costs, pension and savings fund, the self-employed rate, the 2026 pensioner AZV relief (0% on the first Afl. 30,000), the employer-only ZV (2.65%) and OV (0.25% to 2.5%) with the Afl. 5,850 monthly wage threshold, cessantia of Afl. 40, and the monthly return and payment to DIMP by the 15th. Trigger phrases include Aruba social security, AOV AWW Aruba, AZV premium, SVB Aruba, premiegrens Aruba, cessantia Aruba."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/aw-social-contributions"
  jurisdiction: "AW"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Aruba social contributions: 2026 v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. The SVB (Sociale Verzekeringsbank Aruba) runs AOV and AWW; the Uitvoeringsorgaan AZV runs AZV; DIMP levies and collects the AOV/AWW and AZV premiums with wage tax ([DIMP, Premies volksverzekering](https://www.impuesto.aw/premies-volksverzekering)). Amounts in Aruban florins (Afl.).

## Who this applies to

- **Employers** withhold the employee share of AOV/AWW and AZV and pay both shares to DIMP with wage tax ([DIMP, Premies volksverzekering](https://www.impuesto.aw/premies-volksverzekering)).
- **Self-employed people without staff** pay premiums through their income tax ([DIMP, Loonbelasting en Premies](https://www.impuesto.aw/loonbelasting-en-premies)).
- **Pensioners** aged 65 or over (AOV pension age) have a lower AZV rate on the first Afl. 30,000 from 2026 ([DIMP, Premiegrenzen AZV](https://www.impuesto.aw/premiegrenzen-azv)).
- **Employer-only schemes** ZV, OV and cessantia are SVB matters ([SVB, Summary of tariffs 2026](https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en)).
- Not covered: benefit claims, coverage exemptions for individual workers, wage tax itself (`aw-individual-income-tax`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| AOV and AWW combined | 15.5%: employer 10.5%, employee 5% | Up to premium income of Afl. 85,000 | 2026 | [SVB, Summary of tariffs 2026](https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en) |
| AOV alone | 14.5%: employer 10%, employee 4.5% | Part of the 15.5% | 2026 | same |
| AWW alone | 1%: employer 0.5%, employee 0.5% | Part of the 15.5% | 2026 | same |
| AOV/AWW maximum premium | Afl. 13,175 (employer 8,925, employee 4,250); self-employed 13,175 | Premium ceiling Afl. 85,000, unchanged since 2015 | 2026 | [DIMP, Premiegrenzen AOV/AWW](https://www.impuesto.aw/premiegrenzen-aovaww) |
| AZV | 10.5%: employer 8.9%, employee 1.6% | Up to premium income of Afl. 85,000 | 2026 | [DIMP, Premiegrenzen AZV](https://www.impuesto.aw/premiegrenzen-azv) |
| AZV maximum premium | Afl. 8,925 (employer 7,565, employee 1,360); self-employed 10.5%, max 8,925 | | 2026 | same |
| AZV for pensioners 65 and over | 0% on the first Afl. 30,000, 10.5% above, to Afl. 85,000; max Afl. 5,775 | From 1 January 2026; in 2025 it was 5% on the first 30,000, max 7,275 | 2026 | same |
| ZV (sickness insurance) | 2.65% of gross salary, employer only | Income threshold below | 2026 | [SVB, Summary of tariffs 2026](https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en) |
| OV (accident insurance) | 0.25% to 2.5% of gross salary, employer only | By hazard class | 2026 | same |
| ZV/OV income threshold | Afl. 270 a day (5-day week), 225 a day (6-day week), 1,350 a week, 5,850 a month, 70,200 a year | | 2026 | same |
| Cessantia | Afl. 40 a year per employee employed on 1 January | Employer | 2026 | same |
| Premium-income deductions | costs 3%, max Afl. 1,500; employee pension contribution; savings and provision fund 5%, max Afl. 3,360 | Deducted from wage to reach premium income | 2026 | [DIMP, Premies volksverzekering](https://www.impuesto.aw/premies-volksverzekering) |

## The base

1. **Premium income** (premie-inkomen) is the wage less the 3% costs (max Afl. 1,500), the employee pension contribution and the total savings and provision fund contribution (5%, max Afl. 3,360). The same premium income is used for AOV/AWW and AZV ([DIMP, Premies volksverzekering](https://www.impuesto.aw/premies-volksverzekering)).
2. **Ceiling:** no premium above Afl. 85,000 premium income a year (same page; [DIMP, Premiegrenzen AZV](https://www.impuesto.aw/premiegrenzen-azv)).
3. **Wage** for premiums follows the wage tax concept: money, benefits in kind, entitlements and allowances ([DIMP, Waarover houdt u loonbelasting en premies in](https://www.impuesto.aw/waarover-houdt-u-loonbelasting-en-premies-in)).
4. **ZV and OV** are a percentage of gross salary. SVB lists an income threshold; whether it caps the premium or limits who is insured is not stated on the summary page ([SVB, Summary of tariffs 2026](https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en)).
5. **Pensioners:** the 0% applies to the first Afl. 30,000 of income or salary from former employment ([Government of Aruba, 8 January 2026](https://www.gobierno.aw/nl/vanaf-1-januari-2026-betalen-gepensioneerden-minder-azv-premies)).

## Deadlines and filing

- One monthly return covers wage tax and AOV/AWW and AZV premiums. File and pay by the 15th of the month after the period, or the first working day after if the 15th is a Saturday, Sunday or holiday. File even if no wage was paid; DIMP issues 12 returns a year ([DIMP, Wanneer moet u aangifte doen en betalen (loonbelasting)](https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen-0)).
- Returns are available in BOi early in the month; for example September 2026 returns opened on 2 October and were due on 15 October 2026 ([DIMP, Kalender oktober 2026](https://www.impuesto.aw/kalender-digitale-aangifte-oktober-2026)). DIMP lists 17 February, 16 March and 18 May 2026 as monthly deadlines ([DIMP, Deadlines](https://www.impuesto.aw/deadlines)).
- **Verzamelloonstaat** (annual summary per employee, including directors, supervisory directors, commission workers and interns): due 31 March, through BOi as manual entry or XML upload; from tax year 2025 the Excel file is no longer allowed. Late filing can bring a penalty and an additional assessment ([DIMP, Verzamelloonstaat](https://www.impuesto.aw/verzamelloonstaat-vzl)). The 2025 statement was due 31 March 2026 ([DIMP, Deadlines](https://www.impuesto.aw/deadlines)).

## Penalties and interest

Late or missing returns or payments can bring an additional assessment with a penalty ([DIMP, Wanneer moet u aangifte doen en betalen (loonbelasting)](https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen-0)). Unpaid assessments carry collection costs and collection interest ([DIMP, U betaalt deels niet of niet op tijd](https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd)). The penalty amounts for wage tax and premiums are not on the pages read.

## Cross-border points

- Coverage of foreign workers and workers insured abroad is not on the pages read: refer to the SVB.
- Non-resident pensioners and the AZV pensioner rate: check status with DIMP.

## Two worked examples that recompute

**Case 1: ordinary employee, premium income Afl. 60,000.** AOV/AWW: employee 5% = 3,000, employer 10.5% = 6,300. AZV: employee 1.6% = 960, employer 8.9% = 5,340. Withheld from the employee: 3,960; employer cost: 11,640; all paid to DIMP on the monthly returns. ZV at 2.65% and OV by hazard class are on top for the employer.

```oa-check
name: Aruba 2026 premiums, premium income 60000
inputs:
  premium_income: 60000
  ceiling: 85000
steps:
  - base: min(premium_income, ceiling)
  - aov_aww_employee: base * 0.05
  - aov_aww_employer: base * 0.105
  - azv_employee: base * 0.016
  - azv_employer: base * 0.089
  - employee_total: aov_aww_employee + azv_employee
  - employer_total: aov_aww_employer + azv_employer
expected:
  aov_aww_employee: 3000.00
  aov_aww_employer: 6300.00
  azv_employee: 960.00
  azv_employer: 5340.00
  employee_total: 3960.00
  employer_total: 11640.00
```

**Case 2: pensioner aged 67 with Afl. 56,000 of pension from former employment.** 2026: 0% on 30,000 plus 10.5% on 26,000 = 2,730 (the government's own example). Under the 2025 rule it would have been 5% of 30,000 + 10.5% of 26,000 = 4,230, so the change saves 1,500. Check that the employer or pension payer applies the 0% band; if it withholds at the ordinary rate, the employee and employer shares must be corrected.

```oa-check
name: Aruba pensioner AZV 2026 against 2025
inputs:
  income: 56000
  first_band: 30000
steps:
  - azv_2026: max(min(income, 85000) - first_band, 0) * 0.105
  - azv_2025: min(income, first_band) * 0.05 + max(min(income, 85000) - first_band, 0) * 0.105
  - saving: azv_2025 - azv_2026
expected:
  azv_2026: 2730.00
  azv_2025: 4230.00
  saving: 1500.00
```

## Ask the client first

1. Employee, self-employed, or pensioner aged 65 or over?
2. Gross wage, pension contribution and savings fund contribution (for premium income).
3. More than one employer or pension payer in the year?
4. The OV hazard class of the employer.
5. Is anyone insured abroad or exempt?

## Sources

| Source | URL | Read on |
|---|---|---|
| SVB Aruba, Summary of tariffs 2026: read for AOV, AWW, AZV, ZV and OV rates, the AOV/AWW ceiling, ZV/OV thresholds and cessantia | https://www.svbaruba.org/employer/summary-of-tariffs/summary-of-tariffs-2026/?lang=en | 2026-11-14 |
| DIMP, Premiegrenzen AZV: read for the 2026 and 2025 AZV ceilings, maxima and the pensioner rule | https://www.impuesto.aw/premiegrenzen-azv | 2026-11-14 |
| DIMP, Premiegrenzen AOV/AWW: read for the Afl. 85,000 ceiling and maximum premiums | https://www.impuesto.aw/premiegrenzen-aovaww | 2026-11-14 |
| Government of Aruba, pensioners pay less AZV from 1 January 2026 (8 January 2026): read for the 0% band and the Afl. 56,000 example | https://www.gobierno.aw/nl/vanaf-1-januari-2026-betalen-gepensioneerden-minder-azv-premies | 2026-11-14 |
| DIMP, Premies volksverzekering: read for who runs each scheme, premium income and its deductions | https://www.impuesto.aw/premies-volksverzekering | 2026-11-14 |
| DIMP, Loonbelasting en Premies: read for employer withholding and self-employed premiums | https://www.impuesto.aw/loonbelasting-en-premies | 2026-11-14 |
| DIMP, Waarover houdt u loonbelasting en premies in: read for the wage concept | https://www.impuesto.aw/waarover-houdt-u-loonbelasting-en-premies-in | 2026-11-14 |
| DIMP, Wanneer moet u aangifte doen en betalen (wage tax): read for the monthly period, the 15th and penalties in general | https://www.impuesto.aw/wanneer-moet-u-aangifte-doen-en-betalen-0 | 2026-11-14 |
| DIMP, Kalender digitale aangifte oktober 2026: read for the September 2026 return dates | https://www.impuesto.aw/kalender-digitale-aangifte-oktober-2026 | 2026-11-14 |
| DIMP, Deadlines: read for the listed 2026 deadlines and the 31 March 2026 verzamelloonstaat | https://www.impuesto.aw/deadlines | 2026-11-14 |
| DIMP, Verzamelloonstaat (VZL): read for the 31 March deadline, BOi filing and corrections | https://www.impuesto.aw/verzamelloonstaat-vzl | 2026-11-14 |
| DIMP, U betaalt deels niet of niet op tijd: read for collection costs and interest | https://www.impuesto.aw/u-betaalt-deels-niet-of-niet-op-tijd | 2026-11-14 |

Not yet confirmed: whether the ZV/OV threshold caps the premium or defines who is insured; SVB payment and filing for ZV, OV and cessantia; penalty amounts for late wage tax and premium returns; coverage rules for foreign workers.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `aw-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/aw-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
