---
name: pakistan-sales-tax
description: Use for pakistan sales-tax transaction classification workflow. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 2.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: router
---

# Pakistan sales-tax transaction classification workflow v 2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Start here

Load `vat-workflow-base` with this Pakistan workflow. Classify and reconcile transactions, then send the federal goods leg to `pk-sales-tax-federal` and each provincial/ICT services leg to `pk-sales-tax-services`. This 2026 skill supplies 2025-2026 cycle examples, not a common rate/deadline across all authorities. Mixed businesses may have several registrations/returns. Unknown country, goods/service, rate or tax status is a pending classification, not a domestic 18% default.

## Ask the client first

Obtain actual filing period(s), taxpayer legal identity/NTN and federal/provincial registrations, establishment/worker/customer locations, activity/category, invoice-level contracts and tax-exclusive/inclusive prices, sales/purchase/import/export ledgers, bank/wallet statements, goods/PCT/service CPC codes, delivery/payment/invoice dates, export and remittance evidence, actual supplier/recipient tax status, input invoices/use/payment support, withholding certificates, prior credit/returns/CPRs and actual exemptions/elections/SROs.

A bank statement is the starting completeness record, not sufficient tax evidence. If intake is incomplete ask for missing identifiers, authority type(goods/services/both), establishment and supply locations, actual period/frequency, exports and credit brought forward. Search available records before requesting information; do not infer the customer's supply province merely from the registered-office address.

## Route the work

| Actual issue | Owner and gate |
|---|---|
| Federal goods sale/import and federal registration | `pk-sales-tax-federal`: actual category/PCT/time/value/schedule/status and supporting documents |
| Domestic/provincial/ICT services, imported services or cross-province supply | `pk-sales-tax-services`: real service code/location/liability/rate/election/period |
| Income withholding on the same payment | `pk-withholding-tax`: separate from sales-tax withholding |
| Qualifying export income | `pk-it-export-tax`: PSEB/realisation/finality analysis separate from sales-tax export exemption |
| Real-time invoice integration/correction | `pk-einvoice`: actual applicable digital reporting and remediation |
| Books, payroll and owner transfers | `pk-bookkeeping`/`pk-payroll`: determine the underlying transaction before sales-tax exclusion |
| Refund, SRO manufacturer, EOU, sales-tax withholding or jurisdiction dispute | Specialist work with the actual operative rule and evidence before a final return |

## Rates, bands and thresholds

These are routing checks, not replacements for each owner skill's conditions.

| Confirmed cycle reference | Boundary and source |
|---|---|
| Federal 18% standard;4% further tax | Actual taxable goods and further-tax conditions/exclusions; no blanket higher/luxury rate or universal unregistered-buyer charge. [STA s.3](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Federal input timing/restriction | Relevant period plus 6 succeeding periods;90% ordinary adjustment restriction with fixed/capital asset, notification and other exceptions. [STA ss.7/8 B](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf) |
| Sindh 15% standard | Specific service/election/schedule can differ; IT 3% option and CPC 83159 exclusion are owned by services skill. [Sindh s.8/Second Schedule](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf) |

Zero-rate, exemption, outside-scope, nonclaimable input and provisional-unverified are distinct statuses. A 0 tax field must carry its actual reason. Federal s.4 zero-rating is not s.13 exemption; taxable-business input eligibility under ss.7/8/73 and provincial rules must still be established. [STA ss.4/7/8/13/73](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); [Sindh First Schedule 14](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf).

## Supplier pattern library: hints, never a tax determination

| Statement pattern retained | Initial classification and required evidence |
|---|---|
| HBL/HABIBBANK, UBL/UNITEDBANK, MCB/MUSLIMCOMMERCIAL, ALLIEDBANK, BANKALFALAH, MEEZANBANK, STANDARDCHARTEREDPK | Separate account transfer/principal from actual fee; bank fees can be provincial services, so do not label all financial services exempt |
| INTEREST/LOAN/REPAYMENT | Separate principal/interest/fees and own financing from underlying trade; route income/withholding separately; a description alone establishes no sales-tax credit |
| JAZZCASH/JAZZCASH, EASYPAISA/EASYPAISA, NAYAPAY/SADAPAY | Payment channel does not determine underlying goods/service. Separate platform/transfer fee and obtain actual invoice; do not universally exempt wallet fees |
| FBR/FEDERALBOARDOFREVENUE, CUSTOMS/PAKISTANCUSTOMS, SRB/SINDHREVENUE, PRA/PUNJABREVENUE, EOBI/SOCIALSECURITY, SECP | Actual tax/duty/contribution/registration remittance is a control/payment line, not a purchase invoice. Match CPR/GD; recoverable import tax comes from the proper customs evidence, not duplicate bank booking |
| K-ELECTRIC/KESC/LESCO/FESCO/IESCO, SSGC/SNGPL | Obtain utility invoice and separate sales tax, income tax, levies and principal; no 18% on the whole bill by pattern |
| PTCL/JAZZ/ZONG/TELENOR/UFONE | Telecom service/location/rate analysis, actual tax invoice; do not apply federal goods standard automatically |
| GOOGLE/MICROSOFT/META/AWS, ZOOM/SLACK/CANVA/FIGMA | Determine legal supplier, service/software/goods, recipient/use/location and imported-service liability. No automatic federal 18% self-assessment |
| AUDIT/CA FIRM/ACCOUNTING, LAW FIRM/ADVOCATE, CONSULTANT/ENGINEERING | Actual professional-service code/location and possible reduced/input/withholding conditions in services skill |
| SALARY/WAGES/TANKHWAH | Confirm genuine employment and payroll, then outside this sales-tax sale/purchase register; do not exclude contractor services as payroll by label |
| OWNTRANSFER/INTERNAL | Exclude a supported transfer from sales/purchases, reconcile both sides and avoid duplication |
| CASHWITHDRAWAL/ATM | Cash-control movement pending supporting expenditure; neither automatically taxable sale nor deductible input |

Preserve raw statement descriptions, including Urdu, alongside any translation. HBL/UBL/MCBCSV and wallet exports are usable ingestion inputs; detect currency, debit/credit convention, period, opening/closing balance and duplicates before classification. Keep foreign amounts/rates/dates and actual owner-law conversion evidence; do not apply an invented SBPrate or take a net platform receipt as gross export turnover.

## The method, step by step

1. Reconcile each statement to opening/movements/closing, preserving original transaction IDs and documents. Match internal transfers once; isolate taxes, financing, payroll and cash controls from the sales/purchase base.
2. Link sales/purchases to invoices and actual goods/service/location/date. Separate output from input and tax-exclusive value from gross. Mark missing evidence/ambiguous split in a pending register; never invent a higher “safe” rate or country.
3. Run the appropriate owner computation. Federal input needs actual ss.7/8/8 B/73 evidence and restrictions, including business use, matching, banking and statutory exceptions. Provincial input, mixed-use apportionment and cross-credit are authority-specific. Keep denied and unverified credits separately identified.
4. Preserve imports via own-name GD and exports via actual conditions/documents; imported goods and imported services follow different routes. Further tax, extra tax, retail-price/special regimes and sales-tax withholding need actual owner law. Do not conflate export income withholding with goods/services sales tax.
5. Build the `vat-workflow-base` working paper with Pakistan fields: date, source ID, counterparty/rawdescription, direction/currency/gross, net, tax, rate/base, goods/service/code, authority/province, registration/status, document/source, exemption/election reason, business use/admissibility, default/pending flag and reviewer action. Use distinct federal output/input/zero/exempt, each provincial output/input, withholding, brought-forward/next credit and each authority's net payment.
6. Reconcile control totals to documents/owner calculations and actual returns/payments. Do not offset one authority's liability with another's credit. Produce a brief and action list for missing evidence and specialist matters, then route to `pk-return-assembly` if relevant. This workflow does not file or certify a return.

## Two worked examples that recompute

### Earlier domestic goods case retained

The 05 April 2026 DOMESTICBUYER receipt 1,180,000 is assumed supported by an ordinary 18%-tax-inclusive goods invoice, with no further/special tax. This is a conditional owner calculation, not the unknown-rate default.

```oa-check
name: Domestic goods inclusive invoice
inputs:
  gross_receipt: 1180000
steps:
  - net_value: gross_receipt / 1.18
  - output_tax: gross_receipt - net_value
expected:
  net_value: 1000000
  output_tax: 180000
```

### Earlier Sindh service case retained and corrected

The 10 April 2026 CLIENTCOcase previously used 13% and 226,000 gross. For **the same exclusive value 200,000**, assume a supported ordinary 15% Sindh service with no special rate/election; corrected tax 30,000 andgross 230,000 follow. Do not silently treat the old 226,000 payment as 230,000 cash; reconcile actual invoice/receivable or, if price truly inclusive, apply the actual inclusive-price calculation.

```oa-check
name: Sindh ordinary service correction and actual cash reconciliation
inputs:
  exclusive_service_value: 200000
  actual_received_under_old_invoice: 226000
steps:
  - corrected_output_tax: exclusive_service_value * 0.15
  - corrected_gross: exclusive_service_value + corrected_output_tax
  - receivable_difference: corrected_gross - actual_received_under_old_invoice
expected:
  corrected_output_tax: 30000
  corrected_gross: 230000
  receivable_difference: 4000
```

### Other historical cases preserved as their actual evidence gates

The 15 April 2026 USIMPORTERINC 5,000,000 goods export has 0 output **only after actual export/zero-rate conditions**; input/refund is a separate test. The 18 April 2026 GOOGLECLOUD 50,000 payment is an imported-service classification hold; the old 9,000 federal 18% assertion is withdrawn. The 25 April 2026 JAZZCASH 50 fee requires its actual invoice/service/authority classification, not the blanket “financial-serviceexempt” label. None of these transfers creates input credit from bank text alone.

## Deadlines, filing and records

Use each owner skill's actual category/period/calendar and extension evidence. Federal ordinary 15/18 dates have special categories/quarterly branches; provincial periods also vary. Keep authority payment instruction and actual CPR separate from submitted-return acknowledgment. Retain the actual authority's records period, including extended proceedings and historic asset/basis needs; no universal 5 or 6 year rule across all authorities. [STA s.24](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); [Sindh s.27](https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf); owner skills.

## When to refuse or refer

Retain R-PK-1 multi-province service analysis, R-PK-2 SROmanufacturing concessions, R-PK-3 sales-tax withholding agents and R-PK-4 EOUzero-rating. Also hold incomplete documents, mixed goods/service contracts, rate/exemption/export doubts, registration/place disputes, reverse-charge/imported services, partial exemption/blocked input/cross-credit/refunds and notices/audits. Refer with the evidence register and exact unresolved issue; do not remove the transaction or finalise a return on a guessed default.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for federal Act ss.3/4/7/8/8 B/13/14/23/24/73; owner skill retains operative conditions and exceptions | https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf |2026-11-14|
| Read for Sindh Act ss.3/8/9/27 and First Schedule 14/Second Schedule 20; separate services law, not a universal 13% rate | https://www.srb.gos.pk/srb/wp-content/uploads/2026/01/Sindh-Sales-Tax-Act-2011-25-26-2.pdf |2026-11-14|

Not yet confirmed: individual supplier/tax-invoice classifications, actual later 2026 amendments/extension calendars, all provincial input/cross-credit/refund/withholding/marketplace specifics and any special SRO/EOU/extra-tax/POS eligibility. The pattern library is workflow guidance, not legal evidence for a counterparty exemption. No professional approval is claimed.
