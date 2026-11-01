---
name: zw-payroll-social
description: >
  Zimbabwe payroll and social contributions, tax year 2026: PAYE in USD and ZWG, 3% AIDS levy, NSSA pension 4.5% each on a USD 700 ceiling, workers compensation by industry, ZIMDEF, the monthly PAYE return due on the 5th and payment on the 10th, and the long return in TaRMS. Use for questions such as Zimbabwe payroll, ZIMRA PAYE, P2 return, NSSA contributions, P4 form or what does an employee cost in Zimbabwe. Individual returns are in zw-income-tax.
version: 1.0
jurisdiction: ZW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
source_checked: 2026-11-01
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zimbabwe payroll

## Who this applies to

Employers paying remuneration in Zimbabwe in USD or ZWG. NSSA pension contributions stop at age 65; workers compensation premiums apply at any age (https://www.nssa.org.zw/contributions/).

## Rates, bands and thresholds

ZIMRA lists no 2026 table as read on 1 November 2026. The 2025 tables are the latest published, and Finance Act 7 of 2025 does not change them.

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| USD monthly 0 to 100 | 0% | 2026 | Latest ZIMRA table is labelled Jan-Dec 2025; Finance Act 7 of 2025 does not amend these bands | https://www.zimra.co.zw/domestic-taxes/tax-tables |
| USD monthly 100.01 to 300 | 20%, deduct 20 | 2026 | Same | same |
| USD monthly 300.01 to 1,000 | 25%, deduct 35 | 2026 | Same | same |
| USD monthly 1,000.01 to 2,000 | 30%, deduct 85 | 2026 | Same | same |
| USD monthly 2,000.01 to 3,000 | 35%, deduct 185 | 2026 | Same | same |
| USD monthly above 3,000 | 40%, deduct 335 | 2026 | Same | same |
| ZWG monthly 0 to 2,800 | 0% | 2026 | Same; ZWG pay only | same |
| ZWG monthly 2,800.01 to 8,400 | 20%, deduct 560 | 2026 | Same | same |
| ZWG monthly 8,400.01 to 28,000 | 25%, deduct 980 | 2026 | Same | same |
| ZWG monthly 28,000.01 to 56,000 | 30%, deduct 2,380 | 2026 | Same | same |
| ZWG monthly 56,000.01 to 84,000 | 35%, deduct 5,180 | 2026 | Same | same |
| ZWG monthly above 84,000 | 40%, deduct 9,380 | 2026 | Same | same |
| AIDS levy | 3% of tax chargeable | 2026 | Added to the tax, not to income | https://www.zimra.co.zw/domestic-taxes/corporate/tax-rates |
| NSSA pension, employee | 4.5% | 2026 | On earnings up to the ceiling | https://www.nssa.org.zw/contributions/ |
| NSSA pension, employer | 4.5% | 2026 | Same | same |
| NSSA insurable ceiling | USD 700 a month | 2026 | NSSA says it is gazetted quarterly; the page carries no date | same |
| Workers compensation, example IC 0110 | 1.38% | 2026 | Employer only; rate depends on industry code and NSSA notice | same |
| ZIMDEF levy | unverified: 1% of wage bill | 2026 | Not reconfirmed on an official page | unverified |
| National minimum wage | unverified: USD 150 a month | 2026 | SI 186 of 2024 not opened | unverified |

## The base

### Earlier working notes, carried

These sections come from the earlier version. Where a figure conflicts with the tables above, the tables above win. Anything marked as a research gap stays unconfirmed.

## zimbabwe-payroll

### Zimbabwe Payroll Skill v1.0

> **Verification status:** Tier 2. `verified_by: pending`  -  this skill has NOT yet been signed off by a registered Zimbabwean tax accountant or ZIMRA-registered tax agent. Every output must be labelled as an estimate and routed to a qualified professional.

> **CRITICAL  -  Zimbabwe runs a dual-currency payroll system.** Remuneration paid in **USD (foreign currency)** and remuneration paid in **ZiG / ZWG (Zimbabwe Gold, the local currency since April 2024)** are taxed using **two separate PAYE tax tables**. PAYE is remitted to ZIMRA **in the currency in which the income was earned**. You MUST establish the pay currency (or the currency split) before computing anything. The legacy ZWL/RTGS tables are obsolete and must never be used.

### Section 1  -  Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Zimbabwe (Republic of Zimbabwe) |
| Currencies | USD (foreign currency) **and** ZiG / ZWG (Zimbabwe Gold)  -  dual-currency payroll |
| Standard pay frequency | Monthly (most common); daily, weekly, fortnightly equivalents published by ZIMRA |
| Tax year | Calendar year (1 January – 31 December 2026) |
| Tax withholding system | PAYE under a **Final Deduction System (FDS)**  -  correctly-operated PAYE is the final tax  |
| Income tax authority | Zimbabwe Revenue Authority (ZIMRA) |
| Social security authority | National Social Security Authority (NSSA) |
| Training levy authority | Zimbabwe Manpower Development Fund (ZIMDEF) |
| Key levies | PAYE; AIDS Levy (3% of tax); NSSA POBS (9% split); NSSA APWCS (employer, industry-rated); ZIMDEF (1% employer) |
| Filing portal | TaRMS Self-Service Portal (https://mytaxselfservice.zimra.co.zw) |
| Monthly PAYE return | Form **P2** |
| PAYE remittance deadline | Return by the **5th**, payment by the **10th of the following month** (ZIMRA, PAYE Explained) |
| Validated by | Pending  -  requires sign-off by a registered Zimbabwean tax accountant / ZIMRA tax agent |
| Skill version | 1.0 |

- **Effective top marginal income tax rate**  -  40% × 1.03 (AIDS Levy) = 41.2%

### Section 2  -  Income Tax Withholding (PAYE)

Zimbabwe **has** personal income tax, withheld monthly by the employer as **PAYE** and remitted to ZIMRA. PAYE is computed on **taxable remuneration** (gross pay less allowable deductions such as the employee NSSA contribution). The marginal-rate "deduct" tables below collapse the progressive bands into a single line: `Tax = (income × rate) − deduct`.

> Zimbabwe operates a **Final Deduction System (FDS)**: where PAYE is operated correctly, it is the employee's final tax and most employees do not file an annual income-tax return .

#### 2a. PAYE  -  USD (Foreign Currency) MONTHLY Table 2025

**PAYE USD Monthly Table 2025**  _(ZIMRA, "PAY AS YOU EARN (PAYE) FOREIGN CURRENCY TAX TABLES FOR JANUARY TO DECEMBER 2025" (official ZIMRA PDF, https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4211:usd-jan-dec-2025-tax-tables))_

| Monthly taxable income (USD) | Marginal rate | Deduct (USD) |
| --- | --- | --- |
| 0 – 100.00 | 0% | – |
| 100.01 – 300.00 | 20% | 20.00 |
| 300.01 – 1,000.00 | 25% | 35.00 |
| 1,000.01 – 2,000.00 | 30% | 85.00 |
| 2,000.01 – 3,000.00 | 35% | 185.00 |
| 3,000.01 and above | 40% | 335.00 |

- **USD tax-free threshold**  -  USD 100/month (USD 1,200/year)  _(ZIMRA USD 2025 PDF)_

#### 2b. PAYE  -  USD (Foreign Currency) ANNUAL Table 2025

**PAYE USD Annual Table 2025**  _(same ZIMRA USD 2025 PDF)_

| Annual taxable income (USD) | Rate | Deduct (USD) |
| --- | --- | --- |
| 0 – 1,200 | 0% | – |
| 1,201 – 3,600 | 20% | 240 |
| 3,601 – 12,000 | 25% | 420 |
| 12,001 – 24,000 | 30% | 1,020 |
| 24,001 – 36,000 | 35% | 2,220 |
| 36,001 and above | 40% | 4,020 |

Daily, weekly and fortnightly USD equivalents are published in the same PDF (e.g. daily: 0% up to USD 3.29; top 40% from USD 98.64). Use the table that matches the pay frequency.

#### 2c. PAYE  -  ZiG / ZWG (Local Currency) MONTHLY Table 2025

**PAYE ZWG Monthly Table 2025**  _(ZIMRA, "PAY AS YOU EARN (PAYE) ZWG TAX TABLES FOR 1 JANUARY TO 31 DECEMBER 2025" (official ZIMRA PDF, https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4205:zwg-2025-tax-tables))_

| Monthly taxable income (ZWG) | Marginal rate | Deduct (ZWG) |
| --- | --- | --- |
| 0 – 2,800.00 | 0% | – |
| 2,800.01 – 8,400.00 | 20% | 560 |
| 8,400.01 – 28,000.00 | 25% | 980 |
| 28,000.01 – 56,000.00 | 30% | 2,380 |
| 56,000.01 – 84,000.00 | 35% | 5,180 |
| 84,000.01 and above | 40% | 9,380 |

- **ZWG tax-free threshold**  -  ZWG 2,800/month (ZWG 33,600/year)  _(ZIMRA ZWG 2025 PDF)_

#### 2d. PAYE  -  ZiG / ZWG (Local Currency) ANNUAL Table 2025

**PAYE ZWG Annual Table 2025**  _(same ZIMRA ZWG 2025 PDF)_

| Annual taxable income (ZWG) | Rate | Deduct (ZWG) |
| --- | --- | --- |
| 0 – 33,600 | 0% | – |
| 33,601 – 100,800 | 20% | 6,720 |
| 100,801 – 336,000 | 25% | 11,760 |
| 336,001 – 672,000 | 30% | 28,560 |
| 672,001 – 1,008,000 | 35% | 62,160 |
| 1,008,001 and above | 40% | 112,560 |

#### 2e. AIDS Levy

- **AIDS Levy rule**  -  3% of the PAYE / individual's tax payable  -  a surcharge on the tax, not on income. Stated verbatim on both official ZIMRA tax-table PDFs: "Aids Levy is 3% of the Individuals' Tax payable."  _(official ZIMRA tax-table PDFs)_
- **Computation order**  -  (1) compute PAYE from the bracket table; (2) AIDS Levy = PAYE × 3%; (3) total tax withheld = PAYE + AIDS Levy.
- **Effective top marginal rate**  -  40% × 1.03 = 41.2%

### Section 3  -  Social Security (NSSA)

NSSA administers two schemes. The **POBS** (pension) is split employee/employer; the **APWCS** (workers' compensation) is employer-only.

#### 3a. Pension and Other Benefits Scheme (POBS)

**POBS rate table**  _(NSSA, "Contributions" (https://www.nssa.org.zw/contributions/))_

| Component | Employee | Employer | Combined |
| --- | --- | --- | --- |
| POBS rate | 4.5% of insurable earnings | 4.5% of insurable earnings | **9.0%** |

Employee 4.5% + Employer 4.5% = **9.0%** combined. ✓

- **Insurable earnings ceiling**  -  USD 700/month (introduced mid-2024, retained for 2025). Maximum contribution = USD 31.50 each / USD 63.00 total per month for anyone earning ≥ USD 700 (4.5% × 700 = 31.50; ×2 = 63.00). ✓

The ceiling is gazetted quarterly  -  verify the current quarter's figure before each payroll run (NSSA Schedule of Insurable Earnings, https://www.nssa.org.zw/scheduleofinsurableearnings/). **[RESEARCH GAP  -  reviewer to confirm the ceiling applicable to the specific pay period; USD 700 was the 2024/2025 level.]**

For ZiG-paid employees, NSSA applies the gazetted ZiG-equivalent ceiling for the quarter. **[RESEARCH GAP  -  reviewer to confirm the current ZiG-equivalent insurable-earnings ceiling.]**

- **Employee POBS deductibility**  -  Employee POBS contributions are deductible when computing taxable income for PAYE (subtract before applying the PAYE table).
- **Remittance deadline**  -  10th of the following month

#### 3b. Accident Prevention & Workers' Compensation Scheme (APWCS / WCIF)

**APWCS rate table**  _(NSSA guidance))_

| Component | Employee | Employer |
| --- | --- | --- |
| APWCS rate | 0% (employee pays nothing) | **Varies by industry-risk (IC) code** on the monthly insurable wage bill |

- **IC code example**  -  Employer-only. The rate depends on the employer's industry-risk classification (IC) code assessed by NSSA. Published example: IC Code 0110 = 1.38% → on a USD 5,000 wage bill = USD 69.00/month (5,000 × 1.38% = 69.00). ✓

Low-risk sectors (offices, retail) attract lower rates; high-risk sectors (mining, construction) attract higher rates.

**[RESEARCH GAP  -  reviewer to confirm the employer's exact APWCS rate from its NSSA assessment notice. A complete 2025 IC-code rate schedule was not obtainable from an authoritative source; only the IC 0110 = 1.38% example is published.]**

### Section 4  -  ZIMDEF Manpower Development Levy

**ZIMDEF levy table**  _(ZIMDEF FAQs (https://zimdef.org.zw/faqs/); Manpower Planning & Development Act (Ch. 28:02), SIs 74 & 392 of 1999)_

| Component | Employee | Employer |
| --- | --- | --- |
| ZIMDEF levy | 0% | **1% of the gross monthly wage bill (leviable items)** |

- **Employer-only training levy**  -  Employer-only training levy.
- **Remittance deadline**  -  within 30 days after month-end
- **Non-compliance**  -  Failure to register / remit is a criminal offence.

#### Employer statutory cost summary (per employee, monthly)

**Employer statutory cost summary**

| Charge | Who pays | Rate / basis | Source |
| --- | --- | --- | --- |
| POBS pension | Employer | 4.5% of insurable earnings (cap USD 700) | NSSA Contributions |
| APWCS / WCIF | Employer | Industry-rated (e.g. IC 0110 = 1.38%) | NSSA guidance |
| ZIMDEF | Employer | 1% of leviable wage bill | ZIMDEF FAQs |

**Self-check  -  employer charges are distinct lines, no double-count:** POBS (4.5%) + APWCS (industry %) + ZIMDEF (1%) are three separate remittances to two authorities (NSSA, ZIMDEF). The employer does **not** pay AIDS Levy or PAYE out of its own funds  -  those are withheld from the employee. ✓

### Section 5  -  Minimum Wage

**Minimum wage table**  _(SI 186 of 2024; National Employment Council (NEC) collective bargaining agreements)_

| Item | Value | Source |
| --- | --- | --- |
| National minimum wage | **USD 150/month** (or ZiG equivalent) | SI 186 of 2024 (first general statutory minimum wage) |
| Sector minimum wages | Set by ~22 NECs, gazetted as SIs, legally binding per sector; usually higher than the SI 186 floor | NEC CBAs |
| Example  -  Agriculture grade A1 | USD 80/month (eff. 1 June 2025) | Agriculture NEC CBA **[RESEARCH GAP  -  reviewer to confirm current grade rates]** |
| Example  -  Agriculture grade C2 | USD 159/month (eff. 1 June 2025) | Agriculture NEC CBA **[RESEARCH GAP  -  reviewer to confirm current grade rates]** |

> **Currency-split rule:** workers are generally paid **65% in USD** and the remainder in ZiG. This split determines which PAYE table applies to each portion of pay. **[RESEARCH GAP  -  the 65/35 split is a market norm, not a uniform statutory rule; reviewer to confirm the contractual / NEC split for the specific employer.]**

### Section 6  -  Conservative Defaults

When a required input is missing and the user asks you to proceed anyway, apply the **most conservative** assumption (the one least likely to under-withhold tax or under-state a statutory liability), flag it loudly, and queue it for reviewer confirmation. Never silently guess.

**Conservative defaults table**  _(https://www.zimra.co.zw/domestic-taxes/individual/pay-as-you-earn-paye)_

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Pay currency | Treat as **USD** and apply the USD PAYE table | Avoids mis-applying the ZiG threshold; but DO NOT finalise  -  currency drives everything. Flag hard. |
| Currency split (USD/ZiG) | Use the USD tax tables on the whole salary and apportion the tax due between the currencies (ZIMRA instruction); if the split is unknown, treat full pay in the stated currency | Splitting across two tables understates tax |
| NSSA insurable ceiling | Use **USD 700/month** (2024/2025 gazetted level) | Latest confirmed figure; flag that it is gazetted quarterly |
| APWCS IC rate | Do **not** invent a rate  -  leave as `[reviewer to supply IC rate]` | No authoritative full schedule exists |
| Employee NSSA deductibility | Deduct employee POBS before PAYE | Statutorily allowed; omitting it over-withholds tax |
| Tax-free threshold currency | Match threshold to pay currency (USD 100 vs ZWG 2,800) | Mixing currencies corrupts the base |
| Pay frequency | Assume **monthly** | Most common; use monthly tables |

### Section 7  -  Required Inputs & Refusal Catalogue

#### Required inputs (gather before any computation)

- **Required inputs list**  -  1. **Pay currency**  -  USD, ZiG/ZWG, or a stated split (and the split ratio). 2. Gross remuneration for the period, broken into taxable and non-taxable components. 3. Employee NSSA (POBS) membership status (most formal-sector employees are members). 4. Employer's **APWCS IC-code rate** (from the NSSA assessment notice). 5. Pay frequency and the specific pay period. 6. Any allowances / benefits in kind (affect both PAYE base and the ZIMDEF leviable base). 7. Whether the employer is registered with ZIMRA (BP number), NSSA, and ZIMDEF.

#### Refusal Catalogue  -  STOP and ask; do not produce numbers

- **Pay currency not stated**  -  **Refuse to compute.** Ask: "Is this employee paid in USD, ZiG/ZWG, or a split? Zimbabwe uses separate PAYE tables per currency."
- **Legacy ZWL/RTGS figures supplied**  -  **Refuse.** Tell the user the ZWL/RTGS tables are obsolete; payroll since April 2024 is USD or ZiG/ZWG.
- **APWCS rate requested but no IC code/assessment**  -  Compute everything else; leave APWCS as `[reviewer to supply IC rate]`. Do not invent a percentage.
- **User asks to omit AIDS Levy**  -  **Refuse.** AIDS Levy (3% of PAYE) is mandatory on all PAYE.
- **User asks to skip employee NSSA to "simplify"**  -  Flag that omitting the POBS deduction over-withholds PAYE; confirm membership before excluding.
- **No employee data at all**  -  Stop; list the required inputs above.
- **Request to present output as final/filed**  -  **Refuse.** Output is an estimate pending a registered Zimbabwean tax agent's sign-off.

### Section 8  -  Transaction / Payment Pattern Library (deterministic)

Apply these classifications **in order**; first match wins. Currency tags (USD / ZiG) help disambiguate which PAYE table the underlying pay used.

#### 8a. Salary credits (money INTO an employee account)

**Salary credits table**  _(https://www.zimra.co.zw/domestic-taxes/individual/paye-explained)_

| Bank-statement text (typical) | Classification |
| --- | --- |
| `SALARY`, `MUHOLO` (Shona: wages/pay), `MUVUZO`, `WAGES`, `PAY` | Net salary payment |
| `EMPLOYER [name] TRF`, `STAFF SALARY`, `PAYROLL CR` | Net salary payment |
| `ALLOWANCE`, `HOUSING ALLOW`, `TRANSPORT ALLOW` | Allowance (taxable unless specifically exempt) |
| `BONUS`, `13TH CHEQUE` | Bonus (taxable above the ZIMRA tax-free bonus threshold; included in ZIMDEF leviable base) |
| `NSSA REFUND` | NSSA adjustment  -  not income |

#### 8b. Employer statutory debits (money OUT of the employer account)

**Employer statutory debits table**

| Bank-statement text (typical) | Classification |
| --- | --- |
| `ZIMRA`, `ZIMRA SINGLE ACCOUNT`, `PAYE`, `P2 PAYMENT` | PAYE + AIDS Levy remittance to ZIMRA |
| `ZIMRA AIDS LEVY` | AIDS Levy component (if shown separately) |
| `NSSA`, `NSSA POBS`, `NSSA PENSION` | NSSA POBS pension remittance |
| `NSSA APWCS`, `NSSA WCIF`, `ACCIDENT FUND` | NSSA workers' compensation remittance (employer) |
| `ZIMDEF`, `MANPOWER LEVY`, `TRAINING LEVY` | ZIMDEF 1% levy remittance |
| `NET WAGES`, `SALARY RUN`, `PAYROLL` | Salary disbursement to employees |

> Currency note: ZIMRA remittances are made in the **currency the income was earned in** (USD pay → remit in USD; ZiG pay → remit in ZiG) into the **ZIMRA Single Bank Account**.

### Section 9  -  Worked Examples

> All figures are **estimates** for illustration. Recomputed end-to-end below. Round to the cent.

#### Example 1  -  USD salary, mid-band employee

- Gross monthly pay: **USD 1,500**, paid entirely in USD. NSSA member.
- **Employee NSSA (POBS):** 4.5% × min(1,500, 700 ceiling) = 4.5% × 700 = **USD 31.50**.
- **PAYE taxable income:** 1,500 − 31.50 = **USD 1,468.50** (falls in 1,000.01–2,000 band → 30%, deduct 85).
- **PAYE:** 1,468.50 × 0.30 − 85 = 440.55 − 85 = **USD 355.55**.
- **AIDS Levy:** 355.55 × 0.03 = **USD 10.67** (10.6665 → 10.67).
- **Total tax withheld:** 355.55 + 10.67 = **USD 366.22**.
- **Net pay:** 1,500 − 31.50 − 366.22 = **USD 1,102.28**.
- **Employer cost on top:** POBS 31.50 + ZIMDEF (1% × 1,500 = 15.00) + APWCS `[reviewer to supply IC rate]`.

#### Example 2  -  USD salary, top-band executive

- Gross monthly pay: **USD 5,000**, USD. NSSA member.
- **Employee NSSA:** 4.5% × 700 (ceiling) = **USD 31.50**.
- **Taxable income:** 5,000 − 31.50 = **USD 4,968.50** (above 3,000 → 40%, deduct 335).
- **PAYE:** 4,968.50 × 0.40 − 335 = 1,987.40 − 335 = **USD 1,652.40**.
- **AIDS Levy:** 1,652.40 × 0.03 = **USD 49.57** (49.572 → 49.57).
- **Total tax withheld:** 1,652.40 + 49.57 = **USD 1,701.97**.
- **Net pay:** 5,000 − 31.50 − 1,701.97 = **USD 3,266.53**.
- **Employer ZIMDEF:** 1% × 5,000 = USD 50.00. **APWCS (illustrative IC 0110 = 1.38%):** 1.38% × 5,000 = USD 69.00.

#### Example 3  -  USD salary below the tax-free threshold

- Gross monthly pay: **USD 90**, USD. NSSA member.
- **Employee NSSA:** 4.5% × 90 = **USD 4.05** (below the 700 ceiling).
- **Taxable income:** 90 − 4.05 = **USD 85.95** (≤ 100 → 0% band).
- **PAYE:** 0. **AIDS Levy:** 0 (3% of zero). **Total tax:** **USD 0.00**.
- **Net pay:** 90 − 4.05 = **USD 85.95**.
- Note: USD 90 is below the SI 186 of 2024 national minimum wage of USD 150  -  flag a potential minimum-wage breach to the reviewer.

#### Example 4  -  ZiG/ZWG salary, mid-band employee

- Gross monthly pay: **ZWG 40,000**, paid entirely in ZiG. NSSA member.
- **Employee NSSA:** 4.5% × ZiG insurable earnings, capped at the gazetted ZiG-equivalent ceiling. **[RESEARCH GAP  -  ZiG ceiling not confirmed; this example assumes pay is at/below the ceiling, so NSSA = 4.5% × 40,000 = ZWG 1,800. Reviewer to confirm the ZiG ceiling.]**
- **Taxable income (assuming NSSA = 1,800):** 40,000 − 1,800 = **ZWG 38,200** (28,000.01–56,000 → 30%, deduct 2,380).
- **PAYE:** 38,200 × 0.30 − 2,380 = 11,460 − 2,380 = **ZWG 9,080**.
- **AIDS Levy:** 9,080 × 0.03 = **ZWG 272.40**.
- **Total tax withheld:** 9,080 + 272.40 = **ZWG 9,352.40**.
- **Net pay:** 40,000 − 1,800 − 9,352.40 = **ZWG 28,847.60**.
- ZIMRA remittance is made **in ZiG** into the ZIMRA Single Bank Account.

#### Example 5  -  Split pay (65% USD / 35% ZiG)

- Total gross: **USD 1,000-equivalent**, split 65% USD / 35% ZiG. ZIMRA: "for salaries with both ZWG and USD components use the USD tax tables and apportion the tax due accordingly." Compute PAYE once on the total on the USD table, then apportion the tax between the USD and ZiG portions and remit each portion in its own currency. Do not apply each currency's table to its own portion.
- **USD portion:** USD 650. Employee NSSA 4.5% × 650 = USD 29.25. Taxable 650 − 29.25 = 620.75 (300.01–1,000 → 25%, deduct 35). PAYE = 620.75 × 0.25 − 35 = 155.19 − 35 = **USD 120.19** (155.1875 → 120.19). AIDS Levy = 120.19 × 0.03 = **USD 3.61** (3.6057 → 3.61).
- **ZiG portion:** assume ZWG-equivalent of the remaining 35%. Compute on the ZWG monthly table per Section 2c. **[RESEARCH GAP  -  requires the USD/ZiG exchange rate for the period; reviewer to supply.]**
- Remit USD PAYE in USD and ZiG PAYE in ZiG. Do **not** net the two currencies.

### Section 10  -  Tier 1 Rules (deterministic  -  always apply)

- **Tier 1 Rules**  -  1. Establish **pay currency** first; select the matching PAYE table (USD = Section 2a/2b; ZiG = Section 2c/2d). Never mix. 2. Deduct the **employee NSSA (POBS) 4.5%** (capped) before applying the PAYE table. 3. Compute PAYE as `income × rate − deduct` from the correct frequency table. 4. Apply **AIDS Levy = PAYE × 3%** after PAYE, never on gross income. 5. Total employee tax withheld = PAYE + AIDS Levy. 6. Employer pays POBS 4.5%, APWCS (industry-rated), and ZIMDEF 1% **separately**  -  never deducted from the employee. 7. Remit PAYE + AIDS Levy to ZIMRA via **Form P2** by the **10th of the following month**, in the currency earned. 8. Remit NSSA by the 10th; remit ZIMDEF within 30 days of month-end. 9. Never use legacy ZWL/RTGS tables. 10. Label every output as an estimate pending professional sign-off.

### Section 11  -  Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Item | Why it needs judgement |
| --- | --- |
| Current NSSA insurable-earnings ceiling | Gazetted quarterly; USD 700 was 2024/2025 |
| ZiG-equivalent NSSA ceiling | Not confirmed in research data |
| Employer APWCS IC-code rate | No authoritative full schedule; assessment-specific |
| Taxability of specific allowances / benefits in kind | Depends on ZIMRA treatment of each item |
| Split-pay PAYE mechanics across two currencies | Threshold application uncertain; confirm with ZIMRA |
| Applicable NEC sector minimum wage | ~22 sectors, each with its own gazetted SI |
| USD/ZiG exchange rate for split or conversion | Period-specific; reviewer to supply |
| Late-PAYE penalty quantum | Applied per ZIMRA assessment (see Section 14) |

### Section 12  -  Excel Working Paper Template

**Excel Working Paper Template**

| Col | Field | Formula / source |
| --- | --- | --- |
| A | Employee name / ID | input |
| B | Pay currency (USD / ZWG) | input |
| C | Gross pay (this currency) | input |
| D | Insurable earnings (capped) | `=MIN(C, ceiling)` (ceiling = USD 700 or gazetted ZiG figure) |
| E | Employee NSSA (POBS) | `=D*0.045` |
| F | Taxable income | `=C-E` |
| G | PAYE marginal rate | lookup vs Section 2a (USD) or 2c (ZWG) table |
| H | PAYE deduct | lookup (same row as G) |
| I | PAYE | `=F*G-H` (floor at 0) |
| J | AIDS Levy | `=I*0.03` |
| K | Total tax withheld | `=I+J` |
| L | Net pay | `=C-E-K` |
| M | Employer POBS | `=D*0.045` |
| N | Employer APWCS | `=C*IC_rate` (IC rate from NSSA assessment  -  `[reviewer]`) |
| O | Employer ZIMDEF | `=leviable_base*0.01` |

> Check totals: Σ(K) across USD employees = PAYE+AIDS to remit to ZIMRA in USD; Σ(K) across ZWG employees = remit in ZiG. Keep currencies in separate sheets  -  never sum across currencies.

### Section 13  -  Bank Statement / Terminology Reading Guide

**Terminology guide table**

| Term | Meaning |
| --- | --- |
| ZIMRA | Zimbabwe Revenue Authority (income tax / PAYE) |
| NSSA | National Social Security Authority (pension + accident fund) |
| ZIMDEF | Zimbabwe Manpower Development Fund (1% training levy) |
| PAYE | Pay As You Earn (employer-withheld income tax) |
| AIDS Levy | 3% surcharge on PAYE |
| POBS | Pension and Other Benefits Scheme (NSSA, 9% split) |
| APWCS / WCIF | Accident Prevention & Workers' Compensation Scheme (employer-only) |
| FDS | Final Deduction System (PAYE is the final tax) |
| P2 | Monthly PAYE return form |
| TaRMS | Tax and Revenue Management System (ZIMRA self-service portal) |
| ITF263 | Tax Clearance Certificate |
| BP number | Business Partner number (ZIMRA registration) |
| ZiG / ZWG | Zimbabwe Gold  -  the local currency since April 2024 |
| Muholo / Muvuzo | Shona for wages / pay (may appear on statements) |
| ZWL / RTGS | **Obsolete** legacy currency  -  do not use 2025 |

### Section 14  -  Filing, Penalties & Onboarding Fallback

#### Filing obligations

**Filing obligations table**

| Obligation | Form / channel | Deadline | Source |
| --- | --- | --- | --- |
| Monthly PAYE + AIDS Levy | Form **P2** via TaRMS portal | return 5th, payment **10th of following month** | ZIMRA, PAYE Explained |
| NSSA (POBS + APWCS) | NSSA channels | return 5th, payment **10th of following month** | NSSA Contributions |
| ZIMDEF levy | ZIMDEF | **within 30 days after month-end** | ZIMDEF FAQs |
| Employer registration | ZIMRA (BP number) before operating PAYE | Before first payroll | ZIMRA **[RESEARCH GAP  -  exact registration-page figures not retrievable]** |

- Payments are made into the **ZIMRA Single Bank Account**, **in the currency in which the income was earned**.
- Under the **FDS**, correctly-operated PAYE is final; most employees do not file an annual return .

#### Penalties / interest

- **Late-PAYE interest**  -  10% per annum on late-remitted PAYE (stated on the P2 PAYE return form)  _(P2 PAYE return form)_
- **Penalties and ITF263 disqualification**  -  Late / non-remittance also triggers penalties and disqualification from a Tax Clearance Certificate (ITF263).

**[RESEARCH GAP  -  no single authoritative flat-penalty percentage for late PAYE was found; ZIMRA applies penalties per assessment under the Income Tax Act and Revenue Authority statutes. State as "per ZIMRA assessment," not a fixed figure.]**

#### Onboarding fallback

If the employer is not yet registered with ZIMRA / NSSA / ZIMDEF, stop and tell the user: registration (ZIMRA BP number, NSSA employer registration, ZIMDEF registration) must be completed before PAYE and statutory contributions can be lawfully operated. Route to a registered Zimbabwean tax agent for onboarding.

### Section 15  -  Reference Material

**Reference Material table**

| # | Item | Value | Source |
| --- | --- | --- | --- |
| R1 | USD tax-free threshold | USD 100/month (USD 1,200/yr) | ZIMRA USD 2025 PDF |
| R2 | USD top marginal rate | 40% (from USD 3,000.01/month) | ZIMRA USD 2025 PDF |
| R3 | ZWG tax-free threshold | ZWG 2,800/month (33,600/yr) | ZIMRA ZWG 2025 PDF |
| R4 | ZWG top marginal rate | 40% (from ZWG 84,000.01/month) | ZIMRA ZWG 2025 PDF |
| R5 | AIDS Levy | 3% of PAYE | ZIMRA tax-table PDFs |
| R6 | Effective top rate | 41.2% | unverified |
| R7 | NSSA POBS | 4.5% EE + 4.5% ER = 9% | NSSA Contributions |
| R8 | NSSA ceiling | USD 700/month (gazetted quarterly) | NSSA Schedule of Insurable Earnings |
| R9 | APWCS | Employer-only, industry-rated (e.g. IC 0110 = 1.38%) | NSSA guidance |
| R10 | ZIMDEF | 1% of leviable wage bill (employer) | ZIMDEF FAQs |
| R11 | National minimum wage | USD 150/month | SI 186 of 2024 |
| R12 | PAYE deadline | 10th of following month | ZIMRA PAYE Explained |
| R13 | Late-PAYE interest | 10% p.a. | ZIMRA P2 return |

#### Primary source URLs

- ZIMRA USD 2025 table: https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4211:usd-jan-dec-2025-tax-tables
- ZIMRA ZWG 2025 table: https://www.zimra.co.zw/domestic-taxes/tax-tables?download=4205:zwg-2025-tax-tables
- ZIMRA tax tables index: https://www.zimra.co.zw/domestic-taxes/tax-tables
- ZIMRA PAYE explained: https://www.zimra.co.zw/domestic-taxes/individual/paye-explained
- NSSA contributions: https://www.nssa.org.zw/contributions/
- NSSA schedule of insurable earnings: https://www.nssa.org.zw/scheduleofinsurableearnings/
- ZIMDEF FAQs: https://zimdef.org.zw/faqs/

### Section 16  -  Test Suite

Each test recomputed end-to-end. Use these to validate any implementation.

1. **USD 100 exactly →** PAYE = 0 (within 0% band, ≤ 100). AIDS = 0. ✓
2. **USD 100.01 →** taxable 100.01 (before NSSA): 100.01 × 0.20 − 20 = 20.002 − 20 = **USD 0.00** (0.002 ≈ 0; band entry point). ✓
3. **USD 700 NSSA cap →** employee POBS = 4.5% × 700 = **USD 31.50** (max); USD 1,000 gross still caps at 31.50. ✓
4. **USD 1,500 (Example 1) →** PAYE 355.55, AIDS 10.67, net 1,102.28. ✓
5. **USD 5,000 (Example 2) →** PAYE 1,652.40, AIDS 49.57, net 3,266.53; ZIMDEF 50.00. ✓
6. **ZWG 2,800 exactly →** PAYE = 0 (top of 0% band). ✓
7. **ZWG 8,400 →** 8,400 × 0.20 − 560 = 1,680 − 560 = **ZWG 1,120**; AIDS = 33.60. ✓
8. **ZWG 40,000 (Example 4) →** PAYE 9,080, AIDS 272.40, net 28,847.60 (NSSA 1,800 assumed). ✓
9. **AIDS Levy isolation →** PAYE 1,000 → AIDS = 1,000 × 0.03 = **30.00**; total 1,030. ✓
10. **POBS combined →** 4.5% + 4.5% = 9.0% of insurable earnings. ✓
11. **APWCS example →** USD 5,000 wage bill × 1.38% (IC 0110) = **USD 69.00**. ✓
12. **ZIMDEF →** USD 5,000 leviable × 1% = **USD 50.00**. ✓
13. **Currency guard →** unspecified currency must trigger the Section 7 refusal (no number produced). ✓
14. **Legacy guard →** ZWL/RTGS input must trigger refusal. ✓

### PROHIBITIONS

- **Prohibitions list**  -  - NEVER compute Zimbabwe payroll without first establishing the **pay currency** (USD vs ZiG/ZWG)  -  the tables are different. - NEVER use the legacy **ZWL / RTGS** tax tables  -  they are obsolete since the ZiG transition (April 2024). - NEVER apply the AIDS Levy to gross income  -  it is **3% of PAYE**, computed after PAYE. - NEVER omit the AIDS Levy from any PAYE computation. - NEVER compute employee NSSA above the gazetted insurable-earnings ceiling (USD 700/month, or the current quarter's figure). - NEVER invent an APWCS IC-code rate  -  leave it for the reviewer to supply from the NSSA assessment. - NEVER net USD and ZiG PAYE together  -  remit each in the currency the income was earned in. - NEVER deduct employer POBS, APWCS, or ZIMDEF from the employee  -  they are employer costs. - NEVER miss the P2 PAYE deadline (10th of the following month)  -  10% p.a. interest and penalties apply. - NEVER present payroll computations as definitive  -  always label as estimated and direct to a registered Zimbabwean tax agent / accountant.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered Zimbabwean tax accountant or ZIMRA-registered tax agent) before implementation. This is a Tier 2 skill that has not yet received professional verification (`verified_by: pending`).

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Deadlines and filing

| Obligation | Return | Payment |
|---|---|---|
| PAYE and AIDS levy | 5th of next month | 10th of next month |
| NSSA P4 | Monthly on the NSSA self-service portal | With form P4A |

Steps for PAYE:

1. Log into the Self Service Portal at mytaxselfservice.zimra.co.zw and select your TIN.
2. Upload the long PAYE return through the employee management menu (Public Notice 5 of 2025, repeated in Public Notice 61 of 2026).
3. Go to Tax Return Management, Pending Returns, complete and submit.
4. Pay into the ZIMRA account with TIN and name. Payment posts only once the return is filed.

From 1 January 2026 employer returns are monthly unless the Commissioner approves longer, and an employer who ceases files within 14 days (Finance Act 7 of 2025 s.26).

Steps for NSSA: e-file P4 on the portal; complete P4A to show the split between schemes; use P4C for leavers; complete WC50 for the yearly wage declaration.

## Penalties and interest

Public Notice 61 of 2026 warns of penalties or prosecution for late returns or payments, without a figure. An employer may not recover NSSA surcharges, penalties or interest from employees (https://www.nssa.org.zw/contributions/). The 10% a year interest from the P2 form in the earlier version was not reconfirmed.

## Cross-border points

Expatriates employed by an international financial services centre pay 15% on that income (Act ss.5, 6). A BKPO service gets a youth employment credit of 1,500 dollars per extra employee, capped at 60,000 a year (Act s.3). An employee with two employers is covered by each.

## Two worked examples that recompute

USD 900 a month: NSSA 31.50; taxable 868.50; tax 868.50 x 25% - 35 = 182.13; levy 5.46; total 187.59. Deducting NSSA before PAYE follows the earlier version and is not confirmed from the Act.

```oa-check
name: USD 900 monthly pay
inputs:
  pay: 900
steps:
  - nssa: min(pay, 700) * 0.045
  - taxable: pay - nssa
  - tax: taxable * 0.25 - 35
  - total: tax * 1.03
expected:
  nssa: 31.50
  total: 187.59
```

Decision: is NSSA capped? Staff member on USD 5,000 in farming, employer cost excluding ZIMDEF: POBS 31.50 plus compensation 1.38% of 5,000 = 69, total 100.50. The pension is capped, the compensation premium is not.

```oa-check
name: Employer cost on USD 5,000, IC 0110
inputs:
  pay: 5000
steps:
  - pobs: min(pay, 700) * 0.045
  - comp: pay * 0.0138
  - cost: pobs + comp
expected:
  cost: 100.50
```

## Ask the client first

1. Pay currency and any split.
2. Pay period.
3. Employee age, for the 65 limit.
4. NSSA industry code and rate notice.
5. Sector, for the NEC wage.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act No. 7 of 2025 (Veritas copy of the Government Printer text), whole Act | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf | 2026-11-01 |
| ZIMRA Public Notices 5, 7, 11, 49, 50, 58, 61 of 2026 (list page; each PDF opened) | https://www.zimra.co.zw/public-notices | 2026-11-01 |
| ZIMRA Tax Tables page and 2025 PDFs, monthly and annual tables | https://www.zimra.co.zw/domestic-taxes/tax-tables | 2026-11-01 |
| NSSA Contributions page, whole page, in a browser | https://www.nssa.org.zw/contributions/ | 2026-11-01 |

Not yet confirmed: any 2026 PAYE table; current quarter NSSA ceiling and its ZWG equivalent; full IC rates; ZIMDEF rate and deadline; SI 186 of 2024 and NEC wages, including the 65% USD split; late PAYE penalty; order of NSSA and PAYE.

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
