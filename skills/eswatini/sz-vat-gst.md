---
name: sz-vat-gst
description: "Eswatini VAT for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about VAT in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: international
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini VAT v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Businesses making taxable supplies in Eswatini, importers of goods, and recipients of imported services. Tax year: calendar 2026 periods.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15%, since 1 August 2018 | 2026 | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf |
| Exports and Second Schedule supplies, such as prescribed brown bread and agricultural inputs (fertiliser, seed, pesticide) | 0% | 2026 | https://www.ers.org.sz/documents/EswatiniTax-VAT_Act_2011.pdf |
| Compulsory registration threshold | unverified: ERS Registration page says E900,000; the ERS new business guide says E500,000. Get the Gazette notice under s 6(2) before relying on either | 2026 | https://www.ers.org.sz/Registration |
| Registration test | One quarter of the annual threshold exceeded in any 3 months, or expected at the start of 3 months. Apply within 20 days of the end of the period (s 6) | 2026 | https://www.ers.org.sz/documents/EswatiniTax-VAT_Act_2011.pdf |
| Cancellation | Last 3 months at or below one quarter of the threshold and last 12 months at or below 75% of it | 2026 | https://www.ers.org.sz/documents/EswatiniTax-VAT_Act_2011.pdf |
| Private individual importing services | Reverse charge above E5,000 a month (reg 18) | 2026 | https://www.ers.org.sz/documents/EswatiniTax-VAT_Regulations.pdf |
| Refund minimum, King, Indlovukazi, diplomats and international organisation officials only | Monthly claim where it exceeds E500; otherwise carried to the next period (reg 6(4)) | 2026 | https://www.ers.org.sz/documents/EswatiniTax-VAT_Regulations.pdf |

## The base

VAT applies to most supplies and to imports. Import VAT is charged at entry on customs value plus duties (s 23). Voluntary registration needs a fixed place of business, proper records, reliable returns and the Commissioner General's approval. Legal Notice 130 of 2025, in force from Gazette publication on 17 December 2025, changed the schedules: domestic tap water and waste water services stay exempt, investment-grade gold (99.5%) and silver (99.9%) became exempt when supplied to a licensed financial institution, with Central Bank approval, for trade or investment, condensed milk left the zero rate, and fresh mealies (lifutfo), reusable nappies and inserts, sanitary pads and tampons, and listed medical items are zero rated. Existing exemptions cover items such as residential property, passenger transport, financial and welfare services; see https://www.ers.org.sz/ExemptSupplies and the zero-rated list at https://www.ers.org.sz/VAT/ZeroRated, which predate that notice.

## Deadlines and filing

The Act sets monthly periods and a return within 20 days (ss 31, 32). Regulation 5 makes monthly (Category A) the group with turnover of at least E20 million and quarterly (Category B) the others, by the Commissioner General's written designation. The ERS guide gives 27 days. If you hold no written ERS confirmation of the later date, file within 20 days. Reverse charge declaration and payment: within 30 days of the invoice or payment, whichever is earlier.

### How to file
1. Download the TIN registration form or collect it from an ERS office, and submit it with attachments. ERS answers within 30 days.
2. Display the certificate, charge VAT from the registration date and issue tax invoices.
3. File the return on e-Tax (TaxEase, https://taxease.ers.org.sz/) and pay, quoting the reference.
4. For reverse charge, submit the declaration form at https://www.ers.org.sz/documents/ReverseChargeDeclarationForm.pdf and pay.
5. ERS is rolling out e-invoicing through approved fiscal devices or vendor software; see the e-Invoicing page for your date.

## Penalties and interest

Keep records for 5 years, in Eswatini, in English or siSwati. Penalty rates were not extracted; see the Not yet confirmed line. Where a refund follows an objection, Tribunal or High Court decision, ERS pays interest of 1% a month, and 2% a month if it fails to refund within two months (s 49).

## Cross-border points

Reverse charge does not apply to registered businesses with full input deduction. It is not withholding: 15% income tax withholding applies as well. Exports are zero rated.

## Two worked examples that recompute

Monthly return: output on E200,000 less input of E12,000.

```oa-check
name: VAT payable
inputs:
  sales: 200000
  input_vat: 12000
steps:
  - output: sales * 0.15
  - payable: output - input_vat
expected:
  payable: 18000
```

Decision: compare a foreign and a local provider at E100,000 for a business without full input deduction. Both cost E115,000, so VAT does not decide it. This is the ERS example.

```oa-check
name: Reverse charge and withholding on E100,000
inputs:
  fee: 100000
steps:
  - wht: fee * 0.15
  - to_supplier: fee - wht
  - vat: fee * 0.15
  - total: to_supplier + wht + vat
expected:
  to_supplier: 85000
  total: 115000
```

## Ask the client first

1. What was taxable turnover in the last 3 and 12 months?
2. Which category and tax period did ERS designate in writing?
3. Do you have full input deduction?
4. Do you import services or goods?
5. Are any supplies on the schedules changed in December 2025?

## Sources

| Source | URL | Read on |
|---|---|---|
| Legal Notice 112 of 2018, VAT rate; cited sections read | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf | 2026-11-01 |
| VAT Act 2011, ss 6, 16, 31, 32, 47, 49, Second Schedule; cited sections read | https://www.ers.org.sz/documents/EswatiniTax-VAT_Act_2011.pdf | 2026-11-01 |
| VAT Regulations, regs 5, 6 and 18; cited sections read | https://www.ers.org.sz/documents/EswatiniTax-VAT_Regulations.pdf | 2026-11-01 |
| Legal Notice 130 of 2025, VAT schedules (scanned, OCR); cited sections read | https://www.ers.org.sz/documents/THE_VALUE_ADDED_TAX_ACT_LEGAL_NOTICE_30_OF_2025.pdf | 2026-11-01 |
| ERS, VAT Registration; whole page read | https://www.ers.org.sz/Registration | 2026-11-01 |
| ERS, Reverse Charge Concept; whole page read | https://www.ers.org.sz/ReverseCharge | 2026-11-01 |
| ERS, e-Invoicing; whole page read | https://www.ers.org.sz/e-invoicing | 2026-11-01 |
| ERS, Step-by-Step Guide for New Businesses; whole page read | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf | 2026-11-01 |

Not yet confirmed: The registration threshold (E900,000 or E500,000): Gazette notice not found. The return deadline conflict (20 days in the Act, 27 days in the guide). Commencement notice for the VAT (Amendment) Act 2022. VAT penalty rates. E-invoicing go-live date and regulations, whose pages load by script. Whether the ERS exempt and zero-rated pages reflect all changes.

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
