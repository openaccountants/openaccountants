---
name: panama-social-contributions
description: "Use this skill for Panama social security contributions to the Caja de Seguro Social (CSS) in 2026. It gives the rates of Ley 51 of 2005 as reformed by Ley 462 of 2025 (consolidated text, Gaceta Oficial 30284-B of 22 May 2025): employee 9.75% of salary, employer 13.25% until 28 February 2027 (14.25% to February 2029, 15.25% from March 2029), the special contribution on each of the three 13th-month instalments (employer 10.75%, employee 7.25%), independent workers (9.36% for IVM, 8.5% voluntary health on at least B/.800 a month), pensioners 6.75%, and the late payment surcharges (2%, 5%, 10%, 15% plus 1% a month interest). Trigger phrases include CSS Panama, cuota obrero patronal, Ley 462, decimotercer mes cuota, trabajador independiente CSS and planilla CSS."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/panama-social-contributions"
  jurisdiction: "PA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Panama social security contributions (CSS), 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Panamanian accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Panama.

## Who this applies to

Employers, employees, independent workers and pensioners covered by the Caja de Seguro Social in 2026, under Ley 51 of 2005 as reformed by Ley 462 of 18 March 2025 (Gaceta Oficial 30238; consolidated text in Gaceta Oficial 30284-B of 22 May 2025). Income tax withholding is in [panama-payroll](panama-payroll.md).

Refusal catalogue:
- **R-PA-CSS-1 Worker status unknown.** Employees and independents are entirely different regimes; stop until the status is known.
- **R-PA-CSS-2 Professional risk premium.** The riesgos profesionales premium depends on the employer's risk class; refer.
- **R-PA-CSS-3 Educational insurance on salaries** (seguro educativo, employee and employer): rates not in this law and not confirmed in this pass; refer.
- Arrears, payment agreements, audits of planillas (CSS may review planillas at any time, art. 3-A): refer.

## Rates, bands and thresholds

| Contribution | Rate | Base and period | Source |
| --- | --- | --- | --- |
| Employee (art. 96.1) | 9.75% | Salary | Gaceta Oficial 30284-B, Ley 51 consolidated (Procuraduria de la Administracion): http://gacetas.procuraduria-admon.gob.pa/30284-B_64831.pdf |
| Employer (art. 96.2 a) | 13.25% | Salaries, from Ley 462 in force to 28 February 2027 | same |
| Employer (art. 96.2 b) | 14.25% | 1 March 2027 to 28 February 2029 | same |
| Employer (art. 96.2 c) | 15.25% | From 1 March 2029 | same |
| Employer special contribution on the 13th month (art. 96.4) | 10.75% | Each of the three 13th-month instalments | same |
| Employee special contribution on the 13th month (art. 96.5) | 7.25% | Each of the three instalments | same |
| Independent workers, IVM (arts. 76, 96.3) | 9.36% | Ingreso cotizable | same |
| Independent workers, voluntary health and maternity (art. 76) | 8.5% | Declared income, not below B/.800 a month | same |
| Pensioners (art. 96.6) | 6.75% | Monthly pension | same |
| Insured receiving subsidies (art. 96.7) | 9.75% | Subsidy | same |
| State contribution (art. 96.9) | 0.8% | Salaries and contribution bases | same |
| Late payment surcharge, days 1 to 10 (art. 121) | 2% | Amount owed | same |
| Late payment surcharge, days 11 to 20 | 5% | | same |
| Late payment surcharge, days 21 to 30 | 10% | | same |
| Late payment surcharge, after 30 days | 15% | | same |
| Late payment interest | 1% a month or part | In addition to surcharges | same |
| Refusing information to CSS (art. 120) | B/.1,000 to B/.50,000 | Employers | same |

## The base

- Employee and employer contributions are on salaries (sueldos); no ceiling appears in art. 96.
- The 13th month (decimotercer mes) is paid in three instalments; each bears the special contributions of 10.75% (employer) and 7.25% (employee) instead of the ordinary rates.
- Independent workers pay their own IVM contribution of 9.36% of ingreso cotizable and may join health and maternity at 8.5% of a declared income of at least B/.800 a month (CSS may update it by regulation).
- Contributions are paid monthly within the periods the CSS board sets by regulation (art. 121).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Monthly planilla and payment | Within the periods set by CSS regulation (not confirmed in this pass) | CSS SIPE system |
| New employer registration | Within the first six working days of starting operations | CSS |
| DGI Planilla 03 (income tax) | Within 60 calendar days after the CSS planilla is filed | DGI e-Tax 2.0 (https://dgi.mef.gob.pa/DInforme/Planilla03.php) |

## Penalties and interest

Late payment: 2% in the first 10 days, 5% in the next 10, 10% to day 30, 15% after 30 days, plus 1% interest a month (art. 121). Contributions deducted from salaries and not paid to CSS within 90 days may be reported to the Public Ministry. Refusing information: B/.1,000 to B/.50,000 (art. 120).

## Cross-border points

Foreign employees working in Panama under a Panamanian employment relationship contribute like nationals. Totalisation agreements were not checked.

## Two worked examples that recompute

### Example 1: monthly salary of B/.2,000, and a 13th-month instalment of B/.666.67

Ordinary month: employee 9.75% = B/.195.00, employer 13.25% = B/.265.00. On the 13th-month instalment: employee 7.25% = B/.48.33, employer 10.75% = B/.71.67.

```oa-check
name: PA 2026 CSS salary and 13th-month instalment
inputs:
  salary: 2000
  decimo_instalment: 666.67
steps:
  - employee: salary * 0.0975
  - employer: salary * 0.1325
  - decimo_employee: round(decimo_instalment * 0.0725, 2)
  - decimo_employer: round(decimo_instalment * 0.1075, 2)
expected:
  employee: 195
  employer: 265
  decimo_employee: 48.33
  decimo_employer: 71.67
```

### Example 2: the March 2027 step (budget decision)

A payroll of B/.100,000 a month costs B/.13,250 in employer CSS to February 2027 and B/.14,250 from March 2027: B/.1,000 more a month, B/.10,000 over March to December 2027. An employer budgeting 2027 must use both rates.

```oa-check
name: PA employer CSS step in March 2027
inputs:
  payroll: 100000
steps:
  - to_feb_2027: payroll * 0.1325
  - from_mar_2027: payroll * 0.1425
  - extra_month: from_mar_2027 - to_feb_2027
  - extra_mar_to_dec: extra_month * 10
expected:
  to_feb_2027: 13250
  from_mar_2027: 14250
  extra_month: 1000
  extra_mar_to_dec: 10000
```

## Ask the client first

1. Is the worker an employee or an independent?
2. Monthly salary and the 13th-month instalments paid.
3. For independents: ingreso cotizable and whether health cover is wanted.
4. Payroll month (the employer rate changes on 1 March 2027).
5. Any arrears or payment agreement with CSS.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Gaceta Oficial 30284-B (22 May 2025), Ley 51 of 2005 consolidated with Ley 462: arts. 3-A, 76, 96, 120, 121, 127 | http://gacetas.procuraduria-admon.gob.pa/30284-B_64831.pdf | 2026-11-14 |
| Read for Gaceta Oficial 30238 (18 March 2025), Ley 462 as published (scanned; used to confirm date and number) | http://gacetas.procuraduria-admon.gob.pa/30238_64368.pdf | 2026-11-14 |
| Read for DGI, Planilla 03: 60-day link to the CSS planilla | https://dgi.mef.gob.pa/DInforme/Planilla03.php | 2026-11-14 |

Not yet confirmed: educational insurance (seguro educativo) on salaries, employee and employer (the old file gave 1.25% and 1.50%); the riesgos profesionales premium; the monthly CSS payment due date; the old file's statement that there is no contribution ceiling (none is in art. 96, but the regulations were not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `panama-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/panama-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
