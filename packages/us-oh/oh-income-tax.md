---
name: oh-income-tax
description: Triggers when the taxpayer is an Ohio resident sole proprietor or single-member LLC needing to file Ohio Form IT 1040. Covers Ohio's graduated income tax on nonbusiness income (0%, 2.75%, 3.125% for tax year 2025), the business income deduction ($250,000 exclusion taxed at flat 3%), Ohio Schedule of Adjustments, and interaction with federal AGI. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.1"
jurisdiction: US-OH
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ohio individual income tax (Form IT 1040), including sole proprietors

## Scope and who this is for ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [OBM Monthly Financial Report, December 2025](https://archives.obm.ohio.gov/Files//Budget_and_Planning/Monthly_Financial_Report/2025-12-mfr.pdf))

This Guide covers the Ohio individual income tax return, **Ohio IT 1040**, for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns** (due 15 April 2026, or 15 October 2026 on extension). It is for full-year residents, part-year residents and nonresidents with Ohio income, including sole proprietors and owners of pass-through entities whose business income reaches Ohio through federal adjusted gross income (AGI).

Figures are for tax year 2025 unless labelled 2026. The reason: the Department of Taxation had not published the 2026 IT 1040 instructions or a 2026 rate schedule on 25 September 2026. What is known for 2026 is stated as such in "Figures by year", with its source.

It does **not** compute the **school district income tax** (Form SD 100) or any **municipal income tax**; it only says when to look at them. It also does not cover the pass-through entity's own returns (IT 4708, IT 1140, IT 4738), fiduciary returns (IT 1041) or certificate-based business credits.

**Who must file (2025 rules, [2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)).**
- Every Ohio resident and part-year resident is subject to the tax. Every nonresident with Ohio-sourced income must also file (for example Ohio wages, Ohio lottery, casino or sports gaming winnings, income from Ohio property, or income from a sole proprietorship or pass-through entity doing business in Ohio).
- **Reciprocity exception:** a **full-year** nonresident living in Indiana, Kentucky, Michigan, Pennsylvania or West Virginia need not file if their **only** Ohio-sourced income is wages.
- **No return is needed** if any of these is true:
  - Ohio AGI (IT 1040 line 3) is $0 or less;
  - the senior citizen, lump sum distribution and joint filing credits together equal or exceed the tax on line 8c, **and** there is no school district income tax liability;
  - the exemption amount (line 4) equals or exceeds Ohio AGI.
- A school district income tax liability forces an IT 1040 even when one of those exceptions applies.
- The Department recommends filing an IT 1040 or IT 10 when federal AGI is greater than $28,450, even with no tax due, to avoid delinquency billings.

## Ask the client first

- **Which tax year?** 2025 has three nonbusiness brackets with a top rate of 3.125%. From 2026 Ohio moves to a single 2.75% rate ([OBM Monthly Financial Report](https://archives.obm.ohio.gov/Files//Budget_and_Planning/Monthly_Financial_Report/2025-12-mfr.pdf)), but the official 2026 schedule is not yet published.
- **Residency for the whole year**, for each spouse: where the client's abode is, whether they moved into or out of Ohio (and the dates), and how many **contact periods** they had in Ohio. A person with an Ohio abode is presumed to be a resident.
- **Federal filing status.** Ohio must match it. A couple who filed jointly federally must file jointly in Ohio even if one or both are nonresidents.
- **Federal AGI and what is in it:** Schedule C, E and F results, wages, guaranteed payments, pensions and IRA distributions (and whether any was a lump sum), taxable Social Security, interest (including other states' bonds and U.S. obligations), capital gains.
- **Ownership percentage** in any pass-through entity. Wages and guaranteed payments from an entity the client owns **20% or more** of are business income ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)).
- **Bonus depreciation and section 179** claimed on the federal return this year, and Ohio add-backs from the five prior years (for the deduction schedule).
- **Dates of birth** (65 or older at year-end for the senior citizen and lump sum distribution credits) and whether either spouse ever took an Ohio lump sum retirement or lump sum distribution credit.
- **Each spouse's own income** that counts for the joint filing credit (wages and similar, not interest, dividends, capital gains, rents or royalties, and not amounts deducted on the Schedule of Adjustments).
- **Other states:** income taxed elsewhere, with that state's return and proof of payment.
- **School district:** the school district of residence for the year (use The Finder at tax.ohio.gov/Finder). Some districts levy an income tax.
- **Payments:** Ohio withholding, estimated payments (dates and amounts), prior-year Ohio tax and whether the prior-year return was filed on time, any credit carryforward and any extension payment.

## The method, step by step

Line numbers are from the 2025 forms ([2025 IT 1040 and schedules](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf); [2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)). Ohio has **no standard deduction** and no itemized deductions; it starts from federal AGI.

1. **Line 1, federal AGI** from federal Form 1040 line 11a. It must match federal AGI as defined in the Internal Revenue Code. The deductible half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions are already inside federal AGI. The federal qualified business income deduction has no effect on the Ohio return.
2. **Classify business income** on the **Ohio Schedule of Business Income** (formerly IT BUS). Business income arises from the regular course of a trade or business, from property integral to it, from a business liquidation (including goodwill), from certain sales of an ownership interest, and from compensation or guaranteed payments paid by a pass-through entity to an investor owning **20% or more** of it. Everything else is nonbusiness income. Apply the transactional or functional test; do not simply copy federal schedule totals ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)).
   - Line 10 is total business income. **Line 11** is the lesser of line 10 and federal AGI (IT 1040 line 1); if zero or negative, there is no deduction and no taxable business income.
   - **Line 12:** $250,000 for single, head of household, qualifying surviving spouse or married filing jointly; $125,000 for married filing separately ([2025 IT 1040 and schedules](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf)).
   - **Line 13, the business income deduction (BID):** the lesser of lines 11 and 12. It is carried to Schedule of Adjustments line 13.
3. **Schedule of Adjustments.** Additions (line 12 total, to IT 1040 line 2a) include non-Ohio state and local bond interest, Ohio pass-through entity tax not in federal AGI, and the **section 168(k) and 179 add-back** (line 9, see "Federal conformity and depreciation"). Deductions (line 47 total, to line 2b) include the BID, taxable Social Security (federal 1040 line 6b), certain railroad benefits, U.S. obligation interest, state and local refunds in federal AGI, the prior-year depreciation deduction (line 27), 529 contributions and uniformed services retirement income.
4. **Line 3, Ohio AGI** = line 1 plus line 2a minus line 2b.
5. **MAGI** (modified adjusted gross income) = Ohio AGI **plus** the BID. MAGI, not Ohio AGI, sets the exemption amount and most credit limits (MAGI worksheet in the instructions).
6. **Line 4, exemptions:** one for the taxpayer and one for the spouse on a joint return (each only if not claimed as someone else's dependent), plus one per dependent claimed on the federal return, times the amount for the client's MAGI (see "Figures by year").
7. **Line 5, Ohio income tax base** = line 3 minus line 4 (not below zero).
8. **Line 6, taxable business income** = the lesser of (Schedule of Business Income line 11 minus line 13) and IT 1040 line 5. **Line 7, taxable nonbusiness income** = line 5 minus line 6. So the exemptions reduce nonbusiness income first.
9. **Line 8a**, tax on line 7 from the nonbusiness brackets; **line 8b**, line 6 times 3% (Schedule of Business Income line 16); **line 8c** = 8a + 8b ([2025 IT 1040 and schedules](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf)).
10. **Line 9, nonrefundable credits** from the Ohio Schedule of Credits (retirement, senior, lump sum, child care, exemption, joint filing, earned income and others, see "Credits"). **Line 10** = line 8c minus line 9, not below zero. Nonresident credit (IT NRC) and resident credit (IT RC) also go through the Schedule of Credits.
11. **Lines 11 to 26:** add the IT/SD 2210 interest penalty (line 11) and unpaid use tax (line 12); subtract withholding (line 14), estimated and extension payments and carryforward (line 15) and refundable credits (line 16); add interest on late payment (line 21) to reach the amount due (line 22) or the overpayment (line 23).
12. **Then check the separate local taxes:** if the client lived in a taxing school district, an SD 100 is required; any city or village income tax is filed with the municipality or its administrator. See "When to refuse or refer".

## Figures by year

### Nonbusiness income tax brackets ([2025 IT 1040 instructions, page 18](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [Department annual tax rates](https://tax.ohio.gov/individual/resources/annual-tax-rates); [OBM Monthly Financial Report](https://archives.obm.ohio.gov/Files//Budget_and_Planning/Monthly_Financial_Report/2025-12-mfr.pdf))

**Tax year 2025**, all filing statuses, applied to IT 1040 line 7:

| Taxable nonbusiness income: more than | Up to | Tax |
| --- | --- | --- |
| $0 | $26,050 | None |
| $26,050 | $100,000 | $342.00 plus 2.75% of the amount over $26,050 |
| $100,000 | no limit | $2,394.32 plus 3.125% of the amount over $100,000 |

- The Department's example: taxable nonbusiness income of $68,050 2.75% of $42,000 is $1,155, plus $342 gives $1,497.
- Apply the schedule exactly as printed, or use the Department's calculator at tax.ohio.gov/taxcalculator. The printed base amounts do not run continuously: at $100,000 the second row gives $2,375.63, the third row starts at $2,394.32. Do not "correct" the table.

**Tax year 2026.**
- The Office of Budget and Management reports that under the FY 2026-2027 budget (HB 96), "beginning in 2026, there will be a single 2.75 percent income tax rate, eliminating the multiple tax rate brackets previously in Ohio law".
- The Department had not published the 2026 rate schedule (the zero-tax threshold and any base amount) on its site by 25 September 2026. Do not assume the 2025 base amount of $342 carries over. Before computing a 2026 return, take the schedule from the 2026 IT 1040 instructions or from R.C. 5747.02 as amended by HB 96.
- The **2026 IT 1040ES worksheet** still prints the 2025 brackets, including 3.125% above $100,000 ([2026 IT 1040ES worksheet](https://dam.assets.ohio.gov/image/upload/v1735926006/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf)). Using it for 2026 estimates overstates tax on nonbusiness income above $100,000, which is the safe direction for estimates only.

### Business income ([Department business income deduction page](https://tax.ohio.gov/individual/resources/businessincomededuction); [2025 IT 1040 and schedules](https://dam.assets.ohio.gov/image/upload/v1758139620/tax.ohio.gov/forms/ohio_individual/individual/2025/1040-bundle.pdf))

| Item | Tax year 2025 |
| --- | --- |
| Business income deduction, single, head of household, qualifying surviving spouse, married filing jointly | First $250,000 |
| Business income deduction, married filing separately | First $125,000 |
| Rate on taxable business income above the deduction | 3% |

- The deduction applies only to business income included in federal AGI, and is capped at federal AGI (Schedule of Business Income line 11).
- For 2026: the official pages checked for this Guide report no change to the deduction amounts or the 3% business rate. Confirm both in the 2026 instructions before filing a 2026 return.

### Personal and dependent exemptions ([2025 IT 1040 instructions, line 4](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [2026 IT 1040ES worksheet](https://dam.assets.ohio.gov/image/upload/v1735926006/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf))

**Tax year 2025**, per exemption, based on **MAGI** (Ohio AGI plus BID):

| MAGI | Exemption amount |
| --- | --- |
| $40,000 or less | $2,400 |
| $40,001 to $80,000 | $2,150 |
| $80,001 to $749,999 | $1,900 |
| $750,000 or greater | $0 |

- A dependent who can be claimed by someone else enters $0 on line 4.
- **2026 estimates:** the 2026 IT 1040ES worksheet uses $1,900 per exemption and says: "If line 3 of the worksheet above is $500,000 or greater, line 4 should be zero." Treat $500,000 as the 2026 estimate rule only; confirm the 2026 exemption table in the 2026 instructions.

### Credits ([2025 IT 1040 instructions, Schedule of Credits and worksheets](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

Tax year 2025. All are **nonrefundable**; unused amounts are lost unless the instructions say they carry forward.

- **Retirement income credit (line 2).** All of these must be true:
  - MAGI less exemptions is less than $100,000;
  - the client received income from a pension, profit-sharing or retirement plan (such as a traditional IRA or 401(k)), received on account of retirement, and included in Ohio AGI;
  - the client has never taken the Ohio lump sum retirement credit.

  Social Security and other amounts deducted on the Schedule of Adjustments (such as uniformed services retirement income) do not count. The maximum is $200 per return, from this table (joint filers use combined eligible retirement income):

| Retirement income in Ohio AGI | Credit |
| --- | --- |
| $500 or less | None |
| $501 to $1,500 | $25 |
| $1,501 to $3,000 | $50 |
| $3,001 to $5,000 | $80 |
| $5,001 to $8,000 | $130 |
| $8,001 or more | $200 |

- **Lump sum retirement credit (line 3).** For a total lump sum distribution on account of retirement from a qualified plan, included in Ohio AGI, with MAGI less exemptions under $100,000, never claimed before. Taking it bars the retirement income credit that year and in all future years.
- **Senior citizen credit (line 4):** $50 per return, if MAGI less exemptions is less than $100,000, the client was 65 or older at the end of the year, and the client has never taken the lump sum distribution credit.
- **Lump sum distribution credit (line 5):** for someone 65 or older with a total lump sum distribution from a qualified plan, MAGI less exemptions under $100,000, never claimed before. The credit is an age multiple times $50. Taking it bars the $50 senior citizen credit that year and in all future years.
- **Child and dependent care credit (line 6):** only if MAGI is less than $40,000 and the federal child and dependent care credit was claimed. Below $20,000 the credit equals the federal amount (Form 2441 line 9c); from $20,000 to under $40,000 it is 25% of Form 2441 line 11.
- **Exemption credit (line 9):** $20 per exemption claimed, if MAGI less exemptions is less than $30,000.
- **Joint filing credit (line 12).** All of these must be true:
  - the couple files jointly;
  - **each** spouse has at least $500 of qualifying income. Qualifying income is income in Ohio AGI other than interest, dividends and distributions, capital gains, and rents and royalties. Business income deducted as the BID, Social Security and other deducted amounts are not in Ohio AGI, so they do not qualify;
  - MAGI is less than $750,000.

  The credit is a percentage of the tax after the Schedule of Credits lines 2 to 9 (Schedule of Credits line 11), capped at $650, and a statement listing each spouse's qualifying income must be attached:

| MAGI less exemptions | Percentage of Schedule of Credits line 11 |
| --- | --- |
| $0 to $25,000 | 20% |
| $25,001 to $50,000 | 15% |
| $50,001 to $75,000 | 10% |
| $75,001 to $749,999 | 5% |

- **Ohio earned income credit (line 13):** 30% of the federal earned income credit, nonrefundable.
- **Campaign contribution credit (line 8):** repealed by HB 96; the instructions say it is not available after tax year 2025.
- **2026:** the Department had not published 2026 credit limits by 25 September 2026. The 2026 IT 1040ES worksheet lowers the exemption cut-off to $500,000; check whether the $750,000 limits on the joint filing credit also changed before using them for 2026.

### Federal conformity and depreciation ([Ohio conformity updates](https://tax.ohio.gov/wps/portal/gov/tax/individual/file-now/ohio-conformity-updates); [2025 IT 1040 instructions, Schedule of Adjustments lines 9 and 27](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

- **Conformity date.** The Department says: "On March 5th, 2026, Governor Mike DeWine signed Senate Bill 9 into law. This bill officially puts Ohio into conformity for tax year 2025 (filed in 2026)." This "includes conformity with the tax changes contained in the One Big Beautiful Bill Act (OBBBA) that impact Ohio taxation." The Department's table gives the conformity date for tax year 2025 as 5 March 2026 (prior effective date 7 March 2025).
- **Election (R.C. 5701.11).** Because the conformity bill passed after the 2025 year closed, a taxpayer may irrevocably elect to file 2025 using the Internal Revenue Code as it stood at year-end instead. It is all or nothing; provisions cannot be mixed. The prior version is elected by attaching the statement the Department prescribes. Filing normally under the 2025 instructions elects the current version.
- **Decoupling survives conformity.** Where Ohio decouples through Schedule of Adjustments add-backs and deductions, conformity legislation does not change those items unless they are amended or repealed.
- **Bonus depreciation and section 179 add-back (line 9).** Add back **5/6** of federal section 168(k) bonus depreciation, and 5/6 of section 179 expense above what section 179 would have allowed as it existed on 31 December 2002.
  - Use **2/3** instead of 5/6 for an employer that increased Ohio income tax withheld by at least 10% over the previous year.
  - Use **6/6** where the depreciation creates a federal net operating loss.
  - **No add-back** for an employer whose increase in Ohio withholding over the previous year is at least the total 168(k) and 179 expense, or for depreciation from a pass-through entity in which the taxpayer owns less than 5%.
- **Recovery (line 27).** Deduct, in equal amounts in consecutive later years: 1/5 of each prior 5/6 add-back (five years), 1/2 of each 2/3 add-back (two years), 1/6 of each 6/6 add-back (six years). An unused portion does not carry forward, except that in a year with an NOL, NOL carryback or NOL carryforward the deduction cannot be claimed and moves to the next year with no NOL. Only amounts actually added back on an earlier IT 1040 may be deducted, even if the asset has been sold.
- **2026:** no 2026 conformity statement was published by 25 September 2026. Check the conformity page before filing a 2026 return.

### Penalty, interest and estimated tax figures ([Department interest rates](https://tax.ohio.gov/individual/resources/interest-rates); [2025 IT/SD 2210](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf); [Department failure-to-file notice](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/individual/FailuretoFileNotice103019.pdf); [2026 IT 1040ES worksheet](https://dam.assets.ohio.gov/image/upload/v1735926006/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf))

| Item | Figure |
| --- | --- |
| Interest rate on unpaid tax, calendar year 2026 | 7% |
| Interest rate on unpaid tax, calendar year 2025 | 8% |
| Estimated payments needed if expected tax after credits, less Ohio withholding, is more than | $500 |
| Required annual estimate: lesser of current-year tax times | 90% |
| or prior-year tax (only if the prior-year return was filed on time) times | 100% |
| Each quarterly installment, cumulative share of the required amount | 25% |
| Late payment penalty | Double the interest rate |
| Late filing penalty, per month late | Greater of 5% of the tax due or $50 |
| Late filing penalty, maximum | Greater of 50% of the tax due or $500 |

- The late filing penalty applies "even if the late-filed return results in a refund". These penalty figures come from a Department notice dated 2019; confirm against R.C. 5747.15 before quoting one in writing.

### 2025 returns (due 15 April 2026, or 15 October 2026 on extension) ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

- Use the 2025 brackets (top rate 3.125%), the 2025 exemption table (cut-off $750,000) and the 2025 credits above.
- Other 2025 changes: the Ohio educator expense deduction rose to $300 per taxpayer; the home school expenses credit became $250 per qualifying student (it was per return); a new deduction for contributions to a pregnancy resource center; the IT NRS form is no longer used (see "Residency").
- Conformity for 2025 includes OBBBA (Senate Bill 9); a 2025 return filed earlier on the old Code may need review. An extended return is due 15 October 2026, with interest on unpaid tax from 15 April 2026.

## Residency, nonresidents and part-year residents ([2025 IT 1040 instructions, pages 13, 16 and 62](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

- **Resident** means domiciled in Ohio. Anyone with an abode in Ohio (owned or rented) is **presumed** to be a resident, and a temporary absence from that abode, however long, does not change it.
- **Part-year resident:** permanently moved into or out of Ohio during the year. They get the nonresident credit (IT NRC) for income earned while resident elsewhere, and the resident credit (IT RC) for non-Ohio income earned while an Ohio resident and taxed by another state.
- **Nonresident:** resident elsewhere all year; nonresident credit for income not earned or received in Ohio.
- **Contact periods.** A contact period is when the person has an abode outside Ohio, is away overnight from it, and spends any part of **two consecutive days** in Ohio (they need not sleep in Ohio). With **fewer than 213** contact periods, nonresidency must be shown "more likely than not"; with **213 or more**, by "clear and convincing" documentation.
- **Nonresident presumption (replaces the old affidavit).** From tax year 2025 the IT NRS form is no longer used; earlier years used the IT NRS, and before that the IT DA affidavit. The presumption is now claimed by checking the **Ohio Nonresident Statement** box on the IT 10 or IT 1040 (each spouse checks their own box). Once claimed, the Department cannot later treat the person as a resident for that year. All five criteria must be met:
  1. no more than 212 contact periods in Ohio;
  2. an abode outside Ohio on which no depreciation was claimed (not a vacation home, rental or other income property);
  3. no Ohio driver's license or state ID, surrendered to a motor vehicle bureau before the year began;
  4. no Ohio homestead exemption or owner-occupied property tax reduction;
  5. no Ohio in-state tuition received by the individual.
- **Deadline for the statement:** the 15th day of the 10th month after year-end (15 October for calendar years). This does not extend the return's due date. Part-year residents cannot use the presumption.
- **Resident credit (IT RC):** only for tax paid to another U.S. state or the District of Columbia on income also in Ohio AGI; not for city, foreign or territory taxes, not for states without an income tax, and not for wages earned in the five reciprocity states.

## Boundary and exception table ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [2025 IT/SD 2210](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf))

| Situation | Rule |
| --- | --- |
| Owner of 20% of an S corporation draws a W-2 salary | The wages are business income, eligible for the BID. Below 20% ownership, wages and guaranteed payments are nonbusiness income. |
| Spouse works for the other spouse's company and owns none of it directly or indirectly | Wages are nonbusiness income. Attribution under federal rules does not count as indirect ownership. |
| Schedule C profit is larger than federal AGI | BID and taxable business income are limited to federal AGI (Schedule of Business Income line 11). |
| MAGI is exactly $80,000 (2025) | Exemption is $2,150. The $1,900 band starts at $80,001. |
| MAGI is exactly $750,000 (2025) | No exemption, and no joint filing credit (it needs MAGI less than $750,000). |
| MAGI less exemptions is exactly $100,000 | No retirement income, lump sum or senior citizen credit (each needs less than $100,000). |
| Couple files jointly; one spouse has only business income and Social Security | No joint filing credit: that spouse has no qualifying income in Ohio AGI. |
| Client took the lump sum distribution credit in an earlier year | No senior citizen credit this year or later. |
| Kentucky resident whose only Ohio income is wages | No Ohio return. If they also have Ohio rental income, they file and report it. |
| Part-year resident who otherwise meets the five nonresident criteria | Cannot claim the nonresident presumption. |
| Expected tax after credits less withholding is exactly $500 | No estimated payments are required, and IT/SD 2210 line 8 stops the penalty. |
| Prior-year Ohio return was not filed on time | The 100%-of-prior-year safe harbor is unavailable; use 90% of current-year tax. |
| Federal NOL year with an unrecovered 5/6 depreciation add-back | The line 27 deduction waits until a year with no NOL, carryback or carryforward. |

## Worked cases ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [2025 IT/SD 2210](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf))

Amounts described as client facts are hypothetical inputs. Ohio rounds to the nearest dollar.

**Case 1: 2025, single sole proprietor, full-year resident.**

Client facts: Schedule C profit of $300,000 and no other income. After the deductible half of self-employment tax and a SEP contribution, federal AGI is $285,000. No Schedule of Adjustments items other than the BID. No dependents.
- Schedule of Business Income: line 10 is $300,000; line 11 is the lesser of that and federal AGI, $285,000; line 13 BID is $250,000.
- Ohio AGI: $285,000 minus $250,000 = $35,000.
- MAGI: $35,000 plus the $250,000 BID = $285,000, so one exemption of $1,900 (the Ohio AGI alone would wrongly suggest $2,400).
- Line 5: $35,000 minus $1,900 = $33,100.
- Line 6: the lesser of $35,000 (line 11 minus line 13) and $33,100 = $33,100. Line 7 nonbusiness income is zero.
- Tax: $33,100 times 3% = $993.

**Case 2: 2025, married filing jointly, both employed, one dependent.**

Client facts: wages of $90,000 and $30,000, joint bank interest of $2,000, federal AGI $122,000, no adjustments, no other credits.
- MAGI $122,000: three exemptions at $1,900 = $5,700. Line 5 and line 7: $116,300.
- Tax: 3.125% of $16,300 is $509.38; plus $2,394.32 gives $2,903.70, rounded to $2,904.
- Joint filing credit: each spouse has at least $500 of wages (interest does not count); MAGI is under $750,000; MAGI less exemptions is $116,300, so 5%. Credit: 5% of $2,904 = $145.20, rounded to $145.
- Tax after credits: $2,904 minus $145 = $2,759.

**Case 3: 2025, single retiree aged 70.**

Client facts: IRA and pension income of $40,000 received on account of retirement, taxable Social Security of $20,000, federal AGI $60,000. Never took a lump sum credit.
- Schedule of Adjustments deducts the $20,000 of Social Security. Ohio AGI and MAGI: $40,000, so the exemption is $2,400.
- Line 5 and line 7: $37,600. Tax: 2.75% of $11,550 is $317.63; plus $342 gives $659.63, rounded to $660.
- MAGI less exemptions is $37,600, under $100,000: retirement income credit $200 (retirement income of $8,001 or more) and senior citizen credit $50, together $250.
- Tax after credits: $660 minus $250 = $410.

**Case 4: 2026 estimated tax for a sole proprietor.**

Client facts: 2025 Ohio tax after credits of $3,000 on a return filed on time; expected 2026 tax after credits of $4,000; no Ohio withholding.
- Expected tax less withholding is more than $500, so estimates are required.
- Required annual amount: the lesser of 90% of $4,000 = $3,600 and 100% of $3,000 = $3,000, so $3,000.
- Each installment: 25% of $3,000 = $750, due 15 April, 15 June and 15 September 2026 and 15 January 2027.

**Case 5: 2025, snowbird with homes in Ohio and Florida.**

Client facts: lives in Florida most of the year and spends summers at an Ohio house; 150 contact periods in Ohio; Florida home not depreciated; Ohio driver's license surrendered in 2024; no homestead reduction on the Ohio house; no Ohio in-state tuition.
- All five criteria are met, so the client may check the Ohio Nonresident Statement box on the IT 10 or IT 1040, no later than 15 October 2026.
- If the client still held an Ohio driver's license, the presumption is unavailable. With fewer than 213 contact periods, the client can still file as a nonresident but must show nonresidency is more likely than not, with documents.

**Case 6: 2025, sole proprietor with bonus depreciation.**

Client facts: federal section 168(k) bonus depreciation of $60,000 on equipment; no section 179; no NOL; the client has no employees, so the withholding exceptions do not apply.
- Schedule of Adjustments line 9 add-back: 5/6 of $60,000 = $50,000 on the 2025 return.
- Line 27 deduction: 1/5 of $50,000 = $10,000 a year for tax years 2026 through 2030, provided none of those years has an NOL, NOL carryback or carryforward.

## When to refuse or refer

- **School district income tax (SD 100).** Only residents of a taxing school district for any part of the year owe it; working in a district without living there does not create it. Districts use either a traditional base or an earned income base. Look up the district and its rate in the SD 100 instructions or The Finder at tax.ohio.gov/Finder, and prepare the SD 100 separately. Do not guess a rate.
- **Municipal (city or village) income tax.** Not part of the IT 1040 or SD 100, and not creditable on the Ohio return. Refer to the municipality or its tax administrator for residence and workplace rules and rates.
- **Residency in doubt:** an Ohio abode with a claimed move, 213 or more contact periods, or a client who fails one of the five nonresident criteria.
- **Business or nonbusiness classification** that is unclear (a sale of an ownership interest, rental activity, mixed-use assets), since it moves income between the 3% rate with the BID and the nonbusiness brackets ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf)).
- **Pass-through entities:** IT 4738 electing entity tax, IT 4708 composite returns, IT K-1 credits and the non-Ohio entity tax add-back.
- **2026 returns** until the 2026 rate schedule, exemption table and credit limits are published.
- **The R.C. 5701.11 election** for 2025, or an amended 2025 return triggered by conformity.
- **NOL carrybacks** (Schedule IT NOL), multi-year depreciation histories with missing records, military servicemembers, assessments and appeals.

## Filing and payment ([2025 IT 1040 instructions, pages 6 to 9](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf); [2026 IT 1040ES worksheet](https://dam.assets.ohio.gov/image/upload/v1735926006/tax.ohio.gov/forms/ohio_individual/individual/2026/ites-instructions-fi.pdf); [2025 IT/SD 2210](https://dam.assets.ohio.gov/image/upload/v1762982566/tax.ohio.gov/forms/ohio_individual/individual/2025/itsd2210-fi.pdf))

- **Due date:** 15 April 2026 for 2025 returns. Returns for 2026 are due in April 2027; confirm the date in the 2026 instructions.
- **Extension:** Ohio has no extension form. It honours a federal extension: check the extension box and include a copy of the IRS extension or acknowledgment, or the extension confirmation number. The 2025 return is then due 15 October 2026. **An extension to file is not an extension to pay**: extension payments were due 15 April 2026, and interest runs on unpaid tax from then (penalties may also apply).
- **Estimated tax for 2026:** required if expected Ohio tax after credits, less Ohio withholding, is more than $500. Due 15 April, 15 June and 15 September 2026 and 15 January 2027. Payments apply only to the SSN on the coupon, so spouses unsure of their filing status should pay separately. A revised IT 4 raising withholding is an alternative.
- **Underpayment interest penalty (IT/SD 2210).** No penalty if payments by the due dates reach 90% of current-year tax, or 100% of prior-year tax where the prior-year return was filed on time, or if current-year tax less withholding is $500 or less. Otherwise the penalty is computed per quarter on each shortfall, at the statutory rate for the days late. Farmers and fishermen (at least 2/3 of gross income) may avoid it by filing and paying in full by 1 March.
- **Interest** on late tax runs from the unextended due date. **Late payment penalty** is double the interest rate; the **late filing penalty** is set out in the figures table.
- **Payment:** electronically at tax.ohio.gov/pay, or by check payable to "Ohio Treasurer of State" with the coupon. The Department cannot set up payment plans. Pay Ohio and school district tax separately.
- **Refund claims** generally within four years from the date of payment. An amended return is required within 90 days after the IRS finalises a change to federal AGI.

## Completion checklist ([2025 IT 1040 instructions](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/forms/ohio_individual/individual/2025/it1040-booklet.pdf))

- **Year:** brackets, exemption table and credit limits match the tax year; nothing from 2025 is used for 2026 without confirming it.
- **Residency:** each spouse's status is checked; Ohio Nonresident Statement box used only when all five criteria are met; IT NRC and IT RC attached where claimed.
- **Line 1** is federal AGI; filing status matches the federal return.
- **Schedule of Business Income:** 20% ownership test applied; line 11 capped at federal AGI; BID on Schedule of Adjustments line 13; entities listed in Part 4.
- **Schedule of Adjustments:** 168(k) and 179 add-back computed; prior-year 1/5, 1/2 or 1/6 deductions taken (unless an NOL year); Social Security deducted.
- **Exemptions** use MAGI, not Ohio AGI.
- **Credits:** conditions for each credit checked (MAGI less exemptions under $100,000; joint filing credit qualifying income per spouse with a statement attached).
- **Payments:** withholding schedule and statements attached; estimates and extension payments on line 15; IT/SD 2210 reviewed.
- **Local taxes:** school district residence and SD 100 considered; municipal tax referred out.

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
