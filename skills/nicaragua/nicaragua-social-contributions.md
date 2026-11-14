---
name: nicaragua-social-contributions
description: >
  Use this skill for Nicaragua social security contributions to the INSS in 2026. It
  gives the rates published by INSS for each affiliation regime, the integral regime
  (employer 21.5% with fewer than 50 workers, 22.50% with more than 50, employee 7.0%),
  the IVM-RP regime without health cover (employer 15.5% or 16.50%, employee 5.0%), the
  voluntary (facultativo) regimes (22.25% integral, 14.00% IVM, on declared income not
  below the minimum wage), how the employee share reduces taxable salary, and what is
  still open (ceiling, INATEC, deadlines). Trigger phrases include INSS Nicaragua,
  cotizacion patronal, cotizacion laboral 7%, regimen integral, seguro facultativo and
  planilla INSS.
version: "1.0"
jurisdiction: NI
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

# Nicaragua social security contributions (INSS), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Nicaragua.

## Who this applies to

Employers, employees and voluntary contributors of the Instituto Nicaraguense de Seguridad Social (INSS) in 2026. IR retention is in [nicaragua-payroll](nicaragua-payroll.md).

Refer: public sector, special regimes, arrears and agreements with INSS, occupational accident claims.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Regime unknown | Integral regime |
| Employer headcount unknown | More than 50 workers rate (22.50%) |
| Contribution ceiling | Do not apply one; see Not yet confirmed |

## Rates, bands and thresholds

| Regime | Employer | Employee | Condition | Source |
| --- | --- | --- | --- | --- |
| Integral (health, maternity, IVM, occupational risk) | 21.5% | 7.0% | Fewer than 50 workers | INSS, Regimenes de afiliacion: https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion |
| Integral | 22.50% | 7.0% | More than 50 workers | same |
| IVM-RP (invalidity, old age, death, occupational risk; no health) | 15.5% | 5.0% | Fewer than 50 workers | same |
| IVM-RP | 16.50% | 5.0% | More than 50 workers | same |
| Voluntary integral (facultativo) | 22.25% | 0.00% | On declared income, the established minimum wage | same |
| Voluntary IVM (facultativo) | 14.00% | 0.00% | Medium and long term benefits only | same |

## The base

- Contributions are computed on the worker's salary each month at the regime rates above.
- The employee's share is deducted from taxable salary for IR (DGI projection method, see the payroll skill).
- The voluntary integral regime excludes work accident benefits; its base is the declared income at the minimum wage set by INSS.

## Deadlines and filing

Monthly INSS payroll (planilla) through INSS systems; the due date was not confirmed in this pass.

## Penalties and interest

Not confirmed in this pass (INSS law and its regulation not read).

## Cross-border points

Foreign workers employed in Nicaragua are affiliated like nationals; totalisation agreements were not checked.

## Two worked examples that recompute

### Example 1: salary of C$30,000, employer with 20 workers

Employee 7.0% = C$2,100; employer 21.5% = C$6,450; total C$8,550.

```oa-check
name: NI 2026 INSS integral, small employer
inputs:
  salary: 30000
steps:
  - employee: salary * 0.07
  - employer: salary * 0.215
  - total: employee + employer
expected:
  employee: 2100
  employer: 6450
  total: 8550
```

### Example 2: growing past 50 workers (decision on cost)

A monthly payroll of C$1,500,000 costs C$322,500 in employer INSS at 21.5%; once the employer has more than 50 workers the rate is 22.50%, C$337,500. The step adds C$15,000 a month, C$180,000 a year, on the whole payroll, not only on the new hires.

```oa-check
name: NI 2026 INSS employer rate step at 50 workers
inputs:
  payroll: 1500000
steps:
  - small: payroll * 0.215
  - large: payroll * 0.225
  - extra_month: large - small
  - extra_year: extra_month * 12
expected:
  small: 322500
  large: 337500
  extra_month: 15000
  extra_year: 180000
```

## Ask the client first

1. Number of workers and regime registered with INSS.
2. Each worker's monthly salary.
3. Any voluntary contributors.
4. Arrears or agreements with INSS.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for INSS, Regimenes de afiliacion: rates of the integral, IVM-RP and voluntary regimes | https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion | 2026-11-14 |
| Read for DGI FAQ, Periodo fiscal y tarifa del impuesto: INSS deducted before the IR projection | https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm | 2026-11-14 |

Not yet confirmed: whether a maximum contributory salary applies (the old file said INSS Resolution RI-112-2018 removed it; not read); the INATEC 2% training levy; how exactly 50 workers is classed; payment deadline and surcharges; Decreto 06-2019 text.
