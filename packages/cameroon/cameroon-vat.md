---
name: cameroon-vat
description: "Cameroon VAT (TVA) for 2026: real-regime scope, standard and social-housing rates with CAC, inputs, foreign services, electronic invoices, monthly returns and export/credit conditions from the official CGI."
version: 2.1
jurisdiction: CM
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Cameroon VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year 2026. The previous file attributed a 2026-06-21 review to **Nkinyam Courage Ndasi**. That historical credit is preserved; it does not attest this rewrite, which has not been reviewed by an accountant. The original identifier 3472800 is retained solely as an unverified historical identifier, not a current credential or approval.

## Who this applies to

Businesses making taxable independent economic supplies in Cameroon, imports, and customers/platforms dealing with foreign services. Establish actual VAT status, regime, supply, place and documents before computing. A bank statement from Afriland First Bank, BICEC, Societe Generale Cameroun, Ecobank Cameroun, UBA Cameroun or another bank is a starting record, not enough to substantiate input deduction.

Free-zone businesses are expressly within CGI 127(8); never assume a Douala Free Zone exemption. **R-CM-1:** refer the specific approved convention/decree and transition terms. **R-CM-2:** oil, gas and mining conventions require sector review. Existing establishment conventions can continue under 153; do not extrapolate them to another taxpayer.

Historical contributor credit: Open Accounting Skills Registry. This preserves the prior registry credit; it does not attribute this rewrite or its attestation to that registry.

## Rates, bands and thresholds

| Item | Rule / amount in XAF unless stated | Official source |
|---|---|---|
| Standard TVA | 17.5%; CAC 10% of TVA gives derived total 19.25%, not 27.5%. | CGI 142(1)-(3); C83(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Reduced rate | 10% TVA; derived 11% with CAC. Applies to INTEREST remunerating real-estate loans to natural persons acquiring their first social home, with tax quitus; first-social-home sales to natural persons with quitus; and social-housing rentals by public/parapublic promoters. Loan principal is not interest. | CGI 142(4); C83(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Zero rate | 0% for exports of taxable products. International transport and diplomatic transactions require their own exemption/territorial conditions; they are not blanket zero-rated. | CGI 142(5);128(2),(16);129(3): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Ordinary VAT regime | Real regime only. Annual turnover excluding tax at least 50,000,000 for ordinary businesses or 30,000,000 for liberal professions; compulsory real-regime categories and express derogations also apply. | CGI 132;93 quater: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Regime exceptions | Petroleum, mining, gas, credit, microfinance, insurance and mobile-phone new taxpayers; listed specifically approved businesses, notaries and express DGI derogations can be real-regime regardless of turnover. Falling below thresholds retains initial regime for 2 years. | CGI 93 quater(2)b;93 quinquies: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Household water/electricity | Exempt household consumption not exceeding 20 m 3 water/month or 220 kw electricity/month, as printed. Do not infer exemption from supplier name alone. | CGI 128(9): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| VAT base rounding | Round the taxable base down to the nearest 1,000. | CGI 141: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Cash-paid input | For a taxable operation valued at least 100,000, input deduction requires noncash payment. Refund/offset claims cannot be based on cash-paid invoices. | CGI 143(1)d;149(4): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Input claim limit | Exercise deduction by the end of the 2nd tax year after VAT became chargeable; supplier chargeability and valid documents remain required. | CGI 143(1)c,(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Partial exemption | Eligible taxable receipts/all receipts, including taxable exports and specified CEMAC-transit/diplomatic/convention adjustments. Provisional ratio:previous-year receipts/products; new taxpayer:current-year forecasts. Existing businesses justify prior final ratio; new businesses supply forecast accounts. Verification and a ratio declaration are required. Final ratio and true-up by 31 March; below 10% no deduction. | CGI 147, with 148 separate-sector condition: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Capital adjustment | Nontaxable disposal before the end of the 4th year: repay deduction less 1/5 per year or fraction since acquisition. Full repayment for noncapital items diverted to nontaxable use or relevant fraud. | CGI 145: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Foreign service declaration | Declare the contract and accredited responsible representative within 15 working days of concluding the verbal/written convention. Without the declaration, customer is jointly liable for VAT eventually due. | CGI 151: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Monthly return | Real regime: return and payment within the first 15 days of the following month; file NEANT when no taxable operations. The old simplified quarterly VAT route is not current ordinary guidance. | CGI 149(1);152(2)-(5): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Late self-assessed declaration/payment | 10% per month, maximum 30% of principal, plus late-payment interest 1.5% per month under L106. Do not apply the separate assessment-interest 50% cap automatically to collection interest. | LPF L106(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Understatement | Assessment interest 1.5%/month capped 50%; additional 30% good faith,100% bad faith,150% fraud. L96(2) separately gives 15% principle penalty on accepted audit assessments paid spontaneously; this 15% cannot subsequently be remitted or transacted. | LPF L95-L98, especially L96(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| No return after notice | Assessment plus 100%, or 150% repeat; separate office-based fines apply. Default assessment can forfeit input VAT and prior-period credit. | LPF L97; L103: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Registration failure | Failure to request registration or changes within legal time: 250,000 fine; this is not the old blanket penalty of 100% of tax due. | LPF L100(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Missing NIU | Missing NIU on an invoice denies deduction. False/incomplete invoices also attract separate penalties; an invoice alone is not proof of a taxable business purchase. | LPF L101-L102; CGI 150: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |


## The base

### Supply, timing and tax-inclusive amounts

CGI 125-127 cover paid economic activities: goods, services, self-supplies, imports, immovable operations, leasing, commercial subsidies and e-commerce. Goods normally trigger on delivery; advances become chargeable on receipt to their extent. Services, works and social-housing operations are chargeable on receipts/advances; specific property, lease and import events differ (133-134). All invoiced TVA must be remitted. Do not substitute a bank date for the statutory event.

The domestic base is the consideration including incidental charges and taxes other than TVA, so excise is included (135-136). Invoice discounts, exact disbursements, commercial promotional gifts and non-consideration receipts have the specific 137 exclusions. Imported goods use customs value plus customs duty and excise, with the stated CEMAC origin rule (138). Apply 141 rounding to the actual base. For an amount already including standard TVA and CAC, divide by 1.1925 only after confirming the rate and tax-inclusive invoice; the factor is derived from 142/C83.

### Exempt versus zero-rated

Use the exact 128 category and tariff description. Its families include listed necessities/agricultural inputs and producers' direct sales, authorised education fees/boarding, medical care and listed pharmaceutical products/equipment, specified nonprofessional property transfers subject to registration, life-insurance savings contracts, specified low-value microfinance interest, international traffic and diplomatic official use under reciprocity/headquarters agreements and quotas. Food/product exclusions and tariff lists matter. Household utility limits are above. Petroleum sales are expressly taxable under 127(9), subject to the narrow aviation-fuel exemption in 128(8). Do not label all petroleum, bank services, residential rents, medicines or agricultural purchases exempt from a broad name. Furnished/professional property letting is expressly within 127(5); establish whether a particular nonprofessional transaction meets 128(1).

A taxable export is zero-rated with input rights. An exempt domestic transaction generally does not carry those rights; special 147 adjustments must be identified. International navigation/maintenance/provisioning and CEMAC transit have specific 128(2) rules, not a universal zero rate. Diplomatic supplies follow 128(16), not automatic zero-rating.

### Deduction, documents, blocked costs and bad debts

For a registered real-regime taxpayer,143 requires eligible production/business use, supplier chargeability and prescribed support. A local invoice must use DGI's electronic invoicing tracking system, an active registered real-regime supplier and NIU. Foreign suppliers are expressly excepted from those local supplier conditions, not from proof of the transaction. Imports use the actual consumption declaration (D3, D43 or T6 bis); self-supplies use the special declaration; withholding requires an attestation generated by the tax system. Retain proof of actual export and upstream VAT remittance for export credit. Test noncash payment and claim time separately.

143(3)d excludes passenger vehicles, their spares and repairs;144 blocks accommodation, meals, reception, entertainment, passenger-vehicle hire/transport, goods/services used by third parties/directors/staff, and services related to excluded assets. The tourism/restaurant/entertainment/motor-dealer exception is limited to their own taxable professional activity. Nonused goods re-exported unchanged are also blocked. The old universal “fewer than 9 seats unless taxi” test and an automatic fuel-for-blocked-vehicles rule have not been established from this current text; hold that precise test while applying the actual passenger-vehicle and related-service exclusions. Personal use never supports a business input claim.

Treat TVA and its CAC consistently because C83 makes CAC follow the principal; do not recover the CAC of a blocked input while disallowing its TVA. CGI 147 governs partial deduction, with verification and annual true-up;148 permits separate sectors only with separate accounts. The old generic “DGI approval under 143” is not a substitute for these conditions.

Under 146, cancelled/rescinded sales require a replacement invoice to be established AND sent to the customer. For a genuinely and definitively irrecoverable debt, send the prescribed duplicate showing the unpaid net price and related TVA. The text does not impose the old universal court-judgment condition. Keep evidence of final irrecoverability; ageing alone is insufficient.

### Statement patterns and working paper

Treat AFRILAND FIRST BANK/AFRILAND, BICEC, SGC/SOCIETE GENERALE CAMEROUN, ECOBANK CAMEROUN and UBA CAMEROUN as counterparties to investigate, not evidence all fees are exempt. INTEREST/LOAN may identify interest or principal; separate each from taxable fees. DGI/DIRECTION GENERALE DES IMPOTS and CNPS suggest statutory payments; reconcile to returns before posting. DOUANE/CUSTOMS requires the customs document separating duty, excise and import TVA/CAC.

ENEO/SONATREL and CAMWATER/CDE require invoice/use/consumption checks; household exemptions differ from business supply. MTN CAMEROUN/ORANGE CAMEROUN require actual telecom invoices. GOOGLE/MICROSOFT/AWS and ZOOM/SLACK/NOTION require supplier/platform registration, representative and Cameroon-use checks. None authorises automatic input recovery or a duplicate customer charge where the supplier/platform already lawfully collected tax. Original EC1 concerned a US SaaS supplier. Check Cameroon use/place, representative/platform/supplier collection and actual customer liability. Net zero requires a real charge plus full input eligibility and documents; blocked use or an already lawfully collected supplier/platform charge changes the answer.

Maintain output taxable/exempt/zero-rated bases, principal TVA and CAC, customer-accounted foreign tax, adjustments and total output; eligible local/import/capital/foreign-service inputs, blocked amounts, pro rata, withholding attestations, credit carried in and net payable/credit. Reconcile both tax components. The old A1-A10, B1-B8 and C1-C3 labels are retained only as unconfirmed legacy worksheet labels under Sources; do not map them into a live form. Never file without checking credit reporte.

## Deadlines and filing

Use the actual DGI administration-provided return and current taxpayer account.152 requires signature by taxpayer or duly mandated fiscal representative, filing at the competent centre (DGE for large enterprises) and matching payment. Portal flow and the old fiscalis.minfi.cm link were not verified; do not invent screens or boxes.

149(2) requires VAT withholding by listed public/private/nonprofit entities at payment, including specified public suppliers irrespective of their regime; use an actual listing and system attestation. Certain structural-credit businesses can be dispensed by the Minister. Carry-forward under 149(3) is normally without time limit; ordinary-trade credit beyond 3 months requires prior validation. Refund/offset is an application with separate eligibility, no outstanding compensable tax and supporting certificates; exporters have a 2-month statutory processing route with customs/actual-export/repatriation proof and a limit tied to exports. Do not turn a credit into an automatic cash refund. Other 149/149 bis/149 ter categories and risk controls need a separate claim review.

## Penalties and interest

Use the dated breach, principal, notice and return before applying the table. L106 starts collection interest according to its notice/filing/due-date rules, not a universal 30-day grace period. L95-L98 assessment interest differs. Do not state that every late return gets a flat 30% or every registration failure 100%. L103 default-assessment input/credit forfeiture is separate. Refer contested arrears and refund penalties; a bank statement does not establish the enforcement balance.

## Cross-border points

129 places goods delivered in Cameroon and services/rights/rentals used there in scope;130/130 bis distinguish locally situated and intangible services. A foreign enterprise needs an accredited solvent Cameroon representative; if none is designated the customer pays on its account under 130(2).149 quater separately makes e-commerce platform operators collect, declare and remit supply tax and their commission tax, with registration and possible access suspension. Confirm the responsible party before customer accounting and before input deduction. There is no automatic “foreign SaaS means net zero”.

A Gabon/CEMAC goods movement still needs the Cameroon customs treatment; do not use an EU-style acquisition mechanism. Timber/cocoa exports require taxable-product status and actual export proof. Free-zone, oil/gas/mining, diplomatic and specific international-transport cases require the exact governing instrument.

## Two worked examples that recompute

### Standard sale and eligible purchase

A standard domestic taxable sale has a base of 1,000,000: TVA175,000 plus CAC17,500, total 192,500 and invoice 1,192,500. At 10,000,000 the corresponding tax is 1,925,000. For a fully eligible, documented noncash purchase of 5,000,000, the corresponding input 875,000 plus 87,500 is 962,500. These are derived computations from 142/C83; deduction remains conditional on 143-144.

```oa-check
name: Standard sale and fully eligible local purchase
inputs:
  sale: 1000000
  purchase: 5000000
steps:
  - sale_tva: sale * 0.175
  - sale_cac: sale_tva * 0.10
  - sale_tax: sale_tva + sale_cac
  - invoice: sale + sale_tax
  - input_tva: purchase * 0.175
  - input_cac: input_tva * 0.10
  - input_total: input_tva + input_cac
expected:
  sale_tva: 175000
  sale_cac: 17500
  sale_tax: 192500
  invoice: 1192500
  input_total: 962500
```

### Foreign IT service: full eligibility versus blocked use

French IT services used in Cameroon cost 8,000,000. Assume no local representative/platform collection, customer liability actually applies, and the invoice/payment meets all current requirements. TVA1,400,000 plus CAC140,000 is 1,540,000. Full taxable business use and documentary eligibility permit the same input, giving net 0. If instead the entire service serves a blocked/nonbusiness purpose, input is 0 and net liability 1,540,000. Do not infer these facts from a GOOGLE/ZOOM debit.

```oa-check
name: Foreign IT service, eligible versus blocked input
inputs:
  service: 8000000
steps:
  - tva: service * 0.175
  - cac: tva * 0.10
  - output: tva + cac
  - eligible_input: output
  - eligible_net: output - eligible_input
  - blocked_input: 0
  - blocked_net: output - blocked_input
expected:
  tva: 1400000
  cac: 140000
  eligible_net: 0
  blocked_net: 1540000
```

Further old regressions retained: cocoa exports 200,000,000 have output 0 only where 142(5) and actual-export conditions hold; input recovery requires 143. Entertainment 3,000,000 with TVA525,000 and CAC52,500 has blocked tax 577,500 and cost 3,577,500 unless the actual professional exception applies. A blocked motor vehicle blocks its related TVA/CAC. Excise enters the VAT base; a CEMAC import uses customs documentation. These are scenario inputs and derived arithmetic, not additional exemption rules.

## Ask the client first

1. Tax year, VAT registration/real regime, annual turnover excluding tax and actual activity?
2. Goods or service, customer/supplier location, Cameroon use, foreign representative/platform collection and tax point?
3. Valid invoice/NIU/e-invoice or customs/withholding document, payment method and business use?
4. Exempt/zero-rated category, tariff item, export proof or special convention?
5. Opening credit, blocked costs, pro rata and any default-assessment/arrears notice?

Refuse a definitive return from bank descriptions alone. Escalate the free-zone/sector conventions above and any unidentified foreign collector. Provide the workpaper, assumptions and **REVIEWER FLAG / ESCALATION REQUIRED** items for a qualified practitioner; do not file or sign. Computations must recompute through the deterministic engine and be reviewed. Direct tax, PAYE and CNPS remain separate jobs: use their sibling skills rather than the old blanket 33% company-tax or payroll-rate shortcut.

## Sources

| Official source | URL | Read on / scope |
|---|---|---|
| DGI CGI Edition 2026 | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-15. Read for 125-153 including taxable events,128 exemptions and neighboring exceptions,130/130 bis foreign services,132 real-regime restriction,141-149 quater rate/input/credit/platform conditions,150-152 invoices and filing;93 quater/quinquies regime; C83 CAC; LPF L95-L106 including penalties/NIU/default-assessment. Whole AnnexI product list, detailed refund procedures and actual portal not read. |

Not yet confirmed: exact current DGI return fields and portal screens; old output A1-A10 (sales/exempt/export/total/TVA/CAC/foreign TVA/CAC/adjustments/output), input B1-B8 (local TVA/CAC/import TVA/CAC/capital/foreign/blocked/total) and net C1-C3 (output less input/opening credit/payable) box identities; the legacy fewer-than 9-seats/taxi test and precise related fuel exclusion; particular Douala Free Zone or oil/gas/mining conventions; actual platform/customer collection and deduction facts for a named SaaS provider; tariff-level exemption treatment beyond the paragraphs actually read. These remain outside usable filing instructions. The old 100,000,000 real/50,000,000-100,000,000 simplified VAT thresholds, quarterly ordinary VAT filing, blanket international-transport/diplomatic zero rate, bank-fee/petroleum exemptions and court-judgment-only bad-debt rule are superseded by the specific 2026 provisions above.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
