---
name: va-income-tax
description: Use this skill whenever asked about Virginia individual income tax, Virginia Form 760, Virginia graduated tax rates, Virginia self-employment income tax at the state level, Virginia standard deduction, or any Virginia personal income tax question for sole proprietors. Trigger on phrases like "Virginia income tax", "VA income tax", "Form 760", "Virginia tax brackets", "Virginia 5.75%", "Virginia standard deduction", or any request involving Virginia state individual income tax computation or filing.
version: "0.1"
jurisdiction: US-VA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Virginia individual income tax (Form 760) for residents, including sole proprietors

## Scope and who this is for ([2025 Form 760 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

This Guide covers the Virginia resident individual income tax return, **Form 760**, for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns** (still being filed on extension until November 2026). It is written for full-year Virginia residents, including sole proprietors and owners of a single-member LLC that is disregarded for federal tax, whose business profit reaches Virginia through federal adjusted gross income.

It does **not** cover part-year residents (Form 760PY), nonresidents (Form 763), fiduciaries, corporations, the pass-through entity's own return, or local business licence taxes. See "When to refuse or refer".

**Who is a resident.** A resident is "every person domiciled in Virginia at any time during the taxable year and every other person who, for an aggregate of more than 183 days of the taxable year, maintained his place of abode within Virginia, whether domiciled in Virginia or not" (Va. Code § 58.1-302). The statute is the rule. Both tests matter: a person domiciled elsewhere who keeps a Virginia home for more than 183 days is an "actual resident" and files as a resident. Such a person may have to file as a resident in both Virginia and the domicile state; the 2025 instructions say to claim the credit for tax paid to Virginia on the domicile state's return.

**The instructions word the day test more widely.** The 2025 Form 760 instructions say you are an actual resident if "You maintained an abode in Virginia or were physically present in Virginia for more than 183 total days during the taxable year, even if you are a domiciliary resident of another state or country." The statute looks only at the abode. **Refer** anyone who was physically present in Virginia for more than 183 days but had no Virginia abode: do not decide their residency from this Guide.

**Members of Congress.** The term "resident" does not include a member of the United States Congress who is domiciled in another state. The exception does not cover the member's spouse, dependents or staff, who test their own residency. A member with Virginia-source income other than congressional pay may still need to file Form 763 (2025 instructions).

A full-year resident files Form 760. A person who was resident for only part of the year files Form 760 only if all income for the whole year came from Virginia sources; otherwise Form 760PY.

**Who must file (2025 and 2026).** A resident must file if Virginia adjusted gross income (VAGI, Form 760 Line 9) is at or above: single $11,950; married filing jointly (combined) $23,900; married filing separately $11,950. Below the threshold the tax is $0, but a return is still needed to get back withholding or estimated payments. The 2026 Form 760ES uses the same three thresholds for 2026.

Official sources: 2025 Form 760 instructions, https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf ; Code of Virginia Title 58.1, Chapter 3, https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-302/ ; 2026 Form 760ES, https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2026/760es-2026.pdf .

## Ask the client first

- Which tax year? 2025 and 2026 share rates, standard deduction and exemptions, but the estimated-tax threshold changed for 2026 (see Estimated tax).
- Resident all year? Domicile, any Virginia home kept more than 183 days, and days physically present in Virginia. If the person moved in or out, stop (Form 760PY). If they were present more than 183 days with no Virginia abode, refer.
- Federal filing status, and did the client **itemize federally**? Virginia follows the federal choice.
- Dates of birth of taxpayer and spouse (age deduction, age 65 exemption), blindness, and number of dependents.
- Federal AGI (line 11a on the 2025 Form 1040), taxable Social Security, and any state income tax refund included in federal income.
- For the business: did the federal return use bonus depreciation, the increased section 179 limit, immediate R&E expensing or qualified production property expensing? Each needs a Virginia adjustment.
- Interest from other states' bonds (addition), and interest from U.S. or Virginia obligations (subtraction).
- Federal earned income credit claimed, and family VAGI (low-income credits).
- Income taxed by another state; income from a partnership or S corporation that made the Virginia pass-through entity tax (PTET) election.
- Virginia withholding, estimated payments (dates and amounts), prior-year tax, and any extension payment.

## The method, step by step

Form 760 line numbers are from the 2025 return.

1. **Line 1, federal AGI.** Enter federal adjusted gross income, not federal taxable income. A sole proprietor's Schedule C profit, the deduction for half of self-employment tax, self-employed health insurance and SEP/SIMPLE/solo 401(k) contributions all sit inside federal AGI, so they flow through with no Virginia entry. Deductions taken after federal AGI do not reach Virginia: on the 2025 Form 1040 these include the qualified business income deduction (line 13a) and the Schedule 1-A additional deductions (line 13b), as well as the federal standard deduction.
2. **Line 2, additions (Schedule ADJ).** Common ones: interest on other states' obligations; fixed-date conformity additions (see Federal conformity); the add-back of a pass-through entity's state income tax deduction when the owner claims the PTET credit.
3. **Line 3** = Line 1 + Line 2.
4. **Line 4, age deduction** (see Exemptions and the age deduction). Not a Schedule ADJ subtraction; it has its own line.
5. **Line 5**, taxable Social Security and Tier 1 Railroad Retirement benefits included in federal AGI.
6. **Line 6**, state income tax refund or overpayment credit included in federal income.
7. **Line 7, other subtractions (Schedule ADJ).** Examples: interest on U.S. obligations exempt in Virginia; interest on Virginia obligations; unemployment compensation included in federal AGI; the sum of Virginia Lottery prizes under $600 each included in federal AGI; disability income (up to $20,000, and not together with the age deduction); fixed-date conformity subtractions. [2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf)
8. **Line 9, VAGI** = Line 3 minus (Lines 4 + 5 + 6 + 7). Compare to the filing threshold.
9. **Line 10 or 11, deductions.** Itemize on Virginia Schedule A only if the client itemized federally; otherwise take the Virginia standard deduction (see Standard deduction). If one spouse itemizes, both must.
10. **Line 12, exemptions**: $930 for each personal and dependent exemption, plus $800 for each taxpayer or spouse who is 65 or older or blind. [§ 58.1-322.03](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-322.03/)
11. **Line 13, Schedule ADJ deductions** (for example child and dependent care expenses on which the federal credit is based, Commonwealth Savers contributions, long-term care premiums not deducted federally).
12. **Line 15, Virginia taxable income** = Line 9 minus Lines 10 or 11, 12 and 13.
13. **Line 16, tax** from the rate schedule (see Tax rates). Round return amounts to whole dollars.
14. **Line 17, spouse tax adjustment**, joint filers only (see Spouse tax adjustment).
15. **Lines 19 to 26, payments and credits**: withholding, estimated payments, extension payment, the low-income or earned income credit (Line 23), credit for tax paid to another state (Line 24, Schedule OSC), and Schedule CR credits including the PTET credit (Line 25). The other-state credit is the lesser of the net tax on the other state's return on earned, business and capital gain income (Schedule OSC Line 5) and the Virginia ratio (Line 9: Form 760 Line 18 tax times the share of Virginia taxable income that the other state taxed): "Enter the lesser of Line 5 or Line 9". It is nonrefundable, and the sum of all nonrefundable credits cannot exceed the tax on Form 760 Line 18.
16. **Line 32**, addition to tax, penalties and interest (see Filing and payment).

## Rates, thresholds and figures by year

### Tax rates (all filing statuses; unchanged since 1990; same for 2025 and 2026) ([§ 58.1-320](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-320/))

| Virginia taxable income | Tax |
| --- | --- |
| Not over $3,000 | 2% of taxable income |
| Over $3,000, not over $5,000 | $60 plus 3% of the excess over $3,000 |
| Over $5,000, not over $17,000 | $120 plus 5% of the excess over $5,000 |
| Over $17,000 | $720 plus 5.75% of the excess over $17,000 |

Source: Va. Code § 58.1-320 ("Five and three-quarters percent on income in excess of $17,000 for taxable years beginning on and after January 1, 1990"), https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-320/ , and the rate schedule in the 2025 instructions and 2026 Form 760ES. The official example: taxable income of $90,000 gives $4,917.50, rounded to $4,918.

### Standard deduction (only if the client did not itemize federally) ([§ 58.1-322.03](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-322.03/))

| Taxable years | Single | Married filing jointly | Married filing separately |
| --- | --- | --- | --- |
| 2025 and 2026 | $8,750 | $17,500 | $8,750 |
| 2027 (Code as now published) | $9,200 | $18,400 | one-half of the married amount |
| 2028 and 2029 (Code as now published) | $9,300 | $18,600 | one-half of the married amount |
| 2030 onward (Code as now published) | $3,000 | $6,000 | one-half of the married amount |

- A single filer with head-of-household federal status uses the single amount.
- A person who can be claimed as a dependent on another return may take the standard deduction "only with respect to earned income": the smaller of earned income or the standard deduction.
- **Sunset: check before planning 2027.** The 2025 instructions say the increase "is scheduled to sunset after Taxable Year 2026" and revert to $3,000 / $6,000. The Code section as now published (Va. Code § 58.1-322.03, amended in the 2026 Special Session I) instead sets the 2027 to 2029 amounts above and reverts only from 2030. Treat 2027+ amounts as statute text until the 2027 forms confirm them.

Sources: https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-322.03/ ; 2025 instructions, Line 11.

### Exemptions and the age deduction ([§ 58.1-322.03](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-322.03/))

- **Exemptions (2025 and 2026):** $930 per personal and dependent exemption; an additional $800 for each taxpayer or spouse aged 65 or older or blind (for 2025, 65 or older on or before January 1, 2026). The additional $800 is allowed whether or not the client itemizes. Source: Va. Code § 58.1-322.03(2); 2026 Form 760ES worksheet line 4.
- **Age deduction (Line 4):** up to $12,000 per qualifying taxpayer.
  - Born on or before January 1, 1939: $12,000, no income test.
  - Otherwise (for 2025, born on or between January 2, 1939 and January 1, 1961): the $12,000 is reduced $1 for every $1 that adjusted federal AGI (AFAGI) exceeds $50,000 (single) or $75,000 (married). AFAGI is federal AGI, adjusted for conformity additions and subtractions, minus taxable Social Security and Tier 1 Railroad Retirement benefits.
  - **Married couples always use joint AFAGI**, even when filing separately. If both spouses qualify, compute one joint deduction (the $12,000 per spouse, less the one reduction) and split it in half.
  - For 2026 the statutory test is having "attained the age of 65"; confirm the birth-date cut-off in the 2026 instructions when published.
  - A taxpayer who claims the age deduction may not claim the disability income subtraction, the low-income credit or either Virginia earned income credit. If either spouse claims one of those credits, neither spouse may claim the age deduction.
  - Source: Va. Code § 58.1-322.03(5); 2025 instructions, Line 4 and the Age 65 and Older Deduction Worksheet.

### Spouse tax adjustment (joint filers) ([2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

Filing status 2 couples may reduce tax by up to $259 if both spouses have income and combined taxable income is more than $3,000. Compute it with the worksheet in the instructions or the Department's calculator, and enter the spouse's VAGI on the return. Source: 2025 instructions, Line 17.

### Federal conformity and One Big Beautiful Bill Act (P.L. 119-21) decoupling ([§ 58.1-301](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-301/))

- Virginia now conforms to the Internal Revenue Code **as it existed on December 31, 2025**, plus later federal amendments that only extend the expiry of a provision Virginia already follows (Va. Code § 58.1-301 B). This replaced the suspended rolling conformity; it was enacted February 20, 2026 and applies to 2025 returns (Tax Bulletin 26-1).
- Virginia follows P.L. 119-21 only to the extent it changes federal AGI or federal itemized deductions, **except** that it decouples from:
  - immediate expensing of qualified production property;
  - immediate expensing of domestic research and experimental expenditures, including the retroactive and catch-up provisions (Virginia keeps the amortization period);
  - the increased section 179 expensing limits.
- Continuing decouplings: federal bonus depreciation under IRC § 168(k) (recompute Virginia depreciation as if no bonus was taken); the federal overall limitation on itemized deductions (Virginia keeps its own Pease-style limitation; Virginia generally applies no SALT cap, but a taxpayer subject to that Virginia limitation applies the federal SALT cap for the year when computing it, per Tax Bulletin 26-1); the federal reduction of the medical expense floor (Virginia uses 10% of federal AGI).
- Mechanics: keep separate Virginia depreciation and amortization records. When the federal deduction is larger in a year, make a fixed-date **conformity addition**; when the Virginia deduction is larger in a later year, make a conformity **subtraction**. Enclose a schedule and explanation.
- Business interest: Virginia follows the federal IRC § 163(j) limitation, and for 2025 and later allows a Virginia deduction of 20% of the business interest disallowed federally (enclose federal Form 8990).
- Sources: https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-301/ ; Tax Bulletin 26-1, https://www.tax.virginia.gov/sites/default/files/inline-files/tb-26-1-date-of-irc-conformity-advanced.pdf .

### Estimated tax ([2026 Form 760ES](https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2026/760es-2026.pdf))

- **2026 onward:** estimated payments (or more withholding) are required if Virginia tax after withholding and credits is expected to be **more than $1,000**. Nothing is required if the excess is $1,000 or less, or if expected VAGI is below the filing threshold.
- **2025:** there is no addition to tax if every payment was on time and the balance owed with the 2025 return is $150 or less.
- **Due dates (2026 year):** May 1, 2026, June 15, 2026, September 15, 2026 and January 15, 2027, each 25% when the requirement is met by April 15. If the requirement is first met later, the number of payments falls (three, two or one). If the 2026 return is filed and all tax paid by March 1, 2027, the January 15 payment is not needed.
- **Safe harbours** (Va. Code § 58.1-492; Form 760ES section VIII): no addition to tax if each timely installment is at least 90% of the current-year tax (actual or annualized), or at least 100% of the prior year's tax (prior year a full 12-month year with a liability), or is based on prior-year income at current rates and exemptions; or if total installment underpayments for the year are $1,000 or less (2026). The addition to tax is interest-rate based, computed on Form 760C.
- **Electronic payment mandate:** all payments must be electronic if any estimated installment or any return or extension payment exceeds $1,500, or total estimated tax exceeds $6,000.
- Sources: 2026 Form 760ES sections I, II and VIII; 2025 instructions, Schedule ADJ Line 18; https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-490/ ; https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-492/ .

### Low-income credit and Virginia earned income credit (Line 23; claim only one) ([§ 58.1-339.8](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-339.8/))

- **Credit for Low-Income Individuals:** nonrefundable, $300 for each personal and dependent exemption (not the 65-or-older or blind exemptions), if **family VAGI** (taxpayer, spouse and dependents) is equal to or less than the federal poverty guideline for the family size. For 2025 returns the table starts at $15,650 for one person and is $26,650 for three. Only one spouse may claim it when filing separately.
- **Virginia earned income credit:** for taxpayers who claimed the federal earned income credit. For **2025 and 2026 only**, a **refundable** credit of 20% of the federal credit (it was 15% for 2022 to 2024). The alternative nonrefundable credit is also 20% of the federal credit. Nonresidents and part-year residents cannot take the refundable version.
- **Barred** for the whole household if the taxpayer, spouse or any dependent claims: the age deduction; the 65-or-older or blind exemption; the Virginia National Guard, basic military pay or federal/state employee subtraction; or if the taxpayer is claimed as a dependent on another return.
- Sources: https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-339.8/ ; 2025 instructions, "Tax Credit for Low-Income Individuals or Virginia Earned Income Tax Credit".

### Pass-through entity elective tax (PTET) ([§ 58.1-390.3](https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.3/))

A partnership, LLC taxed as a partnership, or S corporation (including an S corporation with a single shareholder, since the test is being a separate entity for federal tax, not the number of owners) may elect annually, on its timely filed return (including extensions), to pay Virginia tax at 5.75% on its eligible owners' shares. An individual owner then claims a refundable credit for their share on Schedule CR and must add back their share of the entity's state income tax deduction. A sole proprietorship or single-member LLC disregarded for federal tax is **not** a pass-through entity for this purpose, because the definition requires an entity "recognized as a separate entity for federal income tax purposes". Sources: https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.3/ ; https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.1/ .

### 2025 returns: what differs from 2026 ([2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

- Rates, standard deduction ($8,750 / $17,500), exemptions and age-deduction limits are the same.
- The 2025 estimated-tax penalty test uses the $150 balance-due rule, not the $1,000 rule.
- Conformity: the December 31, 2025 conformity date and the P.L. 119-21 decouplings apply to 2025 returns. Clients who filed a 2025 return before February 20, 2026 may need to amend (Tax Bulletin 26-1).
- Due dates: filed by May 1, 2026; extended returns are due November 1, 2026, which is a Sunday, so a return postmarked Monday, November 2, 2026 is timely under the weekend rule.

## Boundaries and exceptions ([2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

| Situation | Rule |
| --- | --- |
| Client itemized federally | Must itemize on Virginia Schedule A; no Virginia standard deduction. Itemized deductions are reduced by state and local income taxes deducted federally |
| Married, one spouse itemizes | Both must itemize |
| Dependent of another taxpayer | Standard deduction limited to earned income; barred from low-income and earned income credits |
| Age deduction, single, AFAGI exactly $50,000 | Full $12,000: the reduction applies only to the amount that exceeds $50,000 |
| Age deduction, married filing separately | Reduction uses both spouses' combined AFAGI over $75,000 |
| Age deduction vs disability subtraction | One or the other per person |
| Age deduction or 65/blind exemption claimed by anyone in the household | No low-income credit and no Virginia earned income credit |
| 2026 expected tax after withholding exactly $1,000 | No estimated payments required ("$1,000 or less") |
| Extension balance due exactly 10% of the tax | No extension penalty; the penalty applies only when the underpayment is **more than** 10% (interest still runs) |
| Income taxed by Arizona, California or Oregon | Do not claim the Virginia credit; claim the credit on that state's nonresident return |
| Income from the District of Columbia | No Virginia credit for tax paid on that income. If D.C. income tax was paid (for example withheld), follow D.C.'s instructions to get it refunded |
| Virginia resident with wages or salaries earned as a nonresident in Kentucky, Maryland, Pennsylvania or West Virginia | No credit for any income the other state does not tax |
| Tax paid to another state larger than the Virginia tax on that income | Credit limited to the lesser of the two (Schedule OSC Line 10), and all nonrefundable credits together cannot exceed Line 18 tax |
| Federal bonus depreciation, increased section 179, R&E or production-property expensing | Virginia conformity addition in the year taken; later subtractions as Virginia deductions catch up |
| Qualified business income deduction and Schedule 1-A deductions | Taken after federal AGI; no effect on Virginia; no Virginia addition needed |
| Disregarded single-member LLC | Reported on the owner's Form 760; cannot make the PTET election |

## Worked cases ([2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

All are hypothetical full-year residents with no additions or subtractions unless stated. Tax is shown before rounding to whole dollars.

**Case C1, ordinary (2026).** Single, age 40, sole proprietor. Federal AGI $80,000 after the self-employment tax deduction. Took the federal standard deduction.
- Virginia taxable income = $80,000 − $8,750 − $930 = $70,320.
- Tax = $720 + 5.75% × ($70,320 − $17,000) = $3,785.90.
- Expected tax after withholding (none) is more than $1,000, so four estimated payments are required (25% each on May 1, June 15 and September 15, 2026 and January 15, 2027). The federal QBI deduction does not reduce Virginia income.

**Case C2, age deduction phase-out (2025).** Single, born 1958. Federal AGI $80,000, of which $20,000 is taxable Social Security. No conformity adjustments. Standard deduction.
- AFAGI = $80,000 − $20,000 = $60,000. Excess over $50,000 = $10,000. Age deduction = $12,000 − $10,000 = $2,000.
- VAGI = $80,000 − $2,000 − $20,000 = $58,000.
- Exemptions = $930 + $800 = $1,730. Taxable income = $58,000 − $8,750 − $1,730 = $47,520.
- Tax = $720 + 5.75% × ($47,520 − $17,000) = $2,474.90.
- With AFAGI of $62,000 or more, the age deduction would be nil. Because this client claims the age deduction and the 65-or-older exemption, no low-income or earned income credit is available.

**Case C3, choosing the credit (2025).** Married filing jointly, one child, family VAGI $26,000 (at or below the $26,650 guideline for three), federal earned income credit claimed $4,000. Standard deduction.
- Taxable income = $26,000 − $17,500 − $2,790 (three exemptions) = $5,710. Tax = $120 + 5% × ($5,710 − $5,000) = $155.50.
- Low-income credit = $900 (three exemptions at $300) but nonrefundable, so limited to $155.50.
- Refundable Virginia earned income credit = 20% × $4,000 = $800; tax is eliminated and the excess is refunded. Claim the earned income credit, not both.

**Case C4, extension penalty threshold (2025 return).** Total 2025 tax $5,000. By May 1, 2026 the client paid $4,400 (withholding, estimates and a Form 760IP payment) and filed on August 15, 2026, paying the rest.
- Underpayment $600 is more than 10% of the tax ($500), so the extension penalty applies: 2% per month or part of a month from May 1 to August 15 (four months) = 8% × $600 = $48, plus interest.
- If $4,500 had been paid by May 1 (balance $500, exactly 10%), there is no extension penalty, only interest.

**Case C5, conformity (2026).** A sole proprietor expensed equipment federally under the increased section 179 limit and took bonus depreciation on other assets. Virginia decouples from both: recompute Virginia depreciation without them, report the excess federal deduction as a fixed-date conformity addition on Schedule ADJ for 2026, and take conformity subtractions in later years as the Virginia depreciation exceeds federal.

## When to refuse or refer

- Part-year residents (Form 760PY) or nonresidents (Form 763), including spouses with different residency who have not elected to file jointly as residents.
- Anyone physically present in Virginia for more than 183 days who had no Virginia abode. The statute (Va. Code § 58.1-302) tests the abode; the 2025 Form 760 instructions also count physical presence. Do not decide it here.
- Military personnel: Servicemembers Civil Relief Act elections, combat-zone and basic-pay subtractions, and military benefits subtractions.
- Pass-through entity returns (Form 502), the PTET election itself, and composite returns.
- Credit for tax paid to another state beyond a simple single-state nonresident return (for example more than one state, composite returns, or pass-through income taxed elsewhere), and any Arizona, California or Oregon credit claimed on that state's return.
- Multi-year depreciation or R&E amortization tracking under the conformity decouplings where no Virginia records exist yet.
- Business credits on Schedule CR (land preservation, historic rehabilitation and others), net operating loss carrybacks, and amended returns after a federal audit (federal changes must be reported within one year of the final determination).
- Planning for 2027 and later standard deductions until the 2027 forms are published.

## Filing and payment ([2025 instructions](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-760-instructions.pdf))

| Item | 2025 return | 2026 return |
| --- | --- | --- |
| Due date (calendar year) | May 1, 2026 | May 1, 2027 (a Saturday; the weekend rule allows the next business day) |
| Automatic extension to file | Six months: November 1, 2026 (a Sunday, so November 2, 2026) | Six months: November 1, 2027 |
| Tax to pay by the original due date | Balance of the tax, with Form 760IP or online | Same |
| Taxpayers outside the U.S. on the due date | July 1, 2026 | July 1, 2027 (Va. Code § 58.1-344 D) |

- **Extension:** no application needed, but it extends filing, not payment. Pay at least 90% of the tax by May 1. If the balance paid late is more than 10% of the tax, an extension penalty of 2% per month or part month applies from the due date to the filing date, up to 12%.
- **Late payment:** 6% per month or part month from filing to payment, up to 30%.
- **Late filing:** a return filed more than six months after the due date gets no extension; the late filing penalty is 30% of the tax due.
- **Fraud or failure to file with intent to evade:** an additional penalty of 100% of the correct tax.
- **Interest** runs on unpaid tax from the due date, even with an extension.
- **Fiscal year filers:** the 15th day of the 4th month after year end.
- Sources: 2025 instructions ("When to File Your Return", "Reminders", Schedule ADJ Lines 18 to 20); https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-341/ ; https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-344/ .

## Completion checklist ([2026 Form 760ES](https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2026/760es-2026.pdf))

- [ ] Residency confirmed as full year (domicile, or a Virginia home kept more than 183 days); otherwise stop. Present more than 183 days with no Virginia abode: refer.
- [ ] Line 1 is federal AGI, not taxable income.
- [ ] Conformity additions/subtractions for bonus depreciation, section 179, R&E and production property; Virginia depreciation records kept.
- [ ] Age deduction worked from AFAGI; married couples used joint AFAGI.
- [ ] Standard vs itemized follows the federal return; dependent's standard deduction limited to earned income.
- [ ] Exemptions: $930 each, plus $800 for 65 or older or blind.
- [ ] Tax from the rate schedule; spouse tax adjustment considered for joint filers.
- [ ] Only one of the low-income credit or Virginia earned income credit; neither if anyone claimed the age deduction or the 65/blind exemption.
- [ ] Schedule OSC credit limited to the lesser of other-state tax and the Virginia tax on that income; none for Arizona, California or Oregon (claimed there), none for D.C. income (get any D.C. withholding refunded), none for Kentucky, Maryland, Pennsylvania or West Virginia wages those states do not tax; PTET credit with its add-back.
- [ ] Estimated tax tested: 2026 more-than-$1,000 rule; 2025 $150 rule; electronic payment mandate.
- [ ] Balance paid by May 1 even when filing on extension.

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
