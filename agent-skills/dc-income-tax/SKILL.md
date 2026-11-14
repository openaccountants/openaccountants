---
name: dc-income-tax
description: "District of Columbia Individual Income Tax Return (Form D-40) for sole proprietors and single-member LLCs. Covers the seven-bracket graduated system (4%–10.75%), DC standard deduction computation, Schedule S additions and subtractions, estimated tax (D-40ES), and the Earned Income Tax Credit. Trigger: taxpayer is domiciled in DC or maintains an abode for 183+ days during the tax year."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dc-income-tax"
  jurisdiction: "US-DC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# District of Columbia individual income tax (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.


## Scope

This skill covers the District of Columbia (DC) individual income tax return, **Form D-40**, for **tax year 2026** (returns filed in 2027), with a dated section for **2025 returns**. It is for DC residents and part-year residents, including sole proprietors and single-member LLC owners whose business profit reaches DC through federal adjusted gross income (AGI).

**Answer first:** The 2026 rate schedule is confirmed. The latest read annual form is the **2025-2026 filing cycle** D-40 booklet. The current posted Code now incorporates August 2026 emergency amendments, and OTR's current EITC page confirms an 85% match for qualifying-child filers in 2026-2028. The standard-deduction/federal-conformity position still requires final 2026 instructions and the successor act's status before filing; do not use an earlier draft or estimate worksheet to settle a later law. [OTR EITC](https://otr.cfo.dc.gov/page/eitc-faqs); [§47-1801.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04).

It does **not** cover the unincorporated business franchise tax return (Form D-30) beyond a pointer, the corporate franchise tax (D-20), fiduciary returns (D-41), withholding, real property tax, or estate tax. See "When to refuse or refer".

**Who is a resident** ([D.C. Code § 47-1801.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04), paragraph 42):
- anyone **domiciled** in DC **at any time** during the tax year; or
- anyone who maintains a **place of abode in DC for an aggregate of 183 days or more** during the year, whether or not domiciled in DC.
- **Excluded unless domiciled in DC at some time in the year:**
  - elected officers of the US government;
  - staff of an elected legislative official who are bona fide residents of that official's state;
  - presidential appointees confirmed by the Senate who serve at the President's pleasure;
  - Supreme Court justices.
- A temporary or transitory absence from DC does not change domicile or place of abode.

**Nonresidents are not taxed on their income.** The Home Rule Act bars the Council from imposing "any tax on the whole or any portion of the personal income ... of any individual not a resident of the District" ([D.C. Code § 1-206.02](https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02)). A commuter who lives in Maryland or Virginia and works in DC does not file a D-40. Some commuters have DC tax withheld from their pay, or pay DC estimated tax, in error. They claim it back on **Form D-40B, Nonresident Request for Refund** (see "Filing and payment").

## Ask the client first

1. Tax year, domicile/move dates, days a DC home was maintained, and any congressional, appointed-official or military exclusion?
2. Federal filing status, AGI, standard/itemized choice, each spouse's income, age and blindness?
3. Business gross income, owners' personal-service share, material capital, franchise income/loss and depreciation history?
4. Federal/state differences: other-state bonds, small-business stock, interest limitation and Schedule 1-A items?
5. Qualifying children, federal EITC eligibility, ITINs, childcare/licensing/subsidies, rent/property tax and household income?
6. Withholding and dated estimates, prior full-year DC residency/tax, extensions and federal-return changes?

## The method, step by step

D-40 line numbers below describe the 2025-2026 filing cycle, from the 2025 return ([2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf)).

1. **Decide residency** using the tests in "Scope". Nonresidents stop here. They file no D-40 and use D-40B to recover DC tax withheld.
2. **Decide whether a return is needed.**
   - A resident must file a D-40 if gross income was **at least** the DC filing threshold for their status (see the 2025 chart in "Figures by year"). This applies even if no federal return is required.
   - Also file to get a refund of withholding, or to claim a refundable credit: DC EITC, Schedule N, Schedule H or Schedule ELC.
   - If no federal return is required, prepare a mock federal return to get federal AGI.
3. **Line 4, federal AGI.** Start from federal AGI, not federal taxable income.
   - These items are all inside federal AGI and flow through: a sole proprietor's Schedule C profit, the deduction for half of self-employment tax, self-employed health insurance, and retirement plan contributions.
   - Federal computations and indexed figures remain in `us-schedule-c-and-se-computation`, `us-self-employed-health-insurance`, `us-self-employed-retirement` and `us-child-tax-credit-and-eitc`. The federal qualified business income deduction (section 199A) is taken below AGI, so it never reaches DC. DC also bars it by statute for 2025 ([D.C. Code § 47-1803.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.04), subsection (d)(4)).
4. **Line 5, franchise tax.** Add back any franchise tax deducted on a federal business return (Forms 1065 or 1120-S).
5. **Line 6, other additions (Schedule I, Calculation A).**
   - Section 168 additional (bonus) depreciation.
   - Pass-through losses from DC unincorporated businesses that exceed the $12,000 threshold ([2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf), Schedule I).
   - "Other" items. For 2025, these include interest on other states' municipal bonds, section 1202 gain, and the DC business interest limitation adjustment.
6. **Lines 8 to 15, subtractions.**
   - Line 8: part-year residents subtract income received while domiciled outside DC.
   - Line 9: taxable refunds of state and local income tax.
   - Line 10: the **taxable amount of Social Security and tier 1 railroad retirement**, so DC does not tax it.
   - Line 11: income taxed on a DC franchise or fiduciary return, such as the D-30.
   - Line 12: DC and federal government survivor benefits, for survivors aged 62 or older.
   - Line 13: unemployment insurance benefits.
   - Line 14: Schedule I, Calculation B items.
7. **Line 16, DC AGI** = Line 7 minus Line 15.
8. **Lines 17 and 18, deduction.** Take the same type as on the federal return ([D.C. Code § 47-1803.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.04), subsection (b)).
   - **Federal standard deduction taken:** take the DC standard deduction. That is the basic amount, plus any additional amount for age 65 or blindness.
   - **Itemized federally:** itemize on the DC return. If one spouse itemizes on a separate return, neither spouse may take the standard deduction.
   - **What DC itemized deductions allow.** Income taxes are not deductible. Real estate taxes are deductible in full, with no federal SALT cap.
   - **High-income reduction.** It applies if DC AGI is **greater than** $200,000 ($100,000 married filing separately). Itemized deductions are then reduced by 5% of the excess. Medical expenses, investment interest and casualty losses are not reduced. Use Calculation F, or Calculation D for part-year residents ([D.C. Code § 47-1803.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.04), subsection (c)(2)).
9. **Line 19, taxable income** = Line 16 minus Line 18.
10. **Tax.** Use the tax tables in the [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) if taxable income is $100,000 or less. Otherwise use the rate schedule in "Figures by year".
11. **Credits and payments.** Take non-refundable credits first. Then add:
    - withholding and estimated payments;
    - refundable credits: the DC EITC, Schedule U refundable credits such as the Keep Child Care Affordable credit, and Schedule H.

    Then add any D-2210 underpayment interest.
12. **Part-year residents.** Report only income for the period of DC domicile, and prorate the standard deduction and credits.
    - The 2025 booklet prorates by days: "dividing the number of days you were domiciled in DC by 365 (366 if leap year)".
    - The statute prorates the standard deduction by months ([§ 47-1801.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04), paragraph 44(D)).
    - Follow the booklet method on the return. Refer if the difference matters.

**Sole proprietors and the D-30.** DC taxes an unincorporated business on a separate return, the D-30.
- **When to check it.** The [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) applies to anyone with gross income from DC sources of more than $12,000 from an unincorporated business or business activity, "including rents and royalties". They must check the D-30 instructions. If a D-30 is required: "do not include the income here, but report it on your D-30 return instead."
- **Businesses outside the D-30.** Some businesses are excluded altogether ([D.C. Code § 47-1808.01](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.01)). The main exclusion for sole proprietors has two conditions, and both must be met:
  - **more than 80%** of gross income comes from personal services actually rendered by the owners ([§ 47-1808.01](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.01), paragraph 3); and
  - capital is not a material income-producing factor.
- **Out of scope.** Whether a D-30 is due, and the tax on it, are outside this skill.

## Figures by year

### Tax rates, 2025 and 2026 ([D.C. Code § 47-1806.03](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03); [OTR rates page](https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates))

The same schedule applies to all filing statuses for taxable years beginning after 31 December 2021. It did not change for 2025 or 2026. The 2026 D-40ES prints the same table ([2026 D-40ES](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_D40ES_Book_wLinks04012026.pdf)).

| Taxable income | Tax  Official source |
| --- | ---  --- |
| Not over $10,000 | 4% of taxable income  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $10,000, not over $40,000 | $400 plus 6% of the excess over $10,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $40,000, not over $60,000 | $2,200 plus 6.5% of the excess over $40,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $60,000, not over $250,000 | $3,500 plus 8.5% of the excess over $60,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $250,000, not over $500,000 | $19,650 plus 9.25% of the excess over $250,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $500,000, not over $1,000,000 | $42,775 plus 9.75% of the excess over $500,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |
| Over $1,000,000 | $91,525 plus 10.75% of the excess over $1,000,000  [Official source](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03) |

Spouses or domestic partners who live together and file separately are each treated as single for the rate schedule.

### Standard deduction and filing threshold, 2025 ([2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf); [D.C. Code § 47-1801.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04), paragraph 3A)

| Filing status | 2025 basic standard deduction | 2025 D-40 filing threshold (gross income at least)  Official source |
| --- | --- | ---  --- |
| Single, married filing separately, dependent filer | $15,000 | $15,000  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Head of household | $22,500 | $22,500  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Married or registered domestic partners filing jointly or separately on the same return; qualifying widow(er) | $30,000 | $30,000  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |

- **Additional standard deduction (2025).** It applies to each taxpayer or spouse who was born before 2 January 1961, or who is blind.
  - The amount is $1,600.
  - It is $2,000 for someone who is single, head of household, or a dependent claimed by someone else, and who is not married.
  - Compute it on Schedule S, Calculation G-1, and attach it.
  - On a separate return, the spouse's additional amount is allowed only if the spouse had no gross income, is not filing, and cannot be claimed as a dependent.
- **No personal exemptions.** The temporary act repealed D.C. Code § 47-1806.02.

### Standard deduction, 2026: reconcile the period before computing

OTR's March 2026 estimate worksheet prints the then-federal basic amounts ($16,100/$24,150/$32,200) and additional amounts ($1,650/$2,050). Those are historical estimate-sheet entries, not a confirmed final DC return deduction. The current posted §47-1801.04(3A),(44)-(46) instead uses the DC base amounts $15,000/$22,500/$30,000, annual DC cost-of-living adjustment and specified rounding, with a decoupling period through 2029 in the August emergency text. Do not use the federal indexed amount as the final DC amount or assume the April draft's proposed 2027 realignment survived. The final 2026 indexed DC figure and successor-law status remain unconfirmed. The old worksheet amounts are preserved here only to explain the source conflict. [2026 D-40ES](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_D40ES_Book_wLinks04012026.pdf); [current posted Code](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04).

### DC earned income tax credit (EITC) ([D.C. Code § 47-1806.04](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.04), subsection (f); [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf))

| Tax year | DC EITC for a filer **with** a qualifying child | Status  Official source |
| --- | --- | ---  --- |
| 2022 to 2024 | 70% of the federal EITC | Law (subparagraph (B-1))  [Official source](https://otr.cfo.dc.gov/page/eitc-faqs) |
| 2025 | 100% of the federal EITC | Temporary act raised (B-2) from 85% to 100%  [Official source](https://otr.cfo.dc.gov/page/eitc-faqs) |
| 2026 to 2028 | 85% of the federal EITC | Confirmed by current OTR EITC FAQ  [Official source](https://otr.cfo.dc.gov/page/eitc-faqs) |
| 2029 onward | 100% of the federal EITC | Current OTR schedule; recheck before that future year  [Official source](https://otr.cfo.dc.gov/page/eitc-faqs) |

- **Where the years come from.**
  - The 2024 budget delayed the 100% match to "beginning in tax year 2029, rather than 2026" ([ORA, Revenue Provisions in DC's New Budget](https://ora-cfo.dc.gov/blog/revenue-provisions-dc%E2%80%99s-new-budget)).
  - The temporary act moved 2025 to 100%.
  - OTR's current [EITC FAQ](https://otr.cfo.dc.gov/page/eitc-faqs) now independently publishes 85% for 2026-2028; this is no longer supported only by a proposed-act statement.
- **Conditions for the percentage match.** It applies only to an individual **with a qualifying child** who is allowed the federal EITC under IRC section 32. The statute speaks of a return "filed for a full calendar or fiscal year". That describes the return's period, such as a calendar-year D-40. It does not exclude part-year residents, who still claim, prorated as below. The credit is refundable.
- **No qualifying child.** DC computes its own credit under subparagraph (C), with its own phase-out. For 2025, the maximum is $649 and the federal investment-income eligibility test remains in `us-child-tax-credit-and-eitc` (the old skill restated the federal limit).
- **ITIN filers.** From 1 January 2023, a DC resident can claim the DC EITC with an ITIN. This applies if they would get the federal EITC except that they do not have a Social Security number.
- **Part-year residents** prorate the credit by the days they were domiciled in DC. The booklet's example is $649 times 0.1945 = $126.
- **Non-custodial parents** aged 18 to 30 who meet the child support conditions claim on Schedule N.

### Keep Child Care Affordable tax credit (Schedule ELC) ([D.C. Code § 47-1806.15](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.15); [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf))

- **Amount:** the lesser of the eligible child care expenses paid and the per-child limit. The 2025 maximum is **$1,200 per eligible child**. The limit is indexed each year; check the 2026 Schedule ELC.
- **Eligible child:** a dependent claimed by the taxpayer who **has not reached age 4 by 30 September** of the tax year.
- **Eligible expenses:** payments to a licensed child development facility (or one exempt from licensing under the statute). Care after 31 August does not count for a child old enough to enrol in pre-kindergarten.
- **Refundable.** A part-year return prorates the credit by months.
- **No credit if any of these applies:**
  - the child is not claimed as a dependent on both the federal and DC returns;
  - someone else claims the child;
  - DC child care subsidies were received or paid for the child;
  - someone else got this credit for the same child;
  - DC **taxable income exceeds** the limit. The statutory limit is $150,000 (single, head of household or joint) or $75,000 (married filing separately), indexed. Use the Schedule ELC figure for the year.

### Homeowner and renter property tax credit (Schedule H) ([D.C. Code § 47-1806.06](https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.06); [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf))

- **2025 limits:**
  - the maximum credit is $1,425;
  - the tax filing unit's federal AGI must not exceed $66,000 for claimants under 70, or $90,000 for claimants 70 or older.

  For 2026 amounts, check the 2026 Schedule H.
- **Who can claim:**
  - The claimant must be an owner of record of a DC home, or a tenant paying rent on one, **during the entire calendar year** before the year of the claim.
  - Only one claimant per tax filing unit.
  - No credit for a year in which the claimant was a dependent, unless they were or became 65 or older that year.
  - Not for a property owned by a government, a house of worship or a non-profit organisation.
- **How it works.**
  - Renters treat **20% of rent** paid as property tax.
  - The credit is the property tax (or 20% of rent) that exceeds a percentage of the filing unit's federal AGI, up to the maximum.
  - In the lowest band (AGI under $25,000), the percentage is 3.0%.
  - Use the Schedule H worksheet for other bands and for claimants 70 or older.
- **Filing:** attach Schedule H to the D-40. Someone who is not required to file a D-40 can file Schedule H as a standalone return.

### Federal conformity: distinguish the 2025 cycle and the posted August 2026 text

The 2025-2026 filing cycle booklet disallows the federal higher basic standard deduction, tips/overtime/car-loan/enhanced-senior deductions, R&E expensing, business-interest changes, special production-property depreciation, nonitemizer charity deduction and section 1202 exclusion; it retains the bonus-depreciation addback. These are 2025 return directions. [2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf).

The February Attorney General opinion concluded that congressional disapproval did not retroactively change the tax liability for years ending December 31, 2025, and discussed the temporary act expiring September 25, 2026. The February revenue estimate and April fiscal-impact draft are historical evidence, not final 2026 law. The old April proposal would have continued DC basic deduction decoupling for 2026, allowed Schedule 1-A items/R&E/section 1202 from 2026, delayed nonitemizer charity relief and used an 85% EITC match. Do not apply a draft's terms automatically.

The posted Code now shows August 13, 2026 Act 26-416 changes. Section 47-1803.04(d)(6)-(9),(e)(3)-(6) distinguishes disallowed pre-2026 Schedule 1-A items from allowed post-2025 items; §47-1801.04 shows a longer DC basic-deduction decoupling period than the April draft. Its notes identify emergency legislation, so the effective successor measure and final 2026 forms must be checked before filing. This skill does not resolve the temporary/emergency enactment chain by assuming continued effect. The final Sources line lists the unresolved 2026 items, including any child credit. The old temporary-act $1,000-per-child 2026 credit is not an established usable current-year amount. [current deduction section](https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.04); [current definitions](https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04).

## Boundary and exception table

| Situation | Rule  Official source |
| --- | ---  --- |
| Domiciled in Virginia, keeps a DC apartment for exactly 183 days | Resident: the test is 183 days **or more**. Files a D-40 on all income.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Domiciled in Maryland, DC apartment for 182 days, works in DC | Nonresident. No D-40. Claim back any DC withholding on D-40B.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Moved into DC with intent to stay on 1 July | Part-year resident from the date domicile changed. Report DC-period income; prorate deduction and credits.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Single resident, 2025 gross income exactly $15,000 | Must file: the threshold is "at least" $15,000.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Itemized on the federal return, DC standard deduction would be larger | Must itemize on the DC return.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| DC AGI exactly $200,000 (joint) | No 5% itemized reduction: it applies only when DC AGI is greater than $200,000.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Consultant whose income is almost all personal services, no material capital | Likely outside the D-30 under the more-than-80% rule. Confirm with the D-30 instructions.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Client moved into DC in March of the prior year | The 110% prior-year route is not available (they must have been a DC resident during all of the prior year). Use 90% of the current year's tax.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| DC tax after withholding and credits is below $100 | No estimated tax interest.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |
| Taxpayer with no qualifying child, 2025 | DC's own childless EITC applies (2025 maximum $649), not the percentage match.  [Official source](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf) |

## Worked cases

Amounts described as client facts are hypothetical inputs.

**Case 1: 2025, single, full-year resident.**

Client facts: federal AGI of $80,000, no DC additions or subtractions, federal standard deduction, under 65, not blind.
- DC AGI is $80,000. The 2025 DC standard deduction is $15,000, so taxable income is $65,000.
- Tax: $3,500 plus 8.5% of the $5,000 over $60,000 ($425) = $3,925. On the return itself, the booklet's tax table gives the figure for incomes of $100,000 or less. The rate schedule result is shown here.


**Recomputation for Case 1 (2025-2026 filing cycle).**

```oa-check
name: DC prior-cycle single 65000 taxable
inputs:
  agi: 80000
  deduction: 15000
steps:
- taxable: agi - deduction
- tax: 3500 + (taxable - 60000) * 0.085
expected:
  taxable: 65000
  tax: 3925
```

**Case 2: 2025, married filing jointly, full-year residents.**

Client facts: federal AGI of $150,000, federal standard deduction, both under 65.
- The 2025 DC standard deduction is $30,000, so taxable income is $120,000.
- Tax: $3,500 plus 8.5% of the $60,000 over $60,000 ($5,100) = $8,600.


**Recomputation for Case 2 (2025-2026 filing cycle).**

```oa-check
name: DC prior-cycle married taxable 120000
inputs:
  agi: 150000
  deduction: 30000
steps:
- taxable: agi - deduction
- tax: 3500 + (taxable - 60000) * 0.085
expected:
  taxable: 120000
  tax: 8600
```

**Case 3: 2026 estimated tax, the 110% rule.**

Client facts: the Case 2 couple were DC residents for all of 2025, with a 2025 DC tax of $8,600. They expect 2026 DC tax of $9,000 and have no DC withholding.
- Current-year route: 90% of $9,000 = $8,100.
- Prior-year route: 110% of $8,600 = $9,460. DC uses 110% for **every** filer. There is no 100% option and no income test.
- No interest is due if payments reach the smaller of the two.
- The 2026 tax is unknown in April, so the safe plan is the prior-year route: $9,460 divided by 4 = $2,365 on each of 15 April, 15 June and 15 September 2026 and 15 January 2027.


**Recomputation for Case 3:** If the $9,000 current-year estimate is reliable, $8,100/4 = $2,025 per quarter suffices; the prior-year route buys protection against an underestimated current-year liability for an additional $340 per quarter. If actual 2026 tax rises to $12,000, 90% becomes $10,800 and the $9,460 prior-year route is then the smaller amount. Choose by the reliability of the estimate and prior-year residency, not by always preferring one route.

```oa-check
name: DC 2026 estimated tax decision
inputs:
  prior_tax: 8600
  estimated_current: 9000
  higher_actual: 12000
steps:
- current_route: estimated_current * 0.9
- prior_route: prior_tax * 1.1
- minimum_current: min(current_route, prior_route)
- quarter_current: minimum_current / 4
- quarter_prior: prior_route / 4
- extra_quarter: quarter_prior - quarter_current
- higher_current_route: higher_actual * 0.9
- higher_minimum: min(higher_current_route, prior_route)
expected:
  current_route: 8100
  prior_route: 9460
  quarter_current: 2025
  quarter_prior: 2365
  extra_quarter: 340
  higher_current_route: 10800
  higher_minimum: 9460
```

**Case 4: DC EITC, 2025 and 2026.**

Client facts: a full-year resident with one qualifying child, allowed a federal EITC of $4,000.
- 2025: DC EITC = 100% of $4,000 = $4,000, refundable.
- 2026: the published OTR match is 85%, so DC EITC = 85% of $4,000 = $3,400. [Current OTR FAQ](https://otr.cfo.dc.gov/page/eitc-faqs).


**Recomputation for Case 4:** use an independently determined eligible federal credit; this is not its federal calculation.

```oa-check
name: DC 2026 EITC qualifying child
inputs:
  federal_credit: 4000
steps:
- prior_cycle: federal_credit * 1
- dc2026: federal_credit * 0.85
expected:
  prior_cycle: 4000
  dc2026: 3400
```

**Case 5: commuter refund (D-40B).**

Client facts: domiciled in Maryland all of 2025 and never had a DC place of abode. The client's only DC income was wages, and the employer withheld $2,000 of DC tax in error.
- Not a DC resident, so no D-40.
- File D-40B, claiming the Commuter/Domiciliary State Exemption, for a refund of the $2,000. Attach the W-2s and a copy of the Maryland return.


**Recomputation for Case 5 (2025-2026 filing cycle).**

```oa-check
name: DC nonresident wage refund
inputs:
  withheld: 2000
  dc_liability: 0
steps:
- refund: withheld - dc_liability
expected:
  refund: 2000
```

**Case 6: Schedule H renter credit, 2025.**

Client facts: a single renter aged 40, not anyone's dependent, who rented the same DC apartment all of 2024 and 2025. Federal AGI is $20,000. Rent paid in 2025 is $12,000.
- Rent treated as property tax: 20% of $12,000 = $2,400.
- Threshold: 3.0% of $20,000 = $600 (lowest AGI band).
- Excess: $2,400 minus $600 = $1,800. This is capped at the 2025 maximum, so the credit is $1,425.


**Recomputation for Case 6 (2025-2026 filing cycle).**

```oa-check
name: DC prior-cycle renter credit cap
inputs:
  rent: 12000
  agi: 20000
  cap: 1425
steps:
- deemed_tax: rent * 0.2
- threshold: agi * 0.03
- credit: min(max(deemed_tax - threshold, 0), cap)
expected:
  deemed_tax: 2400
  threshold: 600
  credit: 1425
```

## When to refuse or refer

- **Residency in doubt**, for example:
  - a DC place of abode close to 183 days;
  - a disputed change of domicile;
  - dual residency with Maryland or Virginia;
  - members of Congress, congressional staff, Senate-confirmed appointees and their families.
- **The D-30** ([2025 D-40 booklet](https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf)). Refer any sole proprietor, partnership or LLC with DC-source gross income of more than $12,000 where the more-than-80% personal services exclusion is unclear. The D-30 has its own return, rate and estimated payments; refer to the D-30 instructions or a specialist.
- **2026 items that still need the final effective text/instructions:**
  - the standard deduction;
  - the tips, overtime, car loan interest and senior deductions;
  - the child tax credit;
  - the charitable deduction for non-itemizers.

  Check OTR's 2026 forms before filing. Warn clients that 2026 estimates based on the D-40ES may differ from the final rules.
- **Business depreciation history:** bonus or special depreciation add-backs across several years, or the sale of an asset with a different DC basis.
- **Part-year residents** where the booklet's day-based proration and the statute's month-based proration give materially different answers.
- **Other credits:** credit for tax paid to another state, the DC Low-Income Housing Tax Credit, and other Schedule U credits.
- **Military members and spouses** (combat zone extensions, Military Spouse Residency Relief Act).
- **Health care shared responsibility (Schedule HSR)** where coverage was not full-year.
- **Outside this skill:** fiduciary returns (D-41), corporate franchise tax (D-20), the ballpark fee (a business-level fee), estate tax and real property tax.

## Filing and payment

- **Due date:** 15 April (15 April 2026 for 2025 returns; 15 April 2027 for 2026 returns). If it falls on a weekend or legal holiday, file by the next business day.
- **Extension: DC does not follow the federal extension automatically.** File **Form FR-127** by 15 April for a six-month extension (to 15 October 2026 for 2025 returns).
  - If a balance is expected, pay it with the FR-127.
  - The FR-127 is not required if no balance is expected and the tax was reasonably estimated and paid through withholding or estimates.
  - An extension to file is not an extension to pay. Interest and penalties run on tax not paid by 15 April.
  - Taxpayers living or travelling outside the US can get a further six months, but only after filing the first FR-127 on time.
- **Late filing and late payment penalties** ([D.C. Code § 47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213)). Neither applies if there is reasonable cause and no willful neglect.
  - **Failure to file:** 5% of the unpaid tax for each month or part of a month, up to 25% in total.
  - **Failure to pay:** 5% a month, up to 25%.
  - **Overlap:** the failure-to-file addition is reduced by the failure-to-pay addition for the same months.
- **Interest** on unpaid tax runs from the original due date, disregarding any extension to file. The rate is **10% a year, compounded daily** ([D.C. Code § 47-4201](https://code.dccouncil.gov/us/dc/council/code/sections/47-4201)).
- **Estimated tax (D-40ES).** Required if the client must file a DC return and expects to owe **$100 or more** in tax.
  - The D-2210 describes the trigger as tax "expected to be more than $100". At exactly $100, check.
  - Vouchers are due 15 April, 15 June and 15 September 2026 and 15 January 2027.
  - If the D-40 is filed and the balance paid by 15 January, do not send the last voucher.
- **Underpayment interest (Form D-2210)** is charged at 10% a year, compounded daily. It is not due if either:
  - tax after DC withholding and credits is less than $100; or
  - withholding plus timely estimates equal at least 90% of the current year's tax, or 110% of last year's tax. The 110% route is available only to someone who was a DC resident for all 12 months of the prior year.

  An annualized income method is available when income was uneven.
- **Electronic payment** is required if a payment for a period exceeds $5,000 (MyTax.DC.gov or Modernized e-File).
- **Nonresident refunds (D-40B).** Available to a nonresident whose only DC-source income was wages, and who either commuted daily from their home state or was domiciled in another state. They must not have kept a DC place of abode for 183 days or more.
  - Attach the W-2s or 1099s.
  - From tax year 2025, commuter and domiciliary claimants attach a copy of their home state's income tax return. If the home state has no income tax, the form asks for residency proof, but it is inconsistent. One place says "two proof of residency documents"; another says a state-issued ID or driver's license plus one proof of residency. Follow the D-40B line instructions, and when in doubt attach the ID and two proofs.
  - Military spouses attach DD Form 2058.
  - From tax year 2025, the D-40B can be filed on MyTax.DC.gov.
- **Federal return copy.** From tax year 2025, OTR Tax Notice 2025-01 requires certain high-income filers to submit an electronic copy of their federal return. Check the booklet for the thresholds.

## Completion checklist

- **Year:** 2025 amounts are used for 2025. For 2026, the form/deduction/conformity gaps are unresolved until the reviewer checks final effective instructions; the EITC match is now published.
- **Residency:** the domicile and 183-day abode tests are applied and the excluded groups considered; part-year dates are on Line 2.
- **Filing need:** gross income is compared with the DC threshold ("at least").
- **Federal AGI** is on Line 4, not taxable income.
- **Additions:** franchise tax and Schedule I additions are entered (bonus depreciation, other states' bond interest, and for 2025 the OBBBA items).
- **Subtractions:** taxable Social Security (Line 10), income reported on a D-30 (Line 11), and Schedule I, Calculation B items.
- **Deduction type** matches the federal return. Itemized deductions exclude income taxes, and the 5% reduction applies above $200,000 ($100,000 MFS).
- **Credits:** DC EITC at the correct percentage for the year; the Schedule ELC, Schedule H and Schedule N conditions are checked.
- **D-30:** the need is considered for any business with DC-source gross income over $12,000.
- **Estimates and interest:** the D-2210 is reviewed. The 110% prior-year route is used only if the client was a full-year DC resident in the prior year.
- **Extension:** the FR-127 is filed with payment if a balance was expected.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| income-00.pdf: official source. Read for pp.4-8,12-22 and relevant Schedule S/I/H/ELC/N fields, 2025 filing-cycle deductions, credits, residency and filing. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40_Book_082026_v1.pdf | 2026-11-13 |
| income-01.html: official source. Read for July Council announcement, passage only, not enacted tax text. | https://dccouncil.gov/council-wraps-up-budget-season-with-second-vote-on-the-budget-support-act/ | 2026-11-13 |
| income-02.html: official source. Read for paragraphs 3A,28,42,44-46, residence and current posted deduction text plus emergency notes. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1801.04 | 2026-11-13 |
| income-03.html: official source. Read for subsection (a)(5), nonresident income-tax restriction. | https://code.dccouncil.gov/us/dc/council/code/sections/1-206.02 | 2026-11-13 |
| income-04.html: official source. Read for definition exclusions, especially more-than-80% owner services and material capital. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.01 | 2026-11-13 |
| income-05.pdf: official source. Read for both pages, installment interest trigger, 90%/110% and full prior-year residency. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D-2210_021226.pdf | 2026-11-13 |
| income-06.html: official source. Read for subsections b-e, deduction choice, itemized reduction, QBI and posted Schedule 1-A treatment. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1803.04 | 2026-11-13 |
| income-07.html: official source. Read for post-2021 rate schedule and filing-status application. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.03 | 2026-11-13 |
| income-08.html: official source. Read for current rate schedule. | https://otr.cfo.dc.gov/page/dc-individual-and-fiduciary-income-tax-rates | 2026-11-13 |
| income-09.pdf: official source. Read for 2026 estimate instructions, due dates, safe harbors and estimate worksheet, not final annual deductions. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_D40ES_Book_wLinks04012026.pdf | 2026-11-13 |
| income-10.html: official source. Read for temporary conformity act text and expiry, historical context. | https://code.dccouncil.gov/us/dc/council/laws/26-89 | 2026-11-13 |
| income-11.pdf: official source. Read for tax conformity subtitle in April draft only, not final law. | https://app.cfo.dc.gov/services/fiscal_impact/pdf/spring09/FIS%20FY%202027%20Budget%20Support%20Act%20of%202026_EOM.pdf | 2026-11-13 |
| income-12.html: official source. Read for subsections f-g, EITC match, ITIN, proration and noncustodial parent conditions. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.04 | 2026-11-13 |
| income-13.html: official source. Read for 2024 budget EITC delay, historical context. | https://ora-cfo.dc.gov/blog/revenue-provisions-dc%E2%80%99s-new-budget | 2026-11-13 |
| income-14.html: official source. Read for childcare ages, licensing, subsidies, income test and index mechanism. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.15 | 2026-11-13 |
| income-15.html: official source. Read for rent fraction, credit computation, eligibility and index mechanism. | https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.06 | 2026-11-13 |
| income-16.pdf: official source. Read for opinion conclusions on 2025 retroactivity and temporary-act duration. | https://oag.dc.gov/sites/default/files/2026-02/AG-Opinion-Decoupling-Retroactivity-and-Validity-.pdf | 2026-11-13 |
| income-17.pdf: official source. Read for February estimate treatment of then-pending conformity legislation. | https://ora-cfo.dc.gov/sites/default/files/public/Revenue%20Estimate%20Letter_FINAL-FEB%202026_02%2027%202026.pdf | 2026-11-13 |
| income-18.pdf: official source. Read for FR-127 filing, payment and extension conditions. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_FR-127_021226.pdf | 2026-11-13 |
| income-19.pdf: official source. Read for D-40B claimant categories, attachments and inconsistent proof wording. | https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2025_D40B_Form_012026.pdf | 2026-11-13 |
| income-20.html: official source. Read for late filing/payment rates, overlap and estimated-tax exclusion. | https://code.dccouncil.gov/us/dc/council/code/sections/47-4213 | 2026-11-13 |
| income-21.html: official source. Read for underpayment interest and daily compounding. | https://code.dccouncil.gov/us/dc/council/code/sections/47-4201 | 2026-11-13 |
| OTR EITC FAQ. Read for current 2025, 2026-2028 and 2029 match schedule, qualifying-child distinction and ITIN/refund mechanics. | https://otr.cfo.dc.gov/page/eitc-faqs | 2026-11-13 |

Not yet confirmed: final 2026 D-40, indexed DC standard/additional deductions, filing thresholds, childless EITC and child-care/property-credit amounts; effective successor to the August emergency conformity provisions, section 1202/R&E/business-interest/charity and any child-credit treatment; material statutory-month vs booklet-day proration differences; final 2026 D-2210/FR-127/D-40B layouts. The historical April draft, expired temporary act and earlier D-40ES deduction figures are not usable substitutes for final 2026 law. The 2026 EITC qualifying-child match itself is confirmed by OTR at 85%.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dc-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dc-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
