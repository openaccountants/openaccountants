---
name: belgium-einvoice
description: "Belgian structured e-invoicing for 2026: the B2B obligation in force since 1 January 2026 under VAT Code art. 53 § 2bis (Law of 6 February 2024, amended by the Law of 10 February 2026), the Royal Decree of 8 July 2025 (Peppol BIS in UBL over the Peppol network, rounding, fines), who must send and who must be able to receive, exclusions (art. 44 exempt businesses, flat-rate farmers, businesses not established in Belgium), self-billing, credit notes, the EUR 1,500 / 3,000 / 5,000 fines, the three-month tolerance in early 2026 and the self-billing tolerance to 30 June 2026, B2G invoicing through Mercurius, Peppol BIS Billing 3.0 fields and validation, VAT computed per VAT category, archiving for seven years, and the 120% cost deduction for small businesses. Trigger on: Peppol Belgium, e-invoicing Belgium 2026, e-facturatie, facturation électronique, structured invoice Belgium, Mercurius, Peppol BIS, UBL Belgium, B2B e-invoice fine. Out of scope: VAT rates and returns (be-vat-return, be-vat-return), bookkeeping (belgium-bookkeeping)."
version: 1.1
jurisdiction: BE
category: invoicing
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Einvoice

Rules below are those in force in 2026. Each line names its source; the full list is in Sources at the end. The laws were read in the Belgisch Staatsblad (ejustice.just.fgov.be) and the administration's e-invoicing site (efactuur.belgium.be / einvoice.belgium.be) on 2026-10-30.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Belgium (Koninkrijk België / Royaume de Belgique) |
| Currency | EUR |
| E-invoicing system | Peppol network (B2B and B2G); Mercurius for invoices to public bodies (B2G) |
| Authority | FOD Financiën / SPF Finances (tax rules); FOD BOSA is the Belgian Peppol Authority (since 1 January 2016) |
| B2B legal basis | VAT Code (WBTW) art. 53 § 2bis, inserted by the Law of 6 February 2024 (Staatsblad 20 February 2024), in force 1 January 2026 (art. 6) |
| Amendments | Law of 10 February 2026, art. 4 (customer that cannot receive; EU norm wording), in force on publication, 20 February 2026 (art. 22); art. 6 of the same law repealed the clause in art. 6 of the Law of 6 February 2024 that made its entry into force depend on an EU Council authorisation under art. 395 of Directive 2006/112/EC |
| Format and network rules | Royal Decree of 8 July 2025 (Staatsblad 14 July 2025): KB nr. 1 art. 13ter and 13quater (Peppol BIS in UBL, Peppol network), KB nr. 8 (rounding), KB nr. 44 (fines), in force 1 January 2026 (art. 6) |
| B2G legal basis | Royal Decree of 9 March 2022 (public procurement): e-invoices required for contracts published after 1 March 2024 |
| Status in 2026 | In force since 1 January 2026. Fines not applied in the first three months of 2026 to businesses that took timely steps; self-billing tolerance to 30 June 2026 |
| Tax incentive | 120% deduction of e-invoicing software subscription and advice costs for small companies and the self-employed, taxable periods 2024 to 2027 (WIB 92 art. 64ter) |

## Section 2 -- Mandate Scope

### Who must comply

- **Who must send.** A taxable person established in Belgium issues a structured electronic invoice to its customer for supplies of goods and services that are not exempt under art. 44, where the customer must give its Belgian VAT number for that supply (WBTW art. 53 § 2bis, first paragraph). This covers VAT group members using their sub-number.
- **Excluded senders.** Taxable persons under the flat-rate scheme of art. 56, and bankrupt taxable persons for the activity for which they were declared bankrupt (art. 53 § 2bis, first paragraph). The flat-rate scheme ends at the latest on 1 January 2028 (efactuur.belgium.be, "Voor wie wordt e-facturatie verplicht?").
- **Businesses that make only art. 44 exempt supplies** need not send and need not be able to receive structured e-invoices (same page).
- **Not established in Belgium.** A taxable person without an establishment in Belgium is outside the obligation, even if it has a Belgian VAT number, both for sending and for receiving (same page). The Law of 10 February 2026 removed the reference to the VAT number of art. 50 § 1, 3° from art. 53 § 2bis (art. 4, 1°), so the obligation now turns on the customer's VAT number under art. 50 § 1, 1° (or a VAT group sub-number).
- **Small-business exemption.** Businesses under the small-business exemption (turnover up to EUR 25,000) are covered (efactuur.belgium.be FAQ, question 2). See [be-vat-return](be-vat-return.md).
- **Farmers under the special agricultural scheme** are covered at least for receiving B2B invoices (same FAQ).
- **Customers.** Every Belgian VAT-identified recipient of a structured e-invoice must be able to receive it in the format in which it was issued, itself or through a third party (art. 53 § 2bis, last paragraph of the 2024 text).
- **Customer that cannot receive.** If the recipient cannot receive a structured e-invoice for technical reasons, the supplier need not issue one, but must still issue an ordinary invoice (art. 53 § 2bis, paragraph added by the Law of 10 February 2026, art. 4, 4°).
- **B2C.** Invoices to private customers are outside the obligation. A business that works only for private customers must still be able to receive structured e-invoices from its suppliers (efactuur.belgium.be, "Voor wie wordt e-facturatie verplicht?").
- **Voluntary use.** Anyone may use structured e-invoices where not required, if both parties agree. Registration on Peppol counts as agreement to receive (efactuur.belgium.be FAQ, question 9; summary table on the "Voor wie" page).

### Transaction scope

- **In scope.** Supplies of goods and services not exempt under art. 44 to a Belgian VAT-registered customer, and invoices for advance payments that make VAT due before the supply (art. 53 § 2bis, first paragraph, 2°).
- **Credit notes.** Any document that changes and refers specifically to the original invoice counts as a structured e-invoice and is issued in the same format (art. 53 § 2bis, third paragraph).
- **Out of scope.** Art. 44 exempt supplies; B2C; cross-border and other situations outside the B2B / B2G scope (efactuur.belgium.be summary table). Intra-EU invoicing is planned to follow from 2030 under the EU VAT in the Digital Age package (einvoice.belgium.be).
- **Invoices issued from 1 January 2026.** Every in-scope invoice drawn up, issued or sent from 1 January 2026 is a structured e-invoice, whether the supply took place before or after that date (efactuur.belgium.be FAQ, question 14).
- **Registered cash systems.** A structured e-invoice does not replace the receipt from a registered cash system; where the customer is a business, both are issued (same FAQ, question 16).

### Timeline

**Timeline**

| Date | Milestone | Source |
| --- | --- | --- |
| 1 January 2016 | FOD BOSA acts as the Belgian Peppol Authority | efactuur.belgium.be, Peppol FAQ, question 8 |
| 1 January 2024 | 120% cost deduction applies from assessment year 2025 (periods starting from 1 January 2024) | Law of 6 February 2024, art. 6 |
| 20 February 2024 | Law of 6 February 2024 published | Staatsblad |
| 1 March 2024 | E-invoicing compulsory for public contracts published after this date | efactuur.belgium.be, "Voor wie" |
| 1 January 2025 | Investment deduction for digital investments rises to 20% (sole traders and SMEs; for companies only small companies, Law of 18 December 2025 art. 32 and 33) | efactuur.belgium.be, "Fiscale stimulansen" |
| 14 July 2025 | Royal Decree of 8 July 2025 published | Staatsblad |
| 1 January 2026 | B2B obligation, KB nr. 1 art. 13ter / 13quater and the KB nr. 44 fine in force | Law of 6 February 2024 art. 6; KB 8 July 2025 art. 6 |
| 1 January to 31 March 2026 | Tolerance: no fines for businesses that took timely and reasonable steps | einvoice.belgium.be, news item on the tolerance period |
| 20 February 2026 | Law of 10 February 2026 art. 4 in force (customer unable to receive) | Law of 10 February 2026, art. 22 |
| 30 June 2026 | End of the self-billing tolerance | efactuur.belgium.be FAQ, question 23 |
| 2028 | Near real-time e-reporting of invoice data to the administration, between Belgian VAT-registered businesses: in the federal coalition agreement with timing 2028, not yet in Belgian law; it will replace the annual client listing | einvoice.belgium.be, FAQ on e-reporting, question 1 |
| 1 January 2028 | 120% deduction provision repealed for assessment year 2029 onward | Law of 6 February 2024, art. 6 |
| 1 July 2030 | Latest date for Belgian law to bring in reporting of intra-EU transactions under the ViDA package | einvoice.belgium.be, FAQ on e-reporting, question 3 |

## Section 3 -- Technical Format

### Standard and syntax

**Standard and syntax**

| Component | Value | Source |
| --- | --- | --- |
| Default format | The European e-invoicing norm and its syntaxes under Directive 2014/55/EU, as set out in the Peppol BIS format in the UBL version | KB nr. 1 art. 13ter, first paragraph, 1° |
| Default network | The Peppol transmission network | KB nr. 1 art. 13ter, first paragraph, 2° |
| Other format by agreement | Allowed if both parties agree and the format meets the European norm and its syntaxes; it may then be sent by another digital route | KB nr. 1 art. 13ter, second paragraph; WBTW art. 53 § 2bis, second paragraph |
| Technical means | A business bound by the obligation must have the technical means to issue and receive Peppol BIS invoices over Peppol, even where it agrees another format with a customer | KB nr. 1 art. 13quater |
| Business specification | Peppol BIS Billing 3.0 (version 3.0.21 read), an application of EN 16931 | docs.peppol.eu; efactuur.belgium.be Peppol FAQ |
| Attachments | Sent in the same channel, inside the UBL file or by link; allowed types pdf, png, jpg, csv, xlsx, ods (xml by agreement) | efactuur.belgium.be FAQ, questions 19 to 21 |
| PDF copy | Optional; the customer cannot demand it or refuse the invoice for lack of it | efactuur.belgium.be FAQ, questions 11 and 12 |

### Key Peppol identifiers

**Key Peppol identifiers**

| Field | Value | Source |
| --- | --- | --- |
| CustomizationID (specification identifier) | `urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0` | Peppol BIS Billing 3.0, rule PEPPOL-EN16931-R004 |
| ProfileID (business process) | `urn:fdc:peppol.eu:2017:poacc:billing:01:1.0` | Peppol BIS Billing 3.0 |
| Belgian participant identifier | Enterprise number (KBO / BCE) with scheme ID 0208; service providers must register every Belgian business at least under it | efactuur.belgium.be Peppol FAQ, question 4 |
| Format of 0208 identifier | 10 digits passing a modulo-97 check | Peppol BIS Billing 3.0, rule PEPPOL-COMMON-R043 |
| Other identifiers (VAT number, GLN, IBAN) | Optional, by agreement between the parties | efactuur.belgium.be Peppol FAQ, question 4 |

### Document types

- **Invoice type codes** allowed in the billing profile include 380 (commercial invoice). **Credit note type codes** include 381 (Peppol BIS Billing 3.0, rules PEPPOL-EN16931-P0100 and P0101).
- UBL root elements are `Invoice` and `CreditNote` in the OASIS UBL 2.1 namespaces; a UBL invoice should not carry a UBLVersionID other than 2.1 (Peppol BIS Billing 3.0).

## Section 4 -- Mandatory Fields

### Peppol BIS Billing 3.0 key fields

**Peppol BIS Billing 3.0 key fields**

| Field | UBL element | Rule |
| --- | --- | --- |
| Specification identifier | `cbc:CustomizationID` | Must begin with the Peppol billing 3.0 value (R004) |
| Business process | `cbc:ProfileID` | Must be provided (R001) and approved (R007) |
| Invoice number | `cbc:ID` | Required by EN 16931 |
| Issue date | `cbc:IssueDate` | Required |
| Invoice type code | `cbc:InvoiceTypeCode` | Must be a code allowed for the profile, for example 380 (P0100) |
| Currency | `cbc:DocumentCurrencyCode` | Required |
| Buyer reference or order reference | `cbc:BuyerReference` or `cac:OrderReference/cbc:ID` | One of the two must be given (R003) |
| Seller electronic address | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` with `@schemeID` (0208 for a Belgian enterprise number) | Must be provided (R020) |
| Buyer electronic address | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | Must be provided (R010) |
| Seller and buyer name, address, VAT number | `cac:PartyLegalEntity`, `cac:PostalAddress`, `cac:PartyTaxScheme` | Required where EN 16931 requires them |
| Line quantity and net amount | `cbc:InvoicedQuantity` with `@unitCode`, `cbc:LineExtensionAmount` | Line net = quantity x net price + charges - allowances (R120) |
| Line VAT category and rate | `cac:Item/cac:ClassifiedTaxCategory` | Category from UNCL5305; rate required except for category O |
| VAT breakdown | `cac:TaxTotal/cac:TaxSubtotal` | One per VAT category and rate; only one tax total with subtotals (R053) |
| Totals and amount due | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Totals must add up (BR-CO-15, BR-CO-16) |
| Payment means | `cac:PaymentMeans/cbc:PaymentMeansCode` | For example 30 credit transfer, 58 SEPA credit transfer, 59 SEPA direct debit |
| Payee account | `cac:PayeeFinancialAccount/cbc:ID` | IBAN for a transfer |
| No empty elements | All | R008 |

The 2025 version said BuyerReference is always mandatory. The rule is a buyer reference **or** an order reference (R003).

### Peppol VAT category codes (Belgian use)

**Peppol VAT category codes (UNCL5305 subset)**

| Code | Meaning | Belgian use |
| --- | --- | --- |
| S | Standard rate | Any positive Belgian rate (21%, 12%, 6%) |
| Z | Zero rated goods | Zero-rated supplies |
| E | Exempt from tax | Exempt supplies |
| AE | VAT reverse charge | Belgian reverse charge, for example construction work |
| K | VAT exempt for EEA intra-community supply | Intra-EU supplies (outside the Belgian B2B obligation) |
| G | Free export item, tax not charged | Exports |
| O | Services outside scope of tax | Not subject to VAT; VAT amount must be zero |
| L, M | Canary Islands, Ceuta and Melilla taxes | Not used for Belgian supplies |

The rates themselves are in [be-vat-return](be-vat-return.md).

## Section 5 -- Transmission Method

### B2B: Peppol network

**B2B: Peppol network**

| Component | Detail | Source |
| --- | --- | --- |
| Network | Peppol: an open agreement framework and network, compared to a telecom network; participants must at least receive Peppol BIS | efactuur.belgium.be Peppol FAQ |
| Service providers (access points) | Certified Peppol service providers connect businesses to the network; a business cannot register directly | Same, questions on service providers and registration |
| Registration | Through end-user software connected to a service provider; registration under the enterprise number (0208) is contractually required of providers | Same, questions 4 and 5 |
| Lookup | The Peppol directory shows who can receive; search "0208:" plus the enterprise number; it does not show who can send | Same, question 6 |
| Peppol-first | Software should send via Peppol whenever the partner is on Peppol; suppliers need not ask customers for a Peppol ID | Same, question 4; efactuur.belgium.be FAQ, question 15 |
| Customer portals | A customer cannot oblige a supplier to upload invoices to its own portal without the supplier's express agreement | efactuur.belgium.be FAQ, question 18 |
| Delivery time | Usually minutes to a few hours; Peppol does not guarantee real-time delivery; ask the software supplier after one working day of delay | efactuur.belgium.be Peppol FAQ, question 9 |
| Authority | FOD BOSA is the Belgian Peppol Authority | Same, question 8 |

### B2G: Mercurius

**B2G: Mercurius**

| Component | Detail | Source |
| --- | --- | --- |
| Rule | Electronic invoicing compulsory for public contracts published after 1 March 2024, under the Royal Decree of 9 March 2022 | efactuur.belgium.be, "Voor wie" |
| Threshold | As a rule for contracts from EUR 3,000 excluding VAT; buyers may require it below that; federal buyers have required it below EUR 3,000 since 1 March 2024 | Same, footnote 1 |
| Contact | Questions on Mercurius go through the Mercurius contact form of FOD BOSA | einvoice.belgium.be |

### Hermes

The 2025 version described Hermes, a free government platform that converts structured invoices to PDF for recipients that are not ready. No official page on Hermes was found on 2026-10-30; see the "Not yet confirmed" line.

## Section 6 -- Validation Rules

### Peppol validation layers

- **Validation layers.** (1) UBL 2.1 schema; (2) EN 16931 business rules (BR- rules); (3) Peppol BIS Billing 3.0 rules (PEPPOL- rules), marked fatal or warning (Peppol BIS Billing 3.0).
- **Belgian enterprise number** used as an identifier with scheme 0208 must have 10 digits and pass the modulo-97 check (PEPPOL-COMMON-R043, fatal).

### Pre-submission checks

- **Pre-submission checks.** Validate against the UBL schema and the Peppol schematrons; check the customer is on Peppol (directory lookup on 0208); give a buyer reference or order reference; one VAT category per line; one VAT breakdown per category and rate; totals add up; no empty elements; attachments inside the UBL file.

### Common rejection reasons

**Common rejection reasons**

| Reason | Rule |
| --- | --- |
| No buyer reference and no order reference | PEPPOL-EN16931-R003 |
| Seller or buyer electronic address missing | PEPPOL-EN16931-R020 / R010 |
| Wrong specification identifier | PEPPOL-EN16931-R004 |
| Empty XML elements | PEPPOL-EN16931-R008 |
| Invoice type code not allowed for the profile | PEPPOL-EN16931-P0100 |
| Belgian enterprise number in wrong format | PEPPOL-COMMON-R043 |
| Totals do not add up | BR-CO-15, BR-CO-16 |
| Line net amount does not equal quantity x price | PEPPOL-EN16931-R120 |
| Customer not registered on Peppol | Not a schema error: the access point cannot deliver; use another method (Section 9) |

## Section 7 -- Tax Computation Rules

### VAT rates

The 2026 Belgian rates (21%, 12%, 6%, 0%) and what they apply to are in [be-vat-return](be-vat-return.md). The 2025 version's rate table described the 12% rate wrongly and is replaced by that link.

### Rounding rules

- **Per VAT category, not per line.** The VAT breakdown has one entry per combination of VAT category and rate. Its taxable amount is the sum of the line net amounts plus document-level charges less allowances, and its tax amount is that taxable amount times the rate (Peppol BIS Billing 3.0, section 10.4). The invoice total VAT is the sum of the category amounts (section 8.4).
- **Two decimals.** Line net amounts and all document-level amounts are rounded to two decimals; totals built from already rounded amounts are not rounded again (Peppol BIS Billing 3.0, section 9).
- **Belgian rounding rule.** KB nr. 8 allows rounding per item, per rate or otherwise for bookkeeping reasons, but not in a structured e-invoice issued in a format meeting the European norm (KB nr. 8 art. 1, third paragraph, as replaced by the KB of 8 July 2025, art. 4).
- The 2025 version said VAT is calculated and rounded per line. Under the Peppol rules VAT is calculated per category on the summed net amounts.

### Worked example: VAT per category

A supplier invoices two lines at 21%: line 1 net EUR 10.03, line 2 net EUR 10.03. Per category, the taxable amount is 10.03 + 10.03 = 20.06 and the VAT is 20.06 x 21% = 4.2126, rounded to EUR 4.21. Rounding per line would give 2.1063, rounded to 2.11, twice, so EUR 4.22. The e-invoice must show EUR 4.21: rule BR-CO-17 sets the VAT category tax amount at the category taxable amount times the rate, rounded to two decimals. A line-by-line figure of EUR 4.22 breaks that rule.

```oa-check
name: Belgium e-invoice VAT per category versus per line
tolerance: 0.001
inputs:
  line_1_net: 10.03
  line_2_net: 10.03
  rate_pct: 21
steps:
  - category_taxable: line_1_net + line_2_net
  - category_vat: round(pct(category_taxable, rate_pct), 2)
  - per_line_vat: round(pct(line_1_net, rate_pct), 2) + round(pct(line_2_net, rate_pct), 2)
  - difference: per_line_vat - category_vat
expected:
  category_taxable: 20.06
  category_vat: 4.21
  per_line_vat: 4.22
  difference: 0.01
```

### Multi-rate invoice handling

- **Multi-rate invoices.** Each line carries exactly one VAT category code and, except for category O, a rate; one VAT breakdown is given per distinct category and rate (Peppol BIS Billing 3.0, sections 10.4 and on line VAT information).

### Self-billing

- **Self-billing rule.** The customer may issue the structured e-invoice in the supplier's name only with a prior agreement between both parties and an acceptance procedure for each invoice by the supplier (WBTW art. 53 § 2bis, fourth paragraph; efactuur.belgium.be FAQ, question 10).
- **Tolerance.** Where software cannot yet send or receive structured self-billing invoices, the administration is lenient until 30 June 2026 if the business shows its software supplier is implementing it; self-billing invoices may meanwhile be issued another way without sanction for either side (efactuur.belgium.be FAQ, question 23).
- The Peppol self-billing specification and its type code are on the "Not yet confirmed" line.

## Section 8 -- Archiving Requirements

**Archiving requirements**

| Requirement | Detail | Source |
| --- | --- | --- |
| Retention period | 7 years: the Law of 18 December 2025 (art. 97) replaced "ten" by "seven" in VAT Code art. 60 § 3 and § 4, for VAT due from 1 January 2023 (art. 101) | Law of 18 December 2025 |
| What to keep | The structured e-invoice itself, for the full retention period; the archiving rules did not change with the e-invoicing obligation | efactuur.belgium.be FAQ, question 17 |
| Readability | Readability must be guaranteed for the whole period, usually by a PDF or a secure viewer; a PDF must keep the content unchanged | Same |
| Use of the readable copy | Needed for tax audits and for courts, banks, insurers and public bodies that ask for an invoice | Same |
| Bookkeeping link | Invoices are the dated supporting documents for the books; see [belgium-bookkeeping](belgium-bookkeeping.md) | WER art. III.86 (in belgium-bookkeeping) |
| Capital goods | The VAT revision period for buildings and similar services is 15 years, and 25 years for certain lettings (WBTW art. 48 § 2 as replaced by the Law of 10 February 2026, art. 7); how long the related invoices must be kept is on the "Not yet confirmed" line | Law of 10 February 2026 |

The 2025 version gave a 7-year period counted from the year the return was due, and 10 or 15 years for property. The period is 7 years after the Law of 18 December 2025; the starting point of the count and the property periods are on the "Not yet confirmed" line.

## Section 9 -- Penalties for Non-Compliance

### E-invoicing fine (KB nr. 44)

**Fine for not having the technical means to issue and receive structured e-invoices (KB nr. 44 annex, section 2, I.C)**

| Infringement | Fine (EUR) |
| --- | --- |
| First | 1,500 |
| Second | 3,000 |
| Each following | 5,000 |

A second or later infringement counts as such only if the administration finds it at least three months after it found the previous infringement that led to a fine (KB of 8 July 2025, art. 5). The fine applies from 1 January 2026 (art. 6).

### Tolerance in early 2026

- **First three months of 2026.** FOD Financiën did not apply fines for offences under the new obligation in January to March 2026, if the business can show it took timely and reasonable steps to comply. This covered not yet having the technical means to send or receive, and not issuing a structured e-invoice because its own or a third party's system could not yet do so. The invoice still had to be issued another way. Each case is assessed individually, and there is no general postponement (einvoice.belgium.be, "Period of tolerance during the first three months of 2026").
- **Self-billing.** Lenient treatment to 30 June 2026 (Section 7).

### Supplier or customer not ready

- **Supplier not ready.** The customer may in principle refuse the invoice. If it accepts an invoice issued another way (PDF or paper), it keeps its right to deduct VAT; an electronic alternative needs the customer's agreement. The supplier risks a fine (efactuur.belgium.be FAQ, question 7).
- **Customer not ready.** The supplier may use another method; an electronic alternative needs the customer's agreement. The invoice sent that way is legally valid and the supplier meets its invoicing duty; the customer risks a fine. Once the customer is ready, past invoices need not be re-sent (efactuur.belgium.be FAQ, question 8; WBTW art. 53 § 2bis as amended by the Law of 10 February 2026, art. 4, 4°).

### Other VAT penalties

Late or missing invoices, wrong VAT and late returns carry the ordinary VAT fines in KB nr. 41 and KB nr. 44. The amounts are in [be-vat-return](be-vat-return.md).

### Practical consequences

A business that cannot send through Peppol must still invoice by another route and risks the fine above; a business that cannot receive risks the same fine, and its suppliers will send by other means.

## Section 10 -- Interaction with Tax Skills

### E-invoice to VAT return (btw-aangifte / déclaration TVA)

Structured invoice data feeds the periodic VAT return; the grids and deadlines are in [be-vat-return](be-vat-return.md).

- **No e-reporting in 2026.** In the phase in force from 1 January 2026, no invoice data is sent to the administration. Near real-time e-reporting between Belgian VAT-registered businesses is in the federal coalition agreement with timing 2028, but it is not yet in Belgian law; it will replace the annual client listing (einvoice.belgium.be, FAQ on e-reporting, question 1). Reporting of intra-EU transactions under the ViDA package must be in Belgian law by 1 July 2030 at the latest (same FAQ, question 3).

### Income tax incentives

- **120% cost deduction.** Costs (other than depreciation) of invoicing packages to draw up, send and receive structured e-invoices are deductible at 120% (WIB 92 art. 64ter, first paragraph, 1°, restored by the Law of 6 February 2024, art. 4). For companies it applies only to small companies (WIB 92 art. 194octies, as amended by art. 5). It runs for taxable periods 2024 to 2027: in force from assessment year 2025 and repealed from assessment year 2029 (art. 6).
- **What qualifies.** Periodic subscription costs and advice costs specific to preparing for or operating the obligation; the extra price for e-invoicing on an existing subscription qualifies if shown separately on the invoice; depreciation never qualifies (efactuur.belgium.be, "Fiscale stimulansen").
- **Investment deduction.** The investment deduction for digital investments rose to 20% from 1 January 2025 for sole traders and SMEs (same page). For companies, the Law of 18 December 2025 limits the 10-point increase for digital fixed assets to companies that count as small for the assessment year of the investment (WIB 92 art. 201 § 1, 1°/1, inserted by art. 32, 3°), for assets acquired or created from 1 January 2025 (art. 33). See [be-corporate-tax](be-corporate-tax.md) and [be-income-tax](be-income-tax.md).

### Automated bookkeeping

Structured invoices can be booked automatically into the accounting system. Automatic processing is not a legal obligation (efactuur.belgium.be FAQ, question 23). See [belgium-bookkeeping](belgium-bookkeeping.md).

### Purchase order matching

The order reference field (`cac:OrderReference`) links the invoice to the purchase order and satisfies rule R003 where no buyer reference is given.

### Cross-border interoperability

Peppol connects participants in other countries using the same specification. The Belgian obligation covers only domestic B2B; cross-border use needs the customer's agreement, and registration on Peppol counts as agreement (efactuur.belgium.be summary table). EU-wide e-invoicing for intra-EU supplies is planned from 2030 (einvoice.belgium.be).

### Corporate tax (vennootschapsbelasting / impôt des sociétés)

Invoice data supports the accounting profit used in [be-corporate-tax](be-corporate-tax.md). Whether and how FOD Financiën will receive invoice data directly (e-reporting) is on the "Not yet confirmed" line.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Law of 6 February 2024 amending the VAT Code and the Income Tax Code (mandatory e-invoicing), Staatsblad 20 February 2024 | https://www.ejustice.just.fgov.be/eli/wet/2024/02/06/2024001635/staatsblad | 2026-10-30 |
| Royal Decree of 8 July 2025 amending KB nr. 1, 8 and 44 (structured e-invoices), Staatsblad 14 July 2025 | https://www.ejustice.just.fgov.be/eli/besluit/2025/07/08/2025005169/staatsblad | 2026-10-30 |
| Law of 10 February 2026 on various VAT provisions (art. 3 to 7, 22), Staatsblad 20 February 2026 | https://www.ejustice.just.fgov.be/eli/wet/2026/02/10/2026001291/staatsblad | 2026-10-30 |
| Law of 18 December 2025 on various provisions (art. 32 and 33, investment deduction; art. 97 and 101, VAT retention) | https://www.ejustice.just.fgov.be/eli/wet/2025/12/18/2025009647/staatsblad | 2026-10-30 |
| efactuur.belgium.be, FAQ on the B2B obligation | https://efactuur.belgium.be/nl/FAQ/algemene-vragen-b2b | 2026-10-30 |
| efactuur.belgium.be, "Voor wie wordt e-facturatie verplicht?" | https://efactuur.belgium.be/nl/article/voor-wie-wordt-e-facturatie-verplicht | 2026-10-30 |
| efactuur.belgium.be, FAQ on Peppol | https://efactuur.belgium.be/nl/FAQ/algemene-vragen-over-peppol | 2026-10-30 |
| efactuur.belgium.be, "Fiscale stimulansen voor het invoeren van e-facturering" | https://efactuur.belgium.be/nl/article/fiscale-stimulansen-voor-het-invoeren-van-e-facturatie | 2026-10-30 |
| einvoice.belgium.be, "Period of tolerance during the first three months of 2026" | https://einvoice.belgium.be/en/news/period-tolerance-during-first-three-months-2026 | 2026-10-30 |
| einvoice.belgium.be, "Structured electronic invoices between companies are compulsory since 2026" | https://einvoice.belgium.be/en/article/structured-electronic-invoices-between-companies-are-compulsory-2026 | 2026-10-30 |
| einvoice.belgium.be, FAQ "General questions about e-reporting" | https://einvoice.belgium.be/en/FAQ/general-questions-about-e-reporting | 2026-10-30 |
| FOD Financiën, E-facturering (points to efactuur.belgium.be) | https://financien.belgium.be/nl/ondernemingen/btw/e-facturatie | 2026-10-30 |
| OpenPeppol, Peppol BIS Billing 3.0 (version 3.0.21) | https://docs.peppol.eu/poacc/billing/3.0/bis/ | 2026-10-30 |

Not yet confirmed: the consolidated text of VAT Code art. 53 § 2bis and art. 60 (FisconetPlus returned a 502 error page on 2026-10-30, twice, and Justel holds no consolidated text of the VAT Code, so the rules were read in the amending laws); the start date, scope and technical model of e-reporting (the 2025 version's "five-corner" model), which no Belgian law sets yet; the Hermes platform (no official page found); Peppol identifier scheme 9925 for VAT numbers, the AS4 transport profile and the Peppol PKI certificates; the full Peppol document type identifiers for invoice and credit note; the Peppol BIS Self-Billing specification, its version and type code 389; how long invoices for buildings must be kept now that the revision period is 15 or 25 years; the 2025 version's statement that FOD Financiën cross-checks e-invoice data against reported revenue; the 2025 version's list of "Duplicate invoice" and "Unsupported document type" as rejection reasons; the channel Mercurius uses for B2G invoices (the 2025 version said Peppol plus a web portal with track and trace); when the 7-year retention period starts to run; the 2025 version's points that invoices stored outside Belgium must be accessible electronically from within the EU, that Mercurius archives B2G invoices, that CII syntax is accepted through Mercurius, and that Parliament approved the law on 1 February 2024.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
