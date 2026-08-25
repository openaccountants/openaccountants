---
name: belarus-payroll
description: Use this skill whenever asked about Belarus payroll processing for employed persons. Trigger on phrases like "Belarus payroll", "Belarusian salary", "зарплата", "podokhodny nalog", "подоходный налог", "13% income tax Belarus", "PIT Belarus", "tax agent Belarus", "FSZN", "ФСЗН", "Social Protection Fund Belarus", "Фонд социальной защиты населения", "взносы в ФСЗН", "vznosy v FSZN", "28% pension Belarus", "6% social insurance Belarus", "1% employee contribution Belarus", "Belgosstrakh", "Белгосстрах", "accident insurance Belarus", "Form 4-fund", "4-фонд", "PU-3", "ПУ-3", "standard deduction Belarus", "child deduction Belarus", "minimum wage Belarus", "минимальная зарплата", "MZP Belarus", "net salary Belarus", "gross to net Belarus", "PAYE Belarus", "tax withholding Belarus", "employer contributions Belarus", "high-income 25% Belarus", "BYN 220000 threshold", "HTP Belarus", "High-Tech Park payroll", "foreign worker salary Belarus", or any question about computing employee pay, withholding income tax, or mandatory social/accident contributions for Belarus-based employees. This skill covers the flat 13% income tax withholding (employer as tax agent), the FSZN employer 34% (28% pension + 6% social) and employee 1% contributions, compulsory Belgosstrakh accident insurance, the standard/child/category deductions, the high-income 25% annual surtax, minimum wage, foreign-worker salary thresholds, the High-Tech Park base cap, and Form 4-fund / PU-3 filing obligations. ALWAYS read this skill before processing any Belarus payroll.
version: 0.1
jurisdiction: BY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus Payroll

## Belarus Payroll Skill v0.1

**Tier 2 -- research-verified. Figures below are sourced from the Official Internet Portal of the President of the Republic of Belarus (president.gov.by tax-legislation release), the Ministry of Taxes and Duties (MNS / nalog.gov.by), the State Social Protection Fund (FSZN / ssf.gov.by), Belgosstrakh (bgs.by), and cross-checked against established law-firm guides (GSL, Chandrawat & Partners) and specialist Belarusian payroll providers (Spex.by, EOR.by, Recruitment.by, Asanify). NOT yet signed off by a licensed Belarusian accountant (бухгалтер) or auditor. Treat every computation as an estimate pending professional review. All amounts are in Belarusian rubles (BYN / Br).

## Provenance caveat

**Provenance caveat (read before relying on any figure).** PwC Worldwide Tax Summaries no longer maintains a standalone Belarus territory page (URLs 404), and the official ssf.gov.by page timed out on direct fetch, so the FSZN 28%/6% split and the quarterly Form 4-fund / PU-3 reporting were confirmed via secondary Belarusian sources rather than scraped from the authority. Penalty/peni figures are NOT sourced from an authority page and are flagged low-confidence. Standard-deduction amounts (192/56/107/272 BYN) and the minimum wage (726 BYN) are 2025 figures indexed annually -- confirm against the gazetted decree. **Tax-year precision: the 25% surtax over BYN 220,000 is the 2025 rule; the President's release describes a BYN 350,000 threshold and an added 30% band as effective 2026 -- do NOT mix these.**

## Section 1 -- Quick Reference

**Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` -- follow that runbook with this skill supplying the Belarus-specific content.**

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Belarus (Republic of Belarus / Республика Беларусь) |
| Currency | BYN (Belarusian ruble / Br) only |
| Standard pay frequency | At least monthly; in practice advance + final settlement, final by start of the following month (Asanify) |
| Tax year | Calendar year (1 January -- 31 December) |
| Tax withholding system | PAYE-equivalent -- the employer is the **tax agent** and withholds flat 13% PIT at the moment income is paid out, after applying any monthly standard/child/category deductions (EOR.by) |
| Income tax authority | Ministry of Taxes and Duties (MNS / Министерство по налогам и сборам) -- https://www.nalog.gov.by |
| Social security authority | State Social Protection Fund of the Ministry of Labour and Social Protection (FSZN / ФСЗН) -- https://ssf.gov.by |
| Accident-insurance authority | Belgosstrakh (Belarusian Republican Unitary Insurance Enterprise) -- https://www.bgs.by |
| Key legislation | Tax Code of the Republic of Belarus (Налоговый кодекс), Special Part -- esp. arts. 199--214 (individual income tax); Law No. 138-XIII of 31.01.1995 on state social insurance + FSZN decree/law framework (employer 34% / employee 1%); Law on Compulsory Insurance against Industrial Accidents and Occupational Diseases (Belgosstrakh) |
| Filing portal | MNS portal https://www.portal.nalog.gov.by ; FSZN personalised-records system |
| Income tax | **Flat 13%** on most employment income for 2025 (~98% of employees); a 25% surtax applies to ANNUAL income over BYN 220,000 but is assessed on the individual's annual declaration, NOT withheld monthly (president.gov.by; eor.by; reform.news) |
| Validated by | Pending -- requires sign-off by a licensed Belarusian accountant |
| Skill version | 0.1 |

### The single most important Belarus facts

> **1. Income tax is a FLAT 13%, withheld by the employer as tax agent.** It is charged on the PIT base = gross income MINUS the employee's applicable standard/child/category deductions. The employee's 1% FSZN contribution is NOT a deduction from the PIT base (unlike some other CIS systems). (EOR.by; Tax Code arts. 199--214)
>
> **2. The 25% high-income surtax is NOT a monthly payroll item.** For 2025 it applies only to the portion of an individual's ANNUAL income exceeding BYN 220,000, and it is assessed by the tax authority on the basis of the individual's annual declaration filed by 31 March of the following year -- the employer does NOT withhold it monthly. (eor.by; reform.news)
>
> **3. The employer on-cost is dominated by FSZN 34% + Belgosstrakh ~0.6%.** FSZN = 28% pension + 6% social on the full gross salary with no general ceiling for standard employers; Belgosstrakh accident insurance is a standard 0.6% (0.1% for budget organisations; ~0.1%--0.9% by professional-risk class). The employee bears only 13% PIT + 1% FSZN = 14%. (recruiting.by; spex.by; eor.by; bgs.by)

## Section 2 -- Income Tax Withholding (подоходный налог / PIT)

The employer withholds income tax as the **tax agent** at the moment income is paid out. Belarus operates a **single flat rate** for employment income with no marital-status tables.

### Flat Income Tax Rate (2025)

**Flat Income Tax Rate (2025) table**

| Item | Value |
| --- | --- |
| Income tax rate on employment income | **13%** (flat) (president.gov.by; eor.by) |
| Tax base | Gross income **minus** the employee's applicable standard / child / category deductions (the BYN amounts in Section 5) (EOR.by; Tax Code art. 209) |
| High-income surtax (2025) | **25%** on the portion of ANNUAL income over **BYN 220,000** -- assessed via the individual's annual declaration, NOT withheld monthly (eor.by; reform.news) |
| 2026 forward change (do NOT apply to 2025) | Threshold rises to **BYN 350,000** and a **30%** top band is added for ultra-high incomes, effective 2026 (president.gov.by) |
| Dividends | 13% (and 25% on high amounts); 6% if no profit distributed for 3 consecutive years; 0% if none for 5 years (GSL) **[RESEARCH GAP -- 6%/0% special rates from a 2024 GSL snapshot; reviewer to re-verify for 2025]** |

### Withholding computation method

- **PIT computation formula** — PIT_base = gross_income - applicable_deductions   # standard 192 (income-tested) + per-child 56/107 + category 272 PIT      = PIT_base x 13%

There are no FS4-style status categories or cumulative projection. The monthly withholding is mechanically simple:

The 13% is withheld by the employer-as-tax-agent at payout. **The 25% surtax is never part of monthly withholding.** If an employee's annualised income looks set to exceed BYN 220,000, flag it for the annual declaration -- do not increase the monthly withholding.

> **Note on the surtax mechanism.** Because the flat 13% has already been withheld on the full salary, the additional liability assessed on the annual declaration for income over BYN 220,000 is the **incremental** 12% (25% − 13%) on the excess portion -- see Worked Example 4. (eor.by; reform.news)

## Section 3 -- Social, Pension and Accident Contributions -- Tables (2025)

Contributions are computed on the **full gross salary**. For standard (non-HTP, non-budget) employers there is **no general upper ceiling** in 2025; the minimum contribution base is tied to the minimum wage for periods worked. (eor.by)

### 3.1 Standard employer (non-HTP, non-budget) -- the default case

**Standard employer contributions table**

| Contribution (Russian) | Employee | Employer | Total | Source |
| --- | --- | --- | --- | --- |
| FSZN pension / retirement insurance (пенсионное страхование) | 1% | 28% | 29% | eor.by; recruiting.by |
| FSZN social insurance -- sickness, maternity, etc. (социальное страхование) | 0% | 6% | 6% | spex.by; chandrawatpartners.com |
| **FSZN subtotal** | **1%** | **34%** | **35%** | eor.by |
| Belgosstrakh -- accident & occupational-disease insurance (Белгосстрах) | 0% | 0.6% (standard) | 0.6% | spex.by; bgs.by |
| **TOTAL social/accident on-cost** | **1%** | **34.6%** | **35.6%** | (derived) |

**Arithmetic check (component rows sum to the subtotals/total):**
- FSZN employer column: pension 28% + social 6% = **34%** ✓
- FSZN employee column: 1% + 0% = **1%** ✓
- FSZN total: 34% + 1% = **35%** ✓
- Belgosstrakh employer column: **0.6%** (standard) ✓
- Employer grand total: 34% + 0.6% = **34.6%** ✓
- Combined (EE + ER): 1% + 34.6% = **35.6%** ✓

> The 1% employee FSZN is the **only** payroll contribution withheld from the employee; the employer's 34% FSZN and Belgosstrakh are paid on top of gross. The employee's total deduction from gross is therefore **13% PIT + 1% FSZN = 14%** before any PIT deductions are applied.

### 3.2 Belgosstrakh accident-insurance rate (employer-only)

**Belgosstrakh rate table**

| Policyholder type | Rate on gross payroll | Source |
| --- | --- | --- |
| Standard / most policyholders | **0.6%** | spex.by; eor.by |
| Budget / state organisations | **0.1%** | spex.by; eor.by |
| Effective range by professional-risk class (discounts/surcharges) | **~0.1% -- 0.9%** | bgs.by |

Use 0.6% as the default for a standard private employer; use the policyholder's actual risk-class rate when known.

### 3.3 Contribution base -- floor and ceiling (2025)

**Contribution base table**

| Threshold | Value | Source |
| --- | --- | --- |
| General upper ceiling (standard employer) | **None** in 2025 -- FSZN on full gross | eor.by |
| Minimum contribution base | Tied to the **minimum wage** (BYN 726/month in 2025) for periods worked | eor.by |
| HTP-resident special base | FSZN may be computed on the **national average monthly wage** (Belstat) instead of full salary, capping high earners | recruitment.by |

> **HTP cap is a RESEARCH GAP for the exact figure.** The Belstat national average monthly wage used as the HTP cap is not supplied in the research data. **[RESEARCH GAP -- reviewer to confirm the current Belstat national average monthly wage used as the HTP FSZN base.]**

### 3.4 Other regimes (reference only -- NOT employer payroll)

**Other regimes table**

| Regime | Rate | Base | Source |
| --- | --- | --- | --- |
| Self-employed / individual entrepreneurs (self-pay) | **35%** = 29% pension + 6% social | self-declared income, min tied to minimum wage | chandrawatpartners.com; spex.by |
| HTP residents (employer/employee) | same **34% / 1%** rates | FSZN base may be the Belstat national average wage | recruitment.by |

## Section 4 -- Conservative Defaults

When an input is ambiguous, apply the conservative default below and flag it for the reviewer.

**Conservative Defaults table**

| Ambiguity | Conservative default | Rationale |
| --- | --- | --- |
| Belgosstrakh risk-class rate unknown | Use the standard **0.6%** -> employer on-cost 34.6% | The 0.1% rate is budget-org only; the ~0.1%--0.9% band is risk-class dependent (bgs.by) |
| Standard BYN 192 deduction -- eligibility unclear | Do **NOT** apply it unless monthly income ≤ BYN 1,164 is confirmed | The deduction is only available below the BYN 1,164 monthly ceiling, and most employees earn above it (eor.by) |
| Employer total on-cost (quick estimate) | **~34.6% of gross** (34% FSZN + 0.6% Belgosstrakh) for a standard non-HTP, non-budget employer | Use the 0.6% standard rate unless the risk class is known |
| Employee deduction from gross (quick estimate) | **14% of gross** (13% PIT + 1% FSZN) before any standard/child deductions | Most employees earn above BYN 1,164/month so the BYN 192 standard deduction often does not apply |
| High-income 25% surtax | Do **NOT** apply in monthly withholding; flag for annual declaration if annual income > BYN 220,000 | It is assessed by the tax authority on the annual return, not withheld by the employer (eor.by) |
| HTP-resident FSZN base unknown | Default to FSZN on **full gross** (standard treatment) and flag the HTP cap for the reviewer | The Belstat average-wage cap requires the exact figure, which is a RESEARCH GAP |
| 2026 vs 2025 threshold | Use the **BYN 220,000 / 25%** 2025 rule for 2025 runs; flag the BYN 350,000 / 30% rule as a 2026-only forward change | The President's release dates the new band to 2026 (president.gov.by) |

## Section 5 -- Required Inputs and Refusal Catalogue

### Required inputs

**Minimum viable** -- gross monthly remuneration and confirmation that the worker is an employee (not a self-employed individual entrepreneur). Without a gross figure, STOP.

**Recommended** -- the employer's Belgosstrakh professional-risk class (to fix the 0.1%--0.9% rate), whether the employer is a High-Tech Park resident, the number of qualifying children/dependents (for the BYN 56/107 deductions), and whether monthly income is below BYN 1,164 (for the BYN 192 standard deduction).

**Ideal** -- payslip showing the FSZN and PIT split, MNS confirmation of withheld PIT remitted, the latest Form 4-fund (4-фонд) and PU-3 (ПУ-3) personalised records, the employee's residency status, and -- for high earners -- the annualised income projection against the BYN 220,000 threshold.

### Refusal catalogue

- **R-BY-PAY-1** — Trigger: no gross monthly remuneration provided. Message: "A gross monthly remuneration is mandatory. PIT (13%) is charged on gross minus applicable deductions, and FSZN/Belgosstrakh are percentages of gross. Cannot proceed without the gross figure."
- **R-BY-PAY-2** — Trigger: client has unpaid contributions or withheld PIT from prior periods and wants the arrears + interest quantified. Message: "Overdue taxes/contributions accrue penalty interest (peni) based on the National Bank refinancing rate, plus administrative fines for late/incorrect filing. The exact 2025 peni formula is NOT confirmed from an authority page [RESEARCH GAP]. Escalate to a Belarus-qualified accountant -- do not estimate arrears."
- **R-BY-PAY-3** — Trigger: client wants the exact 25% surtax computed and remitted through payroll. Message: "The 25% surtax on annual income over BYN 220,000 is NOT withheld monthly by the employer -- it is assessed by the tax authority on the individual's annual declaration filed by 31 March of the following year. Flag the exposure; do not add it to monthly withholding."
- **R-BY-PAY-4** — Trigger: employee works across EAEU states, is a non-resident, or splits duties internationally. Message: "Cross-border and EAEU social-security/PIT coordination and non-resident rates are outside the scope of this skill. Escalate to a Belarus-qualified accountant."
- **R-BY-PAY-5** — Trigger: the worker is a self-employed individual entrepreneur (ИП), not an employee. Message: "This skill covers EMPLOYED persons (employer is the tax agent and withholds PIT + the 1% FSZN, and pays 34% FSZN on top). Self-employed/individual-entrepreneur FSZN is self-paid at 35% (29% pension + 6% social) on declared income and is out of scope. Escalate to a Belarus-qualified accountant."
- **R-BY-PAY-6** — Trigger: hiring a foreign national from 1 Nov 2025. Message: "From 1 November 2025 foreign employees must earn at least BYN 3,630/month (= 5x minimum wage) under a special work permit / temporary residence permit, or BYN 2,100/month for other categories, and must be on local BYN payroll (Nairametrics, citing Fragomen). Confirm the category and threshold with an immigration adviser before running payroll."

## Section 6 -- Payment Pattern Library

Deterministic pre-classifier for Belarusian bank-statement lines related to payroll. Match by case-insensitive substring on the counterparty/reference as it appears in the statement. References may be Cyrillic or transliterated Latin.

### 6.1 Employer debits -- remittances to MNS / FSZN / Belgosstrakh

**Employer debits remittances table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ПОДОХОДНЫЙ НАЛОГ, PODOKHODNY, PIT, ИФНС, МНС, MNS | 13% PIT withheld and remitted to the budget | Tag separately from contributions |
| ФСЗН, FSZN, ФОНД СОЦ ЗАЩИТЫ, СОЦСТРАХ | FSZN contribution remittance (employer 34% + employee 1%) | Pension + social bundled |
| ПЕНСИОННЫЕ ВЗНОСЫ, PENSION CONTRIB | FSZN pension (retirement) portion | Part of the 28%/1% pension split |
| БЕЛГОССТРАХ, BELGOSSTRAKH, СТРАХ ОТ НЕСЧ СЛУЧ | Belgosstrakh accident/occupational-disease insurance | Employer-only, ~0.6% |

### 6.2 Employer debits -- net wages to employees

**Employer debits net wages table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ЗАРПЛАТА, ZARPLATA, SALARY, ОПЛАТА ТРУДА, WAGES | Net salary disbursement (payroll expense) | Net of withheld PIT + 1% FSZN |
| АВАНС, AVANS, ADVANCE | Salary advance (part of net wage) | Reconcile against the month's net pay; final settlement follows |
| ОКОНЧАТЕЛЬНЫЙ РАСЧЕТ, FINAL SETTLEMENT | Final salary settlement | Typically by start of the following month |

### 6.3 Employee credits -- pay received

**Employee credits table**

| Pattern | Classification | Notes |
| --- | --- | --- |
| ЗАРПЛАТА, SALARY (incoming) | Net employment income received | Already net of PIT + 1% FSZN |
| ПЕНСИЯ, PENSIA, PENSION (incoming) | FSZN pension benefit | NOT employment income; not a payroll item |
| ПОСОБИЕ, POSOBIE, BENEFIT (incoming) | FSZN sickness/maternity benefit | NOT employment income |

### 6.4 Bank-specific debit descriptions

**Bank-specific debit descriptions table**

| Bank | Typical debit description | Classification |
| --- | --- | --- |
| Belarusbank (Беларусбанк) | "ФСЗН ВЗНОСЫ" / "FSZN" | FSZN contribution remittance |
| Belagroprombank | "ПОДОХОДНЫЙ НАЛОГ" / "MNS" | 13% PIT remittance |
| Priorbank | "БЕЛГОССТРАХ" | Accident insurance |
| Belinvestbank | "ЗАРПЛАТА" / "SALARY" | Net wage disbursement |

## Section 7 -- Worked Examples

Realistic Minsk-based payroll scenarios for a hypothetical standard (non-HTP, non-budget) employer at the standard 0.6% Belgosstrakh class, unless stated. Currency is BYN. Every figure below is recomputed end-to-end. Unless stated, the employee earns above BYN 1,164/month, so the BYN 192 standard deduction does NOT apply and no children are claimed.

### Example 1 -- Standard salary above the deduction ceiling (gross BYN 2,000)

**Input line:**
`25.05.2025 ; ФСЗН ВЗНОСЫ 04/2025 ; DEBIT ; ФСЗН + ПОДОХОДНЫЙ ; -960.00 ; BYN`

**Reasoning:**
Gross BYN 2,000 exceeds BYN 1,164, so no standard deduction; no children. PIT base = full gross.
- PIT = 13% × 2,000 = **BYN 260.00**
- Employee FSZN = 1% × 2,000 = **BYN 20.00**
- **Net pay** = 2,000 − 260.00 − 20.00 = **BYN 1,720.00**
- Employer FSZN = 34% × 2,000 = **BYN 680.00**
- Belgosstrakh = 0.6% × 2,000 = **BYN 12.00**
- Employer on-cost = 680.00 + 12.00 = **BYN 692.00**; total cost to employer = 2,000 + 692.00 = **BYN 2,692.00**

The combined remittance shown on the bank line above is employee FSZN 20.00 + PIT 260.00 + employer FSZN 680.00 = **BYN 960.00** to MNS/FSZN; Belgosstrakh 12.00 is paid separately on the Belgosstrakh schedule.

**Classification:** Net wage BYN 1,720.00 to employee; FSZN + PIT BYN 960.00 by the 22nd of the following month; employer-share FSZN BYN 680.00 and Belgosstrakh BYN 12.00 are deductible payroll on-costs.

### Example 2 -- Minimum-wage employee, standard deduction applies (gross BYN 726)

**Input line:**
`25.06.2025 ; ЗАРПЛАТА МАЙ 2025 ; DEBIT ; МИН ЗП ; -649.32 ; BYN`

**Reasoning:**
Gross BYN 726 (the 2025 statutory minimum wage) is below BYN 1,164, so the BYN 192 standard deduction applies; no children.
- PIT base = 726 − 192 = BYN 534.00; PIT = 13% × 534.00 = **BYN 69.42**
- Employee FSZN = 1% × 726 = **BYN 7.26**
- **Net pay** = 726 − 69.42 − 7.26 = **BYN 649.32**
- Employer FSZN = 34% × 726 = **BYN 246.84**
- Belgosstrakh = 0.6% × 726 = **BYN 4.36** (726 × 0.006 = 4.356, rounded)

**Classification:** Net wage BYN 649.32. The standard deduction reduces PIT only because income is under the BYN 1,164 ceiling; if income rises above it in any month the BYN 192 falls away.

### Example 3 -- Low-paid parent with one child (gross BYN 1,000, 1 child)

**Input line:**
`25.07.2025 ; ЗАРПЛАТА ИЮНЬ 2025 ; DEBIT ; ЗП + ДЕТСКИЙ ВЫЧЕТ ; -892.24 ; BYN`

**Reasoning:**
Gross BYN 1,000 is below BYN 1,164, so the BYN 192 standard deduction applies; plus one child under 18 at BYN 56.
- Deductions = 192 + 56 = BYN 248.00
- PIT base = 1,000 − 248.00 = BYN 752.00; PIT = 13% × 752.00 = **BYN 97.76**
- Employee FSZN = 1% × 1,000 = **BYN 10.00**
- **Net pay** = 1,000 − 97.76 − 10.00 = **BYN 892.24**
- Employer FSZN = 34% × 1,000 = **BYN 340.00**; Belgosstrakh = 0.6% × 1,000 = **BYN 6.00**

**Classification:** Net wage BYN 892.24. Child deduction stacks on the standard deduction. A parent of 2+ children, a single parent, or a guardian would use the enhanced BYN 107 per child instead of BYN 56.

### Example 4 -- High earner triggering the annual 25% surtax (gross BYN 20,000/month)

**Input line:**
`25.05.2025 ; ФСЗН + ПОДОХОДНЫЙ 04/2025 ; DEBIT ; ВЫСОКАЯ ЗП ; -9,600.00 ; BYN`

**Reasoning -- monthly withholding only:**
Gross BYN 20,000/month, annualised BYN 240,000 (> BYN 220,000). The employer withholds ONLY the flat 13% monthly; there is no FSZN ceiling for a standard employer.
- PIT withheld = 13% × 20,000 = **BYN 2,600.00**
- Employee FSZN = 1% × 20,000 = **BYN 200.00**
- **Net pay (monthly, before surtax)** = 20,000 − 2,600.00 − 200.00 = **BYN 17,200.00**
- Employer FSZN = 34% × 20,000 = **BYN 6,800.00**; Belgosstrakh = 0.6% × 20,000 = **BYN 120.00**
- Combined monthly MNS/FSZN remittance = 200.00 + 2,600.00 + 6,800.00 = **BYN 9,600.00**.

**Reasoning -- annual surtax (NOT a payroll item):**
Annual income BYN 240,000; excess over BYN 220,000 = BYN 20,000. The 25% rate applies to that excess. Because the flat 13% was already withheld on the whole salary, the **incremental** liability assessed on the individual's annual declaration is (25% − 13%) × 20,000 = 12% × 20,000 = **BYN 2,400.00**, due via the declaration filed by 31 March of the following year. (eor.by; reform.news)

**Classification:** Run monthly payroll at the flat 13% only. Flag the high earner for the annual declaration; do NOT add the BYN 2,400.00 to monthly withholding. (For 2026 onward the threshold becomes BYN 350,000 with a 30% top band -- do not apply to 2025.)

### Example 5 -- High-Tech Park (HTP) resident, FSZN base capped (gross BYN 10,000)

**Input line:**
`25.06.2025 ; ФСЗН ПВТ 05/2025 ; DEBIT ; HTP CAPPED BASE ; -1,300.00 ; BYN`

**Reasoning:**
HTP residents apply the same 13% PIT and the same 34%/1% FSZN rates, but FSZN may be computed on the **national average monthly wage** (Belstat) rather than the full BYN 10,000 salary. (recruitment.by)
- PIT (no cap) = 13% × 10,000 = **BYN 1,300.00** (the bank line above shows PIT; FSZN is on the capped base)
- Employee FSZN = 1% × [Belstat national average wage] -- **[RESEARCH GAP -- the Belstat average-wage cap figure is not in the research data; reviewer to supply]**
- Employer FSZN = 34% × [Belstat national average wage] -- **[RESEARCH GAP]**
- Belgosstrakh = 0.6% × 10,000 = **BYN 60.00** (Belgosstrakh follows full gross unless told otherwise -- flag for reviewer)

**Classification:** PIT is unaffected by HTP status; only the FSZN base is capped at the national average wage for the salary above it. The cap figure must be confirmed before the FSZN amounts can be finalised.

### Example 6 -- Budget organisation, reduced Belgosstrakh rate (gross BYN 2,000, 0.1% class)

**Input line:**
`25.05.2025 ; БЕЛГОССТРАХ БЮДЖ 04/2025 ; DEBIT ; СТРАХ 0.1% ; -2.00 ; BYN`

**Reasoning:**
Same employee as Example 1 (gross BYN 2,000) but a budget/state organisation, so Belgosstrakh is 0.1% instead of 0.6%.
- PIT = **BYN 260.00** (unchanged); Employee FSZN = **BYN 20.00** (unchanged); Net pay = **BYN 1,720.00** (unchanged)
- Employer FSZN = 34% × 2,000 = **BYN 680.00** (unchanged)
- Belgosstrakh = 0.1% × 2,000 = **BYN 2.00** (vs BYN 12.00 at 0.6%)
- Employer on-cost = 680.00 + 2.00 = **BYN 682.00**

**Classification:** Only the Belgosstrakh on-cost changes; the employee net pay is identical to Example 1. Use 0.1% ONLY for budget/state organisations.

## Section 8 -- Tier 1 Rules (deterministic)

Apply exactly as written when inputs are clear.

### Rule 1 -- Income tax is a flat 13% on the deduction-adjusted base

- **Flat 13% PIT rule** — PIT_base = gross_income - applicable_deductions   # standard 192 (income-tested) + per-child 56/107 + category 272 PIT      = PIT_base x 13% No brackets, no marital-status tables. The employer withholds at payout as the tax agent.  _(president.gov.by; eor.by)_

### Rule 2 -- FSZN contribution formula (standard employer)

- **FSZN contribution formula** — fszn_base            = gross_income            # no general ceiling for standard employers in 2025 employee_fszn        = fszn_base x 1% employer_fszn        = fszn_base x 34%          # 28% pension + 6% social belgosstrakh         = gross_income x 0.6%      # standard; 0.1% budget org; 0.1%–0.9% by risk class employer_on_cost     = employer_fszn + belgosstrakh   # = 34.6% at the 0.6% rate  _(eor.by; recruiting.by; spex.by; bgs.by)_

### Rule 3 -- The employee bears only 14% of gross

- **Employee total deduction** — The employee's total deduction from gross is 13% PIT + 1% FSZN = 14% (before any PIT deductions). Everything else is employer on-cost.  _(eor.by)_

### Rule 4 -- Standard deduction is income-tested

- **Standard deduction eligibility** — The BYN 192/month standard deduction applies ONLY if monthly income ≤ BYN 1,164. Above that, it falls away. Child deductions (BYN 56, or enhanced BYN 107) and the BYN 272 category deduction are not subject to the BYN 1,164 standard-deduction ceiling but have their own eligibility rules.  _(eor.by; Tax Code art. 209)_

### Rule 5 -- The 25% surtax is annual, not monthly

- **Annual surtax rule** — For 2025, income over BYN 220,000/year bears 25% on the excess, assessed on the individual's annual declaration filed by 31 March of the following year. The employer NEVER withholds it monthly; the incremental liability after the flat 13% is (25% − 13%) × excess.  _(eor.by; reform.news)_

### Rule 6 -- Belgosstrakh is employer-only

- **Belgosstrakh employer-only rule** — Compulsory accident/occupational-disease insurance (standard 0.6%; 0.1% budget org; ~0.1%--0.9% by risk class) is paid ENTIRELY by the employer and is never withheld from the employee.  _(spex.by; bgs.by)_

### Rule 7 -- Monthly remittance and deadline

- **Remittance deadline rule** — Withheld PIT and FSZN/Belgosstrakh contributions are due monthly, generally by the 22nd of the month following salary payment; monthly tax reports by the 20th of the following month. The Tax Code rule is that the tax agent transfers withheld PIT no later than the day of payout from the bank (or next day), with the 22nd as a backstop. [RESEARCH GAP -- confirm the exact PIT remittance timing against Tax Code art. 216]  _(asanify.com; by.icalculator.com)_

### Rule 8 -- Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Income tax (PIT) remittance | Employer (tax agent) transfers withheld 13% PIT to the budget | At payout; not later than the 22nd of the following month where withholding is deferred | asanify.com; by.icalculator.com |
| FSZN Form 4-fund (4-фонд) + PU-3 (ПУ-3) personalised records | Quarterly report to the FSZN on accrued/paid contributions and personalised employee data | Contributions paid monthly by the 22nd (or by payday); quarterly 4-fund report generally by the 20th of the month after the quarter | ssf.gov.by; asanify.com |
| Annual individual income declaration (high earners) | Individual declares income over BYN 220,000 and pays the 25% surtax on the excess | 31 March of the year following the reporting year | eor.by |
| Employer annual income/withholding report to MNS | Report of employee income and tax withheld | By March of the following year (annual reconciliation) | rivermate.com; asanify.com |
| Belgosstrakh accident-insurance reporting | Mandatory occupational accident/disease premiums and reporting; employer registers with Belgosstrakh | Per Belgosstrakh schedule (monthly/quarterly) | bgs.by |

### Rule 9 -- Minimum wage and minimum contribution base

- **Minimum wage rule** — The 2025 statutory minimum wage is BYN 726/month (was BYN 626 in 2024; rises to BYN 858 in 2026); hourly equivalent ≈ BYN 4.54. The minimum FSZN contribution base is tied to the minimum wage for periods worked.  _(wageindicator.org; belarusvc.com; eor.by)_

### Rule 10 -- Employer registration / foreign workers

- **Employer registration rule** — Employers must register with the MNS, the FSZN, and Belgosstrakh before hiring. From 1 November 2025, foreign employees must earn at least BYN 3,630/month (= 5x minimum wage) under a special work permit / temporary residence permit, or BYN 2,100/month for other categories, and be on local BYN payroll.  _(asanify.com; nairametrics.com)_

## Section 9 -- Tier 2 Catalogue (reviewer judgement)

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Belgosstrakh risk class unknown

*Trigger:* employer's professional-risk class / economic activity not provided. *Issue:* the rate ranges ~0.1%--0.9% (standard 0.6%, budget 0.1%). *Action:* default to 0.6% for a standard private employer; flag for the reviewer to confirm the gazetted risk-class rate. (bgs.by)

### T2-2 -- High earner near/over the BYN 220,000 annual threshold

*Trigger:* annualised income approaches or exceeds BYN 220,000. *Issue:* the 25% surtax on the excess is due via the annual declaration, not monthly withholding. *Action:* run monthly payroll at flat 13% only; flag the annual-declaration exposure (incremental 12% on the excess). (eor.by; reform.news)

### T2-3 -- HTP-resident FSZN base cap

*Trigger:* employer is a High-Tech Park resident. *Issue:* FSZN may be computed on the Belstat national average wage rather than full salary, capping high earners. *Action:* flag for reviewer; obtain the current Belstat average-wage figure. [RESEARCH GAP -- Belstat national average monthly wage not in research data]

### T2-4 -- Standard-deduction eligibility borderline

*Trigger:* monthly income near the BYN 1,164 ceiling. *Issue:* the BYN 192 standard deduction is available only at/below the ceiling, and a small raise can remove it. *Action:* confirm the exact monthly income before applying the deduction. (eor.by)

### T2-5 -- Dividend / mixed-income recipients

*Trigger:* the individual also receives dividends. *Issue:* dividends bear 13% (and 25% on high amounts), with special 6%/0% rates for retained-profit conditions, on a 2024 snapshot. *Action:* flag for reviewer; route dividend taxation outside payroll. [RESEARCH GAP -- 6%/0% dividend rates from a 2024 GSL snapshot; re-verify for 2025/2026]

### T2-6 -- Payroll arrears, peni and fines

*Trigger:* unpaid contributions or withheld PIT from prior periods. *Issue:* penalty interest (peni) accrues on overdue amounts based on the National Bank refinancing rate, plus administrative fines. *Action:* do not quantify without an MNS/FSZN statement; escalate to a qualified accountant. [RESEARCH GAP -- exact 2025 peni formula not confirmed from an authority page]

### T2-7 -- 2026 forward changes

*Trigger:* computation for 2026. *Issue:* the high-income threshold rises to BYN 350,000 with an added 30% top band, the minimum wage rises to BYN 858, and deduction/threshold figures are indexed annually. *Action:* do NOT apply the 2026 figures to 2025 payroll; flag and confirm the gazetted 2026 decrees. (president.gov.by; belarusvc.com)

## Section 10 -- Excel Working Paper Template

BELARUS PAYROLL -- WORKING PAPER
Client / Employer: [name]            HTP resident: [YES/NO]   Budget org: [YES/NO]
Tax Year: [2025]    Currency: BYN
Prepared: [date]

INPUT DATA
  Employee name:                 [____]
  Gross monthly remuneration:    [____]
  Monthly income <= BYN 1,164:   [YES/NO]   (governs the BYN 192 standard deduction)
  Children under 18 / dependents:[____]      Enhanced (2+ / single parent / guardian): [YES/NO]
  Category deduction (BYN 272):  [YES/NO]
  Belgosstrakh risk-class rate:  [0.6% standard / 0.1% budget / 0.1%–0.9%]
  Annualised income > BYN 220,000: [YES/NO]  (annual-declaration surtax flag only)

PIT DEDUCTIONS (monthly)
  Standard (BYN 192, only if income <= BYN 1,164): [____]
  Per child (BYN 56) x [n]:                        [____]
  Enhanced per child (BYN 107) x [n]:              [____]
  Category (BYN 272):                              [____]
  Total deductions:                                [____]

INCOME TAX (flat 13%)
  PIT base (gross - deductions):                   [____]
  PIT (13%):                                       [____]

CONTRIBUTIONS
  FSZN base (full gross; HTP = Belstat avg wage):  [____]
  Employee FSZN (1%):                EE [____]
  Employer FSZN (34% = 28% + 6%):              ER [____]
  Belgosstrakh (0.6% / 0.1% / risk):           ER [____]
  Employee total (13% PIT + 1% FSZN):EE [____]
  Employer on-cost (34% + Belgosstrakh):       ER [____]

NET PAY
  Gross - PIT - employee FSZN:                     [____]

REMITTANCE
  PIT + FSZN to MNS/FSZN (by 22nd of following month): [____]
  Belgosstrakh (per schedule):                         [____]
  Form 4-fund + PU-3 (quarterly, by 20th after qtr):   [filed Y/N]
  High-earner annual declaration flagged (>220,000):   [YES/NO]

REVIEWER FLAGS
  [List any Tier 2 flags and RESEARCH GAP markers here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]

## Section 11 -- Bank Statement / Terminology Reading Guide

References commonly appear in Cyrillic; some banks transliterate to Latin. All amounts are in BYN.

**Belarusian/Russian term glossary**

| Belarusian/Russian term | Transliteration | Meaning |
| --- | --- | --- |
| Зарплата / Оплата труда | Zarplata / Oplata truda | Salary / wage |
| Подоходный налог | Podokhodny nalog | Personal income tax (flat 13%) |
| ФСЗН (Фонд социальной защиты населения) | FSZN | State Social Protection Fund |
| Пенсионное страхование | Pensionnoe strakhovanie | Pension (retirement) insurance (28% ER / 1% EE) |
| Социальное страхование | Sotsialnoe strakhovanie | Social insurance -- sickness/maternity (6% ER) |
| Белгосстрах | Belgosstrakh | Accident/occupational-disease insurance (employer-only) |
| Минимальная заработная плата (МЗП) | Minimalnaya zarabotnaya plata (MZP) | Minimum wage |
| Стандартный вычет | Standartny vychet | Standard PIT deduction (BYN 192) |
| Детский вычет | Detskiy vychet | Child deduction (BYN 56 / enhanced 107) |
| Аванс | Avans | Salary advance |
| Окончательный расчёт | Okonchatelny raschyot | Final settlement |
| Форма 4-фонд / ПУ-3 | Forma 4-fund / PU-3 | FSZN quarterly report / personalised records |
| Пеня | Penya (peni) | Penalty interest on overdue tax/contributions |

**Identification tips:**
1. PIT and FSZN debits are outgoing (DEBIT) to MNS/FSZN and recur monthly around the 22nd.
2. A single MNS/FSZN debit may bundle employee FSZN + employer FSZN + the 13% PIT -- split by reference (ФСЗН = contributions; ПОДОХОДНЫЙ = income tax).
3. Belgosstrakh is a separate, much smaller debit (~0.6% of payroll) on its own schedule.
4. Net wage to the employee (ЗАРПЛАТА outgoing) is separate from the MNS/FSZN remittance and is net of the 14% employee burden (after deductions).
5. Do not confuse outgoing contribution debits with incoming FSZN benefit credits (ПЕНСИЯ pension, ПОСОБИЕ benefit).
6. The 25% surtax never appears in monthly payroll -- it is settled via the individual's annual declaration.

## Section 12 -- Onboarding Fallback

If the client provides only a bank statement and no other information:

1. **Scan for MNS/FSZN debits** -- identify all outgoing payments matching Section 6 patterns (ФСЗН / ПОДОХОДНЫЙ / БЕЛГОССТРАХ).
2. **Separate PIT from contributions** -- tag ФСЗН/ПЕНСИОННЫЕ as FSZN contributions; tag ПОДОХОДНЫЙ as the 13% PIT; tag БЕЛГОССТРАХ as accident insurance.
3. **Reverse-engineer the base** -- for an employer FSZN remittance, divide the FSZN amount by the combined 35% (employer 34% + employee 1%) to estimate gross payroll; cross-check against the 13% PIT and the ~0.6% Belgosstrakh.
4. **Match the net wage** -- a ЗАРПЛАТА outgoing equals gross minus the 13% PIT (on the deduction-adjusted base) minus 1% employee FSZN.
5. **Flag for reviewer:** "Payroll figures derived from bank-statement amounts only. Employment status, Belgosstrakh risk class, HTP status, deduction eligibility, and any high-income annual-declaration exposure have not been independently verified. Reviewer must confirm before filing Form 4-fund / PU-3."

## Section 13 -- Reference Material

### Calculation summary (2025, BYN; standard employer; 0.6% Belgosstrakh; no children unless noted)

**Calculation summary table**  _(eor.by / recruiting.by / spex.by / bgs.by)_

| Gross monthly | Deductions | PIT base | PIT (13%) | Employee FSZN (1%) | Net pay | Employer FSZN (34%) | Belgosstrakh (0.6%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BYN 726 (min wage) | BYN 192 (standard) | BYN 534.00 | BYN 69.42 | BYN 7.26 | BYN 649.32 | BYN 246.84 | BYN 4.36 |
| BYN 1,000 (1 child) | BYN 248 (192 + 56) | BYN 752.00 | BYN 97.76 | BYN 10.00 | BYN 892.24 | BYN 340.00 | BYN 6.00 |
| BYN 2,000 | none | BYN 2,000.00 | BYN 260.00 | BYN 20.00 | BYN 1,720.00 | BYN 680.00 | BYN 12.00 |
| BYN 20,000 | none | BYN 20,000.00 | BYN 2,600.00 | BYN 200.00 | BYN 17,200.00 | BYN 6,800.00 | BYN 120.00 |

*All sourced to the rates in Section 3 (eor.by / recruiting.by / spex.by / bgs.by). The BYN 20,000 row's annual income (240,000) triggers a separate 25% surtax on the BYN 20,000 excess over 220,000, settled via the annual declaration -- incremental 12% = BYN 2,400.00 (eor.by; reform.news).*

### Thresholds (with provenance)

**Thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| Income tax rate (employment income) | 13% flat | president.gov.by; eor.by |
| High-income surtax (2025) | 25% on annual income over BYN 220,000 (annual declaration) | eor.by; reform.news |
| 2026 forward change (NOT 2025) | threshold BYN 350,000 + 30% top band | president.gov.by |
| Standard monthly deduction | BYN 192/month, only if monthly income ≤ BYN 1,164 | eor.by; Tax Code art. 209 |
| Per-child / dependent deduction | BYN 56/month | eor.by |
| Enhanced child deduction | BYN 107/month per child (2+ children, single parents, disabled children, widow(er)s, guardians/foster carers) | eor.by |
| Category deduction (specified disabled/vulnerable) | BYN 272/month | eor.by |
| Standard-deduction income ceiling | BYN 1,164/month | eor.by |
| Minimum wage (MZP) 2025 | BYN 726/month (was BYN 626 in 2024; BYN 858 in 2026); hourly ≈ BYN 4.54 | wageindicator.org; belarusvc.com |
| FSZN employer rate | 34% (28% pension + 6% social) on full gross | recruiting.by; spex.by; eor.by |
| FSZN employee rate | 1% on full gross | eor.by; chandrawatpartners.com |
| FSZN general ceiling (standard employer, 2025) | None; minimum base tied to minimum wage | eor.by |
| Belgosstrakh accident insurance | 0.6% standard; 0.1% budget org; ~0.1%--0.9% by risk class | spex.by; eor.by; bgs.by |
| Foreign-worker minimum salary (from 1 Nov 2025) | BYN 3,630/month (= 5x min wage) special permit; BYN 2,100/month other categories | nairametrics.com |
| Self-employed / IE FSZN (reference) | 35% (29% pension + 6% social) self-paid | chandrawatpartners.com; spex.by |

### Penalties

**Penalties table**

| Penalty | Detail | Source |
| --- | --- | --- |
| Late payment of taxes/contributions | Penalty interest (peni) on overdue amounts based on the National Bank refinancing rate; administrative fines for late/incorrect filing | GSL **[RESEARCH GAP -- exact 2025 peni formula not confirmed from an authority page; low confidence]** |
| Failure to withhold/remit PIT as tax agent | Administrative liability and recovery of unwithheld amounts plus peni | eor.by **[RESEARCH GAP -- figure not confirmed; low confidence]** |

### Authorities

- **MNS / Министерство по налогам и сборам** (https://www.nalog.gov.by) -- income tax; employer is the tax agent.
- **FSZN / ФСЗН** (https://ssf.gov.by) -- pension and social-insurance contributions; Form 4-fund / PU-3.
- **Belgosstrakh** (https://www.bgs.by) -- compulsory accident/occupational-disease insurance.

### Wider entity context (informational, not payroll)

Corporate income tax is 20% standard (25% where annual profit exceeds BYN 25,000,000) and VAT is 20% standard (10%/0% reduced). (GSL) **[RESEARCH GAP -- BYN 25m corporate 25% band and dividend special rates from a 2024 GSL snapshot; re-verify for 2025/2026]**

### Test suite

**Test 1:** Employee, gross BYN 726 (min wage), no children, income ≤ 1,164 so BYN 192 standard deduction applies. -> PIT base = 534.00; PIT = BYN 69.42; employee FSZN = BYN 7.26; net = BYN 649.32; employer FSZN = BYN 246.84; Belgosstrakh 0.6% = BYN 4.36.

**Test 2:** Employee, gross BYN 1,000, one child, income ≤ 1,164 (deductions 192 + 56 = 248). -> PIT base = 752.00; PIT = BYN 97.76; employee FSZN = BYN 10.00; net = BYN 892.24; employer FSZN = BYN 340.00; Belgosstrakh = BYN 6.00.

**Test 3:** Employee, gross BYN 2,000, no deductions (above the 1,164 ceiling). -> PIT base = 2,000.00; PIT = BYN 260.00; employee FSZN = BYN 20.00; net = BYN 1,720.00; employer FSZN = BYN 680.00; Belgosstrakh = BYN 12.00. Employer total cost = BYN 2,692.00.

**Test 4:** High earner, gross BYN 20,000/month (annual 240,000). -> Monthly: PIT 13% = BYN 2,600.00; employee FSZN = BYN 200.00; net = BYN 17,200.00; employer FSZN = BYN 6,800.00; Belgosstrakh = BYN 120.00. Annual surtax (NOT monthly): excess 20,000 over 220,000; incremental 12% = BYN 2,400.00 via the 31 March annual declaration.

**Test 5:** Same as Test 3 but a budget organisation (Belgosstrakh 0.1%). -> Employee figures unchanged (net BYN 1,720.00); Belgosstrakh = 0.1% × 2,000 = BYN 2.00; employer on-cost = 680.00 + 2.00 = BYN 682.00.

**Test 6:** HTP resident, gross BYN 10,000. -> PIT (uncapped) = 13% × 10,000 = BYN 1,300.00; FSZN base capped at the Belstat national average wage (figure not supplied). Flag for reviewer. **[RESEARCH GAP -- Belstat average-wage cap.]**

**Test 7:** Foreign hire from 1 Nov 2025 on a special work permit. -> Must earn ≥ BYN 3,630/month (5x min wage) and be on local BYN payroll; otherwise out of compliance (refusal R-BY-PAY-6). Standard 13% PIT + FSZN apply once on payroll.

**Test 8:** Worker is a self-employed individual entrepreneur, not an employee. -> Out of scope; self-pays FSZN at 35% (29% pension + 6% social) on declared income; route per refusal R-BY-PAY-5.

- **R-BY-PAY-6** — Foreign hire on special work permit not earning ≥ BYN 3,630/month (5x min wage) or not on local BYN payroll is out of compliance  _(Test 7, Section 13)_
- **R-BY-PAY-5** — Self-employed individual entrepreneur is out of scope of employee payroll; self-pays FSZN at 35% on declared income  _(Test 8, Section 13)_

## Section 14 -- Interaction with Other Skills

**Interaction with other skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (13% PIT + FSZN + Belgosstrakh) | **This skill (belarus-payroll.md)** |
| Belarus VAT (NDS) returns | belarus-vat.md |
| Self-employed / individual-entrepreneur contributions | (out of scope -- escalate to a qualified accountant) |
| High-income annual income declaration (> BYN 220,000) | (individual annual return -- escalate; not payroll) |

### Key handoff points

- **Payroll -> Bookkeeping:** Gross wages and the employer's 34% FSZN + Belgosstrakh are expenses; the 13% PIT and the 1% employee FSZN are liabilities until remitted to MNS/FSZN.
- **Payroll -> Income Tax:** The employer's annual income/withholding report feeds the individual's record; high earners (> BYN 220,000) must file their own annual declaration by 31 March for the 25% surtax on the excess.
- **Payroll -> VAT:** Independent of NDS; salaries are outside the scope of VAT.

## PROHIBITIONS

- NEVER withhold the 25% high-income surtax through monthly payroll -- it is assessed on the individual's annual declaration (filed by 31 March) for income over BYN 220,000 in 2025
- NEVER apply the 2026 BYN 350,000 threshold or 30% top band to 2025 payroll -- they are a forward change effective 2026
- NEVER apply the BYN 192 standard deduction when monthly income exceeds BYN 1,164 -- it is income-tested
- NEVER subtract the 1% employee FSZN from the PIT base -- the PIT base is gross minus the BYN standard/child/category deductions, not minus FSZN
- NEVER withhold the employer's 34% FSZN or the Belgosstrakh premium from the employee -- only the 1% FSZN and 13% PIT come out of the employee's pay
- NEVER use the 0.1% Belgosstrakh rate for a private employer -- 0.1% is for budget/state organisations; the standard private rate is 0.6%
- NEVER assume an FSZN ceiling for a standard employer in 2025 -- contributions are on full gross (only HTP residents may cap the base at the Belstat average wage)
- NEVER treat self-employed/individual-entrepreneur FSZN (35%, self-paid) as employer payroll
- NEVER miss the 22nd-of-following-month remittance deadline for PIT and FSZN, or the quarterly Form 4-fund / PU-3 -- peni and fines apply
- NEVER quantify payroll arrears, peni, or fines without an MNS/FSZN statement -- the exact 2025 formula is unconfirmed; escalate to a qualified accountant
- NEVER treat the 6%/0% dividend rates or the BYN 25m corporate band as confirmed 2025 figures -- they are from a 2024 snapshot and must be re-verified
- NEVER present payroll computations as definitive -- always label as estimated and direct to a licensed Belarusian accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Belarusian accountant or auditor) before implementation.

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
