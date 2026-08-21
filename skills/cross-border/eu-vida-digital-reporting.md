---
name: eu-vida-digital-reporting
description: "Comprehensive guide for the European Union VAT in the Digital Age (ViDA) package adopted by ECOFIN. Covers the three core pillars: (1) Digital Reporting Requirements (DRR) and mandatory real-time electronic invoicing for intra-EU B2B transactions based on the European standard EN 16931, (2) the deemed supplier regime for digital platforms in passenger transport and short-term accommodation, and (3) the expansion of Single VAT Registration (SVR) including the extension of the One-Stop Shop (OSS) and Import One-Stop Shop (IOSS). Includes phased rollout timelines from 2025 to 2030, technical XML requirements (UBL/CII), cross-border invoice validation rules, and penalty avoidance. Primary sources: Council Directive (EU) amending Directive 2006/112/EC, Council Regulations (EU) 904/2010 and 282/2011."
jurisdiction: INTL
category: cross-border
tax_year: 2025
tax_year_notes: "2025-2030 phased implementation"
tier: 2
last_updated: 2026-08-21
version: 1.0
depends_on:
  - cross-border-workflow-base
  - eu-vat-base
verified_by: pending
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EU ViDA: VAT in the Digital Age & Digital Reporting v1.0

> **General reference only.** This skill is general tax and compliance reference material for AI-assisted workflows. It has not been reviewed for any specific entity's facts, transaction flows, ERP architecture, or member state options. Do not rely on it without review by a qualified tax professional in the relevant EU member state.

---

## What this file is

This skill covers the compliance and technical architecture of the European Union's **VAT in the Digital Age (ViDA)** package. It details how cross-border businesses operating across EU member states must adapt their transaction reporting, invoicing engines, platform operations, and VAT accounting systems.

---

## Section 1 — Scope Statement

### What this skill covers:
- **Pillar 1: Digital Reporting Requirements (DRR) & E-Invoicing**:
  - Mandatory electronic invoicing for all intra-Community B2B supplies.
  - Phasing out summary recapitulative statements (VIES EC Sales Lists) in favor of transaction-by-transaction real-time reporting.
  - Required data structures adhering to **EN 16931** (UBL 2.1 and UN/CEFACT CII).
- **Pillar 2: Platform Economy (Deemed Supplier Model)**:
  - Deemed supplier liability for online mediation platforms in short-term accommodation (up to 30 nights) and passenger road transport.
  - Record-keeping and transmission obligations for non-deemed facilitator platforms.
- **Pillar 3: Single VAT Registration (SVR) & OSS Expansion**:
  - Expansion of OSS to cover all B2C supplies of goods (including domestic sales by non-established suppliers) and transfers of own goods.
  - Mandatory reverse-charge mechanism for B2B supplies made by non-established suppliers.

### What this skill does NOT cover:
- Domestic-only non-EU B2B transactions.
- Purely domestic member-state clearance regimes (e.g. Italy SDI, Poland KSeF) except where harmonized under ViDA standards.

---

## Section 2 — Phased Implementation Timeline

| Phase / Date | Milestone | Scope & Statutory Obligation |
|---|---|---|
| **Phase 1: 2025–2026** | **Harmonization & National Permissions** | Member states may mandate domestic B2B e-invoicing without seeking individual European Commission derogations (Art. 218/232 amended). |
| **Phase 2: 2027–2028** | **Single VAT Registration & SVR** | Extension of OSS to own-goods transfers and all cross-border B2C movements; simplified call-off stock regime phased out. |
| **Phase 3: 2028–2029** | **Platform Deemed Supplier Regime** | Platforms facilitating short-term rental and passenger transport deemed to receive and supply the underlying service unless underlying provider supplies valid VAT ID. |
| **Phase 4: 2030 (Full DRR)** | **Intra-EU Real-Time DRR** | Full mandatory e-invoicing and real-time transaction reporting within 10 days of the taxable event for intra-EU B2B supplies; abolition of recapitulative statements. |

---

## Section 3 — Key Technical & Compliance Requirements

### 1. E-Invoice Technical Standard (EN 16931)
- Under ViDA, an electronic invoice is strictly defined as an invoice issued, transmitted, and received in a structured electronic format that allows for automated electronic processing (**PDF and unstructured scans no longer qualify**).
- Core syntax models:
  - **OASIS Universal Business Language (UBL 2.1 / 2.3)** XML.
  - **UN/CEFACT Cross Industry Invoice (CII) XML** (16B).
- Hybrid formats (such as **ZUGFeRD / Factur-X**) are compliant only if the embedded XML file strictly conforms to EN 16931.

### 2. Intra-EU Digital Reporting Timeline (DRR)
- **Issuance deadline**: Within **10 calendar days** following the chargeable event (supply of goods or services).
- **Transmission**: Immediate automated transmission to national tax authority platform at the time of issuance or within 2 business days.
- **Data payload**: Core invoice subset including Seller/Buyer VAT numbers, place of supply, taxable amount per rate, applied exemption/reverse charge clause, and payment details.

---

## Section 4 — Step-by-Step Compliance Rules

### Step 1 — Entity Transaction Classification
1. Identify whether the transaction is:
   - Intra-Community B2B supply of goods (Art. 138).
   - Cross-border B2B service subject to reverse charge (Art. 196).
   - Platform-facilitated B2C transaction (Platform deemed supplier rules).
   - Domestic transfer of own business assets.

### Step 2 — Verify VAT Identification Numbers (VIES)
1. Verify the customer's VAT number via the **VIES API**.
2. Retain automated timestamped validation logs with consultation number.

### Step 3 — Construct Structured E-Invoice Payload
1. Format invoice strictly as EN 16931 compliant XML (UBL or CII).
2. Populate mandatory ViDA extensions:
   - `InvoiceTypeCode`: standard 380.
   - `PaymentMeansCode`: ISO 20022 compliant.
   - `TaxExemptionReason`: Explicit reference to Directive 2006/112/EC article (e.g., *"Reverse charge — Article 196"*).

### Step 4 — Real-Time Reporting
1. Dispatch structured e-invoice to buyer's registered Peppol endpoint or member-state access point.
2. Simultaneously transmit telemetry payload to the designated national tax authority DRR ingestion node.

---

## Section 5 — Audit Flash Points

> **AUDIT FLASH POINT 1 — VIES Recapitulative Statement vs DRR Mismatch.** Transitioning between legacy VIES recapitulative quarterly filings and real-time digital reporting presents reconciliation hazards. Discrepancies between customs data and DRR payloads trigger immediate automatic risk scoring.

> **AUDIT FLASH POINT 2 — Platform Deemed Supplier Misclassification.** Platforms failing to collect and verify supplier VAT registrations will be held strictly liable for unpaid output VAT plus late payment surcharges on all mediated bookings.

---

## Section 6 — Self-Checks

- [ ] Invoice file is structured XML conforming to EN 16931 (not visual PDF).
- [ ] Supplier and Customer VAT numbers are verified via active VIES lookups.
- [ ] Reverse charge or exemption statement explicitly cites Directive 2006/112/EC.
- [ ] Transmission timestamp is within 10 days of the chargeable supply date.

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
