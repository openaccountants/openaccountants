---
name: ky-income-tax
description: Use this skill whenever asked about Kentucky individual income tax. Trigger on phrases like "Kentucky income tax", "KY income tax", "Form 740", "KRS 141", "Kentucky flat tax". Kentucky has a flat 3.5% rate for TY2026 (was 4% for TY2025). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kentucky individual income tax (Form 740), tax year 2026

## Scope and who this is for

This Guide covers the Kentucky individual income tax return for **full-year Kentucky residents** (Form 740), including sole proprietors and owners of single-member LLCs that are disregarded for federal purposes. It is written for **tax year 2026** (returns due in 2027), with a dated section for **2025 returns**, which are still being filed on extension until 15 October 2026.

Out of scope, refer instead:

- Part-year residents and nonresidents: they file Form 740-NP, not Form 740.
- Residents of Illinois, Indiana, Michigan, Ohio, Virginia, West Virginia or Wisconsin who only had Kentucky wages withheld: Form 740-NP-R.
- Corporations, the limited liability entity tax (LLET) and pass-through entity returns.
- Local occupational license taxes (see When to refuse or refer). They are separate local taxes, not part of Form 740.

Official sources used throughout: the Kentucky Department of Revenue (DOR) 2025 Form 740 instruction packet (https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf), the DOR Form 740-ES instructions for 2026 estimated tax and the DOR individual income tax page (https://revenue.ky.gov/Individual/Individual-Income-Tax/Pages/default.aspx). The statute is KRS Chapter 141.

## Ask the client first

- Which tax year is this: 2025 or 2026? The rate and standard deduction differ.
- Was the person a Kentucky resident for the **whole** year? If not, stop: Form 740-NP.
- Filing status on the federal return, and, if married, did both spouses have income? (Kentucky lets spouses file separately on one combined return.)
- Federal AGI (Form 1040 line 11), and whether any federal return was filed at all.
- Age 65 or over, legally blind, or a Kentucky National Guard member on 31 December?
- Family size and modified gross income (for the filing test and the family size tax credit).
- Pension, IRA, 401(k) or annuity income? Any of it from the federal government, the Commonwealth of Kentucky or a Kentucky local government?
- Social Security or railroad retirement benefits in federal AGI?
- Interest from US government obligations, or from other states' municipal bonds?
- Self-employed: gross receipts, depreciation, Section 179 or bonus depreciation taken federally, and where the work is done (for local occupational tax)?
- Tuition paid to a college **located in Kentucky**, and was a federal American Opportunity or Lifetime Learning credit allowed?
- Kentucky withholding, estimated payments, and the prior year's Kentucky tax (for the estimated tax safe harbour)?

## The method, step by step

1. **Check the filing requirement.** A full-year resident must file if modified gross income exceeds the Chart A amount for the family size **and** Kentucky AGI exceeds the Chart B amount. For 2025, Chart A is $15,650 (family of one), $21,150 (two), $26,650 (three) and $32,150 (four or more). A self-employed person must file regardless of Chart B if gross receipts from self-employment exceed the Chart A amount for the family size. File anyway to get back Kentucky tax withheld. Source: [2025 Form 740 instructions](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf).
2. **Line 5: federal AGI.** Start from federal adjusted gross income, not federal taxable income. If no federal return was required, enter total income from all sources.
3. **Line 6: additions (Schedule M, Part I).** Main items: interest on bonds of other states and their subdivisions (Kentucky bonds are exempt); federal bonus depreciation and the increased Section 179 deduction (line 3, then recomputed on line 12); a federal net operating loss deduction (line 4, replaced by the Kentucky NOL); and other differences listed in the instructions. A child's income cannot be moved onto a parent's return: the federal election to report a child's investment income on the parent's return is "Not permitted" for Kentucky (differences chart, item 20). If the parent made that election federally (Form 8814), keep the child's income off the parent's Kentucky return and test whether the child must file a Kentucky return of their own. The instructions give no worked method for removing it from the parent's federal AGI, so refer if unsure.
4. **Line 8: subtractions (Schedule M, Part II).** Taxable state income tax refunds included in federal AGI (line 7); interest on US government obligations, but not Fannie Mae, Ginnie Mae or Freddie Mac securities that are merely guaranteed (line 8); the pension income exclusion (line 9); Social Security and railroad retirement benefits included in federal AGI (line 10); Kentucky depreciation (line 12); active duty military pay (line 13); other subtractions (line 14).
5. **Line 9: Kentucky AGI** = line 5 + line 6 − line 8.
6. **Line 10: deduction.** Standard deduction or Kentucky itemized deductions (Schedule A), whichever is larger. If one spouse itemizes, the other must itemize too.
7. **Line 11: taxable income** = line 9 − line 10.
8. **Line 12: tax** = taxable income × the flat rate for the year. There are no brackets; every filing status uses the same rate.
9. **Credits.** Nonrefundable credits: personal tax credits (Schedule ITC, Section B, line 17), family size tax credit (lines 20 and 21), education tuition tax credit (line 23, Form 8863-K), child and dependent care credit (line 24), business incentive credits and the credit for tax paid to other states (Schedule ITC, Section A).
10. **Payments and balance.** Kentucky withholding from Schedule KW-2, estimated and extension payments, refundable credits, then penalties and interest (line 34) and the amount owed or refunded.

## [Figures by year](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

| Item | 2025 returns | 2026 returns | Source |
| --- | --- | --- | --- |
| Flat rate | 4% | 3.5% | 2025 Form 740 instructions; 2026 Form 740-ES instructions; 2026 withholding formula |
| Standard deduction (per return; per spouse on a combined separate return) | $3,270 | $3,360 | 2025 instructions; DOR announcement of 4 September 2025 |
| Pension income exclusion (per taxpayer) | $31,110 | Not yet published on a 2026 form; DOR's current page still uses $31,110 | 2025 instructions; DOR individual income tax page |
| Personal tax credits | $40 each for age 65+ and for blindness; $20 Kentucky National Guard | Same credits shown on the 2026 Form 740-ES worksheet | DOR individual income tax page; 2026 Form 740-ES |
| Family size tax credit ceiling on MGI (family of four or more) | $42,760 | 2026 table not yet published; DOR prints the 2025 table in the 2026 Form 740-ES | 2026 Form 740-ES instructions |

**2026 rate.** DOR applies 3.5% for 2026 in the Form 740-ES worksheet ("Multiply line 7 by 3.5%"), the 2026 withholding formula and its payroll page ("The Kentucky Withholding Tax rate will be 3.5% for tax year 2026"). Kentucky's rate cuts are made by acts of the General Assembly. This Guide could not reach the Legislative Research Commission site on 25 September 2026 to confirm the text of the act that set 3.5%, or whether any cut applies for 2027. Before using a 2027 rate, check the 2027 Form 740-ES and the 2027 withholding formula when DOR publishes them.

**2027 standard deduction.** DOR announced on 11 September 2026 that the 2027 standard deduction is $3,470. Use it only for 2027 planning.

## [Federal conformity and the One Big Beautiful Bill Act](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

- Kentucky uses the Internal Revenue Code **as of a fixed date**. HB 775 moved that date from 31 December 2023 to 31 December 2024 for individual and corporate income tax (KRS 141.010(21)). Federal changes made after the reference date "shall not apply for purposes of Chapter 141 unless adopted by the General Assembly."
- DOR states for 2025: "Recent federal income tax changes were enacted after Kentucky's conformity date … these federal changes do not apply to Kentucky returns. Items such as qualified tips, overtime income, and car loan interest are not deductible on the Kentucky return." Social Security remains exempt under KRS 141.019(1)(e).
- For 2026, no later conformity date was found on DOR's site as of 25 September 2026. Treat the 31 December 2024 date as current and check the "What's New" page of the 2026 Form 740 packet when it is published.
- **Credits that are a percentage of a federal credit.** The Kentucky child and dependent care credit is a percentage of the federal Form 2441 credit. For 2026, that federal credit includes the P.L. 119-21 increase to IRC §21, which Kentucky has not adopted. Do not take 20% of it until the 2026 line 24 instructions confirm the base (see the credits section).
- **Some post-2024 federal changes sit inside federal AGI.** The tips, overtime and car loan interest deductions come after federal AGI, so they never reach line 5. Other P.L. 119-21 changes reduce business income on Schedule C or Schedule E, and so are already inside the federal AGI that Form 740 starts from. Depreciation is covered below. Another example is the federal deduction for domestic research or experimental expenditures under the new IRC §174A: "there shall be allowed as a deduction any domestic research or experimental expenditures". It applies to amounts paid or incurred in tax years beginning after 31 December 2024, which is after Kentucky's conformity date. If a Schedule C or E includes a §174A deduction or another P.L. 119-21 benefit, Kentucky income may need a Schedule M adjustment to reverse it. Check the Schedule M instructions for the year, and refer the case if they give no line for it.
- **Depreciation is permanently decoupled.** For property placed in service after 10 September 2001, Kentucky depreciation follows IRC Section 168 as in effect on 31 December 2001, so no bonus depreciation. For property placed in service on or after 1 January 2020, the Kentucky Section 179 limit is $100,000 and the investment phase-out does not apply. Recompute on a "Kentucky" Form 4562, add back federal depreciation on Schedule M line 3 and subtract Kentucky depreciation on line 12. Gains and losses on disposal use Kentucky basis.
- The federal qualified business income deduction is taken after federal AGI, so it never reaches Form 740, which starts from federal AGI. Self-employed health insurance, the deductible half of self-employment tax and SEP/SIMPLE/solo 401(k) deductions reduce federal AGI and flow through.
- **Home office.** A self-employed person's home office deduction is taken on Schedule C, so it is already inside the federal AGI entered on line 5. The Schedule M lines in the 2025 instructions include no separate home office adjustment, so the federal conditions decide it. Under IRC §280A(c)(1), that part of the home must be "exclusively used on a regular basis" in one of three ways: as the principal place of business, as a place where patients, clients or customers meet the taxpayer in the normal course of business, or as a separate structure used in the business.

## [Exclusions, deductions and credits: the conditions](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

**Pension income exclusion (Schedule M line 9).** For 2025 it is "100 percent of taxable retirement benefits or $31,110, whichever is less." It covers pension and retirement income paid under a written plan: pensions, annuities, IRAs, 401(k) and similar plans, Roth conversions, death benefits and disability retirement benefits. It is **per taxpayer**; each spouse computes their own, even on a joint return. If the total is more than $31,110 and any of it is from the federal government, the Commonwealth of Kentucky or a Kentucky local government, or is supplemental US railroad retirement, complete **Schedule P**: service before 1 January 1998 can make more than $31,110 exempt.

**Social Security and railroad retirement.** Fully exempt. Subtract the amounts included in federal AGI.

**Military pay.** All military pay of active duty members of the US Armed Forces, reserve components and the National Guard is exempt (KRS 141.019). Active duty pay is subtracted on Schedule M line 13.

**Standard deduction versus itemizing.** Kentucky itemized deductions differ from federal. The following are **not deductible** for Kentucky: medical and dental expenses, state income taxes, local income taxes, real estate taxes, personal property taxes, and casualty and theft losses. Married taxpayers filing separately on a combined return (Filing Status 2) enter the standard deduction in both columns. On a joint return only one standard deduction is allowed.

**Filing Status 2.** Married couples who both had income may file separately on one combined return, whatever they did federally. DOR says this "usually results in a lower tax than Filing Status 3", mainly because each spouse gets a standard deduction.

**Personal tax credits.** Kentucky has **no general personal credit** for every taxpayer. The credits are $40 if 65 or over, $40 if legally blind (so $80 if both), and $20 for a Kentucky National Guard member (military reserves are not eligible). Status is tested on 31 December. They are nonrefundable.

**Family size tax credit (KRS 141.066).** A nonrefundable percentage of tax for low incomes. Modified gross income (MGI) is the **greater of** federal AGI (plus non-Kentucky municipal bond interest and lump-sum pension distributions not in federal AGI) or Kentucky AGI (plus those lump-sum distributions). Family size counts you, your spouse if married and living in the same household, and qualifying children; the maximum is four. For 2025 the credit is 100% of tax at MGI up to $15,650 (one), $21,150 (two), $26,650 (three) or $32,150 (four or more), falling in bands to nothing above $42,760 for a family of four or more. Read the percentage from the band table in the Schedule ITC or Form 740-ES instructions; do not interpolate.

**Education tuition tax credit (KRS 141.069, Form 8863-K, line 23).** The credit is "25% of the allowable federal credit":

- American Opportunity credit: capped at $625 for each qualifying student.
- Lifetime Learning credit: capped at $500 per return.

All of these conditions apply:

- Only **undergraduate** expenses count.
- The institution must be **physically located in Kentucky**.
- A federal credit must have been allowed, using the federal qualification rules.
- The credit is nonrefundable and limited to tax.
- Any unused credit carries forward for up to five years. Form 8863-K must have been completed for the year the credit arose.

**Child and dependent care credit (line 24).**

- **2025 returns:** the credit is 20% of the federal credit from Form 2441, line 11 ("Multiply this amount by 20 percent (.20)"). It is also available to someone who had no federal filing requirement but would have qualified: complete Form 2441 and write "did not meet federal filing requirements" on it.
- **2026 returns: check before applying 20%.** P.L. 119-21 raised the federal applicable percentage in IRC §21 for tax years beginning after 31 December 2025. The federal rate now starts at 50%, falling to a floor of 35%, where it used to start at 35% and fall to 20%. Kentucky follows the Internal Revenue Code only as of 31 December 2024 (see the conformity section). So the 2026 Form 2441 credit includes a federal increase that Kentucky has not adopted. For a lower-income family, 20% of that figure could overstate the Kentucky credit by as much as 50/35. Do not simply apply 20% to the 2026 federal credit. Read the line 24 instructions in the 2026 Form 740 packet when DOR publishes it. They may require the federal credit to be recomputed under the §21 percentages in force before 2026 (35% falling to 20%). Until DOR says, treat the 2026 amount as unconfirmed.

**Credit for tax paid to other states (Schedule ITC).** Residents report all income wherever earned. The credit is the lesser of the Kentucky tax on the double-taxed income and the other state's tax. Withholding by another state is not a Kentucky payment.

## [Boundary and exception table](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

| Situation | Treatment |
| --- | --- |
| Moved into or out of Kentucky during the year | Not Form 740; use Form 740-NP |
| State income tax refund included in federal AGI | Subtract it (Schedule M line 7). It is not an addition |
| Interest on another state's municipal bonds | Add it (line 1). Kentucky bonds are exempt |
| Fannie Mae, Ginnie Mae or Freddie Mac interest | Taxable; only direct US obligations are subtracted |
| Retirement income of exactly $31,110 (2025) | Whole amount excluded; Schedule P not needed |
| Retirement income above $31,110 with Kentucky, federal or Kentucky local government service | Complete Schedule P; the exclusion may exceed $31,110 |
| Tips, overtime or car loan interest deducted federally for 2025 | No Kentucky deduction |
| 2026 child and dependent care credit | Federal credit includes the P.L. 119-21 §21 increase (50%, floor 35%). Check the 2026 line 24 instructions before taking 20% |
| Federal §174A research expensing or another post-2024 change inside Schedule C or E | Already in federal AGI; may need a Schedule M adjustment. Check the year's instructions or refer |
| Parent elected federally to report a child's investment income | Not permitted for Kentucky |
| Federal bonus depreciation or Section 179 above the Kentucky limit | Add back and recompute Kentucky depreciation |
| Tuition at an out-of-state college, or graduate tuition | No Kentucky education credit |
| Family of five | Use the family-of-four-or-more line |
| Expected tax after withholding and credits is $500 or less | No estimated payments required |
| Local occupational tax withheld on the W-2 | Not a Kentucky payment; do not put it on line 31(a) |

## [Worked cases](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

**Case A: 2026, single, self-employed.** Federal AGI $60,000 (all Schedule C, no Kentucky modifications, standard deduction). Taxable income $60,000 − $3,360 = $56,640. Tax $56,640 × 3.5% = $1,982.40. MGI $60,000 is above every family size band, so no family size credit.

**Case B: the same facts on a 2025 return.** $60,000 − $3,270 = $56,730. Tax $56,730 × 4% = $2,269.20.

**Case C: 2025, single retiree aged 67.** Private pension $40,000 and taxable Social Security $17,000; federal AGI $57,000. Subtract the pension exclusion $31,110 (no government service, so no Schedule P) and Social Security $17,000: Kentucky AGI $8,890. Less $3,270 = $5,620 taxable. Tax $5,620 × 4% = $224.80, less the $40 age credit = $184.80. MGI is the greater of federal AGI ($57,000) and Kentucky AGI, so there is no family size credit even though Kentucky AGI is low.

**Case D: 2025, married couple with no qualifying children (family size two), filing jointly.** MGI and Kentucky AGI $22,000. Taxable $22,000 − $3,270 = $18,730. Tax $18,730 × 4% = $749.20. MGI falls in the band over $21,996 and not over $22,842, so the credit is 80%: $599.36. Tax after the credit is $149.84.

**Case E: 2025 education credit.** Federal American Opportunity credit of $2,500 for an undergraduate at a Kentucky university. Kentucky tentative credit 25% = $625, which is also the per-student cap. It is then limited to the tax on line 22, and any excess carries forward. If the same student attended a college in Tennessee, there is no Kentucky credit.

**Case F: 2026 estimated tax.** Case A's taxpayer has no withholding and owed $2,269.20 for 2025 (Case B, a full 12-month return). The 2026 estimate is $1,982.40, which is more than $500, so payments are required. Required annual payment is the smaller of 90% × $1,982.40 = $1,784.16 and 100% of the 2025 tax ($2,269.20). That is $1,784.16, or $446.04 per quarterly voucher. The 110% rule does not apply because 2025 Kentucky AGI was not over $150,000.

## When to refuse or refer

- Part-year or nonresident: Form 740-NP.
- Schedule P cases (government pension with service before 1998), lump-sum 10-year averaging (Form 4972-K) or farm income averaging.
- Business incentive credits, pass-through entity tax credits, the LLET or Kentucky Schedule K-1 adjustments.
- Schedule C or E amounts shaped by post-2024 federal changes (for example §174A research expensing) where the year's Schedule M instructions give no line to reverse them.
- Kentucky net operating loss, excess business loss (Form 461-K) or passive loss (Form 8582-K) recomputations.
- **Local occupational license taxes.** Many Kentucky cities and counties levy their own occupational license tax on wages and net business profits. These are administered locally, not by DOR, and are not claimed on Form 740 ("Local government occupational, license or income tax must not be included on line 31(a)"). Send the person to the city or county tax office where the work is done. Do not quote local rates from memory.
- Any 2027 rate question until DOR publishes 2027 forms.

## [Filing, payment, estimated tax and penalties](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

**Due dates.** A calendar-year 2025 return must be "postmarked or submitted electronically no later than April 15, 2026." The same rule puts the 2026 return on 15 April 2027. Confirm this on the 2026 packet.

**Extensions.** Kentucky allows up to six months to file, which puts an extended 2025 return on 15 October 2026. A federal automatic extension (Form 4868) is honoured: attach a copy to the Kentucky return. You can also file Form 740EXT, which needs a reasonable cause; "inability to pay is not an acceptable reason." An extension is **not** an extension to pay. Interest runs from the original due date, and a payment can be sent with the Form 740EXT voucher. Combat zone service defers filing and payment until 12 months after service ends.

**Estimated tax (KRS 141.305, Form 740-ES).** Estimated tax may be required for anyone who can expect more than $5,000 of income with no Kentucky withholding. No payment is required if the estimated tax after withholding and credits is $500 or less. Otherwise, pay enough by withholding and instalments to cover the smaller of:

- 90% of the 2026 tax; or
- 100% of the 2025 tax, from a 12-month return.

If Kentucky AGI for 2025 was more than $150,000 ($75,000 if married filing separately for 2026), use 110% instead of 100%. The 740-ES adds: "This rule does not apply to farmers."

**Farmers and fishermen.** If at least two-thirds of gross income for 2025 or 2026 is from farming or fishing:

- The 90% safe harbour becomes 66 2/3% of the 2026 tax ("substitute 66 2/3% for 90%").
- The 110% rule for higher incomes does not apply.
- They can either pay all the estimated tax by 15 January 2027, or file the 2026 return and pay in full by 1 March 2027.

There is no estimated tax requirement if the person had no Kentucky liability for a full 12-month 2025 year. Instalments for 2026 are due 15 April, 15 June and 15 September 2026, and 15 January 2027. The annualized income method (Form 2210-K) is available for uneven income.

**Penalties and interest.**

| Item | Rule |
| --- | --- |
| Underpaid estimated tax | May apply if the amount owed is more than $500. Compute on Form 2210-K, line 34(a) |
| Late payment | 2% of the tax due per 30 days or part, capped at 20%, minimum $10. Not assessed if at least 75% of the tax was paid on time |
| Late filing | 2% of the tax due per 30 days or part, capped at 20%, minimum $10 |
| Interest | Unpaid tax accrues interest from the original due date at **9% for 2026** and **10% for 2025** (the Form 2210-K instructions give 10 percent for calendar year 2025 and 9 percent for 2026). [DOR's 2026 notice](https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx) confirms that unpaid tax "will accrue interest at the rate of 9 %" under KRS 131.183(2)(a)2. Its separate base "tax interest rate" of 7% is not the rate charged on unpaid tax |
| Waiver | Penalties, but not interest, may be reduced or waived for reasonable cause |

**Other points.**

- Enclose Schedule KW-2 to get credit for withholding.
- Amended returns use Form 740 with the amended box checked, within four years of the due date.
- A final IRS audit determination must be reported to DOR within 180 days.

## [Completion checklist](https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf)

- [ ] Full-year resident confirmed; correct year and rate (2025: 4%; 2026: 3.5%).
- [ ] Filing requirement tested (Chart A, Chart B and the self-employment rule).
- [ ] Line 5 is federal AGI, not federal taxable income.
- [ ] Schedule M: other-state bond interest added; state refund, US obligations, Social Security, military pay subtracted.
- [ ] Pension exclusion computed per taxpayer; Schedule P if over the cap with government service.
- [ ] Depreciation and Section 179 recomputed under Kentucky rules; no federal changes after 31 December 2024 applied, including any inside Schedule C or E (for example §174A).
- [ ] Child and dependent care credit: 20% of Form 2441 line 11 for 2025; for 2026, base confirmed against the 2026 line 24 instructions (no 20% of the P.L. 119-21 enhanced credit without DOR's say-so).
- [ ] No child's income reported on the parent's Kentucky return.
- [ ] Standard deduction or Kentucky itemized deductions (no state or local tax, real estate tax or medical deductions).
- [ ] Personal credits only for 65+, blind or Kentucky National Guard.
- [ ] Family size credit tested on MGI (greater of the two measures).
- [ ] Form 8863-K only for undergraduate study at a Kentucky institution; caps applied; carryforward recorded.
- [ ] Withholding from Schedule KW-2 only; no local occupational tax or other-state withholding included.
- [ ] Penalties and interest considered; extension copy attached.
- [ ] 2026 estimated tax vouchers set up if the 2026 estimate is more than $500.
- [ ] Local occupational license tax obligations referred to the locality.

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
