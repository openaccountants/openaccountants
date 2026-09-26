---
name: co-income-tax
description: Use this skill whenever asked about Colorado individual income tax for self-employed individuals or sole proprietors — filing Form DR 0104, CO estimated tax (Form DR 0104EP), Colorado flat tax rate, Colorado additions and subtractions, or any query involving Colorado state income tax compliance. Trigger on phrases like "Colorado income tax", "CO income tax", "Form 104", "DR 0104", "Colorado estimated tax", "Colorado self-employed tax", "TABOR refund", or "C.R.S. §39-22".
version: "0.1"
jurisdiction: US-CO
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Colorado individual income tax (Form DR 0104), including sole proprietors

## Scope and who this is for ([Colorado Individual Income Tax Guide](https://tax.colorado.gov/individual-income-tax-guide))

This Guide covers the Colorado individual income tax return, **Form DR 0104**, for **tax year 2026** (returns filed in 2027). It has a dated section for **2025 returns**. It is for full-year residents, part-year residents and nonresidents with Colorado-source income, including sole proprietors and single-member LLC owners whose business profit reaches Colorado through federal taxable income.

Figures are for tax year 2026 unless labelled 2025. On 25 September 2026 the Department of Revenue (DOR) had not published a 2026 filing booklet. Line numbers and rules found only in the 2025 booklet are labelled 2025.

It does **not** cover:
- the pass-through entity's own return, or the SALT Parity election made by a partnership or S corporation (only the owner-level add-back is covered here);
- corporate, fiduciary or withholding returns;
- city occupational privilege taxes, which some Colorado cities levy on people who work in the city. The city, not DOR, runs them; see "When to refuse or refer";
- credits other than those named here.

**Who must file.** A Colorado resident, part-year resident or nonresident with Colorado-source income must file if **either** of these is true:
- they are required to file a federal income tax return; or
- they have a Colorado tax liability for the year.

A person who is not required to file federally generally does not have to file in Colorado, but may file to claim a refund of withholding or refundable credits.

**Residency.** A person is a Colorado resident if **either**:
- they are domiciled in Colorado; or
- they keep a permanent place of abode in Colorado **and** spend, in aggregate, **more than** six months of the tax year in Colorado.

Someone who moves their domicile into or out of Colorado during the year is a part-year resident, not a statutory resident, even if they spent more than six months in Colorado. A person has only one domicile at a time.

## Ask the client first

- **Which tax year?** The 2026 return has new add-backs (overtime, a much lower deduction limit for high earners), a lower Colorado earned income tax credit, and no family affordability tax credit. The 2025 return does not.
- **Residency for the whole year**: domicile, move dates, any Colorado home kept while living elsewhere, and days spent in Colorado. For a joint return, each spouse's status. Military: home of record and days stationed outside the U.S.
- **Federal return**: filing status (Colorado must use the same one), federal taxable income (Form 1040 line 15), federal AGI (line 11a), and whether the client itemized.
- **Federal deductions that Colorado adds back**: the §199A qualified business income (QBI) deduction amount, any state income tax on Schedule A, business meals on Schedule C line 24b, and, for 2026, the overtime deduction on Schedule 1-A. Also ask whether any partnership or S corporation issued a Colorado K-1 (DR 0106K) with the SALT Parity Election box marked.
- **Does the client file Schedule F?** Farmers are outside the high-income QBI add-back.
- **Dates of birth** of the taxpayer and spouse (age at 31 December drives the pension and Social Security subtractions), plus Form 1099-R distribution codes (death benefits; early distributions).
- **Retirement income, per spouse**: taxable Social Security (line 6b) and gross benefits (line 6a) for each spouse, taxable pensions (line 5b) and taxable IRA distributions (line 4b). Also any military retirement, PERA/DPS or railroad retirement.
- **Children**: ages at year-end, and the federal earned income credit allowed (Form 1040 line 27a). Did anyone lack a Social Security number valid for work?
- **Payments**: Colorado withholding, estimated payments (dates and amounts), prior-year carryforward, prior-year Colorado net tax and prior-year federal AGI (for the 110% rule, [Individual Income Tax Guide, Part 6](https://tax.colorado.gov/individual-income-tax-guide)), and any extension payment made with DR 0158.
- **Other states and cities**: income taxed by another state, and any city occupational privilege tax withheld.

## The method, step by step

Line numbers are from the 2025 DR 0104 ([2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf)). Check them against the 2026 form when DOR publishes it.

1. **Finish the federal return first.** Colorado tax is based on federal taxable income, which already reflects the federal standard or itemized deduction and, where claimed, the QBI deduction. A sole proprietor's Schedule C profit, half of self-employment tax, self-employed health insurance, and SEP or solo 401(k) contributions all flow through with no Colorado entry.
2. **Line 1: federal taxable income** from Form 1040, 1040-SR or 1040-SP line 15, not AGI and not wages. Enter a negative amount as negative.
3. **Additions (lines 2 to 9).** Work through every addition in "Additions and subtractions" below:
   - line 2, state income tax addback;
   - line 3, QBI addback;
   - line 4, standard or itemized federal deduction addback;
   - line 5, business meals;
   - lines 6 and 7, non-qualifying CollegeInvest and ABLE distributions;
   - line 9, other additions (non-Colorado state and municipal bond interest, K-1 additions and others).

   For 2026, also expect an overtime addback; the 2026 form has not been published, so the line is not yet known.
4. **Line 10, subtotal** = line 1 plus the additions.
5. **Line 11, subtractions** from Schedule DR 0104AD, line 22 (2025). Do not enter negative amounts. Submit the DR 0104AD with the return.
6. **Line 12, Colorado taxable income** = line 10 minus line 11.
7. **Line 13, tax.**
   - **Full-year residents:** use the DOR tax table if taxable income is under $50,000 ([Individual Income Tax Guide, Part 2](https://tax.colorado.gov/individual-income-tax-guide)). Otherwise multiply line 12 by the rate for the year (see "Figures by year").
   - **Part-year residents and nonresidents:** complete DR 0104PN (step 9) and carry its line 36 to line 13.
8. **Lines 14 to 21: alternative minimum tax, recapture, credits.**
   - Colorado AMT: first complete federal Form 6251, then DR 0104AMT. Tentative minimum tax is Colorado alternative minimum taxable income times 3.47% ([Individual Income Tax Guide, Part 2](https://tax.colorado.gov/individual-income-tax-guide)). Colorado AMT is the excess of that over the normal Colorado tax.
   - Nonrefundable credits come from DR 0104CR and cannot exceed line 16.
9. **Part-year residents and nonresidents: DR 0104PN.**
   - Compute the tax on **all** Colorado taxable income from line 12, as if the client were a full-year resident (PN line 35).
   - PN line 34 ratio = modified Colorado AGI (line 33) divided by modified federal AGI (line 32), rounded to four decimal places. The ratio can exceed 100% ([Part-Year Residents & Nonresidents](https://tax.colorado.gov/income-tax-topics-part-year-residents-nonresidents)).
   - PN line 36 = line 35 times the line 34 percentage. Carry it to DR 0104 line 13.
   - The state income tax addback, conservation easement addback, federal deduction addback and QBI addback are **not** entered on PN line 26.
   - A nonresident's retirement income (4 U.S.C. §114(b)) is not Colorado-source income.
10. **Lines 24 to 33, payments and refundable credits**: withholding (submit the W-2s and 1099s), prior-year carryforward, estimated payments, extension payment, other prepayments, and refundable credits from DR 0104CR (for example the Colorado earned income tax credit).
11. **Lines 34 to 38, TABOR state sales tax refund** (full-year residents only). Modified AGI = federal AGI + nontaxable Social Security (line 6a minus line 6b) + non-Colorado bond interest added on line 9. Look up the amount in the refund table for the year.
12. **Lines 39 to 42, balance or refund**, including any carryforward to next year's estimates. Then check the estimated tax penalty (DR 0204), late payment penalty and interest.

## Figures by year

### Rate ([Colorado Individual Income Tax Guide, Part 2](https://tax.colorado.gov/individual-income-tax-guide); [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf); [TABOR refunds](https://tax.colorado.gov/TABOR))

| Tax year | Rate on Colorado taxable income | Note |
| --- | --- | --- |
| 2024 | 4.25% | Temporary TABOR rate reduction, refunding the 2023-24 fiscal year surplus |
| 2025 | 4.4% | No temporary reduction; the 2025 booklet tax table uses 4.4% |
| 2026 | 4.4% (as published on 25 September 2026) | The 2026 DR 0104EP worksheet computes tax as "4.4% of line 1". A temporary TABOR reduction for 2026 is possible, but DOR had not announced one |

- **The base rate is 4.4%**, a single flat rate for every filing status. Colorado has no standard deduction or personal exemption of its own: the federal deduction is already inside federal taxable income.
- **Temporary TABOR rate cuts** (SB 24-228, [bill summary](https://leg.colorado.gov/bills/sb24-228)) are active for income tax years 2024 through 2034. The rate is cut only if "remaining excess state revenues" (the surplus left after the property tax reimbursement in step 1 of "TABOR refund mechanisms" below) are above $300 million. The size of the cut follows the table there.
- **Do not quote a reduced 2026 rate** until DOR publishes one. Check the rate table in the Individual Income Tax Guide, Part 2, before filing a 2026 return. If a reduced rate is published, recompute the tax and any estimate built on 4.4%.

### Additions and subtractions that most often matter ([Colorado Individual Income Tax Guide, Parts 3 and 4](https://tax.colorado.gov/individual-income-tax-guide); [2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))

| Item | 2025 | 2026 |
| --- | --- | --- |
| QBI addback (single return) | AGI greater than $500,000 | Same (made permanent by HB 25B-1001) |
| QBI addback (joint return) | AGI greater than $1,000,000 | Same |
| Standard or itemized deduction addback: AGI trigger | Exceeds $300,000 | Exceeds $300,000 |
| Deduction limit, single filers (2025 booklet: single, head of household, married filing separately) | $12,000 | $1,000 |
| Deduction limit, joint filers | $16,000 | $2,000 |
| Overtime deduction addback | None | Full federal deduction (Schedule 1-A) |
| Qualified tips deduction | No addback | No addback |
| Business meals addback | Full §274(k) deduction (tax years 2024 through 2030) | Same |
| Charitable subtraction (non-itemizers only) | Contributions above $500 | Same |

**QBI addback** ([HB 25B-1001, session law](https://leg.colorado.gov/laws/session-laws/HB25B-1001/5/download); [2025 Book 104, line 3](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))
- **Who adds it back.** A taxpayer who claimed the §199A deduction (Form 1040 line 13a) and whose AGI is **greater than** $500,000 on a single return, or **greater than** $1,000,000 on a joint return. DOR's 2025 booklet applies $500,000 to every non-joint status.
- **All or nothing.** The **entire** deduction is added back, however far AGI is over the threshold. At exactly $500,000 or $1,000,000 there is no addback.
- **Exception.** The addback does not apply to a taxpayer who is required to file federal **Schedule F** for the year.
- **SALT Parity route.** Separately, a partner or shareholder in a partnership or S corporation that made a **SALT Parity Election** (shown on the Colorado K-1, DR 0106K) must add back their **whole** QBI deduction at any AGI. This is not limited to the electing entity's share.
- **HB 25B-1001** (2025 special session, signed 28 August 2025) struck the words "but before January 1, 2026", so the addback continues for 2026 and later. A 2025 special-session bill to end it ([HB 25B-1020](https://leg.colorado.gov/bills/hb25b-1020)) was lost.

**Standard or itemized federal deduction addback** ([2025 Book 104, line 4](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf); [Individual Income Tax Guide, Part 3](https://tax.colorado.gov/individual-income-tax-guide); [January 2026 tax policy updates](https://tax.colorado.gov/january-2026-tax-policy-updates))
- **Applies only if both** are true:
  - federal AGI (Form 1040 line 11a) **exceeds** $300,000;
  - the federal standard or itemized deduction (line 12e) exceeds the limit for the year.
- **Addback** = the deduction minus the limit. The limit is $12,000 (single filers) or $16,000 (joint) for 2023 to 2025. It is $1,000 (single) or $2,000 (joint) for 2026 and later. DOR credits the 2026 change to Proposition MM.
- **Reduce it** by any Schedule A state income tax already added back on line 2. Do **not** reduce it by K-1 state income tax addbacks from a partnership or S corporation.
- It applies whether the client itemized or took the standard deduction.

**State income tax addback, line 2** ([Income Tax Topics: State Income Tax Addback](https://tax.colorado.gov/income-tax-topics-state-income-tax-addback))
- **Who adds it back.** Anyone who deducted **state income tax** on federal Schedule A, whether paid to Colorado or another state, and whether they are a resident or not. It includes FAMLI premiums deducted as state income tax.
- **Not added back:** general sales taxes, local income or occupational taxes, real estate taxes and personal property taxes.
- **Two limits** (they do not apply to K-1 amounts). The addback is the **smaller** of:
  - the Schedule A state and local tax deduction less the local income, real estate and personal property taxes in it (worksheet line 5);
  - total itemized deductions minus the federal standard deduction the client could have claimed (worksheet line 8).
- **Married filing separately:** if either spouse itemizes, the standard deduction for each spouse is $0 for this worksheet.
- **Pass-through share.** A partner's or resident S corporation shareholder's share of state income tax deducted by the entity (Colorado K-1 line 9, Column A) is added back in full, in addition to their own. A **nonresident** S corporation shareholder adds back only their share of **Colorado** income tax the S corporation deducted (Column B), not tax paid to other states.

**Overtime addback, 2026 and later** ([Individual Income Tax Guide, Part 3](https://tax.colorado.gov/individual-income-tax-guide); [HB 25-1296](https://leg.colorado.gov/bills/hb25-1296))
- A taxpayer who claims the federal overtime compensation deduction must add back the **full amount** claimed on Schedule 1-A (Form 1040).
- There is **no addback** for the federal qualified tips deduction.
- Overtime pay remains subject to Colorado **wage withholding** even when it is exempt from federal withholding.
- SB 26-056, which would have limited the overtime addback to 2026 only, was lost ([SB 26-056](https://leg.colorado.gov/bills/SB26-056)). So the addback applies for 2026 and later.
- The DOR guide lists no other 2026 addback for the new federal deductions in P.L. 119-21. Confirm on the 2026 DR 0104 once it is published.

**Other 2025 special session changes** ([HB 25B-1002](https://leg.colorado.gov/bills/hb25b-1002))
- HB 25B-1002 adds, for C corporations only and from 1 January 2026, an addback of the federal foreign-derived deduction eligible income deduction and new "listed" tax-haven jurisdictions. It does not change the individual return; nor do the other enacted special-session tax bills (insurance premium tax, sale of tax credits, sales tax vendor fee).

**Subtractions for state income tax refunds and U.S. government interest** ([Individual Income Tax Guide, Part 4](https://tax.colorado.gov/individual-income-tax-guide); [2025 Book 104, DR 0104AD lines 1 and 2](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))
- **State income tax refunds (DR 0104AD line 1).** Subtract any state income tax refunds, credits or offsets reported on the federal return and included in federal taxable income. This is generally the amount on line 1 of federal Schedule 1, which is usually there only if the client itemized in the year the tax was paid. If the client did not complete Schedule 1, enter zero.
- **U.S. government interest (DR 0104AD line 2).** Subtract interest on obligations of the United States and its possessions, and income from U.S. government stocks or obligations, but only to the extent it is included in federal taxable income. No subtraction is allowed for:
  - any obligation or payment from the U.S. government for services rendered;
  - income from instruments issued by private financial institutions and guaranteed by the U.S. government.

  The booklet also excludes interest from Fannie Mae and Ginnie Mae, and warns that mutual fund dividends may not be 100% exempt.

**Business meals addback, line 5** ([Individual Income Tax Guide, Part 3](https://tax.colorado.gov/individual-income-tax-guide))
- For tax years 2024 through 2030, add back the **full** federal deduction for business meals under IRC §274(k): the amount on Schedule C line 24b, plus any business meals addition on Colorado K-1 line 10, Column A.

### Pension, annuity and Social Security subtraction ([Income Tax Topics: Social Security, Pensions and Annuities](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities); [2025 Book 104, DR 0104AD lines 3 and 4](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))

| Age on 31 December | Social Security included in federal taxable income | Cap on pension and annuity subtraction |
| --- | --- | --- |
| 65 or older | Entire amount | $24,000, less the Social Security subtracted |
| 55 to 64, AGI not over $75,000 (single) or $95,000 (joint) | Entire amount (tax years 2025 and later) | $20,000, less the Social Security subtracted |
| 55 to 64, AGI above those amounts | Up to $20,000, shared with pension | $20,000, less the Social Security subtracted |
| Under 55 | Only benefits received as a death benefit, up to $20,000 | $20,000, death benefits only |

- **Each spouse is computed separately.** Each spouse's age and income are tested on their own. One spouse's unused cap **cannot** be used by the other.
- **Splitting joint Social Security.** Split the taxable Social Security in proportion to each spouse's gross benefits (DOR's joint worksheet).
- **Social Security uses up the pension cap.** The Social Security subtraction reduces the pension subtraction. For someone aged 65 or older with $24,000 or more of taxable Social Security, no pension subtraction is left.
- **Income that qualifies:**
  - taxable pensions and annuities (line 5b);
  - taxable IRA distributions (line 4b). Premature distributions (those subject to the federal additional tax) from an IRA or a self-employed retirement plan, such as a 401(k), SEP or SIMPLE plan, do not qualify;
  - fully matured privately purchased annuities;
  - taxable permanent disability benefits of a person aged 55 or older.
- **AGI thresholds.** DOR states them only for single ($75,000) and married filing jointly ($95,000) filers. For head of household or married filing separately, check the 2026 DR 0104AD instructions.
- **Separate subtractions** (not subject to the $20,000 or $24,000 caps):
  - railroad retirement benefits, at any age;
  - military retirement for retirees **under** 55, up to $15,000 for 2022 to 2028;
  - PERA contributions made from 1 July 1984 to 31 December 1986, or DPS contributions made in 1986. Claim the pension subtraction first.

  The same income cannot be subtracted twice.

### Colorado earned income tax credit and family affordability tax credit ([Income Tax Topics: Earned Income Tax Credit](https://tax.colorado.gov/income-tax-topics-earned-income-tax-credit); [Income Tax Topics: Family Affordability Tax Credit](https://tax.colorado.gov/income-tax-topics-family-affordability-tax-credit))

| Credit | 2025 | 2026 |
| --- | --- | --- |
| Colorado EITC, as a share of the federal EITC | 50% | 25% |
| Family affordability tax credit (FATC) | Available | "will not be available for tax year 2026" |
| FATC AGI limit, single, head of household, married filing separately | $85,000 | Not applicable |
| FATC AGI limit, joint | $96,000 | Not applicable |
| FATC maximum per child under 6 | $3,273 | Not applicable |
| FATC maximum per child aged 6 to 16 | $2,455 | Not applicable |

**Colorado EITC:**
- **Residency.** Full-year and part-year residents only; nonresidents cannot claim it.
- **The federal credit comes first.** The client generally must claim and be allowed the federal EITC. The Colorado credit is that federal amount times the year's percentage.
- **Without a federal EITC**, the Colorado credit is still available (file DR 0104TN) in two cases:
  - the taxpayer, spouse or a dependent lacks a Social Security number valid for employment (from 2020), but all other federal rules are met;
  - a filer under 25 with no qualifying child and a work-eligible SSN (from 2022) who is:
    - 24 at year-end, if a specified student;
    - 19 to 24, if not a student;
    - 18 to 24, if a qualified former foster youth or homeless youth.
- **Refundable.** Part-year residents multiply it by the DR 0104PN line 34 percentage, capped at 100%.

**Family affordability tax credit (2024 and 2025 only):**
- **Who can claim it.** Refundable, and available to full-year and part-year residents only.
- **The child** must be **under 17** at year-end and meet the federal child tax credit relationship and residency tests. A Social Security number is not required.
- **The amount** is a fixed amount per child that falls as AGI rises. Head of household and married filing separately use the single table.
- **The joint table.** DOR's published 2025 joint table reaches $0 at "$95,001 or more", although the stated joint AGI limit is $96,000. Use the DR 0104CN table for the return.
- **Part-year residents** multiply it by the DR 0104PN line 34 percentage, capped at 100%.
- **Claiming it** takes DR 0104, DR 0104CR and DR 0104CN.

### TABOR refund mechanisms ([SB 24-228](https://leg.colorado.gov/bills/sb24-228); [TABOR](https://tax.colorado.gov/TABOR); [Income Tax Topics: State Sales Tax Refund](https://tax.colorado.gov/income-tax-topics-state-sales-tax-refund))

When state revenue exceeds the TABOR limit, SB 24-228 refunds it in this order:
1. **Property tax reimbursement** to local governments for the homestead exemptions (qualifying seniors, veterans with disabilities, surviving spouses of veterans who died in the line of duty) and the qualified-senior valuation reduction.
2. **Temporary income tax rate cut** (income tax years 2024 through 2034). For 2024 the rate was cut from 4.40% to 4.25%. After 2024 the rate is cut by the amount below. The bill summary writes each cut with a % sign; the 4.40% to 4.25% step shows these are percentage points:

   | Remaining excess state revenues | Rate cut |
   | --- | --- |
   | Above $300 million, up to $500 million | 0.04% |
   | Above $500 million, up to $600 million | 0.07% |
   | Above $600 million, up to $700 million | 0.09% |
   | Above $700 million, up to $800 million | 0.11% |
   | Above $800 million, up to $1 billion | 0.12% |
   | Above $1 billion, up to $1.5 billion | 0.13% |
   | Above $1.5 billion | 0.15% |

3. **Temporary state sales and use tax rate cut** of 0.13%, but only if remaining excess revenues exceed $1.5 billion (adjusted annually) after the first two mechanisms.
4. **State sales tax refund**, a refundable credit on the DR 0104 (or the PTC Rebate application). It is paid either as an identical amount to everyone or through a six-tier table based on modified AGI.

**2025 state sales tax refund (claimed on the 2025 DR 0104, line 38):**

| Modified AGI | Single | Joint |
| --- | --- | --- |
| $52,000 or less | $19 | $38 |
| $52,001 to $105,000 | $25 | $50 |
| $105,001 to $168,000 | $29 | $58 |
| $168,001 to $233,000 | $35 | $70 |
| $233,001 to $299,000 | $37 | $74 |
| $299,001 or more | $59 | $118 |

- **Residency.** The client must have been domiciled in Colorado for the **entire** year (or from 1 January to death). Part-year residents and nonresidents do not qualify.
- **Filing deadline.** The return or PTC application must be filed by 15 October of the following year (15 October 2026 for 2025).
- **Age.** Anyone aged 18 or older before the tax year began qualifies without further conditions. Anyone younger qualifies only if they have a Colorado tax liability or file to claim a refund of Colorado wage withholding.
- **Incarceration.** Not allowed to someone serving a felony sentence who was incarcerated for **at least** 180 days of the 12 months ending 30 June of the tax year.
- **Joint returns.** If one spouse qualifies and the other does not, the joint return gets the single amount.
- **2026:** any TABOR refund for 2026 depends on the 2025-26 fiscal year surplus. DOR had not published 2026 amounts on 25 September 2026.

### Penalties and interest ([Individual Income Tax Guide, Parts 6 and 7](https://tax.colorado.gov/individual-income-tax-guide))

| Item | 2025 | 2026 |
| --- | --- | --- |
| Interest on late tax, regular rate | 12% | 11% |
| Interest, discounted rate | 9% | 8% |
| Estimated tax penalty rate (charged as interest) | 12% | 11% |

- **Late payment penalty**: the greater of $5 or 5% of the unpaid tax, plus 0.5% for each month it stays unpaid, up to 12% in total. It is waived only if **all** of these are met:
  - at least 90% of the tax was paid by the original due date;
  - the return is filed by the extended due date;
  - the balance is paid with the return.
- **Discounted interest** applies if the tax is paid in full before a notice of deficiency or within 30 days of it, or if a monthly payment agreement is made within those 30 days.
- **Interest** runs from the original due date, not including any extension. An extension to file is not an extension to pay.

## Boundary and exception table ([2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf); [Individual Income Tax Guide](https://tax.colorado.gov/individual-income-tax-guide); [Social Security, Pensions and Annuities](https://tax.colorado.gov/income-tax-topics-social-security-pensions-and-annuities))

| Situation | Rule |
| --- | --- |
| Joint AGI exactly $1,000,000, QBI deduction claimed | No QBI addback; the test is "greater than" |
| Joint AGI $1,000,001, QBI deduction $30,000 | Add back the full $30,000, not only the excess over the threshold |
| High-AGI farmer filing Schedule F | No AGI-based QBI addback. A SALT Parity K-1 addback still applies |
| AGI exactly $300,000 | No deduction addback; AGI must exceed $300,000 |
| Taxpayer 64 on 31 December, single, AGI $80,000 | Social Security subtraction capped at $20,000 (AGI over $75,000) |
| Spouse A 70 has $40,000 pension; spouse B 58 has none | A subtracts up to $24,000; B's unused $20,000 cannot be used by A |
| IRA distribution at 52 with the federal early-distribution additional tax | No pension subtraction |
| Colorado resident servicemember stationed outside the U.S. 305 days or more | May elect nonresident treatment on DR 0104PN |
| 2026 overtime deducted federally; tips deducted federally | Add back overtime; no addback for tips |
| Prior-year federal AGI above $150,000 ($75,000 if married filing separately) | Estimated tax safe harbor is 110% of prior-year tax, not 100% |

## Worked cases ([2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf); [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf); [Individual Income Tax Guide](https://tax.colorado.gov/individual-income-tax-guide))

Amounts described as client facts are hypothetical inputs. 2026 cases use 4.4% because DOR had not published any other 2026 rate on 25 September 2026.

**Case 1: 2026, single sole proprietor, full-year resident.**

Client facts: federal AGI of $95,000 and federal taxable income of $80,000. Schedule C business meals deduction of $1,200. No other additions or subtractions. The 2025 Colorado net tax was $3,000 on a 12-month return, and 2025 federal AGI was $90,000.
- No QBI addback (AGI not over $500,000) and no deduction addback (AGI not over $300,000). The meals deduction is added back in full.
- Colorado taxable income: $80,000 + $1,200 = $81,200.
- Tax: $81,200 times 4.4% = $3,572.80.
- Estimated tax. 2025 federal AGI was not over $150,000, so the 100% prior-year option applies. The required annual payment is the lesser of:
  - 70% of $3,572.80 = $2,500.96;
  - 100% of $3,000.

  That is $2,500.96, or $625.24 a quarter.
- Paying $750 a quarter (100% of 2025) is the safe route while the 2026 total is unknown.

**Case 2: 2026, married filing jointly, high earners with QBI.**

Client facts: federal AGI $1,200,000; QBI deduction $40,000; federal itemized deductions $50,000 with no state income tax on Schedule A; federal taxable income $1,110,000. The 2025 Colorado net tax was $45,000 on a 12-month return.
- QBI addback: AGI is over $1,000,000, so add back the full $40,000.
- Deduction addback: AGI exceeds $300,000, so the addback is $50,000 minus the 2026 joint limit of $2,000 = $48,000. For 2025 the same facts would give $50,000 minus $16,000 = $34,000.
- Colorado taxable income: $1,110,000 + $40,000 + $48,000 = $1,198,000.
- Tax: $1,198,000 times 4.4% = $52,712.
- Estimated tax. Prior-year AGI was over $150,000, so the prior-year option is 110% of $45,000 = $49,500. 70% of $52,712 is $36,898.40. The required annual payment is the lesser: $36,898.40.

**Case 3: 2025 return, married filing jointly, retirees aged 67 and 63.**

Client facts: federal AGI $110,000; federal taxable income $80,000.
- Spouse A (67): taxable Social Security $18,000 and a pension of $30,000.
- Spouse B (63): taxable Social Security $22,000.
- Nontaxable Social Security for the couple: $12,000.
- Both are full-year residents.

Working:
- **Spouse A** (65 or older): subtracts all $18,000 of Social Security. The pension subtraction is $24,000 minus $18,000 = $6,000.
- **Spouse B** (55 to 64): joint AGI is over $95,000, so Social Security is capped at $20,000. With joint AGI of $95,000 or less, B could have subtracted all $22,000.
- **Total subtractions:** $18,000 + $6,000 + $20,000 = $44,000.
- **Colorado taxable income:** $80,000 minus $44,000 = $36,000. That is under $50,000, so use the 2025 tax table: the $36,000 to $36,100 row gives $1,586.
- **TABOR refund:** modified AGI is $110,000 + $12,000 = $122,000. Both spouses qualify, so the joint amount for $105,001 to $168,000 is $58.

**Case 4: 2025 return, single, moved into Colorado on 1 July 2025.**

Client facts: federal taxable income $90,000; DR 0104PN modified federal AGI (line 32) $105,000; modified Colorado AGI (line 33) $52,500. No additions or subtractions.
- Line 34 ratio: $52,500 / $105,000 = 50.0000%.
- Line 35: tax on all $90,000 at 4.4% = $3,960 (over $50,000, so the booklet worksheet, not the table).
- Line 36: $3,960 times 50% = $1,980, carried to DR 0104 line 13.
- No TABOR sales tax refund, because the client was not a full-year resident.

**Case 5: full-year resident head of household, one child aged 4, federal AGI $28,000, federal EITC allowed $4,000.**
- **2025:**
  - Colorado EITC: 50% of $4,000 = $2,000.
  - FATC (single table, $25,001 to $30,000, child under 6): $2,598.
  - Both are refundable.
- **2026, same facts:**
  - Colorado EITC: 25% of $4,000 = $1,000.
  - FATC: none, because it is not available for 2026.
- A child aged 4 may also qualify for the separate Colorado child tax credit (DR 0104CN) in both years. That credit is not covered here, so check it before filing.

## When to refuse or refer

- **Residency in doubt**: a Colorado home kept while claiming domicile elsewhere, more than six months in Colorado without domicile, or an unproven mid-year move. The six-month statutory-resident test and domicile evidence are fact-heavy; see DOR Rule 39-22-103(8)(a).
- **Multistate business income** needing apportionment under §39-22-303.6, C.R.S., the credit for tax paid to another state, or wages earned both inside and outside Colorado.
- **Partnership and S corporation owners**: SALT Parity elections, DR 0106K modifications, nonresident shareholder addbacks and composite filings.
- **Net operating losses** with any non-Colorado portion. Non-Colorado NOL deductions must be added back, and part-year allocation uses a days fraction.
- **Colorado AMT**, the Colorado capital gain subtraction, conservation easement credits and additions, enterprise zone, CHIPS zone and strategic capital credits.
- **A 2026 return filed before DOR publishes the 2026 DR 0104 and booklet.** Confirm the rate, the overtime addback line and any TABOR refund first.
- **Military servicemembers and spouses**: nonresident elections, the reacquired-residency subtraction and DR 1059.
- **City occupational privilege taxes (OPT).** These are levied by certain Colorado cities, not the state, and are not claimed on DR 0104. The Schedule A deduction for local occupational taxes is **not** part of the state income tax addback. Send the client to the city that levies the tax for rates, exemptions and employer withholding.
- **Audits, protests and assessments**: a protest must be filed within 30 days of the notice. Also refer amended returns after IRS changes (DR 0104X within 180 days) and any suggestion of fraud or evasion.

## Filing and payment ([Individual Income Tax Guide, Parts 6 to 8](https://tax.colorado.gov/individual-income-tax-guide); [2026 DR 0104EP](https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf); [2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))

- **Due date:** 15 April of the following year (15 April 2027 for 2026), or the next business day if it falls on a weekend or holiday.
- **Extension:** an automatic six-month extension to file, to 15 October. There is no extension to pay. To avoid the late payment penalty, pay at least 90% of the tax by 15 April (Revenue Online or DR 0158), file by 15 October and pay the rest with the return.
- **Abroad on the due date:** the filing deadline is 15 June, and 15 October with the automatic extension. Interest still runs from 15 April, and the 90% rule applies.
- **E-filing is required** for more than five dependents.
- **Estimated tax: who must pay.** Anyone whose net Colorado tax after withholding and credits is expected to be more than $1,000. No estimates are required, and no penalty is due, if either:
  - the net tax less all credits, withholding and any sales tax refund is under $1,000; or
  - the client was a full-year resident for a 12-month prior year with no net Colorado tax liability.
- **Estimated tax: required annual payment** is the lesser of:
  - 70% of the current year's net tax;
  - 100% of the prior year's net tax. If prior-year federal AGI was more than $150,000 (more than $75,000 if married filing separately), use 110% instead.

  The prior-year options apply only if the client filed a Colorado return for a 12-month prior year.
- **Farmers and fishermen** (at least 2/3 of gross income from farming or fishing, for the tax year or for the preceding tax year): 50% of the current tax, paid in one installment by 15 January. Alternatively, file and pay in full by 1 March.
- **Estimated tax: due dates** are 15 April, 15 June and 15 September, and 15 January of the next year.
  - Pay through Revenue Online, EFT, or a check with DR 0104EP.
  - Couples who pay federal estimates jointly must pay Colorado estimates jointly, with the SSNs in the same order on every form.
  - The annualized method is allowed only if the client also uses it federally.
- **Estimated tax penalty (DR 0204).** It is interest on each underpaid installment. Withholding and the sales tax refund count as paid 25% per quarter unless actual dates are shown. There is no penalty on an underpaid fourth installment if the return is filed and the tax paid by 31 January.
- **Refunds.** Claim within four years of the due date (excluding extensions) on an original return. On an amended return, claim within four years of the original filing; later claims are limited to payments made in the preceding three years.

### 2025 returns (due 15 April 2026, or 15 October 2026 on extension) ([2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))

- **Rate** 4.4% (tax table under $50,000; worksheet at 4.4% above).
- **Deduction addback** limits: $12,000 or $16,000. There is no overtime addback.
- **Credits and refund:** Colorado EITC at 50%, the FATC is available, and the 2025 TABOR sales tax refund is on line 38.
- **The TABOR refund** requires the return (or PTC application) to be filed by 15 October 2026.
- **2025 estimated tax penalty and interest** use 12%, and the discounted interest rate is 9%.

## Completion checklist ([2025 Book 104](https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf))

- **Year**: rate, addback limits, EITC percentage and FATC availability match the tax year.
- **Residency** box, and DR 0104PN attached for any part-year or nonresident spouse.
- **Line 1** is federal taxable income (line 15), not AGI or wages.
- **Additions checked**: state income tax (limited), QBI (AGI test or SALT Parity), deduction addback (AGI over $300,000), business meals, and overtime for 2026.
- **DR 0104AD**: each spouse's age, Social Security split and caps checked; the pension cap is reduced by Social Security subtracted.
- **Credits**: DR 0104CR, DR 0104TN and DR 0104CN attached as needed; part-year credits apportioned by PN line 34 (capped at 100%).
- **TABOR refund** claimed only for full-year residents, using modified AGI.
- **Payments**: withholding forms attached, estimated payments matched to Revenue Online, and DR 0204 reviewed.

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
