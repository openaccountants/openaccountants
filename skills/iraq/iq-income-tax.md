---
name: iq-income-tax
version: 0.3
description: "Personal income tax source extracts for federal Iraq, with explicit holds on current rates, allowances and filing steps. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Personal Income Tax 0.3

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Source baseline: Income Tax Law 113 of 1982, GCT consolidation including 2004 amendments. Article 5(1) concerns a resident **Iraqi national** and income inside or outside Iraq; art. 5(2) concerns a nonresident and Iraqi-source income even if not received there; art. 5(3) excludes foreign-source income of a non-Iraqi resident. These are source-text extracts subject to IQ-CURRENT, not a residence test or treaty conclusion.

## Rates, bands and thresholds

**Historical annual scale only, IQ-CURRENT applies to every row.** Article 13(1)(a) applies the resident-individual scale after the legal allowances. The same marginal amounts appear in art. 13(1)(b) for nonresidents, subject to art. 19. No allowance entitlement is inferred from the rate scale.

| Item and source version | Amount | Official URL |
|---|---|---|
| Law 113, art. 13, 2004 consolidation, first IQD 250,000 of taxable annual income | 3% | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf |
| Same art., next IQD 250,000 | 5% | same |
| Same art., next IQD 500,000 | 10% | same |
| Same art., excess over IQD 1,000,000 | 15% | same |

The public sector 2019 allowance cases belong in [payroll](iq-payroll-social.md). Historical doubled allowances for 2010, 2011 and 2013 are not evidence of a 2026 entitlement.

## The base

Article 3 distinguishes the preceding-year basis for the art. 2(1),(2),(3),(6) income categories from the same-assessment-year basis for art. 2(4),(5), where known. It also contains source-cessation, provisional-assessment and nonresident receipt/account-credit rules. Do not turn the GCT guide's short preceding-year summary into a rule for every income category.

Expense eligibility, exemptions, personal allowances, family conditions, guideline assessments and loss relief require their own conditions. They are held below, except the loss source extract in [company tax](iq-corporate-income-tax.md).

## Deadlines and filing

Historical source workflow, subject to IQ-CURRENT: art. 27(2) requires a taxable-income report before 1 June of the assessment year, registered or unregistered, if not already requested by written or published notice. Art. 27(1) separately gives 21 days from a request; art. 27(3) permits an extension for a legitimate excuse. Article 44 requires notice of the amount and due date; art. 45 uses 21 days from notice. These extracts do not establish the current form, portal, branch submission, receipt, payment reference or extensions. Do not file using this incomplete workflow. Source: https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf.

## Penalties and interest

Held: no current penalty or interest calculation is supplied. Article 45 in the old consolidation contains additions and discretionary relief, with separate footnoted interest provisions. A bare percentage would omit the relief and other charges. See IQ-PIT-PROCEDURE below.

## Cross-border points

Use the nationality/source distinction above. Treaty eligibility, foreign-tax credits, outward payments and permanent establishments require a separate check; use the source extracts and holds in [company tax](iq-corporate-income-tax.md). No country list here establishes a treaty in force.

## Two worked examples that recompute

Arithmetic demonstrations of the historical art. 13 scale only. Both assume the stated amount is already taxable after all legally available deductions. Neither assumes an allowance or determines a 2026 bill.

At IQD 1,000,000 taxable income, the historical tax is IQD 70,000.

```oa-check
name: Historical scale to one million
inputs:
  taxable: 1000000
steps:
  - tax: 250000 * 0.03 + 250000 * 0.05 + 500000 * 0.10
expected:
  tax: 70000
```

Decision sensitivity: if a separately verified deduction reduces an already-taxable IQD 9.5m to IQD 9m, the historical-scale difference is IQD 75,000. The example does not establish that any deduction is available.

```oa-check
name: Historical deduction sensitivity
inputs:
  before: 9500000
  after: 9000000
steps:
  - first: 70000 + (before - 1000000) * 0.15
  - second: 70000 + (after - 1000000) * 0.15
  - difference: first - second
expected:
  first: 1345000
  second: 1270000
  difference: 75000
```

## Ask the client first

- Federal Iraq or Kurdistan Region, and which income and assessment year?
- Nationality, residence evidence and location of each income source?
- Employment, business, profession or another income category?
- Family circumstances, dependency evidence and other income sources?
- Books, notices, payments and any claimed foreign tax?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Law 113: PDF pp. 5–6 arts. 3–5; p. 13 art. 11; p. 16 art. 13; p. 26 art. 27; p. 33 arts. 44–46, visually read with neighbours | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT** complete later amendments and 2026 budget effects; **IQ-PIT-BASE** current expenses, exemption categories (including agriculture), allowance increases, child dependency/income/age rules, spouse merger, age relief and non-Iraqi proration; **IQ-PIT-GUIDELINES** application of the 2026 profit-guideline activities, expense treatment, multi-source reduction and continuing circulars; **IQ-PIT-PROCEDURE** registration documents, current income-report submission, objection/appeal routes, instalments, late-report cap, concealment, books penalty and all interest/additions. Earlier draft subjects remain preserved in the evidence ledger; none of these holds is a current entitlement or obligation.

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
