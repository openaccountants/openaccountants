---
name: ye-cross-border-withholding
description: >
  Yemen source-cited draft of non-resident payment withholding under Income Tax Law 17/2010 article 71. Covers payer scope, gross basis, named exclusions, statements and remittance, with two conditional examples. Distinguishes incidental commission withholding under article 68. Treaty entitlement, current amendments, final-tax status and administration-specific application remain unresolved; not complete cross-border coverage.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://agoyemen.net/lib_details.php?id=198"
    title: "Public Prosecution, Income Tax Law 17/2010, articles 2–4, 68 and 71"
    as_of: "2026-10-22"
---

# Yemen: cross-border payment withholding

## Scope and source status

This Guide translates selected provisions of Law 17/2010. It is not a certified current nationwide withholding schedule. Establish the administering tax office, location, applicable amendments, payer/payee status, contract and payment character first. Different administrations' rules, later measures and treaty implementation have not been reconciled. Arabic controls over this research translation. [Official reproduction](https://agoyemen.net/lib_details.php?id=198).

## Payers, recipients and gross base

Article 71(a) describes payments by sole-proprietor business owners and resident legal persons, and non-residents with a permanent establishment in Yemen, to an external entity or non-resident person. It imposes **10% without deduction of costs**. Determine whether the actual parties and payment fall within the provision; it is not a rule for every overseas bank transfer. Residence and permanent establishment require articles 3–4 and any applicable treaty analysis. This draft does not resolve ambiguous payer status or territorial source cases. [Articles 3–4 and 71(a)](https://agoyemen.net/lib_details.php?id=198).

The non-exhaustive list includes returns, foreign-loan interest, royalties, services, technology-use rights, artistic/sporting activity, trademark/patent licences and specified know-how/management payments. Article 2 defines returns and royalties broadly. Do not decide tax treatment from the invoice label alone or deduct the recipient's costs from the withholding base. No conclusion on final tax, credit/refund entitlement or treaty reduction is established here. [Articles 2 and 71(a)](https://agoyemen.net/lib_details.php?id=198).

## Named exclusions need evidence

Article 71(a)(2) excepts interest on loans granted by international financial institutions or approved foreign banks. Establish the lender's qualifying status and approval rather than treating every foreign lender as exempt. Article 71(b) separately exempts foreign-source loan/credit-facility interest obtained by the government or local-authority units. It does not extend that wording automatically to a privately owned borrower. [Article 71(a)(2), (b)](https://agoyemen.net/lib_details.php?id=198).

Article 71(a)(4) excludes the following from its service-fee category: a Yemen permanent establishment's share of foreign head-office expenses; transport/freight; shipping; insurance of imported goods; participation in exhibitions/conferences; and listing on international exchanges. That classification does not prove exemption from all other taxes or establish the deductibility of head-office expenses. Mixed invoices require supported allocation and review of other charging provisions. [Article 71(a)(4)](https://agoyemen.net/lib_details.php?id=198).

## Statement and remittance

Article 71(c) requires withholding, a statement showing the amount paid and deducted, and a copy to both the tax authority and the recipient. Remittance is due within **15 days from deduction**, through the statutory authority/central-bank channels specified there. Current bank details, forms, electronic procedures, currency conversion and holiday rules remain unverified; no payment instructions are invented. [Article 71(c)](https://agoyemen.net/lib_details.php?id=198).

Article 68 separately imposes **10% on incidental commission/brokerage**, with a right for the recipient to credit it against tax for the relevant assessment period and remittance within 15 days. Do not infer that article 71 is creditable merely because article 68 is. Where a payment appears to fall under both provisions, resolve the interaction before applying or stacking withholding. [Article 68](https://agoyemen.net/lib_details.php?id=198).

## Example 1: established taxable gross service fee

Assume a resident company pays a non-resident supplier a gross YER2,000,000 service fee independently established to fall within article 71, with no exclusion, treaty relief or gross-up arrangement. Withholding is YER200,000 and net payment YER1,800,000. The supplier's own expenses do not reduce this gross withholding base.

```oa-check
name: Yemen article 71 gross service withholding
inputs:
  gross_fee: 2000000
  rate: 0.10
steps:
  - withheld_tax: gross_fee * rate
  - net_payment: gross_fee - withheld_tax
expected:
  withheld_tax: 200000
  net_payment: 1800000
```

## Example 2: qualifying lender exception

Assume YER1,000,000 loan interest is independently established to fall within article 71(a)(2)'s approved-foreign-bank exception. Withholding under that item is zero. For an otherwise taxable payment with no qualifying lender exception or other relief, the same gross amount produces YER100,000 withholding. This does not establish lender approval, exemption under another provision or treaty entitlement.

```oa-check
name: Yemen qualifying lender exception versus taxable comparator
inputs:
  gross_interest: 1000000
  qualifying_exception_rate: 0
  taxable_comparator_rate: 0.10
steps:
  - exception_withholding: gross_interest * qualifying_exception_rate
  - comparator_withholding: gross_interest * taxable_comparator_rate
expected:
  exception_withholding: 0
  comparator_withholding: 100000
```

## Intake and remaining work

Collect payer/payee residence and establishment evidence, contracts, invoices, service location, payment/deduction dates, gross/net clauses, lender approval where claimed, treaty evidence and remittance statements. Remaining work includes administration-specific amendments, source and permanent-establishment detail, treaty inventory/relief procedure, mixed payments, gross-up treatment, foreign exchange, refunds/credits, penalties and operational forms. No complete withholding/cross-border coverage or professional attestation is claimed.

## Sources

- [Public Prosecution, Income Tax Law 17/2010](https://agoyemen.net/lib_details.php?id=198), articles 2–4, 68 and 71, retrieved 22 October 2026.

## Disclaimer

Source-cited research draft. Verify applicable law, administration, facts and procedures before making a payment or filing.
