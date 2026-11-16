---
name: kz-bookkeeping
description: "Kazakhstan 2026 records: conditional entrepreneur accounting exemption, tax records, primary documents, receipts, retention and reconciliations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/kz-bookkeeping"
  jurisdiction: "KZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Kazakhstan ИП bookkeeping and records v1.1

> **General reference only.** This skill produces draft working papers for review by a qualified Kazakhstan professional before filing, payment or taking a tax position. It is not approval of any particular taxpayer’s facts.

## Who this applies to

Persons in private practice also need a separate recordkeeping/status assessment; do not apply the simplified-ИП accounting exemption to them merely by analogy. Refer their professional and reporting requirements separately.

ИП/жеке кәсіпкер keeping records under simplified or general taxation, including whether full бухгалтерский учёт and financial statements are required. Legal entities/ТОО use `kz-financial-statements` for their accounting framework. Reply in the user’s language, retaining налоговый учёт, первичные документы, ЭСФ, ККМ, ОФД, Виртуальный склад and СНТ. Tax accounting and supporting documents remain required even when the specific full-accounting exemption applies.

## Rates, bands and thresholds

| Item and conditions | Rule for 2026 | Official source |
|---|---|---|
| ИП full-accounting exemption: all conditions together | Simplified declaration; annual income no more than 135,000 МРП; not VAT registered; not a natural monopoly (Accounting Law art. 2(2)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| Exemption ceases | Books/statements required from the month after a condition fails; a voluntary choice to keep them also starts next month (art. 2(2)) | https://adilet.zan.kz/rus/docs/Z070000234_ |
| 2026 exemption ceiling | KZT 583,875,000 = 135,000 × KZT 4,325, derived; this is not the special-regime eligibility ceiling | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru |
| Document retention | Until the applicable limitation period expires, and at least 5 years; generally starts with the tax period following the obligation computation period. Longer asset-specific rules apply (Tax Code art. 206; 5 in words on the page) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |
| Tax-record language | Kazakh and/or Russian; authority can require translation of foreign-language documents (art. 206) | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru |

## The base

1. Establish legal form, actual regime, annual income, VAT/natural-monopoly status and any voluntary accounting election. A general-regime ИП is not automatically exempt. An ИП can remain within the simplified tax regime while exceeding the lower accounting-exemption ceiling. Use `kz-financial-statements` when full accounting starts.
2. Maintain a tax accounting policy and registers appropriate to the regime under arts. 202–205/218–220, with records traceable to the primary documents. For a qualifying accounting-exempt ИП, entries rest on primary documents; the Tax Code permits their preparation in IS ESF with digital signature. Supporting documents include акт выполненных работ/оказанных услуг, накладная, счёт на оплату, ЭСФ where required, фискальный чек, bank statements and СНТ for covered goods. A payment request alone is not proof of supply. Preserve transaction identifiers, dates, counterparty, business purpose, currency and reconciliation.
3. For accounting-exempt ИП, art. 220 uses the official exchange rate on the operation date, not a generic receipt-date/annual-average shortcut. The selected regime’s income-recognition rules still matter. Separate business funds from personal Kaspi/Halyk movements, internal transfers and loan principal; do not exclude taxable interest just because it accompanies a loan payment.
4. Determine invoice obligations under `kz-einvoice` and arts. 207–209. In particular art. 208 expressly includes simplified taxpayers; non-VAT or ordinary services does not alone remove the invoice obligation. Evaluate the specific receipt/end-consumer/other exceptions and a buyer’s demand. Imported goods, international freight, commission/traceability and Виртуальный склад cases need their specific analysis.
5. Cash, card and mobile-payment receipts are within “денежные расчеты” (art. 19). Use a registered permitted ККМ under arts. 110–111 unless a specific exemption applies. The mobile-app route, specified professional categories and other enumerated exemptions must be distinguished. No-network areas generally use a non-transmitting machine, not an assumed exemption from receipts. Register through ОФД data for a transmitting register; issue each fiscal receipt and retain the registration/status evidence. OFD storage does not replace taxpayer retention.
6. Determine whether the actual goods and movement fall under current СНТ/Виртуальный склад/traceability lists. These are not synonymous with all imports or every non-VAT trader. Keep movement, stock and invoice links. Exact current goods-list scope, catalogue linkage, form-field changes, machine-firmware procedures and СНТ issuance/recovery terms are unresolved here; route rather than invent them.
7. Retain ordinary records for art. 206’s minimum and any longer limitation/asset period. Group I/other separately depreciated assets use a period running after the last depreciation period; other asset-group and non-depreciable-asset rules have their own starting points. Reorganisation transfers the storage duty to successors. Do not destroy records merely because 5 years passed if a longer rule applies.

## Deadlines and filing

Reconcile the tax ledger with the applicable income return (`kz-simplified-regime`/`kz-income-tax`), payroll, social payments and VAT jobs. Tax returns and statutory statements are different outputs. Issue the correct invoices/receipts through IS ESF and the registered ККМ/app, retain signed/accepted status and stock/movement links. Use `kz-einvoice` for operative invoice deadlines, not a universal issuance window. Do not state unconfirmed 2026 appendix fields as authoritative.

## Penalties and interest

Do not quote an unverified penalty for missing invoices, receipts, records or a register. Preserve the actual breach, period, taxpayer category and notice for application of the current administrative provision.

## Cross-border points

Foreign currency, foreign-language documents and EAEU/traceable goods need the specific exchange-rate, translation and movement records. ТОО, payroll computation, patent/retail historical transitions and complex imports are routed to their owning jobs; an accounting-exemption assumption cannot resolve them.

## Two worked examples that recompute

Case 1: Aizhan is an otherwise qualifying simplified-regime ИП IT freelancer, with hypothetical annual income KZT 500,000,000. At the 2026 МРП, accounting-exemption headroom is KZT 83,875,000. She keeps primary documents and tax registers, with invoice/ККМ exemptions tested on actual payments; bank transfer alone does not answer every invoice condition.

```oa-check
name: Aizhan accounting exemption ceiling
inputs:
  income: 500000000
  mrp: 4325
steps:
  - ceiling: 135000 * mrp
  - headroom: ceiling - income
expected:
  ceiling: 583875000
  headroom: 83875000
```

Case 2: Bauyrzhan’s hypothetical simplified retail business has annual income KZT 600,000,000, no natural-monopoly status. It exceeds the full-accounting exemption by KZT 16,125,000 while remaining below the separately tested simplified tax ceiling. Identify the actual failure month; books/statements start the next month. Cash/card/mobile sales require the ККМ analysis, with СНТ/ЭСФ checked for the goods.

```oa-check
name: Bauyrzhan distinct accounting and tax ceilings
inputs:
  income: 600000000
  mrp: 4325
steps:
  - accounting_ceiling: 135000 * mrp
  - tax_ceiling: 600000 * mrp
  - accounting_excess: income - accounting_ceiling
  - tax_headroom: tax_ceiling - income
expected:
  accounting_excess: 16125000
  tax_headroom: 1995000000
```

Dana is the preserved general-regime, VAT-registered mixed B2B/B2C case: she cannot use this simplified-regime accounting exemption. Keep full applicable books/statements, tax registers and valid ЭСФ; assess ККМ on cash/card/mobile payments. The former statement that every ИП keeps only tax accounting was incorrect.

## Ask the client first

- Exact regime, legal form, annual income and exemption/election evidence?
- VAT status and natural-monopoly status?
- Payment methods, customer types and required invoice/receipt documents?
- Goods, imports, traceability/stock movements and current list coverage?
- Full primary documents, currencies, dates, asset classes and record-retention holds?

## Sources

| Source and operative sections actually read | URL | Read on |
|---|---|---|
| Read for current Accounting Law art. 2, opened in ordinary browser including 2026 amendment | https://adilet.zan.kz/rus/docs/Z070000234_ | 2026-11-14 |
| Read for Tax Code arts. 19, 110–111, 202–209, 218–220 and 65 | https://www.gov.kz/org/kgd-akmola/documents/details/1084149?lang=ru | 2026-11-14 |
| Read for 2026 budget law art. 7 | https://www.gov.kz/org/kgd-ulytau/documents/details/939202?lang=ru | 2026-11-14 |
| Read for current accounting-exemption conditions and prohibited-list identification | https://www.gov.kz/situations/814/1716?lang=ru | 2026-11-14 |

Not yet confirmed: The old assertion that accounting-exempt ИП primary documents must omit bookkeeping-account references is unconfirmed, as are exact current primary-document form requirements; Exact current СНТ/Виртуальный склад goods lists, national-catalogue links, 2026 new invoice field, KKM model/firmware requirements (including the old named Mercury, Minika and Port models), implementing-order numbers such as the old tentative No. 626, paper-recovery periods for СНТ, and numerical penalties. Historical press/vendor generalisations are not substituted for these instruments.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `kz-bookkeeping` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/kz-bookkeeping. If neither is available, confirm every figure against the official source pages cited above before relying on it.
