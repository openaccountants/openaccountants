---
name: costa-rica-payroll
description: >
  Use this skill to run Costa Rica payroll in 2026. It covers the employer's monthly
  withholding of the salary tax (impuesto al salario) on the 2026 table of Decreto
  Ejecutivo 45333-H (not subject to CRC 918,000 a month, then 10%, 15%, 20% and 25%),
  the monthly family credits (CRC 1,710 per child, CRC 2,590 for the spouse), the
  deduction of the worker's 10.83% social charges and the employer's 26.83% from the
  CCSS table, the planilla calendar and what is still open (aguinaldo, minimum wages).
  Trigger phrases include planilla Costa Rica, impuesto al salario 2026, retencion
  salario, cargas sociales, salario neto Costa Rica and TRIBU-CR retenciones.
version: "1.0"
jurisdiction: CR
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Costa Rica payroll, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Costa Rican accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Costa Rica.

## Who this applies to

Employers in Costa Rica paying salaries in 2026. The salary tax table and credits are here; social charges detail is owned by [costa-rica-social-contributions](costa-rica-social-contributions.md); the individual's annual return by [costa-rica-income-tax](costa-rica-income-tax.md).

Refer: termination settlements (preaviso, cesantia), foreign employees not resident, free zone employers, payroll arrears.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross salary unknown | Stop |
| Family credit claimed with no proof | Do not apply the credit |
| Two employers | Each withholds on its own salary; see Not yet confirmed |

## Rates, bands and thresholds

| Monthly gross salary from (CRC) | To (CRC) | Rate | Source |
| --- | --- | --- | --- |
| 0 | 918,000 | Not subject | Hacienda, Tramos del impuesto sobre la renta 2026: https://www.hacienda.go.cr/docs/TramosRenta2026.pdf |
| 918,000 | 1,347,000 | 10% | same |
| 1,347,000 | 2,364,000 | 15% | same |
| 2,364,000 | 4,727,000 | 20% | same |
| Over 4,727,000 | | 25% | same |
| Credit per child, monthly | CRC 1,710 | Against the tax | same |
| Credit for spouse, monthly | CRC 2,590 | Against the tax | same |
| Worker social charges | 10.83% | SEM 5.50, IVM 4.33, Banco Popular 1.00 | CCSS, Patronos (quota calculator, 2026): https://www.ccss.sa.cr/patronos |
| Employer social charges | 26.83% | CCSS, other institutions and LPT | same |

## The base

1. Apply the monthly table to the gross salary of the month; tax each slice at its rate.
2. Subtract the monthly credits for each qualifying child and the spouse.
3. Deduct the worker's 10.83% social charges; the employer pays 26.83% on top.
4. Pay net salary; remit withheld tax monthly in TRIBU-CR and the CCSS planilla in the CCSS window.

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Salary tax withheld | Monthly; due day not confirmed in this pass | TRIBU-CR |
| CCSS planilla | Present from the 26th to the fourth working day of the next month | Oficina Virtual CCSS |

## Penalties and interest

Late payment of withheld tax: 1% a month or part, up to 20% (Codigo de Normas art. 80, Hacienda 2026 summary); late filing: half a salario base, CRC 231,100. Not presenting the CCSS planilla: 2% on SEM and 2% on IVM billing.

## Cross-border points

Foreign workers on a Costa Rican payroll follow the same table if resident; payments to non-residents fall under the remittance tax (not covered).

## Two worked examples that recompute

### Example 1: salary of CRC 1,500,000, no credits

Tax: 10% of CRC 429,000 = 42,900 plus 15% of CRC 153,000 = 22,950; total CRC 65,850. Worker charges CRC 162,450. Net pay CRC 1,271,700. Employer charges CRC 402,450.

```oa-check
name: CR 2026 payroll on 1.5 million
inputs:
  gross: 1500000
steps:
  - tax: (1347000 - 918000) * 0.10 + (gross - 1347000) * 0.15
  - worker_charges: gross * 0.1083
  - net_pay: gross - tax - worker_charges
  - employer_charges: gross * 0.2683
expected:
  tax: 65850
  worker_charges: 162450
  net_pay: 1271700
  employer_charges: 402450
```

### Example 2: family credits near the threshold (decision)

Salary CRC 1,000,000: tax on the CRC 82,000 above CRC 918,000 is CRC 8,200. With two children and a spouse the credits are CRC 6,010, leaving CRC 2,190. Without proof of the dependants the employer withholds the full CRC 8,200, so collecting the documents is worth CRC 6,010 a month to the worker.

```oa-check
name: CR 2026 family credits on 1 million
inputs:
  gross: 1000000
  children: 2
steps:
  - tax: (gross - 918000) * 0.10
  - credits: children * 1710 + 2590
  - tax_after_credits: max(tax - credits, 0)
expected:
  tax: 8200
  credits: 6010
  tax_after_credits: 2190
```

## Ask the client first

1. Monthly gross salary of each employee.
2. Children and spouse for credits, with documents.
3. Other employers of the same worker.
4. CCSS employer number and the planilla calendar used.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Hacienda, Tramos del impuesto sobre la renta 2026: salaried table and monthly credits | https://www.hacienda.go.cr/docs/TramosRenta2026.pdf | 2026-11-14 |
| Read for CCSS Patronos page: 2026 worker and employer percentages, planilla dates, surcharges | https://www.ccss.sa.cr/patronos | 2026-11-14 |
| Read for Hacienda, Infracciones y sanciones administrativas mas relevantes (2026): arts. 79 and 80 | https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf | 2026-11-14 |

Not yet confirmed: the aguinaldo (13th month, Ley 2412) amount, date and tax treatment; the 2026 minimum wage decree (MTSS); vacation and termination pay; the due day of the monthly withholding return in TRIBU-CR; treatment of a second employer.
