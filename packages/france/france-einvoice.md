---
name: france-einvoice
description: Use this skill whenever asked about French e-invoicing, facturation électronique, Chorus Pro, Factur-X, Plateforme Agréée (PA), Plateforme de Dématérialisation Partenaire (PDP), Portail Public de Facturation (PPF), e-reporting France, B2B e-invoicing mandate France 2026, lifecycle statuses, or any question about issuing, receiving, validating, or archiving electronic invoices in France. Also trigger when preparing invoices for submission via a certified platform, configuring PA/PDP connectivity, handling e-reporting obligations for B2C or cross-border transactions, or advising on Factur-X profile selection. This skill covers accepted formats (Factur-X, UBL 2.1, CII), the PPF/PA architecture, mandatory fields, validation rules, archiving, penalties, and interaction with French VAT returns. ALWAYS read this skill before touching any French e-invoicing work.
version: 1.0
jurisdiction: FR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# France Einvoice

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | France (République française) |
| Currency | EUR |
| E-invoicing system | Portail Public de Facturation (PPF) + Plateformes Agréées (PA) |
| B2G platform | Chorus Pro (operational since 2017) |
| Accepted formats | Factur-X (EN 16931), UBL 2.1, UN/CEFACT CII |
| Governing body | Direction Générale des Finances Publiques (DGFiP) |
| Platform certification | Agence pour l'Informatique Financière de l'État (AIFE) |
| Key legislation | CGI Art. 289 bis (Loi de Finances 2024, Art. 91); CGI Art. 1737, 1788 D (penalties) |
| Portal URL | https://portail.chorus-pro.gouv.fr (B2G); PPF routing portal (B2B from 2026) |
| B2G mandatory since | 1 January 2020 (all suppliers to public sector) |
| B2B Phase 1 | 1 September 2026 (receive: all; issue: large + mid-size enterprises) |
| B2B Phase 2 | 1 September 2027 (issue: SMEs and micro-enterprises) |
| Current status | B2G fully operational; B2B in preparation -- PA certification in progress |
| Skill version | 1.0 |

### Who Must Comply

**Who Must Comply**

| Scope | Requirement |
| --- | --- |
| B2G | Mandatory for all suppliers to public entities via Chorus Pro since 1 January 2020 |
| B2B (receive) | All VAT-registered businesses in France must receive e-invoices from 1 September 2026 |
| B2B (issue -- Phase 1) | Large enterprises (turnover > EUR 1.5B) and ETI (EUR 250M--1.5B) must issue from 1 September 2026 |
| B2B (issue -- Phase 2) | PME and micro-enterprises must issue from 1 September 2027 |
| B2C | Not subject to e-invoicing mandate, but e-reporting of B2C transaction data is required |
| Cross-border | Not subject to e-invoicing, but e-reporting of cross-border transaction and payment data is required |
| Non-established businesses | If VAT-registered in France without fixed establishment: e-reporting obligations only (no issuance obligation) |
| Fixed establishment in France | Full e-invoicing obligations apply |

### E-Reporting Obligation

- **E-reporting obligation scope** — France mandates e-reporting (transmission des données de transaction) for: B2C domestic transactions (sales to non-VAT-registered persons); Cross-border B2B transactions (intra-EU and exports); Payment data for domestic B2B transactions. E-reporting follows the same phased timeline as e-invoicing issuance.

### Timeline Summary

**Timeline Summary**

| Date | Milestone |
| --- | --- |
| January 2020 | B2G fully mandatory via Chorus Pro |
| 1 September 2026 | All businesses must receive e-invoices; large/ETI must issue; e-reporting starts for large/ETI |
| 1 September 2027 | All remaining businesses (PME/micro) must issue; e-reporting for all |

### Accepted Formats

**Accepted Formats**

| Format | Type | Standard | Preferred Use |
| --- | --- | --- | --- |
| Factur-X | Hybrid (PDF/A-3 + embedded XML) | EN 16931 (Franco-German standard, known as ZUGFeRD in Germany) | Most popular for French businesses; human-readable + machine-processable |
| UBL 2.1 | Pure XML | OASIS UBL, EN 16931 compliant | International interoperability, Peppol |
| UN/CEFACT CII | Pure XML | UN/CEFACT Cross-Industry Invoice, EN 16931 compliant | Chorus Pro native format |

### Factur-X Profiles

**Factur-X Profiles**

| Profile | Complexity | Use Case |
| --- | --- | --- |
| Minimum | Very low | Basic compliance -- invoice reference and totals only |
| Basic WL | Low | Standard invoices without line detail |
| Basic | Medium | Standard invoices with line items |
| EN 16931 (Comfort) | High | Full EN 16931 compliance |
| Extended | Very high | Additional business data beyond EN 16931 |

- **Recommended profile for B2B compliance** — For B2B mandate compliance, at least the Basic profile is recommended. The EN 16931 profile ensures full European standard compliance.

### Key Technical Parameters

**Key Technical Parameters**

| Parameter | Value |
| --- | --- |
| Factur-X version | 1.0.06 (current) |
| PDF standard | PDF/A-3 |
| XML attachment name | `factur-x.xml` (embedded in PDF) |
| UBL namespace | `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2` |
| CII namespace | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` |
| Character encoding | UTF-8 |
| CIUS | French CIUS based on EN 16931 (AFNOR specifications) |

### Core Invoice Fields (EN 16931 Business Terms)

**Core Invoice Fields (EN 16931 Business Terms)**

| BT Code | Field | Required |
| --- | --- | --- |
| BT-1 | Invoice number | Yes |
| BT-2 | Invoice issue date | Yes |
| BT-3 | Invoice type code | Yes |
| BT-5 | Invoice currency code (EUR for domestic) | Yes |
| BT-6 | VAT accounting currency code | Yes (if different from BT-5) |
| BT-9 | Payment due date | Yes |
| BT-10 | Buyer reference | Yes (mandatory in France) |
| BT-24 | Specification identifier (EN 16931 CIUS) | Yes |
| BT-27 | Seller name | Yes |
| BT-29 | Seller country code | Yes |
| BT-30 | Seller legal registration identifier (SIREN) | Yes |
| BT-31 | Seller VAT identifier (FR + 11 digits) | Yes |
| BT-34 | Seller electronic address (SIRET or Peppol ID) | Yes |
| BT-44 | Buyer name | Yes |
| BT-46 | Buyer country code | Yes |
| BT-47 | Buyer legal registration identifier (SIREN) | Yes |
| BT-48 | Buyer VAT identifier | Yes |
| BT-49 | Buyer electronic address (SIRET) | Yes |

### France-Specific Additional Fields

**France-Specific Additional Fields**

| Field | Description | Required |
| --- | --- | --- |
| SIREN / SIRET | Legal entity identification (9/14 digits) | Yes (seller and buyer) |
| Buyer reference (BT-10) | Required for all French invoices; serves as routing reference | Yes |
| Invoice lifecycle status | Deposited / Received / Accepted / Rejected / Paid | Managed by PA/PPF |
| Payment mention | "TVA acquittée sur les débits" or similar as applicable | Conditional |
| Mention obligatoire | Legal mentions required by CGI (e.g., "Autoliquidation" for reverse charge) | Conditional |

### Architecture Overview

The French system uses a Y-model:

1. **Seller** → issues invoice via their PA (Plateforme Agréée)
2. **Seller's PA** → transmits invoice to **Buyer's PA** (interoperability required)
3. Both PAs → report invoice data and lifecycle statuses to the **PPF** (Portail Public de Facturation)
4. **PPF** → aggregates data for DGFiP tax reporting

The PPF no longer handles direct invoice exchange. It serves as: (a) a central business directory for routing, (b) a data concentrator for tax authorities, and (c) a free fall-back platform for businesses without a commercial PA.

### Platforms

**Platforms**

| Platform | Role |
| --- | --- |
| PPF (Portail Public de Facturation) | Central directory, tax data aggregation, free fall-back |
| PA (Plateforme Agréée) | Certified private platform for invoice exchange; formerly PDP |
| Chorus Pro | Remains the reference platform for B2G invoicing from 2026 onward |

### Chorus Pro (B2G) Transmission

**Chorus Pro (B2G) Transmission**

| Method | Detail |
| --- | --- |
| Web portal | Manual upload via portail.chorus-pro.gouv.fr |
| API (PISTE) | REST API via https://api.piste.gouv.fr/cpro/ with OAuth2 authentication |
| EDI | Structured data exchange for high-volume senders |
| Peppol | Via Peppol Access Point connected to Chorus Pro |

### Invoice Lifecycle Statuses

**Invoice Lifecycle Statuses**

| Status | Description |
| --- | --- |
| Deposée (Deposited) | Invoice submitted by seller to PA |
| Reçue (Received) | Invoice delivered to buyer's PA |
| Acceptée (Accepted) | Buyer accepts the invoice |
| Refusée (Rejected) | Buyer rejects the invoice (with reason) |
| Payée (Paid) | Buyer confirms full payment |
| En litige (Disputed) | Invoice under dispute |

### Pre-Submission Validation

**Pre-Submission Validation**

| Check | Description |
| --- | --- |
| Schema validation | XML must conform to Factur-X, UBL 2.1, or CII schema |
| SIREN/SIRET validation | Seller and buyer identifiers verified against INSEE database |
| VAT number format | Must follow French format: FR + 2 check digits + 9-digit SIREN |
| Mandatory field completeness | All required BT fields must be populated |
| Tax calculation consistency | Line totals must reconcile with summary totals |
| Profile conformance | Factur-X XML must match declared profile level |

### Common Rejection Reasons

**Common Rejection Reasons**

| Issue | Resolution |
| --- | --- |
| Missing buyer reference (BT-10) | Always populate -- mandatory in French context |
| Invalid SIRET | Verify against INSEE Sirene database |
| Tax calculation mismatch | Ensure line-level VAT sums match document-level totals |
| Unsupported Factur-X profile | Use at least Basic profile for B2B compliance |
| Missing legal mentions | Include required CGI mentions (auto-liquidation, TVA non applicable Art. 293B, etc.) |
| Duplicate invoice | Check invoice numbering is sequential and unique per tax year |

### VAT Rates (2025/2026)

**VAT Rates (2025/2026)**

| Rate | Application |
| --- | --- |
| 20% | Standard rate (taux normal) |
| 10% | Intermediate rate (taux intermédiaire) -- renovation, transport, restaurants |
| 5.5% | Reduced rate (taux réduit) -- essential food, books, energy |
| 2.1% | Super-reduced rate (taux particulier) -- newspapers, pharmaceuticals |
| 0% | Exempt / non-taxable (with legal mention required) |

### Rounding

- **VAT line rounding rule** — Compute VAT per line: HT × rate, round to 2 decimal places. Document-level totals must equal sum of line-level amounts. Standard arithmetic rounding (banker's rounding not required but accepted). Tolerance: document-level and sum-of-lines totals must match within EUR 0.01 per VAT rate group.

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling** — Each VAT rate must have a separate tax subtotal group (BG-23 in EN 16931). The invoice must clearly distinguish between taxable, exempt, and reverse-charge amounts. Reverse charge (auto-liquidation) requires explicit mention and rate = 0% with appropriate category code.

### Discount and Charge Handling

- **Discount and charge handling** — Document-level allowances/charges (BG-20, BG-21) affect the total taxable base. Line-level allowances (BG-27, BG-28) must be reflected in the line net amount. Both must specify the applicable VAT category.

## Section 8 -- Archiving Requirements

**Section 8 -- Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention period | 6 years for tax purposes (Art. L102 B, Livre des Procédures Fiscales); 10 years for commercial purposes (Code de Commerce) |
| Format | Original electronic format (XML or PDF/A-3 with embedded XML) |
| Integrity | Tamper-proof storage with traceable access logs |
| Authenticity | Guaranteed by: qualified electronic signature, EDI with audit trail, or internal controls (piste d'audit fiable -- PAF) |
| Storage location | France or EU member state with reciprocal access agreement |
| Audit access | Full read access must be available to tax authorities on demand |
| PA obligation | Certified platforms must provide compliant archiving services |

## Section 9 -- Penalties for Non-Compliance

**Section 9 -- Penalties for Non-Compliance**

| Violation | Penalty | Cap |
| --- | --- | --- |
| Failure to issue compliant e-invoice | EUR 50 per invoice | EUR 15,000 per calendar year |
| Failure to transmit e-reporting data (transaction/payment) | EUR 500 per missing transmission | EUR 15,000 per calendar year |
| Failure to designate a PA for receiving invoices | EUR 500 after 3-month formal notice; EUR 1,000 after each subsequent 3-month period | No annual cap |
| Issuing fraudulent invoices | 50% of invoice amount | EUR 375,000 |
| Total failure to issue any invoice | Up to EUR 375,000 (first offence); EUR 750,000 (repeat) | -- |
| PA platform non-compliance | EUR 15 per invoice (failure to transmit/receive) | EUR 45,000 per calendar year |
| PA failure to transmit e-reporting | EUR 750 per transmission | EUR 100,000 per calendar year |

### VAT Return Integration

- **VAT Return Integration** — E-invoicing data transmitted to the PPF will progressively feed into pre-filled VAT returns (CA3 monthly/quarterly). The DGFiP aims to use aggregated e-invoicing + e-reporting data to pre-populate TVA declarations. Domestic B2B: invoice data flows directly from PA → PPF → DGFiP VAT systems. B2C and cross-border: e-reporting data supplements the invoice data for complete VAT return coverage. Invoice lifecycle statuses (particularly "paid" status) enable future pre-filling of payment-related VAT fields.

### Income Tax Integration

- **Income Tax Integration** — For auto-entrepreneurs (micro-BIC / micro-BNC), e-invoicing data contributes to pre-filled revenue declarations. Professional income from invoices issued via PA feeds into the BIC/BNC professional income return (2031/2035).

### Chorus Pro and Public Accounting

- **Chorus Pro and Public Accounting** — B2G invoices in Chorus Pro integrate with public-sector accounting systems (Hélios for local government, Chorus for central government). Invoice lifecycle statuses in Chorus Pro directly affect cash flow planning and payment tracking for public contracts.

### Cross-Border Considerations

- **Cross-Border Considerations** — E-reporting obligations for intra-EU supplies require reporting of buyer VAT ID, invoice amount, and applicable exemption. Import VAT (auto-liquidation since 1 January 2022 for all importers) is reported separately but related invoice data flows through e-reporting.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert-comptable, commissaire aux comptes, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

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
