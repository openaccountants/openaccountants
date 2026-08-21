---
name: bc-eht
description: Use this skill for British Columbia Employer Health Tax — replaced MSP premiums in 2019. Different structure from Ontario EHT. Triggers "BC EHT", "British Columbia Employer Health Tax", "BC payroll tax", "EHT BC $1.5M threshold", "eTaxBC EHT". ALWAYS read alongside canada-payroll.
jurisdiction: CA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# BC Eht

## British Columbia — Employer Health Tax (EHT) — Skill v1.0

The BC Employer Health Tax (EHT) is a payroll-based tax imposed on employers under the **Employer Health Tax Act, SBC 2018, c. 42**. It is administered by the BC Ministry of Finance and filed/paid through the **eTaxBC** portal. It replaced the per-employee Medical Services Plan (MSP) premiums that BC eliminated effective January 1, 2020.

**Important — do not confuse with Ontario EHT.** Ontario's EHT (Employer Health Tax Act, RSO 1990, c. E.11) has a $1,000,000 exemption with a 1.95% top rate and is filed with the Ontario Ministry of Finance. BC's EHT shares the top rate but has different thresholds, a different sliding-scale formula, a different return (eTaxBC), and a different instalment rule. Always confirm the province before computing or filing.

## 1. Quick reference

**Quick reference table**

| Item | 2025 value |
| --- | --- |
| Statute | Employer Health Tax Act, SBC 2018, c. 42 |
| Administrator | BC Ministry of Finance (Income Taxation Branch) |
| Filing portal | eTaxBC (https://www.etax.gov.bc.ca) |
| Annual return due | **March 31** of the year following the calendar year |
| Exemption threshold (regular employers) | BC remuneration ≤ **$1,000,000** → **fully exempt** |
| Notch / sliding-scale band | **$1,000,001 – $1,500,000** → graduated up to 2.925% |
| Flat-rate band | BC remuneration **> $1,500,000** → **1.95%** on **full** payroll |
| Charities / non-profits exemption | **$1,500,000** per qualifying location |
| Charities top rate | **1.95%** on full payroll once over the cap, with a separate 2.925% notch band |
| Instalment trigger | Prior-year EHT **> $2,925** → quarterly instalments required |
| Instalment due dates | June 15, September 15, December 15, and final balance March 31 |

## 2. Required inputs + refusal catalogue

### 2.1 Required inputs

- **Required inputs list** — To compute and file BC EHT, gather: 1. Total BC remuneration for the calendar year — gross wages, salaries, bonuses, commissions, taxable benefits (T4 Box 14 equivalent), vacation pay, taxable allowances, and employer-paid stock option benefits for employees who report for work at a permanent establishment in BC (or are paid from BC if no PE). 2. Associated-employer group structure — a list of all corporations and entities under common control (within the meaning of s. 256 ITA, applied for EHT purposes) so the $1M exemption can be allocated. 3. Charitable or non-profit status — if applicable, evidence of registration (CRA registered charity number) and a list of qualifying locations. 4. Prior-year EHT liability — to determine whether quarterly instalments are required in the current year. 5. eTaxBC enrolment — the employer's BC EHT account number and eTaxBC logon credentials, or confirmation that registration is still pending.

### 2.2 Refusal catalogue — out of scope for v1.0

- **R-BC-EHT-1** — Stock-option benefits where the §7 ITA timing (exercise vs. acquisition vs. CCPC deferral) is contested.
- **R-BC-EHT-2** — Cross-border or non-resident employees where the BC permanent establishment test under s. 400 Reg. is in doubt.
- **R-BC-EHT-3** — Anti-avoidance issues under s. 32 of the EHT Act (the general anti-avoidance rule for EHT).
- **R-BC-EHT-4** — Audit, reassessment, or objection work — refer to a BC tax lawyer or designated practitioner.
- **R-BC-EHT-5** — Bankruptcy, receivership, or wind-up year returns where partial-year proration of the exemption is required.
- **R-BC-EHT-6** — Successor-employer rules where the exemption has already been used by a predecessor in the same calendar year.

## 3. Rate structure (2024 and later calendar years)

The Employer Health Tax Act, ss. 8–10, sets a three-tier structure for non-charitable employers based on total BC remuneration for the calendar year:

### 3.1 Tier 1 — Fully exempt

- **Tier 1 rule** — BC remuneration ≤ $1,000,000 → EHT = $0. No return required if the employer is not registered. Registration is mandatory only once BC remuneration exceeds the threshold (or once instalments are triggered).  _(Employer Health Tax Act, ss. 8–10)_

### 3.2 Tier 2 — Notch / sliding scale

- **Tier 2 formula** — BC remuneration between $1,000,001 and $1,500,000. Formula: EHT = 5.85% × (BC remuneration − $1,000,000). This produces an effective rate that rises from 0% at $1,000,000 to 1.95% at $1,500,000, with a marginal rate of 5.85% inside the notch. The marginal rate of 5.85% over the $500,000 notch is the mechanism that delivers the often-quoted 2.925% effective rate at the top of the notch (i.e., $1,500,000 × 1.95% ≈ $29,250, which equals 5.85% × $500,000).  _(Employer Health Tax Act, ss. 8–10)_

### 3.3 Tier 3 — Flat rate

- **Tier 3 formula** — BC remuneration > $1,500,000. Formula: EHT = 1.95% × full BC remuneration (no exemption applied; the exemption is fully phased out at this level).  _(Employer Health Tax Act, ss. 8–10)_

### 3.4 Charity / non-profit schedule (s. 9 of the Act)

- **Charity/non-profit schedule** — Registered charities and qualifying non-profit employers compute EHT per qualifying location with a higher exemption: BC remuneration ≤ $1,500,000 per location → exempt. BC remuneration $1,500,001 – $4,500,000 per location → 2.925% × (remuneration − $1,500,000). BC remuneration > $4,500,000 per location → 1.95% × full remuneration. Each qualifying location is treated separately. This is the principal structural difference from the regular-employer schedule.  _(s. 9 of the Act)_

## 4. Exemption uplift — 2024 budget change

- **2024 exemption uplift** — The exemption threshold for regular employers was raised from $500,000 to $1,000,000 for the 2024 and later calendar years, and the notch band was extended from $500,001–$1,500,000 to $1,000,001–$1,500,000, as announced in the BC Budget 2024 (Budget and Fiscal Plan 2024/25 – 2026/27, tabled February 22, 2024) and enacted through the Budget Measures Implementation Act, 2024. Effect: many small BC employers that paid EHT in 2023 are fully exempt from 2024 onward. The change does not affect the top-tier 1.95% rate or the $1.5M flat-rate threshold. The charity schedule was not changed by Budget 2024. When preparing a 2024 or 2025 return, do not use pre-2024 thresholds. When preparing a 2023 return (e.g., a late filing or amendment), use the $500,000 exemption and the $500,001 – $1,500,000 notch.  _(BC Budget 2024 (Budget and Fiscal Plan 2024/25 – 2026/27), tabled February 22, 2024; Budget Measures Implementation Act, 2024)_

## 5. Calculation — what counts as BC remuneration

- **BC remuneration inclusions** — BC remuneration is defined in s. 1 of the EHT Act and largely tracks the federal T4 reporting concept. It includes: Gross wages, salaries, and commissions paid in the calendar year. Bonuses and incentive pay. Vacation pay, statutory holiday pay, and termination/severance pay (the cash portions; retiring allowances rolled into RRSPs are excluded to the extent excluded for T4 purposes). Taxable benefits reported on T4 — including the standby charge and operating benefit, group term life insurance over $25,000, employer-paid group health premiums treated as taxable, and most non-cash benefits. Employer contributions to an Employee Profit Sharing Plan (EPSP). Stock-option benefits under §7 ITA (timing follows the federal rules). Directors' fees paid to BC-resident directors.  _(s. 1 of the EHT Act)_
- **BC remuneration exclusions** — It excludes: Pension contributions to a registered pension plan (RPP). Employer contributions to an RRSP that are not taxable to the employee in the year (rare — most employer RRSP contributions are taxable and therefore included). Reimbursements of bona fide business expenses. Most non-taxable allowances (e.g., reasonable per-kilometre motor-vehicle allowances within the CRA prescribed rate). Remuneration paid to employees who do not report for work at a BC permanent establishment and are not paid from a BC PE.  _(s. 1 of the EHT Act)_
- **Allocation rule** — Allocation rule — when an employee reports for work at PEs in more than one province during the year, allocate remuneration to BC on the same basis as federal Regulation 102 source-deduction allocation: by working days at each PE, or by a reasonable method if multiple PEs are used.  _(federal Regulation 102)_

## 6. Filing — eTaxBC return and instalments

### 6.1 Annual return

- **Annual return rules** — The annual EHT return is filed electronically through eTaxBC. There is no paper return for regular employers; charities may file by paper on request. Due date: March 31 of the year following the calendar year (so the 2025 return is due March 31, 2026). Late filing penalty: greater of $100 and 5% of the unpaid balance, plus 1% per full month for up to 12 months (s. 50 of the Act). Interest accrues on unpaid amounts at the BC prescribed rate, compounded daily.  _(s. 50 of the Act)_

### 6.2 Quarterly instalments

- **Quarterly instalment rule** — If the prior calendar year's EHT exceeded $2,925, the employer must remit quarterly instalments in the current year. Each instalment equals one-quarter of the lesser of: The prior year's EHT, or An estimate of the current year's EHT (if the employer chooses the current-year estimate method and accepts the risk of a deficiency interest charge). Instalment due dates: Q1: June 15, Q2: September 15, Q3: December 15, Final balance: March 31 with the annual return. An employer below the $2,925 prior-year threshold pays the full liability with the annual return; no instalments are required.

### 6.3 Registration

- **Registration requirement** — Registration through eTaxBC is required once BC remuneration exceeds the exemption threshold for the year, or once instalments are triggered. Late registration does not waive the obligation to file and pay for the year in which the threshold was first exceeded.

## 7. Charities and non-profits

- **Charity/non-profit definitions and treatment** — A "qualifying charity" for EHT is a registered charity under s. 248(1) ITA. A "qualifying non-profit" is an entity described in paragraph 149(1)(l) ITA. For these employers: The exemption is $1,500,000 per qualifying location (s. 9 of the EHT Act). A "qualifying location" is a permanent establishment of the charity in BC that has at least one employee reporting for work there in the year. A charity with three BC locations and $2M of remuneration spread across them (say, $700k / $700k / $600k) is fully exempt because each location is under $1.5M. The same charity with $4M at a single location pays EHT on the band $1.5M–$4M at 2.925%, plus the standard rules above $4.5M. This per-location treatment is the principal reason charities are addressed by a separate schedule rather than the regular sliding scale.  _(s. 248(1) ITA; paragraph 149(1)(l) ITA; s. 9 of the EHT Act)_

## 8. Multi-employer groups — associated employers

- **Associated employer rules** — Under s. 11 of the EHT Act, associated employers must share a single $1,000,000 exemption for the calendar year. "Associated" is defined by reference to s. 256 ITA (with EHT-specific modifications), so the federal CCPC small-business-deduction sharing concept is the relevant starting point. Mechanics: 1. The associated group files Schedule B (Allocation of Exemption Amount Among Associated Employers) with eTaxBC, allocating the $1,000,000 across members. 2. Any unallocated amount is lost; the allocation cannot exceed $1,000,000 in aggregate. 3. If members fail to file an allocation, the Minister may allocate $0 to each member by default, exposing the entire group to tax from the first dollar of payroll. 4. The notch and flat-rate thresholds are applied to the combined BC remuneration of the group only for purposes of determining which schedule applies; the tax itself is computed entity-by-entity using each member's allocated exemption. For charity groups, each member's per-location $1.5M exemption is not aggregated; the associated-employer rule applies only to the regular-employer schedule.  _(s. 11 of the EHT Act; s. 256 ITA)_

## 9. Historical context — replacement of MSP premiums

Until December 31, 2019, BC funded a significant portion of provincial health care through MSP premiums — a flat per-person monthly premium paid mostly by individuals, with many employers paying the premium as a taxable benefit. The 2018 BC Budget announced a two-step transition: January 1, 2018 — MSP premiums halved. January 1, 2019 — EHT introduced at the rates above (with the original $500k exemption). January 1, 2020 — MSP premiums eliminated entirely. For the 2019 calendar year only, employers paid both half-rate MSP and the new EHT, which is why 2019 transition workpapers often look anomalous on review. From 2020 forward, EHT is the only BC health-care payroll tax. The 2024 exemption uplift to $1,000,000 is the most recent material change.

## 10. Worked example — Vancouver tech company, $2,000,000 payroll

Facts: A Vancouver-based software company, sole BC permanent establishment. Calendar 2025 total BC remuneration: $2,000,000 (T4 Box 14 plus taxable benefits, with stock-option benefits of $150,000 under §7 ITA included). Not associated with any other employer. Not a charity. Prior-year (2024) EHT liability: $9,750 (so instalments are required in 2025).

Step 1 — Determine the schedule.
$2,000,000 > $1,500,000 → Tier 3 (flat-rate band).

Step 2 — Compute the tax.
EHT = 1.95% × $2,000,000 = $39,000.

Step 3 — Instalments.
Prior-year EHT ($9,750) > $2,925 → quarterly instalments are required. Using the prior-year safe-harbour:
- June 15, 2025: $2,437.50
- September 15, 2025: $2,437.50
- December 15, 2025: $2,437.50
Total instalments paid by year-end: $7,312.50.

Step 4 — Final balance.
Filed with the annual return on March 31, 2026:
Balance owing = $39,000 − $7,312.50 = $31,687.50.

Step 5 — Reasonableness check.
At $2M flat-band payroll the effective rate is 1.95%. Output of $39,000 matches 1.95% × $2,000,000. No reconciliation difference.

## 11. Conservative defaults

- **Conservative defaults list** — When inputs are ambiguous, apply the following defaults and flag them in the reviewer notes: 1. Permanent establishment — if it is unclear whether an employee's remuneration is BC remuneration, default to including it and flag for review. 2. Stock-option benefits — default to the §7 ITA inclusion year shown on the T4; do not override the federal timing. 3. Associated employers — if the corporate group structure is unclear, default to $0 allocated exemption for the entity being prepared and flag for review. Do not assume an exemption is available without confirming the allocation. 4. Charity status — do not apply the charity schedule unless the entity has confirmed registered-charity or paragraph 149(1)(l) status. Default to the regular schedule. 5. Instalment requirement — if the prior-year liability is not in hand, assume instalments are required if the current-year projection exceeds $2,925. 6. Late registration — if registration was late, compute tax from the first dollar over the threshold and flag the late-filing penalty exposure. 7. 2023 vs. 2024+ thresholds — confirm the calendar year before selecting the exemption amount; never apply the $1,000,000 threshold to a pre-2024 year.

## 12. Sources

- Employer Health Tax Act, SBC 2018, c. 42 — particularly ss. 1 (definitions), 8 (regular-employer schedule), 9 (charity/non-profit schedule), 10 (notch and flat-rate computation), 11 (associated employers), 32 (anti-avoidance), and 50 (penalties).
- BC Budget 2024 — Budget and Fiscal Plan 2024/25 – 2026/27, tabled February 22, 2024, announcing the exemption uplift from $500,000 to $1,000,000.
- Budget Measures Implementation Act, 2024 (SBC 2024) — enacting the threshold change.
- BC Ministry of Finance — Employer Health Tax guidance pages (gov.bc.ca/employerhealthtax), including the Notice 2024-001 series describing the exemption uplift and rate schedule.
- eTaxBC — filing portal and registration guidance (etax.gov.bc.ca).
- Medicare Protection Amendment Act, 2019 — eliminating MSP premiums effective January 1, 2020 (historical context only).
- Income Tax Act (Canada), s. 256 — associated-corporation rules applied by reference for EHT purposes.
- Income Tax Act (Canada), s. 248(1) and para. 149(1)(l) — definitions of registered charity and qualifying non-profit, applied by reference.

Companion skills — always read alongside canada-payroll (federal T4 and source-deduction context) and, where the employer has Ontario PEs as well, the Ontario EHT skill so the two regimes are not conflated.

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
