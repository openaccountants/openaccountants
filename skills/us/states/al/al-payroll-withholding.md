---
name: al-payroll-withholding
description: >
  Use this skill whenever asked about Alabama payroll withholding for
  tax year 2026 -- Form A-1 (withholding return) and A-2 (annual
  reconciliation), A-3 (non-resident real-estate withholding), A-6
  (withholding on non-payroll compensation), bulk-filer registration
  (Form BF-1), the A-1/A-6 file-layout change effective 2024-01-27
  for overtime-exemption reporting, and Alabama withholding on
  non-resident members of pass-through entities. Trigger on "Alabama
  withholding", "Alabama A-1", "Alabama A-6", "Alabama bulk filing",
  "Alabama overtime exemption W-2".
jurisdiction: US-AL
category: payroll
domain: payroll
type: filing-howto
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama payroll withholding

> **Source-cited draft.** Built from the ALDOR Withholding Bulk Filing page, read 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Alabama professional.

## Who this applies to

- Every employer paying Alabama-source wages withholds Alabama income tax on the ALDOR withholding tables (table mechanics unconfirmed).
- **Bulk filers:** "accountants or tax filing services who file withholding tax returns and payments on behalf of employers must register with ALDOR as a bulk filer and must utilize their bulk filer registration when filing withholding tax returns on behalf of their clients" (ALDOR Withholding Bulk Filing page, effective April 7, 2008). Registration is via Form BF-1, "Application to Become a Bulk Filer (Updated: 05/02/2016)".
- Payers of non-payroll compensation (pass-through distributions, certain non-resident payments) withhold under A-6 rules -- the statutory trigger is unconfirmed.
- Buyers of Alabama real estate from non-residents withhold under A-3 (percentage unconfirmed).

## Rates, bands and thresholds

| Item | Value | Tax year | Source |
|---|---|---|---|
| Withholding tables | Graduated per ALDOR tables | 2026 | Table mechanics unconfirmed |
| Bulk-filer registration | Mandatory for accountants/tax filing services filing for employers (Form BF-1) | current | [ALDOR Withholding Bulk Filing page](https://revenue.alabama.gov/taxes-fees/withholding/) |
| Bulk file types | A-1/A-6 and A-3, comma-delimited .csv or .txt | current | [ALDOR Withholding Bulk Filing page](https://revenue.alabama.gov/taxes-fees/withholding/) |
| A-1/A-6 layout change | New layout required for files uploaded after January 27, 2024 (overtime-exemption fields) | current | [ALDOR Withholding Bulk Filing page](https://revenue.alabama.gov/taxes-fees/withholding/) |

## The taxable base

- Alabama-source wages are withheld at source on the ALDOR tables (mechanics unconfirmed).
- The overtime-exemption reporting ties to Alabama's overtime-pay statute: A-1/A-6 bulk files uploaded after January 27, 2024 must carry the overtime-exemption fields. "Zeros should be entered for the 'Number of Employees with Exempt Overtime Wages' and 'Total Amount of Exempt Overtime Wages Paid' and a '1' entered in the 'No Exempt Overtime Wages Paid to Report.'" (ALDOR page; the underlying statute text is unconfirmed.)
- A-3 covers "Withholding on Sales/Transfers of Real Property and Associated Tangible Personal Property by Nonresidents" (ALDOR page menu).

## Deadlines and filing

- Bulk filings: "If uploading December 2023 returns after January 27, 2024, the bulk file must use the new file layout" (ALDOR page).
- Not yet confirmed: A-1 return and deposit frequencies, and the A-2 annual reconciliation date (previously carried as January 31).

## Penalties and interest

- Failure-to-file and failure-to-deposit penalties and interest run under the general Title 40 provisions (percentages unconfirmed). A penalty example previously carried in this skill used a 5% assumed FTD-penalty rate; that rate was an assumption and has been removed.
- Common failure modes: (1) bulk filers uploading pre-2024 layouts after the cutover (zeros + the "no exempt overtime wages" flag are required, not blank fields); (2) treating A-6 as optional for pass-through distributions; (3) A-3 missed on non-resident property sales.

## Cross-border points

- Non-resident members of Alabama-sourcing partnerships/LLCs are covered by A-6 withholding -- see `al-cross-border` (statutory trigger unconfirmed).
- Reciprocity: the prior draft asserted Alabama has no withholding reciprocity with neighboring states; unconfirmed. Remote workers trigger Alabama withholding once Alabama wages exist.

## Worked examples

Client facts in these examples are hypothetical; no unconfirmed rates are used.

**Example 1: bulk-filing volume**

A bulk filer (hypothetical) submitting 3 employers × 12 monthly A-1s in one year:

```oa-check
name: AL bulk filing volume
inputs:
  employers: 3
  months: 12
steps:
  - filings: employers * months
expected:
  filings: 36.00
```

**Example 2: A-3 withholding on a non-resident closing**

A non-resident sells Alabama real property for a hypothetical $240,000. A-3 withholding is 3% of the sales price unless an affidavit applies:

```oa-check
name: AL A-3 non-resident real estate withholding
inputs:
  sales_price: 240000
  rate: 0.03
steps:
  - withheld: sales_price * rate
expected:
  withheld: 7200.00
```

## Ask the client first

- Are bulk uploads on the post-January-2024 A-1/A-6 layout with the overtime-exemption fields populated (zeros + flag when none)?
- Is A-6 withholding being run for non-resident pass-through members?
- Are A-3 withholdings captured on non-resident real-estate closings?
- What is the current deposit frequency tier (confirm with ALDOR -- unconfirmed here)?

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR Withholding Bulk Filing page (bulk-filer registration, Form BF-1, A-1/A-6 and A-3 layouts, 2024-01-27 layout change and overtime-exemption fields) | https://revenue.alabama.gov/taxes-fees/withholding/ | 2026-10-28 |

Not yet confirmed: the A-1 withholding table mechanics and employee certificate (Form A-4); deposit frequency tiers; the A-2 annual reconciliation due date (previously carried as January 31); the A-3 withholding percentage; the statutory trigger for A-6 withholding on pass-through members (§40-18-411 et seq.); the overtime-preemption statute text behind the W-2 reporting fields; whether Alabama has withholding reciprocity with any neighboring state; the §40-2A-1 penalty percentages; the 5% late-deposit penalty rate previously carried (assumed, removed).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
