---
name: kz-einvoice
description: "Kazakhstan 2026 electronic invoices and fiscal receipts: issuer scope, statutory exceptions, issuance dates, paper recovery and workflow evidence."
version: 1.1
jurisdiction: KZ
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: tax

type: filing-howto
---

# Kazakhstan electronic invoices and fiscal receipts v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Taxpayers assessing ЭСФ electronic invoices, online ККМ and ОФД receipts, plus whether goods movements need СНТ. A non-VAT taxpayer can still have invoice duties; a cash-register receipt exception is specific rather than universal. Determine the legal issuer category and transaction before selecting the exception or deadline.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| Ordinary invoice issuance | Default: not before turnover and no later than 15 calendar days after it; the specific periodical-publication/media rule in art. 493(5) contains an early-issue option for the full calendar-year turnover; do not assume that option covers other supply categories; 15 in words on the page | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Specified monthly utilities/communication/transport and other listed supplies | Invoice after month-end by the 20th of the following month under art. 493(2); check the full listed category | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Goods placed under the customs export procedure | Within 20 calendar days after turnover; 20 in words on the page (art. 493) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Buyer-request invoice in statutory receipt exceptions | Buyer demand within 15 calendar days, supplier issue within 30 calendar days after turnover; figures in words on the page (arts. 208, 493) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Non-VAT temporary paper invoice after confirmed technical failure/suspension | Enter electronically within 15 calendar days after the failure ends/suspension is lifted; 15 in words on the page (art. 209) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Non-VAT emergency paper invoice | Enter within 30 calendar days after the emergency ends; 30 in words on the page (art. 209) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

Use arts. 207–209 for non-VAT issuers, including simplified taxpayers, specified international freight/external-trade operators, imported goods and Virtual Warehouse goods, medical suppliers and listed professional categories. Apply the personal-property exclusion. Then test the exact receipt, electronic-payment, utility, ticket, finance, final-consumer or microbusiness exception applicable to that issuer category, including the exceptions to those exceptions and the purchaser’s demand rights. Do not carry forward the old “ordinary services on simplified generally no invoice” shortcut. VAT issuers use chapter 50, including arts. 491–493.

Issue through IS ESF (esf.gov.kz) using the actual authorised taxpayer/issuer identity, supply date, customer identifiers, goods/services, base and applicable tax status. Sign with ЭЦП as required and check the issued/accepted status. A non-VAT invoice does not create VAT credit. The invoice form/rules are the Ministry order; use the current portal and official form rather than inventing the old alleged new field.

ККМ: cash/card/mobile monetary settlements generally require a permitted registered machine and receipt under arts. 19/110–111. Specific exemptions include the statutory special-mobile-app route and listed persons/transactions; a no-network area uses a non-transmitting machine. Registration of transmitting ККМ uses ОФД data, while a non-transmitting machine uses an application. Preserve OFD transmission and receipt records. Do not assume small/no-staff retail is exempt.

СНТ is the electronic accompanying goods document; assess it with the current goods/movement/traceability list and Virtual Warehouse coverage. It is not automatically required for every supply described as imported or excisable. Retain stock, movement and invoice linkage; current lists and specific СНТ terms are unresolved here.

## Deadlines and filing

Start from the turnover date and exact art. 493 category. In IS ESF select the correct invoice type and issuer/recipient, complete current form data, validate/sign, and retain status/number/date. For non-resident service self-invoices, art. 493 requires issuance after VAT payment and within 5 calendar days of payment (5 in words on the page), not an automatic simultaneous credit. Paper invoices are permitted only in the statutory cases; non-VAT technical-failure/suspension/emergency recovery uses art. 209 terms above. A paper form is not a general substitute for electronic issuance. See `kazakhstan-vat` for credit recognition and timing.

## Penalties and interest

Missing, late or inaccurate invoices/receipts may create administrative liability and deny a buyer’s credit; the exact current penalty depends on the breach/category. No amount is supplied without the operative sanction provision.

## Cross-border points

International transport, imported and traceable goods, commission/consignment and EAEU movement rules can override a domestic shortcut. VAT place of supply and customs obligations do not follow from an invoice label alone. Refer borderline goods-list scope and complex movements.

## Two worked examples that recompute

Case 1: hypothetical taxable utility supply is KZT 100,000 before VAT. At the ordinary 2026 rate in `kazakhstan-vat`, invoice gross is KZT 116,000 and stated VAT KZT 16,000. A non-VAT supplier with the same price instead has no output VAT to pass through as credit. The decision turns on issuer and supply status.

```oa-check
name: Invoice taxable versus nonVAT issue
inputs:
  base: 100000
  vat_rate: 0.16
steps:
  - taxable_vat: base * vat_rate
  - taxable_gross: base + taxable_vat
  - nonvat_gross: base
expected:
  taxable_vat: 16000
  taxable_gross: 116000
  nonvat_gross: 100000
```

Case 2: hypothetical receipt ledger has KZT 80,000 cash, KZT 120,000 card and KZT 50,000 mobile payments. Reconciled receipt total is KZT 250,000; only KZT 230,000 transmitted leaves a KZT 20,000 discrepancy to resolve. A software receipt screen does not establish complete OFD reporting.

```oa-check
name: Cash register and OFD reconciliation
inputs:
  cash: 80000
  card: 120000
  mobile: 50000
  transmitted: 230000
steps:
  - receipt_total: cash + card + mobile
  - difference: receipt_total - transmitted
expected:
  receipt_total: 250000
  difference: 20000
```

## Ask the client first

- VAT/nonVAT issuer category, regime, actual supply and turnover date?
- Customer status, payment method, receipt evidence and invoice demand?
- ESF authority/signature, technical-failure/suspension/emergency evidence?
- Goods/movement/traceability list and current portal form?
- KKM registration, OFD data and receipt reconciliation?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for Tax Code arts. 19, 110–111, 207–209, 480–482, 491–493 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for Ministry invoice form and issuance rules: operative issuance/status/form portions | https://www.gov.kz/org/minfin/documents/details/917390 | 2026-11-14 |

Not yet confirmed: Availability of the early-issue option outside the specific periodical/media provision; exact fiscal-receipt content and QR requirements; Current СНТ/Virtual Warehouse goods lists and issue deadlines, exact new 2026 ESF field, all special supply-category deadlines, machine firmware/model detail and numerical penalties. Do not assert a blanket nonVAT services exemption or a universal paper-invoice recovery rule.
