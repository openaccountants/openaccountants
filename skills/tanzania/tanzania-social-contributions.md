---
name: tanzania-social-contributions
description: Use this skill whenever asked about Tanzania (Mainland) payroll taxes and social security contributions for employers and employees. Trigger on phrases like "Tanzania PAYE", "how much NSSF do I pay", "NSSF contribution", "PSSSF", "Skills and Development Levy", "SDL Tanzania", "Workers Compensation Fund", "WCF Tanzania", "TZS payroll", "Tanzania payroll deductions", "PAYE bracket Tanzania", "social security Tanzania", "pension contribution Tanzania", or any question about Tanzanian employer/employee statutory contributions. Also trigger when classifying bank statement transactions that relate to TRA payments, NSSF/PSSSF pension debits, SDL, or WCF remittances from CRDB, NMB, NBC, or other Tanzanian banks. This skill covers PAYE progressive brackets, NSSF/PSSSF pension splits, SDL, WCF, monthly remittance deadlines, penalties, minimum wage, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Tanzanian payroll or contributions work.
jurisdiction: TZ
tax_year: 2026
last_updated: 2026-07-13
authored_by: Baraka Cassian, CPA, CA, CTA
reviewed_by: Baraka Cassian
review_status: current
trust_label: Checked by Baraka Cassian
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania (Mainland) Social Security & Payroll Contributions

## Tanzania (Mainland) Social Security & Payroll Contributions Skill v0.1

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Baraka Cassian** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### tanzania-social-contributions

- **NSSF - total contribution (private sector)** — 20% of employee's monthly wages (joint employer/employee)  _(NSSF Act, Cap 50, s.13)_
- **NSSF - split** — Employee share capped at 10% of monthly wage; standard splits 10% employer / 10% employee, or 15% / 5%  _(NSSF Act, Cap 50, s.13)_
- **NSSF - payment deadline** — Within one month after the end of the month to which the contribution relates  _(NSSF Act, Cap 50, s.14)_
- **NSSF - late payment penalty** — 5% of the unpaid amount for each month or part of a month after the due date  _(NSSF Act, Cap 50, ss.14-15)_
- **NSSF - registration** — Employers must register with NSSF and register all employees (membership mandatory for private-sector employees)  _(NSSF Act, Cap 50)_
- **PSSSF - public service scheme** — 20% of salary: employer 15% / employee 5%  _(Public Service Social Security Fund Act No. 2 of 2018 (Cap 371 RE 2023), Part IV - contributions)_
- **WCF - tariff rate** — 0.5% of cash sums paid to employees - both private and public sector employers  _(Workers Compensation Act, Cap 263; Tariff Regulations)_
- **WCF - payment deadline** — Monthly; payable within the contribution month or not later than the end of the following month  _(Workers Compensation (Payment of Tariff) Regulations)_
- **WCF - late payment interest** — 2% of the unpaid amount per month of delay  _(WCF regulations/notices)_
- **SDL - cross reference** — 3.5% of gross emoluments, employers with 10+ employees, monthly by the 7th (see tanzania-payroll sheet)  _(VETA Act, Cap 82 (as amended by Finance Act 2023))_
- **HESLB - employer deduction** — 15% of monthly salary of each loan beneficiary; remit by the 15th day of the following month  _(HESLB Act, Cap 178)_
- **HESLB - employer penalty** — 10% of the monthly deduction amount for failure to deduct/remit on time  _(HESLB Act, Cap 178)_
- **NHIF - public service** — 6% of basic salary: 3% employer / 3% employee (mandatory for public servants)  _(National Health Insurance Fund Act, Cap 395)_
- **Employer statutory on-cost (private sector summary)** — NSSF 10% + SDL 3.5% + WCF 0.5% = 14% of gross payroll (SDL-liable employers, 10/10 NSSF split)  _(Derived)_
- **Employee statutory deductions (typical)** — NSSF 10% of wages + PAYE per bands (+ 15% HESLB if loan beneficiary)  _(Derived)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | United Republic of Tanzania (Mainland — see Zanzibar note) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Primary Legislation (PAYE) | Income Tax Act, Cap. 332 |
| Pension Legislation (private) | National Social Security Fund Act, Cap. 50 |
| Pension Legislation (public) | Public Service Social Security Act, 2018 |
| Levy Legislation | Vocational Education and Training Act (SDL); Workers Compensation Act (WCF) |
| Tax Authority | Tanzania Revenue Authority (TRA) |
| Pension funds | NSSF (private/informal sector); PSSSF (public sector) |
| Personal income tax? | YES — Tanzania has PAYE (this is NOT a no-PIT jurisdiction) |
| Resident PAYE rates | 0% / 8% / 20% / 25% / 30% progressive (TRA) |
| Non-resident employment rate | 15% flat, final tax (PwC) |
| Tax-free threshold | First TZS 270,000/month (TRA) |
| NSSF total | 20% of gross wage — 10% employer / 10% employee (NSSF) |
| PSSSF total | 20% of gross wage — 15% employer / 5% employee (secondary; see gap) |
| SDL | 3.5% of gross emoluments, employer ≥10 employees (TRA) |
| WCF | 0.5%–0.6% of cash paid to employees, employer-only (see gap) |
| Currency | TZS only |
| Validated by | Pending — requires sign-off by a Tanzanian tax practitioner |
| Validation date | Verified by Baraka Cassian (ACPA 3158) on 2026-06-12 |

**Contribution overview (private-sector Mainland employee)**

| Item | Employer | Employee | Total | Base | Source |
| --- | --- | --- | --- | --- | --- |
| PAYE | — | 0%–30% progressive | — | Monthly income after pension | TRA |
| NSSF pension | 10% | 10% | 20% | Gross wage | NSSF |
| SDL | 3.5% | — | 3.5% | Gross emoluments (if ≥10 employees) | TRA |
| WCF | 0.5%–0.6% | — | 0.5%–0.6% | Cash paid to employees | PwC / WCF [RESEARCH GAP — reviewer to confirm tariff] |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Assume resident (progressive PAYE); ask before applying 15% flat |
| Unknown sector (private vs public) | Assume private → NSSF (10%/10%); confirm before PSSSF |
| Unknown employee headcount for SDL | If unknown, flag — SDL only applies at ≥10 employees (TRA) |
| Unknown WCF tariff | Use 0.6% private / 0.5% public and FLAG [RESEARCH GAP] |
| Unknown whether pension already deducted before PAYE | Deduct mandatory pension before computing PAYE base (TRA) |
| Zanzibar vs Mainland not stated | Assume Mainland; STOP on levies if Zanzibar (different regime) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — gross monthly wage (TZS), residency status (resident / non-resident), and sector (private vs public). Without gross wage, STOP.

**Recommended** — employer headcount (for SDL liability), whether employee is on a permitted alternative NSSF split (15%/5%), and Mainland vs Zanzibar location.

**Ideal** — TRA PAYE return (ITX 300.01.E credit slip), NSSF Form NSSF/CON.5 earnings statement, payroll register, and bank statements showing TRA / NSSF / WCF remittances.

### Refusal catalogue

- **R-TZ-SC-1 — Gross wage unknown** — Trigger: monthly gross wage not provided. Message: "Monthly gross wage in TZS is mandatory for PAYE and pension computation. PAYE is progressive and pension is a percentage of gross. Cannot proceed without this figure."
- **R-TZ-SC-2 — Zanzibar payroll levies** — Trigger: employment located in Zanzibar. Message: "PAYE brackets are identical in Zanzibar per TRA, but SDL and certain social levies operate under a separate Zanzibar regime. Do not apply Mainland SDL/levy figures to Zanzibar without confirming the Zanzibar schedule. Escalate to a practitioner."
- **R-TZ-SC-3 — WCF tariff confirmation** — Trigger: a definitive WCF figure is required for filing. Message: "The current private-sector WCF tariff is unconfirmed from WCF's own publications (PwC states 0.5%; other sources state 0.6%). Do not present a definitive WCF charge without confirming the tariff directly with WCF."
- **R-TZ-SC-4 — Arrears / penalty quantification** — Trigger: client has unpaid PAYE, NSSF, SDL, or WCF from prior periods. Message: "Statutory penalties (TRA 2.5%/month, NSSF 5%/month) compound on unpaid amounts. Do not attempt to quantify arrears without official statements. Escalate to a practitioner."
- **R-TZ-SC-5 — Presumptive tax / non-PAYE individuals** — Trigger: individual under the presumptive regime (turnover ≤ TZS 100 million). Message: "The presumptive income tax regime is outside the scope of this payroll skill and its rate bands are not captured here. Escalate to a practitioner. [RESEARCH GAP — presumptive bands not extracted]"

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Tanzanian payroll taxes and social security. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statutory remittances (PAYE, NSSF, PSSSF, SDL, WCF) are EXCLUDED from any VAT return — they are statutory obligations, not business supplies. The employer share of pension/SDL/WCF is a deductible business cost; the employee share is withheld from wages, not an employer expense.

### 3.1 TRA payments (PAYE / SDL)

**TRA payments (PAYE / SDL)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRA, TANZANIA REVENUE AUTHORITY | EXCLUDE — statutory tax remittance | PAYE and/or SDL monthly remittance |
| PAYE, P.A.Y.E | EXCLUDE — employee tax withheld | Remitted by 7th of following month |
| SDL, SKILLS DEVELOPMENT LEVY | EXCLUDE — employer levy | 3.5%; employer ≥10 staff |
| ITX 300, ITX300.01.E | EXCLUDE — employment taxes credit slip | TRA payment reference |

### 3.2 Pension fund debits (NSSF / PSSSF)

**Pension fund debits (NSSF / PSSSF)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NSSF, NATIONAL SOCIAL SECURITY FUND | EXCLUDE — pension contribution | 20% total (10% er / 10% ee) |
| NSSF/CON.5, CON.5 | EXCLUDE — NSSF contribution statement | Form filed with payment |
| PSSSF, PUBLIC SERVICE SOCIAL SECURITY | EXCLUDE — public-sector pension | 20% total (15% er / 5% ee) |
| MICHANGO YA PENSHENI | EXCLUDE — pension contribution | Swahili: "pension contributions" |

### 3.3 Workers Compensation Fund (WCF)

**Workers Compensation Fund (WCF)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| WCF, WORKERS COMPENSATION FUND | EXCLUDE — employer levy | 0.5%–0.6%, employer-only |
| MFUKO WA FIDIA KWA WAFANYAKAZI | EXCLUDE — WCF | Swahili: "workers compensation fund" |

### 3.4 Salary and payroll (exclude from contributions classification)

**Salary and payroll (exclude from contributions classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, MSHAHARA (outgoing) | EXCLUDE — payroll expense | Gross wage paid; not a contribution |
| SALARY, MSHAHARA (incoming) | EXCLUDE — employment income received | Not a contribution |
| WAGES, MISHAHARA | EXCLUDE — payroll expense | Plural Swahili "salaries" |

### 3.5 Pension / benefit payments received (NOT contributions)

**Pension / benefit payments received (NOT contributions)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NSSF PENSION, PSSSF PENSION (credit) | EXCLUDE — pension benefit received | Inbound, not a contribution paid |
| PENSHENI (credit) | EXCLUDE — pension income | Swahili: "pension" received |

## Section 4 -- Worked examples

Six bank statement / payroll classifications for a hypothetical private-sector employer and employee in Tanzania Mainland. All amounts in TZS. PAYE is computed on income **after** deducting the mandatory NSSF employee contribution (TRA).

### Example 1 — Mid-bracket employee PAYE + NSSF

**Input:** Resident employee, gross monthly wage TZS 800,000, private sector, employer has 25 staff.

**Reasoning:**
- NSSF employee 10% = 80,000. NSSF employer 10% = 80,000. NSSF total 20% = 160,000.
- PAYE base = 800,000 − 80,000 = 720,000.
- PAYE: falls in band 520,001–760,000 → 20,000 + 20% × (720,000 − 520,000) = 20,000 + 20% × 200,000 = 20,000 + 40,000 = **60,000**.
- Net pay = 800,000 − 80,000 (NSSF ee) − 60,000 (PAYE) = **660,000**.
- Employer also bears: NSSF 80,000 + SDL 3.5% × 800,000 = 28,000 + WCF 0.6% × 800,000 = 4,800.

**Classification:** PAYE 60,000 and NSSF ee 80,000 withheld; NSSF er 80,000, SDL 28,000, WCF 4,800 employer-borne. All statutory remittances EXCLUDE from VAT.

### Example 2 — Top-bracket employee PAYE

**Input:** Resident employee, gross monthly wage TZS 1,500,000, private sector.

**Reasoning:**
- NSSF employee 10% = 150,000. PAYE base = 1,500,000 − 150,000 = 1,350,000.
- PAYE: above 1,000,000 → 128,000 + 30% × (1,350,000 − 1,000,000) = 128,000 + 30% × 350,000 = 128,000 + 105,000 = **233,000**.
- Net pay = 1,500,000 − 150,000 − 233,000 = **1,117,000**.

**Classification:** PAYE 233,000 + NSSF ee 150,000 withheld. EXCLUDE remittances from VAT.

### Example 3 — Low earner below tax-free threshold

**Input:** Resident employee, gross monthly wage TZS 290,000, private sector.

**Reasoning:**
- NSSF employee 10% = 29,000. PAYE base = 290,000 − 29,000 = 261,000.
- PAYE base 261,000 ≤ 270,000 tax-free threshold → PAYE = **Nil** (TRA).
- Net pay = 290,000 − 29,000 = **261,000**.
- Note: 290,000 gross is below the new general minimum-wage baseline of TZS 358,322/month effective 1 Jan 2026 (GN 605A/2025) — flag wage compliance.

**Classification:** PAYE Nil; NSSF ee 29,000 withheld. Flag minimum-wage compliance.

### Example 4 — Non-resident employee (flat 15%)

**Input:** Non-resident employee, gross monthly employment income TZS 4,000,000.

**Reasoning:**
- Non-resident employment income is taxed at a **flat 15% final tax** (PwC) — progressive brackets do NOT apply.
- PAYE = 15% × 4,000,000 = **600,000**.
- Pension: NSSF applicability to non-residents is case-specific; flag for reviewer.

**Classification:** PAYE 600,000 (final tax). EXCLUDE from VAT. Flag NSSF applicability.

### Example 5 — TRA bank debit (combined PAYE + SDL)

**Input line:**
`07.02.2026 ; TANZANIA REVENUE AUTHORITY ; DEBIT ; ITX 300.01.E JAN PAYE+SDL ; -1,250,000 ; TZS`

**Reasoning:**
Matches "TANZANIA REVENUE AUTHORITY" / "ITX 300.01.E" (patterns 3.1). This is the monthly employment-taxes remittance (PAYE withheld + SDL) due by the 7th of the following month (TRA). EXCLUDE from VAT. The PAYE component is withheld employee tax (not an employer cost); the SDL component (3.5%) is a deductible employer levy.

**Classification:** EXCLUDE from VAT. Statutory PAYE+SDL remittance.

### Example 6 — Ambiguous NSSF debit (possible arrears/penalty)

**Input line:**
`20.03.2026 ; NATIONAL SOCIAL SECURITY FUND ; DEBIT ; ARREARS ; -3,500,000 ; TZS`

**Reasoning:**
Matches "NATIONAL SOCIAL SECURITY FUND" (pattern 3.2) but amount is irregular and reference says "ARREARS." NSSF late penalty is 5% of the unpaid amount per month or part-month (NSSF Act, Cap. 50). Cannot separate principal from penalty without an NSSF statement / Form NSSF/CON.5. EXCLUDE from VAT. Flag for reviewer.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request NSSF breakdown to split contribution principal from 5%/month penalty.

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 — PAYE is computed on income AFTER mandatory pension

- **PAYE base formula** — PAYE base = gross monthly income − mandatory NSSF/PSSSF employee contribution. Pension contributions are deductible before applying the PAYE schedule.  _(TRA)_

### Rule 2 — Resident PAYE progressive schedule (monthly, TZS)

**Resident PAYE progressive schedule**  _(TRA (Income Tax for Individuals); PwC (last reviewed 14 Jan 2026))_

| Monthly PAYE base (TZS) | Tax |
| --- | --- |
| 0 – 270,000 | Nil |
| 270,001 – 520,000 | 8% of excess over 270,000 |
| 520,001 – 760,000 | 20,000 + 20% of excess over 520,000 |
| 760,001 – 1,000,000 | 68,000 + 25% of excess over 760,000 |
| Above 1,000,000 | 128,000 + 30% of excess over 1,000,000 |

- **Cumulative figures verification and lowest band note** — Cumulative figures verified: at 520,000 → 20,000; at 760,000 → 68,000; at 1,000,000 → 128,000. Lowest band is 8% (TRA/PwC) — do not use the outdated 9% from some secondary calculators.  _(TRA/PwC)_

### Rule 3 — Tax-free threshold

- **Tax-free threshold** — The first TZS 270,000/month is not taxed (TRA states annual income of TZS 3,240,000 is not taxable). 270,000 × 12 = 3,240,000 ✓.  _(TRA)_

### Rule 4 — Non-resident flat rate

- **Non-resident employment income rate** — Non-resident employment income is taxed at a flat 15% final tax. The progressive schedule does not apply.  _(PwC)_

### Rule 5 — NSSF (private sector) contribution

- **NSSF total contribution and split** — Total NSSF = 20% of gross monthly wage, joint employer/employee. Standard split: 10% employer / 10% employee (employee share capped at 10%). Permitted alternative: 15% employer / 5% employee; employer may remit the full 20% without deducting from the employee. The legal obligation to remit rests on the employer. No published floor or ceiling on the contribution base.  _(NSSF; PwC)_

### Rule 6 — PSSSF (public sector) contribution

- **PSSSF total contribution and split** — Total PSSSF = 20%, split 15% employer / 5% employee, under the Public Service Social Security Act, 2018. [RESEARCH GAP — split sourced from secondary material; reviewer to confirm against PSSSF official documentation.]  _(Public Service Social Security Act, 2018)_

### Rule 7 — Skills and Development Levy (SDL)

- **SDL rate and threshold** — SDL = 3.5% of total gross monthly emoluments paid to all employees, payable by employers with 10 or more employees (TRA — authoritative; ignore secondary "4 or more" sources). Form ITX 300.01.E. Employer-borne. Exemptions: government departments / wholly govt-financed institutions, certain interns, and farm employers whose employees are solely engaged in farming.  _(TRA)_

### Rule 8 — Workers Compensation Fund (WCF)

- **WCF rate and treatment** — WCF is employer-borne only (not deducted from employees), payable monthly on cash paid to employees. Rate: PwC (Jan 2026) states 0.5%; other sources state 0.6% private / 0.5% public (0.6% private effective July 2021). [RESEARCH GAP — exact current private-sector tariff unconfirmed from WCF's own publications; default to 0.6% private / 0.5% public and FLAG before filing.]  _(PwC / WCF)_

### Rule 9 — Monthly remittance deadlines

**Monthly remittance deadlines**

| Item | Deadline | Source |
| --- | --- | --- |
| PAYE + SDL (TRA) | 7th day of the month following the payroll month | TRA |
| WCF | Monthly (with cash paid) | PwC |
| NSSF | Within one month after the end of the month it relates to (NSSF Act s.14); practitioners cite end of following month | NSSF Act Cap. 50 |

### Rule 10 — Penalties

**Penalties**

| Item | Penalty | Source |
| --- | --- | --- |
| PAYE/SDL late (TRA) | Higher of 2.5% of unpaid tax per month (or part) or 15 currency points (body corporate); plus interest | TRA |
| NSSF late | 5% of unpaid amount per month or part-month | NSSF Act Cap. 50 |

### Rule 11 — Minimum wage (private sector, effective 1 Jan 2026)

- **Minimum wage** — New order Government Notice No. 605A (13 Oct 2025) raises the baseline by an average 33.4% to TZS 358,322/month (cross-sector average; rates are sector-specific). Sectors not specifically covered: TZS 175,000/month. Based on a 45-hour workweek.  _(TanzLII GN 605A/2025; PKF)_

### Rule 12 — Statutory remittances are not VATable supplies

- **VAT treatment of statutory remittances** — PAYE, NSSF, PSSSF, SDL, and WCF remittances are EXCLUDED from any VAT return. Employer shares of pension/SDL/WCF are deductible business costs; employee withholdings are not employer expenses.

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 — Residency status ambiguity

- **Residency status ambiguity** — Trigger: Unclear whether the employee is resident or non-resident for the tax year. Issue: Residents use the progressive 0%–30% schedule; non-residents pay a flat 15% final tax. Misclassification changes the entire computation. Action: Flag for reviewer. Confirm tax residency before computing PAYE.

### T2-2 — NSSF split election (15%/5% vs 10%/10%)

- **NSSF split election** — Trigger: Employer applies, or asks about, the alternative 15% employer / 5% employee split, or remits the full 20% with no employee deduction. Issue: Net pay and employer cost differ depending on which permitted split applies. The employee share must not exceed 10%. Action: Flag for reviewer. Confirm the agreed split before computing net pay.

### T2-3 — SDL headcount near the threshold

- **SDL headcount near threshold** — Trigger: Employer headcount is around 9–11, or fluctuates across months. Issue: SDL applies only at 10 or more employees (TRA). Crossing the threshold mid-year changes SDL liability. Action: Flag for reviewer. Confirm the monthly headcount basis.

### T2-4 — WCF tariff (0.5% vs 0.6%)

- **WCF tariff ambiguity** — Trigger: A definitive WCF charge is needed. Issue: PwC states 0.5%; other sources state 0.6% private / 0.5% public. The exact current private tariff is unconfirmed from WCF's own publications. Action: Flag for reviewer. Confirm the tariff directly with WCF before filing. [RESEARCH GAP]

### T2-5 — Public vs private sector / fund selection

- **Public vs private sector fund selection** — Trigger: Unclear whether the employer is in the public sector (PSSSF) or private/informal sector (NSSF). Issue: Fund and split differ — NSSF 10%/10% vs PSSSF 15%/5%. The PSSSF split itself is sourced from secondary material. Action: Flag for reviewer. Confirm sector and the applicable fund.

### T2-6 — Zanzibar employment

- **Zanzibar employment** — Trigger: Employment located in Zanzibar. Issue: PAYE brackets are identical, but SDL and certain social levies follow a separate Zanzibar regime. Action: Flag for reviewer. Do not apply Mainland levy figures to Zanzibar without the Zanzibar schedule.

### T2-7 — Arrears and penalties

- **Arrears and penalties** — Trigger: Unpaid PAYE, NSSF, SDL, or WCF from prior periods. Issue: TRA penalty 2.5%/month (or part) plus interest; NSSF penalty 5%/month (or part). These compound on unpaid amounts. Action: Do not quantify arrears without official statements. Escalate to a practitioner.

## Section 7 -- Excel working paper template

When producing a Tanzanian payroll computation, structure the working paper as follows:

```
TANZANIA (MAINLAND) PAYROLL COMPUTATION -- WORKING PAPER
Client / Employer: [name]
Tax Year: [calendar year]
Prepared: [date]

INPUT DATA
  Employee name:                 [____]
  Residency status:              [Resident / Non-resident]
  Sector:                        [Private (NSSF) / Public (PSSSF)]
  Gross monthly wage (TZS):      [____]
  Employer headcount:            [____]   (SDL applies if >= 10)
  NSSF split:                    [10/10 standard / 15/5 alt / 20 er-only]
  Location:                      [Mainland / Zanzibar]

PENSION (NSSF private: 20% total)
  Employee share (10%):          TZS [____]
  Employer share (10%):          TZS [____]
  Total (20%):                   TZS [____]

PAYE (resident progressive; base = gross - employee pension)
  PAYE base:                     TZS [____]
  Band applied:                  [0 / 8% / 20% / 25% / 30%]
  PAYE due (monthly):            TZS [____]
  (Non-resident: 15% flat final tax on gross employment income)

EMPLOYER LEVIES
  SDL (3.5% of gross emoluments, if >= 10 staff): TZS [____]
  WCF (0.5%-0.6% of cash paid) [CONFIRM TARIFF]:  TZS [____]

NET PAY
  Gross:                         TZS [____]
  Less employee NSSF (10%):      TZS [____]
  Less PAYE:                     TZS [____]
  Net pay:                       TZS [____]

REMITTANCE DEADLINES
  PAYE + SDL (TRA, 7th of next month): [____]
  NSSF (within one month after month-end): [____]
  WCF (monthly): [____]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How payroll-tax debits appear on Tanzanian bank statements

**CRDB Bank:**
- Description: "TRA", "TANZANIA REVENUE AUTHORITY", "PAYE", "SDL", "NSSF", "WCF"
- Timing: TRA (PAYE/SDL) around the 7th of the following month; NSSF by month-end following

**NMB Bank:**
- Description: "TRA PAYMENT", "ITX 300", "NSSF", "PSSSF", "WCF"
- Timing: Same monthly cycle

**NBC Bank:**
- Description: "TANZANIA REVENUE AUTHORITY", "NATIONAL SOCIAL SECURITY FUND", "WORKERS COMPENSATION FUND"
- Timing: Same monthly cycle

**Key identification tips:**
1. Statutory remittances are always outgoing (DEBIT), never credits.
2. TRA debits cover PAYE and/or SDL; pension debits go to NSSF or PSSSF; WCF is a separate small debit.
3. PAYE/SDL recur around the 7th of the following month; NSSF by the end of the following month.
4. Swahili terms: MSHAHARA = salary; MICHANGO YA PENSHENI = pension contributions; MFUKO WA FIDIA KWA WAFANYAKAZI = workers compensation fund; PENSHENI = pension.
5. Inbound credits labelled "NSSF PENSION" / "PENSHENI" are benefits received, not contributions paid.
6. Irregular lump sums with "ARREARS" may include penalties — flag and request a fund statement.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for statutory debits** — identify all outgoing payments matching Section 3 patterns (TRA, NSSF, PSSSF, SDL, WCF).
2. **Group by type** — separate TRA (PAYE/SDL) from pension (NSSF/PSSSF) and from WCF.
3. **Reverse-engineer the wage base where possible:**
   - NSSF total ÷ 20% ≈ gross wage (standard split). Employee 10% line ÷ 10% ≈ gross wage.
   - SDL ÷ 3.5% ≈ total gross emoluments for the payroll (only if employer has ≥10 staff).
4. **Confirm sector** — NSSF implies private/informal; PSSSF implies public.
5. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Residency, sector, NSSF split, headcount, and the WCF tariff have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### PAYE worked figures (resident, 2026)

**PAYE worked figures (resident, 2026)**

| Gross wage (TZS) | NSSF ee (10%) | PAYE base | PAYE due | Net pay | Source |
| --- | --- | --- | --- | --- | --- |
| 290,000 | 29,000 | 261,000 | 0 | 261,000 | TRA |
| 800,000 | 80,000 | 720,000 | 60,000 | 660,000 | TRA |
| 1,500,000 | 150,000 | 1,350,000 | 233,000 | 1,117,000 | TRA |

(Arithmetic: 720,000 → 20,000 + 20%×200,000 = 60,000. 1,350,000 → 128,000 + 30%×350,000 = 233,000.)

### Thresholds and rates summary

**Thresholds and rates summary**

| Item | Figure | Source |
| --- | --- | --- |
| Tax-free threshold | TZS 270,000/month (TZS 3,240,000/year) | TRA |
| Top marginal PAYE | 30% (over TZS 1,000,000/month base) | TRA |
| Non-resident PAYE | 15% flat final | PwC |
| NSSF total | 20% (10% er / 10% ee) | NSSF |
| PSSSF total | 20% (15% er / 5% ee) [GAP — secondary] | Public Service SSA 2018 |
| SDL | 3.5%, employer ≥10 staff | TRA |
| WCF | 0.5%–0.6% [GAP — confirm] | PwC / WCF |
| Minimum wage (1 Jan 2026) | TZS 358,322/month avg; TZS 175,000 uncovered sectors | GN 605A/2025; PKF |
| Corporate income tax (context) | 30% standard; 25% newly DSE-listed 3 yrs | PwC / TRA |

### Penalties

**Penalties**

| Item | Penalty | Source |
| --- | --- | --- |
| PAYE/SDL late (TRA) | Higher of 2.5%/month (or part) of unpaid tax or 15 currency points (body corporate) + interest | TRA |
| NSSF late | 5% of unpaid amount per month or part-month | NSSF Act Cap. 50 |

### Test suite

**Test 1:** Resident, gross 800,000, private. → NSSF ee 80,000; PAYE base 720,000; PAYE 60,000; net 660,000.

**Test 2:** Resident, gross 1,500,000, private. → NSSF ee 150,000; PAYE base 1,350,000; PAYE 233,000; net 1,117,000.

**Test 3:** Resident, gross 290,000, private. → NSSF ee 29,000; PAYE base 261,000; PAYE Nil; net 261,000.

**Test 4:** Resident, gross 600,000, private. → NSSF ee 60,000; PAYE base 540,000; PAYE = 20,000 + 20%×(540,000−520,000) = 20,000 + 4,000 = 24,000; net = 600,000 − 60,000 − 24,000 = 516,000.

**Test 5:** Resident, gross 1,000,000, private. → NSSF ee 100,000; PAYE base 900,000; PAYE = 68,000 + 25%×(900,000−760,000) = 68,000 + 35,000 = 103,000; net = 1,000,000 − 100,000 − 103,000 = 797,000.

**Test 6:** Non-resident, gross 4,000,000. → PAYE = 15%×4,000,000 = 600,000 (final tax).

**Test 7:** Private employer, total payroll 50,000,000, 30 staff. → SDL = 3.5%×50,000,000 = 1,750,000 (employer-borne). WCF (0.6%) = 300,000 [confirm tariff].

**Test 8:** Public-sector employee, gross 1,200,000, PSSSF 15/5. → PSSSF ee 5% = 60,000; PSSSF er 15% = 180,000; total 20% = 240,000 [GAP — confirm PSSSF split].

### Prohibitions

- NEVER compute PAYE without the monthly gross wage.
- NEVER apply progressive brackets to a non-resident — non-resident employment income is a flat 15% final tax.
- NEVER compute PAYE on gross — always deduct the mandatory employee pension contribution first (TRA).
- NEVER charge SDL to an employer with fewer than 10 employees (TRA).
- NEVER present a definitive WCF figure without confirming the current tariff with WCF [RESEARCH GAP].
- NEVER apply the PSSSF 15/5 split as definitive without confirming against PSSSF documentation [RESEARCH GAP].
- NEVER apply Mainland SDL/levy figures to Zanzibar without the Zanzibar schedule.
- NEVER deduct more than 10% from an employee for NSSF — the employee share is capped at 10%.
- NEVER quantify arrears or penalties without official TRA/NSSF statements — escalate to a practitioner.
- NEVER present figures as definitive — label as estimated and direct the client to their TRA/NSSF statements.

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
