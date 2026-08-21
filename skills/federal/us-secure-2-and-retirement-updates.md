---
name: us-secure-2-and-retirement-updates
description: Tier 2 US federal content skill for SECURE Act 2.0 (Division T of CAA 2023) retirement plan changes plus IRS guidance through 2025. Covers the RMD age 73 (born 1951-1959) / 75 (born 1960+) transition, the $11,250 super catch-up for ages 60-63 effective 2025, the 2026 Roth-mandatory catch-up for $145k+ wage earners (delayed from 2024), the inherited-IRA annual RMDs during the 10-year rule effective 2025 per the July 2024 final regs, Saver's Match replacing Saver's Credit in 2027, Solo 401(k) ability to establish + fund by extended return due date, emergency-savings within plans, $1,000 emergency distribution, $10k domestic-abuse withdrawal, 529-to-Roth $35k lifetime rollover, the $108,000 QCD limit for 2025, Roth SEP and Roth SIMPLE, and the backdoor / mega-backdoor Roth mechanics with §408(d)(2) pro-rata.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Secure 2 And Retirement Updates

## US SECURE Act 2.0 and Retirement Updates (Tax Year 2025)

## 1. Scope and Companion Reading

This Tier 2 content skill covers retirement-plan rule changes wrought by:

- **SECURE Act 1.0** — Setting Every Community Up for Retirement Enhancement Act of 2019 (Division O of the Further Consolidated Appropriations Act 2020, P.L. 116-94, enacted December 20, 2019).
- **SECURE Act 2.0** — Division T of the Consolidated Appropriations Act 2023 (P.L. 117-328, enacted December 29, 2022). Roughly 90 provisions phased in across 2023-2033.
- **IRS Guidance through November 2025**, including:
  - **Notice 2022-53** (RMD relief for 2021-2022 inherited IRAs)
  - **Notice 2023-54** (RMD relief for 2023)
  - **Notice 2024-35** (RMD relief for 2024)
  - **Notice 2023-62** (Roth catch-up administrative transition, two-year delay to 2026)
  - **Notice 2024-2** ("Grab Bag" guidance on numerous SECURE 2.0 provisions)
  - **Final regulations TD 10001** (July 19, 2024) on RMDs and the 10-year rule
  - **Proposed regs REG-103529-23** (July 2024) on SECURE 2.0 RMD changes
  - **Rev. Proc. 2024-40** (2025 inflation adjustments)

This skill is the **companion** to `us-self-employed-retirement` (which covers the core Solo 401(k) / SEP-IRA / SIMPLE-IRA / IRA mechanics for self-employed taxpayers). This skill focuses on the **rule changes layered on top of that baseline** by SECURE 1.0 and 2.0 plus the post-enactment IRS guidance.

**Federal only.** State retirement-plan add-ons (CalSavers, Illinois Secure Choice, etc.) are out of scope and belong in state skills.

### What this skill does NOT cover

- Defined-benefit plan funding rules (PBGC, §430 valuations)
- ESOP transactions and §1042 rollovers
- Excess-business-loss limitations under §461(l) interacting with retirement deductions
- Section 457(f) ineligible deferred compensation
- Multi-employer plan withdrawal liability
- Cash-balance plan design

For those, the reviewer should engage an ERISA actuary or specialist.

## 2. SECURE Act 1.0 (2019) Baseline

Before SECURE 2.0 stacked another set of changes on top, SECURE 1.0 (effective for tax years beginning after Dec 31, 2019, with some exceptions) made the following foundational changes that still govern 2025 returns:

### 2.1 RMD age 70½ → 72

- **RMD age raised to 72** — Old §401(a)(9): required beginning date was April 1 of the year following the year the participant attained age 70½. SECURE 1.0 §114 raised the age to 72 for participants who attain age 70½ after December 31, 2019 (i.e., born July 1, 1949 or later). This was then raised again by SECURE 2.0 (see §3.1 below).  _(SECURE 1.0 §114; old §401(a)(9))_

### 2.2 Death of the Stretch IRA — the 10-year rule

- **10-year rule for non-spouse beneficiaries** — Pre-2020: a designated beneficiary could "stretch" inherited IRA distributions over their own life expectancy, deferring tax for decades. SECURE 1.0 §401 imposed a 10-year rule for most non-spouse designated beneficiaries: the entire inherited account must be distributed by December 31 of the year containing the 10th anniversary of the participant's death. Applies to participants who died after December 31, 2019. Eligible Designated Beneficiaries (EDBs) retained life-expectancy stretch (see §16 for the 2024 final regs).  _(SECURE 1.0 §401)_

### 2.3 Increased small-employer plan startup credit — §45E

- **§45E startup credit increase** — SECURE 1.0 raised the §45E small-employer pension-plan startup cost credit from a flat $500 to up to $5,000 per year for 3 years. SECURE 2.0 then dramatically expanded this further to a 100% credit for small employers (≤50 employees) — see §3.  _(§45E; SECURE 1.0)_

### 2.4 Removal of age cap on traditional IRA contributions

- **No age cap on traditional IRA contributions** — SECURE 1.0 §107 repealed the §219(d)(1) prohibition on traditional-IRA contributions after age 70½. Beginning 2020, a working person of any age can contribute to a traditional IRA if they have earned income. Still in force in 2025.  _(SECURE 1.0 §107; §219(d)(1))_

### 2.5 Penalty-free birth/adoption distribution — §72(t)(2)(H)

- **Birth/adoption distribution up to $5,000** — Up to $5,000 per parent per birth or adoption can be withdrawn from a qualified plan or IRA within one year of the qualifying event, free of the 10% §72(t) early-withdrawal penalty. SECURE 2.0 extended the repayment window — see §10.  _(§72(t)(2)(H))_

### 2.6 Long-term part-time employee inclusion

- **LTPT employee inclusion — 3-year rule (SECURE 1.0)** — SECURE 1.0 §112: 401(k) plans must allow employees who worked 500 hours per year for 3 consecutive years to make elective deferrals. SECURE 2.0 reduced this to 2 consecutive years beginning 2025 (see §6.5 below).  _(SECURE 1.0 §112)_

## 3. SECURE 2.0 (2022) — Effective-Date Master Table

This table maps the major provisions to their effective tax year. Provisions that affect a 2025 federal tax return are highlighted with [2025 RELEVANT].

**SECURE 2.0 Effective-Date Master Table**  _(Table verbatim from source)_

| § | Provision | Effective | 2025 Impact |
| --- | --- | --- | --- |
| 101 | Auto-enrollment for new 401(k)/403(b) plans | Plan years after Dec 31, 2024 | **[2025 RELEVANT]** §6 |
| 102 | Modify §45E startup credit — 100% credit | TY 2023+ | Still active |
| 103 | Saver's Match replaces Saver's Credit | TY 2027+ | Planning only |
| 107 | RMD age 73 (born 1951-1959) / 75 (born 1960+) | TY 2023+ / TY 2033+ | **[2025 RELEVANT]** §4 |
| 109 | Higher catch-up — ages 60-63 super catch-up | TY 2025+ | **[2025 RELEVANT]** §5 |
| 110 | Student loan match | Plan years after Dec 31, 2023 | Active |
| 113 | Small immediate financial-incentive (gift cards) | DOE | Active |
| 115 | Penalty-free emergency distribution $1,000 | TY 2024+ | **[2025 RELEVANT]** §11 |
| 116 | Multiple Employer 403(b) | Plan years after Dec 31, 2022 | Active |
| 117 | SIMPLE-IRA higher contribution limits | TY 2024+ | Active |
| 121 | Starter 401(k) | Plan years after Dec 31, 2023 | Active |
| 126 | 529-to-Roth IRA rollover | TY 2024+ | **[2025 RELEVANT]** §13 |
| 127 | Pension-Linked Emergency Savings Account (PLESA) | Plan years after Dec 31, 2023 | **[2025 RELEVANT]** §11 |
| 201 | Qualified Longevity Annuity Contracts (QLACs) | DOE | Active |
| 202 | QLAC limit raised, no 25% AV cap | DOE | Active |
| 302 | RMD excise tax 50% → 25% (10% if cured) | TY 2023+ | **[2025 RELEVANT]** §4.5 |
| 307 | QCD indexed; one-time $50k QCD-to-CRT | TY 2023+ | **[2025 RELEVANT]** §14 |
| 314 | $10k domestic-abuse distribution | TY 2024+ | **[2025 RELEVANT]** §11.3 |
| 317 | Sole prop Solo 401(k) — establish by tax-return due date | TY 2023+ | **[2025 RELEVANT]** §9 |
| 325 | Roth not subject to RMDs (during owner's lifetime) | TY 2024+ | **[2025 RELEVANT]** §4.6 |
| 326 | Penalty-free distribution for terminally ill | TY 2023+ | Active |
| 327 | Surviving spouse RMD election | TY 2024+ | Active |
| 334 | Long-term care insurance distribution | TY 2026+ | Planning only |
| 601 | Roth SEP and Roth SIMPLE allowed | TY 2023+ | **[2025 RELEVANT]** §15 |
| 603 | Catch-up Roth-mandatory for $145k+ | TY 2024 (DELAYED to TY 2026) | Planning only — see §7 |
| 604 | Roth treatment of employer matching | DOE | Active |

DOE = Date of Enactment, December 29, 2022.

## 4. RMD Age Transition

This is the single most operationally important SECURE 2.0 change for 2025 returns because **2025 is the first year that ushers in mandatory annual inherited-IRA RMDs** under the final regs (see §16), and because misidentifying a client's RMD age generates penalty exposure.

### 4.1 The age bands

Under §107 of SECURE 2.0, the required beginning date (RBD) is now determined by the participant's year of birth:

**RMD age bands by year of birth**  _(SECURE 2.0 §107)_

| Year of Birth | RMD Age | First RBD |
| --- | --- | --- |
| Before July 1, 1949 | 70½ | Already past |
| July 1, 1949 – Dec 31, 1950 | 72 | Already past |
| 1951 – 1959 | **73** | April 1 of year following age 73 |
| 1960 or later | **75** | April 1 of year following age 75 |

### 4.2 2025 transition cases

**Born 1952 (turning 73 in 2025).** This taxpayer's first distribution year is **2025**. The required beginning date is **April 1, 2026**. The taxpayer may elect to:

- Defer the first RMD until April 1, 2026 (resulting in two RMDs in calendar 2026 — the 2025 RMD by 4/1/2026 plus the 2026 RMD by 12/31/2026), or
- Take the first RMD by December 31, 2025 (and one RMD per year thereafter).

**Born 1953 (turning 72 in 2025).** This taxpayer is **not yet RMD-eligible**. The first RMD year will be 2026 (age 73), with RBD of April 1, 2027.

**Born 1960 (turning 65 in 2025).** Falls in the second age band. No RMD until age 75 (year 2035), RBD April 1, 2036.

**Born 1951 (turning 74 in 2025).** First RMD year was **2024** (age 73). The 2024 RMD could have been deferred to April 1, 2025 (creating a stacked-RMD year). The 2025 RMD is due December 31, 2025.

### 4.3 Computing the RMD amount

Use the **Uniform Lifetime Table** (Treas. Reg. §1.401(a)(9)-9 as amended November 2020). 2025 example divisors:

**Uniform Lifetime Table divisors**  _(Treas. Reg. §1.401(a)(9)-9 as amended November 2020)_

| Age | Divisor |
| --- | --- |
| 73 | 26.5 |
| 74 | 25.5 |
| 75 | 24.6 |
| 76 | 23.7 |
| 77 | 22.9 |
| 80 | 20.2 |
| 85 | 16.0 |
| 90 | 12.2 |
| 95 | 8.9 |

- **Joint and Last Survivor Table use case** — If the sole beneficiary is a spouse more than 10 years younger, use the Joint and Last Survivor Table instead.  _(Treas. Reg. §1.401(a)(9)-9)_
- **RMD calculation formula** — Prior-year-end account balance ÷ divisor = RMD.  _(Treas. Reg. §1.401(a)(9)-9)_

### 4.4 Aggregation rules

- **Traditional IRAs aggregation** — Traditional IRAs: aggregate the prior-year-end balances of all the participant's traditional IRAs and SEP-IRAs and SIMPLE-IRAs; the resulting total RMD may be withdrawn from any one of them.
- **403(b) aggregation** — 403(b) accounts: separate aggregation rule — 403(b) RMDs may be aggregated across the participant's 403(b)s but not with IRAs.
- **401(k), 401(a), 457(b) no aggregation** — 401(k), 401(a), 457(b), other defined-contribution plans: NO aggregation. Each plan computes and pays its own RMD separately.

### 4.5 §4974 excise tax — reduced from 50% to 25% (10% if cured)

- **Pre-SECURE 2.0 50% excise tax** — Pre-SECURE 2.0: missing an RMD triggered a 50% excise tax on the shortfall under §4974(a). This was the harshest penalty in the Code.  _(§4974(a))_
- **§4974 excise tax on missed RMD (post SECURE 2.0)** — 25% (reduced to 10% if corrected within the correction window (generally 2 years from when the tax was first owed))  _(SECURE 2.0 §302 (effective TY 2023+))_
- **Correction requirement** — "Correction" requires actually taking the missed distribution and filing Form 5329 for the year(s) involved.  _(SECURE 2.0 §302)_
- **Form 5329 waiver request** — Even after SECURE 2.0, the IRS retains discretion under §4974(d) to waive the excise tax entirely upon a showing of reasonable cause and that reasonable steps are being taken to remedy the shortfall. Attach a written explanation to Form 5329 and write "RC" in the margin next to the waiver line.  _(§4974(d))_

**AUDIT FLASH POINT — missed 2025 inherited IRA RMDs.** The 2024 final regs end the 2020-2024 transitional waiver of annual inherited-IRA RMDs (see §16). Many beneficiaries who inherited from a participant who had already reached their RBD have NOT been taking annual RMDs because the IRS waived the requirement during 2021-2024 by successive notices. Starting in 2025, the annual RMD is required, and the §4974 excise tax (now 25% / 10%) applies to any shortfall. **Every inherited-IRA client should be re-screened for 2025 RMD compliance during return preparation.**

### 4.6 Roth IRA and Roth 401(k) — no RMD during owner's lifetime (post-2023)

- **Roth IRA RMD exemption baseline** — Roth IRAs have always been RMD-exempt during the owner's lifetime.
- **Designated Roth accounts RMD exemption** — Designated Roth accounts in 401(k), 403(b), and governmental 457(b) plans are also exempt from RMDs during the participant's lifetime beginning tax year 2024. (Prior to 2024, Roth 401(k) accounts had to begin distributions at the RBD.) Beneficiary RMDs after the owner's death still apply.  _(SECURE 2.0 §325)_

**Planning consequence**: many retirees now defer Roth 401(k) → Roth IRA rollovers because the Roth 401(k) no longer forces distributions at RBD.

## 5. Super Catch-up for Ages 60-63 — §414(v)(2)(E)

**Effective tax year 2025.** This is one of the most operationally important provisions for 2025 returns because clients turning 60-63 in 2025 can contribute meaningfully more.

### 5.1 The rule

- **Super catch-up definition** — Under SECURE 2.0 §109, for participants who attain age 60, 61, 62, or 63 by the end of the plan year, the catch-up contribution limit is the greater of: $10,000 (indexed for inflation after 2025), OR 150% of the regular age-50 catch-up limit for the year.  _(SECURE 2.0 §109)_

**401(k)/403(b)/gov 457(b) 2025 catch-up amounts**  _(SECURE 2.0 §109)_

| Item | 2025 Amount |
| --- | --- |
| Regular employee deferral limit §402(g) | $23,500 |
| Age-50 catch-up §414(v)(2)(B)(i) | $7,500 |
| **Super catch-up ages 60-63** | **$11,250** (= $7,500 × 150%) |
| Total deferral, age 50-59 | $31,000 |
| **Total deferral, age 60-63** | **$34,750** |
| Total deferral, age 64+ | $31,000 (back to regular catch-up) |

**SIMPLE-IRA/SIMPLE-401(k) 2025 catch-up amounts**  _(SECURE 2.0 §109)_

| Item | 2025 Amount |
| --- | --- |
| Regular deferral limit | $16,500 |
| Age-50 catch-up | $3,500 |
| **Super catch-up ages 60-63** | **$5,250** (= $3,500 × 150%) |

### 5.2 The age-64 cliff

- **Age-64 cliff for super catch-up** — The super catch-up applies only in the years the participant is age 60, 61, 62, or 63 at year-end. Once the participant attains age 64 by year-end, the catch-up drops back to the regular $7,500 (indexed). This creates a four-year window for accelerated contributions.  _(SECURE 2.0 §109)_

### 5.3 Plan-document requirement

- **Plan-document amendment deadline** — The plan document must permit the super catch-up. SECURE 2.0 amendments are mandatory but the IRS extended the formal plan-amendment deadline to December 31, 2026 for most plans (Notice 2024-2, Q-1). Operational compliance must occur on the effective date even if the plan-document amendment is later.  _(Notice 2024-2, Q-1)_

### 5.4 Self-employed Solo 401(k) eligibility

- **Solo 401(k) super catch-up eligibility** — Solo 401(k) participants — typically the sole proprietor and any working spouse — qualify for the super catch-up if they are age 60-63 at year-end and the Solo 401(k) plan document permits it. Most prototype Solo 401(k) plan documents from major providers (Fidelity, Schwab, ETrade, Vanguard) were updated in 2024-2025 to include the super catch-up.

### 5.5 Interaction with the Roth catch-up mandate

- **Super catch-up subject to §603 Roth mandate** — The super catch-up is also subject to the §603 Roth catch-up mandate for high earners once that takes effect in 2026 (see §7). A 62-year-old with prior-year FICA wages > $145k will, beginning in 2026, be required to make the entire $11,250 super catch-up as Roth.  _(SECURE 2.0 §603)_

## 6. Automatic Enrollment Mandate — §414A

**Effective plan years beginning after December 31, 2024** — so the first 2025 calendar-year plans must comply on January 1, 2025.

### 6.1 The mandate

- **EACA mandate features** — Under SECURE 2.0 §101, new 401(k) and 403(b) plans established after December 29, 2022 must adopt an Eligible Automatic Contribution Arrangement (EACA) with the following features: - Auto-enrollment at a default deferral rate between 3% and 10% of compensation. - Automatic escalation of +1 percentage point per year until the rate reaches at least 10% (cannot escalate above 15%). - Permissible withdrawal: employees may opt out within 90 days and withdraw auto-contributions without the 10% §72(t) penalty. - Qualified Default Investment Alternative (QDIA) must hold the auto-enrolled contributions (typically a target-date fund).  _(SECURE 2.0 §101)_

### 6.2 Plans EXEMPT from the auto-enrollment mandate

- **Exemptions from auto-enrollment mandate** — A plan is NOT required to auto-enroll if it is: 1. A SIMPLE 401(k) plan under §401(k)(11). 2. A governmental plan under §414(d). 3. A church plan under §414(e). 4. Maintained by an employer with 10 or fewer employees (counting all employees aggregated under §414(b)/(c)/(m)/(o)). 5. Maintained by an employer less than 3 years in business. 6. Grandfathered — established on or before December 29, 2022. (This is the key exception: plans existing on the date of enactment of SECURE 2.0 are exempt, regardless of when 2025 begins.)  _(SECURE 2.0 §101)_

### 6.3 What this means for self-employed clients

A Solo 401(k) maintained by a sole proprietor for the proprietor (and spouse) is technically a 401(k) plan. However:

- It almost certainly qualifies for the ≤10 employee exception (#4), and
- A Solo 401(k) established before December 29, 2022 is also grandfathered (#6).
- Even if it qualified for neither, the auto-enrollment rules apply only to deferrals from W-2 employees. A sole proprietor's elective deferrals come out of self-employment earnings, not W-2 wages, and the proprietor is making an affirmative deferral election anyway.

**Practical answer**: Solo 401(k)s for self-employed clients are effectively outside the §414A mandate. Confirm with the plan provider that the prototype document does not require auto-enrollment for any employee participants.

### 6.4 Penalty for non-compliance

- **Auto-enrollment non-compliance penalties** — Failure to auto-enroll exposes the plan to §401(k) qualification disqualification, EPCRS correction filings, and §6652 penalties of $100 per missed enrollee per day. Most 401(k) providers have updated their plan documents and recordkeeping platforms to enforce this automatically.  _(§6652)_

### 6.5 Long-term part-time employee inclusion — accelerated

- **LTPT eligibility reduced to 2 years** — SECURE 2.0 §125 reduced the SECURE 1.0 LTPT eligibility threshold from 3 consecutive years of 500+ hours to 2 consecutive years of 500+ hours. Effective 2025: LTPT employees who completed 500+ hours in 2023 and 2024 must be allowed to defer beginning January 1, 2025. They are not required to be included in employer match or top-heavy testing.  _(SECURE 2.0 §125)_

## 7. Roth Catch-up Mandate — §603 (Delayed to 2026)

This is the most contested SECURE 2.0 provision. **Originally effective 2024**, the IRS delayed enforcement to **tax year 2026** via Notice 2023-62 and again confirmed in subsequent guidance.

### 7.1 The rule

- **Roth catch-up mandate for high earners** — Under §603, catch-up contributions (the age-50 / age-60-63 catch-ups) made to 401(k), 403(b), and governmental 457(b) plans by an employee whose prior-year FICA wages exceeded $145,000 (indexed; the threshold for catch-ups made in 2026 will be based on 2025 FICA wages > $145,000 indexed) MUST be made as Roth (after-tax) contributions. The catch-up cannot be made on a pre-tax basis.  _(SECURE 2.0 §603)_
- **Roth catch-up mandate FICA wage threshold** — $145,000 USD (prior-year FICA wages, indexed)  _(SECURE 2.0 §603)_

### 7.2 What it does NOT apply to

- **Exclusions from §603 Roth mandate** — - IRA catch-ups (the $1,000 age-50 IRA catch-up under §219(b)(5)(B)) — these can still be traditional. - SIMPLE-IRA catch-ups — these are NOT subject to §603. - The first $23,500 of regular elective deferrals — only the catch-up portion is Roth-mandatory. - Self-employed taxpayers whose income is reported on Schedule C — the $145,000 threshold is measured by FICA wages (Box 3 of W-2). A sole proprietor has no Box 3 wages; their self-employment earnings are subject to SE tax but are not "FICA wages" for §603 purposes. Therefore a high-earning sole proprietor's Solo 401(k) catch-up remains traditional-eligible under current guidance.  _(§219(b)(5)(B); SECURE 2.0 §603)_

### 7.3 The administrative transition relief

- **Notice 2023-62 transition relief** — Notice 2023-62 provided a 2-year administrative transition period through December 31, 2025, during which plan sponsors that have not yet implemented the Roth catch-up mandate are not subject to penalty even if they allow high earners to make pre-tax catch-ups. First mandatory year: 2026.  _(Notice 2023-62)_

### 7.4 Plan-document changes required

- **Required plan-document amendments for §603** — Plans must either: - Amend to permit Roth (designated Roth) contributions if they don't already (most plans already do), and - Amend to automatically classify the catch-up of an over-$145k earner as Roth, or - Eliminate the catch-up feature for over-$145k earners (rare).

### 7.5 Practical worked through

Suppose a corporate employee earned $200,000 W-2 wages in 2025 and turns 52 in 2026. In 2026:

- Regular deferral: $23,500 + indexing — can be pre-tax (or Roth at employee's election).
- Catch-up: $7,500 + indexing — MUST be Roth.
- The employee cannot reduce 2026 taxable income via a pre-tax catch-up.

This is roughly a $1,800 cost (assuming 24% marginal bracket on $7,500).

**AUDIT FLASH POINT — Roth catch-up violations in 2026.** Plan sponsors that fail to enforce Roth treatment of catch-ups for over-$145k earners in 2026 are operating in violation of §603. The plan can use EPCRS to correct, but the corrective contributions are taxable to the employee. Reviewers should confirm that 2026 plan administration treats high-earner catch-ups as Roth.

## 8. Saver's Match — §103 (Effective 2027)

Beginning tax year 2027, the existing nonrefundable Saver's Credit under §25B is replaced by a federal matching contribution deposited directly into the taxpayer's retirement account.

### 8.1 The mechanics

- **Saver's Match mechanics** — - Match rate: 50% of contributions, up to the first $2,000 contributed. - Maximum federal match: $1,000 per individual. - Deposit destination: directly into the taxpayer's IRA or qualified plan, NOT a refund. - Refundability: the match is technically a refundable credit, but the credit cannot be paid in cash — it must flow into a retirement account.  _(SECURE 2.0 §103; §25B)_

### 8.2 Phaseout thresholds (2027 statutory amounts, will be indexed)

**Saver's Match phaseout thresholds by filing status**  _(SECURE 2.0 §103)_

| Filing Status | Phaseout Begins | Phaseout Ends |
| --- | --- | --- |
| Single / MFS | $20,500 | $35,500 |
| Head of Household | $30,750 | $53,250 |
| Married Filing Jointly | $41,000 | $71,000 |

- **Linear phaseout scaling** — Within the phaseout range, the match scales linearly from 50% down to 0%.

### 8.3 2025 status

For tax year 2025, the legacy Saver's Credit under §25B still applies as a nonrefundable credit. No 2025 return mentions the Saver's Match. Practitioners should flag the upcoming transition in 2027 planning memos.

## 9. Solo 401(k) Liberalization — §317

This is a meaningful change for self-employed sole proprietors and single-member LLCs.

### 9.1 Pre-SECURE 2.0 rule

- **Pre-SECURE 2.0 Solo 401(k) establishment deadline** — A Solo 401(k) plan had to be established by the last day of the tax year in order for the sole proprietor to make any contributions (employee deferral or employer profit-sharing) for that year. A taxpayer who realized in March 2024 that they wanted to contribute for 2023 was out of luck because the plan didn't exist on 12/31/2023.

### 9.2 SECURE 2.0 §317 rule (effective TY 2023+)

- **Extended Solo 401(k) establishment deadline** — A sole proprietor (or single-member LLC disregarded for federal tax) may now establish AND fund the employer (profit-sharing) portion of a Solo 401(k) up to the tax-return due date including extensions (i.e., October 15, 2026 for TY 2025 returns extended).  _(SECURE 2.0 §317)_
- **Employee deferral deadline unchanged** — HOWEVER: The employee deferral portion of a Solo 401(k) must still be elected by December 31 of the tax year. Practically, this means a taxpayer who has not signed a deferral election by 12/31/2025 cannot retroactively make the $23,500 employee deferral for 2025 — only the employer profit-sharing (up to 25% of net SE earnings, subject to the §415(c) overall cap of $70,000 for 2025) can be made retroactively.  _(SECURE 2.0 §317; §415(c))_

### 9.3 §415(c) limit recap for 2025

**§415(c) limit recap for 2025**  _(§415(c); §401(a)(17))_

| Item | 2025 |
| --- | --- |
| §415(c) total DC plan limit | $70,000 |
| §402(g) employee deferral | $23,500 |
| Age-50 catch-up | $7,500 |
| Super catch-up (60-63) | $11,250 |
| §415(c) including catch-up (50-59) | $77,500 |
| §415(c) including super catch-up (60-63) | $81,250 |
| Compensation cap §401(a)(17) | $350,000 |

### 9.4 Comparison table — Solo 401(k) vs SEP-IRA after SECURE 2.0

**Solo 401(k) vs SEP-IRA comparison**  _(SECURE 2.0; §408(d))_

| Feature | Solo 401(k) | SEP-IRA |
| --- | --- | --- |
| Establish by 12/31 of plan year | Employee deferral: YES. Employer: NO (extended to return due date) | NO (extended to return due date) |
| Roth contributions accepted (post §601) | YES | YES (TY 2023+) |
| Employee deferral component | $23,500 + catch-up | NO |
| Employer profit-sharing component | Up to 25% of net SE × 0.9235 | Up to 25% of net SE × 0.9235 (effective 20%) |
| §415(c) cap | $70,000 (+ catch-up) | $70,000 |
| Loans permitted | YES (up to $50k or 50% AV) | NO |
| §408(d) pro-rata applies to backdoor Roth? | NO (Solo 401(k) is not an IRA) | YES (SEP balance counts) |
| Form 5500-EZ required | Once plan assets ≥ $250k | NO |
| Administrative complexity | Medium | Low |

- **Backdoor Roth interaction** — **Backdoor Roth interaction**: a sole proprietor weighing Solo 401(k) vs SEP-IRA should consider that SEP-IRA balances are aggregated with traditional IRAs for §408(d)(2) pro-rata purposes when executing a backdoor Roth. A SEP-IRA balance of $200,000 can effectively kill the tax-free backdoor Roth strategy. Solo 401(k) balances are NOT subject to §408(d)(2) — they are in a separate plan type — making the Solo 401(k) the strategically superior vehicle for taxpayers who want to maintain backdoor Roth capability. See §17.  _(§408(d)(2))_

### 9.5 Roth Solo 401(k) employer contributions (§604)

- **Roth employer contributions permitted** — SECURE 2.0 §604 (DOE, December 29, 2022) permits employer contributions to be designated Roth at the employee's election, provided the plan permits it. Most Solo 401(k) prototype documents added this feature in 2023-2024.  _(SECURE 2.0 §604)_
- **Roth employer contribution tax treatment** — The Roth employer contribution is fully vested immediately (per §604), is included in the employee's gross income for the year of contribution, and is reported on Form 1099-R with code "G" (direct rollover) at the time of the in-plan designation.  _(SECURE 2.0 §604)_

## 10. Pre-existing penalty exceptions and their SECURE 2.0 enhancements

### 10.1 Birth or adoption distribution — §72(t)(2)(H)

- **Birth/adoption distribution rules and repayment window** — - SECURE 1.0: up to $5,000 per parent per qualifying event, no 10% penalty, repayable. - SECURE 2.0 §311: extended the repayment window from indefinite to 3 years from the date of distribution. Repayment is treated as a rollover.  _(§72(t)(2)(H); SECURE 2.0 §311)_

### 10.2 Terminally ill distribution — §72(t)(2)(L)

- **Terminally ill distribution rule** — SECURE 2.0 §326 (TY 2023+): up to a participant's entire vested balance can be withdrawn without the 10% penalty if the participant has been certified by a physician as terminally ill (life expectancy ≤ 7 years per IRS guidance).  _(§72(t)(2)(L); SECURE 2.0 §326)_

### 10.3 Public safety officer extension

- **Public safety officer exception extension** — SECURE 2.0 §308: the §72(t)(10) exception for public safety officers separating from service in or after the year of age 50 now extends to private-sector firefighters and is broadened to apply at age 50 or 25 years of service (whichever is earlier).  _(§72(t)(10); SECURE 2.0 §308)_

## 11. Emergency Savings and Distributions

### 11.1 $1,000 emergency distribution — §72(t)(2)(I) (SECURE 2.0 §115)

- **$1,000 emergency distribution rule** — Effective tax year 2024+. A participant may withdraw up to $1,000 per calendar year from a qualified plan or IRA, free of the 10% §72(t) penalty, for any unforeseeable or immediate financial need for personal or family emergency expenses. The withdrawal is still subject to ordinary income tax. - One distribution per year. - Repayment: the participant may repay within 3 years. Until repaid (or the 3-year window closes), the participant cannot take another emergency distribution. - Self-certification: the participant self-certifies the emergency to the plan administrator. No documentation required.  _(§72(t)(2)(I); SECURE 2.0 §115)_

### 11.2 Pension-Linked Emergency Savings Account (PLESA) — §127

- **PLESA rules** — Effective plan years beginning after December 31, 2023. A 401(k)/403(b) sponsor may offer a PLESA to non-highly-compensated employees: - Maximum balance: $2,500 (indexed). Contributions cease when balance reaches the cap. - Roth treatment: contributions are after-tax (Roth), no taxation on withdrawal. - Withdrawals: at least 4 per year must be permitted free of fees. - Employer match: employer may match PLESA contributions to the underlying 401(k) (NOT to the PLESA itself) up to plan match limits. - Auto-enroll permitted: sponsor may auto-enroll at up to 3% of comp.  _(SECURE 2.0 §127)_

Most self-employed taxpayers do not have PLESAs because they don't sponsor multi-employee plans. The provision matters mainly for clients who are employees of larger sponsors.

### 11.3 Domestic abuse distribution — §72(t)(2)(K) (SECURE 2.0 §314)

- **Domestic abuse distribution rule** — Effective tax year 2024+. A participant who is a victim of domestic abuse by a spouse or domestic partner may withdraw up to the lesser of $10,000 (indexed) or 50% of the account balance without the 10% penalty. - Self-certification: participant self-certifies the abuse; no documentation required. - Repayable: within 3 years, treated as a rollover. - Includible in income in the year of distribution, but the income may be recouped via the repayment.  _(§72(t)(2)(K); SECURE 2.0 §314)_

### 11.4 Disaster-related distribution — §72(t)(2)(M) (SECURE 2.0 §331)

- **Disaster-related distribution rule** — Effective for disasters occurring after January 26, 2021. Up to $22,000 of "qualified disaster recovery distribution" is exempt from the 10% penalty, may be spread over 3 years of taxable income, and is repayable within 3 years. This essentially codifies the ad hoc disaster relief that Congress had been passing on an event-by-event basis since 2017.  _(§72(t)(2)(M); SECURE 2.0 §331)_

### 11.5 Long-term care insurance premium distribution — §72(t)(2)(N) (SECURE 2.0 §334)

- **LTC insurance premium distribution rule** — Effective tax year 2026+. Up to $2,500 per year (indexed) may be distributed from a retirement plan to pay LTC insurance premiums for the participant or spouse without the 10% penalty. The distribution is still subject to ordinary income tax. Not in force for 2025 returns — planning only.  _(§72(t)(2)(N); SECURE 2.0 §334)_

## 12. Small Immediate Financial Incentive — §113

- **Small immediate financial incentive rule** — SECURE 2.0 §113 (DOE) permits an employer to offer a small immediate financial incentive (e.g., a gift card) to induce employees to enroll in a 401(k). The incentive must be de minimis (the IRS has indicated $250 or less) and must be paid from employer funds, NOT from plan assets.  _(SECURE 2.0 §113)_

Practical effect: small employer can give a $50 Amazon gift card for signing up. Most self-employed clients won't encounter this.

## 13. 529 → Roth IRA Rollover — §126

Effective tax year 2024+. A long-overdue provision allowing untouched 529 plan funds to be rolled to a Roth IRA in the beneficiary's name.

### 13.1 Conditions

- **529 must be maintained for at least 15 years** — The 529 plan must have been maintained for at least 15 years.  _(§126)_
- **Rollover destination** — The rollover destination is a Roth IRA in the name of the 529 beneficiary (not the account owner).  _(§126)_
- **Contributions in prior 5 years not eligible** — Contributions made in the prior 5 years (and earnings on them) are NOT eligible for rollover.  _(§126)_
- **Annual rollover cap** — $7,000 for 2025; $8,000 if age 50+, reduced by other IRA contributions made for the year USD (annual, equal to IRA contribution limit)  _(§126)_
- **Lifetime cap on rollovers per beneficiary** — $35,000 USD  _(§126)_
- **Earned income requirement** — The beneficiary must have earned income at least equal to the rollover amount (the rollover counts as an IRA contribution and is subject to the earned-income requirement of §219(b)).  _(§219(b))_

### 13.2 What it DOES NOT do

- **No tax deduction** — Does not provide a tax deduction (it's a Roth contribution).
- **Does not eliminate penalty automatically** — Does not eliminate the §529 10% earnings penalty if the funds were never going to be used for education — the rollover is the avoidance mechanism.  _(§529)_
- **No traditional IRA rollovers** — Does not allow rolling 529s to traditional IRAs.
- **15-year clock reset uncertainty** — Does not reset the 15-year clock if the 529 owner switches beneficiaries — there is open uncertainty about whether a beneficiary change resets the 15-year clock; conservative position is YES, it resets.

### 13.3 Worked example

A 529 was opened in 2008 with the beneficiary's daughter as recipient. The daughter is now 24 in 2025 with earned income of $50,000. Account balance: $42,000. Contributions in 2021-2025: $10,000 (these are not eligible). Eligible rollover principal: $32,000 (plus relevant earnings).

For tax year 2025: rollover up to $7,000 to Roth IRA (subject to daughter not having made any other IRA contributions). For tax years 2026-2030: similar annual rollovers, total cumulative cap $35,000.

## 14. Qualified Charitable Distribution (QCD) — §307

### 14.1 Pre-existing rule

- **QCD age and amount** — A taxpayer age 70½ or older may direct up to $100,000 from an IRA directly to a qualified charity. The QCD is excluded from gross income (does not appear in AGI) and counts toward the taxpayer's RMD for the year.  _(§307)_

### 14.2 SECURE 2.0 enhancements

- **QCD annual limit indexed for inflation** — $105,000 in 2024, $108,000 in 2025, projected ~$112,000 in 2026 USD  _(§307)_
- **One-time QCD to CGA or CRT** — One-time $50,000 QCD to a Charitable Gift Annuity (CGA) or Charitable Remainder Trust (CRT) (also indexed; $54,000 in 2025). This is a one-shot lifetime opportunity — once used, the taxpayer cannot use it again. USD  _(§307)_

### 14.3 RMD interaction

The QCD reduces the otherwise-required RMD on a dollar-for-dollar basis. Example: taxpayer's 2025 RMD is $40,000. She directs $30,000 as a QCD to her alma mater. She must then withdraw at least $10,000 to herself (or another QCD) to satisfy the RMD. The $30,000 QCD is excluded from her AGI, which helps with IRMAA Medicare premium thresholds and the §86 Social Security inclusion calculation.

### 14.4 No double-dip

- **No Schedule A double dip** — The QCD cannot also be claimed as a charitable deduction on Schedule A. The exclusion from gross income is the tax benefit.

### 14.5 Form 1040 reporting

- **QCD reporting steps** — QCD reporting is by hand: Form 1099-R from the IRA custodian reports the full distribution (gross). On Form 1040 Line 4a, enter the gross IRA distribution. On Line 4b, enter the taxable portion (gross minus QCD). Write "QCD" next to Line 4b. The IRA custodian does NOT separately code a QCD on the 1099-R; the responsibility falls on the taxpayer to identify it.

## 15. Roth SEP and Roth SIMPLE — §601

Effective date of enactment (December 29, 2022). Previously, SEP-IRAs and SIMPLE-IRAs were pre-tax only. SECURE 2.0 §601 permits employers (including sole proprietors) to make designated Roth contributions to these vehicles.

### 15.1 Mechanics

- **Employee election per contribution** — The Roth designation is at the employee's election for each contribution (an employee can split: part pre-tax, part Roth).
- **Roth contribution included in gross income** — The Roth contribution is included in gross income in the year of contribution.
- **5-year rule applies** — The Roth SEP/SIMPLE balance is subject to the same 5-year rule as other Roth accounts (see §17.4).
- **Plan document amendments required** — Plan-document amendments were required; many SEP/SIMPLE documents were updated through 2023-2024.

### 15.2 Self-employed application

A sole proprietor with a SEP-IRA may now designate the SEP contribution as Roth. The trade-off: Traditional SEP: 25% of (net SE × 0.9235) contribution is deductible on Schedule 1 Line 16, reducing AGI. Roth SEP: No current deduction; contribution included in gross income; tax-free growth and tax-free qualified distribution after 5 years and age 59½. For a high-bracket sole proprietor expecting lower future brackets, traditional remains more attractive. For a low-bracket young sole proprietor expecting higher future brackets, Roth SEP is the better long-term move.

### 15.3 Form 1099-R reporting

- **Roth SEP/SIMPLE 1099-R reporting** — Roth SEP and Roth SIMPLE contributions are reported on Form 1099-R in the year of contribution with the appropriate Roth code. The IRA custodian must be aware of the Roth designation; some custodians did not support Roth SEP/SIMPLE until late 2024.

## 16. Inherited IRA 10-Year Rule and the July 2024 Final Regs

This is the highest-stakes area for 2025 returns.

### 16.1 The basic 10-year rule (SECURE 1.0)

- **10-year rule basics** — For participants who died after December 31, 2019, a designated beneficiary who is NOT an Eligible Designated Beneficiary must withdraw the entire inherited account by December 31 of the year containing the 10th anniversary of the participant's death.

### 16.2 Eligible Designated Beneficiaries (EDBs)

- **EDB categories** — 1. Surviving spouse — full stretch, plus the spousal rollover election (treating the inherited IRA as the surviving spouse's own). 2. Minor child of the decedent — stretch until the child reaches the age of majority (21 under final regs, applied uniformly), then the 10-year rule begins. 3. Disabled beneficiary under §72(m)(7) — full stretch. 4. Chronically ill beneficiary under §7702B(c)(2) — full stretch. 5. Beneficiary not more than 10 years younger than the decedent — full stretch. Adult non-disabled non-chronically-ill children, grandchildren, siblings, friends, etc., are non-EDB designated beneficiaries subject to the 10-year rule.  _(§72(m)(7); §7702B(c)(2))_

### 16.3 Non-designated beneficiaries (estates, non-look-through trusts, charities)

- **5-year or ghost life expectancy rule** — Subject to the 5-year rule (full distribution by end of 5th year) if the participant died before the required beginning date, or to the decedent's remaining life expectancy ("ghost life expectancy") if the participant died on or after the required beginning date.

### 16.4 The annual-RMD-during-the-10-years controversy

The text of §401(a)(9)(H) as amended by SECURE 1.0 was ambiguous about whether a non-EDB must take annual RMDs during years 1-9 of the 10-year period (in addition to the final distribution by year 10), or simply must complete distribution by year 10 with no intermediate requirement.

The proposed regulations issued February 2022 controversially took the position that:

- If the participant died AFTER the required beginning date (RBD), the non-EDB beneficiary MUST take annual RMDs in years 1-9 PLUS the full balance by year 10.
- If the participant died BEFORE the RBD, no annual RMDs are required; only the year-10 cleanout.

This shocked the planning community because many practitioners had assumed (and advised clients) that the 10-year rule was a single cleanout obligation.

### 16.5 IRS notices waiving 2021-2024 RMDs

- **Notice 2022-53 waiver** — Waived 2021 and 2022 annual RMDs for affected beneficiaries.  _(Notice 2022-53)_
- **Notice 2023-54 waiver** — Waived 2023.  _(Notice 2023-54)_
- **Notice 2024-35 waiver** — Waived 2024.  _(Notice 2024-35)_
- **No 2025 waiver** — (No waiver for 2025.)

### 16.6 Final regulations — TD 10001 (July 19, 2024)

- **Final regs confirm proposed reg position** — Non-EDB beneficiaries of a participant who died after the RBD MUST take annual RMDs in years 1-9 of the 10-year period, computed using the beneficiary's single-life expectancy.  _(TD 10001, July 19, 2024)_
- **Annual RMDs begin 2025** — Annual RMDs begin in tax year 2025 (the first year not covered by a waiver notice).  _(TD 10001)_
- **§4974 excise tax for missed RMD** — 25%, reduced to 10% if cured percent  _(§4974)_

### 16.7 2025 mechanics

For a beneficiary of a participant who died in 2020 having already begun RMDs:

- Year 2021-2024: annual RMDs waived per Notices 2022-53, 2023-54, 2024-35.
- Year 2025: annual RMD REQUIRED. Compute using the beneficiary's single-life expectancy from the year following the decedent's death, reduced by 1 each year ("subtraction method").
- Year 2026-2029: annual RMDs.
- Year 2030 (10th anniversary year): full cleanout of remaining balance.

AUDIT FLASH POINT — missed 2025 inherited IRA RMDs. Many CPAs and beneficiaries are unaware that the waiver ends in 2025. Every inherited-IRA client (death year 2020 or later, decedent past RBD) needs a 2025 RMD computation. The §4974 excise tax is 25% of the shortfall (reduced to 10% with timely correction). File Form 5329 to report any shortfall and request the waiver under §4974(d) if reasonable cause exists.

### 16.8 Decision flowchart — inherited IRA 2025 RMD

Decedent died ON or AFTER Jan 1, 2020?
  NO → pre-SECURE rules; life-expectancy stretch may still apply
  YES → continue:

Is beneficiary an EDB (spouse, minor child, disabled, chronically ill, ≤10 yrs younger)?
  YES → life-expectancy stretch (or spousal rollover); no 10-year rule
  NO → continue to 10-year rule analysis:

Did decedent die BEFORE their required beginning date?
  YES → 10-year rule applies; NO annual RMDs required in years 1-9; cleanout by year 10
  NO (died AFTER RBD) → 10-year rule applies; annual RMDs REQUIRED in years 1-9 starting 2025; cleanout by year 10

### 16.9 Surviving spouse beneficiary — special election (§327)

- **Spousal election to be treated as deceased participant** — SECURE 2.0 §327 (TY 2024+): surviving spouse may elect to be treated as the deceased participant for RMD purposes. This permits: Using the Uniform Lifetime Table (slower distribution) rather than the spouse's own Single-Life Table. Deferring RMD start until the deceased participant would have reached their RBD (rather than the surviving spouse's own RBD). This election is irrevocable. It is most beneficial when the surviving spouse is older than the deceased participant — distributions can be deferred until the (younger) deceased spouse would have reached RBD.  _(§327)_

## 17. Backdoor Roth and Mega Backdoor Roth — Unchanged by SECURE 2.0

SECURE 2.0 did not modify the backdoor or mega-backdoor Roth strategies. The 2021 House-passed Build Back Better Act contained a provision that would have eliminated the backdoor Roth and capped contributions for high-balance IRAs, but the final BBBA legislation died in the Senate and SECURE 2.0 did not include those provisions. Backdoor and mega-backdoor Roth remain available in 2025.

### 17.1 Backdoor Roth — basic mechanics

- **Roth IRA MAGI phaseout 2025** — $165k single / $246k MFJ for 2025 USD  _(§408A(c)(3))_
- **Backdoor Roth steps** — 1. Contribute up to $7,000 ($8,000 age 50+) to a traditional IRA. Because the taxpayer is over the deduction phaseout (with an active workplace plan), the contribution is nondeductible and creates basis under §72. 2. Convert the nondeductible traditional IRA balance to a Roth IRA. The conversion is taxable only on the portion attributable to pre-tax dollars and earnings. 3. File Form 8606 to track the basis and report the conversion.  _(§408A(c)(3); §72)_

### 17.2 The §408(d)(2) pro-rata trap

- **Pro-rata basis allocation rule** — §408(d)(2) requires that, on any traditional-IRA distribution or conversion, the basis (nondeductible contributions) be allocated proportionally across the aggregate balance of ALL the taxpayer's traditional IRAs (including SEP-IRAs and SIMPLE-IRAs) as of December 31 of the conversion year.  _(§408(d)(2))_

Example. Taxpayer has: $200,000 in a pre-tax rollover IRA (entirely pre-tax basis). Newly contributed $7,000 nondeductible to a traditional IRA. Total aggregate balance: $207,000. Basis: $7,000. Nondeductible ratio: 7,000 / 207,000 = 3.38%. If the taxpayer converts the $7,000 to Roth, only 3.38% of $7,000 = $237 is treated as a return of basis. The remaining $6,763 is taxable income. The other $200,000 retains $6,763 of basis going forward, deferring the rest of the basis recovery. Practical consequence: backdoor Roth is highly tax-inefficient for taxpayers with pre-existing pre-tax traditional IRA, SEP-IRA, or SIMPLE-IRA balances.

- **Workarounds to pro-rata trap** — 1. Reverse rollover of the pre-tax IRA balance into the taxpayer's employer 401(k) before year-end (if the 401(k) plan accepts rollovers). The 401(k) is not aggregated under §408(d)(2). After the reverse rollover, the only traditional IRA balance left is the nondeductible contribution, and the backdoor conversion is fully tax-free. 2. Use a Solo 401(k) rather than a SEP-IRA for self-employed contributions, since Solo 401(k) balances are not aggregated under §408(d)(2). 3. Convert the entire pre-tax IRA to Roth in a single high-cost year, eating the tax bill once, then enjoy clean backdoor Roth thereafter.  _(§408(d)(2))_

Preparers frequently report a backdoor Roth conversion as if entirely nontaxable, ignoring an aggregate SEP-IRA balance. Form 8606 Line 6 explicitly asks for the aggregate 12/31 balance of all traditional, SEP, and SIMPLE IRAs. The IRS cross-checks Form 5498 (issued by every IRA custodian) against Form 8606 Line 6. Mismatches generate CP-2000 notices. The reviewer should verify Line 6 against ALL Forms 5498 received by the taxpayer.

### 17.3 Mega Backdoor Roth — mechanics

- **Mega backdoor Roth steps** — 1. Contribute the regular $23,500 employee deferral (pre-tax or Roth). 2. The employer's matching/profit-sharing contributions fill some of the remaining §415(c) cap. 3. Additional after-tax (non-Roth) contributions fill the remaining §415(c) cap up to $70,000 total (2025; $77,500 with age-50 catch-up; $81,250 with super catch-up). 4. Convert the after-tax contributions to Roth via either in-plan Roth conversion or in-service withdrawal to a Roth IRA, before significant earnings accrue.  _(§415(c))_
- **Maximum mega-backdoor Roth amount 2025, age 50, no match** — $77,500 − $31,000 (deferral + catch-up) = $46,500 mega-backdoor capacity USD  _(§415(c))_

Solo 401(k) mega-backdoor application: a Solo 401(k) prototype document with after-tax contribution + in-plan Roth conversion features (these are not standard in most prototypes — confirm with provider) can support the mega-backdoor Roth. Most Solo 401(k) documents from major brokerages do NOT support after-tax contributions; specialized providers (e.g., MySolo401k, Carry) offer Solo 401(k) prototypes that do.

### 17.4 The two Roth 5-year clocks

- **Clock 1 — Roth contribution 5-year clock** — Starts January 1 of the first year the taxpayer made ANY Roth IRA contribution (including a conversion). Applies to determining whether Roth IRA earnings can be distributed tax-free. Once satisfied, applies to ALL Roth IRAs forever. There is only one Clock 1 per taxpayer.  _(§408A(d)(2)(B))_
- **Clock 2 — Roth conversion 5-year clock** — Each conversion has its own 5-year clock starting January 1 of the conversion year. Applies to whether the converted principal can be distributed without the 10% §72(t) penalty (if under age 59½). Once age 59½ is reached, Clock 2 becomes irrelevant.  _(§408A(d)(3)(F))_

Example. Taxpayer makes first Roth IRA contribution in 2020 and converts $50,000 from traditional IRA in 2024. Taxpayer is age 55. Clock 1 (contributions, governing tax-free earnings) is satisfied in 2025 (5 years from 2020). Earnings can be distributed tax-free after age 59½. Clock 2 (2024 conversion, governing 10% penalty avoidance) is satisfied in 2029. If the taxpayer withdraws the $50,000 converted principal before 2029 and before age 59½, the 10% penalty applies (even though the conversion itself was already taxed).

### 17.5 Roth ordering rules for distributions

- **Roth distribution ordering** — Roth IRA distributions are deemed to come out in this order: 1. Regular Roth contributions (always tax-free and penalty-free). 2. Roth conversions, oldest first (each subject to its own Clock 2). 3. Earnings (tax-free only if Clock 1 satisfied AND age 59½ / death / disability / first-time homebuyer). This means a backdoor Roth contributor can always withdraw the contribution principal tax-free and penalty-free. The conversion 5-year clock only matters if they want to also touch the converted principal early.

## 18. Tax Planning Interactions

### 18.1 Roth conversion and the §6654 safe harbor

- **§6654(d)(1)(B) safe harbor for high AGI** — A large Roth conversion can spike taxable income and create a large unexpected tax liability. §6654(d)(1)(B) safe harbor: a taxpayer with prior-year AGI > $150,000 must pay 110% of prior-year total tax through withholding and estimates to avoid underpayment penalty. A Roth conversion in mid-year that doubles AGI may put the safe harbor out of reach unless prior-year tax × 110% has already been covered through W-2 withholding or estimates.  _(§6654(d)(1)(B))_

Planning tactic: time the Roth conversion late in Q4 so that the conversion year's tax can be paid via Q4 estimate by January 15 without triggering Q1-Q3 underpayment. Use Form 2210 Annualized Income Installment method to avoid penalty for early quarters.

### 18.2 Roth conversion and the 3.8% NIIT

- **NIIT interaction with Roth conversion** — A Roth conversion is NOT itself subject to NIIT under §1411 (retirement distributions are excluded from net investment income). But the conversion does increase MAGI, which can push the taxpayer over the MAGI threshold ($200k single / $250k MFJ) and subject other investment income (interest, dividends, capital gains, rental income) to the 3.8% NIIT for that year. Model this before executing a large conversion.  _(§1411)_

### 18.3 Roth conversion and IRMAA (Medicare premium surcharges)

- **IRMAA lookback and surcharge** — A Roth conversion at age 63 (or later) raises MAGI for the two-year-lookback IRMAA determination. A 2025 conversion pushes 2027 Medicare Part B and Part D premiums into higher tiers. The 2025 IRMAA thresholds are based on 2023 income; conversions in 2025 affect 2027 premiums. The marginal IRMAA surcharge can be substantial — IRMAA Tier 4 adds approximately $419/month per spouse for Part B in 2025 — making this a meaningful indirect cost of conversion.

### 18.4 Roth conversion and ACA premium tax credit

- **ACA PTC interaction** — If the taxpayer obtains health insurance through the ACA marketplace and receives the premium tax credit (PTC) under §36B, a Roth conversion increases MAGI for PTC purposes and can trigger excess advance PTC repayment under §36B(f)(2) on Form 8962. The PTC phaseout previously had a hard cliff at 400% FPL; under the Inflation Reduction Act of 2022 as extended, the cliff is replaced with a continuous 8.5% of income test through tax year 2025. For 2026+, the cliff is scheduled to return absent further legislation.  _(§36B; §36B(f)(2))_

### 18.5 Roth conversion and the §86 Social Security taxability formula

- **Social Security taxability effect** — A retiree taking Social Security benefits may find that a Roth conversion increases provisional income, pushing more of the Social Security benefits into taxable territory (up to 85% taxable). The marginal effect can be a 22% federal × 1.85 = ~40% effective marginal rate on the conversion. For low-bracket retirees, this is often the binding tax cost of conversion.  _(§86)_

### 18.6 Roth conversion and §199A QBI deduction

- **QBI threshold interaction** — A Roth conversion does NOT count as QBI (it's not from a qualified trade or business). However, it does increase taxable income, which affects: The §199A taxable-income threshold ($197,300 single / $394,600 MFJ for 2025) above which the W-2 wage and UBIA limitations begin to bite for SSTBs. The overall taxable-income cap on the §199A deduction (which equals 20% of taxable income reduced by net capital gain). For a sole proprietor near the SSTB threshold, a Roth conversion can reduce the QBI deduction. Model this.  _(§199A)_

## 19. Worked Examples

### 19.1 Example 1 — Born 1952, first RMD in 2025

Facts. Hiroshi turned 73 on March 4, 2025 (born 1952). His prior-year-end (12/31/2024) traditional IRA balance was $480,000. His Roth IRA balance was $150,000 (no RMD required during his lifetime). He has no inherited accounts. He has no employer 401(k).

Analysis.

- 2025 RMD year: First year. RBD is April 1, 2026.
- Computation: $480,000 ÷ 26.5 (age 73 Uniform Lifetime divisor) = $18,113.
- Election: Hiroshi may defer to April 1, 2026 OR take by December 31, 2025.
- Stacking consequence of deferral: if Hiroshi defers, he takes $18,113 by April 1, 2026 (covering 2025) AND $18,491 (= 2025 year-end balance / 25.5) by December 31, 2026 (covering 2026). Two RMDs in 2026 calendar year. Often the worse outcome if 2026 marginal rates are similar.
- Recommendation: Take the 2025 RMD by December 31, 2025 to avoid bracket creep in 2026.
- QCD planning: Hiroshi turned 70½ in 2022, so he is QCD-eligible. He may direct up to $108,000 of the IRA distribution to charity, satisfying his RMD and excluding the QCD amount from AGI. If he is charitably inclined, this is highly tax-efficient.
- Form 5498: confirm Vanguard reports the correct 12/31/2024 balance to validate the RMD computation.
- Form 1099-R: Code 7 (normal distribution).

### 19.2 Example 2 — Super catch-up at age 62

Facts. Priya is a sole proprietor (LLC disregarded), age 62 throughout 2025 (born 1962, but for this example assume she turns 62 in 2025). Net SE earnings (after Schedule C, before §1402(a)(12) and SE-tax half-deduction) = $250,000. She maintains a Solo 401(k) established in 2020. The plan document supports the super catch-up. She is unmarried, no employees other than herself.

Compute SE base for §415(c):

- Net SE earnings: $250,000
- §1402(a)(12) reduction (× 0.9235): $230,875
- SE tax: $176,100 × 12.4% + $230,875 × 2.9% = $21,836 + $6,695 = $28,531
- Deductible half of SE tax: $14,266 (rounded for clarity)
- Net SE for retirement (compensation): $250,000 − $14,266 = $235,734

Solo 401(k) employee deferral (Roth or pre-tax):

- Regular: $23,500
- Age-60-63 super catch-up: $11,250
- Total deferral: $34,750

Solo 401(k) employer profit-sharing:

- 25% of $235,734 (or equivalently 20% of net SE before deduction, with the §1402(a)(12) adjustment) = up to $46,847 capped by §415(c).

§415(c) cap including super catch-up: $70,000 + $11,250 = $81,250.

- Deferral + employer = $34,750 + $46,847 = $81,597 — exceeds cap by $347.
- Reduce employer profit-sharing to $46,500 to fit within $81,250.

Total Solo 401(k) contribution: $81,250. The catch-up portion ($11,250) is the super catch-up under §414(v)(2)(E).

Schedule 1 Line 16 deduction: $46,500 (the pre-tax employer portion) + portion of the $23,500 deferral elected as pre-tax. Roth portion is not deducted.

Filing deadline: Employee deferral elected by 12/31/2025. Employer contribution funded by extended return due date (October 15, 2026).

Note re §603 Roth catch-up mandate: Priya is a sole proprietor with NO FICA W-2 wages > $145,000. Even when §603 takes effect in 2026, her Solo 401(k) catch-up is NOT Roth-mandatory under current guidance because §603 measures wages by FICA wages, not by self-employment earnings. (Confirm in 2026 if IRS guidance changes.)

### 19.3 Example 3 — Inherited IRA 2025 annual RMD (final regs)

Facts. Devon's father (born 1948, RBD April 1, 2020 under SECURE 1.0 age 72) passed away on June 14, 2021 at age 73, having already taken his 2020 and 2021 RMDs from his $600,000 traditional IRA. Devon is the sole designated beneficiary. Devon is age 45 in 2025 — non-EDB.

Pre-2024 analysis.

- Death in 2021 means the 10-year cleanout deadline is December 31, 2031.
- IRS Notices 2022-53, 2023-54, 2024-35 waived annual RMDs for 2022-2024. Devon took no distributions 2022-2024.

2025 analysis (post-final-regs).

- Per final regs TD 10001, annual RMD is required in 2025. Devon's father died AFTER his RBD, so annual RMDs apply during years 1-9.
- Single-life expectancy factor: Devon was age 41 in 2022 (year after death). Per Single Life Table, age-41 factor is 44.3 (factor in year 1 — 2022).
- Subtraction method: 2022 = 44.3, 2023 = 43.3, 2024 = 42.3, 2025 = 41.3, 2026 = 40.3, …
- 12/31/2024 account balance: $700,000.
- 2025 RMD = $700,000 ÷ 41.3 = $16,949.
- Take by December 31, 2025.
- Repeat each year 2026-2030 with successively smaller divisors.
- Year 2031: cleanout of remaining balance.

Failure to take 2025 RMD: §4974 excise tax = 25% × $16,949 = $4,237. If Devon catches the omission and distributes by early 2026, the rate drops to 10% = $1,695. Form 5329 must be filed and "RC" annotated if reasonable-cause waiver is sought.

Recommendation: Set up an automatic annual distribution at the custodian to prevent recurrence.

### 19.4 Example 4 — Backdoor Roth with §408(d)(2) basis trap

Facts. Karen is a self-employed consultant, age 45, MAGI $300,000 in 2025. She has: Pre-existing SEP-IRA: $180,000 (entirely pre-tax). No other traditional, SEP, or SIMPLE IRA balances. Roth IRA balance: $40,000 (built up before MAGI rose).

She wants to execute a backdoor Roth for 2025. Direct Roth contribution is foreclosed by her MAGI being above the $165k single phaseout.

Naïve approach (will hurt her).

- Contribute $7,000 nondeductible to a new traditional IRA.
- Convert $7,000 to Roth IRA.
- 12/31/2025 aggregate traditional+SEP balance: $180,000 + 0 (the $7,000 was converted) = $180,000. Basis remaining: $7,000 × ($180,000 / $187,000) carry-forward = $6,738 of basis is locked into the SEP-IRA. Only $262 of the $7,000 conversion is treated as basis recovery. $6,738 of the $7,000 conversion is taxable.

Better approach (Solo 401(k) reverse rollover).

- Karen establishes a Solo 401(k) by 12/31/2025.
- Rolls her $180,000 SEP-IRA into the Solo 401(k). (SEPs can be rolled into 401(k)s — confirm Solo 401(k) plan document accepts rollovers from SEPs.)
- 12/31/2025 aggregate traditional+SEP+SIMPLE IRA balance: $0 (SEP rolled into Solo 401(k), which is not aggregated under §408(d)(2)).
- Contribute $7,000 nondeductible to traditional IRA.
- Convert $7,000 to Roth IRA.
- Form 8606 Line 6 = $0 (no traditional/SEP/SIMPLE balance on 12/31/2025).
- Conversion is entirely tax-free (full basis recovery).

Form 8606 reporting: file Form 8606 for the nondeductible contribution AND the conversion. Line 1 = $7,000 (nondeductible contribution). Line 6 = $0 (12/31 balance). Line 8 = $7,000 (conversion amount). Line 13 = $7,000 (basis recovered). Taxable conversion = $0.

AUDIT FLASH POINT — Form 8606 Line 6 verification. Many preparers leave Line 6 blank or report only the destination Roth IRA's traditional sub-account. The IRS receives a Form 5498 from every IRA custodian reporting the 12/31 fair market value of every traditional, SEP, and SIMPLE IRA. Mismatches against Form 8606 Line 6 trigger CP-2000 notices. Confirm 5498s from ALL custodians.

## 20. Reviewer Checklist (Sole Proprietor / Single-Member LLC)

A reviewer should verify the following for any 2025 federal return where retirement contributions or distributions are reported:

### 20.1 If client is age 73-74 in 2025

- [ ] Identify year of birth and apply correct RMD age (73 for born 1951-1959; 75 for born 1960+).
- [ ] If turning 73 in 2025 (born 1952), confirm whether first RMD will be taken in 2025 or deferred to April 1, 2026.
- [ ] Compute RMD using Uniform Lifetime Table (or Joint and Last Survivor if sole spouse beneficiary is >10 years younger).
- [ ] Verify 12/31/2024 balance against Form 5498.
- [ ] Confirm RMD was actually distributed; obtain Form 1099-R.
- [ ] Consider QCD opportunity (up to $108,000 in 2025) for charitably inclined clients age 70½+.

### 20.2 If client age 60-63 in 2025

- [ ] Confirm Solo 401(k) plan document supports the super catch-up.
- [ ] Maximize employee deferral including the $11,250 super catch-up if cash flow permits.
- [ ] Verify the contribution fits within §415(c) including the catch-up ($81,250 max).
- [ ] Flag the 2026 Roth catch-up mandate if client has FICA wages > $145k (employee, not self-employed).

### 20.3 If client has inherited IRA (death year 2020+)

- [ ] Identify whether decedent died before or after RBD.
- [ ] Identify whether beneficiary is EDB or non-EDB.
- [ ] If non-EDB and decedent died after RBD: COMPUTE 2025 ANNUAL RMD (this is the audit flash point).
- [ ] Use Single-Life Table with subtraction method from year following death.
- [ ] Verify distribution was actually taken by 12/31/2025.
- [ ] If RMD missed, prepare Form 5329 with reasonable-cause waiver request.
- [ ] Identify the year-10 cleanout deadline and plan progressive distributions to avoid year-10 bracket spike.

### 20.4 If client executed a Roth conversion in 2025

- [ ] Confirm Form 1099-R Code 2 (under 59½) or Code 7 (over 59½).
- [ ] Compute §408(d)(2) pro-rata if traditional/SEP/SIMPLE IRA balances exist on 12/31/2025.
- [ ] Verify Form 8606 Line 6 against ALL Forms 5498.
- [ ] Cross-check conversion impact on §6654 safe harbor, NIIT, IRMAA, ACA PTC, §86 Social Security.
- [ ] Document the 5-year conversion clock for future early-withdrawal planning.

### 20.5 If client made backdoor Roth in 2025

- [ ] Confirm nondeductible traditional IRA contribution and same-year (or short-window) conversion.
- [ ] File Form 8606 for the nondeductible contribution.
- [ ] File Form 8606 for the conversion (can be the same form if same year).
- [ ] Verify NO existing traditional/SEP/SIMPLE IRA balances would trigger pro-rata. If they do, advise reverse rollover to Solo 401(k) or full conversion.

### 20.6 If client took an emergency distribution in 2025

- [ ] $1,000 emergency distribution under §72(t)(2)(I): confirm self-certification documentation in client file.
- [ ] Verify no other emergency distribution taken in 2024 that has not yet been repaid.
- [ ] $10,000 domestic abuse distribution under §72(t)(2)(K): self-certification; confirm 3-year repayment window tracking.
- [ ] Birth/adoption distribution under §72(t)(2)(H): confirm timing within 1 year of qualifying event; 3-year repayment window.

### 20.7 If client received a 529-to-Roth rollover for 2025

- [ ] Verify 529 plan ≥ 15 years old.
- [ ] Verify beneficiary's earned income ≥ rollover amount.
- [ ] Confirm no contributions in the prior 5 years are being rolled.
- [ ] Track lifetime $35,000 cap (cumulative across years).
- [ ] Annual rollover capped at IRA contribution limit ($7,000 or $8,000 if age 50+) less any other IRA contributions.

## 21. Open Issues and Pending Guidance

As of November 2025, the following SECURE 2.0 provisions remain partially or fully unaddressed by IRS guidance:

1. §603 Roth catch-up final regs: proposed regs January 10, 2025 (REG-100669-24). Final regs expected during 2026. Plan sponsors operating in 2026 must navigate proposed-reg rules.
2. §325 lifetime Roth 401(k) RMD elimination: clarification needed on coordination with rollovers from Roth 401(k) to Roth IRA.
3. §334 LTC distribution: regs not yet issued. Effective 2026.
4. §603 application to self-employed: open question whether self-employment net earnings will ultimately be deemed analogous to FICA wages for §603 purposes. Conservative position: NO (sole proprietors retain pre-tax catch-up capability).
5. §126 529-to-Roth and beneficiary-change clock reset: unclear whether changing the 529 beneficiary resets the 15-year clock. IRS has not addressed.
6. §109 super catch-up for SIMPLE plans: confirmed in IRS Notice 2024-2 but practical implementation by SIMPLE-IRA providers was inconsistent through 2024.

Reviewers should monitor the IRS Priority Guidance Plan and updates to Notice 2024-2 for additional guidance.

## 22. Citation Index

**Citation Index**  _(P.L. 116-94 Div. O (SECURE 1.0); P.L. 117-328 Div. T (SECURE 2.0); §72(t) et seq.; §103; §107; §109; §126; §127; §307; §317; §325; §327; §401(a)(9); §401(a)(9)(H); §408(d)(2); §408A; §408A(c)(3); §408A(d)(2); §408A(d)(3); §414A; §414(v)(2)(E); §415(c); §601; §603; §604; §4974; §6654; Notice 2022-53; Notice 2023-54; Notice 2023-62; Notice 2024-2; Notice 2024-35; TD 10001; REG-103529-23; REG-100669-24; Rev. Proc. 2024-40; Form 1099-R; Form 5329; Form 5498; Form 8606; Form 8962)_

| Authority | Subject |
| --- | --- |
| P.L. 116-94 Div. O (SECURE 1.0) | Original retirement provisions, 10-year rule |
| P.L. 117-328 Div. T (SECURE 2.0) | Comprehensive retirement changes |
| §72(t) | Early-withdrawal 10% penalty exceptions |
| §72(t)(2)(H) | Birth/adoption distribution |
| §72(t)(2)(I) | $1,000 emergency distribution (SECURE 2.0 §115) |
| §72(t)(2)(K) | $10,000 domestic abuse distribution (SECURE 2.0 §314) |
| §72(t)(2)(L) | Terminally ill distribution (SECURE 2.0 §326) |
| §72(t)(2)(M) | Disaster recovery distribution (SECURE 2.0 §331) |
| §72(t)(2)(N) | LTC premium distribution (SECURE 2.0 §334, eff. 2026) |
| §103 | Saver's Match (SECURE 2.0, eff. 2027) |
| §107 | RMD age 73/75 (SECURE 2.0) |
| §109 | Super catch-up 60-63 (SECURE 2.0) |
| §126 | 529-to-Roth rollover (SECURE 2.0, eff. 2024) |
| §127 | PLESA (SECURE 2.0) |
| §307 | QCD indexing and CRT (SECURE 2.0) |
| §317 | Solo 401(k) sole prop establishment (SECURE 2.0) |
| §325 | Roth 401(k) lifetime no RMD (SECURE 2.0) |
| §327 | Surviving spouse RMD election (SECURE 2.0) |
| §401(a)(9) | RMD rules |
| §401(a)(9)(H) | 10-year rule |
| §408(d)(2) | Traditional IRA pro-rata basis |
| §408A | Roth IRA |
| §408A(c)(3) | Roth IRA income phaseout |
| §408A(d)(2) | Roth 5-year contribution clock |
| §408A(d)(3) | Roth 5-year conversion clock |
| §414A | Auto-enrollment mandate (SECURE 2.0 §101) |
| §414(v)(2)(E) | Super catch-up 60-63 |
| §415(c) | DC plan total contribution limit |
| §601 | Roth SEP / Roth SIMPLE (SECURE 2.0) |
| §603 | Roth catch-up mandate (SECURE 2.0; delayed to 2026) |
| §604 | Roth employer contributions (SECURE 2.0) |
| §4974 | RMD excise tax (25%/10%) |
| §6654 | Estimated tax safe harbor |
| Notice 2022-53 | RMD waiver 2021-2022 |
| Notice 2023-54 | RMD waiver 2023 |
| Notice 2023-62 | Roth catch-up administrative transition |
| Notice 2024-2 | SECURE 2.0 grab bag |
| Notice 2024-35 | RMD waiver 2024 |
| TD 10001 (July 2024) | Final RMD regulations |
| REG-103529-23 | Proposed regs on SECURE 2.0 RMD |
| REG-100669-24 (Jan 2025) | Proposed regs on §603 Roth catch-up |
| Rev. Proc. 2024-40 | 2025 inflation adjustments |
| Form 1099-R | Retirement distribution reporting |
| Form 5329 | Additional taxes on retirement plans; §4974 waiver |
| Form 5498 | IRA custodian annual reporting |
| Form 8606 | Nondeductible IRA basis and conversions |
| Form 8962 | Premium Tax Credit reconciliation |

## 23. Refusal Catalogue

- **Defined-benefit plan funding** — Defined-benefit plan funding — engage actuary.  _(unsure)_
- **Cash-balance plan design** — Cash-balance plan design — engage actuary.  _(unsure)_
- **ESOP transactions** — ESOP transactions — engage ESOP specialist.  _(unsure)_
- **Multi-employer plan withdrawal liability** — Multi-employer plan withdrawal liability — engage ERISA counsel.  _(unsure)_
- **Excise tax on prohibited transactions §4975** — Excise tax on prohibited transactions §4975 — engage ERISA counsel.  _(§4975)_
- **State-mandated auto-IRA programs** — State-mandated auto-IRA programs (CalSavers, IL Secure Choice, etc.) — outside federal scope; load state skill.  _(unsure)_
- **Foreign retirement plan reporting** — Foreign retirement plan reporting (Form 8938, Form 3520, FBAR for foreign pensions) — load foreign-account skills.  _(unsure)_

This skill does NOT produce final advice on:

- **Defined-benefit plan funding** — engage actuary.
- **Cash-balance plan design** — engage actuary.
- **ESOP transactions** — engage ESOP specialist.
- **Multi-employer plan withdrawal liability** — engage ERISA counsel.
- **Excise tax on prohibited transactions §4975** — engage ERISA counsel.
- **State-mandated auto-IRA programs** (CalSavers, IL Secure Choice, etc.) — outside federal scope; load state skill.
- **Foreign retirement plan reporting** (Form 8938, Form 3520, FBAR for foreign pensions) — load foreign-account skills.

For any of the above, the reviewer should refuse to issue a federal opinion within this skill and refer to the appropriate specialist or load the proper companion skill.

## End of skill us-secure-2-and-retirement-updates v0.1.

*End of skill us-secure-2-and-retirement-updates v0.1.*

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
