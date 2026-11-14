---
name: la-payroll-social
description: "Lao PDR payroll, tax year 2026: social security 6% employer and 5.5% employee on insurable earnings between the minimum wage and the ceiling (Social Security Law No. 54/NA), monthly remittance and 30-day registration; salary income tax 0% to 25% monthly scale, minimum-wage exemption and withholding by the 20th of the next month (revised Law on Income Tax, 2025)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/la-payroll-social"
  jurisdiction: "LA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Laos payroll and social contributions

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to run payroll without professional review.

## Who this applies to

Enterprises with employees in Lao PDR. Social security is run by the Lao Social Security Organisation (LSSO) under the revised Social Security Law No. 54/NA of 27 June 2018 (LSSO register date 1 May 2019) and Instruction No. 0060/MLSW of 11 January 2023, in force from 1 May 2023 (Notice No. 1356), which replaced Instruction No. 1206/MLSW. An enterprise with at least one employee registers with the LSSO, including covered foreign employees (arts 90 to 92). Salary income tax is under the Law on Income Tax (Revised), promulgated 6 August 2025 and published in the Official Gazette on 19 June 2026 (art. 74 names 1 September 2025; check which rules govern pay periods between the two dates).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Social security, employer (art. 74(2.1)) | 6% of monthly insurable earnings | 2026 | https://lsso.gov.la/Legislation/nssf%20law%2054%20en.pdf |
| Social security, employee (art. 74(2.2)) | 5.5% of monthly insurable earnings | 2026 | https://lsso.gov.la/Legislation/nssf%20law%2054%20en.pdf |
| Social security, voluntary insured person (art. 74(2.3)) | 9% of the selected insurable earnings | 2026 | https://lsso.gov.la/Legislation/nssf%20law%2054%20en.pdf |
| Cash payment at the LSSO allowed (art. 75(2.3)) | If not over five million kips | 2026 | https://lsso.gov.la/Legislation/nssf%20law%2054%20en.pdf |

Salary income tax, monthly scale (art. 38(1)), in kip:

| Band | Monthly income | Rate | Tax on the band | Cumulative | Official URL |
|---|---|---|---|---|---|
| 1 | up to 2,500,000 | 0% | 0 | 0 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| 2 | over 2,500,000 to 5,000,000 | 5% | 125,000 | 125,000 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| 3 | over 5,000,000 to 15,000,000 | 10% | 1,000,000 | 1,125,000 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| 4 | over 15,000,000 to 25,000,000 | 15% | 1,500,000 | 2,625,000 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| 5 | over 25,000,000 to 65,000,000 | 20% | 8,000,000 | 10,625,000 | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |
| 6 | over 65,000,000 | 25% | | | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf |

The sentence under the table says the band amounts will be adjusted in line with the government minimum wage from time to time; the rates are fixed by the Law, the kip amounts are not.

## The base

- **Social security.** Insurable earnings are basic salary, output-based pay, overtime and other wages declared for income tax; daily or weekly pay is summed for the month (art. 74). The floor is the government minimum wage for the period; the ceiling is set separately on economic and actuarial grounds (art. 77). The LAK 4,500,000 ceiling came from Decision No. 1740/MLSW and Notice No. 0824, effective 1 January 2017 under the previous law; no current figure was found, so confirm the ceiling with the LSSO for the month before capping.
- **Income tax.** Salary, wages, overtime, allowances, bonuses, meeting fees and other benefits in cash or in kind (art. 33(1)). Salary and other income up to the government minimum wage is exempt (art. 34(1)); so are salaries of diplomatic and international-organisation staff and foreign experts under an agreement (art. 34(2)).

## Deadlines and filing

- **Social security.** Each month the employer prepares the payroll, calculates its 6%, deducts the employee's 5.5%, pays both to the LSSO account at a bank and files a detailed contribution list (art. 75(2.1)). The Law sets monthly payment without a day; the 15th of the following month in Instruction No. 0060 item 13 is for voluntary contributors. Register employees within 30 days of signing the employment contract (Notice No. 3185 of 16 September 2022).
- **Income tax.** Withhold and declare to the tax office no later than the 20th of the following month, and give the employee a withholding certificate on the Tax Department form, certified by a tax officer (art. 39). Non-domiciled staff: same scale (art. 48(1)) but declare and remit within fifteen days of paying (art. 49). Annual reconciliation on a scale twelve times the monthly one (art. 50).

## Penalties and interest

Not read for this guide (Social Security Law and Tax Administration Law).

## Cross-border points

Covered foreign employees are registered with the LSSO. Non-domiciled employees pay the same salary scale with a 15-day remittance clock. Foreign experts under an agreement are exempt from salary tax (art. 34(2)).

## Two worked examples that recompute

**1. Employee earning LAK 4,000,000 a month (assumed between the floor and the ceiling).** Employer 6% = LAK 240,000; employee 5.5% = LAK 220,000 (derived).

```oa-check
name: Laos social security 4000000
inputs:
  pay: 4000000
steps:
  - employer: pay * 0.06
  - employee: pay * 0.055
expected:
  employer: 240000
  employee: 220000
```

**2. Monthly salary income tax on LAK 10,000,000.** Bands 1 and 2 give LAK 125,000; band 3 taxes 5,000,000 at 10% = LAK 500,000; total LAK 625,000 due by the 20th of the next month (derived).

```oa-check
name: Laos salary tax 10000000
inputs:
  pay: 10000000
steps:
  - tax: 125000 + (min(pay, 15000000) - 5000000) * 0.10
expected:
  tax: 625000
```

## Ask the client first

- Monthly pay of each employee and what it includes?
- Is the employee Lao-domiciled, foreign, or an expert under an agreement?
- Current minimum wage and LSSO ceiling for the month?
- Is the enterprise and each employee registered with the LSSO?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Law No. 54/NA, LSSO English version, arts 74, 75 and 77 (Read for the rates, remittance and ceiling rule) | https://lsso.gov.la/Legislation/nssf%20law%2054%20en.pdf | 2026-11-14 |
| Law on Income Tax (Revised), Lao Official Gazette scan, arts 33, 34, 38 and 39 on printed pages 15, 18 and 19 (Read as rendered pages for the scale, exemption and 20th) | https://laoofficialgazette.gov.la/kcfinder/upload/files/88-25-6-2025_0001.pdf | 2026-11-14 |
| Instruction No. 0060/MLSW, item 13 (Read by Ryan Duguid for the voluntary 15th) | https://www.lsso.gov.la/Legislation/knn_new0060.pdf | 2026-11-11 |
| Notice No. 0824 and Decision No. 1740 (Read by Ryan Duguid for the 2017 ceiling) | https://www.lsso.gov.la/images/stories/Notices/notices_phadan_4500000.pdf | 2026-11-11 |
| Notice No. 3185 of 16 September 2022 (Read by Ryan Duguid for 30-day registration) | https://www.lsso.gov.la/images/stories/Notices/notices_regis.pdf | 2026-11-11 |

Not yet confirmed: the insurable earnings ceiling and minimum wage for 2026 (the old guide's LAK 4,500,000 ceiling and maximum contributions of LAK 270,000 and LAK 247,500 date from 2017); the enterprise payment day; which income tax rules govern pay before 19 June 2026; art. 48 to 50 text as Ryan Duguid read it (pages not reopened here); penalties.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `la-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/la-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
