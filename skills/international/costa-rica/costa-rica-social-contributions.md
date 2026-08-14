---
name: costa-rica-social-contributions
description: Use this skill whenever asked about Costa Rica social-security / payroll contributions ("cargas sociales") to the CCSS and the related employment-income withholding. Trigger on phrases like "how much CCSS do I pay", "cargas sociales Costa Rica", "CCSS employer cost", "patrono CCSS", "cuota obrero-patronal", "IVM contribution", "SEM CCSS", "planilla CCSS", "Banco Popular deduction", "FODESAF", "INA exemption", "deducciones de planilla", "retención del impuesto al trabajo dependiente", "Costa Rica payroll tax", "social charges 2025/2026", "trabajador independiente CCSS", or any question about Costa Rican employer/employee social contributions, the monthly salary-tax withholding, the minimum contribution base (BMC), or net-pay computation. Also trigger when classifying bank-statement lines that relate to CCSS planilla debits, SICERE payments, INS riesgos-del-trabajo premiums, Banco Popular debits, or D-103 withholding remittances on BAC, BN, BCR, Davivienda, or other Costa Rican bank statements. This skill covers the SEM and IVM rates (including the confirmed 1 Jan 2026 IVM increase), FODESAF/IMAS/INA/FCL/ROP/Banco Popular components, the INS work-risk premium, employer and employee totals, the BMC floor, the monthly progressive salary-tax brackets, family tax credits, aguinaldo treatment, minimum wage, forms D-103/D-101/D-151, the CCSS planilla cycle, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Costa Rican payroll / social-contribution work.
version: 0.1
jurisdiction: CR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Costa Rica Social-Security Contributions (Cargas Sociales) & Salary-Tax Withholding —

## Costa Rica Social-Security Contributions (Cargas Sociales) & Salary-Tax Withholding — Skill v0.1

**Tier 2 (research-verified). Confidence: medium.** Several primary authority PDFs (Hacienda CP-103-2024, live CCSS pages, BDO/BLP, OECD) returned HTTP errors during research, so figures were corroborated from multiple secondary tax/legal sources (PwC, BDO, La Nación, EY, BLP, siemprealdía) rather than read off every authority page. Every figure carries an inline citation or an explicit `[RESEARCH GAP — reviewer to confirm]` marker. A Costa Rican CPA / contador público autorizado must sign off before any output is filed or relied upon.

## Section 1 — Quick reference

**Read this whole section before computing or classifying anything.**

- **Country** — Costa Rica (República de Costa Rica)
- **Currency** — CRC — Costa Rican colón (₡) only
- **Social-insurance authority** — Caja Costarricense de Seguro Social (CCSS) — https://www.ccss.sa.cr; collected via SICERE / Oficina Virtual
- **Income-tax authority** — Ministerio de Hacienda — Dirección General de Tributación (DGT), https://www.hacienda.go.cr
- **Minimum-wage authority** — Consejo Nacional de Salarios (CNS), under MTSS — https://www.mtss.go.cr
- **Primary social legislation** — Ley Constitutiva de la CCSS (Ley No. 17); Ley de Protección al Trabajador (LPT, Ley No. 7983 — FCL, ROP/OPC, Banco Popular worker quota)
- **Supporting legislation** — Reglamento del Seguro de Salud; Reglamento del Seguro de IVM; Reglamento para el Aseguramiento Contributivo de los Trabajadores Independientes; Ley del Impuesto sobre la Renta (Ley No. 7092)
- **Tax basis** — TERRITORIAL — only Costa Rican-source income is taxed, regardless of nationality or residence  _(PwC)_
- **Employer total social charge** — ≈26.67% of gross (2025) → ≈26.83% (from 1 Jan 2026)  _(siemprealdía, La Nación, BDO)_
- **Employee total deduction** — ≈10.67% of gross (2025) → ≈10.83% (from 1 Jan 2026)  _(siemprealdía, BDO)_
- **Salary-tax (impuesto al trabajo dependiente)** — Monthly progressive, 0% to 25% — see Section 5  _(Decreto 44772-H, Hacienda)_
- **Income-tax-exempt monthly salary (2025)** — ₡922,000/month  _(Decreto 44772-H)_
- **Minimum wage (unskilled generic, 2026)** — ₡373,092.42/month, effective 1 Jan 2026 (general +1.63%)  _(CNS/MTSS)_
- **Social-contribution filing** — CCSS planilla via SICERE / Oficina Virtual, monthly
- **Withholding return** — Form D-103 — first 15 calendar days of the following month
- **Validated by** — Pending — requires sign-off by a Costa Rican CPA / contador público autorizado
- **Validation date** — Pending

**Component overview (2025, % of gross salary)**  _(siemprealdía, CCSS, La Nación, BDO, EY, remotepeople)_

placeholder

**Component overview (2025, % of gross salary)**  _(siemprealdía, CCSS, La Nación, BDO, EY, remotepeople)_

| Fund | Employer | Employee | Source |
| --- | --- | --- | --- |
| CCSS SEM (Seguro de Enfermedad y Maternidad — health & maternity) | 9.25% | 5.50% | siemprealdía, CCSS |
| CCSS IVM (Invalidez, Vejez y Muerte — pension) | 5.42% | 4.17% | La Nación, BDO, EY, siemprealdía |
| FODESAF / Asignaciones Familiares (family allowances) | 5.00% | 0% | siemprealdía |
| IMAS (Instituto Mixto de Ayuda Social) | 0.50% | 0% | siemprealdía |
| INA (Instituto Nacional de Aprendizaje — vocational training) | 1.50% | 0% | siemprealdía (exempt for some employers — see Rule 6) |
| Banco Popular y de Desarrollo Comunal | 0.50% | 1.00% | siemprealdía |
| FCL — Fondo de Capitalización Laboral (LPT) | 1.50% | 0% | siemprealdía, LPT |
| ROP / OPC — pensión complementaria obligatoria (LPT) | 2.00% | 0% | siemprealdía, LPT |
| INS — Riesgos del Trabajo (workplace-risk premium) | ~1.00% referential | 0% | remotepeople (activity/risk-class dependent — see Rule 7) |
| **TOTAL (2025)** | **≈26.67%** | **≈10.67%** | siemprealdía, La Nación, BDO |

Employer component arithmetic (2025): 9.25 + 5.42 + 5.00 + 0.50 + 1.50 + 0.50 + 1.50 + 2.00 = 25.67%, plus INS ~1.00% = **26.67%**. Employee: 5.50 + 4.17 + 1.00 = **10.67%**. (Both totals reconcile to the official figures cited above.)

**2026 changes (effective 1 Jan 2026)**  _(CCSS noticia, La Nación, BDO, EY)_

| Fund | Employer 2025 → 2026 | Employee 2025 → 2026 | State 2025 → 2026 | Source |
| --- | --- | --- | --- | --- |
| CCSS IVM | 5.42% → 5.58% (+0.16pp) | 4.17% → 4.33% (+0.16pp) | 1.57% → 1.75% | CCSS noticia, La Nación, BDO, EY |
| All other funds | unchanged | unchanged | — | siemprealdía |
| **TOTAL** | **≈26.67% → ≈26.83%** | **≈10.67% → ≈10.83%** | — | BDO, La Nación |

IVM increase is +0.16pp on each of employer and employee, effective 1 Jan 2026 through 31 Dec 2028; worker IVM share is scheduled to keep rising toward a target ~12.16% total IVM by 2029 (La Nación, EY). 2026 employer: 25.67 − 5.42 + 5.58 = 25.83% + INS 1.00% = **26.83%**. 2026 employee: 5.50 + 4.33 + 1.00 = **10.83%**.

## Section 1A — Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Employer total social charge | Use 26.67% of gross for 2025 / 26.83% from 1 Jan 2026; treat INS work-risk as ~1% referential and flag that the real rate is set by the occupational risk class (siemprealdía, BDO) |
| Employee total deduction | 10.67% of gross for 2025 / 10.83% from 1 Jan 2026 (SEM 5.50% + IVM 4.17%/4.33% + Banco Popular 1.00%) |
| Low-wage contribution base | If gross salary is below the CCSS BMC (≈₡333,328 SEM / ≈₡311,990 IVM for 2025), compute contributions on the BMC, not the actual lower salary (CCSS BMC data) |
| Aguinaldo (13th-month) | Exclude from BOTH CCSS social charges and income tax (PwC, MTSS) |
| Unknown which year applies | Ask the period; if the payroll month is on/after Jan 2026, use the 2026 IVM rates |
| Unknown employer size (INA exemption) | Assume INA 1.50% APPLIES (do not drop it) until headcount is confirmed (BDO) |
| Unknown INS risk class | Use ~1% referential and flag for reviewer; do not present as final |
| Self-employed / trabajador independiente | Do NOT apply the fixed employer/employee split — use the graduated five-tier net-income scale; flag for reviewer (Reglamento del Trabajador Independiente) |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — gross monthly salary (₡), payroll month/year (to pick 2025 vs 2026 rates), and worker type (dependent employee vs trabajador independiente). Without the gross salary and the period, STOP.

**Recommended** — employer headcount and whether agricultural (for the INA exemption), occupational risk class (for INS), number of dependent children and whether a spouse is claimed (for family tax credits), and whether the amount is ordinary salary or aguinaldo.

**Ideal** — the CCSS planilla detail (per-fund breakdown), the employer's INS riesgos-del-trabajo policy rate, prior D-103 filings, and for self-employed clients the current CCSS independent-worker contribution scale.

### Refusal catalogue

- **R-CR-SOC-1 — Period unknown** — Trigger: the payroll month/year is not provided. Message: "The IVM rate changed on 1 January 2026 (employer 5.42% → 5.58%, employee 4.17% → 4.33%). I cannot compute contributions without knowing which payroll period applies."
- **R-CR-SOC-2 — Self-employed contribution amount** — Trigger: client asks for the exact CCSS cuota of a trabajador independiente. Message: "Independent-worker contributions follow a graduated five-tier scale by net-income band, not the fixed employer/employee split, and the scale and BMC figures must be read off the current CCSS regulation. I can flag the framework, but a Costa Rican CPA must confirm the exact tier and amount."
- **R-CR-SOC-3 — CCSS arrears / penalties** — Trigger: client has unpaid cuotas obrero-patronales or asks to quantify CCSS penalties/interest. Message: "CCSS pursues administrative and judicial collection (cobro judicial) with interest and fines on overdue cuotas; the precise rates are not confirmed in this skill `[RESEARCH GAP — reviewer to confirm]`. Do not estimate arrears — escalate to a Costa Rican CPA and request a CCSS statement."
- **R-CR-SOC-4 — INS work-risk rate** — Trigger: client needs the exact riesgos-del-trabajo premium. Message: "The INS work-risk premium is set per occupational risk class; ~1% is only referential. The exact rate must come from the employer's INS policy. Flag for reviewer."
- **R-CR-SOC-5 — Expat / cross-border source** — Trigger: foreign-source income or treaty questions. Message: "Costa Rica taxes on a territorial basis (Costa Rican-source income only). Cross-border, treaty, and totalization questions are outside this skill — escalate to a Costa Rican CPA."

## Section 3 — Payment pattern library

Deterministic pre-classifier for Costa Rican bank-statement transactions related to social charges and salary-tax withholding. Match by case-insensitive substring on the counterparty/reference as it appears on the statement. CCSS, INS-risk, Banco Popular, and D-103 remittances all EXCLUDE from any IVA (VAT) return — they are statutory payroll obligations, not taxable supplies.

### 3.1 CCSS planilla debits (employer social-contribution payment)

**CCSS planilla debits patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CCSS, C.C.S.S., CAJA COSTARRICENSE | EXCLUDE — CCSS planilla payment | Monthly cuota obrero-patronal |
| SICERE | EXCLUDE — CCSS planilla payment | CCSS collection system |
| PLANILLA CCSS, CUOTA OBRERO PATRONAL | EXCLUDE — CCSS planilla payment | Explicit reference |
| SEGURO SOCIAL, SEM, IVM | EXCLUDE — CCSS planilla payment | Fund references |

### 3.2 Other statutory payroll funds

**Other statutory payroll funds patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INS, RIESGOS DEL TRABAJO, POLIZA RIESGOS | EXCLUDE — INS work-risk premium | Mandatory occupational-accident policy |
| BANCO POPULAR, BP DESARROLLO COMUNAL | EXCLUDE — Banco Popular LPT quota | Worker 1.00% + employer 0.50% |
| FODESAF, ASIGNACIONES FAMILIARES | EXCLUDE — family-allowance charge | Employer-only |
| INA, APRENDIZAJE | EXCLUDE — vocational-training charge | Employer-only (exempt for some — Rule 6) |

### 3.3 Income-tax withholding remittances (NOT CCSS — do not confuse)

**Income-tax withholding remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HACIENDA, TRIBUTACION, DGT | EXCLUDE — tax remittance, not CCSS | Ministry of Finance |
| D-103, RETENCION FUENTE | EXCLUDE — salary-tax withholding remittance | Monthly D-103, not a social charge |
| D-101, IMPUESTO RENTA | EXCLUDE — annual income tax | Self-employed / business return |

### 3.4 Salary / payroll outflows (exclude from social-charge classification)

**Salary / payroll outflows patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, PLANILLA NETA, PAGO QUINCENA | EXCLUDE — net wage payment | The employee's net pay, not a contribution |
| AGUINALDO | EXCLUDE — 13th-month bonus | Exempt from CCSS and income tax (Rule 9) |

### 3.5 Incoming CCSS credits (benefits received — not contributions)

**Incoming CCSS credits patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CCSS INCAPACIDAD, SUBSIDIO | EXCLUDE — sickness/maternity benefit received | Not a contribution paid |
| PENSION IVM, PENSION CCSS | EXCLUDE — pension income received | Taxable income, not a deduction |

## Section 4 — Worked examples

Six bank-statement / payroll classifications for a hypothetical San José services SME and its employees. All figures in CRC (₡). All rates as cited in Sections 1 and 5.

### Example 1 — Employee net pay, mid-range salary (2025)

**Input:** Dependent employee, gross ₡2,000,000/month, payroll June 2025, no children/spouse claimed.

**Reasoning:**
- Employee social deductions = 10.67% × 2,000,000 = **₡213,400** (SEM 5.50% = 110,000; IVM 4.17% = 83,400; Banco Popular 1.00% = 20,000) (siemprealdía, BDO).
- Salary tax (monthly brackets, Decreto 44772-H): first ₡922,000 at 0% = 0; (1,352,000 − 922,000) = 430,000 × 10% = 43,000; (2,000,000 − 1,352,000) = 648,000 × 15% = 97,200. Total salary tax = **₡140,200**.
- Net pay = 2,000,000 − 213,400 − 140,200 = **₡1,646,400**.
- Employer cost on top of gross = 26.67% × 2,000,000 = **₡533,400**; total employer outlay = **₡2,533,400**.

**Classification:** CCSS planilla and D-103 remittances EXCLUDE from IVA. Salary tax withheld and remitted on D-103.

### Example 2 — Same employee, payroll January 2026 (IVM increase)

**Input:** Same ₡2,000,000 gross, payroll January 2026.

**Reasoning:**
- Employee social deductions = 10.83% × 2,000,000 = **₡216,600** (SEM 5.50% = 110,000; IVM 4.33% = 86,600; Banco Popular 1.00% = 20,000) (CCSS noticia, La Nación). The change vs 2025 is +₡3,200 (the +0.16pp IVM rise).
- Salary tax unchanged at this gross (2026 monthly brackets `[RESEARCH GAP — 2026 monthly salary-tax brackets not separately confirmed; 2025 brackets used]`) = **₡140,200** if 2025 brackets still apply.
- Employer cost = 26.83% × 2,000,000 = **₡536,600**.

**Classification:** EXCLUDE from IVA. Flag the bracket-year assumption for reviewer.

### Example 3 — Low-wage employee below the BMC (2025)

**Input:** Part-time employee, gross ₡250,000/month, payroll 2025.

**Reasoning:**
- ₡250,000 is below both the SEM BMC (≈₡333,328) and IVM BMC (≈₡311,990) for 2025 (CCSS BMC data). Contributions are computed on the BMC, not on ₡250,000 (Rule 4 / Default).
- Employee SEM = 5.50% × 333,328 = ₡18,333; IVM = 4.17% × 311,990 = ₡13,010; Banco Popular = 1.00% × 250,000 = ₡2,500 `[RESEARCH GAP — whether the Banco Popular 1% also uses the BMC floor or the actual salary not confirmed; reviewer to confirm]`.
- Salary is far below ₡922,000, so **no salary tax** is due.

**Classification:** EXCLUDE from IVA. Flag the BMC grossing-up and the Banco Popular base for reviewer.

### Example 4 — CCSS planilla debit on the bank statement (BAC)

**Input line:**
`05/07/2025 ; CCSS SICERE PLANILLA JUN ; DEBITO ; CUOTA OBRERO PATRONAL ; -2.450.000 ; CRC`

**Reasoning:** Matches "CCSS SICERE PLANILLA" (pattern 3.1). This is the monthly employer cuota obrero-patronal for the June planilla, paid in the early-July window (reporting window ~26th to the 4th business day of the following month). It bundles SEM, IVM, FODESAF, IMAS, INA, FCL, ROP and the Banco Popular quotas.

**Classification:** EXCLUDE from IVA — statutory payroll obligation. Reconcile against the planilla detail.

### Example 5 — D-103 withholding remittance (NOT CCSS)

**Input line:**
`12/07/2025 ; MINISTERIO HACIENDA D-103 ; DEBITO ; RETENCION FUENTE JUN ; -310.000 ; CRC`

**Reasoning:** Matches "MINISTERIO HACIENDA D-103" (pattern 3.3). This is the monthly salary-tax withholding remittance (impuesto al trabajo dependiente), due within the first 15 calendar days of the following month — NOT a social charge. Do not classify as CCSS.

**Classification:** EXCLUDE from IVA — income-tax remittance, not a social contribution.

### Example 6 — Aguinaldo payment (exempt)

**Input line:**
`18/12/2025 ; PLANILLA AGUINALDO 2025 ; DEBITO ; 13 SALARIO ; -1.800.000 ; CRC`

**Reasoning:** Matches "AGUINALDO" (pattern 3.4). The mandatory 13th-month salary, payable by 20 December, is exempt from BOTH CCSS social charges and income tax (PwC, MTSS). No CCSS or D-103 withholding applies to this line.

**Classification:** EXCLUDE from IVA. No social charge, no salary tax. Confirm it is the genuine aguinaldo (~1/12 of Dec–Nov earnings), not an ordinary bonus.

## Section 5 — Tier 1 rules

Apply exactly as written when inputs are clear.

### Rule 1 — Territorial basis

- **Territorial basis** — Costa Rica taxes individuals on Costa Rican-source income only, regardless of nationality or residence. Foreign-source income of a Costa Rican resident is outside scope.  _(PwC)_

### Rule 2 — Employment-income (salary) tax — monthly progressive brackets, 2025

Withheld monthly by the employer; −0.79% adjustment vs 2024; effective 1 Jan–31 Dec 2025 (Decreto 44772-H, Hacienda).

**Monthly progressive brackets 2025**  _(Decreto 44772-H, Hacienda)_

| Monthly band (₡) | Rate | Tax on band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 – 922,000 | 0% | 0 | ₡0 |
| 922,000 – 1,352,000 | 10% | up to 43,000 | ₡43,000 |
| 1,352,000 – 2,373,000 | 15% | up to 153,150 | ₡196,150 |
| 2,373,000 – 4,745,000 | 20% | up to 474,400 | ₡670,550 |
| over 4,745,000 | 25% | — | (₡670,550 + 25% of excess) |

Cumulative check: 43,000; 43,000 + (2,373,000−1,352,000)×15% = 43,000 + 153,150 = 196,150; 196,150 + (4,745,000−2,373,000)×20% = 196,150 + 474,400 = 670,550. ✓

### Rule 3 — Family tax credits (créditos fiscales), 2025

- **Family tax credits** — Credited against the employee's salary-tax withholding: ₡1,710/month per child and ₡2,590/month per spouse. Apply after computing gross salary tax.  _(Decreto 44772-H)_

### Rule 4 — Minimum contribution base (BMC)

- **Minimum contribution base (BMC)** — For low earners, compute CCSS contributions on the BMC, not the actual lower salary: SEM BMC ≈ ₡333,328/month and IVM BMC ≈ ₡311,990/month for 2025. Salaries below are grossed up to the BMC.  _(CCSS BMC data)_

### Rule 5 — Total social charges

- **Total social charges** — 2025: employer ≈26.67% + employee ≈10.67% of gross. From 1 Jan 2026: employer ≈26.83% + employee ≈10.83%. Component breakdown per Section 1.  _(siemprealdía, La Nación, BDO)_

### Rule 6 — INA small-employer exemption

- **INA small-employer exemption** — Non-agricultural employers with fewer than 5 permanent employees are exempt from the 1.50% INA contribution, lowering their employer total by 1.50pp (e.g. ~25.17% in 2025).  _(BDO, BLP)_

### Rule 7 — INS work-risk premium is risk-class specific

- **INS work-risk premium risk-class specific** — The mandatory póliza de riesgos del trabajo with INS is set per occupational risk classification; ~1% is only referential. Some "CCSS-only" quotes of ~26.5% exclude it. Always flag the actual rate for reviewer.  _(remotepeople)_

### Rule 8 — Banco Popular split

- **Banco Popular split** — Worker contributes 1.00% (mandatory savings under the LPT); employer contributes 0.50% total. The LPT-funded employer components (Banco Popular 0.50%, FCL 1.50%, ROP/OPC 2.00%) reconcile to the official employer total, but the line allocation is worded differently across sources `[RESEARCH GAP — confirm the ROP vs Banco Popular split against the CCSS planilla rate schedule]`.  _(siemprealdía)_

### Rule 9 — Aguinaldo

- **Aguinaldo** — The mandatory 13th-month salary (~1/12 of Dec–Nov total earnings), payable by 20 December, is exempt from both CCSS social charges and income tax.  _(PwC, MTSS)_

### Rule 10 — Minimum wage

- **Minimum wage** — Unskilled generic worker (trabajador no calificado genérico): ₡373,092.42/month, effective 1 Jan 2026 (general +1.63% increase). Differentiated 2026 increases: domestic work +3.96%, specialized +2.18%, mid-level diversified-education technicians +2.50%. 2025 base ≈ ₡367,108 `[RESEARCH GAP — derived by backing out the 1.63% increase; the exact 2025 decree amount was not read directly]`.  _(CNS/MTSS)_

### Rule 11 — Self-employed (trabajador independiente)

- **Self-employed contribution framework** — Independent workers must enroll with CCSS once monthly net income exceeds the reference income (≈₡327,338/month, the SEM BMC, 2025). Their contribution % follows a graduated five-tier scale by net-income band, not the fixed employer/employee split. Do not apply the employee 10.67% to a self-employed person.  _(Reglamento del Trabajador Independiente, CCSS)_

### Rule 12 — Self-employment / business profit (utilidades) — annual brackets, 2026 period

**Utilidades annual brackets, 2026 period**  _(PwC)_

| Annual band (₡) | Rate |
| --- | --- |
| 0 – 4,094,000 | 0% |
| 4,094,000 – 6,115,000 | 10% |
| 6,115,000 – 10,200,000 | 15% |
| 10,200,000 – 20,442,000 | 20% |
| over 20,442,000 | 25% |

`[RESEARCH GAP — these are 2026-period figures; the 2025 utilidades brackets were not separately isolated.]`

### Rule 13 — Filing

**Filing table**

| Item | Detail | Deadline | Source |
| --- | --- | --- | --- |
| D-103 (withholding return) | Monthly retención en la fuente — salaries, allowances, dividends, remittances abroad | First 15 calendar days of the following month | BLP, PwC |
| CCSS planilla (SICERE) | Monthly employer social-contribution return and payment | Reporting window ~26th of month to the 4th business day of the next month | Section 4 / general practice |
| D-101 (annual income tax) | Self-employed / businesses; calendar fiscal year Jan–Dec | ~15/16 March | PwC |
| D-151 (annual informative) | Summary of clients, suppliers, specified payments/withholdings | Last business day of February | PwC |

### Rule 14 — Non-resident withholding

- **Non-resident withholding** — 25% withholding applies to personal services from a Costa Rican source paid to non-residents (remesas al exterior); reported on Form D-103.  _(PwC)_

## Section 6 — Tier 2 catalogue (reviewer judgement)

Flag these for a Costa Rican CPA when data is ambiguous.

### T2-1 — INA exemption eligibility

- **INA exemption eligibility** — Trigger: employer near the 5-permanent-employee threshold or agricultural. Issue: the 1.50% INA drop applies only to non-agricultural employers with fewer than 5 permanent employees; headcount and sector must be confirmed. Action: flag; default to INA applying until confirmed.

### T2-2 — INS risk-class rate

- **INS risk-class rate** — Trigger: exact employer cost requested. Issue: ~1% is referential only; the póliza rate depends on the activity's risk class. Action: request the INS policy; flag.

### T2-3 — Self-employed contribution tier

- **Self-employed contribution tier** — Trigger: trabajador independiente needs a cuota amount. Issue: five-tier graduated scale by net-income band, not a fixed %. Action: read the current CCSS regulation; flag. `[RESEARCH GAP — the 2025 scale table and current BMC figures should be confirmed on the live CCSS/SCIJ regulation.]`

### T2-4 — LPT component allocation

- **LPT component allocation** — Trigger: per-fund employer breakdown must match the planilla exactly. Issue: Banco Popular 0.50% / FCL 1.50% / ROP 2.00% allocation is worded differently across sources though the total reconciles. Action: reconcile against the CCSS planilla rate schedule; flag.

### T2-5 — 2026 salary-tax brackets

- **2026 salary-tax brackets** — Trigger: salary-tax computation for a 2026 payroll period. Issue: only the 2025 monthly brackets are confirmed in this skill. Action: confirm the 2026 Decreto brackets before withholding. `[RESEARCH GAP — 2026 monthly salary-tax brackets not confirmed.]`

### T2-6 — CCSS / Hacienda penalties and arrears

- **CCSS / Hacienda penalties and arrears** — Trigger: late payment, non-registration, or arrears. Issue: precise interest/penalty rates not captured. Action: do not estimate; escalate. `[RESEARCH GAP — penalty/interest rates not confirmed from an authoritative source.]`

## Section 7 — Excel working paper template

```
COSTA RICA PAYROLL / CARGAS SOCIALES — WORKING PAPER
Client: [name]            Employee: [name]
Payroll period: [MM/YYYY]  Prepared: [date]
Rate set (auto from period): [2025 / 2026 IVM]

INPUT DATA
  Gross monthly salary:            CRC [____]
  Worker type:                     [Dependent employee / Trabajador independiente]
  Employer headcount / agri?:      [____]  (INA exemption test)
  INS risk class / policy rate:    [____]  (default ~1% referential)
  Children claimed:                [____]   Spouse claimed: [Y/N]
  Ordinary salary or aguinaldo:    [____]

CONTRIBUTION BASE
  BMC test — SEM floor ₡333,328 / IVM floor ₡311,990 (2025):  [actual / grossed-up]
  Base used:                       CRC [____]

EMPLOYEE DEDUCTIONS                 Rate      Amount
  SEM                              5.50%     CRC [____]
  IVM (4.17% 2025 / 4.33% 2026)    [____]    CRC [____]
  Banco Popular                    1.00%     CRC [____]
  TOTAL employee (10.67%/10.83%)             CRC [____]

EMPLOYER CONTRIBUTIONS              Rate      Amount
  SEM 9.25% / IVM 5.42%(5.58%) / FODESAF 5.00% / IMAS 0.50%
  INA 1.50% (if applicable) / Banco Popular 0.50% / FCL 1.50% / ROP 2.00%
  INS riesgos ~1.00% (risk-class)
  TOTAL employer (26.67%/26.83%)             CRC [____]

SALARY TAX (monthly brackets, 2025)
  Gross salary tax:                          CRC [____]
  Less child credits (₡1,710 each):          CRC [____]
  Less spouse credit (₡2,590):               CRC [____]
  Net salary tax withheld (D-103):           CRC [____]

NET PAY = Gross − employee deductions − net salary tax:   CRC [____]
TOTAL EMPLOYER OUTLAY = Gross + employer contributions:   CRC [____]

REVIEWER FLAGS / RESEARCH GAPS
  [List]
```

## Section 8 — Bank statement reading guide

### How payroll obligations appear on Costa Rican bank statements

**BAC Credomatic / Banco Nacional (BN) / Banco de Costa Rica (BCR) / Davivienda / Scotiabank:**
- CCSS planilla: "CCSS", "SICERE", "PLANILLA CCSS", "CAJA COSTARRICENSE", "CUOTA OBRERO PATRONAL"
- INS work-risk: "INS", "RIESGOS DEL TRABAJO", "POLIZA RIESGOS"
- Salary-tax remittance: "HACIENDA", "TRIBUTACION", "D-103", "RETENCION FUENTE"
- Banco Popular quota: "BANCO POPULAR", "BP DESARROLLO COMUNAL"
- Net wages: "SALARIO", "PLANILLA NETA", "PAGO QUINCENA"; bonus: "AGUINALDO"

**Spanish ↔ English glossary:**
- *Cargas sociales* = social charges; *cuota obrero-patronal* = employee+employer contribution
- *Planilla* = payroll / contribution return; *patrono* = employer
- *Retención en la fuente* = withholding at source; *aguinaldo* = 13th-month salary
- *Débito / Crédito* = debit / credit; *salario bruto / neto* = gross / net salary
- *Trabajador independiente* = self-employed worker; *BMC (base mínima contributiva)* = minimum contribution base

**Key identification tips:**
1. CCSS planilla debits are monthly and outgoing, in the ~26th-to-4th-business-day window.
2. The planilla amount bundles all funds; do not split unless you have the planilla detail.
3. D-103 (Hacienda) is income-tax withholding, NOT a social charge — keep them separate.
4. Aguinaldo lines (December) carry no social charge and no salary tax.
5. Incoming CCSS credits are benefits received, not contributions.

## Section 9 — Onboarding fallback

If the client provides only a bank statement and no payroll detail:

1. **Scan for CCSS / SICERE debits** — identify monthly outgoing planilla payments (Section 3.1).
2. **Separate Hacienda D-103** withholding remittances (income tax) from CCSS (social charges).
3. **Estimate gross payroll:** a CCSS planilla debit ≈ 26.67% (2025) / 26.83% (2026) of total gross; reverse to approximate gross = planilla ÷ 0.2667 (employer share). Flag as an estimate.
4. **Check December** for an aguinaldo line (exempt — exclude from both bases).
5. **Flag for reviewer:** "Payroll figures derived from bank-statement amounts only; per-fund split, BMC grossing-up, INA exemption, INS risk class, and salary-tax withholding have not been independently verified. A Costa Rican CPA must confirm before filing."

## Section 10 — Reference material

### Thresholds

**Thresholds table**

| Name | Value | Source |
| --- | --- | --- |
| Income-tax-exempt monthly salary (2025) | ₡922,000/month (at/below = 0% salary tax) | Decreto 44772-H |
| CCSS SEM minimum contribution base (BMC) 2025 | ≈₡333,328/month | CCSS BMC data |
| CCSS IVM minimum contribution base 2025 | ≈₡311,990/month | CCSS BMC data |
| Independent-worker mandatory-affiliation reference income (2025) | ≈₡327,338/month (SEM BMC) | Reglamento del Trabajador Independiente |
| INA exemption | Non-agricultural employers with fewer than 5 permanent employees | BDO, BLP |
| Family credit — per child (2025) | ₡1,710/month | Decreto 44772-H |
| Family credit — spouse (2025) | ₡2,590/month | Decreto 44772-H |
| Minimum wage (unskilled generic, 2026) | ₡373,092.42/month | CNS/MTSS |
| Non-resident services withholding | 25% (remesas al exterior) | PwC |

### Penalties

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| CCSS late/non-payment | Interest + fines on overdue cuotas; administrative + judicial collection (cobro judicial), liens | siemprealdía; rate `[RESEARCH GAP — verify with CCSS]` |
| Failure to register employees with CCSS | Retroactive assessment of all contributions plus fines and surcharges | CCSS patronos |
| Income-tax / withholding non-compliance | Late-filing + late-payment penalties plus interest (Código de Normas y Procedimientos Tributarios) | DGT; 2025 amounts `[RESEARCH GAP — verify with Hacienda]` |

### Test suite

Recompute each end-to-end before relying on it.

**Test 1 — Employee deductions, 2025.** Gross ₡1,000,000. Employee = 10.67% = **₡106,700** (SEM 55,000 + IVM 41,700 + BP 10,000). Salary tax: (1,000,000 − 922,000) × 10% = **₡7,800**. Net = 1,000,000 − 106,700 − 7,800 = **₡885,500**.

**Test 2 — Employee deductions, 2026.** Gross ₡1,000,000. Employee = 10.83% = **₡108,300** (SEM 55,000 + IVM 43,300 + BP 10,000). +₡1,600 vs 2025 from the IVM rise.

**Test 3 — Employer cost, 2025.** Gross ₡1,000,000. Employer = 26.67% = **₡266,700**. Total outlay = **₡1,266,700**.

**Test 4 — Employer cost, 2026.** Gross ₡1,000,000. Employer = 26.83% = **₡268,300**.

**Test 5 — Below-BMC employee, 2025.** Gross ₡250,000 (< BMC). SEM on 333,328 = 5.50% = ₡18,333; IVM on 311,990 = 4.17% = ₡13,010. No salary tax (< ₡922,000).

**Test 6 — High earner salary tax, 2025.** Gross ₡5,000,000. Salary tax = 670,550 + (5,000,000 − 4,745,000) × 25% = 670,550 + 63,750 = **₡734,300**.

**Test 7 — INA small employer, 2025.** Non-agricultural employer with 4 permanent employees → drop INA 1.50% → employer total ≈ **25.17%**.

**Test 8 — Aguinaldo.** ₡1,800,000 December aguinaldo → **₡0** CCSS, **₡0** salary tax (exempt).

**Test 9 — Family credits, 2025.** Gross ₡2,000,000, 2 children + spouse. Gross salary tax ₡140,200 (per Example 1) − (2 × ₡1,710) − ₡2,590 = 140,200 − 3,420 − 2,590 = **₡134,190** net withholding.

**Test 10 — Self-employed.** Trabajador independiente, net income ₡500,000/month → enroll with CCSS (> ₡327,338); contribution via five-tier scale, NOT 10.67%. Flag for reviewer.

### Prohibitions

- NEVER apply the employee 10.67%/10.83% split to a self-employed person — use the CCSS five-tier independent-worker scale.
- NEVER compute contributions on a sub-BMC salary without grossing up to the BMC floor.
- NEVER use 2025 IVM rates for a payroll period on/after 1 January 2026 (or vice versa).
- NEVER charge CCSS or salary tax on the aguinaldo — it is exempt from both.
- NEVER present the INS work-risk premium (~1%) as final — it is risk-class specific.
- NEVER drop the 1.50% INA without confirming the employer is non-agricultural with fewer than 5 permanent employees.
- NEVER conflate the D-103 income-tax remittance with the CCSS planilla — they are separate obligations to separate authorities.
- NEVER quantify CCSS or Hacienda arrears/penalties — escalate; rates are a research gap.
- NEVER treat foreign-source income as taxable — Costa Rica is territorial.
- NEVER present any figure marked `[RESEARCH GAP]` as confirmed without a Costa Rican CPA's sign-off.

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
