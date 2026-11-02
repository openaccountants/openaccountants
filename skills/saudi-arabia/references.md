---
name: saudi_arabia-references
jurisdiction: SA
tier: 2
last_updated: 2026-06-12
version: 1.0
description: Primary source references and related open-source projects for this jurisdiction.
---

# Saudi Arabia — Related Open-Source Projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

OpenAccountants is AGPL-3.0. All projects below have compatible licenses (MIT).

## SallaApp/ZATCA

- Repository: [SallaApp/ZATCA](https://github.com/SallaApp/ZATCA)
- License: MIT
- Language: PHP
- Stars: 160
- Scope: ZATCA (Fatoora) e-invoicing implementation maintained by Salla (Saudi e-commerce platform). Covers Phase 1 QR code generation and Phase 2 invoice signing (CSR generation, XML signing, ZATCA API integration). TLV encoding for the 5 mandatory QR fields (seller name, VAT registration number, timestamp, invoice total, VAT total). Includes certificate handling for ZATCA's FATOORA platform.
- Tax computation data: Confirms VAT is a single-rate system (examples use 15%). TLV Tag 5 = invoice VAT total. Confirms 15-digit TIN format. No standalone rate tables — the VAT rate is passed as a parameter, not hardcoded.
- Integration: MIT — fully compatible. Reference for ZATCA e-invoicing QR code and signing workflows. Useful for validating e-invoice compliance assertions in the VAT skill (Section 5.10).

## wes4m/zatca-xml-js

- Repository: [wes4m/zatca-xml-js](https://github.com/wes4m/zatca-xml-js)
- License: MIT
- Language: TypeScript
- Stars: 88
- Scope: Full ZATCA e-invoicing implementation covering Phase 1 and Phase 2. Generates UBL 2.1 XML invoices, handles CSR/certificate lifecycle with ZATCA sandbox and production APIs, signs invoices with ECDSA, and generates QR codes. Includes ZATCA's official PDF specification documents in `/docs`.
- Tax computation data: Confirms key tax constants embedded in invoice construction:
  - `VAT_percent: 0.15` in sample line items (standard 15% rate)
  - Tax category `S` (standard-rated) and `O` (out of scope / zero-rated) per UN/ECE 5305
  - Invoice type codes: 388 (Tax Invoice), 383 (Debit Note), 381 (Credit Note) per UN/CEFACT 1001
  - Payment method codes: 10 (Cash), 30 (Credit), 42 (Bank Account), 48 (Bank Card)
  - Currency hardcoded to SAR
  - VAT computation: `line_item_subtotal × VAT_percent` with rounding rules (BR-KSA-DEC-02, BR-KSA-DEC-03)
  - Tax-inclusive amount: `tax_exclusive_amount + total_taxes`
  - QR TLV structure: 9 tags for Phase 2 (seller name, VAT number, timestamp, total, VAT total, invoice hash, digital signature, public key, certificate signature)
- Integration: MIT — fully compatible. The most complete open-source ZATCA implementation. Invoice type codes and payment method codes could supplement the VAT skill's e-invoicing section. The ZATCA specification PDFs in `/docs` are valuable primary source references.

## axenda/zatca

- Repository: [axenda/zatca](https://github.com/axenda/zatca)
- License: MIT
- Language: TypeScript
- Stars: 60
- Scope: Lightweight ZATCA QR code generator for Phase 1 e-invoicing. Generates TLV-encoded QR codes from the 5 mandatory invoice fields. Works in both frontend (browser) and backend (Node.js) environments. Validated against ZATCA's official SDK output.
- Tax computation data: Minimal — the package takes invoice total and VAT total as string inputs (`invoiceTotal: '100.00'`, `invoiceVatTotal: '15.00'`). The test examples consistently use 15% VAT (15.00 on 100.00 total). No rate computation logic — the VAT amount is pre-calculated by the caller.
- Integration: MIT — fully compatible. Simple reference for QR code TLV encoding. Validates the QR field structure used in the VAT skill's e-invoicing section.

## Assessment: Tax computation content

These three repos are **e-invoicing tools**, not tax computation engines. They handle invoice formatting, signing, and ZATCA API compliance — the VAT rate and amounts are inputs, not computed from rate tables. Key findings:

| Data point | Present in repos? | Already in VAT skill? |
|---|---|---|
| Standard VAT rate 15% | Yes (as parameter/example) | Yes (Section 1, 5.1) |
| Zero-rated / exempt categories | Partially (category codes S/O only) | Yes (detailed in Sections 5.2, 5.3) |
| Tax category codes (UN/ECE 5305) | Yes (S, O) | Implicit in field mappings |
| Invoice type codes (388/383/381) | Yes | Not explicitly listed |
| Payment method codes | Yes (10/30/42/48) | Not explicitly listed |
| VAT computation formula | Yes (subtotal × rate) | Yes (Section 5.14) |
| Withholding tax rates on non-residents | No | No |
| Zakat computation rules (2.5% on net assets) | No | No (out of scope for VAT skill) |
| Registration thresholds | No | Yes (SAR 40M monthly/quarterly) |
| Penalty rules | No | Yes (Section 5.11, 5.12) |

**Conclusion:** No material tax computation data to extract from these repos beyond what the existing skill already covers. The repos are useful as e-invoicing implementation references and for cross-validating the invoice structure and category codes documented in the VAT skill.

### Withholding tax and zakat — data gap

None of the three repos contain withholding tax rate tables or zakat computation rules. These are separate ZATCA obligations:

- **Withholding tax (WHT):** 5% on management fees, 15% on royalties, 5% on rent, 20% on payments for services rendered in KSA — rates set by the Income Tax Law (Royal Decree No. M/1). A WHT skill would need to be authored from ZATCA's published WHT rate schedules, not from these e-invoicing repos.
- **Zakat:** 2.5% on the zakat base (net adjusted assets × Saudi/GCC ownership percentage) — governed by the Zakat Collection Regulations. These e-invoicing repos do not touch zakat computation. A zakat skill would need to be authored from ZATCA's zakat guidelines and the Implementing Regulations.
