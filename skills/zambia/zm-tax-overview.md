---
name: zm-tax-overview
description: "Tax overview for Zambia, charge year 2026: which tax applies, headline rates, due dates and where to file with ZRA. Trigger on Zambia tax system, what taxes in Zambia, ZRA overview, tax year Zambia, TPIN. For anyone orienting before using a specific Zambia skill. Rates are owned by the linked skills."
jurisdiction: ZM
category: international
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals and businesses with income from a Zambian source. Residents are also taxed on foreign interest and dividends per the old file (see Not yet confirmed). Charge year: 1 January to 31 December. Currency: Kwacha.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Top PAYE rate | 37% | 2026 | https://www.zra.org.zm/tax-information/ |
| Company standard rate | 30% | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-Income-Tax.pdf |
| VAT standard rate | 16% | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-VAT.pdf |
| Turnover tax | 5% up to K5,000,000 | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf |
| Rental income tax | 0%, 4%, 16% on turnover | 2026 | same |
| Minimum alternative tax | 1% of turnover | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf |
| Property transfer tax | 8% land, shares, IP; 10% mining licence, processing licence | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Property-Transfer.pdf |

Detail: [Income tax](zm-income-tax.md), [Corporate income tax](zm-corporate-income-tax.md), [VAT](zambia-vat.md), [Payroll](zm-payroll-social.md).

## The base

Authority: Zambia Revenue Authority. Register a TPIN within 30 days of starting business: www.zra.org.zm, login, register, captcha, fill in details, or dial *858#. Mobile money levy, tourism levy, insurance premium levy, excise and mineral royalty also exist.

## Deadlines and filing

PAYE and levy 10th; turnover, rental, WHT-related presumptive 14th; VAT 18th; provisional 31 March; annual return 21 June. File through the ZRA portal, TaxOnApp or TaxOnPhone (*858#).

## Penalties and interest

See the linked skill for each tax. One penalty unit is K0.40.

## Cross-border points

Remittances above USD 2,000 without tax clearance draw advance income tax. Zambia keeps treaties listed on ZRA's DTA table.

## Two worked examples that recompute

**Simple.** Turnover business K6,000 in January (ZRA method).

```oa-check
name: Turnover tax January
inputs:
  sales: 6000
steps:
  - tax: (sales - 2500) * 0.05
expected:
  tax: 175.00
```

**Decision: sole trader or company.** Turnover K6,000,000, profit K1,000,000, all profit taken out. Sole trader K341,512 on the annual bands. Company K300,000 plus 15% dividend WHT on K700,000: K405,000. If all profit is drawn, sole trading is cheaper by K63,488; MAT is creditable in both.

```oa-check
name: Sole trader v company
inputs:
  profit: 1000000
steps:
  - sole: 4800 + 7560 + (profit - 110400) * 0.37
  - cit: profit * 0.30
  - wht: (profit - cit) * 0.15
  - company: cit + wht
  - gap: company - sole
expected:
  sole: 341512.00
  company: 405000.00
  gap: 63488.00
```

## Ask the client first

- Individual, partnership or company?
- Annual turnover?
- Employees?
- Resident?
- Sector?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) (No. 2) Act No. 17 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2017%20of%202025%2C%20The%20Income%20Tax%20%28Amendment%29%28No.%202%29%20Act.pdf | 2026-11-01 |
| Income Tax (Amendment) Act No. 10 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2010%20of%202025%20-%20The%20Income%20Tax%20%28Amendment%29-Act.pdf | 2026-11-01 |
| VAT (Amendment) Act No. 19 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2019%20of%202025%20The%20Value%20Added%20Tax%20%28Amendment%29%20Act.pdf | 2026-11-01 |
| Property Transfer Tax (Amendment) Act No. 21 of 2025, whole Act; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2021%20of%202025%2C%20The%20Property%20Transfer%20Tax%20%28Amendment%29%20Act.pdf | 2026-11-01 |
| ZRA Tax Information page, Turnover Tax and PAYE sections; read: full text of the pages listed | https://www.zra.org.zm/tax-information/ | 2026-11-01 |
| ZRA leaflet Introduction to VAT (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-VAT.pdf | 2026-11-01 |
| ZRA leaflet Introduction to Income Tax (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Introduction-to-Income-Tax.pdf | 2026-11-01 |
| ZRA leaflet Post-Registration Requirements (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Post-Registration-Requirements.pdf | 2026-11-01 |
| ZRA leaflet Property Transfer (2026), rates part; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Property-Transfer.pdf | 2026-11-01 |
| ZRA DTA rates table; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2023/09/DTA-Rates.pdf | 2026-11-01 |
| ZRA Advance Income Tax on remittances leaflet (2026), first page; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/08/Refunds-of-Advance-Income-Tax-on-Remittance.pdf | 2026-11-01 |

Not yet confirmed: resident taxation of foreign interest and dividends; whether individual dividend WHT is final in this comparison.

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
