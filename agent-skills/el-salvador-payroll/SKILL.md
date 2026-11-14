---
name: el-salvador-payroll
description: "Use this skill to run El Salvador payroll in 2026. It covers the employer's monthly ISR retention on the Decreto Ejecutivo 10 tables in force from May 2025 (no retention to USD 550 a month, then 10%, 20% and 30% with fixed amounts of USD 17.67, 60.00 and 288.57), the retention base after the employee's ISSS and AFP, the 10% retention on second jobs, the aguinaldo exemption of two monthly minimum wages of commerce and services (USD 817.60), the minimum wages of Decreto Ejecutivo 11 in force from 1 June 2025 (USD 408.80 commerce, services and industry) and the employer's obligations. ISSS and AFP rates live in el-salvador-social-contributions. Trigger phrases include planilla El Salvador, retencion de renta asalariados, aguinaldo exento, salario minimo 2025 and tabla de retencion mensual."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/el-salvador-payroll"
  jurisdiction: "SV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# El Salvador payroll, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Salvadoran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in El Salvador.

## Who this applies to

Employers in El Salvador paying salaries in 2026: monthly ISR retention, aguinaldo, minimum wages and remittance. ISSS and AFP contributions are in [el-salvador-social-contributions](el-salvador-social-contributions.md); the employee's annual tax in [el-salvador-income-tax](el-salvador-income-tax.md).

Refer: non-domiciled employees (30% or 20% final retention), public sector payrolls, termination settlements, agricultural piece-rate pay, employers under DGII audit.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross salary unknown | Stop |
| Employee has a second job | Table on the larger salary, 10% on the rest (Decreto Ejecutivo 10) |
| Sector for the minimum wage unknown | Commerce and services, USD 408.80 |
| Aguinaldo above USD 817.60 | Retain on the excess |

## Rates, bands and thresholds

**Monthly retention table, Decreto Ejecutivo 10 (in force from May 2025), applied to salary after the employee's ISSS and AFP.**

| Band | From (USD) | To (USD) | Rate on excess | Over | Plus fixed | Source |
| --- | --- | --- | --- | --- | --- | --- |
| I | 0.01 | 550.00 | No retention | | | Ministerio de Hacienda, Decreto Ejecutivo 10: https://www.mh.gob.sv/wp-content/uploads/2025/05/Modificacion-a-las-tablas-de-retenci%C3%B3n-del-Impuesto-Sobre-la-Renta-Decreto-Ejecutivo-NO.10.pdf |
| II | 550.01 | 895.24 | 10% | 550.00 | 17.67 | same |
| III | 895.25 | 2,038.10 | 20% | 895.24 | 60.00 | same |
| IV | 2,038.11 | and above | 30% | 2,038.10 | 288.57 | same |

The same decree gives fortnightly (II from USD 275.01, fixed 8.83; III from 447.63, fixed 30.00; IV from 1,019.06, fixed 144.28) and weekly tables (II from USD 137.51, fixed 4.42; III from 223.82, fixed 15.00; IV from 509.53, fixed 72.14), plus June and December recalculation tables.

**Other payroll figures.**

| Item | Amount | Condition | Source |
| --- | --- | --- | --- |
| Retention on a second job | 10% of the sums paid | The worker tells each employer in January | Ministerio de Hacienda, Decreto Ejecutivo 10: https://www.mh.gob.sv/wp-content/uploads/2025/05/Modificacion-a-las-tablas-de-retenci%C3%B3n-del-Impuesto-Sobre-la-Renta-Decreto-Ejecutivo-NO.10.pdf |
| Salary above which the employee must file | USD 60,000 a year | Decreto Ejecutivo 10 and LISR art. 38 | same |
| Aguinaldo exempt from ISR | Two monthly minimum wages of commerce and services | LISR art. 4.16; excess retained | Asamblea Legislativa, LISR consolidated: https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf |
| So, exempt aguinaldo 2026 | USD 817.60 | 2 x USD 408.80, the commerce and services wage below | Organo Ejecutivo, Decreto Ejecutivo 11 (2025), Jurisprudencia: https://www.jurisprudencia.gob.sv/DocumentosBoveda/D/2/2020-2029/2025/05/10A4DA.PDF |
| Minimum wage, commerce and services | USD 408.80 a month (USD 13.440 a day, USD 1.680 an hour) | Decreto Ejecutivo 11, in force 1 June 2025 | Organo Ejecutivo, Decreto Ejecutivo 11 (2025), Jurisprudencia: https://www.jurisprudencia.gob.sv/DocumentosBoveda/D/2/2020-2029/2025/05/10A4DA.PDF |
| Minimum wage, industry, sugar mills, agroindustry | USD 408.80 a month | same | same |
| Minimum wage, textile maquila | USD 402.32 a month | same | same |
| Minimum wage, coffee processing and sugar cane harvest | USD 305.23 a month | same | same |
| Minimum wage, agriculture and fishing | USD 272.53 a month | same | same |

## The base

1. **Retention base:** monthly salary less the employee's ISSS (3%, capped) and AFP (7.25%); LISR art. 29.7 puts contributions and, up to USD 9,100 a year, the USD 1,600 fixed deduction inside the retention. The Band II amounts do not include the USD 1,600; the decree says it must be considered in the calculation.
2. **Apply the table** for the pay period. In June and December the employer recalculates with the recalculation tables so the year's retention approaches the annual tax.
3. **Aguinaldo** paid in December is not retained up to two minimum wages of commerce and services (CT art. 155); the excess is retained.
4. **Second employer:** 10% on the smaller salary.
5. **Remit** monthly to DGII with the retention return.

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| Retained ISR | Within the first 10 working days of the following month (with the monthly returns) | DGII retention return (F-14) |
| June and December recalculation | June and December payrolls | Employer |
| Annual report of retentions | Not confirmed in this pass | DGII |
| ISSS and AFP | See el-salvador-social-contributions | |

## Penalties and interest

Codigo Tributario art. 246: retained and not remitted, a fine equal to the amount; not retained, 75% of the amount; remitted late, 50%; short remitted, 30%. A breach of the minimum wage decree is fined per right breached (Decreto Ejecutivo 11 art. 12) and checked by the labour inspectorate (art. 13).

## Cross-border points

Payments to non-domiciled individuals for work in El Salvador bear the 20% final retention of CT art. 158 or 30% by assessment, not the table. Totalisation of pension periods abroad was not checked.

## Two worked examples that recompute

### Example 1: salary of USD 1,200 a month

ISSS 3% of USD 1,000 (cap) = USD 30.00; AFP 7.25% = USD 87.00. Retention base USD 1,083.00, band III: USD 60.00 + 20% of USD 187.76 = USD 97.55.

```oa-check
name: SV 2026 monthly retention, USD 1,200 salary
inputs:
  salary: 1200
  isss_cap: 1000
steps:
  - isss: min(salary, isss_cap) * 0.03
  - afp: salary * 0.0725
  - base: salary - isss - afp
  - retention: round(60 + (base - 895.24) * 0.20, 2)
expected:
  isss: 30
  afp: 87
  base: 1083
  retention: 97.55
```

### Example 2: aguinaldo of USD 1,000, retain or not (decision)

The exempt amount is two minimum wages of commerce and services, USD 817.60. An aguinaldo of USD 1,000 has USD 182.40 subject to retention; an aguinaldo of USD 800 has none. The minimum wage of the employee's own sector does not matter: the law fixes the commerce and services wage.

```oa-check
name: SV 2026 aguinaldo exemption
inputs:
  min_wage_commerce: 408.80
  aguinaldo_a: 1000
  aguinaldo_b: 800
steps:
  - exempt: min_wage_commerce * 2
  - taxable_a: max(aguinaldo_a - exempt, 0)
  - taxable_b: max(aguinaldo_b - exempt, 0)
expected:
  exempt: 817.60
  taxable_a: 182.40
  taxable_b: 0
```

## Ask the client first

1. Each employee's salary, pay period (monthly, fortnightly, weekly) and sector.
2. Any second job, and which employer applies the table.
3. Aguinaldo amounts and dates.
4. Domicile of each employee.
5. Whether the employer is current with DGII, ISSS and AFP.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Decreto Ejecutivo 10 (2025) (read from the transparencia.mh.gob.sv copy, which now redirects scripts to the portal; this is the Ministerio de Hacienda copy of the same decree, behind a Cloudflare check): retention tables (monthly, fortnightly, weekly, recalculation), second job rule, USD 60,000 filing rule, art. 4 in force | https://www.mh.gob.sv/wp-content/uploads/2025/05/Modificacion-a-las-tablas-de-retenci%C3%B3n-del-Impuesto-Sobre-la-Renta-Decreto-Ejecutivo-NO.10.pdf | 2026-11-14 |
| Read for the Ministerio de Hacienda notice that the Decreto Ejecutivo 10 tables apply from May 2025 | https://www.mh.gob.sv/wp-content/uploads/2025/05/Modificacion-a-las-tablas-de-retenci%C3%B3n-del-Impuesto-Sobre-la-Renta-Decreto-Ejecutivo-NO.10.pdf | 2026-11-14 |
| Read for Decreto Ejecutivo 11 (2025), minimum wage table art. 2 and arts. 12, 13, 15 | https://www.jurisprudencia.gob.sv/DocumentosBoveda/D/2/2020-2029/2025/05/10A4DA.PDF | 2026-11-14 |
| Read for LISR consolidated, arts. 4.16, 29.7 and 38 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/F326A5D9-F56E-4FCA-81D6-60088ABB52BF.pdf | 2026-11-14 |
| Read for Codigo Tributario consolidated, arts. 155, 156, 158 and 246 | https://www.asamblea.gob.sv/sites/default/files/documents/decretos/297557B6-E5FD-4A41-B734-089751C41FDA.pdf | 2026-11-14 |

Not yet confirmed: any minimum wage decree for 2026 (the 2025 decree is to be reviewed under Codigo de Trabajo art. 159); aguinaldo days by seniority (Codigo de Trabajo arts. 196 to 202 not read); vacation pay; the annual retention report and its date; INSAFORP.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `el-salvador-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/el-salvador-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
