---
name: mw-income-tax
description: "Malawi draft for 2026 individual income-tax working papers, distinguishing the employment and non-employment schedules. Use it to route a taxpayer to the correct income category, reconcile supplied taxable income, apply the stated annual or monthly bands, and check the two numerical cases. It does not treat every receipt as salary or replace the taxpayer's source, residence and exemption analysis with a headline rate. Benefits, mixed income, pension deductibility, withholding finality, transitions and current filing procedures remain limited as specified in the body. This is a partial source-led computation draft, subject to the identified amendment and commencement checks and independent review."
jurisdiction: MW
tax_year: 2026
tax_year_notes: "Intended 2026 research draft; Act 3/2026 read and relevant effects identified; appointed commencement chain unresolved; live use held."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 1.3
---

# Malawi individual income tax: current salary bands v1.3

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Malawi.

## Who this applies to

**Current-year source hold.** This is a draft reconstruction of the cited provisions, not confirmed operative 2026 coverage. The enacted [Taxation (Amendment) Act 3 of 2026](https://media.malawilii.org/media/legislation/15519/source_file/2e96ab6e73cdf961/mw-act-2026-3-publication-document.pdf) has now been read in full and its relevant changes are identified in the company, individual and TP drafts. Appointed commencement notices for the Tax Administration Act and the 2021 administrative cutover remain unread; period allocation and the complete operative chain are not approved. Do not use this draft to determine an actual 2026 tax position, file, pay or complete a live registration/notice response until those checks are closed. The examples illustrate the cited-text assumptions only. The 2026 year label identifies the intended research period, not completed verification.

Use for a confirmed taxable employment-income base, or a confirmed annual non-employment taxable base, under the separate tables in the Eleventh Schedule Appendix as replaced by Act 36/2025. Source and deemed-source rules still matter; do not treat a foreign payer as automatic exemption. [Act 36/2025 s 6(c)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [Taxation 11](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content). This file does not establish residence-day tests, treaty allocation, FBT valuation or a pension deduction. It applies the current tables to 2026 calculations after both dates identified by the conflicting December notices; it does not allocate a straddling period.

## Rates, bands and thresholds

| Current table and tranche | Rate | Official source |
|---|---|---|
| Employment, first K2,040,000 annually / K170,000 monthly | 0% | [Act 36/2025 Appendix B](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [MRA VI](https://www.mra.mw/admin/storage/download_files/1767952247_NEW%20TAX%20MEASURES...pdf) |
| Next K16,800,000 annually / monthly excess above 170,000 through 1,570,000 | 30% | [Act 36 Appendix B](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [MRA VI](https://www.mra.mw/admin/storage/download_files/1767952247_NEW%20TAX%20MEASURES...pdf) |
| Next K101,160,000 annually / monthly excess above 1,570,000 through 10,000,000 | 35% | [Act 36 Appendix B](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [MRA VI](https://www.mra.mw/admin/storage/download_files/1767952247_NEW%20TAX%20MEASURES...pdf) |
| Employment annual excess above K120,000,000 / monthly excess above K10,000,000 | 40% | [Act 36 Appendix B](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [MRA VI](https://www.mra.mw/admin/storage/download_files/1767952247_NEW%20TAX%20MEASURES...pdf) |
| Non-employment annual first K2,040,000, then excess | 0%, then 30% | [Act 36 Appendix A](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content) |

The 2024/25 25% salary band is no longer in the replacement table. Apply marginal rates; do not charge 40% on the whole salary or apply employment bands to non-employment income.

## The base

Obtain an evidenced taxable base from pay and tax-adjustment records before applying the table. Include taxable remuneration under section 102/PAYE Rules; do not equate cash paid with net salary, and do not silently subtract every employee pension contribution. Ordinary pension deduction eligibility requires the current Taxation 37/Fifth Schedule conditions and scheme facts, which have not been fully reconciled here. Employer fringe benefits require their own statutory base and liability test. [Taxation 102 and PAYE Rules 3,6](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content); [2023 replacement 37](https://elibrary.rat.gov.mw/server/api/core/bitstreams/72477a6a-7348-4dd8-8a05-a7ea265a5e00/content). The cases deliberately take the confirmed taxable base as input, without inventing a deduction. Screen residential rental income and listed-share disposal proceeds separately before treating an amount as ordinary non-employment taxable income. Act 3/2026 s 3 inserts a separate final-tax rental regime with payer/entity exclusions; s 13 inserts final withholding for listed-share disposals with exemptions. Those full computations and the rent cross-reference printed as section 19(3)(a), rather than the newly inserted 18A, are unresolved here. The non-employment example assumes neither category is present. [Act 3/2026 ss 3,13](https://media.malawilii.org/media/legislation/15519/source_file/2e96ab6e73cdf961/mw-act-2026-3-publication-document.pdf).

## Deadlines and filing

For employment, the employer maintains an employee record of pay and deductions and supplies the monthly statement within fourteen days after month-end (PAYE Rule 6). Payment goes through [payroll/social](mw-payroll-social.md). The current annual return obligation/exemption for employees or other-income taxpayers is not established by quoting the old section 84(1), which the 2021 cutover deleted. Obtain the actual current prescribed return/notice and keep its acknowledgement. [PAYE Rules 6,10](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content); [Act 15/2021 Schedule 84](https://elibrary.rat.gov.mw/server/api/core/bitstreams/e43a8644-e1e1-46d8-82d7-7e80afd5fd50/content); [TAA 40](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content).

## Penalties and interest

Use the current TAA late-payment framework linked in [company tax](mw-corporate-income-tax.md), identifying employer withholding liability separately from the employee assessment. Do not use stale fixed penalties from an old PAYE brochure as current law. A bank-rate input must be current before calculating interest.

## Cross-border points

Confirm where the duties and income sources arise, any treaty and any foreign employer before computing. The ordinary table is a rate computation, not proof of resident/non-resident tax treatment for every type of income. Treaty relief and non-resident final withholding remain gaps.

## Two worked examples that recompute

Hypothetical full-month taxable employment income with no additional adjustments. The first crosses the top band.

```oa-check
name: Current monthly employment top band
inputs:
  taxable_month: 11000000
steps:
  - band30: 1400000 * 0.30
  - band35: 8430000 * 0.35
  - band40: (taxable_month - 10000000) * 0.40
  - tax: band30 + band35 + band40
expected:
  band30: 420000
  band35: 2950500
  band40: 400000
  tax: 3770500
```

Second, a hypothetical confirmed annual non-employment taxable base uses its own table, not twelve salary calculations.

```oa-check
name: Annual nonemployment table
inputs:
  taxable_year: 6000000
steps:
  - taxable_excess: max(0, taxable_year - 2040000)
  - tax: taxable_excess * 0.30
expected:
  taxable_excess: 3960000
  tax: 1188000
```

## Ask the client first

Get the taxable-pay reconciliation and pay frequency, period, each income category, source/work location and payer, pension scheme/contribution evidence, benefit arrangements, other income and withholding evidence, treaty facts, and any current MRA return/assessment notice.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [Act 36/2025](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content), s 6 Appendix A/B read in full | 2026-11-01 |
| [MRA updatednotice](https://www.mra.mw/admin/storage/download_files/1767952247_NEW%20TAX%20MEASURES...pdf), V–VI current annual/monthly tables; date wording compared with earlier notice | 2026-11-01 |
| [Taxation official-library consolidation](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content), s 11,102; PAYE Rules 3,6,10 only, not old rates | 2026-11-01 |
| [Act 17/2023](https://elibrary.rat.gov.mw/server/api/core/bitstreams/72477a6a-7348-4dd8-8a05-a7ea265a5e00/content), s 4 replacement 37 | 2026-11-01 |
| [Act 15/2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/e43a8644-e1e1-46d8-82d7-7e80afd5fd50/content), Schedule 84/102 cutover | 2026-11-01 |
| [Act 3/2026](https://media.malawilii.org/media/legislation/15519/source_file/2e96ab6e73cdf961/mw-act-2026-3-publication-document.pdf), all six pages screened, especially ss 3 and 13; separate rental/share regimes identified but not implemented in these examples | 2026-11-01 |
| [TAA 2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content), s 40 and 87 | 2026-11-01 |

**Not yet confirmed:** appointed commencement notices for TAA/cutover and full period allocation; employee pension deductibility under all current conditions; full FBT rate/base/employer liability; residence-day test and specific non-resident income rules; current employee filing exemptions/annual due date; special arrears, severance and bonus treatment; live portal boxes. The old automatic pension-before-PAYE and blanket employee-final-tax statements are not verified and are not calculation steps.

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
