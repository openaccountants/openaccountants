---
name: ethiopia-social-contributions
description: Use this skill whenever asked about Ethiopia payroll taxes, social security / pension contributions, or employment income tax (PAYE) for employees or employers. Trigger on phrases like "Ethiopia pension contribution", "POESSA", "how much PAYE in Ethiopia", "Ethiopian payroll tax", "employee pension deduction", "employer social security Ethiopia", "11% pension", "7% pension", "Ethiopia income tax bracket", "Birr salary tax", "net pay Ethiopia", "Proclamation 1395/2025", or any question about Ethiopian payroll/PAYE/pension obligations. Also trigger when classifying bank statement transactions that relate to POESSA pension remittances, Ministry of Revenue PAYE remittances, or salary debits from Commercial Bank of Ethiopia (CBE), Awash Bank, Dashen Bank, or other Ethiopian banks. This skill covers the post-July-2025 PAYE brackets, the 7%/11% pension split, contribution base, remittance deadlines, eligibility (citizens vs foreign nationals), bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Ethiopian payroll, PAYE, or pension work.
version: 0.1
jurisdiction: ET
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Social Security & Payroll Tax

## Ethiopia Social Security & Payroll Tax Skill v0.1

> **Reform note.** Ethiopia overhauled personal income taxation via the **Income Tax (Amendment) Proclamation No. 1395/2025** (approved by Parliament 17 July 2025; effective **7 July 2025**, with local withholding provisions effective 1 August 2025). Every PAYE figure in this skill reflects the post-reform regime. Source: Afriwise, "Update on Ethiopia's New Income Tax Amendment Proclamation"; PwC Worldwide Tax Summaries — Ethiopia (last reviewed 18 Dec 2025), https://taxsummaries.pwc.com/ethiopia/individual/taxes-on-personal-income.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Ethiopia (Federal Democratic Republic of Ethiopia) |
| Primary Legislation (PAYE) | Income Tax (Amendment) Proclamation No. 1395/2025 (amends Proclamation No. 979/2016) |
| Primary Legislation (pension) | Private Organisation Employees' Pension Proclamation (POESSA scheme) |
| Tax administration | Federal Tax Administration Proclamation No. 983/2016 (as amended) |
| Tax Authority | Ministry of Revenue (MoR), mor.gov.et |
| Pension Authority (private sector) | Private Organisation Employees Social Security Agency (POESSA) |
| Pension Authority (public sector) | Public Servants' Social Security Agency |
| Employee pension rate | 7% of basic salary [PwC, Other taxes] |
| Employer pension rate | 11% of basic salary [PwC, Other taxes] |
| Total pension rate | 18% of basic salary [PwC, Other taxes] |
| Contribution base | Basic salary (normal-hours basic pay), NOT total gross with allowances [PwC, Other taxes] |
| PAYE exemption threshold | First 2,000 ETB/month exempt [PwC; Proclamation 1395/2025] |
| PAYE top rate | 35% on monthly salary over 14,000 ETB [PwC; Proclamation 1395/2025] |
| Currency | Ethiopian Birr (ETB) only |
| Tax year | 8 July – 7 July (Ethiopian fiscal year; Hamle 1 – Sene 30) [PwC, Tax administration] |
| Validated by | Pending — requires sign-off by a licensed Ethiopian tax practitioner |
| Validation date | Pending |

**Who is covered by the pension scheme**  _(PwC, Other taxes)_

| Category | Pension status | Source |
| --- | --- | --- |
| Ethiopian citizens (private-org employees) | Mandatory | PwC, Other taxes |
| Foreign nationals of Ethiopian origin | Optional | PwC, Other taxes |
| Other (non-Ethiopian-origin) foreign nationals | Excluded — not available | PwC, Other taxes |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown citizenship / origin | STOP — pension eligibility depends on citizenship; do not deduct 7% without confirming the employee is an Ethiopian citizen or Ethiopian-origin foreign national who has opted in |
| Unknown contribution base | Use **basic salary**, not total gross; if only gross is known, flag for reviewer |
| Unknown whether allowances are part of "basic salary" | Treat allowances as OUTSIDE the pension base; flag for reviewer |
| Unknown public vs private sector | Assume private sector (POESSA); flag if employer is a government body |
| Unknown whether a debit is PAYE or pension | Classify by counterparty (MoR = PAYE; POESSA = pension); flag if reference is bare |
| Pension salary ceiling/floor | None found in authoritative sources — **[RESEARCH GAP — reviewer to confirm]**; compute on full basic salary and flag |

## Section 2 -- Rate and bracket tables

### 2.1 Pension contributions (the core of this skill)

**Pension contribution rate table**  _(PwC, Other taxes)_

| Party | Rate | Base | Source |
| --- | --- | --- | --- |
| Employee | 7% | Basic salary | PwC, Other taxes |
| Employer | 11% | Basic salary | PwC, Other taxes |
| **Total** | **18%** | Basic salary | PwC, Other taxes |

*Arithmetic check: 7% + 11% = 18%.*

- **Pension contribution base** — Base = basic salary (gross basic pay for normal working hours), explicitly NOT total gross including allowances  _(PwC, Other taxes)_
- **No statutory floor or ceiling on contributable salary** — No statutory floor or ceiling on contributable salary was found in authoritative sources (POESSA/PwC). [RESEARCH GAP — reviewer to confirm] whether any salary cap applies; do not assert one either way.  _(POESSA/PwC)_
- **Vesting period** — An employee must contribute at least 10 years to qualify for a retirement pension  _(PwC, Other taxes; 2merkato labour-law background)_
- **Remittance timing** — The employer deducts the employee's 7% and remits both contributions (18% total) within 30 days of the deduction / the last day of the salary month  _(PwC, Other taxes)_
- **Enforcement after non-payment** — If an employer fails to pay contributions for three months, the Social Security Agency may deduct arrears directly from the company's bank account  _(PwC, Other taxes)_

### 2.2 Employment income tax (PAYE) — monthly brackets (effective 7 July 2025)

**PAYE monthly brackets**  _(PwC; Proclamation 1395/2025)_

| Monthly salary (ETB) | Marginal rate | Source |
| --- | --- | --- |
| 0 – 2,000 | 0% (exempt) | PwC; Proclamation 1395/2025 |
| 2,001 – 4,000 | 15% | PwC; Proclamation 1395/2025 |
| 4,001 – 7,000 | 20% | PwC; Proclamation 1395/2025 |
| 7,001 – 10,000 | 25% | PwC; Proclamation 1395/2025 |
| 10,001 – 14,000 | 30% | PwC; Proclamation 1395/2025 |
| Over 14,000 | 35% | PwC; Proclamation 1395/2025 |

- **Minimum taxable income** — 2,000 ETB/month (was 600). Income at or below 2,000 ETB is fully exempt  _(PwC; Proclamation 1395/2025)_
- **Bracket structure change** — Brackets reduced from seven to six; lowest positive rate raised from 10% to 15%; top rate 35% now applies above 14,000 ETB/month (previously above 10,900 ETB)  _(PwC; PaySpace; MyWorkPay)_

### 2.3 PAYE quick-calculation (deduction) method — **DERIVED**

Ethiopian PAYE is conventionally computed as `tax = (monthly salary × rate) − deduction`. The deduction constants below are the **arithmetic equivalent** of the progressive brackets in 2.2. They were computed from the official rate/threshold structure and were **not** found stated verbatim on an authoritative page — **[RESEARCH GAP — reviewer to confirm against the official Ministry of Revenue schedule]**.

**PAYE quick-calc deduction table**  _(Derived — [RESEARCH GAP])_

| Monthly salary (ETB) | Rate | Deduction (derived) | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 – 2,000 | 0% | 0 | 0 |
| 2,001 – 4,000 | 15% | 300 | 300 |
| 4,001 – 7,000 | 20% | 500 | 900 |
| 7,001 – 10,000 | 25% | 850 | 1,650 |
| 10,001 – 14,000 | 30% | 1,350 | 2,850 |
| Over 14,000 | 35% | 2,050 | (open-ended) |

*Arithmetic self-check of the cumulative tax column (recomputed end-to-end):*
- At 4,000: 2,000 × 15% = 300. Quick-calc: 4,000 × 15% − 300 = 300. ✓
- At 7,000: 300 + 3,000 × 20% = 900. Quick-calc: 7,000 × 20% − 500 = 900. ✓
- At 10,000: 900 + 3,000 × 25% = 1,650. Quick-calc: 10,000 × 25% − 850 = 1,650. ✓
- At 14,000: 1,650 + 4,000 × 30% = 2,850. Quick-calc: 14,000 × 30% − 1,350 = 2,850. ✓
- Continuity into top band at 14,000: 14,000 × 35% − 2,050 = 2,850. ✓

## Section 3 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — employee citizenship/origin status and monthly basic salary. Without citizenship/origin status, STOP: pension eligibility (and therefore the 7% deduction) cannot be determined.

**Recommended** — full gross pay split into basic salary vs allowances, public vs private sector, and the salary month (Ethiopian-calendar offset matters for deadlines).

**Ideal** — POESSA registration confirmation, MoR PAYE registration confirmation, bank statements showing monthly pension and PAYE remittances, and the employer payroll register.

### Refusal catalogue

- **R-ET-1 -- Citizenship/origin unknown** — Trigger: employee citizenship or Ethiopian-origin status not provided. Message: "Pension eligibility depends on citizenship. The 7%/11% pension scheme is mandatory only for Ethiopian citizens, optional for foreign nationals of Ethiopian origin, and unavailable to other foreign nationals. Cannot apply the pension deduction without this information."  _(R-ET-1)_
- **R-ET-2 -- Pension salary cap** — Trigger: client asks whether a ceiling caps the contributable salary. Message: "No statutory pension floor or ceiling was found in authoritative sources. [RESEARCH GAP — reviewer to confirm] whether a cap applies before relying on an uncapped 18% computation. Escalate to a licensed Ethiopian practitioner."  _(R-ET-2)_
- **R-ET-3 -- Pension arrears / direct bank recovery** — Trigger: employer has unpaid contributions, especially three months or more. Message: "After three months of non-payment the Social Security Agency may deduct arrears directly from the company's bank account. Quantifying arrears (principal plus any charges) requires the POESSA statement. Escalate to a licensed practitioner."  _(R-ET-3)_
- **R-ET-4 -- PAYE penalties and interest** — Trigger: client asks the exact late-filing/late-payment penalty or interest figures. Message: "Exact income-tax penalty and interest rates could not be confirmed from a fully authoritative source. [RESEARCH GAP — reviewer to confirm] against Federal Tax Administration Proclamation No. 983/2016 (as amended) and the Ministry of Revenue. Do not quote a penalty figure as definitive."  _(R-ET-4)_
- **R-ET-5 -- Public-sector employees** — Trigger: employer is a government body / employee is a public servant. Message: "Public-sector pensions are administered by the Public Servants' Social Security Agency, not POESSA, and may use different rules. This skill covers the private-sector POESSA scheme. Escalate to a reviewer."  _(R-ET-5)_

## Section 4 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Ethiopian payroll. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Pension and PAYE remittances always EXCLUDE from any VAT return — they are statutory payroll obligations, not taxable supplies. Amharic terms may appear; common ones are noted.

### 4.1 Pension (POESSA) remittances

**Pension remittance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| POESSA | EXCLUDE — pension remittance | Private Organisation Employees Social Security Agency |
| PRIVATE ORGAN PENSION, PENSION CONTRIB | EXCLUDE — pension remittance | Employer + employee 18% |
| SOCIAL SECURITY AGENCY, SSA | EXCLUDE — pension remittance | POESSA or public-sector agency |
| PENSION 18%, PENSION 7%, PENSION 11% | EXCLUDE — pension remittance | Explicit split reference |
| ጡረታ (TIRETA = pension) | EXCLUDE — pension remittance | Amharic-language reference |

### 4.2 PAYE / employment income tax remittances

**PAYE remittance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MINISTRY OF REVENUE, MOR | EXCLUDE — PAYE remittance | Withheld employment income tax |
| PAYE, EMPLOYMENT INCOME TAX | EXCLUDE — PAYE remittance | Monthly withholding |
| ERCA, REVENUE AUTHORITY | EXCLUDE — PAYE remittance | Legacy / regional revenue references |
| የገቢ ግብር (YEGEBI GIBIR = income tax) | EXCLUDE — PAYE remittance | Amharic-language reference |

### 4.3 Salary and payroll (exclude from pension/PAYE classification)

**Salary/payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, NET PAY, ደመወዝ (DEMEWEZ = salary) (outgoing) | EXCLUDE — payroll expense | The net wage paid to staff, not a contribution |
| SALARY, NET PAY (incoming) | EXCLUDE — employment income received | Not a contribution |

### 4.4 Other taxes (NOT pension/PAYE — do not confuse)

**Other taxes pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| VAT, ተ.እ.ታ (VAT) | EXCLUDE from this skill | Output/input VAT, separate regime |
| WITHHOLDING 2%, WHT | EXCLUDE from this skill | Supplier withholding, not PAYE |
| PROFIT TAX, BUSINESS INCOME TAX | EXCLUDE from this skill | Corporate/business income tax |

## Section 5 -- Worked examples

Five bank-statement / payroll classifications for a hypothetical private-sector employer in Addis Ababa with Ethiopian-citizen employees. All figures recomputed end-to-end.

### Example 1 -- Mid-band employee: PAYE + pension on a 12,000 ETB basic salary

**Input line:**
`30 Hamle 2017 ; CBE ; SALARY RUN ; ABEBE T. BASIC 12,000 ; ETB`

**Reasoning (basic salary = 12,000 ETB, Ethiopian citizen):**
- PAYE band = 10,001–14,000 → 30%, deduction 1,350 (derived). PAYE = 12,000 × 30% − 1,350 = 3,600 − 1,350 = **2,550 ETB**.
- Employee pension = 12,000 × 7% = **840 ETB**.
- Employer pension = 12,000 × 11% = **1,320 ETB**.
- Net pay to employee = 12,000 − 2,550 (PAYE) − 840 (pension) = **8,610 ETB**.
- Total employer cost = 12,000 + 1,320 = **13,320 ETB**.
- Total pension remitted to POESSA = 840 + 1,320 = **2,160 ETB** (= 12,000 × 18%). ✓

**Classification:** Salary debit EXCLUDE from VAT (payroll). PAYE 2,550 remitted to MoR; pension 2,160 remitted to POESSA. Deadlines per Section 6.

### Example 2 -- POESSA pension remittance debit

**Input line:**
`05 Nehase 2017 ; AWASH BANK ; DEBIT ; POESSA PENSION CONTRIB HAMLE ; -2,160.00 ; ETB`

**Reasoning:**
Matches "POESSA" (pattern 4.1). Amount 2,160 ETB = 18% of a 12,000 ETB basic salary (840 employee + 1,320 employer), consistent with Example 1. This is the monthly pension remittance, due within 30 days of the salary month.

**Classification:** EXCLUDE from VAT — pension remittance to POESSA.

### Example 3 -- Ministry of Revenue PAYE remittance debit

**Input line:**
`28 Nehase 2017 ; DASHEN BANK ; DEBIT ; MINISTRY OF REVENUE PAYE HAMLE ; -2,550.00 ; ETB`

**Reasoning:**
Matches "MINISTRY OF REVENUE" / "PAYE" (pattern 4.2). Amount 2,550 ETB reconciles to the PAYE withheld in Example 1 (12,000 × 30% − 1,350). This is the monthly PAYE remittance, NOT a pension payment.

**Classification:** EXCLUDE from VAT — PAYE remittance to MoR. Do not classify as pension.

### Example 4 -- Exempt low earner (no PAYE)

**Input line:**
`30 Hamle 2017 ; CBE ; SALARY RUN ; KIDAN G. BASIC 2,000 ; ETB`

**Reasoning (basic salary = 2,000 ETB, Ethiopian citizen):**
- PAYE: salary is at the 2,000 ETB exemption threshold → **0 ETB PAYE** (band 0–2,000 is exempt).
- Employee pension = 2,000 × 7% = **140 ETB**.
- Employer pension = 2,000 × 11% = **220 ETB**.
- Net pay = 2,000 − 0 − 140 = **1,860 ETB**.
- Total pension to POESSA = 140 + 220 = **360 ETB** (= 2,000 × 18%). ✓

**Classification:** Salary debit EXCLUDE from VAT. No PAYE due. Pension 360 ETB still remitted — pension has no exemption threshold (note: no floor was found; [RESEARCH GAP — reviewer to confirm]).

### Example 5 -- Foreign (non-Ethiopian-origin) employee: no pension

**Input line:**
`30 Hamle 2017 ; CBE ; SALARY RUN ; J. SMITH (UK NATIONAL) BASIC 30,000 ; ETB`

**Reasoning (basic salary = 30,000 ETB, non-Ethiopian-origin foreign national):**
- Pension scheme is **not available** to non-Ethiopian-origin foreign nationals → employee pension = 0, employer pension = 0.
- PAYE: band = over 14,000 → 35%, deduction 2,050 (derived). PAYE = 30,000 × 35% − 2,050 = 10,500 − 2,050 = **8,450 ETB**.
- Net pay = 30,000 − 8,450 = **21,550 ETB** (no pension deduction).

**Classification:** Salary debit EXCLUDE from VAT. PAYE 8,450 ETB remitted to MoR. NO pension. Confirm nationality/origin before suppressing the pension deduction (R-ET-1).

## Section 6 -- Tier 1 rules

These rules apply when payroll/bank-statement data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 -- Pension formula

- **Pension formula** — employee_pension = basic_salary × 7% employer_pension = basic_salary × 11% total_pension    = basic_salary × 18% Base = basic salary, not total gross with allowances  _(PwC, Other taxes)_

### Rule 2 -- PAYE formula (quick-calc method)

- **PAYE formula** — PAYE = max(0, monthly_salary × rate − deduction) Rate and deduction come from the band the monthly salary falls in (Section 2.2 / 2.3). Deduction constants are derived — [RESEARCH GAP — reviewer to confirm against the official MoR schedule].  _(Section 2.2 / 2.3)_

### Rule 3 -- Exemption threshold

- **Exemption threshold** — The first 2,000 ETB/month is exempt. Salary at or below 2,000 ETB → 0 PAYE  _(PwC; Proclamation 1395/2025)_

### Rule 4 -- Pension eligibility by citizenship

- **Pension eligibility by citizenship** — Mandatory for Ethiopian citizens; optional for Ethiopian-origin foreign nationals; unavailable to other foreign nationals. Do not apply the 7%/11% deduction outside eligible categories.  _(PwC, Other taxes)_

### Rule 5 -- Pension base excludes allowances

- **Pension base excludes allowances** — Compute pension on basic salary only. Allowances are outside the base unless a reviewer confirms otherwise  _(PwC, Other taxes)_

### Rule 6 -- Remittance deadlines

**Remittance deadlines table**

| Obligation | Deadline | Source |
| --- | --- | --- |
| Pension (employee 7% + employer 11%) | Within 30 days of deduction / last day of salary month | PwC, Other taxes |
| PAYE | By the end of the month following the month income was earned | PwC, Tax administration |

Account for the Ethiopian-calendar offset (~7–8 days vs Gregorian) when mapping deadlines.

### Rule 7 -- Employee return-filing

- **Employee return-filing** — Employees with only employment income are NOT required to file a personal return; the employer's withholding and remittance discharges the obligation  _(PwC, Tax administration)_

### Rule 8 -- Vesting

- **Vesting** — A retirement pension requires at least 10 years of contributions. Do not promise a pension entitlement below 10 years.  _(PwC, Other taxes; 2merkato)_

### Rule 9 -- Enforcement after non-payment

- **Enforcement after non-payment** — After three months of unpaid contributions, the Social Security Agency may deduct arrears directly from the employer's bank account  _(PwC, Other taxes)_

### Rule 10 -- Tax year and statute of limitations

- **Tax year and statute of limitations** — Tax year = 8 July – 7 July. Authorities may assess within 5 years of the declaration filing date  _(PwC, Tax administration)_

## Section 7 -- Tier 2 catalogue

When payroll data is ambiguous or circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Basic salary vs total gross

- **T2-1 -- Basic salary vs total gross** — Trigger: only a single "salary" figure is given, with allowances bundled in. Issue: pension base is basic salary, not total gross; over-stating the base over-charges 18%. Action: request the basic/allowance split; flag for reviewer.

### T2-2 -- Ethiopian-origin foreign national opt-in

- **T2-2 -- Ethiopian-origin foreign national opt-in** — Trigger: employee is a foreign national of Ethiopian origin. Issue: pension is optional, not automatic; deducting 7% without an opt-in election is wrong. Action: confirm the election; flag for reviewer.

### T2-3 -- Pension salary cap

- **T2-3 -- Pension salary cap** — Trigger: high earner where a ceiling could matter. Issue: no statutory cap was found — [RESEARCH GAP — reviewer to confirm]. Action: compute uncapped and flag; do not assert a cap exists or does not.

### T2-4 -- Pension arrears / direct bank recovery

- **T2-4 -- Pension arrears / direct bank recovery** — Trigger: unpaid contributions, especially ≥ three months. Issue: the agency may seize from the company bank account; arrears quantum needs a POESSA statement. Action: escalate; do not estimate.

### T2-5 -- Public vs private sector

- **T2-5 -- Public vs private sector** — Trigger: employer is a government body. Issue: the Public Servants' Social Security Agency, not POESSA, applies. Action: flag; this skill covers private sector only.

### T2-6 -- PAYE penalties and interest

- **T2-6 -- PAYE penalties and interest** — Trigger: late filing/payment. Issue: exact penalty/interest figures unconfirmed — [RESEARCH GAP — reviewer to confirm against Proclamation 983/2016]. Action: do not quote definitive figures; escalate. (A 2025 tax-penalty-waiver directive also exists — LexAfrica, May 2025 — and may affect relief.)

## Section 8 -- Excel working paper template

When producing an Ethiopian payroll computation, structure the working paper as follows:

```
ETHIOPIA PAYROLL COMPUTATION -- WORKING PAPER
Employer: [name]              Tax Year: [8 Jul YYYY – 7 Jul YYYY]
Employee: [name]              Salary month: [Ethiopian + Gregorian]
Prepared: [date]

INPUT DATA
  Citizenship / origin:          [Ethiopian citizen / Ethiopian-origin foreign / Other foreign]
  Pension eligible:              [Mandatory / Optional-opted-in / Excluded]
  Sector:                        [Private (POESSA) / Public]
  Basic salary (ETB):            [____]
  Allowances (ETB, excl. base):  [____]
  Total gross (ETB):             [____]

PAYE COMPUTATION (quick-calc, DERIVED deductions)
  Band / rate:                   [____ %]
  Deduction constant:            [____]   (derived — reviewer to confirm)
  PAYE = gross × rate − deduction: ETB [____]   (floor at 0)

PENSION COMPUTATION (base = basic salary)
  Employee 7%:                   ETB [____]
  Employer 11%:                  ETB [____]
  Total 18% to POESSA:           ETB [____]

NET PAY
  Net pay = basic+allow − PAYE − employee 7%: ETB [____]
  Total employer cost = gross + employer 11%: ETB [____]

REMITTANCE
  PAYE to MoR — due:             [end of following month]
  Pension to POESSA — due:       [within 30 days of salary month]

REVIEWER FLAGS / RESEARCH GAPS
  [List Tier 2 flags and any [RESEARCH GAP] items here]
```

## Section 9 -- Bank statement reading guide

### How payroll obligations appear on Ethiopian bank statements

**Commercial Bank of Ethiopia (CBE):**
- Salary run: "SALARY", "NET PAY", or Amharic "ደመወዝ"
- Pension remittance: "POESSA", "PENSION CONTRIB"
- PAYE remittance: "MINISTRY OF REVENUE", "PAYE"

**Awash Bank / Dashen Bank / Bank of Abyssinia:**
- Similar references; pension debits often carry "PENSION" or "POESSA"; PAYE debits carry "MOR" or "REVENUE"

**Key identification tips:**
1. Pension and PAYE remittances are always outgoing (DEBIT).
2. A pension remittance should equal 18% of total contributable basic salaries for the month (7% employee + 11% employer).
3. A PAYE remittance equals the sum of withheld employee tax for the month.
4. Dates use the Ethiopian calendar (Hamle, Nehase, Meskerem …) — convert before testing against Gregorian deadlines.
5. Do not confuse pension (POESSA) with PAYE (MoR), or either with VAT / supplier withholding.

## Section 10 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for salary, POESSA, and MoR debits** matching Section 4 patterns.
2. **Reconcile pension:** for each month, pension debit ÷ 18% ≈ total contributable basic salary; employee share = that ÷ 18% × 7%, employer share × 11%.
3. **Reconcile PAYE:** PAYE debit should equal the sum of `gross × rate − deduction` across employees (Section 2.3).
4. **Flag eligibility unknowns:** "Pension applied assuming all staff are Ethiopian citizens. Citizenship/origin not independently verified — reviewer must confirm before relying on the 7%/11% split."
5. **Flag every [RESEARCH GAP]:** derived PAYE deductions, pension cap, and penalty figures are unconfirmed.

## Section 11 -- Reference material

### Calculation examples (post-July-2025 regime; ETB, monthly)

**Calculation examples table**

| Basic salary | Band / rate | PAYE (gross×rate−ded.) | Employee 7% | Employer 11% | Net pay (citizen) |
| --- | --- | --- | --- | --- | --- |
| 2,000 | 0% | 0 | 140 | 220 | 1,860 |
| 4,000 | 15% (ded. 300) | 300 | 280 | 440 | 3,420 |
| 7,000 | 20% (ded. 500) | 900 | 490 | 770 | 5,610 |
| 10,000 | 25% (ded. 850) | 1,650 | 700 | 1,100 | 7,650 |
| 14,000 | 30% (ded. 1,350) | 2,850 | 980 | 1,540 | 10,170 |
| 30,000 | 35% (ded. 2,050) | 8,450 | 2,100 | 3,300 | 19,450 |

*Net pay = basic − PAYE − employee 7%. Recomputed: 4,000 − 300 − 280 = 3,420 ✓; 7,000 − 900 − 490 = 5,610 ✓; 10,000 − 1,650 − 700 = 7,650 ✓; 14,000 − 2,850 − 980 = 10,170 ✓; 30,000 − 8,450 − 2,100 = 19,450 ✓. PAYE deductions are DERIVED — reviewer to confirm.*

### Related thresholds & business taxes (context only)

**Related thresholds and business taxes table**

| Item | Value | Source |
| --- | --- | --- |
| VAT registration threshold | Taxable supplies > 2,000,000 ETB / 12 months | VAT Proclamation No. 1341/2024 + Reg. 570/2025 (Hulunem; Haymanot Belay) |
| Business income Category A | Annual gross income ≥ 2,000,000 ETB | Afriwise (Proclamation 1395/2025) |
| Business income Category B | Below 2,000,000 ETB (excl. companies/SOEs/book-keepers) | Afriwise (Proclamation 1395/2025) |
| Minimum Alternative Tax (MAT) | ≥ 2.5% of annual turnover if computed income tax falls below; creditable up to 5 years | Afriwise (Proclamation 1395/2025) |
| Cash-payment restriction | 50,000 ETB/day cash limit; admin penalties on breach | Afriwise (Proclamation 1395/2025) |

### Minimum wage

- **No national/private-sector statutory minimum wage** in Ethiopia; private pay is set by contract and collective bargaining. A national assessment is underway but not enacted [RemotePeople; minimum-wage.org].
- Public-sector reference only: minimum government salary raised to **6,000 ETB/month** (~Sept 2025); entry-level bachelor's-degree starting salary raised to 11,500 ETB [BirrMetrics]. Not applicable to private-sector PAYE/pension.

### Penalties — **PARTIALLY CONFIRMED, [RESEARCH GAP — reviewer to confirm]**

**Penalties table**

| Item | Indicative (UNVERIFIED) | Source / status |
| --- | --- | --- |
| Late filing | ~1,000 ETB per month (or part) late, plus interest | Secondary sources only — **[RESEARCH GAP]**; verify vs Proclamation 983/2016 |
| Late payment | Interest on unpaid tax; possible suspension of tax clearance | Secondary — **[RESEARCH GAP]** |
| Fraud | Criminal sanctions | Secondary — **[RESEARCH GAP]** |
| 2025 penalty waiver directive | Relief program exists | LexAfrica, May 2025 |
| Pension non-payment (3 months) | Direct bank-account deduction of arrears | PwC, Other taxes (confirmed) |

### Test suite

**Test 1:** Citizen, basic 12,000 ETB. → PAYE = 12,000×30% − 1,350 = **2,550**. Employee 7% = **840**. Employer 11% = **1,320**. Pension total = **2,160**. Net = **8,610**.

**Test 2:** Citizen, basic 2,000 ETB. → PAYE = **0** (exempt band). Employee 7% = **140**. Employer 11% = **220**. Net = **1,860**.

**Test 3:** Citizen, basic 7,000 ETB. → PAYE = 7,000×20% − 500 = **900**. Employee 7% = **490**. Employer 11% = **770**. Net = **5,610**.

**Test 4:** Citizen, basic 30,000 ETB. → PAYE = 30,000×35% − 2,050 = **8,450**. Employee 7% = **2,100**. Employer 11% = **3,300**. Net = **19,450**.

**Test 5:** Non-Ethiopian-origin foreign national, basic 30,000 ETB. → Pension EXCLUDED (0 / 0). PAYE = **8,450**. Net = **21,550**.

**Test 6:** Citizen, basic 4,000 ETB. → PAYE = 4,000×15% − 300 = **300**. Employee 7% = **280**. Employer 11% = **440**. Net = **3,420**.

**Test 7:** Employer fails to remit pension for 3 months. → Social Security Agency may deduct arrears directly from the company bank account; escalate (R-ET-3).

**Test 8:** Employee with only employment income asks if they must file a return. → No; employer withholding discharges the obligation (Rule 7).

### Prohibitions

- NEVER apply the 7%/11% pension deduction without confirming the employee is an Ethiopian citizen (or Ethiopian-origin foreign national who opted in).
- NEVER compute pension on total gross including allowances — the base is basic salary.
- NEVER assert a pension salary cap (or its absence) as fact — it is a [RESEARCH GAP].
- NEVER present the derived PAYE deduction constants as officially published — they are arithmetic derivations pending MoR confirmation.
- NEVER quote an exact PAYE penalty/interest figure as definitive — those figures are unconfirmed.
- NEVER apply the old (pre-July-2025) seven-band schedule or the 600 ETB threshold — they are superseded by Proclamation 1395/2025.
- NEVER tell a low earner they pay no pension because PAYE is zero — PAYE exemption ≠ pension exemption.
- NEVER map Ethiopian-calendar dates to Gregorian deadlines without converting the ~7–8 day offset.
- NEVER conflate POESSA pension remittances with MoR PAYE remittances on a bank statement.
- NEVER promise a retirement pension entitlement below 10 years of contributions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. This skill is Tier 2 (research-verified) and not yet accountant-verified; several figures are flagged [RESEARCH GAP — reviewer to confirm].

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
