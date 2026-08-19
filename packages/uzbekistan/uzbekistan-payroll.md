---
name: uzbekistan-payroll
description: "Use this skill whenever asked about Uzbekistan (the Republic of Uzbekistan — Oʻzbekiston, Central Asia) payroll processing for employed persons. Trigger on phrases like \"Uzbekistan payroll\", \"Uzbek payroll\", \"ish haqi\", \"oylik maosh\", \"salary tax Uzbekistan\", \"PIT withholding Uzbekistan\", \"12% income tax Uzbekistan\", \"PAYE Uzbekistan\", \"social tax Uzbekistan\", \"ijtimoiy soliq\", \"INPS Uzbekistan\", \"individual accumulative pension fund\", \"soliq.uz payroll\", \"my.soliq.uz\", \"State Tax Committee Uzbekistan\", \"monthly payroll report Uzbekistan\", \"net salary Uzbekistan\", \"gross to net Uzbekistan\", \"employer cost Uzbekistan\", \"minimum wage Uzbekistan\", \"BCV Uzbekistan\", \"base calculation value\", or any question about computing employee pay, salary withholding tax (PIT), or employer social tax for Uzbekistan-based employees. This skill covers the flat 12% personal income tax withheld at source (the employer is the tax agent), the 12% employer Social Tax (Ijtimoiy soliq), the 0.1% employee INPS pension contribution carved out of PIT, the cumulative monthly withholding method, the monthly payroll report on my.soliq.uz, the minimum wage and Base Calculation Value (BCV), and penalties. CRITICAL: jurisdiction code UZ is the country of Uzbekistan (currency UZS, soʻm) and figures are anchored to PwC Worldwide Tax Summaries (reviewed 16 Jan 2026) and the EY Jan-2026 tax alert. ALWAYS read this skill before processing any Uzbekistan payroll."
version: 0.1
jurisdiction: UZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uzbekistan Payroll

## Uzbekistan Payroll Skill v0.1

> **Tier 2 — Research-verified.** Rates and structure are cross-verified across PwC Worldwide Tax Summaries (Uzbekistan, Individual & Corporate; reviewed 16 Jan 2026), the EY Global Tax Alert "Uzbekistan: tax updates effective from 2026" (Jan 2026), LegalAct.uz (PIT cumulative method and the 0.1% INPS carve-out), WageIndicator (minimum wage from 1 Aug 2025) and EOR practitioner guides (Asanify). The official primary sources — the Tax Code of the Republic of Uzbekistan (Soliq kodeksi) and soliq.uz — were not directly text-extracted line-by-line; figures rely on the Big-4 / specialist English summaries. Every figure below carries an inline source or a `[RESEARCH GAP — reviewer to confirm]` marker. A qualified Uzbek tax adviser / licensed accountant must validate this skill before production use. **Confidence: medium.**

> **CRITICAL DISAMBIGUATION.** Jurisdiction code **UZ = the Republic of Uzbekistan (Oʻzbekiston, Central Asia), currency UZS (Uzbek soʻm)**. Do not confuse with neighbouring CIS payrolls (Kazakhstan KZT, Azerbaijan AZN, Tajikistan TJS, etc.) — their rates and forms differ and must NOT appear in this skill.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Uzbekistan (Oʻzbekiston — Central Asia) |
| Jurisdiction code | UZ |
| Currency | UZS (Uzbek soʻm) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December). Source: PwC WWTS Uzbekistan, Individual: Tax administration. |
| Has personal income tax? | Yes -- **flat 12%** on gross employment income, withheld at source; the employer is the tax agent. Source: PwC WWTS Uzbekistan, Individual: Taxes on personal income. |
| Personal income tax (salary) | 12% flat on gross employment income (residents and, post-reform, non-resident employment income). **No progressive bands since the 2019 reform.** Source: PwC WWTS Uzbekistan. |
| Employer Social Tax (Ijtimoiy soliq) — standard | 12% of total gross payroll (local and expatriate staff); **employer cost, not withheld from the employee**. Source: PwC WWTS Uzbekistan, Corporate: Other taxes. |
| Employer Social Tax — budget (state-financed) organisations | 25% of gross payroll. Source: PwC WWTS Uzbekistan, Individual: Other taxes. |
| Employee INPS pension (accumulative) | 0.1% of gross salary, **carved out of the 12% PIT** (not an additional charge). Source: LegalAct.uz. |
| Other employer payroll tax | **None** beyond the Social Tax (no separate employer health/unemployment levy at standard commercial rates). Source: PwC WWTS Uzbekistan, Corporate: Other taxes. |
| Tax authority | State Tax Committee of the Republic of Uzbekistan (Davlat soliq qoʻmitasi) — soliq.uz |
| Pension administrator | Pension Fund (reported through the State Tax Committee) |
| Filing portal | my.soliq.uz (e-filing) |
| Primary form | Monthly payroll / withholding report (PIT + Social Tax); annual individual income tax declaration where required |
| Monthly report deadline | By the **15th** of the month following the reporting month; tax and contributions paid by the same date. Source: Asanify EOR guide; `[RESEARCH GAP]` — confirm official form designation. |
| Validated by | Pending -- requires sign-off by a qualified Uzbek tax adviser / licensed accountant |
| Skill version | 0.1 |

**Legislation**

| Law | Scope | Source |
| --- | --- | --- |
| Tax Code of the Republic of Uzbekistan (Soliq kodeksi), as amended for 2025 | PIT, Social Tax, withholding, declarations, penalties | PwC WWTS Uzbekistan; soliq.uz |
| Presidential Decree No. UP-97 (2025) | Minimum wage and Base Calculation Value (BCV) from 1 Aug 2025 | WageIndicator; PwC WWTS Uzbekistan, Significant developments |
| Annual budget / tax-policy amendment laws; EY 2026 alert | 2026 changes (IE fixed-PIT regime cancelled; 1% turnover tax) | EY Global Tax Alert, Jan 2026 |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified Uzbek tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate and document the gap.

## Section 2 -- Personal Income Tax (PIT) Withholding -- the Employer as Tax Agent

- **PIT flat rate and employer as tax agent** — Employment income is taxed at a flat 12% of gross salary. The employer acts as the tax agent, withholds PIT at source at the moment of salary payment, and remits it to the State Tax Committee. There has been no progressive band since the 2019 reform — the rate is a single flat 12%.  _(PwC WWTS Uzbekistan, Individual: Taxes on personal income.)_
- **PIT formula [T1]** — PIT = PIT base × 12%  _(PwC WWTS Uzbekistan; LegalAct.uz)_
- **PIT base and BCV deduction eligibility** — For a standard payroll, the PIT base is gross employment income. A monthly 1× BCV personal deduction is available only to specified categories of employee (e.g. certain low-income / benefit-eligible employees) — it is not universal. Do not apply the deduction to a generic payroll without confirming eligibility. See CD6 / [RESEARCH GAP].  _(PwC WWTS Uzbekistan; LegalAct.uz)_
- **INPS carve-out effect on net pay** — The 0.1% INPS pension contribution is carved OUT of the 12% PIT (Section 3) — it does not reduce net pay below gross × 0.88 and is not an additional charge. [T1]
- **Cumulative monthly PIT computation** — PIT is computed on a cumulative (year-to-date) monthly basis: PIT for the month = PIT(Jan→current month) − PIT(Jan→previous month). For a flat 12% with a constant monthly salary and no deduction, this reduces to a simple monthly gross × 12%. The cumulative method matters when salary varies month to month or when the BCV deduction applies.  _(LegalAct.uz)_

### Non-employment / context PIT rates (NOT salary) [T1 / informational]

**Non-employment / context PIT rates table**  _(PwC WWTS Uzbekistan, Individual)_

| Income type | Rate | Note | Source |
| --- | --- | --- | --- |
| Resident employment income | **12%** | The standard payroll rate (this skill). | PwC WWTS Uzbekistan, Individual |
| Non-resident employment income | **12%** | Reduced from the former 20% on Uzbek-source income of non-residents (except dividends/interest/freight). Verify treaty relief for genuine non-residents [T2]. | PwC WWTS Uzbekistan, Individual |
| Resident dividends and interest | 5% | Not employment income. JSC share dividends PIT-exempt for residents & non-residents 1 Apr 2022–31 Dec 2028. | PwC WWTS Uzbekistan, Individual |
| Non-resident dividends and interest | 10% | Not employment income. | PwC WWTS Uzbekistan, Individual |
| Non-resident transportation / freight services | 6% | Not employment income. | PwC WWTS Uzbekistan, Individual |

> These special rates apply to **investment / non-employment income** or to non-residents. Do not apply them to a standard salary computation. If a "salary" turns out to be a dividend, freight payment or IE turnover, this is [T3] — out of payroll scope.

## Section 3 -- Social Tax (Ijtimoiy soliq) and the INPS Pension

Uzbekistan has two distinct payroll levies in addition to PIT:

1. **Employer Social Tax (Ijtimoiy soliq)** — paid by the employer, on top of gross payroll. It is not withheld from the employee.
2. **Employee INPS contribution** (Individual Accumulative Pension Fund) — 0.1% of gross, but carved OUT of the 12% PIT, so it is not an additional employee cost.

### 3a. Employer Social Tax rate table [T1]

**Employer Social Tax rate table**  _(PwC WWTS Uzbekistan, Corporate: Other taxes)_

| Payer / case | Rate | Base | Source |
| --- | --- | --- | --- |
| **Standard commercial entity** | **12%** | Total gross payroll (local + expatriate staff) | PwC WWTS Uzbekistan, Corporate: Other taxes |
| Budget (state-financed) organisation | 25% | Gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| Specialised workshops employing persons with disabilities | 4.7% | Gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| "SOS Children's Villages of Uzbekistan" association | 7% | Gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| Temporary 1% reduced rate (specified sectors/cases — see below) | 1% | Gross payroll | PwC WWTS Uzbekistan, Corporate: Other taxes; EY 2026 alert |

- **Social Tax is an employer cost** — Social Tax is an employer cost — it does not appear on the employee's payslip as a deduction and does not reduce net pay. [T1]
- **No upper ceiling; minimum wage base** — There is no upper ceiling. In practice, where wages are below the statutory minimum wage, Social Tax is computed on at least the minimum wage per employee (CD4 / [RESEARCH GAP]). [T2]

#### Temporary 1% Social Tax — qualifying cases [T2]

**Temporary 1% Social Tax qualifying cases table**  _(PwC WWTS Uzbekistan, Corporate: Other taxes; EY 2026 alert)_

| Case | Window |
| --- | --- |
| Employers of low-income staff earning > 1.5× minimum wage | 1 Jan 2025 – 1 Jan 2028 |
| Employers of students under 30 in vocational training | 1 Sep 2024 – 1 Sep 2027 |
| Qualifying greenhouse farms | per statute `[RESEARCH GAP]` |
| Cotton-textile / knitwear / garment clusters | per statute `[RESEARCH GAP]` |
| Fruit / vegetable sellers | per statute `[RESEARCH GAP]` |
| Children's-content producers | per statute `[RESEARCH GAP]` |

### 3b. Employee INPS pension (0.1%, carved out of PIT) [T1]

**INPS pension table**  _(LegalAct.uz)_

| Item | Value | Source |
| --- | --- | --- |
| INPS contribution rate | **0.1%** of gross salary | LegalAct.uz |
| Funded from | **Out of the calculated 12% PIT** — it reduces the PIT remitted to budget and is redirected to the employee's individual pension account | LegalAct.uz |
| Additional cost to employee? | **No** — it is part of the 12%, not on top of it | LegalAct.uz |
| Additional cost to employer? | **No** | LegalAct.uz |

- **Arithmetic check** — On gross × 12% PIT, the split is: gross × 0.1% → INPS pension account; gross × 11.9% → State budget as PIT. The employee's total deduction is still 12% of gross, and net pay is still gross × 0.88. [T1]

> **[RESEARCH GAP — reviewer to confirm].** One secondary news item (newslineuz.com) suggested a planned increase of the INPS rate to **2%**, but that page failed to load (TLS error) and the increase / effective date is **UNCONFIRMED**. Treat INPS as **0.1%, carved out of the 12% PIT** until verified against the Tax Code. Source: research caveat (1).

## Section 4 -- Gross-to-Net and Employer-Cost Computation Order

- **Deterministic order of operations** — 1.  Determine gross salary (ish haqi / oylik maosh), in UZS. 2.  PIT = gross × 12%                              (withheld from gross by the employer as tax agent). of which: INPS = gross × 0.1%             (carved out; goes to the employee's pension account) to budget = gross × 11.9%       (remitted to the State Tax Committee as PIT) 3.  Net pay = gross − PIT = gross × (1 − 0.12) = gross × 0.88. 4.  Employer Social Tax = gross × 12%              (standard rate; paid ON TOP of gross). 5.  Total employer cash cost = gross + employer Social Tax = gross × 1.12.  _(PwC WWTS Uzbekistan (PIT 12% withholding; Social Tax 12%); LegalAct.uz (0.1% INPS carve-out).)_
- **Arithmetic check net/employer-cost multipliers** — Arithmetic check: net multiplier = 1 − 0.12 = 0.88; standard employer-cost multiplier = 1 + 0.12 = 1.12. [T1]

**Variant multipliers by employer Social Tax rate**

| Employer type | Social Tax rate | Employer-cost multiplier |
| --- | --- | --- |
| Standard commercial | 12% | 1.12 |
| Budget organisation | 25% | 1.25 |
| Disability workshop | 4.7% | 1.047 |
| SOS Children's Villages | 7% | 1.07 |
| Temporary 1% case | 1% | 1.01 |

## Section 5 -- Conservative Defaults

**Conservative Defaults table**  _(research conservative_defaults)_

| # | Default assumption | Rationale / source |
| --- | --- | --- |
| CD1 | Apply **12%** flat PIT to gross employment income for both residents and resident-status non-residents; for a genuine non-resident, verify treaty relief [T2]. | PwC WWTS Uzbekistan, Individual. |
| CD2 | Use the **12% standard** employer Social Tax rate unless the entity is a budget organisation (25%) or qualifies for a specific reduced/temporary rate. | PwC WWTS Uzbekistan, Corporate: Other taxes. |
| CD3 | Treat the **0.1% INPS** as **carved out of the 12% PIT** (no extra employee cost) — net pay = gross × 0.88. | LegalAct.uz; research caveat (1). |
| CD4 | Where wages are **below the statutory minimum wage**, compute employer Social Tax on **at least the minimum wage** per employee; flag [T2]. | EOR guidance; exact statutory mechanic unconfirmed `[RESEARCH GAP]`. |
| CD5 | File and pay PIT + Social Tax by the **15th** of the following month. | Asanify EOR guide; `[RESEARCH GAP]` — confirm official deadline. |
| CD6 | Do **not** apply the monthly 1× BCV PIT personal deduction to a generic payroll — it applies only to specified eligible categories. PIT base = full gross unless eligibility is confirmed. | PwC WWTS Uzbekistan; research caveat (2). |

## Section 6 -- Required Inputs and Refusal Catalogue

- **Required inputs before computing any payroll [T1]** — Ask for any unknown item. Do not compute until items 1--4 are confirmed. 1. Employer TIN (INN / STIR) and registration with the State Tax Committee. 2. Pay period and payment date (PIT is withheld on payment; the monthly report is filed by the 15th of the following month — CD5). 3. Gross salary for the period, in UZS. If only a net figure is known, flag for gross-up (gross = net / 0.88) and present as estimate only [T2]. 4. Employer Social Tax category: standard commercial (12%), budget organisation (25%), disability workshop (4.7%), SOS Children's Villages (7%), or a qualifying temporary-1% case (CD2) [T2 if unclear].

### Refusal Catalogue [T1]

**Refusal Catalogue table**

| Trigger | Action |
| --- | --- |
| Request concerns a **different CIS jurisdiction** (Kazakhstan KZT, Azerbaijan AZN, Tajikistan TJS, etc.) | STOP. Wrong jurisdiction. This skill is Uzbekistan (UZ / UZS). Escalate to the correct skill [T3]. |
| Gross salary not provided (only "net" or "budget") | Gross-up required (gross = net / 0.88). Present as estimate only and flag [T2]. |
| Payment date / pay period unknown | STOP. Report timing depends on the payment date (CD5). |
| Worker is an **individual entrepreneur (IE) / self-employed** | OUT OF SCOPE for payroll. From 1 Jan 2026 the fixed-PIT IE regime is cancelled and a **1% turnover tax** applies to IEs/self-employed with annual turnover up to UZS 1 billion (EY 2026 alert). Escalate [T3]. |
| Income is **not employment income** (dividends 5%/10%, interest, freight 6%, services) | OUT OF SCOPE for this skill [T3]. |
| Employee may qualify for the **1× BCV PIT deduction** | Do not apply it by default (CD6); confirm eligibility in the Tax Code, flag [T2] / `[RESEARCH GAP]`. |
| Genuine **non-resident** with possible **treaty relief** | Apply 12% by default (CD1) but flag [T2]; verify the applicable double-tax treaty. |

## Section 7 -- Transaction / Payment Pattern Library (Deterministic)

Map bank-statement narrations (often Uzbek / Russian / transliterated) to payroll classifications. All patterns [T1] unless flagged. Major Uzbek banks: National Bank of Uzbekistan (NBU), Uzpromstroybank (SQB), Ipoteka Bank, Hamkorbank, Kapitalbank, Asaka Bank, Agrobank, Davr Bank.

### 7a. Salary credits to the employee's account

**Salary credits narration table**

| Narration pattern (Uzbek / Russian / common) | Classification |
| --- | --- |
| ISH HAQI, OYLIK, OYLIK MAOSH | Net salary payment |
| ZARPLATA, ЗАРПЛАТА (Russian "salary") | Net salary payment |
| OYLIK [month/year], MONTHLY SALARY | Net monthly salary |
| AVANS, AVANS TOʻLOVI | Salary advance — partial net payment [T2] |
| PREMIYA, BONUS, MUKOFOT | Bonus — taxable as employment income (12% PIT applies) [T1] |
| OTPUSKNYE, TAʼTIL PULI | Holiday / leave pay — employment income [T1] |

### 7b. Employer remittances (debits from the company account)

**Employer remittances narration table**

| Narration pattern | Classification |
| --- | --- |
| SOLIQ, DSQ, DAVLAT SOLIQ QOʻMITASI, SOLIQ.UZ | Tax remittance to the State Tax Committee (PIT) |
| JSHDS, JISMONIY SHAXSLAR DAROMAD SOLIGʻI | Personal income tax (PIT) withholding remittance |
| IJTIMOIY SOLIQ, SOTSIALNYY NALOG | Employer Social Tax payment |
| INPS, JAMGʻARIB PENSIYA | Individual Accumulative Pension Fund (the 0.1% carved out of PIT) |
| ISH HAQI, ZARPLATA, PAYROLL, NET WAGES | Net salary disbursement to employees |

> Salaries, PIT and Social Tax are **never** items on a VAT (QQS) return — keep them out of uzbekistan-vat. Cross-reference: uzbekistan-vat.md.

## Section 8 -- Filing Obligations

**Forms table**

| Form | Purpose | Deadline | Portal | Source |
| --- | --- | --- | --- | --- |
| **Monthly payroll / withholding report** (PIT + Social Tax) | Declare employee gross income, withheld 12% PIT, employee INPS, and employer 12% Social Tax | By the **15th** of the month following the reporting month; tax + contributions paid by the same date | my.soliq.uz | Asanify EOR guide; `[RESEARCH GAP]` — confirm official form designation |
| **Individual annual tax return** (declaration of income) | Filed by individuals where required (multiple income sources, foreign income); most pure-employment taxpayers are settled via employer withholding | **Filing by 1 April** of the following year; **PIT balance payable by 1 June** of the following year | my.soliq.uz | PwC WWTS Uzbekistan, Individual: Tax administration |

> **[RESEARCH GAP — reviewer to confirm].** The monthly report **form name** and the e-filing mechanics (my.soliq.uz, 15th-of-month deadline) come from secondary EOR guides, not directly from the authority. Confirm the current official form designation and deadline against soliq.uz / the Tax Code before relying. Source: research caveat (6).

> For an employee whose salary is fully taxed at source via the employer as tax agent, **no annual return** is generally required — the annual return is for individuals with income (e.g. multiple sources, foreign income) not fully settled by withholding. [T1]

## Section 9 -- Minimum Wage and Base Calculation Value (BCV)

Two statutory reference figures drive Uzbek payroll thresholds. Both were reset effective **1 August 2025** by Presidential Decree No. UP-97 (2025).

**Minimum wage and BCV table**

| Item | Value | Effective | Source |
| --- | --- | --- | --- |
| Statutory minimum wage | **UZS 1,271,000 / month** (up from UZS 1,155,000) | 1 Aug 2025 | WageIndicator; Presidential Decree No. UP-97 (2025) |
| Base Calculation Value (BCV / BHM) | **UZS 412,000 / month** | 1 Aug 2025 | PwC WWTS Uzbekistan, Individual: Significant developments |

- **Minimum wage and BCV usage** — The minimum wage is the floor for contractual pay and, in practice, the minimum base for employer Social Tax where actual wages are lower (CD4 / [RESEARCH GAP]). [T2] The BCV is used for the standard 1× BCV monthly PIT personal deduction (eligible categories only — CD6), and for fines, duties and statutory thresholds. [T1]

## Section 10 -- Worked Examples

All figures in UZS. Each example is recomputed end-to-end. Unless stated, the employer is a **standard commercial entity** (employee net = gross × 0.88; employer cost = gross × 1.12) and **no BCV deduction** applies (CD6).

### Example 1 -- Standard salary, UZS 5,000,000 gross [T1]

- PIT = 5,000,000 × 12% = **600,000**
  - of which INPS (0.1%) = 5,000,000 × 0.1% = **5,000** (to the employee's pension account)
  - of which to budget = 600,000 − 5,000 = **595,000**
- **Net pay = 5,000,000 − 600,000 = 4,400,000** (= 5,000,000 × 0.88) ✓
- Employer Social Tax = 5,000,000 × 12% = **600,000**
- **Total employer cost = 5,000,000 + 600,000 = 5,600,000** (= 5,000,000 × 1.12) ✓
- Total to remit (PIT + employer Social Tax) = 600,000 + 600,000 = **1,200,000**

Bank statement: a credit of UZS 4,400,000 narrated `ISH HAQI 03/2025`.

### Example 2 -- Mid salary, UZS 3,000,000 gross [T1]

- PIT = 3,000,000 × 12% = **360,000** (INPS 0.1% = 3,000; to budget = 357,000)
- **Net pay = 3,000,000 − 360,000 = 2,640,000** (= 3,000,000 × 0.88) ✓
- Employer Social Tax = 3,000,000 × 12% = **360,000**
- **Total employer cost = 3,360,000** (= 3,000,000 × 1.12) ✓
- Total to remit = 360,000 + 360,000 = **720,000**

### Example 3 -- Minimum-wage salary, UZS 1,271,000 gross [T1]

- PIT = 1,271,000 × 12% = **152,520** (INPS 0.1% = 1,271; to budget = 151,249)
- **Net pay = 1,271,000 − 152,520 = 1,118,480** (= 1,271,000 × 0.88) ✓
- Employer Social Tax = 1,271,000 × 12% = **152,520**
- **Total employer cost = 1,423,520** (= 1,271,000 × 1.12) ✓

> Note: there is **no tax-free band** by default — PIT applies from the first soʻm of salary (the 1× BCV deduction is for eligible categories only, CD6). [T1]

### Example 4 -- High salary, UZS 10,000,000 gross [T1]

- PIT = 10,000,000 × 12% = **1,200,000** (INPS 0.1% = 10,000; to budget = 1,190,000)
- **Net pay = 10,000,000 − 1,200,000 = 8,800,000** (= 10,000,000 × 0.88) ✓
- Employer Social Tax = 10,000,000 × 12% = **1,200,000**
- **Total employer cost = 11,200,000** (= 10,000,000 × 1.12) ✓
- Total to remit = 1,200,000 + 1,200,000 = **2,400,000**

### Example 5 -- Budget (state-financed) organisation, UZS 4,000,000 gross [T1]

- PIT = 4,000,000 × 12% = **480,000** (INPS 0.1% = 4,000; to budget = 476,000)
- **Net pay = 4,000,000 − 480,000 = 3,520,000** (= 4,000,000 × 0.88) ✓
- Employer Social Tax (**25%** — budget organisation) = 4,000,000 × 25% = **1,000,000**
- **Total employer cost = 4,000,000 + 1,000,000 = 5,000,000** (= 4,000,000 × 1.25) ✓

> The employee side is **identical** to a commercial entity (12% PIT). Only the **employer Social Tax rate** differs (25% vs 12%). [T1]

### Example 6 -- Temporary 1% Social Tax case, UZS 2,000,000 gross [T1] / [T2]

Employer qualifies for a temporary 1% Social Tax rate (e.g. low-income staff earning > 1.5× minimum wage, 1 Jan 2025 – 1 Jan 2028 — confirm eligibility).

- PIT = 2,000,000 × 12% = **240,000** (INPS 0.1% = 2,000; to budget = 238,000)
- **Net pay = 2,000,000 − 240,000 = 1,760,000** (= 2,000,000 × 0.88) ✓
- Employer Social Tax (**1%**) = 2,000,000 × 1% = **20,000**
- **Total employer cost = 2,000,000 + 20,000 = 2,020,000** (= 2,000,000 × 1.01) ✓

> **[T2].** The 1% rate is conditional and time-limited (Section 3a). Confirm the employer/employee qualifies and the window is open before applying it; otherwise default to 12% (CD2).

## Section 11 -- Tier 1 Rules (Deterministic)

**Tier 1 Rules table**

| # | Rule | Source |
| --- | --- | --- |
| T1-1 | PIT on salary is a **flat 12%** of the PIT base (gross, by default), withheld at source by the employer as tax agent. No progressive bands since the 2019 reform. | PwC WWTS Uzbekistan, Individual |
| T1-2 | Non-resident Uzbek-source **employment** income is also taxed at **12%** (reduced from the former 20%). Verify treaty relief for genuine non-residents. | PwC WWTS Uzbekistan, Individual |
| T1-3 | Employer **Social Tax (Ijtimoiy soliq)** standard rate is **12%** of total gross payroll (local + expatriate); it is an employer cost, **not** withheld from the employee. | PwC WWTS Uzbekistan, Corporate: Other taxes |
| T1-4 | **Budget organisations** pay Social Tax at **25%**; specialised disability workshops at **4.7%**; SOS Children's Villages at **7%**; defined temporary cases at **1%**. | PwC WWTS Uzbekistan, Individual / Corporate: Other taxes; EY 2026 alert |
| T1-5 | Employee **INPS** pension is **0.1% of gross, carved OUT of the 12% PIT** — it reduces the PIT remitted to budget and is NOT an additional employee or employer cost. | LegalAct.uz |
| T1-6 | PIT is computed on a **cumulative (year-to-date)** basis each month: `PIT(Jan→current) − PIT(Jan→previous)`. For constant salary with no deduction this equals `monthly gross × 12%`. | LegalAct.uz |
| T1-7 | Net pay = gross × **0.88**; standard total employer cash cost = gross × **1.12** (1.25 budget org; 1.047 disability workshop; 1.07 SOS; 1.01 temporary-1% case). | derived from T1-1 + T1-3/T1-4 |
| T1-8 | **BCV = UZS 412,000/month** (eff. 1 Aug 2025); used for the 1× BCV PIT deduction (eligible categories only) and for fines/duties. | PwC WWTS Uzbekistan, Significant developments |
| T1-9 | **Statutory minimum wage = UZS 1,271,000/month** (eff. 1 Aug 2025, up from UZS 1,155,000) under Presidential Decree No. UP-97. | WageIndicator; Presidential Decree No. UP-97 |
| T1-10 | Tax residency: **183+ days** of presence in any 12-month period beginning or ending in the tax year; or < 183 days but more than in any other country. | PwC WWTS Uzbekistan, Individual: Residence |
| T1-11 | The tax year is the **calendar year**. The monthly payroll report (PIT + Social Tax) is filed and paid by the **15th** of the following month (CD5; confirm form designation). | PwC WWTS Uzbekistan, Tax administration; Asanify |
| T1-12 | Individual annual income tax return, where required, is due by **1 April** of the following year; any PIT balance is payable by **1 June** of the following year. | PwC WWTS Uzbekistan, Individual: Tax administration |

### Context rates (for cross-skill reference; not payroll) [T1]

**Context rates table**

| Item | Rate / value | Source |
| --- | --- | --- |
| Resident dividends / interest PIT | 5% | PwC WWTS Uzbekistan, Individual |
| Non-resident dividends / interest PIT | 10% | PwC WWTS Uzbekistan, Individual |
| Non-resident transportation / freight PIT | 6% | PwC WWTS Uzbekistan, Individual |
| IE / self-employed turnover tax (from 1 Jan 2026) | 1% of turnover up to UZS 1 billion/yr; fixed-PIT IE regime cancelled; under-UZS-100m exemption abolished | EY Global Tax Alert, Jan 2026 |

## Section 12 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 Catalogue table**

| # | Situation | Why it needs judgement | Action |
| --- | --- | --- | --- |
| T2-1 | Employee may qualify for the **1× BCV PIT deduction** | The deduction applies only to specified categories, not universally | Default to full gross (CD6); confirm eligibility; flag `[RESEARCH GAP]`. |
| T2-2 | **Genuine non-resident** employee | Treaty relief may reduce / reallocate taxing rights | Apply 12% by default (CD1); verify the applicable double-tax treaty. |
| T2-3 | Employer **Social Tax category** unclear (commercial vs budget vs reduced/temporary) | Rate ranges from 1% to 25% | Default 12% (CD2); confirm category before finalising. |
| T2-4 | **Temporary 1% Social Tax** eligibility / window | Each case has its own conditions and sunset date | Confirm eligibility and that the window is open; else default to 12%. |
| T2-5 | Wages **below the minimum wage** — Social Tax minimum base | Exact statutory minimum-base mechanic unconfirmed | Compute Social Tax on at least the minimum wage (CD4); flag `[RESEARCH GAP]`. |
| T2-6 | **Net-to-gross** gross-up requested | Iterative / rounding-sensitive (gross = net / 0.88) | Present as estimate; flag for adviser. |
| T2-7 | Worker may be an **IE / self-employed** rather than an employee | Wrong regime (1% turnover tax from 2026, not payroll) | Escalate [T3] — out of payroll scope. |
| T2-8 | **INPS rate** | A secondary source hinted at a planned 2% rate (unverified, page failed to load) | Use 0.1% (CD3); confirm against the Tax Code before relying. `[RESEARCH GAP]` |
| T2-9 | Exact **penalty / late-payment interest (peni)** amounts | Not confirmed from a primary authority source | Cross-check the Tax Code / Code of Administrative Liability before relying. `[RESEARCH GAP]` |

## Section 13 -- Excel Working Paper Template

**Excel Working Paper Template table**

| Cell ref | Label | Formula / source |
| --- | --- | --- |
| B1 | Pay period (month/year) | input |
| B2 | Payment date | input — drives report timing (CD5) |
| B3 | Gross salary (ish haqi) | input |
| B4 | Employer Social Tax rate (0.12 / 0.25 / 0.047 / 0.07 / 0.01) | input (CD2) |
| B5 | PIT (12%) | `=ROUND(B3*0.12,2)` |
| B6 | of which INPS (0.1%, carved out of B5) | `=ROUND(B3*0.001,2)` |
| B7 | of which PIT to budget | `=B5-B6` |
| B8 | **Net pay** | `=B3-B5` |
| B9 | Employer Social Tax | `=ROUND(B3*B4,2)` |
| B10 | **Total employer cost** | `=B3+B9` |
| B11 | Total to remit (PIT + employer Social Tax) | `=B5+B9` |

Validation rows: confirm B8 = B3 × 0.88; confirm B6 + B7 = B5; confirm B10 = B3 × (1 + B4); for a standard commercial entity (B4 = 0.12), confirm B10 = B3 × 1.12.

## Section 14 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide table**

| Term (Uzbek / Russian transliterated) | English | Notes |
| --- | --- | --- |
| ish haqi / oylik / oylik maosh | salary / wage | gross unless context says net |
| zarplata (зарплата) | salary | Russian — common in narrations |
| avans | advance / instalment | partial salary payment |
| premiya / mukofot | bonus / premium | taxable as employment income (12% PIT) |
| jismoniy shaxslar daromad soligʻi (JShDS) | personal income tax | the 12% PIT |
| ijtimoiy soliq | social tax | employer 12% (etc.) |
| INPS / jamgʻarib pensiya | individual accumulative pension fund | the 0.1% carved out of PIT |
| Davlat soliq qoʻmitasi (DSQ) | State Tax Committee | soliq.uz / my.soliq.uz |
| STIR / INN | taxpayer identification number | employer / individual TIN |
| naqd pul | cash | cash withdrawal — exclude from payroll classification |
| ichki oʻtkazma | internal transfer | between client's own accounts — exclude |

**Conventions.** Uzbek banks export statements in UZS; dates often DD.MM.YYYY. Convert foreign-currency salaries to UZS at the Central Bank of the Republic of Uzbekistan (cbu.uz) rate on the relevant date. Narrations may appear in Uzbek (Latin or Cyrillic) or Russian.

## Section 15 -- Onboarding Fallback

If the engagement is mid-year or records are incomplete:

1. **No prior monthly reports on hand** → request the my.soliq.uz filing history; reconcile each month's PIT and Social Tax against bank remittances to the State Tax Committee. Do not assume prior months were correct.
2. **Net-only history** → reconstruct gross via the gross-to-net order (Section 4): gross = net / 0.88, iterating for rounding; mark all reconstructed grosses as estimates [T2].
3. **Employer Social Tax category unknown** → default to **12% standard** (CD2) unless the entity is clearly a budget organisation (25%) or a confirmed reduced/temporary case; confirm before finalising.
4. **Worker type unclear (employee vs IE/self-employed)** → STOP and confirm; the IE / self-employed regimes (1% turnover tax from 2026) are out of payroll scope [T3].
5. **BCV-deduction eligibility uncertain** → do **not** apply the 1× BCV deduction by default (CD6); compute PIT on full gross and flag [T2] / `[RESEARCH GAP]`.

## Section 16 -- Reference Material

**Reference Material table**

| Item | Value | Source |
| --- | --- | --- |
| PIT (salary) rate | 12% flat on gross (residents and non-resident employment income) | PwC WWTS Uzbekistan, Individual |
| Employer Social Tax — standard | 12% of gross payroll | PwC WWTS Uzbekistan, Corporate: Other taxes |
| Employer Social Tax — budget org | 25% of gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| Employer Social Tax — disability workshop | 4.7% of gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| Employer Social Tax — SOS Children's Villages | 7% of gross payroll | PwC WWTS Uzbekistan, Individual: Other taxes |
| Employer Social Tax — temporary case | 1% of gross payroll (conditional / time-limited) | PwC WWTS Uzbekistan, Corporate: Other taxes; EY 2026 alert |
| Employee INPS pension | 0.1% of gross, carved out of the 12% PIT (not additional) | LegalAct.uz |
| Net pay multiplier | 0.88 | derived |
| Employer cost multiplier (standard / budget / disability / SOS / 1% case) | 1.12 / 1.25 / 1.047 / 1.07 / 1.01 | derived |
| Statutory minimum wage | UZS 1,271,000/month (eff. 1 Aug 2025) | WageIndicator; Presidential Decree No. UP-97 |
| Base Calculation Value (BCV) | UZS 412,000/month (eff. 1 Aug 2025) | PwC WWTS Uzbekistan, Significant developments |
| Tax residency | 183 days in any 12-month period | PwC WWTS Uzbekistan, Individual: Residence |
| Monthly report + payment deadline | 15th of following month | Asanify EOR guide; `[RESEARCH GAP]` |
| Annual individual return | Filing by 1 April; PIT balance payable by 1 June | PwC WWTS Uzbekistan, Tax administration |
| Tax year | Calendar year | PwC WWTS Uzbekistan, Tax administration |
| Resident dividends / interest PIT | 5% | PwC WWTS Uzbekistan, Individual |
| Non-resident dividends / interest PIT | 10% | PwC WWTS Uzbekistan, Individual |
| Non-resident freight PIT | 6% | PwC WWTS Uzbekistan, Individual |

### Penalties [T2]

**Penalties table**  _(PwC WWTS Uzbekistan, Tax administration)_

| Violation | Amount / rate | Source |
| --- | --- | --- |
| Late filing / late payment of PIT and Social Tax | Penalties + late-payment interest (peni) per the Tax Code and Code of Administrative Liability; exact rates **unconfirmed** | PwC WWTS Uzbekistan, Tax administration — `[RESEARCH GAP]` |

> **[RESEARCH GAP — reviewer to confirm].** Exact penalty and late-payment interest (peni) percentages and fixed fines were **not confirmed from a primary authority source** in this research. Penalties for failure to withhold, file or remit PIT and Social Tax on time are set in the Tax Code of the Republic of Uzbekistan and the Code of Administrative Liability — confirm the current per-day peni rate and fixed fines against soliq.uz / the Tax Code before relying. Source: research caveat (4).

### Authorities and legislation

- **State Tax Committee of the Republic of Uzbekistan** (Davlat soliq qoʻmitasi) — soliq.uz; e-filing my.soliq.uz. Pension/social administered via the Pension Fund and reported through the State Tax Committee.
- **Tax Code of the Republic of Uzbekistan** (Soliq kodeksi), as amended for 2025 — PIT, Social Tax, withholding, declarations, penalties.
- **Presidential Decree No. UP-97 (2025)** — minimum wage and Base Calculation Value (BCV) from 1 Aug 2025.
- **Annual budget / tax-policy amendment laws**; **EY Jan-2026 alert** for 2026 changes.

### Sources

1. PwC Worldwide Tax Summaries — Uzbekistan, Individual: Taxes on personal income (12% PIT; non-resident 12%; dividends/interest/freight). https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Uzbekistan, Individual: Other taxes (Social Tax rates: 25% budget, 4.7% disability, 7% SOS). https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/other-taxes
3. PwC Worldwide Tax Summaries — Uzbekistan, Corporate: Other taxes (Social Tax base 12%; reduced/temporary rates). https://taxsummaries.pwc.com/republic-of-uzbekistan/corporate/other-taxes
4. PwC Worldwide Tax Summaries — Uzbekistan, Individual: Tax administration (deadlines; 1 April / 1 June). https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/tax-administration
5. PwC Worldwide Tax Summaries — Uzbekistan, Individual: Residence (183-day rule). https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/residence
6. PwC Worldwide Tax Summaries — Uzbekistan, Individual: Significant developments (BCV UZS 412,000). https://taxsummaries.pwc.com/republic-of-uzbekistan/individual/significant-developments
7. EY Global Tax Alert — "Uzbekistan: tax updates effective from 2026" (Jan 2026). https://www.ey.com/en_uz/technical/tax-alerts/2026/01/uzbekistan-tax-updates-2026
8. LegalAct.uz — "How to Calculate PIT in Uzbekistan — Rates, Rules, Deductions" (cumulative method; 0.1% INPS carve-out). https://legalact.uz/en/news/personal-income-tax-in-uzbekistan-how-calculate-correctly
9. WageIndicator.org — "Minimum Wage Updated in Uzbekistan from 01 August 2025" (UZS 1,271,000). https://wageindicator.org/salary/minimum-wage/minimum-wages-news/2025/minimum-wage-updated-in-uzbekistan-from-01-august-2025-august-03-2025
10. Asanify — "Payroll in Uzbekistan: A Complete Employer Guide" (monthly filing by the 15th). https://asanify.com/global-employer-of-record/uzbekistan/payroll/

> **Reviewer note on tax year / 2026.** Figures reflect 2025 and were current as of the PwC review dated 16 Jan 2026; the BCV and minimum wage are the 1 Aug 2025 values. The official primary source (soliq.uz / the Tax Code text) was not directly fetched; re-confirm the exact 2025-final figures and any mid-2026 changes before applying. Source: research caveat (general). **Confidence: medium.**

## Section 17 -- Test Suite

Each test states inputs and the recomputed expected output. Reviewers should rerun every figure. All amounts in UZS. Unless stated, the employer is a **standard commercial entity** (net = gross × 0.88; employer cost = gross × 1.12) and no BCV deduction applies.

### Test 1 -- Standard salary

**Input:** Gross UZS 5,000,000, paid March 2025, standard commercial entity.
**Expected:** PIT 600,000 (INPS 5,000; to budget 595,000). **Net 4,400,000.** Employer Social Tax 600,000. **Total employer cost 5,600,000.** Total to remit 1,200,000.

### Test 2 -- Mid salary

**Input:** Gross UZS 3,000,000, paid June 2025, standard commercial entity.
**Expected:** PIT 360,000 (INPS 3,000; to budget 357,000). **Net 2,640,000.** Employer Social Tax 360,000. **Total employer cost 3,360,000.** Total to remit 720,000.

### Test 3 -- Minimum-wage salary

**Input:** Gross UZS 1,271,000 (statutory minimum, eff. 1 Aug 2025), standard commercial entity.
**Expected:** PIT 152,520 (INPS 1,271; to budget 151,249), no tax-free band by default. **Net 1,118,480.** Employer Social Tax 152,520. **Total employer cost 1,423,520.**

### Test 4 -- High salary

**Input:** Gross UZS 10,000,000, paid April 2025, standard commercial entity.
**Expected:** PIT 1,200,000 (INPS 10,000; to budget 1,190,000). **Net 8,800,000.** Employer Social Tax 1,200,000. **Total employer cost 11,200,000.** Total to remit 2,400,000.

### Test 5 -- Budget (state-financed) organisation

**Input:** Gross UZS 4,000,000, budget organisation (Social Tax 25%).
**Expected:** PIT 480,000 (INPS 4,000; to budget 476,000). **Net 3,520,000.** Employer Social Tax 1,000,000. **Total employer cost 5,000,000** (= 4,000,000 × 1.25). Employee side identical to a commercial entity.

### Test 6 -- Temporary 1% Social Tax case [T2]

**Input:** Gross UZS 2,000,000, qualifying temporary-1% Social Tax case (confirm eligibility / window).
**Expected:** PIT 240,000 (INPS 2,000; to budget 238,000). **Net 1,760,000.** Employer Social Tax 20,000. **Total employer cost 2,020,000** (= 2,000,000 × 1.01). Flag: confirm the 1% rate applies; else default to 12%.

### Test 7 -- Net-to-gross gross-up [T2]

**Input:** Known net UZS 4,400,000, standard commercial entity, no BCV deduction.
**Expected:** Gross = 4,400,000 / 0.88 = **5,000,000**; PIT 600,000; employer Social Tax 600,000; total employer cost 5,600,000. Present as estimate; flag for adviser.

### Test 8 -- Wrong jurisdiction guard

**Input:** Request references Kazakhstan KZT / Azerbaijan AZN payroll forms.
**Expected:** REFUSE — this is Uzbekistan (UZ / UZS), not a neighbouring CIS jurisdiction. Escalate to the correct skill [T3].

### Test 9 -- IE / self-employed guard

**Input:** "Salary" turns out to be individual-entrepreneur turnover.
**Expected:** REFUSE for payroll — from 1 Jan 2026 IEs/self-employed pay 1% turnover tax (up to UZS 1 billion/yr); fixed-PIT IE regime cancelled. Out of payroll scope [T3].

## PROHIBITIONS

- **Do not confuse Uzbekistan with neighbouring CIS jurisdictions** — NEVER confuse Uzbekistan (UZ, UZS, soʻm) with a neighbouring CIS jurisdiction (Kazakhstan KZT, Azerbaijan AZN, Tajikistan TJS) — their rates and forms must NOT appear in this skill.
- **No progressive band for Uzbek salary PIT** — NEVER apply a progressive band to Uzbek salary PIT — it is a flat 12% since the 2019 reform.
- **0.1% INPS is carved out of PIT, not additional** — NEVER treat the 0.1% INPS as an additional employee charge — it is carved out of the 12% PIT; net pay is gross × 0.88, not less.
- **Employer Social Tax is not an employee deduction** — NEVER add the employer 12% Social Tax as a deduction from the employee's pay — it is an employer cost on top of gross.
- **1x BCV PIT deduction restricted to eligible categories** — NEVER apply the 1× BCV PIT deduction to a generic payroll by default — it is for specified eligible categories only (CD6); flag [RESEARCH GAP].  _(CD6)_
- **Employer Social Tax rate ranges 1% to 25%, confirm category** — NEVER assume the employer Social Tax rate without confirming the category — it ranges from 1% to 25% (12% standard, 25% budget org, 4.7% disability workshop, 7% SOS, 1% temporary cases).
- **Temporary 1% Social Tax requires confirmed eligibility and open window** — NEVER apply a temporary 1% Social Tax rate without confirming eligibility and that the statutory window is open.
- **IE/self-employed regime out of payroll scope** — NEVER apply the IE / self-employed regime (1% turnover tax from 2026) to an employee's payroll — that is out of payroll scope [T3].
- **Never guess INPS rate, penalty amounts, or RESEARCH GAP figures** — NEVER guess the INPS rate (use 0.1%), the penalty/peni amounts, or any figure marked [RESEARCH GAP — reviewer to confirm] — verify against soliq.uz / the Tax Code.  _(soliq.uz / the Tax Code)_
- **Do not miss monthly payroll report/payment deadline** — NEVER miss the monthly payroll report and payment deadline (15th of the following month, CD5) — confirm the official form designation.  _(CD5)_
- **Always label computations as estimated, direct to qualified adviser** — NEVER present payroll computations as definitive — always label as estimated and direct to a qualified Uzbek tax adviser / licensed accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Uzbek tax adviser or licensed accountant in Uzbekistan) before implementation.

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
