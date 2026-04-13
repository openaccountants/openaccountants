---
name: serbia-vat
description: Use this skill whenever asked to prepare, review, or advise on a Serbia VAT (PDV) return or any PDV-related classification. Trigger on phrases like "prepare PDV return", "Serbia VAT", "PPPDV", "Serbian VAT filing", "e-Faktura", "Poreska Uprava", or any request involving Serbian VAT obligations. This skill contains the complete Serbian PDV classification rules, rate tables, e-invoicing requirements, filing deadlines, and deductibility rules required to produce a correct return. ALWAYS read this skill before touching any Serbia VAT-related work.
---

# Serbia VAT (PDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Serbia (Republika Srbija) |
| Jurisdiction Code | RS |
| Primary Legislation | Zakon o porezu na dodatu vrednost (Law on Value Added Tax), Official Gazette RS No. 84/2004, as amended |
| Supporting Legislation | Pravilnik o PDV (PDV Rulebook); Zakon o fiskalizaciji (Fiscalization Law); Zakon o elektronskom fakturisanju (E-Invoicing Law) |
| Tax Authority | Poreska uprava (Tax Administration), Ministry of Finance |
| Filing Portal | https://eporezi.purs.gov.rs (ePorezi portal) |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return box assignment, reverse charge, e-invoicing rules. Tier 2: partial exemption, sector-specific rules, place of supply. Tier 3: group structures, special tax zones, complex international arrangements. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and PIB (Poreski identifikacioni broj)** [T1] -- 9-digit tax identification number
2. **PDV registration number** [T1] -- Separate from PIB; format RS + 9 digits
3. **Registration type** [T1] -- Mandatory PDV taxpayer, voluntary PDV taxpayer, or non-registered (below threshold)
4. **Filing period** [T1] -- Monthly (if turnover > RSD 50,000,000) or quarterly (if turnover <= RSD 50,000,000)
5. **Industry/sector** [T2] -- Impacts specific exemption rules
6. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (Article 30 of Zakon o PDV)
7. **Is the client registered for e-Faktura?** [T1] -- Mandatory for B2G since 1 January 2023; mandatory for B2B since 1 January 2024
8. **Does the client use fiscal cash registers?** [T1] -- Mandatory for retail (B2C) under Fiscalization Law
9. **PDV credit carried forward from prior period** [T1] -- Prethodni porez (pretplata)
10. **Does the client deal with the public sector (B2G)?** [T1] -- e-Faktura mandatory; treasury payment rules apply

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output PDV -- obracunati PDV) or Purchase (input PDV -- prethodni porez)
- Salaries (zarade), social contributions (doprinosi), tax payments, loan repayments, dividends = OUT OF SCOPE (never on PDV return)
- **Legislation:** Zakon o PDV, Article 3 (taxable transactions), Article 4 (supply of goods), Article 5 (supply of services)

### 1b. Determine Counterparty Location [T1]

- **Domestic (Serbia):** Supplier/customer is in Serbia
- **Foreign:** All countries outside Serbia (including EU member states)
- **Note:** Serbia is NOT an EU member state. Serbia is an EU candidate country. No intra-community supply rules apply.
- **Kosovo:** Treated as separate customs territory; imports from Kosovo treated as imports from abroad [T2]
- **Legislation:** Zakon o PDV, Article 11-12 (place of supply)

### 1c. Determine PDV Rate [T1]

| Rate | Category | Legal Basis |
|------|----------|-------------|
| 20% | Standard rate (opsta stopa) | Zakon o PDV, Article 23(1) |
| 10% | Reduced rate (posebna stopa) | Zakon o PDV, Article 23(2) |
| 0% | Zero-rated (exports, international transport) | Zakon o PDV, Article 24 |

### 1d. Standard Rate (20%) Applies To [T1]

- All goods and services not specifically listed for the reduced rate
- Professional services (legal, accounting, consulting, IT)
- Telecommunications and electronic services
- Construction services
- Motor vehicles
- Electronics, furniture, luxury goods
- Restaurant and catering services
- **Legislation:** Zakon o PDV, Article 23(1)

### 1e. Reduced Rate (10%) Applies To [T1]

| Category | Examples | Legal Basis |
|----------|----------|-------------|
| Basic foodstuffs | Bread, milk, flour, cooking oil, sugar, meat, fish, eggs, fruits, vegetables | Art 23(2), Point 1 |
| Daily newspapers | Newspapers published at least 3 times per week | Art 23(2), Point 4 |
| Medicines | Registered medicinal products | Art 23(2), Point 2 |
| Medical devices | Registered medical devices on official list | Art 23(2), Point 2a |
| Textbooks and teaching materials | School and university textbooks | Art 23(2), Point 5 |
| Hotel accommodation | First overnight stay (not food/beverages) | Art 23(2), Point 11 |
| Public utilities | Heating, water supply, waste collection | Art 23(2), Points 7-9 |
| Computers and components | Desktop, laptop, tablet computers | Art 23(2), Point 10 |
| Baby food and diapers | Infant nutrition and hygiene products | Art 23(2), Point 1a |
| Agricultural inputs | Seeds, fertilizers, pesticides | Art 23(2), Point 3 |
| Natural gas and firewood | Energy for household heating | Art 23(2), Point 13 |

### 1f. Zero-Rated Supplies [T1]

- Export of goods (Article 24(1), Point 1) -- goods must leave Serbia, confirmed by customs declaration
- International transport services (Article 24(1), Point 5)
- Supplies connected with international air and sea transport (Article 24(1), Point 4)
- Supplies to diplomatic and consular missions (Article 24(1), Point 6)
- Supplies financed by international donor agreements (Article 24(1), Point 7) [T2]
- **Note:** Zero-rated suppliers can claim full input PDV refund
- **Legislation:** Zakon o PDV, Article 24

### 1g. Exempt Supplies (Without Input PDV Recovery) [T1]

| Category | Legal Basis |
|----------|-------------|
| Financial services (banking, lending, securities) | Art 25(1), Point 1-5 |
| Insurance and reinsurance | Art 25(1), Point 6 |
| Residential rent (stambeni prostor) | Art 25(1), Point 10 |
| Education services (accredited institutions) | Art 25(1), Point 14 |
| Healthcare services (by licensed providers) | Art 25(1), Point 8 |
| Social welfare services | Art 25(1), Point 9 |
| Cultural and sporting events (by non-profits) | Art 25(1), Point 15-16 |
| Postal services (universal postal service) | Art 25(1), Point 7 |
| Land (not building land) | Art 25(1), Point 11 |
| Used residential property | Art 25(1), Point 12 |

**Note:** Exempt suppliers CANNOT recover input PDV on related purchases (Article 30)

**Legislation:** Zakon o PDV, Article 25

---

## Step 2: PDV Return Structure (PPPDV Form)

The PDV return (Poreska prijava poreza na dodatu vrednost -- PPPDV) is filed electronically via ePorezi. The form structure is:

### Section I: Output PDV (Obracunati PDV) [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| 001 | Taxable base at 20% (opsta stopa) | Net value of standard-rated supplies |
| 002 | PDV at 20% | = Field 001 x 20% |
| 003 | Taxable base at 10% (posebna stopa) | Net value of reduced-rated supplies |
| 004 | PDV at 10% | = Field 003 x 10% |
| 005 | Total output PDV | = Field 002 + Field 004 |

### Section II: Reverse Charge PDV (Interni obracun) [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| 006 | Taxable base for internal calculation at 20% | Import of services / deemed supplies |
| 007 | PDV at 20% (internal) | = Field 006 x 20% |
| 008 | Taxable base for internal calculation at 10% | Import of services at reduced rate |
| 009 | PDV at 10% (internal) | = Field 008 x 10% |
| 010 | Total internal PDV | = Field 007 + Field 009 |

### Section III: Total Output PDV [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| 011 | Total output PDV | = Field 005 + Field 010 |

### Section IV: Input PDV (Prethodni porez) [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| 101 | Input PDV at 20% (domestic) | From invoices with 20% PDV |
| 102 | Input PDV at 10% (domestic) | From invoices with 10% PDV |
| 103 | Input PDV from internal calculation (reverse charge) | = Field 007 + Field 009 |
| 104 | Input PDV on imports (from customs) | From customs declarations |
| 105 | Input PDV from agricultural farmers (pausalci) | 8% compensation |
| 106 | Input PDV corrections (increase) | Adjustments increasing input PDV |
| 107 | Input PDV corrections (decrease) | Adjustments decreasing input PDV |
| 108 | Total input PDV | = Fields 101+102+103+104+105+106-107 |

### Section V: PDV Payable or Credit [T1]

```
IF Field 011 > Field 108 THEN
    Field 109 (PDV payable / obaveza) = Field 011 - Field 108
    Field 110 = 0
ELSE
    Field 109 = 0
    Field 110 (PDV credit / pretplata) = Field 108 - Field 011
END
```

### Section VI: Exempt and Zero-Rated Supplies [T1]

| Field | Description | Notes |
|-------|-------------|-------|
| 201 | Exports (Article 24) | Zero-rated supply base |
| 202 | Exempt supplies without credit (Article 25) | Exempt supply base |
| 203 | Other non-taxable supplies | Informational |

**Legislation:** Zakon o PDV, Article 50-51; PPPDV form instructions (Pravilnik)

---

## Step 3: Reverse Charge (Interni Obracun) Mechanics [T1]

### 3a. When Reverse Charge Applies [T1]

The Serbian recipient must self-assess PDV (interni obracun) when:

1. **Services received from a foreign supplier** with no fixed establishment in Serbia (Article 10(1), Point 3)
2. **Goods imported (physical)** -- PDV assessed at customs, not via reverse charge on the return
3. **Specific domestic transactions** where the recipient is designated as the PDV debtor (Article 10(1), Point 3 and 3a):
   - Construction services (recipient is the PDV debtor if both parties are PDV registered)
   - Supplies of waste and secondary raw materials
   - Supplies of certain metals (as designated by regulation)

### 3b. Reverse Charge -- Foreign Services [T1]

| Step | Action | Field |
|------|--------|-------|
| 1 | Determine net value of service | Base amount |
| 2 | Apply appropriate rate (20% or 10%) | Determine rate |
| 3 | Report base in Field 006 or 008 | Output side (interni obracun) |
| 4 | Report PDV in Field 007 or 009 | Output PDV |
| 5 | Deduct same PDV in Field 103 | Input side |
| 6 | Net effect = zero for fully taxable businesses | Check |

**Legislation:** Zakon o PDV, Article 10(1), Point 3; Article 12

### 3c. Reverse Charge -- Domestic Construction [T2]

- When both supplier and recipient are PDV registered, and the supply is construction services
- The recipient (not the supplier) is the PDV debtor
- Supplier invoices without PDV, noting "PDV obracunava primalac" (PDV calculated by recipient)
- Recipient self-assesses in Fields 006/007 and deducts in Field 103
- **Flag for reviewer:** Confirm that the service qualifies as construction under the regulation
- **Legislation:** Zakon o PDV, Article 10(1), Point 3a

### 3d. Import of Goods [T1]

- PDV on imported physical goods is assessed and collected by Customs (Uprava Carina)
- Importer pays PDV at the border via customs declaration (carinska deklaracija)
- This import PDV is deductible as input PDV (Field 104)
- **Do NOT self-assess on the PPPDV return** -- Customs handles assessment
- **Legislation:** Zakon o PDV, Article 7 (import as taxable transaction), Article 28 (input PDV from imports)

---

## Step 4: E-Invoicing (e-Faktura) System

### 4a. Overview [T1]

Serbia has implemented a comprehensive mandatory e-invoicing system (Sistem elektronskih faktura -- SEF) managed by the Ministry of Finance.

| Milestone | Requirement |
|-----------|-------------|
| 1 January 2022 | B2G: Public sector entities must receive e-invoices |
| 1 January 2023 | B2G: All suppliers to public sector must issue via SEF |
| 1 January 2024 | B2B: Mandatory issuance and receipt between PDV taxpayers |
| Ongoing | B2C: Fiscal cash register (e-fiskalizacija) applies |

**Legislation:** Zakon o elektronskom fakturisanju (E-Invoicing Law), Official Gazette RS No. 44/2021

### 4b. SEF Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Registration | All PDV taxpayers must register on SEF portal |
| Invoice format | XML-based, transmitted via SEF system |
| Mandatory fields | PIB, date, invoice number, line items, PDV breakdown |
| Acceptance | B2G invoices require buyer acceptance within 15 days |
| Rejection | If B2G buyer does not respond within 15 days, invoice is deemed accepted |
| Storage | Invoices stored on SEF for 10 years |
| CRF integration | Public sector invoices also registered with CRF (Central Registry of Invoices) |

### 4c. Fiscal Cash Registers (e-Fiskalizacija) [T1]

| Requirement | Details |
|-------------|---------|
| Mandatory for | All retail (B2C) transactions |
| System | Electronic fiscal device (ESIR or V-PFR) connected to Tax Administration |
| Real-time reporting | Each transaction reported to Poreska uprava in real time |
| Receipt | Fiscal receipt with QR code issued to customer |

**Legislation:** Zakon o fiskalizaciji, Official Gazette RS No. 153/2020

---

## Step 5: Registration Rules

### 5a. Mandatory Registration [T1]

| Criterion | Threshold | Legal Basis |
|-----------|-----------|-------------|
| Domestic turnover (last 12 months) | RSD 8,000,000 | Art 38(1) |
| Foreign entities with taxable supply in Serbia | No threshold (any amount) | Art 10a |

- Once the RSD 8,000,000 threshold is exceeded, the taxpayer must apply for PDV registration within prescribed deadline
- PDV obligation begins from the day stated in the registration certificate
- **Legislation:** Zakon o PDV, Article 38

### 5b. Voluntary Registration [T1]

- Taxpayers below the RSD 8,000,000 threshold may voluntarily register
- Once registered voluntarily, the taxpayer must remain registered for at least 2 years
- **Legislation:** Zakon o PDV, Article 38a

### 5c. Non-Resident Registration [T1]

- Foreign entities performing taxable supplies in Serbia must either:
  1. Register for PDV through a fiscal representative (poreski punomoenik), OR
  2. Appoint a tax representative who assumes joint liability
- **Legislation:** Zakon o PDV, Article 10a

### 5d. Deregistration [T1]

- Taxpayer may apply for deregistration if turnover falls below RSD 8,000,000 for 12 consecutive months
- Must have been registered for at least 2 years (if voluntarily registered)
- Must adjust (reverse) input PDV on remaining assets at time of deregistration
- **Legislation:** Zakon o PDV, Article 39

---

## Step 6: Deductibility Rules

### 6a. General Deduction Right [T1]

- All input PDV on goods and services used for taxable business activities is deductible
- Input PDV must be documented by a proper PDV invoice (PDV racun), customs declaration, or e-Faktura
- **Legislation:** Zakon o PDV, Article 27-28

### 6b. Non-Deductible Input PDV (Article 29) [T1]

The following input PDV is BLOCKED and cannot be recovered:

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Passenger vehicles and motorcycles | Art 29(1), Point 1 | Exception: taxi, rental, driving school, vehicle dealers |
| Fuel for non-deductible vehicles | Art 29(1), Point 1 | Follows vehicle deductibility |
| Entertainment and hospitality (reprezentacija) | Art 29(1), Point 2 | 50% deductible only [T2] |
| Personal consumption of employees | Art 29(1), Point 3 | Gifts, personal items |
| Goods/services for exempt activities | Art 30 | No input PDV on exempt supplies |

### 6c. Partial Deduction -- Entertainment (Reprezentacija) [T2]

- 50% of input PDV on entertainment and hospitality is deductible
- Remaining 50% is non-deductible (becomes an expense for CIT purposes)
- **Flag for reviewer:** Confirm that the expense qualifies as reprezentacija under Article 29
- **Legislation:** Zakon o PDV, Article 29(1), Point 2

### 6d. Partial Exemption (Pro-Rata -- Srazmerni odbitak) [T2]

- If a business makes both taxable and exempt supplies, input PDV must be apportioned
- Pro-rata formula: `Deductible % = (Taxable Supplies + Zero-Rated Supplies) / Total Supplies x 100`
- Applied to input PDV that cannot be directly attributed to taxable or exempt activities
- Annual correction required
- **Flag for reviewer:** Pro-rata calculation must be confirmed by qualified tax adviser
- **Legislation:** Zakon o PDV, Article 30

### 6e. Capital Goods Adjustment [T2]

- Input PDV on capital goods (equipment >= 5 years useful life; real estate >= 10 years) is subject to adjustment if use changes
- If a capital good shifts from taxable to exempt use (or vice versa), input PDV must be corrected proportionally
- **Flag for reviewer:** Capital goods adjustment is complex; confirm with adviser
- **Legislation:** Zakon o PDV, Article 32

### 6f. Agricultural Flat-Rate Farmers (Pausalac) [T1]

- Farmers not registered for PDV are entitled to PDV compensation at 8% of their sales value
- The PDV-registered buyer pays the 8% compensation to the farmer and claims it as input PDV (Field 105)
- Farmer does not file PDV returns
- **Legislation:** Zakon o PDV, Article 34

---

## Step 7: Key Thresholds

| Threshold | Value | Notes |
|-----------|-------|-------|
| Standard PDV rate | 20% | Art 23(1) |
| Reduced PDV rate | 10% | Art 23(2) |
| Mandatory registration | RSD 8,000,000 (last 12 months) | Art 38(1) |
| Monthly filing threshold | RSD 50,000,000 annual turnover | Below = quarterly filing |
| Voluntary registration lock-in | 2 years minimum | Art 38a |
| Agricultural compensation rate | 8% | Art 34 |
| Entertainment deductibility | 50% of input PDV | Art 29(1)(2) |
| Capital goods adjustment -- equipment | 5 years | Art 32 |
| Capital goods adjustment -- real estate | 10 years | Art 32 |
| e-Faktura B2B mandatory | Since 1 January 2024 | E-Invoicing Law |

---

## Step 8: Filing Deadlines

| Return | Period | Filing Deadline | Payment Deadline |
|--------|--------|-----------------|-----------------|
| PPPDV (monthly filer) | Monthly | 15th of the following month | 15th of the following month |
| PPPDV (quarterly filer) | Quarterly | 20th of the month following quarter end | 20th of the month following quarter end |
| Annual PDV reconciliation | N/A | No separate annual return | N/A |
| e-Faktura registration | Ongoing | Must be registered before first B2B/B2G transaction | N/A |

**Filing method:** Electronic only via ePorezi portal (paper filing not accepted).

**Legislation:** Zakon o PDV, Article 48, 50, 51

### Late Filing and Payment Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | Fine: RSD 100,000 to RSD 2,000,000 for legal entities |
| Late payment | Interest: reference rate of NBS + 10% per annum (calculated daily) |
| Failure to issue e-Faktura | Fine: RSD 200,000 to RSD 2,000,000 for legal entities |
| Failure to register for PDV | Fine: RSD 100,000 to RSD 2,000,000 + mandatory registration |
| Non-use of fiscal cash register | Fine: RSD 300,000 to RSD 2,000,000 + temporary business closure |

**Legislation:** Zakon o PDV, Article 60-61; Zakon o poreskom postupku i poreskoj administraciji

---

## Step 9: Place of Supply Rules

### 9a. Supply of Goods [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| Goods not dispatched | Location of goods at time of supply | Art 11(1) |
| Goods dispatched/transported | Where dispatch begins | Art 11(1)(2) |
| Goods installed/assembled | Place of installation | Art 11(1)(3) |
| Import of goods | Serbia (at point of customs clearance) | Art 11(2) |

### 9b. Supply of Services [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| B2B (general rule) | Where the recipient is established | Art 12(4) |
| B2C (general rule) | Where the supplier is established | Art 12(5) |
| Real estate related | Where the property is located | Art 12(6)(1) |
| Transport of goods (B2B) | Where recipient is established | Art 12(4) |
| Cultural, sporting events | Where event takes place | Art 12(6)(4) |
| Restaurant/catering | Where services performed | Art 12(6)(5) |
| Short-term vehicle rental | Where vehicle made available | Art 12(6)(6) |

**Legislation:** Zakon o PDV, Articles 11-12

---

## Step 10: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., Microsoft 365) [T1]

**Situation:** Serbian company pays for cloud services from a US company, no PDV on invoice.
**Resolution:** Reverse charge (interni obracun). Self-assess at 20% in Fields 006/007. Deduct in Field 103. Net effect = zero.
**Legislation:** Zakon o PDV, Article 10(1)(3), Article 12(4)

### EC2 -- Export of goods to EU country [T1]

**Situation:** Serbian manufacturer exports goods to Germany. Customs declaration obtained.
**Resolution:** Zero-rated under Article 24(1)(1). Report in Field 201. No output PDV. Full input PDV recovery on related purchases.
**Legislation:** Zakon o PDV, Article 24(1)(1)

### EC3 -- Construction services between two PDV taxpayers [T2]

**Situation:** PDV-registered contractor provides construction services to PDV-registered developer.
**Resolution:** Reverse charge applies. Contractor invoices without PDV, noting "PDV obracunava primalac". Developer self-assesses in Fields 006/007, deducts in Field 103. Flag for reviewer: confirm service qualifies as construction.
**Legislation:** Zakon o PDV, Article 10(1)(3a)

### EC4 -- Purchase of passenger car [T1]

**Situation:** Company purchases a sedan for employee use.
**Resolution:** Input PDV is BLOCKED under Article 29(1)(1). PDV becomes part of the cost of the asset. No input PDV recovery.
**Legislation:** Zakon o PDV, Article 29(1)(1)

### EC5 -- Business entertainment (reprezentacija) [T2]

**Situation:** Company hosts a client dinner, PDV on invoice is RSD 5,000.
**Resolution:** 50% of input PDV (RSD 2,500) is deductible in Field 101. Remaining 50% (RSD 2,500) is non-deductible (expense for CIT). Flag for reviewer: confirm qualification as reprezentacija.
**Legislation:** Zakon o PDV, Article 29(1)(2)

### EC6 -- Purchase from flat-rate farmer (pausalac) [T1]

**Situation:** Food processing company buys wheat from an unregistered farmer for RSD 1,000,000.
**Resolution:** Company pays 8% compensation (RSD 80,000) to farmer. Company claims RSD 80,000 as input PDV in Field 105.
**Legislation:** Zakon o PDV, Article 34

### EC7 -- Import of goods from China [T1]

**Situation:** Serbian retailer imports electronics from China.
**Resolution:** PDV assessed by Customs at 20%. Import PDV deductible in Field 104. Do NOT self-assess on PPPDV. Customs duties are separate.
**Legislation:** Zakon o PDV, Article 7, Article 28

### EC8 -- Residential property rental [T1]

**Situation:** Company rents out apartments to tenants.
**Resolution:** Exempt under Article 25(1)(10). No output PDV. Input PDV on related costs is NOT deductible (Article 30).
**Legislation:** Zakon o PDV, Article 25(1)(10)

### EC9 -- Credit notes [T1]

**Situation:** Supplier issues a credit note reducing a previous invoice.
**Resolution:** Adjust the original entry. If original was in Field 001/002 (output), reduce Fields 001/002 by credit note amount. If original was input, reduce relevant input field. Issue credit note via e-Faktura system.
**Legislation:** Zakon o PDV, Article 21

### EC10 -- Services to foreign client (B2B export of services) [T1]

**Situation:** Serbian IT company provides software development to a UK client.
**Resolution:** Place of supply is where the recipient is established (UK) per Article 12(4). Supply is outside the scope of Serbian PDV. No PDV charged. Not reported as output but may be shown in Field 203 (informational). Input PDV on related costs is deductible.
**Legislation:** Zakon o PDV, Article 12(4)

### EC11 -- Supply of waste and secondary raw materials [T2]

**Situation:** Company sells scrap metal to another PDV-registered company.
**Resolution:** Reverse charge applies. Seller invoices without PDV. Buyer self-assesses. Flag for reviewer: confirm material qualifies under the waste/scrap regulation.
**Legislation:** Zakon o PDV, Article 10(1)(3a)

### EC12 -- Free supply of goods (employee gifts) [T1]

**Situation:** Company distributes promotional gifts to employees.
**Resolution:** Deemed taxable supply if input PDV was deducted on acquisition. Output PDV must be charged on the market value (emsal vrednost). If input PDV was not deducted, no output PDV.
**Legislation:** Zakon o PDV, Article 4(4)

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

### Test 1 -- Standard domestic sale at 20%

**Input:** Serbian company sells IT consulting to a domestic client, net RSD 500,000, PDV RSD 100,000.
**Expected output:** Field 001 = RSD 500,000. Field 002 = RSD 100,000. Output PDV reported.

### Test 2 -- Reduced rate sale at 10%

**Input:** Bakery sells bread to a retailer, net RSD 200,000, PDV RSD 20,000.
**Expected output:** Field 003 = RSD 200,000. Field 004 = RSD 20,000.

### Test 3 -- Export of goods, zero-rated

**Input:** Serbian manufacturer exports furniture to Italy, net RSD 3,000,000. Customs declaration obtained.
**Expected output:** Field 201 = RSD 3,000,000. No output PDV. Input PDV on related purchases refundable.

### Test 4 -- Import of services, reverse charge

**Input:** Serbian company receives marketing services from a UK agency, EUR 10,000 (approx. RSD 1,170,000). No PDV on invoice.
**Expected output:** Field 006 = RSD 1,170,000. Field 007 = RSD 234,000 (20%). Field 103 = RSD 234,000. Net effect = zero.

### Test 5 -- Purchase of passenger car, blocked input

**Input:** Company purchases sedan, net RSD 5,000,000, PDV RSD 1,000,000.
**Expected output:** Input PDV of RSD 1,000,000 is BLOCKED (Article 29). Asset capitalized at RSD 6,000,000. No input PDV recovery.

### Test 6 -- Entertainment expense at 50%

**Input:** Company hosts client dinner, net RSD 30,000, PDV RSD 6,000.
**Expected output:** Field 101 includes RSD 3,000 (50% of RSD 6,000). Remaining RSD 3,000 non-deductible.

### Test 7 -- Purchase from flat-rate farmer

**Input:** Food processor buys milk from unregistered farmer, purchase price RSD 500,000.
**Expected output:** Compensation paid to farmer: RSD 40,000 (8%). Field 105 = RSD 40,000.

### Test 8 -- Construction reverse charge (domestic)

**Input:** PDV-registered contractor invoices PDV-registered developer for construction work, net RSD 10,000,000. No PDV on invoice.
**Expected output:** Developer: Field 006 = RSD 10,000,000. Field 007 = RSD 2,000,000. Field 103 = RSD 2,000,000. Net = zero.

---

## PROHIBITIONS [T1]

- NEVER allow input PDV deduction on passenger vehicles (unless taxi/rental/dealer business)
- NEVER skip reverse charge (interni obracun) for services received from foreign suppliers
- NEVER treat Serbia as an EU member state -- no intra-community rules apply
- NEVER allow full input PDV deduction on entertainment -- maximum 50%
- NEVER issue paper invoices when e-Faktura is mandatory
- NEVER confuse zero-rated (Article 24, with input recovery) with exempt (Article 25, without input recovery)
- NEVER register import of goods via reverse charge -- Customs handles PDV on imports
- NEVER allow input PDV recovery on purchases used for exempt activities (Article 30)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER ignore the RSD 8,000,000 registration threshold -- monitor and flag when approaching

---

## Step 13: Invoice Requirements and Documentation

### 13a. PDV Invoice (PDV Racun) Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Who must issue | All PDV-registered taxpayers for every taxable supply |
| Mandatory fields | Supplier name, PIB, PDV number; buyer name, PIB, PDV number; date of issue; sequential number; date of supply; description; quantity; unit price; taxable base; PDV rate; PDV amount; total |
| Issuance deadline | By the date of supply or receipt of advance payment |
| Format | e-Faktura (electronic) for all B2B and B2G transactions |
| Storage | 10 years (electronic storage on SEF system) |
| Language | Serbian (translations may be attached for cross-border) |

**Legislation:** Zakon o PDV, Article 42; Zakon o elektronskom fakturisanju

### 13b. Credit Note (Knjizno odobrenje) and Debit Note (Knjizno zaduzenje) [T1]

| Document | Purpose | Requirements |
|----------|---------|-------------|
| Credit note | Reduce previously invoiced amount | Must reference original invoice number; issue via e-Faktura |
| Debit note | Increase previously invoiced amount | Must reference original invoice number; issue via e-Faktura |
| PDV effect | Both adjust output and input PDV in the period of issuance | Buyer and seller adjust simultaneously |

### 13c. Internal Invoice (Interni Racun) [T1]

| Requirement | Details |
|-------------|---------|
| When issued | For reverse charge (interni obracun) transactions -- services from abroad |
| Who issues | The Serbian recipient (PDV payer) |
| Purpose | Self-assesses PDV on imported services |
| Fields | Same as PDV racun but supplier section shows foreign entity details |
| Registration | Must be registered in the e-Faktura system |

---

## Step 14: Advance Payments and Tax Point Rules

### 14a. Tax Point (Promet) [T1]

| Event | Tax Point | Legal Basis |
|-------|-----------|-------------|
| Supply of goods | Date of delivery | Art 14(1) |
| Supply of services | Date of completion | Art 15(1) |
| Advance payment received | Date of receipt | Art 16(1) |
| Continuous supply | End of each billing period | Art 14(4) |
| Import of goods | Date of customs clearance | Art 7 |

### 14b. Advance Payments [T1]

- When an advance payment (avans) is received, PDV is triggered immediately
- Seller must issue a PDV invoice for the advance
- When goods/services are subsequently delivered, a final invoice is issued covering the remaining amount
- The advance PDV invoice and final invoice together equal the total transaction
- **Legislation:** Zakon o PDV, Article 16

---

## Step 15: Penalties and Interest Reference Table

| Violation | Amount / Rate | Legal Basis |
|-----------|--------------|-------------|
| Late filing of PPPDV | Fine: RSD 100,000 -- RSD 2,000,000 (legal entity) | Art 60 |
| Late filing (entrepreneur) | Fine: RSD 50,000 -- RSD 500,000 | Art 60 |
| Late filing (responsible person) | Fine: RSD 10,000 -- RSD 100,000 | Art 60 |
| Late payment | Interest: NBS reference rate + 10% p.a. (daily calculation) | Zakon o poreskom postupku |
| Failure to register for PDV | Fine: RSD 100,000 -- RSD 2,000,000 + mandatory registration | Art 60 |
| Failure to issue e-Faktura | Fine: RSD 200,000 -- RSD 2,000,000 (legal entity) | E-Invoicing Law |
| Failure to use fiscal cash register | Fine: RSD 300,000 -- RSD 2,000,000 + temporary closure (up to 60 days) | Fiscalization Law |
| Issuing incorrect PDV invoice | Fine: RSD 100,000 -- RSD 2,000,000 | Art 60 |
| Tax evasion | Criminal prosecution under Criminal Code | Criminal Code Art 229 |
| Failure to keep records | Fine: RSD 100,000 -- RSD 2,000,000 | Art 60 |

---

## Step 16: Double Taxation Treaty Considerations [T3]

- Serbia has an extensive double taxation treaty network (over 60 treaties)
- DTTs do NOT affect PDV/VAT obligations -- they cover income tax only
- However, DTTs may affect withholding tax on payments that also have PDV implications
- **ALWAYS escalate cross-border arrangements involving DTT analysis to a qualified tax adviser**
- **Legislation:** Individual DTTs; Zakon o porezu na dobit pravnih lica (Corporate Income Tax Law)

---

## Step 17: Record-Keeping Requirements [T1]

| Record Type | Retention Period | Legal Basis |
|-------------|-----------------|-------------|
| PDV invoices (e-Faktura system) | 10 years (stored on SEF) | E-Invoicing Law |
| Accounting ledgers | 10 years | Zakon o racunovodstvu |
| Bank statements | 10 years | Zakon o racunovodstvu |
| Contracts and agreements | 10 years | Zakon o racunovodstvu |
| Customs declarations | 5 years | Carinski zakon |
| PPPDV returns (filed electronically) | Maintained by Poreska uprava | Electronic filing |
| Fiscal cash register data | 5 years | Zakon o fiskalizaciji |
| Internal invoices (interni racun) | 10 years | E-Invoicing Law |

---

## 2026 Legislative Amendments (Effective 1 April 2026)

Serbia adopted a major package of amendments to the VAT Law on 3 December 2025 (Official Gazette RS No. 109/2025), largely effective from 1 April 2026:

| Change | Details | Effective |
|--------|---------|-----------|
| Credit notes mandatory | Suppliers must issue credit notes for any subsequent decrease in tax base | 1 April 2026 |
| PDV correction timing | Reduction in calculated PDV allowed in the period the change occurred, subject to conditions by filing deadline | 1 April 2026 |
| Pre-filled VAT returns | Pre-completed PPPDV returns introduced via SEF e-invoicing system | 1 January 2026 |
| Internal invoice compliance | No input PDV deduction unless internal invoices comply with SEF rules | 1 April 2026 |
| E-invoicing alignment | Advances and tax base adjustments must follow SEF format requirements | 1 April 2026 |

**Note:** VAT rates (20% standard, 10% reduced) are unchanged by these amendments. The changes are procedural/administrative.

---

## Contribution Notes

This skill covers Serbian PDV as of April 2026. Serbian tax law is subject to frequent amendment. All rates and thresholds should be verified against the most recent Official Gazette publications before filing. A qualified Serbian tax adviser (poreski savetnik) must validate all T1 rules before this skill is used in production.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
