---
name: oh-income-tax
description: Compute an Ohio individual's 2026 income tax on Form IT 1040, for residents, part-year residents and nonresidents, including sole proprietors and pass-through owners. Covers the 2026 single nonbusiness rate under R.C. 5747.02 as amended by HB 96 (no tax up to $26,050, then $332.00 plus 2.75% of the excess), the business income deduction (first $250,000, or $125,000 married filing separately) with the 3% rate on the rest, exemptions by modified AGI with the 2026 cut-off of $500,000, the Schedule of Adjustments, credits, the contact-period residency test, estimated tax and penalties. Trigger on "Ohio income tax", "IT 1040", "Ohio business income deduction", "Ohio nonresident", "Ohio estimated tax", "IT 1040ES". Points to school district and municipal income taxes without computing them. Load the federal skills first for federal AGI.
version: "1.1"
jurisdiction: US-OH
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Ohio individual income tax (Form IT 1040), tax year 2026

> **Source-cited draft.** Built from R.C. 5747.02 and 5747.025 as amended by HB 96 (136th General Assembly, effective 30 September 2025), the 2026 Ohio IT 1040ES worksheet and instructions, the 2025 Ohio IT 1040 instructions, and the Department of Taxation interest rate page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For tax year 2026 Ohio has one rate on nonbusiness income: no tax on the first $26,050 of Ohio AGI less taxable business income and exemptions, then **$332.00 plus 2.75%** of the amount above $26,050 (R.C. 5747.02(A)(3)(c)). Business income keeps its own track: the first **$250,000** ($125,000 married filing separately) is deducted, and the rest is taxed at a flat **3%** (R.C. 5747.02(A)(4)). Exemptions are allowed only when modified AGI is under **$500,000** for 2026 (R.C. 5747.025(A)); for 2025 the cut-off was $750,000. Ohio has no standard deduction and no itemized deductions; it starts from federal AGI.

## Scope and who this is for

In scope: the Ohio IT 1040 for tax year 2026 (filed in 2027), with the 2025 rules kept where a 2025 return is still open. Full-year residents, part-year residents and nonresidents with Ohio income, including sole proprietors and owners of pass-through entities whose business income reaches Ohio through federal AGI.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Federal AGI, Schedule C and self-employment tax | `us-schedule-c-and-se-computation` and the federal return skills |
| Federal estimated tax | `us-quarterly-estimated-tax` |
| Ohio employer withholding and unemployment insurance | `oh-payroll` |
| Ohio school district income tax (SD 100) | not computed here: see "When to refuse or refer" |
| Ohio municipal (city and village) income taxes | not computed here: a cross-state local income tax skill covers them. Pointer only, see "When to refuse or refer" |
| Pass-through entity returns (IT 4708, IT 1140, IT 4738), fiduciary returns (IT 1041), certificate-based business credits | refer |
| Ohio sales and use tax, Commercial Activity Tax | the Ohio sales tax and CAT skills in this folder |

**Who must file** ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); confirm against the 2026 instructions when published):
- Every Ohio resident and part-year resident is subject to the tax. Every nonresident with Ohio-sourced income must also file (for example Ohio wages, Ohio lottery, casino or sports gaming winnings, income from Ohio property, or income from a sole proprietorship or pass-through entity doing business in Ohio).
- **Reciprocity exception:** a **full-year** nonresident living in Indiana, Kentucky, Michigan, Pennsylvania or West Virginia need not file if their **only** Ohio-sourced income is wages.
- **No return is needed** if any of these is true: Ohio AGI (IT 1040 line 3) is $0 or less; the senior citizen, lump sum distribution and joint filing credits together equal or exceed the tax on line 8c **and** there is no school district income tax liability; or the exemption amount (line 4) equals or exceeds Ohio AGI.
- A school district income tax liability forces an IT 1040 even when one of those exceptions applies.
- For 2025 the Department recommends filing an IT 1040 or IT 10 when federal AGI is greater than $28,450, even with no tax due, to avoid delinquency billings.

## Ask the client first

1. **Which tax year?** 2025 has two nonbusiness brackets above zero with a top rate of 3.125%; 2026 has the single 2.75% rate. The exemption cut-off also changes ($750,000 to $500,000).
2. **Residency for the whole year**, for each spouse: where the client's abode is, whether they moved into or out of Ohio (and the dates), and how many **contact periods** they had in Ohio. A person with an Ohio abode is presumed to be a resident.
3. **Federal filing status.** Ohio must match it. A couple who filed jointly federally must file jointly in Ohio even if one or both are nonresidents.
4. **Federal AGI and what is in it:** Schedule C, E and F results, wages, guaranteed payments, pensions and IRA distributions (and whether any was a lump sum), taxable Social Security, interest (including other states' bonds and U.S. obligations), capital gains.
5. **Ownership percentage** in any pass-through entity. Wages and guaranteed payments from an entity the client owns **20% or more** of are business income.
6. **Bonus depreciation and section 179** claimed on the federal return this year, and Ohio add-backs from the five prior years (for the recovery deduction).
7. **Dates of birth** (65 or older at year-end for the senior citizen and lump sum distribution credits) and whether either spouse ever took an Ohio lump sum retirement or lump sum distribution credit.
8. **Each spouse's own qualifying income** for the joint filing credit (wages and similar, not interest, dividends, capital gains, rents or royalties, and not amounts deducted on the Schedule of Adjustments).
9. **Other states:** income taxed elsewhere, with that state's return and proof of payment.
10. **School district and municipality** of residence for the year, and the cities where the client worked (use The Finder at tax.ohio.gov/Finder for the school district).
11. **Payments:** Ohio withholding, estimated payments (dates and amounts), prior-year Ohio tax and whether the prior-year return was filed on time, any credit carryforward and any extension payment.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount, 2026 | Rate or amount, 2025 | Source |
| --- | --- | --- | --- |
| Nonbusiness income, zero-tax band | $26,050 or less: no tax | $26,050 or less: no tax | [R.C. 5747.02(A)(3)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| Nonbusiness income above the band | $332.00 plus 2.75% of the amount over $26,050 | $26,050 to $100,000: $342.00 plus 2.75% of the excess; over $100,000: $2,394.32 plus 3.125% of the excess | [R.C. 5747.02(A)(3)(b) and (c)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| Business income deduction | First $250,000 ($125,000 married filing separately) | Same | [2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); 2026 not yet confirmed |
| Rate on taxable business income | 3% | 3% | [R.C. 5747.02(A)(4)(a)](https://codes.ohio.gov/ohio-revised-code/section-5747.02) |
| Exemption allowed only if MAGI is less than | $500,000 | $750,000 | [R.C. 5747.025(A)](https://codes.ohio.gov/ohio-revised-code/section-5747.025) |
| Exemption per person, MAGI $40,000 or less | not yet published (indexed under R.C. 5747.025(C)) | $2,400 | [R.C. 5747.025(A)(1), (C)](https://codes.ohio.gov/ohio-revised-code/section-5747.025); [2025 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf) |
| Exemption per person, MAGI $40,001 to $80,000 | not yet published (indexed under R.C. 5747.025(C)) | $2,150 | same |
| Exemption per person, MAGI above $80,000 | not yet published (indexed under R.C. 5747.025(C)); the 2026 IT 1040ES uses $1,900 | $1,900 | [R.C. 5747.025(A)(3)](https://codes.ohio.gov/ohio-revised-code/section-5747.025); [2025 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [2026 IT 1040ES](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf) |
| Estimated payments needed if tax after credits less withholding is more than | $500 | $500 | [2026 IT 1040ES](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf) |
| Estimated tax safe harbor | lesser of 90% of 2026 tax or 100% of 2025 tax | same rule | [2026 IT 1040ES worksheet lines 10 and 11](https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf) |
| Interest rate on unpaid tax | 7% (calendar year 2026) | 8% (calendar year 2025) | [Department interest rate page](https://tax.ohio.gov/individual/resources/interest-rates) |

Notes on the table:
- **The 2026 rate is in the statute, not yet in a 2026 form.** R.C. 5747.02(A)(3)(c) reads: "For taxable years beginning in 2026 and thereafter, $332.00 plus 2.75% of the amount in excess of $26,050." The tax commissioner indexes the $26,050 band each August under R.C. 5747.02(A)(5) and does not adjust rates; no 2026 adjusted band had been published when read. Use $26,050 until the 2026 IT 1040 instructions say otherwise.
- **The 2026 IT 1040ES worksheet is out of date on the brackets.** Its revised January 2026 edition still prints the 2025 brackets ($342.00 plus 2.75%, and $2,394.32 plus 3.125% above $100,000). Using it for 2026 estimates overstates tax above $100,000 of nonbusiness income: safe for estimates, wrong for the return.
- **The tax jumps at $26,050.** At $26,050 the tax is $0; one dollar more gives $332.00 plus 2.75% of $1. This step is how the statute is written (the $332.00 is the estate rate of 1.27448% times $26,050, R.C. 5747.02(A)(2) and (A)(5)). Do not smooth it.
- **2025 printed bases do not run continuously** either: at $100,000 the second 2025 row gives $2,375.63 while the third row starts at $2,394.32. Apply the schedule as printed.

### From federal AGI to Ohio tax

Line numbers are from the 2025 forms ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)); check them against the 2026 form when published.

1. **Line 1, federal AGI** from federal Form 1040 line 11. The deductible half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions are already inside federal AGI. The federal qualified business income deduction has no effect on the Ohio return.
2. **Classify business income** on the **Ohio Schedule of Business Income**. Business income arises from the regular course of a trade or business, from property integral to it, from a business liquidation (including goodwill), from certain sales of an ownership interest (an asset sale for federal purposes, or one where the seller materially participated in the year of sale or any of the five years before), and from compensation or guaranteed payments paid by a pass-through entity to an investor owning **20% or more** of it. Everything else is nonbusiness income. Apply the transactional or functional test; do not simply copy federal schedule totals.
   - Line 10 is total business income. **Line 11** is the lesser of line 10 and federal AGI; if zero or negative, there is no deduction and no taxable business income.
   - **Line 12:** $250,000, or $125,000 for married filing separately.
   - **Line 13, the business income deduction (BID):** the lesser of lines 11 and 12, carried to the Schedule of Adjustments.
3. **Schedule of Adjustments.** Additions (to line 2a) include non-Ohio state and local bond interest, Ohio pass-through entity tax not in federal AGI, and the section 168(k) and 179 add-back. Deductions (to line 2b) include the BID, taxable Social Security, certain railroad benefits, U.S. obligation interest, state and local refunds in federal AGI, the prior-year depreciation recovery, 529 contributions and uniformed services retirement income.
4. **Line 3, Ohio AGI** = line 1 plus line 2a minus line 2b.
5. **MAGI** (modified adjusted gross income) = Ohio AGI **plus** the BID. MAGI, not Ohio AGI, sets the exemption amount and most credit limits.
6. **Line 4, exemptions:** one for the taxpayer and one for the spouse on a joint return (each only if not claimed as someone else's dependent), plus one per dependent claimed on the federal return, times the amount for the client's MAGI. Zero if MAGI is $500,000 or more (2026).
7. **Line 5, Ohio income tax base** = line 3 minus line 4 (not below zero).
8. **Line 6, taxable business income** = the lesser of (Schedule of Business Income line 11 minus line 13) and line 5. **Line 7, taxable nonbusiness income** = line 5 minus line 6. The exemptions therefore reduce nonbusiness income first; any excess comes off business income (R.C. 5747.02(A)(4)(b)).
9. **Line 8a**, tax on line 7 from the nonbusiness schedule; **line 8b**, line 6 times 3%; **line 8c** = 8a + 8b.
10. **Line 9, nonrefundable credits** from the Ohio Schedule of Credits (see "Credits"). **Line 10** = line 8c minus line 9, not below zero. The nonresident credit (IT NRC) and resident credit (IT RC) also go through the Schedule of Credits.
11. **Lines 11 onward:** add the IT/SD 2210 interest penalty and unpaid use tax; subtract withholding, estimated and extension payments, carryforward and refundable credits; add interest on late payment, to reach the amount due or the overpayment. Ohio rounds to the nearest dollar.
12. **Then check the separate local taxes:** a school district income tax (SD 100) if the client lived in a taxing district, and any municipal income tax (filed with the city or its administrator). Neither is computed here.

### Credits (2025 rules; 2026 limits not yet published)

All are **nonrefundable**; unused amounts are lost unless the instructions say they carry forward.

- **Retirement income credit.** MAGI less exemptions under $100,000; income from a pension, profit-sharing or retirement plan received on account of retirement and included in Ohio AGI; never took the Ohio lump sum retirement credit. Social Security and other deducted amounts do not count. Maximum $200 per return:

| Retirement income in Ohio AGI | Credit |
| --- | --- |
| $500 or less | None |
| $501 to $1,500 | $25 |
| $1,501 to $3,000 | $50 |
| $3,001 to $5,000 | $80 |
| $5,001 to $8,000 | $130 |
| $8,001 or more | $200 |

- **Lump sum retirement credit.** For a total lump sum distribution on account of retirement from a qualified plan, MAGI less exemptions under $100,000, never claimed before. Taking it bars the retirement income credit that year and in all future years.
- **Senior citizen credit:** $50 per return, if MAGI less exemptions is under $100,000, the client was 65 or older at year-end, and never took the lump sum distribution credit.
- **Lump sum distribution credit:** for someone 65 or older with a total lump sum distribution from a qualified plan, MAGI less exemptions under $100,000, never claimed before; an age multiple times $50. Bars the senior citizen credit that year and later.
- **Child and dependent care credit:** only if MAGI is under $40,000 and the federal credit was claimed. Below $20,000 it equals the federal amount; from $20,000 to under $40,000 it is 25% of the federal credit.
- **Exemption credit:** $20 per exemption claimed, if MAGI less exemptions is under $30,000.
- **Joint filing credit:** joint return; **each** spouse has at least $500 of qualifying income in Ohio AGI (not interest, dividends, capital gains, rents or royalties, and not amounts deducted such as the BID or Social Security); MAGI under $750,000 for 2025. A percentage of the tax after the earlier credits, capped at $650, with a statement of each spouse's qualifying income:

| MAGI less exemptions | Percentage |
| --- | --- |
| $0 to $25,000 | 20% |
| $25,001 to $50,000 | 15% |
| $50,001 to $75,000 | 10% |
| $75,001 to $749,999 | 5% |

- **Ohio earned income credit:** 30% of the federal earned income credit, nonrefundable.
- **Campaign contribution credit:** repealed by HB 96; the 2025 instructions say it is not available after tax year 2025.
- **2026:** check whether the $750,000 joint filing credit limit moved with the exemption cut-off before using it.

### Federal conformity and depreciation

- **Conformity.** The Department reports that Senate Bill 9, signed 5 March 2026, conforms Ohio to the Internal Revenue Code for tax year 2025, including the One Big Beautiful Bill Act changes that affect Ohio. A taxpayer may irrevocably elect, under R.C. 5701.11, to file 2025 under the Code as it stood at year-end instead; all or nothing. No 2026 conformity statement was found when read: check the Department's conformity page before filing a 2026 return.
- **Decoupling survives conformity.** Ohio's own add-backs and deductions on the Schedule of Adjustments stay unless amended.
- **Bonus depreciation and section 179 add-back.** Add back **5/6** of federal section 168(k) bonus depreciation, and 5/6 of section 179 expense above what section 179 allowed on 31 December 2002. Use **2/3** for an employer that increased Ohio income tax withheld by at least 10% over the previous year; **6/6** where the depreciation creates a federal net operating loss; **no add-back** for an employer whose increase in Ohio withholding is at least the total 168(k) and 179 expense, or for depreciation from a pass-through entity in which the taxpayer owns less than 5%.
- **Recovery.** Deduct in equal amounts in later years: 1/5 of each 5/6 add-back (five years), 1/2 of each 2/3 add-back (two years), 1/6 of each 6/6 add-back (six years). In a year with an NOL, carryback or carryforward the deduction waits for the next year without one. Only amounts actually added back may be recovered, even if the asset has been sold.

### Residency, nonresidents and part-year residents

- **Resident** means domiciled in Ohio. Anyone with an abode in Ohio (owned or rented) is **presumed** to be a resident; a temporary absence does not change it.
- **Part-year resident:** permanently moved into or out of Ohio during the year. They get the nonresident credit (IT NRC) for income earned while resident elsewhere, and the resident credit (IT RC) for non-Ohio income earned while an Ohio resident and taxed by another state.
- **Nonresident:** resident elsewhere all year; nonresident credit for income not earned or received in Ohio.
- **Contact periods.** A contact period is when the person has an abode outside Ohio, is away overnight from it, and spends any part of **two consecutive days** in Ohio. With **fewer than 213** contact periods, nonresidency must be shown "more likely than not"; with **213 or more**, by clear and convincing evidence.
- **Nonresident presumption.** From tax year 2025 the IT NRS form is no longer used; the presumption is claimed by checking the **Ohio Nonresident Statement** box on the IT 10 or IT 1040 (each spouse their own box). All five criteria must be met: (1) no more than 212 contact periods in Ohio; (2) an abode outside Ohio on which no depreciation was claimed; (3) no Ohio driver's license or state ID, surrendered before the year began; (4) no Ohio homestead exemption or owner-occupied property tax reduction; (5) no Ohio in-state tuition received. Deadline: the 15th day of the 10th month after year-end (15 October). Part-year residents cannot use it.
- **Resident credit (IT RC):** only for tax paid to another U.S. state or the District of Columbia on income also in Ohio AGI; not for city, foreign or territory taxes, not for states without an income tax, and not for wages earned in the five reciprocity states.

### 2025 returns still open

- 2025 returns were due 15 April 2026, or 15 October 2026 on extension, with interest on unpaid tax from 15 April 2026.
- Use the 2025 brackets (top rate 3.125%), the 2025 exemption table (cut-off $750,000) and the 2025 credits.
- Other 2025 changes: the Ohio educator expense deduction rose to $300 per taxpayer; the home school expenses credit became $250 per qualifying student; a new deduction for contributions to a pregnancy resource center; the IT NRS form is no longer used.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Owner of 20% of an S corporation draws a W-2 salary | The wages are business income, eligible for the BID. Below 20% ownership, wages and guaranteed payments are nonbusiness income. |
| Spouse works for the other spouse's company and owns none of it directly or indirectly | Wages are nonbusiness income. Federal attribution does not count as indirect ownership. |
| Schedule C profit is larger than federal AGI | BID and taxable business income are limited to federal AGI (Schedule of Business Income line 11). |
| Taxable nonbusiness income exactly $26,050 (2026) | No tax. At $26,051 the tax is $332.00 plus 2.75% of $1. |
| MAGI exactly $500,000 (2026) | No exemption: the statute needs MAGI less than $500,000. |
| MAGI exactly $750,000 (2025) | No exemption and no joint filing credit. |
| MAGI exactly $80,000 (2025) | Exemption is $2,150; the $1,900 band starts at $80,001. |
| MAGI less exemptions exactly $100,000 | No retirement income, lump sum or senior citizen credit (each needs less than $100,000). |
| Couple files jointly; one spouse has only business income and Social Security | No joint filing credit: that spouse has no qualifying income in Ohio AGI. |
| Client took the lump sum distribution credit in an earlier year | No senior citizen credit this year or later. |
| Kentucky resident whose only Ohio income is wages | No Ohio return. If they also have Ohio rental income, they file and report it. |
| Part-year resident who meets the five nonresident criteria | Cannot claim the nonresident presumption. |
| Expected tax after credits less withholding exactly $500 | No estimated payments required. |
| Prior-year Ohio return not filed on time | The 100%-of-prior-year safe harbor is unavailable; use 90% of current-year tax. |
| Federal NOL year with an unrecovered 5/6 depreciation add-back | The recovery deduction waits until a year with no NOL, carryback or carryforward. |
| 2026 estimate computed from the printed IT 1040ES brackets | Overstates tax above $100,000 of nonbusiness income; acceptable for estimates, never for the return. |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| 2026 exemption amount | $1,900 per exemption (the 2026 IT 1040ES figure), flagged as not yet confirmed; zero at MAGI of $500,000 or more |
| Ownership share in a pass-through paying the client wages | Treat the wages as nonbusiness income until the share is shown to be 20% or more |
| Whether the prior-year return was filed on time | Use 90% of current-year tax for the estimate |
| School district of residence | Look it up in The Finder; never assume no district tax |

### Red flags to raise with the client

- An Ohio abode with a claimed move out of Ohio, or 213 or more contact periods.
- Business income from the sale of an ownership interest, or a rental called a business.
- Wages from the client's own company with ownership near 20%.
- A 2026 estimate or projection that used the 3.125% bracket: recompute on the 2026 single rate.
- Any city or village of residence or work: municipal income tax is separate and must be handled.

## Worked cases

Client facts are invented; rates and thresholds are real. Ohio rounds to the nearest dollar on the return; the checks below keep cents.

**Case 1: married couple, wages, 2026 against 2025.** Wages of $90,000 and $30,000, joint bank interest of $2,000, federal AGI $122,000, one dependent, no adjustments. MAGI $122,000, so three exemptions at the $1,900 figure (not yet confirmed for 2026) = $5,700. Line 5 and line 7: $116,300. 2026 tax: $332.00 plus 2.75% of ($116,300 minus $26,050) = $332.00 + $2,481.88 = $2,813.88, so $2,814. On the 2025 schedule the same income gave $2,394.32 plus 3.125% of $16,300 = $2,903.70. The single rate saves $89.82 before credits.

```oa-check
name: Ohio MFJ wages 2026 single rate against 2025 brackets
inputs:
  fed_agi: 122000
  exemptions: 3
  exemption_amount: 1900
steps:
  - base: fed_agi - exemptions * exemption_amount
  - tax_2026: 332 + 0.0275 * max(base - 26050, 0)
  - tax_2025: 2394.32 + 0.03125 * max(base - 100000, 0)
  - saving: tax_2025 - tax_2026
expected:
  base: 116300
  tax_2026: 2813.88
  tax_2025: 2903.70
  saving: 89.82
```

**Case 2: sole proprietor with investment income, and which estimate safe harbor to use (decision).** Single, 2026. Schedule C profit $400,000, interest and dividends $60,000, federal AGI $460,000. BID $250,000, so Ohio AGI is $210,000 and MAGI $460,000: under $500,000, so one exemption of $1,900. Line 5: $208,100. Line 6, taxable business income: the lesser of $150,000 ($400,000 minus $250,000) and $208,100 = $150,000. Line 7, nonbusiness: $58,100. Tax: $332.00 plus 2.75% of $32,050 = $1,213.38 on nonbusiness income, plus 3% of $150,000 = $4,500, total $5,713.38. Decision: the client's 2025 Ohio tax was $6,000 on a return filed on time. The required annual estimate is the lesser of 90% of 2026 tax ($5,142.04) and 100% of 2025 tax ($6,000), so pay on the 90% figure: four installments of $1,285.51. If the 2025 return had been late, only the 90% route is open, which gives the same answer here; if 2026 income could rise, the 100%-of-prior-year figure is the safer harbor because it does not move.

```oa-check
name: Ohio sole proprietor 2026 with BID, and estimate safe harbor
inputs:
  business_income: 400000
  nonbusiness_income: 60000
  fed_agi: 460000
  exemption_amount: 1900
  prior_year_tax: 6000
steps:
  - bid: min(min(business_income, fed_agi), 250000)
  - ohio_agi: fed_agi - bid
  - line5: ohio_agi - exemption_amount
  - taxable_business: min(business_income - bid, line5)
  - taxable_nonbusiness: line5 - taxable_business
  - tax_nonbusiness: 332 + 0.0275 * max(taxable_nonbusiness - 26050, 0)
  - tax_business: taxable_business * 0.03
  - total_tax: tax_nonbusiness + tax_business
  - required_annual: min(total_tax * 0.9, prior_year_tax)
  - installment: required_annual * 0.25
expected:
  ohio_agi: 210000
  taxable_business: 150000
  taxable_nonbusiness: 58100
  tax_nonbusiness: 1213.38
  total_tax: 5713.38
  required_annual: 5142.04
  installment: 1285.51
```

**Further cases in words (2025 rules, kept from the earlier version).**
- *Single sole proprietor, 2025:* Schedule C $300,000, federal AGI $285,000. BID $250,000; Ohio AGI $35,000; MAGI $285,000, so one exemption of $1,900 (Ohio AGI alone would wrongly suggest $2,400). Line 5 $33,100, all business income: tax 3% = $993. The same facts give $993 in 2026, since the business track did not change.
- *Retiree aged 70, 2025:* IRA and pension $40,000, taxable Social Security $20,000 (deducted). Ohio AGI and MAGI $40,000, exemption $2,400, line 7 $37,600. Tax $342.00 plus 2.75% of $11,550 = $659.63, so $660. Retirement income credit $200 and senior citizen credit $50: tax after credits $410.
- *Snowbird, 2025:* Florida home not depreciated, 150 contact periods in Ohio, Ohio license surrendered in 2024, no homestead reduction, no Ohio in-state tuition. All five criteria met: check the Ohio Nonresident Statement box by 15 October 2026. Had the client kept an Ohio license, the presumption fails, but with fewer than 213 contact periods nonresidency can still be shown more likely than not.
- *Bonus depreciation, 2025:* federal 168(k) of $60,000, no employees, no NOL. Add back 5/6 = $50,000 on the 2025 return; deduct $10,000 a year for 2026 to 2030.

## When to refuse or refer

- **School district income tax (SD 100).** Only residents of a taxing school district owe it; working in a district without living there does not create it. Districts use a traditional base or an earned income base. Look up the district and rate (The Finder, or the Department's 2026 school district rate list) and prepare the SD 100 separately. Do not guess a rate.
- **Municipal (city and village) income tax.** Ohio cities and villages levy their own income taxes under R.C. Chapter 718, filed with the municipality or its administrator, not on the IT 1040 or SD 100, and not creditable on the state return. This skill does not compute them: use the cross-state local income tax skill, and confirm each city's rate and credit with the city.
- **Residency in doubt:** an Ohio abode with a claimed move, 213 or more contact periods, or a client who fails one of the five nonresident criteria.
- **Unclear business or nonbusiness classification** (a sale of an ownership interest, rental activity, mixed-use assets): it moves income between the 3% track with the BID and the nonbusiness schedule.
- **Pass-through entities:** IT 4738 electing entity tax, IT 4708 composite returns, IT K-1 credits and the non-Ohio entity tax add-back.
- **Final 2026 returns** until the 2026 IT 1040 instructions publish the exemption table, credit limits and any indexed band.
- **The R.C. 5701.11 election** for 2025, or an amended 2025 return triggered by conformity.
- **NOL carrybacks** (Schedule IT NOL), multi-year depreciation histories with missing records, military servicemembers, assessments and appeals.

## Filing and payment

- **Due date:** the 2026 IT 1040 is due in April 2027 (15 April unless the 2026 instructions say otherwise; not yet published). 2025 returns were due 15 April 2026.
- **Extension:** Ohio has no extension form. It honours a federal extension: check the extension box and include the IRS extension, acknowledgment or confirmation number; the return is then due 15 October. **An extension to file is not an extension to pay**: interest runs on unpaid tax from the April due date.
- **Estimated tax for 2026:** required if expected Ohio tax after credits, less Ohio withholding, is more than $500. Due **15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027**, each 25% of the required annual amount, using the Ohio Universal Payment Coupon (OUPC). Payments apply only to the SSN on the coupon, so spouses unsure of their filing status should pay separately. A revised IT 4 raising withholding is an alternative.
- **Underpayment interest penalty (IT/SD 2210):** none if timely payments reach 90% of current-year tax, or 100% of prior-year tax where that return was filed on time, or if current-year tax less withholding is $500 or less. Farmers and fishermen have special rules (Adm. Code 5703-7-04).
- **Interest** on late tax: 7% for calendar year 2026, 8% for 2025. **Late payment penalty:** double the interest rate. **Late filing penalty:** the greater of $50 a month (up to $500) or 5% a month (up to 50%) of the tax, even when the return shows a refund. Confirm against R.C. 5747.15 before quoting a penalty in writing.
- **Payment:** electronic check or card at tax.ohio.gov/pay (OH|TAX eServices), or check payable to "Ohio Treasurer of State" with the coupon. Pay Ohio and school district tax separately.
- **Refund claims** generally within four years from the date of payment. An amended return is required within 90 days after the IRS finalises a change to federal AGI.

## Completion checklist

- [ ] Year: 2026 single rate ($332.00 plus 2.75% above $26,050) used for 2026; 2025 brackets only for 2025.
- [ ] Exemptions use MAGI, not Ohio AGI; zero at MAGI of $500,000 or more for 2026; the per-person 2026 amount flagged until published.
- [ ] Residency checked for each spouse; Ohio Nonresident Statement box used only when all five criteria are met; IT NRC and IT RC attached where claimed.
- [ ] Line 1 is federal AGI; filing status matches the federal return.
- [ ] Schedule of Business Income: 20% ownership test applied; line 11 capped at federal AGI; BID on the Schedule of Adjustments.
- [ ] Schedule of Adjustments: 168(k) and 179 add-back computed; prior-year recovery taken (unless an NOL year); Social Security deducted.
- [ ] Credits: each condition checked; joint filing credit statement attached.
- [ ] Payments: withholding statements, estimates and extension payments entered; IT/SD 2210 reviewed.
- [ ] Local taxes: school district residence and SD 100 considered; municipal income tax handed to the local tax skill.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| R.C. 5747.02, tax rates (effective 30 September 2025, HB 96). Read for (A)(3)(b) 2025 brackets, (A)(3)(c) 2026 "$332.00 plus 2.75% of the amount in excess of $26,050", (A)(4) 3% on taxable business income, (A)(5) August indexing. | https://codes.ohio.gov/ohio-revised-code/section-5747.02 | 2026-11-13 |
| R.C. 5747.025, personal exemptions (effective 30 September 2025, HB 96). Read for (A) the $750,000 (2025) and $500,000 (2026 and after) MAGI cut-offs and the statutory bases, (C) indexing. | https://codes.ohio.gov/ohio-revised-code/section-5747.025 | 2026-11-13 |
| 2026 Ohio IT 1040ES worksheet and instructions (revised January 2026). Read for the $1,900 exemption on line 4, the $500,000 note, the 90% and 100% safe harbor, 25% installments, the $500 threshold and the four due dates. | https://dam.assets.ohio.gov/image/upload/v1768492539/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf | 2026-11-13 |
| 2025 Ohio IT 1040 instructions. Read for who must file, the business income deduction ($250,000 or $125,000) and 3%, the 2025 exemption table, the credits, residency and contact periods, and the April 2026 due dates. | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf | 2026-11-13 |
| Ohio Department of Taxation, interest rates. Read for 7.0% (2026) and 8.0% (2025). | https://tax.ohio.gov/individual/resources/interest-rates | 2026-11-13 |
| Ohio Department of Taxation, employer withholding page. Read for the 2026 school district rate list and the supplemental rate (used for the pointer to `oh-payroll`). | https://tax.ohio.gov/business/employer-withholding | 2026-11-13 |

Not yet confirmed: the 2026 IT 1040 and its instructions were not published when read, so the 2026 per-person exemption amounts (the $1,900 used above comes from the 2026 IT 1040ES worksheet), any August 2026 indexing of the $26,050 band, the 2026 business income deduction amounts (assumed unchanged at $250,000 and $125,000 from the 2025 instructions), the 2026 credit limits, the 2026 conformity date and the April 2027 due date are not confirmed. The 2025 conformity statement (Senate Bill 9) and the late filing penalty figures are carried from the earlier version of this skill and were not reopened today.
