---
name: de-einvoice-2025-2027
description: "Comprehensive guide for mandatory B2B electronic invoicing in Germany under the Growth Opportunities Act (Wachstumschancengesetz). Covers the phased statutory timeline: mandatory receipt capability for all German business enterprises starting 1 January 2025, mandatory issuance for companies with prior-year turnover exceeding €800,000 starting 1 January 2027, and universal B2B issuance starting 1 January 2028. Details compliant structured data formats under European standard EN 16931, including XRechnung 3.0.x and ZUGFeRD 2.x / Factur-X (Comfort and Extended profiles). Explains transmission channels (Peppol Network, dedicated email endpoints), statutory exemptions for small-amount invoices under €250 (§ 33 UStDV) and tax-exempt supplies (§ 4 UStG), input tax deduction eligibility under § 14 and § 15 UStG, and ERP implementation workflows. Primary sources: § 14 UStG, § 27 Abs. 38 UStG, BMF Guidance on E-Invoicing."
jurisdiction: DE
category: international
tax_year: 2025
tax_year_notes: "2025-2028 transitional regime"
tier: 2
last_updated: 2026-08-21
version: 1.0
depends_on:
  - einvoice-workflow-base
  - germany-bookkeeping
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Mandatory B2B E-Invoicing (2025–2028) v1.0

> **General reference only.** This skill is general tax and accounting reference material for AI-assisted workflows. It has not been reviewed for any specific company's facts, ERP configuration, or tax accounting procedures. Do not rely on it without review by a Steuerberater or qualified tax professional in Germany.

---

## What this file is

This skill covers the statutory requirements, format specifications, and implementation roadmap for mandatory B2B electronic invoicing (*elektronische Rechnung*) in Germany introduced by the **Wachstumschancengesetz** (Growth Opportunities Act), amending **§ 14 and § 27 UStG**.

---

## Section 1 — Statutory Scope & Definitions

### Legal Definition of an E-Invoice (§ 14 Abs. 1 Satz 3–6 UStG)
Under German tax law from 1 January 2025:
- **E-Invoice (*Elektronische Rechnung*)**: An invoice issued, transmitted, and received in a structured electronic format that complies with the European standard **EN 16931** (or is interoperable with it) allowing electronic extraction.
- **Other Invoice (*Sonstige Rechnung*)**: Paper invoices as well as non-structured electronic invoices (standard PDF, JPEG, TIFF, or Word documents). From 2025, standard PDFs are classified as "other invoices" and are subject to phase-out rules for domestic B2B transactions.

### Scope of the Mandate:
- Applies to all supplies of goods and services between taxable enterprises (**B2B**) where both supplier and recipient are established in Germany (or have a fixed establishment participating in the transaction).

### Out of Scope / Exemptions:
1. **B2C Transactions**: Supplies to private end consumers remain non-mandatory.
2. **Small-value invoices (*Kleinbetragsrechnungen*)**: Invoices with a gross total not exceeding **€250** (§ 33 UStDV) may continue to be issued as paper or standard PDF.
3. **Public transport tickets**: Fahrausweise (§ 34 UStDV).
4. **Tax-exempt supplies**: Strictly tax-exempt supplies under § 4 Nr. 8–29 UStG (such as financial services, medical care).

---

## Section 2 — Phased Implementation Timeline

| Date | Phase | Statutory Requirement & Legal Basis |
|---|---|---|
| **1 Jan 2025** | **Mandatory Receipt for ALL B2B** | Every German business (regardless of revenue, including Kleinunternehmer) must be capable of receiving and processing EN 16931 compliant e-invoices. Buyer consent is **no longer required** for e-invoice delivery (§ 27 Abs. 38 UStG). |
| **1 Jan 2025 – 31 Dec 2026** | **Transitional Issuance** | Suppliers may still issue paper or standard PDF invoices (with recipient consent) during this window. |
| **1 Jan 2027** | **Mandatory Issuance (> €800k)** | Businesses with prior-year total turnover (*Gesamtumsatz* § 19 Abs. 3 UStG) exceeding **€800,000** must issue structured e-invoices for domestic B2B sales. |
| **1 Jan 2028** | **Universal Mandatory Issuance** | All German businesses must issue structured e-invoices for domestic B2B transactions. EDI legacy formats remain permitted only if convertible to EN 16931. |

---

## Section 3 — Permitted Technical Formats

To qualify under § 14 Abs. 1 UStG, invoices must strictly adhere to the **CEN standard EN 16931**:

### 1. Pure XML Formats
* **XRechnung (CIUS-DE)**: Standard syntax developed by KoSIT for public procurement (B2G) and B2B in Germany. Uses UBL 2.1 (`urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`) or UN/CEFACT CII syntax.
* **Peppol BIS Billing 3.0**: European cross-border standard profile conforming to EN 16931.

### 2. Hybrid Formats
* **ZUGFeRD 2.2+ / Factur-X**: A PDF/A-3 container document with an embedded structured XML file (`factur-x.xml`).
  - *Compliant profiles*: **EN 16931 (Comfort)** and **Extended**.
  - *Non-compliant profile*: ZUGFeRD *Basic* or *Minimum* profiles do NOT meet EN 16931 requirements for the German B2B mandate.

---

## Section 4 — Step-by-Step Compliance Rules

### Step 1 — Receipt Readiness (Active since 1 Jan 2025)
1. Establish a designated electronic mailbox (e.g., `invoice@company.de` or API/Peppol ID).
2. Configure accounting/ERP software to validate, render, and archive incoming XML / PDF/A-3 invoices.
3. Ensure long-term storage meets **GoBD** requirements (structured XML must be archived in its native digital form, immutable, for 10 years; archiving only a rendered PDF printout is non-compliant).

### Step 2 — Mandatory Invoice Content Checks
Ensure all structured fields required by § 14 Abs. 4 UStG are present in the XML payload:
1. Full name and address of supplier and recipient.
2. Supplier Steuernummer or USt-IdNr.
3. Invoice issue date and unique sequential invoice number.
4. Quantity and standard description of supplied goods/services.
5. Date of supply / performance (*Lieferdatum* / *Leistungszeitpunkt*).
6. Net consideration split by VAT tax rate (19%, 7%, 0%) and total tax amount.
7. Buyer reference identifier (*Leitweg-ID* / *Käuferreferenz*) when applicable.

---

## Section 5 — Audit Flash Points

> **AUDIT FLASH POINT 1 — Input Tax Deduction Denial (§ 15 UStG).** When mandatory issuance applies (e.g. from 2027 for >€800k businesses and 2028 for all), receiving a non-structured invoice (such as a paper or standard PDF invoice) violates proper invoicing rules. The tax office (*Finanzamt*) may deny the recipient's input tax deduction (*Vorsteuerabzug*) until a proper structured e-invoice is provided.

> **AUDIT FLASH POINT 2 — GoBD Archiving of Hybrid Invoices.** For ZUGFeRD / Factur-X hybrid files, both the human-readable PDF/A layer and the embedded `factur-x.xml` constitute the tax document. In the event of a discrepancy, the XML data layer legally supersedes the visual representation.

---

## Section 6 — Self-Checks

- [ ] Invoice format is verified as EN 16931 compliant (XRechnung XML or ZUGFeRD EN 16931 profile).
- [ ] Inbound e-invoices are stored electronically in their original XML structure per GoBD rules.
- [ ] Invoices with gross total > €250 contain all mandatory § 14 Abs. 4 UStG data elements.
- [ ] Supplier Steuernummer / USt-IdNr is validated prior to posting in the general ledger.

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a licensed tax advisor (*Steuerberater*) or equivalent practitioner before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
