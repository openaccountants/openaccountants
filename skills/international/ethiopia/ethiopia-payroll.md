---
name: ethiopia-payroll
description: Use this skill whenever asked about Ethiopia payroll processing for employed persons. Trigger on phrases like "Ethiopia payroll", "Ethiopian PAYE", "employment income tax Ethiopia", "Schedule A tax Ethiopia", "pension contribution Ethiopia", "POESSA", "social security Ethiopia", "Form 17 Ethiopia", "net salary Ethiopia", "ETB payroll", "gross to net Ethiopia", "withholding tax Ethiopia", "salary calculation Ethiopia", "Proclamation 1395/2025", "employer pension Ethiopia 11%", or any question about computing employee pay, employment income tax withholding, or pension/social-security contributions for Ethiopia-based employees. This skill covers Schedule A PAYE withholding (post-7-July-2025 brackets), private-organisation pension contributions (employee 7% / employer 11%), filing obligations, and remittance deadlines. ALWAYS read this skill before processing any Ethiopia payroll.
version: 0.1
jurisdiction: ET
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Payroll Skill v0.1 (Tier 2 -- Research-Verified)

## Ethiopia Payroll Skill v0.1 (Tier 2 -- Research-Verified)

> **Tier 2 status:** Figures below are research-verified against PwC Worldwide Tax Summaries and the Income Tax (Amendment) Proclamation No. 1395/2025 (effective 7 July 2025). Items marked **[RESEARCH GAP -- reviewer to confirm]** could not be confirmed from a primary authoritative source and MUST be checked by a licensed Ethiopian accountant before reliance.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**  _(PwC Worldwide Tax Summaries -- Ethiopia (reviewed 18 Dec 2025), Tax administration and Significant developments pages.)_

| Field | Value |
| --- | --- |
| Country | Federal Democratic Republic of Ethiopia |
| Currency | Ethiopian Birr (ETB) only |
| Standard pay frequency | Monthly |
| Tax year | Ethiopian fiscal year (8 July -- 7 July); note Ethiopian calendar lags Gregorian by ~7--8 days |
| Tax withholding system | PAYE under Schedule "A" -- employment income tax, withheld monthly by employer |
| Income tax authority | Ministry of Revenue (formerly ERCA -- Ethiopian Revenues and Customs Authority) |
| Pension / social security authority | Private Organisation Employees Social Security Agency (POESSA); parallel public-servant scheme for government staff |
| Key legislation | Income Tax Proclamation as amended by Proclamation No. 1395/2025 (eff. 7 July 2025); Federal Tax Administration Proclamation No. 983/2016; Private Organisation Employees' Pension Proclamation |
| Monthly declaration form | Form 17 (monthly salary / withholding declaration) |
| Validated by | Pending -- requires sign-off by a licensed Ethiopian accountant |
| Skill version | 0.1 |

Source for legislation and authorities: PwC Worldwide Tax Summaries -- Ethiopia (reviewed 18 Dec 2025), Tax administration and Significant developments pages.

## Section 2 -- Employment Income Tax (PAYE / Schedule "A")

The employer withholds employment income tax monthly under Schedule "A". Employees whose only income is employment income do **NOT** file a personal return -- the employer's monthly withholding and remittance is final.

### Monthly tax brackets (effective 7 July 2025, FY 2025/26)

**Monthly tax brackets (effective 7 July 2025, FY 2025/26)**  _(PwC Worldwide Tax Summaries -- Ethiopia, Taxes on personal income (reviewed 18 Dec 2025); TaxDev (IFS) "Ethiopia's revised income tax explained"; Afriwise (Proc. No. 1395/2025, effective 7 July 2025).)_

| Monthly taxable salary (ETB) | Marginal rate | Quick-deduction constant (ETB) |
| --- | --- | --- |
| 0 -- 2,000 | 0% (exempt) | 0 |
| 2,001 -- 4,000 | 15% | 300 |
| 4,001 -- 7,000 | 20% | 500 |
| 7,001 -- 10,000 | 25% | 850 |
| 10,001 -- 14,000 | 30% | 1,350 |
| Over 14,000 | 35% | 2,050 |

- **Quick-deduction constants derivation** — Derived arithmetically from the marginal brackets so that `tax = salary x rate - constant` reproduces the cumulative bracket tax exactly (see Section 11 self-check). These constants are not published in the gazetted text.  _([RESEARCH GAP -- reviewer to confirm against the gazetted proclamation; some payroll vendors publish identical constants but they are derived, not statutory.])_

### Key facts and 2025 reform changes

- Tax-free threshold **raised from ETB 600 to ETB 2,000/month** (PwC; TaxDev).
- Brackets reduced from **seven to six**; the **old 10% lowest taxable band was removed** -- the lowest taxable rate is now **15%**. (Some secondary summaries still quote "10%--35%"; that is the pre-reform schedule and is outdated. The 15% lowest rate is the current PwC table.)
- Top rate **35%** unchanged but now begins above **ETB 14,000/month** (PwC).
- Residents are taxed on worldwide income; non-residents on Ethiopian-source income; the **same Schedule A rates apply to both** (PwC, Taxes on personal income).
- No published per-bracket personal relief/allowance for employment income beyond the ETB 2,000 exempt band -- tax is computed bracket-by-bracket. **[RESEARCH GAP -- the official annual-equivalent bracket table is not published by PwC; only monthly is confirmed.]**

### Computation method (per pay run)

- **PAYE computation formula** — taxable_salary  = gross taxable employment income for the month (cash salary + taxable allowances/benefits) PAYE            = taxable_salary x marginal_rate - quick_deduction_constant (apply the row whose range contains taxable_salary)  _(Section 2, PwC Worldwide Tax Summaries -- Ethiopia)_
- **PAYE not cumulative** — PAYE is not cumulative across the year (unlike Malta's FSS) -- each month is computed standalone on that month's taxable salary.  _(Section 2)_

## Section 3 -- Pension / Social Security Contributions

**Scheme:** Private Organisation Employees' Social Security, administered by **POESSA** (Private Organisation Employees Social Security Agency). A parallel scheme covers government employees. The contribution base is **basic salary** (not gross; excludes allowances/overtime), per PwC.

### Contribution rates

**Contribution rates**  _(PwC Worldwide Tax Summaries -- Ethiopia, Other taxes (employee 7%, employer 11%, base = basic salary, no ceiling stated).)_

| Party | Rate | Base |
| --- | --- | --- |
| Employee | 7% | Basic salary |
| Employer | 11% | Basic salary |
| **Combined total** | **18%** | Basic salary |

- **Self-check combined pension rate** — employee 7% + employer 11% = 18% combined. Confirmed.  _(PwC Worldwide Tax Summaries -- Ethiopia, Other taxes)_

### Coverage and mechanics

- Mandatory for **Ethiopian citizens**; optional for foreign nationals of Ethiopian origin; **not available to other foreign nationals / expats** (PwC).
- The **employer remits both portions** (employee 7% withheld + employer 11%).
- Funds old-age pension, survivors', and work-injury / invalidity benefits.

### Contribution ceiling

- **No ceiling per PwC** — PwC (primary source) states there is NO ceiling on the contribution base.  _(PwC Worldwide Tax Summaries -- Ethiopia)_

Several secondary payroll guides (e.g. Multiplier, Playroll) cite a **maximum insurable earning of ETB 15,000/month** (which would cap combined contributions at ETB 2,700/month). This **could not be confirmed from a primary authoritative source** (the ISSA country-profile PDF returned HTTP 403). **[RESEARCH GAP -- reviewer to confirm whether a POESSA directive imposes an ETB 15,000/month insurable-earnings ceiling. Default below applies NO ceiling, per PwC.]**

## Section 4 -- Conservative Defaults

**Section 4 -- Conservative Defaults**

| Input | Conservative default | Rationale |
| --- | --- | --- |
| Residency / source | Treat as **resident**, taxed on the stated employment income | Same Schedule A rates apply either way; no rate difference |
| Pension eligibility | Treat employee as an **Ethiopian citizen** (pension applies) unless told otherwise | Pension is mandatory for citizens; assuming it applies is the conservative (higher-cost) stance |
| Pension base | Use **basic salary only**; if only "gross" is given, **ask** before assuming the whole amount is basic | Contributions on too-large a base over-deduct; PwC base = basic salary |
| Pension ceiling | Apply **no ceiling** (PwC) | Primary source says no ceiling; do not silently cap at 15,000 |
| Taxable vs non-taxable allowances | Treat all stated allowances as **taxable** unless a specific exemption is provided | Avoids understating PAYE |
| Pay frequency | Assume **monthly** | Standard Ethiopian practice |
| PAYE remittance date | Use **end of the following month** (PwC) and FLAG the 8th-day discrepancy | See Section 8 |

Never present any computed figure as definitive -- always label it estimated and direct to a licensed Ethiopian accountant.

## Section 5 -- Required Inputs and Refusal Catalogue

### Required inputs before any payroll computation

- **Required inputs list** — 1. **Gross monthly employment income** (ETB), with a breakdown of **basic salary vs allowances/benefits**. 2. Which allowances are **taxable** vs exempt (if any exemption is claimed). 3. Whether the employee is an **Ethiopian citizen** (or foreign national of Ethiopian origin) for pension eligibility. 4. Pay period (month/year). 5. Any non-employment income? (If yes -> employee may need to file separately; this skill covers employment income only.)

### Refusal catalogue -- DO NOT compute; ask first

**Refusal catalogue -- DO NOT compute; ask first**

| Situation | Why refuse / pause |
| --- | --- |
| Only "gross salary" given, no basic-salary split | Pension base is basic salary; computing on gross over-deducts. Ask for the split. |
| Employee is a non-Ethiopian expat and pension treatment is unclear | Pension generally not available to expats; do not deduct 7%/11% without confirmation. |
| Request to compute the ETB 15,000 ceiling effect as if it were law | Ceiling is unconfirmed; do not present it as authoritative. |
| Request for the annual-equivalent bracket table as a definitive figure | Annual table not published; do not fabricate it. |
| Request for exact late-filing / late-payment penalty amounts | Penalty figures not in any primary source available; do not invent. |
| Request to treat the lowest band as 10% | Outdated pre-reform rate; refuse and use 15% (post-7-July-2025). |

## Section 6 -- Transaction / Payment Pattern Library

Deterministic mapping from posting context to bookkeeping treatment. Amounts are illustrative; classifications are the deliverable.

**Transaction / Payment Pattern Library table**

| Event | Debit | Credit |
| --- | --- | --- |
| Accrue gross salary | Salary expense (gross) | Net pay payable; PAYE payable; Pension payable (employee 7%) |
| Accrue employer pension (11%) | Pension expense (employer) | Pension payable (employer 11%) |
| Pay net salary to employee | Net pay payable | Bank |
| Remit PAYE to Ministry of Revenue | PAYE payable | Bank |
| Remit pension (18% combined) to POESSA | Pension payable (7% + 11%) | Bank |

- **Treatment rules** — - Gross salary and employer pension (11%) are **expenses**. - Employee PAYE and employee pension (7%) are **liabilities withheld** -- they reduce net pay, not employer cost. - Net pay = gross taxable salary - PAYE - employee pension (7% of basic salary).

## Section 7 -- Worked Examples

All figures in **ETB**. Bank lines mimic realistic Ethiopian statement narrations (e.g. CBE = Commercial Bank of Ethiopia, Awash, Dashen, telebirr). PAYE uses Section 2 brackets; pension uses Section 3 (no ceiling).

### Example 1 -- Low earner, fully exempt PAYE

- Basic salary = gross taxable = **ETB 2,000/month**.
- PAYE: salary is in 0--2,000 band -> **0% -> ETB 0**.
- Employee pension: 2,000 x 7% = **ETB 140**.
- Net pay = 2,000 - 0 - 140 = **ETB 1,860**.
- Employer pension: 2,000 x 11% = **ETB 220**.
- Employer total cost = 2,000 + 220 = **ETB 2,220**.

Bank line (net): `CBE TRANSFER DEBIT - DAMTEW W SALARY JUNE - 1,860.00` -> Net salary payment.

### Example 2 -- Mid earner, 20% band

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
- `POESSA PENSION 18% - 1,080.00` -> Pension remittance (420 + 660).

### Example 3 -- Allowances split (taxable allowance, pension on basic only)

- Basic salary = **ETB 10,000**; taxable transport allowance = **ETB 2,000**. Gross taxable = **ETB 12,000**.
- PAYE on 12,000: in 10,001--14,000 band -> 12,000 x 30% - 1,350 = 3,600 - 1,350 = **ETB 2,250**.
  - Bracket cross-check: 300 + 600 + 750 + (12,000-10,000)x30% = 300+600+750+600 = 2,250. Reconciles.
- Employee pension on **basic only** (10,000): 10,000 x 7% = **ETB 700**.
- Net pay = 12,000 - 2,250 - 700 = **ETB 9,050**.
- Employer pension on basic only: 10,000 x 11% = **ETB 1,100**.
- Employer total cost = 12,000 + 1,100 = **ETB 13,100**.

Note: pension is on basic salary (10,000), NOT on the 2,000 allowance.

### Example 4 -- High earner, top 35% band

- Basic salary = gross taxable = **ETB 30,000/month**.
- PAYE: over 14,000 -> 30,000 x 35% - 2,050 = 10,500 - 2,050 = **ETB 8,450**.
  - Bracket cross-check: cumulative tax at 14,000 = 2,850; plus (30,000-14,000)x35% = 5,600; total = **8,450**. Reconciles.
- Employee pension (no ceiling, PwC): 30,000 x 7% = **ETB 2,100**.
- Net pay = 30,000 - 8,450 - 2,100 = **ETB 19,450**.
- Employer pension: 30,000 x 11% = **ETB 3,300**.
- Employer total cost = 30,000 + 3,300 = **ETB 33,300**.

**[RESEARCH GAP]** If a confirmed ETB 15,000 insurable-earnings ceiling existed, employee pension would cap at 15,000 x 7% = 1,050 and employer at 15,000 x 11% = 1,650 (combined 2,700). This skill does **not** apply that cap by default (PwC says no ceiling).

### Example 5 -- Boundary at exactly ETB 7,000 (band edge)

- Gross taxable = **ETB 7,000** (top of the 20% band).
- PAYE: 7,000 x 20% - 500 = 1,400 - 500 = **ETB 900**.
  - Bracket cross-check: 300 + (7,000-4,000)x20% = 300 + 600 = 900. Reconciles.
- Employee pension: 7,000 x 7% = **ETB 490**.
- Net pay = 7,000 - 900 - 490 = **ETB 5,610**.
- Employer pension: 7,000 x 11% = **ETB 770**.

## Section 8 -- Filing and Remittance Obligations

**Section 8 -- Filing and Remittance Obligations**  _(PwC Worldwide Tax Summaries -- Ethiopia, Tax administration; Rivermate -- Employment taxes in Ethiopia (Form 17).)_

| Item | Detail | Deadline |
| --- | --- | --- |
| Monthly declaration (Form 17) | Gross salaries, employer + employee pension, income tax withheld, net paid | Monthly |
| PAYE remittance to Ministry of Revenue | Withheld employment income tax | **End of the month following** the month income was earned (PwC) |
| Pension remittance to POESSA | Combined 18% (7% employee + 11% employer) | **Within 30 days** of deduction |
| Personal annual return | **Not required** for employees with only employment income -- employer withholding is final | N/A |

**[RESEARCH GAP -- remittance-day discrepancy]:** PwC states PAYE is due by **the end of the following month**. Several secondary guides cite the **8th day** (or last day) of the following month. This skill defaults to **end of the following month** (PwC) but the reviewer must confirm the exact statutory day against the Federal Tax Administration Proclamation No. 983/2016.

**Calendar note:** Ethiopia uses the Ethiopian calendar (~7--8 day lag from Gregorian); confirm the effective Gregorian due date when scheduling payments.

Source: PwC Worldwide Tax Summaries -- Ethiopia, Tax administration; Rivermate -- Employment taxes in Ethiopia (Form 17).

## Section 9 -- Employer Registration

- Employers -- including **foreign companies employing staff in Ethiopia even without a permanent establishment** -- must register with the Ministry of Revenue as an employer to withhold and remit PAYE (Rivermate; PwC).
- **No published de-minimis revenue/headcount threshold** for PAYE -- the obligation arises on employing staff. **[RESEARCH GAP -- no authoritative threshold located.]**

## Section 10 -- Penalties

Governed by the **Federal Tax Administration Proclamation No. 983/2016** (still in force):

**Penalties table**  _(Federal Tax Administration Proclamation No. 983/2016)_

| Article | Subject | Classification |
| --- | --- | --- |
| Art. 104 | Late filing of returns | High-level penalty |
| Art. 105 | Late payment of tax | Medium-level penalty |
| Art. 109 | Understatement of tax | Low-level penalty |

- **Cash-transaction penalty (Proc. 1395/2025)** — 2x amount paid multiplier (cash payments over ETB 50,000 made outside electronic/cheque channels)  _(PwC, Significant developments)_
- **Statute of limitations** — 5 years years (from the filing date)  _(PwC)_

**[RESEARCH GAP -- exact penalty amounts]:** The specific ETB-per-month late-filing figures, late-payment percentages, and interest rates under Articles 104/105 could not be extracted from a primary source (the Proc. 983/2016 PDF was unparseable; PwC does not state the rates). Reviewer must read the gazetted text of Arts. 104/105/110.

Source: PwC -- Significant developments; Proclamation 983/2016 (gazetted text, not machine-readable via fetch).

## Section 11 -- Minimum Wage

- **No national / private-sector statutory minimum wage** exists in Ethiopia (RemotePeople; WageIndicator).
- A **Wage Board** (government, employers, unions) is provided for under the Labour Proclamation to set/revise minimum wages periodically; **not yet operational for the private sector**.
- **Public sector only** (does NOT apply to private payroll): a long-standing federal reference of **ETB 420/month** (unchanged since ~2012); some sources report a civil-servant minimum raised toward the **ETB ~4,800/month** range. **[RESEARCH GAP -- the current civil-servant figure varies by source; not applicable to private employers regardless.]**

Source: RemotePeople -- Minimum wage Ethiopia; WageIndicator -- Ethiopia; Capital Ethiopia (July 2025).

## Section 12 -- Tier 1 Rules (deterministic -- always apply)

- **Tier 1 rules list** — 1. Apply the **post-7-July-2025** Schedule A brackets (lowest taxable rate 15%, top 35% above ETB 14,000). NEVER use the pre-reform 10% lowest band. 2. PAYE is computed **per month, standalone** -- not cumulative across the year. 3. Pension is **employee 7% / employer 11%** on **basic salary only** (exclude allowances/overtime). 4. The **employer remits both** the 7% and 11% pension portions (combined 18%). 5. Net pay = gross taxable salary - PAYE - employee pension (7% of basic). 6. Apply **no pension ceiling** by default (PwC); only apply a ceiling if the reviewer confirms one. 7. All amounts in **ETB**. 8. Employees with only employment income do **not** file a personal return.

## Section 13 -- Tier 2 Catalogue (reviewer judgement required)

**Section 13 -- Tier 2 Catalogue (reviewer judgement required)**

| Question | Why it needs a reviewer |
| --- | --- |
| Is a particular allowance (transport, housing, per-diem) taxable or exempt? | Exemption treatment varies; not exhaustively published here. |
| Does an ETB 15,000 pension ceiling apply? | Unconfirmed; reviewer to check POESSA directive. |
| Exact PAYE remittance day (end of month vs 8th)? | Source discrepancy; reviewer to confirm statute. |
| Quick-deduction constants vs gazetted text | Constants are derived, not statutory; reviewer to confirm. |
| Pension treatment for foreign nationals of Ethiopian origin | Optional scheme; case-specific. |
| Exact penalty / interest figures | Not in available primary sources. |
| Annual-equivalent bracket table | Not published; do not fabricate. |

## Section 14 -- Excel Working Paper Template

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
| B12 | Combined pension to POESSA | `=B9 + B11` |
| B13 | Employer total cost | `=B5 + B11` |

Note: pension formulas reference **basic salary (B3)**, not gross taxable (B5).

## Section 15 -- Bank Statement / Terminology Reading Guide

**Section 15 -- Bank Statement / Terminology Reading Guide**

| Term / narration | Meaning |
| --- | --- |
| ETB / Br | Ethiopian Birr |
| CBE | Commercial Bank of Ethiopia |
| Awash / Dashen / Abyssinia | Major Ethiopian commercial banks |
| telebirr | Ethio Telecom mobile-money wallet (common for net-pay disbursement) |
| MOR / ERCA | Ministry of Revenue (formerly Ethiopian Revenues and Customs Authority) -- PAYE payee |
| POESSA | Private Organisation Employees Social Security Agency -- pension payee |
| Form 17 | Monthly salary withholding declaration |
| PAYE / Schedule A | Employment income tax withholding |
| "Pension 18%" / "POESSA 18%" | Combined 7% + 11% pension remittance |
| Net salary / Selari / Demoz | Net pay to employee |

## Section 16 -- Onboarding Fallback

- **Onboarding fallback steps** — If the client cannot provide a clean basic-vs-allowance split or pension-eligibility confirmation: 1. Request the **employment contract** (states basic salary) and the latest **Form 17** if one exists. 2. Confirm **citizenship/residency** for pension eligibility. 3. In the interim, compute PAYE on the stated gross taxable figure and **flag** that pension may be mis-stated until the basic-salary split is confirmed. 4. Do not finalise or file until the reviewer signs off.

## Section 17 -- Reference Material

**Section 17 -- Reference Material**

| Item | Value | Source |
| --- | --- | --- |
| PAYE brackets (monthly) | 0% / 15% / 20% / 25% / 30% / 35% | PwC; TaxDev; Afriwise |
| Tax-free threshold | ETB 2,000/month | PwC; TaxDev |
| Top rate threshold | Over ETB 14,000/month | PwC |
| Employee pension | 7% of basic salary | PwC, Other taxes |
| Employer pension | 11% of basic salary | PwC, Other taxes |
| Combined pension | 18% of basic salary | PwC (7%+11%) |
| Pension ceiling | None (default) | PwC |
| PAYE remittance | End of following month | PwC, Tax administration |
| Pension remittance | Within 30 days of deduction | Secondary guides **[RESEARCH GAP]** |
| Dividends WHT | 15% | PwC, Significant developments |
| Interest WHT | 10% | PwC |
| Royalties WHT | 10% | PwC |
| Cash-transaction penalty | 2x amount paid (cash > ETB 50,000) | PwC, Significant developments |
| Statute of limitations | 5 years from filing | PwC |
| Minimum wage (private) | None | RemotePeople; WageIndicator |
| Effective date of reform | 7 July 2025 | Afriwise (Proc. 1395/2025) |

Primary sources:
- PwC Worldwide Tax Summaries -- Ethiopia: Taxes on personal income; Other taxes; Tax administration; Significant developments (reviewed 18 Dec 2025).
- TaxDev (IFS) -- "Ethiopia's revised income tax explained".
- Afriwise -- Update on Income Tax (Amendment) Proclamation No. 1395/2025.
- Federal Tax Administration Proclamation No. 983/2016 (penalties).

## Section 18 -- Test Suite

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

## PROHIBITIONS

- **Prohibitions list** — - NEVER use the pre-reform 10% lowest band -- the lowest taxable rate is 15% (effective 7 July 2025). - NEVER compute pension on gross/allowances -- use **basic salary only**. - NEVER omit the employer's 11% pension portion -- the employer remits both 7% and 11%. - NEVER silently apply an ETB 15,000 pension ceiling -- it is unconfirmed; PwC says no ceiling. - NEVER treat PAYE as cumulative across the year -- it is computed standalone each month. - NEVER deduct pension for a non-Ethiopian expat without confirming eligibility. - NEVER present the quick-deduction constants as statutory -- they are derived. - NEVER invent exact penalty amounts or the annual bracket table -- mark as research gaps. - NEVER state a single remittance day as certain -- flag the end-of-month vs 8th discrepancy. - NEVER present payroll computations as definitive -- always label as estimated and direct to a licensed Ethiopian accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Ethiopia) before implementation.

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
