---
name: ethiopia-payroll
description: Use this skill whenever asked about Ethiopia payroll processing for employed persons. Trigger on phrases like "Ethiopia payroll", "Ethiopian PAYE", "employment income tax Ethiopia", "Schedule A tax Ethiopia", "pension contribution Ethiopia", "POESSA", "social security Ethiopia", "Form 17 Ethiopia", "net salary Ethiopia", "ETB payroll", "gross to net Ethiopia", "withholding tax Ethiopia", "salary calculation Ethiopia", "Proclamation 1395/2025", "employer pension Ethiopia 11%", or any question about computing employee pay, employment income tax withholding, or pension/social-security contributions for Ethiopia-based employees. This skill covers Schedule A PAYE withholding (post-7-July-2025 brackets), private-organisation pension contributions (employee 7% / employer 11%), filing obligations, and remittance deadlines. ALWAYS read this skill before processing any Ethiopia payroll.
version: 0.2
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Payroll

## Who this applies to

Employers paying employment income in Ethiopia, in the tax year 8 July to 7 July. Employment bands apply to income derived from 8 July 2025 onward (Proc. 1395/2025 art. 4). Work permit bodies report foreign employees to the Tax Authority (art. 12(7)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Employment income, monthly: 0 to 2,000 / 2,001 to 4,000 / 4,001 to 7,000 / 7,001 to 10,000 / 10,001 to 14,000 / over 14,000 (art. 11) | 0% / 15% / 20% / 25% / 30% / 35% | 2026 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf |
| Pension: employer 11%, employee 7%, on regular-hours monthly salary before deductions (arts 2(7), 10) | 18% total | 2026 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf |
| Employer pension or provident contribution exempt to 15% of monthly salary (Proc. 979/2016 exemption list) | 15% | 2026 | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf |

## The base

Apply the bands monthly to employment income. Each band taxes only its slice. Quick deductions 300, 500, 850, 1,350 and 2,050 give the same result; they are arithmetic, not law.

## Deadlines and filing

1. Withhold on each salary payment.
2. Pay and declare withheld tax within 30 days after the month of payment, on the approved form (Proc. 979/2016 art. 97 in the print read).
3. Pay pension within 30 days of the last day of the salary month (Proc. 1268/2022 art. 12(2)). Pagumen dates need checking against the Ethiopian calendar.
4. Give each employee the withholding receipt; for employees with no filing duty it stands as their assessment (art. 87(3)).
5. Employees with two employers declare within 30 days of year end (art. 87(2)).

## Penalties and interest

| Failure | Penalty | Tax year | Official URL |
|---|---|---|---|
| Not registered when required (art. 101, now 118) | 25% of tax due in the period; ETB 1,000 a month if none and if higher | 2026 | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf |
| Late declaration (art. 104, now 121) | 5% of unpaid tax per period, to 25%; first-period cap ETB 50,000; if no tax, ETB 10,000 a period | 2026 | same |
| Late payment (art. 105, now 122) | 5% first month, 2% each later month; never above the tax | 2026 | same |
| Tax not withheld or remitted (art. 106, now 123) | 10% of the tax, plus ETB 2,000 on each responsible officer, where the added condition in 1434/2026 is met | 2026 | https://www.mor.gov.et/domestic-law-proclamation |
| Understatement (art. 109, now 126) | 10%, then 30% second time, 40% third time onward | 2026 | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf |
| Records not kept (art. 102, now 119) | 20% of tax; if none, ETB 20,000 income tax or ETB 2,000 other tax a year | 2026 | same |
| Late-payment interest (art. 37) | highest commercial bank lending rate last quarter plus 15%, simple, daily | 2026 | same |
| Pension unpaid (Proc. 1268/2022 art. 12(4)) | bank deposit interest plus 5% a month, total capped | 2026 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf |

## Cross-border points

Non-diplomatic staff of embassies and international organisations are recorded through the Ministry of Foreign Affairs (art. 12(5), (6)). Foreign pension rules: see [social contributions](ethiopia-social-contributions.md).

## Two worked examples that recompute

Simple case: salary ETB 10,000, tax 1,650, employee pension 700.

```oa-check
name: Salary ETB 10,000
inputs:
  s: 10000
steps:
  - b15: (min(s, 4000) - 2000) * 0.15
  - b20: (min(s, 7000) - 4000) * 0.20
  - b25: (min(s, 10000) - 7000) * 0.25
  - b30: (min(s, 14000) - 10000) * 0.30
  - b35: max(s - 14000, 0) * 0.35
  - tax: b15 + b20 + b25 + b30 + b35
  - pension: s * 0.07
  - net: s - tax - pension
expected:
  tax: 1650.00
  pension: 700.00
  net: 7650.00
```

Edge case: salary ETB 20,000 reaches the top band.

```oa-check
name: Salary ETB 20,000
inputs:
  s: 20000
steps:
  - b15: (min(s, 4000) - 2000) * 0.15
  - b20: (min(s, 7000) - 4000) * 0.20
  - b25: (min(s, 10000) - 7000) * 0.25
  - b30: (min(s, 14000) - 10000) * 0.30
  - b35: max(s - 14000, 0) * 0.35
  - tax: b15 + b20 + b25 + b30 + b35
expected:
  tax: 4950.00
```

## Ask the client first

- Ethiopian citizen or foreign employee?
- Basic salary against allowances?
- Private organisation or public body?
- More than one employer?
- Pay dates and the month each salary belongs to?

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Income Tax (Amendment) Proclamation 1395/2025, Federal Negarit Gazette 31st Year No. 64 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf | 2026-11-01 | Whole text read (English column) |
| Federal Income Tax Proclamation 979/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf | 2026-11-01 | Declaration, payment, withholding and exemption articles read in Amharic; article numbers are those before the 1395/2025 renumbering |
| Federal Tax Administration Proclamation 983/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf | 2026-11-01 | Penalty articles and art. 37 read in Amharic |
| Tax Administration (Amendment) Proclamation 1434/2026, Federal Negarit Gazette 32nd Year No. 48, 30 July 2026, listed by the Ministry of Revenues | https://www.mor.gov.et/domestic-law-proclamation | 2026-11-01 | Whole text read; adds 17 to the penalty article numbers of 983/2016 |
| Private Organization Employees Pension Proclamation 1268/2022 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf | 2026-11-01 | Arts 2, 10 to 12 read |
| Ministry of Revenues forms list | https://www.mor.gov.et/forms | 2026-11-01 | Titles of the published forms read; the form boxes were not read |

Not yet confirmed: the Council of Ministers income tax regulation that sets the digital service tax rate (capped at 5%) was not found; the e-tax portal steps and the box numbers on the Ministry forms were not read, so no box numbers are given as law; whether the employee 7% reduces taxable income; the 1434/2026 condition on officer liability was read only in part; the cap wording in Proc. 1268/2022 art. 12(4) was read in part; the minimum wage, allowance and ceiling items in the retained notes below were not re-read.

### Retained working notes from the earlier version (not re-read against the law)

### Ethiopia Payroll Skill v0.1 (Tier 2 -- Sourced from the law)


### Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Federal Democratic Republic of Ethiopia |
| Currency | Ethiopian Birr (ETB) only |
| Standard pay frequency | Monthly |
| Tax year | Ethiopian fiscal year (8 July -- 7 July); note Ethiopian calendar lags Gregorian by ~7--8 days |
| Tax withholding system | PAYE under Schedule "A" -- employment income tax, withheld monthly by employer |
| Income tax authority | Ministry of Revenue (formerly ERCA -- Ethiopian Revenues and Customs Authority) |
| Pension / social security authority | Private Organisation Employees Social Security Agency (the pension fund administration); parallel public-servant scheme for government staff |
| Key legislation | Income Tax Proclamation as amended by Proclamation No. 1395/2025 (eff. 7 July 2025); Federal Tax Administration Proclamation No. 983/2016; Private Organisation Employees' Pension Proclamation |
| Monthly declaration form | Form 17 (monthly salary / withholding declaration) |
| Validated by | Pending -- requires sign-off by a licensed Ethiopian accountant |
| Skill version | 0.1 |


### Section 2 -- Employment Income Tax (PAYE / Schedule "A")

The employer withholds employment income tax monthly under Schedule "A". Employees whose only income is employment income do **NOT** file a personal return -- the employer's monthly withholding and remittance is final.

#### Monthly tax brackets (effective 7 July 2025, FY 2025/26)

**Monthly tax brackets (effective 7 July 2025, FY 2025/26)**

| Monthly taxable salary (ETB) | Marginal rate | Quick-deduction constant (ETB) |
| --- | --- | --- |
| 0 -- 2,000 | 0% (exempt) | 0 |
| 2,001 -- 4,000 | 15% | 300 |
| 4,001 -- 7,000 | 20% | 500 |
| 7,001 -- 10,000 | 25% | 850 |
| 10,001 -- 14,000 | 30% | 1,350 |
| Over 14,000 | 35% | 2,050 |

- **Quick-deduction constants derivation**, Derived arithmetically from the marginal brackets so that `tax = salary x rate - constant` reproduces the cumulative bracket tax exactly (see Section 11 self-check). These constants are not published in the gazetted text.  _((not confirmed))_

#### Key facts and 2025 reform changes


#### Computation method (per pay run)

- **PAYE computation formula**, taxable_salary  = gross taxable employment income for the month (cash salary + taxable allowances/benefits) PAYE            = taxable_salary x marginal_rate - quick_deduction_constant (apply the row whose range contains taxable_salary)
- **PAYE not cumulative**, PAYE is not cumulative across the year (unlike Malta's FSS) -- each month is computed standalone on that month's taxable salary.  _(Section 2)_

### Section 3 -- Pension / Social Security Contributions


#### Contribution rates

**Contribution rates**

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 7% | Basic salary |
| Employer | 11% | Basic salary |
| **Combined total** | **18%** | Basic salary |

- **Self-check combined pension rate**, employee 7% + employer 11% = 18% combined. Confirmed.

#### Coverage and mechanics

- The **employer remits both portions** (employee 7% withheld + employer 11%).
- Funds old-age pension, survivors', and work-injury / invalidity benefits.

#### Contribution ceiling



### Section 4 -- Conservative Defaults

**Section 4 -- Conservative Defaults**

| Input | Conservative default | Rationale |
| --- | --- | --- |
| Residency / source | Treat as **resident**, taxed on the stated employment income | Same Schedule A rates apply either way; no rate difference |
| Pension eligibility | Treat employee as an **Ethiopian citizen** (pension applies) unless told otherwise | Pension is mandatory for citizens; assuming it applies is the conservative (higher-cost) stance |
| Taxable vs non-taxable allowances | Treat all stated allowances as **taxable** unless a specific exemption is provided | Avoids understating PAYE |
| Pay frequency | Assume **monthly** | Standard Ethiopian practice |

Never present any computed figure as definitive -- always label it estimated and direct to a licensed Ethiopian accountant.

### Section 5 -- Required Inputs and Refusal Catalogue

#### Required inputs before any payroll computation

- **Required inputs list**, 1. **Gross monthly employment income** (ETB), with a breakdown of **basic salary vs allowances/benefits**. 2. Which allowances are **taxable** vs exempt (if any exemption is claimed). 3. Whether the employee is an **Ethiopian citizen** (or foreign national of Ethiopian origin) for pension eligibility. 4. Pay period (month/year). 5. Any non-employment income? (If yes -> employee may need to file separately; this skill covers employment income only.)

#### Refusal catalogue -- DO NOT compute; ask first

**Refusal catalogue -- DO NOT compute; ask first**

| Situation | Why refuse / pause |
| --- | --- |
| Only "gross salary" given, no basic-salary split | Pension base is basic salary; computing on gross over-deducts. Ask for the split. |
| Employee is a non-Ethiopian expat and pension treatment is unclear | Pension generally not available to expats; do not deduct 7%/11% without confirmation. |
| Request to compute the ETB 15,000 ceiling effect as if it were law | Ceiling is unconfirmed; do not present it as authoritative. |
| Request for the annual-equivalent bracket table as a definitive figure | Annual table not published; do not fabricate it. |
| Request for exact late-filing / late-payment penalty amounts | Penalty figures not in any primary source available; do not invent. |
| Request to treat the lowest band as 10% | Outdated pre-reform rate; refuse and use 15% (post-7-July-2025). |

### Section 6 -- Transaction / Payment Pattern Library

Deterministic mapping from posting context to bookkeeping treatment. Amounts are illustrative; classifications are the deliverable.

**Transaction / Payment Pattern Library table**

| Event | Debit | Credit |
| --- | --- | --- |
| Accrue gross salary | Salary expense (gross) | Net pay payable; PAYE payable; Pension payable (employee 7%) |
| Accrue employer pension (11%) | Pension expense (employer) | Pension payable (employer 11%) |
| Pay net salary to employee | Net pay payable | Bank |
| Remit PAYE to Ministry of Revenue | PAYE payable | Bank |
| Remit pension (18% combined) to the pension fund administration | Pension payable (7% + 11%) | Bank |

- **Treatment rules**, - Gross salary and employer pension (11%) are **expenses**. - Employee PAYE and employee pension (7%) are **liabilities withheld** -- they reduce net pay, not employer cost. - Net pay = gross taxable salary - PAYE - employee pension (7% of basic salary).

### Section 7 -- Worked Examples

All figures in **ETB**. Bank lines mimic realistic Ethiopian statement narrations (e.g. CBE = Commercial Bank of Ethiopia, Awash, Dashen, telebirr). PAYE uses Section 2 brackets; pension uses Section 3 (no ceiling).

#### Example 1 -- Low earner, fully exempt PAYE

- Basic salary = gross taxable = **ETB 2,000/month**.
- PAYE: salary is in 0--2,000 band -> **0% -> ETB 0**.
- Employee pension: 2,000 x 7% = **ETB 140**.
- Net pay = 2,000 - 0 - 140 = **ETB 1,860**.
- Employer pension: 2,000 x 11% = **ETB 220**.
- Employer total cost = 2,000 + 220 = **ETB 2,220**.

Bank line (net): `CBE TRANSFER DEBIT - DAMTEW W SALARY JUNE - 1,860.00` -> Net salary payment.

#### Example 2 -- Mid earner, 20% band

- Basic salary = gross taxable = **ETB 6,000/month**.
- PAYE: in 4,001--7,000 band -> 6,000 x 20% - 500 = 1,200 - 500 = **ETB 700**.
  - Cross-check by bracket: (4,000-2,000)x15% + (6,000-4,000)x20% = 300 + 400 = **700**. Reconciles.
- Employee pension: 6,000 x 7% = **ETB 420**.
- Net pay = 6,000 - 700 - 420 = **ETB 4,880**.
- Employer pension: 6,000 x 11% = **ETB 660**.
- Employer total cost = 6,000 + 660 = **ETB 6,660**.

Bank lines:
- `AWASH BANK PAYROLL CR - NETSALARY - 4,880.00` -> Net salary.
- `MOR PAYE REMIT FORM17 - 700.00` -> PAYE to Ministry of Revenue.
- `the pension fund administration PENSION 18% - 1,080.00` -> Pension remittance (420 + 660).

#### Example 3 -- Allowances split (taxable allowance, pension on basic only)

- Basic salary = **ETB 10,000**; taxable transport allowance = **ETB 2,000**. Gross taxable = **ETB 12,000**.
- PAYE on 12,000: in 10,001--14,000 band -> 12,000 x 30% - 1,350 = 3,600 - 1,350 = **ETB 2,250**.
  - Bracket cross-check: 300 + 600 + 750 + (12,000-10,000)x30% = 300+600+750+600 = 2,250. Reconciles.
- Employee pension on **basic only** (10,000): 10,000 x 7% = **ETB 700**.
- Net pay = 12,000 - 2,250 - 700 = **ETB 9,050**.
- Employer pension on basic only: 10,000 x 11% = **ETB 1,100**.
- Employer total cost = 12,000 + 1,100 = **ETB 13,100**.

Note: pension is on basic salary (10,000), NOT on the 2,000 allowance.

#### Example 4 -- High earner, top 35% band

- Basic salary = gross taxable = **ETB 30,000/month**.
- PAYE: over 14,000 -> 30,000 x 35% - 2,050 = 10,500 - 2,050 = **ETB 8,450**.
  - Bracket cross-check: cumulative tax at 14,000 = 2,850; plus (30,000-14,000)x35% = 5,600; total = **8,450**. Reconciles.
- Net pay = 30,000 - 8,450 - 2,100 = **ETB 19,450**.
- Employer pension: 30,000 x 11% = **ETB 3,300**.
- Employer total cost = 30,000 + 3,300 = **ETB 33,300**.


#### Example 5 -- Boundary at exactly ETB 7,000 (band edge)

- Gross taxable = **ETB 7,000** (top of the 20% band).
- PAYE: 7,000 x 20% - 500 = 1,400 - 500 = **ETB 900**.
  - Bracket cross-check: 300 + (7,000-4,000)x20% = 300 + 600 = 900. Reconciles.
- Employee pension: 7,000 x 7% = **ETB 490**.
- Net pay = 7,000 - 900 - 490 = **ETB 5,610**.
- Employer pension: 7,000 x 11% = **ETB 770**.

### Section 8 -- Filing and Remittance Obligations

**Section 8 -- Filing and Remittance Obligations**

| Item | Detail | Deadline |
| --- | --- | --- |
| Monthly declaration (Form 17) | Gross salaries, employer + employee pension, income tax withheld, net paid | Monthly |
| Pension remittance to the pension fund administration | Combined 18% (7% employee + 11% employer) | **Within 30 days** of deduction |
| Personal annual return | **Not required** for employees with only employment income -- employer withholding is final | N/A |


**Calendar note:** Ethiopia uses the Ethiopian calendar (~7--8 day lag from Gregorian); confirm the effective Gregorian due date when scheduling payments.


### Section 9 -- Employer Registration

- **No published de-minimis revenue/headcount threshold** for PAYE -- the obligation arises on employing staff. (not confirmed)

### Section 10 -- Penalties

Governed by the **Federal Tax Administration Proclamation No. 983/2016** (still in force):

**Penalties table**  _(Federal Tax Administration Proclamation No. 983/2016)_

| Article | Subject | Classification |
| --- | --- | --- |
| Art. 104 | Late filing of returns | High-level penalty |
| Art. 105 | Late payment of tax | Medium-level penalty |
| Art. 109 | Understatement of tax | Low-level penalty |

- **Statute of limitations**, 5 years years (from the filing date)



### Section 11 -- Minimum Wage

- **No national / private-sector statutory minimum wage** exists in Ethiopia (RemotePeople; WageIndicator).
- A **Wage Board** (government, employers, unions) is provided for under the Labour Proclamation to set/revise minimum wages periodically; **not yet operational for the private sector**.
- **Public sector only** (does NOT apply to private payroll): a long-standing federal reference of **ETB 420/month** (unchanged since ~2012); some sources report a civil-servant minimum raised toward the **ETB ~4,800/month** range. (not confirmed)

Source: RemotePeople -- Minimum wage Ethiopia; WageIndicator -- Ethiopia; Capital Ethiopia (July 2025).

### Section 12 -- Tier 1 Rules (deterministic -- always apply)


### Section 13 -- Tier 2 Catalogue (reviewer judgement required)

**Section 13 -- Tier 2 Catalogue (reviewer judgement required)**

| Question | Why it needs a reviewer |
| --- | --- |
| Is a particular allowance (transport, housing, per-diem) taxable or exempt? | Exemption treatment varies; not exhaustively published here. |
| Does an ETB 15,000 pension ceiling apply? | Unconfirmed; reviewer to check the pension fund administration directive. |
| Exact PAYE remittance day (end of month vs 8th)? | Source discrepancy; reviewer to confirm statute. |
| Quick-deduction constants vs gazetted text | Constants are derived, not statutory; reviewer to confirm. |
| Pension treatment for foreign nationals of Ethiopian origin | Optional scheme; case-specific. |
| Exact penalty / interest figures | Not in available primary sources. |
| Annual-equivalent bracket table | Not published; do not fabricate. |

### Section 14 -- Excel Working Paper Template

**Section 14 -- Excel Working Paper Template**

| Cell | Label | Formula / input |
| --- | --- | --- |
| B1 | Employee name | (input) |
| B2 | Pay period | (input) |
| B3 | Basic salary (ETB) | (input) |
| B4 | Taxable allowances (ETB) | (input) |
| B5 | Gross taxable salary | `=B3+B4` |
| B6 | PAYE marginal rate | lookup B5 against Section 2 table |
| B7 | PAYE quick-deduction constant | lookup B5 against Section 2 table |
| B8 | PAYE | `=MAX(0, B5*B6 - B7)` |
| B9 | Employee pension (7% of basic) | `=B3*0.07` |
| B10 | Net pay | `=B5 - B8 - B9` |
| B11 | Employer pension (11% of basic) | `=B3*0.11` |
| B12 | Combined pension to the pension fund administration | `=B9 + B11` |
| B13 | Employer total cost | `=B5 + B11` |

Note: pension formulas reference **basic salary (B3)**, not gross taxable (B5).

### Section 15 -- Bank Statement / Terminology Reading Guide

**Section 15 -- Bank Statement / Terminology Reading Guide**

| Term / narration | Meaning |
| --- | --- |
| ETB / Br | Ethiopian Birr |
| CBE | Commercial Bank of Ethiopia |
| Awash / Dashen / Abyssinia | Major Ethiopian commercial banks |
| telebirr | Ethio Telecom mobile-money wallet (common for net-pay disbursement) |
| MOR / ERCA | Ministry of Revenue (formerly Ethiopian Revenues and Customs Authority) -- PAYE payee |
| the pension fund administration | Private Organisation Employees Social Security Agency -- pension payee |
| Form 17 | Monthly salary withholding declaration |
| PAYE / Schedule A | Employment income tax withholding |
| "Pension 18%" / "the pension fund administration 18%" | Combined 7% + 11% pension remittance |
| Net salary / Selari / Demoz | Net pay to employee |

### Section 16 -- Onboarding Fallback

- **Onboarding fallback steps**, If the client cannot provide a clean basic-vs-allowance split or pension-eligibility confirmation: 1. Request the **employment contract** (states basic salary) and the latest **Form 17** if one exists. 2. Confirm **citizenship/residency** for pension eligibility. 3. In the interim, compute PAYE on the stated gross taxable figure and **flag** that pension may be mis-stated until the basic-salary split is confirmed. 4. Do not finalise or file until the reviewer signs off.

### Section 17 -- Reference Material

**Section 17 -- Reference Material**

| Item | Value | Source |
| --- | --- | --- |
| Pension remittance | Within 30 days of deduction | Secondary guides (not confirmed) |
| Minimum wage (private) | None | RemotePeople; WageIndicator |
| Effective date of reform | 7 July 2025 | Afriwise (Proc. 1395/2025) |

Primary sources:
- TaxDev (IFS) -- "Ethiopia's revised income tax explained".
- Afriwise -- Update on Income Tax (Amendment) Proclamation No. 1395/2025.
- Federal Tax Administration Proclamation No. 983/2016 (penalties).

### Section 18 -- Test Suite

Each test recomputes end-to-end. PAYE per Section 2; pension per Section 3 (no ceiling); net = gross taxable - PAYE - employee pension (7% of basic). Where gross = basic, pension base = gross.

1. **Gross taxable ETB 2,000, basic 2,000.** PAYE = 0 (exempt band). Employee pension = 140. Net = 2,000 - 0 - 140 = **1,860**. Employer pension = 220.
2. **Gross taxable ETB 4,000, basic 4,000.** PAYE = 4,000 x 15% - 300 = 600 - 300 = **300**. Pension (emp) = 280. Net = 4,000 - 300 - 280 = **3,420**. Employer pension = 440.
3. **Gross taxable ETB 6,000, basic 6,000.** PAYE = 6,000 x 20% - 500 = **700**. Pension = 420. Net = 6,000 - 700 - 420 = **4,880**. Employer pension = 660.
4. **Gross taxable ETB 7,000, basic 7,000.** PAYE = 7,000 x 20% - 500 = **900**. Pension = 490. Net = 7,000 - 900 - 490 = **5,610**.
5. **Gross taxable ETB 10,000, basic 10,000.** PAYE = 10,000 x 25% - 850 = 2,500 - 850 = **1,650**. Pension = 700. Net = 10,000 - 1,650 - 700 = **7,650**. Employer pension = 1,100.
6. **Gross taxable ETB 12,000, basic 10,000 (allowance 2,000).** PAYE = 12,000 x 30% - 1,350 = **2,250**. Pension on basic = 10,000 x 7% = 700. Net = 12,000 - 2,250 - 700 = **9,050**. Employer pension = 1,100.
7. **Gross taxable ETB 14,000, basic 14,000.** PAYE = 14,000 x 30% - 1,350 = 4,200 - 1,350 = **2,850**. Pension = 980. Net = 14,000 - 2,850 - 980 = **10,170**.
8. **Gross taxable ETB 30,000, basic 30,000.** PAYE = 30,000 x 35% - 2,050 = **8,450**. Pension = 2,100. Net = 30,000 - 8,450 - 2,100 = **19,450**. Employer pension = 3,300.
9. **Cumulative-tax consistency check:** cumulative tax at each band edge = 0 (2,000), 300 (4,000), 900 (7,000), 1,650 (10,000), 2,850 (14,000). Each equals `edge x rate - constant` for its band. Confirmed.
10. **Pension combined check:** for any basic B, employee 0.07B + employer 0.11B = 0.18B. Confirmed.

### PROHIBITIONS

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
