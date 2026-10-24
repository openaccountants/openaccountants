---
name: no-transfer-pricing
description: >
  Screen Norwegian controlled-transaction reporting and transfer-pricing
  documentation, distinguish size exemptions and prepare method-selection
  evidence. Current statutory scope, special exceptions and independent
  review remain outstanding.
jurisdiction: "NO"
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.2
---

# Norway transfer-pricing preparation v0.2

## Who this applies to

Use this draft for corporate controlled transactions and balances involving Norway, including foreign-enterprise screening. Confirm the statutory related-party definition and PE scope before applying the tests below. A foreign address or a small standalone Norwegian entity does not resolve the compliance position.

The foreign-company guidance describes reporting where combined fair-value controlled transactions reach **NOK 10 million**, or combined receivables, debts and guarantees reach **NOK 25 million at period end**. Equality meets either stated threshold. [Foreign-company guidance][screen]

### Statutory scope reproduced in the handbook

Section 8-11(4) uses **at least 50%** direct/indirect ownership or control, including ownership in either direction, common control and specified family-connected routes. Assess each route; do not substitute a majority-only test. Section 8-11(5) extends the duties to dealings between Norwegian entities and foreign PEs, and foreign entities and Norwegian PEs. [Section 8-11(4)–(5)][scope]

Section 8-11(3) withholds the size exemption for the specified information-exchange cases and petroleum taxpayers under Petroleum Tax Act section 5. Identify the actual counterparty jurisdiction and legal exchange entitlement before relying on the exemption. [Section 8-11(3)][scope]

The current URL displays **2025 handbook**. It reproduces statutory wording, but this draft has not independently audited subsequent amendments in the legislation register. [Current handbook][scope]

## Documentation size test

The same guidance describes an exemption for entities that, together with associates, have fewer than 250 employees and either sales no greater than NOK 400 million or balance sheet no greater than NOK 350 million. It excludes dealings with entities in jurisdictions from which Norway cannot demand tax information. [Foreign-company guidance][screen]

This exemption is distinct from the transaction/balance reporting thresholds. Its complete scope, including detailed application of those exceptions, still requires current statutory reconciliation. Do not infer that an exemption from this documentation obligation establishes acceptable pricing, removes other information duties or exempts the tax return.

The size tests involve associates; do not compare only the Norwegian entity's accounts. Preserve the ownership structure and the figures used for each condition. The procedural relationship routes above must be checked separately from any substantive pricing relationship test; no pricing safe harbour is established here.

## Requests and retention

The current Tax Administration handbook reproduces section 8-11(2): documentation must support evaluation against independent-party conditions, be supplied within **45 days of request**, and be retained for **at least ten years after the tax period ends**. [Current handbook][handbook]

Its regulatory discussion requires information and analysis proportionate to transaction value, complexity and the authority's evaluation needs. A prescribed sequence of headings is not required; extensive files need a summary. A general group document must still support the actual transaction. [Current handbook][handbook]

Calendar the actual request, preserve receipt/submission evidence and reconcile the requested material to the relevant period. This draft has not verified extensions, current language requirements, penalties or live submission channels.

## Pricing workpaper and method

The authority's method guidance starts with the delineated transaction, functions/assets/risks and available comparables. It lists CUP, resale price, cost plus, TNMM and profit split. It distinguishes unilateral tested-party methods from profit split, which examines both parties. The choice depends on the evidence; the list does not prescribe a margin. [Method guidance][method]

Other methods require a verifiable process/result and an explanation of why the standard methods are unsuitable. A range does not automatically justify selecting its median: the quality of comparability and the circumstances matter. [Method guidance][method]

As a practical preparation framework:

- Identify parties, relationships, residences, periods and transaction categories.
- Reconcile contracts, invoices and year-end balances to the accounts, including guarantees.
- Describe actual conduct and functions, assets and risks.
- Record comparable searches, adjustments, method choice and rejected alternatives.
- Connect the supported result to the booked amount and tax computation.
- Keep reporting, documentation, requests and foreign adjustments in one reconciliation.

This checklist does not claim to reproduce every statutory documentation item. Financing, services, intangibles, restructurings and PE attribution require transaction-specific work.

## Worked example

Assume two qualifying controlled-transaction categories have established fair values of NOK 6 million and NOK 4 million. Their NOK 10 million total meets the reporting screen. This assumes classification and aggregation are correct; it does not establish documentation liability or a tax adjustment.

```oa-check
name: Norway assumed controlled transaction reporting boundary
inputs:
  goods_fair_value: 6000000
  services_fair_value: 4000000
  reporting_threshold: 10000000
steps:
  combined_fair_value: goods_fair_value + services_fair_value
  excess_over_threshold: combined_fair_value - reporting_threshold
expected:
  combined_fair_value: 10000000
  excess_over_threshold: 0
```

### 2. Period-end balance threshold

Assume qualifying year-end receivables of NOK 8 million, debt of NOK 12 million and guarantees of NOK 5 million. Their NOK 25 million total meets the balance reporting screen. Eligibility, valuation and avoiding duplication are assumed; transaction reporting is a separate screen.

```oa-check
name: Norway assumed period end controlled balances
inputs:
  receivables: 8000000
  debt: 12000000
  guarantees: 5000000
  balance_threshold: 25000000
steps:
  combined_balance: receivables + debt + guarantees
  excess_over_threshold: combined_balance - balance_threshold
expected:
  combined_balance: 25000000
  excess_over_threshold: 0
```

## Ask the client first

- What relationships, residences, transactions and PE dealings exist?
- Which balances, guarantees and fair values reconcile to the accounts?
- What associate-level employee, sales and asset figures support the size screen?
- Which jurisdictions and special tax regimes affect the exemption?
- What pricing evidence, requests, filings and foreign adjustments exist?

## Sources and review limits

Read 23 October 2026 through indexed official text:

- [Foreign-company reporting/documentation guidance][screen].
- [Current handbook, section 8-11(2)][handbook]; [full section 8-11][scope], directly opened on 23 October 2026, displaying the 2025 edition.
- [Method-selection guidance][method], published 28 October 2025.

Not yet confirmed: complete current statute and regulations, complete related-party/PE application, reporting form and deadline, petroleum and other exemption exceptions, language, full documentation contents, sanctions, CbCR, treaty relief and live filing. Independent review and professional attestation remain outstanding. Norway's TP and country coverage remain partial. Retired guidance and historical handbook editions must not substitute for current law.

[screen]: https://www.skatteetaten.no/en/business-and-organisation/foreign/tax-returns-and-tax-assessment-notices/transfer-pricing/
[handbook]: https://www.skatteetaten.no/en/rettskilder/type/handboker/skatteforvaltningshandboken/gjeldende/kapittel-8-opplysningsplikt-for-skattepliktige-trekkpliktige-mv/ID-8-11.001/ID-8-11.009/
[method]: https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/foreign-large-companies-and-groups/transfer-pricing/specific-transfer-pricing-topics/how-to-conduct-a-comparability-analysis/comparability-and-pricing/select-method/

[scope]: https://www.skatteetaten.no/en/rettskilder/type/handboker/skatteforvaltningshandboken/gjeldende/kapittel-8-opplysningsplikt-for-skattepliktige-trekkpliktige-mv/ID-8-11.001/
