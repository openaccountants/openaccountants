---
name: lr-vat-gst
description: "Reads Liberia’s enacted GST rate changes and unresolved VAT transition for the 2026 tax year, distinguishing the old 12 percent regime from the 13 percent amendment and telecom surtax. Use for Liberia GST, a VAT registration, a manufacturer, taxable imports, service tax, invoice tax or the announced January 2027 rollout. The Guide records a published commencement conflict instead of declaring it solved, and uses conditional GST examples only after the applicable regime is established. Registration, base, returns and limited manufacturing-import relief are traced to the Code. The full VAT Act, commencement exception and deferral instrument remain missing, so this is not authority to issue an operative 2026 tax invoice or file a return."
jurisdiction: LR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Liberia GST and VAT Transition v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Read on: 2026-11-01. Source-cited country draft; currentness gaps are listed below.

## Who this applies to

Manufacturers, importers and listed service providers investigating the correct 2026 regime. **Transition hold:** the VAT amendment’s commencement wording and LRA’s  later announcement have not been reconciled by an enacted deferral instrument. Establish which law applies to the transaction before using a GST or VAT calculation. Under the cited GST framework, goods tax attaches to taxable manufacturer supplies/imports, and services tax to specified taxable services by registered providers. This is not a universal retail sales tax or an assumed multistage input-credit VAT. [ss 1000(a),(c),1001,1002,1021(a),1022](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V05]

## Rates, bands and thresholds

| Rule | Condition and result | Official source |
|---|---|---|
| V01 | The 2024 Chapters 8/10 Act sets ordinary GST 12%, with export goods 0%; its 12% services rule excludes   telecommunications. Treat this as the enacted pre-April 2026 baseline, not the current 13% rule. | [amended ss 1000(b)(3),1021(b)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-2024-AMENDING-CERTAIN-PORTIONS-OF-CHAPTERS-8-AND-10-OF-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [V01] |
| V02 | The Act printed 1 April 2026 sets 13% goods/services GST, export goods 0%, and an additional 5% surtax on telecommunications. Within this GST framework telecom therefore totals 18%. GST/VAT commencement conflict remains unresolved below. | [amended ss 1000(b)(3),1021(b)](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [V02] |
| V03 | The 2024 VAT amendment sets 15% standard VAT and commencement eighteen months after handbill publication or 1 July 2026, whichever is sooner, subject to 1066(b). The full VAT Act/1066(b)/later deferral instrument have not been reconciled here. Do not apply 15% to a 2026 invoice merely because it appears in this law. | [amended VAT ss 1003,1066(a)](https://www.lra.gov.lr/wp-content/uploads/2025/02/ANACTT1.pdf) [V03] |
| V04 | LRA’s  29 September 2026 announcement describes  1 January 2027 VAT implementation. This is evidence of the announced administrative position, not the legal instrument reconciling the published commencement clause. | [29 September 2026 announcement](https://www.lra.gov.lr/lra-commits-to-deepening-partnership-with-civil-society-on-revenue-mobilization/) [V04] |
| V06 | The 2020 GST text uses LRD 3 m taxable amount over actual/expected twelve-months for manufacturer/services registration, with application within 21 days; related supply aggregation and voluntary manufacturer registration conditions apply. The old LRD 5 m claim is unsupported; current transition registration threshold needs reconciliation before action. | [ss 1006(a),1026(a)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V06] |

## The base

The taxable amount uses consideration including relevant duties/charges excluding this GST, less qualifying discounts; related or no-consideration supplies can use fair market value. Imports follow the customs-value-plus-statutory-additions rule, not merely the invoice price. [ss 1004,1025](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V07]

GST import liability has an exception for registered manufacturers’ imports used to produce their manufactured goods. Do not replace this with a blanket no-relief statement or assume a full VAT input-credit chain. [s 1000(c)(2)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V09]

The GST examples below are conditional on the GST provisions applying. They are not a declaration that GST law remained operative after the published VAT commencement date. Do not infer a universal input-credit chain, reverse-charge rule or blanket export exemption beyond the cited export-goods provision.

## Deadlines and filing

GST returns are monthly, and due respectively within 21 days of period end even if nil; output payment follows return due date, import GST generally at arrival/customs collection. The actual registration and transition must first be established. [ss 1008,1029,1045](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V08]

The catalogue lists Monthly GST Return Excluding Hotels, and the LRA home page links [GST/VAT Registration](https://portal.gstreg.lra.gov.lr/). Retrieve the current taxpayer-specific registration status and written transition direction before acting. Current VAT threshold, forms, boxes, accounting-period transition and successful filing have not been verified. Use the official [LRA Forms and Schedules](https://www.lra.gov.lr/forms-and-schedules/) catalogue and [LITAS](https://elitas.lra.gov.lr/) link published by LRA. Select the tax kind, year and TIN; reconcile the return with the working paper and withholding credits; submit the applicable return and schedules, pay against the resulting reference and preserve submission/payment confirmation. The public catalogue was read; live portal screens, box numbers, payment references and a successful filing have not been verified. Stop before submission if the live workflow differs. [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07]

## Penalties and interest

For the general late-filing, late-payment, recordkeeping and interest rules, use [Tax overview](lr-tax-overview.md#penalties-and-interest). Do not invent a fixed interest rate or treat a civil late-payment charge as a criminal conviction.

Do not decide a penalty using a rate from the wrong GST/VAT regime. The transition issue is a reason to obtain the actual governing instrument, not to estimate a filing liability.

## Cross-border points

Imports are tested under the GST customs-collection rules if that regime applies; exports require documentary proof under the Code. Any VAT reverse charge or imported-service treatment must be verified from the full operative VAT law before use. [ss 1000(a),(c),1001,1002,1021(a),1022](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V05] [s 1000(c)(2)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [V09]

## Two worked examples that recompute

### Compare enacted GST rate periods conditionally

Assume a taxable ordinary supply base 100,000 and that GST applies in each relevant period. The 12% baseline gives 12,000; the 1 April 2026 amendment gives 13,000, a 1,000 difference. This compares enacted GST figures only; it does not resolve VAT commencement. [amended ss 1000(b)(3),1021(b)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-2024-AMENDING-CERTAIN-PORTIONS-OF-CHAPTERS-8-AND-10-OF-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [V01] [amended ss 1000(b)(3),1021(b)](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [V02]

```oa-check
name: Compare enacted GST rate periods conditionally
inputs:
  base: 100000
steps:
  - baseline_gst: base * 0.12
  - amended_gst: base * 0.13
  - difference: amended_gst - baseline_gst
expected:
  baseline_gst: 12000
  amended_gst: 13000
  difference: 1000
```

### Telecom surtax is additional under the 2026 GST text

Assume the amended GST framework applies to taxable telecom services with base 100,000. Ordinary 13,000 plus additional 5,000 equals 18,000; using 13% alone understates by 5,000. This is a conditional legal comparison, not a cleared current invoice. [amended ss 1000(b)(3),1021(b)](https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf) [V02]

```oa-check
name: Telecom surtax is additional under the 2026 GST text
inputs:
  base: 100000
steps:
  - ordinary: base * 0.13
  - surtax: base * 0.05
  - total: ordinary + surtax
  - understatement: total - ordinary
expected:
  ordinary: 13000
  surtax: 5000
  total: 18000
  understatement: 5000
```

## Ask the client first

- Transaction date and the actual governing GST/VAT commencement/transition instrument.
- Manufacturer/importer/service classification, registration and turnover.
- Taxable base, related parties, exemptions, discounts and import documentation.
- Telecom/export classification and evidence, period returns and tax collected.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| December 2024 general amendment, approved 17 December/printed 20 December 2024, substantive pages 1–9 | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| 2024 Chapters 8/10 amendment, substantive pages 1–2 and cover | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-2024-AMENDING-CERTAIN-PORTIONS-OF-CHAPTERS-8-AND-10-OF-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| Revenue Code 2020, selected general, income, nonresident, filing and GST provisions | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA Forms and Schedules, named return/schedule links read; not a completed portal filing | https://www.lra.gov.lr/forms-and-schedules/ | 2026-11-01; read in part, specific scope in first column |
| December 2025 amendment, approved 24 March/printed 1 April 2026, cover/preliminary/amended 63,74,76,79,90–92,803,805,806,1000,1021; excise schedule not used | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA 29 September 2026 announcement, VAT implementation sentence read | https://www.lra.gov.lr/lra-commits-to-deepening-partnership-with-civil-society-on-revenue-mobilization/ | 2026-11-01; read in part, specific scope in first column |
| VAT amendment, cover and amended 1003/1066(a), substantive pages 1–2 | https://www.lra.gov.lr/wp-content/uploads/2025/02/ANACTT1.pdf | 2026-11-01; read in part, specific scope in first column |

Not yet confirmed: Full 2024 VATAct including 1066(b); binding legal deferral/reconciliation with announced 1 January 2027 rollout; current registration threshold and VAT input credits/reverse charge; telecom treatment across the full transition; operative invoices/returns/boxes and all later amendments.

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
