---
name: nigeria-vat
description: Use this skill whenever asked to prepare, review, or create a Nigeria VAT return for any client. Trigger on phrases like "prepare VAT return", "Nigeria VAT", "FIRS return", "file VAT Nigeria", "withholding VAT", or any request involving Nigerian VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Nigeria VAT classification rules, return structure, withholding VAT mechanics, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Nigeria VAT-related work.
---

# Nigeria VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Federal Republic of Nigeria |
| Jurisdiction Code | NG |
| Primary Legislation | Nigeria Tax Act 2025 (NTA), signed 26 June 2025, effective 1 January 2026; formerly Value Added Tax Act (Cap V1 LFN 2004), as amended by Finance Acts 2019, 2020, 2023 |
| Supporting Legislation | Nigeria Tax Administration Act 2025 (NTAA); Nigeria Revenue Service Act 2025 (NRSA); Joint Revenue Board Act 2025 (JRBA); former FIRS Information Circulars (transitional reference) |
| Tax Authority | Nigeria Revenue Service (NRS) -- formerly Federal Inland Revenue Service (FIRS), renamed under NRSA 2025 |
| Filing Portal | https://taxpromax.firs.gov.ng (TaxProMax -- transitioning to NRS portal) |
| Standard VAT Rate | 7.5% (effective 1 February 2020; previously 5%) |
| Currency | Nigerian Naira (NGN) |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: classification, withholding VAT, exempt/zero-rated lists, filing. Tier 2: complex supplies, cross-border services, partial exemption. Tier 3: transfer pricing, sector-specific rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A chartered accountant or tax advisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to chartered accountant/tax advisor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Tax Identification Number)** [T1] -- Issued by Joint Tax Board or FIRS
2. **VAT registration status** [T1] -- All taxable persons making taxable supplies must register; no threshold for registration itself, but turnover determines filing obligations
3. **VAT filing period** [T1] -- Monthly (all VAT-registered persons)
4. **Industry/sector** [T2] -- Impacts exempt supply classification (e.g., banking, oil/gas, telecommunications, agriculture)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input VAT recovery restrictions apply
6. **Is the business a government agency or designated "large taxpayer"?** [T1] -- Determines withholding VAT obligations
7. **Does the business import services from non-residents?** [T1] -- Self-accounting (reverse charge) applies
8. **Excess credit brought forward** [T1] -- From prior period
9. **Does the client operate in a free trade zone?** [T2] -- May affect treatment of certain supplies
10. **Is the client an appointed withholding VAT agent?** [T1] -- If yes, must withhold and remit VAT on purchases

**Legislation:** VAT Act, Sections 7-10 (registration); Finance Act 2019, Section 34 (amendments).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, pension contributions, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act, Section 1 (charge of VAT); Section 2 (taxable goods and services)

### 1b. Determine Counterparty Location [T1]
- Nigeria (local): supplier/customer within Nigeria
- ECOWAS: West African states (no VAT reciprocity mechanism exists)
- International: all other countries
- **Note:** Nigeria does not have a regional VAT framework like the EU or GCC. Each transaction is domestic or international.
- **Legislation:** VAT Act, Section 2; Finance Act 2020, Section 39 (place of supply for services)

### 1c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Standard rate: 7.5%
- Zero rate: 0% (with input VAT recovery)
- Exempt: no VAT charged, no input VAT recovery
- Out of scope: not a supply for VAT purposes
- **Legislation:** VAT Act, Section 4 (rate); Finance Act 2019, Section 33 (rate increase to 7.5%)

### 1d. Withholding VAT Status [T1]
- Check if the purchasing entity is a designated withholding VAT agent
- If yes, purchaser withholds VAT at source and remits directly to FIRS
- **Legislation:** FIRS Information Circular 2004/02; Finance Act 2019

---

## Step 2: VAT Return Form Structure (FIRS Form) [T1]

The Nigeria VAT return is filed monthly via TaxProMax. The form captures:

### Section A: Output VAT (Sales)

| Line | Description | Notes |
|------|-------------|-------|
| A1 | Value of standard rated supplies | Taxable sales at 7.5% |
| A2 | Value of zero-rated supplies | Exports and diplomatic supplies |
| A3 | Value of exempt supplies | Per First Schedule to VAT Act |
| A4 | Total value of supplies | A1 + A2 + A3 |
| A5 | Output VAT charged | A1 x 7.5% |

### Section B: Input VAT (Purchases)

| Line | Description | Notes |
|------|-------------|-------|
| B1 | Value of standard rated purchases (local) | Domestic purchases at 7.5% |
| B2 | Value of imported goods/services (self-accounted) | Reverse charge amounts |
| B3 | Value of zero-rated purchases | Zero-rated purchases |
| B4 | Value of exempt purchases | Purchases of exempt items |
| B5 | Total value of purchases | B1 + B2 + B3 + B4 |
| B6 | Input VAT on purchases | (B1 + B2) x 7.5% |

### Section C: VAT Withheld

| Line | Description | Notes |
|------|-------------|-------|
| C1 | VAT withheld at source by customers | VAT deducted by withholding agents on client's sales |
| C2 | VAT withheld by client on purchases | VAT withheld by client (if appointed agent) |

### Section D: Net VAT

| Line | Description | Notes |
|------|-------------|-------|
| D1 | Net VAT payable | A5 - B6 - C1 |
| D2 | Credit carried forward | If D1 is negative |

**Legislation:** VAT Act, Section 14 (returns); FIRS TaxProMax filing guidelines.

---

## Step 3: Supply Classification Matrix [T1]

### Zero-Rated Supplies (0% VAT, input tax recoverable)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods physically exported from Nigeria | NTA 2025; formerly VAT Act, Section 2(1) |
| Goods for humanitarian donor-funded projects | Supplies to approved humanitarian projects | NTA 2025; formerly Finance Act 2019, Section 35 |
| Goods/services to diplomatic missions | Supplies to accredited diplomatic missions with valid exemption certificate | NTA 2025 |
| Basic food items and consumables | Food and basic consumables (reclassified from exempt to zero-rated under NTA 2025, effective 1 January 2026) -- enables input VAT recovery | NTA 2025 |
| Medical and pharmaceutical products | Medicines, medical devices, hospital equipment (reclassified from exempt to zero-rated under NTA 2025) | NTA 2025 |
| Educational materials | Books, newspapers, educational supplies (reclassified from exempt to zero-rated under NTA 2025) | NTA 2025 |
| Agricultural equipment and inputs | Fertilizers, seeds, pesticides, tractors, agricultural machinery (reclassified from exempt to zero-rated under NTA 2025) | NTA 2025 |

**IMPORTANT NOTE (NTA 2025 Transition):** The Nigeria Tax Act 2025 (effective 1 January 2026) reclassified several categories that were previously VAT-exempt (basic food, medical products, educational materials, agricultural inputs) as zero-rated. This is a significant change: suppliers of these goods can now recover input VAT on their costs, whereas previously they could not. The exempt categories listed below reflect items that remain exempt (no input recovery) under the NTA.

### Exempt Supplies (no VAT, no input recovery) -- NTA 2025 (effective 1 January 2026)

**NOTE:** Under the NTA 2025, several categories previously exempt (basic food, medical/pharmaceutical, educational materials, agricultural equipment) have been reclassified as ZERO-RATED (see above). The following remain exempt:

#### Exempt Goods

| Category | Description | Legislation |
|----------|-------------|-------------|
| Baby products | Baby food, baby clothing, diapers, feeding bottles | NTA 2025 |
| Veterinary medicines | Veterinary pharmaceuticals and supplies | NTA 2025 |
| Plant and machinery for use in EPZs | Equipment imported for use in Export Processing Zones | NTA 2025 |
| Locally manufactured sanitary towels | Feminine hygiene products produced in Nigeria | NTA 2025 |

#### Exempt Services

| Category | Description | Legislation |
|----------|-------------|-------------|
| Healthcare services | Services provided by hospitals, clinics, medical practitioners (exempt; medicines and products are now zero-rated) | NTA 2025 |
| Educational services | Tuition and related services by educational institutions (exempt; educational materials are now zero-rated) | NTA 2025 |
| Passenger road transport | Public passenger transport services | NTA 2025 |
| Plays and performances by educational institutions | Cultural performances for educational purposes | NTA 2025 |

### Out of Scope

| Category | Notes |
|----------|-------|
| Salaries, wages, PAYE | Employment, not a supply |
| Dividends | Return on investment |
| Pension contributions | Statutory deductions |
| Loan repayments (principal) | Financial transaction |
| Government levies/fines | Sovereign functions |
| Intra-company transfers | Not a supply (same legal entity) |

**Legislation:** VAT Act, First Schedule; Finance Act 2019, Sections 33-36; Finance Act 2020, Sections 38-41.

---

## Step 4: Withholding VAT Mechanism [T1]

### What is Withholding VAT?

Withholding VAT is a mechanism where designated agents deduct VAT at source from payments to suppliers and remit it directly to FIRS on behalf of the supplier. The supplier receives payment net of VAT.

### Who Must Withhold VAT? [T1]

The following entities are designated withholding VAT agents:

| Agent Category | Description | Legislation |
|----------------|-------------|-------------|
| Government ministries, departments, agencies (MDAs) | All federal, state, and local government bodies | FIRS Circular 2004/02 |
| Oil and gas companies | International oil companies (IOCs) and major operators | FIRS Circular 2004/02 |
| Telecommunications companies | MTN, Airtel, Glo, 9mobile, and similar | FIRS designation |
| Banks and financial institutions | All licensed banks, insurance companies | FIRS designation |
| Nigerian National Petroleum Corporation (NNPC) | And subsidiaries | FIRS designation |
| Other large taxpayers | As specifically designated by FIRS | FIRS designation |

### How Withholding VAT Works [T1]

1. Supplier issues invoice including 7.5% VAT
2. Withholding agent deducts the VAT portion from payment
3. Withholding agent remits the deducted VAT to FIRS within 21 days
4. Withholding agent issues a withholding VAT credit note to the supplier
5. Supplier records the withholding VAT credit note as VAT already remitted
6. Supplier reports the full output VAT on their return and offsets the withheld amount in Section C1

### Example [T1]

```
Invoice amount (net):          NGN 1,000,000
VAT at 7.5%:                   NGN    75,000
Gross invoice:                 NGN 1,075,000

Withholding agent pays supplier: NGN 1,000,000 (net, VAT withheld)
Withholding agent remits to FIRS: NGN    75,000
Supplier receives credit note for: NGN    75,000
```

### Supplier's VAT Return Treatment [T1]

- Section A: Report full output VAT (NGN 75,000) in A5
- Section C1: Report VAT withheld (NGN 75,000) in C1
- Section D1: Net = A5 - B6 - C1

**Legislation:** FIRS Information Circular 2004/02; VAT Act, Section 14(3).

---

## Step 5: Reverse Charge (Self-Accounting) on Imported Services [T1]

### When Self-Accounting Applies

A Nigerian business that receives services from a non-resident supplier must self-account for VAT at 7.5% on the value of the services.

**Legislation:** Finance Act 2019, Section 34(2) (amendment to VAT Act, Section 10); Finance Act 2020, Section 39.

### Self-Accounting Steps

1. Determine the value of services received from the non-resident
2. Calculate VAT at 7.5% on that value
3. Report as output VAT in Section A5 (or as import VAT in B2 depending on FIRS filing format)
4. If the business makes only taxable supplies, claim the same amount as input VAT in B6
5. Net effect: zero for fully taxable businesses

### Exceptions [T1]
- Out-of-scope categories: NEVER self-account
- Services physically performed and consumed outside Nigeria: no Nigerian VAT
- Non-resident supplier registered for VAT in Nigeria: supplier charges VAT directly

### Non-Resident Digital Services [T2]

Non-resident companies providing digital services to Nigerian consumers (B2C) are required to register for VAT in Nigeria and charge 7.5% VAT. This applies to:
- Streaming services (Netflix, Spotify, etc.)
- Online advertising (Google, Meta)
- App stores (Apple, Google)
- Cloud services (when provided to consumers)

**Flag for reviewer:** The enforcement mechanism for non-resident digital services is evolving. Confirm current FIRS enforcement status.

**Legislation:** Finance Act 2021, Section 6; FIRS Guidelines on Non-Resident Digital Services.

---

## Step 6: Input Tax Recovery Rules

### General Rule [T1]

Input VAT incurred on purchases used to make taxable supplies (standard-rated or zero-rated) is recoverable. Input VAT on purchases used to make exempt supplies is NOT recoverable.

**Legislation:** VAT Act, Section 16 (input tax deduction).

### Blocked Input Tax [T1]

Nigeria does not have a formally codified "blocked input tax" list comparable to GCC states. However, the following are not recoverable:

| Category | Reason | Legislation |
|----------|--------|-------------|
| Purchases used for exempt supplies | General rule | VAT Act, Section 16(1) |
| Personal/non-business expenses | Not related to taxable supplies | VAT Act, Section 16(1) |
| Purchases without valid tax invoice | Documentary requirement not met | VAT Act, Section 16(2) |
| VAT charged by unregistered persons | Invalid VAT charge | VAT Act, Section 16(3) |
| Input VAT on entertainment | Not allowable per FIRS practice | FIRS administrative guidance |
| Input VAT on motor vehicles (private use) | Personal consumption | FIRS administrative guidance |

### Partial Exemption (Mixed Supplies) [T2]

If a business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

**Flag for reviewer:** FIRS does not provide detailed regulations on partial exemption methodology. The fraction approach is commonly applied in practice. Confirm with advisor.

**Legislation:** VAT Act, Section 16(1) (by implication).

---

## Step 7: VAT Rates Summary Table [T1]

| Rate | Application | Input Recovery |
|------|-------------|----------------|
| 7.5% (standard) | All taxable supplies not zero-rated or exempt | Yes (subject to rules) |
| 0% (zero-rated) | Exports, diplomatic supplies, humanitarian goods, basic food, medical/pharmaceutical products, educational materials, agricultural inputs (reclassified under NTA 2025) | Yes |
| Exempt | Healthcare services, educational services, passenger transport, baby products, veterinary medicines, EPZ equipment, sanitary products | No |
| Out of scope | Salaries, dividends, pensions, government levies | N/A |

**Legislation:** VAT Act, Section 4; First Schedule; Finance Act 2019.

---

## Step 8: Registration Rules [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Who must register | Every person or body making taxable supplies of goods or services above the threshold | NTA 2025; formerly VAT Act, Section 7 |
| Registration threshold | NGN 50,000,000 annual turnover (effective 1 January 2026 under NTA 2025). Small businesses at or below this threshold are not required to file VAT returns but may voluntarily opt in. Previously no formal threshold existed. | NTA 2025; formerly VAT Act, Section 7 |
| Registration timeline | Within 6 months of commencement of business or exceeding threshold | NTA 2025 |
| Group registration | Not formally provided for under the NTA | N/A |
| Non-resident registration | Required for non-residents making taxable supplies in Nigeria (especially digital services) | NTA 2025; formerly Finance Act 2021, Section 6 |
| Deregistration | On cessation of taxable activity; must notify NRS | NTA 2025 |
| TIN requirement | Must have TIN before VAT registration | NRS administrative requirement |

**Legislation:** VAT Act, Sections 7-10.

---

## Step 9: Filing Deadlines and Penalties [T1]

### Filing Frequency

| Requirement | Detail |
|-------------|--------|
| Filing period | Monthly (all VAT-registered persons) |
| Filing deadline | 21st day of the month following the tax period |
| Payment deadline | Same as filing deadline (21st of following month) |
| Filing method | Electronic via TaxProMax portal |

### Monthly Calendar

| Tax Period | Filing/Payment Deadline |
|------------|------------------------|
| January | 21 February |
| February | 21 March |
| March | 21 April |
| April | 21 May |
| May | 21 June |
| June | 21 July |
| July | 21 August |
| August | 21 September |
| September | 21 October |
| October | 21 November |
| November | 21 December |
| December | 21 January |

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | NGN 50,000 for the first month + NGN 25,000 for each subsequent month | VAT Act, Section 26 |
| Non-remittance of VAT collected | 150% of the amount not remitted + 5% interest per annum above CBN rediscount rate | VAT Act, Section 25 |
| Failure to register | NGN 50,000 for the first month + NGN 25,000 each subsequent month | VAT Act, Section 26 |
| Failure to issue tax invoice | NGN 50,000 per offence | VAT Act, Section 26 |
| Failure to keep records | NGN 50,000 per offence | VAT Act, Section 26 |
| Evasion | Fine of 2x amount evaded + criminal prosecution (up to 5 years imprisonment) | VAT Act, Section 27 |
| Withholding agent failure to remit | 150% of amount not remitted + interest | VAT Act, Section 25; FIRS Circular |

**Legislation:** VAT Act, Sections 25-29.

---

## Step 10: Tax Invoice Requirements [T1]

| Field | Requirement | Legislation |
|-------|-------------|-------------|
| Name and address of supplier | As registered with FIRS | Section 20 |
| TIN of supplier | Tax Identification Number | Section 20 |
| Name and address of customer | Required for B2B | Section 20 |
| Invoice number | Sequential and unique | Section 20 |
| Date of invoice | Date of issue | Section 20 |
| Description of goods/services | Clear description | Section 20 |
| Quantity | For goods | Section 20 |
| Unit price | Exclusive of VAT | Section 20 |
| VAT rate | 7.5% or 0% or Exempt | Section 20 |
| VAT amount | In NGN | Section 20 |
| Total amount | Inclusive of VAT | Section 20 |

**Note:** Nigeria does not have a simplified invoice regime. All tax invoices must meet the full requirements.

**Legislation:** VAT Act, Section 20.

---

## Step 11: Specific Sector Rules

### Oil and Gas [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Crude oil exports | Zero-rated (export) | VAT Act, Section 2 |
| Domestic sale of refined petroleum products | Standard rated (7.5%) -- BUT Premium Motor Spirit (PMS/petrol) is effectively zero-rated due to government policy | Section 4; FIRS administrative practice |
| Oilfield services | Standard rated (7.5%) | Section 2 |
| Oil companies as withholding agents | Must withhold VAT on purchases from suppliers | FIRS Circular 2004/02 |

**Flag for reviewer:** VAT treatment of petroleum products is subject to government pricing policy. Confirm current treatment.

### Banking and Financial Services [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Interest on loans | Not subject to VAT (not a supply of goods or services under VAT Act) | FIRS interpretation |
| Bank fees and commissions (explicit) | Standard rated (7.5%) | Section 2 |
| Insurance premiums | Standard rated (7.5%) | Section 2 |
| Foreign exchange transactions | Not subject to VAT (per FIRS practice) | FIRS administrative position |
| ATM charges | Standard rated (7.5%) | Section 2 |
| Banks as withholding agents | Must withhold VAT on purchases | FIRS Circular 2004/02 |

**Flag for reviewer:** FIRS position on financial services VAT treatment has evolved. Confirm current position.

### Telecommunications [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Airtime/data sales | Standard rated (7.5%) | Section 2 |
| Equipment sales | Standard rated (7.5%) | Section 2 |
| Tower rental income | Standard rated (7.5%) | Section 2 |
| Telecom companies as withholding agents | Must withhold VAT on purchases | FIRS designation |

### Real Estate and Construction [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Sale of commercial property | Standard rated (7.5%) | Section 2 |
| Sale of residential property | Standard rated (7.5%) -- no exempt or zero-rate for residential | Section 2 |
| Rental income (commercial) | Standard rated (7.5%) | Section 2 |
| Rental income (residential) | Standard rated (7.5%) | Section 2 |
| Construction services | Standard rated (7.5%) | Section 2 |
| Bare land | Not subject to VAT (not a good or service) | FIRS interpretation |

**Flag for reviewer:** VAT on residential property and rent is a disputed area. Some practitioners argue residential rent should be exempt. Confirm FIRS current position.

### Agriculture [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Unprocessed agricultural produce | Exempt | First Schedule, Part I |
| Processed food (by restaurant/hotel/caterer) | Standard rated (7.5%) | Section 2 (excluded from exemption) |
| Agricultural equipment | Exempt | First Schedule, Part I, Item 5 |
| Fertilizers and pesticides | Exempt | First Schedule, Part I, Item 5 |

---

## Step 12: Record Keeping Requirements [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Retention period | 6 years from date of transaction | VAT Act, Section 18 |
| Language | English | N/A (official language) |
| Format | Paper or electronic | Section 18 |
| Records required | Tax invoices, credit/debit notes, import documents, bank statements, accounting records | Section 18 |

**Legislation:** VAT Act, Section 18.

---

## Step 13: Derived Calculations [T1]

```
A4 = A1 + A2 + A3
A5 = A1 * 7.5%
B5 = B1 + B2 + B3 + B4
B6 = (B1 + B2) * 7.5%
D1 = A5 - B6 - C1

IF D1 > 0 THEN
  VAT payable = D1
ELSE
  Credit carried forward = |D1|
  (May be offset against future returns or refund requested)
END
```

**Legislation:** VAT Act, Section 14.

---

## Step 14: Refund Mechanism [T1]

| Scenario | Treatment | Legislation |
|----------|-----------|-------------|
| Excess input VAT | Carry forward to next period (default) | VAT Act, Section 17 |
| Refund request | Apply to FIRS; refund within 90 days of application | VAT Act, Section 17(2) |
| Exporters with persistent credit | May apply for refund each period | Finance Act 2019, Section 36 |
| Diplomatic missions | Direct refund from FIRS on application | VAT Act, Section 3 |
| Cash basis filing | VAT is accounted for on a cash basis -- refund timing affected | FIRS Circular |

**Note:** In practice, FIRS refunds have historically been slow. Many businesses choose to carry forward credits.

**Legislation:** VAT Act, Sections 16-17; Finance Act 2019.

---

## Step 15: Place of Supply Rules (Cross-Border) [T1]

| Type of Supply | Place of Supply | Legislation |
|----------------|----------------|-------------|
| Goods | Where goods are located at time of supply | VAT Act, Section 2 |
| Services (general rule) | Where services are performed | Finance Act 2020, Section 39 |
| Digital services (B2C) | Where the consumer is located (Nigeria) | Finance Act 2021, Section 6 |
| International transport | Zero-rated if departing Nigeria | VAT Act, First Schedule |

**Legislation:** VAT Act, Section 2; Finance Acts 2020-2021.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the legislation
- NEVER charge VAT on exempt supplies (basic food, medical, education, baby products, agriculture)
- NEVER apply reverse charge to out-of-scope categories (salaries, dividends, pensions)
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER allow input VAT recovery without a valid tax invoice
- NEVER allow input VAT recovery on purchases from unregistered persons
- NEVER ignore withholding VAT obligations if the client is a designated agent
- NEVER file a return without accounting for VAT withheld at source (Section C1)
- NEVER apply the old 5% rate to supplies made on or after 1 February 2020
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER overlook the cash basis requirement for VAT accounting
- NEVER classify bare land as a taxable supply
- NEVER classify processed/restaurant food as zero-rated or exempt (only basic/unprocessed food is zero-rated under NTA 2025; restaurant food is standard-rated)
- NEVER confuse the former exempt treatment (pre-2026) with the new zero-rated treatment (post-1 January 2026) for basic food, medical, and educational items -- zero-rated allows input VAT recovery, exempt did not

---

## Step 16: Edge Case Registry

### EC1 -- Withholding VAT credit note not received [T2]
**Situation:** Government ministry withheld VAT on a supplier's invoice but has not issued the withholding VAT credit note.
**Resolution:** Supplier cannot claim credit in Section C1 without the credit note. Must follow up with the ministry. If credit note is not received, report full output VAT and do not claim credit. Flag for reviewer: may need to engage FIRS dispute resolution.
**Legislation:** FIRS Circular 2004/02.

### EC2 -- Restaurant meal: exempt or taxable? [T1]
**Situation:** Company buys lunch from a restaurant. Supplier did not charge VAT, claiming food is exempt.
**Resolution:** WRONG. Food prepared and served by restaurants, hotels, or caterers is TAXABLE at 7.5%. Only basic/unprocessed food is exempt. Restaurant must charge VAT. If supplier did not charge, flag for review of supplier compliance.
**Legislation:** VAT Act, First Schedule, Part I, Item 1 (exclusion for prepared food).

### EC3 -- Services received from non-resident (self-accounting) [T1]
**Situation:** Nigerian company receives consulting services from a UK firm. Invoice in GBP, no Nigerian VAT.
**Resolution:** Self-accounting applies. Calculate 7.5% VAT on the NGN equivalent. Report in Section B2 (import services) and include output VAT in A5. Claim input in B6 if used for taxable supplies. Net effect zero for fully taxable business.
**Legislation:** Finance Act 2019, Section 34(2).

### EC4 -- Export of goods: documentation [T1]
**Situation:** Client exports goods to Ghana. Wants to zero-rate.
**Resolution:** Zero-rated, but must have: (i) customs export declaration (NCS Form C16), (ii) bill of lading/airway bill, (iii) commercial invoice. Without documentation, must charge 7.5%.
**Legislation:** VAT Act, Section 2(1); FIRS guidelines on export documentation.

### EC5 -- E-commerce platform collecting VAT [T2]
**Situation:** Foreign e-commerce platform (Amazon) sells goods to Nigerian consumers. Who accounts for VAT?
**Resolution:** Under Finance Act 2021, non-resident digital companies supplying goods or services to Nigeria must register and charge VAT. If the platform collects and remits, the Nigerian buyer does not self-account. Flag for reviewer: enforcement and compliance status varies.
**Legislation:** Finance Act 2021, Section 6.

### EC6 -- VAT on imported goods at customs [T1]
**Situation:** Company imports machinery from China. Customs collects 7.5% VAT at the border.
**Resolution:** VAT paid to Customs is recoverable input tax. Report in Section B1 or B2. Retain the customs assessment and payment receipt.
**Legislation:** VAT Act, Section 16; FIRS guidance on import VAT recovery.

### EC7 -- Intra-company transfer between branches [T1]
**Situation:** Company transfers goods from Lagos branch to Abuja branch.
**Resolution:** Not a supply for VAT purposes (same legal entity). No VAT charged. Not reported on VAT return.
**Legislation:** VAT Act, Section 1 (supply must be between different persons).

### EC8 -- Mixed supply: goods + services bundle [T2]
**Situation:** IT company sells a bundled package: hardware (goods) + installation services.
**Resolution:** If the components can be separately identified and priced, apply VAT to each component separately. If they form a single composite supply, the dominant element determines treatment. Both components are likely taxable at 7.5% in this case. Flag for reviewer: confirm whether any component is exempt.
**Legislation:** VAT Act, Section 2 (by implication).

### EC9 -- Government contract: is VAT included in price? [T2]
**Situation:** Government contract states price as "all-inclusive." Does VAT apply?
**Resolution:** VAT applies regardless of contract language. If contract is silent, the contract price is deemed VAT-inclusive and VAT must be extracted. If contract explicitly states "exclusive of VAT," VAT is added on top. Flag for reviewer: contract interpretation required.
**Legislation:** VAT Act, Section 5 (VAT is a charge on the consumer).

### EC10 -- Excess input VAT for extended period [T2]
**Situation:** Exporter has accumulated NGN 50,000,000 in excess input VAT over 12 months.
**Resolution:** Entitled to request refund from FIRS. File refund application via TaxProMax. FIRS has 90 days to process. In practice, may take longer. Flag for reviewer: consider engaging FIRS directly for large refund claims.
**Legislation:** VAT Act, Section 17(2); Finance Act 2019, Section 36.

### EC11 -- Contractor vs. employee: VAT implications [T1]
**Situation:** Client engages a freelance consultant on a recurring basis. Is there VAT?
**Resolution:** If the consultant is genuinely self-employed and providing services (not an employee), VAT at 7.5% applies to their fees (if the consultant is registered). If reclassified as an employee, payments are salary (out of scope). Test: does the person have a TIN and invoice independently?
**Legislation:** VAT Act, Section 1; Employment distinction per Labour Act.

### EC12 -- Waiver of penalty [T3]
**Situation:** Client wants to apply for waiver of late filing penalty.
**Resolution:** FIRS has discretion to waive penalties. Must apply in writing with justification. Outcome is uncertain. Escalate to tax advisor.
**Legislation:** FIRS discretionary powers; no guaranteed waiver.

---

## Step 17: EU VAT Comparison [T1]

| Feature | Nigeria | EU (Directive 2006/112/EC) |
|---------|---------|---------------------------|
| Standard rate | 7.5% | 15-27% (varies) |
| Registration threshold | Effectively none (all taxable persons) | Varies (EUR 0 to EUR 85,000) |
| Reverse charge (import of services) | Yes (self-accounting) | Yes (Article 196) |
| Withholding VAT | Yes (designated agents) | No (except some member states for specific sectors) |
| Filing frequency | Monthly | Varies (monthly/quarterly/annual) |
| Cash vs. accrual basis | Cash basis | Varies (generally invoice/accrual) |
| Group registration | No | Yes (Article 11) |
| Capital goods adjustment | No formal scheme | Yes (5/10/20 years) |
| Bad debt relief | Not formally provided | Yes (varies by member state) |
| Electronic filing | Mandatory (TaxProMax) | Varies |
| Exempt basic food | Yes (extensive list) | Varies (some states use reduced rates) |
| Withholding VAT at source | Yes (unique feature) | Rare |
| Place of supply for digital services | Customer location (B2C) | Customer location (B2C, per MOSS/OSS) |

---

## Step 18: Test Suite

### Test 1 -- Standard local sale, 7.5% VAT
**Input:** Nigerian company sells IT equipment to a local client. Net NGN 1,000,000. VAT NGN 75,000. Gross NGN 1,075,000.
**Expected output:** A1 = NGN 1,000,000. A5 = NGN 75,000.

### Test 2 -- Sale to withholding VAT agent (government)
**Input:** Company sells office furniture to a federal ministry. Net NGN 2,000,000. VAT NGN 150,000.
**Expected output:** A1 = NGN 2,000,000. A5 = NGN 150,000. C1 = NGN 150,000 (VAT withheld by ministry). D1 impact: VAT effectively settled by withholding.

### Test 3 -- Export of goods (zero-rated)
**Input:** Company exports cocoa beans to Netherlands. Invoice NGN 10,000,000. Export documentation complete.
**Expected output:** A2 = NGN 10,000,000. A5 = NGN 0. Input VAT on related purchases recoverable.

### Test 4 -- Purchase of basic food (exempt)
**Input:** Company buys raw rice for staff canteen from a wholesaler. NGN 500,000. No VAT charged.
**Expected output:** B4 = NGN 500,000. B6 does NOT include any VAT. Correctly exempt.

### Test 5 -- Restaurant meal (taxable, not exempt)
**Input:** Company buys catered lunch from a restaurant. NGN 100,000 + NGN 7,500 VAT.
**Expected output:** B1 = NGN 100,000. B6 includes NGN 7,500. Input VAT recoverable if business-related.

### Test 6 -- Self-accounting on imported services
**Input:** Nigerian company receives cloud hosting from US provider. USD 5,000 (~NGN 4,000,000). No Nigerian VAT on invoice.
**Expected output:** B2 = NGN 4,000,000. Self-account output VAT = NGN 300,000 in A5. Input VAT = NGN 300,000 in B6. Net = zero.

### Test 7 -- Medical supplies purchase (exempt)
**Input:** Pharmacy buys pharmaceuticals from local manufacturer. NGN 3,000,000. No VAT charged.
**Expected output:** B4 = NGN 3,000,000. Exempt. No input VAT.

### Test 8 -- Late filing penalty
**Input:** Monthly return for March 2026 due 21 April 2026. Filed 15 May 2026. Tax payable NGN 500,000.
**Expected output:** Late filing penalty: NGN 50,000 (first month late). Late payment penalty: 5% + CBN rate interest on NGN 500,000 for 24 days.

### Test 9 -- Withholding VAT by client (as agent)
**Input:** Client is a designated withholding agent (bank). Pays supplier NGN 5,000,000 + NGN 375,000 VAT for services.
**Expected output:** Client withholds NGN 375,000. Reports in C2 = NGN 375,000. Remits to FIRS by 21st of following month.

### Test 10 -- Mixed supplies (partial exemption)
**Input:** Company makes 60% taxable, 40% exempt supplies. Office rent NGN 2,000,000 + NGN 150,000 VAT.
**Expected output:** B1 = NGN 2,000,000. B6 includes NGN 90,000 (60% of NGN 150,000). Recovery restricted by ratio.

### Test 11 -- Agricultural equipment (exempt purchase)
**Input:** Farming company buys tractor from local dealer. NGN 15,000,000. No VAT charged.
**Expected output:** B4 = NGN 15,000,000. Exempt under First Schedule. No VAT.

### Test 12 -- Digital service to Nigerian consumer (non-resident provider)
**Input:** Netflix charges Nigerian subscriber NGN 5,000/month. Netflix is registered with FIRS.
**Expected output:** Netflix charges and remits 7.5% VAT (NGN 375). Consumer pays NGN 5,375 total. No action for the consumer.

---

## Step 19: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Chartered accountant or tax advisor must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to chartered accountant or tax advisor. Document gap.
```

---

## Contribution Notes

If you are adapting this skill for another jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all return line items with your jurisdiction's VAT return structure.
3. Replace VAT rates with your jurisdiction's rates.
4. Replace the exempt/zero-rated lists with your jurisdiction's lists.
5. Replace the withholding VAT mechanism if your jurisdiction has one (most do not).
6. Have a chartered accountant in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases for known ambiguous situations.
8. Run all test suite cases against your jurisdiction's rules.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
