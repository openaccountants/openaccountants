---
name: gq-corporate-income-tax
description: >
  Corporate income tax (Impuesto sobre Sociedades) in Equatorial Guinea for tax year 2026 under Ley 1/2024 General Tributaria. Covers the 25% rate, the 1.5% Cuota Minima Fiscal, who is liable, the taxable base, losses, interest limits, incentives for new companies and investors, the annual Declaracion Estadistica y Fiscal, audit report thresholds, payment dates, withholding and penalties. Use for questions such as what is the company tax rate in Equatorial Guinea, when is the DEF due, how does the minimum tax work, how long can losses be carried forward, and do new companies get relief. Applies to SA, SAS, SARL, cooperatives, partnerships, branches and public companies. Oil and mining have added rules.
jurisdiction: GQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies with economic activity in Equatorial Guinea in 2026: SA, SAS and SL companies whatever their object, cooperatives, general and limited partnerships, autonomous public companies, certain civil companies, de facto companies and other profit-making legal persons (art 37). Economic interest groups, participation companies and other civil companies can opt in, irrevocably (art 37.3, 37.4). Non-resident companies with a permanent establishment pay on profits attributable to it (art 44.2). The tax year is the calendar year (art 43).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 25%, fractions under 1,000 XAF ignored (art 75) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Cuota Minima Fiscal | 1.5% of income for the year; not applied to newly created companies (art 75.3, 75.4) | 2026 | same |
| State-funded suppliers | 1.5% withheld monthly as minimum tax; agent pays within 15 days (art 80.3, 80.4) | 2026 | same |
| New company relief | 50% off for the first 5 fiscal years (art 77.4) | 2026 | same |
| Cooperatives, crafts, production, livestock, farming, fishing | 50% off for up to 5 years (art 77.2) | 2026 | same |
| Small producers | Exempt for 5 years (art 77.3) | 2026 | same |
| Investment credit | 10% in Malabo and Bata, 15% elsewhere, for 500,000,000 XAF or more (art 78) | 2026 | same |
| Loss carry-forward | Next year plus 5 further years (art 73) | 2026 | same |
| Interest cap, overall | 30% of gross operating surplus; excess carried 5 years (art 68.4, 68.5) | 2026 | same |
| Interest cap, shareholders and group | BEAC rate plus 3 points, capital fully paid (art 68.2) | 2026 | same |
| Cash expenses | Up to 500,000 XAF a month per expense (art 52.e) | 2026 | same |
| Hydrocarbon sector withholding | 10% non-residents, 3% resident services, 5% mobilisation and demobilisation (art 312) | 2026 | same |

## The base

Net profit is all income less deductible costs, under SYSCOHADA (art 42). A cost must relate to the period, be booked and real, serve the business, carry proper invoices and help earn non-exempt income (art 52). Specific limits are in arts 53 to 72. Losses from a year of exemption do not carry forward (art 73.4). Foreign tax is a credit up to the tax due here (art 44.1).

## Deadlines and filing

| Item | Deadline | Source |
|---|---|---|
| Declaracion Estadistica y Fiscal (DEF) | Within 6 months of year end (art 79.1.b) | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| DEF, entity outside the audit test, not an SA | 30 April (art 79.5) | same |
| Tax due | 15 days after filing the DEF (art 80.1) | same |
| Minimum tax | 15 July on January to June income; 15 January on July to December income (art 80.2) | same |

The DEF carries an independent auditor's report, minutes of general meetings, a statement of pay to partners, an eight-column trial balance, and the ledger and journal (art 79.2). The audit report is not required for an entity under two of three limits: balance sheet 125,000,000 XAF, turnover 250,000,000 XAF, 50 permanent staff. An SA always needs it (art 79.3, 79.4). Bank proof of minimum tax paid goes with the DEF (art 80.5).

To pay minimum tax, use the [form](https://minhacienda-gob.com/uploads/2025/10/CUOTA-MIN.FISCAL_SEC.COMUN_.pdf) (code 3720): base, reductions, rate, tax, surcharges, interest. Pay at a Treasury bank, then lodge the form and proof at the Ministry (https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial). The form on the page for the common sector is headed petroleum and mining; confirm the heading with the tax office.

## Penalties and interest

Surcharge 5%, 10% or 15% (art 410); interest 2.5% a month (art 412); under-declaration 10% to 25% (art 411.A). Late annual statements: 50,000 XAF a month under the minimum cash system, 100,000 XAF a month under the normal system (art 411.E). Withholding failures in hydrocarbons have their own scale (art 315).

## Cross-border points

Withholding and treaties are in [Cross-border](gq-cross-border.md). Related-party rules are in [Transfer pricing](gq-transfer-pricing.md).

## Two worked examples that recompute

**Established company, profit 40,000,000 XAF, income 500,000,000 XAF.** Tax is 10,000,000. Minimum tax paid in the year is 7,500,000 and is credited (art 80.6), so 2,500,000 is due after the DEF.

```oa-check
name: Tax less minimum tax
inputs:
  profit: 40000000
  income: 500000000
steps:
  - cit: profit * 0.25
  - minimum: income * 0.015
  - balance: cit - minimum
expected:
  cit: 10000000
  minimum: 7500000
  balance: 2500000
```

**Decision: invest 500,000,000 XAF in Bata or elsewhere, with annual tax of 8,000,000.** The credit is 50,000,000 in Bata and 75,000,000 elsewhere. It is usable for 5 years only (art 78.5), so 40,000,000 is used either way. Location does not change the tax saved. The unused part is not refunded but is a loss over the next 5 years (art 78.6).

```oa-check
name: Investment credit by location
inputs:
  invest: 500000000
  tax: 8000000
steps:
  - used_bata: min(invest * 0.10, tax * 5)
  - used_other: min(invest * 0.15, tax * 5)
expected:
  used_bata: 40000000
  used_other: 40000000
```

## Ask the client first

1. Legal form and activity, including oil, mining or State contracts?
2. Year of creation?
3. Income, profit, balance sheet total and staff?
4. Losses brought forward?
5. Group or foreign shareholders?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 37, 42 to 44, 52, 68, 73 to 80, 312, 315, 410 to 412 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |
| Ministry of Finance, tax return forms page, list read | https://minhacienda-gob.com/formularios-de-declaraciones-fiscales | 2026-11-01 |
| Government press office, 13 Jan 2025 presentation, read in full (filing route) | https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial | 2026-11-01 |
| Minimum tax form, read | https://minhacienda-gob.com/uploads/2025/10/CUOTA-MIN.FISCAL_SEC.COMUN_.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: whether art 75.3 makes minimum tax final when it exceeds the tax, since art 80.6 turns the excess into a credit; the current BEAC reference rate; the old note that no provincial or local income taxes exist.

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
