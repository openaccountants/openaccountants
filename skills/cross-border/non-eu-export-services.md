---
name: non-eu-export-services
description: Use this skill whenever a freelancer or small business sells services to a client located outside their own VAT/GST jurisdiction and needs to determine the correct indirect tax treatment. Trigger on phrases like "export of services", "services to overseas client", "zero-rated services", "out of scope", "no VAT on export", "GST-free export", "outside the scope of VAT", "services to US client", "services to non-EU client", "Division 38", "Fifth Schedule", or any request about the VAT/GST treatment of services supplied to foreign clients. This skill covers the rules for EU sellers exporting services outside the EU, UK sellers to non-UK clients, Australian sellers (GST-free exports under Division 38), Indian sellers (zero-rated export of services), and Singaporean sellers (zero-rated under the Fifth Schedule). ALWAYS read this skill before advising on the indirect tax treatment of service exports.
---

# Export of Services -- VAT/GST Treatment for Services Sold Outside the Seller's Jurisdiction

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Multi-jurisdiction (EU, UK, Australia, India, Singapore, and general principles) |
| Primary Legislation | EU: VAT Directive Art 44, 59; UK: VATA 1994 s7, s8, Sch 4A; AU: GST Act 1999 Div 38; IN: IGST Act 2017 s2(6); SG: GST Act s21(3), Fifth Schedule |
| Scope | Services (not goods) supplied by a seller in one jurisdiction to a client in a different jurisdiction, where the service is consumed outside the seller's country |
| Contributor | OpenAccountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard B2B service exports (consulting, IT, professional services). Tier 2: land-related services, events, transport, mixed supplies. Tier 3: complex multi-party arrangements, services with unclear place of consumption. |
| Cross-references | `eu-reverse-charge.md`, `eu-oss-digital.md`, `permanent-establishment-risk.md`, country-specific VAT return skills |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a qualified professional.

---

## Step 0: Pre-Check Questions [T1]

1. **Where is the seller established / registered for VAT or GST?** Determines which country's rules govern the supply.
2. **Where is the client located?** Must be outside the seller's VAT/GST jurisdiction.
3. **Is the client a business (B2B) or a consumer (B2C)?** Affects the place of supply rule in many jurisdictions.
4. **What is the nature of the service?** Check for exceptions (land, events, transport).
5. **Where is the service physically performed or consumed?** Some exceptions depend on this.

**If items 1-3 are unknown, STOP.**

---

## Step 1: General Principle [T1]

**The general principle across most VAT/GST systems worldwide:**

Services supplied to a client outside the seller's jurisdiction are typically:
- **Zero-rated** (VAT/GST at 0%, but the seller retains the right to recover input VAT/GST on related costs), or
- **Out of scope** (not within the charge to VAT/GST at all; input recovery depends on the jurisdiction).

**The effect for the seller is the same in practice:** no VAT/GST is charged on the invoice to the foreign client.

**BUT there are important exceptions** where the service is taxed where it is performed or where the property is located, regardless of the client's location. See Step 7.

---

## Step 2: EU Seller to Non-EU Client [T1]

**Legislation:** VAT Directive Art 44 (B2B general rule), Art 59 (B2C specific services), Art 45 (B2C general rule).

### B2B: Seller (any EU country) to Non-EU Business Client [T1]

| Rule | Detail |
|------|--------|
| Place of supply | Client's country (Art 44) -- outside the EU |
| VAT charged | None (outside the scope of EU VAT) |
| Invoice notation | "Outside the scope of VAT -- services supplied to a customer outside the EU" or equivalent |
| Input VAT recovery | Seller retains FULL right to recover input VAT on costs related to these out-of-scope supplies (they are not exempt supplies) |
| Reporting | Report on the VAT return in the out-of-scope / non-EU sales box (e.g., Malta Box 2, Germany KZ 45, France Line E1) |
| ESL / Intrastat | NOT required (not an intra-EU supply) |

### B2C: Seller (any EU country) to Non-EU Private Consumer [T2]

| Service Type | Place of Supply | VAT Charged |
|-------------|-----------------|-------------|
| Consulting, IT, legal, accounting, engineering, advertising, data processing, information supply | Client's country (Art 59) | None -- outside scope |
| Telecoms, broadcasting, ESS | Client's country (Art 58) | None -- outside scope (but may trigger registration in client's country if it has its own rules) |
| Land-related services | Where property is located (Art 47) | If property is in EU: EU VAT applies regardless of client location [T2] |
| Event admission | Where event takes place (Art 53) | If event is in EU: EU VAT applies |
| Restaurant/catering | Where performed (Art 55) | If performed in EU: EU VAT applies |
| Passenger transport | Where transport occurs (Art 48) | If in EU: EU VAT applies proportionally |
| All other services (e.g., personal services) | Seller's country (Art 45) | Seller's domestic VAT rate applies -- EVEN if client is outside EU [T2] |

**Critical distinction:** For B2C, only certain "listed services" under Art 59 shift the place of supply to the consumer's country. Other services remain taxable in the seller's country even if the consumer is abroad. This catches out many freelancers.

### Country-Specific Box Mappings (EU Sellers) [T1]

| Seller Country | VAT Return Box for Non-EU Services | Notes |
|---------------|-----------------------------------|-------|
| Malta (MT) | Box 2 | Non-EU supplies |
| Germany (DE) | KZ 45 (nicht steuerbare sonstige Leistungen) | Out-of-scope services |
| France (FR) | Cadre E / Line E1 | Opérations non imposables |
| Italy (IT) | VE30 field 4 / Esterometro | Operazioni non imponibili |
| Slovakia (SK) | Row 15 (not subject to SK VAT) | Out of scope |

---

## Step 3: UK Seller to Non-UK Client [T1]

**Legislation:** Value Added Tax Act 1994, s7, s8, Schedule 4A; VAT Place of Supply of Services Order 1992 (as amended post-Brexit).

### B2B: UK Seller to Any Non-UK Business [T1]

| Rule | Detail |
|------|--------|
| Place of supply | Client's country (s7(10) VATA 1994, general B2B rule) |
| VAT charged | None -- outside the scope of UK VAT |
| Invoice notation | "Outside the scope of UK VAT" |
| Input VAT recovery | Full recovery retained on related costs |
| VAT return | Box 6 (total value of sales excluding VAT) -- include the value. Do NOT include in Box 1 (output tax). |

### B2C: UK Seller to Non-UK Consumer [T2]

Similar to EU rules: "listed services" (consulting, IT, legal, etc.) shift to the consumer's country and are outside the scope of UK VAT. Other services (e.g., personal services performed in the UK) remain subject to UK VAT even if the consumer is abroad.

### Post-Brexit Note [T1]

Since 1 January 2021, the UK is outside the EU VAT system. An EU client of a UK seller does NOT use the reverse charge under Art 196. Instead, the EU client self-assesses under their domestic rules for services received from outside the EU (similar to non-EU acquisition reverse charge).

---

## Step 4: Australian Seller to Non-Australian Client [T1]

**Legislation:** A New Tax System (Goods and Services Tax) Act 1999, Division 38, Subdivision 38-E.

### GST-Free Export of Services (Div 38-190) [T1]

A supply of services is GST-free (zero-rated) if:

1. The supply is made to a **non-resident** who is NOT in Australia when the service is performed, AND
2. The supply is NOT a supply of a right or option to acquire something the supply of which would be connected with Australia, AND
3. The effective use or enjoyment of the supply is NOT in Australia.

| Condition | Test |
|-----------|------|
| Non-resident recipient | Client's registered address or usual place of business is outside Australia |
| Not in Australia when performed | The client (or their representative) is not physically present in Australia at the time the service is delivered |
| No Australian connection | The service does not relate to real property in Australia, does not involve work physically performed on goods in Australia |

### Reporting [T1]

- GST-free exports appear in **G2 (Export sales)** on the BAS (Business Activity Statement).
- Input tax credits (GST on costs) are FULLY recoverable.
- No GST is charged on the invoice.

### Common Scenario [T1]

An Australian freelance developer provides software development services to a US company. The developer works from Australia. The client is in the US and the software is used in the US. **Result:** GST-free under Div 38-190. Invoice AUD amount, no GST.

---

## Step 5: Indian Seller to Non-Indian Client [T1]

**Legislation:** Integrated Goods and Services Tax Act 2017, Section 2(6) (definition of export of services); Section 16 (zero-rating).

### Export of Services -- Conditions [T1]

A supply of services qualifies as an "export of services" (zero-rated) if ALL of the following are met:

| Condition | Requirement |
|-----------|-------------|
| 1. Supplier location | Supplier is located in India |
| 2. Recipient location | Recipient is located outside India |
| 3. Place of supply | Place of supply is outside India (under the IGST place of supply rules) |
| 4. Payment | Payment is received in convertible foreign exchange or Indian rupees (where permitted by RBI) |
| 5. Not merely an establishment | Supplier and recipient are not merely establishments of the same person |

### Two Options for Zero-Rating [T1]

| Option | Treatment | LUT/Bond |
|--------|-----------|----------|
| Export WITH payment of IGST | Charge IGST at applicable rate, then claim refund from government | No LUT needed |
| Export WITHOUT payment of IGST (under LUT/Bond) | Do not charge IGST; file under Letter of Undertaking (LUT) | LUT filed annually via Form GST RFD-11 |

**Recommended for freelancers:** File LUT annually and export without charging IGST. Avoids the cash flow burden of paying IGST and waiting for refund.

### Reporting [T1]

- Report in GSTR-1 under "Exports" table.
- Report in GSTR-3B under "Zero-rated supply."
- Input Tax Credit (ITC) on domestic purchases is FULLY available for refund or adjustment.

### Common Scenario [T1]

An Indian freelance developer provides software development to a US company. Paid in USD. LUT filed. **Result:** Zero-rated. No IGST charged. Full ITC recovery. Report as export in GSTR-1.

---

## Step 6: Singaporean Seller to Non-Singaporean Client [T1]

**Legislation:** Goods and Services Tax Act (Cap 117A), Section 21(3); GST (International Services) Order; Fifth Schedule.

### Zero-Rating Under the Fifth Schedule [T1]

Services are zero-rated (GST at 0%) if they fall under the categories in the Fifth Schedule and are supplied to an overseas person:

| Condition | Test |
|-----------|------|
| Overseas person | Customer does not have a business or fixed establishment in Singapore; or if they do, the service is not for the Singapore establishment |
| Service type | Must be a prescribed international service under the Fifth Schedule (includes most B2B professional services) |

### Key Fifth Schedule Categories [T1]

| Category | Examples |
|----------|----------|
| Para 1 | Services under a contract with an overseas person (catch-all for most B2B services: consulting, IT, accounting, legal, design) |
| Para 2 | Services supplied in connection with goods for export |
| Para 3 | International transport |
| Para 10 | Intellectual property rights |

### Reporting [T1]

- Report in **Box 2** of the GST return (zero-rated supplies).
- Input GST (GST on purchases) is FULLY recoverable.
- No GST charged on the invoice.

### Common Scenario [T1]

A Singaporean UI/UX designer provides design services to a UK company. **Result:** Zero-rated under Fifth Schedule Para 1. No GST. Full input tax recovery.

---

## Step 7: When Export Zero-Rating Does NOT Apply [T2]

The following exceptions apply across most jurisdictions. Even if the client is abroad, VAT/GST may still be charged:

| Exception | Jurisdictions | Reason |
|-----------|--------------|--------|
| **Services related to land/immovable property** | EU (Art 47), UK, AU, IN, SG | Place of supply = where property is located. If property is in seller's country, domestic VAT/GST applies. |
| **Event admission / attendance** | EU (Art 53), UK | Place of supply = where event takes place. If event is in seller's country, domestic VAT applies. |
| **Restaurant and catering** | EU (Art 55), UK | Place of supply = where performed. |
| **Passenger transport** | EU (Art 48), UK, AU | Where transport occurs. |
| **Services performed on goods physically in the seller's country** | AU (Div 38-190 fails), SG | If goods are in Australia/Singapore and the service is performed there, may not be GST-free. |
| **Services where effective use and enjoyment is in seller's country** | AU, SG, UK (anti-avoidance) | If the service is effectively used in the seller's country, export relief may be denied. [T2] |
| **B2C "other services" (not listed services)** | EU (Art 45) | Place of supply = seller's country for unlisted B2C services. Domestic VAT applies even if consumer is abroad. |

---

## Step 8: Country-Specific Worked Examples [T1]

### Example 1 -- Malta IT freelancer to US client (B2B) [T1]
**Facts:** Maltese IT consultant provides remote software development to a US company. Invoices EUR 5,000 monthly.
**Treatment:** Place of supply = US (Art 44, B2B). Outside the scope of Malta VAT. Invoice 0% VAT. Report in Box 2. Full input VAT recovery on Malta costs.

### Example 2 -- German designer to Japanese client (B2B) [T1]
**Facts:** German graphic designer invoices a Japanese company EUR 3,000 for branding work.
**Treatment:** Place of supply = Japan (Art 44, B2B). Outside the scope of German VAT. Report in KZ 45. No output VAT.

### Example 3 -- UK accountant to Australian client (B2B) [T1]
**Facts:** UK chartered accountant provides tax advisory services to an Australian company. Invoices GBP 10,000.
**Treatment:** Place of supply = Australia (s7(10) VATA 1994). Outside the scope of UK VAT. Include value in Box 6 but not Box 1.

### Example 4 -- Australian developer to Canadian client (B2B) [T1]
**Facts:** Australian freelance developer provides app development to a Canadian company. Invoices AUD 20,000.
**Treatment:** GST-free under Div 38-190. Client is non-resident, not in Australia, service not connected with Australia. Report in G2 on BAS. No GST.

### Example 5 -- Indian developer to UK client (B2B) [T1]
**Facts:** Indian software company provides development services to a UK client. Invoices USD 10,000. LUT filed.
**Treatment:** Export of services under IGST s2(6). All 5 conditions met. Zero-rated (no IGST under LUT). Report in GSTR-1 exports table. Full ITC recovery.

### Example 6 -- Singaporean consultant to German client (B2B) [T1]
**Facts:** Singaporean management consultant provides advisory services to a German company. Invoices SGD 15,000.
**Treatment:** Zero-rated under Fifth Schedule Para 1. Client is overseas person. No GST. Report in Box 2.

### Example 7 -- French architect, property in Switzerland (Exception) [T2]
**Facts:** French architect designs a building to be constructed in Switzerland for a Swiss client. Invoices EUR 20,000.
**Treatment:** Service related to immovable property (Art 47). Place of supply = Switzerland (where property is). Outside the scope of French VAT. BUT: Swiss VAT may apply -- architect may need to register for Swiss VAT. Flag T2.

### Example 8 -- Maltese trainer, in-person event in Malta for US client [T2]
**Facts:** Maltese company organises a 3-day training event in Malta. Attendees are from a US company. Invoices EUR 10,000.
**Treatment:** If classified as event admission (Art 53): place of supply = Malta, charge Maltese VAT 18%. If classified as a bespoke training service (B2B, Art 44): place of supply = US, no Malta VAT. Flag T2 -- classification depends on whether the event is "open to the public" or bespoke.

---

## PROHIBITIONS

1. **NEVER** charge domestic VAT/GST on a standard B2B service export without checking the place of supply rule. The default for B2B services is the client's country.
2. **NEVER** assume that "zero-rated" and "exempt" are the same. Zero-rated / out-of-scope exports preserve input tax recovery. Exempt supplies do NOT.
3. **NEVER** forget to report export services on the VAT/GST return. Even though no tax is charged, the value must be reported.
4. **NEVER** assume all B2C services to foreign consumers are outside the scope. In the EU, only "listed services" (Art 59) shift to the consumer's country. Other B2C services remain taxable in the seller's country.
5. **NEVER** zero-rate a service related to land/property in the seller's country. Place of supply = where the property is located.
6. **NEVER** advise an Indian exporter to skip the LUT filing -- without LUT, IGST must be charged and then refunded, creating cash flow problems.
7. **NEVER** assume that GST-free status in Australia extends to services where the effective use and enjoyment is in Australia.

---

## Edge Cases

### EC1 -- Service partly performed in seller's country, partly abroad [T2]
**Situation:** An Australian consultant travels to Singapore for 2 weeks to deliver a project, then works from Australia for 4 weeks. Client is a Singaporean company.
**Resolution:** Under Div 38-190, the entire supply may still be GST-free if the recipient (SG company) is not in Australia when the services are performed. The 2 weeks in Singapore strengthen the export position. However, if part of the service benefit is enjoyed in Australia, IRAS/ATO may challenge. Flag for reviewer.

### EC2 -- EU freelancer sells B2C to a US consumer (non-listed service) [T2]
**Situation:** A French yoga instructor provides a private in-person yoga session in Paris to a US tourist. The service is not a "listed service" under Art 59.
**Resolution:** Place of supply = France (Art 45, seller's country, B2C non-listed service). French VAT at 20% applies, even though the client is a US resident. The fact that the client is foreign does NOT make it an export.

### EC3 -- Indian freelancer paid in INR, not foreign exchange [T1]
**Situation:** Indian developer provides services to a Dubai-based client but receives payment in INR.
**Resolution:** Under IGST s2(6), payment must be received in convertible foreign exchange OR in INR where permitted by RBI. If payment in INR is not permitted by RBI for this transaction, the supply does NOT qualify as "export of services" and IGST must be charged. Check RBI guidelines.

### EC4 -- UK seller to EU client post-Brexit [T1]
**Situation:** UK web developer invoices a French company for services post-Brexit.
**Resolution:** The supply is outside the scope of UK VAT (place of supply = France, B2B). The French company must self-assess French VAT under French domestic reverse charge rules for services from outside the EU. The UK developer does NOT charge UK VAT and does NOT use the EU reverse charge mechanism.

### EC5 -- Singaporean seller, client has a Singapore branch [T2]
**Situation:** A Singaporean advertising agency provides services to an overseas parent company, but the parent has a branch office in Singapore.
**Resolution:** Under the Fifth Schedule, the supply is zero-rated only if it is NOT supplied directly in connection with the Singapore branch's activities. If the Singapore branch is the effective recipient or beneficiary, zero-rating may be denied. Flag for reviewer.

---

## Test Suite

### Test 1 -- Standard B2B, Malta to US
**Input:** Maltese sole trader provides IT consulting to a US company. Invoice EUR 3,000.
**Expected:** Outside the scope of Malta VAT. Box 2 = EUR 3,000. No output VAT. Full input VAT recovery.

### Test 2 -- B2C, French seller to US consumer (Art 59 listed service)
**Input:** French consultant provides remote data processing services to a US individual. Invoice EUR 1,000.
**Expected:** Art 59 listed service. Place of supply = US (consumer's country). Outside scope of French VAT. No VAT charged.

### Test 3 -- Indian export with LUT
**Input:** Indian developer invoices US client USD 5,000. LUT filed. Payment in USD.
**Expected:** Zero-rated export. No IGST. Report in GSTR-1 exports. Full ITC recovery.

### Test 4 -- Australian GST-free export
**Input:** Australian designer invoices UK company AUD 8,000 for logo design. Client not in Australia.
**Expected:** GST-free under Div 38-190. G2 on BAS. No GST.

### Test 5 -- Exception: property-related service
**Input:** UK surveyor surveys a building located in the UK for a Singaporean buyer. Invoice GBP 5,000.
**Expected:** Service related to land in the UK (Sch 4A, VATA 1994). UK VAT at 20% = GBP 1,000. Total invoice GBP 6,000. NOT an export -- place of supply is UK regardless of client location.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your export VAT position, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
