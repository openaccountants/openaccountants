---
name: us-equity-compensation-restricted-stock-units-and
description: How US employers and their advisers withhold and report federal tax on restricted stock units and stock options, and how the section 83(i) deferral election works for qualified equity grants.
jurisdiction: US
tax_year: 2026
last_updated: 2026-10-03
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equity compensation: RSUs, stock options, supplemental wage withholding and the section 83(i) deferral election in United States

This Guide covers the federal tax on equity pay for employees and founders, and the payroll side for the employer: restricted stock and the section 83(b) election, restricted stock units (RSUs), nonstatutory stock options (NSOs), incentive stock options (ISOs) and the alternative minimum tax (AMT), the flat-rate withholding on supplemental wages, the cost basis trap on Form 1099-B, and the section 83(i) deferral election for private companies. Figures are for tax year 2026. Federal rules only; state tax is not covered. The 2026 figures come from Publication 15 (2026), Publication 15-B (2026) and Rev. Proc. 2025-32. The statute is read on the LII mirror of the U.S. Code (law.cornell.edu) as amended by Public Law 119-21 (the One Big Beautiful Bill Act, 4 July 2025). Some IRS method pages read on 3 October 2026 were still the 2025 editions (Publication 525, Instructions for Form 6251 and Form 8949); this Guide says so where it relies on them, and their rules, not their line numbers, are what it uses. Worked examples use hypothetical amounts and are labelled as such.

Related Guides: sale of the shares and the capital gain rates are in `us-capital-gains`; the section 1202 exclusion for founders' stock is in `us-section-1202-qsbs`; the employer's Form 941 and Form 940 filings are in `us-form-941-940-payroll`; the wider 2026 changes are in `us-2026-federal-tax-changes`.

## Who this is for

- Employees and founders who hold restricted stock, RSUs, NSOs or ISOs, and their advisers.
- Employers, and their payroll and tax agents, that transfer stock to employees for services, or settle RSUs or options in stock. They operate the chapter 24 income tax withholding and report on Form W-2 and Form 941.
- The section 83(i) part applies only where the corporation is an eligible corporation and the individual is a qualified employee (eligible corporation: Publication 15-B table and step 12; excluded employee: the section 83 table).
- Not for non-employee service providers, partners, or equity in a partnership or LLC. Not for state withholding.

## Rates, thresholds and deadlines

### Supplemental wage withholding and employment taxes, 2026

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/publications/p15 |
| Optional flat income tax withholding rate on supplemental wages, 2026, while the employee's supplemental wages from you in the calendar year are not more than USD 1 million | 22% | "Withhold a flat 22% (no other percentage allowed)." Allowed only if you withheld income tax from the employee's regular wages in the current or immediately preceding calendar year. |
| Mandatory rate on supplemental wages above the calendar-year threshold, 2026 | 37% | "the excess is subject to withholding at 37% (or the highest rate of income tax for the year). Withhold using the 37% rate without regard to the employee's Form W-4." |
| Calendar-year supplemental wage threshold for the mandatory rate | USD 1 million | "Special rules apply to the extent supplemental wages paid to any one employee during the calendar year exceed $1 million." Payments from all businesses under common control count. |
| Social security wage base limit, 2026 | USD 184,500 | "The social security wage base limit is $184,500." |
| Medicare tax rate, 2026, each for employee and employer, no wage base limit | 1.45% | "The Medicare tax rate is 1.45% each for the employee and employer" |
| Additional Medicare Tax withholding rate, employee only | 0.9% | "you must withhold a 0.9% Additional Medicare Tax from wages you pay to an employee in excess of $200,000 in a calendar year" |
| Additional Medicare Tax withholding threshold, per employee per calendar year | USD 200,000 | same sentence; "There is no employer share of Additional Medicare Tax." |

The rate column above applies by calendar year and per employee. Only the part of the supplemental wages above USD 1 million is withheld at the mandatory rate; the part up to that amount follows the ordinary supplemental wage rules: either the optional flat rate (only if income tax was withheld from the employee's regular wages in the current or immediately preceding calendar year) or aggregation with regular wages for the payroll period. Publication 15-T (2026) says its own withholding methods "can't be used if the 37% mandatory flat rate withholding applies or if the 22% optional flat rate withholding is used" (https://www.irs.gov/publications/p15t).

### Alternative minimum tax figures, 2026

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
| AMT exemption, 2026, unmarried individuals (other than surviving spouses) | USD 90,100 | "Unmarried Individuals (other than Surviving Spouses) $90,100" |
| AMT exemption, 2026, joint returns or surviving spouses | USD 140,200 | "Joint Returns or Surviving Spouses $140,200" |
| AMT exemption, 2026, married filing separately | USD 70,100 | "Married Individuals Filing Separate Returns $70,100" |
| Exemption phase-out threshold, 2026, unmarried individuals | USD 500,000 | "Unmarried Individuals (other than $500,000 $680,200 Surviving Spouses)" |
| Exemption fully phased out, 2026, unmarried individuals | USD 680,200 | same row |
| Exemption phase-out threshold, 2026, joint returns or surviving spouses | USD 1,000,000 | "Joint Returns or Surviving Spouses $1,000,000 $1,280,400" |
| Exemption fully phased out, 2026, joint returns or surviving spouses | USD 1,280,400 | same row |
| Exemption phase-out threshold, 2026, married filing separately (same number as unmarried) | USD 500,000 | "Married Individuals Filing Separate $500,000 $640,200 Returns" |
| Exemption fully phased out, 2026, married filing separately | USD 640,200 | same row |
| Excess taxable income above which the 28% AMT rate applies, 2026, all taxpayers other than married filing separately | USD 244,500 | "All Other Taxpayers $244,500" |
| Same, married filing separately, 2026 | USD 122,250 | "Married Individuals Filing Separate Returns $122,250" |

### AMT rates and the 2026 phase-out rate in the statute

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.law.cornell.edu/uscode/text/26/55 |
| AMT rate on the taxable excess up to the 28% threshold in the table above (individuals) | 26% | Section 55(b)(1)(A), LII mirror of the U.S. Code: "26 percent of so much of the taxable excess as does not exceed" the threshold |
| AMT rate on the taxable excess above that threshold | 28% | "28 percent of so much of the taxable excess as exceeds" the threshold |
| Exemption phase-out rate for taxable years beginning after 31 December 2025 | 50% | Section 55(d)(4)(A)(ii)(IV): "by substituting "50 percent" for "25 percent"". The exemption is reduced, but not below zero, by this share of the alternative minimum taxable income above the threshold. |

### Public Law 119-21 (OBBBA): the AMT change and its start date

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm |
| Phase-out rate substituted by section 70107(c) of the Act | 50% | "by substituting `50 percent' for `25 percent'"; section 70107(d): "The amendments made by this section shall apply to taxable years beginning after December 31, 2025." |

Section 70107 also removed the end date of the higher exemption amounts, and changed the inflation indexing of the USD 1,000,000 joint threshold so that it is indexed only for taxable years beginning after 2026, with 2025 as the base year. For 2026 the exemption therefore shrinks twice as fast above the threshold as it did under the 25 percent rate. An ISO exercise that did not trigger AMT in 2025 can trigger it in 2026 at the same spread. The 2026 thresholds are in the Rev. Proc. table above.

### Incentive stock options: the statutory limits

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.law.cornell.edu/uscode/text/26/422 |
| Annual limit on ISOs first exercisable, by value at grant, per individual per calendar year, all plans of the employer group | USD 100,000 | Section 422(d)(1), LII mirror of the U.S. Code: "exceeds $100,000, such options shall be treated as options which are not incentive stock options". Options are taken in the order granted (422(d)(2)); value is fixed at grant (422(d)(3)). |
| Holding periods (no figure) | 2 years from grant and also 1 year after transfer of the share | Section 422(a)(1): "no disposition of such share is made by him within 2 years from the date of the granting of the option nor within 1 year after the transfer of such share to him" |
| Employment condition (no figure) | employee from grant until 3 months before exercise | Section 422(a)(2) |

### Election deadlines and the deferral period under section 83

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.law.cornell.edu/uscode/text/26/83 |
| Section 83(b) election deadline | not later than 30 days after the date of the transfer | Section 83(b)(2), LII mirror of the U.S. Code: the election "shall be made not later than 30 days after the date of such transfer. Such election may not be revoked except with the consent of the Secretary." |
| Section 83(i) election deadline | no later than 30 days after the first date the rights in the stock are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier | Section 83(i)(4)(A): made "in a manner similar to the manner in which an election is made under subsection (b)". |
| Maximum deferral under section 83(i) | 5 years after the first date the rights in the stock are transferable or not subject to a substantial risk of forfeiture, whichever is earlier | One of the events in section 83(i)(1)(B); income falls in the taxable year that includes the earliest event. |
| Other events that end the deferral | the first date the stock becomes transferable (including to the employer); the date the employee first becomes an excluded employee; the first date any stock of the issuing corporation becomes readily tradable on an established securities market; the date the employee revokes the election | Section 83(i)(1)(B). |
| Excluded employee: ownership test | a 1-percent owner (section 416(i)(1)(B)(ii)) at any time during the calendar year, or at any time during the 10 preceding calendar years | Section 83(i)(3)(B)(i). |
| Excluded employee: chief executive or chief financial officer | anyone who "is or has been at any prior time" the CEO or CFO, or acting in that capacity | Section 83(i)(3)(B)(ii). No look-back limit. |
| Excluded employee: family | anyone with a section 318(a)(1) family relationship to a person in the CEO or CFO test | Section 83(i)(3)(B)(iii). |
| Excluded employee: officer test | one of the 4 highest compensated officers for the taxable year, or for any of the 10 preceding taxable years | Section 83(i)(3)(B)(iv). |
| Stock redemption limit | no election if the corporation bought any of its outstanding stock in the preceding calendar year, unless not less than 25 percent of the total dollar amount bought is deferral stock and the sellers were chosen on a reasonable basis | Section 83(i)(4)(B)(iii). |

### Section 83(i) and the employer: Publication 15-B (2026)

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/publications/p15b |
| Written plan coverage needed for an eligible corporation | 80% | "not less than 80% of all U.S. employees are granted options or RSUs with the same rights and privileges to receive qualified stock" |
| Income tax withholding rate when deferred income is included | 37% | "the employer must withhold federal income tax at 37% in the tax year that the amount deferred is included in the employee's income" |

### Section 83(i) administration: Notice 2018-97

| What | Value | Note |
|---|---|---|
| Source | all figures below | https://www.irs.gov/pub/irs-drop/n-18-97.pdf |
| Provision containing the 80% requirement | section 83(i)(2)(C)(i)(II) | The notice addresses "the 80% requirement of section 83(i)(2)(C)(i)(II)". |
| Employer recovery of income tax withholding it paid from its own funds on deferral stock | before April 1 of the year after the year of inclusion | "the employer may recover the income tax from the employee prior to April 1 of the year following the year in which the inclusion in wages under section 3401(i) occurs" |
| Good faith transition rule for the 80% requirement and the section 83(i)(6) notice | a reasonable good faith interpretation counts as compliance until regulations or other guidance are issued | as described in the notice |
| Amount included when the deferral ends | the value at the vesting date, even if the stock has since fallen | "the amount of income recognized at the end of the deferral period will be based on the value of the stock at the time at which the rights of the employee first become transferable or not subject to a risk of forfeiture, notwithstanding whether the value of the stock has declined during the deferral period" |

## How each type of award is taxed

### Restricted stock (actual shares, subject to vesting)

- Default rule, any year: under section 83(a) the employee includes the value of the shares, less any amount paid, in the first taxable year the shares are transferable or not subject to a substantial risk of forfeiture, whichever occurs earlier (https://www.law.cornell.edu/uscode/text/26/83). This is wages. The Treasury regulation lists "wage income recognized on the lapse of a restriction on restricted property transferred from an employer to an employee" as supplemental wages (https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1).
- Section 83(b) election: the employee may instead include the value at the date of transfer, less the amount paid, in the year of transfer. The deadline is in the section 83 table above. If made, later growth is not compensation when the shares vest, and if the shares are later forfeited "no deduction shall be allowed in respect of such forfeiture" (section 83(b)(1)). Publication 525 (2025) says the election is made by a written statement or Form 15620 filed with the IRS service center where the return is filed, with a copy to the employer, and that it cannot be made for a statutory or nonstatutory stock option (https://www.irs.gov/publications/p525).
- Dividends on restricted stock with no 83(b) election are compensation, not dividends; with the election they are dividends (Publication 525 (2025)).

### Restricted stock units (RSUs)

- An RSU is a promise to deliver shares (or cash) later. For section 83 the term property excludes "an unfunded and unsecured promise to pay money or property in the future" (26 CFR 1.83-3(e), https://www.ecfr.gov/current/title-26/section-1.83-3). So nothing is transferred at grant, and there is no section 83(b) election for an RSU. This is our reading of the regulation; the accountant should confirm it for any RSU that is funded or secured.
- When the RSU settles in shares, Notice 2018-97 describes the income "that would otherwise be included under section 83(a) upon the transfer of stock pursuant to the exercise of a stock option or the settlement of a restricted stock unit (RSU)" (Notice 2018-97, https://www.irs.gov/pub/irs-drop/n-18-97.pdf). The value of the shares at settlement is wages and is not regular wages (our reading of the regulation's general definition), so the employer withholds under the supplemental wage rules in the first table.
- Social security and Medicare tax apply to the same wages, subject to the wage base in the first table. This Guide does not cover the social security and Medicare timing of RSUs that settle after vesting (see When to refuse or refer).

### Nonstatutory stock options (NSOs)

- Grant, any year: no income at grant unless the option has a readily determinable fair market value; most do not, because an option not traded on an established market qualifies only if it is transferable, immediately exercisable in full, free of significant restrictions, and its option privilege can be readily valued (Publication 525 (2025) at https://www.irs.gov/publications/p525 and Topic 427 at https://www.irs.gov/taxtopics/tc427).
- Exercise: for an option without a readily determinable value, the spread (value of the shares at exercise less the price paid) is compensation at exercise, or later at vesting if the shares received are still substantially nonvested (Publication 525 (2025)).
- The spread is supplemental wages: the regulation lists "income recognized on the exercise of a nonstatutory stock option" (https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1). The employer reports it in Form W-2 boxes 1, 3 (up to the social security wage base) and 5, and in box 12 with code V (Publication 15-B (2026), https://www.irs.gov/publications/p15b).

### Incentive stock options (ISOs)

- Regular tax, any year: no income at grant or at exercise (Publication 525 (2025); Topic 427).
- Social security, Medicare and FUTA: wages for these taxes "don't include remuneration resulting from the exercise of an incentive stock option or an employee stock purchase plan option, or from any disposition of stock acquired by exercising such an option" (Publication 15-B (2026), https://www.irs.gov/publications/p15b).
- AMT: section 56(b)(3) switches off section 421 for the AMT, so the spread is an adjustment in alternative minimum taxable income (https://www.law.cornell.edu/uscode/text/26/56). The Instructions for Form 6251 (2025) measure it as the value of the stock when the rights first become transferable or no longer subject to a substantial risk of forfeiture, less the amount paid, that is measured at vesting for shares that are still unvested at exercise, unless the holder elects within 30 days of the transfer to take the adjustment at exercise: "Even if your rights in the stock aren't transferable and are subject to a substantial risk of forfeiture, you may elect to include in AMT income the excess of the stock's FMV (determined without regard to any lapse restriction) over the exercise price upon the transfer to you of the stock acquired through exercise of the option. You must make the election by the 30th day after the date of the transfer." (https://www.irs.gov/instructions/i6251), and say: "If you acquired stock by exercising an ISO and you disposed of that stock in the same year, the tax treatment under the regular tax and the AMT is the same, and no adjustment is required." (https://www.irs.gov/instructions/i6251). The 2025 form reports it on line 2i; check the 2026 form for the line.
- AMT basis: increase the AMT basis of the shares by the adjustment, and keep separate regular tax and AMT basis records (Instructions for Form 6251 (2025)).
- Qualifying disposition: if the shares are held past both holding periods in the ISO table, the whole gain over the price paid is capital gain (Publication 525 (2025)); for rates see `us-capital-gains`.
- Disqualifying disposition: if either holding period is missed, the gain is ordinary income up to the spread at exercise, and any further gain is capital gain. Where the disqualifying disposition is a sale or exchange "with respect to which a loss (if sustained) would be recognized" (section 422(c)(2), https://www.law.cornell.edu/uscode/text/26/422), the ordinary income "shall not exceed the excess (if any) of the amount realized on such sale or exchange over the adjusted basis" of the share. So a sale at arm's length below the value at exercise caps the ordinary income at the actual gain; a sale to a related person or a wash sale does not. Publication 525 (2025) states the general rule only ("This ordinary income isn't limited to your gain from the sale of the stock."); the statute carries the cap. The employer reports the spread in Form W-2 box 1, but income tax withholding "isn't required" on it, and it is not wages for social security, Medicare or FUTA (Publication 15-B (2026)).
- The USD 100,000 first-exercisable limit in the ISO table turns the excess into NSOs, by value at grant, in grant order.

### Basis on Form 1099-B (all award types)

- For compensatory options granted after 2013, the broker's basis on Form 1099-B "won't reflect any amount you included in income upon grant or exercise of the option. Increase your basis by any amount you included in income" (Instructions for Form 8949 (2025), https://www.irs.gov/instructions/i8949).
- Shares delivered on an RSU settlement (vested when acquired): basis reflects any amount paid and any amount included in the employee's income (26 CFR 1.61-2(d)(2)(i), https://www.ecfr.gov/current/title-26/section-1.61-2), which says "its basis shall be the amount paid for the property increased by the amount of such difference included in gross income". Restricted stock is acquired while still substantially nonvested; its basis follows the same rule in 26 CFR 1.83-4(b)(1) (https://www.ecfr.gov/current/title-26/section-1.83-4), whether or not an 83(b) election was made.
- Where the Form 1099-B basis is wrong, enter code B in column (f) of Form 8949 and the adjustment in column (g), or the correct basis in column (e), as the Form 8949 instructions direct for the box checked. Without this the same income is taxed twice, once as wages and once as capital gain.

## The method, step by step

1. Identify each award and its taxable event under section 83: transfer of restricted stock, vesting, RSU settlement, or option exercise (https://www.law.cornell.edu/uscode/text/26/83). Ask whether the option is an ISO under section 422(b) or an NSO; an option that fails the ISO rules, or that exceeds the 422(d) limit, is an NSO (https://www.law.cornell.edu/uscode/text/26/422).
2. Restricted stock: decide on the section 83(b) election within 30 days of the transfer, measured from the transfer date in the section 83 table. File by statement or Form 15620 and give the employer a copy (https://www.irs.gov/publications/p525). Not for options (Publication 525); for RSUs see the reading in the RSU section.
3. RSU settlement and NSO exercise: treat the income as supplemental wages (https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1). Withhold income tax using the first table: the optional flat rate, or aggregation, while the employee's supplemental wages from the employer group in the calendar year stay at or below the threshold; the mandatory rate on the excess above it, whatever the Form W-4 says (https://www.irs.gov/publications/p15).
4. Apply social security tax up to the 2026 wage base, Medicare tax on all of it, and Additional Medicare Tax withholding once the employee's wages from you pass the threshold in the first table (https://www.irs.gov/publications/p15). The employer's deposits and Form 941 are in `us-form-941-940-payroll`.
5. Sell-to-cover: where the plan sells or withholds shares to fund the withholding, the shares sold are still part of the wages; the employee's basis in the shares sold equals their value at settlement, so that sale shows little or no gain once basis is corrected (26 CFR 1.61-2(d)(2)(i), https://www.ecfr.gov/current/title-26/section-1.61-2).
6. Test the employee's own position: compare the flat-rate withholding with the employee's marginal rate for 2026 (single brackets in Rev. Proc. 2025-32, https://www.irs.gov/pub/irs-drop/rp-25-32.pdf). A large RSU vest withheld at the optional flat rate can leave tax unpaid for an employee in a higher band. Worked example 2 shows the size of the gap.
7. ISO exercise: before exercising, compute the AMT for 2026 using the exemption, phase-out and rate tables above and Form 6251 (https://www.irs.gov/instructions/i6251). Remember the 2026 phase-out rate from Public Law 119-21 (https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm). Worked example 1 shows how fast the exemption disappears.
8. ISO exercise: keep the Form 3921 the corporation must file and furnish for each transfer of a share on an ISO exercise (https://www.irs.gov/instructions/i3921). It gives the grant date, exercise date, price and value needed for the AMT adjustment and the holding periods. Form 3922 does the same for ESPP shares in the cases its instructions list.
9. AMT credit: AMT paid because of an ISO adjustment (a timing item) becomes a minimum tax credit for later years under section 53, usable only to the extent regular tax exceeds the tentative minimum tax in that later year (section 53(c), https://www.law.cornell.edu/uscode/text/26/53). Claim it on Form 8801 (https://www.irs.gov/instructions/i6251). AMT caused by exclusion items, such as the standard deduction add-back, does not create credit (section 53(d)(1)(B)).
10. ISO sale: test both holding periods (2 years from grant and also 1 year after transfer; section 422(a)(1), https://www.law.cornell.edu/uscode/text/26/422). A sale in the same calendar year as exercise is a disqualifying disposition and also removes the AMT adjustment for that year (https://www.irs.gov/instructions/i6251).
11. Any sale: correct the Form 1099-B basis on Form 8949 with code B as described above (https://www.irs.gov/instructions/i8949). Capital gain rates and holding period tests are in `us-capital-gains`; founders' stock that may qualify under section 1202 is in `us-section-1202-qsbs`.
12. Section 83(i), private companies only: test the corporation (no stock readily tradable on an established securities market during any preceding calendar year; written plan covering not less than 80 percent of U.S. employees with the same rights and privileges; the redemption limit) and the employee (not an excluded employee under any of the four tests in the section 83 table) (https://www.law.cornell.edu/uscode/text/26/83). Qualified stock comes only from an option exercise or RSU settlement, never from a restricted stock award, and not where the employee may take cash instead (https://www.irs.gov/publications/p525).
13. Section 83(i): the corporation gives the section 83(i)(6) notice (https://www.irs.gov/pub/irs-drop/n-18-97.pdf). The employee elects within 30 days, under Notice 2018-97, not on Form 15620 (https://www.irs.gov/publications/p525). No election is possible if the employee made a section 83(b) election for the same stock, or if any stock of the corporation is readily tradable at any time before the election is made (section 83(i)(4)(B)). An 83(i) election on an option exercise means the option is no longer treated as an ISO (https://www.irs.gov/publications/p15b).
14. Section 83(i) payroll: the election defers income tax only. It "has no effect on the application of social security, Medicare, and FUTA taxes" (https://www.irs.gov/publications/p15b). When the deferral ends, include the amount in wages, withhold income tax at the rate in the Publication 15-B table, and report it in Form W-2 box 12 with code GG; report the total deferred at year end with code HH. Recover withholding paid from the employer's own funds before the date in the Notice 2018-97 table (https://www.irs.gov/pub/irs-drop/n-18-97.pdf).
15. Where the official pages are silent, say so rather than fill the gap: none of the pages read here gives a valuation method for private company stock, and this Guide states none.

## Worked examples (hypothetical amounts)

### Example 1: an ISO exercise that creates AMT in 2026

A single filer with no other income or deductions. Rates and thresholds are the 2026 figures from Rev. Proc. 2025-32. The shares are vested at exercise, so the adjustment is measured at exercise; for early-exercised unvested shares see the ISO section above.

| Source | all figures below | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
|---|---|---|
| Step | Amount | Note |
| Wages for 2026 (hypothetical) | USD 200,000 | regular salary |
| Standard deduction, single, 2026 | USD 16,100 | "Unmarried Individuals (other than Surviving Spouses and Heads of $16,100" |
| Taxable income | USD 183,900 | USD 200,000 minus USD 16,100 |
| Regular tax, single 2026 table: base for taxable income over USD 105,700 | USD 17,966 | "$17,966 plus 24% of the excess over $105,700" |
| Plus 24% of the excess over USD 105,700 (USD 78,200) | USD 18,768 | |
| Regular tax | USD 36,734 | USD 17,966 plus USD 18,768 |
| ISO exercised in 2026 on vested shares: 10,000 shares at USD 5 when the value is USD 45 (hypothetical) | USD 400,000 | AMT adjustment: 10,000 times USD 40 spread; cash paid USD 50,000; no regular tax income |
| Alternative minimum taxable income | USD 600,000 | USD 183,900 plus the USD 16,100 standard deduction added back plus USD 400,000 |
| Exemption before phase-out, single | USD 90,100 | |
| Phase-out: 50% of the excess of USD 600,000 over USD 500,000 | USD 50,000 | phase-out rate from section 55(d)(4)(A)(ii)(IV) |
| Exemption allowed | USD 40,100 | USD 90,100 minus USD 50,000 |
| Taxable excess | USD 559,900 | USD 600,000 minus USD 40,100 |
| 26% of the first USD 244,500 | USD 63,570 | |
| 28% of the remaining USD 315,400 | USD 88,312 | |
| Tentative minimum tax | USD 151,882 | USD 63,570 plus USD 88,312 |
| AMT for 2026 | USD 115,148 | USD 151,882 minus regular tax USD 36,734 |
| Taxable excess without the exercise | USD 109,900 | USD 200,000 minus the full USD 90,100 exemption, no phase-out below the USD 500,000 threshold |
| Tentative minimum tax without the exercise | USD 28,574 | 26% of USD 109,900 |

Without the exercise, alternative minimum taxable income is USD 200,000, the full USD 90,100 exemption applies, and the taxable excess and tentative minimum tax are in the table above. That is below the regular tax of USD 36,734, so no AMT is due. Under section 53(d)(1)(B) the credit is the net minimum tax less the net minimum tax that only the section 56(b)(1) items (here the standard deduction add-back) would produce; that second amount is zero here, so the whole USD 115,148 carries forward (https://www.law.cornell.edu/uscode/text/26/53). It is used only in a year when regular tax exceeds the tentative minimum tax. Selling the shares in 2026 would remove the adjustment, but the sale would be a disqualifying disposition and the spread would be ordinary income for regular tax (https://www.irs.gov/instructions/i6251).

### Example 2: an RSU vest withheld at the flat rate

A single filer. Salary of USD 250,000 has already been paid in 2026 before the vest. 1,000 RSUs settle in shares worth USD 150 each (hypothetical). The employee has received no other supplemental wages this year.

| Source | all figures below | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf |
|---|---|---|
| Step | Amount | Note |
| Salary paid before the vest (hypothetical) | USD 250,000 | already above the social security wage base and the Additional Medicare threshold |
| RSU settlement: 1,000 shares at USD 150 (hypothetical) | USD 150,000 | supplemental wages |
| Income tax withheld at the optional flat 22% | USD 33,000 | first table, Publication 15 (2026) |
| Social security tax on the RSU | USD 0 | wage base already reached |
| Medicare tax, 1.45% | USD 2,175 | employee share |
| Additional Medicare Tax withholding, 0.9% | USD 1,350 | wages already above USD 200,000 |
| Amount funded by sell-to-cover | USD 36,525 | USD 33,000 plus USD 2,175 plus USD 1,350 |
| Taxable income without the RSU | USD 233,900 | USD 250,000 minus the USD 16,100 standard deduction |
| Regular tax on USD 233,900 | USD 51,304 | "$41,024 plus 32% of the excess over $201,775": 32% of USD 32,125 is USD 10,280 |
| Taxable income with the RSU | USD 383,900 | |
| Regular tax on USD 383,900 | USD 103,134.25 | "$58,448 plus 35% of the excess over $256,225": 35% of USD 127,675 is USD 44,686.25 |
| Income tax caused by the RSU | USD 51,830.25 | USD 103,134.25 minus USD 51,304 |
| Shortfall against the flat-rate withholding | USD 18,830.25 | USD 51,830.25 minus USD 33,000 |

The employee should pay the shortfall through estimated tax or a higher Form W-4 amount for the rest of 2026. Each share kept has a basis of USD 150, the amount included in wages (26 CFR 1.61-2(d)(2)(i), https://www.ecfr.gov/current/title-26/section-1.61-2). If the Form 1099-B for a later sale shows a different basis, correct it on Form 8949 with code B (https://www.irs.gov/instructions/i8949).

## Ask the client first

- Is the award restricted stock, an RSU, an NSO, an ISO under section 422(b), or an ESPP right under section 423(c)? If an ISO, what is its grant date and the value of the shares at grant, against the USD 100,000 first-exercisable limit?
- For restricted stock: on what date were the shares transferred, and has a section 83(b) election been filed within 30 days?
- How much supplemental wage has the employee already received this calendar year from the whole employer group, against the USD 1 million threshold, and has income tax been withheld from regular wages this year or last year?
- For an ISO: what is the spread at exercise, what is the rest of the 2026 income, and will the shares be sold in the same calendar year, within 2 years of grant or within 1 year of exercise?
- For section 83(i): is any stock of the corporation readily tradable, did the corporation buy back stock in the preceding calendar year, and has the employee ever been CEO or CFO (no time limit), or a 1-percent owner or one of the 4 highest paid officers in the current year or the 10 preceding years?
- For any sale: what basis does the Form 1099-B show, and was the option granted before or after 2013?

## When to refuse or refer

- State and local income tax on equity pay, including sourcing for employees who moved or worked in more than one state.
- Social security and Medicare tax timing for RSUs or deferred stock units that settle after vesting (section 3121(v)(2)), and section 409A treatment of deferred units and discounted options.
- ISOs granted to a holder of more than 10 percent of the voting power, ISO modifications, and ESPP offerings under section 423 beyond the reporting step in this Guide.
- AMT where the taxpayer also has other preference items, foreign tax credit, or a minimum tax credit already carried forward: run the full Form 6251 and Form 8801.
- The due dates, penalties and electronic filing rules for Forms 3921, 3922 and W-2, none of which are stated in this Guide.
- Equity granted to non-employees, partners, or by a partnership or LLC, and equity granted by a non-US parent.
- Securities law questions, including section 16(b) exposure, beyond the effect section 83(c)(3) gives it.
- Valuation of private company stock, and any case where the fair market value at the taxable event is in dispute.
- Exclusion of gain under section 1202 on stock from options or restricted stock: refer to `us-section-1202-qsbs`.

## Sources

- https://www.irs.gov/publications/p15 (Publication 15 (2026): supplemental wage withholding, social security wage base, Medicare and Additional Medicare Tax)
- https://www.irs.gov/publications/p15t (Publication 15-T (2026): its methods do not apply when the flat rates are used)
- https://www.irs.gov/publications/p15b (Publication 15-B (2026): stock options, FICA exclusion for ISOs, section 83(i) withholding and Form W-2 codes)
- https://www.ecfr.gov/current/title-26/chapter-I/subchapter-C/part-31/subpart-E/section-31.3402%28g%29-1 (26 CFR 31.3402(g)-1: what counts as supplemental wages)
- https://www.irs.gov/pub/irs-drop/rp-25-32.pdf (Rev. Proc. 2025-32: 2026 AMT exemption, phase-out, 28% threshold, brackets, standard deduction)
- https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm (Public Law 119-21, section 70107: AMT phase-out rate from 2026)
- https://www.law.cornell.edu/uscode/text/26/55 (26 U.S.C. 55, LII mirror of the U.S. Code: AMT rates and exemption phase-out)
- https://www.law.cornell.edu/uscode/text/26/56 (26 U.S.C. 56(b)(3), LII mirror: ISO adjustment)
- https://www.law.cornell.edu/uscode/text/26/53 (26 U.S.C. 53, LII mirror: minimum tax credit)
- https://www.law.cornell.edu/uscode/text/26/422 (26 U.S.C. 422, LII mirror: ISO holding periods and the 422(d) limit)
- https://www.law.cornell.edu/uscode/text/26/83 (26 U.S.C. 83, LII mirror: section 83(a), 83(b) and 83(i))
- https://www.ecfr.gov/current/title-26/section-1.83-3 (26 CFR 1.83-3(e): definition of property)
- https://www.ecfr.gov/current/title-26/section-1.83-4 (26 CFR 1.83-4(b): basis)
- https://www.ecfr.gov/current/title-26/section-1.61-2 (26 CFR 1.61-2(d)(2)(i): basis of vested shares)
- https://www.irs.gov/publications/p525 (Publication 525 (2025): options, restricted property, 83(b) and 83(i) procedure)
- https://www.irs.gov/taxtopics/tc427 (Topic 427: stock options)
- https://www.irs.gov/instructions/i6251 (Instructions for Form 6251 (2025): ISO adjustment, Form 8801)
- https://www.irs.gov/instructions/i8949 (Instructions for Form 8949 (2025): basis of compensatory option stock, code B)
- https://www.irs.gov/instructions/i3921 (Instructions for Forms 3921 and 3922)
- https://www.irs.gov/pub/irs-drop/n-18-97.pdf (Notice 2018-97: section 83(i) guidance)

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
