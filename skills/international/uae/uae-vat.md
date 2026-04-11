---
name: uae-vat
description: Use this skill whenever asked to prepare, review, or create a UAE VAT return (VAT201 form) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT201", "create the return", "UAE VAT filing", or any request involving UAE VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete UAE VAT classification rules, box mappings, input tax recovery rules, reverse charge treatment, designated zone rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any UAE VAT-related work.
---

# UAE VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Arab Emirates |
| Jurisdiction Code | AE |
| Primary Legislation | Federal Decree-Law No. 8 of 2017 on Value Added Tax (VAT Decree-Law) |
| Supporting Legislation | Cabinet Decision No. 52 of 2017 (Executive Regulation); Federal Decree-Law No. 7 of 2017 on Tax Procedures; Cabinet Decision No. 40 of 2017 (Designated Zones); Cabinet Decision No. 49 of 2021 (Penalties, superseded by Cabinet Decision No. 129 of 2025 from 14 April 2026) |
| Tax Authority | Federal Tax Authority (FTA), United Arab Emirates |
| Filing Portal | https://eservices.tax.gov.ae (FTA e-Services Portal) |
| VAT Introduction Date | 1 January 2018 |
| Standard Rate | 5% |
| Currency | AED (United Arab Emirates Dirham) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: box assignment, reverse charge, input tax blocks, derived calculations. Tier 2: partial apportionment, designated zone classification, sector-specific zero-rating conditions. Tier 3: complex group structures, profit margin scheme, multi-jurisdictional supplies. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified tax agent or registered tax advisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax advisor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TRN** [T1] -- 15-digit Tax Registration Number (format: numeric, e.g., 100123456789012). The TRN must appear on all tax invoices, returns, and official VAT correspondence.
2. **Legal form** [T1] -- LLC, sole establishment, branch, free zone entity, etc.
3. **VAT registration date** [T1] -- when the entity became VAT-registered.
4. **Tax period** [T1] -- quarterly or monthly (as assigned by FTA). Registrants cannot choose their own period without FTA approval.
5. **Industry/sector** [T2] -- impacts zero-rating eligibility (healthcare, education, real estate).
6. **Does the business make exempt supplies?** [T2] -- If yes, input tax apportionment required.
7. **Is the business in a Designated Zone?** [T2] -- Impacts goods treatment significantly. Designated Zones are treated as being outside the UAE for VAT purposes, but only for goods transactions (Art. 51, VAT Decree-Law).
8. **Does the business import goods?** [T1] -- Customs documentation required.
9. **Does the business receive services from non-resident suppliers?** [T1] -- Reverse charge required.
10. **Carried forward excess input tax from prior period?** [T1] -- Needed for net position. Note: from 1 January 2026, a five-year limitation applies to excess input VAT refunds.

**If items 1-4 are unknown, STOP. Do not classify any transactions until registration details and period are confirmed.**

### Territorial Scope [T1]

- VAT applies throughout all seven Emirates: Abu Dhabi, Dubai, Sharjah, Ajman, Umm Al Quwain (UAQ), Ras Al Khaimah (RAK), and Fujairah.
- The UAE is a member of the Gulf Cooperation Council (GCC). The GCC VAT Framework Agreement provides for mutual recognition, but as of 2026, only Saudi Arabia, Bahrain, and Oman have implemented VAT alongside the UAE. Kuwait and Qatar have not yet implemented.
- **Legislation:** VAT Decree-Law Art. 1 (definitions), Art. 2 (scope), Art. 51 (Designated Zones).

### Currency [T1]

All amounts on the VAT201 form are reported in **United Arab Emirates Dirhams (AED)**. Foreign currency transactions must be converted to AED at the exchange rate published by the UAE Central Bank on the date of supply.

**Legislation:** Executive Regulation Art. 69.

---

## Step 1: Transaction Classification Rules

### 1.1 Classification Framework [T1]

Every transaction must be classified into one of four categories:

| Category | VAT Rate | Output VAT | Input Tax Recovery | Box |
|----------|----------|------------|-------------------|-----|
| Standard Rated | 5% | Yes, 5% | Yes | Box 1 (sales), Box 9 (purchases) |
| Zero-Rated | 0% | No (0%) | Yes | Box 4 (sales) |
| Exempt | N/A | No | No | Box 5 (sales) |
| Out of Scope | N/A | No | No | Not reported |

### 1.2 Determining Transaction Type [T1]

- **Supply of goods:** Transfer of ownership or the right to dispose of goods (Art. 2, VAT Decree-Law).
- **Supply of services:** Any supply that is not a supply of goods (Art. 3, VAT Decree-Law).
- **Deemed supply:** Goods/services used for non-business purposes; disposal of assets without consideration (Art. 6-7, VAT Decree-Law). Free samples/gifts exceeding AED 500 per recipient per year trigger deemed supply treatment.
- **Out of scope:** Salaries/wages, government fees, fines, dividends, loan repayments, bank interest (non-financial-services), personal transfers.

**Legislation:** VAT Decree-Law Art. 1-7; Executive Regulation Art. 1-5.

### 1.3 Place of Supply Rules [T1]

| Transaction Type | Place of Supply | Reference |
|-----------------|----------------|-----------|
| Goods without transport | Where goods are at time of supply | Art. 27 |
| Goods with transport | Where transport starts | Art. 27 |
| Goods assembled/installed | Where assembly/installation takes place | Art. 28 |
| Water/energy via network | Where delivered | Art. 28 |
| Services (general rule) | Where supplier has place of residence | Art. 29 |
| Services (B2B override) | Where recipient has place of residence | Art. 30 |
| Real estate services | Where real estate is located | Art. 31 |
| Transport services | Where transport starts | Art. 32 |
| Telecommunications | Where SIM was issued / where received | Art. 33 |
| Electronic services (B2C) | Where customer resides | Art. 34 |

**Legislation:** VAT Decree-Law Art. 27-34; Executive Regulation Art. 14-21.

### 1.4 Date of Supply (Tax Point) [T1]

The date of supply determines in which tax period the supply must be reported:

| Event | Date of Supply | Reference |
|-------|---------------|-----------|
| Goods supplied without installation | Earlier of: removal date or date made available | Art. 25(1) |
| Goods with installation | Date installation/assembly completed | Art. 25(2) |
| Services | Date services performed or completed | Art. 25(3) |
| Payment received before supply | Date payment received (partial or full) | Art. 25(4) |
| Tax invoice issued before supply | Date of invoice | Art. 25(5) |
| Periodic supplies (continuous) | Earlier of: invoice date or payment due date | Art. 25(6) |

**The earliest of the above triggers applies.**

**Legislation:** VAT Decree-Law Art. 25-26; Executive Regulation Art. 11-13.

### 1.5 Supply Classification Lookup Table [T1]

| Supply Description | Category | Rate | Sales Box | Legislation |
|-------------------|----------|------|-----------|-------------|
| Sale of goods within UAE | Standard | 5% | Box 1 | Art. 2, 5 |
| Provision of services within UAE | Standard | 5% | Box 1 | Art. 3, 5 |
| Export of goods outside UAE | Zero-rated | 0% | Box 4 | Art. 45(1) |
| Export of services outside UAE | Zero-rated | 0% | Box 4 | Art. 31(1)(a) |
| International passenger transport | Zero-rated | 0% | Box 4 | Art. 45(2) |
| International freight transport | Zero-rated | 0% | Box 4 | Art. 45(2) |
| Supply of aircraft/vessel for international transport | Zero-rated | 0% | Box 4 | Art. 45(3) |
| First sale of residential property (<3 years) | Zero-rated | 0% | Box 4 | Art. 45(4) |
| Qualifying education services | Zero-rated | 0% | Box 4 | Art. 45(5) |
| Qualifying healthcare services | Zero-rated | 0% | Box 4 | Art. 45(6) |
| Investment precious metals (99%+ purity) | Zero-rated | 0% | Box 4 | Art. 45(7) |
| Crude oil and natural gas | Zero-rated | 0% | Box 4 | Art. 45(8) |
| Financial services (interest/margin-based) | Exempt | N/A | Box 5 | Art. 46(1) |
| Residential property (resale/lease after first supply) | Exempt | N/A | Box 5 | Art. 46(2) |
| Bare land | Exempt | N/A | Box 5 | Art. 46(3) |
| Local passenger transport | Exempt | N/A | Box 5 | Art. 46(4) |
| Life insurance and reinsurance | Exempt | N/A | Box 5 | Art. 46(5) |
| Salary payment | Out of scope | N/A | None | N/A |
| Dividend payment | Out of scope | N/A | None | N/A |
| Government fine/penalty | Out of scope | N/A | None | N/A |
| Loan repayment (principal) | Out of scope | N/A | None | N/A |
| Transfer of business as going concern | Out of scope | N/A | None | Art. 7(2) |

### 1.6 Purchases Classification Lookup Table [T1]

| Purchase Description | Category | Input Tax | Purchase Box | Legislation |
|---------------------|----------|-----------|-------------|-------------|
| Domestic purchase from VAT-registered supplier | Standard | Recoverable | Box 9 | Art. 54 |
| Import of goods via customs | Import | Recoverable | Box 6 | Art. 47-49 |
| Purchase from non-resident supplier (reverse charge) | Reverse charge | Recoverable (input side) | Box 3 / Box 10 | Art. 48 |
| Purchase related to exempt supplies | Mixed | Not recoverable (apportionment) | Box 9 | Art. 55 |
| Blocked expense (entertainment) | Blocked | Not recoverable | Box 9 (no tax recovery) | Art. 53 |
| Salary expense | Out of scope | N/A | Not reported | N/A |

### 1.7 Zero-Rated Supply Conditions [T1/T2]

#### Exports of Goods (Art. 45(1)) [T1]
- Direct export: goods physically leave the UAE within 90 days of supply.
- Indirect export: overseas customer arranges transport; goods leave UAE within 90 days.
- Evidence required: customs export declaration, bill of lading/airway bill, proof of delivery outside UAE.
- **Legislation:** Executive Regulation Art. 30.

#### International Transport (Art. 45(2)) [T1]
- Transport of passengers and goods that starts or ends outside the UAE, or crosses the UAE as part of an international journey.
- Includes ancillary services directly connected to international transport.
- **Legislation:** Executive Regulation Art. 31.

#### Means of Transport for International Use (Art. 45(3)) [T1]
- Supply, lease, repair, maintenance, and conversion of aircraft and vessels used for international transport.
- Supply of goods and services for use on board such aircraft or vessels.
- **Legislation:** Executive Regulation Art. 32.

#### First Supply of Residential Property (Art. 45(4)) [T2]
- First supply of a residential building within **3 years of completion**.
- "First supply" includes first sale or first lease.
- The building must be designed or adapted for residential use.
- **After 3 years from completion, subsequent supplies are exempt (not zero-rated).**
- Mixed-use properties: [T2] flag for reviewer -- apportionment may be required between residential and commercial portions.
- **Legislation:** Executive Regulation Art. 33; VAT Public Clarification VATP002.

#### Education Services (Art. 45(5)) [T2]
- Education services and related goods/services supplied by educational institutions recognized by the competent government authority.
- Must be included in a curriculum recognized by the federal or emirate-level education authority.
- Pre-school, school education, and higher education qualify.
- **Conditions:** The institution must be licensed/recognized. Private tutoring outside recognized institutions is standard rated. [T2] flag if institution recognition status is unclear.
- **Legislation:** Executive Regulation Art. 34.

#### Healthcare Services (Art. 45(6)) [T2]
- Preventive and basic healthcare services as defined by the relevant health authority.
- Supply of related goods and services directly connected to healthcare treatment.
- **Conditions:** Must be provided by a licensed healthcare provider. Cosmetic/elective procedures are standard rated unless medically necessary. [T2] flag if procedure classification is unclear.
- **Legislation:** Executive Regulation Art. 35.

#### Investment Precious Metals (Art. 45(7)) [T1]
- Gold, silver, and platinum of **99% purity or higher** (or as specified).
- Must be investment-grade (tradeable on global markets).
- Jewellery and manufactured gold items are **standard rated** (not zero-rated).
- **Legislation:** Executive Regulation Art. 36.

#### Crude Oil and Natural Gas (Art. 45(8)) [T1]
- Supply and import of crude oil and natural gas.
- Refined petroleum products (petrol, diesel) are **standard rated**.
- **Legislation:** Executive Regulation Art. 37.

### 1.8 Exempt Supply Rules [T1/T2]

Exempt supplies are not subject to VAT. No output VAT is charged, and **input tax on costs related to exempt supplies is NOT recoverable**.

#### Financial Services (Art. 46(1)) [T2]
- **Exempt:** Interest on loans, credit cards, finance leases (margin-based, interest-based financial services).
- **Standard rated:** Explicit fee-based financial services (e.g., advisory fees, arrangement fees, brokerage commissions, fund management fees).
- The distinction between margin-based (exempt) and fee-based (standard rated) financial services is critical. [T2] flag when classification is ambiguous.
- **Legislation:** Executive Regulation Art. 38; VAT Public Clarification VATP011.

#### Residential Property -- Subsequent Supply/Lease (Art. 46(2)) [T1]
- Sale of residential property more than 3 years after completion.
- Lease of residential property.
- **Commercial property is always standard rated** (sale or lease).
- **Legislation:** Executive Regulation Art. 39; VAT Public Clarification VATP002.

#### Bare Land (Art. 46(3)) [T1]
- Supply of bare (undeveloped) land.
- Land with any building or civil engineering works is NOT bare land.
- **Legislation:** Executive Regulation Art. 40.

#### Local Passenger Transport (Art. 46(4)) [T1]
- Transport of passengers by any means within the UAE.
- Includes taxis, buses, metro, tram within the UAE.
- Does NOT include limousine/luxury car hire (standard rated).
- **Legislation:** Executive Regulation Art. 41.

#### Life Insurance (Art. 46(5)) [T1]
- Life insurance policies and reinsurance of life insurance.
- General insurance (property, motor, health, travel) is **standard rated**.
- **Legislation:** Executive Regulation Art. 42.

---

## Step 2: Box/Line Assignment

### VAT201 Form Structure [T1]

The UAE VAT return is filed on **Form VAT201** via the FTA e-Services portal at https://eservices.tax.gov.ae. Filed **exclusively online** -- no paper filing accepted. A Tax Registration Number (TRN) is required for access.

**Legislation:** Tax Procedures Law Art. 28; Executive Regulation Art. 59.

### Deterministic Box Assignment Table [T1]

| Box | Label | What Goes Here | Amount Column | VAT Column | Adjustment Column |
|-----|-------|---------------|---------------|------------|-------------------|
| **1** | Standard Rated Supplies | All domestic sales at 5%, broken down by Emirate (1a-1g) | Net value (AED) | 5% of net | If applicable |
| **2** | Tax Refunds Provided to Tourists | VAT refunded under Tourist Refund Scheme (Planet/Fintrax) | Refund amount | -- | -- |
| **3** | Supplies Subject to Reverse Charge (Purchases) | Value of taxable supplies received from non-resident suppliers | Net value | 5% VAT | -- |
| **4** | Zero-Rated Supplies | All zero-rated sales (exports, international transport, first residential, healthcare, education, precious metals, crude oil/gas) | Net value | AED 0 | -- |
| **5** | Exempt Supplies | All exempt sales (margin-based financial services, residential lease/resale, bare land, local transport, life insurance) | Net value | -- | -- |
| **6** | Goods Imported into the UAE | Value of goods imported through customs (including from Designated Zones to mainland) | Net value | 5% VAT | -- |
| **7** | Adjustments to Output Tax | Credit notes, corrections, bad debt relief, capital asset adjustments | +/- amount | -- | -- |
| **8** | Total Output Tax Due | **Calculated:** VAT on Box 1 + Box 2 + VAT on Box 3 + VAT on Box 6 + Box 7 | -- | Total | -- |
| **9** | Standard Rated Expenses | All domestic purchases at 5% from UAE-registered suppliers | Net value | 5% VAT | -- |
| **10** | Reverse Charge Input Tax | VAT recoverable on reverse charge supplies from Box 3 | -- | VAT amount | -- |
| **11** | Total Recoverable Input Tax | **Calculated:** VAT on Box 9 + Box 10 - blocked input tax adjustments | -- | Total | -- |

### Box 1 Emirate-Level Breakdown [T1]

| Sub-Box | Emirate | Amount (AED) | VAT Amount (AED) | Adjustment (AED) |
|---------|---------|-------------|-------------------|-------------------|
| 1a | Abu Dhabi | Net value | 5% of net | If applicable |
| 1b | Dubai | Net value | 5% of net | If applicable |
| 1c | Sharjah | Net value | 5% of net | If applicable |
| 1d | Ajman | Net value | 5% of net | If applicable |
| 1e | Umm Al Quwain | Net value | 5% of net | If applicable |
| 1f | Ras Al Khaimah | Net value | 5% of net | If applicable |
| 1g | Fujairah | Net value | 5% of net | If applicable |

**Rules for Emirate allocation:**
- Supplies of goods: Emirate where the goods are delivered or made available to the customer.
- Supplies of services: Emirate where the supplier's place of business (or fixed establishment providing the service) is located.
- If a supplier has establishments in multiple Emirates, allocate to the Emirate of the establishment most directly concerned with the supply.

**Legislation:** VAT Decree-Law Art. 29-31 (place of supply); Executive Regulation Art. 14-19.

### Populating the VAT201 Form [T1]

1. **Box 1:** Sum all standard rated sales by Emirate.
2. **Box 2:** Enter tourist refund amounts (from approved operator reports).
3. **Box 3:** Sum all reverse charge supplies received from non-residents.
4. **Box 4:** Sum all zero-rated sales.
5. **Box 5:** Sum all exempt sales.
6. **Box 6:** Sum all imported goods values.
7. **Box 7:** Enter any adjustments (credit notes, corrections, bad debt relief).
8. **Box 8:** Calculate total output tax.
9. **Box 9:** Sum all standard rated purchases.
10. **Box 10:** Enter reverse charge input tax from Box 3.
11. **Box 11:** Calculate total recoverable input tax (after blocked items and apportionment).

### Validation Checks [T1]

1. Cross-check: Box 8 (output) minus Box 11 (input) = Net VAT payable or refundable.
2. Verify Emirate-level breakdown in Box 1 sums to total standard rated supplies.
3. Verify reverse charge entries appear on both output (Box 3) and input (Box 10) sides.
4. Confirm no blocked input tax has been included in Box 11.
5. Submit via FTA e-Services portal before the 28th of the month following period end.
6. Make payment before the same deadline.

---

## Step 3: Reverse Charge Mechanics

### 3.1 When Reverse Charge Applies (Art. 48, VAT Decree-Law) [T1]

The reverse charge applies when a **UAE-registered taxable person** receives:

1. **Services from a non-resident supplier** who does not have a place of residence in the UAE and is not registered for UAE VAT.
2. **Goods from a non-resident supplier** where the goods are located in the UAE at the time of supply.
3. **Concerned Goods** as specified by Cabinet Decision (e.g., hydrocarbons between registrants).

### 3.2 Reverse Charge Step-by-Step [T1]

```
Step 1: Identify supply from non-resident supplier (goods or services).
Step 2: Determine the value of supply (contract value, excluding any foreign VAT).
Step 3: Self-assess output VAT at 5% on the value of supply.
Step 4: Report in Box 3 (value) and include 5% VAT in output tax.
Step 5: If entitled to input tax recovery, report the same VAT in Box 10.
Step 6: Net effect for fully taxable business = zero.
```

**Note (effective 1 January 2026):** Taxpayers are no longer required to issue a tax invoice to themselves for imports under the reverse charge mechanism.

### 3.3 Reverse Charge -- Import of Goods [T1]

| Import Method | Treatment | Reference |
|--------------|-----------|-----------|
| Via Customs (standard) | VAT paid at customs border (or deferred under customs scheme) | Art. 47 |
| Customs deferment scheme | VAT accounted for via VAT return (Box 6) | Art. 48 |
| From Designated Zone to mainland | Treated as import; VAT due via return (Box 6) | Art. 51 |

**Legislation:** VAT Decree-Law Art. 47-49; Executive Regulation Art. 39-42.

### 3.4 Reverse Charge -- Services from Non-Resident [T1]

| Scenario | Reverse Charge Applies? | Box |
|----------|------------------------|-----|
| Non-resident supplier, services consumed in UAE | Yes | Box 3 / Box 10 |
| Non-resident supplier registered for UAE VAT | No (supplier charges VAT) | Box 9 |
| GCC supplier (from implementing state) | Depends on GCC mutual agreement status | [T2] flag |
| Out-of-scope categories (wages, dividends) | NEVER | Not reported |

**Legislation:** VAT Decree-Law Art. 48; Executive Regulation Art. 33.

### 3.5 Concerned Goods (Art. 48(2)) [T1]

Certain categories of goods are subject to reverse charge when supplied between VAT-registered persons within the UAE:

- Crude oil and refined petroleum products.
- Hydrocarbons.
- Natural gas.

The recipient (buyer) accounts for the VAT rather than the supplier.

**Legislation:** VAT Decree-Law Art. 48(2); Cabinet Decision No. 25 of 2018.

---

## Step 4: Deductibility Check

### 4.1 General Right to Recover (Art. 54, VAT Decree-Law) [T1]

A taxable person may recover input tax incurred on goods and services used, or intended to be used, for making **taxable supplies** (standard rated or zero-rated).

**Conditions for recovery:**
1. The person must be a VAT-registered taxable person.
2. The goods/services must be used for making taxable supplies.
3. A valid tax invoice must be held.
4. The input tax must not fall into a blocked category.

**Legislation:** VAT Decree-Law Art. 54; Executive Regulation Art. 43-46.

### 4.2 Blocked Input Tax (Art. 53, Executive Regulation) [T1]

The following categories of input tax are **NOT recoverable** regardless of business purpose:

| Blocked Category | Description | Reference |
|-----------------|-------------|-----------|
| Entertainment | Entertainment, hospitality, and recreation services for non-business purposes | Exec. Reg. Art. 53(1)(a) |
| Motor vehicles | Purchase, hire, or lease of motor vehicles (unless used for taxable supply as stock-in-trade, or the vehicle is specifically designed for the business purpose) | Exec. Reg. Art. 53(1)(b) |
| Employee personal benefits | Goods/services provided for personal benefit of employees (not required by law and not a deemed supply) | Exec. Reg. Art. 53(1)(c) |

#### Entertainment Block Details [T1]
- Hospitality of any kind provided to anyone other than employees.
- Client entertainment (meals, events, gifts).
- **Exception:** Entertainment provided to employees as part of employment (e.g., staff meals in the workplace) is NOT blocked.
- **Legislation:** Executive Regulation Art. 53(1)(a).

#### Motor Vehicle Block Details [T1]
- Purchase, rental, or lease of motor vehicles.
- Running costs (fuel, maintenance, insurance) for blocked vehicles are also blocked.
- **Exceptions where recovery IS allowed:**
  - Vehicle is stock-in-trade (e.g., car dealership).
  - Vehicle is used for licensed taxi services.
  - Vehicle is used for a rental business (renting vehicles is the business activity).
  - Vehicle is designed and used exclusively for business transport of goods (e.g., delivery van with no passenger seats).
  - Emergency vehicles for licensed operators.
- [T2] flag if client claims vehicle is purely for business -- reviewer must confirm before allowing recovery.
- **Legislation:** Executive Regulation Art. 53(1)(b).

#### Employee Personal Benefits Block [T1]
- Gym memberships, personal phone plans, personal accommodation (unless required by law or a condition of employment).
- **Exception:** Benefits required by UAE labour law (e.g., end-of-service gratuity provisions do not apply here as they are cash, not goods/services).
- **Legislation:** Executive Regulation Art. 53(1)(c).

### 4.3 Input Tax Recovery Summary Table [T1]

| Expense Type | Taxable Business | Partially Exempt Business | Fully Exempt Business |
|-------------|-----------------|--------------------------|----------------------|
| Standard rated purchase (general) | Recoverable | Apportioned | Not recoverable |
| Standard rated purchase (blocked category) | NOT recoverable | NOT recoverable | NOT recoverable |
| Zero-rated purchase | No VAT to recover | No VAT to recover | No VAT to recover |
| Reverse charge (from Box 3/10) | Recoverable | Apportioned | Not recoverable |
| Import VAT (from Box 6) | Recoverable | Apportioned | Not recoverable |

### 4.4 Apportionment for Mixed Supplies (Art. 55-56, VAT Decree-Law) [T2]

If a taxable person makes both **taxable and exempt supplies**, input tax must be apportioned. Only the portion relating to taxable supplies is recoverable.

**Standard apportionment method:**
```
Recoverable input tax = Total input tax x (Value of taxable supplies / Total value of all supplies)
```

**Rules:**
1. Input tax directly attributable to taxable supplies: fully recoverable.
2. Input tax directly attributable to exempt supplies: NOT recoverable.
3. Residual input tax (overheads): apportioned using the formula above.
4. An annual adjustment is required at the end of each tax year.

**Special methods:** The FTA may approve alternative apportionment methods if the standard method does not produce a fair result.

**[T2] flag: The apportionment calculation and method must be confirmed by a qualified tax advisor before filing.**

**Legislation:** VAT Decree-Law Art. 55-56; Executive Regulation Art. 47-49.

### 4.5 Capital Assets Scheme (Art. 57, VAT Decree-Law) [T2]

For capital assets exceeding **AED 5,000,000** (buildings/land) or other capital assets with a useful life exceeding **5 years**:

- Input tax recovery is adjusted over a period of:
  - **10 years** for real estate/buildings.
  - **5 years** for other capital assets.
- An annual adjustment is made if the proportion of taxable use changes.
- The adjustment period starts from the tax period in which the asset was acquired.

**[T2] flag: Capital asset adjustments are complex. Reviewer must confirm the calculation.**

**Legislation:** VAT Decree-Law Art. 57; Executive Regulation Art. 50.

### 4.6 Five-Year Limitation on Excess Input Tax Refunds [T1]

Effective **1 January 2026**, a five-year limitation applies to claims for excess input VAT refunds or offsets. Taxpayers have a one-year transition period for pre-existing claims. If the excess is neither used to offset VAT liabilities nor the subject of a refund request within five years from the end of the tax period in which the excess arose, the right to recover the excess lapses.

**Legislation:** Amendment to Federal Decree-Law No. 7 of 2017 (Tax Procedures Law).

---

## Step 5: Derived Calculations

### 5.1 Net Tax Calculation [T1]

```
Net VAT Payable = Box 8 (Total Output Tax) - Box 11 (Total Recoverable Input Tax)

IF Net VAT Payable > 0:
    Tax is payable to FTA by the due date.
IF Net VAT Payable < 0:
    Excess input tax may be:
    (a) Carried forward to offset against future output tax; OR
    (b) Refunded by the FTA upon application.
    Note: Five-year limitation applies from 1 January 2026.
```

**Legislation:** VAT Decree-Law Art. 55 (net tax); Tax Procedures Law Art. 29 (refunds).

### 5.2 Box 8 -- Total Output Tax Due [T1]

```
Box 8 = VAT on Box 1 (total across all Emirates) + Box 2 + VAT on Box 3 + VAT on Box 6 + Box 7
```

### 5.3 Box 11 -- Total Recoverable Input Tax [T1]

```
Box 11 = VAT on Box 9 + Box 10 - any blocked input tax adjustments
```

---

## Step 6: Key Thresholds

### 6.1 Registration Thresholds [T1]

| Registration Type | Threshold (AED) | Threshold (approx. USD) | Condition |
|------------------|-----------------|------------------------|-----------|
| Mandatory | 375,000 | ~102,000 | Past 12 months or next 30 days |
| Voluntary | 187,500 | ~51,000 | Past 12 months or next 30 days |
| Non-resident | No threshold | N/A | Any taxable supply in UAE |
| Tax Group | 375,000 (combined) | ~102,000 | Combined group taxable supplies |

**Legislation:** VAT Decree-Law Art. 13, 17; Executive Regulation Art. 6-7.

### 6.2 Other Key Thresholds [T1]

| Threshold | Amount | Purpose | Reference |
|-----------|--------|---------|-----------|
| Voluntary Disclosure trigger | AED 10,000 (tax difference) | If error exceeds AED 10,000, Voluntary Disclosure is mandatory; if AED 10,000 or less, adjust in next return | Tax Procedures Law Art. 30 |
| Simplified Tax Invoice limit | AED 10,000 (inclusive of VAT) | Supplies not exceeding this may use simplified invoice | Exec. Reg. Art. 59(6) |
| Free samples/gifts threshold | AED 500 per recipient per year | Below = no deemed supply; above = deemed supply, 5% output VAT due on cost | Art. 6; Exec. Reg. Art. 5 |
| Capital Assets Scheme | AED 5,000,000 (buildings/land) | Triggers multi-year input tax adjustment (10 years for buildings, 5 years for other assets) | Art. 57; Exec. Reg. Art. 50 |
| Tax period assignment | AED 150,000,000 annual turnover | Below = quarterly; at or above = monthly (FTA discretion) | Art. 59-60; Exec. Reg. Art. 55 |

### 6.3 Deregistration [T1]

- **Mandatory deregistration:** The person ceases to make taxable supplies.
- **Voluntary deregistration:** Taxable supplies in the past 12 months fell below AED 187,500 (and was not mandatorily registered based on exceeding AED 375,000 threshold).
- The FTA must be notified within 20 business days of cessation.

**Legislation:** VAT Decree-Law Art. 21-22; Executive Regulation Art. 9-10.

### 6.4 VAT Grouping (Art. 18, VAT Decree-Law) [T2]

Two or more taxable persons may apply to form a **Tax Group** if:
- Each is a legal person.
- They are related parties (common control or direction).
- One or more members are established in the UAE.

**Effects:**
- The group is treated as a single taxable person with one TRN.
- Intra-group supplies are disregarded for VAT.
- The representative member files the return and is liable for group VAT obligations.

**[T2] flag: VAT grouping has significant implications. Reviewer must confirm eligibility and impact.**

**Legislation:** VAT Decree-Law Art. 18; Executive Regulation Art. 8.

---

## Step 7: Filing Deadlines

### 7.1 Tax Periods [T1]

| Registrant Type | Standard Period | Frequency |
|----------------|----------------|-----------|
| Default (annual turnover < AED 150 million) | Quarterly | 4 returns per year |
| Assigned by FTA (annual turnover >= AED 150 million) | Monthly | 12 returns per year |
| As specified by FTA | Custom | As determined |

Tax periods are assigned by the FTA upon registration. Registrants cannot choose their own period without FTA approval.

**Legislation:** VAT Decree-Law Art. 59-60; Executive Regulation Art. 55.

### 7.2 Filing and Payment Deadline [T1]

- **Filing deadline:** 28th day of the month following the end of the tax period.
- **Payment deadline:** Same day -- 28th day of the month following the end of the tax period.
- Both the return and the payment must be submitted/completed by this date.
- If the 28th falls on a weekend or public holiday, the deadline moves to the next working day.

| Quarter | Period | Filing/Payment Due |
|---------|--------|-------------------|
| Q1 | 1 Jan -- 31 Mar | 28 April |
| Q2 | 1 Apr -- 30 Jun | 28 July |
| Q3 | 1 Jul -- 30 Sep | 28 October |
| Q4 | 1 Oct -- 31 Dec | 28 January (next year) |

**Legislation:** Tax Procedures Law Art. 28-29.

### 7.3 Penalties Framework [T1]

The penalty regime was updated by **Cabinet Decision No. 49 of 2021** (effective 28 June 2021) and further revised by **Cabinet Decision No. 129 of 2025** (effective 14 April 2026).

#### Late Filing Penalties [T1]

| Offence | Penalty |
|---------|---------|
| Late filing -- first offence | AED 1,000 |
| Late filing -- repeat offence (within 24 months) | AED 2,000 |

**Legislation:** Cabinet Decision No. 49 of 2021, Table 1; Cabinet Decision No. 129 of 2025.

#### Late Payment Penalties [T1]

**Prior to 14 April 2026 (Cabinet Decision No. 49 of 2021):**

| Timing | Penalty |
|--------|---------|
| Immediately upon late payment | 2% of unpaid tax |
| 7 days after due date | Additional 4% of unpaid tax |
| After 7 days: monthly penalty | 1% per month on outstanding balance |
| Maximum cumulative late payment penalty | 300% of the unpaid tax |

**From 14 April 2026 (Cabinet Decision No. 129 of 2025):**

| Timing | Penalty |
|--------|---------|
| Late payment | 14% per annum, calculated monthly from the day after the due date until payment is made |

**Legislation:** Cabinet Decision No. 49 of 2021, Table 1, Item 11; Cabinet Decision No. 129 of 2025.

#### Other Key Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Failure to register | AED 20,000 |
| Failure to display TRN | AED 20,000 |
| Failure to notify FTA of amendments to tax return | AED 1,000 (first), AED 2,000 (repeat) |
| Failure to submit Voluntary Disclosure | Fixed penalty + percentage of tax difference |
| Failure to issue tax invoice | AED 5,000 per invoice |
| Failure to issue tax credit note | AED 5,000 per credit note |
| Failure to keep records | AED 10,000 (first), AED 50,000 (repeat) |
| Filing incorrect return | Fixed penalty + percentage of tax underpaid |
| Tax evasion | Criminal prosecution, imprisonment, and/or fines up to 5x the evaded tax |

**Legislation:** Cabinet Decision No. 49 of 2021; Cabinet Decision No. 129 of 2025; Tax Procedures Law Art. 42-48.

### 7.4 Voluntary Disclosure [T1]

If a registrant discovers an error in a previously filed return that resulted in an underpayment of tax or overpayment of refund:

- **Voluntary Disclosure** must be filed via the FTA portal.
- If the error results in a tax difference exceeding **AED 10,000**, a Voluntary Disclosure is mandatory.
- If the error is **AED 10,000 or less**, the adjustment can be made in the next return filing.

**Legislation:** Tax Procedures Law Art. 30; Executive Regulation (Tax Procedures).

---

## Step 8: Designated Zones, Tax Invoices, Record-Keeping, and EU Comparison

### 8.1 Designated Zones (Free Zones) (Art. 51, VAT Decree-Law) [T1]

Certain free zones in the UAE are designated as **Designated Zones** by Cabinet Decision. For VAT purposes, Designated Zones are treated as being **outside the UAE** but **only for the supply of goods**.

**Key principle:** Goods transactions involving Designated Zones follow import/export rules. Services within or to Designated Zones are treated as UAE supplies (standard UAE VAT rules apply).

**Legislation:** VAT Decree-Law Art. 51; Cabinet Decision No. 59 of 2017 (as amended).

#### Conditions for Designated Zone Treatment [T1]

A free zone qualifies as a Designated Zone only if:
1. It is fenced and has security and customs controls on entry/exit of goods and people.
2. It has internal procedures for record-keeping of goods and inventory.
3. The operator of the zone complies with FTA requirements.

**Legislation:** Executive Regulation Art. 51.

#### VAT Treatment of Designated Zone Transactions [T1]

| Transaction | VAT Treatment | Reference |
|------------|---------------|-----------|
| Supply of goods within same Designated Zone | Not a supply (no VAT) | Art. 51(1) |
| Transfer of goods between two Designated Zones | Not a supply (no VAT) | Art. 51(2) |
| Supply of goods from Designated Zone to UAE mainland | Treated as import (VAT due) | Art. 51(4) |
| Supply of goods from UAE mainland to Designated Zone | May be zero-rated if conditions met | Art. 51(3) |
| Supply of goods from Designated Zone to outside UAE | Export (zero-rated) | Art. 45(1) |
| Import of goods from outside UAE to Designated Zone | Not an import (no VAT at point of entry) | Art. 51(5) |
| Supply of services within Designated Zone | Standard UAE VAT rules apply (5%) | Art. 51(8) |
| Supply of services from mainland to Designated Zone | Standard UAE VAT rules apply (5%) | Art. 51(8) |
| Supply of water, energy, or telecommunications to Designated Zone | Standard UAE VAT rules apply (5%) | Art. 51(7) |

#### Key Designated Zones [T1]

The following is a non-exhaustive list of Designated Zones specified by Cabinet Decision:

**Abu Dhabi:**
- Khalifa Industrial Zone (KIZAD)
- Abu Dhabi Airport Free Zone
- Masdar City Free Zone
- twofour54 (for goods only)
- Abu Dhabi Global Market (ADGM) -- note: services are standard rated

**Dubai:**
- Jebel Ali Free Zone (JAFZA)
- Dubai Airport Free Zone (DAFZA)
- Dubai Multi Commodities Centre (DMCC) -- for goods only
- Dubai Silicon Oasis (portions)
- Dubai South Free Zone
- Dubai International Financial Centre (DIFC) -- note: only for goods
- Dubai Gold & Diamond Park
- Dubai Textile City
- Dubai Auto Zone
- International Humanitarian City

**Sharjah:**
- Hamriyah Free Zone
- Sharjah Airport International Free Zone (SAIF Zone)

**Ajman:**
- Ajman Free Zone

**Umm Al Quwain:**
- Umm Al Quwain Free Trade Zone (UAQFTZ)
- Ahmed Bin Rashid Free Zone

**Ras Al Khaimah:**
- RAK Free Trade Zone
- RAK Investment Authority Free Zone
- RAK Maritime City Free Zone
- Al Hamra Industrial Zone

**Fujairah:**
- Fujairah Free Zone
- Fujairah Oil Industry Zone (FOIZ)
- Fujairah Creative City

**[T2] flag: The list of Designated Zones is updated periodically by Cabinet Decision. Always verify the current list on the FTA website before applying Designated Zone treatment.**

**Legislation:** Cabinet Decision No. 59 of 2017 (as amended).

### 8.2 E-Invoicing (Effective 2026-2027) [T1]

Cabinet Decision No. 106 of 2025 introduces e-invoicing requirements:
- **Voluntary pilot:** Expected to begin July 2026.
- **Mandatory adoption:** Large businesses from January 2027.
- Penalties for non-compliance apply from mid-2026.

**[T2] flag: E-invoicing requirements are evolving. Verify current status with FTA before advising on compliance obligations.**

### 8.3 Tax Invoice Requirements [T1]

#### Full Tax Invoice (Art. 59, Executive Regulation) [T1]

A tax invoice must be issued within **14 days** of the date of supply and must contain:

| Field | Requirement |
|-------|-------------|
| Title | "Tax Invoice" clearly displayed |
| Supplier name | Full legal name of the supplier |
| Supplier address | Registered address |
| Supplier TRN | 15-digit Tax Registration Number |
| Recipient name | Full legal name of the recipient |
| Recipient address | Address of the recipient |
| Recipient TRN | If recipient is VAT-registered |
| Invoice number | Sequential, unique number |
| Invoice date | Date of issuance |
| Date of supply | If different from invoice date |
| Description | Description of goods/services supplied |
| Quantity | For goods: quantity of items |
| Unit price | Price per unit (exclusive of VAT) |
| Discount | Any discount applied |
| Net amount | Total value before VAT |
| VAT rate | 5%, 0%, or "Exempt" |
| VAT amount | In AED |
| Gross amount | Total including VAT |
| Currency | If not AED, state the exchange rate used |

**Legislation:** Executive Regulation Art. 59.

#### Simplified Tax Invoice [T1]

A simplified tax invoice may be issued for supplies not exceeding **AED 10,000** (inclusive of VAT). Required fields:

| Field | Requirement |
|-------|-------------|
| Title | "Tax Invoice" |
| Supplier name | Full legal name |
| Supplier TRN | 15-digit number |
| Invoice date | Date of issuance |
| Description | Description of goods/services |
| Total amount | Including VAT |
| VAT amount | In AED |

**Legislation:** Executive Regulation Art. 59(6).

#### Tax Credit Note [T1]

A tax credit note must be issued when there is a decrease in the consideration for a supply. It must contain:
- Reference to the original tax invoice.
- Reason for the credit note.
- The amount of the adjustment.
- The VAT amount adjusted.

**Legislation:** Executive Regulation Art. 62.

### 8.4 Record-Keeping Requirements [T1]

Registrants must maintain the following records for a minimum of **5 years** (15 years for real estate):

| Record Type | Retention Period | Reference |
|------------|-----------------|-----------|
| Tax invoices (issued and received) | 5 years | Tax Procedures Law Art. 26 |
| Tax credit notes | 5 years | Tax Procedures Law Art. 26 |
| Import/export documents | 5 years | Tax Procedures Law Art. 26 |
| Accounting records | 5 years | Tax Procedures Law Art. 26 |
| Bank statements | 5 years | Tax Procedures Law Art. 26 |
| Contracts and agreements | 5 years | Tax Procedures Law Art. 26 |
| Real estate records | 15 years | Tax Procedures Law Art. 26 |
| VAT returns filed | 5 years | Tax Procedures Law Art. 26 |
| Customs declarations | 5 years | Tax Procedures Law Art. 26 |

**Legislation:** Tax Procedures Law Art. 26; Executive Regulation (Tax Procedures) Art. 16.

### 8.5 Comparison with EU VAT [T1]

| Feature | UAE VAT | EU VAT (Directive 2006/112/EC) |
|---------|---------|-------------------------------|
| Standard rate | 5% (single rate) | Varies by member state: 17-27% (e.g., MT 18%, DE 19%, HU 27%) |
| Reduced rates | None | Multiple reduced rates permitted (5%, 9%, 12%, etc.) |
| Zero-rating | Specified categories (Art. 45) | Limited zero-rating (mostly UK legacy); EU uses exemptions with/without credit |
| Exempt categories | Financial services (margin), residential property, bare land, local transport, life insurance | Broader: medical, education, insurance, postal, cultural, sports, financial, real estate |
| Registration threshold (resident) | AED 375,000 (~EUR 94,000) | Varies: EUR 5,000 (Sweden) to EUR 85,000 (UK pre-Brexit); no EU-wide standard |
| Filing frequency | Quarterly (default) or monthly | Varies: monthly, quarterly, annual depending on member state |
| Reverse charge (imports) | Via VAT return (Box 3/6) or customs | Via VAT return (acquisitions boxes) |
| Intra-community supplies | N/A (no GCC equivalent fully operational) | Extensive rules for goods (EC Sales List, Intrastat) |
| Emirate-level breakdown | Required (Box 1) | No sub-national breakdown required |
| Tourist refund scheme | Yes (Planet/Fintrax) | Yes (various operators per member state) |
| Tax invoicing | Mandatory for all taxable supplies | Mandatory with EU-wide minimum requirements |
| Digital services (B2C) | Non-resident must register | One-Stop Shop (OSS) available |
| VAT grouping | Available | Available in most member states |
| Profit margin scheme | Available (second-hand goods) | Available (Directive Art. 312-325) |
| Penalties (late filing) | AED 1,000 / 2,000 | Varies widely by member state |
| Penalties (late payment) | 14% per annum (from Apr 2026) | Varies widely by member state |
| Capital assets adjustment | 5-10 years | 5-20 years depending on member state |

#### Key Conceptual Differences [T1]

1. **Single rate vs. multiple rates:** The UAE has only one positive rate (5%). EU member states have standard, reduced, super-reduced, and parking rates. This makes UAE classification simpler.

2. **No intra-community system:** The EU has an extensive intra-community supply/acquisition system with EC Sales Lists and Intrastat reporting. The GCC equivalent is not yet fully operational (only SA, BH, OM have implemented alongside UAE).

3. **Designated Zones:** The UAE's Designated Zone concept (treating free zones as outside the state for goods) has no direct EU equivalent. EU free zones exist but operate differently for VAT.

4. **Emirate-level reporting:** The UAE requires supplies to be broken down by Emirate in Box 1. No EU member state requires sub-national VAT reporting on the return itself (though Intrastat and local reporting may exist).

5. **Simpler exemption structure:** UAE exemptions are narrower than EU exemptions. The EU exempts a wider range of activities (medical, education, cultural, sports, postal) while the UAE zero-rates some of these (healthcare, education) allowing input tax recovery.

6. **No input tax deduction for exempt businesses:** Both systems deny input tax recovery for exempt activities, but the EU's partial exemption rules are more complex due to the broader range of exempt activities.

#### Practical Implications for Multi-Jurisdictional Businesses [T2]

If a business operates in both the UAE and an EU member state:
- **Transfer pricing:** Intra-group supplies must be at arm's length for both UAE VAT (Art. 36) and EU VAT purposes.
- **Reverse charge:** A UAE entity receiving services from an EU entity applies UAE reverse charge (5%). The EU entity treats the supply as an export of services (outside EU).
- **No mutual recognition:** UAE VAT registration does not confer any status in the EU, and vice versa. Separate registrations required.
- **Different fiscal representatives:** UAE does not require fiscal representatives for non-residents (they register directly with FTA). Some EU states require fiscal representatives for non-EU businesses.

---

## PROHIBITIONS

- **NEVER** let AI guess VAT box assignment -- it is deterministic from the classification facts. [T1]
- **NEVER** classify a supply as zero-rated without verifying the specific conditions under Art. 45 are met. [T1]
- **NEVER** allow input tax recovery on blocked categories (entertainment, motor vehicles for personal use, employee personal benefits) under any circumstances. [T1]
- **NEVER** apply the reverse charge to out-of-scope categories (salaries, dividends, fines, loan repayments). [T1]
- **NEVER** apply the reverse charge when the non-resident supplier is already registered for UAE VAT and has charged VAT on the invoice. [T1]
- **NEVER** treat services in a Designated Zone as being outside the UAE -- only goods qualify for Designated Zone treatment. [T1]
- **NEVER** report services supplied within or to a Designated Zone as exports or outside the scope of UAE VAT. [T1]
- **NEVER** confuse zero-rated (Art. 45, input tax recoverable) with exempt (Art. 46, input tax NOT recoverable). [T1]
- **NEVER** omit the Emirate-level breakdown in Box 1 -- the FTA requires supplies to be allocated by Emirate. [T1]
- **NEVER** file a return without confirming the tax period assignment (quarterly vs. monthly) with the FTA portal. [T1]
- **NEVER** ignore the AED 500 per recipient threshold for free samples -- exceeding it triggers deemed supply treatment. [T1]
- **NEVER** apply tourist refund amounts without confirmation from the approved operator (Planet/Fintrax). [T1]
- **NEVER** allow bad debt relief without verifying the 6-month aging and write-off conditions. [T1]
- **NEVER** accept a "first supply" residential property zero-rating claim without verifying the completion date is within 3 years. [T1]
- **NEVER** compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]
- **NEVER** classify financial services as standard rated without confirming they are fee-based (not margin/interest-based). [T1]
- **NEVER** ignore the AED 5,000,000 capital asset threshold when determining whether the Capital Assets Scheme applies. [T1]

---

## Edge Case Registry

### EC1 -- Designated Zone: Goods Transfer Between Zones [T1]
**Situation:** Company A in JAFZA sells goods to Company B in KIZAD. Both are Designated Zones.
**Resolution:** This is NOT a supply for VAT purposes. No output VAT, no invoice required (for VAT purposes). The transfer of goods between Designated Zones is treated as outside the UAE. No entry on the VAT return.
**Legislation:** VAT Decree-Law Art. 51(2); Executive Regulation Art. 51.

### EC2 -- Designated Zone: Goods from Zone to Mainland [T1]
**Situation:** Company in JAFZA sells goods to a Dubai mainland customer.
**Resolution:** This is treated as an **import** by the mainland customer. The goods enter the UAE mainland and VAT at 5% is due. The mainland buyer reports this in **Box 6** (goods imported). The JAFZA company does NOT charge VAT (the zone company treats this as an export from the zone).
**Legislation:** VAT Decree-Law Art. 51(4); Executive Regulation Art. 51.

### EC3 -- Real Estate: First Sale vs. Resale [T2]
**Situation:** Developer sells a new residential apartment completed 18 months ago for the first time.
**Resolution:** This is a **zero-rated** supply under Art. 45(4) (first supply of residential property within 3 years of completion). Report in **Box 4**. Input tax on construction costs is recoverable.
**Follow-up:** If the buyer later resells the same property 5 years after original completion, that subsequent sale is **exempt** under Art. 46(2). Report in **Box 5**. Input tax on costs related to the resale is NOT recoverable.
**[T2] flag: Verify "first supply" status and completion date with supporting documentation.**
**Legislation:** VAT Decree-Law Art. 45(4), Art. 46(2); VAT Public Clarification VATP002.

### EC4 -- Profit Margin Scheme (Art. 29, Executive Regulation) [T2]
**Situation:** Second-hand goods dealer purchases a used car from a private (non-registered) individual and resells it.
**Resolution:** The **profit margin scheme** may apply. VAT is calculated on the **profit margin** (selling price minus purchase price), not the full selling price. This is available for second-hand goods, antiques, and collectors' items where VAT was not charged on the original purchase.
**[T2] flag: Profit margin scheme requires specific conditions. Reviewer must confirm eligibility.**
**Legislation:** VAT Decree-Law Art. 44; Executive Regulation Art. 29.

### EC5 -- Tourist VAT Refund (Planet/Fintrax) [T1]
**Situation:** Retail store participates in the Tourist Refund Scheme and processes refunds for departing tourists.
**Resolution:** The store charges 5% VAT at point of sale (standard rated, Box 1). The tourist claims a refund at the airport/port via the approved operator (Planet Tax Free). The **refund amount** is reported in **Box 2** of the store's VAT return, reducing the net output tax liability. The store must be registered with the Tourist Refund Scheme.
**Legislation:** VAT Decree-Law Art. 68; Cabinet Decision No. 41 of 2018; FTA Tourist Refund Scheme guidelines.

### EC6 -- Healthcare/Education Zero-Rating Conditions [T2]
**Situation:** Private clinic provides cosmetic surgery services.
**Resolution:** Cosmetic procedures are **NOT** qualifying healthcare under Art. 45(6) unless the procedure is deemed medically necessary by a licensed healthcare professional. Elective cosmetic surgery is **standard rated** at 5%.
**[T2] flag: Classification depends on medical necessity. Reviewer must confirm with client's medical documentation.**
**Similarly for education:** Private tutoring outside a recognized institution is **standard rated**. Only education within a curriculum recognized by the relevant government authority qualifies for zero-rating.
**Legislation:** VAT Decree-Law Art. 45(5)-(6); Executive Regulation Art. 34-35.

### EC7 -- Agent vs. Principal (Art. 8-9, VAT Decree-Law) [T1]
**Situation:** Company A acts as an agent for Company B, collecting payments on behalf of Company B.
**Resolution:** Determine whether the person acts as **agent** (disclosed) or **principal** (undisclosed):
- **Disclosed agent:** The agent is not making the supply. The principal makes the supply. The agent reports only their commission/fee as their taxable supply. The underlying supply is reported by the principal.
- **Undisclosed agent:** The agent is treated as having received and made the supply. Both the acquisition and the onward supply must be reported.
**Legislation:** VAT Decree-Law Art. 8-9; Executive Regulation Art. 6.

### EC8 -- Related Party Supplies at Market Value (Art. 36, VAT Decree-Law) [T1]
**Situation:** Parent company supplies services to a subsidiary at below-market-value prices. The subsidiary is partially exempt and cannot recover all input tax.
**Resolution:** Where a supply is made between **related parties** and the recipient cannot fully recover input tax, the supply is valued at **open market value** (not the actual consideration). This prevents VAT leakage through underpriced intra-group transactions.
- If both parties can fully recover input tax, the actual consideration is accepted.
**Legislation:** VAT Decree-Law Art. 36; Executive Regulation Art. 23.

### EC9 -- Bad Debt Relief (Art. 64, VAT Decree-Law) [T2]
**Situation:** Supplier issued a tax invoice 18 months ago, charged and reported VAT, but the customer has not paid and the debt is now written off as bad.
**Resolution:** The supplier may adjust the output tax previously reported if:
1. The supply was made to a registered person (or the supply value including VAT exceeds AED 500).
2. The supplier has written off the debt (wholly or partly) in their accounts.
3. More than **6 months** have passed since the payment was due.
4. The supplier has made reasonable efforts to collect the debt.
The adjustment is reported in **Box 7** as a negative adjustment to output tax.
**If the customer later pays (full or partial), the supplier must re-account for the output tax.**
**[T2] flag: Bad debt relief conditions must be verified by reviewer. Documentary evidence required.**
**Legislation:** VAT Decree-Law Art. 64; Executive Regulation Art. 52.

### EC10 -- Capital Assets Adjustment [T2]
**Situation:** A company acquired a building 3 years ago for AED 10 million (plus AED 500,000 VAT) and claimed full input tax. The building is now partially used for exempt supplies (leasing residential units).
**Resolution:** The **Capital Assets Scheme** requires annual adjustment of input tax over:
- 10 years for buildings.
- 5 years for other capital assets over AED 5 million.
In Year 4, if 30% of the building is used for exempt supplies, the company must repay 30% of 1/10th of the original input tax claimed (AED 500,000 x 1/10 x 30% = AED 15,000 repayment).
**[T2] flag: Capital asset adjustments are complex. Reviewer must verify the calculation and usage proportions.**
**Legislation:** VAT Decree-Law Art. 57; Executive Regulation Art. 50.

### EC11 -- E-Commerce and Digital Services [T1]
**Situation:** UAE-based e-commerce company sells goods online to customers within the UAE and ships from a warehouse in Dubai.
**Resolution:** Standard rated supply at 5%. Report in Box 1 (Emirate: Dubai, based on warehouse location). If the company also sells to customers outside the UAE, those are exports (Box 4, zero-rated) provided export evidence (customs declarations, delivery proof) is maintained.
**For non-resident digital service providers:** If a non-resident provides electronic/digital services to UAE consumers (B2C), the non-resident must register for UAE VAT (no threshold applies) and account for VAT.
**Legislation:** VAT Decree-Law Art. 34 (electronic services place of supply); Executive Regulation Art. 21.

### EC12 -- Mixed-Use Building (Residential + Commercial) [T2]
**Situation:** Developer constructs a building with ground-floor commercial units and upper-floor residential apartments. First sale.
**Resolution:** The commercial portion is **standard rated** at 5%. The residential portion (first supply within 3 years) is **zero-rated**. Input tax on construction must be apportioned between the two uses.
**[T2] flag: Apportionment method must be confirmed by reviewer (e.g., floor area, cost allocation).**
**Legislation:** VAT Decree-Law Art. 45(4); Executive Regulation Art. 33.

### EC13 -- Free Samples and Gifts [T1]
**Situation:** Company distributes free product samples to potential customers.
**Resolution:** If the cost per recipient per year is **AED 500 or less**, this is NOT a deemed supply and no output VAT is due. If the cost exceeds AED 500 per recipient, it is a **deemed supply** and output VAT at 5% must be accounted for on the cost of the goods.
**Legislation:** VAT Decree-Law Art. 6; Executive Regulation Art. 5.

### EC14 -- Intercompany Services within a Tax Group [T1]
**Situation:** Company A and Company B are members of the same VAT Tax Group. Company A provides management services to Company B.
**Resolution:** Intra-group supplies between members of a registered Tax Group are **disregarded** for VAT purposes. No output VAT, no entry on the VAT return. The group is treated as a single taxable person.
**Legislation:** VAT Decree-Law Art. 18; Executive Regulation Art. 8.

---

## Test Suite

### Test 1 -- Standard Local Sale (Dubai) [T1]
**Input:** UAE-registered company sells office furniture to a Dubai customer. Invoice: AED 10,000 net + AED 500 VAT. Customer is in Dubai.
**Expected output:** Box 1b (Dubai) = AED 10,000. VAT amount = AED 500. Total output tax includes AED 500.

### Test 2 -- Export of Goods (Zero-Rated) [T1]
**Input:** UAE-registered company exports machinery to India. Invoice: AED 50,000 net. Customs export declaration obtained. Goods left UAE within 30 days.
**Expected output:** Box 4 = AED 50,000. VAT amount = AED 0. No output VAT. Full input tax recovery on related purchases.

### Test 3 -- Reverse Charge: Services from Non-Resident [T1]
**Input:** UAE-registered company receives legal advisory services from a UK law firm. Invoice: AED 20,000 (no VAT charged). UK firm has no UAE establishment.
**Expected output:** Box 3 = AED 20,000. Output VAT = AED 1,000 (5%). Box 10 = AED 1,000 (input tax recovery). Net VAT effect = zero (for fully taxable business).

### Test 4 -- Exempt Supply: Residential Lease [T1]
**Input:** UAE-registered property company leases a residential apartment (completed 5 years ago). Monthly rent: AED 8,000.
**Expected output:** Box 5 = AED 8,000. No output VAT. Input tax on expenses related to this property is NOT recoverable.

### Test 5 -- Blocked Input Tax: Motor Vehicle [T1]
**Input:** UAE-registered company purchases a sedan for employee use. Invoice: AED 120,000 + AED 6,000 VAT. Not a taxi company, not a car rental business.
**Expected output:** Box 9 = AED 120,000. Input tax recovery = AED 0 (BLOCKED under Exec. Reg. Art. 53(1)(b)). The AED 6,000 VAT is a cost to the business.

### Test 6 -- Designated Zone: Goods from JAFZA to Abu Dhabi Mainland [T1]
**Input:** Company in JAFZA (Designated Zone) sells goods valued at AED 30,000 to a customer in Abu Dhabi mainland.
**Expected output (Abu Dhabi customer's return):** Box 6 = AED 30,000. Import VAT = AED 1,500 (5%). Input tax recoverable: AED 1,500 (if fully taxable business). The JAFZA company does not charge VAT (treats as export from zone).

### Test 7 -- Tourist VAT Refund [T1]
**Input:** Dubai retail store (VAT-registered) sells goods worth AED 5,000 + AED 250 VAT to a tourist. Tourist claims AED 212.50 refund via Planet Tax Free at departure.
**Expected output:** Box 1b (Dubai) = AED 5,000. Output VAT = AED 250. Box 2 = AED 212.50 (tourist refund). Net output tax contribution from this transaction: AED 250 - AED 212.50 = AED 37.50.

### Test 8 -- Bad Debt Relief [T2]
**Input:** UAE company issued invoice for AED 10,500 (AED 10,000 + AED 500 VAT) in Q1 2025. Customer has not paid. 8 months have passed. Debt written off. Reasonable collection efforts documented.
**Expected output:** Box 7 = -AED 500 (negative adjustment to output tax). Net output tax reduced by AED 500. If customer later pays, AED 500 must be re-accounted.

### Test 9 -- First Sale of Residential Property (Zero-Rated) [T2]
**Input:** Developer sells a new residential villa completed 24 months ago. Sale price: AED 2,000,000. This is the first sale of this property.
**Expected output:** Box 4 = AED 2,000,000. VAT = AED 0 (zero-rated). Input tax on construction costs is fully recoverable.
**[T2] flag: Verify completion date and "first supply" status.**

### Test 10 -- Mixed Supplies: Apportionment [T2]
**Input:** Financial services company makes both fee-based services (standard rated, AED 600,000/year) and interest income (exempt, AED 400,000/year). Total input tax for the period: AED 12,000.
**Expected output:**
- Recoverable input tax = AED 12,000 x (600,000 / 1,000,000) = AED 7,200.
- Non-recoverable (exempt portion) = AED 4,800.
- Box 11 = AED 7,200 (after apportionment).
**[T2] flag: Apportionment ratio and method must be confirmed by reviewer.**

### Test 11 -- Credit Note Adjustment [T1]
**Input:** UAE company issued a credit note for AED 2,100 (AED 2,000 net + AED 100 VAT) against a previous standard rated sale in Abu Dhabi.
**Expected output:** Box 7 = -AED 100 (negative adjustment to output VAT). Box 1a (Abu Dhabi) is reduced by AED 2,000 in the adjustment column.

### Test 12 -- E-Commerce Export to Saudi Arabia [T1]
**Input:** UAE-registered online retailer ships goods to a customer in Saudi Arabia. Invoice: AED 3,000. Customs export documentation obtained.
**Expected output:** Box 4 = AED 3,000. VAT = AED 0 (zero-rated export). Full input tax recovery on related costs. Export evidence must be retained.

---

## Reviewer Escalation Protocol

### Tier 2 Flag Format [T2]

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified UAE tax advisor must confirm before filing.
```

### Tier 3 Escalation Format [T3]

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified UAE tax advisor. Document gap.
```

### Situations Requiring Escalation [T2/T3]

| Situation | Tier | Reason |
|-----------|------|--------|
| Apportionment method selection | T2 | Multiple methods possible; reviewer must confirm |
| Healthcare/education zero-rating eligibility | T2 | Conditions depend on licensing and recognition |
| First sale of residential property | T2 | Completion date verification required |
| Profit margin scheme eligibility | T2 | Specific conditions must be met |
| Bad debt relief | T2 | Documentation and timing conditions |
| Capital asset adjustment calculation | T2 | Complex multi-year calculation |
| Designated Zone status verification | T2 | Zone list may be updated |
| VAT group formation/dissolution | T2 | Significant structural implications |
| Financial services classification (margin vs. fee) | T2 | Critical distinction for exempt vs. standard |
| Transfer of business as going concern | T3 | Complex conditions; outside skill scope |
| Multi-jurisdictional group restructuring | T3 | Requires specialist cross-border advice |
| Criminal tax evasion concerns | T3 | Legal matter; outside skill scope entirely |
| FTA audit response strategy | T3 | Requires specialist representation |

---

## Contribution Notes

If you are adapting this skill for another GCC jurisdiction (Saudi Arabia, Bahrain, Oman, Kuwait, Qatar), you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all box numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard rate (SA/BH: 15%; OM: 5%; KW/QA: not yet implemented).
4. Replace the registration thresholds with your jurisdiction's equivalents.
5. Replace the Designated Zone rules with your jurisdiction's free zone VAT treatment.
6. Replace the penalty schedule with your jurisdiction's penalty framework.
7. Replace the Emirate-level breakdown requirement (UAE-specific) with any sub-national reporting.
8. Have a qualified tax advisor in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
