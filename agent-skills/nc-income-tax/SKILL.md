---
name: nc-income-tax
description: "Compute North Carolina individual income tax on Form D-400 for tax year 2026, for a full-year resident, including sole proprietors and single-member LLC owners. Covers the flat 3.99% rate for 2026 (G.S. 105-153.7), the NC standard deduction ($12,750 single, $25,500 joint, $19,125 head of household), the child deduction by federal AGI band, NC itemized deductions with the $20,000 mortgage interest and property tax cap, the Schedule S additions (85% bonus depreciation and section 179 add-backs, other states' bond interest) and deductions (US obligations, Social Security, Bailey and military retirement), conformity to the Internal Revenue Code as of July 5, 2025, and the credit for tax paid to another state. Trigger on \"North Carolina income tax\", \"NC income tax\", \"Form D-400\", \"D-400 Schedule S\", \"NC standard deduction\", \"NC child deduction\", \"NCDOR income tax\". NC has no local income tax."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-income-tax"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina individual income tax, tax year 2026

> **Source-cited draft.** Built from G.S. 105-153.5, 105-153.6, 105-153.7, 105-153.9, 105-155 and 105-236, the NCDOR Tax Rate Schedules page, the NCDOR 2025 D-401 instructions and the NCDOR notice of 23 July 2026 on Session Laws 2026-31 and 2026-41, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, North Carolina taxes a resident's NC taxable income at one flat rate of **3.99%**. NC taxable income is federal adjusted gross income, plus the Schedule S additions, minus the Schedule S deductions, minus the NC standard deduction (or NC itemized deductions), minus the child deduction. The 2026 standard deduction is **$12,750** single or married filing separately, **$25,500** married filing jointly or surviving spouse, **$19,125** head of household. There are no personal exemptions, no extra amount for age 65 or blindness, and no local income tax. The 2026 return is due **April 15, 2027**.

## Scope and who this is for

In scope: a full-year North Carolina resident individual filing Form D-400 for tax year 2026, including a sole proprietor or single-member LLC owner whose Schedule C profit is in federal AGI. The skill produces D-400 lines 6 to 15 and the Schedule S entries most such clients need.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal AGI, Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| Federal section 179 and bonus depreciation amounts | `us-section-179-and-bonus-depreciation` |
| Bailey, military and Social Security retirement deductions in depth | `nc-bailey-settlement-retirement` |
| NC quarterly estimated tax (Form NC-40) and underpayment interest (Form D-422) | `nc-estimated-tax` |
| Employer withholding (NC-4, NC-5, NC-3) and unemployment insurance | `nc-payroll` |
| Corporate income and franchise tax, taxed pass-through entity election | `nc-corporate-tax` |
| Putting the federal and NC package together | `nc-return-assembly` |
| Consumer use tax beyond the D-400 line 18 entry | `nc-sales-tax` |

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
| Individual income tax rate, taxable years beginning after 2025 | 3.99% | [G.S. 105-153.7(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html); [NCDOR Tax Rate Schedules](https://www.ncdor.gov/taxes-forms/tax-rate-schedules) |
| Rate for 2025 (prior year, for comparisons and amended returns) | 4.25% | [G.S. 105-153.7(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| Rate reduction trigger for 2027: General Fund revenue for FY 2025-2026 above this amount cuts the rate by 0.5 point (never below 2.49%) | $33,042,000,000 | [G.S. 105-153.7(a1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| Standard deduction, married filing jointly or surviving spouse | $25,500 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, head of household | $19,125 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, single | $12,750 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Standard deduction, married filing separately (zero if the spouse itemizes, and zero for anyone not eligible for a federal standard deduction) | $12,750 | [G.S. 105-153.5(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html); [NCDOR 2025 D-401, line 11](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Cap on NC itemized mortgage interest plus real estate taxes (both spouses combined) | $20,000 | [G.S. 105-153.5(a)(2)b](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Add-back of federal bonus depreciation (section 168(k)), and of section 179 above the NC limits | 85% | [G.S. 105-153.6(a), (c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html) |
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

None of these amounts is indexed for inflation. NCDOR publishes the 2026 returns in January 2027; until then the line numbers below are the 2025 form's.

### Step 1: federal AGI (D-400 line 6)

Take federal AGI from Form 1040 line 11. North Carolina follows the Internal Revenue Code as in effect on July 5, 2025, so the July 2025 federal law (the One Big Beautiful Bill Act) flows into AGI except where NC decouples. A negative AGI is entered as negative.

### Step 2: additions (Schedule S Part A, to D-400 line 7)

Add, to the extent not in federal AGI ([G.S. 105-153.5(c), (c2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)):

- Interest on bonds of other states and their local governments (Part A line 1).
- **Bonus depreciation**: 85% of the federal section 168(k) deduction taken for 2026 (Part A line 3).
- **Section 179**: 85% of the amount by which the federal section 179 deduction exceeds what the NC $25,000 / $200,000 limits allow (Part A line 4).
- **Research and experimental expenditures**: 80% of the amount fully expensed federally under IRC 174A(a) (G.S. 105-153.6A, added by S.L. 2026-31).
- Any federal net operating loss deduction (Part A line 7); NC allows its own State net operating loss instead (G.S. 105-153.5(b)(16)).
- Gain deferred or excluded under the Opportunity Zone rules (IRC 1400Z-2).
- Expenses deducted federally that relate to income exempt from NC tax (from 2023).
- An S corporation, partnership or trust owner's share of state, local or foreign income tax the entity deducted (Part A line 8).

### Step 3: deductions (Schedule S Part B, to D-400 line 9)

Deduct, to the extent included in federal AGI ([G.S. 105-153.5(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)):

- Interest on US obligations and NC obligations ((b)(1); US interest is Part B line 18).
- **Social Security and Railroad Retirement benefits**, all of them ((b)(3); line 19).
- **Bailey** government retirement benefits ((b)(5); line 20) and **uniformed services retirement pay** for 20-year or medically retired members and Survivor Benefit Plan payments ((b)(5a); line 21). Detail in `nc-bailey-settlement-retirement`.
- Refunds of state, local and foreign income taxes included in AGI ((b)(4)).
- **20% of each earlier bonus depreciation and section 179 add-back** (for 2026, from the 2021 to 2025 returns); the 2025 form put bonus recovery on line 23.
- 25% of an earlier R&E add-back in each of the four following years (G.S. 105-153.6A).
- The amount by which NC basis exceeds federal basis, in the year of disposal ((b)(7)).
- Income of an enrolled tribal member earned on the reservation while living there ((b)(6)).

### Step 4: deduction for the year (D-400 line 11)

Take the larger of the NC standard deduction and NC itemized deductions (Schedule A). NC itemized deductions are only these ([G.S. 105-153.5(a)(2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)): charitable contributions allowed under IRC 170; qualified residence interest plus real estate property taxes, together capped at **$20,000** (shared between spouses); medical and dental expenses allowed under IRC 213; certain repayments of income included in an earlier year; and, from 2025, gambling losses allowed under IRC 165(d) to the extent not deducted in AGI (S.L. 2026-41). State income tax and sales tax are not NC itemized deductions, and the federal Schedule 1-A deductions are not NC deductions (2025 D-401). The overall limit of IRC 68 does not apply.

### Step 5: child deduction (D-400 line 10)

Number of qualifying children times the per-child amount from the table, using **federal AGI** (D-400 line 6), not NC income.

### Step 6: taxable income and tax (D-400 lines 12 to 15)

NC taxable income = line 6 + line 7 minus line 9, line 10 and line 11. A full-year resident carries it to line 14 (line 13 is the part-year or nonresident percentage). **Tax, line 15 = line 14 × 3.99%** (zero if line 14 is zero or less).

### Step 7: credits, use tax, payments (lines 16 to 28)

- Line 16, credits on Form D-400TC. The credit for income tax paid to another state ([G.S. 105-153.9](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.9.html)) is the smaller of (a) NC tax times the share of NC-modified gross income that the other state taxed, and (b) the net tax actually paid to that state. Attach the other state's return.
- Line 18, consumer use tax on untaxed purchases (see `nc-sales-tax`).
- Lines 20a and 20b, NC tax withheld (attach W-2s and 1099s showing NC withholding); line 21, estimated payments, extension payments and tax paid by a partnership or S corporation for a nonresident owner.
- Line 26e, interest on underpaid estimated tax (see `nc-estimated-tax`).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Schedule C profit | In federal AGI; taxed at 3.99%. NC has no separate self-employment tax; the federal one stays federal |
| Home office, self-employed health insurance, SEP or solo 401(k) | Follow federal AGI; no NC adjustment |
| Qualified business income deduction (IRC 199A) | Taken after AGI federally, so it never reaches NC; no NC equivalent |
| Hobby or business question | NC follows the federal result through AGI |
| Capital gains | Taxed at the same 3.99% flat rate; no preferential rate |
| Social Security | Fully deducted, whatever the income level |
| Private pensions, IRAs, 401(k), 403(b) | Taxable; NC has no general retirement exclusion |
| Married filing separately, spouse itemizes | NC standard deduction is zero; must itemize |
| Federal standard deduction not allowed (for example a dual-status alien) | NC standard deduction is zero |
| Age 65 or blind | No extra NC standard deduction |
| Property sold that had a bonus or section 179 add-back | Basis is the same for NC and federal (G.S. 105-153.6(d)); keep taking the remaining 20% recoveries |
| Mortgage interest plus property tax above $20,000 | Capped at $20,000 combined for both spouses; joint obligations split by who paid, or by income for a joint account |
| Gambling winnings and losses | Losses only as an NC itemized deduction, limited to the IRC 165(d) amount not already in AGI |
| Taxed partnership or taxed S corporation | The owner deducts the NC-taxed share of income on Schedule S (G.S. 105-153.5(c3)); see `nc-corporate-tax` |
| Local income tax | None in North Carolina |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Prior NC bonus or section 179 add-backs | Ask for the 2021 to 2025 NC Schedules S; without them, take no recovery deduction |
| Whether the client itemizes | Use the standard deduction; ask for mortgage, property tax, charity and medical totals |
| Whether children qualified for the federal child tax credit | No child deduction until confirmed on federal Schedule 8812 |
| Residence all year | Treat as resident only if the client confirms domicile in NC all of 2026 |

## Worked cases

### Case 1: single sole proprietor with bonus depreciation

Federal AGI $90,000, after $20,000 of federal bonus depreciation on equipment bought in 2026. US Treasury interest of $1,000 is in AGI. No children, no itemizing. Addition: 85% × $20,000 = $17,000. Deduction: $1,000. NC income after Schedule S: $106,000. Less the single standard deduction of $12,750: taxable income $93,250. Tax at 3.99%: **$3,720.68**. In each of 2027 to 2031 the client deducts 20% of the $17,000 add-back ($3,400).

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

| Situation | Action |
| --- | --- |
| Part-year resident or nonresident (Schedule PN, line 13 percentage) | Refer; this skill covers full-year residents only |
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
| Extension | Automatic if the client has a federal extension: fill in the "Federal Extension" circle on page 1. Otherwise Form D-410 by the due date. An extension does not extend the time to pay | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Late filing penalty | 5% of the tax for each month or part, up to 25% | [G.S. 105-236(a)(3)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Late payment penalty (until July 1, 2030) | 5% of the tax | [G.S. 105-236(a)(4)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Negligence penalty | 10% of the deficiency due to negligence | [G.S. 105-236(a)(5)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |
| Interest on late tax | 7% a year for 1 January 2025 to 31 December 2026; 8% for 1 January to 30 June 2027 | [NCDOR interest rate](https://www.ncdor.gov/interest) |
| Payment | Online on the NCDOR website, or check with Form D-400V to NCDOR, PO Box 25000, Raleigh, NC 27640-0640 | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Estimated tax for 2026 | April 15, June 15, September 15 2026 and January 15 2027 | `nc-estimated-tax` |

## Completion checklist

- [ ] Residence for all of 2026 confirmed
- [ ] Federal AGI ties to Form 1040 line 11
- [ ] Bonus, section 179 and R&E add-backs computed; prior-year 20% recoveries listed by year
- [ ] Social Security, Bailey and military deductions supported by attached 1099s
- [ ] Standard against itemized compared, $20,000 housing cap applied
- [ ] Child deduction uses federal AGI and the federal child tax credit count
- [ ] Rate 3.99% applied; withholding and estimates tie to W-2s, 1099s and NC-40 records
- [ ] Credit for tax paid to another state supported by that state's return

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% rate after 2025 and the 2027 trigger | 2026-11-13 |
| G.S. 105-153.5 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | Read for standard, itemized and child deductions, additions and deductions | 2026-11-13 |
| G.S. 105-153.6 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html | Read for the 85% bonus and section 179 add-backs and the $25,000 / $200,000 limits | 2026-11-13 |
| G.S. 105-153.9 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.9.html | Read for the credit for tax paid to another state | 2026-11-13 |
| G.S. 105-155 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-155.html | Read for the April 15 due date | 2026-11-13 |
| G.S. 105-236 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html | Read for late filing, late payment and negligence penalties | 2026-11-13 |
| NCDOR Tax Rate Schedules | https://www.ncdor.gov/taxes-forms/tax-rate-schedules | Read for 4.25% in 2025 and 3.99% after 2025 | 2026-11-13 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for D-400 and Schedule S line numbers, extension, penalties, payment | 2026-11-13 |
| NCDOR notice on S.L. 2026-31 and 2026-41 (23 July 2026, updated 9 October 2026) | https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-impact-recently-enacted-laws-north-carolina-individual-and-corporate-income | Read for the July 5, 2025 IRC conformity date, the R&E add-back and the gambling loss deduction | 2026-11-13 |
| NCDOR FAQs on recent Session Law changes | https://www.ncdor.gov/taxes-forms/corporate-income-franchise-tax/frequently-asked-questions-and-important-notices/faqs-regarding-recent-session-law-changes | Read for 2026 returns being published in January 2027 | 2026-11-13 |
| NCDOR interest rate | https://www.ncdor.gov/interest | Read for 7% through 2026 and 8% from January 2027 | 2026-11-13 |

Not yet confirmed: the 2026 D-400, Schedule S and D-401 line numbers (2026 forms publish in January 2027; the 2025 numbers are used); whether the FY 2025-2026 revenue trigger was met, which would set a 2027 rate of 3.49% (the Office of State Controller report was not read); the State net operating loss rules of G.S. 105-153.5A (not read; v0.1 said "post-2017 NOLs limited to 80%", which is not repeated here); the D-400 filing requirement gross income chart (page 6 of the D-401, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
