---
name: barbados-vat
description: Use this skill whenever asked to prepare, review, or create a Barbados VAT return for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "Barbados VAT", or any request involving Barbados VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Barbados VAT classification rules, return form mappings, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Barbados VAT-related work.
---

# Barbados VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Barbados |
| Jurisdiction Code | BB |
| Primary Legislation | Value Added Tax Act, 2005 (Cap. 87) (as amended) |
| Supporting Legislation | VAT Regulations; Excise Tax Act; Customs Act |
| Tax Authority | Barbados Revenue Authority (BRA) |
| Filing Portal | https://www.bra.gov.bb (BRA Online Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires sign-off by a licensed Barbados accountant (ICAB member) |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: rate classification, return box assignment, input tax recovery, derived calculations. Tier 2: partial exemption, tourism levy interaction, international business company treatments. Tier 3: complex group structures, advance rulings, transfer pricing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Tax Identification Number)** [T1]
2. **VAT registration number** [T1] -- assigned by BRA
3. **VAT filing period** [T1] -- bi-monthly (standard) or monthly (for large taxpayers as designated by BRA)
4. **Industry/sector** [T2] -- impacts classification (tourism, financial services, international business)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input tax attribution required
6. **Does the business import goods?** [T1] -- impacts customs VAT treatment
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business a licensed international business company?** [T2] -- different regime may apply

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: VAT Rate Structure [T1]

**Legislation:** VAT Act 2005, Section 8; First Schedule; Second Schedule.

### Standard Rate

| Rate | Application |
|------|-------------|
| 17.5% | Standard rate on all taxable supplies and imports not otherwise specified [T1] |

### Reduced Rate

| Rate | Application |
|------|-------------|
| 10% | Hotel and tourism accommodation services (guest houses, hotels, inns, vacation/holiday homes). Increased from 7.5% to 10% effective 1 January 2020. [T1] |

### Higher Rate

| Rate | Application |
|------|-------------|
| 22% | Mobile telecommunications services [T1] |

### Zero-Rated Supplies (0%) [T1]

**Legislation:** VAT Act, First Schedule.

- Exports of goods
- International transport services
- Basic food items (specified in Schedule): rice, flour, sugar, milk (fresh and powdered), bread, fresh meat, fresh fish, fresh fruits and vegetables, cooking oil, margarine
- Prescription drugs and medicines
- Agricultural inputs (fertilizers, pesticides, seeds, animal feed)
- Water (piped, domestic supply)
- Kerosene and cooking gas (LPG)
- Printed books and educational materials

### Exempt Supplies (No VAT, No Input Credit) [T1]

**Legislation:** VAT Act, Second Schedule.

- Financial services (interest, life insurance premiums, foreign exchange transactions)
- Residential rental
- Medical and dental services
- Educational services (approved institutions)
- Public transportation
- Land (sale of undeveloped land)
- Burial and cremation services
- Childcare services (approved facilities)

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, NIS contributions, loan repayments, dividends = OUT OF SCOPE (never on VAT return)

### 2b. Determine Counterparty Location [T1]
- Domestic (Barbados): supplier/customer in BB
- CARICOM: Trinidad, Jamaica, Guyana, Suriname, Belize, Bahamas, Haiti, OECS states
- International: all other countries

### 2c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize: 0%, 10% (accommodation), 17.5% (standard), or exempt
- Boundaries: <= 1% = 0%; 7-12% = 10%; >= 14% = 17.5%

### 2d. Determine Expense Category [T1]
- Capital goods: equipment, machinery, vehicles, furniture
- Inventory for resale: goods purchased for direct resale
- Operating expenses/overheads: everything else

---

## Step 3: VAT Return Form Structure [T1]

**The VAT return is filed bi-monthly (or monthly for large taxpayers).**

### Part A -- Supplies (Output)

| Box | Description |
|-----|-------------|
| 1 | Value of taxable supplies at standard rate (17.5%) |
| 2 | VAT on standard-rate supplies (Box 1 x 17.5%) |
| 3 | Value of supplies at reduced rate (10%) |
| 4 | VAT on reduced-rate supplies (Box 3 x 10%) |
| 5 | Value of zero-rated supplies |
| 6 | Value of exempt supplies |
| 7 | Total value of all supplies (Box 1 + Box 3 + Box 5 + Box 6) |
| 8 | VAT charged on imports (customs entries) |
| 9 | Reverse charge VAT on imported services |
| 10 | Total output tax (Box 2 + Box 4 + Box 8 + Box 9) |

### Part B -- Purchases (Input)

| Box | Description |
|-----|-------------|
| 11 | VAT on local purchases at standard rate |
| 12 | VAT on local purchases at reduced rate |
| 13 | VAT on imports (claimable) |
| 14 | Total input tax (Box 11 + Box 12 + Box 13) |
| 15 | Input tax adjustments (blocked/apportioned) |
| 16 | Net allowable input tax (Box 14 - Box 15) |

### Part C -- Tax Payable / Refundable

| Box | Description | Calculation |
|-----|-------------|-------------|
| 17 | Net VAT (Box 10 - Box 16) |
| 18 | Credit brought forward |
| 19 | Net amount payable / (refundable) (Box 17 - Box 18) |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Act, Section 9.

When a Barbados registered person receives services from a non-resident supplier:

1. Self-assess VAT at 17.5% on the value of the imported service [T1]
2. Report as output tax (Box 9) [T1]
3. Claim input tax (Box 11) if used for taxable supplies [T1]
4. Net effect: zero for fully taxable businesses [T1]

### Exceptions [T1]
- Out-of-scope categories: NEVER reverse charge
- Services exempt if supplied domestically: reverse charge applies but NO input credit
- Services consumed entirely outside Barbados: NOT subject to VAT

---

## Step 5: Deductibility Check

### Blocked Input Tax (No Recovery) [T1]

**Legislation:** VAT Act, Section 18; Third Schedule.

- **Entertainment** -- meals, hospitality, amusement (unless hospitality trade) [T1]
- **Motor cars** -- purchase, lease, maintenance of passenger vehicles (exception: car rental, taxi, driving instruction) [T1]
- **Club memberships** -- sporting, social, recreational [T1]
- **Personal use items** -- goods/services not for business purposes [T1]
- **Goods/services for exempt supplies** -- no input credit [T1]

### Registration-Based Recovery [T1]
- VAT-registered making taxable supplies: full recovery (subject to blocked categories)
- Non-registered: NO recovery
- Registered making only exempt supplies: NO recovery

### Partial Exemption / Apportionment [T2]

**Legislation:** VAT Act, Section 18(3).

If both taxable and exempt supplies:
- Direct attribution: allocate to taxable or exempt
- Common costs: `Recovery % = (Taxable Supplies / Total Supplies) * 100`
- **Flag for reviewer: apportionment must be confirmed by licensed accountant.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual taxable supplies exceeding BBD 200,000 |
| Voluntary registration | Below BBD 200,000 (may register if making taxable supplies) |
| Note: BBD is pegged to USD at 2:1 | BBD 200,000 = approximately USD 100,000 |

**Legislation:** VAT Act, Section 12.

---

## Step 7: Filing Deadlines and Penalties [T1]

**Legislation:** VAT Act, Sections 36, 39, 40.

### Filing Deadlines

| Period Type | Deadline |
|-------------|----------|
| Bi-monthly (standard) | 21st of the month following the end of the bi-monthly period [T1] |
| Monthly (large taxpayers) | 21st of the following month [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | BBD 500 per return plus BBD 100 per day (maximum BBD 5,000) [T1] |
| Late payment | Interest at 1% per month or part thereof on outstanding tax [T1] |
| Failure to register | Back-assessment plus penalties [T1] |
| Fraudulent return | Criminal prosecution; fines up to BBD 50,000 and/or imprisonment up to 5 years [T1] |
| Failure to keep records | BBD 5,000 and/or imprisonment [T1] |

---

## Step 8: Tax Invoice Requirements [T1]

**Legislation:** VAT Act, Section 26.

A valid tax invoice must contain:

1. The words "Tax Invoice"
2. Supplier's name, address, and VAT registration number
3. Customer's name and VAT registration number (for B2B above BBD 100)
4. Date of issue
5. Sequential invoice number
6. Description of goods or services
7. Quantity and unit price
8. Total value excluding VAT
9. VAT rate applied
10. VAT amount
11. Total value including VAT

---

## Step 9: Classification Matrix -- Common Transactions [T1]

### Domestic Purchases

| Category | VAT Treatment | Input Credit | Return Box |
|----------|--------------|--------------|------------|
| Office supplies | 17.5% | Yes | Box 11 |
| Commercial rent | 17.5% | Yes | Box 11 |
| Residential rent | Exempt | No | N/A |
| Electricity (commercial) | 17.5% | Yes | Box 11 |
| Telephone/internet | 17.5% | Yes | Box 11 |
| Motor car purchase | 17.5% | BLOCKED | Box 15 |
| Entertainment | 17.5% | BLOCKED | Box 15 |
| Hotel accommodation (business) | 10% | Yes | Box 12 |
| Professional fees | 17.5% | Yes | Box 11 |
| Insurance (general) | 17.5% | Yes | Box 11 |
| Insurance (life) | Exempt | No | N/A |
| Basic food items | 0% | N/A | N/A |
| Prescription drugs | 0% | N/A | N/A |

### Sales

| Category | VAT Treatment | Return Box |
|----------|--------------|------------|
| Domestic sale (standard) | 17.5% | Box 1, Box 2 |
| Hotel accommodation | 10% | Box 3, Box 4 |
| Export of goods | 0% | Box 5 |
| Export of services | 0% | Box 5 |
| Exempt supply | Exempt | Box 6 |

### Imports

| Category | VAT Treatment | Return Box |
|----------|--------------|------------|
| Goods imported | 17.5% at customs | Box 8 (output), Box 13 (input) |
| Services imported | Self-assess 17.5% | Box 9 (output), Box 11 (input) |

---

## Step 10: Tourism Sector Rules [T2]

**Legislation:** VAT Act, Section 8(2); Tourism Development Act.

- Hotel accommodation: 10% reduced rate (increased from 7.5% effective 1 January 2020) [T1]
- Restaurant services within hotels: 17.5% standard rate (NOT 10%) [T1]
- Tourism Levy: separate from VAT -- additional levy on hotel room rates (currently 2.5%). This is NOT VAT and is not reported on the VAT return [T1]
- Shared Accommodation Levy: applies to Airbnb-type rentals. Separate from VAT [T2]
- Tourism-related goods sold in duty-free shops: may be zero-rated for departing visitors [T2]
- Flag for reviewer: tourism sector has multiple overlapping levies. Confirm which apply.

---

## Step 11: International Business Companies [T2]

**Legislation:** International Business Companies Act; VAT Act exemptions.

- International Business Companies (IBCs) and International Societies with Restricted Liability (ISRLs) may have special VAT treatments
- Services exported by IBCs: generally zero-rated
- Supplies between IBCs and domestic businesses: standard VAT rules apply
- Flag for reviewer: IBC status does not automatically exempt from VAT. Confirm treatment on a case-by-case basis [T3]

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from facts
- NEVER allow input tax credit on blocked categories (entertainment, motor cars, clubs)
- NEVER apply reverse charge to out-of-scope categories (salaries, NIS, PAYE)
- NEVER allow non-registered persons to claim input tax credits
- NEVER confuse zero-rated (input credit allowed) with exempt (NO input credit)
- NEVER confuse the Tourism Levy (not VAT) with VAT
- NEVER apply the 10% reduced rate to anything other than hotel/tourism accommodation
- NEVER ignore the BBD 200,000 registration threshold
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 12: Edge Case Registry

### EC1 -- Imported software subscription [T1]
**Situation:** Barbados registered business subscribes to US cloud software. No VAT on invoice.
**Resolution:** Reverse charge at 17.5%. Output tax (Box 9). Input tax (Box 11) if used for taxable supplies. Net = zero.

### EC2 -- Hotel restaurant vs. accommodation [T1]
**Situation:** Hotel invoice covers both room (10%) and restaurant meals (17.5%).
**Resolution:** Split by line item. Room = 10%. Restaurant = 17.5%. If not split on invoice, flag for reviewer.

### EC3 -- Motor vehicle for delivery [T2]
**Situation:** Client purchases a pickup truck for deliveries.
**Resolution:** Passenger vehicles are blocked. Commercial vehicles (trucks, vans designed for goods transport) may not be blocked. Flag for reviewer: confirm vehicle classification.

### EC4 -- Credit notes [T1]
**Situation:** Client issues credit note for returned goods.
**Resolution:** Reduce output tax. Report net figures. Do not create separate negative entries.

### EC5 -- Shared accommodation (Airbnb) [T2]
**Situation:** Client rents property via Airbnb short-term.
**Resolution:** May be subject to VAT at 10% (accommodation) plus the Shared Accommodation Levy. If client is not VAT registered but exceeds threshold, registration may be required. Flag for reviewer.

### EC6 -- Duty-free imports under concession [T2]
**Situation:** Client imports equipment under government duty-free concession.
**Resolution:** Duty concession may waive customs duty but not necessarily VAT. Confirm whether VAT relief is included in the concession order. Flag for reviewer.

### EC7 -- Supplies between related parties [T2]
**Situation:** Client sells goods to a related company at below-market value.
**Resolution:** VAT is assessed on the open market value, not the transaction price, for supplies between related parties. Flag for reviewer: confirm open market value.
**Legislation:** VAT Act, Section 10.

### EC8 -- Second-hand goods margin scheme [T1]
**Situation:** Client buys second-hand goods from non-registered person.
**Resolution:** Barbados does not have a margin scheme for second-hand goods. Full VAT applies on resale. No input credit on the purchase from non-registered supplier.

### EC9 -- Construction services [T1]
**Situation:** Contractor provides building construction services.
**Resolution:** Construction services are taxable at 17.5%. Input VAT on materials and subcontractors is recoverable. For property owner: input VAT only recoverable if property used for taxable supplies.

### EC10 -- Digital/streaming services from abroad [T2]
**Situation:** Barbados resident subscribes to Netflix, Spotify, or other digital services from abroad.
**Resolution:** Non-resident digital service providers are increasingly required to register for VAT. For business consumers, reverse charge at 17.5%. Flag for reviewer: confirm current digital services registration requirements.

---

## Step 12a: Sector-Specific Guidance [T2]

### Tourism Sector (Detailed)

**Legislation:** Tourism Development Act; VAT Act.

- **Hotel accommodation**: 10% reduced rate (increased from 7.5% effective 1 January 2020) [T1]
- **Restaurant services in hotels**: 17.5% standard rate (NOT 10%) [T1]
- **Tourism Levy (TL)**: 2.5% on room revenue -- separate from VAT, NOT on VAT return [T1]
- **Shared Accommodation Levy (SAL)**: applies to Airbnb/short-term rental -- separate from VAT [T2]
- **Product Enhancement Fund (PEF)**: additional levy on tourism -- separate from VAT [T2]
- **Tour operator services**: 17.5% [T1]
- **Water sports and activities**: 17.5% [T1]
- **Cruise ship passenger levy**: separate from VAT [T1]
- Flag for reviewer: tourism has 4+ overlapping levies. Distinguish VAT from non-VAT charges.

### Financial Services

- **Interest income**: exempt [T1]
- **Banking fees**: taxable at 17.5% [T1]
- **Insurance premiums (life)**: exempt [T1]
- **Insurance premiums (general)**: taxable at 17.5% [T1]
- **Foreign exchange commissions**: exempt [T1]
- **International business company (IBC) services**: flag for reviewer [T2]

### Construction and Real Estate

- **Construction services**: 17.5% [T1]
- **Sale of new real estate**: 17.5% [T2]
- **Sale of undeveloped land**: exempt [T1]
- **Commercial rental**: 17.5% [T1]
- **Residential rental**: exempt [T1]
- **Construction materials**: 17.5% [T1]

### Agriculture

- **Unprocessed produce**: zero-rated (basic food) [T1]
- **Processed food**: 17.5% (unless on basic food list) [T1]
- **Agricultural inputs**: zero-rated [T1]
- **Sugar cane and rum production**: standard rate on domestic sales [T1]

### Rum and Spirits Industry

- **Rum production inputs**: 17.5% VAT, input credit available [T1]
- **Domestic rum sales**: 17.5% VAT + Excise Tax (separate) [T1]
- **Rum exports**: zero-rated [T1]
- **Excise Tax**: separate from VAT, not on VAT return [T1]

---

## Step 12b: Books and Records Requirements [T1]

**Legislation:** VAT Act, Section 46.

All VAT-registered persons must maintain:

- **Sales records**: all tax invoices issued, credit notes, export documentation
- **Purchase records**: all purchase invoices with VAT breakdowns
- **Import records**: customs entries showing VAT paid
- **VAT account**: summary ledger of output/input VAT
- **Bank statements**: reconciled to business records
- Records must be retained for a minimum of **7 years**
- Records must be in English and available for BRA inspection at registered address

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
Action Required: Licensed accountant must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed accountant. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard local purchase, 17.5%
**Input:** Barbados supplier, office equipment, gross BBD 11,750, VAT BBD 1,750, net BBD 10,000, registered person.
**Expected output:** Box 11 = BBD 1,750 input tax. Full recovery.

### Test 2 -- Hotel accommodation sale, 10%
**Input:** Registered hotel charges guest BBD 5,500 (BBD 5,000 + BBD 500 VAT at 10%).
**Expected output:** Box 3 = BBD 5,000. Box 4 = BBD 500. Tourism Levy reported separately.

### Test 3 -- Export, zero-rated
**Input:** Registered exporter ships goods to UK, net BBD 20,000.
**Expected output:** Box 5 = BBD 20,000. No output VAT. Input tax fully recoverable.

### Test 4 -- Motor car, blocked
**Input:** Registered person purchases sedan BBD 80,000, VAT BBD 14,000.
**Expected output:** Box 15 adjustment = BBD 14,000. Net input credit = zero.

### Test 5 -- Imported services, reverse charge
**Input:** US accounting firm provides services USD 3,000 (~ BBD 6,000). No VAT on invoice.
**Expected output:** Box 9 output = BBD 1,050 (17.5%). Box 11 input = BBD 1,050. Net = zero.

### Test 6 -- Exempt supply (residential rental)
**Input:** Registered person earns residential rental BBD 3,000/month.
**Expected output:** Box 6 = BBD 3,000. No output VAT. Input tax on rental expenses NOT recoverable.

### Test 7 -- Mixed business apportionment
**Input:** 75% taxable, 25% exempt supplies. Common VAT = BBD 2,000.
**Expected output:** Flag T2. Input = BBD 1,500 (75%). Blocked = BBD 500 (25%).

### Test 8 -- Entertainment, blocked
**Input:** Client dinner BBD 2,350 inclusive of VAT BBD 350.
**Expected output:** VAT BBD 350 BLOCKED. No input credit.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
