---
name: poland-einvoice
description: Use this skill whenever asked about Polish e-invoicing, KSeF, Krajowy System e-Faktur, faktura ustrukturyzowana, FA(3) schema, structured invoice Poland, e-Faktura, UPO (Urzędowe Poświadczenie Odbioru), KSeF API, KSeF 2.0, batch submission Poland, offline mode KSeF, GTU codes, split payment MPP, NIP validation, or any question about issuing, receiving, validating, or archiving electronic invoices in Poland. Also trigger when preparing FA(3) XML invoices, configuring KSeF API integration, handling KSeF rejection errors, or advising on the transition to mandatory KSeF. This skill covers the FA(3) schema, KSeF API architecture, mandatory fields, validation rules, archiving, penalties, and interaction with Polish VAT returns. ALWAYS read this skill before touching any Polish e-invoicing work.
version: 1.0
jurisdiction: PL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Poland Einvoice

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Poland (Rzeczpospolita Polska) |
| Currency | PLN (Polish złoty); foreign currency invoices also supported |
| E-invoicing system | KSeF (Krajowy System e-Faktur) -- Krajowy System e-Faktur 2.0 |
| Invoice format | FA(3) XML (proprietary Polish schema, NOT EN 16931) |
| Governing body | Ministerstwo Finansów (Ministry of Finance) |
| Tax authority | Krajowa Administracja Skarbowa (KAS) |
| Key legislation | Act of 29 October 2021 amending VAT Act (Dz.U. 2021 poz. 2076); RD on KSeF implementation; VAT Act Art. 106na--106nd |
| Portal URL | https://ksef.podatki.gov.pl |
| Schema URL | https://crd.gov.pl/wzor/2025/06/25/13775/ (FA(3) production) |
| API documentation | OpenAPI 3.0.4 specification at ksef.podatki.gov.pl |
| Phase 1 mandatory | 1 February 2026 (businesses with 2024 VAT sales > PLN 200M) |
| Phase 2 mandatory | 1 April 2026 (all remaining VAT-registered businesses) |
| Penalties effective | 1 January 2027 |
| Current status | Fully operational in production since 1 February 2026 |
| Skill version | 1.0 |

## Section 2 -- Mandate Scope

### Who Must Comply

**Who Must Comply**

| Scope | From | Requirement |
| --- | --- | --- |
| Large taxpayers (2024 VAT sales > PLN 200M) | 1 February 2026 | Must issue all B2B invoices via KSeF |
| All remaining VAT-registered businesses | 1 April 2026 | Must issue all B2B invoices via KSeF |
| B2G | 1 February 2026 | Invoices to public entities must be issued via KSeF (integration with PEF -- Platforma Elektronicznego Fakturowania) |
| B2C | Not mandatory | Consumer invoices may be issued outside KSeF; if issued via KSeF, buyer receives a visualisation (not the XML) |
| Foreign entities with Polish VAT registration | 1 April 2026 | Must issue structured invoices via KSeF for Polish-taxable transactions |
| Cross-border invoices | Required | All invoices issued by Polish VAT payers, including cross-border, must be reported through KSeF |

### Exemptions

- Invoices issued by taxpayers not registered for Polish VAT
- Tickets and simplified invoices for amounts up to PLN 450 (EUR ~100) -- exempt from KSeF but subject to Veri\*factu-like fiscal printer rules
- Invoices from the agricultural flat-rate scheme (rolnik ryczałtowy) issued by the buyer (RR invoices use a separate FA_RR(1) schema)

### Timeline Summary

**Timeline Summary**

| Date | Milestone |
| --- | --- |
| October 2021 | KSeF legislative framework enacted |
| January 2022 | Voluntary KSeF 1.0 launched |
| September 2023 | FA(2) schema published |
| April 2025 | AEAT Veri\*factu services enter production |
| June 2025 | KSeF 2.0 API documentation published |
| September 2025 | Open API testing begins |
| October 2025 | Pre-production DEMO environment available |
| 1 February 2026 | KSeF 2.0 production launch; mandatory for large taxpayers; FA(3) schema effective |
| 1 April 2026 | Mandatory for all remaining VAT-registered businesses |
| 1 January 2027 | Financial penalties for non-compliance take effect |

## Section 3 -- Technical Format

### FA(3) Schema

**FA(3) Schema**

| Parameter | Value |
| --- | --- |
| Format | Proprietary Polish XML schema (NOT EN 16931 / UBL / CII) |
| Schema version | FA(3) (effective 1 February 2026, replacing FA(2)) |
| Schema location | https://crd.gov.pl/wzor/2025/06/25/13775/ |
| Encoding | UTF-8 |
| Namespace | As defined in FA(3) XSD |
| Validation | XSD schema validation + semantic business rules |

### FA(3) Root Structure

**FA(3) Root Structure**

| Element | Required | Description |
| --- | --- | --- |
| `Naglowek` | Yes | Header: schema version, form code, creation date |
| `Podmiot1` | Yes | Seller: tax ID (NIP), name, address |
| `Podmiot2` | Yes | Buyer: tax ID (NIP or other), name, address |
| `Podmiot3` | No | Third party (e.g., tax representative, factor) |
| `PodmiotUpowazniony` | Conditional | Authorised entity (if issuing on behalf of seller) |
| `Fa` | Yes | Invoice body: header data, line items, totals, payment, annotations |
| `Stopka` | No | Footer: additional free-text information |
| `Zalacznik` | No | Attachment node (new in FA(3) -- for structured attachments) |

### Key Differences from EN 16931

**Key Differences from EN 16931**

| Feature | KSeF FA(3) | EN 16931 |
| --- | --- | --- |
| Schema | Proprietary Polish XSD | UBL 2.1 or CII |
| GTU codes | Required for classified goods/services (GTU_01--GTU_13) | No equivalent |
| MPP marker | Split payment indicator for transactions > PLN 15,000 | No equivalent |
| Adnotacje (annotations) | Mandatory boolean fields (P_16 through P_18A, Zwolnienie, etc.) | Free-text notes |
| Hash/chain integrity | Not in schema (KSeF assigns number) | Not applicable |
| Peppol interoperability | Not supported -- closed national system | Core design principle |

## Section 4 -- Mandatory Fields

### Naglowek (Header)

**Naglowek (Header)**

| Field | Description | Required |
| --- | --- | --- |
| `KodFormularza` | Form code (must be "FA") | Yes |
| `WariantFormularza` | Schema variant (3 for FA(3)) | Yes |
| `DataWytworzeniaFa` | XML creation datetime | Yes |
| `SystemInfo` | Issuing system identifier | Yes |

### Podmiot1 (Seller)

**Podmiot1 (Seller)**

| Field | Description | Required |
| --- | --- | --- |
| `DaneIdentyfikacyjne/NIP` | Seller Polish tax ID (NIP, 10 digits) | Yes |
| `DaneIdentyfikacyjne/Nazwa` | Seller full legal name | Yes |
| `Adres` | Seller address (street, city, postal code, country) | Yes |

### Podmiot2 (Buyer)

**Podmiot2 (Buyer)**

| Field | Description | Required |
| --- | --- | --- |
| `DaneIdentyfikacyjne/NIP` or `NrVatUE` or `KodUE`+`NrID` | Buyer identification | Yes (at least one) |
| `DaneIdentyfikacyjne/Nazwa` | Buyer name | Yes |
| `Adres` | Buyer address | Yes |

### Fa (Invoice Body)

**Fa (Invoice Body)**

| Field | Description | Required |
| --- | --- | --- |
| `P_1` | Invoice issue date (YYYY-MM-DD) | Yes |
| `P_2` | Invoice number (sequential) | Yes |
| `P_3A` or `P_3B` | Sale/service date or period | Yes (one required) |
| `FaWiersz/NrWierszaFa` | Line number (unique, sequential) | Yes |
| `FaWiersz/P_7` | Description of goods/services | Yes |
| `FaWiersz/P_8A` or `P_8B` | Unit of measure | Yes |
| `FaWiersz/P_9A` or `P_9B` | Quantity | Yes |
| `FaWiersz/P_10` | Unit net price (up to 8 decimal places) | Conditional |
| `FaWiersz/P_11` | Line net amount (2 decimal places) | Yes |
| `FaWiersz/P_11A` | Line VAT amount | Conditional |
| `FaWiersz/P_12` | VAT rate (23, 8, 5, 0, zw, oo, np) | Yes |
| `P_13_1` through `P_13_11` | Summary net amounts per rate | Conditional (per applicable rate) |
| `P_14_1` through `P_14_5` | Summary VAT amounts per rate | Conditional |
| `P_15` | Total gross amount (brutto) | Yes |

### Adnotacje (Annotations -- Mandatory Booleans)

**Adnotacje (Annotations -- Mandatory Booleans)**

| Field | Description | Values |
| --- | --- | --- |
| `P_16` | Reverse charge (Art. 17 ust. 1 pkt 7/8) | 1 or 2 |
| `P_17` | Self-supply (Art. 106a pkt 2 lit. b) | 1 or 2 |
| `P_18` | Margin scheme | 1 or 2 |
| `P_18A` | Mechanism of split payment (MPP) | 1 or 2 |
| `Zwolnienie` | VAT exemption basis | Selection required if any line is "zw" |

### GTU Codes (Goods/Services Classification)

**GTU Codes (Goods/Services Classification)**

| Code | Category |
| --- | --- |
| GTU_01 | Alcohol |
| GTU_02 | Fuel |
| GTU_03 | Heating oil |
| GTU_04 | Tobacco |
| GTU_05 | Waste |
| GTU_06 | Electronic devices |
| GTU_07 | Vehicles and parts |
| GTU_08 | Precious metals |
| GTU_09 | Pharmaceuticals |
| GTU_10 | Buildings/land |
| GTU_11 | Emission allowances |
| GTU_12 | Intangible services (consulting, advisory, legal, management) |
| GTU_13 | Transport services |

## Section 5 -- Transmission Method

### KSeF API 2.0

**KSeF API 2.0**

| Parameter | Detail |
| --- | --- |
| API specification | OpenAPI 3.0.4 (JSON) |
| Production endpoint | `https://api.ksef.mf.gov.pl/v2` |
| DEMO endpoint | `https://api-demo.ksef.mf.gov.pl/v2` |
| Test endpoint | `https://api-test.ksef.mf.gov.pl/v2` |
| Authentication | Qualified electronic signature, trusted profile (profil zaufany), or KSeF authorisation token |
| Session types | Interactive (real-time, single invoices) or Batch (bulk submission) |

### Submission Flow

1. **Authenticate** -- open a KSeF session using certificate, trusted profile, or token
2. **Submit** -- send FA(3) XML file via API endpoint
3. **Validate** -- KSeF performs XSD and semantic validation
4. **Accept or Reject** -- if valid, KSeF assigns a unique KSeF number and timestamp; if invalid, returns error
5. **UPO** -- download Urzędowe Poświadczenie Odbioru (official receipt of acceptance) as proof of issuance
6. **Buyer access** -- buyer retrieves invoice from KSeF using their NIP credentials

### Alternative Submission Methods

**Alternative Submission Methods**

| Method | Description |
| --- | --- |
| Aplikacja Podatnika KSeF | Free web application from Ministry of Finance |
| Aplikacja Mobilna KSeF | Free mobile app for issuing/receiving on smartphone |
| e-mikrofirma | Integration with e-Urząd Skarbowy for micro-businesses |
| Batch mode | Upload ZIP of multiple FA(3) XMLs; each validated individually |

### Offline Mode

If KSeF is unavailable (system downtime declared by MF), businesses may:

1. Issue invoices outside KSeF with offline numbering
2. Submit to KSeF within 7 days of system restoration
3. The date of issue (P_1) remains the original date; the KSeF date is the submission date
4. Offline invoices require specific handling and must reference the offline period

### KSeF Number Format

- **KSeF Number Format** — Format: `{NIP}-{YYYYMMDD}-{sequential number}` -- assigned by KSeF upon acceptance. This number becomes the primary legal identifier of the invoice.

## Section 6 -- Validation Rules

### XSD Validation (First Layer)

- **XSD validation rejection rate** — KSeF validates every submitted XML against the FA(3) XSD. Approximately 70% of rejections are XSD validation errors.

**XSD Validation (First Layer)**

| Common XSD Error | Cause | Resolution |
| --- | --- | --- |
| Missing required element | Required field not populated (e.g., NIP in Podmiot1) | Populate all mandatory fields |
| Wrong date format | Dates must be YYYY-MM-DD (not DD.MM.YYYY or DD/MM/YYYY) | Standardise date formatting |
| Invalid element order | XML elements must follow XSD-defined sequence | Reorder elements per schema |
| Wrong data type | Numeric field contains text or vice versa | Validate field types |
| Excess decimal places | Amounts: max 2 decimals; prices: max 8; quantities: max 6 | Apply correct precision |

### Semantic Validation (Second Layer)

**Semantic Validation (Second Layer)**

| Rule | Description |
| --- | --- |
| NIP checksum | Seller NIP must pass modulus-11 check digit validation |
| Tax calculation | Sum of line net amounts per rate must equal summary amount (P_13_x); VAT amounts must equal P_14_x |
| Gross total | P_15 must equal sum of all net amounts + all VAT amounts |
| GTU format | Must be exact codes (e.g., `GTU_12` not `12` or `GTU 12`) |
| Duplicate detection | Same seller NIP + invoice number + date = error 440 (duplicate) |
| Adnotacje completeness | All mandatory annotation fields (P_16, P_17, P_18, P_18A) must be populated |
| Zwolnienie logic | If any line has rate "zw", the Zwolnienie element must specify the exemption basis |
| Currency handling | Foreign currency invoices must include PLN conversion amounts in separate fields |

### Common Rejection Scenarios

**Common Rejection Scenarios**

| Issue | Resolution |
| --- | --- |
| Polish NIP in NrVatUE field | Polish NIPs go in the NIP field; NrVatUE is for EU VAT numbers with country prefix |
| Rounding mismatch | Use banker's rounding; ensure line totals sum to header totals within 1 grosz |
| Negative quantities on non-corrective invoice | Only corrective invoices (korekta) may have negative values |
| Missing Adnotacje fields | Even if not applicable, P_16 through P_18A must contain value "2" (not applicable) |
| Invalid bank account format | Polish IBAN must be exactly 26 characters (digits only, no PL prefix in domestic format) |

## Section 7 -- Tax Computation Rules

### VAT Rates (2025/2026)

**VAT Rates (2025/2026)**

| Rate Code | Rate | Application |
| --- | --- | --- |
| 23 | 23% | Standard rate |
| 8 | 8% | Reduced (construction, certain food, medical) |
| 5 | 5% | Reduced (basic food, books, periodicals) |
| 0 | 0% | Zero-rated (intra-EU supplies, exports) |
| zw | Exempt | VAT-exempt supplies (must specify exemption basis) |
| oo | Not subject | Out-of-scope transactions |
| np | Not applicable | Supplies not subject to Polish VAT (e.g., place of supply outside Poland) |

### Rounding

- **Rounding rules** — - Line net amount (`P_11`): 2 decimal places - Unit price (`P_10`): up to 8 decimal places - Quantity (`P_9A`/`P_9B`): up to 6 decimal places - VAT amount per line (`P_11A`): 2 decimal places - Gross total (`P_15`): 2 decimal places - Use banker's rounding (round half to even) for consistency with KSeF validation - Sum of line amounts must exactly equal the corresponding summary field -- no tolerance

### Multi-Rate Invoice Handling

- **Multi-rate invoice handling** — - Each applicable VAT rate has dedicated summary fields (P_13_1/P_14_1 for 23%, P_13_2/P_14_2 for 8%, etc.) - Line items reference the rate via P_12 - If a single invoice has lines at 23%, 8%, and exempt, all three summary pairs must be populated - P_15 (gross total) = sum of all P_13_x + sum of all P_14_x

### Split Payment (Mechanizm Podzielonej Płatności -- MPP)

- **Split payment (MPP) rule** — - Mandatory for transactions > PLN 15,000 gross involving goods/services listed in Annex 15 to the VAT Act - Set annotation P_18A = 1 when MPP applies - Invoice must include the phrase "mechanizm podzielonej płatności" - Payment is split: net amount to seller's account, VAT amount to seller's VAT account  _(Annex 15 to the VAT Act)_

### Corrective Invoices (Faktury Korygujące)

- **Corrective invoices rule** — - Must reference the original KSeF number of the corrected invoice - Show both "before" and "after" values, or the difference - Use same FA(3) schema with corrective-specific fields populated - KSeF validates that the referenced original invoice exists and belongs to the same seller NIP

## Section 8 -- Archiving Requirements

**Section 8 -- Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| KSeF as legal archive | KSeF stores all accepted invoices for 10 years -- this constitutes the legal archive |
| No separate archiving needed | Once accepted by KSeF, the invoice is legally archived; businesses do not need to maintain separate copies for VAT purposes |
| Attachments | KSeF does NOT store attachments (Zalacznik node in FA(3) is metadata only); supporting documents (contracts, delivery notes) must be archived separately by the business |
| UPO retention | Retain UPO (official receipt) as proof of successful submission |
| Pre-KSeF invoices | Invoices issued before KSeF mandate remain subject to standard Polish archiving rules (5 years from end of tax year) |
| Access | Both seller and buyer can retrieve invoices from KSeF at any time during the retention period using their NIP credentials |
| Audit | Tax authorities have direct access to all KSeF invoices; no separate data provision needed during audits |

## Section 9 -- Penalties for Non-Compliance

Financial penalties take effect from 1 January 2027. During 2026, the practical consequences of non-compliance are primarily operational (invoices not legally valid for VAT deduction).

## Section 9 -- Penalties for Non-Compliance

**Penalties table**

| Violation | Penalty |
| --- | --- |
| Issuing invoice outside KSeF (when mandatory) | Up to 100% of the VAT amount on the invoice |
| Invoice not conforming to FA(3) schema | Rejection by KSeF -- invoice not legally issued; must correct and resubmit |
| Failure to issue invoice at all | Standard VAT Act penalties apply (up to 720 daily rates under fiscal penal code) |
| Late submission in offline mode | Must submit within 7 days of system restoration; late submission may trigger penalties |
| Buyer deducting input VAT from non-KSeF invoice | Input VAT deduction denied -- buyer bears the risk |
| Using non-KSeF invoices after mandate date | Trading partners on compliant systems may reject non-KSeF invoices |

### Practical Risks During 2026 (Before Penalty Enforcement)

- Invoices not submitted through KSeF are not legally valid for VAT deduction purposes
- Trading partners may refuse non-KSeF invoices
- Audit exposure increases as KAS cross-references KSeF data

## Section 10 -- Interaction with Tax Skills

### VAT Return Integration

- **VAT return integration** — - KSeF data directly feeds into JPK_VAT (Jednolity Plik Kontrolny) -- the standard audit file for VAT - JPK_V7M (monthly) and JPK_V7K (quarterly) declarations must reconcile with invoices in KSeF - KSeF invoice numbers are used as references in JPK records - GTU codes from KSeF invoices must match GTU markings in JPK_VAT - Split payment (MPP) markers from KSeF feed into JPK_VAT classification - Tax authorities can automatically cross-check KSeF invoices against JPK declarations in real-time

### e-Urząd Skarbowy Integration

- The e-mikrofirma module in e-Urząd Skarbowy connects directly to KSeF
- Taxpayers can issue invoices in KSeF and transfer data directly to VAT records without manual re-entry
- Pre-filled VAT returns based on KSeF data are progressively being developed

### Income Tax Integration

- **Income tax integration** — - For sole proprietors (JDG -- jednoosobowa działalność gospodarcza), KSeF invoice data feeds into the annual PIT-36/PIT-36L return - Revenue and cost figures must reconcile with KSeF records - KSeF provides an authoritative source for income verification during audits

### Cross-Border Considerations

- **Cross-border considerations** — - All invoices issued by Polish VAT payers, including intra-EU and export invoices, must be reported through KSeF - Intra-EU supplies must be reported in both KSeF and the EU VAT Information Exchange System (VIES) via VAT-UE declaration - Import VAT (from customs declarations) is handled separately but must reconcile with purchase invoices in KSeF

### PEF (Platforma Elektronicznego Fakturowania) Integration

- B2G invoices previously submitted through PEF are being migrated to KSeF
- From 1 February 2026, PEF forwards invoices to KSeF production environment
- Public entities receive invoices through KSeF with PEF acting as an intermediary during transition

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a doradca podatkowy, biegły rewident, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
