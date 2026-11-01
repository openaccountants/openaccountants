---
name: gn-property-tax
description: "Guinea CFU property-classification and rate working paper using the enacted March 2026 replacement of CGI article 265. Use it only after separately confirming property liability, exemption status and the annual rental-value base, and establishing that this version governs the actual period including any October rectification effect. It distinguishes owner-occupied residential and professional property, rented property and completed unoccupied property. Two examples reconcile assumed annual values and rates without establishing a valuation method. If the governing version is not confirmed, the result is hypothetical March-text analysis only. It cannot support a live assessment, filing or payment conclusion. Full property procedures and other pack domains remain partial."
jurisdiction: GN
category: international
tax_year: 2026
tax_year_notes: "Enacted 31 March 2026 replacement text; earlier periods and October rectification status unconfirmed."
tier: 2
last_updated: 2026-11-01
version: 1.1
---

# Guinea CFU: property classification and rate workpaper v1.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Guinea.

## Who this applies to

**Governing-version prerequisite.** Before using this workflow for an actual period or invoice, establish that the March replacement text governs it, including the promulgation, effective date and effect of any October rectification. If that is not confirmed, label every result **hypothetical March-text analysis only** and stop before a live tax/compliance conclusion, filing/payment decision or legally required invoice-correction request. The source gap does not authorise assuming the March text remains unchanged.

Use for a property already confirmed to fall within the Contribution Foncière Unique (CFU), with its taxable annual rental value and exemption status established separately. This job selects the rate from CGI article 265 as replaced by article 14 of Law L/2026/010/CNT of 31 March 2026. It produces a rate workpaper, not a complete property assessment. The same official bundle contains promulgation decree D/2026/0103/PRG/SGG, signed 31 March 2026. Use this replacement text where applicable; allocation to periods before the replacement and the status/effect of the October rectifying bill remain unconfirmed. [Law art. 14 and decree arts. 1–2, PDF pp. 21,27](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf).

## Rates, bands and thresholds

| Confirmed property classification | CFU rate and base under replaced CGI 265 | Official source |
|---|---|---|
| Residential property occupied by its owner | 2% of actual annual rental value | [Law art. 14 / CGI 265, first bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Professional-use property occupied by its owner | 10% of actual annual rental value | [Law art. 14 / CGI 265, second bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Rented property | 15% of actual annual rental value | [Law art. 14 / CGI 265, third bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |
| Completed property that is unoccupied | 5% of estimated annual rental value | [Law art. 14 / CGI 265, fourth bullet](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21) |

The base is rental value, not the property's purchase price. Keep actual annual rental value and estimated annual rental value in separate workpaper fields; the law uses different bases for occupied/rented and completed-unoccupied property. These rates do not establish that a particular taxpayer or property is taxable. [CGI 265 as replaced](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21).

## The base

0. Establish the governing-version prerequisite above and record the evidence for the actual period or invoice, including any October effect. If unresolved, stop live use; the following steps may only illustrate the March text hypothetically.
1. Identify the property, owner, relevant period and supporting ownership/occupation evidence. Obtain the independently confirmed CFU scope and exemption conclusion before calculating.
2. Record whether it is owner-occupied residential, owner-occupied professional, rented, or completed and unoccupied. Preserve the lease, occupation evidence or completion/vacancy facts that support that classification.
3. Obtain the established annual rental-value base and its valuation evidence. Do not substitute purchase cost, capital value or monthly rent without the applicable valuation determination.
4. Multiply that annual base by the corresponding rate above. Reconcile the result to the assessment or draft calculation, showing any difference for review. The multiplication follows the express rate/base pairs in [CGI 265](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf#page=21).
5. Stop for a mixed-use property, a change of use during the year, partial ownership, a contested valuation or an exemption question. Article 265 alone does not resolve those facts. The completed workpaper records the evidence, category, base, rate and computed amount, with unresolved items separately identified.

## Deadlines and filing

This is a computation workpaper. Complete it before a filing/payment decision and retain the calculation with the classification and valuation evidence as a workflow control. This is not a statutory retention-period claim. The opened amendment does not establish the CFU return form, portal, field numbers, filing/payment dates or payment receipt process. No submission or payment instruction is supplied until those are verified.

## Penalties and interest

No CFU penalty, late-payment interest rate or relief condition has been confirmed from the opened replacement article. Do not compute a sanction from a rate used in a different tax.

## Cross-border points

The rate table classifies property by use/occupation, but it does not establish non-resident ownership liability, fiscal representation, treaty relief or foreign-tax credit entitlement. Obtain those conclusions separately before using the result for an overseas owner's filing.

## Two worked examples that recompute

First, an owner-occupied home has an independently confirmed actual annual rental-value base of GNF 60,000,000. The property is assumed taxable without exemption and the replaced article applies. CFU is GNF 1,200,000. The example establishes no valuation method.

```oa-check
name: Owner-occupied residential rate workpaper
inputs:
  confirmed_annual_rental_value: 60000000
  rate: 0.02
steps:
  - cfu: confirmed_annual_rental_value * rate
expected:
  cfu: 1200000
```

Second, compare a completed property remaining wholly unoccupied with a hypothetical letting for a full annual period. Each scenario has an independently confirmed GNF 120,000,000 annual base, estimated in the vacancy scenario and actual in the rental scenario. The results are GNF 6,000,000 and GNF 18,000,000. The GNF 12,000,000 difference is only the CFU component of a letting decision; rent, costs, other taxes and transition allocation are not modeled.

```oa-check
name: Vacancy versus full-period rental CFU component
inputs:
  confirmed_estimated_vacant_base: 120000000
  confirmed_actual_rented_base: 120000000
  vacant_rate: 0.05
  rented_rate: 0.15
steps:
  - vacant_cfu: confirmed_estimated_vacant_base * vacant_rate
  - rented_cfu: confirmed_actual_rented_base * rented_rate
  - additional_cfu_if_rented: rented_cfu - vacant_cfu
expected:
  vacant_cfu: 6000000
  rented_cfu: 18000000
  additional_cfu_if_rented: 12000000
```

## Ask the client first

Obtain the evidence establishing the governing version for the actual period, including any October effect; the property/ownership record; actual occupation, lease and completion facts for the period; the confirmed taxable/exemption position; established annual rental valuation and its evidence; the assessment/filing notice; and any mixed use, change of use or non-resident ownership facts.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [DGB official enacted 2026 law bundle](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf), scanned law pp. 19–24, especially art. 14 fully replacing CGI 265 on p. 21; promulgation decree arts. 1–2 on p. 27 and corroborating reference on p. 28. Operative page and signed decree also visually inspected. | 2026-11-01 |

**Not yet confirmed:** complete CFU scope/exemptions, valuation machinery and deductions, mixed use/change-of-use/part-year treatment, legal incidence/withholding on rent, non-resident rules, return and payment deadlines/forms/portal/receipts, penalties and interest, effect before the 31 March replacement and final promulgated status/effect of the October 2026 rectifying bill. This bounded calculation does not confirm full 2026 property compliance.
