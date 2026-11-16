---
name: saudi-einvoice
description: "Saudi Arabia FATOORA e-invoicing for 2026: establish resident/transaction scope and notified integration wave, choose standard or simplified invoices/notes, map UBL XML and VAT category calculations, protect EGS identity/hash chains, generate signatures and QR TLV, onboard and separate production/simulation, then interpret clearance/reporting outcomes and retain records. Corrects historical wave dates, stamping roles and production endpoints; preserves original technical and enforcement topics with explicit evidence boundaries. Read before Saudi invoice generation, integration or troubleshooting."
version: "1.1"
jurisdiction: SA
tax_year: 2026
last_updated: "2026-11-16"
depends_on:
  - einvoice-workflow-base
category: invoicing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: e-invoicing
type: "filing-howto"
---

# Saudi Arabia FATOORA e-invoicing: 2026 implementation and control method

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill prepares a compliance/integration workpaper. It does not certify a software product, authorise a production submission or replace the VAT analysis of the underlying supply.

## Scope

Read before generating, validating, signing, clearing, reporting, correcting or troubleshooting Saudi electronic invoices and associated credit/debit notes. Apply the **E-invoicing Regulation published 4 December 2020**, the implementation resolution updated **19 May 2023**, and its XML/security standards. The regulation was not first issued in December 2021: **4 December 2021** is the mandatory generation date. Phase 2 began **1 January 2023** in notified waves. The current official laws/standards landing pages still identify these instruments; a 2025 public-consultation draft is not substituted for an enacted rule. [Regulation arts. 1–7](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf); [resolution, First/Sixth](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf).

**Quick reference:** determine the resident supplier and invoicing obligation, actual standard/simplified document type, notified integration date and EGS unit first. **Standard documents are cleared before delivery to the buyer; simplified documents are taxpayer-stamped and reported within 24 hours**. Standard clearance stamping by ZATCA differs from simplified stamping by the taxpayer's EGS. A PDF scan, a QR-only library or a successful sandbox test is not proof of production compliance. [Resolution, Second/Third](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf); [technical guideline §§4.3.1–4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

Use [VAT](saudi-arabia-vat.md) for registration, place/time of supply, taxable/exempt/out-of-scope treatment, rates, deductions and returns; [WHT](sa-withholding-tax.md) for non-resident payments; [formation](sa-formation.md) for entity/permission setup; [references](references.md) for third-party tooling; and the existing `einvoice-workflow-base` dependency for its common workflow. Technical acceptance does not establish the right VAT treatment or input-tax entitlement.

## Ask the client first

Obtain the supplier's actual residence, VAT/group registration and taxable identity; issuing party and any third-party/self-billing arrangement; supply/payment/issue dates; customer location/status/identity; transaction and VAT classification; invoice/credit/debit/prepayment type; currency/exchange-rate evidence; original invoices and adjustment reason; and all required line, discount, charge, advance and tax data.

For integration, obtain the **dated ZATCA wave/individual notification**, historical VAT-subject revenue for the stated selection years, EGS architecture and units, device/branch identifiers, existing certificates/expiry/revocation state, environment and vendor/SDK versions. Request the XML, hash/UUID/ICV/PIH audit trail, **redacted** request/response and transport status, acceptance/warning/error details, queue timestamps and any official outage instruction. Never request private keys, passwords, OTPs, CSID secrets or live credentials in a public workpaper.

Do not diagnose from a screenshot of a QR alone. Missing actual notification, invoice type, tax treatment, original XML or environment identity stops a final go-live/submission recommendation. A recently registered taxpayer's status cannot be inferred only from the current-year turnover.

## The method, step by step

### 1. Establish mandate, transaction scope and wave

Regulation art. 3 covers a **resident taxable person** and a customer/third party invoicing on that resident supplier's behalf. It expressly excludes non-residents from the electronic-invoice/note obligation for their Saudi-taxed supplies/receipts. Therefore “all VAT-registered persons, no exemptions” was too broad. The implementation resolution's First clause includes the specified taxable/zero-rated supplies, exports, relevant intra-GCC/nominal supplies and advance receipts, while excluding fully exempt supplies/related receipts, reverse-charge supplies and goods imports from this e-invoicing issuance scope. These exclusions do not exempt an unrelated domestic sale made by an importer. [Regulation art. 3](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf); [resolution First(5)–(7)](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf).

Phase 1 requires compliant generation/storage; handwriting, word-processing/spreadsheet invoices and scanned paper do not meet the structured electronic requirement. Phase 2 adds the specific structured fields, security and integration once applicable to that taxpayer. An excluded e-invoice transaction may still need VAT/accounting records. Standard versus simplified eligibility follows VAT invoicing law, not a crude rule that every business customer must receive the same format and every consumer transaction can use a simplified invoice. [Regulation arts. 1–4](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf); [resolution First/Second/Third](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf).

#### Rates, bands and thresholds

The first nine historical waves are retained and corrected below. These are announced selection criteria/start dates; **use the actual notice and applicable later wave for the taxpayer**, not a choice among historical dates.

| Wave / parameter | Revenue selection or requirement | Date / conditions | Official source |
|---|---|---|---|
| Phase 1 | Persons/transactions within regulation art. 3 | Mandatory generation/storage **4 December 2021** | [Resolution First](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf) |
| Wave 1 | VAT-subject revenue **over SAR 3bn in 2021** | From **1 January 2023** | [Official commencement notice](https://zatca.gov.sa/en/MediaCenter/News/Pages/News-990.aspx) |
| Wave 2 | **Over SAR 500m in 2021** | From **1 July 2023** | [Wave 2](https://zatca.gov.sa/en/MediaCenter/News/Pages/Phase2-Wave2-Integration-Criteria.aspx) |
| Wave 3 | **Over SAR 250m in 2021 or 2022** | From **1 October 2023** | [Wave 3](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1023.aspx) |
| Wave 4 | **Over SAR 150m in 2021 or 2022** | From **1 November 2023** | [Wave 4](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1039.aspx) |
| Wave 5 | **Over SAR 100m in 2021 or 2022** | From **1 December 2023** | [Wave 5](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1051.aspx) |
| Wave 6 | **Over SAR 70m in 2021 or 2022** | From **1 January 2024**, not the old March date | [Arabic Wave 6](https://zatca.gov.sa/ar/MediaCenter/News/Pages/news-1063.aspx) |
| Wave 7 | **Over SAR 50m in 2021 or 2022** | From **1 February 2024**, not the old June date | [Wave 7](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1084.aspx) |
| Wave 8 | **Over SAR 40m in 2021 or 2022** | From **1 March 2024**, not the old October date; Arabic text specifies “exceeds” | [Arabic Wave 8](https://zatca.gov.sa/ar/MediaCenter/News/Pages/news-1089.aspx) |
| Wave 9 | **Over SAR 30m in 2021 or 2022** | From **1 June 2024**, not the old December date | [Wave 9](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1134.aspx) |
| Later waves / 2026 announced example | Wave 25: VAT-subject revenue **over SAR 187,500 in any of 2022, 2023, 2024 or 2025** | Announced **24 July 2026**, integration **no later than 1 February 2027**; do not defer an earlier-wave taxpayer to this later date | [Wave 25 notice](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx) |
| Direct notification | Subsequent waves notified at least **six months** before integration | Notice and selection years, not a generic turnover table alone, decide the actual implementation project | [Wave 25](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx) |
| Standard clearance | Standard invoices and their notes | Clear **before** providing to buyer, subject to ZATCA's specifically enabled contingency process | [Technical guideline §4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf) |
| Simplified reporting | Simplified invoices and their notes | Report **within 24 hours** of transaction completion; taxpayer EGS supplies stamp/QR | [Technical guideline §4.3.1](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf) |

The old “wave 10+ progressively lower in 2025–2026” line is replaced by an actual dated later notice. Waves **10–24**, any later announcement and a particular taxpayer's individual integration date are not fully catalogued here: retrieve the applicable official notice rather than interpolating a missing wave or treating Wave 25 as proof that every smaller registrant can wait. The accessible official commencement notice confirms the first-wave population and date; the earlier announcement URL now redirects to not-found, as disclosed in Sources.

### 2. Choose the legal document and XML type

Use **UBL 2.1** with the Saudi CIUS/business rules. The XML standard §11.2.1 states that the UBL message type is **Invoice for all document types**, with `cbc:InvoiceTypeCode` distinguishing invoice/note types. The standard's examples and business-rule paths use `/ubl:Invoice`; do not generate a generic UBL `<CreditNote>` or `<DebitNote>` root just because the document is a note. One summary table's credit-note message cell is inconsistent with that explicit statement/examples; validate against the official schemas/Schematron and current SDK. [XML standard §§11.2.1, 12–13](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

| Business document | `cbc:InvoiceTypeCode` | Ordinary `@name` without other flags | Route and condition |
|---|---|---|---|
| Standard tax invoice | `388` | `0100000` | Clearance before buyer delivery |
| Simplified tax invoice | `388` | `0200000` | Taxpayer stamp, then reporting |
| Standard credit note | `381` | `0100000` | Standard-note clearance; original invoice reference and reason |
| Simplified credit note | `381` | `0200000` | Simplified-note stamping/reporting; original reference and reason |
| Standard debit note | `383` | `0100000` | Standard-note clearance |
| Simplified debit note | `383` | `0200000` | Simplified-note stamping/reporting |
| Prepayment invoice | `386` | Appropriate `01`/`02` subtype and valid flags | Use the actual advance/payment adjustment rules rather than treating an advance as a second final sale |

Source for the whole document-type table: [XML standard §11.2.1](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf); [technical guideline §§4.3.1–4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf). These `@name` examples are not immutable defaults for special transactions. **BR-KSA-06 defines seven positions `NNPNESB`**: two-digit subtype, then third-party, nominal, export, summary and self-billing flags. Apply the permitted combinations, including simplified/self-billing/export restrictions in the adjacent rules. Do not confuse this invoice transaction code with the CSR's different invoice-capability code. [XML standard BR-KSA-06/07/31](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

A note corrects a qualifying original supply/invoice and follows its document type; it is not permission to edit/delete the issued invoice. XML §5.1 permits reference to one or more original invoices. The old absolute requirement for the original **UUID alone** does not replace the prescribed preceding-invoice `BillingReference/InvoiceDocumentReference/ID`, reason and any additional reference requirements. No universal “a credit note can never exceed one original invoice's value” server rule has been confirmed here; assess the actual referenced adjustments and VAT law.

### 3. Assemble the complete semantic data, not a QR-only document

Use the official data dictionary, XML schemas, CIUS and rule set for the installed release. Key paths retained from the original are below; they are a field map, not a complete validation schema.

| XML area | Required information / conditional rule |
|---|---|
| Root/namespaces | `Invoice` in `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`; `cac`, `cbc`, `ext` namespaces per §12, UTF-8 encoding |
| `cbc:ID`, `cbc:UUID` | Invoice identifier and unique machine-issued message identifier; BR-KSA-03 requires permitted characters. The old universal RFC-4122-v4 claim is not imposed without the current implementation specification |
| `cbc:IssueDate`, `cbc:IssueTime` | Actual issue date/time, not a future or altered timestamp; preserve reliable time/event evidence |
| `cbc:InvoiceTypeCode/@name` | Legal document code and actual seven-position transaction flags |
| `cbc:DocumentCurrencyCode`, `cbc:TaxCurrencyCode` | Document currency may differ from SAR; required accounting-currency VAT is SAR. Do not force every commercial invoice total to SAR |
| Additional document references `ICV`, `PIH`, `QR` | Counter, prior-invoice hash and required QR data in their specified elements; retain unit sequence and original records |
| Supplier `cac:AccountingSupplierParty` | Actual legal name, permitted business ID/scheme, VAT/group identity and prescribed address. Supplier VAT number format is 15 digits beginning/ending in 3; syntax is not proof of live registration |
| Supplier postal address | Street, building, city, postal code, **district** and country, plus the applicable Saudi address-format rules; the old minimal address list was incomplete |
| Buyer `cac:AccountingCustomerParty` | Name, address and identification according to document/customer/export status. Do not invent a Saudi VAT number for an unregistered or export buyer |
| Buyer VAT/other IDs | BR-KSA-14 supplies permitted other-ID schemes such as `TIN`, `CRN`, `MOM`, `MLS`, `700`, `SAG`, `NAT`, `GCC`, `IQA`, `OTH`; apply the exact circumstance and format. Export BR-KSA-46 prohibits the Saudi buyer VAT/group-number field described there |
| `cac:TaxTotal` and `cac:TaxSubtotal` | Taxable bases, category codes/rates, exemption/exception reasons and category/document VAT; required SAR accounting-currency VAT where applicable |
| `cac:InvoiceLine` | Line ID, actual quantity/unit, item name, net line amount, VAT classification, price/base quantity, allowances/charges and required line VAT/amount-with-VAT fields |
| `cac:LegalMonetaryTotal` | Sum of line nets, document allowances/charges, tax-exclusive/inclusive totals, prepayment, rounding and amount due, with the required arithmetic |
| Notes/advances/special supplies | Billing reference, adjustment reason, delivery/payment details and advance-invoice adjustments where the actual transaction requires them |

Sources: [XML standard §§5, 7–13; BR-KSA-03/04/06/09/14/26/27/33/34/40/42/44/46/51–56](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf). Arabic invoice content is required; an English translation may be included. A full Arabic-language record and retrievable original are separate from a UI language switch. [VAT IR art. 66(2)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).

### 4. Calculate and classify VAT correctly

The XML codes mean **S = standard-rated, Z = zero-rated, E = exempt, O = not subject to VAT**. A zero amount does not make E/O supplies zero-rated. In particular, “O = government services” is not a legal universal classification; determine the actual person's activity/supply in the VAT skill. Use the exact category/reason-code combination and relevant rate/percent-presence rules; do not decide treatment from a software enum or set every category's percentage to zero blindly. [XML standard §§8, 11.2.4, BR-S/BR-Z/BR-E/BR-O and BR-KSA](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

For each line, account for price **base quantity**, quantity, item discount, line allowance and line charge. For each distinct **category plus rate**, aggregate relevant net lines and document charges less allowances. Category VAT is calculated on that category base; document VAT is the sum of category VAT. Tax-inclusive total is tax-exclusive plus document VAT; amount due additionally deducts advances and includes permitted rounding. Do not omit document charges, distribute an allowance to the wrong category or tax an already VAT-inclusive price a second time. [XML standard §§8–10](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

The standard specifies **half-up rounding**, document totals to **two decimals**, and category VAT calculated at document/category level rather than summing already-rounded line VAT. Its line calculation separately specifies how components/line net are rounded. Do not interpret “no intermediate rounding” as permission to ignore those specific line rules, impose two decimals on every unit price, or grant a blanket **SAR 0.01 tolerance for every business rule**. Check each rule's own precision and tolerance in the current schema/Schematron. [XML standard §§9.2–9.6, 10, BR-DEC/BR-CO](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

### 5. Preserve unit identity, hash chain and signing responsibilities

An **EGS unit** may be a signing server or a capable POS unit depending on architecture. It is not automatically every dumb terminal. Determine where generation, stamping and submission occur; the official technical guideline has distinct central/cloud, smart-POS and branch-server cases. Protect each required unit's identity, credentials and audit trail. [Technical guideline §3.5](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

Generate the proper ECDSA key pair/CSR and protect the private key in the prescribed non-exportable security module. Security standard §2.2 requires **SHA-256, ECDSA and 256-bit** cryptography; the detailed guideline's OpenSSL example and developer manual specify **secp256k1**. The security certificate-profile table is explicitly illustrative and includes a generic P-256 label; use the actual official CSR/SDK profile, not an arbitrary interchangeable elliptic curve. XML stamping uses the specified XAdES enveloped signature/profile; PDF/A-3 has its PAdES/embedded-XML requirements. [Security standard §§2.2–2.3](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf); [technical guideline signing/appendix](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf); [developer manual, platform requirements](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/DEVELOPER-PORTAL-MANUAL.pdf).

For invoice hashing, apply the specified XML transforms, including exclusions for **`ext:UBLExtensions`, `cac:Signature` and the QR `AdditionalDocumentReference`**, then the required **C14N11 canonicalisation**, SHA-256 and correct Base64 encoding of the digest. Do not hash a pretty-printed display string, accidentally double-hash/double-Base64 or include the QR/signature circularly. Construct and sign the required `SignedInfo`/signed properties/certificate references and verify the complete signature, not just one digest. The detailed guideline lays out the signing stages; source examples are not a substitute for checking the actual byte-level SDK vectors. [Security standard §2.3.3](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf); [technical guideline §5.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

Maintain UUID, **ICV** and **PIH** with the actual generated sequence for the issuing unit. Security §3 uses the prescribed invoice-hash transform for the previous hash; XML BR-KSA-26 describes the initial hash. Use the specification's exact initial value and encoding, not an invented hash-of-display-text variant. Do not reset a counter/hash after a restart, omit rejected/generated records from the audit trail to hide them, or regenerate identifiers reflexively on a network timeout. Reconcile the actual document and acknowledged result before retry/correction. [XML BR-KSA-03/26/33/34](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf); [security §3](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf).

### 6. Generate QR TLV with the correct field types

Construct the TLV byte array first, then Base64 it, then render the QR. **UTF-8 byte length, not character count**, controls text lengths. The specification uses one-byte tag and length fields and different treatment for binary cryptographic values. A hex string, a Base64 string and the raw digest/signature bytes are different representations; use the documented encoding and vectors. Do not Base64 each field again merely because the final QR is Base64. [Security standard §4.1, technical guideline §6](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf).

| Tag | Preserved field | Condition / representation control |
|---|---|---|
| 1 | Seller name | Correct UTF-8 text; Arabic bytes can exceed the visible character count |
| 2 | Seller VAT number | Actual VAT identity text; not the commercial registration or invented TIN |
| 3 | Invoice timestamp | ISO 8601 issue timestamp with the correct time basis |
| 4 | Invoice total including VAT | Actual required total representation |
| 5 | VAT total | The standard identifies **BT-110**, not any arbitrary SAR/line amount substituted into this tag |
| 6 | XML invoice hash | SHA-256 digest representation under the TLV rules; §4.1 specifies a **32-byte** hash |
| 7 | ECDSA signature of XML hash | Correct cryptographic binary/encoded representation from the official vector |
| 8 | ECDSA public key | Use the prescribed extracted key representation; do not substitute an arbitrary PEM file/string |
| 9 | CA signature of cryptographic stamp | **For simplified invoices and associated notes**, the stated technical-CA signature; do not demand tag 9 for every standard document |

Source: [Security standard §4.1 and table 3, pp. 25–26](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf). Tags 1–5 are the Phase 1 basic content; Phase 2 adds the applicable cryptographic fields. For standard invoices, use the cleared document/updated QR returned by ZATCA; for simplified invoices, the taxpayer's EGS creates the stamp/QR before reporting. A readable QR is not a replacement for a compliant complete XML document or a successful production acknowledgment.

### 7. Onboard, renew and separate environments

1. Log in to **FATOORA portal** (`https://fatoora.zatca.gov.sa/`) with the taxpayer's authorised ZATCA/ERAD identity. This is separate from Developer Portal credentials. Select the current **onboard new solution unit/device** function and generate the required OTP for the actual unit(s).
2. The portal manual states OTP validity of **one hour**. Enter it locally into the intended EGS; generate the correct unit/taxpayer CSR/key and submit the CSR/OTP to the **Compliance CSID** process. Keep the private key inside the signing system; store issued token/secret securely. An OTP for another taxpayer/environment is not valid evidence.
3. Run compliance samples for the actual **CSR capability**. Technical guideline §3.3.4 requires standard invoice, standard debit and standard credit samples for capability `1000`; simplified invoice, simplified debit and simplified credit for `0100`. A unit supporting both must satisfy both relevant sets. The old universal three-sample list that omitted debit notes and mixed standard/simplified capabilities was wrong.
4. After passing the applicable checks, request the **Production CSID** using the required compliance identity/reference. Record unit/subject, issuing chain, environment, validity and secure storage. A compliance/test certificate is not a permanent production credential.
5. Begin the correct production clearance/reporting route only after the actual compliance and authorisation gates. Plan renewal against the actual certificate/portal state and current procedure. Renewal and revocation are different actions; revoking a certificate makes the affected unit inactive and requires the appropriate recovery/onboarding route.

Sources: [FATOORA portal manual §§1.A–D, pp. 4–12](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf); [technical guideline §§3.3.2–3.3.6](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf); [security standard §§2.1–2.2, 5](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf). Do not claim every certificate has the same fixed lifetime from an illustrative profile. VAT-group onboarding, changed VAT status and revoked/suspended registrations require the specific group/lifecycle procedure, not copying an old individual certificate.

The portal manual §3 lists these **production** routes under base **`https://gw-fatoora.zatca.gov.sa/e-invoicing/core`**:

| Path appended to production base | Method / purpose |
|---|---|
| `/compliance` | POST, request compliance CSID with required CSR/OTP data |
| `/compliance/invoices` | POST, required compliance documents |
| `/production/csids` | POST, request/renew production identity through the specified lifecycle |
| `/invoices/clearance/single` | POST, clearance of a standard invoice/note |
| `/invoices/reporting/single` | POST, reporting of a simplified invoice/note |

Source: [FATOORA portal manual §3, p. 30](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf). The old production base ending **`/developer-portal`** and invoice endpoints without **`/single`** are not these production routes. The manual separately lists **`/e-invoicing/simulation`** routes and distinct CSR template/environment values. Developer sandbox, FATOORA simulation and production are different environments; **do not send live taxpayer data or production secrets to a test environment**. No API call or onboarding was performed for this skill rewrite.

Use the actual current API documentation/Swagger for body, request headers, API version and response schema. Security standard §5 describes certificate/client identity plus issued secret using Basic authentication; protect both in transit/storage and redact them from logs. Do not paste a certificate/private key/secret into a web-based hashing tool even if an old appendix links one. Do not treat an old manual's illustrative JSON/status spelling or temporary sandbox profile as proof of the current production contract. [Security §5](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf); [developer manual §§2.3.8–2.3.11](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/DEVELOPER-PORTAL-MANUAL.pdf).

### 8. Validate, submit, interpret the result and correct lawfully

Validate **offline first** using the relevant official schemas/rules and available SDK version. Check business classification, mandatory/conditional fields, numeric precision, XML namespace/type, hash transforms, signature/certificate/expiry/revocation, unit counter/previous hash, QR bytes, seller/buyer identity and invoice uniqueness. A third-party package's tests or an offline SDK pass do not perform every production referential/security check. The developer manual expressly says sandbox success is testing only and test CSIDs cannot be used in core production. [XML §§4, 13](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf); [developer manual §§2.3.8–2.3.10](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/DEVELOPER-PORTAL-MANUAL.pdf).

For **standard** documents, submit for clearance and retain the returned cleared/stamped XML and updated QR before buyer delivery. For **simplified** documents, generate the taxpayer stamp/QR, provide the appropriate customer representation and queue/report within the required period. Preserve issue, transaction, request and acknowledgment timestamps. An HTTP response alone does not prove acceptance; parse the actual document outcome and error/warning information. The technical guideline distinguishes **accepted**, **accepted with warnings**, and **rejected**. Warnings in an accepted response still require investigation; a list containing warnings does not by itself establish acceptance. [Technical guideline §§4.3.1–4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

| Original failure/status topic retained | Correct diagnostic action |
|---|---|
| Invalid signature / `INVALID-SIGNATURE` label | Check intended signing unit/key/certificate, profile, transforms and immutable XML; do not blindly generate another private key and lose the issuing identity |
| Invalid certificate / `INVALID-CERTIFICATE` | Check environment, subject/VAT/unit, chain, expiry and revocation; follow actual lifecycle resolution rather than always re-onboarding immediately |
| Duplicate UUID / `DUPLICATE-UUID` | Locate original submission and outcome; distinguish retry after timeout from genuinely reused identity. Never create duplicate commercial invoices just to obtain a new UUID |
| Invalid hash / `INVALID-HASH` | Recompute using exact transformations/canonical bytes and digest encoding, then locate where content or encoding changed |
| Previous hash / `PIH-MISMATCH` | Reconcile the actual unit sequence and records; do not reset or rewrite issued history to force agreement |
| Tax calculation / `TAX-CALC-ERROR` | Check quantity/base quantity, discounts/charges, category/rate, rounding, advances and all line/category/document arithmetic |
| Missing field / `MISSING-FIELD` | Read the specific rule/path and conditional field requirement; do not fabricate buyer identity or legal tax category |
| Cleared / reported | Retain actual production document acknowledgment and applicable cleared output, not a screenshot of a success word |
| Rejected | Preserve failed request/response and determine the documented correction/resubmission procedure before issuing or changing documents |
| Warning | Distinguish accepted-with-warning from rejection; log and fix the actual rule without assuming that a warning always permits buyer delivery |

The capitalised failure strings above are **legacy diagnostic labels**, not a confirmed list of literal current ZATCA API error codes. Use the code/path actually returned by the current service. No live Swagger/error-code schema was read, so current field-name/case/status-code exhaustiveness is not asserted. [Technical guideline §§4.3.1–4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

Do not delete or overwrite an issued invoice to correct a commercial/VAT error; issue the legally required linked credit/debit document. Do not treat a retry, a genuine corrected rejected payload and an issued-document adjustment as the same operation. ZATCA-disabled clearance has a specifically described reporting contingency in §4.3.2; an ordinary taxpayer connectivity failure is **not proof** that this exception has been activated. Preserve the actual outage instruction and recovery evidence. [Regulation art. 4](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf); [technical guideline §4.3.2 notes](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

### 9. Archive, reconcile with VAT and assess actual enforcement

Retain original structured invoices/notes, unit identifiers/chain, signatures/QR/certificates, response and cleared output, submission timestamps, correction references, warning/error resolution and accounting reconciliation. Keep records retrievable with the required Saudi access, security and integrity controls. Ordinary VAT records are retained **at least six years after the relevant tax period**; capital-asset records follow the adjustment period **plus five years from acquisition**, with other laws/notices also relevant. Arabic records/invoices are required; bilingual presentation is permitted. Do not reduce every class to a six-year maximum or retain only a PDF image. [VAT IR art. 66](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf); [resolution Third, storage/integrity requirements](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf).

Reconcile cleared/reported sales, notes, VAT-category totals and timing to the sales ledger and the VAT return using the **VAT skill's actual return boxes**. E-invoicing acceptance does not prove return pre-population, correct Box 1/Box 2 labels, deductibility, payment or a complete tax return. The old claim that cleared invoices automatically feed a particular pre-populated return and every reported B2C amount supplies a stated box was not confirmed. Explain timing differences, advances, exempt/out-of-scope transactions and errors with evidence rather than forcing the tax return to an API total.

WHT is a separate gross-payment/treaty obligation. Determine its lawful base and contract/gross-up through WHT; do not reduce the XML VAT amount merely because the bank remits a net payment, and do not assume WHT automatically applies to an ordinary Saudi domestic VAT invoice. A platform record does not replace the taxpayer's independent audit trail or prove every seller-supplied extra field was retained by ZATCA. [Technical guideline §4.3 storage notes](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

Preserve the original enforcement subjects: failure to issue, missing fields, failure to integrate, deleting/modifying issued records, missing storage, obstruction and repeated violations. The old blanket **SAR 5,000–50,000** and **SAR 10,000–50,000** ranges are not established as a current automatic tariff for each subject. ZATCA's published field-violation reclassification guide describes warnings/correction/repeat rules and distinguishes field violations from filing/payment/evasion; apply the actual legal category, date, previous finding and notice. Universal penalty doubling, business suspension, public naming or tax-registration suspension for every e-invoicing breach is **not confirmed** here. [Regulation art. 4](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf); [official field-violation guide, scope and classification](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/VAT%20Violations%20Penalties_EN.pdf). Any temporary relief requires its own actual eligibility analysis, not deletion of an underlying invoice/reporting duty.

## Worked cases

### A. Category VAT with a document charge, allowance and exempt lines

Use the XML standard's category example as a technical fixture: standard-category line net amounts total **SAR 5,800**, a standard-category document charge is **SAR 200**, allowance **SAR 100**, and the correctly classified assumed standard rate is **15%**. Separate exempt-category line amounts total **SAR 3,000**, supported by the relevant tax reason. Standard taxable base is **SAR 5,900**, category VAT **SAR 885**; exempt category VAT is zero. Document tax-exclusive total is **SAR 8,900**, VAT **SAR 885**, inclusive total **SAR 9,785**. The example rate/classification is an established fixture input, not advice that every supply has that treatment. [XML standard §§9.6, 10 example pp. 26–28](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

```oa-check
name: XML category calculation includes document charge and allowance in the right category
inputs:
  standard_line_nets: 5800
  standard_document_charge: 200
  standard_document_allowance: 100
  standard_rate: 0.15
  exempt_line_nets: 3000
steps:
  - standard_category_base: standard_line_nets + standard_document_charge - standard_document_allowance
  - standard_category_vat: standard_category_base * standard_rate
  - exempt_category_vat: 0
  - tax_exclusive: standard_category_base + exempt_line_nets
  - document_vat: standard_category_vat + exempt_category_vat
  - tax_inclusive: tax_exclusive + document_vat
expected:
  standard_category_base: 5900
  standard_category_vat: 885
  tax_exclusive: 8900
  document_vat: 885
  tax_inclusive: 9785
```

### B. Category-level rounding differs from adding rounded line VAT

Assume three eligible standard-category lines each with final net **SAR 0.05**, no discounts/charges and the same correctly determined **15%** rate. Category base is **SAR 0.15**. Category VAT **0.0225** rounds half-up to **SAR 0.02**. Rounding each line's **0.0075** to **SAR 0.01** and adding gives **SAR 0.03**, which is **not the method for category VAT**. Follow the line rules for required line values and the distinct category/document formula; do not invent a global one-cent override to erase an unexplained difference. [XML standard §§9.6, 10](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf).

```oa-check
name: Half-up category VAT is not the sum of already rounded line VAT
inputs:
  line_count: 3
  final_net_per_line: 0.05
  established_vat_rate: 0.15
steps:
  - category_base: line_count * final_net_per_line
  - category_vat: round(category_base * established_vat_rate, 2)
  - illustrative_rounded_line_vat: round(final_net_per_line * established_vat_rate, 2)
  - sum_rounded_line_vat: line_count * illustrative_rounded_line_vat
  - excess_from_wrong_aggregation: sum_rounded_line_vat - category_vat
  - document_inclusive: category_base + category_vat
expected:
  category_base: 0.15
  category_vat: 0.02
  illustrative_rounded_line_vat: 0.01
  sum_rounded_line_vat: 0.03
  excess_from_wrong_aggregation: 0.01
  document_inclusive: 0.17
```

### C. Standard versus simplified and an ambiguous timeout

An otherwise compliant standard invoice generated at **10:00** cannot be delivered as a cleared document merely because a reporting request was transmitted. Obtain actual clearance/stamped output before delivery unless ZATCA's specific contingency applies. A simplified invoice issued for a completed **10:00** transaction is stamped by the EGS and reported within **24 hours**, ordinarily by **10:00 the following day**, preserving the actual time basis. A timeout in either route is not proof of rejection: inspect the existing UUID/submission record before creating any new commercial document. These are process controls, not a verified implementation test or a universal current retry/idempotency contract. [Technical guideline §§4.3.1–4.3.2](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf).

## When to refuse or refer

Stop production submission/go-live if the supplier's VAT/residence/authority, invoice-type eligibility, notified date, transaction tax treatment, unit/certificate/environment, hash/chain or original document is unresolved. Refer VAT classification/input recovery/adjustments to the VAT owner; treaty/gross-up matters to WHT; taxpayer-specific penalties/disputes to qualified advice. Unsupported customs/import, exempt or reverse-charge transactions must not be made to look like ordinary domestic taxable invoices merely to satisfy a schema.

Stop if a proposed fix exports signing keys, exposes secrets, alters/deletes issued history, fabricates buyer identities, misuses another unit's certificate, sends private live data to a sandbox or bypasses a blocked portal/CAPTCHA. Return the actual failed rule, redacted evidence, safe correction path and missing official specification. A package that only makes Phase 1 QR codes cannot be approved as a Phase 2 signing/clearance solution without separate evidence.

Deliver an implementation workpaper with scope/notice, versions and architecture, field/tax mapping, signing/QR/chain test evidence, onboarding status, environment-specific endpoints, actual response handling, queue/recovery controls, archiving and ledger/VAT reconciliation. A local arithmetic check validates only the fixture's arithmetic. **No production integration, live certificate or software conformance certification was tested in this rewrite.**

## Sources

Read date: **16 November 2026**. Official Arabic legal text prevails over the English translations; technical versions and limited reading scope are recorded below.

| Source | What was read and used |
|---|---|
| [E-invoicing Regulation, 4 December 2020](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/E-invoicing-Regulations.pdf) | Read on 2026-11-16. Read for arts. 1–7: definition, resident/non-resident scope, VAT incorporation, security and staged implementation |
| [Implementation resolution updated 19 May 2023](https://zatca.gov.sa/en/E-Invoicing/Introduction/LawsAndRegulations/Documents/20230519_E-Invoicing%20Implementation%20Resolution%20English.pdf) | Read on 2026-11-16. Read for First/Second/Third and implementation annex scope: transactions, exclusions, format, generation, stamping, sharing, storage and integration dates |
| [XML implementation standard v1.2](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_XML_Implementation_Standard_%20vF.pdf) | Read on 2026-11-16. Read for §§5, 8–13: document/transaction codes, field/rule paths, categories, monetary/rounding examples, UUID/PIH/ICV and buyer/supplier conditions; not every dictionary row is reproduced |
| [Security features standard v1.2](https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20230519_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vF.pdf) | Read on 2026-11-16. Read for §§2.1–2.3, 3–5: stamping responsibilities, key/certificate protection/profile, transformations, prior hash, QR TLV fields and authentication. Profile is explicitly illustrative |
| [Detailed technical guideline](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/E-invoicing-Detailed-Technical-Guideline.pdf) | Read on 2026-11-16. Read for §§3.3–3.5, 4.3.1–4.3.2, signing §5.2 and OpenSSL appendix: onboarding samples, architecture, accepted/warning/rejected outcomes, clearance contingency and secp256k1/hash process |
| [FATOORA portal user manual v3, May 2023](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/Fatoora_Portal_User_Manual_English.pdf) | Read on 2026-11-16. Read for production/simulation login, onboarding/renewal/revocation/OTP and §3 pp. 30–31 endpoint lists and environment separation |
| [Developer Portal manual v3, November 2022](https://zatca.gov.sa/en/E-Invoicing/Introduction/Guidelines/Documents/DEVELOPER-PORTAL-MANUAL.pdf) | Read on 2026-11-16. Read for SDK/platform and §§2.3.8–2.3.11 sandbox/compliance limitations, technical API topics and secp256k1 reference. Old runtime ranges/illustrative response schema are not certified current |
| [Wave 1 official commencement notice](https://zatca.gov.sa/en/MediaCenter/News/Pages/News-990.aspx) and [earlier announcement](https://zatca.gov.sa/en/MediaCenter/News/Pages/News_912.aspx) | Read on 2026-11-16: the accessible commencement notice confirms over SAR 3bn VAT-subject revenue in 2021 and 1 January 2023 integration. The earlier announcement was read in the cached web result; its direct and later-open not-found responses are not fresh read evidence |
| [Wave 2](https://zatca.gov.sa/en/MediaCenter/News/Pages/Phase2-Wave2-Integration-Criteria.aspx), [Wave 3](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1023.aspx), [Wave 4](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1039.aspx), [Wave 5](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1051.aspx) | Read on 2026-11-16. Read each announcement's selection revenue/year and integration-start paragraph; no inference from an undated secondary wave list |
| [Wave 6](https://zatca.gov.sa/ar/MediaCenter/News/Pages/news-1063.aspx), [Wave 7](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1084.aspx), [Arabic Wave 8](https://zatca.gov.sa/ar/MediaCenter/News/Pages/news-1089.aspx), [Wave 9](https://zatca.gov.sa/en/MediaCenter/News/Pages/news-1134.aspx) | Read on 2026-11-16. Read each operative selection/start paragraph, correcting the former 2024 dates and confirming the Arabic Wave 8 “exceeds” condition |
| [Wave 25, 24 July 2026](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx) | Read on 2026-11-16. Read for SAR 187,500, selection years, 1 February 2027 latest integration and six-month notification; not a taxpayer-specific deferral |
| [VAT implementing regulation](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) | Read on 2026-11-16. Read for art. 66 ordinary/capital records, Arabic, Saudi access and electronic controls. The separate VAT skill owns supply/return computations |
| [VAT field-violation reclassification guide](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/VAT%20Violations%20Penalties_EN.pdf) | Read on 2026-11-16. Read for scope, warning/correction/repeat distinctions and exclusion of non-field breaches; no blanket current per-breach tariff asserted |

**Not yet confirmed:** all waves 10–24/later notices and the individual taxpayer's notified date; current live Swagger request/response field names, API version/header requirements, exhaustive literal error/status codes and retry/idempotency contract; the actual installed SDK/certificate profile and byte-vector pass; universal credit-note value cap/original-UUID-only rule; VAT-return pre-population/old box mapping; automatic fine ranges/doubling/business or registration suspension/public naming; eligibility for temporary penalty relief; client-specific VAT classifications and signing/hosting controls. The sandbox-hosted manual returned 403 and was not read there; the separately fetched official ZATCA-hosted manuals above were read. No blocked access was bypassed.
