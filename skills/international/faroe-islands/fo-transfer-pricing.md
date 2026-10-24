---
name: fo-transfer-pricing
description: >
  Assess Faroese controlled transactions, distinguish disclosure from written
  documentation, test the small-business exemption and prepare pricing evidence.
  Covers ownership and voting control, the two-year size test and TAKS requests.
  Country-by-country reporting, thin capitalisation and treaty remedies require
  separate analysis. Source-cited draft for 2026; professional review pending.
jurisdiction: FO
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
review_status: pending_review
---

# Faroe Islands transfer pricing v0.1

## Who this applies to

Under Tax Act §37a, covered relationships include foreign control, control of legal persons, common-group entities and foreign/Faroese permanent establishments. Control generally requires **more than 50%** of capital or votes; indirect holdings, related persons and joint-control agreements matter. Denmark and Greenland count as foreign jurisdictions. Section 118a separately requires controlled-transaction disclosure, including domestic relationships. Test both provisions rather than assuming identical wording. [Current Tax Act, §§37a and 118a][law]

This Guide addresses pricing and documentation. It does not determine PE existence, corporate residence, thin-capitalisation adjustments, country-by-country reporting or treaty relief.

## Rates, bands and thresholds

These are documentation thresholds, not tax rates.

| Test | Amount | Period/source |
|---|---:|---|
| Balance sheet total | DKK 36 million | Two consecutive financial years; §118a(6) |
| Net turnover | DKK 72 million | Same |
| Average full-time employees | 50 | Same |

For the §118a(6) exemption, assess the taxpayer alone or together with its group: at each of two consecutive year-ends, at least two limits must not be exceeded. TAKS retains power to demand documentation in special cases. The exemption concerns preparation/retention under subsection 4, not the separate disclosure requirement. [2018 amendment, §1(11), effective 1 January 2019][amendment]; [current §118a(6)][law].

## The base

Use independent-party prices and terms for covered transactions. Keep the ownership chart and voting agreements distinct: multiplication of economic ownership does not establish voting control. [Tax Act §37a][law]

TAKS's older guidance recommends a transaction inventory covering goods, services, financing, intangibles and other economic dealings. Document functions, assets, risks, contracts and comparables; explain the selected method for each transaction type. Its methods include CUP, resale price, cost plus, TNMM and profit split. A single method is not automatically suitable throughout a group. Its DKK 500,000 discussion is **not a blanket exemption for smaller dealings**. [TAKS guidance, pages 8–13][guidance]

Practical workpaper: reconcile each counterparty total to the ledger, identify the pricing evidence available when the transaction occurred, and record why any proposed adjustment follows from that evidence. An illustrative markup is never a safe harbour.

## Deadlines and filing

Disclose transaction type and volume on the tax return. Required written documentation must reach TAKS within **60 days of its request**. [§118a(1), (4)][law]

TAKS's company-return guidance gives **1 July** as the ordinary return deadline. Accounts accompany the return and must be submitted through Borgaragluggin. A justified extension requires application; the published outer limit is **15 August**. Preserve the actual extension decision. [TAKS tax returns][returns]

Do not substitute the Danish documentation timetable. Retrieve the current Faroese return and appendices for the relevant filing year; the 2017 PDF's form identifier is historical.

## Penalties and interest

Missing required documentation permits estimated assessment under §118a(5). That subsection also requires approval from Stýrið before the tax authority makes an arm’s-length income adjustment. This Guide does not quantify fines or interest: their applicable provisions and current amounts remain unverified. Do not interpret that gap as absence of sanctions. [§118a(5)][law]

## Cross-border points

Evaluate the relevant treaty and any corresponding-adjustment procedure separately. The older English guidance is useful for analytical examples but predates the 2019 documentation exemption. It cannot establish current filing obligations on its own. Country-by-country reporting is a separate unresolved topic in this pack.

## Two worked examples that recompute

### 1. Evidence-supported cost plus

Assume the reviewer establishes that DKK 800,000 is the appropriate cost base and independent comparables support a 6% markup for these services. The resulting charge is DKK 848,000. An actual charge of DKK 820,000 leaves DKK 28,000 to investigate; this illustration does not itself authorise a tax adjustment.

```oa-check
name: Faroese services illustrative cost-plus reconciliation
inputs:
  cost: 800000
  markup: 0.06
  actual: 820000
steps:
  supported_charge: cost * (1 + markup)
  difference: supported_charge - actual
expected:
  supported_charge: 848000
  difference: 28000
```

### 2. Documentation size boundary

Assume the consolidated figures are identical in both relevant years: balance sheet DKK 36 million, turnover DKK 73 million and average employees 50. Two limits are met at equality; turnover exceeds its limit. Subject to a special TAKS demand, the subsection 4 documentation exemption applies. Disclosure and arm's-length pricing still need their own assessment. If employees instead average 51 in either year, only one limit is met for that year, so this two-year exemption test fails. [§118a(6), enacted by the 2018 amendment][amendment]

```oa-check
name: Faroese documentation threshold margins
inputs:
  assets: 36000000
  turnover: 73000000
  employees: 50
steps:
  asset_margin: 36000000 - assets
  turnover_margin: 72000000 - turnover
  employee_margin: 50 - employees
  alternative_employee_margin: 50 - 51
expected:
  asset_margin: 0
  turnover_margin: -1000000
  employee_margin: 0
  alternative_employee_margin: -1
```

The checks recompute arithmetic; the legal conclusions require the stated facts and review.

## Ask the client first

- Who owns capital and votes, directly, indirectly and under voting agreements?
- Which related parties and PEs transact, where are they resident, and what are the ledger totals?
- What are the standalone/group figures for each of the two relevant years?
- Has TAKS requested documentation, and when was that request received?
- What evidence supports the pricing method and actual transaction terms?

## Review limits

Source-cited draft, not professional attestation. Current forms, sanctions, documentation retention duration, new-company treatment of the two-year test, CbCR and treaty remedies remain open. The presence of this Guide does not establish comprehensive TP or country coverage.

## Sources

All sources read 23 October 2026.

| Source | Locator |
|---|---|
| Tax Act consolidated through Act 53 of 1 June 2026 | [§§37a, 118a][law] |
| Act 191 of 21 December 2018 | [§1(8)–(11), §2][amendment] |
| TAKS English transfer-pricing guidance, 2017 | [Pages 8–13; historical guidance][guidance] |
| TAKS company-return procedure | [Tax returns][returns] |

[law]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[amendment]: https://logir.fo/Logtingslog/191-fra-21-12-2018-um-broyting-i-logtingslog-um-landsskatt-og-kommunuskatt-Skattalogin
[guidance]: https://taks-2.cdn.fo/savn/2009/171027-transfer-pricing-guidelines.pdf?s=8fH4hUHIJNGzb9vHkqvE-ZUgNzk
[returns]: https://www.taks.fo/en/individuals/tax/tax-return
