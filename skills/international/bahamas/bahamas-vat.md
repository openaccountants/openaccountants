---
name: bahamas-vat
description: Use this skill whenever asked to prepare, review, or advise on Bahamas VAT returns, VAT registration, or VAT classification. Trigger on phrases like "Bahamas VAT", "Bahamian VAT", "Bahamas tax return", "DIR Bahamas", "Department of Inland Revenue Bahamas", or any request involving Bahamas VAT compliance. The Bahamas imposes VAT at 10% under the Value Added Tax Act 2014. The Department of Inland Revenue (DIR) administers the tax. ALWAYS read this skill before handling any Bahamas VAT work.
---

# Bahamas VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | The Bahamas (Commonwealth of The Bahamas) |
| Jurisdiction Code | BS |
| Primary Legislation | Value Added Tax Act 2014 (as amended) |
| Supporting Legislation | VAT Regulations; VAT Rules; Customs Management Act |
| Tax Authority | Department of Inland Revenue (DIR) |
| Filing Portal | https://inlandrevenue.finance.gov.bs (VAT online portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by licensed Bahamian tax practitioner |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: standard rate, exempt supplies, zero-rated supplies, registration, filing deadlines. Tier 2: financial services exemption, tourism sector treatment, input apportionment. Tier 3: complex import schemes, investment fund treatment, cross-island supply chains. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Business name and TIN (Taxpayer Identification Number)** [T1]
2. **VAT registration status** [T1] -- registered or not
3. **VAT period** [T1] -- monthly, bi-monthly, quarterly, or annual (based on turnover)
4. **Industry/sector** [T2] -- impacts exemptions
5. **Does the business make exempt supplies?** [T2] -- if yes, input VAT apportionment required
6. **Does the business import goods?** [T1] -- customs VAT treatment
7. **Does the business export goods or services?** [T1] -- zero-rating
8. **Turnover bracket** [T1] -- determines filing frequency

**If items 1-3 are unknown, STOP. Do not classify transactions.**

---

## Step 1: VAT Rate Structure [T1]

### Standard Rate

| Rate | Application |
|------|-------------|
| **10%** | Standard rate on most goods and services |

**Legislation:** VAT Act 2014, as amended. The rate was increased from 7.5% to 12% in 2018, then reduced to 10% effective January 1, 2022.

### Reduced Rate [T1]

| Rate | Application |
|------|-------------|
| **5%** | Food sold in food stores (effective 1 April 2025). Includes fresh fruits, vegetables, baby food, frozen foods, grocery staples. Does NOT apply to prepared food (restaurants, deli counters, ready-to-eat meals). [T1] |
| **5%** | Baby and adult diapers, feminine hygiene products, medications, and medical supplies (effective 1 September 2025). [T1] |

**NOTE:** Effective 1 April 2026 VAT on unprepared food (grocery items) is being reduced from 5% to 0% (zero-rated). Verify current status before filing. [T2]

### Rate History [T1]

| Period | Rate |
|--------|------|
| January 2015 - June 2018 | 7.5% (breadbasket items zero-rated) |
| July 2018 - December 2021 | 12% (breadbasket items zero-rated) |
| January 2022 - March 2025 | 10% (breadbasket zero-rating removed; all food at 10%) |
| April 2025 - present | 10% standard; 5% on food in food stores and certain essentials |

### Zero-Rated Supplies (0% VAT, Input VAT Recoverable) [T1]

- Exports of goods outside The Bahamas [T1]
- International transport of goods and passengers [T1]
- Certain supplies to other VAT-registered businesses in specific contexts [T2]

### Exempt Supplies (No VAT, No Input Recovery) [T1]

The following are exempt from VAT:
- Financial services (banking, insurance, securities dealing) [T1]
- Residential rental (long-term) [T1]
- Educational services (accredited institutions) [T1]
- Medical and dental services [T1]
- Domestic passenger transportation [T1]
- Sale of residential property (first sale may be exempt, conditions) [T2]
- Certain government services [T1]
- Charitable activities [T2]

**Legislation:** VAT Act 2014, Schedule 1 (Exempt Supplies).

---

## Step 2: VAT Registration [T1]

### Mandatory Registration

| Criterion | Threshold |
|-----------|-----------|
| Annual taxable turnover | BSD 100,000 or more |
| Importers | Subject to VAT at customs regardless |

### Voluntary Registration [T1]

Businesses below BSD 100,000 but above BSD 50,000 may register voluntarily.

### Registration Process [T1]

1. Apply through DIR online portal
2. Submit business licence, financial records, proof of turnover
3. DIR issues VAT registration certificate and TIN
4. Registration effective from the date specified by DIR

### Filing Frequency Based on Turnover [T1]

| Annual Turnover | Filing Frequency |
|----------------|------------------|
| Above BSD 5,000,000 | Monthly |
| BSD 400,000 - BSD 5,000,000 | Bi-monthly |
| BSD 100,000 - BSD 400,000 | Quarterly |
| Below BSD 100,000 (voluntary) | Annually |

---

## Step 3: Transaction Classification Rules [T1]

### 3a. Determine Transaction Type [T1]
- Sale of goods/services (output VAT) or Purchase (input VAT)
- Salaries, government levies, loan repayments, dividends = OUT OF SCOPE

### 3b. Determine Place of Supply [T1]
- Goods: where goods are delivered in The Bahamas
- Services: where the recipient is located (general rule)
- Imports: at Bahamian customs
- Exports: zero-rated if goods leave The Bahamas

### 3c. Determine VAT Rate [T1]
- 10% standard rate for most taxable supplies
- 5% reduced rate on food in food stores, diapers, feminine hygiene, medications (from April/September 2025)
- 0% for exports and zero-rated items
- Exempt: no VAT

### 3d. Calculate VAT [T1]
- `VAT = Net Amount * 10%`
- `Gross = Net + VAT`
- `Net = Gross / 1.10`

---

## Step 4: VAT Return Structure [T1]

### Return Form

The VAT return filed with DIR contains:

| Line | Description |
|------|-------------|
| 1 | Total value of standard-rated supplies (10%) |
| 2 | Output VAT on standard-rated supplies |
| 3 | Total value of zero-rated supplies |
| 4 | Total value of exempt supplies |
| 5 | Total supplies (1 + 3 + 4) |
| 6 | Total value of taxable purchases (domestic) |
| 7 | Input VAT on domestic purchases |
| 8 | Total value of imports |
| 9 | VAT paid on imports (at customs) |
| 10 | Total input VAT (7 + 9) |
| 11 | Net VAT (2 - 10) -- positive = payable, negative = refundable |

### Output VAT Reporting [T1]

- Report all standard-rated sales at 10%
- Zero-rated: report value, no VAT
- Exempt: report value, no VAT

### Input VAT Recovery [T1]

- Input VAT on purchases related to taxable supplies: **fully recoverable** [T1]
- Input VAT on purchases related to exempt supplies: **NOT recoverable** [T1]
- Input VAT on mixed-use: **apportioned** [T2]
- VAT paid at customs on imports: **recoverable** if for taxable supplies [T1]

### Input Tax Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Recovery % = (Taxable Supplies / Total Supplies) * 100
```
**Flag for practitioner: method must be approved by DIR. Annual adjustment required.**

---

## Step 5: Reverse Charge Mechanism [T1]

### When Reverse Charge Applies

- Services received from a non-resident supplier not registered with DIR [T1]
- The Bahamian recipient must self-assess VAT at 10% [T1]

### Procedure [T1]

1. Identify service from non-resident supplier
2. Self-assess output VAT at 10% on the service value
3. Claim input VAT at 10% if service relates to taxable supplies
4. Report both on the VAT return

### Exceptions [T1]

- Physical goods imported: VAT collected by Customs, not reverse charge [T1]
- Services consumed entirely outside The Bahamas: not subject to Bahamian VAT [T1]

---

## Step 6: Imports and Customs VAT [T1]

### VAT on Imports

- All goods imported into The Bahamas are subject to VAT at 10% [T1]
- VAT base: CIF value plus customs duties plus excise [T1]
- VAT collected by Bahamas Customs at point of entry [T1]
- VAT paid at customs is recoverable as input VAT [T1]

### Documentation [T1]

- Customs entry form
- Proof of VAT payment
- Import invoice
- Bill of lading

### Duty-Free / Freeport Areas [T2]

- Grand Bahama Port Authority (Freeport) has special provisions
- Goods within Freeport area may have customs and VAT concessions
- VAT applies when goods leave Freeport for domestic Bahamas consumption
- Flag for practitioner: Freeport/Grand Bahama rules require specialist analysis

---

## Step 7: Tourism Sector [T2]

### Hotels and Resorts

- Hotel room charges: VAT at 10% applies [T1]
- Food and beverage in hotels: VAT at 10% [T1]
- Tour operator services: generally taxable [T1]
- Cruise ship supplies: may be zero-rated if for international voyage [T2]

### No Income Tax Reminder [T1]

The Bahamas does NOT have income tax. VAT is the primary tax. Tourism businesses pay:
- VAT on supplies
- Business licence fees
- Real property tax
- Hotel occupancy tax (separate from VAT) [T2]

---

## Step 8: Filing Deadlines [T1]

### Filing Schedule

| Frequency | Deadline |
|-----------|----------|
| Monthly | 21st of the month following the return period |
| Bi-monthly | 21st of the month following the bi-monthly period |
| Quarterly | 21st of the month following the quarter end |
| Annual | 21st of March following the return year |

### Bi-Monthly Periods [T1]

| Period | Months | Filing Deadline |
|--------|--------|----------------|
| Period 1 | January - February | March 21 |
| Period 2 | March - April | May 21 |
| Period 3 | May - June | July 21 |
| Period 4 | July - August | September 21 |
| Period 5 | September - October | November 21 |
| Period 6 | November - December | January 21 |

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | BSD 1,000 or 5% of tax due (whichever is greater) |
| Late payment | 5% of unpaid amount plus 1% per month |
| Failure to register | Assessment plus penalties plus potential prosecution |
| Failure to issue VAT invoices | Fines per DIR schedule |
| Tax evasion | Criminal penalties (fines and/or imprisonment) |

---

## Step 9: Invoice Requirements [T1]

VAT invoices must contain:

1. Supplier name, address, and TIN [T1]
2. Customer name, address, and TIN (for B2B above BSD 500) [T1]
3. Invoice date and unique sequential number [T1]
4. Description of goods/services [T1]
5. Quantity and unit price [T1]
6. VAT rate (10%) [T1]
7. VAT amount separately stated [T1]
8. Total amount including VAT [T1]
9. The words "VAT Invoice" clearly displayed [T1]

**Simplified invoices** allowed for supplies under BSD 500: supplier name, TIN, date, description, gross amount with statement that VAT is included. [T1]

---

## Step 10: Deductibility Rules [T1]

### Non-Deductible Input VAT [T1]

Input VAT is NOT recoverable on:
- Entertainment and hospitality [T1]
- Motor vehicles for personal use [T1]
- Personal-use goods and services [T1]
- Purchases related to exempt supplies [T1]
- Club memberships [T1]

### Blocked Categories [T1]

- Passenger vehicles (unless taxi, rental, or delivery business) [T1]
- Entertainment (meals, events, gifts for clients) [T1]
- Personal expenses of owners/directors [T1]

---

## Step 11: Key Thresholds

| Threshold | Value |
|-----------|-------|
| VAT standard rate | 10% |
| VAT reduced rate (food/essentials) | 5% (from April 2025) |
| Mandatory registration | BSD 100,000 annual turnover |
| Voluntary registration | BSD 50,000 - BSD 100,000 |
| Monthly filing threshold | Above BSD 5,000,000 |
| Simplified invoice threshold | BSD 500 |
| Filing deadline | 21st of month following period |
| Late filing penalty | BSD 1,000 or 5% of tax due |

---

## PROHIBITIONS [T1]

- NEVER apply the old rates (7.5% or 12%) to current period transactions
- NEVER apply 10% to food in food stores after 1 April 2025 (reduced to 5%; and moving to 0% from April 2026)
- NEVER allow input VAT recovery on exempt supplies
- NEVER ignore the reverse charge on services from non-resident suppliers
- NEVER treat imports as zero-rated (VAT is paid at customs)
- NEVER allow input VAT recovery on blocked categories
- NEVER assume Freeport/Grand Bahama VAT treatment without specialist review
- NEVER issue invoices without "VAT Invoice" designation
- NEVER assume income tax exists in The Bahamas -- it does not
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not AI

---

## Step 12: Edge Case Registry

### EC1 -- Rate transition periods [T1]
**Situation:** Invoice dated before January 1, 2022 but payment received after.
**Resolution:** VAT rate is determined by the tax point (time of supply), not date of payment. Supplies made before January 1, 2022 are at 12%. Supplies made on or after are at 10%. Time of supply is the earlier of: invoice date, payment date, or delivery date.
**Legislation:** VAT Act 2014, Section 14 (time of supply).

### EC2 -- Financial services exemption [T1]
**Situation:** Bank charges fees for account management.
**Resolution:** Financial services are exempt. No VAT on bank fees. The bank cannot recover input VAT on related purchases.

### EC3 -- Foreign SaaS subscription [T1]
**Situation:** Bahamian company subscribes to US software, no VAT on invoice.
**Resolution:** Reverse charge applies. Self-assess output VAT at 10%. Claim input VAT at 10% if for taxable supplies. Net effect zero for fully taxable business.

### EC4 -- Export of goods [T1]
**Situation:** Bahamian company exports conch products to the US.
**Resolution:** Zero-rated. Report value in zero-rated section. No output VAT. Input VAT on related purchases is fully recoverable. Must retain export documentation (customs declaration, bill of lading).

### EC5 -- Grand Bahama Freeport [T2]
**Situation:** Business operates within the Grand Bahama Port Authority area.
**Resolution:** Freeport has special customs and tax provisions under the Hawksbill Creek Agreement. VAT treatment may differ from the rest of The Bahamas. Flag for practitioner: Freeport operations require specialist analysis of the interaction between the VAT Act and the Hawksbill Creek Agreement.

### EC6 -- Credit notes [T1]
**Situation:** Supplier issues credit note for returned goods.
**Resolution:** Credit note reduces output VAT in the period issued. Must reference original invoice. Adjust VAT return accordingly.

### EC7 -- Food sold in food stores [T1]
**Situation:** Supermarket sells rice, flour, sugar, fresh produce, frozen foods, and other grocery items.
**Resolution:** From 1 April 2025, food sold in food stores is subject to VAT at 5% (reduced from 10%). This includes all unprepared food items -- fresh fruits, vegetables, baby food, lunch snacks, frozen foods. Does NOT apply to prepared food (deli counter, ready-to-eat meals). From 1 April 2026, unprepared food is being moved to 0% (zero-rated). Verify current rate at time of filing. [T2]

---

## Step 13: No Income Tax Confirmation [T1]

The Bahamas does NOT have:
- Personal income tax [T1]
- Corporate income tax [T1]
- Capital gains tax [T1]
- Withholding tax [T1]

Revenue is raised through:
- VAT (10%) [T1]
- Customs duties [T1]
- Business licence fees [T1]
- Real property tax [T1]
- Stamp duty on certain transactions [T1]
- Other government fees and charges [T1]

---

## Step 14: Test Suite

### Test 1 -- Standard domestic sale
**Input:** Bahamian retailer sells goods for BSD 1,000 net.
**Expected output:** Output VAT = BSD 100 (10%). Total = BSD 1,100.

### Test 2 -- Export, zero-rated
**Input:** Bahamian company exports goods to the US, value BSD 5,000.
**Expected output:** VAT at 0%. Report in zero-rated section. Input VAT recoverable.

### Test 3 -- Reverse charge on foreign service
**Input:** Bahamian company receives consulting from UK firm, USD 3,000, no VAT.
**Expected output:** Self-assess output VAT BSD 300 (10%). Claim input VAT BSD 300 if fully taxable. Net effect zero.

### Test 4 -- Exempt supply (banking)
**Input:** Bahamian bank earns BSD 500,000 in fees. Purchases office supplies BSD 10,000 + VAT BSD 1,000.
**Expected output:** No output VAT (exempt). Input VAT BSD 1,000 NOT recoverable.

### Test 5 -- Import of goods
**Input:** Bahamian business imports electronics from China. CIF value BSD 20,000. Customs duty 35% = BSD 7,000.
**Expected output:** VAT base = BSD 27,000. VAT at 10% = BSD 2,700. Paid at customs. Recoverable as input VAT.

### Test 6 -- Food in food store (reduced rate)
**Input:** Supermarket sells rice for BSD 500 net (after April 2025).
**Expected output:** VAT at 5% = BSD 25. Total BSD 525. Output VAT = BSD 25. Input VAT on rice procurement is recoverable. (Note: if after April 2026, rice may be zero-rated at 0% -- verify current rate.)

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Bahamian tax practitioner must confirm.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax practitioner. Document gap.
```

---

## Contribution Notes

This skill covers The Bahamas' VAT system under the VAT Act 2014. Key features:
1. Standard rate of 10% (since January 2022), with a 5% reduced rate on food in food stores and certain essentials (since April/September 2025)
2. No income tax of any kind -- VAT is the primary tax
3. Food in food stores taxed at 5% (reduced from 10% in April 2025); unprepared food moving to 0% from April 2026
4. Financial services are exempt
5. Grand Bahama Freeport has special provisions requiring specialist analysis
6. The Bahamas uses the Bahamian dollar (BSD), pegged 1:1 to the US dollar

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
