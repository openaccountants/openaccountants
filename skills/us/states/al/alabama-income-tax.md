---
name: alabama-income-tax
description: "Alabama Form 40 (full-year resident): how I do it"
jurisdiction: US-AL
tax_year: 2026
tax_year_notes: "Covers the 2025-2026 filing cycle: tax year 2025 figures (2025 Form 40 booklet) for returns filed in 2026, plus the 2026 estimated-tax dates and the 2026 overtime premium deduction where stated."
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: filing-howto
version: 0.7
---

# Alabama Income Tax

Alabama Form 40 (full-year resident): how I do it

Includes self-employed individuals and sole proprietors. See also: `alabama-cross-border`, `al-payroll-withholding`.

**Coverage period.** This tax-year-2026 snapshot retains the verified **2025-2026 filing cycle** amounts and 2025 Form 40 line mappings below. Those filing thresholds, deductions and exemptions are not represented as published 2026 return amounts. The 2026 estimated-tax schedule and overtime rule are separately dated. Do not prepare a 2026 final return by silently relabelling the 2025 charts.

Form 40 is the Alabama individual income tax return for someone who was a legal resident of Alabama for the entire tax year. A resident reports income from all sources, wherever earned, unless Alabama specifically exempts it. This Guide uses calendar 2025; income otherwise follows the federal taxable year and accounting method (§40-18-13). Filing is due with the corresponding federal return (§40-18-27(c)).

## Who this applies to

Full-year Alabama residents. You must use Form 40 if you're a full-year resident who itemizes, or who doesn't meet every condition for the short Form 40A.

You may use Form 40A instead only if all of these hold: full-year resident, not itemizing, no adjustments to income (no IRA deduction, alimony paid, or prior-year federal tax), no income other than salaries and wages except interest and dividends not exceeding $1,500, no business income or loss from federal Schedules C, D, E or F, and not claiming credit for taxes paid to another state (2025 Form 40 booklet, p.5).

This guide does not cover part-year residents or nonresidents. Those are a different return and a different allocation, and a part-year resident who also had Alabama-source income while a nonresident may need both Form 40 and Form 40NR. Send elsewhere: multi-state residency disputes, foreign income and treaty positions, and anyone with an open Alabama audit or collections matter.

Before you start, ask the client: Were you a legal resident of Alabama for the whole of the year, and did you move at any point? Filing status at December 31, and your spouse's residency. Alabama is not a community property state, and you cannot file a joint Alabama return if you are a resident and your spouse is a resident of another state; that is married filing separate (2025 Form 40 booklet: "NOTE: Alabama is not a community property state"). Any income taxed by another state, or by a foreign country? Any income not on a W-2 or 1099: rents, royalties, gains on sales of property, K-1s, farm? Any Alabama estimated payments or an extension payment, and how much? Any out-of-state purchases on which no sales tax was collected?

## Rates, bands and thresholds

| Item | Value | Source |
|---|---|---|
| Rate schedule, single / head of family / married filing separate | 2% on the first $500 of taxable income; 4% on the next $2,500; 5% on all over $3,000 | [§40-18-5](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-5); [ADOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| Rate schedule, married filing joint | 2% on the first $1,000; 4% on the next $5,000; 5% on all over $6,000 | [§40-18-5](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-5); [ADOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| 2025 full-year resident gross-income filing chart | ADOR says file at least: single $4,500; head of family $8,200; married filing joint $11,500; married filing separate $5,750. These equal maximum standard deduction plus personal exemption; §40-18-27(a) says gross income exceeding the allowable sum. Follow the published chart at equality rather than use the statutory wording to skip filing | [§40-18-27(a)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-27); [2025 booklet p.5](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Personal exemption (line 13) | Single $1,500; married filing joint $3,000; married filing separate $1,500; head of family $3,000 | [§40-18-19(a)(8)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-19); [2025 Form 40](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40.pdf) |
| Personal exemption, single dependent or student | $1,500, even if claimed by another taxpayer; otherwise use the filing-status amount above | [2025 Form 40 booklet, p.5](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Dependent exemption (line 14), per dependent, by Alabama AGI (line 10) | $50,000 or less: $1,000; over $50,000 through $100,000: $500; over $100,000: $300 | [§40-18-19(a)(9)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-19); [booklet p.10](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Standard deduction, married filing joint | $8,500 at Alabama AGI $0 to $25,999, stepping down in bands to $5,000 at $35,500 and above | [§40-18-15(b)(4)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15); [booklet p.9 chart](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Standard deduction, married filing separate | $4,250 at $0 to $12,999, stepping down to $2,500 at $17,750 and above | [§40-18-15(b)(4)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15); [booklet p.9 chart](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Standard deduction, head of family | $5,200 at $0 to $25,999, stepping down to $2,500 at $35,500 and above | [§40-18-15(b)(4)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15); [booklet p.9 chart](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Standard deduction, single | $3,000 at $0 to $25,999, stepping down to $2,500 at $35,500 and above | [§40-18-15(b)(4)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15); [booklet p.9 chart](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Schedule B trigger | Taxable and nontaxable interest and dividends of $1,500 or more | [2025 Form 40 booklet, p.8](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Alabama ABLE contribution deduction | Up to $5,000 per individual per year, regardless of itemizing; no second deduction for already-deducted rollovers; nonqualified withdrawals add back the withdrawal plus 10%; unavailable for tax years beginning after December 31, 2030 | [§40-18-15.8](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15.8); [booklet p.17](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Qualified overtime, calendar 2026 through 2028 (Act 2026-604) | Lesser of qualified compensation and $1,000 per taxpayer, whether itemizing or not; the amount must be defined and calculated under federal §225. Only required FLSA overtime above the regular rate qualifies; see the boundary below before computing | [§40-18-15(a)(29)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15); [§225](https://uscode.house.gov/us/usc/t26/s225/); [ADOR](https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/) |

## The taxable base

The method, step by step:

1. Finish the federal return first. The Alabama return depends on it in two directions: figures flow up from it, and the federal income tax deduction on line 12 depends on the federal liability. Working Alabama before the federal return is settled means reworking it.
2. Confirm full-year residency before you touch a number. If the client moved during the year, stop the full-year computation and use the part-year/40NR boundary below.
3. Set filing status and personal exemption on lines 1 to 4, carrying the exemption to line 13. Head of family requires being unmarried or legally separated at year end, not a surviving spouse, and no foster-child qualification. Pay more than half the cost of a home for the entire year for a dependent parent (who need not live with you), or a home shared for more than six months (including temporary absences) with an unmarried child/descendant, adopted child or stepchild (need not be dependent), a married such child who is dependent (the booklet has a divorced-parent exception), or another qualifying dependent relative. For birth/death during the year, use the part of the year alive. Attach Schedule HOF (booklet pp.6-7,33).
4. Build income, lines 5 to 8. Report all W-2 information on Schedule W-2. If the client earned wages in more than one state, include the total state wages from all states. If taxable and nontaxable interest and dividends are $1,500 or more, complete Schedule B. Other income (rents, royalties, gains, anything not in the state wages box) goes on line 7 with page 2, Part I and the supporting federal schedules attached. Federal Social Security benefits are on the booklet's list of income Alabama does not tax.
5. Watch what is not Alabama withholding. Do not treat federal income tax, FICA, local or occupational tax, or tax paid to another state as Alabama tax withheld. This is a common source of notices.
6. Take adjustments on line 9, then compute Alabama adjusted gross income on line 10.
7. Choose itemized or standard on line 11, and compute it both ways. Check box a and attach Schedule A to itemize; check box b for the standard deduction and use the chart, which is keyed to Alabama AGI on line 10, not federal AGI. The federal choice does not control Alabama. If you take the standard deduction and later want to itemize, you can amend. A dependent or student may take the standard deduction even if claimed by someone else. Married separate spouses must both use standard or both itemize unless they lived apart all year; neither deducts the other’s expenses (§40-18-15(d); booklet p.8).
8. Compute the federal income tax deduction on line 12 from the booklet p.31 worksheet: federal Form 1040 line 22 plus Form 8960 line 17, less the worksheet's refundable credits (EIC, additional child tax credit, refundable American Opportunity and adoption credits, and Form 2439 credit), floored at zero. This is not withholding or total federal tax including self-employment tax. Attach federal pages 1 and 2 and Schedule 1 if applicable. For a joint federal return and separate Alabama returns, allocate federal liability using **each spouse's federal AGI / joint federal AGI**, not the spouse's Alabama AGI (booklet p.8). Paid/accrued wording in §40-18-15(c) follows the taxpayer's proper federal accounting method under §40-18-13; it is not a free annual timing election. A prior-year federal-tax adjustment needs its own substantiation and return-year instructions.
9. Apply the personal exemption (line 13) and dependent exemption (line 14). The dependent exemption is per dependent and steps down with Alabama AGI. A dependent must be a relative listed in §40-18-19(a)(9) receiving over 50% of support from the taxpayer (either spouse on a joint return). Foster children, friends, cousins, self and spouse do not qualify; use actual support records, excluding a student child’s scholarships (booklet pp.8,10). Complete Schedule DS and attach it before filling page 2, Part III.
10. Add lines 11 to 14 for total deductions (line 15) and subtract them from line 10 for taxable income (line 16). Figure the tax on line 17 from the Tax Table, using the filing status you checked. If there's a net operating loss carryover or carryback, you cannot use the table: indicate the method and attach Form NOL-85A (2025 Form 40, lines 15 to 17).
11. Compute credits through Schedule OC and check its box at line 18. For another state or US territory, complete Schedule CR, attach the other return (or W-2G if that state permits no gambling return), and carry the credit to OC. The same income must be taxed in both jurisdictions for the same period. No credit if a corresponding deduction fully offsets it. Under §40-18-21(a), limit to actual other-state tax and Alabama tax on the same taxable income, **and** to Alabama precredit liability × (Alabama AGI attributable to states/territories where tax was paid / total Alabama AGI). Do not include untaxed states in that numerator. The booklet p.22 example explains adjusting the common income for Alabama-allowed expenses. Foreign tax is not Schedule CR; see the separate boundary below.
12. Pick up additional taxes on Schedule ATP, including consumer use tax on out-of-state purchases. If there were no such purchases, enter zero and check the box on ATP Part I line 1; still consider the other ATP taxes.
13. Reconcile payments before you sign: Alabama withholding per Schedule W-2, estimated payments per the client's records and the state account, any extension payment on Form 40V, and any prior-year overpayment applied forward. Use line 22 for withholding and line 23 for estimates/extension payments; match applied prior-year credits to the account. Exclude a prior-year balance paid this year and refunded overpayments. These must tie.
14. File electronically and keep the acknowledgment. Direct deposit is not available on a blank paper Form 40, and refunds cannot be deposited to or through a foreign financial institution; those get a paper check.

Use the [2025 Form 40 and booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), not an assumed federal-AGI starting box: Alabama separately totals its income and adjustments. On the form, credits reduce line 17 to line 18; ATP goes to line 19; total tax/contributions are line 21; payments total line 27 and adjusted payments line 29; balance due is line 30 and refund line 35. Complete page 2 Part IV, sign/validate (both spouses for joint returns), and retain the return and acknowledgment.

Alabama-exempt income in the booklet's list includes federal Social Security and Railroad Retirement benefits, military retirement pay, unemployment compensation, state income tax refunds, and interest on obligations of Alabama and its subdivisions and of the United States (2025 Form 40 booklet, p.7). Interest on other states' obligations is taxable (booklet, Schedule B instructions pp.21-22).

For self-employment, attach federal Schedule C, adjusting for Alabama differences, and carry net profit/loss to page 2 Part I line 2. Ordinary necessary trade/business expenses follow §40-18-15(a)(1); personal expenses do not become deductible by being on Schedule C. The booklet p.13 specifically says Alabama has no counterpart to the federal limit on otherwise deductible office/home expense: do not automatically copy the federal limited amount. Business-versus-hobby classification, mixed personal/business use and depreciation/depletion adjustments must be resolved before using net profit.

Qualified IRA and pension/SEP deductions rest on §40-18-15(a)(11)-(12), not blanket AGI conformity. Page 2 Part II line 1 uses the federal IRA limitation with Alabama AGI before the IRA deduction; line 2 covers Keogh/SEP contributions. A solo-401(k) needs the correct employee/employer component and state treatment established rather than being copied twice. Self-employed health insurance on Part II line 7 is deductible to the federal extent (booklet p.16). For a disputed home-office/business classification, solo-401(k) allocation or specific §199A/QBI treatment, no deduction outcome is supplied here. Check this point with one of our partner accountants. A change to federal liability must in all events feed the line-12 worksheet.

**2026 overtime boundary.** Alabama's own §40-18-15(a)(29), enacted by Act 2026-604 §1 (effective October 1, 2026), expressly covers 2026 through 2028; it is not inferred from federal conformity and does not alter this Guide's 2025 return figures. Obtain the premium separately (ADOR identifies W-2 box 12 code TT). Section 225 defines qualifying overtime as the FLSA-required excess over the regular rate and excludes qualified tips. Its federal deduction also has MAGI, valid-SSN and married-joint-return conditions. For Alabama application of those conditions, especially high-income or separate-return cases, the $1,000 headline alone does not establish an allowable amount; no computed state deduction for those cases is supplied here. Check this point with one of our partner accountants. Do not invent a 2026 final-return line from the 2025 form.

## Deadlines and filing

| Item | Value | Source |
|---|---|---|
| Filing deadline | Same date as the federal return: "no later than the due date of the federal return" | [2025 Form 40 booklet, p.5](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Automatic extension | "You will automatically be granted an extension until October 15, 2026"; pay with Form 40V, "Automatic Extension Payment" box checked, by the federal due date. Time to file only, not time to pay | [2025 Form 40 booklet, p.5, p.18](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Refund claim window, general rule | Later of three years from filing or two years from payment; if no return was timely filed, two years from payment. Withholding and estimates are deemed paid on the original return due date; special NOL rules need separate review | [§40-2A-7(c)(2)](https://alison.legislature.state.al.us/code-of-alabama?section=40-2A-7) |
| 2026 estimated tax trigger, ordinary case | Both: expected balance at least $500 after withholding/credits, and withholding plus credits below the required annual payment below; use Form 40ES | [§40-18-80](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-80); [2026 Form 40ES](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf) |
| 2026 estimated tax installments | Ordinary calendar-year schedule: April 15, 2026; June 15, 2026; September 15, 2026; January 15, 2027; next business day if weekend/state holiday | [2026 Form 40ES instructions](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf) |
| Estimated tax safe harbor | Required annual payment: smaller of 90% of 2026 tax or 100% of 2025 tax; prior-year return must have been filed for twelve months. Substitute 110% if 2025 Alabama AGI exceeded $150,000 ($75,000 if filing separately for 2026); credit withholding against timely installments | [2026 Form 40ES instructions](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf) |

Pay required installments timely; an annual total paid late does not cure earlier shortfalls. Changed income can change the starting installment; use the 40ES payment schedule. A qualifying farmer may pay the whole estimate by January 15, 2027 or file and pay the full tax by March 1, 2027 instead. Under §40-18-80 / §6654(i), farmer/fisherman status requires at least two-thirds of gross income from farming/fishing in the current or preceding year; its current-year safe harbor is 66⅔% with no high-income uplift. A twelve-month preceding year with no tax liability and US citizenship or residency throughout that year qualifies for the adopted §6654(e)(2) exception. Annualization and waiver claims require their separate conditions; no particular relief amount is supplied here. Check this point with one of our partner accountants.

Estimated-tax vouchers go to Alabama Department of Revenue, Individual Estimates, P.O. Box 327485, Montgomery, AL 36132-7485 (2026 Form 40ES instructions), or pay through [My Alabama Taxes](https://myalabamataxes.alabama.gov/).

On bank statements, `ALABAMA DOR` / `AL DEPT OF REVENUE`, `ADOR TAX PAYMENT`, `STATE OF AL TAX` and `MY ALABAMA TAXES` are payment clues only: the same payee can receive sales tax, withholding or income tax. Match each debit to the account statement in My Alabama Taxes before treating it as an income tax estimate.

## Penalties and interest

| Item | Value | Source |
|---|---|---|
| Failure to timely file | "10% of the tax due or $50, whichever is greater. ... does not apply to a tax return filed indicating no tax due or a refund" | [§40-2A-11(a)](https://alison.legislature.state.al.us/code-of-alabama?section=40-2A-11) |
| Failure to timely pay | "1% of the unpaid amount for each month or fraction of a month that the tax remains unpaid. The maximum penalty is 25%" | [§40-2A-11(b)](https://alison.legislature.state.al.us/code-of-alabama?section=40-2A-11) |
| Estimated-tax underpayment | Use Form 2210AL, by installment. Alabama adopts §6654 with a $500 small-tax exception and its specified state substitutions. The ordinary 90%/100%/110% tests and farmer exception above apply to their respective years; for the 2025 return compare 2025 tax and 2024 tax/AGI, not 2026 estimates | [§40-18-80](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-80); [§6654](https://uscode.house.gov/us/usc/119-134/t26/s6654/) |
| Interest | Treasury §6621 underpayment rate from the original due date, even with a filing extension | [§40-1-44(a)](https://alison.legislature.state.al.us/code-of-alabama?section=40-1-44) |

For an individual, willful failure to file under [§40-29-112](https://alison.legislature.state.al.us/code-of-alabama?section=40-29-112) is a misdemeanor: on conviction, up to $25,000 or one year imprisonment, or both, plus prosecution costs. Obtain professional representation for any criminal/audit issue. Civil penalties may be waived for established reasonable cause, with the burden on the taxpayer (§40-2A-11(h)); interest is separate.

## Cross-border points

- Residents report all-source income; nonresidents report Alabama-source income (§40-18-14(a)(4)); this Guide does not compute nonresident allocations.
- Other-state credit: the three limits in step 11 apply. For foreign-country taxes, the booklet points to Schedule OC Section B Part I, not CR. [§40-18-21(c)](https://alison.legislature.state.al.us/code-of-alabama?section=40-18-21) expressly covers qualifying resident pass-through owners/estate or trust beneficiaries at 50% of their proportionate foreign tax, capped at Alabama tax on that foreign income; [Rule 810-3-21-.03](https://admincode.legislature.state.al.us/api/rule/810-3-21-.03) adds the Alabama-source liability floor and an alternative methodology for foreign-source income with federal foreign tax credits. These are not a blanket credit for all foreign tax. No particular foreign/treaty credit result is supplied here. Check this point with one of our partner accountants.
- Part-year residents: Form 40 for the resident period, reporting only income earned while resident and prorating itemized deductions and the federal tax deduction; they keep the full standard deduction and personal and dependent exemptions (booklet, p.5). Nonresidents file Form 40NR and prorate exemptions. When both returns are required for the year, claim personal/dependent exemptions on the part-year Form 40 only, not again on 40NR. The original April move example therefore needs the actual move date and both income periods. See `alabama-cross-border`.

## Worked examples

Client facts in these examples are hypothetical. The rates, the standard deduction chart and the exemptions come from the table above. These four original cases use calendar-2025 facts and the statutory rate schedule to show arithmetic. For filing, line 17 requires the booklet Tax Table unless the NOL exception applies; the banded table result can differ. Do not enter the rate-schedule illustration as the table liability.

**Example 1: single filer through the brackets**

A full-year resident with $10,000 of Alabama taxable income after the standard deduction and exemptions:

```oa-check
name: AL Form 40 tax from rate schedule, single
inputs:
  taxable: 10000
steps:
  - tax: 0.02 * 500 + 0.04 * 2500 + 0.05 * (taxable - 3000)
expected:
  tax: 460.00
```

**Example 2: single filer from Alabama AGI to tax, with one dependent**

A single filer has Alabama AGI (line 10) of $40,000, a federal income tax liability of $3,000 fully deductible under the worksheet (no credit reduction or allocation), and one qualifying dependent. AGI is above $35,500, so the standard deduction is $2,500; the personal exemption is $1,500; AGI is at or below $50,000, so the dependent exemption is $1,000.

```oa-check
name: AL Form 40, single, AGI 40000, one dependent
inputs:
  alabama_agi: 40000
  standard_deduction: 2500
  federal_tax_deduction: 3000
  personal_exemption: 1500
  dependent_exemption: 1000
steps:
  - total_deductions: standard_deduction + federal_tax_deduction + personal_exemption + dependent_exemption
  - taxable: alabama_agi - total_deductions
  - tax: 0.02 * 500 + 0.04 * 2500 + 0.05 * (taxable - 3000)
expected:
  total_deductions: 8000.00
  taxable: 32000.00
  tax: 1560.00
```

**Example 3: single filer with $2,000 taxable income**

A single self-employed filer with Alabama taxable income of $2,000 after deductions and exemptions:

```oa-check
name: AL individual tax, single brackets
inputs:
  taxable: 2000
steps:
  - tax: 0.02 * 500 + 0.04 * (taxable - 500)
expected:
  tax: 70.00
```

**Example 4: married-filing-joint with $8,000 taxable income**

A married couple filing jointly with Alabama taxable income of $8,000:

```oa-check
name: AL individual tax, MFJ brackets
inputs:
  taxable: 8000
steps:
  - tax: 0.02 * 1000 + 0.04 * 5000 + 0.05 * (taxable - 6000)
expected:
  tax: 320.00
```

## Ask the client first

1. What are the taxpayer's and spouse's residency dates, year-end filing status and dependents? Confirm full-year return eligibility before computing.
2. What income exists beyond W-2/1099 amounts: rents, royalties, gains, K-1s, farms or Schedule C, and is any taxed by another state or foreign country?
3. What are taxable and nontaxable interest/dividends, including the Schedule B trigger, and what federal liability and Alabama adjustments/deductions are established?
4. What estimates, withholding and extension payments actually appear in the Alabama account, and does expected tax meet the estimated-tax trigger?
5. What out-of-state purchases lacked sales tax, for Schedule ATP consumer use tax?
6. For 2026, what overtime premium is shown in W-2 box 12 code TT, and is the return-year form available for the period being computed?

Refer out to a professional rather than answer from this skill: multistate business activity needing apportionment; part-year residency with complex sourcing; an Alabama net operating loss carryforward; Business Privilege Tax for entities beyond a sole proprietorship; municipal occupational taxes; Alabama credits (Historic Rehabilitation, Growing Alabama and similar); audit representation or controversy; and any question about tax fraud, evasion or aggressive positions. No computation of those held outcomes is supplied. Check this point with one of our partner accountants. The detailed questions and trigger amounts in the body remain part of intake.

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | 2025 Form 40 booklet: pp.5-18 (filing/status, income, chart, credits, adjustments, payments, penalties), pp.21-22 Schedule B/CR, p.31 federal-tax worksheet and p.33 required schedules; relevant provisions read, not an assertion of a 2026 final form | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf | 2026-11-27 |
| 2 | 2025 Form 40: filing status/exemptions; income/deduction, credit/payment/balance/refund mappings; page 2 Parts I-V; Schedule A/B boundary | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40.pdf | 2026-11-27 |
| 3 | Code §40-18-5: all single/head-of-family/separate and joint rate bands; rendered official Legislature text read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-5 | 2026-11-27 |
| 4 | Code §40-18-15: (a)(1),(11)-(12),(29), (b)(4), (c),(d),(f); business/retirement, enacted overtime, standard deduction, federal tax and spouse elections; rendered official text read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15 | 2026-11-27 |
| 5 | Code §40-18-19(a)(8)-(9): personal and dependent exemption amounts, support and relationship definitions; rendered text read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-19 | 2026-11-27 |
| 6 | Code §40-18-15.8: Alabama ABLE contributions, rollover/withdrawal rules and sunset, all subsections read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-15.8 | 2026-11-27 |
| 7 | Code §40-18-21(a),(c),(d): interstate cap/common-income/AGI limitation and foreign-owner credit; historic 2013-2017 exception not applied to 2025; rendered text read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-21 | 2026-11-27 |
| 8 | Rule 810-3-21-.03: general floor and foreign-credit alternative, official three-page rule read | https://admincode.legislature.state.al.us/api/rule/810-3-21-.03 | 2026-11-27 |
| 9 | 2026 Form 40ES: worksheet, ordinary/high-income tests, installments, changed-income and farmer instructions, mailing address | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf | 2026-11-27 |
| 10 | Code §40-18-80: adoption of federal estimated-tax rules and Alabama substitutions, all subsections read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-80 | 2026-11-27 |
| 11 | 26 USC §6654: (a)-(i) and (k) installment, safe harbor, exceptions and farmer conditions; operative text read | https://uscode.house.gov/us/usc/119-134/t26/s6654/ | 2026-11-27 |
| 12 | Code §40-18-27(a),(c): filing threshold and due date; §40-18-42(a) balance payment deadline, rendered provisions read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-27 ; https://alison.legislature.state.al.us/code-of-alabama?section=40-18-42 | 2026-11-27 |
| 13 | Code §40-2A-7(c)(2)a: refund general time limits and deemed payment date, rendered text read | https://alison.legislature.state.al.us/code-of-alabama?section=40-2A-7 | 2026-11-27 |
| 14 | Code §40-2A-11(a),(b),(h): late filing/payment, reasonable cause; §40-1-44(a): interest, rendered provisions read | https://alison.legislature.state.al.us/code-of-alabama?section=40-2A-11 ; https://alison.legislature.state.al.us/code-of-alabama?section=40-1-44 | 2026-11-27 |
| 15 | Code §40-29-112: individual criminal failure-to-file consequence and costs; full section read | https://alison.legislature.state.al.us/code-of-alabama?section=40-29-112 | 2026-11-27 |
| 16 | Code §40-18-13(a): federal taxable year/accounting method; §40-18-14(a)(1),(3)-(4) and §40-18-14.2: separate Alabama income/adjustments, rendered provisions read | https://alison.legislature.state.al.us/code-of-alabama?section=40-18-13 ; https://alison.legislature.state.al.us/code-of-alabama?section=40-18-14 ; https://alison.legislature.state.al.us/code-of-alabama?section=40-18-14.2 | 2026-11-27 |
| 17 | Act 2026-604/HB527 enrolled: §1 overtime definition/cap; §3 effective date, pp.8,15; checked with current codified §40-18-15(a)(29) | https://alison.legislature.state.al.us/files/pdf/SearchableInstruments/2026RS/HB527-enr.pdf | 2026-11-27 |
| 18 | ADOR overtime page: state premium/cap and code TT reporting, substantive page read | https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/ | 2026-11-27 |
| 19 | 26 USC §225: full operative section, especially qualified FLSA premium, federal limitations, SSN, joint return and sunset | https://uscode.house.gov/us/usc/t26/s225/ | 2026-11-27 |
| 20 | ADOR rate FAQ: both progressive rate schedules read | https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/ | 2026-11-27 |

Not yet confirmed: no unproven amount is usable here. Specific foreign/treaty credits, disputed business/home-office deductions, solo-401(k) component allocations, §199A/QBI outcomes, NOL computations, municipal/occupational interactions, special credits and controversy are explicit referral boundaries above. Alabama application of §225's federal conditions in high-income/separate-return overtime cases is held, not an unconditional $1,000 entitlement. This Guide supplies no 2026 final-return filing thresholds, deduction/exemption chart or line mapping. For those held outcomes: Check this point with one of our partner accountants.

> Contributed by Anthony Bandura.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
