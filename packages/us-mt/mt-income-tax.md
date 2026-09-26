---
name: mt-income-tax
description: Use this skill whenever asked about Montana individual income tax for self-employed persons, sole proprietors, or single-member LLCs. Trigger on phrases like "Montana income tax", "MT income tax", "Form 2", "Montana DOR", "MCA 15-30-2103".
version: "0.1"
jurisdiction: US-MT
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montana individual income tax (Form 2), including sole proprietors

## Scope and who this is for ([2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf))

This Guide covers the Montana individual income tax return, **Form 2**, for **tax year 2026** (returns filed in 2027). It has a dated section for **2025 returns**. It is for residents, part-year residents and nonresidents, including sole proprietors and single-member LLC owners.

Figures are for tax year 2026 unless labelled 2025. The 2026 rates and brackets come from **HB 337** (2025). The 2026 Form 2 and its instructions were not out on 25 September 2026, so rules found only in the 2025 instructions are labelled 2025.

It does **not** cover pass-through entity returns or the pass-through entity tax election, corporate tax, estate and trust returns (Form FID-3), or employer withholding.

**Who must file ([DOR filing requirements](https://revenue.mt.gov/taxes/individual-income-tax/filing-requirements)).** For tax years beginning after 31 December 2023:
- A resident or part-year resident, or a nonresident who received Montana source income, must file if they had a requirement to file a federal return.
- Someone with no federal filing requirement must still file if they have a Montana addition or subtraction.
- A return is also needed to claim the Montana earned income tax credit or the elderly homeowner/renter credit, and to get back Montana withholding or estimated payments.
- Anyone who incurred or reported losses (capital, passive or net operating losses) must file so that Montana can track them. DOR warns that "Unreported losses may lead to the disallowance of their use in future years."

**Residency ([DOR residency](https://revenue.mt.gov/taxes/individual-income-tax/residency)).**
- **Resident:** "You are a Montana resident if you are domiciled or maintain a permanent place of abode in Montana." A resident is taxed on all income, wherever earned.
  - DOR weighs many factors (driver's licence, voter registration, resident hunting or fishing licence, where the person has a home, gets mail and runs their business). The person need not meet all of them, and DOR's guidance has **no day-count test**.
- **Two homes:** if a person keeps a place of abode in Montana and in another state with "similar permanency characteristics", DOR looks at whether residency in one state was abandoned for the other "through affirmative actions".
- **Part-year resident:** a Montana resident at the start of the year who established residency elsewhere during the year, or the reverse. These people are **not** part-year residents:
  - snowbird retirees who stay Montana residents;
  - seasonal workers who do not establish residency;
  - students at out-of-state colleges who have not established residency elsewhere.
- **Nonresident:** neither of the above. Taxed only on Montana source income. That includes wages for work done in Montana, even for an out-of-state employer while working remotely in Montana.
- **Mixed residency (a box added on the 2025 Form 2):** a Montana resident filing jointly with a nonresident or part-year resident spouse. All of the resident's income, plus the other spouse's Montana source income, is taxed ([2025 Form 2 instructions, Residency Status](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf)).

## Ask the client first

- **Which tax year?** 2026 uses 4.7% and 5.65% with wider brackets; 2025 uses 4.7% and 5.9% with narrower ones. 2027 changes again ([HB 337, DOR](https://revenue.mt.gov/news/recent-news/HB-337)).
- **Residency for the whole year** for each spouse: domicile, homes in and out of Montana, move-in or move-out dates. Any change means Schedule II.
- **Federal filing status.** Montana requires the same status as the federal return. A married couple can file separately for Montana only if they file separately federally ([DOR tax simplification hub](https://revenue.mt.gov/montana-tax-simplification-resource-hub)).
- **The federal Form 1040:**
  - line 11b (AGI);
  - line 12e (standard or itemized deduction);
  - line 13a (qualified business income deduction);
  - line 13b (Schedule 1-A deductions: tips, overtime, car loan interest, enhanced senior deduction).
- **If the client itemized:** the state income tax deducted on Schedule A, and any pass-through entity tax or mineral royalty withholding deducted in business income.
- **Dates of birth** of taxpayer and spouse. They drive the 65-and-older subtraction and the elderly homeowner/renter credit, which starts at age 62.
- **Net long-term capital gains** (federal Schedule D lines 15 and 16) and qualified dividends, which Montana taxes as ordinary income.
- **Other states:** income taxed by another state and a copy of that state's return; any wages earned in North Dakota.
- **Montana-specific items:** U.S. obligation interest, other states' bond interest, 529, ABLE and medical savings account deposits, Railroad Retirement, military pay or retirement pay, and tribal reservation income.
- **Payments:** Montana withholding (W-2 box 17, 1099-R box 14, Montana K-1s), estimated and extension payments with dates, any overpayment applied, and last year's Form 2 line 10 tax (for the estimated-tax safe harbor).
- **Age 62 or older with household income under $45,000?** Ask about rent or property tax for the elderly homeowner/renter credit ([DOR elderly credit](https://revenue.mt.gov/property/property-tax-help/montana-elderly-homeowner-renter-credit)).

## The method, step by step

Form 2 line numbers are from the 2025 return ([2025 Form 2](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/2025_Montana_Individual_Income_Tax_Return_Form_2.pdf)). Since tax year 2024, Montana starts from **federal taxable income, without the qualified business income deduction** ([DOR tax simplification hub](https://revenue.mt.gov/montana-tax-simplification-resource-hub)). Montana has no standard deduction, itemized deductions, personal exemption or dependent exemption of its own.

1. **Line 1, federal AGI** from Form 1040 line 11b.
   - A sole proprietor's Schedule C profit is already inside it, as are the deductions for half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions.
   - A full-year resident has no separate Montana business schedule.
2. **Line 2 = Form 1040 line 12e plus line 13b.**
   - Line 12e is the federal standard deduction or federal itemized deductions. "You must use the same type of deduction taken on your federal return."
   - Line 13b is the Schedule 1-A total (qualified tips, qualified overtime, car loan interest and the enhanced senior deduction). The 2025 instructions say these "are included in the calculation of Montana taxable income".
   - **Line 13a is left out.** "Do not include the federal qualified business income deduction to determine your federal taxable income for Montana purposes." For a sole proprietor this is usually the largest difference from federal taxable income.
3. **Line 3** = line 1 minus line 2, not below zero.
4. **Line 4, additions (Schedule I, Part I, lines 1 to 6)** ([2025 Form 2 instructions, Schedule I](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf)):
   - interest and mutual fund dividends from bonds of other states and their localities;
   - recoveries of amounts that reduced Montana tax in an earlier year;
   - non-qualified withdrawals from a Montana medical savings account or first-time homebuyer account;
   - **state income tax deducted** federally, figured on Worksheet B. For an itemizer, only the part that does not take itemized deductions below the federal standard deduction is added, and it is figured after the federal SALT cap. Pass-through entity tax, composite tax and mineral royalty withholding deducted in business income are added in full;
   - expenses used to claim a Montana tax credit;
   - other coded additions: S corporation federal tax, farm and ranch risk management distributions, title plant depreciation, and the NOL transition carryforward.
5. **Line 5, subtractions (Schedule I, Part I, lines 8 to 23).** The main ones:
   - state income tax refunds included in federal taxable income;
   - interest on U.S. obligations (Treasury bills, notes, savings bonds). Interest on Ginnie Mae, Fannie Mae and Freddie Mac securities does **not** qualify;
   - active-duty military pay and the working military retiree subtraction (see "Retirement income");
   - deposits to Montana medical savings accounts (with earnings), 529 plans and ABLE accounts;
   - Tier I and Tier II Railroad Retirement benefits;
   - a business expense disallowed federally because a federal credit was claimed (for example wages reduced by the work opportunity credit). The instructions add: "Depreciation, depletion, and amortization deductions must be the same for federal and Montana income tax purposes."
6. **Line 6, the 65-and-older subtraction** (see "Retirement income").
7. **Line 7, Montana taxable income** = lines 3 plus 4, minus lines 5 and 6, not below zero.
8. **Tax (page 2).** Split taxable income into net long-term capital gains and Montana ordinary income, and tax each at its own rates (see "Figures by year").
   - Residents: the tax goes to line 8.
   - Nonresidents, part-year residents and mixed-residency filers: compute the tax as if resident, then apply the Schedule II ratios (step 10).
9. **Credits.** DOR applies them in this order ([DOR filing requirements](https://revenue.mt.gov/taxes/individual-income-tax/filing-requirements)):
   1. single-year nonrefundable credits (Schedule III, including the credit for tax paid to another state);
   2. nonrefundable credits that carry over;
   3. refundable credits: the Montana EITC (line 15), the elderly homeowner/renter credit (line 16, Schedule 2EC) and others on Schedule III.

   Nonrefundable credits cannot take tax below zero.
10. **Schedule II for nonresidents, part-year residents and mixed residency** ([2025 Schedule II](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/Form_2_2025_Schedule_II.pdf)).
    - **Ordinary income ratio (line 17)** = Montana source ordinary income (line 15) divided by everywhere ordinary income. Line 16 is Form 1040 line 9, less certain federal adjustments, less net long-term capital gains. The ratio is rounded to six decimal places and cannot exceed 1.000000.
    - **Line 19** = the page 2 ordinary income tax times that ratio.
    - **Capital gains ratio (line 22)** = Montana source net long-term capital gains divided by all net long-term capital gains. **Line 24** = the page 2 capital gains tax times that ratio.
    - **Line 25** = lines 19 plus 24, carried to Form 2 line 8.
    - A part-year resident includes in Montana source income **everything received while a resident**, plus Montana source income received while a nonresident.
    - A nonresident sole proprietor must complete **Form DE** first to apportion and allocate the business income. Residents do not complete Form DE.
    - Voluntary adjustments such as HSA or IRA contributions are not treated as related to Montana source income.
11. **Payments and balance.** Withholding, estimates, extension payment and refundable credits (lines 11 to 17) give the balance due or refund; penalties and interest go on Schedule IV.

## Figures by year

### Ordinary income rates ([HB 337, DOR](https://revenue.mt.gov/news/recent-news/HB-337); [MCA 15-30-2103](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0030/0150-0300-0210-0030.html); [DOR 2025 tax tables](https://revenue.mt.gov/taxes/tax-tables-and-deductions/2025))

Montana ordinary income is all taxable income that is not a net long-term capital gain, "and includes qualified dividends". Each rate applies only to the income inside its bracket.

| Filing status | 2025: 4.7% up to | 2025: 5.9% over | 2026: 4.7% up to | 2026: 5.65% over |
| --- | --- | --- | --- | --- |
| Single, married filing separately | $21,100 | $21,100 | $47,500 | $47,500 |
| Married filing jointly, qualifying surviving spouse | $42,200 | $42,200 | $95,000 | $95,000 |
| Head of household | $31,700 | $31,700 | $71,250 | $71,250 |

- **2026 brackets are fixed in the statute** (the version of MCA 15-30-2103 that "Terminates December 31, 2026"). They are not indexed.
- **2027 (HB 337):** 4.7% up to $65,000 (single and married filing separately), $130,000 (joint and surviving spouse) or $97,500 (head of household), and 5.4% above. The 2027 version of the statute then has DOR index the brackets by 1 November each year, from a June 2026 price base.

### Net long-term capital gains rates ([2025 Form 2, page 2](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/2025_Montana_Individual_Income_Tax_Return_Form_2.pdf); [MCA 15-30-2103](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0030/0150-0300-0210-0030.html))

- **What counts:** "the net gain from the sale or exchange of a capital asset held for more than one year".
  - On the return it is the net long-term capital gain subject to the federal capital gains tax, generally the lesser of federal Schedule D line 15 or line 16. If no Schedule D is required, it is Form 1040 line 7.
  - Short-term gains are ordinary income.
- **Rates (2025 and 2026 alike):** 3% on gains that fit in the lower bracket after ordinary income, 4.1% on the rest. HB 337 kept "3.0% and 4.1%" and moved the bracket to match ordinary income.
- **How to compute (page 2, lines 1 to 11):**
  1. Ordinary income = taxable income minus the net long-term capital gains.
  2. Room in the lower bracket = the bracket amount minus ordinary income, not below zero. The bracket amount is $47,500 single, $95,000 joint or $71,250 head of household for 2026 ($21,100, $42,200 and $31,700 for 2025).
  3. Gains up to that room are taxed at 3%; the remaining gains at 4.1%.
  4. If ordinary income is at or above the bracket amount, **all** the gains are taxed at 4.1%.

### Montana earned income tax credit ([2025 Form 2 instructions, line 15](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf); [HB 337, DOR](https://revenue.mt.gov/news/recent-news/HB-337))

- **2025:** 10% of the federal EITC, refundable. The full 10% applies only to a full-year resident who is neither:
  - an enrolled tribal member living on their tribe's reservation, nor
  - a member of an IRC 501(d) agricultural organization.
- **Nonresidents do not qualify.** The 2025 instructions say: "Nonresidents do not qualify for the Montana EITC. ... If you are a nonresident, leave this line blank."
- **Proration (2025):** part-year residents, mixed-residency filers, those tribal members, 501(d) members and resident active-duty servicemembers get the credit in the ratio of Montana earned income to total earned income (Worksheet A). For part-year and mixed-residency filers, Montana earned income is only the earned income (used for the federal EITC) earned in Montana while a resident. Income sourced to Montana while not a resident, or earned by a nonresident spouse, does not count, even if it was earned in Montana.
- **2026:** 20% of the federal EITC, "beginning in tax year 2026". The 2026 proration rules had not been published at the time of writing; check the 2026 Form 2.
- A return must be filed to claim it, and the client must qualify for the federal EITC.

### Subtraction amounts ([DOR 2025 tax tables](https://revenue.mt.gov/taxes/tax-tables-and-deductions/2025); [MCA 15-30-2120](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0200/0150-0300-0210-0200.html); [2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf))

| Item | 2025 | 2026 |
| --- | --- | --- |
| 65-and-older subtraction, per qualifying taxpayer | $5,660 ($11,320 joint, both 65 or older) | Indexed; DOR sets it by 1 November 2026 |
| Montana medical savings account contributions, per taxpayer | Up to $4,600 | Not yet published |
| 529 plan deposits | Up to $4,500 ($9,000 joint) | Indexed from 2026; not yet published |
| ABLE account deposits | Up to $3,000 ($6,000 joint) | Same limits in the statute |
| Volunteer firefighter or volunteer emergency care provider | Not available | $3,000, indexed for inflation (HB 129) |

- **Volunteer subtraction conditions.** For the whole calendar year, the person must have been an active, unpaid member of the same volunteer fire company or emergency medical service, and must have completed the required training (30 hours for firefighters).
- **529 conditions.** The subtraction applies only to accounts owned by the taxpayer, the spouse, or a child or stepchild who is a Montana resident. Non-qualified withdrawals of deducted contributions carry a 5.9% recapture tax (2025 instructions).

### Retirement income ([2025 Form 2, line 6](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/2025_Montana_Individual_Income_Tax_Return_Form_2.pdf); [MCA 15-30-2120](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0200/0150-0300-0210-0200.html); [DOR tax simplification hub](https://revenue.mt.gov/montana-tax-simplification-resource-hub))

- **65-and-older subtraction.** The statute allows it "for each taxpayer that has attained the age of 65".
  - On a joint return where both spouses are 65 or older it is doubled ($11,320 for 2025).
  - It does not depend on having pension income.
  - DOR indexes it each year by 1 November, rounded to the nearest $10. The 2026 figure was not yet published.
- **No general pension exclusion.** From 2024 Montana repealed the "Partial pension, annuity, and IRA deduction" and the partial interest deduction for people 65 or older.
  - Pensions, IRA distributions and taxable Social Security are taxed to the extent they are in federal taxable income.
  - DOR: "Taxable Social Security Income and net operating losses are included in Montana taxable income to the extent that they are included in federal taxable income."
- **Federal deductions still count.** The federal additional standard deduction for age and the enhanced senior deduction on Schedule 1-A reduce Montana income through line 2. They stack with the Montana 65-and-older subtraction.
- **Railroad Retirement** Tier I and Tier II benefits are fully subtracted.
- **Working military retirees and survivor benefits (Form WMRE).** The subtraction is the lesser of 50% of military retirement income and Montana source wages, business income and farm income. Survivors under the Department of Defense Survivor Benefit Plan can exclude up to 50% of those benefits.
  - It is available only to someone who became a resident on or after 30 June 2023, or who was a resident before receiving the retirement income and stayed one.
  - It runs for only five consecutive years. It is not available again to someone who claimed it and then became a nonresident.
  - For those resident before 1 July 2023, the instructions say the five years end with tax year 2028.

### Elderly homeowner/renter credit, 2025 rules ([DOR elderly credit](https://revenue.mt.gov/property/property-tax-help/montana-elderly-homeowner-renter-credit); [Schedule 2EC](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/Form_2_2025_Schedule_2EC.pdf); [2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf))

- **Eligibility.** All of these must be true:
  - 62 or older by 31 December (on a joint return where both own or rent the home, one spouse is enough);
  - lived in Montana at least nine months of the year;
  - owned, rented or leased a Montana home for at least six months;
  - gross household income less than $45,000;
  - the only member of the household claiming it.
- **Income.** Gross household income includes taxable **and** non-taxable income of **every** household member. That covers Social Security, all IRA distributions and pensions, "Capital gain, including any exclusion" (so the home-sale exclusion is not taken off), refundable credits received and government assistance. Losses are left out. Rent paid by a rental-assistance program is neither income nor rent paid for the credit.
- **Computation (Schedule 2EC):**
  1. Gross household income minus $12,600, times a multiplier from 0 (under $2,000) to 0.05 ($12,000 or more). This is net household income.
  2. Add property tax billed on the home and up to one acre, and 15% of rent paid.
  3. Subtract net household income. The result is capped at $1,150.
  4. Multiply by the credit multiplier for gross household income:

| Gross household income | Multiplier |
| --- | --- |
| Less than $35,000 | 100% |
| $35,000 to $37,500 | 40% |
| $37,501 to $40,000 | 30% |
| $40,001 to $42,500 | 20% |
| $42,501 to $44,999 | 10% |
| $45,000 and greater | 0% |

- **Claiming.** The credit is refundable. It is claimed on Form 2 with Schedule 2EC, even by someone with no filing requirement; DOR's page says it can also be filed free through the TransAction Portal. First-time claimants must attach the property tax bill or rent receipts.
- **Deaths.** A claim for a person who died before 1 October of the year is not allowed.
- **Care facilities.** Rent in a care facility is only the out-of-pocket rent. Without a breakdown from the facility, use Worksheet C, which removes 20% of the payment for board and 30% for care.

## Federal conformity and P.L. 119-21 (OBBBA) ([MCA 15-30-2101](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0010/0150-0300-0210-0010.html); [2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf))

- **Rolling conformity.** For this chapter, "Internal Revenue Code" means the Code "as amended, or as it may be labeled or further amended". Federal changes flow into Montana through federal AGI and the federal deductions on line 2, unless Montana lists an adjustment.
- **What flows through for 2025 and 2026:**
  - the higher federal standard deduction;
  - the Schedule 1-A deductions (tips, overtime, car loan interest, enhanced senior deduction), which "are included in the calculation of Montana taxable income";
  - federal depreciation, including bonus depreciation and section 179. Schedule I has no depreciation add-back (other than for a title plant), and the instructions require depreciation to be "the same for federal and Montana income tax purposes".
- **Montana's own adjustments** are the Schedule I items above. The two that matter most after OBBBA are:
  - the **QBI deduction**, which never reaches Montana (MCA 15-30-2120(2)(i));
  - the **state income tax add-back**, computed after the federal SALT cap. The 2025 instructions describe the federal cap as $40,000 ($20,000 married filing separately), phased down above $500,000 ($250,000) of modified AGI until it reaches $10,000. If the deduction was limited by the cap, the add-back is reduced "after considering all state and local taxes, other than state income tax".
- **No decoupling found.** We found no Montana decoupling from P.L. 119-21 in MCA 15-30-2120 or the 2025 Form 2 instructions (checked 25 September 2026). Check DOR's 2026 Form 2 instructions when they are published.

### Federal standard deduction used on line 2 ([Rev. Proc. 2025-32, section 4.14](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [2025 Form 1040](https://www.irs.gov/pub/irs-pdf/f1040.pdf))

| Filing status | 2025 | 2026 |
| --- | --- | --- |
| Single or married filing separately | $15,750 | $16,100 |
| Married filing jointly or qualifying surviving spouse | $31,500 | $32,200 |
| Head of household | $23,625 | $24,150 |

These are the basic amounts. The federal add-ons for age and blindness also count for Montana ([Publication 1](https://revenuefiles.mt.gov/files/Forms/Montana-Publication-1-Prepaying-Income-Tax.pdf)).

## 2025 returns (due 15 April 2026, or 15 October 2026 on extension) ([2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf))

- **Rates:** 4.7% and 5.9% with the 2025 brackets in the rate table above. Capital gains are taxed at 3% and 4.1% with the 2025 brackets.
- **65-and-older subtraction** $5,660 ($11,320 joint, both 65 or older). **EITC** 10% of the federal credit, with proration.
- **New for 2025:** the Mixed Residency box, and the state income tax add-back moved to Schedule I line 4 (Worksheet B).
- **Filing after 15 April 2026 without full payment:** interest at 7% runs from 15 April 2026, recalculated after each part payment.
- **2025 overpayment:** it can be applied to the first 2026 estimated installment (line 24).

## Boundary and exception table ([Publication 1](https://revenuefiles.mt.gov/files/Forms/Montana-Publication-1-Prepaying-Income-Tax.pdf); [MCA 15-30-2103](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0030/0150-0300-0210-0030.html))

| Situation | Rule |
| --- | --- |
| 2026 single, ordinary taxable income exactly $47,500 | All at 4.7%. The 5.65% rate applies only to income "in excess of $47,500". |
| 2026 single, ordinary income of $47,500 or more, plus long-term gains | All the gains are taxed at 4.1%: "if the total nonqualified taxable income is $47,500 or greater". |
| Qualified dividends | Ordinary income for Montana, taxed at 4.7% or 5.65%, not at the capital gains rates. |
| Sole proprietor with a federal QBI deduction | Left out of line 2. Montana taxable income is higher than federal taxable income by that amount, before other adjustments. |
| Nonresident employee with only wages, 30 days or less in Montana, who worked in more than one state | No Montana return or tax on those wages. Not available to the self-employed, construction workers, professional athletes, entertainers, per-event workers, employees paid over $500,000, qualified production employees for the MEDIA Credit, or anyone with other Montana source income. |
| North Dakota resident with Montana wages | Wages not taxable in Montana under the reciprocity agreement. |
| Montana resident with North Dakota wages, North Dakota tax withheld | No other-state credit. The tax is recovered by filing a North Dakota return. |
| Montana resident working remotely for an out-of-state employer that withholds for its state | Wages are Montana source. No credit for the other state's tax ([DOR other-state credit](https://revenue.mt.gov/taxes/tax-credits/credit-for-income-tax-paid-to-other-state)). |
| Other state or country gives Montana residents a credit for Montana tax | No Montana credit for that tax. The Montana credit is nonrefundable and cannot be carried over. |
| Taxes paid to a foreign country with a federal foreign tax credit claimed | No Montana credit. A Montana credit is possible only if the foreign tax was taken as an itemized deduction instead. |
| Estimated tax: prior-year Montana tax was zero on a 12-month return, or no Montana return was required last year | No estimated payments required. |
| Estimated tax: retired and at least 62 at the end of the previous year | No estimated payments required, but only in the year of retirement and one year after. |
| Estimated tax: became disabled in the previous or current year | No estimated payments required. |
| Estimated tax: at least two-thirds of gross income from farming or ranching | No estimated payments required. |
| Elderly credit: gross household income of $45,000 or more | No credit. From $35,000 to $44,999 the credit is scaled down (see Case 5). |
| Elderly credit: rent paid on property exempt from property tax | Not eligible, unless paid to a county or municipal housing authority ([DOR elderly credit](https://revenue.mt.gov/property/property-tax-help/montana-elderly-homeowner-renter-credit)). |

## Worked cases ([MCA 15-30-2103](https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0030/0150-0300-0210-0030.html); [Schedule 2EC](https://revenue.mt.gov/files/Forms/Montana-Individual-Income-Tax-Return-Form-2/Form_2_2025_Schedule_2EC.pdf))

Amounts described as client facts are hypothetical inputs.

**Case 1: 2026, single sole proprietor, full-year resident.**

Client facts: federal AGI of $90,000, all from Schedule C. Federal standard deduction of $16,100 (line 12e), a federal QBI deduction of $14,780 (line 13a), nothing on line 13b. No Montana adjustments, no capital gains. The 2025 Form 2 line 10 tax was $3,500.
- Line 2 = $16,100 (the QBI deduction is left out). Montana taxable income = $90,000 − $16,100 = $73,900.
- Tax: 4.7% × $47,500 = $2,232.50, plus 5.65% × $26,400 = $1,491.60, total $3,724.10.
- Estimated tax: 90% of the 2026 tax is $3,351.69, below 100% of the 2025 tax ($3,500).
- Four payments of $875 (100% of the 2025 tax) are safe whatever 2026 turns out to be. They are due 15 April, 15 June and 15 September 2026 and 15 January 2027.

**Case 2: 2025 return, married filing jointly, both 67, full-year residents.**

Client facts: federal AGI of $100,000 (pensions, IRA distributions and taxable Social Security). Form 1040 lines 12e plus 13b total $46,700 (standard deduction with age add-ons, plus the enhanced senior deduction, from the federal return). No other adjustments.
- Line 3 = $100,000 − $46,700 = $53,300.
- Line 6: both are 65 or older, so $11,320.
- Montana taxable income = $53,300 − $11,320 = $41,980, below the $42,200 joint bracket.
- Tax: 4.7% × $41,980 = $1,973.06.

**Case 3: 2026, single, with long-term capital gains.**

Client facts: Montana taxable income of $60,000, including $20,000 of net long-term capital gains. The other $40,000 includes qualified dividends.
- Ordinary tax: 4.7% × $40,000 = $1,880.
- Room in the lower bracket: $47,500 − $40,000 = $7,500.
- Gains: 3% × $7,500 = $225, plus 4.1% × $12,500 = $512.50. Capital gains tax is $737.50.
- Total tax: $2,617.50.
- If ordinary income had been $47,500 or more, all $20,000 of gains would have been taxed at 4.1% ($820).

**Case 4: 2026, single nonresident with a Montana rental.**

Client facts: lives in Washington. Form 1040 line 9 total income is $66,100, including $10,000 of net rent from a Montana house. No federal adjustments, no capital gains, federal standard deduction $16,100.
- Montana taxable income as if resident: $66,100 − $16,100 = $50,000.
- Ordinary tax: $2,232.50 + 5.65% × $2,500 ($141.25) = $2,373.75.
- Schedule II line 17 ratio: $10,000 / $66,100 = 0.151286.
- Tax on Montana source income: $2,373.75 × 0.151286 = $359.12, carried to Form 2 line 8.

**Case 5: 2025 elderly homeowner/renter credit, single renter aged 70.**

Client facts: lived all year in a rented Montana apartment on taxable property. Gross household income $20,000. Rent paid $9,600.
- Line 20: $20,000 − $12,600 = $7,400. The multiplier for $7,000 to $7,999 is 0.035, so net household income is $259.
- Line 25: 15% × $9,600 = $1,440.
- Line 27: $1,440 − $259 = $1,181. Line 28: the lesser of $1,181 and $1,150 = $1,150.
- Line 29: gross household income is under $35,000, so the multiplier is 1.00. **Credit $1,150** (refundable).
- If gross household income had been $38,000:
  - line 20 is $25,400, the multiplier is 0.05, and net household income is $1,270;
  - $1,440 − $1,270 = $170;
  - the multiplier for $37,501 to $40,000 is 0.30, so the credit is $51.

## When to refuse or refer

- **Residency in doubt**: homes in two states with similar permanency, or a claimed change of domicile without affirmative steps.
- **Nonresident sole proprietors and partners** who need Form DE apportionment, the alternative 0.5% gross receipts election, or publicly traded partnership gains ([2025 Form 2 instructions, Schedule II](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf)). The election is open only to a nonresident who meets all three conditions:
  - their only Montana activity is receipts;
  - they own or rent no real or tangible personal property in Montana;
  - their Montana gross receipts do not exceed $100,000 ([2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf)).
- **Pass-through entity tax** elections, composite returns, Montana K-1 withholding, tribal reservation income (Form ETM), military pay and WMRE questions.
- **NOL transition** carryforwards (codes AN and SL), losses not tracked on earlier Montana returns, and Montana business credits that need preapproval or certificates.
- **Amended returns after federal changes**: these must be filed within 180 days of the IRS final determination or of filing the amended federal return.
- **Non-qualified withdrawals** from farm and ranch risk management accounts, first-time homebuyer accounts and medical savings accounts, which carry 10% penalties ([2025 Form 2 instructions, Schedule IV](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf)).
- **2026 returns** before DOR publishes the 2026 Form 2: confirm the 65-and-older subtraction, the 529 limit and EITC proration.

## Filing and payment ([2025 Form 2 instructions](https://revenue.mt.gov/files/forms/Montana-Individual-Income-Tax-Return-Form-2-Instructions/2025_Montana_Individual_Income_Tax_Return_Form_2_Instructions.pdf); [DOR extensions](https://revenue.mt.gov/taxes/individual-income-tax/extensions); [DOR penalty and interest](https://revenue.mt.gov/taxes/penalty-and-interest); [DOR estimated tax](https://revenue.mt.gov/taxes/estimated-tax-payments); [Publication 1](https://revenuefiles.mt.gov/files/Forms/Montana-Publication-1-Prepaying-Income-Tax.pdf))

- **Due date:** 15 April (15 April 2026 for 2025; 15 April 2027 for 2026).
- **Extension:** an automatic six months, to 15 October. No form and no federal extension are needed.
  - It covers filing only: "You must still pay your tax liability by the due date to avoid penalties and interest." Pay by 15 April through the TransAction Portal or with Form IT.
  - Servicemembers in a combat zone or contingency operation get up to 180 days from their last day there.
- **Late filing penalty** (after the extended due date): 5% a month of the tax owed on 15 October, up to 25%, with a **$50 minimum** "even if you are claiming a refund" (2025 instructions). It may be waived if tax and interest are paid within 30 days of the first Notice of Assessment.
- **Late payment penalty:** 0.5% a month, calculated daily, from 15 April, capped at 12% of the unpaid tax. The 2025 instructions say it is waived automatically if all tax and interest are paid with the return, or within 30 days of the first Notice of Assessment. DOR's penalty page names only the 30-days-after-notice route.
- **Interest** is charged on tax paid after 15 April and on underpaid estimates, computed daily. The rate is 7% for 2026 (0.019178% a day); it was 8% for 2025.
- **Other penalties** ([DOR penalty and interest](https://revenue.mt.gov/taxes/penalty-and-interest)):
  - understatement: 20% of the understatement. An individual may be subject to it if the understatement is more than 10% of the tax or $3,000;
  - purposely or knowingly failing to file: 15% a month, up to 75%;
  - fraud: 75%;
  - frivolous return: $2,500.
- **Estimated tax: who must pay.** Anyone whose tax after withholding and nonrefundable credits is expected to be more than $500, residents and nonresidents alike, unless an exception in the boundary table applies.
- **Estimated tax: amount.** Each installment is the lesser of:
  - one quarter of 100% of the prior year's tax (2025 Form 2 line 10 for 2026 estimates), less expected withholding. Publication 1 uses 100% for everyone, with no higher percentage for high earners. This option needs a return for the preceding year, and it cannot be used if that return covered a short year;
  - one quarter of 90% of the current year's tax.

  Seasonal income can use the annualization method (Worksheet ESA) to work out the 90% current-year amount.
- **Estimated tax: due dates:** 15 April, 15 June, 15 September and 15 January of the next year, or the next business day if a date falls on a weekend or holiday. Fiscal years: the 15th day of the 4th, 6th and 9th months and of the first month after year-end.
- **Paying estimates:** the TransAction Portal (tap.dor.mt.gov) or the Form IT voucher. Underpayment interest is figured on Form EST-I, or DOR figures it.

## Completion checklist

- **Year and status:** rates, brackets, 65-and-older amount and EITC percentage match the year; filing status matches the federal return; the residency box is right.
- **Lines 1 to 7:** line 2 is Form 1040 lines 12e plus 13b only (no QBI deduction); Schedule I includes the Worksheet B add-back; line 6 is claimed for each spouse 65 or older.
- **Page 2:** net long-term capital gains are split out; qualified dividends stay in ordinary income.
- **Schedule II** (with Form DE for nonresident business income) for part-year, nonresident and mixed residency returns.
- **Credits and payments:** other-state credit with that state's return, EITC, Schedule 2EC, withholding, estimates, extension payment and Schedule IV interest and penalties.

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
