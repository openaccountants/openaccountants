---
name: laos-vat
description: "Classify Laos VAT transactions for 2026 using actual invoices, supply and supplier facts; prepare a reviewable monthly working paper and hold unsupported treatments."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/laos-vat"
  jurisdiction: "LA"
  tax_year: "2026"
  last_updated: "2026-11-17"
---

# Laos VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Written by Codex. Not reviewed by an accountant.

## Scope

Use this skill with `vat-workflow-base` v0.1 or later to classify documented 2026 Laos transactions and prepare a VAT working paper. A bank statement is a starting reconciliation record, not a tax invoice, export proof or a completed return. This is the ordinary regime; SEZ incentives and concessions retain the refusal rules below.

**Quick reference:** taxable domestic supplies and covered imports/non-established foreign supplies generally use 10%; qualifying goods exports use 0%, which differs from exemption. Ordinary monthly declaration and payment are due by the following month's 20th; the specified foreign-supplier withholding branch has its own 15-day clock. [VAT Law 60/NA, Articles 3(16), 12, 17, 30 and 31](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

## Ask the client first

- What TIN, VAT-system status, exact month and business activities apply, and is the entity a micro-business, SEZ or concession enterprise?
- For each bank line, what invoice/credit note, contract, actual supply, supplier establishment and place-of-supply facts support it?
- Is the amount gross including VAT, a VAT-exclusive price, a deposit, a payment net of withholding or a non-sale movement?
- What export/import declarations, goods classification, transport and bank-settlement evidence exist?
- For each purchase, what taxable business use, valid VAT evidence, Lao-bank settlement and declaration/claim timing are proven?
- What credit brought forward, prior return, corrections and actual payment/withholding records reconcile to this month?

## The method, step by step

### Establish supply, classification and registration [https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf)

Identify the actual goods/service and Lao supply connection under Articles 11–13 before selecting a rate. Electronic supplies by domiciled or non-domiciled providers are expressly within Article 11; a brand name alone does not identify the liable party. Businesses with enterprise registration, TIN and the relevant operating permission enter the VAT system under Article 33; micro-enterprise entry has separate rules. Do not invent an ordinary turnover threshold.

| Rate or treatment | Conditions | Official source |
|---|---|---|
| 10% | Covered imports, taxable supplies in Laos and purchases from foreign legal entities without a Lao enterprise; first check exemptions and the supply/collection branch. | Articles 11–13 and 17(1): https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |
| 0% | Qualifying goods exports abroad or to the specified zones, including finished mineral products; check Article 12 exempt export categories and actual customs/export facts. Do not extend the goods rule to every foreign customer or service. | Articles 3(3), 3(16), 12(3) and 17(2): https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |
| Exempt | Only the actual Article 12 category: e.g. specified unprocessed/initially processed agriculture and animals, qualifying education, medical services, specified financial transactions, international transit transport and other listed cases. “All public transport” is not established. | Article 12: https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |

Zero rating permits the appropriate input-credit/refund route subject to conditions; exemption does not itself permit a credit/refund for its related inputs. Do not code them as the same bucket. [Article 3(16), with Articles 21–29](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Compute the correct base and output tax [https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf)

For ordinary domestic supplies, use the supply value plus excise where applicable, excluding VAT. If an invoice confirms a gross VAT-inclusive ordinary price, net = gross / 1.10 and VAT = gross − net. For imports within Article 15(1.1), use the actual border value plus import duty **and excise where applicable**, not bank cash or duty alone. Article 15(1.5) separately adds **gross profit** for goods imported for the importer’s own use. Do not apply the Article 15(1.1) formula alone to that branch: its gross-profit measurement and implementation have not been established here, so hold the own-use import computation until the operative instruction and actual use facts are confirmed. Foreign non-established supplier purchases use the actual VAT-exclusive value in Article 15(1.3); a bank amount cannot prove whether VAT was included or withheld. Convert foreign-currency business revenue into kip using the Bank of the Lao PDR rate at the relevant time and retain the dated rate/source, rather than assuming one rate for every bank line. [Articles 14–18](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

Domestic VAT is computed/collected on the supply; exchange, gifts, debt settlement and self-use have their specific actual-use/transfer rule. Imports are assessed with the import declaration; covered non-established foreign supplies are withheld when the supplier is paid. The bank posting date alone does not replace those events. [Article 18](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Admit a credit only after the conditions pass [https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf)

Credit requires direct use in producing/doing business in taxable goods or services and all Article 23 conditions: required regular declarations, approved payment route for tax, Lao-bank settlement for purchases, correct complete supporting invoices/receipts/declarations and claim timing. For the covered non-established foreign supplier, the VAT must have been remitted. Begin the input claim in the month it arises; do not confuse unclaimed documents with an already declared credit carried forward. [Articles 21–23](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

Article 24 excludes inputs linked to exempt supplies, amounts already deducted/refunded/expensed, deficient conditions, non-business/personal use, unsupported expenses and non-business asset/utility portions. It also excludes otherwise supported VAT not declared within the specified three-month window and has particular foreign-transport, electricity and mineral restrictions. Missing proof means **credit held pending evidence**, not a fabricated statutory 0% recovery rate. The old blanket passenger-vehicle and entertainment prohibition is not established by those labels alone; determine actual business use, evidence and any specific implementing restriction first. [Article 24](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

Reconcile output less admissible input and established credit brought forward. Article 32 distinguishes additional tax payable from credit carried to the next month; a credit is not an automatically approved cash refund. Refunds need their own Articles 25–29 conditions. Export refunds include proper books/invoices/export proof and the export-proceeds banking condition; unused-credit refunds have review conditions. [Articles 23–32](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Read bank patterns as leads, not legal conclusions [https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf)

| Original pattern library | Evidence-led treatment |
|---|---|
| BCEL / BANQUE COMMERCE EXTERIEUR; LDB / LAO DEVELOPMENT BANK; JDB / JOINT DEVELOPMENT BANK; PHONGSAVANH BANK; BFL | Obtain the actual fee. Article 12(2.12) covers specified deposit/loan interest, transfer revenue, FX gains and other financial transactions of licensed banks/financial institutions. A bank name does not prove every fee exempt. |
| INTEREST, LOAN, REPAYMENT | Separate qualifying financial-service interest from principal and fees. Proven borrowing/principal movements are not sales simply because cash moved; verify the contract. |
| TAX DEPARTMENT / MOF; CUSTOMS / LAO CUSTOMS; LSSO / SOCIAL SECURITY | Reconcile proven tax/duty/contribution payments outside sales. Customs import VAT has its own documented input analysis; never exclude all customs payments as duty. |
| EDL / ELECTRICITE DU LAOS; NPLAOS / LAO WATER; LTC / UNITEL / ETL | Read the utility/telecom invoice and actual supply. Taxable use and credits are conditional; electricity has express special rules, so neither supplier identity nor payment alone proves recoverable VAT. |
| GOOGLE / MICROSOFT / META / AWS; ZOOM / SLACK / CANVA | Obtain supplier/invoice and registration/establishment details, service location and gross/net/withholding facts. Apply the established foreign-supply branch only after those facts; special digital-provider implementation is not completed here. Do not double-charge VAT already properly collected or assume an equal input credit. |
| SALARY / WAGES; OWN TRANSFER / INTERNAL | Exclude only after evidence proves employment pay or an internal movement, rather than a taxable supplier service. Reconcile both sides of transfers. |
| CASH WITHDRAWAL | Ask the purpose and obtain underlying receipts. Hold classification; withdrawing cash does not prove a deductible purchase or an exempt supply. |
| Vehicle costs / entertainment / rent | Check actual use, invoice, taxable landlord/supplier status, evidence and specific restrictions. Hold any credit without proof; do not use an invented recovery percentage. |

Legal classification and credit support above: [Articles 11–15 and 21–24](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf). Names are reconciliation search strings, not determinations of the client's actual suppliers.

## Boundary and exception table

| Ambiguity or exception | Action |
|---|---|
| Unknown sale rate or counterparty location | Hold classification and request the supply, place and invoice facts. Never default to domestic 10%. |
| Unknown purchase VAT or business-use proportion | Hold the credit and request evidence; do not label this a statutory denial or assume a percentage. |
| R-LA-1: client in SEZ with tax incentives | Refer for the actual zone/authorization instruments. SEZ status does not automatically exempt all transactions; the law expressly covers specified zone movements. |
| R-LA-2: client with a government concession (mining, hydropower) | Refer for the concession and current sector/investment instruments. Do not calculate bespoke incentives from this ordinary skill. |
| Digital-provider special regime, foreign transport or mineral/electricity special branch | Resolve actual establishment, transaction and implementation before computing or crediting. |
| Historic 7%-to-10% transition | The old transition remains outside this 2026 ordinary computation. Read Ordinance 003/2024 plus actual implementing dates and supply facts for historical adjustments. |

## Worked cases

### Original case 1: domestic sale, conditional on invoice evidence

05.04.2026 ; LAO TRADING CO ; CREDIT ; Invoice LA-041 ; LAK 11,000,000

The bank input is unchanged. **Illustrative additional assumption, not a recovered client fact:** Invoice LA-041 proves an ordinary taxable domestic supply and an LAK 11,000,000 VAT-inclusive price, with no exemption or special regime. Net = LAK 10,000,000; output VAT = LAK 1,000,000. Without that invoice/classification evidence, hold rather than applying this arithmetic. [Articles 13–18](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

```oa-check
name: Original LA-041 inclusive domestic sale with confirmed classification
inputs:
  gross: 11000000
steps:
  - net: gross / 1.10
  - output_vat: gross - net
expected:
  net: 10000000
  output_vat: 1000000
```

### Original case 2: export evidence is missing

15.04.2026 ; THAI BUYER CO ; CREDIT ; Exported wood ; LAK 50,000,000

Keep the original input, but **hold classification**. “Exported wood” and a foreign customer do not establish the actual goods/category, lawful documented export or whether Article 12 excludes the supply from the zero-rated branch. The legacy table's LAK 50,000,000 net and zero VAT were an unsupported filing conclusion. If the goods and complete documents establish Article 17(2) zero rating, the arithmetic is LAK 50,000,000 × 0% = zero; that conditional identity is not an approval of this actual line or its input-credit/refund entitlement. [Articles 3, 12, 17 and 27](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Original case 3: foreign digital invoice and settlement branch unresolved

18.04.2026 ; GOOGLE ; DEBIT ; Google Ads ; LAK 2,200,000

Hold the output/withholding and input classification. The legacy LAK 2,000,000 net/LAK 200,000 VAT split assumes a VAT-inclusive domestic-style gross; Article 15(1.3) instead uses the actual VAT-exclusive foreign-supply value when that branch applies. The bank input does not establish that value, supplier establishment/collection status, digital regime or paid withholding. Do not post the old automatic “Output + Input” result. Obtain the invoice and resolve who collected/remits and whether Article 23's credit conditions pass. [Articles 11, 13, 15, 17–18, 23 and 30–31](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Original case 4: bank fee type unresolved

30.04.2026 ; BCEL ; DEBIT ; Monthly fee ; LAK -50,000

Retain the negative bank amount. Hold exemption classification until the fee is identified. If it is a qualifying licensed financial transaction under Article 12(2.12), apply that exemption; the bank name and the words “Monthly fee” do not establish it. No input VAT is inferred from the payment. [Articles 12 and 23–24](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

### Case 5: decide whether documented input reduces the monthly balance

Illustrative ordinary month: LAK 22,000,000 confirmed VAT-inclusive domestic sales and LAK 5,500,000 confirmed VAT-inclusive taxable-business purchases, no brought-forward credit or other transactions. All Article 23 conditions pass and Article 24 does not exclude the input. Output VAT = LAK 2,000,000; input VAT = LAK 500,000; balance = LAK 1,500,000. If the purchase invoice/business-use evidence is missing, the credit stays held; the provisional working-paper balance before that unresolved credit is LAK 2,000,000. Resolve it before filing, rather than treating the provisional balance as final legal liability. [Articles 15, 17 and 21–24, 32](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

```oa-check
name: Decision on evidenced input credit versus pending evidence
inputs:
  gross_sales: 22000000
  gross_purchases: 5500000
steps:
  - output_vat: gross_sales - gross_sales / 1.10
  - evidenced_input: gross_purchases - gross_purchases / 1.10
  - balance_if_all_conditions_pass: output_vat - evidenced_input
  - provisional_before_held_credit: output_vat
expected:
  output_vat: 2000000
  evidenced_input: 500000
  balance_if_all_conditions_pass: 1500000
  provisional_before_held_credit: 2000000
```

## When to refuse or refer

Keep R-LA-1 and R-LA-2 active for their original triggers. Also stop a filing-ready result for missing invoices, goods/service/place facts, supplier collection status, unresolved imports/digital supplies, undocumented credit brought forward or unknown claim timing. Neither the minimum bank record nor an arithmetic check authorizes filing. Do not manufacture a filing month from dates in sample bank lines.

## Filing and payment

| Branch | Declaration/payment clock | Official source |
|---|---|---|
| Ordinary VAT registrant | Monthly; declare and pay no later than the 20th of the next month. | Articles 30(2) and 31(2): https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |
| Purchase from covered foreign legal entity without a Lao enterprise | Declaration no later than 15 days after computation/collection/withholding; payment within 15 days from payment to the supplier. Identify actual trigger dates separately. | Articles 18(3), 30(3) and 31(3): https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |
| Import | Declare with customs at import; payment follows Article 31(1)'s permitted customs/treasury/bank or specifically authorized procedure. | Articles 18(1), 30(1) and 31(1): https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf |

Article 23 names Tax RIS and approved tax-payment channels, but Article 30 leaves forms, invoice schedules and electronic filing details to separate rules. The current live form, fields/boxes, login URL, receipt and payment-reference walkthrough have not been confirmed. Do not call a working paper filed or invent those fields. [Articles 23 and 30–31](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

Prepare the `vat-workflow-base` working paper with separate columns for original bank line, invoice/declaration, supply and tax-point date, currency and dated conversion source, rate/category, taxable base, output, domestic input, import/foreign-supply input, credit status, brought-forward credit and net balance. Preserve separate zero-rated and exempt columns, reasons and unresolved items. BCEL/LDB/JDB and the other original bank patterns remain import/reconciliation leads; actual CSV/export formats and USD/THB conversion inputs must be inspected rather than presumed. Do not duplicate a cash receipt, transfer or import-VAT payment.

## Completion checklist

Reconcile original cash signs, invoices and customs records; confirm registration, exact month, taxable categories, imported services, every credit condition and brought-forward amount. Recompute the return working paper, keep withheld/paid VAT separate from ordinary output, and retain proof of acceptance/payment when eventually filed. Article 35 requires accounting evidence kept for ten years. [VAT Law Articles 21–24, 30–36](https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf).

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| Native VAT Law 60/NA, 28 June 2024, Articles 2–3, 6–18, 20–38 and 59–61; definitions, complete exemptions, place/base/rate/collection, input and refund exceptions, declaration/payment and commencement; rate/base and poor OCR checked visually | https://laoofficialgazette.gov.la/kcfinder/upload/files/%2060.28.6.2024.pdf | 2026-11-17 |
| Native Ordinance 003, 19 March 2024, Articles 1–4, old statutory rate change from 7% to 10%; not a completed historical invoice-transition determination | https://laoofficialgazette.gov.la/kcfinder/upload/files/003%2019.3.2024.pdf | 2026-11-17 |

Not yet confirmed: client-specific SEZ/concession incentives; digital-provider special implementation and supplier collection status; foreign-transport/mineral/electricity special calculations; complete live form/box/login/acknowledgment/payment steps; current micro-business entry and simplified input rules; detailed invoice-format rules including legacy TIN-field prescription; any categorical passenger-vehicle/entertainment block beyond the conditions actually read; historical rate-transition timing; actual BCEL/LDB CSV formats; specific late-filing/interest/penalty figures; accountant approval. These held branches must not be used as exemptions, zero rates or credits.

### Change log

v2.1 (17 November 2026): Native-law rewrite; restores documentary conditions, separate foreign-supplier timing and preserved original cases with unsupported outputs held. Legacy v2.0 (April 2026) described a ten-section rewrite; that history is not validation of its former classifications.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-17. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `laos-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/laos-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
