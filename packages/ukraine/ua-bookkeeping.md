---
name: ua-bookkeeping
description: "Ukrainian sole-proprietor (ФОП) record-keeping and bookkeeping: the income ledger and income-and-expense ledger, software cash registers (ПРРО / PRRO), primary documents that support income and expenses, fiscalisation, and document retention. Records and process, not rate computation."
version: 1.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-11-15
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: router
---

# Ukraine FOP records and bookkeeping

**2026 process review, read 15 November 2026.** This skill covers Ukrainian individual FOP records, primary documents, RRO/PRRO fiscalisation and retention. The independent-professional record form is retained as a separate branch, not treated as a FOP registration or single-tax election. Currency is UAH (₴); authority is the State Tax Service, **ДПС**, with [Електронний кабінет](https://cabinet.tax.gov.ua). Contributor: **Open Accountants Community**. It computes no tax, ЄСВ, military levy or VAT: route those to `ua-single-tax`, `ua-income-tax`, `ua-social-contributions` and `ukraine-vat`.

**Current corrections:** non-VAT single-tax records are free form with **monthly** income reflection under 296.1; a daily transaction trail is useful evidence, not a universal daily statutory ledger requirement. VAT-registered Group 3 uses a **prescribed** income/expense form, not free form. Current 44.3 puts documents needed for **141.4 nonresident-income control in the 2555-day category**, not the old 1825-day assumption. Martial law does not establish a blanket current suspension of every audit clock. [Tax Code 44,296](https://tax.gov.ua/nk/).

## Start here: evidence and routing

Obtain the intake package and effective regime/group/VAT dates, FOP versus independent-professional status, KVED/actual activities, premises, sold goods and warranty/medicine/jewellery/excise flags. Obtain all payment flows: cash, POS, online acquiring, PSP/marketplace, collection-on-delivery, direct bank transfer, currency and any intermediary contract. A bank account labelled IBAN does not classify every upstream customer payment.

Match the receipt ledger, statements, fiscal receipts/Z-reports, client/supplier contracts, invoices, delivery notes, work/service acts, refunds, FX credit advice/SWIFT records and stock-origin evidence. Flag missing records, cap breaches, status changes and disputes. **Do not assume PRRO is required or exempt merely from a group or brand name.** Unknown group, activity or payment channel blocks that classification. Company/TOV accounts and financial statements are outside this FOP workflow; refer them. Group 4 farming/e-resident rules and disputed independent-professional status require separate review.

### Conservative practices, with legal limits

- Keep the required records even when no tax-office ledger-registration step applies; keeping records and registering a PRRO are different obligations.
- Preserve electronic exports, scanned originals where appropriate and independent backups. A spreadsheet is a free-form option only where the law allows it; it does not replace a prescribed form or the original source documents.
- Keep documents supporting receipts, deductible costs and origin of goods. A non-VAT single-tax payer does not acquire a general expense-ledger duty merely because a cautious internal file retains supplier documents.
- Keep records longer when classification or a legal hold is unresolved. This is a preservation policy, **not a claim that never having been audited automatically creates an unlimited statutory retention period**.
- Do not destroy records based only on the shorthand 3/5/7 years, a software retention window or a closed FOP registration. Build the actual document-category and suspension analysis first.

## The method, step by step

### 1. Choose the correct record form

| Taxpayer branch | Required record | Form and timing | Source |
| --- | --- | --- | --- |
| Ordinary Group 1, Group 2 and Group 3 **non-VAT FOP** | Received income, free form | Paper and/or electronic; **monthly** reflection under 296.1. Keep transaction-level supporting dates and daily records as needed to prove the monthly total. No universal current mandatory registered Книга or daily form is inferred | [296.1](https://tax.gov.ua/nk/) |
| Ordinary Group 3 **VAT FOP**, the eligible **3%** path | Income **and expenses**, plus separate VAT records | **Typical form prescribed by Order 405 of 30 November 2022**, as amended; not the old free-form claim. Use the current full form/instructions for exact columns, corrections and entry timing; those detailed 405 instructions were not recovered here. Record own agricultural production/sales separately from other activities; e-residents are excluded from ordinary 296.1 requirements | [296.1/293.3](https://tax.gov.ua/nk/); [1 July 2026 DPS explanation](https://rv.tax.gov.ua/media-ark/news-ark/print-1026027.html) |
| General-system FOP | Documented income and business expenses, goods-origin documents | **Order 261 of 13 May 2021** typical form, paper/electronic including Cabinet; enter from primary documents at the end of each working day with income/expense. Current form is **not registered** with the tax authority. Electronic records must be available as a duly certified paper copy on request | [177.10](https://tax.gov.ua/nk/); [2 July 2026 DPS](https://kh.tax.gov.ua/media-ark/news-ark/print-1026346.html) |
| Independent professional activity, separately verified | Income/expense record under its own regime | Order **261** typical form, effective **16 July 2021**, daily source-based entries, paper/electronic and paper copy on request; current form not tax-office registered. Do not equate all professional tax rules with FOP rules | [8 May 2026 DPS](https://tr.tax.gov.ua/media-ark/news-ark/print-1008795.html) |

For the general-system form, 177.10 also separates own agricultural production/sales and the specified fuel-location retail fuel/alcohol/tobacco activity from other business records. General-system expenses require both documentation and substantive eligibility under 177.4; paying or recording an invoice alone does not establish deductibility. The September 2026 guidance distinguishes actual receipt/expense timing and goods actually sold/used in the appropriate column. Refer disputed costs, depreciation, mixed personal use and special activities to `ua-income-tax`. [177.2,177.4,177.10](https://tax.gov.ua/nk/); [10 September 2026 DPS](https://tr.tax.gov.ua/media-ark/news-ark/print-1048797.html).

**Historical registration claim retained as a correction:** the old text said registration was abolished for every FOP form on **1 January 2021**. Current non-VAT free-form records and current unregistered Order 261 form are confirmed above, but the universal historical effective-date claim is not established here. Do not add a tax-office book-registration task in this current workflow; verify a historical-period record separately. PRRO registration remains a separate real process.

### 2. Keep a reconstructable income trail

Record actual receipt date, currency/quantity, payer/counterparty, transaction and bank/fiscal identifiers, gross receipt, any separately evidenced fee/refund and the monthly/period total. For non-VAT single tax, 292.5 converts foreign-currency income at the **NBU official rate on the income receipt date**; 292.6 supplies the receipt rule. Do not use the later bank-sale rate or infer an invoice date is the cash receipt date. Other special material/free-goods/payables cases and exclusions in 292 remain with the income classifier. A refund reduces single-tax income only where the actual statutory conditions of 292.11(5) are satisfied, including the relevant goods return/contract termination/refund-application basis. [292.5-292.6,292.11](https://tax.gov.ua/nk/).

A bank credit advice, statement and SWIFT record support the actual credit/receipt date. Where value date, intermediary receipt, platform balance, conversion date or bank fee differs, retain every date and refer the unresolved recognition/classification; never assume every credit is taxable business income or every self-transfer is exempt. The old claim that general-system/independent-professional FX recognition automatically follows the same simplified-system rule is **not confirmed here**.

The free-form non-VAT record may be a spreadsheet (for example Excel/Sheets, retained as unendorsed format pointers) with monthly totals and an underlying daily transaction register. General-system users must keep the prescribed 261 structure. The official Cabinet's **«Облік доходів і витрат»** function is confirmed for that form, with КЕП/private access and no service charge in the cited explanation. It describes a **3-year** electronic storage window; that software window is **not permission to delete documents** before the applicable legal retention period. Export and back up records. Same-day corrections and later difference entries are described there; preserve the audit trail. Do not assume an identical Cabinet feature/schema for every single-tax branch. [9 April 2026 DPS](https://tr.tax.gov.ua/media-ark/news-ark/print-999349.html).

### 3. Classify RRO/PRRO by the actual settlement, not the product name

RRO is a hardware fiscal registrar; **ПРРО / PRRO** is a registered software fiscal registrar using the DPS fiscal server. Software and hardware can coexist. DPS offers a free software solution, while commercial products also exist; **not every PRRO is free** and the old claim that almost all FOPs use PRRO is unverified. Checkbox and Vchasno.Kasa remain old third-party pointers only; their current product status, pricing and compliance were not opened here. [DPS official PRRO FAQ, questions 3,7-11,15,19](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

| Payment/taxpayer situation | Classification and required next step | Source |
| --- | --- | --- |
| Genuine current Group 1 single-tax payer | **296.10 exempts Group 1 from RRO/PRRO.** Independently establish that activity still qualifies for Group 1 under 291.4/291.7. Market retail/household services, online/delivery expansion and listed goods are eligibility flags, not proof of a separate blanket override of 296.10 | [291,296.10](https://tax.gov.ua/nk/) |
| Group 2/3 or general FOP making ordinary cash/card settlement operations | Use registered RRO/PRRO and provide the prescribed fiscal receipt unless an actual statutory special rule applies. A POS/acquirer payment confirmation is not itself the seller's fiscal receipt | [3 April 2026 DPS, Law265 art3 and receipt distinction](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) |
| Direct bank credit transfer to the seller's current-account IBAN | The October 2026 QR guidance distinguishes full bank-IBAN credit-transfer details from another electronic payment instrument: the former route does not use RRO/PRRO in that stated case. Keep the contract/invoice and actual payment-route evidence | [2 October 2026 DPS](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) |
| QR or payment link using a card/other electronic instrument or acquiring service | A QR symbol alone is not the test. The other-electronic-instrument route requires fiscalisation on the general basis in the cited explanation. Examine the seller's acquiring contract and true payment chain | [October QR explanation](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html); [April payment-chain explanation](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) |
| Services paid exclusively through remote bank systems and/or funds-transfer services | Preserve the **Law265 art9(14)** exception as explained by national DPS in **2023**, including services within a business that also sells goods. It does **not** exempt the goods sales. That explanation also excludes cash and accepting electronic payment instruments/cards/tokens etc from its stated exempt service case. Do not treat every branded PSP as automatically qualifying or automatically disqualifying; current consolidated exception/application to the actual flow remains a referral if unresolved | [DPS full 7 November 2023 explanation](https://nvp.tax.gov.ua/media-ark/news-ark/725416.html) |
| Exclusively electronic delivery where settlement location cannot be determined | The April 2026 explanation has a distinct exception, with examples computer programs, e-books, reports, conclusions/expert assessments delivered solely electronically. The actual facts must satisfy that explanation; an ordinary online order of physically delivered goods/services is not the same case | [3 April 2026 DPS, final exception paragraphs](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) |
| NovaPay, LiqPay, WayForPay, Fondy, marketplace/collection-on-delivery or account codes **2924,2650,2654** | Old research pointers retained. Obtain contracts, actual payer/recipient/acquirer/settlement chain, goods versus service, place of settlement and proof of receipt. Those brand names/codes alone do not decide the exemption; current product-specific conclusions are **Not yet confirmed** | [Actual payment-chain method](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) |

**Listed-goods warning, with the old overstatement corrected:** technically complex warranty household goods, medicines/medical products/devices, jewellery/precious or semiprecious articles, and excisable alcohol/tobacco/fuel remain mandatory referral flags. Check Group 1 eligibility, the exact goods list, goods-stock documentation, excise licensing and actual Law265 exception before concluding. The current 296.10 wording itself is a Group 1 exemption; the old assertion that all these goods automatically override it “regardless of group” is not supported by that paragraph. Jewellery making/repair household services are not the same as commercial jewellery manufacture/trade. The former household categories are expressly within 291.7, subject to actual eligibility; commercial jewellery has its own Group3 restriction. [291.4,291.5,291.7,296.10](https://tax.gov.ua/nk/). No retired turnover threshold is a current exemption.

### 4. Operate and reconcile the PRRO

1. Confirm the taxpayer and business unit are on tax record; register the PRRO by the current electronic application through Cabinet or other accepted software. Use it after inclusion in the PRRO register. Register the FOP/cashier signing certificates and authority; only authorized certificates in the register may conduct operations. This is different from maintaining an unregistered tax ledger. [DPS FAQ questions10,18-19](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).
2. Program the actual goods/services, create the prescribed fiscal receipt on the full settlement, transmit for fiscal-server registration and retain the fiscal number/acknowledgment. Supply the buyer the required paper/electronic fiscal document. The April guidance requires it no later than handover/service acceptance and at settlement where payment and handover are simultaneous; do not replace it with an acquiring receipt. [DPS FAQ1-3,7,11](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi); [April timing](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html).
3. If communication fails, use only the actually applicable authorized offline procedure, reserved fiscal-number range and subsequent synchronization. The official FAQ includes ordinary offline caps and a wartime/emergency/force-majeure exception; the complete current consolidated rule and detailed limits were not recovered here. **Do not invent a universal time/receipt-count allowance or operate without the required range.** If authorized offline operation cannot be established, stop settlement operations and refer. Online receipts are searchable after registration; offline ones after transmission. [DPS FAQ7,12-13,16-26](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).
4. Create daily **Z-reports** where settlement operations took place, with the statutory vending-machine exception. Retain and reconcile receipts/Z totals to cash, card gross settlements and bank movements. The August 2026 guidance discusses end-of-day air alarms/power failure: where these actually prevent closure, form the report by the next working day **before starting settlements**. Keep evidence and seek review of relief; a generic outage label does not prove exemption. The old **X-report** current-total pointer is retained, but exact current device function/procedure is unconfirmed and it is not a replacement for the Z-report. [17 August 2026 DPS](https://rv.tax.gov.ua/media-ark/local-news/1040850.html); [DPS FAQ45,49-50](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi).

| Exposure, not a final penalty computation | Confirmed general headline | Source and boundary |
| --- | --- | --- |
| Specified incomplete/nonfiscal/no-receipt settlement violations under Law265 art17(1) | **100%** of affected sales value for first violation; **150%** for each subsequent violation, as the 2026 DPS explanation describes from **1 August 2025** | [29 April 2026 DPS](https://poltava.tax.gov.ua/kampaniya-prro/print-1005661.html). The old reduced **25%/50%** route described there ended **31 July 2025** at latest and had activity/VAT conditions. Establish violation count, period, statutory relief/territorial/force-majeure rules before any actual assessment. Complete relief provisions and final client penalty are **Not yet confirmed** here |

### 5. Assemble primary documents, without declaring every invoice sufficient

- **Income:** client contract; invoice/рахунок; work/service acceptance act or other valid operation evidence; fiscal receipt and Z-report for covered settlements; bank statement, credit advice and SWIFT record for noncash/foreign receipts. Link each to ledger entries and actual payment/return dates. An invoice paid by a client is not automatically sufficient for every legal purpose: the old claim that it can replace an act whenever it has requisites needs the actual transaction and current document rules. Its applicability is held for review.
- **Expenses:** supplier invoice, **видаткова накладна**, service/work act, cash/payment document and business-purpose evidence. A documented expense can still be outside the permitted general-system categories or timing. VAT credit and Group3 VAT-form expenses have their own rules; do not import general-system deductions into turnover tax or VAT.
- **Goods origin:** retain purchase/import/delivery and stock evidence where required. Non-VAT single tax is not blanket permission to discard these documents. Exact Law265 art3(12)/Order496 stock-book scope and goods exceptions require separate current verification before enforcing a universal stock-ledger duty.
- **Foreign currency:** preserve contract, invoice/act as appropriate, foreign-currency credit and conversion records, original currency and the actual official rate/date. The old statement that every export-service receipt must be repatriated within one prescribed term is unconfirmed. Current NBU exceptions, type/date of export, bank supervision and sanctions need separate review; no universal repatriation deadline is supplied here. A **2024** DPS explanation explicitly refers to service/work/IP exceptions under Resolution67, and is historical context rather than a current 2026 deadline source. [Historical explanation](https://cvp.tax.gov.ua/media-ark/news-ark/print-757248.html).

The governing evidence rule is **44.1**: tax indicators must be based on the required supporting records; unsupported numbers cannot be invented. Preserve the original documents/electronic validity and corrections, not just a total pasted into a spreadsheet. Loss, damage, early destruction, nonproduction during audit and subsequent audit-document submissions have distinct **44.5-44.7** procedures: escalate promptly rather than reconstructing fictional documents. [44.1,44.3-44.7](https://tax.gov.ua/nk/). This source review does not approve a specific invoice's requisites or an exact loss-restoration deadline for a client.

### 6. Classify retention before giving a disposal date

| Current category | Minimum, with conditions | Source |
| --- | --- | --- |
| Documents/information required for control under **39,39-2 and 141.4** | **2555 days**. This includes the specified nonresident-income-control category; the old allocation of nonresident-payment records to 1825 days is corrected. Determine whether a FOP's actual payment/document falls within 141.4; do not infer the category from “foreign” alone | [44.3.1](https://tax.gov.ua/nk/) |
| Specified primary/accounting/financial/tax records of persons listed in **133.1,133.2.2,133.4** and simplified-system **legal entities**, except the longer category | **1825 days**. Not a universal FOP rule. Company records remain outside this workflow, but the old 5-year category is preserved accurately | [44.3.2](https://tax.gov.ua/nk/) |
| Other documents not covered by the two preceding categories | **1095 days**, subject to longer legal periods and extensions; ordinary FOP minimum is not automatic destruction permission | [44.3.3](https://tax.gov.ua/nk/) |
| Documents for other legislation supervised by the tax authority, including permits | **1095 days**, with different start points: relevant operation, or permit expiry for the relevant permits | [44.3.4](https://tax.gov.ua/nk/) |
| Audit, administrative appeal or court-related records | Until the audit and statutory appeal period/end of litigation as applicable, and never less than the 44.3 periods. The separate foreign-official improper-benefit extension adds **1095 days** only for the specified notified records **after its commencement under XX.10.74-1**: first reporting period following both the first official NABU circumstances-list publication and approval of the 86.14 procedure. Commencement evidence has not been established here; hold that branch for review rather than assume it operates today | [44.4,86.14,XX.10.74-1](https://tax.gov.ua/nk/) |

For tax/other reporting records, **44.3 counts from the actual filing date of the report for which they were used**, or the statutory filing deadline if it was not filed. This corrects the old blanket “deadline or actual filing if later” formula. Other-law operations/permits have their own start point above. Taxpayer liquidation has a separate archival-transfer rule covering at least **1825 days**, or **2555** for the specified longer category; do not equate FOP termination with a completed archival/disposal analysis. [Full44.3](https://tax.gov.ua/nk/).

The 3/5/7-year shorthand is retained only to explain the old text: use the statutory **1095/1825/2555 day counts**, actual start and extensions, not calendar-year rounding. Under 44.3, periods extend for applicable **102.3** suspensions: the full list includes continuous absence from Ukraine of at least **183 days**, statutory/court audit prohibition, specified postponed/extended/suspended audit, defined inability to audit/nonadmission/contested-audit circumstances, and administrative/court assessment appeal. Actual facts and lawful exceptions matter. [44.3,102.3](https://tax.gov.ua/nk/).

**Wartime correction:** XX.10.69.9's general suspension wording says **until 1 August 2023**, with listed exceptions. It does not support the old claim that every clock remains stopped throughout all current martial law. Earlier COVID/war intervals, current taxpayer-specific audit prohibitions, other statutory lists, nonfiling and special retention rules still need a period-by-period analysis. Do not publish a final destruction date from this partial historical review. **Never-audited files remain on preservation hold until an accountant confirms disposal conditions**, but this skill does not establish the old universal “keep until a first audit no matter how long” assertion as enacted law. [69.9,44.3-44.4,102.3](https://tax.gov.ua/nk/).

## Worked cases and meaningful reconciliation

**Original A: Group 3 non-VAT IT freelancer paid by bank.** Software for foreign clients, USD/EUR to the FOP FX account, no cash/card/PSP: free-form non-VAT income record with monthly totals and receipt-date evidence/NBU translation, not a mandatory daily 261 ledger. Verify the actual direct bank flow for the RRO conclusion. Keep service contract, act/equivalent valid operation evidence, statement, SWIFT/credit advice and actual rate/date. Retention uses the applicable report/record category and actual filing start, **not necessarily an annual declaration deadline**: Group3 ordinarily reports cumulatively quarterly. No blanket current-war/no-audit disposal conclusion.

A hypothetical confirmed receipt of **USD1000** at an explicitly hypothetical receipt-day NBU rate **41.50** gives a **UAH41500** receipt record. A later bank sale of those dollars yields **UAH41000**: difference **500** flags conversion reconciliation; it does not replace the original receipt entry or establish the tax treatment of that difference. Actual bank date/rate and downstream adjustments must be verified. [292.5-292.6](https://tax.gov.ua/nk/).

```oa-check
name: Receipt record differs from later currency sale
inputs:
  usd_receipt: 1000
  hypothetical_receipt_day_rate: 41.5
  later_bank_sale_uah: 41000
steps:
  receipt_record_uah: usd_receipt * hypothetical_receipt_day_rate
  conversion_reconciliation_difference: receipt_record_uah - later_bank_sale_uah
expected:
  receipt_record_uah: 41500
  conversion_reconciliation_difference: 500
```

**Original B: Group 2 café/services to individuals, cash and POS.** Non-VAT free-form income record; classify the ordinary cash/POS operations, register/use the appropriate fiscal registrar and issue fiscal receipts unless an actual special exception is established. Reconcile daily fiscal records into monthly income totals; retain goods-origin records where relevant and statements for card settlement. Keep Z-reports under the daily-settlement rule. Retention follows category/start/extensions, not an automatic 1095-day destruction rule.

Hypothetical fiscal records show **14000 cash +6000 card =20000** gross receipts; the acquirer retains a documented **1200** fee and pays **4800** to the bank. Cash plus bank movement is **18800**; adding the documented fee reconciles to **20000**, difference **0**. This records the gross settlement trail; it does not deduct a fee from single-tax income or determine its tax eligibility. Any unmatched amount blocks completion rather than being silently written off.

```oa-check
name: Fiscal gross to cash and net bank settlement
inputs:
  fiscal_cash: 14000
  fiscal_card: 6000
  documented_acquirer_fee: 1200
  bank_net: 4800
steps:
  fiscal_gross: fiscal_cash + fiscal_card
  cash_and_bank: fiscal_cash + bank_net
  reconstructed_gross: cash_and_bank + documented_acquirer_fee
  unexplained_difference: fiscal_gross - reconstructed_gross
expected:
  fiscal_gross: 20000
  cash_and_bank: 18800
  reconstructed_gross: 20000
  unexplained_difference: 0
```

**Original C: general-system consulting and equipment resale, with mixed bank and card income.** Keep prescribed **261** income/expense records, supporting supplier invoices/delivery notes/acts, bank/PRRO receipts, contracts and goods-origin records; current form not registered. Classify cash/card/PSP versus verified direct bank and qualifying service exceptions transaction by transaction. Undocumented expenses cannot be accepted as deductions merely because they were paid. Ordinary 1095-day category may be superseded; a 141.4 payment-control document belongs to the 2555-day route, not a guessed1825. Cost eligibility, depreciation and any nonresident payment require separate review.

**Original D: Group 1 market trader.** Facts remain retail at a market to individuals, within Group1 limits. Maintain free-form monthly income reflection backed by transaction records; 296.10 exempts a genuine Group1 payer. Online/delivery expansion or listed goods triggers eligibility/goods-specific review; it does not make the old “every listed good overrides296.10” claim correct. Retain origin evidence where required. A voluntary daily register is useful, not a universal Group1 daily statutory form.

## When to refuse or refer

Retain all eight original accountant-judgment jobs:

1. **Payment-chain classification:** actual bank/acquirer/PSP/marketplace/collection-on-delivery contracts and codes2924/2650/2654; service versus goods and settlement place; no brand-based exemption.
2. **Group1 format:** market/household eligibility and changed online/delivery channels; a registration label alone cannot prove continuing eligibility.
3. **Listed goods:** warranty goods, medicines/devices, jewellery and excise goods; actual lists, licensing and genuine group status, not a blanket override.
4. **Goods-origin evidence and stock-book scope:** refer missing or insufficient supplier/import records and actual statutory exemptions.
5. **General-system cost eligibility:** documents, business link, payment/use period, depreciation and mixed use; no automatic deduction.
6. **Retention:** each1095/1825/2555category,141.4nonresidentcontrol,assets,nonfiling/closure/audit/litigation/COVID/war/suspension timeline; do not authorize destruction under a generic rule.
7. **FX date/rate:** credit versus value/intermediary/conversion dates, original currency, documents and current NBU supervision exceptions; no invented rate or export deadline.
8. **Limit breach/status change:** coordinate dated reclassification, records and reporting with `ua-single-tax`; do not infer an automatic retroactive PRRO obligation without the actual law/settlement facts.

Also stop for a missing required source document, unresolved PRRO/offline or penalty relief, disputed professional/company status, unverifiable actual receipt or a mismatch that cannot be reconciled. Prepare a reviewer package with branch/timeline, record format, documents, payment-channel analysis, reconciliation, retention classification/holds and unresolved questions. It is provisional until qualified Ukrainian professional review.

### Completion checklist

- [ ] Correct regime/group/VAT or independent-professional branch and effective dates; correct income-only/prescribed income-expense form.
- [ ] Paper/electronic records reconstructable, backed up and in the required structure; no invented book-registration task.
- [ ] Monthly non-VAT totals versus required daily261 records distinguished; receipt dates, FX and refunds supported.
- [ ] Cash/POS/online/PSP/direct-bank flows actually classified; every applicable exception documented before a no-RRO conclusion.
- [ ] Required PRRO and cashier certificates registered; fiscal receipts, numbers, acknowledgments and Z-reports retained/reconciled; no unsupported offline operation.
- [ ] Contracts, invoices, acts, delivery notes, payments, statements and credit/SWIFT advice linked to the records; document sufficiency reviewed.
- [ ] Goods-origin and actual stock-book obligations reviewed; no universal expense-ledger demand on non-VAT turnover taxpayers.
- [ ] Every retention category/start/extension/hold documented; source-backed accountant decision before any disposal.

### Prohibitions preserved and corrected

Do not assert a current tax-office ledger-registration requirement from an obsolete book. Do not promise no PRRO without verified group/activity/settlement facts or ignore a real services exception. Do not authorize disposal at1095days, on software expiry or simply because there was no audit; preserve and refer until actual legal conditions are established. Do not impose an expense ledger on ordinary non-VAT single tax or imply its source documents are disposable. Do not quote a final penalty or NBU repatriation term without current full eligibility/relief verification. Do not compute tax, ЄСВ, levy or VAT here, and do not provide TOV/company accounting through this FOP skill. Do not call this accountant-attested or claim every source/regulatory schedule has been read.

## Sources

Actual reads **2026-11-15**. Official operative paragraphs and neighboring exceptions were read at the scopes below. The full consolidated Tax Code, full current Law265 and full Order405 were not all recovered/read; no such blanket read claim is made. Direct Parliament law/print attempts were inaccessible; ordinary official Tax Service texts support the bounded statements and remaining details stay held.

| Official source | Read for | Read date |
| --- | --- | --- |
| [Tax Code, official consolidated DPS publication](https://tax.gov.ua/nk/) | Read for44.1,44.3-44.7,86.14,XX.10.74-1,102.3,177.2/.4/.10,291eligibility/household/jewellery,292receipt/FX/refund,296.1/.10 and69.9includingexceptions; not entireCode or finalarchive/deletionanalysis | 2026-11-15 |
| [2 July general-system records](https://kh.tax.gov.ua/media-ark/news-ark/print-1026346.html) | Read for full operative explanation:26113May2021,paper/electronic/certifiedcopy,dailyentries,separatesectors,noformregistration | 2026-11-15 |
| [10 September general-system timing](https://tr.tax.gov.ua/media-ark/news-ark/print-1048797.html) | Read for full explanation:net/documentedcostcategories,dailyrecords/receipt/expenseandgoodsactuallysoldorused | 2026-11-15 |
| [8 May independent-professional form](https://tr.tax.gov.ua/media-ark/news-ark/print-1008795.html) | Read for full explanation:261effective16July2021,dailyrecords,paper/electronic/copyandnoregistration;notallequatedFOPtaxrules | 2026-11-15 |
| [1 July VAT-Group3 form](https://rv.tax.gov.ua/media-ark/news-ark/print-1026027.html) | Read for full operative body:prescribed40530November2022,agriculturalseparation,formats,ere sidentexception;full405columninstructionsnotrecovered | 2026-11-15 |
| [9 April Cabinet record service](https://tr.tax.gov.ua/media-ark/news-ark/print-999349.html) | Read for full operative explanation:261Cabinetfunction,KEP,freeuse,3yearsoftwarewindow,correctiontrailanddepreciationmode;notlegaldisposalpermission | 2026-11-15 |
| [3 April internet/payment-chain RRO explanation](https://zp.tax.gov.ua/media-ark/news-ark/print-1009759.html) | Read for full operative body:Law265art3,Group1,currentpayment-chain/terminalreceipt/distinctelectronicdeliveryexception/receiptdeadline | 2026-11-15 |
| [2 October QR payment method](https://tr.tax.gov.ua/media-ark/news-ark/print-1055743.html) | Read for full operative body:QRnotitselfpaymentinstrument,bankIBANcredittransferversusotherinstrumentandbank-operationexceptionconditions | 2026-11-15 |
| [National DPS service exception, 2023](https://nvp.tax.gov.ua/media-ark/news-ark/725416.html) | Read for full operative2023body:9(14)remote-bank/transfer-servicesonly,noacceptedcash/card/tokensetc,goodsnotcovered,mixedgoodsandservicesretainservicebranch;notcurrentproduct-specificassurance | 2026-11-15 |
| [Official PRRO FAQ](https://tax.gov.ua/baneryi/programni-rro/aktualni-zapitannya-vidpovidi) | Read for questions1-3,7-19,21-28,45,49-50:registration/cashiers/freeandcommercial/softwarehardware/receipts/offlineandexception/numberranges/search/timestampsandZcontexts;notentireFAQorallcurrentconsolidatedofflineprovisions | 2026-11-15 |
| [17 August Z-report interruption guidance](https://rv.tax.gov.ua/media-ark/local-news/1040850.html) | Read for full operativebody:dailysettlements/vendingexception,airalarm/powerfailureactualimpossibility,nextworkingdaybeforestart;noautomaticclientrelief | 2026-11-15 |
| [29 April 2026 penalty explanation](https://poltava.tax.gov.ua/kampaniya-prro/print-1005661.html) | Read for full operativebody:specifiedviolations100/150from1August2025,earlierreduced25/50andconditions/end;notfullcurrentterritorialrelieforactualassessment | 2026-11-15 |
| [Historical 20 February 2024 FX supervision explanation](https://cvp.tax.gov.ua/media-ark/news-ark/print-757248.html) | Read for full bodyconfirmingResolution67services/work/IPexceptionsexistashistoricalcontext;its180/400k/agriculturalfiguresnotusedascurrent2026rules | 2026-11-15 |

Not yet confirmed: actual commencement of the 44.4 foreign-official extension under both XX.10.74-1 triggers;  complete current Order405 columns/timing/corrections; universal historical1January2021registrationclaim; exact Law265 goods-stock/Order496scope and listed-goods exceptions; current full9(14)/product-specificsettlementclassificationwherefactsuncertain; completeofflinecaps/rangesandcurrentwartexception;X-reportcurrentfirmwaredetails;invoice-instead-of-act sufficiency; independent-professional/general FX specifics; current NBU export-service supervision/exceptions/terms; full penalty/territorialrelief; period-specificCOVID/war/archive/no-auditretentionandfinaldisposaldate. Missingdocs/rate/date/classificationorunreconciledamountsblockrelease.

## Disclaimer

This skill is a source-cited process draft with the exact official read scopes and unresolved branches above. It has not yet been signed off by a qualified Ukrainian accountant or auditor. Ukrainian record-keeping and PRRO rules change frequently and are affected by martial-law measures. This is general information, not tax or legal advice; a credentialed Ukrainian professional must review any output before it is used for filing or compliance. Part of the open-source library at openaccountants.com. Contributions and corrections from qualified Ukrainian practitioners are welcome.
