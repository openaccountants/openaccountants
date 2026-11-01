---
name: mw-tax-overview
description: "Malawi tax-intake router for the partial 2026 country drafts. Use it to gather the entity, income, turnover, assessment period, transaction and employee facts that determine which source-led computation job to open. It routes ordinary company tax and MAT, individual tax, domestic VAT, conditional pension reconciliation, tax registration and a limited transfer-pricing notice response. The two turnover projections are intake controls and do not establish tax-registration liability by themselves. Annual filing deadlines, commencement and transition checks, specialist sectors, full incorporation law, cross-border withholding and treaties, and comprehensive transfer-pricing compliance remain unconfirmed where stated. Presence of these Guides is not complete country coverage or accountant attestation."
jurisdiction: MW
tax_year: 2026
tax_year_notes: "Intended 2026 research draft; Act 3/2026 read and relevant effects identified; appointed commencement chain unresolved; live use held."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
version: 1.3
---

# Malawi 2026 tax router and evidence checks v1.3

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Malawi.

## Who this applies to

**Current-year source hold.** This is a draft reconstruction of the cited provisions, not confirmed operative 2026 coverage. The enacted [Taxation (Amendment) Act 3 of 2026](https://media.malawilii.org/media/legislation/15519/source_file/2e96ab6e73cdf961/mw-act-2026-3-publication-document.pdf) has now been read in full and its relevant changes are identified in the company, individual and TP drafts. Appointed commencement notices for the Tax Administration Act and the 2021 administrative cutover remain unread; period allocation and the complete operative chain are not approved. Do not use this draft to determine an actual 2026 tax position, file, pay or complete a live registration/notice response until those checks are closed. The examples illustrate the cited-text assumptions only. The 2026 year label identifies the intended research period, not completed verification.

Use to assign a Malawi tax question to an actual computation or compliance job. The Malawi Revenue Authority is the Authority in TAA 2. Start with the taxpayer’s identity, source/income type, applicable assessment period and actual transaction dates. A budget year, a company accounting year and a calendar-month payroll period must not be treated as interchangeable. The old principal defines a year of assessment as a twelve-month period, but this pack has not established a universal current default accounting close. [TAA 2](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Taxation 2](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content).

## Rates, bands and thresholds

| Job | Owning Guide | Operative source |
|---|---|---|
| Company income tax, marginal excess charge and MAT credit | [Company tax](mw-corporate-income-tax.md) | [Act 36/2025 ss 3–6](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content) |
| Ordinary salary and non-employment individual rate tables | [Individual income tax](mw-income-tax.md) | [Act 36/2025 Appendix A/B](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content) |
| Current domestic VAT and foreign digital-supply boundary | [VAT](mw-vat-gst.md) | [Act 5/2026](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content); [Act 37/2025](https://elibrary.rat.gov.mw/server/api/core/bitstreams/b0ea0034-2169-45bd-9afe-c7321fb17337/content) |
| Covered mandatory pension/PAYE reconciliation | [Payroll/social](mw-payroll-social.md) | [Pension 2023 ss 10–14](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |
| TP information notice and audit retention | [TP notice response](mw-transfer-pricing.md) | [TAA 91](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [Act 6/2026](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content) |
| New-business tax registration | [Formation handoff](mw-company-formation.md) | [TAA 21–23](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content) |

Rates have one home in the owning Guide. No standalone cross-border pack is complete; the old withholding figures are preserved as gaps in company tax.

## The base

Classify the income source and taxpayer, distinguish employee pay from non-employment income, and identify exemptions/final-withholding amounts before computation. The current company tax/MAT base is in 66–66B; the replacement annual individual tables are separate. Do not substitute the former branch surcharge, the old 25% salary band or a continuous-loss MAT condition. [Act 36/2025 ss 3–6](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content); [Act 14/2025 s 3](https://elibrary.rat.gov.mw/server/api/core/bitstreams/fb807c0f-1335-442a-a1ce-9d6644186525/content). Use confirmed taxable-base inputs when deduction or benefit classification remains unverified.

## Deadlines and filing

Build the compliance calendar from the applicable statutory job and actual assessment/notice period. The current annual income-tax deadline is an explicit gap; neither the old 180-day section 84(1) nor an old government-budget calendar is silently used. Save the actual submitted form, electronic document registration number, payment reference and payment confirmation. Under TAA 38(3), the registration number identifies electronic receipt; a locally saved draft is insufficient evidence. [TAA 38–40](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content); [2021 cutover](https://elibrary.rat.gov.mw/server/api/core/bitstreams/e43a8644-e1e1-46d8-82d7-7e80afd5fd50/content).

## Penalties and interest

Identify the breach before choosing a sanction: missed tax payment, missing return, failure to comply with a TP information notice and unpaid pension contributions are separate. The company, TP and payroll Guides own the bounded consequences. Do not reuse a penalty from a superseded brochure.

## Cross-border points

Ask about foreign income, non-resident counterparties, digital services, group relationships and expatriates before routing. This pack does not establish a full treaty network, exit tax, non-resident withholding or foreign-tax-credit computation. Keep those jobs open in the README.

## Two worked examples that recompute

Hypothetical full twelve-month turnover projections, used only for routing under the current VAT rule. Projected turnover is not itself the final statutory liability test; confirm actual taxable activities and period before registration.

```oa-check
name: Annual turnover projection A
inputs:
  monthly_sales: 6000000
  months: 12
steps:
  - projected_sales: monthly_sales * months
expected:
  projected_sales: 72000000
```

```oa-check
name: Annual turnover projection B
inputs:
  monthly_sales: 2500000
  months: 12
steps:
  - projected_sales: monthly_sales * months
expected:
  projected_sales: 30000000
```

## Ask the client first

Get taxpayer/legal identity and TIN, activities, income type/source, actual assessment and pay periods, turnover/profit reconciliations, special approvals and scheme exemptions, foreign/digital/group transactions, previous returns/credits and actual current notices/forms.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [TAA 2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content), ss 2,21–23,38–40,91 | 2026-11-01 |
| [Act 36/2025](https://elibrary.rat.gov.mw/server/api/core/bitstreams/f9c5b41b-5dce-4764-b7c2-923c808bda48/content), ss 3–6 and current income tables | 2026-11-01 |
| [Act 14/2025](https://elibrary.rat.gov.mw/server/api/core/bitstreams/fb807c0f-1335-442a-a1ce-9d6644186525/content), s 3 foreign-incorporation surcharge removal | 2026-11-01 |
| [April 2026 gazettebundle](https://elibrary.rat.gov.mw/server/api/core/bitstreams/21540b28-6bfd-45b5-a910-b80f13db59b4/content), VATAct 5 and TaxAdminAct 6 | 2026-11-01 |
| [Taxation historicalconsolidation](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content), s 2 definition only, not old current-rate metadata | 2026-11-01 |
| [2021 cutover](https://elibrary.rat.gov.mw/server/api/core/bitstreams/e43a8644-e1e1-46d8-82d7-7e80afd5fd50/content), section 84 deletion and VAT administrative substitutions | 2026-11-01 |

**Not yet confirmed:** appointed commencement notices for TAA/cutover and full period allocation; universal current assessment-year default, annual income-tax filing deadline, full cross-border/TP annual compliance, company-law incorporation, current exemption/commencement orders, specialist sectors and authenticated portals. The partial declarations in README control this pack’s scope. No accountant attestation or full-country completion is claimed.

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
