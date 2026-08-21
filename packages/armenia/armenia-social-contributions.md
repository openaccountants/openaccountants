---
name: armenia-social-contributions
description: Use this skill whenever asked about Armenia payroll social contributions and personal income tax for employees, individual entrepreneurs, or expatriates. Trigger on phrases like "Armenia payroll tax", "Armenian pension contribution", "funded pension 5% 10%", "military stamp duty Armenia", "Insurance Foundation for Servicemen", "Armenia social security", "how much PIT do I withhold in Armenia", "Armenian employer social tax", "mandatory health insurance Armenia", "SRC monthly payroll return", "net pay calculation Armenia", or any question about Armenian payroll withholding obligations. Also trigger when classifying bank statement transactions that relate to SRC tax payments, pension contributions, military stamp duty, or salary payments from Armenian banks (Ameriabank, Ardshinbank, Acba Bank, Inecobank, Converse Bank). This skill covers the flat 20% PIT, mandatory funded pension contribution, military stamp duty, the new mandatory health insurance contribution (effective Dec 2025/Jan 2026), the fact that the private sector has NO separate employer social tax, monthly filing deadlines, penalties, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Armenian payroll or social-contribution work.
version: 0.1
jurisdiction: AM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia Social Contributions & Payroll Withholding

## Armenia Social Contributions & Payroll Withholding Skill v0.1

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Armenia |
| Primary Legislation | Tax Code of the Republic of Armenia (effective 1 Jan 2018, as amended) — ARLIS arlis.am/en/acts/205620 |
| Supporting Legislation | Law on Funded Pensions; Law on the Insurance Foundation for Servicemen (military stamp duty); Law on Universal/Mandatory Health Insurance |
| Tax Authority | State Revenue Committee of the Republic of Armenia (SRC) — e-filing at src.am |
| Currency | AMD only |
| Personal income tax | Flat 20% on gross employment income, no allowance, no brackets (effective 1 Jan 2023) — PwC |
| Employer separate social tax | NONE — private sector has no employer-paid social security contribution; employer withholds employee amounts only — PwC / Vardanyan & Partners |
| Funded pension (employee) | 5% of gross if gross < AMD 500,000; else 10% of gross − AMD 25,000, capped — PwC |
| Funded pension max contribution | AMD 87,500/month (base capped at AMD 1,125,000 = 15× min wage) — PwC |
| Military stamp duty (employee) | AMD 1,000/month if gross ≤ AMD 1,000,000; AMD 15,000/month if > AMD 1,000,000 (from Dec 2025) — PwC / Vardanyan |
| Mandatory health insurance (employee) | AMD 4,800/month (gross 200,001–500,000); AMD 10,800/month (gross > 500,000); exempt ≤ 200,000 (from 25 Dec 2025) — PwC |
| Minimum monthly wage | AMD 75,000 (effective 1 Jan 2023, unchanged through 2025/2026) — tradingeconomics / arka.am |
| Monthly filing + payment deadline | 20th day of the month following the reporting month, via SRC e-portal — SRC / Vardanyan |
| Validated by | Pending — requires sign-off by an Armenian licensed tax adviser |
| Validation date | Pending |

- **Pension birth-date eligibility** — Mandatory funded pension applies only to employees born on or after 1 January 1974. Those born before are exempt.  _(PwC)_

**Payroll deduction overview (employees, private sector):**

**Payroll deduction overview (employees, private sector)**

| Item | Payer | Rate / amount | Authority |
| --- | --- | --- | --- |
| Personal income tax (PIT) | Employee (withheld) | 20% flat of gross | PwC |
| Funded pension contribution | Employee (withheld) | 5% (< 500k) or 10% − 25,000 (≥ 500k), capped 87,500 | PwC |
| Military stamp duty | Employee (withheld) | AMD 1,000 (≤ 1,000,000) or AMD 15,000 (> 1,000,000) | PwC / Vardanyan |
| Mandatory health insurance | Employee (withheld) | AMD 0 / 4,800 / 10,800 by band | PwC |
| Employer separate social tax | Employer | **AMD 0 — none** | PwC / Vardanyan |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown birth year | STOP — funded pension depends on birth date (on/after 1 Jan 1974). Do not compute pension without it |
| Unknown period (pre/post Dec 2025) | Assume the current two-tier military stamp + new health contribution apply only from Dec 2025/Jan 2026; flag pre-Dec-2025 periods for reviewer |
| Unknown employment status | Treat as an employee under an employment contract; individual-entrepreneur rules differ — flag |
| Unknown citizenship | Health insurance applies to Armenian citizens; for foreigners confirm with reviewer |
| Employer social tax line seen on statement | There is no employer social tax — treat as a misclassification and flag |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — Monthly gross employment income (AMD) and the employee's birth year (or confirmation born on/after 1 Jan 1974). Without birth year, STOP on the pension line. Do not compute the funded pension contribution.
- **Recommended** — The payroll period (month/year, to determine whether the Dec 2025/Jan 2026 changes apply), Armenian citizenship status (for health insurance), and whether the worker is an employee or an individual entrepreneur.
- **Ideal** — The SRC monthly unified payroll report, the employment contract, and bank statements showing salary credits and SRC remittances.

### Refusal catalogue

- **R-AM-SC-1** — Trigger: employee birth year/decade not provided. Message: "Birth year is mandatory to compute the funded pension contribution. The mandatory funded pension applies only to employees born on or after 1 January 1974; those born earlier are exempt. Cannot compute the pension line without this information."  _(R-AM-SC-1)_
- **R-AM-SC-2** — Trigger: the payroll period is before December 2025, or it is ambiguous whether the new military-stamp two-tier schedule and the new health insurance contribution apply. Message: "The two-tier military stamp duty (AMD 1,000 / 15,000) and the mandatory health insurance contribution take effect from December 2025 / January 2026. Earlier periods used a different (multi-tier) military stamp schedule and had no health contribution. Escalate the exact go-live date to a reviewer before computing pre-2026 periods. [RESEARCH GAP — reviewer to confirm exact effective date]"  _(R-AM-SC-2)_
- **R-AM-SC-3** — Trigger: the worker is an individual entrepreneur, not an employee. Message: "Individual-entrepreneur funded pension, military stamp duty, and health insurance use annual-income formulas that differ from the employee withholding rules, and some figures rest on secondary sources only. Escalate to a reviewer. [RESEARCH GAP — IE military stamp AMD 12,000/120,000 and IE health AMD 129,600 are secondary-source only]"  _(R-AM-SC-3)_
- **R-AM-SC-4** — Trigger: the employee is a foreign citizen and the health insurance line is in question. Message: "The new mandatory health insurance contribution is documented for Armenian citizens employed under employment contracts. Application to foreign citizens is not confirmed. Escalate to a reviewer. [RESEARCH GAP — reviewer to confirm foreign-citizen health insurance treatment]"  _(R-AM-SC-4)_
- **R-AM-SC-5** — Trigger: unpaid PIT or contributions from prior periods. Message: "Late-payment interest accrues at 0.075% per day (Tax Code Art. 401) up to 730 days, and late filing adds further penalties. Do not quantify arrears without the SRC account statement. Escalate to a licensed adviser."  _(R-AM-SC-5 / Tax Code Art. 401)_

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Armenian payroll and social contributions. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. PIT, pension, military stamp, and health-insurance remittances EXCLUDE from any VAT return classification — they are statutory withholding obligations remitted by the employer as tax agent, not business supplies.

### 3.1 SRC tax / contribution remittances (employer as tax agent)

**SRC tax / contribution remittances**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ՊԵԿ, SRC, STATE REVENUE COMMITTEE | EXCLUDE — SRC remittance | Monthly remittance of withheld PIT + contributions |
| ԵԿԱՄՏԱՀԱՐԿ, INCOME TAX, PIT, IIT | EXCLUDE — withheld 20% PIT | Final monthly withholding |
| ԿԵՆՍԱԹՈՇԱԿ, PENSION, FUNDED PENSION | EXCLUDE — funded pension contribution | Employee withholding |
| ԴՐՈՇՄԱՆԻՇ, MILITARY STAMP, STAMP DUTY | EXCLUDE — military stamp duty | Insurance Foundation for Servicemen |
| ԱՌՈՂՋԱՊԱՀՈՒԹՅՈՒՆ, HEALTH INSURANCE | EXCLUDE — mandatory health contribution | From Dec 2025 |

### 3.2 Remittances appearing on specific Armenian banks

**Remittances appearing on specific Armenian banks**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Ameriabank | "SRC TAX PAYMENT" or "ՊԵԿ" | EXCLUDE — SRC remittance |
| Ardshinbank | "STATE BUDGET" or "INCOME TAX" | EXCLUDE — SRC remittance |
| Acba Bank | "ՊԵԿ" or "TAX/SOCIAL PAYMENT" | EXCLUDE — SRC remittance |
| Inecobank | "SRC" or "PENSION CONTRIBUTION" | EXCLUDE — SRC remittance |
| Converse Bank | "STATE REVENUE COMMITTEE" | EXCLUDE — SRC remittance |

### 3.3 Salary and payroll (exclude from contribution classification)

**Salary and payroll patterns**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ԱՇԽԱՏԱՎԱՐՁ, SALARY, WAGE (outgoing) | EXCLUDE — payroll expense (net pay) | Net of all withholdings |
| SALARY, WAGE (incoming) | EXCLUDE — employment income received | Net pay credited to employee |

### 3.4 Items that are NOT employee social contributions (do not confuse)

**Items that are NOT employee social contributions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EMPLOYER SOCIAL TAX, SOC TAX | FLAG — Armenia has NO employer social tax | Likely a misclassification; escalate |
| VAT, ԱԱՀ | EXCLUDE — VAT remittance, not a payroll contribution | Separate regime |
| CIT, PROFIT TAX (18%) | EXCLUDE — corporate income tax, not payroll | Separate regime |
| DIVIDEND, ROYALTY, INTEREST WHT | EXCLUDE — other withholding taxes | Not employee social contributions |

### 3.5 Pension / benefit payments received (not contributions)

**Pension / benefit payments received**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION RECEIVED, ԹՈՇԱԿ (incoming) | EXCLUDE — pension income received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical Armenian software company and its employees, all assuming a period from December 2025 onward (new health contribution and two-tier military stamp in force). All employees assumed born on/after 1 Jan 1974 (pension applies) and Armenian citizens, unless stated.

### Example 1 -- Standard mid-range salary, gross AMD 300,000

**Input line:**
`05.01.2026 ; ARMSOFT LLC SALARY ; CREDIT ; NET PAY DEC 2025 ; +219,200 ; AMD`

**Reasoning:**
Gross AMD 300,000. PIT = 20% × 300,000 = AMD 60,000. Pension: gross < 500,000 → 5% × 300,000 = AMD 15,000. Military stamp: gross ≤ 1,000,000 → AMD 1,000. Health: gross in band 200,001–500,000 → AMD 4,800. Total withheld = 60,000 + 15,000 + 1,000 + 4,800 = AMD 80,800. Net = 300,000 − 80,800 = **AMD 219,200**. Matches the credit. Salary credit (pattern 3.3) — exclude from VAT.

**Classification:** EXCLUDE — net employment income received. Withholdings remitted by employer to SRC.

### Example 2 -- Higher salary above pension threshold, gross AMD 600,000

**Input line:**
`05.01.2026 ; ARMSOFT LLC SALARY ; CREDIT ; NET PAY DEC 2025 ; +433,200 ; AMD`

**Reasoning:**
Gross AMD 600,000. PIT = 20% × 600,000 = AMD 120,000. Pension: gross ≥ 500,000 → 10% × 600,000 − 25,000 = 60,000 − 25,000 = AMD 35,000 (base below the AMD 1,125,000 cap). Military stamp: gross ≤ 1,000,000 → AMD 1,000. Health: gross > 500,000 → AMD 10,800. Total withheld = 120,000 + 35,000 + 1,000 + 10,800 = AMD 166,800. Net = 600,000 − 166,800 = **AMD 433,200**. Matches.

**Classification:** EXCLUDE — net employment income received.

### Example 3 -- High earner above all caps, gross AMD 1,500,000

**Input line:**
`05.01.2026 ; ARMSOFT LLC SALARY ; CREDIT ; NET PAY DEC 2025 DIRECTOR ; +1,086,700 ; AMD`

**Reasoning:**
Gross AMD 1,500,000. PIT = 20% × 1,500,000 = AMD 300,000. Pension: base capped at AMD 1,125,000 → 10% × 1,125,000 − 25,000 = 112,500 − 25,000 = AMD 87,500 (the statutory maximum). Military stamp: gross > 1,000,000 → AMD 15,000. Health: gross > 500,000 → AMD 10,800. Total withheld = 300,000 + 87,500 + 15,000 + 10,800 = AMD 413,300. Net = 1,500,000 − 413,300 = **AMD 1,086,700**. Matches.

**Classification:** EXCLUDE — net employment income received. Pension at statutory max AMD 87,500.

### Example 4 -- Low earner exempt from health, gross AMD 200,000

**Input line:**
`05.01.2026 ; ARMSOFT LLC SALARY ; CREDIT ; NET PAY DEC 2025 JUNIOR ; +149,000 ; AMD`

**Reasoning:**
Gross AMD 200,000. PIT = 20% × 200,000 = AMD 40,000. Pension: gross < 500,000 → 5% × 200,000 = AMD 10,000. Military stamp: gross ≤ 1,000,000 → AMD 1,000. Health: gross ≤ 200,000 → **exempt (AMD 0)**. Total withheld = 40,000 + 10,000 + 1,000 = AMD 51,000. Net = 200,000 − 51,000 = **AMD 149,000**. Matches. Note the AMD 200,000 health threshold is the upper edge of the exempt band (exempt if ≤ 200,000).

**Classification:** EXCLUDE — net employment income received. No health contribution (at/under threshold).

### Example 5 -- Employee born before 1 Jan 1974 (pension-exempt), gross AMD 300,000

**Input line:**
`05.01.2026 ; ARMSOFT LLC SALARY ; CREDIT ; NET PAY DEC 2025 SENIOR ; +234,200 ; AMD`

**Reasoning:**
Employee born 1968 → exempt from the mandatory funded pension. Gross AMD 300,000. PIT = 20% × 300,000 = AMD 60,000. Pension: **AMD 0 (born before 1 Jan 1974)**. Military stamp: gross ≤ 1,000,000 → AMD 1,000. Health: gross 200,001–500,000 → AMD 4,800. Total withheld = 60,000 + 0 + 1,000 + 4,800 = AMD 65,800. Net = 300,000 − 65,800 = **AMD 234,200**. Matches. Contrast with Example 1 (same gross, but pension-eligible): the AMD 15,000 difference is the omitted pension contribution.

**Classification:** EXCLUDE — net employment income received. Pension omitted (birth date before 1 Jan 1974).

### Example 6 -- SRC monthly remittance (employer remitting withheld amounts)

**Input line:**
`20.01.2026 ; STATE REVENUE COMMITTEE ; DEBIT ; ՊԵԿ MONTHLY PAYROLL DEC 2025 ; -1,234,000 ; AMD`

**Reasoning:**
Matches "STATE REVENUE COMMITTEE" / "ՊԵԿ" (pattern 3.1). This is the employer remitting the aggregate withheld PIT + funded pension + military stamp + health insurance for all staff for December 2025, due by the 20th of the following month. It is a remittance of amounts already withheld from employees, not a business expense or VAT item. The constituent lines should reconcile to the sum of each employee's withholdings on the SRC monthly report.

**Classification:** EXCLUDE — SRC remittance (employer as tax agent). Reconcile to the monthly payroll report.

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and all required inputs are available. Apply exactly as written. All figures per PwC Worldwide Tax Summaries (Armenia) and Vardanyan & Partners unless marked otherwise.

### Rule 1 -- Personal income tax is a flat 20%

- **Personal income tax rate** — 20% percent (Flat on gross, no personal allowance, no brackets, effective 1 Jan 2023. Employer is tax agent and applies final monthly withholding.)  _(PwC)_

### Rule 2 -- No separate employer social tax

- **No employer social tax** — Armenia's private sector has no separate employer-paid social security contribution. The employer only withholds and remits employee amounts. Never add an employer social-tax line for private-sector employers.  _(PwC / Vardanyan & Partners)_

### Rule 3 -- Funded pension contribution (employees)

- **Funded pension contribution formula** — if gross_monthly < 500,000: pension = 0.05 × gross_monthly else: base = min(gross_monthly, 1,125,000)      # base ceiling = 15 × min wage 75,000 pension = 0.10 × base − 25,000             # max 87,500 at base = 1,125,000 Applies only to employees born on or after 1 January 1974; those born earlier are exempt. There is no separate employer pension share — the state co-finances from the budget.  _(PwC)_

### Rule 4 -- Pension base ceiling and maximum

- **Pension base ceiling and maximum** — The pension calculation base is capped at AMD 1,125,000/month (15 × the AMD 75,000 minimum wage), giving a maximum employee contribution of AMD 87,500/month (10% × 1,125,000 − 25,000).  _(PwC)_

### Rule 5 -- Military stamp duty (Insurance Foundation for Servicemen), employees

- **Military stamp duty** — Two-tier, from December 2025: AMD 1,000/month if monthly gross ≤ AMD 1,000,000; AMD 15,000/month if gross > AMD 1,000,000. Withheld monthly by the employer. (Replaced the prior multi-tier AMD 1,500–15,000 schedule.)  _(PwC / Vardanyan)_

### Rule 6 -- Mandatory health insurance contribution (employees), from 25 Dec 2025

- **Mandatory health insurance contribution formula** — For Armenian citizens under employment contracts: if gross_monthly <= 200,000:      health = 0          # exempt elif gross_monthly <= 500,000:    health = 4,800      # band 200,001–500,000 else:                             health = 10,800     # gross > 500,000 Effective from 25 December 2025 per PwC (some secondary sources say first payroll January 2026). [RESEARCH GAP — reviewer to confirm exact go-live and any later phase-in for sub-AMD-200,000 earners]  _(PwC)_

### Rule 7 -- Net pay formula (private-sector employee)

- **Net pay formula** — net_pay = gross − PIT − funded_pension − military_stamp − health_insurance PIT = 0.20 × gross

### Rule 8 -- Monthly filing and remittance deadline

- **Monthly filing and remittance deadline** — File the SRC monthly unified payroll / income-tax & social-payment report and remit all withheld amounts (PIT, pension, stamp, health) via the SRC e-portal by the 20th day of the month following the reporting month.  _(SRC / Vardanyan)_

### Rule 9 -- Other withholding-tax rates (context, not employee social contributions)

- **Other withholding-tax rates** — Royalties 10%; interest 20% (from 1 Jan 2023); property lease income 10% (plus an additional 10% if annual lease income exceeds AMD 60,000,000); dividends 5% (refundable if reinvested in the same entity within the tax year).  _(PwC)_

### Rule 10 -- Annual personal income tax declaration

- **Annual personal income tax declaration** — Required only for income not taxed at source. For FY2025 the deadline is 1 November 2026; from 2027 the window is 2 March – 1 July of the following year.  _(PwC)_

### Rule 11 -- Minimum monthly wage

- **Minimum monthly wage** — AMD 75,000/month AMD (Effective 1 Jan 2023, unchanged through 2025 and 2026; a planned rise to AMD 85,000 for 2026 was discussed but not enacted as of early 2026. Used as the basis for the pension base ceiling (15× = 1,125,000).)  _(tradingeconomics / arka.am)_

## Section 6 -- Tier 2 catalogue

When payroll data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 -- Period straddling the December 2025 reform

- **Period straddling reform** — Trigger: payroll period spans late 2025, or it is unclear whether the new military-stamp two-tier schedule and health contribution apply. Issue: Pre-December-2025 periods used the prior multi-tier military stamp duty (AMD 1,500–15,000) and had no mandatory health insurance contribution. The exact go-live of both items is documented mainly by PwC/Vardanyan, not directly from the SRC text. Action: Flag for reviewer. Confirm the effective date against the SRC/arlis.am Tax Code before computing affected periods. [RESEARCH GAP — reviewer to confirm exact effective date]

### T2-2 -- Individual entrepreneur (sole proprietor) contributions

- **Individual entrepreneur contributions** — Trigger: the worker is an individual entrepreneur, not an employee under an employment contract. Issue: IE pension is annual-income based (5% if annual basic income ≤ AMD 6,000,000; else 10% of income − AMD 300,000). IE military stamp is reportedly AMD 12,000/year (annual income ≤ AMD 12,000,000) or AMD 120,000/year (> AMD 12,000,000) from January 2026 — secondary source only. IE health insurance is reportedly AMD 129,600/year for 2025 income ≥ AMD 2,400,001, due by 20 April — verify. Action: Flag for reviewer. [RESEARCH GAP — IE military stamp and IE health figures are secondary-source only]

### T2-3 -- Foreign-citizen employees

- **Foreign-citizen employees** — Trigger: the employee is a foreign citizen. Issue: Funded pension applies to Armenian and foreign citizens born on/after 1 Jan 1974, but health insurance is documented for Armenian citizens; foreign-citizen treatment is unconfirmed. Public-sector employees and those not employed as of 1 July 2014 cannot opt out of the pension. Action: Flag for reviewer to confirm citizenship-specific treatment. [RESEARCH GAP — reviewer to confirm foreign-citizen health insurance treatment]

### T2-4 -- Pension opt-in/opt-out and birth-date edge cases

- **Pension opt-in/opt-out and birth-date edge cases** — Trigger: employee born close to 1 Jan 1974, or claims a pension opt-out. Issue: Those born before 1 Jan 1974 are exempt; public-sector employees and those not employed as of 1 July 2014 cannot opt out. Edge cases around opt-in/opt-out require confirmation. Action: Flag for reviewer. Do not apply or omit the pension contribution on assumption alone.

### T2-5 -- Pension formula wording above AMD 500,000

- **Pension formula wording above AMD 500,000** — Trigger: gross at or above AMD 500,000. Issue: The formula above AMD 500,000 is sometimes worded as "10% of the maximum threshold − AMD 25,000." The operative reading is 10% of gross (subject to the AMD 1,125,000 base ceiling) − AMD 25,000, capped at AMD 87,500. Action: Apply the operative reading; flag any case where a third-party computation diverges.

### T2-6 -- Arrears, penalties, and the "stamp tax" conflict

- **Arrears, penalties, and the stamp tax conflict** — Trigger: unpaid contributions, or a query about whether Armenia has a stamp tax. Issue: PwC's corporate page states Armenia "does not have stamp taxes," but the individual page, Vardanyan, and other guides confirm the military insurance stamp duty (a stamp fee to the Insurance Foundation for Servicemen) is withheld from payroll. Treat it as a mandatory payroll deduction, not a classic stamp tax. Late-payment interest is 0.075%/day up to 730 days. Action: Treat the military stamp as a payroll deduction. Do not quantify arrears without the SRC statement; escalate to a licensed adviser.

## Section 7 -- Excel working paper template

When producing an Armenian payroll withholding computation, structure the working paper as follows:

```
ARMENIA PAYROLL WITHHOLDING -- WORKING PAPER
Client / Employer: [name]
Employee: [name]
Period (month/year): [____]   (confirm Dec-2025+ for new health/military rules)
Prepared: [date]

INPUT DATA
  Monthly gross income (AMD):        [____]
  Birth year:                        [____]
  Born on/after 1 Jan 1974:          [YES/NO]   -> pension applies?
  Armenian citizen:                  [YES/NO]   -> health insurance applies?
  Employee or Individual Entrepreneur: [EMP / IE]

COMPUTATION (private-sector employee)
  PIT (20% × gross):                 AMD [____]
  Funded pension:
    if gross < 500,000:  5% × gross  AMD [____]
    if gross >= 500,000: 10% × min(gross,1,125,000) − 25,000 (max 87,500)  AMD [____]
    (AMD 0 if born before 1 Jan 1974)
  Military stamp duty:
    1,000 if gross <= 1,000,000; else 15,000   AMD [____]
  Health insurance (from Dec 2025):
    0 if gross <= 200,000;
    4,800 if 200,001–500,000;
    10,800 if > 500,000                         AMD [____]
  Total withheld:                    AMD [____]
  NET PAY (gross − total withheld):  AMD [____]

EMPLOYER SOCIAL TAX
  Private sector:                    AMD 0 (none)

FILING
  SRC monthly report + remittance due: 20th of following month

REVIEWER FLAGS
  [List any Tier 2 flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How payroll items appear on Armenian bank statements

**Ameriabank:**
- Salary credit: "SALARY", "ԱՇԽԱՏԱՎԱՐՁ", employer name + "NET PAY"
- SRC remittance (employer): "SRC TAX PAYMENT", "ՊԵԿ", "STATE BUDGET"
- Timing of SRC remittance: by the 20th of the month following the payroll month

**Ardshinbank:**
- Salary credit: "SALARY", employer name
- SRC remittance: "STATE BUDGET", "INCOME TAX", "ՊԵԿ"

**Acba Bank / Inecobank / Converse Bank:**
- SRC remittance: "ՊԵԿ", "SRC", "STATE REVENUE COMMITTEE", "PENSION CONTRIBUTION"

**Key identification tips:**
1. Employee salary credits are the net figure (after PIT, pension, military stamp, health) — never the gross.
2. Employer SRC remittances are outgoing (DEBIT), aggregate across staff, and dated around the 20th of the following month.
3. There is no separate employer social-tax line — if one appears, flag it as a likely misclassification.
4. Do not confuse SRC payroll remittances with VAT (ԱԱՀ), corporate profit tax (18%), or dividend/royalty/interest WHT.
5. Armenian-script references: ՊԵԿ (SRC), եկամտահարկ (income tax), կենսաթոշակ (pension), դրոշմանիշ (stamp), առողջապահություն (health).

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for salary credits** — identify net pay amounts and the employer.
2. **Scan for SRC remittances** — identify outgoing payments matching Section 3.1/3.2 patterns around the 20th of each month.
3. **Reverse-engineer gross from net (employee, born ≥ 1974, Armenian citizen, Dec 2025+):** for a net figure, test the bracket — net AMD 219,200 implies gross AMD 300,000 (Example 1); net AMD 433,200 implies gross AMD 600,000 (Example 2). The mapping is not always unique, so confirm against the payslip.
4. **Flag for reviewer:** "Gross/withholding figures derived from bank-statement net amounts only. Birth year, citizenship, and period (pre/post Dec 2025) have not been independently verified. Reviewer must confirm before relying on the computation."

### Calculation examples (Dec 2025+, employee born ≥ 1974, Armenian citizen)

**Calculation examples (Dec 2025+, employee born ≥ 1974, Armenian citizen)**  _(PwC Worldwide Tax Summaries (Armenia) and Vardanyan & Partners)_

| Gross (AMD) | PIT (20%) | Pension | Military stamp | Health | Total withheld | Net pay |
| --- | --- | --- | --- | --- | --- | --- |
| 75,000 (min wage) | 15,000 | 3,750 | 1,000 | 0 | 19,750 | 55,250 |
| 200,000 | 40,000 | 10,000 | 1,000 | 0 | 51,000 | 149,000 |
| 300,000 | 60,000 | 15,000 | 1,000 | 4,800 | 80,800 | 219,200 |
| 600,000 | 120,000 | 35,000 | 1,000 | 10,800 | 166,800 | 433,200 |
| 1,000,000 | 200,000 | 75,000 | 1,000 | 10,800 | 286,800 | 713,200 |
| 1,500,000 | 300,000 | 87,500 | 15,000 | 10,800 | 413,300 | 1,086,700 |

Source for all rates/thresholds: PwC Worldwide Tax Summaries (Armenia) and Vardanyan & Partners. Pension at 1,000,000 = 10% × 1,000,000 − 25,000 = 75,000 (base below the 1,125,000 cap). Military stamp at exactly 1,000,000 = AMD 1,000 (≤ 1,000,000 tier).

### Thresholds and key amounts

**Thresholds and key amounts**  _(PwC / Vardanyan / tradingeconomics / arka.am)_

| Item | Value | Source |
| --- | --- | --- |
| PIT flat rate | 20% of gross | PwC |
| Pension 5%→10% threshold | AMD 500,000/month gross | PwC |
| Pension base ceiling | AMD 1,125,000/month (15 × AMD 75,000) | PwC |
| Pension fixed deduction (10% formula) | AMD 25,000 | PwC |
| Pension maximum contribution | AMD 87,500/month | PwC |
| Pension birth-date eligibility | Born on/after 1 Jan 1974 | PwC |
| Military stamp band break | AMD 1,000,000/month (1,000 vs 15,000) | PwC / Vardanyan |
| Health insurance entry threshold | Gross > AMD 200,000/month | PwC |
| Health insurance band break | AMD 500,000/month (4,800 vs 10,800) | PwC |
| Minimum monthly wage | AMD 75,000 | tradingeconomics / arka.am |
| Property lease surcharge trigger | Annual lease income > AMD 60,000,000 | PwC |
| Corporate income tax (context) | 18% on net profit | Vardanyan / PwC |

### Penalties

**Penalties**  _(Tax Code / mondaq / Vardanyan)_

| Penalty | Rate / detail | Source |
| --- | --- | --- |
| Late payment of tax / contributions | 0.075% of unpaid amount per day (Tax Code Art. 401; ~27% annualized), up to 730 days (2 years) | Tax Code / mondaq / Vardanyan |
| Late filing of a return/declaration | 5% of unpaid tax per 15-day period of delay, in addition to the 0.075%/day late-payment interest. [RESEARCH GAP — cap not confirmed from primary text] | mondaq / Vardanyan |

### Forms and deadlines

**Forms and deadlines**  _(SRC / Vardanyan / PwC)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Monthly unified payroll / income-tax & social-payment report (SRC e-portal) | Report and remit withheld PIT, funded pension, military stamp, health insurance | 20th of the following month | SRC / Vardanyan |
| Annual personal income tax declaration | Self-declaration of income NOT taxed at source | FY2025: 1 Nov 2026; from 2027: 2 Mar – 1 Jul of following year | PwC |

### Individual entrepreneur summary (verify before use)

- Pension: 5% of gross if annual basic income ≤ AMD 6,000,000 (paid monthly); else 10% of income − AMD 300,000. — PwC
- Military stamp: AMD 12,000/year (annual income ≤ AMD 12,000,000) or AMD 120,000/year (> AMD 12,000,000), from January 2026. [RESEARCH GAP — secondary source only]
- Health insurance: AMD 129,600/year for 2025 income ≥ AMD 2,400,001, due by 20 April. [RESEARCH GAP — verify]

### Test suite

**Test 1:** Gross AMD 300,000, born 1990, Armenian citizen, Dec 2025+. → PIT 60,000; pension 15,000; military 1,000; health 4,800; total 80,800; **net 219,200**.

**Test 2:** Gross AMD 600,000, born 1985. → PIT 120,000; pension (10%×600,000−25,000) 35,000; military 1,000; health 10,800; total 166,800; **net 433,200**.

**Test 3:** Gross AMD 1,500,000, born 1980. → PIT 300,000; pension capped 87,500; military 15,000; health 10,800; total 413,300; **net 1,086,700**.

**Test 4:** Gross AMD 200,000, born 1992. → PIT 40,000; pension 10,000; military 1,000; health 0 (≤ threshold); total 51,000; **net 149,000**.

**Test 5:** Gross AMD 300,000, born 1968 (before 1 Jan 1974). → PIT 60,000; pension **0**; military 1,000; health 4,800; total 65,800; **net 234,200**.

**Test 6:** Gross AMD 75,000 (min wage), born 1995. → PIT 15,000; pension 3,750; military 1,000; health 0; total 19,750; **net 55,250**.

**Test 7:** Gross AMD 1,000,000, born 1988. → PIT 200,000; pension (10%×1,000,000−25,000) 75,000; military 1,000 (≤ 1,000,000 tier); health 10,800; total 286,800; **net 713,200**.

**Test 8:** Private-sector employer remittance for one AMD 300,000 employee (born 1990). → Employer social tax **0**; remits PIT 60,000 + pension 15,000 + military 1,000 + health 4,800 = AMD 80,800 to SRC by the 20th of the following month.

### Prohibitions

- **No employer separate social-tax line for private-sector employers** — NEVER add an employer separate social-tax line for private-sector employers — Armenia has none.  _(unsure)_
- **Pension requires birth year knowledge** — NEVER compute the funded pension without knowing the employee's birth year (eligibility hinges on birth on/after 1 Jan 1974).  _(unsure)_
- **No pre-Dec 2025 application without confirmation** — NEVER apply the two-tier military stamp duty or the health insurance contribution to periods before December 2025 without reviewer confirmation.  _(unsure)_
- **Never report gross as net pay** — NEVER report the gross figure as net pay — salary credits on statements are net of all withholdings.  _(unsure)_
- **Military stamp is a mandatory payroll deduction** — NEVER treat the military stamp duty as a classic stamp tax or omit it because one PwC page says Armenia "has no stamp taxes" — it is a mandatory payroll deduction.  _(unsure)_
- **IE rules differ from employee withholding** — NEVER apply employee withholding formulas to an individual entrepreneur — the IE annual-income rules differ.  _(unsure)_
- **Pension cap enforcement** — NEVER exceed the pension maximum of AMD 87,500/month or compute pension on a base above AMD 1,125,000/month.  _(unsure)_
- **No arrears quantification without SRC statement** — NEVER quantify arrears or penalties without the SRC account statement — escalate to a licensed adviser.  _(unsure)_
- **Figures are estimates only** — NEVER present figures as definitive — label as estimated and direct the client to their SRC account and payslip, given the very recent Dec 2025/Jan 2026 changes.  _(unsure)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. This is a Tier-2 (research-verified) skill: several December 2025 / January 2026 figures rest on PwC and Vardanyan & Partners guides rather than directly fetched SRC/arlis.am text, and items marked "[RESEARCH GAP — reviewer to confirm]" require independent confirmation.

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
