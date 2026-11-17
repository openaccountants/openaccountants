---
name: gi-einvoice
description: "Gibraltar invoicing reference for companies and suppliers performing covered public procurement contracts. Explains the structured electronic invoice definition, public authority receipt and processing duty, core data elements and company-name disclosure. Provides an invoice reconciliation example and a workflow for confirming contract scope, syntax and delivery evidence. Based on primary legislation checked in October 2026. General business-to-business issuance mandates, current procurement eligibility, technical standard versions, buyer endpoints, transaction-specific retention periods and professional review remain unresolved. This source-cited draft does not certify a software format or establish that every Gibraltar invoice must be electronic."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/gi-einvoice"
  jurisdiction: "GI"
  tax_year: "2026"
  last_updated: "2026-11-15"
---

# Gibraltar: invoices and public procurement e-invoicing

## Who this applies to

Use this skill for Gibraltar company invoice identification, covered public procurement electronic invoices and the evidence needed to keep electronic invoice records. The operative source scopes below were read on 15 November 2026. This source-cited draft does not establish a universal private B2B/B2C electronic-issuance obligation or exemption, certify a software format, or prove a buyer endpoint works.

Before applying a rule, identify the supplier, buyer, actual award regime and contract, security classification, applicable semantic/syntax profile and actual transaction tax treatment. The [facts to obtain](#ask-the-client-first) also include delivery evidence, payments, record periods and holds.

The Procurement (Electronic Invoicing) Regulations 2018 cover electronic invoices arising from an economic operator's performance of goods, works or services contracts awarded under or pursuant to the defence/security 2012, public-sector 2016, concession 2016 or utilities 2016 procurement regulations. Record the actual award and regime; a public-sector customer's name alone does not decide coverage. For covered contracts the authority must be equipped to receive and process invoices securely, while the submitted invoice must satisfy the semantic, syntax and minimum-information requirements. These are procurement-specific rules, not authority for a universal private-business mandate. [EI regulations 2–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

| Situation | Rule and boundary | Official source |
|---|---|---|
| Covered procurement performance | Apply the actual award regime and invoice requirements; do not substitute foreign procurement thresholds | [EI 2–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Secret/security-sensitive defence contract | Excluded only where procurement/performance are declared secret or require special security measures and the essential interests cannot be guaranteed by less intrusive measures | [EI 3(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Public-sector or concession economic operator | Current definitions cover market-offering natural/legal persons, public entities and groups, including temporary associations; separate old contractor nationality wording is not a blanket exclusion | [Public-sector 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s084/2016s084(15-01-26).pdf); [Concession 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s086/2016s086(15-10-26).pdf) |
| Utilities economic operator | Current definition covers persons, utilities and qualifying combinations/groups offering works, products or services | [Utilities 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s085/2016s085(15-01-26).pdf) |
| Defence supplier eligibility | The current defence definition still cross-refers to contractor/supplier/services-provider definitions containing Member State nationality/establishment conditions. Actual EU-exit/treaty entitlement for the supplier is held for confirmation | [Defence 2–5](https://gibraltarlaws.gov.gi/uploads/legislations/public-finance/2012s088/2012s088(29-06-17).pdf); [EI 2](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Other private B2B/B2C invoice | These procurement provisions establish neither a general mandate nor a general exemption; company identification and record duties must still be considered | [EI 3–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf); [Companies 179](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf) |

The live e-invoice index still selects the 20 December 2018 instrument. Current procurement sources must be checked separately: the public-sector and utilities texts select 15 January 2026, while the concession text includes the 15 October 2026 amendment on negotiated procedures, duration and savings. Do not infer eligibility from the age of the e-invoice instrument, a stale search result or another country's thresholds. This skill does not decide procurement award legality or remedies. [Current EI index](https://www.gibraltarlaws.gov.gi/legislations/procurement-electronic-invoicing-regulations-2018-4469); [concession amendment, regulations 1–4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s086/2026=357.pdf).

## Rates, bands and thresholds

These are format, record and sanction controls, not a VAT rate card. The original invoice example's zero tax is an independently established assumption for that invoice.

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| Minimum core information | 13 groups, subject to the semantic/syntax requirements and applicable conditional fields | [EI 4–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Dated OJ semantic baseline | EN 16931-1:2017 and CEN/TS 16931-2:2017 published by Decision 2017/1870; this alone does not establish Gibraltar's local 2026 migration profile | [Decision article 1 and annex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017D1870) |
| Dated syntax/binding baseline | UBL 2.1 invoice/credit-note messages, ISO/IEC 19845:2015, binding CEN/TS 16931-3-2:2017; CII D16B, binding CEN/TS 16931-3-3:2017 | [Decision annex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017D1870); [Commission syntax and binding sections](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108934/Required%2Bsyntaxes) |
| Semantic migration | EN 16931-1:2026 published in May 2026; 2017 edition withdrawn but remains compliant during migration according to the June 2026 notice. No Gibraltar cutover is established here | [Commission migration notice](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108661/European%2BStandard%2Band%2BSpecifications) |
| Company books | 5 years under section 239, subject to section 243; retain proper books of money, purchases/sales and assets/liabilities. This is not an invoice-date tax-destruction rule | [Companies 239](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf) |
| Tax-return records | 6 years from the end of the return period under sections 28/29, with section 63 notice/enquiry extensions; significant invoices and supporting documents included | [Income Tax 63](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |
| Company-name omission | Level 2 offence for company under 179(3) and issuing/authorising officer under 179(4), subject to the actual statutory conditions; cash equivalent not established here | [Companies 179(1)(b), (3)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf) |
| Failure to keep tax records | Penalty not exceeding level 5 on the standard scale; appeal to Magistrates' Court. Recordkeeping penalty, not an invented e-invoice late-filing charge | [Income Tax 63A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf) |

## The base

### Identify a compliant structured invoice

An electronic invoice must be issued, transmitted and received in a structured format capable of automatic electronic processing. A scanned image or ordinary unstructured PDF alone does not demonstrate that requirement. Apply the semantic data-model standard, minimum core information and a compliant syntax on the Official Journal list together. A filename, readable rendering or correct total alone proves none of the other tests. [EI 2 and 5(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

The dated OJ decision lists CII XML Schemas 16B and UBL invoice/credit-note messages under ISO/IEC 19845:2015. The Commission's February 2026 page identifies UBL 2.1 and the corresponding 2017 syntax bindings. Binding is version-specific: a newer XML version is not automatically compliant. Validation artifacts have their own release cycle; selecting a syntax does not establish that an instance passes the applicable business rules. [OJ annex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017D1870); [Commission syntax, version and validation sections](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108934/Required%2Bsyntaxes).

The Commission's June 2026 page says the new semantic edition was published in May, the old edition was formally withdrawn, and the old edition remains compliant during migration. The page is under review and directs users to the relevant authority. It gives no Gibraltar cutover date. Keep semantic edition, syntax/version, binding, validation-artifact release, buyer profile and delivery route as separate implementation fields. Obtain the applicable local arrangements before choosing the 2026 edition or rejecting a 2017 invoice. These are recommended controls; neither Commission page certifies a Gibraltar endpoint, replacement local transition instrument or live submission. [Migration notice](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108661/European%2BStandard%2Band%2BSpecifications); [EI 5(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

### Keep all core information and the correct company identification

Regulation 4 has 13 core groups. The following retains the grouped working-paper mapping; the right column is recommended evidence, not a complete technical schema. [EI 4–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

| Core groups | Working-paper evidence | Official source |
|---|---|---|
| Process/invoice identifiers; invoice period | Invoice/process references and relevant dates/period | [EI 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Economic operator; buyer; payee; tax representative | Applicable party details and profile treatment for absent parties | [EI 4–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Contract references; delivery details | Award/order reference and performance/delivery records | [EI 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Payment instructions | Agreed method, account and terms | [EI 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Allowances/charges; invoice line items | Quantities, prices, adjustments and descriptions, reconciled once | [EI 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |
| Invoice totals; VAT breakdown if applicable | Arithmetic reconciliation and independently established tax treatment | [EI 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf) |

Determine mandatory and conditional fields under the applicable standard/profile. Do not invent a tax representative or tax charge to fill an absent-party field. The conditional VAT-breakdown reference is not authority to charge Gibraltar VAT; cross-border tax fields require the actual tax analysis. [EI 4–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

A company must show its name legibly on its invoices. Companies section 180 separately addresses business letters, order forms and website homepages, including registration and other particulars. Do not transpose every section 180 field into an invoice requirement solely from that provision; procurement, contract or other law may add information. [Companies 179–180](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf).

### Distinguish electronic originals, production and retention

The Electronic Commerce Act applies separate tests to original-document requirements, producing a document and retaining records. Meeting one does not establish the others. [Sections 19–22](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

| Requirement | Conditions and exceptions | Official source |
|---|---|---|
| Original-document requirement, section 19 | Reliable integrity assurance from final-form generation; where presentation is required, legible display to the recipient | [19(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf) |
| Paper/tangible document produced electronically, section 20 | Reliable generation method protecting integrity and reasonable expectation of ready future access at creation; recipient consent **or** legible production to the recipient | [20(1)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf) |
| Electronic retention, section 21 | Accessible for later reference; original generated/sent/received format or demonstrably accurate representation; retain origin, destination and sending/receipt date/time information | [21(1)–(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf) |
| Transmission-only information | Narrow exclusion for information whose sole purpose is enabling transmission; does not remove the origin/destination/timestamp condition | [21(3), read with 21(2)(c)](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf) |
| Third-party storage | Permitted if the retention conditions are met; successful upload alone does not demonstrate them | [21(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf) |

For sections 19–20, integrity means completeness and absence of alteration, allowing endorsements and normal communication, storage or display changes. Reliability depends on the purpose and all relevant circumstances. Consent is not the only electronic-production route under section 20. These form/evidence conditions set neither a universal retention duration nor automatic permission to destroy paper. Sections 11–18 are repealed in the current consolidation; specific signature and trust-service requirements remain held. [Sections 19–21 and repealed Part II](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

Electronic form alone is not a ground for excluding a document from evidence. A non-original also receives protection where it is the best evidence reasonably obtainable by the person adducing it. Weight still depends on generation/storage/communication reliability, integrity and originator identification. Admissibility or a hash does not prove the underlying invoice correct or identify its sender by itself. [Section 22](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

## Deadlines and filing

The cited procurement invoice regulations do not supply a universal invoice-issue deadline, payment period, filing portal, box number or buyer endpoint. Do not invent one. Use the actual contract and buyer-confirmed profile; hold implementation where those are missing. This workflow records recommended controls alongside the statutory scope/format duties. [EI 3–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

1. Confirm the buyer, actual award regime and contract, supplier status and any security exclusion.
2. Obtain the buyer's supported delivery route and applicable semantic edition, syntax/version and profile. Record who confirmed them and when.
3. Map required fields to approved party, contract, delivery and accounting records. Check the company name.
4. Recompute line extensions, allowances/charges, tax and payable amount. Establish tax treatment independently; do not deduct an allowance twice.
5. Validate the structured file against the actual required schema and business rules. Retain validation results and a separate readable rendering.
6. Submit by the confirmed route and retain receipt/rejection evidence. File generation alone proves neither receipt, acceptance nor payment.

Steps 2–6 are recommended implementation controls. No live buyer endpoint or test invoice has been exercised for this version. Preserve any rejection and correction history; the legal credit-note/correction profile remains a boundary until confirmed. [EI 5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf); [Electronic Commerce 21–22](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

### Apply the actual record period and any hold

Company books and tax-return records have different rules. Section 239 requires company books for 5 years, subject to section 243, at the registered office or another place the directors choose and available to directors. Tax section 63 applies to persons required to deliver section 28/29 returns: preserve necessary records for 6 years from the end of the return period. A notice before that period expires can extend retention until the enquiry ends or enquiry power ends; a later notice also preserves relevant records still held until that point. Required records include significant invoices/contracts and their supporting documents; books must be in English. Do not use the shorter company period or an invoice's own date to erase tax-required evidence. [Companies 239](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf); [Income Tax 63(1)–(8)](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

The [bookkeeping skill](gi-bookkeeping-and-tax-records.md) owns the full recordkeeping workflow. Confirm applicable enquiry/litigation and other transaction holds before deletion. Electronic form, access and metadata requirements continue throughout the actual required period. [Electronic Commerce 19–21](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

## Penalties and interest

The linked rates table distinguishes company-name offences at level 2 from the tax-record failure cap at level 5. Company section 179(4) concerns the director, manager, officer or person issuing/authorising the document; its separate personal liability relates to the stated money instruments and is not a blanket personal debt for every invoice. Tax-record penalties have the section 63A appeal route. No cash standard-scale conversion, e-invoice-specific late-submission fine, automatic payment surcharge or interest rate is established for this job. Hold those amounts rather than import a tax-return sanction. [Companies 179(3)–(4)](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf); [Income Tax 63A](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf).

Retain production, delivery, validation and retrieval evidence: admissibility is different from evidential weight and transaction truth. A storage-provider success message, readable PDF or matching arithmetic alone cannot discharge every statutory condition. [Electronic Commerce 19–22](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

## Cross-border points

Procurement coverage depends on the actual regime and award. The broad current public-sector/concession/utilities economic-operator definitions do not resolve the separate defence wording or a particular supplier's entitlement under EU-exit/treaty measures. Do not substitute another jurisdiction's threshold or eligibility rule. The OJ/Commission standards baseline does not supply Gibraltar's local migration date, buyer endpoint or cross-border tax treatment. [EI 2–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf); [public-sector 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s084/2016s084(15-01-26).pdf); [concession 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s086/2016s086(15-10-26).pdf); [utilities 4](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s085/2016s085(15-01-26).pdf); [defence 2–5](https://gibraltarlaws.gov.gi/uploads/legislations/public-finance/2012s088/2012s088(29-06-17).pdf).

Invoice senders and recipients must observe applicable personal-data law and keep invoice use to the intended or compatible purposes. The Data Protection Act 2004 remains operative and supplements the Gibraltar GDPR; its old title does not mean it has been repealed or supplies the whole framework alone. The current local texts select 15 July 2026. The 2026 amending instrument addresses transfer/adequacy provisions and commences on the Treaty Implementation Date; this skill does not independently certify that date from a standalone commencement notice. [EI 6](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf); [DPA 3/6](https://www.gibraltarlaws.gov.gi/uploads/legislations/data-protection/2004-01/2004-01(15-07-26).pdf); [2026/096, regulations 2/4/5](https://www.gibraltarlaws.gov.gi/uploads/legislations/data-protection/2004-01/2026=096.pdf).

For actual personal-data processing, determine material/territorial scope and a lawful basis. Gibraltar-establishment processing can be covered even where processing occurs elsewhere; some non-established targeting/monitoring is covered too. Contract, legal obligation, public task and legitimate interests are conditional bases; consent is not universally required, and public-authority tasks cannot use the legitimate-interest basis. Minimise data, apply purpose/accuracy/storage limits and accountability, and implement security appropriate to risk, including recovery and testing. Reconcile legal retention and claim holds with privacy, rather than erase evidence mechanically or keep it indefinitely. The precise third-country transfer route and any special-category data require transaction-specific review. [Gibraltar GDPR 2–6 and 32](https://www.gibraltarlaws.gov.gi/legislations/regulation-eu-2016679-5582); [DPA 3/6](https://www.gibraltarlaws.gov.gi/uploads/legislations/data-protection/2004-01/2004-01(15-07-26).pdf).

## Two worked examples that recompute

### Original GBP invoice reconciliation, preserved in full

Assume a contract priced in GBP, with 10 units at £80 and 3 units at £50, a £50 agreed invoice allowance and a £20 agreed charge. Assume independently confirmed zero tax due on this particular invoice; this is not a country-wide exemption conclusion.

- Line totals: 10 × £80 = £800; 3 × £50 = £150.
- Before adjustments: £800 + £150 = £950.
- Adjusted total: £950 − £50 + £20 = **£920**.
- With £200 already paid, remaining payable: £920 − £200 = **£720**.

Check that the allowance is not deducted both on a line and again at invoice level. If duplicated, the payable amount would be incorrectly reduced to £670. Matching arithmetic alone does not prove syntax compliance or correct tax treatment.

The following block recomputes every original amount, including the wrong duplicate-allowance result. Inputs are hypothetical record facts; outputs are derived arithmetic, not tax rates or statutory thresholds.

```oa-check
name: Original GBP invoice and duplicate-allowance control
inputs:
  quantity_a: 10
  price_a: 80
  quantity_b: 3
  price_b: 50
  allowance: 50
  charge: 20
  independently_confirmed_tax: 0
  already_paid: 200
steps:
  - line_a: quantity_a * price_a
  - line_b: quantity_b * price_b
  - subtotal: line_a + line_b
  - invoice_total: subtotal - allowance + charge + independently_confirmed_tax
  - payable: invoice_total - already_paid
  - incorrect_duplicate_payable: payable - allowance
  - duplicate_error: payable - incorrect_duplicate_payable
expected:
  line_a: 800
  line_b: 150
  subtotal: 950
  invoice_total: 920
  payable: 720
  incorrect_duplicate_payable: 670
  duplicate_error: 50
```

### Decision: remaining payment or overpayment credit

Keep the same independently established £920 invoice. Compare the original £200 received with a hypothetical £1,000 received. The first leaves £720 to collect; the second leaves no further amount to collect and an £80 overpayment credit in the working paper. Forcing the second branch into a request for another positive payment would be wrong. This is a payment-reconciliation decision, not authority to issue a negative XML payable or a particular legal credit note: the buyer's correction/credit-note profile remains held. All amounts are hypothetical inputs or derived outputs, with no country-wide tax-exemption conclusion.

```oa-check
name: GBP payment reconciliation branches
inputs:
  established_invoice_total: 920
  original_payment: 200
  overpayment_received: 1000
steps:
  - original_balance: established_invoice_total - original_payment
  - original_to_collect: max(original_balance, 0)
  - original_credit: max(-original_balance, 0)
  - second_balance: established_invoice_total - overpayment_received
  - second_to_collect: max(second_balance, 0)
  - second_credit: max(-second_balance, 0)
expected:
  original_balance: 720
  original_to_collect: 720
  original_credit: 0
  second_balance: -80
  second_to_collect: 0
  second_credit: 80
```

### Original record-retention control example, preserved in full

Suppose the supplier keeps a readable invoice image but discards the source file and all evidence of where and when it was sent. Readability alone does not demonstrate section 21 compliance: the retained format must accurately represent the information and the required origin/destination/timestamp information must remain available. A storage provider's successful upload message alone establishes neither condition.

As recommended controls, retain the structured invoice, a readable rendering, delivery metadata and validation results; test retrieval after migration and retain evidence of any conversion's accuracy. These are implementation controls, not statutory requirements to use a particular software product, hash algorithm or file extension. A hash can support integrity checking but does not by itself prove that the original invoice was correct or identify its sender.

## Ask the client first

- Identify supplier entity/status and buyer; provide the actual procurement contract, award regime and any security classification.
- Provide the buyer-confirmed semantic edition, syntax/version, binding, validation profile and delivery route, with dated confirmation.
- Supply approved party/contract/delivery records and the independently established transaction tax treatment, including any cross-border facts.
- Supply quantities/prices, agreed allowances/charges, prior payments and correction history so the invoice and payment branches can be reconciled.
- Identify the company/tax return periods, record location, accessible formats, origin/destination/timestamps, enquiry/litigation holds and any storage provider.
- Identify personal data, purposes, lawful basis, recipients/hosting/transfers and who will review the actual transaction and technical output.

### Completion checklist and refusal boundaries

Confirm actual contract coverage/security/supplier status; full core/profile mapping and company name; independently established tax; recomputed totals and payments; actual schema/business-rule validation; retained readable/structured/delivery evidence; retrievability and conversion accuracy; applicable record periods/holds and privacy. Stop implementation where a required eligibility, migration, buyer route, correction, signature, tax or transfer fact is missing. Do not certify an untested endpoint or use a zero-tax fixture as an exemption rule. Independent source review and professional attestation are separate from writer research.

### Disclaimer

Source-cited draft, not professionally attested. A qualified reviewer must check the transaction, current law and technical requirements before the invoice is submitted or relied upon.

## Sources

| Source and actual read scope | Official URL | Read on |
|---|---|---|
| Procurement (Electronic Invoicing) Regulations 2018: Read for the entire five-page instrument, regulations 1–6 and all definitions/operative neighbors; current index selects 20 December 2018. | https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf | 2026-11-15 |
| Electronic Commerce Act 2001: Read for the amendment table, arrangement, full sections 19–22, repealed 10A/11–18 and section 23 opening neighbors; consolidation 1 January 2021. | https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf | 2026-11-15 |
| Companies Act 2014: Read for full sections 179–180 with 178 ending/181 opening, and full 239 with 237A/238/240 opening neighbors; consolidation 1 August 2025. | https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf | 2026-11-15 |
| Income Tax Act 2010: Read for full sections 63/63A with 62 ending/64 opening, including record scope and notice/enquiry extensions; consolidation 23 March 2026. | https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/2010-21/2010-21(23-03-26).pdf | 2026-11-15 |
| European Commission, Required syntaxes: Read for all substantive syntax/list/binding/version/code-list/validation sections; updated 2 February 2026. | https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108934/Required%2Bsyntaxes | 2026-11-15 |
| European Commission, European Standard and Specifications: Read for the full substantive migration notice, standards table and under-review notice; updated 24 June 2026. | https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108661/European%2BStandard%2Band%2BSpecifications | 2026-11-15 |
| Public-sector procurement: Read for the amendment table, definition context and full regulations 3–4 with 5/A6 neighbors; consolidation 15 January 2026. Full threshold rules are outside this read scope. | https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s084/2016s084(15-01-26).pdf | 2026-11-15 |
| Concession procurement: Read for the amendment table, definitions and full regulations 3–4 with neighbors; consolidation 15 October 2026. The current amendment was separately read in full. | https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s086/2016s086(15-10-26).pdf | 2026-11-15 |
| Utilities procurement: Read for the amendment table, definitions/authority scope, full regulations 3–4 and adjacent clauses; consolidation 15 January 2026. | https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s085/2016s085(15-01-26).pdf | 2026-11-15 |
| Defence/security procurement: Read for the amendment table, contractor/services-provider/supplier definitions and full regulations 3–5 with timing/scope neighbors; consolidation 29 June 2017. | https://gibraltarlaws.gov.gi/uploads/legislations/public-finance/2012s088/2012s088(29-06-17).pdf | 2026-11-15 |
| LN 2026/357: Read for the entire six-page amending instrument, regulations 1–4, all inserted provisions, savings and explanatory memorandum; 15 October 2026. | https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2016s086/2026=357.pdf | 2026-11-15 |
| Data Protection Act 2004: Read for the amendment table, definition context and full sections 3–7; consolidation 15 July 2026. | https://www.gibraltarlaws.gov.gi/uploads/legislations/data-protection/2004-01/2004-01(15-07-26).pdf | 2026-11-15 |
| Gibraltar GDPR: Read for current-version Articles 1–7 and 32 in full with material/territorial/definition/security neighbors; current text 15 July 2026. | https://www.gibraltarlaws.gov.gi/legislations/regulation-eu-2016679-5582 | 2026-11-15 |
| LN 2026/096: Read for the entire three-page instrument, commencement and all GDPR/DPA amendments and explanatory memorandum; effective on Treaty Implementation Date, recorded in current consolidation as 15 July 2026. | https://www.gibraltarlaws.gov.gi/uploads/legislations/data-protection/2004-01/2026=096.pdf | 2026-11-15 |
| Decision 2017/1870: Read for full operative Articles 1–3 and annex, recitals and in-force status through the web opening; published 17 October 2017. Empty ordinary fetch not treated as a read. | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017D1870 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/procurement-electronic-invoicing-regulations-2018-4469 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/electronic-commerce-act-2001-462 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/data-protection-act-2004-1046 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/data-protection-regulations-2026-8442 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/procurement-public-sector-contracts-regulations-2016-2858 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/procurement-concession-contracts-regulations-2016-4027 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/procurement-concession-contracts-amendment-regulations-2026-9230 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://www.gibraltarlaws.gov.gi/legislations/procurement-utilities-contracts-regulations-2016-2860 | 2026-11-15 |
| Current-version index: Read for the active text/version header and listed amending instruments; historical version warnings distinguished from the current selection. | https://gibraltarlaws.gov.gi/legislations/procurement-defence-and-security-public-contracts-regulations-2012-2859 | 2026-11-15 |

Not yet confirmed: a general private B2B/B2C electronic-issuance mandate or exemption; actual procurement thresholds/award eligibility for a particular contract, including defence supplier entitlement under EU-exit/treaty measures; Gibraltar-specific semantic migration/cutover, replacement syntax list or local transition instrument; live buyer endpoints/submission acceptance; credit-note/correction and electronic-signature/trust-service workflows; transaction-specific record periods beyond the sourced company/tax rules and enquiry/litigation holds; actual cross-border tax fields, special-category data or third-country transfer route; cash standard-scale conversions, invoice-specific lateness fines/payment surcharge/interest; standalone source establishing the Treaty Implementation Date; independent professional approval. These are unusable boundaries, not not-applicable conclusions. The ordinary EUR-Lex fetch returned an empty HTTP202 response; the full operative decision and annex were instead actually opened through the web tool. No live buyer endpoint, schema service or calculator/API has been exercised.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-15. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `gi-einvoice` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/gi-einvoice. If neither is available, confirm every figure against the official source pages cited above before relying on it.
