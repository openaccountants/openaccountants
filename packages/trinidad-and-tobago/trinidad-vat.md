---
name: trinidad-vat
description: Use this skill whenever asked to prepare, review, or create a Trinidad and Tobago VAT return for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "Trinidad VAT", "T&T VAT", or any request involving Trinidad and Tobago VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Trinidad and Tobago VAT classification rules, return form mappings, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Trinidad VAT-related work.
---

# Trinidad and Tobago VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Trinidad and Tobago |
| Jurisdiction Code | TT |
| Primary Legislation | Value Added Tax Act, 1989 (as amended) |
| Supporting Legislation | VAT Regulations; Finance Act (annual amendments); Customs Act |
| Tax Authority | Board of Inland Revenue (BIR) |
| Filing Portal | https://www.ird.gov.tt (Inland Revenue Division Online) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires sign-off by a licensed Trinidad and Tobago accountant (ICATT member) |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: rate classification, return box assignment, input tax recovery, derived calculations. Tier 2: partial exemption, energy sector treatments, free-zone operations. Tier 3: complex group structures, advance rulings, transfer pricing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and BIR file number** [T1] -- unique taxpayer identifier
2. **VAT registration number** [T1] -- assigned by BIR upon registration
3. **VAT filing period** [T1] -- bi-monthly (standard: Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec)
4. **Industry/sector** [T2] -- impacts classification (energy sector, manufacturing, financial services)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input tax attribution required
6. **Does the business import goods?** [T1] -- impacts customs VAT treatment
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business in the energy/petrochemical sector?** [T2] -- special regimes may apply

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: VAT Rate Structure [T1]

**Legislation:** VAT Act 1989, Section 6; First Schedule; Second Schedule.

### Standard Rate

| Rate | Application |
|------|-------------|
| 12.5% | Standard rate on all taxable supplies and imports not otherwise specified [T1] |

### Zero-Rated Supplies (0%) [T1]

**Legislation:** VAT Act, First Schedule.

- Exports of goods
- International transport of goods and passengers
- Supplies of unprocessed food (basic food basket items -- rice, flour, sugar, milk, bread, fresh fruit, vegetables, fresh meat, fresh fish)
- Agricultural inputs (fertilizers, animal feed, seeds)
- Prescription drugs and pharmaceutical products
- Crude oil and natural gas (upstream supplies)
- Printed books and newspapers
- Water (piped, domestic use)

### Exempt Supplies (No VAT, No Input Credit) [T1]

**Legislation:** VAT Act, Second Schedule.

- Financial services (interest, foreign exchange, life insurance premiums)
- Residential rental (unfurnished)
- Medical and dental services (public and private)
- Educational services (approved institutions)
- Postage stamps (at face value)
- Burial and cremation services
- Land (sale of bare land)

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, NIS contributions, Health Surcharge, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act, Section 2 (definitions of taxable supply)

### 2b. Determine Counterparty Location [T1]
- Domestic (Trinidad and Tobago): supplier/customer in TT
- CARICOM: Jamaica, Barbados, Guyana, Suriname, Belize, Bahamas, Haiti, OECS states
- International: all other countries

### 2c. Determine VAT Rate [T1]
- Calculate from amounts: `rate = vat_amount / net_amount * 100`
- Normalize: 0% (zero-rated), 12.5% (standard), or exempt
- Boundaries: <= 1% = 0%; >= 10% = 12.5%
- **Legislation:** VAT Act, Section 6

### 2d. Determine Expense Category [T1]
- Capital goods: equipment, machinery, vehicles, furniture
- Inventory for resale: goods purchased for direct resale
- Operating expenses/overheads: everything else

---

## Step 3: VAT Return Form Structure [T1]

**The VAT return (Form VAT 1) is filed bi-monthly.**

### Part A -- Output Tax

| Box | Description |
|-----|-------------|
| 1 | Total value of taxable supplies at 12.5% |
| 2 | VAT on taxable supplies (Box 1 x 12.5%) |
| 3 | Total value of zero-rated supplies |
| 4 | Total value of exempt supplies |
| 5 | Total value of all supplies (Box 1 + Box 3 + Box 4) |
| 6 | VAT charged on imports (from customs entries) |
| 7 | Reverse charge VAT on imported services |
| 8 | Total output tax (Box 2 + Box 6 + Box 7) |

### Part B -- Input Tax

| Box | Description |
|-----|-------------|
| 9 | VAT on local purchases of goods and services |
| 10 | VAT on imports (from customs entries, claimable portion) |
| 11 | Total input tax (Box 9 + Box 10) |
| 12 | Input tax adjustments (blocked/apportioned) |
| 13 | Net allowable input tax (Box 11 - Box 12) |

### Part C -- Tax Payable / Refundable

| Box | Description | Calculation |
|-----|-------------|-------------|
| 14 | Net VAT (Box 8 - Box 13) |
| 15 | Credit brought forward |
| 16 | Net amount payable / (refundable) (Box 14 - Box 15) |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Act, Section 7 (imported services).

When a Trinidad and Tobago registered person receives services from a non-resident supplier:

1. The recipient must self-assess VAT at 12.5% on the value of the imported service [T1]
2. Report the self-assessed VAT as output tax (Box 7) [T1]
3. If the service is used in making taxable supplies, claim input tax (Box 9) [T1]
4. Net effect: zero for fully taxable businesses [T1]

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, dividends, loan repayments): NEVER reverse charge
- Services that would be exempt if supplied domestically: reverse charge applies but NO input credit
- Services consumed entirely outside Trinidad and Tobago: NOT subject to VAT

---

## Step 5: Deductibility Check

### Blocked Input Tax (No Recovery) [T1]

**Legislation:** VAT Act, Section 16; Section 17.

The following have ZERO VAT recovery:

- **Entertainment** -- meals, hospitality, amusement (unless business is in the hospitality trade) [T1]
- **Motor cars** -- purchase, lease, maintenance of motor cars (exception: car rental, taxi, driving school businesses) [T1]
- **Club subscriptions** -- sporting, social, recreational [T1]
- **Personal/domestic use** -- any goods or services for personal consumption [T1]
- **Goods/services for making exempt supplies** -- no input credit [T1]

### Registration-Based Recovery [T1]
- VAT-registered making taxable supplies: full recovery (subject to blocked categories)
- Non-registered: NO recovery
- Registered making only exempt supplies: NO recovery

### Partial Exemption / Apportionment [T2]

**Legislation:** VAT Act, Section 16(2).

If the business makes both taxable and exempt supplies:
- Directly attributable input tax: allocate to taxable or exempt
- Common input tax: apportion using: `Recovery % = (Taxable Supplies / Total Supplies) * 100`
- **Flag for reviewer: apportionment must be confirmed by licensed accountant.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual taxable supplies exceeding TTD 600,000 |
| Voluntary registration | Below TTD 600,000 (may register voluntarily if making taxable supplies) |

**Legislation:** VAT Act, Section 9 (registration threshold).

---

## Step 7: Filing Deadlines and Penalties [T1]

**Legislation:** VAT Act, Sections 31, 34, 35, 36.

### Filing Deadlines

| Period Type | Deadline |
|-------------|----------|
| Bi-monthly (standard) | 25th of the month following the end of the bi-monthly period [T1] |
| Example: Jan-Feb period | Due by 25 March [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | TTD 100 per day for each day the return is late (to a maximum) [T1] |
| Late payment | Interest at rate prescribed by the Minister (currently 20% per annum on unpaid tax) [T1] |
| Failure to register | Back-assessment of VAT plus penalties [T1] |
| Fraudulent return | Criminal penalties; fines and/or imprisonment [T1] |
| Failure to keep records | TTD 10,000 fine and/or 2 years imprisonment [T1] |

---

## Step 8: Tax Invoice Requirements [T1]

**Legislation:** VAT Act, Section 23.

A valid VAT tax invoice must contain:

1. The words "Tax Invoice"
2. Supplier's name, address, and VAT registration number
3. Customer's name and VAT registration number (B2B)
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
| Office supplies | 12.5% | Yes | Box 9 |
| Commercial rent | 12.5% | Yes | Box 9 |
| Residential rent (unfurnished) | Exempt | No | Not on return |
| Electricity (commercial) | 12.5% | Yes | Box 9 |
| Telephone/internet | 12.5% | Yes | Box 9 |
| Motor car | 12.5% | BLOCKED | Box 12 (adjustment) |
| Entertainment | 12.5% | BLOCKED | Box 12 (adjustment) |
| Professional fees | 12.5% | Yes | Box 9 |
| Insurance (general) | 12.5% | Yes | Box 9 |
| Insurance (life) | Exempt | No | N/A |
| Basic food items | 0% | N/A (no VAT charged) | N/A |
| Prescription drugs | 0% | N/A | N/A |
| Equipment/machinery | 12.5% | Yes | Box 9 |

### Sales

| Category | VAT Treatment | Return Box |
|----------|--------------|------------|
| Domestic sale of goods (standard) | 12.5% | Box 1, Box 2 |
| Export of goods | 0% | Box 3 |
| Services to local customers | 12.5% | Box 1, Box 2 |
| Services to overseas customers | 0% (export) | Box 3 |
| Exempt financial services | Exempt | Box 4 |
| Sale of bare land | Exempt | Box 4 |

### Imports

| Category | VAT Treatment | Return Box |
|----------|--------------|------------|
| Goods imported for resale | 12.5% at customs | Box 6 (output), Box 10 (input) |
| Services imported (reverse charge) | Self-assess 12.5% | Box 7 (output), Box 9 (input) |

---

## Step 10: Energy Sector Special Rules [T2]

**Legislation:** VAT Act, First Schedule; Petroleum Taxes Act.

Trinidad and Tobago's economy is heavily dependent on the energy sector. Special considerations:

- Upstream oil and gas (exploration, production): supplies of crude oil and natural gas are zero-rated [T1]
- Services to energy companies: generally taxable at 12.5% [T1]
- LNG exports: zero-rated as exports [T1]
- Petrochemical manufacturing: standard 12.5% applies to domestic sales; exports zero-rated [T1]
- Capital equipment imported for energy sector: may qualify for customs duty concessions but VAT still applies at 12.5% (input credit available) [T2]
- Flag for reviewer: energy sector transactions often involve complex contractual arrangements. Verify supply classification.

---

## Step 11: CARICOM Trade [T2]

**Legislation:** VAT Act; CARICOM Revised Treaty of Chaguaramas.

- Goods imported from CARICOM member states: VAT at 12.5% collected by customs (same as other imports) [T1]
- Services from CARICOM providers: reverse charge at 12.5% [T1]
- Exports to CARICOM: zero-rated (same as other exports) [T1]
- CARICOM does NOT have an EU-style single-market VAT system -- each country collects its own VAT independently [T1]
- Double-taxation relief may apply to certain transactions [T2] -- flag for reviewer

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT classification -- it is deterministic from facts
- NEVER allow input tax credit on blocked categories (entertainment, motor cars, clubs)
- NEVER apply reverse charge to out-of-scope categories (salaries, NIS, PAYE)
- NEVER allow non-registered persons to claim input tax credits
- NEVER confuse zero-rated (input credit allowed) with exempt (NO input credit)
- NEVER ignore the TTD 600,000 registration threshold
- NEVER file a return without verifying the VAT registration number
- NEVER treat CARICOM imports differently from other imports for VAT purposes (same rate applies)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 12: Edge Case Registry

### EC1 -- Imported services from US software provider [T1]
**Situation:** TT registered business subscribes to US-based cloud software. No VAT on invoice.
**Resolution:** Reverse charge applies. Self-assess VAT at 12.5%. Report as output tax (Box 7). Claim input tax (Box 9) if used for taxable supplies. Net effect = zero.
**Legislation:** VAT Act, Section 7.

### EC2 -- Motor vehicle for delivery fleet [T2]
**Situation:** Client purchases a delivery van for transporting goods.
**Resolution:** Delivery vehicles (vans, trucks) designed for goods transport are generally NOT blocked under the motor car restriction. Motor car restriction applies to passenger vehicles. Flag for reviewer: confirm vehicle classification (motor car vs. commercial vehicle).
**Legislation:** VAT Act, Section 17.

### EC3 -- Mixed supply: financial services + advisory fees [T2]
**Situation:** Bank charges include both exempt interest and taxable advisory/management fees.
**Resolution:** Split by nature. Interest = exempt. Advisory/management fees = taxable at 12.5%. Input tax on costs attributable to advisory services is recoverable. Flag for reviewer to confirm split.

### EC4 -- Credit notes [T1]
**Situation:** Client issues a credit note for returned goods.
**Resolution:** Reduce output tax by the VAT on the credit note. Report net figures. Do not create a separate negative entry in a different box.

### EC5 -- Furnished residential rental [T2]
**Situation:** Client rents out a furnished apartment.
**Resolution:** Unfurnished residential rental is exempt. Furnished rental may be treated as a taxable supply (it is closer to accommodation/hotel). Flag for reviewer: confirm treatment based on nature and duration of rental.
**Legislation:** VAT Act, Second Schedule.

### EC6 -- VAT refund processing [T2]
**Situation:** Client has excess input tax credits accumulated over multiple periods.
**Resolution:** Excess credits are carried forward. Refund claims may be filed but BIR processing can be slow (6-12 months). Flag for reviewer: advise client on refund application process and documentation requirements.
**Legislation:** VAT Act, Section 29.

### EC7 -- Imports under duty-free concessions [T2]
**Situation:** Client imports machinery under a duty-free concession from the government.
**Resolution:** Duty-free concession may waive customs duty but NOT necessarily VAT. Confirm whether the concession order specifically includes VAT relief. If VAT was paid, input credit is available. Flag for reviewer.

### EC8 -- Digital services to non-resident consumers [T2]
**Situation:** TT-based company provides digital services to consumers in other countries.
**Resolution:** Services consumed outside TT may qualify as zero-rated exports. However, the place of supply rules must be carefully considered. Flag for reviewer: confirm place of supply and whether zero-rating applies.
**Legislation:** VAT Act, Section 11 (place of supply).

### EC9 -- Construction services on real property [T1]
**Situation:** Contractor provides building renovation services.
**Resolution:** Construction services are taxable at 12.5%. Input VAT on construction materials and subcontractor services is fully recoverable for the contractor. For the property owner: input VAT recoverable only if the property is used for taxable supplies.

### EC10 -- Sale of a going concern [T2]
**Situation:** Client sells entire business as a going concern.
**Resolution:** Transfer of a going concern may be treated as outside the scope of VAT. However, this depends on the specific facts and whether the business is transferred as a whole. Flag for reviewer: confirm treatment and documentation requirements.

---

## Step 12a: Sector-Specific Guidance [T2]

### Energy Sector (Detailed)

**Legislation:** Petroleum Taxes Act; VAT Act.

- **Upstream (exploration and production)**: crude oil and natural gas supplies are zero-rated [T1]
- **Downstream (refining, marketing)**: domestic sales of refined petroleum products -- subject to fuel subsidy/tax arrangements, generally VAT applies [T2]
- **LNG exports**: zero-rated as exports [T1]
- **Petrochemical manufacturing**: standard 12.5% on domestic; zero-rated on exports [T1]
- **Service companies to energy sector**: 12.5% on all services [T1]
- **Capital equipment imported for energy operations**: VAT at 12.5% at customs; input credit available [T1]
- **Production Sharing Contracts (PSCs)**: complex arrangements -- flag for specialist review [T3]

### Financial Services

- **Interest income**: exempt [T1]
- **Banking fees and commissions**: taxable at 12.5% [T1]
- **Insurance premiums (life)**: exempt [T1]
- **Insurance premiums (general)**: taxable at 12.5% [T1]
- **Securities trading**: exempt [T1]
- **Credit card processing fees**: taxable at 12.5% [T1]

### Construction and Real Estate

- **Construction services**: taxable at 12.5% [T1]
- **Sale of new commercial property**: taxable at 12.5% [T2]
- **Sale of residential property**: exempt [T1]
- **Commercial rental**: taxable at 12.5% [T1]
- **Residential rental (unfurnished)**: exempt [T1]
- **Construction materials**: taxable at 12.5% [T1]

### Agriculture

- **Unprocessed food (basic food basket)**: zero-rated [T1]
- **Processed food**: taxable at 12.5% [T1]
- **Agricultural inputs**: zero-rated [T1]
- **Fishing**: unprocessed fish is zero-rated [T1]

---

## Step 12b: Books and Records Requirements [T1]

**Legislation:** VAT Act, Section 55.

All VAT-registered persons must maintain:

- **Sales records**: all tax invoices issued, credit/debit notes, export documentation
- **Purchase records**: all purchase invoices with VAT breakdowns, import entries
- **Import records**: customs declarations showing VAT paid
- **VAT account**: summary showing output VAT collected, input VAT claimed, net position
- **Bank statements**: reconciled to business records
- Records must be retained for a minimum of **6 years**
- Records must be in English and available for BIR inspection

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

### Test 1 -- Standard local purchase, 12.5% VAT
**Input:** TT supplier, office furniture, gross TTD 11,250, VAT TTD 1,250, net TTD 10,000, registered person.
**Expected output:** Box 9 = TTD 1,250 input tax. Full recovery.

### Test 2 -- Export sale, zero-rated
**Input:** Registered person exports goods to Barbados, net TTD 50,000. VAT at 0%.
**Expected output:** Box 3 = TTD 50,000. No output VAT. Input tax fully recoverable.

### Test 3 -- Motor car purchase, blocked
**Input:** Registered person purchases a sedan for TTD 250,000, VAT TTD 31,250.
**Expected output:** Box 12 adjustment = TTD 31,250. Net input credit = zero. VAT is blocked.

### Test 4 -- Imported services, reverse charge
**Input:** UK law firm provides legal advice, GBP 5,000 (~ TTD 45,000). No VAT on invoice.
**Expected output:** Box 7 output = TTD 5,625 (12.5%). Box 9 input = TTD 5,625. Net effect = zero.

### Test 5 -- Exempt supply (life insurance)
**Input:** Insurance company earns life insurance premiums TTD 200,000.
**Expected output:** Box 4 = TTD 200,000. No output VAT. Input tax on related costs NOT recoverable.

### Test 6 -- Zero-rated basic food sale
**Input:** Registered grocery sells rice and flour for TTD 15,000.
**Expected output:** Box 3 = TTD 15,000. No output VAT. Input tax on related purchases IS recoverable.

### Test 7 -- Mixed business apportionment
**Input:** Registered business: 80% taxable, 20% exempt supplies. Common overhead VAT = TTD 10,000.
**Expected output:** Flag T2. Apportioned input = TTD 8,000 (80%). Blocked = TTD 2,000 (20%).

### Test 8 -- Entertainment expense
**Input:** Client entertaining at restaurant, TTD 5,625 inclusive of VAT TTD 625.
**Expected output:** VAT TTD 625 BLOCKED. No input credit. Full TTD 5,625 is a cost.

---

## Contribution Notes

If adapting this skill for another Caribbean jurisdiction:

1. Replace all legislation references with the equivalent national legislation.
2. Replace the VAT rate (12.5%) with your jurisdiction's rate.
3. Replace the registration threshold (TTD 600,000) with your jurisdiction's equivalent.
4. Replace blocked categories with your jurisdiction's non-deductible categories.
5. Have a licensed accountant validate every T1 rule before publishing.
6. Add your own edge cases for known ambiguous situations.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
