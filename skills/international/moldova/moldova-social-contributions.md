---
name: moldova-social-contributions
description: Use this skill whenever asked about Moldova payroll social contributions, health insurance, or personal income tax for employees, employers, or self-employed individuals. Trigger on phrases like "Moldova payroll", "CNAS contribution", "CNAM health insurance", "how much social insurance in Moldova", "Moldova employer cost", "24% social contribution", "9% health insurance Moldova", "Moldova PIT 12%", "IPC21 declaration", "fixed social contribution self-employed Moldova", "Moldova minimum wage", "MDL salary calculation", "Moldova IT Park 7%", or any question about Moldovan State Social Insurance (CNAS), Mandatory Health Insurance (CNAM), or income tax withholding. Also trigger when classifying bank statement transactions that relate to CNAS, CNAM, SFS (Serviciul Fiscal de Stat), or payroll tax payments from Moldovan banks (Maib, MICB/Moldindconbank, OTP, Victoriabank). Also trigger when preparing a monthly IPC21 declaration or an annual CET18 individual return where contribution and PIT computations are relevant. This skill covers the 12% flat PIT, employer 24%/32% CNAS rates, employee 9% CNAM, fixed annual contributions for the self-employed, minimum wage and average-salary thresholds, payroll forms, penalties, the IT Park single-tax regime, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Moldovan payroll or contribution work.
version: 0.1
jurisdiction: MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova Social Contributions, Health Insurance & Personal Income Tax

## Section 1 -- Quick reference

**Section 1 quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Moldova |
| Primary Legislation | Tax Code of the Republic of Moldova (Codul fiscal); Law No. 489/1999 on the state social insurance system; Law No. 303/2024 on the state social insurance budget for 2025; Law No. 1593/2002 on mandatory health insurance contributions |
| Tax / Contribution Authorities | State Tax Service (Serviciul Fiscal de Stat / SFS, sfs.md) collects payroll PIT, social and health contributions via the monthly IPC21 declaration; CNAS (Casa Nationala de Asigurari Sociale, cnas.gov.md) administers social insurance/pensions; CNAM (Compania Nationala de Asigurari in Medicina, cnam.md) administers mandatory health insurance |
| Personal income tax (PIT) | Flat 12% (PwC, *Taxes on personal income*) |
| Employer social insurance (CNAS) | 24% of gross remuneration; 32% for special/hazardous working conditions (PwC, *Corporate -- Other taxes* / *Individual -- Other taxes*) |
| Employee social insurance (CNAS) | 0% -- employees pay NO state social insurance (PwC, *Individual -- Other taxes*) |
| Employee health insurance (CNAM) | 9% of wages, withheld by employer (PwC, *Individual -- Other taxes*) |
| Employer health insurance (CNAM) | 0% -- abolished in the October 2018 reform (PwC, *Corporate -- Other taxes*) |
| Standard PIT personal allowance (2025) | 29,700 MDL/year (~2,475 MDL/month), only if annual taxable income <= 360,000 MDL (Intelcont; PwC carries the same figure for 2026) |
| Minimum wage (2025) | 5,500 MDL/month gross, full-time (Govt Decision No. 846 of Dec 2024; WageIndicator) |
| Minimum wage (2026, confirmed) | 6,300 MDL/month (Govt decision of 17 Dec 2025; MOLDPRES) |
| Forecast average monthly salary | 16,100 MDL for 2025; 17,400 MDL for 2026 (Min. of Labour / social.gov.md) |
| Payroll return | Form IPC21, monthly, by the 25th of the following month (Rivermate; SFS) |
| Annual individual return | Form CET18, by 30 April of the following year (PwC, *Individual -- Tax administration*) |
| Currency | MDL (Moldovan leu) only |
| Validated by | Pending -- requires sign-off by a licensed Moldovan accountant |
| Validation date | Pending |

**Payroll component overview (standard private-sector employee)**

| Component | Payer | Rate / amount | Authority |
| --- | --- | --- | --- |
| State social insurance (CNAS) | Employer | 24% of gross (32% special conditions) | PwC, *Corporate -- Other taxes* |
| State social insurance (CNAS) | Employee | 0% | PwC, *Individual -- Other taxes* |
| Mandatory health insurance (CNAM) | Employee (employer withholds) | 9% of wages | PwC, *Individual -- Other taxes* |
| Mandatory health insurance (CNAM) | Employer | 0% | PwC, *Corporate -- Other taxes* |
| Personal income tax (PIT/PAYE) | Employee (employer withholds) | 12% flat on base after allowance and CNAM | PwC, *Individual -- Taxes on personal income* |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown working conditions | Assume standard 24% employer CNAS (NOT 32%) and flag for reviewer |
| Source cites a 6% "employee social insurance" figure | Treat as 0% (pre-2018 legacy figure); do NOT apply 6% (PwC; see caveats) |
| Source cites a 4.5%/4.5% employer/employee health split | Treat as 9% fully employee-borne, 0% employer (post-2018 reform) |
| Unknown tax year | Use 2025 figures (5,500 MDL min wage, 20,518 MDL fixed SSC); apply 2026 figures only from 1 Jan 2026 |
| Unknown whether personal allowance applies | Apply standard 29,700 MDL/year ONLY if annual income <= 360,000 MDL; otherwise nil allowance |
| Self-employed vs employed status unclear | STOP -- the contribution base (24% on gross vs fixed annual amount) differs entirely; ask before computing |
| Employer in Moldova IT Park (MITP) | STOP -- standard SSC/PIT do NOT apply; the 7% single tax replaces them; escalate |

## Section 2 -- Required inputs and refusal catalogue

- **Required inputs -- Minimum viable** — Employment status (employed vs self-employed/individually insured), gross monthly remuneration in MDL, and the tax year. Without employment status, STOP: an employee is taxed on 24% employer / 9% employee / 12% PIT, whereas a self-employed person pays a fixed annual contribution.
- **Required inputs -- Recommended** — Working conditions (standard vs special/hazardous, which sets 24% vs 32% employer CNAS), full-time vs part-time (which sets the minimum contribution base), entitlement to personal/major/dependent allowances, and annual taxable income (to test the 360,000 MDL allowance cap).
- **Required inputs -- Ideal** — Monthly IPC21 declarations, CNAS and CNAM statements, the employment contract, and prior-year CET18 return.
- **R-MD-SC-1 -- Employment status unknown** — Trigger: not stated whether the individual is an employee or self-employed/individually insured. Message: "Employment status is mandatory. Employees are subject to 24% employer CNAS, 9% employee CNAM and 12% PIT on remuneration; self-employed/individually insured persons instead pay a fixed annual contribution (20,518 MDL in 2025). Cannot proceed without this information."
- **R-MD-SC-2 -- Moldova IT Park (MITP) resident** — Trigger: employer is a registered Moldova IT Park resident. Message: "MITP residents pay a single 7% tax on monthly turnover (not less than 30% of the forecast average monthly salary per employee) that REPLACES CIT, salary PIT, employer SSC, employee health insurance and several other taxes (Invest Moldova). Standard payroll computations do not apply. Escalate to a licensed Moldovan accountant."  _(Invest Moldova)_
- **R-MD-SC-3 -- Special/hazardous working conditions** — Trigger: client claims the 32% employer CNAS rate or an industry-specific split (e.g. agriculture). Message: "The 32% special-conditions rate and any sector-specific splits must be confirmed against the current state social insurance budget law for the relevant year. Do not apply without reviewer confirmation."
- **R-MD-SC-4 -- Contribution arrears or penalties** — Trigger: unpaid CNAS/CNAM/PIT from prior periods. Message: "Late social insurance is penalised at 0.1% per day (Law 489/1999, art. 28) and late PIT interest at 0.0301% per day; both compound. Quantify only from an official SFS/CNAS statement and escalate to a licensed Moldovan accountant."  _(Law 489/1999, art. 28)_
- **R-MD-SC-5 -- Increased/major allowance entitlement** — Trigger: client claims the major allowance (34,620 MDL), spouse's major allowance (21,780 MDL), or severe-disability dependent allowance. Message: "Qualifying conditions for the increased personal/spouse/dependent allowances are not fully enumerated in this skill [RESEARCH GAP -- reviewer to confirm]. Confirm eligibility before applying."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Moldovan payroll, social and health contributions, and income tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement (Romanian and English variants are both shown). Contribution and PIT payments are statutory obligations -- they EXCLUDE from any VAT return; employer-side contributions are a payroll cost, employee-side withholdings are remitted on the employee's behalf.

### 3.1 State social insurance (CNAS) payments

**3.1 State social insurance (CNAS) payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNAS, CASA NATIONALA DE ASIGURARI SOCIALE | EXCLUDE -- social insurance (CNAS) | Employer 24% (or 32%) contribution |
| ASIGURARI SOCIALE, CONTRIBUTII SOCIALE | EXCLUDE -- social insurance | Romanian-language reference |
| BASS, BUGETUL ASIGURARILOR SOCIALE DE STAT | EXCLUDE -- social insurance budget | State social insurance budget |
| CONTRIBUTIE SOCIALA FIXA | EXCLUDE -- fixed annual SSC | Self-employed / individually insured |

### 3.2 Mandatory health insurance (CNAM) payments

**3.2 Mandatory health insurance (CNAM) payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CNAM, COMPANIA NATIONALA DE ASIGURARI IN MEDICINA | EXCLUDE -- health insurance (CNAM) | Employee-borne 9%, withheld by employer |
| ASIGURARE MEDICALA, ASIGURARI MEDICALE | EXCLUDE -- health insurance | Romanian-language reference |
| PRIMA ASIGURARE MEDICALA, FAOAM | EXCLUDE -- fixed health premium | Fixed annual CNAM premium (self-employed) |

### 3.3 Income tax (PIT) and combined SFS payments

**3.3 Income tax (PIT) and combined SFS payments**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SFS, SERVICIUL FISCAL DE STAT | EXCLUDE -- tax/contribution remittance | SFS collects PIT + CNAS + CNAM via IPC21 |
| IMPOZIT PE VENIT, IPC21 | EXCLUDE -- PIT / payroll return remittance | 12% PIT withholding |
| IPC | EXCLUDE -- combined monthly payroll remittance | IPC21 declaration payment |

### 3.4 Salary and payroll (exclude from contribution classification)

**3.4 Salary and payroll (exclude from contribution classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIU, SALARIZARE (outgoing) | EXCLUDE -- payroll expense | Net wage to employee, not a contribution |
| SALARIU, AVANS (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Pension and benefit payments (received -- not contributions)

**3.5 Pension and benefit payments (received -- not contributions)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSIE, CNAS PENSIE | EXCLUDE -- pension income received | Benefit received, not a contribution |
| INDEMNIZATIE, AJUTOR SOCIAL | EXCLUDE -- social benefit received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank statement / payroll classifications for a hypothetical Moldovan employer and its employees. All figures in MDL, 2025 tax year. PIT is computed as 12% of (gross − 9% CNAM − monthly personal allowance), allowance = 29,700/12 = 2,475 MDL/month (Intelcont; PwC, *Individual -- Taxes on personal income* / *Deductions*).

### Example 1 -- Standard employee at minimum wage (5,500 MDL)

**Input line:**
`31.01.2025 ; SALARIU IANUARIE ; DEBIT ; SALARIU NET ; -4,701.40 ; MDL`

**Reasoning:**
Gross = 5,500 MDL (2025 minimum wage; Govt Decision 846/2024). Employee CNAM 9% = 495.00. PIT base = 5,500 − 495 − 2,475 = 2,530.00. PIT 12% = 303.60. Net pay = 5,500 − 495 − 303.60 = **4,701.40**. Employer CNAS 24% = 1,320.00. Employer total cost = 5,500 + 1,320 = **6,820.00**. The net salary debit excludes from VAT; it is a payroll expense.

**Classification:** EXCLUDE from VAT -- net salary (payroll expense). CNAS 1,320.00 and CNAM 495.00 + PIT 303.60 remitted via IPC21.

### Example 2 -- Employee at the forecast average salary (16,100 MDL)

**Input line:**
`25.02.2025 ; SFS IPC21 IAN ; DEBIT ; CONTRIBUTII + IMPOZIT ; -5,313.12 ; MDL`

**Reasoning:**
Gross = 16,100 MDL (forecast average monthly salary 2025; social.gov.md). Employee CNAM 9% = 1,449.00. PIT base = 16,100 − 1,449 − 2,475 = 12,176.00. PIT 12% = 1,461.12. Net pay = 16,100 − 1,449 − 1,461.12 = 13,189.88. Employer CNAS 24% = 3,864.00. The IPC21 remittance line bundles employer CNAS (3,864.00) − no, it bundles the amounts paid TO SFS: CNAM 1,449.00 + PIT 1,461.12 + CNAS 3,864.00 would be the full remittance. The debit shown (5,313.12) = CNAM 1,449.00 + PIT 1,461.12 + (this employer remits CNAS separately). Confirm the exact composition against the IPC21 line. Employer total cost = 16,100 + 3,864 = **19,964.00**.

**Classification:** EXCLUDE from VAT -- statutory remittance via IPC21 (PIT + CNAM = 2,910.12; CNAS 3,864.00 if combined = 6,774.12). Flag composition for reviewer if the bank line does not itemise.

### Example 3 -- Employer CNAS payment (standard 24%)

**Input line:**
`25.03.2025 ; CNAS BASS ; DEBIT ; CONTRIBUTIE FEB ; -2,400.00 ; MDL`

**Reasoning:**
Matches "CNAS" (pattern 3.1). For a 10,000 MDL gross employee, employer CNAS 24% = 10,000 × 0.24 = **2,400.00**. This is an employer payroll cost, not withheld from the employee. Excludes from VAT.

**Classification:** EXCLUDE from VAT -- employer social insurance (CNAS) cost.

### Example 4 -- Special working conditions employer CNAS (32%)

**Input line:**
`25.04.2025 ; CASA NATIONALA DE ASIGURARI SOCIALE ; DEBIT ; CONTRIBUTIE 32% ; -6,400.00 ; MDL`

**Reasoning:**
Matches "CASA NATIONALA DE ASIGURARI SOCIALE" (pattern 3.1) with a 32% reference. For a 20,000 MDL gross employee in special/hazardous conditions, employer CNAS 32% = 20,000 × 0.32 = **6,400.00** (PwC, *Individual -- Other taxes*). For the same employee: CNAM 9% = 1,800.00; PIT base = 20,000 − 1,800 − 2,475 = 15,725.00; PIT 12% = 1,887.00; net pay = 20,000 − 1,800 − 1,887 = 16,313.00. The 32% rate must be reviewer-confirmed (R-MD-SC-3).

**Classification:** EXCLUDE from VAT -- employer social insurance (special conditions). Flag 32% rate for reviewer.

### Example 5 -- Self-employed fixed annual social contribution

**Input line:**
`15.06.2025 ; CNAS CONTRIBUTIE SOCIALA FIXA ; DEBIT ; ANUL 2025 ; -20,518.00 ; MDL`

**Reasoning:**
Matches "CONTRIBUTIE SOCIALA FIXA" (pattern 3.1). The 2025 fixed annual SSC for self-employed/individually insured persons = **20,518 MDL** (1,709.84 MDL/month × 12 per the CNAS Aug-2025 declaration; rises to 22,878 MDL in 2026). This is not based on the 24% employer rate -- it is a flat statutory amount. Excludes from VAT.

**Classification:** EXCLUDE from VAT -- fixed annual social insurance contribution (self-employed).

### Example 6 -- Fixed annual health insurance premium (non-salaried)

**Input line:**
`30.03.2025 ; CNAM PRIMA ASIGURARE MEDICALA ; DEBIT ; 2025 ; -12,636.00 ; MDL`

**Reasoning:**
Matches "PRIMA ASIGURARE MEDICALA" (pattern 3.2). The fixed annual CNAM premium for non-salaried individuals = **12,636 MDL**, unchanged for 2025 and 2026 (PwC, *Individual -- Deductions*). Early-payment discounts may apply. This is distinct from the employee 9% withholding. Excludes from VAT.

**Classification:** EXCLUDE from VAT -- fixed annual health insurance premium (self-employed / non-salaried).

## Section 5 -- Tier 1 rules

These rules apply when payroll/contribution data is clear and all required inputs are available. Apply exactly as written. All citations are to PwC Worldwide Tax Summaries (reviewed Jan 2026), CNAS, and the named statutes unless otherwise noted.

### Rule 1 -- Personal income tax is a single flat 12%

- **PIT flat rate** — PIT on employment, professional/entrepreneurial and most other income = 12% flat for resident individuals. There are no progressive brackets.  _(PwC, *Individual -- Taxes on personal income*)_

### Rule 2 -- PIT base (PAYE) formula

- **Monthly PIT / net pay formula** — monthly_PIT = 12% x (gross_remuneration - employee_CNAM - monthly_personal_allowance) employee_CNAM = 9% x gross_remuneration monthly_personal_allowance = 29,700 / 12 = 2,475 MDL   (only if annual income <= 360,000 MDL) net_pay = gross_remuneration - employee_CNAM - monthly_PIT CNAM (9%) is deducted before PIT; the personal allowance is then subtracted.  _(PwC, *Individual -- Taxes on personal income* / *Deductions*)_

### Rule 3 -- Employer state social insurance (CNAS) = 24%

- **Employer CNAS rate** — 24% percent of gross salary, meal tickets and other remuneration (minimum monthly base cannot be lower than national minimum monthly salary (5,500 MDL in 2025), or 25% of it for part-time; NO ceiling; 32% applies to special/hazardous working conditions (reviewer-confirm per R-MD-SC-3))  _(PwC, *Corporate -- Other taxes*; PwC, *Individual -- Other taxes*)_

### Rule 4 -- Employees pay NO state social insurance

- **Employee CNAS = 0%** — The employee state social insurance contribution is 0% under the current system. The "6% employee" figure on many EOR/aggregator sites reflects the pre-October-2018 regime and is incorrect for 2025 (see caveats).  _(PwC, *Individual -- Other taxes*)_

### Rule 5 -- Health insurance (CNAM) = 9%, fully employee-borne

- **Employee CNAM rate** — 9% percent of wages (fully borne by employee and withheld by employer; employer pays 0% health insurance; old 4.5%/4.5% split abolished in October 2018 reform)  _(PwC, *Individual -- Other taxes* / *Corporate -- Other taxes*)_

### Rule 6 -- Total payroll wedge

- **Total payroll wedge formula** — employer_total_cost = gross x 1.24            (gross + 24% CNAS; 1.32 for special conditions) employee_deductions = 9% CNAM + 12% PIT (on the post-allowance base)  _(PwC, *Corporate -- Other taxes* / *Individual -- Taxes on personal income*)_

### Rule 7 -- Personal allowances (annual)

**Personal allowances (annual)**  _(PwC, *Individual -- Deductions*)_

| Allowance | Annual amount | Condition | Source |
| --- | --- | --- | --- |
| Standard personal | 29,700 MDL | Only if annual taxable income <= 360,000 MDL | Intelcont; PwC (same for 2026) |
| Major (increased) personal | 34,620 MDL | Qualifying individuals (e.g. disability) [RESEARCH GAP -- reviewer to confirm exact conditions] | PwC, *Individual -- Deductions* |
| Spouse's major allowance | 21,780 MDL | Qualifying spouse | PwC, *Individual -- Deductions* |
| Per dependent | 9,900 MDL (21,780 MDL if dependent has severe disability since childhood) | Per qualifying dependent | PwC, *Individual -- Deductions* |

### Rule 8 -- Fixed annual contributions for self-employed / individually insured

**Fixed annual contributions table**  _(CNAS Aug-2025 declaration; PwC, *Individual -- Deductions*)_

| Contribution | 2025 amount | 2026 amount | Source |
| --- | --- | --- | --- |
| Fixed annual social insurance (CNAS) | 20,518 MDL (1,709.84 MDL/month) | 22,878 MDL | CNAS Aug-2025 declaration |
| Fixed annual health premium (CNAM) | 12,636 MDL | 12,636 MDL (unchanged) | PwC, *Individual -- Deductions* |

### Rule 9 -- Payroll filing: monthly IPC21

- **IPC21 filing deadline** — Employers file Form IPC21 (combined PIT + CNAS + CNAM) by the 25th of the month following the reporting month, with payment due the same date, to the State Tax Service (SFS).  _(Rivermate; SFS)_

### Rule 10 -- Annual individual return: CET18

- **CET18 filing deadline** — The annual individual income tax return (Form CET18) is due by 30 April of the year following the reporting year. Foreign citizens earning income from Moldovan residents file a short-stay return within 3 days of ending the activity.  _(PwC, *Individual -- Tax administration*)_

### Rule 11 -- Minimum wage and average salary

- **Minimum wage and average salary** — Minimum wage = 5,500 MDL/month in 2025, rising to 6,300 MDL/month from 1 January 2026. Forecast economy-wide average monthly salary = 16,100 MDL for 2025 and 17,400 MDL for 2026; it is used for contribution caps/floors and the IT Park minimum tax base.  _(Govt Decision 846/2024; WageIndicator; Govt decision of 17 Dec 2025; MOLDPRES; social.gov.md)_

### Rule 12 -- Moldova IT Park (MITP) single tax = 7%

- **MITP single tax rate** — 7% percent of monthly turnover (not less than 30% of the forecast average monthly salary per employee; REPLACES CIT, salary PIT, employer SSC, employee health insurance and several other taxes; regime guaranteed to 2035; standard payroll rules do not apply (R-MD-SC-2))  _(Invest Moldova)_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Special / hazardous working conditions (32% vs 24%)

- **T2-1** — Trigger: Employer claims the 32% employer CNAS rate, or the work involves hazardous conditions. Issue: The 32% rate (vs the standard 24%) and any sector-specific splits (e.g. an 18% employer + 6% state-budget split mentioned in one PwC pass for agriculture) must be confirmed against the current state social insurance budget law. Action: Flag for reviewer. Default to 24% until confirmed.

### T2-2 -- Conflicting secondary data (6% employee SSC / 4.5%-4.5% health split)

- **T2-2** — Trigger: A source (Rivermate, Safeguard Global, G-P, Native Teams, etc.) reports a 6% employee social insurance contribution and/or a 4.5%/4.5% employer-employee health split. Issue: These reflect the pre-October-2018 regime and are contradicted by PwC's current pages (24% employer CNAS, 9% employee-borne CNAM, no employee SSC). Action: Apply PwC/CNAS (0% employee SSC, 9% employee CNAM). Flag for reviewer to confirm the precise 2025 employee-side position against the Tax Code / Law 489/1999, especially for special categories.

### T2-3 -- Personal allowance cap (360,000 MDL)

- **T2-3** — Trigger: Annual taxable income approaches or exceeds 360,000 MDL. Issue: The standard 29,700 MDL personal allowance is available only if annual taxable income does not exceed 360,000 MDL. Above that, no allowance applies. Action: Confirm annual income before applying the monthly 2,475 MDL allowance in PAYE; recompute on the CET18.

### T2-4 -- Increased / major allowances

- **T2-4** — Trigger: Client claims the major (34,620 MDL), spouse (21,780 MDL), or severe-disability dependent (21,780 MDL) allowance. Issue: Qualifying conditions for the increased allowances are not fully enumerated [RESEARCH GAP -- reviewer to confirm]. Action: Flag for reviewer. Do not apply increased allowances without confirmation.

### T2-5 -- Tax-year boundary (2025 vs 2026 figures)

- **T2-5** — Trigger: Computation spans the 2025/2026 boundary, or it is unclear which year's figures apply. Issue: Minimum wage rises from 5,500 to 6,300 MDL, fixed SSC from 20,518 to 22,878 MDL, and forecast average salary from 16,100 to 17,400 MDL effective 1 Jan 2026. PwC pages now display 2026 figures because they were re-reviewed in January 2026. Action: Use 2025 figures for periods up to 31 Dec 2025; 2026 figures from 1 Jan 2026. Flag any cross-boundary computation for reviewer.

### T2-6 -- Self-employed / individually insured status

- **T2-6** — Trigger: Individual has no employer, or status (employee vs self-employed) is unclear. Issue: Self-employed/individually insured persons pay a fixed annual SSC (20,518 MDL in 2025) and a fixed CNAM premium (12,636 MDL) rather than percentage-based contributions on remuneration. Justice-sector freelancers have a higher fixed SSC. Action: Confirm status and category before computing (R-MD-SC-1).

### T2-7 -- Contribution arrears and penalties

- **T2-7** — Trigger: Unpaid CNAS/CNAM/PIT from prior periods. Issue: Late CNAS = 0.1%/day (Law 489/1999, art. 28); late PIT interest = 0.0301%/day. Both compound. Action: Quantify only from an official SFS/CNAS statement. Escalate to a licensed Moldovan accountant (R-MD-SC-4).  _(Law 489/1999, art. 28)_

## Section 7 -- Excel working paper template

When producing a Moldovan payroll/contribution computation, structure the working paper as follows:

```
MOLDOVA PAYROLL & CONTRIBUTION COMPUTATION -- WORKING PAPER
Client / Employer: [name]
Tax Year:          [2025 / 2026]
Prepared:          [date]

INPUT DATA
  Employment status:             [Employee / Self-employed / Individually insured]
  Working conditions:            [Standard 24% / Special 32%]
  Full-time or part-time:        [FT / PT]
  Gross monthly remuneration:    MDL [____]
  Annual taxable income:         MDL [____]   (test vs 360,000 cap)
  Personal allowance applies:    [YES if <= 360,000 / NO]
  MITP resident:                 [YES -> STOP / NO]

EMPLOYEE-SIDE COMPUTATION (monthly)
  Gross remuneration:            MDL [____]
  Employee CNAM (9%):            MDL [____]
  Personal allowance (2,475):    MDL [____]
  PIT base:                      MDL [____]   (gross - CNAM - allowance)
  PIT (12%):                     MDL [____]
  Net pay:                       MDL [____]   (gross - CNAM - PIT)

EMPLOYER-SIDE COMPUTATION (monthly)
  Employer CNAS (24% / 32%):     MDL [____]
  Employer CNAM (0%):            MDL 0.00
  Employer total cost:           MDL [____]   (gross + CNAS)

SELF-EMPLOYED (if applicable, annual)
  Fixed annual SSC:              MDL [20,518 (2025) / 22,878 (2026)]
  Fixed annual CNAM premium:     MDL 12,636

FILING
  Monthly IPC21 due:             25th of following month
  Annual CET18 due:              30 April following year

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How payroll, contribution and PIT items appear on Moldovan bank statements

Moldovan retail/business banks include Maib (formerly Moldova Agroindbank), MICB (Moldindconbank), OTP Bank Moldova, and Victoriabank. Statements are typically in Romanian; English variants appear on some corporate accounts.

**Social insurance (CNAS):**
- Description: "CNAS", "CASA NATIONALA DE ASIGURARI SOCIALE", "BASS", "CONTRIBUTII SOCIALE", "CONTRIBUTIE SOCIALA FIXA"
- Timing: monthly (employer 24%/32%), or annual lump sum (self-employed fixed)
- Amount: employer = 24% (or 32%) of gross; self-employed = 20,518 MDL annual (2025)

**Health insurance (CNAM):**
- Description: "CNAM", "ASIGURARE MEDICALA", "ASIGURARI MEDICALE", "PRIMA ASIGURARE MEDICALA", "FAOAM"
- Timing: monthly (employee 9% via IPC21), or annual (fixed 12,636 MDL premium)

**Income tax / combined remittance:**
- Description: "SFS", "SERVICIUL FISCAL DE STAT", "IMPOZIT PE VENIT", "IPC21", "IPC"
- Timing: by the 25th of the following month
- Note: SFS collects PIT, CNAS and CNAM together via IPC21; a single line may bundle all three

**Key identification tips:**
1. Contribution and PIT remittances are always outgoing (DEBIT) to CNAS/CNAM/SFS, never credits
2. Employer CNAS recurs monthly at a consistent percentage of gross; self-employed fixed SSC is a single annual lump sum
3. PENSIE / INDEMNIZATIE / AJUTOR SOCIAL credits are benefits RECEIVED, not contributions paid
4. A single IPC21 remittance line may combine PIT + employee CNAM + employer CNAS -- request the IPC21 detail to itemise
5. SALARIU / AVANS debits are net wages (payroll expense), not contributions

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for CNAS / CNAM / SFS debits** -- identify all outgoing payments matching Section 3 patterns
2. **Sum by category** -- total CNAS (employer social), CNAM (health), and SFS/IPC21 (PIT + combined) separately
3. **Reverse-engineer the gross (employee case):**
   - Employer CNAS / 0.24 ~= monthly gross (standard conditions)
   - Employee CNAM / 0.09 ~= monthly gross
   - Cross-check the two; they should imply the same gross
4. **Identify self-employed fixed payments:**
   - A single ~20,518 MDL CNAS debit (2025) -> fixed annual social contribution
   - A single ~12,636 MDL CNAM debit -> fixed annual health premium
5. **Flag for reviewer:** "Payroll classification derived from bank statement amounts only. Employment status, working conditions, allowance entitlement and tax year have not been independently verified. Reviewer must confirm before filing IPC21 / CET18."

### Contribution & rate summary (2025; sources in column)

**Contribution & rate summary (2025; sources in column)**  _(PwC; CNAS)_

| Item | Payer | Rate / amount | Source |
| --- | --- | --- | --- |
| State social insurance (CNAS), standard | Employer | 24% of gross | PwC, *Corporate -- Other taxes* |
| State social insurance (CNAS), special conditions | Employer | 32% of gross | PwC, *Individual -- Other taxes* |
| State social insurance (CNAS) | Employee | 0% | PwC, *Individual -- Other taxes* |
| Mandatory health insurance (CNAM) | Employee | 9% of wages | PwC, *Individual -- Other taxes* |
| Mandatory health insurance (CNAM) | Employer | 0% | PwC, *Corporate -- Other taxes* |
| Personal income tax (PIT) | Employee | 12% flat | PwC, *Individual -- Taxes on personal income* |
| Fixed annual SSC (self-employed) | Individual | 20,518 MDL (2025); 22,878 MDL (2026) | CNAS |
| Fixed annual health premium (self-employed) | Individual | 12,636 MDL (2025 & 2026) | PwC, *Individual -- Deductions* |

- **Standard employee totals summary** — Standard employee totals (per cell): employee column = 0% CNAS + 9% CNAM = 9%; employer column = 24% CNAS + 0% CNAM = 24%; combined statutory wedge above gross = 24% (employer) + 9% (employee withholding) + 12% PIT on net-of-allowance base.  _(PwC)_

### Other Moldovan rates (context; not payroll, but cited for cross-checks)

**Other Moldovan rates (context; not payroll, but cited for cross-checks)**  _(PwC; Invest Moldova)_

| Tax | Rate | Source |
| --- | --- | --- |
| Corporate income tax (standard) | 12% | PwC, *Corporate -- Taxes on corporate income* |
| SME regime (non-VAT) | 4% of turnover | PwC, *Corporate -- Taxes on corporate income* |
| Farming | 7% | PwC, *Corporate -- Taxes on corporate income* |
| IT Park (MITP) single tax | 7% of turnover (>= 30% of forecast avg salary/employee) | Invest Moldova |
| VAT (standard) | 20% (reduced 8% / 6%) | PwC, *Corporate -- Other taxes* |

### Thresholds (sources in column)

**Thresholds (sources in column)**  _(Intelcont; PwC; WageIndicator; MOLDPRES; social.gov.md; KPMG)_

| Threshold | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Standard personal allowance | 29,700 MDL/yr (~2,475/mo), only if income <= 360,000 MDL | 29,700 MDL/yr (PwC carries same) | Intelcont; PwC |
| Major personal allowance | 34,620 MDL/yr | -- [RESEARCH GAP -- reviewer to confirm 2026] | PwC, *Individual -- Deductions* |
| Spouse's major allowance | 21,780 MDL/yr | -- [RESEARCH GAP -- reviewer to confirm 2026] | PwC, *Individual -- Deductions* |
| Per dependent | 9,900 MDL/yr (21,780 if severe disability) | -- [RESEARCH GAP -- reviewer to confirm 2026] | PwC, *Individual -- Deductions* |
| Minimum wage | 5,500 MDL/mo | 6,300 MDL/mo (confirmed) | WageIndicator; MOLDPRES |
| Forecast average monthly salary | 16,100 MDL | 17,400 MDL | social.gov.md |
| SSC minimum contribution base | National minimum wage (5,500 MDL); 25% for part-time | National minimum wage (6,300 MDL) | PwC, *Corporate -- Other taxes* |
| VAT mandatory registration | 1,200,000 MDL / 12 months | 1,500,000 MDL (from 1 Jan); 1,700,000 MDL (from 1 Mar) | KPMG |

### Forms

**Forms**  _(Rivermate; SFS; PwC)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| IPC21 | Monthly combined declaration of withheld PIT + CNAS + CNAM (employer return) | 25th of the following month | Rivermate; SFS |
| CET18 | Annual individual income tax return / reconciliation | 30 April of the following year | PwC, *Individual -- Tax administration* |
| Foreign-citizen short-stay return | Return for foreign citizens earning income from Moldovan residents | Within 3 days of ending the activity | PwC, *Individual -- Tax administration* |

### Penalties

**Penalties**  _(CNAS; PwC)_

| Penalty | Rate | Basis | Source |
| --- | --- | --- | --- |
| Late payment of social insurance (CNAS) | 0.1% of the amount owed per day | Law No. 489/1999, art. 28 | CNAS |
| Interest on late payment of PIT | 0.0301% per day on total tax due | Tax Code (rate set annually) | PwC, *Individual -- Tax administration* |

### Test suite

All employee tests use 2025 figures: CNAM 9%, allowance 2,475 MDL/month, PIT 12% on (gross − CNAM − allowance), employer CNAS 24% standard.

Test 1 -- Minimum wage employee (5,500 MDL). CNAM = 495.00; PIT base = 5,500 − 495 − 2,475 = 2,530.00; PIT = 303.60; net = 4,701.40; employer CNAS = 1,320.00; employer cost = 6,820.00.

Test 2 -- Average-salary employee (16,100 MDL). CNAM = 1,449.00; PIT base = 16,100 − 1,449 − 2,475 = 12,176.00; PIT = 1,461.12; net = 13,189.88; employer CNAS = 3,864.00; employer cost = 19,964.00.

Test 3 -- 10,000 MDL employee. CNAM = 900.00; PIT base = 10,000 − 900 − 2,475 = 6,625.00; PIT = 795.00; net = 8,305.00; employer CNAS = 2,400.00; employer cost = 12,400.00.

Test 4 -- Special-conditions employee (20,000 MDL, 32% CNAS). CNAM = 1,800.00; PIT base = 20,000 − 1,800 − 2,475 = 15,725.00; PIT = 1,887.00; net = 16,313.00; employer CNAS 32% = 6,400.00; employer cost = 26,400.00. (32% to be reviewer-confirmed.)

Test 5 -- High earner above allowance cap (gross 40,000 MDL/mo => 480,000 MDL/yr > 360,000). No personal allowance. CNAM = 3,600.00; PIT base = 40,000 − 3,600 − 0 = 36,400.00; PIT = 4,368.00; net = 31,032.00; employer CNAS = 9,600.00; employer cost = 49,600.00.

Test 6 -- Self-employed (2025). Fixed annual SSC = 20,518.00 MDL; fixed annual CNAM premium = 12,636.00 MDL; total fixed contributions = 33,154.00 MDL. No 24% / 9% percentage contributions apply.

Test 7 -- Employee SSC check. Any employee, any gross: employee state social insurance = 0.00 MDL. (Reject any 6% employee figure.)

Test 8 -- Tax-year boundary. Same gross employee on 1 Jan 2026: use minimum wage 6,300 MDL, fixed SSC 22,878 MDL, average salary 17,400 MDL; rates (24% / 9% / 12%) unchanged absent a new budget law.

### Prohibitions

- **No 6% employee SSC** — NEVER apply a 6% employee social insurance contribution -- employees pay 0% under the current (post-2018) system  _(n/a)_
- **No 4.5%/4.5% CNAM split** — NEVER apply a 4.5%/4.5% employer/employee health split -- CNAM is 9%, fully employee-borne, employer 0%  _(n/a)_
- **No standard payroll for MITP resident** — NEVER compute standard payroll for a Moldova IT Park (MITP) resident -- the 7% single tax replaces SSC/PIT; escalate  _(n/a)_
- **No unconfirmed 32% special-conditions rate** — NEVER apply the 32% special-conditions CNAS rate without reviewer confirmation -- default to 24%  _(n/a)_
- **No allowance above 360,000 MDL** — NEVER grant the 29,700 MDL personal allowance when annual taxable income exceeds 360,000 MDL  _(n/a)_
- **No mixing 2025/2026 thresholds** — NEVER mix 2025 and 2026 thresholds in one computation -- pick the year of the period and apply it consistently  _(n/a)_
- **Fixed SSC not a percentage** — NEVER treat the self-employed fixed annual SSC (20,518 MDL) as a percentage of income -- it is a flat statutory amount  _(n/a)_
- **No confusing credit with contribution** — NEVER confuse a CNAS/CNAM credit (PENSIE / INDEMNIZATIE benefit received) with a contribution paid  _(n/a)_
- **No quantifying arrears without official statement** — NEVER quantify contribution arrears or penalties without an official SFS/CNAS statement -- escalate  _(n/a)_
- **Figures are estimates only** — NEVER present figures as definitive -- label as estimated and direct the client to their SFS e-cabinet / IPC21 and CNAS/CNAM statements  _(n/a)_

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
