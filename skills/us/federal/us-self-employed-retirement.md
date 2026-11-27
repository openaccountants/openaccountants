---
name: us-self-employed-retirement
description: Compute 2026 SEP, solo 401(k), SIMPLE IRA and personal IRA contributions for a sole proprietor or disregarded single-member LLC with no employees. Covers contribution and deduction bases, shared deferrals, catch-ups, IRA income tests, elections and deadlines. Load us-schedule-c-and-se-computation first; pass the deductible amount to us-self-employed-health-insurance and us-qbi-deduction. Historical 2025 examples are explicitly separated. Federal only.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US self-employed retirement contributions, tax year 2026

For a sole proprietor with one business and no common-law employees, compute the deductible SE-tax share first, then the plan contribution. A SEP has employer contributions; a solo 401(k) can also have elective deferrals. Plan terms, earned income and deadlines constrain both. A personal IRA has a separate contribution limit and income tests.

## Ask the client first

Read the available records before requesting missing facts: age at year end; filing status and whether spouses lived together; business profit and deductible SE-tax share; all W-2 wages and deferrals; plan documents, adoption/election/deposit dates; pre-tax versus Roth designations; IRA compensation and modified AGI; spouse's compensation/contributions/plan coverage; and year-end assets of every one-participant plan maintained by the employer. Identify other businesses, related employers, partnerships and employees before using the single-business calculation.

Do not invent eligibility, elections or contributions when records are missing. An under-50, pre-tax estimate may illustrate arithmetic only; hold the deduction until the actual plan terms, age and payments are established. Present the maximum separately from the amount actually chosen and paid.

## Rates, bands and thresholds

All amounts are USD for 2026. Catch-ups require plan permission, sufficient compensation and eligibility under section 414(v); the ages-60–63 amount replaces the ordinary catch-up. [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf), [26 U.S.C. 414(v)](https://uscode.house.gov/us/usc/t26/s414/).

| Item and condition | 2026 amount | Official source |
| --- | --- | --- |
| Basic 401(k) elective deferrals, pre-tax and designated Roth combined, shared per person with other section 402(g) deferrals | 24,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Ordinary 401(k) catch-up, age 50–59 or 64+ at year end | 8,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| 401(k) catch-up, attains age 60, 61, 62 or 63 during the year | 11,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Annual additions, excluding eligible catch-ups | 72,000, also subject to the compensation limit | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [IRS solo plans](https://www.irs.gov/retirement-plans/one-participant-401k-plans) |
| Annual compensation cap used in the employer contribution calculation | 360,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE basic deferrals: general limit; higher limit for a qualifying employer with no more than 25 employees receiving at least 5,000 in the preceding year (also apply the prior-plan restriction below) | 17,000; 18,100 respectively | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [26 U.S.C. 408(p)(2)(E)](https://uscode.house.gov/us/usc/t26/s408/) |
| SIMPLE ordinary catch-up, age 50–59 or 64+: general plan; higher-limit small-employer plan above | 4,000; 3,850 respectively | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [26 U.S.C. 414(v)(2)(B)](https://uscode.house.gov/us/usc/t26/s414/) |
| SIMPLE catch-up, attains age 60, 61, 62 or 63 | 5,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Personal traditional and Roth IRA contributions combined | 7,500; additional 1,100 if age 50+ by year end (8,600 total, computed) | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out: covered contributor, single or head of household | MAGI 81,000–91,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out: covered contributor, joint return or qualifying surviving spouse | MAGI 129,000–149,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out: contributor not covered, spouse covered, joint return | MAGI 242,000–252,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out: separate return, lived together during year, contributor or spouse covered | MAGI 0–10,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [Pub. 590-A](https://www.irs.gov/publications/p590a) |
| Roth IRA contribution phase-out: single, head of household, or separate return with spouses apart all year | MAGI 153,000–168,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [Pub. 590-A](https://www.irs.gov/publications/p590a) |
| Roth IRA contribution phase-out: joint return or qualifying surviving spouse | MAGI 242,000–252,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA contribution phase-out: separate return, lived together at any time | MAGI 0–10,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [Pub. 590-A](https://www.irs.gov/publications/p590a) |

Traditional IRA deduction: the full income-based allowance applies at or below the lower threshold, partial above it and below the upper threshold, none at or above the upper threshold. Roth income reduction starts above the lower threshold and ends eligibility at the upper threshold. Use the applicable IRA worksheets and MAGI definition, not ordinary AGI or compensation interchangeably. For a separate-return traditional IRA test, spouses apart the entire year use the single rules. [Pub. 590-A, Deduction Phaseout and Roth contribution worksheets](https://www.irs.gov/publications/p590a).

## The method, step by step

### SEP and solo 401(k)

1. For the business sponsoring the plan, let **P** be Schedule C line 31 profit and **H** the attributable deductible regular SE-tax share. Let **N = P − H**, the worksheet amount before the owner's plan contribution. N is not final statutory plan compensation: that also accounts for the owner's contribution. Do not use 92.35% of profit as N. The health insurance deduction does not enter this subtraction. If N is not positive, there is no contribution supported by this business. Other businesses and allocation of H need separate analysis, not automatic pooling. [Pub. 560, Earned income and chapter 5](https://www.irs.gov/publications/p560).
2. Use the contribution rate in the actual plan. At a 25% plan rate, the reduced self-employed rate is 0.25 / 1.25 = **20%**. For a SEP without deferrals, the maximum is **min(20% × N, 25% × 360,000, 72,000)**. A lower plan rate requires its own reduced rate. [Pub. 560, Rate Worksheet and Deduction Worksheet](https://www.irs.gov/publications/p560); [2026 indexed amounts](https://www.irs.gov/pub/irs-drop/n-25-67.pdf).
3. For a solo 401(k), let **D** be allowable elected regular deferrals after the individual's shared limit and compensation tests. At the same 25% employer rate, employer contribution **E = min(20% × N, 25% × 360,000, 72,000 − D, (N − D) / 2)**. Require 0 ≤ D ≤ N. The worksheet then limits the regular deferral to min(D, N − E). Catch-up is limited to the permitted age-band amount and the remaining N − E − regular deferral; subtract designated Roth deferrals from the deductible total. Do not mechanically add 20% employer contributions to a deferral already using all earnings. [Pub. 560, worksheet steps 9–21](https://www.irs.gov/publications/p560).
4. Regular deferrals to other 401(k), 403(b), SARSEP or SIMPLE arrangements use the person's shared section 402(g) limit. Thus 15,000 already deferred leaves at most 9,500 of the 2026 basic limit. Employer annual-addition limits are not automatically separate per account: combine plans of the same employer; related-employer/multiple-plan cases are referred below. [Pub. 560, Limit on Elective Deferrals and More than one plan](https://www.irs.gov/publications/p560).

Age 59, or turning 64 during 2026, uses the ordinary catch-up, not the ages-60–63 amount. A new ordinary SEP has no elective-deferral catch-up; a legacy SARSEP is outside this calculation. For 2026, mandatory Roth catch-up applies where preceding-year FICA wages from the sponsoring employer exceed **150,000**; an owner with self-employment income only and no such wages does not meet that wage condition. Designated Roth deferrals give no current deduction. Roth SEP or Roth employer contribution features require the plan's terms and separate tax reporting; do not treat them as an ordinary pre-tax deduction. [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf); [26 U.S.C. 414(v)(7)](https://uscode.house.gov/us/usc/t26/s414/); [Pub. 560](https://www.irs.gov/publications/p560).

### SIMPLE IRA

For the higher small-employer deferral limit, confirm that neither the employer, controlled-group member nor predecessor maintained another specified retirement plan with contributions or benefit accruals for substantially the same employees during the three taxable years before the first SIMPLE year (section 408(p)(2)(E)(iv)); otherwise do not assume the higher limit. Use the SIMPLE compensation base: **Schedule SE line 4, before subtracting the owner's SIMPLE contributions**, not N above. Deferrals cannot exceed compensation or the applicable limit. For the ordinary required employer contribution, use a dollar-for-dollar match up to **3%** of compensation, or a **2%** nonelective contribution on compensation capped at **360,000** (7,200 maximum, computed). Read the election and notice terms before choosing either formula. Reduced matches, optional additional contributions and employers electing enhanced limits outside the small-employer category above need specialist review. A SIMPLE generally must be the only employer plan receiving contributions or benefit accruals for that year's services; exceptions are referred below. [Pub. 560, SIMPLE compensation and contribution limits](https://www.irs.gov/publications/p560); [26 U.S.C. 408(p)](https://uscode.house.gov/us/usc/t26/s408/).

### Personal IRAs and where the deduction goes

A separate personal IRA limit remains available alongside the business plan, but sufficient **IRA compensation must remain after the deductible business-plan contribution and deductible SE-tax share**. For a joint-return spousal IRA, combined eligible compensation must cover both spouses' contributions. Business-plan existence alone does not establish active participation: test actual contributions/allocations and the applicable coverage year. If neither spouse is covered, the income phase-out does not limit the traditional IRA deduction, though the contribution/compensation limits still apply. Nondeductible traditional IRA contributions require Form 8606. Personal Roth IRA contributions are not deductible. [Pub. 590-A, Compensation, Coverage, Spousal IRA and Nondeductible Contributions](https://www.irs.gov/publications/p590a).

The owner's deductible SEP, SIMPLE and qualified-plan contributions go on Schedule 1 line 16; the personal IRA deduction goes on line 20. Employee plan contributions, if employees are found, belong in the employee-expense calculation, not the owner's deduction: stop and refer. Deductible business-plan contributions generally reduce attributable QBI; personal IRA deductions and nondeductible Roth amounts do not produce that business deduction. Owner contributions do not reduce Schedule C profit or regular SE tax. Pass the same-business deduction to Form 7206 line 9 and `us-self-employed-health-insurance`; pass the attributable business deduction to `us-qbi-deduction`, estimated tax and return assembly. These box references use the **2025 forms**, not an assertion that 2026 forms are final. [Schedule 1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf); [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf); [IRS QBI guidance](https://www.irs.gov/newsroom/qualified-business-income-deduction); [Pub. 560, Where To Deduct](https://www.irs.gov/publications/p560).

## Filing and payment

These are ordinary calendar-year dates; disaster or other special postponements require separate confirmation. A filing extension must actually apply before using an extended deadline.

| Action for 2026 | Deadline / condition | Official source |
| --- | --- | --- |
| Adopt a qualified plan after year end | By the employer's return due date including extensions; elect treatment as adopted on the last day of the tax year | [26 U.S.C. 401(b)(2)](https://uscode.house.gov/us/usc/t26/s401/) |
| Elect deferrals under an existing solo plan | By 31 December 2026; owner deposits may follow by the return due date including extensions | [Pub. 560, Elective deferral](https://www.irs.gov/publications/p560) |
| First-year post-year-end solo-plan elective deferrals | Entire unincorporated business owned by the individual, who is its only employee; adoption and payment before the unextended return deadline, ordinarily 15 April 2027 | [26 U.S.C. 401(b)(2)](https://uscode.house.gov/us/usc/t26/s401/); [Pub. 560](https://www.irs.gov/publications/p560) |
| Qualified-plan employer contribution; SEP adoption and funding | Return due date including extensions, ordinarily 15 April 2027 or 15 October 2027 with a valid extension | [Pub. 560, SEP set-up and Contributions deadline](https://www.irs.gov/publications/p560) |
| First SIMPLE adoption | Effective between 1 January and 1 October if no prior SIMPLE; a new employer formed after 1 October acts as soon as administratively feasible. Replacement of a previous SIMPLE is effective only on 1 January | [Pub. 560, SIMPLE set-up deadline](https://www.irs.gov/publications/p560) |
| SIMPLE salary reduction versus employer contribution | For a self-employed individual, salary reduction within 30 days after year end (30 January 2027 for 2026); matching/nonelective amounts by the return due date including extensions. Do not apply the solo-401(k) deposit deadline to SIMPLE deferrals | [Pub. 560, Time limits for contributing funds](https://www.irs.gov/publications/p560); [IRS SIMPLE FAQs, depositing contributions](https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-simple-ira-plans) |
| Personal traditional/Roth IRA contribution | Ordinary unextended return deadline, 15 April 2027; filing extension does not extend it | [Pub. 590-A](https://www.irs.gov/publications/p590a) |
| One-participant annual return | Apply the combined-assets test across the employer's one-participant plans: exemption at 250,000 or less, except the final plan year. File Form 5500-EZ when required; seventh-month deadline moves to the next business day, so a calendar-2026 plan is ordinarily due **2 August 2027**, not Saturday 31 July | [Form 5500-EZ instructions, Who Does Not Have To File / When To File](https://www.irs.gov/pub/irs-pdf/i5500ez.pdf) |

A SEP does not require an annual Form 5500-EZ. Compare administration, actual plan terms and deposit dates when choosing a plan, not just the maximum deduction. For an under-50 owner with the full basic deferral available and a 25% employer rate, the solo plan reaches 72,000 at N = 237,500; the SEP reaches 72,000 at N = 360,000. The full 24,500 difference is possible from N = 40,833.333… to 237,500; below that, worksheet compensation constraints matter. These are computed comparisons, not universal plan recommendations. [Pub. 560, worksheet and SEP reporting](https://www.irs.gov/publications/p560); [2026 limits](https://www.irs.gov/pub/irs-drop/n-25-67.pdf).

## Worked cases

All results below assume timely permitted pre-tax contributions actually made, no employees and no other plans unless stated. Carry full precision through arithmetic and round only displayed outputs. Eligibility facts are illustrative assumptions, not evidence of a real person's entitlement.

**Case 1 (2026).** Single consultant, age 45, net profit 100,000, no wages/other plan. H = 100,000 × 0.9235 × 0.153 / 2 = 7,064.78 displayed; N = 92,935.23. SEP = 18,587.05; solo = 24,500 + 18,587.05 = **43,087.05**, 24,500 more. At the supplied 22% hypothetical rate, 24,500 × 22% = 5,390 before QBI and other tax interactions; this is not a computed tax-liability saving. A missed existing-plan election does not rule out the first-year exception above.

```oa-check
name: SEP against solo 401(k), age 45 (2026)
inputs:
  net_profit: 100000
  deferral_limit: 24500
  dollar_limit: 72000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - step_3: net_profit - half_se
  - employer: min(step_3 * 0.20, 360000 * 0.25, dollar_limit - deferral_limit, (step_3 - deferral_limit) / 2)
  - sep_total: min(step_3 * 0.20, dollar_limit)
  - solo_total: deferral_limit + employer
  - solo_advantage: solo_total - sep_total
expected:
  half_se: 7064.78
  step_3: 92935.23
  employer: 18587.05
  sep_total: 18587.05
  solo_total: 43087.05
  solo_advantage: 24500.00
```

**Case 2 (2026).** Part-time photographer, age 30, net profit 20,000, elected deferral 15,000. Assume no wages/other plan. H = 1,412.96 displayed; N = 18,587.05. Employer is limited to (N − 15,000) / 2 = 1,793.52, instead of the unconstrained 3,717.41. Total **16,793.52**.

```oa-check
name: Solo 401(k) earned income cap (2026)
inputs:
  net_profit: 20000
  deferral: 15000
  dollar_limit: 72000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - step_3: net_profit - half_se
  - employer_20: step_3 * 0.20
  - employer: min(employer_20, dollar_limit - deferral, (step_3 - deferral) / 2)
  - total: deferral + employer
expected:
  half_se: 1412.96
  step_3: 18587.05
  employer_20: 3717.41
  employer: 1793.52
  total: 16793.52
```

### Historical 2025 cases and regression inputs

The earlier Guide's people, ages, amounts and plan dates below remain **2025** cases; do not apply 2026 limits to them. The supplied half-SE amounts are retained as original inputs, not accepted as computed tax. For the recomputed comparisons, assume ordinary SE coverage, no wages or other income except the stated W-2 case, and no other plan contributions. Use the 2025 Social Security base **176,100**, deferral **23,500**, additions **70,000**, compensation cap **350,000**, catch-up **7,500** (ages 50–59/64+) or **11,250** (60–63), and personal IRA **7,000 + 1,000** at age 50+. [2025 Schedule SE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf); [Notice 2024-80](https://www.irs.gov/pub/irs-drop/n-24-80.pdf); [Pub. 560](https://www.irs.gov/publications/p560).

- **Example 1: Maria Hernandez**, single, age 34, freelance UX designer, Schedule C amount 62,644 (previously mislabeled net SE earnings), supplied half 4,427, solo plan established December 2024. Recomputed H = **4,425.66**, N = **58,218.34**, employer **11,643.67**, plus 23,500 gives **35,143.67**. If the supplied H were separately substantiated, its conditional total would instead be **35,143.40**.
- **Example 2: James Chen**, single, age 42, freelance software developer, profit 250,000, supplied half 16,583 (the July correction used 14,266). Recomputed H = **14,265.89**, N = **235,734.11**, SEP **47,146.82**; solo could reach **70,000**, a **22,853.18** difference. With the original supplied half alone, conditional SEP = **46,683.40**, difference **23,316.60**. No solo plan was established: missing 31 December alone does not eliminate the statutory first-year exception.
- **Example 3: Lisa Park**, joint return, age 61, freelance accountant, profit 180,000, supplied half 12,717, solo plan established 2020. Recomputed H = **12,716.60**, N = **167,283.41**, employer **33,456.68**, regular deferral 23,500 and catch-up 11,250: **68,206.68**. Conditional total using supplied H = **68,206.60**.
- **Example 4: Alex Rivera**, single, age 28, freelance graphic designer, profit 18,000, supplied half 1,272, no employer plan. Recomputed H = **1,271.66**, N = **16,728.34**, SEP **3,345.67**; a permitted solo deferral using all N leaves **zero** employer room. Conditional N from supplied H = **16,728**, SEP = **3,345.60**. Without a business plan, either personal traditional IRA or Roth IRA could take 7,000 under the stated income/compensation assumptions, combined limit 7,000; the traditional deduction changes if employer-plan coverage is established.
- **Test 1**, age 40, profit 100,000, supplied half 7,065, established solo plan: recomputed H **7,064.78**, employer **18,587.05**, solo **42,087.05**; conditional supplied-half total **42,087**.
- **Test 2**, age 55, profit 400,000, supplied half 23,886 (July correction 16,275), no solo plan: recomputed H **16,274.50**, N **383,725.50**, uncapped 20% **76,745.10**, SEP capped at **70,000**. Conditional supplied-half 20% = **75,222.80**, also capped at **70,000**. SEP has no age catch-up.
- **Test 3**, age 62, profit 200,000, supplied half 14,130 (July correction 13,596), established solo plan: recomputed H **13,596.35**, N **186,403.65**, employer **37,280.73**, regular subtotal **60,780.73**, plus 11,250 = **72,030.73**. Conditional supplied-half total **71,924**.
- **Test 4**, age 30, profit 20,000, supplied half 1,413, established solo plan: recomputed N **18,587.05** may all be deferred, employer **zero**. Conditional supplied-half total **18,587**, also with zero employer; the old **22,304** is not permitted.
- **Test 5**, age 45, profit 80,000, supplied half 5,652, established solo plan and W-2 plan deferrals 15,000: remaining basic deferral **8,500**; using the supplied H conditionally, N **74,348**, employer **14,869.60**, solo **23,369.60**. Actual W-2 Social Security wages are missing, so H cannot be verified from profit alone. Check this point with one of our partner accountants.
- **Test 6**, single, age 35, profit 120,000, SEP contribution 20,000 and supplied MAGI 100,000: the 2025 covered-single IRA deduction phase-out **79,000–89,000** leaves **zero** traditional IRA deduction. Roth contribution up to **7,000** is possible if the separate Roth MAGI is also 100,000 (below the 2025 **150,000–165,000** phase-out) and compensation suffices; do not derive either MAGI by subtracting only the SEP contribution. [Notice 2024-80](https://www.irs.gov/pub/irs-drop/n-24-80.pdf); [Pub. 590-A](https://www.irs.gov/publications/p590a).

```oa-check
name: Historical 2025 cases recomputed without changing original profit inputs
inputs:
  maria_profit: 62644
  james_profit: 250000
  lisa_profit: 180000
  alex_profit: 18000
  test1_profit: 100000
  test2_profit: 400000
  test3_profit: 200000
  test4_profit: 20000
  test5_profit: 80000
  test5_supplied_half: 5652
  test5_other_deferral: 15000
steps:
  - maria_half: maria_profit * 0.9235 * 0.153 / 2
  - maria_total: 23500 + (maria_profit - maria_half) * 0.20
  - james_half: (176100 * 0.124 + james_profit * 0.9235 * 0.029) / 2
  - james_sep: (james_profit - james_half) * 0.20
  - james_gap: 70000 - james_sep
  - lisa_half: lisa_profit * 0.9235 * 0.153 / 2
  - lisa_total: 23500 + 11250 + (lisa_profit - lisa_half) * 0.20
  - alex_half: alex_profit * 0.9235 * 0.153 / 2
  - alex_solo: alex_profit - alex_half
  - test1_total: 23500 + (test1_profit - test1_profit * 0.9235 * 0.153 / 2) * 0.20
  - test2_half: (176100 * 0.124 + test2_profit * 0.9235 * 0.029) / 2
  - test2_sep: min((test2_profit - test2_half) * 0.20, 70000)
  - test3_half: (176100 * 0.124 + test3_profit * 0.9235 * 0.029) / 2
  - test3_total: 23500 + 11250 + (test3_profit - test3_half) * 0.20
  - test4_solo: test4_profit - test4_profit * 0.9235 * 0.153 / 2
  - test5_conditional: 23500 - test5_other_deferral + (test5_profit - test5_supplied_half) * 0.20
expected:
  maria_half: 4425.66
  maria_total: 35143.67
  james_half: 14265.89
  james_sep: 47146.82
  james_gap: 22853.18
  lisa_half: 12716.60
  lisa_total: 68206.68
  alex_half: 1271.66
  alex_solo: 16728.34
  test1_total: 42087.05
  test2_half: 16274.50
  test2_sep: 70000.00
  test3_half: 13596.35
  test3_total: 72030.73
  test4_solo: 18587.05
  test5_conditional: 23369.60
```

## When to refuse or refer

| Code / topic | Action |
| --- | --- |
| R-RET-DB: defined benefit, cash balance, ESOP or stock-based plan | Check this point with one of our partner accountants. |
| R-RET-EMPLOYEES: employees, SEP participation eligibility, coverage, nondiscrimination, top-heavy or DOL administration | Check this point with one of our partner accountants. |
| R-RET-EXCESS: overcontributions, correction, penalties, interest or late filing | Check this point with one of our partner accountants. |
| R-RET-RMD: distributions, required minimum distributions, QCDs, inherited accounts, SIMPLE two-year rollover/early-distribution rules, 529-to-Roth, Saver's Credit or Saver's Match | Check this point with one of our partner accountants. Route retirement-update questions to `us-secure-2-and-retirement-updates`. |
| R-RET-ROTHCONV: Roth conversions/backdoor Roth, pro-rata IRA balances, Roth employer/SEP/SIMPLE reporting | Check this point with one of our partner accountants. |
| R-RET-PARTNER: partnership, S corporation, related employers, multiple self-employment businesses or overlapping employer plans; SIMPLE exceptions/special elections | Check this point with one of our partner accountants. S corporation return questions route to `us-form-1120-s-s-corporation-return`. |

## Completion checklist

Confirm the sponsoring business, actual plan rate and contribution type; reconcile the SE-tax share; apply the worksheet earnings and shared limits; check catch-up age and plan permission; document election, adoption and deposits; distinguish IRA compensation from each MAGI test; claim actual eligible payments rather than an unchosen maximum; and flag annual plan reporting. Part-year trading does not by itself prorate annual deferral limits, but actual earnings and eligibility still constrain them. [IRS solo-plan contribution rules](https://www.irs.gov/retirement-plans/one-participant-401k-plans).

This is general federal computational information. Apply reasonable factual and legal assumptions and consider all relevant facts; it does not establish any taxpayer's eligibility or replace professional review before filing (Circular 230 section 10.37).

## Sources

Read 2026-11-26 except the unchanged Schedule C/SE and SE-deduction dependency quotes reused from completed reads on 2026-11-22. Current-year operative limits are distinguished from the expressly historical cases.

- [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf): 2026 plan/IRA limits and income ranges.
- [IRS Publication 560 (2025 edition)](https://www.irs.gov/publications/p560): single-business earnings, SIMPLE base, contributions, elections, deadlines, reduced rate and deduction worksheet.
- [26 U.S.C. 401(b)(2), (c)(2)](https://uscode.house.gov/us/usc/t26/s401/), [408(p)](https://uscode.house.gov/us/usc/t26/s408/) and [414(v)](https://uscode.house.gov/us/usc/t26/s414/): late adoption/first-year deferrals, SIMPLE and catch-up conditions. Statute controls over the publication's unqualified year-end plan-adoption sentence.
- [IRS Publication 590-A (2025 edition, including 2026 updates)](https://www.irs.gov/publications/p590a): IRA compensation, coverage, MAGI, spousal limits, filing and contribution dates.
- [IRS one-participant 401(k) plans](https://www.irs.gov/retirement-plans/one-participant-401k-plans): owner contributions and shared deferrals.
- [Schedule 1](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf), [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf) and [IRS QBI guidance](https://www.irs.gov/newsroom/qualified-business-income-deduction): deduction mapping and attribution.
- [Form 5500-EZ instructions](https://www.irs.gov/pub/irs-pdf/i5500ez.pdf): combined assets, final-year filing and weekend rule; these instructions' “does not exceed” exemption controls this Guide over the overview page's abbreviated threshold.
- [Notice 2024-80](https://www.irs.gov/pub/irs-drop/n-24-80.pdf) and [2025 Schedule SE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf): historical 2025 cases; [current Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) and [26 U.S.C. 164(f)](https://uscode.house.gov/us/usc/t26/s164/) for the unchanged SE-tax computation dependency.

Not yet confirmed: final 2026 worksheet/form box numbering and individual eligibility in the illustrative cases. Do not file from assumed facts or historical form positions; referred topics have no usable tax conclusion here.
