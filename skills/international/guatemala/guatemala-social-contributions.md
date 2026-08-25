---
name: guatemala-social-contributions
description: Use this skill whenever asked about Guatemala social-security contributions (IGSS) and payroll income-tax withholding (ISR sobre rentas del trabajo) for employees and employers. Trigger on phrases like "how much IGSS do I pay", "cuota laboral", "cuota patronal", "IGSS employee rate", "IGSS employer rate", "INTECAP IRTRA", "Guatemala payroll deductions", "ISR retencion empleados", "ISR planilla", "salario minimo Guatemala", "bonificacion incentivo", "Q250 bono", "constancia de retencion", "SAT-1331", "crédito por IVA planilla", or any question about Guatemalan payroll, social contributions, or employee income-tax withholding. Also trigger when classifying bank statement transactions that relate to IGSS debits, INTECAP/IRTRA levies, or SAT income-tax payments from Banco Industrial, Banrural, BAM, G&T Continental, or other Guatemalan banks. This skill covers the 15.50% combined IGSS split (4.83% employee / 10.67% employer + 2% parafiscal), the Q250 bonificación incentivo, the 2026 minimum wage, ISR brackets and deductions (including the Decreto 13-2026 reform), forms, deadlines, penalties, bank-statement classification, and edge cases. ALWAYS read this skill before touching any Guatemalan payroll or IGSS work.
version: 0.1
jurisdiction: GT
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Guatemala Social Contributions (IGSS) & Payroll Income Tax (ISR)

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Guatemala (República de Guatemala) |
| Currency | Quetzal (Q / GTQ) only |
| Contribution / tax year | Calendar year (1 Jan -- 31 Dec) |
| Social-security authority | IGSS -- Instituto Guatemalteco de Seguridad Social (igssgt.org/cuotas) |
| Tax authority | SAT -- Superintendencia de Administración Tributaria (portal.sat.gob.gt) |
| Social-security legislation | Ley Orgánica del IGSS; Acuerdos Junta Directiva IGSS (Acuerdo 1118; Acuerdo 1529) |
| Income-tax legislation | Ley de Actualización Tributaria, Decreto 10-2012 (ISR); Código Tributario, Decreto 6-91 (penalties); Decreto 13-2026 (2026 reform) |
| IGSS employee total (cuota laboral) | 4.83% of ordinary salary (igssgt.org/cuotas) |
| IGSS employer total (cuota patronal) | 10.67% IGSS + 1% INTECAP + 1% IRTRA = 12.67% (igssgt.org / FUNDESA / Prensa Libre) |
| Combined IGSS (ee + er, IGSS only) | 15.50% (Banco Industrial 2026) |
| Contribution base | Ordinary salary, EXCLUDING the Q250 bonificación incentivo (Decreto 37-2001) |
| Employer IGSS registration threshold | 1 or more workers since 17 Jan 2023 (Acuerdo Junta Directiva 1529) |
| ISR bracket 1 | 5% on annual taxable income up to Q300,000 (Decreto 10-2012; SAT) |
| ISR bracket 2 | Q15,000 fixed + 7% on the excess over Q300,000 (Decreto 10-2012; SAT) |
| ISR fixed personal deduction | Q48,000/year (≈ Q4,000/month exempt), pre-Decreto 13-2026 (Decreto 10-2012) |
| IVA credit deduction cap | Q12,000/year (SAT) |
| Min wage non-agri C1 (Dept. Guatemala), 2026 | Q4,002.28/month + Q250 bono = Q4,252.28 (EY / Acuerdo Gubernativo 256-2025) |
| Min wage non-agri C2 (rest of country), 2026 | Q3,816.90/month + Q250 bono = Q4,066.90 (Prensa Libre / Acuerdo 256-2025) |
| ISR refund / annual liquidation deadline | 28 February of following year (oficsa / vescco) |
| Constancia de retención deadline | Within 10 business days of final/annual payment (vescco) |
| Validated by | Pending — requires sign-off by a Guatemalan licensed contador / perito contador |
| Validation date | Pending |

**IGSS programme split (2025--2026)**  _(IGSS official "Cuotas" (igssgt.org/cuotas); Acuerdo 1118; FUNDESA; Banco Industrial 2026; Prensa Libre.)_

| Programme | Employee | Employer | Combined |
| --- | --- | --- | --- |
| Accidentes (Accidents) | 1.00% | 3.00% | 4.00% |
| EMA -- Enfermedad y Maternidad (Sickness & Maternity) | 2.00% | 4.00% | 6.00% |
| IVS -- Invalidez, Vejez y Sobrevivencia (Disability/Old-age/Survivors) | 1.83% | 3.67% | 5.50% |
| **Subtotal IGSS** | **4.83%** | **10.67%** | **15.50%** |
| INTECAP (training institute) | — | 1.00% | 1.00% |
| IRTRA (workers' recreation institute) | — | 1.00% | 1.00% |
| **Total cost** | **4.83%** | **12.67%** | **17.50%** |

*Arithmetic check:* employee 1.00 + 2.00 + 1.83 = **4.83%**; employer IGSS 3.00 + 4.00 + 3.67 = **10.67%**; employer total 10.67 + 1.00 + 1.00 = **12.67%**; combined IGSS 4.83 + 10.67 = **15.50%**.
Source: IGSS official "Cuotas" (igssgt.org/cuotas); Acuerdo 1118; FUNDESA; Banco Industrial 2026; Prensa Libre.

**[RESEARCH GAP — reviewer to confirm]** The precise per-department allocation of the employer Accidentes/EMA/IVS split may historically have varied by department; only the headline totals (4.83% / 10.67% / 15.50%) are firmly confirmed by IGSS and Banco Industrial. Confirm the line-by-line split against the current Junta Directiva acuerdo for the employer's department.

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown ordinary salary vs bono split | Treat the Q250 bono separately; apply IGSS only to ordinary salary |
| Unknown circumscription (C1 vs C2) | Ask -- do not assume; min-wage floor differs |
| Unknown employer worker count | Assume IGSS registration is required (threshold is 1+ worker) |
| Unknown whether ISR deductions apply | Apply the Q48,000 fixed personal deduction only; do not assume IVA credit |
| Ambiguous IGSS vs penalty debit | Classify as IGSS contribution; flag for reviewer |
| Minimum-wage worker, 2026+ | Flag Decreto 13-2026 ISR exemption — escalate to reviewer |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable input** — Monthly ordinary salary (Q), and whether the worker earns at or above minimum wage. Without the ordinary salary figure, STOP. Do not compute IGSS or ISR.

**Recommended** -- circumscription (C1 = Department of Guatemala; C2 = rest of country), economic activity (non-agri / agri / maquila), the Q250 bonificación incentivo amount actually paid, and the worker's other documented deductions (IGSS, life insurance, donations, IVA credit).

**Ideal** -- IGSS planilla, SAT-1431 employee deduction declaration, prior-year constancia de retención, and bank statements showing IGSS and SAT debits.

### Refusal catalogue

- **R-GT-1 -- Ordinary salary unknown** — Trigger: monthly ordinary salary not provided. Message: "The monthly ordinary salary is mandatory for IGSS and ISR computation. IGSS applies to ordinary salary excluding the Q250 bonificación incentivo, and ISR depends on annualised taxable income. Cannot proceed without this figure."
- **R-GT-2 -- IGSS arrears / mora** — Trigger: employer has unpaid IGSS contributions. Message: "IGSS late-payment surcharge (recargo por mora) uses the maximum simple interest rate set annually by the Junta Monetaria, plus a 5% administrative-cost surcharge on a formal aviso de cobro (capped at Q3,000). Do not quantify arrears without an IGSS statement. Escalate to a licensed Guatemalan accountant."
- **R-GT-3 -- Pension / maximum-insurable-salary questions** — Trigger: client asks about the IGSS IVS pension benefit ceiling or maximum insurable salary. Message: "The exact current maximum insurable salary / IVS pension ceiling is [RESEARCH GAP — reviewer to confirm] and was not confirmed from an authoritative source. Do not state a figure. Escalate to a licensed accountant and confirm with IGSS."
- **R-GT-4 -- Minimum-wage ISR exemption (Decreto 13-2026)** — Trigger: worker earns minimum wage in 2026 onward. Message: "Decreto 13-2026 exempts minimum-wage workers from ISR withholding and redefines the personal deduction formulaically. Transitional rules apply for 2026 (extraordinary Q3,024 deduction). Confirm publication date and the worker's exact wage with a licensed accountant before applying."
- **R-GT-5 -- Department-specific IGSS split** — Trigger: client requires the precise Accidentes/EMA/IVS allocation for a specific department. Message: "Only the headline IGSS totals (4.83% / 10.67% / 15.50%) are firmly confirmed. The per-department split is [RESEARCH GAP — reviewer to confirm]. Escalate to a licensed accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to payroll, social security, and income tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. IGSS and ISR payments EXCLUDE from any IVA (VAT) return — they are statutory payroll obligations, not taxable supplies.

### 3.1 IGSS contributions (cuota patronal + cuota laboral)

**IGSS contributions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IGSS, I.G.S.S. | EXCLUDE -- IGSS contribution | Combined employer + employee IGSS remittance |
| INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL | EXCLUDE -- IGSS contribution | Full authority name |
| SEGURIDAD SOCIAL, CUOTA PATRONAL | EXCLUDE -- IGSS contribution | Employer share |
| CUOTA LABORAL, DESCUENTO IGSS | EXCLUDE -- IGSS contribution | Employee share withheld |
| PLANILLA IGSS | EXCLUDE -- IGSS contribution | Monthly IGSS planilla payment |

### 3.2 Parafiscal training / recreation levies (employer only)

**Parafiscal levies pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTECAP | EXCLUDE -- INTECAP levy (1%) | Employer training-institute levy |
| IRTRA | EXCLUDE -- IRTRA levy (1%) | Employer recreation-institute levy |

### 3.3 Income-tax payments to SAT (NOT IGSS -- do not confuse)

**SAT income-tax pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SAT, SUPERINTENDENCIA DE ADMINISTRACION TRIBUTARIA | EXCLUDE -- tax payment, not IGSS | Income tax / withholding to SAT |
| ISR, RETENCION ISR, RETENISR | EXCLUDE -- ISR withholding | Employer ISR retention (SAT-1331) |
| SAT-1331, FORMULARIO 1331 | EXCLUDE -- ISR retention return | Monthly withholding return |
| IVA, FEL | EXCLUDE -- VAT, not payroll | Not IGSS / not ISR-payroll |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, NOMINA, PLANILLA (outgoing) | EXCLUDE -- payroll expense | Gross wage payment, not a contribution |
| BONIFICACION INCENTIVO, BONO 250 | EXCLUDE -- bono incentivo (non-salary) | Q250 mandatory bonus, NOT subject to IGSS |
| SALARIO, SUELDO (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Benefits received (not contributions)

**Benefits received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IGSS PENSION, JUBILACION | EXCLUDE -- pension income received | Not a contribution paid |
| IGSS SUBSIDIO, INCAPACIDAD | EXCLUDE -- IGSS benefit received | Sickness/maternity subsidy, not a contribution |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical Guatemalan employer and employee (non-agricultural, Department of Guatemala, C1). All amounts in Quetzales (Q). IGSS applies only to ordinary salary, excluding the Q250 bono.

### Example 1 -- IGSS employee withholding on an above-minimum salary (Banco Industrial)

**Input line:**
`31/01/2026 ; IGSS PLANILLA ; DEBITO ; CUOTA LABORAL ENERO ; -241.50 ; GTQ`

**Reasoning:**
Matches "IGSS PLANILLA" / "CUOTA LABORAL" (patterns 3.1). Ordinary salary Q5,000.00. Employee IGSS = 4.83% × Q5,000.00 = **Q241.50**. The Q250 bono is excluded from the base. Exclude from IVA. This is the employee's statutory withholding.

**Classification:** EXCLUDE from IVA -- IGSS employee contribution (cuota laboral).

### Example 2 -- Employer IGSS + parafiscal cost on the same salary

**Input line:**
`31/01/2026 ; INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL ; DEBITO ; CUOTA PATRONAL ENERO ; -633.50 ; GTQ`

**Reasoning:**
Matches "INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL" (pattern 3.1). On ordinary salary Q5,000.00: employer IGSS = 10.67% × Q5,000.00 = Q533.50; INTECAP 1% = Q50.00; IRTRA 1% = Q50.00. The IGSS line here is Q533.50; if INTECAP/IRTRA appear together with IGSS the total is Q633.50. *Check:* Q533.50 + Q50.00 + Q50.00 = **Q633.50**. Exclude from IVA — employer payroll cost.

**Classification:** EXCLUDE from IVA -- employer IGSS + INTECAP + IRTRA (cuota patronal + parafiscal).

### Example 3 -- ISR monthly withholding to SAT (NOT IGSS)

**Input line:**
`14/02/2026 ; SAT RETENISR ; DEBITO ; SAT-1331 ISR RENTAS TRABAJO ; -989.63 ; GTQ`

**Reasoning:**
Matches "SAT RETENISR" / "SAT-1331" (pattern 3.3). This is ISR income-tax withholding, NOT IGSS. For a worker on Q25,000/month ordinary salary (annual salary Q300,000): annual IGSS deduction = 4.83% × Q300,000 = Q14,490.00; less fixed personal deduction Q48,000.00 → annual taxable income = Q300,000 − Q14,490 − Q48,000 = Q237,510.00, within bracket 1 (5%). Annual ISR = 5% × Q237,510.00 = Q11,875.50; monthly retención ≈ Q11,875.50 / 12 = **Q989.63**. Exclude from IVA. This is income tax, not social security.

**Classification:** EXCLUDE from IVA -- ISR withholding (SAT). NOT IGSS.

### Example 4 -- Salary outgoing including bono incentivo

**Input line:**
`30/01/2026 ; JUAN PEREZ NOMINA ; DEBITO ; SALARIO + BONO 250 ENERO ; -5,008.50 ; GTQ`

**Reasoning:**
Matches "NOMINA" / "BONO 250" (pattern 3.4). Net pay to the worker on a Q5,000.00 ordinary salary: gross ordinary Q5,000.00, less employee IGSS Q241.50 = Q4,758.50, plus Q250.00 bono incentivo = **Q5,008.50** (before any ISR — none due here, salary is below the Q4,000/month exempt-equivalent only on the bono-excluded base; annual taxable Q5,000×12 − IGSS − Q48,000 = Q60,000 − Q2,898 − Q48,000 = Q9,102, ISR 5% = Q455.10/yr ≈ Q37.93/mo, withheld separately). The bono is excluded from IGSS; the salary line is a payroll expense, not a contribution.

**Classification:** EXCLUDE from IVA -- payroll expense (salary + bono incentivo). NOT a contribution.

### Example 5 -- IGSS benefit received (subsidio, not a contribution)

**Input line:**
`12/03/2026 ; IGSS SUBSIDIO ; CREDITO ; INCAPACIDAD TEMPORAL ; +1,800.00 ; GTQ`

**Reasoning:**
Matches "IGSS SUBSIDIO" / "INCAPACIDAD" (pattern 3.5). This is an IGSS sickness/maternity benefit RECEIVED, not a contribution paid. Do not confuse inbound IGSS credits with outbound contribution debits. Exclude from IVA. Not an employer cost or employee withholding.

**Classification:** EXCLUDE from IVA -- IGSS benefit received. NOT a contribution.

### Example 6 -- Ambiguous IGSS debit (arrears / mora)

**Input line:**
`20/04/2026 ; IGSS ; DEBITO ; AVISO DE COBRO RECARGO MORA ; -3,520.00 ; GTQ`

**Reasoning:**
Matches "IGSS" (pattern 3.1) but the reference says "AVISO DE COBRO RECARGO MORA." This includes mora interest (Junta Monetaria maximum simple rate) and possibly the 5% administrative-cost surcharge (capped at Q3,000). Cannot separate contribution principal from penalty without an IGSS statement. Flag for reviewer.

**Classification:** EXCLUDE from IVA. Flag for reviewer -- request IGSS breakdown to split contribution principal from mora/surcharge (penalties are not a normal deductible payroll contribution).

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- IGSS base excludes the bono incentivo

- **IGSS computation formula** — IGSS_employee = 4.83% x ordinary_salary IGSS_employer = 10.67% x ordinary_salary           (IGSS only) parafiscal    = 2.00% x ordinary_salary            (INTECAP 1% + IRTRA 1%, employer only) employer_total_cost = 12.67% x ordinary_salary  _(Decreto 37-2001)_

### Rule 2 -- Employee never pays INTECAP or IRTRA

- **Employee cuota laboral scope** — The cuota laboral is 4.83% only. INTECAP (1%) and IRTRA (1%) are employer-only parafiscal levies. Never deduct them from the employee.

### Rule 3 -- Combined IGSS headline

- **Combined IGSS headline rate** — Employee 4.83% + employer IGSS 10.67% = 15.50% combined IGSS. INTECAP + IRTRA sit on top of the employer side only.  _(Banco Industrial 2026)_

### Rule 4 -- ISR base (rentas del trabajo)

- **ISR taxable income formula** — annual_taxable = annual_ordinary_salary + annual_bono_incentivo (subject to ISR, NOT to IGSS) - IGSS_IVS_and_other_deductible_contributions - Q48,000 fixed personal deduction (no documentation) - life insurance (non-dotal, proportional share) - donations (state/universities unlimited; non-profits capped at 5% of gross) - IVA credit (documented personal purchases, capped at Q12,000/year)  _(Decreto 10-2012; SAT; vescco; inbers)_

The first Q4,000/month is effectively exempt via the Q48,000 fixed deduction.

### Rule 5 -- ISR progressive brackets

**ISR progressive brackets**  _(SAT; Decreto 10-2012)_

| Annual taxable income | Tax |
| --- | --- |
| Q0.01 -- Q300,000 | 5% of taxable income |
| Over Q300,000 | Q15,000 + 7% of the excess over Q300,000 |

*Cumulative check:* at exactly Q300,000, bracket 1 tax = 5% × Q300,000 = Q15,000, which equals the fixed amount that opens bracket 2 — the schedule is continuous. Source: SAT; Decreto 10-2012.

### Rule 6 -- IGSS registration threshold is 1 worker

- **IGSS employer registration threshold** — Every employer with 1 or more workers must register with IGSS and affiliate employees, since 17 January 2023. The old 3-worker threshold (Acuerdo 1123) no longer applies.  _(Acuerdo Junta Directiva 1529; Prensa Libre; IGSS patronos)_

### Rule 7 -- Minimum contribution base tied to minimum wage

- **Minimum contribution base / no confirmed ceiling** — IGSS applies a minimum contribution base ("cuota mínima") tied to the minimum wage. There is no confirmed standard ceiling for contributions from an authoritative source — contributions apply to full ordinary salary. [RESEARCH GAP — reviewer to confirm] the maximum insurable salary affecting the IVS pension benefit.  _(IGSS noticia, 2022)_

### Rule 8 -- Forms and deadlines

**Forms and deadlines table**  _(oficsa; vescco; SAT)_

| Form / event | Purpose | Frequency / deadline |
| --- | --- | --- |
| SAT-1331 (RetenISR2 Web) | Employer monthly ISR withholding return | Monthly |
| SAT-1431 | Employee's annual declaration of deductions to employer | Annual (Jan–Mar window) |
| Constancia de retención | Withholding certificate to employee | Within 10 business days of final/annual payment |
| Annual liquidation / refund | Year-end ISR reconciliation; over-withholding refund | By 28 February of following year |
| IVA-FEL planilla | Personal-purchase VAT credit filing | First business days of January (commonly cited 10 January) |

### Rule 9 -- 2026 reform (Decreto 13-2026)

- **Decreto 13-2026 reform details** — Approved by Congress 28 April 2026. Minimum-wage workers are exempt from ISR withholding from 2026 onward. The personal deduction is redefined as 12 monthly non-agricultural minimum salaries including the Q250 bono (replacing the flat Q48,000), auto-updating to the highest minimum wage. For 2026 only, an extraordinary additional deduction of Q3,024 (no documentation) applies; it takes effect 8 days after publication, with remaining provisions effective 1 January 2027.  _(Prensa Libre; vescco; Congreso; DCA)_

*Computed (not directly published — flag if used):* 12 × (Q4,002.28 + Q250) = Q51,027.36 as the 2026 non-agri C1 derived personal-deduction figure. Treat as computed, not a published statutory number.

### Rule 10 -- Minimum wage by circumscription (2026, non-agri)

**Minimum wage by circumscription table**  _(EY Centroamérica; Acuerdo Gubernativo 256-2025; Prensa Libre; AGN)_

| Circumscription | Daily | Monthly salary | + Q250 bono = total |
| --- | --- | --- | --- |
| C1 (Dept. of Guatemala) | Q131.58 | Q4,002.28 | Q4,252.28 |
| C2 (rest of country) | Q125.49 | Q3,816.90 | Q4,066.90 |

Agricultural and maquila/export rates differ — confirm by activity.

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Department-specific IGSS allocation

- **Trigger/Issue/Action** — Trigger: Employer needs the exact Accidentes/EMA/IVS split for a specific department. Issue: Only the headline totals (4.83% / 10.67% / 15.50%) are firmly confirmed. [RESEARCH GAP — reviewer to confirm] the per-department split. Action: Flag for reviewer; confirm against the current Junta Directiva acuerdo for that department.

### T2-2 -- Minimum-wage worker under Decreto 13-2026

- **Trigger/Issue/Action** — Trigger: Worker earns minimum wage in 2026 onward. Issue: ISR exemption + formulaic personal deduction + extraordinary Q3,024 transitional deduction; effective dates depend on Diario Oficial publication. Action: Flag for reviewer; confirm wage and publication date before applying.

### T2-3 -- IGSS arrears / mora

- **Trigger/Issue/Action** — Trigger: Employer has unpaid IGSS contributions. Issue: Mora uses the Junta Monetaria maximum simple rate; a formal aviso de cobro adds a 5% administrative surcharge capped at Q3,000. The former 50% surcharge-exemption benefit was repealed. Action: Do not quantify without an IGSS statement. Escalate to a licensed accountant.

### T2-4 -- Maximum insurable salary / pension ceiling

- **Trigger/Issue/Action** — Trigger: Client asks about the IVS pension benefit ceiling. Issue: [RESEARCH GAP — reviewer to confirm] — the exact current Q amount was not confirmed from an authoritative source. Action: Do not state a figure. Escalate; confirm with IGSS.

### T2-5 -- Non-standard wage components

- **Trigger/Issue/Action** — Trigger: Worker receives commissions, overtime, bonuses beyond the Q250 bono, or in-kind benefits. Issue: Some components form part of ordinary salary (IGSS base) and some do not; the Q250 bono incentivo is specifically excluded from IGSS but subject to ISR. Action: Flag for reviewer to confirm which components enter the IGSS base.

### T2-6 -- Donations and IVA credit deductions

- **Trigger/Issue/Action** — Trigger: Worker claims donation deductions or the IVA-FEL credit. Issue: Donations to non-profits are capped at 5% of gross income; the IVA credit is capped at Q12,000/year and requires the planilla filed in early January. Action: Flag for reviewer; require documentation before applying.

## Section 7 -- Excel working paper template

When producing an IGSS / ISR computation, structure the working paper as follows:

```
GUATEMALA PAYROLL COMPUTATION -- WORKING PAPER
Client / Employer: [name]
Worker: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Monthly ordinary salary (Q):        [____]
  Monthly bonificacion incentivo:     250.00
  Circumscription (C1 / C2):          [____]
  Economic activity:                  [non-agri / agri / maquila]
  At/above minimum wage:              [YES / NO]
  Other ISR deductions (Q):           [life ins / donations / IVA credit]

IGSS COMPUTATION (base = ordinary salary, EXCLUDES Q250 bono)
  Employee 4.83%:                     Q [____]
  Employer IGSS 10.67%:               Q [____]
  INTECAP 1%:                         Q [____]
  IRTRA 1%:                           Q [____]
  Employer total cost 12.67%:         Q [____]

ISR COMPUTATION (annual)
  Annual ordinary salary:             Q [____]
  Annual bono incentivo (ISR base):   Q 3,000.00
  Less IGSS/IVS deductible:           Q [____]
  Less fixed personal deduction:      Q 48,000.00   (pre-Decreto 13-2026)
  Less other deductions:              Q [____]
  Annual taxable income:              Q [____]
  Bracket 1 (5% up to Q300,000):      Q [____]
  Bracket 2 (Q15,000 + 7% excess):    Q [____]
  Annual ISR:                         Q [____]
  Monthly retencion (SAT-1331):       Q [____]

DEADLINES
  SAT-1331 monthly withholding:       [monthly]
  Constancia de retencion:            [within 10 business days]
  Annual liquidation / refund:        28 February [year+1]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How IGSS and ISR debits appear on Guatemalan bank statements

**Banco Industrial:**
- Description: "IGSS", "IGSS PLANILLA", "INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL"
- ISR: "SAT RETENISR", "SAT-1331"
- Timing: IGSS planilla paid monthly; ISR withholding remitted monthly

**Banrural (Banco de Desarrollo Rural):**
- Description: "IGSS CUOTA", "SEGURIDAD SOCIAL", "INTECAP", "IRTRA"
- Timing: Monthly

**BAM (Banco Agromercantil) / G&T Continental / BAC:**
- Description: "IGSS", "PLANILLA IGSS", "SAT ISR", "RETENCION ISR"
- Timing: Monthly

**Key identification tips:**
1. IGSS and ISR debits are always outgoing (DEBITO), never credits.
2. Employee IGSS should be ≈ 4.83% of ordinary salary; employer IGSS ≈ 10.67%; INTECAP + IRTRA ≈ 2%.
3. The Q250 "BONO" / "BONIFICACION INCENTIVO" is NOT subject to IGSS — exclude from the contribution base.
4. Do not confuse SAT/ISR debits (income tax) with IGSS debits (social security).
5. Inbound "IGSS SUBSIDIO" / "JUBILACION" / "PENSION" are benefits received, not contributions.
6. Irregular IGSS debits referencing "MORA" or "AVISO DE COBRO" include penalties — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for IGSS debits** -- identify outgoing payments matching Section 3.1/3.2 patterns.
2. **Reverse-engineer the ordinary salary:** employer IGSS debit / 10.67% ≈ ordinary salary; employee IGSS / 4.83% ≈ ordinary salary. They should reconcile.
3. **Identify ISR withholding** -- match SAT/ISR debits (Section 3.3); these are income tax, not social security.
4. **Separate the bono** -- the Q250 bono incentivo is excluded from IGSS but subject to ISR.
5. **Flag for reviewer:** "IGSS/ISR classification derived from bank statement amounts only. Ordinary salary, circumscription, and deductions have not been independently verified. Reviewer must confirm before filing. Note Decreto 13-2026 minimum-wage exemption if applicable."

## Section 10 -- Reference material

### Calculation examples (ordinary salary basis; C1, non-agri, 2026)

**Calculation examples table**  _(igssgt.org/cuotas)_

| Ordinary salary (mo) | EE IGSS 4.83% | ER IGSS 10.67% | INTECAP+IRTRA 2% | ER total 12.67% |
| --- | --- | --- | --- | --- |
| Q4,002.28 (min wage) | Q193.31 | Q427.04 | Q80.05 | Q507.09 |
| Q5,000.00 | Q241.50 | Q533.50 | Q100.00 | Q633.50 |
| Q10,000.00 | Q483.00 | Q1,067.00 | Q200.00 | Q1,267.00 |
| Q25,000.00 | Q1,207.50 | Q2,667.50 | Q500.00 | Q3,167.50 |

*Spot-check (Q5,000):* 4.83% × 5,000 = 241.50; 10.67% × 5,000 = 533.50; 2% × 5,000 = 100.00; 12.67% × 5,000 = 633.50. ✓ Source: igssgt.org/cuotas.

### ISR computation examples (annual; Q48,000 fixed deduction; IGSS-IVS 1.83% only deducted)

**ISR computation examples table**  _(Decreto 10-2012; SAT)_

| Annual ordinary salary | Annual IVS (1.83%) | Fixed deduction | Taxable | Annual ISR |
| --- | --- | --- | --- | --- |
| Q60,000 | Q1,098.00 | Q48,000 | Q10,902.00 | Q545.10 (5%) |
| Q120,000 | Q2,196.00 | Q48,000 | Q69,804.00 | Q3,490.20 (5%) |
| Q360,000 | Q6,588.00 | Q48,000 | Q305,412.00 | Q15,000 + 7%×Q5,412 = Q15,378.84 |

*Spot-check (Q360,000):* taxable Q360,000 − Q6,588 − Q48,000 = Q305,412.00; over Q300,000 by Q5,412.00; ISR = Q15,000 + 7% × Q5,412.00 = Q15,000 + Q378.84 = Q15,378.84. ✓ Source: Decreto 10-2012; SAT. (Worked Example 3 above deducts the full 4.83% IGSS rather than IVS-only; reviewer to confirm which contributions are deductible for the specific client — both treatments shown for transparency.)

### Penalties

**Penalties table**

| Penalty | Rate / amount | Source |
| --- | --- | --- |
| IGSS mora (late payment) | Junta Monetaria maximum simple interest rate on unpaid contribution | IGSS reglamento recaudación (2018) |
| IGSS aviso de cobro surcharge | 5% administrative cost, capped at Q3,000 | IGSS reglamento recaudación |
| ISR omission of tax (Art. 89) | 100% of tax omitted (−50% if paid before SAT requirement) | Código Tributario, Decreto 6-91 |
| ISR mora (Art. 92) | tax × 0.005 × days late (0.5% per day) | Código Tributario, Decreto 6-91 |

### Test suite

**Test 1:** Ordinary salary Q5,000/mo. Employee IGSS = 4.83% × 5,000 = **Q241.50**. ✓

**Test 2:** Ordinary salary Q5,000/mo. Employer IGSS = 10.67% × 5,000 = **Q533.50**; INTECAP+IRTRA = 2% × 5,000 = Q100.00; employer total = 12.67% × 5,000 = **Q633.50**. ✓

**Test 3:** Annual taxable income Q237,510 (from Q25,000/mo salary less 4.83% IGSS less Q48,000). ISR = 5% × Q237,510 = **Q11,875.50**; monthly ≈ **Q989.63**. ✓

**Test 4:** Annual taxable income exactly Q300,000. ISR = 5% × 300,000 = **Q15,000.00** (bracket boundary). ✓

**Test 5:** Annual taxable income Q305,412. ISR = Q15,000 + 7% × Q5,412 = **Q15,378.84**. ✓

**Test 6:** Q250 bono incentivo paid. IGSS base contribution on the bono = **Q0.00** (excluded). Bono IS subject to ISR. ✓

**Test 7:** Employer with 1 worker. IGSS registration required? **YES** (Acuerdo 1529, since 17 Jan 2023). ✓

**Test 8:** 2026 minimum-wage worker (Q4,002.28/mo). ISR withholding under Decreto 13-2026 = **exempt** (flag for reviewer to confirm publication/effective date). ✓

**Test 9:** Min-wage non-agri C1 monthly total = Q4,002.28 + Q250 bono = **Q4,252.28**. ✓

**Test 10:** Computed 2026 personal deduction (Decreto 13-2026, C1) = 12 × (Q4,002.28 + Q250) = **Q51,027.36** (derived, flag as computed). ✓

### Prohibitions

- NEVER apply IGSS to the Q250 bonificación incentivo — it is excluded from the contribution base.
- NEVER deduct INTECAP or IRTRA from the employee — they are employer-only (the cuota laboral is 4.83% flat).
- NEVER state a maximum insurable salary / IVS pension ceiling — that figure is a confirmed RESEARCH GAP.
- NEVER state a per-department IGSS split as fact — only the 4.83% / 10.67% / 15.50% totals are confirmed.
- NEVER use current-year minimum-wage ISR rules for prior years without confirming Decreto 13-2026 effective dates.
- NEVER quantify IGSS mora or arrears without an IGSS statement — escalate.
- NEVER confuse SAT/ISR debits (income tax) with IGSS debits (social security).
- NEVER present the Q51,027.36 Decreto 13-2026 figure as published — it is a derived computation, flag it as such.
- NEVER present IGSS/ISR figures as definitive — always label as estimated and direct the client to IGSS/SAT records.
- NEVER compute penalties without escalating to a licensed Guatemalan accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
