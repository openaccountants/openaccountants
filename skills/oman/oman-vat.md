---
name: oman-vat
description: "Use this skill to prepare, review or classify transactions for an Oman VAT return, tax year 2026. Oman applies 5% VAT under Royal Decree 121/2020, run by the Tax Authority. Covers registration, rates, statutory 0% categories and a hold on September 2026 lists, blocked input, boxes, deadlines and penalties."
version: 2.2
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman VAT v2.2

> **General reference only.** This Guide is a draft for AI-assisted reference. It has not received independent closeout review or accountant attestation. Do not use it to file, pay or take a position without professional review.

## Who this applies to

Persons with a place of residence in Oman whose supplies pass the thresholds, and non-residents, who register from the date they are liable to pay VAT under the Law, not automatically on every first supply (arts 55, 57). A person whose supplies are all zero-rated may apply for exemption from registration (art. 60). The Tax Authority runs VAT at https://tms.taxoman.gov.om/portal/. Primary law: RD 121/2020 and the Executive Regulations (Decision 53/2021, amended by 456/2022, 521/2023, 81/2025).

**Bookkeeping triage only: unresolved items stay in review suspense and do not enter a filed return on these assumptions.**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 5% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Oman |
| Unknown blocked-input status | Blocked |

Input package: bank statement and reconciliation for the period, registration number and effective date, sales and purchase invoices, invoice register, previous return and credit brought forward. A bank statement is enough for triage, never enough on its own to establish a VAT classification or input deduction. The predecessor's OMR 20 invoice-evidence cutoff is NONOPERATIVE: the opened input-tax guide requires valid evidence without that exemption.

**Refuse and refer:** VAT groups (R-OM-1); free zone and special zone entities (R-OM-2) without their authorisation; mixed taxable and exempt supplies without a worked apportionment (R-OM-3).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 5% of taxable value (art. 36) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Mandatory registration | Supplies above OMR 38,500 over 12 months, past or expected (art. 55) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/Determining+the+Mandatory+and+Voluntary+Registration+Thresholds.pdf/4c5d8dcb-5b81-34ae-a1d2-e3c6d8431988?t=1733169610184 |
| Voluntary registration | Supplies or expenses above OMR 19,250 over 12 months (art. 61) | 2026 | same |
| Non-resident | Registers with no threshold (art. 57) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409 |
| Refund on request | More than OMR 100 | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409 |
| Late tax | 1% a month or part of a month (art. 1) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Zero: food | NONOPERATIVE HOLD: authority news announces a replacement list; decision and annex not recovered, so no product classification from this row | 2026 | https://tms.taxoman.gov.om/portal/web/taxportal/-/the-tax-authority-issues-three-new-decisions-expanding-the-0-vat-rate-list-to-cover-essential-goods-and-healthcare-products. |
| Zero: medicines | NONOPERATIVE HOLD: authority news only; operative decision, annex and clearance conditions not recovered | 2026 | same |
| Zero: veterinary | NONOPERATIVE HOLD: authority news only; operative decision, annex and clearance conditions not recovered | 2026 | same |
| Zero: other | Investment gold, silver, platinum; international and intra-GCC transport; commercial transport means; rescue craft; oil, derivatives and natural gas (art. 51) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Zero: exports | Exports, customs suspension, re-export after repair, services to customers with no GCC residence and benefit outside the GCC, excluding art. 24 services, on regulatory conditions (art. 52); exempt supplies outside the GCC (art. 53) | 2026 | same |
| Exempt | Financial services; healthcare; education; bare land; resale of residential property; local passenger transport; residential rental (art. 47) | 2026 | same |

Points of detail: the first supply of a residential property is 5%, its resale is exempt (https://tms.taxoman.gov.om/portal/documents/20126/1414820/Taxpayer+Manual+Guide+of+Real+Estate.pdf/06ee6dc8-2732-aceb-3ce7-9f8954c44b81?t=1733169611885, section 5.2). Healthcare from licensed institutions is exempt, not zero-rated (https://tms.taxoman.gov.om/portal/documents/d/taxportal/vat-taxpayer-guide-health-care-guide-, section 3.1). Residential rental exemption requires a lawful tenancy granting continuous occupation for more than 3 months; hotels and serviced accommodation do not qualify (Real Estate guide, section 5.3). Financial services for a fee, commission or commercial discount are 5%; licensed life-insurance and life-reinsurance premiums are exempt; separately charged administration fees are 5% (https://tms.taxoman.gov.om/portal/documents/d/taxportal/financial-services-sector-vat-guide). Prices shown to customers include VAT (art. 37).

## The base

Taxable value is the consideration without VAT, including charges to the customer and fees (art. 31). Between related parties, market value where the price is lower (art. 32). Imports: customs value plus taxes and charges due on import (art. 34). Used goods sold in the regular activity use the profit-margin mechanism only under the Regulations (art. 39); this Guide does not supply those eligibility conditions.

**Input tax.** Deduct input tax on taxable supplies with a valid tax invoice (art. 41; https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910, section 2.8). The right lapses 3 years from the end of the period it arose (art. 44). Pre-registration goods within 3 years and still available for use qualify only if normal deductibility conditions hold; eligible services have a separate 6-month lookback, and capital assets use input tax multiplied by net book value divided by acquisition value with mixed-use adjustment (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910).

Blocked (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910, section 2.13): entertainment; motor vehicles for personal use, meaning vehicles for not more than 10 passengers including the driver, excluding rental fleets and emergency vehicles; food and beverage catering, except legally required or remote-site employee sustenance without reasonable alternatives and ordinary meeting refreshments. Only the private-use portion of a mixed-use vehicle is blocked. Goods later supplied onward remain subject to the normal deduction conditions. Prohibited goods are never deductible (art. 43). Employee purchases in their capacity as employees count, with low-value goods and services up to OMR 500, business-purpose records required and private or personal-benefit portions excluded (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910, section 2.10).

Apportionment for mixed supplies: first remove non-economic use and blocked input; directly attribute taxable and exempt input. Apply taxable supplies divided by total taxable and exempt supplies, times 100 and rounded to 3 decimals, only to residual input. Exclude out-of-territory supplies, reverse-charge supplies, capital-goods sales and incidental non-recurring non-core supplies as the guide specifies; preliminary periodic amounts require annual adjustment (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910, section 2.14).

**Reverse charge.** A taxable person receiving services from a non-resident self-assesses 5% and deducts it if for taxable supplies. Report in box 2b.

**Bank-statement patterns (bookkeeping defaults, not law)**

| Pattern | Treatment | Notes |
|---|---|---|
| BANK MUSCAT / BANKMUSCAT, NBO / NATIONAL BANK OF OMAN, BANK DHOFAR, SOHAR INTERNATIONAL / SOHAR BANK, OAB / OMAN ARAB BANK, ALIZZ ISLAMIC | Exclude margin items; check fees | Fees charged as a fee are taxable |
| INTEREST, LOAN REPAYMENT | Exclude | Out of scope |
| OTA, OMAN TAX AUTHORITY, TAX AUTHORITY | Exclude | Tax payment |
| CUSTOMS, ROYAL OMAN POLICE | Exclude | Check import VAT separately |
| SOCIAL PROTECTION FUND, SPF, PASI, PUBLIC AUTHORITY FOR SOCIAL INSURANCE | Exclude | Contributions |
| MINISTRY | Exclude | Government fee |
| NAMA, MAZOON, MUSCAT ELECTRICITY, OMANTEL, OOREDOO OMAN, HAYA WATER | Domestic 5% | Utilities and telecoms |
| GOOGLE, MICROSOFT, ADOBE, META, AWS, ZOOM, SLACK, NOTION, ANTHROPIC, OPENAI, GITHUB, FIGMA | Reverse charge 5% | Check for an Omani VAT invoice |
| SALARY, WAGES, OWN TRANSFER, INTERNAL, DIVIDEND | Exclude | Out of scope |

## Deadlines and filing

Tax periods are calendar quarters; a new registrant's first period runs from the effective date to the quarter end (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409, section 4). The return and payment are due within 30 days of the period end (art. 72; https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409, section 3.3). Payment is electronic. Correct within 30 days of finding an error, up to 3 years from filing, provided no Authority inspection has started (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409, section 3.5). Claim a year-end refund by the due date of the first period of the new year; all claims within 5 years (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409).

How to file (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409, section 3.2): sign in to the Tax Authority portal, open VAT Returns, select "Add new return", complete the boxes, tick "I want to be refunded" if the credit is above OMR 100 and attach the Taxpayer Checklist, select SUBMIT, then YES at the prompt. Pay any tax by the due date.

| Box | Content |
|---|---|
| 1a | Standard rated supplies, excluding VAT |
| 1b | Zero-rated supplies, excluding exports |
| 1c | Exempt supplies |
| 1d, 1e | GCC reverse charge supplies, not activated |
| 1f | Profit margin supplies |
| 2a | GCC purchases under reverse charge, not activated |
| 2b | Reverse charge purchases from outside the GCC |
| 3a | Exports |
| 4a | Imported goods with postponed VAT |
| 4b | All other imports |
| 5a, 5b | VAT due, and adjustments |
| 6a to 6d | Purchases, imports, fixed assets, adjustments |
| 7a to 7c | Total due, total input, net |

The return guide is dated June 2021; check the live form.

## Penalties and interest

Additional tax of 1% a month (art. 1). Deliberate failures such as not filing, no invoice or no records: 2 months to 1 year and OMR 1,000 to 10,000, or either (art. 100). Deliberately not registering, false returns or forged records: 1 to 3 years and OMR 5,000 to 20,000, or either (art. 101). Repeat offences can double (arts 100, 101).

## Cross-border points

Imports: VAT paid with customs duty, or postponed on Tax Authority approval and reported in 4a (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409, section 3.4). Exports: box 3a. GCC reverse charge boxes are "not activated until GCC rules apply" (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409). Free zones at Salalah, Sohar and Al Mazyunah and Duqm are special zones; zero rating needs authorisation and registration (https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+For++Free+Zones.pdf/6bc21a32-209c-b348-e8b6-804f7458ad67?t=1733169612723).

E-invoicing: the Tax Authority launched Rafid and issued the first e-invoice at its 2026 conference (https://tms.taxoman.gov.om/portal/web/taxportal/-/tax-conference-2026-highlights-the-latest-developments-and-changes-in-the-tax-system). The phases run from selected large taxpayers to all VAT-registered entities, and companies must issue approved electronic invoices through a certified provider or compatible system (https://tms.taxoman.gov.om/portal/e-invoicing).

## Two worked examples that recompute

**1. Quarter with sales OMR 200,000 at 5%, input OMR 3,000, UK services OMR 3,000.** Reverse charge nets to zero; pay OMR 7,000.

```oa-check
name: Quarter with reverse charge
inputs:
  sales: 200000
  input_vat: 3000
  rc_base: 3000
steps:
  - output: sales * 0.05
  - rc: rc_base * 0.05
  - net: output + rc - input_vat - rc
expected:
  output: 10000
  rc: 150
  net: 7000
```

**2. Decision: register voluntarily at supplies of OMR 25,000 with OMR 20,000 of costs carrying 5%?** Registered, the client recovers OMR 1,000 a year but must charge OMR 1,250. That helps when customers can recover it, and costs consumers.

```oa-check
name: Voluntary registration
inputs:
  supplies: 25000
  costs: 20000
steps:
  - output: supplies * 0.05
  - recovered: costs * 0.05
expected:
  output: 1250
  recovered: 1000
```

**Preserved original transaction examples, corrected and conditional.** The original Zoom statement was USD 14.99 translated to OMR 5.77. Assume an Oman taxable recipient, taxable-business use, no supplier Oman VAT and an otherwise recoverable input: reverse charge is OMR 0.2885 before return/currency rounding, with equal eligible input. The original Muscat Trading receipt of OMR 2,000 is assumed to be a net taxable sale, giving OMR 100 output. The original OMR 8,000 sedan is assumed entirely private: no input deduction. Bank text alone does not prove these facts.

```oa-check
name: Original Zoom and Muscat and sedan transactions
inputs:
  zoom_omr: 5.77
  muscat_net: 2000
  sedan: 8000
steps:
  - zoom_rc_unrounded: zoom_omr * 0.05
  - zoom_net: zoom_rc_unrounded - zoom_rc_unrounded
  - muscat_output: muscat_net * 0.05
  - sedan_input: 0
expected:
  zoom_rc_unrounded: 0.2885
  zoom_net: 0
  muscat_output: 100
  sedan_input: 0
```

Conditional self-checks, assuming invoice evidence, eligible taxable-business use and the relevant export or credit-note conditions: a sale of OMR 10,000 gives output OMR 500; a purchase of OMR 5,000 plus OMR 250 is recoverable; entertainment of OMR 500 plus OMR 25 gives zero input; an OMR 8,000 sedan for personal use is blocked; exported goods of OMR 50,000 go in box 3a at 0% with input recoverable; a credit note adjusts VAT under art. 40. Never apply a rate other than 5%, 0% or exempt, and always check credit brought forward.

## Ask the client first

- Registered? If so, VAT number and first period?
- Sales by type: domestic, export, exempt, zero-rated?
- Any free zone, Duqm, VAT group or mixed activity?
- Imports, and is VAT postponed?
- Foreign services bought?
- Sales and purchase invoices, and last return?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Law, RD 121/2020, Tax Authority English text (arts 28 to 57, 61, 71, 72, 99 to 101 read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 | 2026-11-01 |
| Chairman decision on registration thresholds, Tax Authority English text (articles One and Two read for mandatory and voluntary thresholds) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/Determining+the+Mandatory+and+Voluntary+Registration+Thresholds.pdf/4c5d8dcb-5b81-34ae-a1d2-e3c6d8431988?t=1733169610184 | 2026-11-01 |
| Tax Authority, VAT Return Filing guide, version 1, June 2021 (sections 3.2 to 3.5 and 4, and the return-box table read; not a whole-document read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+-+VAT+Return+Filing.pdf/fae31d0c-e7e7-0014-9f28-a4c506b36614?t=1733169613409 | 2026-11-01 |
| Tax Authority, VAT Input Tax guide (sections 2.7 to 2.14 read for evidence, blocked input and apportionment; not a whole-document read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Taxpayer+Guide+%28Input+Tax%29.pdf/d5e0fe80-c131-257e-c68d-3c4b58521fad?t=1733169615910 | 2026-11-01 |
| Tax Authority, Real Estate VAT guide (sections 4 and 5 read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/Taxpayer+Manual+Guide+of+Real+Estate.pdf/06ee6dc8-2732-aceb-3ce7-9f8954c44b81?t=1733169611885 | 2026-11-01 |
| Tax Authority, Health Care VAT guide (section 3 read) | https://tms.taxoman.gov.om/portal/documents/d/taxportal/vat-taxpayer-guide-health-care-guide- | 2026-11-01 |
| Tax Authority, Financial Services VAT guide (sections 4.1 and 4.2 and the life-insurance passage read; not a whole-document read) | https://tms.taxoman.gov.om/portal/documents/d/taxportal/financial-services-sector-vat-guide | 2026-11-01 |
| Tax Authority, VAT for Free Zones note (read in full for special-zone authorisation and transaction conditions) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+For++Free+Zones.pdf/6bc21a32-209c-b348-e8b6-804f7458ad67?t=1733169612723 | 2026-11-01 |
| Tax Authority news, three 0% VAT decisions, 28 Sep 2026 (whole page read; the decisions themselves not found) | https://tms.taxoman.gov.om/portal/web/taxportal/-/the-tax-authority-issues-three-new-decisions-expanding-the-0-vat-rate-list-to-cover-essential-goods-and-healthcare-products. | 2026-11-01 |
| Tax Authority news, Tax Conference 2026, 21 Sep 2026 (read for announced tax-system changes only; news is not the operative instrument) | https://tms.taxoman.gov.om/portal/web/taxportal/-/tax-conference-2026-highlights-the-latest-developments-and-changes-in-the-tax-system | 2026-11-01 |
| Tax Authority, e-invoicing page (read for rollout phases and format/provider statements; effective phase dates not established) | https://tms.taxoman.gov.om/portal/e-invoicing | 2026-11-01 |

Not yet confirmed: the text and annexes of the three 0% decisions of September 2026 (news page only); the old late-filing fine of OMR 25 a day up to OMR 2,500 and the old failure-to-register fine of OMR 5,000 (neither is in the law text; the Regulations gazette PDF would not extract); Regulations article numbers, since the gazette PDFs garble; recreational club memberships as blocked; treatment of supplies to Qatar and Kuwait and the old rule treating them as non-implementing states (art. 52 speaks of outside the GCC, boxes are not activated); monthly periods, which the old skill listed and the guide does not; excise on alcohol and pork from the old skill (the Tax Authority rate page does not list them); e-invoicing start dates by phase; the Taxpayer Checklist layout. Excise, income tax and contributions are out of scope here; see the [overview](om-tax-overview.md).

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
