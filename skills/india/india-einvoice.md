---
name: india-einvoice
description: Use this skill whenever asked about India GST e-invoicing, Invoice Registration Portal (IRP), IRN generation, e-invoice JSON schema, NIC portal, GST INV-01 format, e-invoice threshold, B2B invoice reporting under GST, QR code on invoices, GSTR-1 auto-population, e-way bill integration with e-invoice, or any question about generating, validating, or troubleshooting Indian e-invoices. Also trigger when advising on e-invoice compliance for businesses crossing Rs 5 crore turnover, configuring ERP/billing software for IRP integration, or handling IRP rejections. ALWAYS read this skill before touching any India e-invoice work.
version: 1.0
jurisdiction: IN
tax_year: 2026
last_updated: 2026-10-17
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# India GST E-Invoicing (IRN under Rule 48(4))

This Guide covers GST e-invoicing in India: who must obtain an Invoice Reference Number (IRN) before issuing an invoice, who is excluded, what the invoice must then show, and what happens when an invoice is issued without one. Figures are for tax year 2026. GST is not year-based, so this Guide states the rules in force on 17 October 2026 and the date each one started. The law is rule 48(4) to (6) of the Central Goods and Services Tax Rules, 2017 (CGST Rules) and Notification No. 13/2020-Central Tax as amended. The 57th GST Council meeting of 8 October 2026 recommended extending e-invoicing to more transactions; that is a proposal, not law (see Section 2).

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | India (Republic of India) |
| Currency | INR (Indian Rupee) |
| E-invoicing system | Invoice Reference Number (IRN) obtained by uploading invoice data to the Common Goods and Services Tax Electronic Portal (the Invoice Registration Portal, IRP) |
| Who runs the portals | Goods and Services Tax Network (GSTN); the e-invoice websites listed in Notification No. 69/2019-Central Tax are "managed by the Goods and Services Tax Network" |
| Key law | Rule 48(4), (5) and (6) of the CGST Rules; Notification No. 13/2020-Central Tax of 21 March 2020 as amended (who must comply) |
| Invoice format | FORM GST INV-01 particulars (rule 48(4)); the IRP uses a JSON schema published by GSTN (see Section 3) |
| Current threshold | Aggregate turnover in any preceding financial year from 2017-18 onwards exceeding five crore rupees, from 1 August 2023 (Section 2) |
| E-invoicing start | 1 October 2020 (paragraph 2 of Notification No. 13/2020-Central Tax) |
| Portal websites | The e-invoice websites listed in [Notification No. 69/2019-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-69-central-tax-english-2019.pdf) |

### Turnover Phase-In Timeline

Each row is the amendment to Notification No. 13/2020-Central Tax that set the threshold. The test is aggregate turnover "exceeding" the amount, so a business at exactly the amount is not caught by that row.

| Aggregate turnover exceeding | Mandatory from | Notification |
| --- | --- | --- |
| five hundred crore rupees | 1 October 2020 | [61/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-61-central-tax-english-2020.pdf) (start date in [13/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-13-central-tax-english-2020.pdf)) |
| one hundred crore rupees | 1 January 2021 | [88/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-88-central-tax-english-2020.pdf) |
| fifty crore rupees | 1 April 2021 | [05/2021-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-05-central-tax-english-2021.pdf) |
| twenty crore rupees | 1 April 2022 | [01/2022-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/nn_01_2022_english.pdf) |
| ten crore rupees | 1 October 2022 | [17/2022-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/17-2022-ct-eng_1_1.pdf) |
| five crore rupees | 1 August 2023 | [10/2023-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf) |

The note printed under Notification No. 10/2023-Central Tax says the principal notification "was last amended vide notification No. 17/2022-Central Tax". Check the CBIC notification pages for any later amendment of Notification No. 13/2020-Central Tax.

## Section 2: Mandate Scope

### Who Must Comply

- **Compliance obligation.** A registered person whose aggregate turnover in any preceding financial year from 2017-18 onwards exceeds five crore rupees must prepare invoices "and other prescribed documents" under rule 48(4) for supplies of goods or services or both to a registered person, and for exports. Source: [Notification No. 13/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-13-central-tax-english-2020.pdf), with "any preceding financial year from 2017-18 onwards" and "or for exports" inserted by [Notification No. 70/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf), and the five crore rupees figure from [Notification No. 10/2023-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf) from 1 August 2023.
- **Any preceding year counts.** The test looks at every financial year from 2017-18 up to the year before the current one. One year above the threshold is enough. A later fall in turnover does not take the business out, because the test still finds that earlier year.
- **Aggregate turnover** means the value of all taxable supplies (excluding inward supplies taxed under reverse charge), exempt supplies, exports and inter-State supplies of persons with the same PAN, computed on an all-India basis, excluding central tax, State tax, Union territory tax, integrated tax and cess. Source: section 2(6) of the [CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter1/section2_v1.00.html). So all GSTINs under one PAN are added together.
- **Coverage.** Supplies to registered persons (B2B) and exports. Supplies to unregistered persons (B2C) are outside rule 48(4); see the B2C QR code rule below.
- Rule 48(4) also lets "the Commissioner ... by notification, exempt a person or a class of registered persons from issuance of invoice under this sub-rule for a specified period" ([rule 48](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule48_v1.00.html)).

### Document Types Covered

Notification No. 13/2020-Central Tax covers the "invoice and other prescribed documents". The IRP schema uses these document type codes (from the earlier version of this Guide; the schema itself could not be read for this Guide):

| Document | IRP Document Type Code |
| --- | --- |
| Tax Invoice | INV |
| Credit Note | CRN |
| Debit Note | DBN |

### Exempted Categories

These registered persons are outside Notification No. 13/2020-Central Tax whatever their turnover:

- An insurer, a banking company, or a financial institution including a non-banking financial company (rule 54(2)).
- A goods transport agency supplying services of transporting goods by road in a goods carriage (rule 54(3)).
- A supplier of passenger transportation service (rule 54(4)).
- A registered person supplying services by way of admission to exhibition of cinematograph films in multiplex screens (rule 54(4A)). Rule 54(4A) adds that a supplier "in a screen other than multiplex screens may, at his option, follow the above procedure"; whether that brings a single-screen cinema inside the exclusion is not settled.
- A Special Economic Zone unit (inserted by [Notification No. 61/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-61-central-tax-english-2020.pdf)). This excludes the SEZ unit as a supplier. It does not exclude other suppliers who sell to an SEZ unit.
- A government department and a local authority (inserted by [Notification No. 23/2021-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-23-central-tax-english-2021.pdf)).

The rule 54 classes are listed in [rule 54 of the CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule54_v1.00.html); Notification No. 13/2020-Central Tax excludes the persons "referred to in sub-rules (2), (3), (4) and (4A) of rule 54".

**Declaration on invoices of excluded persons.** Rule 46(s) requires this declaration 'in all cases where an invoice is issued, other than in the manner so specified under the said sub-rule (4) of rule 48, by the taxpayer having aggregate turnover in any preceding financial year from 2017-18 onwards more than the aggregate turnover as notified'. The declaration reads: "I/We hereby declare that though our aggregate turnover in any preceding financial year from 2017-18 onwards is more than the aggregate turnover notified under sub-rule (4) of rule 48, we are not required to prepare an invoice in terms of the provisions of the said sub-rule." It clearly covers the excluded classes above. The rule text does not settle whether it also covers B2C invoices of a taxpayer that e-invoices its B2B supplies; ask a practitioner. Source: rule 46(s) of the [CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html).

### B2C invoices: Dynamic QR code (a different rule)

A B2C invoice issued by a registered person whose aggregate turnover in any preceding financial year from 2017-18 onwards exceeds five hundred crore rupees must carry a Dynamic Quick Response (QR) code. Excluded: the persons in rule 54(2), (3), (4) and (4A), and a registered person referred to in section 14 of the Integrated Goods and Services Tax Act, 2017. Where the supplier makes a Dynamic QR code available to the recipient through a digital display, a B2C invoice "containing cross-reference of the payment using a Dynamic Quick Response (QR) code, shall be deemed to be having Quick Response (QR) code". Source: [Notification No. 14/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-14-central-tax-english-2020.pdf), with the turnover test and the start date of 1 December 2020 set by [Notification No. 71/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-71-central-tax-english-2020.pdf). This QR code is not an IRN; B2C invoices are not reported to the IRP under rule 48(4).

### Time Limit for Reporting

No allowed official page states a time limit for obtaining an IRN after the invoice date. GSTN has announced reporting limits by advisory on the GST portals, which could not be read for this Guide. Rule 48(4) itself requires the invoice to be prepared "after obtaining an Invoice Reference Number", so the IRN comes first and the invoice is issued with it, inside the time for issuing an invoice under section 31 of the CGST Act (for goods, "before or at the time of" removal or delivery). Before advising on a late IRN, check the current GSTN advisory on the e-invoice portal.

### Pending: 57th GST Council recommendation (not law)

On 8 October 2026 the 57th GST Council recommended "extending e-invoicing to domestic supplies received from an unregistered person where the tax is payable under reverse charge mechanism, as well as to the import of services" for taxpayers above a stated turnover. Source: [57th GST Council press release](https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf). It applies only once the CGST Rules or the notifications are amended and notified. On 17 October 2026 it is not in force.

## Section 3: Technical Format

The schema, field names, codes, limits, API and portal behaviour in Sections 3 to 7 come from the earlier version of this Guide and from GSTN's published schema and API documents. The GSTN e-invoice and GST portals refuse the fetcher this Guide was checked with, so none of this technical detail was checked against an official page; statements there that link a rule, notification or the Council release were checked. Before building or fixing an integration, confirm every field, code and limit against the schema and API documents on the e-invoice portal.

### Schema Specification

| Aspect | Detail |
| --- | --- |
| Format | JSON (not XML, not UBL) |
| Legal form | Particulars of FORM GST INV-01 (rule 48(4)) |
| Character encoding | UTF-8 |
| Date format | DD/MM/YYYY |
| Decimal precision | 2 decimal places for amounts |
| Schema and API version | Check the version currently published by GSTN |

### JSON Structure (Top-Level Objects)

~~~json
{
  "Version": "1.1",
  "TranDtls": { },
  "DocDtls": { },
  "SellerDtls": { },
  "BuyerDtls": { },
  "DispDtls": { },
  "ShipDtls": { },
  "ItemList": [ ],
  "ValDtls": { },
  "PayDtls": { },
  "RefDtls": { },
  "AddlDocDtls": [ ],
  "ExpDtls": { },
  "EwbDtls": { }
}
~~~

### IRN Generation Algorithm

- **IRN generation.** The IRP, not the taxpayer, returns the IRN after it validates the upload. Per GSTN's documents it is a 64-character hash built from the supplier GSTIN, the financial year, the document type and the document number. Because the IRN is derived from those fields, the same document type and number cannot be registered twice in one financial year by the same GSTIN.

## Section 4: Mandatory Fields

Field names below are the GSTN JSON schema names (not checked; see Section 3).

### Transaction Details (TranDtls)

| Field Path | Description | Values |
| --- | --- | --- |
| TranDtls.TaxSch | Tax scheme | "GST" |
| TranDtls.SupTyp | Supply type | B2B, SEZWP, SEZWOP, EXPWP, EXPWOP, DEXP |
| TranDtls.RegRev | Reverse charge | Y / N |
| TranDtls.IgstOnIntra | IGST on intra-State supply | Y / N |

### Document Details (DocDtls)

| Field Path | Description | Constraints |
| --- | --- | --- |
| DocDtls.Typ | Document type | INV, CRN, DBN |
| DocDtls.No | Document number | Rule 46(b): "a consecutive serial number not exceeding sixteen characters", letters, numerals, hyphen or slash, unique for a financial year |
| DocDtls.Dt | Document date | DD/MM/YYYY |

The sixteen-character limit is in [rule 46(b) of the CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html).

### Seller Details (SellerDtls)

| Field Path | Description |
| --- | --- |
| SellerDtls.Gstin | 15-character GSTIN |
| SellerDtls.LglNm | Legal name (as per PAN) |
| SellerDtls.Addr1 | Address line 1 |
| SellerDtls.Loc | City or location |
| SellerDtls.Pin | 6-digit PIN code |
| SellerDtls.Stcd | State code |

### Buyer Details (BuyerDtls)

| Field Path | Description |
| --- | --- |
| BuyerDtls.Gstin | Buyer GSTIN (or URP for an unregistered recipient, for example in an export) |
| BuyerDtls.LglNm | Legal name |
| BuyerDtls.Pos | Place of supply (State code) |
| BuyerDtls.Addr1 | Address line 1 |
| BuyerDtls.Loc | Location |
| BuyerDtls.Pin | PIN code |
| BuyerDtls.Stcd | State code |

### Item Details (ItemList[])

| Field Path | Description |
| --- | --- |
| SlNo | Serial number (from 1) |
| PrdDesc | Product description |
| IsServc | Is service (Y/N) |
| HsnCd | HSN or SAC code; number of digits as in the HSN table below |
| Qty | Quantity |
| Unit | Unit of measurement (UQC code) |
| UnitPrice | Unit price |
| TotAmt | Total amount (Qty x UnitPrice) |
| AssAmt | Assessable amount (after discount) |
| GstRt | GST rate (IGST rate, or the CGST and SGST rates combined) |
| IgstAmt / CgstAmt / SgstAmt | Tax amounts |
| TotItemVal | Total item value including tax |

**HSN digits.** From 1 April 2021, a registered person whose aggregate turnover in the preceding financial year was up to five crores rupees shows 4 digits of the HSN code, and one with more than five crores rupees shows 6 digits. A person with turnover up to five crores rupees may leave the HSN code off invoices to unregistered persons. Source: [Notification No. 78/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf). This test uses the preceding financial year only, not any year since 2017-18.

### Value Details (ValDtls)

| Field Path | Description |
| --- | --- |
| ValDtls.AssVal | Total assessable value |
| ValDtls.IgstVal | Total IGST |
| ValDtls.CgstVal | Total CGST |
| ValDtls.SgstVal | Total SGST or UTGST |
| ValDtls.TotInvVal | Total invoice value (INR) |

## Section 5: Transmission Method

### API Integration (Recommended)

The IRP exposes an API for direct ERP integration, with a separate sandbox for testing. The base URLs, the API version in the path and the endpoint names are published by GSTN on the e-invoice portal; this Guide does not list them because those hosts could not be read. The earlier version of this Guide named these operations: authenticate, generate IRN (post invoice JSON), cancel IRN, and get invoice by IRN.

### Authentication

| Header | Description |
| --- | --- |
| client-id | Issued on API registration |
| client-secret | Issued on API registration |
| user_name | Taxpayer's API user name |
| Gstin | Taxpayer's GSTIN |
| AuthToken | Session token returned by the authentication call; its validity period and refresh method are set by GSTN |

### Alternative Submission Methods

1. **GSP or ASP route.** A GST Suvidha Provider or application service provider sits between the ERP and the IRP.
2. **Bulk upload.** JSON file upload through the IRP web portal.
3. **Offline tool.** A spreadsheet-to-JSON tool from the IRP portal, for low volumes.

## Section 6: Validation Rules

### IRP Pre-Checks (Real-Time)

From the earlier version of this Guide (not checked; see Section 3):

1. GSTIN validity: the supplier and buyer GSTINs must be active.
2. Duplicate check: supplier GSTIN, document type, document number and financial year must be unique.
3. Date validation: the document date cannot be in the future.
4. HSN validation: the code must exist in the HSN master, with enough digits (Section 4).
5. Arithmetic: line totals must agree with document totals, within a small rounding tolerance.
6. State code and PIN code must be consistent.
7. GST rate: GstRt must be a rate the IRP accepts. The IRP's accepted-rate list could not be read; the general rates from 22 September 2025 are in Section 7.

### Common Rejection Reasons

The error codes below are from the earlier version of this Guide and were not checked against GSTN's current error list.

| Error Code | Description | Fix |
| --- | --- | --- |
| 2150 | Duplicate IRN | Document already registered; fetch the existing IRN |
| 2163 | Document date outside the permitted window | Read the current GSTN advisory before re-issuing |
| 2174 | GSTIN not enabled for e-invoicing | Check enablement on the e-invoice portal |
| 2283 | HSN code invalid | Correct the HSN code and digit count |
| 2269 | Item value mismatch | Recalculate TotAmt as Qty x UnitPrice |
| 2287 | Total invoice value mismatch | Check ValDtls.TotInvVal against the sum of the components |

## Section 7: Tax Computation Rules

### Tax Amount Calculation

- **Intra-State supply.** CGST and SGST (or UTGST), each half of the GST rate.
- **Inter-State supply.** IGST at the full GST rate.
- **Place of supply.** BuyerDtls.Pos decides intra-State or inter-State.

### GST rates for GstRt from 22 September 2025

The 56th GST Council moved GST from four general slabs to two rates plus a special de-merit rate, for services and most goods from 22 September 2025. The old general slabs that are not in the table below no longer exist as general slabs.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf |
| Standard rate | 18% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Merit rate | 5% | "a 2 rate structure with a Standard Rate of 18% and a Merit Rate of 5%" |
| Special de-merit rate (a select few goods and services) | 40% | "a special de-merit rate of 40% for a select few goods and services" |

The 22 September 2025 date does not apply to pan masala, gutkha, cigarettes, chewing tobacco, unmanufactured tobacco and bidi. A revised rate structure for those goods took effect on 1 February 2026 ([GST Council newsletter, December 2025](https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf)). Take the rate for each HSN code from the rate notification, not from this table.

### Rounding Rules

- **Rounding.** Amounts to 2 decimal places. Round each line, then sum. The IRP allows a small difference between the sum of lines and the document total; check GSTN's current tolerance.

### Multi-Rate Invoice

- **Multi-rate invoices.** Each line carries its own GstRt. ValDtls adds up IGST, CGST and SGST across lines. One invoice may mix rates.

### Discount Handling

- **Discounts.** Applied at line level: AssAmt = TotAmt minus discount. Tax is calculated on AssAmt.

## Section 8: Archiving Requirements

| Requirement | Detail |
| --- | --- |
| Retention period | Until the expiry of seventy-two months from the due date of the annual return for the year the records relate to (section 36 of the [CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html)). If the person is party to an appeal or other proceedings, or is under investigation, the records for that subject matter are kept until one year after final disposal, if that is later. |
| What to keep | Recommended (not a rule): The invoice data uploaded, and the signed response from the IRP with the IRN and QR code |
| QR code | The invoice must carry a "Quick Response code, having embedded Invoice Reference Number (IRN) in it" where it is issued under rule 48(4) (rule 46(r) of the [CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html)). The other contents of the QR code are set by GSTN; the earlier version of this Guide listed them as IRN, invoice date, supplier GSTIN, buyer GSTIN, invoice value, number of line items, HSN codes and a unique hash (unchecked GSTN material; see Section 3). |
| Storage medium | The earlier version of this Guide said no specific medium is mandated and records must be producible on demand during audit (unchecked legacy statement; no allowed page was read for it). |
| Paper copies | Rule 48(6): the triplicate and duplicate copy rules in rule 48(1) and (2) do not apply to an invoice prepared under rule 48(4). |

## Section 9: Penalties for Non-Compliance

Rule 48(5): an invoice issued by a person to whom rule 48(4) applies "in any manner other than the manner specified in the said sub-rule shall not be treated as an invoice". Source: [rule 48 of the CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule48_v1.00.html). The penalties in the CGST Act are below; which one an officer uses depends on the facts.

| Offence (CGST Act wording) | Penalty | Legal basis |
| --- | --- | --- |
| "supplies any goods or services or both without issue of any invoice or issues an incorrect or false invoice" | "ten thousand rupees or an amount equivalent to the tax evaded", whichever is higher | [Section 122(1)(i)](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section122_v1.00.html) |
| "issues any invoice or bill without supply of goods or services or both" | The same section 122(1) penalty: ten thousand rupees or the amount it names (tax evaded, or input tax credit "availed of or passed on or distributed irregularly"), whichever is higher | [Section 122(1)(ii)](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section122_v1.00.html) |
| "fails to issue invoice in accordance with the provisions of this Act or the rules made thereunder" | "may extend to twenty-five thousand rupees" | [Section 122(3)(e)](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section122_v1.00.html) |
| Any contravention with no separate penalty | "may extend to twenty-five thousand rupees" | [Section 125](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section125_v1.00.html) |

Section 122(1) does not use the words "per invoice". Whether each invoice issued without an IRN is a separate offence is not settled by the section text. The 57th GST Council recommended reducing the maximum general penalty under section 125. Separately, in amendments to sections 73, 74 and 74A (tax demands), it recommended removing the condition of a minimum penalty in non-fraud cases; that recommendation is not about section 122 ([57th GST Council press release](https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf)). These are recommendations, not law on 17 October 2026.

### Cascading Impact

Section 16(2)(a) of the [CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html) allows input tax credit only where the buyer "is in possession of a tax invoice or debit note issued by a supplier registered under this Act, or such other tax paying documents as may be prescribed". A document that rule 48(5) says "shall not be treated as an invoice" therefore puts the buyer's credit at risk. That gives buyers a reason to insist on an IRN, and suppliers a commercial reason to comply.

## Section 10: Interaction with Tax Guides

The portal behaviour in this section is GSTN's and was not checked against an official page (see Section 3).

### GSTR-1 Auto-Population

- **GSTR-1.** The IRP passes e-invoice data to the GST portal, which fills the supplier's FORM GSTR-1. The supplier still files GSTR-1 and should reconcile what was filled against its books before filing. The earlier version of this Guide said the IRP pushes the data the next day, and that where e-invoice data and manually entered GSTR-1 data differ, the e-invoice data prevails (unchecked GSTN material; see Section 3).

### E-Way Bill Integration

- **E-way bill.** Rule 138 of the [CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter16/rule138_v1.00.html) requires the e-way bill information before movement of goods of consignment value exceeding fifty thousand rupees, whether in relation to a supply, for reasons other than supply, or for an inward supply from an unregistered person. The IRP can take e-way bill details (EwbDtls) with the invoice upload; this saves a step but does not change the rule 138 test.

### GSTR-2B / ITC Matching

- **GSTR-2B.** The buyer's GSTR-2B is built from what suppliers report, including e-invoices. Use it to match credit claims.

### Annual Return (GSTR-9)

- **GSTR-9.** E-invoice data feeds the annual return reconciliation. Expect officers to compare GSTR-9 figures with IRP data.

## The method, step by step

1. **Find the aggregate turnover for every financial year from 2017-18.** Add all GSTINs under the same PAN, on an all-India basis, excluding taxes and inward reverse-charge supplies (section 2(6) of the [CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter1/section2_v1.00.html)).
2. **Apply the threshold.** If any financial year from 2017-18 up to the year before the current one exceeds five crore rupees, the business is in from 1 August 2023 ([Notification No. 10/2023-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf)) or, if the first such year is FY 2023-24 or later, from 1 April of the next financial year, when that year becomes a "preceding financial year" ([Notification No. 70/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf)). For an earlier date of a breach, use the phase-in table in Section 1.
3. **Check the exclusions.** Insurer, bank, financial institution or NBFC, goods transport agency, passenger transport, multiplex cinema admission ([rule 54](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule54_v1.00.html)), SEZ unit ([Notification No. 61/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-61-central-tax-english-2020.pdf)), government department or local authority ([Notification No. 23/2021-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-23-central-tax-english-2021.pdf)). An excluded person above the threshold prints the rule 46(s) declaration on its invoices ([rule 46](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html)).
4. **Sort the documents.** Invoices and other prescribed documents for supplies to registered persons, and for exports, go through the IRP ([Notification No. 13/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-13-central-tax-english-2020.pdf) as amended by [70/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf)). B2C invoices do not. If the turnover test of [Notification No. 14/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-14-central-tax-english-2020.pdf) is met, B2C invoices need a Dynamic QR code instead.
5. **Get the IRN before issuing.** Rule 48(4) requires the invoice to be prepared after obtaining the IRN ([rule 48](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule48_v1.00.html)), within the invoice timing of [section 31](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter7/section31_v1.00.html). Check the current GSTN advisory for any reporting window.
6. **Show the QR code and HSN.** The invoice carries the QR code with the embedded IRN (rule 46(r)) and the HSN digits set by [Notification No. 78/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf).
7. **Keep the records** for the period in [section 36](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html).

## Ask the client first

- What was the aggregate turnover across all GSTINs under your PAN in each financial year from 2017-18 to last year? One year above five crore rupees is enough.
- Are you an insurer, bank, financial institution or NBFC, goods transport agency, passenger transport operator, multiplex cinema, SEZ unit, government department or local authority?
- Which of your supplies go to registered buyers, which are exports, and which go to unregistered customers?
- Has any invoice already gone out without an IRN, and if so, has the buyer claimed input tax credit on it?
- Do you move goods with a consignment value above the rule 138 limit, and do you want e-way bills raised with the IRN?

## When to refuse or refer

- **Invoices already issued without an IRN.** Rule 48(5) says they are not invoices. Fixing them (cancelling and re-issuing, and the buyer's credit) and any penalty exposure under section 122 needs a GST practitioner who can see the documents and the portal.
- **Notice, audit or penalty proceedings.** Refer. The choice between section 122(1), 122(3) and 125 depends on facts this Guide cannot see.
- **Unclear exclusion.** A business with mixed activities (for example a bank arm and a trading arm under one PAN), or a single-screen cinema, needs a practitioner's reading of rule 54 and the notifications.
- **Rule 46(s) declaration on B2C invoices.** Whether rule 46(s) requires the declaration on the B2C invoices of a taxpayer that already e-invoices its B2B supplies is not settled by the rule text; ask a practitioner.
- **IRP time limits and rejection codes.** These are set by GSTN advisory. Refuse to give a deadline from this Guide; check the e-invoice portal.
- **The 57th Council proposals.** Do not advise that the extension to reverse-charge inward supplies or imports of services, or any penalty change, is in force until it is notified.

## Sources

- [Rule 48, CGST Rules (CBIC consolidated text)](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule48_v1.00.html)
- [Rule 46, CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule46_v1.00.html)
- [Rule 54, CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter6/rule54_v1.00.html)
- [Rule 138, CGST Rules](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/rules/cgst_rules/active/chapter16/rule138_v1.00.html)
- [Section 2, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter1/section2_v1.00.html)
- [Section 16, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter5/section16_v1.00.html)
- [Section 31, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter7/section31_v1.00.html)
- [Section 36, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter8/section36_v1.00.html)
- [Section 122, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section122_v1.00.html)
- [Section 125, CGST Act](https://taxinformation.cbic.gov.in/content/html/tax_repository/gst/acts/2017_CGST_act/active/chapter19/section125_v1.00.html)
- [Notification No. 69/2019-Central Tax (e-invoice portals)](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-69-central-tax-english-2019.pdf)
- [Notification No. 13/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-13-central-tax-english-2020.pdf) and amendments [61/2020](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-61-central-tax-english-2020.pdf), [70/2020](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-70-central-tax-english-2020.pdf), [88/2020](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-88-central-tax-english-2020.pdf), [05/2021](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-05-central-tax-english-2021.pdf), [23/2021](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-23-central-tax-english-2021.pdf), [01/2022](https://gstcouncil.gov.in/sites/default/files/2024-05/nn_01_2022_english.pdf), [17/2022](https://gstcouncil.gov.in/sites/default/files/2024-05/17-2022-ct-eng_1_1.pdf), [10/2023](https://gstcouncil.gov.in/sites/default/files/2024-05/10ct_eng.pdf)
- [Notification No. 14/2020-Central Tax (B2C Dynamic QR code)](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-14-central-tax-english-2020.pdf) and [71/2020-Central Tax](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-71-central-tax-english-2020.pdf)
- [Notification No. 78/2020-Central Tax (HSN digits)](https://gstcouncil.gov.in/sites/default/files/2024-05/notfctn-78-central-tax-english-2020.pdf)
- [56th GST Council press release (rates from 22 September 2025)](https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau_0.pdf)
- [GST Council newsletter, December 2025](https://gstcouncil.gov.in/sites/default/files/2026-01/monthly_newsletter_december_2025_1_0.pdf)
- [57th GST Council press release (recommendations, not law)](https://gstcouncil.gov.in/sites/default/files/2026-10/press_release_0.pdf)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CA, CPA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained by OpenAccountants.

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
