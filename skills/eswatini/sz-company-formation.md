---
name: sz-company-formation
description: "Eswatini Company Formation and Entity Choice for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about company formation in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: formation
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Founders forming a business in Eswatini. Law: Companies Act 2009, read on EswatiniLII. Tax year 2026.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Private company directors | At least one (s 191) | 2026 | https://eswatinilii.org/akn/sz/act/2009/8/eng@1998-12-01 |
| Public company directors | At least two (s 191) | 2026 | https://eswatinilii.org/akn/sz/act/2009/8/eng@1998-12-01 |
| Private company | Share capital, articles restrict transfers and prohibit public offers (s 16) | 2026 | https://eswatinilii.org/akn/sz/act/2009/8/eng@1998-12-01 |
| TIN registration | 4 working days | 2026 | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf |

## The base

Vehicles: private company, public company, external company, sole trader, partnership, non-profit association. Lodge the Memorandum and Articles with the Registrar of Companies, Ministry of Commerce, Industry and Trade.

## Deadlines and filing

### How to set up
1. Reserve the name and lodge the constitutive documents with the Registrar.
2. Obtain a trading licence.
3. Apply for a TIN at an ERS Service Centre with certificate of incorporation, Form J, and Public Officer ID.
4. Appoint a Public Officer.
5. Register for provisional tax, PAYE, VAT as needed, or presumptive tax within 2 months of starting.
6. Register with ENPF if you employ eligible staff.

## Penalties and interest

See [Corporate income tax](sz-corporate-income-tax.md).

## Cross-border points

A foreign company's branch pays 25% plus branch profits tax.

## Two worked examples that recompute

Branch profit E100,000: tax E25,000, then 15% on E75,000.

```oa-check
name: Branch of a non-resident
inputs:
  profit: 100000
steps:
  - cit: profit * 0.25
  - bpt: (profit - cit) * 0.15
  - total: cit + bpt
expected:
  total: 36250
```

Decision: subsidiary paying everything to a non-SACU parent. Same total of E36,250, so the choice turns on liability and treaty, not rate.

```oa-check
name: Subsidiary, full dividend
inputs:
  profit: 100000
steps:
  - cit: profit * 0.25
  - nrst: (profit - cit) * 0.15
  - total: cit + nrst
expected:
  total: 36250
```

## Ask the client first

1. Who owns it, and from where?
2. Will it offer shares to the public?
3. What is the activity?
4. Will it employ?
5. Expected turnover?

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies Act 2009 ss 16, 191, read in a browser on EswatiniLII; ss 16 and 191 read | https://eswatinilii.org/akn/sz/act/2009/8/eng@1998-12-01 | 2026-11-01 |
| ERS, Step-by-Step Guide for New Businesses; whole page read | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf | 2026-11-01 |
| ERS, VAT Registration; whole page read | https://www.ers.org.sz/Registration | 2026-11-01 |
| ERS, Presumptive Tax; whole page read | https://www.ers.org.sz/IncomeTax/PresumptiveTax | 2026-11-01 |
| Income Tax Order 1975, ERS consolidated copy to the 2013 amendments; sections cited were read; cited sections read | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | 2026-11-01 |

Not yet confirmed: Not rechecked in the Act: no minimum share capital, annual return, audit and AGM rules, and name reservation steps from the old pack. Registrar portal, fees and timeline: gov.sz did not open. Trading Licences Order not opened.

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
