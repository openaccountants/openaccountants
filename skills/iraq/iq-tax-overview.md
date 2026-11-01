---
name: iq-tax-overview
version: 0.3
description: "Federal Iraq tax-job routing and a limited property-rent source extract, with explicit limits on current law and inherited formation material. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Tax Overview 0.3

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Research router for federal Iraq questions, not an end-to-end country filing manual. Route income tax, company tax, payroll and consumption tax to their existing job Guides. Property rent is retained here as an authority-page source extract. Obtain separate Kurdistan Region advice rather than assuming this pack applies there.

## Rates, bands and thresholds

**Undated GCT property-page extract only, subject to IQ-CURRENT and IQ-PROPERTY.**

| Source scope and condition | Page amount | Official URL |
|---|---|---|
| GCT guide describing Law 162/1959 as amended, rented property, annual rent after stated maintenance/depreciation deduction | 10% tax after a 10% deduction, equivalent to 9% of annual rent | https://tax.mof.gov.iq/%D8%AF%D9%84%D9%8A%D9%84-%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9-%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%B1/ |

This undated webpage does not prove that later amendments left these figures unchanged. Income, company, public-sector payroll and historical sales-tax figures stay in their owning Guides; the overview does not duplicate their rates.

## The base

Route by the underlying transaction: [personal income](iq-income-tax.md), [company income](iq-corporate-income-tax.md), [payroll/social](iq-payroll-social.md), [VAT/sales](iq-vat-gst.md). For property, distinguish recurring rent, sale/transfer, vacant land, owner occupation, demolition and subdivision. The source page discusses different procedures for those subjects; the rent formula cannot be used for a transfer or land valuation.

## Deadlines and filing

The GCT property guide's rent-payment sequence is branch review, basic-tax collection form, additional-tax debt check, audit and manager review, cash-office receipt, then posting the receipt to the basic-tax records. It allows payment of annual rent tax in one instalment during the year, or two instalments with the first half-year and second half-year windows. This is a page description, not confirmation of current deadlines or a complete property-filing instruction. Current forms, electronic options, references and all transfers remain held.

## Penalties and interest

No country-wide penalty figure belongs in this router. Use the underlying job and its specific procedural hold. The property page contains late interest and objection periods; neither is cleared as current law here.

## Cross-border points

Use [Iraq tax routing](iraq-tax.md) for cross-border and transfer-pricing intake holds. Nationality and source matter; do not call federal Iraq uniformly territorial. Oil contracts, foreign credits, permanent establishments and treaty status require their owning source and conditions.

## Two worked examples that recompute

Property arithmetic from the undated authority page, explicitly conditional on that source formula applying. These examples do not clear currentness, exemptions or ownership allocation.

At annual rent IQD 12m, the page formula produces IQD 1.08m.

```oa-check
name: GCT property page illustration
inputs:
  rent: 12000000
steps:
  - tax: (rent - rent * 0.10) * 0.10
expected:
  tax: 1080000
```

Decision sensitivity: two proposed annual rental receipts of IQD 12m and IQD 10m produce historical-page amounts of IQD 1.08m and IQD 0.9m, a difference of IQD 180,000. Compare net receipts only after verifying costs and legal treatment; this is not a recommendation to choose a lease.

```oa-check
name: Property receipt sensitivity
inputs:
  rent_a: 12000000
  rent_b: 10000000
steps:
  - a: rent_a * 0.9 * 0.10
  - b: rent_b * 0.9 * 0.10
  - difference: a - b
expected:
  a: 1080000
  b: 900000
  difference: 180000
```

## Ask the client first

- Location and relevant year, including federal/Kurdistan distinction?
- Person, company, employer, importer or property owner?
- Exact income, payment or transaction type?
- Property rent, transfer, vacant land or use change?
- Actual notices, forms, contracts and proof of payments?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| GCT property guide: main text read, basic rent formula and payment sequence plus neighbouring transfer/land/use-change procedures; undated authority guidance | https://tax.mof.gov.iq/%D8%AF%D9%84%D9%8A%D9%84-%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9-%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%B1/ | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT** source currentness through 2026; **IQ-PROPERTY** amended Law 162/1959, exemptions, additional-tax treatment, present rates, instalment dates, late interest and appeals, transfer Law 48/2015, valuation and vacant-land rules; **IQ-OVERVIEW-ADMIN** assessment/calendar-year basis, complete authority/remit/language/currency and current workflow for each job. The existing company-formation Guide remains an inherited 2025 research hold, not evidence of current incorporation requirements. All seven core tax jobs remain partial as the README states.

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
