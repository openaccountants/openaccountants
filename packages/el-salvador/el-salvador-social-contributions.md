---
name: el-salvador-social-contributions
description: Use this skill whenever asked about El Salvador statutory payroll contributions, social security, pensions, or payroll-related income tax withholding for employees and employers. Trigger on phrases like "ISSS contribution", "how much ISSS do I pay", "AFP pension contribution", "Salvadoran payroll deductions", "descuentos de ley", "cotización ISSS", "cotización AFP", "INSAFORP levy", "retención de renta", "sueldo neto El Salvador", "planilla ISSS", "OVISSS", "salario mínimo El Salvador", or any question about El Salvador employer/employee social cost. Also trigger when classifying bank-statement transactions that relate to ISSS debits, AFP (Crecer, Confía) pension debits, INSAFORP payments, or Ministerio de Hacienda income-tax withholding from Salvadoran banks (Banco Agrícola, Cuscatlán, Davivienda, BAC). Also trigger when preparing or reviewing a Form F-11 (Declaración del Impuesto sobre la Renta) where statutory deductions are relevant. This skill covers ISSS health rates and the USD 1,000 cap, AFP pension rates and the SSF maximum contributory base, the INSAFORP 1% training levy, minimum wages, progressive resident PIT and non-resident flat tax, monthly withholding tables, payment channels, penalties, and bank-statement classification patterns. ALWAYS read this skill before touching any El Salvador payroll, social-security, or payroll-withholding work.
version: 0.1
jurisdiction: SV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# El Salvador Statutory Payroll Contributions (ISSS / AFP / INSAFORP) and Payroll Income Tax

## El Salvador Statutory Payroll Contributions (ISSS / AFP / INSAFORP) and Payroll Income Tax -- Skill v0.1

Scope note. El Salvador does have a personal income tax (Impuesto sobre la Renta), so this skill covers BOTH the statutory social contributions (ISSS health, AFP pension, INSAFORP training levy) AND the payroll income-tax withholding/annual return that sit alongside them. Every rate, cap, and deadline below is sourced inline. Where the research confidence is low or a figure is administratively variable, the text carries an explicit [RESEARCH GAP — reviewer to confirm] marker rather than a guessed value.

## Section 1 -- Quick reference

Read this whole section before computing or classifying anything.

- **Country** — El Salvador (Republic of El Salvador, ISO `SV`)
- **Currency** — USD only — El Salvador uses the US dollar as legal tender (Bitcoin's forced-tender status was repealed in 2025; USD remains the accounting/contribution currency)
- **Social-security legislation** — Ley del Seguro Social and its Reglamento para la Aplicación del Régimen del Seguro Social (ISSS)
- **Pension legislation** — Ley Integral del Sistema de Pensiones (Decreto 462, reformed Dec 2022, effective Jan 2023) [EY pension-law alert]
- **Training-levy legislation** — Ley de Formación Profesional (INSAFORP)
- **Income-tax legislation** — Ley de Impuesto sobre la Renta
- **Health/SS authority** — Instituto Salvadoreño del Seguro Social (ISSS, www.isss.gob.sv)
- **Pension authority** — AFPs supervised by the Superintendencia del Sistema Financiero (SSF, www.ssf.gob.sv)
- **Training authority** — Instituto Salvadoreño de Formación Profesional (INSAFORP)
- **Income-tax authority** — Ministerio de Hacienda (www.mh.gob.sv)
- **ISSS employee rate** — 3% of monthly salary, contributory base capped at USD 1,000/month (max USD 30.00/month)  _([PwC; ISSS Reglamento Art. 3])_
- **ISSS employer rate** — 7.5% of monthly salary, contributory base capped at USD 1,000/month (max USD 75.00/month)  _([PwC; ISSS Reglamento Art. 3])_
- **AFP employee rate** — 7.25% of the Ingreso Base de Cotización (full salary), no USD 1,000-style cap  _([PwC; AFP Crecer])_
- **AFP employer rate** — 8.75% of the Ingreso Base de Cotización (full salary)  _([PwC; AFP Crecer])_
- **AFP total system rate** — 16% (7.25% + 8.75%)  _([AFP Crecer; EY])_
- **AFP maximum contributory salary** — ~USD 7,045.06/month (2026 figure; periodically updated by SSF) [RESEARCH GAP — reviewer to confirm exact effective amount/date against current SSF/AFP publication]  _([AFP Crecer; EY])_
- **INSAFORP training levy** — 1% of total payroll, employer-only, for private employers with 10+ employees (0.25% for permanent agricultural workers)  _([The Central American Group; Ley de Formación Profesional])_
- **Resident PIT** — Progressive 0% / 10% / 20% / 30% on annual net income (see Section 5)  _([PwC])_
- **Non-resident PIT** — 30% flat on Salvadoran-source income  _([PwC])_
- **Annual income-tax return** — Form F-11, due 30 April following the tax year  _([Ministerio de Hacienda; PwC])_
- **ISSS/AFP filing** — Monthly — ISSS via OVISSS, AFP via SSF/AFP electronic planilla, due early the following month  _([ISSS OVISSS; SSF])_
- **Validated by** — Pending — requires sign-off by a Salvadoran licensed accountant / contador público
- **Validation date** — Pending

**Contribution overview (monthly, per worker)**

| Branch | Employee | Employer | Base / cap |
| --- | --- | --- | --- |
| ISSS (health/sickness/maternity) | 3% | 7.5% | Salary, contributory base capped at USD 1,000/mo [PwC; ISSS Reglamento Art. 3] |
| AFP (pension) | 7.25% | 8.75% | Ingreso Base de Cotización (full salary), SSF max contributory base ~USD 7,045.06/mo **[RESEARCH GAP — confirm cap]** [PwC; AFP Crecer] |
| INSAFORP (training) | — | 1% of total payroll (0.25% permanent agric.) | Employer-only, 10+ employees, no salary cap [The Central American Group] |
| **Statutory total on worker pay** | **10.25%** (3% + 7.25%) | **16.25%** (7.5% + 8.75%) before INSAFORP | — |

Arithmetic check. Employee column: 3% + 7.25% = 10.25% ✓. Employer column (excl. INSAFORP, which is on total payroll not the individual cap base): 7.5% + 8.75% = 16.25% ✓. AFP system total: 7.25% + 8.75% = 16% ✓.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Employee earning above USD 1,000/month | ISSS employee = USD 30.00 fixed, ISSS employer = USD 75.00 fixed (cap reached) [PwC; ISSS Reglamento Art. 3] |
| AFP for any salary | 7.25% employee + 8.75% employer on full Ingreso Base de Cotización, no USD 1,000-style cap; only the high SSF max-contributory base applies [PwC; AFP Crecer] |
| Employer with fewer than 10 employees | No INSAFORP 1% levy [The Central American Group] |
| Total typical employee statutory deductions | ISSS 3% (max USD 30) + AFP 7.25% + income-tax withholding per tables [PwC] |
| Unknown salary | STOP — cannot compute ISSS/AFP/withholding without the monthly gross |
| Unknown headcount (for INSAFORP) | Ask — do not assume the 1% levy applies until 10+ employees confirmed |
| Unknown residency (for PIT) | Ask — resident progressive vs non-resident 30% flat differ materially |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Minimum viable -- monthly gross salary (in USD) and whether the worker is the employee or you are computing the employer cost. Without the gross, STOP. Do not compute ISSS, AFP, or withholding.

Recommended -- residency/domicile status (for PIT), employer headcount (for INSAFORP), sector (Industry/Commerce/Services vs textile maquila vs agriculture, for minimum-wage checks), and the AFP the worker is enrolled in.

Ideal -- ISSS planilla (OVISSS) extract, AFP planilla previsional extract, prior-year Form F-11, and bank statements showing the monthly ISSS/AFP/INSAFORP debits and income-tax withholding remittances.

### Refusal catalogue

- **R-SV-SOC-1 -- Salary not provided** — Trigger: monthly gross salary not given. Message: "Monthly gross salary in USD is mandatory. ISSS (3%/7.5% capped at a USD 1,000 base), AFP (7.25%/8.75% on full salary), and income-tax withholding all key off the monthly gross. Cannot proceed without it."
- **R-SV-SOC-2 -- AFP maximum contributory base** — Trigger: salary exceeds, or is near, the SSF maximum contributory salary (~USD 7,045.06/month). Message: "Above the SSF maximum contributory salary, AFP contributions are computed on the capped base, not full salary. The exact cap (~USD 7,045.06/month for 2026) is set periodically by the SSF and must be re-verified directly against the current SSF/AFP publication before computing. Flag for reviewer." [RESEARCH GAP — reviewer to confirm cap]  _([AFP Crecer; EY])_
- **R-SV-SOC-3 -- ISSS/AFP arrears or penalties** — Trigger: unpaid ISSS or AFP contributions from prior months. Message: "ISSS late-payment surcharges (5% up to 15 days late, 10% beyond) and the failure-to-file fine (25% of contributions due, min USD 10, max USD 500) compound, and persistent delinquency is enforced via an executive-title certification (título ejecutivo) by the ISSS Director General. Do not quantify arrears without the ISSS statement; escalate to a Salvadoran accountant."  _([ISSS Reglamento])_
- **R-SV-SOC-4 -- Non-resident / cross-border worker** — Trigger: worker is non-resident, non-domiciled, or seconded. Message: "Non-resident / non-domiciled individuals pay a flat 30% on Salvadoran-source income, and social-security coverage may differ. This requires case-specific confirmation. Escalate to a Salvadoran accountant."  _([PwC])_
- **R-SV-SOC-5 -- INSAFORP threshold / sector ambiguity** — Trigger: unclear whether the employer has 10+ employees, or whether agricultural 0.25% rate applies. Message: "INSAFORP's 1% levy (0.25% for permanent agricultural workers) applies to private employers with 10 or more employees. The threshold and agricultural carve-out come from secondary advisory sources; confirm against the Ley de Formación Profesional before applying." [RESEARCH GAP — confirm against statute]  _([The Central American Group])_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to Salvadoran payroll and social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

How to read this table. Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statutory employee contributions (ISSS, AFP) withheld from pay and remitted are NOT business supplies; employer contributions and the INSAFORP levy are payroll costs (deductible employer expenses), not VAT-bearing supplies. None of these belong on a VAT/IVA return as input or output tax.

### 3.1 ISSS contributions (health / sickness / maternity)

**ISSS contributions patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ISSS, INSTITUTO SALVADOREÑO DEL SEGURO SOCIAL | EXCLUDE from VAT — ISSS contribution remittance | Monthly planilla (employee 3% + employer 7.5%, capped) |
| SEGURO SOCIAL, COTIZACION ISSS | EXCLUDE from VAT — ISSS contribution | Same |
| OVISSS, PLANILLA ISSS | EXCLUDE from VAT — ISSS contribution | Electronic planilla payment |

### 3.2 AFP pension contributions

**AFP pension contributions patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AFP, AFP CRECER, AFP CONFIA, AFP CONFÍA | EXCLUDE from VAT — AFP pension remittance | Monthly planilla previsional (employee 7.25% + employer 8.75%) |
| COTIZACION PREVISIONAL, PLANILLA PREVISIONAL | EXCLUDE from VAT — AFP pension | Same |
| PENSIONES, SAP (Sistema de Ahorro para Pensiones) | EXCLUDE from VAT — AFP pension | Same |

### 3.3 INSAFORP training levy

**INSAFORP training levy patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSAFORP | EXCLUDE from VAT — employer training levy | 1% of total payroll, employer-only, 10+ employees |
| FORMACION PROFESIONAL, FORMACIÓN PROFESIONAL | EXCLUDE from VAT — training levy | Same |

### 3.4 Income-tax withholding and Ministerio de Hacienda (NOT a social contribution)

**Income-tax patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MINISTERIO DE HACIENDA, MH | EXCLUDE from VAT — income tax, not social security | Income-tax remittance / withholding |
| RETENCION RENTA, RETENCIÓN DE RENTA, ISR | EXCLUDE from VAT — income-tax withholding | Monthly retención per MH tables |
| DGII, DECLARACION F-11, F-11 | EXCLUDE from VAT — income-tax filing | Annual income-tax return |

### 3.5 Salary and payroll (exclude from contribution classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, PLANILLA SUELDOS (outgoing) | EXCLUDE from VAT — payroll/wage expense | Not a contribution remittance |
| SALARIO, SUELDO (incoming) | EXCLUDE from VAT — employment income received | Not a contribution remittance |
| AGUINALDO (Dec) | EXCLUDE from VAT — statutory Christmas bonus expense | Payroll cost, not a contribution |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical Salvadoran SME (a software services firm, Industry/Commerce/Services sector) and its employees. All amounts in USD.

### Example 1 -- Mid-range employee deductions ($600/month)

Input line:
`30.06.2025 ; PLANILLA SUELDOS JUNIO ; DEBIT ; EMPLEADO J. PEREZ ; -600.00 ; USD`

Reasoning (employee statutory deductions on USD 600 gross):
- ISSS employee: 3% × 600 = USD 18.00 (under the USD 1,000 cap) [PwC; ISSS Reglamento Art. 3]
- AFP employee: 7.25% × 600 = USD 43.50 [PwC; AFP Crecer]
- Income-tax withholding: the ISR base is salary net of AFP and ISSS = 600.00 − 18.00 − 43.50 = 538.50, which is ≤ 550.00 → Tramo I → USD 0.00 retención [Ministerio de Hacienda; the retención base = gross − AFP − ISSS employee contributions]
- Total deductions: 18.00 + 43.50 + 0.00 = USD 61.50
- Net pay: 600.00 − 61.50 = USD 538.50

Classification: Gross salary is a payroll expense (EXCLUDE from VAT). The withheld ISSS/AFP/ISR amounts are remitted to ISSS, the AFP, and Ministerio de Hacienda respectively.

### Example 2 -- High earner above the ISSS cap ($1,500/month)

Input line:
`31.07.2025 ; PLANILLA SUELDOS JULIO ; DEBIT ; EMPLEADO M. RIVAS ; -1,500.00 ; USD`

Reasoning (employee deductions on USD 1,500 gross):
- ISSS employee: capped — 3% × 1,000 = USD 30.00 (salary exceeds the USD 1,000 contributory base) [PwC; ISSS Reglamento Art. 3]
- AFP employee: 7.25% × 1,500 = USD 108.75 (no USD 1,000-style cap; under the SSF max base) [PwC; AFP Crecer]
- Income-tax withholding: 1,500 in 895.25–2,038.10 → 60.00 + 20%×(1,500 − 895.24) = 60.00 + 120.95 = USD 180.95 [PwC]
- Total deductions: 30.00 + 108.75 + 180.95 = USD 319.70
- Net pay: 1,500.00 − 319.70 = USD 1,180.30

Classification: EXCLUDE from VAT. Note the ISSS cap bites at USD 30.00 while AFP keeps rising with salary.

### Example 3 -- Employer monthly social cost for the $1,500 employee (10+ staff)

Input line:
`05.08.2025 ; AFP CRECER PLANILLA PREVISIONAL JUL ; DEBIT ; ; -131.25 ; USD`

Reasoning (employer cost on USD 1,500 gross, firm has 10+ employees):
- ISSS employer: capped — 7.5% × 1,000 = USD 75.00 [PwC; ISSS Reglamento Art. 3]
- AFP employer: 8.75% × 1,500 = USD 131.25 (this line) [PwC; AFP Crecer]
- INSAFORP: 1% × 1,500 = USD 15.00 (employer has 10+ employees) [The Central American Group]
- Total employer social cost: 75.00 + 131.25 + 15.00 = USD 221.25

Classification: Each remittance EXCLUDE from VAT; all three are deductible employer payroll costs. This bank line matches AFP pattern 3.2 (USD 131.25 = the AFP employer portion).

### Example 4 -- ISSS planilla remittance (OVISSS)

Input line:
`08.07.2025 ; ISSS OVISSS PLANILLA JUN ; DEBIT ; COTIZACION SEGURO SOCIAL ; -105.00 ; USD`

Reasoning:
Matches "ISSS" / "OVISSS" (pattern 3.1). For the USD 1,500 employee, ISSS employee USD 30.00 + ISSS employer USD 75.00 = USD 105.00 total ISSS for the month. Filed monthly via OVISSS, due early the following month. [ISSS OVISSS]

Classification: EXCLUDE from VAT — ISSS contribution remittance (combined employee + employer).

### Example 5 -- Income-tax withholding remittance (NOT a social contribution)

Input line:
`10.08.2025 ; MINISTERIO DE HACIENDA RETENCION RENTA JUL ; DEBIT ; ISR ; -180.95 ; USD`

Reasoning:
Matches "MINISTERIO DE HACIENDA" / "RETENCION RENTA" (pattern 3.4). This is the income-tax (ISR) withheld from the USD 1,500 employee (USD 180.95 from Example 2), remitted to Ministerio de Hacienda. It is NOT an ISSS or AFP social contribution — do not classify it as social security. [PwC]

Classification: EXCLUDE from VAT — income-tax withholding. NOT a social contribution.

### Example 6 -- Minimum-wage employee, low deductions, no income tax

Input line:
`30.06.2025 ; PLANILLA SUELDOS JUNIO ; DEBIT ; EMPLEADO A. GOMEZ ; -408.80 ; USD`

Reasoning (Industry/Commerce/Services minimum wage USD 408.80/month, effective 1 Jun 2025):
- ISSS employee: 3% × 408.80 = USD 12.26 [PwC; ISSS Reglamento Art. 3]
- AFP employee: 7.25% × 408.80 = USD 29.64 [PwC; AFP Crecer]
- Income-tax withholding: 408.80 is below the USD 550 monthly nil band → USD 0.00 [PwC]
- Total deductions: 12.26 + 29.64 + 0.00 = USD 41.90
- Net pay: 408.80 − 41.90 = USD 366.90

Classification: EXCLUDE from VAT. Confirm the worker is paid at least the applicable sector minimum wage (USD 408.80 Industry/Commerce/Services; USD 402.26 textile maquila; USD 272.72 agriculture, all effective 1 Jun 2025) [MTPS official].

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- ISSS health contribution (employee 3% / employer 7.5%, capped)

- **ISSS formula** — ISSS_base      = min(monthly_salary, 1000.00) ISSS_employee  = ISSS_base × 3%      # practical max USD 30.00 ISSS_employer  = ISSS_base × 7.5%    # practical max USD 75.00 The contributory base is capped at USD 1,000/month, so the practical monthly maximums are USD 30.00 (employee) and USD 75.00 (employer).  _([PwC; ISSS Reglamento Art. 3])_

### Rule 2 -- AFP pension contribution (employee 7.25% / employer 8.75%, no USD-1,000 cap)

- **AFP formula** — AFP_base      = min(monthly_salary, SSF_max_contributory_salary)   # ~USD 7,045.06/mo (2026) — confirm AFP_employee  = AFP_base × 7.25% AFP_employer  = AFP_base × 8.75% AFP_total     = AFP_base × 16% AFP is on the Ingreso Base de Cotización (full salary). There is NO USD 1,000-style cap — the old USD salary cap was eliminated in January 2023. A separate, high SSF maximum contributory salary (~USD 7,045.06/month for 2026) applies and is updated periodically by the SSF. [RESEARCH GAP — reviewer to confirm exact cap amount and effective date against current SSF/AFP publication]  _([PwC; AFP Crecer; EY])_

### Rule 3 -- AFP 16% allocation (post-2022 reform)

- **AFP 16% component allocation** — Of the 16% AFP total, roughly 9% to the worker's individual account, ~6% to the Solidarity Guarantee Fund (CGS), and ~1% to the AFP commission (which now includes disability/survivors insurance). The AFP commission was cut from 1.9% to 1% under the Dec 2022 reform effective Jan 2023. These component figures are approximate. [RESEARCH GAP — component split is approximate; reviewer to confirm exact allocation]  _([EY pension-law alert; SSA])_

### Rule 4 -- INSAFORP training levy (employer-only, 10+ employees)

- **INSAFORP formula** — if employees >= 10: INSAFORP = total_payroll × 1%          # 0.25% for permanent agricultural workers else: INSAFORP = 0 Paid by the EMPLOYER ONLY, applicable to private employers with 10 or more employees, no salary cap. [RESEARCH GAP — threshold/agricultural rate from secondary sources; confirm against statute]  _([The Central American Group; Ley de Formación Profesional])_

### Rule 5 -- Resident personal income tax (progressive, annual net income)

**Resident PIT table**

| Annual net income (USD) | Tax |
| --- | --- |
| 0 – 6,600.00 | 0% (exempt) [PwC] |
| 6,600.01 – 10,742.86 | USD 212.12 + 10% on excess over 6,600.00 [Decreto Ejecutivo 10/2025] |
| 10,742.87 – 24,457.14 | USD 720.00 + 20% on excess over 10,742.86 [Decreto Ejecutivo 10/2025] |
| 24,457.15 and over | USD 3,462.86 + 30% on excess over 24,457.14 [Decreto Ejecutivo 10/2025] |

Note (reformed table — Decreto Ejecutivo 10, in force 8 May 2025). Cuotas fijas (212.12 / 720.00 / 3,462.86) are statutory fixed amounts at the band floors 6,600 / 10,742.86 / 24,457.14. The table is intentionally NOT fully continuous: the $212.12 is a step at the exempt threshold, and band 2→3 steps up from 626.41 (= 212.12 + 10%×(10,742.86 − 6,600)) to the 720.00 band-3 base. Band 3→4 is continuous (720.00 + 20%×(24,457.14 − 10,742.86) = 3,462.86). [Diario El Mundo; Contaportable; Decreto Ejecutivo 10]

### Rule 6 -- Non-resident / non-domiciled PIT

- **Non-resident PIT** — Non-resident / non-domiciled individuals pay a flat 30% on Salvadoran-source income.  _([PwC])_

### Rule 7 -- Monthly income-tax withholding tables (retención)

**Monthly withholding table**

| Monthly taxable pay (USD) — = gross − AFP − ISSS employee contributions | Withholding |
| --- | --- |
| 0 – 550.00 | Nil [PwC] |
| 550.01 – 895.24 | USD 17.67 + 10% on excess over 550.00 [Decreto Ejecutivo 10/2025] |
| 895.25 – 2,038.10 | USD 60.00 + 20% on excess over 895.24 [PwC] |
| 2,038.11 and over | USD 288.57 + 30% on excess over 2,038.10 [PwC] |

Note. Monthly cuotas fijas (17.67 / 60.00 / 288.57) mirror the annual table ÷ 12. As with the annual table there is a small step at the $895.24 boundary (the 10% progression reaches 52.19 vs the $60.00 band-3 base). At 2,038.10: 60.00 + 20%×(2,038.10 − 895.24) = 288.57 ✓ (continuous from band 3). [Decreto Ejecutivo 10/2025]

The employer withholds monthly per the Ministerio de Hacienda tables; the employee reconciles annually on Form F-11. [PwC]

### Rule 8 -- Annual income-tax return (Form F-11)

- **Form F-11 filing** — The annual individual income-tax return is Form F-11, filed with Ministerio de Hacienda by 30 April following the tax year (e.g., 30 Apr 2026 for FY2025), 11:59pm.  _([Ministerio de Hacienda; PwC])_

### Rule 9 -- Monthly contribution filing channels

- **Filing channels** — ISSS contributions are declared/paid monthly via the OVISSS platform; AFP contributions via the SSF/AFP electronic planilla previsional per the SSF monthly calendar. Both are due early the following month.  _([ISSS OVISSS; SSF])_

### Rule 10 -- Minimum wages (effective 1 June 2025, +12%)

**Minimum wages table**

| Sector | Monthly minimum |
| --- | --- |
| Industry / Commerce / Services | USD 408.80 [MTPS official; Consortium Legal] |
| Textile / clothing maquila | USD 402.26 [MTPS / official gazette] |
| Agriculture | USD 272.72 [MTPS / official gazette] |

- **Publication date** — Published in the Official Gazette 23 May 2025; unchanged for 2026.  _([MTPS official])_

### Rule 11 -- ISSS late-payment surcharge

- **Late-payment surcharge** — 5% surcharge if up to 15 days late; 10% if more than 15 days late — on the monthly contribution. [RESEARCH GAP — penalty figures from a Spanish secondary summary of the Reglamento; confirm against official text]  _([ISSS Reglamento])_

### Rule 12 -- ISSS failure-to-file fine

- **Failure-to-file fine** — Fine = 25% of contributions due, minimum USD 10.00, maximum USD 500.00; persistent delinquency is enforced via an executive-title certification (título ejecutivo) issued by the ISSS Director General, enabling forced collection plus interest. [RESEARCH GAP — confirm against official Reglamento]  _([ISSS Reglamento])_

### Rule 13 -- Corporate income tax (context only — not a social contribution)

- **Corporate income tax** — Corporate income tax is 30% standard, reduced to 25% where annual taxable income is USD 150,000 or less. Included for completeness; it is not a payroll contribution.  _([PwC])_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Salary above the SSF maximum contributory base

Trigger: monthly salary exceeds, or is near, ~USD 7,045.06/month.

Issue: AFP contributions are computed on the capped base, not full salary. The exact SSF maximum is administratively variable and was sourced as a 2026 figure from an AFP administrator and a secondary site. PwC describes AFP as having "no ceiling," reflecting the elimination of the old USD-cap in Jan 2023, so the high SSF max-contributory base is a separate, evolving parameter.

Action: Re-verify the cap against the current SSF/AFP publication. Flag for reviewer. [RESEARCH GAP]

### T2-2 -- INSAFORP threshold and agricultural rate

Trigger: employer near the 10-employee threshold, or with permanent agricultural workers.

Issue: The 1% levy applies at 10+ employees (0.25% for permanent agricultural workers). The threshold and carve-out come from secondary advisory sources, not a directly-fetched INSAFORP statute page.

Action: Confirm against the Ley de Formación Profesional before applying. Flag for reviewer. [RESEARCH GAP]

### T2-3 -- Multiple employers / split contributions

Trigger: worker holds more than one job, or income from multiple employers.

Issue: ISSS and AFP caps/bases interact across employers; the ISSS USD 1,000 base and the SSF AFP cap may need aggregation. Annual F-11 reconciliation may change the final income-tax position versus monthly withholding.

Action: Flag for reviewer to confirm aggregation and F-11 reconciliation.

### T2-4 -- ISSS / AFP arrears and penalties

Trigger: unpaid ISSS or AFP contributions from prior months.

Issue: ISSS surcharges (5%/10%), the failure-to-file fine (25%, min USD 10 / max USD 500), and executive-title enforcement compound. AFP arrears carry their own SSF enforcement.

Action: Do not quantify arrears without the ISSS/AFP statements. Escalate to a Salvadoran accountant immediately.

### T2-5 -- Residency / domicile for income tax

Trigger: worker may be non-resident or non-domiciled.

Issue: Residents pay progressive PIT (0%–30%); non-residents pay a flat 30% on Salvadoran-source income. Withholding mechanics differ.

Action: Flag for reviewer to confirm residency before applying brackets.

### T2-6 -- AFP 16% component allocation

Trigger: client asks how the 16% AFP is split (individual account vs CGS vs commission).

Issue: The 9%/6%/1% split is approximate, based on EY/SSA descriptions of the post-2022 reform; the AFP commission now bundles disability/survivors insurance.

Action: Flag for reviewer; do not present the split as exact. [RESEARCH GAP]

## Section 7 -- Excel working paper template

When producing an El Salvador payroll-contribution computation, structure the working paper as follows:

```
EL SALVADOR PAYROLL CONTRIBUTIONS -- WORKING PAPER
Client / Employer: [name]
Worker:            [name]
Tax Year:          [year]
Prepared:          [date]

INPUT DATA
  Monthly gross salary (USD):       [____]
  Sector (Ind/Comm/Svc / maquila / agric): [____]
  Residency (resident / non-resident):     [____]
  Employer headcount (for INSAFORP):        [____]
  AFP administrator:                        [____]

ISSS (health) — base capped at USD 1,000
  ISSS base = min(salary, 1,000):   USD [____]
  Employee 3%  (max 30.00):         USD [____]
  Employer 7.5% (max 75.00):        USD [____]

AFP (pension) — base capped at SSF max (~7,045.06) [confirm]
  AFP base = min(salary, SSF_max):  USD [____]
  Employee 7.25%:                   USD [____]
  Employer 8.75%:                   USD [____]
  AFP total 16%:                    USD [____]

INSAFORP (employer-only, 10+ employees)
  1% of total payroll (0.25% agric): USD [____]

INCOME-TAX WITHHOLDING (monthly table)
  Monthly taxable pay:              USD [____]
  Withholding per MH table:         USD [____]

NET PAY
  Gross:                            USD [____]
  Less ISSS employee:               USD [____]
  Less AFP employee:                USD [____]
  Less income-tax withholding:      USD [____]
  Net pay:                          USD [____]

EMPLOYER SOCIAL COST (this worker)
  ISSS employer + AFP employer + INSAFORP share: USD [____]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How Salvadoran payroll/social debits appear on bank statements

Banco Agrícola / Banco Cuscatlán / Davivienda / BAC Credomatic:
- ISSS: "ISSS", "SEGURO SOCIAL", "OVISSS", "COTIZACION ISSS"
- AFP: "AFP CRECER", "AFP CONFIA", "PLANILLA PREVISIONAL", "COTIZACION PREVISIONAL"
- INSAFORP: "INSAFORP", "FORMACION PROFESIONAL"
- Income tax: "MINISTERIO DE HACIENDA", "RETENCION RENTA", "ISR", "F-11"
- Payroll: "PLANILLA", "SUELDOS", "SALARIO", "AGUINALDO" (December bonus)

Timing:
1. ISSS and AFP planilla remittances are monthly, due early the following month.
2. Income-tax withholding remittances are monthly to Ministerio de Hacienda.
3. The annual F-11 income-tax payment (if any) lands around the 30 April deadline.
4. Aguinaldo (statutory Christmas bonus) typically appears in December.

Key identification tips:
1. ISSS and AFP debits are outgoing (DEBIT) remittances, never the worker's pension/benefit credits.
2. ISSS amounts plateau once salary exceeds USD 1,000 (employee USD 30, employer USD 75); AFP amounts keep rising with salary.
3. Do not confuse Ministerio de Hacienda / RETENCION RENTA (income tax) debits with ISSS/AFP (social contributions).
4. Pension benefits RECEIVED are credits, not contributions — do not classify them as payments.
5. All amounts are in USD.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. Scan for ISSS debits -- match Section 3.1 patterns. ISSS employee USD 30 + employer USD 75 = USD 105/worker/month signals a salary at or above the USD 1,000 cap; lower means salary below the cap (back out salary = ISSS / 0.105 for the combined 10.5% rate, approximately).
2. Scan for AFP debits -- match Section 3.2. AFP total = 16% of salary; back out salary = AFP_total / 0.16 (subject to the SSF max base).
3. Scan for INSAFORP debits -- match Section 3.3. Presence implies 10+ employees; INSAFORP / 0.01 ≈ total payroll.
4. Scan for income-tax withholding -- match Section 3.4 (Ministerio de Hacienda / RETENCION RENTA). This is income tax, not a contribution.
5. Flag for reviewer: "Contribution classification derived from bank-statement amounts only. Salaries, headcount, residency, and the SSF AFP cap have not been independently verified. Reviewer must confirm before relying on these figures or filing F-11."

### Calculation examples (2025 figures)

**Calculation examples (2025 figures)**  _([PwC; AFP Crecer; ISSS Reglamento Art. 3])_

| Monthly gross (USD) | ISSS ee (3%, cap) | AFP ee (7.25%) | Withholding | Net pay |
| --- | --- | --- | --- | --- |
| 408.80 (min wage) | 12.26 | 29.64 | 0.00 | 366.90 |
| 600.00 | 18.00 | 43.50 | 0.00 | 538.50 |
| 1,000.00 | 30.00 | 72.50 | 80.95 | 816.55 |
| 1,500.00 | 30.00 (cap) | 108.75 | 180.95 | 1,180.30 |

> Source for all rates: [PwC; AFP Crecer; ISSS Reglamento Art. 3]. Withholding per the monthly MH table [PwC]. USD 1,000 row check: ISSS ee 3%×1,000 = 30.00; AFP ee 7.25%×1,000 = 72.50; withholding (895.25–2,038.10): 60.00 + 20%×(1,000 − 895.24) = 60.00 + 20.95 = 80.95; net = 1,000 − 30 − 72.50 − 80.95 = **816.55** ✓.

### Employer-cost examples (2025 figures)

**Employer-cost examples (2025 figures)**  _([PwC; AFP Crecer; The Central American Group])_

| Monthly gross (USD) | ISSS er (7.5%, cap) | AFP er (8.75%) | INSAFORP (1%, 10+ staff) | Employer total |
| --- | --- | --- | --- | --- |
| 408.80 | 30.66 | 35.77 | 4.09 | 70.52 |
| 1,000.00 | 75.00 | 87.50 | 10.00 | 172.50 |
| 1,500.00 | 75.00 (cap) | 131.25 | 15.00 | 221.25 |

> Source: [PwC; AFP Crecer; The Central American Group]. USD 1,500 row check: 75.00 + 131.25 + 15.00 = **221.25** ✓.

### Thresholds

**Thresholds**  _([PwC])_

| Label | Value | Source |
| --- | --- | --- |
| PIT exemption threshold | USD 6,600.00 annual net income (resident) | [PwC] |
| ISSS contributory salary ceiling | USD 1,000.00/month | [PwC; ISSS Reglamento Art. 3] |
| AFP maximum contributory salary (tope) | ~USD 7,045.06/month (2026; periodically updated) **[RESEARCH GAP — confirm]** | [AFP Crecer; EY] |
| INSAFORP levy threshold | 10 or more employees | [The Central American Group] **[RESEARCH GAP — confirm against statute]** |
| Reduced CIT threshold | taxable income ≤ USD 150,000 → 25% (else 30%) | [PwC] |

### Forms

**Forms**  _([Ministerio de Hacienda; PwC])_

| Form | Purpose | Deadline | Authority | Source |
| --- | --- | --- | --- | --- |
| F-11 — Declaración del Impuesto sobre la Renta (persona natural) | Annual individual income-tax return | 30 April following the tax year (e.g. 30 Apr 2026 for FY2025), 11:59pm | Ministerio de Hacienda | [Ministerio de Hacienda; PwC] |
| ISSS monthly contribution payroll (planilla OVISSS) | Declare/pay monthly ISSS employee + employer | Monthly, early the following month | ISSS | [ISSS OVISSS] |
| AFP monthly pension payroll (planilla previsional) | Declare/pay monthly AFP contributions | Monthly per SSF calendar | AFP / SSF | [SSF cotizaciones previsionales 2025] |

### Penalties

**Penalties**  _([ISSS Reglamento])_

| Penalty | Amount | Source |
| --- | --- | --- |
| ISSS late payment — up to 15 days late | 5% surcharge on the monthly contribution | [ISSS Reglamento] **[RESEARCH GAP]** |
| ISSS late payment — more than 15 days late | 10% surcharge on the monthly contribution | [ISSS Reglamento] **[RESEARCH GAP]** |
| ISSS failure to submit payroll | 25% of contributions due, min USD 10.00, max USD 500.00 | [ISSS Reglamento] **[RESEARCH GAP]** |
| ISSS delinquency | Executive-title (título ejecutivo) certification by Director General → forced collection plus interest | [ISSS / jurisprudencia.gob.sv] |

### Test suite

**Test 1:** Employee, gross USD 600. ISSS ee 3%×600 = 18.00; AFP ee 7.25%×600 = 43.50; ISR base = 600 − 18 − 43.50 = 538.50 ≤ 550 → retención 0.00; total 61.50. → **Net pay USD 538.50.**

**Test 2:** Employee, gross USD 1,500. ISSS ee capped 30.00; AFP ee 7.25%×1,500 = 108.75; withholding (895.25–2,038.10) 60.00 + 20%×(1,500 − 895.24) = 180.95; total 319.70. → **Net pay USD 1,180.30.**

**Test 3:** Employer cost, gross USD 1,500, 10+ staff. ISSS er capped 75.00 + AFP er 8.75%×1,500 = 131.25 + INSAFORP 1%×1,500 = 15.00. → **Employer total USD 221.25.**

**Test 4:** Minimum-wage employee (Industry/Commerce/Services), gross USD 408.80. ISSS ee 12.26 + AFP ee 29.64 + withholding 0.00 (below USD 550). → **Net pay USD 366.90.**

**Test 5:** Resident, annual net income USD 18,000 (F-11). Band 3 (10,742.87–24,457.14): 720.00 + 20%×(18,000 − 10,742.86) = 720.00 + 1,451.43 = **USD 2,171.43 tax due.**

**Test 6:** Resident, annual net income USD 6,600. Band 1 exempt. → **USD 0.00 tax due.**

**Test 7:** Resident, annual net income USD 30,000. Band 4 (24,457.15+): 3,462.86 + 30%×(30,000 − 24,457.14) = 3,462.86 + 1,662.86 = **USD 5,125.72 tax due.**

**Test 8:** Non-resident, Salvadoran-source income USD 30,000. Flat 30% → **USD 9,000.00 tax due.**

**Test 9:** Employer with 6 employees. INSAFORP threshold (10+) not met. → **INSAFORP USD 0.00.**

**Test 10:** Employee, gross USD 1,000 (exactly at ISSS cap). ISSS ee 3%×1,000 = 30.00; AFP ee 7.25%×1,000 = 72.50; withholding (895.25–2,038.10) 60.00 + 20%×(1,000 − 895.24) = 80.95; total 183.45. → **Net pay USD 816.55.**

### Prohibitions

- **Never compute without gross salary** — NEVER compute ISSS, AFP, or withholding without knowing the monthly gross salary in USD.  _([ISSS Reglamento Art. 3])_
- **Never apply ISSS cap to AFP** — NEVER apply a USD 1,000 cap to AFP — that cap is ISSS-only; AFP is on full salary up to the (separate, high) SSF maximum contributory base.  _([AFP Crecer; EY])_
- **Never omit ISSS cap** — NEVER omit the ISSS USD 1,000 cap — above it, ISSS is fixed at USD 30 (employee) / USD 75 (employer).  _([PwC; ISSS Reglamento Art. 3])_
- **Never apply INSAFORP under 10 employees** — NEVER apply the INSAFORP 1% levy to an employer with fewer than 10 employees.  _([The Central American Group])_
- **Never conflate withholding with social contribution** — NEVER treat income-tax withholding (Ministerio de Hacienda / RETENCION RENTA) as a social contribution, or vice versa.  _([Ministerio de Hacienda; PwC])_
- **Never apply resident brackets to non-resident** — NEVER apply resident progressive brackets to a non-resident — non-residents pay a flat 30%.  _([PwC])_
- **Never confirm AFP max base without re-verifying** — NEVER quote the SSF AFP maximum contributory base as definitive without re-verifying the current figure — it is a RESEARCH GAP.  _([AFP Crecer; EY])_
- **Never quantify arrears without official statement** — NEVER quantify ISSS/AFP arrears or penalties without the official statement — escalate to a Salvadoran accountant.  _([ISSS / jurisprudencia.gob.sv])_
- **Never present research gap figures as confirmed** — NEVER present any figure marked [RESEARCH GAP] as confirmed — surface the caveat to the reviewer.  _([AFP Crecer; EY])_
- **Never assume Bitcoin replaced USD** — NEVER assume USD has been replaced by Bitcoin — Bitcoin's forced-tender status was repealed in 2025; USD is the accounting/contribution currency.  _([PwC])_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, contador público, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
