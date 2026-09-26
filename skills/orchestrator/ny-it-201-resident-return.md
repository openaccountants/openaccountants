---
name: ny-it-201-resident-return
description: Tier 2 New York content skill for preparing Form IT-201 (Full-Year Resident Income Tax Return) for New York State full-year residents who are sole proprietors or single-member LLCs disregarded for federal tax purposes. Covers the NYAGI computation starting from federal AGI, Form IT-225 addition and subtraction modifications (notably A-201 for unincorporated business taxes deducted federally), Form IT-558 OBBBA decoupling adjustments including the §168(k) bonus depreciation add-back and the §174A R&E expensing uncertainty, the standard vs itemized deduction decision, NY state tax computation including the $107,650 recapture worksheet, NYC resident tax computation (lines 47a-53) including the NYC UBT credit flow via Form IT-219, Yonkers resident surcharge and nonresident earnings tax (lines 55-57), MCTMT for self-employed individuals in the MCTD (lines 54a-54b), credits and payments, and the reviewer brief for the complete NY state-level return package. Does NOT cover part-year or nonresident returns (Form IT-203), itemized deduction limitations above $100,000 NYAGI in detail, PTET election scenarios, convenience-of-the-employer rule cases, NY source income allocation for multi-state activity, or NYC Unincorporated Business Tax computation itself — see Section 7. MUST be loaded alongside us-tax-workflow-base v0.2 or later. Typically loaded alongside ny-llc-filing-fee-it-204-ll (if SMLLC), nyc-unincorporated-business-tax (if NYC resident), and ny-estimated-tax-it-2105. New York State full-year residents only.
jurisdiction: US-NY
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New York State resident return (Form IT-201): 2026 method, with 2025 return notes

Figures are for tax year 2026 unless a line says 2025. The 2026 New York State rates come from the 2026 estimated tax instructions ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)), because the 2026 Form IT-201 instructions are not published yet. Chapter 59 of the Laws of 2025 (Part A) cut the rates for the lower brackets from 2026 ([NYS-50-T-NYS (1/26)](https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf)). 2025 returns use the 2025 Form IT-201 instructions ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)). A separate section covers them. Returns on extension are due October 15, 2026.

## Scope and who this is for

- **Covers:** individuals who were New York State residents for the whole year and file Form IT-201. That includes the New York City resident tax, the Yonkers resident surcharge, the metropolitan commuter transportation mobility tax (MCTMT) on self-employment earnings, and the main New York additions, subtractions, deductions and credits.
- **Residents are taxed on all income, wherever it is earned.** New York City residents also pay city tax on all their income ([Tax Department residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)).
- **Does not cover:** part-year residents and nonresidents. They file Form IT-203; see the IT-203 instructions. It also does not cover fiduciary returns, amended returns, the NYC unincorporated business tax (UBT) return itself, the pass-through entity tax (PTET) election, or the detail of the resident credit for tax paid to another state (Form IT-112-R).
- **Federal first.** Form IT-201 starts from federal adjusted gross income (AGI), so the federal return must be finished first ([IT-201-I (2025), lines 1 through 19](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

## Ask the client first

- Which tax year (2025 or 2026)? What was the federal filing status? New York generally requires the same status. The exception is a married couple where only one spouse is a New York resident.
- Where was the client domiciled all year? Did they keep a permanent place of abode in New York State, in New York City or in Yonkers, and how many days (any part of a day counts) did they spend there? Keep the day-count records.
- Did the client move into or out of New York, New York City or Yonkers during the year? If so, this is a part-year case (see "When to refuse or refer").
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

## New York State tax rates for 2026 ([IT-2105-I (2026), page 10](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

For 2026, the rates on the first five brackets are lower than in 2025. The brackets and the top four rates are unchanged.

| Taxable income over | But not over | Single / married filing separately (2026) | Tax at bracket start (single) |
| --- | --- | --- | --- |
| $0 | $8,500 | 3.90% | $0 |
| $8,500 | $11,700 | 4.40% | $332 |
| $11,700 | $13,900 | 5.15% | $473 |
| $13,900 | $80,650 | 5.40% | $586 |
| $80,650 | $215,400 | 5.90% | $4,191 |
| $215,400 | $1,077,550 | 6.85% | $12,141 |
| $1,077,550 | $5,000,000 | 9.65% | $71,198 |
| $5,000,000 | $25,000,000 | 10.3% | $449,714 |
| $25,000,000 | and over | 10.9% | $2,509,714 |

| Bracket rate (2026) | Married filing jointly / qualifying surviving spouse: income over | Head of household: income over |
| --- | --- | --- |
| 3.90% | $0 | $0 |
| 4.40% | $17,150 | $12,800 |
| 5.15% | $23,600 | $17,650 |
| 5.40% | $27,900 | $20,900 |
| 5.90% | $161,550 | $107,650 |
| 6.85% | $323,200 | $269,300 |
| 9.65% | $2,155,350 | $1,616,450 |
| 10.3% | $5,000,000 | $5,000,000 |
| 10.9% | $25,000,000 | $25,000,000 [(IT-2105-I (2026))](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

- **Check before filing a 2026 return:** confirm these against the 2026 Form IT-201 instructions when published. Never apply them to a 2025 return.

### Recapture: New York AGI over $107,650 ([IT-201-I (2025), tax computation worksheets](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

- If New York AGI is **more than** $107,650, you cannot use the table or the rate schedule alone. Use the tax computation worksheet that matches the filing status and taxable income. The worksheet takes back the benefit of the lower brackets. It is phased in over each $50,000 of New York AGI above the start point.
- **Single, lowest worksheet (worksheet 7), taxable income $215,400 or less:** the tax becomes a flat 5.90% of taxable income for 2026 (6% for 2025) once New York AGI is $157,650 or more. Between $107,650 and $157,650 it is phased in.
- **Married filing jointly, lowest worksheet (worksheet 1), taxable income $161,550 or less:** the flat rate is 5.40% for 2026 (5.5% for 2025), from the same $157,650 New York AGI.
- **New York AGI over $25,000,000:** the tax is 10.9% of all taxable income (worksheet 6 for joint filers).
- The worksheets' "recapture base" and "incremental benefit" amounts change with the rates. Never reuse 2025 amounts for 2026.

## Standard deduction, dependent exemption and household credit ([2025 standard deductions](https://www.tax.ny.gov/pit/file/standard_deductions.htm); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Filing status | Standard deduction, 2025 and 2026 |
| --- | --- |
| Single, can be claimed as a dependent | $3,100 |
| Single, cannot be claimed as a dependent | $8,000 |
| Married filing jointly | $16,050 |
| Married filing separately | $8,000 |
| Head of household (with qualifying person) | $11,200 |
| Qualifying surviving spouse | $16,050 [(standard deductions)](https://www.tax.ny.gov/pit/file/standard_deductions.htm) |

- **Dependent exemption:** $1,000 per dependent. There is no exemption for the taxpayer or the spouse ([IT-201-I (2025), line 36](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **New York State household credit** (nonrefundable). It is not allowed to anyone who can be claimed as a dependent. It applies only if federal AGI is $28,000 or less for single filers, or $32,000 or less for the other statuses. For single filers it is at most $75 ([household credit](https://www.tax.ny.gov/pit/credits/household_credit.htm); [IT-201-I (2025), table 1](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

### Itemized deductions ([IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf))

- The client can itemize for New York **whether or not** they itemized on the federal return.
- New York itemized deductions follow the Internal Revenue Code as it stood **before** the 2017 Tax Cuts and Jobs Act. There are adjustments on Form IT-196.
- **No federal SALT cap for New York.** The federal deduction for state and local taxes is limited to $40,000 ($20,000 married filing separately) for 2025. New York's deduction for taxes is not subject to that limit. But New York does **not** allow a deduction for state and local income taxes, or general sales tax (Form IT-196, line 41). In practice, real property taxes are deductible without the cap, and New York income tax is not deductible at all.
- **High-income limit.** If New York AGI is **more than** $100,000, the itemized deduction is reduced. The reduction uses worksheets for New York AGI up to $475,000 and from $475,000 to $525,000. Above $525,000 and up to $1,000,000, the reduction is 50% of the deduction. Above $1,000,000 and up to $10,000,000, the deduction is limited to 50% of total charitable gifts (Form IT-196, line 19); above $10,000,000, to 25%.

## Additions, subtractions and pensions ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-225-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf))

- **Pension and annuity exclusion (line 29):** up to $20,000 of qualifying pension and annuity income per person. The client must be 59½ before January 1 of the tax year. A client who turns 59½ during the year can exclude only the amounts received after that date, still up to $20,000. Qualifying income includes periodic and lump-sum IRA payments and private employer pensions. Each spouse has their own $20,000. A spouse cannot use the other's unused part.
- **Government pensions (line 26):** pensions from New York State or local government plans, or from federal government plans, are subtracted in full. They are not part of the $20,000 exclusion.
- **Social Security (line 27):** the taxable amount of Social Security benefits included in federal AGI is subtracted ([Form IT-201 (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201_fill_in.pdf)).
- **US government bond interest (line 28)** is subtracted. **Other states' municipal bond interest (line 20)** is added.
- **New York 529 contributions (line 30):** up to $5,000 can be subtracted ($10,000 for married filing jointly). Nonqualified withdrawals are added back on line 22.

| Code (Form IT-225) | What it is | When it applies |
| --- | --- | --- |
| A-201 | Personal income taxes and unincorporated business taxes deducted in computing federal AGI | Add back NYC UBT deducted on Schedule C |
| A-214 | MCTMT | Add back any MCTMT deducted on the federal return |
| A-209 / S-213 | Section 168(k) property depreciation. For 2025 on, also section 168(n) qualified production property | Add back the federal accelerated depreciation. Subtract depreciation calculated as if the special election had not been made. Compute on Form IT-398 |
| A-225 / S-221 | Section 174 / 174A R&E expenditures paid or incurred on or after January 1, 2025 | Add back the federal deduction. Subtract 60-month amortization |
| A-225 / S-222 | R&E expenditures paid or incurred before January 1, 2025 | Continue amortizing under the federal rules in effect on January 1, 2022 |
| A-219 | PTET deduction add-back | Only where an entity elected PTET: refer [(IT-225-I (2025))](https://www.tax.ny.gov/pdf/current_forms/it/it225i.pdf) |

### Federal changes in 2025 (P.L. 119-21) ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm))

- New York's 2026-2027 budget decoupled from the federal accelerated depreciation for qualified production property under IRC §168(n). It also decoupled from the federal treatment of R&E expenditures. Both apply to tax years beginning on or after January 1, 2025.
- **If a 2025 return has already been filed without these modifications, it must be amended.** Penalty and interest relief is available if the 2025 return is filed on time, or amended, to report them.
- A partner, shareholder or beneficiary reports the modification figures the entity provides (Form IT-225, Part 2). Do not recompute them yourself.
- Other federal changes reach New York only through federal AGI, because the return starts there. For any federal deduction taken after AGI, check tax.ny.gov for New York's position before assuming it carries over.

## New York City, Yonkers and MCTMT

### New York City resident tax, 2025 and 2026 ([IT-201-I (2025), NYC rate schedule](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Rate | Single / married filing separately: income over | Married filing jointly / qualifying surviving spouse: income over | Head of household: income over |
| --- | --- | --- | --- |
| 3.078% | $0 | $0 | $0 |
| 3.762% | $12,000 | $21,600 | $14,400 |
| 3.819% | $25,000 | $45,000 | $30,000 |
| 3.876% | $50,000 | $90,000 | $60,000 |

- The rates and brackets are the same in the 2025 instructions and the 2026 estimated tax instructions. For single filers, the tax at the start of each bracket is $369, $858 and $1,813 ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- Use the city tax table if city taxable income is less than $65,000. Otherwise use the rate schedule. There is no city recapture.
- **City household credit (line 48):** single filers get it only if federal AGI is $12,500 or less (at most $15). For joint, head of household and surviving spouse filers, the limit is $22,500 ([IT-201-I (2025), tables 4 to 6](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **UBT credit (Form IT-219):** 100% of the UBT imposed if city taxable income is $42,000 or less. It falls gradually to 23% when city taxable income is $142,000 or more. The credit cannot exceed the city tax ([IT-219-I](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf)).
- **School tax credit, fixed amount (line 69):** $63 for single, married filing separately and head of household, or $125 for joint and surviving spouse filers. It is available only if income is $250,000 or less and the client cannot be claimed as a dependent. The **rate reduction amount (line 69a)** is available only if income is $500,000 or less ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- **City earned income credit (line 70):** a city resident who claimed, or could have claimed, the federal earned income credit completes Worksheet C of Form IT-215. It can apply even when the state credit does not ([IT-215-I](https://www.tax.ny.gov/pdf/current_forms/it/it215i.pdf)).

### Yonkers ([IT-201-I (2025), line 55](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

- **Resident surcharge:** 16.75% of the net New York State tax, computed on the Yonkers worksheet. The worksheet starts from line 46, less certain credits such as the Empire State child credit. The rate is the same for 2026 ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf)).
- A Yonkers **nonresident** who earned wages or carried on business in Yonkers files Form Y-203, and the tax goes on line 56.

### MCTMT on self-employment earnings ([IT-201-I (2025), lines 54a to 54e](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

| Item | 2025 | 2026 |
| --- | --- | --- |
| Zone 1 (the five New York City counties) rate | 0.60% | 0.60% |
| Zone 2 (Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, Westchester) rate | 0.34% | 0.34% |
| Threshold: net earnings allocated to the zone must **exceed** | $50,000 | $150,000 [(IT-2105-I (2026))](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |

- Once a zone's earnings exceed the threshold, the rate applies to **all** of that zone's earnings, not only to the excess. In the 2025 example in the instructions, $70,000 in Zone 2 gives a tax of $238.
- The threshold is tested **per person and per zone**, even on a joint return. If one spouse's base in a zone is at or below the threshold, leave that spouse's base out.
- No credit can reduce the MCTMT. Anyone who owes MCTMT must make estimated payments of it.

## Credits

- **Empire State child credit** (refundable, Form IT-213): full-year residents with a qualifying child **under 17** on December 31 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - **2025:** $1,000 per child under 4, plus $330 per child aged 4 to 16 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - **2026 and 2027:** $1,000 per child under 4, plus $500 per child aged 4 to 16 ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - The credit is reduced by $16.50 for every $1,000 of federal AGI above $110,000 for married filing jointly, $75,000 for single, head of household or qualifying surviving spouse, or $55,000 for married filing separately ([Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm)).
  - Every child and the claimant need a valid SSN or ITIN. For 2025, New York decoupled this credit from the federal child tax credit ([IT-213-I](https://www.tax.ny.gov/pdf/current_forms/it/it213i.pdf)).
- **New York State earned income credit** (Form IT-215) ([earned income credit](https://www.tax.ny.gov/pit/credits/earned_income_credit.htm)).
  - Generally 30% of the allowable federal earned income credit, reduced by the household credit. It is fully refundable for full-year residents ([earned income credit](https://www.tax.ny.gov/pit/credits/earned_income_credit.htm)).
  - The client must have claimed the federal credit and must not have claimed the noncustodial parent credit. Valid SSNs are needed by the due date, including extensions.
- **Resident credit (Form IT-112-R):** a nonrefundable credit for income that another state sourced and taxed while the client was a New York resident ([residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm)). Refer the computation.

## Boundaries and exceptions

| Rule | Condition that decides it | Source |
| --- | --- | --- |
| Statutory resident | Permanent place of abode for substantially all of the year **and** 184 days or more. 183 days is not enough. Any part of a day counts, and the days need not be spent at the abode | [Residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm) |
| Domiciled but not resident | A New York domiciliary is not a resident if they meet all of Group A: no permanent place of abode in New York, a permanent place of abode outside New York all year, and 30 days or less in New York. Group B is the 548-day foreign-presence test | [Income tax definitions](https://www.tax.ny.gov/pit/file/pit_definitions.htm) |
| Changing domicile | Domicile does not change until there is clear and convincing evidence of leaving the old one and setting up a new one. A certificate or a voter registration is not enough | [Residency FAQ](https://www.tax.ny.gov/pit/file/nonresident-faqs.htm) |
| Table, schedule or worksheet | Table only if New York AGI is $107,650 or less **and** taxable income is under $65,000. Worksheet if New York AGI is **more than** $107,650 | [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Pension exclusion age | 59½ before January 1 of the tax year for the full year. Otherwise only the amounts after reaching 59½. At most $20,000 per person, and the total with the disability income exclusion cannot exceed $20,000 | [IT-201-I (2025), line 29](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| MCTMT threshold | Tested **per person, per zone**. "Exceed" means an amount exactly at the threshold owes nothing. For 2026 the threshold is $150,000 | [IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf); [IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf) |
| Joint return, one spouse nonresident | File separately, or file jointly as if both were residents | [IT-201-I (2025), Item A](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |
| Itemizing | Allowed even if the client took the federal standard deduction. The reduction starts only when New York AGI is **more than** $100,000 | [IT-196-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it196i.pdf) |
| Empire State child credit age | Under 17 on December 31. Full-year residents only | [Empire State child credit](https://www.tax.ny.gov/pit/credits/empire_state_child_credit.htm) |
| OBBBA decoupling | Applies to tax years beginning on or after January 1, 2025. A 2025 return filed without it must be amended | [Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm) |

## Worked cases

The amounts in these cases are made up for illustration. The rates and thresholds come from the sources linked in each heading. Tax amounts use the rate schedule and are rounded to the whole dollar.

### Case 1: 2026 single New York City resident, rate schedule ([IT-2105-I (2026)](https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf))

- New York AGI $95,000. That is not over $107,650, so there is no recapture. Standard deduction $8,000. Taxable income: $95,000 - $8,000 = $87,000. That is $65,000 or more, so use the rate schedule.
- State tax: $4,191 + 5.90% × ($87,000 - $80,650 = $6,350) = $4,191 + $374.65 = $4,565.65, rounded to $4,566.
- City tax: $1,813 + 3.876% × ($87,000 - $50,000 = $37,000) = $1,813 + $1,434.12 = $3,247.12, rounded to $3,247.
- For comparison, the same income in 2025 gives a state tax of $4,652: the excess is taxed at 6% × $6,350 = $381, and $4,271 + $381 = $4,652 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).

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

## 2025 returns: tax year 2025, extended deadline October 15, 2026 ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf))

Use the 2025 Form IT-201 and its instructions. The standard deductions, the New York City rates and the brackets are the same as for 2026. The differences are:

| Item (2025) | Amount |
| --- | --- |
| State rates, lowest five brackets | 4%, 4.5%, 5.25%, 5.5%, 6% |
| State rates, top four brackets | 6.85%, 9.65%, 10.3%, 10.9% |
| Single: tax at the start of the $80,650 bracket | $4,271 |
| Married filing jointly: tax at the start of the $161,550 bracket | $8,553 |
| MCTMT threshold per person per zone | $50,000 |
| Empire State child credit, child aged 4 to 16 | $330 [(IT-201-I (2025), rate schedule)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf) |

- The 2025 rate for the first bracket is 4% of taxable income up to $8,500 for single filers ([IT-201-I (2025)](https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf)).
- Add the Notice N-26-1 modifications (A-209/S-213 and A-225/S-221/S-222) where they apply. If the 2025 return is already filed without them, amend it ([Notice N-26-1](https://www.tax.ny.gov/forms/n-notices/n-26-1.htm)).
- An extension to October 15, 2026 only helps if Form IT-370 was filed by April 15, 2026 with full payment of the properly estimated tax. Interest runs from April 15, 2026 on any unpaid tax ([IT-370-I](https://www.tax.ny.gov/pdf/current_forms/it/it370i.pdf)).

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
