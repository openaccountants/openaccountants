---
name: armenia-payroll
description: "Use this skill whenever asked about Armenia (Republic of Armenia — Hayastan, South Caucasus) payroll processing for employed persons. Trigger on phrases like \"Armenia payroll\", \"Armenian payroll\", \"ashkhatavarts\", \"salary tax Armenia\", \"PIT withholding Armenia\", \"20% income tax Armenia\", \"flat income tax Armenia\", \"funded pension Armenia\", \"mandatory pension Armenia\", \"stamp duty Armenia\", \"military stamp payment\", \"health insurance contribution Armenia\", \"State Revenue Committee\", \"src.am payroll\", \"e-register.am\", \"monthly aggregated income tax calculation\", \"net salary Armenia\", \"gross to net Armenia\", \"employer cost Armenia\", \"minimum wage Armenia\", or any question about computing employee pay, salary withholding tax, mandatory funded pension, stamp duty or health insurance contributions for Armenia-based employees. This skill covers the flat 20% personal income tax withheld at source, the mandatory funded pension (5% or 10%-minus-AMD-25,000), the stamp/military duty, the new (late-2025) employee health insurance contribution, the monthly aggregated calculation filed via the SRC e-portal, and penalties. CRITICAL: this is the COUNTRY of Armenia (jurisdiction AM, currency AMD, Armenian dram) — there is NO separate employer social-security/payroll tax. ALWAYS read this skill before processing any Armenia payroll."
version: 0.1
jurisdiction: AM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia Payroll

## Armenia Payroll Skill v0.1

> **Tier 2 — Research-verified.** Rates and structure are cross-verified across PwC Worldwide Tax Summaries (Armenia, Individual & Corporate, reviewed 5 February 2026), the Tax Code of the Republic of Armenia (Law HO-165-N, in force from 2018, as amended), the Law "On Funded Pensions", the Law "On Stamp Payments" (military/stamp duty), Vardanyan & Partners (armenian-lawyer.com), and Regfollower/Orbitax. Official Armenian-language statute PDFs were not directly text-extracted line-by-line; figures rely on the English consolidations plus Big-4 and specialist summaries. Every figure below carries an inline source or a `[RESEARCH GAP — reviewer to confirm]` marker. A qualified Armenian tax adviser / licensed accountant must validate this skill before production use.

> **CRITICAL DISAMBIGUATION.** Jurisdiction code **AM = the Republic of Armenia (Hayastan, South Caucasus), currency AMD (Armenian dram)**. Do not confuse Armenia (AM) with its neighbour Azerbaijan (AZ) or with the US state of any similar name. If a request concerns another jurisdiction, this is the WRONG skill — escalate.

> **CRITICAL TIMING.** Tax year **2025** spans two regimes. For the **bulk of 2025** (pay periods **before 25 December 2025**): the **five-band stamp/military duty** applies and there is **no** employee health-insurance contribution. For pay periods **on/after 25 December 2025** (and into 2026): a **two-band stamp duty** and a **new mandatory employee health-insurance contribution** apply. Always confirm the **payment date** before choosing the schedule (see CD3, CD4 and Section 4).

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Armenia (Republic of Armenia / Hayastan — South Caucasus) |
| Jurisdiction code | AM |
| Currency | AMD (Armenian dram) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December). Source: PwC WWTS Armenia, Tax administration. |
| Has personal income tax? | Yes -- **flat 20%** on gross employment income, withheld at source by the employer as tax agent. Source: PwC WWTS Armenia, Individual: Taxes on personal income. |
| Personal income tax (salary) | 20% flat on gross employment income. **No personal allowance; no brackets; no progressive rates** (in force since 1 Jan 2023; general PIT rate reached 20% from 1 July 2023). Source: PwC WWTS Armenia, Individual: Taxes on personal income. |
| Mandatory funded pension (employee) | **5%** of gross if gross **< AMD 500,000**; **10% of gross − AMD 25,000** if gross **≥ AMD 500,000**. Withheld by employer. Source: PwC WWTS Armenia, Individual: Other taxes. |
| Funded pension max base / cap | Max monthly base **AMD 1,125,000** (15 × the AMD 75,000 minimum wage); employee contribution capped at **AMD 87,500/month**. Source: PwC WWTS Armenia, Individual: Other taxes. |
| Stamp / military duty (employee) | **Through 24 Dec 2025:** five-band schedule (AMD 1,500 / 3,000 / 5,500 / 8,500 / 15,000). **From 25 Dec 2025:** two bands — **AMD 1,000** if gross ≤ AMD 1,000,000, **AMD 15,000** if gross > AMD 1,000,000. Source: PwC WWTS Armenia, Individual: Other taxes. |
| Employee health-insurance contribution | **From 25 Dec 2025** (effectively a 2026 payroll item): exempt if gross ≤ AMD 200,000; **AMD 4,800/month** for AMD 200,001--500,000; **AMD 10,800/month** above AMD 500,000. Source: Vardanyan & Partners (armenian-lawyer.com). |
| Employer social/payroll tax | **None.** There is **no separate employer-paid social-security or payroll tax** in Armenia's private sector. The employer pays gross salary and acts only as withholding/remitting agent. Source: Vardanyan & Partners (armenian-lawyer.com). |
| Tax authority | State Revenue Committee of the Republic of Armenia (SRC) — src.am |
| Registration / e-filing | e-Register (e-register.am); SRC e-portal for the monthly payroll return |
| Primary forms | Monthly aggregated income-tax-and-social-payment calculation (payroll return); annual personal income declaration (only for income not taxed at source) |
| Monthly return + payment deadline | By the **20th** day of the month following the salary payment; PIT and contributions remitted to the State Budget by the same date. Source: PwC WWTS Armenia, Tax administration. |
| Validated by | Pending -- requires sign-off by a qualified Armenian tax adviser / licensed accountant |
| Skill version | 0.1 |

**Legislation table**

| Law | Scope | Source |
| --- | --- | --- |
| Tax Code of the Republic of Armenia (Law HO-165-N, in force from 2018, as amended) | PIT withholding, declarations, penalties | PwC WWTS Armenia; SRC (src.am) |
| Law "On Funded Pensions" | Mandatory funded pension contributions | PwC WWTS Armenia, Individual: Other taxes |
| Law "On Stamp Payments" | Military / stamp duty (stamp payment) | PwC WWTS Armenia, Individual: Other taxes |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified Armenian tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate and document the gap.

## Section 2 -- Personal Income Tax (PIT) Withholding

- **PIT on employment income** — Employment income (salary, bonuses, commissions, fees) is taxed at a flat 20% of gross pay. The employer is a tax agent: it withholds the 20% PIT at source and remits it to the State Budget by the 20th day of the following month. There is no personal allowance, no brackets and no progressive rate for employment income — the rate is a single flat 20% (in force since 1 January 2023; the general PIT rate reached 20% from 1 July 2023).  _(PwC WWTS Armenia, Individual: Taxes on personal income; Tax administration)_

### PIT formula [T1]

- **PIT formula** — PIT = Gross employment income × 20%  _(PwC WWTS Armenia, Individual: Taxes on personal income)_
- **No tax-free band adjustment** — No tax-free band, no standard deduction, no marital/dependant adjustment for salary. [T1]  _(PwC WWTS Armenia, Individual: Taxes on personal income)_
- **PIT base not reduced by other deductions** — PIT is computed on actual gross salary and is not reduced by the pension/stamp/health deductions (those come out of net, not the PIT base). [T1]  _(PwC WWTS Armenia)_
- **PIT remittance timing** — PIT is withheld at source and remitted by the 20th of the following month via the SRC e-portal.  _(PwC WWTS Armenia, Tax administration)_
- **Residents vs non-residents** — Residents are taxed on worldwide income; non-residents only on Armenian-source income — both are subject to the same 20% wage withholding on Armenian-source employment income. [T1]  _(PwC WWTS Armenia)_

### Other PIT rates (context — NOT employment income) [T1 / informational]

**Other PIT rates table**

| Income type | Rate | Note | Source |
| --- | --- | --- | --- |
| Royalties | 10% | Not employment income. | PwC WWTS Armenia, Individual: Taxes on personal income |
| Interest | 20% | Subject to 20% from 1 Jan 2023. Not employment income. | PwC WWTS Armenia, Individual: Taxes on personal income |
| Lease of property | 10% | Not employment income. | PwC WWTS Armenia, Individual: Taxes on personal income |
| Dividends | 5% | 5% for both foreign and Armenian individuals (conditions apply). Not employment income. | PwC WWTS Armenia, Individual: Taxes on personal income |
| Other income paid by a tax agent (no proper entrepreneur documentation) | 20% | Flat withholding by tax agent. Not salary. | PwC WWTS Armenia, Individual: Tax administration |

> These rates apply to **non-employment** income streams. Do not apply them to a salary payroll computation. If a "salary" turns out to be a royalty, dividend, lease or self-employed fee, this is [T3] — out of scope for payroll.

## Section 3 -- Mandatory Funded Pension Contribution

- **Funded pension applicability** — A mandatory funded pension applies to employees, notaries and individual entrepreneurs born on or after 1 January 1974 (the opt-out ended 1 July 2018). It also applies to foreign nationals with Armenian residence. For employees it is withheld by the employer from gross pay; the scheme is co-financed by the State, but the only payroll-side withholding is the employee deduction — there is no separate employer pension contribution.  _(PwC WWTS Armenia, Individual: Other taxes)_

### Funded pension formula (2025 rates, in force from 1 Jan 2023) [T1]

- **Funded pension formula** — If gross < AMD 500,000:        contribution = gross × 5% If gross ≥ AMD 500,000:        contribution = gross × 10% − AMD 25,000 Subject to a maximum base of AMD 1,125,000 → contribution capped at AMD 87,500/month.  _(PwC WWTS Armenia, Individual: Other taxes)_

### Funded pension worked checks [T1]

- **Continuity at the AMD 500,000 kink:** at exactly AMD 500,000 both formulae give the same result — 500,000 × 5% = **25,000**, and 500,000 × 10% − 25,000 = 50,000 − 25,000 = **25,000**. ✓ The function is continuous, so there is no jump at the threshold.
- **Cap check:** the maximum base is AMD 1,125,000 (= 15 × the AMD 75,000 minimum wage). At that base: 1,125,000 × 10% − 25,000 = 112,500 − 25,000 = **AMD 87,500** — equal to the stated monthly cap. ✓ For any gross above AMD 1,125,000, the contribution stays at **AMD 87,500**.

**Funded pension worked checks table**

| Gross (AMD) | Formula used | Contribution (AMD) |
| --- | --- | --- |
| 75,000 | 5% × gross | 3,750 |
| 300,000 | 5% × gross | 15,000 |
| 499,999 | 5% × gross | 24,999.95 |
| 500,000 | 10% × gross − 25,000 | 25,000 |
| 600,000 | 10% × gross − 25,000 | 35,000 |
| 1,125,000 | 10% × gross − 25,000 (= cap) | 87,500 |
| 1,200,000 | base capped at 1,125,000 | 87,500 |

### Participation / scope rules [T1]

- **Mandatory participation cutoff** — Participation is mandatory for those born on or after 1 January 1974 (opt-out ended 1 July 2018).  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Exemption for older employees** — Employees born before 1 January 1974 are treated as exempt from the pension deduction (CD2) — they remain subject to the 20% PIT and stamp duty (and health insurance from 25 Dec 2025).  _(birth-year cutoff is statutory; research conservative_defaults)_
- **Foreign nationals with Armenian residence** — Applies to foreign nationals with Armenian residence.  _(PwC WWTS Armenia, Individual: Other taxes)_

> **[RESEARCH GAP — reviewer to confirm]** the precise treatment of State co-financing. One source mentions State co-financing of the funded pension; another describes the deduction as coming entirely from the employee. The figure captured here (5% / 10%-minus-AMD-25,000) is the **employee-side withholding**, which is what payroll computes. Confirm whether any State top-up needs to be reflected in the pension transfer mechanics. Source: research caveat.

## Section 4 -- Stamp / Military Duty and Health-Insurance Contribution

- **Deductions are employee-side** — Both stamp/military duty and health-insurance contribution are employee deductions withheld by the employer. They are not employer costs. Both depend on the payment date (see CRITICAL TIMING above).

### 4a. Stamp / military duty (stamp payment) [T1 / T2]

**Five-band schedule (through 24 December 2025)**  _(PwC WWTS Armenia, Individual: Other taxes (prior schedule); research caveat)_

| Monthly gross (AMD) | Stamp duty (AMD/month) |
| --- | --- |
| Up to 100,000 | 1,500 |
| 100,001 -- 200,000 | 3,000 |
| 200,001 -- 500,000 | 5,500 |
| 500,001 -- 1,000,000 | 8,500 |
| 1,000,001 and above | 15,000 |

**Two-band schedule (from 25 December 2025)**  _(PwC WWTS Armenia, Individual: Other taxes)_

| Monthly gross (AMD) | Stamp duty (AMD/month) |
| --- | --- |
| Up to 1,000,000 | 1,000 |
| Above 1,000,000 | 15,000 |

> **[T2] / [RESEARCH GAP — reviewer to confirm].** The older Vardanyan/ISSA-era materials show the five-band schedule; PwC and the updated "Taxes in Armenia 2026" page state the simplified two-band schedule effective **25 December 2025**. For most of tax year 2025 the five-band schedule applied. Confirm the **exact transition date** and per-band amounts against the SRC / Law "On Stamp Payments" before relying on either for a specific pay period (CD3). Source: research caveat.

### 4b. Employee health-insurance contribution (from 25 December 2025) [T2]

- **Health insurance contribution scope** — Mandatory employee health-insurance contribution for employees on employment contracts, withheld by the employer, effective 25 December 2025 (commonly described as effectively a 2026 payroll item).  _(Vardanyan & Partners (armenian-lawyer.com))_

**Health-insurance contribution bands**  _(Vardanyan & Partners (armenian-lawyer.com))_

| Monthly gross (AMD) | Health-insurance contribution (AMD/month) |
| --- | --- |
| Up to 200,000 | 0 (exempt) |
| 200,001 -- 500,000 | 4,800 |
| Above 500,000 | 10,800 |

> **[T2] / [RESEARCH GAP — reviewer to confirm].** This contribution is brand-new (effective 25 Dec 2025) and is described by secondary sources as effectively a 2026 payroll item. The precise commencement date, and whether it overlaps/replaces any other charge, should be verified against primary legislation. **Conservative default (CD4):** apply it only to wages paid **on/after 25 Dec 2025** with gross **over AMD 200,000**; treat it as **not applicable** for the bulk of the 2025 tax year. Source: research caveat.

## Section 5 -- Gross-to-Net Computation Order

- **Gross-to-net computation order** — 1.  Determine gross employment income (ashkhatavarts), in AMD. 2.  PIT                = gross × 20%                              (withheld from gross). 3.  Funded pension     = gross × 5%               if gross < 500,000 = gross × 10% − 25,000     if gross ≥ 500,000   (cap AMD 87,500) = 0                        if employee born before 1 Jan 1974 (CD2) 4.  Stamp / military duty = per Section 4a band (schedule depends on payment date). 5.  Health insurance   = per Section 4b band      (only if paid on/after 25 Dec 2025; CD4). 6.  Net pay            = gross − PIT − pension − stamp − health. 7.  Total employer cash cost = gross  (no employer social contribution — CD1).  _(PwC WWTS Armenia (PIT 20%, tax-agent withholding; funded pension); Vardanyan & Partners (no employer contribution))_

> Unlike a single fixed-percentage jurisdiction, Armenia's net pay is **not** a clean multiplier of gross — the funded pension formula has a kink at AMD 500,000, and stamp duty + health insurance are **flat band amounts**, not percentages. Always compute each line explicitly; do not approximate with a single ratio. [T1]

## Section 6 -- Conservative Defaults

**Conservative defaults table**  _(research conservative_defaults)_

| # | Default assumption | Rationale / source |
| --- | --- | --- |
| CD1 | Employer payroll cost = **gross salary only** (0% employer social contribution) unless a sector-specific levy is identified. | Armenia has no general employer social-security charge. Vardanyan & Partners. |
| CD2 | Apply the funded pension to employees **born on/after 1 Jan 1974**; treat employees **born before 1974** as **exempt** from the pension deduction (still subject to 20% PIT and stamp duty). | Birth-year cutoff is statutory. PwC WWTS Armenia, Individual: Other taxes. |
| CD3 | For pay periods **on/after 25 Dec 2025** use the **two-band** stamp schedule (AMD 1,000 / AMD 15,000); for periods **before** that date use the **five-band** schedule. | Late-2025 legislative change. PwC; research caveat. |
| CD4 | Apply the health-insurance contribution **only** to wages paid **on/after 25 Dec 2025** with gross **over AMD 200,000**; treat as **not applicable** for the bulk of the 2025 tax year. | New rule effective at the very end of 2025. Vardanyan & Partners. |
| CD5 | Treat the income as standard **employment income** (20% PIT withholding) unless told otherwise; do not apply royalty/dividend/lease/self-employed regimes to payroll. | Those rates apply to non-employment income. PwC WWTS Armenia. |
| CD6 | Use the **agreed contractual gross salary** as the payroll base; the AMD 75,000 minimum wage is a floor, not the computation base. | Minimum wage AMD 75,000 (secondary aggregator — confirm). RemotePeople. |

## Section 7 -- Required Inputs and Refusal Catalogue

- **Required inputs before computing any payroll [T1]** — Ask for any unknown item. Do not compute until items 1--5 are confirmed. 1. Employer TIN (8-digit) and registration with the SRC (e-register.am). 2. Pay period and payment date — the payment date drives (a) the 20th-of-following-month deadline and (b) which stamp schedule and whether health insurance applies (25 Dec 2025 cutoff). 3. Gross salary for the period, in AMD. If only a net figure is known, flag for gross-up (iterative — the pension kink and flat band charges make this non-linear) and present as estimate only [T2]. 4. Employee date of birth (born on/after vs before 1 Jan 1974) — determines funded-pension applicability (CD2) [T2 if unclear]. 5. Confirmation the income is employment income (not royalty/dividend/lease/self-employed fee).

### Refusal Catalogue [T1]

**Refusal catalogue table**

| Trigger | Action |
| --- | --- |
| Request concerns a **different country** (e.g. Azerbaijan, or a US jurisdiction) | STOP. Wrong jurisdiction. This skill is the Republic of Armenia (AM / AMD). Escalate [T3]. |
| Gross salary not provided (only "net" or "budget") | Gross-up required — but it is **non-linear** (pension kink + flat band charges). Present as estimate only and flag [T2]. |
| Payment date / pay period unknown | STOP. The stamp schedule, health-insurance applicability and filing deadline all depend on the payment date (25 Dec 2025 cutoff). |
| Employee date of birth unknown (pension applicability) | Default to **enrolled** for unknown DOB (CD2), but flag [T2] — if the employee was born before 1 Jan 1974 they are pension-exempt. |
| Worker is **self-employed / individual entrepreneur**, on the **micro-business** (< AMD 24,000,000 turnover) or **turnover/SME** regime | OUT OF SCOPE for payroll (the employer still withholds 20% PIT on any **wages** it pays, but the IE's own regime is separate). Escalate [T3]. |
| Income is **not employment income** (royalties 10%, interest 20%, lease 10%, dividends 5%) | OUT OF SCOPE for this skill — separate withholding regimes [T3]. |
| Stamp-schedule transition date / health-insurance commencement materially affects the result | Apply CD3/CD4, flag [T2] / `[RESEARCH GAP]`, and require SRC / primary-legislation confirmation. |

## Section 8 -- Transaction / Payment Pattern Library (Deterministic)

- **Transaction library intro** — Map bank-statement narrations (often Armenian / transliterated) to payroll classifications. All patterns [T1] unless flagged. Armenian banks: Ameriabank, Ardshinbank, Acba Bank, Converse Bank, Inecobank, ID Bank, Evocabank, Unibank, Araratbank.

### 8a. Salary credits to the employee's account

**Salary credit narrations table**

| Narration pattern (Armenian / common) | Classification |
| --- | --- |
| ASHKHATAVARTS, աշխատավարձ | Net salary payment |
| ASHKHATAVARTS [month/year], MONTHLY SALARY | Net monthly salary |
| ASHKHATAVARDZ, REMUNERATION, ALARI | Salary / remuneration |
| KANKHIK / AVANS, SALARY ADVANCE | Salary advance — partial net payment [T2] |
| PREMIA / HAVELAVCHAR, BONUS | Bonus — taxable as employment income (20% PIT; pension/stamp/health bands apply) [T1] |

### 8b. Employer remittances (debits from the company account)

**Employer remittance narrations table**

| Narration pattern | Classification |
| --- | --- |
| HARKADIR / HARK, TAX PAYMENT, SRC | PIT / tax remittance to the State Budget (State Revenue Committee) |
| EKAMTAYIN HARK, INCOME TAX | Income (personal) tax payment — the 20% PIT |
| KENSATHOSHAK / FUNDED PENSION, PENSION CONTRIBUTION | Funded pension transfer (employee withholding) |
| DROSHMANISHAYIN / STAMP, MILITARY DUTY | Stamp / military duty remittance |
| APAHOVAGRAKAN / HEALTH INSURANCE | Health-insurance contribution (from 25 Dec 2025) |
| ASHKHATAVARTSER, PAYROLL, NET WAGES | Net salary disbursement to employees |

> Salaries, PIT, pension, stamp duty and health-insurance contributions are **never** items on a VAT return — keep them out of armenia-vat. Source: armenia-vat.md (salary/payroll = EXCLUDE).

### Forms [T1]

**Forms table**

| Form | Purpose | Deadline | Portal | Source |
| --- | --- | --- | --- | --- |
| **Monthly aggregated income-tax-and-social-payment calculation** (payroll return) | Reports per-employee gross income, PIT withheld, funded-pension contribution, stamp duty (and health insurance from 25 Dec 2025) | By the **20th** day of the month following the salary payment; **PIT and contributions remitted to the State Budget by the same date** | SRC e-portal | PwC WWTS Armenia, Tax administration |
| **Annual personal income declaration** | Individuals with income **not** taxed at source (e.g. foreign income, untaxed Armenian income); employees with only PIT-withheld salary generally need **not** file | For 2025 income: by **1 November 2026**. From the 2027 cycle the window shifts to **2 March -- 1 July** of the following year. | SRC e-portal | PwC WWTS Armenia, Tax administration |
| **Employer / business registration (e-Register)** | Register entity with the SRC and obtain an **8-digit TIN**; both employer and each employee need a TIN to operate payroll | Within **15 days** of incorporation / commencing activity | e-register.am | State Revenue Committee (src.am) |

> For an employee whose salary is fully taxed at source, **no annual return** is generally required — the annual return is for individuals with income **not** taxed at source. [T1]

## Section 10 -- Minimum Wage

**Minimum wage table**

| Item | Value | Source |
| --- | --- | --- |
| Statutory minimum monthly wage | **AMD 75,000** gross, effective 1 Jan 2023 and unchanged through 2025 | RemotePeople / WageIndicator (secondary) — `[RESEARCH GAP]` |
| 2026 proposal | An increase to **AMD 85,000** was discussed for 2026 but **not confirmed enacted** as of early 2026 | RemotePeople (secondary) — `[RESEARCH GAP]` |
| Funded pension max base link | The pension max base AMD 1,125,000 = **15 × the AMD 75,000 minimum wage** | PwC WWTS Armenia, Individual: Other taxes |

> **[RESEARCH GAP — reviewer to confirm].** The AMD 75,000 minimum wage and the planned AMD 85,000 for 2026 come from secondary aggregators (RemotePeople / WageIndicator), not directly from an Armenian government gazette. Confirm against the SRC or Ministry of Labour. Use the **agreed contractual salary** as the payroll base (CD6).

## Section 11 -- Worked Examples

All figures in AMD. Each example is recomputed end-to-end. Unless stated, the employee is born on/after 1 Jan 1974 (pension applies), and the pay period is in the bulk of 2025 (before 25 Dec 2025) so the five-band stamp applies and there is no health insurance.

### Example 1 -- Standard salary, AMD 300,000 gross (below 500k) [T1]

- PIT = 300,000 × 20% = **60,000**
- Funded pension = 300,000 × 5% = **15,000**
- Stamp duty (200,001--500,000 band) = **5,500**
- Health insurance = **0** (pre-25 Dec 2025)
- **Net pay = 300,000 − 60,000 − 15,000 − 5,500 = 219,500** ✓
- **Total employer cost = 300,000** (no employer social contribution) ✓

Bank statement: a credit of AMD 219,500 narrated `ASHKHATAVARTS 06/2025`.

### Example 2 -- Low salary, AMD 150,000 gross [T1]

- PIT = 150,000 × 20% = **30,000**
- Funded pension = 150,000 × 5% = **7,500**
- Stamp duty (100,001--200,000 band) = **3,000**
- Health insurance = **0** (pre-25 Dec 2025)
- **Net pay = 150,000 − 30,000 − 7,500 − 3,000 = 109,500** ✓
- **Total employer cost = 150,000** ✓

> Note: there is **no tax-free allowance** — PIT applies from the first dram of salary. [T1]

### Example 3 -- Above-kink salary, AMD 600,000 gross (≥ 500k) [T1]

- PIT = 600,000 × 20% = **120,000**
- Funded pension = 600,000 × 10% − 25,000 = 60,000 − 25,000 = **35,000**
- Stamp duty (500,001--1,000,000 band) = **8,500**
- Health insurance = **0** (pre-25 Dec 2025)
- **Net pay = 600,000 − 120,000 − 35,000 − 8,500 = 436,500** ✓
- **Total employer cost = 600,000** ✓

### Example 4 -- High salary above the pension cap base, AMD 1,200,000 gross [T1]

- PIT = 1,200,000 × 20% = **240,000**
- Funded pension: gross exceeds the AMD 1,125,000 max base → contribution **capped at 87,500** (not 10% × 1,200,000 − 25,000 = 95,000). Use **87,500**.
- Stamp duty (1,000,001 and above band) = **15,000**
- Health insurance = **0** (pre-25 Dec 2025)
- **Net pay = 1,200,000 − 240,000 − 87,500 − 15,000 = 857,500** ✓
- **Total employer cost = 1,200,000** ✓

### Example 5 -- Minimum-wage salary, AMD 75,000 gross [T1]

- PIT = 75,000 × 20% = **15,000**
- Funded pension = 75,000 × 5% = **3,750**
- Stamp duty (up to 100,000 band) = **1,500**
- Health insurance = **0** (pre-25 Dec 2025; also below AMD 200,000 floor)
- **Net pay = 75,000 − 15,000 − 3,750 − 1,500 = 54,750** ✓
- **Total employer cost = 75,000** ✓

### Example 6 -- Pension-exempt employee (born before 1 Jan 1974), AMD 400,000 gross [T1]

- Employee is **exempt** from the funded pension (CD2). Drop the pension line; PIT and stamp still apply.
- PIT = 400,000 × 20% = **80,000**
- Funded pension = **0**
- Stamp duty (200,001--500,000 band) = **5,500**
- Health insurance = **0** (pre-25 Dec 2025)
- **Net pay = 400,000 − 80,000 − 5,500 = 314,500** ✓
- **Total employer cost = 400,000** ✓

### Example 7 -- Late-Dec-2025 / 2026 basis, AMD 600,000 gross (two-band stamp + health insurance) [T1 / T2]

Payment date on/after 25 Dec 2025 → two-band stamp + health insurance apply (CD3, CD4).

- PIT = 600,000 × 20% = **120,000**
- Funded pension = 600,000 × 10% − 25,000 = **35,000**
- Stamp duty (≤ 1,000,000, two-band) = **1,000**
- Health insurance (above 500,000) = **10,800**
- **Net pay = 600,000 − 120,000 − 35,000 − 1,000 − 10,800 = 433,200** ✓
- **Total employer cost = 600,000** ✓

> Compare with Example 3 (same gross, pre-25 Dec 2025): net was 436,500. The lower stamp (1,000 vs 8,500) is more than offset by the new 10,800 health-insurance charge, so net **falls** by 3,300. Confirm the transition date before applying [T2].

## Section 12 -- Tier 1 Rules (Deterministic)

**Tier 1 rules table**

| # | Rule | Source |
| --- | --- | --- |
| T1-1 | PIT on employment income is a **flat 20%** of gross, withheld at source by the employer as tax agent. No personal allowance, no brackets, no progressive rates (since 1 Jan 2023; 20% general rate from 1 July 2023). | PwC WWTS Armenia, Individual: Taxes on personal income |
| T1-2 | The employer is a **tax agent**: it withholds the 20% PIT and remits it to the State Budget by the **20th** day of the following month, alongside the monthly aggregated calculation on the SRC e-portal. | PwC WWTS Armenia, Tax administration |
| T1-3 | There is **NO separate employer-paid social-security or payroll tax**. All payroll deductions come out of the employee's gross pay; the employer's only payroll cost is the gross salary plus its agent/remittance duties. | Vardanyan & Partners (armenian-lawyer.com) |
| T1-4 | Mandatory funded pension applies to employees **born on/after 1 Jan 1974** (opt-out ended 1 July 2018): **5%** of gross if gross < AMD 500,000; **10% × gross − AMD 25,000** if gross ≥ AMD 500,000; withheld by the employer. | PwC WWTS Armenia, Individual: Other taxes |
| T1-5 | Funded-pension **max monthly base is AMD 1,125,000** (15 × the AMD 75,000 minimum wage); the employee contribution is **capped at AMD 87,500/month**. | PwC WWTS Armenia, Individual: Other taxes |
| T1-6 | Stamp / military duty was simplified effective **25 Dec 2025** to two bands: **AMD 1,000** for gross ≤ AMD 1,000,000 and **AMD 15,000** above. Through 24 Dec 2025 a **five-band** schedule applied (AMD 1,500 / 3,000 / 5,500 / 8,500 / 15,000). | PwC WWTS Armenia, Individual: Other taxes |
| T1-7 | A mandatory **employee health-insurance contribution** starts **25 Dec 2025** for employees with gross over AMD 200,000: **AMD 4,800/month** for AMD 200,001--500,000 and **AMD 10,800/month** above AMD 500,000. | Vardanyan & Partners (armenian-lawyer.com) |
| T1-8 | The tax year is the **calendar year**. Employees with only PIT-withheld salary generally need **not** file an annual return; the annual personal income declaration is for income **not** taxed at source. | PwC WWTS Armenia, Tax administration |
| T1-9 | Residents are taxed on **worldwide** income; non-residents only on **Armenian-source** income — both salary types attract the same 20% wage withholding on Armenian-source employment income. | PwC WWTS Armenia, Individual: Taxes on personal income |
| T1-10 | Employers and employees must each hold an **8-digit TIN**; entities register with the SRC via **e-register.am** within **15 days** of incorporation / commencing activity. | State Revenue Committee (src.am) |

### Context rates (for cross-skill reference; not payroll) [T1]

**Context rates table**

| Item | Rate / value | Source |
| --- | --- | --- |
| Corporate income (profit) tax | 18% of net profit | PwC WWTS Armenia, Corporate: Taxes on corporate income |
| Standard VAT | 20% | PwC WWTS Armenia, Corporate: Other taxes; see armenia-vat.md |
| VAT registration threshold | AMD 115,000,000 annual turnover | PwC WWTS Armenia, Corporate: Other taxes |
| Micro-business exemption threshold | AMD 24,000,000 annual turnover (exempt from main taxes; employer still withholds 20% PIT on any wages) | PwC WWTS Armenia, Corporate: Taxes on corporate income |
| Currency | Armenian dram (AMD); all withholding and Treasury payments in AMD | research key_rules |

## Section 13 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 catalogue table**

| # | Situation | Why it needs judgement | Action |
| --- | --- | --- | --- |
| T2-1 | Stamp-duty schedule for a specific pay period | Five-band (≤ 24 Dec 2025) vs two-band (≥ 25 Dec 2025); exact transition date/per-band amounts not pinned to primary text | Apply CD3 by payment date; flag `[RESEARCH GAP]`; confirm against the Law "On Stamp Payments" / SRC. |
| T2-2 | Health-insurance contribution applicability | Brand-new (effective 25 Dec 2025); commencement and overlap with other charges uncertain | Apply CD4 (only on/after 25 Dec 2025, gross > AMD 200,000); flag `[RESEARCH GAP]`. |
| T2-3 | Employee may be **pension-exempt** (born before 1 Jan 1974) | Eligibility depends on date of birth | Confirm DOB before dropping the pension line (CD2). |
| T2-4 | Net-to-gross gross-up requested | Non-linear (pension kink at AMD 500,000 + flat band charges) | Present as estimate; iterate; flag for adviser. |
| T2-5 | Bonus / commission / benefit-in-kind | Taxable as employment income, but band placement (stamp/health) shifts with total gross | Default: treat cash bonus as salary (20% PIT; recompute pension/stamp/health on total gross); flag non-cash items [T2]. |
| T2-6 | Worker may be self-employed / IE / micro-business | Wrong regime entirely (turnover tax / micro-business 0%) | Escalate [T3] — out of payroll scope. |
| T2-7 | Non-resident / posted / cross-border employee | Residency, treaty and social coordination apply | Confirm Armenian-source treatment; escalate complex cases [T3]. |
| T2-8 | State co-financing of the funded pension | One source mentions State co-financing; another downplays it | Payroll computes the employee-side withholding only; confirm transfer mechanics `[RESEARCH GAP]`. |
| T2-9 | Exact penalty amounts / Tax Code article numbers | Penalty figures sourced partly from a single law-firm source | Cross-check against Tax Code Articles 400--402 before relying. `[RESEARCH GAP]` |

## Section 14 -- Excel Working Paper Template

**Excel working paper template table**

| Cell ref | Label | Formula / source |
| --- | --- | --- |
| B1 | Pay period (month/year) | input |
| B2 | Payment date | input — drives deadline + which stamp/health schedule (25 Dec 2025 cutoff) |
| B3 | Gross salary (ashkhatavarts) | input |
| B4 | Pension-applicable? (1 = born on/after 1 Jan 1974, 0 = exempt) | input (CD2) |
| B5 | On/after 25 Dec 2025? (1 = yes, 0 = no) | input (CD3/CD4) |
| B6 | PIT (20%) | `=ROUND(B3*0.20,2)` |
| B7 | Funded pension | `=IF(B4=0,0,MIN(87500,IF(B3<500000,B3*0.05,B3*0.10-25000)))` |
| B8 | Stamp duty | `=IF(B5=1, IF(B3<=1000000,1000,15000), IF(B3<=100000,1500,IF(B3<=200000,3000,IF(B3<=500000,5500,IF(B3<=1000000,8500,15000)))))` |
| B9 | Health insurance | `=IF(B5=1, IF(B3<=200000,0,IF(B3<=500000,4800,10800)), 0)` |
| B10 | **Net pay** | `=B3-B6-B7-B8-B9` |
| B11 | **Total employer cost** | `=B3` (no employer social contribution — CD1) |
| B12 | Total to remit (PIT + pension + stamp + health) | `=B6+B7+B8+B9` |

Validation rows: confirm B10 + B6 + B7 + B8 + B9 = B3; confirm B7 ≤ 87,500; confirm B7 = ROUND(B3×0.05) when B3 < 500,000 (and = B3×0.10 − 25,000 when 500,000 ≤ B3 ≤ 1,125,000); confirm B11 = B3.

## Section 15 -- Bank Statement / Terminology Reading Guide

**Terminology reading guide table**

| Armenian term (transliterated) | English | Notes |
| --- | --- | --- |
| ashkhatavarts (աշխատավարձ) | salary / wage | gross unless context says net |
| avans / kankhik | advance / instalment | partial salary payment |
| premia / havelavchar | bonus / supplement | taxable as employment income |
| ekamtayin hark (եկամտային հարկ) | income tax | the 20% PIT |
| kensathoshak / kutakayin kensathoshak | (funded / accumulated) pension | the funded pension contribution |
| droshmanishayin vchar | stamp / military duty | the stamp payment |
| apahovagrakan vchar | insurance contribution | the (new) health-insurance contribution |
| HARK (ՀՀ ՊԵԿ) | tax (State Revenue Committee) | SRC remittance |
| TIN | taxpayer identification number | 8 digits |
| kankhik / cash | cash | cash withdrawal — exclude from payroll classification |
| nersktin pokhantsum | internal transfer | between client's own accounts — exclude |

**Conventions.** Major Armenian banks (Ameriabank, Ardshinbank, Acba Bank, Converse Bank, Inecobank, ID Bank) export CSV with various delimiters; dates DD.MM.YYYY or ISO depending on setting. Convert foreign-currency salaries to AMD at the Central Bank of Armenia (cba.am) rate on the relevant date.

## Section 16 -- Onboarding Fallback

If the engagement is mid-year or records are incomplete:

1. **No prior monthly returns on hand** → request the SRC e-portal filing history; reconcile each month's PIT/pension/stamp/health against bank remittances to the State Budget. Do not assume prior months were correct.
2. **Net-only history** → reconstruct gross via the gross-to-net order (Section 5). This is **non-linear** (pension kink at AMD 500,000 + flat band charges), so iterate and mark all reconstructed grosses as estimates [T2].
3. **Pension applicability unknown (DOB)** → default to **applies** (CD2) unless the employee was born before 1 Jan 1974; confirm before dropping the pension line.
4. **Pay periods straddling 25 Dec 2025** → split: pre-25 Dec uses five-band stamp + no health insurance; on/after 25 Dec uses two-band stamp + health insurance (CD3/CD4). Confirm transition date `[RESEARCH GAP]`.
5. **Worker type unclear (employee vs IE/micro-business)** → STOP and confirm; the IE/turnover/micro-business regimes are out of payroll scope [T3].

## Section 17 -- Reference Material

**Reference Material table**  _(PwC WWTS Armenia; Vardanyan & Partners; State Revenue Committee (src.am); RemotePeople)_

| Item | Value | Source |
| --- | --- | --- |
| PIT (salary) rate | 20% flat on gross; no allowance | PwC WWTS Armenia, Individual: Taxes on personal income |
| Funded pension (employee) | 5% if gross < AMD 500,000; 10% × gross − AMD 25,000 if ≥ AMD 500,000 | PwC WWTS Armenia, Individual: Other taxes |
| Funded pension max base / cap | AMD 1,125,000 base; AMD 87,500/month cap | PwC WWTS Armenia, Individual: Other taxes |
| Employer social/payroll tax | None (0%) | Vardanyan & Partners |
| Stamp duty (through 24 Dec 2025) | 5 bands: 1,500 / 3,000 / 5,500 / 8,500 / 15,000 | PwC WWTS Armenia, Individual: Other taxes |
| Stamp duty (from 25 Dec 2025) | AMD 1,000 (≤ 1,000,000) / AMD 15,000 (> 1,000,000) | PwC WWTS Armenia, Individual: Other taxes |
| Health insurance (from 25 Dec 2025) | 0 (≤ 200,000) / AMD 4,800 (200,001--500,000) / AMD 10,800 (> 500,000) | Vardanyan & Partners |
| Monthly return + payment deadline | 20th of the following month | PwC WWTS Armenia, Tax administration |
| Annual personal declaration (2025 income) | By 1 November 2026 (window shifts to 2 Mar -- 1 Jul from 2027 cycle) | PwC WWTS Armenia, Tax administration |
| Tax year | Calendar year | PwC WWTS Armenia, Tax administration |
| Minimum monthly wage | AMD 75,000 (2023--2025; AMD 85,000 discussed for 2026, unconfirmed) | RemotePeople (secondary) — `[RESEARCH GAP]` |
| Corporate income (profit) tax | 18% | PwC WWTS Armenia, Corporate: Taxes on corporate income |
| Standard VAT / registration threshold | 20% / AMD 115,000,000 annual turnover | PwC WWTS Armenia, Corporate: Other taxes |
| Micro-business exemption threshold | AMD 24,000,000 annual turnover | PwC WWTS Armenia, Corporate: Taxes on corporate income |
| Employer / employee TIN | 8 digits; register within 15 days via e-register.am | State Revenue Committee (src.am) |

- **PIT (salary) rate** — 20% flat on gross; no allowance  _(PwC WWTS Armenia, Individual: Taxes on personal income)_
- **Funded pension (employee)** — 5% if gross < AMD 500,000; 10% × gross − AMD 25,000 if ≥ AMD 500,000  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Funded pension max base / cap** — AMD 1,125,000 base; AMD 87,500/month cap  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Employer social/payroll tax** — None (0%)  _(Vardanyan & Partners)_

**Stamp duty (through 24 Dec 2025)**  _(PwC WWTS Armenia, Individual: Other taxes)_

5 bands: 1,500 / 3,000 / 5,500 / 8,500 / 15,000

- **Stamp duty (from 25 Dec 2025)** — AMD 1,000 (≤ 1,000,000) / AMD 15,000 (> 1,000,000)  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Health insurance (from 25 Dec 2025)** — 0 (≤ 200,000) / AMD 4,800 (200,001--500,000) / AMD 10,800 (> 500,000)  _(Vardanyan & Partners)_
- **Monthly return + payment deadline** — 20th of the following month  _(PwC WWTS Armenia, Tax administration)_
- **Annual personal declaration (2025 income)** — By 1 November 2026 (window shifts to 2 Mar -- 1 Jul from 2027 cycle)  _(PwC WWTS Armenia, Tax administration)_
- **Tax year** — Calendar year  _(PwC WWTS Armenia, Tax administration)_
- **Minimum monthly wage** — AMD 75,000 (2023--2025; AMD 85,000 discussed for 2026, unconfirmed)  _(RemotePeople (secondary) — `[RESEARCH GAP]`)_
- **Corporate income (profit) tax** — 18%  _(PwC WWTS Armenia, Corporate: Taxes on corporate income)_
- **Standard VAT / registration threshold** — 20% / AMD 115,000,000 annual turnover  _(PwC WWTS Armenia, Corporate: Other taxes)_
- **Micro-business exemption threshold** — AMD 24,000,000 annual turnover  _(PwC WWTS Armenia, Corporate: Taxes on corporate income)_
- **Employer / employee TIN** — 8 digits; register within 15 days via e-register.am  _(State Revenue Committee (src.am))_

### Penalties [T2]

**[RESEARCH GAP — reviewer to confirm].** Non-filing and corporate late-return figures come partly from a single law-firm source; cross-check against Tax Code Articles 400--402. Source: research caveat.

**Penalties table**  _(Regfollower / Orbitax; Tax Code Art. 401; Vardanyan & Partners)_

| Violation | Amount / rate | Source |
| --- | --- | --- |
| Late payment / late remittance of withheld amounts | **0.075% per calendar day** of the unpaid tax, up to a maximum of **730 days** (Tax Code Art. 401; 0.075% rate effective 1 Jan 2025, raised from the COVID-era 0.04%) | Regfollower / Orbitax; Tax Code Art. 401 |
| Failure to file personal income declaration | Flat fine: **AMD 5,000** for most individuals; **AMD 50,000** for entrepreneurs / major participants | Vardanyan & Partners — `[RESEARCH GAP]` |
| Late corporate tax return | **5% of unpaid tax per 15-day period** of delay, capped at the total tax liability | Vardanyan & Partners — `[RESEARCH GAP]` |

- **Late payment / late remittance of withheld amounts** — **0.075% per calendar day** of the unpaid tax, up to a maximum of **730 days** (Tax Code Art. 401; 0.075% rate effective 1 Jan 2025, raised from the COVID-era 0.04%)  _(Regfollower / Orbitax; Tax Code Art. 401)_
- **Failure to file personal income declaration** — Flat fine: **AMD 5,000** for most individuals; **AMD 50,000** for entrepreneurs / major participants  _(Vardanyan & Partners — `[RESEARCH GAP]`)_
- **Late corporate tax return** — **5% of unpaid tax per 15-day period** of delay, capped at the total tax liability  _(Vardanyan & Partners — `[RESEARCH GAP]`)_

### Authorities and legislation

- **State Revenue Committee of the Republic of Armenia (SRC)** — src.am; monthly payroll return filed via the SRC e-portal; TIN / business registration via e-Register (e-register.am).
- **Tax Code of the Republic of Armenia** (Law HO-165-N, in force from 2018, as amended) — PIT withholding, declarations, penalties (Arts. 400--402).
- **Law "On Funded Pensions"** — mandatory funded pension.
- **Law "On Stamp Payments"** — military / stamp duty.

### Sources

1. PwC Worldwide Tax Summaries — Armenia, Individual: Taxes on personal income (reviewed 5 Feb 2026). https://taxsummaries.pwc.com/armenia/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Armenia, Individual: Other taxes (funded pension, stamp duty). https://taxsummaries.pwc.com/armenia/individual/other-taxes
3. PwC Worldwide Tax Summaries — Armenia, Individual: Tax administration. https://taxsummaries.pwc.com/armenia/individual/tax-administration
4. PwC Worldwide Tax Summaries — Armenia, Corporate: Taxes on corporate income (18% CIT; micro-business). https://taxsummaries.pwc.com/armenia/corporate/taxes-on-corporate-income
5. PwC Worldwide Tax Summaries — Armenia, Corporate: Other taxes (VAT; AMD 115,000,000 threshold). https://taxsummaries.pwc.com/armenia/corporate/other-taxes
6. Vardanyan & Partners — "Taxes in Armenia 2026: Rates & Guide for Foreigners" (no employer contribution; health insurance). https://armenian-lawyer.com/taxes-armenia/
7. Vardanyan & Partners — "Armenian Payroll Tax Guide: Income, Pension & Military Duty Requirements." https://armenian-lawyer.com/business-immigration/armenian-payroll-tax-withholding-social-security-guide/
8. Vardanyan & Partners — "Armenia Tax Filing Deadlines & Compliance Guide 2025" (penalties). https://armenian-lawyer.com/business-immigration/armenia-tax-filing-deadlines-compliance-guide-2025/
9. Regfollower / Orbitax — "Armenia increases late payment interest rate" (0.075%/day from 1 Jan 2025). https://regfollower.com/armenia-increases-late-payment-interest-rate/
10. State Revenue Committee of Armenia — TIN / e-Register (official). https://www.src.am/en/getMenusContents/110
11. RemotePeople — "Minimum Wage in Armenia for 2025 (AMD 75,000)" (secondary aggregator). https://remotepeople.com/countries/armenia/hire-employees/minimum-wage/

> **Reviewer note on tax year / regime split.** PwC pages were last reviewed 5 February 2026 and explicitly cover the 2025 tax year. The stamp-duty simplification (two bands) and the new employee health-insurance contribution both take effect **25 December 2025** — confirm the exact transition date and whether the health-insurance charge is operationally a 2026 item before applying to any specific pay period. Source: research caveat.

## Section 18 -- Test Suite

Each test states inputs and the recomputed expected output. Reviewers should rerun every figure. All amounts in AMD. Unless stated, employee is **born on/after 1 Jan 1974** and the period is **pre-25 Dec 2025** (five-band stamp, no health insurance).

### Test 1 -- Standard salary, below kink

**Input:** Gross AMD 300,000, paid June 2025.
**Expected:** PIT 60,000. Pension 15,000 (5%). Stamp 5,500. Health 0. **Net 219,500.** Employer cost 300,000. Total to remit 80,500.

### Test 2 -- Low salary

**Input:** Gross AMD 150,000, paid May 2025.
**Expected:** PIT 30,000. Pension 7,500 (5%). Stamp 3,000. Health 0. **Net 109,500** (no tax-free allowance). Employer cost 150,000. Total to remit 40,500.

### Test 3 -- Above the AMD 500,000 kink

**Input:** Gross AMD 600,000, paid April 2025.
**Expected:** PIT 120,000. Pension 35,000 (= 60,000 − 25,000). Stamp 8,500. Health 0. **Net 436,500.** Employer cost 600,000. Total to remit 163,500.

### Test 4 -- Pension cap (gross above AMD 1,125,000 base)

**Input:** Gross AMD 1,200,000, paid March 2025.
**Expected:** PIT 240,000. Pension **87,500** (capped — NOT 95,000). Stamp 15,000. Health 0. **Net 857,500.** Employer cost 1,200,000. Total to remit 342,500.

### Test 5 -- Minimum wage

**Input:** Gross AMD 75,000, paid February 2025.
**Expected:** PIT 15,000. Pension 3,750 (5%). Stamp 1,500. Health 0. **Net 54,750.** Employer cost 75,000. Total to remit 20,250.

### Test 6 -- Pension-exempt (born before 1 Jan 1974)

**Input:** Gross AMD 400,000, paid June 2025, born 1970.
**Expected:** PIT 80,000. Pension **0** (exempt). Stamp 5,500. Health 0. **Net 314,500.** Employer cost 400,000. Total to remit 85,500.

### Test 7 -- Late-Dec-2025 / 2026 basis (two-band stamp + health insurance)

**Input:** Gross AMD 600,000, paid 28 December 2025.
**Expected:** PIT 120,000. Pension 35,000. Stamp **1,000** (two-band, ≤ 1,000,000). Health **10,800** (above 500,000). **Net 433,200.** Employer cost 600,000. Total to remit 166,800. Flag CD3/CD4 transition `[RESEARCH GAP]`.

### Test 8 -- Continuity at the kink

**Input:** Gross exactly AMD 500,000, pre-25 Dec 2025.
**Expected:** Pension under 5% rule would be 25,000; under 10%−25,000 rule = 50,000 − 25,000 = 25,000 — **identical** (formula continuous). PIT 100,000. Stamp 5,500 (200,001--500,000 band). Health 0. **Net 369,500.** Employer cost 500,000.

### Test 9 -- No employer social contribution guard

**Input:** Any gross; question asks "what is the employer's social-security cost?"
**Expected:** Employer social/payroll contribution = **0** — there is no separate employer social-security or payroll tax in Armenia. Employer cash cost = gross salary only [T1].

### Test 10 -- Wrong jurisdiction / wrong income type guard

**Input:** Request references a dividend, royalty or a different country.
**Expected:** REFUSE for payroll — dividends (5%), royalties (10%), lease (10%) are separate withholding regimes [T3]; a different country is the wrong skill [T3].

## PROHIBITIONS

- **No allowance / progressive PIT** — NEVER apply a tax-free personal allowance or progressive bands to Armenian salary PIT — it is a **flat 20%** from the first dram.  _(Section 17 -- Reference Material)_
- **No employer social security/payroll tax (CD1)** — NEVER add an employer social-security or payroll tax — there is **no separate employer contribution** in Armenia; the employer's only payroll cost is the gross salary (CD1).  _(Vardanyan & Partners)_
- **Pension exemption for pre-1974 born (CD2)** — NEVER apply the funded pension to an employee **born before 1 Jan 1974** without confirming they opted in — they are otherwise exempt (CD2).  _(Section 17 -- Reference Material)_
- **Pension cap** — NEVER exceed the funded-pension cap of **AMD 87,500/month** (max base AMD 1,125,000) for a high earner.  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Correct stamp-duty schedule (CD3)** — NEVER use the wrong stamp-duty schedule — five-band through 24 Dec 2025, two-band from 25 Dec 2025 (CD3); confirm the transition date `[RESEARCH GAP]`.  _(PwC WWTS Armenia, Individual: Other taxes)_
- **Health insurance timing/threshold (CD4)** — NEVER apply the employee health-insurance contribution to wages paid **before 25 Dec 2025** or to gross **≤ AMD 200,000** (CD4).  _(Vardanyan & Partners)_
- **Flat band amounts, not percentage** — NEVER treat stamp duty or health insurance as a percentage — they are **flat band amounts**.  _(Section 17 -- Reference Material)_
- **Filing deadline** — NEVER miss the monthly return + payment deadline (**20th of the following month**) on the SRC e-portal.  _(PwC WWTS Armenia, Tax administration)_
- **Out-of-scope regimes (T3)** — NEVER apply the micro-business / turnover / self-employed regimes to an employee's payroll — those are out of payroll scope [T3].  _(Section 17 -- Reference Material)_
- **Research gap guard** — NEVER guess any figure marked `[RESEARCH GAP — reviewer to confirm]` — verify against src.am / the relevant statute.  _(Section 17 -- Reference Material)_
- **Not definitive advice** — NEVER present payroll computations as definitive — always label as estimated and direct to a qualified Armenian tax adviser / licensed accountant.  _(Disclaimer)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a qualified Armenian tax adviser or licensed accountant in Armenia) before implementation.

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
