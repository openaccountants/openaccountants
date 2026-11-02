---
name: gm-tax-overview
description: "tax overview for The Gambia (tax year 2026): the main taxes, rates and deadlines, linked to the skill that owns each. Built from official GRA, SSHFC and Ministry of Justice pages."
jurisdiction: GM
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gambia Tax Overview

## Who this applies to

Anyone needing a map of Gambian tax. The Gambia Revenue Authority (GRA) administers tax; the currency is the dalasi (GMD, D); the tax year is the calendar year. Residents: individuals with at least 183 days, entities incorporated, managed or controlled in The Gambia. Resident companies are taxed on all income, non-residents on Gambian-source income.

## Rates, bands and thresholds

Basis for 2026: the rows below come from the GRA and SSHFC pages live on 1 November 2026. The Income and Value Added Tax Act 2012 and any 2026 amending Act could not be opened, so a 2026 change that GRA has not published is not reflected.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Top personal rate | 25%: see [income tax](gm-income-tax.md) | 2026 | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 |
| Corporation tax | 27% or the turnover minimum: see [corporate](gm-corporate-income-tax.md) | 2026 | https://www.gra.gm/domestic-faqs |
| VAT | 15%: see [VAT](gm-vat-gst.md) | 2026 | https://www.gra.gm/domestic-faqs |
| Rental income tax | 8% residential, 15% commercial, gross | 2026 | https://www.gra.gm/domestic-faqs |
| Payroll | See [payroll](gm-payroll-social.md) | 2026 | https://www.gra.gm/download-file/221f7a81-6596-11f1-b086-029254d29bb1 |

## The base

Rent is taxed on gross income with no deductions, on a cash basis. Hotels, guest houses and similar are not residential. Rent on property of local and district authorities and government institutions is exempt.

## Deadlines and filing

Annual income returns: 31 March. PAYE, VAT, withholding: 15 days after month end. Quarterly declarations: 15 days after quarter end. Stated in the [income](gm-income-tax.md) and [corporate](gm-corporate-income-tax.md) skills.

### How to file on the GRA portal
1. Go to https://www.gra.gm and log in with portal credentials. A new user creates temporary credentials first and registers for a TIN.
2. Select the tax type, then complete the return form or upload it.
3. Upload supporting documents and submit.
4. The system sends an instant e-acknowledgement, then a notice with a document ID used to pay.
5. Pay by bank or another listed platform. The system sends a URL to print the receipt.
To amend or extend, use the same login, select the tax type, return and period, complete the request, upload reasons and submit; GRA notifies approval or rejection. Paper returns go to the nearest DTD office, or to Kanifing Revenue Office for the Large Taxpayer Unit. Box numbers are not listed here because the form could not be read as a PDF.

## Penalties and interest

Objection to any tax decision: within 30 days. Amounts are in no official page opened.

## Cross-border points

Withholding, dividends and treaty relief are in the corporate skill.

## Two worked examples that recompute

GRA's rent example: D600,000 residential, D1,200,000 commercial.

```oa-check
name: Rent tax
inputs:
  res: 600000
  com: 1200000
steps:
  - tax: res * 0.08 + com * 0.15
expected:
  tax: 228000.00
```

Decision: hold land personally or in a company. Sale D2,000,000, gain D380,000. An individual pays D100,000; a company D200,000.

```oa-check
name: Capital gain by holder
inputs:
  price: 2000000
  gain: 380000
steps:
  - person: max(gain * 0.15, price * 0.05)
  - company: max(gain * 0.25, price * 0.10)
  - gap: company - person
expected:
  gap: 100000.00
```

## Ask the client first

- Individual, company or partnership?
- Resident?
- Which income or transaction?
- Tax year in question?

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |
| GRA Income Tax Table 2025 (monthly table; band edges and last row read, latest table on the GRA downloads page), read for the rows cited | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA Rental Income Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0ce2c1-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Capital Gains Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0c6de0-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| Expatriate Quota Pay Roll Tax Notice, 2026, under Payroll Tax Act Cap. 83:04 s.21 (whole), read in full for this skill | https://www.gra.gm/download-file/221f7a81-6596-11f1-b086-029254d29bb1 | 2026-11-01 |
| GRA E-Filing brochure (whole), read in full for this skill | https://www.gra.gm/download-file/7937e6d9-48f3-11ef-b086-029254d29bb1 | 2026-11-01 |

Not yet confirmed: The Income and Value Added Tax Act 2012 and any 2026 amendment. Penalty amounts.

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
