---
name: bh-tax-overview
description: "Bahrain tax router for 2026: personal tax screening, hydrocarbon tax, DMTT, payroll/social insurance, VAT, transfer pricing and cross-border domain owners. Makes current-year procedural and source holds explicit."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.3
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Tax Overview v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

People deciding which Bahrain tax or employment-compliance job to run in 2026. Use the domain owner below. This router does not grant a blanket exemption from business, payroll or foreign taxes.

## Rates, bands and thresholds

| Job | Routing decision | Year | Official source |
|---|---|---|---|
| Personal income tax | EDB states no taxation on personal income; use [bh-income-tax](bh-income-tax.md) and its explicitly dated archive | 2026 reference | https://web.archive.org/web/20260321041012/https://www.bahrainedb.com/app/uploads/2026/01/Bahrain-EDB-MFG-Factsheet-2026.pdf |
| Hydrocarbon income tax | Screen statutory activity and income using [bh-corporate-income-tax](bh-corporate-income-tax.md), art. 2 | 2026 | https://www.lloc.gov.bh/Legislation/HTM/L2279 |
| DMTT | Screen the multinational-group revenue test and Bahrain entity scope using the corporate Guide, law arts. 1 to 4 | 2026 | https://www.lloc.gov.bh/Legislation/HTM/L1124 |
| Social insurance/payroll | Establish coverage, wage and service dates using [bh-payroll-social](bh-payroll-social.md); unresolved employer phase-in/minimum-base issues block a full payroll computation | 2026 | https://www.lloc.gov.bh/FullAr/L2476.docx |
| VAT | Use [bahrain-vat](bahrain-vat.md), by Mehran Habib, unchanged on 2025. Obtain a current-year review before acting | 2026 screening only | https://www.nbr.gov.bh/laws_regulations/vat |

## The base

Each figure has one home: corporate income tax and DMTT computations belong to the corporate Guide; social contributions and EOSB to payroll; personal income tax screening to the individual Guide. Formation is [bh-company-formation](bh-company-formation.md). No new narrow Guide is needed. General corporate-tax enactment status and excise coverage remain held below.

## Deadlines and filing

Follow the owner Guide for its return, payment and records. Do not treat a VAT period, social-insurance payment date or DMTT reporting year as a universal Bahrain fiscal-year rule. Current electronic form/box workflows must be established before submitting.

## Penalties and interest

Penalties are regime-specific. Use the corporate or payroll Guide with its act/article; VAT penalties require the named-author VAT Guide's current-year review.

## Cross-border points

Use [bh-transfer-pricing](bh-transfer-pricing.md) for DMTT transfer pricing and CbCR, and [bh-cross-border-tax](bh-cross-border-tax.md) for Bahrain cross-border screening. They are unchanged by this repair; this router does not independently attest their content.

## Two worked examples that recompute

Routing check: an individual has BHD 60,000 salary and BHD 2,000 payroll deductions. Personal income tax remains zero; payroll amounts must be reconciled separately.
```oa-check
name: Overview individual routing
inputs:
  salary: 60000
  deductions: 2000
steps:
  - pit: salary * 0
  - payroll_reconciliation: salary - deductions
expected:
  pit: 0
  payroll_reconciliation: 58000
```

Decision: route a company to DMTT screening for revenue below versus above the corporate Guide's revenue threshold? For four twelve-month preceding years, EUR 800 million in each of two years exceeds EUR 750 million by EUR 50 million in each; EUR 700 million in the other two falls short. Two qualifying years meet art. 3(C), subject to all other entity-scope conditions. These are screening inputs, not a tax amount.
```oa-check
name: DMTT revenue screening comparison
inputs:
  higher: 800000000
  lower: 700000000
  threshold: 750000000
steps:
  - higher_excess: max(higher - threshold, 0)
  - lower_shortfall: max(threshold - lower, 0)
expected:
  higher_excess: 50000000
  lower_shortfall: 50000000
```

## Ask the client first

- Individual or entity, and what activity?
- Any hydrocarbon exploration, production or refining?
- Any multinational group and what preceding-year consolidated revenue/year lengths?
- Any employees, their nationality and first registration dates?
- Any actual or expected taxable business supplies or foreign-country connections?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| EDB manufacturing factsheet, both pages read; March 2026 archive, personal-tax statement p. 2 | https://web.archive.org/web/20260321041012/https://www.bahrainedb.com/app/uploads/2026/01/Bahrain-EDB-MFG-Factsheet-2026.pdf | 2026-11-01 |
| Income Tax Law, enactment and arts. 1 to 13 read | https://www.lloc.gov.bh/Legislation/HTM/L2279 | 2026-11-01 |
| DMTT Law, arts. 1 to 4 and 44 read with scope definitions | https://www.lloc.gov.bh/Legislation/HTM/L1124 | 2026-11-01 |
| Social Insurance Law, arts. 1 to 4, 17 to 33 and 47 to 49 read | https://www.lloc.gov.bh/FullAr/L2476.docx | 2026-11-01 |

Not yet confirmed: general corporate-tax enactment status; the older EDB blanket zero corporate-tax statement; excise; universal calendar-fiscal-year assumption; historic VAT rate/registration/filing assertions as current 2026 instructions; social employer phase-in and minimum-base implementation. Full predecessor text and exact destinations are preserved in [the country evidence](../../evidence/ledgers/bahrain-20261101/README.md). These are NON-OPERATIVE holds, never defaults or authority to compute.

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
