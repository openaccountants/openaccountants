---
name: mo-income-tax
description: "Missouri MO-1040: 2026 brackets, separate spouse computation, business and capital-gain subtractions, federal tax deduction, estimates and filing-cycle limits."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mo-income-tax"
  jurisdiction: "US-MO"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Missouri individual income tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Missouri resident individuals, including sole proprietors and disregarded single-member LLC owners, preparing Form MO-1040. Federal inputs belong to `us-form-1040-individual-return`, `us-schedule-c-and-se-computation` and `us-section-179-and-bonus-depreciation`. Missouri starts with federal adjusted gross income (FAGI). Published **2026 MO-1040ES** supplies the 2026 brackets and estimate rules. Annual return line references below describe the final **2025-2026 filing cycle**, pending final 2026 instructions. [2026 estimates](https://dor.mo.gov/forms/MO-1040ES_2026.pdf); [final annual booklet](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

A Missouri domiciliary is generally resident, but a domiciliary with no permanent Missouri living quarters, permanent quarters elsewhere and no more than 30 Missouri days meets the stated exception. A nondomiciliary with permanent Missouri living quarters and **more than 183 days** can be resident. These are combined tests, not a day-count-only rule. The final annual booklet exempts from filing people not required to file federally and certain low-income filers: resident Missouri AGI below 1,200, nonresident Missouri income below 600, or Missouri AGI below the applicable standard deduction plus exemption. A return can still be needed for a withholding refund. [Annual booklet, pp.3-5](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

## Rates, bands and thresholds

USD, 2026; same schedule for each taxpayer. On a married combined Missouri return, compute **each spouse's tax separately**, then combine. Never apply this schedule once to combined taxable income or double the band boundaries.

| Missouri taxable income | Tax computation | Official source |
| --- | --- | --- |
| 0-1,348 | 0 | [2026 MO-1040ES chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 1,348-2,696 | 2% of excess over 1,348 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 2,696-4,044 | 27 + 2.5% of excess over 2,696 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 4,044-5,392 | 61 + 3% of excess over 4,044 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 5,392-6,740 | 101 + 3.5% of excess over 5,392 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 6,740-8,088 | 148 + 4% of excess over 6,740 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 8,088-9,436 | 202 + 4.5% of excess over 8,088 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Over 9,436 | 263 + 4.7% of excess over 9,436 | [2026 chart](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Individual estimate trigger | Expected Missouri tax after credits/withholding **100 or more** | [2026 MO-1040ES, item 1](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Missouri-source business income subtraction | 20% of qualifying positive combined business income, no duplicate subtraction | [MO-A line 17](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [143.022](https://revisor.mo.gov/main/OneSection.aspx?section=143.022) |
| State HOH / qualifying widow(er) additional exemption | 1,400; same filing status as federal return | [2026 estimate line 5](https://dor.mo.gov/forms/MO-1040ES_2026.pdf) |
| Federal-income-tax deduction cap | 5,000 other returns; 10,000 married combined, after income-based percentage | [143.171](https://revisor.mo.gov/main/OneSection.aspx?section=143.171); [annual line 13](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf) |

Published bracket constants are rounded whole-dollar amounts. Do not substitute an independently accumulated 262.86 for the published 263. Annual tax-table lookup and whole-dollar rounding can differ from a rate-schedule estimate. Federal standard-deduction amounts have their home in the federal skill; obtain the applicable 2026 federal input and apply Missouri's rules, rather than copying old 2025 amounts.

## The base

Begin with FAGI, splitting jointly reported income between spouses using the adjusted-gross-income worksheet. Apply Form MO-A additions/subtractions separately. Household deduction allocation uses the spouses' Missouri income percentages; where one spouse has negative income and the other positive, the annual instructions use zero/100%. Do not blindly halve deductions. Non-Missouri municipal-bond interest can require addition; qualifying U.S.-obligation interest and state income-tax refunds included federally can qualify for subtraction, with the actual related-expense rules. A federal tax refund that previously produced a Missouri benefit may require an addition. [Annual booklet, pp.6-8, MO-A](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [143.121](https://revisor.mo.gov/main/OneSection.aspx?section=143.121).

**Business deduction.** Combine Missouri-source Schedule C net profits, Schedule E Part II partnership/S corporation income or loss and Schedule F/Form 4835 combined profits under the worksheet. Deduct 20% of the eligible positive total to the extent included in FAGI and not already subtracted. Remove agricultural-disaster relief already excluded. This is Missouri's business-income subtraction under 143.022, distinct from federal QBI; ordinary Schedule E rental income outside Part II is not automatically eligible. Federal SE-tax and self-employed health-insurance deductions already in FAGI are not deducted again. [MO-A line 17 and worksheet](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [143.022](https://revisor.mo.gov/main/OneSection.aspx?section=143.022).

**Capital gains.** Section 143.121.3(14)(a) allows an individual 100% of income federally reported as capital gain beginning in **2025**. The current DOR FAQ contradicts itself: its opening and combined-return example say 2025, while one answer says first claim 2026. The statute and final 2025 MO-A line 18 resolve that conflict in favour of 2025 commencement. Both short- and long-term capital gain included federally can qualify; ordinary business-asset recapture is not automatically capital gain. A capital loss is not an extra subtraction. For spouses with a net combined gain 10,000 made up of one spouse's 15,000 gain and the other's 5,000 loss, the annual allocation puts 10,000 on the gaining spouse's MO-A, zero on the losing spouse's, not 15,000. Section 143.022 owns business income, not this capital-gain provision. [Statute](https://revisor.mo.gov/main/OneSection.aspx?section=143.121); [final MO-A line 18](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [FAQ conflict/example](https://dor.mo.gov/faq/taxation/individual/capital-gains-subtraction.html).

The 2026 gold/silver-specie subtraction is already encompassed by the individual's general capital-gain subtraction: do not claim it twice. Corporations, trusts and elected PTEs have different eligibility; use `mo-corporate-tax`. [DOR specie FAQ](https://dor.mo.gov/faq/taxation/individual/specie_subtraction.html).

**Federal income tax deduction.** Use same-year federal **income tax liability after the specified credits**, not payroll withholding, estimates paid, a prior-year proxy, self-employment tax, FICA or railroad tax. In the verified 2025 annual mapping, lines 9-11 derive the eligible amount from federal return tax and the listed credits/other-tax adjustments. The base is not simply federal total tax. Multiply that eligible base by the percentage below, then apply the 5,000/10,000 cap. Use the total Missouri AGI on the combined return to select the percentage, not separate spouse AGI. [Annual lines 9-13](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [143.171](https://revisor.mo.gov/main/OneSection.aspx?section=143.171).

| Missouri income range for the percentage | Deductible percentage of eligible federal liability | Official source |
| --- | --- | --- |
| 25,000 or less | 35% | [143.171.2; annual line 12 uses Missouri AGI](https://revisor.mo.gov/main/OneSection.aspx?section=143.171) |
| 25,001-50,000 | 25% | [143.171.2](https://revisor.mo.gov/main/OneSection.aspx?section=143.171) |
| 50,001-100,000 | 15% | [143.171.2](https://revisor.mo.gov/main/OneSection.aspx?section=143.171) |
| 100,001-125,000 | 5% | [143.171.2](https://revisor.mo.gov/main/OneSection.aspx?section=143.171) |
| 125,001 or more | 0% | [143.171.2](https://revisor.mo.gov/main/OneSection.aspx?section=143.171) |

**Deductions and credits.** The annual booklet carries the federal standard deduction when federally standard; when federally itemized, compare allowed Missouri itemization with the state standard deduction unless required to itemize. MO-A Part 2 adjusts federal itemization, including income-tax and other state-specific items; do not subtract both methods or assume independent state itemization when federal standard was claimed. Preserve qualified age/blind/disaster adjustments and the separate 1,400 HOH/QSS state exemption. [Annual lines 14-15 and MO-A Part 2](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [2026 estimate lines 5-6](https://dor.mo.gov/forms/MO-1040ES_2026.pdf).

Social Security retirement subtraction requires age 62 or older; qualifying Social Security disability has its own eligibility. Removal of the income phase-out does not make every under-62 survivor benefit automatically exempt. Public/private pension and military retirement deductions also need their worksheets and qualifying facts. Do not conflate state deductions with federal exclusion. [MO-A Part 3](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

Working Family Tax Credit is nonrefundable, limited by remaining Missouri tax, and is 20% of federal EIC **recomputed under the law as of January 1,2021**, subject to qualifying status and current-year federal EIC eligibility. It is not necessarily 20% of the current federal EIC actually received. Use MO-WFTC. Senior/disabled property-tax/rent credit uses MO-PTS with a return or eligible MO-PTC standalone; eligibility, household income, ownership/rent and other claimant rules need separate support. Other credits use MO-TC and approval records. [Annual lines 36-40, MO-A Part 3, MO-PTS/MO-WFTC](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

## Deadlines and filing

The ordinary calendar-year filing/payment date is April 15 following the year; the verified 2025 return was due April 15,2026. For 2026 the ordinary date is April 15,2027, subject to official relief and final instructions. A federal filing extension ordinarily extends filing; without one use MO-60 as required. An extension does not extend payment. File MO-1040, MO-A and applicable schedules with required federal attachments through approved e-file or the correct paper address. An amended return uses **MO-1040 marked amended**, with corrected schedules and reason, not a presumed MO-1040X. [Annual booklet, pp.3-5](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

2026 individual estimates use MO-1040ES, generally April 15, June 15, September 15, January 15 following, adjusted for weekends/holidays. Amend by the next installment date after a material change. Safe-harbour protection requires timely cumulative installments reaching either 100% of a prior 12-month return that showed liability, or 90% of current tax; qualifying farmers use 66 2/3% and may use the January 15 payment/March 1 filing rule when at least two-thirds of estimated Missouri gross income is farming. Payment at year end alone does not cure earlier underpayment. [2026 MO-1040ES, items 1-9](https://dor.mo.gov/forms/MO-1040ES_2026.pdf).

## Penalties and interest

The annual booklet gives late filing 5% of unpaid tax per month up to 25%, late payment 5%, and calendar 2026 interest 7% annually. Extension and reasonable-cause rules require actual facts; estimate underpayment is a separate MO-2210 computation. Interest crossing January 1 needs that later calendar year's published rate;7% is not asserted for 2027. [Annual booklet, pp.3-4](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [2026 estimates](https://dor.mo.gov/forms/MO-1040ES_2026.pdf).

## Cross-border points

Residents generally report all income with potential MO-CR credit for qualifying other-state income tax. Part-year filers compare resident treatment with MO-CR and nonresident treatment with MO-NRI, using MO-1040 in either case; do not claim both methods for the same taxpayer. A spouse may independently choose the appropriate method. Nonresidents compute tax on all income and then the Missouri income percentage under MO-NRI, rather than applying the brackets only to Missouri wages. Missouri headquarters alone does not make a nonresident's wholly out-of-state remote wages Missouri-source. [Annual booklet, pp.4-5, lines 31-32](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf); [remote-work resources](https://dor.mo.gov/taxation/business/remote.html).

City earnings taxes in Kansas City and St. Louis remain a separate job: residence, actual work location, business-profit allocation, current rate, returns and refunds need current city-specific support. `mo-payroll` preserves the old city cases as conditional arithmetic and explicitly identifies the unresolved city filing rules. Interstate transport, military spouses, nonresident athletes/entertainers, credits and multi-state businesses need their special rules. Entity filings and elected PTE tax belong to `mo-corporate-tax`; employer withholding/UI to `mo-payroll`; consumer use tax to `mo-sales-tax`.

## Two worked examples that recompute

**Invented sole proprietor, 2026 estimate.** Single resident has FAGI60,000 including eligible Missouri Schedule C profit 50,000 after federal adjustments. Assume no other state adjustments, eligible same-year federal income-tax-liability base 6,000 and allowed standard-deduction input 16,100 supplied by the federal computation. State business subtraction 10,000 gives Missouri AGI50,000, selecting 25%, so federal-tax deduction 1,500. Taxable income 32,400; rate-schedule estimate 263+(32,400-9,436)x 4.7%=1,342.308, about 1,342.31, before credits/payments. This is not a computation of federal SE tax or a final annual tax-table result.

```oa-check
name: Missouri business subtraction and federal tax percentage
inputs:
  fagi: 60000
  eligible_business: 50000
  eligible_federal_tax: 6000
  federal_standard_input: 16100
steps:
  - business_subtraction: eligible_business * 0.20
  - mo_agi: fagi - business_subtraction
  - federal_deduction: eligible_federal_tax * 0.25
  - taxable: mo_agi - federal_deduction - federal_standard_input
  - tax: round(263 + (taxable - 9436) * 0.047, 2)
expected:
  business_subtraction: 10000
  mo_agi: 50000
  federal_deduction: 1500
  taxable: 32400
  tax: 1342.31
```

**Itemization decision.** Another invented single resident has Missouri AGI80,000, no eligible federal-tax deduction in this simplified case, and federally itemized. Allowed Missouri itemization after MO-A adjustments is 19,000; standard input from the federal computation is 16,100. Itemizing produces taxable income 61,000 and tax 2,686.51 versus taxable 63,900 and tax 2,822.81 with standard, saving 136.30. State facts permit the comparison because federal itemization was used; do not generalize it to federal-standard filers.

```oa-check
name: Missouri allowed itemization decision
inputs:
  mo_agi: 80000
  allowed_itemized: 19000
  standard_input: 16100
steps:
  - standard_taxable: mo_agi - standard_input
  - itemized_taxable: mo_agi - allowed_itemized
  - standard_tax: round(263 + (standard_taxable - 9436) * 0.047, 2)
  - itemized_tax: round(263 + (itemized_taxable - 9436) * 0.047, 2)
  - saving: round(standard_tax - itemized_tax, 2)
expected:
  standard_taxable: 63900
  itemized_taxable: 61000
  standard_tax: 2822.81
  itemized_tax: 2686.51
  saving: 136.3
```

## Ask the client first

1. Tax year, domicile, permanent homes, Missouri days, moves and all other states' income/returns?
2. Filing status, spouse's separately owned income/losses, federal itemization, age/disability and dependent facts?
3. FAGI, Missouri-source Schedule C/E-II/F/4835 profit/loss, capital-gain reporting, bonds, refunds and depreciation records?
4. Actual federal income-tax liability/credit schedules, state deductions, pension/SSA documents and duplicate deductions?
5. Withholding, dated estimates, prior 12-month liability, credit approvals, property/rent eligibility and city work/residence?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 MO-1040ES. Read for 2026 rate chart, spouse allocation, state HOH exemption, estimate threshold/dates/safe harbours. | https://dor.mo.gov/forms/MO-1040ES_2026.pdf | 2026-11-13 |
| Final 2025 MO-1040 booklet. Read for 2025-2026 filing cycle: residency, MO-A, deductions, credits, forms, filing, payments and penalties. | https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf | 2026-11-13 |
| 143.121 Missouri AGI. Read for capital-gain commencement, specie and state adjustments; resolves inconsistent FAQ date. | https://revisor.mo.gov/main/OneSection.aspx?section=143.121 | 2026-11-13 |
| 143.022 business deduction. Read for business-income components, ownership and maximum 20%. | https://revisor.mo.gov/main/OneSection.aspx?section=143.022 | 2026-11-13 |
| 143.171 federal tax deduction. Read for same-year liability, individual percentages/caps and corporate distinction. | https://revisor.mo.gov/main/OneSection.aspx?section=143.171 | 2026-11-13 |
| Capital gains FAQ. Read for combined-spouse allocation and entity restrictions; inconsistent commencement answer reconciled. | https://dor.mo.gov/faq/taxation/individual/capital-gains-subtraction.html | 2026-11-13 |
| Specie FAQ. Read for 2026 gold/silver and prohibition on double individual subtraction. | https://dor.mo.gov/faq/taxation/individual/specie_subtraction.html | 2026-11-13 |
| Alternative remote work resources. Read for nonresident remote work and MO-CR versus MO-NRI. | https://dor.mo.gov/taxation/business/remote.html | 2026-11-13 |

Not yet confirmed: final 2026 annual MO-1040/MO-A/MO-NRI/MO-CR/MO-WFTC/MO-PTS/MO-TC/MO-2210 forms and line mapping, detailed pension/disability/property-credit/other-credit calculations, special military/transport/athlete cases and city earnings-tax computations;2027 interest rate. Federal figures remain owned by federal skills.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mo-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mo-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
