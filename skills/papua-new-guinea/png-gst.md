---
name: png-gst
description: >
  Prepare an already registered PNG business GST working paper for 2026 using the published IRC G1 lines, standard output/input calculation, direct and common input attribution, special-payment withholding and enacted household-goods relief. Confirm registration and assigned period from records. Missing current legal inputs remain held rather than being filled from old unsupported figures.
jurisdiction: PG
category: international
tax_year: 2026
last_updated: 2026-11-16
version: 1.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Papua New Guinea GST return preparation v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare a supported 2026 PNG GST working paper for an already registered business with its filing period confirmed by IRC. Use the IRC G1 return published with an effective date of January 2024, its instructions and the enacted budget amendments. This is a field-mapping and review workflow, not proof that the live portal or every general GST provision was accessed. Do not submit a return or apply a registration threshold without the actual current registration rule and client's status record.

| Field | Entry |
|---|---|
| Contributor | Open Accounting Skills Registry |

The old guide's internal confidence tiers were workflow tags, not professional approval. Here a confirmed rule has an official source; an unresolved legal condition is held explicitly. Do not call any bank-narrative classification deterministic or “no reviewer judgement required”.

### Quick reference

| Item | Rule or figure with conditions | Official source |
|---|---|---|
| Standard GST | 10% of the standard-rated value; registered suppliers account for output and eligible input GST | [IRC GST factsheet, explanation and example](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf) |
| Inclusive standard-rated price | Derived GST fraction 1/11; this is not the tax fraction for an exempt or zero-rated supply | [IRC G1 line 6](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Household goods in the statutory list | 0%, zero-rated in words on the page, from 1 June 2025 through 31 December 2026 | [2025 Budget amendment s. 2](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf); [2026 Budget amendment s. 2](https://pdis.parliament.gov.pg/uploads/953e2445-7185-4aa7-9d0f-0fcea47e75a9) |
| Longer taxable period | Turnover in the preceding 12 months not above PGK 1,500,000 permits IRC to substitute a period not exceeding 3 months, subject to conditions; not automatic quarterly filing | [2025 Budget amendment s. 3, replacing GST s. 26(3)](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf) |
| Ordinary monthly return | Official factsheet states by 21st of the following month; verify an approved longer period or varied due date separately | [IRC GST factsheet page 3](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf) |
| No prior-credit subtraction on G1 | The form states no requirement to carry forward prior months' accumulated credits; do not deduct them again | [IRC G1 notes, Credit Carried Forward](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |

The temporary product list is baby diaper, soap, biscuit, cooking oil, flour, chicken, noodle, rice, sanitary pad and tampon, tea, coffee, tinned fish and tinned meat. Apply the actual product description and supply date, not a blanket exemption for groceries, processed fish, all agriculture or all household purchases. Although placed in the section headed Exempt Supplies, the enacted text expressly describes these as zero-rated goods. The subsequent amendment extends the end date, not the product list. [2025 amendment s. 2](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf); [2026 amendment s. 2](https://pdis.parliament.gov.pg/uploads/953e2445-7185-4aa7-9d0f-0fcea47e75a9).

## Ask the client first

Obtain entity and TIN, GST registration and effective dates, assigned taxable period and any variation, activity and locations, sales/purchase ledgers, invoices and credit/debit notes, imports and Customs assessments, export evidence, exempt and private-use allocations, bank reconciliation, prior returns/account balance and any withholding notices/certificates. Determine whether supplies involve employee benefits, government buyers, connected entities, resource agreements or overseas services. Use existing case records before requesting missing facts.

Stop return finalisation if entity, registration or period is unknown. Do not infer no registration from a modest current-period bank balance, or quarterly status from turnover alone. A business below an unconfirmed threshold cannot be declared outside the registration rules. Historical credit balances are reconciliation items and possible refund claims, not an invented G1 carry-forward field.

## The method, step by step

### 1. Build the supply and evidence schedule

For every transaction record supplier/customer, invoice and supply dates, description, location, consideration and currency, tax amount, evidence, business/private use and the classification rationale. Identify sale/output versus purchase/input separately. Salary, a loan principal movement, a dividend, a superannuation transfer or an own-account transfer is not automatically consideration for a GST supply; check what actually happened and preserve the ledger trail. Tax classification follows the supply, not the bank direction alone.

Domestic, imported and exported transactions have different rules. An overseas address does not by itself prove export zero-rating or a reverse charge. Capital goods, trading stock and services/overheads need separate asset and input-credit records; an asset useful for more than a year is not automatically an immediate income-tax expense. Use actual invoice-period data where the G1 form requires an invoice basis, not a cash bank summary. [IRC G1, front page and Notes 1-4](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

### 2. Distinguish standard-rated, zero-rated and exempt

The G1 instructions separately list exempt sales and zero-rated sales. Zero-rated supplies can preserve related input credit, whereas exempt supplies restrict attributable input GST. The form's ordinary exempt categories cover health, education, gambling and financial services, with specific employee vehicle/housing treatment. It does not support the old blanket list declaring fresh food, domestic water, public transport and all residential rent exempt. Hold the exact category until the current statutory exemption and its conditions are read. [G1 Notes 2, 4 and 5](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

The G1 zero-rating instructions identify qualifying exports, travel outside PNG, duty-free-shop sales, ships/aircraft stores for use outside PNG, a business sold as a going concern, specified medical supplies, prescription glasses supplied by a registered doctor or optician and refined gold, silver or platinum sold by the refiner to a metal dealer or jeweller. Do not replace those conditions with “all gold”, “all international shipping” or “all medical services”. Export evidence must establish the applicable export timing and conditions; the form describes export within 28 days. [G1 Note 3](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

For a medical supply, use the current applicable IRC ruling rather than treating the form's cross-reference as the ruling's full text. For a going concern, determine the legal conditions rather than zero-rating any sale of assets. Mining, petroleum and LNG agreements, zero-rated project supplies and imports require the actual applicable agreement and statutory provision. Resource status alone does not give a universal zero rate.

### 3. Prepare the actual G1 field mapping

The published G1 has numbered lines and three calculation blocks. The old invented Parts A-F and B.1/E.1 fields are not return boxes. TIN, taxpayer/contact/address and period appear above the calculation. Retain the official field names in the working paper and reconcile to the actual form version used for filing. [IRC G1 form](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

| G1 field | What to enter or calculate | Official source |
|---|---|---|
| Line 1 | Total sales including GST and applicable withholding sales; include benefits only under the applicable legal valuation rule | [G1 line 1 and Note 1](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Lines 2 and 3 | Exempt sales and zero-rated sales, separately | [G1 lines 2-3 and Notes 2-3](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 4 | Computed: line 2 plus line 3 | [G1 line 4](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 5 | Computed: line 1 less line 4, GST-inclusive standard-rated sales | [G1 line 5](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 6 | Computed: line 5 divided by 11, output debits | [G1 line 6](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 7 | Deferred import liabilities, only for entities with approved GST deferment | [G1 line 7](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 8 | GST paid on business inputs in the period, subject to the form's exclusions and attribution | [G1 line 8 and Note 4](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Lines 9 and 10 | Input GST for exempt sales and private purposes, separately | [G1 lines 9-10 and Notes 5-6](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 11 | Computed: lines 9 plus 10 | [G1 line 11](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 12 | Computed: line 8 less line 11, input credits | [G1 line 12](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 13 | Computed: lines 6 plus 7, output debits | [G1 line 13](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 14 | Copy line 12 input credits | [G1 line 14](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 15 | Computed: line 13 less line 14, GST payable or refundable before the separate withholding credit | [G1 line 15](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |
| Line 16 | GST withholding credit under the special-payment provision, with the actual withholding evidence | [G1 line 16 and Note 8](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf) |

The separate sales-by-province schedule reconciles total taxable sales to the form and allocates positive net GST proportionately as instructed. Keep one province total and the overall reconciliation; do not invent extra tax by paying the same net amount separately for each location. Follow the published instructions for a refund rather than completing a positive-payable allocation mechanically. [G1 sales-by-province instructions](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

The printed common-input worksheet contains a conflicting transfer-line reference. The face of the form identifies exempt-input attribution separately from total inputs. Follow the correct numbered fields on the return and retain an explicit worksheet reconciliation; never reduce business inputs and then reduce them again for the same exempt-use amount. [G1 Note 5 and lines 8-12](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

### 4. Establish input-credit eligibility and restrictions

Obtain a tax invoice or other legally permitted evidence, supplier identity/registration, actual supply/import and business use. A payment receipt alone does not prove a recoverable input. Non-registered buyers cannot use this registered-person return to recover tax. Do not manufacture an input GST amount on a purchase from an unregistered seller. Keep exempt, private and taxable purposes separate. The supplier's TIN and an invoice showing tax do not by themselves cure an ineligible underlying supply. [IRC G1 Notes 4-7](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf); [IRC factsheet output/input explanation](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf).

First attribute inputs used exclusively for taxable/zero-rated activities and exclusively for exempt activities. Apportion only the common inputs under the form's supported method, with the relevant sales values and period. Then separately account for private use. The old formula applying one taxable-sales ratio to all inputs would incorrectly reduce directly taxable inputs and over-credit directly exempt ones. [G1 Note 5](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

The G1 car restriction includes defined cars and related vehicles, with a dealer/rental-car exception, rather than just private-use cars. The published note includes four-wheel-drive vehicles, station wagons, motorcycles, panel vans, light utility trucks and smaller passenger buses within its definition. Obtain the actual vehicle specification and exception before claiming input credit; do not treat business use alone as sufficient. Employee-provided cars and housing have separate exempt-supply/input restrictions. [G1 Notes 2, 4 and 7](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

The form does not support a blanket input-credit prohibition for every entertainment, club subscription, alcohol or tobacco purchase. It discusses specified employee benefits and their output/input treatment. Test the supply, taxable purpose, employee benefit valuation, private use and specific restriction. Do not import an income-tax entertainment restriction into GST without authority. Current employment-benefit values must be checked against the new income-tax law and applicable regulations; the historical values reproduced in the form notes are not certified for 2026 by this read.

For second-hand goods from an unregistered seller, do not invent GST charged. The old statement that no input credit always means the entire price is immediately expensed is wrong: capital versus revenue treatment is separate. Any statutory deemed-credit concession needs its own current legal text, which was not read here; hold it rather than asserting it does not exist.

### 5. Imports, overseas services and special sectors

Use the Customs assessment and proof of import GST actually paid, or an approved deferment record. Tie recoverable GST to taxable business use, with capital assets separately identified. Do not derive every Customs tax base from the old simplified customs-value-plus-duty-plus-excise formula without the actual import rule and assessment. Approved deferred imports need the separate output-liability and input entries shown on G1 so the tax is neither omitted nor claimed twice. [G1 lines 7-8 and Note 4](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

For imported consulting or digital services, hold the reverse-charge conclusion until place of supply, recipient status, taxable use and the current charging provision are established. An Australian supplier's invoice alone does not authorise automatic self-assessed GST and an equal credit. Preserve the potential liability in an open-items schedule; do not conclude there is no tax merely because this read did not establish it.

| Original sector or edge case | Retained control and corrected treatment |
|---|---|
| Mining equipment imports | Obtain project agreement, import assessment and approved concession; refer before classification |
| Petroleum or LNG | Check project-specific exemption/zero-rating, subcontractor status and fiscal terms; no blanket contractor exemption |
| Gold or other fine metal | The form's domestic relief requires refined metal sold by the refiner to the specified recipient; export relief needs its own conditions |
| Farming and unprocessed food | No blanket fresh-food exemption is established; test registration and current product rule; listed chicken and other household goods have the temporary statutory relief |
| Fisheries | Tinned fish is in the temporary zero-rated list; the old all-processed-fish standard-rate statement is wrong during the relief period; other fish needs its actual rule |
| Agriculture inputs | Test actual tax charged, supplier and business use; do not promise credit on every seed/tool payment |
| Coffee, cocoa or copra exports | Require qualifying export evidence and timing, not just a commodity name |
| Construction, including remote works | Establish taxable supply, progress/invoice timing and actual supplier tax; no input on a tax-free village receipt merely because it is a business cost |
| Government supply or government buyer | Determine the actual supply rule and any withholding notice; government identity alone does not establish exemption |
| International freight | Establish actual qualifying travel/export/store provision before zero-rating and attributing inputs |
| Credit/debit note or returned goods | Preserve original and adjustment documents, reverse the affected output/input once under the applicable rule, not by deleting the original ledger entry |

### 6. Government and other special-payment withholding

An IRC notice can direct a buyer to remit GST charged by its suppliers directly to IRC. The supplier still reports GST-inclusive sales and output tax; the amount paid on its behalf is a separate withholding credit, not a reduction in sales or an additional purchase input. Keep buyer and supplier identities, amount withheld, payment date, applicable notice and certificate/statement. The buyer's remittance return is distinct from its own ordinary G1. [IRC special-payment factsheet, explanation and annex](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf).

Use the current buyer/supplier notice, not an assumption that every government contract is covered or that government withholding is only income tax. The budget amendment increases the special statutory notice-noncompliance fine range; old fines copied from an earlier factsheet must not be used as current. [2025 Budget amendment s. 5](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf).

### 7. File, pay, reconcile and handle refunds

Confirm the assigned period and any due-date variation. The amended longer-period provision is discretionary and conditional; turnover eligibility alone does not authorise quarterly filing. The amendment also permits IRC to vary return dates for specified cases/classes. Preserve approval and the assigned due date with the working paper. [2025 Budget amendment ss. 3-4](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf).

Review the completed G1, sales/input schedules, provincial allocation and any special-payment credit. A bank statement supports payment reconciliation but not the invoice-basis sales total by itself. Use the current authorised IRC filing/payment channel, preserve submission acknowledgement and payment reference, and reconcile to the taxpayer account. No live account, portal submission or form completion was performed in this audit. Do not promise that every tax can be filed in a particular old MyIRC menu.

If the G1 calculation is negative, reconcile the excess to the IRC account and refund-claim process. The published form expressly rejects a required carry-forward of accumulated monthly credits. Do not subtract an old account credit again from the next return. For withholding-driven refunds, the factsheet requests the return and a supplier listing with supplier names, TINs, expense/tax amounts and descriptions. Keep supporting invoices and the buyer's withheld-tax evidence. No guaranteed processing period or automatic requirement for several successive credit months is established. [G1 credit note](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf); [IRC factsheet refund instructions](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf).

The enacted amendment changes the refund-application limitation provisions by tax year. It is not a promise to issue a refund within that many years. Before a limitation conclusion, obtain the complete current refund section and classify the applicable subsection and year; do not reuse the old invented refund section numbers or a processing-time estimate. [2025 Budget amendment s. 6](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf).

### 8. Penalties, records, audit and objections

The prior late-filing-per-day, invoice, fraud and flat record-keeping penalty table was unsupported and must not be used. The Tax Administration Act 2017 contains a different administrative-penalty structure. Its income-tax application is expressly incorporated in the new Income Tax Act, but this audit did not read the Gazette material establishing the current GST commencement/transition and any subsequent administrative amendments. Therefore a numerical GST penalty, interest or appeal-deadline conclusion requires that current application to be established, not merely the existence of the older Act. Retain the actual notice and service date and obtain immediate practitioner review. [TAA ss. 24-30, 39, 79 and 92-101](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d).

Record-keeping remains a real obligation: keep sales and purchases, tax invoices, credit/debit notes, Customs and export evidence, GST control ledger, bank/payment records, stock and assets, payroll records relevant to benefit supplies, notices and return acknowledgements. The TAA record provision specifies retention after the tax period with extensions for amendment periods, losses, audits and proceedings; confirm its applicable current GST operation before setting a destruction date. Never destroy material supporting an open enquiry.

Do not promise a universal audit window. Preserve the return and assessment dates, distinguish ordinary amendment periods from fraud/wilful-neglect cases, record grounds and payment arrangements and refer an audit, objection or Tribunal/Court appeal. The old fixed audit period and appeal sequence cannot be relied on without the governing current provisions.

### 9. Currency, adjustments and reviewer record

The G1 is denominated in kina. For foreign-currency invoices and imports retain original amounts, currency, supply/tax point, actual conversion source and assessment. The old blanket rule requiring a particular central-bank daily rate for every supply was not verified; obtain the statutory conversion rule and Customs treatment rather than guessing. A foreign currency contract does not justify a foreign-currency G1.

Every unresolved item carries the source document, amount, proposed treatments, missing legal/factual condition and the effect on output/input/net GST. A resource agreement, imported-service charge, exempt category or deemed second-hand credit not established by this source read is a held legal issue, not a “low confidence” number ready to file.

## Worked cases

All values are illustrative PGK inputs. Each case assumes registration and the stated legal supply classification are independently established. The form source for field mappings is the published G1, not a guessed portal layout. [IRC G1](https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf).

### Full G1 reconciliation, standard-rated local supplies

Standard-rated sales excluding tax are PGK 50,000 and GST PGK 5,000. Eligible taxed purchases are PGK 20,000 excluding GST, with PGK 2,000 input GST, no exempt/private attribution, no deferred import and no withholding. G1 total sales are PGK 55,000, output PGK 5,000, input PGK 2,000 and net payable PGK 3,000. This retains and corrects the old local-sale and purchase tests.

```oa-check
name: PNG G1 ordinary standard-rated sales and input
inputs:
  net_sales: 50000
  eligible_net_purchases: 20000
  exempt_sales: 0
  zero_sales: 0
  deferred_import: 0
  exempt_input: 0
  private_input: 0
steps:
  - line_1: net_sales * 1.10
  - line_4: exempt_sales + zero_sales
  - line_5: line_1 - line_4
  - line_6: line_5 / 11
  - line_8: eligible_net_purchases * 0.10
  - line_11: exempt_input + private_input
  - line_12: line_8 - line_11
  - line_13: line_6 + deferred_import
  - line_15: line_13 - line_12
expected:
  line_1: 55000
  line_6: 5000
  line_12: 2000
  line_15: 3000
```


### Common versus directly attributable inputs

Common input GST is PGK 50,000, with a supported taxable share of eighty percent and exempt share of twenty percent under the form method. In addition there is PGK 7,000 directly taxable input and PGK 3,000 directly exempt input. G1 total input is PGK 60,000, exempt attribution PGK 13,000 and eligible input PGK 47,000. Applying eighty percent indiscriminately to all inputs would be wrong. This retains the old mixed-supply test while correcting its scope.

```oa-check
name: PNG G1 common input attribution
inputs:
  common_input: 50000
  taxable_fraction: 0.8
  direct_taxable: 7000
  direct_exempt: 3000
steps:
  - line_8: common_input + direct_taxable + direct_exempt
  - common_exempt: common_input * (1 - taxable_fraction)
  - line_9: common_exempt + direct_exempt
  - line_12: line_8 - line_9
expected:
  line_8: 60000
  line_9: 13000
  line_12: 47000
```


### Withholding credit is separate from output

The official factsheet illustrates gross sales PGK 11,000, output GST PGK 1,000, input GST PGK 750 and GST remitted on the supplier's behalf PGK 1,000. Net G1 output less input is PGK 250; after the separately evidenced credit, the position is a PGK 750 refund. Do not reduce gross sales or claim the withholding as input tax. [IRC factsheet page 3](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf).

```oa-check
name: PNG supplier with special-payment GST withheld
inputs:
  gross_sales: 11000
  input_gst: 750
  withheld: 1000
steps:
  - output_gst: gross_sales / 11
  - line_15: output_gst - input_gst
  - after_withholding: line_15 - withheld
expected:
  output_gst: 1000
  line_15: 250
  after_withholding: -750
```


### Other original classification tests retained

- **Export:** PGK 200,000 coffee sale with the actual qualifying export/timing evidence goes to zero-rated sales, not invented field B.2. Output GST is nil under that established classification; input credit still needs its own eligibility.
- **Entertainment:** A PGK 3,000 payment and PGK 300 stated tax is not automatically blocked in full or credited in full. Determine business/employee/private use and the actual GST rule; hold the outcome until supported.
- **Import equipment:** A Customs assessment showing PGK 11,000 GST paid may support that input only with registration, taxable use and required evidence. Do not turn this document-based case into a universal Customs valuation formula.
- **Gold:** A PGK 5,000,000 domestic refined-gold sale needs the refiner/recipient conditions in the form instructions. If established, it is zero-rated; mining and a generic gold description alone are insufficient.
- **Late payment:** For PGK 10,000 paid after the assigned date, preserve the due date, payment date, notice and governing current penalty/interest provisions. The prior test's automatic fixed penalty is not certified for GST by this read.

A calculation engine must recompute the arithmetic, but it cannot supply missing legal classification, documents, approvals or rates. Never file without reconciliations, claim another person's GST, equate exemption with zero-rating, fabricate an input on an unregistered receipt or apply a project concession without its conditions.

## When to refuse or refer

Refuse finalisation for an unknown registration/period, unsupported supply classification, missing invoices or Customs evidence, unreconciled output/input/province figures or disputed credit. Refer resource projects, imported-service charging rules, current penalty commencement, refund limitation disputes, exempt categories not established here, special invoice concessions and audit/appeal cases. Drafts may be prepared transparently without inventing professional approval; filing advice requires the client's facts and a qualified practitioner's review.

## Sources

Read on 16 November 2026. A scoped read does not certify every provision in a long Act.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for IRC G1, effective 1 January 2024: all numbered fields and Notes 1-8, input attribution, vehicles, provincial allocation and credit note; historical benefit values not certified for 2026 | https://static.irc.gov.pg/2023/October/P0Jjks-media-g1_2023.pdf | 2026-11-16 |
| Read for IRC special-payment factsheet: standard rate, output/input, withholding notice and refund evidence; historical penalty annex superseded by amendment | https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf | 2026-11-16 |
| Read for Certified GST 2025 Budget amendment: zero-rated goods, longer taxable period, varied return date, special fine and refund limitation changes | https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf | 2026-11-16 |
| Read for Certified GST 2026 Budget amendment: commencement, monitoring classes and relief extension | https://pdis.parliament.gov.pg/uploads/953e2445-7185-4aa7-9d0f-0fcea47e75a9 | 2026-11-16 |
| Read for Tax Administration Act 2017: record, amendment, dispute, interest and penalty text read; current GST commencement/transition not established | https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d | 2026-11-16 |

Not yet confirmed: Current consolidated GST registration threshold and application wording, complete exemptions and refund provisions, Gazette commencement/transition for current GST administration, current penalty/interest inputs and dispute deadlines, live 2026 form/portal version, imported-services charge and Customs valuation, deemed second-hand credits, statutory invoice minima/concessions, current employee-benefit values and foreign-currency conversion rule. IRC legislation/registration pages returned an access block or JavaScript shell; no CAPTCHA was solved. The old unsupported exemption, penalty and processing-time figures are not usable guidance.
