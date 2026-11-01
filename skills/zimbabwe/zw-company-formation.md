---
name: zw-company-formation
description: >
  Company formation and entity choice in Zimbabwe, tax year 2026: Pvt Ltd, private business corporation, other entities, and tax registration after incorporation. Company law items are marked unverified because the Companies and Other Business Entities Act was not opened in this update.
version: 1.0
jurisdiction: ZW
category: formation
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---
# Zimbabwe Company Formation & Entity Choice

## Entity types and incorporation

- **Governing legislation**: unverified: Companies and Other Business Entities Act (Chapter 24:31)  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Private Limited Company (Pvt Ltd)**: unverified: Separate legal entity; shareholders' liability limited to shares; commonly 1+ directors (historically a minimum of 2) ((approx - confirm current minimum director count))  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Private Business Corporation (PBC)**: unverified: Simplified entity with 1 to 20 members; requires an accounting officer; at least one Zimbabwean member  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Other entity types**: unverified: Public limited company, partnership, sole trader, co-operative, and registered branch of a foreign company  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Minimum share capital**: unverified: No statutory minimum; share capital can be set as low as USD 1 (number and class of shares stated at incorporation) USD  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Name search and reservation**: unverified: Submit a name-search application to DCIP; an approved name is reserved before incorporation  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Incorporation documents**: unverified: Pvt Ltd: lodge memorandum and articles (CR forms) with director/shareholder details; PBC: lodge a statement of incorporation (PBC2) naming members, contributions and accounting officer  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Typical incorporation timeline**: unverified: Approximately 1-4 weeks depending on name approval and document processing ((approx - confirm current DCIP turnaround))  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Indicative registration cost**: unverified: PBC from around USD 70 (up to ~USD 140 with member certificates/by-laws); Pvt Ltd costs vary with capital and agent fees ((approx - fees change; confirm current schedule)) USD  _(Companies and Other Business Entities Act (Chapter 24:31))_
- **Post-incorporation tax registration:** Register in TaRMS for a TIN, for VAT if taxable supplies exceed USD 25,000 ([VAT](zimbabwe-vat.md)), and for PAYE and NSSA if employing staff.
- **Core annual compliance:** ITF12C and QPDs: see [corporate income tax](zw-corporate-income-tax.md). unverified: annual return with DCIP and statutory records.
- **Annual return obligation**: unverified: Registered entities must lodge an annual return with DCIP each year to remain in good standing  _(Companies and Other Business Entities Act (Chapter 24:31))_

## Two worked examples that recompute

VAT after incorporation: expected taxable supplies of USD 30,000 in 12 months against the USD 25,000 threshold are USD 5,000 over, so the new company registers.

```oa-check
name: VAT registration test for a new company
inputs:
  expected_supplies: 30000
  threshold: 25000
steps:
  - excess: expected_supplies - threshold
expected:
  excess: 5000.00
```

Decision: company or sole trader on USD 100,000 of taxable trade income. Both pay 25% plus the 3% AIDS levy, so the choice does not change that tax; dividends and liability decide it.

```oa-check
name: Company against sole trader, income tax only
inputs:
  profit: 100000
steps:
  - company: profit * 0.25 * 1.03
  - individual: profit * 0.25 * 1.03
  - difference: company - individual
expected:
  company: 25750.00
  difference: 0.00
```

## Sources

| Source | URL | Read on |
|---|---|---|
| ZIMRA VAT Registration page | https://www.zimra.co.zw/domestic-taxes/vat/vat-registration | 2026-11-01 |
| ZIMRA Tax Rates page | https://www.zimra.co.zw/domestic-taxes/corporate/tax-rates | 2026-11-01 |

Not yet confirmed: every line marked unverified; the Companies and Other Business Entities Act [Chapter 24:31] and DCIP fees were not opened.

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
