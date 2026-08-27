---
name: north-macedonia-payroll
description: Use this skill whenever asked about North Macedonia payroll processing for employed persons. Trigger on phrases like "North Macedonia payroll", "Macedonian salary", "плата", "plata", "MPIN", "МПИН", "flat tax Macedonia", "10% income tax Macedonia", "personal income tax Macedonia", "PIT Macedonia", "данок на личен доход", "social contributions Macedonia", "придонеси", "pridonesi", "PIOM", "ПИОМ", "pension fund Macedonia", "ФЗОМ", "FZOM", "health insurance Macedonia", "unemployment contribution Macedonia", "personal allowance Macedonia", "личен ослободување", "net salary Macedonia", "gross to net Macedonia", "neto plata", "PAYE Macedonia", "tax withholding Macedonia", "employer contributions Macedonia", "minimum wage Macedonia", "минимална плата", "UJP", "УЈП", "Public Revenue Office Macedonia", "M1 registration Macedonia", "contribution ceiling Macedonia", "MKD payroll", or any question about computing employee pay, withholding personal income tax, or mandatory social contributions for North Macedonia-based employees. This skill covers the flat 10% personal income tax, the 28% employee-borne mandatory social contributions (pension & disability, health, unemployment, additional/disability), the monthly personal allowance, the minimum and maximum contribution bases, the minimum wage, the MPIN monthly integrated-collection declaration, the annual PIT draft return, and M1 employment registration. ALWAYS read this skill before processing any North Macedonia payroll.
version: 0.1
jurisdiction: MK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# North Macedonia Payroll

## North Macedonia Payroll Skill v0.1

**Tier 2 — research-verified. Figures below are sourced from the Public Revenue Office (Управа за јавни приходи / UJP / PRO — ujp.gov.mk), the social funds (Pension & Disability Insurance Fund PIOM, Health Insurance Fund FZOM, Employment Agency AVRSM), the Ministry of Labour and Social Policy (mtsp.gov.mk), the Official Gazette (Службен весник), PwC Worldwide Tax Summaries, and the Eurofast North Macedonia Tax Card 2025 / Payroll Guide 2025. NOT yet signed off by a licensed Macedonian accountant (овластен сметководител) or authorised auditor. Treat every computation as an estimate pending professional review.**

> **The single most distinctive North Macedonia fact:** ALL mandatory social contributions (28% in total) are levied on the employee's gross salary, WITHHELD from gross, and remitted by the employer on the employee's behalf. There is **NO separate employer-side contribution on top of gross salary** unless a special law requires one. The employer's payroll cost is the gross salary; it is not grossed up by an additional social charge. (Eurofast Tax Card / Payroll Guide 2025)

## Section 1 -- Quick Reference

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the North Macedonia-specific content.**

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | North Macedonia (Republic of North Macedonia / Република Северна Македонија) |
| Currency | MKD (Macedonian denar) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Monthly withholding -- employer computes gross, withholds 28% social contributions and the flat 10% PIT, and remits everything via the MPIN integrated-collection declaration (Eurofast Payroll Guide 2025) |
| Income tax authority | Public Revenue Office (UJP / PRO — Управа за јавни приходи) — https://www.ujp.gov.mk (PwC) |
| Pension authority | Pension and Disability Insurance Fund (PIOM / Фонд за ПИОМ) (Eurofast Tax Card 2025) |
| Health authority | Health Insurance Fund (FZOM / Фонд за здравствено осигурување) (Eurofast Tax Card 2025) |
| Employment / unemployment authority | Employment Agency (AVRSM / Агенција за вработување) (Eurofast Payroll Guide 2025) |
| Minimum-wage setter | Ministry of Labour and Social Policy (mtsp.gov.mk) (Official Gazette 68/25) |
| Key legislation | Law on Personal Income Tax; Law on Contributions from Mandatory Social Insurance; Law on Pension and Disability Insurance; Law on Labour Relations (Official Gazette 62/05 et seq., latest 111/23); Law on Minimum Salary (amendments Official Gazette 41/2022; 2025 amount in Official Gazette 68/25) |
| Filing portal | UJP e-services (MPIN electronic declaration) |
| Income tax | **Flat 10%** on employment income (games of chance 15%); reverted to flat 10% from 2020 (PwC) |
| Validated by | Pending -- requires sign-off by a licensed Macedonian accountant |
| Skill version | 0.1 |

### The three most important North Macedonia facts

> **1. Personal income tax is a FLAT 10%.** It applies to employment income (and most other income — self-employment, royalties/IP, rental, capital, capital gains, insurance, other income); games of chance are 15%; securities held > 2 years have a 0% capital-gains rate. There are no progressive bands for ordinary salary. (PwC — Taxes on personal income)
>
> **2. The PIT base is gross MINUS contributions MINUS the personal allowance.** Mandatory social contributions are FULLY deductible from the PIT base, and a monthly personal allowance of **MKD 10,270** is exempt before the 10% applies. (Eurofast Tax Card 2025)
>
> **3. The 28% social contributions are EMPLOYEE-borne.** Pension & Disability 18.8% + Health 7.5% + Unemployment/Employment 1.2% + Additional/Disability 0.5% = **28.0%**, all withheld from the employee's gross. The employer adds **NOTHING** on top of gross. (Eurofast Tax Card 2025; PwC)

## Section 2 -- Income Tax Withholding (данок на личен доход)

The employer withholds personal income tax (PIT) monthly. North Macedonia operates a **single flat rate** with no brackets for employment income.

### PIT rate schedule (2025)

**PIT rate schedule (2025)**  _(PwC)_

| Income type | Rate | Source |
| --- | --- | --- |
| Employment income (salary) | **10%** (flat) | PwC |
| Self-employment, royalties/IP, rental, capital, capital gains, insurance, other income | 10% (flat) | PwC |
| Games of chance | 15% | PwC |
| Capital gains on securities held > 2 years | 0% | PwC |

> **Historical note:** A progressive PIT (10% / 18%) was introduced for 2019 only and then suspended; North Macedonia reverted to the flat 10% from 2020 onward. (PwC)

### PIT base formula and the monthly personal allowance

- **Monthly withholding mechanics** — contributions = contribution_base x 28% PIT_base      = gross_salary - contributions - personal_allowance PIT           = max(PIT_base, 0) x 10%  _(PwC)_

**PIT base items table**  _(Eurofast Tax Card 2025)_

| Item | Value | Source |
| --- | --- | --- |
| Income tax rate on salary | 10% (flat) | PwC |
| Monthly personal allowance (PIT exemption for salary earners) | **MKD 10,270** | Eurofast Tax Card 2025 |
| Deductibility of contributions | Whole 28% is deductible from the PIT base | Eurofast Tax Card 2025 |

- **Employer computation process** — The employer computes gross salary, deducts the 28% mandatory social contributions, subtracts the monthly personal allowance (MKD 10,270), and applies the flat 10% PIT to the resulting base. Net pay, contributions, and PIT are paid concurrently via a single encrypted payment order generated from the MPIN declaration.  _(Eurofast Payroll Guide 2025)_

> **Note:** The personal allowance is the salary earner's PIT-free amount; it is NOT deducted from the contribution base — contributions are computed on the full (clamped) gross before the allowance. Only the 10% PIT benefits from the allowance.

## Section 3 -- Social Contributions (придонеси) -- Contribution Table (2025)

- **Contribution base and employee-borne nature** — All mandatory social contributions are computed on the employee's gross salary, clamped between the minimum and maximum contribution bases (Section 3.2). Every component is employee-borne (withheld from gross) and remitted by the employer; the employer adds nothing on top of gross.  _(Eurofast Tax Card 2025; PwC)_

### 3.1 Contribution rates (2025)

**Contribution rates table**  _(Eurofast Tax Card 2025)_

| Fund | Employee (withheld) | Employer (on top of gross) | Total | Source |
| --- | --- | --- | --- | --- |
| Pension and Disability Insurance (Pension Fund / PIOM — Фонд за ПИОМ) | 18.8% | 0% | 18.8% | Eurofast Tax Card 2025 |
| Health Insurance (Health Fund / FZOM — Фонд за здравство) | 7.5% | 0% | 7.5% | Eurofast Tax Card 2025 |
| Employment / Unemployment Insurance (Unemployment Fund) | 1.2% | 0% | 1.2% | Eurofast Tax Card 2025 |
| Additional health / Disability and bodily-injury insurance | 0.5% | 0% | 0.5% | PwC (Other taxes) |
| **TOTAL mandatory social contributions** | **28.0%** | **0%** | **28.0%** | Eurofast Tax Card 2025 |

**Arithmetic check (component rows sum to the TOTAL row):**
- Employee column: 18.8 + 7.5 + 1.2 + 0.5 = **28.0%** ✓
- Employer column: 0 + 0 + 0 + 0 = **0%** ✓ (no employer-side contribution on top of gross)
- Total column: 28.0 + 0 = **28.0%** ✓

> **Label discrepancy on the 0.5% component.** The Eurofast Tax Card 2025 lists the four funds as Pension 18.8%, Health 7.5%, Unemployment 1.2%, Disability 0.5%; PwC and several secondary sources describe the 0.5% as "additional health insurance." The TOTAL (28%) and the other three components are consistent across all authoritative sources, so the 0.5% is included either way. (Eurofast Tax Card 2025; PwC) **An outlier source (Rivermate) reports 7.3% health / 27.3% total and a 4× ceiling — this was NOT used; Eurofast + PwC (28% total, 16× ceiling) are treated as authoritative.** **[RESEARCH GAP — reviewer to confirm the exact label/allocation of the 0.5% against the Law on Contributions from Mandatory Social Insurance.]**

### 3.2 Contribution base — floor and ceiling (2025)

- **Basis of floor/ceiling** — Contributions are computed on the gross salary clamped between a minimum and a maximum base, both expressed as a multiple of the national average gross monthly salary.  _(Eurofast Tax Card / Payroll Guide 2025)_

**Contribution base floor/ceiling table**  _(Eurofast Payroll Guide 2025)_

| Threshold | Basis | 2025 value | Source |
| --- | --- | --- | --- |
| National average gross monthly salary (reference) | — | **MKD 63,154** | Eurofast Payroll Guide 2025 |
| Minimum contribution base (floor) | 50% of national average gross salary | **≈ MKD 31,577** (0.5 × 63,154) | Eurofast Tax Card 2025 |
| Maximum contribution base (ceiling) | 16 × national average gross salary | **≈ MKD 1,010,464** (16 × 63,154) | Eurofast Payroll Guide 2025 |

- **Floor/ceiling application** — Floor 31,577 < ceiling 1,010,464 (consistency check ✓). Gross below the floor is brought up to the floor for contribution purposes; gross above the ceiling bears no contributions on the excess (PIT still applies to the full base).  _(Eurofast Tax Card / Payroll Guide 2025)_

> **[RESEARCH GAP — reviewer to confirm the current published national average gross salary base.]** The MKD 63,154 figure is the value cited for 2025 by Eurofast; the PRO / State Statistical Office updates this periodically, so confirm the current published base before computing the floor/ceiling in late 2025 / 2026.

## Section 4 -- Conservative Defaults

When an input is ambiguous, apply the conservative default below and flag it for the reviewer.

**Conservative defaults table**

| Ambiguity | Conservative default | Rationale |
| --- | --- | --- |
| National average gross salary base unknown | Use **MKD 63,154/month** as the 2025 reference for the floor/ceiling | Stated in the Eurofast 2025 guides; the official base is updated periodically by the PRO / State Statistical Office (Eurofast Payroll Guide 2025) |
| Who bears the contributions | Treat all **28% as employee-borne** (withheld from gross); employer cost on top = **0%** | All consulted authoritative sources confirm there is no separate employer contribution; the employer only remits (Eurofast Tax Card / Payroll Guide 2025) |
| Minimum wage period within 2025 unclear | Apply the **March-onward MKD 36,037 gross** figure for current full-year hires | Jan–Feb 2025 used a lower interim figure before the March indexation; use the March-onward figure for current calculations (Official Gazette 68/25) |
| Gross below the floor | Bring the contribution base UP to **MKD 31,577** (50% of average) | Contributions must be on at least the minimum base, even if actual pay is lower (Eurofast Tax Card 2025) |
| Gross above the ceiling | Cap the contribution base at **MKD 1,010,464**; the excess bears 10% PIT but NO contributions | The ceiling is a hard cap on all funds (Eurofast Payroll Guide 2025) |
| Personal allowance entitlement unclear | Apply the **MKD 10,270/month** salary-earner allowance to the PIT base | This is the standard monthly exemption for salary earners (Eurofast Tax Card 2025) |
| Unknown worker status | Assume **employee** (employer withholds 28% + 10% PIT and remits via MPIN) | Employment income has no de-minimis threshold; default to the withholding obligation |

> **Note on the 0.5% component.** Whether the 0.5% is labelled "disability" (Eurofast) or "additional health" (PwC), it is included in the 28% total either way; the choice of label does not change any computation.

## Section 5 -- Required Inputs and Refusal Catalogue

### Required inputs

**Minimum viable** — gross monthly salary and confirmation that the worker is an employee (not self-employed). Without a gross figure, STOP.

**Recommended** — confirmation of the pay period (to pick the correct 2025 minimum wage tier), whether the gross is below the floor or above the ceiling, and confirmation that the standard MKD 10,270 personal allowance applies.

**Ideal** — payslip showing the per-fund split, the MPIN declaration for the month, the M1 employment registration, the latest published national average gross salary base, and the annual PIT draft return prepared by the PRO.

### Refusal catalogue

- **R-MK-PAY-1 — Gross figure unknown** — Trigger: no gross monthly salary provided. Message: "A gross monthly salary is mandatory. Contributions are 28% of the (clamped) gross, and the 10% PIT base is gross minus contributions minus the MKD 10,270 personal allowance. Cannot proceed without the gross figure."
- **R-MK-PAY-2 — Payroll arrears / late-payment quantification** — Trigger: client has unpaid contributions or withheld PIT from prior periods and wants the arrears + interest quantified. Message: "Overdue social contributions and withheld PIT accrue penalty interest of 0.03% per day plus possible administrative fines and PRO/labour inspections. Exact arrears and interest must be confirmed against a PRO statement. Escalate to a North Macedonia-qualified accountant — do not estimate arrears."  _(PwC — Corporate tax administration)_
- **R-MK-PAY-3 — Payroll-declaration penalty schedule** — Trigger: client wants the exact monetary fine for failing to file or pay the MPIN declaration on time. Message: "Late payment carries 0.03% per-day penalty interest, and general non-compliance carries 'fines plus interest', but a payroll-declaration-specific monetary fine schedule (separate from the per-day interest) was not found in consulted authoritative sources — published EUR fine ranges relate to VAT/CIT returns, not the MPIN. [RESEARCH GAP — reviewer to confirm against the Law on Contributions / Tax Procedure Law.] Escalate to a North Macedonia-qualified accountant."
- **R-MK-PAY-4 — Cross-border / posted-worker / treaty coverage** — Trigger: employee works across borders, is a posted worker, or claims treaty/totalisation relief. Message: "Cross-border social-security coordination and which state's contributions apply is outside the scope of this skill. Escalate to a North Macedonia-qualified accountant."
- **R-MK-PAY-5 — Self-employed / non-employment income** — Trigger: the worker is self-employed or the income is royalties, rental, capital, or games-of-chance. Message: "This skill covers EMPLOYED persons (employer withholds 28% contributions + 10% PIT and remits via MPIN). Self-employment and other income types are taxed at 10% (games of chance 15%) under different mechanics — route to a North Macedonia income-tax skill or a qualified accountant."

## Section 6 -- Payment Pattern Library

Deterministic pre-classifier for Macedonian bank-statement lines related to payroll. Match by case-insensitive substring on the counterparty/reference as it appears in the statement. References may be Cyrillic or transliterated Latin. Currency is MKD.

### 6.1 Employer debits -- remittances to the PRO / funds

**Employer debit patterns to PRO/funds**

| Pattern | Classification | Notes |
| --- | --- | --- |
| УЈП, UJP, УПРАВА ЗА ЈАВНИ ПРИХОДИ, PRO | Contribution + PIT remittance to the Public Revenue Office | MPIN single encrypted payment order |
| МПИН, MPIN | MPIN integrated-collection payment | Bundles net pay, contributions and PIT |
| ПРИДОНЕСИ, PRIDONESI, SOCIAL CONTRIBUTIONS | Social-contribution remittance (28%) | Employee-borne, remitted by employer |
| ПИОМ, PIOM, ПЕНЗИСКИ ФОНД, PENSION | Pension & Disability (18.8%) | Component of the 28% |
| ФЗОМ, FZOM, ЗДРАВСТВЕНО ОСИГУРУВАЊЕ, HEALTH | Health insurance (7.5%) | Component of the 28% |
| ВРАБОТУВАЊЕ, UNEMPLOYMENT, AVRSM | Unemployment/Employment (1.2%) | Component of the 28% |
| ДАНОК НА ЛИЧЕН ДОХОД, ДЛД, PERSONAL INCOME TAX, PIT | 10% flat PIT withheld | NOT a contribution — tag separately |

### 6.2 Employer debits -- net wages to employees

**Employer debit patterns net wages**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ПЛАТА, PLATA, НЕТО ПЛАТА, NETO PLATA, SALARY, WAGES | Net salary disbursement (payroll expense) | Net of withheld contributions + PIT |
| АВАНС, AVANS, ADVANCE | Salary advance (part of net wage) | Reconcile against the month's net pay |

### 6.3 Employee credits -- pay received

**Employee credit patterns**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ПЛАТА, PLATA, SALARY (incoming) | Net employment income received | Already net of contributions + PIT |
| ПЕНЗИЈА, PENZIJA, PENSION (incoming) | PIOM pension benefit | NOT employment income; not a payroll item |
| НАДОМЕСТОК, NADOMESTOK, BENEFIT (incoming) | Unemployment/sickness benefit | NOT employment income |

### 6.4 Bank-specific debit descriptions

**Bank-specific debit descriptions table**

| Bank | Typical debit description | Classification |
| --- | --- | --- |
| Komercijalna banka | "УЈП ПРИДОНЕСИ" / "UJP CONTRIB" | Contribution + PIT remittance |
| Stopanska banka | "МПИН ПЛАТА" / "MPIN SALARY" | MPIN integrated payment |
| NLB banka | "ПРИДОНЕСИ + ДЛД" / "CONTRIB + PIT" | Contribution / PIT |
| Halkbank | "ПИОМ / ФЗОМ" | Pension / health contribution |

## Section 7 -- Worked Examples

Realistic Skopje-based payroll scenarios for a hypothetical employer. Currency is MKD. The 2025 figures apply: 28% employee-borne contributions, flat 10% PIT, MKD 10,270 monthly personal allowance, floor MKD 31,577, ceiling MKD 1,010,464. Every figure below is recomputed end-to-end.

### Example 1 -- Minimum-wage employee (gross MKD 36,037, from March 2025)

**Input line:**
`15.04.2025 ; МПИН ПЛАТА 03/2025 ; DEBIT ; МИНИМАЛНА ПЛАТА ; -24,378.98 ; MKD`

**Reasoning:**
Gross MKD 36,037 (the March-onward 2025 minimum wage, Official Gazette 68/25). It is above the floor (31,577) and below the ceiling, so the contribution base = MKD 36,037.
- Contributions = 28% × 36,037 = **MKD 10,090.36**
- PIT base = 36,037 − 10,090.36 − 10,270 = MKD 15,676.64; PIT = 10% × 15,676.64 = **MKD 1,567.66**
- **Net pay** = 36,037 − 10,090.36 − 1,567.66 = **MKD 24,378.98** (≈ MKD 24,379, matching the published minimum-wage net)
- Employer remittance to the PRO = contributions 10,090.36 + PIT 1,567.66 = **MKD 11,658.02**.

**Classification:** Net wage MKD 24,378.98 to employee; combined contributions + PIT MKD 11,658.02 to the PRO via MPIN by the 15th. The employer adds nothing on top of gross — total employer cost is the MKD 36,037 gross.

### Example 2 -- Standard salary (gross MKD 50,000)

**Input line:**
`15.06.2025 ; УЈП ПРИДОНЕСИ + ДЛД 05/2025 ; DEBIT ; ПЛАТА ; -16,573.00 ; MKD`

**Reasoning:**
Gross MKD 50,000 is between the floor and the ceiling, so the contribution base = MKD 50,000.
- Contributions = 28% × 50,000 = **MKD 14,000.00** (Pension 9,400 + Health 3,750 + Unemployment 600 + Additional/Disability 250)
- PIT base = 50,000 − 14,000 − 10,270 = MKD 25,730.00; PIT = 10% × 25,730 = **MKD 2,573.00**
- **Net pay** = 50,000 − 14,000 − 2,573 = **MKD 33,427.00**
- Employer remittance = 14,000 + 2,573 = **MKD 16,573.00**.

**Classification:** Net wage MKD 33,427.00; combined contributions + PIT MKD 16,573.00 to the PRO. Component split confirms the 28% (9,400 + 3,750 + 600 + 250 = 14,000 ✓).

### Example 3 -- Salary at the national average (gross MKD 63,154)

**Input line:**
`15.08.2025 ; МПИН 07/2025 ; DEBIT ; ПРОСЕЧНА ПЛАТА ; -21,203.21 ; MKD`

**Reasoning:**
Gross MKD 63,154 equals the national average gross salary; below the ceiling, so the contribution base = MKD 63,154.
- Contributions = 28% × 63,154 = **MKD 17,683.12**
- PIT base = 63,154 − 17,683.12 − 10,270 = MKD 35,200.88; PIT = 10% × 35,200.88 = **MKD 3,520.09**
- **Net pay** = 63,154 − 17,683.12 − 3,520.09 = **MKD 41,950.79**
- Employer remittance = 17,683.12 + 3,520.09 = **MKD 21,203.21**.

**Classification:** Net wage MKD 41,950.79; combined remittance MKD 21,203.21.

### Example 4 -- Low-paid / part-time below the contribution floor (gross MKD 25,000)

**Input line:**
`15.05.2025 ; УЈП ПРИДОНЕСИ 04/2025 ; DEBIT ; НИСКА ПЛАТА ; -9,841.56 ; MKD`

**Reasoning:**
Gross MKD 25,000 is **below the minimum contribution base (MKD 31,577)**, so contributions are computed on the floor, not on actual gross.
- Contribution base (floored) = **MKD 31,577**; contributions = 28% × 31,577 = **MKD 8,841.56**
- PIT base = 25,000 − 8,841.56 − 10,270 = MKD 5,888.44; PIT = 10% × 5,888.44 = **MKD 588.84**
- **Net pay** = 25,000 − 8,841.56 − 588.84 = **MKD 15,569.60**
- Employer remittance = 8,841.56 + 588.84 = **MKD 9,430.40**.

**Classification:** Contributions are on the MKD 31,577 floor even though gross is lower; PIT is on actual gross minus those (floored) contributions minus the allowance. Note: most legitimate full-time hires must be at least the minimum wage (MKD 36,037) — a gross of MKD 25,000 implies part-time/partial-month work; flag for the reviewer.

### Example 5 -- High earner above the contribution ceiling (gross MKD 1,200,000)

**Input line:**
`15.07.2025 ; МПИН 06/2025 ; DEBIT ; ВИСОКА ПЛАТА ; -373,609.93 ; MKD`

**Reasoning:**
Gross MKD 1,200,000 exceeds the maximum contribution base (MKD 1,010,464). Contributions are computed only up to the ceiling:
- Contribution base (capped) = **MKD 1,010,464**; contributions = 28% × 1,010,464 = **MKD 282,929.92**
- Income above the ceiling (MKD 189,536) bears NO contributions.
- PIT base = 1,200,000 − 282,929.92 − 10,270 = MKD 906,800.08; PIT = 10% × 906,800.08 = **MKD 90,680.01**
- **Net pay** = 1,200,000 − 282,929.92 − 90,680.01 = **MKD 826,390.07**
- Employer remittance = 282,929.92 + 90,680.01 = **MKD 373,609.93**.

**Classification:** Contributions clamped to MKD 1,010,464; the 10% PIT applies to the full gross minus the (capped) contributions minus the allowance. High salaries do NOT scale contributions proportionally.

### Example 6 -- New hire requiring M1 employment registration

**Input line:**
`02.03.2025 ; АВРМ M1 РЕГИСТРАЦИЈА ; INFO ; ПРИЈАВА ВРАБОТУВАЊЕ ; 0.00 ; MKD`

**Reasoning:**
This is not a payment but an employment-registration event. The vacancy must first be published on the Employment Agency (AVRSM) portal — registration of the employment relationship is only possible after **3 working days** — and the M1 document proves the registration. Employment must be registered before it is officialised. (Eurofast Payroll Guide 2025)

**Classification:** No payroll amount; compliance event. Confirm the M1 registration was completed before the employee's start date.

## Section 8 -- Tier 1 Rules (deterministic)

Apply exactly as written when inputs are clear.

### Rule 1 -- Personal income tax is a flat 10%

- **PIT formula** — PIT_base = gross_salary - contributions - personal_allowance PIT      = max(PIT_base, 0) x 10%  _(PwC)_
- **No brackets note** — No brackets for salary; games of chance are 15%; reverted to flat 10% from 2020.  _(PwC)_

### Rule 2 -- Contributions are 28% of the (clamped) gross, employee-borne

- **Contribution formula** — contribution_base = clamp(gross_salary, MKD 31,577, MKD 1,010,464) contributions     = contribution_base x 28%   # 18.8% + 7.5% + 1.2% + 0.5% employer_extra    = 0                          # NOTHING on top of gross  _(Eurofast Tax Card 2025; PwC)_
- **All 28% withheld and remitted** — All 28% is withheld from the employee and remitted by the employer.  _(Eurofast Tax Card 2025; PwC)_

### Rule 3 -- The personal allowance is MKD 10,270/month

- **Personal allowance rule** — The monthly personal allowance of MKD 10,270 is exempt from PIT for salary earners (2025). It reduces the PIT base only — not the contribution base.  _(Eurofast Tax Card 2025)_

### Rule 4 -- Contributions apply only between the floor and the ceiling

- **Floor/ceiling rule** — Gross below MKD 31,577 (50% of the national average gross salary) is brought up to the floor; gross above MKD 1,010,464 (16× the average) bears no contributions on the excess. PIT still applies to the full base.  _(Eurofast Tax Card / Payroll Guide 2025)_

### Rule 5 -- No separate employer-side contribution

- **No employer top-up rule** — Unless a special law requires otherwise, the employer makes NO social contribution on top of gross; it only withholds and remits the employee's 28%. The employer's payroll cost equals the gross salary.  _(Eurofast Tax Card / Payroll Guide 2025)_

### Rule 6 -- Monthly remittance via MPIN and deadlines

- **MPIN remittance deadlines** — The employer files the electronic PIT/contribution calculation to the PRO for approval by the 10th of the month following the salary month, and pays the contributions and withheld PIT by the 15th of that month, via a single encrypted MPIN payment order that also disburses net pay.  _(PwC — Tax administration; Eurofast Payroll Guide 2025)_

### Rule 7 -- Minimum wage

- **2025 minimum wage** — MKD 36,037 gross / MKD 24,379 net per month, effective March 2025. Jan–Feb 2025 used a lower interim figure.  _(Pepeljugoski / Official Gazette 68/25)_

### Rule 8 -- Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| MPIN (Месечна пресметка за интегрирана наплата — Monthly Integrated Collection declaration) | Monthly electronic payroll declaration reporting gross salaries, contributions, personal allowances and withheld PIT; functions as a single encrypted payment order for net pay, contributions and PIT for all employees | Electronic calculation filed to PRO for approval by the 10th; payment by the 15th of the month following the salary month | PwC |
| Annual PIT return (draft prepared by the PRO) | Since 2019 individuals do not self-file; the PRO prepares a draft annual return | Draft delivered by 30 April; taxpayer confirms/corrects by 31 May of the year following the tax year; if no action, the draft becomes final | PwC |
| M1 / employment registration (Employment Agency) | Registration of the employment relationship; vacancy first published on the AVRSM portal (registration only after 3 working days); M1 document proves registration | Before employment commences | Eurofast Payroll Guide 2025 |

### Rule 9 -- Penalty interest and statute of limitations

- **Penalty interest and statute of limitations** — Late payment of tax/contributions accrues penalty interest of 0.03% per day. The statute of limitations is 5 years from the end of the calendar year of the tax event (10 years for tax evasion).  _(PwC — Corporate tax administration)_

### Rule 10 -- Employer-entity context (informational)

- **CIT and VAT threshold context** — Corporate income tax is a flat 10%; the VAT registration threshold is MKD 2,000,000 annual turnover — context for the employer entity, not payroll-specific.  _(Eurofast Tax Card 2025; Mondaq)_

## Section 9 -- Tier 2 Catalogue (reviewer judgement)

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- National average gross salary base outdated

*Trigger:* computation in late 2025 / 2026 or where the published base may have changed. *Issue:* the floor (MKD 31,577) and ceiling (MKD 1,010,464) derive from the MKD 63,154 average; if the PRO has published a newer base, both shift. *Action:* confirm the current published average before computing the floor/ceiling. **[RESEARCH GAP.]**

### T2-2 -- Minimum-wage period within 2025

*Trigger:* salary computed for January or February 2025. *Issue:* a lower interim minimum wage applied before the March MKD 36,037 indexation (Official Gazette 68/25). *Action:* flag for reviewer; confirm which minimum-wage tier applies to the period. **[RESEARCH GAP — the Jan–Feb 2025 interim figure was not captured here.]**

### T2-3 -- 0.5% component label/allocation

*Trigger:* a payslip or fund statement that itemises the 0.5%. *Issue:* Eurofast labels it "disability"; PwC labels it "additional health." *Action:* the 28% total is unaffected; confirm the per-fund allocation against the Law on Contributions if the per-fund split is material. **[RESEARCH GAP.]**

### T2-4 -- Gross below the floor (part-time / partial month)

*Trigger:* gross below MKD 31,577. *Issue:* contributions must be on the floor, not actual gross; this also implies part-time/partial-month work that may need legal review. *Action:* apply the floor to contributions and flag the employment arrangement for the reviewer.

### T2-5 -- Special-law employer contribution

*Trigger:* a sector or arrangement where a special law imposes an employer-side charge on top of gross. *Issue:* the default 0% employer contribution may not hold. *Action:* flag for reviewer; the standard rule assumes no employer top-up. **[RESEARCH GAP — no specific special-law charge was identified in consulted sources.]**

### T2-6 -- Payroll arrears, interest and fines

*Trigger:* unpaid contributions or PIT from prior periods. *Issue:* 0.03%/day penalty interest plus possible fines, but no payroll-specific fine schedule was found. *Action:* do not quantify arrears without a PRO statement; escalate to a qualified accountant. **[RESEARCH GAP — payroll-declaration fine schedule.]**

### T2-7 -- M1 registration and start-date sequencing

*Trigger:* a new hire. *Issue:* the vacancy must be published and the 3-working-day window observed before registration; the M1 must be in place before work starts. *Action:* confirm the M1 registration date precedes the start date.

## Section 10 -- Excel Working Paper Template

```
NORTH MACEDONIA PAYROLL -- WORKING PAPER
Client / Employer: [name]
Tax Year: [2025]    Currency: MKD
Prepared: [date]

INPUT DATA
  Employee name:                 [____]
  Pay period (month):            [____]   (Jan-Feb 2025 use interim min wage)
  Gross monthly salary:          [____]

CONTRIBUTION BASE
  National average gross salary: [MKD 63,154]
  Minimum base (50% of average): [MKD 31,577]
  Maximum base (16x average):    [MKD 1,010,464]
  Contribution base (clamped):   [____]

SOCIAL CONTRIBUTIONS (employee-borne; employer adds 0% on top)
  Pension & Disability (PIOM) 18.8%:     [____]
  Health (FZOM) 7.5%:                    [____]
  Unemployment / Employment 1.2%:        [____]
  Additional / Disability 0.5%:          [____]
  TOTAL contributions (28%):             [____]

INCOME TAX (flat 10%)
  Personal allowance (monthly):          [MKD 10,270]
  PIT base (gross - contrib - allowance):[____]   (floor at 0)
  PIT (10%):                             [____]

NET PAY
  Gross - contributions - PIT:           [____]

EMPLOYER REMITTANCE (MPIN, by the 15th of the following month)
  MPIN calculation filed by 10th:        [YES/NO]
  Contributions + PIT remitted by 15th:  [____]
  M1 employment registration (new hire): [YES/NO]

REVIEWER FLAGS
  [List any Tier 2 flags and RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 11 -- Bank Statement / Terminology Reading Guide

References commonly appear in Cyrillic; some banks transliterate to Latin. Currency is MKD.

**Terminology reading guide table**

| Macedonian term | Transliteration | Meaning |
| --- | --- | --- |
| Плата | Plata | Salary / wage |
| Нето плата | Neto plata | Net salary |
| Бруто плата | Bruto plata | Gross salary |
| Придонеси | Pridonesi | Social contributions |
| ПИОМ (Пензиско и инвалидско осигурување) | PIOM | Pension and Disability Insurance Fund |
| ФЗОМ (Фонд за здравствено осигурување) | FZOM | Health Insurance Fund |
| Данок на личен доход (ДЛД) | Danok na lichen dohod (DLD) | Personal income tax (10% flat) |
| Личен ослободување | Lichen oslobóduvanje | Personal allowance |
| Минимална плата | Minimalna plata | Minimum wage |
| УЈП (Управа за јавни приходи) | UJP | Public Revenue Office |
| МПИН | MPIN | Monthly Integrated Collection declaration |
| Просечна плата | Prosechna plata | Average salary (contribution-base reference) |
| АВРМ (Агенција за вработување) | AVRSM | Employment Agency |

**Identification tips:**
1. Contribution/PIT debits are outgoing (DEBIT) to the PRO (УЈП) and recur monthly around the 15th.
2. A single MPIN debit may bundle social contributions + the 10% PIT — split by reference (ПРИДОНЕСИ = contributions; ДЛД = income tax).
3. The net wage to the employee (ПЛАТА outgoing) is separate from the PRO remittance.
4. There is NO separate employer-contribution debit on top of gross — do not expect one.
5. Gross above the MKD 1,010,464 ceiling produces no additional contribution; gross below MKD 31,577 still attracts contributions on the floor.
6. Do not confuse outgoing contribution debits with incoming PIOM pension or unemployment-benefit credits (ПЕНЗИЈА pension, НАДОМЕСТОК benefit).

## Section 12 -- Onboarding Fallback

If the client provides only a bank statement and no other information:

1. **Scan for PRO debits** — identify all outgoing payments matching Section 6 patterns (УЈП / МПИН / ПРИДОНЕСИ / ПИОМ / ФЗОМ / ДЛД).
2. **Separate contributions from PIT** — tag ПРИДОНЕСИ / ПИОМ / ФЗОМ as the 28% social contributions; tag ДЛД as the 10% PIT.
3. **Reverse-engineer the base** — for a contribution-only amount, divide by 0.28 to estimate the contribution base; check against the floor (MKD 31,577) and ceiling (MKD 1,010,464). If the implied base equals the ceiling exactly, the employee is at or above the cap; if it equals the floor, the employee earns at or below 50% of average.
4. **Match the net wage** — a ПЛАТА outgoing equals gross minus the 28% contributions minus the 10% PIT (the PIT having allowed MKD 10,270). To recover gross from net is iterative — flag for the reviewer rather than asserting a single figure.
5. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Employment status, gross salary, the applicable national average base, and the personal-allowance entitlement have not been independently verified. Reviewer must confirm before filing the MPIN."

### Calculation summary (2025, MKD; 28% employee contributions, flat 10% PIT, MKD 10,270 allowance)

**Calculation summary (2025, MKD; 28% employee contributions, flat 10% PIT, MKD 10,270 allowance)**  _(Eurofast Tax Card 2025 / PwC; MKD 10,270 allowance (Eurofast Tax Card 2025); floor/ceiling derived from MKD 63,154 average (Eurofast Payroll Guide 2025))_

| Gross monthly | Contribution base | Contributions (28%) | PIT base | PIT (10%) | Net pay |
| --- | --- | --- | --- | --- | --- |
| MKD 25,000 | MKD 31,577 (floored) | MKD 8,841.56 | MKD 5,888.44 | MKD 588.84 | MKD 15,569.60 |
| MKD 36,037 (min wage) | MKD 36,037 | MKD 10,090.36 | MKD 15,676.64 | MKD 1,567.66 | MKD 24,378.98 |
| MKD 50,000 | MKD 50,000 | MKD 14,000.00 | MKD 25,730.00 | MKD 2,573.00 | MKD 33,427.00 |
| MKD 63,154 (average) | MKD 63,154 | MKD 17,683.12 | MKD 35,200.88 | MKD 3,520.09 | MKD 41,950.79 |
| MKD 1,200,000 | MKD 1,010,464 (capped) | MKD 282,929.92 | MKD 906,800.08 | MKD 90,680.01 | MKD 826,390.07 |

All sourced to the rates in Section 3 (Eurofast Tax Card 2025 / PwC), the MKD 10,270 allowance (Eurofast Tax Card 2025), and the floor/ceiling derived from the MKD 63,154 average (Eurofast Payroll Guide 2025).

### Thresholds (with provenance)

**Thresholds (with provenance)**  _(See row-level sources)_

| Item | Value | Source |
| --- | --- | --- |
| Personal income tax rate (salary) | 10% flat (games of chance 15%; securities held > 2 yrs 0%) | PwC |
| Monthly personal allowance | MKD 10,270 | Eurofast Tax Card 2025 |
| Total social contributions | 28.0% (18.8% pension + 7.5% health + 1.2% unemployment + 0.5% additional/disability) | Eurofast Tax Card 2025; PwC |
| Employer contribution on top of gross | 0% | Eurofast Tax Card / Payroll Guide 2025 |
| National average gross monthly salary (base reference 2025) | MKD 63,154 | Eurofast Payroll Guide 2025 **[RESEARCH GAP — confirm current published base]** |
| Minimum contribution base (floor) | 50% of average ≈ MKD 31,577 | Eurofast Tax Card 2025 |
| Maximum contribution base (ceiling) | 16× average ≈ MKD 1,010,464 | Eurofast Payroll Guide 2025 |
| Minimum wage 2025 (from March) | MKD 36,037 gross / MKD 24,379 net | Pepeljugoski / Official Gazette 68/25 |
| Minimum wage Jan–Feb 2025 (interim) | Lower interim figure | Official Gazette **[RESEARCH GAP — exact interim figure not captured]** |
| Corporate income tax (employer context) | 10% flat | Eurofast Tax Card 2025 |
| VAT registration threshold (employer context) | MKD 2,000,000 annual turnover | Mondaq |

### Penalties

**Penalties**  _(See row-level sources)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of tax/contributions | 0.03% per day penalty interest | PwC — Corporate tax administration |
| Statute of limitations | 5 years from end of the calendar year of the tax event (10 years for tax evasion) | PwC |
| Non-compliance (general) | Fines plus interest; possible PRO/labour inspections; no payroll-declaration-specific monetary fine schedule found in consulted authoritative sources | Rivermate **[RESEARCH GAP — confirm payroll-specific fine schedule]** |

### Authorities

- **Public Revenue Office (UJP / PRO — Управа за јавни приходи)** (https://www.ujp.gov.mk) — administers PIT and collects contributions via MPIN.
- **Pension and Disability Insurance Fund (PIOM)** — administers the 18.8% pension contribution.
- **Health Insurance Fund (FZOM)** — administers the 7.5% health contribution.
- **Employment Agency (AVRSM)** — handles employment registration (M1) and the 1.2% unemployment contribution.
- **Ministry of Labour and Social Policy (mtsp.gov.mk)** — sets the minimum wage.

> **Note:** The official PRO (ujp.gov.mk) detailed rate page could not be loaded directly for primary confirmation during research; figures rely on PwC + Eurofast, which closely corroborate. 2025 figures are confirmed; 2026 figures (indexed minimum wage, updated average-salary base) were not officially confirmed and are out of scope. **[RESEARCH GAP — primary PRO confirmation pending.]**

### Test suite

**Test 1:** Gross MKD 36,037 (minimum wage, March 2025). -> Contribution base 36,037; contributions 28% = MKD 10,090.36. PIT base = 36,037 − 10,090.36 − 10,270 = 15,676.64; PIT = MKD 1,567.66. Net = MKD 24,378.98 (≈ published net MKD 24,379). Remittance = MKD 11,658.02.

**Test 2:** Gross MKD 50,000. -> Contributions 28% = MKD 14,000.00 (9,400 + 3,750 + 600 + 250). PIT base = 50,000 − 14,000 − 10,270 = 25,730.00; PIT = MKD 2,573.00. Net = MKD 33,427.00. Remittance = MKD 16,573.00.

**Test 3:** Gross MKD 63,154 (national average). -> Contributions = MKD 17,683.12. PIT base = 63,154 − 17,683.12 − 10,270 = 35,200.88; PIT = MKD 3,520.09. Net = MKD 41,950.79. Remittance = MKD 21,203.21.

**Test 4:** Gross MKD 25,000 (below floor). -> Contribution base floored to MKD 31,577; contributions = MKD 8,841.56. PIT base = 25,000 − 8,841.56 − 10,270 = 5,888.44; PIT = MKD 588.84. Net = MKD 15,569.60. Contributions are on the floor, not actual gross.

**Test 5:** Gross MKD 1,200,000 (above ceiling). -> Contribution base capped at MKD 1,010,464; contributions = MKD 282,929.92. PIT base = 1,200,000 − 282,929.92 − 10,270 = 906,800.08; PIT = MKD 90,680.01. Net = MKD 826,390.07. Income above the ceiling bears no contribution.

**Test 6:** Component-split check on Test 2 (gross 50,000). -> Pension 18.8% = 9,400; Health 7.5% = 3,750; Unemployment 1.2% = 600; Additional/Disability 0.5% = 250; sum = MKD 14,000 = 28% ✓.

**Test 7:** Employer-cost check (gross 50,000). -> Employer adds 0% on top of gross; total employer payroll cost = MKD 50,000 (the gross). No separate employer contribution debit should appear.

**Test 8:** New hire without an M1 registration filed. -> Compliance breach; employment must be registered (vacancy published, 3-working-day window, M1 issued) before work starts. Flag for reviewer (refusal R-MK-PAY-3 / T2-7).

**Test 9:** Worker is self-employed or income is games-of-chance. -> Out of scope for this employee-payroll skill; 10% applies to most income, 15% to games of chance, under different mechanics. Route per refusal R-MK-PAY-5.

- **R-MK-PAY-3 / T2-7** — New hire without an M1 registration filed is a compliance breach; employment must be registered before work starts.  _(Test 8)_
- **R-MK-PAY-5** — Worker is self-employed or income is games-of-chance; out of scope for this employee-payroll skill; route per this refusal code.  _(Test 9)_

## Section 14 -- Interaction with Other Skills

**Section 14 -- Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (10% PIT + 28% contributions) | **This skill (north-macedonia-payroll.md)** |
| North Macedonia VAT returns | north-macedonia-vat.md |
| Self-employed / other-income PIT | A North Macedonia income-tax skill or a qualified accountant |
| Employer corporate income tax (10%) | A North Macedonia corporate-tax skill or a qualified accountant |

### Key handoff points

- **Payroll -> Bookkeeping:** Gross wages are the employer's expense (there is no separate employer-contribution on-cost); the 28% employee contributions and the 10% PIT are liabilities until remitted to the PRO via MPIN.
- **Payroll -> Income Tax:** Since 2019 individuals do not self-file; the PRO prepares a draft annual return (delivered by 30 April) that becomes final if not corrected by 31 May. Employment income feeds that draft.
- **Payroll -> VAT:** Payroll is unrelated to VAT, but the employer entity may have a VAT obligation above the MKD 2,000,000 turnover threshold — route to `north-macedonia-vat.md`.

## PROHIBITIONS

- **PIT base calculation** — NEVER apply the 10% PIT to raw gross -- the base is gross MINUS the 28% contributions MINUS the MKD 10,270 personal allowance  _(PROHIBITIONS section)_
- **No employer-side contribution** — NEVER add an employer-side social contribution on top of gross -- there is NONE unless a special law requires it; the employer only withholds and remits the employee's 28%  _(PROHIBITIONS section)_
- **Ceiling is hard cap** — NEVER compute contributions on income above the ceiling (MKD 1,010,464) -- the cap is hard  _(PROHIBITIONS section)_
- **Floor enforcement** — NEVER compute contributions on less than the floor (MKD 31,577) when actual gross is lower -- bring the base up to the floor  _(PROHIBITIONS section)_
- **Personal allowance must be applied** — NEVER omit the MKD 10,270 personal allowance from the PIT base for a salary earner  _(PROHIBITIONS section)_
- **Allowance not applied to contributions** — NEVER apply the personal allowance to the contribution base -- it reduces the PIT base only  _(PROHIBITIONS section)_
- **Contributions and PIT are separate** — NEVER conflate the 28% contributions with the 10% PIT -- they are separate items even though both are remitted via MPIN  _(PROHIBITIONS section)_
- **Minimum wage period accuracy** — NEVER use the Jan–Feb 2025 interim minimum wage for a March-onward period (or vice versa) without confirming the period  _(PROHIBITIONS section)_
- **Average-salary base not permanent** — NEVER treat the MKD 63,154 average-salary base as permanent -- confirm the current published base before computing the floor/ceiling  _(PROHIBITIONS section)_
- **M1 registration required before work starts** — NEVER let a new employee start work before the M1 employment registration is in place  _(PROHIBITIONS section)_
- **MPIN deadlines** — NEVER miss the MPIN deadlines (calculation filed by the 10th, payment by the 15th of the following month) -- 0.03%/day penalty interest applies  _(PROHIBITIONS section)_
- **Arrears quantification escalation** — NEVER quantify payroll arrears, interest, or fines without a PRO statement -- escalate to a qualified accountant  _(PROHIBITIONS section)_
- **Estimated outputs disclaimer** — NEVER present payroll computations as definitive -- always label as estimated and direct to a licensed Macedonian accountant  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Macedonian accountant or authorised auditor) before implementation.

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
