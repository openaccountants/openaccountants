---
name: slovenia-payroll
description: Use this skill whenever asked about Slovenia payroll processing for employed persons. Trigger on phrases like "Slovenia payroll", "Slovenian payroll", "akontacija dohodnine", "dohodnina withholding", "REK-O", "REK obrazec", "prispevki ZPIZ", "social contributions Slovenia", "ZZZS contributions", "long-term care contribution Slovenia", "ZDOsk", "splošna olajšava", "minimalna plača", "minimum wage Slovenia", "bruto plača", "neto plača", "net salary Slovenia", "gross to net Slovenia", "employer SSC Slovenia", "FURS payroll", "eDavki", "salary calculation Slovenia", or any question about computing employee pay, withholding income tax, or social security contributions for Slovenia-based employees. This skill covers progressive PIT withholding (akontacija dohodnine), employee and employer social security contributions (ZPIZ pension, ZZZS health, unemployment, parental, injury-at-work), the new long-term care contribution (ZDOsk-1, from 1 July 2025), the flat compulsory health contribution, minimum wage, the general tax allowance, and REK-O filing obligations. ALWAYS read this skill before processing any Slovenia payroll.
version: 0.1
jurisdiction: SI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovenia Payroll

## Slovenia Payroll Skill v0.1

> **Tier 2 — research-verified, NOT yet accountant-verified.** Several figures rely on Big-4 (PwC/KPMG) and aggregator summaries rather than FURS primary documents. Items marked **[RESEARCH GAP — reviewer to confirm]** require a licensed Slovenian accountant (davčni svetovalec / pooblaščeni računovodja) to confirm against FURS/ZPIZ/ZZZS primary sources before reliance. Research confidence: **medium**.

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Slovenia (Republic of Slovenia / Republika Slovenija) |
| Currency | EUR only |
| Standard pay frequency | Monthly (most common); paid by the agreed pay date |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax | Progressive personal income tax (dohodnina), 5 brackets 16% / 26% / 33% / 39% / 50% [PwC] |
| Tax withholding system | Monthly advance withholding at source (akontacija dohodnine) by employer [FURS] |
| Tax authority | Financial Administration of the Republic of Slovenia (FURS / Finančna uprava RS) |
| Social security administrators | ZPIZ (pension/disability); ZZZS (health + long-term care); contributions collected via FURS [PwC] |
| Filing portal | eDavki (edavki.durs.si) |
| Primary payroll return | REK-O (Obračun davčnih odtegljajev), filed on the day of payment [FURS] |
| Key legislation | ZDoh-2 (PIT); ZPIZ-2 (pension/disability); ZZVZZ (health); ZDOsk-1 (long-term care, LTC contribution from 1 Jul 2025); ZPSV (social-security contributions) |
| Validated by | Pending -- requires sign-off by a licensed Slovenian accountant |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (Akontacija Dohodnine)

The employer withholds personal income tax (dohodnina) monthly at source as an advance (akontacija) on employment income, applying the monthly portion of the general allowance (splošna olajšava) and any registered personal reliefs. The advance is computed on the FURS monthly schedule and reconciled annually by FURS [FURS — dohodnina, dohodek iz zaposlitve].

### Progressive PIT Rate Table (2025)

**Progressive PIT Rate Table (2025)**  _(PwC Worldwide Tax Summaries / FURS dohodninska lestvica 2025)_

| Bracket | Taxable Base (EUR) | Marginal Rate | Cumulative Tax at Lower Bound (EUR) |
| --- | --- | --- | --- |
| 1 | 0 -- 9,210.26 | 16% | 0 |
| 2 | 9,210.26 -- 27,089 | 26% | 1,473.64 |
| 3 | 27,089 -- 54,178 | 33% | 6,122.11 |
| 4 | 54,178 -- 78,016.32 | 39% | 15,061.48 |
| 5 | over 78,016.32 | 50% | 24,358.43 |

**Cumulative-tax self-check (recomputed):**
- B1 top: 9,210.26 x 16% = 1,473.64 ✓
- B2 top: 1,473.64 + (27,089 − 9,210.26) x 26% = 1,473.64 + 4,648.47 = 6,122.11 ✓
- B3 top: 6,122.11 + (54,178 − 27,089) x 33% = 6,122.11 + 8,939.37 = 15,061.48 ✓
- B4 top: 15,061.48 + (78,016.32 − 54,178) x 39% = 15,061.48 + 9,296.94 = 24,358.42 (≈ 24,358.43, rounding) ✓

### Progressive PIT Rate Table (2026, indexed)

**Progressive PIT Rate Table (2026, indexed)**  _(Orbitax (Slovenia Personal Income Tax Brackets and Relief for 2026))_

| Bracket | Taxable Base (EUR) | Marginal Rate |
| --- | --- | --- |
| 1 | 0 -- 9,721.43 | 16% |
| 2 | 9,721.43 -- 28,592.44 | 26% |
| 3 | 28,592.44 -- 57,184.88 | 33% |
| 4 | 57,184.88 -- 82,346.23 | 39% |
| 5 | over 82,346.23 | 50% |

### General Allowance (Splošna Olajšava)

**General Allowance table**  _(PwC Slovenia Deductions)_

| Item | Value (EUR) | Source |
| --- | --- | --- |
| Base general allowance (annual) | 5,000 | PwC Slovenia Deductions |
| Additional low-earner linear allowance | **[RESEARCH GAP — reviewer to confirm]** — for low earners an additional linear allowance applies; the 2025 threshold/formula reported around income up to EUR 16,832 with formula `19,736.99 − 1.17259 x annual income` is **unverified against the FURS primary document** | WebSearch (FURS olajšave 2025) — NOT verified |

> Do **not** assume a higher EUR 5,260 base figure; it was not confirmed and is likely a different year. Use EUR 5,000 base unless a reviewer confirms otherwise against FURS.

### Withholding Method

- **Withholding method** — For monthly withholding the employer applies the FURS monthly schedule: take the monthly gross, deduct employee social contributions, deduct 1/12 of the applicable annual general allowance (and any registered reliefs), and apply the progressive scale (annualised or via the FURS monthly table). The 0% band does not exist in Slovenia — the lowest bracket is 16%; the tax-free effect comes from the general allowance, not a zero-rate band. FURS issues an annual informative income-tax calculation (informativni izračun dohodnine) reconciling withheld advances against final liability.  _([FURS])_

### Out of Scope (schedular income)

- **Capital income schedular treatment** — Capital income (interest, dividends, capital gains, rental) is taxed schedularly at a flat 25% (capital gains rate reduces with holding period), outside the progressive wage scale. Do not run capital income through the payroll progressive brackets.  _([PwC])_

## Section 3 -- Social Security -- Employee Deductions

Employee social security contributions are deducted from gross employment income (bruto plača). Employee contributions on employment income are **uncapped** (no ceiling); the 3.5x-average-wage maximum base applies to self-employed only (see Section 5 / Section 11) [KPMG Flash Alert 2025-133; ZPIZ-2].

### Employee Contribution Rates (2025)

**Employee Contribution Rates (2025)**  _(PwC Worldwide Tax Summaries — Slovenia Other taxes; long-term care row per KPMG Flash Alert 2025-133 / ZDOsk-1)_

| Contribution | Administrator | Rate | Notes |
| --- | --- | --- | --- |
| Pension and disability insurance | ZPIZ | 15.50% | gross employment income |
| Compulsory health insurance | ZZZS | 6.36% | gross employment income |
| Unemployment insurance | — | 0.14% | gross employment income |
| Parental protection insurance | — | 0.10% | gross employment income |
| **Subtotal (before LTC)** |  | **22.10%** | applies to payrolls before 1 Jul 2025 |
| Long-term care (LTC) contribution | ZZZS (ZDOsk-1) | 1.00% | **NEW from 1 July 2025** |
| **TOTAL (from 1 Jul 2025, incl. LTC)** |  | **23.10%** | applies to payrolls from 1 Jul 2025 |

**Employee total self-check (recomputed):** 15.50 + 6.36 + 0.14 + 0.10 = 22.10 ✓; + 1.00 LTC = 23.10 ✓

> **Date split is mandatory.** Payrolls dated before 1 July 2025 use 22.10%; payrolls dated on/after 1 July 2025 use 23.10% (the extra 1% is the LTC contribution) [KPMG Flash Alert 2025-133; ZDOsk-1].

### Separate Flat Compulsory Health Contribution (CHC / OZZ replacement)

**Separate Flat Compulsory Health Contribution table**  _(PwC; WebSearch summary)_

| Period (2025) | Monthly amount (EUR) | Source |
| --- | --- | --- |
| January -- February 2025 | 35.00 | PwC; WebSearch summary |
| 1 March 2025 -- end 2025 | 37.17 | PwC; WebSearch summary |

A separate flat per-capita Compulsory Health Contribution is deducted from insured individuals (not a percentage of wage).

> **[RESEARCH GAP — reviewer to confirm]** The CHC amounts and **who remits it** (employer-deducted vs. employee self-pay) come from a secondary search summary and should be verified against ZZZS. The worked examples below show it as a separate deduction line and flag it.

## Section 4 -- Social Security -- Employer Contributions

Employer social security contributions are paid on top of gross employment income. Source: PwC Worldwide Tax Summaries; long-term care row per KPMG Flash Alert 2025-133 / ZDOsk-1.

### Employer Contribution Rates (2025)

**Employer Contribution Rates (2025)**  _(PwC Worldwide Tax Summaries; long-term care row per KPMG Flash Alert 2025-133 / ZDOsk-1)_

| Contribution | Administrator | Rate | Notes |
| --- | --- | --- | --- |
| Pension and disability insurance | ZPIZ | 8.85% | gross employment income |
| Compulsory health insurance | ZZZS | 6.56% | gross employment income |
| Injury at work / occupational disease | — | 0.53% | employer only |
| Unemployment insurance | — | 0.06% | gross employment income |
| Parental protection insurance | — | 0.10% | gross employment income |
| **Subtotal (before LTC)** |  | **16.10%** | applies to payrolls before 1 Jul 2025 |
| Long-term care (LTC) contribution | ZZZS (ZDOsk-1) | 1.00% | **NEW from 1 July 2025** |
| **TOTAL (from 1 Jul 2025, incl. LTC)** |  | **17.10%** | applies to payrolls from 1 Jul 2025 |

**Employer total self-check (recomputed):** 8.85 + 6.56 + 0.53 + 0.06 + 0.10 = 16.10 ✓; + 1.00 LTC = 17.10 ✓

**Combined contribution wedge (from 1 Jul 2025):** employee 23.10% + employer 17.10% = 40.20% of gross [PwC + KPMG].

## Section 5 -- Minimum Wage and Contribution Bases

### National Minimum Wage (Minimalna Plača), Gross Monthly

**National Minimum Wage table**  _(WageIndicator / SeeNews; RRA Koroška)_

| Year | Gross Monthly (EUR) | Source |
| --- | --- | --- |
| 2025 | 1,277.72 | WageIndicator / SeeNews |
| 2026 | 1,481.88 | RRA Koroška (+15.99%) |

### Reference Wages and Bases

**Reference Wages and Bases table**  _(WebSearch summary; ZPIZ-2)_

| Item | Value (EUR) | Notes | Source |
| --- | --- | --- | --- |
| Average monthly gross salary (contribution-base anchor) | 2,536.03 (2025) | used mainly for self-employed base calc | WebSearch summary **[RESEARCH GAP — reviewer to confirm]** |
| Minimum contribution base (≈60% of avg gross wage) | 1,521.62 (2025) | primarily self-employed | WebSearch summary; ZPIZ-2 **[RESEARCH GAP — reviewer to confirm]** |
| Maximum contribution base (3.5x avg wage) | 8,876.11 (2025) | **self-employed only**; employee wage contributions are uncapped | WebSearch summary; ZPIZ-2 **[RESEARCH GAP — reviewer to confirm]** |

> Working-time, overtime premia, and statutory leave entitlements are governed by the Employment Relationships Act (ZDR-1) and applicable collective agreements (kolektivne pogodbe). Specific overtime multipliers and leave-day counts were **not** captured at figure level in this research. **[RESEARCH GAP — reviewer to confirm]** the applicable overtime rate, weekly hours cap, and minimum annual leave under ZDR-1 / the relevant collective agreement before relying on them.

## Section 6 -- Conservative Defaults

**Conservative Defaults table**  _([KPMG Flash Alert 2025-133; PwC])_

| Assumption | Conservative default |
| --- | --- |
| Employee social contribution rate | Use **23.10%** for payrolls from 1 July 2025 onward (incl. 1% LTC); **22.10%** before that date [KPMG] |
| Employer social contribution rate | Use **17.10%** for payrolls from 1 July 2025 onward (incl. 1% LTC); **16.10%** before that date [KPMG] |
| Employee contribution ceiling | Treat employee contributions as **uncapped** on gross wage (no ceiling for employees); the 3.5x cap applies to self-employed only [KPMG; ZPIZ-2] |
| General allowance | Apply **EUR 5,000** base general allowance plus the low-earner additional allowance where the employee qualifies; do **not** assume EUR 5,260 [PwC] |
| Date split | If the pay date is unknown but the period spans 1 July 2025, **ask** rather than guess; the LTC 1%+1% only applies from that date |
| CHC flat contribution | Treat the EUR 37.17/month (from 1 Mar 2025) as a separate deduction line and flag remittance responsibility as unconfirmed |
| PIT brackets | Use 2025 brackets for 2025 pay dates; 2026 indexed brackets for 2026 pay dates |

## Section 7 -- Required Inputs + Refusal Catalogue

### Required Inputs

- **Required inputs before computing a payslip** — Before computing any Slovenia payslip, you MUST have: 1. Gross monthly salary (bruto plača) in EUR; 2. Pay date (determines 2025 vs 2026 brackets AND pre/post 1 July 2025 LTC rate); 3. Tax residency (resident vs non-resident — affects allowance entitlement); 4. General allowance eligibility (is the employee a low earner qualifying for the additional linear allowance?); 5. Registered personal reliefs (dependants, disability, etc., as registered with FURS); 6. Whether the flat CHC is employer-deducted for this employee.

### Refusal Catalogue — refuse or flag, do not guess

**Refusal Catalogue table**

| Situation | Action |
| --- | --- |
| No pay date given | REFUSE to pick a contribution rate — ask whether the pay date is before or from 1 July 2025 |
| Pay date in 2026 but only 2025 brackets requested | Use 2026 indexed brackets; flag the switch |
| Employee claims a EUR 5,260 general allowance | Decline; use EUR 5,000 unless reviewer confirms |
| Request to cap employee contributions at EUR 8,876.11 | Decline — that cap is self-employed only; employee contributions are uncapped |
| Request to apply a 0% tax band | Decline — Slovenia's lowest band is 16%; the relief is the general allowance, not a 0% bracket |
| Capital/dividend/rental income mixed into the wage base | Separate it — that is schedular 25% income, not progressive wage income |
| Exact statutory penalty figure requested | State that fine bands are in ZDavP-2 / ZPSV and were not captured at figure level — flag as research gap |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Slovenian bank-statement narratives. Match on the Slovenian (and common English) keywords.

### Salary Credits (employee receiving pay)

**Salary Credits table**

| Bank narrative pattern (SI) | Classification |
| --- | --- |
| PLAČA, NETO PLAČA, IZPLAČILO PLAČE | Net salary payment |
| AKONTACIJA PLAČE | Salary advance |
| REGRES, REGRES ZA LETNI DOPUST | Holiday allowance (regres) — see leave note |
| POVRAČILO STROŠKOV, PREVOZ, MALICA | Expense reimbursement (transport / meal allowance) — generally not wage income |
| BOŽIČNICA, 13. PLAČA | Christmas / 13th-month bonus (taxable) |

### Employer Debits (employer paying obligations)

**Employer Debits table**

| Bank narrative pattern (SI) | Classification |
| --- | --- |
| FURS, DOHODNINA, AKONTACIJA DOHODNINE | Withheld income tax remittance to FURS |
| PRISPEVKI, ZPIZ, PRISPEVEK PIZ | Pension/disability contribution (ZPIZ) |
| ZZZS, PRISPEVEK ZA ZDRAVSTVO | Health insurance contribution (ZZZS) |
| DOLGOTRAJNA OSKRBA, ZDOsk, LTC | Long-term care contribution (from 1 Jul 2025) |
| PRISPEVEK ZA ZAPOSLOVANJE | Unemployment insurance contribution |
| STARŠEVSKO VARSTVO | Parental protection contribution |
| OBVEZNI ZDRAVSTVENI PRISPEVEK, OZZ, CHC | Flat compulsory health contribution |
| NETO PLAČE, IZPLAČILO PLAČ | Net wages disbursement to employees |
| eDavki, REK-O | Payroll return filing / linked payment reference |

## Section 9 -- Worked Examples

> All examples assume a **resident, single** employee with only the **EUR 5,000 base** general allowance (no additional low-earner allowance modelled — see the research gap in Section 2), monthly pay, and the FURS schedule approximated by annualising the monthly taxable base. Figures are recomputed end-to-end and reconcile to the cent. They are **estimates** for illustration; a reviewer must confirm the exact FURS monthly-schedule treatment and the additional allowance.

Convention used in every example:
- `monthly general allowance = 5,000 / 12 = 416.67`
- `monthly PIT base = gross − employee SSC − 416.67`
- `annual PIT base = monthly PIT base x 12`, taxed on the bracket table, then `÷ 12` for the month
- CHC shown separately at EUR 37.17/month (from 1 Mar 2025) where applicable

### Example 1 — EUR 2,000 gross, pay date in/after July 2025 (LTC applies)

Bank line: `IZPLAČILO PLAČE — EUR 1,323.21` (before CHC)

**Example 1 worked table**

| Step | Amount (EUR) |
| --- | --- |
| Gross monthly | 2,000.00 |
| Employee SSC @ 23.10% | 462.00 |
| — pension 15.50% / health 6.36% / unemp 0.14% / parental 0.10% / LTC 1.00% | 310.00 / 127.20 / 2.80 / 2.00 / 20.00 |
| Less monthly general allowance | (416.67) |
| Monthly PIT base | 1,121.33 |
| Annual PIT base (x12) | 13,455.96 |
| Annual PIT (B2: 1,473.64 + (13,455.96 − 9,210.26) x 26%) | 2,577.52 |
| Monthly PIT (÷12) | 214.79 |
| **Net before CHC** (2,000 − 462.00 − 214.79) | **1,323.21** |
| Less flat CHC | (37.17) |
| **Net after CHC** | **1,286.04** |
| Employer SSC @ 17.10% | 342.00 |
| **Total employer cost** (2,000 + 342.00) | **2,342.00** |

### Example 2 — Minimum wage, EUR 1,277.72 gross, pay date from July 2025

**Example 2 worked table**

| Step | Amount (EUR) |
| --- | --- |
| Gross monthly | 1,277.72 |
| Employee SSC @ 23.10% | 295.15 |
| Less monthly general allowance | (416.67) |
| Monthly PIT base | 565.90 |
| Annual PIT base (x12) | 6,790.80 |
| Annual PIT (B1: 6,790.80 x 16%) | 1,086.53 |
| Monthly PIT (÷12) | 90.54 |
| **Net before CHC** | **892.03** |
| Less flat CHC | (37.17) |
| **Net after CHC** | **854.86** |
| Employer SSC @ 17.10% | 218.49 |
| **Total employer cost** | **1,496.21** |

### Example 3 — EUR 3,500 gross, pay date from July 2025 (crosses into 33% band annually)

**Example 3 worked table**

| Step | Amount (EUR) |
| --- | --- |
| Gross monthly | 3,500.00 |
| Employee SSC @ 23.10% | 808.50 |
| Less monthly general allowance | (416.67) |
| Monthly PIT base | 2,274.83 |
| Annual PIT base (x12) | 27,297.96 |
| Annual PIT (B3: 6,122.11 + (27,297.96 − 27,089) x 33%) | 6,191.07 |
| Monthly PIT (÷12) | 515.92 |
| **Net before CHC** | **2,175.58** |
| Less flat CHC | (37.17) |
| **Net after CHC** | **2,138.41** |
| Employer SSC @ 17.10% | 598.50 |
| **Total employer cost** | **4,098.50** |

### Example 4 — EUR 6,500 gross, pay date from July 2025 (into 39% band annually)

**Example 4 worked table**

| Step | Amount (EUR) |
| --- | --- |
| Gross monthly | 6,500.00 |
| Employee SSC @ 23.10% | 1,501.50 |
| Less monthly general allowance | (416.67) |
| Monthly PIT base | 4,581.83 |
| Annual PIT base (x12) | 54,981.96 |
| Annual PIT (B4: 15,061.48 + (54,981.96 − 54,178) x 39%) | 15,375.02 |
| Monthly PIT (÷12) | 1,281.25 |
| **Net before CHC** | **3,717.25** |
| Less flat CHC | (37.17) |
| **Net after CHC** | **3,680.08** |
| Employer SSC @ 17.10% | 1,111.50 |
| **Total employer cost** | **7,611.50** |

### Example 5 — EUR 2,000 gross, pay date Jan-Feb 2025 (PRE-LTC; date-split demonstration)

Demonstrates the mandatory date split: pre-1-July rates 22.10% / 16.10% and CHC EUR 35.00.

**Example 5 worked table**

| Step | Amount (EUR) |
| --- | --- |
| Gross monthly | 2,000.00 |
| Employee SSC @ 22.10% | 442.00 |
| Less monthly general allowance | (416.67) |
| Monthly PIT base | 1,141.33 |
| Annual PIT base (x12) | 13,695.96 |
| Annual PIT (B2: 1,473.64 + (13,695.96 − 9,210.26) x 26%) | 2,639.92 |
| Monthly PIT (÷12) | 219.99 |
| **Net before CHC** | **1,338.01** |
| Less flat CHC (Jan-Feb 2025) | (35.00) |
| **Net after CHC** | **1,303.01** |
| Employer SSC @ 16.10% | 322.00 |
| **Total employer cost** | **2,322.00** |

> Compare Examples 1 and 5: the same EUR 2,000 gross yields a different net and employer cost solely because of the 1 July 2025 LTC contribution. Always confirm the pay date.

## Section 10 -- Tier 1 Rules (Deterministic)

- **Tier 1 deterministic rules** — These rules are mechanical and should be applied without reviewer judgement. 1. Apply the 2025 PIT brackets (Section 2) for 2025 pay dates; the 2026 indexed brackets for 2026 pay dates [PwC; Orbitax]. 2. Employee social contributions = 22.10% before 1 Jul 2025, 23.10% from 1 Jul 2025 (incl. 1% LTC) [PwC; KPMG]. 3. Employer social contributions = 16.10% before 1 Jul 2025, 17.10% from 1 Jul 2025 (incl. 1% LTC) [PwC; KPMG]. 4. Compute the PIT base as gross minus employee social contributions minus the monthly portion of the general allowance and registered reliefs [FURS]. 5. Slovenia has no 0% tax band — the lowest marginal rate is 16%; relief comes from the general allowance [PwC]. 6. Employee wage contributions are uncapped — never apply the EUR 8,876.11 (3.5x) cap to an employee [KPMG; ZPIZ-2]. 7. Capital income (dividends/interest/gains/rental) is flat 25% schedular, never run through the progressive wage scale [PwC]. 8. File REK-O electronically via eDavki on the day of payment of employment income; remit tax and contributions on/around the pay date [FURS]. 9. Minimum gross monthly wage: EUR 1,277.72 (2025), EUR 1,481.88 (2026) — never compute a regular full-time gross below this [WageIndicator; RRA Koroška]. 10. The flat CHC is EUR 35.00/month (Jan-Feb 2025) then EUR 37.17/month (from 1 Mar 2025), a per-capita amount, not a percentage [PwC].  _([PwC; KPMG; FURS; Orbitax; WageIndicator; RRA Koroška])_

## Section 11 -- Tier 2 Catalogue (Reviewer Judgement Required)

**Tier 2 Catalogue table**

| Item | Why it needs judgement |
| --- | --- |
| Additional low-earner general allowance | Formula/threshold unverified against FURS; affects net pay materially [RESEARCH GAP] |
| Exact FURS monthly withholding schedule | This skill annualises the monthly base as an approximation; the official FURS monthly table may differ at the margins |
| Self-employed contribution bases | Min base EUR 1,521.62 (60%), max base EUR 8,876.11 (3.5x), avg wage EUR 2,536.03 — sourced from search summaries / ZPIZ-2 [RESEARCH GAP] |
| CHC remittance responsibility | Whether employer deducts and remits the flat CHC, or the individual self-pays [RESEARCH GAP] |
| Penalty / fine bands | ZDavP-2 / ZPSV figures not captured at statutory amount level [RESEARCH GAP] |
| Overtime, leave, regres (holiday allowance) treatment | Governed by ZDR-1 + collective agreements; not captured at figure level [RESEARCH GAP] |
| Non-resident treatment | Allowance entitlement and treaty relief for non-residents not modelled here |
| Corporate income tax interaction | 19% standard, with reported temporary increase to 22% for 2025-2028 (verify) — out of payroll scope but flagged [RESEARCH GAP] |

## Section 12 -- Excel Working Paper Template

**Excel Working Paper Template table**

| Col | Header | Formula / Source |
| --- | --- | --- |
| A | Employee | input |
| B | Pay date | input (drives bracket year + LTC split) |
| C | Gross monthly (bruto plača) | input |
| D | Employee SSC rate | `=IF(B>=DATE(2025,7,1),0.231,0.221)` |
| E | Employee SSC | `=C*D` |
| F | Monthly general allowance | `=5000/12` (plus additional allowance if qualifying) |
| G | Monthly PIT base | `=C-E-F` |
| H | Annual PIT base | `=G*12` |
| I | Annual PIT | bracket lookup on H (2025/2026 table) |
| J | Monthly PIT | `=I/12` |
| K | Flat CHC | `=IF(B<DATE(2025,3,1),35,37.17)` (confirm remittance) |
| L | Net pay | `=C-E-J-K` |
| M | Employer SSC rate | `=IF(B>=DATE(2025,7,1),0.171,0.161)` |
| N | Employer SSC | `=C*M` |
| O | Total employer cost | `=C+N` |

Add a validation cell asserting `D + M = combined wedge` and a check that the `E` component rows sum to `C*D`.

## Section 13 -- Bank Statement / Terminology Reading Guide

**Terminology Reading Guide table**

| Slovenian | English |
| --- | --- |
| bruto plača | gross salary |
| neto plača | net salary |
| dohodnina | personal income tax |
| akontacija dohodnine | advance income tax withholding |
| prispevki za socialno varnost | social security contributions |
| splošna olajšava | general (tax) allowance |
| olajšava za vzdrževane družinske člane | allowance for dependent family members |
| minimalna plača | minimum wage |
| regres (za letni dopust) | (annual leave) holiday allowance |
| malica / prevoz | meal allowance / transport reimbursement |
| dolgotrajna oskrba | long-term care |
| obvezni zdravstveni prispevek (OZZ) | compulsory health contribution (flat CHC) |
| obračun plač | payroll calculation |
| plačilna lista / plačilni list | payslip |

## Section 14 -- Onboarding Fallback

- **Onboarding fallback order** — If you do not have enough information to compute a payslip, gather these in order and do not guess: 1. Pay date — before or from 1 July 2025? Which calendar year? (sets contribution rate + bracket table); 2. Gross monthly salary (bruto plača) in EUR; 3. Tax residency and general allowance eligibility (incl. low-earner additional allowance); 4. Registered personal reliefs (dependants etc.); 5. CHC handling for this employee. If any of items 1-3 are missing, STOP and ask. Never default a contribution rate without a pay date (the 1 July 2025 LTC split makes this load-bearing).

## Section 15 -- Reference Material

### Rates and Thresholds (with provenance)

**Rates and Thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| PIT brackets 2025 | 16% / 26% / 33% / 39% / 50% (thresholds in Section 2) | PwC; FURS dohodninska lestvica 2025 |
| PIT brackets 2026 (indexed) | 16% / 26% / 33% / 39% / 50% (thresholds in Section 2) | Orbitax |
| Employee SSC | 22.10% (pre 1 Jul 2025) / 23.10% (from 1 Jul 2025) | PwC; KPMG Flash Alert 2025-133 |
| Employer SSC | 16.10% (pre 1 Jul 2025) / 17.10% (from 1 Jul 2025) | PwC; KPMG Flash Alert 2025-133 |
| LTC contribution (ZDOsk-1) | 1% employee + 1% employer (from 1 Jul 2025); self-employed 2%; pensioners 1% of net pension | KPMG Flash Alert 2025-133; ZDOsk-1 |
| Flat CHC | EUR 35.00/mo (Jan-Feb 2025); EUR 37.17/mo (from 1 Mar 2025) | PwC; WebSearch **[RESEARCH GAP — reviewer to confirm]** |
| General allowance (base) | EUR 5,000/yr | PwC Deductions |
| Minimum wage gross | EUR 1,277.72/mo (2025); EUR 1,481.88/mo (2026) | WageIndicator/SeeNews; RRA Koroška |
| Capital income flat rate | 25% (schedular) | PwC |
| VAT standard rate (context) | 22% | Tax rate summaries |
| Corporate income tax (context) | 19% (reported temporary 22% for 2025-2028 — verify) | Tax rate summaries **[RESEARCH GAP — reviewer to confirm]** |
| Self-employed min/max base (context) | EUR 1,521.62 / EUR 8,876.11; avg wage EUR 2,536.03 | WebSearch; ZPIZ-2 **[RESEARCH GAP — reviewer to confirm]** |

### Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| REK-O (Obračun davčnih odtegljajev) | Consolidated monthly employer withholding return reporting withheld PIT and all social contributions per employee; replaced REK-1/REK-1a/REK-2/PNiPD/REK-1f from 1 Jan 2023 (REK-1b retained for social-insurance benefits) | Filed electronically via eDavki on the **day of payment** of employment income; tax + contributions due on/around the pay date | FURS REK obrazci; Navodila za izpolnjevanje REK-O |
| Informativni izračun dohodnine (annual PIT assessment) | FURS-issued informative annual calculation reconciling withheld advance tax against final liability | FURS issues by 31 May (first batch) / 31 Oct of following year | FURS Letna odmera dohodnine |

### Penalties

**Penalties table**

| Item | Detail | Source |
| --- | --- | --- |
| Late/non-filing of REK-O; late payment | Fines for legal entities for failure to calculate, report and pay payroll withholding tax and contributions; default interest accrues on late payments. Specific fine bands are set in ZDavP-2 / ZPSV. | General (ZDavP-2) — **[RESEARCH GAP — reviewer to confirm]** exact fine bands not located at figure level |

### Sources

- PwC Worldwide Tax Summaries — Slovenia, Individual: [Other taxes](https://taxsummaries.pwc.com/slovenia/individual/other-taxes), [Taxes on personal income](https://taxsummaries.pwc.com/slovenia/individual/taxes-on-personal-income), [Deductions](https://taxsummaries.pwc.com/slovenia/individual/deductions)
- KPMG — [Slovenia: New Contributions under the Long-Term Care Act (GMS Flash Alert 2025-133)](https://kpmg.com/xx/en/our-insights/gms-flash-alert/flash-alert-2025-133.html)
- FURS — [REK obrazci](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/rek_obrazci/); Navodila za izpolnjevanje REK-O (velja od 1.1.2023); Dohodninska lestvica 2025 (Lestvica_za_leto_2025.docx); [Splošna olajšava 2025 tool](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_zaposlitve/2024_2025)
- Orbitax — [Slovenia Personal Income Tax Brackets and Relief for 2026](https://orbitax.com/news/country/article/Slovenia-Personal-Income-Tax-B-60703)
- WageIndicator — [Minimum Wage Updated in Slovenia from 01 January 2025](https://wageindicator.org/work/minimum-wage/updates/2025/minimum-wage-updated-in-slovenia-from-01-january-2025-february-5-2025/)
- RRA Koroška — [Minimum wage in Slovenia 2026](https://rra-koroska.si/en/updates/news/minimum-wage-in-the-republic-of-slovenia-in-2026); [Social security contributions for self-employed 2026](https://rra-koroska.si/en/updates/news/social-security-contributions-for-self-employed-persons-in-2026)

> **Caveat (research confidence: medium).** The FURS 2025 bracket schedule is published as a binary .docx (Lestvica_za_leto_2025.docx) not parsed in this session; a reviewer should open that DOCX and the FURS splošna olajšava 2025 tool to confirm the exact 2025 thresholds (PwC-sourced here) and the general-allowance figure (EUR 5,000 base confirmed; EUR 5,260 NOT confirmed). The PwC "other taxes" table lists pre-LTC rates (22.10%/16.10%); the 1%+1% LTC contribution (KPMG 2025-133, ZDOsk-1) took effect 1 July 2025 — any payroll engine must apply a date split. CHC amounts and remittance, the employee "uncapped" treatment, self-employed base figures, the average-wage anchor, and penalty bands all require reviewer confirmation as flagged above.

## Section 16 -- Test Suite

Numbered self-checks an agent (or reviewer) can run against this skill. Expected values recomputed in this skill.

- **Employee SSC components sum (pre-LTC)** — 15.50 + 6.36 + 0.14 + 0.10 = 22.10%
- **Employee SSC with LTC (from 1 Jul 2025)** — 22.10 + 1.00 = 23.10%
- **Employer SSC components sum (pre-LTC)** — 8.85 + 6.56 + 0.53 + 0.06 + 0.10 = 16.10%
- **Employer SSC with LTC (from 1 Jul 2025)** — 16.10 + 1.00 = 17.10%
- **Bracket 2 cumulative tax** — 9,210.26 x 16% = 1,473.64
- **Bracket 3 cumulative tax** — 1,473.64 + (27,089 − 9,210.26) x 26% = 6,122.11
- **Bracket 4 cumulative tax** — 6,122.11 + (54,178 − 27,089) x 33% = 15,061.48
- **Bracket 5 cumulative tax** — 15,061.48 + (78,016.32 − 54,178) x 39% = 24,358.42 (≈ 24,358.43 rounding)
- **Example 1 net before CHC (EUR 2,000, from Jul 2025)** — 2,000 − 462.00 − 214.79 = 1,323.21
- **Example 1 total employer cost** — 2,000 + (2,000 x 17.10%) = 2,000 + 342.00 = 2,342.00
- **Example 2 minimum-wage net before CHC** — 1,277.72 − 295.15 − 90.54 = 892.03
- **Example 3 mid-earner monthly PIT** — annual base 27,297.96 → (6,122.11 + (27,297.96 − 27,089) x 33%)/12 = 515.92
- **Example 4 higher-earner monthly PIT** — annual base 54,981.96 → (15,061.48 + (54,981.96 − 54,178) x 39%)/12 = 1,281.25
- **Date-split check (Example 5)** — same EUR 2,000 gross at 22.10%/16.10% gives net before CHC 1,338.01 and employer cost 2,322.00 — differs from Example 1, confirming the LTC split matters
- **Ceiling sanity** — every bracket upper bound ≥ its lower bound; self-employed max base (8,876.11) ≥ min base (1,521.62)
- **No-0%-band check** — lowest marginal rate is 16%, not 0%

## PROHIBITIONS

- NEVER pick a contribution rate without knowing the pay date — the 1 July 2025 LTC split changes employee 22.10%→23.10% and employer 16.10%→17.10%
- NEVER apply a 0% tax band — Slovenia's lowest marginal rate is 16%; relief comes from the general allowance
- NEVER cap employee social contributions at EUR 8,876.11 — that 3.5x cap is self-employed only; employee wage contributions are uncapped
- NEVER assume a EUR 5,260 general allowance — use EUR 5,000 base unless a reviewer confirms otherwise against FURS
- NEVER run capital income (dividends/interest/gains/rental) through the progressive wage scale — it is flat 25% schedular
- NEVER compute a regular full-time gross below the minimum wage (EUR 1,277.72 in 2025, EUR 1,481.88 in 2026)
- NEVER omit the flat CHC deduction or assume its remittance responsibility — flag it as unconfirmed
- NEVER miss the REK-O obligation — it is filed via eDavki on the day of payment of employment income
- NEVER state a penalty figure as definitive — ZDavP-2 / ZPSV bands were not captured at figure level here
- NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Slovenian accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant or tax adviser in Slovenia) before implementation.

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
