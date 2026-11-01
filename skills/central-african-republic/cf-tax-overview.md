---
name: cf-tax-overview
description: >
  Use this Central African Republic tax overview for 2026 research intake, routing and the directly read procedural amendments. It maps individual tax, corporate profit, VAT, payroll, related parties, cross-border clearance, formation and property to their dedicated Guides, then sets out the general LPF penalty and notice controls verified in the signed 2025 Finance Act. Search triggers include DGID, tax calendar, penalties, NIU, tax complaint and audit information request. It keeps country-pack presence separate from comprehensive coverage. The full new 2024 procedure book, later amendments, tax-specific penalty priority and live filing channels remain incomplete, so this map cannot certify filing compliance.
jurisdiction: CF
category: international
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Central African Republic tax map and procedure controls v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** For choosing a country tax workflow and identifying evidence still needed. This pack is partial in every coverage domain and has no accountant attestation. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

For choosing a country tax workflow and identifying evidence still needed. This pack is partial in every coverage domain and has no accountant attestation.

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| The fiscal year is twelve months from 1 January to 31 December, and “administration fiscale” means DGID in the amended LPF definitions. The specific taxpayer computation and due-date rules remain separate. Amounts in the signed budgets are FCFA; this Guide uses XAF/FCFA units without implying an exchange rate. | 2026 research scope; 2025 Finance Act art. 13 replacing LPF 4 [official text](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf); ledger O01 |
| Amended LPF 243(1): missing/late registration, return, annex or registration/publicity act attracts XAF 500,000; recurrence within a week XAF 1,000,000. This is the general text, not a conclusion that every special fine is cumulative or displaced. | 2026 research scope; 2025 Finance Act art. 18 replacing LPF 243(1) [official text](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf); ledger O02 |
| Amended LPF 243(2): omissions/inaccuracies in the specified return/annex/act carry 25% of duty; bad faith/fraud 50–100%. LPF 243(7) failure of declaration/payment methods is 25%, escalating to 50–100% for the stated fraud/resistance conduct. The applicable degree must be evidenced, not automatically set to the maximum. | 2026 research scope; 2025 Finance Act art. 18 replacing LPF 243(2),(7) [official text](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf); ledger O03 |
| Missing required DGID tax-free invoice visa for VAT exemption attracts XAF 50,000 per detected breach under the new LPF 243(10). Confirm the exemption/payment mechanism and specific act before assessing liability. | 2026 research scope; 2025 Finance Act art. 18 replacing LPF 243(10) [official text](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf); ledger O04 |

## The base

Route salary and individual categories to [individual tax](cf-income-tax.md), company profit/DSF to [corporate tax](cf-corporate-income-tax.md), supplies/invoices to [VAT](cf-vat-gst.md), employer deductions to [payroll](cf-payroll-social.md), foreign charges to [transfer pricing](cf-transfer-pricing.md), transfers/departures to [cross-border](cf-cross-border.md), entity decisions to [formation](cf-company-formation.md), and buildings/rents to [property](cf-property-tax.md). Read the country README before treating a domain as complete. Preserve the actual notice and classify the specific offence before computing a penalty.

## Deadlines and filing

Written penalty/interest notification must identify taxpayer and offence, calculation, issue date, appeal right, appeal conditions and payment period. Preserve the actual notice and service evidence before choosing a response. [2025 Finance Act art. 14 replacing LPF 71](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf) (ledger O05).

Amended LPF 88 requires response to a written information request within a period not exceeding ten days of receipt; on-site missing-support minutes can make later production inadmissible in the stated dispute phases. This is not the old general twenty-day adjustment-response rule. [2025 Finance Act art. 15 replacing LPF 88](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf) (ledger O06).

The administration has 90 days from receipt of a tax complaint to notify its decision; no notification by expiry means deemed acceptance under amended LPF 171. An agent cannot sign a dispute decision concerning an adjustment/tax they originated. Actual complaint admissibility, service and full appeal route require the complete LPF. [2025 Finance Act art. 16 replacing LPF 171](https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf) (ledger O07).

The signed 2024 Finance Act creates a new LPF, and the signed 2025 Act amends it. The source reading here is selective, not a complete 2024 procedural consolidation. Filing portals, current forms/boxes, holiday/electronic-filing exceptions, service dates, objection admissibility and interest calculations must be authenticated for the actual case.

## Penalties and interest

The table owns the cited general penalties and procedural notice requirements. Do not sum them with older CGI special fines without resolving priority, conduct, period and applicable procedural law. No universal interest percentage is established.

## Cross-border points

For treaty/source/clearance questions use [cross-border](cf-cross-border.md). This map does not establish sanctions permission, payment permission or a treaty result.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. General percentage sanction on a stated duty

Assume the applicable amended LPF paragraph has been established, no bad faith/fraud, XAF 4,000,000 relevant duty and a 25% sanction. The percentage penalty is 1,000,000. This does not establish that a separate flat or tax-specific fine must also be added.

```oa-check
name: General percentage sanction on a stated duty
inputs:
  duty: 4000000
steps:
  - penalty: duty*0.25
expected:
  penalty: 1000000
```

### 2. Invoice visa versus a general declaration breach

For two established missing exemption-invoice visas, the specific 50,000-per-breach text gives 100,000. The general first late-declaration fine is 500,000, but it is not a substitute for classifying the actual offence. These are alternative classifications in this example and are not summed.

```oa-check
name: Invoice visa versus a general declaration breach
inputs:
  visa_breaches: 2
  per_visa: 50000
  general_first: 500000
steps:
  - visa_fine: visa_breaches*per_visa
  - difference: general_first-visa_fine
expected:
  visa_fine: 100000
  difference: 400000
```

## Ask the client first

- Taxpayer type, place and actual tax period?
- Which transaction, tax, registration or filing is involved?
- Current official law, notices, forms and proof of service/payment?
- Business activity, turnover, related parties and foreign links?
- Any exemption, complaint, stay or unresolved prior-period debt?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| Signed 2025 Finance Act, fiscal amendments | https://www.finances.gouv.cf/sites/default/files/2025-01/Loi%20de%20Finances%202025.pdf | 2026-11-01; Read fiscal amendment section, especially arts.9–18; old/new text kept distinct; budget schedules not used. |

Not yet confirmed: Complete 2024 LPF and its commencement/supersession clauses; all current procedural amendments and live channels; special/general penalty priority; tax interest calculations and exact appeal admissibility; current year bases outside specifically verified provisions. Former overview rates/deadlines are routed to the relevant Guide, not duplicated as a supposedly complete country snapshot.

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
