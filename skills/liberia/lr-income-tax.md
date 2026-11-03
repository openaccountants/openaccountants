---
name: lr-income-tax
description: "Computes resident personal income tax in Liberia for 2026 from the statutory annual LRD bands, identifies residence and first-arrival conditions, separates employment collection from return obligations, and tests ordinary income, exclusions and disposal gains. Use for Liberian salary tax, individual income tax, a first arrival, a resident business owner, capital gains or an annual personal return. The Guide distinguishes statutory zero-band relief from a second deduction and routes payroll contributions and nonresident withholding to their own Guides. It is a source-cited draft with explicit gaps for pension deductibility, detailed reliefs, current forms and unusual assignment residence cases; no accountant has attested it."
jurisdiction: LR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Liberia Personal Income Tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Read on: 2026-11-01. Source-cited country draft; currentness gaps are listed below.

## Who this applies to

Resident natural persons and advisers preparing a 2026 working paper. A nonresident is not assigned the resident table merely because the employer is Liberian. Residence arises from normal abode plus presence at any time, more than 182 days in a twelve-month period ending in the tax year, or government posting abroad. Prior-year nonresidents are excluded for the period before first arrival. Section 800(c) has express non-presence exclusions, including its wording for entry to perform employee services, transit, medical treatment/full-time study and diplomatic presence; do not use a bare 183-day test for an assignee. [s 800(a)–(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I08]

## Rates, bands and thresholds

| Rule | Condition and result | Official source |
|---|---|---|
| I01 | Resident annual taxable income through LRD 70,000: nil. | [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I01] |
| I02 | Resident annual taxable income over LRD 70,000 through 200,000:5% of excess over 70,000. | [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I02] |
| I03 | Resident annual taxable income over LRD 200,000 through 800,000:6,500+15% of excess over 200,000. | [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I03] |
| I04 | Resident annual taxable income above LRD 800,000:96,500+25% of excess over 800,000. | [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I04] |
| I05 | The LRD 70,000 standard deduction is already reflected in the zero band. Do not deduct it again before using the table. | [s 205(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I05] |

## The base

Resident gross income includes worldwide economic benefits, including employment cash/noncash benefits, business receipts, nonexempt investment income, pensions and gains on investment/business property. Deduct only statutory exclusions, deductions and allowances. [s 201(a)–(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I06]

Statutory exclusions include qualifying sickness/disability/death receipts and gifts/transfers by death. Noncash employee benefits are valued at fair market value with only aggregate excess over LRD 100,000 included; personal-use property gain exclusion ends when disposal proceeds reach LRD 1,600,000. Read each exception before treating a receipt as exempt. [s 202(a)–(f)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I07]

Taxable disposal gain/loss starts with proceeds less adjusted tax cost. Gifts, death transfers, personal-use exclusions, rollovers and investment-loss restrictions require their own tests; there is no separate universal flat capital-gains rate in this Guide. [s 207(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I11]

Statutory dollar amounts are LRD unless expressly denominated otherwise. Books can be in LRD or USD, but USD books must show LRD taxable-income and tax equivalents. USD payment translates LRD due at the CBL market rate on payment day; other foreign-exchange translations follow s 6(c). [s 6(a),(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [O03]

Start with annual gross income, classify exclusions and costs, establish taxable income, then apply exactly one table formula. The employee NASSCORP deduction asserted in the old Guide has not been established from the law read and is withheld. Use the [corporate/business Guide](lr-corporate-income-tax.md) for presumptive-business classification; do not use salary bands for a business that must use that regime.

## Deadlines and filing

A resident with taxable income generally files; the exception includes 90% or more gross income from employment subject to withholding and s 200(c) taxpayers. Eligible persons can elect to file to claim losses, deductions or credits. Small/petty-trader requirements differ. [s 900(a)–(d)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I09]

Income return and final payment are due by the last day of the third month after the tax year, March 31 for a calendar year. [s 902](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I10]

For employment collection use [Payroll](lr-payroll-social.md). The public catalogue names Salary/Wages Schedule A and a monthly withholding return; the individual annual form and actual boxes remain unconfirmed. Use the official [LRA Forms and Schedules](https://www.lra.gov.lr/forms-and-schedules/) catalogue and [LITAS](https://elitas.lra.gov.lr/) link published by LRA. Select the tax kind, year and TIN; reconcile the return with the working paper and withholding credits; submit the applicable return and schedules, pay against the resulting reference and preserve submission/payment confirmation. The public catalogue was read; live portal screens, box numbers, payment references and a successful filing have not been verified. Stop before submission if the live workflow differs. [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07]

## Penalties and interest

For the general late-filing, late-payment, recordkeeping and interest rules, use [Tax overview](lr-tax-overview.md#penalties-and-interest). Do not invent a fixed interest rate or treat a civil late-payment charge as a criminal conviction.

## Cross-border points

Worldwide income applies to residents, subject to statutory exclusions. Use [Cross-border](lr-cross-border.md) for source, foreign tax credits and treaty conditions; a universal flat nonresident individual rate is not supported. [s 201(a)–(c)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I06]

## Two worked examples that recompute

### Resident income of LRD 500000

Assume LRD 500,000 is established taxable income after verified adjustments. The third band gives 6,500 + 15% × 300,000 = LRD 51,500. The zero bracket is already inside the formula. [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I03]

```oa-check
name: Resident income of LRD 500000
inputs:
  taxable: 500000
steps:
  - tax: 6500 + (taxable - 200000) * 0.15
expected:
  tax: 51500
```

### Avoid deducting the zero band twice

At LRD 900,000 taxable income the lawful table produces LRD 121,500. Deducting another LRD 70,000 would incorrectly give 104,000, an understatement of 17,500. Use the lawful calculation. [s 200(a) table](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I04] [s 205(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [I05]

```oa-check
name: Avoid deducting the zero band twice
inputs:
  taxable: 900000
steps:
  - correct: 96500 + (taxable - 800000) * 0.25
  - incorrect: 96500 + (taxable - 70000 - 800000) * 0.25
  - understatement: correct - incorrect
expected:
  correct: 121500
  incorrect: 104000
  understatement: 17500
```

## Ask the client first

- Abode, arrival/departure and presence days, including the reason for each stay.
- Employment, business, investment and foreign income; cash/noncash benefits and disposal costs.
- Payroll withholding, other credits, prior returns and presumptive-business status.
- Evidence supporting an exclusion, pension deduction or loss.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| December 2024 general amendment, approved 17 December/printed 20 December 2024, substantive pages 1–9 | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| Revenue Code 2020, selected general, income, nonresident, filing and GST provisions | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA Forms and Schedules, named return/schedule links read; not a completed portal filing | https://www.lra.gov.lr/forms-and-schedules/ | 2026-11-01; read in part, specific scope in first column |
| December 2025 amendment, approved 24 March/printed 1 April 2026, cover/preliminary/amended 63,74,76,79,90–92,803,805,806,1000,1021; excise schedule not used | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |

Not yet confirmed: Employee pension deductibility; practical interpretation of s 800(c)(1) employee-entry non-presence wording; full medical-credit and benefit valuation computations; current annual individual form/boxes; every subsequent inflation adjustment and special regime.

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
