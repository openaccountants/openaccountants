---
name: rwanda-payroll
description: Use this skill whenever asked about Rwanda payroll processing for employed persons. Trigger on phrases like "Rwanda payroll", "PAYE Rwanda", "RRA PAYE", "RSSB contribution", "pension Rwanda", "occupational hazards Rwanda", "maternity contribution Rwanda", "RAMA", "medical insurance Rwanda", "CBHI", "Mutuelle de Santé", "Ejo Heza", "casual labour Rwanda", "net salary Rwanda", "tax withholding Rwanda", "employer RSSB", "minimum wage Rwanda", "gross to net Rwanda", "salary calculation Rwanda", "RWF payroll", "Frw salary", or any question about computing employee pay, income-tax (PAYE) withholding, or social-security contributions for Rwanda-based employees. This skill covers PAYE income-tax withholding by the employer, RSSB pension, occupational hazards, maternity leave benefits, medical insurance and CBHI contributions, casual-labour withholding, minimum wage, and filing obligations to RRA/RSSB. ALWAYS read this skill before processing any Rwanda payroll.
version: 0.1
jurisdiction: RW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Rwanda Payroll

## Rwanda Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** Several figures carry `[RESEARCH GAP — reviewer to confirm]` markers. A licensed Rwandan tax practitioner / accountant must reconcile those before any output is presented as final.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Rwanda (Republic of Rwanda) |
| Currency | Rwandan Franc (RWF / Frw) only |
| Standard pay frequency | Monthly (most common) |
| Tax year | Calendar year (1 January -- 31 December) (PwC — Tax administration) |
| Income tax | YES — PAYE (Pay-As-You-Earn), progressive 0% / 10% / 20% / 30%, employer-withheld monthly (Law 027/2022) |
| Tax authority | RRA (Rwanda Revenue Authority) |
| Social security authority | RSSB (Rwanda Social Security Board) |
| Pension scheme | RSSB pension (12% total in 2025; phasing to 20% by 2030) (PwC — Other taxes) |
| Other RSSB schemes | Occupational hazards, maternity leave benefits, medical insurance (RAMA), CBHI |
| PAYE monthly deadline | **15th day of the following month** (PwC — Tax administration) |
| RSSB monthly deadline | **15th day of the following month** (RRA — RSSB declaration & payment) |
| Annual ISR return deadline | **31 March** of following year; employment-only earners exempt (PwC) |
| Key legislation | Law No. 027/2022 (income tax); Law No. 020/2023 (tax procedures); RSSB pension/social-security laws |
| Filing portal | RRA online portal (e-tax / declaration system) |
| Validated by | Pending -- requires sign-off by a licensed Rwandan tax practitioner |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (PAYE — Pay-As-You-Earn)

Rwanda **does** levy personal income tax on employees. The employer is the **withholding agent**: it deducts PAYE monthly from payroll and remits it monthly to RRA by the 15th of the following month (PwC — Tax administration). The brackets are expressed on **MONTHLY taxable employment income in RWF** and were set by **Law No. 027/2022 of 20/10/2022**, with the bracket structure fully phased in from **November 2023** (PwC, last reviewed 18 Feb 2026; RRA calculation guide).

### PAYE Progressive Table — Monthly Taxable Income (2025, CONFIRMED)

**PAYE Progressive Table — Monthly Taxable Income (2025, CONFIRMED)**  _(Source: RRA calculation guide (Law 027/2022, monthly bands, raised 0% threshold); PwC — Taxes on personal income.)_

| Monthly taxable income (RWF) | Marginal rate | Tax on this bracket (cumulative at top) |
| --- | --- | --- |
| 0 – 60,000 | **0%** | Frw 0 |
| 60,001 – 100,000 | **10%** | Frw 4,000 |
| 100,001 – 200,000 | **20%** | Frw 24,000 |
| 200,001 and above | **30%** | — |

- **Residency scope** — Same rates apply to residents and non-residents  _(PwC)_
- **Local taxes** — No local / municipal income taxes in Rwanda  _(PwC)_
- **0% threshold history** — The 0% threshold (first Frw 60,000/month) was raised from the prior Frw 30,000 when Law 027/2022 took effect  _(RRA)_

**Subtract-method constants (2025)**  _(monthly tax = (monthly taxable income × rate) − subtract)_

| Band (RWF) | Rate | Subtract (RWF) |
| --- | --- | --- |
| 60,001 – 100,000 | 10% | 6,000 |
| 100,001 – 200,000 | 20% | 16,000 |
| 200,001+ | 30% | 36,000 |

*Continuity check:*
- At 100,000 → 0.10 × 100,000 − 6,000 = **Frw 4,000** (= cumulative band tax). Tie out.
- At 200,000 → 0.20 × 200,000 − 16,000 = **Frw 24,000**. Tie out.
- Band entry at 200,001 → 0.30 × 200,001 − 36,000 = **Frw 24,000.30** ≈ continuous with Frw 24,000. Tie out.

### Casual labour rate

**Casual labour rate**

| Item | Detail | Source |
| --- | --- | --- |
| Casual labourer engaged **< 30 days** in a tax year | Employer withholds a flat **15%** of taxable employment income | RRA calculation guide |
| Tax-free portion for casual labour | Secondary sources conflict (Frw 30,000 older vs Frw 60,000 aligned to general threshold). The **15% flat rate is authoritative**; the exact tax-free slice is **[RESEARCH GAP — reviewer to confirm against current RRA casual-labour rules]** | RRA |

### Withholding mechanism

- **PAYE withholding cadence** — PAYE is withheld monthly by the employer from payroll and remitted monthly to RRA by the 15th  _(PwC)_
- **Annual return exemption** — Individuals earning only employment income are exempt from filing an annual return — PAYE is final. Those with additional income types must file by 31 March.  _(PwC — Tax administration)_

## Section 3 -- RSSB Pension Scheme (Employee + Employer)

All persons working in Rwanda (nationals and foreigners) must contribute to RSSB-managed schemes. The **employer deducts, declares and pays both employer and employee shares** (RRA — RSSB declaration).

> **MAJOR 2025 CHANGE:** the pension rate **doubled from 6% to 12% effective 1 January 2025**, split equally employer/employee, with phased increases to **20% by 2030** (PwC — Other taxes; VisionsAfrica advisory). The contribution **base was expanded in 2025 to include the transport allowance** (previously excluded) (VisionsAfrica).

### Pension Contribution Schedule (basis: gross salary)

**Pension Contribution Schedule (basis: gross salary)**  _(Source: PwC — Other taxes (full schedule, splits, basis); VisionsAfrica (2025 base now includes transport).)_

| Effective | Total | Employer | Employee |
| --- | --- | --- | --- |
| From 1 Jan 2025 | **12%** | 6% | 6% |
| From 1 Jan 2027 | 14% | 7% | 7% |
| From 1 Jan 2028 | 16% | 8% | 8% |
| From 1 Jan 2029 | 18% | 9% | 9% |
| From 1 Jan 2030 | 20% | 10% | 10% |

- **Prior rate** — Prior rate (through 2024) was 6% total / 3% each  _(PwC)_
- **Salary ceiling** — No salary ceiling/cap on pension was found in authoritative sources — contributions appear uncapped (percentage of full gross). [RESEARCH GAP — reviewer to confirm absence of a ceiling with RSSB].

*Column check (2025):* employer 6% + employee 6% = **12%** total. Tie out.

## Section 4 -- RSSB Occupational Hazards Scheme

**Occupational Hazards Scheme**  _(PwC — Other taxes)_

| Item | Total | Employer | Employee | Basis | Source |
| --- | --- | --- | --- | --- | --- |
| Occupational hazards | **2%** | **2%** | **0%** | Gross salary | PwC — Other taxes |

Employer pays **100%** of the 2%; the employee pays nothing.

*Column check:* employer 2% + employee 0% = **2%** total. Tie out.

## Section 5 -- RSSB Maternity Leave Benefits Scheme

**Maternity Leave Benefits Scheme**  _(PwC — Other taxes)_

| Item | Total | Employer | Employee | Source |
| --- | --- | --- | --- | --- |
| Maternity leave benefits | **0.6%** | **0.3%** | **0.3%** | PwC — Other taxes |

- **Basis** — Basis: gross pay including benefits in kind, excluding transport allowance and termination/retirement benefits  _(PwC)_

*Column check:* employer 0.3% + employee 0.3% = **0.6%** total. Tie out.

## Section 6 -- RSSB Medical Insurance Scheme (RAMA / RSSB medical)

**Medical Insurance Scheme**  _(RRA — Medical Insurance Scheme)_

| Item | Total | Employer | Employee | Basis | Source |
| --- | --- | --- | --- | --- | --- |
| Medical insurance | **15%** | **7.5%** | **7.5%** | **BASIC salary** | RRA — Medical Insurance Scheme |

- **Mandatory enrolment** — Mandatory for civil servants / public institutions. Private institutions may/must enrol if they meet registration requirements — must have at least 7 employees and enrol all staff (no individual opt-outs)  _(RRA)_
- **Pensioners deduction** — Pensioners: 7.5% deducted from monthly pension  _(RRA)_

Basis is basic salary, not full gross (distinct from pension/occupational/maternity which use gross).

*Column check:* employer 7.5% + employee 7.5% = **15%** total. Tie out.

## Section 7 -- Community-Based Health Insurance (CBHI / Mutuelle de Santé)

**CBHI Scheme**  _(PwC — Other taxes)_

| Item | Total | Employer | Employee | Source |
| --- | --- | --- | --- | --- |
| CBHI / CBHIS | **0.5%** | **0% (collects only)** | **0.5%** | PwC — Other taxes |

- **Employee-only contribution** — Employee-only contribution; the employer collects and remits it but pays no employer share.  _(PwC)_
- **CBHI base** — Basis: NET salary = gross salary + taxable benefits − PAYE − pension − occupational hazards − maternity contributions. (Medical insurance is not subtracted in arriving at the CBHI base.)  _(PwC)_

*Column check:* employer 0% + employee 0.5% = **0.5%** total. Tie out.

## Section 8 -- Combined Employer / Employee Social Burden (2025)

For a **private employer enrolled in the medical scheme** (7+ employees), on an employee with no separate transport-allowance split (so basic = gross for illustration):

**Combined burden table**

| Contribution | Employee | Employer | Basis |
| --- | --- | --- | --- |
| PAYE | 0–30% progressive | (withholding agent) | monthly taxable income |
| Pension | 6% | 6% | gross |
| Occupational hazards | — | 2% | gross |
| Maternity | 0.3% | 0.3% | gross (excl. transport / termination) |
| Medical insurance | 7.5% | 7.5% | basic |
| CBHI | 0.5% | — | net |

*Employee social column (excl. PAYE, where basic = gross):* 6% + 0.3% + 7.5% + 0.5% = **14.3%** (the CBHI 0.5% is on net, the rest on gross/basic, so this is an upper-bound shorthand — compute each on its own base).
*Employer social column (where basic = gross):* 6% + 2% + 0.3% + 7.5% = **15.8%** of gross.

> If the employer is **not** enrolled in the medical scheme (e.g. fewer than 7 employees and not a public institution), drop the 7.5% / 7.5% medical lines. CBHI 0.5% (employee) and the other RSSB schemes still apply.

## Section 9 -- Minimum Wage

**Minimum Wage**  _(Mywage.org / WageIndicator)_

| Item | Detail | Source |
| --- | --- | --- |
| Statutory national minimum wage | **None effective / enforceable.** The only formally established rate dates to **1974 (Frw 100/day ≈ Frw 2,440/month)** and is obsolete and not enforced | Mywage.org / WageIndicator |
| Practice | Wages set by **sector agreements / collective bargaining** (e.g. mining sector living wage ~Frw 1,500/day as of 2025) | Mywage.org / WageIndicator |
| Status | A statutory minimum wage has been discussed but **not yet introduced** | Mywage.org / WageIndicator |

> Do **not** rely on the 1974 figure as a contractual floor. Use the employee's contract and any applicable sector agreement; flag for the reviewer where no sector benchmark exists.

## Section 10 -- Conservative Defaults

When an input is missing or ambiguous, apply the **conservative** assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

**Conservative Defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| Whether employer is enrolled in medical scheme | If headcount ≥ 7 → assume **enrolled** (7.5%/7.5%); FLAG | Mandatory once registration criteria met |
| Headcount unknown | Compute **without** medical scheme but FLAG; never silently apply 15% | Avoids fabricating a 15% deduction |
| Transport allowance split | If basic vs gross not given, treat **basic = gross** for medical (higher base) and include transport in pension base | Pension base now includes transport (2025) |
| Pension rate | Use **12% (6%/6%)** for 2025 | 2025 doubled rate |
| Casual labour (< 30 days) | Apply **15% flat**; do NOT assume a tax-free slice | Tax-free portion unconfirmed |
| Salary ceiling on RSSB | Apply percentages on **full gross/basic** (no cap) | No ceiling found; flag |
| Tax year | Default to **2025** brackets unless date ≥ 1 Jan 2026 | Skill tax_year is 2025 |
| Currency | Rwandan Franc (RWF) | Local currency |
| Annual return for employment-only earner | Treat PAYE as **final**; no annual return | PwC |

## Section 11 -- Required Inputs + Refusal Catalogue

### Required inputs before computing payroll

1. Gross monthly salary in RWF, and the **basic-salary** component (medical scheme uses basic).
2. Transport-allowance amount (enters pension base from 2025; excluded from maternity base).
3. Pay frequency and whether the worker is a **casual labourer** (< 30 days engagement).
4. Number of employees on the payroll (drives medical-scheme enrolment).
5. Tax/fiscal year (2025 vs later bracket/pension schedule).
6. Whether the employer is a public institution or private (medical-scheme mandate).
7. Any non-ordinary pay components (termination/retirement benefits, benefits in kind).

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue**

| Situation | Action |
| --- | --- |
| No gross salary provided | REFUSE — request salary in RWF |
| Medical scheme needed but basic-salary component not given | REFUSE the medical line — request basic salary; compute the rest |
| Request to omit PAYE or RSSB contributions to "save money" | REFUSE — statutory; escalate to accountant |
| Request to skip pension at the old 6% rate for a 2025 period | REFUSE — 2025 rate is 12% (6%/6%) |
| Request to treat casual labour tax-free slice as a fixed figure | REFUSE the exact figure — flag the research gap; apply 15% flat |
| Self-employed / non-employment income mixed in | REFUSE payroll path — route to a Rwanda income-tax skill (annual return) |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |

## Section 12 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins. Rwandan statements appear in English, French, or Kinyarwanda.

### Salary credits (money arriving in an employee account)

**Salary credits pattern table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARY`, `UMUSHAHARA`, `SALAIRE`, `PAYROLL`, `NET PAY` | Net salary payment |
| `TRANSF.* [employer]`, `ABONO`, `WAGE` | Net salary payment |
| `RSSB REFUND`, `REMBOURSEMENT RSSB` | RSSB refund/adjustment — not income |
| `RRA REFUND`, `PAYE REFUND` | PAYE refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits pattern table**

| Pattern | Classification |
| --- | --- |
| `RRA`, `PAYE`, `IMPOSTO`, `WITHHOLDING TAX` | PAYE withholding remitted to RRA (liability settlement) |
| `RSSB`, `PENSION`, `OCCUPATIONAL`, `MATERNITY` | RSSB contribution (pension / occupational / maternity) |
| `RAMA`, `MEDICAL INSURANCE`, `ASSURANCE MALADIE` | RSSB medical-insurance contribution |
| `CBHI`, `MUTUELLE`, `CBHIS` | CBHI (employee-only) collected/remitted |
| `NET WAGES`, `PAIE`, `DISBURSEMENT`, `SALARY RUN` | Net wages disbursed to employees |

## Section 13 -- Worked Examples

> All figures use the **2025** PAYE table and 2025 RSSB rates (pension 6%/6%). Where the employer is enrolled in the medical scheme, basic = gross is assumed for illustration. Occupational hazards is employer-only (no employee deduction). CBHI base = gross − PAYE − pension − occupational(0 ee) − maternity. Amounts rounded to the franc/centime.

### Example 1 — Low earner below the exempt threshold (no medical scheme)

**Inputs:** Gross salary Frw 50,000/month. Small employer (< 7 staff), **not** medical-enrolled.

- PAYE: 50,000 ≤ 60,000 → **Frw 0**.
- Pension employee 6% × 50,000 = **Frw 3,000**.
- Maternity employee 0.3% × 50,000 = **Frw 150**.
- CBHI base (net) = 50,000 − 0 − 3,000 − 0 − 150 = 46,850 → CBHI 0.5% × 46,850 = **Frw 234.25**.
- **Employee deductions total** = 3,000 + 150 + 234.25 = **Frw 3,384.25**.
- **Net pay** = 50,000.00 − 3,384.25 = **Frw 46,615.75**.

*Bank line example:* `UMUSHAHARA — JUNE` credit **Frw 46,615.75**.

### Example 2 — Mid earner in the 20% PAYE band (medical-enrolled)

**Inputs:** Gross = basic = Frw 150,000/month. Private employer, ≥ 7 staff, medical-enrolled.

- PAYE: 150,000 in 20% band → 0.20 × 150,000 − 16,000 = 30,000 − 16,000 = **Frw 14,000**.
  - Verify by bands: 0 (first 60k) + 4,000 (60k–100k @10%) + 10,000 (100k–150k @20%) = 14,000. Tie out.
- Pension employee 6% × 150,000 = **Frw 9,000**.
- Maternity employee 0.3% × 150,000 = **Frw 450**.
- Medical employee 7.5% × basic 150,000 = **Frw 11,250**.
- CBHI base (net) = 150,000 − 14,000 − 9,000 − 0 − 450 = 126,550 → CBHI 0.5% = **Frw 632.75**.
- **Employee deductions total** = 14,000 + 9,000 + 450 + 11,250 + 632.75 = **Frw 35,332.75**.
- **Net pay** = 150,000.00 − 35,332.75 = **Frw 114,667.25**.

### Example 3 — Higher earner in the 30% PAYE band (medical-enrolled)

**Inputs:** Gross = basic = Frw 500,000/month. Private employer, medical-enrolled.

- PAYE: 500,000 in 30% band → 0.30 × 500,000 − 36,000 = 150,000 − 36,000 = **Frw 114,000**.
  - Verify by bands: 0 + 4,000 + 20,000 (100k–200k @20%) + 90,000 (200k–500k @30%) = 114,000. Tie out.
- Pension employee 6% × 500,000 = **Frw 30,000**.
- Maternity employee 0.3% × 500,000 = **Frw 1,500**.
- Medical employee 7.5% × 500,000 = **Frw 37,500**.
- CBHI base (net) = 500,000 − 114,000 − 30,000 − 0 − 1,500 = 354,500 → CBHI 0.5% = **Frw 1,772.50**.
- **Employee deductions total** = 114,000 + 30,000 + 1,500 + 37,500 + 1,772.50 = **Frw 184,772.50**.
- **Net pay** = 500,000.00 − 184,772.50 = **Frw 315,227.50**.

### Example 4 — Employer total cost of the mid earner (Frw 150,000/month, medical-enrolled)

**Employer total cost table**

| Employer cost item | Computation | Amount (Frw) |
| --- | --- | --- |
| Gross salary | — | 150,000.00 |
| Pension employer 6% | 6% × 150,000 | 9,000.00 |
| Occupational hazards 2% | 2% × 150,000 | 3,000.00 |
| Maternity employer 0.3% | 0.3% × 150,000 | 450.00 |
| Medical employer 7.5% | 7.5% × 150,000 | 11,250.00 |
| CBHI employer share | — (employee-only) | 0.00 |
| **Total employer cost** | sum | **173,700.00** |

*Check:* 150,000 + 9,000 + 3,000 + 450 + 11,250 = **173,700.00**. Tie out.
(Employer-on-top burden = Frw 23,700.00 = **15.8%** of gross at this salary.)

### Example 5 — Casual labourer (< 30 days)

**Inputs:** Casual engagement, taxable employment income Frw 80,000 for the period.

- PAYE = flat **15% × 80,000 = Frw 12,000** (RRA casual-labour rate).
- Net of PAYE = 80,000 − 12,000 = **Frw 68,000**.

> **[RESEARCH GAP — reviewer to confirm]** A tax-free portion for casual labour may apply before the 15% (Frw 30,000 vs Frw 60,000 in conflicting secondary sources). This example applies 15% to the full Frw 80,000; confirm the exact tax-free slice against current RRA casual-labour rules.

### Example 6 — Earner exactly at the exempt boundary (Frw 60,000, no medical scheme)

**Inputs:** Gross salary Frw 60,000/month. Small employer, **not** medical-enrolled.

- PAYE: 60,000 ≤ 60,000 → **Frw 0**.
- Pension employee 6% × 60,000 = **Frw 3,600**.
- Maternity employee 0.3% × 60,000 = **Frw 180**.
- CBHI base (net) = 60,000 − 0 − 3,600 − 0 − 180 = 56,220 → CBHI 0.5% = **Frw 281.10**.
- **Employee deductions total** = 3,600 + 180 + 281.10 = **Frw 4,061.10**.
- **Net pay** = 60,000.00 − 4,061.10 = **Frw 55,938.90**.

## Section 14 -- Tier 1 Rules (hard, non-negotiable)

- **Rule 1** — PAYE is employer-withheld monthly and remitted to RRA by the 15th of the following month; never skip it for salaried staff  _(PwC)_
- **Rule 2** — Use the monthly taxable-income table and apply the subtract-method constants exactly (6,000 / 16,000 / 36,000).
- **Rule 3** — Pension is 12% (6%/6%) for 2025 — never use the old 6% rate for a 2025 period  _(PwC; VisionsAfrica)_
- **Rule 4** — The pension base includes the transport allowance from 2025  _(VisionsAfrica)_
- **Rule 5** — Occupational hazards (2%) is employer-only; maternity (0.6%) splits 0.3%/0.3%.
- **Rule 6** — Medical insurance (15%, 7.5%/7.5%) is on basic salary and applies only where the employer is enrolled (public, or private with ≥ 7 employees, all staff enrolled)  _(RRA)_
- **Rule 7** — CBHI (0.5%) is employee-only, on net salary; the employer collects but pays no share  _(PwC)_
- **Rule 8** — RSSB contributions are remitted monthly by the 15th of the following month  _(RRA)_
- **Rule 9** — Every output is an estimate pending licensed-accountant sign-off.

## Section 15 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Question | Why it needs a reviewer |
| --- | --- |
| Casual-labour tax-free portion (30,000 vs 60,000) | Secondary sources conflict; only the 15% flat rate is confirmed |
| Penalty percentages (20% / 40% / 60%) | Sourced from an advisory firm summarising Law 020/2023, not RRA primary text |
| Medical-scheme remittance date (10th vs 15th) | One RRA medical page references the 10th; general RSSB deadline is the 15th |
| Absence of an RSSB salary ceiling/cap | No cap found in sources; confirm explicitly with RSSB |
| Exact maternity-base treatment of benefits in kind | "Excl. transport/termination" confirmed; in-kind edge cases not |
| Whether a specific private employer must enrol in medical scheme | Depends on ≥ 7 employees + registration criteria |

## Section 16 -- Excel Working Paper Template

Suggested layout (one row per employee per month):

**Excel Working Paper Template table**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Gross monthly salary (Frw) | input |
| C | Basic salary (Frw) | input (drives medical) |
| D | Medical-enrolled? (Y/N) | input (headcount ≥ 7 or public) |
| E | PAYE (monthly) | nested IF on B using subtract constants (6,000 / 16,000 / 36,000) |
| F | Pension employee | `=B*6%` |
| G | Maternity employee | `=B*0.3%` |
| H | Medical employee | `=IF(D="Y", C*7.5%, 0)` |
| I | CBHI base (net) | `=B - E - F - 0 - G` |
| J | CBHI employee | `=I*0.5%` |
| K | Employee deductions | `=E+F+G+H+J` |
| L | Net pay | `=B-K` |
| M | Pension employer | `=B*6%` |
| N | Occupational hazards | `=B*2%` |
| O | Maternity employer | `=B*0.3%` |
| P | Medical employer | `=IF(D="Y", C*7.5%, 0)` |
| Q | Total employer cost | `=B+M+N+O+P` |

- **PAYE formula for column E (2025, monthly)** — `=IF(B<=60000,0, IF(B<=100000, B*0.10-6000, IF(B<=200000, B*0.20-16000, B*0.30-36000)))`

## Section 17 -- Bank Statement / Terminology Reading Guide

**Terminology Reading Guide**

| Term (English / French / Kinyarwanda) | Meaning |
| --- | --- |
| Salary / Salaire / Umushahara | Salary / wage |
| PAYE | Pay-As-You-Earn income-tax withholding |
| RRA (Rwanda Revenue Authority) | Tax authority |
| RSSB (Rwanda Social Security Board) | Social-security authority |
| Pension / Retraite | Pension scheme contribution |
| Occupational hazards / Risques professionnels | Occupational-risk scheme (employer-only) |
| Maternity / Maternité | Maternity-leave benefits scheme |
| RAMA / Medical insurance / Assurance maladie | RSSB medical-insurance scheme (basic salary) |
| CBHI / CBHIS / Mutuelle de Santé | Community-Based Health Insurance (employee-only, on net) |
| Casual labourer | Worker engaged < 30 days/year (flat 15% PAYE) |
| Net pay / Net à payer | Take-home pay after deductions |
| Transport allowance / Indemnité de transport | Allowance now in pension base (2025) |

## Section 18 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior payroll register available** → request the last 3 months of payroll and RRA/RSSB receipts to back-solve the rates actually applied.
2. **Unknown headcount** → default medical scheme OFF, FLAG; confirm before first remittance.
3. **Unknown basic-vs-gross split** → request the contract; medical needs basic salary specifically.
4. **Unknown transport allowance** → confirm; it enters the pension base (2025) and is excluded from the maternity base.
5. **Year ambiguity** → default 2025 table/rates; switch only for periods ≥ 1 Jan of a later year (pension steps up again in 2027).

## Section 19 -- Filing, Forms & Deadlines

**Filing, Forms & Deadlines table**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | PwC — Tax administration |
| PAYE | Declared and remitted to RRA **monthly**, by the **15th** of the following month, via the RRA online portal | PwC; RRA — Declare PAYE |
| RSSB contributions | Declared and paid **monthly**, by the **15th** of the following month | RRA — RSSB declaration & payment |
| Medical-scheme remittance | One RRA medical page references the **10th** of the following month — general RSSB deadline is the 15th. **[RESEARCH GAP — reviewer to reconcile the medical-scheme-specific date]** | RRA — Medical Insurance Scheme |
| Annual return | Generally due **31 March** of the following year; **employment-only earners are exempt** (PAYE is final) | PwC — Tax administration |
| Registration | Employers must register for **PAYE** with RRA and with **RSSB**; medical-scheme enrolment requires ≥ 7 employees (all enrolled) | RRA — PAYE obligations; RRA — Medical Insurance |

## Section 20 -- Penalties (late filing / late payment)

Governed by the **Tax Procedures Law (Law No. 020/2023)** and RSSB rules.

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Late declaration / late payment (≤ 30 days) | **20%** of tax due | ALSM — Law 020/2023 summary |
| Late by 31–60 days | **40%** of tax due | ALSM — Law 020/2023 summary |
| Late by more than 60 days | **60%** of tax due | ALSM — Law 020/2023 summary |
| Late-payment interest | **1.5% per month** on the overdue amount | ALSM; RRA — RSSB declaration |
| RSSB-specific | Employers failing to remit on time are subject to **forced recovery** procedures | RRA — RSSB declaration |

> **[RESEARCH GAP — reviewer to confirm]** The graduated penalty percentages (20% / 40% / 60%) are from a reputable Rwandan tax-advisory firm summarising Law 020/2023, **not** the RRA primary Tax Procedures Law text. The RRA Tax Handbook was unreachable during research; cross-check the exact figures against the RRA Tax Procedures Law / Tax Handbook before relying on them.

## Section 21 -- Reference Material

**Reference Material table**

| Topic | Figure | Source |
| --- | --- | --- |
| PAYE 0% band | 0 – 60,000 RWF/month | RRA; PwC |
| PAYE bands | 10% / 20% / 30% at 100,000 / 200,000 edges | RRA; PwC (Law 027/2022) |
| Casual labour | 15% flat (< 30 days) | RRA calculation guide |
| Pension 2025 | 12% total (6% ee / 6% er), gross incl. transport | PwC; VisionsAfrica |
| Occupational hazards | 2% employer-only, gross | PwC |
| Maternity | 0.6% total (0.3% / 0.3%), gross excl. transport/termination | PwC |
| Medical insurance | 15% total (7.5% / 7.5%), basic; ≥ 7 employees to enrol | RRA — Medical Insurance |
| CBHI | 0.5% employee-only, net | PwC |
| PAYE / RSSB deadline | 15th of following month | PwC; RRA |
| Annual return | 31 March; employment-only exempt | PwC |
| Penalties | 20% / 40% / 60% + 1.5%/month interest | ALSM (Law 020/2023) — flagged |
| Minimum wage | No enforceable statutory rate (1974 Frw 100/day obsolete) | Mywage.org / WageIndicator |

Key authorities: RRA (`rra.gov.rw`, e-tax portal), RSSB. Big-4/secondary: PwC Tax Summaries (individual + corporate other taxes), VisionsAfrica advisory, ALSM (Law 020/2023 summary), Mywage.org / WageIndicator.

## Section 22 -- Test Suite

Each test recomputes end-to-end. Expected values use the 2025 PAYE table and 2025 RSSB rates.

Exempt earner. Gross Frw 50,000/mo, no medical scheme. Expected: PAYE = Frw 0; employee pension Frw 3,000; maternity Frw 150; CBHI Frw 234.25; net Frw 46,615.75.

20% band, medical-enrolled. Gross = basic Frw 150,000/mo. PAYE Frw 14,000; pension Frw 9,000; maternity Frw 450; medical Frw 11,250; CBHI Frw 632.75; net Frw 114,667.25.

30% band, medical-enrolled. Gross = basic Frw 500,000/mo. PAYE Frw 114,000; medical Frw 37,500; CBHI Frw 1,772.50; net Frw 315,227.50.

Employer cost. Gross = basic Frw 150,000/mo, medical-enrolled. Total employer cost Frw 173,700.00 (burden 15.8% of gross).

Casual labour. Taxable income Frw 80,000, < 30 days. PAYE = Frw 12,000 (15% flat); net of PAYE Frw 68,000 (tax-free slice is a research gap).

Boundary earner. Gross Frw 60,000/mo, no medical. PAYE Frw 0; net Frw 55,938.90.

Bracket continuity. At monthly 100,000 → PAYE Frw 4,000; at 200,000 → PAYE Frw 24,000 (subtract constants 6,000 / 16,000 / 36,000 tie out).

Pension rate guard. A 2025 period computed at the old 6% total (3%/3%) is WRONG — must be 12% (6%/6%).

CBHI base. Gross 150,000, PAYE 14,000, pension 9,000, maternity 450 → CBHI base 126,550; CBHI Frw 632.75 (medical NOT subtracted in the base).

Currency / minimum-wage refusal. Treating the 1974 Frw 100/day as a contractual floor → REFUSE; request the contract / sector benchmark.

## PROHIBITIONS

- **PAYE withholding** — NEVER skip PAYE withholding for salaried employees — the employer is the legal withholding agent.
- **2025 pension rate** — NEVER use the old 6% total pension rate for a 2025 period — it doubled to 12% (6%/6%) on 1 Jan 2025.
- **Transport allowance in pension base** — NEVER omit the transport allowance from the pension base for 2025 onward.
- **Medical insurance base** — NEVER apply the medical-insurance 15% to full gross — it is on basic salary, and only where the employer is enrolled.
- **CBHI employer share** — NEVER charge an employer share of CBHI — it is employee-only (0.5% on net); the employer only collects.
- **Casual labour tax-free slice** — NEVER assume a fixed casual-labour tax-free slice — apply 15% flat and flag the research gap.
- **Penalty percentages sourcing** — NEVER state the 20%/40%/60% penalty percentages as RRA-confirmed — they are an advisory-firm summary of Law 020/2023.
- **RSSB salary ceiling** — NEVER apply an RSSB salary ceiling without confirming one exists — no cap was found in the sources.
- **Obsolete minimum wage** — NEVER rely on the obsolete 1974 minimum wage as a contractual floor.
- **Estimated computations disclosure** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Rwandan accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax practitioner in Rwanda) before implementation.

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
