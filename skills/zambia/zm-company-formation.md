---
name: zm-company-formation
description: "Company formation and entity choice for Zambia, 2026: PACRA registration, entity types, annual return contents after the 2025 amendment, TPIN and first tax registrations. Trigger on register a company in Zambia, PACRA, TPIN, annual return PACRA. For founders and advisers. PACRA fees and capital figures are unverified."
jurisdiction: ZM
category: formation
tax_year: 2026
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zambia Company Formation and Entity Choice v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone starting a business in Zambia, 2026.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Annual return contents | Signed by director or secretary; beneficial owners and total employees | 2026 | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2023%20of%202025%2C%20The%20Companies%20%28Amendment%29.pdf |
| Deregistration ground | Registrar may de-register a company with no annual returns for two consecutive years | 2026 | same |
| Tax start notice | Notify ZRA within 30 days of commencing business | 2026 | https://www.zra.org.zm/wp-content/uploads/2026/06/Turnover-Tax.pdf |
| Records | Keep at least six years | 2026 | same |
| PACRA fees | unverified: fees page is a menu with no figures read | 2026 | unverified |
| Minimum share capital | unverified: old sources K15,000 or K20,000, both blogs | 2026 | unverified |


## The base

Entity types carried from the old file: private company limited by shares, public company, company limited by guarantee, business name or sole proprietor (not a separate person). A private company lodges financial statements with its annual return; a public company lodges more, including directors' and auditors' reports (s. 273 as replaced).

## Deadlines and filing

1. Reserve name and incorporate at PACRA (pacra.org.zm portal).
2. Register a TPIN: www.zra.org.zm, login, register, captcha, taxpayer details, reason. ZRA will ask for the PACRA certificate on a demographic amendment.
3. Register tax types: Registrations, Tax Type Amendment.
4. Register for PAYE even if staff are below the threshold, then Smart Invoice.
5. File the PACRA annual return each year. Income tax return: 21 June.

## Penalties and interest

Late tax returns: see [Corporate income tax](zm-corporate-income-tax.md). Missing two annual returns risks de-registration.

## Cross-border points

The annual return's information now includes beneficial owners. A foreign shareholder should expect dividend WHT: see [Corporate income tax](zm-corporate-income-tax.md).

## Two worked examples that recompute

**Simple.** Rental-free retailer turnover K600,000 a year, K50,000 a month: turnover tax.

```oa-check
name: Turnover tax on a small company
inputs:
  monthly: 50000
steps:
  - tax: (monthly - 2500) * 0.05
expected:
  tax: 2375.00
```

**Decision.** See [Tax overview](zm-tax-overview.md) for sole trader against company; here the same inputs at 30% only.

```oa-check
name: Company tax only
inputs:
  profit: 1000000
steps:
  - cit: profit * 0.30
expected:
  cit: 300000.00
```

## Ask the client first

- Who owns it, and from which country?
- Expected turnover?
- Consultancy or other activity?
- Employees from day one?

## Sources

| Source | URL | Read on |
|---|---|---|
| Companies (Amendment) Act No. 23 of 2025, ss. on annual return; read: full text of the pages listed | https://www.parliament.gov.zm/sites/default/files/documents/acts/Act%20No.%2023%20of%202025%2C%20The%20Companies%20%28Amendment%29.pdf | 2026-11-01 |
| ZRA Tax Information page, Turnover Tax and PAYE sections; read: full text of the pages listed | https://www.zra.org.zm/tax-information/ | 2026-11-01 |
| ZRA leaflet Turnover Tax (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Turnover-Tax.pdf | 2026-11-01 |
| ZRA leaflet Post-Registration Requirements (2026), OCR read; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2026/06/Post-Registration-Requirements.pdf | 2026-11-01 |
| ZRA step-by-step applications guide; read: full text of the pages listed | https://www.zra.org.zm/wp-content/uploads/2023/09/STEP-BY-STEP-GUIDE-ON-THE-ZRA-DOMESTIC-TAXES-APPLICATIONS.pdf | 2026-11-01 |

Not yet confirmed: shareholder cap of 50; PACRA timeline of 1 to 5 days; PACRA Act No. 4 of 2020 citation; all fees; share capital; company law text beyond the 2025 amendment.

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
