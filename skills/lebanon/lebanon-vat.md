---
name: lebanon-vat
description: "Use this Guide for Lebanon VAT, TVA Lebanon and Ministry of Finance return questions in 2026. It confirms the budget amendments to periodic filing, deduction for passenger cars, blocked utility costs and input-credit refunds. It supplies two recomputing working-paper cases using already established tax amounts and the car deduction cap. It does not certify the current VAT rate, registration threshold, supplier-based exemptions, foreign-service treatment or current portal form. Those items and the effect of extensions and suspended legal time limits are named non-operative holds. Do not infer a legal classification from a bank label or use the examples as approval to file."
version: 2.2
jurisdiction: LB
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Lebanon VAT

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Lebanon.

## Who this applies to

Lebanon VAT working papers for businesses registered or potentially liable under Law 379/2001. This revision confirms specific 2026 deduction and filing amendments. It does not certify the standard rate or registration threshold. Until VAT-H1 is resolved, stop before applying a rate, deciding registration or submitting a return. An invoice tax amount alone does not prove its legal rate or recoverability.

## Rates, bands and thresholds

| Rule and conditions | Amount | Official source |
|---|---|---|
| Periodic return and payment statutory time limit; any specific extension/suspension must be checked | One month replaces twenty days in VAT Law arts. 35(4), 39 | [Budget 40/2026 art. 51, p. 79](https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf) |
| Ordinary tourist/passenger car acquisition for taxable activity | VAT deduction limited to tax attributable to USD 30,000 excluding VAT, proportional where cost is higher | [Budget 40/2026 art. 30 replacing VAT Law art. 28, pp. 40-41](https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf) |
| Car-cap exception | Cap does not apply to fare-paying passenger transport, car rental, or classified hotels/resorts with four stars or more | same |
| Annual excess-input refund request, and exporter period-end request | Within one month; minimum LBP 200 million claimed | [Budget 40/2026 art. 31 replacing VAT Law art. 30, pp. 41-42](https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf) |
| VAT standard rate and compulsory-registration threshold | Unverified: hold VAT-H1; no operative rate or threshold supplied | [MoF VAT rate page](https://www.finance.gov.lb/ar-lb/Taxation/Companies/VAT/Pages/Tax-Rate.aspx) |

## The base

Separate transactions by their legal character and evidence, not a supplier name. The old automatic BANK AUDI/BLOM/BYBLOS/BANKMED/FRANSABANK, government, utilities and SaaS pattern rules are hold VAT-H2. A bank-statement label is insufficient to identify an exempt supply, import VAT or deductible input.

Budget 2026 art. 30 permits deduction for taxable economic activity and the export/international-transport operations identified by VAT Law arts. 19-21. It addresses pre-registration stock and fixed assets expressly. Water, electricity, communications, internet and petrol costs are expressly non-deductible in amended art. 28; the old utility rows cannot establish input recovery. Keep the invoice and the business-use allocation, and test the car cap and exceptions before deduction. The older entertainment, gifts, personal-use, alcohol/tobacco and club rules need their own current source: VAT-H2.

For mixed activity, calculate the right-to-deduct turnover ratio under VAT Law art. 31 and the Ministry's declaration guidance, then apply the supported ratio to common input. The worked cases use established output and eligible input amounts, not an assumed VAT rate. The exact annual adjustment and excluded turnover items remain VAT-H3.

## Deadlines and filing

The Ministry declaration page identifies calendar quarters, but still displays obsolete twenty-day and postal instructions. Budget art. 51 takes priority for the statutory month. Do not turn that into unconditional dates: extensions, legal suspensions, the active electronic form and payment route remain VAT-H4. Obtain registration details, period, full sales/purchase ledger, invoices, imports, credits and exchange-rate evidence; reconcile the working paper; obtain the current form and payment reference; then have the filing reviewed before submission. The old A-H return layout is held, not an asserted current form.

Budget art. 35 separately requires monthly electronic fixed-stamp declarations within fifteen days of month end for persons obliged to issue invoices/receipts/credit or debit notes, excluding licensed stamping-machine users. It contains its own historic application and transition provisions. Stamp amounts, active fields and late-period treatment remain VAT-H5; this is not VAT output tax.

## Penalties and interest

Do not use the old daily late-filing or monthly late-payment amounts. VAT-H6 covers current penalties and any relief. Budget art. 18 concerns beneficial-owner reporting. The special 2024-refund window in art. 41, and the public-entity penalty settlement in art. 43, require publication, suspension and extension checks before use.

## Cross-border points

Non-resident services, tax representation, import valuation, exchange rates, duty-free supplies and land/real-estate treatment remain VAT-H7. Do not assume every foreign SaaS purchase is a net-zero reverse charge. The customs advance belongs in [Corporate income tax](lb-corporate-income-tax.md), separate from import VAT.

## Two worked examples that recompute

An established taxable transaction set has output VAT LBP 8 million and eligible input LBP 3 million. The working-paper net payable is LBP 5 million. These amounts are inputs already checked against invoices and the law; this example does not establish a rate.

```oa-check
name: Reconciled output less eligible input
inputs:
  output: 8000000
  eligible_input: 3000000
steps:
  - payable: output - eligible_input
expected:
  payable: 5000000
```


Deduction decision under amended art. 28: a USD 40,000 excluding-VAT passenger car has an independently verified VAT charge LBP 400 million and full taxable use. Ordinary business recovery is LBP 300 million under the proportional cap. If the vehicle qualifies for the fare-paying transport exception, the cap does not reduce that LBP 400 million. The classification changes recovery by LBP 100 million. Other eligibility and currency rules still require evidence.

```oa-check
name: Passenger car cap versus qualifying transport
inputs:
  car_usd: 40000
  cap_usd: 30000
  verified_tax_lbp: 400000000
steps:
  - ordinary_recovery: verified_tax_lbp * min(car_usd, cap_usd) / car_usd
  - transport_recovery: verified_tax_lbp
  - difference: transport_recovery - ordinary_recovery
expected:
  ordinary_recovery: 300000000
  transport_recovery: 400000000
  difference: 100000000
```


## Ask the client first

- What are the registration status, period, turnover and supply types?
- Which sales, purchases, customs entries and tax invoices support each amount?
- What foreign currency and tax conversion evidence apply?
- Are supplies mixed, exempt, exported or supplied by non-residents?
- Are cars used for ordinary business or a documented cap exception?
- What active portal notices, extensions, credits and refund requests exist?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| Budget 40/2026 arts. 27, 30-35, 41, 51 and closing art. 57; full clauses and neighbours read in images | https://www.finance.gov.lb/en-us/Finance/BI/ABDP/Annual%20Budget%20Documents%20and%20Process/Budget%20Law%202026%20Approved%20by%20Parliament.pdf | 2026-11-01 |
| MoF VAT declaration page, tax periods, deduction, apportionment and non-residents sections; old 20-day/mail instructions superseded or held | https://www.finance.gov.lb/ar-lb/Taxation/Companies/VAT/Pages/Declaration.aspx | 2026-11-01 |

Not yet confirmed: VAT-H1: current standard rate, any enacted rate change, registration threshold and rolling-period rules. VAT-H2: all legacy supplier-pattern classifications, exemptions, zero rating and blocked-input categories not expressly confirmed above. VAT-H3: full apportionment and annual adjustment. VAT-H4: current form boxes, portal/payment steps and 2026 deadlines after extension/suspension. VAT-H5: stamp amounts and transition implementation. VAT-H6: penalty amounts, settlement and exceptional refund-window availability. VAT-H7: reverse charge, non-resident agent procedure, customs/excise valuation, exchange rate, real estate, gold and special schemes. Prior numeric examples and A-H form rows are historical only in the immutable lineage ledger.

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
