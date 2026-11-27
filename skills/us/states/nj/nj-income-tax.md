---
name: nj-income-tax
description: New Jersey gross income tax for individuals, tax year 2026, on Form NJ-1040 (residents) and Form NJ-1040NR (nonresidents). Covers residency, the filing thresholds, income by category with no cross-category losses, Schedule NJ-BUS-1 business profit for sole proprietors and single-member LLCs, ordinary retirement exclusions with the 150,000 dollar ceiling and a separate Special Exclusion hold, exemptions, the property tax deduction or credit, the 2026 rate schedules (1.4% to 10.75%), the credit for tax paid to other states, NJEITC and Child Tax Credit, estimated tax and extensions. Trigger on "New Jersey income tax", "NJ income tax", "NJ-1040", "NJ-1040NR", "NJ-BUS-1", "NJ Division of Taxation", "NJ property tax deduction", "NJ pension exclusion".
version: "1.2"
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# New Jersey gross income tax (Forms NJ-1040 and NJ-1040NR), tax year 2026

> **Built from the law. Not yet approved.** Read dates and the portions read are in Sources. General reference only; this is not a signed professional opinion or a substitute for the factual analysis required for filing. U.S. tax notice: this material does not provide personalized tax advice.

**Answer first.** Compute New Jersey income by category, rather than copying federal AGI. The 2026 rate schedules run from 1.4% to 10.75%; a category loss does not directly reduce another category. The ordinary retirement exclusions have a $150,000 total-income ceiling, but the separate Special Exclusion needs its own test. For 2026 the Child Tax Credit is **$1,250 / $1,000 / $750 / $500 / $250** across the five income bands, under [P.L. 2026, c.26](https://pub.njleg.state.nj.us/Bills/2026/PL26/26_.PDF), despite the Division's Child Tax Credit page still displaying 2025. Use the dated return instructions below only for their stated year.

## Scope and who this is for

This Guide covers the New Jersey gross income tax for individuals: the resident return, **Form NJ-1040**, and the nonresident return, **Form NJ-1040NR**. The primary year is **tax year 2026** (returns filed in 2027). A dated section covers **2025 returns** (due 15 April 2026, or 15 October 2026 on a valid extension). It is written for employees, retirees, sole proprietors and owners of a single-member LLC disregarded for federal tax.

The current resident and nonresident instruction links read on **27 November 2026** still identify themselves as **2025**. Their line numbers and tax-table amounts below are therefore **2025 return instructions**, not a completed 2026 return specification. The 2026 NJ-1040-ES supplies the 2026 estimate worksheet, rates and exemptions. The enacted Child Tax Credit change takes precedence over the older summary page.

**Who is a resident** ([GIT-6, Part-Year Residents and Nonresidents](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf)):

- **Domiciled in New Jersey:** a resident, unless all three are true: no permanent home in New Jersey, a permanent home outside New Jersey, and not more than 30 days spent in New Jersey.
- **Not domiciled in New Jersey:** outside the military exception, a resident if the person maintains a permanent home in New Jersey **and** spends more than 183 days there. Exactly 183 days does not satisfy this test. Military members and spouses: **HOLD — do not apply this civilian test to decide their return. Check this point with one of our partner accountants.**
- A home kept only for a temporary purpose (for example a temporary job assignment) is not permanent. A vacation home is not a permanent home.
- There is no part-year return. A part-year resident files Form NJ-1040 for the resident period and, if they had New Jersey-source income while a nonresident, Form NJ-1040NR too.

**Who must file** ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)). A return is required if gross income from everywhere, for the entire year, was **more than** $10,000 (single, or married/civil union partner filing separately) or $20,000 (married/civil union couple filing jointly, head of household, qualifying widow(er)/surviving civil union partner). For a part-year filer, if there was no income during the resident period and no New Jersey-source income during the nonresident period, no return is required solely because worldwide income exceeds that threshold ([GIT-6, p.3](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf)). File when needed to recover withholding/estimated payments or claim an available refundable credit.

**Not covered** (see "When to refuse or refer"): trusts and estates (Form NJ-1041), amended returns (Form NJ-1040X), the entity side of the Pass-Through Business Alternative Income Tax (BAIT) and the Corporation Business Tax, which are in the separate Guide **nj-cbt-and-bait**, and New Jersey inheritance tax.

## Ask the client first

- Which tax year and resident period? Obtain the federal return and any section 1202 qualified-small-business-stock exclusion. Keep the 2025 and 2026 Child Tax Credit amounts separate.
- Domicile, any New Jersey home, any home outside New Jersey, and days spent in New Jersey. Did the person move in or out during the year?
- Federal filing status, civil-union status and each spouse's residency. The general federal-status rule has exceptions: if one spouse was a nonresident all year and the other a resident for any part, separate New Jersey returns are available, or both can elect resident treatment on a joint return. Civil-union partners may have a different state status. See [2025 instructions, p.6](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).
- Every income item, sorted by type: W-2 **box 16 state wages** (not box 1), interest, dividends, Schedule C profit or loss, sales of property, pensions and IRA withdrawals, partnership and S corporation shares (Schedules NJK-1 / NJ-K-1), rents, gambling, alimony received.
- Ages on 31 December (62 for the retirement exclusions, 65 for the extra exemption), blindness or disability, veteran status with discharge papers, and dependents (children age 5 or younger; full-time students under 22).
- For the business: any federal **section 179** deduction or **bonus depreciation** this year or in earlier years (a New Jersey adjustment is needed); self-employed health insurance paid, earned income from the business establishing the plan, and eligibility for any employer-subsidized plan for the taxpayer or spouse in each month; any self-employed 401(k) contributions.
- Main home in New Jersey: owned (property tax paid) or rented (rent paid), shared ownership, and whether the building is tax-exempt.
- Income taxed by another state or city (for example New York wages or Philadelphia wage tax), with that return.
- Federal earned income credit claimed and allowed.
- New Jersey withholding, estimated payments (dates and amounts), the prior-year New Jersey tax, and any extension payment.
- Health coverage by month during the tax year and coverage when filing; exemptions and any NJ-EZ Enroll election.

## The method, step by step

Form NJ-1040 line numbers are from the 2025 return ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).

1. **Choose the form.** Resident all year: Form NJ-1040. Nonresident with New Jersey-source income: Form NJ-1040NR. Moved in or out: both, as described in Scope. Part-year residents: prorate exemptions (2025 line 30, using the total on line 13) by resident months, counting 15 days or more as a month. For property tax, deduct only the eligible tax or rent due and paid during the resident period; prorate the credit by qualified resident months rather than applying a second monthly reduction to actual resident-period property taxes. Deductions such as medical expenses and alimony count only amounts paid while a resident. The pension exclusion maximum is prorated by months only if income for the whole year is $100,000 or less, and is not prorated above that; whole-year income must be $150,000 or less (Worksheet E for the other retirement income exclusion).
2. **Do not start from federal AGI.** New Jersey taxes gross income in separate categories, each on its own line: wages (line 15, from W-2 box 16), taxable interest (16a), dividends (17), net profits from business (18, Schedule NJ-BUS-1 Part I), net gains from disposition of property (19, Schedule NJ-DOP), taxable pensions, annuities and IRA withdrawals (20a), partnership income (21), S corporation income (22), rents, royalties, patents and copyrights (23), net gambling winnings (24), alimony received (25) and other income (26). Residents report income from everywhere.
3. **Net losses only inside a category.** A loss can reduce gains in the **same** category only. A net loss in a category is not entered at all (no negative number, no zero), cannot reduce any other category, and cannot be carried back or forward. Example: a Schedule C loss cannot reduce wages; a stock loss cannot reduce rental income. Separately compute the Alternative Business Calculation Adjustment on line 35, Schedule NJ-BUS-2, for eligible business, rents/royalties, partnership and S corporation losses. It is not a direct offset against wages: from 2016, the adjustment is 50% of the business increment; alternative business losses can carry forward for 20 years under [N.J.S.A. 54A:3-9](https://pub.njleg.state.nj.us/Bills/2010/PL11/60_.PDF).
4. **Business profit (Schedule NJ-BUS-1 Part I).** Start from federal Schedule C (or F) and adjust: add back taxes based on income; take out interest exempt for New Jersey; add other states' bond interest; deduct ordinary business meal and entertainment expenses that were not allowed on the federal return; deduct qualified contributions to a self-employed 401(k) plan (not above the federal limits); add interest and dividends derived in the conduct of the business; add or subtract business income or losses from rentals, royalties, patents or copyrights, and gains or losses on disposing of the business's property; add or subtract the depreciation adjustment from Worksheet GIT-DEP (use the result of the current worksheet, rather than an old line-number shortcut). Cannabis licensee adjustments and disputed business-versus-investment classifications are held for a partner accountant. Do not assume every federal deduction carries over unchanged. The federal deduction for half of self-employment tax is not a Schedule C expense, so it does not reduce New Jersey income.
5. **Total income (line 27)** = lines 15 through 26, leaving out the tax-exempt interest on 16b and the excludable pension amounts on 20b. Then subtract the **retirement exclusions** (lines 28a to 28c) to reach **New Jersey gross income (line 29)**.
6. **Exemptions (line 30) and deductions (lines 31 to 37c)**: medical expenses above 2% of line 29, plus Archer MSA contributions and self-employed health insurance (line 31); court-ordered alimony paid (32, excluding child support); any proven eligible deduction on the later lines, including the separately computed Alternative Business Calculation Adjustment (35) and college affordability deductions (37a to 37c). Conservation (33), Health Enterprise Zone (34) and organ/bone-marrow (36) outcomes are held below. **Taxable income (line 39)** = line 29 minus line 38 ([2025 NJ-1040 instructions, page 23](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).
7. **Property tax deduction or credit (lines 40a, 41 and 56).** Compare the deduction with the credit on Worksheet H (or Schedule NJ-COJ and Worksheet I if claiming a credit for tax paid elsewhere) and claim only one. **New Jersey taxable income (line 42)** = line 39 minus any property tax deduction.
8. **Tax (line 43).** If line 42 is less than $100,000, use the Tax Table; at $100,000 or more, use the rate schedules ([2025 NJ-1040 instructions, page 31](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).
9. **Credit for taxes paid to other jurisdictions (line 44, Schedule NJ-COJ).** Then non-refundable credits (lines 46 to 49), use tax (line 51), interest on underpaid estimates (line 52, Form NJ-2210) and any shared responsibility payment (line 53c): test coverage for the tax year, filing threshold, dependents and exemptions on Schedule NJ-HCC; lack of coverage alone does not establish a payment. See pp.37–41 of the [2025 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).
10. **Payments and refundable credits (lines 55 to 65):** withholding, property tax credit, estimated and extension payments, NJEITC, excess UI/DI/FLI, Wounded Warrior Caregivers Credit, BAIT credit (line 63), Child and Dependent Care Credit, Child Tax Credit. Line 67 is tax due; line 68 is an overpayment.
11. **Nonresidents (Form NJ-1040NR)** ([2025 NJ-1040NR instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040nri.pdf)): report income from everywhere in column A and New Jersey-source income in column B. Compute taxable income and tax on column A, then multiply the tax by the income percentage (line 29 column B divided by line 29 column A, to four decimal places). On the 2025 nonresident return, below $100,000 of line 39 either the Tax Table or rate schedules may be used; at $100,000 or more the rate schedules are required. This differs from the resident instructions.

### Rates, bands and thresholds

Apply each amount only to the year stated; 2025 return line references do not establish 2026 form lines.

#### Tax rate schedules, 2025 and 2026 ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

Tax = taxable income × rate − subtraction. The decimal schedules below are those printed by the 2026 ES form and 2025 return; .014 means 1.4%.

**Table A: single, and married/civil union partner filing separately**

| Taxable income over | But not over | Rate | Subtract | Source |
| --- | --- | --- | --- | --- |
| $0 | $20,000 | .014 | $0 | [2026 NJ-1040-ES, page 3](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf) |
| $20,000 | $35,000 | .0175 | $70.00 | same |
| $35,000 | $40,000 | .035 | $682.50 | same |
| $40,000 | $75,000 | .05525 | $1,492.50 | same |
| $75,000 | $500,000 | .0637 | $2,126.25 | same |
| $500,000 | $1,000,000 | .0897 | $15,126.25 | same |
| $1,000,000 | and over | .1075 | $32,926.25 | same |

**Table B: married/civil union couple filing jointly, head of household, qualifying widow(er)/surviving civil union partner**

| Taxable income over | But not over | Rate | Subtract | Source |
| --- | --- | --- | --- | --- |
| $0 | $20,000 | .014 | $0 | [2026 NJ-1040-ES, page 3](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf) |
| $20,000 | $50,000 | .0175 | $70.00 | same |
| $50,000 | $70,000 | .0245 | $420.00 | same |
| $70,000 | $80,000 | .035 | $1,154.50 | same |
| $80,000 | $150,000 | .05525 | $2,775.00 | same |
| $150,000 | $500,000 | .0637 | $4,042.50 | same |
| $500,000 | $1,000,000 | .0897 | $17,042.50 | same |
| $1,000,000 | and over | .1075 | $34,842.50 | same |

#### Exemptions, 2025 and 2026 ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf))

New Jersey has no standard deduction. Exemptions are subtracted from New Jersey gross income.

| Exemption | Amount | Condition | Source |
| --- | --- | --- | --- |
| Taxpayer; spouse or civil union partner if filing jointly; or a registered domestic partner | $1,000 each | Domestic partner only if registered in New Jersey by 31 December and not filing a New Jersey return | [2026 NJ-1040-ES, p.2](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf); [2025 NJ-1040, pp.6–7](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Age 65 or older | $1,000 more each | Taxpayer and joint-filing spouse only, 65 or older on the last day of the year | same |
| Blind or disabled | $1,000 more each | Taxpayer and joint-filing spouse only, on the last day of the year | same |
| Veteran | $6,000 more each | Honorably discharged or released under honorable circumstances from active duty before the last day of the year; documentation needed the first time | same |
| Each dependent | $1,500 | Must qualify as a dependent for federal purposes, with a valid SSN, ITIN or ATIN | same |
| Dependent attending college | $1,000 more | Dependent under 22 on the last day of the year, full-time at an accredited school for some part of each of five calendar months, and the taxpayer paid at least half of tuition and maintenance | same |

#### Retirement income exclusions (2025 return mapping; ordinary statutory rules also used for 2026 estimates) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

Social Security, Railroad Retirement and U.S. military pensions are not taxable and are not entered as taxable income. First determine the New Jersey-taxable distribution, excluding previously taxed contributions under the appropriate recovery method; do not simply copy the federal taxable pension. The ordinary exclusions then apply to that taxable amount (2025 line 20a), and any qualifying unused exclusion to other income.

**Pension exclusion (2025 line 28a).** Allowed only if the taxpayer (or the spouse, if filing jointly) was **62 or older, or disabled as defined by Social Security guidelines** on the last day of the year, **and** total income on line 27 is **$150,000 or less**. On a joint return where only one spouse qualifies, only that spouse's pension counts. The exclusion is the lesser of line 20a and:

| Filing status | Line 27 is $0 to $100,000 | Over $100,000 through $125,000 | Over $125,000 through $150,000 | Source |
| --- | --- | --- | --- | --- |
| Married/civil union couple filing jointly | $100,000 | 50% of line 20a | 25% of line 20a | [54A:6-10(b)](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF) |
| Single, head of household, qualifying widow(er) | $75,000 | 37.5% of line 20a | 18.75% of line 20a | [54A:6-10(b)](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF) |
| Married/civil union partner filing separately | $50,000 | 25% of line 20a | 12.5% of line 20a | [54A:6-10(b)](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF) |

Above $150,000 of line 27 there is no **ordinary pension exclusion or unused ordinary exclusion**. Do not extend that ceiling to the separate Special Exclusion. The boundaries in law are **over $100,000 through $125,000**, then **over $125,000 through $150,000**; the whole-dollar labels in the return table must not leave a gap for cents. See [N.J.S.A. 54A:6-10 and 6-15](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF).

**Other retirement income exclusion (line 28b, Worksheet D).** Only for someone **62 or older** (disability alone does not qualify). Line 27 must be $150,000 or less, and wages plus business, partnership and S corporation income (lines 15, 18, 21 and 22) must be **not more than $3,000**. The unused part of the maximum exclusion (the same table, but as a percentage of line 27 in the two upper bands) can then be excluded. On a joint return where only one spouse is 62 or older, only that spouse's income counts.

**Special exclusion: HOLD.** The separate statutory provision is not subject to the ordinary $150,000 ceiling. Eligibility where Social Security or Railroad Retirement coverage will never be available, and the amount actually claimable, require a separate determination under [54A:6-15(b)](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF). Do not use the ordinary exclusion table to decide this outcome. Check this point with one of our partner accountants.

#### Deductions (2025) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- **Medical expenses:** unreimbursed expenses above 2% of line 29, plus qualified Archer MSA contributions and the self-employed health insurance deduction ([Division exemptions and deductions page](https://www.nj.gov/treasury/taxation/njit13.shtml): the self-employed deduction cannot exceed earned income from the business under which the plan was set up; a child's cover counts only if the child is a dependent). **No self-employed deduction is allowed for a month in which the taxpayer is eligible for a subsidized employer plan of the taxpayer or spouse** ([54A:3-5](https://pub.njleg.state.nj.us/Bills/9899/PL99/222_.PDF)); do not deduct the same premiums again as ordinary medical expenses.
- **Not deductible:** IRA and Keogh contributions, mortgage interest and employee business expenses ([Division exemptions and deductions page](https://www.nj.gov/treasury/taxation/njit13.shtml)).
- **College affordability:** gross income must be $200,000 or less. Deduct actual NJBEST contributions up to $10,000 (2025 line 37a), NJCLASS principal/interest paid up to $2,500 (37b), and tuition designated by an in-state higher-education institution for the taxpayer/spouse/dependent up to $10,000 (37c). Separate spouses cannot exceed the combined caps; part-year residents test whole-year income and prorate by resident months. See [54A:3-12 to 3-14](https://pub.njleg.state.nj.us/Bills/2020/PL21/128_.PDF) and [2025 instructions, pp.24–25](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).
- **Organ or bone marrow donation (line 36): HOLD.** The former $10,000 shorthand omitted expense, timing and combined-limit conditions. Do not use it as a deduction calculation. Check this point with one of our partner accountants.

#### Property tax deduction or credit (2025) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- **Eligibility (all needed):** domiciled in New Jersey and kept a main home there, as owner or tenant; the main home was subject to property tax, paid directly or through rent; income on line 29 is **more than** the filing threshold (seniors 65 or older and blind or disabled people at or below it may claim the credit on Form NJ-1040-HW); in a rented multi-unit building, access to kitchen and bath facilities; if the home is a unit in a property the person owned, no more than four units and no more than one commercial unit.
- **Not eligible:** a vacation or second home; a 100% disabled veteran exempt from property tax on the home; a homeowner paying PILOT (payments in lieu of tax); a tenant in a tax-exempt building.
- **Amount of property tax:** homeowners use the property tax due and paid on the main home for the year (their ownership share); tenants use **18% of rent** paid; mobile home owners in a park use 18% of site fees. Married filing separately while keeping the same main home: half.
- **Deduction:** up to **$15,000** ($7,500 for spouses filing separately who kept the same main home), subtracted on line 41.
- **Credit:** **$50** ($25 for those spouses), refundable, on line 56. Do not claim both deduction and credit. The qualifying senior/blind/disabled exception at or below the filing threshold described above remains available; use NJ-1040 or NJ-1040-HW, not both ([2025 instructions, pp.25 and 41](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).
- **Which one:** compare with the **$50** credit ($25 for those spouses), prorated for qualified resident months if part-year; use Worksheet H, or Worksheet I with Schedule NJ-COJ. Take the deduction when the comparison shows at least that credit amount in tax savings. For a taxpayer eligible for a Senior Freeze reimbursement, the homeowner deduction cannot exceed the base-year property tax liability ([54A:3A-17(g)](https://pub.njleg.state.nj.us/Bills/2024/PL24/88_.PDF)); interactions beyond this cap are held for a partner accountant.

#### New Jersey Earned Income Tax Credit and Child Tax Credit

**NJEITC (2025 line 58).** For a resident who claimed and was allowed federal EIC, the New Jersey credit is 40% of it; part-year residents prorate by resident months. The 2025 return's separate $260 rule for taxpayers without a qualifying child, civil-union computations, separated-spouse eligibility, and the 2026 year-specific calculation are **HOLD** outcomes here; do not infer eligibility from the 40% multiplier. Check this point with one of our partner accountants. See [2025 instructions, p.42](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).

**Child Tax Credit (2025 line 65).** A resident must be allowed the dependent deduction for a child **under age six at year-end** and have New Jersey taxable income **not over $80,000**. SSN or ITIN qualifies. A married taxpayer must file jointly, except a federal head-of-household or surviving-spouse filer. The credit is refundable; for part-year residents prorate by resident months divided by 12, counting 15 days or more as a month. The income test uses the whole year for a part-year resident. Law: [54A:4-17.1, P.L. 2026 c.26](https://pub.njleg.state.nj.us/Bills/2026/PL26/26_.PDF); dated form method: [2025 instructions, p.44](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).

| New Jersey taxable income | Credit per eligible child: 2025 | Credit per eligible child: 2026 | Source |
| --- | --- | --- | --- |
| $30,000 or less | $1,000 | $1,250 | [P.L. 2026 c.26, §1(a)](https://pub.njleg.state.nj.us/Bills/2026/PL26/26_.PDF) |
| Over $30,000, not over $40,000 | $800 | $1,000 | same |
| Over $40,000, not over $50,000 | $600 | $750 | same |
| Over $50,000, not over $60,000 | $400 | $500 | same |
| Over $60,000, not over $80,000 | $200 | $250 | same |

The increased schedule applies to **2026, 2027 and 2028**. The 2025 case below keeps its original year and credit.

#### Where New Jersey differs from federal law ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf); [Worksheet GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf))

| Item | New Jersey treatment |
| --- | --- |
| Starting point | Its own income categories, not federal AGI; wages from W-2 box 16 |
| 401(k) contributions | **Not taxed** when made: employer and employee 401(k) contributions up to the federal limit are excluded; the distributions are taxed later |
| Other retirement contributions (403(b), 457, SEP, federal Thrift Savings Plan) | Included in New Jersey wages when earned, so box 16 can exceed box 1 |
| IRA and Keogh contributions | Not deductible |
| Self-employed health insurance | Deductible, as part of line 31 |
| Self-employed 401(k) contributions | Deducted in Schedule NJ-BUS-1, up to the federal limits |
| Social Security, Railroad Retirement | Not taxable |
| Gain on qualified small business stock | For tax years beginning on or after 1 January 2026, exclude sale/exchange/other-disposition gains **only to the extent exempt federally under section 1202** ([54A:6-34](https://pub.njleg.gov/Bills/2024/PL25/67_.PDF)); 2026 reporting-line outcome held |
| Capital gains | Ordinary rates; losses only against gains in the same category, no carryover |
| Net operating losses | No carryback or carryforward; only the Alternative Business Calculation Adjustment |
| Section 179 | New Jersey maximum is **$25,000**; the federal reduced dollar limit applies using that $25,000; no business-income limit; unused amounts cannot be carried forward |
| Bonus depreciation | Worksheet GIT-DEP allows the federal 30% allowance and not the 50% allowance; the NJ-1040 instructions require an adjustment whenever the federal special bonus allowance or section 179 was deducted for assets placed in service from 1 January 2004 |
| Alimony | Court-ordered payments made are deducted (line 32) and payments received are income (line 25); the instructions set no agreement-date limit |
| New federal deductions from P.L. 119-21 (tips, overtime, car loan interest, seniors) and the QBI deduction | **HOLD:** no New Jersey deduction is authorized here merely because it exists federally. Check this point with one of our partner accountants. |

**Depreciation conditions.** Use [54A:5-1.2](https://pub.njleg.state.nj.us/Bills/2004/PL04/65_.PDF), which fixes the relevant federal depreciation rules at 31 December 2001 for covered post-2003 property, and the current [GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf). The worksheet's $25,000 section 179 ceiling is subject to the federal asset-cost reduction using that ceiling; there is no business-income limit or unused section 179 carryforward. Liberty Zone property, affordable-housing alternate depreciation, a missing initial adjustment, and federal 100% bonus assets need individual analysis: **HOLD — do not copy a federal deduction or infer a final New Jersey depreciation figure. Check this point with one of our partner accountants.**

#### Credit for taxes paid to other jurisdictions (Schedule NJ-COJ) ([GIT-3W](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git3w.pdf); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- Only for income taxed by both New Jersey and another U.S. state, its political subdivision or DC, in the same year. No credit for tax paid to the U.S. government, Puerto Rico or any other country or territory.
- The income must be **properly** taxed there: for a nonresident, generally services performed in that jurisdiction, business carried on there, real or tangible property located there, and gambling there. Interest, dividends and securities gains are generally not properly taxed by another state unless they come from a business there.
- Credit = the lesser of (a) New Jersey tax x (income taxed by both / New Jersey gross income, line 29, carried to seven decimal places) and (b) the tax actually paid to the other jurisdiction on that income. It is not dollar-for-dollar.
- **New York:** establish the income actually and properly taxed by both states. GIT-3W warns that **no single line** of the New York return necessarily represents it. Do not automatically equate the IT-203 state-amount column with the Schedule NJ-COJ numerator or use worldwide income. See [GIT-3W, pp.4–9](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git3w.pdf).
- **Pennsylvania:** under the reciprocal agreement, Pennsylvania does not tax New Jersey residents' employee compensation, so there is no credit for Pennsylvania tax on wages. Self-employment income and property gains taxed by Pennsylvania can qualify. Philadelphia wage tax and other Pennsylvania municipal taxes are outside the agreement and can qualify.
- New York convenience-of-the-employer days, dual residency, S corporation income allocated to New Jersey, foreign/PTE taxes and multiple state/city layers: **HOLD — no credit conclusion is supplied here. Check this point with one of our partner accountants.** [54A:4-1(c), (d) and (f)](https://pub.njleg.state.nj.us/Bills/2022/PL23/125_.PDF) must be considered before using the basic formula.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Single, gross income for the year exactly $10,000 | No filing requirement: it must be **more than** $10,000. File anyway to recover withholding or claim NJEITC | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Civilian not domiciled in New Jersey, permanent New Jersey home, exactly 183 days there | Not resident under this test: needs **more than** 183 days | [GIT-6](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf) |
| Domiciled in New Jersey, lived abroad all year with a permanent home there, no New Jersey home, 30 days in New Jersey | Nonresident: all three conditions met (30 days is not more than 30) | same |
| Joint filers, both 65, line 27 exactly $100,000, pension $60,000 | Band $0 to $100,000: pension exclusion $60,000; unused $40,000 may go on line 28b if earned income is not more than $3,000 | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Same couple, line 27 more than $150,000 | No ordinary pension or unused ordinary exclusion; the Special Exclusion is separately held | same |
| Age 61 and disabled | Pension exclusion can qualify only with Social Security-defined disability and the income/ownership tests; unused ordinary exclusion needs age 62 | [54A:6-10 and 6-15](https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF) |
| Taxable income exactly $80,000, dependent child aged 4, otherwise eligible | Child Tax Credit $200 for 2025; $250 for 2026; prorate for part-year residency | [P.L. 2026 c.26](https://pub.njleg.state.nj.us/Bills/2026/PL26/26_.PDF) |
| Taxable income more than $80,000 | No Child Tax Credit | same |
| Eligible full-year filer; property tax deduction saves less than $50 | Take the $50 credit instead (same-home separate spouses compare $25) | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Taxable income exactly $100,000 | Rate schedules must be used, not the tax table | same |
| Schedule C loss and wage income | Loss makes no entry on line 18 and does not reduce wages; see Schedule NJ-BUS-2 | same |
| Tax for the year after withholding and credits exactly $400 | No estimated payments required: they are required only if tax is **more than** $400 | [2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf) |
| Paid less than 80% of the tax by 15 April, filed by 15 October | Extension denied retroactively; penalties and interest from 15 April | [Form NJ-630](https://www.nj.gov/treasury/taxation/pdf/current/630.pdf) |

## Worked cases

Rates from the [2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf); method from the [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf).

These are assumed cases, with their original years and numeric inputs. Unless stated otherwise, assume full-year New Jersey residence, the eligibility for the listed exemptions/deductions/credits, no additional income or relief, and no special held regime. Case 1 assumes a qualifying taxable main-home rental and no Senior Freeze reimbursement; Case 6 assumes the child qualifies as a dependent and the taxpayer has a valid SSN or ITIN. The 2025 resident return uses the Tax Table below $100,000 of line 42; Cases 2 and 6 show that result separately from schedule arithmetic.

**Case 1, a decision: property tax deduction or credit? Single sole proprietor who rents, 2026.** Schedule C profit $130,000, no New Jersey adjustments; self-employed health insurance $8,000 (assumed paid for eligible months, within plan-business earned income, with no taxpayer/spouse subsidized-employer-plan eligibility); one $1,000 exemption; rent paid on the main home $30,000; no withholding. Line 29: $130,000. Taxable income (line 39): $130,000 - $1,000 - $8,000 = $121,000. Property tax: 18% of $30,000 = $5,400. Worksheet H: with the deduction, taxable income is $115,600 and the tax is $115,600 x 6.37% - $2,126.25 = $5,237.47; without it, $121,000 x 6.37% - $2,126.25 = $5,581.45. The deduction saves $343.98, which is $50 or more, so take the deduction. **Tax: $5,237.47.** Estimated tax is required (more than $400); using the full-year estimate worksheet, the first three installments are $1,309.37 and the last $1,309.36 (cent rounding), due 15 April, 15 June, 15 September 2026 and 15 January 2027.

```oa-check
name: NJ 2026 single, property tax deduction against the 50 dollar credit
inputs:
  taxable_income_line39: 121000
  rent_paid: 30000
steps:
  - property_tax: rent_paid * 0.18
  - deduction_used: min(property_tax, 15000)
  - tax_with_deduction: (taxable_income_line39 - deduction_used) * 0.0637 - 2126.25
  - tax_without: taxable_income_line39 * 0.0637 - 2126.25
  - saving: tax_without - tax_with_deduction
  - tax_if_credit: tax_without - 50
  - installment: round(tax_with_deduction / 4, 2)
  - final_installment: tax_with_deduction - 3 * installment
expected:
  property_tax: 5400.00
  tax_with_deduction: 5237.47
  tax_without: 5581.45
  saving: 343.98
  tax_if_credit: 5531.45
  installment: 1309.37
  final_installment: 1309.36
```

The deduction wins by $293.98 over the credit.

**Case 2: retired couple, 2025.** Married filing jointly, both 67. Pension $60,000 (line 20a), interest $30,000, dividends $20,000, Social Security (not entered). Line 27 = $110,000, in the over-$100,000-through-$125,000 band. Pension exclusion: lesser of $60,000 and 50% of $60,000 = $30,000. Worksheet D: maximum 50% of $110,000 = $55,000; unused $25,000; no wages or business income, so line 28b is $25,000. Line 29 = $110,000 - $55,000 = $55,000. Exemptions: $1,000 x 2 plus $1,000 x 2 for age = $4,000. Taxable income $51,000 (no property tax benefit in this example). Table B: $51,000 x 2.45% - $420 = $829.50; the Tax Table (required below $100,000) gives **$830**.

**Case 3: losses stay in their category, 2026.** Single. Wages (box 16) $70,000; Schedule C loss $20,000; stock gains $5,000 and stock losses $12,000; rental profit $6,000. Line 15: $70,000. Line 18: no entry (loss). Line 19: net loss of $7,000, so no entry, and it is not carried forward. Line 23: $6,000. **Line 27: $76,000.** Any alternative business adjustment must be computed separately on Schedule NJ-BUS-2 (line 35); $76,000 is total income before that adjustment, not a final taxable-income or liability result.

**Case 4: New York commuter, 2025.** Single New Jersey resident who works every day in a New York office. Wages $200,000 (all taxed by New York), bank interest $10,000; lives rent-free with family, so no property tax benefit. Line 29: $210,000. Taxable income: $209,000. Tax: $209,000 x 6.37% - $2,126.25 = $11,187.05. Assume the full $200,000 is actually and properly included in the credit numerator after reconciling both states' treatment, and $12,000 is the final New York tax on that income after credits, not withholding. These are case assumptions, not an IT-203 line shortcut. Credit limit: $11,187.05 x ($200,000 / $210,000) = $10,654.33, which is less than $12,000, so the **credit is $10,654.33** and New Jersey tax after the credit is **$532.72**.

```oa-check
name: NJ resident working in New York, Schedule NJ-COJ credit (2025 and 2026 rates)
inputs:
  nj_gross_income: 210000
  income_taxed_by_both: 200000
  ny_tax_paid: 12000
steps:
  - taxable_income: nj_gross_income - 1000
  - nj_tax: taxable_income * 0.0637 - 2126.25
  - credit_limit: round(nj_tax * income_taxed_by_both / nj_gross_income, 2)
  - credit: min(credit_limit, ny_tax_paid)
  - nj_tax_after_credit: nj_tax - credit
expected:
  nj_tax: 11187.05
  credit: 10654.33
  nj_tax_after_credit: 532.72
```

**Case 5: section 179 over the New Jersey cap, 2026.** A sole proprietor buys $80,000 of equipment and deducts all of it under federal section 179. For ordinary qualifying property, assuming no asset-cost phaseout, Liberty Zone or affordable-housing exception, no federal bonus allowance and a correctly made initial adjustment, $25,000 is allowed as New Jersey section 179; the other $55,000 becomes New Jersey depreciable basis, recovered through regular depreciation on Worksheet GIT-DEP. First-year New Jersey adjustment (added to Schedule NJ-BUS-1): $80,000 - $25,000 - first-year New Jersey depreciation on $55,000. No final first-year adjustment is supplied without the asset class, placed-in-service date and depreciation convention. Later-year and disposal adjustments must be recomputed from the actual New Jersey basis. **HOLD — this case does not authorize a final depreciation deduction. Check this point with one of our partner accountants.**

**Case 6: working parent, 2025.** Head of household, one child aged 3, New Jersey taxable income $35,000, federal EIC claimed and allowed $4,000 (assumed), New Jersey withholding $600. Tax (Table B): $35,000 x 1.75% - $70 = $542.50. NJEITC: 40% x $4,000 = $1,600. Child Tax Credit (over $30,000, not over $40,000): $800. Payments and refundable credits: $600 + $1,600 + $800 = $3,000. Refund on the schedule figure: $2,457.50. The Tax Table (required below $100,000) gives tax of $543, so the **refund on the return is $2,457**.

**Case 7: extension that fails the 80% test, 2025 return.** Tax liability $10,000 (line 45). Paid by 15 April 2026: $7,500, below 80% ($8,000). The extension is denied, and penalties and interest run from 15 April 2026 even if the return is filed by 15 October. Filed 30 September 2026 with $2,500 still due: late filing penalty 5% per month or part month, capped at 25%, is $625; a $100 penalty may also be charged for each month the return is late; late payment penalty 5% is $125; plus interest at 3% above prime.

**Case 8: nonresident with New Jersey rent, 2025 (Form NJ-1040NR).** Single, income from everywhere $200,000, of which New Jersey rental income $50,000 (net income after allowable expenses). Income percentage: $50,000 / $200,000 = 25%. Taxable income (column A, after the $1,000 exemption): $199,000. Tax on it: $199,000 x 6.37% - $2,126.25 = $10,550.05. **New Jersey tax: 25% x $10,550.05 = $2,637.51.**

## When to refuse or refer

These are **non-usable holds**, not suggested tax results. For each point: **Check this point with one of our partner accountants.**

- Military/spouse residence elections; disputed domicile or day counts; part-year calculations beyond the dated worksheets.
- Special retirement exclusion; New York convenience wages, dual residents and multi-jurisdiction or PTE credits.
- Federal 100% bonus, older depreciation regimes, missing initial adjustments, Liberty Zone or affordable-housing rules, asset dispositions and partnership/S corporation basis differences; Case 5 retains its inputs but holds the final depreciation.
- BAIT entity election/computation and Corporation Business Tax (separate Guide **nj-cbt-and-bait**); individual BAIT amounts must come from the relevant K-1, not an assumed credit.
- Complex NJ-BUS-2 carryforwards; Health Enterprise Zones, qualified conservation contributions, organ/bone-marrow deductions, cannabis adjustments and Senior Freeze interactions beyond the stated cap.
- Special NJEITC cases and 2026-specific eligibility; child/dependent-care, excess UI/DI/FLI, Wounded Warrior and other special credits; use tax and shared-responsibility payment calculations beyond the dated instructions.
- Trusts/estates/grantor trusts, inheritance tax, amended returns, refunds outside an ordinary timely return, notices, audits, waivers and appeals; historical local-income-tax assertions and federal comparison amounts are not usable state-tax guidance.

Refuse requests to hide income, invent expenses or misstate residence.

## Filing and payment

Sources: [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf), [Form NJ-630](https://www.nj.gov/treasury/taxation/pdf/current/630.pdf), [GIT-8](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git8.pdf).

**2026 returns.** Due 15 April 2027 for calendar-year filers (the return is due when the federal return is due). This is the ordinary statutory calendar-year date under [54A:8-1](https://pub.njleg.state.nj.us/Bills/2004/PL05/297_.HTM), before any specific relief. Final 2026 return line mapping and extension form directions are held until the year-specific instructions are read; the next paragraph remains explicitly 2025.

**2025 returns (dated section).**

- Due **15 April 2026** for calendar-year filers; fiscal-year filers by the 15th day of the fourth month after the year ends. A return postmarked by the due date is on time.
- **Extension to 15 October 2026** (six months) is to **file**, not to pay, and only if **at least 80%** of the tax liability calculated on the return was paid by 15 April 2026 through withholding, estimated payments or a payment with the extension. Then either file Form NJ-630 (or online) by 15 April 2026, or, with a federal extension, fill in the federal-extension oval and enclose a copy of the federal extension if it was filed on paper. Form NJ-630 is still needed with a federal extension if a payment is required to reach 80%. If the 80% test fails or the return is late, the extension is denied and penalties and interest run from the original due date.

**2026 estimated tax** ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf)).

- Required if the tax expected for 2026, after withholding and credits, is **more than $400**. Not required if gross income will be at or below the filing threshold.
- Pay in full by 15 April 2026 or in four equal installments by 15 April, 15 June, 15 September 2026 and 15 January 2027. The ES instructions state an early-filing exception using 15 February 2027. The holiday-adjusted operative deadline for that exception is **HOLD** here; keep the 15 January installment unless confirmed. Check this point with one of our partner accountants.
- Farmers with at least two-thirds of estimated income from farming may pay the whole amount by 15 January 2027.
- **Interest on underpayment (Forms NJ-2210 / NJ-2210NR).** Do not decide this solely from the annual balance: installment timing matters. [54A:9-6(c)](https://pub.njleg.state.nj.us/Bills/2004/PL05/288_.PDF) uses the lesser of the installments based on 80% of current tax (two-thirds for qualifying farmers) and 100% of the prior return's tax. Its separate subsection (d) exceptions include prior-year return/facts and annualization tests; the prior-year exception requires a liability return covering 12 months and subsection (d)(3) substitutes 110% for 100% in (d)(1)(A)/(B) above prior-year taxable gross income of $150,000 ($75,000 married separately). GIT-8's blanket 100% summary omits that distinction. **HOLD — do not select an exception or conclude no interest without reconciling the applicable statutory route and payment dates. Check this point with one of our partner accountants.**

**Penalties and interest** ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).

- Late filing: 5% per month or part month, up to 25% of the outstanding tax, plus a possible $100 per month.
- Late payment: 5% of the outstanding balance.
- Interest: 3% above the prime rate, for each month or part month unpaid; unpaid tax, penalty and interest are added to the balance at the end of each calendar year.

**Paying.** E-check or credit card online, or check with Form NJ-1040-V payable to "State of New Jersey – TGI". Special refund limitation periods are held for a partner accountant; no universal three-year deadline is supplied here.

## Completion checklist

- [ ] Preserve the tax year, residency periods and evidence for each income category.
- [ ] Reconcile federal-to-state adjustments, deductions and credit eligibility before arithmetic.
- [ ] Use the 2026 enacted Child Tax Credit table only for its stated years; keep all 2025 cases dated.
- [ ] Resolve every applicable hold before a filing result is used; save the return, worksheets and payment confirmations.

## Sources

| Source | URL | Read on |
|---|---|---|
| 2026 Form NJ-1040-ES instructions, pp.1–4 read: thresholds, dates, exemptions, worksheet and both rate schedules | https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf | 2026-11-27 |
| 2025 NJ-1040 instructions: pp.3–8, 16–31, 37–44 and 46–47 read for form choice, income, deductions, exclusions, credits, filing and penalties; tax-table case rows checked | https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf | 2026-11-27 |
| 2025 NJ-1040NR, residency/form chart and pp.25–26 read: both columns, income percentage and tax methods | https://www.nj.gov/treasury/taxation/pdf/current/1040nri.pdf | 2026-11-27 |
| GIT-DEP revised 10/25, general instructions and Part I read; 179 ceiling, depreciation, initial-adjustment and exception conditions | https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf | 2026-11-27 |
| GIT-6, Part-Year Residents and Nonresidents; read for domicile, 30-day and 183-day tests | https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf | 2026-11-27 |
| GIT-3W (January 2026), pp.3–10 read for actual/properly taxed income, credit formula, New York warning and Pennsylvania | https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git3w.pdf | 2026-11-27 |
| GIT-8 (January 2026), pp.2–3 and 10–12 read; its 100% summary is not substituted for 54A:9-6(d)(3) | https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git8.pdf | 2026-11-27 |
| Division Child Tax Credit page (last updated 07/15/26; shows tax year 2025); read for the figures cited from it | https://www.nj.gov/treasury/taxation/individuals/childtaxcredit.shtml | 2026-11-27 |
| Division exemptions and deductions page; read for self-employed health insurance, items not deductible | https://www.nj.gov/treasury/taxation/njit13.shtml | 2026-11-27 |
| Form NJ-630, both pages read: 2025 extension conditions, deadlines and penalty rules | https://www.nj.gov/treasury/taxation/pdf/current/630.pdf | 2026-11-27 |
| Division new laws page; read for P.L. 2025, c.67 small business stock exclusion from 2026 | https://www.nj.gov/treasury/taxation/newlegislation.shtml | 2026-11-27 |

| N.J.S.A. 54A:2-1(a)(7), (b)(7), enacted rate schedules; operative 2020 bands read and reconciled to ES | https://pub.njleg.state.nj.us/Bills/2020/AL20/94_.HTM | 2026-11-27 |
| N.J.S.A. 54A:2-4 and 8-3.1, filing thresholds/status exceptions, §§1–2 read | https://pub.njleg.state.nj.us/Bills/9899/PL99/260_.PDF | 2026-11-27 |
| 54A:6-10 and 6-15, retirement boundaries and separate Special Exclusion; operative portions read | https://pub.njleg.state.nj.us/Bills/2020/PL21/129_.PDF | 2026-11-27 |
| 54A:3-3 and 3-5, medical and self-employed insurance limits, §§1–2 read | https://pub.njleg.state.nj.us/Bills/9899/PL99/222_.PDF | 2026-11-27 |
| College Affordability Act, §§3–5 and 8 read for income caps, qualifying payments and effective date | https://pub.njleg.state.nj.us/Bills/2020/PL21/128_.PDF | 2026-11-27 |
| 54A:3A-16 and 3A-20 definitions and credit, 1996 Act §§2 and 6 read; old deduction cap superseded | https://pub.njleg.state.nj.us/Bills/9697/PL96/60_.PDF | 2026-11-27 |
| 54A:3A-17, 2024 Act §22 read: current homeowner cap, ownership shares, reimbursement cap; §23 read for mixed homes | https://pub.njleg.state.nj.us/Bills/2024/PL24/88_.PDF | 2026-11-27 |
| 54A:4-17.1, entire 2026 child-credit law read, including effective years and eligibility | https://pub.njleg.state.nj.us/Bills/2026/PL26/26_.PDF | 2026-11-27 |
| 54A:6-34, entire qualified-small-business-stock exclusion law read | https://pub.njleg.gov/Bills/2024/PL25/67_.PDF | 2026-11-27 |
| 54A:3-9, entire alternative business calculation law read | https://pub.njleg.state.nj.us/Bills/2010/PL11/60_.PDF | 2026-11-27 |
| 54A:5-1.2, 2004 Act §26 read: fixed-date federal depreciation/section 179 rules | https://pub.njleg.state.nj.us/Bills/2004/PL04/65_.PDF | 2026-11-27 |
| 54A:4-1 and 5-8, 2023 Act §§1–2 read for credit limits and source-income conditions | https://pub.njleg.state.nj.us/Bills/2022/PL23/125_.PDF | 2026-11-27 |
| 54A:9-6, 2005 Act §3(c)–(d) read for installment tests and high-income exception | https://pub.njleg.state.nj.us/Bills/2004/PL05/288_.PDF | 2026-11-27 |
| 54A:8-1, ordinary due-date provision read | https://pub.njleg.state.nj.us/Bills/2004/PL05/297_.HTM | 2026-11-27 |

Not yet confirmed: final 2026 resident/nonresident forms, line numbers and tax tables; 2026-specific NJEITC outcomes; holiday-adjusted early-filing exception; final depreciation in Case 5 and special depreciation/basis regimes; Special Exclusion eligibility; federal tips/overtime/car-loan/senior/QBI deductions' New Jersey effect; and the other expressly held rare outcomes above. **Each is non-usable until resolved. Check this point with one of our partner accountants.**
