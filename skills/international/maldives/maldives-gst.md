---
name: maldives-gst
description: Use this skill whenever asked to prepare, review, or create a Maldives GST return or any GST filing for a Maldivian business. Trigger on phrases like "prepare GST return", "Maldives GST", "MIRA filing", "tourism GST", or any request involving Maldives GST. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill contains the complete Maldives GST classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Maldives GST-related work.
---

# Maldives GST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Republic of Maldives |
| Jurisdiction Code | MV |
| Primary Legislation | Goods and Services Tax Act (Act No. 10/2011, as amended) |
| Supporting Legislation | GST Regulation; MIRA Rulings |
| Tax Authority | Maldives Inland Revenue Authority (MIRA) |
| Filing Portal | https://www.mira.gov.mv (MIRAconnect portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: dual-rate classification (17% tourism / 8% general), input-output mapping, return structure. Tier 2: mixed tourism/general supplies, sector exemptions. Tier 3: special economic zones, complex resort structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tax Identification Number from MIRA
2. **GST registration status** [T1] -- Registered (mandatory or voluntary) or below threshold
3. **Business category** [T1] -- **Critical: Tourism or General sector** (determines GST rate)
4. **Filing period** [T1] -- monthly (standard)
5. **Does the business provide tourism goods/services?** [T1] -- determines 17% vs 8% rate
6. **Does the business make exempt supplies?** [T2] -- apportionment required
7. **Does the business export goods/services?** [T1] -- zero-rating
8. **Excess credit brought forward** [T1] -- from prior period
9. **Is the entity a resort, guesthouse, hotel, liveaboard, or dive center?** [T1] -- tourism sector

**If any of items 1-4 are unknown, STOP. The tourism/general classification is ESSENTIAL.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output GST) or Purchase (input GST)
- Salaries, pension contributions, loan repayments = OUT OF SCOPE
- **Legislation:** GST Act 10/2011, Section 4

### 1b. Determine Supply Location [T1]
- Domestic (within Maldives)
- Import (outside Maldives)
- Export (outside Maldives)
- **Legislation:** GST Act 10/2011, Section 12

### 1c. Determine GST Rate [T1]

**THE MALDIVES HAS A DUAL-RATE GST SYSTEM:**

| Sector | GST Rate |
|--------|----------|
| **Tourism goods and services** | **17%** (increased from 16% effective 1 July 2025) |
| **General goods and services** | **8%** |
| Zero-rated (exports) | 0% |
| Exempt | N/A |

### Tourism Goods and Services (17%) [T1]
The following attract the 17% tourism rate (increased from 16% effective 1 July 2025 per the seventh amendment to the GST Act):
- Resort accommodation and food/beverage
- Guesthouse accommodation (registered tourism establishments)
- Hotel services
- Liveaboard/cruise services
- Dive center services (tourism-registered)
- Spa services in tourism establishments
- Water sports and excursion services in tourism
- Goods sold at tourist shops within resort premises
- Any goods/services provided by a tourism establishment to tourists

### General Goods and Services (8%) [T1]
All other taxable supplies that are NOT tourism sector:
- General retail sales
- Professional services (legal, accounting, consulting)
- Construction services
- General food and beverage (non-tourism)
- Telecommunications
- Wholesale trade

### Exempt Supplies [T1]
- Basic food items (rice, flour, sugar, etc. per MIRA list)
- Education services (registered institutions)
- Health services
- Residential rental
- Financial services (interest on loans, insurance premiums)
- Government services
- International transport of goods

### Zero-Rated [T1]
- Exports of goods
- International transport services
- Supplies to foreign diplomats

---

## Step 2: GST Return Form Structure [T1]

**Legislation:** GST Act 10/2011; MIRA prescribed form (GST 201).

### GST-201 Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Tourism sector output |
| 2.1 | Tourism taxable supplies at 17% |
| 2.2 | Tourism output GST |
| Part 3 | General sector output |
| 3.1 | General taxable supplies at 8% |
| 3.2 | General output GST |
| Part 4 | Other output |
| 4.1 | Zero-rated supplies |
| 4.2 | Exempt supplies |
| 4.3 | Total supplies |
| Part 5 | Total output GST (Part 2.2 + Part 3.2) |
| Part 6 | Input GST |
| 6.1 | GST on domestic purchases |
| 6.2 | GST on imports |
| 6.3 | Total input GST credit |
| Part 7 | Net GST |
| 7.1 | Output GST minus Input GST |
| 7.2 | Credit brought forward |
| 7.3 | Net payable or credit |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** GST Act 10/2011, Sections 32-38.

### Eligibility

1. Business must be GST registered [T1]
2. Purchase must relate to making taxable supplies [T1]
3. Valid tax invoice held [T1]
4. Supplier must be registered [T1]
5. Goods/services received [T1]

### Cross-Sector Input Credit [T2]

If a business makes both tourism (17%) and general (8%) supplies, input credit must be allocated:
- Directly attributable inputs: allocate to the relevant sector
- Common inputs (overheads): apportion by revenue ratio

```
Tourism Input Credit = Common Input GST x (Tourism Revenue / Total Revenue)
General Input Credit = Common Input GST x (General Revenue / Total Revenue)
```
**Flag for reviewer: cross-sector apportionment must be confirmed.**

### Tourism Sector Input Credit [T1]
- Tourism businesses claim input credit on purchases at any rate (8% or 17%)
- Full credit regardless of whether input was purchased at 8% or 17%
- The key test is: was the purchase used for making taxable tourism supplies?

---

## Step 4: Deductibility Check

### Blocked Input GST Credit [T1]

**Legislation:** GST Act 10/2011, Section 34.

These have ZERO input GST credit:

- Motor vehicles for personal use
- Entertainment (unless tourism business providing to guests as part of service)
- Personal consumption of owners/directors/employees
- Purchases without valid tax invoice
- Purchases from non-registered suppliers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless for tourism establishment resale/service)

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

### Special Tourism Exception [T1]
Tourism establishments (resorts, hotels, guesthouses) CAN claim input credit on food, beverages, and entertainment items purchased for guest services. This is NOT entertainment for the business owner -- it is a business input for the tourism service.

---

## Step 5: GST on Imports [T1]

**Legislation:** GST Act 10/2011, Section 16; Customs Act.

### Import GST
- GST payable at point of importation
- Calculated on: CIF value + Customs Duty
- Rate: 8% (general rate applies to imports; 17% if specifically for tourism establishment use)
- Paid to Maldives Customs Service
- Recoverable as input credit if for taxable supplies

---

## Step 6: Green Tax (Tourism) [T1]

**Legislation:** Green Tax Act (amended effective 1 January 2025).

- Green Tax (effective 1 January 2025):
  - **USD 12 per person per night** for tourist resorts, integrated resorts, resort hotels, tourist vessels, hotels/guesthouses on uninhabited islands, and hotels/guesthouses with more than 50 rooms on inhabited islands
  - **USD 6 per person per night** for hotels and guesthouses with 50 rooms or fewer on inhabited islands
  - Children under 2 at check-in are exempt
  - Charged per 24-hour block when a guest stays 12 hours or more during that block (the "12-hour rule")
- This is a SEPARATE levy from GST
- Green Tax does NOT affect GST calculations
- Reported and paid separately to MIRA monthly via MIRAconnect by the 28th of the following month

**Do not include Green Tax in GST return calculations.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory GST registration (tourism) | All tourism establishments (no threshold) |
| Mandatory GST registration (general) | Annual turnover > MVR 1,000,000 |
| Voluntary registration (general) | Below threshold but may register |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| GST return (monthly) | Monthly | 28th of the following month |
| Payment | Monthly | Same as return deadline |
| Annual income tax | Annual | Per MIRA schedule |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | MVR 50 per day (individuals) / MVR 100 per day (companies) |
| Late payment | 0.5% per month on unpaid amount |
| Non-filing | Assessment by MIRA + penalties |
| Non-registration (tourism) | MVR 50,000 + retrospective registration |

---

## Step 9: Derived Calculations [T1]

```
Tourism Output GST     = Tourism taxable supplies x 17%
General Output GST     = General taxable supplies x 8%
Total Output GST       = Tourism Output GST + General Output GST
Total Input GST        = GST on domestic purchases + GST on imports
Net GST Payable        = Total Output GST - Total Input GST - Credit B/F
If Net < 0             = Credit carried forward
Total Payable          = Net GST + Penalties (if any)
```

---

## Step 10: Currency Considerations [T1]

**Legislation:** GST Act 10/2011, Section 47.

- Tourism establishments typically invoice in USD
- GST return must be filed in MVR
- Convert at MMA (Maldives Monetary Authority) rate on date of supply
- USD-denominated accounts: convert each transaction at daily rate

---

## PROHIBITIONS [T1]

- NEVER apply 8% rate to tourism goods/services -- tourism is ALWAYS 17%
- NEVER apply 17% rate to general goods/services -- general is ALWAYS 8%
- NEVER allow unregistered entities to claim input credit
- NEVER classify exempt supplies as zero-rated
- NEVER include Green Tax in GST calculations
- NEVER accept input credit without valid tax invoice
- NEVER apply input credit on blocked categories (except tourism guest service exception)
- NEVER file return without separating tourism and general supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Resort with staff canteen [T2]
**Situation:** Resort purchases food for staff canteen (not guest dining).
**Resolution:** Staff canteen is for employees, not tourism guests. Input credit may be limited. If staff are essential for tourism operations, credit may be argued. Flag for reviewer: distinguish guest F&B from staff F&B.

### EC2 -- Guesthouse providing local and tourist services [T2]
**Situation:** Guesthouse on inhabited island serves both tourists (17%) and locals (8%).
**Resolution:** Must separate tourism supplies (17%) from general supplies (8%). Each revenue stream reported in its respective section. Input credit apportioned. Flag for reviewer.

### EC3 -- Reverse charge on imported services [T2]
**Situation:** Resort pays for marketing services from a foreign agency.
**Resolution:** Self-assess GST at applicable rate (17% if tourism-related, 8% if general). Claim input credit if for taxable supplies. Flag for reviewer: confirm rate classification.

### EC4 -- Duty-free shop in resort [T1]
**Situation:** Resort operates a duty-free shop for guests.
**Resolution:** Sales to tourists within resort premises attract 17% tourism GST. Not truly duty-free for GST purposes -- GST still applies on domestic supply within tourism establishment.

### EC5 -- Charter yacht / liveaboard [T1]
**Situation:** Liveaboard vessel provides accommodation and diving for tourists.
**Resolution:** All services at 17% tourism rate. Green Tax at USD 12/person/night separately (or USD 6 if 50 rooms or fewer on inhabited island). Input credit on fuel, food, equipment at whatever rate was charged.

### EC6 -- Construction of new resort [T2]
**Situation:** Developer building a new resort, purchasing construction materials and services.
**Resolution:** Input GST credit during construction phase is allowed if the developer is GST registered and will make taxable tourism supplies. Credit may accumulate before revenue begins. Flag for reviewer: confirm registration timing.

### EC7 -- Mixed invoice: tourism and general [T1]
**Situation:** Supplier provides services to both tourism and general sectors of the same business.
**Resolution:** Split by line item. Tourism portion at 17%. General portion at 8%. If not separable, classify based on predominant use.

### EC8 -- Online travel agent (OTA) commissions [T2]
**Situation:** Resort pays commission to Booking.com or Expedia.
**Resolution:** Commission is a service from a non-resident. Reverse charge applies. Rate: 17% (tourism-related service). Input credit allowed. Flag for reviewer: confirm classification as tourism vs general.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [most likely correct treatment]
Action Required: Qualified accountant must confirm before filing.
```

When a [T3] situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Tourism supply at 17%
**Input:** Resort room revenue USD 10,000 (MVR 154,200). Tourism sector.
**Expected output:** Part 2.1: MVR 154,200. Part 2.2: Tourism GST MVR 26,214 (17%).

### Test 2 -- General supply at 8%
**Input:** Consulting firm provides advisory services MVR 50,000 to local client.
**Expected output:** Part 3.1: MVR 50,000. Part 3.2: General GST MVR 4,000 (8%).

### Test 3 -- Purchase with input credit
**Input:** Resort purchases food from registered supplier, MVR 100,000, GST MVR 8,000 (8%).
**Expected output:** Part 6.1: Input GST MVR 8,000. Full credit (used for tourism taxable supply).

### Test 4 -- Export (zero-rated)
**Input:** Fish processing company exports tuna, FOB MVR 500,000.
**Expected output:** Part 4.1: MVR 500,000 at 0%. No output GST. Input credit recoverable.

### Test 5 -- Blocked input: director's car
**Input:** Company purchases car for director, MVR 300,000, GST MVR 24,000.
**Expected output:** Input GST MVR 0 (BLOCKED -- personal use).

### Test 6 -- Mixed tourism and general
**Input:** Hotel serves tourists (MVR 200,000 revenue) and local event catering (MVR 50,000). Input GST on common costs MVR 10,000.
**Expected output:** Tourism output: MVR 200,000 x 17% = MVR 34,000. General output: MVR 50,000 x 8% = MVR 4,000. Input apportionment: Tourism = MVR 10,000 x (200/250) = MVR 8,000. General = MVR 10,000 x (50/250) = MVR 2,000.

### Test 7 -- Import GST
**Input:** Import supplies for resort, CIF MVR 200,000. Duty MVR 30,000. Import GST at 8% on MVR 230,000 = MVR 18,400.
**Expected output:** Part 6.2: Input GST MVR 18,400. Credit allowed.

### Test 8 -- Green Tax separation
**Input:** Resort hosts 50 guests for 7 nights. Green Tax = 50 x 7 x USD 6 = USD 2,100.
**Expected output:** Green Tax USD 2,100 reported separately (note: at the new USD 12 rate this would be USD 4,200; verify applicable rate). NOT included in GST return. GST on accommodation reported at 17% in Part 2.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** GST Act 10/2011, Section 26.

### Mandatory Contents of GST Invoice
1. Supplier's name, address, and TIN
2. Buyer's name and TIN (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. GST rate (8% or 17%) and GST amount -- MUST specify which rate
8. Total amount including GST
9. Currency (MVR or USD with exchange rate)

### Tourism vs General Invoices
- Tourism invoices: clearly state 17% GST
- General invoices: clearly state 8% GST
- Mixed invoices: line-by-line breakdown required

---

## Step 15: Record Keeping [T1]

**Legislation:** GST Act 10/2011, Section 40; Tax Administration Act.

### Mandatory Records (retain for 5 years)
1. All purchase and sales invoices
2. GST control account
3. Import documentation
4. Bank statements (MVR and USD accounts)
5. General ledger and journals
6. Guest folios (tourism sector)
7. Room occupancy records (tourism sector)
8. Green Tax records (separate from GST)
9. Credit and debit notes
10. Staff records and payroll (separate)

---

## Step 16: Specific Sector Rules

### Resort Operations [T1]
- Room revenue: GST at 17%
- Food and beverage (guest): GST at 17%
- Spa services: GST at 17%
- Excursions and water sports: GST at 17%
- Retail shop within resort: GST at 17%
- Staff accommodation and meals: not a supply (internal consumption)
- Green Tax: USD 12 per person per night for resorts (USD 6 for small guesthouses) -- separate

### Guesthouse Operations [T1]
- Room revenue: GST at 17% (if registered as tourism establishment)
- Food and beverage: GST at 17% (if served to tourists)
- Local catering services: GST at 8% (if general, not tourism)
- Must maintain separate revenue streams if serving both tourists and locals

### General Retail [T1]
- All goods sold: GST at 8%
- Basic food items (specified): exempt
- Input credit allowed on purchases from registered suppliers

### Fishing Industry [T1]
- Fresh fish (unprocessed): exempt
- Processed fish products: GST at 8%
- Export of fish: zero-rated
- Fishing supplies and equipment: GST at 8% (input credit allowed)

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register (tourism) | MVR 50,000 |
| Failure to register (general) | MVR 30,000 |
| Late filing | MVR 50/day (individual) / MVR 100/day (company) |
| Late payment | 0.5% per month |
| Non-issuance of invoice | MVR 5,000 per instance |
| Incorrect rate applied | Difference in tax + penalty |
| Failure to maintain records | MVR 10,000 |
| Under-declaration | Additional tax + 100% penalty |
| Tax evasion | Criminal prosecution + fines |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. MIRA may audit within **5 years** of filing
2. Tourism establishments subject to more frequent audits
3. Types: desk audit, field audit, investigation

### Appeals
1. File objection with MIRA within **30 days** of assessment
2. Appeal to Tax Appeal Tribunal within **30 days**
3. Further appeal to High Court

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified accountant or tax advisor practicing in the Maldives before use in production. All T1 rules must be verified against the latest amendments to the GST Act and MIRA rulings.

**A skill may not be published without sign-off from a qualified practitioner in the Maldives.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
