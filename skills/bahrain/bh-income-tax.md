---
name: bh-income-tax
description: "Bahrain personal income tax screening for 2026 using an explicitly dated EDB official archive. Separates personal income tax from payroll, end-of-service, VAT and foreign-country obligations. No payroll or VAT filing is authorised by this Guide."
jurisdiction: BH
tax_year: 2026
last_updated: 2026-11-01
version: 0.3
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bahrain Personal Income Tax v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals asking about Bahrain personal income tax in 2026, including employees and people working for themselves. The Bahrain Economic Development Board (EDB) manufacturing factsheet, archived in March 2026, states that personal income is not taxed. It also states that wealth and capital gains are not taxed. The official live URL now redirects to the EDB homepage; the dated archive is used explicitly. This is a personal-tax screening Guide, not a payroll or VAT filing instruction.

## Rates, bands and thresholds

| Item | Treatment and condition | Year | Official source |
|---|---|---|---|
| Personal income tax | No tax on personal income, per EDB factsheet p. 2; the statement does not remove business, employment or foreign-country obligations | 2026 reference | https://web.archive.org/web/20260321041012/https://www.bahrainedb.com/app/uploads/2026/01/Bahrain-EDB-MFG-Factsheet-2026.pdf |
| Social insurance and end of service | Determine nationality, coverage and employment dates first; use [bh-payroll-social](bh-payroll-social.md) | 2026 | https://www.lloc.gov.bh/FullAr/L2476.docx |
| Business VAT | Route actual and expected taxable supplies to [bahrain-vat](bahrain-vat.md); that named-author Guide remains on 2025 and needs a current-year review before filing | 2026 screening only | https://www.nbr.gov.bh/vat_registration |

## The base

Do not turn salary receipts, business expenses, SIO deductions or employer end-of-service contributions into a personal income tax deduction calculation. EDB identifies no personal income tax. A company is a separate question: screen hydrocarbon activity and multinational-group status using [bh-corporate-income-tax](bh-corporate-income-tax.md).

A bank-description match is a bookkeeping lead, not proof that a receipt is taxable turnover or includes VAT. Reconcile platform payouts to underlying invoices and commissions. Do not default unknown turnover to below a registration threshold or apply a wage ceiling before coverage is established.

## Deadlines and filing

No personal income tax computation is produced under this screening scope. Do not manufacture a personal return, filing box or payment reference. Refer payroll to the payroll Guide and business VAT to its owner. The exact NBR/SIO online forms and current WPS submission procedure are held below, so this file does not authorise those submissions.

## Penalties and interest

No personal income tax penalty computation is made. Payroll, VAT and work-permit charges remain separate obligations; do not label an SIO or NBR bank debit a personal income tax penalty.

## Cross-border points

A Bahrain personal-tax result does not settle another country's residence, source, citizenship or filing rules. Ask for all relevant countries before answering a foreign-income question. Use [bh-cross-border-tax](bh-cross-border-tax.md) for the Bahrain side; establish the foreign rule separately.

## Two worked examples that recompute

An employee receives BHD 60,000 salary. Under the EDB personal-tax statement the Bahrain personal income tax charge is BHD 0. This does not compute take-home pay: social insurance is separate.
```oa-check
name: Salary personal-tax screen
inputs:
  salary: 60000
steps:
  - pit: salary * 0
expected:
  pit: 0
```

Decision: can BHD 2,000 of payroll deductions on that salary reduce a Bahrain personal income tax bill? Compare before and after: both personal income tax amounts remain zero. Retain the deductions in the payroll reconciliation, not as personal tax relief.
```oa-check
name: Deduction belongs in payroll not PIT
inputs:
  salary: 60000
  deductions: 2000
steps:
  - before: salary * 0
  - after: (salary - deductions) * 0
  - pit_saving: before - after
expected:
  before: 0
  after: 0
  pit_saving: 0
```

## Ask the client first

- Is the activity employment, self-employment or a company?
- Which countries and periods are involved?
- What is the worker's nationality and social insurance coverage?
- For business receipts, what do the invoices show and what are actual and expected taxable supplies?
- Is the question personal income tax, payroll, VAT or WPS compliance?

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| EDB manufacturing factsheet, both pages read, decisive statement p. 2, archived 21 March 2026 | https://web.archive.org/web/20260321041012/https://www.bahrainedb.com/app/uploads/2026/01/Bahrain-EDB-MFG-Factsheet-2026.pdf | 2026-11-01 |
| Social Insurance Law, consolidated Arabic, arts. 2 to 4 and 17 to 33 read | https://www.lloc.gov.bh/FullAr/L2476.docx | 2026-11-01 |

Not yet confirmed: estate, inheritance and gift-tax absence; municipal rental tax; exact personal residence-certificate procedure; current WPS Resolution 68/2019 and enhanced 2026 procedure; minimum wage; VAT registration/returns/penalties and bank-description tax classifications in the predecessors. The former SIO percentages, cap and defaults now route to payroll; none is repeated here. Full predecessor text and exact destinations are preserved in [the country evidence](../../evidence/ledgers/bahrain-20261101/README.md). These are NON-OPERATIVE holds, never defaults or authority to compute.

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
