---
name: germany-einvoice
description: Use this skill whenever asked about German e-invoicing, XRechnung, ZUGFeRD, ERechV, E-Rechnungsverordnung, Peppol BIS Billing Germany, Leitweg-ID, OZG-RE invoice portal, B2B e-invoicing mandate Germany, Wachstumschancengesetz, EN 16931 Germany, GoBD e-invoice archiving, or any question about issuing, receiving, validating, or archiving electronic invoices in Germany. Also trigger when preparing XRechnung XML invoices, configuring Peppol endpoints for German public-sector invoicing, handling B2B e-invoice reception requirements, or advising on ZUGFeRD profile selection. This skill covers XRechnung CIUS, ZUGFeRD hybrid format, Peppol transmission, mandatory fields, validation rules, GoBD archiving, penalties, and interaction with German VAT returns. ALWAYS read this skill before touching any German e-invoicing work.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Einvoice

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Currency | EUR |
| National CIUS | XRechnung (EN 16931 compliant) |
| Hybrid format | ZUGFeRD 2.1+ (PDF/A-3 + embedded CII XML) |
| Current XRechnung version | 3.0.1 (mandatory from 1 February 2024) |
| Governing body | Bundesministerium der Finanzen (BMF) |
| Standards body | Koordinierungsstelle für IT-Standards (KoSIT) |
| Key legislation | E-Rechnungsverordnung (ERechV); Wachstumschancengesetz (Growth Opportunities Act); §14 UStG; GoBD (updated 14 July 2025) |
| B2G portal | OZG-RE (Online-Zugangsgesetz-konforme Rechnungseingangsplattform) -- replaced ZRE in September 2025 |
| B2G mandatory since | 27 November 2020 (federal level) |
| B2B reception mandatory | 1 January 2025 |
| B2B issuance Phase 1 | 1 January 2027 (businesses with turnover > EUR 800,000) |
| B2B issuance Phase 2 | 1 January 2028 (all remaining businesses) |
| B2C | Not subject to e-invoicing mandate |
| Current status | B2G fully operational; B2B reception mandatory; B2B issuance transitioning |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

**Who Must Comply table**

| Scope | Requirement |
| --- | --- |
| B2G (federal) | All suppliers to federal public authorities must submit XRechnung or EN 16931-compliant invoices via OZG-RE since November 2020 |
| B2G (Länder) | Most German states have enacted their own e-invoicing regulations; timelines vary by state (all effective by 2024) |
| B2B (reception) | All domestic businesses must be able to receive EN 16931-compliant e-invoices from 1 January 2025 |
| B2B (issuance -- Phase 1) | Businesses with prior-year turnover > EUR 800,000 must issue e-invoices for domestic B2B from 1 January 2027 |
| B2B (issuance -- Phase 2) | All remaining businesses must issue from 1 January 2028 |
| B2C | Not mandated -- consumer invoices may continue as paper or PDF |
| Exemptions (B2B) | Small-amount invoices under EUR 250 (§33 UStDV); passenger transport tickets; tax-free supplies under §4 Nr. 8--29 UStG; businesses under §19 UStG (Kleinunternehmer, annual turnover ≤ EUR 22,000) |

### Transitional Rules (2025--2027)

**Transitional Rules table**

| Period | Rule |
| --- | --- |
| 2025--2026 | Businesses may still issue paper invoices or non-EN 16931 EDI invoices with buyer consent |
| 2027 | Issuance mandatory for larger businesses; smaller businesses may still use paper with buyer consent if their turnover ≤ EUR 800,000 |
| 2028 onward | All domestic B2B invoices must be EN 16931-compliant structured electronic invoices |

### Timeline Summary

**Timeline Summary table**

| Date | Milestone |
| --- | --- |
| November 2020 | Federal B2G mandate effective |
| January 2025 | B2B reception mandatory for all businesses |
| September 2025 | OZG-RE replaces ZRE as sole federal submission portal |
| July 2025 | GoBD updated for e-invoice archiving rules |
| January 2027 | B2B issuance mandatory (turnover > EUR 800,000) |
| January 2028 | B2B issuance mandatory for all |

## Section 3 -- Technical Format

### Accepted Formats

**Accepted Formats table**

| Format | Type | Standard | Status |
| --- | --- | --- | --- |
| XRechnung | Pure XML (UBL 2.1 or CII) | EN 16931 CIUS | Primary national standard |
| ZUGFeRD 2.1+ | Hybrid (PDF/A-3 + CII XML) | EN 16931 conformant | Accepted for B2B and B2G |
| Peppol BIS Billing 3.0 | Pure XML (UBL 2.1) | EN 16931 CIUS | Accepted -- nearly equivalent to XRechnung since v3.0.1 harmonisation |

### XRechnung Technical Details

**XRechnung Technical Details table**

| Parameter | Value |
| --- | --- |
| Version | 3.0.1 |
| UBL namespace | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` |
| CII namespace | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` |
| CustomizationID (UBL) | `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0` |
| ProfileID (BT-23) | `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` |
| Encoding | UTF-8 |
| Validation | KoSIT Validator (open-source, Java-based) |
| Schema download | https://www.xeinkauf.de |

### ZUGFeRD Profiles

**ZUGFeRD Profiles table**

| Profile | EN 16931 Compliant | Use Case |
| --- | --- | --- |
| Minimum | No | Basic PDF with minimal XML (not sufficient for B2G) |
| Basic WL | No | Without line detail |
| Basic | Yes (if fully populated) | Standard use |
| Comfort (EN 16931) | Yes | Full compliance |
| Extended | Yes (superset) | Additional business information |
| XRechnung | Yes | XRechnung rules embedded in ZUGFeRD container |

- **Profile selection guidance** — For B2G compliance, use the XRechnung or Comfort profile. For B2B mandate compliance, any EN 16931-conformant profile is accepted.

## Section 4 -- Mandatory Fields

### EN 16931 Core Fields (Required by XRechnung)

**EN 16931 Core Fields table**

| BT Code | Field | Required |
| --- | --- | --- |
| BT-1 | Invoice number | Yes |
| BT-2 | Invoice issue date | Yes |
| BT-3 | Invoice type code (380 = commercial invoice, 381 = credit note) | Yes |
| BT-5 | Invoice currency code | Yes |
| BT-9 | Payment due date | Yes |
| BT-10 | Buyer reference (Leitweg-ID for B2G) | Yes |
| BT-23 | Business process type (ProfileID) | Yes (mandatory since XRechnung 3.0.1) |
| BT-24 | Specification identifier (CustomizationID) | Yes |
| BT-27 | Seller name | Yes |
| BT-29 | Seller country code | Yes |
| BT-31 | Seller VAT identifier | Yes (unless exempt under §19 UStG) |
| BT-34 | Seller electronic address + scheme ID | Yes (mandatory since XRechnung 3.0.1) |
| BT-44 | Buyer name | Yes |
| BT-46 | Buyer country code | Yes |
| BT-48 | Buyer VAT identifier | Yes (for reverse charge / intra-EU) |
| BT-49 | Buyer electronic address + scheme ID | Yes (mandatory since XRechnung 3.0.1) |

### XRechnung-Specific Additional Requirements

**XRechnung-Specific Additional Requirements table**

| Field | Description | Required |
| --- | --- | --- |
| BT-10 (Leitweg-ID) | Hierarchical routing identifier for B2G (format: coarse-fine-check digit) | Yes (B2G) |
| BT-23 (ProfileID) | Must be set to the Peppol process identifier | Yes |
| BT-34 / BT-49 | Electronic addresses with scheme identifier (e.g., 0204 for Leitweg-ID, 9930 for DE VAT number) | Yes |
| Payment instructions (BG-16) | At least one payment means must be specified | Yes |
| BT-20 | Payment terms (text description) | Recommended |
| BT-81 | Payment means type code (e.g., 58 = SEPA credit transfer) | Yes |

## Section 5 -- Transmission Method

### B2G Transmission

**B2G Transmission table**

| Channel | Description |
| --- | --- |
| OZG-RE Web Portal | Upload via browser at https://xrechnung.bund.de |
| OZG-RE Email | Submit XRechnung XML as email attachment to designated address |
| Peppol | Machine-to-machine via Peppol Access Point using participant ID (format: 0204:{Leitweg-ID}) |

The ZRE (Zentrale Rechnungseingangsplattform) was decommissioned in September 2025. All federal submissions now go through OZG-RE.

### B2B Transmission

Germany does not prescribe a specific transmission channel for B2B e-invoices. Accepted methods include:

**B2B Transmission table**

| Channel | Description |
| --- | --- |
| Email | XRechnung or ZUGFeRD sent as email attachment |
| Peppol | Via Peppol network using Peppol participant IDs |
| EDI | Existing EDI channels, provided the invoice content conforms to EN 16931 |
| API / portal | Bilateral agreement between trading partners |
| Download portal | Seller provides structured e-invoice for download |

### Peppol in Germany

- KoSIT manages the German Peppol Authority
- Public authorities connected to OZG-RE are reachable via Peppol
- Peppol participant IDs for federal authorities use scheme 0204 (Leitweg-ID based)
- For B2B, scheme 9930 (DE VAT number) is commonly used

## Section 6 -- Validation Rules

### KoSIT Validator

The official open-source validation tool provided by KoSIT performs multi-layer validation:

**KoSIT Validator layers table**

| Layer | Description |
| --- | --- |
| Schema validation | XML against UBL 2.1 or CII XSD |
| Schematron (EN 16931) | European standard business rules |
| Schematron (XRechnung) | National CIUS rules (German-specific) |
| Schematron (Extension) | Extension rules for additional national requirements |

### Common Rejection Reasons

**Common Rejection Reasons table**

| Issue | Resolution |
| --- | --- |
| Missing BT-23 (ProfileID) | Mandatory since XRechnung 3.0.1 -- always populate |
| Missing BT-34 / BT-49 (electronic addresses) | Mandatory since 3.0.1 -- include with correct scheme ID |
| Invalid Leitweg-ID format | Must follow pattern: numeric segments separated by hyphens with check digit |
| Missing BT-10 (Buyer reference) | Mandatory for B2G; strongly recommended for B2B |
| Tax calculation inconsistency | Line net amount × tax rate must equal line tax amount; sum of lines must equal document total |
| Wrong CustomizationID | Must match XRechnung 3.0.1 URN exactly |
| Mixed currency without conversion | If invoice currency differs from EUR, provide BT-6 (VAT accounting currency) and conversion rate |

### OZG-RE Additional Checks

- Validates Leitweg-ID against the registered directory
- Verifies that the recipient authority is connected and active
- Returns structured error messages for rejected invoices

## Section 7 -- Tax Computation Rules

### VAT Rates (2025/2026)

**VAT Rates table**

| Rate | Application |
| --- | --- |
| 19% | Standard rate (Regelsteuersatz) |
| 7% | Reduced rate (ermäßigter Steuersatz) -- food, books, public transport, cultural events |
| 0% | Intra-EU supplies, exports (with §4 UStG exemption code) |

### Rounding

- **Line-level rounding** — Line-level: net amount = quantity × unit price, rounded to 2 decimal places
- **Tax amount per line rounding** — Tax amount per line: net amount × rate, rounded to 2 decimal places
- **Document-level totals** — Document-level totals must equal sum of line-level amounts within each tax category
- **Validation tolerance per tax subtotal group** — EUR 0.01 EUR (XRechnung validation tolerance per tax subtotal group)
- **Banker's rounding** — Banker's rounding (round half to even) is accepted but not required

### Multi-Rate Invoice Handling

- **Separate tax subtotal group per rate** — Each VAT rate requires a separate tax subtotal group (BG-23)
- **Tax category codes** — S (standard), AA (reduced), Z (zero-rated), E (exempt), AE (reverse charge), K (intra-EU), G (export), O (outside scope)
- **Reverse charge category code** — For reverse charge (§13b UStG), use category code AE with rate = 0%  _(§13b UStG)_
- **Tax exemption reason population** — Tax exemption reason (BT-120/BT-121) must be populated for zero-rate and exempt categories

### §14 UStG Invoice Requirements

German VAT law (§14 UStG) mandates specific content that must appear in the structured data:

- **§14 UStG required content list** — - Full name and address of seller and buyer - Tax number (Steuernummer) or VAT ID (USt-IdNr.) - Invoice date and sequential invoice number - Quantity and description of goods/services - Delivery/service date or period - Net amount per rate, applicable tax rate, and tax amount - Total gross amount  _(§14 UStG)_

## Section 8 -- Archiving Requirements

**Section 8 Archiving Requirements table**  _(§14b UStG)_

| Requirement | Detail |
| --- | --- |
| Retention period | 8 years (§14b UStG; reduced from 10 years by Bürokratieentlastungsgesetz IV, effective 2025) |
| Format | Original structured format (XML) as received or sent |
| GoBD compliance | Must satisfy Grundsätze zur ordnungsmäßigen Führung und Aufbewahrung (GoBD, updated 14 July 2025) |
| Hybrid invoices (ZUGFeRD) | Only the structured XML part must be archived; the PDF part is only required if it contains additional tax-relevant information (e.g., booking notes) |
| Immutability | Archived invoices must be tamper-proof -- no modifications allowed after receipt |
| Verfahrensdokumentation | Written procedural documentation describing the entire e-invoice lifecycle (receipt, processing, archiving) is mandatory |
| Storage location | Germany or EU member state; tax authorities must have full online access |
| Audit access | Three levels: Z1 (direct access to DV system), Z2 (indirect access via data export), Z3 (data carrier handover) |
| Conversion | Format conversion allowed only if original is also retained and the conversion process is documented |

## Section 9 -- Penalties for Non-Compliance

**Section 9 Penalties table**  _(§14 UStG; §26a UStG; §26a Abs. 1 UStG; §370 AO)_

| Violation | Penalty |
| --- | --- |
| Failure to issue proper invoice (§14 UStG breach) | Administrative fine up to EUR 5,000 per occurrence (§26a UStG) |
| Retention violation | Fine up to EUR 1,000 for specific breaches; up to EUR 30,000 for serious cases (§26a Abs. 1 UStG) |
| Non-compliant invoice → input VAT deduction denied | Buyer may lose right to deduct input VAT until a corrected compliant invoice is received |
| Estimated tax assessment | Tax authority may estimate turnover and VAT liability if records are insufficient |
| GoBD non-compliance | May lead to rejection of bookkeeping in tax audit (Betriebsprüfung) and estimated assessment with safety margins |
| Repeated/wilful violations | Potential referral for criminal investigation (Steuerhinterziehung under §370 AO for deliberate cases) |

## Section 10 -- Interaction with Tax Skills

### VAT Return Integration

- E-invoices provide the data basis for the monthly/quarterly Umsatzsteuer-Voranmeldung (advance VAT return) via ELSTER
- Properly archived e-invoices serve as documentary evidence for input VAT deduction claims
- Non-compliant invoices (missing mandatory fields) may result in denied input VAT deduction until corrected
- The BMF has indicated plans for future pre-filled VAT returns based on e-invoice data, aligned with the EU ViDA initiative

### Income Tax Integration

- For Einzelunternehmer (sole proprietors) and Freiberufler (freelancers), e-invoice revenue data feeds into the Einkommensteuer return (Anlage S or Anlage G)
- EÜR (Einnahmenüberschussrechnung -- cash-basis accounting) practitioners must ensure e-invoice dates align with payment dates for revenue recognition
- Bilanzierung (accrual accounting) practitioners recognise revenue at invoice date

### Intra-EU Reporting

- Intra-EU supplies reported via Zusammenfassende Meldung (recapitulative statement) must reconcile with e-invoices issued with tax category K (intra-community supply)
- Buyer VAT IDs on e-invoices (BT-48) must match VIES-validated numbers

### GoBD and Tax Audit

- Tax auditors may request Z1 (direct system access), Z2 (data export in GDPdU/IDEA format), or Z3 (data carrier) access to archived e-invoices
- Verfahrensdokumentation must describe the e-invoice workflow from receipt to archiving
- Failure to produce compliant archives during Betriebsprüfung can trigger estimated assessments with penalty surcharges (Zuschläge)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
