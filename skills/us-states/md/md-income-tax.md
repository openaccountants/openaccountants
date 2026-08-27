---
name: md-income-tax
description: Use this skill whenever asked about Maryland individual income tax. Trigger on phrases like "Maryland income tax", "MD income tax", "Form 502", "Comptroller of Maryland", "Maryland county tax", "piggyback tax". Maryland has 10 graduated state brackets (2%–6.50%) PLUS mandatory county/city income taxes (2.25%–3.20%). ALWAYS load us-tax-workflow-base first.
version: "0.1"
jurisdiction: US-MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MD Income Tax

## Maryland Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers Maryland Form 502 (Resident Income Tax Return) for sole proprietors and single-member LLCs. It addresses the 10-bracket graduated state income tax, mandatory county/Baltimore City piggyback taxes, and Maryland-specific deductions. It does NOT cover nonresident returns (Form 505), part-year returns, corporate returns (Form 500), or the pass-through entity tax (Form 510).

> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Section 1: Metadata

- **Jurisdiction** — Maryland (US-MD)
- **Tax authority** — [Comptroller of Maryland](https://www.marylandtaxes.gov/)
- **Filing portal** — [Maryland iFile](https://interactive.marylandtaxes.gov/Individuals/iFile_ChooseForm/)
- **Legislation** — Md. Code Ann., Tax–General, Title 10
- **Primary form** — Form 502 (Maryland Resident Income Tax Return)
- **Filing deadline** — April 15, 2027 (for tax year 2026)
- **Version** — 0.1
- **Date** — May 22, 2026
- **Validation status** — AI-drafted — Q3

### Sources consulted

1. Comptroller of Maryland — 2025 Resident Tax Booklet: <https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/instructions/2025/resident-booklet.pdf>
2. RemoteLaws — Maryland Income Tax Rates 2025: <https://remotelaws.com/state-income-tax/us-states/maryland/>
3. TaxFormCalculator — Maryland 2026 Tax Tables: <https://www.taxformcalculator.com/maryland/tax-tables/2026.html>
4. StateByStateTax — Maryland County Rates: <https://www.statebystatetax.com/states/maryland.html>
5. Md. Code Ann., Tax–General, §§ 10-105, 10-106

## Section 2: Quick reference — rates and thresholds

### State income tax brackets — Single, Married Filing Separately, Dependent (TY2025+)

**State income tax brackets — Single, Married Filing Separately, Dependent (TY2025+)**

| Taxable net income | Rate | Tax calculation |
| --- | --- | --- |
| $0 – $1,000 | 2.00% | 2.00% of taxable net income |
| $1,001 – $2,000 | 3.00% | $20 + 3.00% of excess over $1,000 |
| $2,001 – $3,000 | 4.00% | $50 + 4.00% of excess over $2,000 |
| $3,001 – $100,000 | 4.75% | $90 + 4.75% of excess over $3,000 |
| $100,001 – $125,000 | 5.00% | $4,697.50 + 5.00% of excess over $100,000 |
| $125,001 – $150,000 | 5.25% | $5,947.50 + 5.25% of excess over $125,000 |
| $150,001 – $250,000 | 5.50% | $7,260.00 + 5.50% of excess over $150,000 |
| $250,001 – $500,000 | 5.75% | $12,760.00 + 5.75% of excess over $250,000 |
| $500,001 – $1,000,000 | 6.25% | $27,135.00 + 6.25% of excess over $500,000 |
| Over $1,000,000 | 6.50% | $58,385.00 + 6.50% of excess over $1,000,000 |

### State income tax brackets — Married Filing Jointly, Head of Household, Qualifying Surviving Spouse

**State income tax brackets — Married Filing Jointly, Head of Household, Qualifying Surviving Spouse**

| Taxable net income | Rate | Tax calculation |
| --- | --- | --- |
| $0 – $1,000 | 2.00% | 2.00% of taxable net income |
| $1,001 – $2,000 | 3.00% | $20 + 3.00% of excess over $1,000 |
| $2,001 – $3,000 | 4.00% | $50 + 4.00% of excess over $2,000 |
| $3,001 – $150,000 | 4.75% | $90 + 4.75% of excess over $3,000 |
| $150,001 – $175,000 | 5.00% | $7,072.50 + 5.00% of excess over $150,000 |
| $175,001 – $225,000 | 5.25% | $8,322.50 + 5.25% of excess over $175,000 |
| $225,001 – $300,000 | 5.50% | $10,947.50 + 5.50% of excess over $225,000 |
| $300,001 – $600,000 | 5.75% | $15,072.50 + 5.75% of excess over $300,000 |
| $600,001 – $1,200,000 | 6.25% | $32,322.50 + 6.25% of excess over $600,000 |
| Over $1,200,000 | 6.50% | $69,822.50 + 6.50% of excess over $1,200,000 |

### County / Baltimore City piggyback tax rates (TY2025)

**County / Baltimore City piggyback tax rates (TY2025)**

| Jurisdiction | Rate | Type |
| --- | --- | --- |
| Baltimore City | 3.20% | Flat |
| Allegany County | 3.20% | Flat |
| Anne Arundel County | 2.25%–3.20% | Progressive |
| Baltimore County | 3.20% | Flat |
| Calvert County | 3.20% | Flat |
| Caroline County | 3.20% | Flat |
| Carroll County | 3.03% | Flat |
| Cecil County | 2.74% | Flat |
| Charles County | 3.03% | Flat |
| Dorchester County | 3.30% | Flat |
| Frederick County | Progressive | Progressive |
| Garrett County | 2.65% | Flat |
| Harford County | 3.06% | Flat |
| Howard County | 3.20% | Flat |
| Kent County | 3.20% | Flat |
| Montgomery County | 3.20% | Flat |
| Prince George's County | 3.20% | Flat |
| Queen Anne's County | 3.20% | Flat |
| Somerset County | 3.20% | Flat |
| St. Mary's County | 3.20% | Flat |
| Talbot County | 2.40% | Flat |
| Washington County | 3.00% | Flat |
| Wicomico County | 3.20% | Flat |
| Worcester County | 2.25% | Flat |

**Note:** Anne Arundel and Frederick counties use progressive local brackets. See Comptroller instructions for details.

### Standard deduction

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single / MFS / Dependent | 15% of Maryland AGI, min $1,800, max $3,350 |
| MFJ / HoH / QSS | 15% of Maryland AGI, min $3,600, max $6,700 |

### Personal exemption

**Personal exemption table**

| Category | Amount (TY2025) |
| --- | --- |
| Each taxpayer, spouse, dependent | $3,200 |
| Additional for age 65+ or blind | $1,000 per qualifying condition |

Personal exemptions phase out for higher incomes (above ~$100,000 single / ~$150,000 MFJ — see Form 502 instructions).

## Section 3: How this skill works with the federal return

### Starting point

- **Starting point** — Maryland starts from **federal adjusted gross income (AGI)** — Form 1040, Line 11. This is entered on Form 502, Line 1.

### Additions to income

**Additions to income table**

| Item | Description | Source |
| --- | --- | --- |
| Out-of-state bond interest | Interest on bonds of other states | Md. Tax–General § 10-204 |
| Bonus depreciation add-back | Maryland decouples from IRC §168(k) bonus depreciation | Md. Tax–General § 10-210.1 |
| Other IRC decoupling items | Maryland may decouple from certain federal provisions — verify annually | Md. Tax–General § 10-107 |

### Subtractions from income

**Subtractions from income table**

| Item | Description | Source |
| --- | --- | --- |
| U.S. government interest | Interest on U.S. obligations | Md. Tax–General § 10-207(a) |
| Social Security benefits | Maryland fully exempts Social Security from state tax | Md. Tax–General § 10-207(q) |
| Pension exclusion | Up to $39,500 (2025) for qualifying taxpayers age 65+ or permanently disabled | Md. Tax–General § 10-209 |
| Military pay | Various exclusions for active-duty and reserve service | Md. Tax–General § 10-207 |
| Child/dependent care expenses | Subtraction based on federal credit amount | Md. Tax–General § 10-207 |
| Two-income subtraction (MFJ) | Up to $1,200 for two-earner married couples | Md. Tax–General § 10-207(m) |

### Resulting computation

- **Maryland tax computation formula** — Federal AGI + additions − subtractions = Maryland AGI → minus standard or itemized deduction → minus personal exemptions = Maryland taxable net income → apply state bracket rates → apply county rate → sum = total Maryland income tax.

## Section 4: Self-employed specific rules

### Estimated tax payments

- **Estimated tax payment threshold** — Self-employed individuals must make quarterly estimated tax payments if they expect to owe $500 or more in combined state and county tax.

**Estimated tax payment schedule**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Use Form 502D for estimated payments.

### Self-employment health insurance

- **SE health insurance treatment** — Maryland follows federal treatment — the deduction reduces federal AGI and flows through.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contributions treatment** — Maryland follows federal treatment — these deductions reduce federal AGI and flow through.

### Home office deduction

- **Home office deduction treatment** — Maryland follows the federal home office deduction as part of Schedule C, included in federal AGI.

### QBI deduction (Section 199A)

- **QBI deduction treatment** — Maryland does **not** allow the federal QBI deduction because Maryland starts from federal AGI (before the QBI deduction). The QBI deduction does not affect Maryland taxable income.

### County tax on self-employment income

- **County tax on self-employment income** — The county piggyback tax applies to Maryland taxable income, which includes self-employment income. The county is determined by the taxpayer's residence as of the last day of the tax year (December 31).

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply the 10-bracket graduated rate schedule based on filing status. |
| R-2 | Apply the county/city piggyback tax rate based on county of residence as of December 31. |
| R-3 | Start from federal AGI and apply Maryland additions and subtractions. |
| R-4 | Standard deduction is 15% of Maryland AGI, with minimums and maximums based on filing status. |
| R-5 | Personal exemptions are $3,200 per person; they phase out above $100,000/$150,000 AGI. |
| R-6 | Social Security is fully exempt. |
| R-7 | U.S. government bond interest is exempt. |
| R-8 | Add back interest from out-of-state municipal bonds. |
| R-9 | Both state and county taxes are computed on the same Maryland taxable net income. |
| R-10 | The county tax base = Maryland taxable net income (same as the state tax base, Form 502, Line 21). |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Determine whether the personal exemption phase-out applies based on income level. |
| J-2 | Evaluate whether Maryland itemized deductions exceed the standard deduction (15% of AGI with caps). |
| J-3 | Determine the correct county rate when the taxpayer moved during the year (use county as of Dec 31). |
| J-4 | Assess Maryland IRC conformity for bonus depreciation and other decoupling areas. |
| J-5 | Determine eligibility for the pension exclusion ($39,500 for age 65+). |
| J-6 | Evaluate credit for taxes paid to other states (important for D.C./VA border commuters). |
| J-7 | Apply Anne Arundel or Frederick County progressive local rates when applicable. |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Pattern | Maryland treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → Maryland AGI. Subject to state graduated rates + county rate. |
| Rental income (Schedule E) | Flows through federal AGI → Maryland AGI. Subject to both state and county tax. |
| Capital gains | Fully taxable at graduated state rates + county rate. |
| Interest / dividends | Taxable except U.S. and Maryland obligations (exempt). |
| Social Security | Fully exempt from Maryland state and county income tax. |
| Pension / retirement | Up to $39,500 exempt for age 65+ (pension exclusion). Remainder taxable. |

## Section 8: Form mapping

**Form 502 mapping table**

| Form 502 line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal AGI (Form 1040, Line 11) | Federal return |
| Lines 2–6 | Additions to income | Md. Tax–General § 10-204 |
| Lines 7–14 | Subtractions from income | Md. Tax–General §§ 10-207, 10-209 |
| Line 16 | Maryland AGI | Computed |
| Line 17 | Standard or itemized deduction | Md. Tax–General § 10-217 |
| Line 19 | Personal exemptions | Md. Tax–General § 10-211 |
| Line 20 | Net taxable income (before additional deductions) | Computed |
| Line 21 | Maryland taxable net income | Computed |
| Line 22 | Maryland state tax (from tax table or rate schedule) | Md. Tax–General § 10-105 |
| Line 24 | County/city tax | Md. Tax–General § 10-106 |
| Line 27 | Total Maryland tax | Line 22 + Line 24 |
| Lines 28–38 | Credits (earned income, poverty level, child/dependent care) | Various |
| Lines 39–46 | Payments, withholding, estimated payments | Various |
| Line 50 | Balance due or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-MD-01 | Taxpayer is a nonresident or part-year resident | Refuse; requires Form 505 or 515. |
| REF-MD-02 | Taxpayer lives in Anne Arundel or Frederick County (progressive local rates) | Flag for reviewer — requires local bracket lookup. |
| REF-MD-03 | Taxpayer has pass-through entity tax (PTET) election | Flag for reviewer — requires Form 510. |
| REF-MD-04 | Taxpayer claims complex credits (e.g., Biotechnology, Film, Heritage Structure) | Flag for reviewer — separate forms required. |
| REF-MD-05 | Taxpayer is a D.C. or Virginia commuter needing credit for taxes paid to other states | Flag for reviewer — reciprocal agreements and credit computation needed. |
| REF-MD-06 | Taxpayer's personal exemptions are subject to the income-based phase-out | Flag for reviewer — verify exemption reduction calculation. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
