---
name: al-income-tax
description: "Use this skill whenever asked about Alabama individual income tax for self-employed individuals or sole proprietors, filing Form 40, AL estimated tax (Form 40ES), Alabama tax brackets, Alabama deductions, federal income tax deduction on AL return, or any query involving Alabama state income tax compliance. Trigger on phrases like \"Alabama income tax\", \"AL income tax\", \"Form 40\", \"Alabama estimated tax\", \"Alabama self-employed tax\", \"ADOR income tax\", or \"Code of Ala. §40-18\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/al-income-tax"
  jurisdiction: "US-AL"
  tax_year: "2025"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama individual income tax: self-employed / sole proprietor

> **Source-cited draft.** Built from the ALDOR individual income tax rate FAQ, the ALDOR Individual Income Tax page, the 2025 Form 40 and its booklet and the 2026 Form 40ES instructions, read 2026-11-13. No accountant has reviewed it. Do not file from it without review by a qualified Alabama professional.

Tax year: the calendar year. Authority: Alabama Department of Revenue (ALDOR), My Alabama Taxes portal (myalabamataxes.alabama.gov, per the Form 40 booklet). Governing provisions: Code of Alabama §§40-18-1 through 40-18-30 and 40-18-40 through 40-18-59, as cited on the ALDOR Individual Income Tax page.

See also: `alabama-income-tax` (the full Form 40 walkthrough), `alabama-cross-border`, `al-payroll-withholding`.

## Who this applies to

- Self-employed individuals and sole proprietors who are Alabama residents file Form 40 (the long return), reporting income from all sources unless Alabama specifically exempts it (ALDOR Individual Income Tax page: "Taxable net income earned from all sources by residents"; 2025 Form 40 booklet, Who Must File). Anyone with Schedule C, D, E or F income cannot use the short Form 40A (booklet, p.5).
- Part-year residents and non-residents use Form 40/40NR under different allocation rules; see `alabama-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Single, head of family, married filing separately | 2% on the first $500 of taxable income; 4% on the next $2,500; 5% on all over $3,000 | 2025 and 2026 | [ALDOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| Married filing jointly | 2% on the first $1,000; 4% on the next $5,000; 5% on all over $6,000 | 2025 and 2026 | [ALDOR rate FAQ](https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/) |
| Filing requirement (gross income) | Single $4,500; head of family $8,200; married filing joint $11,500; married filing separate $5,750 | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.5 |
| Personal exemption (Form 40 line 13) | Single $1,500; married filing joint $3,000; married filing separate $1,500; head of family $3,000 | 2025 | [2025 Form 40](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40.pdf), lines 1 to 4 |
| Dependent exemption by Alabama AGI (line 14) | $1,000 at AGI $0 to $50,000; $500 at $50,001 to $100,000; $300 over $100,000 | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.10 dependent exemption chart |
| Standard deduction, married filing joint | $8,500 at Alabama AGI $0 to $25,999, stepping down in bands to $5,000 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, married filing separate | $4,250 stepping down to $2,500 at $17,750 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, head of family | $5,200 stepping down to $2,500 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Standard deduction, single | $3,000 stepping down to $2,500 at $35,500 and above | 2025 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.9 chart |
| Estimated tax threshold | "Every individual who reasonably expects to owe at least $500 in tax in 2026 is required to file and pay estimated tax" | 2026 | [2025 Form 40 booklet](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf), p.18 |
| Estimated tax due dates | April 15, 2026; June 15, 2026; September 15, 2026; January 15, 2027 | 2026 | [2026 Form 40ES instructions](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf) |
| Overtime premium deduction (Act 2026-604) | Lesser of the actual overtime premium or $1,000 per taxpayer | 2026 to 2028 | [ALDOR Overtime Premium Deduction page](https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/) |

Alabama is one of the few states allowing a deduction for federal income taxes paid (Amendment 225, ALDOR Individual Income Tax page: "provided deduction for federal income taxes paid by individual taxpayers").

## The taxable base

1. **Starting point:** Alabama begins from federal adjusted gross income, carried to Form 40 through the income lines (lines 5 to 8).
2. **Additions:** income excluded federally but taxable in Alabama (for example, interest on other states' obligations).
3. **Subtractions:** Alabama-exempt income. The booklet's "Examples of Income You DO NOT Report" include federal Social Security benefits, federal Railroad Retirement benefits, military retirement pay, unemployment compensation and state income tax refunds, and interest on obligations of the State of Alabama and its subdivisions and of the United States (2025 Form 40 booklet).
4. **Federal income tax deduction (line 12):** deduct federal income taxes actually paid (or accrued) during the tax year, using the booklet worksheet (Amendment 225; booklet line 12).
5. **Standard deduction or itemized (line 11):** the standard deduction chart is keyed to Alabama AGI (line 10), not federal AGI; compute both ways. "A dependent or student may take the standard deduction even if claimed as a dependent by someone else" (booklet).
6. **Personal exemption** (line 13) and **dependent exemption** (line 14, Schedule DS): the dependent exemption steps down with Alabama AGI per the chart above.
7. Total deductions (line 15) come off Alabama AGI to give taxable income (line 16); the tax goes on line 17 from the Tax Table (2025 Form 40).

Self-employed specifics: Alabama computes income on the federal pattern, so Schedule C business deductions, the self-employed health-insurance deduction, SEP-IRA and solo-401(k) contributions and the federal home-office deduction flow through federal AGI into the Alabama starting point. The federal QBI deduction (§199A) reduces federal tax, and therefore reduces the federal income tax available for the Alabama line-12 deduction, but does not itself change Alabama taxable income.

## Deadlines and filing

- **Filing deadline:** the same date as the federal return: "You should file as soon as you can after January 1, 2026, but no later than the due date of the federal return" (2025 Form 40 booklet, When To File).
- **Automatic extension:** "You will automatically be granted an extension until October 15, 2026" with no form to file; pay expected tax with Form 40V, "Automatic Extension Payment" box checked, by the federal due date. "An extension means only that you will not be assessed a penalty for filing your return after the due date"; interest still runs (booklet).
- **Estimated tax:** Form 40ES, four installments on April 15, June 15 and September 15, 2026 and January 15, 2027. Safe harbor: withholding plus credits at least the smaller of 90% of the 2026 tax or 100% of the 2025 tax (110% where 2025 Alabama AGI was over $150,000, or $75,000 married filing separate) (2026 Form 40ES instructions). Vouchers go to Alabama Department of Revenue, Individual Estimates, P.O. Box 327485, Montgomery, AL 36132-7485 (2026 Form 40ES instructions), or pay through My Alabama Taxes.
- **Refund window:** "Original returns must be filed within two years of the date the taxes are paid to be eligible for a refund" (booklet).
- Reading the client's bank statements for Alabama payments: debits to the Alabama Department of Revenue or through My Alabama Taxes are usually estimated or balance-due income tax payments, but a business may also pay sales tax or withholding to the same payee. Match each debit to the account statement in My Alabama Taxes before treating it as an income tax estimate.

## Penalties and interest

- **Failure to timely file:** "Alabama law provides a penalty of 10% of the tax due or $50, whichever is greater, if filed late. The penalty does not apply to a tax return filed indicating no tax due or a refund" (booklet, p.17).
- **Failure to timely pay:** "The penalty for not paying the tax when due is 1% of the unpaid amount for each month or fraction of a month that the tax remains unpaid. The maximum penalty is 25%" (booklet, p.17).
- **Underpayment (estimated tax):** where 2025 tax due is $500 or more and withholding plus timely estimates fell short of "the smaller of: 1. 90% of your 2025 tax (66-2/3% for farmers), or 2. 100% of your 2024 tax" (12-month period), computed on Form 2210AL (booklet, p.17).
- **Interest:** "Alabama law provides that the same rate of interest shall be collected as currently prescribed by the Internal Revenue Service," running from the due date even where an extension was granted (booklet).
- **ABLE deduction:** contributions up to $5,000 per individual per year under §40-18-15.8, Code of Alabama 1975 (booklet, p.17).
- **Criminal liability:** §40-29-112, Code of Alabama 1975: willful failure to file is a misdemeanor punishable by a fine up to $25,000 or imprisonment up to 1 year, or both (booklet, p.17).

## Cross-border points

- Residents are taxed on all-source income; non-residents on Alabama-source income (ALDOR Individual Income Tax page).
- Credit for taxes paid to another state runs through Schedule CR (see `alabama-income-tax` for the mechanics).
- Multistate allocation and part-year proration: see `alabama-cross-border`.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the table above are used.

**Example 1: single filer with $2,000 taxable income**

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

**Example 2: married-filing-joint with $8,000 taxable income**

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

- Filing status, Alabama residency dates, and the spouse's residency (where the spouses' residencies differ, confirm the joint-return eligibility rules before filing).
- Any income taxed by another state or a foreign country (Schedule CR / Schedule OC)?
- Income not on a W-2 or 1099: rents, royalties, gains, K-1s, farm (Schedule C flow-through)?
- Alabama estimated payments or extension payments made, and how much?
- Expected tax of at least $500 for the year (the estimated-tax trigger)?
- Refer out to a professional rather than answer from this skill: multistate business activity needing apportionment; part-year residency with complex sourcing; an Alabama net operating loss carryforward; Business Privilege Tax for entities beyond a sole proprietorship; municipal occupational taxes; Alabama credits (Historic Rehabilitation, Growing Alabama and similar); audit representation or controversy; and any question about tax fraud, evasion or aggressive positions.

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR FAQ: What is Alabama's individual income tax rate?, read for 2%/4%/5% brackets by filing status | https://www.revenue.alabama.gov/faqs/what-is-alabamas-individual-income-tax-rate/ | 2026-11-13 |
| 2 | ALDOR Individual Income Tax page, read for authority sections, application, Amendments 25/61/225, minimum exemptions | https://revenue.alabama.gov/taxes-fees/individual-income-tax/ | 2026-11-13 |
| 3 | 2025 Alabama Form 40 booklet, 25f40bk, read for filing thresholds, exemptions, standard-deduction chart, deadlines, penalties, estimated tax, exempt income, ABLE, criminal liability | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf | 2026-11-13 |
| 4 | 2025 Alabama Form 40, read for personal exemptions by filing status, lines 10 to 17 | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40.pdf | 2026-11-13 |
| 5 | 2026 Form 40ES estimated tax instructions, read for installment dates, safe harbor, mailing address | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/26f40esblk.pdf | 2026-11-13 |
| 6 | ALDOR Overtime Premium Deduction (Act 2026-604) page, read for the page as a whole | https://www.revenue.alabama.gov/individual-corporate/overtime-premium-deduction-act-2026-604/ | 2026-11-13 |

Not yet confirmed: the 2026 filing thresholds, standard deduction chart and dependent exemption chart (no 2026 Form 40 booklet was published when read, so the 2025 figures are shown); the Form 40 line numbers for additions, credits and payments beyond lines 10 to 17; the paid-versus-accrued method choice for the federal income tax deduction; the treatment of an Alabama net operating loss.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `al-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/al-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
