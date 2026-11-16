---
name: zw-tax-overview
description: >
  Starting point for Zimbabwe tax questions in 2026. Routes income tax, company tax, VAT, payroll and formation; identifies USD/ZWG currency questions, ZIMRA and TaRMS, the ordinary calendar year, provisional-tax currency split, dated monthly filing notices and new tax types. Linked Guides retain their own source gaps; this router is not comprehensive filing guidance.
version: 1.1
jurisdiction: ZW
category: orchestrator
tax_year: 2026
last_updated: 2026-11-16
type: router
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Zimbabwe tax overview v1.1

## The method, step by step

Use this as a routing and intake Guide for 2026, then load the relevant subject Guide. The pack has source gaps; following a link does not clear a claim identified there as unconfirmed.

### Establish the period, currency and taxpayer

Ask for taxpayer/entity type, activity and income sources, accounting year end, exact transaction or pay period, currency of each receipt/payment and foreign-currency share, employees, and existing TIN/tax registrations. Do not silently convert USD into ZWG or assume a historic ZWG exchange rate.

| Starting point | Rule and boundary | Official authority |
|---|---|---|
| Authority and portal | ZIMRA; TaRMS Self-Service Portal at mytaxselfservice.zimra.co.zw. Use the taxpayer's TIN and relevant tax type | [ZIMRA Public Notice 50 of 2026, registration and returns](https://www.zimra.co.zw/public-notices?download=4539:public-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms) |
| Ordinary year | January to December; a Commissioner-approved different accounting year requires its approved dates | [Income Tax Act s.2, year of assessment](https://www.zimra.co.zw/legislation/17-acts?download=4233:income-tax-act-updated-to-1st-dec-2024); [Public Notice 58 of 2026, opening paragraph](https://www.zimra.co.zw/public-notices?download=4553:public-notice-58-of-2026-forth-qpd-2026) |
| Income-tax basis | Zimbabwe-source or deemed-source income; do not interpret this as an exemption for every foreign receipt | [Income Tax Act s.8(1), gross income definition](https://www.zimra.co.zw/legislation/17-acts?download=4233:income-tax-act-updated-to-1st-dec-2024) |
| Provisional-tax currency split | For 2026 estimated total income more than 50% in foreign currency, account for tax separately on a 50:50 foreign/local basis; at 50% or less, account in the currency of trade. This is not a PAYE currency-selection rule | [Public Notice 58 of 2026, para.1 A-B](https://www.zimra.co.zw/public-notices?download=4553:public-notice-58-of-2026-forth-qpd-2026) |

### Load the subject Guide

| Question | Guide and handoff |
|---|---|
| Employee or sole trader, source rules, personal top rate or AIDS levy | [Individual income tax](zw-income-tax.md). Establish whether the income is remuneration or trade/investment first; confirm the table's stated year and applicable currency before calculating |
| Company tax, company rate, credits, instalments or top-up tax | [Corporate income tax](zw-corporate-income-tax.md). Obtain activity, licences, accounting year and group facts |
| VAT, registration, invoices or imported services | [VAT](zimbabwe-vat.md). Establish taxable/exempt activities, turnover, time of supply and period/category |
| PAYE, NSSA or employer onboarding | [Payroll and social contributions](zw-payroll-social.md). Obtain pay period, currencies, employee facts and current NSSA authority; its unresolved contribution inputs are not defaults |
| Choosing an entity or incorporation | [Company formation and entity choice](zw-company-formation.md). Confirm member and director facts before tax registration |

The standard VAT rate changed from 15% to 15.5% on 1 January 2026. Earlier time-of-supply rules can still require 15% for a transaction declared in a later period; Category A's December/January return needs the transition calculation. Load the VAT Guide for the computation ([ZIMRA Public Notice 7 of 2026, introductory paragraphs and both category examples](https://www.zimra.co.zw/public-notices?download=4441:public-notice-07-of-2026-change-of-vat-rate-on-submission-of-return-category-a)).

### Use the right filing notice

Do not turn a notice naming a tax and period into a universal filing deadline for every tax.

| Tax/period | Confirmed return and payment position | Official authority |
|---|---|---|
| PAYE, withholding taxes, mining royalties and other tax types listed in the notice, for month ended October 2026 | Return by November fifth; remittance by November tenth. Use the full notice's list to identify the tax type. Later periods need the corresponding applicable notice or operative rule | [Public Notice 61 of 2026, opening paragraph and tax table](https://www.zimra.co.zw/public-notices?download=4556:public-notice-61-of-2026-returns-and-payments-november-2026-due-date-5) |
| VAT Categories B/C and appointed digital-services withholding agents, period ended August 2026 | Return by September tenth; payment by September fifteenth. Other periods/categories need their applicable notice and the VAT Guide | [Public Notice 49 of 2026, opening paragraph](https://www.zimra.co.zw/public-notices?download=4540:public-notice-49-of-2026-vat-returns-and-payments-date-10-september-2026) |
| Provisional income tax, ordinary December year end | Fourth return by December fifteenth and payment by December twentieth 2026; fourth instalment is 35% of estimated annual tax. For other approved years use approved dates | [Public Notice 58 of 2026, opening paragraph and para.1](https://www.zimra.co.zw/public-notices?download=4553:public-notice-58-of-2026-forth-qpd-2026) |

For TaRMS, log in and select the TIN. To add a tax type, select Taxpayer Information, Taxpayer Profile, Tax Type, New Tax Type, then complete and submit the relevant registration. Pending returns follow the effective registration date. For a return use Tax Return Management, Pending Returns, choose the actual tax type, complete and submit. These steps are from [Public Notice 50 of 2026](https://www.zimra.co.zw/public-notices?download=4539:public-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms); they do not replace the conditions creating liability.

### Screen for new 2026 tax types

[Public Notice 50 of 2026](https://www.zimra.co.zw/public-notices?download=4539:public-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms) confirms these Finance Act 7 of 2025 changes effective from 1 January 2026 are configured in TaRMS: presumptive rental income tax, withholding on digital services, gaming operators' tax, domestic minimum top-up tax, and special capital gains tax on transfers of shares or interests in land-holding entities. Their names do not establish that a particular person is liable. Route to the relevant income-tax/company-tax/VAT Guide, then refer any uncovered computation. Do not treat special capital gains tax as a tax on every ordinary capital disposal.

### Worked routing example

Boundary test only: estimated total income expressed on a consistent, already-established measurement basis is 100,000 units and the foreign-currency component is 50,000. The share is exactly 50%, so the notice's more-than-50% trigger is not met and the currency-of-trade rule applies. If the foreign component is 50,001 instead, the share is 50.001% and the 50:50 rule applies. This checks the trigger, not an exchange rate or the amount payable in either currency ([Public Notice 58, para.1 A-B](https://www.zimra.co.zw/public-notices?download=4553:public-notice-58-of-2026-forth-qpd-2026)).

```oa-check
name: Provisional-tax currency routing at and above the boundary
inputs:
  total: 100000
  foreign_at_boundary: 50000
  foreign_above_boundary: 50001
steps:
  - share_at_boundary: foreign_at_boundary / total * 100
  - share_above_boundary: foreign_above_boundary / total * 100
expected:
  share_at_boundary: 50
  share_above_boundary: 50.001
```

## When to refuse or refer

Stop a computation if currency, period, income classification or taxpayer type is missing, or if the linked Guide identifies a necessary figure as unconfirmed. Refer treaty relief, transfer pricing, foreign investment and tax types without complete usable coverage to a Zimbabwe tax professional. Do not supply current PAYE bands, NSSA ceilings, new-tax rates, penalties or interest from this router. A pending-return screen or new tax-type listing does not prove substantive liability.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| Income Tax Act, ZIMRA consolidation updated to December 2024; s.2 ordinary year and s.8(1) gross income definition and neighboring opening paragraphs. Recovered official cache read; use subject Guides for later source-rule amendments | https://www.zimra.co.zw/legislation/17-acts?download=4233:income-tax-act-updated-to-1st-dec-2024 | 2026-11-16 |
| ZIMRA Public Notice 50 of 2026, both pages: new tax types/effective date, registration and pending-return paths, neighboring changes; original recovered PDF/text read | https://www.zimra.co.zw/public-notices?download=4539:public-notice-50-of-2026-new-2026-legislation-changes-deployed-in-tarms | 2026-11-16 |
| ZIMRA Public Notice 58 of 2026, opening paragraph, para.1 currency rules and fourth instalment, neighboring taxpayer exceptions and quarterly return table; read actual notice | https://www.zimra.co.zw/public-notices?download=4553:public-notice-58-of-2026-forth-qpd-2026 | 2026-11-16 |
| ZIMRA Public Notice 61 of 2026, all pages: named October-period deadlines, listed tax types, PAYE long return, payment/TIN and return-posting conditions; read actual notice | https://www.zimra.co.zw/public-notices?download=4556:public-notice-61-of-2026-returns-and-payments-november-2026-due-date-5 | 2026-11-16 |
| ZIMRA Public Notice 7 of 2026, introductory rate/effective-date paragraphs and both transition examples, including supplies deemed to occur in the earlier year | https://www.zimra.co.zw/public-notices?download=4441:public-notice-07-of-2026-change-of-vat-rate-on-submission-of-return-category-a | 2026-11-16 |
| ZIMRA Public Notice 49 of 2026, both pages: August-period VAT/DST category scope, return/payment dates and neighboring filing instructions; later PN50 supersedes its temporary manual-DST instruction | https://www.zimra.co.zw/public-notices?download=4540:public-notice-49-of-2026-vat-returns-and-payments-date-10-september-2026 | 2026-11-16 |

Not yet confirmed: a complete current-year PAYE table and current NSSA inputs in linked Guides; first three QPD payment dates from the cited notice; later monthly periods beyond those expressly cited; liability and computation of new 2026 taxes beyond the usable scope of linked Guides; penalties, interest and treaty rates. This router does not resolve the linked Guides' holds.
