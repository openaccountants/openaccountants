---
name: om-payroll-social
description: "Payroll and social contributions for Oman, tax year 2026: Social Protection Fund rates by branch and date, the statutory ceiling and its current-decision hold, payment by the 15th, non-Omani workers, late charges, from the law and the Fund."
version: 1.4
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Oman Payroll & Social Contributions v1.3

> **General reference only.** This Guide is a draft for AI-assisted reference. Independent review accepts only the documented partial source closeout and its recorded conditions. It has not received accountant attestation. Do not use it to file, pay or take a position without professional review.

## Who this applies to

Employers of Omani workers in Oman, Omani self-employed people, and employers of non-Omani workers for the branches that reach them. The Social Protection Fund runs the scheme under the Social Protection Law (RD 52/2023), in force from 1 January 2024 with staged branches (decree art. VI). No income tax is withheld from pay in 2026; see [income tax](om-income-tax.md).

## Rates, bands and thresholds

| Branch | Worker | Employer | Since | Official URL |
|---|---|---|---|---|
| Old age, disability and death | 7.5% | 11% | 1 Jan 2024 | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ |
| Work injury and occupational disease | 0% | 1% | 1 Jan 2024 | same |
| Employment security | 0.5% | 0.5% | 1 Jan 2024 | same |
| Sick and other leave | 0% | 1% | 19 Jul 2026: decree VI(3), replaced by RD 60/2025, gives three years after 19 July 2023; SPF Decision R/13/2026 extends the branch to listed non-Omani workers from the same date | https://www.nsg.gov.om/data/RD_No.60_2025_amending_No.52_2023_promulgating_the_Social_ProtectionLaw.pdf |
| Maternity leave | 0% | 1% | 2024 commencement: decree VI(4) gives one year after 19 July 2023; FAQ gives 1 July 2024. Historic start requires reconciliation | same |
| Total when all listed branches apply | 8% | 14.5% | From 19 Jul 2026; before that date the sick-leave 1% is not charged, so 13.5% employer (derived). Conditional calculation; not a universal 2026 payroll rate | same |
| Sick and other leave, non-Omani workers | 0% | 1% | 19 Jul 2026, compulsory for all non-Omani employees of state administrative units and other public legal persons, and non-Omani workers in private establishments under the Labour Law (Decision R/13/2026, arts 1 and 3, Official Gazette 1654) | https://www.mjla.gov.om/modules/decisions/download.php?file=2219 |

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Wage ceiling, old age and work injury branches | Statutory starting ceiling OMR 3,000 a month; Board can increase it. Current 2026 ceiling decision not recovered, so no live above-ceiling computation (art. 52) | statutory base, current-year hold | https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf |
| Non-Omani savings system | 9% of monthly basic wage (art. 139(1)), from a date set by the Board, no later than 4 years from 19 July 2023 (decree art. VI(5), replaced by RD 60/2025 art. I) | 2026 | same |
| Late or unpaid contributions | Additional 5.5% a year (art. 155) | 2026 | same |
| Income tax withholding on pay | None in 2026; starts 2028 | 2026 | https://tms.taxoman.gov.om/portal/documents/d/taxportal/-56_2025-1?download=true |

Art. 52 names only two branches for the ceiling, so the other three branches run on the full wage in the examples below.

## The base

Wage is gross salary or basic wage plus all allowances and stipends (art. 1(15)); contributions are calculated on the monthly wage, on a daily basis (arts 70, 90, 116, 123, 128). Employment-security excludes self-employed and part-time workers (art. 115); sick-leave and maternity exclude self-employed, part-time, GCC-working and overseas-working Omanis (arts 121, 127). The full five-branch illustration is for an ordinary covered Omani employee only. The regulation defines exempt categories and surplus handling (art. 52).

## Deadlines and filing

Contributions are paid within the first 15 days of the month after the one they cover. The employer pays both shares and deducts the worker's share from the wage (art. 58, https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf). Registration and upload screens are on the Fund's site, which refused most connections, so no portal how-to is given here.

## Penalties and interest

An employer that fails to register workers, understates wages, or pays late owes an additional 5.5% a year on the amounts due (art. 155), unless the Board's controls excuse it (https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf).

## Cross-border points

The old age branch is compulsory for Omanis working in Oman, and covers Omanis under the GCC extension systems (art. 68). Non-Omani workers: the work injury branch reaches them from 5 years after issue, so from 19 July 2028 under RD 60/2025 art. I, in the categories the Board decides (decree art. VI, art. 87). The sick leave branch reaches them by Board decision (art. 121); that decision is SPF Decision R/13/2026, which makes it compulsory from 19 July 2026 for all non-Omani employees of state administrative units and other public legal persons and for non-Omani workers in private establishments covered by the Labour Law (https://www.mjla.gov.om/modules/decisions/download.php?file=2219, arts 1 and 3). The savings system is compulsory for them at the art. 139(1) amount (art. 136); service before the start date stays under the Labour Law end-of-service rules (art. 138). Check the Board's decision before charging any of these.

## Two worked examples that recompute

**1. Conditional illustration: covered Omani worker on OMR 1,000 a month from 19 July 2026, all five branches applying.** Employer pays OMR 145; worker pays OMR 80.

```oa-check
name: Omani wage 1000
inputs:
  wage: 1000
steps:
  - employer: wage * (0.11 + 0.01 + 0.005 + 0.01 + 0.01)
  - worker: wage * (0.075 + 0.005)
expected:
  employer: 145
  worker: 80
```

**2. Preserved statutory illustration, nonoperative for live 2026 payroll until the current ceiling is recovered: covered Omani worker on OMR 4,000, assumed ceiling OMR 3,000, all five branches applying.** The assumed ceiling cuts the old age and injury shares. Employer pays OMR 460, worker OMR 245.

```oa-check
name: Omani wage 4000 with ceiling
inputs:
  wage: 4000
  ceiling: 3000
steps:
  - capped: min(wage, ceiling)
  - employer: capped * 0.12 + wage * 0.025
  - worker: capped * 0.075 + wage * 0.005
expected:
  employer: 460
  worker: 245
```

## Ask the client first

- Omani or non-Omani, and any GCC national?
- Monthly wage, and what it is made of?
- Contract type (temporary, training, part-time)?
- Date of joining?
- Any arrears or unregistered workers?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Protection Fund, contribution-rate FAQ answer checked in cached Fund FAQ HTML; conflicting commencement dates held | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ | 2026-11-01 |
| Social Protection Law, RD 52/2023, Fund-hosted English first edition 2024 (law arts 1, 5, 52, 58, 68, 70, 87, 90, 115, 116, 121, 123, 127, 128, 136, 138, 139 and 155 checked; RD 60/2025 commencement amendment separately read) | https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf | 2026-11-01 |
| RD 60/2025, art. I replacing decree VI(2), (3), (5), official gazette issue 1604 p. 9, complete page visually read | https://www.nsg.gov.om/data/RD_No.60_2025_amending_No.52_2023_promulgating_the_Social_ProtectionLaw.pdf | 2026-11-01 |
| Read for the sick-leave start date: RD 60/2025, Arabic gazette text, art. I(3) three years from the decree, art. III in force the day after publication | https://www.mjla.gov.om/modules/decrees/download.php?file=1345 | 2026-11-14 |
| Read for the non-Omani sick-leave categories: SPF Decision R/13/2026, Arabic gazette text, Official Gazette 1654, arts 1 and 3 (in force 19 July 2026) | https://www.mjla.gov.om/modules/decisions/download.php?file=2219 | 2026-11-14 |
| Personal Income Tax Law, RD 56/2025, official Tax Authority-hosted gazette issue 1602 pp. 7 to 31, all 25 PDF pages visually read | https://tms.taxoman.gov.om/portal/documents/d/taxportal/-56_2025-1?download=true | 2026-11-01 |

Not yet confirmed: NONOPERATIVE HOLD on current 2026 contribution ceiling decisions: do not apply the statutory starting ceiling as a verified live payroll instruction. Sick-leave start: the Fund FAQ's 1 July 2025 is superseded; RD 60/2025 gives 19 July 2026 and Decision R/13/2026 starts the non-Omani categories the same day. The Fund's notice that employer claims and settlements go online from 1 August 2026 could not be opened (spf.gov.om refused the connection). Also open: whether the Board has set the start date of the 9% savings system and its current status; the Board decision on work injury and sick leave for non-Omani workers (the old skill said 1% for all expatriates, not confirmed);   Fund portal steps; GCC national contribution rates. The old skill’s employer total of 12.5% omitted the two leave branches and is replaced.
