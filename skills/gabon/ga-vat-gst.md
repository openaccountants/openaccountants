---
name: ga-vat-gst
description: >
  Gabon VAT reference for domestic taxable activity, registration thresholds, ordinary monthly returns, invoice evidence and the 2026 finance-law changes. Use for TVA, imported services, reduced rates, zero rating, nonresident digital suppliers and the separate solidarity contribution. Use this Guide to identify the facts, statutory computation and source documents needed before preparing a working paper. It separates the historical code baseline from the enacted finance-law amendments read for this draft. It does not certify the complete 2026 amendment chain or authenticated filing screens. Missing procedures and unresolved old topics are listed explicitly, and the pack remains partial until those gaps and independent review are complete.
jurisdiction: GA
category: international
tax_year: 2026
tax_year_notes: "2026 research draft; CGI 2025 baseline plus enacted finance laws read; currency and commencement holds remain"
last_updated: 2026-11-01
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Gabon VAT and turnover taxes v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**2026 draft and currency hold.** This is a research draft for 2026, not a certified consolidation of the law in force. The DGI-hosted 2025 CGI is a historical baseline, read alongside enacted Law 041/2025 of 29 December 2025 and Law 002/2026 of 17 July 2026. The complete intervening amendment chain, transaction-specific commencement and implementing instruments have not been established. Do not use a baseline figure as an operative 2026 filing instruction. A July amendment is identified as such; its promulgation date alone does not establish its first taxable period. No independent pack review or accountant attestation has occurred.

## Who this applies to

Independent economic activity under articles 207-209, including sales, imports and services. Domestic threshold rules cannot be applied to a nonresident without considering July article 208 ter. Forestry has a distinct threshold. Exempt, zero-rated and outside-scope transactions must be classified separately before deduction. [CGI arts207-209](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-SCOPE); [LFR002/2026 art4, CGI art208ter](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-NONRES).

## Rates, bands and thresholds

| Item and conditions | Rule or amount (XAF unless stated) | Period/status | Official source |
|---|---|---|---|
| Ordinary domestic registration gateway | Annual turnover excluding tax at least 60,000,000; special continuation/option rules apply | 2025 statutory baseline; 2026 currency hold | [CGI art208](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-DOMCAP) |
| Forestry gateway | 500,000,000, subject to the code scope | 2025 statutory baseline; 2026 currency hold | [CGI art208](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-FORESTCAP) |
| Nonresident taxable persons | No Gabon turnover minimum | July 2026 text; implementation/first period unresolved | [LFR002/2026 art4, CGI art208ter](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-NONRES) |
| Ordinary rate | 18%; classify reduced, zero and exempt items first | 2026 initial law and July amendment | [LF041/2025 art4, CGI art221](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178946560179.pdf) (ledger V-RATESLF) |
| July specified reduced items | 10%: listed auto spare parts, axles, construction tiles, nails; retained earlier terms require reconciliation | July 2026 amendment | [LFR002/2026 art4, CGI art221(2)](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-TEN) |
| July specified imported items | 5%: imported newspapers/magazines and mineral water; retained earlier terms require reconciliation | July 2026 amendment | [LFR002/2026 art4, CGI art221(3)](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-FIVE) |
| July local rebar | 3% only for reinforcing iron manufactured in Gabon | July 2026 amendment | [LFR002/2026 art4, CGI art221(4)](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-THREE) |
| Specified international supplies | 0% for listed exports/transport/aircraft or ship operations and qualifying foreign-place services | July 2026 amendment | [LFR002/2026 art4, CGI art221(5)](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-ZERO) |
| Separate CSS gateway | 30,000,000 annual turnover excluding tax; separate exemptions and digital amendments | 2025 statutory baseline; 2026 currency hold | [TFNC section7 CSS art14](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-CSSCAP) |
| Separate CSS | 1% of its own nonexempt base; not VAT | 2025 statutory baseline; 2026 currency hold | [TFNC section7 CSS arts13-27](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-CSS) |

## The base

Use the supply, invoice, payment, import and place-of-use evidence. Sales are generally exigible on delivery; services on collection with debit-authorisation exceptions. Consideration excludes VAT and CSS; the statutory taxable base is rounded down to 1,000. [CGI arts212-220](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-BASE). July moves specified goods to exemption, including natural mineral water produced in Gabon and electric vehicles. A zero-rate label is not a substitute for exemption classification. The July text also says parts of the earlier lists remain unchanged. Do not decide an omitted product merely from these selected examples. [LFR002/2026 art4, CGI art210](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-EXEMPT); [LFR002/2026 art4, CGI art221](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-RATESLFR).

Input tax needs normalized electronic-invoice or permitted substitute evidence and an actual right to deduct. July changes supplier-exigibility timing and inventory-entry conditions. Partial activities need the statutory ratio: no credit at or below 10%, full credit above 90%, actual ratio strictly between those values. The exact 90% boundary is not resolved by the quoted wording and remains on hold. [LFR002/2026 art4, CGI arts222-224](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-INPUT); [LFR002/2026 art4, CGI art227](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-PRORATA). CSS is separately assessed with its own exemptions, place and receipt rules; do not add it to the VAT base. [TFNC section7 CSS arts13-27](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-CSS).

## Deadlines and filing

Ordinary monthly return and payment are due by the twentieth of the next month, including nil declarations. Reconcile output and input schedules and customs references for exporters. [CGI art237](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-FILE). Nonresident digital suppliers can have an optional simplified quarterly route, not the ordinary monthly route; July bars Gabon input credit under that option and includes CSS. [LFR002/2026 art4, CGI arts248septies-248nonies](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-DIGITAL).

The public e-tax link does not prove a complete filing route. This draft has not inspected an authenticated account, current return identifier, box numbers, payment reference generation or acceptance receipt. Obtain the current authority form and preserve the accepted declaration and payment receipt before treating the job as complete.

## Penalties and interest

The baseline late-return rule is 5% of declared rights before formal notice, or 10% if filed within seven days after notice. Failure after notice moves to ex officio assessment and separate sanctions. Nil, deficit and missing-annex returns have their own fixed penalties; do not apply a percentage to zero and call the penalty zero. [CGI artsP998-999](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger G-DELAY). July 2026 replaces the DGE/CIME late or incomplete electronic-payment rule with a 10% penalty plus article P-996 interest and excludes collection penalties when P-998 late-filing penalties apply. For an actual default, establish its date, taxpayer service and procedural notices before computing. [LFR002/2026 art4, CGI artP1000](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger G-PAY). VAT deduction loss, missing invoices, nil returns and refund conditions require their own tests; these are not represented by an ordinary late-return percentage.

## Cross-border points

The baseline client withholding rule for a nonresident without a permanent establishment or professional installation must be reconciled with July nonresident and digital provisions. [CGI art240](https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf) (ledger V-RC); [LFR002/2026 art4, CGI arts248septies-248nonies](https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf) (ledger V-DIGITAL). Digital place-of-supply evidence and registration alone do not establish corporate PE. Use [cross-border](ga-cross-border.md) for income withholding; VAT does not replace that analysis.

## Two worked examples that recompute

**Ordinary taxable month.** Assume transaction timing and classification are already established, standard-rated base is 10,000,000 and supported allowable input VAT is 700,000. Output tax is 1,800,000 and net VAT is 1,100,000. CSS, withholding and prior credits are excluded from this example.

```oa-check
name: Ordinary VAT working paper
inputs:
  taxable_base: 10000000
  allowable_input: 700000
steps:
  - output_vat: floor(taxable_base / 1000) * 1000 * 0.18
  - net_vat: output_vat - allowable_input
expected:
  output_vat: 1800000
  net_vat: 1100000
```

**Decision: prove product origin.** Under the July text, locally manufactured rebar with base 10,000,000 produces 300,000 at its specific rate. An otherwise standard-rated comparator at the same base produces 1,800,000. The difference is 1,500,000, so origin and product evidence change the calculation. The comparator is expressly assumed standard-rated; this does not classify imported rebar or settle the first period.

```oa-check
name: Decision prove July local rebar eligibility
inputs:
  base: 10000000
steps:
  - local_rebar_vat: base * 0.03
  - standard_comparator: base * 0.18
  - difference: standard_comparator - local_rebar_vat
expected:
  local_rebar_vat: 300000
  standard_comparator: 1800000
  difference: 1500000
```

## Ask the client first

- What is the supply, product specification, origin and transaction date?
- Where are supplier, customer, delivery and use located?
- What turnover, forestry status, registration and voluntary-option evidence exist?
- What delivery, collection, customs and electronic-invoice records exist?
- Which inputs relate to taxable, exempt or mixed activity, and which nonresident regime was selected?

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| CGI: Read the cover amendment list and selected passages from arts 2-3, 4-7 (including PE thresholds and exceptions), 8-11 introduction and 11-IV, 12-28, 73-80, 90-96, 108-114, 162-178bis, 206-209, 211-224, 235-243ter, 346-351, P-816-819, P-826-832, P-996-1010ter and TFNC CSS arts 13-27. Exact read rules are the matched ledger quotes; this is not a claim that every paragraph across those ranges was read. | https://dgi.ga/wp-content/uploads/dgi-content/d1dde772234076c5d2bc0a8d8d3db573ed3d8fdd6c3e869c8c57cd181a81bb70/assets/dgi/2d50ab6c2e-Gabon-CGI-2025.pdf | 2026-11-01 |
| LFR: Read enacted identity; fiscal amendments printed1-16 including arts11bis,91bis,178bis,202-204,208ter,210,211ter,215,221-224,227,230,243bis,248septies-nonies,401-404bis,P832ter,P1000; art7 OCAM withdrawal and final101-102/promulgation. Other fiscal measures read for screening only; budget annexes not reviewed. | https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178593988623.pdf | 2026-11-01 |
| LF: Read enacted identity and arts 1-4 with selected fiscal amendments on printed pages 1-5 and 15-18; detailed reconciliation of art11,23,178bis,210,221,223, deletion234, P832ter-quinquies/P917/P1000; final arts78-79/promulgation printed69-70. Customs and budget schedules not used. | https://dgb-gabon.net/uploads/documentation/Texte%20juridique/178946560179.pdf | 2026-11-01 |

Not yet confirmed: The complete 2025-to-2026 item-level rate/exemption consolidation and commencement, the exact 90% prorata case, construction/property exceptions, refund workflow, digital registration form/current interface, reverse-charge interaction, CSS implementation and current excise schedule. The old broad 5%-40% excise claim is unverified and not a rate instruction. Complete intervening amendments, date-specific commencement, current forms and boxes, and independent review. See the [country evidence](../../docs/research/2026-11-01-gabon-pack/README.md) and [old-topic destination map](../../docs/research/2026-11-01-gabon-pack/old-topic-map.md).

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
