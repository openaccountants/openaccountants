---
name: bulgaria-payroll
description: Use this skill whenever asked about Bulgaria payroll processing for employed persons. Trigger on phrases like "Bulgaria payroll", "Bulgarian salary", "заплата", "ZDDFL", "ЗДДФЛ", "flat tax Bulgaria", "10% income tax Bulgaria", "data varhu dohodite", "social security Bulgaria", "осигуровки", "osigurovki", "ДОО", "DOO", "pension fund Bulgaria", "Универсален пенсионен фонд", "Universal Pension Fund", "UPF Bulgaria", "2nd pillar Bulgaria", "health insurance Bulgaria", "здравно осигуряване", "НЗОК", "NZOK", "NHIF", "Declaration 1", "Declaration 6", "Декларация образец 1", "Декларация образец 6", "Obrazets 1", "Obrazets 6", "net salary Bulgaria", "gross to net Bulgaria", "PAYE Bulgaria", "tax withholding Bulgaria", "employer contributions Bulgaria", "employer on-cost Bulgaria", "minimum wage Bulgaria", "минимална работна заплата", "МРЗ", "minimum insurable income", "МОД", "maximum insurable income", "осигурителен доход", "TZPB", "work accident Bulgaria", "NRA", "НАП", "NSSI", "НОИ", "Art. 62 notification", "employment contract registration Bulgaria", or any question about computing employee pay, withholding income tax, or mandatory social/health contributions for Bulgaria-based employees. This skill covers the 10% flat income tax withholding, state social insurance (ДОО) contributions (pension, supplementary 2nd-pillar pension, sickness/maternity, unemployment, work-accident), health insurance, the insurable-income floor and ceiling, minimum wage, the euro changeover from 1 January 2026, Declaration 1 / Declaration 6 filing, and Art. 62 employment-contract registration. ALWAYS read this skill before processing any Bulgaria payroll.
version: 0.1
jurisdiction: BG
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria Payroll

## Bulgaria Payroll Skill v0.1

**Tier 2 — research-verified. Figures below are sourced from the National Revenue Agency (НАП / NRA), the National Social Security Institute (НОИ / NSSI), the Bulgarian Ministry of Economy and Industry, PwC Worldwide Tax Summaries, the European Central Bank, and cross-checked against Big-4-adjacent payroll guides (Leinonen, Lano, Innovires, Eurofast). NOT yet signed off by a licensed Bulgarian accountant (счетоводител) or registered auditor. Treat every computation as an estimate pending professional review. Bulgaria adopts the euro on 1 January 2026 at the irrevocably fixed rate EUR 1 = BGN 1.95583 — this skill carries 2025 BGN figures and shows the EUR equivalents for the changeover.**

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Bulgaria (Republic of Bulgaria / Република България) |
| Currency | BGN (Bulgarian lev) through 31 Dec 2025; EUR from 1 Jan 2026 at the fixed irrevocable rate EUR 1 = BGN 1.95583 (ECB) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | Monthly PAYE -- employer withholds 10% flat advance income tax and all employee social/health contributions; annual reconciliation by the employer at year-end (Lano) |
| Income tax authority | National Revenue Agency (NRA / Национална агенция за приходите, НАП) -- https://nra.bg |
| Social security authority | National Social Security Institute (NSSI / Национален осигурителен институт, НОИ) -- https://www.nssi.bg (contributions collected via the NRA) |
| Health authority | National Health Insurance Fund (NHIF / Национална здравноосигурителна каса, НЗОК) |
| Key legislation | Personal Income Taxes Act (ЗДДФЛ / ZDDFL); Social Insurance Code (Кодекс за социално осигуряване / KSO); Health Insurance Act (ЗЗО / ZZO); Labour Code (Кодекс на труда) Art. 62; annual State Social Insurance Budget Act (ЗБДОО) setting min/max insurable income; Tax-Insurance Procedure Code (ДОПК) |
| Filing portal | NRA e-services (електронни услуги на НАП) |
| Income tax | **Flat 10%** on taxable employment income -- no progressive bands, no general personal allowance for ordinary salary (mi.government.bg; PwC) |
| Validated by | Pending -- requires sign-off by a licensed Bulgarian accountant |
| Skill version | 0.1 |

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Bulgaria-specific content.**

### The single most important Bulgaria facts

> **1. Income tax is a FLAT 10%.** There is no progressive band and no general personal allowance for ordinary salary. The 10% applies to **gross pay minus the employee's own mandatory social and health contributions** -- not to raw gross. (ZDDFL; mi.government.bg)
>
> **2. Contributions are capped.** Both employer and employee social/health contributions stop at the **maximum monthly insurable income** ceiling (BGN 4,130 from 1 Apr 2025 ≈ EUR 2,111.64). Above the ceiling only the 10% income tax continues to apply. (mi.government.bg; PwC)
>
> **3. Work-accident contribution is the only variable.** The Accident at Work and Occupational Disease Fund (TZPB) rate is 0.4%--1.1%, set by the employer's economic-activity risk class, and is paid ENTIRELY by the employer. It is the sole reason the employer/total rate is a band. (PwC)

## Section 2 -- Income Tax Withholding (данък върху доходите, ЗДДФЛ)

The employer withholds income tax monthly under PAYE. Bulgaria operates a **single flat rate** with no brackets.

### Flat Income Tax Rate (2025)

**Flat Income Tax Rate (2025) table**

| Item | Value |
| --- | --- |
| Income tax rate on employment income | **10%** (flat) (mi.government.bg) |
| Tax base | Gross monthly pay **minus** the employee's mandatory social security and health contributions (mi.government.bg) |
| General personal allowance | **None** for ordinary employment income (limited reliefs exist for disability and children, claimed via annual reconciliation) (mi.government.bg) |

- **Income tax rate on employment income** — 10% (flat)  _(mi.government.bg)_

### FSS-equivalent Computation Method

- **Monthly PIT withholding formula** — PIT_base = gross_remuneration - mandatory_employee_contributions PIT      = PIT_base x 10%  _(mi.government.bg)_

There are no status categories, no marital-status rate tables, and no cumulative-projection mechanism such as Malta's FSS. The monthly withholding is mechanically simple. The employer withholds this 10% as **advance** income tax each month and performs an **annual reconciliation** for the employee at year-end. Both the PIT and the contributions are due by the **25th of the following month** (Lano). Remuneration above the insurable-income ceiling still bears 10% PIT on the full (gross minus capped contributions) amount, even though no further contributions accrue above the ceiling.

> **Note on reliefs:** Disability relief and child tax relief reduce the annual base but are claimed at year-end via the employer's annual reconciliation or the individual annual return, not as a monthly per-payslip allowance. Treat ordinary monthly withholding as having no allowance. (mi.government.bg)

## Section 3 -- Social Security and Health -- Contribution Tables (2025)

All social and health contributions are computed on **insurable income**, clamped between the monthly minimum and the monthly maximum (cap). The tables below are for an employee **born on/after 1 January 1960** (the common case). Rates per Leinonen, the Ministry of Economy summary, and PwC; the per-fund employer/employee split is cross-verified between Leinonen and mi.government.bg.

### 3.1 Employee born on/after 1 Jan 1960 (the default case)

**Contribution table -- born on/after 1960**  _(PwC)_

| Fund (Bulgarian) | Employee | Employer | Total | Source |
| --- | --- | --- | --- | --- |
| Pension Fund -- state old-age & death (Пенсионен фонд / ДОО) | 6.58% | 8.22% | 14.8% | Leinonen |
| Supplementary mandatory Universal Pension Fund -- 2nd pillar (ДЗПО / УПФ) | 2.2% | 2.8% | 5.0% | mi.government.bg |
| General Disease & Maternity (Общо заболяване и майчинство) | 1.4% | 2.1% | 3.5% | Leinonen |
| Unemployment (Безработица) | 0.4% | 0.6% | 1.0% | Leinonen |
| Accident at Work & Occupational Disease -- TZPB (ТЗПБ) | 0% | 0.4%--1.1% | 0.4%--1.1% | PwC |
| Health Insurance -- NHIF (НЗОК) | 3.2% | 4.8% | 8.0% | PwC |
| **TOTAL** | **13.78%** | **18.92%--19.62%** | **32.70%--33.40%** | PwC |

**Arithmetic check (component rows sum to the TOTAL row):**
- Employee column: 6.58 + 2.2 + 1.4 + 0.4 + 0 + 3.2 = **13.78%** ✓
- Employer column (low TZPB 0.4%): 8.22 + 2.8 + 2.1 + 0.6 + 0.4 + 4.8 = **18.92%** ✓
- Employer column (high TZPB 1.1%): 8.22 + 2.8 + 2.1 + 0.6 + 1.1 + 4.8 = **19.62%** ✓
- Total (low): 13.78 + 18.92 = **32.70%** ✓; Total (high): 13.78 + 19.62 = **33.40%** ✓

The employer/employee split is roughly 60/40 by design. (PwC)

### 3.2 Employee born before 1 Jan 1960

**Contribution table -- born before 1960**

| Fund | Employee | Employer | Total | Source |
| --- | --- | --- | --- | --- |
| Pension Fund -- state (NO separate 2nd-pillar Universal Pension Fund) | 8.78% (approx) | 11.02% (approx) | 19.8% | Innovires (cites the 19.8% split as 11.88% / 7.92%) |
| General Disease & Maternity | 1.4% | 2.1% | 3.5% | Leinonen |
| Unemployment | 0.4% | 0.6% | 1.0% | Leinonen |
| Accident at Work & Occupational Disease (TZPB) | 0% | 0.4%--1.1% | 0.4%--1.1% | PwC |
| Health Insurance (NHIF) | 3.2% | 4.8% | 8.0% | PwC |

For persons born before 1960 the pension is **19.8%** to the state Pension Fund and there is **NO** separate 5% Universal Pension Fund (Pillar II) contribution -- it is rolled into the state fund. **[RESEARCH GAP -- reviewer to confirm the exact pre-1960 employer/employee split against the KSO; Innovires cites 11.88% / 7.92% within the 19.8%, but this is a secondary source and is not used in the default-case worked examples.]**

### 3.3 Insurable-income floor and ceiling (2025)

**Insurable-income floor and ceiling table**  _(mi.government.bg / PwC)_

| Threshold | 1 Jan -- 31 Mar 2025 | 1 Apr -- 31 Dec 2025 | From 1 Jan 2026 (EUR) | Source |
| --- | --- | --- | --- | --- |
| Minimum monthly insurable income (general floor = min wage) | BGN 933 | BGN 1,077 | -- | mi.government.bg |
| Maximum monthly insurable income (cap, all funds) | BGN 3,750 | BGN 4,130 | ≈ EUR 2,111.64 | mi.government.bg / PwC |

Occupation-specific minimum insurance thresholds (минимални осигурителни доходи) may set a **higher** floor per profession than the general minimum wage. (mi.government.bg)

## Section 4 -- Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Conservative default | Rationale |
| --- | --- | --- |
| Work-accident (TZPB) employer rate unknown | Use **1.1%** (top of band) -> employer 19.62%, combined 33.40% | Avoids under-withholding; the actual 0.4%--1.1% rate is set by economic-activity code (PwC) |
| Employee birth-year / pension scheme unknown | Assume **born on/after 1 Jan 1960** (14.8% pension + 5% Universal Pension Fund) | Pre-1960 employees are now past statutory retirement age; the 19.8% single-fund treatment is increasingly rare |
| Minimum insurable base unclear | Use the higher **occupation-specific** minimum insurance threshold where applicable, otherwise the BGN 1,077 (from 1 Apr 2025) floor | Contributions must be on at least the profession's minimum осигурителен доход, not just the general minimum wage (mi.government.bg) |
| Income above the ceiling | Cap insurable income at **BGN 4,130 / EUR 2,111.64**; income above bears 10% PIT but NO further contributions | The ceiling is a hard cap on all funds (mi.government.bg) |
| Currency for 2026 runs | Convert BGN thresholds at **1.95583** and apply EUR equivalents from 1 Jan 2026 | Euro becomes sole legal tender; dual circulation Jan 2026, BGN cash ends 1 Feb 2026 (ECB) |
| Unknown employment status | Assume employee (employer withholds 13.78% and adds the employer share) | Employment income has no de-minimis threshold; default to the withholding obligation |

> **Note on the default TZPB rate.** Section 3 worked examples use the **low end (0.4%)** to illustrate the minimum employer on-cost, but when the risk class is genuinely unknown for a live run, use 1.1% per the table above. The two figures bracket the employer total at 18.92%--19.62%.

## Section 5 -- Required Inputs and Refusal Catalogue

### Required inputs

**Minimum viable** -- gross monthly remuneration and confirmation that the worker is an employee (not self-employed). Without a gross figure, STOP.

**Recommended** -- employee birth year (to confirm the 5% 2nd-pillar applies vs the pre-1960 19.8% treatment), the employer's work-accident risk class / economic activity (NACE), and whether any occupation-specific minimum insurable income applies.

**Ideal** -- payslip showing the per-fund split, NRA confirmation of contributions paid, the latest Declaration 1 / Declaration 6 filings, the employee's Art. 62 contract notification, and the FS3-equivalent annual income statement.

### Refusal catalogue

- **R-BG-PAY-1** — Trigger: no gross monthly remuneration provided. Message: "A gross monthly remuneration is mandatory. The 10% PIT base is gross minus the employee's contributions, and contributions are a percentage of insurable income clamped between the minimum and maximum thresholds. Cannot proceed without the gross figure."
- **R-BG-PAY-2** — Trigger: client has unpaid contributions or withheld PIT from prior periods and wants the arrears + interest quantified. Message: "Overdue social/health contributions and withheld PIT accrue statutory interest (Bulgarian National Bank base rate + 10 percentage points per annum) plus possible administrative fines. Exact arrears and interest must be confirmed against an NRA statement. Escalate to a Bulgaria-qualified accountant -- do not estimate arrears."
- **R-BG-PAY-3** — Trigger: client wants the exact fine for failing to notify an employment contract to the NRA under Labour Code Art. 62. Message: "Non-registration of an employment contract is penalised; one secondary source reports EUR 7,500--15,000 per case, and the Labour Code sets higher per-violation fines for repeated breaches, but the exact figure must be confirmed against the Labour Code. [RESEARCH GAP -- reviewer to confirm.] Escalate to a Bulgaria-qualified accountant."
- **R-BG-PAY-4** — Trigger: employee works across EU states, holds an A1 certificate, or is a posted worker. Message: "Cross-border social-security coordination (EU Regulation 883/2004, A1 certificates, posted workers) determines which state's contributions apply and is outside the scope of this skill. Escalate to a Bulgaria-qualified accountant."
- **R-BG-PAY-5** — Trigger: the worker is self-employed (самоосигуряващо се лице), not an employee. Message: "This skill covers EMPLOYED persons (employer withholds PIT + contributions). Self-employed/freelancer contributions (27.8% / 31.3%, paid by the individual, reconciled annually) are covered by `bulgaria-social-contributions.md`. Use that skill instead."

## Section 6 -- Payment Pattern Library

Deterministic pre-classifier for Bulgarian bank-statement lines related to payroll. Match by case-insensitive substring on the counterparty/reference as it appears in the statement. References may be Cyrillic or transliterated Latin. From 1 Jan 2026 amounts are EUR-denominated.

### 6.1 Employer debits -- remittances to the NRA

**Employer debits to NRA table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| НАП, NRA, NAP, НАЦ. АГЕНЦИЯ ПРИХОДИ | Contribution + PIT remittance to NRA | All osigurovki + health + PIT are collected by the NRA |
| ОСИГУРОВКИ, OSIGUROVKI, ОСИГУРИТЕЛНИ ВНОСКИ | Social/health contribution remittance | Employer + employee share remitted together |
| ДОО, DOO, ПЕНСИОНЕН ФОНД | State social-security / pension contribution | -- |
| УПФ, UPF, УНИВЕРСАЛЕН ПЕНСИОНЕН | 2nd-pillar Universal Pension Fund | Born on/after 1960 only |
| НЗОК, NZOK, ЗДРАВНИ ОСИГУРОВКИ | Health insurance (NHIF) contribution | -- |
| ДДФЛ, ДОД, ZDDFL, ДАНЪК ВЪРХУ ДОХОДА | 10% flat PIT withheld | NOT a contribution -- tag separately |

### 6.2 Employer debits -- net wages to employees

**Employer debits net wages table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ЗАПЛАТА, ZAPLATA, SALARY, WAGES, ВЪЗНАГРАЖДЕНИЕ | Net salary disbursement (payroll expense) | Net of withheld PIT + employee contributions |
| АВАНС, AVANS, ADVANCE | Salary advance (part of net wage) | Reconcile against the month's net pay |

### 6.3 Employee credits -- pay received

**Employee credits table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ЗАПЛАТА, SALARY (incoming) | Net employment income received | Already net of PIT + employee contributions |
| ПЕНСИЯ, PENSIA, PENSION (incoming) | NSSI pension benefit | NOT employment income; not a payroll item |
| ОБЕЗЩЕТЕНИЕ, OBESHTETENIE, BENEFIT (incoming) | NSSI sickness/maternity/unemployment benefit | NOT employment income |

### 6.4 Bank-specific debit descriptions

**Bank-specific debit descriptions table**

| Bank | Typical debit description | Classification |
| --- | --- | --- |
| UniCredit Bulbank | "НАП ОСИГУРОВКИ" / "NRA SOC SEC" | Contribution + PIT remittance |
| DSK Bank | "НАЦ. АГЕНЦИЯ ПРИХОДИ" / "NRA" | Contribution / PIT |
| Postbank (Eurobank Bulgaria) | "ОСИГУРИТЕЛНИ ВНОСКИ" / "NAP" | Contribution |
| Fibank (First Investment Bank) | "НЗОК" / "ДОО" | Health / social security |

## Section 7 -- Worked Examples

Realistic Sofia-based payroll scenarios for a hypothetical employer. Currency is BGN through 2025 and EUR from 1 Jan 2026. Employees are born after 1959 (so the 2nd pillar applies) and the work-accident class is the 0.4% low end unless stated. Every figure below is recomputed end-to-end.

### Example 1 -- Standard salary below the cap (gross BGN 3,000)

**Input line:**
`25.05.2025 ; НАП ОСИГУРОВКИ 04/2025 ; DEBIT ; ОСИГУРОВКИ + ДДФЛ ; -1,239.66 ; BGN`

**Reasoning:**
Gross BGN 3,000 is below the BGN 4,130 cap, so insurable income = BGN 3,000.
- Employee contributions = 13.78% × 3,000 = **BGN 413.40**
- Employer contributions (0.4% TZPB) = 18.92% × 3,000 = **BGN 567.60**
- PIT base = 3,000 − 413.40 = BGN 2,586.60; PIT = 10% × 2,586.60 = **BGN 258.66**
- **Net pay** = 3,000 − 413.40 − 258.66 = **BGN 2,327.94**
- The combined NRA remittance the employer makes = employee contributions 413.40 + employer contributions 567.60 + PIT 258.66 = **BGN 1,239.66**.

**Classification:** Net wage BGN 2,327.94 to employee; combined contributions + PIT BGN 1,239.66 to NRA by 25 May. Employer-share BGN 567.60 is a deductible payroll on-cost.

### Example 2 -- Minimum-wage employee (gross BGN 1,077)

**Input line:**
`25.06.2025 ; ЗАПЛАТА МАЙ 2025 ; DEBIT ; МИНИМАЛНА РЗ ; -835.73 ; BGN`

**Reasoning:**
Gross BGN 1,077 (the minimum monthly wage / general insurable floor from 1 Apr 2025); below the cap.
- Employee contributions = 13.78% × 1,077 = **BGN 148.41**
- Employer contributions (0.4%) = 18.92% × 1,077 = **BGN 203.77**
- PIT base = 1,077 − 148.41 = BGN 928.59; PIT = 10% × 928.59 = **BGN 92.86**
- **Net pay** = 1,077 − 148.41 − 92.86 = **BGN 835.73**

**Classification:** Net wage BGN 835.73. If the employee's occupation carries a higher minimum insurable threshold, contributions must be recomputed on that higher floor (flag for reviewer).

### Example 3 -- Salary above the cap (gross BGN 6,000)

**Input line:**
`25.07.2025 ; НАП ОСИГУРОВКИ 06/2025 ; DEBIT ; ВИСОКА ЗАПЛАТА ; -1,893.60 ; BGN`

**Reasoning:**
Gross BGN 6,000 exceeds the BGN 4,130 cap. Contributions are computed only up to BGN 4,130:
- Employee contributions = 13.78% × 4,130 = **BGN 569.11**
- Employer contributions (0.4%) = 18.92% × 4,130 = **BGN 781.40**
- Income above BGN 4,130 (BGN 1,870) bears NO contributions.
- PIT, however, applies to full gross minus the (capped) employee contributions: PIT base = 6,000 − 569.11 = BGN 5,430.89; PIT = 10% × 5,430.89 = **BGN 543.09**
- **Net pay** = 6,000 − 569.11 − 543.09 = **BGN 4,887.80**
- Combined NRA remittance = 569.11 + 781.40 + 543.09 = **BGN 1,893.60**.

**Classification:** Insurable income clamped to BGN 4,130; PIT still on the full base. A high salary does NOT scale contributions proportionally.

### Example 4 -- High-risk employer (1.1% work-accident class, gross BGN 3,000)

**Input line:**
`25.05.2025 ; НАП ОСИГУРОВКИ 04/2025 ; DEBIT ; ТЗПБ КЛАС ВИСОК ; -1,260.66 ; BGN`

**Reasoning:**
Same employee as Example 1 (gross BGN 3,000) but the employer's economic-activity risk class carries the top 1.1% TZPB rate, so the employer rate is 19.62%.
- Employee contributions = 13.78% × 3,000 = **BGN 413.40** (unchanged -- TZPB is employer-only)
- Employer contributions = 19.62% × 3,000 = **BGN 588.60** (vs BGN 567.60 at 0.4%)
- PIT = **BGN 258.66** (unchanged)
- Combined NRA remittance = 413.40 + 588.60 + 258.66 = **BGN 1,260.66**.

**Classification:** Only the employer cost changes; the employee net pay (BGN 2,327.94) is identical to Example 1.

### Example 5 -- Euro-era payroll after the changeover (gross EUR 1,500, Jan 2026)

**Input line:**
`25.02.2026 ; НАП ОСИГУРОВКИ 01/2026 ; DEBIT ; OSIGUROVKI + DDFL ; -619.83 ; EUR`

**Reasoning:**
From 1 Jan 2026 all amounts are EUR-denominated at the fixed 1.95583 rate. Gross EUR 1,500 is below the EUR 2,111.64 cap.
- Employee contributions = 13.78% × 1,500 = **EUR 206.70**
- Employer contributions (0.4%) = 18.92% × 1,500 = **EUR 283.80**
- PIT base = 1,500 − 206.70 = EUR 1,293.30; PIT = 10% × 1,293.30 = **EUR 129.33**
- **Net pay** = 1,500 − 206.70 − 129.33 = **EUR 1,163.97**
- Combined NRA remittance = 206.70 + 283.80 + 129.33 = **EUR 619.83**.

**Classification:** EUR-denominated; the 2025 ceiling/rates carry over as EUR equivalents. [RESEARCH GAP -- the 2026 EUR thresholds (max base ≈ EUR 2,111.64, min wage ≈ EUR 620.20) are derived/secondary; reviewer to confirm against the 2026 State Social Insurance Budget Act once published.]

### Example 6 -- New hire requiring Art. 62 registration

**Input line:**
`02.04.2025 ; НАП УВЕДОМЛЕНИЕ ЧЛ.62 ; INFO ; РЕГИСТРАЦИЯ ТРУДОВ ДОГОВОР ; 0.00 ; BGN`

**Reasoning:**
This is not a payment but an employment-contract notification. Under Labour Code Art. 62, the employer must notify the NRA of the contract **within 3 days** of conclusion (3 working days for foreign employers), and the employee may only start work after NRA confirmation. Termination is notified within 7 days. (Innovires / Leinonen)

**Classification:** No payroll amount; compliance event. Confirm the Art. 62 notification was filed before the employee's start date; missing registration carries a penalty (see refusal R-BG-PAY-3).

## Section 8 -- Tier 1 Rules (deterministic)

Apply exactly as written when inputs are clear.

### Rule 1 -- Income tax is a flat 10% on net-of-contributions base

- **PIT formula** — PIT_base = gross_remuneration - mandatory_employee_contributions PIT      = PIT_base x 10% No brackets, no monthly personal allowance.  _(mi.government.bg; PwC)_

### Rule 2 -- Contribution formula (employee born after 1959)

- **Contribution formula** — insurable_income     = clamp(gross_remuneration, minimum_insurable, maximum_insurable) employee_contribution = insurable_income x 13.78% employer_contribution = insurable_income x (18.92% .. 19.62%)   # TZPB 0.4%–1.1% total_contribution    = insurable_income x (32.70% .. 33.40%) Where (1 Apr -- 31 Dec 2025): minimum_insurable = BGN 1,077 (or the higher occupation floor); maximum_insurable = BGN 4,130 = EUR 2,111.64.  _(mi.government.bg / PwC)_

### Rule 3 -- Contributions apply only between the floor and the ceiling

- **Floor/ceiling application** — Income above BGN 4,130 / EUR 2,111.64 bears NO social or health contributions; income below the minimum is brought up to the minimum insurable income.  _(mi.government.bg)_

### Rule 4 -- Health insurance is 8% of the same base

- **Health insurance total rate** — 8.0% total, split 4.8% employer / 3.2% employee, on the same insurable-income base  _(PwC)_

### Rule 5 -- Birth year determines the pension treatment

- **Pension treatment by birth year** — Born on/after 1 Jan 1960: Pension Fund 14.8% (6.58% employee / 8.22% employer) PLUS Universal Pension Fund 5% (2.2% employee / 2.8% employer). Born before 1 Jan 1960: state Pension Fund 19.8%, NO separate 2nd pillar.  _(mi.government.bg; Innovires)_

### Rule 6 -- Work-accident contribution is employer-only

- **TZPB employer-only rule** — The TZPB contribution (0.4%--1.1%, set by the employer's economic-activity risk class) is paid ENTIRELY by the employer and is never withheld from the employee. It is the only reason the employer/total rate is a band.  _(PwC)_

### Rule 7 -- Monthly remittance and deadline

- **Remittance deadline** — The employer withholds the employee share + advance PIT, adds the employer share, and remits combined social/health contributions AND the 10% PIT to the NRA by the 25th of the month following the income month, filing Declaration 1 and Declaration 6.  _(Innovires; Lano)_

### Rule 8 -- Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Declaration Form 1 (Декларация образец № 1 -- Данни за осигуреното лице) | Per-employee monthly declaration of insurable income and social/health contributions | 25th of the following month | Innovires |
| Declaration Form 6 (Декларация образец № 6 -- Данни за дължими вноски и данък по чл. 42 ЗДДФЛ) | Employer-aggregate monthly declaration of total contributions and PIT withheld | 25th of the following month | Innovires |
| NRA contract notification (Уведомление по чл. 62 КТ) | Register/amend an employment contract with the NRA before the employee starts | Within 3 days of conclusion (3 working days for foreign employers); termination within 7 days | Innovires / Leinonen |
| Annual employer income statement (annual wage declaration) | Report all 2025 employment income, contractor payments and qualifying distributions to NRA | 28 February of the following year (29 Feb in leap years) | Eurofast |
| Annual personal income tax return (individual) | Individual annual reconciliation of income tax | 30 April of the following year (5% early-filing discount up to BGN 500) | Lano |

### Rule 9 -- Euro changeover (1 Jan 2026)

- **Euro changeover rule** — From 1 Jan 2026 all amounts are EUR-denominated at the fixed irrevocable rate 1.95583 BGN = 1 EUR; dual circulation runs in January 2026 and BGN cash ends 1 February 2026. The 2025 ceiling BGN 4,130 = EUR 2,111.64.  _(ECB; Leinonen)_

### Rule 10 -- Employer registration / no de-minimis

- **No de-minimis rule** — Any employer paying employment income must register as a contributor with the NRA and withhold PIT + contributions from the first employee; there is no de-minimis threshold for employment income.  _(Innovires)_

## Section 9 -- Tier 2 Catalogue (reviewer judgement)

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Work-accident risk class unknown

Trigger: employer's NACE / economic-activity risk class not provided. Issue: employer total ranges 18.92%--19.62%. Action: default to 1.1% for a conservative estimate, flag for the reviewer to confirm against the State Social Insurance Budget Act annex.

### T2-2 -- Employee born before 1960

Trigger: employee born before 1 Jan 1960. Issue: state Pension Fund is 19.8% with NO 2nd pillar; the per-fund split differs from the headline figures. Action: flag for reviewer; do not apply the 2.2%/2.8% 2nd-pillar split. [RESEARCH GAP -- exact pre-1960 split.]

### T2-3 -- Occupation-specific minimum insurable income

Trigger: employee in a profession with a minimum osiguritelen dohod above the general minimum wage. Issue: using the BGN 1,077 floor understates contributions. Action: flag for reviewer; apply the higher occupation floor.

### T2-4 -- 2026 EUR thresholds not yet confirmed from the budget

Trigger: computation for 2026. Issue: the EUR equivalents (max base ≈ EUR 2,111.64, min wage ≈ EUR 620.20, self-employed min base ≈ EUR 550.66) are derived/secondary. Action: flag for reviewer; confirm against the 2026 State Social Insurance Budget Act once published. [RESEARCH GAP.]

### T2-5 -- Dual status (employee who is also self-employed)

Trigger: worker is both employed and self-employed. Issue: the maximum insurable income ceiling applies across all sources combined. Action: flag for reviewer; route the self-employed leg to `bulgaria-social-contributions.md`.

### T2-6 -- Art. 62 registration and penalties

Trigger: a new hire, contract amendment, or termination. Issue: notification deadlines (3 days / 7 days) and non-registration penalties apply. Action: confirm the Art. 62 notification was filed; do not quantify the fine without the Labour Code. [RESEARCH GAP -- EUR 7,500--15,000 figure is secondary.]

### T2-7 -- Payroll arrears and interest

Trigger: unpaid contributions or PIT from prior periods. Issue: statutory interest = BNB base rate + 10pp per annum, plus possible fines. Action: do not quantify without an NRA statement; escalate to a qualified accountant. [RESEARCH GAP -- interest mechanism is from a secondary summary; confirm against the DOPK.]

## Section 10 -- Excel Working Paper Template

```
BULGARIA PAYROLL -- WORKING PAPER
Client / Employer: [name]
Tax Year: [2025 / 2026]    Currency: [BGN pre-2026 / EUR from 1 Jan 2026]
Prepared: [date]

INPUT DATA
  Employee name:                 [____]
  Birth year:                    [____]   Born on/after 1 Jan 1960: [YES/NO]
  Gross monthly remuneration:    [____]
  Work-accident (TZPB) rate:     [0.4% .. 1.1%]   (employer only; default 1.1% if unknown)
  Occupation min insurable floor:[____]   (if higher than the general minimum)

INSURABLE INCOME
  Minimum monthly insurable:     [BGN 1,077 / occupation floor]
  Maximum monthly insurable cap: [BGN 4,130 / EUR 2,111.64]
  Insurable income (clamped):    [____]

CONTRIBUTIONS (employee born after 1959)
  Pension 14.8%   (6.58% EE / 8.22% ER):  EE [____]  ER [____]
  Universal Pension 5% (2.2/2.8):         EE [____]  ER [____]
  Disease & Maternity 3.5% (1.4/2.1):     EE [____]  ER [____]
  Unemployment 1.0% (0.4/0.6):            EE [____]  ER [____]
  Work-accident 0.4%–1.1% (ER only):                ER [____]
  Health (NHIF) 8.0% (3.2/4.8):           EE [____]  ER [____]
  Employee total (13.78%):                EE [____]
  Employer total (18.92%–19.62%):                   ER [____]

INCOME TAX (flat 10%)
  PIT base (gross - employee contrib.):   [____]
  PIT (10%):                              [____]

NET PAY
  Gross - employee contrib - PIT:         [____]

REMITTANCE (by 25th of following month)
  Declaration 1 filed:           [YES/NO]
  Declaration 6 filed:           [YES/NO]
  Combined NRA remittance (EE + ER contrib + PIT): [____]
  Art. 62 contract notification (new hires): [YES/NO]

REVIEWER FLAGS
  [List any Tier 2 flags and RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 11 -- Bank Statement / Terminology Reading Guide

References commonly appear in Cyrillic; some banks transliterate to Latin. From 1 Jan 2026 amounts are EUR-denominated.

**Terminology table**

| Bulgarian term | Transliteration | Meaning |
| --- | --- | --- |
| Заплата | Zaplata | Salary / wage |
| Възнаграждение | Vaznagrazhdenie | Remuneration |
| Осигуровки / Осигурителни вноски | Osigurovki / Osiguritelni vnoski | Social security contributions |
| ДОО (Държавно обществено осигуряване) | DOO | State social insurance |
| УПФ (Универсален пенсионен фонд) | UPF | Universal Pension Fund (2nd pillar) |
| НЗОК (Национална здравноосигурителна каса) | NZOK | National Health Insurance Fund |
| ДДФЛ / ДОД (данък върху доходите) | DDFL / DOD | Personal income tax (10% flat) |
| ТЗПБ | TZPB | Accident at Work & Occupational Disease fund |
| Минимална работна заплата (МРЗ) | MRZ | Minimum wage |
| Минимален осигурителен доход (МОД) | MOD | Minimum insurable income |
| Максимален осигурителен доход | -- | Maximum insurable income (cap) |
| Уведомление по чл. 62 | Uvedomlenie po chl. 62 | Art. 62 employment-contract notification |

**Identification tips:**
1. Contribution/PIT debits are always outgoing (DEBIT) to the NRA; recur monthly around the 25th.
2. A single NRA debit may bundle social + health + the 10% PIT -- split by reference (ОСИГУРОВКИ = contributions; ДДФЛ/ДОД = income tax).
3. Net wage to the employee (ЗАПЛАТА outgoing) is separate from the NRA remittance.
4. Income above the BGN 4,130 / EUR 2,111.64 ceiling produces no additional contribution.
5. Do not confuse outgoing contribution debits with incoming NSSI benefit credits (ПЕНСИЯ pension, ОБЕЗЩЕТЕНИЕ benefit).

## Section 12 -- Onboarding Fallback

If the client provides only a bank statement and no other information:

1. **Scan for NRA debits** -- identify all outgoing payments matching Section 6 patterns (НАП / ОСИГУРОВКИ / НЗОК / ДОО / УПФ / ДДФЛ).
2. **Separate contributions from PIT** -- tag ОСИГУРОВКИ/ДОО/НЗОК/УПФ as social/health contributions; tag ДДФЛ/ДОД as the 10% PIT.
3. **Reverse-engineer the base** -- for an employer remittance that excludes PIT, divide the contribution by the combined rate (0.3270 at the 0.4% class, up to 0.3340 at 1.1%) to estimate insurable income; check against the BGN 4,130 / EUR 2,111.64 ceiling. If the implied base equals the ceiling exactly, the employee is at or above the cap.
4. **Match the net wage** -- a ЗАПЛАТА outgoing equals gross minus employee contributions minus PIT.
5. **Flag for reviewer:** "Payroll figures derived from bank statement amounts only. Employment status, birth year, work-accident class, and insurable income have not been independently verified. Reviewer must confirm before filing Declaration 1/6."

## Section 13 -- Reference Material

**Section 13 heading**

### Calculation summary (2025, BGN; born after 1959; 0.4% accident class unless noted)

**Calculation summary (2025, BGN; born after 1959; 0.4% accident class unless noted)**  _(Leinonen / mi.government.bg / PwC; BGN 4,130 cap (mi.government.bg); ECB fixed 1.95583 rate)_

| Gross monthly | Insurable income | Employee (13.78%) | Employer (18.92%) | PIT (10% of base) | Net pay |
| --- | --- | --- | --- | --- | --- |
| BGN 1,077 | BGN 1,077 | BGN 148.41 | BGN 203.77 | BGN 92.86 | BGN 835.73 |
| BGN 3,000 | BGN 3,000 | BGN 413.40 | BGN 567.60 | BGN 258.66 | BGN 2,327.94 |
| BGN 6,000 | BGN 4,130 (capped) | BGN 569.11 | BGN 781.40 | BGN 543.09 | BGN 4,887.80 |
| EUR 1,500 (2026) | EUR 1,500 | EUR 206.70 | EUR 283.80 | EUR 129.33 | EUR 1,163.97 |

*All sourced to the rates in Section 3 (Leinonen / mi.government.bg / PwC) and the BGN 4,130 cap (mi.government.bg). EUR figures use the fixed 1.95583 rate (ECB).*

### Thresholds (with provenance)

**Thresholds (with provenance)**  _(mi.government.bg / PwC / Leinonen / ECB)_

| Item | Value | Source |
| --- | --- | --- |
| Income tax rate | 10% flat | mi.government.bg |
| Minimum monthly wage 2025 | BGN 1,077 (from 1 Jan 2025; was BGN 933 in 2024); hourly ≈ BGN 6.49 | mi.government.bg |
| Minimum monthly wage 2026 (EUR) | ≈ EUR 620.20/month (≈ EUR 3.74/hr) | Leinonen **[RESEARCH GAP -- confirm against 2026 budget]** |
| Minimum monthly insurable income | BGN 933 (Jan--Mar 2025) then BGN 1,077 (Apr--Dec 2025); higher per occupation | mi.government.bg |
| Maximum monthly insurable income | BGN 3,750 (Jan--Mar 2025) then BGN 4,130 (Apr--Dec 2025) ≈ EUR 2,111.64 | mi.government.bg / PwC |
| Self-employed min monthly insurable base 2026 | ≈ EUR 550.66 (= BGN 1,077) | PwC **[RESEARCH GAP -- confirm against 2026 budget]** |
| Euro changeover | 1 Jan 2026 at fixed 1.95583 BGN/EUR | ECB |

### Penalties

**Penalties**  _(Innovires / PwC)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Failure to register an Art. 62 contract | Reported EUR 7,500--15,000 per case (secondary); Labour Code sets per-violation fines, higher for repeat breaches | Innovires **[RESEARCH GAP -- confirm against Labour Code]** |
| Late payment of contributions / withheld PIT | Statutory interest = Bulgarian National Bank base rate + 10 percentage points per annum, plus possible administrative fines | PwC **[RESEARCH GAP -- confirm against DOPK]** |

### Authorities

- **NRA / НАП** (https://nra.bg) -- collects ALL contributions and PIT.
- **NSSI / НОИ** (https://www.nssi.bg) -- administers social-insurance benefits.
- **NHIF / НЗОК** -- administers health insurance.

### Test suite

**Test 1:** Employee born 1990, gross BGN 1,077 (minimum), 0.4% class. -> Insurable BGN 1,077. Employee 13.78% = BGN 148.41. Employer 18.92% = BGN 203.77. PIT base = 928.59; PIT = BGN 92.86. Net = BGN 835.73.

**Test 2:** Employee born 1990, gross BGN 3,000, 0.4% class. -> Employee = BGN 413.40. Employer = BGN 567.60. PIT base = 2,586.60; PIT = BGN 258.66. Net = BGN 2,327.94.

**Test 3:** Employee born 1990, gross BGN 6,000, 0.4% class. -> Insurable capped at BGN 4,130. Employee = BGN 569.11. Employer = BGN 781.40. PIT base = 5,430.89; PIT = BGN 543.09. Net = BGN 4,887.80. Income above BGN 4,130 bears no contribution.

**Test 4:** Employer at high TZPB class (1.1%), gross BGN 3,000. -> Employer = 19.62% × 3,000 = BGN 588.60 (vs BGN 567.60 at 0.4%). Employee net unchanged at BGN 2,327.94.

**Test 5:** Employee born 1955 (pre-1960). -> State Pension Fund 19.8%, NO 2nd pillar. Flag for reviewer to confirm the pre-1960 split. **[RESEARCH GAP.]**

**Test 6:** 2026 computation, gross EUR 1,500, employee born 1990. -> Ceiling EUR 2,111.64; rates unchanged. Employee 13.78% = EUR 206.70; employer 18.92% = EUR 283.80; PIT base = 1,293.30; PIT = EUR 129.33; net = EUR 1,163.97.

**Test 7:** New hire starting work without an Art. 62 notification filed. -> Compliance breach; employee may only start after NRA confirmation. Flag the penalty exposure (refusal R-BG-PAY-3).

- **R-BG-PAY-3** — Compliance breach; employee may only start after NRA confirmation. Flag the penalty exposure.  _(Test 7)_

**Test 8:** Worker is self-employed, not an employee. -> Out of scope; route to `bulgaria-social-contributions.md` (27.8% / 31.3%, reconciled annually).

## Section 14 -- Interaction with Other Skills

**Section 14 -- Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (10% PIT + contributions) | **This skill (bulgaria-payroll.md)** |
| Self-employed / freelancer contributions | bulgaria-social-contributions.md |
| Individual annual income tax return | bulgaria-income-tax.md |
| Bulgaria VAT returns | bulgaria-vat-return.md |

### Key handoff points

- **Payroll -> Bookkeeping:** Gross wages and employer-share contributions are expenses; employee-share contributions and the 10% PIT are liabilities until remitted to the NRA.
- **Payroll -> Income Tax:** The annual employer income statement feeds the employee's annual reconciliation. Employment income with no other source generally needs no individual return.
- **Payroll -> Social Contributions:** A worker who is both employed and self-employed shares one annual insurable-income ceiling -- reconcile across sources.

## PROHIBITIONS

- **PIT base exclusion of mandatory contributions** — NEVER apply the 10% PIT to raw gross -- the base is gross MINUS the employee's mandatory contributions  _(PROHIBITIONS)_
- **Hard contribution ceiling** — NEVER compute contributions on income above the monthly ceiling (BGN 4,130 / EUR 2,111.64) -- the cap is hard  _(PROHIBITIONS)_
- **No scaling beyond ceiling** — NEVER tell a high earner that contributions scale with their full salary -- they stop at the ceiling  _(PROHIBITIONS)_
- **TZPB employer-only** — NEVER withhold the work-accident (TZPB) contribution from the employee -- it is employer-only  _(PROHIBITIONS)_
- **2nd pillar age restriction** — NEVER apply the 5% Universal Pension Fund (2nd pillar) to a person born before 1960 -- they pay 19.8% to the state Pension Fund with no 2nd pillar  _(PROHIBITIONS)_
- **Occupation-specific insurable floor** — NEVER use only the general minimum wage as the insurable floor when an occupation-specific minimum is higher  _(PROHIBITIONS)_
- **PIT vs contributions separation** — NEVER conflate the 10% flat PIT with social/health contributions -- they are separate even though both go to the NRA  _(PROHIBITIONS)_
- **Art. 62 notification before start** — NEVER let a new employee start work before the Art. 62 employment-contract notification is confirmed by the NRA  _(PROHIBITIONS)_
- **25th-of-month deadline** — NEVER miss the 25th-of-following-month deadline for Declaration 1, Declaration 6, and payment -- interest and fines apply  _(PROHIBITIONS)_
- **2026 figures unconfirmed** — NEVER treat any contested or unpublished 2026 figure as confirmed -- use the carried-over 2025 EUR equivalents and flag the RESEARCH GAP  _(PROHIBITIONS)_
- **No quantifying arrears without NRA statement** — NEVER quantify payroll arrears, interest, or fines without an NRA statement -- escalate to a qualified accountant  _(PROHIBITIONS)_
- **Estimated label required** — NEVER present payroll computations as definitive -- always label as estimated and direct to a licensed Bulgarian accountant  _(PROHIBITIONS)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Bulgarian accountant or registered auditor) before implementation.

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
