---
name: gq-tax-overview
description: >
  Overview of the Equatorial Guinea tax system for tax year 2026. Sets out the governing law, Ley 1/2024 General Tributaria, which replaced Ley 4/2004, the tax authority, currency, tax year, residence, main rates and deadlines, and where each topic lives in this pack. Use for questions such as what taxes apply in Equatorial Guinea, what is the corporate tax rate, what is the VAT rate, what is the top income tax rate, who collects tax in Equatorial Guinea, and when are returns due. Applies to companies, sole traders, employees and foreign investors. Each figure links to the skill and the law that owns it, and the detail stays in those sibling skills.
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

# Equatorial Guinea Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking how Equatorial Guinea taxes a business or person in 2026. Ley 1/2024 of 19 November, General Tributaria, governs tax and repealed Ley 4/2004. It took effect on publication; the Government states 6 December 2024. The 2026 Budget Law is Ley 9/2025. The country belongs to CEMAC and OHADA, and companies keep SYSCOHADA accounts (art 42).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Currency | XAF (FCFA) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Tax year | Calendar year (art 43) | 2026 | same |
| Tax administration | Direccion General de Impuestos y Recaudaciones on the forms; art 78 names Direccion General de Impuestos y Contribuciones | 2026 | https://minhacienda-gob.com/formularios-de-declaraciones-fiscales |
| Residence | Worldwide for salary and capital income of residents; see income tax (arts 103, 126) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Corporate tax | 25% (art 75) | 2026 | same |
| Minimum tax | 1.5% of income, 15 July and 15 January (arts 75, 80) | 2026 | same |
| Top salary rate | 25% (art 130) | 2026 | same |
| VAT | 15%, 5%, 0% (art 155) | 2026 | same |
| Corporate return | Within 6 months of year end; 30 April for smaller non-SA entities (art 79) | 2026 | same |
| Registration | Within 15 working days of starting (art 13) | 2026 | same |
| Wealth tax | 0% to 300,000,000 XAF, then 0.015% to 0.090% (art 202) | 2026 | same |

Other taxes in the law: property (IBI), transfers, stamp, inheritance and gifts, financial activities, gambling and excise (arts 171 to 276).

Skills: [Income tax](gq-income-tax.md), [Corporate income tax](gq-corporate-income-tax.md), [VAT](gq-vat-gst.md), [Payroll](gq-payroll-social.md), [Transfer pricing](gq-transfer-pricing.md), [Cross-border](gq-cross-border.md), [Company formation](gq-company-formation.md).

## The base

Each tax has its own base; see the skills above.

## Deadlines and filing

Self-assessed taxes follow one route: download the form from the https://minhacienda-gob.com/formularios-de-declaraciones-fiscales page, pay at a Treasury bank, then lodge the form and proof at the Ministry (https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_general_tributaria_de_guinea_ecuatorial). Dates are in each skill.

## Penalties and interest

Surcharge of 5% to 15% (art 410) and interest of 2.5% a month (art 412). Detail is in the [VAT](gq-vat-gst.md) skill.

## Cross-border points

See [Cross-border](gq-cross-border.md).


## Two worked examples that recompute

**Company, profit 10,000,000 XAF, income 100,000,000 XAF.** Tax 2,500,000 is above the 1,500,000 minimum.

```oa-check
name: Company tax against minimum
inputs:
  profit: 10000000
  income: 100000000
steps:
  - cit: profit * 0.25
  - minimum: income * 0.015
  - due: max(cit, minimum)
expected:
  cit: 2500000
  minimum: 1500000
  due: 2500000
```

**Decision: pay out profit of 8,000,000 as salary or dividend to a resident individual.** As salary, ignoring other income and company tax effects, the scale gives 810,000 on a net figure of 8,000,000. As a dividend, 25% company tax of 2,000,000 then 10% of the 6,000,000 left is 2,600,000. Salary costs 1,790,000 less, before social contributions.

```oa-check
name: Salary against dividend
inputs:
  profit: 8000000
steps:
  - salary_tax: 360000 + (profit - 5000000) * 0.15
  - company_tax: profit * 0.25
  - dividend_tax: (profit - company_tax) * 0.10
  - dividend_total: company_tax + dividend_tax
  - gap: dividend_total - salary_tax
expected:
  salary_tax: 810000
  company_tax: 2000000
  dividend_tax: 600000
  dividend_total: 2600000
  gap: 1790000
```

## Ask the client first

1. Company, sole trader or employee?
2. Resident or not?
3. Sector?
4. Annual income?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 13, 42, 43, 75, 79, 80, 103, 126, 130, 155, 171 to 276 headings, 202, repeal and final clauses read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |
| Ministry of Finance, tax return forms page, list read | https://minhacienda-gob.com/formularios-de-declaraciones-fiscales | 2026-11-01 |
| Ley 9/2025, 2026 Budget Law, Title II arts 13 and 14 read | https://minhacienda-gob.com/uploads/2026/05/libro-lpge-2026-bcb5ebfc7795.pdf | 2026-11-01 |
| Government press office, 6 Dec 2024 entry into force, read | https://www.guineaecuatorialpress.com/noticias/presentacion_oficial_de_la_nueva_ley_tributaria_de_la_republica_de_guinea_ecuatorial | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: gazette date of Ley 1/2024; the exact current name of the tax directorate.

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
