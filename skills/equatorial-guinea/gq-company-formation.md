---
name: gq-company-formation
description: >
  Company formation in Equatorial Guinea for tax year 2026. Covers the entity types under OHADA, tax registration within 15 working days, the tax forms each company files, bookkeeping and audit report tests, and the items not yet confirmed such as minimum capital and local ownership rules. Use for questions such as how do I set up a company in Equatorial Guinea, what is the minimum capital for an SL or SA, do I need a local shareholder, how do I get an NIF, and how long does incorporation take. Applies to founders, foreign investors and advisers. Tax rules come from Ley 1/2024; OHADA and local content figures could not be read from an official text and are marked unverified.
jurisdiction: GQ
category: formation
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders and investors forming a company in Equatorial Guinea in 2026. Companies are formed under OHADA law; tax registration and filing are under Ley 1/2024.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Entity types taxed as companies | SA, SAS, SL, cooperatives, general and limited partnerships (art 37) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Tax registration | Within 15 working days of starting, at the local tax office (art 13) | 2026 | same |
| Registration papers | Name, representative with power of attorney, capital, statutes, notarial deed, office, activities (art 13.3) | 2026 | same |
| Books | SYSCOHADA; retained 10 years for VAT (arts 79, 166) | 2026 | same |
| Audit report | Required unless under two of three limits; always for an SA (art 79) | 2026 | same |
| Minimum capital SARL | unverified: 1,000,000 XAF, old skill from a commercial site; OHADA made it default, so national law can differ | 2026 | unverified |
| Minimum capital SA | unverified: 10,000,000 XAF | 2026 | unverified |
| Minimum members SARL | unverified: 1 | 2026 | unverified |
| Local ownership | unverified: 35% held by nationals and one third of directors | 2026 | unverified |
| Timeline | unverified: 8 to 16 weeks | 2026 | unverified |

Old-skill items also unverified: physical registered office required; capital deposited in a local bank with a certificate to the notary; steps of notarised articles, deposit, RCCM entry, NIF, social security.

Annual cycle: accounts, DEF, monthly VAT and payroll, register updates. See [Corporate income tax](gq-corporate-income-tax.md).

## The base

Company tax base: see [Corporate income tax](gq-corporate-income-tax.md).

## Deadlines and filing

Register for tax within 15 working days of starting (art 13). Filing dates are in the sibling skills.

## Penalties and interest

Surcharge and interest as in the [VAT](gq-vat-gst.md) skill (arts 410, 412).

## Cross-border points

See [Cross-border](gq-cross-border.md).


## Two worked examples that recompute

**Audit test.** Balance sheet 100,000,000 XAF and turnover 300,000,000 XAF, 20 staff: only turnover is over a limit, so one is exceeded; a non-SA needs no audit report.

```oa-check
name: Limits exceeded
inputs:
  balance: 100000000
  turnover: 300000000
  staff: 20
steps:
  - over_turnover: clamp(turnover - 250000000, 0, 1) 
  - over_balance: clamp(balance - 125000000, 0, 1)
  - over_staff: clamp(staff - 50, 0, 1)
  - over: over_turnover + over_balance + over_staff
expected:
  over: 1
```

**Decision: new company or branch of a foreign company.** On profit of 40,000,000 XAF a new company pays 5,000,000 with the 50% relief (art 77.4); this assumes a branch does not count as newly created, which the law does not settle.

```oa-check
name: New company relief
inputs:
  profit: 40000000
steps:
  - full: profit * 0.25
  - relieved: full * 0.50
  - saving: full - relieved
expected:
  full: 10000000
  relieved: 5000000
  saving: 5000000
```

## Ask the client first

1. Local or foreign owners?
2. Sector?
3. Expected turnover and staff?
4. Company or branch?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 13, 37, 79, 166 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: every row marked unverified; the OHADA Uniform Act text did not open on ohada.org or ohada.com; the investment law on boe.gob.gq was not read.

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
