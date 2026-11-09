---
name: al-income-tax
description: Use this skill whenever asked about Alabama individual income tax for self-employed individuals or sole proprietors -- filing Form 40, AL estimated tax (Form 40ES), Alabama tax brackets, Alabama deductions, federal income tax deduction on AL return, or any query involving Alabama state income tax compliance. Trigger on phrases like "Alabama income tax", "AL income tax", "Form 40", "Alabama estimated tax", "Alabama self-employed tax", "ADOR income tax", or "Code of Ala. §40-18".
jurisdiction: US-AL
domain: income-tax
type: filing-howto
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama individual income tax -- self-employed / sole proprietor

> **Source-cited draft.** Built from the ALDOR individual income tax rate FAQ and Individual Income Tax page and the 2025 Form 40 booklet (25f40bk), read 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified Alabama professional.

Tax year: the calendar year. Authority: Alabama Department of Revenue (ALDOR), My Alabama Taxes portal (myalabamataxes.alabama.gov, per the Form 40 booklet). Governing provisions: Code of Alabama §§40-18-1 through 40-18-30 and 40-18-40 through 40-18-59, as cited on the ALDOR Individual Income Tax page.

See also: `alabama-income-tax` (the full Form 40 walkthrough), `al-cross-border`, `al-payroll-withholding`.

## Who this applies to

- Self-employed individuals and sole proprietors who are Alabama residents file Form 40 (the long return), reporting income from all sources unless Alabama specifically exempts it (ALDOR Individual Income Tax page: "Taxable net income earned from all sources by residents"; 2025 Form 40 booklet, Who Must File).
- The booklet: "All income is subject to Alabama income tax unless specifically exempted by state law" (ALDOR FAQ, What income must I report).
- Part-year residents and non-residents use Form 40/40NR under different allocation rules -- see `al-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Single, head of family, married filing separately | 2% on the first $500 of taxable income; 4% on the next $2,500; 5% on all over $3,000 | current | [ALDOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| Married filing jointly | 2% on the first $1,000; 4% on the next $5,000; 5% on all over $6,000 | current | [ALDOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| Filing requirement (gross income) | Single: gross income at least $4,500; head of family: $8,200; married filing joint: $11,500; married filing separate: $5,750 | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.5 |
| Minimum personal exemptions | $1,500 for single taxpayers, $3,000 for joint filers; minimum dependent exemption of $300 for each dependent (Amendment 25) | current | [ALDOR Individual Income Tax page](https://revenue.alabama.gov/taxes-fees/individual-income-tax/) |
| Dependent exemption by Alabama AGI | $1,000 at AGI $0–50,000; $500 at $50,001–100,000; $300 over $100,000 | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.8 dependent exemption chart |
| Standard deduction, married filing joint | $8,500 at Alabama AGI $0–25,999, stepping down in bands to $5,000 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, married filing separate | $4,250 stepping down to $2,500 at $17,750 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, head of family | $5,200 stepping down to $2,500 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, single | $3,000 stepping down to $2,500 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Estimated tax threshold | "Every individual who reasonably expects to owe at least $500 in tax in 2026 is required to file and pay estimated tax" | 2026 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), Payment of Estimated Tax |

The personal exemption is set by filing status (booklet: "If you check box 2, enter $3,000 on line 13"; a dependent or student "can claim a personal exemption of $1,500"). Alabama is one of the few states allowing a deduction for federal income taxes paid (Amendment 225, ALDOR Individual Income Tax page: "provided deduction for federal income taxes paid by individual taxpayers").

## The taxable base

1. **Starting point:** Alabama begins from federal adjusted gross income.
2. **Additions:** income excluded federally but taxable in Alabama (e.g., interest on other states' obligations).
3. **Subtractions:** Alabama-exempt income -- "Interest on obligations of the State of Alabama or any county, city, or municipality of Alabama, and interest on obligations of the United States, or any of its possessions" (ALDOR FAQ); Social Security benefits: not archived in a primary source this run, so treat as unconfirmed until the ALDOR exempt-income list is checked.
4. **Federal income tax deduction:** deduct federal income taxes actually paid (or accrued) during the tax year (Amendment 225; booklet line 12 worksheet).
5. **Standard deduction or itemized:** the standard deduction chart is keyed to Alabama AGI (line 10), not federal AGI; compute both ways. "A dependent or student may take the standard deduction even if claimed as a dependent by someone else" (booklet).
6. **Personal exemption** (line 13) and **dependent exemption** (line 14, Schedule DS): the dependent exemption steps down with Alabama AGI per the chart above.
7. Result: Alabama taxable income -- apply the graduated rates.

Self-employed specifics: Alabama computes income on the federal pattern, so Schedule C business deductions, the self-employed health-insurance deduction, SEP-IRA and solo-401(k) contributions and the federal home-office deduction flow through federal AGI into the Alabama starting point. The federal QBI deduction (§199A) reduces federal tax -- and therefore reduces the federal income tax available for the Alabama line-12 deduction -- but does not itself change Alabama taxable income.

Form 40 line mapping confirmed in the booklet: line 11 itemized/standard deduction, line 12 federal income tax deduction, line 13 personal exemption, line 14 dependent exemption; Schedule B is required where taxable and nontaxable interest and dividends reach $1,500 or more (booklet: interest and dividends "cannot exceed $1,500" as a Form 40A condition). The remaining line-by-line mapping previously carried here is unconfirmed.

## Deadlines and filing

- **Filing deadline:** the same date as the federal return -- "You should file as soon as you can after January 1, 2026, but no later than the due date of the federal return" (2025 Form 40 booklet, When To File).
- **Automatic extension:** "You will automatically be granted an extension until October 15, 2026" with no form to file; pay expected tax with Form 40V, "Automatic Extension Payment" box checked, by the federal due date. "An extension means only that you will not be assessed a penalty for filing your return after the due date" -- interest still runs (booklet).
- **Estimated tax:** Form 40ES; "The due dates for making estimated tax payments are the same as required by Federal Income Tax Law" (booklet) -- the specific calendar dates are federal law and are not stated in the booklet (see Not yet confirmed).
- **Refund window:** "Original returns must be filed within two years of the date the taxes are paid to be eligible for a refund" (booklet).
- Payment by mail (Form 40 payment to the booklet's Montgomery address) or through My Alabama Taxes.

## Penalties and interest

- **Failure to timely file:** "Alabama law provides a penalty of 10% of the tax due or $50, whichever is greater, if filed late. The penalty does not apply to a tax return filed indicating no tax due or a refund" (booklet, p.17).
- **Failure to timely pay:** "The penalty for not paying the tax when due is 1% of the unpaid amount for each month or fraction of a month that the tax remains unpaid. The maximum penalty is 25%" (booklet, p.17).
- **Underpayment (estimated tax):** where 2025 tax due is $500 or more and withholding plus timely estimates fell short of "the smaller of: 1. 90% of your 2025 tax (66-2/3% for farmers), or 2. 100% of your 2024 tax" (12-month period), computed on Form 2210AL (booklet, p.17).
- **Interest:** "Alabama law provides that the same rate of interest shall be collected as currently prescribed by the Internal Revenue Service," running from the due date even where an extension was granted (booklet).
- **ABLE deduction:** contributions up to $5,000 per individual per year under §40-18-15.8, Code of Alabama 1975 (booklet).
- **Criminal liability:** §40-29-112, Code of Alabama 1975 -- willful failure to file is a misdemeanor punishable by a fine up to $25,000 or imprisonment up to 1 year, or both (booklet, p.17).

## Cross-border points

- Residents taxed on all-source income; non-residents on Alabama-source income (ALDOR Individual Income Tax page).
- Credit for taxes paid to another state runs through Schedule CR (see `alabama-income-tax` for mechanics; limitation rules are tied out there).
- Multistate allocation and part-year proration: see `al-cross-border`. The mechanics there are marked unconfirmed.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used.

**Example 1: single filer with $2,000 taxable income**

A single self-employed filer (hypothetical) with Alabama taxable income of $2,000 after deductions and exemptions:

```oa-check
name: AL individual tax, single brackets
inputs:
  taxable: 2000
steps:
  - tax: 0.02 * 500 + 0.04 * (taxable - 500)
expected:
  tax: 70.00
```

**Example 2: married-filing-joint with $8,000 taxable income**

MFJ (hypothetical) with Alabama taxable income of $8,000:

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

- Filing status, Alabama residency dates, and the spouse's residency (where the spouses' residencies differ, confirm the joint-return eligibility rules before filing).
- Any income taxed by another state or a foreign country (Schedule CR / Schedule OC)?
- Income not on a W-2 or 1099 -- rents, royalties, gains, K-1s, farm (Schedule C flow-through)?
- Alabama estimated payments or extension payments made, and how much?
- Expected tax at least $500 for the year (estimated-tax trigger)?
- Multistate business activity, NOL carryforwards, Business Privilege Tax questions, municipal occupational taxes, Alabama credits, audit matters -- refer out (see the refusal points in `alabama-income-tax`).

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR FAQ: What is Alabama's individual income tax rate? (2%/4%/5% brackets by filing status) | https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate | 2026-10-28 |
| ALDOR Individual Income Tax page (authority sections, application, Amendments 25/61/225, minimum exemptions, filing AGI thresholds) | https://revenue.alabama.gov/taxes-fees/individual-income-tax/ | 2026-10-28 |
| 2025 Alabama Form 40 booklet, 25f40bk (filing thresholds, exemptions, standard-deduction chart, deadlines, penalties, estimated tax, ABLE, criminal liability) | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf | 2026-10-28 |

Not yet confirmed: the full Form 40 line-by-line mapping beyond lines 11–14 (previously carried: federal AGI line 7, additions line 8, subtractions line 9, AL AGI line 10, tax line 15, credits lines 16–18, estimates line 23, balance/refund lines 27–28 -- confirm against the form); the estimated-tax installment calendar dates (previously carried as April 15, June 15, September 15, January 15 -- the booklet says only "the same as required by Federal Income Tax Law"); the treatment of Social Security benefits as a specific exclusion (the exempt-income list was not archived); the tiered filing-threshold schedule by AGI for lower incomes; supplier-pattern interpretations of bank-statement labels.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
