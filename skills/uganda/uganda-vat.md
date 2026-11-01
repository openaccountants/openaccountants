---
name: uganda-vat
description: >
  Uganda VAT return work, tax year 2026-27: the 18% rate, registration threshold of UGX 300,000,000 from 1 July 2026, withholding VAT at 6% and its 2026 e-invoice exception, zero-rated supplies, blocked input tax, EFRIS, supplier patterns, bad debts and penalties. Use for Uganda questions from URA taxpayers, employers, advisers and foreign investors, including rates, thresholds, filing dates, the URA portal and worked computations. Figures for tax year 2026-27 come from Uganda Revenue Authority pages and the law, and items that could not be opened are named as unverified in the Sources section. Not reviewed by a licensed accountant.
version: 2.1
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

# Uganda VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026-27 (year of income 1 July 2026 to 30 June 2027).

## Who this applies to

Persons making taxable supplies in Uganda above the threshold, voluntary registrants, designated withholding agents, and buyers of imported services.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Annual registration threshold | UGX 300,000,000 (was 150,000,000) | 2026-27 | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ |
| Quarterly test, one quarter of threshold | UGX 75,000,000 | 2026-27 | same; s.7(1) in https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |
| Standard rate | unverified: 18% (old file; s.78(2) not opened) | 2026-27 | unverified |
| Withholding VAT | 6% of taxable value; none if an e-invoice or e-receipt is issued | 2026-27 | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ |
| Refund for non-taxable buyer on e-receipts | 5% of tax, on UGX 2,000,000 within 30 days | 2026-27 | same |
| Refund interest cut-off | Excess of not less than 5% of the claim | 2026-27 | same |
| Late return penal tax | Greater of UGX 200,000 or Fifth Schedule charge | 2021 text | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ |

## The base

Zero-rated, 2021 text (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, Third Schedule): exports; international transport; drugs, medicines and medical sundries manufactured in Uganda; educational materials; seeds, fertilisers, pesticides and hoes; sanitary towels and tampons and inputs; leased aircraft and related items; cereals grown and milled in Uganda; National Medical Stores handling of donor medicines.

New exemption 2026: goods and services to contractors and subcontractors of nuclear energy (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). Hotel or tourism developers investing USD 10m (foreigner) or USD 5m (citizen) get input credit on capital supplies made within two years before commissioning, arising on commissioning (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/).

Blocked input tax, 2021 text s.28: passenger automobiles and their repair, unless dealing or hiring; entertainment, unless that is the business or staff meals on own premises; 10% of input tax on telephone services. Mixed use is apportioned.

Bad debts, s.43: unpaid two years after supply, tax paid in full, reasonable steps taken (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/). This corrects the old file's three years, on the 2021 text.

Supplier patterns (classification hints, not law):

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STANBIC UG, STANBIC UGANDA | EXCLUDE | Exempt financial |
| DFCU, DFCU BANK | EXCLUDE | Same |
| STANDARD CHARTERED UG | EXCLUDE | Same |
| CENTENARY BANK | EXCLUDE | Same |
| URA, UGANDA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NSSF UGANDA | EXCLUDE | Social security |
| UMEME | Domestic 18% | Electricity |
| NWSC | Domestic 18% | Water |
| MTN UG, AIRTEL UG | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |


## Deadlines and filing

Register within 20 days of the end of a three-month period above UGX 75,000,000, or at the start of a period where you expect to exceed it (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.7). VAT return: 15th of the following month (https://ura.go.ug/en/domestic-taxes/returns/). Input and output entries must carry FDNs from EFRIS (https://ura.go.ug/en/domestic-taxes/returns/).

Steps: 1. Register on EFRIS: e-invoicing link, portal login, OTP, First time registration, choose e-invoicing or EFD, submit (https://ura.go.ug/en/efris/efris-registration/). 2. At https://ura.go.ug click File a Return. 3. Log in with TIN. 4. Prepare all purchases and sales including exempt. 5. Upload the return. 6. Pay. Withholding VAT is recognised as a payment in the supplier's next return (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.5). Current box numbers were not on any page read; take them from the downloaded template.

## Penalties and interest

Failure to register: double the tax payable for the period (s.65(1)). Late return: see table. Late payment: penal tax at the Fifth Schedule rate. No records: double the tax for the period (s.65(5)). EFRIS failures: double the tax or 10 currency points, whichever is higher (https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/). All 2021 text except EFRIS.

## Cross-border points

Imported services are self-assessed. EAC trade has no intra-community mechanism: goods imported from Kenya bear VAT at customs (old file). Non-resident digital services register through URA's [digital provider page](https://ura.go.ug/en/domestic-taxes/tin-application/non-resident-digital-service-providers-registration/).

## Two worked examples that recompute

Example 1. An agent pays UGX 50,000,000 plus VAT, with no e-invoice. Withheld: 6% of 50,000,000 = UGX 3,000,000. With an e-invoice, nothing is withheld.

```oa-check
name: Withholding VAT
inputs:
  value: 50000000
  rate: 0.18
steps:
  - vat: value * rate
  - withheld: value * 0.06
  - paid: value + vat - withheld
expected:
  vat: 9000000.00
  withheld: 3000000.00
  paid: 56000000.00
```

Example 2. A decision: must a trader with UGX 80,000,000 in one quarter register? Test is 300,000,000 / 4 = 75,000,000, and 80,000,000 exceeds it, so yes.

```oa-check
name: Quarterly registration test
inputs:
  threshold: 300000000
  quarter: 80000000
steps:
  - test: threshold / 4
  - excess: quarter - test
expected:
  test: 75000000.00
  excess: 5000000.00
```

## Ask the client first

- Taxable turnover in the last three months and the next three?
- Registered, and on EFRIS?
- Customer a designated withholding agent, and was an e-invoice issued?
- Exports or imported services?
- Passenger cars or entertainment in inputs?

## Sources

| Source | URL | Read on |
|---|---|---|
| URA, Tax Amendments FY 2026-27 handbook (36-page PDF, all read); printed before the Income Tax and Excise Acts were assented | https://ura.go.ug/en/download/tax-amendments-fy-2026-2027/ | 2026-11-01 |
| URA, File a Tax Return page (still shows the old UGX 2,820,000 threshold) | https://ura.go.ug/en/domestic-taxes/returns/ | 2026-11-01 |
| URA, EFRIS registration | https://ura.go.ug/en/efris/efris-registration/ | 2026-11-01 |
| URA compendium of domestic tax laws, as of July 2021: ITA Cap 340, VAT Act Cap 349 (only the sections cited; old numbering) | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ | 2026-11-01 |

Not yet confirmed: 18% standard rate in the law; the exempt list (old file: unprocessed foodstuffs, financial services, medical, education, unfurnished residential rent, social welfare, burial, postal, domestic water; furnished rent treatment); deemed supplies and the UGX 100,000 gift limit; Fifth Schedule rates (old file: 2% a month, compounding); box numbers 1 to 15 in the old file, including Box 14 for withholding credits; aircraft and diplomatic zero rating; revised-edition section numbers; the enacted VAT (Amendment) Act 2026 text; whether the 2021 Schedules were changed between 2022 and 2025. Old tests kept in mind: UGX 20m sale gives 3.6m output; 500,000 gift gives 90,000 only if the deemed supply rule holds.

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
