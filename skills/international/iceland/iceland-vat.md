---
name: iceland-vat
description: Use this skill whenever asked to prepare, review, or advise on an Iceland VAT (VSK) return or any VSK-related classification. Trigger on phrases like "prepare VSK return", "Iceland VAT", "virðisaukaskattur", "Icelandic VAT filing", "Rikisskattstjori", or any request involving Icelandic VAT obligations. This skill contains the complete Icelandic VSK classification rules, rate tables, filing deadlines, and deductibility rules required to produce a correct return. ALWAYS read this skill before touching any Iceland VAT-related work.
---

# Iceland VAT (VSK) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Iceland (Island) |
| Jurisdiction Code | IS |
| Primary Legislation | Log um virdisaukaskatt (Value Added Tax Act), Act No. 50/1988 |
| Supporting Legislation | Regulation No. 630/2008 (on VSK returns); Regulation No. 505/2013 (on registration); EEA Agreement (relevant for cross-border rules) |
| Tax Authority | Rikisskattstjori (Directorate of Internal Revenue / Iceland Revenue and Customs) |
| Filing Portal | https://www.skattur.is (Skatturinn portal) |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return field assignment, reverse charge, deductibility rules. Tier 2: partial exemption, sector-specific rules, EEA service rules. Tier 3: complex group structures, special investment zones, fishing vessel schemes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and kennitala (national ID number)** [T1] -- 10-digit number used as tax ID for both individuals and legal entities
2. **VSK number (VSK-numerid)** [T1] -- Assigned upon registration; format IS + 5 or 6 digits
3. **Registration type** [T1] -- Standard VSK-registered, below-threshold (exempt), or voluntary registration
4. **Filing period** [T1] -- Bi-monthly (standard) or monthly (for large taxpayers, optional)
5. **Industry/sector** [T2] -- Impacts specific exemption rules and reduced rate eligibility
6. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required
7. **EEA trading status** [T1] -- Iceland is an EEA member (not EU) via EFTA; EEA rules apply for services
8. **Credit carried forward from prior period** [T1] -- Innskattur til yfirfaerslu
9. **Does the client operate in tourism/hospitality?** [T2] -- 11% reduced rate applies; specific rules for accommodation
10. **Does the client export goods or services?** [T1] -- Zero-rated; refund eligibility

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output VSK -- utskattur) or Purchase (input VSK -- innskattur)
- Salaries (laun), social contributions (tryggingagjald), tax payments, loan repayments, dividends = OUT OF SCOPE (never on VSK return)
- **Legislation:** Act 50/1988, Article 2 (taxable transactions), Article 3 (supply of goods and services)

### 1b. Determine Counterparty Location [T1]

- **Domestic (Iceland):** Supplier/customer is in Iceland
- **EEA (European Economic Area):** EU 27 member states + Norway + Liechtenstein. Iceland is an EEA member via EFTA
- **Non-EEA:** All other countries (US, UK post-Brexit, Switzerland [EFTA but not EEA for VAT], etc.)
- **Note:** Iceland is NOT an EU member state. However, EEA rules apply for cross-border services
- **Note:** Faroe Islands are NOT part of Iceland for VSK purposes (separate Danish territory)
- **Legislation:** Act 50/1988, Article 12 (place of supply); EEA Agreement

### 1c. Determine VSK Rate [T1]

| Rate | Category | Legal Basis |
|------|----------|-------------|
| 24% | Standard rate (almennur skattur) | Act 50/1988, Article 14(1) |
| 11% | Reduced rate (laegri skattur) | Act 50/1988, Article 14(2) |
| 0% | Zero-rated (exports, international transport) | Act 50/1988, Article 12, 42 |

### 1d. Standard Rate (24%) Applies To [T1]

- All goods and services not specifically listed for the reduced rate or zero rate
- Professional services (legal, accounting, consulting, IT)
- Telecommunications and electronic services
- Construction services and materials
- Motor vehicles, electronics, furniture
- Clothing and footwear
- Alcohol (in addition to excise duties)
- **Legislation:** Act 50/1988, Article 14(1)

### 1e. Reduced Rate (11%) Applies To [T1]

| Category | Examples | Legal Basis |
|----------|----------|-------------|
| Food and consumables | All food for human consumption (raw and processed) | Art 14(2), Item 1 |
| Hotel and guest accommodation | Overnight accommodation (not food/beverages served) | Art 14(2), Item 2 |
| Newspapers and periodicals | Published at regular intervals | Art 14(2), Item 4 |
| Books | Printed and electronic books | Art 14(2), Item 5 |
| Geothermal hot water | District heating from geothermal sources | Art 14(2), Item 3 |
| Heating fuel oil | For domestic heating | Art 14(2), Item 3a |
| Electricity | For domestic and commercial use | Art 14(2), Item 3b |
| Music recordings | Audio recordings (CDs, digital downloads) | Art 14(2), Item 6 |
| Passenger transport | Domestic flights, buses, taxis, whale watching, horseback riding | Art 14(2), Item 7 |
| Travel agency and tour operator services | Package tours and travel services | Art 14(2), Item 8 |
| Admission to swimming pools and spas | Public baths, hot springs | Art 14(2), Item 9 |
| Radio and television subscriptions | Broadcast subscription services | Art 14(2), Item 10 |

### 1f. Zero-Rated Supplies (Undanthegid med innskattsfradraetti) [T1]

- Export of goods (Article 12(1)) -- goods must leave Iceland, confirmed by customs documentation
- International transport of passengers and goods (Article 12(3))
- Services directly connected with exported goods (Article 12(4))
- Supplies to foreign ships and aircraft (Article 12(5))
- Supplies to diplomatic missions and international organizations (Article 12(10))
- **Note:** Zero-rated suppliers can claim full input VSK refund
- **Legislation:** Act 50/1988, Article 12

### 1g. Exempt Supplies (Undanthaga -- No Input Recovery) [T1]

| Category | Legal Basis |
|----------|-------------|
| Financial services (banking, lending, securities) | Art 2(3)(10) |
| Insurance and reinsurance | Art 2(3)(9) |
| Healthcare services (by licensed providers) | Art 2(3)(1) |
| Education (schools, universities) | Art 2(3)(2) |
| Social welfare services | Art 2(3)(3) |
| Postal services (universal service) | Art 2(3)(4) |
| Rental of residential property | Art 2(3)(5) |
| Cultural activities (museums, libraries -- certain) | Art 2(3)(7) |
| Sporting activities (by non-profit organizations) | Art 2(3)(8) |
| Sale of real property (excluding new buildings) | Art 2(3)(14) |
| Lottery and gambling | Art 2(3)(11) |
| Author and artist royalties | Art 2(3)(6) |
| Funeral services | Art 2(3)(12) |

**Note:** Exempt suppliers CANNOT recover input VSK on related purchases

**Legislation:** Act 50/1988, Article 2(3)

---

## Step 2: VSK Return Structure

The VSK return (Virdisaukaskattsframtal) is filed electronically via skattur.is. The standard bi-monthly return structure:

### Section A: Output VSK (Utskattur) [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| A1 | Sales at 24% -- taxable base | Net value of standard-rated supplies |
| A2 | Output VSK at 24% | = A1 x 24% |
| A3 | Sales at 11% -- taxable base | Net value of reduced-rated supplies |
| A4 | Output VSK at 11% | = A3 x 11% |
| A5 | Self-assessed VSK (reverse charge) at 24% | Import of services / deemed supplies |
| A6 | Self-assessed VSK (reverse charge) at 11% | Import of services at reduced rate |
| A7 | Total output VSK | = A2 + A4 + A5 + A6 |

### Section B: Exempt and Zero-Rated [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| B1 | Zero-rated sales (exports) | Article 12 supplies |
| B2 | Exempt sales (no credit) | Article 2(3) supplies |
| B3 | Total non-taxed supplies | = B1 + B2 |

### Section C: Input VSK (Innskattur) [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| C1 | Input VSK on domestic purchases | From invoices with VSK |
| C2 | Import VSK (from customs declarations) | Goods imported from abroad |
| C3 | Self-assessed input VSK (reverse charge) | = A5 + A6 (offsetting entry) |
| C4 | Prior period carry-forward credit | Innskattur til yfirfaerslu |
| C5 | Input VSK corrections (increase) | Adjustments |
| C6 | Input VSK corrections (decrease) | Adjustments |
| C7 | Total input VSK | = C1 + C2 + C3 + C4 + C5 - C6 |

### Section D: VSK Payable or Refundable [T1]

```
IF A7 > C7 THEN
    D1 (VSK payable / virdisaukaskattur til greidtslu) = A7 - C7
    D2 = 0
ELSE
    D1 = 0
    D2 (VSK refundable / virdisaukaskattur til endurgreidslu) = C7 - A7
END
```

**Legislation:** Act 50/1988, Article 24; Regulation No. 630/2008

---

## Step 3: Reverse Charge Mechanics [T1]

### 3a. When Reverse Charge Applies [T1]

The Icelandic recipient must self-assess VSK when:

1. **Services received from a foreign supplier** with no fixed establishment in Iceland (Article 35a)
2. **Electronic services received from abroad** (B2B)
3. **Intangible services** (consulting, legal, advertising, software) from foreign suppliers

### 3b. Reverse Charge -- Foreign Services [T1]

| Step | Action | Field |
|------|--------|-------|
| 1 | Determine net value of service | Base amount |
| 2 | Apply appropriate rate (24% or 11%) | Determine rate |
| 3 | Report VSK in Field A5 (24%) or A6 (11%) | Output side |
| 4 | Deduct same VSK in Field C3 | Input side |
| 5 | Net effect = zero for fully taxable businesses | Check |

**Legislation:** Act 50/1988, Article 35a

### 3c. Import of Goods [T1]

- VSK on imported physical goods is assessed and collected by Customs (Tollstjori)
- Importer pays VSK at the border via customs declaration (tollaframtal)
- This import VSK is deductible as input VSK (Field C2)
- **Do NOT self-assess imports of goods on the VSK return** -- Customs handles assessment
- **Legislation:** Act 50/1988, Article 36 (VSK on imports)

### 3d. EEA Service Rules [T1]

- Iceland, as an EEA member, follows the EU B2B place of supply rule for services:
  - B2B services: place of supply is where the recipient is established
  - B2C services: place of supply is where the supplier is established (with exceptions for electronic services)
- When an Icelandic business receives B2B services from an EEA or non-EEA supplier, reverse charge applies
- When an Icelandic business supplies B2B services to an EEA customer, the supply is outside the scope of Icelandic VSK
- **Legislation:** Act 50/1988, Article 12; EEA Agreement implementation

---

## Step 4: Registration Rules

### 4a. Mandatory Registration [T1]

| Criterion | Threshold | Legal Basis |
|-----------|-----------|-------------|
| Taxable turnover (last 12 months) | ISK 2,000,000 | Art 5(1) |
| Foreign entities with taxable supply in Iceland | No threshold (any amount) | Art 5(2) |

- Once the ISK 2,000,000 threshold is exceeded, the business must register immediately
- **Legislation:** Act 50/1988, Article 5

### 4b. Voluntary Registration [T1]

- Businesses below the ISK 2,000,000 threshold may voluntarily register
- Useful for businesses making zero-rated supplies (exports) to claim input VSK refunds
- **Legislation:** Act 50/1988, Article 5(3)

### 4c. Non-Resident Registration [T2]

- Foreign entities performing taxable supplies in Iceland must register
- May appoint a fiscal representative (skattalegur fulltrui) in Iceland
- For electronic services to Icelandic consumers (B2C), the foreign supplier must register
- **Flag for reviewer:** Determine if non-resident registration or reverse charge by recipient applies
- **Legislation:** Act 50/1988, Article 5(2), Article 35a

### 4d. Deregistration [T1]

- Business may apply for deregistration if turnover falls below ISK 2,000,000
- Must settle any outstanding VSK obligations
- Must reverse input VSK on assets still held at deregistration
- **Legislation:** Act 50/1988, Article 5(4)

---

## Step 5: Deductibility Rules

### 5a. General Deduction Right [T1]

- All input VSK on goods and services used for taxable business activities is deductible
- Input VSK must be documented by a proper invoice (reikningur) meeting statutory requirements
- Invoice must show: supplier name, kennitala/VSK number, date, description, net amount, VSK amount, rate
- **Legislation:** Act 50/1988, Article 16

### 5b. Non-Deductible Input VSK [T1]

The following input VSK is BLOCKED and cannot be recovered:

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Passenger vehicles (foldbilar) | Art 16(3)(1) | Exception: taxi, rental car, driving school |
| Fuel for non-deductible vehicles | Art 16(3)(1) | Follows vehicle deductibility |
| Entertainment and hospitality (skemmtanakostnadur) | Art 16(3)(2) | Business entertainment, gifts |
| Food and beverages for employees | Art 16(3)(3) | Staff canteen (unless hospitality business) |
| Residential accommodation for employees | Art 16(3)(4) | Housing provided to staff |
| Goods/services for exempt activities | Art 16(6) | No input VSK on exempt supplies |

### 5c. Partial Deduction Rules [T2]

- **Mixed-use assets:** If a vehicle or asset is used for both business and personal purposes, only the business portion of input VSK is deductible
- **Mixed taxable/exempt:** If a business makes both taxable and exempt supplies, input VSK on overhead must be apportioned using a pro-rata formula:
  `Deductible % = (Taxable + Zero-Rated Supplies) / Total Supplies x 100`
- **Flag for reviewer:** Pro-rata must be confirmed by tax adviser. Annual adjustment required.
- **Legislation:** Act 50/1988, Article 16(4)-(6)

### 5d. Capital Goods Scheme [T2]

- Input VSK on real property is subject to a 20-year adjustment period
- Input VSK on machinery and equipment is subject to a 5-year adjustment period (if value exceeds ISK 500,000)
- If use of the capital good changes (from taxable to exempt or vice versa), annual adjustments are required
- **Flag for reviewer:** Capital goods adjustments are complex; confirm with tax adviser
- **Legislation:** Act 50/1988, Article 16a

---

## Step 6: Key Thresholds

| Threshold | Value | Notes |
|-----------|-------|-------|
| Standard VSK rate | 24% | Art 14(1) |
| Reduced VSK rate | 11% | Art 14(2) |
| Mandatory registration | ISK 2,000,000 (last 12 months) | Art 5(1) |
| Capital goods -- real property adjustment | 20 years | Art 16a |
| Capital goods -- equipment adjustment | 5 years (if > ISK 500,000) | Art 16a |
| Filing period | Bi-monthly (standard) | Art 24 |
| Refund threshold | No minimum (refund if in credit) | Art 25 |

---

## Step 7: Filing Deadlines

### Bi-Monthly Filing Periods [T1]

| Period | Months Covered | Filing & Payment Deadline |
|--------|---------------|--------------------------|
| Period 1 | January -- February | 5 April |
| Period 2 | March -- April | 5 June |
| Period 3 | May -- June | 5 August |
| Period 4 | July -- August | 5 October |
| Period 5 | September -- October | 5 December |
| Period 6 | November -- December | 5 February (following year) |

**Note:** If the 5th falls on a weekend or public holiday, the deadline moves to the next business day.

**Filing method:** Electronic via skattur.is (Rikisskattstjori portal).

**Legislation:** Act 50/1988, Article 24; Regulation No. 630/2008

### Late Filing and Payment Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | Surcharge (alag): 1% of the VSK payable, minimum ISK 25,000 |
| Continued late filing | Additional 2% per month, up to 10% maximum |
| Late payment | Default interest (dravaxta): official interest rate published by Central Bank |
| Failure to register | Estimated assessment by Rikisskattstjori + penalties |
| Failure to issue proper invoice | Fine per incident |
| Repeated non-compliance | May result in deregistration and estimated assessments |

**Legislation:** Act 50/1988, Articles 27-28

---

## Step 8: Refund Mechanism

### 8a. Automatic Refund [T1]

- If total input VSK exceeds total output VSK, the excess is refundable
- Refunds are generally processed within 10 business days of filing
- Rikisskattstjori may withhold refund pending audit (particularly for new registrations or unusual claims)
- **Legislation:** Act 50/1988, Article 25

### 8b. Refund to Foreign Businesses [T2]

- Foreign businesses not registered in Iceland may claim refund of Icelandic VSK on business expenses incurred in Iceland
- Applies to EEA-established businesses under reciprocity rules
- Application filed with Rikisskattstjori; specific forms and documentation required
- **Flag for reviewer:** Eligibility depends on reciprocity with the claimant's country
- **Legislation:** Act 50/1988, Article 43; Regulation on foreign business VSK refund

### 8c. Tourist Refund (Tax Free Shopping) [T1]

- Non-residents (outside Iceland) can claim a VSK refund on goods purchased in Iceland and taken abroad
- Minimum purchase: ISK 6,000 per transaction
- Refund processed at departure via authorized refund agents
- **This does not appear on the seller's VSK return** -- the seller charges normal VSK
- **Legislation:** Act 50/1988, Article 42a

---

## Step 9: Specific Sector Rules

### 9a. Tourism and Hospitality [T2]

- Hotel accommodation: 11% reduced rate
- Restaurant services (food served on premises): 11% for the food component; 24% for alcohol
- Tour operator services: 11%
- Car rental: 24% (standard rate -- not reduced)
- **Flag for reviewer:** Split invoices between 11% and 24% components where applicable
- **Legislation:** Act 50/1988, Article 14(2)

### 9b. Fishing Industry [T3]

- Complex rules apply for fishing vessels, catch quotas, and fish processing
- Certain supplies to fishing vessels may be zero-rated
- Escalate to qualified tax adviser for all fishing industry transactions
- **Legislation:** Act 50/1988, Article 12(5); specific fishing industry regulations

### 9c. Construction and Real Property [T2]

- New buildings (first sale): subject to VSK at 24%
- Sale of used buildings: exempt (no VSK)
- Construction services: 24%
- Self-supply of construction services (developer builds own building): deemed taxable supply [T2]
- **Flag for reviewer:** Real property transactions require careful analysis of first-sale vs. used status
- **Legislation:** Act 50/1988, Article 2(3)(14), Article 3

### 9d. Digital Services to Foreign Consumers [T1]

- Icelandic businesses providing electronic services to consumers in EEA countries must consider place of supply rules
- B2B: place of supply is where customer is established (no Icelandic VSK)
- B2C to EEA: may need to register in the customer's country or use the One Stop Shop (OSS) equivalent [T2]
- **Legislation:** Act 50/1988, Article 12; EEA implementation

---

## Step 10: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., Dropbox, Slack) [T1]

**Situation:** Icelandic company pays for cloud services from a US company, no VSK on invoice.
**Resolution:** Reverse charge. Self-assess at 24% in Field A5. Deduct in Field C3. Net effect = zero.
**Legislation:** Act 50/1988, Article 35a

### EC2 -- Export of goods to EU country [T1]

**Situation:** Icelandic manufacturer exports fish products to France. Customs documentation obtained.
**Resolution:** Zero-rated under Article 12(1). Report in Field B1. No output VSK. Full input VSK recovery.
**Legislation:** Act 50/1988, Article 12(1)

### EC3 -- Hotel accommodation sale [T1]

**Situation:** Hotel charges guest ISK 30,000 for a room (net ISK 27,027 + VSK ISK 2,973 at 11%).
**Resolution:** Field A3 = ISK 27,027. Field A4 = ISK 2,973. Output VSK at 11%.
**Legislation:** Act 50/1988, Article 14(2)

### EC4 -- Purchase of passenger car [T1]

**Situation:** Company purchases a sedan for employee use, net ISK 5,000,000, VSK ISK 1,200,000.
**Resolution:** Input VSK is BLOCKED under Article 16(3)(1). Vehicle capitalized at ISK 6,200,000. No input VSK recovery.
**Legislation:** Act 50/1988, Article 16(3)(1)

### EC5 -- Import of machinery from Germany [T1]

**Situation:** Icelandic manufacturer imports industrial equipment from Germany. Customs declaration shows ISK 10,000,000 value, VSK ISK 2,400,000.
**Resolution:** Import VSK paid to Customs. Deductible as input VSK in Field C2 = ISK 2,400,000.
**Legislation:** Act 50/1988, Article 36

### EC6 -- Consulting services sold to Norwegian client (B2B) [T1]

**Situation:** Icelandic consultancy provides services to a Norwegian business.
**Resolution:** Place of supply is Norway (where recipient is established). Outside scope of Icelandic VSK. No output VSK. May be reported in Field B1 or B3 for information. Input VSK on related costs is deductible.
**Legislation:** Act 50/1988, Article 12 (EEA B2B rule)

### EC7 -- Restaurant serving food and alcohol [T2]

**Situation:** Restaurant invoice for ISK 15,000 includes food and wine.
**Resolution:** Food component at 11% reduced rate. Alcohol component at 24% standard rate. Invoice must be split. Flag for reviewer: confirm split between food and beverage.
**Legislation:** Act 50/1988, Article 14(1) and 14(2)

### EC8 -- Employee housing provided by employer [T1]

**Situation:** Company pays rent for employee apartment.
**Resolution:** Input VSK on residential accommodation for employees is NOT deductible under Article 16(3)(4). VSK on the rent (if charged) cannot be recovered.
**Legislation:** Act 50/1988, Article 16(3)(4)

### EC9 -- Credit notes [T1]

**Situation:** Supplier issues a credit note correcting a previous invoice.
**Resolution:** Reduce the original field amounts. If original output was in A1/A2, reduce by credit note amount. If original input, reduce relevant input field. Credit note must reference original invoice.
**Legislation:** Act 50/1988, Article 22

### EC10 -- Geothermal heating supply [T1]

**Situation:** Utility company supplies geothermal hot water to households and businesses.
**Resolution:** Reduced rate of 11%. Field A3 (base) and A4 (VSK at 11%).
**Legislation:** Act 50/1988, Article 14(2), Item 3

### EC11 -- Services from EEA supplier (e.g., Danish law firm) [T1]

**Situation:** Icelandic company receives legal advice from a Danish law firm. No VSK on invoice.
**Resolution:** Reverse charge. Self-assess at 24% in Field A5. Deduct in Field C3. Net = zero. Same treatment as non-EEA services.
**Legislation:** Act 50/1988, Article 35a

### EC12 -- Whale watching tour operator [T1]

**Situation:** Tour operator sells whale watching tours to tourists.
**Resolution:** 11% reduced rate applies (passenger transport / tour services). Field A3/A4.
**Legislation:** Act 50/1988, Article 14(2), Item 7-8

---

## Step 11: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified tax adviser must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified tax adviser. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard domestic sale at 24%

**Input:** Icelandic company sells IT services to a domestic client, net ISK 1,000,000, VSK ISK 240,000.
**Expected output:** Field A1 = ISK 1,000,000. Field A2 = ISK 240,000. Output VSK reported.

### Test 2 -- Reduced rate sale at 11%

**Input:** Bookshop sells books, net ISK 50,000, VSK ISK 5,500.
**Expected output:** Field A3 = ISK 50,000. Field A4 = ISK 5,500.

### Test 3 -- Export of goods, zero-rated

**Input:** Fish processor exports to the UK, net ISK 20,000,000. Customs documentation obtained.
**Expected output:** Field B1 = ISK 20,000,000. No output VSK. Input VSK on related purchases refundable.

### Test 4 -- Import of services, reverse charge

**Input:** Icelandic company receives consulting from a US firm, USD 5,000 (approx. ISK 700,000). No VSK.
**Expected output:** Field A5 = ISK 168,000 (24% of ISK 700,000). Field C3 = ISK 168,000. Net = zero.

### Test 5 -- Passenger car purchase, blocked input

**Input:** Company purchases sedan, net ISK 8,000,000, VSK ISK 1,920,000.
**Expected output:** Input VSK of ISK 1,920,000 is BLOCKED. Asset capitalized at ISK 9,920,000.

### Test 6 -- Hotel accommodation

**Input:** Hotel invoices guest for 3 nights, net ISK 90,000, VSK ISK 9,900 (11%).
**Expected output:** Field A3 = ISK 90,000. Field A4 = ISK 9,900.

### Test 7 -- Import of goods from EU

**Input:** Icelandic retailer imports clothing from Italy. Customs value ISK 5,000,000, import VSK ISK 1,200,000.
**Expected output:** Field C2 = ISK 1,200,000 (input VSK from customs).

### Test 8 -- B2B service to Norway, outside scope

**Input:** Icelandic design firm provides services to Norwegian company, ISK 3,000,000.
**Expected output:** No output VSK. Field B1 or B3 = ISK 3,000,000 (informational). Input VSK on related costs deductible.

---

## PROHIBITIONS [T1]

- NEVER allow input VSK deduction on passenger vehicles (unless taxi/rental business)
- NEVER allow input VSK deduction on entertainment or employee housing
- NEVER skip reverse charge on foreign services -- self-assessment is mandatory
- NEVER treat Iceland as an EU member state -- Iceland is EEA via EFTA
- NEVER confuse zero-rated (Article 12, with input recovery) with exempt (Article 2(3), without input recovery)
- NEVER register import of goods via reverse charge -- Customs handles VSK on imports
- NEVER allow input VSK recovery on purchases used for exempt activities
- NEVER charge 24% on reduced-rate items (food, hotel, books) or vice versa
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER guess fishing industry rules -- always escalate [T3]

---

## Step 13: Invoice Requirements and Documentation

### 13a. Invoice (Reikningur) Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Who must issue | All VSK-registered businesses for every taxable supply |
| Mandatory fields | Supplier name, kennitala, VSK number; buyer name and kennitala (for B2B); date; sequential number; description of goods/services; quantity; unit price; net amount; VSK rate; VSK amount; total |
| Issuance deadline | At the time of supply or within a reasonable period |
| Format | Paper or electronic (both accepted; e-invoicing not yet mandatory) |
| Storage | 7 years from end of financial year |
| Language | Icelandic (English commonly accepted for international transactions) |

**Legislation:** Act 50/1988, Article 22; Regulation on invoicing

### 13b. Credit Notes [T1]

| Requirement | Details |
|-------------|---------|
| Purpose | Reduce or cancel a previously issued invoice |
| Requirements | Must reference original invoice; show the correction amounts |
| VSK effect | Adjusts output VSK in the period of issuance |
| Buyer | Must correspondingly reduce input VSK |

### 13c. Simplified Invoice [T1]

| Requirement | Details |
|-------------|---------|
| When allowed | Retail sales (B2C) below ISK 50,000 |
| Content | May omit buyer details; must show VSK amount |
| Cash register | Electronic cash register required for retail |

---

## Step 14: Advance Payments and Tax Point Rules

### 14a. Tax Point (Skattskyldutimamark) [T1]

| Event | Tax Point | Legal Basis |
|-------|-----------|-------------|
| Supply of goods | Date of delivery | Art 13(1) |
| Supply of services | Date service is completed | Art 13(2) |
| Advance payment received | Date of receipt | Art 13(3) |
| Continuous supply | End of each billing period | Art 13(4) |
| Import of goods | Date of customs clearance | Art 36 |

### 14b. Advance Payments [T1]

- When an advance payment is received before delivery, VSK is triggered on the date of receipt
- Supplier must issue an invoice for the advance showing VSK
- Final invoice upon delivery covers the remaining balance
- **Legislation:** Act 50/1988, Article 13

---

## Step 15: International Agreements and EEA Considerations

### 15a. EEA Agreement Impact [T1]

| Area | Impact | Notes |
|------|--------|-------|
| Services (B2B) | EEA place of supply rules apply | Same as EU for B2B services |
| Services (B2C) | General rule: supplier's location | Exceptions for digital services |
| Goods | NOT covered by EU single market for VAT | Customs duties may apply per EFTA rules |
| Refund to EEA businesses | Available under reciprocity | Application to Rikisskattstjori |
| OSS (One Stop Shop) | Not available (EU-only mechanism) | Must register individually in EU states if B2C digital |

### 15b. EFTA Convention [T1]

- Iceland is an EFTA member (with Norway, Switzerland, Liechtenstein)
- EFTA does NOT create a VAT area -- each country has independent VAT rules
- Free trade agreements may reduce customs duties but do NOT affect VSK
- **Legislation:** EFTA Convention; EEA Agreement

---

## Step 16: Penalties and Interest Reference Table

| Violation | Amount / Rate | Legal Basis |
|-----------|--------------|-------------|
| Late filing | Surcharge (alag): 1% of VSK payable, min ISK 25,000 | Art 27 |
| Continued late filing | Additional 2% per month, max 10% | Art 27 |
| Late payment | Default interest (dravaxta): Central Bank rate + margin | Art 28 |
| Failure to register | Estimated assessment + penalties | Art 26 |
| Failure to issue proper invoice | Fine per incident | Art 27a |
| Failure to keep records | Fine + potential deregistration | Art 27a |
| Repeated non-compliance | Deregistration and estimated assessments | Art 26 |
| Tax fraud | Criminal prosecution under General Penal Code | Penal Code |
| Incorrect return (negligence) | 25% surcharge on underpaid VSK | Art 27 |
| Incorrect return (gross negligence) | 50% surcharge on underpaid VSK | Art 27 |

---

## Step 17: Withholding and Special Mechanisms

### 17a. No General Withholding System [T1]

- Unlike Turkey (tevkifat), Iceland does NOT have a general VAT withholding mechanism
- The supplier always charges full VSK and remits to Rikisskattstjori
- The buyer claims input VSK through the return

### 17b. Reverse Charge Only Exception [T1]

- The only exception is the reverse charge on imported services (Article 35a)
- There is no domestic reverse charge for construction or other sectors (unlike EU countries that have adopted domestic reverse charge under Art 199 of the VAT Directive)

---

## Step 18: Record-Keeping Requirements [T1]

| Record Type | Retention Period | Legal Basis |
|-------------|-----------------|-------------|
| Invoices (reikningar) | 7 years from end of financial year | Act 50/1988, Art 20 |
| Accounting ledgers | 7 years | Accounting Act |
| Bank statements | 7 years | Accounting Act |
| Contracts and agreements | 7 years | Accounting Act |
| Customs declarations (tollaframtal) | 7 years | Customs Act |
| VSK returns (filed electronically) | Maintained by Rikisskattstjori | Electronic filing |
| Cash register records | 7 years | Act 50/1988 |
| Purchase and sales registers | 7 years | Regulation 630/2008 |

### 18a. Audit and Inspection [T1]

- Rikisskattstjori may request access to all books and records at any time
- Businesses must cooperate fully with tax audits
- Failure to produce records may result in estimated assessments
- Electronic records must be provided in a machine-readable format upon request
- **Legislation:** Act 50/1988, Articles 26-28; Tax Administration Act

---

## Contribution Notes

This skill covers Icelandic VSK as of April 2026. Icelandic tax law is subject to amendment by the Althingi (parliament). All rates and thresholds should be verified against the most recent legislation and Rikisskattstjori guidance before filing. A qualified Icelandic tax adviser (loggiltur endurskodandi or skattaradgjafi) must validate all T1 rules before this skill is used in production.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
