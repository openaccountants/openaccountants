---
name: uzbekistan-social-contributions
description: Use this skill whenever asked about Uzbekistan employer social tax (social insurance contributions), payroll withholding, personal income tax (PIT), or the Individual Accumulated Pension Fund (INPS) for employees and employers in the Republic of Uzbekistan. Trigger on phrases like "how much social tax do I pay in Uzbekistan", "Uzbek payroll tax", "social insurance contributions Uzbekistan", "INPS pension", "izhtimoiy soliq", "soliq.uz social tax", "12% social tax", "Uzbekistan PIT withholding", "do I withhold pension in Uzbekistan", "budget organisation social tax 25%", "Uzbek minimum wage payroll", or any question about employer/employee statutory contributions in Uzbekistan. Also trigger when classifying bank statement transactions that relate to Soliq (State Tax Committee) debits, social tax remittances, PIT withholding payments, or pension fund transfers from Uzbek banks (NBU, Ipoteka Bank, Asaka Bank, Kapitalbank, Hamkorbank, etc.). This skill covers employer social tax rates (12% private / 25% budget / 7% / 4.7% / 1% incentives), the flat 12% PIT, the 0.1% INPS carve-out, monthly reporting deadlines, residency rules, minimum wage and BCU, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Uzbekistan social-tax or payroll work.
version: 0.1
jurisdiction: UZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uzbekistan Social Tax & Payroll Contributions

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Uzbekistan |
| Primary Legislation | Tax Code of the Republic of Uzbekistan (Налоговый кодекс), as amended (social tax and PIT governed by the Tax Code) |
| Latest amendments | Adopted December 2025, effective 1 January 2026 (EY Uzbekistan Tax Alert, Jan 2026) |
| Tax Authority | State Tax Committee of the Republic of Uzbekistan (Soliq) — soliq.uz; Pension Fund under the Ministry of Economy and Finance |
| Employer social tax — private (non-budget) | 12% of gross payroll (PwC, reviewed 16 Jan 2026) |
| Employer social tax — budget (state-funded) organisations | 25% of gross payroll (PwC) |
| Employer social tax — organisations employing persons with disabilities | 4.7% of gross payroll (PwC) |
| Employer social tax — Assoc. "SOS Children's Villages of Uzbekistan" | 7% of gross payroll (PwC) |
| Employer social tax — time-limited incentives | 1% of gross payroll (sector/condition specific) (EY, Jan 2026) |
| Personal income tax (PIT) | Flat 12% on residents' employment income, rent, capital gains, most income (PwC) |
| INPS (Individual Accumulated Pension Fund) | 0.1% of employee gross — carved OUT of the 12% PIT, NOT an extra deduction (LegalAct.uz) |
| Social tax base | Gross payroll of local and foreign employees (PwC) |
| Social tax floor / ceiling | None published [RESEARCH GAP — reviewer to confirm against current Tax Code] |
| Reporting frequency | Monthly |
| Reporting/payment deadline | 15th day of the month following the reporting month (PwC) |
| Currency | UZS (Uzbekistani soum) only |
| Minimum wage | UZS 1,271,000/month from 1 Aug 2025 (WageCentre) [cross-check Presidential Decree] |
| Base Calculation Unit (BCU) | UZS 412,000 from 1 Aug 2025 (PwC significant developments) |
| Validated by | Pending — requires sign-off by a qualified Uzbek tax professional |
| Validation date | Pending |

**Employer social tax rate table (one rate applies per employer; rates are NOT additive)**

| Category | Who | Employer rate | Source |
| --- | --- | --- | --- |
| Other taxpayers (private / non-budget) | Standard commercial employers | 12% | PwC |
| Budget organisations | State-funded organisations | 25% | PwC |
| Organisations employing persons with disabilities | Qualifying employers | 4.7% | PwC |
| SOS Children's Villages of Uzbekistan | That specific association | 7% | PwC |
| Incentive (time-limited, sector/condition) | Cotton-textile/garment clusters, children's content producers, fruit/veg packaging, low-income-employee hirers, youth/vocational hires | 1% | EY (Jan 2026) |

- **Employer category rates mutual exclusivity** — These are mutually exclusive employer-category rates — an employer pays exactly one social tax rate on its gross payroll, not the sum of several. There is no "total" of these rows.

**Employee-side payroll (per employee, on gross income)**

| Item | Rate | Who bears it | Net effect | Source |
| --- | --- | --- | --- | --- |
| Personal income tax (PIT) | 12% | Employee (withheld by employer) | Reduces net pay | PwC |
| INPS pension allocation | 0.1% | Employee — carved OUT of the 12% PIT | Zero additional deduction | LegalAct.uz |
| **Total employee deduction** | **12%** | Employee | 12% of gross (the 0.1% INPS is part of the 12%, not added on top) | LegalAct.uz |

- **INPS is not additive to PIT** — CRITICAL: The 0.1% INPS is NOT 12% + 0.1% = 12.1%. The 0.1% is taken FROM WITHIN the 12% PIT and credited to the employee's individual cumulative pension account. Total employee deduction remains exactly 12%.  _(LegalAct.uz)_

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown employer category | Assume 12% (private / "other taxpayers") — most users are private businesses |
| Unknown whether INPS adds cost | Do NOT add 0.1% on top; net employee deduction stays 12% |
| Unknown contribution base cap | Assume NO ceiling on the social tax base; flag for reviewer |
| Unknown residency | Ask — residency determines PIT scope; do not assume |
| Foreign employee without residence permit | Generally exempt from INPS carve-out; PIT still applies — flag |
| Incentive 1% rate claimed | Do NOT apply without confirming the sector AND the time window; default to 12% |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Minimum viable -- employer category (private vs budget vs special) and each employee's monthly gross income in UZS. Without the employer category, STOP — the employer social tax rate cannot be selected.
- **Recommended inputs** — Recommended -- employee residency status, whether the employee is a foreign citizen with/without an Uzbek residence permit (affects INPS), and the reporting month.
- **Ideal inputs** — Ideal -- payroll register, prior-month cumulative year-to-date PIT figures (for the cumulative withholding method), Soliq monthly tax report, and confirmation of any claimed incentive social-tax rate with its statutory time window.

### Refusal catalogue

- **R-UZ-ST-1 -- Employer category unknown** — Trigger: employer category (private / budget / disability / SOS / incentive) not provided. Message: "The employer social tax rate depends on the employer category — 12% for private (non-budget) employers, 25% for budget organisations, 4.7% / 7% / 1% for special categories. Cannot compute social tax without confirming the category."
- **R-UZ-ST-2 -- Incentive 1% rate** — Trigger: client claims the 1% incentive social tax rate. Message: "The 1% social tax incentive is sector-specific AND time-limited (e.g., cotton-textile/garment clusters 1 Sep 2025–1 Sep 2028; children's content producers 1 Jul 2025–1 Jul 2030; fruit/veg packaging 1 May 2025–1 Jan 2028; low-income-employee hirers at >1.5x min wage 1 Jan 2025–1 Jan 2028; vocational students under 30 from 1 Sep 2024–1 Sep 2027). Confirm both the sector qualification and that the payroll month falls inside the window before applying. Escalate to a qualified Uzbek tax professional."
- **R-UZ-ST-3 -- Contribution base cap** — Trigger: client asks whether a floor or ceiling caps the social tax base. Message: "No statutory floor or ceiling on the social tax base was found in authoritative sources [RESEARCH GAP]. Do not assume a cap. Escalate to a qualified Uzbek tax professional to confirm against the current Tax Code."
- **R-UZ-ST-4 -- Penalty / arrears quantification** — Trigger: client has unpaid social tax or PIT and wants the penalty quantified. Message: "Late payment interest accrues at 1/300 of the Central Bank refinancing rate per day. Fixed-amount fines for late registration/understatement were not retrievable from authoritative sources [RESEARCH GAP]. Do not quantify arrears or fines without verifying the current Tax Code. Escalate to a qualified Uzbek tax professional."
- **R-UZ-ST-5 -- Non-resident / cross-border employment** — Trigger: employee is a non-resident or works partly outside Uzbekistan. Message: "Non-residents are taxed at 12% on most Uzbek-source income (10% dividends/interest, 6% freight/transport). Residency and treaty relief require case-specific confirmation. Escalate to a qualified Uzbek tax professional."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to social tax, PIT and pension. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Social tax and PIT remittances always EXCLUDE from any VAT return; they are statutory payroll obligations, not business supplies. Uzbek statements may be in Uzbek (Latin or Cyrillic) or Russian — both forms are listed.

### 3.1 Employer social tax remittances

**Employer social tax remittances patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IJTIMOIY SOLIQ, IZHTIMOIY SOLIQ | EXCLUDE -- employer social tax | "Social tax" in Uzbek |
| СОЦИАЛЬНЫЙ НАЛОГ, СОЦНАЛОГ | EXCLUDE -- employer social tax | "Social tax" in Russian |
| SOCIAL TAX, SOC TAX | EXCLUDE -- employer social tax | English reference |
| SOLIQ QO'MITASI, GNK, ГНК | EXCLUDE -- tax authority remittance | State Tax Committee |

### 3.2 PIT (personal income tax) withholding remittances

**PIT withholding remittance patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| JISMONIY SHAXSLAR DAROMAD SOLIG'I | EXCLUDE -- PIT withholding | "Personal income tax" in Uzbek |
| НДФЛ, НАЛОГ НА ДОХОДЫ ФИЗ ЛИЦ | EXCLUDE -- PIT withholding | PIT in Russian |
| PIT, INCOME TAX WITHHELD | EXCLUDE -- PIT withholding | English reference |

### 3.3 INPS / pension fund transfers

**INPS / pension fund transfer patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INPS, JAMG'ARMA PENSIYA | EXCLUDE -- pension allocation | Individual accumulated pension — funded from within PIT |
| ПЕНСИОННЫЙ ФОНД, ПЕНСИЯ | EXCLUDE -- pension fund | Russian reference |

### 3.4 Salary and payroll (exclude from social-tax classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OYLIK, ISH HAQI (outgoing) | EXCLUDE -- payroll/wages expense | Net salary to employees |
| ЗАРПЛАТА, ОКЛАД (outgoing) | EXCLUDE -- payroll expense | Russian reference |
| OYLIK, ЗАРПЛАТА (incoming) | EXCLUDE -- employment income received | Not a contribution payment |

### 3.5 Other tax payments (NOT social tax -- do not confuse)

**Other tax payment patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| QQS, НДС, VAT | EXCLUDE -- VAT, not social tax | 12% VAT remittance |
| FOYDA SOLIG'I, НАЛОГ НА ПРИБЫЛЬ | EXCLUDE -- corporate income tax | CIT, not social tax |
| AYLANMA SOLIG'I, turnover tax | EXCLUDE -- turnover tax | Simplified regime, not social tax |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical private (non-budget) Uzbek company employing resident staff. All figures in UZS. Employer social tax rate = 12% unless stated. PIT = 12% flat; INPS 0.1% is carved out of the PIT (no extra deduction).

### Example 1 -- Standard resident employee, gross UZS 5,000,000/month (private employer)

**Input line:**
`31.01.2025 ; OYLIK YANVAR ; DEBIT ; NET SALARY ; -4,400,000 ; UZS`

**Reasoning:**
Gross UZS 5,000,000. PIT = 12% × 5,000,000 = UZS 600,000. INPS = 0.1% × 5,000,000 = UZS 5,000, taken FROM WITHIN the 600,000 PIT (no extra deduction). Net pay = 5,000,000 − 600,000 = UZS 4,400,000. Separately, employer social tax = 12% × 5,000,000 = UZS 600,000 (employer cost, not deducted from the employee). Total employer cost = 5,000,000 + 600,000 = UZS 5,600,000.

**Classification:** Net salary debit EXCLUDE from VAT (payroll expense). PIT UZS 600,000 and social tax UZS 600,000 remitted to Soliq by 15 Feb 2025.

### Example 2 -- PIT withholding remittance (private employer)

**Input line:**
`14.02.2025 ; NDFL YANVAR ; DEBIT ; JISMONIY SHAXSLAR DAROMAD SOLIG'I ; -600,000 ; UZS`

**Reasoning:**
Matches PIT pattern (3.2). UZS 600,000 = 12% PIT on the UZS 5,000,000 gross from Example 1, withheld and remitted by the employer. Of this, UZS 5,000 (0.1%) is credited to the employee's INPS account; the remainder UZS 595,000 is general budget PIT. Paid before the 15 Feb deadline.

**Classification:** EXCLUDE from VAT. PIT withholding remittance.

### Example 3 -- Employer social tax remittance (private employer, 12%)

**Input line:**
`14.02.2025 ; IJTIMOIY SOLIQ YANVAR ; DEBIT ; SOCIAL TAX ; -600,000 ; UZS`

**Reasoning:**
Matches social tax pattern (3.1). UZS 600,000 = 12% × UZS 5,000,000 gross payroll. This is an employer cost, not withheld from the employee. Reported and paid monthly by the 15th.

**Classification:** EXCLUDE from VAT. Employer social tax (deductible business expense).

### Example 4 -- Budget (state-funded) organisation, gross UZS 4,000,000/month (25% social tax)

**Input line:**
`14.04.2025 ; СОЦНАЛОГ МАРТ ; DEBIT ; СОЦИАЛЬНЫЙ НАЛОГ ; -1,000,000 ; UZS`

**Reasoning:**
Budget organisation → social tax rate 25% (PwC). Gross UZS 4,000,000. Employer social tax = 25% × 4,000,000 = UZS 1,000,000. PIT on the employee = 12% × 4,000,000 = UZS 480,000; net pay = 4,000,000 − 480,000 = UZS 3,520,000. Total employer cost = 4,000,000 + 1,000,000 = UZS 5,000,000.

**Classification:** EXCLUDE from VAT. Budget-organisation social tax at 25%.

### Example 5 -- Cumulative year-to-date PIT (March remittance)

**Input lines (payroll YTD):**
`Jan–Feb cumulative gross: 10,000,000 ; Jan–Mar cumulative gross: 15,000,000 ; UZS`

**Reasoning:**
PIT is withheld cumulatively (LegalAct.uz): monthly PIT = YTD PIT to current month − YTD PIT to prior month. YTD PIT to March = 12% × 15,000,000 = UZS 1,800,000. YTD PIT to February = 12% × 10,000,000 = UZS 1,200,000. March PIT = 1,800,000 − 1,200,000 = UZS 600,000. (Here income is level UZS 5,000,000/month, so the cumulative method reconciles to a flat 12% per month.)

**Classification:** EXCLUDE from VAT. March PIT remittance UZS 600,000, due 15 Apr 2025.

### Example 6 -- Organisation employing persons with disabilities (4.7%), gross UZS 3,000,000/month

**Input line:**
`14.05.2025 ; IJTIMOIY SOLIQ APREL ; DEBIT ; SOCIAL TAX ; -141,000 ; UZS`

**Reasoning:**
Organisation employing persons with disabilities → social tax rate 4.7% (PwC). Gross UZS 3,000,000. Employer social tax = 4.7% × 3,000,000 = UZS 141,000. PIT on the employee = 12% × 3,000,000 = UZS 360,000; net pay = 3,000,000 − 360,000 = UZS 2,640,000.

**Classification:** EXCLUDE from VAT. Reduced 4.7% social tax. Confirm the organisation qualifies before applying the reduced rate (R-UZ-ST-2 logic).

## Section 5 -- Tier 1 rules

These rules apply when payroll/bank statement data is clear and all required inputs are available. Apply exactly as written. (Primary authority: PwC Worldwide Tax Summaries, reviewed 16 Jan 2026; INPS treatment per LegalAct.uz; 2026 changes per EY Jan 2026.)

### Rule 1 -- Employer social tax formula (one rate per employer)

- **Employer social tax formula** — Employer social tax = gross_payroll x rate rate = 12%   if private / "other taxpayers"            (PwC) rate = 25%   if budget (state-funded) organisation     (PwC) rate = 4.7%  if organisation employing persons w/ disabilities (PwC) rate = 7%    if SOS Children's Villages of Uzbekistan   (PwC) rate = 1%    if a qualifying time-limited incentive applies (EY)  _(PwC; EY)_
- **Social tax base** — The social tax base is gross payroll of local AND foreign employees, with no published floor or ceiling [RESEARCH GAP — confirm cap].

### Rule 2 -- PIT is a flat 12% (not progressive)

- **PIT flat rate rule** — Uzbekistan uses a FLAT 12% PIT on residents' employment income, rent, capital gains and most other income (PwC). There are no progressive bands. Resident dividends and interest are taxed at 5% (JSC dividends PIT-exempt 1 Apr 2022–31 Dec 2028).  _(PwC)_

### Rule 3 -- INPS is carved OUT of the 12% PIT

- **INPS carve-out rule** — The Individual Accumulated Pension Fund (INPS) contribution is 0.1% of employee gross income, deducted FROM the calculated 12% PIT (not added on top) and credited to the employee's individual cumulative pension account (LegalAct.uz). Net employee deduction = exactly 12%. Foreign citizens without an Uzbek residence permit are generally exempt from INPS.  _(LegalAct.uz)_

### Rule 4 -- Cumulative year-to-date PIT withholding

- **Cumulative YTD PIT formula** — monthly_PIT = PIT(Jan..current month, cumulative) - PIT(Jan..prior month, cumulative)  _(LegalAct.uz)_
- **Level income reconciliation** — With level monthly income, this reconciles to a flat 12% each month.

### Rule 5 -- Monthly reporting and payment

- **Monthly reporting and payment deadline** — Employers report and pay PIT, employer social tax, and the INPS allocation monthly, by the 15th day of the month following the reporting month (PwC). Payment is due the same date.  _(PwC)_

### Rule 6 -- Non-resident rates

- **Non-resident rates** — Non-residents: 12% on most Uzbek-source income (incl. employment and royalties); 10% on dividends/interest; 6% on freight/transport (PwC). Escalate cross-border cases (R-UZ-ST-5).  _(PwC)_

### Rule 7 -- Social tax is an employer cost, PIT is an employee cost

- **Cost bearer separation** — Employer social tax is borne by the employer and does NOT reduce the employee's net pay. PIT (12%, incl. the 0.1% INPS carve-out) is withheld from the employee. Never net these against each other.

### Rule 8 -- Tax residency

- **Tax residency rule** — Tax residency = 183+ days in any 12-month period beginning or ending in the tax year; or, if under 183 days, more days in Uzbekistan than in any other single country. Early residency election available with a long-term employment contract (PwC). Tax year = calendar year.  _(PwC)_

### Rule 9 -- Minimum wage and BCU

- **Minimum wage and BCU rule** — Minimum wage = UZS 1,271,000/month from 1 Aug 2025 (WageCentre) [cross-check Presidential Decree]. Base Calculation Unit (BCU) = UZS 412,000 from 1 Aug 2025 (PwC). The minimum wage and BCU are separate figures; BCU is used for fees, fines, state duties and certain thresholds — NOT directly as the social tax base.  _(WageCentre; PwC)_

### Rule 10 -- 2026 changes (confirmed)

- **2026 confirmed changes** — From 1 January 2026 (EY, PwC): fixed-amount PIT for individual entrepreneurs (IEs) is cancelled; IE turnover tax up to UZS 1 billion set at 1%; e-commerce CIT raised to 15% and e-commerce turnover tax to 4%; tax returns auto-prepared by the authority with a 5-business-day correction window. The 12% employer social tax and flat 12% PIT are unchanged into 2026 — but re-verify rates before each tax year (rates may be re-indexed annually).  _(EY; PwC)_

## Section 6 -- Tier 2 catalogue

When payroll/bank statement data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Employer category boundary (private vs budget)

- **Employer category boundary flag** — Trigger: Entity is partly state-funded, a quasi-government body, or a state enterprise operating commercially. Issue: The 12% (private) vs 25% (budget) distinction turns on whether the organisation is budget-financed. A misclassification more than doubles or halves the social tax. Action: Flag for reviewer. Confirm the budget-organisation status with Soliq before applying 12% or 25%.

### T2-2 -- Incentive 1% rate qualification and window

- **Incentive 1% rate qualification flag** — Trigger: Client claims the 1% social tax incentive (cotton-textile/garment, children's content, fruit/veg packaging, low-income-employee hirer, youth/vocational hire). Issue: Each incentive is sector-specific AND time-bounded; payroll months outside the window revert to 12%. Eligibility conditions (e.g., wages >1.5x minimum wage for low-income-employee hirers; students under 30) must be met. Action: Flag for reviewer. Do not apply 1% without confirming both the sector and the date window.

### T2-3 -- Foreign employees and INPS exemption

- **Foreign employee INPS exemption flag** — Trigger: Employer has foreign staff; unclear whether each holds an Uzbek residence permit. Issue: Foreign citizens without an Uzbek residence permit are generally exempt from the INPS carve-out (LegalAct.uz). PIT and employer social tax still apply on foreign-employee gross payroll. Residency also affects PIT scope. Action: Flag for reviewer. Confirm residence-permit status per employee.  _(LegalAct.uz)_

### T2-4 -- Contribution base cap

- **Contribution base cap flag** — Trigger: Very high salaries; client asks whether the social tax base is capped. Issue: No statutory floor/ceiling on the social tax base was found in authoritative sources [RESEARCH GAP]. Action: Flag for reviewer. Compute on full gross payroll unless a client-specific exemption is confirmed.

### T2-5 -- Annual individual PIT declaration

- **Annual individual PIT declaration flag** — Trigger: Resident has property/IP income, income from two or more sources, foreign income, or income from non-withholding sources. Issue: Such residents must file an annual PIT declaration in addition to employer withholding — filing by 1 April, payment by 1 June of the following year (PwC). Action: Flag for reviewer. Employer monthly withholding does not discharge the individual's annual filing obligation.  _(PwC)_

### T2-6 -- Expatriate departure return

- **Expatriate departure return flag** — Trigger: An expatriate employee is leaving Uzbekistan. Issue: Expatriates file a departure (exit) return — one month before departure (unless departing before 1 February) (PwC). Action: Flag for reviewer to confirm timing and final-period reconciliation.  _(PwC)_

## Section 7 -- Excel working paper template

When producing a payroll / social tax computation, structure the working paper as follows:

```
UZBEKISTAN PAYROLL & SOCIAL TAX -- WORKING PAPER
Client: [name]
Tax Year: [year]
Reporting month: [month]
Prepared: [date]

INPUT DATA
  Employer category:             [Private / Budget / Disability / SOS / Incentive]
  Employer social tax rate:      [12% / 25% / 4.7% / 7% / 1%]
  Incentive window confirmed:    [YES/NO/N/A]
  Employee gross income (UZS):   [____]
  Employee residency:            [Resident / Non-resident]
  Foreign w/o residence permit:  [YES/NO]  (affects INPS)

EMPLOYEE-SIDE (per employee)
  PIT rate:                      12%
  PIT (12% x gross):             UZS [____]
  of which INPS (0.1% x gross):  UZS [____]   (carved out of PIT — NOT extra)
  Net pay (gross - PIT):         UZS [____]

EMPLOYER-SIDE
  Social tax (rate x gross):     UZS [____]
  Total employer cost:           UZS [____]   (gross + social tax)

CUMULATIVE PIT CHECK (if mid-year)
  YTD PIT to current month:      UZS [____]
  YTD PIT to prior month:        UZS [____]
  Monthly PIT (difference):      UZS [____]

REMITTANCE
  PIT due (by 15th next month):       UZS [____]
  Social tax due (by 15th next month):UZS [____]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their tax impact]
```

## Section 8 -- Bank statement reading guide

### How social tax, PIT and pension remittances appear on Uzbek bank statements

Uzbek statements may be in Uzbek (Latin or Cyrillic) or Russian. Common banks: National Bank of Uzbekistan (NBU), Ipoteka Bank, Asaka Bank, Kapitalbank, Hamkorbank, Agrobank, Uzpromstroybank (SQB).

**Employer social tax:**
- Description: "IJTIMOIY SOLIQ", "СОЦИАЛЬНЫЙ НАЛОГ", "SOCIAL TAX", or to "SOLIQ QO'MITASI / ГНК"
- Timing: monthly, on or before the 15th of the following month
- Amount: employer rate (usually 12%) × gross payroll for the month

**PIT withholding:**
- Description: "JISMONIY SHAXSLAR DAROMAD SOLIG'I", "НДФЛ", "PIT"
- Timing: same monthly cycle, by the 15th
- Amount: 12% of monthly gross payroll (cumulative method)

**INPS / pension:**
- Description: "INPS", "JAMG'ARMA PENSIYA", "ПЕНСИОННЫЙ ФОНД"
- Note: the 0.1% is funded from within the PIT — it may appear as a sub-allocation, not a separate extra debit

**Key identification tips:**
1. Social tax and PIT remittances are always outgoing (DEBIT) to the tax authority.
2. They recur monthly with amounts proportional to payroll.
3. Do NOT confuse social tax with QQS/НДС (VAT 12%), FOYDA SOLIG'I (CIT 15%), or AYLANMA SOLIG'I (turnover tax).
4. Do NOT treat the 0.1% INPS as an additional 0.1% debit on top of the 12% PIT — it is inside the 12%.
5. Net salary debits (OYLIK / ЗАРПЛАТА) are payroll expense, not contribution remittances.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for tax-authority debits** — identify all outgoing payments matching Section 3 patterns (social tax, PIT, pension).
2. **Identify the employer category** — if a monthly tax-authority debit ≈ 12% of net-salary-implied gross, assume private (12%); if ≈ 25%, suspect a budget organisation. Flag for confirmation.
3. **Reverse-engineer gross payroll:**
   - If net salaries total X and PIT = 12% of gross, then gross ≈ net / 0.88 (since net = gross − 12% PIT).
   - Cross-check: employer social tax debit / employer rate should reconcile to the same gross.
4. **Flag for reviewer:** "Employer category and gross payroll derived from bank statement amounts only. Residency, foreign-employee status, and any incentive rate have not been independently verified. Reviewer must confirm before filing the Soliq monthly report."

## Section 10 -- Reference material

### Computation examples (private employer, 12% social tax, resident employee)

**Computation examples table**  _(PwC; LegalAct.uz; WageCentre)_

| Gross/month (UZS) | PIT 12% (UZS) | of which INPS 0.1% (UZS) | Net pay (UZS) | Employer social tax 12% (UZS) | Total employer cost (UZS) |
| --- | --- | --- | --- | --- | --- |
| 1,271,000 (min wage) | 152,520 | 1,271 | 1,118,480 | 152,520 | 1,423,520 |
| 3,000,000 | 360,000 | 3,000 | 2,640,000 | 360,000 | 3,360,000 |
| 5,000,000 | 600,000 | 5,000 | 4,400,000 | 600,000 | 5,600,000 |
| 10,000,000 | 1,200,000 | 10,000 | 8,800,000 | 1,200,000 | 11,200,000 |

*All derived from the flat 12% PIT and 12% employer social tax (PwC); INPS 0.1% carve-out per LegalAct.uz. Minimum wage UZS 1,271,000 from 1 Aug 2025 (WageCentre).*

### Other employer categories (social tax on gross UZS 4,000,000)

**Other employer categories table**  _(PwC; EY)_

| Category | Rate | Social tax (UZS) | Source |
| --- | --- | --- | --- |
| Private / other taxpayers | 12% | 480,000 | PwC |
| Budget organisation | 25% | 1,000,000 | PwC |
| SOS Children's Villages | 7% | 280,000 | PwC |
| Disability-employing org | 4.7% | 188,000 | PwC |
| Incentive (qualifying, time-limited) | 1% | 40,000 | EY |

### Key tax rates (context)

**Key tax rates table**  _(PwC)_

| Tax | Rate | Source |
| --- | --- | --- |
| Personal income tax (PIT) | 12% flat | PwC |
| PIT — resident dividends/interest | 5% | PwC |
| WHT — non-resident dividends/interest | 10% | PwC |
| WHT — non-resident other income | 12% (freight/transport 6%) | PwC |
| Corporate income tax (standard) | 15% (20% banks, cement, polyethylene, mobile operators, markets/malls) | PwC |
| VAT (standard) | 12% | PwC |
| Turnover (simplified) tax | generally 4% (turnover < UZS 1bn); IE 1% from 2026 | PwC |

### Thresholds

**Thresholds table**  _(PwC; WageCentre)_

| Threshold | Value | Source |
| --- | --- | --- |
| Tax residency | 183+ days in any 12-month period beginning/ending in the tax year; else more days in UZ than any other country | PwC |
| Turnover (simplified) eligibility | Annual turnover < UZS 1 billion | PwC |
| VAT/CIT base threshold | Turnover > UZS 1 billion → standard CIT (15%) + VAT (12%) | PwC |
| IE turnover tax 2026 | Up to UZS 1 billion at 1%; fixed-amount IE PIT cancelled | PwC |
| Minimum wage | UZS 1,271,000/month from 1 Aug 2025 [cross-check Decree] | WageCentre |
| Base Calculation Unit (BCU) | UZS 412,000 from 1 Aug 2025 | PwC |

### Forms and deadlines

**Forms and deadlines table**  _(PwC)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly tax report (PIT, Social Tax, INPS) | Employer reports/pays withheld PIT, employer social tax, INPS allocation | 15th of the month after the reporting month; payment same date | PwC |
| Annual individual PIT declaration | Residents with property/IP income, 2+ sources, foreign income, or non-withholding income | File by 1 April; pay by 1 June of the following year | PwC |
| Departure (exit) return | Expatriates leaving Uzbekistan | One month before departure (unless departing before 1 February) | PwC |

### Penalties

**Penalties table**  _(RemotePeople; UzDaily; PwC)_

| Item | Detail | Source |
| --- | --- | --- |
| Late payment interest (penya) | 1/300 of the Central Bank of Uzbekistan refinancing rate per day of delay | RemotePeople (secondary) |
| Late report grace | No fine for delays up to 5 days if filed on time over the prior 3 months; single consolidated fine across tax types (penalty-reduction reform) | UzDaily (secondary) |
| Fixed-amount fines (registration/understatement) | [RESEARCH GAP — reviewer to confirm against current Tax Code] | — |
| Statute of limitations | Three-year limitation period for tax assessment | PwC |

### Test suite

**Test 1:** Private employer, resident, gross UZS 5,000,000. → PIT = 600,000; net pay = 4,400,000; employer social tax (12%) = 600,000; total employer cost = 5,600,000.

**Test 2:** Private employer, resident, gross UZS 10,000,000. → PIT = 1,200,000; net pay = 8,800,000; employer social tax (12%) = 1,200,000; total employer cost = 11,200,000.

**Test 3:** Budget organisation, resident, gross UZS 4,000,000. → PIT = 480,000; net pay = 3,520,000; employer social tax (25%) = 1,000,000; total employer cost = 5,000,000.

**Test 4:** Disability-employing organisation, gross UZS 3,000,000. → PIT = 360,000; net pay = 2,640,000; employer social tax (4.7%) = 141,000.

**Test 5:** SOS Children's Villages, gross UZS 4,000,000. → employer social tax (7%) = 280,000.

**Test 6:** Minimum-wage employee, gross UZS 1,271,000 (private). → PIT = 152,520; net pay = 1,118,480; employer social tax (12%) = 152,520; total employer cost = 1,423,520.

**Test 7:** Cumulative PIT — YTD gross to March 15,000,000, YTD gross to Feb 10,000,000. → YTD PIT to Mar = 1,800,000; YTD PIT to Feb = 1,200,000; March PIT = 600,000.

**Test 8:** INPS treatment — gross UZS 5,000,000. → Total employee deduction = 12% = 600,000 (NOT 12.1%); INPS 5,000 is inside the 600,000, not on top.

**Test 9:** Foreign employee without residence permit, gross UZS 8,000,000 (private). → PIT 12% = 960,000 still applies; INPS carve-out generally does not (flag T2-3); employer social tax (12%) = 960,000.

### Prohibitions

- NEVER add the 0.1% INPS on top of the 12% PIT — total employee deduction is 12%, not 12.1%.
- NEVER apply the 25% budget rate to a private commercial employer, or the 12% private rate to a budget organisation, without confirming the category.
- NEVER apply the 1% incentive rate without confirming BOTH the qualifying sector AND the statutory time window.
- NEVER assume a floor or ceiling on the social tax base — none was found [RESEARCH GAP]; compute on full gross unless a confirmed exemption applies.
- NEVER net employer social tax against employee PIT — they are separate obligations borne by different parties.
- NEVER use progressive brackets for PIT — Uzbekistan PIT is a flat 12%.
- NEVER use data from EOR/payroll guides that reference "INCES", "INPS 4% Social Security", "0.5% Unemployment", or "Housing Loan Regime" — those are Venezuela's system, erroneously copied; they are WRONG for Uzbekistan.
- NEVER quantify penalties or arrears beyond the 1/300-refinancing-rate daily interest without verifying the current Tax Code — fixed fines are a [RESEARCH GAP].
- NEVER present figures as definitive — label as estimated and direct the client to Soliq (soliq.uz) and a qualified Uzbek tax professional.
- NEVER treat the BCU (UZS 412,000) as the social tax base — the base is gross payroll.

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
