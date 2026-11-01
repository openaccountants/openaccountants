---
name: sh-services-tax
description: >
  Saint Helena island Services Tax for tax year 2026. Saint Helena has no VAT in the tax lists of the Income Tax Office. Services Tax is 10% on insurance and telecommunications services, charged by the provider, paid with a monthly return by the 15th. Covers exclusions, invoicing, refunds for unpaid accounts, records and offences. Use for VAT, GST, sales tax or service tax questions on St Helena. Does not apply to Ascension or Tristan da Cunha.
version: 0.3
jurisdiction: SH
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Saint Helena island: Services Tax v0.3

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. It covers Saint Helena island only, not Ascension or Tristan da Cunha, which have separate laws.

## Who this applies to

Anyone providing insurance or telecommunications services in or from Saint Helena. Tax Guide 12 lists the taxes as income tax, Services Tax and withholding, and lists no VAT or general sales tax. Other businesses charge no Services Tax. Goods bear customs duty at the border: see [cross-border points](sh-cross-border.md).

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Services Tax rate | 10% of the chargeable amount (Services Tax Ordinance s.3(2)) | 2026 | https://www.sainthelena.gov.sh/documents/Services-Tax-Ordinance |
| Filing and payment | By the 15th of each month for the preceding month (s.6(1)) | 2026 | same |
| Records | 5 years after the end of the month (s.7) | 2026 | same |
| Offences | Fine of £2,000 or 6 months, or both (ss.6(3), 7(2), 8(2)) | 2026 | same |
| Appeal | Within 21 days to the Magistrates' Court (s.10) | 2026 | same |

## The base

Taxable services: an insurance service is underwriting or selling a policy, excluding life assurance and policies designed to fund funeral costs. A telecommunications service is one provided for reward and regulated under the Telecommunications Ordinance 1989, including internet services (s.2).

Chargeable amount: all fees, charges, commissions or other sums charged in a calendar month. Sums are charged on the earlier of invoice and receipt of payment (s.4(1)). Not chargeable: sales of hardware such as handsets, modems and decoders, though rental is chargeable; and interest, late payment penalties and similar charges (s.4(2)).

There is no input credit in the Ordinance. This is a tax on the charge, not a VAT.

## Deadlines and filing

1. Add the tax to the invoice and itemise it, or show it on a receipt if there is no invoice (s.5).
2. Total the month's charges.
3. By the 15th, pay the Collector (the Financial Secretary or authorised person) and submit the return in the approved form, showing total fees charged (s.6(1)).
4. Keep records for 5 years.

If an invoice stays unpaid and future payment appears unlikely, the Collector must refund the tax on proof (s.9(1)). If paid later, pay it back (s.9(1A)). Part payments discharge the tax first (s.9(2)).

## Penalties and interest

Overdue tax bears interest at the prescribed rate (s.6(2)). Failure to pay, failure to file and a knowingly false return are offences (s.6(3)). Directors can be liable (s.12). Unpaid tax is recoverable as a civil debt in the Magistrates' Court (s.11).

## Cross-border points

The charge falls on services provided in or from Saint Helena by a service provider. The Ordinance has no rule for services bought from overseas providers.

## Two worked examples that recompute

Example 1: £1,000 of charges in a month, plus £200 of handset sales.

```oa-check
name: Monthly tax
inputs:
  charges: 1000
  handsets: 200
  rate: 0.1
steps:
  - tax: charges * rate
  - invoice: charges + handsets + tax
expected:
  tax: 100.00
  invoice: 1300.00
```

Example 2: invoice of £1,100 including £100 tax; the customer pays £550. The tax is discharged first.

```oa-check
name: Part payment
inputs:
  paid: 550
  tax: 100
steps:
  - toward_charge: paid - tax
expected:
  toward_charge: 450.00
```


## Ask the client first

- Is the service insurance or telecommunications?
- Any life or funeral policies?
- Hardware sold or rented?
- Bad debts?

## Sources

| Source | URL | Read on |
|---|---|---|
| Services Tax Ordinance 2011, read in full | https://www.sainthelena.gov.sh/documents/Services-Tax-Ordinance | 2026-11-01 |
| Tax Guide 12, Questions on Taxes and Allowances (April 2024), read in full | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-12-Questions-on-Taxes-Allowances-on-St-Helena | 2026-11-01 |

Not yet confirmed: The prescribed interest rate. The approved return form and where it is sent. Regulations under s.13: the consolidation says none to 1 November 2017; later instruments were not audited.

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
