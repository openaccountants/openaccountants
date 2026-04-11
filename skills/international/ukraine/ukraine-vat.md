---
name: ukraine-vat
description: Use this skill whenever asked to prepare, review, or advise on a Ukraine VAT (PDV) return or any PDV-related classification. Trigger on phrases like "prepare PDV return", "Ukraine VAT", "podatok na dodanu vartist", "Ukrainian VAT filing", "DPS", "SEA PDV", "tax invoice registration", or any request involving Ukrainian VAT obligations. This skill contains the complete Ukrainian PDV classification rules, rate tables, electronic administration system (SEA PDV) rules, mandatory tax invoice registration, filing deadlines, and deductibility rules required to produce a correct return. ALWAYS read this skill before touching any Ukraine VAT-related work.
---

# Ukraine VAT (PDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ukraine (Ukraina) |
| Jurisdiction Code | UA |
| Primary Legislation | Podatkovyi Kodeks Ukrainy (Tax Code of Ukraine, TCU), Law No. 2755-VI of 2 December 2010 |
| Supporting Legislation | CMU Resolutions on VAT administration; Order of Ministry of Finance on PDV return form; Law on Electronic Administration of VAT |
| Tax Authority | Derzhavna Podatkova Sluzhba (DPS -- State Tax Service of Ukraine) |
| Filing Portal | https://cabinet.tax.gov.ua (Electronic Cabinet of Taxpayer) |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return field assignment, reverse charge, tax invoice registration, SEA PDV mechanics. Tier 2: wartime temporary provisions, agricultural special regime (legacy), partial exemption. Tier 3: group structures, free economic zones, occupied territory transactions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax adviser and document the gap.

---

## Wartime Provisions Notice [T2]

**IMPORTANT:** Since 24 February 2022, martial law (voiennyi stan) has been in effect in Ukraine. Temporary legislative provisions affect PDV administration:

| Provision | Impact | Status |
|-----------|--------|--------|
| Extended filing deadlines | Taxpayers in combat zones may have extended deadlines | Active during martial law |
| Tax invoice registration grace period | 6 months after martial law ends to register invoices that could not be registered during hostilities | Active |
| Destroyed/lost goods | Input PDV on goods destroyed due to hostilities is not reversed, but cannot be refunded in cash -- offset only | Active |
| Free supply to Armed Forces | Supply of goods/services free of charge to the Armed Forces of Ukraine is not treated as a taxable supply | Active |
| Import exemptions | Certain military goods and humanitarian aid imports are PDV-exempt | Active |
| Simplified registration | Simplified voluntary registration available for certain entities | Active |

**Flag for reviewer:** All filings during martial law should be reviewed for applicability of temporary provisions. Provisions may be extended, modified, or terminated by Verkhovna Rada (parliament).

**Legislation:** Tax Code of Ukraine, Transitional Provisions; Laws No. 2118-IX, 2120-IX, and subsequent amendments

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and EDRPOU code (or RNOCPP for individuals)** [T1] -- EDRPOU is 8-digit code for legal entities; RNOCPP is 10-digit individual tax number
2. **PDV registration number (IPN -- Individualnyi Podatkovyi Nomer)** [T1] -- 12-digit number assigned upon PDV registration
3. **Registration type** [T1] -- Mandatory PDV payer, voluntary PDV payer, or non-registered (below threshold)
4. **Filing period** [T1] -- Monthly (standard for all PDV payers)
5. **Industry/sector** [T2] -- Impacts specific rates (7%, 14%) and exemption rules
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional allocation required (Article 199 TCU)
7. **SEA PDV account balance** [T1] -- Electronic administration system account balance (affects ability to register tax invoices)
8. **Is the client in a territory affected by hostilities?** [T2] -- Wartime provisions may apply
9. **PDV credit carried forward from prior period** [T1] -- Vidiemnne znachennia PDV
10. **Does the client export goods or services?** [T1] -- Zero-rated; refund eligibility

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output PDV -- podatkove zoboviazannia) or Purchase (input PDV -- podatkovyi kredyt)
- Salaries (zarobitna plata), social contributions (YeSV), tax payments, loan repayments, dividends = OUT OF SCOPE (never on PDV return)
- **Legislation:** Tax Code of Ukraine, Article 185 (taxable transactions)

### 1b. Determine Counterparty Location [T1]

- **Domestic (Ukraine):** Supplier/customer is in Ukraine (government-controlled territory)
- **EU:** EU member states (not relevant for intra-community rules as Ukraine is not an EU member, but relevant for place of supply)
- **Foreign:** All countries outside Ukraine
- **Temporarily occupied territories (TOT):** Crimea and parts of Donetsk, Luhansk, Zaporizhzhia, Kherson oblasts [T3] -- special rules; escalate
- **Note:** Ukraine is NOT an EU member state. No intra-community supply rules apply. Ukraine is an EU candidate country.
- **Legislation:** TCU Article 185-186 (place of supply)

### 1c. Determine PDV Rate [T1]

| Rate | Category | Legal Basis |
|------|----------|-------------|
| 20% | Standard rate (zagalna stavka) | TCU Article 193.1 |
| 14% | Reduced rate (for certain agricultural products) | TCU Article 193.1 |
| 7% | Reduced rate (medicines, medical devices) | TCU Article 193.1 |
| 0% | Zero-rated (exports, international transport) | TCU Article 195 |

### 1d. Standard Rate (20%) Applies To [T1]

- All goods and services not specifically listed for reduced rates, zero rate, or exemption
- Professional services (legal, accounting, consulting, IT)
- Telecommunications and electronic services
- Construction services and materials
- Motor vehicles (new and used)
- Electronics, furniture, clothing
- Restaurant and catering services
- Real property transactions (excluding residential -- first supply)
- **Legislation:** TCU Article 193.1

### 1e. Reduced Rate -- 7% [T1]

| Category | Examples | Legal Basis |
|----------|----------|-------------|
| Medicines | Registered medicinal products on approved list | TCU Art 193.1(1) |
| Medical devices | Registered medical devices and equipment | TCU Art 193.1(1) |
| Certain cultural services | Admission to theaters, museums, exhibitions | TCU Art 193.1 |
| Periodicals (newspapers, magazines) | Print and digital periodicals | TCU Art 193.1 |

### 1f. Reduced Rate -- 14% [T1]

| Category | Examples | Legal Basis |
|----------|----------|-------------|
| Certain agricultural products | Soybeans, rapeseed, sunflower seeds, corn, sugar beet, flax, hemp | TCU Art 193.1 |
| Milk (raw) | Supplied by agricultural producers | TCU Art 193.1 |
| Livestock (live weight) | Cattle, pigs, poultry -- supplied by agricultural producers | TCU Art 193.1 |

**Note:** The 14% rate was introduced in 2021 (replacing the abolished special agricultural regime) and applies to a specific list of agricultural commodities.

### 1g. Zero-Rated Supplies [T1]

- Export of goods (Article 195.1.1) -- goods must leave Ukraine customs territory, confirmed by customs declaration
- International transport of passengers and cargo (Article 195.1.3)
- Supplies to duty-free shops (Article 195.1.4)
- Supplies of gold to the National Bank of Ukraine (Article 195.1.5)
- Toll processing services on goods subsequently exported (Article 195.1.6)
- **Note:** Zero-rated suppliers can claim full input PDV refund
- **Legislation:** TCU Article 195

### 1h. Exempt Supplies (Without Input PDV Recovery) [T1]

| Category | Legal Basis |
|----------|-------------|
| Financial and banking services | Art 197.1.1 |
| Insurance services | Art 197.1.2 |
| Education services (licensed institutions) | Art 197.1.7 |
| Healthcare services (licensed institutions) | Art 197.1.5 |
| Postal services (Ukrposhta -- universal service) | Art 197.1.3 |
| Residential rent | Art 197.1.14 |
| Land transactions (except building land) | Art 197.1.21 |
| Religious organizations (sales of religious items) | Art 197.1.8 |
| Precious metals to NBU | Art 197.1.9 |
| Social housing (first supply) | Art 197.1.14 |
| Funeral services | Art 197.1.10 |

**Note:** Exempt suppliers CANNOT recover input PDV on related purchases (Article 198.4)

**Legislation:** TCU Article 197

---

## Step 2: PDV Return Structure

The PDV return (Podatkova deklaratsiia z PDV) is filed electronically via the taxpayer's electronic cabinet. Monthly filing is mandatory for all PDV payers.

### Section I: Tax Obligations (Output PDV -- Podatkovi Zoboviazannia) [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 1 | Supply of goods/services at 20% -- base | Net value |
| 1.1 | PDV at 20% | = Line 1 x 20% |
| 2 | Supply of goods/services at 7% -- base | Net value |
| 2.1 | PDV at 7% | = Line 2 x 7% |
| 3 | Supply of goods/services at 14% -- base | Net value |
| 3.1 | PDV at 14% | = Line 3 x 14% |
| 4 | Export of goods (0%) | Zero-rated base |
| 5 | Other zero-rated supplies | Other Art 195 supplies |
| 6 | Exempt supplies (Art 197) | Exempt base (informational) |
| 7 | Supplies not subject to PDV | Out-of-scope (informational) |
| 8 | Self-assessed PDV on imported services | Reverse charge output |
| 8.1 | PDV on imported services | = Line 8 x applicable rate |
| 9 | Total output PDV | = 1.1 + 2.1 + 3.1 + 8.1 |

### Section II: Tax Credit (Input PDV -- Podatkovyi Kredyt) [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 10 | Domestic purchases with PDV -- base | From registered tax invoices |
| 10.1 | Input PDV on domestic purchases | From tax invoices |
| 11 | Import of goods -- base | From customs declarations |
| 11.1 | Import PDV | From customs declarations |
| 12 | Input PDV on imported services (reverse charge offset) | = Line 8.1 |
| 13 | Adjustment increase (from calculation of Art 192, 199) | Corrections increasing credit |
| 14 | Adjustment decrease (from calculation of Art 192, 199) | Corrections decreasing credit |
| 15 | Credit from prior periods (negative value carried forward) | Vidiemnne znachennia |
| 16 | Total input PDV | = 10.1 + 11.1 + 12 + 13 - 14 + 15 |

### Section III: Calculation of PDV Payable or Credit [T1]

```
IF Line 9 > Line 16 THEN
    Line 18 (PDV payable / suma PDV do splaty) = Line 9 - Line 16
    Line 19 = 0
    Line 20 = 0
ELSE
    Line 18 = 0
    Line 19 (Negative value / vidiemnne znachennia) = Line 16 - Line 9
    Line 20.1 (Amount declared for budget refund) = portion of Line 19 requested as refund [T2]
    Line 20.2 (Carry-forward to next period) = Line 19 - Line 20.1
END
```

**Legislation:** TCU Articles 200-200a; Ministry of Finance Order on PDV return form

---

## Step 3: Electronic Administration System (SEA PDV)

### 3a. Overview [T1]

Ukraine operates a unique Electronic Administration System for VAT (Systema Elektronnogo Administruvannia PDV -- SEA PDV). Each PDV payer has a special account (rakhunok v SEA PDV) at the State Treasury.

| Feature | Details |
|---------|---------|
| Purpose | Control registration of tax invoices; prevent fraudulent input PDV claims |
| Account | Each PDV payer has a virtual account in the Treasury |
| Registration limit | Tax invoices can only be registered if the SEA PDV account has sufficient balance |
| Balance formula | See 3b below |

**Legislation:** TCU Article 200-1

### 3b. SEA PDV Account Balance Formula [T1]

```
Registration Limit (reiestratsiyni limit) =

  + PDV paid to the SEA account (bank transfers to Treasury)
  + Input PDV from registered tax invoices received
  + Import PDV paid at customs
  + PDV overpayment from prior periods
  + Adjustment notes received
  - Output PDV from registered tax invoices issued
  - PDV declared for budget refund
  - Adjustment notes issued
```

**Key principle:** You CANNOT register a tax invoice (podatkova nakladna) if your SEA PDV account balance is insufficient. If the registration limit is too low, the taxpayer must either:

1. Wait for incoming tax invoices from suppliers to increase the balance, or
2. Transfer funds (top-up) to the SEA PDV account at the Treasury

### 3c. Consequences of Non-Registration [T1]

| Scenario | Consequence |
|----------|-------------|
| Tax invoice not registered within 15 days | Buyer cannot claim input PDV |
| Tax invoice registered late (after 15 days) | Buyer can claim input PDV only after registration, but seller faces a fine |
| Tax invoice not registered at all | Buyer has NO input PDV right; seller faces fines |
| Wartime grace period | Tax invoices that could not be registered during hostilities may be registered within 6 months after martial law ends [T2] |

**Legislation:** TCU Article 201.10

### 3d. Tax Invoice (Podatkova Nakladna) Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Format | Electronic only (since 1 January 2017) |
| Registration | Must be registered in the Unified Register of Tax Invoices (YERPN) within 15 calendar days |
| Mandatory fields | Supplier and buyer IPN, date, sequential number, description, quantity, unit price, PDV amount, rate |
| Self-invoice (samoinvois) | Required for reverse charge on imported services (supplier section left blank or shows non-resident) |
| Correction (rozrakhunok koryguvannia) | Adjustment document for changing registered tax invoices |
| Blocking | Tax invoices may be automatically blocked by the SMKOR system (monitoring criteria) -- see 3e |

### 3e. Tax Invoice Blocking (SMKOR) [T2]

- The automatic monitoring system (SMKOR -- Systema Monitoryngu Kryteriiv Otsinky Ryzykiv) may block registration of tax invoices deemed high-risk
- Blocking criteria include: new registrants, mismatched volumes, suspicious patterns
- If blocked, the taxpayer must submit explanations and supporting documents to unblock
- Unblocking decision by a regional commission within 5 business days
- If not unblocked, the taxpayer can appeal to court
- **Flag for reviewer:** Blocking events should be tracked; they can delay input PDV claims for buyers
- **Legislation:** TCU Article 201.16; CMU Resolution No. 1165

---

## Step 4: Reverse Charge Mechanics [T1]

### 4a. Import of Goods [T1]

- PDV on imported physical goods is assessed and collected by Customs (Derzhavna Mytna Sluzhba)
- Importer pays PDV at the border via customs declaration (mytna deklaratsiia)
- This import PDV is deductible as input PDV (Line 11.1)
- Import PDV paid at customs also increases the SEA PDV registration limit
- **Do NOT self-assess imports of goods on the PDV return** -- Customs handles assessment
- **Legislation:** TCU Article 190, 206

### 4b. Import of Services (Reverse Charge) [T1]

- When a Ukrainian PDV payer receives services from a non-resident with no permanent establishment in Ukraine:
  1. Self-assess PDV at the applicable rate (20%, 7%, or 14%) on the service value
  2. Report in Line 8 (base) and Line 8.1 (PDV)
  3. Register a self-invoice (podatkova nakladna) in YERPN
  4. Claim input PDV in Line 12 (= Line 8.1)
  5. Net effect: zero for fully taxable businesses
- **Legislation:** TCU Article 208

### 4c. Non-Resident Digital Services [T2]

- Since 1 January 2022, non-resident providers of electronic services (e-services) to Ukrainian individuals (B2C) must register for PDV and charge 20%
- Applies to: streaming services, app stores, online advertising, cloud services (B2C)
- B2B: standard reverse charge by the Ukrainian business applies (not the foreign provider)
- **Flag for reviewer:** Determine if the foreign provider is already registered and charging PDV (B2C) or if the Ukrainian business should self-assess (B2B)
- **Legislation:** TCU Article 208-1

---

## Step 5: Deductibility Rules

### 5a. General Deduction Right [T1]

- All input PDV on goods and services used for taxable business activities is deductible
- Input PDV must be confirmed by a registered tax invoice (podatkova nakladna) in YERPN or customs declaration
- If the tax invoice is not registered in YERPN, the buyer CANNOT claim input PDV
- **Legislation:** TCU Article 198

### 5b. Non-Deductible Input PDV [T1]

The following input PDV is BLOCKED and cannot be recovered:

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| Passenger vehicles (lehkovyi avtomobil) | Art 198.4 / Art 139.1.6 | Exception: taxi, rental car, emergency services |
| Goods/services not used in business | Art 198.4 | Personal consumption |
| Purchases without registered tax invoice | Art 198.6 | No YERPN registration = no credit |
| Goods/services for exempt activities | Art 198.4 | No input PDV on exempt supplies |
| Entertainment (if not business-related) | Art 198.4 / Art 139.1.1 | Flag for reviewer [T2] |
| Goods destroyed/stolen (non-wartime) | Art 198.5 | Must reverse previously claimed input PDV |

### 5c. Vehicle Deductibility Rules [T1]

| Vehicle Type | Input PDV Deductible | Notes |
|-------------|----------------------|-------|
| Private passenger car (lehkovyi avtomobil) | NO | Blocked |
| Taxi (licensed) | YES | Business use vehicle |
| Rental car (by rental company) | YES | Business stock |
| Delivery van (classified as vantazhnyi) | YES | Commercial vehicle |
| Truck (vantazhnyi avtomobil) | YES | Commercial vehicle |
| Bus | YES | Commercial vehicle |
| Ambulance / emergency | YES | Special purpose vehicle |
| Fuel for blocked vehicle | NO | Follows vehicle classification |
| Fuel for deductible vehicle | YES | Follows vehicle classification |

### 5d. Proportional Allocation (Article 199) [T2]

- If a business makes both taxable and exempt supplies, input PDV on shared overhead must be proportionally allocated
- Formula: `Deductible % = (Taxable + Zero-Rated Supplies) / Total Supplies x 100`
- Calculated based on prior year's proportions; adjusted annually (re-calculation in December return)
- Threshold: if taxable supplies are >= 97% of total, the business may treat all input PDV as deductible (no allocation needed)
- **Flag for reviewer:** Proportional allocation must be confirmed by qualified tax adviser
- **Legislation:** TCU Article 199

### 5e. Destroyed and Lost Goods [T1]

- If goods for which input PDV was claimed are destroyed or lost, the input PDV must be reversed (charged as output PDV)
- **Exception (wartime):** Goods destroyed as a result of hostilities (Russian aggression) are NOT subject to input PDV reversal [T2]
- However, wartime-destroyed goods PDV cannot be refunded in cash -- can only offset future liabilities
- **Flag for reviewer:** Documentation of wartime destruction required (military administration confirmation)
- **Legislation:** TCU Article 198.5; Transitional Provisions

---

## Step 6: PDV Refund Mechanism

### 6a. Refund Eligibility [T1]

- When input PDV exceeds output PDV (negative value / vidiemnne znachennia), the excess can be:
  1. Carried forward to the next period (Line 20.2), OR
  2. Declared for budget refund (Line 20.1)
- Budget refund is available if the negative value is confirmed by the SEA PDV account balance

### 6b. Refund Process [T1]

| Step | Timeline | Notes |
|------|----------|-------|
| Declaration filed | By filing deadline | Refund amount declared in Line 20.1 |
| DPS verification | 30 calendar days (standard) / 60 days (audit) | DPS checks YERPN registrations and SEA balance |
| Refund conclusion | Within 5 days after verification | DPS issues refund conclusion to Treasury |
| Payment | Within 5 business days after conclusion | Treasury transfers to taxpayer's bank account |

### 6c. Automatic Refund [T1]

- Taxpayers meeting "risk criteria" (positive compliance history) are eligible for automatic refund without desk audit
- Criteria: registered for 24+ months, no tax debt, director not under criminal investigation, sufficient operational activity
- **Legislation:** TCU Article 200.19-200.20

### 6d. Refund Delays and Issues [T2]

- Refund delays are common in practice, especially during wartime
- If DPS misses the 30/60-day deadline, the taxpayer is entitled to interest
- If the refund is rejected, the taxpayer can appeal administratively (within 10 days) or judicially
- **Flag for reviewer:** Track refund applications and follow up on overdue refunds
- **Legislation:** TCU Article 200

---

## Step 7: Key Thresholds

| Threshold | Value | Notes |
|-----------|-------|-------|
| Standard PDV rate | 20% | TCU Art 193.1 |
| Reduced PDV rate (medicines) | 7% | TCU Art 193.1 |
| Reduced PDV rate (agriculture) | 14% | TCU Art 193.1 |
| Mandatory registration | UAH 1,000,000 (last 12 months) | TCU Art 181.1 |
| Tax invoice registration deadline | 15 calendar days from date of supply | TCU Art 201.10 |
| Proportional allocation threshold | 97% taxable = no allocation needed | TCU Art 199 |
| Automatic refund eligibility | 24+ months registered | TCU Art 200.19 |
| Document retention | 1,095 days (3 years) from filing deadline | TCU Art 44.3 |
| SEA PDV top-up | No minimum | Voluntary transfer to Treasury |

---

## Step 8: Filing Deadlines

| Return | Period | Filing Deadline | Payment Deadline |
|--------|--------|-----------------|-----------------|
| PDV return (standard) | Monthly | 20th of the following month | 10 calendar days after filing deadline (i.e., 30th) |
| PDV return (wartime extended) | Monthly | May be extended for taxpayers in combat zones [T2] | Correspondingly extended |
| Correction return (utochniuiucha) | N/A | Anytime (corrections to prior periods) | Additional PDV + 3% self-assessed penalty |

**Filing method:** Electronic only via the Electronic Cabinet of Taxpayer (Elektronyi Kabinet Platnyaka Podatkiv).

**Legislation:** TCU Article 49, 203

### Late Filing and Payment Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing (first occurrence in year) | Warning (no fine) |
| Late filing (repeated) | UAH 340 |
| Late filing (continued, 30+ days late) | UAH 1,020 |
| Late payment | Penalty interest (penia): 120% of NBU discount rate per annum, calculated daily |
| Failure to register tax invoice (within 15 days) | 10% of PDV amount on the invoice |
| Failure to register tax invoice (16-30 days late) | 20% of PDV amount |
| Failure to register tax invoice (31-60 days late) | 30% of PDV amount |
| Failure to register tax invoice (61+ days late) | 40% of PDV amount |
| Non-registration (no invoice issued at all) | 50% of PDV amount |

**Note:** Wartime provisions may suspend certain penalties for taxpayers in territories with active hostilities [T2].

**Legislation:** TCU Articles 120-1, 126-1, 163

---

## Step 9: Place of Supply Rules

### 9a. Supply of Goods [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| Goods located in Ukraine at time of supply | Ukraine | Art 186.1(a) |
| Goods dispatched from Ukraine | Ukraine | Art 186.1(a) |
| Goods imported into Ukraine | Ukraine (at customs) | Art 186.1(c) |
| Goods exported from Ukraine | Ukraine (zero-rated) | Art 195 |

### 9b. Supply of Services [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| B2B (general rule) | Where the recipient is registered | Art 186.4 |
| B2C (general rule) | Where the supplier is registered | Art 186.4 |
| Real estate related | Where the property is located | Art 186.2.2(a) |
| Cultural, artistic, sporting events | Where event takes place | Art 186.2.1(a) |
| Transport of goods | Where transport occurs (proportionally) | Art 186.2.3 |
| Restaurant/catering | Where services performed | Art 186.2.2(b) |
| Electronic services (B2C from non-resident) | Where buyer is located (Ukraine) | Art 208-1 |

**Legislation:** TCU Articles 185-186

---

## Step 10: Agricultural Sector Special Rules

### 10a. Former Special Regime (Historical Context) [T1]

- Until 31 December 2016, agricultural producers could use a special PDV regime where PDV collected was retained by the producer (not remitted to the budget)
- This regime was abolished from 1 January 2017
- The 14% reduced rate was introduced in 2021 as a partial substitute for certain agricultural commodities

### 10b. Current Agricultural Rules [T1]

| Item | Rate | Notes |
|------|------|-------|
| Soybeans | 14% | On the specified list |
| Rapeseed (canola) | 14% | On the specified list |
| Sunflower seeds | 14% | On the specified list |
| Corn (maize) | 14% | On the specified list |
| Sugar beet | 14% | On the specified list |
| Flax, hemp (industrial) | 14% | On the specified list |
| Raw milk (from farms) | 14% | Agricultural producer supply |
| Live cattle, pigs, poultry | 14% | Agricultural producer supply |
| Wheat, barley, rye | 20% | NOT on the 14% list (standard rate) |
| Processed food products | 20% | Manufacturing, not agriculture |
| Fresh vegetables (domestic market) | 20% | Standard rate (unlike Israel) |
| Meat (processed/retail) | 20% | Standard rate |

**Legislation:** TCU Article 193.1; CMU list of 14% goods

### 10c. Agricultural Input PDV [T1]

- Agricultural producers claim input PDV on standard terms (same as all other businesses)
- No special retention or separate accounting (unlike the former special regime)
- **Legislation:** TCU Article 198 (general rules apply)

---

## Step 11: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., Google Workspace) [T1]

**Situation:** Ukrainian company pays for cloud services from a US company (B2B), no PDV on invoice.
**Resolution:** Reverse charge. Self-assess at 20% in Line 8/8.1. Register self-invoice in YERPN. Deduct in Line 12. Net = zero.
**Legislation:** TCU Article 208

### EC2 -- Export of goods to EU country [T1]

**Situation:** Ukrainian manufacturer exports grain to Germany. Customs declaration obtained.
**Resolution:** Zero-rated under Article 195.1.1. Report in Line 4. No output PDV. Full input PDV refund available.
**Legislation:** TCU Article 195.1.1

### EC3 -- Sale of medicines at 7% [T1]

**Situation:** Pharmaceutical distributor sells registered medicines to a pharmacy, net UAH 500,000.
**Resolution:** Line 2 = UAH 500,000. Line 2.1 = UAH 35,000 (7%).
**Legislation:** TCU Article 193.1

### EC4 -- Purchase of passenger car [T1]

**Situation:** Company purchases a sedan for management use, net UAH 1,000,000, PDV UAH 200,000.
**Resolution:** Input PDV of UAH 200,000 is BLOCKED (Article 198.4). Vehicle capitalized at UAH 1,200,000.
**Legislation:** TCU Article 198.4

### EC5 -- Sale of sunflower seeds at 14% [T1]

**Situation:** Agricultural producer sells sunflower seeds to a processing plant, net UAH 2,000,000.
**Resolution:** Line 3 = UAH 2,000,000. Line 3.1 = UAH 280,000 (14%).
**Legislation:** TCU Article 193.1; 14% rate list

### EC6 -- Tax invoice blocked by SMKOR [T2]

**Situation:** Supplier registers a tax invoice, but it is blocked by the monitoring system.
**Resolution:** Buyer CANNOT claim input PDV until the invoice is unblocked. Supplier must submit explanations and documents to the regional commission. If unblocked, buyer claims input PDV in the period of unblocking. Flag for reviewer: track unblocking process.
**Legislation:** TCU Article 201.16; CMU Resolution No. 1165

### EC7 -- Goods destroyed by shelling [T2]

**Situation:** Warehouse with goods (input PDV previously claimed) is destroyed by Russian military attack.
**Resolution:** Input PDV is NOT reversed under wartime provisions. However, the PDV amount cannot be refunded in cash -- it can only offset future liabilities. Documentation required: act of destruction, military administration confirmation. Flag for reviewer: confirm wartime provision applicability.
**Legislation:** TCU Transitional Provisions; Law No. 2118-IX

### EC8 -- Import of goods from China [T1]

**Situation:** Ukrainian retailer imports electronics from China. Customs declaration shows UAH 3,000,000 value, PDV UAH 600,000.
**Resolution:** Import PDV paid at customs. Deductible in Line 11.1 = UAH 600,000. Also increases SEA PDV registration limit.
**Legislation:** TCU Article 190, 206

### EC9 -- Free supply of goods to Armed Forces [T1]

**Situation:** Company donates supplies (food, equipment) to the Armed Forces of Ukraine free of charge.
**Resolution:** NOT a taxable supply under wartime provisions. No output PDV. Input PDV on the donated goods is NOT reversed. This is a specific wartime exemption.
**Legislation:** TCU Transitional Provisions; Law No. 2120-IX

### EC10 -- Credit notes (rozrakhunok koryguvannia) [T1]

**Situation:** Supplier issues an adjustment calculation (rozrakhunok koryguvannia) to correct a previous tax invoice.
**Resolution:** Adjustment must be registered in YERPN. Buyer must confirm acceptance (for decreases). Affects output/input PDV in the period of registration. Both parties adjust their returns accordingly.
**Legislation:** TCU Article 192

### EC11 -- Services to foreign client (B2B export of services) [T1]

**Situation:** Ukrainian IT company provides software development services to a US client.
**Resolution:** Place of supply is where the recipient is established (US) per Article 186.4. Supply is outside the scope of Ukrainian PDV. No output PDV charged. Input PDV on related costs is deductible.
**Legislation:** TCU Article 186.4

### EC12 -- Residential property rental [T1]

**Situation:** Company rents out apartments to tenants for residential use.
**Resolution:** Exempt under Article 197.1.14. No output PDV. Input PDV on related costs is NOT deductible (Article 198.4).
**Legislation:** TCU Article 197.1.14

### EC13 -- SEA PDV insufficient balance [T1]

**Situation:** Company needs to register a tax invoice for UAH 500,000 PDV but SEA PDV account shows only UAH 300,000 balance.
**Resolution:** Cannot register the invoice. Must either wait for incoming registered tax invoices (which increase the balance) or transfer UAH 200,000 to the SEA PDV Treasury account to top up the balance.
**Legislation:** TCU Article 200-1

---

## Step 12: Reviewer Escalation Protocol

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

## Step 13: Test Suite

### Test 1 -- Standard domestic sale at 20%

**Input:** Ukrainian company sells IT services to a domestic client, net UAH 1,000,000, PDV UAH 200,000.
**Expected output:** Line 1 = UAH 1,000,000. Line 1.1 = UAH 200,000. Output PDV reported.

### Test 2 -- Sale of medicines at 7%

**Input:** Pharmaceutical company sells registered medicines, net UAH 300,000, PDV UAH 21,000.
**Expected output:** Line 2 = UAH 300,000. Line 2.1 = UAH 21,000.

### Test 3 -- Sale of sunflower seeds at 14%

**Input:** Agricultural producer sells sunflower seeds, net UAH 5,000,000, PDV UAH 700,000.
**Expected output:** Line 3 = UAH 5,000,000. Line 3.1 = UAH 700,000.

### Test 4 -- Export of goods, zero-rated

**Input:** Ukrainian manufacturer exports machinery to Poland, net UAH 10,000,000. Customs declaration obtained.
**Expected output:** Line 4 = UAH 10,000,000. No output PDV. Input PDV refundable.

### Test 5 -- Import of services, reverse charge

**Input:** Ukrainian company receives consulting from a UK firm, GBP 20,000 (approx. UAH 1,000,000). No PDV.
**Expected output:** Line 8 = UAH 1,000,000. Line 8.1 = UAH 200,000 (20%). Line 12 = UAH 200,000. Net = zero.

### Test 6 -- Passenger car purchase, blocked

**Input:** Company purchases sedan, net UAH 1,500,000, PDV UAH 300,000.
**Expected output:** Input PDV UAH 300,000 BLOCKED. Vehicle capitalized at UAH 1,800,000.

### Test 7 -- Import of goods

**Input:** Ukrainian retailer imports goods from Turkey. Customs value UAH 2,000,000, import PDV UAH 400,000.
**Expected output:** Line 11.1 = UAH 400,000 (input PDV from customs).

### Test 8 -- Donation to Armed Forces (wartime)

**Input:** Company donates UAH 500,000 worth of food to Armed Forces. Input PDV of UAH 100,000 was claimed.
**Expected output:** No output PDV (wartime exemption). Input PDV of UAH 100,000 is NOT reversed.

---

## PROHIBITIONS [T1]

- NEVER allow input PDV deduction without a registered tax invoice in YERPN
- NEVER allow input PDV deduction on passenger vehicles (unless taxi/rental/emergency)
- NEVER skip reverse charge (self-assessment) for services received from non-residents
- NEVER treat Ukraine as an EU member state -- no intra-community supply rules apply
- NEVER register a tax invoice when SEA PDV balance is insufficient -- top up first
- NEVER confuse zero-rated (Article 195, with input recovery) with exempt (Article 197, without recovery)
- NEVER register import of goods via reverse charge -- Customs handles PDV on imports
- NEVER ignore the 15-day tax invoice registration deadline -- fines are significant
- NEVER apply the 14% rate to goods not on the specific agricultural list
- NEVER assume wartime provisions apply without confirming the specific provision and documentation [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER process transactions involving temporarily occupied territories without qualified tax adviser [T3]

---

## Step 14: Invoice and Documentation Requirements

### 14a. Tax Invoice (Podatkova Nakladna) Detailed Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Format | Electronic only (mandatory since 1 January 2017) |
| Registration | Must be registered in YERPN within 15 calendar days of the tax point |
| Mandatory fields | Supplier name, EDRPOU/RNOCPP, IPN; buyer name, EDRPOU/RNOCPP, IPN; date of supply; date of issuance; sequential number; description of goods/services; unit of measure; quantity; unit price (excluding PDV); PDV rate; PDV amount; total (including PDV) |
| Self-invoice | Required for reverse charge (import of services); supplier field shows non-resident details |
| Copies | Electronic original stored in YERPN; accessible to both parties |
| Correction | Via rozrakhunok koryguvannia (adjustment calculation); must reference original |
| Void | Cancelled invoices must still be registered as "cancelled" in YERPN |

**Legislation:** TCU Article 201; Ministry of Finance Order No. 1307

### 14b. Adjustment Calculation (Rozrakhunok Koryguvannia) [T1]

| Feature | Details |
|---------|---------|
| Purpose | Adjust a previously registered tax invoice (increase or decrease) |
| When required | Returns, price changes, errors, partial cancellation |
| Buyer confirmation | Required for adjustment decreases (buyer must accept in YERPN) |
| Deadline | Within 15 calendar days of the event triggering adjustment |
| Effect | Adjusts output PDV (seller) and input PDV (buyer) in the period of registration |

### 14c. Advance Payment Invoicing [T1]

| Event | Tax Point | Invoice Obligation |
|-------|-----------|-------------------|
| Advance received (before delivery) | Date of receipt | Tax invoice must be registered within 15 days |
| Delivery after advance | Date of delivery | Final tax invoice for remaining amount |
| Full prepayment | Date of receipt | Single tax invoice for full amount |

**Legislation:** TCU Article 187

---

## Step 15: Record-Keeping and Reporting

### 15a. PDV Registers [T1]

| Register | Description | Legal Basis |
|----------|-------------|-------------|
| Register of issued tax invoices | All tax invoices issued (including adjustments) | Art 201.11 |
| Register of received tax invoices | All tax invoices received (including adjustments) | Art 201.11 |
| YERPN register | Central electronic register maintained by DPS | Art 201.10 |
| Annexes to PDV return | Detailed tables (D1-D7) submitted with the monthly return | Ministry of Finance Order |

### 15b. PDV Return Annexes [T1]

| Annex | Content |
|-------|---------|
| D1 | Detailed breakdown of tax invoices issued and received (decryption) |
| D2 | Transactions not subject to PDV or exempt |
| D3 | Adjustment calculations issued |
| D4 | Adjustment calculations received |
| D5 | Decryption of transactions with non-residents |
| D6 | Summary of PDV refund calculations |
| D7 | Not currently in use |

### 15c. Document Retention [T1]

| Document | Retention Period |
|----------|-----------------|
| Tax invoices (in YERPN) | 1,095 days (3 years) from filing deadline |
| Customs declarations | 1,095 days |
| Contracts and agreements | 1,095 days |
| Bank statements | 1,095 days |
| Accounting records | 1,095 days (may be longer per accounting law) |

**Legislation:** TCU Article 44.3

---

## 2026 Changes

| Change | Details | Effective |
|--------|---------|-----------|
| Electric vehicles | PDV exemption on import and sale of electric vehicles expired; standard 20% rate now applies to EVs | 1 January 2026 |
| Energy equipment import exemption | Extended until 1 January 2029; scope expanded to include wind turbines | Extended |
| Martial law provisions | Continue in effect as of April 2026; monitor for any changes | Ongoing |

---

## Contribution Notes

This skill covers Ukrainian PDV as of April 2026. Ukrainian tax law is subject to frequent amendment, particularly during the period of martial law. Wartime provisions are temporary and may be extended, modified, or terminated at any time by the Verkhovna Rada. All rates, thresholds, and wartime provisions should be verified against the most recent legislation and DPS guidance before filing. A qualified Ukrainian tax adviser (podatkovyi konsultant) or auditor must validate all T1 rules before this skill is used in production.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
