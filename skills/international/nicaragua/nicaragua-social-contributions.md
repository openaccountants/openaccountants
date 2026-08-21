---
name: nicaragua-social-contributions
description: Use this skill whenever asked about Nicaragua (ISO NI) social security and payroll taxes for employees and employers. Trigger on phrases like "how much INSS do I pay", "Nicaragua social security", "INSS employer contribution", "INSS laboral patronal", "INATEC 2%", "Nicaragua payroll tax", "Régimen Integral", "IVM IVM-RP", "córdoba payroll", "IR rentas del trabajo", "Nicaragua income tax withholding", "Form IR-122", "Form IR-106", "retención salarial Nicaragua", or any question about Nicaraguan INSS/INATEC/payroll IR obligations. Also trigger when classifying Nicaraguan bank statement transactions that relate to INSS debits, INATEC payments, DGI retention remittances, or payroll runs from BANPRO, BAC, LAFISE, FICOHSA or other Nicaraguan banks. This skill covers INSS employee/employer rates by regime, the INATEC training levy, the IR progressive employment-income schedule, monthly and annual filing deadlines, registration, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Nicaraguan social-contribution or payroll work.
version: 0.1
jurisdiction: NI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nicaragua Social Security & Payroll Contributions (INSS / INATEC / IR Salarial)

## Section 1 -- Quick reference

**Section 1 quick reference table**

| Field | Value |
| --- | --- |
| Country | Nicaragua (Republic of Nicaragua), ISO NI |
| Currency | Nicaraguan córdoba (NIO / C$) -- all figures in córdobas |
| Tax year | Calendar year |
| Social-security authority | INSS (Instituto Nicaragüense de Seguridad Social) |
| Training levy authority | INATEC (Tecnológico Nacional), collected via INSS |
| Tax authority (income tax) | DGI (Dirección General de Ingresos) |
| Primary income-tax legislation | Ley No. 822 (Ley de Concertación Tributaria, LCT), Art. 23; as reformed by Ley No. 891 |
| Social-security legal basis | Decreto 06-2019 (Feb 2019 INSS reform) |
| Employee INSS (Régimen Integral) | 7.00% of gross salary (no ceiling, "sin techo") — Decreto 06-2019 / PwC |
| Employer INSS (Régimen Integral) | 21.50% (≤50 employees) / 22.50% (>50 employees) — PwC / Decreto 06-2019 |
| INATEC levy (employer) | 2.00% of total gross payroll — Ley Orgánica del INATEC |
| Income-tax basis | Territorial — only Nicaraguan-source income taxed (LCT) |
| Income-tax exempt band | First C$100,000/year exempt (LCT Art. 23) |
| Income-tax top marginal rate | 30% on income above C$500,000/year (LCT Art. 23) |
| Non-resident WHT (Nicaraguan-source) | 20% definitive WHT — PwC |
| Monthly remittance form | IR-122 (retenciones), due 5th of following month — DGI FAQ |
| Annual individual return | IR-106, due within 90 days of year-end (~31 March) — PwC |
| Validated by | Pending — requires sign-off by a Nicaraguan licensed accountant (contador público autorizado) |
| Validation date | Pending |

**Contribution overview (Régimen Integral, standard formal employment)**

| Party | Rate | Notes |
| --- | --- | --- |
| Employee (Laboral) | 7.00% | Withheld from gross salary; no ceiling |
| Employer (Patronal), ≤50 employees | 21.50% | Plus 2.00% INATEC = 23.50% total burden |
| Employer (Patronal), >50 employees | 22.50% | Plus 2.00% INATEC = 24.50% total burden |
| State | 1.75% | Enfermedad y Maternidad — funded by the State, not the employer |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown contribution regime | Assume **Régimen Integral** (standard for formal employees) |
| Unknown employer size (≤50 vs >50) | Assume **≤50 employees** (lower 21.50% employer rate); flag for reviewer |
| Unknown whether income is Nicaraguan-source | STOP — territorial system means source must be confirmed before taxing |
| Unknown residence/domicile of payee | Ask — non-residents face 20% definitive WHT, not the progressive schedule |
| Unknown whether INSS debit is contribution or penalty | Classify as contribution; flag for reviewer |
| Unknown gross vs net salary | Ask — INSS is computed on **gross**; do not infer from net |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — gross monthly salary (in córdobas) and contribution regime (Integral vs IVM-RP). Without gross salary, STOP. Do not compute INSS or IR.
- **Recommended inputs** — employer headcount (≤50 vs >50, determines employer INSS rate), residence/domicile of the employee, and whether the individual has more than one employer.
- **Ideal inputs** — INSS planilla (payroll schedule), DGI IR-122 monthly remittances, prior-year IR-106 (if filed), and bank statements showing INSS/INATEC/DGI debits.

### Refusal catalogue

- **R-NI-SOC-1 -- Gross salary unknown** — Gross salary is mandatory. INSS contributions and IR withholding are both computed on gross salary, with no maximum insurable ceiling (Decreto 06-2019). Cannot proceed without the gross figure. (Trigger: gross monthly salary not provided.)  _(Decreto 06-2019)_
- **R-NI-SOC-2 -- Penalty / surcharge quantification** — Exact penalty, surcharge and value-maintenance (mantenimiento de valor) amounts under the Código Tributario (Ley No. 562) could not be confirmed from an authoritative source. Do not estimate. Escalate to a licensed Nicaraguan accountant. [RESEARCH GAP — reviewer to confirm] (Trigger: client asks to quantify late-filing or late-payment penalties (multa, recargo por mora, mantenimiento de valor).)  _(Código Tributario (Ley No. 562))_
- **R-NI-SOC-3 -- Non-Nicaraguan-source income** — Nicaragua uses a territorial system — only Nicaraguan-source income is taxed (LCT). Source determination requires case-specific analysis. Escalate to a licensed accountant before computing IR. (Trigger: income may be foreign-source.)  _(LCT)_
- **R-NI-SOC-4 -- Special regimes / Free Trade Zone** — Special regimes (Zona Franca / Free Trade Zone, mining, fishing) have distinct INSS and minimum-wage treatment. Escalate to a licensed Nicaraguan accountant. (Trigger: client operates under Zona Franca, mining, fishing, or other special regime.)
- **R-NI-SOC-5 -- INSS sub-component precision** — PwC confirms only the headline totals (7.00% employee; 21.50% / 22.50% employer). The sub-component split is taken from a Nicaraguan tax-reference source consistent with Decreto 06-2019 but not from inss.gob.ni directly. Flag for reviewer if component-level precision is required. [RESEARCH GAP — reviewer to confirm components] (Trigger: client needs the exact IVM / Salud / Riesgos Profesionales / Víctimas de Guerra split rather than the headline total.)  _(PwC; Decreto 06-2019)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for Nicaraguan bank statement transactions related to social security and payroll tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. INSS, INATEC and DGI remittances EXCLUDE from any VAT (IVA) return or revenue classification — they are statutory contributions/withholdings, not business supplies. Spanish-language references are common; both Spanish and English forms are listed.

### 3.1 INSS contributions (employee withholding + employer share)

**INSS contributions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, INSTITUTO NICARAGUENSE DE SEGURIDAD SOCIAL | EXCLUDE -- INSS contribution | Monthly remittance of employee + employer INSS |
| SEGURIDAD SOCIAL, SEG SOCIAL | EXCLUDE -- INSS contribution | Same |
| APORTE PATRONAL, CUOTA PATRONAL | EXCLUDE -- employer INSS share | Employer 21.50% / 22.50% |
| APORTE LABORAL, CUOTA LABORAL | EXCLUDE -- employee INSS withholding | Employee 7.00% |
| SIE INSS, PLANILLA INSS | EXCLUDE -- INSS payroll remittance | INSS payment via planilla |

### 3.2 INATEC training levy

**INATEC pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INATEC, TECNOLOGICO NACIONAL | EXCLUDE -- INATEC 2% levy | Employer training levy, collected via INSS |
| APORTE INATEC, CAPACITACION 2% | EXCLUDE -- INATEC levy | 2.00% of gross payroll |

### 3.3 DGI income-tax remittances (NOT INSS -- do not confuse)

**DGI pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, DIRECCION GENERAL DE INGRESOS | EXCLUDE -- income tax remittance | IR, not social security |
| IR-122, RETENCION IR, RETENCIONES | EXCLUDE -- IR withholding remittance | Monthly employer withholding (Form IR-122) |
| IR-106, RENTA ANUAL | EXCLUDE -- annual income-tax return payment | Form IR-106 |
| RENTAS DEL TRABAJO | EXCLUDE -- employment-income IR | Not INSS |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary/payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, NOMINA, PLANILLA (outgoing) | EXCLUDE -- payroll expense | Gross wage payment, not a contribution |
| PAGO SALARIO, ABONO NOMINA (incoming) | EXCLUDE -- employment income received | Not a contribution |

### 3.5 INSS benefits received (not contributions)

**INSS benefits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION INSS, JUBILACION | EXCLUDE -- pension income received | Not a contribution paid |
| SUBSIDIO INSS, SUBSIDIO MATERNIDAD | EXCLUDE -- benefit received | Sickness/maternity subsidy, not a contribution |

## Section 4 -- Worked examples

Six bank statement / payroll classifications for a hypothetical formal employer and employee in Nicaragua (Régimen Integral unless stated). All amounts in córdobas (C$). All arithmetic uses the rates in Section 5.

### Example 1 -- Employee INSS withholding on a C$30,000 monthly salary

**Input line:**
`05.04.2025 ; INSS APORTE LABORAL ; DEBITO ; PLANILLA MARZO 2025 ; -2,100.00 ; NIO`

**Reasoning:**
Matches "INSS ... APORTE LABORAL" (pattern 3.1). Employee INSS = 7.00% × C$30,000 gross = **C$2,100.00**. No ceiling applies (Decreto 06-2019). This is the employee withholding portion only; the employer share is separate.

**Classification:** EXCLUDE from IVA. Employee INSS withholding = C$2,100.00.

### Example 2 -- Employer INSS share (≤50 employees) on the same salary

**Input line:**
`05.04.2025 ; INSS APORTE PATRONAL ; DEBITO ; PLANILLA MARZO 2025 ; -6,450.00 ; NIO`

**Reasoning:**
Matches "INSS ... APORTE PATRONAL" (pattern 3.1). Employer with ≤50 employees pays 21.50% × C$30,000 = **C$6,450.00**. (For an employer with >50 employees it would be 22.50% × C$30,000 = C$6,750.00.)

**Classification:** EXCLUDE from IVA. Employer INSS share = C$6,450.00 (≤50-employee rate).

### Example 3 -- INATEC training levy

**Input line:**
`05.04.2025 ; INATEC CAPACITACION 2% ; DEBITO ; NOMINA MARZO 2025 ; -600.00 ; NIO`

**Reasoning:**
Matches "INATEC" (pattern 3.2). INATEC = 2.00% × C$30,000 gross payroll = **C$600.00**, collected via INSS infrastructure on behalf of INATEC.

**Classification:** EXCLUDE from IVA. INATEC employer levy = C$600.00.

### Example 4 -- Monthly IR withholding remittance to DGI (Form IR-122)

**Input line:**
`05.04.2025 ; DGI RETENCION IR-122 ; DEBITO ; RENTAS DEL TRABAJO MAR 2025 ; -3,496.67 ; NIO`

**Reasoning:**
Matches "DGI ... IR-122" (pattern 3.3) — income tax, NOT INSS. Computation for a C$30,000/month employee in the Régimen Integral:
- Monthly gross: C$30,000; employee INSS (deductible): 7% = C$2,100.
- Monthly taxable base after INSS: C$30,000 − C$2,100 = C$27,900.
- Annualised taxable income: C$27,900 × 12 = C$334,800 (falls in the 200,000.01–350,000 bracket).
- Annual IR = base C$15,000 + 20% × (C$334,800 − C$200,000) = C$15,000 + C$26,960 = **C$41,960.00/year**.
- Monthly withholding = C$41,960 / 12 = **C$3,496.67**.

**Classification:** EXCLUDE from IVA. IR (rentas del trabajo) withholding, not INSS. Remitted on Form IR-122.

### Example 5 -- Exempt-band employee (no IR withholding)

**Input line:**
`05.04.2025 ; INSS APORTE LABORAL ; DEBITO ; PLANILLA MARZO 2025 ; -560.00 ; NIO`

**Reasoning:**
Matches pattern 3.1. Employee earns C$8,000/month gross. Employee INSS = 7% × C$8,000 = **C$560.00**. Annualised taxable base after INSS = (8,000 − 560) × 12 = C$89,280, which is below the C$100,000 exempt band (LCT Art. 23). **No IR withholding is due** — there would be no corresponding DGI IR-122 debit for this employee.

**Classification:** EXCLUDE from IVA. Employee INSS = C$560.00; IR = nil (below exempt band).

### Example 6 -- Non-resident definitive withholding (NOT progressive)

**Input line:**
`12.05.2025 ; DGI RETENCION NO RESIDENTE ; DEBITO ; PAGO SERVICIOS ; -10,000.00 ; NIO`

**Reasoning:**
Matches "DGI RETENCION" (pattern 3.3). Payment of C$50,000 of Nicaraguan-source income to a non-resident. Non-residents face a **20% definitive WHT** (PwC), not the progressive schedule: 20% × C$50,000 = **C$10,000.00**. The progressive brackets do NOT apply to non-residents.

**Classification:** EXCLUDE from IVA. 20% non-resident definitive WHT = C$10,000.00. Confirm Nicaraguan source before applying.

## Section 5 -- Tier 1 rules

These rules apply when bank statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- INSS is computed on GROSS salary, no ceiling

- **INSS base** — INSS contributions apply to the full gross salary. There is no maximum insurable salary ("sin techo") since Decreto 06-2019. Never cap the base.  _(Decreto 06-2019)_

### Rule 2 -- Régimen Integral rates (standard formal employment)

**Régimen Integral component rates**  _(PwC; nicatributos.com; Decreto 06-2019)_

| Component | Employee | Employer ≤50 | Employer >50 |
| --- | --- | --- | --- |
| IVM (pension) | 4.75% | 12.50% | 13.50% |
| Enfermedad y Maternidad (health) | 2.25% | 6.00% | 6.00% |
| Riesgos Profesionales | — | 1.50% | 1.50% |
| Víctimas de Guerra | — | 1.50% | 1.50% |
| **Total** | **7.00%** | **21.50%** | **22.50%** |

Source: PwC (headline totals 7.00% / 21.50% / 22.50%); component split per nicatributos.com consistent with Decreto 06-2019. [RESEARCH GAP — component split not confirmed on inss.gob.ni directly.] The State separately funds 1.75% (Enfermedad y Maternidad).

### Rule 3 -- Régimen IVM-RP rates (pension + occupational risk only, no health)

**Régimen IVM-RP rates**  _(nicatributos.com)_

| Party | Total | Components |
| --- | --- | --- |
| Employee | 5.00% | IVM 4.75% + Víctimas de Guerra 0.25% |
| Employer ≤50 | 15.50% | — |
| Employer >50 | 16.50% | — |

Source: nicatributos.com (consistent with Decreto 06-2019). Use only when the IVM-RP regime is explicitly confirmed; otherwise default to Régimen Integral.

### Rule 4 -- INATEC training levy

- **INATEC levy** — INATEC = 2.00% of total gross payroll, paid by the employer, mandatory for all employers, collected monthly through INSS on behalf of INATEC. It is an employer cost separate from INSS.  _(Ley Orgánica del INATEC)_

### Rule 5 -- Total employer payroll burden (Integral)

- **Total employer burden ≤50** — 21.50% INSS + 2.00% INATEC = 23.50% of gross payroll.
- **Total employer burden >50** — 22.50% INSS + 2.00% INATEC = 24.50% of gross payroll.

This is on top of the 7.00% employee INSS withholding (which is borne by the employee, not the employer).

### Rule 6 -- IR (employment income) progressive schedule

Income tax on rentas del trabajo (LCT Art. 23). System is territorial — only Nicaraguan-source income.

**IR progressive schedule**  _(PwC; LCT Art. 23 as reformed by Ley No. 891)_

| Annual taxable income (C$) | Base tax (C$) | Marginal % on excess over lower bound |
| --- | --- | --- |
| 0 – 100,000 | 0 | 0% (exempt) |
| 100,000.01 – 200,000 | 0 | 15% |
| 200,000.01 – 350,000 | 15,000 | 20% |
| 350,000.01 – 500,000 | 45,000 | 25% |
| 500,000.01 and above | 82,500 | 30% |

Cumulative-tax check: 100,000×15% = 15,000 → base for next band. 15,000 + 150,000×20% = 15,000 + 30,000 = 45,000 → base for next. 45,000 + 150,000×25% = 45,000 + 37,500 = 82,500 → base for top band. Source: PwC; LCT Art. 23 as reformed by Ley No. 891.

### Rule 7 -- IR taxable base is gross less employee INSS

- **IR taxable base** — Employee INSS (7.00% under the Integral regime) is deductible in arriving at the IR taxable base for employment income. Compute IR on (annual gross − annual employee INSS).

### Rule 8 -- Non-residents: 20% definitive WHT

- **Non-resident WHT** — Nicaraguan-source income paid to non-residents (whether domiciled or not) is subject to a 20% definitive withholding tax. The progressive schedule does not apply.  _(PwC)_

### Rule 9 -- Monthly remittance deadline (Form IR-122)

- **Monthly remittance deadline** — Employers withhold and remit employment-income IR monthly via Form IR-122, due no later than the 5th day of the following month.  _(DGI FAQ)_

### Rule 10 -- Annual individual return (Form IR-106)

- **Annual individual return deadline** — Annual individual return is Form IR-106, due within 90 days after year-end (~31 March). Final tax payment also due within 90 days after year-end.  _(PwC)_

### Rule 11 -- Single-employer filing exemption

- **Single-employer filing exemption** — An individual with a single employer and no other qualifying income/deductions is generally not required to file an annual return — the employer's monthly withholding is final. An annual return is required where aggregate income from multiple employers exceeds C$100,000.  _(PwC / DGI FAQ)_

## Section 6 -- Tier 2 catalogue

When bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Employer size at the ≤50 / >50 boundary

- **T2-1** — Trigger: Employer headcount is near 50, or fluctuates month to month. Issue: The employer INSS rate (21.50% vs 22.50%) and IVM-RP rate (15.50% vs 16.50%) depend on whether the employer has ≤50 or >50 employees. The exact counting basis at the boundary is not clear from secondary sources. Action: Flag for reviewer. Default to ≤50 (lower rate) only as a stated assumption.

### T2-2 -- Regime classification (Integral vs IVM-RP)

- **T2-2** — Trigger: It is unclear whether an employee falls under Régimen Integral or Régimen IVM-RP. Issue: IVM-RP (no health component) applies to specific cases only. Misclassifying changes both employee (7.00% vs 5.00%) and employer rates. Action: Flag for reviewer. Default to Régimen Integral.

### T2-3 -- Multiple employers and annual return obligation

- **T2-3** — Trigger: Individual has income from more than one employer in the year. Issue: Aggregate income from multiple employers exceeding C$100,000 triggers an annual IR-106 filing obligation; withholding by each employer may not equal the correct annual tax. Action: Flag for reviewer. Recommend an annual reconciliation on Form IR-106.

### T2-4 -- Source of income (territorial system)

- **T2-4** — Trigger: Income may be partly foreign-source, or paid from/to abroad. Issue: Nicaragua taxes only Nicaraguan-source income. Source characterisation is fact-specific. Action: Flag for reviewer. Do not tax foreign-source income without confirmation.

### T2-5 -- Penalties, surcharges and mantenimiento de valor

- **T2-5** — Trigger: Client has late INSS, INATEC, or IR filings/payments. Issue: Late filing/payment under the Código Tributario (Ley No. 562) triggers multas, recargo por mora, interest, and mantenimiento de valor (indexation). The exact percentages and unit amounts could not be confirmed from an authoritative source (DGI penalties page was blocked). Action: Do NOT quantify. Escalate to a licensed accountant. [RESEARCH GAP — reviewer to confirm against Ley No. 562 / DGI.]  _(Código Tributario (Ley No. 562))_

### T2-6 -- Special regimes (Zona Franca, mining, fishing)

- **T2-6** — Trigger: Employer operates in a Free Trade Zone or other special sector. Issue: These sectors have distinct INSS, minimum-wage, and (for Zona Franca) income-tax treatment. Action: Flag for reviewer. Do not apply standard rates without confirmation.

## Section 7 -- Excel working paper template

When producing a Nicaraguan payroll/contribution computation, structure the working paper as follows:

```
NICARAGUA PAYROLL / CONTRIBUTION COMPUTATION -- WORKING PAPER
Client / Employer: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Employee name:                 [____]
  Gross monthly salary (C$):     [____]
  Contribution regime:           [Integral / IVM-RP]
  Employer headcount:            [≤50 / >50]
  Residence/domicile:            [Resident / Non-resident]
  Multiple employers:            [YES/NO]

INSS COMPUTATION (per month)
  Gross salary (no ceiling):     C$ [____]
  Employee INSS (7.00% Integral):C$ [____]
  Employer INSS (21.50%/22.50%): C$ [____]
  INATEC (2.00% employer):       C$ [____]
  Total employer burden:         C$ [____]   (INSS + INATEC)

IR (RENTAS DEL TRABAJO) COMPUTATION
  Annual gross (12 x monthly):   C$ [____]
  Less annual employee INSS:     C$ [____]
  Annual taxable base:           C$ [____]
  Bracket:                       [exempt / 15% / 20% / 25% / 30%]
  Base tax + marginal on excess: C$ [____]
  Annual IR:                     C$ [____]
  Monthly IR withholding (/12):  C$ [____]

NON-RESIDENT (if applicable)
  Nicaraguan-source amount:      C$ [____]
  20% definitive WHT:            C$ [____]

FILING / REMITTANCE
  Monthly IR-122 due:            5th of following month
  Annual IR-106 due:             within 90 days of year-end (~31 Mar)

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How contributions and remittances appear on Nicaraguan bank statements

Statements are typically in Spanish and in córdobas (NIO / C$). Common banks: BANPRO, BAC, LAFISE (Banco LAFISE Bancentro), FICOHSA, Banco de Finanzas (BDF).

**INSS remittances:**
- Description: "INSS", "INSTITUTO NICARAGUENSE DE SEGURIDAD SOCIAL", "APORTE PATRONAL", "APORTE LABORAL", "PLANILLA INSS"
- Timing: Monthly, typically early in the month following the payroll month
- Amount: Employee 7.00% and employer 21.50%/22.50% may appear as one combined remittance or split lines

**INATEC levy:**
- Description: "INATEC", "TECNOLOGICO NACIONAL", "CAPACITACION 2%"
- Timing: Monthly, collected via INSS
- Amount: 2.00% of gross payroll

**DGI income-tax remittances:**
- Description: "DGI", "DIRECCION GENERAL DE INGRESOS", "RETENCION IR", "IR-122"
- Timing: Monthly, due by the 5th of the following month
- Amount: aggregate IR withheld from employees

**Key identification tips:**
1. INSS/INATEC/DGI debits are always outgoing (DEBITO), never credits.
2. INSS recurs monthly; the employer share is roughly 3x the employee share under the Integral regime (21.50% vs 7.00%).
3. INATEC is small and consistent (2.00% of gross payroll).
4. Do NOT confuse DGI (income tax, IR-122) debits with INSS (social security) debits — different authorities, different obligations.
5. Inbound INSS credits (PENSION INSS, SUBSIDIO) are benefits received, not contributions.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for INSS / INATEC / DGI debits** — identify all outgoing payments matching Section 3 patterns.
2. **Separate the three streams** — INSS (social security), INATEC (2% levy), and DGI (income tax, IR-122).
3. **Reverse-engineer gross payroll where possible:**
   - Employer INSS debit / 0.215 ≈ gross payroll (≤50 employees), or / 0.225 (>50 employees).
   - INATEC debit / 0.02 ≈ gross payroll (cross-check against the INSS-derived figure).
   - Employee INSS debit / 0.07 ≈ gross payroll (Integral regime).
4. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Contribution regime, employer headcount, and income source have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### Contribution summary (Régimen Integral, 2025)

**Contribution summary table**  _(PwC; Decreto 06-2019)_

| Party | Rate | Source |
| --- | --- | --- |
| Employee INSS | 7.00% | PwC; Decreto 06-2019 |
| Employer INSS, ≤50 employees | 21.50% | PwC; Decreto 06-2019 |
| Employer INSS, >50 employees | 22.50% | PwC; Decreto 06-2019 |
| INATEC (employer) | 2.00% | Ley Orgánica del INATEC |
| State contribution | 1.75% | nicatributos.com / Decreto 06-2019 |

### IR (employment income) brackets, 2025

**IR brackets table**  _(PwC; LCT Art. 23)_

| Annual taxable income (C$) | Base tax (C$) | Marginal % | Source |
| --- | --- | --- | --- |
| 0 – 100,000 | 0 | 0% | PwC; LCT Art. 23 |
| 100,000.01 – 200,000 | 0 | 15% | PwC; LCT Art. 23 |
| 200,000.01 – 350,000 | 15,000 | 20% | PwC; LCT Art. 23 |
| 350,000.01 – 500,000 | 45,000 | 25% | PwC; LCT Art. 23 |
| 500,000.01 + | 82,500 | 30% | PwC; LCT Art. 23 |
| Non-resident (Nicaraguan-source) | — | 20% definitive WHT | PwC |

### Minimum wage by sector (in force from 1 Mar 2025, +4%; Acuerdo Ministerial ALTB-01-02-2025)

**Minimum wage table**  _(Acuerdo Ministerial ALTB-01-02-2025; EY / Bloomberg Línea)_

| Sector | C$/month | Source |
| --- | --- | --- |
| Agriculture (Agropecuario) | 5,950.02 | EY / Bloomberg Línea |
| Micro & small artisanal industry | 6,268.83 | EY / Bloomberg Línea |
| Central & municipal government | 7,419.90 | EY / Bloomberg Línea |
| Manufacturing industry | 8,000.46 | EY / Bloomberg Línea |
| Community, social & personal services | 8,341.29 | EY / Bloomberg Línea |
| Fishing | 9,047.20 | EY / Bloomberg Línea |
| Mining & quarrying | 10,686.02 | EY / Bloomberg Línea |
| Electricity/gas/water, commerce, restaurants, hotels, transport, storage & communications | 10,913.54 | EY / Bloomberg Línea |
| Construction, financial establishments & insurance | 13,315.61 | EY (primary; some sources quote 13,315.71) |

Note: 2025 rates remain in force into 2026 for most sectors as MITRAB had not set 2026–2027 rates (except Free Trade Zone) as of March 2026. [RESEARCH GAP — 2026–2027 sectoral minimum wages not yet published.]

### Filing & remittance deadlines

**Filing deadlines table**  _(DGI FAQ; PwC; INSS / Ley Orgánica del INATEC)_

| Obligation | Form | Deadline | Source |
| --- | --- | --- | --- |
| Monthly IR withholding | IR-122 | 5th of following month | DGI FAQ |
| Annual individual return | IR-106 | Within 90 days of year-end (~31 Mar) | PwC |
| INSS / INATEC monthly remittance | INSS planilla | Monthly (via INSS) | INSS / Ley Orgánica del INATEC |

### Registration

- Employers must register with **INSS** and enrol employees; contributions remitted monthly through INSS (which also collects the 2% INATEC levy).
- Employers register with **DGI** as withholding agents (responsable retenedor) for IR.
- Registration is **obligation-based** (employing staff / carrying on economic activity), not turnover-threshold based. [RESEARCH GAP — no córdoba registration threshold found in an authoritative source; reviewer to confirm.]

### Penalties

- Late filing/payment under the Código Tributario (Ley No. 562) triggers multas, recargo por mora, interest, and mantenimiento de valor (indexation). **Exact percentages and unit amounts could not be confirmed** — the DGI penalties page was blocked. [RESEARCH GAP — reviewer to confirm against Ley No. 562 / DGI.]

### Test suite

**Test 1:** Régimen Integral, gross C$30,000/month. -> Employee INSS = 7% × 30,000 = **C$2,100.00**.

**Test 2:** Régimen Integral, gross C$30,000/month, ≤50 employees. -> Employer INSS = 21.50% × 30,000 = **C$6,450.00**.

**Test 3:** Régimen Integral, gross C$30,000/month, >50 employees. -> Employer INSS = 22.50% × 30,000 = **C$6,750.00**.

**Test 4:** Gross monthly payroll C$30,000. -> INATEC = 2.00% × 30,000 = **C$600.00**. Total employer burden (≤50) = 6,450 + 600 = **C$7,050.00** (23.50%).

**Test 5:** Gross C$30,000/month, Integral. Annual taxable base = (30,000 − 2,100) × 12 = C$334,800 (20% bracket). -> Annual IR = 15,000 + 20% × (334,800 − 200,000) = 15,000 + 26,960 = **C$41,960.00**; monthly withholding = **C$3,496.67**.

**Test 6:** Gross C$8,000/month, Integral. Annual taxable base = (8,000 − 560) × 12 = C$89,280 (below C$100,000 exempt band). -> IR = **nil**.

**Test 7:** Non-resident paid C$50,000 of Nicaraguan-source income. -> 20% definitive WHT = **C$10,000.00**. Progressive schedule does NOT apply.

**Test 8:** Régimen IVM-RP, gross C$20,000/month. -> Employee = 5.00% × 20,000 = **C$1,000.00**; employer (≤50) = 15.50% × 20,000 = **C$3,100.00**.

**Test 9:** Annual taxable income exactly C$500,000. -> IR = 45,000 + 25% × (500,000 − 350,000) = 45,000 + 37,500 = **C$82,500.00** (confirms the top-band base tax).

**Test 10:** Annual taxable income C$700,000. -> IR = 82,500 + 30% × (700,000 − 500,000) = 82,500 + 60,000 = **C$142,500.00**.

### Prohibitions

- NEVER cap the INSS base — there is no maximum insurable salary ("sin techo") since Decreto 06-2019.
- NEVER compute INSS or IR on net salary — both use GROSS salary (less employee INSS for the IR base only).
- NEVER apply the progressive IR schedule to a non-resident — non-residents pay 20% definitive WHT.
- NEVER tax foreign-source income — Nicaragua is territorial; confirm source first.
- NEVER quantify penalties, surcharges, or mantenimiento de valor — the figures are unconfirmed; escalate.
- NEVER present the INSS sub-component split (IVM/Salud/RP/Guerra) as authoritative — only the 7.00% / 21.50% / 22.50% totals are PwC-confirmed.
- NEVER confuse DGI (income tax, IR-122) debits with INSS (social security) debits — separate authorities.
- NEVER assume employer size — the ≤50 vs >50 rate difference is material; confirm or flag.
- NEVER present figures as definitive — label as estimated and direct the client to their INSS planilla and DGI account.
- NEVER skip reviewer escalation on special regimes (Zona Franca, mining, fishing).

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
