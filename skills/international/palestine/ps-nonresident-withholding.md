---
name: ps-nonresident-withholding
description: >
  Palestine source-cited research draft on taxable payments to non-residents, the reinsurance exception, remittance and the distinction from distributions and payroll. Based on selected provisions of consolidated Income Tax Decree-Law 8/2011. Later amendments, territorial administration, treaty relief and current filing procedures remain unresolved. Includes two conditional calculations; not a complete cross-border pack.
jurisdiction: PS
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين"
    title: "Official Gazette Bureau consolidated Income Tax Decree-Law 8/2011, articles 7, 15, 16, 30 and 31"
    as_of: "2026-10-22"
---

# Palestine: non-resident payments and withholding

## Scope and source limits

This is a research translation of the Arabic consolidated legislation retrieved on 22 October 2026. The portal lists amendments through 2016. The later amendment chain, emergency measures and actual administration in the West Bank, Gaza and East Jerusalem remain unverified. The examples show the retrieved statute's conditional arithmetic, not certified current filing instructions. Arabic controls. [Official text](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Establish whether the payment is taxable

Article 31(2) applies where a **resident pays a non-resident an amount taxable under this Decree-Law**. It requires 10% withholding from that amount as a fixed, final tax, remitted to the department. If the payer does not deduct it, the provision makes the payer liable for that amount. It does not impose 10% on every international bank transfer. Establish residence, the character of the payment and its chargeability first. [Article 31(2)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 7(15) exempts income arising abroad unless it arises from the person's funds or deposits in Palestine. Article 7(9) recognises exemptions under special legislation or bilateral/multilateral agreements concluded by the Palestinian Authority. These provisions do not by themselves establish where a particular service is sourced, which treaty applies or how treaty relief is claimed. Do not infer taxable source from the payer's address alone or quote an unverified treaty rate. [Article 7(9), (15)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Reinsurance exception and payer responsibility

Article 31(2) expressly excepts **reinsurance premiums paid to insurance companies abroad**. A general insurance premium, commission or bundled service fee is not automatically within that wording. Retain the reinsurance contract, recipient details and payment allocation. This exception to the specified withholding rule is not a finding of exemption from every Palestinian tax. [Article 31(2)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 31(1) separately makes a resident acting as a legal/commercial agent, branch or partner of a non-resident, or having a commercial relationship with one, responsible for the law's procedures on that person's behalf, including deducting and remitting tax due. Do not assume absence of a locally incorporated company removes compliance duties. [Article 31(1)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Remittance and other payment categories

Article 30(5) requires remittance within **30 days from deduction**, expressly subject to article 31. Payroll has its own article 31(3) duty: deduct at payment and remit with a detailed statement within **15 days from payment**. The payroll deadline is not a general month-end deadline and should not be used for all non-resident payments. Current forms, payment channels, holiday rules and administrative extensions have not been verified. [Articles 30(5), 31(3)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

Article 16(5) separately specifies 10% withholding on profits distributed as profit shares or cash distributions. Article 16(4) says the legal person's tax is final and cannot be refunded or credited to a partner or shareholder. Do not treat company tax as the shareholder's withholding credit. Where a distribution also falls within article 31(2), the interaction must be resolved before payment; this Guide does not add the two 10% figures together. [Article 16(4)–(5)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Controlled non-resident dealings

Under article 15(4), where a non-resident carries on taxable business/activity/profession with a resident and the assessor finds non-resident control leaves the resident no income/profit or less than obtainable, tax is assessed on the non-resident by reference to the real profits. If the non-resident defaults, the resident must pay on that basis. This provision alone does not establish a complete transfer-pricing documentation regime, threshold, method or treaty adjustment procedure. [Article 15(4)](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين).

## Worked example 1: taxable gross payment

Assume residence and chargeability have been established independently, article 31(2) governs, no treaty or statutory exception applies, and ILS20,000 is the gross taxable payment. Withholding is ILS2,000 and the recipient receives ILS18,000. There is no contractual gross-up in this example.

```oa-check
name: Palestine taxable non-resident gross payment
inputs:
  gross_payment: 20000
  rate: 0.10
steps:
  - withholding: gross_payment * rate
  - net_payment: gross_payment - withholding
expected:
  withholding: 2000
  net_payment: 18000
```

## Worked example 2: independently established reinsurance exception

Assume a separately documented ILS30,000 payment consists entirely of qualifying reinsurance premiums paid to an insurance company abroad. Article 31(2)'s deduction is zero. For comparison, an independently established taxable non-exempt payment of the same amount produces ILS3,000 withholding. The comparison tests the exception; it does not classify an actual insurance arrangement or determine other taxes.

```oa-check
name: Palestine reinsurance exception compared with taxable payment
inputs:
  payment: 30000
  exempt_withholding_rate: 0
  ordinary_withholding_rate: 0.10
steps:
  - reinsurance_withholding: payment * exempt_withholding_rate
  - taxable_comparator_withholding: payment * ordinary_withholding_rate
expected:
  reinsurance_withholding: 0
  taxable_comparator_withholding: 3000
```

## File preparation and unresolved work

Before a live payment, obtain payer/payee residence evidence, contract, invoice, income-source analysis, gross/net payment terms, any treaty eligibility evidence, the applicable administration and payment/deduction dates. Keep the computation and actual remittance evidence. Confirm current forms and procedures with the relevant authority; none are invented here.

Outstanding work: later amendments and emergency measures; territorial implementation; treaty inventory and relief process; source and permanent-establishment rules; distribution interaction; refunds and credit treatment beyond the quoted provisions; transfer-pricing procedures; penalties; currency conversion and gross-up authority. This Guide does not close the cross-border or withholding topic and has no professional attestation.

## Sources

- [Official Gazette Bureau consolidated Income Tax Decree-Law 8/2011](https://mjr.ogb.gov.ps/MergedLegislations/ViewText/111/قرار-بقانون-رقم-8-لسنة-2011م-بشأن-ضريبة-الدخل-فلسطين), articles 7(9), 7(15), 15(4), 16(4)–(5), 30(5), 31(1)–(3), retrieved 22 October 2026. Amendment list on the retrieved page ends with 14/2016.

## Disclaimer

Source-cited research draft. Verify the governing law, territory, facts and current procedures before relying on it for filing or payment.
