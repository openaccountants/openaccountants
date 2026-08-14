---
name: nicaragua-income-tax
description: Use this skill whenever asked about Nicaragua income tax (Impuesto sobre la Renta, IR) on employment income — rentas del trabajo. Trigger on phrases like "how much tax do I pay in Nicaragua", "Impuesto sobre la Renta", "IR rentas del trabajo", "retención IR", "IR-122", "IR-106", "annual income tax return Nicaragua", "INSS laboral", "córdoba tax", "DGI", "payroll income tax Nicaragua", "exempt threshold C$100,000", or any question about computing or filing income tax on salary for a Nicaraguan resident employee. Also trigger when preparing or reviewing monthly IR withholding, annualizing a salary to the progressive scale, computing the deductible 7% INSS laboral before IR, or advising on the annual IR-106 filing obligation. This skill covers the progressive employment-income scale (exempt up to C$100,000/yr, then 15/20/25/30%), the deductibility of INSS laboral, monthly withholding via IR-122, the annual IR-106 return, non-resident definitive withholding, and the interaction with INSS. ALWAYS read this skill before touching any Nicaragua income-tax work.
version: 0.1
jurisdiction: NI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nicaragua Income Tax -- Rentas del Trabajo

## Nicaragua Income Tax -- Rentas del Trabajo Skill v0.1

> **DISAMBIGUATION:** "NI" in this skill means **NICARAGUA**, the Central American republic. It does **NOT** mean Northern Ireland or UK National Insurance. There is no HMRC, no pound sterling, and no UK content anywhere in this skill. Currency is the **córdoba (C$ / NIO)**. The tax authority is the **DGI (Dirección General de Ingresos)**. Social security is administered by **INSS (Instituto Nicaragüense de Seguridad Social)**.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Nicaragua (República de Nicaragua) |
| Tax | Impuesto sobre la Renta (IR) — rentas del trabajo (employment income) |
| Currency | Córdoba (C$ / NIO) only |
| Tax year | Calendar year (1 January -- 31 December); other 12-month periods only by DGI authorization |
| Primary legislation | Ley No. 822, Ley de Concertación Tributaria (LCT) |
| Supporting legislation | Ley No. 891 (reform to the LCT); LCT Art. 23 (progressive scale); LCT Art. 19–22 (rentas del trabajo, deductions) |
| Tax authority | DGI — Dirección General de Ingresos |
| Social security | INSS — Instituto Nicaragüense de Seguridad Social |
| Training levy | INATEC (2%, employer-paid only) |
| Monthly withholding form | IR-122 (employer withholds and remits monthly) |
| Annual individual return | IR-106 (due within 90 days after year-end, ~31 March) |
| Validated by | Pending — requires sign-off by a Nicaraguan licensed accountant (Contador Público Autorizado, CCPN) |
| Validation date | Pending |
| Skill version | 0.1 |

### Progressive Annual Scale — Rentas del Trabajo (2025)

**Progressive Annual Scale — Rentas del Trabajo (2025)**  _(LCT (Ley 822) Art. 23, as reformed by Ley 891)_

| Annual taxable income (C$) | Base tax (C$) | % on excess over lower bound | Lower bound (C$) |
| --- | --- | --- | --- |
| 0.01 -- 100,000.00 | 0.00 | 0% (exempt) | 0.00 |
| 100,000.01 -- 200,000.00 | 0.00 | 15% | 100,000.00 |
| 200,000.01 -- 350,000.00 | 15,000.00 | 20% | 200,000.00 |
| 350,000.01 -- 500,000.00 | 45,000.00 | 25% | 350,000.00 |
| 500,000.01 and above | 82,500.00 | 30% | 500,000.00 |

- **Base-tax column reconciliation** — At C$200,000.00 → 15% × (200,000.00 − 100,000.00) = C$15,000.00. At C$350,000.00 → 15,000.00 + 20% × (350,000.00 − 200,000.00) = 15,000.00 + 30,000.00 = C$45,000.00. At C$500,000.00 → 45,000.00 + 25% × (500,000.00 − 350,000.00) = 45,000.00 + 37,500.00 = C$82,500.00. Each base-tax figure equals the cumulative tax at the top of the band below it. The column is internally consistent.  _(LCT (Ley 822) Art. 23, as reformed by Ley 891)_
- **Exempt threshold** — C$100,000.00 per year (≈ C$8,333.33 per month) is exempt. IR withholding applies only to taxable income above this amount.  _(LCT (Ley 822) Art. 23, as reformed by Ley 891)_
- **Tax formula for taxable income T (C$)** — IR_annual = base_tax(band) + rate(band) × (T − lower_bound(band))  _(LCT (Ley 822) Art. 23, as reformed by Ley 891)_

### Non-Residents

- **Non-resident taxation** — Non-residents are taxed by 20% definitive withholding (retención definitiva) on Nicaraguan-source income — a flat rate, NOT the progressive scale. This is final; no annual return reconciliation applies for the withheld amount. **[RESEARCH GAP: confirm any treaty overrides for specific counterparties before applying.]**

### INSS and INATEC Rates (2025)

**INSS and INATEC Rates (2025)**

| Contribution | Payer | Rate | Base |
| --- | --- | --- | --- |
| INSS laboral (régimen Integral) | Employee | 7.00% | Whole gross salary, **no upper cap** |
| INSS patronal — employers with ≤50 employees | Employer | 21.50% | Whole gross salary, no cap |
| INSS patronal — employers with >50 employees | Employer | 22.50% | Whole gross salary, no cap |
| INATEC (training levy) | Employer | 2.00% | Gross salary (on top of INSS) |

- **Salary ceiling eliminated** — The maximum insurable-earnings ceiling was removed by INSS Resolution RI-112-2018. Contributions are calculated on the entire gross salary with NO upper cap. The employee rate rose from 6.25% to 7.00% effective 15 Feb 2019. Do NOT use the stale ceiling of C$130,362.60/month or the pre-2019 6.25% rate — they are outdated.  _(INSS Resolution RI-112-2018)_

### Order of Computation (critical)

- **Order of computation** — IR on employment income is computed on income net of the employee's 7% INSS laboral. INSS laboral is a deduction from gross before the progressive scale is applied.
- **Order of computation formula** — Annual taxable income = Annual gross salary − Annual INSS laboral (7% of gross) Annual IR = scale applied to annual taxable income

**[RESEARCH GAP: confirm the exact ordering and any further allowable deductions against LCT Art. 19–23 / DGI guidance before signing off a return.]**

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Residence status unknown | STOP — do not pick progressive vs 20% definitive WHT without residence |
| Currency not stated | Assume córdoba (C$ / NIO); do not assume USD |
| Income source (employment vs business) | Treat as rentas del trabajo only; refuse other income classes |
| Whether INSS already deducted | Assume gross (INSS not yet deducted); deduct 7% before the scale |
| Multiple employers in the year | Flag IR-106 annual-return obligation (see Section 5) |
| Monthly vs annual figures | Confirm; annualize (×12) before applying the annual scale |
| Any deduction beyond INSS laboral | Not allowed without explicit DGI basis |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Minimum viable — annual (or monthly, clearly labelled) gross salary in córdobas, confirmation of residence status (resident vs non-resident), and confirmation that the income is employment income (rentas del trabajo).
- **Recommended inputs** — Recommended — payslips or a payroll summary (colilla de pago) for the full year, the employer's INSS laboral deduction records, number of employers during the year, and any prior-year IR-106 or DGI assessment.
- **Ideal inputs** — Ideal — full payroll ledger (nómina), INSS contribution receipts, employer remittance records (IR-122 filings), and confirmation of whether the employee has more than one employer.
- **Refusal if minimum missing** — Refusal if minimum is missing — SOFT WARN. No salary figure at all = hard stop. Salary without payslips = proceed with reviewer warning: "This IR computation was produced from a stated salary figure alone. The reviewer must verify gross salary, the 7% INSS laboral deduction, residence status, and whether an annual IR-106 return is required (more than one employer)."

### Refusal Catalogue

- **R-NI-1** — Residence status unknown. "Residence determines whether the progressive rentas-del-trabajo scale or the 20% definitive non-resident withholding applies. This skill cannot compute IR without confirmed residence status. Please confirm before proceeding."
- **R-NI-2** — Business / professional income (rentas de actividades económicas). "This skill covers employment income (rentas del trabajo) only. IR on business and professional activity (rentas de actividades económicas) uses a different regime and rates. Escalate to a Nicaraguan licensed accountant (CCPN)."
- **R-NI-3** — Capital income (rentas de capital y ganancias de capital). "Income from capital and capital gains is taxed under a separate IR cédula (typically definitive withholding). Out of scope. Escalate to a Nicaraguan licensed accountant."
- **R-NI-4** — Non-resident beyond simple WHT. "Non-resident situations involving treaty relief, permanent establishments, or mixed-source income require specialised analysis. This skill applies only the flat 20% definitive WHT to clearly Nicaraguan-source employment income of a non-resident. Escalate otherwise."
- **R-NI-5** — Arrears / DGI enforcement. "Client has outstanding IR arrears or is subject to DGI enforcement. Surcharges and interest (recargos) apply. Do not advise. Escalate to a Nicaraguan licensed accountant immediately."
- **R-NI-6** — IVA / VAT requested. "This skill covers income tax (IR rentas del trabajo) only. For Nicaragua IVA, use the nicaragua-iva skill."
- **R-NI-7** — Payroll / INSS-employer computation requested. "For full payroll processing, INSS patronal, and INATEC employer contributions, use the nicaragua-payroll skill. This skill computes the employee's IR and 7% INSS laboral only."

## Section 3 -- Transaction / Payslip Pattern Library

This is the deterministic pre-classifier for payroll and payslip (colilla de pago) lines. When a line matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the line label as it appears on the payslip or payroll ledger. If multiple patterns match, use the most specific. All amounts are córdobas (C$).

### 3.1 Income / Earnings Lines (add to gross)

**3.1 Income / Earnings Lines (add to gross)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, SALARIO BASE, SUELDO BÁSICO | Gross employment income | Add to annual gross |
| HORAS EXTRA, OVERTIME | Gross employment income | Taxable employment income |
| COMISIÓN, COMISIONES, BONO, BONIFICACIÓN | Gross employment income | Taxable; part of rentas del trabajo |
| INCENTIVO, GRATIFICACIÓN | Gross employment income | Taxable unless a specific exemption is documented |
| AGUINALDO, DÉCIMO TERCER MES (13th-month) | Gross employment income — EXEMPT subject to limit | 13th-month pay (aguinaldo) is exempt up to the legal amount. **[RESEARCH GAP: confirm exemption ceiling against LCT before excluding.]** |
| VIÁTICOS (genuine business reimbursement) | EXCLUDE | Reimbursed business expense, not income, if genuine and documented |
| INDEMNIZACIÓN (statutory severance) | EXEMPT subject to limit | Statutory severance exempt up to legal limit. **[RESEARCH GAP: confirm ceiling.]** |

### 3.2 Deduction Lines (subtract before the IR scale)

**3.2 Deduction Lines (subtract before the IR scale)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, INSS LABORAL, SEGURO SOCIAL (7%) | DEDUCT before IR scale | 7% of gross; reduces taxable income. Deduct from gross to get IR base |

### 3.3 Withholding / Tax Lines (NOT a deduction from the IR base)

**3.3 Withholding / Tax Lines (NOT a deduction from the IR base)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RETENCIÓN IR, IR RETENIDO, IMPUESTO SOBRE LA RENTA | IR withheld | This is the tax itself — a credit against the annual IR liability, not a deductible expense |

### 3.4 Lines That Are NEITHER Income Nor a Pre-IR Deduction

**3.4 Lines That Are NEITHER Income Nor a Pre-IR Deduction**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INATEC | EXCLUDE (employer cost) | Employer-paid 2% levy; not an employee deduction, not employee income |
| INSS PATRONAL | EXCLUDE (employer cost) | Employer 21.5%/22.5%; out of scope for employee IR |
| ANTICIPO, PRÉSTAMO, ADELANTO (salary advance) | EXCLUDE | Advance / loan against salary — not income, not a deduction |
| EMBARGO, RETENCIÓN JUDICIAL | EXCLUDE from IR base | Court-ordered garnishment; does not reduce taxable income |

### 3.5 Non-Resident Line

**3.5 Non-Resident Line**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Non-resident Nicaraguan-source employment payment | 20% definitive WHT | Flat 20% on the gross Nicaraguan-source amount; do NOT apply the progressive scale |

## Section 4 -- Worked Examples

All amounts in córdobas (C$). Every total reconciles to the cent.

### Example 1 -- Monthly salary below the exempt threshold

**Input:** Resident employee, gross salary C$8,000.00 / month (C$96,000.00 / year).

**Reasoning:**
- Annual gross = 8,000.00 × 12 = C$96,000.00.
- INSS laboral = 7% × 96,000.00 = C$6,720.00.
- Annual taxable income = 96,000.00 − 6,720.00 = C$89,280.00.
- C$89,280.00 ≤ C$100,000.00 → falls in the 0% exempt band.

**Classification:** Annual IR = C$0.00. No monthly IR withholding. INSS laboral of C$560.00/month (6,720.00 / 12) is still deducted and remitted.

### Example 2 -- Salary in the 15% band

**Input:** Resident employee, gross salary C$20,000.00 / month (C$240,000.00 / year).

**Reasoning:**
- Annual gross = 20,000.00 × 12 = C$240,000.00.
- INSS laboral = 7% × 240,000.00 = C$16,800.00.
- Annual taxable income = 240,000.00 − 16,800.00 = C$223,200.00.
- C$223,200.00 falls in the 200,000.01 – 350,000.00 band (base C$15,000.00, 20% on excess over 200,000.00).
- IR = 15,000.00 + 20% × (223,200.00 − 200,000.00) = 15,000.00 + 20% × 23,200.00 = 15,000.00 + 4,640.00 = C$19,640.00.

**Classification:** Annual IR = C$19,640.00. Monthly withholding ≈ 19,640.00 / 12 = C$1,636.67/month (employer reconciles to the annual figure via IR-122).

### Example 3 -- Salary in the 25% band

**Input:** Resident employee, gross salary C$40,000.00 / month (C$480,000.00 / year).

**Reasoning:**
- Annual gross = 40,000.00 × 12 = C$480,000.00.
- INSS laboral = 7% × 480,000.00 = C$33,600.00.
- Annual taxable income = 480,000.00 − 33,600.00 = C$446,400.00.
- C$446,400.00 falls in the 350,000.01 – 500,000.00 band (base C$45,000.00, 25% on excess over 350,000.00).
- IR = 45,000.00 + 25% × (446,400.00 − 350,000.00) = 45,000.00 + 25% × 96,400.00 = 45,000.00 + 24,100.00 = C$69,100.00.

**Classification:** Annual IR = C$69,100.00. Monthly withholding ≈ C$5,758.33/month.

### Example 4 -- Salary in the top 30% band

**Input:** Resident employee, gross salary C$70,000.00 / month (C$840,000.00 / year).

**Reasoning:**
- Annual gross = 70,000.00 × 12 = C$840,000.00.
- INSS laboral = 7% × 840,000.00 = C$58,800.00.
- Annual taxable income = 840,000.00 − 58,800.00 = C$781,200.00.
- C$781,200.00 falls in the 500,000.01 and above band (base C$82,500.00, 30% on excess over 500,000.00).
- IR = 82,500.00 + 30% × (781,200.00 − 500,000.00) = 82,500.00 + 30% × 281,200.00 = 82,500.00 + 84,360.00 = C$166,860.00.

**Classification:** Annual IR = C$166,860.00. Monthly withholding ≈ C$13,905.00/month.

### Example 5 -- Non-resident definitive withholding

**Input:** Non-resident, Nicaraguan-source employment payment C$50,000.00.

**Reasoning:**
- Non-residents are subject to 20% definitive WHT on Nicaraguan-source income — flat, not the progressive scale.
- WHT = 20% × 50,000.00 = C$10,000.00.
- This is definitive; no annual reconciliation on this amount.

**Classification:** Definitive WHT = C$10,000.00. Net paid = C$40,000.00. **[RESEARCH GAP: check treaty before applying.]**

### Example 6 -- Bracket boundary at exactly C$100,000 taxable

**Input:** Resident employee, annual taxable income (after INSS) = C$100,000.00 exactly.

**Reasoning:**
- C$100,000.00 is the top of the 0% exempt band (0.01 – 100,000.00).
- IR = C$0.00. The 15% rate applies only to income strictly above C$100,000.00.

**Classification:** Annual IR = C$0.00.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Scope — Rentas del Trabajo Only

- **Scope** — This skill computes IR on employment income (rentas del trabajo) for resident employees, plus the flat 20% definitive WHT for non-residents. Business income (rentas de actividades económicas) and capital income (rentas de capital) are out of scope (R-NI-2, R-NI-3).  _(LCT (Ley 822) Art. 19)_

### 5.2 INSS Laboral Is Deducted Before the Scale

- **INSS laboral deducted before scale** — The employee's 7% INSS laboral is deducted from gross salary to arrive at taxable employment income. Apply the progressive scale to the net-of-INSS figure. INSS laboral is on the whole gross salary with no upper cap (RI-112-2018). **[RESEARCH GAP: confirm exact ordering / further deductions against DGI guidance.]**  _(LCT Art. 19–23)_

### 5.3 The Progressive Scale (annual)

- **Progressive scale application** — IR_annual = base_tax(band) + rate(band) × (taxable_income − lower_bound(band)) The first C$100,000.00 is exempt. The scale is annual; for monthly payroll, annualize (×12) before applying it, or use the C$8,333.33/month exempt equivalent.

### 5.4 Monthly Withholding (IR-122)

- **Monthly withholding via IR-122** — The employer withholds the employee's IR monthly through payroll and remits it on Form IR-122 (monthly withholding income-tax return). Monthly withholding approximates annual IR ÷ 12, reconciled across the year as salary varies.

### 5.5 Annual Return (IR-106) — When Required

**5.5 Annual Return (IR-106) — When Required**

| Situation | Annual IR-106 return |
| --- | --- |
| Single employer, standard withholding, no extra deductions | **Not required** — withholding is final |
| Income from **more than one employer** totaling **over C$100,000/year** | **Required** — file IR-106 |

- **IR-106 form details** — Form IR-106 is the annual individual income-tax return. It is due within 90 days after year-end (≈ 31 March). Any final payment is due with the return.

### 5.6 Non-Resident Definitive Withholding

- **Non-resident definitive withholding** — Non-residents pay 20% definitive WHT on Nicaraguan-source income — flat, final, no progressive scale, no annual reconciliation on the withheld amount.

### 5.7 Tax Year

- **Tax year** — Calendar year (1 January – 31 December). Alternative 12-month periods are allowed only with DGI authorization.

### 5.8 Items Not Deductible Against the IR Base

**5.8 Items Not Deductible Against the IR Base**

| Item | Reason |
| --- | --- |
| INATEC (2%) | Employer-paid levy; not an employee deduction |
| INSS patronal (21.5%/22.5%) | Employer cost; out of scope for employee IR |
| The IR withholding itself | It is the tax — a credit, not a deduction from the base |
| Salary advances / loans (anticipos) | Movement of cash, not income or expense |
| Court garnishments (embargos) | Do not reduce taxable income |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Aguinaldo (13th-Month Pay) Exemption

- **Aguinaldo exemption** — The aguinaldo (décimo tercer mes) is generally exempt up to the legal amount. Flag for reviewer: confirm the exempt ceiling and whether any excess is taxable. **[RESEARCH GAP: confirm ceiling against LCT.]**

### 6.2 Statutory Severance (Indemnización)

- **Statutory severance exemption** — Statutory severance is generally exempt up to a legal limit; amounts above may be taxable. Flag for reviewer: confirm the exempt limit and the nature of the payment.

### 6.3 Viáticos and Reimbursements

- **Viáticos treatment** — Genuine, documented business reimbursements (viáticos) are excluded from income. Flag for reviewer: confirm the reimbursement is genuine and documented, not disguised remuneration.

### 6.4 Multiple Employers — IR-106 Obligation

- **Multiple employers IR-106 obligation** — If the employee had more than one employer and total income exceeds C$100,000/year, an IR-106 annual return is required to aggregate income and reconcile withholding. Flag for reviewer: confirm number of employers and total income; prepare IR-106 if triggered.

### 6.5 Residence Determination

- **Residence determination** — Residence drives progressive scale vs 20% definitive WHT. Flag for reviewer: confirm residence status and any treaty position before finalizing. **[RESEARCH GAP: treaty overrides.]**

### 6.6 Mid-Year Joiners / Leavers and Variable Pay

- **Mid-year joiners/leavers and variable pay** — Part-year employment and variable monthly pay require annualization and reconciliation to the annual scale. Flag for reviewer: confirm the annualization method and year-end reconciliation.

## Section 7 -- Working Paper Template

```
NICARAGUA INCOME TAX -- IR RENTAS DEL TRABAJO WORKING PAPER
Tax Year: 2025                Currency: Córdoba (C$ / NIO)
Client: ___________________________
Residence: Resident / Non-resident
Number of employers in year: ______

A. GROSS EMPLOYMENT INCOME (annual)
  A1. Salario / sueldo base                     ___________
  A2. Horas extra / overtime                    ___________
  A3. Comisiones / bonos / incentivos           ___________
  A4. Aguinaldo (taxable excess only)  [T2]     ___________
  A5. Other taxable employment income           ___________
  A6. TOTAL gross employment income             ___________

B. PRE-IR DEDUCTION
  B1. INSS laboral (7% of A6, no cap)           ___________

C. ANNUAL TAXABLE INCOME (A6 - B1)              ___________

D. IR COMPUTATION (progressive scale, residents)
   Band of C: __________________________
  D1. Base tax for band                         ___________
  D2. Excess over lower bound                    ___________
  D3. Rate on excess (%)                         ___________
  D4. Tax on excess (D2 x D3)                    ___________
  D5. ANNUAL IR (D1 + D4)                        ___________

E. NON-RESIDENT (alternative to D)
  E1. Gross Nicaraguan-source amount             ___________
  E2. 20% definitive WHT (E1 x 20%)              ___________

F. RECONCILIATION
  F1. Annual IR (D5 or E2)                       ___________
  F2. IR already withheld (IR-122, sum)          ___________
  F3. IR due / (refund) with IR-106 (F1 - F2)    ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Currency confirmed as córdoba (C$/NIO)?
  [ ] INSS laboral (7%) deducted before the scale?
  [ ] Aguinaldo / severance exemption confirmed? [T2]
  [ ] Viáticos genuinely reimbursements? [T2]
  [ ] More than one employer → IR-106 required?
  [ ] Annual figures (not monthly) used in the scale?
  [ ] IR withholding treated as a credit, not a deduction?
```

## Section 8 -- Payslip / Payroll Reading Guide

### Key Nicaraguan Payroll Terms (Spanish → English)

**Key Nicaraguan Payroll Terms (Spanish → English)**

| Term | English | Classification Hint |
| --- | --- | --- |
| Salario / Sueldo | Salary | Gross employment income |
| Salario base / Sueldo básico | Base salary | Gross employment income |
| Horas extra | Overtime | Gross employment income |
| Comisión / Bono / Incentivo | Commission / bonus / incentive | Gross employment income |
| Aguinaldo / Décimo tercer mes | 13th-month pay | Exempt up to limit [T2] |
| Indemnización | Severance | Exempt up to limit [T2] |
| Viáticos | Travel/expense reimbursement | Exclude if genuine |
| INSS laboral | Employee social security (7%) | Deduct before IR scale |
| INSS patronal | Employer social security (21.5/22.5%) | Employer cost — exclude |
| INATEC | Training levy (2%, employer) | Employer cost — exclude |
| Retención IR / IR retenido | Income-tax withheld | Credit against annual IR |
| Anticipo / Préstamo / Adelanto | Salary advance / loan | Exclude |
| Embargo / Retención judicial | Garnishment | Exclude from IR base |
| Colilla de pago | Payslip | Source document |
| Nómina | Payroll ledger | Source document |

### Forms Reference

**Forms Reference**

| Form | Purpose | Frequency / Deadline |
| --- | --- | --- |
| IR-122 | Monthly withholding income-tax return (employer withholds and remits) | Monthly |
| IR-106 | Annual individual income-tax return | Within 90 days of year-end (~31 March) |

## Section 9 -- Onboarding Fallback

If the client provides a salary figure but cannot answer onboarding questions immediately:

1. Classify all payslip/payroll lines using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — assume gross, deduct 7% INSS, assume córdoba.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- NICARAGUA INCOME TAX (IR)
1. Residence status: resident or non-resident of Nicaragua?
2. Is the income employment income (rentas del trabajo), or business/capital income?
3. Is the salary figure monthly or annual, and in córdobas (C$)?
4. Has the 7% INSS laboral already been deducted, or is this gross?
5. How many employers did you have during the year?
6. If more than one employer, what is the combined annual income?
7. Any aguinaldo (13th-month), severance, or viáticos included in the figure?
8. How much IR has already been withheld during the year (IR-122)?
```

## Section 10 -- Reference Material

### Key Legislation References

**Key Legislation References**

| Topic | Reference |
| --- | --- |
| Income tax — general framework | Ley No. 822, Ley de Concertación Tributaria (LCT) |
| Reform | Ley No. 891 |
| Rentas del trabajo / deductions | LCT Art. 19–22 |
| Progressive scale | LCT Art. 23 |
| Tax administration / filing | DGI guidance; forms IR-122, IR-106 |
| INSS laboral rate (7%) | INSS reform 2019; Resolution RI-112-2018 (ceiling eliminated) |

### Sources (cross-verified June 2026)

**Sources (cross-verified June 2026)**

| Source | Coverage | URL |
| --- | --- | --- |
| PwC — Taxes on personal income | Progressive scale, non-resident WHT | https://taxsummaries.pwc.com/nicaragua/individual/taxes-on-personal-income |
| PwC — Other taxes | INSS rates | https://taxsummaries.pwc.com/nicaragua/individual/other-taxes |
| PwC — Tax administration | IR-122, IR-106, deadlines | https://taxsummaries.pwc.com/nicaragua/individual/tax-administration |
| Lorente Consultores | Ley 822 reforms, employee tax burden | https://www.lorenteconsultores.com/post/el-trabajador-y-su-carga-impositiva-lo-que-establece-la-ley-822-y-sus-reformas |
| DGI — "Aprendamos a Tributar" | Official DGI guidance | https://www.dgi.gob.ni/pdfArchivo/22 |
| Mercer | 2019 INSS reform detail | https://www.mercer.com/en-us/insights/law-and-policy/nicaragua-revises-social-security-arrangements/ |
| GCH (Servicio Contable Nicaragua) | Current INSS/INATEC rates, no ceiling | https://www.serviciocontablenicaragua.com/la-gestion-de-nomina-en-nicaragua/ |
| INSS official | Social security authority | https://www.inss.gob.ni/ |

Big Four coverage for Nicaragua individuals is essentially PwC-only on taxsummaries; EY and Deloitte do not maintain a standalone Nicaragua individual page. PwC is corroborated by Nicaraguan professional sources (CCPN — Colegio de Contadores Públicos de Nicaragua, and the firms cited above).

### Test Suite

All amounts in córdobas (C$). Each result reconciles to the cent.

**Test 1 — Below exempt threshold.**
Input: Resident, gross C$8,000/month = C$96,000/year.
INSS = 6,720.00. Taxable = 89,280.00 (≤ 100,000.00).
Expected: Annual IR = **C$0.00**.

**Test 2 — 15% band.**
Input: Resident, gross C$20,000/month = C$240,000/year.
INSS = 16,800.00. Taxable = 223,200.00.
Expected: IR = 15,000.00 + 20% × 23,200.00 = **C$19,640.00**.
(Note: taxable C$223,200 sits in the 20% band; the "15% band" label in the input refers to the headline rate the employee first crosses — the computation is correct at 20% on the excess over C$200,000.)

**Test 3 — 25% band.**
Input: Resident, gross C$40,000/month = C$480,000/year.
INSS = 33,600.00. Taxable = 446,400.00.
Expected: IR = 45,000.00 + 25% × 96,400.00 = **C$69,100.00**.

**Test 4 — 30% top band.**
Input: Resident, gross C$70,000/month = C$840,000/year.
INSS = 58,800.00. Taxable = 781,200.00.
Expected: IR = 82,500.00 + 30% × 281,200.00 = **C$166,860.00**.

**Test 5 — Non-resident definitive WHT.**
Input: Non-resident, Nicaraguan-source payment C$50,000.
Expected: 20% × 50,000.00 = **C$10,000.00** definitive WHT (no progressive scale).

**Test 6 — Exact boundary at C$100,000 taxable.**
Input: Resident, taxable income exactly C$100,000.00.
Expected: IR = **C$0.00** (15% applies only above C$100,000.00).

**Test 7 — Pure 15%-band check (taxable C$150,000).**
Input: Resident, taxable income C$150,000.00 (after INSS).
Expected: IR = 0.00 + 15% × (150,000.00 − 100,000.00) = **C$7,500.00**.

## PROHIBITIONS

- NEVER treat "NI" as Northern Ireland or UK National Insurance — this is Nicaragua. No HMRC, no £, no UK content.
- NEVER apply the progressive scale to a non-resident — non-residents get flat 20% definitive WHT.
- NEVER apply the scale without first deducting the 7% INSS laboral from gross.
- NEVER apply an INSS ceiling — RI-112-2018 eliminated the cap; INSS is on the whole gross salary.
- NEVER use the pre-2019 6.25% employee INSS rate or the stale C$130,362.60 ceiling.
- NEVER apply the annual scale to a monthly figure without annualizing (×12) first.
- NEVER treat the IR withholding itself as a deduction from the IR base — it is a credit.
- NEVER include employer INSS patronal (21.5%/22.5%) or INATEC (2%) in the employee's IR computation.
- NEVER assume USD — figures are córdobas (C$ / NIO) unless explicitly stated otherwise.
- NEVER present tax calculations as definitive — always label as estimated and pending professional review.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Autorizado in Nicaragua, or an equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
