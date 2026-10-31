---
name: gi-einvoice
description: >
  Gibraltar invoicing reference for companies and suppliers performing covered public procurement contracts. Explains the structured electronic invoice definition, public authority receipt and processing duty, core data elements and company-name disclosure. Provides an invoice reconciliation example and a workflow for confirming contract scope, syntax and delivery evidence. Based on primary legislation checked in October 2026. General business-to-business issuance mandates, current procurement eligibility, technical standard versions, buyer endpoints, transaction-specific retention periods and professional review remain unresolved. This source-cited draft does not certify a software format or establish that every Gibraltar invoice must be electronic.
jurisdiction: GI
category: invoicing
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.3
verified_by: pending
sources:
  - url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108934/Required%2Bsyntaxes"
    title: "European Commission: Required syntaxes, updated 2 February 2026"
    as_of: "2026-10-22"
  - url: "https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108661/European%2BStandard%2Band%2BSpecifications"
    title: "European Commission: European Standard and Specifications, migration notice updated 24 June 2026"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf"
    title: "Electronic Commerce Act 2001, sections 19–22, 1 January 2021 consolidation"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf"
    title: "Procurement (Electronic Invoicing) Regulations 2018, regulations 2–6"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf"
    title: "Companies Act 2014, sections 179–180, 1 August 2025 consolidation"
    as_of: "2026-10-22"
---

# Gibraltar: invoices and public procurement e-invoicing

## Scope and applicability

The Procurement (Electronic Invoicing) Regulations 2018 apply to electronic invoices issued by an economic operator when performing a goods, works or services contract awarded under the listed procurement regulations: defence/security (2012), public-sector, concession and utilities contracts (2016). Record the award regime and contract, not merely the customer's public-sector name. A specific exclusion applies to secret/security-sensitive defence contracts where the stated essential-interest conditions are met. [Regulations 2–3](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

For a covered contract, regulation 5(1) requires the contracting authority to have the means to receive and process electronic invoices securely. Regulation 5(2) specifies requirements for the invoice submitted. This establishes a public-procurement receipt/processing regime; these provisions do not by themselves impose universal electronic issuance on every private business. A general B2B/B2C mandate or exemption has not been established by this Guide. EI remains applicable to the country pack because this specific legislation exists. [Regulations 3–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

The official legislation index presents the 20 December 2018 text as current on the access date. Some definitions retain Member State nationality/establishment wording. The interaction with subsequent procurement legislation, EU-exit measures and the 2026 treaty requires separate checking for supplier eligibility. Do not infer eligibility from the age of the text or substitute another country's procurement thresholds.

## What counts as an electronic invoice

Regulation 2 requires a structured electronic format issued, transmitted and received so that automatic electronic processing is possible. A scanned image or ordinary unstructured PDF alone does not demonstrate that requirement. Regulation 5(2) requires the European semantic data-model standard and a syntax on the published Official Journal list, together with the minimum core information. Before implementation, obtain the current standard/version, syntax profile, validation rules and buyer submission route. This Guide does not certify a particular XML schema, network or portal. [Regulations 2, 5(2)](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

## Standard editions and syntax migration

Gibraltar regulation 5(2) requires both the semantic standard and a compliant syntax on the Official Journal list. The Commission's February 2026 technical page identifies the **2017 framework** as UBL 2.1 invoice/credit-note messages (ISO/IEC 19845:2015) and UN/CEFACT CII D16B. Its binding references are CEN/TS 16931-3-2:2017 and 16931-3-3:2017 respectively. Syntax bindings are version-specific: selecting a newer XML version does not itself establish conformity. [Commission syntax guidance](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108934/Required%2Bsyntaxes).

There is now a migration question. The Commission's June 2026 notice says EN 16931-1:2026 was published in May, the 2017 edition was formally withdrawn, and the older edition remains compliant during migration. It says migration plans are being developed and directs users to the relevant authority. That page is explicitly under review. It does **not** supply a Gibraltar cutover date. [Commission migration notice](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108661/European%2BStandard%2Band%2BSpecifications).

For implementation, record the semantic edition, syntax/version, binding, validation-artifact release, buyer profile and delivery route as separate fields. Obtain evidence of the applicable Gibraltar migration arrangements before choosing the 2026 edition or rejecting a 2017 invoice. These are recommended controls; neither Commission page proves a Gibraltar buyer endpoint is ready. This Guide has not verified a replacement Official Journal list, local transition instrument or live submission. The 2017 syntax identifiers above are a dated baseline, not certification of the complete current Gibraltar implementation.

## Required information

Regulation 4 lists thirteen core information groups:

| Group | Working-paper evidence |
|---|---|
| Process/invoice identifiers; invoice period | Invoice reference, process reference, relevant dates/period |
| Economic operator; buyer; payee; tax representative | Applicable party identifiers and details, with profile rules for absent parties |
| Contract references; delivery details | Award/order reference and performance/delivery records |
| Payment instructions | Agreed method, account and payment terms |
| Allowances/charges; line items | Reconciled quantities, prices, adjustments and descriptions |
| Totals; VAT breakdown if applicable | Arithmetic reconciliation and separately established tax treatment |

The right column is a suggested evidence mapping, not a complete technical schema. Determine mandatory/conditional fields under the required standard; do not invent a tax representative or VAT charge just to populate a field. The phrase “VAT breakdown if applicable” is not authority to charge Gibraltar VAT. Check relevant tax law separately. [Regulations 4–5](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

A company must show its name legibly on its invoices under Companies Act section 179(1)(b). Section 180 separately specifies registration and other particulars for business letters, order forms and website homepages. Do not claim every section 180 particular is an invoice requirement solely from that section; contractual, procurement and other legal requirements can add fields. [Companies Act, sections 179–180](https://www.gibraltarlaws.gov.gi/uploads/legislations/companies/2014-19/2014-19(01-08-25).pdf).

## Preparation and submission workflow

1. Confirm the buyer, procurement award regime, supplier status and any security exclusion.
2. Obtain the buyer's supported delivery route and applicable standard/syntax/version. Record who confirmed them and when.
3. Map the required fields to approved party, contract, delivery and accounting records. Verify the company name.
4. Recompute line extensions, allowances/charges, tax and payable amount. Establish tax treatment independently.
5. Validate the structured file against the actual required schema and business rules. Retain validation results and a readable rendering as separate evidence.
6. Submit by the confirmed route and retain receipt/rejection evidence. File generation alone is not proof of receipt, acceptance or payment.

Steps 2–6 are recommended implementation controls. No live buyer endpoint or test invoice has been exercised for this draft.

## Recomputable invoice example

Assume a contract priced in GBP, with 10 units at £80 and 3 units at £50, a £50 agreed invoice allowance and a £20 agreed charge. Assume independently confirmed zero tax due on this particular invoice; this is not a country-wide exemption conclusion.

- Line totals: 10 × £80 = £800; 3 × £50 = £150.
- Before adjustments: £800 + £150 = £950.
- Adjusted total: £950 − £50 + £20 = **£920**.
- With £200 already paid, remaining payable: £920 − £200 = **£720**.

Check that the allowance is not deducted both on a line and again at invoice level. If duplicated, the payable amount would be incorrectly reduced to £670. Matching arithmetic alone does not prove syntax compliance or correct tax treatment.

## Electronic originals and retained records

The Electronic Commerce Act distinguishes an original-document requirement, production of a document and retention of records. Check each relevant requirement; passing one test does not establish all the others.

| Requirement | Conditions in the Act |
|---|---|
| Present or retain an original, section 19 | Reliable assurance of integrity from the time the information was first generated in final form; if presentation is required, it must be capable of legible display to the recipient. |
| Produce a paper or tangible document electronically, section 20 | At creation, the generation method must reliably assure integrity and there must be a reasonable expectation of accessibility for future use. The recipient must consent to electronic production **or** receive the document in legible form. Consent is not the only route in this provision. |
| Retain documents, records or information electronically, section 21 | Information must remain accessible and capable of retention for later reference, in its generated/sent/received format or a format demonstrably representing that information accurately. Retain information identifying origin, destination and the date and time of sending or receipt. |

For sections 19–20, integrity concerns completeness and absence of alteration, allowing endorsements and normal communication, storage or display changes. Reliability depends on purpose and circumstances. Section 21(3) excludes information whose sole purpose is enabling transmission; this does not remove section 21(2)(c)'s identification and timestamp condition. Section 21(4) permits a third-party storage service if the retention conditions are met. [Electronic Commerce Act, sections 19–21](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

These provisions prescribe conditions for electronic records, not a universal retention period or an automatic permission to destroy paper. Determine the applicable tax/company retention period and outstanding enquiry or litigation holds separately; the [bookkeeping Guide](gi-bookkeeping-and-tax-records.md) addresses the tax and company record rules. Signature and trust-service requirements need separate verification: sections 11–18 are repealed in this consolidation.

An electronic document cannot be excluded from evidence solely because it is electronic; the Act also protects a non-original where it is the best evidence reasonably obtainable by the person adducing it. Evidential weight still depends on relevant factors including reliable generation, storage or communication, maintained integrity and originator identification. Admissibility does not prove the invoice accurate. [Section 22](https://www.gibraltarlaws.gov.gi/uploads/legislations/electronic-commerce/2001-07/2001-07(01-01-21).pdf).

### Record-retention control example

Suppose the supplier keeps a readable invoice image but discards the source file and all evidence of where and when it was sent. Readability alone does not demonstrate section 21 compliance: the retained format must accurately represent the information and the required origin/destination/timestamp information must remain available. A storage provider's successful upload message alone establishes neither condition.

As recommended controls, retain the structured invoice, a readable rendering, delivery metadata and validation results; test retrieval after migration and retain evidence of any conversion's accuracy. These are implementation controls, not statutory requirements to use a particular software product, hash algorithm or file extension. A hash can support integrity checking but does not by itself prove that the original invoice was correct or identify its sender.

## Data, retention and remaining checks

Regulation 6 restricts processing of personal data and the purposes for which invoice data can be used. Its reference to the 2004 Data Protection Act needs reconciliation with the current data-protection framework; this Guide does not treat that old citation as a complete statement of current privacy duties. Minimise unnecessary personal data and confirm the lawful processing and retention requirements for the actual transaction. [Regulation 6](https://www.gibraltarlaws.gov.gi/uploads/legislations/public-finance/2018s290/2018s290.pdf).

Outstanding: current procurement scope/thresholds and eligibility; applicable standard and syntax list; buyer endpoints; general B2B/B2C requirements; credit-note/correction workflows; electronic signatures/trust services; transaction-specific retention periods and holds; cross-border tax fields; independent source review and professional attestation. No not-applicable determination is made for those unresolved areas.

## Disclaimer

Source-cited draft, not professionally attested. A qualified reviewer must check the transaction, current law and technical requirements before the invoice is submitted or relied upon.
