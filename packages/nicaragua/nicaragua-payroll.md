---
name: nicaragua-payroll
description: >
  Use this skill to run Nicaragua payroll in 2026. It covers the employer's monthly IR
  retention on employment income by the DGI projection method (monthly gross less the
  employee's 7% INSS and savings fund contributions, times 12, on the art. 23 scale,
  divided by 12), the extra retention on occasional payments such as vacation pay and
  bonuses, exempt items (13th month, severance up to the legal limits, reimbursed
  expenses), definitive retentions on severance above C$500,000, board fees and
  non-residents, and the INSS employer and employee rates that live in
  nicaragua-social-contributions. Trigger phrases include planilla Nicaragua, retencion IR
  salarios, treceavo mes, vacaciones retencion and INSS patronal.
version: "1.0"
jurisdiction: NI
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

# Nicaragua payroll, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Nicaraguan accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Nicaragua.

## Who this applies to

Employers in Nicaragua paying salaries in 2026. Retention of IR on employment income is here; the scale and exemptions are owned by [nicaragua-income-tax](nicaragua-income-tax.md); INSS rates by [nicaragua-social-contributions](nicaragua-social-contributions.md).

Refer: public sector, free zones, expatriates who are not resident, termination settlements above the legal limits, employers with INSS or DGI arrears.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross salary unknown | Stop |
| Employee not resident | 20% definitive retention, no scale |
| Bonus or vacation pay | Taxable; use the occasional payment method |
| Employer size for INSS unknown | Use the higher (more than 50 workers) employer rate |

## Rates, bands and thresholds

| Item | Rate or rule | Condition | Source |
| --- | --- | --- | --- |
| Retention scale | Art. 23: exempt to C$100,000, 15% to C$200,000, 20% to C$350,000 (base C$15,000), 25% to C$500,000 (base C$45,000), 30% above (base C$82,500) | Annual projection | DGI FAQ, Periodo fiscal y tarifa del impuesto: https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm |
| Monthly method | (Monthly gross less INSS and savings fund) x 12, apply the scale, divide by 12 | Reglamento art. 19 | same |
| Occasional payments | Add to the annual projection, recompute, the difference is the extra retention | Vacation, bonuses, half-yearly or annual incentives | same |
| Retention code for salaries | Code 11, table of art. 23 | Monthly declaration | DGI catalogue of retention codes and rates (Aviso 005-01-2024): https://www.dgi.gob.ni/pdfNoticia/3175 |
| Severance above five months and C$500,000 (code 31) | 15% definitive | On the excess | same |
| Board fees, residents (code 32) | 25% definitive | | same |
| Non-resident employment income (code 35) | 20% definitive | | same |
| INSS employee, integral regime | 7.0% | Both employer sizes | INSS, Regimenes de afiliacion: https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion |
| INSS employer, integral regime | 21.5% (fewer than 50 workers) or 22.50% (more than 50) | | same |

## The base

- Taxable pay includes salary, overtime, vacation pay, incentives and bonuses. The 13th month is exempt; so are severance within the legal limits, collective agreement benefits in kind given to all, social security subsidies and genuine expense reimbursements (LCT art. 19, DGI FAQ).
- The employee's INSS contribution and savings fund contributions are deducted before the projection.
- With two employers, each retains on its own pay; the employee files if the combined net exceeds C$100,000.

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| IR retained on salaries | Monthly, declaration of recaudos y anticipos | DGI VET |
| INSS contributions | Monthly | INSS |
| 13th month payment | Codigo del Trabajo date not confirmed in this pass | Employer |

## Penalties and interest

Codigo Tributario art. 124 sanctions; fines in unidades de multa. Surcharges: see Not yet confirmed.

## Cross-border points

Non-resident employees: 20% definitive retention on Nicaraguan employment income (LCT art. 24.3 as reformed by Ley 987). No tax treaty confirmed.

## Two worked examples that recompute

### Example 1: monthly retention on C$40,000

INSS 7% C$2,800; projection C$37,200 x 12 = C$446,400; annual IR C$69,100; monthly retention C$5,758.33. The employer also owes INSS of 21.5% (C$8,600) if it has fewer than 50 workers.

```oa-check
name: NI 2026 payroll, C$40,000 salary
inputs:
  gross: 40000
steps:
  - inss_employee: gross * 0.07
  - projection: (gross - inss_employee) * 12
  - annual_ir: 45000 + (projection - 350000) * 0.25
  - monthly_ir: round(annual_ir / 12, 2)
  - inss_employer_small: gross * 0.215
expected:
  inss_employee: 2800
  projection: 446400
  annual_ir: 69100
  monthly_ir: 5758.33
  inss_employer_small: 8600
```

### Example 2: vacation pay in the month (occasional payment method)

Salary C$20,000; net of INSS C$18,600; projection C$223,200; annual IR C$19,640. Vacation pay of one month (C$18,600 net) raises the projection to C$241,800 and the annual IR to C$23,360. The extra retention that month is C$3,720, on top of the normal C$1,636.67. Spreading the vacation pay as ordinary salary would not change the annual tax, only its timing.

```oa-check
name: NI 2026 vacation pay retention
inputs:
  gross: 20000
steps:
  - net_month: gross * 0.93
  - projection: net_month * 12
  - ir_base: 15000 + (projection - 200000) * 0.20
  - projection_with_vacation: projection + net_month
  - ir_with_vacation: 15000 + (projection_with_vacation - 200000) * 0.20
  - extra_retention: ir_with_vacation - ir_base
  - normal_monthly: round(ir_base / 12, 2)
expected:
  projection: 223200
  ir_base: 19640
  ir_with_vacation: 23360
  extra_retention: 3720
  normal_monthly: 1636.67
```

## Ask the client first

1. Each employee's gross, residence and other employer.
2. Number of workers (INSS employer rate).
3. Occasional payments in the month (vacation, bonus, incentives).
4. Savings fund contributions.
5. Any severance or board fees paid.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for DGI FAQ, Periodo fiscal y tarifa del impuesto: art. 23 scale, monthly projection and occasional payment method | https://www.dgi.gob.ni/FAQ/periodo_fiscal_y_tarifa_del_im.htm | 2026-11-14 |
| Read for DGI FAQ, Materia imponible y hecho generador: exempt items, taxable vacation and bonuses | https://www.dgi.gob.ni/FAQ/materia_imponible_y_hecho_gene.htm | 2026-11-14 |
| Read for DGI catalogue of retention codes and rates, codes 11 and 31 to 35 | https://www.dgi.gob.ni/pdfNoticia/3175 | 2026-11-14 |
| Read for INSS, Regimenes de afiliacion: integral regime rates | https://inss-princ.inss.gob.ni/index.php/tramites-37/10-afiliaciones/13-regimenes-de-afiliacion | 2026-11-14 |

Not yet confirmed: the 2026 minimum wage table (MITRAB site unreachable); the INATEC training levy (the old file said 2% of payroll, employer only); 13th month calculation and payment date (Codigo del Trabajo not read); INSS contribution ceiling or its absence; the due date of the monthly retention declaration; surcharges.
