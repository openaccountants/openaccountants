---
name: zimbabwe-vat
description: >
  Zimbabwe VAT return work, tax year 2026: the 15.5% standard rate from 1 January 2026, registration at USD 25,000, VAT categories, returns on the 10th and payment on the 15th, fiscal tax invoices through FDMS, imported services paid in USD, digital services withholding tax, and 10% export taxes on some minerals. Use for classifying transactions, preparing a VAT return, or questions such as what is the VAT rate in Zimbabwe, do I need to register for VAT with ZIMRA, or can I claim input tax on this invoice.
version: 2.1
jurisdiction: ZW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zimbabwe VAT

## Who this applies to

Traders whose taxable supplies exceed or are expected to exceed USD 25,000 or ZiG equivalent in 12 months, voluntary registrants, and buyers of imported services. Traders dealing only in exempt supplies do not register.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Standard rate | 15.5% | 2026 | From 1 Jan 2026; 15% before; Act s.34 | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf |
| Zero rate | 0% | 2026 | Section 10, mainly exports; the regulations' zero-rated list was repealed from 1 Jan 2024 | https://www.zimra.co.zw/domestic-taxes/vat/mechanics-of-vat |
| Compulsory registration | USD 25,000 | 2026 | Or ZiG equivalent, 12 months | https://www.zimra.co.zw/domestic-taxes/vat/vat-registration |
| Category C threshold | USD 240,000 | 2026 | Or ZiG equivalent | same |
| Category D threshold | USD 120,000 | 2026 | Or ZiG equivalent | same |
| No fiscal invoice needed | under USD 10 | 2026 | Or ZiG equivalent | same |
| Refund held in credit | under USD 60 | 2026 | Until cumulative refunds reach USD 60 | https://www.zimra.co.zw/domestic-taxes/vat/mechanics-of-vat |
| Digital services withholding | 15.5% | 2026 | Foreign supplier not VAT registered | https://www.zimra.co.zw/public-notices |
| Digital services withholding, registered supplier | 3/23 tax fraction | 2026 | As stated in Public Notice 5 of 2026 | same |
| Export tax on lithium ore or concentrate | 10% | 2026 | Lithium sulphate 0%; Act s.39 | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf |
| Export tax on chrome, antimony | 10% | 2026 | Paid in USD; Act s.42 | same |

## The base

Output tax is charged on taxable supplies, imported goods and imported services. From 2024 food and similar items sit in the exemptions, not the zero rate, and from 2026 s.11 also exempts prescribed agricultural goods and services, prescribed medicines, and rural electrification services funded by the Rural Electrification Fund. Zero-rated or exempt items supplied as part of entertainment are a single standard-rated supply (Act s.36).

Input tax is claimed within 12 months of the invoice date. From tax periods in 2026 there are no manual input schedules unless the Commissioner approves: fiscal invoices auto-populate from FDMS into Invoice Management in TaRMS, and only an invoice showing Valid on the FDMS portal with correct buyer details counts. An invoice must carry the TIN and a QR or authentication code (Act s.45). A registered operator must issue fiscal tax invoices within 30 days of supply.

Supplier patterns carried from the earlier version, to be checked against the invoice: banks exclude as financial services; ZIMRA and NSSA exclude; customs check for import VAT; ZESA, ZETDC, ZINWA, Econet, NetOne and Telecel at the standard rate only with a valid fiscal invoice; Google, Microsoft and AWS see imported services below.

## Deadlines and filing

Return for the tax period: 10th of the next month. Payment: 15th of the next month (SI 81 of 2025 as stated in Public Notices 11 and 49 of 2026). ZIMRA's Mechanics of VAT page still says the 25th; the notices are later and control. Categories A and B file in alternating months and Category C every month, as the notices show. Keep records six years.

To register: in TaRMS go to Taxpayer Profile, Tax Type, New Tax Type, select VAT; select Local / Export Sales; set the effective date as the first day of the month after the threshold; choose compulsory or voluntary; enter taxable turnover in USD; attach the sales schedule, invoices or contracts, stamped bank statement, public officer letter and lease or title deed.

To file:

1. Log into mytaxselfservice.zimra.co.zw and select your TIN.
2. Tax Return Management, Pending Returns, select the VAT return.
3. Declare standard rated supplies, zero rated local and exports, exempt supplies and imported services. On the paper VAT 7 these are lines 9, 10, 10a, 12 and 13; total output is line 20, and input starts at line 21. The return also has a 10% exports rate.
4. Pick input tax from Invoice Management. Attach Value Added Withholding Tax certificate schedules.
5. Submit, then pay by the 15th with TIN and name.

## Penalties and interest

Section 39 interest now also covers tax under s.13 (Act s.47). Non-payment of digital services withholding carries a further 15% and personal liability of the intermediary. The older USD 30 a day and 10% figures were not reconfirmed.

## Cross-border points

The buyer self-accounts for VAT on imported services that are not electronic, and from 2026 pays it in USD (Act s.43). For electronic services, banks and mobile money operators withhold at the rates above; if payment goes through a foreign platform, the non-resident supplier accounts in full and credits any tax withheld. The withholding return is filed by hand at a ZIMRA office until configured. Physical goods stay under import VAT.

## Two worked examples that recompute

Sale of USD 10,000 at 15.5%, input on valid fiscal invoices USD 775: net 775.

```oa-check
name: Simple period at 15.5%
inputs:
  sales: 10000
  input_tax: 775
steps:
  - output: sales * 0.155
  - net: output - input_tax
expected:
  net: 775.00
```

Edge case from Public Notice 7 of 2026: Category A period straddling the rate change. December supplies 2,000 at 15% give 300, restated 300 / 0.155 = 1,935.48; add January 3,000; declare 4,935.48. Decision: registering voluntarily turns on whether input tax exceeds output tax for your customers; ask.

```oa-check
name: Category A December and January return
inputs:
  dec: 2000
  jan: 3000
steps:
  - dec_tax: dec * 0.15
  - restated: dec_tax / 0.155
  - declared: restated + jan
  - tax: declared * 0.155
expected:
  declared: 4935.48
  tax: 765.00
```

## Ask the client first

1. VAT category and tax period.
2. Turnover in the last 12 months, USD and ZiG.
3. Exports, and of which minerals.
4. Imported services, and how they were paid.
5. Is every input invoice Valid on FDMS.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act No. 7 of 2025 (Veritas copy of the Government Printer text), whole Act | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf | 2026-11-01 |
| ZIMRA Public Notices 5, 7, 11, 49, 50, 58, 61 of 2026 (list page; each PDF opened) | https://www.zimra.co.zw/public-notices | 2026-11-01 |
| ZIMRA VAT Registration page, read thresholds and how to register | https://www.zimra.co.zw/domestic-taxes/vat/vat-registration | 2026-11-01 |
| ZIMRA Mechanics of VAT page, read rates, obligations, input tax | https://www.zimra.co.zw/domestic-taxes/vat/mechanics-of-vat | 2026-11-01 |
| ZIMRA Public Notice 5 of 2026, sections 1 to 8 read | https://www.zimra.co.zw/public-notices | 2026-11-01 |
| ZIMRA VAT 7 form, whole form read, older issue with RTGS wording | https://www.zimra.co.zw/downloads/category/9-domestic-taxes | 2026-11-01 |

Not yet confirmed: the exemption list in the VAT regulations (earlier version: financial, medical, education, residential rental, public transport, postal, water, and as zero-rated: maize meal, bread, milk, sugar, cooking oil, salt, fruit and vegetables, farming inputs, medical supplies, fuel, domestic electricity); blocked input under s.16 (earlier version: vehicles under 9 seats, entertainment, club subscriptions, personal use); gifts over USD 25 as deemed supply; late filing USD 30 a day and late payment 10%; criminal penalty for non-fiscalisation; Category D period; USD to ZiG conversion rule; the 3/23 fraction, which predates 15.5%; SI 81 of 2025 text; the current TaRMS field numbers.

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
