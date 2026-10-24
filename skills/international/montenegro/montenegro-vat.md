---
name: montenegro-vat
description: "Prepare 2026 Montenegro VAT workpapers, distinguishing current rates, tax points, registration, place of supply and input recovery. Reconcile the official PR PDV-2 form and IRMS transition; includes six executable mixed-rate, advance, import, recipient-service, shared-input and credit controls. Use for PDV, VAT returns, imports, reverse charge and refund requests. Full implementing rules/special schemes, property corrections, current portal acceptance, procedures and independent country review remain open. Source-cited preparation draft, not professional attestation."
version: 2.1
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
depends_on:
  - vat-workflow-base
sources:
  - url: "https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0"
    title: "VAT consolidation through 12/26"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/80b15e7e-da28-49b7-9ca6-de1849b9ab61?version=1.0"
    title: "12/26 operative VAT amendment"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/e3d2b1f2-341b-487e-8e2a-d77868bbf52e?version=1.0"
    title: "Official PR PDV-2 form and instructions"
    as_of: "2026-10-24"
---

# Montenegro VAT preparation v2.1

## Who this applies to

Prepare Montenegro PDV workpapers for the taxpayer's actual registration status, effective date, supplies, recipient, place, tax point and recovery entitlement. Work with `vat-workflow-base` and retain the country-specific decisions below. A bank description, foreign payer or low turnover does not establish exemption or zero rating. [Articles 3–4, 12–20, 37, 42, 55][law]

This source-cited 2026 draft replaces v2.0 preserved in Git at `38410ae4`. It removes the old invented box table, broad food/accommodation classifications and automatic foreign-receipt/SaaS rules. Ordinary examples below concern October 2026, after the February and April changes. Special schemes, all implementing-rule amendments, current IRMS schema, property/asset corrections, procedure and independent country/professional review remain open.

## Rates and date gates

| Item | Rule / gate | Official source |
| --- | --- | --- |
| Standard rate | 21%, unless a supported reduced/zero/exemption rule applies | Article 24 |
| 7% | Specified basic foods, medicines/devices, textbooks and other enumerated classes; not every food or medical product | Article 24a(1), implementing classification required |
| 15% | Specified accommodation, catering and other enumerated classes; catering exclusions include alcohol, specified sweetened drinks and coffee | Article 24a(2) |
| 0% | Statutory classes including qualifying exports, with their evidence/conditions | Article 25 |
| Domestic small-taxpayer threshold | EUR 30,000 rolling twelve months / likelihood test; voluntary registration has a minimum three-year period; Article 42 does not apply to foreign-established taxpayers | Article 42 |
| Registration application | By the twentieth of the next calendar month after crossing the statutory turnover threshold; effective status follows the authority decision | Article 55 |
| Period / filing / payment | Calendar month; electronic return and payment ordinarily by the fifteenth of the next month; nil-liability returns still required | Articles 33, 35–36 |

Sources: [consolidation through 12/26][law]. Obtain the actual product/service classification, operative implementing list and supply date before choosing a rate. In particular, the old Guide's “15% food” and “7% accommodation” descriptions are superseded. Exemption without credit, zero rating and outside-Montenegro supplies are different categories.

The 12/26 amendment entered into force on publication, 6 February 2026. Its building-land change applies from 1 April 2026, with specified pre-April advances protected up to their amount on the later final invoice. It also changes service place, invoice, correction and registration-number rules. Cases before the operative change need the prior text; the October examples do not validate all earlier-2026 cases. [12/26 Articles 1–16, especially new 72b–72c][amend]

The separate July 104/26 replacement law starts applying on EU accession under its Article 213; Article 212 then repeals the current law. Do not adopt its intra-EU/special-scheme provisions simply because it was enacted in 2026. [Replacement Articles 212–213][future]

## The base and liability

### Registration, supply and tax point

Reconcile qualifying turnover and forecast to a registration schedule, including prior twelve months and decision/effective date. Being below the threshold does not cancel existing registration, eliminate foreign-supplier/recipient duties or establish an exemption for a specific transaction. Cessation requires the Article 56 route and its closing obligations. [Articles 12, 42, 55–56][law]

Maintain a transaction register with contract/invoice/customs reference, parties/status, supply, place article, date, net/gross consideration, tax rate, tax and recovery decision. Article 18 covers invoice/supply events, advances and recipient-liability timing; Article 19 governs import timing. Do not date all tax points by bank settlement or apply the advance rule twice at final billing. [Articles 18–20][law]

For nonresident services, first decide whether the recipient is a taxable person, the establishment actually receiving the service and the general or special place rule. Articles 17a–17j cover property, transport, events, catering, hiring, digital/other services and use/enjoyment. Article 12 governs supplier/representative/recipient liability. An imported-service reverse charge is conditional, not a default for every SaaS or foreign invoice. [Articles 12, 17–17j, 18(8)][law]

Exports require actual statutory/customs evidence. A foreign bank receipt or a customer address alone does not establish export of goods or a 0% service. Keep outside-scope services separate and validate their actual return reporting; invoice wording under amended Article 32 is part of the classification work. [Articles 17–17j, 25, 32][law]

### Consideration, imports and corrections

Article 20 includes qualifying consideration, linked subsidies and incidental amounts and distinguishes discounts and properly evidenced amounts paid in another's name/account. Do not automatically remove every recharge as a disbursement. Corrected consideration and input tax require matching evidence/period treatment. [Articles 20–20a][law]

Import value starts with the customs value and includes the specified duties/taxes and ancillary costs; no second addition of a cost already included. Reconcile customs declaration, importer and payment evidence before claiming recovery. The import example uses an explicitly assumed duty amount, not a researched tariff rate. [Articles 19, 22, 36–37][law]

The 2026 Article 20a bad-debt amendment requires the specified final court/proceeding circumstances and evidence, with tax on subsequent recovery. An overdue invoice or write-off alone does not clear a reduction. Capital/input adjustments under Article 39 have separate equipment/property periods and conditions; a general credit note is not the complete method. [Articles 20–20a, 39][law]; [12/26 Articles 7, 12][amend]

### Input recovery and mixed supplies

Separate directly creditable, directly noncreditable, restricted and shared inputs. Verify valid invoices/customs documentation, period and taxable-business use. Article 37 includes restrictions for specified vehicles/recreation, new residential buildings and representation, with specified vehicle-business exceptions. Do not deduct tax overcharged or invoiced by an unauthorised person merely because it was paid. Recipient-liability recovery has its own Article 37(10) gate. [Article 37][law]

For mixed supplies, Article 38 defines the annual turnover proportion, statutory exclusions, upward rounding to a whole percentage, prior-year provisional rule and annual reconciliation. Include relevant non-price subsidies in the denominator as specified; remove the specified equipment/incidental financial/property amounts. Do not apply a shared-input percentage to an input already wholly disallowed. Estimated/segmented methods require the specified authority consent. [Article 38][law]

Article 39 provides a five-year equipment and ten-year property correction context, with specified changes and a difference threshold over EUR 30. The complete amount/timing and current implementing method have not been developed here; do not infer that every use change is an automatic one-tenth annual adjustment. [Article 39][law]

## Official return mapping and IRMS

The Tax Administration's PR PDV-2 attachment and instructions were downloaded and the two form pages visually inspected. This supersedes the old Guide's boxes 1–20. The attachment predates IRMS; actual current electronic schema/acceptance remains open. [Official form and instructions][form]

| Rows | Published meaning |
| --- | --- |
| 1–8 / 9 | Identity/period/amended-return context / no-transactions marker |
| 10 / 11 / 12 | Taxable supply values at 21% / 15% / 7% |
| 13 / 14 / 15 | 0% supplies / exempt supplies / specified energy supplies with transferred liability |
| 16 / 17 / 18 | Domestic output VAT at 21% / 15% / 7% |
| 19 / 20 | Domestic input VAT / import VAT paid |
| 21 | Foreign-service recipient VAT, with output and input columns |
| 22 / 23 | Specified farmer flat-rate compensation / specified energy recipient VAT |
| 24 | Published total output: 16 + 17 + 18 + 21 |
| 25 / 26 / 27 | Published gross input: 19 + 20 + 21 + 22 / non-deductible input / deductible input: 25 − 26 |
| 28 / 29 / 30 | Payable difference / credit difference / refund-request choice, not a tax amount |

The printed totals do not include energy row 23. Energy cases require current implementing/electronic reconciliation before filing; do not silently extend the printed formula or claim the special scheme verified. Every worked return below excludes energy and farmer cases. For ordinary inputs, row 25 is not automatically all deductible: row 26 removes restrictions/noncreditable portions. Keep tax-account credit balances separately; the old invented credit-brought-forward field is not retained. [Form/instructions][form]

IRMS replaced the legacy route in January 2026 according to the authority notice. Its transitional extensions concern specified returns/periods and expressly do not postpone statutory payment. Do not reproduce a December-2025 transitional filing date as the deadline for all 2026 returns. Obtain current authorisation/signature setup, schema and accepted submission/payment evidence. [Authority IRMS notice][irms]; [Articles 35–36][law]

## Credits, refunds, penalties and procedure

Article 50 recognises an excess as carryforward or, on request, repayment under its conditions: ordinary 60-day and qualifying exporter/repeated-credit 30-day routes, with due other taxes offset. A row-30 request is not a refund approval or proof of the applicable accelerated route. Nonresident and traveller refunds use separate Articles 51–52 and implementation; these remain incomplete methods. [Articles 50–52][law]

Article 59 specifies EUR 6,000–20,000 legal-person fines for listed computation/invoice/recovery/payment/record failures; its responsible-person range is EUR 1,500–2,000 and entrepreneur range EUR 2,000–6,000. Article 58 covers other listed failures separately, and Article 60 permits a protective restriction for specified offences. Classify the actual offence and current procedure before quoting exposure. No current interest, appeal or amended-return deadline is invented here. [Articles 58–62][law]

## Worked examples

Hypothetical October 2026 EUR cases. Classification, tax point, registration and deduction evidence are explicit assumptions, not findings about actual taxpayers or filed returns.

### 1. Three rates and ordinary return reconciliation

A registered business has correctly classified gross supplies: standard 12,100; qualifying accommodation 11,500; specified 7% basic foods 1,070. Domestic input VAT is 900 and paid eligible import VAT 400; 300 of domestic input is restricted. There are no reverse-charge, energy, farmer or other transactions. [Articles 20, 24–24a, 37][law]; [form][form]

```oa-check
name: Montenegro three rate ordinary VAT return
inputs:
  standard_gross: 12100
  accommodation_gross: 11500
  basic_food_gross: 1070
  domestic_input_vat: 900
  import_vat_paid: 400
  restricted_input: 300
steps:
  - row_10: standard_gross / 1.21
  - row_11: accommodation_gross / 1.15
  - row_12: basic_food_gross / 1.07
  - row_16: standard_gross - row_10
  - row_17: accommodation_gross - row_11
  - row_18: basic_food_gross - row_12
  - row_24: row_16 + row_17 + row_18
  - row_25: domestic_input_vat + import_vat_paid
  - row_27: row_25 - restricted_input
  - payable: row_24 - row_27
expected:
  row_10: 10000
  row_11: 10000
  row_12: 1000
  row_16: 2100
  row_17: 1500
  row_18: 70
  row_24: 3670
  row_25: 1300
  row_27: 1000
  payable: 2670
```

### 2. Advance and final standard-rated supply

A contract totals 24,200 gross. A prior-period advance of 6,050 was correctly taxed; the final invoice reconciles that advance. There is no earlier additional tax-point event or property transition. [Articles 18, 20, 24][law]

```oa-check
name: Montenegro advance final invoice reconciliation
inputs:
  contract_gross: 24200
  prior_advance_gross: 6050
  rate: 0.21
steps:
  - contract_net: contract_gross / (1 + rate)
  - full_contract_vat: contract_gross - contract_net
  - advance_net: prior_advance_gross / (1 + rate)
  - prior_advance_vat: prior_advance_gross - advance_net
  - final_period_vat: full_contract_vat - prior_advance_vat
expected:
  contract_net: 20000
  full_contract_vat: 4200
  advance_net: 5000
  prior_advance_vat: 1050
  final_period_vat: 3150
```

### 3. Customs base without double-counted ancillary costs

Customs value is 20,000. Assumed duty 1,000 and eligible ancillary costs 500 are not already included. Goods are standard rated. The importer pays the assessed VAT and all Article 37 recovery conditions are met. These assumptions do not establish a duty tariff or actual import payment. [Articles 19, 22, 24, 36–37][law]

```oa-check
name: Montenegro import VAT base and recovery input
inputs:
  customs_value: 20000
  assumed_duty: 1000
  additional_ancillary_costs: 500
  vat_rate: 0.21
steps:
  - import_vat_base: customs_value + assumed_duty + additional_ancillary_costs
  - import_vat_assessed: import_vat_base * vat_rate
  - eligible_paid_import_input: import_vat_assessed
expected:
  import_vat_base: 21500
  import_vat_assessed: 4515
  eligible_paid_import_input: 4515
```

### 4. Recipient service VAT with partial recovery

A registered Montenegro business receives a qualifying general B2B service for 2,400 from a foreign supplier without a Montenegro representative. Place, recipient liability and tax point are established under Articles 12/17/18. Rate is 21% and only 60% is recoverable under an independently established deduction method. This is not an automatic SaaS classification. [Articles 12, 17, 18, 24, 37–38][law]; [row 21 instructions][form]

```oa-check
name: Montenegro recipient service VAT partial recovery
inputs:
  service_base: 2400
  vat_rate: 0.21
  established_recovery_fraction: 0.60
steps:
  - row_21_output: service_base * vat_rate
  - row_21_gross_input: row_21_output
  - eligible_input: row_21_gross_input * established_recovery_fraction
  - row_26_disallowed_part: row_21_gross_input - eligible_input
  - net_vat_cost: row_21_output - eligible_input
expected:
  row_21_output: 504
  row_21_gross_input: 504
  eligible_input: 302.40
  row_26_disallowed_part: 201.60
  net_vat_cost: 201.60
```

### 5. Rounded annual shared-input proportion

After all Article 38 inclusions/exclusions, credit-bearing annual turnover is 65,001 and other denominator turnover 34,999. Shared input VAT is 1,000, directly deductible input 200, directly exempt input 100 and separately restricted input 50. This is the final annual allocation; prior provisional deductions and any resulting correction require a separate reconciliation. [Articles 37–38][law]

```oa-check
name: Montenegro shared input upward rounded annual proportion
inputs:
  credit_bearing_turnover: 65001
  other_denominator_turnover: 34999
  shared_input: 1000
  directly_deductible_input: 200
  directly_exempt_input: 100
  restricted_input: 50
steps:
  - denominator: credit_bearing_turnover + other_denominator_turnover
  - rounded_percent: ceil(credit_bearing_turnover / denominator * 100)
  - shared_deductible: shared_input * rounded_percent / 100
  - total_deductible: directly_deductible_input + shared_deductible
  - gross_input: shared_input + directly_deductible_input + directly_exempt_input + restricted_input
  - total_nondeductible: gross_input - total_deductible
expected:
  denominator: 100000
  rounded_percent: 66
  shared_deductible: 660
  total_deductible: 860
  gross_input: 1350
  total_nondeductible: 490
```

### 6. Credit and other-tax offset

Eligible input is 5,000 and output tax 1,800. Confirmed due other taxes total 700. The illustration calculates the amount left after the statutory offset; it is not a refund decision, an accelerated-refund entitlement or an actual account balance. [Article 50][law]; [rows 29–30][form]

```oa-check
name: Montenegro excess input and due other tax offset
inputs:
  eligible_input: 5000
  output_tax: 1800
  confirmed_due_other_taxes: 700
steps:
  - vat_credit: max(0, eligible_input - output_tax)
  - offset: min(vat_credit, confirmed_due_other_taxes)
  - credit_after_offset: vat_credit - offset
expected:
  vat_credit: 3200
  offset: 700
  credit_after_offset: 2500
```

## Review handover

Deliver registration/operative-date decisions, supply/place/rate register, tax-point and customs schedules, invoice/recovery and annual allocation evidence, current-form reconciliation, credit/offset register and unresolved issues. Complete actual current IRMS validation, all implementing-rate/rulebook amendments, energy/farmer/travel/used-goods/gold schemes, property transition and capital corrections, nonresident/traveller refunds, precise procedure and independent country review. Six passing calculations do not close comprehensive VAT or country coverage.

## Sources

[law]: https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0
[amend]: https://wapi.gov.me/download/80b15e7e-da28-49b7-9ca6-de1849b9ab61?version=1.0
[future]: https://wapi.gov.me/download/a7c33b8f-aa74-4197-b1fa-317ea466161f?version=1.0
[form]: https://wapi.gov.me/download/e3d2b1f2-341b-487e-8e2a-d77868bbf52e?version=1.0
[irms]: https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms

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
