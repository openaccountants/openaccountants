---
name: mg-tax-overview
description: "Madagascar 2026 tax intake and routing across business IR, salary IRSA, TVA, payroll, transfer pricing and non-resident services; partial pack."
jurisdiction: MG
tax_year: 2026
last_updated: 2026-11-01
version: 1.0
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: orchestrator
---

# Madagascar 2026 tax router

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Madagascar.

## Who this applies to

Use this router before computing Madagascar tax for a business, employee or foreign counterparty. The output is a workpaper scope, source list and missing-facts list. Follow the Guide that owns the computation; do not combine headline rates across different taxes. All monetary examples use Malagasy ariary (MGA). This is tier 2 source research; no accountant has attested to this candidate.

## Rates, bands and thresholds

| Decision | Guide that owns the rule | Official foundation |
|---|---|---|
| Business IR/IS boundary, ordinary profit tax and minimum | [Corporate/business tax](mg-corporate-income-tax.md) | [CDI 01.01.02,14; 01.02.02–05](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Employee salary marginal bands and benefits | [Personal IRSA](mg-income-tax.md) | [CDI 01.03.01–19](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Domestic or imported-service TVA | [TVA](mg-vat-gst.md) | [CDI 06.01.01–24](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Employer remittance, social control | [Payroll/social](mg-payroll-social.md) | [CPF I-20–25](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf) |
| Related-party pricing and disclosures | [Transfer pricing](mg-transfer-pricing.md) | [CDI 01.01.13 IV](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |
| Foreign services and PE | [Cross-border](mg-cross-border.md) | [CDI 01.01.02,14 II](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf) |

Do not read “2026” as proof that a partial domain is complete. The [pack README](README.md) states the remaining gaps. The signed July [LFR 2026, Loi 2026-004](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf) was read alongside the LFI codes; it changes capital income, cooperatives, VAT and disclosure timing. Its article 22 ties entry to radio/posted publication, whose exact date has not been established here.

## The base

Classify legal entity, activity, income type, residence, annual turnover, accounting close and special regimes first. A company can use a calendar, July–June or other twelve-month year, with a special first-period rule in CDI 01.01.09. Resident IR income is not restricted to local sources: 01.01.04–05 includes income regardless of origin. Salary scope has its own rules under 01.03.04–05. Do not apply the old territorial summary. Use the return-year and activity exceptions in the owning Guide before calculating. [CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf).

## Deadlines and filing

Build a calendar from the [business](mg-corporate-income-tax.md), [salary](mg-income-tax.md), [TVA](mg-vat-gst.md) and [TP](mg-transfer-pricing.md) Guides. The annual results deadline depends on accounting close; salary and TVA use their separate reporting periods. Keep declared figures, returns, receipts and payment evidence together. Current portal forms and box instructions remain partial; do not mark a filing complete without its actual acceptance and payment evidence. [CPF I-11,20–25,104](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf).

## Penalties and interest

Use the breach and payer classification in the relevant Guide. Income-tax late payment, salary withholding omission, non-remittance of collected tax, missing TP documentation and late credit declarations are different breaches. Do not apply one generic penalty to every tax.

## Cross-border points

Ask about foreign income and payers before routing. Use [cross-border](mg-cross-border.md) for residence/PE and service payment triage, [IRSA](mg-income-tax.md) for foreign salary, [TVA](mg-vat-gst.md) for imported services and [TP](mg-transfer-pricing.md) for controlled transactions. Treaty and dividend interaction gaps are explicit in the cross-border Guide.

## Two worked examples that recompute

Hypothetical turnover inputs support regime routing under CDI 01.01.02/01.02.02; they do not determine the tax payable. First, a general trading business has these annual VAT-exclusive revenue streams. Compare the total against the threshold in the business Guide and confirm its existing/elected regime.

```oa-check
name: Aggregate revenue streams before regime test
inputs:
  stream_a: 300000000
  stream_b: 150000000
steps:
  - annual_turnover: stream_a + stream_b
expected:
  annual_turnover: 450000000
```

Second, annualise a full twelve months only when that is the actual accounting period; special activities/elections still override ordinary IS routing.

```oa-check
name: Full year revenue budget
inputs:
  monthly_revenue: 8000000
  months: 12
steps:
  - annual_turnover: monthly_revenue * months
expected:
  annual_turnover: 96000000
```

## Ask the client first

Get NIF/registration, legal form, sector, activities, tax regime/elections, accounting dates, residence and management facts, turnover by stream, employees, foreign payers/suppliers, group structure, special approvals and prior returns. Do not request specialist calculations before establishing which job applies.

## Sources

 | Source and provisions actually read | Read on |
|---|---|
| [DGI 2026 CDI](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CDI-LFI%202026.pdf), 01.01.01–05,09,13–14; 01.02.02–05; 01.03.01–19; 06.01.01–24 | 2026-11-01 |
| [DGI 2026 CPF](https://www.impots.mg/explorer?path=/legislation/Codes%20et%20Manuels/CPF-LFI%202026.pdf), I-11; I-20–25; I-104; IV-08–10 | 2026-11-01 |
| [DGI code directory](https://www.impots.mg/explorer?path=%2Flegislation%2FCodes+et+Manuels), listing identifying CDI-LFI and CPF-LFI 2026 | 2026-11-01 |

| [Signed Loi 2026-004, LFR 2026](https://www.mef.gov.mg/assets/vendor/ckeditor/plugins/kcfinder/upload/files/2026/lfr/LFR2026%20Ampliation%20SIGNEE%20DATEE.pdf), tax amendments and article 22 entry provision read | 2026-11-01 |

**Not yet confirmed:** Exact radio/posted publication date activating the July LFR under article 22; do not resolve a transaction at that transition without the publication evidence. pack completion, accountant review, specialist sectors, complete non-salary individual/capital taxation, current social schedules, operative treaty relief and live filing workflows. See each owning Guide and README.

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
