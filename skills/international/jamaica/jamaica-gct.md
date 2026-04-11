---
name: jamaica-gct
description: Use this skill whenever asked to prepare, review, or create a Jamaica General Consumption Tax (GCT) return for any client. Trigger on phrases like "prepare GCT return", "do the GCT", "fill in GCT", "Jamaica tax return", or any request involving Jamaica consumption tax filing. Also trigger when classifying transactions for GCT purposes from bank statements, invoices, or other source data. This skill contains the complete Jamaica GCT classification rules, return form mappings, deductibility rules, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any GCT-related work.
---

# Jamaica GCT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Jamaica |
| Jurisdiction Code | JM |
| Primary Legislation | General Consumption Tax Act, 1991 (as amended) |
| Supporting Legislation | GCT Regulations; Special Provisions Act; Fiscal Incentives legislation |
| Tax Authority | Tax Administration Jamaica (TAJ) |
| Filing Portal | https://www.jamaicatax.gov.jm (TAJ Online) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires sign-off by a licensed Jamaican accountant |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: rate classification, return box assignment, input tax recovery rules, derived calculations. Tier 2: partial exemption apportionment, sector-specific reliefs, tourism sector concessions. Tier 3: complex group structures, rulings, transfer pricing. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TRN (Taxpayer Registration Number)** [T1] -- 9-digit TRN
2. **GCT registration status** [T1] -- registered or not registered
3. **GCT filing period** [T1] -- monthly (standard) or bi-monthly (approved small taxpayers)
4. **Industry/sector** [T2] -- impacts classification (e.g., tourism sector has special provisions)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input tax attribution required
6. **Does the business import goods?** [T1] -- impacts customs GCT treatment
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business an approved farmer or manufacturer?** [T2] -- may qualify for zero-rating or reduced rate

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

---

## Step 1: GCT Rate Structure [T1]

**Legislation:** General Consumption Tax Act, Section 3; First Schedule; Second Schedule.

### Standard Rate

| Rate | Application |
|------|-------------|
| 15% | Standard rate on all taxable supplies and imports not otherwise specified [T1] |

### Special Rates [T1]

| Rate | Application |
|------|-------------|
| 25% | Telephone services (including phone cards) and handsets [T1] |
| ~10% | Hotels and other businesses in the tourism sector (effective rate) [T2] |

### Zero-Rated Supplies (0%) [T1]

- Exports of goods
- International transport services
- Supplies to diplomats and approved international organizations
- Certain agricultural inputs (approved list)
- Supplies to approved free-zone entities

### Exempt Supplies (No GCT, No Input Credit) [T1]

**Legislation:** GCT Act, Second Schedule.

- Unprocessed agricultural produce (fresh fruits, vegetables, ground provisions)
- Basic food items (specified in Second Schedule): flour, rice, cornmeal, counter flour, chicken backs and necks
- Medical and dental services
- Educational services (approved institutions)
- Financial services (interest, life insurance premiums)
- Residential rental
- Public transportation
- Water (piped, up to specified threshold)
- Electricity (up to specified threshold for domestic consumers)
- Petroleum products (subject to Special Consumption Tax instead)

### Special Provisions [T2]

- **Tourism sector:** Accommodation and tourism-related services may have specific treatments. Confirm with reviewer.
- **Free-zone enterprises:** Supplies to and from free zones have special rules. Confirm with reviewer.

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output GCT) or Purchase (input GCT)
- Salaries, PAYE, NIS contributions, NHT contributions, Education Tax, loan repayments, dividends = OUT OF SCOPE (never on GCT return)
- **Legislation:** GCT Act, Section 2 (definitions of taxable supply)

### 2b. Determine Counterparty Location [T1]
- Domestic (Jamaica): supplier/customer in JM
- International: supplier/customer outside Jamaica
- CARICOM: Barbados, Trinidad and Tobago, Guyana, Suriname, Belize, Bahamas, Haiti, Antigua, Dominica, Grenada, St Kitts, St Lucia, St Vincent, Montserrat

### 2c. Determine GCT Rate [T1]
- Calculate from amounts: `rate = gct_amount / net_amount * 100`
- Normalize: 0% (zero-rated), 15% (standard), or exempt
- **Legislation:** GCT Act, Section 3 (rate), First Schedule (zero-rated), Second Schedule (exempt)

### 2d. Determine Expense Category [T1]
- Capital goods: equipment, machinery, vehicles, furniture above JMD threshold
- Inventory for resale: goods purchased for direct resale
- Operating expenses/overheads: everything else
- **Legislation:** GCT Act, Section 16 (input tax credit)

---

## Step 3: GCT Return Form Structure [T1]

**The GCT return (Form GCT-R) consists of the following sections:**

### Output Tax (GCT Collected/Charged)

| Line | Description | Source |
|------|-------------|--------|
| 1 | Total taxable supplies at standard rate (15%) | Net value of all 15% sales |
| 2 | GCT on taxable supplies | Line 1 x 15% |
| 3 | Zero-rated supplies | Net value of all 0% supplies |
| 4 | Exempt supplies | Net value of all exempt supplies |
| 5 | Total supplies | Line 1 + Line 3 + Line 4 |
| 6 | GCT on imports (from customs entries) | Per C78 customs declaration |
| 7 | Total output tax | Line 2 + Line 6 |

### Input Tax (GCT Paid on Purchases)

| Line | Description | Source |
|------|-------------|--------|
| 8 | GCT paid on local purchases | Sum of input GCT on domestic purchases |
| 9 | GCT paid on imports | From customs entries (C78) |
| 10 | Total input tax | Line 8 + Line 9 |
| 11 | Input tax adjustments (disallowed/apportioned) | Blocked + partial exemption |
| 12 | Net input tax claimable | Line 10 - Line 11 |

### Tax Payable / Refundable

| Line | Description | Calculation |
|------|-------------|-------------|
| 13 | Net GCT payable/(refundable) | Line 7 - Line 12 |
| 14 | Credit brought forward | From prior period |
| 15 | Net amount payable/(refundable) | Line 13 - Line 14 |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** GCT Act, Section 4A (services imported into Jamaica).

When a Jamaican registered person receives services from a non-resident supplier:

1. The recipient must self-assess GCT at 15% on the value of the imported service [T1]
2. Report the self-assessed GCT as output tax on the return [T1]
3. If the service is used in making taxable supplies, the same amount may be claimed as input tax [T1]
4. Net effect: zero for fully taxable businesses [T1]

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories (wages, dividends, loan repayments): NEVER reverse charge
- Services that would be exempt if supplied domestically: reverse charge applies but NO input credit
- Services consumed entirely outside Jamaica: NOT subject to GCT

---

## Step 5: Deductibility Check

### Blocked Input Tax (No Recovery) [T1]

**Legislation:** GCT Act, Section 16(2); Section 17.

The following have ZERO GCT recovery:

- **Entertainment expenses** -- meals, drinks, amusement, recreation (unless the business is in the entertainment/hospitality trade) [T1]
- **Motor cars** -- acquisition, lease, or maintenance of motor cars (exception: car rental businesses, taxi operators, driving schools) [T1]
- **Club subscriptions and membership fees** -- sporting, social, or recreational clubs [T1]
- **Personal use items** -- any goods or services not used in the course of business [T1]
- **Goods and services used to make exempt supplies** -- no input credit on purchases attributable to exempt outputs [T1]

### Registration-Based Recovery [T1]
- GCT-registered person making taxable supplies: full recovery (subject to blocked categories)
- Non-registered person: NO recovery (GCT is a cost)
- Registered person making only exempt supplies: NO recovery

### Partial Exemption / Apportionment [T2]

**Legislation:** GCT Act, Section 16(3).

If the business makes both taxable and exempt supplies:
- Directly attributable input tax: allocate to taxable or exempt supplies
- Common/overhead input tax: apportion using the formula:
  `Recovery % = (Taxable Supplies / Total Supplies) * 100`
- **Flag for reviewer: apportionment calculation must be confirmed by licensed accountant before applying.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory GCT registration | Annual taxable supplies exceeding JMD 15,000,000 |
| Voluntary registration | Below JMD 15,000,000 (may register voluntarily) |
| Small taxpayer bi-monthly filing | Approved by TAJ for smaller businesses |

**Legislation:** GCT Act, Section 8 (registration threshold).

---

## Step 7: Filing Deadlines and Penalties [T1]

**Legislation:** GCT Act, Sections 28, 30, 31; Tax Administration Jamaica (Procedures) Act.

### Filing Deadlines

| Period Type | Deadline |
|-------------|----------|
| Monthly filer | 25th of the month following the return period [T1] |
| Bi-monthly filer | 25th of the month following the end of the bi-monthly period [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | JMD 5,000 per month or part thereof (minimum) [T1] |
| Late payment | Interest at prescribed rate (currently 1.5% per month or part thereof) on unpaid tax [T1] |
| Failure to register | Penalties plus back-assessment of GCT that should have been collected [T1] |
| Fraudulent return | Criminal prosecution; fines up to JMD 2,000,000 and/or imprisonment [T1] |
| Failure to issue tax invoice | JMD 50,000 per invoice [T1] |

### Interest on Late Payment [T1]
- Interest accrues from the due date until the date of payment
- Rate is prescribed by the Minister of Finance (currently approximately 1.5% per month)

---

## Step 8: Tax Invoice Requirements [T1]

**Legislation:** GCT Act, Section 20.

A valid GCT tax invoice must contain:

1. The words "Tax Invoice" prominently displayed
2. Supplier's name, address, and TRN
3. Customer's name and TRN (for B2B supplies above JMD 10,000)
4. Date of issue
5. Sequential invoice number
6. Description of goods or services supplied
7. Quantity and unit price
8. Total value excluding GCT
9. GCT amount
10. Total value including GCT

**Simplified invoice:** For supplies under JMD 10,000, a simplified invoice may be used (supplier details and total inclusive of GCT).

---

## Step 9: Classification Matrix -- Common Transactions [T1]

### Domestic Purchases

| Category | GCT Treatment | Input Credit | Return Line |
|----------|--------------|--------------|-------------|
| Office supplies (15% GCT) | Taxable | Yes (if for taxable business) | Line 8 |
| Rent (commercial property) | Taxable at 15% | Yes | Line 8 |
| Rent (residential) | Exempt | No | Not reported |
| Electricity (commercial) | Taxable at 15% | Yes | Line 8 |
| Electricity (residential, <= 250 kWh/month) | GCT waived (2025/2026 budget) | No | N/A |
| Electricity (residential, > 250 kWh/month) | 7% (reduced from 15% per 2025/2026 budget) | N/A | N/A |
| Telephone/internet | Telephone services at 25%; internet at 15% | Yes | Line 8 |
| Motor car purchase | Taxable at 15% | BLOCKED | Line 11 (adjustment) |
| Entertainment | Taxable at 15% | BLOCKED | Line 11 (adjustment) |
| Professional fees (legal, accounting) | Taxable at 15% | Yes | Line 8 |
| Insurance (general) | Taxable at 15% | Yes | Line 8 |
| Insurance (life) | Exempt | No | Not reported |
| Basic food items (Second Schedule) | Exempt | No | Not reported |
| Equipment/machinery | Taxable at 15% | Yes | Line 8 |
| Fuel | Subject to SCT, not GCT | No GCT component | N/A |

### Sales (Output Tax)

| Category | GCT Treatment | Return Line |
|----------|--------------|-------------|
| Domestic sale of goods (standard) | 15% | Line 1, Line 2 |
| Export of goods | 0% | Line 3 |
| Services to local customers | 15% | Line 1, Line 2 |
| Services to overseas customers | 0% (export of services) | Line 3 |
| Sale of exempt items | Exempt | Line 4 |
| Rental income (commercial) | 15% | Line 1, Line 2 |
| Rental income (residential) | Exempt | Line 4 |

### Imports

| Category | GCT Treatment | Return Line |
|----------|--------------|-------------|
| Goods imported for resale | GCT paid at customs (15%) | Line 6 (output), Line 9 (input) |
| Goods imported for own use | GCT paid at customs (15%) | Line 6 (output), Line 9 (input, if for taxable use) |
| Services imported (reverse charge) | Self-assess at 15% | Line 7 (output), Line 10 (input, if for taxable use) |

---

## Step 10: Special Industry Rules [T2]

### Tourism Sector
- Hotels and tourism operators registered under the Jamaica Tourist Board may have specific GCT treatments
- Tourism Enhancement Fund levy is separate from GCT
- Flag for reviewer: confirm applicable concessions with TAJ

### Agriculture
- Unprocessed agricultural produce is exempt
- Agricultural inputs may qualify for zero-rating under approved farmer scheme
- Flag for reviewer: verify approved farmer status with TAJ

### Manufacturing
- Manufacturers may qualify for GCT relief on raw materials under approved manufacturer scheme
- Flag for reviewer: confirm approved status and applicable orders

### Financial Services
- Most financial services are exempt from GCT
- Fees and commissions charged by financial institutions may be taxable
- Flag for reviewer: distinguish between exempt financial services and taxable fee-based services [T2]

---

## Step 11: Withholding GCT [T1]

**Legislation:** GCT Act, Section 19A.

Certain government entities and large taxpayers may be designated as GCT withholding agents:
- Withholding agents deduct GCT from payments to suppliers and remit directly to TAJ
- The supplier receives a withholding certificate to claim credit for GCT withheld
- Withholding rate: two-thirds of the GCT amount (i.e., 10% of the GCT-exclusive value) [T2]
- Flag for reviewer: confirm current withholding rate and whether client is a designated withholding agent

---

## PROHIBITIONS [T1]

- NEVER let AI guess GCT classification -- it is deterministic from facts
- NEVER allow input tax credit on blocked categories (entertainment, motor cars, clubs)
- NEVER apply reverse charge to out-of-scope categories (salaries, PAYE, NIS, NHT)
- NEVER allow non-registered persons to claim input tax credits
- NEVER confuse zero-rated (input credit allowed) with exempt (NO input credit)
- NEVER apply GCT to petroleum products (subject to SCT instead)
- NEVER ignore the JMD 15,000,000 registration threshold -- businesses above this MUST register
- NEVER file a return without verifying the TRN and registration status
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 12: Edge Case Registry

### EC1 -- Imported services from a CARICOM supplier [T1]
**Situation:** Jamaican registered business receives consulting services from a Trinidad-based firm. No GCT on invoice.
**Resolution:** Reverse charge applies. Self-assess GCT at 15% on the value of the service. Report as output tax. Claim input tax credit if used for taxable supplies.
**Legislation:** GCT Act, Section 4A.

### EC2 -- Mixed supply: taxable and exempt components [T2]
**Situation:** A single invoice includes both taxable and exempt items.
**Resolution:** Split by line item. Apply 15% GCT to taxable components; exempt components carry no GCT. If line items are not broken out, flag for reviewer to confirm split with client.

### EC3 -- Motor vehicle used exclusively for business (delivery, taxi) [T2]
**Situation:** Client purchases a motor vehicle claiming it is used exclusively for deliveries.
**Resolution:** Motor car GCT is generally blocked. Exception only for: taxi operators, car rental businesses, driving schools, and vehicles designed exclusively for the transport of goods (trucks, vans). Flag for reviewer: confirm vehicle type and business use before allowing input credit.
**Legislation:** GCT Act, Section 16(2).

### EC4 -- GCT on customs brokerage fees [T1]
**Situation:** Client pays a customs broker to clear imported goods. Broker charges 15% GCT on their fee.
**Resolution:** The GCT on the brokerage fee is a legitimate input tax credit (it is a service, not a blocked category). Claim on Line 8. Separate from the GCT paid on the imported goods themselves (Line 9).

### EC5 -- Credit notes / returns [T1]
**Situation:** Client issues a credit note to a customer for returned goods.
**Resolution:** Reduce output tax by the GCT component of the credit note. Reduce taxable supplies by the net amount. Report net figures on the return. Do not create a separate negative entry.
**Legislation:** GCT Act, Section 21.

### EC6 -- Supplies to free-zone entities [T2]
**Situation:** Client sells goods to a company operating within a Jamaica Special Economic Zone (formerly Free Zone).
**Resolution:** Supplies to approved free-zone entities may be zero-rated. Confirm the purchaser holds a valid free-zone licence. Flag for reviewer: verify free-zone status and applicable order.
**Legislation:** Special Economic Zones Act, 2016.

### EC7 -- Staff meals and entertainment [T1]
**Situation:** Restaurant purchases food items used to prepare meals for staff.
**Resolution:** Staff meals are treated as entertainment/personal benefit. GCT on inputs used for staff meals is BLOCKED. Exception: if the business is a hotel or restaurant and staff meals are an integral part of the employment contract, [T2] flag for reviewer.
**Legislation:** GCT Act, Section 16(2).

### EC8 -- Second-hand goods [T1]
**Situation:** Client purchases second-hand equipment from a non-registered person (no GCT charged).
**Resolution:** No GCT was charged, so no input tax credit arises. The full purchase price is a cost. Jamaica does not have a margin scheme for second-hand goods like the EU.

### EC9 -- E-commerce and digital services [T2]
**Situation:** Foreign e-commerce company sells digital services to Jamaican consumers.
**Resolution:** Non-resident digital service providers may be required to register for GCT. Under recent amendments, digital economy transactions are being brought within the GCT net. Flag for reviewer: confirm current registration obligations for non-resident digital suppliers.

### EC10 -- Construction services [T1]
**Situation:** Client pays contractor for building renovation.
**Resolution:** Construction services are taxable at 15%. GCT applies to the full service charge. Input GCT on construction costs is recoverable if the building is used for taxable business purposes.

---

## Step 12a: Sector-Specific Guidance [T2]

### Tourism Sector

- **Hotels and guest houses**: GCT at 15% on room charges and services [T1]
- **Tourism Enhancement Fund (TEF)**: separate from GCT, levied on accommodation. NOT reported on GCT return [T1]
- **All-inclusive resorts**: GCT applies to the total package price [T1]
- **Tour operator services**: taxable at 15% [T1]
- **Craft vendors in tourist areas**: must register if above threshold [T2]
- Flag for reviewer: tourism sector has multiple overlapping levies (GCT, TEF, accommodation tax)

### Financial Services

- **Interest income**: exempt from GCT [T1]
- **Banking fees and commissions**: taxable at 15% [T1]
- **Insurance premiums (life)**: exempt [T1]
- **Insurance premiums (general)**: taxable at 15% [T1]
- **Foreign exchange transactions**: exempt [T1]
- Flag for reviewer: distinguish exempt financial intermediation from taxable fee-based services

### Agriculture

- **Unprocessed produce (fresh fruits, vegetables, ground provisions)**: exempt [T1]
- **Processed food products**: taxable at 15% (unless on exempt basic food list) [T1]
- **Approved Farmer Scheme**: farmers may purchase inputs GCT-free with TAJ approval [T2]
- **Agricultural equipment**: may qualify for GCT relief under incentive programmes [T2]
- Flag for reviewer: confirm approved farmer status

### Manufacturing

- **Manufacturing inputs**: taxable at 15%, input credit available [T1]
- **Finished goods sold domestically**: 15% [T1]
- **Exports**: zero-rated [T1]
- **Approved manufacturer scheme**: may purchase inputs GCT-free [T2]
- Flag for reviewer: confirm approved manufacturer status with TAJ

### Construction and Real Estate

- **Construction services**: taxable at 15% [T1]
- **Sale of real property**: exempt from GCT (subject to Transfer Tax and Stamp Duty instead) [T1]
- **Commercial rental**: taxable at 15% [T1]
- **Residential rental**: exempt [T1]
- **Construction materials**: taxable at 15% [T1]

---

## Step 12b: Books and Records Requirements [T1]

**Legislation:** GCT Act, Section 25; Tax Administration Jamaica (Procedures) Act.

All GCT-registered persons must maintain:

- **Sales records**: all sales invoices/receipts, tax invoices issued, credit notes
- **Purchase records**: all purchase invoices with GCT breakdowns, customs entries (C78)
- **Import records**: customs declarations showing GCT paid at importation
- **Bank statements**: reconciled to sales and purchase records
- **GCT account**: summary ledger showing output GCT collected, input GCT paid, net position
- Records must be retained for a minimum of **6 years** from the end of the accounting period
- Records must be available for TAJ inspection at the registered business address

---

## Step 13: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

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

### Test 1 -- Standard local purchase, 15% GCT overhead
**Input:** Jamaican supplier, office supplies, gross JMD 115,000, GCT JMD 15,000, net JMD 100,000, registered person making taxable supplies.
**Expected output:** Line 8 input tax = JMD 15,000. Full input tax recovery.

### Test 2 -- Export sale, zero-rated
**Input:** Registered person exports goods to US customer, net value JMD 500,000. GCT at 0%.
**Expected output:** Line 3 = JMD 500,000. No output GCT. Input tax on related purchases is fully recoverable.

### Test 3 -- Motor car purchase, blocked
**Input:** Registered person purchases a sedan, JMD 5,000,000 net, GCT JMD 750,000.
**Expected output:** Line 8 = JMD 750,000 (gross input), Line 11 adjustment = JMD 750,000 (blocked). Net input credit = zero.

### Test 4 -- Imported services, reverse charge
**Input:** US-based consultant provides marketing services, USD 2,000 (~ JMD 310,000). No GCT on invoice.
**Expected output:** Self-assess output GCT = JMD 46,500 (15%). Claim input GCT = JMD 46,500. Net effect = zero.

### Test 5 -- Exempt supply (residential rental)
**Input:** Registered person earns residential rental income JMD 80,000/month.
**Expected output:** Line 4 = JMD 80,000. No output GCT. Input tax on expenses attributable to residential rental is NOT recoverable.

### Test 6 -- Mixed business (taxable + exempt)
**Input:** Registered person makes 70% taxable and 30% exempt supplies. Common overhead GCT = JMD 100,000.
**Expected output:** Flag T2. Apportioned input credit = JMD 70,000 (70%). Blocked amount = JMD 30,000 (30%). Reviewer must confirm apportionment.

### Test 7 -- GCT on imports at customs
**Input:** Registered person imports goods from China, CIF value JMD 1,000,000. GCT at 15% = JMD 150,000 paid at customs.
**Expected output:** Line 6 = JMD 150,000 (output, customs GCT). Line 9 = JMD 150,000 (input, customs GCT). Net effect on return = zero (if goods are for taxable resale).

### Test 8 -- Entertainment expense, blocked
**Input:** Registered person takes clients to dinner. Restaurant bill JMD 23,000 inclusive of GCT JMD 3,000.
**Expected output:** GCT of JMD 3,000 is BLOCKED. No input tax credit. Full JMD 23,000 is a cost.

---

## Contribution Notes

If adapting this skill for another Caribbean jurisdiction:

1. Replace all legislation references with the equivalent national legislation.
2. Replace GCT rates with your jurisdiction's standard and reduced rates.
3. Replace the registration threshold (JMD 15,000,000) with your jurisdiction's equivalent.
4. Replace blocked categories with your jurisdiction's non-deductible categories.
5. Replace the return form structure with your jurisdiction's return form.
6. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
7. Add your own edge cases for known ambiguous situations.
8. Run all test suite cases against your jurisdiction's rules and replace expected outputs.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
