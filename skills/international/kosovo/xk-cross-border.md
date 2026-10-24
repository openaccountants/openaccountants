---
name: xk-cross-border
description: >
  Screen Kosovo non-resident business activity for permanent establishments,
  classify service, royalty, interest and rent withholding, and prepare
  foreign-tax-credit workpapers. Treaty application, current amendment and
  implementing-rule checks, forms and independent review remain outstanding.
jurisdiction: XK
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Kosovo cross-border business income v0.1

## Who this applies to

Use this draft for a Kosovo payer contracting with a non-resident business, a non-resident operating in Kosovo, or a Kosovo resident corporate taxpayer receiving foreign business income. Employment and natural-person classifications require separate analysis; the service-withholding rule must not replace payroll treatment merely because an invoice describes services. [Articles 29–31 and 33][law]

This is a source-cited draft based on the original official English text of Law 06/L-105, published in 2019 and read on 23 October 2026. The metadata identifies the intended research year, not a completed 2026 amendment audit. Current implementing instructions, treaty-specific outcomes and independent review remain outstanding. Do not use the rates below as a final filing conclusion until those checks are completed.

## Permanent-establishment screening

A permanent establishment (PE) changes the analysis before the payer selects the non-PE service-withholding route. Record actual premises, activities, personnel, contracts and dates; company registration alone does not resolve these tests. [Articles 30 and 33(2)][law]

| Domestic test | Retrieved statutory rule | Evidence to collect |
|---|---|---|
| Fixed place | Business wholly or partly carried on through a fixed place for longer than six months within any twelve months | Premises, access, activity and operating dates |
| Construction, assembly, installation and associated supervision | Longer than 183 days within any twelve months; actual commencement includes preparatory activities | Project timeline, preparation and supervision records |
| Services through employees or other personnel | Article 30(3.2) states more than 90 days within any twelve months, followed by an individual-presence proviso discussed below | Personnel-by-personnel presence and service dates |
| Immovable property | Article 30(3.3) separately includes Kosovo immovable property owned by a non-resident | Ownership and location |
| Dependent agent | Regular exercise in Kosovo of authority to conclude contracts for the non-resident, subject to the limited-activity exception | Authority, actual contracts and conduct |

[Article 30(1)–(3), (6)][law]. Do not convert six months into 183 days or treat a calendar-year total as the rolling twelve-month test.

The English services provision adds wording concerning commencement by an individual and that individual's presence exceeding 183 days within twelve months. Its interaction with the 90-day service test is unresolved in this draft. Verify the authoritative local-language text and applicable interpretation before deciding a borderline service PE. This draft does not assert that every service engagement becomes a PE after 90 days. [Article 30(3.2)][law]

Article 30(4) lists limited-purpose exclusions, including storage/display/distribution, processing by another enterprise, purchasing or information collection, and specified preparatory or auxiliary activities. Combined activities must satisfy the stated preparatory/auxiliary condition. Paragraph 5 limits the exclusions for related operations forming coherent business activity; do not split an operating business across related persons to assume an exclusion. The English translation has awkward place terminology, so a contested case requires local-language reconciliation. [Article 30(4)–(5)][law]

An independent broker or commission agent acting in its ordinary business does not alone create a PE. Ownership or control of another company does not alone establish one either. These are not exemptions for an agent whose actual conduct meets the dependent-agent test. [Article 30(6)–(8)][law]

## Rates, bands and thresholds

These are domestic rules in the retrieved statute, before a verified exemption or applicable treaty. Classify the payment before choosing a rate.

| Payment | Domestic withholding | Conditions and source |
|---|---|---|
| Non-resident services performed in Kosovo under an agreement with a Kosovo person or entity | 5% of gross compensation | Recipient has no Kosovo PE; Article 33(2)–(3) |
| Non-resident entertainers and sportspeople's personal activities in Kosovo | 5% of gross compensation | Direct or indirect payment; separate Article 33(1), (3) route |
| Interest on credits/loans and royalties | 10% at payment or credit | Article 31(2), subject to paragraph 4 interest exceptions |
| Rent | 9% at payment or credit | Article 31(3), except tax-exempt lessor income |

[Articles 31 and 33][law]. Article 31(4) excludes interest on ordinary-course customer loans provided by CBK-licensed financial institutions and interest on financial instruments issued or guaranteed by a Kosovo public authority. Do not apply that exception to every foreign bank or group loan.

The retrieved Article 33 contains **no EUR 5,000 minimum** for its service-payment route. Search results still expose older legislation with that threshold; do not import it into this statute. Services performed abroad, mixed-location contracts, bundled royalties/services and any administrative apportionment exception require further source review. A Kosovo payer alone does not prove that a service was performed in Kosovo. [Article 33(2)–(3)][law]

## Filing and payment dates

For Article 33 payments, submit the withholding statement and remit within 15 days after the calendar month ends. The payer must submit the annual reconciliation no later than 1 March following the tax period, including the required certificate copies. On recipient request, provide the withholding certificate before 1 March. The statute treats this withholding as final for the income concerned and removes the recipient's declaration requirement for that income; it does not exempt unrelated income or activities from filing. [Article 33(3)–(6)][law]

For Article 31 interest/royalty and rent withholding, remit by the 15th of the following month after payment or credit. Article 31(5) requires the certificate before 1 March following the tax period. Current electronic forms, administrative filing conventions and holiday extensions have not been verified here. [Article 31(2)–(5)][law]

## Foreign tax relief and treaties

Article 29 gives a Kosovo resident taxpayer a credit for foreign income tax paid on foreign business income, capped at the Kosovo tax attributable to that income before the credit. Collect the foreign assessment, proof of payment, income reconciliation and allocation of the Kosovo tax. Do not treat foreign tax as an unlimited reduction of domestic liability or assume unused credit is refundable or carried forward. This draft has not verified such additional relief. [Article 29(1)–(2)][law]

An applicable double-tax agreement takes precedence under Article 29(3). Verify the actual treaty, entry into effect for the period, residence and entitlement, relevant income/PE article and domestic relief procedure before reducing withholding. No treaty-rate matrix or automatic exemption is supplied here. A foreign transfer-pricing adjustment also requires separate analysis; see [transfer pricing](xk-transfer-pricing.md).

## Worked examples

### 1. Domestic non-resident service withholding

Assume a corporate supplier performs the entire service in Kosovo, has no Kosovo PE after the applicable tests, receives EUR 20,000 gross, and no treaty or exemption changes Article 33. The payer withholds EUR 1,000 and pays the supplier EUR 19,000. The contract does not promise a net-of-tax fee; a gross-up would need a different calculation.

```oa-check
name: Kosovo domestic non-resident service withholding
inputs:
  gross_fee: 20000
  withholding_rate: 0.05
steps:
  withholding: gross_fee * withholding_rate
  supplier_payment: gross_fee - withholding
expected:
  withholding: 1000
  supplier_payment: 19000
```

### 2. Foreign-tax-credit ceiling

Assume eligible foreign income tax of EUR 1,400 has been paid and the correctly allocated Kosovo tax on that income is EUR 1,000 before credit. The allowable credit is EUR 1,000, leaving EUR 400 outside this credit calculation. These tax amounts are assumptions after base and allocation work, not a shortcut using foreign gross receipts.

```oa-check
name: Kosovo foreign tax credit ceiling
inputs:
  foreign_tax_paid: 1400
  kosovo_attributable_tax: 1000
steps:
  allowed_credit: min(foreign_tax_paid, kosovo_attributable_tax)
  unrelieved_foreign_tax: foreign_tax_paid - allowed_credit
  kosovo_tax_after_credit: kosovo_attributable_tax - allowed_credit
expected:
  allowed_credit: 1000
  unrelieved_foreign_tax: 400
  kosovo_tax_after_credit: 0
```

## Ask the client first

- Where is the recipient resident, and is it a business entity, employee or natural non-business person?
- Where was each service physically performed, and what does the contract actually supply?
- What premises, property, personnel, project dates and contracting authority exist in Kosovo?
- Is the agreed fee gross or net of tax, and when was it paid or credited?
- What treaty entitlement, exemption and foreign-tax-payment evidence is available?
- Which monthly statements, annual reconciliations and certificates have already been filed or issued?

## Sources and review limits

- [Law 06/L-105, official English PDF][law], Articles 29–31 and 33. Read 23 October 2026 from the previously retrieved PDF. Fresh browser retrieval returned HTTP 502.

Not yet confirmed: full amendment chain through 2026; implementing instructions and their reconciliation with the newer statute; local-language service-PE interpretation; treaty network, entitlement and relief forms; mixed-location service rules; PE profit attribution, registration and branch compliance; current penalties and administration; property disposals and other cross-border categories. Independent review and professional attestation remain outstanding. These limitations keep the cross-border domain partial.

[law]: https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf
