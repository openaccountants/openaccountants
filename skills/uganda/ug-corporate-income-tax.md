---
name: ug-corporate-income-tax
description: >
  Uganda corporate income tax for companies and branches, tax year 2026-27: the 30% rate, withholding on dividends, interest, royalties and fees, the 2026 changes on interest caps, arm's length, hotels and bad debts, provisional tax and the annual return. Use for Uganda questions from URA taxpayers, employers, advisers and foreign investors, including rates, thresholds, filing dates, the URA portal and worked computations. Figures for tax year 2026-27 come from Uganda Revenue Authority pages and the law, and items that could not be opened are named as unverified in the Sources section. Not reviewed by a licensed accountant.
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

# Uganda Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026-27 (year of income 1 July 2026 to 30 June 2027).

## Who this applies to

Companies resident in Uganda on worldwide income, and non-residents on Uganda-source income. Mining and petroleum run on separate rules. Trustees and retirement funds pay 30% (2021 text).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Company rate, other than mining | 30% | 2024 text | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 |
| Mining companies | 70 - 1500/X, floor 25%, ceiling 45% | 2021 text | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |
| Non-resident rate on payments | 15% | 2024 text | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 |
| Interest on government securities, non-resident or resident | 20% to 10 years; 10% at 10 years or more | 2021 text | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |
| Interest and dividends, resident | 15%; listed-company dividends to individuals 10% | 2021 text | same |
| Designated agent payments | 6% of gross | 2024 text | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 |
| Widely issued debentures to overseas bank | 5% on gross interest | 2026-27 | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ |
| Telecom commissions | 10% on gross | 2026-27 | same |
| Insurance agent commission | 10%, final | 2026-27 | same |
| Betting and gaming winnings | 15% | 2026-27 | same |
| Public entertainer | 6% on gross | 2026-27 | same |
| Shipping and aircraft income | 2% | 2021 text | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |

## The base

Gross income less allowed deductions. An assessed loss carries forward (2021 text, s.38). Rental: where a non-individual's rental expenses and losses exceed 50% of rental income, the deduction is limited to 50% (https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23).

2026 changes, from 1 July 2026 (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/):
- Royalty includes software.
- Interest cap (s.25): a group needs at least 51% common underlying ownership, dormant members are excluded, and brought forward losses are excluded from the earnings base.
- Controlled transactions, meaning between associates, must follow the arm's length principle.
- Microfinance deposit taking and tier 4 institutions may deduct qualifying bad debts.
- Bujagali hydro income is exempt to 30 June 2032.
- A hotel or tourism developer is exempt if the investment is at least USD 10m for a foreigner or USD 5m for a citizen, with the 70% local inputs and citizen staff tests.
- Infrastructure bonds need not be listed. BADEA and the Uganda Red Cross are listed institutions.

## Deadlines and filing

Provisional tax: two instalments, last day of months 6 and 12, each (50% x estimated tax) less tax withheld (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.111). Annual return: within six months of year end (https://ura.go.ug/en/domestic-taxes/returns/); extension up to 90 days in aggregate, payment date unchanged. Withholding returns: 15th of the following month (https://ura.go.ug/en/domestic-taxes/returns/).

Portal steps from URA: click File a Return at https://ura.go.ug, log in with the TIN, open the e-services return menu, upload the template. Box numbers are not on the page read. To register, upload the template with the certificate of incorporation and company form 20 ([URA](https://ura.go.ug/en/domestic-taxes/tin-application/tin-registration-non-individual/)).

## Penalties and interest

Late payment: 2% a month (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.136). EFRIS: failure to use the device, or to issue an e-invoice, or tampering, costs double the tax due or 10 currency points, whichever is higher (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). Objection: 45 days (https://ura.go.ug/en/domestic-taxes/objection-appeals/object-to-tax-assessment/). Waivers: see the [income tax skill](ug-income-tax.md).

## Cross-border points

Branch: repatriated income is taxed at the Part IV rate, 15% (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.83 and nearby). Royalties to non-residents: 15% withholding, not digital service tax (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). Treaties reduce rates; read the treaty.

## Two worked examples that recompute

Example 1. Chargeable income UGX 100,000,000 at 30% gives UGX 30,000,000.

```oa-check
name: Company at 30%
inputs:
  income: 100000000
steps:
  - tax: income * 0.30
expected:
  tax: 30000000.00
```

Example 2. A decision: pay the first instalment on an estimate of UGX 30,000,000 with UGX 2,000,000 already withheld. Instalment = 15,000,000 - 2,000,000 = UGX 13,000,000.

```oa-check
name: First provisional instalment
inputs:
  estimate: 30000000
  withheld: 2000000
steps:
  - instalment: estimate * 0.5 - withheld
expected:
  instalment: 13000000.00
```

## Ask the client first

- Accounting date?
- Sector: mining, petroleum, finance, hotel?
- Member of a group, and payments to associates?
- Payments to non-residents?
- Tax withheld so far?

## Sources

| Source | URL | Read on |
|---|---|---|
| URA, Tax Amendments FY 2026-27 handbook (36-page PDF, all read); printed before the Income Tax and Excise Acts were assented | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ | 2026-11-01 |
| URA notice, effective date of Income Tax (Amendment) Act 2026, 23 Sep 2026 | https://ura.go.ug/en/effective-date-of-the-income-tax-amendment-act-2026-and-the-excise-duty-amendment-act-2026/ | 2026-11-01 |
| URA, File a Tax Return page (still shows the old UGX 2,820,000 threshold) | https://ura.go.ug/en/domestic-taxes/returns/ | 2026-11-01 |
| URA compendium of domestic tax laws, as of July 2021: ITA Cap 340, VAT Act Cap 349 (only the sections cited; old numbering) | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ | 2026-11-01 |
| Income Tax Act, ULII consolidated text at 2024-12-23 (read in a browser: Schedule tables and rate lines only) | https://ulii.org/akn/ug/act/1997/11/eng@2024-12-23 | 2026-11-01 |
| URA, Object to Tax Assessment | https://ura.go.ug/en/domestic-taxes/objection-appeals/object-to-tax-assessment/ | 2026-11-01 |

Not yet confirmed: loss restriction (old file: 50% restriction beyond 7 years; not found in the text searched); 0% on dividends where a resident company holds 25% or more of the voting power; 15% management fee row wording and the UGX 1,000,000 threshold on the 6% designated agent rate; branch remittance section number in the 2024 revised text; the enacted Income Tax (Amendment) Act 2026 text; TP documentation rules.

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
