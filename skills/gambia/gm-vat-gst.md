---
name: gm-vat-gst
description: "VAT for The Gambia (tax year 2026): 15% rate, registration thresholds, exempt supplies, monthly filing and refunds. Built from official GRA, SSHFC and Ministry of Justice pages."
jurisdiction: GM
tax_year: 2026
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gambia VAT

## Who this applies to

Businesses making taxable supplies in The Gambia, and importers. Below the voluntary threshold a business cannot register or charge VAT.

## Rates, bands and thresholds

Basis for 2026: the rows below come from the GRA and SSHFC pages live on 1 November 2026. The Income and Value Added Tax Act 2012 and any 2026 amending Act could not be opened, so a 2026 change that GRA has not published is not reflected.

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% | 2026 | https://www.gra.gm/domestic-faqs |
| Exports of goods and services | 0% | 2026 | https://www.gra.gm/domestic-faqs |
| Compulsory registration | Taxable supplies of at least D2,000,000 in a tax year | 2026 | https://www.gra.gm/domestic-faqs |
| Voluntary registration | Taxable supplies of D1,000,000 and above in a tax year | 2026 | https://www.gra.gm/domestic-faqs |
| De-registration | Registered 2 years, turnover below D1,000,000 for the previous 12 months, filed regularly | 2026 | https://www.gra.gm/domestic-faqs |
| Exempt electricity and water | Monthly domestic use below 1,000 kWh and water below 250 cubic metres | 2026 | https://www.gra.gm/download-file/8d0cfa28-d217-11ed-9b31-029254d29bb1 |

## The base

Registered suppliers' prices include VAT: the VAT is price / 115 * 15. VAT is collected at import and on domestic taxable supplies. Input VAT is credited against output VAT.

Exempt: basic foods (rice, sugar, flour, cooking oil, onions, potatoes and similar), education, prescription drugs, medical, dental, veterinary and optical services, agriculture and aquaculture products, inputs and equipment, unprocessed agricultural and aquacultural products, life and health insurance, financial services not rendered for a fee or commission, domestic transport and ferry services excluding tourism transport, rental or supply of residential property.

Registrants keep records, display the certificate at all premises, issue VAT-inclusive invoices and quote prices with VAT.

## Deadlines and filing

Return and payment are monthly, by the 15th of the following month. A nil return is required. Import VAT is paid before release. Refunds: diplomatic missions and diplomats, international organisations, NGOs, registrants on credit for three consecutive months, and registrants with 50% of supplies in the preceding 12 months zero rated.

### How to file on the GRA portal
1. Go to https://www.gra.gm and log in with portal credentials. A new user creates temporary credentials first and registers for a TIN.
2. Select the tax type, then complete the return form or upload it.
3. Upload supporting documents and submit.
4. The system sends an instant e-acknowledgement, then a notice with a document ID used to pay.
5. Pay by bank or another listed platform. The system sends a URL to print the receipt.
To amend or extend, use the same login, select the tax type, return and period, complete the request, upload reasons and submit; GRA notifies approval or rejection. Paper returns go to the nearest DTD office, or to Kanifing Revenue Office for the Large Taxpayer Unit. Box numbers are not listed here because the form could not be read as a PDF.

## Penalties and interest

Offences include failure to register, keep records, lodge, issue VAT invoices or notes, notify changes or apply for cancellation. The Commissioner General can cancel a registration for failure to report. Amounts are on the Not yet confirmed line. Objection within 30 days, then the Tax Tribunal, then the Court of Appeal.

## Cross-border points

Exports are zero rated. Imports of goods and services are taxable; import VAT is paid before goods are released. The rule for non-resident digital suppliers is on the Not yet confirmed line.

## Two worked examples that recompute

GRA's example: a VAT-inclusive supply of D1,150,000 holds D150,000 VAT.

```oa-check
name: VAT in a price
inputs:
  price: 1150000
steps:
  - vat: price / 115 * 15
expected:
  vat: 150000.00
```

Decision: register voluntarily. Net sales D1,500,000, input VAT D120,000 on purchases. Registered, the business pays D105,000 and recovers the D120,000. Unregistered, it charges nothing and bears D120,000. Register if customers can recover VAT or will absorb the 15%.

```oa-check
name: Voluntary registration
inputs:
  sales: 1500000
  input: 120000
steps:
  - output: sales * 0.15
  - payable: output - input
expected:
  payable: 105000.00
```

## Ask the client first

- Taxable supplies in the last tax year?
- Are the supplies exempt, zero rated or standard?
- Importer or exporter?
- Customers VAT-registered?
- Credit position for three months running?

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA Domestic Taxes FAQs (whole), read in full for this skill | https://www.gra.gm/domestic-faqs | 2026-11-01 |
| GRA VAT brochure (whole), read in full for this skill | https://www.gra.gm/download-file/8d0cfa28-d217-11ed-9b31-029254d29bb1 | 2026-11-01 |
| GRA E-Filing brochure (whole), read in full for this skill | https://www.gra.gm/download-file/7937e6d9-48f3-11ef-b086-029254d29bb1 | 2026-11-01 |
| GRA E-Payment brochure (first part), read for the rows cited | https://www.gra.gm/download-file/2d4c2498-48f5-11ef-b086-029254d29bb1 | 2026-11-01 |

Not yet confirmed: The VAT provisions of the Income and Value Added Tax Act 2012 and any 2026 amendment. Non-resident digital supplier registration (old file cited a 2025 reform from a non-official site). Mandatory e-invoicing, reported from the 2026 budget but no official text opened. Penalty and interest amounts. Refund time limits. VAT Return box numbers.

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
