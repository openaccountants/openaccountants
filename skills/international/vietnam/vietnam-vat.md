---
name: vietnam-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for Vietnam VAT (Value Added Tax / Thue Gia Tri Gia Tang) purposes. Trigger on phrases like "Vietnam VAT", "GTGT", "Vietnamese tax", "eTax Vietnam", "VAT declaration Vietnam", "Law on VAT", or any request involving Vietnamese VAT filing, classification, or compliance. This skill contains the complete Vietnam VAT classification rules, declaration form mappings, deductibility rules, credit method vs. direct method, reverse charge treatment, e-invoicing mandates, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Vietnam VAT-related work.
---

# Vietnam VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Vietnam |
| Jurisdiction Code | VN |
| Primary Legislation | Law on Value Added Tax No. 13/2008/QH12 (as amended by Law No. 31/2013/QH13 and Law No. 71/2014/QH13) |
| Supporting Legislation | Decree No. 209/2013/ND-CP (detailing the VAT Law); Circular No. 219/2013/TT-BTC (guiding VAT implementation); Decree No. 123/2020/ND-CP (e-invoicing); Circular No. 78/2021/TT-BTC (e-invoicing guidance); Resolution No. 43/2022/QH15 (temporary VAT reduction to 8%); Decree No. 72/2024/ND-CP (VAT reduction extension); Resolution No. 204/2025/QH15 (VAT reduction extended to 31 Dec 2026 with expanded scope) |
| Tax Authority | General Department of Taxation (Tong Cuc Thue), Ministry of Finance |
| Filing Portal | https://thuedientu.gdt.gov.vn (eTax) |
| Contributor | [Jurisdiction practitioner to be confirmed] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: transaction classification, rate determination, declaration form mapping, blocked input VAT, credit method calculations, e-invoicing requirements. Tier 2: direct method vs. credit method selection, partial input VAT allocation, sector-specific rate determinations. Tier 3: transfer pricing disputes, industrial zone incentives, complex financial restructuring. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed tax consultant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax consultant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Tax Code (Ma So Thue / MST)** [T1] -- 10-digit (or 13-digit for branches) tax code
2. **VAT calculation method** [T1] -- Credit method (khau tru) or Direct method (truc tiep). This is CRITICAL -- different forms, different rules
3. **Filing frequency** [T1] -- Monthly (revenue > VND 50 billion/year) or Quarterly (revenue <= VND 50 billion/year)
4. **Business type** [T1] -- LLC (TNHH), JSC (CTCP), sole proprietorship, foreign-invested enterprise (FIE), representative office, branch
5. **Industry/sector** [T2] -- impacts rate classification (10% vs. 5% vs. 0%)
6. **Does the business make both taxable and non-taxable/exempt supplies?** [T2] -- if yes, input VAT allocation required (Circular 219, Article 14); reviewer must confirm allocation method
7. **Does the business operate in an Industrial Zone / Export Processing Zone (EPZ)?** [T3] -- special VAT treatment; escalate
8. **Excess VAT credit carried forward** [T1] -- from prior period
9. **Does the business import goods?** [T1] -- import VAT is collected by Customs
10. **Does the business receive services from overseas suppliers?** [T1] -- impacts foreign contractor tax (FCT) / reverse charge treatment

**If any of items 1-2 are unknown, STOP. Do not classify any transactions until the VAT calculation method is confirmed.**

---

## Step 1: VAT Calculation Methods [T1]

**CRITICAL DISTINCTION:** Vietnam has TWO fundamentally different VAT calculation methods. The method determines the form, the rules, and the ability to claim input VAT.

### Credit Method (Phuong phap khau tru) [T1]
**Legislation:** Law on VAT, Article 10; Circular 219, Article 12

- Used by: enterprises with full accounting records and books
- Mandatory for: enterprises with annual revenue > VND 1 billion AND maintaining proper accounting
- **How it works:** Output VAT - Input VAT = VAT payable (or excess credit)
- Input VAT is creditable (recoverable)
- Form: Declaration Form 01/GTGT

### Direct Method (Phuong phap truc tiep) [T1]
**Legislation:** Law on VAT, Article 11; Circular 219, Article 13

- Used by: individuals, household businesses, enterprises not meeting credit method requirements
- **How it works:** VAT = Revenue x Direct Rate (varies by industry, typically 1-5%)
- NO input VAT credit
- Form: Declaration Form 04/GTGT

### Direct Method Rates by Industry [T1]
**Legislation:** Circular 219, Article 13(2)

| Industry | Direct Rate |
|----------|-------------|
| Distribution, supply of goods | 1% |
| Services, construction (excluding materials) | 5% |
| Manufacturing, transport, services linked to goods, construction (including materials) | 3% |
| Other business activities | 2% |

**This skill primarily covers the Credit Method (01/GTGT). Direct Method is noted for reference but its application is simpler and does not involve input VAT crediting.**

---

## Step 2: VAT Rates and Classification Matrix

### Standard Rate: 10% [T1]
**Legislation:** Law on VAT, Article 8(3)

All goods and services NOT listed at 5%, 0%, or exempt are subject to 10%. This is the default rate. Includes:
- Most manufactured goods
- Most services (consulting, IT, construction, etc.)
- Telecommunications
- Real estate transfers (commercial)
- Hotels, restaurants, tourism

### Temporary VAT Reduction: 8% (Selected Goods/Services) [T1]
**Legislation:** Resolution No. 43/2022/QH15; Decree No. 72/2024/ND-CP; Resolution No. 204/2025/QH15

- Effective: Various periods from 2022 onward; most recently extended through **31 December 2026** (Resolution No. 204/2025/QH15, adopted 17 June 2025, effective 1 July 2025). The scope has been **expanded** compared to earlier resolutions.
- Applies to: goods and services currently subject to 10% VAT, EXCEPT:
  - Telecommunications
  - Financial services
  - Banking
  - Securities
  - Insurance
  - Real estate
  - Metals and prefabricated metal products
  - Mining products (excluding coal)
  - Coke, refined petroleum
  - Goods/services subject to excise tax (excluding gasoline)
- **IMPORTANT 2025 change:** Compared to earlier resolutions, Resolution 204/2025 **expanded** the list of eligible goods/services. Transportation, logistics, and information technology goods and services are NOW eligible for the 8% reduced rate (previously excluded). Chemical products have also been removed from the exclusion list.
- **For eligible goods/services, rate is 8% instead of 10%**
- [T2] Flag for reviewer if uncertain whether a specific good/service qualifies for the 8% reduction

### Reduced Rate: 5% [T1]
**Legislation:** Law on VAT, Article 8(2); Circular 219, Article 10

| Category | Examples |
|----------|---------|
| Clean water for daily life | Piped water, processed water for consumption |
| Ore for fertilizer production; pesticides | Agricultural chemicals |
| Teaching/learning aids | Books, notebooks, teaching equipment |
| Medical equipment, instruments, medicines | Prescription drugs, medical devices, cotton, bandages |
| Cultural/sporting goods | Musical instruments, sports equipment |
| Products from agricultural by-products | Sugar, cashew, pepper, processed agricultural goods (specified list) |
| Unprocessed forestry products (except timber) | Bamboo, rattan, resin |
| Animal husbandry services | Ploughing, dredging, cultivation services |
| Scientific/technological services per law | Research and development services |
| Social housing | Sale/lease of social housing under specific programs |
| Rubber latex | Preliminary processed rubber |

### Zero Rate: 0% [T1]
**Legislation:** Law on VAT, Article 8(1); Circular 219, Article 9

| Category | Conditions |
|----------|------------|
| Exported goods | Goods sold and shipped outside Vietnam; customs declaration required |
| Exported services | Services rendered for consumption outside Vietnam; foreign currency payment required |
| Goods/services sold to EPZ enterprises | Treated as exports (cross-border doctrine within Vietnam) |
| International transport services | Transport from Vietnam to overseas or between overseas points |
| Goods/services not subject to VAT when exported | Specific categories per Circular 219, Article 9(2) |

### Zero-Rating Documentation Requirements [T1]
For 0% to apply:
1. Contract with foreign party or EPZ enterprise
2. Proof of payment (bank transfer) -- preferably in foreign currency for services
3. For goods: customs export declaration (To Khai Hai Quan)
4. For services: evidence that service is consumed entirely outside Vietnam

### Non-Taxable / Exempt Goods and Services [T1]
**Legislation:** Law on VAT, Article 5; Circular 219, Article 4

| Category | Article 5 Reference | Notes |
|----------|---------------------|-------|
| Unprocessed agricultural products | 5(1) | Products of cultivation, husbandry, aquaculture, not yet processed or only through ordinary preliminary processing |
| Breeding livestock/poultry | 5(2) | Including eggs for hatching, breeds |
| Irrigation/ploughing services for agriculture | 5(3) | Agricultural support services |
| Salt production | 5(4) | Industrial salt making |
| Government housing for social policy | 5(5) | State-owned social housing |
| Land use rights | 5(6) | Transfer of land use rights only (not the structure on it) |
| Life insurance | 5(7) | Life insurance, health insurance, student insurance |
| Financial services (specific) | 5(8) | Lending, deposit taking, financial leasing, securities trading, money transfer |
| Medical services | 5(9) | Healthcare by licensed medical establishments |
| Educational services | 5(10) | Teaching and vocational training per law |
| Publishing/importing cultural materials | 5(11) | Newspapers, magazines, political books |
| Public transport (bus, electric vehicle) | 5(12) | Intra-city buses and specified public transport |
| Technology transfer | 5(13) | Per the Law on Technology Transfer |
| Gold in bars/bullion | 5(14) | Gold traded as financial instrument |
| Exported natural resources not yet processed | 5(15) | Unprocessed minerals, crude oil |
| Weapons/military equipment | 5(16) | For national defense/security |
| Imported goods as development aid | 5(17) | ODA goods and humanitarian aid |
| Personal goods of foreign diplomats | 5(18) | Diplomatic immunity |
| Goods in bonded warehouses / customs transit | 5(19) | Not entering domestic market |
| Goods/services of household businesses with revenue below VND 100M/year | 5(25) | Small household business exemption |

---

## Step 3: Declaration Form Structure (Credit Method -- Form 01/GTGT) [T1]

**Legislation:** Circular 219; Circular 80/2021/TT-BTC (declaration forms)

### Form 01/GTGT Structure

#### Section I: Output VAT

| Item | Description | Revenue Column | VAT Column |
|------|-------------|---------------|------------|
| [21] | Goods/services not subject to VAT declaration | Revenue amount | -- |
| [22] | Goods/services not subject to VAT (exempt under Article 5) | Revenue amount | -- |
| [23] | Goods/services subject to 0% | Revenue amount | 0 |
| [24] | Goods/services subject to 5% | Revenue amount | VAT at 5% |
| [25] | Goods/services subject to 8% (temporary reduction) | Revenue amount | VAT at 8% |
| [26] | Goods/services subject to 10% | Revenue amount | VAT at 10% |
| [27] | Total goods/services sold | Sum of [21]-[26] | -- |
| [28] | Total output VAT | -- | Sum of VAT from [23]-[26] |

#### Section II: Input VAT

| Item | Description | Value Column | VAT Column |
|------|-------------|-------------|------------|
| [29] | Input VAT on goods/services for taxable activities (with invoices) | Purchase value | Input VAT |
| [30] | Input VAT on imported goods (Customs-collected) | Import value | Import VAT |
| [31] | Total input VAT ([29] + [30]) | Sum | Sum |
| [32] | Input VAT allocated to taxable activities (if mixed) | -- | Allocated amount |
| [33] | Input VAT adjustment (increase) | -- | Amount |
| [34] | Input VAT adjustment (decrease) | -- | Amount |
| [35] | Total deductible input VAT ([32] + [33] - [34]) | -- | Net deductible |

#### Section III: VAT Calculation

| Item | Description | Calculation |
|------|-------------|-------------|
| [36] | VAT payable in the period (if [28] > [35]) | [28] - [35] |
| [37] | Input VAT carried forward to next period (if [35] > [28]) | [35] - [28] |
| [38] | Input VAT carried forward from prior period | From previous declaration |
| [39] | Cumulative excess input VAT ([37] + [38]) | Sum |
| [40] | Input VAT requested for refund | Amount (if eligible) |
| [41] | Input VAT carried forward after refund ([39] - [40]) | Net carry forward |

### Derived Calculations [T1]

```
[27] = [21] + [22] + [23] + [24] + [25] + [26]
[28] = VAT from [23](=0) + VAT from [24] + VAT from [25] + VAT from [26]
[31] = [29] + [30]
[35] = [32] + [33] - [34]
IF [28] > [35] THEN
  [36] = [28] - [35]  -- VAT payable
  [37] = 0
ELSE
  [36] = 0
  [37] = [35] - [28]  -- Excess input VAT
END
[39] = [37] + [38]
[41] = [39] - [40]
```

---

## Step 4: Input VAT Crediting Rules (Credit Method) [T1]

### Creditable Input VAT [T1]
**Legislation:** Law on VAT, Article 12; Circular 219, Article 14-15

| Condition | Creditable? | Reference |
|-----------|-------------|-----------|
| Purchases of goods/services for taxable business, with valid e-invoice | Yes | Article 12(1) |
| Import VAT paid to Customs | Yes | Article 12(1) |
| Purchases >= VND 20 million: must have bank transfer proof | Yes (if bank proof exists) | Article 15(1) Circular 219 |
| Purchases < VND 20 million: cash payment acceptable | Yes | Article 15(1) |
| Purchases for production of exported goods | Yes | Article 12 |

### Non-Creditable / Blocked Input VAT [T1]
**Legislation:** Circular 219, Article 14; Law on VAT, Article 12

| Blocked Category | Reference | Notes |
|-----------------|-----------|-------|
| No valid invoice (or non-e-invoice after e-invoicing mandate) | Article 15 | Cannot credit without proper documentation |
| Purchases >= VND 20M paid in cash (no bank transfer) | Article 15(1) | Must have proof of non-cash payment for purchases >= VND 20M |
| Input VAT on goods/services for exempt/non-taxable activities | Article 14(2) | Unless apportioned for mixed activities |
| Input VAT on goods/services for non-business purposes | Article 14 | Personal consumption |
| Motor vehicles with 9 seats or fewer (passenger cars) | Article 14(4) | Exception: vehicles for sale/lease, taxi, driving school |
| Input VAT exceeding VND 300 million on passenger cars | Article 14(4) | For permitted passenger cars, input VAT capped at VND 300M |
| Input VAT on goods lost, damaged, or expired (beyond normal levels) | Article 14(2) | Normal loss/damage during transport/storage is creditable |
| Input VAT on purchases from non-registered suppliers | -- | No valid VAT invoice from non-registered entity |

### Motor Vehicle Cap [T1]
**Legislation:** Circular 219, Article 14(4)

- For businesses NOT in the vehicle sale/lease/transport business:
  - Passenger vehicles (9 seats or fewer): input VAT is BLOCKED
  - Exception: if the business is a car dealer, leasing company, taxi operator, or driving school, input VAT is creditable
- Even for permitted businesses: input VAT on passenger vehicles is capped at VND 300 million per vehicle
  - If VAT exceeds VND 300M, only VND 300M is creditable; the excess is a cost

### VND 20 Million Payment Threshold [T1]
**Legislation:** Circular 219, Article 15(1)

- For single purchases with total value >= VND 20,000,000 (inclusive of VAT):
  - Payment MUST be made via bank transfer (wire, check, payment order)
  - Cash payment = input VAT NOT creditable
  - This applies regardless of the relationship between buyer and seller
- For purchases < VND 20,000,000: cash payment is acceptable, input VAT remains creditable

### Partial Input VAT Allocation (Mixed Activities) [T2]
**Legislation:** Circular 219, Article 14(3)

If taxpayer has both taxable and exempt/non-taxable revenue:
- Input VAT directly for taxable supplies = fully creditable
- Input VAT directly for exempt supplies = non-creditable
- Common input VAT = allocated by revenue ratio:

```
Creditable % = (Taxable Revenue / Total Revenue) * 100
```

- If non-creditable portion <= 5% of total input VAT, the ENTIRE input VAT may be credited (de minimis rule)
- Annual adjustment in the final period
- **Flag for reviewer:** Allocation methodology and direct vs. common classification must be confirmed

---

## Step 5: Foreign Contractor Tax (FCT) / Reverse Charge [T1]

**Legislation:** Circular No. 103/2014/TT-BTC (Foreign Contractor Tax)

Vietnam does not use the term "reverse charge" but has the Foreign Contractor Tax (FCT) regime, which includes a VAT component.

### When FCT Applies
When a foreign organization or individual (foreign contractor / foreign subcontractor) provides services or goods associated with services in Vietnam for a Vietnamese entity.

### FCT VAT Component Methods [T1]

| Method | Description | Who Applies |
|--------|------------|-------------|
| Credit Method (registration) | Foreign contractor registers for VAT in Vietnam, issues invoices, files returns | Foreign contractor with permanent establishment or project > 182 days |
| Direct Method (withholding by Vietnamese party) | Vietnamese party withholds VAT on payment to foreign contractor at deemed rates | Most common method |
| Hybrid Method | Mix of credit and direct depending on the contract | Specific cases |

### Direct Method Deemed VAT Rates (Withholding) [T1]
**Legislation:** Circular 103/2014, Article 12

| Service Category | Deemed VAT Rate |
|-----------------|-----------------|
| Services generally | 5% of revenue |
| Services with goods supply (goods >= 50% of contract) | 3% of revenue |
| Services with goods supply (goods < 50%) | 5% of revenue |
| Goods supply only (with or without installation/assembly, where goods are imported) | 2% of revenue (if not imported via customs) |
| Interest on loans | Exempt |
| Leasing of machinery/equipment (without operator) | 5% of revenue |
| Insurance | Exempt |
| Construction (without materials) | 5% of revenue |
| Construction (with materials) | 3% of revenue |
| Transport | 3% of revenue |
| Restaurant/hotel/casino management | 5% of revenue |

### Vietnamese Party's Obligations [T1]
1. Register the foreign contractor tax obligation with the local tax authority
2. Withhold VAT (and CIT component) from payment to foreign contractor
3. File FCT return (Form 01/NTNN) within 10 days of payment
4. The withheld VAT is creditable as input VAT for the Vietnamese party on Form 01/GTGT (Item [29])

---

## Step 6: E-Invoicing Requirements [T1]

**Legislation:** Decree No. 123/2020/ND-CP; Circular No. 78/2021/TT-BTC

### Mandate
- E-invoicing (hoa don dien tu) is MANDATORY for all enterprises, organizations, and individual businesses from 1 July 2022
- All invoices must be issued electronically through the General Department of Taxation's e-invoice system
- Paper invoices are NO LONGER valid (except emergency/system failure situations with specific approval)

### E-Invoice Types [T1]

| Type | Code | Usage |
|------|------|-------|
| VAT invoice (authenticated) | Mau 1 | For credit method taxpayers selling goods/services |
| Sales invoice | Mau 2 | For direct method taxpayers |
| Export invoice | Mau 3 | For exported goods |
| Electronic stamps/tickets | Mau 4 | For transport, entertainment, etc. |

### Mandatory E-Invoice Fields [T1]

1. Invoice name, form symbol, serial number
2. Name, address, tax code of the seller
3. Name, address, tax code of the buyer (for B2B)
4. Name of goods/services, unit, quantity, unit price
5. Total amount before VAT
6. VAT rate
7. VAT amount
8. Total amount including VAT
9. Digital signature of the seller
10. Tax authority's code (for authenticated invoices)
11. Time of creation/signing

### E-Invoice and Input VAT Credit [T1]
- Input VAT can ONLY be credited if supported by a valid e-invoice
- E-invoices must bear the tax authority's authentication code (for Mau 1 invoices)
- Self-generated e-invoices (without tax authority code) are valid only for specified taxpayers authorized by the tax authority

---

## Step 7: Registration Rules [T1]

**Legislation:** Law on Tax Administration No. 38/2019/QH14; Circular 219

| Registration Rule | Condition |
|-------------------|-----------|
| VAT registration | Automatic upon business registration -- all enterprises are registered for VAT |
| Credit method eligibility | Enterprises with annual revenue > VND 1 billion AND maintaining proper accounting records |
| Credit method (voluntary) | Enterprises with revenue <= VND 1B may apply for credit method if they maintain proper books |
| Direct method (default for small) | Household businesses, individuals, enterprises not meeting credit method criteria |
| Filing frequency: Monthly | Annual revenue of previous year > VND 50 billion |
| Filing frequency: Quarterly | Annual revenue of previous year <= VND 50 billion |
| Branch registration | Branches must register separately; head office may file centralized if authorized |
| Foreign contractor registration | Required if contract > 182 days or permanent establishment exists |

### Household Business Exemption [T1]
**Legislation:** Law on VAT, Article 5(25)

- Household businesses / individual businesses with annual revenue from goods/services <= VND 100,000,000 (VND 100 million) per year are NOT subject to VAT
- This threshold is per business activity, per individual

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Law on Tax Administration No. 38/2019/QH14; Decree No. 125/2020/ND-CP (penalties)

### Filing Deadlines

| Obligation | Deadline | Notes |
|------------|----------|-------|
| Monthly VAT declaration (Form 01/GTGT) | 20th of the following month | For taxpayers with revenue > VND 50B |
| Quarterly VAT declaration (Form 01/GTGT) | Last day of the first month following the quarter | For taxpayers with revenue <= VND 50B |
| FCT declaration (Form 01/NTNN) | 10th day after payment to foreign contractor | Per payment |
| Import VAT | Paid at time of customs clearance | Collected by Customs |

### Penalties [T1]
**Legislation:** Decree No. 125/2020/ND-CP

| Violation | Penalty | Reference |
|-----------|---------|-----------|
| Late filing (1-5 days, first offense) | Warning | Article 13(1) |
| Late filing (1-5 days, repeat) | VND 2,000,000 -- 5,000,000 | Article 13(2) |
| Late filing (6-30 days) | VND 5,000,000 -- 8,000,000 | Article 13(3) |
| Late filing (31-60 days) | VND 8,000,000 -- 15,000,000 | Article 13(4) |
| Late filing (61-90 days without tax due) | VND 15,000,000 -- 25,000,000 | Article 13(5) |
| Failure to file (>90 days) | Fine + potential criminal prosecution | Article 13(5), Article 17 |
| Late payment of tax | Interest at 0.03% per day on unpaid amount | Article 59, Law on Tax Administration |
| Tax evasion | Fine of 1-3x the evaded tax amount + criminal prosecution | Article 17 |
| Incorrect declaration (leading to underpayment) | 20% of the deficient tax amount + interest | Article 16 |
| Failure to issue e-invoice | VND 5,000,000 -- 10,000,000 | Article 24 |
| Issuing incorrect e-invoice | VND 3,000,000 -- 5,000,000 | Article 24 |

### Late Payment Interest Calculation [T1]
- Rate: 0.03% per day on the unpaid tax amount
- Calculated from the day after the filing/payment deadline until the date of actual payment
- No cap on total interest (unlike some jurisdictions)

---

## Step 9: Refund Rules [T1]

**Legislation:** Law on VAT, Article 13; Circular 219, Article 18-19

### Refund Eligibility (Credit Method Only)

| Situation | Refund Available? | Conditions |
|-----------|-------------------|------------|
| Excess input VAT for 12 consecutive months (or 4 quarters) | Yes | Minimum refund claim: VND 300 million |
| Excess input VAT on exported goods/services | Yes | Minimum refund claim: VND 300 million per period |
| New enterprise in investment phase (no revenue yet) | Yes | If accumulated input VAT >= VND 300 million |
| Export revenue >= 50% of total revenue | Yes | Pro-rata refund on export-related input VAT |
| Dissolution / bankruptcy / ownership change | Yes | Remaining excess input VAT at termination |

### Refund Processing [T1]
- Fast-track refund (pre-refund, post-audit): within 6 working days -- for low-risk taxpayers
- Standard refund (pre-audit, post-refund): within 40 working days -- for first-time or medium-risk
- Full audit refund: within 40 working days -- for high-risk taxpayers
- Tax authority may extend audit period by up to 40 additional working days for complex cases

### VND 300 Million Minimum [T1]
- Refund is only available if excess input VAT is at least VND 300,000,000
- If below VND 300M, the excess is carried forward (not refunded)

---

## Step 10: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- SaaS subscription from foreign provider [T1]
**Situation:** Vietnamese enterprise pays monthly subscription to a US-based SaaS company (no Vietnam presence). No Vietnamese VAT on the invoice.
**Resolution:** Foreign Contractor Tax (FCT) applies. Vietnamese enterprise withholds VAT at the deemed rate (typically 5% for services) from the payment. The withheld VAT is creditable as input VAT on Form 01/GTGT. Also withhold CIT component (typically 5%). File Form 01/NTNN within 10 days of payment.
**Legislation:** Circular 103/2014/TT-BTC

### EC2 -- Purchase of passenger car (9 seats or fewer) [T1]
**Situation:** Enterprise purchases a sedan for director use, price VND 1,500,000,000, VAT VND 150,000,000.
**Resolution:** Input VAT on passenger vehicles (9 seats or fewer) is BLOCKED for non-transport/non-dealer businesses. However, if the vehicle is for a dealer/leasing/taxi business, input VAT is creditable up to VND 300 million per vehicle. In this case (general business use): input VAT VND 150,000,000 = BLOCKED entirely. Gross amount capitalized as fixed asset.
**Legislation:** Circular 219, Article 14(4)

### EC3 -- Payment >= VND 20 million made in cash [T1]
**Situation:** Enterprise purchases goods for VND 25,000,000 (inclusive of VAT) and pays in cash.
**Resolution:** Input VAT is NOT creditable because the purchase value exceeds VND 20 million and was paid in cash. The full VND 25,000,000 is treated as a cost. To preserve the input VAT credit, payment must be made via bank transfer.
**Legislation:** Circular 219, Article 15(1)

### EC4 -- Export of goods: customs documentation incomplete [T2]
**Situation:** Enterprise exports goods and applies 0% VAT but customs export declaration has not been finalized.
**Resolution:** Zero-rate requires completed customs declaration. If documentation is unavailable at filing time, [T2] flag for reviewer. Tax authority may reclassify as domestic sale at 10% (or 8% if eligible for temporary reduction) if export evidence is not produced.
**Legislation:** Circular 219, Article 9

### EC5 -- Temporary 8% rate: telecommunications service [T1]
**Situation:** Enterprise provides telecommunications services. Asks whether the 8% temporary reduction applies.
**Resolution:** Telecommunications is specifically EXCLUDED from the 8% temporary reduction. Standard 10% rate applies. Decree 72/2024 explicitly lists telecommunications as an excluded category.
**Legislation:** Decree 72/2024/ND-CP; Resolution 43/2022/QH15

### EC6 -- Credit note / adjustment invoice [T1]
**Situation:** Seller issues a credit note for returned goods via e-invoice.
**Resolution:** Issue an adjustment e-invoice (hoa don dieu chinh) referencing the original e-invoice number. The adjustment reduces output VAT for the seller and input VAT for the buyer in the period the adjustment invoice is issued. Both parties must record the adjustment in their respective declarations.
**Legislation:** Decree 123/2020/ND-CP, Article 19

### EC7 -- Import VAT on raw materials [T1]
**Situation:** Enterprise imports raw materials for manufacturing. Customs collects 10% VAT on CIF + duty value.
**Resolution:** Import VAT is creditable as input VAT. Report on Form 01/GTGT, Item [30] (import VAT). Supporting documents: customs declaration and proof of VAT payment to Customs.
**Legislation:** Law on VAT, Article 12; Circular 219, Article 14

### EC8 -- Sale of unprocessed agricultural products [T1]
**Situation:** Enterprise sells fresh unprocessed rice (cultivated, not processed beyond preliminary cleaning).
**Resolution:** Exempt from VAT under Article 5(1) of the Law on VAT. No output VAT. Report in Form 01/GTGT Item [22] (exempt). Input VAT on expenses exclusively for this exempt activity = not creditable. If mixed with taxable activities, allocate [T2].
**Legislation:** Law on VAT, Article 5(1)

### EC9 -- Foreign contractor: interest on loan from overseas bank [T1]
**Situation:** Vietnamese enterprise pays interest to a foreign bank on a USD-denominated loan.
**Resolution:** Interest income is EXEMPT from VAT component of FCT (Circular 103/2014, Article 4(1)). Only CIT component of FCT applies (typically 5% on interest). No VAT withheld. No input VAT to claim.
**Legislation:** Circular 103/2014, Article 4(1)

### EC10 -- E-invoice system failure [T1]
**Situation:** The e-invoice system is down. Enterprise needs to issue an invoice urgently.
**Resolution:** Under Decree 123/2020, Article 14, in case of system failure or disaster, the enterprise may issue paper invoices TEMPORARILY. Must notify the tax authority before using paper invoices. Once the system is restored, must input the paper invoices into the e-invoice system within the prescribed timeframe. Failure to notify = penalties.
**Legislation:** Decree 123/2020/ND-CP, Article 14

### EC11 -- Mixed taxpayer: de minimis rule (non-creditable < 5%) [T1]
**Situation:** Enterprise has total input VAT of VND 500 million. Revenue split: 97% taxable, 3% exempt. Non-creditable portion = 3% = VND 15 million.
**Resolution:** Since the non-creditable portion (VND 15M / VND 500M = 3%) is less than 5% of total input VAT, the de minimis rule applies. The ENTIRE VND 500 million input VAT is creditable. No allocation needed.
**Legislation:** Circular 219, Article 14(3)

### EC12 -- Goods sold at below cost / promotional pricing [T2]
**Situation:** Enterprise sells goods at a price significantly below market value for promotional purposes.
**Resolution:** Tax authority may reassess the taxable value at market price for VAT purposes if the declared price is unreasonably low without valid business justification. [T2] Flag for reviewer: confirm that the pricing has legitimate business rationale (clearance sale, near-expiry goods, market competition). Transfer pricing rules may also apply for related-party transactions.
**Legislation:** Law on VAT, Article 7; Circular 219, Article 7

---

## Step 11: Key Thresholds Summary

| Threshold | Value | Legal Reference |
|-----------|-------|-----------------|
| Credit method revenue threshold | VND 1,000,000,000 (VND 1B) annual | Circular 219, Article 12 |
| Monthly filing threshold | VND 50,000,000,000 (VND 50B) annual | Law on Tax Administration |
| Cash payment limit for input VAT credit | VND 20,000,000 per transaction | Circular 219, Article 15(1) |
| VAT refund minimum | VND 300,000,000 accumulated | Law on VAT, Article 13 |
| Household business exemption | VND 100,000,000 annual revenue | Law on VAT, Article 5(25) |
| Passenger vehicle input VAT cap | VND 300,000,000 per vehicle | Circular 219, Article 14(4) |
| Standard VAT rate | 10% | Law on VAT, Article 8(3) |
| Temporary reduced rate | 8% (eligible goods/services) | Decree 72/2024 |
| Reduced rate | 5% | Law on VAT, Article 8(2) |
| Zero rate (exports) | 0% | Law on VAT, Article 8(1) |
| Late payment interest | 0.03% per day | Law on Tax Administration, Article 59 |
| Partial allocation de minimis rule | 5% of total input VAT | Circular 219, Article 14(3) |
| Fast-track refund processing | 6 working days | Circular 219, Article 18 |
| Standard refund processing | 40 working days | Circular 219, Article 18 |
| E-invoicing mandatory from | 1 July 2022 | Decree 123/2020 |

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed tax consultant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax consultant. Document gap.
```

---

## Step 13: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic sale at 10%
**Input:** Vietnamese enterprise (credit method) sells goods to domestic buyer, net VND 100,000,000, VAT VND 10,000,000.
**Expected output:** Form 01/GTGT Item [26]: Revenue VND 100,000,000, VAT VND 10,000,000 (output VAT). Item [28] includes VND 10,000,000.

### Test 2 -- Domestic sale at temporary 8% rate
**Input:** Enterprise sells eligible manufactured goods (not excluded from 8% reduction), net VND 200,000,000.
**Expected output:** Form 01/GTGT Item [25]: Revenue VND 200,000,000, VAT VND 16,000,000 (8%). Item [28] includes VND 16,000,000.

### Test 3 -- Domestic purchase with valid e-invoice, payment by bank transfer
**Input:** Enterprise purchases office equipment for VND 50,000,000 net + VND 5,000,000 VAT (10%). Paid by bank transfer. Valid e-invoice received.
**Expected output:** Form 01/GTGT Item [29]: Purchase VND 50,000,000, Input VAT VND 5,000,000 (creditable).

### Test 4 -- Purchase >= VND 20M paid in cash
**Input:** Enterprise purchases supplies for VND 22,000,000 (inclusive of VND 2,000,000 VAT). Paid in cash.
**Expected output:** Input VAT VND 2,000,000 = NOT CREDITABLE (cash payment above VND 20M threshold). Full VND 22,000,000 is a cost.

### Test 5 -- Export sale at 0%
**Input:** Enterprise exports goods to Australia, FOB VND 500,000,000. Customs declaration obtained.
**Expected output:** Form 01/GTGT Item [23]: Revenue VND 500,000,000, VAT = VND 0 (zero-rated). Input VAT on related purchases fully creditable.

### Test 6 -- Foreign contractor tax on overseas IT service
**Input:** Enterprise pays USD 10,000 (= VND 250,000,000) to a US IT company for cloud hosting (no Vietnam presence). Service category: services generally (5% VAT, 5% CIT).
**Expected output:** Withhold VAT: 5% x VND 250,000,000 = VND 12,500,000. Withhold CIT: 5% x VND 250,000,000 = VND 12,500,000. File Form 01/NTNN within 10 days. VAT VND 12,500,000 creditable as input VAT on Form 01/GTGT Item [29].

### Test 7 -- Passenger car purchase (blocked)
**Input:** Enterprise (non-transport) purchases sedan, price VND 800,000,000, VAT VND 80,000,000.
**Expected output:** Input VAT VND 80,000,000 = BLOCKED. Gross VND 880,000,000 capitalized as fixed asset. No input VAT on Form 01/GTGT.

### Test 8 -- Import VAT
**Input:** Enterprise imports raw materials, CIF + duty VND 300,000,000. Customs collects 10% VAT = VND 30,000,000.
**Expected output:** Form 01/GTGT Item [30]: Import value VND 300,000,000, Import VAT VND 30,000,000 (creditable).

### Test 9 -- Exempt supply: unprocessed agricultural products
**Input:** Enterprise sells fresh unprocessed vegetables, VND 150,000,000.
**Expected output:** Form 01/GTGT Item [22]: Revenue VND 150,000,000 (exempt). No output VAT. Input VAT on expenses exclusively for this supply = non-creditable.

### Test 10 -- De minimis rule: mixed taxpayer
**Input:** Enterprise has total input VAT VND 400,000,000. Revenue: 96% taxable, 4% exempt. Non-creditable portion = 4% = VND 16,000,000.
**Expected output:** 4% < 5% threshold. De minimis rule applies. Entire VND 400,000,000 input VAT is creditable. No allocation needed. Form 01/GTGT Item [32] = Item [31].

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the facts and legislation
- NEVER claim input VAT on purchases >= VND 20 million paid in cash -- bank transfer proof is mandatory
- NEVER claim input VAT on passenger vehicles (9 seats or fewer) for non-transport/non-dealer businesses
- NEVER claim input VAT exceeding VND 300 million on a single permitted passenger vehicle
- NEVER claim input VAT without a valid e-invoice (post-1 July 2022 mandate)
- NEVER apply the 8% temporary reduction to excluded categories (telecoms, banking, insurance, real estate, etc.)
- NEVER confuse zero-rated supplies (input VAT fully recoverable) with exempt supplies (input VAT NOT recoverable)
- NEVER request a VAT refund if accumulated excess input VAT is below VND 300 million
- NEVER apply the credit method for a taxpayer that has not been approved/eligible for it -- direct method taxpayers cannot claim input VAT
- NEVER confuse the FCT VAT component (withheld by Vietnamese party) with regular output VAT
- NEVER accept paper invoices as valid for input VAT credit after the e-invoicing mandate (1 July 2022), unless emergency paper invoice procedures were properly followed
- NEVER ignore the de minimis rule -- if non-creditable portion < 5%, full credit is allowed
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

If you are adapting this skill for another ASEAN jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace Form 01/GTGT items with the equivalent form structure for your jurisdiction.
3. Replace VAT rates with your jurisdiction's standard and reduced rates.
4. Replace the registration thresholds with your jurisdiction's equivalents.
5. Replace the blocked categories with your jurisdiction's equivalent non-creditable categories.
6. Have a licensed tax practitioner in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases to the Edge Case Registry.
8. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
