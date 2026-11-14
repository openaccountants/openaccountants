---
name: costa-rica-social-contributions
description: >
  Use this skill for Costa Rica employer and employee social charges (cargas sociales) in
  2026. It gives the CCSS table in force from January 2026, health and maternity (SEM)
  9.25% employer and 5.50% worker, pensions (IVM) 5.58% employer and 4.33% worker after
  the January 2026 increase to 11.66% in total, the employer's other institutions
  (Asignaciones Familiares 5%, IMAS 0.5%, INA 1.5%, Banco Popular 0.25%) and the Ley de
  Proteccion al Trabajador charges (Banco Popular 0.25% employer and 1% worker, FCL 1.5%,
  OPC 2%, INS 1%), totals 26.83% employer and 10.83% worker, the minimum contributory
  bases (CRC 346,789 SEM, CRC 324,590 IVM), the planilla calendar and the 2% surcharges.
  Trigger phrases include cargas sociales 2026, CCSS planilla, SEM IVM, Ley de Proteccion
  al Trabajador and BMC.
version: "1.0"
jurisdiction: CR
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Costa Rica social charges (CCSS, other institutions and LPT), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Costa Rican accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Costa Rica.

## Who this applies to

Employers (patronos fisicos or juridicos) and employees in Costa Rica in 2026, for the planilla billed by the Caja Costarricense de Seguro Social (CCSS), which also collects for other institutions and the Ley de Proteccion al Trabajador (LPT). Salary income tax withholding: [costa-rica-payroll](costa-rica-payroll.md).

Refer: independent workers and voluntary insured (their own rates, 11.66% IVM in total from 2026), work-risk insurance policy pricing beyond the 1% INS line, arrears and payment agreements.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Salary below the minimum contributory base | Billing is adjusted to the BMC (CCSS) |
| Planilla not presented in the window | Expect the 2% SEM and 2% IVM surcharges |
| Whether a payment is salary | Report 100% of salary, including maternity licence amounts paid by CCSS |

## Rates, bands and thresholds

| Line | Employer | Worker | Source |
| --- | --- | --- | --- |
| SEM (health and maternity) | 9.25% | 5.50% | CCSS, Patronos (quota calculator, 2026): https://www.ccss.sa.cr/patronos |
| IVM (pensions), from 1 January 2026 | 5.58% | 4.33% | same |
| Banco Popular (other institutions) | 0.25% | | same |
| Asignaciones Familiares | 5.00% | | same |
| IMAS | 0.50% | | same |
| INA | 1.50% | | same |
| LPT: Banco Popular | 0.25% | 1.00% | same |
| LPT: Fondo de Capitalizacion Laboral | 1.50% | | same |
| LPT: Operadora de pensiones complementarias | 2.00% | | same |
| LPT: INS | 1.00% | | same |
| Total | 26.83% | 10.83% | same |
| Minimum contributory base, SEM | CRC 346,789 | | same |
| Minimum contributory base, IVM | CRC 324,590 | | same |
| IVM total 2026 to 2028 (with State 1.75%) | 11.66% | | CCSS news, 18 Dec 2025: https://www.ccss.sa.cr/noticias/noticia?v=822124515110 |
| IVM until 31 December 2025 | 5.42% | 4.17% | same |
| Surcharge for not presenting the planilla | 2% of SEM billing plus 2% of IVM billing | | CCSS, Patronos (quota calculator, 2026): https://www.ccss.sa.cr/patronos |

## The base

- Report 100% of the salary paid in the month; the worker's 10.83% is deducted from it and the employer adds 26.83%.
- Salaries below CRC 346,789 (SEM) and CRC 324,590 (IVM) are adjusted to the minimum contributory base (BMC) when billed.
- The IVM rate rose on 1 January 2026 by 0.16 points for employers and for workers (the fifth step towards 12.16% in 2029); it stays at 11.66% in total until December 2028.

## Deadlines and filing

| Step | When | Where |
| --- | --- | --- |
| Present the planilla | From the 26th of the month to the fourth working day of the next month (large clients: to the third working day) | Oficina Virtual CCSS |
| Billing | Automatic on the fifth working day if not billed by the employer | Oficina Virtual CCSS |
| Payment | Check the payment date in the Oficina Virtual (CCSS says from the 16th to the 20th of each month); quotas can be paid up to 59 days overdue at collection points | Banks and collection points |

## Penalties and interest

Not presenting the planilla: 2% surcharge on the SEM billing and 2% on the IVM billing, and monthly changes are not recorded. Other late payment charges were not read in this pass.

## Cross-border points

Foreign employees under a Costa Rican employment relationship are reported like nationals. Totalisation agreements were not checked.

## Two worked examples that recompute

### Example 1: salary of CRC 1,500,000

Worker 10.83% = CRC 162,450; employer 26.83% = CRC 402,450; total cost of social charges CRC 564,900.

```oa-check
name: CR 2026 cargas sociales on 1.5 million
inputs:
  salary: 1500000
steps:
  - worker: salary * (0.055 + 0.0433 + 0.01)
  - employer: salary * (0.0925 + 0.0558 + 0.0725 + 0.0475)
  - total: worker + employer
expected:
  worker: 162450
  employer: 402450
  total: 564900
```

### Example 2: what the IVM step costs a payroll of CRC 10,000,000 (budget decision)

Employer IVM moved from 5.42% to 5.58%: CRC 542,000 to CRC 558,000 a month, CRC 16,000 more; workers' IVM also rises by CRC 16,000 in total, reducing net pay. Over 12 months the employer pays CRC 192,000 more.

```oa-check
name: CR 2026 IVM increase on a 10 million payroll
inputs:
  payroll: 10000000
steps:
  - employer_2025: payroll * 0.0542
  - employer_2026: payroll * 0.0558
  - extra_month: employer_2026 - employer_2025
  - extra_year: extra_month * 12
  - worker_extra_month: payroll * (0.0433 - 0.0417)
expected:
  employer_2025: 542000
  employer_2026: 558000
  extra_month: 16000
  extra_year: 192000
  worker_extra_month: 16000
```

## Ask the client first

1. Monthly salaries of each worker, including any maternity licence.
2. Employer type and whether it is a large client of CCSS.
3. Planilla presentation dates used so far and any surcharge billed.
4. Independent workers or voluntary insured in the household or business.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for CCSS Patronos page: 2026 quota calculator table (SEM, IVM, other institutions, LPT, totals 26.83% and 10.83%), BMC amounts, planilla steps and dates, 2% surcharges, 59-day payment note | https://www.ccss.sa.cr/patronos | 2026-11-14 |
| Read for CCSS news of 18 Dec 2025: IVM rates before and from January 2026, 11.66% total, State share | https://www.ccss.sa.cr/noticias/noticia?v=822124515110 | 2026-11-14 |

Not yet confirmed: interest and surcharges for late payment beyond the 2% for not presenting; independent worker rates by income band; work-risk insurance (riesgos del trabajo) policy cost beyond the 1% INS line; whether the IVM base is adjusted in the same way as SEM for part-time staff.
