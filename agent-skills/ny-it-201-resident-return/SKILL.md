---
name: ny-it-201-resident-return
description: "Prepare New York State Form IT-201 for a full-year New York resident, tax year 2026, with notes for 2025 returns still on extension. Covers New York adjusted gross income from federal AGI, the Form IT-225 modifications (A-201 for unincorporated business tax deducted federally, the Notice N-26-1 decoupling codes), the standard or itemized deduction, the 2026 rate schedule (3.90% to 10.9%) and the recapture worksheets above New York AGI of $107,650, New York City resident tax (3.078% to 3.876%) with the IT-219 UBT credit, the Yonkers 16.75% surcharge, MCTMT on self-employment earnings over $150,000 per zone, and the main credits. Trigger on \"IT-201\", \"New York resident return\", \"NY state income tax\", \"NYC resident tax\", \"IT-219\", \"Empire State child credit\", \"Yonkers surcharge\". Full-year residents only; part-year and nonresident cases go to ny-residency-leaving-new-york."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ny-it-201-resident-return"
  jurisdiction: "US-NY"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New York State resident return (Form IT-201), tax year 2026, with 2025 return notes

> **Source-cited draft.** Built from the 2026 Form IT-2105 instructions, the 2025 Form IT-201, IT-196, IT-219, IT-225 and Y-203 instructions, Notice N-26-1 and the Tax Department's residency, credit and standard deduction pages, read on 2026-11-06 and rechecked on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the New York State rates run from 3.90% to 10.9%; the first five brackets are lower than in 2025 (Chapter 59 of the Laws of 2025, Part A). The single standard deduction is $8,000 (joint $16,050). Above New York AGI of $107,650 the recapture worksheets apply. New York City residents add 3.078% to 3.876%; Yonkers residents add 16.75% of the net state tax. Self-employed people in the MCTD owe MCTMT only on a zone's net earnings over $150,000 for 2026 (it was $50,000 for 2025). The 2026 rates come from the 2026 estimated tax instructions ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)), because the 2026 Form IT-201 instructions are not published yet ([NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf)). 2025 returns use the 2025 Form IT-201 instructions ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)); returns on extension were due October 15, 2026.

## Scope and who this is for

- **Covers:** individuals who were New York State residents for the whole year and file Form IT-201. That includes the New York City resident tax, the Yonkers resident surcharge, the metropolitan commuter transportation mobility tax (MCTMT) on self-employment earnings, and the main New York additions, subtractions, deductions and credits.
- **Residents are taxed on all income, wherever it is earned.** New York City residents also pay city tax on all their income ([Tax Department residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)).
- **Does not cover:** part-year residents and nonresidents. They file Form IT-203; see the IT-203 instructions. It also does not cover fiduciary returns, amended returns, the NYC unincorporated business tax (UBT) return itself, the pass-through entity tax (PTET) election, or the detail of the resident credit for tax paid to another state (Form IT-112-R).
- **Federal first.** Form IT-201 starts from federal adjusted gross income (AGI), so the federal return must be finished first ([IT-201-I (2025), lines 1 through 19](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

## Ask the client first

- Which tax year (2025 or 2026)? What was the federal filing status? New York generally requires the same status. The exception is a married couple where only one spouse is a New York resident.
- Where was the client domiciled all year? Did they keep a permanent place of abode in New York State, in New York City or in Yonkers, and how many days (any part of a day counts) did they spend there? Keep the day-count records.
- Did the client move into or out of New York, New York City or Yonkers during the year? If so, this is a part-year case (see "When to refuse or refer").
- What public school district did the client live in on December 31? The return needs the district name and code number even if the client was away from the district for a while, their children went to school elsewhere, or they have no children in school ([IT-201-I (2025), school district name and code number](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- Get the finished federal return, W-2s, 1099s, Schedules C and SE, and any K-1s with New York modification statements (Form IT-204-IP).
- For the self-employed: where was the business carried on? How much of the net earnings from self-employment is allocated to the MCTMT district, Zone 1 or Zone 2? Was NYC UBT or MCTMT paid and deducted on the federal return?
- Did the client receive a pension or annuity? From what payer (New York State or local government, federal government, private plan, or IRA)? What is the client's date of birth, to check the age 59½ test?
- Did the client receive interest from other states' municipal bonds, or interest on US government bonds? Did they contribute to or withdraw from New York's 529 college savings program?
- Will the client itemize? Get real property taxes, state and local income taxes, mortgage interest, charitable gifts and medical costs.
- Get the children's ages at December 31, federal AGI, and whether the federal earned income credit was claimed or could have been.
- Get the estimated tax payments made (Form IT-2105), any Form IT-370 extension payment, and last year's New York AGI and tax (for the safe harbor).
- For any business: any bonus depreciation, qualified production property or research and experimental (R&E) expenditures?

## The method, step by step

1. **Confirm full-year residence** for New York State, and separately for New York City and Yonkers. You are a resident if you are domiciled there. You are also a resident if you keep a permanent place of abode there for substantially all of the year **and** spend 184 days or more there ([income tax definitions](https://www.tax.ny.gov/pit/file/pit_definitions.htm)). The same test applies to New York City and to Yonkers, with the city in place of the state ([residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)).
2. **Check the filing requirement.** A resident must file if they must file a federal return. Without a federal requirement, they must file if federal AGI plus New York additions was more than $4,000. For a single person who can be claimed as a dependent, the limit is $3,100. A resident also files to claim a refund of withholding or a refundable credit ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
3. **Copy federal lines 1 to 19** from the federal return, ending at federal AGI.
4. **Add New York additions** (lines 20 to 23): interest on other states' bonds, public employee 414(h) contributions, nonqualified New York 529 withdrawals, and Form IT-225 additions. Use the codes in the modifications table below.
5. **Subtract New York subtractions** (lines 24 to 31): New York and federal government pensions, taxable Social Security benefits, US government bond interest, the pension and annuity exclusion of up to $20,000, New York 529 contributions, and Form IT-225 subtractions. The result is New York AGI (line 33) ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
6. **Deduct the larger** of the New York standard deduction or the New York itemized deduction (Form IT-196). Then subtract $1,000 for each dependent. The result is taxable income (line 38) ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
7. **Compute New York State tax** (line 39). The method depends on New York AGI and taxable income:
   - New York AGI $107,650 or less, and taxable income under $65,000: use the tax table ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
   - New York AGI $107,650 or less, and taxable income $65,000 or more: use the rate schedule ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
   - New York AGI over $107,650: use the tax computation worksheet for the filing status. That is the recapture described below ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
8. **Subtract the New York State household credit** (line 40) and the other nonrefundable credits.
9. **New York City residents:** compute the city resident tax on New York City taxable income, which is the line 38 amount in most cases (lines 47 and 47a). Then subtract the city household credit and, where it applies, the UBT credit (Form IT-219).
10. **Add the MCTMT** (lines 54a to 54e) if an individual's net earnings from self-employment allocated to a zone exceed the threshold. **Yonkers residents:** add the resident surcharge (line 55).
11. **Apply refundable credits and payments:** the Empire State child credit, the New York State and New York City earned income credits, the New York City school tax credit, withholding, estimated payments and the IT-370 payment. Then work out the refund or the balance due, and check the estimated tax penalty (Form IT-2105.9).

### Rates, bands and thresholds

For 2026, the rates on the first five brackets are lower than in 2025. The brackets and the top four rates are unchanged.

| Taxable income over | But not over | Single / married filing separately (2026) | Tax at bracket start (single) | Source |
| --- | --- | --- | --- | --- |
| $0 | $8,500 | 3.90% | $0 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $8,500 | $11,700 | 4.40% | $332 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $11,700 | $13,900 | 5.15% | $473 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $13,900 | $80,650 | 5.40% | $586 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $80,650 | $215,400 | 5.90% | $4,191 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $215,400 | $1,077,550 | 6.85% | $12,141 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $1,077,550 | $5,000,000 | 9.65% | $71,198 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $5,000,000 | $25,000,000 | 10.3% | $449,714 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| $25,000,000 | and over | 10.9% | $2,509,714 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

| Bracket rate (2026) | Married filing jointly / qualifying surviving spouse: income over | Head of household: income over | Source |
| --- | --- | --- | --- |
| 3.90% | $0 | $0 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 4.40% | $17,150 | $12,800 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 5.15% | $23,600 | $17,650 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 5.40% | $27,900 | $20,900 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 5.90% | $161,550 | $107,650 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 6.85% | $323,200 | $269,300 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 9.65% | $2,155,350 | $1,616,450 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 10.3% | $5,000,000 | $5,000,000 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 10.9% | $25,000,000 | $25,000,000 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

- **Check before filing a 2026 return:** confirm these against the 2026 Form IT-201 instructions when published. Never apply them to a 2025 return.

#### Recapture: New York AGI over $107,650 ([IT-201-I (2025), tax computation worksheets](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

- If New York AGI is **more than** $107,650, you cannot use the table or the rate schedule alone. Use the tax computation worksheet that matches the filing status and taxable income. The worksheet takes back the benefit of the lower brackets. It is phased in over each $50,000 of New York AGI above the start point.
- **Single, lowest worksheet (worksheet 7), taxable income $215,400 or less:** the tax becomes a flat 5.90% of taxable income for 2026 (6% for 2025) once New York AGI is $157,650 or more. Between $107,650 and $157,650 it is phased in.
- **Married filing jointly, lowest worksheet (worksheet 1), taxable income $161,550 or less:** the flat rate is 5.40% for 2026 (5.5% for 2025), from the same $157,650 New York AGI.
- **New York AGI over $25,000,000:** the tax is 10.9% of all taxable income (worksheet 6 for joint filers).
- The worksheets' "recapture base" and "incremental benefit" amounts change with the rates. Never reuse 2025 amounts for 2026.

### Standard deduction, dependent exemption and household credit ([2025 standard deductions](https://www.tax.ny.gov/pit/file/standard_deductions.htm); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Filing status | Standard deduction, 2025 and 2026 |
| --- | --- |
| Single, can be claimed as a dependent | $3,100 |
| Single, cannot be claimed as a dependent | $8,000 |
| Married filing jointly | $16,050 |
| Married filing separately | $8,000 |
| Head of household (with qualifying person) | $11,200 |
| Qualifying surviving spouse | $16,050 [(standard deductions)](https://www.tax.ny.gov/pit/file/standard_deductions.htm) |

- **Dependent exemption:** $1,000 per dependent. There is no exemption for the taxpayer or the spouse ([IT-201-I (2025), line 36](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
  - Count the dependents listed at item H of Form IT-201 (and item H continued, for more than 7) and multiply by $1,000 ([IT-201-I (2025), line 36](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
  - If line 36 is more than line 35, leave taxable income (lines 37 and 38) blank. There is no negative taxable income ([IT-201-I (2025), lines 37 and 38](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **New York State household credit** (nonrefundable). It is not allowed to anyone who can be claimed as a dependent. It applies only if federal AGI is $28,000 or less for single filers, or $32,000 or less for the other statuses. For single filers it is at most $75 ([household credit](https://www.tax.ny.gov/pit/credits/household_credit.htm); [IT-201-I (2025), table 1](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

#### Itemized deductions ([IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf))

- The client can itemize for New York **whether or not** they itemized on the federal return.
- New York itemized deductions follow the Internal Revenue Code as it stood **before** the 2017 Tax Cuts and Jobs Act. There are adjustments on Form IT-196.
- **No federal SALT cap for New York.** The federal deduction for state and local taxes is limited to $40,000 ($20,000 married filing separately) for 2025. New York's deduction for taxes is not subject to that limit. But New York does **not** allow a deduction for state and local income taxes, or general sales tax (Form IT-196, line 41). In practice, real property taxes are deductible without the cap, and New York income tax is not deductible at all.
- **High-income limit.** If New York AGI is **more than** $100,000, the itemized deduction is reduced. The reduction uses worksheets for New York AGI up to $475,000 and from $475,000 to $525,000. Above $525,000 and up to $1,000,000, the reduction is 50% of the deduction. Above $1,000,000 and up to $10,000,000, the deduction is limited to 50% of total charitable gifts (Form IT-196, line 19); above $10,000,000, to 25%.

### Additions, subtractions and pensions ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-225-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf))

- **Pension and annuity exclusion (line 29):** up to $20,000 of qualifying pension and annuity income per person. The client must be 59½ before January 1 of the tax year. A client who turns 59½ during the year can exclude only the amounts received after that date, still up to $20,000. Qualifying income includes periodic and lump-sum IRA payments and private employer pensions. Each spouse has their own $20,000. A spouse cannot use the other's unused part.
- **Government pensions (line 26):** pensions from New York State or local government plans, or from federal government plans, are subtracted in full. They are not part of the $20,000 exclusion.
- **Social Security (line 27):** the taxable amount of Social Security benefits included in federal AGI is subtracted ([Form IT-201 (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201_fill_in.pdf)).
- **US government bond interest (line 28)** is subtracted. **Other states' municipal bond interest (line 20)** is added.
- **New York 529 contributions (line 30):** up to $5,000 can be subtracted ($10,000 for married filing jointly). Nonqualified withdrawals are added back on line 22.

| Code (Form IT-225) | What it is | When it applies |
| --- | --- | --- |
| A-101 | New York City flexible benefits program (IRC 125) | Add back amounts that a Form W-2 shows were deducted or deferred from salary under a flexible benefits program of New York City or certain other New York City public employers |
| A-201 | Personal income taxes and unincorporated business taxes deducted in computing federal AGI | Add back NYC UBT deducted on Schedule C |
| A-214 | MCTMT | Add back any MCTMT deducted on the federal return |
| A-209 / S-213 | Section 168(k) property depreciation. For 2025 on, also section 168(n) qualified production property | Add back the federal accelerated depreciation. Subtract depreciation calculated as if the special election had not been made. Compute on Form IT-398 |
| A-225 / S-221 | Section 174 / 174A R&E expenditures paid or incurred on or after January 1, 2025 | Add back the federal deduction. Subtract 60-month amortization |
| A-225 / S-222 | R&E expenditures paid or incurred before January 1, 2025 | Continue amortizing under the federal rules in effect on January 1, 2022 |
| A-219 | PTET deduction add-back | Only where an entity elected PTET: refer [(IT-225-I (2025))](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf) |

#### Federal changes in 2025 (P.L. 119-21) ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm))

- New York's 2026-2027 budget decoupled from the federal accelerated depreciation for qualified production property under IRC §168(n). It also decoupled from the federal treatment of R&E expenditures. Both apply to tax years beginning on or after January 1, 2025.
- **If a 2025 return has already been filed without these modifications, it must be amended.** Penalty and interest relief is available if the 2025 return is filed on time, or amended, to report them.
- A partner, shareholder or beneficiary reports the modification figures the entity provides (Form IT-225, Part 2). Do not recompute them yourself.
- Other federal changes reach New York only through federal AGI, because the return starts there. For any federal deduction taken after AGI, check tax.ny.gov for New York's position before assuming it carries over.

### New York City, Yonkers and MCTMT

#### New York City resident tax, 2025 and 2026 ([IT-201-I (2025), NYC rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Rate | Single / married filing separately: income over | Married filing jointly / qualifying surviving spouse: income over | Head of household: income over | Source |
| --- | --- | --- | --- | --- |
| 3.078% | $0 | $0 | $0 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 3.762% | $12,000 | $21,600 | $14,400 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 3.819% | $25,000 | $45,000 | $30,000 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| 3.876% | $50,000 | $90,000 | $60,000 | [IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

- The rates and brackets are the same in the 2025 instructions and the 2026 estimated tax instructions. For single filers, the tax at the start of each bracket is $369, $858 and $1,813 ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- Use the city tax table if city taxable income is less than $65,000. Otherwise use the rate schedule. There is no city recapture.
- **City household credit (line 48):** single filers get it only if federal AGI is $12,500 or less (at most $15). For joint, head of household and surviving spouse filers, the limit is $22,500 ([IT-201-I (2025), tables 4 to 6](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
  - Table 5 (joint, head of household and surviving spouse) gives an amount for each person counted: the taxpayer, the spouse on a joint return, and each dependent at item H. It is $30 a person with federal AGI of $15,000 or less, $25 over $15,000 to $17,500, $15 over $17,500 to $20,000, and $10 over $20,000 to $22,500 ([IT-201-I (2025), table 5](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
  - Nobody who can be claimed as a dependent (item C marked Yes) gets the city household credit ([IT-201-I (2025), line 48](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **UBT credit (Form IT-219):** 100% of the UBT imposed if city taxable income is $42,000 or less. It falls gradually to 23% when city taxable income is $142,000 or more. The credit cannot exceed the city tax ([IT-219-I](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
  - **The percentage between $42,000 and $142,000** (Form IT-219, Worksheet B): take city taxable income (Form IT-201, line 47), subtract $42,000, divide by $100,000 and round to three decimals. Multiply by 0.770 and subtract the result from 1.000 ([Form IT-219 (2025), Part 4 and Worksheet B](https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf)).
  - The UBT the percentage applies to comes from Form NYC-202, line 21, or Form NYC-202S, line 8. A joint return uses the couple's joint city taxable income ([IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
  - The credit is the lesser of that amount and the city tax less the city household credit (with the IT-201-ATT, lines 32 and 33 amounts). It goes to Form IT-201-ATT, line 8, then through Section C (line 10) to Form IT-201, line 53. Any unused credit is not refunded or carried over ([Form IT-219 (2025), lines 12 to 16](https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf); [IT-201-I (2025), line 53](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-219-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
- **School tax credit, fixed amount (line 69):** $63 for single, married filing separately and head of household, or $125 for joint and surviving spouse filers. It is available only if income is $250,000 or less and the client cannot be claimed as a dependent. The **rate reduction amount (line 69a)** is available only if income is $500,000 or less ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **City earned income credit (line 70):** a city resident who claimed, or could have claimed, the federal earned income credit completes Worksheet C of Form IT-215. It can apply even when the state credit does not ([IT-215-I](https://www.tax.ny.gov/pdf/current_forms/it/it215i.pdf)).

#### Yonkers ([IT-201-I (2025), line 55](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

- **Resident surcharge:** 16.75% of the net New York State tax, computed on the Yonkers worksheet. The worksheet starts from line 46, less certain credits such as the Empire State child credit. The rate is the same for 2026 ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- A Yonkers **nonresident** who earned wages or carried on business in Yonkers files Form Y-203, and the tax goes on line 56.
  - **Nonresident earnings tax:** 0.5% of Yonkers wages and net earnings from self-employment allocated to Yonkers, after an exclusion ([Form Y-203 (2025), line 6](https://www.tax.ny.gov/pdf/current_forms/it/y203_fill_in.pdf); [Y-203-I (2025), line 6](https://www.tax.ny.gov/pdf/current_forms/it/y203i.pdf)).
  - **Exclusion for a full year of nonresidence:** $3,000 if those wages and earnings are $10,000 or less, $2,000 if over $10,000 up to $20,000, and $1,000 if over $20,000 up to $30,000. Above $30,000 there is no exclusion. For part of a year, use the months of nonresidence in the Form Y-203 table ([Form Y-203 (2025), exclusion table](https://www.tax.ny.gov/pdf/current_forms/it/y203_fill_in.pdf)).
  - If both spouses owe it, each files a separate Form Y-203. On a joint New York return, add the two amounts on line 56 ([Y-203-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/y203i.pdf)).

#### MCTMT on self-employment earnings ([IT-201-I (2025), lines 54a to 54e](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Item | 2025 | 2026 |
| --- | --- | --- |
| Zone 1 (the five New York City counties) rate | 0.60% | 0.60% |
| Zone 2 (Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester) rate | 0.34% | 0.34% |
| Threshold: net earnings allocated to the zone must **exceed** | $50,000 | $150,000 [(IT-2105-I (2026))](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

- Once a zone's earnings exceed the threshold, the rate applies to **all** of that zone's earnings, not only to the excess. In the 2025 example in the instructions, $70,000 in Zone 2 gives a tax of $238.
- The threshold is tested **per person and per zone**, even on a joint return. If one spouse's base in a zone is at or below the threshold, leave that spouse's base out.
- No credit can reduce the MCTMT. Anyone who owes MCTMT must make estimated payments of it.
- **The base** is net earnings from self-employment: generally federal Schedule SE (Form 1040), Part 1, line 6, for that source of self-employment income. If the earnings are not subject to federal self-employment tax, compute them on Schedule SE as if they were ([IT-201-I (2025), lines 54a and 54b](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **Allocation to a zone** follows where the business activity is carried on. If all of it is inside Zone 1 (or Zone 2), all the earnings go to that zone. If it is carried on both inside and outside the zone, use Form IT-203-A to work out the amount for line 54a (or 54b) ([IT-201-I (2025), lines 54a and 54b](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

### Credits

- **Empire State child credit** (refundable, Form IT-213): full-year residents with a qualifying child **under 17** on December 31 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - **2025:** $1,000 per child under 4, plus $330 per child aged 4 to 16 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - **2026 and 2027:** $1,000 per child under 4, plus $500 per child aged 4 to 16 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - The credit is reduced by $16.50 for every $1,000 of federal AGI above $110,000 for married filing jointly, $75,000 for single, head of household or qualifying surviving spouse, or $55,000 for married filing separately ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - Every child and the claimant need a valid SSN or ITIN. For 2025, New York decoupled this credit from the federal child tax credit ([IT-213-I](https://www.tax.ny.gov/pdf/current_forms/it/it213i.pdf)).
- **New York State earned income credit** (Form IT-215) ([earned income credit](https://www.tax.ny.gov/pit/credits/earned_income_credit.htm)).
  - Generally 30% of the allowable federal earned income credit, reduced by the household credit. It is fully refundable for full-year residents ([earned income credit](https://www.tax.ny.gov/pit/credits/earned_income_credit.htm)).
  - The client must have claimed the federal credit and must not have claimed the noncustodial parent credit. Valid SSNs are needed by the due date, including extensions.
- **Real property tax credit (line 67):** check the Form IT-214 instructions. If the client qualifies, complete Form IT-214, carry the amount to line 67 and submit the form with the return ([IT-201-I (2025), line 67](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **College tuition credit (line 68):** if the client, the spouse or a dependent paid college tuition and the client did not take the college tuition itemized deduction on Form IT-196, complete Form IT-272 and carry the credit to line 68 ([IT-201-I (2025), line 68](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **Resident credit (Form IT-112-R):** a nonrefundable credit for income that another state sourced and taxed while the client was a New York resident ([residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)). Refer the computation.

## Boundary and exception table

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| Statutory resident | Permanent place of abode for substantially all of the year **and** 184 days or more. 183 days is not enough. Any part of a day counts, and the days need not be spent at the abode | [Residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm) |
| Domiciled but not resident | A New York domiciliary is not a resident if they meet all of Group A: no permanent place of abode in New York, a permanent place of abode outside New York all year, and 30 days or less in New York. Group B is the 548-day foreign-presence test | [Income tax definitions](https://www.tax.ny.gov/pit/file/pit_definitions.htm) |
| Changing domicile | Domicile does not change until there is clear and convincing evidence of leaving the old one and setting up a new one. A certificate or a voter registration is not enough | [Residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm) |
| Table, schedule or worksheet | Table only if New York AGI is $107,650 or less **and** taxable income is under $65,000. Worksheet if New York AGI is **more than** $107,650 | [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Pension exclusion age | 59½ before January 1 of the tax year for the full year. Otherwise only the amounts after reaching 59½. At most $20,000 per person, and the total with the disability income exclusion cannot exceed $20,000 | [IT-201-I (2025), line 29](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| MCTMT threshold | Tested **per person, per zone**. "Exceed" means an amount exactly at the threshold owes nothing. For 2026 the threshold is $150,000 | [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Joint return, one spouse nonresident | File separately, or file jointly as if both were residents | [IT-201-I (2025), Item A](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Joint federal return, separate New York return for other reasons | Allowed only if (a) the spouse's address or whereabouts is unknown, reasonable efforts were made to find them and there is good cause, or (b) the spouse refuses to sign, reasonable efforts were made to get the signature, there is objective evidence of alienation (an order of protection, a legal separation, or living apart for the 12 months before applying or before certain divorce or family court proceedings began) and there is good cause | [IT-201-I (2025), Item A](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Itemizing | Allowed even if the client took the federal standard deduction. The reduction starts only when New York AGI is **more than** $100,000 | [IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf) |
| Empire State child credit age | Under 17 on December 31. Full-year residents only | [Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm) |
| OBBBA decoupling | Applies to tax years beginning on or after January 1, 2025. A 2025 return filed without it must be amended | [Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm) |

### 2025 returns: tax year 2025, extended deadline October 15, 2026 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

Use the 2025 Form IT-201 and its instructions. The standard deductions, the New York City rates and the brackets are the same as for 2026. The differences are:

| Item (2025) | Amount | Source |
| --- | --- | --- |
| State rates, lowest five brackets | 4%, 4.5%, 5.25%, 5.5%, 6% | [IT-201-I (2025), rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| State rates, top four brackets | 6.85%, 9.65%, 10.3%, 10.9% | [IT-201-I (2025), rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Single: tax at the start of the $80,650 bracket | $4,271 | [IT-201-I (2025), rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Married filing jointly: tax at the start of the $161,550 bracket | $8,553 | [IT-201-I (2025), rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| MCTMT threshold per person per zone | $50,000 | [IT-201-I (2025), rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Empire State child credit, child aged 4 to 16 | $330 | [Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm) |

- The 2025 rate for the first bracket is 4% of taxable income up to $8,500 for single filers ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- Add the Notice N-26-1 modifications (A-209/S-213 and A-225/S-221/S-222) where they apply. If the 2025 return is already filed without them, amend it ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm)).
- An extension to October 15, 2026 only helps if Form IT-370 was filed by April 15, 2026 with full payment of the properly estimated tax. Interest runs from April 15, 2026 on any unpaid tax ([IT-370-I](https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf)).

## Worked cases

The amounts in these cases are made up for illustration. The rates and thresholds come from the sources linked in each heading. Tax amounts use the rate schedule and are rounded to the whole dollar.

### Case 1: 2026 single New York City resident, rate schedule ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

- New York AGI $95,000. That is not over $107,650, so there is no recapture. Standard deduction $8,000. Taxable income: $95,000 - $8,000 = $87,000. That is $65,000 or more, so use the rate schedule.
- State tax: $4,191 + 5.90% × ($87,000 - $80,650 = $6,350) = $4,191 + $374.65 = $4,565.65, rounded to $4,566.
- City tax: $1,813 + 3.876% × ($87,000 - $50,000 = $37,000) = $1,813 + $1,434.12 = $3,247.12, rounded to $3,247.
- For comparison, the same income in 2025 gives a state tax of $4,652: the excess is taxed at 6% × $6,350 = $381, and $4,271 + $381 = $4,652 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

```oa-check
name: Case 1, 2026 single New York City resident, rate schedule (IT-2105-I 2026)
inputs:
  ny_agi: 95000
  standard_deduction: 8000
  state_base_tax: 4191
  state_bracket_start: 80650
  state_rate: 0.059
  city_base_tax: 1813
  city_bracket_start: 50000
  city_rate: 0.03876
steps:
  - taxable_income: ny_agi - standard_deduction
  - state_tax: state_base_tax + state_rate * (taxable_income - state_bracket_start)
  - city_tax: city_base_tax + city_rate * (taxable_income - city_bracket_start)
expected:
  taxable_income: 87000
  state_tax: 4565.65
  city_tax: 3247.12
```

### Case 2: 2025 single filer, recapture ([IT-201-I (2025), worksheet 7](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

- New York AGI $200,000, taxable income $192,000. New York AGI is over $107,650 and taxable income is $215,400 or less, so use worksheet 7. New York AGI is $157,650 or more, so the tax is a flat 6% of taxable income: $192,000 × 6% = $11,520.
- The rate schedule alone would give $4,271 + 6% × ($192,000 - $80,650 = $111,350) = $4,271 + $6,681 = $10,952. So the recapture adds $568.
- For 2026, the same facts give $192,000 × 5.90% = $11,328 ([IT-2105-I (2026), worksheet 7](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).

### Case 3: MCTMT, 2025 and 2026 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

- A Brooklyn sole proprietor has $120,000 of net earnings from self-employment, all allocated to Zone 1.
- 2025: $120,000 exceeds $50,000, so the MCTMT is $120,000 × 0.60% = $720, on the whole amount. If the $720 was deducted on the federal return, add it back with code A-214.
- 2026: $120,000 does not exceed $150,000, so there is no MCTMT for 2026 on the same earnings.

### Case 4: 2025 retiree, government pension and IRA ([IT-201-I (2025), lines 26 and 29](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

- A single filer, aged 67 all year, received a New York State retirement system pension of $25,000 and IRA distributions of $30,000. Both are in federal AGI.
- Line 26: subtract the whole $25,000 government pension.
- Line 29: the IRA distributions qualify. The exclusion is $20,000, and the rest, $30,000 - $20,000 = $10,000, stays taxable.

### Case 5: 2026 Empire State child credit with phase-down ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm))

- Married filing jointly, full-year residents. Children aged 2 and 9 on December 31, 2026. Federal AGI $130,000.
- Before the phase-down: $1,000 + $500 = $1,500. Federal AGI is over $110,000 by $20,000, which is 20 steps of $1,000. The reduction is 20 × $16.50 = $330. Credit: $1,500 - $330 = $1,170, refundable.

### Case 6: 2025 itemizer with a large property tax bill ([IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf))

- Single filer, New York AGI $90,000. Real property tax $14,000, New York income tax withheld $6,000, and cash gifts to charity $3,000. There are no other deductions.
- For New York, the income tax is not deductible, and the property tax is not limited by the federal cap. New York itemized deduction: $14,000 + $3,000 = $17,000. That is more than the $8,000 standard deduction, so the client itemizes. New York AGI is not over $100,000, so there is no reduction.

### Case 7: statutory residency ([residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm))

- The client is domiciled in Connecticut. They rent a Manhattan apartment all year that is suitable for year-round use, and spend 190 days (counting part days) in New York City.
- They are a statutory resident of both New York State and New York City. They file Form IT-201, and are taxed by the state and the city on all their income. They claim the Form IT-112-R resident credit for income taxed by another state.
- On 183 days they would not be a statutory resident. They would be a nonresident, taxed by New York State only on New York source income (Form IT-203), and not liable for New York City personal income tax.

### Case 8: 2025 New York City UBT credit in the phase-down range ([Form IT-219 (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf); [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

- A single New York City resident freelancer has city taxable income (Form IT-201, line 47) of $95,000. Form NYC-202, line 21 shows UBT of $2,500.
- $95,000 is more than $42,000 and less than $142,000, so use Worksheet B. ($95,000 - $42,000) / $100,000 = 0.530. 0.530 × 0.770 = 0.4081. The credit percentage is 1.000 - 0.4081 = 0.5919.
- Credit before the limit: $2,500 × 0.5919 = $1,479.75.
- The limit is the city tax less the city household credit. The 2025 city tax on $95,000 is $1,813 + 3.876% × ($95,000 - $50,000) = $3,557.20, and there is no household credit at this income. The credit of $1,479.75 is below the limit, so it is allowed in full. It goes to Form IT-201-ATT, line 8, and then to Form IT-201, line 53.
- At city taxable income of $142,000 or more the same UBT would give 23%: $2,500 × 0.23 = $575.

```oa-check
name: Case 8, 2025 NYC UBT credit (Form IT-219 Worksheet B)
inputs:
  city_taxable_income: 95000
  ubt: 2500
  city_base_tax: 1813
  city_bracket_start: 50000
  city_rate: 0.03876
steps:
  - ratio: round((city_taxable_income - 42000) / 100000, 3)
  - percentage: 1 - ratio * 0.77
  - credit_before_limit: ubt * percentage
  - city_tax: city_base_tax + city_rate * (city_taxable_income - city_bracket_start)
  - credit: min(credit_before_limit, city_tax)
expected:
  ratio: 0.53
  percentage: 0.5919
  credit_before_limit: 1479.75
  city_tax: 3557.20
  credit: 1479.75
```

## When to refuse or refer

- **Refer** a move into or out of New York State, New York City or Yonkers during the year. That is a part-year return on Form IT-203 (with Form IT-360.1 for the city), and income is split by period.
- **Refer** doubtful domicile or statutory residency, where days are close to 184 or the abode's status is unclear. These are audit-prone; see the Nonresident Audit Guidelines on tax.ny.gov.
- **Refer** the resident credit for taxes paid to another state (Form IT-112-R) where the amounts are material, and any convenience-of-the-employer question for a nonresident employee.
- **Refer** PTET elections and credits (Form IT-653, code A-219), the NYC UBT return itself, and qualified production property or R&E modifications that come from an entity. Use the entity's figures.
- **Refer** the itemized deduction reduction when New York AGI is over $100,000 and the amounts are material. Run the IT-196 worksheets and have them reviewed ([IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf)).
- **Refuse to guess** a 2026 figure that the 2026 instructions have not yet confirmed, or any federal change after AGI whose New York treatment is not stated on tax.ny.gov. Say it is unconfirmed and point to the Tax Department page to check.
- **Refer** fiduciary, deceased-taxpayer, amended (IT-201-X) and military special-condition cases.

## Filing and payment

- **Due date:** the 2025 return and payment were due April 15, 2026. Filing Form IT-370 by that date, with full payment of the properly estimated tax, extends the filing date to October 15, 2026. It does **not** extend the time to pay. A federal extension form is not accepted in place of Form IT-370 ([IT-370-I](https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf); [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **2026 returns** will be due in April 2027. Confirm the date in the 2026 instructions.
- **Late filing penalty:** 5% of the tax due for each month or part of a month, up to 25%. If the return is more than 60 days late, the minimum is the lesser of $100 or 100% of the unpaid tax ([IT-370-I](https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf)).
- **Late payment penalty:** ½ of 1% of the unpaid amount for each month or part of a month, up to 25%. Neither penalty applies if the client shows reasonable cause. Reasonable cause for late payment is presumed if the extension rules were met, the balance is no more than 10% of the total tax, and it is paid with the return. Interest is compounded daily and cannot generally be waived. A returned payment costs $50 ([IT-370-I](https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf)).
- **Estimated tax for 2026** ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)):
  - Pay if the client expects to owe at least $300 of New York State, New York City or Yonkers tax after withholding and credits, or any MCTMT ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
  - The instalments are due April 15, June 15, September 15, 2026 and January 15, 2027. The January instalment is not needed if the 2026 return is filed and paid in full by January 31, 2027.
  - To avoid the underpayment penalty (Form IT-2105.9), pay 90% of the 2026 tax, or 100% of the 2025 tax. Use 110% of the 2025 tax if New York AGI (or MCTD self-employment earnings) on the 2025 return was more than $150,000, or $75,000 if married filing separately. The prior-year rule needs a full 12-month 2025 return ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- **Refund claims:** generally within three years of filing or two years of paying, whichever is later ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **How to pay a balance due** ([IT-201-I (2025), payment options](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)):
  - Electronic funds withdrawal from a US bank account, authorized on the return: mark the box at line 80, give the account on line 83 and the withdrawal date on line 84, on or before the due date.
  - Check or money order payable to New York State Income Tax, with the last four digits of the Social Security number and the tax year written on it, sent with Form IT-201-V.
  - Online through an Individual Online Services account: bank withdrawal, or debit or credit card (the card vendor charges a fee).
- **Sales or use tax (line 59):** report sales or use tax owed on untaxed purchases, such as items bought online or out of state and brought into New York. Use Form ST-141 for any item or service costing $1,000 or more, and for purchases of a business not registered for sales tax, rental real estate or royalty activities; the instructions' chart covers smaller personal purchases. If line 59 is $1,700 or more, also submit Form IT-135. If nothing is owed, enter 0; do not leave line 59 blank ([IT-201-I (2025), line 59](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **Records:** keep copies of the return for at least seven years after filing, with the books, schedules and statements behind it ([IT-201-I (2025), keep a copy of your tax records](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

## Completion checklist

- Full-year residence is confirmed for the state, and separately for New York City and Yonkers, with day counts on file.
- Lines 1 to 19 tie to the finished federal return.
- Every New York addition and subtraction is supported. IT-225 codes are used correctly: A-201, A-214, A-209/S-213, A-225/S-221/S-222.
- The pension exclusion is limited to $20,000 per person, and government pensions are on line 26 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- The standard and itemized deductions are compared. State and local income taxes are removed from itemized deductions, and the over-$100,000 reduction is applied ([IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf)).
- The table, rate schedule or worksheet is chosen correctly, with the 2026 rates for 2026 and the 2025 rates for 2025.
- City tax, the household credits, the UBT credit, the school tax credits and the city earned income credit are checked for city residents.
- The MCTMT is tested per person and per zone against $50,000 (2025) or $150,000 (2026). The 16.75% surcharge is applied for Yonkers residents ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- The Empire State child credit is computed for the right year's amounts and phase-down. The state earned income credit is checked.
- The Notice N-26-1 modifications are reported, or a 2025 amendment is flagged.
- Payments, the IT-370 payment and estimated tax are reconciled. Penalty exposure is noted, and next year's estimated payments are set up.

## Sources

| Source | URL | Read on |
|---|---|---|
| IT-201-I (2025), read for Item A, Item C, school district, lines 36 to 38, 48 and table 5, 53, 54a and 54b, 56, 59, 67, 68, payment options and record keeping | https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf | 2026-11-06 |
| Form IT-201 (2025), read for lines 27, 83 and 84 | https://www.tax.ny.gov/pdf/current_forms/it/it201_fill_in.pdf | 2026-11-06 |
| IT-2105-I (2026), read for the 2026 rate schedules (page 10), worksheet 7 (5.90%, $157,650), the $150,000 MCTMT threshold and the estimated tax rules | https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf | 2026-11-13 |
| NYS-50-T-NYS (1/26), read for the Chapter 59 of the Laws of 2025, Part A, rate cut | https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf | 2026-11-06 |
| Form IT-219 (2025), read for Part 4, lines 8 to 16, and Worksheet B | https://www.tax.ny.gov/pdf/current_forms/it/it219_fill_in.pdf | 2026-11-06 |
| IT-219-I (2025), read for the credit percentage, married taxpayers and Part 4 | https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf | 2026-11-06 |
| Form Y-203 (2025), read for line 6 and the exclusion table | https://www.tax.ny.gov/pdf/current_forms/it/y203_fill_in.pdf | 2026-11-06 |
| Y-203-I (2025), read for who must file and lines 4 and 6 | https://www.tax.ny.gov/pdf/current_forms/it/y203i.pdf | 2026-11-06 |
| IT-225-I (2025), read for codes A-101, A-201, A-209, A-214, A-219 and S-213 | https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf | 2026-11-06 |
| Notice N-26-1, read for codes A-209, S-213, A-225, S-221 and S-222 and the amendment rule | https://www.tax.ny.gov/forms/n-notices/n-26-1.htm | 2026-11-06 |
| IT-196-I (2025), read for the itemized deduction reduction bands | https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf | 2026-11-06 |
| Residency FAQ, read for the 184-day test and Yonkers residence | https://www.tax.ny.gov/pit/file/nonresident-faqs.htm | 2026-11-06 |
| Income tax definitions, read for resident and the 548-day test | https://www.tax.ny.gov/pit/file/pit_definitions.htm | 2026-11-06 |
| Standard deductions, read for the amounts by filing status | https://www.tax.ny.gov/pit/file/standard_deductions.htm | 2026-11-06 |
| Household credit, read for the federal AGI limits | https://www.tax.ny.gov/pit/credits/household_credit.htm | 2026-11-06 |
| Empire State child credit, read for the 2025 and 2026 amounts and the phase-down | https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm | 2026-11-06 |
| IT-213-I (2025), read for the 2025 decoupling note | https://www.tax.ny.gov/pdf/current_forms/it/it213i.pdf | 2026-11-06 |
| Earned income credit, read for the 30% rule | https://www.tax.ny.gov/pit/credits/earned_income_credit.htm | 2026-11-06 |
| IT-215-I (2025), read for Worksheet C | https://www.tax.ny.gov/pdf/current_forms/it/it215i.pdf | 2026-11-06 |
| IT-370-I (2025), read for the extension and the penalties | https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf | 2026-11-06 |

Not yet confirmed: the 2026 Form IT-201, IT-219 and Y-203 and their instructions are not published, so the IT-219 Worksheet B figures, the Yonkers 0.5% rate and exclusion table, the city household credit table 5 amounts, the school district, payment and line 59 rules are taken from the 2025 forms. Confirm them against the 2026 forms for a 2026 return. The 2026 return due date in April 2027 is also unconfirmed until those instructions are out.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ny-it-201-resident-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ny-it-201-resident-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
