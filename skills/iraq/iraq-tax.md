---
name: iraq-tax
description: "Federal Iraq intake routing across seven tax jobs, preserving transaction-review flags while holding unsupported tax, exemption and filing conclusions. Use this Guide when a question mentions federal Iraq, the General Commission for Taxes, GCT Baghdad, or Iraqi dinar tax. It identifies the source version, the evidence actually read, the conditions attached to its extracts, the facts needed from the taxpayer, and the unresolved matters that stop a current filing calculation. It does not cover the Kurdistan Region. Follow the linked country Guides for the underlying job and keep every stated hold attached to any answer."
version: 2.2
jurisdiction: IQ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iraq Tax Routing 2.2

> **General reference.** Source extracts and research holds only. This Guide does not establish the law currently in force for a filing.

Tax year: 2026 is the question-routing year, not a certification that these older instruments remain unchanged. **IQ-CURRENT hold:** the complete later-amendment and commencement chain through 2026 has not been established. The extracts below describe only the named source version. Do not use their figures for a current liability until that hold is closed.

## Who this applies to

Use this intake router for federal Iraq questions spanning individual tax, company tax, consumption tax, payroll, social contributions, transfer pricing or cross-border income. This is a routing recommendation, not a legal classification. A bank statement alone does not establish residence, source, beneficial ownership, exemption or filing obligations.

## Rates, bands and thresholds

| Routing item | Evidence needed | Source or status |
|---|---|---|
| Tax rates and thresholds | Use owning job Guide, retaining its currentness hold | unverified: no current rate list in this router |
| Transfer pricing | Related parties, contracts, pricing method and relevant countries/periods | unverified: operative law and documentation workflow held |
| Cross-border | Nationality/residence, source, PE, payment type, country and treaty evidence | unverified: country-specific current-law conclusion held |

## The base

Recommended workflow: classify the transaction using contracts and invoices before computing. Route ordinary individual income to [income tax](iq-income-tax.md), company profit/loss to [company tax](iq-corporate-income-tax.md), employment to [payroll/social](iq-payroll-social.md), goods/services to [consumption tax](iq-vat-gst.md), and property to [overview](iq-tax-overview.md). Retain oil, agriculture, e-commerce and KRI as explicit classification questions; do not reuse the old automatic exemption, tax or escalation-tier conclusions.

Bank pattern preservation: RASHEED BANK, RAFIDAIN BANK, TRADE BANK OF IRAQ/TBI, INTEREST, LOAN, GCT/GENERAL COMMISSION FOR TAXES, CUSTOMS and SOCIAL SECURITY are review flags only. Never auto-exclude transactions because a bank or authority name occurs in the description. Inspect principal, interest, fees, counterparties, liability and receipts. The former EXCLUDE tables are superseded, with exact predecessor bytes retained in the evidence directory.

## Deadlines and filing

Recommended order: collect period and location; identify the taxpayer and transaction; find the owning Guide and source version; close its specific legal/currentness hold; obtain the actual current form/portal and notice; prepare and reconcile; obtain competent sign-off; submit only through the confirmed channel; retain confirmation, payment reference and receipt. If any step lacks evidence, stop that filing step and record what is missing. This router supplies no universal due date or Arabic-document rule.

## Penalties and interest

No penalty engine is authorised by this router. Identify the specific tax, notice, event, date, interest basis, relief and appeal provisions in the applicable source before any computation. Owning Guides retain the procedural gaps.

## Cross-border points

**IQ-TP / IQ-XB:** collect group structure, relationship/control, countries, contracts, services/goods/finance, pricing method, year, residence certificates and any PE facts. No transfer-pricing threshold, method, return, documentation date, treaty rate or PE conclusion is cleared here. An ordinary foreign contractor is not automatically taxed like an oil contractor, and a foreign bank description is not an exemption. Keep the source extracts in company tax distinct from current-law advice.

## Two worked examples that recompute

Intake arithmetic only, using user-supplied evidence counts. These are not tax rates or legally required document counts.

A client lists 12 relevant transactions and supplies supporting documents for 9. Three need evidence before classification.

```oa-check
name: Evidence reconciliation
inputs:
  transactions: 12
  supported: 9
steps:
  - missing: transactions - supported
expected:
  missing: 3
```

Decision: option A has 6 unsupported classifications; option B has 2. Resolving B still leaves 2 open and improves the evidence count by 4. This does not make either filing ready or establish that fewer documents satisfy a law.

```oa-check
name: Evidence resolution decision
inputs:
  missing_a: 6
  missing_b: 2
steps:
  - improvement: missing_a - missing_b
  - remaining: missing_b
expected:
  improvement: 4
  remaining: 2
```

## Ask the client first

- Taxpayer/entity, nationality/residence and relevant period?
- Federal Iraq, Kurdistan Region and other countries involved?
- Exact income, transaction, counterparty and supporting documents?
- Related parties, oil contract, PE, employment or property facts?
- Prior filings, authority notices, registrations and disputed items?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Law 113: PDF pp. 5–6 arts. 3–5 and p. 13 art. 11 read with neighbours, source baseline informing the nationality/source/loss routing; no complete 2026 currentness chain | https://tax.mof.gov.iq/uploads/Najwan/law/Income-Tax-Law-No.-113-of-1982-Ar.pdf | 2026-11-01 |

Not yet confirmed: **IQ-CURRENT** complete current law; **IQ-TP** transfer-pricing legal basis, scope, methods, thresholds and full documentation/filing workflow; **IQ-XB** residence/PE/source tests, current treaties and payment-specific rules; **IQ-ROUTER-LEGACY** agricultural exemption scope, ordinary foreign-contractor result, oil classification, VAT/GST absence, registration, reverse charge, input credits, digital supplies and KRI dual-filing claim. Old sample answers/tests, mandatory Arabic-books instruction and broad tax prohibitions are superseded holds, not operative answers. Current forms, deadlines, sanctions and sign-off requirements must be established job by job. Historical source extracts are not proof that an obligation is absent.

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
