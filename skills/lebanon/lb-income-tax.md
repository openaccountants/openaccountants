---
name: lb-income-tax
description: "Use this Guide for Lebanon personal income tax, salary tax and business income questions in 2026. It distinguishes the annual employment and business bands and explains the business taxable base, household deduction conditions and employer withholding rule. It includes two recomputing examples that start with established taxable income. It does not establish the current salary allowance, pension treatment, treaty relief, annual return fields or a final filing date after extensions and legal suspensions. Those topics are named non-operative holds. Use the questions and cited law before calculating, and refer unresolved filing facts for Lebanese professional review."
version: 1.3
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Lebanon Personal Income Tax

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

Individuals with Lebanese business or employment income. Keep the schedules separate: Income Tax Law arts. 1-3 and 46. For wages, establish the public/private payer, residence and place of work; the old shorthand that any Lebanese funding makes every salary taxable is not a substitute for art. 46. This Guide supplies the annual bands and business base. Salary allowances, pensions and final filing remain subject to the holds below.

## Rates, bands and thresholds

Annual taxable amounts after the applicable deductions. Tax each slice, not all income at the highest rate. Budget 324/2024 arts. 46-47 replace Income Tax Law arts. 32 and 58. The 2025 tax chapter and 2026 budget amendments were screened for later changes to these bands.

| Annual taxable slice, LBP | Business rate | Employment rate | Official source |
|---|---|---|---|
| Business: first 540,000,000 | 4% | Not applicable | [2024 art. 46, p. 45](https://finance.gov.lb/en-us/Finance/BI/ABDP/Documents/Budget%202024.pdf) |
| Business: above 540,000,000 to 1,440,000,000 | 7% | Not applicable | same |
| Business: above 1,440,000,000 to 3,240,000,000 | 12% | Not applicable | same |
| Business: above 3,240,000,000 to 6,240,000,000 | 16% | Not applicable | same |
| Business: above 6,240,000,000 to 13,500,000,000 | 21% | Not applicable | same |
| Business: above 13,500,000,000 | 25% | Not applicable | same |
| Employment: first 360,000,000 | Not applicable | 2% | [2024 art. 47, pp. 46-47](https://finance.gov.lb/en-us/Finance/BI/ABDP/Documents/Budget%202024.pdf) |
| Employment: above 360,000,000 to 900,000,000 | Not applicable | 4% | same |
| Employment: above 900,000,000 to 1,800,000,000 | Not applicable | 7% | same |
| Employment: above 1,800,000,000 to 3,600,000,000 | Not applicable | 11% | same |
| Employment: above 3,600,000,000 to 7,200,000,000 | Not applicable | 15% | same |
| Employment: above 7,200,000,000 to 13,500,000,000 | Not applicable | 20% | same |
| Employment: above 13,500,000,000 | Not applicable | 25% | same |

## The base

For business income, reconcile receipts and evidenced expenses needed for the business, then adjustments, the applicable art. 31 personal deduction and the bands. Personal spending is not a business deduction (Income Tax Law art. 7). The 2024 art. 49 amendment sets the business deduction at LBP 450 million, adding LBP 225 million for a qualifying spouse and LBP 45 million per dependent child, at most five. Apply the household conditions on pp. 48-49 beside these amounts: a dependent male child must be no older than eighteen, or no older than twenty-five while pursuing university study; the separate disabled-male-child rule requires no paid work and the specified Ministry of Social Affairs disability certificate. A dependent female child qualifies before marriage, or if widowed or divorced. If both spouses work, each gets the single deduction and the child deductions are shared equally. For legal separation, the husband legally required to pay maintenance receives the deduction. If the father does not work for wages and the mother carries on a taxable profession or job, she receives her own single deduction plus the full spouse and child deductions under that paragraph. Obtain evidence for the applicable child status and household allocation before deducting; do not infer eligibility from the amounts. Do not automatically reuse these business deductions for salary: the salary deduction and its later amendments remain hold PIT-H1.

For wages, art. 49 includes cash and benefits in kind, and art. 50 describes deductions. Use an evidenced taxable base; gross wages are not the taxable band input. If the person also has business income, art. 57 prevents a second personal deduction under the salary schedule. Do not issue a final salary computation while PIT-H1 is unresolved.

## Deadlines and filing

Employers withhold. Income Tax Law art. 63 as replaced by 2025 budget art. 17 requires remittance every three months by the fifteenth of the next month; foreign-currency pay uses the BDL rate at each month end and is remitted in LBP. No numeric exchange rate is supplied here. The old R10 annual-return claim is wrong: the Ministry index distinguishes annual R5/R6/R7 from periodic R10. Current portal fields, annual form, payment reference, extensions and suspension effects are hold PIT-H2. Prepare the reconciliation and stop before submission until those are obtained.

## Penalties and interest

Hold PIT-H3 covers the applicable filing/payment penalties. Budget 2026 art. 18 is about beneficial-owner declarations, not a general payroll penalty. Do not apply its figures to an ordinary late income return. The temporary art. 43 settlement is held pending the publication date and later deadline-suspension analysis.

## Cross-border points

Determine source, residence and payer under art. 46 before selecting the salary schedule. Treaty relief, non-resident remittance rules and pension treatment are hold PIT-H4. NSSF belongs in [Payroll and social contributions](lb-payroll-social.md); company profit and import advances in [Corporate income tax](lb-corporate-income-tax.md).

## Two worked examples that recompute

Business taxable profit, already after allowable deductions, is LBP 900 million. The first slice costs LBP 21.6 million and the next LBP 25.2 million, total LBP 46.8 million.

```oa-check
name: Business taxable profit 900 million
inputs:
  base: 900000000
steps:
  - first: min(base, 540000000) * 0.04
  - second: max(min(base, 1440000000) - 540000000, 0) * 0.07
  - tax: first + second
expected:
  tax: 46800000
```


Classification decision: two separately established taxable bases of LBP 900 million produce different results. Employment costs LBP 28.8 million; business costs LBP 46.8 million. The LBP 18 million difference is why the income character must be evidenced. These are annual taxable-base examples, not gross-to-net salary calculations or an election to relabel employment.

```oa-check
name: Employment versus business character
inputs:
  employment_base: 900000000
  business_base: 900000000
steps:
  - salary_tax: 360000000 * 0.02 + (employment_base - 360000000) * 0.04
  - business_tax: 540000000 * 0.04 + (business_base - 540000000) * 0.07
  - difference: business_tax - salary_tax
expected:
  salary_tax: 28800000
  business_tax: 46800000
  difference: 18000000
```


## Ask the client first

- What is the income character, payer, residence and place of work?
- What is the taxable year and evidenced business or salary base?
- Is the spouse working, and who claims each qualifying child and personal deduction?
- What currencies and monthly conversion records were used?
- Are there multiple employers, pensions, foreign receipts or overdue declarations?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| Income Tax Law 144/1959, arts. 1-3, 7, 11-14, 46, 49-50, 57-59; only these clauses and neighbours read; older consolidation | https://www.finance.gov.lb/en-us/Taxation/LRT/Documents/%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9%20%D8%A7%D9%84%D8%AF%D8%AE%D9%84.pdf | 2026-11-01 |
| Budget 324/2024, arts. 46-49, pp. 45-49; amounts read from page images | https://finance.gov.lb/en-us/Finance/BI/ABDP/Documents/Budget%202024.pdf | 2026-11-01 |
| Budget 2025, Decree 56/2025, tax chapter arts. 16-53, PDF pp. 27-71; amendment headings screened, art. 17 read in full | https://finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%202025.pdf | 2026-11-01 |
| Budget 40/2026, arts. 16-18, 27-35, 40-43, 51-52 and closing art. 57; relevant clauses and neighbours read, annexes not read | https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf | 2026-11-01 |

Not yet confirmed: PIT-H1: current salary personal allowances, disability relief, part-year allocation and gross-to-net computation. PIT-H2: annual forms/boxes, portal/payment sequence, 2026 extensions and legal-suspension effect. PIT-H3: current late-filing/payment penalties and any available settlement. PIT-H4: pension rate reduction, treaty relief and non-resident collection frequency. These holds are non-operative; historical claims and every replaced item remain in the per-Guide ledger and immutable Git versions.

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
