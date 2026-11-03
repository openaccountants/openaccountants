---
name: gm-income-tax
description: "personal income tax for The Gambia (tax year 2026): bands, minimum tax, small business and informal sector tax, capital gains, filing steps. Built from official GRA, SSHFC and Ministry of Justice pages."
jurisdiction: GM
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gambia Personal Income Tax

## Who this applies to

Individuals with economic or income generating activity in The Gambia. An individual is resident with at least 183 days in the tax year. Employment income earned abroad by a resident is taxed subject to the foreign source rule. Employees on one job with no other income do not file. Payroll is in [gm-payroll-social](gm-payroll-social.md); rent, dividends and withholding are in [gm-corporate-income-tax](gm-corporate-income-tax.md).

## Rates, bands and thresholds

Basis for 2026: the rows below come from the GRA and SSHFC pages live on 1 November 2026. The Income and Value Added Tax Act 2012 and any 2026 amending Act could not be opened, so a 2026 change that GRA has not published is not reflected.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Band 1: D0 to D36,000 a year | 0% | 2026 | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 |
| Band 2: D36,001 to D46,000 | 5% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 3: D46,001 to D56,000 | 10% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 4: D56,001 to D66,000 | 15% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 5: D66,001 to D76,000 | 20% | 2026 | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 |
| Band 6: above D76,000 | 25%; the GRA table runs at 25% to its last row, D100,000 a month | 2026 | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 |
| Employment threshold | Above D3,000 a month or D36,000 a year | 2026 | https://www.gra.gm/domestic-faqs |
| Business income: minimum tax | Higher of the schedule tax or 1% of turnover (audited accounts) or 2% (any other case) | 2026 | https://www.gra.gm/domestic-faqs |
| Business turnover under D500,000 a year | 3% of turnover, final tax; quarterly declaration, no annual return | 2026 | https://www.gra.gm/download-file/8d0cd78a-d217-11ed-9b31-029254d29bb1 |
| Informal sector: one-off annual charge by trade | D1,000 to D50,000, for example barbers D2,000, welders D10,000, foreign exchange bureaus D30,000; final unless turnover exceeds D100,000 | 2026 | https://www.gra.gm/download-file/8d0cb474-d217-11ed-9b31-029254d29bb1 |
| Capital gains, individuals | Higher of 15% of the gain or 5% of the consideration | 2026 | https://www.gra.gm/domestic-faqs |
| Capital gains exemption | Gain not above D24,000 | 2026 | https://www.gra.gm/download-file/8d0c6de0-d217-11ed-9b31-029254d29bb1 |

The PIT brochure prints an older table starting at D24,000 ("as at 2018"); the FAQ points to the First Schedule, and GRA's employment table starts at D36,000. Whether business income uses the D36,000 bands is on the Not yet confirmed line.

## The base

Chargeable income is business income plus other taxable income. Allowed: cost of stock sold, business expenditure, qualified pension contributions, initial and annual allowance and amortisation, pre-commencement expenditure, business bad debts, losses carried forward within six years. Not allowed: closing stock, fines, personal expenditure, taxes (except on fringe benefits), bribes, entertainment, depreciation and capital expenditure, gifts and donations, losses carried back. Capital gain is the selling price less purchase price, improvement cost and disposal cost; capital losses do not offset other gains and do not carry forward. Private residence and agricultural land have reinvestment exemptions if occupied or used by the taxpayer or parents in the two prior years: full consideration reinvested within one year (residence) or two years (agricultural land).

## Deadlines and filing

Tax year: calendar year; a Special Tax Year needs Commissioner General approval.

| Item | Due |
|---|---|
| Annual return and final payment | 31 March |
| Quarterly instalment and declaration | 15 days after quarter end |
| Capital gains return and payment | 15 days after disposal |
| Informal sector payment | On or before 31 March |

Credits apply in this order: foreign tax credits, instalments, non-final withheld taxes. Unused credits carry forward for at most 3 years, first in first out.

### How to file on the GRA portal
1. Go to https://www.gra.gm and log in with portal credentials. A new user creates temporary credentials first and registers for a TIN.
2. Select the tax type, then complete the return form or upload it.
3. Upload supporting documents and submit.
4. The system sends an instant e-acknowledgement, then a notice with a document ID used to pay.
5. Pay by bank or another listed platform. The system sends a URL to print the receipt.
To amend or extend, use the same login, select the tax type, return and period, complete the request, upload reasons and submit; GRA notifies approval or rejection. Paper returns go to the nearest DTD office, or to Kanifing Revenue Office for the Large Taxpayer Unit. Box numbers are not listed here because the form could not be read as a PDF.

## Penalties and interest

GRA lists these as offences: failure to lodge, false information, failure to notify a change of address, improper use of TIN, obstruction. The amounts are on the Not yet confirmed line. Objection: within 30 days, then the Tax Tribunal, then the Court of Appeal.

## Cross-border points

Foreign capital gains tax is a credit to the extent a treaty provides, at the lesser of foreign tax paid or Gambian tax. An employee taxed on foreign employment income in that foreign country is exempt from PAYE.

## Two worked examples that recompute

Employee on D50,000 a month (GRA's own example): annual D600,000, tax D136,000 a year, D11,333.33 a month.

```oa-check
name: Employee D600,000 a year
inputs:
  income: 600000
steps:
  - tax: (income - 76000) * 0.25 + 5000
  - monthly: tax / 12
expected:
  tax: 136000.00
  monthly: 11333.33
```

Decision: audit or not. A trader with turnover D5,000,000 and profit D100,000. Schedule tax is under the minimum on either band table, so the turnover minimum decides: audited D50,000, unaudited D100,000. Audit if its cost is under D50,000.

```oa-check
name: Audit decision
inputs:
  turnover: 5000000
steps:
  - audited: turnover * 0.01
  - unaudited: turnover * 0.02
  - saving: unaudited - audited
expected:
  saving: 50000.00
```

## Ask the client first

- Employment only, or business, rent or other income?
- Resident for 183 days or more?
- Annual turnover: under D500,000, or an informal sector trade?
- Audited accounts?
- Any disposal of land, shares or other capital asset?

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |
| GRA Income Tax Table 2025 (monthly table; band edges and last row read, latest table on the GRA downloads page), read for the rows cited | https://www.gra.gm/download-file/2a69ec11-c633-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA PAYE brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0ccc58-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Personal Income Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0cd78a-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Informal Sector Income Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0cb474-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Capital Gains Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0c6de0-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA E-Filing brochure (whole), read in full for this skill | https://www.gra.gm/download-file/7937e6d9-48f3-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA E-Payment brochure (first part), read for the rows cited | https://www.gra.gm/download-file/2d4c2498-48f5-11ef-b086-029254d29bb1 | 2026-11-01 |

Not yet confirmed: The Income and Value Added Tax Act 2012 and any 2026 amendment (not on the sites opened; mofea.gov.gm and assembly.gm searched). Whether business income uses D24,000 or D36,000 bands. The statutory rule for non-resident individuals. Penalty and interest amounts. Return box numbers. Informal sector list is from the regulation as amended 2015 per the brochure; current amounts unconfirmed.

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
