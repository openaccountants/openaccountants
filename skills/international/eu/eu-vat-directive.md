---
name: eu-vat-base
description: Load this skill as a shared reference whenever working on VAT for any EU member state. Contains the common rules from Council Directive 2006/112/EC that apply across all 27 EU member states — intra-community acquisitions, reverse charge mechanics, place of supply rules, OSS, distance selling thresholds, and EU country list. Always load the country-specific VAT skill alongside this one. Do NOT use this skill alone — it must be combined with the relevant country skill (e.g. ireland-vat-return, germany-vat-return) which overrides anything country-specific.
---

# EU VAT Base — Common Rules (Directive 2006/112/EC)

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Scope | All 27 EU Member States |
| Primary Legislation | Council Directive 2006/112/EC of 28 November 2006 (consolidated to 14 April 2025) |
| Supporting Legislation | Directive 2022/542/EU (reduced rates reform); Implementing Regulation 282/2011 |
| Source | EUR-Lex: https://eur-lex.europa.eu/eli/dir/2006/112/oj/eng |
| Contributor | Open Accounting Skills Registry |
| Version | 1.0 |
| Rates Current As Of | 1 January 2026 |
| Status | awaiting-validation |
| Note | This skill contains ONLY rules common to all EU member states. Country-specific rules (form boxes, national rates, filing deadlines, small business thresholds) are in the country skill. The country skill overrides this one where there is any conflict. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Derived directly from the Directive. Applies in all member states unless the country skill specifies otherwise.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Rule exists in the Directive but national implementation varies. Check the country skill.
- **[T3] Tier 3 -- Out of Scope.** Not covered by this skill. Refer to country skill or warranted practitioner.

---

## Section 1: EU Member State List [T1]

**Legislation:** Directive 2006/112/EC, Article 1

Current EU member states (27) for counterparty location classification:

AT Austria | BE Belgium | BG Bulgaria | HR Croatia | CY Cyprus | CZ Czech Republic | DK Denmark | EE Estonia | FI Finland | FR France | DE Germany | GR Greece | HU Hungary | IE Ireland | IT Italy | LV Latvia | LT Lithuania | LU Luxembourg | MT Malta | NL Netherlands | PL Poland | PT Portugal | RO Romania | SK Slovakia | SI Slovenia | ES Spain | SE Sweden

**NOT EU (treat as non-EU / third country):**
- UK (left EU 31 January 2020)
- Norway, Switzerland, Iceland (EEA but not EU)
- USA, Canada, Australia, UAE, and all other non-EU countries

---

## Section 2: VAT Rate Framework [T1]

**Legislation:** Directive 2006/112/EC, Articles 96-99; Directive 2022/542/EU

### Rate Structure Rules (apply in all member states)

| Rule | Detail |
|------|--------|
| Standard rate minimum | Cannot be lower than 15% (Article 97) |
| Reduced rates | Maximum two reduced rates, neither below 5% |
| Super-reduced rate | Below 5% -- only permitted for specific categories under Annex III derogations |
| Zero rate | Permitted for specific categories under acquired rights |
| Parking rate | Minimum 12% -- applies in some member states to transitional categories |

### 2026 Rate Table -- All EU Member States

| Country | Code | Standard | Reduced 1 | Reduced 2 | Super-Reduced | Zero |
|---------|------|----------|-----------|-----------|---------------|------|
| Austria | AT | 20% | 10% | 13% | -- | Yes |
| Belgium | BE | 21% | 6% | 12% | -- | Yes |
| Bulgaria | BG | 20% | 9% | -- | -- | Yes |
| Croatia | HR | 25% | 5% | 13% | -- | Yes |
| Cyprus | CY | 19% | 5% | 9% | -- | Yes |
| Czech Republic | CZ | 21% | 12% | -- | -- | Yes |
| Denmark | DK | 25% | -- | -- | -- | Yes |
| Estonia | EE | 24% | 9% | -- | -- | Yes |
| Finland | FI | 25.5% | 13.5% | -- | -- | Yes |
| France | FR | 20% | 5.5% | 10% | 2.1% | Yes |
| Germany | DE | 19% | 7% | -- | -- | Yes |
| Greece | GR | 24% | 6% | 13% | -- | Yes |
| Hungary | HU | 27% | 5% | 18% | -- | Yes |
| Ireland | IE | 23% | 9% | 13.5% | -- | Yes |
| Italy | IT | 22% | 5% | 10% | 4% | Yes |
| Latvia | LV | 21% | 12% | 5% | -- | Yes |
| Lithuania | LT | 21% | 5% | 12% | -- | Yes |
| Luxembourg | LU | 16% | 8% | -- | 3% | Yes |
| Malta | MT | 18% | 5% | 7% | -- | Yes |
| Netherlands | NL | 21% | 9% | -- | -- | Yes |
| Poland | PL | 23% | 5% | 8% | -- | Yes |
| Portugal | PT | 23% | 6% | 13% | -- | Yes |
| Romania | RO | 19% | 5% | 9% | -- | Yes |
| Slovakia | SK | 23% | 5% | 19% | -- | Yes |
| Slovenia | SI | 22% | 5% | 9.5% | -- | Yes |
| Spain | ES | 21% | 10% | -- | 4% | Yes |
| Sweden | SE | 25% | 6% | 12% | -- | Yes |

**Note:** Rates current as of 1 January 2026. Always verify current rates against the European Commission's TEDB (Taxes in Europe Database) before filing.

---

## Section 3: Intra-Community Acquisitions (ICA) [T1]

**Legislation:** Directive 2006/112/EC, Articles 2(1)(b), 20, 40-42

### Definition
An ICA occurs when physical goods are dispatched or transported from one EU member state to another, between two VAT-registered businesses (B2B).

### Rules
- The place of ICA is where transport ends (Article 40)
- The acquiring business is liable for VAT via reverse charge
- The supplier invoices at 0% (zero-rated intra-community supply)
- The acquirer self-assesses output VAT at their local standard rate AND claims the same amount as input VAT
- Net cash effect = zero for a fully taxable business
- The supplier must quote the customer's VAT number on the invoice
- The supplier must report the sale on an EC Sales List (ESL) / Recapitulative Statement

### Invoice Reference
Supplier invoice must state: **"VAT exempt intra-Community supply -- Article 138(1) Directive 2006/112/EC"**

---

## Section 4: Reverse Charge -- Cross-Border Services (B2B) [T1]

**Legislation:** Directive 2006/112/EC, Articles 44, 196

### The General B2B Rule (Article 44)
For services supplied B2B across EU borders, the place of supply is where the **customer** is established.

Consequence: The supplier charges 0% VAT. The customer self-assesses output VAT at their local rate and claims the same as input VAT. Net effect = zero for a fully taxable business.

### Mandatory for
- All B2B cross-border services where Article 44 applies
- Services supplied by a non-EU supplier to an EU VAT-registered customer

### Invoice Reference
Supplier invoice must state: **"VAT exempt intra-Community supply of services -- Articles 44 and 196 Directive 2006/112/EC"** or simply **"Reverse charge"**

### Exceptions to Article 44 (place where service is physically performed) [T2]
These services are taxed where performed, not where the customer is established:

| Service Type | Place of Supply | Directive Article |
|-------------|----------------|-------------------|
| Services related to immovable property | Where property is located | Article 47 |
| Passenger transport | Distance covered | Article 48 |
| Restaurant / catering services | Where physically carried out | Article 55 |
| Short-term hire of transport | Where vehicle put at disposal | Article 56 |
| Admission to cultural / sports events | Where event takes place | Article 53 |

[T2] For any of these exception categories, flag for reviewer to confirm correct place of supply treatment.

---

## Section 5: Reverse Charge -- Non-EU Supplier to EU Business [T1]

**Legislation:** Directive 2006/112/EC, Articles 44, 196

When a non-EU supplier (US, UK, CH, AU etc.) provides services to an EU VAT-registered business:
- Supplier invoices at 0% (no EU VAT charged)
- EU customer self-assesses output VAT at local rate
- EU customer claims same amount as input VAT (if fully taxable)
- Net effect = zero for fully taxable business
- This applies to: software subscriptions (AWS, Google, Microsoft, Notion, Slack), consulting services, digital services, IP licences

**Common examples:** AWS, Google Workspace, Microsoft 365, Notion, Slack, Stripe fees, LinkedIn ads -- all trigger reverse charge when purchased by an EU VAT-registered business.

---

## Section 6: Distance Selling -- B2C Cross-Border [T1]

**Legislation:** Directive 2006/112/EC, Articles 33, 59c; OSS rules

### The EUR 10,000 Threshold
If a supplier's total B2C distance sales across ALL EU countries combined exceed EUR 10,000 per calendar year:
- Must apply VAT at the rate of the **customer's** country (destination principle)
- Must either register in each destination country OR use the OSS (One Stop Shop)

Below EUR 10,000: apply VAT at the supplier's own country rate.

### One Stop Shop (OSS)
Allows a supplier to register in one EU member state and declare and pay VAT for all EU B2C distance sales through that single registration. Eliminates the need to register separately in every customer's country.

[T2] If client makes significant B2C sales across EU: flag for reviewer to assess OSS registration requirement.

---

## Section 7: EC Sales List / Recapitulative Statement [T1]

**Legislation:** Directive 2006/112/EC, Articles 262-265

Every VAT-registered business that makes intra-community supplies (ICA or B2B services under Article 44) must file an EC Sales List (called Recapitulative Statement in the Directive) reporting:
- Customer VAT numbers
- Total value supplied to each customer
- Period covered

Filing frequency and format varies by country -- check country skill.

---

## Section 8: Local Consumption Exception [T1]

**Legislation:** Directive 2006/112/EC, Articles 52-54 (services); Article 32 (goods)

When a business pays for services consumed locally in another EU country (hotel, restaurant, taxi, conference admission), the VAT is charged locally by the supplier at their national rate. This is NOT reverse charge.

Examples:
- Employee stays in a Paris hotel -- French VAT charged, not reverse charge
- Delegate attends a Berlin conference -- German VAT charged, not reverse charge
- Business lunch in Amsterdam -- Dutch VAT charged, not reverse charge

The foreign VAT paid is an expense (generally irrecoverable unless the business files a cross-border VAT refund claim under Directive 2008/9/EC).

[T2] Cross-border VAT refund claims: possible for EU businesses but requires separate process. Flag for reviewer if amounts are material.

---

## Section 9: Import of Physical Goods from Non-EU [T2]

**Legislation:** Directive 2006/112/EC, Articles 70-71; national customs legislation

When physical goods are imported from outside the EU:
- Import VAT is charged at the border by Customs, not via reverse charge on the VAT return
- Import VAT is paid to Customs at the point of entry
- The business recovers import VAT as input tax via the VAT return (using the Customs entry document)
- Reverse charge on the VAT return is NOT used for physical goods imports

[T2] Process and documentation varies by country. Flag for reviewer to confirm: (a) client has the customs entry document, (b) import VAT amount is correct, (c) recovery is allowable.

---

## Section 10: VAT Number Validation [T1]

**Legislation:** Directive 2006/112/EC, Article 18

Before applying zero rate (ICA or B2B services):
- Verify the customer's VAT number is valid using the EU VIES system: https://ec.europa.eu/taxation_customs/vies/
- A valid VAT number is a prerequisite for zero-rating
- If VIES validation fails, do not zero-rate -- apply local VAT rate

---

## Section 11: Blocked Categories -- Common EU Rules [T1/T2]

**Legislation:** Directive 2006/112/EC, Articles 176-177

The Directive permits member states to maintain restrictions on input tax deduction that existed before 1979 (standstill clause). As a result, blocked categories vary significantly by country.

Common categories blocked in most EU member states [T1]:
- Entertainment expenses (client meals, hospitality)
- Personal use items

Categories blocked in some but not all member states [T2]:
- Motor vehicles (blocked in some, partially allowed in others)
- Fuel (varies by country and vehicle type)
- Accommodation (varies)

**Always check the country skill for the specific blocked categories for that jurisdiction.**

---

## Section 12: Invoicing Requirements [T1]

**Legislation:** Directive 2006/112/EC, Articles 219a-237

Mandatory invoice elements for all EU member states:
- Date of issue
- Sequential invoice number
- Supplier VAT number
- Customer VAT number (for B2B intra-community supplies)
- Full name and address of supplier and customer
- Description of goods or services
- Date of supply (if different from invoice date)
- Taxable amount per VAT rate
- VAT rate applied
- VAT amount in the currency of the invoice
- For zero-rated intra-community supplies: reference to exemption (Article 138 or 44/196)
- For reverse charge: statement "Reverse charge"

[T2] E-invoicing mandates vary by country and are being introduced progressively across the EU. Check country skill for any mandatory e-invoicing requirements.

---

## PROHIBITIONS

- NEVER zero-rate an intra-community supply without a valid customer VAT number verified on VIES
- NEVER apply reverse charge to services consumed locally in another EU country (hotel, restaurant, taxi)
- NEVER apply reverse charge to physical goods imports -- import VAT is handled via Customs
- NEVER use this skill alone -- always load the country skill alongside it
- NEVER override the country skill with this base skill -- the country skill takes precedence on all national specifics
- NEVER present EU-wide rules as applying without exception -- national derogations exist and are significant

---

## Gap Report

| Area | Status |
|------|--------|
| Core Directive rules | T1 -- sourced from EUR-Lex consolidated text |
| 2026 rate table | T1 -- sourced from European Commission TEDB and multiple verified sources |
| OSS / IOSS detail | T2 -- covered at high level only; detailed country implementation in country skills |
| Intrastat thresholds | T3 -- not covered; varies by country; add to country skills |
| SAF-T / e-invoicing mandates | T3 -- not covered; varies significantly by country |
| VAT groups | T3 -- not covered; varies by country |
| Capital goods adjustment period | T3 -- varies by country; covered in country skills |

**Practitioner review required for:** rate table accuracy (verify against EC TEDB), any T2 rules before advising clients.
