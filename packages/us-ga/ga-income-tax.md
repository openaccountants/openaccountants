---
name: ga-income-tax
description: "Georgia Individual Income Tax Return (Form 500) for sole proprietors and single-member LLCs.   Covers the flat 5.19% rate (tax year 2025), Georgia taxable income computation from federal AGI,   standard deduction, dependent exemption, and estimated tax. Trigger: taxpayer is a Georgia   resident or has Georgia-source income."
version: "0.1"
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia individual income tax (Form 500), including sole proprietors

## Scope and who this is for ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download))

This Guide covers the Georgia individual income tax return, **Form 500**, for **tax year 2026** (returns filed in 2027). It has a dated section for **2025 returns**. It is for residents, part-year residents and nonresidents with Georgia income, including sole proprietors and single-member LLC owners whose business profit reaches Georgia through federal adjusted gross income (AGI).

Figures are for tax year 2026 unless labelled 2025. The 2026 rate, standard deduction and dependent exemption come from **HB 463** (2026), which applies to taxable years beginning on or after 1 January 2026. The 2026 IT-511 booklet was not out on 25 September 2026, so rules found only in the 2025 booklet are labelled 2025.

It does **not** cover the pass-through entity's own return or the pass-through entity (PTE) tax election (see the Guide `ga-corporate-and-ptet`), corporate income or net worth tax, fiduciary returns (Form 501), employer withholding, or tax credits beyond those named here. See "When to refuse or refer".

**Who must file (2025 rules, [DOR residency filing requirements](https://dor.georgia.gov/residency-filing-requirements)).**
- **Full-year resident.** Must file if any of these is true:
  - they are required to file a federal return;
  - they have income taxable in Georgia but not federally;
  - their income exceeds the 2025 standard deduction for their filing status: $12,000 (single, head of household, qualifying surviving spouse or married filing separately) or $24,000 (married filing jointly).

  This applies "as long as your legal residence is Georgia, even if you are absent from or live outside the State temporarily".
- **Part-year resident** (a legal resident of Georgia for only part of the year). Must file if required to file a federal return, and completes Schedule 3.
- **Nonresident** who works in Georgia or has Georgia-source income (for example wages, Georgia lottery winnings, flow-through income or rents). Must file if required to file a federal return. The exception is a legal resident of another state whose only Georgia activity is working as an employee: they need not file if that pay does not exceed the lesser of five percent of their pay from all places or $5,000.
- **2026 thresholds** were not published by DOR at the time of writing; check the 2026 IT-511.

**Residency.** Form 500 Line 4 codes are full-year resident (lived in Georgia the entire year, "regardless of temporary living arrangements"), part-year resident and nonresident. DOR describes residency as "legal residence" (domicile); the statute (O.C.G.A. § 48-7-1) has more tests, so treat doubtful cases as referrals.

## Ask the client first

- **Which tax year?** 2026 has a new rate (4.99%), a higher standard deduction and a higher dependent exemption. 2025 uses 5.19%, a $12,000 or $24,000 standard deduction and a $4,000 dependent exemption ([HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download)).
- **Residency for the whole year.** Legal residence (domicile), move-in or move-out dates, and whether the spouse had the same residency all year. If not, you need Schedule 3 and a choice between joint and separate returns.
- **Federal filing status**, and whether the client itemized or took the standard deduction federally. Georgia follows that choice.
- **Federal AGI and what is in it:** Schedule C profit, wages, taxable pensions and IRA distributions, taxable Social Security, interest (including from other states' bonds and U.S. obligations) and capital gains.
- **Dates of birth** of the taxpayer and spouse, and any permanent disability date. These drive the retirement income exclusion (age 62, age 65) and the military retirement exclusion (under 62).
- **Military retirees under 62:** the amount of military retirement pay, and the client's **Georgia earned income** (wages and self-employment income).
- **Number of dependents**, including any **unborn dependents** (Line 7b). Georgia follows the federal rules for qualified dependents. On separate returns, only one spouse may claim a given dependent, decided under the prior federal rules.
- **The business:** was federal **bonus depreciation (section 168(k))** claimed this year or earlier, and has any bonus-depreciated asset been sold?
- **2026 only:** qualified overtime (full-time hourly employees only) and cash tips, with the employer's figures.
- **Pass-through entities.** Does the client own part of an entity that elected to pay Georgia tax at the entity level? If so, use `ga-corporate-and-ptet` for the entity side.
- **Other states.** Any income taxed by another state, plus a copy of that state's return (required for the credit).
- **Payments.** Georgia withholding, estimated payments (dates and amounts), the prior-year Georgia tax and any extension payment.
- **Surplus refund.** Were the 2024 and 2025 Georgia returns filed on time, and what was the 2024 tax on Form 500 Line 16?

## The method, step by step

Form 500 line numbers are from the 2025 return ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download)). Part-year residents and nonresidents skip Lines 9 to 14 and use Schedule 3 (step 9).

1. **Line 8, federal AGI.** Enter federal adjusted gross income from Form 1040, not federal taxable income.
   - A sole proprietor's Schedule C profit, the deduction for half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions are all inside federal AGI. They flow through with no Georgia entry.
   - The qualified business income deduction does not apply. In the booklet's words: "Georgia does not allow the 20% qualified business income deduction (I.R.C. Section 199A). However, since Georgia starts with Federal AGI, no adjustment is necessary on the Georgia return." ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download))
2. **Line 9, Schedule 1 adjustments.**
   - Additions include interest and dividends from non-Georgia municipal bonds. They also include adjustments for federal provisions Georgia has not adopted, such as section 168(k) bonus depreciation.
   - Subtractions include the retirement and military retirement exclusions, Social Security and Railroad Retirement in federal AGI, U.S. obligation interest, other states' income tax refunds, and Path2College 529 contributions up to $4,000 per beneficiary ($8,000 per beneficiary on a joint return) ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download)).
   - For 2026, Farmer Bridge Assistance Program and Assistance for Specialty Crop Farmers Program payments are excluded, "subject to certain conditions" ([DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates)); refer if these apply.
3. **Line 10, Georgia AGI** = Line 8 plus or minus Line 9.
4. **Line 11 or Line 12, deduction.** Georgia follows the federal choice:
   - If the client took the federal standard deduction, they must take the Georgia standard deduction.
   - If they itemized federally, or they are married filing separately and the spouse itemized, they must itemize on the Georgia return.
   - Georgia itemized deductions are federal Schedule A (Line 12a), less income taxes paid to other states and investment interest expense for producing income exempt from Georgia tax (Line 12b).
5. **Line 14, dependent exemption:** the total on Line 7c (Line 7a qualified dependents plus Line 7b unborn dependents) times $5,000 for 2026, or $4,000 for 2025. An unborn child born during the same year goes on Line 7a, not 7b. On separate returns, only one spouse may claim a given dependent. There has been no personal exemption for the taxpayer or spouse after 31 December 2023, so from tax year 2024 ([2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download)).
6. **Lines 15a to 15c, taxable income.**
   - **Line 15a** = Line 10 minus the deduction minus Line 14.
   - **Line 15b** is any Georgia net operating loss. For losses from 2018 onward, the NOL cannot exceed 80% of Georgia income before the NOL ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download)).
   - **Line 15c** is Georgia taxable income.
7. **Line 16, tax** = Line 15c times the flat rate (4.99% for 2026, 5.19% for 2025), rounded to the nearest dollar ([HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [HB 111](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download)).
8. **Credits.**
   - **Line 17, low income credit.** Available if federal AGI is under $20,000 and the client is not claimed, and not eligible to be claimed, as a dependent ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download)).
   - **Line 18, credit for tax paid to other states.** It covers only state (including DC) and U.S. local income tax imposed on net income, never foreign tax. The income must be taxable both in Georgia and in the other state. The other state's return must be attached, or the credit is refused.
   - **Line 19**, the Georgia eligible itemizer credit (2025; see "2025 returns"), and **Line 20**, IND-CR credits.
9. **Part-year residents and nonresidents: Schedule 3.**
   - **Columns:** A is income as if a full-year resident, B is income not taxable to Georgia, C is Georgia income; A = B + C.
   - **Line 9 ratio** = Line 8 Column C divided by Line 8 Column A ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download)). It cannot be negative and cannot exceed 100%. It is zero if Georgia AGI is zero or negative. It is 100% if the adjusted federal AGI is zero or negative.
   - **Lines 10 to 14:** Line 10 is the deduction (standard, or itemized less other-state income taxes); Line 11 is dependents times the exemption; Line 12 = Lines 10 + 11; Line 13 = Line 12 times the Line 9 ratio; Line 14 = Line 8 Column C minus Line 13, carried to Form 500 Line 15a.
10. **Payments and balance.** Withholding from W-2s and 1099s (Line 24), G2-A, G2-FL, G2-LP and G2-RP withholding (Line 25), estimated and extension payments (Line 26) and refundable credits (Line 27, electronic filing only) give the balance due or overpayment. Then add the Form 500 UET estimated tax penalty (Line 42), late filing and late payment penalties (Line 43) and interest (Line 44).

## Figures by year

### Rate, standard deduction and dependent exemption ([HB 463 of 2026](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [HB 111 of 2025](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download); [DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates))

| Item | Tax year 2025 | Tax year 2026 |
| --- | --- | --- |
| Flat rate on Georgia taxable income | 5.19% (HB 111) | 4.99% (HB 463) |
| Standard deduction, married filing jointly | $24,000 | $30,000 |
| Standard deduction, single, head of household or married filing separately | $12,000 | $15,000 |
| Dependent exemption, per dependent | $4,000 | $5,000 |
| Personal exemption for taxpayer or spouse | None | None |

- **How the rate got here.** HB 111 (2025) set 5.19% for 2025, with 0.10-point cuts each year from 2026 until the rate reached 4.99%. HB 463 (2026) replaced that path. The rate is 4.99% "for taxable years beginning on or after January 1, 2026". From 1 January 2027 it falls by 0.125 of a point each year until it reaches 3.99%.
- **Each future cut can be delayed.** A scheduled cut is delayed by one year for each year that any of these is true as of 1 December:
  - the Governor's revenue estimate for the next fiscal year is not at least 3 percent above the current year's estimate;
  - the prior fiscal year's net revenue collections were not higher than each of the three preceding years' collections;
  - the Revenue Shortfall Reserve does not exceed the projected revenue cost of the cut.

  The Office of Planning and Budget reports by 1 December each year; do not quote a 2027 rate before then.
- **Scheduled increases from 2027**, subject to the same delay tests: the joint standard deduction by $750 a year to $36,000; the single, head of household and married filing separately deduction by $375 a year to $18,000; the dependent exemption by $125 a year to $6,000.
- **Qualifying surviving spouse** used the single amount for 2025 ($12,000, per the 2025 booklet). HB 463 does not name this status, so confirm the 2026 amount in the 2026 booklet.
- **The 2026 Form 500-ES worksheet still prints the 2025 amounts** ($12,000, $24,000, $4,000). Use the HB 463 amounts for 2026 estimates ([2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download)).

### Retirement income exclusion ([2025 IT-511 booklet, Subtractions and page 24](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download))

| Taxpayer | Maximum exclusion, 2025 and 2026 | From 2027 (HB 463) |
| --- | --- | --- |
| Age 62 to 64, or under 62 and permanently disabled | $35,000 | $35,000 |
| Age 65 or older | $65,000 | $70,000 |

- **Each spouse qualifies separately.** A joint return can carry two exclusions, but only if each spouse meets the age or disability test in their own right. Jointly owned income is split 50/50. Otherwise, income belongs to the spouse who owns the item.
- **Disability route (under 62).** The taxpayer must be permanently disabled "to such an extent that they are unable to perform any type of gainful employment". The date of disability is required on the return.
- **What counts as retirement income:** interest, dividends, alimony, capital gains, other income, taxable IRA distributions and pensions, and rent and royalties. Earned income can make up **no more than $5,000** of the exclusion (2025 booklet, Schedule 1 page 2). Earned income includes wages, self-employment income, rental, royalty or partnership income subject to self-employment tax, and S corporation income where the taxpayer materially participated.
- **What does not count:**
  - Social Security and Railroad Retirement, which are already subtracted in full;
  - exempt interest and other income not taxable to Georgia;
  - income from lotteries, gambling or illegal sources.
- **Part-year residents and nonresidents** prorate the exclusion in two parts:
  - the earned portion, by Georgia-source earned income over total earned income;
  - the unearned portion, by Georgia-source unearned retirement income over total unearned retirement income.

  Both ratios are computed as if the taxpayer were a full-year resident.
- **The 2027 increase** applies only to the 65-and-older amount. HB 463 limits the $35,000 and $65,000 division to years "ending on or before December 31, 2026".

### Military retirement income exclusion ([2025 IT-511 booklet, Subtraction 2](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download))

- **Only for taxpayers under 62.** Up to $17,500 of military retirement income can be excluded.
- **A second $17,500 applies only** if the taxpayer has more than $17,500 of earned income in Georgia. The Schedule 1 worksheet stops if Georgia earned income is less than $17,501.
- **Limits.** The combined maximum is $35,000, and the exclusion cannot exceed the taxable military retirement received.
- **Each spouse qualifies separately.**
- **Part-year residents and nonresidents** can claim the base $17,500 against all the military retirement income they received. They can reach the extra $17,500 only through Georgia-source earned income.
- **From age 62,** the military-specific worksheet no longer applies. The general retirement income exclusion above covers "retirement income from any source" (HB 463 text of O.C.G.A. § 48-7-27(a)(5)(A)).

### Overtime and cash tips, 2026 to 2028 only ([HB 463, Section 2-4](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates))

Georgia did **not** adopt the federal deductions for tips and overtime from P.L. 119-21. It has its own, smaller exclusions, both starting with taxable years beginning on or after 1 January 2026:
- **Overtime** (taxable years beginning on or after 1 January 2026 and ending on 31 December 2028). Up to $1,750 of "qualified overtime compensation" (as defined in IRC section 225) received by a **full-time employee paid by an hourly wage**.
  - Salaried and part-time workers do not qualify.
  - Employers under the federal Railway Labor Act use the definition in their collective bargaining agreements.
- **Cash tips** (taxable years beginning on or after 1 January 2026). Up to $1,750 received in cash tips. Despite the name, HB 463 defines "cash tips" to include tips "paid in cash or charged", so card tips count, and, for an employee, tips received under a tip-sharing arrangement. The tips qualify only if:
  - they are paid voluntarily, are not negotiated, and the amount is set by the payer;
  - the occupation customarily and regularly receives tips and has a Treasury Tipped Occupation Code;
  - the occupation is not one excluded under IRC section 63.

Both paragraphs "stand repealed and reserved on December 31, 2028", and neither applies to 2025 returns. DOR had not published the 2026 Schedule 1 line for them at the time of writing.

### Federal conformity and bonus depreciation ([HB 1199 of 2026](https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download); [DOR federal tax changes](https://dor.georgia.gov/taxes/tax-rules-and-policies/income-tax-federal-tax-changes))

- **Conformity date.** HB 1199 was signed on 20 March 2026. It updates the Georgia definition of the Internal Revenue Code to federal law "enacted on or before January 1, 2026". Section 1 applies "to all taxable years beginning on or after January 1, 2025". So 2025 and 2026 returns start from an IRC that includes P.L. 119-21 ("OBBBA"), apart from the provisions HB 1199 lists.
- **The 2025 IT-511 booklet is out of date on this point.** It was printed before HB 1199. It says Georgia conforms to the IRC as of 1 January 2025 and has not adopted OBBBA.
  - For a 2025 return where an OBBBA change affects federal AGI, follow HB 1199.
  - Check DOR's federal tax changes page for guidance. At the time of writing, that page's latest section covered 2024.
- **Provisions Georgia treats as not in effect** include:
  - section 168(k), bonus depreciation;
  - section 174A, the new domestic research expensing;
  - section 163(h)(4), the federal car loan interest deduction;
  - section 179(d)(1)(B)(ii), section 179 for certain real property;
  - section 199.

  Georgia applies sections 163(j) and 174 as they stood before the 2017 federal act.
- **Below-the-line federal deductions** (QBI, the new federal tips, overtime and senior deductions, the federal standard deduction) never reach Georgia, which starts from federal AGI.
- **Bonus depreciation.** Georgia has not adopted "30%, 50%, and 100% bonus depreciation rules, I.R.C. Section 168(k)". Depreciation is computed one way for federal and another way for Georgia:
  1. Attach the federal Form 4562.
  2. Add back the federal depreciation on the other addition line.
  3. Compute Georgia depreciation, without 168(k), on Georgia Form 4562, and enter it on the other subtraction line.
  4. Attach a statement explaining the differences.

  When a bonus-depreciated asset is sold, the Georgia gain or loss differs from the federal one and needs its own adjustment.
- **Net operating losses (Georgia rules).** Losses from 2018 onward have no carryback and an unlimited carryforward, with the 80% limit based on Georgia taxable net income. Farm losses and certain insurance losses have their own carryback rules.

### Surplus refund: HB 1000, signed 20 March 2026 ([HB 1000](https://gov.georgia.gov/document/2026-signed-legislation/hb-1000/download); [DOR HB 1000 FAQs](https://dor.georgia.gov/2025-hb-1000-surplus-tax-refund-faqs))

- **Who qualifies:** an individual who filed Georgia returns for **both 2024 and 2025** by the due date of the 2025 return, including any extension. With an extension, that means by 15 October 2026.
- **Who is excluded:** nonresident aliens, estates and trusts, and anyone claimed as a dependent for 2024 unless they had 2024 earned income.

  HB 1000 does not exclude ITIN filers. DOR's FAQ answers "Maybe" for them: DOR sends ITIN filers a letter asking for more information to decide whether they qualify, and they reply through the Georgia Tax Center or by mail. So an ITIN filer's refund is not paid automatically.
- **Amount:** the lesser of the 2024 tax liability (2024 Form 500 Line 16, or Form 500EZ Line 4) and a cap by 2024 filing status: $250 single or married filing separately, $375 head of household, $500 married filing jointly. A 2024 liability of $0 means no refund.
- **Part-year residents and nonresidents** get the amount prorated by the 2024 Schedule 3 Line 9 ratio.
- **How it is paid.** For most filers, DOR credits the refund automatically once the 2025 return is filed; there is no claim form. ITIN filers must first answer DOR's letter (above). It is paid using the refund method on the 2025 return, after any offset against debts owed to the state, and carries no interest.
- **Tax treatment.** The refund is not taxable for Georgia. If it is included in federal AGI, subtract it on Schedule 1 (the line 12 adjustment). DOR's FAQ says it may be federally taxable if the client itemized, deducted state income tax and got a federal tax benefit from that deduction.

### Penalties and interest ([DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates))

| Penalty (individual income tax) | Rate | Maximum |
| --- | --- | --- |
| Late filing (O.C.G.A. § 48-7-57) | 5% of the tax not paid by the original due date, plus 5% for each additional month | 25% of the tax due |
| Late payment (§ 48-7-86) | 0.5% of the unpaid tax, plus 0.5% of the outstanding tax for each additional month | 25% of the tax due |
| Negligent underpayment (§ 48-7-86) | 5% of the underpayment | none stated |
| Fraudulent underpayment (§ 48-7-86) | 50% of the underpayment | none stated |
| Frivolous return (§ 48-7-57.1) | $1,000 | $1,000 |
| Underpayment of estimated tax (§ 48-7-120) | 9% per year of the underpayment (Form 500 UET) | none stated |

- The late filing and late payment penalties together cannot exceed 25% of the tax due on the return due date.
- **Interest** on late tax accrues monthly from the due date. For months from 1 July 2016, the rate is the Federal Reserve prime rate plus 3 percent a year. DOR reviews the rate each January.
- An extension to file does not extend the time to pay.

### 2025 returns (due 15 April 2026, or 15 October 2026 on extension) ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download))

- **Rates and amounts** are in the tables above. There is no overtime or tips exclusion for 2025.
- **Form 500EZ is discontinued** from 2025. Everyone files Form 500.
- **Georgia eligible itemizer credit (Line 19).** Up to $300 per taxpayer, for a full-year or part-year resident who itemized and either lived in Georgia 183 days or longer or was living in Georgia on the last day of the year. It cannot exceed the tax liability and cannot be carried forward.
- **Child and dependent care credit (credit code 202):** 50 percent of the federal credit.
- **Hurricane Helene subtractions** apply only to the extent the amount is in federal AGI (see "When to refuse or refer"). The crop insurance subtraction is 2025 only. The agricultural disaster relief payments subtraction runs for taxable years from 2025 through 2029, so it also applies in 2026.
- **Conformity:** see HB 1199 above. For 2025 the federal AGI starting point includes OBBBA, apart from the provisions Georgia decoupled from, even though the booklet says otherwise.

## Boundary and exception table ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download))

| Situation | Rule |
| --- | --- |
| Taxpayer turned 62 during the year | Uses the age-based retirement exclusion, not the military exclusion. The military worksheet asks "Are you under the age of 62?" |
| Taxpayer 61, disabled, can still do some paid work | No retirement exclusion through the disability route. The disability must prevent any type of gainful employment. |
| One spouse 66, the other 60 and not disabled | Only the 66-year-old claims an exclusion. The 60-year-old gets none. |
| Retiree with wages above the earned-income cap | Only $5,000 of the wages counts toward the exclusion. |
| Military retiree under 62 with Georgia earned income of exactly $17,500 | Base exclusion only. The extra amount needs more than $17,500 of Georgia earned income. |
| Hourly part-time worker with overtime in 2026 | No Georgia overtime exclusion (full-time hourly employees only). |
| Nonresident employee whose Georgia pay does not exceed the lesser of 5% of total pay or $5,000 | No Georgia return needed. |
| Estimated tax, prior-year return covered fewer than 12 months | The 100%-of-prior-year option on Form 500 UET is not available. Use 70% of the current year. |

## Worked cases ([HB 463](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download))

Amounts described as client facts are hypothetical inputs.

**Case 1: 2026, single sole proprietor, full-year resident.**

Client facts: federal AGI of $80,000, all of it Schedule C profit. No Schedule 1 adjustments, federal standard deduction, no dependents. The 2025 Georgia tax on a 12-month return was $3,000.
- Georgia AGI is $80,000. The standard deduction is $15,000, so taxable income is $65,000.
- Tax: $65,000 times 4.99% = $3,243.50, rounded to $3,244.
- Estimated tax: 100% of the prior year's tax is $3,000, and 70% of the current year's tax is $2,270.80. On Form 500 UET, the required annual amount is the lesser, $2,270.80.
- It is paid in four installments, due 15 April, 15 June and 15 September 2026 and 15 January 2027.
- Paying 100% of the 2025 tax ($750 a quarter) is the safe route, since the 2026 tax is unknown in April.

**Case 2: 2026, married filing jointly, one spouse 66 and one 63, both retired.**

Client facts: each spouse has a taxable pension of $60,000, and they have $20,000 of jointly owned interest. Taxable Social Security is $25,000. Federal AGI is $165,000. They took the federal standard deduction. Full-year residents, no dependents.
- Retirement income per spouse: the $60,000 pension plus half the interest ($10,000) = $70,000.
  - The 66-year-old's exclusion is capped at $65,000.
  - The 63-year-old's exclusion is capped at $35,000.
- Subtractions: Social Security of $25,000 plus retirement exclusions of $100,000.
- Georgia AGI is $40,000. The standard deduction is $30,000, so taxable income is $10,000.
- Tax: $10,000 times 4.99% = $499.

**Case 3: 2025 return, married filing jointly, military retiree aged 50.**

Client facts: $40,000 of military retirement pay and $60,000 of Georgia wages. The spouse has no income. Two dependents. Federal AGI is $100,000, and the couple took the federal standard deduction.
- Military exclusion: the base is $17,500. Georgia earned income ($60,000) is more than $17,500, so the extra $17,500 applies. The total is $35,000, which is within the $40,000 received.
- Georgia AGI is $65,000.
- Deductions: the 2025 standard deduction of $24,000, plus the dependent exemption of 2 times $4,000 = $8,000. Taxable income is $33,000.
- Tax: $33,000 times 5.19% = $1,712.70, rounded to $1,713.

**Case 4: 2025 return, single, moved into Georgia on 1 July 2025.**

Client facts: $100,000 of wages for the year (Schedule 3 Column A), of which $50,000 was earned after the move (Column C). No adjustments, federal standard deduction, no dependents.
- Schedule 3 Line 9 ratio: $50,000 / $100,000 = 50%.
- Line 12 is the $12,000 standard deduction. Line 13 is $12,000 times 50% = $6,000.
- Line 14: $50,000 minus $6,000 = $44,000 of Georgia taxable income.
- Tax: $44,000 times 5.19% = $2,283.60, rounded to $2,284.

**Case 5: surplus refund (HB 1000).**

Client facts: a full-year resident filing with a Social Security number, not claimed as anyone's dependent for 2024. Filed a 2024 return as head of household, with a 2024 Form 500 Line 16 tax of $300. Filed the 2025 return on 10 April 2026.
- Refund = the lesser of the $300 liability and the $375 head-of-household cap = $300.
- The refund is not Georgia income on the 2026 return.

## When to refuse or refer

- **Residency in doubt**, such as a home elsewhere but much of the year in Georgia, or an unproven mid-year change of domicile.
- **Pass-through entity tax elections.** The entity-level election and the owner's PTEADD adjustment are covered in `ga-corporate-and-ptet`.
- **2025 returns where an OBBBA change moved federal AGI** and the return followed the 2025 booklet's conformity statement. Check DOR's current guidance before filing or amending (Form 500X).
- **Multi-year bonus depreciation tracking** with no Georgia depreciation schedules, or a sale of a bonus-depreciated asset. Rebuild the Georgia Form 4562 history first, or refer.
- **Multistate business income:** apportionment, S corporation income where another state does not recognise the S election, and the subtraction for entity-level tax paid to another state (O.C.G.A. § 48-7-27(d)).
- **A nonresident's deferred compensation or stock options** earned in Georgia in an earlier year. Federal limits on state taxation of retirement income interact with the 5% or $5,000 test ([DOR residency filing requirements](https://dor.georgia.gov/residency-filing-requirements)).
- **Other tax credits** (IND-CR, Schedule 2, film, timber, rural hospital), which have preapproval and e-filing rules.
- **Hurricane Helene** crop insurance (2025) and disaster relief (2025 to 2029) subtractions, and disaster postponements.
- **Military personnel** serving outside the continental U.S. (special filing deadline), combat zone pay, and spouses of nonresident military personnel.
- **Assessments:** 45-day protest and appeal windows apply from 1 July 2025, and the Georgia Tax Court hears appeals from 1 July 2026.

## Filing and payment ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download); [Form 500 UET](https://dor.georgia.gov/document/document/beginning-or-after-january-1-2025-500-uet-underpayment-estimated-tax-individuals/download))

- **Due date:** 15 April (15 April 2026 for 2025; 15 April 2027 for 2026). Fiscal years: the 15th day of the fourth month after year-end.
- **Extension:** file with a copy of federal Form 4868 (or the IRS confirmation) by the extended federal due date, or use Georgia Form IT-303 if there is no federal extension. It does not extend the time to pay; pay by the original due date (Form IT-560 or the Georgia Tax Center) and report it on Line 26.
- **Electronic filing is required** if the return uses a series 100 tax credit, if payments are made by electronic funds transfer, or for a paid preparer whenever the federal return must be e-filed.
- **Attachments:** federal pages 1-2 and Schedule 1 if Line 8 is $40,000 or more or less than the W-2 total; federal Schedule A if itemizing; the other state's return for the other-state credit.
- **Estimated tax: who must pay.** Anyone who reasonably expects gross income to exceed the dependent exemptions plus estimated deductions plus $1,000 of income not subject to withholding, unless the employer withholds extra by agreement to cover it.
- **Estimated tax: due dates:** 15 April, 15 June, 15 September and 15 January of the next year. If the requirement is first met later in the year, fewer installments are due. Farmers and fishermen (at least two thirds of gross income) may instead file and pay in full by 1 March.
- **Underpayment penalty (Form 500 UET).** The required installment is the lesser of:
  - 100% of the prior year's tax, if the prior-year return covered 12 months, divided by the number of installments required for the year;
  - 70% of the current year's tax after credits, divided by the number of installments required for the year.

  The penalty is 9% a year on the shortfall. Three exceptions can remove it:
  - tax on the prior year's income at the current year's rates and exemptions;
  - paying at least 70% of the tax on annualized current-year income;
  - paying at least 90% of the tax on actual income for the 3, 5 and 8 month periods.
- **Payment.** Pay through the Georgia Tax Center (gtc.dor.ga.gov), or by check payable to the Georgia Department of Revenue with Form 525-TV (balance due) or Form 500-ES (estimates). Payment agreements of up to 60 months are available once every return has been filed.
- **Refund claims** must be made within three years from the later of the date the tax was paid or the return's due date, including extensions.

## Completion checklist ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download))

- **Year:** rate, standard deduction and dependent amounts match the tax year.
- **Residency:** Line 4 code is correct; Schedule 3 is used for part-year, nonresident and mixed-residency joint returns.
- **Line 8** is federal AGI, not federal taxable income.
- **Schedule 1:** additions (non-Georgia municipal interest, federal depreciation where 168(k) was claimed) and subtractions (Social Security, U.S. obligation interest, other-state refunds, Georgia depreciation) are entered.
- **Retirement and military exclusions** are computed per spouse, with ages, caps and earned-income conditions checked.
- **Deduction** choice matches the federal return; dependents are totalled on Line 7c (Line 7a plus unborn dependents on Line 7b).
- **Estimated tax:** Form 500 UET reviewed; exception box checked if used.
- **Attachments and signatures:** federal pages attached where required; both spouses and any paid preparer sign.

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
