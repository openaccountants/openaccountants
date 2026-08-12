---
name: north-macedonia-social-contributions
description: Use this skill whenever asked about North Macedonia (Republic of North Macedonia, MK) compulsory social security contributions and the related payroll/personal income tax mechanics for 2025. Trigger on phrases like "Macedonia social contributions", "Macedonia payroll tax", "PIOM contribution", "FZOM health contribution", "how much social security do I pay in Macedonia", "Macedonia gross to net salary", "MPIN form", "Macedonia minimum wage contributions", "Macedonia pension contribution rate", "denar payroll", "Macedonia flat tax 10%", "Macedonia personal allowance", "Macedonia contribution ceiling", or any question about an employer withholding/remitting contributions in North Macedonia. Also trigger when classifying bank-statement transactions that relate to UJP (Public Revenue Office) payroll debits, PIOM/FZOM remittances, or social-contribution transfers from Komercijalna Banka, Stopanska Banka, NLB Banka or other Macedonian banks. This skill covers the 28% total employee-borne contribution rate, the four constituent funds, the min/max monthly contribution bases, the flat 10% personal income tax and personal allowance, the MPIN integrated monthly filing, gross-to-net computation, bank-statement classification, and edge cases. ALWAYS read this skill before touching any North Macedonia payroll or social-contribution work.
version: 0.1
jurisdiction: MK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Macedonia Compulsory Social Contributions & Payroll

## North Macedonia Compulsory Social Contributions & Payroll Skill v0.1

> **Confidence: HIGH.** Rate, base and threshold figures rest on the KPMG Tax Card 2025, Eurofast Tax Card 2025, PwC Worldwide Tax Summaries, and Bloomberg Tax's report of the Public Revenue Office (UJP) announcement of 22 January 2025. The official UJP page (ujp.gov.mk) was confirmed for procedural deadlines but did not itself yield the rate tables. English statute names are working translations.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | North Macedonia (Republic of North Macedonia) |
| Currency | MKD (Macedonian denar). EUR conversions approximate at EUR 1 ≈ MKD 61.5 (denar pegged) |
| Primary Legislation | Law on Contributions from Compulsory Social Insurance (Закон за придонеси од задолжително социјално осигурување) [KPMG Tax Card 2025] |
| Supporting Legislation | Law on Personal Income Tax (Закон за данок на личен доход), flat 10% effective 1 Jan 2023 [PwC; KPMG] |
| Tax / Collection Authority | Public Revenue Office (Управа за јавни приходи / UJP) — https://www.ujp.gov.mk/en [UJP] |
| Policy owner | Ministry of Finance (https://finance.gov.mk/en-GB) [Ministry of Finance] |
| Funds | Pension & Disability Insurance Fund (PIOM); Health Insurance Fund (FZOM); Employment Service Agency [KPMG Tax Card 2025] |
| Total compulsory social contribution rate (2025) | **28.0% of gross salary** — fully employee-borne [KPMG Tax Card 2025; Eurofast Tax Card 2025] |
| Employer additional contribution | **0% — none.** Employer only calculates, withholds and remits [Eurofast Tax Card 2025; KPMG] |
| Minimum monthly contribution base (2025) | MKD 31,577 (= 50% of MKD 63,154 average salary) [UJP via Bloomberg Tax, 22 Jan 2025] |
| Maximum monthly contribution base, employees (2025) | MKD 1,010,464 (~EUR 16,430) [UJP via Bloomberg Tax; KPMG] |
| Maximum monthly contribution base, self-employed (2025) | MKD 757,848 [UJP via Bloomberg Tax] |
| Reference average monthly salary (2025) | MKD 63,154 (State Statistical Office) [UJP via Bloomberg Tax; KPMG] |
| Personal income tax | Flat 10% on employment income, after contributions and allowance [PwC; KPMG] |
| Monthly PIT personal allowance (2025) | MKD 10,270 (MKD 123,240/year) [Eurofast & KPMG Tax Cards 2025] |
| Minimum gross monthly wage (from Mar 2025) | MKD 36,037 gross (MKD 24,379 net) [Law office Pepeljugoski, citing Official Gazette / Ministry of Labour and Social Policy, 28 Mar 2025] |
| Payroll reporting form | MPIN (Месечна пресметка за интегрирана наплата / Monthly Calculation for Integrated Payment) [UJP; PwC] |
| Reporting deadline | MPIN calculation submitted electronically by the 10th of the month for the prior month [UJP; PwC] |
| Payment deadline | On salary payment date; or by the 15th of the current month for the prior month if salary unpaid [UJP] |
| Validated by | Pending — requires sign-off by a North Macedonia tax professional |
| Validation date | Pending |

**Contribution composition (2025) — all employee-borne:**

**Contribution composition (2025) — all employee-borne**

| Fund / contribution | Rate | Employer-side | Source |
| --- | --- | --- | --- |
| Pension & disability insurance (PIOM) | 18.8% | 0% | KPMG Tax Card 2025; PwC |
| Health insurance (FZOM) | 7.5% | 0% | KPMG Tax Card 2025; PwC |
| Employment / unemployment insurance | 1.2% | 0% | KPMG Tax Card 2025; Eurofast |
| Additional health insurance (work injury / occupational accidents) | 0.5% | 0% | KPMG Tax Card 2025; PwC |
| **TOTAL compulsory social contributions** | **28.0%** | **0%** | KPMG; Eurofast |

*Arithmetic check: 18.8 + 7.5 + 1.2 + 0.5 = 28.0%. Employer column: 0 + 0 + 0 + 0 = 0%.*

> **Labelling caveat.** The 0.5% line is called "additional health insurance" by PwC and Eurofast; KPMG labels it "additional health insurance contributions in case of accidents at work and work-related injuries"; one secondary summary (Mondaq) mislabels it "Disability Fund". The 0.5% rate and the 28.0% total are consistent across all sources [PwC; Eurofast; KPMG].

- **Pension & disability insurance (PIOM)** — 18.8%  _(KPMG Tax Card 2025; PwC)_
- **Health insurance (FZOM)** — 7.5%  _(KPMG Tax Card 2025; PwC)_
- **Employment / unemployment insurance** — 1.2%  _(KPMG Tax Card 2025; Eurofast)_
- **Additional health insurance (work injury / occupational accidents)** — 0.5%  _(KPMG Tax Card 2025; PwC)_
- ****TOTAL compulsory social contributions**** — **28.0%**  _(KPMG; Eurofast)_
- **Minimum monthly contribution base (2025)** — MKD 31,577 (= 50% of MKD 63,154 average salary)  _(UJP via Bloomberg Tax, 22 Jan 2025)_
- **Maximum monthly contribution base, employees (2025)** — MKD 1,010,464 (~EUR 16,430)  _(UJP via Bloomberg Tax; KPMG)_
- **Maximum monthly contribution base, self-employed (2025)** — MKD 757,848  _(UJP via Bloomberg Tax)_
- **Monthly PIT personal allowance (2025)** — MKD 10,270 (MKD 123,240/year)  _(Eurofast & KPMG Tax Cards 2025)_
- **Personal income tax** — Flat 10% on employment income, after contributions and allowance  _(PwC; KPMG)_
- **Minimum gross monthly wage (from Mar 2025)** — MKD 36,037 gross (MKD 24,379 net)  _(Law office Pepeljugoski, citing Official Gazette / Ministry of Labour and Social Policy, 28 Mar 2025)_

## Section 2 -- Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown total social contribution rate | Use 28.0% of gross salary [KPMG Tax Card 2025] |
| Unknown who bears the contribution | Treat all 28% as employee-borne; employer 0% additional [Eurofast; KPMG] |
| Gross salary below the contribution floor | Apply contribution base floor MKD 31,577/month [UJP via Bloomberg Tax] |
| Gross salary above the employee ceiling | Cap contribution base at MKD 1,010,464/month [UJP via Bloomberg Tax] |
| Unknown personal allowance | Apply MKD 10,270/month [Eurofast & KPMG Tax Cards 2025] |
| Unknown PIT rate | Apply flat 10% [PwC; KPMG] |
| Self-employed contribution ceiling | Apply MKD 757,848/month, NOT the employee ceiling [UJP via Bloomberg Tax] |
| Penalty amounts requested | Do not quantify — penalties follow statutory formulas; escalate (see Section 6 / 10) |

## Section 3 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — gross monthly salary in MKD and confirmation the worker is an employee (Class: employment income). Without a gross figure, STOP. Do not compute contributions from a net figure unless you reverse-engineer it explicitly and flag it.

**Recommended** — pay period/month, whether the salary is at or below the minimum wage, whether the worker is full-time, and whether the personal allowance applies in full (a single employer applies the full monthly allowance).

**Ideal** — the MPIN calculation for the month, the employment contract, and bank statements showing the net salary payment plus the UJP remittance of contributions and PIT.

### Refusal catalogue

- **R-MK-SSC-1 -- Self-employed / sole trader contributions** — Trigger: worker is self-employed (трговец поединец / sole proprietor) rather than an employee. Message: "Self-employed contribution bases and the annual self-employed return (due 15 March, settlement 30 June) follow a different ceiling (MKD 757,848/month) and advance-payment regime. Confirm the regime with a North Macedonia tax professional before computing."  _(UJP via Bloomberg Tax; PwC)_
- **R-MK-SSC-2 -- Penalty / arrears quantification** — Trigger: client asks for the exact fine for late or missing MPIN/contribution filing. Message: "Penalty amounts for payroll/contribution non-compliance follow case-by-case statutory formulas under the General Tax Procedure Law; the illustrative figures in this skill are drawn from the VAT misdemeanour scale and are NOT contribution-specific. Escalate to a North Macedonia tax professional." [RESEARCH GAP — reviewer to confirm exact misdemeanour fines for late MPIN/contribution filing against the current statute]  _(KPMG; PwC)_
- **R-MK-SSC-3 -- Expat / cross-border / posted workers** — Trigger: worker is a non-resident, posted worker, or covered by a totalisation/social-security agreement. Message: "Residency (worldwide vs Macedonia-sourced) and totalisation-agreement coverage change the contribution and PIT outcome materially. Residents are taxed on worldwide income; non-residents only on Macedonia-sourced income. Escalate to a North Macedonia tax professional."  _(PwC)_
- **R-MK-SSC-4 -- Pillar Two / corporate top-up tax** — Trigger: client asks how the 15% minimum tax interacts with payroll. Message: "The Pillar Two domestic minimum top-up tax of 15% for in-scope MNE groups (Official Gazette No. 3/2025, effective 1 Jan 2025) is a corporate-level tax and does not change employee social contributions or the flat 10% PIT. Escalate corporate-tax questions to a North Macedonia tax professional."  _(KPMG; Mondaq)_

## Section 4 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to North Macedonia payroll and social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Social-contribution and PIT remittances are statutory obligations — EXCLUDE them from any VAT classification. For an employer client they are payroll costs (the gross salary is the expense; the withholdings are part of gross, not an additional cost).

### 4.1 UJP / contribution & PIT remittances (outgoing)

**4.1 UJP / contribution & PIT remittances (outgoing)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UJP, УЈП, UPRAVA ZA JAVNI PRIHODI | EXCLUDE — UJP remittance | Public Revenue Office: contributions and/or PIT |
| MPIN, ИНТЕГРИРАНА НАПЛАТА | EXCLUDE — integrated payroll remittance | Integrated monthly contribution + PIT payment |
| PRIDONESI, ПРИДОНЕСИ | EXCLUDE — social contributions | "Contributions" |
| PIOM, ПИОМ, PENZISKO | EXCLUDE — pension contribution | Pension & Disability Insurance Fund |
| FZOM, ФЗОМ, ZDRAVSTVENO | EXCLUDE — health contribution | Health Insurance Fund |
| DANOK NA LICEN DOHOD, ДЛД, PIT | EXCLUDE — personal income tax withheld | Flat 10% PIT remittance |

### 4.2 Remittances appearing on specific Macedonian banks

**4.2 Remittances appearing on specific Macedonian banks**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Komercijalna Banka | "UJP" / "PRIDONESI I DANOK" | EXCLUDE — UJP remittance |
| Stopanska Banka | "UPRAVA ZA JAVNI PRIHODI" / "MPIN" | EXCLUDE — UJP remittance |
| NLB Banka | "UJP DANOK" / "PRIDONESI" | EXCLUDE — UJP remittance |
| Halkbank / ProCredit | "UJP" / "ПРИДОНЕСИ" | EXCLUDE — UJP remittance |

### 4.3 Net salary payments (outgoing — payroll, not a contribution)

**4.3 Net salary payments (outgoing — payroll, not a contribution)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLATA, ПЛАТА, NET SALARY (outgoing) | EXCLUDE — net wage payment | Net pay to employee; gross is the expense |
| ZARABOTKA, ЗАРАБОТКА (outgoing) | EXCLUDE — wage payment | Same |

### 4.4 Salary received (incoming — not a contribution)

**4.4 Salary received (incoming — not a contribution)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLATA, ПЛАТА (incoming) | EXCLUDE — net employment income received | Already net of withholdings |

### 4.5 Pension / benefit received (incoming — not a contribution)

**4.5 Pension / benefit received (incoming — not a contribution)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENZIJA, ПЕНЗИЈА | EXCLUDE — pension income received | Benefit, not a contribution paid |

## Section 5 -- Worked examples

Six gross-to-net / bank-statement classifications for a hypothetical North Macedonian employer and its staff. All figures in MKD for 2025. PIT base = gross − 28% contributions (on the contribution base) − MKD 10,270 personal allowance; PIT = 10% of that base [PwC; Rivermate]. Contributions and PIT computed on the contribution base, which is clamped to the floor/ceiling.

### Example 1 -- Average-salary employee (gross MKD 63,154)

**Input line:**
`25.04.2025 ; PLATA APRIL 2025 ; DEBIT ; NET SALARY ; -41,950.79 ; MKD`

**Reasoning:**
Gross MKD 63,154 is between the floor (31,577) and ceiling (1,010,464), so the full gross is the contribution base.
- Contributions 28% × 63,154 = **MKD 17,683.12** (PIOM 18.8% = 11,872.95; FZOM 7.5% = 4,736.55; employment 1.2% = 757.85; add'l health 0.5% = 315.77; check: 11,872.95 + 4,736.55 + 757.85 + 315.77 = 17,683.12).
- PIT base = 63,154 − 17,683.12 − 10,270 = **MKD 35,200.88**.
- PIT = 10% × 35,200.88 = **MKD 3,520.09**.
- Net pay = 63,154 − 17,683.12 − 3,520.09 = **MKD 41,950.79**. Matches the statement line.

**Classification:** EXCLUDE — net salary payment. The MKD 17,683.12 contributions + MKD 3,520.09 PIT are remitted to UJP via MPIN.

### Example 2 -- Minimum-wage employee (gross MKD 36,037)

**Input line:**
`25.05.2025 ; ПЛАТА МАЈ ; DEBIT ; PLATA ; -24,379.00 ; MKD`

**Reasoning:**
Gross MKD 36,037 (the March-2025 statutory minimum gross wage) is above the floor, so the full gross is the contribution base.
- Contributions 28% × 36,037 = **MKD 10,090.36**.
- PIT base = 36,037 − 10,090.36 − 10,270 = **MKD 15,676.64**.
- PIT = 10% × 15,676.64 = **MKD 1,567.66**.
- Net = 36,037 − 10,090.36 − 1,567.66 = **MKD 24,378.98 ≈ MKD 24,379**, which reconciles to the published net minimum wage [Pepeljugoski].

**Classification:** EXCLUDE — net minimum-wage payment.

### Example 3 -- UJP integrated remittance (outgoing, employer)

**Input line:**
`10.05.2025 ; UPRAVA ZA JAVNI PRIHODI ; DEBIT ; MPIN APR 2025 PRIDONESI I ДЛД ; -21,203.21 ; MKD`

**Reasoning:**
Matches "UPRAVA ZA JAVNI PRIHODI" / "MPIN" (patterns 4.1–4.2). For the Example-1 employee this is contributions 17,683.12 + PIT 3,520.09 = MKD 21,203.21, paid to UJP. EXCLUDE from VAT. For the employer this is part of the gross-salary cost already recognised, not an additional expense.

**Classification:** EXCLUDE — UJP contribution + PIT remittance.

### Example 4 -- High earner below the ceiling (gross MKD 200,000)

**Input line:**
`25.06.2025 ; PLATA JUNE ; DEBIT ; NET SALARY DIRECTOR ; -135,193.00 ; MKD`

**Reasoning:**
Gross MKD 200,000 < ceiling 1,010,464, so the full gross is the contribution base.
- Contributions 28% × 200,000 = **MKD 56,000.00**.
- PIT base = 200,000 − 56,000 − 10,270 = **MKD 133,730.00**.
- PIT = 10% × 133,730 = **MKD 13,373.00**.
- Net = 200,000 − 56,000 − 13,373 = **MKD 130,627.00**.

*Note: the statement shows -135,193, which does NOT reconcile to the computed net of 130,627.* Flag for reviewer — the bank line may exclude a separate deduction or use a different allowance treatment. Do not assume the statement is authoritative.

**Classification:** EXCLUDE from VAT — net salary. FLAG: net per statement (135,193) ≠ computed net (130,627); reconcile before filing.

### Example 5 -- Earner above the employee ceiling (gross MKD 1,200,000)

**Input line:**
`25.07.2025 ; ПЛАТА ЈУЛИ CEO ; DEBIT ; NET ; -826,390.07 ; MKD`

**Reasoning:**
Gross MKD 1,200,000 > ceiling 1,010,464. Contributions are computed on the capped base, NOT on gross.
- Contribution base = MKD 1,010,464 (ceiling).
- Contributions 28% × 1,010,464 = **MKD 282,929.92** (PIOM 18.8% = 189,967.23; FZOM 7.5% = 75,784.80; employment 1.2% = 12,125.57; add'l health 0.5% = 5,052.32; check sum = 282,929.92).
- PIT base = 1,200,000 − 282,929.92 − 10,270 = **MKD 906,800.08**.
- PIT = 10% × 906,800.08 = **MKD 90,680.01**.
- Net = 1,200,000 − 282,929.92 − 90,680.01 = **MKD 826,390.07**. Matches the statement line.

**Classification:** EXCLUDE — net salary. Contributions capped at the MKD 1,010,464 base; no contributions on the MKD 189,536 of gross above the ceiling.

### Example 6 -- Pension received (incoming — not a contribution)

**Input line:**
`05.05.2025 ; ПЕНЗИЈА МАЈ ; CREDIT ; PIOM ; +28,400.00 ; MKD`

**Reasoning:**
Matches "ПЕНЗИЈА" / "PIOM" (pattern 4.5). This is a pension benefit RECEIVED, not a contribution paid. Do not confuse inbound PIOM credits with outbound contribution remittances. EXCLUDE from VAT.

**Classification:** EXCLUDE — pension income received. NOT a contribution.

## Section 6 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written. All figures 2025.

### Rule 1 -- Total contribution formula

- **Total contribution formula** — contribution_base = clamp(gross_salary, MKD 31,577, MKD 1,010,464)   # employees, monthly total_contributions = contribution_base × 28.0% Floor MKD 31,577 and ceiling MKD 1,010,464 per month. Self-employed ceiling is MKD 757,848.  _(UJP via Bloomberg Tax)_

### Rule 2 -- Contribution composition

- **Contribution composition** — PIOM 18.8% + FZOM 7.5% + employment 1.2% + additional health 0.5% = 28.0%. Each fund is computed on the same contribution base.  _(KPMG Tax Card 2025; PwC)_

### Rule 3 -- All contributions are employee-borne; employer 0%

- **All contributions are employee-borne; employer 0%** — The full 28% is legally borne by the employee/insured and deducted from gross salary. The employer makes NO additional employer-side contribution — it only calculates, withholds and remits.  _(Eurofast Tax Card 2025: "Employers are not required to make additional contributions"; KPMG)_

### Rule 4 -- PIT is a flat 10%

- **PIT is a flat 10%** — Personal income tax is a flat 10% on employment and most other income, effective 1 Jan 2023 (the earlier 10%/18% progressive schedule was repealed).  _(PwC; KPMG)_

### Rule 5 -- PIT base formula

- **PIT base formula** — PIT_base = gross_salary − total_contributions − monthly_personal_allowance PIT = PIT_base × 10% net_pay = gross_salary − total_contributions − PIT Monthly personal allowance MKD 10,270 (MKD 123,240/year), applied by the employer in monthly withholding.  _(Eurofast & KPMG Tax Cards 2025; PwC; Rivermate)_

### Rule 6 -- Contribution base floor

- **Contribution base floor** — If gross salary is below MKD 31,577/month, contributions are still due on the MKD 31,577 floor (= 50% of the MKD 63,154 average salary). Note the statutory minimum gross wage (MKD 36,037 from March 2025) is above this floor, so a full-time minimum-wage employee contributes on actual gross [Pepeljugoski].  _(UJP via Bloomberg Tax)_

### Rule 7 -- Contribution base ceiling

- **Contribution base ceiling** — No contributions are due on monthly salary above MKD 1,010,464 (employees). PIT, however, applies to the full PIT base with no upper cap.  _(UJP via Bloomberg Tax; KPMG)_

### Rule 8 -- MPIN integrated filing

- **MPIN integrated filing** — Payroll is reported via the MPIN integrated monthly filing to the UJP — gross salaries, contributions per fund, personal allowance, PIT base and withheld PIT per employee. The calculation is submitted electronically by the 10th of the following month.  _(UJP; PwC; Rivermate)_

### Rule 9 -- Payment timing

- **Payment timing** — Contributions and withheld PIT are payable on the salary payment date; or by the 15th of the current month for the prior month if salary is unpaid.  _(UJP, ujp.gov.mk)_

### Rule 10 -- Annual PIT return is pre-filled

- **Annual PIT return is pre-filled** — The UJP prepares a pre-filled annual PIT return: it delivers a draft by 30 April and the taxpayer confirms/corrects by 31 May, otherwise the draft is deemed confirmed.  _(PwC)_

### Rule 11 -- Residency scope

- **Residency scope** — Residents are taxed on worldwide income; non-residents only on Macedonia-sourced income.  _(PwC)_

## Section 7 -- Tier 2 catalogue (reviewer judgement)

When payroll data is ambiguous or circumstances are unclear, flag these for reviewer confirmation.

### T2-1 -- Multiple employers and the personal allowance

**Trigger:** worker has more than one employer in the same month.

**Issue:** the MKD 10,270 monthly personal allowance is applied once. If two employers each apply it, PIT is under-withheld and an annual adjustment is needed.

**Action:** flag for reviewer; confirm which employer applies the allowance.

### T2-2 -- Self-employed vs employee classification

**Trigger:** worker may be a sole trader (трговец поединец) rather than an employee.

**Issue:** the self-employed ceiling (MKD 757,848) and the annual return / advance-payment regime differ from employee payroll.

**Action:** flag for reviewer (see R-MK-SSC-1).

### T2-3 -- Salary at or below the contribution floor

**Trigger:** part-time or partial-month gross below MKD 31,577.

**Issue:** contributions are due on the floor, not the lower actual gross, which can make net pay disproportionately low. Pro-rating rules for partial months need confirmation.

**Action:** flag for reviewer. [RESEARCH GAP — reviewer to confirm partial-month / part-time floor pro-rating]

### T2-4 -- Ceiling-basis discrepancy between sources

**Trigger:** reconciling the ceiling against a multiplier.

**Issue:** PwC/Eurofast describe the maximum base as 16× average salary; KPMG describes the 2025 pension ceiling as 12× average. Both nonetheless arrive at the published MKD 1,010,464/month, so the binding number is reliable but the stated multiplier basis differs.

**Action:** use the published figure MKD 1,010,464; flag the multiplier basis for reviewer if a derivation is needed.

### T2-5 -- Penalty / arrears exposure

**Trigger:** late or missing MPIN filings or contribution payments.

**Issue:** fines follow statutory formulas under the General Tax Procedure Law; interest on late payment accrues.

**Action:** do not quantify; escalate (see R-MK-SSC-2).

### T2-6 -- Non-resident / posted / treaty-covered workers

**Trigger:** cross-border worker.

**Issue:** residency and totalisation coverage change both contributions and PIT.

**Action:** flag for reviewer (see R-MK-SSC-3).

## Section 8 -- Excel working paper template

When producing a North Macedonia payroll computation, structure the working paper as follows:

```
NORTH MACEDONIA PAYROLL COMPUTATION -- WORKING PAPER
Client / Employer: [name]
Employee:          [name]
Month / Year:      [month] 2025
Prepared:          [date]
Currency:          MKD

INPUT DATA
  Gross monthly salary:            MKD [____]
  Worker type:                     [Employee / Self-employed]
  Full personal allowance applies: [YES/NO]   (single employer = YES)

CONTRIBUTION BASE
  Floor (2025):                    MKD 31,577
  Ceiling, employees (2025):       MKD 1,010,464
  Contribution base = clamp(gross, floor, ceiling):  MKD [____]

CONTRIBUTIONS (on contribution base)
  PIOM pension & disability  18.8%:  MKD [____]
  FZOM health                 7.5%:  MKD [____]
  Employment / unemployment   1.2%:  MKD [____]
  Additional health           0.5%:  MKD [____]
  TOTAL contributions        28.0%:  MKD [____]   (check = sum of four lines)

PERSONAL INCOME TAX
  Personal allowance (monthly):    MKD 10,270
  PIT base = gross − contributions − allowance:  MKD [____]
  PIT @ 10%:                       MKD [____]

NET PAY
  Net = gross − contributions − PIT:  MKD [____]

UJP REMITTANCE (MPIN)
  Contributions + PIT remitted:    MKD [____]
  MPIN due (10th of next month):   [date]
  Payment due (salary date):       [date]

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 9 -- Bank statement reading guide

### How payroll items appear on North Macedonian bank statements

**Komercijalna Banka:**
- Outgoing UJP remittance: "UJP", "PRIDONESI I DANOK", "MPIN"
- Net salary: "PLATA", "ПЛАТА"
- Timing: net salary around month-end; UJP remittance on the salary payment date / by the 15th

**Stopanska Banka:**
- Outgoing UJP remittance: "UPRAVA ZA JAVNI PRIHODI", "MPIN"
- Net salary: "ЗАРАБОТКА" / "PLATA"

**NLB Banka:**
- Outgoing UJP remittance: "UJP DANOK", "PRIDONESI"
- Net salary: "PLATA"

**Key identification tips:**
1. Contribution/PIT remittances are always outgoing (DEBIT) to UJP — never credits.
2. Net salary payments are also outgoing but go to the employee, not to UJP.
3. Inbound "ПЕНЗИЈА" / "PIOM" credits are pension benefits received, not contributions paid — do not confuse.
4. The UJP remittance ≈ 28% of contribution base + 10% PIT; the net salary ≈ gross − that remittance.
5. Macedonian-language references (придонеси = contributions, данок = tax, плата = salary, пензија = pension) are common alongside Latin transliterations.

## Section 10 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for UJP debits** — identify all outgoing payments matching Section 4 patterns (UJP / MPIN / PRIDONESI).
2. **Scan for net salary debits** — identify "PLATA" / "ЗАРАБОТКА" outgoing payments.
3. **Reverse-engineer gross (approximate):** for a single-employer employee with the full allowance, net ≈ gross − 28%·gross − 10%·(gross − 28%·gross − 10,270) within the base limits. Solve for gross only as an estimate.
4. **Sanity-check against thresholds:** a full-time worker should not net below ~MKD 24,379 (the 2025 minimum net wage).
5. **Flag for reviewer:** "Payroll figures derived from bank-statement amounts only. Gross salary, allowance application, and worker classification have not been independently verified. Reviewer must confirm before filing MPIN."

## Section 11 -- Reference material

### Gross-to-net reference table (2025, single employer, full allowance)

**Gross-to-net reference table (2025, single employer, full allowance)**

| Gross MKD/month | Contribution base | Contributions 28% | PIT base | PIT 10% | Net pay | Source basis |
| --- | --- | --- | --- | --- | --- | --- |
| 36,037 (min wage) | 36,037 | 10,090.36 | 15,676.64 | 1,567.66 | 24,378.98 | [Pepeljugoski; KPMG; Eurofast] |
| 63,154 (avg salary) | 63,154 | 17,683.12 | 35,200.88 | 3,520.09 | 41,950.79 | [UJP via Bloomberg Tax; KPMG] |
| 100,000 | 100,000 | 28,000.00 | 61,730.00 | 6,173.00 | 65,827.00 | [KPMG; Eurofast] |
| 200,000 | 200,000 | 56,000.00 | 133,730.00 | 13,373.00 | 130,627.00 | [KPMG; Eurofast] |
| 1,200,000 (above ceiling) | 1,010,464 | 282,929.92 | 906,800.08 | 90,680.01 | 826,390.07 | [UJP via Bloomberg Tax; KPMG] |

### Thresholds (2025)

**Thresholds (2025)**

| Item | Value | Basis | Source |
| --- | --- | --- | --- |
| Minimum monthly contribution base | MKD 31,577 | 50% of MKD 63,154 average salary | UJP via Bloomberg Tax |
| Maximum monthly contribution base, employees | MKD 1,010,464 | 16× average (PwC/Eurofast) / 12× pension ceiling (KPMG) — both → same figure | UJP via Bloomberg Tax; PwC; KPMG |
| Maximum monthly contribution base, self-employed | MKD 757,848 | 12× average salary | UJP via Bloomberg Tax |
| PIT personal allowance (monthly / annual) | MKD 10,270 / MKD 123,240 | Standard salaried personal allowance | Eurofast & KPMG Tax Cards 2025 |
| Reference average monthly salary | MKD 63,154 | State Statistical Office 2025 | UJP via Bloomberg Tax; KPMG |
| Minimum gross monthly wage (from Mar 2025) | MKD 36,037 (net 24,379) | Official Gazette / Ministry of Labour | Pepeljugoski |

### Rate brackets / other taxes (2025)

**Rate brackets / other taxes (2025)**

| Type | Rate | Note | Source |
| --- | --- | --- | --- |
| Personal income tax (employment & most income) | 10% flat | Effective 1 Jan 2023; replaced 10%/18% progressive | PwC; KPMG |
| Capital gains on securities/shares held > 2 years | 0% | Exempt if held over 2 years | PwC |
| Games of chance | 15% | n/a | PwC |
| Corporate income tax | 10% flat | Pillar Two 15% minimum top-up for in-scope MNE groups from 1 Jan 2025 (Official Gazette 3/2025) | KPMG; Mondaq |

### Forms

**Forms**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| MPIN (Месечна пресметка за интегрирана наплата / Monthly Calculation for Integrated Payment) | Monthly payroll report: gross, contributions per fund, allowance, PIT base, withheld PIT per employee; integrated single filing for contributions + PIT | Calculation submitted electronically by the 10th of the following month; payment on salary date or by the 15th of the current month for the prior month if salary unpaid | UJP; PwC; Rivermate |
| Annual personal income tax return (pre-filled) | UJP prepares a pre-filled annual return; taxpayer confirms or corrects | UJP delivers draft by 30 April; taxpayer confirms/corrects by 31 May; if no response the draft is deemed confirmed | PwC |
| Self-employed annual accounts & return | Annual accounts and return for self-employed keeping records; monthly advance = 1/12 of prior-year tax | Annual return by 15 March; final settlement by 30 June | PwC |

### Penalties (illustrative — NOT contribution-specific)

**Penalties (illustrative — NOT contribution-specific)**

| Type | Amount | Note | Source |
| --- | --- | --- | --- |
| Late / failure to submit return | ~EUR 1,500 (company) + EUR 500 (responsible person) for delayed submission; ~EUR 2,500 + EUR 1,000 for failure to submit | Drawn from the VAT misdemeanour scale; comparable misdemeanour fines apply to payroll/contribution non-compliance | KPMG Tax Card 2025 via Mondaq |
| Tax assessment after rejected calculation/return | Payment due within 15 days of delivery of the assessment; late-payment interest accrues per the General Tax Procedure Law | Procedural | PwC |

> [RESEARCH GAP — reviewer to confirm] The exact statutory misdemeanour fines for late or missing MPIN/contribution filing. The figures above are the VAT-scale illustration from the KPMG card, not contribution-specific.

### Sources

- PwC Worldwide Tax Summaries — North Macedonia, Individual: Other taxes — https://taxsummaries.pwc.com/north-macedonia/individual/other-taxes
- PwC Worldwide Tax Summaries — North Macedonia, Individual: Taxes on personal income — https://taxsummaries.pwc.com/north-macedonia/individual/taxes-on-personal-income
- PwC Worldwide Tax Summaries — North Macedonia, Individual: Tax administration — https://taxsummaries.pwc.com/north-macedonia/individual/tax-administration
- KPMG DOOEL Skopje — North Macedonia Tax Card 2025 — https://assets.kpmg.com/content/dam/kpmg/al/pdf/Tax%20Card%202025%20(2).pdf
- Mondaq / KPMG — North Macedonia Tax Card 2025 (summary) — https://www.mondaq.com/tax-authorities/1583146/north-macedonia-tax-card-2025
- Eurofast — North Macedonia Tax Card 2025 — https://eurofast.eu/wp-content/uploads/2025/02/NorthMacedoniaTaxCard2025-2.pdf
- Bloomberg Tax — North Macedonia Tax Agency Clarifies 2025 Wage Thresholds (reporting the UJP announcement, 22 Jan 2025) — https://news.bloombergtax.com/payroll/north-macedonia-tax-agency-clarifies-2025-wage-thresholds-for-calculating-social-security-contributions
- Public Revenue Office (UJP), North Macedonia — contributions guidance — https://www.ujp.gov.mk/en/vodic/category/707
- Law office Pepeljugoski — Increased minimum salary for 2025 (citing Official Gazette / Ministry of Labour and Social Policy) — https://pepeljugoski.com.mk/en/2025/05/05/increased-minimum-salary-for-2025/

### Test suite

**Test 1:** Gross MKD 63,154 (average salary), single employer, full allowance. → Contributions = 17,683.12; PIT base = 35,200.88; PIT = 3,520.09; Net = 41,950.79.

**Test 2:** Gross MKD 36,037 (minimum wage). → Contributions = 10,090.36; PIT base = 15,676.64; PIT = 1,567.66; Net = 24,378.98 (≈ published net minimum MKD 24,379).

**Test 3:** Gross MKD 100,000. → Contributions = 28,000.00; PIT base = 61,730.00; PIT = 6,173.00; Net = 65,827.00.

**Test 4:** Gross MKD 200,000. → Contributions = 56,000.00; PIT base = 133,730.00; PIT = 13,373.00; Net = 130,627.00.

**Test 5:** Gross MKD 1,200,000 (above employee ceiling). → Contribution base capped at 1,010,464; Contributions = 282,929.92; PIT base = 906,800.08; PIT = 90,680.01; Net = 826,390.07.

**Test 6:** Gross MKD 25,000 (below floor). → Contribution base = floor 31,577; Contributions = 8,841.56; PIT base = 25,000 − 8,841.56 − 10,270 = 5,888.44; PIT = 588.84; Net = 25,000 − 8,841.56 − 588.84 = 15,569.60. (Flag T2-3: contributions on floor, not actual gross.)

**Test 7:** Composition check on MKD 1,010,464 base. → PIOM 189,967.23 + FZOM 75,784.80 + employment 12,125.57 + add'l health 5,052.32 = 282,929.92 = 28% × 1,010,464. ✓

**Test 8:** Employer additional contribution on any gross. → MKD 0. Employer only withholds and remits.

### Prohibitions

- NEVER treat any part of the 28% as an employer-side cost — in North Macedonia the full 28% is employee-borne; the employer's additional contribution is 0%.
- NEVER compute contributions on actual gross below the floor — use the MKD 31,577 floor (employees).
- NEVER compute contributions on gross above the ceiling — cap the base at MKD 1,010,464 (employees) / MKD 757,848 (self-employed).
- NEVER apply a progressive PIT schedule — PIT is a flat 10% since 1 Jan 2023.
- NEVER omit the MKD 10,270 monthly personal allowance from the PIT base for a single-employer employee.
- NEVER apply the personal allowance twice across multiple employers (flag T2-1).
- NEVER quantify penalties from the illustrative VAT-scale figures — escalate.
- NEVER confuse inbound PIOM/pension credits with outbound contribution remittances.
- NEVER present figures as definitive — label as estimated and direct the client to their MPIN / UJP records, pending sign-off by a North Macedonia tax professional.

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
