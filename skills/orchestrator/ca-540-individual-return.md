---
name: ca-540-individual-return
description: Tier 2 content skill for preparing California Form 540 (Resident Income Tax Return) for US sole proprietors and single-member LLCs who are California residents. Covers tax year 2025 California personal income tax including the Schedule CA (540) decoupling adjustments from federal AGI, California's non-conformity with OBBBA bonus depreciation and section 174 R&E expensing, the nine-bracket rate structure (1% through 12.3% plus the 1% Mental Health Services Tax surcharge above $1M), standard and itemized deductions, California tax credits (renter's credit, CalEITC, young child tax credit), SDI/VPDI deduction, and California's own AMT. Defers estimated tax to ca-estimated-tax-540es, SMLLC franchise tax to ca-smllc-form-568, and health coverage mandate to ca-form-3853-coverage. MUST be loaded alongside us-tax-workflow-base v0.1 or later and us-federal-return-assembly. California full-year residents only.
jurisdiction: US-CA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# California Form 540: resident sole proprietors and single-member LLC owners

This Guide is written for tax year 2026, with a dated section for 2025 returns that are still being filed on extension. It covers the California resident income tax return (Form 540) of a full-year California resident who reports a business on federal Schedule C, directly or through a single-member LLC that is disregarded for federal tax. It starts from a finished federal return and turns it into California taxable income, tax, credits and payments.

**Status of the figures (checked 25 September 2026).** California indexes its brackets, standard deduction, exemption credits and credit income limits every year. The Franchise Tax Board (FTB) has **not yet published the 2026 indexed amounts**. Its own 2026 estimated-tax instructions tell taxpayers to use the 2025 standard deduction and the 2025 tax table for now. Every indexed amount below is therefore a **2025** amount and is labelled 2025. Use it for 2025 returns and for 2026 estimates; replace it with the 2026 amount once the FTB publishes the 2026 Form 540 booklet. Rates set in statute (the 1% Behavioral Health Services Tax and the 7% AMT rate) do not change. [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)

**Scope limits.** This Guide does not cover part-year residents or nonresidents (Form 540NR), Form 568 for the LLC itself, or multi-state apportionment. It also leaves the health coverage penalty (form 3853) and registered domestic partner (RDP) recalculations to their own FTB instructions.

## Ask the client first

- Was the client a California resident for all of the tax year? Which filing status did they use federally? California normally follows the federal filing status. The exceptions are RDPs and some military or nonresident spouses.
- The complete federal return: Form 1040 with Schedules 1, 1-A, A, C, D, E and SE, and Forms 4562, 8995 and 8889, plus W-2s showing California wages and SDI withheld.
- A fixed-asset register for every asset still being depreciated, with the **California** basis and California depreciation to date. Include anything expensed federally under §179 or bonus depreciation, the cost of all §179 property placed in service in the year, and any research and experimental costs.
- The business's gross receipts from all trades or businesses, including pass-through shares. This decides whether business items are left out of the California alternative minimum tax (AMT).
- Health savings account (HSA) contributions (including the employer's, from W-2 box 12 code W), HSA interest, dividends and gains, and any HSA distributions.
- Rent paid on a California home for the year, and whether anyone else can claim the client as a dependent. Also: children's ages at year-end, both spouses' SSNs or ITINs, and investment income. These are needed for the renter's credit, CalEITC and the Young Child Tax Credit (YCTC).
- California estimated payments made, with dates, prior-year overpayment applied, and prior-year California AGI and tax. Also any California NOL, excess business loss or credit carryovers.
- Social Security, California lottery winnings, mortgage and home-equity loan balances, charitable gifts and property taxes.

## The method, step by step

1. **Confirm scope and year.** Full-year resident, Schedule C or disregarded single-member LLC, and the tax year. For 2026 amounts that are not yet published, carry the labelled 2025 amount and flag it.
2. **Start from federal AGI** (Form 1040 line 11). Form 540 line 13 takes federal AGI. Every difference between federal and California law goes on Schedule CA (540). [Form 540 instructions](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
3. **Schedule CA (540), Part I (income).** Column B is **subtractions** and column C is **additions**. Enter the business depreciation difference from form 3885A on Section B, line 3 (business income), the HSA items, Social Security and the other items in the tables below. Form 540 line 14 takes Part I line 27 column B, and line 16 takes column C. [Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)
4. **Schedule CA (540), Part II (deductions).** Compare the California itemized total with the California standard deduction and use the larger. On a married/RDP filing separately return, both spouses must choose the same method. Federal deductions taken **below** federal AGI never reach the California return. These are the qualified business income (QBI) deduction on Form 1040 line 13a and the Schedule 1-A deductions on line 13b (tips, overtime, car loan interest and the senior deduction). No Schedule CA entry is needed for them. [2025 Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf)
5. **Taxable income** is Form 540 line 17 minus line 18 (line 19). Up to $100,000, use the FTB tax table. Above that, use the tax rate schedule for the filing status. [Form 540 instructions, line 31](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
6. **Credits.** Subtract the exemption credits (line 32), reduced if federal AGI is above the limit. Then apply the nonrefundable credits, including the renter's credit (line 46). [Form 540 instructions](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
7. **Other taxes.** Work through Schedule P (540) for the AMT (line 61), and add the Behavioral Health Services Tax if taxable income is over $1,000,000 (line 62). [Form 540 instructions, line 62](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
8. **Refundable credits and payments.** Claim CalEITC, YCTC and the Foster Youth Tax Credit on form 3514, then apply withholding and estimated and extension payments. Work out any penalty for underpaying estimated tax (form 5805). [Form 3514 booklet](https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html)
9. **File and pay** by the dates below, and set up the next year's estimated payments.

## California does not follow the federal changes (2025 and 2026)

For tax years beginning on or after 1 January 2025, California conforms to the Internal Revenue Code **as of 1 January 2025**, with continuing differences. It does **not** conform to the One Big Beautiful Bill Act (OBBBA, enacted 4 July 2025). The old statement that California conformity stops at 1 January 2015 is out of date. Before filing a 2026 return, check the FTB conformity page for any 2026 legislation. [Schedule CA (540) instructions, General Information](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html); [FTB Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf)

| Federal item | California treatment | Where |
|---|---|---|
| Bonus depreciation, §168(k), including OBBBA's permanent 100% for property acquired after 19 January 2025 | Not allowed at **any** percentage. There is no California phase-down rate to apply. Recompute California depreciation without bonus depreciation. [Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) | form 3885A, then Schedule CA Section B line 3 |
| §179 expensing | Limit **$25,000**, reduced dollar for dollar once §179 property placed in service in the year costs more than **$200,000**. No §179 for off-the-shelf software or qualified real property. The deduction also cannot exceed business income (not less than zero); any disallowed amount carries forward to the next year on the 3885A worksheet. The California basis is reduced by the California §179 amount. [Form 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) | form 3885A Part II |
| Domestic research costs, §174A (OBBBA expensing), and §174 | California follows §174 **as it read on 1 January 2015**. It does not follow the TCJA amortization rule or the OBBBA expensing rule. [Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) | form 3885A |
| §168(n) 100% election for qualified production property (placed in service after 4 July 2025) | Not allowed. [Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) | form 3885A |
| QBI deduction (§199A) and Schedule 1-A deductions | Not allowed. They sit below federal AGI, so no Schedule CA entry is needed. [Form 1040 lines 13a–13b](https://www.irs.gov/pub/irs-pdf/f1040.pdf) | None |
| HSA contribution deduction | Not allowed. Enter the federal deduction on Section C line 13, column B. Enter the employer contribution (W-2 box 12 code W) on line 1h, column C. [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) | Schedule CA Part I |
| HSA earnings | Taxable in the year earned: interest on line 2 and dividends on line 3, column C. A non-qualified distribution that is taxed federally is **not** taxed by California (line 8f, column B). [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) | Schedule CA Part I |
| Educator expenses | Not allowed (line 11, column B). [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) | Schedule CA Part I |
| Moving expenses | Allowed for all taxpayers, not only the armed forces (form 3913). [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) | Section C line 14 |
| Excess business loss, §461(l) | California applies its own limit: net business losses over **$313,000** (**$626,000** joint) for 2025, figured on form 3461. A disallowed amount carries over as an excess business loss, not as an NOL. [Schedule CA instructions, line 8p](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) | Line 8p |

**Common subtractions (column B).** Social Security and equivalent Tier 1 railroad retirement benefits are fully excluded: enter the taxable federal amount from line 6b in column B. California lottery winnings are excluded; other states' lottery winnings are not. [Schedule CA instructions, lines 6 and 8b](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)

**NOL suspension (2024 to 2026).** For taxable years beginning in 2024, 2025 and 2026, California suspends the NOL carryover deduction. The suspension does not apply to taxpayers with net business income or modified AGI of less than $1,000,000, or with disaster loss carryovers. An NOL can still be computed and carried forward during the suspension. [Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html)

## Deductions: California rules that differ

| Item | California rule (2025 forms) |
|---|---|
| Standard deduction | **$5,706** single or MFS; **$11,412** MFJ, HOH or qualifying surviving spouse/RDP. If the client can be claimed as a dependent, use the dependents worksheet (minimum **$1,350**). [Form 540 instructions, line 18](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html) |
| State income tax, SDI, sales tax | **Not deductible.** This includes State Disability Insurance (SDI) withheld from wages. Remove it on Schedule CA Part II line 5a, column B. |
| Federal SALT limit | California has no limit. For 2025 the federal limit is **$40,000** (**$20,000** MFS), but it is reduced when modified AGI is over **$500,000** (**$250,000** MFS), though not below **$10,000** (**$5,000** MFS). On line 5e, column C, add back the amount the federal return **actually** disallowed. The 2026 federal amounts are different; use the 2026 IRS Schedule A instructions. Real property taxes stay deductible. [IRS Schedule A instructions (2025)](https://www.irs.gov/instructions/i1040sca) |
| Mortgage interest | California keeps the **$1,000,000** acquisition-debt limit (**$500,000** MFS), not the federal **$750,000** (**$375,000** MFS). It also allows interest on up to **$100,000** (**$50,000** MFS) of home-equity debt. Adjust on line 8, column C. |
| Charitable gifts | Limited to **50%** of federal AGI. Conservation easements are limited to **30%**. |
| Personal casualty and theft losses | Allowed (California did not follow the federal suspension). Disaster losses are deductible only if the client itemizes. |
| Miscellaneous deductions subject to the **2%** floor | Allowed (California did not follow the federal suspension). Examples are unreimbursed employee expenses and tax preparation fees. Enter them on Part II lines 19 to 22. |
| High-income limitation | If federal AGI is over **$252,203** (single or MFS), **$378,310** (HOH) or **$504,411** (MFJ or QSS), reduce itemized deductions by the smaller of **6%** of the excess or **80%** of the deductions subject to the limit. |

**2026 federal Schedule A changes.** OBBBA changes to federal itemized deductions that start in 2026 include a floor on charitable gifts, a cap on wagering losses and a cap on itemized deductions for top-bracket taxpayers. They flow into Schedule CA column A. Because California generally does not conform to OBBBA, expect them to need column B or C adjustments; confirm when the 2026 FTB Schedule CA instructions are published. [FTB Pub. 1001](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf)

Source for the rows without their own link: [Schedule CA (540) instructions, Part II](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html). The client may itemize for California while taking the standard deduction federally, and the other way round. If they itemize only for California, attach a federal Schedule A completed for that purpose. [Form 540 instructions, line 18](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)

## Tax, exemption credits and the Behavioral Health Services Tax

### 2025 tax rate schedules (use when taxable income is over $100,000)

| Over | But not over | Single or MFS (Schedule X): tax is | Of the amount over |
|---|---|---|---|
| 0 | $11,079 | 1.00% | 0 [2025 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf) |
| $11,079 | $26,264 | $110.79 + 2.00% | $11,079 |
| $26,264 | $41,452 | $414.49 + 4.00% | $26,264 |
| $41,452 | $57,542 | $1,022.01 + 6.00% | $41,452 |
| $57,542 | $72,724 | $1,987.41 + 8.00% | $57,542 |
| $72,724 | $371,479 | $3,201.97 + 9.30% | $72,724 |
| $371,479 | $445,771 | $30,986.19 + 10.30% | $371,479 |
| $445,771 | $742,953 | $38,638.27 + 11.30% | $445,771 |
| $742,953 | and over | $72,219.84 + 12.30% | $742,953 |

For **MFJ or qualifying surviving spouse/RDP (Schedule Y)**, the rates are the same and the bracket tops are $22,158, $52,528, $82,904, $115,084, $145,448, $742,958, $891,542 and $1,485,906. For **head of household (Schedule Z)**, the bracket tops are $22,173, $52,530, $67,716, $83,805, $98,990, $505,208, $606,251 and $1,010,417. Read the base tax for each bracket from the FTB schedule. [2025 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf)

**Exemption credits (2025).** Each personal exemption is **$153**: one for single, MFS or HOH, and two for MFJ or QSS. Each blind or age-65 exemption adds **$153**, and each dependent is **$475**. [2025 Form 540](https://www.ftb.ca.gov/forms/2025/2025-540.pdf) The credits shrink when federal AGI is over **$252,203** (single or MFS), **$504,411** (MFJ or QSS) or **$378,310** (HOH). Divide the excess by **$2,500** (**$1,250** MFS), round up, and multiply by **$6**. That amount comes off each exemption. [Form 540 instructions, line 32](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)

**Behavioral Health Services Tax** (formerly the Mental Health Services Tax). It is an extra **1%** on taxable income **in excess of $1,000,000**, reported on Form 540 line 62. Taxable income of exactly $1,000,000 owes none. The threshold is the same for every filing status. It is **not** doubled for a joint return, and the filing-status and joint-return bracket rules do not apply to it. Credits cannot reduce it. The top marginal rate on income above $1,000,000 is therefore **13.3%**. [R&TC §17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043); [Form 540 instructions, line 62](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)

**Alternative minimum tax (Schedule P (540)).** The tentative minimum tax is **7%** of AMTI above the exemption. The AMT is the excess of that tax over the regular tax. [R&TC §17062](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17062) A **qualified taxpayer** has aggregate gross receipts of **less than $1,000,000** from all trades or businesses they own or have an interest in. That taxpayer leaves out of AMTI all income, adjustments and preferences from any trade or business. The test is **$1,000,000** for every filing status; it does not become $2,000,000 on a joint return. For most small sole proprietors, differences in business depreciation therefore create no California AMT. The 2025 exemptions are **$92,749** (single or HOH), **$123,667** (MFJ or QSS) and **$61,830** (MFS). The exemption is reduced by **25%** of AMTI above **$347,808**, **$463,745** or **$231,868**. [Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html)

## Credits

| Credit (2025) | Who qualifies | Amount |
|---|---|---|
| Nonrefundable renter's credit (line 46) | Paid rent on a California principal residence for at least half the year, on property that was not tax exempt. California AGI must be **$53,994 or less** (single or MFS) or **$107,987 or less** (MFJ, HOH or surviving spouse). The client did not live with someone who can claim them as a dependent, and neither spouse received a property tax exemption for the year. [FTB renter's credit](https://www.ftb.ca.gov/file/personal/credits/nonrefundable-renters-credit.html) | **$60** single or MFS; **$120** MFJ, HOH or surviving spouse |
| CalEITC (refundable, form 3514) | Earned income of at least $1 and not more than **$32,900**. Age 18 or older, or has a qualifying child. Valid SSN or ITIN for everyone on the claim. Lived in California more than half the year. Cannot be claimed as another taxpayer's qualifying child, and cannot be claimed as another taxpayer's dependent unless the client has a qualifying child. MFS filers must meet all of these: a qualifying child lived with them for more than half the year, **and** either they lived apart from their spouse/RDP for the last 6 months of the year, or they are legally separated under a written separation agreement or decree of separate maintenance and did not live in the same household as their spouse/RDP at the end of the year. [FTB CalEITC eligibility](https://www.ftb.ca.gov/file/personal/credits/caleitc/eligibility-and-credit-information.html) | Up to **$302** with no children, **$2,016** (1), **$3,339** (2), **$3,756** (3 or more) |
| CalEITC investment-income test | Not allowed if investment income is more than **$4,814**. [Form 3514 booklet](https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html) | None |
| Young Child Tax Credit (refundable) | Qualifies for CalEITC and has a qualifying child **under 6** at the end of the year. The credit starts to shrink once earned income passes **$27,425** and is gone at **$32,901**. A client with zero or negative earned income can still qualify if net losses and wages are each no more than **$35,640**. [Form 3514 booklet](https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html); [FTB YCTC](https://www.ftb.ca.gov/file/personal/credits/young-child-tax-credit.html) | Up to **$1,189** per return |

For a self-employed client, earned income for CalEITC is Schedule C profit (Schedule 1 line 3) **minus** the deductible part of self-employment tax (Schedule 1 line 15). It is not Schedule C profit alone. [Form 3514 booklet, Worksheet 3](https://www.ftb.ca.gov/forms/2025/2025-3514-booklet.html) Most business credits are limited: from 2024 to 2026 they cannot reduce net tax by more than **$5,000,000**. The limit does not apply to the Low-Income Housing Credit or the PTE elective tax credit. The renter's credit, CalEITC, YCTC and exemption credits are not business credits, so the limit does not touch them. [Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html)

## Payroll SDI on the client's W-2 wages

The employee SDI withholding rate is **1.2%** for 2025 and **1.3%** for 2026. From 1 January 2024 all wages are subject to SDI, with no wage limit and no annual maximum. [EDD rates and withholding](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/) SDI is **not** deductible on the California return (see the deductions table). A sole proprietor's own Schedule C profit is not wages for SDI.

## Boundaries and exceptions

| Situation | Treatment |
|---|---|
| Taxable income exactly $1,000,000 | No Behavioral Health Services Tax. It applies only in excess of $1,000,000. [R&TC §17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043) |
| MFJ with $1,050,000 taxable income | Tax of $500 on $50,000 (the threshold is not doubled) |
| Renter's credit, single, California AGI exactly $53,994 | Qualifies ("or less"). $53,995 does not. [FTB renter's credit](https://www.ftb.ca.gov/file/personal/credits/nonrefundable-renters-credit.html) |
| Business gross receipts $999,999 compared with $1,000,000 | Below $1,000,000, business items are excluded from AMTI. At $1,000,000 they are included. [Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html) |
| §179 property placed in service costs $225,000 or more | California §179 limit is nothing: $25,000 minus the cost over $200,000. Below that, the deduction is still capped at business income (not less than zero). [Form 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) |
| Prior-year California AGI over $150,000 ($75,000 MFS) | The prior-year safe harbor for estimated tax becomes 110% of prior-year tax. [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html) |
| Current-year California AGI of $1,000,000 or more ($500,000 MFS) | No prior-year safe harbor. Estimates must be based on the current year's tax. |
| Married, spouse itemizes on a separate return | This spouse must itemize too, even if the standard deduction is larger. [Form 540 instructions, line 18](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html) |

## Worked cases

**Case 1: ordinary return, single (2025 schedule).** California taxable income is **$150,000**, federal AGI is below the exemption-credit limit and there are no other credits. The amount over the bracket start is $150,000 − $72,724 = $77,276. Multiply by 9.30% to get $7,186.67, then add $3,201.97 for **$10,388.64**, entered as **$10,389** on line 31. Subtract the **$153** exemption credit: tax is **$10,236**. [2025 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf)

**Case 2: §179 over the California limit (2025).** Machinery costing **$210,000** was placed in service in 2025 and expensed in full federally. Schedule C business income before §179 is at least **$15,000**, so the business-income cap does not bite. The California §179 limit is $25,000 − ($210,000 − $200,000) = **$15,000**. The remaining **$195,000** of California basis is depreciated on form 3885A under California rules, with no bonus depreciation. The Schedule CA Part I Section B line 3, column C addition is the federal deduction minus the California §179 amount and California depreciation. If the cost had been **$500,000**, the California §179 limit would be nothing. [Form 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html)

**Case 3: Behavioral Health Services Tax.** A single filer has taxable income of **$1,200,000**. The tax is 1% × $200,000 = **$2,000**, on top of the regular tax. A married couple filing jointly with **$1,050,000** owes **$500**. [Form 540 instructions, line 62](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)

**Case 4: SDI is not deductible (exclusion).** A client with a side W-2 job earned **$40,000** of wages in 2026, so **$520** of SDI was withheld at 1.3%. If that SDI is in federal Schedule A state and local taxes, remove it on Schedule CA Part II line 5a, column B. [EDD rates](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/); [Schedule CA instructions, line 5a](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)

**Case 5: 2026 estimated tax.** The required annual payment is **$10,000**. Pay **$3,000** by 15 April 2026, **$4,000** by 15 June 2026, nothing on 15 September 2026, and **$3,000** by 15 January 2027. [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)

**Case 6: HSA (exclusion).** A client deducted a **$4,300** HSA contribution federally and earned HSA interest. Enter $4,300 on Schedule CA Section C line 13, column B, and the interest on line 2, column C. A later non-qualified distribution that is taxed federally is subtracted on line 8f, column B. [Schedule CA instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)

## When to refuse or refer

- Refer the client if they were not a California resident for the whole year, or a spouse was a nonresident on a joint return (Form 540NR is required).
- Refer RDP returns that need the RDP adjustments worksheet (FTB Pub. 737), and community-property splits.
- Refer business gross receipts of $1,000,000 or more when there are preference items (full Schedule P AMT), and NOL use when income is $1,000,000 or more (suspension rules, form 3805V).
- Refer assets without California depreciation history (the California basis cannot be rebuilt from the federal Form 4562 alone), research costs under the 1 January 2015 version of §174, or any excess business loss.
- Do not state a 2026 bracket, standard deduction, exemption credit or credit income limit as final until the FTB publishes it. Give the labelled 2025 amount and say it will change.
- Refer if California enacts conformity legislation for the tax year after these sources were checked. Recheck the FTB conformity page first.

## Filing and payment

**2026 returns.** The return is due **15 April 2027**. [Form 540 instructions](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html) California grants an **automatic six-month extension to file**, with no form needed, but the extension does **not** extend the time to pay. [FTB extension to file](https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html)

**2026 estimated tax (Form 540-ES).** The installments are **30%** by 15 April 2026, **40%** by 15 June 2026, no third installment for 15 September 2026, and **30%** by 15 January 2027. Estimates are required if the client expects to owe at least **$500** (**$250** MFS) after withholding and credits. The required annual payment is the smaller of **90%** of the 2026 tax or **100%** of the 2025 tax, including AMT. Use **110%** of the prior-year tax if 2025 California AGI was over **$150,000** (**$75,000** MFS). There is no prior-year option if 2026 California AGI is **$1,000,000** or more (**$500,000** MFS). Filing the 2026 return by 31 January 2027 and paying in full replaces the fourth installment. [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)

**Electronic payment.** Once a client makes an estimate or extension payment over **$20,000**, or files an original return with total tax over **$80,000**, all later payments must be electronic. A non-electronic payment then carries a **1%** penalty. [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html)

## 2025 returns still open (dated section)

A 2025 return was due **15 April 2026**. The automatic extension to file runs to **15 October 2026**, but payment was due **15 April 2026**; use form 3519 or Web Pay for extension payments. [FTB due dates](https://www.ftb.ca.gov/file/when-to-file/due-dates-personal.html) The penalties are:

- Late payment: **5%** of the unpaid tax, plus one-half percent for each month or part of a month it stays unpaid. The FTB presumes reasonable cause if **90%** of the tax was paid by 15 April 2026. [Form 540 instructions, interest and penalties](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
- Late filing (after 15 October 2026): the maximum total penalty is **25%** of the unpaid tax. For a return more than 60 days late, the minimum is the smaller of **$135** or the balance due. [Form 540 instructions, interest and penalties](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
- Interest compounds daily and cannot be waived. A one-time abatement of a timeliness penalty is available.

Use the 2025 figures in this Guide. The 2025 SDI rate was 1.2%. [EDD rates](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/)

## Completion checklist

- [ ] Resident all year; filing status matches federal, or the exception is documented.
- [ ] Form 540 line 13 equals federal AGI (Form 1040 line 11).
- [ ] Schedule CA Part I: column B subtractions and column C additions tie to support (form 3885A, HSA, Social Security, lottery).
- [ ] No QBI or Schedule 1-A deduction carried into California.
- [ ] California §179 recomputed with the $200,000 phase-out and the business-income cap (carry forward any excess); no bonus depreciation; California asset basis records updated. [Form 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html)
- [ ] Itemized deductions: SDI and state income tax removed, mortgage and home-equity limits applied, charity capped, high-income limitation checked.
- [ ] Tax from the table (taxable income $100,000 or less) or the rate schedule; exemption credits reduced if federal AGI is over the limit. [Form 540 instructions](https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html)
- [ ] Behavioral Health Services Tax checked when taxable income is over $1,000,000; AMT gross-receipts test documented. [Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html)
- [ ] Renter's credit, CalEITC, YCTC and Foster Youth Tax Credit tested against the conditions, not only the income limits.
- [ ] Payments, extension payments and estimated-tax penalty reconciled; 2026 installments scheduled at 30/40/0/30.
- [ ] Any 2025 indexed amount used for 2026 is flagged for replacement.

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
