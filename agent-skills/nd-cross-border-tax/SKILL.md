---
name: nd-cross-border-tax
description: "Use when an individual's income crosses the North Dakota border in tax year 2026, covering nonresident and part-year filing on Form ND-1 and the North Dakota income ratio, the Minnesota and Montana reciprocity agreements and Form NDW-R, the statutory 7-month residence rule, military residence and the military pay exclusion, the employer credit for wages paid to a mobilized employee, and the credit for income tax paid to another state. Trigger on North Dakota nonresident, ND-1 part-year, ND Minnesota reciprocity, NDW-R, ND military pay, credit for tax paid another state North Dakota."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-cross-border-tax"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# North Dakota cross-border tax (nonresidents, reciprocity, military, credits), tax year 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer first.** Minnesota and Montana residents who work in North Dakota pay no North Dakota income tax on those wages under reciprocity (a Minnesota resident must return home at least once a month) and stop withholding by giving the employer Form NDW-R each year. Other nonresidents pay North Dakota tax computed on their whole North Dakota taxable income and then multiplied by the share of federal adjusted gross income that comes from North Dakota. A North Dakota resident taxed by another state on the same income claims the credit on Schedule ND-1CR, limited to the lesser of the other state's tax and the North Dakota tax on that income. The 2026 rate schedules are owned by `nd-income-tax`.

## Who this applies to

- Individuals who live elsewhere and have North Dakota-source income (wages for work in North Dakota, North Dakota rental or royalty income, a North Dakota business), and part-year residents who moved in or out during 2026.
- Residents of **Minnesota and Montana** working in North Dakota under the reciprocity agreements, and North Dakota residents working in those states.
- People with a home in North Dakota who spend more than 210 days there (the statutory 7-month rule).
- Members of the US armed forces stationed in or from North Dakota, and their civilian spouses.
- Employers of National Guard or reserve members mobilized for federal active duty.
- North Dakota residents who paid income tax to another state or a local jurisdiction in that state on the same income.

Business nexus and corporate apportionment are not here: see `nd-corporate-tax` and `nd-transfer-pricing`.

## Rates, bands and thresholds

The 2026 individual rate schedules (0%, 1.95% and 2.50%) and their breakpoints are owned by `nd-income-tax`; this skill does not restate them. The cross-border figures are:

| Item | Amount, tax year 2026 | Official source |
| --- | --- | --- |
| Statutory 7-month rule: a nonresident with a permanent place of abode in North Dakota files as a full-year resident above this many days in the state (2025 booklet, 2025-2026 filing cycle) | more than 210 days; excludes part-year North Dakota residents, full-year nonresident U.S. armed-forces members, and full-year Montana or Minnesota residents covered by reciprocity | [2025 individual booklet, "Statutory 7-month rule"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf) |
| Reciprocity: North Dakota withholding on covered wages that requires a North Dakota return to claim the refund (2025 booklet, 2025-2026 filing cycle) | USD 5.00 or more | same booklet, "Reciprocity" |
| Form NDW-R: employee gives it to the employer by this date each year, or within 30 days of starting work or moving | 28 February | [Form NDW-R (SFN 28729)](https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf) |
| North Dakota income ratio on the 2026 estimate worksheet: rounding | two decimal places, capped at 1.00 | [2026 Form ND-1ES, lines 16 to 18](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf) |
| Credit for income tax paid to another state | lesser of the tax actually paid to the other state and the North Dakota tax on the income taxed by the other state | [Tax Commissioner, credit for income tax paid to another state](https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction) |
| Mobilized employee credit (for the employer): rate | 25% of the lesser of continued compensation and the reduction in compensation | [Tax Commissioner, wages paid to a mobilized military employee credit](https://www.tax.nd.gov/wages-paid-mobilized-military-employee-tax-credit) |
| Mobilized employee credit: maximum per eligible employee | USD 1,000 | same |
| Mobilized employee credit: carryforward | five taxable years | same |

## The base

1. **Residents** are taxed on all income through federal taxable income and the state adjustments in `nd-income-tax`.
2. **Nonresidents:** North Dakota-source gross income includes wages and fees for services in North Dakota; income from tangible property in North Dakota (rents, oil and gas royalties, gains on that property); income from a trade or business carried on in North Dakota; estate and trust income from those sources; North Dakota gambling income; and unemployment compensation from earlier North Dakota work ([2025 booklet, "Gross income from North Dakota sources"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)).
3. **Not North Dakota-source for a nonresident:** military pay, interest, dividends, pensions, annuities, gains on intangible property, compensation exempt under the Minnesota or Montana reciprocity, compensation exempt under federal military and interstate commerce laws, and compensation exempt under North Dakota's mobile workforce exemption. Interest, dividends and gains are North Dakota-source if they come from a trade or business carried on in North Dakota (same booklet).
4. **Proration:** the tax is computed on the full North Dakota taxable income using the 2026 rate schedule, then multiplied by the North Dakota income ratio: North Dakota-source federal adjusted gross income (reduced by the state subtractions) divided by federal adjusted gross income (reduced by US obligation interest), rounded to two decimals ([2026 Form ND-1ES, lines 15 to 19](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)). For the final return, the **2025 Schedule ND-1NR, line 20, rounds the ratio to four decimal places**, rather than the two used for the 2026 estimate; line 23 applies that ratio to the full-income tax ([2025 Schedule ND-1NR, lines 20 to 23, 2025-2026 filing cycle](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28724-schedule-nd-1nr-2025.pdf)). Confirm the final 2026 schedule before preparing that return.
5. **Reciprocity wages:** a Minnesota resident who keeps a permanent home in Minnesota and returns to it at least once a month owes no North Dakota tax on pay for personal or professional services in North Dakota; a Montana resident owes no North Dakota tax on wages for work in North Dakota. Their non-wage North Dakota income (rentals, a North Dakota business, contract work outside the agreement) stays taxable ([2025 booklet, "Reciprocity"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf); [Form NDW-R instructions](https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf)). The wages remain taxable in the state of residence.
6. **Military:** a North Dakota resident in the armed forces files as a full-year resident wherever stationed; a nonresident service member stationed in North Dakota files only if they have North Dakota-source income other than military pay. Military pay included in federal taxable income is subtracted on Form ND-1, line 11, and taxable military retirement on line 14 ([2025 booklet](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). From tax year 2026, military pay that qualifies for the military pay deduction is no longer subject to North Dakota withholding (Senate Bill 2047, 2025), unless the member asks the employer to withhold (same booklet, "Military Updates").
7. **Credit for tax paid to another state:** a full-year or part-year resident who paid income tax to another state or a local jurisdiction in that state on the same income claims it on Schedule ND-1CR (Form ND-1, line 21). For a part-year resident the income must have been earned or received while a North Dakota resident. A resident included in another state's composite return filed by a pass-through entity also qualifies ([credit page, citing N.D.C.C. 57-38-30.3(4)](https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction)).

## Deadlines and filing

- **Form ND-1 for 2026:** due by the regular due date, generally 15 April 2027 ([2026 Form ND-1ES](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf)). A federal extension is recognized for North Dakota with no separate form; without one, Form 101 must be postmarked by the due date and needs good cause ([2025 booklet, "Extension of time to file"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)).
- **Who must file (2025 booklet rules):** a nonresident who must file a federal return and had North Dakota-source gross income. A Minnesota resident need not file if the only North Dakota income was pay for services and they returned home monthly; a Montana resident need not file if the only North Dakota income was wages (same booklet).
- **Reciprocity refund:** a Minnesota or Montana resident whose employer withheld USD 5.00 or more of North Dakota tax on covered wages files Form ND-1 for the refund and fills in the "MN/MT reciprocity" circle (item F) (same booklet).
- **Form NDW-R:** a new form every year, given to the employer by 28 February or within 30 days of starting work or changing residence. An incomplete form means the employer must withhold. The employer mails forms received by 28 February to the Office of State Tax Commissioner by 31 March, and others within 30 days ([Form NDW-R](https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf)).
- **North Dakota residents working in Minnesota or Montana:** Minnesota reciprocity on wages requires maintaining a home in North Dakota and returning to it at least once every month. Confirm those facts before using Minnesota Form MW-R or treating Minnesota withholding as refundable. Montana wages of a North Dakota resident have the separate reciprocity treatment described in the same instructions; use Montana Form MT-R when eligible. If reciprocity applies and the other state withheld tax, its refund return is the recovery route and no ND-1CR credit is allowed for that erroneous withholding. If the Minnesota home/monthly-return condition fails, do not assume an exemption or refund: obtain the Minnesota tax determination and assess any credit for actual Minnesota income tax under the ND-1CR credit method above ([2025 ND-1CR p2, "Did you work in Minnesota?", "Did you work in Montana?" and general credit instructions, 2025-2026 filing cycle](https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28721-schedule-nd-1cr-2025.pdf)).
- **Estimated tax:** a nonresident or new resident whose North Dakota income starts after the first due date pays in equal amounts over the remaining dates. The tests and dates are in `nd-estimated-tax`.

## Penalties and interest

Under [N.D.C.C. 57-38-45](https://ndlegis.gov/cencode/t57c38.pdf):

- Tax shown on a timely return but not paid: 5% of the unpaid tax or USD 5, whichever is greater.
- Return filed late: 5% of the tax (or USD 5) for the first month or part month, plus 5% for each further month or part, up to 25% in total.
- Interest on unpaid tax: 1% per month or part month, except the month the tax was due. With a valid extension: 12% per year from the original due date, and no penalty if the return and tax are in by the extended date ([2025 booklet, "Extension interest" and "Penalty and interest"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)).
- The Commissioner may waive penalty or interest for good cause (57-38-45(5)).
- Common reciprocity problem: a Minnesota or Montana resident who did not give the employer Form NDW-R has North Dakota tax withheld and must file to get it back. That is a refund claim, not a penalty.

## Cross-border points

- **Federal deduction for state income tax:** the federal state and local tax cap for 2025 and 2026 was changed by Public Law 119-21 and is owned by `us-schedule-a-itemized-deductions`; do not restate it here. (The old file's USD 10,000 figure is wrong for 2025 and 2026.)
- **Foreign income and treaties:** income tax treaties do not apply for North Dakota income tax unless the treaty specifically exempts income from tax by a US state, so treaty-exempt income can still be North Dakota-taxable ([2025 booklet, "Nonresident alien"](https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf)). The credit on Schedule ND-1CR is described for tax paid to another state or a local jurisdiction in that state; it is not a foreign tax credit. Manitoba and other foreign tax is handled federally.
- **Military spouses:** a civilian spouse is treated as a resident or nonresident according to an election under the federal Servicemembers Civil Relief Act; a nonresident civilian spouse living in North Dakota only to be with a service member stationed here does not file if all the booklet's conditions are met (same booklet).
- **Employers:** multi-state withholding follows a valid Form NDW-R, not the employee's address. Withholding mechanics belong to `nd-payroll`.
- **No exit or entry tax:** no such tax appears among the Tax Commissioner's income tax rules read for this skill; a mover is taxed by residence periods and source.

## Two worked examples that recompute

**Example 1: South Dakota resident with Fargo wages (no reciprocity).** Single, full-year South Dakota resident. 2026 federal adjusted gross income USD 115,000, of which USD 69,000 is wages for work in Fargo. North Dakota taxable income (worksheet line 5) USD 100,000, no subtractions. Tax on the full USD 100,000 under the 2026 single schedule (owned by `nd-income-tax`: 0% to USD 49,575, 1.95% to USD 250,400) is (100,000 - 49,575) x 1.95% = USD 983.29. Ratio 69,000 / 115,000 = 0.60. North Dakota tax USD 983.29 x 0.60 = USD 589.97.

```oa-check
name: ND 2026 nonresident, tax prorated by the ND income ratio
inputs:
  nd_taxable_income: 100000
  zero_band_top: 49575
  rate: 0.0195
  nd_source_agi: 69000
  federal_agi: 115000
steps:
  - full_tax: round((min(nd_taxable_income, 250400) - zero_band_top) * rate, 2)
  - ratio: round(min(nd_source_agi / federal_agi, 1), 2)
  - nd_tax: round(full_tax * ratio, 2)
expected:
  full_tax: 983.29
  ratio: 0.60
  nd_tax: 589.97
```

**Example 2: decision, should a Moorhead commuter give the employer Form NDW-R?** Full-year Minnesota resident who returns home every night, earning USD 55,000 of Fargo wages and nothing else from North Dakota. Under reciprocity the North Dakota tax on those wages is zero either way.

- **With Form NDW-R by 28 February:** no North Dakota withholding, no North Dakota return.
- **Without it:** the employer must withhold North Dakota tax (say USD 640 over the year, an invented figure). North Dakota tax is still zero, so the client must file Form ND-1 (item F) to get all USD 640 back after the year ends.
- **The figure that decides:** the cash withheld and the cost of an extra return, against nothing. Give the employer Form NDW-R every year.

```oa-check
name: ND reciprocity, refund when NDW-R was not filed
inputs:
  nd_wages: 55000
  nd_withheld_without_ndwr: 640
  nd_tax_rate_on_reciprocity_wages: 0
steps:
  - nd_tax: nd_wages * nd_tax_rate_on_reciprocity_wages
  - refund_due: nd_withheld_without_ndwr - nd_tax
  - cash_held_with_ndwr: 0
  - cash_held_without_ndwr: refund_due
expected:
  nd_tax: 0
  refund_due: 640
  cash_held_without_ndwr: 640
```

## Ask the client first

1. Where was the client domiciled during 2026, did any move cross a state line, and on what dates?
2. Does the client keep a permanent place of abode in North Dakota, and how many days were spent there?
3. Is the client a Minnesota or Montana resident working in North Dakota (and, for Minnesota, home at least monthly)? Is Form NDW-R on file with each employer for 2026?
4. Military: is the client or spouse in the armed forces, where is the permanent duty station, and what residence is claimed (including a Servicemembers Civil Relief Act election by the spouse)?
5. Which other states taxed the same income, and how much tax was actually paid there?
6. Any North Dakota rentals, royalties or business that keep North Dakota in scope with no North Dakota wages?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 individual income tax booklet, 2025-2026 filing cycle. Read for residence rules including the 7-month rule, who must file, nonresident North Dakota-source income and exceptions, reciprocity, military updates, extension and penalty pages, and Form ND-1 lines 11, 14, 20, 21 and 26. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/2025-individual-income-tax-booklet.pdf | 2026-11-14 |
| 2026 Form ND-1ES. Read for the nonresident and part-year worksheet lines 15 to 19, the North Dakota income ratio and the part-year installment rule. | https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28709-form-nd-1es-2026%20final.pdf | 2026-11-14 |
| 2025 Schedule ND-1NR, 2025-2026 filing cycle. Read for lines 18 to 23, especially the four-decimal ratio on line 20 and tax transfer on line 23. | https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2025-iit/28724-schedule-nd-1nr-2025.pdf | 2026-11-14 |
| 2025 Schedule ND-1CR, 2025-2026 filing cycle. Read for p2 general credit instructions and the Minnesota home/monthly-return and Montana reciprocity paragraphs, distinguishing actual other-state tax from refundable withholding. | https://www.tax.nd.gov/sites/www/files/documents/forms/software-developer/individual-income-forms/28721-schedule-nd-1cr-2025.pdf | 2026-11-14 |
| Form NDW-R (SFN 28729, 12-2023). Read for the employee and employer instructions: monthly-return condition, 28 February and 30-day deadlines, yearly renewal, mailing by 31 March. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf | 2026-11-14 |
| Tax Commissioner page, credit for income tax paid to another state or local jurisdiction. Read for qualifications, the lesser-of amount, Schedule ND-1CR and the N.D.C.C. 57-38-30.3(4) reference. | https://www.tax.nd.gov/credit-income-tax-paid-another-state-or-local-jurisdiction | 2026-11-14 |
| Tax Commissioner page, wages paid to a mobilized military employee credit. Read for who claims it, the 25% rate, USD 1,000 cap and five-year carryforward. Read through Firecrawl after a direct request returned 403. | https://www.tax.nd.gov/wages-paid-mobilized-military-employee-tax-credit | 2026-11-14 |
| N.D.C.C. chapter 57-38. Read for section 57-38-45 (penalties, interest, good-cause waiver). | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-14 |

Not yet confirmed: the 2026 Form ND-1 and Schedule ND-1NR line numbers and any 2026 change to the 7-month rule or the USD 5.00 reciprocity refund threshold (the 2025 booklet is used, labelled 2025-2026 filing cycle); the text of the Minnesota and Montana reciprocity agreements and their statutory cites; the statutory text of the mobile workforce exemption.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-cross-border-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-cross-border-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
