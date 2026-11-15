---
name: tm-tax-overview
description: "Turkmenistan tax overview, tax year 2026: personal income tax 10%, profit tax 8% / 20% / 50% and 2% for private SMEs, VAT 15% (privately owned legal persons outside VAT), dividends 15%, property tax 1%, and the main return and payment dates, from the Tax Code on the Mejlis site."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tm-tax-overview"
  jurisdiction: "TM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Turkmenistan tax overview

> **General reference only.** Source-cited draft, not reviewed by an accountant. Do not use it to file without professional review.

## Who this applies to

Anyone who needs the map of Turkmenistan's taxes for 2026. The Tax Code of Turkmenistan (Unified Law "On Taxes") is administered by the Tax Directorate of the Ministry of Finance and Economy. Tax year: the calendar year. Currency: manat (TMT). Residents are taxed on worldwide income, non-residents on Turkmen-source income. Detail sits in the sibling skills, which own their figures: [profit tax](tm-corporate-income-tax.md), [VAT](tm-vat-gst.md), [personal income tax](tm-income-tax.md), [payroll](tm-payroll-social.md), [company formation](tm-company-formation.md).

## Rates, bands and thresholds

| Tax | Headline | Tax year | Official URL |
|---|---|---|---|
| Personal income tax (art. 192(1)) | 10% unless the Code says otherwise | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Profit tax, resident legal persons (art. 172(1)) | 8% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Profit tax, state banks and insurers, communications, certification (art. 172(1)) | 50% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Profit tax, other legal persons (art. 172(1)) | 20% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Private SMEs, on gross income (art. 172(4)) | 2% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| VAT (art. 103) | 15%, and 0% for art. 105 transactions | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |
| Dividends (art. 172(2)) | 15% | 2026 | https://mejlis.gov.tm/single-code/10?lang=ru |

## The base

Profit tax on taxable profit (gross income for private SMEs); VAT on taxable transactions by payers, with privately owned legal persons outside VAT (art. 95(2)); personal income tax on individuals' income; property tax at 1% of the year's base for entities (art. 141).

## Deadlines and filing

| Obligation | When | Official URL |
|---|---|---|
| VAT return and payment | Return by the 20th, payment by the 25th of the month after the period; entrepreneurs half-yearly | https://mejlis.gov.tm/single-code/10?lang=ru |
| Profit tax advances | 25th of each month | https://mejlis.gov.tm/single-code/10?lang=ru |
| Profit tax return | On the financial-statement deadline set by the Ministry or Central Bank (art. 176(1)) | https://mejlis.gov.tm/single-code/10?lang=ru |
| Individual returns (art. 197(1)) | By the 25th of the month after the reporting period; foreign citizens by 1 April after the tax year | https://mejlis.gov.tm/single-code/10?lang=ru |

## Penalties and interest

Not read for this guide; see the sibling skills.

## Cross-border points

Non-resident legal persons without a permanent establishment: 15% withheld from gross Turkmen-source income, 6% for bareboat vessel and aircraft leases (art. 180(3)). Treaties may reduce withholding; the treaty list was not checked. Currency exchange controls apply (Law on Currency Regulation, not read).

## Two worked examples that recompute

**1. Employee earning TMT 5,000 in a month.** Personal income tax at 10% = TMT 500 (derived; ignores any deductions under the Code).

```oa-check
name: Turkmenistan PIT 10 percent
inputs:
  income: 5000
steps:
  - tax: income * 0.10
expected:
  tax: 500
```

**2. State bank with TMT 2,000,000 profit from banking.** Profit tax at 50% = TMT 1,000,000 (derived), against TMT 160,000 at the 8% resident rate the old guide implied.

```oa-check
name: Turkmenistan state bank 50 percent
inputs:
  profit: 2000000
steps:
  - tax: profit * 0.50
  - at_8: profit * 0.08
expected:
  tax: 1000000
  at_8: 160000
```

## Ask the client first

- Individual or legal person; resident or not?
- Ownership (state share, private, foreign investment) and sector?
- Headcount (for the SME 2% regime)?
- Payments to non-residents?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Turkmenistan, Russian text on the Mejlis site, arts 95, 103, 111, 141, 172, 175, 176, 180, 192 and 197 (Read for every figure and date here) | https://mejlis.gov.tm/single-code/10?lang=ru | 2026-11-14 |

Not yet confirmed: the double tax treaty list (the old guide's "about 30 treaties" came from a private website); exchange control rules; penalties; financial-statement deadlines. The old guide's "on or about 31 March" annual return date has no basis in arts 176 or 197.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tm-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tm-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
