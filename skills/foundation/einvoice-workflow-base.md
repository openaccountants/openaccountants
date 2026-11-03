---
name: einvoice-workflow-base
description: Universal e-invoicing compliance workflow base that defines validation, field checking, format verification, and compliance reporting for all jurisdictions. Contains no jurisdiction-specific content — no country mandate thresholds, no local schema requirements, no penalty regimes, no transmission endpoints. This skill MUST be loaded alongside a country-specific e-invoicing skill that provides the mandate rules, format standard, and field requirements. This skill alone cannot produce any output.
version: 1.0
category: foundation
jurisdiction: GLOBAL
last_updated: 2026-06-12
tier: 2
---

# E-Invoice Workflow Base Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## What this file is, and what it is not

**This file contains workflow architecture only.** It defines how Claude should approach an e-invoicing compliance task: the order of operations, what to validate, how to report findings, what to check before delivering. It contains no country-specific mandate thresholds, no national schema definitions, no penalty regimes, no transmission endpoint details, no local field requirements beyond the universal baseline.

**This file must always be loaded with a country-specific e-invoicing skill** that provides the mandate applicability rules, required format standard, country-specific mandatory fields, transmission method, and penalty regime (e.g., `it-fatturapa`, `mx-cfdi`, `in-einvoice-irn`, `my-myinvois`, `pl-ksef`). This file alone cannot validate an invoice or produce a compliance report. Loading it without a companion is a configuration error and Claude must refuse to proceed.

**This file is the contract.** When a country e-invoicing skill says it conforms to v1.0 of this base, it means: it fills the country slots specified in Section 6, it participates in the workflow in Section 1, and its validation results can be verified by the self-checks in Section 5.

---

## Section 1 — The workflow (read this first, follow exactly)

You are helping a taxpayer or their advisor validate invoices against e-invoicing compliance requirements. The output is a compliance report that identifies issues before submission to the government platform. Your job is to catch validation errors, format problems, and computation mismatches before they trigger rejection or penalty.

Execute these seven steps in order. Do not skip. Do not reorder. Do not produce any compliance output before step 6.

### Step 1 — Confirm the companion skills are loaded

This workflow base requires a country-specific e-invoicing skill providing the mandate rules, format standard, field requirements, and transmission details.

If no country-specific skill is loaded, stop and tell the user: "I need a country-specific e-invoicing skill loaded alongside this workflow base. Which country's e-invoicing requirements are you checking against?" Do not proceed without it.

If a VAT/GST workflow skill is also loaded, note its presence — tax computation validation in Step 6 will cross-reference the tax skill's rate tables.

### Step 2 — Determine mandate applicability

Before validating any invoice content, confirm that the taxpayer is subject to the e-invoicing mandate:

1. **Check the country skill's mandate threshold.** Is the taxpayer above the turnover/revenue threshold that triggers the mandate? If below, the mandate may not apply — inform the user that e-invoicing is voluntary for their situation (but validation is still useful if they choose to comply).

2. **Check the transaction type.** Does this specific transaction type fall within the mandate scope? Some mandates apply only to B2B, others to B2G, others to all transactions. The country skill specifies which.

3. **Check effective dates.** Is the mandate in force for the invoice date on this document? Many mandates phase in by taxpayer size or transaction type. The country skill provides the timeline.

4. **Check exemptions.** Does the taxpayer qualify for any exemption (small business, specific sector, cross-border where mandate does not apply)? The country skill lists exemptions.

Output a one-sentence mandate status: "Mandate applies / Mandate does not apply (voluntary) / Partially applies (B2B only)" with the reason. Proceed with validation regardless — even voluntary compliance benefits from validation.

### Step 3 — Invoice data ingestion

Read the invoice data provided by the user. Accept any of:

- Structured XML/JSON (UBL, CII, country-specific format)
- PDF invoice (extract fields)
- Pasted text or tabular data
- Image of invoice (extract fields if readable)
- Draft invoice data in any format

For each invoice or batch of invoices, identify:

- Number of invoices in the batch
- Format the data is currently in (vs. the format required by the country mandate)
- Whether the data appears to be a draft (pre-submission) or a received invoice (post-submission validation)
- Language of the document
- Currency

If the data is unreadable or too degraded to extract fields reliably, stop and tell the user.

### Step 4 — Field validation

For every invoice in the batch, check every field against two layers of requirements:

**Layer 1 — Universal mandatory fields (Section 2 of this base).** These fields are required under virtually all e-invoicing regimes worldwide. A missing universal field is almost certainly an error regardless of jurisdiction.

**Layer 2 — Country-specific mandatory fields (from the country skill).** These fields are required by the specific national mandate. They may include fields not on the universal list (e.g., SAT regime code for Mexico CFDI, IRN hash for India, PEC address for Italy FatturaPA, QR code data for Saudi Arabia).

For each field, determine:
- **Present and valid:** The field exists and its content conforms to format rules (e.g., VAT number matches the expected pattern, date is in correct format, amounts are numeric).
- **Present but potentially invalid:** The field exists but the content may be incorrect (e.g., VAT number present but fails check-digit validation, date format wrong, amount has wrong decimal places).
- **Missing — mandatory:** The field is required and absent. The invoice will be rejected.
- **Missing — recommended:** The field is not strictly mandatory but its absence may cause processing issues or fails best practice.

Record every finding. Do not stop at the first error — validate exhaustively.

### Step 5 — Format compliance check

Verify that the invoice data conforms to the required format standard:

1. **Schema compliance.** If the invoice is in XML/JSON format, does it conform to the schema required by the country mandate? Check element names, nesting, namespaces, required vs. optional elements, data types, and enumerated value lists.

2. **Syntax validation.** Are there well-formedness issues? Unclosed tags, invalid characters, encoding problems, BOM issues, line ending inconsistencies.

3. **Code list compliance.** Do coded values (unit of measure codes, currency codes, country codes, tax category codes) match the allowed values from the relevant code lists (UN/ECE, ISO 4217, ISO 3166, UNCL 5305)?

4. **Business rule compliance.** Do cross-field validations pass? Examples: if tax category is "exempt," tax amount must be zero; if invoice type is "credit note," amounts should be negative or a reference to the original invoice must be present; if payment means is "direct debit," a bank account must be specified.

5. **Schematron / additional rules.** If the country mandate specifies additional validation rules beyond schema (common in Peppol BIS, EN 16931, country-specific extensions), check those rules.

If the invoice is not yet in the required format (e.g., user provides a PDF but the mandate requires UBL XML), note the gap and validate the field content as if it were going to be converted — the fields must be correct regardless of current format.

### Step 6 — Tax computation validation

For every line item and the invoice totals, verify tax arithmetic:

1. **Rate validation.** Does the tax rate applied to each line match a valid rate for that goods/services category in the country? Cross-reference the tax skill if loaded, or the country e-invoicing skill's rate table.

2. **Line-level computation.** For each line: quantity × unit price = line net amount. Line net amount × tax rate = line tax amount. Line net + line tax = line gross. Check each computation. Flag rounding differences above the country skill's tolerance (typically 0.01 in the invoice currency).

3. **Tax category consistency.** If a line is marked as exempt, zero-rated, or reverse charge, the tax amount must be zero and the relevant notation must be present.

4. **Invoice-level totals.** Sum of all line net amounts = invoice total net. Sum of all line tax amounts = invoice total tax. Total net + total tax = invoice total gross (or total due, accounting for discounts and charges).

5. **Tax summary consistency.** If the invoice has a tax breakdown summary (subtotals by rate), verify each rate subtotal matches the sum of line amounts at that rate. Verify the overall totals match.

6. **Rounding rules.** Apply the country skill's rounding convention (round per line then sum, or sum then round). Flag if the invoice appears to use a different rounding method that produces a different total.

7. **Discount and charge handling.** If discounts or charges are applied, verify they are correctly reflected in both the net amounts and the tax calculations. Document-level discounts must be allocated to tax categories per the country skill's rules.

### Step 7 — Produce compliance report

Produce the compliance report in the format specified in Section 3 (output specification). The report covers every finding from Steps 4, 5, and 6, categorized by severity.

Run the self-checks in Section 5 against the report. If any check fails, fix and re-run. Only deliver when all checks pass.

Write a short closing chat response:
- Overall pass/fail status
- Count of critical / warning / advisory findings
- The single most important action item
- Whether the invoice can be submitted as-is or requires corrections first

---

## Section 2 — Universal mandatory invoice fields

These fields are required under virtually every e-invoicing regime worldwide. They derive from the EU VAT Directive Article 226 (the most comprehensive baseline), the UN/CEFACT Cross-Industry Invoice standard, and the Peppol BIS 3.0 requirements. Country skills add fields beyond this list; they never subtract from it.

### Document identification

| Field | Description | Validation rule |
|---|---|---|
| Invoice number | Unique sequential identifier | Must be present; must be unique within the supplier's numbering sequence; must not contain only zeros |
| Invoice date | Date the invoice was issued | Must be present; must be a valid date; must not be in the future for submitted invoices |
| Invoice type code | Invoice, credit note, debit note, etc. | Must be present; must be from the allowed code list (UNCL 1001 subset or country equivalent) |
| Currency code | ISO 4217 currency of the invoice | Must be present; must be a valid ISO 4217 code |

### Supply information

| Field | Description | Validation rule |
|---|---|---|
| Tax point date / supply date | Date the supply was made or completed | Must be present (may equal invoice date); must be a valid date |
| Delivery date / period | When goods were delivered or services performed | Required if different from tax point date; if a period, start must precede end |

### Supplier (seller) identification

| Field | Description | Validation rule |
|---|---|---|
| Supplier name | Legal name of the supplier | Must be present; must not be empty |
| Supplier address | Postal address including country code | Must be present; country code must be valid ISO 3166-1 alpha-2 |
| Supplier tax ID | VAT number, GST number, or equivalent | Must be present for B2B; must conform to country-specific format; check digit validation where applicable |

### Customer (buyer) identification

| Field | Description | Validation rule |
|---|---|---|
| Customer name | Legal name of the buyer | Must be present |
| Customer address | Postal address including country code | Must be present for B2B; country code must be valid |
| Customer tax ID | VAT/GST number of the buyer | Required for B2B above the country skill's threshold; format validation where present |

### Line items

| Field | Description | Validation rule |
|---|---|---|
| Line item description | Description of goods or services | Must be present; must not be empty or generic placeholder |
| Quantity | Number of units | Must be present; must be numeric; must be positive (or negative for credit notes) |
| Unit of measure | UN/ECE Recommendation 20 code or description | Must be present; should be a valid code |
| Unit price | Price per unit excluding tax | Must be present; must be numeric |
| Line net amount | Quantity × unit price (before tax) | Must be present; must be numeric; must equal quantity × unit price within rounding tolerance |
| Tax rate per line | Applicable tax rate percentage | Must be present; must match a valid rate for the country |
| Tax amount per line | Tax computed on the line net | Must be present; must equal line net × rate within rounding tolerance |

### Totals

| Field | Description | Validation rule |
|---|---|---|
| Total net amount | Sum of all line net amounts | Must be present; must equal sum of line nets within rounding tolerance |
| Total tax amount | Sum of all line tax amounts | Must be present; must equal sum of line taxes within rounding tolerance |
| Total gross / amount due | Net + tax (adjusted for discounts/charges) | Must be present; must equal net + tax within rounding tolerance |

### Payment information

| Field | Description | Validation rule |
|---|---|---|
| Payment terms | Due date or payment terms description | Must be present; due date must be a valid date on or after invoice date |
| Payment means | Method of payment (bank transfer, direct debit, card, etc.) | Must be present; should be a valid code (UNCL 4461) |
| Payment account | Bank account details for payment | Required when payment means is bank transfer or direct debit |

### Conditional fields (required when applicable)

| Field | Trigger condition | Description |
|---|---|---|
| Reverse charge notation | When reverse charge applies | Textual indication that the customer accounts for tax |
| Exemption reason | When a line is exempt from tax | Reference to the legal provision granting exemption |
| Credit note reference | When document is a credit note | Reference to the original invoice being credited |
| Purchase order reference | When a PO was issued | Buyer's PO number for matching |
| Contract reference | When invoicing under a framework contract | Contract identifier |

---

## Section 3 — E-invoicing format standards (overview)

This section provides awareness of the major format standards. The country skill specifies which one applies. This workflow base validates against whichever standard the country skill designates.

### UBL 2.1 (Universal Business Language)

- **Scope:** EU standard via EN 16931; Peppol network; Australia/New Zealand (A-NZ extension); Singapore.
- **Structure:** XML with defined namespaces. Invoice and CreditNote are the primary document types.
- **Key characteristics:** Verbose element names, strong typing, code list references embedded as attributes, extension points for national customizations.
- **Peppol BIS 3.0:** The most common UBL implementation profile. Adds business rules (Schematron) on top of the schema. CIUS (Core Invoice Usage Specification) extensions exist per country.

### CII (Cross Industry Invoice) — UN/CEFACT

- **Scope:** Factur-X (France), ZUGFeRD (Germany), EN 16931 alternative syntax.
- **Structure:** XML based on the UN/CEFACT SCRDM (Supply Chain Reference Data Model). Different namespace and element structure from UBL.
- **Key characteristics:** Factur-X/ZUGFeRD embeds the XML inside a PDF/A-3, creating a hybrid human-readable + machine-readable document. Multiple profiles (Minimum, Basic, EN 16931, Extended) with increasing field requirements.

### Country-specific formats

| Format | Country | Key characteristics |
|---|---|---|
| FatturaPA | Italy | XML via SDI (Sistema di Interscambio); PA format for government, FPR12 for B2B; digital signature required |
| CFDI 4.0 | Mexico | XML via SAT portal; requires PAC (authorized certification provider); includes fiscal regime, usage code, and RFC tax ID |
| e-Invoice IRN | India | JSON payload submitted to IRP (Invoice Registration Portal); returns signed IRN and QR code; mandatory above ₹5 crore threshold (phasing down) |
| KSeF | Poland | Structured XML submitted to the national KSeF system; assigns a unique KSeF number; currently voluntary, mandatory from February 2026 |
| MyInvois | Malaysia | XML/JSON via LHDN (Inland Revenue Board) API; LHDN validates and returns a unique identifier; phased rollout by turnover |
| e-Fatura | Turkey | UBL-TR (Turkish UBL customization) via GIB (Revenue Administration); mandatory for all registered taxpayers |
| FEL | Guatemala | XML via SAT-certified provider; real-time authorization required before invoice is valid |
| Nota Fiscal | Brazil | Various XML formats (NF-e for goods, NFS-e for services) via SEFAZ/municipality portals; each state has slightly different requirements |

### Transmission methods

| Method | Description | Examples |
|---|---|---|
| Peppol network | Four-corner model via certified access points | EU cross-border, Singapore, Australia/NZ, Japan (pending) |
| Government portal | Direct upload to tax authority system | Italy SDI, Poland KSeF, India IRP, Mexico SAT |
| API submission | REST/SOAP API to government or certified intermediary | Malaysia MyInvois, India IRP, Turkey GIB |
| Certified intermediary | Submission via authorized third-party provider | Mexico PAC, Brazil authorized transmitter |
| Certified email (PEC) | Delivery via certified email system | Italy (alternative to SDI for some cases) |
| Network of networks | Interoperable multi-network routing | Peppol + national networks (e.g., France PPF + PDP) |

### What each format requires vs. what this base validates

This base validates **content correctness** (are the fields present, are the values valid, does the arithmetic check out). It does NOT validate **technical format conformance** at the byte level (is the XML well-formed against the XSD, is the digital signature valid, is the PDF/A-3 container compliant). Technical format validation requires tools (XML validators, signature verification libraries) that are outside this skill's scope. The country skill specifies which technical validation the user needs to perform externally and where to perform it.

---

## Section 4 — Validation tiers

Every finding from the validation process is assigned to one of three severity tiers. The tier determines the recommended action.

### Critical — Invoice will be rejected or is invalid

Findings that will cause the invoice to be rejected by the government platform, or that make the invoice legally invalid:

- Missing mandatory field (Layer 1 or Layer 2)
- Tax ID fails format validation or check-digit validation
- Invoice number is duplicate or missing
- Tax computation error above the country skill's tolerance threshold
- Required format element missing or malformed (would fail schema validation)
- Missing reverse charge notation when reverse charge applies
- Invoice total does not equal sum of lines
- Currency code invalid or missing
- Mandatory digital signature absent (where the country requires it)
- Tax rate does not match any valid rate for the country

**Recommended action:** Must be corrected before submission. Invoice cannot be submitted as-is.

### Warning — Potentially incorrect, may cause issues

Findings that will not necessarily cause immediate rejection but indicate a likely error or may trigger queries from the tax authority:

- Tax ID present but cannot be verified as active (VIES, GST portal, etc.)
- Rounding difference within tolerance but at the boundary
- Tax category code present but unusual for the goods/services described
- Supply date significantly different from invoice date (>30 days) without explanation
- Payment terms missing due date (terms present but ambiguous)
- Unit of measure code not from the standard code list (free text used instead)
- Line description very generic (e.g., "services" with no further detail)
- Credit note references an invoice number that appears non-sequential
- Discount applied without clear basis or reference

**Recommended action:** Should be reviewed and corrected if possible. Submission may succeed but the invoice may be queried or flagged in audit.

### Advisory — Best practice not followed

Findings that do not affect validity or compliance but represent best practice gaps:

- Purchase order reference absent (useful for buyer matching but not mandatory)
- Payment account details absent when payment means is bank transfer (buyer may delay payment)
- Contract reference absent for ongoing supply relationships
- Delivery address absent when different from buyer address
- Buyer email/electronic address absent (useful for Peppol routing)
- Line item classification code absent (CPV, UNSPSC, or country equivalent)
- Notes/remarks field empty where context would help
- Invoice period absent for recurring services

**Recommended action:** Consider adding for operational efficiency. No compliance risk from omission.

### Severity assignment rules

- If the country skill explicitly lists a field as mandatory for its mandate, missing = Critical, regardless of whether it appears on the universal list.
- If a field is on the universal list (Section 2) but the country skill's mandate does not enforce it, missing = Warning (not Critical).
- Computation errors are always Critical if they affect the tax amount. Computation errors that affect only the net amount (e.g., quantity × price rounding) are Warning if within the country skill's tolerance.
- The country skill may escalate Advisory findings to Warning for specific fields it considers important.

---

## Section 5 — Self-checks (run before delivering output)

Run these ten checks against the compliance report. If any fails, fix and re-run. Do not deliver until all pass.

### Completeness

**Check 1 — All invoices covered.** Every invoice in the batch provided by the user has a section in the compliance report. Count invoices in; count report sections; they must match.

**Check 2 — All mandatory fields checked.** For every invoice, every field on the universal mandatory list (Section 2) AND every field on the country skill's mandatory list has been validated. No field was skipped.

**Check 3 — Every finding has a severity.** Every issue identified in the report is assigned exactly one severity tier (Critical, Warning, or Advisory). No unclassified findings.

### Correctness

**Check 4 — Tax arithmetic independently verified.** For every invoice where tax computation was validated, the skill's own computation (quantity × price × rate) was performed independently, not merely read from the invoice. The report states the expected value and the invoice value for any discrepancy.

**Check 5 — No false positives on mandatory fields.** If the report flags a field as "missing — mandatory," verify it is genuinely mandatory by checking both the universal list (Section 2) and the country skill's list. A field flagged as mandatory-missing that is actually optional for this country is a false positive and must be removed or downgraded.

**Check 6 — Rate validation uses correct country.** The tax rates used for validation match the country of the supply (determined by place-of-supply rules), not necessarily the country of the supplier or buyer. If the supply is cross-border, the correct rate is the destination country's rate (or zero/exempt/reverse-charge as applicable).

### Consistency

**Check 7 — Severity is consistent across invoices.** The same type of finding receives the same severity across all invoices in the batch. If invoice 1 has a missing PO reference as "Advisory" and invoice 2 has the identical issue as "Warning" without justification, the report is inconsistent.

**Check 8 — Report summary matches detail.** The summary counts (X critical, Y warning, Z advisory) at the top of the report exactly match the count of findings in the detailed sections below.

### Actionability

**Check 9 — Every Critical finding has a suggested correction.** For each Critical finding, the report states what the correct value should be (if determinable) or what information the user needs to provide to fix it. "Missing field" alone is not sufficient — state which field, what it should contain, and where to find the correct value.

**Check 10 — Report is self-contained.** The report can be understood and acted upon without referring back to this skill file. All country-specific terms are explained. All field names use the user-facing name, not internal XML element names (though the XML element name may be noted in parentheses for technical users).

### Failure handling

If any check fails, fix the report and re-run all ten. Do not deliver until all pass. If a check fails twice on the same item, report the inconsistency to the user transparently.

---

## Section 6 — Country skill contract

Every country-specific e-invoicing skill loaded alongside this workflow base MUST provide the following. The country skill is incomplete without all mandatory slots.

### Mandatory slots

1. **Mandate applicability rules** — turnover/revenue threshold triggering mandatory e-invoicing, transaction types covered (B2B, B2C, B2G), effective dates and phase-in timeline, and how to determine if a specific taxpayer is in scope.

2. **Mandatory fields beyond universal list** — country-specific fields not on the Section 2 universal list. For each field: name, description, format/validation rule, and where the taxpayer finds the correct value.

3. **Format standard** — which format the country requires (UBL 2.1, CII, FatturaPA, CFDI, custom XML/JSON, etc.), the schema version, and where to obtain the schema/documentation.

4. **Transmission method and endpoint** — how invoices are submitted (government portal URL, API endpoint, Peppol network, certified intermediary), authentication requirements, and the expected response (acceptance/rejection notification, unique identifier assignment).

5. **Tax rate table** — all valid tax rates for the country with their category codes, descriptions of what each rate applies to, and the code list values used in the e-invoice format.

6. **Rounding rules** — whether to round per line then sum, or sum then round; decimal places required for amounts, quantities, and rates; tolerance for computation differences.

7. **Penalty regime for non-compliance** — what happens if an invoice fails validation, is submitted late, or is not submitted at all. Monetary penalties, percentage-based penalties, and any grace periods.

8. **Exemptions** — which taxpayers or transaction types are exempt from the mandate, with the conditions for each exemption.

9. **Code lists** — country-specific code lists for: tax categories, invoice type codes, unit of measure codes (if different from UN/ECE Rec 20), payment means codes, and any other enumerated values required by the format.

10. **Validation rules beyond schema** — business rules that cannot be expressed in the XSD/JSON schema alone (Schematron rules, cross-field validations, conditional requirements). For each rule: the condition, what is checked, and the error message.

11. **Sample valid invoice** — at least one complete example of a valid invoice in the country's required format, annotated with explanations of each field. This serves as a reference for validation and as a template for users creating new invoices.

### Optional slots

12. **Common errors catalogue** — a list of the most frequently encountered validation errors for this country's system, with their causes and fixes. Helps prioritize advisory guidance.

13. **Integration with accounting systems** — notes on how major accounting software packages export invoices for this country's system, common export errors, and format conversion guidance.

14. **Cross-border rules** — how the country's e-invoicing mandate interacts with cross-border supplies (does the mandate apply to exports? to intra-community supplies? to imports?).

15. **Archiving requirements** — how long e-invoices must be retained, in what format, and whether the original XML/JSON must be preserved or if a PDF representation suffices.

---

## Section 7 — Reference material

### Validation status

This file is v1.0 of `einvoice-workflow-base`, drafted as part of the Open Accountants skill architecture in May 2026. It follows the structural pattern established by `vat-workflow-base` v0.2.0 and extends it to e-invoicing compliance.

### Design decisions

1. **Validation-only, not generation.** This workflow validates existing invoices and reports issues. It does not generate e-invoices from scratch (that would require integration with invoicing software, digital signature capabilities, and government API access that are outside this skill's scope). Future versions may add a "draft preparation" mode.

2. **Universal baseline from EU Article 226.** The EU VAT Directive Article 226 provides the most comprehensive list of mandatory invoice fields among major jurisdictions. Using it as the baseline means most country skills only need to ADD fields, not redefine the core. Countries outside the EU still benefit from the baseline because their requirements are typically a subset plus country-specific additions.

3. **Three severity tiers, not two.** Unlike the VAT workflow's binary (classify/ask), e-invoice validation has a natural three-tier structure: will be rejected (Critical), might cause problems (Warning), and could be better (Advisory). This maps to the user's decision space: must fix, should fix, nice to fix.

4. **Format-agnostic validation.** This base validates content correctness regardless of the current format the data is in. Technical format validation (schema conformance, signature verification) is noted as required but deferred to external tools. This keeps the skill useful even when the user provides data in PDF or plain text rather than structured XML.

5. **Batch support.** The workflow handles single invoices and batches. The self-checks enforce consistency across a batch, which catches the common error of applying different rules to identical situations in different invoices.

### Known gaps

1. Digital signature validation is acknowledged but not performed. This requires cryptographic tooling outside the skill's scope.
2. Real-time VIES/GST portal verification of tax IDs is referenced but not performed (no API access). The skill validates format only.
3. Peppol network routing validation (SMP lookup, endpoint verification) is outside scope.
4. PDF/A-3 container compliance for Factur-X/ZUGFeRD hybrid invoices is outside scope.
5. The 10 self-checks are integrity checks on the report itself. They do not guarantee the underlying validation logic is correct — that depends on the country skill's accuracy.

### Change log

- **v1.0 (May 2026):** Initial release. Establishes the universal e-invoicing validation workflow, field requirements baseline from EU Article 226, three-tier severity model, 10 self-checks, and country skill contract.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
