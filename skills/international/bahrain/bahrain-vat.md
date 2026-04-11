---
name: bahrain-vat
description: Use this skill whenever asked to prepare, review, or create a Bahrain VAT return for any client. Trigger on phrases like "prepare VAT return", "Bahrain VAT", "NBR return", "file VAT Bahrain", or any request involving Bahrain VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Bahrain VAT classification rules, return box mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Bahrain VAT-related work.
---

# Bahrain VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Kingdom of Bahrain |
| Jurisdiction Code | BH |
| Primary Legislation | Decree-Law No. 48 of 2018 (VAT Law) |
| Supporting Legislation | Resolution No. 12 of 2018 (Executive Regulations); Resolution No. 33 of 2021 (rate increase to 10%); Ministerial Order No. 14 of 2019 (blocked input tax) |
| Tax Authority | National Bureau for Revenue (NBR) |
| Filing Portal | https://www.nbr.gov.bh (NBR Portal) |
| Standard VAT Rate | 10% (effective 1 January 2022; previously 5%) |
| Currency | Bahraini Dinar (BHD) |
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

1. **Entity name and VAT registration number** [T1] -- Format: 13-digit TIN issued by NBR
2. **VAT registration type** [T1] -- Mandatory (turnover exceeds BHD 37,500), Voluntary (turnover exceeds BHD 18,750), or Group registration
3. **VAT period** [T1] -- Monthly (turnover > BHD 3,000,000) or Quarterly (all others)
4. **Industry/sector** [T2] -- Impacts zero-rating and exemption classification (e.g., oil/gas, financial services, healthcare, education)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (pro-rata rate needed; reviewer must confirm rate)
6. **Does the business trade goods for resale?** [T1] -- Impacts classification of purchases
7. **Excess credit brought forward** [T1] -- From prior period
8. **Is the business in the oil and gas sector?** [T1] -- Specific zero-rating rules under Article 68 of the VAT Law
9. **Does the client import goods into Bahrain?** [T1] -- Impacts customs VAT treatment
10. **Is the client part of a VAT group?** [T2] -- Intra-group supplies are outside scope if so

**Legislation:** Decree-Law No. 48/2018, Articles 2-5 (definitions and scope); Article 39 (registration).

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, contractor payments, tax payments, loan repayments, dividends, bank charges (margin-based) = OUT OF SCOPE (never on VAT return)
- **Legislation:** Decree-Law No. 48/2018, Article 2 (definitions of taxable supply); Article 14 (supply of goods); Article 15 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Bahrain (local): supplier/customer registered with NBR
- GCC Implementing States: Saudi Arabia (SA), UAE (AE), Oman (OM) -- states that have implemented VAT under the GCC Unified VAT Agreement
- GCC Non-Implementing States: Kuwait (KW), Qatar (QA) -- treated as non-GCC for VAT purposes until they implement VAT
- Non-GCC: all other countries (US, UK, EU, India, etc.)
- **Legislation:** Decree-Law No. 48/2018, Article 11 (place of supply); GCC Unified VAT Agreement, Chapter 2

### 1c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Standard rate: 10%
- Zero rate: 0% (with input VAT recovery)
- Exempt: no VAT charged, no input VAT recovery
- Out of scope: not a supply for VAT purposes
- **Legislation:** Decree-Law No. 48/2018, Article 56 (standard rate); Article 59 (zero-rated); Article 64 (exempt)

### 1d. Determine Expense Category [T1]
- Capital goods: significant assets used in the business over time
- Resale: goods bought to literally resell
- Overhead/services: everything else
- **Legislation:** Decree-Law No. 48/2018, Article 49 (input tax deduction)

---

## Step 2: VAT Return Form Structure (NBR Form) [T1]

The Bahrain VAT return is filed electronically via the NBR portal. The form consists of the following sections:

### Section 1: VAT on Sales (Output Tax)

| Box | Description | Rate | Notes |
|-----|-------------|------|-------|
| Box 1 | Standard rated sales | 10% | Local taxable supplies at standard rate |
| Box 2 | Sales to GCC implementing states (registered customers) | 10% | Intra-GCC supplies to VAT-registered recipients |
| Box 3 | Sales to GCC implementing states (non-registered customers) | 10% | Intra-GCC supplies to non-registered recipients |
| Box 4 | Zero-rated sales | 0% | Exports, international transport, oil/gas, etc. |
| Box 5 | Exempt sales | -- | Financial services (margin), bare land, residential |
| Box 6 | Total sales | -- | Sum of Boxes 1-5 |
| Box 7 | Total output VAT | -- | VAT due on Boxes 1-3 |

### Section 2: VAT on Purchases (Input Tax)

| Box | Description | Rate | Notes |
|-----|-------------|------|-------|
| Box 8 | Standard rated purchases | 10% | Local purchases at standard rate |
| Box 9 | Imports subject to VAT | 10% | Goods imported into Bahrain (customs VAT or reverse charge) |
| Box 10 | Purchases from GCC implementing states | 10% | Intra-GCC acquisitions |
| Box 11 | Zero-rated purchases | 0% | Purchases of zero-rated goods/services |
| Box 12 | Exempt purchases | -- | Purchases of exempt goods/services |
| Box 13 | Total purchases | -- | Sum of Boxes 8-12 |
| Box 14 | Total input VAT | -- | Recoverable input tax on Boxes 8-10 |

### Section 3: Adjustments

| Box | Description | Notes |
|-----|-------------|-------|
| Box 15 | Corrections from previous periods (output) | Adjustments to output tax |
| Box 16 | Corrections from previous periods (input) | Adjustments to input tax |

### Section 4: Net VAT

| Box | Description | Notes |
|-----|-------------|-------|
| Box 17 | Net VAT due | Box 7 - Box 14 + Box 15 - Box 16 |

**Legislation:** Decree-Law No. 48/2018, Article 55 (VAT return); Executive Regulations, Article 30.

---

## Step 3: Supply Classification Matrix [T1]

### Zero-Rated Supplies (0% VAT, input tax recoverable)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods physically exported from Bahrain | Article 59(1) |
| Exports of services | Services provided to non-resident not in Bahrain | Article 59(2) |
| International transport | Transport of goods or passengers departing from or arriving in Bahrain | Article 68(a) |
| Oil and gas sector | Crude oil, natural gas, and related hydrocarbons | Article 68(b) |
| First supply of residential property | First supply/lease within 3 years of completion | Article 68(c) |
| Precious metals (investment grade) | Gold, silver, platinum (99%+ purity) for investment | Article 68(d) |
| Healthcare services | Preventive and basic healthcare; medical goods on approved list | Article 68(e) |
| Education services | Recognised educational institutions; curriculum-based education | Article 68(f) |
| Construction of new residential buildings | Construction services for new residential buildings | Article 68(g) |
| Certain food items | Basic food items on government-approved list (Government Resolution No. 11/2019) | Article 68(h) |

### Exempt Supplies (no VAT charged, no input tax recovery)

| Category | Description | Legislation |
|----------|-------------|-------------|
| Financial services (margin-based) | Banking, insurance, reinsurance where consideration is implicit (interest margins, spreads) | Article 64(1) |
| Bare land | Supply of undeveloped land | Article 64(2) |
| Residential property (subsequent supply) | Subsequent sale or lease of residential property (after first supply/3-year window) | Article 64(3) |
| Life insurance | Life insurance and reinsurance | Article 64(4) |
| Local passenger transport | Licensed public passenger transport within Bahrain | Article 64(5) |

### Out of Scope

| Category | Notes |
|----------|-------|
| Salaries and wages | Employment relationship, not a supply |
| Dividends and profit distributions | Return on investment, not a supply |
| Government fees and fines | Sovereign functions |
| Intra-group supplies (VAT group) | Disregarded if within an approved VAT group (Article 45) |
| Statutory compensation | Court-ordered compensation payments |

**Legislation:** Decree-Law No. 48/2018, Articles 59, 64, 68; Executive Regulations, Articles 15-20.

---

## Step 4: Reverse Charge Mechanics [T1]

### When Reverse Charge Applies

The recipient accounts for VAT (reverse charge) when:
1. Services are received from a supplier who is non-resident and does not have a place of residence in Bahrain
2. Goods are imported where the reverse charge mechanism applies (certain scenarios under the GCC framework)

**Legislation:** Decree-Law No. 48/2018, Article 46 (reverse charge on services from non-residents); Article 47 (deemed supply on import).

### Reverse Charge Mechanics

For services received from non-resident suppliers:
1. Report the net value in Box 9 (imports subject to VAT)
2. Self-assess output VAT at 10% -- include in Box 7 (total output VAT)
3. Claim input VAT at 10% -- include in Box 14 (total input VAT)
4. Net effect: zero for fully taxable businesses

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, dividends, etc.): NEVER reverse charge
- Services consumed outside Bahrain: place of supply is outside Bahrain, no Bahrain VAT
- Supplier has a Bahrain VAT registration: supplier charges Bahrain VAT directly, no reverse charge needed
- Supplies within a VAT group: disregarded for VAT purposes

### GCC Reverse Charge (Transitional) [T2]

Under the GCC Unified VAT Agreement, supplies between implementing states follow transitional rules:
- Customer registered for VAT in Bahrain receiving goods from another GCC implementing state: reverse charge applies
- Customer not registered: supplier in originating state charges VAT
- **Flag for reviewer:** GCC transitional rules are evolving. Confirm treatment with advisor for cross-GCC transactions.

**Legislation:** GCC Unified VAT Agreement, Chapter 3; Decree-Law No. 48/2018, Articles 46-47.

---

## Step 5: Input Tax (Deductibility) Rules

### General Rule [T1]

Input VAT is recoverable if the purchase is used to make taxable supplies (standard-rated or zero-rated). Input VAT is NOT recoverable if the purchase is used to make exempt supplies or is for non-business purposes.

**Legislation:** Decree-Law No. 48/2018, Article 49 (right to deduct input tax); Article 50 (conditions for deduction).

### Blocked Input Tax [T1]

The following categories have ZERO VAT recovery regardless of business use:

| Category | Description | Legislation |
|----------|-------------|-------------|
| Entertainment | Hospitality, recreation, entertainment for non-employees | Ministerial Order No. 14/2019, Article 1(a) |
| Motor vehicles | Private motor vehicles (passenger cars seating < 10) | Ministerial Order No. 14/2019, Article 1(b) |
| Fuel for blocked vehicles | Fuel for private motor vehicles that are themselves blocked | Ministerial Order No. 14/2019, Article 1(c) |
| Personal use | Goods or services for personal (non-business) consumption | Decree-Law No. 48/2018, Article 50(2) |

### Motor Vehicle Exceptions [T2]

Input VAT on motor vehicles IS recoverable if the vehicle is used:
- As stock in trade (car dealership)
- Exclusively for taxable business activities (delivery, taxi, rental)
- For employee transport where contractually required

**Flag for reviewer:** Client must demonstrate exclusive business use. Mixed personal/business use remains blocked.

### Blocked Categories Override Partial Exemption [T1]

Check blocked status FIRST. If blocked, recovery is zero even if the business is fully taxable.

### Registration-Based Recovery [T1]
- VAT-registered (mandatory or voluntary): full recovery (subject to category rules and apportionment)
- Not VAT-registered: no recovery

### Partial Exemption (Mixed Use) [T2]

If business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```

**Legislation:** Decree-Law No. 48/2018, Article 51 (apportionment for mixed supplies); Executive Regulations, Article 27.

**Flag for reviewer:** Pro-rata calculation must be confirmed by licensed tax advisor before applying. Annual adjustment required under Article 51(3).

---

## Step 6: VAT Rates Summary Table [T1]

| Rate | Application | Input Recovery |
|------|-------------|----------------|
| 10% (standard) | All taxable supplies not zero-rated or exempt | Yes (subject to blocked list) |
| 0% (zero-rated) | Exports, international transport, oil/gas, healthcare, education, basic food, first residential, precious metals | Yes |
| Exempt | Financial services (margin), bare land, subsequent residential, life insurance, local transport | No |
| Out of scope | Salaries, dividends, government fees, intra-group (VAT group) | N/A |

**Legislation:** Decree-Law No. 48/2018, Articles 56, 59, 64, 68.

---

## Step 7: Registration Thresholds [T1]

| Threshold | Amount | Legislation |
|-----------|--------|-------------|
| Mandatory registration | BHD 37,500 (taxable supplies in prior 12 months or expected next 30 days) | Article 39(1) |
| Voluntary registration | BHD 18,750 (taxable supplies or taxable expenditure in prior 12 months) | Article 39(2) |
| Group registration | Two or more legal persons related by ownership (50%+) or control | Article 45 |
| Non-resident registration | No threshold -- must register if making taxable supplies in Bahrain (unless customer reverse charges) | Article 40 |
| Deregistration | Turnover falls below BHD 18,750 for 12 consecutive months | Article 43 |

**Legislation:** Decree-Law No. 48/2018, Articles 39-45.

---

## Step 8: Filing Deadlines and Penalties [T1]

### Filing Frequency

| Criteria | Period | Deadline |
|----------|--------|----------|
| Annual turnover > BHD 3,000,000 | Monthly | Last day of month following the tax period |
| Annual turnover <= BHD 3,000,000 | Quarterly | Last day of month following the quarter end |
| Voluntary registrants | Quarterly | Last day of month following the quarter end |

### Quarterly Periods (Calendar Year)

| Quarter | Period | Filing Deadline |
|---------|--------|-----------------|
| Q1 | 1 Jan -- 31 Mar | 30 April |
| Q2 | 1 Apr -- 30 Jun | 31 July |
| Q3 | 1 Jul -- 30 Sep | 31 October |
| Q4 | 1 Oct -- 31 Dec | 31 January |

### Penalties

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | BHD 500 for each incomplete or unfiled return (first offence); doubled for repeat offences | Article 80(1) |
| Late payment | 1% of unpaid tax per day, capped at 100% of the unpaid tax amount | Article 80(2) |
| Failure to register | BHD 5,000 + backdated VAT liability | Article 79(1) |
| Incorrect return (negligence) | 50% of the tax underpaid | Article 81(1) |
| Incorrect return (fraud) | 200% of the tax underpaid + criminal prosecution | Article 81(2) |
| Failure to keep records | BHD 1,000 -- BHD 10,000 | Article 82 |
| Failure to issue tax invoice | BHD 1,000 per invoice | Article 83 |

**Legislation:** Decree-Law No. 48/2018, Articles 79-85 (Penalties and Offences).

---

## Step 9: Tax Invoice Requirements [T1]

A valid tax invoice must contain the following (simplified invoice allowed for supplies < BHD 500):

### Full Tax Invoice

| Field | Requirement |
|-------|-------------|
| Invoice number | Sequential, unique |
| Date of issue | Date the invoice is issued |
| Date of supply | If different from date of issue |
| Supplier name, address, TIN | As registered with NBR |
| Customer name, address, TIN | For B2B supplies |
| Description of goods/services | Sufficient detail to identify supply |
| Quantity | For goods |
| Unit price (exclusive of VAT) | Net amount per unit |
| Discount | If applicable |
| VAT rate | 10%, 0%, or Exempt |
| VAT amount | In BHD |
| Total amount (inclusive of VAT) | Gross amount |

### Simplified Tax Invoice (supplies < BHD 500)

| Field | Requirement |
|-------|-------------|
| Invoice number | Sequential, unique |
| Date of issue | Date of issue |
| Supplier name and TIN | As registered |
| Description of goods/services | Brief description |
| Total amount (inclusive of VAT) | Gross amount |
| VAT rate or statement that VAT is included | Rate or "inclusive of VAT" |

**Legislation:** Decree-Law No. 48/2018, Article 36 (tax invoices); Executive Regulations, Article 14.

---

## Step 10: Capital Goods Scheme [T2]

Bahrain does not have a formal multi-year Capital Goods Scheme adjustment mechanism comparable to the EU. However:

- Input tax on capital assets must be apportioned at the time of acquisition based on intended use (taxable vs. exempt)
- If the use changes significantly, an adjustment may be required under Article 51(3) (annual adjustment for mixed-use assets)
- Real property: adjustments apply for 10 years from acquisition
- Other capital assets: adjustments apply for 5 years from acquisition

**Flag for reviewer:** Capital goods adjustment calculations must be reviewed by a licensed tax advisor. The Executive Regulations provide detailed computation methods.

**Legislation:** Decree-Law No. 48/2018, Article 51(3); Executive Regulations, Article 28.

---

## Step 11: Transitional Rules (5% to 10% Rate Change) [T1]

The VAT rate increased from 5% to 10% effective 1 January 2022 (Resolution No. 33 of 2021). Transitional rules:

| Scenario | Treatment |
|----------|-----------|
| Supply completed before 1 Jan 2022 | 5% rate applies regardless of invoice date |
| Supply completed on/after 1 Jan 2022 | 10% rate applies |
| Continuous supply spanning the change date | Apportion: 5% for portion before 1 Jan 2022, 10% for portion on/after |
| Contract signed before 1 Jan 2022, supply after | 10% applies (unless customer is end consumer and contract is non-adjustable) |
| Advance payments received before 1 Jan 2022 | 5% applies to the advance; 10% applies to balance invoiced after |

**NOTE:** As of April 2026, transitional rules are largely historical. However, corrections to prior periods may still reference the 5% rate.

**Legislation:** Resolution No. 33 of 2021; NBR Transitional Guidance published November 2021.

---

## Step 12: Specific Sector Rules

### Oil and Gas Sector [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Crude oil exports | Zero-rated | Article 68(b) |
| Natural gas for domestic supply | Zero-rated | Article 68(b) |
| Refined petroleum products (domestic sale) | Standard rated (10%) | Article 56 (not listed in zero-rate or exempt) |
| Oilfield services to non-residents | Zero-rated (export of services) | Article 59(2) |
| Oilfield equipment imports | Standard rated, input recoverable | Article 49 |

### Financial Services [T2]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Interest on loans (margin-based) | Exempt | Article 64(1) |
| Fee-based services (explicit charges) | Standard rated (10%) | Article 56 |
| Foreign exchange (margin/spread) | Exempt | Article 64(1) |
| Foreign exchange (explicit commission) | Standard rated (10%) | Article 56 |
| Insurance premiums (general) | Standard rated (10%) | Article 56 |
| Life insurance premiums | Exempt | Article 64(4) |
| Fund management fees | Standard rated (10%) | Article 56 |

**Flag for reviewer:** Financial services classification between exempt (margin-based) and standard-rated (fee-based) requires case-by-case analysis.

### Real Estate [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| First supply of residential property (within 3 years of completion) | Zero-rated | Article 68(c) |
| Subsequent supply/lease of residential property | Exempt | Article 64(3) |
| Commercial property (sale or lease) | Standard rated (10%) | Article 56 |
| Bare land | Exempt | Article 64(2) |
| Construction of new residential building | Zero-rated | Article 68(g) |
| Construction of commercial building | Standard rated (10%) | Article 56 |

### Healthcare [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Preventive healthcare | Zero-rated | Article 68(e) |
| Basic/curative healthcare on approved list | Zero-rated | Article 68(e) |
| Cosmetic/elective procedures | Standard rated (10%) | Article 56 |
| Pharmaceuticals on approved list | Zero-rated | Article 68(e) |
| Non-listed medical supplies | Standard rated (10%) | Article 56 |

### Education [T1]

| Supply | Treatment | Legislation |
|--------|-----------|-------------|
| Licensed educational institution (curriculum-based) | Zero-rated | Article 68(f) |
| Related educational goods and services | Zero-rated | Article 68(f) |
| Commercial training/professional development | Standard rated (10%) | Article 56 |
| Private tutoring (not by licensed institution) | Standard rated (10%) | Article 56 |

---

## Step 13: Record Keeping Requirements [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Retention period | 5 years from end of tax period | Article 52(3) |
| Language | Arabic required; bilingual (Arabic/English) acceptable | Article 52(2) |
| Format | Paper or electronic; must be accessible within Bahrain | Article 52(1) |
| Records required | Tax invoices, credit/debit notes, import documents, contracts, accounting records, bank statements | Article 52(1) |
| Notification of record destruction | Must notify NBR before destroying records | Article 52(4) |

**Legislation:** Decree-Law No. 48/2018, Article 52.

---

## Step 14: Derived Box Calculations [T1]

```
Box 6  = Box 1 + Box 2 + Box 3 + Box 4 + Box 5
Box 7  = (Box 1 * 10%) + (Box 2 * 10%) + (Box 3 * 10%)
Box 13 = Box 8 + Box 9 + Box 10 + Box 11 + Box 12
Box 14 = Recoverable input tax on (Box 8 + Box 9 + Box 10), subject to blocked list and apportionment
Box 17 = Box 7 - Box 14 + Box 15 - Box 16

IF Box 17 > 0 THEN
  Tax payable = Box 17
ELSE
  Tax refundable = |Box 17|
  (Refund may be carried forward or claimed per Article 53)
END
```

**Legislation:** Decree-Law No. 48/2018, Article 55 (returns); Article 53 (refunds).

---

## Step 15: Refund Mechanism [T1]

| Scenario | Treatment | Legislation |
|----------|-----------|-------------|
| Excess input tax | Carry forward to next period (default) or request refund | Article 53(1) |
| Refund request | Filed via NBR portal; NBR has 60 days to process | Article 53(2) |
| Refund for non-resident businesses | Available if no taxable supplies in Bahrain and reciprocity exists | Article 54 |
| Export-dominant businesses | May apply for monthly refund cycle regardless of quarterly filing | Article 53(3) |

**Legislation:** Decree-Law No. 48/2018, Articles 53-54.

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from the facts and legislation
- NEVER apply input tax recovery on blocked categories (entertainment, private motor vehicles, personal use)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER apply the old 5% rate to supplies made on or after 1 January 2022 (unless correcting a prior period)
- NEVER allow unregistered persons to claim input VAT
- NEVER file a return without confirming the filing period and registration type
- NEVER classify financial services without distinguishing margin-based (exempt) from fee-based (standard rated)
- NEVER classify residential property without confirming whether it is a first supply within 3 years
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER ignore the GCC transitional rules for cross-border GCC supplies
- NEVER accept an invoice without Arabic text as a valid tax invoice for Bahrain VAT purposes

---

## Step 16: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Service received from non-resident, no Bahrain VAT charged [T1]
**Situation:** Bahrain-registered business receives consulting services from a UK firm. Invoice shows GBP amount, no Bahrain VAT.
**Resolution:** Reverse charge applies. Self-assess output VAT at 10% and claim input VAT at 10% (if used for taxable supplies). Report in Box 9 and include in Boxes 7 and 14. Net effect zero for fully taxable business.
**Legislation:** Decree-Law No. 48/2018, Article 46.

### EC2 -- GCC supply from UAE supplier [T2]
**Situation:** Bahrain business purchases goods from UAE supplier. UAE supplier is VAT-registered. Goods shipped from UAE to Bahrain.
**Resolution:** Under GCC transitional rules, reverse charge applies. Bahrain customer self-assesses in Box 10. However, if the UAE supplier has a Bahrain VAT registration, the supplier charges Bahrain VAT directly. Flag for reviewer: confirm whether UAE supplier has Bahrain registration.
**Legislation:** GCC Unified VAT Agreement, Chapter 3; Decree-Law No. 48/2018, Article 47.

### EC3 -- Mixed supply: taxable and exempt components [T2]
**Situation:** Bank charges a single fee covering both advisory services (taxable) and interest margin (exempt).
**Resolution:** Must split the supply into taxable and exempt components. If the supply is naturally a single supply, the dominant element determines treatment. Flag for reviewer: single vs. mixed supply classification requires professional judgement.
**Legislation:** Executive Regulations, Article 4 (composite supplies).

### EC4 -- Motor vehicle for delivery fleet [T1]
**Situation:** Logistics company purchases delivery vans used exclusively for business deliveries.
**Resolution:** Input VAT IS recoverable. Delivery vehicles used exclusively for taxable business activities are excepted from the motor vehicle block. Must demonstrate exclusive business use and vehicle must have a commercial registration.
**Legislation:** Ministerial Order No. 14/2019, Article 1(b) (exception for commercial vehicles).

### EC5 -- First supply of residential property: 3-year window [T1]
**Situation:** Developer sells apartment 2.5 years after completion.
**Resolution:** Zero-rated. The 3-year window runs from the date of completion (occupancy permit). First supply means the first sale or lease to a buyer/tenant after completion.
**Legislation:** Decree-Law No. 48/2018, Article 68(c).

### EC6 -- Free zone transactions [T2]
**Situation:** Business located in a Bahrain free zone sells goods to a mainland Bahrain customer.
**Resolution:** Free zones in Bahrain are generally within the VAT territory. Goods moving from free zone to mainland are not treated as imports. Standard VAT rules apply. Flag for reviewer: confirm whether the specific free zone has any special VAT treatment under NBR guidance.
**Legislation:** Executive Regulations, Article 5 (designated zones).

### EC7 -- Credit notes [T1]
**Situation:** Client issues a credit note to a customer for a partial refund.
**Resolution:** Credit note reduces the original output VAT. If original supply was in Box 1, the credit note reduces Box 1 and Box 7 by the corresponding amounts. Credit note must reference the original invoice number.
**Legislation:** Decree-Law No. 48/2018, Article 37 (credit notes).

### EC8 -- Imports of goods via Customs [T1]
**Situation:** Business imports machinery from Germany. Bahrain Customs collects 10% VAT at the border.
**Resolution:** VAT paid to Customs is recoverable input tax. Report the VAT amount in Box 9 (imports) and claim in Box 14. Retain the customs declaration as supporting documentation. The customs declaration serves as the tax document for input VAT recovery.
**Legislation:** Decree-Law No. 48/2018, Article 26 (imports); Article 49 (input tax deduction on imports).

### EC9 -- Staff welfare: meals for employees [T2]
**Situation:** Company provides subsidised meals in a staff canteen.
**Resolution:** If the meals are a contractual obligation or provided in the ordinary course of business, input VAT is recoverable. If the meals are entertainment (non-contractual perks for client entertainment), input VAT is blocked. Flag for reviewer: confirm whether the meals are contractual or discretionary.
**Legislation:** Ministerial Order No. 14/2019, Article 1(a) (entertainment block); NBR Public Clarification on employee benefits.

### EC10 -- Pre-registration input tax [T1]
**Situation:** Business registered for VAT on 1 July 2025. Wants to claim input VAT on goods purchased in May 2025.
**Resolution:** Input VAT on goods held in stock at the date of registration is recoverable, provided the goods were purchased within 5 years before registration and are still held at registration date. Services: input VAT recoverable if received within 6 months before registration.
**Legislation:** Decree-Law No. 48/2018, Article 50(4) (pre-registration input tax).

### EC11 -- Bad debt relief [T2]
**Situation:** Client issued a tax invoice 18 months ago but has not received payment. Customer appears insolvent.
**Resolution:** Bad debt relief is available if: (i) output VAT was accounted for, (ii) 12 months have passed since the supply, (iii) the debt has been written off in the accounts, and (iv) reasonable efforts to collect have been made. Flag for reviewer: confirm all conditions are met before adjusting.
**Legislation:** Decree-Law No. 48/2018, Article 31 (bad debt adjustment).

### EC12 -- Supply of used goods (margin scheme) [T3]
**Situation:** Second-hand car dealer wants to apply a margin scheme.
**Resolution:** Bahrain does not currently have a formal profit margin scheme for second-hand goods. Standard VAT applies on the full selling price. Escalate to licensed tax advisor if client operates in used goods.
**Legislation:** No specific provision in Decree-Law No. 48/2018.

---

## Step 17: EU VAT Comparison (for cross-reference) [T1]

| Feature | Bahrain | EU (Directive 2006/112/EC) |
|---------|---------|---------------------------|
| Standard rate | 10% | 15-27% (varies by member state) |
| Registration threshold | BHD 37,500 (~EUR 90,000) | Varies (EUR 0 to EUR 85,000) |
| Reverse charge (imports of services) | Yes (Article 46) | Yes (Article 196) |
| Intra-community/GCC supply | Transitional GCC rules | Intra-community supply rules |
| Capital goods adjustment | 5/10 years | 5/10/20 years (varies) |
| Bad debt relief | Yes (12 months) | Varies by member state |
| Margin scheme (used goods) | No | Yes (Articles 312-325) |
| Group registration | Yes (Article 45) | Yes (Article 11) |
| Tax point (time of supply) | Earlier of payment or invoice | Earlier of payment or invoice |
| Electronic filing | Mandatory | Varies by member state |

---

## Step 18: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard local purchase, 10% VAT
**Input:** Bahrain supplier, office supplies, BHD 110 gross, VAT BHD 10, net BHD 100. Fully taxable business.
**Expected output:** Box 8 = BHD 100, Box 14 includes BHD 10. Input VAT recoverable in full.

### Test 2 -- Reverse charge on services from non-resident
**Input:** US supplier (AWS), monthly cloud hosting USD 1,000 (~BHD 377), no VAT on invoice. Fully taxable business.
**Expected output:** Box 9 = BHD 377. Output VAT BHD 37.70 in Box 7. Input VAT BHD 37.70 in Box 14. Net VAT effect = zero.

### Test 3 -- Export of goods (zero-rated)
**Input:** Client exports goods to India. Invoice value BHD 5,000. Bill of lading and export declaration available.
**Expected output:** Box 4 = BHD 5,000. Box 7 = BHD 0 (no output VAT). Input VAT on related purchases is fully recoverable.

### Test 4 -- Exempt financial service
**Input:** Bank earns BHD 50,000 in interest margin income on loans to local customers.
**Expected output:** Box 5 = BHD 50,000. No output VAT. Input VAT on related costs is NOT recoverable.

### Test 5 -- Blocked motor vehicle
**Input:** Company buys a sedan for the managing director. BHD 12,000 net + BHD 1,200 VAT = BHD 13,200 gross.
**Expected output:** Box 8 = BHD 12,000. Box 14 = BHD 0 for this purchase. VAT BLOCKED under Ministerial Order No. 14/2019.

### Test 6 -- First supply of residential property (zero-rated)
**Input:** Developer sells new apartment (completed 18 months ago) for BHD 80,000.
**Expected output:** Box 4 = BHD 80,000. Zero-rated. Input VAT on construction costs is recoverable.

### Test 7 -- Subsequent lease of residential property (exempt)
**Input:** Landlord leases apartment (built 5 years ago, previously sold once) for BHD 500/month.
**Expected output:** Box 5 = BHD 1,500 (quarterly). No output VAT. Input VAT on maintenance NOT recoverable.

### Test 8 -- Healthcare supply (zero-rated)
**Input:** Hospital provides listed medical treatment to patient. Fee BHD 2,000.
**Expected output:** Box 4 = BHD 2,000. Zero-rated. Input VAT on medical supplies is recoverable.

### Test 9 -- Credit note adjustment
**Input:** Client issues credit note for BHD 500 + BHD 50 VAT on a previous standard-rated sale.
**Expected output:** Box 1 reduced by BHD 500. Box 7 reduced by BHD 50. Credit note must reference original invoice.

### Test 10 -- Pre-registration input tax claim
**Input:** Business registered 1 March 2026. Claims VAT on equipment purchased 15 December 2025 (BHD 3,000 net + BHD 300 VAT). Equipment still held at registration date.
**Expected output:** Box 8 = BHD 3,000. Box 14 includes BHD 300. Pre-registration claim valid (within 5-year window, goods still held).

### Test 11 -- Mixed-use purchase (partial exemption)
**Input:** Company makes 70% taxable and 30% exempt supplies. Purchases office rent BHD 2,000 + BHD 200 VAT (used for all activities).
**Expected output:** Box 8 = BHD 2,000. Box 14 includes BHD 140 (70% of BHD 200). Recovery restricted by pro-rata ratio.

### Test 12 -- Late filing penalty calculation
**Input:** Quarterly return for Q2 2025 due 31 July 2025. Filed 15 August 2025. Tax payable BHD 8,000.
**Expected output:** Late filing penalty: BHD 500. Late payment penalty: BHD 80/day x 15 days = BHD 1,200. Total penalty = BHD 1,700. Tax due = BHD 9,700.

---

## Step 19: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

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
| Goods (no transport) | Where goods are located at time of supply | Article 11(1) |
| Goods (with transport) | Where transport begins | Article 11(2) |
| Goods (installed/assembled) | Where installation/assembly takes place | Article 11(3) |
| Services (general rule) | Where supplier has place of residence | Article 13(1) |
| Services (B2B) | Where customer has place of residence | Article 13(2) |
| Real estate services | Where property is located | Article 14 |
| Transport services | Where transport takes place (apportioned if cross-border) | Article 15 |
| Telecommunications/electronic services (B2C) | Where customer uses and enjoys the service | Article 16 |
| Restaurant/catering | Where services are physically performed | Article 17 |

**Legislation:** Decree-Law No. 48/2018, Articles 11-17.

---

## Step 21: Deemed Supplies [T1]

| Situation | Treatment | Legislation |
|-----------|-----------|-------------|
| Business gifts > BHD 25 per person per year | Deemed supply at market value, output VAT due | Article 27 |
| Goods/services for non-business (personal) use | Deemed supply at cost, output VAT due | Article 28 |
| Cessation of registration while holding stock | Deemed supply on remaining stock | Article 29 |
| Transfer of goods between branches (cross-border) | May trigger deemed supply | Article 30 |

**Legislation:** Decree-Law No. 48/2018, Articles 27-30.

---

## Contribution Notes

If you are adapting this skill for another jurisdiction, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all box numbers with the equivalent boxes on your jurisdiction's VAT return form.
3. Replace VAT rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the registration thresholds with your jurisdiction's equivalent.
5. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
6. Have a licensed or warranted accountant in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
8. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
