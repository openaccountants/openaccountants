---
name: nc-income-tax
description: Compute North Carolina individual income tax on Form D-400 for tax year 2026, for a full-year resident, including sole proprietors and single-member LLC owners. Covers the flat 3.99% rate for 2026 (G.S. 105-153.7), the NC standard deduction ($12,750 single, $25,500 joint, $19,125 head of household), the child deduction by federal AGI band, NC itemized deductions with the $20,000 mortgage interest and property tax cap, the Schedule S additions (85% bonus depreciation and section 179 add-backs, other states' bond interest) and deductions (US obligations, Social Security, Bailey and military retirement), conformity to the Internal Revenue Code as of July 5, 2025, and the credit for tax paid to another state. Trigger on "North Carolina income tax", "NC income tax", "Form D-400", "D-400 Schedule S", "NC standard deduction", "NC child deduction", "NCDOR income tax".
version: "1.1"
jurisdiction: US-NC
tax_year: 2026
last_updated: 2026-11-28
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# North Carolina individual income tax, tax year 2026

This Guide computes the state tax on supported facts. The 2025 form references below are a crosswalk only: they are not verified 2026 filing instructions.

**Answer first.** For 2026, North Carolina taxes a resident's NC taxable income at one flat rate of **3.99%**. NC taxable income is federal adjusted gross income, plus the Schedule S additions, minus the Schedule S deductions, minus the NC standard deduction (or NC itemized deductions), minus the child deduction. The 2026 standard deduction is **$12,750** single or married filing separately, **$25,500** married filing jointly or surviving spouse, **$19,125** head of household. There are no personal exemptions, no extra amount for age 65 or blindness, and this Guide computes state tax only. The 2026 return is due **April 15, 2027**.

## Scope and who this is for

In scope: a full-year North Carolina resident individual filing Form D-400 for tax year 2026, including a sole proprietor or single-member LLC owner whose Schedule C profit is in federal AGI. The Guide produces the taxable-income and tax computation and a provisional D-400/Schedule S crosswalk. Do not file a 2026 return using unverified 2025 lines. [NCDOR publication timetable](https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/frequently-asked-questions-and-important-notices/faqs-regarding-recent-session-law-changes)

Out of scope, and where it goes:

| Topic | Guide |
| --- | --- |
| Federal AGI, Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| Federal section 179 and bonus depreciation amounts | `us-section-179-and-bonus-depreciation` |
| Bailey, military and Social Security retirement deductions in depth | `nc-bailey-settlement-retirement` |
| NC quarterly estimated tax (Form NC-40) and underpayment interest (Form D-422) | `nc-estimated-tax` |
| Employer withholding (NC-4, NC-5, NC-3) and unemployment insurance | `nc-payroll` |
| Corporate income and franchise tax, taxed pass-through entity election | `nc-corporate-tax` |
| Putting the federal and NC package together | `nc-return-assembly` |
| Consumer use tax beyond the D-400 line 18 entry | `nc-sales-tax` |

For resident filing liability, G.S. 105-153.8(a)(1) uses federal **gross income exceeding** the applicable NC statutory standard deduction, not AGI or taxable income. The Secretary can also require a return; filing may be needed to recover withholding even below that threshold. [G.S. 105-153.8](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.8.html)

## Ask the client first

1. **Resident of North Carolina for all of 2026?** A part-year resident or nonresident uses Schedule PN and a taxable percentage on line 13 (refer, see below).
2. **Filing status and qualifying children** for whom the federal child tax credit was allowed. Status sets the standard deduction; status, federal AGI and the number of children set the child deduction.
3. **Federal bonus depreciation (section 168(k)) and section 179 taken in 2026**, and the NC bonus and section 179 add-backs on the 2021 to 2025 NC returns (for the 20% recovery deductions).
4. **Mortgage interest, real estate taxes, charitable gifts, medical costs, gambling losses**: to test NC itemized deductions against the standard deduction.
5. **Retirement and other income**: Social Security, government pensions (Bailey), military retirement, US Treasury interest, other states' municipal bond interest.
6. **Income taxed by another state**, with that state's return: for the credit on Form D-400TC.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Individual income tax rate, taxable year 2026 | 3.99% | [G.S. 105-153.7(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html); [NCDOR Tax Rate Schedules](https://www.ncdor.gov/taxes-forms/tax-rate-schedules) |
| Rate for 2025 (prior year, for comparisons and amended returns) | 4.25% | [G.S. 105-153.7(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| 2027 trigger: FY 2025-2026 General Fund revenue must exceed this amount; amended trigger uses prior-year rate less 0.25 percentage point, floor 2.49%; not a verified 2027 rate | $33,042,000,000 | [S.L. 2026-41 §44.1, p.607](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf#page=607) |
| Standard deduction, married filing jointly or surviving spouse | $25,500 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, head of household | $19,125 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, single | $12,750 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, married filing separately (zero if the spouse itemizes, and zero for anyone not eligible for a federal standard deduction) | $12,750 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html); [NCDOR 2025 D-401, line 11](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Cap on NC itemized mortgage interest plus real estate taxes (both spouses combined) | $20,000 | [G.S. 105-153.5(a)(2)b](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Add-back of federal special accelerated depreciation (sections 168(k) and 168(n)), and of section 179 above the NC limits | 85% | [G.S. 105-153.6(a), (c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html) |
| Recovery of each add-back, in each of the next five years | 20% | [G.S. 105-153.6(a), (c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html) |
| NC section 179 dollar limitation / investment limitation (taxable years from 2013) | $25,000 / $200,000 | [G.S. 105-153.6(c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html) |
| Add-back of domestic research and experimental expenditures expensed under IRC 174A(a); then 25% deducted in each of the next four years | 80% | [NCDOR notice, 23 July 2026](https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income) (G.S. 105-153.6A) |
| Internal Revenue Code conformity date | July 5, 2025 | [NCDOR notice, 23 July 2026](https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income) |

**Child deduction per qualifying child, by federal AGI** ([G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)). Only for a child for whom the federal child tax credit under IRC section 24 is allowed. Each band runs from over the lower figure up to and including the upper figure.

| Per child | Married filing jointly / surviving spouse | Head of household | Single or married filing separately | Source |
| --- | --- | --- | --- | --- |
| $3,000 | up to $40,000 | up to $30,000 | up to $20,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $2,500 | $40,000 to $60,000 | $30,000 to $45,000 | $20,000 to $30,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $2,000 | $60,000 to $80,000 | $45,000 to $60,000 | $30,000 to $40,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $1,500 | $80,000 to $100,000 | $60,000 to $75,000 | $40,000 to $50,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $1,000 | $100,000 to $120,000 | $75,000 to $90,000 | $50,000 to $60,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $500 | $120,000 to $140,000 | $90,000 to $105,000 | $60,000 to $70,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| $0 | over $140,000 | over $105,000 | over $70,000 | [G.S. 105-153.5(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |

Use the statutory NC amounts, not federal inflation-adjusted deductions. NCDOR says 2026 returns will be published in January 2027. Every D-400, Schedule S and payment line below is the **2025 crosswalk**, subject to issued 2026 forms and instructions; no 2026 line is asserted. Do not infer an actual 2027 rate from the trigger row. S.L. 2026-41 §44.1 replaces the old “after 2025” schedule and the 0.50-point trigger, although the consolidated HTML still shows them. Its scheduled 2027–2029 rate is 3.49%, subject to the amended trigger; the actual trigger outcome is not resolved here. Check this point with one of our partner accountants.

### Step 1: federal AGI (D-400 line 6)

Take federal AGI from the completed federal return for the same tax year; do not assume the old Form 1040 line 11 reference applies to the issued 2026 form. North Carolina follows the Internal Revenue Code as in effect on July 5, 2025, so the July 2025 federal law (the One Big Beautiful Bill Act) flows into AGI except where NC decouples. A negative AGI is entered as negative.

### Step 2: additions (Schedule S Part A, to D-400 line 7)

Add, to the extent not in federal AGI ([G.S. 105-153.5(c), (c2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)):

- Interest on bonds of other states and their local governments (Part A line 1).
- **Bonus depreciation**: 85% of the federal section 168(k) or 168(n) deduction taken for 2026 (Part A line 3).
- **Section 179**: 85% of the amount by which the federal section 179 deduction exceeds what the NC $25,000 / $200,000 limits allow (Part A line 4).
- **Research and experimental expenditures**: 80% of the amount fully expensed federally under IRC 174A(a) (G.S. 105-153.6A, added by S.L. 2026-31).
- Any federal net operating loss deduction (Part A line 7); NC allows its own State net operating loss instead (G.S. 105-153.5(b)(16)).
- Gain deferred under IRC 1400Z-2(a), and gain excluded by the step-up under IRC 1400Z-2(c). On later federal inclusion, deduct only the same income previously included in NC taxable income under the deferral add-back; do not tax it twice (G.S. 105-153.5(c2)(5)–(7)).
- From 2023, expenses deducted federally to the extent allocable to income wholly excluded from gross income or wholly exempt from NC income tax (G.S. 105-153.5(c2)(20)).
- The applicable owner share of state, local or foreign income tax deducted by an S corporation, partnership, estate or trust (2025 Part A line 8; G.S. 105-153.5(c1)). Owner-basis/loss and entity-level-tax adjustments require the entity workpaper; do not infer them from cash distributions.

### Step 3: deductions (Schedule S Part B, to D-400 line 9)

Deduct, to the extent included in federal AGI ([G.S. 105-153.5(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)):

- Interest on US obligations and NC obligations ((b)(1); US interest is Part B line 18).
- **Social Security and Railroad Retirement benefits**, all of them ((b)(3); line 19).
- **Bailey** government retirement benefits only to the extent covered by the settlement court orders ((b)(5); line 20), and **uniformed services retirement pay** for members with at least 20 years’ service or medical retirement under 10 U.S.C. Chapter 61, plus qualifying Survivor Benefit Plan payments ((b)(5a); line 21). Severance pay is excluded; do not deduct the same payment under both provisions. Detail in `nc-bailey-settlement-retirement`.
- Refunds of state, local and foreign income taxes included in AGI ((b)(4)).
- **20% of each earlier bonus depreciation and section 179 add-back** (for 2026, from the 2021 to 2025 returns); the 2025 form put bonus recovery on line 23.
- 25% of an earlier R&E add-back in each of the four following years (G.S. 105-153.6A).
- The amount by which NC basis exceeds federal basis, in the year of disposal ((b)(7)).
- Income earned or received by an enrolled member of a federally recognized tribe, derived from activities on a federally recognized reservation while residing there; the statute includes qualifying reservation-situs intangibles and associated retirement income ((b)(6)).

**State NOL:** add back the federal NOL deduction, then determine the separate State NOL under G.S. 105-153.5A. A State loss has its own business/nonbusiness, capital-loss, section 1202, child-deduction and section 199A adjustments; the 2026 excess-business-loss rule must also be applied. Deduct a supported State loss from one of the preceding 15 years, applying it to the earliest succeeding year first and no more than current NC taxable income before the State NOL deduction. Do not impose the old blanket federal “post-2017 80%” rule. Federal carryforwards entering the State pool under subsection (f), multi-year remeasurement or an unsupported loss schedule need review before use. Check this point with one of our partner accountants. [G.S. 105-153.5A](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5A.html)

### Step 4: deduction for the year (D-400 line 11)

Take the larger of the NC standard deduction and NC itemized deductions (Schedule A). NC itemized deductions are only these ([G.S. 105-153.5(a)(2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)): charitable contributions allowed under IRC 170, excluding a qualified real-property donation used for an allocated G.S. 105-153.11 credit; qualified residence interest plus real estate property taxes, together capped at **$20,000** (shared between spouses); medical and dental expenses allowed under IRC 213; qualifying claim-of-right repayments (apply the separate 2026 conditions in G.S. 105-153.5(a)(2)d; an unresolved repayment is not a usable deduction—Check this point with one of our partner accountants.); and, from 2025, gambling losses allowed under IRC 165(d) to the extent not deducted in AGI ([S.L. 2026-41 §44.2](https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf#page=608), which controls over the not-yet-updated consolidated HTML). State income tax and sales tax are not NC itemized deductions, and the federal Schedule 1-A deductions are not NC deductions (2025 D-401). The overall limit of IRC 68 does not apply.

### Step 5: child deduction (D-400 line 10)

Number of qualifying children times the per-child amount from the table, using **federal AGI** (D-400 line 6), not NC income.

### Step 6: taxable income and tax (D-400 lines 12 to 15)

NC taxable income = line 6 + line 7 minus line 9, line 10b and line 11. A full-year resident carries it to line 14 (line 13 is the part-year or nonresident percentage). **Tax, line 15 = line 14 × 3.99%** (zero if line 14 is zero or less).

### Step 7: credits, use tax, payments (lines 16 to 28)

- Line 16, credits on Form D-400TC. The credit for income tax paid to another state ([G.S. 105-153.9](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.9.html)) requires the same income to be NC-taxed and sourced to, and taxed by, the other state regardless of residence (dual-resident relief requires the Secretary’s decision). The credit is the smaller of (a) NC tax before this credit times the share of NC-modified gross income taxed there and (b) net tax actually paid there, further capped at NC tax less other credits. Attach that return **and proof of payment**; a later refund of the foreign tax requires reversal of the related credit. No credit is allowed for other-state/DC tax on income eligible for the G.S. 105-153.5(c3) deduction. Entity-tax credits need the entity workpaper.
- Line 18, consumer use tax on untaxed purchases (see `nc-sales-tax`).
- Lines 20a and 20b, NC tax withheld (attach W-2s and 1099s showing NC withholding); line 21, estimated payments, extension payments and tax paid by a partnership or S corporation for a nonresident owner.
- Line 26e, interest on underpaid estimated tax (see `nc-estimated-tax`).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Schedule C profit | In federal AGI; apply NC modifications and the 3.99% rate to NC taxable income. Compute federal self-employment tax separately |
| Home office, self-employed health insurance, SEP or solo 401(k) | Start with the permitted federal-AGI treatment, then apply all relevant NC modifications; no blanket exemption from decoupling |
| Qualified business income deduction (IRC 199A) | Taken after AGI federally, so it never reaches NC; no NC equivalent |
| Hobby or business question | Start with the supported federal-AGI result, then apply NC modifications; unresolved federal classification is not a completed NC conclusion |
| Capital gains | Gains in the NC taxable base use the 3.99% rate; apply the stated basis/Opportunity Zone modifications first |
| Social Security | Deduct the covered benefits included in federal AGI; do not deduct an excluded amount twice |
| Private pensions, IRAs, 401(k), 403(b) | Amounts included in federal AGI remain in the NC base unless a specific NC deduction applies |
| Married filing separately, spouse itemizes | NC standard deduction is zero; must itemize |
| Federal standard deduction not allowed (for example a dual-status alien) | NC standard deduction is zero |
| Age 65 or blind | No extra NC standard deduction |
| Property sold that had a bonus or section 179 add-back | Ordinary adjustments leave basis unchanged. For an actual or deemed federal carryover-basis transfer on or after January 1, 2013 that meets G.S. 105-153.6(e), including its written forfeiture certification, the transferor/owners lose remaining bonus deductions and the transferee adds them to basis and depreciates over the remaining life; apply (g) to resulting differences. Do not automatically continue recoveries after any transfer; check the transaction first |
| Mortgage interest plus property tax above $20,000 | Capped at $20,000 combined for both spouses; for separate returns, actual payer claims, with over-cap proration by percentage paid, or income for joint-account payments |
| Gambling winnings and losses | Losses only as an NC itemized deduction, limited to the IRC 165(d) amount not already in AGI |
| Taxed partnership or taxed S corporation | Deduct eligible State-attributable income only if included in both entity NC taxable income and owner AGI; add corresponding State-attributable losses under G.S. 105-153.5(c3). Other-state entity-tax income and owner-basis adjustments need a separate supported reconciliation; see `nc-corporate-tax` |
| Local income-tax question | This Guide computes State tax only; no local levy conclusion is established here. Check this point with one of our partner accountants. |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Prior NC bonus or section 179 add-backs | Ask for the 2021 to 2025 NC Schedules S; without them, leave the recovery computation non-usable pending evidence; Check this point with one of our partner accountants. |
| Whether the client itemizes | Compare only after confirming eligibility (including spouse-itemizing restriction) and obtaining the itemized totals; do not file from an assumed standard deduction |
| Whether children qualified for the federal child tax credit | No child deduction until confirmed on federal Schedule 8812 |
| Residence all year | Resolve actual full-year residence; a missing or disputed residence fact prevents a completed resident computation |

## Worked cases

The original amounts, years and case facts are retained. Cents illustrate arithmetic; apply the issued return’s reporting and rounding rules before filing.

### Case 1: single sole proprietor with bonus depreciation

Federal AGI $90,000, after $20,000 of federal bonus depreciation on equipment bought in 2026. US Treasury interest of $1,000 is in AGI. No children, no itemizing. Addition: 85% × $20,000 = $17,000. Deduction: $1,000. NC income after Schedule S: $106,000. Less the single standard deduction of $12,750: taxable income $93,250. Tax at 3.99%: **$3,720.68**. Assuming no carryover-basis transfer or other event changing entitlement, in each of 2027 to 2031 the client deducts 20% of the $17,000 add-back ($3,400).

```oa-check
name: NC 2026 single, bonus depreciation add-back
inputs:
  fagi: 90000
  bonus: 20000
  us_interest: 1000
  std: 12750
  rate: 0.0399
steps:
  - addback: bonus * 0.85
  - nc_income: fagi + addback - us_interest
  - taxable: nc_income - std
  - tax: round(taxable * rate, 2)
  - recovery_each_year: addback * 0.20
expected:
  addback: 17000
  taxable: 93250
  tax: 3720.68
  recovery_each_year: 3400
```

### Case 2: married couple, itemize or take the standard deduction

Married filing jointly, federal AGI $110,000, two qualifying children. Mortgage interest $15,000 and property taxes $9,000 (together $24,000, capped at $20,000), charitable gifts $6,000. NC itemized: $26,000 against the $25,500 standard deduction, so they itemize. Child deduction: AGI is over $100,000 and up to $120,000, so $1,000 per child, $2,000. Taxable income $82,000; tax **$3,271.80**. Itemizing saves $500 × 3.99% = $19.95. Had charity been $1,000 lower, the standard deduction would win.

```oa-check
name: NC 2026 MFJ itemized versus standard, child deduction
inputs:
  fagi: 110000
  mortgage_interest: 15000
  property_tax: 9000
  charity: 6000
  std: 25500
  children: 2
  per_child: 1000
  rate: 0.0399
steps:
  - housing: min(mortgage_interest + property_tax, 20000)
  - itemized: housing + charity
  - deduction: max(itemized, std)
  - child_ded: children * per_child
  - taxable: fagi - deduction - child_ded
  - tax: round(taxable * rate, 2)
  - saving_from_itemizing: round((deduction - std) * rate, 2)
expected:
  itemized: 26000
  taxable: 82000
  tax: 3271.80
  saving_from_itemizing: 19.95
```

## When to refuse or refer

For unresolved outcomes in this table, do not file or claim a deduction/credit from this Guide alone. Check this point with one of our partner accountants.

| Situation | Action |
| --- | --- |
| Part-year resident or nonresident (Schedule PN, line 13 percentage) | Refer; this Guide covers full-year residents only |
| Corporate, S corporation or partnership return (CD-405, CD-401S, D-403), or a taxed pass-through entity election | Use `nc-corporate-tax` |
| Estate or trust (Form D-407) | Refer |
| Amended return (D-400 with Schedule AM) | Refer for review; the method here still sets the corrected figures |
| Residence in dispute (domicile, the 183-day presumption) | Refer to a reviewer |
| Credit for tax paid to a foreign country, or to several states | Flag for a reviewer before filing |
| Business incentive credits (Form NC-478), historic rehabilitation credits | Refer |
| A 2025 return affected by S.L. 2026-31 or 2026-41 (R&E, timber loss, gambling) | Refer; NCDOR says to file or amend under its 23 July 2026 notice |

## Filing and payment

| Obligation | When and how | Source |
| --- | --- | --- |
| Form D-400 for 2026, calendar year | April 15, 2027 | [G.S. 105-155(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html) |
| Extension | A valid automatic federal extension application gives the corresponding NC filing extension; certify it on the NC return (2025: "Federal Extension" circle). Disaster extensions under IRC 7508A follow separate rules. Otherwise Form D-410 by the due date. Filing extension does not extend payment | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Late filing penalty | 5% per month or part, maximum 25%, on the applicable unpaid/additional tax; a valid filing extension affects the filing due date | [G.S. 105-236(a)(3)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Late payment penalty (until July 1, 2030) | 5% of the applicable net tax due; statutory exceptions include amended tax paid with the amended return and qualifying proposed-assessment payments within 45 days; check G.S. 105-236(a)(4) before applying. The 2025 D-401 also gives relief from automatic late-payment penalty with a valid extension, at least 90% paid by the original due date, and the balance plus interest paid by the extended due date; confirm the issued 2026 instructions before using that administrative treatment | [G.S. 105-236(a)(4)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Negligence penalty | 10% of the negligence deficiency; an individual taxable-income understatement of at least 25% of gross income attracts the separate 25% deficiency rule, and fraud/negligence penalties are not duplicated | [G.S. 105-236(a)(5)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Interest on late tax | 7% a year for 1 January 2025 to 31 December 2026; 8% for 1 January to 30 June 2027 | [NCDOR interest rate](https://www.ncdor.gov/interest) |
| Payment | Online on the NCDOR website, or check with Form D-400V to NCDOR, PO Box 25000, Raleigh, NC 27640-0640 | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Estimated tax for 2026 | April 15, June 15, September 15 2026 and January 15 2027; test the statutory $1,000/no-prior-liability exceptions and applicable installment method rather than treating dates as liability | [G.S. 105-163.15](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.15.html) |

## Completion checklist

- [ ] Residence for all of 2026 confirmed
- [ ] Federal AGI ties to the completed same-year federal return, without assuming a 2026 federal line number
- [ ] Bonus, section 179 and R&E add-backs computed; prior-year 20% recoveries listed by year
- [ ] Social Security, Bailey and military deductions supported by attached 1099s
- [ ] Standard against itemized compared, $20,000 housing cap applied
- [ ] Child deduction uses federal AGI and the federal child tax credit count
- [ ] Rate 3.99% applied; withholding and estimates tie to W-2s, 1099s and NC-40 records
- [ ] Credit for tax paid to another state supported by that state's return

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 2026 rate and original trigger text; S.L. 2026-41 §44.1 controls the amended future schedule/trigger | 2026-11-27 |
| G.S. 105-153.5 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | Read for standard, itemized and child deductions, additions and deductions | 2026-11-27 |
| G.S. 105-153.6 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html | Read for the 85% bonus and section 179 add-backs and the $25,000 / $200,000 limits | 2026-11-27 |
| G.S. 105-153.9 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.9.html | Read for the credit for tax paid to another state | 2026-11-27 |
| G.S. 105-155 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html | Read for the April 15 due date | 2026-11-27 |
| G.S. 105-236 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html | Read for late filing, late payment and negligence penalties | 2026-11-27 |
| NCDOR Tax Rate Schedules | https://www.ncdor.gov/taxes-forms/tax-rate-schedules | Read for 4.25% in 2025 and 3.99% for 2026; future schedule subject to operative Session Law | 2026-11-27; confirmed 2026-11-28 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for D-400 and Schedule S line numbers, extension, penalties, payment | 2026-11-27 |
| NCDOR notice on S.L. 2026-31 and 2026-41 (23 July 2026, updated 9 October 2026) | https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income | Read for the July 5, 2025 IRC conformity date, the R&E add-back and the gambling loss deduction | 2026-11-27 |
| NCDOR FAQs on recent Session Law changes | https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/frequently-asked-questions-and-important-notices/faqs-regarding-recent-session-law-changes | Read for 2026 returns being published in January 2027 | 2026-11-27 |
| S.L. 2026-41 §§44.1–44.2, pages 607–608 | https://www.ncleg.gov/EnactedLegislation/SessionLaws/PDF/2025-2026/SL2026-41.pdf#page=607 | Read for the amended future rate schedule/0.25-point trigger and gambling deduction effective from 2025; operative session law controls over consolidated HTML | 2026-11-27 |
| G.S. 105-153.5A, 105-153.6A | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5A.html | Read for State NOL computation/carryforward and historical federal-pool conditions; R&E quote also read at https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6A.html | 2026-11-27 |
| G.S. 105-153.8, 105-163.15 and 105-263 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.8.html | Read for resident gross-income filing requirement, quarterly installment dates/exceptions and extension/payment distinction | 2026-11-27 |
| G.S. 105-153.4 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.4.html | Read for resident modified-AGI base | 2026-11-28 |
| NCDOR interest rate | https://www.ncdor.gov/interest | Read for 7% through 2026 and 8% from January 2027 | 2026-11-27 |

Not yet confirmed: issued 2026 D-400, Schedule S and D-401 line mappings and reporting/rounding directions (NCDOR says publication January 2027); actual 2027 trigger outcome; any local-income-tax conclusion; individual claim-of-right, transitional NOL, entity-tax/basis, residency or transfer outcome lacking the records required above. These are explicit non-usable holds. Check this point with one of our partner accountants.
