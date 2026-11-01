---
name: ug-income-tax
description: >
  Uganda personal income tax for resident and non-resident individuals, tax year 2026-27: the bands in force from 1 July 2026, the UGX 4,020,000 annual threshold, residence, rental income, the small business turnover tax, provisional tax and the annual return. Use for Uganda questions from URA taxpayers, employers, advisers and foreign investors, including rates, thresholds, filing dates, the URA portal and worked computations. Figures for tax year 2026-27 come from Uganda Revenue Authority pages and the law, and items that could not be opened are named as unverified in the Sources section. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: UG
category: international
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uganda Personal Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026-27 (year of income 1 July 2026 to 30 June 2027).

## Who this applies to

Individuals with Uganda tax to pay. Residents are taxed on worldwide income and non-residents on Uganda-source income. Employees with income only from employment and from one employer do not file (URA: all persons above the threshold file, "save for employees who earn income from only employment and with one employer"). Companies are in [corporate income tax](ug-corporate-income-tax.md); payroll steps are in [payroll](ug-payroll-social.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Resident, annual, up to UGX 4,020,000 | Nil | 2026-27 | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ |
| Resident, UGX 4,020,001 to 4,920,000 | 20% over 4,020,000 | 2026-27 | same |
| Resident, UGX 4,920,001 to 5,820,000 | UGX 180,000 + 25% over 4,920,000 | 2026-27 | same |
| Resident, UGX 5,820,001 to 120,000,000 | UGX 405,000 + 30% over 5,820,000 | 2026-27 | same |
| Resident, above UGX 120,000,000 | As above + additional 10% over 120,000,000 | 2026-27 | same |
| Resident, monthly equivalent | 335,000 / 410,000 / 485,000 / 10,000,000 | 2026-27 | https://ura.go.ug/en/changes-to-paye-return-form-following-the-income-tax-amendment-act-2026/ |
| Non-resident, monthly, to 335,000 | 10% | 2026-27 | https://ura.go.ug/en/domestic-taxes/paye-rates/ |
| Non-resident, monthly, 335,000 to 410,000 | 33,500 + 20% over 335,000 | 2026-27 | same |
| Non-resident, monthly, 410,000 to 10,000,000 | 48,500 + 30% over 410,000 | 2026-27 | same |
| Non-resident, monthly, above 10,000,000 | As above + 10% over 10,000,000 | 2026-27 | same |
| Rental tax, individuals | 30% of chargeable income (2021 text) | 2021 text | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |
| Small business, turnover to UGX 10m | Nil | 2024 text | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 |
| Turnover UGX 10m to 30m | UGX 80,000 without records; 0.4% over 10m with records | 2024 text | same |
| Turnover UGX 30m to 50m | UGX 200,000 without; 8,000 + 0.5% over 30m with | 2024 text | same |
| Turnover UGX 50m to 80m | UGX 400,000 without; 180,000 + 0.6% over 50m with | 2024 text | same |
| Turnover UGX 80m to 150m | UGX 900,000 without; 360,000 + 0.7% over 80m with | 2024 text | same |

The new bands apply from 1 July 2026. URA confirmed that date on 23 Sep 2026 and told employers to amend July and August returns. URA's File a Tax Return page still says 2,820,000; the Act wins. The small business figures come from the 2024 consolidated text and the 2026 handbook lists no change to them.

## The base

Chargeable income is gross income less allowed deductions. An assessed loss carries forward to the next year (2021 text, s.38); individual farming losses are ring-fenced against farming income, and Uganda-source and foreign-source losses are kept apart. From 1 July 2026, 6% is withheld on payments to a public entertainer, and 15% on betting or gaming winnings (the payout less the stake), except national lottery and land-based casino winnings (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). Tax withheld and provisional tax reduce small business tax.

## Deadlines and filing

Annual return: within six months of the end of the period, so 31 December for a 30 June year end (https://ura.go.ug/en/domestic-taxes/returns/). Extension: on application, up to 90 days in aggregate, and the payment date does not move. Provisional tax for individuals: four instalments, by the last day of months 3, 6, 9 and 12 (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.111). From 2026 an individual paying rental tax may file a provisional rental return monthly (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/).

How to file, from URA's page: 1. Go to https://ura.go.ug and click File a Return. 2. Click the link to log in. 3. Log in with your TIN as login ID. 4. Follow the e-services return menu, download the return template (URA return forms page), complete it, upload it. Box numbers are not published on the page read, so ask for the template rather than quoting boxes. New here without a TIN: register first at the [TIN page](https://ura.go.ug/en/domestic-taxes/tin-application/tin-registration-individual/).

## Penalties and interest

Unpaid tax, including provisional tax and tax withheld: 2% per month from the due date (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.136; the 2024 revised numbering differs). Objection to an assessment: within 45 days of receipt, on the portal, with an objection letter (https://ura.go.ug/en/domestic-taxes/objection-appeals/object-to-tax-assessment/). Waivers (Tax Procedures Code Amendment Act 2026): tax outstanding at 30 June 2016 is waived; interest and penalty outstanding at 30 June 2025 is waived if the principal is paid by 30 June 2027 (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/).

## Cross-border points

Foreign employment income and the foreign tax credit sit in ss.80 and 81 of the 2021 text. Payments of royalties to non-residents carry 15% withholding and are outside digital service tax from 2026 (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). Treaty rates are out of scope.

## Two worked examples that recompute

Example 1. Resident employee, UGX 500,000 a month. This is URA's own illustration: 33,750 + 30% of 15,000 = UGX 38,250.

```oa-check
name: Resident, monthly 500,000
inputs:
  income: 500000
steps:
  - tax: 33750 + (income - 485000) * 0.30
expected:
  tax: 38250.00
```

Example 2. A decision: a trader with turnover of UGX 100,000,000 asks whether keeping records is worth it. Without records the tax is UGX 900,000. With records it is 360,000 + 0.7% of 20,000,000 = UGX 500,000. Records save UGX 400,000.

```oa-check
name: Small business, records or none
inputs:
  turnover: 100000000
steps:
  - with_records: 360000 + (turnover - 80000000) * 0.007
  - without_records: 900000
  - saving: without_records - with_records
expected:
  with_records: 500000.00
  saving: 400000.00
```

## Ask the client first

- Resident or non-resident in this year?
- Income sources: employment only, one employer or several, rent, business?
- Business turnover for the year, and are records kept?
- Accounting date, if not 30 June?
- Any tax withheld or provisional tax paid?

## Sources

| Source | URL | Read on |
|---|---|---|
| URA, Tax Amendments FY 2026-27 handbook (36-page PDF, all read); printed before the Income Tax and Excise Acts were assented | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ | 2026-11-01 |
| URA notice, Changes to PAYE return form, 7 Sep 2026 | https://ura.go.ug/en/changes-to-paye-return-form-following-the-income-tax-amendment-act-2026/ | 2026-11-01 |
| URA notice, effective date of Income Tax (Amendment) Act 2026, 23 Sep 2026 | https://ura.go.ug/en/effective-date-of-the-income-tax-amendment-act-2026-and-the-excise-duty-amendment-act-2026/ | 2026-11-01 |
| URA, PAYE rates page | https://ura.go.ug/en/domestic-taxes/paye-rates/ | 2026-11-01 |
| URA, File a Tax Return page (still shows the old UGX 2,820,000 threshold) | https://ura.go.ug/en/domestic-taxes/returns/ | 2026-11-01 |
| URA compendium of domestic tax laws, as of July 2021: ITA Cap 340, VAT Act Cap 349 (only the sections cited; old numbering) | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ | 2026-11-01 |
| Income Tax Act, ULII consolidated text at 2024-12-23 (read in a browser: Schedule tables and rate lines only) | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 | 2026-11-01 |
| URA, Object to Tax Assessment | https://ura.go.ug/en/domestic-taxes/objection-appeals/object-to-tax-assessment/ | 2026-11-01 |

Not yet confirmed: the residence test (old file: 183 days in 12 months, permanent home, government officials; the wording was not re-read in law, so do not state it as confirmed); whether employee NSSF is deductible for PAYE (old file said no, confirm); owner-occupier mortgage relief; the old statement that PAYE is final where there is no other income beyond URA's filing exception; the provisional instalment formula in the 2024 text; the enacted text of the Income Tax (Amendment) Act 2026 (ULII blocked script access and it was not found listed).

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
