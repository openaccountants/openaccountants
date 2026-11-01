---
name: mw-company-formation
description: "Malawi 2026 tax-registration handoff for a newly established business, TIN controls and tax-type routing; company-law incorporation conditions remain explicit gaps."
jurisdiction: MW
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v 1.0 (content)
category: formation
version: 1.0
---

# Malawi company formation: tax-registration handoff v 1.0

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Malawi.

## Who this applies to

Use to prepare the tax-registration handoff for a newly established company/business. TAA 21(1) requires a business that becomes potentially liable under a tax law to apply for taxpayer registration. This verifies a tax job; it does not validate the company’s legal incorporation, shareholder/director rules or registry fees. [TAA 21](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content). Keep the existing incorporation documents and current registry requirements as inputs rather than assuming a certificate settles tax registration.

## Rates, bands and thresholds

| Tax-registration condition | Statutory rule | Official source |
|---|---|---|
| Successful registration application | TIN issued within 14 days of receipt through service of certificate | [TAA 22(1)–(2)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |
| TIN identity/control | One personal TIN at a time, used across tax laws; not transferable | [TAA 22(3)–(5)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |
| Change to TIN-certificate details | Written notification within 21 days | [TAA 22(7)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |
| Separate VAT enrolment | Apply the current scope in [VAT](mw-vat-gst.md); company registration alone is insufficient | [Act 5/2026 s 4](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content) |

The 14-day TIN provision is not a promised incorporation time. No minimum company capital, shareholder cap, director number or setup fee is verified in this table.

## The base

Identify the actual legal taxpayer, true identity and existing TIN before preparing the application. Do not create a new company tax identity by reusing a shareholder’s TIN. Reconcile the legal name, incorporation evidence, registered/business addresses, activity, contact details and authorized person against source documents. The prescribed application must be accompanied by the prescribed documentary evidence under 21(4); obtain the actual current form rather than invent a fixed attachment list. [TAA 21–22](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content). Share-allocation arithmetic below is only a consistency check on supplied records, not a statement of Malawi minimum capital.

## Deadlines and filing

Check for an existing TIN; assemble the current prescribed registration form and documentary identity evidence; resolve inconsistencies; submit through the actual MRA registration channel; retain submission proof; obtain the TIN certificate and verify the legal person/details. Under 22(5), true identity and no existing TIN are conditions to issuance. Use that TIN on tax claims, notices, returns and statements under 23(1). Notify certificate-detail changes in writing within 21 days. Then determine company-income-tax, VAT, payroll/pension and licence obligations separately with their own sources. [TAA 21–23](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content). The actual registry sequence, portal fields and tax-type activation acknowledgements remain outside this verified handoff.

## Penalties and interest

TAA 22(6) allows the Commissioner General to register a taxpayer that failed to register for appropriate tax types;23 prohibits false representation of a TIN. Tax registration does not cure missed filings or payments. Do not quote an unverified registry penalty or current company filing fee. [TAA 22–23](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content).

## Cross-border points

If a non-resident with no fixed place of business is required to register, TAA 28(2) requires a representative taxpayer in Malawi. That is a tax representation rule; it does not prove a company-law resident-director requirement or a treaty residence result. [TAA 28(2)](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content).

## Two worked examples that recompute

Hypothetical capital amounts supplied in incorporation records, equal-rights cash shares only. These are arithmetic consistency controls, with no asserted statutory minimum or filing fee.

```oa-check
name: Share allocation reconciles supplied capital
inputs:
  shares_a: 60
  shares_b: 40
  nominal: 1000
steps:
  - shares: shares_a + shares_b
  - capital: shares * nominal
expected:
  shares: 100
  capital: 100000
```

```oa-check
name: Single shareholder supplied capital
inputs:
  shares: 500
  nominal: 200
steps:
  - capital: shares * nominal
expected:
  capital: 100000
```

## Ask the client first

Get incorporation/legal-form evidence, shareholder/director consents and identity as required by the actual registry, legal name/address/activity, existing TINs, intended tax types, authorized representative and contact details, payroll/fund facts, current registry form/fee schedule and MRA registration requirements.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [TAA 2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content), ss 21–23 and 28(2) read in full | 2026-11-01 |
| [VATAct 5/2026](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content), s 4 registration categories | 2026-11-01 |

**Not yet confirmed:** CompaniesAct 2013 primary text and current incorporation authority mandate; private/public/guarantee/partnership/branch rules; minimum capital, maximum 50 members, director/residence requirement, name reservation/consent forms, exact incorporation steps/timing, registry fees, annual return/AGM/accounts rules. CRIPC official home failed direct DNS and browser DNS on this read; no successful live read is claimed. The old VAT K25 m and 180-day annual-tax claims are superseded or unresolved as stated in the owning Guides.

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
