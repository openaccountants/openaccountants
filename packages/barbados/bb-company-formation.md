---
name: bb-company-formation
description: >
  How to incorporate a company or register a business name in Barbados in 2026
  at the Corporate Affairs and Intellectual Property Office (CAIPO), and register
  it with the BRA and NIS. Gives the CAIPO fees (Articles of Incorporation Form 1
  BBD 750, name search and reservation BBD 30, non-profit BBD 150, external
  company BBD 3,000, business name BBD 100) and the BRA registration documents.
  Trigger on Barbados company formation, CAIPO, incorporate in Barbados, business
  name Barbados. Built from CAIPO and BRA pages; not reviewed by an accountant.
version: 1.0
jurisdiction: BB
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: formation
tier: 2
domain: formation
type: filing-howto
---

# Barbados Company Formation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders forming a company under the Companies Act, Cap. 308, or registering a business name under the Registration of Business Names Act, Cap. 317, with CAIPO in 2026, then registering with the Barbados Revenue Authority (BRA). Amounts are BBD.

Out of scope: societies with restricted liability, international business entities, external company operations beyond registration, regulated financial services.

## Rates, bands and thresholds

| Item | Fee | Conditions | Source |
|---|---|---|---|
| Name search and reservation (Form 33) | BBD 30 | Companies Act | CAIPO, fee schedule: https://caipo.gov.bb/fees/ |
| Articles of Incorporation (Form 1) | BBD 750 | Profit company | same |
| Articles of Incorporation, non-profit (Form 2) | BBD 150 | | same |
| External company registration (Form 28) | BBD 3,000 | Foreign company | same |
| External company annual return (Form 31) | BBD 100 | | same |
| Articles of Amendment (Form 5) | BBD 25 | | same |
| Articles of Amalgamation (Form 15) | BBD 750 | | same |
| Articles of Continuance (Form 17) | BBD 3,000 | | same |
| Restore name to register (Form 32) | BBD 300 | | same |
| Business name application | BBD 100 | Registration of Business Names Act | same |
| Business name search and reservation | BBD 30 | | same |
| Notice of change or cessation of business | BBD 50 each | | same |

## The base

| Form | Liability | Tax |
|---|---|---|
| Company limited by shares | Limited | Corporation tax 9% or 5.5% (see `bb-corporate-income-tax`) |
| Sole trader or partnership under a business name | Unlimited | Personal income tax (see `bb-income-tax`) |
| External company | Parent | Barbados-source income |

## Deadlines and filing

| Step | Where | What | After |
|---|---|---|---|
| 1 | CAIPO | Name search and reservation, Form 33, BBD 30 | Name reserved |
| 2 | CAIPO | Articles of Incorporation (Form 1), Notice of Address (Form 4), Notice of Directors (Form 9); fee BBD 750 | Certificate of Incorporation (Form 3) |
| 3 | BRA, TAMIS | TIN and web user for the company | TIN |
| 4 | BRA | VAT registration if income will reach BBD 200,000 a year (documents: Forms 1, 3, 4, 9 and 33) | See `barbados-vat` |
| 5 | NIS and BRA | Register as an employer before the first payroll | See `bb-payroll-social` |
| 6 | CAIPO | Annual return each year | See Not yet confirmed |

## Penalties and interest

See Not yet confirmed.

## Cross-border points

A foreign company carrying on business in Barbados registers as an external company (Form 28, BBD 3,000) and files Form 31 annual returns (BBD 100).

## Two worked examples that recompute

### Example: CAIPO fees for a local company and for a foreign company's branch

Local company: BBD 30 + BBD 750 = BBD 780. External company: BBD 3,000 plus BBD 100 for its first annual return = BBD 3,100.

```oa-check
name: BB 2026 CAIPO fees, local company vs external company
inputs:
  name: 30
  articles: 750
  external: 3000
  external_return: 100
steps:
  - local_total: name + articles
  - external_total: external + external_return
expected:
  local_total: 780
  external_total: 3100
```

## Ask the client first

1. Local company, external company or business name?
2. Proposed names, directors and registered address.
3. Expected income (VAT BBD 200,000) and employees.
4. Is a small business approval under the Small Business Development Act wanted (5.5% rate)?

## Sources

| Source | URL | Read on |
|---|---|---|
| CAIPO, fee schedule (via Firecrawl): read for Companies Act and Business Names Act fees | https://caipo.gov.bb/fees/ | 2026-11-14 |
| BRA, who must register for VAT: read for the company documents list | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/Who-Must-Register-for-VAT | 2026-11-14 |

Not yet confirmed: the domestic company annual return date and fee (CAIPO has published a 30 June deadline for an earlier year); minimum share capital (earlier version: none); incorporation timeline (earlier version: about 5 business days); societies with restricted liability rules; the earlier version's statement that monthly tax prepayments and economic substance filings apply to all companies (see `bb-corporate-income-tax`).
