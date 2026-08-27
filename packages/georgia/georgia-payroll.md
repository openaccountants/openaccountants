---
name: georgia-payroll
description: "Use this skill whenever asked about Georgia (the country / Republic of Georgia — Sakartvelo, Caucasus) payroll processing for employed persons. Trigger on phrases like \"Georgia payroll\", \"Georgian payroll\", \"khelfasi\", \"salary tax Georgia\", \"PIT withholding Georgia\", \"20% income tax Georgia\", \"PAYE Georgia\", \"funded pension Georgia\", \"pension contribution Georgia\", \"Pension Agency\", \"pensions.ge\", \"Revenue Service Georgia\", \"rs.ge payroll\", \"monthly withholding declaration Georgia\", \"net salary Georgia\", \"gross to net Georgia\", \"employer cost Georgia\", \"minimum wage Georgia\", or any question about computing employee pay, salary withholding tax, or mandatory funded pension contributions for Georgia-based employees. This skill covers the flat 20% personal income tax withheld at source (PAYE), the mandatory funded pension (employer 2% + employee 2% + state co-contribution), participation rules, the monthly withholding declaration on rs.ge, and penalties. CRITICAL: jurisdiction code GE here is the COUNTRY of Georgia (currency GEL, lari) — NOT the US state of Georgia (USD). ALWAYS read this skill before processing any Georgia (country) payroll."
version: 0.1
jurisdiction: GE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Gvantsa Amiridze
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia Payroll

## Georgia Payroll Skill v0.1

> **Tier 2 — Research-verified.** Rates and structure are cross-verified across PwC Worldwide Tax Summaries (Georgia, Individual & Corporate), the Law of Georgia "On Funded Pension" (matsne.gov.ge), the Tax Code of Georgia, Mondaq/Eurofast and Georgian practitioner sources (TPsolution, CXC Global). Official Georgian-language statute PDFs were not directly text-extracted line-by-line; figures rely on the English consolidations on matsne.gov.ge plus Big-4 and specialist summaries. Every figure below carries an inline source or a `[RESEARCH GAP — reviewer to confirm]` marker. A qualified Georgian tax adviser / authorised accountant must validate this skill before production use.

> **CRITICAL DISAMBIGUATION.** Jurisdiction code **GE = the country / Republic of Georgia (Sakartvelo, Caucasus), currency GEL (Georgian lari)**. This skill has **nothing to do with the US state of Georgia** (USD, Form G-7, ~5.19% flat state rate). If a request concerns the US state, this is the WRONG skill — escalate.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Georgia (Republic of Georgia / Sakartvelo — Caucasus, NOT the US state) |
| Jurisdiction code | GE |
| Currency | GEL (Georgian lari) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December). Source: PwC WWTS Georgia, Tax administration. |
| Has personal income tax? | Yes -- **flat 20%** on gross employment income, withheld at source (PAYE). Source: PwC WWTS Georgia, Corporate: Other taxes. |
| Personal income tax (salary) | 20% flat on gross salary. **No tax-free personal allowance; no progressive bands.** Source: PwC WWTS Georgia. |
| Funded pension -- employer | 2% of gross salary. Source: Law on Funded Pension Art. 3(6); PwC WWTS Georgia, Individual: Other taxes. |
| Funded pension -- employee (withheld) | 2% of gross salary. Source: Law on Funded Pension Art. 3(6). |
| Funded pension -- state co-contribution | 2% if annual income < GEL 24,000; 1% on the GEL 24,000--60,000 portion; 0% above GEL 60,000 (paid by the Government, not the employer). Source: Law on Funded Pension Art. 3(6). |
| Other employer social/payroll tax | **None** -- there is no general employer social-security or payroll tax in Georgia beyond the 2% funded pension. Source: PwC WWTS Georgia, Corporate: Other taxes. |
| Tax authority | Revenue Service of Georgia (Sakartvelos Shemosavlebis Samsakhuri), Ministry of Finance |
| Pension administrator | LEPL Pension Agency (pensions.ge) |
| Filing portal | rs.ge / eservices.rs.ge |
| Primary forms | Monthly withholding (PIT) declaration; annual individual income tax declaration; funded-pension transfer to the Pension Agency |
| Monthly declaration deadline | By the **15th** of the month following the payment month; PIT payment due on the day wages are paid. Source: PwC WWTS Georgia, Tax administration; TPsolution. |
| Validated by | Pending -- requires sign-off by a qualified Georgian tax adviser / authorised accountant |
| Skill version | 0.1 |

**Legislation table**

| Law | Scope | Source |
| --- | --- | --- |
| Tax Code of Georgia (Law No. 3591, 2010, as amended) | PIT withholding, declarations, penalties | matsne.gov.ge |
| Law of Georgia "On Funded Pension" (2018; in force from 1 Jan 2019) | Mandatory funded pension contributions | matsne.gov.ge |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified Georgian tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate and document the gap.

## Section 2 -- Personal Income Tax (PIT) Withholding -- PAYE

- **PIT flat rate and withholding at source** — Employment income is taxed at a flat 20%, withheld at source by the employer at the moment of salary payment and remitted to the Revenue Service. There is no progressive bracket for employment income, and no GENERAL tax-free personal allowance — but Tax Code Article 82 does grant specific exemptions to defined categories (see "No allowances, no cap adjustment").  _(Tax Code of Georgia Art. 82; PwC WWTS Georgia. Corrected by Gvantsa Amiridze (ACCA, Georgia))_

### PIT formula [T1]

- **PIT formula** — PIT = Gross salary × 20%  _(PwC WWTS Georgia, Corporate: Other taxes; Tax Code of Georgia)_
- **No allowances, no cap adjustment** — There is no GENERAL tax-free band, no standard deduction, and no marital/dependant adjustment for salary. But it is wrong to tell a taxpayer that no relief exists at all: Tax Code Article 82 grants specific personal exemptions to defined categories — for example individuals engaged in agricultural production, and certain protected categories, on taxable income up to GEL 3,000 / GEL 6,000 in a calendar year. Check Article 82 against the taxpayer's circumstances before concluding there is no relief.  _([Tax Code of Georgia Art. 82; rs.ge Persons Tax FAQ. Corrected by Gvantsa Amiridze (ACCA, Georgia)](https://rs.ge/PersonsTaxFAQ?cat=1&tab=1))_
- **PIT payment and declaration timing** — PIT payment is due on the day wages are paid; the monthly withholding declaration is filed by the 15th of the following month via rs.ge.  _(PwC WWTS Georgia, Tax administration; Tax Code)_

### Other PIT rates (context — NOT employment income) [T1 / informational]

**Other PIT rates table**

| Income type | Rate | Note | Source |
| --- | --- | --- | --- |
| Residential rental (individual, no deductions claimed) | 5% flat on gross | Optional; otherwise 20% on net. Not employment income. | PwC WWTS Georgia, Individual: Income determination |
| Small-business status individual entrepreneur | 1% of turnover (3% if standard turnover > GEL 500,000/yr; wine-tourism/agrotourism threshold is GEL 700,000) | Self-employed / IE regime, not employees. | PwC WWTS Georgia, Individual |
| Micro-business status individual | 0% (exempt) | Annual turnover < GEL 30,000, no employees. Not employment income. | PwC WWTS Georgia, Individual |

> These special regimes apply to **self-employed individuals**, not to employees. Do not apply them to a payroll computation. If a "salary" turns out to be IE turnover, this is [T3] — out of scope for payroll.

## Section 3 -- Funded Pension Contributions

- **Mandatory funded pension overview** — A mandatory funded pension has been in force since 1 January 2019. For each participating employee it is funded by three sources: the employer (2%), the employee (2%, withheld by the employer), and the State (a co-contribution on a sliding scale).  _(Law on Funded Pension Art. 3(6); PwC WWTS Georgia, Individual: Other taxes)_

### Funded pension rate table [T1]

**Funded pension rate table**

| Source | Rate | Base | Who pays / how | Source |
| --- | --- | --- | --- | --- |
| Employer | 2% | Employee gross salary | Employer, on top of gross | Law on Funded Pension Art. 3(6); PwC |
| Employee | 2% | Employee gross salary | Withheld from gross by employer | Law on Funded Pension Art. 3(6) |
| State co-contribution | 2% / 1% / 0% (see schedule) | Participant's **annual** income | Government of Georgia | Law on Funded Pension Art. 3(6) |
| **Combined employer + employee (private)** | **4%** | Gross salary | 2% employer + 2% employee | derived from Art. 3(6) |

- **Arithmetic check for private combined rate** — Arithmetic check: private contributions = employer 2% + employee 2% = 4% of gross. The State portion is paid by the Government and is not an employer or employee cost.  _([T1])_

### State co-contribution schedule [T1]

- **State co-contribution basis** — The State co-contribution is based on the participant's annual salary/income and is tiered. Thresholds reset each calendar year.  _(Law on Funded Pension Art. 3(6))_

**State co-contribution schedule table**  _(Law on Funded Pension Art. 3(6))_

| Annual income band (GEL) | State co-contribution rate |
| --- | --- |
| Up to 24,000 | 2% |
| Portion from 24,000 to 60,000 | 1% |
| Above 60,000 | 0% (no State contribution) |

**Arithmetic check (state co-contribution worked):** [T1]
- Annual income GEL 20,000 (< 24,000): 20,000 × 2% = **GEL 400/yr**.
- Annual income GEL 36,000: (24,000 × 2%) + (12,000 × 1%) = 480 + 120 = **GEL 600/yr**.
- Annual income GEL 70,000: (24,000 × 2%) + (36,000 × 1%) + (10,000 × 0%) = 480 + 360 + 0 = **GEL 840/yr** (the GEL 60,000+ portion gets 0%).

### Contribution base for the private 2% + 2% [T2]

> **[RESEARCH GAP — reviewer to confirm].** Authoritative sources confirm the GEL 24,000 / GEL 60,000 threshold schedule **only for the STATE co-contribution**. Whether the **employee/employer 2% base is itself capped** (e.g. at GEL 60,000) for very high earners, or computed on **full gross salary**, is not pinned to a primary source. **Conservative default (CD2):** compute the 2% + 2% on **full gross salary** unless verified otherwise. Verify cap treatment with the Pension Agency (pensions.ge) or the Law's implementing regulations before finalising payroll for high earners.

### Participation rules [T1]

- **Mandatory participation** — Participation is mandatory for employees.  _(Law on Funded Pension)_
- **Voluntary opt-out for pre-2019 60/55** — Voluntary opt-out is available only for those who had reached 60 (men) / 55 (women) before the law's entry into force (1 Jan 2019). For such persons participation is voluntary.  _(Law on Funded Pension; CD3)_
- **Self-employed pension contribution** — Self-employed individuals contribute 4% of annual income (no employer component, since there is no employer). (Self-employed is not payroll — see Section 6 refusal catalogue.)  _(PwC WWTS Georgia, Individual: Other taxes; Law on Funded Pension)_

## Section 4 -- Gross-to-Net Computation Order

- **Gross-to-net computation order** — 1.  Determine gross salary (khelfasi), in GEL. 2.  PIT = gross × 20%                              (withheld from gross). 3.  Employee funded pension = gross × 2%           (withheld from gross). 4.  Net pay = gross − PIT − employee pension = gross × (1 − 0.20 − 0.02) = gross × 0.78. 5.  Employer funded pension = gross × 2%           (paid on top of gross). 6.  Total employer cash cost = gross + employer pension = gross × 1.02. 7.  State co-contribution is added to the employee's pension account by the Government (per the Section 3 schedule); it is NOT an employer or employee cash cost.  _(PwC WWTS Georgia (PIT 20% withholding); Law on Funded Pension Art. 3(6) (2% + 2%))_
- **Arithmetic check multipliers** — Arithmetic check: net multiplier = 1 − 0.20 − 0.02 = 0.78; employer cost multiplier = 1 + 0.02 = 1.02.  _([T1])_
- **Pension-exempt employee computation** — For an employee who is exempt from the funded pension (60+/55+ before 1 Jan 2019 and has not opted in), drop the 2% lines: net = gross × 0.80; employer cost = gross (no employer pension).  _([T1])_

## Section 5 -- Conservative Defaults

**Conservative defaults table**  _(research conservative_defaults)_

| # | Default assumption | Rationale / source |
| --- | --- | --- |
| CD1 | Employer total statutory on-cost = **2% of gross** (the funded-pension employer share) — there is no other employer payroll/social tax in Georgia. | Georgia has no general employer social-security tax. PwC WWTS Georgia, Corporate. |
| CD2 | Compute the employee/employer 2% + 2% on **full gross salary**; do **not** assume a GEL 60,000 cap on the private share — the GEL 24,000/60,000 thresholds are confirmed only for the STATE co-contribution. Flag [T2]. | Threshold schedule confirmed for State portion only; private cap unverified. `[RESEARCH GAP]` |
| CD3 | Assume **mandatory enrolment** for the employee, except those aged 60+ (men) / 55+ (women) **before 1 Jan 2019**, for whom participation is voluntary. | Law on Funded Pension (mandatory participation). |
| CD4 | Treat the statutory **GEL 20/month** private-sector minimum wage as **non-binding**; use the agreed contractual salary as the payroll base. | The 1999 statutory minimum is obsolete and not enforced. CXC Global; wage.is. |
| CD5 | Treat the income as standard **employment income** (PAYE) unless told otherwise; do not apply small-business/micro-business/IE regimes to payroll. | Those regimes apply to self-employed individuals, not employees. PwC WWTS Georgia. |

## Section 6 -- Required Inputs and Refusal Catalogue

### Required inputs before computing any payroll [T1]

- **required inputs 1-4** — Ask for any unknown item. Do not compute until items 1--4 are confirmed. 1. Employer TIN (9- or 11-digit tax identification number) and registration with the Revenue Service. 2. Pay period and payment date (PIT is due on the payment date; the withholding declaration is filed by the 15th of the following month). 3. Gross salary for the period, in GEL. If only a net figure is known, flag for gross-up (iterative) and present as estimate only [T2]. 4. Funded-pension status of the employee: enrolled (mandatory) or exempt/opted-out under the 60/55 pre-2019 rule (CD3) [T2 if unclear].

### Refusal Catalogue [T1]

**Refusal catalogue table**

| Trigger | Action |
| --- | --- |
| Request concerns the **US state of Georgia** (USD, Form G-7, state withholding) | STOP. Wrong jurisdiction. This skill is the COUNTRY of Georgia (GEL). Escalate to the correct US-state skill [T3]. |
| Gross salary not provided (only "net" or "budget") | Gross-up required (gross = net / 0.78 for an enrolled employee; / 0.80 if pension-exempt). Present as estimate only and flag [T2]. |
| Payment date / pay period unknown | STOP. Declaration timing depends on the payment date. |
| Worker is a **self-employed individual / individual entrepreneur** (small-business 1%/3%, micro-business 0%, or 4% self-employed pension) | OUT OF SCOPE for payroll. Escalate to the relevant Georgia skill / adviser [T3]. |
| Income is **not employment income** (dividends, interest, rent, services) | OUT OF SCOPE for this skill. The 5% rental rate, withholding on dividends/interest etc. are separate [T3]. |
| Funded-pension cap treatment for a **high earner** materially affects the result | Apply CD2 (full gross), flag [T2] / `[RESEARCH GAP]`, and require Pension Agency confirmation. |

## Section 7 -- Transaction / Payment Pattern Library (Deterministic)

Map bank-statement narrations (often Georgian / transliterated) to payroll classifications. All patterns [T1] unless flagged. Georgian banks: TBC Bank, Bank of Georgia, Liberty Bank, Basis Bank, Credo Bank, ProCredit Georgia.

### 7a. Salary credits to the employee's account

**Salary credits table**

| Narration pattern (Georgian / common) | Classification |
| --- | --- |
| KHELFASI, ხელფასი | Net salary payment |
| KHELFASI [month/year], MONTHLY SALARY | Net monthly salary |
| ANAZGHAUREBA, AREMUNERATSIA, REMUNERATION | Salary / remuneration |
| AVANSI, SALARY ADVANCE | Salary advance — partial net payment [T2] |
| PREMIA, BONUS | Bonus — taxable as employment income (20% PIT + 2% pension apply) [T1] |

### 7b. Employer remittances (debits from the company account)

**Employer remittances table**

| Narration pattern | Classification |
| --- | --- |
| REVENUE SERVICE, RS.GE, SASIMOSAVLO SAMSAKHURI | PIT withholding remittance to the Revenue Service |
| GADASAKHADI, TAX PAYMENT | Tax payment (PIT) |
| SAPENSIO, PENSION AGENCY, PENSIONS.GE | Funded pension transfer (employer 2% + withheld employee 2%) |
| DAGROVEBITI SAPENSIO | Funded ("accumulated") pension contribution |
| KHELFASEBI, PAYROLL, NET WAGES | Net salary disbursement to employees |

> Salaries, PIT and pension contributions are **never** items on a VAT (VAT/DAANG) return — keep them out of georgia-vat. Source: georgia-vat.md Section 3.8 (KHELFASI / salary = EXCLUDE).

### Forms [T1]

**Forms table**

| Form | Purpose | Deadline | Portal | Source |
| --- | --- | --- | --- | --- |
| **Monthly withholding (PIT) declaration** | Employer reports PIT withheld on salaries (and other withholding — dividends, interest, services) | By the **15th** of the month following the payment month; **PIT payment due on the day wages are paid** | rs.ge / eservices.rs.ge | PwC WWTS Georgia, Tax administration; TPsolution; expathub.ge |
| **Funded pension contribution** | Employer transfers employer 2% + withheld employee 2% to the Pension Agency | Monthly, alongside payroll (Pension Agency / Revenue Service systems) | Pension Agency systems | Law on Funded Pension; PwC |
| **Annual individual income tax declaration** | Resident individuals whose income was **not** taxed at source must file | Before **1 April** for the prior calendar year | rs.ge | PwC WWTS Georgia, Tax administration |

## Section 8 -- Filing Obligations

> **[RESEARCH GAP — reviewer to confirm]** the exact monthly mechanics/timing for remitting funded-pension contributions to the Pension Agency versus filing the PIT declaration on rs.ge. The two are processed through parallel systems; confirm operational sequencing. Source: research caveat (3).

> For an employee whose salary is fully taxed at source (PAYE), **no annual return** is generally required — the annual return is for individuals with income **not** taxed at source. [T1]

## Section 9 -- Minimum Wage

**Minimum wage table**

| Item | Value | Source |
| --- | --- | --- |
| Private-sector statutory minimum | GEL 20/month (Presidential Decree No. 351 of 1999, unchanged) | CXC Global; wage.is |
| Public-sector minimum | ~GEL 115/month | CXC Global |
| Practical position | The 1999 statutory minimum is **non-binding** in practice; the de facto market floor is far higher. Payroll is based on the **contractual salary**. | CXC Global; CD4 |

Georgia's statutory minimum wage is functionally obsolete. Source: CXC Global; wage.is.

> **Do not** treat GEL 20/month as a meaningful wage floor (CD4). Use the agreed contractual salary as the payroll base.

## Section 10 -- Worked Examples

All figures in GEL. Each example is recomputed end-to-end. Unless stated, the employee is **enrolled** in the funded pension (net = gross × 0.78; employer cost = gross × 1.02).

### Example 1 -- Standard salary, GEL 2,000 gross, enrolled [T1]

- PIT = 2,000 × 20% = **400.00**
- Employee funded pension = 2,000 × 2% = **40.00**
- **Net pay = 2,000 − 400.00 − 40.00 = 1,560.00** (= 2,000 × 0.78) ✓
- Employer funded pension = 2,000 × 2% = **40.00**
- **Total employer cost = 2,000 + 40.00 = 2,040.00** (= 2,000 × 1.02) ✓

Bank statement: a credit of GEL 1,560.00 narrated `KHELFASI 03/2025`.

### Example 2 -- Mid salary, GEL 3,500 gross, enrolled [T1]

- PIT = 3,500 × 20% = **700.00**
- Employee funded pension = 3,500 × 2% = **70.00**
- **Net pay = 3,500 − 700.00 − 70.00 = 2,730.00** (= 3,500 × 0.78) ✓
- Employer funded pension = 3,500 × 2% = **70.00**
- **Total employer cost = 3,570.00** (= 3,500 × 1.02) ✓

### Example 3 -- Low salary, GEL 1,000 gross, enrolled [T1]

- PIT = 1,000 × 20% = **200.00**
- Employee funded pension = 1,000 × 2% = **20.00**
- **Net pay = 1,000 − 200.00 − 20.00 = 780.00** (= 1,000 × 0.78) ✓
- Employer funded pension = 1,000 × 2% = **20.00**
- **Total employer cost = 1,020.00** ✓

> Note: there is no **general** tax-free allowance — PIT applies from the first lari of salary. But Tax Code Art. 82 grants specific exemptions to defined categories (e.g. agricultural production; certain categories up to GEL 3,000 / GEL 6,000 a year) — check it before telling a taxpayer no relief exists. [T1]

### Example 4 -- High salary, GEL 8,000 gross/month, enrolled [T1] / [T2]

- PIT = 8,000 × 20% = **1,600.00**
- Employee funded pension (CD2: full gross) = 8,000 × 2% = **160.00**
- **Net pay = 8,000 − 1,600.00 − 160.00 = 6,240.00** (= 8,000 × 0.78) ✓
- Employer funded pension = 8,000 × 2% = **160.00**
- **Total employer cost = 8,160.00** (= 8,000 × 1.02) ✓

> **[T2] / [RESEARCH GAP].** Annualised, GEL 8,000/month = GEL 96,000/yr, which is above GEL 60,000. The **State** co-contribution would be **0%** on the portion above GEL 60,000. Whether the **private 2% + 2%** is itself capped at GEL 60,000 of annual salary is unconfirmed — CD2 computes on full gross; confirm with the Pension Agency. Source: research caveat (1).

### Example 5 -- Pension-exempt employee (60+/55+ before 1 Jan 2019), GEL 2,500 gross [T1]

- Employee is **exempt** from the funded pension and has not opted in (CD3). Drop both 2% lines.
- PIT = 2,500 × 20% = **500.00**
- Employee funded pension = **0.00**
- **Net pay = 2,500 − 500.00 = 2,000.00** (= 2,500 × 0.80) ✓
- Employer funded pension = **0.00**
- **Total employer cost = 2,500.00** (no employer pension) ✓

### Example 6 -- State co-contribution illustration (not a cash cost), annual GEL 36,000 [T1]

For an enrolled employee earning GEL 3,000/month (= GEL 36,000/yr):

- Employee contributes 36,000 × 2% = GEL 720/yr; employer contributes 36,000 × 2% = GEL 720/yr (CD2, full gross).
- **State** co-contribution = (24,000 × 2%) + (12,000 × 1%) = 480 + 120 = **GEL 600/yr** (paid by the Government to the employee's pension account).
- Total annual additions to the pension account ≈ 720 + 720 + 600 = **GEL 2,040** — but only the GEL 720 employer share is an **employer cash cost**, and only the GEL 720 employee share is **withheld from net pay**. The State GEL 600 is neither. [T1]

## Section 11 -- Tier 1 Rules (Deterministic)

**Tier 1 Rules table**

| # | Rule | Source |
| --- | --- | --- |
| T1-1 | PIT on salary is a **flat 20%** of gross, withheld at source (PAYE). No tax-free allowance, no progressive bands, no marital/dependant adjustment. | PwC WWTS Georgia, Corporate: Other taxes; Tax Code |
| T1-2 | PIT payment is due on the **day wages are paid**; the monthly withholding declaration is filed by the **15th** of the following month via rs.ge. | PwC WWTS Georgia, Tax administration; TPsolution |
| T1-3 | Mandatory funded pension: **employer 2% + employee 2%** of gross salary, in force since 1 Jan 2019; employee 2% is withheld, employer 2% is on top of gross. | Law on Funded Pension Art. 3(6) |
| T1-4 | **State** co-contribution: 2% if annual income < GEL 24,000; 1% on the GEL 24,000--60,000 portion; 0% above GEL 60,000; thresholds reset each calendar year. Paid by the Government, not the employer. | Law on Funded Pension Art. 3(6) |
| T1-5 | Net pay = gross × 0.78 for an enrolled employee (gross × 0.80 if pension-exempt). Total employer cash cost = gross × 1.02 (gross × 1.00 if pension-exempt). | derived from T1-1 + T1-3 |
| T1-6 | There is **no general employer social-security or payroll tax** beyond the 2% funded pension — total mandatory employer on-cost is just 2%. | PwC WWTS Georgia, Corporate: Other taxes |
| T1-7 | Funded-pension participation is **mandatory** for employees; voluntary opt-out only for those aged 60 (men) / 55 (women) before 1 Jan 2019. | Law on Funded Pension |
| T1-8 | The tax year is the **calendar year**. Resident individuals whose income was NOT taxed at source must file an annual PIT declaration before **1 April**. | PwC WWTS Georgia, Tax administration |
| T1-9 | Self-employed individuals contribute **4%** of annual income to the funded pension (no employer component). Not payroll. | PwC WWTS Georgia, Individual: Other taxes |

### Context rates (for cross-skill reference; not payroll) [T1]

**Context rates table**

| Item | Rate / value | Source |
| --- | --- | --- |
| Standard VAT | 18% | PwC WWTS Georgia, Corporate: Other taxes; see georgia-vat.md |
| VAT mandatory registration threshold | GEL 100,000 turnover in any continuous 12-month period | PwC WWTS Georgia, Corporate: Other taxes |
| Optional rental PIT (individual, no deductions) | 5% on gross residential rent | PwC WWTS Georgia, Individual: Income determination |
| Small-business status IE | 1% of turnover (3% if standard turnover > GEL 500,000/yr; wine-tourism/agrotourism threshold is GEL 700,000) | PwC WWTS Georgia, Individual |
| Micro-business status individual | 0% (turnover < GEL 30,000, no employees) | PwC WWTS Georgia, Individual |

## Section 12 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 catalogue table**

| # | Situation | Why it needs judgement | Action |
| --- | --- | --- | --- |
| T2-1 | High earner — private 2% + 2% cap treatment | GEL 24,000/60,000 thresholds confirmed only for the **State** portion; private cap unverified | Apply CD2 (full gross); flag `[RESEARCH GAP]`; confirm with Pension Agency. |
| T2-2 | Employee may qualify for the 60/55 pre-2019 pension opt-out | Eligibility depends on age at 1 Jan 2019 and whether they opted in | Confirm date of birth and election before dropping the 2% lines. |
| T2-3 | Net-to-gross gross-up requested | Iterative; rounding-sensitive (gross = net / 0.78 or / 0.80) | Present as estimate; flag for adviser. |
| T2-4 | Bonus / non-cash benefit / benefit-in-kind | Taxability and pension base may vary | Default: treat cash bonus as salary (20% + pension); flag non-cash items [T2]. |
| T2-5 | Worker may be self-employed / IE rather than an employee | Wrong regime entirely (1%/3%/0% turnover tax, 4% pension) | Escalate [T3] — out of payroll scope. |
| T2-6 | Non-resident / posted / cross-border employee | Residency, treaty and social-security coordination apply | Escalate [T3] — outside payroll scope. |
| T2-7 | Exact penalty amounts / Tax Code article numbers | Penalty figures are periodically amended; sourced from a practitioner summary | Cross-check against the consolidated Tax Code on matsne.gov.ge before relying. `[RESEARCH GAP]` |

## Section 13 -- Excel Working Paper Template

**Excel working paper template table**

| Cell ref | Label | Formula / source |
| --- | --- | --- |
| B1 | Pay period (month/year) | input |
| B2 | Payment date | input — drives declaration timing |
| B3 | Gross salary (khelfasi) | input |
| B4 | Pension-enrolled? (1 = yes, 0 = exempt) | input (CD3) |
| B5 | PIT (20%) | `=ROUND(B3*0.20,2)` |
| B6 | Employee funded pension (2%) | `=ROUND(B3*0.02*B4,2)` |
| B7 | **Net pay** | `=B3-B5-B6` |
| B8 | Employer funded pension (2%) | `=ROUND(B3*0.02*B4,2)` |
| B9 | **Total employer cost** | `=B3+B8` |
| B10 | Total to remit (PIT + employee pension + employer pension) | `=B5+B6+B8` |
| B11 | Memo: State co-contribution (annual, informational) | per Section 3 schedule on annualised salary — NOT a cash cost |

Suggested layout for a single-employee monthly payroll working paper. GEL throughout.

Validation rows: confirm B7 = B3 × 0.78 when B4 = 1 (B3 × 0.80 when B4 = 0); confirm B7 + B5 + B6 = B3; confirm B9 = B3 × 1.02 when B4 = 1.

## Section 14 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide table**

| Georgian term (transliterated) | English | Notes |
| --- | --- | --- |
| khelfasi (ხელფასი) | salary / wage | gross unless context says net |
| anazghaureba | remuneration / pay | salary |
| avansi | advance / instalment | partial salary payment |
| premia | bonus / premium | taxable as employment income |
| sashemosavlo gadasakhadi | income tax | the 20% PIT |
| dagrovebiti sapensio | funded ("accumulated") pension | the 2% + 2% scheme |
| sapensio saagento | Pension Agency | pensions.ge |
| shemosavlebis samsakhuri | Revenue Service | rs.ge |
| TIN | taxpayer identification number | 9 or 11 digits |
| naghdi | cash | cash withdrawal — exclude from payroll classification |
| shida gadaritskhva | internal transfer | between client's own accounts — exclude |

Georgian payroll bank narrations and key terms:

**Conventions.** TBC Bank and Bank of Georgia export CSV with semicolons or commas; dates DD.MM.YYYY or ISO depending on setting. Convert foreign-currency salaries to GEL at the National Bank of Georgia (nbg.gov.ge) rate on the relevant date.

## Section 15 -- Onboarding Fallback

If the engagement is mid-year or records are incomplete:

1. **No prior withholding declarations on hand** → request the rs.ge declaration history; reconcile each month's PIT against bank remittances to the Revenue Service. Do not assume prior months were correct.
2. **Net-only history** → reconstruct gross via the gross-to-net order (Section 4): gross = net / 0.78 (enrolled) or net / 0.80 (pension-exempt), iterating for rounding; mark all reconstructed grosses as estimates [T2].
3. **Pension-enrolment status unknown** → default to **enrolled** (CD3) unless the employee was 60+/55+ before 1 Jan 2019; confirm before dropping the 2% lines.
4. **Worker type unclear (employee vs IE/self-employed)** → STOP and confirm; the IE/self-employed regimes are out of payroll scope [T3].
5. **High-earner pension cap uncertainty** → apply CD2 (full gross), flag [T2]/`[RESEARCH GAP]`, and ask the adviser to confirm with the Pension Agency.

## Section 16 -- Reference Material

**Reference material table**

| Item | Value | Source |
| --- | --- | --- |
| PIT (salary) rate | 20% flat on gross; no allowance | PwC WWTS Georgia, Corporate: Other taxes |
| Funded pension — employer | 2% of gross | Law on Funded Pension Art. 3(6); PwC |
| Funded pension — employee (withheld) | 2% of gross | Law on Funded Pension Art. 3(6) |
| Funded pension — State | 2% (< GEL 24,000) / 1% (24,000--60,000) / 0% (> 60,000), annual | Law on Funded Pension Art. 3(6) |
| Self-employed funded pension | 4% of annual income | PwC WWTS Georgia, Individual: Other taxes |
| Net pay multiplier (enrolled / exempt) | 0.78 / 0.80 | derived |
| Employer cost multiplier (enrolled / exempt) | 1.02 / 1.00 | derived |
| Monthly withholding declaration deadline | 15th of following month; PIT due on payment day | PwC WWTS Georgia, Tax administration; TPsolution |
| Annual individual return deadline | Before 1 April (income not taxed at source) | PwC WWTS Georgia, Tax administration |
| Tax year | Calendar year | PwC WWTS Georgia, Tax administration |
| Standard VAT / registration threshold | 18% / GEL 100,000 in any 12 months | PwC WWTS Georgia, Corporate: Other taxes |
| Small-business status cap | GEL 500,000 standard annual turnover (1%, 3% above); GEL 700,000 for wine tourism / agrotourism | PwC WWTS Georgia, Individual |
| Micro-business status cap | GEL 30,000 annual turnover, no employees (0%) | PwC WWTS Georgia, Individual |
| Private-sector statutory minimum wage | GEL 20/month (1999; obsolete/non-binding) | CXC Global; wage.is |

### Penalties [T2]

**Penalties table**

| Violation | Amount / rate | Source |
| --- | --- | --- |
| Failure to submit a required (marked) tax declaration | GEL 100 per month per declaration (even a nil declaration) | Tax Code of Georgia (Art. ~274); TPsolution; countman.ge — `[RESEARCH GAP]` |
| Understatement / unpaid tax penalty | up to 50% of the principal unpaid/understated tax | Tax Code of Georgia (Art. ~275); TPsolution — `[RESEARCH GAP]` |
| Late-payment interest | 0.05% of unpaid tax per day of delay | Tax Code of Georgia (Art. ~272); TPsolution — `[RESEARCH GAP]` |

> **[RESEARCH GAP — reviewer to confirm].** Figures below are from a Georgian practitioner source (TPsolution) and should be cross-checked against the consolidated Tax Code on matsne.gov.ge, as penalty figures are periodically amended (article numbers are approximate). Source: research caveat (2).

### Authorities and legislation

- **Revenue Service of Georgia** — Revenue Service of Georgia (Sakartvelos Shemosavlebis Samsakhuri), Ministry of Finance — rs.ge; e-services eservices.rs.ge.  _(rs.ge)_
- **LEPL Pension Agency** — LEPL Pension Agency — pensions.ge.  _(pensions.ge)_
- **Tax Code of Georgia** — Tax Code of Georgia (Law No. 3591, 2010, as amended) — PIT withholding, declarations, penalties.  _(matsne.gov.ge)_
- **Law of Georgia On Funded Pension** — Law of Georgia "On Funded Pension" (2018; in force 1 Jan 2019) — mandatory funded pension.  _(matsne.gov.ge)_

### Sources

1. PwC Worldwide Tax Summaries — Georgia, Individual: Taxes on personal income. https://taxsummaries.pwc.com/georgia/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Georgia, Individual: Other taxes (funded pension contributions). https://taxsummaries.pwc.com/georgia/individual/other-taxes
3. PwC Worldwide Tax Summaries — Georgia, Individual: Tax administration. https://taxsummaries.pwc.com/georgia/individual/tax-administration
4. PwC Worldwide Tax Summaries — Georgia, Corporate: Other taxes (VAT; payroll PIT withholding 20%). https://taxsummaries.pwc.com/georgia/corporate/other-taxes
5. Law of Georgia "On Funded Pension" — Legislative Herald of Georgia. https://www.matsne.gov.ge/en/document/view/4280127
6. Tax Code of Georgia — Legislative Herald of Georgia. https://matsne.gov.ge/en/document/view/1043717
7. Mondaq (Eurofast) — "Georgia's Pension Evolution: From Mandatory Participation to Tailored Investment Strategies." https://www.mondaq.com/employee-benefits-compensation/1433340/georgias-pension-evolution-from-mandatory-participation-to-tailored-investment-strategies
8. TPsolution — "Monthly and Annual Tax Reporting Obligations in Georgia." https://tpsolution.ge/tax-reporting-obligations-in-georgia/
9. CXC Global — "Payroll and benefits in Georgia" (minimum wage). https://www.cxcglobal.com/global-hiring-guide/georgia/payroll-and-benefits-in-georgia/

> **Reviewer note on tax year / 2026.** No 2026-specific changes were confirmed; figures reflect 2025 and were current as of the PwC review dated 21 Jan 2026. Re-confirm before applying to a 2026 payroll. Source: research caveat (4).

## Section 17 -- Test Suite

Each test states inputs and the recomputed expected output. Reviewers should rerun every figure. All amounts in GEL. "Enrolled" means net = gross × 0.78, employer cost = gross × 1.02.

### Test 1 -- Standard salary, enrolled

**Input:** Gross GEL 2,000, paid March 2025, enrolled.
**Expected:** PIT 400.00. Employee pension 40.00. **Net 1,560.00.** Employer pension 40.00. **Total employer cost 2,040.00.** Total to remit 480.00.

### Test 2 -- Mid salary, enrolled

**Input:** Gross GEL 3,500, paid June 2025, enrolled.
**Expected:** PIT 700.00. Employee pension 70.00. **Net 2,730.00.** Employer pension 70.00. **Total employer cost 3,570.00.** Total to remit 840.00.

### Test 3 -- Low salary, enrolled

**Input:** Gross GEL 1,000, paid May 2025, enrolled.
**Expected:** PIT 200.00 (no tax-free allowance). Employee pension 20.00. **Net 780.00.** Employer pension 20.00. **Total employer cost 1,020.00.** Total to remit 240.00.

### Test 4 -- High salary, enrolled [T2]

**Input:** Gross GEL 8,000/month (GEL 96,000/yr), paid April 2025, enrolled, CD2 full-gross pension base.
**Expected:** PIT 1,600.00. Employee pension 160.00. **Net 6,240.00.** Employer pension 160.00. **Total employer cost 8,160.00.** Flag: private 2%+2% cap above GEL 60,000 unconfirmed `[RESEARCH GAP]`; State co-contribution 0% above GEL 60,000.

### Test 5 -- Pension-exempt employee (60+/55+ before 1 Jan 2019)

**Input:** Gross GEL 2,500, not enrolled (CD3 exemption).
**Expected:** PIT 500.00. Employee pension 0.00. **Net 2,000.00** (= 2,500 × 0.80). Employer pension 0.00. **Total employer cost 2,500.00.** Total to remit 500.00.

### Test 6 -- State co-contribution band check (annual)

**Input:** Annual salary GEL 36,000, enrolled.
**Expected:** State co-contribution = (24,000 × 2%) + (12,000 × 1%) = **GEL 600/yr** (Government-paid, not a cash cost). Employee/employer private share = 36,000 × 2% = GEL 720/yr each (CD2).

### Test 7 -- State co-contribution above GEL 60,000

**Input:** Annual salary GEL 70,000, enrolled.
**Expected:** State co-contribution = (24,000 × 2%) + (36,000 × 1%) + (10,000 × 0%) = 480 + 360 = **GEL 840/yr**; the portion above GEL 60,000 attracts 0% State contribution.

### Test 8 -- Wrong jurisdiction guard

**Input:** Request references "Georgia Form G-7" / USD state withholding.
**Expected:** REFUSE — this is the US state of Georgia, not the Republic of Georgia (GE/GEL). Escalate to the correct US-state skill [T3].

## PROHIBITIONS

- NEVER confuse the **country of Georgia (GE, GEL, lari)** with the **US state of Georgia (USD)** — the US state's rates and forms (e.g. Form G-7) must NOT appear in this skill.
- NEVER apply a tax-free personal allowance or progressive bands to Georgian salary PIT — it is a **flat 20%** from the first lari.
- NEVER add an employer social-security or payroll tax beyond the **2% funded pension** — there is no other employer on-cost in Georgia.
- NEVER drop the funded-pension 2% + 2% for an employee unless they qualify for the 60/55 pre-2019 opt-out (CD3) — participation is otherwise mandatory.
- NEVER assume the private employee/employer 2% is capped at GEL 60,000 — that schedule is confirmed only for the STATE co-contribution; apply CD2 (full gross) and flag `[RESEARCH GAP]`.
- NEVER treat the State co-contribution as an employer or employee cash cost — it is paid by the Government.
- NEVER apply the small-business (1%/3%), micro-business (0%) or 4% self-employed pension regimes to an employee's payroll — those are self-employed/IE regimes [T3].
- NEVER treat the obsolete GEL 20/month statutory minimum wage as a binding floor — use the contractual salary (CD4).
- NEVER miss the monthly withholding declaration (15th of the following month) or the on-payment-date PIT payment.
- NEVER guess any figure marked `[RESEARCH GAP — reviewer to confirm]` — verify against matsne.gov.ge / the Pension Agency.
- NEVER present payroll computations as definitive — always label as estimated and direct to a qualified Georgian tax adviser / authorised accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Georgian tax adviser or authorised accountant in Georgia) before implementation.

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
