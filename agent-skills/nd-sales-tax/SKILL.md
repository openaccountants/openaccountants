---
name: nd-sales-tax
description: "Compute ordinary North Dakota 2026 sales and use tax at the 5% state rate plus verified local tax. Apply the exceeds-100000 remote-seller test, covered software and conditional food/manufacturing exemptions; register, file and pay in ND TAP. Load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nd-sales-tax"
  jurisdiction: "US-ND"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Dakota sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider relevant facts and circumstances; do not assume missing facts or rely on audit risk.

**Answer first.** Ordinary taxable retail sales bear 5% state tax plus the applicable city/county tax. A remote seller exceeds the statutory USD 100,000 test only when qualifying sales are **greater than** that amount; there is no transaction-count limb. Prewritten software delivered electronically is taxable, but this does not establish a blanket answer for every remote-access service. [57-39.2-02.1,02.2](https://ndlegis.gov/cencode/t57c39-2.pdf).

## Scope

Ordinary sales/use tax, seller permit, destination/location analysis, exemption evidence and state filing/payment. **Load `us-sales-tax` first.** Specialized gross-receipts taxes, vehicles, lodging and other excises require separate classifications. Federal/state corporate income tax and payroll are separate jobs.

## Ask the client first

1. Seller identity, physical activities, permit/accounts and marketplace arrangements.
2. Current/prior calendar-year qualifying North Dakota sales and the date the remote threshold was crossed.
3. Exact product/service/software contract, delivery/receipt location and sale date.
4. Purchaser exemption/resale certificate, use, manufacturing expansion evidence and any approval.
5. Sales/purchase ledgers, tax collected or paid elsewhere, assigned filing frequency and prior returns/payments.

## The method, step by step

### Rates, bands and thresholds

| 2026 item / condition | Rate or threshold | Official source |
| --- | --- | --- |
| Ordinary taxable retail sale | 5% state tax | [57-39.2-02.1](https://ndlegis.gov/cencode/t57c39-2.pdf) |
| City/county tax | Actual address/date-specific rate; quarter changes and product exceptions | [state local-tax page](https://www.tax.nd.gov/sales-and-use-tax/local-taxes-city-and-county-taxes) |
| Remote seller without physical presence | Gross sales of TPP/other taxable items delivered into ND **exceed USD 100,000** in prior or current calendar year | [57-39.2-02.2](https://ndlegis.gov/cencode/t57c39-2.pdf) |
| Remote collection start | Earlier of next calendar year or 60 days after exceeding threshold | [57-39.2-02.2](https://ndlegis.gov/cencode/t57c39-2.pdf) |
| Ordinary monthly-reporting statutory test | Prior-year sales subject to sales/use tax at least USD 333,000; agency waiver/assignment conditions apply | [57-39.2-12](https://ndlegis.gov/cencode/t57c39-2.pdf) |

1. Establish physical presence or the exact remote test. At precisely 100,000 the remote threshold has not been exceeded; physical presence or other duties may still apply. Marketplace collection is a distinct statutory obligation; reconcile marketplace/direct sales rather than assuming all sales are self-collected. Obtain a permit and the actual collection start date.
2. Classify each transaction under the statute, including bundled elements, separately stated charges and the true delivery/receipt arrangement. General tangible personal property and clothing are ordinarily taxable. The old professional-services “not taxable” row is not a safe universal rule: identify whether any enumerated taxable service, tangible item or bundle is sold.
3. Apply the actual exemption conditions and retain evidence. Grocery food is not a blanket exemption for all edible items: prepared food, candy/gum, supplements and specified soft drinks are excluded from the food exemption. Prescription drugs require the stated prescription condition. Resale requires the proper certificate and actual resale; own-use withdrawals need use-tax review.
4. Manufacturing equipment is not universally exempt. Section 04.3 requires direct use in a new plant or physical/economic expansion; ordinary replacement does not qualify without expansion. Nonmanufacturing/administrative items, buildings and excluded equipment require separate treatment. To obtain exemption at purchase, secure the commissioner's certificate; otherwise pay and pursue the specified refund. Contractor purchases have their own refund route.
5. Prewritten software sold/leased/rented, including electronically delivered or load-and-leave software, is specifically taxable. The old prohibition against ever treating SaaS as nontaxable contradicted the closing unresolved issue: **remote-access SaaS, downloads/streaming and other digital goods remain unconfirmed here** without the exact current agency classification. Do not equate taxable downloaded prewritten code with all cloud services.
6. Source the ordinary transaction under chapter 57-39.4: seller-location receipt and delivery-location receipt are different steps in the hierarchy, with purchaser-address fallbacks where required. The former shorthand “destination-based” does not cover every lease, telecommunications or special product. Identify the city/county and transaction date using the state locator; its ordinary sales/use rates do not include all special taxes. The old 0%-3.5% local range/~8.5% maximum has not been confirmed against every current locality and must not set an invoice.
7. Compute state tax on the documented taxable base, add only verified applicable local tax and reconcile certificates/marketplace collection. Compute purchaser use tax on taxable storage/use/consumption where seller collection was absent or insufficient, applying supported other-state tax credit rather than charging duplicate full tax automatically. Property brought into ND after prior use can require the agency's fair-market-value basis instead of original cost.

## Boundary and exception table

| Transaction | Treatment |
| --- | --- |
| General TPP/clothing | Ordinarily taxable at state rate plus verified local tax |
| Grocery versus prepared food | Apply detailed food definition and exclusions, not product-name assumptions |
| Manufacturing equipment | Direct-use/new-or-expansion/approval requirements; replacement not automatically exempt |
| Prescription drugs/resale | Statutory prescription or documented resale conditions |
| Professional services or software bundle | Resolve enumerated goods/services and contract terms before classifying |
| SaaS/digital content, leases, special excises | Refer unresolved classification/sourcing; do not extrapolate from canned software |

## Worked cases

**Preserved Case A.** USD 1,000 of ordinary taxable goods gives USD 50 state tax at 5%, **before** any local tax. This arithmetic is permitted by this computation skill; the old blanket “never compute any number” prohibition was incompatible with its own examples.

```oa-check
name: ND ordinary sale state component only
inputs:
  taxable_price: 1000
steps:
  - state_tax: taxable_price * 0.05
expected:
  state_tax: 50
```

**Preserved Case B and threshold boundary.** A remote seller's qualifying delivered sales of USD 120,000 in 2025 exceed 100,000 by 20,000. Collection begins by the earlier of January 1, 2026 or 60 days after the threshold-crossing date; the crossing date cannot be omitted. At exactly 100,000 the excess test is false, although other nexus can apply.

```oa-check
name: ND remote seller exceeds test and exact boundary
inputs:
  prior_year_qualifying_sales: 120000
  threshold: 100000
steps:
  - excess: max(prior_year_qualifying_sales - threshold, 0)
  - at_exact_threshold_excess: max(threshold - threshold, 0)
expected:
  excess: 20000
  at_exact_threshold_excess: 0
```

## When to refuse or refer

Refer unresolved SaaS/digital goods, bundles, special excises, construction/manufacturing approvals, marketplace responsibility disputes and locality-specific caps/exemptions. Do not use an unverified statewide maximum or a generic service exemption. Streamlined framework provisions do not replace the taxability and sourcing facts.

## Filing and payment

Apply for the seller permit through ND TAP; the agency asks sellers to apply 30 days before opening, and permits do not transfer with a business purchase. Confirm assigned monthly/quarterly/annual or other authorized frequency. Ordinary quarterly returns/payment are due the last day of the following month; monthly returns/payment are due the last day of the next month. The statutory monthly rule at USD 333,000 prior-year taxable sales permits stated waiver conditions; do not independently change an agency assignment.

Use ND TAP to select the period, report gross/taxable/exempt and local details, account for purchaser use tax, submit the return and authorize payment. Reconcile ledgers, retain acceptance and verify the payment posted to the correct account/period. Amend in TAP or follow the agency's paper amendment process; a calculation worksheet notice requires the instructed correction. Business-day relief applies: the published 2026 calendar gives November 2 for Q3 2026, rather than Saturday October 31. Recheck the actual calendar and account deadline.

The read agency page describes late filing at 5% or USD 5 initially, further 5% monthly up to 25%, late payment at 5% or USD 5 and 12% annual interest, with the stated first-month exclusion. Assess actual statutory facts rather than assuming every late return has tax due or that payment alone filed a return.

## Completion checklist

- Nexus, permit and collection start supported.
- Product/exemption and receipt location established from documents.
- Current local rate and separate special-tax treatment confirmed.
- Sales/use tax, certificates and marketplace totals reconcile.
- Assigned-period return accepted and payment credited.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Chapter 57-39.2. Read for ordinary rate, remote strict-exceeds/start rule, taxable software, food/prescription/manufacturing exemptions and return/payment frequency. | https://ndlegis.gov/cencode/t57c39-2.pdf | 2026-11-13 |
| Chapter 57-39.4. Read for state administration and general receipt-location sourcing hierarchy/exceptions. | https://ndlegis.gov/cencode/t57c39-4.pdf | 2026-11-13 |
| Current sales/use page. Read for purchaser use-tax basis/other-state credit, permit application, assigned frequency, TAP amendments and delinquency treatment. | https://www.tax.nd.gov/sales-and-use-tax | 2026-11-13 |
| State local-tax page. Read for quarter changes, locator limits and separate special taxes. | https://www.tax.nd.gov/sales-and-use-tax/local-taxes-city-and-county-taxes | 2026-11-13 |
| Current sales/use deadline calendar. Read for actual 2026 monthly/quarterly dates and Q3 November 2 business-day adjustment. | https://www.tax.nd.gov/sales-and-use-tax-deadlines | 2026-11-13 |

Not yet confirmed: exact current local rate/cap for a particular address and date; the old blanket 0%-3.5%/~8.5% summary; remote-access SaaS and digital content; classification of a particular professional-service/software bundle; specialist exemption approvals. These gaps cannot be resolved by assuming all professional services exempt or all remote software taxable.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nd-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nd-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
