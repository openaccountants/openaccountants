---
name: sri-lanka-payroll
description: Use this skill whenever asked about Sri Lanka payroll processing for employed persons. Trigger on phrases like "Sri Lanka payroll", "APIT", "APIT Table 01", "PAYE Sri Lanka", "EPF deduction", "ETF contribution", "EPF Sri Lanka", "employer EPF", "ETF Board", "T-10 certificate", "APIT certificate", "net salary Sri Lanka", "gross to net Sri Lanka", "salary calculation Sri Lanka", "personal relief Sri Lanka", "minimum wage Sri Lanka", "tax withholding Sri Lanka", "IRD APIT", or any question about computing employee pay, income-tax withholding, or social-fund contributions for Sri Lanka-based employees. This skill covers APIT (Advance Personal Income Tax) monthly withholding, EPF employee and employer contributions, ETF employer contributions, minimum-wage reality, filing obligations to the Inland Revenue Department (IRD), the EPF and the ETF Board, and penalties. ALWAYS read this skill before processing any Sri Lanka payroll.
jurisdiction: LK
tax_year: 2025
last_updated: 2026-07-13
authored_by: Lal kumarasiri, CA
reviewed_by: Lal kumarasiri
review_status: current
trust_label: Checked by Lal kumarasiri
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sri Lanka Payroll

## Sri Lanka Payroll Skill v0.1

> **Tier 2 — research-verified, pending accountant sign-off.** Figures below are current for Sri Lanka's **Year of Assessment 2025/2026 (1 April 2025 – 31 March 2026)**. The personal relief and APIT Table 01 monthly formula are extracted verbatim from the Inland Revenue Department (IRD) primary PDF; the EPF/ETF rates are from official EPF/ETF/Central Bank sources. APIT penalty amounts are corroborated from reputable Sri Lankan tax-advisory summaries of the Inland Revenue Act and carry a flag. Do not present any computation as definitive until a Sri Lanka-qualified tax practitioner (CA Sri Lanka member or equivalent) has signed off.

## Section 1 — Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Democratic Socialist Republic of Sri Lanka |
| Currency | Sri Lankan Rupee (LKR) only |
| Standard pay frequency | Monthly |
| Year of assessment | 1 April – 31 March (e.g. 2025/2026 = 1 Apr 2025 – 31 Mar 2026) — *IRD* |
| Income-tax withholding system | APIT — Advance Personal Income Tax, the PAYE-style monthly withholding under the Inland Revenue Act No. 24 of 2017 (as amended) — *IRD APIT Table 01* |
| Tax authority | Inland Revenue Department (IRD) |
| Provident-fund authority | Employees' Provident Fund (EPF) — administered by the Central Bank / Dept. of Labour |
| Trust-fund authority | Employees' Trust Fund Board (ETF Board) |
| Key legislation | Inland Revenue Act No. 24 of 2017 (as amended); Employees' Provident Fund Act No. 15 of 1958; Employees' Trust Fund Act No. 46 of 1980 |
| Filing channel | IRD e-filing (mandatory for all employers from Y/A 2023/2024) |
| Personal relief (tax-free) | LKR 1,800,000/year = **LKR 150,000/month** (raised from 1,200,000 effective 1 Apr 2025) — *IRD APIT Table 01* |
| Top marginal APIT rate | **36%** on annual taxable income above the 30% band — *IRD APIT 2025/26 guideline* |
| EPF total contribution | 20% of total earnings (8% employee + 12% employer), no ceiling — *EPF Act; EPF Employer FAQ* |
| ETF contribution | 3% of total earnings, employer-only — *ETF Act; ETF Board* |
| Validated by | Pending — requires sign-off by a Sri Lanka-qualified tax practitioner |
| Skill version | 0.1 |

## Section 2 — Income Tax Withholding (APIT)

The employer withholds APIT **monthly** under the Inland Revenue Act No. 24 of 2017 (as amended) and remits to the IRD. Sri Lanka has a genuine personal income tax; this is **not** a no-PIT jurisdiction. The monthly withholding uses **APIT Table 01** for resident employees and Sri Lankan-citizen non-residents on primary employment. The personal relief of **LKR 150,000/month** has already been baked into the Table 01 formula (the "− subtract" term restores it).

> **Which APIT table applies.** Table 01 covers resident employees and non-resident **Sri Lankan citizens** with a single (primary) employment; deduction is **compulsory regardless of employee consent**. Other tables exist for other situations — see Section 11. When the employee's category is unclear, refuse and ask (Refusal Catalogue, Section 7).

### 2.1 Annual progressive rate schedule (Y/A 2025/2026)

**Annual progressive rate schedule (Y/A 2025/2026)**  _(Source: IRD APIT 2025/2026 guideline — https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Guide/APIT_2526_Guideline.pdf)_

| Annual taxable income band (LKR) | Rate |
| --- | --- |
| First 1,000,000 | 6% |
| Next 500,000 | 18% |
| Next 500,000 | 24% |
| Next 500,000 | 30% |
| Balance | 36% |

### 2.2 Monthly APIT Table 01 — exact formula (Y/A 2025/2026)

**Monthly APIT Table 01 — exact formula (Y/A 2025/2026)**  _(Source (verbatim from IRD): https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Table%20-%201/02.%20APIT_2526_Table_01_Text.pdf)_

| Monthly regular profits (LKR) | Monthly APIT |
| --- | --- |
| Up to 150,000 | Nil (relief) |
| 150,001 – 233,333 | **6% × gross − 9,000** |
| 233,334 – 275,000 | **18% × gross − 37,000** |
| 275,001 – 316,667 | **24% × gross − 53,500** |
| 316,668 – 358,333 | **30% × gross − 72,500** |
| Over 358,333 | **36% × gross − 94,000** |

"Monthly regular profits from employment" = gross monthly employment income, including non-cash benefits (Section 2.4). Apply the row that contains the gross figure.

**Band-boundary / cumulative-tax anchors (recomputed):**
- Relief LKR 150,000/month corresponds to annual relief 1,800,000. First annual band 1,000,000 ÷ 12 = 83,333.33 → gross top of 6% band = 150,000 + 83,333.33 = **233,333** ✓
- At gross 233,333: 6% × 233,333 − 9,000 = 13,999.98 − 9,000 = **≈5,000** ✓ (= 6% × 83,333 taxable)
- At gross 275,000 (top of 18% band): 18% × 275,000 − 37,000 = 49,500 − 37,000 = **12,500** ✓
- At gross 316,667 (top of 24% band): 24% × 316,667 − 53,500 = 76,000 − 53,500 = **≈22,500** ✓
- At gross 358,333 (top of 30% band): 30% × 358,333 − 72,500 = 107,500 − 72,500 = **≈35,000** ✓
- Just above 358,333 (36% band): 36% × 358,333 − 94,000 = 129,000 − 94,000 = **≈35,000** ✓ (continuous — the two formulas meet at the boundary)

Each "− subtract" constant reconciles to the lower-band cumulative tax, so the schedule is continuous at every boundary.

### 2.3 No tax-free relief beyond LKR 150,000/month

- **Personal relief limit** — The relief is **LKR 150,000/month** (LKR 1,800,000/year). It is built into the formula; do **not** subtract it a second time. Gross at or below 150,000/month attracts **nil** APIT under Table 01.  _(IRD APIT Table 01 (states "Rs. 150,000.00 per month as personal relief has already been deducted"))_

### 2.4 Regular profits from employment include

- **Regular profits from employment** — Wages, salary, commission, overtime, travel and other allowances, fees, pension; non-cash benefits (housing, conveyance, electricity, telephone, entertainment, etc., at fair market value); medical bills/insurance (with a limited exemption where dental/medical/health insurance is available to all full-time employees on equal terms); third-party payments made for the employee's benefit. Only Third Schedule exemptions (Inland Revenue Act No. 24 of 2017, as amended) apply.  _(IRD APIT Table 01)_

## Section 3 — EPF (Employees' Provident Fund)

EPF is governed by the **Employees' Provident Fund Act No. 15 of 1958**. Contributions are computed on **total monthly earnings** with **no floor and no ceiling**. The statutory rates are minimums — an employer may contribute more.

### 3.1 EPF contribution rates (Y/A 2025/2026)

**EPF contribution rates (Y/A 2025/2026)**  _(Sources: EPF Act — https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/acts/en/epf_act.pdf ; EPF Employer FAQ — https://epf.lk/?page_id=811 ; Central Bank EPF — https://www.cbsl.gov.lk/en/employees-provident-fund)_

| Party | Rate | Base |
| --- | --- | --- |
| Employee | **8%** (deducted from pay) | Total monthly earnings |
| Employer | **12%** | Total monthly earnings |
| **Total** | **20%** | Total monthly earnings |

**Arithmetic self-check:** employee 8% + employer 12% = **20% total** ✓

### 3.2 EPF "total earnings" base

**EPF total earnings base**  _(EPF Employer FAQ)_

| Treatment | Items |
| --- | --- |
| **Included** | Salary/wages/fees; cost-of-living and special living allowances; holiday payments; cash value of food supplied by the employer; food allowances; commissions; piece-rate / contract payments — *EPF Employer FAQ* |
| **Excluded** | Overtime pay; reimbursable travelling expenses; incentive / bonus payments — *EPF Employer FAQ* |

- **EPF base ≠ APIT base** — APIT (Section 2) is computed on full regular profits including overtime and many allowances; the EPF base **excludes** overtime, reimbursed travel and bonuses. Compute the two bases separately; never reuse the gross figure blindly.  _(EPF Employer FAQ)_

### 3.3 Coverage and deadline

**Coverage and deadline**  _(EPF Employer FAQ; EPF Act)_

| Rule | Detail |
| --- | --- |
| Mandatory scope | Any employer with **one or more employees** — EPF applies from the first covered employee; no minimum headcount — *EPF Employer FAQ* |
| Ceiling | **None** — 20% applies to full total earnings — *EPF Act* |
| Floor | **None** identified beyond actual wage — *EPF Employer FAQ* |
| Payment deadline | On or before the **last working day of the following month** — *EPF Employer FAQ* |

## Section 4 — ETF (Employees' Trust Fund)

ETF is governed by the **Employees' Trust Fund Act No. 46 of 1980** (fund established 1 March 1981) and administered by the ETF Board. It is **employer-only**.

**ETF rates**  _(ETF Act No. 46 of 1980; ETF Board payment page — https://etfb.lk/payment-of-contributions/ ; ETF Employers FAQ — https://etfb.lk/employers-faq/)_

| Party | Rate | Base |
| --- | --- | --- |
| Employer | **3%** | Total monthly earnings |
| Employee | **0%** — no employee contribution; must **NOT** be deducted from employee pay | — |

**ETF mandatory scope and deadline**  _(ETF Employers FAQ; ETF Board)_

| Rule | Detail |
| --- | --- |
| Mandatory scope | Any employer with one or more employees — *ETF Employers FAQ* |
| Payment deadline | On or before the **last working day of the following month** — *ETF Board* |

- **Combined employer social cost** — > **Combined employer social cost.** Employer bears **15%** of earnings (12% EPF + 3% ETF); employee bears **8%** (EPF only). Total paid into the two funds = **23%** (20% EPF + 3% ETF). **Arithmetic self-check:** 12% + 3% = 15% employer ✓; 15% employer + 8% employee = 23% total ✓.

## Section 5 — Minimum Wage

**Minimum wage table**  _(Ministry of Labour — https://labourmin.gov.lk/heres-how-the-private-sector-minimum-wage-is-set-to-rise/ ; National Minimum Wage of Workers (Amendment) Act No. 11 of 2025 — https://www.parliament.lk/uploads/acts/gbills/english/6388.pdf ; Daily Mirror (gazette report) — https://www.dailymirror.lk/breaking-news/Govt-announces-Rs-27-000-minimum-monthly-wage-in-gazette-from-April-1/108-309443)_

| Rule | Detail |
| --- | --- |
| National Minimum Monthly Wage (private sector) | **LKR 27,000/month** (effective 1 Apr 2025; raised from LKR 21,000) — *Ministry of Labour; Amendment Act No. 11 of 2025* |
| National Minimum Daily Wage | **LKR 1,080/day** (raised from LKR 700) — *Ministry of Labour; Amendment Act No. 11 of 2025* |
| Budgetary Relief Allowances (BRA) | Consolidated into the LKR 27,000 figure for 2025 — **no separate BRA add-on** — *Ministry of Labour* |
| From 1 January 2026 | Further increase to **LKR 30,000/month** — *Ministry of Labour; Amendment Act No. 11 of 2025* |

- **Implication for payroll** — **Implication for payroll:** there **is** a binding wage floor (LKR 27,000/month for Y/A 2025/2026; LKR 30,000/month from 1 Jan 2026). Flag any monthly gross below the floor.  _(Ministry of Labour; Amendment Act No. 11 of 2025)_

## Section 6 — Conservative Defaults

When a required input is ambiguous and the user cannot supply it, apply the **most conservative** assumption (the one that maximises tax/contribution exposure or that forces a refusal), and label the output as provisional.

**Conservative defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Which APIT table applies | Use **Table 01** ONLY if primary-employment / single-employer is confirmed; otherwise refuse and ask | Tables 02–08 apply to arrears, terminal payments, secondary employment, mid-year joiners — different formulas |
| Whether a payment is "regular profits" for APIT | **Include** it in the APIT gross | APIT base is broad; over-withholding is recoverable, under-withholding makes the employer personally liable (Section 124) |
| Whether a payment is in the EPF "total earnings" base | **Include** unless it is overtime, reimbursed travel or a bonus | Those three are the named exclusions; everything else is in |
| Whether ETF applies | Assume **yes** (3% employer) for any covered employee | ETF has no headcount threshold |
| Pay frequency | **Monthly** | Standard Sri Lanka practice |
| Currency | **LKR** | Only legal payroll currency |
| Gross below the minimum wage | **Flag** as below LKR 27,000/month floor (LKR 30,000 from 1 Jan 2026) | A binding floor exists |
| Residence / citizenship for table selection | Refuse and ask | Table 01 covers residents and Sri Lankan-citizen non-residents only |

## Section 7 — Required Inputs & Refusal Catalogue

### 7.1 Minimum required inputs

- **Minimum required inputs** — To compute Sri Lanka payroll for one employee for one month, you MUST have: 1. **Gross monthly regular profits** (in LKR) for APIT. 2. **Total monthly earnings** for EPF/ETF (may differ from APIT gross — exclude overtime, reimbursed travel, bonuses). 3. **Employee category** confirming **Table 01** applies (resident or Sri Lankan-citizen non-resident; single/primary employment). 4. **Month of pay** (to set remittance deadlines). 5. Confirmation of whether any allowance/benefit is exempt (Third Schedule) or excluded from the EPF base.

### 7.2 Refusal Catalogue — REFUSE and ask if any of these hold

**Refusal Catalogue**

| Situation | Why refuse |
| --- | --- |
| APIT table / employment category not stated | Tables 01–08 have different formulas; never assume Table 01 silently |
| Currency given is not LKR | Payroll must be in LKR; silent FX conversion introduces error |
| Lump-sum / arrears / terminal payment present | These use Table 02/03, not the monthly Table 01 formula |
| APIT gross and EPF base conflated as one number | The bases differ (overtime, travel, bonus excluded from EPF) |
| Employee may have a second employment | Secondary employment uses a different table |
| Non-resident who is **not** a Sri Lankan citizen | Table 01 does not apply; different withholding rules |
| Asked to treat the result as final/filed advice | This is a Tier 2 skill pending sign-off |
| Asked to confirm exact APIT penalty figures as statute | Penalty amounts are flagged — see Section 16 |

When refusing, state the missing input plainly and request it. Do not fabricate.

## Section 8 — Transaction / Payment Pattern Library

Deterministic mapping of Sri Lankan bank-statement narrations to payroll classifications. Match case-insensitively; longer/more specific patterns win. Statements are commonly in English; banks include Bank of Ceylon (BOC), People's Bank, Commercial Bank (Combank), Hatton National Bank (HNB) and Sampath Bank. Sinhala/Tamil narrations occasionally appear.

### 8.1 Salary credits (employee side)

**Salary credits (employee side)**

| Narration pattern | Classification |
| --- | --- |
| `SALARY`, `SAL`, `PAY`, `NET SALARY`, `WAGES` | Net salary credit |
| `EMPLOYER [name] TRANSFER`, `STAFF SAL` | Net salary credit |
| `වැටුප` (Sinhala "salary"), `சம்பளம்` (Tamil "salary") | Net salary credit |
| `BONUS`, `INCENTIVE` | Supplement — taxable for APIT, **excluded** from EPF base |
| `OT`, `OVERTIME` | Overtime — taxable for APIT, **excluded** from EPF base |
| `EPF REFUND`, `ETF REFUND` | Fund adjustment — not income |

### 8.2 Employer debit patterns (remittances)

**Employer debit patterns (remittances)**

| Narration pattern | Classification |
| --- | --- |
| `IRD APIT`, `APIT`, `PAYE`, `IRD PAYMENT` | APIT remittance to IRD |
| `EPF`, `EPF CONTRIBUTION`, `EPF 20%`, `PROVIDENT FUND` | EPF contribution (8% employee + 12% employer) |
| `ETF`, `ETF BOARD`, `TRUST FUND` | ETF contribution (3% employer-only) |
| `NET WAGES`, `PAYROLL`, `SALARY BATCH`, `STAFF SALARIES` | Net salary disbursement to employees |
| `SLIPS`, `PAYMENT VOUCHER IRD` | IRD payment voucher reference — tax remittance |

> **EPF vs ETF note:** an EPF remittance is 20% of the EPF base (8% deducted from staff + 12% employer); an ETF remittance is 3% employer-only. If a single line is labelled "EPF/ETF 23%", split it 20/3 before posting.

## Section 9 — Worked Examples

All examples use **APIT Table 01** (Section 2.2), **EPF 8%/12%** (Section 3.1) and **ETF 3%** (Section 4). For simplicity each example assumes the EPF base equals the APIT gross (i.e. no overtime/bonus); where overtime or a bonus exists, the EPF base would be lower — see the note after Example 6. Every figure recomputed end-to-end.

### Example 1 — Minimum-wage earner (gross LKR 27,000/month)

Statement line: `STAFF SAL EMP001 ... 24,840`

- **APIT:** 27,000 ≤ 150,000 → **LKR 0** (relief)
- **EPF employee (8%):** 8% × 27,000 = **LKR 2,160**
- **EPF employer (12%):** 12% × 27,000 = **LKR 3,240**
- **ETF employer (3%):** 3% × 27,000 = **LKR 810**
- **Net pay:** 27,000 − 0 − 2,160 = **LKR 24,840**
- **Total employer cost:** 27,000 + 3,240 + 810 = **LKR 31,050**

*Cross-check vs statement: net 24,840 matches the narration ✓.*

### Example 2 — At the personal relief (gross LKR 150,000/month)

- **APIT:** 150,000 = top of the Nil band → **LKR 0**
- **EPF employee (8%):** 8% × 150,000 = **LKR 12,000**
- **EPF employer (12%):** 12% × 150,000 = **LKR 18,000**
- **ETF employer (3%):** 3% × 150,000 = **LKR 4,500**
- **Net pay:** 150,000 − 0 − 12,000 = **LKR 138,000**
- **Total employer cost:** 150,000 + 18,000 + 4,500 = **LKR 172,500**

### Example 3 — First APIT band, 6% (gross LKR 200,000/month)

- **APIT:** 200,000 in band 150,001–233,333 → 6% × 200,000 − 9,000 = 12,000 − 9,000 = **LKR 3,000**
- **EPF employee (8%):** 8% × 200,000 = **LKR 16,000**
- **EPF employer (12%):** 12% × 200,000 = **LKR 24,000**
- **ETF employer (3%):** 3% × 200,000 = **LKR 6,000**
- **Net pay:** 200,000 − 3,000 − 16,000 = **LKR 181,000**
- **Total employer cost:** 200,000 + 24,000 + 6,000 = **LKR 230,000**

### Example 4 — 24% band (gross LKR 300,000/month)

- **APIT:** 300,000 in band 275,001–316,667 → 24% × 300,000 − 53,500 = 72,000 − 53,500 = **LKR 18,500**
- **EPF employee (8%):** 8% × 300,000 = **LKR 24,000**
- **EPF employer (12%):** 12% × 300,000 = **LKR 36,000**
- **ETF employer (3%):** 3% × 300,000 = **LKR 9,000**
- **Net pay:** 300,000 − 18,500 − 24,000 = **LKR 257,500**
- **Total employer cost:** 300,000 + 36,000 + 9,000 = **LKR 345,000**

### Example 5 — Top APIT band, 36% (gross LKR 500,000/month)

- **APIT:** 500,000 > 358,333 → 36% × 500,000 − 94,000 = 180,000 − 94,000 = **LKR 86,000**
- **EPF employee (8%):** 8% × 500,000 = **LKR 40,000**
- **EPF employer (12%):** 12% × 500,000 = **LKR 60,000**
- **ETF employer (3%):** 3% × 500,000 = **LKR 15,000**
- **Net pay:** 500,000 − 86,000 − 40,000 = **LKR 374,000**
- **Total employer cost:** 500,000 + 60,000 + 15,000 = **LKR 575,000**

### Example 6 — 18% band (gross LKR 250,000/month)

- **APIT:** 250,000 in band 233,334–275,000 → 18% × 250,000 − 37,000 = 45,000 − 37,000 = **LKR 8,000**
- **EPF employee (8%):** 8% × 250,000 = **LKR 20,000**
- **EPF employer (12%):** 12% × 250,000 = **LKR 30,000**
- **ETF employer (3%):** 3% × 250,000 = **LKR 7,500**
- **Net pay:** 250,000 − 8,000 − 20,000 = **LKR 222,000**
- **Total employer cost:** 250,000 + 30,000 + 7,500 = **LKR 287,500**

> **Overtime/bonus illustration.** If Example 4's LKR 300,000 comprised LKR 270,000 regular + LKR 30,000 overtime, APIT still applies to the full 300,000 (overtime is regular profits for APIT) → LKR 18,500, but the **EPF/ETF base** would be **270,000**: EPF employee 8% × 270,000 = 21,600; EPF employer 32,400; ETF 8,100. Always split the two bases.

## Section 10 — Tier 1 Rules (deterministic, always apply)

- **Tier 1 Rules** — 1. APIT is computed on **gross monthly regular profits** using **Table 01** (Section 2.2) for resident / Sri Lankan-citizen-non-resident primary employment. 2. The personal relief is **LKR 150,000/month**, already built into the Table 01 formula — never deduct it twice. 3. EPF = **8% employee + 12% employer = 20%** of **total earnings** (Section 3.1), **no floor, no ceiling**. 4. ETF = **3% employer-only** of total earnings (Section 4) — **never** deduct ETF from the employee. 5. The **EPF/ETF base excludes** overtime, reimbursed travel and bonuses; the **APIT base includes** them. Compute the two bases separately. 6. Currency is **LKR** only. 7. APIT is remitted by the **15th of the following month**; EPF and ETF by the **last working day of the following month**. 8. The minimum monthly wage is **LKR 27,000** (LKR 30,000 from 1 Jan 2026) — flag any gross below it. 9. Every output is labelled **provisional / pending accountant sign-off**.

## Section 11 — Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Item | Why it needs judgement |
| --- | --- |
| Selection between APIT Tables 01–08 | Lump-sum (Table 02), terminal (Table 03), mid-year joiner/retiree or sub-threshold-but-annual-over-1.8M (Table 05), Table 08 categories — fact-specific |
| Valuation of non-cash benefits (housing, vehicle, utilities) | Fair-market-value rules under the Inland Revenue Act not fully encoded here |
| Whether a medical/insurance benefit qualifies for the equal-terms exemption | Conditional on all full-time staff being covered on equal terms |
| Third Schedule exemptions | Item-by-item statutory analysis |
| Residence / citizenship for table eligibility | Non-Sri-Lankan-citizen non-residents fall outside Table 01 |
| Whether a specific allowance sits in the EPF base | The named exclusions are overtime, reimbursed travel and bonuses; edge cases need judgement |
| Gross-up where the employer bears the APIT | Iterative; depends on contract terms |
| Double-tax-treaty / expatriate relief | Treaty-by-treaty analysis |
| Mid-month joiners/leavers | Pro-ration and Table 05 interaction not encoded |

## Section 12 — Excel Working Paper Template

Suggested column layout for a monthly Sri Lanka payroll working paper (one row per employee):

**Excel Working Paper Template columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | TIN | input |
| C | APIT table (confirm 01) | input |
| D | APIT gross / regular profits (LKR) | input |
| E | EPF/ETF base — total earnings (LKR) | input (exclude OT, reimbursed travel, bonus) |
| F | APIT band applied | lookup on D |
| G | APIT (LKR) | Table 01 formula (Section 2.2) |
| H | EPF employee 8% (LKR) | `=ROUND(E*0.08,2)` |
| I | EPF employer 12% (LKR) | `=ROUND(E*0.12,2)` |
| J | ETF employer 3% (LKR) | `=ROUND(E*0.03,2)` |
| K | Net pay (LKR) | `=D-G-H` |
| L | Total employer cost (LKR) | `=D+I+J` |
| M | Remittance month | APIT 15th; EPF/ETF last working day |

- **APIT Table 01 formula (Excel)** — =IF(D<=150000,0, IF(D<=233333,D*0.06-9000, IF(D<=275000,D*0.18-37000, IF(D<=316667,D*0.24-53500, IF(D<=358333,D*0.30-72500, D*0.36-94000)))))  _(Section 2.2)_

Reconcile column G against the worked examples before relying on the sheet. Note: K subtracts APIT and EPF employee only; ETF and EPF employer are employer costs (column L), not employee deductions.

## Section 13 — Bank Statement / Terminology Reading Guide (Sri Lanka)

**Terminology Reading Guide**

| Term / abbreviation | Meaning |
| --- | --- |
| LKR / Rs. | Sri Lankan Rupee |
| IRD | Inland Revenue Department (income tax / APIT) |
| APIT | Advance Personal Income Tax — the PAYE-style monthly withholding |
| PAYE | Older name for the employee-withholding system, often used interchangeably with APIT |
| TIN | Taxpayer Identification Number (employer and each employee) |
| EPF | Employees' Provident Fund (8% employee + 12% employer = 20%) |
| ETF | Employees' Trust Fund (3% employer-only) |
| T-10 / APIT Certificate | Annual earnings/tax certificate the employer must issue to each employee |
| BRA | Budgetary Relief Allowance — consolidated into the 2025 minimum wage |
| BOC / HNB / Combank | Bank of Ceylon / Hatton National Bank / Commercial Bank |
| Y/A | Year of Assessment (1 April – 31 March) |
| වැටුප / சம்பளம் | "Salary" in Sinhala / Tamil |

## Section 14 — Onboarding Fallback

- **Onboarding fallback questions** — If you lack a required input and cannot proceed, ask the user the following, in order, and stop until answered: 1. "Does **APIT Table 01** apply — is the employee a **resident or Sri Lankan-citizen non-resident** on a **single/primary** employment?" 2. "What are the employee's **gross monthly regular profits in LKR** (for APIT)?" 3. "What is the **total-earnings base for EPF/ETF** — does it differ from the APIT gross (overtime, reimbursed travel and bonuses are excluded from EPF)?" 4. "Which **month** is this pay run for (sets the remittance deadlines)?" 5. "Are any allowances or benefits **exempt (Third Schedule)** or excluded from the EPF base?" Do not estimate around a missing APIT table category or gross figure. Do not deduct ETF from the employee under any circumstance.

## Section 15 — Filing Obligations & Deadlines

**Filing Obligations & Deadlines**  _(IRD APIT Annual Statement guide — https://www.ird.gov.lk/en/Downloads/Other_PAYE_Doc/Asmt_APIT_Guide_2024_2025_E.pdf ; simplebooks — https://simplebooks.com/srilanka/apit-return-filing-in-sri-lanka/ ; EPF Employer FAQ — https://epf.lk/?page_id=811 ; ETF Board — https://etfb.lk/payment-of-contributions/)_

| Obligation | Form / channel | Deadline |
| --- | --- | --- |
| APIT monthly remittance | Pay to Commissioner-General, IRD | **On or before the 15th of the following month** (Section 120(a), IRA) — *IRD; simplebooks* |
| APIT Annual Statement + schedules | IRD e-filing (**mandatory** for all employers from Y/A 2023/2024, Section 113(1B)) | **On or before 30 April** following the year of assessment — *IRD APIT Annual Statement guide* |
| Employee certificate (T-10 / APIT Certificate) | Employer issues to every employee, including zero-tax employees | **By 30 April**, or within **30 days** of cessation of employment — *simplebooks* |
| EPF monthly contribution | EPF (Central Bank / Dept. of Labour) | **Last working day of the following month** — *EPF Employer FAQ* |
| ETF monthly contribution | ETF Board | **Last working day of the following month** — *ETF Board* |

- **Employer liability** — Employer liability: an employer who fails to deduct/remit APIT is **personally liable** for the amount (Section 124(1), IRA).  _(Section 124(1), IRA)_

## Section 16 — Penalties

### 16.1 APIT (Inland Revenue Act)

**APIT (Inland Revenue Act) penalties**  _(LK tax-advisory summaries of the IRA)_

| Default | Penalty |
| --- | --- |
| Late / non-filing of return | **LKR 50,000 fixed + LKR 10,000 per month** (or part), capped at **LKR 400,000** — *LK tax-advisory summaries of the IRA* |
| Late payment of tax | **10% penalty** if not remitted within 14 days of the due date, plus **interest of 1.5% per month** (or part) on unpaid tax — *LK tax-advisory summaries of the IRA* |

> **[RESEARCH GAP — reviewer to confirm]** The APIT penalty amounts above (LKR 50,000 + LKR 10,000/month, cap LKR 400,000; 10% + 1.5%/month) are sourced from reputable Sri Lankan tax-advisory summaries reflecting the Inland Revenue Act provisions, **not** a directly-extracted IRD statute page. They are consistent across multiple sources but must be cross-checked against the Inland Revenue Act No. 24 of 2017 (as amended) before publication. *Sources: simplebooks — https://simplebooks.com/srilanka/apit-return-filing-in-sri-lanka/ ; bizadvisor — https://bizadvisor.lk/handbook/APIT-advance-personal-income-tax-srilanka*

### 16.2 EPF late-payment surcharge

**EPF late-payment surcharge**  _(EPF Employer FAQ — https://epf.lk/?page_id=811)_

| Delay | Surcharge |
| --- | --- |
| 1–10 days | 5% |
| 11 days – 1 month | 15% |
| 1–3 months | 20% |
| 3–6 months | 30% |
| 6–12 months | 40% |
| Over 12 months | 50% |

- **Incomplete details surcharge** — Plus a **2% surcharge** for submitting incomplete details.  _(EPF Employer FAQ — https://epf.lk/?page_id=811)_

### 16.3 ETF late-payment surcharge

**ETF late-payment surcharge**  _(ETF Board — https://etfb.lk/payment-of-contributions/ ; ETF Employers FAQ — https://etfb.lk/employers-faq/)_

| Delay | Surcharge |
| --- | --- |
| ≤10 days | 5% |
| 11 days – 1 month | 15% |
| 1–3 months | 20% |
| 3–6 months | 30% |
| 6–12 months | 40% |
| Over 12 months | 50% |

## Section 17 — Related Context (Corporate Income Tax)

**Corporate income tax reference**  _(simplebooks — https://simplebooks.com/srilanka/apit-tax/ (secondary; the primary authority is the Inland Revenue Act No. 24 of 2017, as amended).)_

| Item | Value |
| --- | --- |
| Standard corporate income tax | **30%** on taxable profits (most companies), Y/A 2025/2026 — *secondary summary; primary is the IRA* |

Not part of payroll, but employers commonly ask:

## Section 18 — Reference Material

**Reference Material summary table**  _(IRD APIT Table 01; IRD APIT guideline; EPF Act; EPF Employer FAQ; ETF Act; ETF Board; Ministry of Labour; Amendment Act No. 11 of 2025; IRD; simplebooks; LK tax-advisory summaries of IRA; IRD APIT Annual Statement guide)_

| Topic | Figure | Source |
| --- | --- | --- |
| Personal relief (tax-free) | LKR 150,000/month (1,800,000/yr) | IRD APIT Table 01 |
| APIT first band | 6% (annual first 1,000,000) | IRD APIT guideline |
| APIT top rate | 36% (annual balance) | IRD APIT guideline |
| APIT Table 01 6% formula | 6% × gross − 9,000 (150,001–233,333) | IRD APIT Table 01 |
| APIT Table 01 18% formula | 18% × gross − 37,000 (233,334–275,000) | IRD APIT Table 01 |
| APIT Table 01 24% formula | 24% × gross − 53,500 (275,001–316,667) | IRD APIT Table 01 |
| APIT Table 01 30% formula | 30% × gross − 72,500 (316,668–358,333) | IRD APIT Table 01 |
| APIT Table 01 36% formula | 36% × gross − 94,000 (over 358,333) | IRD APIT Table 01 |
| EPF employee | 8% of total earnings | EPF Act; EPF Employer FAQ |
| EPF employer | 12% of total earnings | EPF Act; EPF Employer FAQ |
| EPF total | 20% of total earnings, no ceiling | EPF Act; EPF Employer FAQ |
| ETF | 3% employer-only | ETF Act; ETF Board |
| Minimum wage | LKR 27,000/month; LKR 1,080/day (LKR 30,000/month from 1 Jan 2026) | Ministry of Labour; Amendment Act No. 11 of 2025 |
| APIT remittance deadline | 15th of following month (Section 120(a)) | IRD; simplebooks |
| APIT annual statement / T-10 | 30 April; e-filing mandatory | IRD APIT Annual Statement guide |
| EPF/ETF deadline | Last working day of following month | EPF Employer FAQ; ETF Board |
| APIT late-filing penalty | LKR 50,000 + 10,000/month, cap 400,000 **[RESEARCH GAP]** | LK tax-advisory summaries of IRA |
| APIT late-payment | 10% + 1.5%/month interest **[RESEARCH GAP]** | LK tax-advisory summaries of IRA |
| Corporate income tax | 30% | simplebooks (secondary) |
| Year of assessment | 1 Apr – 31 Mar | IRD |

- **Personal relief (tax-free)** — LKR 150,000/month (1,800,000/yr)  _(IRD APIT Table 01)_
- **APIT first band** — 6% (annual first 1,000,000)  _(IRD APIT guideline)_
- **APIT top rate** — 36% (annual balance)  _(IRD APIT guideline)_
- **APIT Table 01 6% formula** — 6% × gross − 9,000 (150,001–233,333)  _(IRD APIT Table 01)_
- **APIT Table 01 18% formula** — 18% × gross − 37,000 (233,334–275,000)  _(IRD APIT Table 01)_
- **APIT Table 01 24% formula** — 24% × gross − 53,500 (275,001–316,667)  _(IRD APIT Table 01)_
- **APIT Table 01 30% formula** — 30% × gross − 72,500 (316,668–358,333)  _(IRD APIT Table 01)_
- **APIT Table 01 36% formula** — 36% × gross − 94,000 (over 358,333)  _(IRD APIT Table 01)_
- **EPF employee** — 8% of total earnings  _(EPF Act; EPF Employer FAQ)_
- **EPF employer** — 12% of total earnings  _(EPF Act; EPF Employer FAQ)_
- **EPF total** — 20% of total earnings, no ceiling  _(EPF Act; EPF Employer FAQ)_
- **ETF** — 3% employer-only  _(ETF Act; ETF Board)_
- **Minimum wage** — LKR 27,000/month; LKR 1,080/day (LKR 30,000/month from 1 Jan 2026)  _(Ministry of Labour; Amendment Act No. 11 of 2025)_
- **APIT remittance deadline** — 15th of following month (Section 120(a))  _(IRD; simplebooks)_
- **APIT annual statement / T-10** — 30 April; e-filing mandatory  _(IRD APIT Annual Statement guide)_
- **EPF/ETF deadline** — Last working day of following month  _(EPF Employer FAQ; ETF Board)_
- **APIT late-filing penalty** — LKR 50,000 + 10,000/month, cap 400,000 **[RESEARCH GAP]**  _(LK tax-advisory summaries of IRA)_
- **APIT late-payment** — 10% + 1.5%/month interest **[RESEARCH GAP]**  _(LK tax-advisory summaries of IRA)_
- **Corporate income tax** — 30%  _(simplebooks (secondary))_
- **Year of assessment** — 1 Apr – 31 Mar  _(IRD)_

**Primary sources:**
- IRD APIT Table 01 (2025/26, primary) — https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Table%20-%201/02.%20APIT_2526_Table_01_Text.pdf
- IRD APIT 2025/26 guideline — https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Guide/APIT_2526_Guideline.pdf
- IRD APIT Annual Statement guide — https://www.ird.gov.lk/en/Downloads/Other_PAYE_Doc/Asmt_APIT_Guide_2024_2025_E.pdf
- EPF Employer FAQ — https://epf.lk/?page_id=811
- Central Bank EPF — https://www.cbsl.gov.lk/en/employees-provident-fund
- EPF Act — https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/laws/acts/en/epf_act.pdf
- ETF Board contributions — https://etfb.lk/payment-of-contributions/
- ETF Employers FAQ — https://etfb.lk/employers-faq/
- Ministry of Labour minimum wage — https://labourmin.gov.lk/heres-how-the-private-sector-minimum-wage-is-set-to-rise/
- Amendment Act No. 11 of 2025 (Parliament) — https://www.parliament.lk/uploads/acts/gbills/english/6388.pdf

## Section 19 — Test Suite

Each test states inputs and the expected output; recompute before trusting any change to this skill. EPF base = APIT gross unless stated; APIT from Section 2.2, EPF/ETF from Sections 3–4.

**Gross 27,000 (minimum wage).** Expect APIT = **0**; EPF emp = 2,160; ETF emp = 0; net = **24,840**; employer cost = 31,050. *(See Example 1.)*

**Gross 150,000 (at relief).** Expect APIT = **0**; EPF emp = 12,000; net = **138,000**; employer cost = 172,500. *(See Example 2.)*

**Gross 200,000.** Expect APIT = 6% × 200,000 − 9,000 = **3,000**; EPF emp = 16,000; net = **181,000**. *(See Example 3.)*

**Gross 250,000.** Expect APIT = 18% × 250,000 − 37,000 = **8,000**; EPF emp = 20,000; net = **222,000**. *(See Example 6.)*

**Gross 300,000.** Expect APIT = 24% × 300,000 − 53,500 = **18,500**; EPF emp = 24,000; net = **257,500**. *(See Example 4.)*

**Gross 500,000.** Expect APIT = 36% × 500,000 − 94,000 = **86,000**; EPF emp = 40,000; net = **374,000**. *(See Example 5.)*

**EPF/ETF total check, any base B.** Expect EPF employer 12% + employee 8% = **20% of B**; ETF employer = **3% of B**; total to funds = **23% of B**; no ceiling.

**ETF deducted from employee.** Expect: **refuse / flag** — ETF is employer-only (0% employee); never deduct from pay.

**Gross 300,000 with 30,000 overtime.** Expect APIT on full 300,000 = **18,500**; EPF base = 270,000 → EPF emp = 21,600, EPF er = 32,400, ETF = 8,100. *(See note after Example 6.)*

**Lump-sum / terminal payment.** Expect: **refuse / flag** — use Table 02/03, not the monthly Table 01 formula.

**Gross 26,000 below minimum wage.** Expect: **flag** as below the LKR 27,000/month floor; APIT still 0 (≤150,000).

## PROHIBITIONS

- **Table 01 residency/employment condition** — NEVER apply Table 01 without confirming the employee is a resident or Sri Lankan-citizen non-resident on a single/primary employment — other categories use different tables.  _(PROHIBITIONS section)_
- **ETF employee deduction prohibition** — NEVER deduct ETF from the employee — it is a 3% employer-only contribution.  _(PROHIBITIONS section)_
- **Double relief prohibition** — NEVER subtract the LKR 150,000 personal relief a second time — it is already inside the Table 01 formula.  _(PROHIBITIONS section)_
- **APIT gross as EPF base without checks** — NEVER reuse the APIT gross as the EPF base without checking for overtime, reimbursed travel and bonuses (which are excluded from EPF).  _(PROHIBITIONS section)_
- **EPF/ETF ceiling or floor prohibition** — NEVER apply a ceiling or floor to EPF/ETF — the percentages apply to full total earnings.  _(PROHIBITIONS section)_
- **Currency restriction** — NEVER compute payroll in any currency other than LKR.  _(PROHIBITIONS section)_
- **Penalty figures not confirmed statute** — NEVER treat the APIT penalty figures as confirmed statute — they are flagged [RESEARCH GAP].  _(PROHIBITIONS section)_
- **Deadline flagging requirement** — NEVER miss the 15th-of-following-month APIT deadline or the last-working-day EPF/ETF deadline without flagging penalty exposure.  _(PROHIBITIONS section)_
- **Minimum wage ignoring prohibition** — NEVER ignore the LKR 27,000/month minimum wage (LKR 30,000 from 1 Jan 2026) when a gross falls below it.  _(PROHIBITIONS section)_
- **Definitive computation prohibition** — NEVER present payroll computations as definitive — always label as estimated and direct to a Sri Lanka-qualified tax practitioner.  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Sri Lanka-qualified tax practitioner) before implementation.

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
