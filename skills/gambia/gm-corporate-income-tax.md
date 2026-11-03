---
name: gm-corporate-income-tax
description: "corporation tax for The Gambia (tax year 2026): 27% rate, turnover minimum, fringe benefits, capital gains, withholding, filing steps. Built from official GRA, SSHFC and Ministry of Justice pages."
jurisdiction: GM
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gambia Corporate Income Tax

## Who this applies to

Companies, partnerships and bodies of trust operating in The Gambia. Those incorporated or controlled in the country are resident and taxed on all income; non-residents on Gambian-source income only. Special Investment Certificate and Export Processing Zone Licence holders are exempt for the specified duration, as are those qualified under a treaty; all companies still file.

## Rates, bands and thresholds

Basis for 2026: the rows below come from the GRA and SSHFC pages live on 1 November 2026. The Income and Value Added Tax Act 2012 and any 2026 amending Act could not be opened, so a 2026 change that GRA has not published is not reflected.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Corporation tax | Higher of 27% of net profit, 1% of turnover (audited) or 2% of turnover (unaudited) | 2026 | https://www.gra.gm/domestic-faqs |
| Fringe benefits tax | 27%, on the employer | 2026 | https://www.gra.gm/domestic-faqs |
| Capital gains, companies, partnerships, trustees | Higher of 25% of the gain or 10% of the consideration | 2026 | https://www.gra.gm/domestic-faqs |
| Dividends | 15% of gross, final | 2026 | https://www.gra.gm/download-file/8d0c84c3-d217-11ed-9b31-029254d29bb1 |
| Contracts: resident | unverified: GRA FAQ says 10%, brochure says 8% | 2026 | https://www.gra.gm/domestic-faqs |
| Contracts: non-resident | unverified: GRA FAQ says 15%, brochure says 10% | 2026 | https://www.gra.gm/domestic-faqs |
| Public works for government, resident contractor | 5% | 2026 | https://www.gra.gm/download-file/8d0d0925-d217-11ed-9b31-029254d29bb1 |
| Air tickets | 1% | 2026 | https://www.gra.gm/download-file/8d0d0925-d217-11ed-9b31-029254d29bb1 |
| Rent: commercial | 15% of gross | 2026 | https://www.gra.gm/domestic-faqs |
| Rent: residential | 8% of gross | 2026 | https://www.gra.gm/domestic-faqs |

## The base

Net profit adjusted for tax, or turnover where the minimum applies. Companies use the accrual method; partnerships and trusts may use accrual or cash. Allowed: cost of stock sold, income-generating expenditure, qualified pension contributions, capital allowance and amortisation, pre-commencement expenditure, business bad debts, losses carried forward within six years, treaty foreign tax credit. Not allowed: closing stock, fines, personal expenditure, taxes (except on fringe benefits), bribes, entertainment, depreciation and capital expenditure, gifts, prizes, donations, losses carried back.

Fringe benefits (housing, vehicle, loans, household staff, debt waiver and others) are taxed at fair value grossed up by dividing by (1 - rate). Exempt: exempt pension contributions, government-provided benefits, benefits to employees with exempt income.

## Deadlines and filing

| Item | Due |
|---|---|
| Corporate return and final payment | 31 March (3 months after year end) |
| Quarterly instalment on quarterly turnover | 15 days after quarter end |
| Withholding schedule and payment | 15 days after month end |
| Withholding statement | 2 months after year end |
| Fringe benefits | Monthly return, 15 days after month end, per FAQ and E-Filing brochure; the FBT brochure says annual with quarterly payments |
| Rental return | 31 March; quarterly declaration and payment |
| Capital gains | 15 days after disposal |

A filing extension needs at least 90% of the liability paid, an application before the due date, at most 30 days, once a year. Issue a withholding certificate to the payee.

### How to file on the GRA portal
1. Go to https://www.gra.gm and log in with portal credentials. A new user creates temporary credentials first and registers for a TIN.
2. Select the tax type, then complete the return form or upload it.
3. Upload supporting documents and submit.
4. The system sends an instant e-acknowledgement, then a notice with a document ID used to pay.
5. Pay by bank or another listed platform. The system sends a URL to print the receipt.
To amend or extend, use the same login, select the tax type, return and period, complete the request, upload reasons and submit; GRA notifies approval or rejection. Paper returns go to the nearest DTD office, or to Kanifing Revenue Office for the Large Taxpayer Unit. Box numbers are not listed here because the form could not be read as a PDF.

## Penalties and interest

GRA lists offences: failure to keep records, pay, or file, false information, failure to notify, failure to recover tax from a person holding money for a taxpayer, improper TIN use, obstruction. Amounts are on the Not yet confirmed line. Objection within 30 days, then the Tax Tribunal; GRA's corporation brochure says then the High Court, other brochures say the Court of Appeal.

## Cross-border points

Dividends paid to resident and non-resident shareholders carry 15%. Withholding on contracts stops only where a treaty or qualified donor-funded project provides. Foreign tax credits apply first in the credit order, then instalments, then non-final withheld tax; unused credits last 3 years, first in first out. Interest and royalty rates are on the Not yet confirmed line.

## Two worked examples that recompute

X and Co (GRA's example): turnover D5,000,000, profit D1,500,000. Tax on profit D405,000 beats the turnover tests.

```oa-check
name: Profit test wins
inputs:
  profit: 1500000
  turnover: 5000000
steps:
  - tax: max(profit * 0.27, turnover * 0.02)
expected:
  tax: 405000.00
```

Decision: audit or not. Turnover D20,000,000, profit D200,000. Profit tax is D54,000, so the minimum decides: D200,000 audited, D400,000 unaudited. Audit if it costs under D200,000.

```oa-check
name: Audit decision
inputs:
  profit: 200000
  turnover: 20000000
steps:
  - audited: max(profit * 0.27, turnover * 0.01)
  - unaudited: max(profit * 0.27, turnover * 0.02)
  - saving: unaudited - audited
expected:
  saving: 200000.00
```

## Ask the client first

- Resident by incorporation or control?
- Turnover and net profit?
- Audited accounts?
- SIC or EPZ licence?
- Payments to contractors, landlords or shareholders, and are they resident?

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |
| GRA Corporation Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0c7954-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Withholding Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0d0925-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Rental Income Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0ce2c1-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Dividend Income Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0c84c3-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Fringe Benefits Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0ca971-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA Capital Gains Tax brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0c6de0-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA E-Filing brochure (whole), read in full for this skill | https://www.gra.gm/download-file/7937e6d9-48f3-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA E-Payment brochure (first part), read for the rows cited | https://www.gra.gm/download-file/2d4c2498-48f5-11ef-b086-029254d29bb1 | 2026-11-01 |

Not yet confirmed: The Income and Value Added Tax Act 2012 and any 2026 amendment. Contract withholding rates, where GRA pages conflict (10% or 8% resident, 15% or 10% non-resident). Withholding on interest and royalties (old file: 15%, no official source). Fringe benefit filing frequency. Final appeal court. Penalty and interest amounts. Treaty rates. Return box numbers. Rent withholding is stated in the brochure as a contract withholding type; who withholds on residential rent was not confirmed.

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
