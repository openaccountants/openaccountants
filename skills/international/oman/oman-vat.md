---
name: oman-vat
description: Use this skill whenever asked to prepare, review, or create an Oman VAT return for any client. Trigger on phrases like "prepare VAT return", "Oman VAT", "Tax Authority return", "file VAT Oman", or any request involving Oman VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Oman VAT classification rules, return structure, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Oman VAT-related work.
---

# Oman VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Sultanate of Oman |
| Jurisdiction Code | OM |
| Primary Legislation | Royal Decree No. 121/2020 (VAT Law) |
| Supporting Legislation | Ministerial Decision No. 53/2021 (Executive Regulations); Ministerial Decision No. 54/2021 (blocked input tax); GCC Unified VAT Agreement |
| Tax Authority | Oman Tax Authority (OTA) |
| Filing Portal | https://www.taxoman.gov.om (Tax Authority Portal) |
| Standard VAT Rate | 5% |
| Currency | Omani Rial (OMR) |
| VAT Effective Date | 16 April 2021 |
| Contributor | Open Accounting Skills Registry |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Validated By | Deep research verification, April 2026 |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption, sector-specific treatment. Tier 3: complex group structures, non-standard supplies. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed tax advisor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax advisor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT registration number (VATIN)** [T1] -- Format: OM + numeric sequence issued by OTA
2. **VAT registration type** [T1] -- Mandatory (taxable supplies > OMR 38,500), Voluntary (taxable supplies or expenditure > OMR 19,250), or Group registration
3. **VAT period** [T1] -- Monthly or Quarterly (assigned by OTA based on turnover)
4. **Industry/sector** [T2] -- Impacts zero-rating and exemption classification (e.g., oil/gas, financial services, healthcare, education, tourism)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (pro-rata rate needed; reviewer must confirm rate)
6. **Does the business trade goods for resale?** [T1] -- Impacts classification of purchases
7. **Excess credit brought forward** [T1] -- From prior period
8. **Is the business in a free zone or special economic zone?** [T2] -- May affect treatment of supplies
9. **Does the client import goods into Oman?** [T1] -- Impacts customs VAT treatment
10. **Is the client part of a VAT group?** [T2] -- Intra-group supplies may be disregarded

**Legislation:** Royal Decree No. 121/2020, Articles 1-10 (definitions and scope); Articles 51-56 (registration).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, contractor payments, tax payments, loan repayments, dividends, bank charges (margin-based) = OUT OF SCOPE (never on VAT return)
- **Legislation:** Royal Decree No. 121/2020, Article 2 (definitions); Article 16 (supply of goods); Article 17 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Oman (local): supplier/customer registered with OTA or located in Oman
- GCC Implementing States: Saudi Arabia (SA), UAE (AE), Bahrain (BH) -- states that have implemented VAT under the GCC Unified VAT Agreement
- GCC Non-Implementing States: Kuwait (KW), Qatar (QA) -- treated as non-GCC for VAT purposes
- Non-GCC: all other countries (US, UK, EU, India, etc.)
- **Legislation:** Royal Decree No. 121/2020, Articles 18-23 (place of supply); GCC Unified VAT Agreement

### 1c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Standard rate: 5%
- Zero rate: 0% (with input VAT recovery)
- Exempt: no VAT charged, no input VAT recovery
- Out of scope: not a supply for VAT purposes
- **Legislation:** Royal Decree No. 121/2020, Article 41 (standard rate); Article 42 (zero-rated); Article 47 (exempt)

### 1d. Determine Expense Category [T1]
- Capital goods: significant assets used in the business over time
- Resale: goods bought to literally resell
- Overhead/services: everything else
- **Legislation:** Royal Decree No. 121/2020, Article 60 (input tax deduction)

---

## Step 2: VAT Return Form Structure (OTA Form) [T1]

The Oman VAT return is filed electronically via the OTA portal. The form consists of the following sections:

### Section 1: Output Tax (Sales)

| Box | Description | Rate | Notes |
|-----|-------------|------|-------|
| Box 1 | Standard rated supplies | 5% | Domestic taxable supplies at standard rate |
| Box 2 | Supplies to registered customers in GCC implementing states | 5% | Intra-GCC to VAT-registered |
| Box 3 | Zero-rated supplies | 0% | Exports, international transport, healthcare, education, etc. |
| Box 4 | Exempt supplies | -- | Financial services (margin), bare land, residential |
| Box 5 | Deemed supplies | 5% | Self-supplies, gifts exceeding OMR 25 |
| Box 6 | Total supplies | -- | Sum of Boxes 1-5 |
| Box 7 | Output VAT on standard rated supplies | -- | VAT on Boxes 1, 2, and 5 |

### Section 2: Input Tax (Purchases)

| Box | Description | Rate | Notes |
|-----|-------------|------|-------|
| Box 8 | Standard rated domestic purchases | 5% | Local purchases at standard rate |
| Box 9 | Imports of goods | 5% | Goods imported through customs |
| Box 10 | Reverse charge on services | 5% | Services from non-residents |
| Box 11 | Purchases from GCC implementing states | 5% | Intra-GCC acquisitions |
| Box 12 | Total purchases | -- | Sum of Boxes 8-11 |
| Box 13 | Total input VAT | -- | Recoverable input tax |

### Section 3: Adjustments and Net Tax

| Box | Description | Notes |
|-----|-------------|-------|
| Box 14 | Corrections from previous periods (output) | Adjustments to output tax |
| Box 15 | Corrections from previous periods (input) | Adjustments to input tax |
| Box 16 | Net VAT due | Box 7 - Box 13 + Box 14 - Box 15 |

**Legislation:** Royal Decree No. 121/2020, Article 67 (VAT return); Executive Regulations, Chapter 8.

---

## Step 3: Supply Classification Matrix [T1]

### Zero-Rated Supplies (0% VAT, input tax recoverable)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods physically exported from Oman | Article 42(1) |
| Exports of services | Services supplied to non-resident outside Oman | Article 42(2) |
| International transport | Transport of goods or passengers departing/arriving Oman | Article 43(a) |
| Oil and gas | Crude oil, natural gas, hydrocarbons | Article 43(b) |
| First supply of residential property | First sale or lease within 3 years of completion | Article 43(c) |
| Precious metals (investment) | Gold, silver, platinum (99%+ purity) for investment | Article 43(d) |
| Healthcare | Preventive and curative healthcare on approved list | Article 43(e) |
| Education | Licensed educational institutions, curriculum-based | Article 43(f) |
| Basic food items | Items on government-approved list (Decision No. 56/2021) | Article 43(g) |
| Water and electricity | Supply of water and electricity for domestic consumption | Article 43(h) |

### Exempt Supplies (no VAT charged, no input tax recovery)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Financial services (margin-based) | Interest, spreads, implicit margins on banking/insurance | Article 47(1) |
| Bare land | Undeveloped land | Article 47(2) |
| Residential property (subsequent) | Subsequent sale or lease of residential property | Article 47(3) |
| Life insurance | Life insurance and reinsurance | Article 47(4) |
| Local passenger transport | Public transport within Oman | Article 47(5) |

### Out of Scope

| Category | Notes |
|----------|-------|
| Salaries and wages | Employment relationship, not a supply |
| Dividends and profit distributions | Return on investment |
| Government fees and fines | Sovereign functions |
| Intra-group supplies (VAT group) | Disregarded if within approved VAT group (Article 59) |
| Statutory compensation | Court-ordered payments |

**Legislation:** Royal Decree No. 121/2020, Articles 42-47.

---

## Step 4: Reverse Charge Mechanics [T1]

### When Reverse Charge Applies

The recipient accounts for VAT (reverse charge) when:
1. Services received from a non-resident supplier who does not have a fixed establishment in Oman
2. Goods imported under the reverse charge mechanism (certain GCC scenarios)

**Legislation:** Royal Decree No. 121/2020, Article 58 (reverse charge on services from non-residents); Article 59 (deemed imports).

### Reverse Charge Steps

For services received from non-resident suppliers:
1. Report net value in Box 10 (reverse charge on services)
2. Self-assess output VAT at 5% -- include in Box 7
3. Claim input VAT at 5% -- include in Box 13
4. Net effect: zero for fully taxable businesses

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Services consumed outside Oman: place of supply is outside Oman
- Supplier registered for VAT in Oman: supplier charges Oman VAT directly
- Intra-group supplies (VAT group): disregarded

### GCC Reverse Charge (Transitional) [T2]

Supplies between GCC implementing states follow transitional rules under the GCC Unified VAT Agreement:
- Customer registered in Oman receiving goods from another GCC implementing state: reverse charge applies
- Customer not registered: supplier charges VAT in originating state
- **Flag for reviewer:** GCC transitional provisions are evolving. Confirm with advisor for cross-GCC transactions.

**Legislation:** GCC Unified VAT Agreement, Chapter 3; Royal Decree No. 121/2020, Articles 58-59.

---

## Step 5: Input Tax (Deductibility) Rules

### General Rule [T1]

Input VAT is recoverable if the purchase is used to make taxable supplies (standard-rated or zero-rated). Input VAT is NOT recoverable if the purchase is used to make exempt supplies or is for non-business purposes.

**Legislation:** Royal Decree No. 121/2020, Article 60 (right to deduct); Article 61 (conditions).

### Blocked Input Tax [T1]

The following categories have ZERO VAT recovery regardless of business use:

| Category | Description | Legislation |
|----------|-------------|-------------|
| Entertainment | Hospitality, recreation, entertainment expenses | Ministerial Decision No. 54/2021, Item 1 |
| Motor vehicles | Private motor vehicles (passenger cars) | Ministerial Decision No. 54/2021, Item 2 |
| Fuel for blocked vehicles | Fuel for private motor vehicles | Ministerial Decision No. 54/2021, Item 3 |
| Tobacco and related products | All tobacco purchases | Ministerial Decision No. 54/2021, Item 4 |
| Personal use | Non-business consumption | Royal Decree No. 121/2020, Article 61(2) |

### Motor Vehicle Exceptions [T2]

Input VAT on motor vehicles IS recoverable if:
- Vehicle is stock in trade (car dealer)
- Vehicle used exclusively for taxable business (delivery, taxi, car rental fleet)
- Vehicle used for employee transport (contractual obligation)

**Flag for reviewer:** Must confirm exclusive business use.

### Blocked Categories Override Partial Exemption [T1]

Check blocked status FIRST. If blocked, recovery is zero even if business is fully taxable.

### Registration-Based Recovery [T1]
- VAT-registered (mandatory or voluntary): full recovery (subject to blocked list and apportionment)
- Not VAT-registered: no recovery

### Partial Exemption (Mixed Use) [T2]

If business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

**Legislation:** Royal Decree No. 121/2020, Article 62 (apportionment); Executive Regulations, Chapter 7.

**Flag for reviewer:** Pro-rata must be confirmed by licensed tax advisor. Annual adjustment required under Article 62(3).

---

## Step 6: VAT Rates Summary Table [T1]

| Rate | Application | Input Recovery |
|------|-------------|----------------|
| 5% (standard) | All taxable supplies not zero-rated or exempt | Yes (subject to blocked list) |
| 0% (zero-rated) | Exports, international transport, oil/gas, healthcare, education, basic food, first residential, water/electricity | Yes |
| Exempt | Financial services (margin), bare land, subsequent residential, life insurance, local transport | No |
| Out of scope | Salaries, dividends, government fees, intra-group (VAT group) | N/A |

**Legislation:** Royal Decree No. 121/2020, Articles 41-47.

---

## Step 7: Registration Thresholds [T1]

| Threshold | Amount | Legislation |
|-----------|--------|-------------|
| Mandatory registration | OMR 38,500 (taxable supplies in prior 12 months or expected next 30 days) | Article 51(1) |
| Voluntary registration | OMR 19,250 (taxable supplies or taxable expenditure in prior 12 months) | Article 51(2) |
| Group registration | Two or more legal persons related by ownership (50%+) or control | Article 59 |
| Non-resident registration | No threshold -- must register if making taxable supplies in Oman | Article 53 |
| Deregistration | Turnover falls below OMR 19,250 for 12 consecutive months | Article 55 |

**Legislation:** Royal Decree No. 121/2020, Articles 51-56.

---

## Step 8: Filing Deadlines and Penalties [T1]

### Filing Frequency

| Criteria | Period | Deadline |
|----------|--------|----------|
| Annual turnover > OMR 1,000,000 | Monthly | Last day of month following the tax period |
| Annual turnover <= OMR 1,000,000 | Quarterly | Last day of month following the quarter end |
| Voluntary registrants | Quarterly | Last day of month following the quarter end |

### Quarterly Periods

| Quarter | Period | Filing Deadline |
|---------|--------|-----------------|
| Q1 | 1 Jan -- 31 Mar | 30 April |
| Q2 | 1 Apr -- 30 Jun | 31 July |
| Q3 | 1 Jul -- 30 Sep | 31 October |
| Q4 | 1 Oct -- 31 Dec | 31 January |

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | OMR 25 per day, maximum OMR 5,000 per return | Article 99(1) |
| Late payment | 1% per month of unpaid tax | Article 99(2) |
| Failure to register | OMR 5,000 + backdated VAT liability | Article 98(1) |
| Incorrect return (negligence) | Fine of OMR 1,000 -- OMR 10,000 | Article 100(1) |
| Incorrect return (fraud/evasion) | 300% of tax evaded + criminal prosecution | Article 100(2) |
| Failure to keep records | OMR 1,000 -- OMR 5,000 | Article 101 |
| Failure to issue tax invoice | OMR 500 -- OMR 5,000 per invoice | Article 102 |

**Legislation:** Royal Decree No. 121/2020, Articles 96-105 (Penalties).

---

## Step 9: Tax Invoice Requirements [T1]

### Full Tax Invoice

| Field | Requirement |
|-------|-------------|
| Invoice number | Sequential, unique |
| Date of issue | Date invoice is issued |
| Date of supply | If different from date of issue |
| Supplier name, address, VATIN | As registered with OTA |
| Customer name, address, VATIN | For B2B supplies |
| Description of goods/services | Sufficient detail |
| Quantity | For goods |
| Unit price (exclusive of VAT) | Net amount |
| Discount | If applicable |
| VAT rate | 5%, 0%, or Exempt |
| VAT amount | In OMR |
| Total amount (inclusive of VAT) | Gross amount |
| Currency | OMR or foreign with OMR equivalent |

### Simplified Tax Invoice (supplies < OMR 500)

| Field | Requirement |
|-------|-------------|
| Invoice number | Sequential, unique |
| Date of issue | Date of issue |
| Supplier name and VATIN | As registered |
| Description of goods/services | Brief description |
| Total amount (inclusive of VAT) | Gross amount |
| Statement of VAT inclusion | "Inclusive of VAT at 5%" |

**Legislation:** Royal Decree No. 121/2020, Article 45 (tax invoices); Executive Regulations, Chapter 6.

### Upcoming: Mandatory E-Invoicing [T2]

In May 2025, OTA signed an agreement to develop a national e-invoicing system. Mandatory e-invoicing is planned to begin in a phased manner from Q3 2026, with full implementation expected by 2028. Businesses should begin preparation for e-invoicing integration.

**Note:** Decision No. 81/2025 expanded VAT refund eligibility to purchases made by the armed forces/security agencies and introduced a tourist VAT refund scheme for non-resident visitors.

---

## Step 10: Capital Goods Adjustment [T2]

Oman applies a capital goods adjustment mechanism for significant assets:

- **Real property (land and buildings):** Adjustment period of 10 years from acquisition
- **Other capital assets (> OMR 5,000):** Adjustment period of 5 years from acquisition
- If the use of a capital asset changes between taxable and exempt activities, input tax must be adjusted proportionally for each remaining year

**Flag for reviewer:** Capital goods adjustment calculations require professional review. Must track use year-by-year.

**Legislation:** Royal Decree No. 121/2020, Article 63; Executive Regulations, Chapter 7.

---

## Step 11: Deemed Supplies [T1]

A deemed supply (self-supply) occurs when:

| Situation | Treatment | Legislation |
|-----------|-----------|-------------|
| Business gifts exceeding OMR 25 per recipient per year | Deemed supply at market value, output VAT due | Article 25 |
| Goods/services applied to non-business use | Deemed supply at cost, output VAT due | Article 26 |
| Transfer of goods between branches (cross-border) | May be treated as deemed supply | Article 27 |
| Cessation of VAT registration while holding stock | Deemed supply on stock held, output VAT due | Article 28 |

**Legislation:** Royal Decree No. 121/2020, Articles 25-28.

---

## Step 12: Specific Sector Rules

### Oil and Gas Sector [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Crude oil exports | Zero-rated | Article 43(b) |
| Natural gas (domestic supply) | Zero-rated | Article 43(b) |
| Refined petroleum products (domestic sale) | Standard rated (5%) | Article 41 |
| Oilfield services to non-residents | Zero-rated (export of services) | Article 42(2) |
| Oilfield equipment imports | Standard rated, input recoverable | Article 60 |

### Financial Services [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Interest on loans (margin-based) | Exempt | Article 47(1) |
| Fee-based services (explicit charges) | Standard rated (5%) | Article 41 |
| Foreign exchange (spread) | Exempt | Article 47(1) |
| Foreign exchange (explicit commission) | Standard rated (5%) | Article 41 |
| Insurance premiums (general) | Standard rated (5%) | Article 41 |
| Life insurance | Exempt | Article 47(4) |
| Islamic finance (murabaha, ijara) | Treated same as conventional equivalent | Executive Regulations, Chapter 3 |

**Flag for reviewer:** Islamic finance products must be mapped to their conventional equivalent for VAT treatment. Confirm with advisor.

### Real Estate [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| First supply of residential property (within 3 years) | Zero-rated | Article 43(c) |
| Subsequent supply/lease of residential property | Exempt | Article 47(3) |
| Commercial property (sale or lease) | Standard rated (5%) | Article 41 |
| Bare land | Exempt | Article 47(2) |
| Construction of new residential building | Zero-rated | Article 43(c) |
| Hotel/short-term accommodation | Standard rated (5%) | Article 41 |

### Healthcare [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Preventive healthcare | Zero-rated | Article 43(e) |
| Curative healthcare (approved list) | Zero-rated | Article 43(e) |
| Cosmetic/elective procedures | Standard rated (5%) | Article 41 |
| Pharmaceuticals (approved list) | Zero-rated | Article 43(e) |
| Non-listed medical supplies | Standard rated (5%) | Article 41 |

### Education [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Licensed institutions (curriculum-based) | Zero-rated | Article 43(f) |
| Related educational goods/services | Zero-rated | Article 43(f) |
| Commercial training/professional development | Standard rated (5%) | Article 41 |
| Private tutoring (not licensed institution) | Standard rated (5%) | Article 41 |

### Tourism [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Hotel accommodation | Standard rated (5%) | Article 41 |
| Tourism services (guided tours) | Standard rated (5%) | Article 41 |
| Tourist refund scheme | Available for eligible tourists (> OMR 25 per purchase) | Article 71 |

---

## Step 13: Record Keeping Requirements [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Retention period | 10 years from end of tax period | Article 64(3) |
| Language | Arabic required; bilingual (Arabic/English) acceptable | Article 64(2) |
| Format | Paper or electronic; accessible within Oman | Article 64(1) |
| Records required | Tax invoices, credit/debit notes, import documents, contracts, accounting records | Article 64(1) |

**Legislation:** Royal Decree No. 121/2020, Article 64.

---

## Step 14: Derived Box Calculations [T1]

```
Box 6  = Box 1 + Box 2 + Box 3 + Box 4 + Box 5
Box 7  = (Box 1 * 5%) + (Box 2 * 5%) + (Box 5 * 5%)
Box 12 = Box 8 + Box 9 + Box 10 + Box 11
Box 13 = Recoverable input tax on (Box 8 + Box 9 + Box 10 + Box 11), subject to blocked list and apportionment
Box 16 = Box 7 - Box 13 + Box 14 - Box 15

IF Box 16 > 0 THEN
  Tax payable = Box 16
ELSE
  Tax refundable = |Box 16|
  (Carry forward or request refund per Article 68)
END
```

**Legislation:** Royal Decree No. 121/2020, Articles 67-68.

---

## Step 15: Refund Mechanism [T1]

| Scenario | Treatment | Legislation |
|----------|-----------|-------------|
| Excess input tax | Carry forward (default) or request refund | Article 68(1) |
| Refund request processing | OTA has 60 days to process | Article 68(2) |
| Tourist refund scheme | Available for non-resident visitors (minimum purchase OMR 25) | Article 71 |
| Diplomatic/international organization refund | Refund available based on reciprocity | Article 72 |

**Legislation:** Royal Decree No. 121/2020, Articles 68-72.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the facts and legislation
- NEVER apply input tax recovery on blocked categories (entertainment, private motor vehicles, tobacco, personal use)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER allow unregistered persons to claim input VAT
- NEVER file a return without confirming the filing period and registration type
- NEVER classify financial services without distinguishing margin-based (exempt) from fee-based (standard rated)
- NEVER classify Islamic finance products without mapping to conventional equivalent
- NEVER classify residential property without confirming first supply within 3 years
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER ignore GCC transitional rules for cross-border GCC supplies
- NEVER accept an invoice without Arabic text as valid for Oman VAT purposes
- NEVER overlook the 10-year record retention requirement (longer than most GCC states)

---

## Step 16: Edge Case Registry

### EC1 -- Service received from non-resident, no Oman VAT [T1]
**Situation:** Oman business receives IT services from an Indian company. Invoice in USD, no Oman VAT.
**Resolution:** Reverse charge applies. Self-assess output VAT at 5% and claim input VAT at 5%. Report in Box 10 and include in Boxes 7 and 13. Net effect zero for fully taxable business.
**Legislation:** Royal Decree No. 121/2020, Article 58.

### EC2 -- Cross-GCC supply from UAE [T2]
**Situation:** Oman business purchases equipment from UAE supplier. UAE supplier is VAT-registered. Goods shipped UAE to Oman.
**Resolution:** Under GCC transitional rules, reverse charge applies. Report in Box 11. Flag for reviewer: confirm UAE supplier does not have Oman VAT registration.
**Legislation:** GCC Unified VAT Agreement, Chapter 3.

### EC3 -- Deemed supply: business gift exceeding OMR 25 [T1]
**Situation:** Company gives promotional gifts worth OMR 50 each to clients during Eid.
**Resolution:** Deemed supply. Output VAT due on market value (OMR 50 x 5% = OMR 2.50 per gift). Report in Box 5.
**Legislation:** Royal Decree No. 121/2020, Article 25.

### EC4 -- Islamic finance: murabaha transaction [T2]
**Situation:** Islamic bank provides murabaha financing. Customer pays cost-plus markup.
**Resolution:** The markup is treated as the equivalent of interest for VAT purposes. If the margin is implicit (no separate fee), it is exempt. If there is an explicit processing fee, the fee is standard rated at 5%. Flag for reviewer: confirm the specific structure of the Islamic finance product.
**Legislation:** Executive Regulations, Chapter 3 (Islamic finance equivalence).

### EC5 -- Free zone entity selling to mainland [T2]
**Situation:** Business in Duqm Special Economic Zone sells goods to customer in Muscat.
**Resolution:** Free zones in Oman may be designated as "special zones" with specific VAT treatment. Goods moving from a designated zone to mainland are treated as imports. Flag for reviewer: confirm designation of the specific zone and applicable rules.
**Legislation:** Royal Decree No. 121/2020, Article 35 (designated zones).

### EC6 -- Credit notes [T1]
**Situation:** Client issues credit note for partial refund on previous sale.
**Resolution:** Credit note reduces original output VAT. Reduce Box 1 and Box 7. Credit note must reference original invoice.
**Legislation:** Royal Decree No. 121/2020, Article 46.

### EC7 -- Imports of goods via Oman Customs [T1]
**Situation:** Business imports raw materials from China. Customs collects 5% VAT at border.
**Resolution:** VAT paid to Customs is recoverable input tax. Report in Box 9, claim in Box 13. Retain customs declaration.
**Legislation:** Royal Decree No. 121/2020, Articles 30-31 (imports); Article 60.

### EC8 -- Motor vehicle for taxi/delivery fleet [T1]
**Situation:** Taxi company purchases sedans for taxi service.
**Resolution:** Input VAT IS recoverable. Taxis are excepted from the motor vehicle block if used exclusively for the licensed taxi business.
**Legislation:** Ministerial Decision No. 54/2021, Item 2 (exception).

### EC9 -- Water and electricity for commercial premises [T1]
**Situation:** Office building receives water and electricity bill from utility company.
**Resolution:** Water and electricity for commercial (non-domestic) consumption is standard rated at 5%. Input VAT is recoverable. The zero-rate applies only to domestic residential consumption.
**Legislation:** Royal Decree No. 121/2020, Article 43(h) (domestic only).

### EC10 -- Pre-registration input tax [T1]
**Situation:** Business registered 1 June 2025. Claims input VAT on inventory purchased 15 March 2025. Inventory still held at registration date.
**Resolution:** Input VAT on goods in stock at registration date is recoverable if purchased within 5 years before registration. Services: recoverable if received within 6 months before registration.
**Legislation:** Royal Decree No. 121/2020, Article 61(4).

### EC11 -- Tourist refund [T1]
**Situation:** Tourist from Germany purchases OMR 200 of goods from a retail store and departs Oman.
**Resolution:** Tourist is eligible for VAT refund under the tourist refund scheme. Retailer must issue a special tax-free shopping document. Tourist claims refund at departure point.
**Legislation:** Royal Decree No. 121/2020, Article 71.

### EC12 -- Bad debt relief [T2]
**Situation:** Client has an unpaid invoice for more than 12 months. Customer is insolvent.
**Resolution:** Bad debt relief available if: (i) output VAT was accounted for, (ii) 12 months since supply, (iii) debt written off in accounts, (iv) reasonable collection efforts made. Flag for reviewer: confirm all conditions.
**Legislation:** Royal Decree No. 121/2020, Article 38.

---

## Step 17: EU VAT Comparison [T1]

| Feature | Oman | EU (Directive 2006/112/EC) |
|---------|------|---------------------------|
| Standard rate | 5% | 15-27% (varies) |
| Registration threshold | OMR 38,500 (~EUR 90,000) | Varies (EUR 0 to EUR 85,000) |
| Reverse charge (imports of services) | Yes (Article 58) | Yes (Article 196) |
| Intra-community/GCC supply | GCC transitional rules | Intra-community supply rules |
| Capital goods adjustment | 5/10 years | 5/10/20 years |
| Bad debt relief | Yes (12 months) | Varies |
| Group registration | Yes (Article 59) | Yes (Article 11) |
| Islamic finance provision | Yes (explicit equivalence) | No |
| Tourist refund scheme | Yes (Article 71) | Yes (Article 170) |
| Record retention | 10 years | 5-10 years (varies) |
| Electronic filing | Mandatory | Varies |
| Zero-rated basic food | Yes | Some states (0% or reduced rate) |

---

## Step 18: Test Suite

### Test 1 -- Standard local purchase, 5% VAT
**Input:** Oman supplier, office supplies, OMR 105 gross, VAT OMR 5, net OMR 100. Fully taxable business.
**Expected output:** Box 8 = OMR 100. Box 13 includes OMR 5. Input VAT recoverable.

### Test 2 -- Reverse charge on services from non-resident
**Input:** US supplier (Microsoft), annual license OMR 500, no VAT on invoice. Fully taxable business.
**Expected output:** Box 10 = OMR 500. Output VAT OMR 25 in Box 7. Input VAT OMR 25 in Box 13. Net = zero.

### Test 3 -- Export of goods (zero-rated)
**Input:** Client exports fish products to Japan. Invoice OMR 10,000. Export documentation complete.
**Expected output:** Box 3 = OMR 10,000. No output VAT. Input on related purchases recoverable.

### Test 4 -- Exempt financial service
**Input:** Bank earns OMR 200,000 in interest margin income.
**Expected output:** Box 4 = OMR 200,000. No output VAT. Input on related costs NOT recoverable.

### Test 5 -- Blocked motor vehicle
**Input:** Company buys sedan for director. OMR 8,000 net + OMR 400 VAT.
**Expected output:** Box 8 = OMR 8,000. Box 13 does NOT include OMR 400. VAT BLOCKED.

### Test 6 -- Deemed supply: business gift
**Input:** Company gives 100 gifts at OMR 40 each to customers (total OMR 4,000).
**Expected output:** Box 5 = OMR 4,000. Output VAT = OMR 200. Gifts exceed OMR 25 threshold.

### Test 7 -- First supply of residential property (zero-rated)
**Input:** Developer sells new villa (completed 2 years ago) for OMR 120,000.
**Expected output:** Box 3 = OMR 120,000. Zero-rated. Input VAT on construction recoverable.

### Test 8 -- Healthcare (zero-rated)
**Input:** Hospital provides listed treatment. Fee OMR 3,000.
**Expected output:** Box 3 = OMR 3,000. Zero-rated. Input VAT recoverable.

### Test 9 -- Credit note adjustment
**Input:** Credit note for OMR 1,000 + OMR 50 VAT on previous standard-rated sale.
**Expected output:** Box 1 reduced by OMR 1,000. Box 7 reduced by OMR 50.

### Test 10 -- Water/electricity for commercial premises
**Input:** Office electricity bill OMR 200 + OMR 10 VAT.
**Expected output:** Box 8 = OMR 200. Box 13 includes OMR 10. Standard rated (commercial use, not domestic zero-rate).

### Test 11 -- Mixed-use purchase (partial exemption)
**Input:** Company makes 80% taxable, 20% exempt supplies. Office rent OMR 5,000 + OMR 250 VAT.
**Expected output:** Box 8 = OMR 5,000. Box 13 includes OMR 200 (80% of OMR 250). Recovery restricted.

### Test 12 -- Late filing penalty
**Input:** Quarterly return for Q3 2025 due 31 October 2025. Filed 15 November 2025. Tax payable OMR 3,000.
**Expected output:** Late filing penalty: OMR 25/day x 15 days = OMR 375. Late payment penalty: 1% x OMR 3,000 = OMR 30 (one month). Total penalty = OMR 405.

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
Action Required: Licensed tax advisor must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax advisor. Document gap.
```

---

## Step 20: Place of Supply Rules [T1]

| Type of Supply | Place of Supply | Legislation |
|----------------|----------------|-------------|
| Goods (no transport) | Where goods are located at time of supply | Article 18(1) |
| Goods (with transport) | Where transport begins | Article 18(2) |
| Goods (installed/assembled) | Where installation/assembly takes place | Article 18(3) |
| Services (general rule) | Where supplier has place of residence | Article 20(1) |
| Services (B2B) | Where customer has place of residence | Article 20(2) |
| Real estate services | Where property is located | Article 21 |
| Transport services | Where transport takes place | Article 22 |
| Telecommunications/electronic services (B2C) | Where customer uses/enjoys the service | Article 23 |
| Restaurant/catering services | Where physically performed | Article 23 |

**Legislation:** Royal Decree No. 121/2020, Articles 18-23.

---

## Step 21: Time of Supply Rules [T1]

| Scenario | Tax Point | Legislation |
|----------|-----------|-------------|
| Goods (general) | Earlier of delivery or payment | Article 24(1) |
| Services (general) | Earlier of completion or payment | Article 24(2) |
| Continuous supply | Each payment or invoice date | Article 24(3) |
| Imported goods | Date of customs declaration | Article 30 |
| Reverse charge services | Earlier of payment or invoice from supplier | Article 58 |

**Legislation:** Royal Decree No. 121/2020, Articles 24, 30, 58.

---

## Contribution Notes

If you are adapting this skill for another jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all box numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the registration thresholds with your jurisdiction's equivalent.
5. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
6. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases for known ambiguous situations in your jurisdiction.
8. Run all test suite cases against your jurisdiction's rules.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
