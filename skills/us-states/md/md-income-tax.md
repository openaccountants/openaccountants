---
name: md-income-tax
description: Use this skill whenever asked about Maryland individual income tax. Trigger on phrases like "Maryland income tax", "MD income tax", "Form 502", "Comptroller of Maryland", "Maryland county tax", "piggyback tax". Maryland has 10 graduated state brackets (2%–6.50%) PLUS mandatory county/city income taxes (2.25%–3.20%). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-MD
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Maryland individual income tax: resident Form 502 for tax year 2026

Figures are for tax year 2026 (returns filed in 2027) unless a line says 2025. The Comptroller of Maryland had not yet published the 2026 resident instructions when this Guide was written (September 2026). The 2026 figures below come from the statute and from the Comptroller's 2026 estimated-tax worksheet (Form PV worksheet). Where a 2026 amount is not yet final, the Guide says so. A separate section covers 2025 returns, which are still being filed on extension until 15 October 2026.

This Guide covers full-year Maryland residents filing Form 502, including sole proprietors, single-member LLC owners, employees and investors. It covers the State income tax, the county or Baltimore City local income tax, and the 2% additional tax on net capital gain. It does not compute nonresident (Form 505) or part-year returns, fiduciary returns, or the pass-through entity tax (Form 510/511). Those are listed under "When to refuse or refer". [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)

## Ask the client first

- Which tax year is being filed? A 2025 return filed now uses the 2025 rules in the 2025 section below. A 2026 return or 2026 estimate uses the main tables.
- Were they a Maryland resident all year? Residence means Maryland domicile, or a place of abode in Maryland for more than six months of the year together with physical presence of 183 days or more. Part-year and nonresident cases are referred.
- Where did they live on 31 December (the last day of the tax year)? That address, and its four-digit political subdivision code, sets the local tax rate. A mid-year move inside Maryland does not split the local tax.
- What is their federal filing status and federal adjusted gross income (FAGI)? Most Maryland thresholds test FAGI, not Maryland income.
- Did they itemize on the federal return? A Maryland itemized deduction is allowed only if they itemized federally.
- Do they have net capital gain, and is FAGI above $350,000? If so, list each gain by asset type to test the surtax exclusions (primary home, retirement accounts, section 179 property, and others). [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- Ages and disability status on 31 December for taxpayer, spouse and dependents; any pension, 401(k), 403(b) or 457(b) income; Social Security received.
- Business facts: Schedule C, E or K-1 income; any federal bonus depreciation, section 174A research expensing or section 163(j) interest changes; any pass-through entity (PTE) that paid Maryland PTE tax for them.
- Maryland withholding (W-2, 1099), estimated payments made, and any 2025 overpayment applied to 2026.
- Income taxed by another state or a locality (credit on Form 502CR), and where the other state is DC, Virginia, West Virginia or Pennsylvania.

## The method, step by step

1. Confirm the return is a full-year resident Form 502 and fix the tax year. Refer part-year and nonresident cases (see "When to refuse or refer").
2. Start from federal adjusted gross income on Line 1 of Form 502 (federal AGI copied from the federal Form 1040). Maryland does not start from federal taxable income, so the federal standard deduction and the section 199A (QBI) deduction never reduce Maryland income.
3. Add Maryland additions (Lines 2 to 5, total on Line 6; for example non-Maryland state and local bond interest and decoupling add-backs on Form 500DM) and subtract Maryland subtractions (Lines 8 to 14, total on Line 15; for example Social Security, the pension exclusion, U.S. obligation interest, the two-income subtraction). The result is Maryland adjusted gross income (Line 16).
4. Choose the standard deduction or, only if the client itemized federally, itemized deductions reduced by state and local income taxes and by the high-income phase-out. Use whichever is larger.
5. Subtract personal exemptions, reduced by the FAGI phase-out. The result is Maryland taxable net income (Line 20).
6. Compute State tax on Line 20 using the tax tables (taxable income under $100,000) or the rate schedule (taxable income of $100,000 or more). [Instruction 17](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
7. If FAGI exceeds $350,000, compute the additional 2% tax on net capital gain on Form 502CG and add it (Line 21b). [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
8. Subtract State credits (earned income, poverty level, Form 502CR credits including credit for tax paid to other states and PTE tax paid).
9. Compute local income tax on the same Line 20 amount at the rate of the county or Baltimore City of residence on 31 December, using the county brackets where the county has them. Subtract local credits.
10. Reconcile withholding, estimated payments and refundable credits; compute any underpayment interest on Form 502UP; file and pay by the deadline.

## Rates and figures

### State income tax rate schedules, tax years 2025 and 2026 ([rate schedules](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf); [statute](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false))

The 2025 Budget Reconciliation and Financing Act (Chapter 604 of 2025) kept the brackets up to 5.75%, capped that bracket, and added two top brackets for tax years beginning after 31 December 2024. The same schedules appear in the Comptroller's 2026 estimated-tax worksheet.

Schedule I: Single, Married Filing Separately, Dependent (and fiduciaries)

| Taxable net income | Maryland tax |
| --- | --- |
| $1 to $1,000 | 2.00% of taxable net income |
| $1,001 to $2,000 | $20.00 plus 3.00% of excess over $1,000 |
| $2,001 to $3,000 | $50.00 plus 4.00% of excess over $2,000 |
| $3,001 to $100,000 | $90.00 plus 4.75% of excess over $3,000 |
| $100,001 to $125,000 | $4,697.50 plus 5.00% of excess over $100,000 |
| $125,001 to $150,000 | $5,947.50 plus 5.25% of excess over $125,000 |
| $150,001 to $250,000 | $7,260.00 plus 5.50% of excess over $150,000 |
| $250,001 to $500,000 | $12,760.00 plus 5.75% of excess over $250,000 |
| $500,001 to $1,000,000 | $27,135.00 plus 6.25% of excess over $500,000 |
| Over $1,000,000 | $58,385.00 plus 6.50% of excess over $1,000,000 |

Schedule II: Married Filing Jointly, Head of Household, Qualifying Surviving Spouse

| Taxable net income | Maryland tax |
| --- | --- |
| $1 to $1,000 | 2.00% of taxable net income |
| $1,001 to $2,000 | $20.00 plus 3.00% of excess over $1,000 |
| $2,001 to $3,000 | $50.00 plus 4.00% of excess over $2,000 |
| $3,001 to $150,000 | $90.00 plus 4.75% of excess over $3,000 |
| $150,001 to $175,000 | $7,072.50 plus 5.00% of excess over $150,000 |
| $175,001 to $225,000 | $8,322.50 plus 5.25% of excess over $175,000 |
| $225,001 to $300,000 | $10,947.50 plus 5.50% of excess over $225,000 |
| $300,001 to $600,000 | $15,072.50 plus 5.75% of excess over $300,000 |
| $600,001 to $1,200,000 | $32,322.50 plus 6.25% of excess over $600,000 |
| Over $1,200,000 | $69,822.50 plus 6.50% of excess over $1,200,000 |

On the return, use the Comptroller's tax tables if taxable income is less than $100,000, and the rate schedule worksheet if it is $100,000 or more. The tables round within $50 bands, so a hand computation from the schedule can differ by a few dollars below $100,000. [Instruction 17](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)

### Additional 2% tax on net capital gain, from tax year 2025 ([statute](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false); [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf))

- Who: an individual whose FAGI is more than $350,000, regardless of filing status. The test is FAGI "in excess of" $350,000, so FAGI of exactly $350,000 is not caught. It is a cliff, not a phase-in: once FAGI is over the threshold, the 2% applies to all the net capital gain included in Maryland AGI, not only the part above $350,000. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- What: 2% of net capital gain (net long-term capital gain over net short-term capital loss, as determined federally) included in Maryland adjusted gross income, on top of the regular rates. Short-term gains that are not part of federal net capital gain are taxed only at the regular rates. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- Period: applies for tax years beginning after 31 December 2024 (from tax year 2025). The statute sets no end date. [§ 10-105(a)(4)](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false); [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- Includes gain passed through from a PTE or distributed by a fiduciary to a member or beneficiary whose FAGI is over $350,000. The PTE does not pay the 2% for the member; the member pays it and should cover it in estimated payments. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- Excluded gain (to the extent included in federal net capital gain): a primary residence sold for less than $1,500,000 that is a single-family home, town house, row home, residential condominium unit or residential cooperative unit (with its land and any accessory dwelling unit); assets held in 401(k), 403(b), 457(b), IRA, Roth IRA, defined contribution, defined benefit or similar retirement plans; cattle, horses or breeding livestock held more than 12 months where more than 50% of gross income is from farming or ranching; land under (or about to be placed under) a conservation, agricultural or forest preservation easement; property used in a trade or business whose cost is deductible under IRC section 179; and affordable housing owned by a nonprofit. [statute](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false)
- A like-kind exchange gain deferred federally under IRC section 1031 is not in FAGI, so it is not in Maryland AGI and not subject to the 2% in that year. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- Report on Form 502CG; the tax goes on Form 502 Line 21b (Line 20a amount multiplied by .02). [Instruction 17](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)

### Standard deduction ([§ 10-217](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-217&enactments=false))

| Filing status | Tax year 2025 | Tax year 2026 |
| --- | --- | --- |
| Single, Married Filing Separately, Dependent | $3,350 | $3,350 indexed for inflation (final amount not yet published) |
| Married Filing Jointly, Head of Household, Qualifying Surviving Spouse | $6,700 | $6,700 indexed for inflation (final amount not yet published) |

- From tax year 2025 the standard deduction is a flat amount. The old rule (a percentage of Maryland AGI between a minimum and a maximum) was repealed and must not be used for 2025 or later. [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- For taxable years beginning after 31 December 2025 the amount is increased each year by a cost-of-living adjustment, with any increase rounded down to the next lowest multiple of $50. [§ 10-217(c)](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-217&enactments=false)
- The Comptroller's 2026 estimated-tax worksheet still uses $3,350 and $6,700. Its 2026 employer withholding guide uses a standard deduction of $3,400 in the withholding formula. Treat $3,350 / $6,700 as a safe estimate for 2026 and confirm the final 2026 return amount in the 2026 resident instructions before filing. [2026 withholding guide](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/withholding/2026/pm225.pdf)

### Itemized deductions and the high-income phase-out ([§ 10-218](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-218&enactments=false))

- Only a taxpayer who itemized on the federal return may itemize for Maryland. Itemizing federally does not force itemizing for Maryland; compute both ways. [Instruction 16](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Start from federal Schedule A total itemized deductions, remove state and local income taxes deducted federally (Line 17b), and remove any preservation or conservation easement deduction claimed as a credit. For 2025 the booklet notes the Line 17b amount is capped at $40,000 ($20,000 married filing separately) because of the federal SALT limit. [2025 booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- From tax year 2025, if FAGI exceeds $200,000 ($100,000 for married filing separately), reduce the remaining itemized deductions by 7.5% of the FAGI above that threshold (Worksheet 14A, Line 17c). The reduction applies after every other limit. It does not apply to fiduciaries. [§ 10-218(c)](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-218&enactments=false)

### Personal exemptions ([§ 10-211](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-211&enactments=false))

Each exemption for the taxpayer, spouse and each dependent is $3,200, plus an extra $3,200 for a dependent aged 65 or over. Add $1,000 for the taxpayer or spouse who is 65 or over on the last day of the tax year, and $1,000 for one who is blind; these $1,000 amounts are not phased out. A person who turns 65 after year-end but before filing does not qualify. A dependent taxpayer (claimable by someone else) gets $0.

| FAGI | Single / MFS: each exemption | MFJ / HOH / QSS: each exemption |
| --- | --- | --- |
| $100,000 or less | $3,200 | $3,200 |
| Over $100,000, not over $125,000 | $1,600 | $3,200 |
| Over $125,000, not over $150,000 | $800 | $3,200 |
| Over $150,000, not over $175,000 | $0 | $1,600 |
| Over $175,000, not over $200,000 | $0 | $800 |
| Over $200,000 | $0 | $0 |

Source: [Exemption Amount Chart 10A](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf); the same chart is in the [2026 estimated-tax worksheet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf).

### Local (county and Baltimore City) income tax ([2026 rates](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf); [2025 rates](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf))

Local tax is a percentage of the same Maryland taxable net income (Line 20). A county may set a rate of at least 2.25% and, from tax years beginning after 31 December 2025, not more than 3.30% (previously 3.20%). Only Dorchester used the one-year option to charge 3.30% for 2025. Counties may use brackets, but no bracket may be below 2.25% and a higher bracket may not carry a lower rate. [§ 10-106](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-106&enactments=false)

| Jurisdiction | 2025 | 2026 |
| --- | --- | --- |
| Baltimore City | 3.20% | 3.20% |
| Allegany | 3.03% | 3.20% |
| Anne Arundel | brackets, see below | brackets, see below |
| Baltimore County | 3.20% | 3.20% |
| Calvert | 3.20% | 3.20% |
| Caroline | 3.20% | 3.20% |
| Carroll | 3.03% | 3.03% |
| Cecil | 2.74% | 2.74% |
| Charles | 3.03% | 3.03% |
| Dorchester | 3.30% | 3.30% |
| Frederick | brackets, see below | brackets, see below |
| Garrett | 2.65% | 2.65% |
| Harford | 3.06% | 3.06% |
| Howard | 3.20% | 3.20% |
| Kent | 3.20% | 3.30% |
| Montgomery | 3.20% | 3.20% |
| Prince George's | 3.20% | 3.20% |
| Queen Anne's | 3.20% | 3.20% |
| St. Mary's | 3.20% | 3.20% |
| Somerset | 3.20% | 3.20% |
| Talbot | 2.40% | 2.40% |
| Washington | 2.95% | 2.95% |
| Wicomico | 3.20% | 3.20% |
| Worcester | 2.25% | 2.25% |

Anne Arundel County (2025 and 2026, [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)):
- Single, MFS, Dependent: 2.7% of taxable net income up to $50,000; $1,350 plus 2.94% of the excess over $50,000 up to $400,000; $11,640 plus 3.2% of the excess over $400,000.
- MFJ, HOH, QSS: 2.7% up to $75,000; $2,025 plus 2.94% of the excess over $75,000 up to $480,000; $13,932 plus 3.2% of the excess over $480,000.

Frederick County (2025 and 2026, [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)): Frederick applies one rate to the whole taxable net income, chosen by the income level.
- Single, MFS, Dependent: 2.25% up to $25,000; 2.75% from $25,001 to $50,000; 2.96% from $50,001 to $150,000; 3.20% at $150,001 or more.
- MFJ, HOH, QSS: 2.25% up to $25,000; 2.75% from $25,001 to $100,000; 2.96% from $100,001 to $250,000; 3.20% at $250,001 or more.

## Common adjustments and treatment

- Social Security and railroad retirement benefits included in FAGI are subtracted in full (Line 11). [Instruction 13](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Pension exclusion (Line 10a, Form 502R required): only if the taxpayer was 65 or over or totally disabled, or the spouse was totally disabled, on the last day of the year, and only for taxable income from an employee retirement system qualified under IRC sections 401(a), 403 or 457(b). A 401(k) or 403(b) qualifies; a traditional, Roth, rollover or SEP IRA does not. The 2025 maximum is $41,200 per qualifying individual, reduced by Social Security and railroad retirement benefits received. The 2026 maximum had not been published at the time of writing. [Instruction 13](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Child and dependent care expenses: a subtraction on Line 9 based on the expenses on federal Form 2441, subject to the dollar limits in Instruction 13. [Instruction 13](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Two-income subtraction: up to $1,200 when both spouses have income subject to Maryland tax and they file jointly (Worksheet 13D). [Instruction 13](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Interest on non-Maryland state and local bonds is an addition (Line 2); interest on Maryland and Maryland-subdivision bonds is not. U.S. obligation interest is a subtraction on Form 502SU and can require an exemption recalculation. [Instruction 12](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Self-employment: Schedule C and E income, the deductible part of self-employment tax, self-employed health insurance, and SEP, SIMPLE or solo 401(k) contributions all reach Maryland through FAGI. Nothing is re-deducted.
- Depreciation and One Big Beautiful Bill Act (P.L. 119-21) business provisions: for tax year 2025 and earlier, Maryland is automatically decoupled from federal full expensing of domestic research and experimental expenditures, the changed business interest limitation, and the special depreciation allowance for qualified production property. Maryland also remains decoupled from other federal depreciation allowances listed in the Form 500DM instructions (see Technical Bulletin 38). Compute the add-backs and later subtractions on Form 500DM. For 2026, check the 2026 Form 500DM instructions for Maryland's conformity position before filing. [2025 booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Credit for tax paid to another state (Form 502CR Part A) requires a copy of the other state's return; without it no credit is allowed. [Instruction 18](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| FAGI exactly $350,000 with capital gains | No 2% additional tax: the test is FAGI "in excess of" $350,000 | [TB 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf) |
| FAGI just over $350,000 | 2% on all included net capital gain, not just the excess | [§ 10-105](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false) |
| Primary home sold for exactly $1,500,000 | Not excluded: the exclusion needs a sale price of less than $1,500,000 | [§ 10-105](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false) |
| Gain on a rental or second home | Subject to the 2% if FAGI is over $350,000 | [TB 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf) |
| FAGI exactly $200,000, itemizing, not MFS | No phase-out reduction: only FAGI above $200,000 counts | [§ 10-218](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-218&enactments=false) |
| Single FAGI exactly $100,000 | Full $3,200 exemptions | [§ 10-211](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-211&enactments=false) |
| Federal standard deduction taken | Maryland standard deduction only | [§ 10-217](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-217&enactments=false) |
| Moved counties during the year | One local rate: county of residence on the last day of the year | [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf) |
| Spouses domiciled in different local jurisdictions | Separate Maryland returns recommended; if filing jointly, split local tax by income ratio and write "separate jurisdictions" on Line 28 | [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf) |
| Turned 65 on 2 January after the tax year | No $1,000 age exemption for that year | [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf) |

## Worked cases

These are illustrations for tax year 2026 using the 2026 rates and, for the standard deduction, the $3,350 / $6,700 amounts in the Comptroller's 2026 estimated-tax worksheet. Replace the standard deduction with the final indexed 2026 amount when it is published. On an actual return below $100,000 of taxable income, take the State tax from the tax table. [2026 worksheet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf)

**Case 1: ordinary single filer, Montgomery County.** A single sole proprietor, age 40, lives in Montgomery County all year. FAGI is $80,000; there are no additions, subtractions or dependents, and no capital gains. Standard deduction $3,350; one exemption of $3,200 (FAGI is not over $100,000). Taxable net income = 80,000 − 3,350 − 3,200 = 73,450. State tax = $90.00 + 4.75% × (73,450 − 3,000) = $3,436.38. Local tax = 3.20% × 73,450 = $2,350.40. Total Maryland and local tax before credits = $5,786.78. [rates](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf)

**Case 2: high-income couple with a capital gain, Howard County.** A married couple filing jointly lives in Howard County. FAGI is $400,000, which includes $100,000 of long-term net capital gain from selling listed shares in a taxable brokerage account. They itemized federally; their federal itemized deductions after removing state and local income taxes are $50,000. Phase-out reduction = 7.5% × (400,000 − 200,000) = $15,000, so Maryland itemized deductions are $35,000, larger than the $6,700 standard deduction. Exemptions are $0 (FAGI over $200,000). Taxable net income = 400,000 − 35,000 = 365,000. State tax = $15,072.50 + 5.75% × (365,000 − 300,000) = $18,810.00. Additional tax on net capital gain = 2% × 100,000 = $2,000. Local tax = 3.20% × 365,000 = $11,680.00. Total before credits = $32,490.00. [TB 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)

**Case 3: the $350,000 cliff.** A single filer has FAGI of exactly $350,000, including $120,000 of long-term gain on shares. No 2% additional tax is due. If one more dollar of interest pushes FAGI over $350,000, the additional tax is 2% × 120,000 = $2,400 on the whole gain. Plan timing of gains and deductions that reduce FAGI with this cliff in mind. [TB 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)

**Case 4: excluded home sale.** A married couple with FAGI over $350,000 sells their primary residence, a town house, for $1,400,000. The part of the gain that is taxable federally (after the federal home-sale exclusion) is in FAGI and Maryland AGI, and taxed at the regular Maryland and local rates. It is not subject to the 2% additional tax, because the home was their primary residence, is a listed dwelling type, and sold for less than $1,500,000. A second home or rental sold on the same terms would be subject to the 2%. [statute](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-105&enactments=false)

**Case 5: exemption phase-out.** A single filer with FAGI of $120,000 is allowed $1,600 per exemption, not $3,200. If they are 65 or over on 31 December, they also get the full $1,000 age exemption, which is not phased out. [§ 10-211](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-211&enactments=false)

**Case 6: Anne Arundel brackets.** A single Anne Arundel County resident has taxable net income of $60,000. Local tax = $1,350 + 2.94% × (60,000 − 50,000) = $1,644.00. [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)

## When to refuse or refer

- Nonresidents with Maryland-source income file Form 505 and pay the special nonresident tax at 2.25% in place of a county rate; part-year residents need prorated exemptions and deductions. Refer both. [nonresident booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/nonresident-booklet.pdf)
- Wage reciprocity: residents of DC, Pennsylvania or Virginia are exempt from Maryland tax on Maryland wages only if they did not maintain a place of abode in Maryland for more than six months (183 days or more) of the year; West Virginia residents are exempt on Maryland wages regardless of time spent in Maryland. A Pennsylvania resident with only Maryland wages need not file only if their Pennsylvania locality does not tax Maryland residents. Refer these cases. [nonresident booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/nonresident-booklet.pdf)
- A PTE election (Form 510/511) or a member credit for PTE tax: refer. For 2025 the PTE rate on individual members' shares is 8.75%. [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- Capital gains where it is unclear whether an asset falls in a surtax exclusion (mixed-use home, easement land, section 179 property, farm livestock): refer and read Technical Bulletin 58.
- Decoupling adjustments on Form 500DM (bonus depreciation, research expensing, business interest), especially for 2026 where Maryland's conformity must be confirmed.
- Business tax credits (Form 500CR), heritage structure, film, biotechnology and similar credits.
- Spouses domiciled in different jurisdictions, military taxpayers, deceased taxpayers, fiscal-year filers and amended returns (Form 502X).
- Any 2026 return filed before the Comptroller publishes the final indexed 2026 standard deduction and pension exclusion: do not guess; wait for the 2026 instructions.

## Filing and payment steps with deadlines

- Who must file: a Maryland resident who must file a federal return. File also if the only purpose is to claim a refund of Maryland withholding or a refundable credit. [Instruction 1](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Due date: the 15th day of the fourth month after the tax year ends, that is 15 April 2027 for tax year 2026. If the date falls on a Saturday, Sunday or legal holiday, file by the next business day. [extension worksheet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf)
- Electronic payment: a taxpayer who files electronically by the due date and pays electronically (including direct debit or credit card) has until 30 April to pay. A bank bill-pay that mails a paper check is not an electronic payment. [Instruction 24](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Extension: Maryland grants an automatic six-month extension to file if the taxpayer filed a federal extension and expects to owe no Maryland tax. If tax is due, file Form PV (or the online extension) with full payment by the original due date. An extension extends time to file, not time to pay; interest runs on unpaid tax from the original due date. [extension worksheet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf)
- Estimated tax (pay with Form 502D, the Form PV voucher, or online): required if the taxpayer must file and expects tax of more than $500 over Maryland withholding. For 2026, pay at least one-fourth by 15 April 2026, then 15 June 2026, 15 September 2026 and 15 January 2027. The fourth payment can be replaced by filing and paying in full by 31 January 2027. Farmers and fishermen (at least two-thirds of gross income) may pay once by 15 January 2027, or file and pay in full by 1 March 2027. Within 60 days of receiving $500 or more of prizes or lottery winnings without Maryland withholding, file a declaration and pay in full. [2026 worksheet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/forms/worksheets/2026-pv-worksheet.pdf)
- Underpayment interest generally does not apply if tax on income not subject to withholding is less than $500, or if timely quarterly payments are at least one-fourth of 110% of last year's tax, or total at least 90% of this year's tax. Compute on Form 502UP. [Instruction 22](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Include expected 2% capital gains tax in estimated payments, including gain expected from a PTE. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- Penalties and interest: the Comptroller may assess a penalty of up to 10% for failing to pay tax or file a return when due, plus interest. Refunds must be claimed within three years of the original due date. [Instruction 22](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Attach W-2s and 1099s showing Maryland tax withheld, Form 502B for dependents, Form 502R for retirement income, Form 502CG for the capital gains tax, Form 502CR for credits and the other state's return for a credit for tax paid elsewhere. Do not send federal forms unless requested. File and pay online through the Comptroller's website where possible.

## Tax year 2025 returns (filed in 2026, extended to 15 October 2026)

- Same State brackets as 2026, including the new 6.25% and 6.50% top brackets. [booklet](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Local rates: use the 2025 column above (Allegany 3.03%, Kent 3.20%, Dorchester 3.30%). [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- Standard deduction $3,350 / $6,700; itemized phase-out at 7.5% of FAGI above $200,000 ($100,000 MFS); 2% additional tax on net capital gain above the $350,000 FAGI line. All three first apply for tax year 2025. [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- Pension exclusion maximum $41,200. [Instruction 13](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Minimum filing levels (taxpayers under 65, 2025): single $15,750, married filing jointly $31,500, head of household $23,625. [Instruction 1](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- Underpaid 2025 estimated tax: the Comptroller waives interest to the extent the underpayment was caused by the 2025 rate increases. [Tax Alert](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/alerts/tax-alert-changes-to-standard-and-itemized-deductions-and-to-state-and-local-income-tax-rates-from-the-2025-legislative-session.pdf)
- Late payment of 2025 tax: interest at 10.8133% a year for months paid after 15 April 2026 and before 1 January 2027. [Instruction 22](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf)
- A 2025 return on extension is due six months after the original due date, that is by 15 October 2026. The extension did not extend the time to pay.

## Completion checklist

- [ ] Tax year confirmed; full-year residence and 31 December county confirmed.
- [ ] Line 1 equals federal AGI; additions and subtractions supported (Form 500DM, 502SU, 502R as needed).
- [ ] Standard deduction versus itemized compared; itemized only if itemized federally; phase-out applied if FAGI is over the threshold.
- [ ] Exemptions taken from the FAGI chart; $1,000 age and blind amounts added in full. [§ 10-211](https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gtg&section=10-211&enactments=false)
- [ ] State tax from the table (under $100,000) or rate schedule; FAGI tested against $350,000 and Form 502CG completed where needed. [Technical Bulletin 58](https://www.marylandtaxes.gov/content/dam/mdcomp/tax/legal-publications/technical-bulletins/tb-58.pdf)
- [ ] Local tax at the correct 2025 or 2026 rate or county brackets.
- [ ] Credits supported (other-state return attached; PTE K-1 attached).
- [ ] Withholding and estimated payments reconciled; Form 502UP interest checked.
- [ ] Filed and paid by the due date, or extension with payment made by the original due date.

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
