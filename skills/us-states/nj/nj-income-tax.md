---
name: nj-income-tax
description: Use this skill whenever asked about New Jersey individual income tax for self-employed / sole proprietors. Trigger on phrases like "New Jersey income tax", "NJ income tax", "Form NJ-1040", "NJ Division of Taxation", "NJ self-employment tax".
version: "0.1"
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Jersey gross income tax (Forms NJ-1040 and NJ-1040NR), including sole proprietors

## Scope and who this is for ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

This Guide covers the New Jersey gross income tax for individuals: the resident return, **Form NJ-1040**, and the nonresident return, **Form NJ-1040NR**. The primary year is **tax year 2026** (returns filed in 2027). A dated section covers **2025 returns** (due 15 April 2026, or 15 October 2026 on a valid extension). It is written for employees, retirees, sole proprietors and owners of a single-member LLC disregarded for federal tax.

The 2026 Form NJ-1040 instructions were not published when this Guide was written (25 September 2026). The Division of Taxation's 2026 Form NJ-1040-ES ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf)) prints the same rate schedules and exemption amounts as 2025, and says the retirement exclusions "only apply for taxpayers with income up to $150,000". Where a figure comes only from the 2025 instructions, it is labelled 2025.

**Who is a resident** ([GIT-6, Part-Year Residents and Nonresidents](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf)):

- **Domiciled in New Jersey:** a resident, unless all three are true: no permanent home in New Jersey, a permanent home outside New Jersey, and not more than 30 days spent in New Jersey.
- **Not domiciled in New Jersey:** a resident only if the person maintains a permanent home in New Jersey **and** spends more than 183 days there. Both are needed.
- A home kept only for a temporary purpose (for example a temporary job assignment) is not permanent. A vacation home is not a permanent home.
- There is no part-year return. A part-year resident files Form NJ-1040 for the resident period and, if they had New Jersey-source income while a nonresident, Form NJ-1040NR too.

**Who must file** ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)). A return is required if gross income from everywhere, for the entire year, was **more than** $10,000 (single, or married/civil union partner filing separately) or $20,000 (married/civil union couple filing jointly, head of household, qualifying widow(er)/surviving civil union partner). File anyway to get a refund of New Jersey withholding or estimated tax, or to claim the New Jersey Earned Income Tax Credit or another credit that gives a refund.

**Not covered** (see "When to refuse or refer"): trusts and estates (Form NJ-1041), amended returns (Form NJ-1040X), the entity side of the Pass-Through Business Alternative Income Tax (BAIT) and the Corporation Business Tax, which are in the separate Guide **nj-cbt-and-bait**, and New Jersey inheritance tax.

## Ask the client first

- Which tax year? For 2026, rates and exemptions are unchanged from 2025; the 2026 Child Tax Credit table was not yet published.
- Domicile, any New Jersey home, any home outside New Jersey, and days spent in New Jersey. Did the person move in or out during the year?
- Filing status. It generally must match the federal status. A married couple who file jointly federally must file jointly in New Jersey.
- Every income item, sorted by type: W-2 **box 16 state wages** (not box 1), interest, dividends, Schedule C profit or loss, sales of property, pensions and IRA withdrawals, partnership and S corporation shares (Schedules NJK-1 / NJ-K-1), rents, gambling, alimony received.
- Ages on 31 December (62 for the retirement exclusions, 65 for the extra exemption), blindness or disability, veteran status with discharge papers, and dependents (children age 5 or younger; full-time students under 22).
- For the business: any federal **section 179** deduction or **bonus depreciation** this year or in earlier years (a New Jersey adjustment is needed); self-employed health insurance paid; any self-employed 401(k) contributions.
- Main home in New Jersey: owned (property tax paid) or rented (rent paid), shared ownership, and whether the building is tax-exempt.
- Income taxed by another state or city (for example New York wages or Philadelphia wage tax), with that return.
- Federal earned income credit claimed and allowed.
- New Jersey withholding, estimated payments (dates and amounts), the prior-year New Jersey tax, and any extension payment.
- Health coverage for everyone in the household when the return is filed.

## The method, step by step

Form NJ-1040 line numbers are from the 2025 return ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).

1. **Choose the form.** Resident all year: Form NJ-1040. Nonresident with New Jersey-source income: Form NJ-1040NR. Moved in or out: both, as described in Scope. Part-year residents: prorate exemptions (line 13) and the property tax deduction or credit by months of residence (15 days or more is a month). Deductions such as medical expenses and alimony count only amounts paid while a resident. The pension exclusion maximum is prorated by months only if income for the whole year is $100,000 or less, and is not prorated above that; whole-year income must be $150,000 or less (Worksheet E for the other retirement income exclusion).
2. **Do not start from federal AGI.** New Jersey taxes gross income in separate categories, each on its own line: wages (line 15, from W-2 box 16), taxable interest (16a), dividends (17), net profits from business (18, Schedule NJ-BUS-1 Part I), net gains from disposition of property (19, Schedule NJ-DOP), taxable pensions, annuities and IRA withdrawals (20a), partnership income (21), S corporation income (22), rents, royalties, patents and copyrights (23), net gambling winnings (24), alimony received (25) and other income (26). Residents report income from everywhere.
3. **Net losses only inside a category.** A loss can reduce gains in the **same** category only. A net loss in a category is not entered at all (no negative number, no zero), cannot reduce any other category, and cannot be carried back or forward. Example: a Schedule C loss cannot reduce wages; a stock loss cannot reduce rental income. The one relief is the Alternative Business Calculation Adjustment on line 35 (Schedule NJ-BUS-2), available if Schedule NJ-BUS-1 shows a loss in any part, or a loss carryforward exists from an earlier year; unused losses tracked there can be carried forward for up to 20 years.
4. **Business profit (Schedule NJ-BUS-1 Part I).** Start from federal Schedule C (or F) and adjust: add back taxes based on income; take out interest exempt for New Jersey; add other states' bond interest; deduct ordinary business meal and entertainment expenses that were not allowed on the federal return; deduct qualified contributions to a self-employed 401(k) plan (not above the federal limits); add interest and dividends derived in the conduct of the business; add or subtract business income or losses from rentals, royalties, patents or copyrights, and gains or losses on disposing of the business's property; add or subtract the depreciation adjustment from Worksheet GIT-DEP (cannabis licensees have one more adjustment). Otherwise the Schedule C figures, including depreciation as adjusted and a home office deduction, carry over. The federal deduction for half of self-employment tax is not a Schedule C expense, so it does not reduce New Jersey income.
5. **Total income (line 27)** = lines 15 through 26, leaving out the tax-exempt interest on 16b and the excludable pension amounts on 20b. Then subtract the **retirement exclusions** (lines 28a to 28c) to reach **New Jersey gross income (line 29)**.
6. **Exemptions (line 30) and deductions (lines 31 to 37c)**: medical expenses above 2% of line 29, plus Archer MSA contributions and self-employed health insurance (line 31); court-ordered alimony paid (32); qualified conservation contributions (33); Health Enterprise Zone deduction (34); Alternative Business Calculation Adjustment (35); organ or bone marrow donation (36); college affordability deductions (37a to 37c). **Taxable income (line 39)** = line 29 minus line 38 ([2025 NJ-1040 instructions, page 23](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).
7. **Property tax deduction or credit (lines 40a, 41 and 56).** Compare the deduction with the credit on Worksheet H (or Schedule NJ-COJ and Worksheet I if claiming a credit for tax paid elsewhere) and claim only one. **New Jersey taxable income (line 42)** = line 39 minus any property tax deduction.
8. **Tax (line 43).** If line 42 is less than $100,000, use the Tax Table; at $100,000 or more, use the rate schedules ([2025 NJ-1040 instructions, page 31](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).
9. **Credit for taxes paid to other jurisdictions (line 44, Schedule NJ-COJ).** Then non-refundable credits (lines 46 to 49), use tax (line 51), interest on underpaid estimates (line 52, Form NJ-2210) and the shared responsibility payment for anyone without health coverage (line 53c).
10. **Payments and refundable credits (lines 55 to 65):** withholding, property tax credit, estimated and extension payments, NJEITC, excess UI/DI/FLI, Wounded Warrior Caregivers Credit, BAIT credit (line 63), Child and Dependent Care Credit, Child Tax Credit. Line 67 is tax due; line 68 is an overpayment.
11. **Nonresidents (Form NJ-1040NR)** ([2025 NJ-1040NR instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040nri.pdf)): report income from everywhere in column A and New Jersey-source income in column B. Compute taxable income and tax on column A, then multiply the tax by the income percentage (line 29 column B divided by line 29 column A, to four decimal places).

## Rates, thresholds and figures by year

### Tax rate schedules, 2025 and 2026 ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

Tax = taxable income (line 42) x rate, minus the subtraction amount for the band. The 2026 Form NJ-1040-ES prints the same two tables as the 2025 instructions.

**Table A: single, and married/civil union partner filing separately**

| Taxable income over | But not over | Rate | Subtract |
| --- | --- | --- | --- |
| $0 | $20,000 | 1.4% | $0 |
| $20,000 | $35,000 | 1.75% | $70.00 |
| $35,000 | $40,000 | 3.5% | $682.50 |
| $40,000 | $75,000 | 5.525% | $1,492.50 |
| $75,000 | $500,000 | 6.37% | $2,126.25 |
| $500,000 | $1,000,000 | 8.97% | $15,126.25 |
| $1,000,000 | and over | 10.75% | $32,926.25 |

**Table B: married/civil union couple filing jointly, head of household, qualifying widow(er)/surviving civil union partner**

| Taxable income over | But not over | Rate | Subtract |
| --- | --- | --- | --- |
| $0 | $20,000 | 1.4% | $0 |
| $20,000 | $50,000 | 1.75% | $70.00 |
| $50,000 | $70,000 | 2.45% | $420.00 |
| $70,000 | $80,000 | 3.5% | $1,154.50 |
| $80,000 | $150,000 | 5.525% | $2,775.00 |
| $150,000 | $500,000 | 6.37% | $4,042.50 |
| $500,000 | $1,000,000 | 8.97% | $17,042.50 |
| $1,000,000 | and over | 10.75% | $34,842.50 |

### Exemptions, 2025 and 2026 ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf))

New Jersey has no standard deduction. Exemptions are subtracted from New Jersey gross income.

| Exemption | Amount | Condition |
| --- | --- | --- |
| Taxpayer; spouse or civil union partner if filing jointly; or a registered domestic partner | $1,000 each | Domestic partner only if registered in New Jersey by 31 December and not filing a New Jersey return |
| Age 65 or older | $1,000 more each | Taxpayer and joint-filing spouse only, 65 or older on the last day of the year |
| Blind or disabled | $1,000 more each | Taxpayer and joint-filing spouse only, on the last day of the year |
| Veteran | $6,000 more each | Honorably discharged or released under honorable circumstances from active duty before the last day of the year; documentation needed the first time |
| Each dependent | $1,500 | Must qualify as a dependent for federal purposes, with a valid SSN, ITIN or ATIN |
| Dependent attending college | $1,000 more | Dependent under 22 on the last day of the year, full-time at an accredited school for some part of each of five calendar months, and the taxpayer paid at least half of tuition and maintenance |

### Retirement income exclusions (2025; the same $150,000 limit for 2026) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

Social Security, Railroad Retirement and U.S. military pensions are not taxable at all and are never entered. The exclusions below apply to taxable pensions, annuities and IRA withdrawals (line 20a) and, if unused, to other income.

**Pension exclusion (line 28a).** Allowed only if the taxpayer (or the spouse, if filing jointly) was **62 or older, or blind or disabled** under Social Security guidelines on the last day of the year, **and** total income on line 27 is **$150,000 or less**. On a joint return where only one spouse qualifies, only that spouse's pension counts. The exclusion is the lesser of line 20a and:

| Filing status | Line 27 is $0 to $100,000 | $100,001 to $125,000 | $125,001 to $150,000 |
| --- | --- | --- | --- |
| Married/civil union couple filing jointly | $100,000 | 50% of line 20a | 25% of line 20a |
| Single, head of household, qualifying widow(er) | $75,000 | 37.5% of line 20a | 18.75% of line 20a |
| Married/civil union partner filing separately | $50,000 | 25% of line 20a | 12.5% of line 20a |

Above $150,000 of line 27 there is no exclusion at all: this is a cliff, not a phase-out.

**Other retirement income exclusion (line 28b, Worksheet D).** Only for someone **62 or older** (disability alone does not qualify). Line 27 must be $150,000 or less, and wages plus business, partnership and S corporation income (lines 15, 18, 21 and 22) must be **not more than $3,000**. The unused part of the maximum exclusion (the same table, but as a percentage of line 27 in the two upper bands) can then be excluded. On a joint return where only one spouse is 62 or older, only that spouse's income counts.

**Special exclusion.** $6,000 (joint, head of household, qualifying widow(er)) or $3,000 (single, married filing separately) for someone who will **never** be able to receive Social Security or Railroad Retirement benefits because their employer did not take part in either programme. Do not claim it if either spouse will ever be eligible.

### Deductions (2025) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- **Medical expenses:** unreimbursed expenses above 2% of line 29, plus qualified Archer MSA contributions and the self-employed health insurance deduction ([Division exemptions and deductions page](https://www.nj.gov/treasury/taxation/njit13.shtml): the self-employed deduction cannot exceed earned income from the business under which the plan was set up; a child's cover counts only if the child is a dependent).
- **Not deductible:** IRA and Keogh contributions, mortgage interest, employee business expenses, moving expenses ([Division exemptions and deductions page](https://www.nj.gov/treasury/taxation/njit13.shtml)).
- **College affordability (only if gross income was $200,000 or less):** NJBEST contributions up to $10,000 (37a), NJCLASS loan payments up to $2,500 (37b), tuition at a New Jersey institution up to $10,000 (37c).
- **Organ or bone marrow donation:** up to $10,000 of unreimbursed expenses (line 36).

### Property tax deduction or credit (2025) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- **Eligibility (all needed):** domiciled in New Jersey and kept a main home there, as owner or tenant; the main home was subject to property tax, paid directly or through rent; income on line 29 is **more than** the filing threshold (seniors 65 or older and blind or disabled people at or below it may claim the credit on Form NJ-1040-HW); in a rented multi-unit building, access to kitchen and bath facilities; if the home is a unit in a property the person owned, no more than four units and no more than one commercial unit.
- **Not eligible:** a vacation or second home; a 100% disabled veteran exempt from property tax on the home; a homeowner paying PILOT (payments in lieu of tax); a tenant in a tax-exempt building.
- **Amount of property tax:** homeowners use the property tax due and paid on the main home for the year (their ownership share); tenants use **18% of rent** paid; mobile home owners in a park use 18% of site fees. Married filing separately while keeping the same main home: half.
- **Deduction:** up to **$15,000** ($7,500 for spouses filing separately who kept the same main home), subtracted on line 41.
- **Credit:** **$50** ($25 for those spouses), refundable, on line 56. Not allowed if the deduction is claimed or income is under the filing threshold.
- **Which one:** take the deduction if it lowers tax by **$50 or more** ($25 for those spouses); otherwise take the credit (Worksheet H, or Worksheet I with Schedule NJ-COJ). Senior Freeze applicants may have to use their base-year amount.

### New Jersey Earned Income Tax Credit and Child Tax Credit (2025; 2026 amounts not yet published) ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf); [Division Child Tax Credit page](https://www.nj.gov/treasury/taxation/individuals/childtaxcredit.shtml))

- **NJEITC (line 58):** 40% of the federal earned income credit claimed **and allowed**. It can give a refund. Part-year residents prorate. A person with no qualifying child who was at least 18, met every federal EIC rule except the age rule and is not listed as someone else's dependent enters $260 (prorated for part-year residents). Married filing separately qualifies only with a qualifying child who lived with the taxpayer for more than half the year **and** living apart from the spouse for the last six months of the year.
- **Child Tax Credit (line 65):** only if taxable income (line 42) is **$80,000 or less**, for each dependent **age 5 or younger** on the last day of the year. Not available when married filing separately. The taxpayer needs a valid SSN or ITIN and must be allowed to claim the child as a dependent for federal purposes. Part-year residents prorate by months.

| New Jersey taxable income (line 42) | Credit per child (2025) |
| --- | --- |
| $30,000 or less | $1,000 |
| Over $30,000, not over $40,000 | $800 |
| Over $40,000, not over $50,000 | $600 |
| Over $50,000, not over $60,000 | $400 |
| Over $60,000, not over $80,000 | $200 |

The Division's page, updated 15 July 2026, still shows 2025 as the latest year; check it for 2026 amounts before filing a 2026 return.

### Where New Jersey differs from federal law ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf); [Worksheet GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf))

| Item | New Jersey treatment |
| --- | --- |
| Starting point | Its own income categories, not federal AGI; wages from W-2 box 16 |
| 401(k) contributions | **Not taxed** when made: employer and employee 401(k) contributions up to the federal limit are excluded; the distributions are taxed later |
| Other retirement contributions (403(b), 457, SEP, federal Thrift Savings Plan) | Included in New Jersey wages when earned, so box 16 can exceed box 1 |
| IRA and Keogh contributions | Not deductible |
| Self-employed health insurance | Deductible, as part of line 31 |
| Self-employed 401(k) contributions | Deducted in Schedule NJ-BUS-1, up to the federal limits |
| Social Security, Railroad Retirement | Not taxable |
| Capital gains | Ordinary rates; losses only against gains in the same category, no carryover |
| Net operating losses | No carryback or carryforward; only the Alternative Business Calculation Adjustment |
| Section 179 | New Jersey maximum is **$25,000**; the federal reduced dollar limit applies using that $25,000; no business-income limit; unused amounts cannot be carried forward |
| Bonus depreciation | Worksheet GIT-DEP allows the federal 30% allowance and not the 50% allowance; the NJ-1040 instructions require an adjustment whenever the federal special bonus allowance or section 179 was deducted for assets placed in service from 1 January 2004 |
| Alimony | Court-ordered payments made are deducted (line 32) and payments received are income (line 25); the instructions set no agreement-date limit |
| New federal deductions from P.L. 119-21 (tips, overtime, car loan interest, seniors) and the QBI deduction | Our reasoning, not a Division statement: these are federal deductions taken after AGI, and New Jersey income starts from W-2 box 16 state wages ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf), page 4) and the category lines, so they do not reduce it |

GIT-DEP names only the 30% and 50% federal allowances. For assets on which the full (100%) bonus depreciation was taken federally (as allowed again by P.L. 119-21), compute New Jersey depreciation without the bonus on Worksheet GIT-DEP and confirm the treatment with the Division before filing.

### Credit for taxes paid to other jurisdictions (Schedule NJ-COJ) ([GIT-3W](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git3w.pdf); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- Only for income taxed by both New Jersey and another U.S. state, its political subdivision or DC, in the same year. No credit for tax paid to the U.S. government, Puerto Rico or any other country or territory.
- The income must be **properly** taxed there: for a nonresident, generally services performed in that jurisdiction, business carried on there, real or tangible property located there, and gambling there. Interest, dividends and securities gains are generally not properly taxed by another state unless they come from a business there.
- Credit = the lesser of (a) New Jersey tax x (income taxed by both / New Jersey gross income, line 29, carried to seven decimal places) and (b) the tax actually paid to the other jurisdiction on that income. It is not dollar-for-dollar.
- **New York:** use the income actually taxed by New York (the "New York State Amount" column of Form IT-203), not the federal-amount column.
- **Pennsylvania:** under the reciprocal agreement, Pennsylvania does not tax New Jersey residents' employee compensation, so there is no credit for Pennsylvania tax on wages. Self-employment income and property gains taxed by Pennsylvania can qualify. Philadelphia wage tax and other Pennsylvania municipal taxes are outside the agreement and can qualify.
- The Division's publications reviewed here do not address wages for days worked at home in New Jersey that New York taxes under its "convenience of the employer" rule. Treat that as a referral point.

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Single, gross income for the year exactly $10,000 | No filing requirement: it must be **more than** $10,000. File anyway to recover withholding or claim NJEITC | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Not domiciled in New Jersey, permanent New Jersey home, exactly 183 days there | Not a resident: needs **more than** 183 days | [GIT-6](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf) |
| Domiciled in New Jersey, lived abroad all year with a permanent home there, no New Jersey home, 30 days in New Jersey | Nonresident: all three conditions met (30 days is not more than 30) | same |
| Joint filers, both 65, line 27 exactly $100,000, pension $60,000 | Band $0 to $100,000: pension exclusion $60,000; unused $40,000 may go on line 28b if earned income is not more than $3,000 | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Same couple, line 27 more than $150,000 | No pension exclusion and no other retirement income exclusion | same |
| Age 61 and disabled | Pension exclusion allowed; other retirement income exclusion not allowed (needs age 62) | same |
| Taxable income exactly $80,000, child aged 4 | Child Tax Credit $200 (over $60,000, not over $80,000) | [Division Child Tax Credit page](https://www.nj.gov/treasury/taxation/individuals/childtaxcredit.shtml) |
| Taxable income more than $80,000 | No Child Tax Credit | same |
| Property tax deduction saves less than $50 | Take the $50 credit instead | [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf) |
| Taxable income exactly $100,000 | Rate schedules must be used, not the tax table | same |
| Schedule C loss and wage income | Loss makes no entry on line 18 and does not reduce wages; see Schedule NJ-BUS-2 | same |
| Tax for the year after withholding and credits exactly $400 | No estimated payments required: they are required only if tax is **more than** $400 | [2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf) |
| Paid less than 80% of the tax by 15 April, filed by 15 October | Extension denied retroactively; penalties and interest from 15 April | [Form NJ-630](https://www.nj.gov/treasury/taxation/pdf/current/630.pdf) |

## Worked cases ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf); [2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

Assumed facts, computed with the rate schedules. Below $100,000 of line 42 the return uses the Tax Table, which can differ by about $1; Cases 2 and 6 show both.

**Case 1: single sole proprietor who rents, 2026.** Schedule C profit $130,000, no New Jersey adjustments; self-employed health insurance $8,000; one $1,000 exemption; rent paid on the main home $30,000; no withholding. Line 29: $130,000. Taxable income (line 39): $130,000 - $1,000 - $8,000 = $121,000. Property tax: 18% of $30,000 = $5,400. Worksheet H: with the deduction, taxable income is $115,600 and the tax is $115,600 x 6.37% - $2,126.25 = $5,237.47; without it, $121,000 x 6.37% - $2,126.25 = $5,581.45. The deduction saves $343.98, which is $50 or more, so take the deduction. **Tax: $5,237.47.** Estimated tax is required (more than $400); four equal installments of $1,309.37 are due 15 April, 15 June, 15 September 2026 and 15 January 2027.

**Case 2: retired couple, 2025.** Married filing jointly, both 67. Pension $60,000 (line 20a), interest $30,000, dividends $20,000, Social Security (not entered). Line 27 = $110,000, in the $100,001 to $125,000 band. Pension exclusion: lesser of $60,000 and 50% of $60,000 = $30,000. Worksheet D: maximum 50% of $110,000 = $55,000; unused $25,000; no wages or business income, so line 28b is $25,000. Line 29 = $110,000 - $55,000 = $55,000. Exemptions: $1,000 x 2 plus $1,000 x 2 for age = $4,000. Taxable income $51,000 (no property tax benefit in this example). Table B: $51,000 x 2.45% - $420 = $829.50; the Tax Table (required below $100,000) gives **$830**.

**Case 3: losses stay in their category, 2026.** Single. Wages (box 16) $70,000; Schedule C loss $20,000; stock gains $5,000 and stock losses $12,000; rental profit $6,000. Line 15: $70,000. Line 18: no entry (loss). Line 19: net loss of $7,000, so no entry, and it is not carried forward. Line 23: $6,000. **Line 27: $76,000.** The business loss can only help through Schedule NJ-BUS-2 (line 35).

**Case 4: New York commuter, 2025.** Single New Jersey resident who works every day in a New York office. Wages $200,000 (all taxed by New York), bank interest $10,000; lives rent-free with family, so no property tax benefit. Line 29: $210,000. Taxable income: $209,000. Tax: $209,000 x 6.37% - $2,126.25 = $11,187.05. New York tax paid on the $200,000: $12,000 (assumed). Credit limit: $11,187.05 x ($200,000 / $210,000) = $10,654.33, which is less than $12,000, so the **credit is $10,654.33** and New Jersey tax after the credit is **$532.72**.

**Case 5: section 179 over the New Jersey cap, 2026.** A sole proprietor buys $80,000 of equipment and deducts all of it under federal section 179. For New Jersey, only $25,000 is allowed as section 179; the other $55,000 becomes New Jersey depreciable basis, recovered through regular depreciation on Worksheet GIT-DEP. First-year New Jersey adjustment (added to Schedule NJ-BUS-1): $80,000 - $25,000 - first-year New Jersey depreciation on $55,000. Later years give subtractions, and a sale uses the New Jersey basis.

**Case 6: working parent, 2025.** Head of household, one child aged 3, New Jersey taxable income $35,000, federal EIC claimed and allowed $4,000 (assumed), New Jersey withholding $600. Tax (Table B): $35,000 x 1.75% - $70 = $542.50. NJEITC: 40% x $4,000 = $1,600. Child Tax Credit (over $30,000, not over $40,000): $800. Payments and refundable credits: $600 + $1,600 + $800 = $3,000. Refund on the schedule figure: $2,457.50. The Tax Table (required below $100,000) gives tax of $543, so the **refund on the return is $2,457**.

**Case 7: extension that fails the 80% test, 2025 return.** Tax liability $10,000 (line 45). Paid by 15 April 2026: $7,500, below 80% ($8,000). The extension is denied, and penalties and interest run from 15 April 2026 even if the return is filed by 15 October. Filed 30 September 2026 with $2,500 still due: late filing penalty 5% per month or part month, capped at 25%, is $625; a $100 penalty may also be charged for each month the return is late; late payment penalty 5% is $125; plus interest at 3% above prime.

**Case 8: nonresident with New Jersey rent, 2025 (Form NJ-1040NR).** Single, income from everywhere $200,000, of which New Jersey rental income $50,000. Income percentage: $50,000 / $200,000 = 25%. Taxable income (column A, after the $1,000 exemption): $199,000. Tax on it: $199,000 x 6.37% - $2,126.25 = $10,550.05. **New Jersey tax: 25% x $10,550.05 = $2,637.51.**

## When to refuse or refer

- Residency in doubt: a disputed domicile, two permanent homes, a count near 183 days, a move during the year (Forms NJ-1040 and NJ-1040NR together), or military personnel and spouses (GIT-7).
- New York "convenience of the employer" wages for days worked at home in New Jersey, other dual-resident situations, or a Schedule NJ-COJ with several jurisdictions or city and state layers.
- Any federal bonus depreciation other than the 30% allowance ([Worksheet GIT-DEP](https://www.nj.gov/treasury/taxation/pdf/current/gitdep.pdf)), assets under older bonus regimes, sales of assets with a New Jersey basis different from federal, or partnership and S corporation basis differences (GIT-9P, GIT-9S).
- BAIT: the entity election and computation are in the **nj-cbt-and-bait** Guide. Here, only enter the member's share on Schedule NJ-BUS-1 and line 63.
- The Alternative Business Calculation Adjustment (Schedule NJ-BUS-2) beyond a simple case, the Health Enterprise Zone deduction, cannabis licensee adjustments, and the Senior Freeze interaction with the property tax benefit.
- Trusts, estates, grantor trusts, inheritance tax, amended returns, Division notices, audits, penalty waivers and appeals.
- Any request to hide income, invent expenses or claim a residency that the facts do not support.

## Filing and payment ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf); [Form NJ-630](https://www.nj.gov/treasury/taxation/pdf/current/630.pdf); [GIT-8](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git8.pdf))

**2025 returns (dated section).**

- Due **15 April 2026** for calendar-year filers; fiscal-year filers by the 15th day of the fourth month after the year ends. A return postmarked by the due date is on time.
- **Extension to 15 October 2026** (six months) is to **file**, not to pay, and only if **at least 80%** of the tax liability calculated on the return was paid by 15 April 2026 through withholding, estimated payments or a payment with the extension. Then either file Form NJ-630 (or online) by 15 April 2026, or, with a federal extension, fill in the federal-extension oval and enclose a copy of the federal extension if it was filed on paper. Form NJ-630 is still needed with a federal extension if a payment is required to reach 80%. If the 80% test fails or the return is late, the extension is denied and penalties and interest run from the original due date.

**2026 estimated tax** ([2026 NJ-1040-ES instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040esi.pdf)).

- Required if the tax expected for 2026, after withholding and credits, is **more than $400**. Not required if gross income will be at or below the filing threshold.
- Pay in full by 15 April 2026 or in four equal installments by 15 April, 15 June, 15 September 2026 and 15 January 2027. The January installment is not needed if the 2026 return is filed and the balance paid in full by 15 February 2027.
- Farmers with at least two-thirds of estimated income from farming may pay the whole amount by 15 January 2027.
- **Interest on underpayment (Form NJ-2210)** ([GIT-8](https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git8.pdf)): charged if total tax after credits is more than $400 and the payments were not at least 80% of the year's tax (66 2/3% for farmers). The required payment is the lesser of 80% of the current year's tax or 100% of the prior year's tax; the prior-year test applies only if a full 12-month prior-year return with a tax obligation was filed. No interest is charged if there was no tax obligation for the prior year. Interest runs at 3% above prime from each due date to payment, but only up to 15 April.

**Penalties and interest** ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf)).

- Late filing: 5% per month or part month, up to 25% of the outstanding tax, plus a possible $100 per month.
- Late payment: 5% of the outstanding balance.
- Interest: 3% above the prime rate, for each month or part month unpaid; unpaid tax, penalty and interest are added to the balance at the end of each calendar year.

**Paying.** E-check or credit card online, or check with Form NJ-1040-V payable to "State of New Jersey – TGI". Refunds must generally be claimed within three years of the due date, including extensions.

## Completion checklist ([2025 NJ-1040 instructions](https://www.nj.gov/treasury/taxation/pdf/current/1040i.pdf))

- [ ] Residency tested (domicile; 30-day exception; permanent home and more than 183 days) and the right form or forms chosen.
- [ ] Each income item on its own category line; wages from W-2 box 16; no negative entries; no loss carried from another year or category.
- [ ] Schedule NJ-BUS-1 adjustments made, including Worksheet GIT-DEP for section 179 above $25,000 and any bonus depreciation.
- [ ] Retirement exclusions tested on line 27 ($150,000 or less), age 62 (or disability for line 28a), filing status band, and the $3,000 earned-income test for line 28b.
- [ ] Exemptions claimed with first-time proofs (age, disability, veteran discharge, domestic partnership).
- [ ] Medical deduction above 2% of line 29, with self-employed health insurance included.
- [ ] Property tax deduction or credit compared ($50 test) and only one claimed; tenant figure is 18% of rent.
- [ ] Schedule NJ-COJ with the other state's return; New York amount taken from the IT-203 New York State Amount column.
- [ ] NJEITC at 40% of the allowed federal EIC; Child Tax Credit only for children 5 or younger and taxable income of $80,000 or less.
- [ ] BAIT share from Schedule NJ-BUS-1 on line 63, with Schedule PTE-K-1 or NJK-1 enclosed.
- [ ] Use tax line 51 completed (0.00 if none) and health coverage questions answered.
- [ ] Extension only with at least 80% paid by 15 April; 2026 estimates set up if the tax will be more than $400.

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
