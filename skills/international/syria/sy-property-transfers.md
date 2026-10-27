---
name: sy-property-transfers
description: >
  Syria property-transfer research draft: Law 15/2021 rates, valuation and gift multipliers, declarations, clearance and objections, reconciled with dated 2025 administrative reports. Includes conditional calculations; current implementation and complete property coverage remain open.
jurisdiction: SY
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
sources:
  - url: "https://archive.sana.sy/?p=1347631"
    title: "SANA: full text of Law 15/2021, 29 March 2021"
    as_of: "2026-10-23"
  - url: "https://sana.sy/economy/2256905/"
    title: "SANA: property clearance circular, 30 July 2025"
    as_of: "2026-10-23"
  - url: "https://sana.sy/locals/2223654/"
    title: "SANA: ministerial relief for mutually abandoned sales, 25 May 2025"
    as_of: "2026-10-23"
  - url: "https://sana.sy/economy/2446227/"
    title: "SANA: ministry discussion of proposed legislative changes, 9 April 2026"
    as_of: "2026-10-23"
  - url: "https://sana.sy/locals/2481883/"
    title: "SANA: temporary Suwayda judicial/property restrictions, 21 May 2026"
    as_of: "2026-10-23"
---

# Syria: property transfers and financial clearance

## Evidence and limits

The [full original Law 15/2021](https://archive.sana.sy/?p=1347631) is available from SANA's official archive. It took effect on 3 May 2021 (article 21); property sales with an established date before commencement are excluded by article 17. This Guide distinguishes that statutory baseline from later administrative reports. It is not a verified consolidation of every measure effective in October 2026.

The Ministry's [9 April 2026 meeting report](https://sana.sy/economy/2446227/) describes property-tax amendments still to be issued. It does not enact a replacement. Confirm subsequent instruments and the competent local administration before relying on a live assessment. Rental income, inheritance outside the provisions described below, registration fees, stamp duty and complete local additions remain outside this draft.

## Classify the property, taxpayer and right

Articles 1–5 use the ministry-adopted market value and financial property classification. This is not automatically the agreed sale price or capital gain. Valuation committees and approved price zones determine the base; article 4 permits property-specific weighting within 25% upwards/downwards.

| Article 5 category | Baseline rate on adopted value |
|---|---|
| Residential property | 1% |
| Land inside an approved planning boundary | 2% |
| Land outside that boundary | 1% |
| Non-residential property | 3% |
| Rooftops in residential properties | 1% |

Article 6 values bare ownership at 40% and usufruct at 60% of the adopted property value. For the stated commercial-property rights, ownership is valued at 10% and the leasehold/premium right, *farough*, at 90%. These are value allocations, not tax rates. Establish precisely which right transfers.

Article 7 applies **15% of the article 5 rate** to gifts to ascendants, descendants and spouses. Other gifts follow sale treatment. Wills follow gift treatment except the obligatory bequest. Do not translate this into a 15% tax on property value or into a general inheritance exemption.

Article 8 includes the listed defence, school, municipal-share and sustainable-development additions within the statutory rates, but excludes the local-administration addition, subject to its income-tax-law cross-reference. The table is therefore not a quotation of all transaction costs.

Article 10 lists exemptions, including specified public-purpose takings, loans for use between the stated close relatives, sales by administrative public bodies and qualified diplomatic/international-organisation sales; it preserves the specified charity exemptions. Economic public-body sales and licensed development-project-company sales instead remain under income-tax law under articles 14–15. Being outside this transfer regime does not mean tax-free. [Law 15/2021, articles 1–15](https://archive.sana.sy/?p=1347631).

## Dated administrative changes to reconcile

The [30 July 2025 ministry circular reported by SANA](https://sana.sy/economy/2256905/) resumes financial-clearance issuance from 3 August. It reports use of previously adopted market values with a **30% reduction for residential property**, and contract-value fallback in areas without adopted values. It also requires the actual-price contract and stamp-duty treatment, removes the compulsory 50% bank-deposit condition, and describes a three-month no-objection document replacing security approval. This report does not prove that all procedures remain unchanged or guarantee immediate processing today. Do not extend the residential reduction to commercial property or automatically apply it to every gift/right allocation without confirmation.

The [25 May 2025 cancellation decision reported by SANA](https://sana.sy/locals/2223654/) concerns a mutually abandoned sale still confined to the finance-office process, before completed property registration. Written declarations by seller and buyer are required; already-paid tax is returned through the prescribed procedure. This is not relief for reversing an already completed registered transfer. Obtain the decision and supporting documents for a claim.

National guidance is not enough for every location: the [21 May 2026 Suwayda report](https://sana.sy/locals/2481883/) describes temporary judicial/property restrictions pending a later modifying or ending decision. Their current scope/status remains unverified here. Do not infer permission to register from a tax calculation alone.

## Declaration, payment, clearance and challenge

Article 9 requires a written sale/gift declaration on the finance-office form within **30 days of the event**, followed by payment within **30 days of the declaration**. These are separate triggers. Failure to declare carries a stated 10% tax-based penalty; late payment refers to Decree 146/1968, whose current penalty mechanics have not been verified for this Guide.

Article 13 requires financial clearance before registration/documentation of property rights. Its court-payment document for a disputed transaction is expressly **not** the final financial clearance needed to execute the judgment. The article separately provides a reimbursement route when a claim is dismissed or struck off, using a certified final judgment; do not confuse that with the 2025 mutual-abandonment procedure.

Article 11 allows an objection within **30 days following notification of the collection order**, conditional on prior payment of the tax, additions and supplements in full and a **1% security deposit on imposed tax**. The deposit is returned for a wholly or partly justified objection and otherwise becomes treasury revenue. Article 12 separates classification objections from valuation review. Its committee consideration period does not create automatic acceptance or promise a refund within 30 days of filing. Refunds under that article go to the taxpayer's bank account, with its stated alternative for settling another tax liability. [Law 15/2021, articles 9, 11–13](https://archive.sana.sy/?p=1347631).

As a working control, retain the property record, financial classification, adopted valuation, precise right transferred, transaction date, parties' relationship where relevant, declaration, assessment, payments, clearance and objection/cancellation evidence. This is a recommended evidence file, not a verified statutory retention period.

## Example 1: qualifying gift-rate multiplier

Assume a gift to a qualifying descendant, confirmed residential classification and an already-established taxable value of 10,000,000 new pounds. Assume no further valuation adjustment. The baseline 1% rate multiplied by 15% is 0.15%; tax before any separately applicable local addition is 15,000. It is not 1,500,000.

```oa-check
name: Syria qualifying family gift multiplier
inputs:
  confirmed_taxable_value: 10000000
  residential_rate: 0.01
  gift_multiplier: 0.15
steps:
  - effective_rate: residential_rate * gift_multiplier
  - baseline_tax: confirmed_taxable_value * effective_rate
expected:
  effective_rate: 0.0015
  baseline_tax: 15000
```

## Example 2: conditional residential-value reduction

Assume the competent office confirms the reported residential reduction applies to this sale and confirms a prior adopted value equivalent to 10,000,000 new pounds. Applying 30% reduction leaves 7,000,000; applying the 1% residential rate gives 70,000 before a separately applicable local addition. This is a conditional illustration, not proof that the contract price is the adopted value or that the reduction applies to every transaction.

```oa-check
name: Syria confirmed residential valuation reduction
inputs:
  prior_adopted_value: 10000000
  confirmed_reduction: 0.30
  residential_rate: 0.01
steps:
  - adjusted_value: prior_adopted_value * (1 - confirmed_reduction)
  - baseline_tax: adjusted_value * residential_rate
expected:
  adjusted_value: 7000000
  baseline_tax: 70000
```

## Remaining work

Recover signed administrative decisions and follow-up clarifications; reconcile later legislation, local additions, executive instructions, rental changes, current forms and geographical restrictions. Original-law rates and arithmetic examples do not prove a complete current assessment. No complete property domain, country coverage or professional attestation is claimed.

## Disclaimer

Source-cited research draft. Confirm current applicable instruments, territory and facts before a transaction, declaration or payment.
