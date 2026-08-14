---
name: mozambique-social-contributions
description: Use this skill whenever asked about Mozambique social security contributions (INSS), payroll, or personal income tax (IRPS) for employees, employers, or self-employed individuals. Trigger on phrases like "how much INSS do I pay", "Mozambique social security", "INSS employer rate", "INSS employee 3%", "Segurança Social", "Instituto Nacional de Segurança Social", "Mozambique payroll tax", "IRPS calculation", "Mozambique income tax brackets", "PAYE Mozambique", "salário mínimo", "Mozambican minimum wage", or any question about Mozambique payroll or social-contribution obligations. Also trigger when classifying bank statement transactions that relate to INSS debits, IRPS/PAYE remittances, or salary payments from Mozambican banks (BCI, Millennium BIM, Standard Bank Moçambique, Absa Moçambique). This skill covers the 4% employer / 3% employee INSS rates, contribution base, registration and payment deadlines, IRPS resident brackets and PAYE, non-resident flat withholding, minimum wages by sector, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Mozambique payroll or social-contribution work.
version: 0.1
jurisdiction: MZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique Social Security (INSS) & Payroll Tax

## Mozambique Social Security (INSS) & Payroll Tax Skill v0.1

Mozambique **does** levy a personal income tax (IRPS), so this skill covers both the **INSS social contribution** (the primary subject) and the **IRPS payroll/PAYE reality** an employer must withhold. It is **not** a no-PIT jurisdiction.

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Mozambique (Republic of Mozambique) |
| Currency | Mozambican Metical (MZN / MT) -- this skill uses MZN only |
| Tax year | Calendar year (1 Jan -- 31 Dec) |
| Social security authority | Instituto Nacional de Segurança Social (INSS) |
| Tax authority | Autoridade Tributária de Moçambique (AT) |
| INSS employer rate | **4%** of monthly remuneration (PwC; mozambiqueexpert) |
| INSS employee rate | **3%** of monthly remuneration (PwC; mozambiqueexpert) |
| INSS total rate | **7%** (PwC; mozambiqueexpert) |
| INSS contribution floor | None found in authoritative sources [RESEARCH GAP -- reviewer to confirm] |
| INSS contribution ceiling | None found in authoritative sources [RESEARCH GAP -- reviewer to confirm] |
| INSS payment window | 20th of current month -- 10th of following month, via INSS e-platform (mozambiqueexpert) |
| IRPS resident regime | Progressive 10%--32% on annual taxable income (PwC) |
| IRPS PAYE remittance | By the 20th of the following month (PwC) |
| Non-resident IRPS | Flat 20% definitive withholding on Mozambique-source income (PwC) |
| Validated by | Pending -- requires sign-off by a Mozambican licensed tax professional |
| Validation date | Pending |

**INSS contribution overview**

| Party | Rate | Mechanism |
| --- | --- | --- |
| Employee | 3% | Withheld by employer from gross remuneration (PwC) |
| Employer | 4% | Paid by employer on top of remuneration (PwC) |
| **Total remitted** | **7%** | Employer remits combined 3% + 4% to INSS (PwC; mozambiqueexpert) |

*Arithmetic check: 3% (employee) + 4% (employer) = 7% (total). ✓*

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown whether worker is employee vs self-employed | Assume employee; INSS 7% (4%+3%) applies |
| Unknown which pay items are in the contribution base | Include only basic wage + regular consistent items; EXCLUDE meal subsidy, one-off bonuses, reimbursements (PwC) |
| Unknown residency for IRPS | Ask -- do not assume; resident = worldwide progressive, non-resident = flat 20% (PwC) |
| Unknown whether foreign employee has home-country scheme | Apply INSS; exemption is by request only (PwC) |
| Unknown contribution floor/ceiling | Apply rate to full remuneration base; no statutory cap found [RESEARCH GAP] |
| Unknown sector for minimum-wage check | STOP -- minimum wage is sector-specific (DLA Piper) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- monthly gross remuneration and a breakdown of pay components (so the contribution base can be isolated), plus worker status (employee vs self-employed).

**Recommended** -- residency status for IRPS, sector (for minimum-wage validation), and whether the worker is a foreign employee with a comparable home-country scheme.

**Ideal** -- INSS registration confirmation, prior payroll runs, and the AT NUIT (Número Único de Identificação Tributária) for the employer.

### Refusal catalogue

- **R-MZ-INSS-1 -- Contribution base unclear** — "The INSS base includes basic wages, seniority/management bonuses, regular productivity/attendance premiums, night-work pay and consistent allowances/commissions, but EXCLUDES meal subsidies, irregular one-off bonuses and expense reimbursements. Cannot compute INSS without an itemised pay breakdown." (Trigger: pay components not itemised.)  _(PwC; mozambiqueexpert)_
- **R-MZ-INSS-2 -- INSS arrears / penalties** — "Late INSS contributions attract monthly late-payment interest plus administrative fines; the exact percentages are not stated in authoritative sources [RESEARCH GAP -- reviewer to confirm]. Do not quantify arrears without an INSS statement. Escalate to a Mozambican licensed professional." (Trigger: client has unpaid INSS contributions.)  _([RESEARCH GAP -- reviewer to confirm])_
- **R-MZ-INSS-3 -- Foreign-employee exemption** — "Foreign employees may request exemption only where they contribute to a comparable scheme in their home country. This is by application, not automatic. Escalate to confirm before excluding INSS." (Trigger: foreign employee claims INSS exemption.)  _(PwC)_
- **R-MZ-IRPS-1 -- New IRPS residency / Law 11/2025 effects** — "Law No. 11/2025 (effective 29 Dec 2025) redefined residency (removed the 180-day test), introduced a 10% final withholding on digital-service income and e-money agent commissions, and added an autonomous capital-gains regime (Art. 54-A). These require case-specific analysis. Escalate to a Mozambican licensed professional." (Trigger: client circumstances touch residency, digital-service income, electronic-money agent commissions, or capital gains.)  _(DLA Piper)_
- **R-MZ-IRPS-2 -- Exact penalty quantification** — "Exact statutory IRPS penalty figures in MZN were not located from the authority; secondary estimates cite roughly USD 100--USD 33,000 plus interest [RESEARCH GAP -- reviewer to confirm]. Do not state a definitive figure. Escalate." (Trigger: client asks for the exact MZN penalty for late filing/payment.)  _([RESEARCH GAP -- reviewer to confirm])_

## Section 3 -- Payment pattern library

Deterministic pre-classifier for Mozambican bank statement transactions. Match by case-insensitive substring on the counterparty/reference. INSS and IRPS payments always EXCLUDE from any VAT return or revenue/expense classification -- they are statutory payroll obligations, not business supplies. (Portuguese is the official language; references appear in Portuguese.)

### 3.1 INSS social-security debits

**INSS social-security debit patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INSS, I.N.S.S. | EXCLUDE -- INSS contribution | Monthly 7% (4% employer + 3% employee) remittance |
| SEGURANCA SOCIAL, SEGURANÇA SOCIAL | EXCLUDE -- INSS contribution | Portuguese-language reference |
| INST NACIONAL SEGURANCA SOCIAL | EXCLUDE -- INSS contribution | Full authority name |
| CONTRIBUICAO INSS, CONTRIBUIÇÃO INSS | EXCLUDE -- INSS contribution | Explicit contribution reference |

### 3.2 IRPS / PAYE tax remittances (NOT INSS -- do not confuse)

**IRPS/PAYE tax remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRPS | EXCLUDE -- income tax (PAYE), not INSS | Withheld employee income tax remitted to AT |
| AUTORIDADE TRIBUTARIA, AT MOCAMBIQUE | EXCLUDE -- tax payment | AT remittance, not social security |
| EDECLARACAO, eDeclaração | EXCLUDE -- tax filing/payment | AT income-tax platform |
| IRPC | EXCLUDE -- corporate income tax | Company-level, not payroll INSS |
| IVA, VAT | EXCLUDE -- value added tax (16%) | Not INSS |

### 3.3 Salary and payroll (exclude from INSS classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SALÁRIO, ORDENADO (outgoing) | EXCLUDE -- payroll expense | Gross wage payment, not the INSS remittance |
| VENCIMENTO, PAGAMENTO SALARIAL (outgoing) | EXCLUDE -- payroll expense | Same |
| SALARIO, ORDENADO (incoming) | EXCLUDE -- employment income received | Not an INSS payment |

### 3.4 Mozambican banks -- typical debit descriptions

**Mozambican banks typical debit descriptions**

| Bank | Typical description | Treatment |
| --- | --- | --- |
| BCI (Banco Comercial e de Investimentos) | "INSS" or "SEGURANCA SOCIAL" | EXCLUDE -- INSS |
| Millennium BIM | "INSS CONTRIB" or "SEGURANÇA SOCIAL" | EXCLUDE -- INSS |
| Standard Bank Moçambique | "INSS" or "INST NAC SEG SOCIAL" | EXCLUDE -- INSS |
| Absa Moçambique | "INSS" or "CONTRIBUICAO SOCIAL" | EXCLUDE -- INSS |

## Section 4 -- Worked examples

All examples use a hypothetical Maputo employer. INSS figures are recomputed to the cent. Contribution base = pensionable remuneration after excluding meal subsidy, one-off bonuses and reimbursements (PwC).

### Example 1 -- Standard monthly INSS remittance (Millennium BIM)

**Input line:**
`10.02.2025 ; INSS CONTRIB ; DEBITO ; REF JANEIRO 2025 ; -2,100.00 ; MZN`

**Reasoning:**
Matches "INSS CONTRIB" (pattern 3.4, Millennium BIM). Single employee, contribution base MZN 30,000.00. Total INSS = 7% x 30,000.00 = **2,100.00** (employer 4% = 1,200.00; employee 3% = 900.00). Paid within the 20th-of-month to 10th-of-following-month window. EXCLUDE from VAT.

*Check: 30,000.00 x 0.07 = 2,100.00; 1,200.00 + 900.00 = 2,100.00. ✓*

**Classification:** EXCLUDE -- INSS contribution.

### Example 2 -- INSS where meal subsidy must be excluded (BCI)

**Input line:**
`08.03.2025 ; SEGURANCA SOCIAL ; DEBITO ; FEV 2025 ; -1,400.00 ; MZN`

**Reasoning:**
Employee gross pay MZN 25,000.00 but includes a MZN 5,000.00 meal subsidy, which is EXCLUDED from the base (PwC). Contribution base = 25,000.00 - 5,000.00 = 20,000.00. Total INSS = 7% x 20,000.00 = **1,400.00** (employer 800.00; employee 600.00).

*Check: 20,000.00 x 0.07 = 1,400.00; 800.00 + 600.00 = 1,400.00. ✓*

**Classification:** EXCLUDE -- INSS contribution. Confirm meal subsidy was correctly excluded from base.

### Example 3 -- IRPS/PAYE remittance (NOT INSS)

**Input line:**
`18.02.2025 ; AUTORIDADE TRIBUTARIA ; DEBITO ; IRPS JANEIRO ; -3,200.00 ; MZN`

**Reasoning:**
Matches "AUTORIDADE TRIBUTARIA" + "IRPS" (pattern 3.2). This is withheld employee income tax remitted to the AT (due by the 20th of the following month, PwC), NOT a social-security contribution. Do not classify as INSS.

**Classification:** EXCLUDE -- income tax (IRPS/PAYE). NOT INSS.

### Example 4 -- Salary outgoing (payroll, not INSS)

**Input line:**
`25.02.2025 ; SALARIO JOAO MUCAVELE ; DEBITO ; VENCIMENTO FEV ; -28,100.00 ; MZN`

**Reasoning:**
Matches "SALARIO" / "VENCIMENTO" (pattern 3.3). This is the net wage paid to the employee, not the INSS remittance. The employee's 3% INSS and IRPS were already withheld; the employer's 4% INSS is remitted separately (see Example 1/2).

**Classification:** EXCLUDE -- payroll expense. NOT the INSS remittance.

### Example 5 -- Combined IRPS calculation for a mid-income employee

**Input data:** Resident employee, annual taxable income MZN 300,000.00. (IRPS bracket 168,000--504,000: 20%, parcela a abater MZN 10,500 -- PwC.)

**Reasoning:**
Annual IRPS = 300,000.00 x 20% - 10,500.00 = 60,000.00 - 10,500.00 = **49,500.00**.

*Check: 300,000.00 x 0.20 = 60,000.00; 60,000.00 - 10,500.00 = 49,500.00. ✓*

INSS on this salary (assuming the full MZN 300,000.00 / 12 = 25,000.00/month is pensionable base): employee 3% = 750.00/month = 9,000.00/year; employer 4% = 1,000.00/month = 12,000.00/year. The employee 3% is deductible from gross income for IRPS (PwC) -- reviewer to apply before final taxable base.

**Classification:** IRPS payable MZN 49,500.00 before the employee-INSS deduction adjustment. EXCLUDE all related remittances from VAT.

### Example 6 -- Non-resident flat withholding

**Input data:** Non-resident contractor, Mozambique-source fee MZN 100,000.00.

**Reasoning:**
Non-residents face a flat **20% definitive withholding** on Mozambique-source income (PwC). IRPS withheld = 100,000.00 x 20% = **20,000.00**. No progressive brackets, no annual return aggregation.

*Check: 100,000.00 x 0.20 = 20,000.00. ✓*

**Classification:** EXCLUDE from VAT. Definitive 20% withholding, not progressive IRPS.

### Example 7 -- Minimum-wage validation (sector check)

**Input data:** Construction-sector employee, basic wage MZN 8,000.00/month.

**Reasoning:**
2025 construction minimum wage (Decree 92/2025) = **8,400.00/month** (DLA Piper). The proposed MZN 8,000.00 is **below** the sector minimum. STOP -- flag for reviewer; the wage must be raised to at least 8,400.00 before INSS is computed on it.

*Check: 8,000.00 < 8,400.00. ✓ (below minimum)*

**Classification:** Payroll non-compliant -- minimum wage breach. Escalate.

## Section 5 -- Tier 1 rules

Apply exactly as written when pay data is clear and inputs are complete.

### Rule 1 -- INSS formula

- **INSS formula** — INSS_employee = contribution_base x 3% INSS_employer = contribution_base x 4% INSS_total    = contribution_base x 7% (Employer withholds the 3% and remits the combined 7%.)  _(PwC; mozambiqueexpert)_

### Rule 2 -- Contribution base

- **Contribution base composition** — Include: basic wages, seniority bonuses, management bonuses, regular productivity/attendance premiums, night-work pay, consistent allowances/commissions. EXCLUDE: meal subsidies, irregular/one-time bonuses, expense reimbursements.  _(PwC; mozambiqueexpert)_

### Rule 3 -- No statutory floor/ceiling found

- **No statutory floor/ceiling** — No statutory minimum or maximum INSS contribution base was found in authoritative sources [RESEARCH GAP -- reviewer to confirm]. Apply the 7% to the full qualifying base unless a reviewer confirms a cap.  _([RESEARCH GAP -- reviewer to confirm])_

### Rule 4 -- Employee 3% is IRPS-deductible

- **Employee 3% IRPS deduction** — The employee's 3% INSS is deductible from gross income for IRPS purposes. Apply before computing progressive IRPS.  _(PwC)_

### Rule 5 -- IRPS resident progressive schedule

**IRPS resident progressive schedule**  _(PwC; brackets confirmed unchanged by Law No. 11/2025, DLA Piper)_

| Annual taxable income (MZN) | Rate | Parcela a abater (MZN) |
| --- | --- | --- |
| 0 -- 42,000 | 10% | 0 |
| 42,000 -- 168,000 | 15% | 2,100 |
| 168,000 -- 504,000 | 20% | 10,500 |
| 504,000 -- 1,512,000 | 25% | 37,500 |
| Over 1,512,000 | 32% | 141,540 |

- **IRPS formula** — IRPS = income x marginal rate - parcela a abater. Monthly PAYE runs 0%--32%.  _(PwC; DLA Piper)_

### Rule 6 -- Non-resident flat withholding

- **Non-resident flat withholding** — Non-residents: flat 20% definitive withholding on Mozambique-source income. No aggregation, no annual return for that income.  _(PwC)_

### Rule 7 -- Foreign-employee INSS exemption is by request only

- **Foreign-employee exemption** — Foreign employees may request exemption only if they contribute to a comparable home-country scheme. Not automatic -- apply INSS unless a reviewer confirms exemption.  _(PwC)_

### Rule 8 -- INSS payment window

- **INSS payment window** — Contributions are payable between the 20th of the current month and the 10th of the following month, via the electronic INSS platform. Treat the 10th of the following month as the deadline.  _(mozambiqueexpert)_

### Rule 9 -- IRPS / PAYE remittance and filing

- **IRPS/PAYE remittance and filing** — Employer PAYE remittance by the 20th of the following month. Annual return filed January--April following the tax year; from 1 Jan 2026, resident individuals with only employment income must file an annual return (previously exempt if fully withheld). Final tax payment: end of May (employment income) / end of June (other income).  _(PwC)_

### Rule 10 -- Registration deadlines (INSS)

- **INSS registration deadlines** — Employers register with INSS within 15 days of business commencement; employees registered within 30 days of contract start; status changes notified within 30 days.  _(mozambiqueexpert)_

### Rule 11 -- Municipal/local tax

- **Municipal/local tax** — Local tax may apply, e.g. Maputo residents owe MZN 510/year (2024 rate), typically withheld by employer. Confirm the current-year figure with the municipality [RESEARCH GAP -- 2025/2026 rate to confirm].  _(PwC)_

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Pay-component classification ambiguity

- **T2-1** — Trigger: A pay item (e.g. a commission or allowance) may or may not be "regular/consistent" enough to enter the INSS base. Issue: Only regular, consistent allowances/commissions are in-base; irregular ones are out. The boundary is judgemental. Action: Flag for reviewer with the payment history.  _(PwC)_

### T2-2 -- Foreign employee with home-country scheme

- **T2-2** — Trigger: Foreign employee asserts a comparable home-country contribution. Issue: Exemption is by application only and depends on the comparability of the foreign scheme. Action: Flag for reviewer; do not exclude INSS without confirmation.  _(PwC)_

### T2-3 -- Law 11/2025 residency reclassification

- **T2-3** — Trigger: Worker's residency status is unclear post-29 Dec 2025. Issue: Law 11/2025 removed the 180-day test and broadened residency to main residence, professional activity, centre of economic interests, Mozambican vessel/aircraft crew, and nationals on foreign assignment not fully taxed abroad. Action: Flag for reviewer to determine resident vs non-resident treatment.  _(DLA Piper)_

### T2-4 -- Digital-service / e-money agent income

- **T2-4** — Trigger: Worker earns digital-service income or electronic-money agent commissions. Issue: From Law 11/2025, these are subject to a final 10% withholding -- different from standard PAYE. Action: Flag for reviewer.  _(DLA Piper)_

### T2-5 -- Capital gains (autonomous regime)

- **T2-5** — Trigger: Individual realises capital gains. Issue: Law 11/2025 added an autonomous capital-gains regime (Art. 54-A) using the same 10%--32% schedule; such income is no longer aggregated. Action: Flag for reviewer; do not aggregate into employment IRPS.  _(DLA Piper)_

### T2-6 -- INSS arrears / penalties

- **T2-6** — Trigger: Unpaid INSS from prior periods. Issue: Monthly late-payment interest and administrative fines apply; exact rates not stated in authoritative sources [RESEARCH GAP]. Action: Do not quantify without an INSS statement. Escalate.  _([RESEARCH GAP])_

### T2-7 -- Minimum-wage breach

- **T2-7** — Trigger: Basic wage appears below the 2025 sector minimum (Section 10 table). Issue: Minimum wages are sector-specific (Decrees 87/2025--94/2025). A further revision took effect ~1 April 2026 [RESEARCH GAP -- 2026 figures not yet sourced]. Action: Flag for reviewer; payroll must comply before INSS computation.  _(DLA Piper)_

## Section 7 -- Excel working paper template

MOZAMBIQUE PAYROLL / INSS COMPUTATION -- WORKING PAPER
Client: [name]               NUIT: [____]
Tax Year: [year]             Prepared: [date]

INPUT DATA
  Worker status:                 [Employee / Self-employed]
  Residency (IRPS):              [Resident / Non-resident]
  Sector (minimum-wage check):   [____]
  Gross monthly remuneration:    MZN [____]
  Meal subsidy (EXCLUDED):       MZN [____]
  One-off bonuses (EXCLUDED):    MZN [____]
  Reimbursements (EXCLUDED):     MZN [____]
  INSS contribution base:        MZN [____]

INSS COMPUTATION (monthly)
  Employee 3%:                   MZN [____]
  Employer 4%:                   MZN [____]
  Total 7% remitted:             MZN [____]
  Payment due (10th of next mo): [____]

IRPS COMPUTATION (annual, residents)
  Annual taxable income:         MZN [____]
  Less employee INSS deduction:  MZN [____]
  Adjusted taxable income:       MZN [____]
  Marginal rate:                 [10/15/20/25/32]%
  Parcela a abater:              MZN [____]
  IRPS = income x rate - parcela:MZN [____]
  (Non-resident: 20% flat)       MZN [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

RESEARCH GAPS APPLIED
  [List any [RESEARCH GAP] items relied upon]

## Section 8 -- Bank statement reading guide

### How INSS and tax debits appear on Mozambican statements

**BCI (Banco Comercial e de Investimentos):**
- Description: "INSS" or "SEGURANCA SOCIAL"
- Timing: monthly, in the 20th-to-10th window (deadline 10th of following month)
- Amount: 7% of the monthly contribution base

**Millennium BIM:**
- Description: "INSS CONTRIB" or "SEGURANÇA SOCIAL"
- Timing: same monthly cycle

**Standard Bank Moçambique / Absa Moçambique:**
- Description: "INSS" / "INST NAC SEG SOCIAL" / "CONTRIBUICAO SOCIAL"
- Timing: same monthly cycle

**Key identification tips:**
1. INSS debits are outgoing (DEBITO), monthly, and equal 7% of the contribution base.
2. Do NOT confuse with AT/IRPS debits (income tax, due 20th of following month) or IRPC (corporate) or IVA (16% VAT).
3. Salary debits ("SALARIO", "VENCIMENTO", "ORDENADO") are net wages, not the INSS remittance.
4. References are typically in Portuguese.
5. The INSS figure should reconcile to 0.07 x base; the employee share alone is 0.03 x base.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for INSS debits** -- identify outgoing payments matching Section 3.1/3.4 patterns.
2. **Reverse-engineer the base** -- INSS / 0.07 = contribution base (e.g. 2,100.00 / 0.07 = 30,000.00).
3. **Separate tax from social security** -- AT/IRPS debits are income tax, not INSS; IRPC/IVA are company-level.
4. **Flag for reviewer:** "INSS and IRPS figures derived from bank statement amounts only. Contribution base composition, residency, and sector minimum wage have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### INSS quick computation (illustrative)

**INSS quick computation table**  _(Rates: PwC; mozambiqueexpert)_

| Contribution base (MZN/mo) | Employee 3% | Employer 4% | Total 7% |
| --- | --- | --- | --- |
| 10,000.00 | 300.00 | 400.00 | 700.00 |
| 20,000.00 | 600.00 | 800.00 | 1,400.00 |
| 30,000.00 | 900.00 | 1,200.00 | 2,100.00 |
| 50,000.00 | 1,500.00 | 2,000.00 | 3,500.00 |

*Check each row: 3% + 4% = 7%; e.g. 900.00 + 1,200.00 = 2,100.00. ✓ (Rates: PwC; mozambiqueexpert)*

### IRPS resident brackets 2025/2026 (PwC; DLA Piper)

**IRPS resident brackets 2025/2026**  _(PwC; DLA Piper)_

| Annual taxable income (MZN) | Rate | Parcela a abater (MZN) |
| --- | --- | --- |
| 0 -- 42,000 | 10% | 0 |
| 42,000 -- 168,000 | 15% | 2,100 |
| 168,000 -- 504,000 | 20% | 10,500 |
| 504,000 -- 1,512,000 | 25% | 37,500 |
| Over 1,512,000 | 32% | 141,540 |

- **Non-resident flat withholding** — Non-residents: flat 20% definitive withholding on Mozambique-source income.  _(PwC)_

### IRPS worked tax (parcela a abater method)

**IRPS worked tax table**

| Annual income (MZN) | Computation | IRPS (MZN) |
| --- | --- | --- |
| 42,000.00 | 42,000 x 15% - 2,100 | 4,200.00 |
| 168,000.00 | 168,000 x 20% - 10,500 | 23,100.00 |
| 300,000.00 | 300,000 x 20% - 10,500 | 49,500.00 |
| 504,000.00 | 504,000 x 25% - 37,500 | 88,500.00 |
| 2,000,000.00 | 2,000,000 x 32% - 141,540 | 498,460.00 |

*Checks: 42,000 x 0.15 = 6,300; 6,300 - 2,100 = 4,200.00 ✓ | 168,000 x 0.20 = 33,600; - 10,500 = 23,100.00 ✓ | 300,000 x 0.20 = 60,000; - 10,500 = 49,500.00 ✓ | 504,000 x 0.25 = 126,000; - 37,500 = 88,500.00 ✓ | 2,000,000 x 0.32 = 640,000; - 141,540 = 498,460.00 ✓*

### Minimum wages 2025 by sector (effective 1 July 2025; DLA Piper)

**Minimum wages 2025 by sector**  _(DLA Piper)_

| Sector | 2025 (MZN/month) | Decree |
| --- | --- | --- |
| Agriculture, Livestock, Hunting & Forestry | 6,688.00 | 87/2025 |
| Industrial/Semi-industrial Fishing | 6,726.88 | 88/2025 |
| Kapenta Fishing | 4,991.09 | 88/2025 |
| Mining Extraction | 15,176.66 | 89/2025 |
| Quarries/Sand (Medium) | 8,008.00 | 89/2025 |
| Salt Mining (Micro/Small) | 6,538.44 | 89/2025 |
| Manufacturing (excl. Bakery/Cashew) | 10,147.50 | 90/2025 |
| Bakery | 7,200.00 | 90/2025 |
| Cashew | 6,653.21 | 90/2025 |
| Electricity/Gas/Water (Large) | 12,275.00 | 91/2025 |
| Electricity/Gas/Water (SME) | 9,960.62 | 91/2025 |
| Construction | 8,400.00 | 92/2025 |
| Non-financial Services | 10,310.00 | 93/2025 |
| Hotel/Tourism | 9,700.00 | 93/2025 |
| Private Security | 8,465.00 | 93/2025 |
| Fuel Retail | 9,739.00 | 93/2025 |
| Banks/Insurance | 19,043.61 | 94/2025 |
| Microfinance/Microinsurance | 16,764.47 | 94/2025 |

A further revision took effect ~1 April 2026 [RESEARCH GAP -- 2026 figures not yet sourced authoritatively].

### Corporate & other taxes (context, PwC)

**Corporate & other taxes**  _(PwC)_

| Tax | Rate |
| --- | --- |
| IRPC (corporate income tax) | 32% standard |
| Non-resident WHT (no PE) | 20% generally; 10% for certain income incl. digital goods/services |
| Autonomous tax on confidential/undocumented expenses | 35% |
| VAT (IVA) | 16% standard |
| Property transfer (SISA) | 2% (10% for privileged-tax-regime beneficiaries) |
| Inheritance & gifts | 2%--10% |
| Stamp duty | 0.03%--50%, or fixed MZN 0.50--5,000 |
| Net wealth tax | None |

### Forms & platforms (PwC)

- **eDeclaração** (https://edeclaracao.at.gov.mz/) -- income-tax and payment returns.
- **Contribuinte Portal** (https://portaldocontribuinte.at.gov.mz/) -- VAT.
- **Form 6** -- declaration of commencement of activity.
- **NUIT** -- Single Tax ID required post-incorporation.
- INSS electronic platform -- contribution payments.

### Penalties

**Penalties**

| Item | Position |
| --- | --- |
| INSS late payment | Monthly interest + administrative fines; exact % not stated [RESEARCH GAP -- reviewer to confirm] (mozambiqueexpert) |
| IRPS late filing/payment | Secondary estimate ~USD 100 -- USD 33,000 plus interest; exact MZN figures not located [RESEARCH GAP] (PwC) |

### Test suite

**Test 1:** Contribution base MZN 30,000.00. -> Employee 900.00, Employer 1,200.00, Total 2,100.00. *(30,000 x 0.03 = 900; x 0.04 = 1,200; x 0.07 = 2,100 ✓)*

**Test 2:** Gross 25,000.00 incl. 5,000.00 meal subsidy. -> Base 20,000.00; Total INSS 1,400.00. *(20,000 x 0.07 = 1,400 ✓)*

**Test 3:** Resident annual taxable income 300,000.00. -> IRPS 49,500.00. *(300,000 x 0.20 - 10,500 = 49,500 ✓)*

**Test 4:** Resident annual taxable income 504,000.00. -> IRPS 88,500.00. *(504,000 x 0.25 - 37,500 = 88,500 ✓)*

**Test 5:** Resident annual taxable income 2,000,000.00. -> IRPS 498,460.00. *(2,000,000 x 0.32 - 141,540 = 498,460 ✓)*

**Test 6:** Non-resident Mozambique-source fee 100,000.00. -> 20% flat = 20,000.00. *(100,000 x 0.20 = 20,000 ✓)*

**Test 7:** Construction basic wage 8,000.00. -> Below 2025 minimum 8,400.00 (Decree 92/2025). STOP -- minimum-wage breach.

**Test 8:** Foreign employee claims exemption, no confirmed home scheme. -> Apply INSS 7%; exemption is by request only (PwC).

### Prohibitions

- NEVER compute INSS without an itemised pay breakdown -- the base excludes meal subsidies, one-off bonuses and reimbursements.
- NEVER assume an INSS floor or ceiling exists -- none was found in authoritative sources [RESEARCH GAP].
- NEVER treat an AT/IRPS debit as INSS, or vice versa -- they are separate obligations with different deadlines.
- NEVER apply progressive IRPS brackets to a non-resident -- they face a flat 20% definitive withholding.
- NEVER exclude INSS for a foreign employee without confirmed home-country-scheme exemption.
- NEVER compute payroll on a wage below the sector minimum -- validate against the 2025 decree table first.
- NEVER quantify INSS or IRPS penalties from this skill -- exact figures are unconfirmed [RESEARCH GAP]; escalate.
- NEVER ignore Law 11/2025 residency, digital-income, e-money or capital-gains changes -- flag to reviewer.
- NEVER present figures as definitive -- label as estimated and direct the client to their INSS statement and the AT.

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
