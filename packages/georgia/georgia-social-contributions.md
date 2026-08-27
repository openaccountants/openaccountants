---
name: georgia-social-contributions
description: "Use this skill whenever asked about social contributions, social security, or the mandatory funded pension in the country of Georgia (GE — Tbilisi, Caucasus; NOT the U.S. state of Georgia). Trigger on phrases like \"Georgia pension contribution\", \"funded pension 2%\", \"Georgia social security\", \"do I pay social contributions in Georgia\", \"pension agency Georgia\", \"Georgia payroll withholding\", \"Georgia PIT 20%\", \"Georgia employer on-cost\", \"Georgia salary net pay\", \"saპensio / sapensio fund\", \"state co-contribution Georgia\", or any question about employment-based social-insurance levies for a Georgian employer or employee. Also trigger when classifying bank statement transactions involving the Pension Agency (LEPL Pension Fund), Revenue Service of Georgia (rs.ge), unified monthly income-tax declaration debits, or PIT withholding from Georgian banks (TBC, Bank of Georgia, Liberty Bank). CRITICAL: Georgia (the country) has NO classic social-security/health/unemployment payroll system — the only mandatory employment social-insurance levy is the funded pension (2% employee + 2% employer + tiered state co-contribution). This skill covers the funded pension rates and tiers, mandatory/voluntary participation, flat 20% PIT withholding, monthly compliance, bank-statement classification, and edge cases. ALWAYS read this skill before touching any Georgia social-contribution or payroll work."
version: 0.1
jurisdiction: GE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Gvantsa Amiridze
review_status: current
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia (Country) Social Contributions & Funded Pension

## Georgia (Country) Social Contributions & Funded Pension Skill v0.1

> **JURISDICTION WARNING.** This skill is for **Georgia the country** (GE — capital Tbilisi, ISO `GE`, currency GEL). It is **NOT** for the U.S. state of Georgia. Search engines and training data heavily conflate the two. If a client mentions USD, the IRS, Atlanta, or a U.S. SSN, STOP — this is the wrong skill.

## Section 1 -- Quick reference

- **Read this whole section** — Read this whole section before computing or classifying anything.
- **Country** — Georgia (the country, Caucasus) — ISO `GE`
- **Currency** — GEL (Georgian lari) only
- **Primary Legislation (pension)** — Law of Georgia "On Funded Pension", effective 1 January 2019 (matsne doc. 4280127)  _(matsne doc. 4280127)_
- **Primary Legislation (PIT)** — Tax Code of Georgia (income tax / payroll withholding)  _(Tax Code of Georgia)_
- **Pension Authority** — Pension Agency of Georgia — LEPL Pension Fund (pensions.ge)
- **Tax Authority (PIT)** — Revenue Service of Georgia (rs.ge)
- **Classic social security (health/unemployment)** — **NONE** — Georgia has no payroll-tax-funded social-security system  _(PwC, Individual — Other taxes)_
- **Funded pension — employee** — 2% of taxable gross salary  _(matsne 4280127)_
- **Funded pension — employer** — 2% of taxable gross salary  _(matsne 4280127)_
- **Funded pension — state co-contribution** — 2% up to GEL 24,000 annual income; 1% from GEL 24,000–60,000; 0% above GEL 60,000  _(matsne 4280127; PwC)_
- **Funded pension — self-employed (opt-in)** — 4% of income, voluntary  _(matsne 4280127; PwC)_
- **Personal income tax (PIT)** — Flat 20%, no brackets, withheld at source  _(PwC, Individual — Taxes on personal income)_
- **Tax year** — Calendar year  _(PwC, Individual — Tax administration)_
- **Monthly declaration deadline** — 15th day of the month following the salary-payment month  _(PwC, Corporate — Tax administration)_
- **Pension transfer deadline** — No later than the 15th of the month following the salary-payment month  _(F-Chain, 1 May 2025 rules)_
- **Annual individual return** — Due 1 April of the following year (income not taxed at source)  _(PwC, Individual — Tax administration)_
- **Late-payment interest** — 0.05% of the unpaid amount per overdue day  _(Tax Code of Georgia; PwC/GSL)_
- **Validated by** — Pending — requires sign-off by a qualified Georgian tax adviser
- **Validation date** — Pending

**Funded pension contribution stack (the ONLY mandatory employment social-insurance levy)**  _(matsne 4280127; PwC Individual — Other taxes)_

| Annual taxable income band | Employee | Employer | State | Total credited to individual account |
| --- | --- | --- | --- | --- |
| Up to GEL 24,000 | 2% | 2% | 2% | **6%** |
| GEL 24,000 – 60,000 (portion in band) | 2% | 2% | 1% | **5%** |
| Above GEL 60,000 (portion in band) | 2% | 2% | 0% | **4%** |

- **Arithmetic check** — 2 + 2 + 2 = 6; 2 + 2 + 1 = 5; 2 + 2 + 0 = 4.  _(matsne 4280127; PwC Individual — Other taxes)_
- **NOTE on tiers** — Employee and employer each pay a flat 2% on the **full** taxable salary — there is no upper ceiling on the 2%+2% portion. Only the **state** share is income-tiered/capped (matsne 4280127). The GEL 24,000 / 60,000 thresholds apply to **annual** income; whether they are applied per-month-prorated or reconciled annually is **[RESEARCH GAP — reviewer to confirm against rs.ge guidance]**.  _(matsne 4280127)_

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Employee age / enactment-status unknown | Treat as MANDATORY participant (under 60 / women under 55) — apply 2% employee + 2% employer on full taxable salary (matsne 4280127) |
| State co-contribution share uncertain | Apply 2% only up to GEL 24,000, 1% from 24,000–60,000, ZERO above 60,000 — never assume a state top-up above GEL 60,000 |
| Self-employed participation unknown | Treat as VOLUNTARY / OFF by default; apply 4% only if the individual has elected in (matsne 4280127) |
| Any health / unemployment / "social security" payroll levy | Do NOT model one — none exists in Georgia (PwC) |
| Currency unstated | Assume GEL; if USD/IRS appears, STOP — wrong jurisdiction |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- confirmation that the engagement concerns **Georgia the country** (not the U.S. state), the employee's taxable gross monthly salary in GEL, and whether the worker is an employee or self-employed.

**Recommended** -- employee's age at the law's entry into force (1 Jan 2019) / current age, annual taxable income (to apply the state co-contribution tiers), and whether the employee has opted out (age-40+ window) or is in the voluntary-only group (60/55+ at enactment).

**Ideal** -- payroll register, the unified monthly income-tax declaration filed with rs.ge, Pension Agency statement of individual account, and bank statements showing PIT and pension transfers.

### Refusal catalogue

- **R-GE-SC-1 -- Wrong Georgia (U.S. state)** — Trigger: references to USD, the IRS, Atlanta, a U.S. SSN, or "Georgia state income tax." Message: "This skill covers the country of Georgia (GE). For the U.S. state of Georgia, use a U.S. state payroll skill — do not apply these rates."
- **R-GE-SC-2 -- Pension arrears / historical contributions** — Trigger: unpaid pension contributions from prior periods. Message: "Late pension/PIT amounts accrue 0.05% per overdue day under the Tax Code of Georgia, and specific declaration fines apply. Do not quantify arrears without a Revenue Service / Pension Agency statement. Escalate to a qualified Georgian adviser."
- **R-GE-SC-3 -- Participation-status edge cases** — Trigger: employee near the 60/55 age boundary, claiming an opt-out, or a returning/re-enrolling participant. Message: "Mandatory vs voluntary participation and the age-40+ opt-out window (3–5 months after joining) are case-specific. Confirm the worker's status with the Pension Agency before computing. Escalate to a reviewer."
- **R-GE-SC-4 -- Expat / treaty / totalisation questions** — Trigger: foreign worker, social-security totalisation, or treaty relief. Message: "Georgia has no classic social-security system, so totalisation does not apply in the usual sense; expat funded-pension treatment is case-specific. Escalate to a qualified Georgian adviser."
- **R-GE-SC-5 -- Specific penalty quantification** — Trigger: request for exact GEL fines for non-filing/non-payment. Message: "The 0.05%/day late interest is confirmed, but exact GEL declaration fines are not reliably sourced here [RESEARCH GAP]. Do not state a precise fine; direct the client to rs.ge / the current Tax Code of Georgia."

## Section 3 -- Payment pattern library

Deterministic pre-classifier for bank statement transactions related to Georgian payroll, PIT, and pension. Match by case-insensitive substring on the counterparty/reference. PIT and pension transfers EXCLUDE from any VAT return — they are statutory payroll/withholding obligations, not business supplies.

### 3.1 Funded pension transfers (employee 2% + employer 2%)

**Funded pension transfers pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION AGENCY, საპენსიო სააგენტო | EXCLUDE -- pension contribution | Transfer to LEPL Pension Fund |
| PENSION FUND, LEPL PENSION FUND | EXCLUDE -- pension contribution | Same |
| საპენსიო, SAPENSIO, PENSIO | EXCLUDE -- pension contribution | Georgian-language reference |
| FUNDED PENSION, დაგროვებითი პენსია | EXCLUDE -- pension contribution | "Funded/accumulated pension" |
| PENSION 2%, PENSION CONTRIB | EXCLUDE -- pension contribution | Explicit rate/contribution reference |

### 3.2 Pension transfers appearing on specific Georgian banks

**Bank pension transfer descriptions**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| TBC Bank | "PENSION AGENCY" or "საპენსიო სააგენტო" | EXCLUDE -- pension contribution |
| Bank of Georgia (BOG) | "PENSION FUND" or "PENSIO" | EXCLUDE -- pension contribution |
| Liberty Bank | "PENSION AGENCY GE" or "PENSIO" | EXCLUDE -- pension contribution |
| Wise / Revolut | Rare — pension transfers usually from local GEL accounts | If present, EXCLUDE |

### 3.3 PIT / Revenue Service payments (NOT pension -- do not confuse)

**PIT / Revenue Service pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| REVENUE SERVICE, RS.GE, შემოსავლების სამსახური | EXCLUDE -- PIT/tax payment | 20% PIT withholding remittance, not pension |
| INCOME TAX, PIT, საშემოსავლო | EXCLUDE -- income tax | Withheld at source, not pension |
| DECLARATION, დეკლარაცია | EXCLUDE -- tax declaration payment | Unified monthly declaration |
| VAT, დღგ, DGG | EXCLUDE -- VAT, not pension | Separate from payroll |

### 3.4 Salary and payroll (exclude from pension/PIT classification)

**Salary and payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, ხელფასი, KHELPASI (outgoing) | EXCLUDE -- payroll expense | Net-of-PIT-and-pension wage payment |
| SALARY, ხელფასი (incoming) | EXCLUDE -- employment income received | Net salary received by employee |

### 3.5 Pension benefits received (NOT a contribution paid)

**Pension benefits received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION PAYOUT, საპენსიო გადახდა | EXCLUDE -- pension benefit received | Inbound credit, not a contribution |
| STATE PENSION, OLD AGE PENSION | EXCLUDE -- pension income | Not a contribution |

## Section 4 -- Worked examples

Bank-statement classifications and computations for a hypothetical Tbilisi employer and its employees. All amounts in GEL. PIT is a flat 20% withheld at source; funded pension is 2% employee + 2% employer (matsne 4280127; PwC).

### Example 1 -- Low salary, mandatory participant (annual ≤ GEL 24,000)

**Input line:**
`15.02.2025 ; PENSION AGENCY ; DEBIT ; PENSION FEB 2025 EMP+EE ; -40.00 ; GEL`

**Facts:** Monthly taxable salary GEL 1,000 (annual GEL 12,000 ≤ 24,000). Employee aged 32 — mandatory participant.

**Reasoning:**
Employee pension 2% × 1,000 = GEL 20. Employer pension 2% × 1,000 = GEL 20. Combined transfer to the Pension Agency = GEL 40 (matches the line). PIT 20% × 1,000 = GEL 200, remitted separately to rs.ge. State co-contribution 2% × 1,000 = GEL 20/month credited by the government (not a bank movement). Net pay to employee = 1,000 − 200 (PIT) − 20 (employee pension) = **GEL 780**.

Check: 200 + 20 + 780 = 1,000. ✓

**Classification:** EXCLUDE from VAT — funded pension contribution (employer 2% + employee 2%).

### Example 2 -- Mid salary, middle state tier (annual GEL 24,000–60,000)

**Input line:**
`15.04.2025 ; REVENUE SERVICE ; DEBIT ; MONTHLY DECLARATION MAR 2025 ; -600.00 ; GEL`

**Facts:** Monthly taxable salary GEL 3,000 (annual GEL 36,000 — middle state tier). Employee aged 41, mandatory participant (no opt-out elected).

**Reasoning:**
The line is the PIT remittance: 20% × 3,000 = GEL 600 (matches). Employee pension 2% × 3,000 = GEL 60; employer pension 2% × 3,000 = GEL 60 (a separate Pension Agency transfer of GEL 120). State co-contribution on annual GEL 36,000 = 2% × 24,000 + 1% × 12,000 = 480 + 120 = **GEL 600/year** (≈ GEL 50/month). Net pay = 3,000 − 600 − 60 = **GEL 2,340**.

Check: 600 + 60 + 2,340 = 3,000. ✓

**Classification:** EXCLUDE from VAT — PIT withholding remittance (NOT a pension transfer).

### Example 3 -- High salary, state share capped (annual > GEL 60,000)

**Input line:**
`15.06.2025 ; PENSION FUND ; DEBIT ; PENSION MAY 2025 ; -240.00 ; GEL`

**Facts:** Monthly taxable salary GEL 6,000 (annual GEL 72,000 > 60,000). Employee aged 29, mandatory participant.

**Reasoning:**
Employee pension 2% × 6,000 = GEL 120; employer pension 2% × 6,000 = GEL 120; combined transfer = GEL 240 (matches). The 2%+2% applies to the FULL salary — there is no ceiling on the employee/employer portion. State co-contribution: 2% × 24,000 + 1% × 36,000 + 0% above 60,000 = 480 + 360 = **GEL 840/year**; nothing on the income above GEL 60,000. PIT 20% × 6,000 = GEL 1,200. Net pay = 6,000 − 1,200 − 120 = **GEL 4,680**.

Check: 1,200 + 120 + 4,680 = 6,000. ✓

**Classification:** EXCLUDE from VAT — funded pension contribution (employer 2% + employee 2%).

### Example 4 -- Self-employed voluntary opt-in (4%)

**Input line:**
`20.03.2025 ; საპენსიო სააგენტო ; DEBIT ; VOLUNTARY PENSION 2024 ; -2,000.00 ; GEL`

**Facts:** Self-employed individual entrepreneur, annual income GEL 50,000, has **elected** to participate in the funded pension.

**Reasoning:**
Self-employed participation is VOLUNTARY (default off). Since this individual opted in, the rate is 4% of income: 4% × 50,000 = **GEL 2,000** (matches). State co-contribution follows the same tiers: 2% × 24,000 + 1% × 26,000 = 480 + 260 = **GEL 740/year**. If the individual had NOT opted in, no pension contribution would be due (matsne 4280127).

Check: 4% × 50,000 = 2,000. ✓

**Classification:** EXCLUDE from VAT — voluntary self-employed funded pension contribution.

### Example 5 -- Revenue Service payment that is NOT pension

**Input line:**
`14.05.2025 ; შემოსავლების სამსახური ; DEBIT ; VAT APR 2025 ; -1,800.00 ; GEL`

**Facts:** The reference says "VAT" (დღგ), not pension or PIT.

**Reasoning:**
Matches the Revenue Service pattern (3.3) but the reference is **VAT**, not pension or PIT withholding. This is a VAT remittance (standard rate 18%, registration threshold GEL 100,000 turnover — GSL/PwC), entirely separate from the funded pension. Do NOT classify as a social/pension contribution.

**Classification:** EXCLUDE from social-contribution classification — VAT payment (handle under a VAT skill).

### Example 6 -- Ambiguous pension debit (arrears / penalty)

**Input line:**
`15.09.2025 ; PENSION AGENCY ; DEBIT ; ARREARS + INTEREST ; -510.00 ; GEL`

**Facts:** Irregular amount; reference mentions "ARREARS + INTEREST."

**Reasoning:**
Matches the Pension Agency pattern (3.1) but the amount is irregular and references interest. Late amounts accrue 0.05%/day under the Tax Code of Georgia, so this likely bundles overdue contribution principal with interest. The split cannot be derived without a Pension Agency / Revenue Service statement. Flag for reviewer.

**Classification:** EXCLUDE from VAT. Flag for reviewer — request a statement to split contribution principal from late interest. Specific GEL fines are **[RESEARCH GAP — reviewer to confirm]**.

## Section 5 -- Tier 1 rules

Apply exactly as written when the data is clear and the engagement is confirmed to be **Georgia the country**.

### Rule 1 -- There is NO classic social security

- **No classic social security** — Georgia has no payroll-tax-funded health, unemployment, or social-security fund. The ONLY mandatory employment social-insurance levy is the funded pension. Do not model any other social contribution.  _(PwC, Individual — Other taxes)_

### Rule 2 -- Funded pension formula

- **Funded pension formula** — employee_pension = 2% × taxable_gross_salary employer_pension = 2% × taxable_gross_salary state_cocontribution = 2% × min(annual_income, 24,000) + 1% × clamp(annual_income − 24,000, 0, 36,000) + 0% × max(annual_income − 60,000, 0) The 2% employee and 2% employer apply to the FULL taxable salary (no ceiling). Only the state share is tiered/capped at GEL 60,000.  _(matsne 4280127)_

### Rule 3 -- PIT is a flat 20%, withheld at source

- **PIT flat 20%** — Employers withhold 20% PIT on gross salary (PAYE-style) and remit it with the unified monthly income-tax declaration. There are no progressive brackets.  _(PwC, Individual — Taxes on personal income)_

### Rule 4 -- Net pay computation

- **Net pay computation** — net_pay = gross_salary − PIT(20%) − employee_pension(2%) Employer pension (2%) is an employer on-cost paid in addition to gross salary, not deducted from the employee. The state co-contribution is credited by the government and is not a bank movement.  _(matsne 4280127)_

### Rule 5 -- Pension base equals the PIT base

- **Pension base equals PIT base** — Funded pension is computed on **taxable salary** — the same base as PIT.  _(matsne 4280127)_

### Rule 6 -- Participation is mandatory for working-age employees

- **Mandatory participation** — Mandatory for all employees who were under age 60 (women under 55) at the law's entry into force (1 Jan 2019); participation begins automatically on the first employer contribution.  _(matsne 4280127; PwC)_

### Rule 7 -- Voluntary groups

- **Voluntary groups** — Persons aged 60/55+ at enactment, and self-employed individuals, participate **voluntarily**. Self-employed opt-in rate is 4% of income.  _(matsne 4280127)_

### Rule 8 -- Opt-out window (age 40+)

- **Opt-out window** — Employees aged 40 or older before the effective date may withdraw, but only within the window **after 3 months and before 5 months** from joining.  _(matsne 4280127)_

### Rule 9 -- Monthly compliance

- **Monthly compliance** — PIT and the unified monthly income-tax declaration are due by the **15th** of the month following the salary-payment month; pension contributions must be transferred no later than the same **15th**.  _(PwC, Corporate — Tax administration; F-Chain 2025)_

### Rule 10 -- Single declaration since 1 May 2025

- **Single declaration since 1 May 2025** — From 1 May 2025, employers no longer file a separate pension declaration — pension data is auto-populated in the Pension Agency system from the income-tax declaration filed with the Revenue Service, and the pension declaration auto-closes once the transferred amount matches.  _(F-Chain, 1 May 2025)_

### Rule 11 -- Calendar tax year; annual return 1 April

- **Calendar tax year; annual return 1 April** — The tax year is the calendar year. Annual individual income tax returns (for income not taxed at source) are due by 1 April of the following year.  _(PwC, Individual — Tax administration)_

### Rule 12 -- Late interest

- **Late interest** — Late payment of tax/contributions accrues interest at 0.05% of the unpaid amount per overdue day.  _(Tax Code of Georgia; PwC/GSL)_

## Section 6 -- Tier 2 catalogue

Flag these for reviewer judgement.

### T2-1 -- Employee near the 60/55 age boundary

- **Employee near the 60/55 age boundary** — Trigger: Worker's age at 1 Jan 2019 enactment is close to 60 (men) / 55 (women). Issue: Above that age at enactment → participation is voluntary, not mandatory. Action: Confirm enactment-date age with the Pension Agency before treating as mandatory. Flag for reviewer.

### T2-2 -- Age-40+ opt-out election

- **Age-40+ opt-out election** — Trigger: Worker was 40+ before the effective date and may have used the 3–5 month opt-out window. Issue: A valid withdrawal means no further employee/employer pension is due for that worker. Action: Verify the opt-out status; do not withhold pension if a valid opt-out exists. Flag for reviewer.

### T2-3 -- State co-contribution tier application (monthly vs annual)

- **State co-contribution tier application** — Trigger: Income straddles the GEL 24,000 / 60,000 annual thresholds. Issue: Whether the tiers are prorated monthly or reconciled annually is **[RESEARCH GAP — reviewer to confirm against rs.ge guidance]**. Action: Compute the employer/employee 2%+2% normally; flag the state-share tiering for reviewer reconciliation.

### T2-4 -- Self-employed participation election

- **Self-employed participation election** — Trigger: Self-employed individual asks whether to/has opted into the pension. Issue: Participation is voluntary at 4%; default is OFF until election. Action: Confirm whether an election was made before applying 4%. Flag for reviewer.

### T2-5 -- Pension/PIT arrears

- **Pension/PIT arrears** — Trigger: Unpaid pension or PIT from prior periods. Issue: 0.05%/day interest accrues; exact GEL declaration fines are **[RESEARCH GAP]**. Action: Do not quantify without a Revenue Service / Pension Agency statement. Escalate to a qualified Georgian adviser.

### T2-6 -- Expat / non-resident worker

- **Expat / non-resident worker** — Trigger: Foreign worker on a Georgian payroll. Issue: Funded-pension applicability and source-of-income rules are case-specific; Georgia has no totalisation framework in the usual sense. Action: Flag for reviewer / qualified Georgian adviser.

## Section 7 -- Excel working paper template

```
GEORGIA (COUNTRY) PAYROLL / PENSION COMPUTATION -- WORKING PAPER
Client: [name]
Tax Year: [calendar year]
Prepared: [date]
JURISDICTION CONFIRMED = COUNTRY OF GEORGIA (GE), NOT U.S. STATE:  [YES/NO]

INPUT DATA
  Worker type:                   [Employee / Self-employed]
  Age at 1 Jan 2019 enactment:   [____]   (< 60 / women < 55 = mandatory)
  Participation status:          [Mandatory / Voluntary / Opted-out]
  Self-employed opt-in?:         [YES / NO / n.a.]
  Monthly taxable gross salary:  GEL [____]
  Annual taxable income:         GEL [____]

PIT (FLAT 20%)
  PIT (20% × gross):             GEL [____]

FUNDED PENSION
  Employee pension (2% × salary):   GEL [____]
  Employer pension (2% × salary):   GEL [____]   (employer on-cost)
  Self-employed (4% × income):      GEL [____]   (if opted in)
  Combined transfer to Pension Agency: GEL [____]

STATE CO-CONTRIBUTION (info only — credited by government)
  2% × min(annual, 24,000):         GEL [____]
  1% × clamp(annual−24,000,0,36,000): GEL [____]
  0% above 60,000:                  GEL 0
  Total state share (annual):       GEL [____]

NET PAY
  Net pay (gross − PIT − employee pension): GEL [____]

COMPLIANCE
  Monthly declaration due (15th of next month): [date]
  Pension transfer due (15th of next month):    [date]

REVIEWER FLAGS
  [List any Tier 2 flags + RESEARCH GAP items here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How pension and PIT movements appear on Georgian bank statements

**TBC Bank:**
- Description: "PENSION AGENCY" / "საპენსიო სააგენტო" (pension) or "REVENUE SERVICE" / "შემოსავლების სამსახური" (PIT)
- Timing: around the 15th of the month following the salary-payment month
- Amount: pension transfer = 4% of salary (employer 2% + employee 2%); PIT = 20% of gross

**Bank of Georgia (BOG):**
- Description: "PENSION FUND" / "PENSIO" (pension) or "INCOME TAX" / "საშემოსავლო" (PIT)
- Timing: same monthly cycle

**Liberty Bank:**
- Description: "PENSION AGENCY GE" or "REVENUE SERVICE GE"
- Timing: same monthly cycle

**Key identification tips:**
1. Pension and PIT transfers are always outgoing (DEBIT) for the employer.
2. A combined pension transfer ≈ 4% of gross salary (2% employer + 2% employee). PIT ≈ 20% of gross.
3. The state co-contribution is NOT a bank movement — it is credited by the government to the individual account.
4. Do NOT confuse Revenue Service (rs.ge) PIT/VAT debits with Pension Agency (pensions.ge) pension transfers.
5. Georgian-language refs: საპენსიო = pension; საშემოსავლო = income tax; დღგ = VAT; ხელფასი = salary.
6. Irregular Pension Agency debits referencing "arrears" or "interest" may bundle 0.05%/day late interest — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Confirm jurisdiction** — verify the currency is GEL and references are to rs.ge / Pension Agency, not the IRS / U.S. Georgia. If USD/IRS, STOP (R-GE-SC-1).
2. **Scan for Pension Agency debits** — identify outgoing payments matching Section 3.1/3.2. A combined transfer ÷ 0.04 estimates gross salary (2% + 2% = 4%).
3. **Scan for Revenue Service debits** — PIT remittances ≈ 20% of gross salary; reconcile against pension-derived salary estimate.
4. **Reverse-engineer participation** — if pension debits exist, the worker is participating (mandatory or voluntary). If none, the worker may be opted-out, voluntary-off, or pre-1 May 2019 exempt — flag.
5. **Flag for reviewer:** "Pension/PIT classification derived from bank-statement amounts only. Worker age, participation status, and the state co-contribution tiers have not been independently verified. Reviewer must confirm before filing the monthly declaration."

## Section 10 -- Reference material

### Contribution & rate summary (2025)

**Contribution & rate summary (2025)**

| Item | Rate / value | Source |
| --- | --- | --- |
| Funded pension — employee | 2% of taxable salary | matsne 4280127; PwC |
| Funded pension — employer | 2% of taxable salary | matsne 4280127; PwC |
| Funded pension — state (≤ GEL 24,000) | 2% | matsne 4280127; PwC |
| Funded pension — state (GEL 24,000–60,000) | 1% | matsne 4280127; PwC |
| Funded pension — state (> GEL 60,000) | 0% | matsne 4280127; PwC |
| Funded pension — self-employed (voluntary) | 4% of income | matsne 4280127; PwC |
| Personal income tax (PIT) | Flat 20% | PwC Individual — Taxes on personal income |
| Corporate income tax (Estonian/distributed-profits model) | 15% (20% for banks/credit/microfinance institutions from 1 Jan 2023) | GSL; PwC Corporate |
| Dividend/interest WHT (individuals/non-residents) | 5% | GSL; PwC Corporate — Withholding taxes |
| VAT standard rate | 18% | GSL; PwC Corporate — Other taxes |
| Late-payment interest | 0.05% per overdue day | Tax Code of Georgia; PwC/GSL |

### Thresholds (2025)

**Thresholds (2025)**

| Threshold | Value | Effect | Source |
| --- | --- | --- | --- |
| State co-contribution upper-tier start | GEL 24,000 annual income | State share drops from 2% to 1% above this | matsne 4280127; PwC |
| State co-contribution cut-off | GEL 60,000 annual income | No state share above this; only 2% + 2% continue | matsne 4280127; PwC |
| Mandatory-pension age exemption | Age 60 (men) / 55 (women) at enactment | Above this at enactment = voluntary only | matsne 4280127 |
| Pension opt-out age | Age 40+ before effective date | May withdraw within the 3-to-5-month window after joining | matsne 4280127 |
| VAT registration threshold | GEL 100,000 taxable turnover in any continuous 12 months | Mandatory VAT registration | GSL; PwC |
| Micro Business PIT exemption | Turnover under GEL 30,000, no employees | Business income PIT-exempt | PwC Individual |
| Small Business turnover regime | Turnover under GEL 500,000 (GEL 700,000 for wine tourism / agrotourism) | 1% turnover tax (3% on excess above GEL 500,000) | PwC Individual; GSL |

### Forms / declarations

**Forms / declarations**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Unified monthly income-tax declaration (rs.ge) | Reports salaries paid, PIT withheld; auto-derives pension data from 1 May 2025 | 15th of the month following the salary-payment month | PwC; F-Chain 2025 |
| Pension contribution transfer (Pension Agency) | Transfer of employer 2% + employee 2% to individual accounts | No later than the 15th of the month following the salary-payment month | F-Chain 2025 |
| Annual individual income tax return | Declare income not taxed at source (self-employed, capital gains, etc.) | 1 April of the year following the tax year | PwC Individual — Tax administration |

### Penalties

**Penalties**

| Penalty | Amount | Source |
| --- | --- | --- |
| Late payment of tax/contributions | Interest at 0.05% of the unpaid amount per overdue day | Tax Code of Georgia; PwC/GSL |
| Failure to submit a required document | GEL 100 per document failure; exact declaration fines **[RESEARCH GAP — reviewer to confirm against the current Tax Code of Georgia]** | PwC/GSL |

### Minimum wage

There is no effective statutory national minimum wage. The nominal figure (Presidential Decree No. 351 of 1999) is ~GEL 20/month private sector and ~GEL 115/month public sector — unchanged since 1999 and economically irrelevant; market and living wages are far higher. **[RESEARCH GAP — sourced from secondary HR/payroll sites (CXC Global, Playroll), not an official gazette; treat as "Georgia effectively has no functional minimum wage."]**

### Calculation examples (2025)

**Calculation examples (2025)**  _(matsne 4280127; PwC)_

| Monthly gross | Annual | State tier | Employee pension (2%) | Employer pension (2%) | PIT (20%) | Net pay |
| --- | --- | --- | --- | --- | --- | --- |
| GEL 1,000 | GEL 12,000 | 2% (≤24k) | GEL 20 | GEL 20 | GEL 200 | GEL 780 |
| GEL 3,000 | GEL 36,000 | 1% band | GEL 60 | GEL 60 | GEL 600 | GEL 2,340 |
| GEL 6,000 | GEL 72,000 | 0% above 60k | GEL 120 | GEL 120 | GEL 1,200 | GEL 4,680 |

- **Arithmetic check** — 1,000 − 200 − 20 = 780; 3,000 − 600 − 60 = 2,340; 6,000 − 1,200 − 120 = 4,680. ✓  _(matsne 4280127; PwC)_

### Test suite

**Test 1:** Country of Georgia, monthly gross GEL 1,000, employee aged 32 (mandatory). → Employee pension GEL 20, employer pension GEL 20, PIT GEL 200, net pay GEL 780. (1,000 − 200 − 20 = 780.)

**Test 2:** Monthly gross GEL 3,000 (annual GEL 36,000), aged 41, no opt-out. → Employee pension GEL 60, employer pension GEL 60, PIT GEL 600, net pay GEL 2,340. State share GEL 600/yr (480 + 120). (3,000 − 600 − 60 = 2,340.)

**Test 3:** Monthly gross GEL 6,000 (annual GEL 72,000), aged 29. → Employee pension GEL 120, employer pension GEL 120, PIT GEL 1,200, net pay GEL 4,680. State share GEL 840/yr (480 + 360, nothing above 60k). (6,000 − 1,200 − 120 = 4,680.)

**Test 4:** Self-employed, annual GEL 50,000, opted IN. → Pension 4% = GEL 2,000. State share GEL 740/yr (480 + 260). (4% × 50,000 = 2,000.)

**Test 5:** Self-employed, annual GEL 50,000, did NOT opt in. → No pension contribution due (voluntary, default off).

**Test 6:** Worker aged 62 at 1 Jan 2019 enactment. → Voluntary participant only; mandatory 2%+2% does NOT apply unless they elect in. Flag for reviewer (T2-1).

**Test 7:** Client mentions USD, the IRS, and Atlanta. → STOP. Wrong jurisdiction (U.S. state of Georgia). Refuse per R-GE-SC-1.

**Test 8:** Revenue Service debit referencing "VAT APR 2025." → Classify as VAT (18%), NOT a social/pension contribution.

### Prohibitions

- NEVER apply this skill to the U.S. state of Georgia — confirm the country (GEL, rs.ge, Pension Agency) first.
- NEVER model a health/unemployment/"social security" payroll contribution for Georgia — none exists.
- NEVER assume a state co-contribution above GEL 60,000 annual income — the state share is zero there.
- NEVER apply a ceiling to the employee/employer 2%+2% — only the state share is capped.
- NEVER treat self-employed participation as mandatory — it is voluntary (4%) only on election.
- NEVER quantify pension/PIT arrears or exact GEL fines without a Revenue Service / Pension Agency statement — flag as [RESEARCH GAP] and escalate.
- NEVER use progressive PIT brackets — Georgia's PIT is a flat 20%.
- NEVER present figures as definitive — label as estimated, pending reviewer sign-off, and direct the client to rs.ge / the Pension Agency.

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
