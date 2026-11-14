---
name: ga-income-tax
description: "Compute a Georgia individual income tax return (Form 500) for tax year 2026, for residents, part-year residents and nonresidents, including sole proprietors and single-member LLC owners. Covers the 4.99% flat rate from HB 463, the $15,000 and $30,000 standard deductions, the $5,000 dependent exemption, Schedule 1 additions and subtractions, the retirement and military retirement exclusions, the 2026 overtime and cash tip exclusions, bonus depreciation decoupling under HB 1199, Schedule 3 proration, credits, the HB 1000 surplus refund and 2025 returns still open. Trigger on \"Georgia income tax\", \"GA Form 500\", \"Georgia retirement exclusion\", \"Georgia standard deduction\", \"Georgia flat tax\". Estimated tax is in ga-estimated-tax-depth."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ga-income-tax"
  jurisdiction: "US-GA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Georgia individual income tax (Form 500), tax year 2026

> **Source-cited draft.** Built from HB 463 (2026), HB 1199 (2026), HB 1000 (2026), HB 111 (2025), the DOR important tax updates and federal tax changes pages, the 2025 IT-511 booklet, the 2026 Employer's Tax Guide and DOR's residency, HB 1000 and penalty pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For tax year 2026 Georgia taxes Georgia taxable income at a flat **4.99%** (5.19% for 2025). The standard deduction is **$15,000** (single, head of household, married filing separately) or **$30,000** (married filing jointly), and each dependent gives a **$5,000** exemption. There is no personal exemption for the taxpayer or spouse. Georgia starts from federal adjusted gross income, so the federal QBI, standard, tips, overtime and senior deductions never reach it. The 2026 return is due 15 April 2027.

## Scope and who this is for

In scope: Form 500 for tax year 2026 (returns filed in 2027), with a dated section for 2025 returns still being filed or amended. Residents, part-year residents and nonresidents with Georgia income, including sole proprietors and single-member LLC owners whose business profit reaches Georgia through federal AGI.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Estimated tax, Form 500-ES and the Form 500 UET penalty | `ga-estimated-tax-depth` |
| The entity's own return and the pass-through entity tax election (the owner's PTEDED and PTEADD lines are here) | `ga-corporate-and-ptet` |
| Employer withholding (Forms G-4, G-7, G-1003) | `ga-payroll` |
| Corporate income tax and net worth tax | `ga-corporate-and-ptet`, `ga-net-worth-tax` |
| Fiduciary returns (Form 501) and credits beyond those named here | refer (see "When to refuse or refer") |
| Federal AGI itself | the federal skills, for example `us-schedule-c-and-se-computation` |

**Who must file (2025 rules; the 2026 thresholds are not yet published).** Source: [DOR residency filing requirements](https://dor.georgia.gov/residency-filing-requirements).
- **Full-year resident.** Must file if any of these is true: they must file a federal return; they have income taxable in Georgia but not federally; their income exceeds the 2025 standard deduction for their status ($12,000 single, head of household, qualifying surviving spouse or married filing separately; $24,000 married filing jointly). This applies "as long as your legal residence is Georgia, even if you are absent from or live outside the State temporarily".
- **Part-year resident** (a legal resident of Georgia for only part of the year): must file if required to file a federal return, and completes Schedule 3.
- **Nonresident** who works in Georgia or has Georgia-source income (wages, Georgia lottery winnings, flow-through income, rents): must file if required to file a federal return. A legal resident of another state whose only Georgia activity is work as an employee need not file if that pay does not exceed the lesser of 5% of pay from all places or $5,000.

**Residency.** Form 500 Line 4 codes are full-year resident ("regardless of temporary living arrangements"), part-year resident and nonresident. DOR describes residency as legal residence (domicile); O.C.G.A. § 48-7-1 has more tests, so doubtful cases are referrals.

## Ask the client first

1. **Which tax year, and residency all year?** 2026 and 2025 have different rates, deductions and exemptions. Legal residence, move dates and whether the spouse had the same residency all year decide whether Schedule 3 is needed and whether to file jointly or separately.
2. **Federal filing status, federal AGI and what is in it**, and whether the client itemized federally. Georgia follows the federal deduction choice. Ask for Schedule C profit, wages, pensions and IRA distributions, taxable Social Security, interest (other states' bonds, U.S. obligations) and capital gains.
3. **Dates of birth and any permanent disability date** for taxpayer and spouse; for military retirees under 62, the military retirement pay and Georgia earned income. These drive the retirement exclusions.
4. **Dependents**, including unborn dependents (Line 7b). On separate returns only one spouse may claim a given dependent.
5. **The business and pass-throughs:** was federal bonus depreciation (section 168(k)) claimed this year or earlier, or a bonus-depreciated asset sold? Does the client own part of an entity that elected to pay Georgia tax at the entity level?
6. **2026 only:** qualified overtime (full-time hourly employees only) and cash tips, with the employer's figures. **Other states:** income taxed by another state, with a copy of that return. **Payments:** Georgia withholding, estimates and any extension payment.

## The method, step by step

Form 500 line numbers are from the 2025 return; the 2026 IT-511 booklet was not published when this was read. Part-year residents and nonresidents skip Lines 9 to 14 and use Schedule 3 (step 9). Source for the line structure: [2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download).

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Flat rate on Georgia taxable income, taxable years beginning on or after 1 January 2026 | 4.99% | [HB 463 (2026), O.C.G.A. § 48-7-20](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) |
| Standard deduction, married filing jointly | $30,000 | [HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) |
| Standard deduction, single, head of household or married filing separately | $15,000 | same |
| Dependent exemption, per dependent | $5,000 | same |
| Personal exemption for taxpayer or spouse (none after 31 December 2023) | $0 | [2026 Form 500-ES](https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download) |
| Retirement income exclusion, age 62 to 64, or under 62 and permanently disabled, per qualifying spouse | $35,000 | [HB 463 (2026), O.C.G.A. § 48-7-27(a)(5)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) |
| Retirement income exclusion, age 65 or older, per qualifying spouse (taxable years ending on or before 31 December 2026) | $65,000 | same |
| Earned income that can count toward the retirement exclusion | $5,000 | [2025 IT-511 booklet, Schedule 1](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download) |
| Military retirement exclusion, under 62, base | $17,500 | [2025 IT-511 booklet, Subtraction 2](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download) |
| Military retirement exclusion, additional amount if Georgia earned income exceeds $17,500 | $17,500 | same |
| Overtime exclusion, full-time hourly employees, taxable years 2026 to 2028 | $1,750 | [HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates) |
| Cash tips exclusion, taxable years beginning on or after 1 January 2026 | $1,750 | same |
| Path2College 529 contribution subtraction, per beneficiary (joint return $8,000) | $4,000 | [2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download) |
| Low income credit: federal AGI must be under | $20,000 | same |
| Net operating loss from 2018 onward, maximum share of Georgia income before the NOL | 80% | same |

**2025 figures (for 2025 returns):** rate 5.19% ([HB 111 (2025)](https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download)); standard deduction $12,000 or $24,000 and dependent exemption $4,000 (the struck-through amounts in [HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download)).

**How the rate moves after 2026.** HB 463 sets 4.99% "for taxable years beginning on or after January 1, 2026", then cuts it by 0.125 of a point each year from 1 January 2027 until it reaches 3.99%. It also raises the joint standard deduction by $750 a year to $36,000, the single, head of household and separate deduction by $375 a year to $18,000, the dependent exemption by $125 a year to $6,000, and the 65-and-older retirement exclusion to $70,000. Each step is delayed one year for each year that, as of 1 December, any of these holds: the Governor's revenue estimate for the next fiscal year is not at least 3% above the current year's; the prior fiscal year's net revenue was not higher than each of the three preceding years'; the Revenue Shortfall Reserve does not exceed the projected cost of the cut. The Office of Planning and Budget reports by 1 December; do not quote a 2027 figure before then. The 2026 Form 500-ES worksheet still prints the 2025 amounts; use the HB 463 amounts for 2026.

### From federal AGI to Georgia taxable income

1. **Line 8, federal AGI** from Form 1040, not federal taxable income. A sole proprietor's Schedule C profit, the deduction for half of self-employment tax, self-employed health insurance and SEP or solo 401(k) contributions are inside federal AGI and flow through with no Georgia entry. In the booklet's words: "Georgia does not allow the 20% qualified business income deduction (I.R.C. Section 199A). However, since Georgia starts with Federal AGI, no adjustment is necessary on the Georgia return."
2. **Line 9, Schedule 1 adjustments.**
   - Additions include interest and dividends from non-Georgia municipal bonds, and adjustments for federal provisions Georgia has not adopted, such as section 168(k) bonus depreciation. Owners of an entity that elected to pay tax at the entity level add their share of entity-level losses (Schedule 1 Line 5, described PTEADD).
   - Subtractions include the retirement and military retirement exclusions, Social Security and Railroad Retirement in federal AGI, U.S. obligation interest, other states' income tax refunds, Path2College 529 contributions, the HB 1000 surplus refund if it is in federal AGI, and for owners of an electing entity their share of income taxed at the entity level (Schedule 1 Line 12, described PTEDED).
   - For 2026, Farmer Bridge Assistance Program and Assistance for Specialty Crop Farmers Program payments are excluded "subject to certain conditions" ([DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates)); refer if they apply.
3. **Line 10, Georgia AGI** = Line 8 plus or minus Line 9.
4. **Line 11 or 12, deduction.** Federal standard deduction taken: take the Georgia standard deduction. Itemized federally, or married filing separately with a spouse who itemizes: itemize in Georgia. Georgia itemized deductions are federal Schedule A (Line 12a) less income taxes paid to other states and investment interest for income exempt from Georgia tax (Line 12b).
5. **Line 14, dependent exemption:** Line 7c (Line 7a qualified dependents plus Line 7b unborn dependents) times $5,000. An unborn child born in the same year goes on Line 7a.
6. **Lines 15a to 15c, taxable income.** Line 15a = Line 10 minus the deduction minus Line 14. Line 15b is any Georgia NOL (80% limit for losses from 2018 onward, based on Georgia taxable net income; no carryback and an unlimited carryforward; farm and certain insurance losses have their own carryback rules). Line 15c is Georgia taxable income.
7. **Line 16, tax** = Line 15c times 4.99% (2026) or 5.19% (2025), rounded to the nearest dollar.
8. **Credits.**
   - Line 17, low income credit: federal AGI under $20,000 and not claimed, or eligible to be claimed, as a dependent.
   - Line 18, credit for tax paid to other states: state (including DC) and U.S. local income tax on net income only, never foreign tax; the income must be taxable in both places; attach the other state's return or the credit is refused. Not available for income taxed at the entity level by Georgia.
   - Line 19, the Georgia eligible itemizer credit (2025 only, see below), and Line 20, IND-CR credits.
9. **Part-year residents and nonresidents: Schedule 3.** Column A is income as if a full-year resident, B is income not taxable to Georgia, C is Georgia income (A = B + C). The Line 9 ratio is Line 8 Column C divided by Line 8 Column A, not below zero nor above 100%; zero if Georgia AGI is zero or negative, 100% if the adjusted federal AGI is zero or negative. Line 10 is the deduction, Line 11 dependents times the exemption, Line 12 = Lines 10 + 11, Line 13 = Line 12 times the ratio, Line 14 = Line 8 Column C minus Line 13, carried to Form 500 Line 15a.
10. **Payments and balance.** Withholding from W-2s and 1099s (Line 24), G2-A, G2-FL, G2-LP and G2-RP withholding (Line 25), estimated and extension payments (Line 26) and refundable credits (Line 27, electronic filing only). Then the Form 500 UET penalty (Line 42, see `ga-estimated-tax-depth`), late filing and late payment penalties (Line 43) and interest (Line 44).

### Retirement income exclusion

Source: [2025 IT-511 booklet, Schedule 1](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download).
- **Each spouse qualifies separately** on a joint return, by their own age or disability. Jointly owned income is split 50/50; otherwise income belongs to the spouse who owns it.
- **Disability route (under 62):** permanently disabled "to such an extent that they are unable to perform any type of gainful employment"; the disability date goes on the return.
- **Counts:** interest, dividends, alimony, capital gains, other income, taxable IRA distributions and pensions, rent and royalties, and up to $5,000 of earned income (wages, self-employment income, rental, royalty or partnership income subject to self-employment tax, S corporation income with material participation).
- **Does not count:** Social Security and Railroad Retirement (subtracted in full anyway), exempt interest and other income not taxable to Georgia, and lottery, gambling or illegal income.
- **Part-year residents and nonresidents** prorate the earned portion by Georgia-source earned income over total earned income, and the unearned portion by Georgia-source unearned retirement income over total, both computed as if a full-year resident.
- **2027:** only the 65-and-older amount rises (to $70,000, subject to the delay tests); HB 463 limits the $35,000 and $65,000 division to years "ending on or before December 31, 2026".

### Military retirement income exclusion

Source: [2025 IT-511 booklet, Subtraction 2](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download).
- Only for taxpayers under 62: up to $17,500, plus a second $17,500 only if Georgia earned income is more than $17,500 (the worksheet stops below $17,501). Combined maximum $35,000, never more than the taxable military retirement received. Each spouse qualifies separately.
- Part-year residents and nonresidents claim the base $17,500 against all military retirement received, and reach the extra $17,500 only through Georgia-source earned income.
- From age 62 the general retirement exclusion covers "retirement income from any source" (HB 463 text of O.C.G.A. § 48-7-27(a)(5)(A)).

### Overtime and cash tips, 2026 to 2028 only

Georgia did not adopt the federal tips and overtime deductions of P.L. 119-21. It has its own exclusions ([HB 463 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download); [DOR important tax updates](https://dor.georgia.gov/taxes/important-tax-updates)):
- **Overtime:** up to $1,750 of "qualified overtime compensation" (as defined in IRC section 225) received by a full-time employee paid by an hourly wage, for taxable years beginning on or after 1 January 2026 and ending on 31 December 2028. Salaried and part-time workers do not qualify. Employers under the federal Railway Labor Act use their collective bargaining agreements' definition.
- **Cash tips:** up to $1,750, where "cash tips" includes tips "paid in cash or charged" and, for an employee, tips under a tip-sharing arrangement. The tips must be voluntary, not negotiated, with the amount set by the payer; the occupation must customarily receive tips, have a Treasury Tipped Occupation Code and not be excluded under IRC section 63.
- Both "stand repealed and reserved on December 31, 2028". Neither applies to 2025. The 2026 Schedule 1 line is not yet published. Employers report the amounts on the 2026 W-2 and 1099 with Form G-1003; reporting them does not reduce withholding ([2026 Employer's Tax Guide](https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download)).

### Federal conformity and bonus depreciation

Source: [HB 1199 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download); [DOR federal tax changes](https://dor.georgia.gov/taxes/tax-rules-and-policies/income-tax-federal-tax-changes).
- HB 1199, signed 20 March 2026, defines the Internal Revenue Code as federal law "enacted on or before January 1, 2026", for "all taxable years beginning on or after January 1, 2025". So 2025 and 2026 returns start from an IRC that includes P.L. 119-21, apart from the provisions it lists. The 2025 IT-511 booklet predates HB 1199 and says Georgia has not adopted P.L. 119-21; follow HB 1199.
- Treated as not in effect: section 168(k) bonus depreciation, section 174A, section 163(h)(4) (federal car loan interest), section 179(d)(1)(B)(ii) and section 199. Sections 163(j) and 174 apply as they stood before the 2017 federal act.
- Excess business losses: DOR's federal tax changes page says Georgia applies the section 461(l) limitation as before the CARES Act and did not adopt the later extensions, so "for taxable years beginning on or after January 1, 2026, the Code Section 461(l) limitation is set to expire for Georgia purposes". A 2026 loss limited federally may need a Georgia subtraction; refer if material.
- Bonus depreciation steps: attach federal Form 4562; add back federal depreciation on the other addition line; compute Georgia depreciation without 168(k) on Georgia Form 4562 and enter it on the other subtraction line; attach a statement. A sale of a bonus-depreciated asset has its own Georgia gain or loss adjustment.

### Surplus refund under HB 1000

Source: [HB 1000 (2026)](https://gov.georgia.gov/document/2026-signed-legislation/hb-1000/download); [DOR HB 1000 FAQs](https://dor.georgia.gov/2025-hb-1000-surplus-tax-refund-faqs).
- **Who:** an individual who filed Georgia returns for both 2024 and 2025 by the 2025 due date including extension (15 October 2026). Excluded: nonresident aliens, estates and trusts, and anyone claimed as a dependent for 2024 unless they had 2024 earned income. ITIN filers: DOR's FAQ answers "Maybe"; DOR writes to them for more information before deciding, and lists filing with an ITIN among the common reasons a refund was not received.
- **Amount:** the lesser of the 2024 tax (2024 Form 500 Line 16, or Form 500EZ Line 4) and $250 (single or separate), $375 (head of household) or $500 (joint). A 2024 liability of $0 means no refund. Part-year residents and nonresidents prorate by the 2024 Schedule 3 Line 9 ratio.
- **Payment and tax:** credited automatically after the 2025 return is filed, by the refund method on that return, after offsets, without interest. Not taxable for Georgia; subtract it on Schedule 1 if it is in federal AGI. DOR says it may be federally taxable if the client itemized, deducted state income tax and got a benefit.

### 2025 returns (due 15 April 2026, or 15 October 2026 on extension)

Source: [2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download).
- Rate 5.19%, deductions $12,000 or $24,000, dependent $4,000; no overtime or tips exclusion.
- Form 500EZ is discontinued from 2025; everyone files Form 500.
- Georgia eligible itemizer credit (Line 19): up to $300 per taxpayer, for a full-year or part-year resident who itemized and either lived in Georgia 183 days or more or was living there on the last day of the year; limited to the tax, no carryforward.
- Child and dependent care credit (credit code 202): 50% of the federal credit.
- Hurricane Helene subtractions apply only to the extent the amount is in federal AGI; the crop insurance subtraction is 2025 only; the agricultural disaster relief payments subtraction runs 2025 to 2029.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Taxpayer turned 62 during the year | Age-based retirement exclusion, not the military exclusion (the worksheet asks "Are you under the age of 62?") |
| Taxpayer 61, disabled, can still do some paid work | No exclusion through the disability route: the disability must prevent any gainful employment |
| One spouse 66, the other 60 and not disabled | Only the 66-year-old claims an exclusion |
| Retiree with wages above $5,000 | Only $5,000 of the wages counts toward the exclusion |
| Military retiree under 62 with Georgia earned income of exactly $17,500 | Base exclusion only; the extra needs more than $17,500 |
| Hourly part-time worker with overtime in 2026 | No Georgia overtime exclusion |
| Nonresident employee whose Georgia pay does not exceed the lesser of 5% of total pay or $5,000 | No Georgia return needed |
| Owner of an entity that elected to pay Georgia tax at entity level | Subtract the share (PTEDED); no credit for the entity's Georgia tax |
| Client took the federal standard deduction but Georgia itemizing would be larger | Not allowed: Georgia follows the federal choice |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Residency dates | Full-year resident only if domicile was Georgia all year; otherwise ask before Schedule 3 |
| Federal deduction choice | Ask; it binds the Georgia choice |
| Dates of birth | No retirement exclusion until ages are confirmed |
| Bonus depreciation history | Ask for prior Georgia Form 4562 schedules; no Georgia depreciation subtraction until rebuilt |
| Overtime and tips figures | No exclusion until the employer's W-2 or 1099 figures are in hand |

## Worked cases

Client facts are invented; rates and amounts are the 2026 figures above.

**Case 1: single sole proprietor, full-year resident.** Federal AGI $80,000, all Schedule C profit. No Schedule 1 adjustments, federal standard deduction, no dependents. Georgia AGI $80,000, less the $15,000 standard deduction, gives taxable income $65,000. Tax: $65,000 x 4.99% = $3,243.50, rounded to $3,244. Had the 2025 figures ($12,000, 5.19%) been used by mistake, the tax would be $3,529.20: the year matters.

```oa-check
name: GA 2026 single sole proprietor, federal AGI 80,000
inputs:
  federal_agi: 80000
  standard_deduction: 15000
  rate: 0.0499
steps:
  - taxable: federal_agi - standard_deduction
  - tax: taxable * rate
  - tax_rounded: round(tax)
  - tax_on_2025_figures: (federal_agi - 12000) * 0.0519
expected:
  taxable: 65000
  tax: 3243.50
  tax_rounded: 3244
  tax_on_2025_figures: 3529.20
```

**Case 2: married filing jointly, spouses 66 and 63, both retired.** Each has a taxable pension of $60,000; they have $20,000 of jointly owned interest and $25,000 of taxable Social Security, so federal AGI is $165,000. Federal standard deduction, full-year residents, no dependents. Retirement income per spouse: $60,000 plus half the interest ($10,000) = $70,000. The 66-year-old's exclusion is capped at $65,000 and the 63-year-old's at $35,000. Subtractions: Social Security $25,000 plus exclusions $100,000. Georgia AGI $40,000, less $30,000, gives taxable income $10,000. Tax $499.

```oa-check
name: GA 2026 joint retirees aged 66 and 63
inputs:
  pension_each: 60000
  joint_interest: 20000
  social_security: 25000
  cap_65_plus: 65000
  cap_62_64: 35000
  standard_deduction: 30000
  rate: 0.0499
steps:
  - federal_agi: pension_each * 2 + joint_interest + social_security
  - retirement_each: pension_each + joint_interest / 2
  - exclusion: min(retirement_each, cap_65_plus) + min(retirement_each, cap_62_64)
  - georgia_agi: federal_agi - social_security - exclusion
  - taxable: max(georgia_agi - standard_deduction, 0)
  - tax: round(taxable * rate)
expected:
  federal_agi: 165000
  exclusion: 100000
  georgia_agi: 40000
  taxable: 10000
  tax: 499
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GA-RES | Residency in doubt (home elsewhere but much of the year in Georgia, unproven mid-year change of domicile) | Refer |
| R-GA-PTET | Entity-level election questions beyond the owner's PTEDED or PTEADD line | Use `ga-corporate-and-ptet` |
| R-GA-OBBBA | 2025 return that followed the booklet's conformity statement where a P.L. 119-21 change moved federal AGI | Check DOR's current guidance before filing or amending (Form 500X) |
| R-GA-DEPR | Multi-year bonus depreciation with no Georgia schedules, or sale of a bonus-depreciated asset | Rebuild the Georgia Form 4562 history first, or refer |
| R-GA-MULTI | Multistate business income: apportionment, S corporation income where another state does not recognise the election, the O.C.G.A. § 48-7-27(d) subtraction | Refer |
| R-GA-DEFCOMP | Nonresident's deferred compensation or stock options earned in Georgia earlier | Refer: federal limits interact with the 5% or $5,000 test |
| R-GA-CREDIT | IND-CR, Schedule 2, film, timber, rural hospital and other credits | Refer: preapproval and e-filing rules |
| R-GA-DISASTER | Hurricane Helene subtractions, disaster postponements | Refer |
| R-GA-MIL | Military serving outside the continental U.S., combat zone pay, spouses of nonresident military | Refer |
| R-GA-ASSESS | Assessments: 45-day protest and appeal windows from 1 July 2025; the Georgia Tax Court hears appeals from 1 July 2026 | Refer |

## Filing and payment

Source: [2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download); [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates).

1. **Due date:** 15 April 2027 for 2026 (15 April 2026 for 2025). Fiscal years: the 15th day of the fourth month after year-end.
2. **Extension:** attach a copy of federal Form 4868 (or the IRS confirmation) and file by the extended federal due date, or use Georgia Form IT-303 if there is no federal extension. Payment is not extended: pay by the original due date (Form IT-560 or the Georgia Tax Center) and report it on Line 26.
3. **Electronic filing is required** if the return uses a series 100 credit, if payments are made by electronic funds transfer, or for a paid preparer whenever the federal return must be e-filed. File through the Georgia Tax Center (gtc.dor.ga.gov) or approved software.
4. **Attachments:** federal pages 1 and 2 and Schedule 1 if Line 8 is $40,000 or more or less than the W-2 total; federal Schedule A if itemizing; the other state's return for the Line 18 credit.
5. **Payment:** through the Georgia Tax Center, or by check payable to the Georgia Department of Revenue with Form 525-TV. Payment agreements of up to 60 months are available once every return is filed.
6. **After filing:** refund claims must be made within three years from the later of the payment date and the return's due date including extensions.

| Penalty (individual income tax) | Rule | Maximum | Source |
| --- | --- | --- | --- |
| Late filing (O.C.G.A. § 48-7-57) | 5% of the tax not paid by the original due date, plus 5% for each additional month | 25% | [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates) |
| Late payment (§ 48-7-86) | 0.5% of the unpaid tax, plus 0.5% for each additional month | 25% | same |
| Negligent underpayment (§ 48-7-86) | 5% of the underpayment | none stated | same |
| Fraudulent underpayment (§ 48-7-86) | 50% of the underpayment | none stated | same |
| Frivolous return (§ 48-7-57.1) | $1,000 | $1,000 | same |
| Interest, months from 1 July 2016 | Federal Reserve prime rate plus 3% a year, reviewed each January | none | same |

Late filing and late payment penalties together cannot exceed 25% of the tax due on the return due date. The estimated tax penalty is in `ga-estimated-tax-depth`.

## Completion checklist

- Rate, standard deduction and dependent amounts match the tax year (4.99%, $15,000 or $30,000, $5,000 for 2026).
- Line 4 residency code correct; Schedule 3 used for part-year, nonresident and mixed-residency joint returns.
- Line 8 is federal AGI, not federal taxable income.
- Schedule 1 additions (non-Georgia municipal interest, federal depreciation where 168(k) was claimed, PTEADD) and subtractions (Social Security, U.S. obligation interest, other-state refunds, Georgia depreciation, PTEDED) entered.
- Retirement and military exclusions computed per spouse, with ages, caps and earned-income conditions checked.
- Deduction choice matches the federal return; dependents totalled on Line 7c.
- Form 500 UET reviewed (see `ga-estimated-tax-depth`).
- Federal pages attached where required; both spouses and any paid preparer sign.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| HB 463 (2026), signed text. Read for the 4.99% rate, the 0.125-point annual cuts to 3.99%, the delay tests, the $30,000 and $15,000 standard deductions, the $5,000 dependent exemption, the retirement exclusion amounts and the overtime and cash tips paragraphs. | https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download | 2026-11-13 |
| HB 111 (2025). Read for the 5.19% rate for 2025. | https://gov.georgia.gov/document/2025-signed-legislation/hb-111/download | 2026-11-13 |
| HB 1199 (2026). Read for the IRC conformity date and the provisions treated as not in effect. | https://gov.georgia.gov/document/2026-signed-legislation/hb-1199/download | 2026-11-13 |
| HB 1000 (2026). Read for the surplus refund eligibility and caps. | https://gov.georgia.gov/document/2026-signed-legislation/hb-1000/download | 2026-11-13 |
| DOR important tax updates. Read for "2026 Income Tax Changes": the 4.99% flat rate, the $15,000 and $30,000 deductions, the farmer payment exclusions and the $1,750 overtime and tips amounts. | https://dor.georgia.gov/taxes/important-tax-updates | 2026-11-13 |
| DOR income tax federal tax changes. Read for the NOL rules and the section 461(l) expiry for Georgia from 2026. | https://dor.georgia.gov/taxes/tax-rules-and-policies/income-tax-federal-tax-changes | 2026-11-13 |
| 2025 IT-511 individual income tax booklet. Read for the Form 500 line structure, Schedule 1, Schedule 3, the retirement and military exclusions, the low income credit, the NOL limit, attachments and filing rules. | https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download | 2026-11-13 |
| 2026 Form 500-ES. Read for the statement that there is no personal exemption after 2023 and for its worksheet amounts. | https://dor.georgia.gov/document/document/2026-500-es-estimated-tax-individuals-and-fiduciaries/download | 2026-11-13 |
| 2026 Employer's Tax Guide (updated September 2026). Read for the 2026 changes summary and the overtime and cash tips reporting rules. | https://dor.georgia.gov/document/document/2026-employers-tax-guide-updated-september-2026/download | 2026-11-13 |
| DOR residency filing requirements. Read for who must file and the 5% or $5,000 nonresident test. | https://dor.georgia.gov/residency-filing-requirements | 2026-11-13 |
| DOR HB 1000 surplus refund FAQs. Read for the ITIN answer, the common reasons for no refund and the tax treatment. | https://dor.georgia.gov/2025-hb-1000-surplus-tax-refund-faqs | 2026-11-13 |
| DOR penalty and interest rates. Read for the income tax penalty table and the prime plus 3% interest rule. | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |

Not yet confirmed: the 2026 IT-511 booklet and 2026 Form 500 were not published when read, so 2026 line numbers, the 2026 Schedule 1 lines for overtime, tips and any section 461(l) adjustment, the 2026 filing thresholds and the 2026 qualifying surviving spouse standard deduction (HB 463 does not name the status; 2025 used the single amount) are not confirmed; any 2027 rate or amount depends on the 1 December 2026 Office of Planning and Budget report.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ga-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ga-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
