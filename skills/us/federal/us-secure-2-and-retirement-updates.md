---
name: us-secure-2-and-retirement-updates
description: US federal SECURE 2.0 retirement rules for 2026, with separately dated 2025 limits and historical cases. Covers catch-ups, Roth catch-up transition conditions, RMDs, inherited IRAs, QCDs, 529-to-Roth transfers, Saver's Credit and Match, solo 401(k) deadlines and automatic enrollment. Special distributions and complex plan cases have explicit holds.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# US SECURE 2.0 and retirement rules (tax year 2026)

## Scope and who this is for

US federal retirement contributions and distributions for **2026**: 401(k), 403(b), governmental 457(b), SIMPLE plans, IRAs, inherited IRAs, QCDs, 529 transfers, Saver's Credit/Match and solo-plan deadlines. Use the separately dated 2025 section for 2025 returns and corrections. Special plan/distribution routes are held below; confirm any disaster deadline relief separately.

## Ask the client first

- **Year of birth**, and whether the person is still working for the employer that sponsors the plan. Are they a 5-percent owner of that employer?
- **Which accounts**: traditional or Roth IRA, SEP IRA, SIMPLE IRA, 401(k), 403(b), governmental 457(b), inherited IRA or plan account, 529 plan.
- For catch-ups: **age at 31 December 2026**, and their **2025 wages from the employer that sponsors the plan, W-2 boxes 3 and 5, and the plan's 2026 good-faith implementation**. Is the income W-2 wages, or self-employment income only?
- Does the plan **offer designated Roth contributions**, and does it offer the higher age 60–63 catch-up?
- For an inherited account: the **owner's date of death**, the owner's date of birth (to fix the owner's required beginning date), and the beneficiary's relationship, age, disability or chronic illness.
- For a QCD: **age on the date of the distribution**, whether the money goes directly from the IRA trustee to the charity, and any **deductible IRA contributions made for years when the owner was 70½ or over**.
- For a 529 rollover: when the 529 account was opened for this beneficiary, contributions in the last 5 years, the beneficiary's compensation for the year, and any other IRA contributions for the same year.
- Any RMD shortfall in an earlier year, and whether a Form 5329 has already been filed for it.

## The method, step by step

1. Fix the tax year and account type; use the corresponding limits and actual plan terms.
2. Check contribution eligibility, compensation, other deferrals, catch-up age and the plan's wage measure.
3. For distributions, establish owner/beneficiary status, required beginning date, correct table and prior-year-end balance; check any QCD separately.
4. Compute shortfalls and deadlines, then follow the filing steps below. Stop on an explicit non-usable hold.

### Rates, bands and thresholds

Source: IRS Notice 2025-67 and news release IR-2025-111 (13 November 2025).

| Item (2026) | Amount | Source |
| --- | --- | --- |
| Elective deferral limit, 401(k) / 403(b) / governmental 457(b) / TSP | $24,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, age 50 or over | $8,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, age 60, 61, 62 or 63 in 2026 | $11,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Defined contribution annual additions limit, §415(c) | $72,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Compensation limit, §401(a)(17) | $360,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth catch-up wage threshold (2025 wages, used for 2026) | $150,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE plan deferral limit | $17,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE enhanced deferral ceiling; eligibility/plan election held, not a default entitlement | $18,100 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up, age 50 or over | $4,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE special catch-up ceiling; eligibility/plan terms held | $3,850 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up, age 60 to 63 | $5,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA contribution limit (traditional and Roth combined) | $7,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA catch-up, age 50 or over | $1,100 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| QCD annual limit per person | $111,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| One-time split-interest QCD indexed ceiling; conditions held | $55,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Domestic-abuse indexed dollar ceiling; eligibility/other limits held | $10,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| PLESA indexed cap; operation/eligibility held | $2,600 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |

Totals that follow from these: a participant aged 50 or over can defer up to **$32,500**. A participant aged 60 to 63 can defer up to **$35,750**. Catch-ups sit on top of the §415(c) limit, so the annual additions ceiling becomes **$80,000** with the age-50 catch-up, or **$83,250** with the age 60–63 catch-up.

**Roth IRA income phase-out (2026, modified AGI; qualifying surviving spouse uses the joint range, separately filing spouses apart all year use the single range):**

- single or head of household: $153,000 to $168,000;
- married filing jointly: $242,000 to $252,000;
- married filing separately and lived with the spouse at any time in the year: phase-out from zero to $10,000.

**Saver's Credit AGI tiers (2026).** For an eligible person aged 18 or over, not a dependent or full-time student, the nonrefundable credit rate is 50%, 20% or 10% of up to $2,000 of eligible contributions, and zero above the top limit. Reduce eligible contributions for testing-period distributions under §25B(d)(2), including the joint-return spouse rule; use Form 8880. The tiers are:

- married filing jointly: 50% up to $48,500, 20% up to $52,500, 10% up to $80,500;
- head of household: $36,375, $39,375 and $60,375;
- everyone else: $24,250, $26,250 and $40,250.

### Catch-ups, including ages 60 to 63 ([IRC §414(v)](https://uscode.house.gov/us/usc/t26/s414/))

- The age-50 catch-up applies to a participant who reaches age 50 by year end and cannot make further ordinary deferrals because of an applicable limit. Catch-ups cannot exceed remaining eligible compensation; these are ceilings, not automatic entitlements.
- The higher catch-up replaces the regular catch-up for a participant who **attains age 60, 61, 62 or 63 by the end of the taxable year**. In the year the participant reaches 64, the regular age-50 catch-up applies again. For 2026 this means people born 1963 through 1966. Other deferrals and compensation can reduce the available amount; the 457(b) special last-three-years catch-up is a separate held calculation.
- The higher limit is an **optional plan term**. Check whether the plan document includes it. If it does not, only the $8,000 catch-up is available.
- The IRA catch-up is separate. It is $1,100 in 2026, and there is no age 60–63 increase for IRAs. There is no upper age limit on traditional IRA contributions; eligible compensation and contribution/deduction limits still apply ([Pub. 590-A](https://www.irs.gov/publications/p590a)).

### Roth-only catch-ups for higher-paid employees ([final regulations, §§1.414(v)-2(a), (b), (e)](https://www.federalregister.gov/documents/2025/09/16/2025-17865/catch-up-contributions))

For ordinary plans in 2026, catch-ups must be designated Roth when preceding-calendar-year sponsoring-employer §3121(a) wages exceed **$150,000**. Exactly $150,000 does not exceed the threshold. The regular $24,500 deferral need not be Roth. This is not a test of household income or all employers' wages combined.

- Final regulations use Social Security wages (W-2 box 3), but generally apply from 2027. **For 2026, reasonable good-faith statutory interpretation applies; using Medicare wages (box 5) can satisfy that standard.** Obtain the plan administrator's implementation before applying a boundary example. Related-employer aggregation, deemed elections and corrections depend on plan terms: Check this point with one of our partner accountants.
- No preceding-year sponsoring-employer FICA wages means the statutory Roth requirement does not apply; self-employment-only earnings are not FICA wages. SEP and SIMPLE IRA plans are excluded. Do not confuse SIMPLE IRA with SIMPLE 401(k).
- A plan without Roth has a zero catch-up limit for a participant subject to the Roth requirement. It can permit other participants' catch-ups, subject to nondiscrimination restrictions; it is not automatically barred from every catch-up. Check actual plan terms.
- Notice 2023-62 transition relief covered 2024–2025 and was not generally extended. Certain multiemployer collectively bargained plans have special deemed-compliance relief, and governmental/collectively bargained plans have different regulatory applicability dates. Do not apply the ordinary-plan rule to them without confirmation: Check this point with one of our partner accountants.

### RMD starting age and deadlines ([IRS: RMDs](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-required-minimum-distributions-rmds))

| Date of birth | Applicable age |
| --- | --- |
| before 1 July 1949 | 70½ |
| 1 July 1949 to 31 December 1950 | 72 |
| 1951 to 1958 | 73 |
| 1959 | **unsettled** (see below) |
| 1960 or later | 75 |

- **Born in 1959:** non-usable hold. The final regulations reserve this cohort; do not give a definitive starting age here. Check this point with one of our partner accountants.
- **IRAs, SEP IRAs and SIMPLE IRAs.** The required beginning date is **1 April of the year after the year the owner reaches the applicable age**.
- **Ordinary workplace plans (governmental/church special ownership rules held).** The first RMD is due by 1 April after the later of reaching the applicable age or retiring, if the plan allows the delay. The delay does not apply to a **5-percent owner**, who must start at the applicable age. It never applies to IRAs.
- **Later years.** Each later RMD is due by **31 December**. If the first RMD is delayed to 1 April, two RMDs fall in that calendar year.
- **2026 in practice.** People born in 1953 reach 73 in 2026. Their first RMD is for 2026, due by 1 April 2027. The 2027 RMD is due by 31 December 2027.
- **Amount.** Divide the balance at the prior 31 December by the Uniform Lifetime Table (Pub. 590-B, Table III) divisor for the owner's age that year. For example, the divisor is 26.5 at 73, 25.5 at 74 and 24.6 at 75. Use the Joint and Last Survivor Table instead if the sole beneficiary is a spouse more than 10 years younger.
- **Aggregation.**
  - IRAs: calculate the RMD for each IRA separately, then take the total from any one or more of them.
  - 403(b) contracts: the same rule applies among 403(b) contracts.
  - 401(k) and 457(b) plans: each plan must pay its own RMD.
- **Roth accounts.** Roth IRAs and designated Roth accounts in 401(k), 403(b) and governmental 457(b) plans need no withdrawals while the owner is alive. Beneficiaries are subject to the RMD rules.

### Missed RMDs: the excise tax ([IRC §4974](https://uscode.house.gov/us/usc/t26/s4974/))

- **Rate.** The tax is **25%** of the shortfall (IRC §4974(a)).
- **Reduced rate.** It drops to **10%** if, within the correction window, the taxpayer takes the missed amount from the same plan **and** files a return reflecting the tax.
- **Correction window.** It starts when the tax is imposed. It ends on the **earliest** of:
  - the mailing of a notice of deficiency;
  - assessment of the tax;
  - the last day of the second taxable year that begins after the year in which the tax was imposed.
- **Waiver.** The IRS can waive part or all of the tax if the shortfall was due to reasonable error and reasonable steps are being taken to remedy it. To ask for this:
  - take the missed distribution;
  - complete Form 5329, Part IX;
  - follow the year-specific Form 5329 waiver instructions, including the explanation;
  - attach a statement of explanation.
  
  The IRS decides whether to grant the waiver.

### Inherited accounts: the 10-year rule ([RMD final regulations](https://www.federalregister.gov/documents/2024/07/19/2024-14542/required-minimum-distributions))

These rules apply where the owner died after 2019.

**Eligible designated beneficiaries (EDBs)** are identified at the owner's death. There are five kinds:

- the surviving spouse;
- the owner's child who has not reached the age of majority. The final regulations fix this at the **21st birthday**, after which the 10-year rule runs;
- a disabled individual;
- a chronically ill individual;
- any other individual not more than 10 years younger than the owner.

An EDB may use life-expectancy payments. Other individual beneficiaries, such as most adult children, grandchildren and friends, are designated beneficiaries who are not EDBs.

**The 10-year rule.** A non-EDB must empty the account by **31 December of the year containing the 10th anniversary of the owner's death**.

**Annual RMDs inside the 10 years**, under the final regulations of 19 July 2024, which apply from 2025:

- **Owner died before the required beginning date:** no distribution is required before the 10th year.
- **Owner died on or after the required beginning date:** annual RMDs **continue** in years 1 to 9, **and** the balance must be emptied by the end of year 10. The annual RMD uses the longer of:
  - the beneficiary's single life expectancy (Table I, fixed in the year after death and reduced by 1 each year); or
  - the owner's remaining life expectancy.

**Relief for 2021 to 2024 only.** Notices 2022-53, 2023-54 and 2024-35 waived the excise tax on these annual RMDs for 2021 to 2024. The relief covered beneficiaries of owners who died in 2020 to 2023 after their required beginning date.

- The relief did **not** extend the 10-year deadline.
- Waived years do not have to be made up.
- **2025 was the first year the annual RMD was enforced.** A 2025 shortfall is now a live 25% / 10% exposure (see Missed RMDs).

**Spouses.** A surviving spouse who is the sole beneficiary can elect to treat the inherited IRA as their own, in which case the Uniform Lifetime Table applies. Spousal elections interact with plan terms. Refer complex spousal cases to the plan or to Pub. 590-B.

### Qualified charitable distributions ([Pub. 590-B](https://www.irs.gov/publications/p590b))

- **Who.** The IRA owner must be **at least 70½ on the date of the distribution**.
- **How.** The IRA trustee pays the amount **directly** to a charity eligible to receive deductible contributions. A QCD cannot come from an ongoing SEP IRA or SIMPLE IRA. The taxpayer needs the same acknowledgment from the charity that a deduction would need.
- **Limit.** $111,000 per person for 2026. Each spouse on a joint return has their own limit. Any excess is taxable like any other distribution. The QCD is limited to the amount that would otherwise be taxable, and it comes first out of taxable amounts.
- **One-time split-interest election:** the indexed ceiling is in the table, but eligibility, permitted income interests, nonassignment, annuity terms and the election statement are not established by that ceiling. Non-usable hold: Check this point with one of our partner accountants.
- **Offset for post-70½ deductions.** The excludable QCD is reduced by deductible IRA contributions for any year the owner was 70½ or over, to the extent those contributions have not already reduced an earlier QCD. Use the Pub. 590-B Appendix D worksheet.
- **RMD.** A QCD counts toward the year's RMD.
- **No double benefit.** There is no charitable deduction for a QCD excluded from income.

### 529 plan to Roth IRA rollover ([IRC §529(c)(3)(E)](https://uscode.house.gov/us/usc/t26/s529/))

This is available for distributions after 31 December 2023. All of the following conditions must be met:

- the 529 account has been maintained for the beneficiary for the **15-year period ending on the date of the distribution**. Pub. 590-A describes this as an account open for more than 15 years;
- the transfer is a **direct trustee-to-trustee transfer** to a Roth IRA **for the 529 beneficiary**;
- it excludes contributions made in the **5 years** before the distribution, and the earnings on them;
- in any year, the rollover is limited to the Roth IRA annual limit ($7,500 in 2026, plus the catch-up if 50 or over), **reduced by all other IRA contributions for that beneficiary for the year**. The Roth limit is tied to the §219 amount, so it cannot exceed the beneficiary's compensation for the year. Treat compensation at least equal to the rollover as a condition;
- the Roth income phase-out is **disregarded** for this rollover (IRC §408A(c)(3)(E));
- the lifetime cap is **$35,000** per beneficiary.

**Timing.** A distribution made after 31 December 2025 and before 15 April 2026, rolled over by 15 April 2026 and designated for 2025, counts as a 2025 Roth contribution.

**Beneficiary change:** non-usable hold; this Guide gives no conclusion on the 15-year clock after a change. Check this point with one of our partner accountants.

### Saver's Credit now, Saver's Match from 2027 ([IRC §6433](https://uscode.house.gov/us/usc/t26/s6433/), [IRC §25B](https://uscode.house.gov/us/usc/t26/s25B/))

- **2026.** The Saver's Credit (IRC §25B) still applies to IRA contributions, elective deferrals and voluntary employee contributions, with the 2026 income limits above. Contributions to the person's own ABLE account also count: P.L. 119-21 (July 2025) made them permanently eligible, for taxable years ending after 31 December 2025.
- **From 2027** (taxable years beginning after 31 December 2026):
  - **The Saver's Credit narrows.** It no longer counts retirement contributions, only the person's own ABLE account contributions. P.L. 119-21 raises the $2,000 contribution cap to $2,100.
  - **Retirement contributions move to the Saver's Match** (IRC §6433). The match is 50% of up to $2,000 of qualifying contributions, so at most **$1,000**.
  - **Where the match goes.** The IRS pays it into the person's retirement account, not as cash. The account must be one that accepts it and is **not a Roth IRA**, nor a designated Roth account.
  - **Small matches.** Someone whose match is above zero but under $100 can elect to take it as a credit instead.
- **Who is eligible for the match.** The person must:
  - be aged 18 or over at year end;
  - not be claimed as a dependent;
  - not be a student;
  - not be a nonresident alien, unless electing to be treated as a resident.
- **Contribution reduction.** Qualifying contributions are reduced by distributions in a testing period. The period covers the year, the 2 years before it, and the time after the year up to the return due date (including extensions). Plan loans, rollovers, conversions, and corrective or returned excess contributions are not counted (§6433(d)(2)(C)).
- **Phase-out.** Married filing jointly: it starts at modified AGI of $41,000 and runs over $30,000, so it is gone at **$71,000**. Head of household uses ¾ of those amounts. Other filers (not joint, not head of household, not surviving spouse) use ½; surviving spouses use the joint amounts. Compute the proportional reduction in the 50% rate and round that reduction down to a whole percentage point. Use §6433(f)(1) modified AGI, which adds back retirement-contribution deductions/exclusions and disregards §§911, 931 and 933. The $41,000 figure is indexed only for years after 2027.

### Early distributions: SECURE-era exceptions to the additional tax ([IRS exceptions table](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions))

The ordinary IRA additional tax before age 59½ is generally 10%; a SIMPLE IRA distribution in its first two participation years can carry 25%. An exception does not by itself exclude taxable income. **Do not use the following headings or indexed ceilings as a finding of eligibility.** Each route is held for account-type, event, timing, certification and repayment analysis: emergency personal expense; domestic abuse; qualified birth/adoption; qualified disaster recovery; terminal illness; long-term-care premiums; automatic-enrollment permissible withdrawal. Check this point with one of our partner accountants.

### Solo 401(k): first-year deferrals and deadlines ([IRC §401(b)](https://uscode.house.gov/us/usc/t26/s401/))

- **Adopting a plan after year end.** An employer may adopt a plan after the year ends but before the return due date **including extensions**, and treat it as adopted on the last day of the year.
- **The election deadline (all other cases).** A sole proprietor's or partner's compensation is treated as available on the last day of the taxable year, so the owner **cannot make a deferral election for a year after that year ends** ([Pub. 560, owner/employee election rule](https://www.irs.gov/publications/p560)). For an existing plan, the 2026 deferral election must be made by 31 December 2026. Only the **deposit** of the deferral can wait until the return due date.
- **First-year exception.** This applies only to a plan adopted after year end under the retroactive-adoption election above. An owner of an unincorporated business who is its **only employee** may make **elective deferrals** for that plan's **first plan year** up to the return due date **without extensions** (normally 15 April). They are treated as made in that first year.
- **Employer contributions.** Profit-sharing contributions to a 401(k), and SEP contributions, are due by the due date of the employer's return **including extensions**.

### Automatic enrollment for new 401(k) and 403(b) plans ([IRC §414A](https://uscode.house.gov/us/usc/t26/s414A/))

- **Which plans.** For plan years beginning after 31 December 2024, §414A generally covers 401(k) arrangements and 403(b) plans established on or after 29 December 2022. An employer joining a pre-existing multiple-employer plan after enactment does not inherit the grandfathering.
- **Default rate.** The first-year rate must be between 3% and 10%. It rises by 1 percentage point after each completed participation year until at least 10%, never more than 15%; the employee may elect out or choose another rate. The arrangement must allow §414(w) permissible withdrawals and compliant default investments.
- **Exceptions:**
  - plans established before 29 December 2022;
  - SIMPLE 401(k) plans;
  - governmental and church plans;
  - employers (including predecessors) in existence for less than 3 years;
  - employers that have never normally employed more than 10 employees.

  The small-employer relief ends 1 year after the close of the first year in which the employer normally employs more than 10.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Age 59 or 64 at 31 December 2026 | Regular $8,000 catch-up ceiling; ages 60–63 instead use $11,250 |
| Sponsor wages exactly $150,000 / over $150,000 under the permitted 2026 measure | Exactly is not above threshold; above is Roth-only for an ordinary-plan catch-up; actual plan terms still control |
| No sponsor FICA wages; self-employment only | Statutory Roth mandate does not apply; confirm plan restrictions |
| Still working at applicable age | No IRA postponement; ordinary workplace delay requires plan permission and non-5-percent-owner status |
| Non-EDB beneficiary, owner died before / on or after RBD | Before: no annual RMD in years 1–9; on/after: annual RMD plus year-10 cleanout |
| IRA distribution at age 70 and 5 months / paid to owner then donated | Not a QCD; assess basis and taxation separately |
| 529 opened 14 years ago / full IRA annual limit already used | No eligible rollover yet / no annual room |

## Worked cases

The contribution cases assume adequate eligible compensation, no other deferrals using the limit, plan permission and the stated ordinary-plan wage interpretation.

**Case C1: ordinary catch-up.** Ana is 55 at the end of 2026. Her 2025 box 3 wages from the employer sponsoring her 401(k) were $120,000, which is under the threshold. She may defer $24,500 + $8,000 = $32,500, pre-tax or Roth as the plan allows.

**Case C2: age 62, Roth catch-up.** Ben turns 62 in 2026. The original supplied 2025 box 3 wages of $180,000 exceed the 2025 Social Security wage-base cap of $176,100, so that box label cannot be relied on. Hold the actual wage test pending corrected W-2 evidence. Conditional on sponsor wages exceeding $150,000 under the plan's permitted measure, the plan offers the higher catch-up and a Roth option. He may defer $24,500 + $11,250 = $35,750.

- On that condition the $11,250 catch-up must be designated Roth. The case's actual eligibility conclusion is non-usable until wage evidence is corrected. Check this point with one of our partner accountants.
- The $24,500 may be pre-tax.
- If the plan had no Roth option, he could make no catch-up contribution.

**Case C3: sole proprietor, excluded from the Roth rule.** Carla is 61 and has a Solo 401(k). Her only income is Schedule C self-employment income, with no FICA wages. The Roth catch-up rule does not apply to her 2026 catch-up. The $11,250 catch-up may be pre-tax if the plan document includes the higher limit. The §415(c) additions limit is still $72,000, before catch-ups.

**Case C4: first RMD.** Dev was born in March 1953, reaches 73 in 2026 and has a traditional IRA. His IRA balance at 31 December 2025 was $397,500. Assuming the Uniform Lifetime Table applies, his 2026 RMD is $397,500 ÷ 26.5 = $15,000.

- It is due by 1 April 2027.
- If he waits until then, his 2027 RMD is also due by 31 December 2027, and both distributions fall in 2027; basis or a QCD can change the taxable amount.

```oa-check
name: First RMD at 73 (2026)
inputs:
  balance_31_dec_2025: 397500
  divisor_age_73: 26.5
steps:
  - rmd_2026: balance_31_dec_2025 / divisor_age_73
expected:
  rmd_2026: 15000
```

**Case C5: inherited IRA, owner died after RBD.** Eva's father died in 2022 at 80, after his required beginning date. Eva is his adult daughter, not disabled or chronically ill, and more than 10 years younger. She is a non-EDB. She was 50 in 2023, the year after death. Her Table I factor is 36.2 for 2023, falling by 1 each year, so it is 33.2 for 2026. Her father's remaining life expectancy is shorter, so hers applies.

- **2026 RMD.** The balance at 31 December 2025 was $332,000, so the RMD is $332,000 ÷ 33.2 = $10,000, due by 31 December 2026.
- **Deadline.** The account must be empty by 31 December 2032.
- **Earlier years.** The 2023 and 2024 RMDs fell under Notice 2023-54 (2023) and Notice 2024-35 (2024) relief. The 2025 RMD was due, and if it was missed it must be corrected now.
- **Excise tax if the 2026 RMD is missed.** The tax is 25% of $10,000 = $2,500. It falls to 10% of $10,000 = $1,000 if she takes the amount and files within the correction window. She can also ask for a reasonable-cause waiver on Form 5329.

```oa-check
name: Inherited IRA annual RMD and missed-RMD excise tax (2026)
inputs:
  balance_31_dec_2025: 332000
  factor_2023: 36.2
  years_since_2023: 3
steps:
  - factor_2026: factor_2023 - years_since_2023
  - rmd_2026: balance_31_dec_2025 / factor_2026
  - excise_25: rmd_2026 * 0.25
  - excise_10_if_corrected: rmd_2026 * 0.10
expected:
  factor_2026: 33.2
  rmd_2026: 10000
  excise_25: 2500
  excise_10_if_corrected: 1000
```

**Case C6: 529 rollover.** Farah's 529 account was opened for her in 2009. In 2026 she is 24, has wages of $40,000 and has already contributed $2,000 to a traditional IRA for 2026. The account has been maintained for more than 15 years. Contributions from the last 5 years, and their earnings, are excluded. Assuming at least $5,500 eligible old funds and unused lifetime capacity, her maximum 2026 rollover is $7,500 − $2,000 = $5,500. It must be a direct transfer to a Roth IRA in her name, and it counts toward her $35,000 lifetime cap.

## 2025 returns and corrections

For 2025, use these figures instead:

| Item (2025) | Amount | Source |
| --- | --- | --- |
| Elective deferral limit | $23,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, age 50 or over | $7,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, age 60 to 63 in 2025 | $11,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| §415(c) annual additions limit | $70,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE deferral limit | $16,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up, age 50 or over | $3,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA limit | $7,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA catch-up | $1,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| QCD limit | $108,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| One-time split-interest QCD | $54,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Domestic abuse distribution cap | $10,300 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |

- **Roth income phase-out for 2025:** $150,000 to $165,000 for single or head of household; $236,000 to $246,000 married filing jointly.
- **Roth catch-up.** It was **not** required in 2025, because the Notice 2023-62 transition period ran to 31 December 2025. A pre-tax catch-up in 2025 is fine.
- **Missed 2025 RMDs are still correctable.** This includes the first annual inherited-IRA RMD under the final regulations, and the first RMD of people born in 1952, which was due by 1 April 2026. Take the distribution now and report it on Form 5329. The 10% rate needs both steps within the correction window.
- **IRA contributions for 2025** were due by 15 April 2026. Extensions do not apply to them.
- **Employer contributions for 2025.** SEP contributions and 401(k) profit-sharing contributions had the applicable employer-return due date, including a valid extension. Do not imply the ordinary extended deadline remains open on this read date.
- **QCD reporting.** On the 2025 Form 1040 the QCD is reported on the IRA lines. Enter the taxable amount on line 4b and tick the QCD box on line 4c.

## Historical cases and holds

Original tax years and case inputs are retained below. A held result is **not usable tax advice**.

| Original case | Destination / result |
| --- | --- |
| H1: Hiroshi, born 4 March 1952; 2025 traditional IRA opening balance $480,000, Roth $150,000; no inherited or employer account | Uniform-table 2025 RMD = $480,000 / 26.5 = $18,113.21, by 1 April 2026. Roth owner RMD zero. The old $18,491 2026 result has no supplied 31 December 2025 balance: non-usable hold. Check this point with one of our partner accountants. |
| H2: Priya, unmarried sole proprietor, 2025 profit $250,000, plan established 2020, no other employees; stated age 62 but birth year 1962 | Conflicting age inputs: born 1962 means turning 63 in 2025, still the higher catch-up band. Original supplied half-SE tax $14,266 and employer $46,847 are not adopted as a computation. Conditional upper ceiling $70,000 + $11,250 = $81,250; actual contribution/deduction non-usable pending earned-income worksheet and elections. Check this point with one of our partner accountants. |
| H3: Devon age 45 in 2025 but stated 41 in 2022; father born 1948, died 14 June 2021 aged 73; $600,000 IRA, supplied 2020/2021 RMDs taken; no 2022–2024 withdrawals; 2024 closing balance $700,000 | Inconsistent beneficiary ages and incorrect old father RBD of 1 April 2020: birth in 1948 puts the applicable age at 70½. Preserve old divisor 44.3 / 41.3 only as rejected inputs. Annual RMD and excise outcomes non-usable until dates of birth are established. Check this point with one of our partner accountants. |
| H4: Karen, age 45, MAGI $300,000 in 2025, pre-tax SEP $180,000, Roth $40,000, no other traditional/SEP/SIMPLE accounts, proposed nondeductible contribution and conversion $7,000; proposed SEP-to-solo rollover $180,000 by year end | Backdoor Roth, aggregation, plan acceptance, year-end values and Form 8606 outcome held; do not use the prior tax-free reverse-rollover recommendation. Check this point with one of our partner accountants. |
| H5: 529 opened 2008, daughter age 24 in 2025, earnings $50,000, balance $42,000, 2021–2025 contributions $10,000 | $42,000 − $10,000 = $32,000 is arithmetic only: earnings attributable to recent contributions must also be excluded. Conditional 2025 annual ceiling $7,000 if no other IRA contributions, sufficient eligible old funds and lifetime capacity; no automatic 2026–2030 schedule. Check this point with one of our partner accountants. |
| H6: 2025 RMD $40,000; proposed direct QCD $30,000 to alma mater | If it qualifies under the QCD rules, $40,000 − $30,000 = $10,000 RMD remains. Institution eligibility, age and deductible-contribution offset must be established. |
| H7: pre-tax rollover IRA $200,000, nondeductible contribution $7,000, proposed conversion $7,000; old aggregate $207,000 | Pro-rata conversion result held until year-end balances, all distributions and basis are established. No automatic tax-free conversion. Check this point with one of our partner accountants. |
| H8: first Roth contribution 2020, conversion $50,000 in 2024, age 55 | Roth contribution/conversion clocks, ordering and early-tax conclusion held pending complete distribution facts. Check this point with one of our partner accountants. |
| H9: corporate employee, 2025 W-2 wages $200,000, turns 52 in 2026; illustrative 24% bracket | The original $7,500 catch-up / $1,800 tax effect is a stale 2025 amount. Conditional 2026 catch-up $8,000 gives $1,920 at the supplied 24% rate; actual sponsor wage measure and plan terms must be confirmed. Check this point with one of our partner accountants. |

Additional legacy numerical illustrations are held, not usable outcomes: a $50 enrollment gift card; age-50 2025 mega-backdoor arithmetic $77,500 − $31,000 = $46,500; and the supplied Social Security interaction 22% × 1.85 = 40.7% (not an established marginal tax rate). Check this point with one of our partner accountants.

## When to refuse or refer

Non-usable holds: special early distributions and repayments, including the public-safety/private-firefighter exception; split-interest QCDs; born-1959 RMD age; changed 529 beneficiaries; spousal elections; disability/chronic-illness documentation; pre-1987 403(b) amounts, pre-2020 deaths, trusts, estates, charities and successor/multiple beneficiaries; governmental/collectively bargained special catch-up rules; §45E startup and employer-contribution credits; student-loan matching; starter and multiple-employer plans; LTPT eligibility; PLESA operation; small incentives; Roth SEP/SIMPLE and Roth employer matching; backdoor/mega-backdoor Roth, Roth clocks and ordering; §408(d)(2) and reverse rollovers; plan loans/5500/EPCRS/amendments/qualification penalties; defined-benefit/cash-balance/ESOP/prohibited transactions/457(f)/withdrawal liability; state auto-IRA, foreign pension reporting and cross-border treatment; Roth conversion interactions with estimates, NIIT, IRMAA, premium tax credit, Social Security inclusion, QBI and excess business losses. Check this point with one of our partner accountants.

## Filing and payment

Sources: [Pub. 560](https://www.irs.gov/publications/p560), [Pub. 590-A](https://www.irs.gov/publications/p590a).

1. **2026 IRA and Roth IRA contributions.** Due by the due date of the 2026 return, **not including extensions**. For most people that is 15 April 2027.
2. **Elective deferrals.**
   - Employees defer through payroll during 2026.
   - For a self-employed person's plan, the deferral **election** must be made by the last day of the taxable year. Pub. 560's date (the due date of the employer's return, including extensions) is the last date to **deposit** the deferral, not to elect it.
   - The one exception is a sole owner's Solo 401(k) adopted after year end: first-year deferrals must be paid by the unextended due date.
3. **SEP and 401(k) employer contributions.** Due by the employer's return due date, including extensions.
4. **RMDs.** Take them by 31 December. The first RMD may wait until 1 April of the following year.
5. **Form 5329.** Report the RMD excise tax, any waiver request, and the early-distribution tax or an exception that Form 1099-R box 7 does not show.
6. **Form 8606.** Report nondeductible IRA contributions, conversions, and distributions with basis.
7. **Extensions.** An extension to 15 October gives more time to file, not to pay.

For written federal tax advice, apply [Circular 230 §10.37](https://www.irs.gov/pub/irs-pdf/pcir230.pdf): use reasonable factual and legal assumptions and consider the relevant facts; do not treat illustrative ceilings as a recommended contribution or distribution.

## Sources

| Source and text read | URL | Read on |
| --- | --- | --- |
| Notice 2025-67, pp. 1–5: 2026 limits, preceding amounts for 2025, Roth ranges and Saver's Credit tiers | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | 2026-11-27 |
| Catch-up final regulations: §§1.414(v)-1 and -2, wage measure, no-Roth plans, nondiscrimination, good-faith period and special applicability | https://www.federalregister.gov/documents/2025/09/16/2025-17865/catch-up-contributions | 2026-11-27 |
| RMD final regulations: §§1.401(a)(9)-2, -4 and -5, applicable ages, EDBs and post-death requirements | https://www.federalregister.gov/documents/2024/07/19/2024-14542/required-minimum-distributions | 2026-11-27 |
| Publication 590-B: RMD tables, beneficiary method, QCD and early IRA tax sections | https://www.irs.gov/publications/p590b | 2026-11-27 |
| Notice 2024-35: specified annual RMD relief for 2024 and previous notices | https://www.irs.gov/pub/irs-drop/n-24-35.pdf | 2026-11-27 |
| IRC §4974: excise, reduction, full correction window and waiver | https://uscode.house.gov/us/usc/t26/s4974/ | 2026-11-27 |
| IRC §529(c)(3)(E) and Publication 590-A: direct transfer, age of account, excluded recent funds and caps; 2025 timing | https://uscode.house.gov/us/usc/t26/s529/ | 2026-11-27 |
| Publication 590-A: IRA contributions, 529 transfer and deadlines | https://www.irs.gov/publications/p590a | 2026-11-27 |
| IRC §25B: eligibility, testing period, ABLE amendment and effective dates | https://uscode.house.gov/us/usc/t26/s25B/ | 2026-11-27 |
| IRC §6433: match, receiving account, eligibility, modified AGI, reduction and effective date | https://uscode.house.gov/us/usc/t26/s6433/ | 2026-11-27 |
| IRC §414A: mandate, investments, employee election and all listed exemptions | https://uscode.house.gov/us/usc/t26/s414A/ | 2026-11-27 |
| IRC §401(b)(2): adoption and sole-owner first-year deferrals, reused unchanged completed read from retirement proof | https://uscode.house.gov/us/usc/t26/s401/ | 2026-11-27 |
| Form 5329 (2025): Part IX and reasonable-error waiver procedure | https://www.irs.gov/instructions/i5329 | 2026-11-27 |
| Circular 230: §10.37 factual/legal assumptions | https://www.irs.gov/pub/irs-pdf/pcir230.pdf | 2026-11-27 |
| Publication 560: owner election/deposit and employer deadlines, reused unchanged retirement proof | https://www.irs.gov/publications/p560 | 2026-11-27 |

Not yet confirmed: every non-usable hold in the referral section and H1–H9 and the additional legacy illustrations; actual 2026 wage evidence for C2; final 2026 form/box instructions (2025 reporting is expressly dated); special SIMPLE higher-limit eligibility. Check this point with one of our partner accountants.
