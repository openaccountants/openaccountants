---
name: cg-tax-overview
description: "Route Republic of Congo company, individual, VAT, payroll, formation, transfer-pricing and cross-border questions to the correct 2026 initial-law reference Guide. Explains the new income-tax architecture, source hierarchy, accounting period and unresolved operational/currentness limits. This is a source-cited research draft for the Republic of Congo, country code CG, using fetched official law and authority material. The initial 2026 statutory baseline is distinguished from unresolved later amendments and operating procedures. Trigger phrases include Congo-Brazzaville tax, tax calculation, tax return, source verification and country compliance. It is general reference, with explicit partial coverage and no accountant attestation. Use the linked country Guides for related jobs and obtain the missing facts before calculating or filing."
jurisdiction: CG
category: international
tax_year: 2026
tax_year_notes: "Initial 2026 enacted-law baseline; later 2026 currentness and filing procedures remain partial"
last_updated: 2026-11-01
version: 1.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Republic of Congo Tax Overview v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Draft scope:** Republic of Congo(CG, Congo-Brazzaville), not Democratic Republic of Congo(CD). This is a pack router and initial-law reference, not comprehensive 2026 coverage or accountant attestation. Independent pack review is pending. Initial 2026 law is not represented as a fully consolidated or operational 2026 position.

## Who this applies to

Republic of Congo(CG, Congo-Brazzaville), not Democratic Republic of Congo(CD). This is a pack router and initial-law reference, not comprehensive 2026 coverage or accountant attestation.

## Rates, bands and thresholds

| Item | Treatment | Authority |
|---|---|---|
| Linked computations | Use the owning Guide linked below; no separate headline rate is created here. | [Initial 2026 Finance Act](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf) |

## The base

For a legal entity start with [corporate tax](cg-corporate-income-tax.md); for salary, business, rent or investment receipts use [income tax](cg-income-tax.md). [VAT](cg-vat-gst.md) owns VAT rates and input restrictions; [payroll/social](cg-payroll-social.md) records social conflicts. [Formation](cg-company-formation.md), [TP](cg-transfer-pricing.md) and [cross-border](cg-cross-border.md) handle their separate jobs. Amounts in examples below import those owners' rules, not alternative pack rates.

| Item | Rule and conditions | Authority |
|---|---|---|
| 2026 tax architecture | The enacted initial 2026 Finance Act transposes the CEMAC income-tax directive into a new IS chapter and separate business, investment, property and salary income chapters. Use the Guides by taxpayer and receipt category, rather than the former single global IRPP shortcut. | [FinanceAct47](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger O01 |
| Preserve source hierarchy | The 2026 law's final 61 retains prior execution provisions only insofar as not contrary to it. 62 provides publication and execution as State law. An unsigned draft, historical CGI compilation or administrative calendar cannot silently displace the enacted text. Later 2026 rectification remains unverified. | [FinanceAct61–62](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger O03 |

## Deadlines and filing

Build a calendar from the actual taxpayer regime, return type and verified statutory/administrative instruments. The corporate Guide records the 4 month/15May contradiction. Actual portals, forms, boxes and acknowledgements are not fully verified. Pack presence is not proof that filing can be executed.

| Item | Rule and conditions | Authority |
|---|---|---|
| Annual accounting period | CGI 9 ordinarily requires 31December accounts; 86 allows a first extended period for enterprises beginning in the final 6 months, with option notified before 31December of the commencement year. This is an option with conditions, not permission for every taxpayer to choose any year-end. | [CGI9,86](https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf); ledger O02 |

## Penalties and interest

Apply each Guide's specific default trigger. Do not reuse a TP documentary fine for payroll, a foreign special-regime daily charge for ordinary tax, or voluntary correction as a universal penalty waiver.

## Cross-border points

Company residence, PE, individual category source and treaty relief are different tests. Select the cross-border and income Guides before computing; foreign ownership alone is not a PE conclusion.

## Two worked examples that recompute

### 1. Compare business and company computations before distributions

Assume ordinary domestic company and ordinary IBA individual each have independently reconciled profit 10,000,000 and minimum receipts 100,000,000. Corporate C01/C08 gives 2,800,000 versus minimum 1,000,000. IBA I02 gives 3,000,000 versus minimum 1,500,000. Difference 200,000 is before distributions, social charges, other levies and compliance costs. It does not by itself decide incorporation.

```oa-check
name: Compare business and company computations before distributions
inputs:
  profit: 10000000
  receipts: 100000000
steps:
  - company_is: max(profit * 0.28, receipts * 0.01)
  - individual_iba: max(profit * 0.30, receipts * 0.015)
  - difference: individual_iba - company_is
expected:
  company_is: 2800000
  individual_iba: 3000000
  difference: 200000
```

### 2. Decision: route centimes to VAT, not a blanket profit surtax

An ordinary VAT invoice with pretax base 1,000,000 needs VAT 180,000 and centimes 9,000 under V01. A system configured for VAT alone totals 1,180,000; correctly including centimes totals 1,189,000. Correct the invoice configuration by 9,000. This VAT rule does not substantiate the old blanket 5% surcharge on every profit-tax bill.

```oa-check
name: Decision: route centimes to VAT, not a blanket profit surtax
inputs:
  base: 1000000
steps:
  - vat_only_total: base * 1.18
  - vat: base * 0.18
  - centimes: vat * 0.05
  - correct_total: base + vat + centimes
  - underbilling: correct_total - vat_only_total
expected:
  correct_total: 1189000
  underbilling: 9000
```

## Ask the client first

- Country code, taxpayer/legal form and precise tax year?
- Income/supply type, source, residence and actual activity?
- Turnover, assets, employees and accounting period?
- Treaties, permits, group relationships and incentives?
- Prior filings, notices and official payment evidence?

## Sources

| Source and portion actually read | Official URL | Read on |
|---|---|---|
| Finance Act 42-2025, official gazette special 3-2026. Enacted initial 2026 law: cover; art 5; art 47 replacement CGI 2–11,15–19,21,25,42,45–49,69–86A,86C–G,92–92E,93–99,102,104–110A,111C–116I,128–131(excerpts through part 6); amendments 374ter and VAT 24/29; state invoice rule 7.2.4; final arts 61–62. Focused provisions with neighbors, not all fiscal schedules or all 116pages read. | https://sgg.cg/JO/2026/congo-jo-2026-3-3.pdf | 2026-11-01 |

Figure/rule quotations and source hashes: [country ledger](../../evidence/ledgers/republic-of-congo-draft-20261101/cg-tax-overview.md). Every worked figure is conditional on the stated example facts.

Not yet confirmed: Later 2026 rectifying law and implementation chain; all domain-specific gaps in the README; operative filing procedures; current monetary-law/euro-peg authority; tax-authority restructuring; the old blanket 5% surtax. General commercial currency statements and organisation labels were not used to certify tax calculations. All old topics remain in the immutable destination map.

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
