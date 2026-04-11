---
name: denmark-vat-return
description: Use this skill whenever asked to prepare, review, or create a Denmark VAT return (Momsangivelse) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in moms", "create the return", "Danish VAT", "momsangivelse", "moms", or any request involving Denmark VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Denmark VAT classification rules, Momsangivelse rubrik mappings, deductibility rules, blocked input tax categories, reverse charge treatment, construction reverse charge, loensumsafgift interaction, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Danish VAT-related work.
---

# Denmark VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Denmark |
| Jurisdiction Code | DK |
| Currency | DKK (Danish Krone) |
| Primary Legislation | Momsloven (Consolidated VAT Act, lovbekendtgoerelse nr. 1021 af 2019, as amended) |
| Supporting Legislation | Momsbekendtgoerelsen (VAT Executive Order); Skattekontrolloven (Tax Control Act); Opkraevningsloven (Collection Act) |
| Payroll Tax on Exempt Activities | Loensumsafgiftsloven (Payroll Tax Act) |
| Tax Authority | Skattestyrelsen (Danish Tax Agency) |
| Filing Portal | https://skat.dk (TastSelv Erhverv) |
| Return Name | Momsangivelse |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Status | awaiting-validation |
| Source Verification | Rates cross-checked against PwC Tax Summaries (taxsummaries.pwc.com/denmark/corporate/other-taxes), April 2026 |
| Confidence Coverage | Tier 1: rubrik assignment, reverse charge, deductibility blocks, filing frequency, registration. Tier 2: partial exemption, voluntary registration, mixed-use apportionment, loensumsafgift. Tier 3: complex group structures, fiscal representation, VAT grouping, cross-border e-commerce OSS. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A statsautoriseret revisor or registreret revisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser and document the gap.

---

## CRITICAL: Denmark Has NO Reduced VAT Rates

**Denmark is UNIQUE in the EU.** Every other EU Member State applies at least one reduced VAT rate. Denmark applies ONLY:

| Rate | Scope | Legislation |
|------|-------|-------------|
| 25% | ALL taxable supplies without exception | momsloven SS33 |
| 0% | Exports, intra-EU B2B supplies of goods, international transport, newspapers/periodicals (from 2024) | momsloven SS34 |

There is no 5%, 7%, 9%, 10%, 12%, 13%, or any other intermediate rate. If a transaction is taxable and not zero-rated, the rate is 25%. Period. This simplifies rate determination but means there are NO reduced-rate boxes on the return.

**Source:** PwC Tax Summaries (April 2026) confirms: "The general VAT rate is 25% of the price charged (exclusive of VAT)." No reduced rates are listed.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and CVR-nummer** [T1] -- 8 digits; DK prefix for EU VIES purposes (format: DK12345678). momsloven SS47(1).
2. **SE-nummer (if different)** [T1] -- Some entities have a separate SE-nummer for VAT; often the same as CVR. momsloven SS47(2).
3. **VAT registration status** [T1] -- Mandatory (turnover > DKK 50,000 in rolling 12 months), voluntary, or non-registered. momsloven SS48-49.
4. **Filing frequency** [T1] -- Monthly (turnover > DKK 50 million), Quarterly (DKK 5 million - 50 million), Half-yearly (< DKK 5 million). momsloven SS57.
5. **Industry/sector** [T2] -- Impacts partial exemption, loensumsafgift, and sector-specific rules. Flag for reviewer.
6. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution (delvis fradragsret) required under momsloven SS38. Reviewer must confirm pro-rata.
7. **Does the business perform construction work (bygge- og anlaegvirksomhed)?** [T1] -- Domestic reverse charge applies. momsloven SS46(1)(3).
8. **Is the business voluntarily registered?** [T2] -- For letting of commercial premises (momsloven SS51), below-threshold registration (momsloven SS49(3)). Reviewer must confirm irrevocability.
9. **Does the business have company cars?** [T1] -- Triggers blocked input tax rules. momsloven SS41-42.
10. **Excess credit brought forward** [T1] -- Denmark refunds excess input VAT automatically. There is NO carry-forward. momsloven SS63(1).

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: VAT Return Form Structure -- Momsangivelse [T1]

**Legislation:** momsloven SS56-57; Skattestyrelsen prescribed form on skat.dk / TastSelv Erhverv.

The Danish Momsangivelse is remarkably simple compared to other EU VAT returns. It consists of three main rubrikker (sections A through C) plus supplementary fields. All filing is electronic via skat.dk TastSelv Erhverv.

### Rubrik A -- Salgsmoms (Output VAT)

| Felt (Field) | Danish Name | Description | What Goes Here |
|---------------|-------------|-------------|----------------|
| A-moms | Salgsmoms | Output VAT on all domestic taxable supplies | Total output VAT at 25% on domestic sales PLUS self-assessed output VAT on reverse charge acquisitions (EU and non-EU) |

**momsloven SS56(1).** This single field captures ALL output VAT. There are no sub-boxes for different rates because Denmark has only one rate (25%).

### Rubrik B -- Koebsmoms (Input VAT)

| Felt (Field) | Danish Name | Description | What Goes Here |
|---------------|-------------|-------------|----------------|
| B-moms | Koebsmoms | Deductible input VAT on purchases | Total deductible input VAT on domestic purchases, imports, and self-assessed reverse charge input VAT, AFTER applying all blocked-category restrictions |

**momsloven SS56(1).** This single field captures ALL deductible input VAT. Blocked categories (momsloven SS42) must be excluded BEFORE entering the figure.

### Rubrik C -- EU-erhvervelser og -leverancer (EU Acquisitions and Supplies)

| Felt (Field) | Danish Name | Description | What Goes Here |
|---------------|-------------|-------------|----------------|
| C-1 | EU-koeb af varer og ydelser | Value of intra-EU acquisitions of goods and services | Net value (excl. VAT) of goods and services acquired from other EU Member States |
| C-2 | EU-salg af varer og ydelser | Value of intra-EU supplies of goods and services | Net value (excl. VAT) of goods and services supplied to other EU Member States (B2B) |

**momsloven SS56(2).** These are VALUE fields only (no VAT amount). The VAT on acquisitions is included in A-moms (output) and B-moms (input).

### Additional Reporting Fields

| Felt (Field) | Danish Name | Description | What Goes Here |
|---------------|-------------|-------------|----------------|
| Eksport | Eksport af varer og ydelser | Value of exports to non-EU | Net value of goods and services exported outside the EU (zero-rated) |
| Import | Import af varer fra ikke-EU | Value of imports from non-EU | Net value of goods imported from outside the EU |

**momsloven SS56(3).**

### Settlement Calculation

| Felt (Field) | Description | Calculation |
|---------------|-------------|-------------|
| Momstilsvar | Net VAT payable or refundable | A-moms minus B-moms |

- **Positive tilsvar:** VAT payable to Skattestyrelsen by the filing deadline.
- **Negative tilsvar:** Excess input VAT automatically refunded to registered bank account. momsloven SS63(1). No application needed. No carry-forward mechanism exists.

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

**Legislation:** momsloven SS3-4 (taxable persons and economic activities).

| Indicator | Classification |
|-----------|---------------|
| Sale of goods or services by the entity | Output / Salgsmoms |
| Purchase of goods or services by the entity | Input / Koebsmoms |
| Salary, wages, AM-bidrag, ATP, A-skat | OUT OF SCOPE -- never on Momsangivelse |
| Loan repayment (principal) | OUT OF SCOPE |
| Dividend payment or receipt | OUT OF SCOPE |
| Share capital transactions | OUT OF SCOPE |
| Income tax payments | OUT OF SCOPE |
| Fines, penalties | OUT OF SCOPE |
| Insurance claim receipts (non-supply) | OUT OF SCOPE |

### 2b. Determine Counterparty Location [T1]

**Legislation:** momsloven SS14-21d (place of supply rules).

| Location | Classification | Notes |
|----------|---------------|-------|
| Denmark | Domestic | Supplier/customer country is DK |
| EU Member State | EU | AT, BE, BG, HR, CY, CZ, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE |
| Greenland | Non-EU / Outside EU VAT | Greenland is NOT part of the EU or EU VAT area, despite being part of the Kingdom of Denmark |
| Faroe Islands | Non-EU / Outside EU VAT | Faroe Islands are NOT part of the EU or EU VAT area, despite being part of the Kingdom of Denmark |
| United Kingdom | Non-EU | Post-Brexit. Treat as third country |
| Norway | Non-EU | EEA but not EU |
| Switzerland | Non-EU | Not EU or EEA |
| All other countries | Non-EU | Third country treatment |

### 2c. Determine VAT Rate [T1]

**Legislation:** momsloven SS33 (standard rate), SS34 (zero-rating), SS13 (exemptions).

**DENMARK VAT RATE LOOKUP TABLE**

| Category | Rate | Legislation | Notes |
|----------|------|-------------|-------|
| ALL taxable goods and services | 25% | momsloven SS33 | The ONLY standard rate. No exceptions. |
| Exports of goods | 0% | momsloven SS34(1)(1) | Must have export documentation |
| Intra-EU B2B supply of goods | 0% | momsloven SS34(1)(2) | Buyer must have valid EU VAT number |
| Intra-EU B2B supply of services (general rule) | 0% (reverse charge) | momsloven SS16(1) | Place of supply shifts to buyer's country |
| International transport of goods | 0% | momsloven SS34(1)(7-8) | |
| International transport of passengers | 0% | momsloven SS34(1)(7) | Domestic passenger transport is EXEMPT, not zero-rated |
| Newspapers and periodicals (print and digital) | 0% | momsloven SS34(1)(18) | Effective from 2024 |
| Repair/maintenance of ships >5 tons | 0% | momsloven SS34(1)(9) | |
| Supply of ships >5 tons for commercial use | 0% | momsloven SS34(1)(6) | |

### 2d. Exempt Supplies (Without Credit) [T1]

**Legislation:** momsloven SS13.

Exempt supplies generate NO output VAT and NO input VAT recovery on related costs.

| Category | Legislation | Notes |
|----------|-------------|-------|
| Hospital and medical care | momsloven SS13(1)(1) | Includes dental, chiropractic, physiotherapy |
| Social services and assistance | momsloven SS13(1)(2) | Elderly care, childcare, etc. |
| Education and vocational training | momsloven SS13(1)(3) | Schools, universities, professional training |
| Financial services | momsloven SS13(1)(11) | Banking, securities, insurance intermediation |
| Insurance and reinsurance | momsloven SS13(1)(10) | All insurance transactions |
| Postal services (universal service) | momsloven SS13(1)(13) | PostNord universal service obligation only |
| Passenger transport | momsloven SS13(1)(15) | Domestic buses, trains, taxis, ferries. NOT international transport. |
| Rental of immovable property (residential) | momsloven SS13(1)(8) | Residential letting. Commercial letting can opt in via voluntary registration (SS51). |
| Cultural activities (certain) | momsloven SS13(1)(6) | Museums, theatres, zoos -- with public funding |
| Gambling and lotteries | momsloven SS13(1)(12) | Subject to separate gambling duty |
| Funeral services | momsloven SS13(1)(14) | |
| Sale of immovable property (existing buildings) | momsloven SS13(1)(9) | New buildings and building plots ARE taxable |
| Sports (non-profit organizations) | momsloven SS13(1)(5) | Commercial gyms/fitness are TAXABLE at 25% |

### 2e. Determine Expense Category [T1]

**Legislation:** momsloven SS43-44 (capital goods scheme / reguleringsforpligtelse).

| Category | Criteria | Adjustment Period | Legislation |
|----------|----------|-------------------|-------------|
| Investeringsgoder -- movable (machinery, equipment) | Acquisition cost > DKK 100,000 excl. VAT | 5 years | momsloven SS43(2)(1) |
| Investeringsgoder -- immovable (buildings, land improvements) | Acquisition or renovation cost > DKK 100,000 excl. VAT | 10 years | momsloven SS43(2)(2) |
| Repair/maintenance of immovable property | Cost > DKK 100,000 excl. VAT | 5 years | momsloven SS43(2)(3) |
| Resale goods | Goods purchased for resale | N/A | momsloven SS37(1) |
| Overhead / services | Everything else | N/A | momsloven SS37(1) |

---

## Step 3: Transaction Classification Matrix -- Lookup Tables [T1]

### TABLE 3A: Purchases -- Domestic (Danish Supplier)

| VAT on Invoice | Category | Rubrik | VAT Treatment | Legislation |
|----------------|----------|--------|---------------|-------------|
| 25% | Overhead / services | B-moms (deductible input VAT) | Full deduction (unless blocked category) | momsloven SS37(1) |
| 25% | Resale goods | B-moms (deductible input VAT) | Full deduction | momsloven SS37(1) |
| 25% | Capital goods (> DKK 100,000) | B-moms (deductible input VAT) | Full deduction; subject to adjustment | momsloven SS43 |
| 25% | Blocked category (see Step 5) | NOT in B-moms | Zero deduction or partial (25% for restaurants) | momsloven SS42 |
| 0% (exempt supply received) | Any | No entry | No input VAT to claim | momsloven SS13 |
| 0% (zero-rated supply) | Any | No entry | No VAT charged, nothing to claim | momsloven SS34 |

### TABLE 3B: Purchases -- EU Supplier (Reverse Charge)

| Type | Reporting Fields | Output Effect | Input Effect | Legislation |
|------|-----------------|---------------|--------------|-------------|
| Goods from EU | C-1 (value) + A-moms (output VAT) + B-moms (input VAT) | Self-assess 25% output | Claim 25% input | momsloven SS11(1)(1), SS46(1)(3) |
| Services from EU (B2B general rule) | C-1 (value) + A-moms (output VAT) + B-moms (input VAT) | Self-assess 25% output | Claim 25% input | momsloven SS16(1), SS46(4) |
| Capital goods from EU (> DKK 100,000) | C-1 (value) + A-moms (output VAT) + B-moms (input VAT) | Self-assess 25% output | Claim 25% input; subject to adjustment | momsloven SS43 |
| Local consumption abroad (hotel, restaurant, taxi) | No entry | None | None -- foreign VAT paid at source is irrecoverable cost | N/A |
| Out-of-scope (wages etc.) | No entry | None | None -- never reverse charge | N/A |

### TABLE 3C: Purchases -- Non-EU Supplier (Reverse Charge / Import)

| Type | Reporting Fields | Output Effect | Input Effect | Legislation |
|------|-----------------|---------------|--------------|-------------|
| Services from non-EU (B2B) | A-moms (output VAT) + B-moms (input VAT) | Self-assess 25% output | Claim 25% input | momsloven SS16(1), SS46(4) |
| Import of goods (customs VAT) | Import field (value) + B-moms (import VAT paid at customs) | VAT assessed by customs | Claim import VAT in B-moms | momsloven SS12, SS37(2)(5) |
| Import of goods (postponed accounting / importmomsordningen) | Import field (value) + A-moms (output) + B-moms (input) | Self-assess 25% output | Claim 25% input | momsloven SS46(6) |
| Local consumption abroad | No entry | None | None | N/A |

### TABLE 3D: Sales -- Domestic

| Transaction | Rubrik | VAT Treatment | Legislation |
|-------------|--------|---------------|-------------|
| Taxable sale of goods | A-moms (output VAT at 25%) | Charge 25% on invoice | momsloven SS33 |
| Taxable sale of services | A-moms (output VAT at 25%) | Charge 25% on invoice | momsloven SS33 |
| Exempt sale | No entry in A-moms | No VAT charged | momsloven SS13 |
| Sale of new building / building plot | A-moms (output VAT at 25%) | Taxable since 2011 | momsloven SS13(1)(9)(b) |

### TABLE 3E: Sales -- EU (B2B)

| Transaction | Rubrik | VAT Treatment | Legislation |
|-------------|--------|---------------|-------------|
| Intra-EU supply of goods (B2B) | C-2 (value, no VAT) | Zero-rated. Buyer reverse charges. | momsloven SS34(1)(2) |
| Intra-EU supply of services (B2B, general rule) | C-2 (value, no VAT) | Place of supply in buyer's country. | momsloven SS16(1) |
| Intra-EU B2C supply of goods (below OSS threshold) | A-moms (output VAT at 25%) | Danish VAT applies | momsloven SS33 |
| Intra-EU B2C supply of goods (above EUR 10,000 OSS threshold) | OSS return (separate) | Register for OSS or in destination country | momsloven SS34(4) [T3] |

### TABLE 3F: Sales -- Non-EU

| Transaction | Rubrik | VAT Treatment | Legislation |
|-------------|--------|---------------|-------------|
| Export of goods | Eksport field (value, no VAT) | Zero-rated with export documentation | momsloven SS34(1)(1) |
| Export of services (B2B) | Eksport field (value, no VAT) | Place of supply outside DK | momsloven SS16(1) |
| Export of services (B2C, general rule) | A-moms (output VAT at 25%) | Place of supply in DK unless specific exception | momsloven SS18 |

---

## Step 4: VAT Rates -- Comprehensive Reference [T1]

### The Single-Rate System

**Denmark is the ONLY EU Member State with no reduced VAT rates.** This is confirmed by PwC Tax Summaries and the European Commission VAT rate database.

**Legislation:** momsloven SS33: "Afgiften udgoor 25 pct. af afgiftsgrundlaget." (The tax amounts to 25% of the taxable base.)

### Comparison: Denmark vs. Other Nordic / EU Countries

| Country | Standard | Reduced 1 | Reduced 2 | Super-Reduced | Zero |
|---------|----------|-----------|-----------|---------------|------|
| **Denmark** | **25%** | **NONE** | **NONE** | **NONE** | **0%** |
| Sweden | 25% | 12% | 6% | -- | 0% |
| Norway (non-EU) | 25% | 15% | 12% | -- | 0% |
| Finland | 25.5% | 14% | 10% | -- | 0% |
| Germany | 19% | 7% | -- | -- | 0% |
| Malta | 18% | 7% | 5% | -- | 0% |

### Zero-Rated Supplies (Full Input VAT Recovery) [T1]

**Legislation:** momsloven SS34.

| Supply | Legislation | Documentation Required |
|--------|-------------|----------------------|
| Export of goods to non-EU | momsloven SS34(1)(1) | Customs export declaration, bill of lading, proof of exit |
| Intra-EU supply of goods (B2B) | momsloven SS34(1)(2) | Buyer's valid EU VAT number (VIES check), transport documentation |
| International transport of goods | momsloven SS34(1)(7-8) | Transport contract, CMR, bill of lading |
| International transport of passengers | momsloven SS34(1)(7) | Ticket/contract showing international route |
| Supply of ships >5 tons (commercial) | momsloven SS34(1)(6) | Ship registration documentation |
| Supply of aircraft for international use | momsloven SS34(1)(10) | Aircraft registration, route documentation |
| Newspapers and periodicals | momsloven SS34(1)(18) | Zero-rated from 2024 (previously 25%) |
| Goods for diplomatic missions | momsloven SS34(1)(13) | Diplomatic exemption certificate |

### Exempt Supplies (NO Input VAT Recovery) [T1]

**Legislation:** momsloven SS13. Full list in Step 2d above.

**KEY CONSEQUENCE:** Businesses making ONLY exempt supplies cannot register for VAT (or if registered, cannot deduct input VAT). Instead, they may be subject to loensumsafgift (payroll tax on exempt activities) -- see Edge Case EC8.

---

## Step 5: Blocked Input Tax (Ikke-Fradragsberettiget Moms) [T1]

**Legislation:** momsloven SS42-45.

### BLOCKED INPUT TAX LOOKUP TABLE

| Category | VAT Recovery | Legislation | Detail |
|----------|-------------|-------------|--------|
| **Restaurationsydelser (restaurant/entertainment)** | **25% deductible ONLY** | **momsloven SS42(2)** | 25% of input VAT on restaurant expenses is deductible. The remaining 75% is blocked. Applies to business meals, client dinners, working lunches. |
| **Hotel / accommodation** | **0% -- BLOCKED** | **momsloven SS42(1)(1)** | No deduction for hotel/accommodation costs. Exception: if accommodation is purchased for resale (e.g., travel agent) or employer-provided housing as part of taxable supply. |
| **Passenger cars -- purchase** | **0% -- BLOCKED** | **momsloven SS42(1)(6)** | No deduction for purchase or lease of passenger cars (personbiler). Exception: taxis, driving schools, car dealers (for resale), leasing companies. |
| **Passenger cars -- running costs (fuel, maintenance, insurance, parking)** | **0% -- BLOCKED** | **momsloven SS42(1)(6)** | Same blocking as the vehicle. Parking MAY be 25% deductible if related to business use -- but this is a [T2] area, flag for reviewer. |
| **Vans and trucks (varebiler/lastbiler) -- purchase** | **100% deductible** | **momsloven SS41(1)** | FULL deduction for vans (max 4 tons total weight) used exclusively for business. Mixed private/business use: see momsloven SS41(2-3). |
| **Vans -- mixed use (gulpladebiler, yellow plates)** | **100% on purchase, own-use charge applies** | **momsloven SS41(2)** | If van is also used privately, business must pay a deemed output VAT (varebilsmoms) calculated per the fixed-rate rules. |
| **Staff canteen / meals** | **Conditional** | **momsloven SS42(3)** | Full deduction ONLY if employer charges employees at least cost price of ingredients. If meals are free or subsidized below cost: BLOCKED. [T2] flag for reviewer. |
| **Gifts to third parties** | **0% -- BLOCKED** | **momsloven SS42(1)(5)** | No deduction. Exception: advertising gifts of small value (markedsfoering) <DKK 100 excl. VAT per item per recipient per year. |
| **Private use of business assets** | **0% -- BLOCKED** | **momsloven SS42(1)(4)** | Must be excluded from input VAT deduction entirely. |
| **Tobacco products** | **0% -- BLOCKED** | **momsloven SS42(1)(8)** | No deduction regardless of business purpose. |

### Restaurant Deduction Calculation [T1]

**momsloven SS42(2): "Virksomheder kan fradrage 25 pct. af afgiften af hotel- og restaurationsydelser."**

Note: Despite the wording referencing "hotel- og restaurationsydelser," in practice the 25% partial deduction applies ONLY to restaurant services (restaurationsydelser). Hotel accommodation remains fully blocked (0%). This is a common source of confusion.

**Example Calculation:**
- Restaurant bill: DKK 4,000 net + DKK 1,000 VAT (25%)
- Deductible VAT: 25% x DKK 1,000 = DKK 250 (goes to B-moms)
- Non-deductible VAT: DKK 750 (added to expense cost)

### Motor Vehicle Rules -- Detail [T1]

**momsloven SS41-42.**

| Vehicle Type | Purchase VAT | Running Cost VAT | Legislation |
|--------------|-------------|-------------------|-------------|
| Passenger car (personbil) -- general business use | BLOCKED | BLOCKED | momsloven SS42(1)(6) |
| Passenger car -- taxi | FULL deduction | FULL deduction | momsloven SS42(7) |
| Passenger car -- driving school (koereskole) | FULL deduction | FULL deduction | momsloven SS42(7) |
| Passenger car -- car dealer (for resale) | FULL deduction | N/A (resale stock) | momsloven SS42(7) |
| Passenger car -- leasing company | FULL deduction | FULL deduction | momsloven SS42(7) |
| Van/truck (varebil/lastbil) -- 100% business use | FULL deduction | FULL deduction | momsloven SS41(1) |
| Van -- mixed use (yellow plates / gulpladebil) | FULL deduction on purchase; own-use output charge | FULL deduction; own-use output charge | momsloven SS41(2) |
| Electric car -- business use | Same rules as petrol/diesel | Same rules | momsloven SS41-42 |
| Motorcycle | BLOCKED (treated as passenger vehicle) | BLOCKED | momsloven SS42(1)(6) |

---

## Step 6: Registration [T1]

### Mandatory Registration

**Legislation:** momsloven SS47-49.

| Requirement | Detail |
|-------------|--------|
| Threshold | DKK 50,000 in taxable turnover within a rolling 12-month period. momsloven SS48(1). |
| Timing | Must register BEFORE making the first taxable supply that causes the threshold to be exceeded. momsloven SS47(1). |
| Format | CVR-nummer: 8-digit number assigned by Erhvervsstyrelsen. For EU VIES purposes: DK + 8 digits (e.g., DK12345678). |
| SE-nummer | Some entities have a separate SE-nummer for VAT filing if they have multiple VAT registrations. Often identical to CVR. |
| Portal | Registration via Virk.dk (business registration) and skat.dk (tax registration). |
| Non-established businesses | Must register if making taxable supplies in Denmark with no fixed establishment. momsloven SS47(2). May appoint a fiscal representative. |

### Voluntary Registration [T2]

**Legislation:** momsloven SS49(3), SS51, SS51a.

| Type | Purpose | Key Rules | Legislation |
|------|---------|-----------|-------------|
| Below-threshold (SS49(3)) | Small business wants to deduct input VAT | Must charge 25% on all sales. Must file returns. | momsloven SS49(3) |
| Commercial letting (SS51) | Landlord charges VAT on commercial rent | Must register each property individually. Residential letting EXCLUDED. Irrevocable for some types. | momsloven SS51 |
| Letting of conference facilities (SS51a) | Conference/meeting room lettings | Separate rules from general letting. | momsloven SS51a |

**Flag for reviewer: Voluntary registration may be irrevocable. Confirm full implications before applying.**

### Deregistration [T1]

**Legislation:** momsloven SS49(1).

- If taxable turnover falls below DKK 50,000 for a consecutive 12-month period, the business MAY (not must) deregister.
- If deregistering, capital goods adjustment rules (momsloven SS43-44) apply to previously claimed input VAT on capital goods still within the adjustment period.

---

## Step 7: Filing Deadlines [T1]

**Legislation:** momsloven SS57; opkraevningsloven SS2.

### Filing Frequency Determination

| Annual Taxable Turnover | Frequency | Legislation |
|------------------------|-----------|-------------|
| > DKK 50,000,000 | Monthly (maanedlig) | momsloven SS57(2) |
| DKK 5,000,001 - 50,000,000 | Quarterly (kvartalsvis) | momsloven SS57(3) |
| <= DKK 5,000,000 | Half-yearly (halvaarsvis) | momsloven SS57(4) |

### Monthly Filing Deadlines (turnover > DKK 50M)

| Period | Filing and Payment Deadline |
|--------|-----------------------------|
| January | 25 March |
| February | 25 April |
| March | 25 May |
| April | 25 June |
| May | 25 July |
| June | 25 August |
| July | 25 September |
| August | 25 October |
| September | 25 November |
| October | 25 December |
| November | 25 January |
| December | 25 February |

**Rule:** 25th of the month following the reporting month. momsloven SS57(2).

### Quarterly Filing Deadlines (turnover DKK 5M - 50M)

| Period | Filing and Payment Deadline |
|--------|-----------------------------|
| Q1: January - March | 1 June |
| Q2: April - June | 1 September |
| Q3: July - September | 1 December |
| Q4: October - December | 1 March (following year) |

**Rule:** 1st of the month, approximately 2 months after quarter-end. momsloven SS57(3). Note these are NOT the 25th.

### Half-Yearly Filing Deadlines (turnover < DKK 5M)

| Period | Filing and Payment Deadline |
|--------|-----------------------------|
| H1: January - June | 1 September |
| H2: July - December | 1 March (following year) |

**Rule:** 1st of the month, approximately 2 months after half-year-end. momsloven SS57(4).

### Weekend / Holiday Rule

If a deadline falls on a Saturday, Sunday, or Danish public holiday (helligdag), the deadline moves to the next business day (hverdag). opkraevningsloven SS2(3).

### Late Filing: Renter og Tillaeg (Interest and Surcharges) [T1]

**Legislation:** opkraevningsloven SS5-8.

| Consequence | Detail | Legislation |
|-------------|--------|-------------|
| Late payment interest (renter) | 0.7% per commenced month of delay (may change annually) | opkraevningsloven SS7(1) |
| Late filing surcharge (tillaeg) | DKK 65 per day the return is late, up to a maximum. Minimum DKK 800. | opkraevningsloven SS5(1) |
| Estimated assessment (foreloebig fastsaettelse) | If no return filed, Skattestyrelsen estimates the VAT payable. The business must still file. | opkraevningsloven SS4 |
| Repeated non-compliance | May result in shortened filing periods (forced monthly filing) or revocation of registration. | momsloven SS62 |

### Supplementary Reporting Deadlines

| Report | Frequency | Deadline | Legislation |
|--------|-----------|----------|-------------|
| EU Sales List (Listesystem) | Quarterly (same as VAT period or quarterly for monthly filers) | 25th of month after quarter-end | momsloven SS54 |
| Intrastat (arrivals/dispatches) | Monthly (if above Intrastat threshold) | 10th of following month | EU Regulation 2019/2152 |

---

## Step 8: Reverse Charge Rules [T1]

### 8a. Intra-EU Acquisitions of Goods [T1]

**Legislation:** momsloven SS11(1)(1), SS46(1)(3).

1. Supplier invoices at 0% with reference to intra-EU supply.
2. Danish buyer self-assesses output VAT at 25% -- include in **A-moms**.
3. Danish buyer claims input VAT at 25% -- include in **B-moms** (if fully taxable).
4. Report acquisition value (excl. VAT) in **C-1**.
5. **Net VAT effect: zero** for fully taxable businesses.

### 8b. Intra-EU Acquisitions of Services (B2B General Rule) [T1]

**Legislation:** momsloven SS16(1), SS46(4).

1. EU supplier invoices without VAT (place of supply is buyer's country).
2. Danish buyer self-assesses output VAT at 25% -- include in **A-moms**.
3. Danish buyer claims input VAT at 25% -- include in **B-moms** (if fully taxable).
4. Report acquisition value in **C-1**.
5. **Net VAT effect: zero** for fully taxable businesses.

### 8c. Import of Services from Non-EU (B2B) [T1]

**Legislation:** momsloven SS16(1), SS46(4).

1. Non-EU supplier invoices without VAT.
2. Danish buyer self-assesses output VAT at 25% -- include in **A-moms**.
3. Danish buyer claims input VAT at 25% -- include in **B-moms** (if fully taxable).
4. **Net VAT effect: zero** for fully taxable businesses.
5. Note: No entry in C-1 (that is EU only). May report in Import field.

### 8d. Import of Goods from Non-EU [T1]

**Legislation:** momsloven SS12, SS46(6).

**Option 1 -- Standard Import (VAT paid at customs):**
1. VAT assessed and paid at customs clearance.
2. Import VAT receipt (toldkvittering) issued.
3. Claim import VAT in **B-moms** as input.
4. Report import value in **Import** field.

**Option 2 -- Postponed Accounting (Importmomsordningen):**
1. If approved for postponed import VAT accounting.
2. Self-assess output VAT at 25% in **A-moms**.
3. Claim input VAT at 25% in **B-moms**.
4. Report import value in **Import** field.
5. **Net VAT effect: zero** -- improves cash flow.

### 8e. Domestic Reverse Charge -- Construction (Bygge- og Anlaeg) [T1]

**Legislation:** momsloven SS46(1)(3).

**IMPORTANT:** Denmark applies DOMESTIC reverse charge for construction services (bygge- og anlaegvirksomhed). This is unusual and a major compliance trap.

| Condition | Treatment |
|-----------|-----------|
| Subcontractor provides construction services to a VAT-registered main contractor | REVERSE CHARGE. Subcontractor invoices without VAT. Main contractor self-assesses. |
| Construction company sells directly to end consumer (B2C) | Normal VAT. Charge 25%. |
| Construction company sells to non-VAT-registered business | Normal VAT. Charge 25%. |
| Supply of building materials only (no installation) | Normal VAT. NOT reverse charge. |
| Supply includes both materials and installation | Reverse charge applies to the ENTIRE supply (composite supply). |

**Buyer (main contractor):**
1. Self-assess 25% output VAT in **A-moms**.
2. Claim 25% input VAT in **B-moms**.
3. Net effect: zero.

**Seller (subcontractor):**
1. Invoice WITHOUT VAT.
2. State on invoice: "Omvendt betalingspligt, jf. momsloven SS46, stk. 1, nr. 3" (Reverse charge pursuant to momsloven SS46(1)(3)).
3. No output VAT entry.

### 8f. Domestic Reverse Charge -- Non-Established Suppliers [T1]

**Legislation:** momsloven SS46(1)(2).

When a non-established business (no fixed establishment in Denmark) supplies goods or services to a Danish VAT-registered buyer:
1. Buyer self-assesses output VAT at 25% in **A-moms**.
2. Buyer claims input VAT at 25% in **B-moms**.
3. Net effect: zero.

### 8g. Sales to EU (B2B) [T1]

| Transaction | Rubrik | VAT | Legislation |
|-------------|--------|-----|-------------|
| Intra-EU supply of goods (B2B) | C-2 | None (zero-rated) | momsloven SS34(1)(2) |
| Intra-EU supply of services (B2B, general rule) | C-2 | None (reverse charge by buyer) | momsloven SS16(1) |

Must report on EU Sales List (Listesystem). momsloven SS54.

### 8h. Sales to Non-EU [T1]

| Transaction | Rubrik | VAT | Legislation |
|-------------|--------|-----|-------------|
| Export of goods | Eksport | None (zero-rated) | momsloven SS34(1)(1) |
| Export of services (B2B) | Eksport | None (place of supply outside DK) | momsloven SS16(1) |

---

## Step 9: Partial Exemption (Delvis Fradragsret) [T2]

**Legislation:** momsloven SS38.

If a business makes BOTH taxable and exempt supplies, input VAT on shared costs (faellesomkostninger) must be apportioned.

### Calculation Method [T2]

```
Fradragsprocent (Recovery %) = (Taxable Turnover / Total Turnover) x 100
```

- Round UP to the nearest whole percentage.
- Total Turnover = Taxable Turnover + Exempt Turnover.
- Financial income that is ancillary to the main business is excluded from the denominator. momsloven SS38(2).
- Directly attributable costs: fully deductible if related to taxable supplies; fully blocked if related to exempt supplies. momsloven SS37(1).
- Shared costs only: apply the pro-rata percentage. momsloven SS38(1).

**Annual adjustment required.** The pro-rata rate used during the year is provisional. An annual adjustment (regulering) must be made in the final period return. momsloven SS38(4).

**Flag for reviewer: Pro-rata calculation and annual adjustment must be confirmed by statsautoriseret/registreret revisor.**

---

## Step 10: Edge Case Registry

### EC1 -- No Reduced Rate Trap [T1]

**Situation:** A client asks what VAT rate to apply to food, children's clothing, books, or any product that carries a reduced rate in other EU countries.
**Resolution:** Denmark has NO reduced rates. ALL goods and services are taxed at 25% unless zero-rated or exempt. Food is 25%. Children's clothing is 25%. Books are 25%. Hairdressing is 25%. There are no exceptions.
**Legislation:** momsloven SS33. Denmark has never implemented any reduced rate under the EU VAT Directive's optional provisions.

### EC2 -- Greenland and Faroe Islands [T1]

**Situation:** Danish company sells goods or services to a customer in Greenland or the Faroe Islands.
**Resolution:** Greenland and the Faroe Islands are NOT part of the EU and NOT part of the EU VAT area, despite being part of the Kingdom of Denmark. Treat as EXPORT (non-EU). Report in Eksport field. Zero-rated with export documentation. Do NOT report in C-2 (that is EU only).
**Legislation:** momsloven SS34(1)(1). Treaty on the Functioning of the EU, Article 355(1) (Greenland excluded); Protocol No. 2 (Faroe Islands excluded).
**Additional note:** Greenland has no VAT. The Faroe Islands have their own VSP (virdisoekjuskattur) system, not momsloven.

### EC3 -- Construction Reverse Charge (Byggemoms) [T1]

**Situation:** A plumbing company (subcontractor) invoices a general contractor for installation work on a building site.
**Resolution:** DOMESTIC reverse charge applies. The plumber invoices WITHOUT VAT and states "Omvendt betalingspligt, jf. momsloven SS46, stk. 1, nr. 3" on the invoice. The general contractor self-assesses 25% in A-moms and claims in B-moms.
**Legislation:** momsloven SS46(1)(3).
**Common error:** If the plumber charges 25% VAT on the invoice despite reverse charge applying, the general contractor should request a corrected invoice. The incorrectly charged VAT is NOT deductible.

### EC4 -- Company Car (Personbil) [T1]

**Situation:** Company buys a passenger car for DKK 400,000 + DKK 100,000 VAT for the managing director.
**Resolution:** Input VAT BLOCKED. No deduction. Full DKK 500,000 is cost. The car is a personbil. Unless the company is a taxi firm, driving school, car dealer (resale), or leasing company, zero input VAT recovery.
**Legislation:** momsloven SS42(1)(6).
**Additional:** The employee may be subject to benefit-in-kind taxation (fri bil) under ligningsloven SS16(4) -- but that is income tax, not VAT.

### EC5 -- Van with Yellow Plates (Gulpladebil) [T1]

**Situation:** Company purchases a van (varebil, max 4 tons) with yellow plates for DKK 200,000 + DKK 50,000 VAT. The van is used 80% for business, 20% privately by an employee.
**Resolution:** FULL input VAT deduction (DKK 50,000) in B-moms. However, because the van is also used privately, the company must account for output VAT on the private use (varebilsmoms) according to the fixed-rate scheme in momsloven SS41(2). The deemed output VAT is calculated based on a fixed percentage of the purchase price and included in A-moms.
**Legislation:** momsloven SS41(1-3).
**Flag for reviewer [T2]:** Confirm the private use percentage and calculate the varebilsmoms amount.

### EC6 -- Business Dinner (Restaurationsmoms) [T1]

**Situation:** Managing director takes clients to dinner. Restaurant bill: DKK 3,000 + DKK 750 VAT (25%).
**Resolution:** 25% of input VAT is deductible. Deductible VAT = 25% x DKK 750 = DKK 187.50, entered in B-moms. Non-deductible VAT = DKK 562.50, added to expense cost.
**Legislation:** momsloven SS42(2).

### EC7 -- Hotel in Denmark [T1]

**Situation:** Employee stays at a Danish hotel for a business trip. DKK 1,500 + DKK 375 VAT (25%).
**Resolution:** Input VAT BLOCKED for accommodation. DKK 375 is NOT deductible. Full DKK 1,875 is cost.
**Legislation:** momsloven SS42(1)(1).
**Common confusion:** momsloven SS42(2) mentions "hotel- og restaurationsydelser" but the 25% partial deduction applies only to restaurant/catering services, NOT to the accommodation portion of a hotel stay.

### EC8 -- Loensumsafgift (Payroll Tax on Exempt Activities) [T2]

**Situation:** A financial services company makes only exempt supplies (momsloven SS13(1)(11)). It cannot register for VAT and cannot deduct input VAT. It asks about its payroll tax obligations.
**Resolution:** Businesses making exempt supplies under momsloven SS13 are typically liable for loensumsafgift (payroll tax) under loensumsafgiftsloven. This is a TAX ON THE WAGE BILL, not a VAT. It effectively replaces the VAT burden for exempt-supply businesses.
**Legislation:** loensumsafgiftsloven SS1.
**Rates (vary by sector):**
- Financial sector (method 2): 15.3% of payroll (2026 rate, may change).
- Other exempt activities (method 4): varies.
**Flag for reviewer [T2]:** Loensumsafgift calculation and filing is a separate obligation. This skill does not compute it. Escalate to adviser for loensumsafgift filing.

### EC9 -- SaaS Subscription from US Provider [T1]

**Situation:** Danish company subscribes to a US SaaS platform. Monthly fee USD 500, no VAT on invoice.
**Resolution:** Import of services from non-EU. Self-assess 25% output VAT in A-moms. Claim 25% input VAT in B-moms (if fully taxable). Net effect: zero. No C-1 entry (non-EU). May report in Import field.
**Legislation:** momsloven SS16(1), SS46(4).

### EC10 -- Excess Input VAT / Automatic Refund [T1]

**Situation:** Company has DKK 80,000 input VAT and DKK 30,000 output VAT for the period.
**Resolution:** Negative tilsvar of DKK 50,000 (B-moms > A-moms). Skattestyrelsen automatically refunds the excess to the registered NemKonto bank account. No application required. No carry-forward. The refund is typically processed within 3 weeks after the filing deadline.
**Legislation:** momsloven SS63(1).
**Note:** If Skattestyrelsen suspects fraud or errors, they may withhold the refund pending review (momsloven SS63(2)).

### EC11 -- Sale of New Building [T1]

**Situation:** Construction company builds and sells a new apartment building.
**Resolution:** Sale of NEW buildings (and building plots) has been TAXABLE at 25% since 1 January 2011. This is an exception to the general exemption for real property sales. "New" means first supply within 5 years of completion.
**Legislation:** momsloven SS13(1)(9)(b), SS13(1)(9)(a).
**Note:** Sale of EXISTING buildings (older than 5 years, previously occupied) remains EXEMPT under momsloven SS13(1)(9)(a). [T2] if the building's age is uncertain.

### EC12 -- EU B2B Service Sale (Consulting to Sweden) [T1]

**Situation:** Danish company provides management consulting to a Swedish client (B2B, Swedish company has SE VAT number).
**Resolution:** Place of supply is Sweden (buyer's country) under the general B2B rule. Danish company invoices without VAT. Report in C-2. Swedish company applies reverse charge in Sweden. Danish company must report on EU Sales List.
**Legislation:** momsloven SS16(1), SS54.

### EC13 -- Faroe Islands Import [T1]

**Situation:** Danish company imports seafood from a Faroese supplier.
**Resolution:** The Faroe Islands are outside the EU. This is an IMPORT from a third country. Import VAT (25%) is assessed at Danish customs. Claim import VAT in B-moms. Report value in Import field. This is NOT an intra-EU acquisition (no C-1 entry).
**Legislation:** momsloven SS12.

### EC14 -- Mixed-Use Property (Voluntary Registration) [T2]

**Situation:** Landlord owns a building with 3 commercial units and 2 residential units. Wants to register for VAT on the commercial letting.
**Resolution:** Can voluntarily register under momsloven SS51 for the COMMERCIAL units only. Must register each unit/property individually. Can deduct input VAT on costs directly attributable to commercial units. Costs shared between commercial and residential units must be apportioned (delvis fradragsret). Residential units remain exempt.
**Legislation:** momsloven SS51, SS38.
**Flag for reviewer:** Confirm apportionment method (floor area, rental income, etc.).

### EC15 -- Electronic Services B2C to EU Consumer (OSS) [T3]

**Situation:** Danish company sells digital services (e.g., streaming, e-books) to private consumers in other EU countries. Total B2C EU sales exceed EUR 10,000.
**Resolution:** Must either register for VAT in each destination country OR register for the One-Stop-Shop (OSS) scheme. OSS return is filed separately from the Momsangivelse. Danish VAT does not apply -- destination country's VAT rate applies.
**Legislation:** momsloven SS34(4), EU VAT Directive Article 58.
**Escalate [T3]:** OSS filing is outside the scope of this skill.

---

## Step 11: Comparison with Malta VAT System

| Feature | Denmark (DK) | Malta (MT) |
|---------|-------------|------------|
| **Standard rate** | 25% (momsloven SS33) | 18% (Cap. 406, 1st Schedule) |
| **Reduced rates** | NONE -- unique in EU | 7%, 5% (5th Schedule) |
| **Super-reduced rate** | NONE | NONE |
| **Zero rate** | 0% (exports, intra-EU, newspapers) | 0% (exports, intra-EU, food, pharma) |
| **Return form** | Momsangivelse (3 rubrikker + supplementary) | VAT3 (45+ boxes) |
| **Form complexity** | Very simple -- few fields | Complex -- many boxes and sub-boxes |
| **Filing portal** | skat.dk / TastSelv Erhverv | cfr.gov.mt / VAT Online |
| **Registration threshold** | DKK 50,000 (~EUR 6,700) | EUR 35,000 (Article 11 exemption) |
| **Registration format** | DK + 8 digits (CVR) | MT + 8 digits |
| **Filing frequency** | Monthly / Quarterly / Half-yearly | Quarterly (Art. 10) / Annual (Art. 11) / Monthly (Art. 12) |
| **Monthly filer threshold** | > DKK 50,000,000 turnover | Article 12 (intra-EU acquisitions) |
| **Quarterly filer threshold** | DKK 5M - 50M turnover | Article 10 (standard) |
| **Small business filing** | Half-yearly (< DKK 5M) | Annual (Article 11, < EUR 35,000) |
| **Excess input VAT** | Automatic refund, no carry-forward | Carried forward or refund on application |
| **Capital goods threshold** | DKK 100,000 excl. VAT (~EUR 13,400) | EUR 1,160 gross |
| **Capital goods adjustment -- movable** | 5 years | 5 years |
| **Capital goods adjustment -- immovable** | 10 years | 20 years |
| **Restaurant/entertainment VAT** | 25% deductible (momsloven SS42(2)) | 0% deductible (10th Schedule) |
| **Hotel VAT** | 0% deductible (BLOCKED) | 0% deductible (BLOCKED) |
| **Motor vehicle VAT** | BLOCKED for passenger cars; vans OK | BLOCKED (10th Schedule, except taxi etc.) |
| **Construction reverse charge** | YES (domestic, subcontractor to contractor) | NO domestic reverse charge for construction |
| **Payroll tax on exempt activities** | YES -- loensumsafgift | NO equivalent |
| **Territories outside EU VAT** | Greenland, Faroe Islands | N/A (Malta is fully within EU VAT) |
| **Currency** | DKK | EUR |
| **Late filing penalty** | DKK 65/day + interest 0.7%/month | Administrative penalties + interest |
| **Derived box calculations** | Minimal (A minus B = tilsvar) | Extensive (Box 5, 8, 12, 16, 17, 22, 25, 26, 33, 39, 42, 43, 45) |

### Key Differences for Practitioners

1. **Rate simplicity:** Denmark's single 25% rate eliminates rate-classification errors entirely. Malta's three positive rates (18%, 7%, 5%) require careful classification.
2. **Form simplicity:** Denmark's Momsangivelse has ~6 fields. Malta's VAT3 has 45+ boxes with complex derived calculations. Denmark trades transparency for simplicity.
3. **Refund mechanism:** Denmark automatically refunds excess input VAT. Malta carries forward or requires a refund application.
4. **Restaurant deduction:** Denmark uniquely allows 25% of restaurant VAT to be deducted. Malta blocks entertainment entirely.
5. **Construction:** Denmark's domestic reverse charge for construction is a major compliance obligation with no Malta equivalent.
6. **Loensumsafgift:** Denmark imposes a payroll tax on exempt-supply businesses. Malta has no equivalent.
7. **Territorial exceptions:** Denmark must account for Greenland and Faroe Islands being outside the EU VAT area. Malta has no such territorial complexity.

---

## Step 12: Test Suite

### Test 1 -- Standard Domestic Purchase [T1]

**Input:** Danish supplier, office supplies, DKK 10,000 net + DKK 2,500 VAT (25%). Fully taxable VAT-registered business.
**Expected:** B-moms += DKK 2,500. Fully deductible overhead.
**Legislation:** momsloven SS37(1).

### Test 2 -- Import of Services from US (SaaS) [T1]

**Input:** US supplier, monthly SaaS fee DKK 2,000 net, no VAT on invoice. Fully taxable VAT-registered business.
**Expected:** A-moms += DKK 500 (25% self-assessed output). B-moms += DKK 500 (25% input). Net effect = zero. No C-1 entry (non-EU).
**Legislation:** momsloven SS16(1), SS46(4).

### Test 3 -- Intra-EU Goods Acquisition [T1]

**Input:** German supplier, raw materials EUR 10,000 (~DKK 75,000) at 0% with DE VAT number. Fully taxable.
**Expected:** A-moms += DKK 18,750 (25% self-assessed output). B-moms += DKK 18,750 (25% input). C-1 += DKK 75,000. Net = zero.
**Legislation:** momsloven SS11(1)(1), SS46(1)(3).

### Test 4 -- Passenger Car Purchase (BLOCKED) [T1]

**Input:** Passenger car DKK 300,000 + DKK 75,000 VAT. General business use (not taxi/driving school).
**Expected:** B-moms += DKK 0. BLOCKED. Full DKK 375,000 is cost. No input VAT recovery.
**Legislation:** momsloven SS42(1)(6).

### Test 5 -- Restaurant Dinner with Clients (25% Rule) [T1]

**Input:** Restaurant bill DKK 2,000 + DKK 500 VAT (25%). Business entertainment.
**Expected:** B-moms += DKK 125 (25% of DKK 500). Remaining DKK 375 VAT is non-deductible cost.
**Legislation:** momsloven SS42(2).

### Test 6 -- Hotel in Denmark (BLOCKED) [T1]

**Input:** Hotel stay DKK 1,200 + DKK 300 VAT (25%). Business trip.
**Expected:** B-moms += DKK 0. BLOCKED. Full DKK 1,500 is cost.
**Legislation:** momsloven SS42(1)(1).

### Test 7 -- Export of Goods to US [T1]

**Input:** Danish company exports goods to US client, DKK 200,000. Export documentation available.
**Expected:** Eksport += DKK 200,000. A-moms += DKK 0 (zero-rated). No output VAT.
**Legislation:** momsloven SS34(1)(1).

### Test 8 -- EU B2B Service Sale to Sweden [T1]

**Input:** Danish company invoices Swedish client for consulting, DKK 50,000. Swedish client has SE VAT number (B2B).
**Expected:** C-2 += DKK 50,000. A-moms += DKK 0 (no Danish output VAT). Must report on EU Sales List.
**Legislation:** momsloven SS16(1), SS54.

### Test 9 -- Excess Input VAT Refund [T1]

**Input:** Period totals: A-moms = DKK 40,000. B-moms = DKK 65,000.
**Expected:** Momstilsvar = -DKK 25,000. Automatically refunded to NemKonto. No carry-forward.
**Legislation:** momsloven SS63(1).

### Test 10 -- Construction Reverse Charge (Subcontractor) [T1]

**Input:** Plumbing subcontractor invoices general contractor DKK 80,000 for installation work on building site. No VAT on invoice (reverse charge stated).
**Expected (General Contractor):** A-moms += DKK 20,000 (25% self-assessed output). B-moms += DKK 20,000 (25% input). Net = zero.
**Expected (Subcontractor):** No A-moms entry. Invoice states "Omvendt betalingspligt, jf. momsloven SS46, stk. 1, nr. 3."
**Legislation:** momsloven SS46(1)(3).

### Test 11 -- Van Purchase (Gulpladebil, Mixed Use) [T2]

**Input:** Van (varebil, yellow plates) DKK 250,000 + DKK 62,500 VAT. Used 70% business, 30% private by employee.
**Expected:** B-moms += DKK 62,500 (FULL deduction on purchase). However, company must calculate and declare varebilsmoms (deemed output VAT on private use) in A-moms for each period. Flag for reviewer to compute varebilsmoms amount.
**Legislation:** momsloven SS41(1-3).

### Test 12 -- Sale to Greenland [T1]

**Input:** Danish company sells machinery to Greenland customer, DKK 150,000.
**Expected:** Eksport += DKK 150,000 (treated as export to non-EU). A-moms += DKK 0 (zero-rated). NOT reported in C-2 (Greenland is not EU).
**Legislation:** momsloven SS34(1)(1).

### Test 13 -- Hotel in EU Country (Italy) [T1]

**Input:** Employee stays at Italian hotel. Invoice EUR 200 including Italian VAT EUR 20 (10%).
**Expected:** No Danish VAT entries. No reverse charge. Italian VAT is irrecoverable cost. Full EUR 200 is expense.
**Legislation:** Local consumption exception. Place of supply is Italy.

### Test 14 -- Partial Exemption Business (Mixed Supplies) [T2]

**Input:** Business makes 60% taxable supplies and 40% exempt supplies (financial services). Shared overhead expense DKK 10,000 + DKK 2,500 VAT.
**Expected:** Fradragsprocent = 60% (rounded up if not whole). Deductible VAT = 60% x DKK 2,500 = DKK 1,500 in B-moms. Non-deductible = DKK 1,000 added to cost. Flag for reviewer to confirm pro-rata rate and annual adjustment.
**Legislation:** momsloven SS38(1).

---

## PROHIBITIONS [T1]

1. **NEVER apply any reduced VAT rate in Denmark.** There are NONE. Only 25% and 0% exist. If you are tempted to apply 5%, 7%, 10%, 12%, or any other rate -- STOP. Denmark does not have it. momsloven SS33.
2. **NEVER let AI guess rubrik assignment.** It is 100% deterministic from transaction facts using the lookup tables in Step 3.
3. **NEVER claim input VAT on passenger car purchase, lease, or running costs** unless the business is a taxi firm, driving school, car dealer (resale), or leasing company. momsloven SS42(1)(6).
4. **NEVER claim more than 25% of input VAT on restaurant expenses.** The 75% block is absolute. momsloven SS42(2).
5. **NEVER claim input VAT on hotel/accommodation costs** unless purchased for resale by a travel agent or similar. momsloven SS42(1)(1).
6. **NEVER carry forward excess input VAT.** Denmark refunds automatically. There is no carry-forward mechanism. momsloven SS63(1).
7. **NEVER apply reverse charge to out-of-scope categories** (wages, dividends, loan repayments, bank charges, etc.).
8. **NEVER apply reverse charge to local consumption services abroad** (hotel in another country, restaurant abroad, taxi abroad). Foreign VAT paid at source is an irrecoverable cost.
9. **NEVER treat Greenland or Faroe Islands as EU.** They are outside the EU VAT area. Treat as third-country (export/import).
10. **NEVER allow a non-registered entity to claim input VAT.** Registration is a prerequisite for any deduction. momsloven SS37(1).
11. **NEVER charge VAT on a construction subcontractor invoice** when domestic reverse charge applies. The subcontractor must invoice WITHOUT VAT. momsloven SS46(1)(3).
12. **NEVER confuse zero-rated (full input VAT recovery) with exempt (no input VAT recovery).** Zero-rated supplies allow full deduction of related input VAT. Exempt supplies do not. momsloven SS34 vs. SS13.
13. **NEVER compute any number.** All arithmetic is handled by the deterministic engine, not the AI. The AI classifies; the engine calculates.
14. **NEVER apply a quarterly deadline of the 25th.** Quarterly deadlines are the 1st of the month (1 June, 1 September, 1 December, 1 March). Only monthly filers use the 25th. momsloven SS57.
15. **NEVER confuse loensumsafgift with moms.** Loensumsafgift is a payroll tax on exempt activities, not a transaction tax. It is a separate filing obligation under a separate law. loensumsafgiftsloven SS1.

---

## Step 13: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Statsautoriseret/registreret revisor must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified adviser. Document gap.
```

---

## Step 14: Loensumsafgift Reference (Payroll Tax on Exempt Activities) [T2]

**Legislation:** loensumsafgiftsloven (Consolidated Act).

This section is REFERENCE ONLY. This skill does not compute or file loensumsafgift. It is included because businesses making exempt supplies must understand the interaction.

### What Is Loensumsafgift?

Loensumsafgift is a tax levied on the wage bill (loensum) of businesses that make VAT-exempt supplies. It exists because exempt businesses do not charge VAT and thus do not contribute to the VAT system. Loensumsafgift ensures they bear a comparable tax burden.

### Who Pays?

| Business Type | Liable? | Method |
|---------------|---------|--------|
| Financial services (banks, insurance, investment) | YES | Method 2: percentage of payroll |
| Healthcare (private clinics, dentists) | YES | Method 4 |
| Education (private schools, training companies) | YES | Method 4 |
| Postal services (universal service) | YES | Method 4 |
| Passenger transport | YES | Method 4 |
| Fully taxable businesses | NO | Not liable -- pays VAT instead |
| Mixed (taxable + exempt) | PARTIAL | Only on payroll attributable to exempt activities |

### Rates (2026, subject to change)

| Method | Basis | Rate |
|--------|-------|------|
| Method 1 | Payroll + profit | 3.54% |
| Method 2 (financial sector) | Payroll | 15.3% |
| Method 3 | Payroll + 90% of profit | 3.54% |
| Method 4 (most exempt businesses) | Payroll | 6.37% |

**Filing:** Quarterly or annually, depending on size. Filed via skat.dk / TastSelv.

**[T2] -- Always escalate loensumsafgift to qualified adviser. This skill does not cover filing.**

---

## Step 15: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | DKK 50,000 annual taxable turnover | momsloven SS48(1) |
| Monthly filing | Turnover > DKK 50,000,000 | momsloven SS57(2) |
| Quarterly filing | Turnover DKK 5,000,001 - 50,000,000 | momsloven SS57(3) |
| Half-yearly filing | Turnover <= DKK 5,000,000 | momsloven SS57(4) |
| Capital goods -- movable | > DKK 100,000 excl. VAT (5-year adjustment) | momsloven SS43(2)(1) |
| Capital goods -- immovable | > DKK 100,000 excl. VAT (10-year adjustment) | momsloven SS43(2)(2) |
| Capital goods -- immovable repair | > DKK 100,000 excl. VAT (5-year adjustment) | momsloven SS43(2)(3) |
| Restaurant VAT deduction | 25% of input VAT only | momsloven SS42(2) |
| Advertising gifts | < DKK 100 excl. VAT per item/recipient/year | momsloven SS42(1)(5) |
| EU distance selling (B2C OSS) | EUR 10,000 (EU-wide threshold) | momsloven SS34(4) |
| Automatic VAT refund | All excess input VAT refunded -- no carry-forward | momsloven SS63(1) |
| Late filing surcharge | DKK 65 per day, minimum DKK 800 | opkraevningsloven SS5(1) |
| Late payment interest | 0.7% per commenced month | opkraevningsloven SS7(1) |

---

## Contribution Notes

This skill was generated based on publicly available information about Denmark's VAT system as of April 2026. Denmark's distinctive features include:

1. **The single 25% rate** with absolutely no reduced rates (unique in the EU).
2. **The extremely simple Momsangivelse** with only a few rubrikker (compared to Malta's 45+ box VAT3).
3. **The 25% restaurant deduction rule** (momsloven SS42(2)) -- partial deduction rather than full block.
4. **Automatic refund of excess input VAT** with no carry-forward mechanism.
5. **Domestic reverse charge for construction** (bygge- og anlaeg) -- a significant compliance obligation.
6. **Loensumsafgift** -- payroll tax on exempt activities, with no equivalent in Malta.
7. **Greenland and Faroe Islands** outside the EU VAT area despite being part of the Kingdom of Denmark.
8. **Half-yearly filing** for small businesses (turnover < DKK 5M).
9. **Van (gulpladebil) rules** with full deduction but deemed output VAT on private use.
10. **No carry-forward** -- negative tilsvar is always refunded.

VAT rates cross-checked against PwC Tax Summaries (taxsummaries.pwc.com/denmark/corporate/other-taxes), April 2026: confirmed 25% standard rate, no reduced rates.

**This skill requires validation by a qualified Danish statsautoriseret revisor or registreret revisor before use in production.**

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
