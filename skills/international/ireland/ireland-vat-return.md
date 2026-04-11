---
name: ireland-vat-return
description: Use this skill whenever asked to prepare, review, or create an Ireland VAT return (VAT3 form), VAT Return of Trading Details (RTD), or any request involving Irish VAT filing. Trigger on phrases like "prepare Irish VAT return", "do the Irish VAT", "fill in VAT3", "create the return", "Irish VAT", "Revenue Online Service", "ROS return", or any request involving Ireland VAT filing. Also trigger when classifying transactions for Irish VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Ireland VAT classification rules, VAT3 box mappings, deductibility rules, reverse charge treatment, capital goods scheme, two-thirds rule, property VAT, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Ireland VAT-related work.
---

# Ireland VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Jurisdiction Code | IE |
| Primary Legislation | Value-Added Tax Consolidation Act 2010 (VATCA 2010), as amended |
| Supporting Legislation | Schedule 1 (exempt activities); Schedule 2 (zero-rated goods/services); Section 59 (blocked deductions); Section 60 (apportionment); Section 64 (Capital Goods Scheme); Section 41 (two-thirds rule); Section 56 (reverse charge) |
| Tax Authority | Revenue Commissioners (Revenue), Ireland |
| Filing Portal | https://www.ros.ie (Revenue Online Service -- ROS) |
| Contributor | PENDING -- requires warranted Irish CPA/CTA |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: VAT3 box assignment, reverse charge, blocked deductions, derived calculations, filing deadlines. Tier 2: partial exemption apportionment, two-thirds rule application, property VAT, cash basis eligibility. Tier 3: complex property transactions, Capital Goods Scheme adjustments, group VAT, cross-border digital services (OSS/IOSS). |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A chartered accountant or chartered tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to chartered accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and VAT number** [T1] -- IE + 7 digits + 1-2 letters (e.g., IE1234567T or IE1234567WI)
2. **VAT accounting basis** [T1] -- Invoice basis (default) or Moneys Received basis (cash basis)
3. **VAT period** [T1] -- bi-monthly (standard), quarterly (by Revenue agreement), annual (small traders), or monthly (by election)
4. **Industry/sector** [T2] -- impacts two-thirds rule applicability, construction reverse charge (RCT), and sector-specific rates
5. **Does the business make exempt supplies?** [T2] -- If yes, partial exemption apportionment required (Section 60 VATCA 2010); reviewer must confirm method
6. **Does the business trade goods for resale?** [T1] -- impacts RTD classification
7. **Is the business a principal contractor under RCT?** [T1] -- impacts construction reverse charge obligations
8. **Does the business deal in property?** [T3] -- triggers Capital Goods Scheme (Section 64), complex rules requiring specialist review
9. **Turnover level** [T1] -- determines cash basis eligibility (under EUR 2 million) and registration obligation
10. **Prior period credit/debit** [T1] -- any VAT balance carried forward

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until VAT registration details and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, PRSI, USC, loan repayments, dividends, bank charges, corporation tax, income tax = OUT OF SCOPE (never on VAT return)
- **Legislation:** VATCA 2010, Section 2 (interpretation), Section 3 (supply of goods), Section 5 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Ireland (domestic): supplier/customer country is IE
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- Non-EU: everything else (US, UK, AU, CH, etc.)
- **Note:** UK is Non-EU post-Brexit. Northern Ireland follows special protocol for goods (XI VAT numbers) but is Non-EU for services. Gibraltar is Non-EU. Channel Islands are Non-EU.
- **Legislation:** VATCA 2010, Section 30 (place of supply of goods), Section 33 (place of supply of services)

### 1c. Determine VAT Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 23% | Standard rate -- most goods and services | VATCA 2010, Section 46(1)(a) |
| 13.5% | Reduced rate -- construction services, building materials (where two-thirds rule applies), fuel (coal, heating oil, gas for non-domestic), repair/maintenance services, cleaning services, waste collection, restaurant/catering (until 30 June 2026), hairdressing (until 30 June 2026), short-term car hire, photographic supplies | VATCA 2010, Schedule 3 |
| 9% | Second reduced rate -- newspapers, e-newspapers, printed periodicals, e-periodicals, sports facilities, cinemas, theatres, amusement services, hairdressing (from 1 July 2026), restaurant/catering (from 1 July 2026), electricity and gas (extended to 31 Dec 2030), hotel and holiday accommodation, heat pump installation, qualifying apartments (8 Oct 2025 to 31 Dec 2030) | VATCA 2010, Schedule 3 as amended by Finance Act 2024/2025 |
| 4.8% | Livestock rate -- livestock (excluding chickens), greyhounds, hire of horses | VATCA 2010, Schedule 3 |
| 4.5% | Flat-rate compensation percentage for unregistered farmers (not a VAT rate -- compensation for input VAT not reclaimed). Decreased from 5.1% to 4.5% effective 1 January 2026. | VATCA 2010, Section 86; Finance Act 2025 |
| 0% | Zero rate -- exports, intra-EU B2B supplies of goods, most food and drink for human consumption, oral medicines (human and animal), children's clothing and footwear, books (printed), seeds/plants/trees, fertilisers, animal feed, disability aids (wheelchairs, crutches, hearing aids), sanitary products | VATCA 2010, Schedule 2 |
| Exempt | No VAT, no input credit -- financial services, insurance, medical/dental services, education, passenger transport, letting of immovable property (residential), funeral services, certain cultural/sporting activities by non-profit bodies | VATCA 2010, Schedule 1 |

### 1d. Determine Expense Category [T1]
- Capital goods (property): developed property -- triggers CGS (20-year adjustment for new build, 10-year for refurbishment)
- Resale: goods bought specifically to resell (stock-in-trade)
- Overhead/services: everything else (office supplies, professional services, utilities, etc.)
- **Note:** Ireland does NOT have a general capital goods threshold for non-property assets like Malta's EUR 1,160. The Capital Goods Scheme applies ONLY to developed property (Section 64 VATCA 2010).
- **Legislation:** VATCA 2010, Section 64 (Capital Goods Scheme)

---

## Step 2: VAT3 Box Assignment [T1]

**Legislation:** VATCA 2010, Section 76 (returns); Revenue guidance on completing VAT3 return.

The Irish VAT3 is structured differently from Malta's. It has far fewer boxes -- the key boxes are T1-T4, E1-E2, ES1-ES2, and PA1.

### VAT3 Box Structure

| Box | Description | What Goes Here |
|-----|-------------|----------------|
| **T1** | VAT charged on sales + VAT self-accounted | All output VAT: VAT on domestic sales at all rates + reverse charge output VAT (EU acquisitions, imported services, construction reverse charge) |
| **T2** | VAT on purchases (reclaimable input VAT) | All deductible input VAT: VAT on domestic purchases + reverse charge input VAT (where deductible) + postponed accounting VAT (where deductible) |
| **T3** | Amount payable | If T1 > T2, then T3 = T1 - T2 (pay this to Revenue) |
| **T4** | Amount repayable | If T2 > T1, then T4 = T2 - T1 (claim this from Revenue) |
| **E1** | Goods supplied to other EU countries | Net value of goods dispatched to VAT-registered customers in other EU Member States (zero-rated intra-EU supplies) |
| **E2** | Goods received from other EU countries | Net value of goods acquired from suppliers in other EU Member States (intra-Community acquisitions) |
| **ES1** | Services supplied to other EU countries | Net value of B2B services supplied to customers in other EU Member States (reverse charge applies in customer's state) |
| **ES2** | Services received from other EU countries | Net value of B2B services received from suppliers in other EU Member States (reverse charge -- self-account in Ireland) |
| **PA1** | Postponed Accounting imports | Customs value + duty of goods imported under the Postponed Accounting scheme |

### Domestic Sales -- Output VAT (goes into T1)

| Rate | Treatment |
|------|-----------|
| 23% | Calculate VAT at 23% on net amount. Include VAT in T1. |
| 13.5% | Calculate VAT at 13.5% on net amount. Include VAT in T1. |
| 9% | Calculate VAT at 9% on net amount. Include VAT in T1. |
| 4.8% | Calculate VAT at 4.8% on net amount. Include VAT in T1. |
| 0% (zero-rated) | No VAT. Nothing in T1. If EU B2B goods, report net in E1. If EU B2B services, report net in ES1. |
| Exempt | No VAT. Nothing in T1. No input credit on related costs. |

### Domestic Purchases -- Input VAT (goes into T2)

| Category | Deductible? | Treatment |
|----------|-------------|-----------|
| Business overhead (not blocked) | Yes | Include VAT paid in T2 |
| Stock for resale | Yes | Include VAT paid in T2 |
| Blocked category (Section 59) | No | Do NOT include in T2 |
| Related to exempt supplies only | No | Do NOT include in T2 |
| Mixed (taxable + exempt) | Partial | Apportion per Section 60 [T2] |

### EU Acquisitions of Goods (Intra-Community Acquisitions)

| Step | Box | Amount |
|------|-----|--------|
| Report net value of goods | E2 | Net amount |
| Self-account output VAT at applicable Irish rate | T1 | VAT amount |
| Claim input VAT (if deductible) | T2 | VAT amount |
| Net effect for fully taxable business | -- | Zero |

### EU Services Received (Reverse Charge -- B2B)

| Step | Box | Amount |
|------|-----|--------|
| Report net value of services | ES2 | Net amount |
| Self-account output VAT at 23% (standard rate) | T1 | VAT amount |
| Claim input VAT (if deductible) | T2 | VAT amount |
| Net effect for fully taxable business | -- | Zero |

### EU Services Supplied (B2B)

| Step | Box | Amount |
|------|-----|--------|
| Report net value of services | ES1 | Net amount |
| No Irish VAT (customer self-accounts) | -- | -- |
| Include on VIES return | -- | -- |

### Non-EU Services Received (Reverse Charge)

| Step | Box | Amount |
|------|-----|--------|
| Self-account output VAT at 23% | T1 | VAT amount |
| Claim input VAT (if deductible) | T2 | VAT amount |
| Net effect for fully taxable business | -- | Zero |
| **Note:** No ES2 entry -- ES2 is EU only | -- | -- |

### Non-EU Services Supplied

| Step | Box | Amount |
|------|-----|--------|
| Outside scope of Irish VAT | -- | No entry on VAT3 |
| No output VAT | -- | -- |

### Imports of Physical Goods from Non-EU

| Method | Treatment |
|--------|-----------|
| **Postponed Accounting (PA)** | Report customs value + duty in PA1. Self-account VAT in T1. Claim in T2 (if deductible). Net effect = zero for fully taxable business. |
| **VAT paid at Customs** | VAT paid to Customs on import. Claim as input VAT in T2 (based on Customs C2/SAD document). |

### Construction Services -- RCT Reverse Charge [T1]

| Scenario | Treatment |
|----------|-----------|
| Subcontractor invoices principal (no VAT charged) | Principal self-accounts: output VAT at 13.5% in T1, input VAT in T2 (if deductible) |
| Principal is the accountable person for VAT | Subcontractor does NOT charge VAT on invoice |
| **Legislation:** VATCA 2010, Section 56(2) | Applies where RCT operates |

---

## Step 3: Reverse Charge Mechanics [T1]

**Legislation:** VATCA 2010, Section 56 (general reverse charge); Section 16 (intra-Community acquisitions); Section 33-37 (place of supply of services).

For EU and non-EU purchases where the Irish business must self-account:
1. Calculate Irish VAT at the applicable rate (usually 23% for services, applicable goods rate for ICA)
2. Include the calculated VAT in T1 (output VAT -- self-accounted)
3. Include the same amount in T2 (input VAT -- if deductible)
4. Net effect: zero for fully taxable businesses

**The VAT3 must show BOTH sides (T1 and T2) for reverse charge transactions.**

### When Reverse Charge Applies [T1]

| Scenario | Reverse Charge? |
|----------|----------------|
| B2B services from EU supplier | Yes -- ES2 + T1 + T2 |
| B2B services from non-EU supplier | Yes -- T1 + T2 (no ES2) |
| Goods from EU supplier (ICA) | Yes -- E2 + T1 + T2 |
| Goods imported from non-EU (Postponed Accounting) | Yes -- PA1 + T1 + T2 |
| Goods imported from non-EU (VAT paid at Customs) | No reverse charge -- claim via T2 from Customs doc |
| Construction services under RCT | Yes -- T1 + T2 |
| B2C services from EU supplier | No -- supplier charges local VAT |

### Exceptions to Reverse Charge [T1]

- Out-of-scope categories (wages, bank charges, dividends, etc.): NEVER reverse charge
- Local consumption abroad (hotel, restaurant, taxi in another country): NOT reverse charge. Foreign VAT paid at source. Irish business cannot recover foreign VAT via Irish return (must use EU VAT Refund Directive if applicable).
- EU supplier charged their local VAT > 0%: NOT reverse charge on Irish return. Foreign VAT is part of the expense cost.
- B2C digital services: may fall under OSS rules [T3]

---

## Step 4: Deductibility Check

### Blocked Categories (Section 59, VATCA 2010) [T1]

**Legislation:** VATCA 2010, Section 59(2).

These have ZERO VAT recovery regardless of business purpose:

| Category | Detail | Legislation Reference |
|----------|--------|-----------------------|
| **Food and drink** | All food and drink for consumption by the business, staff, or clients. Exception: stock-in-trade for resale (e.g., restaurant buying ingredients). | Section 59(2)(a) |
| **Accommodation** | Hotel, B&B, serviced apartment. Exception: qualifying conference attendance (accommodation element only, NOT food/drink). | Section 59(2)(b) |
| **Entertainment** | Client entertainment, staff entertainment, corporate hospitality. No exceptions. | Section 59(2)(c) |
| **Motor vehicles** | Purchase or hire of motor vehicles. Exceptions: stock-in-trade (motor dealer), hire purchase for onward supply (finance house), car hire business, driving instruction. | Section 59(2)(d) |
| **Petrol** | All petrol, regardless of business use. No exceptions. Even if the vehicle itself qualifies for input VAT recovery, petrol does not. | Section 59(2)(e) |

**Critical distinction:** Diesel is NOT blocked. Auto-diesel for business vehicles (where the vehicle qualifies) IS deductible. Petrol is ALWAYS blocked.

Blocked categories OVERRIDE partial exemption. Check blocked FIRST.

### Diesel and Other Fuel [T1]

| Fuel Type | Deductible? | Condition |
|-----------|-------------|-----------|
| Petrol | Never | Blocked under Section 59 |
| Auto-diesel | Yes | If vehicle qualifies (commercial vehicle, taxi, etc.) |
| Marked diesel (green diesel) | Yes | Agricultural/industrial use |
| Heating oil | Yes | Business premises heating |
| Electricity | Yes | Business use |
| Gas | Yes | Business use |

### Registration-Based Recovery [T1]
- VAT-registered (standard): full recovery (subject to category blocks and apportionment)
- Unregistered: NO recovery
- Flat-rate farmer (Section 86): no recovery, but applies flat-rate addition (4.5% from 1 January 2026; was 5.1%) on sales

### Partial Exemption (Section 60, VATCA 2010) [T2]

**Legislation:** VATCA 2010, Section 60.

If business makes both taxable and exempt supplies:
- Direct attribution first: costs directly attributable to taxable supplies = fully deductible; costs directly attributable to exempt supplies = not deductible
- Residual (overhead) costs: apportion using a fair and reasonable method
- Common method: `Recovery % = (Taxable Turnover / Total Turnover) * 100`
- Revenue may agree alternative methods (floor area, headcount, transaction count)

**Flag for reviewer: apportionment method and rate must be confirmed by chartered accountant before applying. Annual review and adjustment may be required.**

---

## Step 5: Derived Box Calculations [T1]

The Irish VAT3 calculations are simpler than Malta's multi-box approach:

```
IF T1 > T2 THEN
  T3 = T1 - T2    -- Amount payable to Revenue
  T4 = 0
ELSE
  T3 = 0
  T4 = T2 - T1    -- Amount repayable from Revenue
END

-- E1, E2, ES1, ES2, PA1 are informational/statistical
-- They do NOT directly feed into T1-T4 calculations
-- BUT the VAT on E2/ES2/PA1 transactions DOES feed into T1 and T2
```

---

## Step 6: Two-Thirds Rule (Section 41) [T2]

**Legislation:** VATCA 2010, Section 41.

When a supply involves both goods and services:

| Condition | Treatment |
|-----------|-----------|
| VAT-exclusive cost of goods to the supplier > two-thirds of VAT-exclusive total charge | Entire supply taxed at the GOODS rate |
| VAT-exclusive cost of goods to the supplier <= two-thirds of VAT-exclusive total charge | Entire supply taxed at the SERVICES rate |

### Common Application
- **Construction:** If materials cost > two-thirds of total contract value, charge goods rate (13.5% or 23%) on entire supply. If materials <= two-thirds, charge services rate (13.5%) on entire supply.
- **Repairs:** Parts + labour. If parts cost > two-thirds, goods rate applies to whole job.

### Exceptions [T1]
The two-thirds rule does NOT apply to:
- Repair and maintenance of motor vehicles
- Repair and maintenance of agricultural machinery
- Supplies where the reverse charge applies (construction RCT)

**Flag for reviewer: determining the cost of goods to the supplier requires judgement. Confirm with client before applying.**

---

## Step 7: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT registration -- goods | EUR 85,000 per annum | VATCA 2010, Schedule 4 (as amended by Finance Act 2024) |
| VAT registration -- services | EUR 42,500 per annum | VATCA 2010, Schedule 4 (as amended by Finance Act 2024) |
| Cash basis (Moneys Received) eligibility | EUR 2,000,000 turnover (or 90%+ supplies to non-VAT registered) | VATCA 2010, Section 14 |
| Intrastat -- Arrivals | EUR 500,000 per calendar year | Revenue Intrastat Traders Manual |
| Intrastat -- Dispatches | EUR 635,000 per calendar year | Revenue Intrastat Traders Manual |
| Intrastat -- Extended arrivals | EUR 5,000,000 per annum (more detailed declaration) | Revenue Intrastat Traders Manual |
| Intrastat -- Extended dispatches | EUR 35,000,000 per annum (more detailed declaration) | Revenue Intrastat Traders Manual |
| Distance sales to Ireland (OSS) | EUR 10,000 aggregate EU threshold | EU VAT e-Commerce Directive |
| Capital Goods Scheme -- new build | 20 adjustment intervals (years) | VATCA 2010, Section 64 |
| Capital Goods Scheme -- refurbishment | 10 adjustment intervals (years) | VATCA 2010, Section 64 |

---

## Step 8: Filing Deadlines

### VAT3 Return [T1]

| Period Type | Period Dates | Filing Deadline (ROS) | Filing Deadline (Paper) |
|-------------|-------------|----------------------|------------------------|
| Bi-monthly (standard) | Jan-Feb | 23 March | 19 March |
| Bi-monthly | Mar-Apr | 23 May | 19 May |
| Bi-monthly | May-Jun | 23 July | 19 July |
| Bi-monthly | Jul-Aug | 23 September | 19 September |
| Bi-monthly | Sep-Oct | 23 November | 19 November |
| Bi-monthly | Nov-Dec | 23 January (following year) | 19 January (following year) |

**ROS filers get 4 extra days.** All VAT-registered businesses must file via ROS.

### Other Returns [T1]

| Return | Frequency | Deadline |
|--------|-----------|----------|
| VAT RTD (Return of Trading Details) | Annual | 23rd of month following accounting year-end (ROS) |
| VIES | Bi-monthly (aligned with VAT3) or monthly (by election) | 23rd of month following period end (ROS) |
| Intrastat | Monthly (if above threshold) | 23rd of month following reference month |

### Penalties for Late Filing [T1]

| Penalty Type | Amount | Legislation |
|-------------|--------|-------------|
| Fixed penalty -- failure to file | EUR 4,000 per return | VATCA 2010, Section 115 |
| Late filing surcharge (within 2 months) | 5% of tax due (max EUR 12,695) | TCA 1997, Section 1084 |
| Late filing surcharge (over 2 months) | 10% of tax due (max EUR 63,485) | TCA 1997, Section 1084 |
| Interest on late payment | 0.0274% per day (~10% per annum) | TCA 1997, Section 1080 |

---

## Step 9: VAT Return of Trading Details (RTD) [T1]

**Legislation:** VATCA 2010, Section 76(2).

The RTD is an annual informational return -- separate from the VAT3. It does NOT create a VAT liability or refund. Revenue uses it for compliance checks and cross-referencing against bi-monthly returns.

### RTD Structure

The RTD breaks down all trading activity across four columns, by VAT rate:

| Column | Description |
|--------|-------------|
| Column 1 | Supplies: value of all goods and services supplied, broken down by rate (23%, 13.5%, 9%, 4.8%, 0%, exempt) |
| Column 2 | Intra-EU Acquisitions + Imports: value of goods/services acquired from EU and imports where VAT was not charged at source, by rate |
| Column 3 | Stock Inputs: value of goods purchased for resale, by rate |
| Column 4 | Non-Stock Inputs: value of goods/services purchased NOT for resale (overheads, capital), by rate |

### RTD Filing [T1]
- Based on the business's accounting year (not calendar year)
- Due: 23rd of the month following the accounting year-end (ROS)
- Failure to file: Revenue will withhold ALL tax refunds across all tax heads until RTD is submitted

---

## Step 10: Cash Basis (Moneys Received) [T1]

**Legislation:** VATCA 2010, Section 14.

| Aspect | Invoice Basis (Default) | Cash Basis (Moneys Received) |
|--------|------------------------|------------------------------|
| When output VAT is due | When invoice is issued | When payment is received |
| When input VAT is claimable | When invoice is received | When invoice is received (NOT when paid) |
| Eligibility | All businesses | Turnover < EUR 2,000,000 OR 90%+ supplies to non-VAT-registered persons |
| How to elect | N/A (default) | Apply at registration or notify Revenue |
| Cancellation trigger | N/A | Exceed EUR 2M or < 90% to unregistered -- notify Revenue by end of following month |

**Important:** On cash basis, input VAT is STILL claimed on the invoice basis (when received), NOT when the supplier is paid. Only output VAT timing changes.

---

## Step 11: Property VAT [T3]

**This is one of the most complex areas of Irish VAT. ALWAYS escalate to a specialist.**

**Legislation:** VATCA 2010, Part 11 (Sections 93-98); Section 64 (CGS).

### Summary of Key Principles (Reference Only -- Do Not Execute)

| Scenario | VAT Treatment |
|----------|---------------|
| Sale of new completed property by developer | Taxable at 13.5% (or 9% for qualifying apartments 2025-2030) |
| Sale of "old" property (no development in 5 years, or occupied 2+ years) | Exempt (unless option to tax exercised for commercial) |
| Residential letting | Always exempt |
| Commercial letting | Exempt, but landlord may opt to tax (creates CGS obligation) |
| Sale of residential property by developer | Always taxable (two-year/five-year rules do not apply to developers) |
| Refurbishment | May create new CGS obligation (10-year adjustment) |

### Capital Goods Scheme [T3]

- New property: 20 annual adjustment intervals
- Refurbishment (exceeding EUR 25,000 ex-VAT): 10 annual adjustment intervals
- Each year, compare actual use (taxable vs exempt) against initial deduction
- If use changes, adjustment required (additional deduction or clawback)
- Disposal triggers full remaining adjustment in year of sale

**NEVER attempt CGS calculations without specialist review.**

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT rates or box assignments -- classification is deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges, etc.)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi consumed in another country)
- NEVER allow input VAT recovery on petrol -- it is ALWAYS blocked under Section 59
- NEVER allow input VAT recovery on food, drink, accommodation, or entertainment (except the narrow conference accommodation exception and stock-in-trade for resale)
- NEVER confuse zero-rated (0% with input credit) with exempt (no VAT, no input credit)
- NEVER apply reverse charge when EU supplier charged their local VAT > 0%
- NEVER attempt Capital Goods Scheme calculations without specialist review
- NEVER apply the two-thirds rule to motor vehicle repairs or agricultural machinery repairs
- NEVER apply the two-thirds rule where the construction reverse charge (RCT) applies
- NEVER confuse diesel (deductible for qualifying vehicles) with petrol (always blocked)
- NEVER assume Northern Ireland is EU for services -- it follows Non-EU rules for services, EU rules for goods only
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file a return without the RTD being up to date -- Revenue will withhold all refunds

---

## Step 12: VIES Returns [T1]

**Legislation:** VATCA 2010, Section 80; Council Regulation (EU) 904/2010.

| Requirement | Detail |
|-------------|--------|
| Who must file | Any Irish VAT-registered business that zero-rates goods to, or supplies reverse-charge services to, a VAT-registered business in another EU Member State |
| Frequency | Bi-monthly (aligned with VAT3 periods), or monthly by election |
| Content | Customer's VAT number, total value of goods (corresponds to E1), total value of services (corresponds to ES1) |
| Deadline | 23rd of month following period end (ROS) |
| Verification | Must verify customer's VAT number on VIES system before zero-rating |

**If a customer's VAT number cannot be verified, do NOT zero-rate the supply. Charge Irish VAT.**

---

## Step 13: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- EU hotel / restaurant / taxi consumed abroad [T1]
**Situation:** Irish VAT-registered business pays for a hotel in France. Invoice shows French VAT.
**Resolution:** NOT reverse charge. French VAT was charged and paid at source. No entry on Irish VAT3 (T1/T2). The foreign VAT is an irrecoverable cost embedded in the expense. If the business wants to recover the French VAT, it must use the EU VAT Refund Directive (Electronic VAT Refund -- EVR) via ROS, which is a separate process.
**Legislation:** VATCA 2010, Section 33 (place of supply exceptions for immovable property services); Council Directive 2008/9/EC (VAT refund).

### EC2 -- SaaS subscription from US company (e.g., AWS, Google, Notion) [T1]
**Situation:** Monthly charge from a US company, no VAT shown on invoice. B2B supply of services.
**Resolution:** Reverse charge applies. Self-account output VAT at 23% in T1. Claim input VAT at 23% in T2 (if deductible). Net effect = zero for fully taxable business. No ES2 entry (ES2 is EU only).
**Legislation:** VATCA 2010, Section 33(b) (B2B services -- place of supply is where customer is established); Section 56 (reverse charge).

### EC3 -- SaaS subscription from EU company (e.g., SAP Germany) [T1]
**Situation:** Monthly charge from a German company, no VAT shown, customer's Irish VAT number on invoice.
**Resolution:** Reverse charge applies. Report net value in ES2. Self-account output VAT at 23% in T1. Claim input VAT at 23% in T2 (if deductible). Net effect = zero for fully taxable business.
**Legislation:** VATCA 2010, Section 33(b); Section 56.

### EC4 -- Intra-Community acquisition of goods [T1]
**Situation:** Irish business buys physical goods from Italian supplier. Invoice shows 0% VAT with Irish customer's VAT number.
**Resolution:** Report net value in E2. Self-account output VAT at applicable Irish rate in T1. Claim input VAT in T2 (if deductible). Report on VIES (this is handled by the Italian supplier on their side).
**Legislation:** VATCA 2010, Section 16 (intra-Community acquisitions).

### EC5 -- Motor vehicle purchase [T1]
**Situation:** Business purchases a car for staff use.
**Resolution:** Input VAT BLOCKED under Section 59(2)(d). No T2 entry for the VAT. Full cost including VAT is the expense. Exception only if: (a) motor dealer buying as stock-in-trade, (b) taxi/hackney operator, (c) car hire business, (d) driving school.
**Legislation:** VATCA 2010, Section 59(2)(d).

### EC6 -- Diesel for commercial van [T1]
**Situation:** Business purchases auto-diesel for a commercial delivery van.
**Resolution:** Input VAT IS deductible. Diesel is NOT petrol. The vehicle must itself qualify (commercial vehicle, not a blocked motor car). Include VAT in T2.
**Legislation:** VATCA 2010, Section 59 -- petrol is blocked, diesel is not.

### EC7 -- Petrol for any vehicle [T1]
**Situation:** Business purchases petrol for a qualifying business vehicle (e.g., taxi).
**Resolution:** Input VAT is BLOCKED. Petrol is always non-deductible under Section 59(2)(e), even if the vehicle itself qualifies for input VAT recovery.
**Legislation:** VATCA 2010, Section 59(2)(e).

### EC8 -- Conference attendance -- hotel accommodation [T2]
**Situation:** Employee attends a qualifying conference in Dublin. Hotel invoice shows accommodation and meals separately.
**Resolution:** VAT on the accommodation element MAY be deductible if: (a) it is a qualifying conference, (b) the accommodation is necessary for attendance, (c) the claim is for accommodation only. VAT on food and drink at the conference is NOT deductible (Section 59 block). Flag for reviewer to confirm qualifying conference status.
**Legislation:** VATCA 2010, Section 59(2)(b) -- exception for qualifying conferences; Revenue guidance.

### EC9 -- Credit notes [T1]
**Situation:** Business receives a credit note from a supplier.
**Resolution:** Reduce the original VAT entry. If original purchase included VAT in T2, reduce T2 by the VAT on the credit note. If the original sale included VAT in T1, reduce T1 by the VAT on the credit note. Net figures are reported.
**Legislation:** VATCA 2010, Section 57 (adjustments).

### EC10 -- Construction subcontractor under RCT [T1]
**Situation:** A principal contractor receives an invoice from a construction subcontractor. The invoice shows no VAT. RCT applies.
**Resolution:** Principal self-accounts for VAT. Output VAT at 13.5% goes in T1. Input VAT at 13.5% goes in T2 (if deductible). The subcontractor does NOT charge VAT. This is separate from the RCT withholding tax (0%/20%/35%) which is an income tax matter.
**Legislation:** VATCA 2010, Section 56(2); Taxes Consolidation Act 1997, Sections 530A-530T (RCT).

### EC11 -- Postponed Accounting for non-EU imports [T1]
**Situation:** Business imports goods from the US. Registered for Postponed Accounting.
**Resolution:** Report customs value + duty in PA1. Self-account VAT in T1 at applicable rate. Claim same VAT in T2 (if deductible). Net cash effect = zero. Without Postponed Accounting, VAT would be paid to Customs at import and recovered later via T2 (cash flow disadvantage).
**Legislation:** VATCA 2010, Section 56(6) as inserted by Finance Act 2020.

### EC12 -- Flat-rate farmer supplies [T1]
**Situation:** VAT-registered business buys agricultural produce from a flat-rate farmer.
**Resolution:** The flat-rate farmer charges a 4.5% flat-rate addition (not VAT; reduced from 5.1% effective 1 January 2026). The purchasing business CAN claim this 4.5% as input VAT in T2. The flat-rate farmer does not file VAT returns.
**Legislation:** VATCA 2010, Section 86.

### EC13 -- Northern Ireland post-Brexit [T1 for goods, T2 for services]
**Situation:** Irish business trades with a Northern Ireland business.
**Resolution for GOODS:** Northern Ireland has XI-prefix VAT numbers. Treat as intra-EU for goods. Use E1/E2 boxes. Zero-rate if B2B with valid XI VAT number.
**Resolution for SERVICES:** Treat Northern Ireland as non-EU (GB). Reverse charge applies. No ES1/ES2 entry (those are EU only). Self-account in T1/T2.
**Legislation:** Northern Ireland Protocol / Windsor Framework; Revenue eBrief guidance.

### EC14 -- Bad debt relief [T2]
**Situation:** Customer has not paid invoice for over 6 months.
**Resolution:** If on invoice basis, business has already accounted for output VAT. Can claim bad debt relief by reducing T1 in the period the debt becomes bad (6 months overdue, written off in accounts, and debtor has been notified). If later recovered, must re-account.
**Legislation:** VATCA 2010, Section 39.

---

## Step 14: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax or corporation tax. The following is reference information only. Do not execute any of these rules. Escalate to chartered accountant.

- **Corporation Tax:** Standard rate 12.5% on trading income; 25% on passive/non-trading income. Pillar Two minimum effective rate of 15% for qualifying groups.
- **Income Tax (self-employed):** Progressive bands 20%/40%. USC applies on gross income. PRSI Class S for self-employed.
- **RCT (Relevant Contracts Tax):** 0%, 20%, or 35% withholding on construction/meat/forestry payments. Separate from VAT. Filed via ROS.
- **Preliminary Tax:** Paid by 23rd of month 11 of accounting period (ROS). 90% of current year or 100% of prior year.

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Chartered accountant or chartered tax adviser must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to chartered accountant. Document gap.
```

---

## Step 16: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic purchase, 23% VAT, office supplies
**Input:** Irish supplier, office supplies, gross EUR 246, VAT EUR 46, net EUR 200. Fully taxable business.
**Expected output:** T2 includes EUR 46. Input VAT recoverable in full.

### Test 2 -- Non-EU SaaS subscription, reverse charge
**Input:** US supplier (AWS), monthly fee EUR 100, no VAT on invoice. Fully taxable business.
**Expected output:** T1 includes EUR 23 (23% self-accounted output VAT). T2 includes EUR 23 (input VAT, deductible). Net VAT effect = zero. No ES2 entry (non-EU).

### Test 3 -- EU SaaS subscription, reverse charge
**Input:** German supplier (SAP), monthly fee EUR 500, no VAT charged, Irish customer VAT number on invoice. Fully taxable business.
**Expected output:** ES2 = EUR 500. T1 includes EUR 115 (23% self-accounted). T2 includes EUR 115 (deductible). Net VAT effect = zero.

### Test 4 -- Intra-Community acquisition of goods
**Input:** Italian supplier ships physical goods to Ireland. Invoice EUR 2,000, no VAT, Irish customer VAT number referenced. Goods are standard-rated in Ireland.
**Expected output:** E2 = EUR 2,000. T1 includes EUR 460 (23% self-accounted). T2 includes EUR 460 (deductible). Net = zero.

### Test 5 -- EU B2B service sale, zero rated
**Input:** Irish business invoices French company EUR 1,000 for consulting. French customer has valid VAT number. Reverse charge applies in France.
**Expected output:** ES1 = EUR 1,000. No T1 entry. No T2 entry. Include on VIES return.

### Test 6 -- Motor vehicle purchase, blocked
**Input:** Business (not motor dealer/taxi) purchases a car for EUR 30,000 including EUR 5,610 VAT (23%).
**Expected output:** T2 = EUR 0 for this transaction. VAT is BLOCKED under Section 59(2)(d). Full EUR 30,000 is cost.

### Test 7 -- Petrol, always blocked
**Input:** Taxi operator purchases petrol EUR 100 including EUR 18.70 VAT (23%).
**Expected output:** T2 = EUR 0 for this transaction. Petrol VAT is BLOCKED even though the taxi itself qualifies for VAT recovery.

### Test 8 -- Diesel for commercial van, deductible
**Input:** Delivery company purchases auto-diesel EUR 150 including EUR 28.05 VAT (23%). Commercial van.
**Expected output:** T2 includes EUR 28.05. Diesel is NOT petrol. Vehicle qualifies. VAT is deductible.

### Test 9 -- EU hotel consumed abroad
**Input:** Employee stays at hotel in Spain. Invoice EUR 200 including EUR 20 Spanish VAT.
**Expected output:** No entry on Irish VAT3. Not reverse charge. Spanish VAT is irrecoverable on Irish return. May be recoverable via EU VAT Refund Directive (separate process).

### Test 10 -- Construction reverse charge (RCT)
**Input:** Principal contractor receives invoice from subcontractor for EUR 10,000, no VAT charged. RCT applies. Construction services at 13.5%.
**Expected output:** T1 includes EUR 1,350 (13.5% self-accounted). T2 includes EUR 1,350 (if deductible). Net = zero.

### Test 11 -- Domestic sale at 9% (restaurant, from July 2026)
**Input:** Restaurant sells meal for EUR 50 net. 9% VAT applies (post-1 July 2026).
**Expected output:** T1 includes EUR 4.50.

### Test 12 -- Postponed Accounting import
**Input:** Business imports goods from US. Customs value EUR 5,000, duty EUR 200. Standard rate goods. Registered for PA.
**Expected output:** PA1 = EUR 5,200. T1 includes EUR 1,196 (23% of EUR 5,200). T2 includes EUR 1,196 (if deductible). Net = zero.

### Test 13 -- Flat-rate farmer purchase
**Input:** Food manufacturer buys cattle from flat-rate farmer. Net EUR 10,000 + 5.5% flat-rate addition = EUR 550.
**Expected output:** T2 includes EUR 550 (flat-rate addition is claimable as input VAT).

### Test 14 -- Entertainment, blocked
**Input:** Business takes client to dinner. Restaurant bill EUR 200 including EUR 16.36 VAT (9%).
**Expected output:** T2 = EUR 0 for this transaction. Entertainment is BLOCKED under Section 59(2)(c). No exceptions.

---

## Step 17: Legal References Summary

| Reference | Description |
|-----------|-------------|
| VATCA 2010 | Value-Added Tax Consolidation Act 2010 (principal legislation) |
| Schedule 1 | Exempt activities |
| Schedule 2 | Zero-rated goods and services |
| Schedule 3 | Goods and services subject to reduced rates |
| Schedule 4 | Registration thresholds |
| Section 3 | Supply of goods |
| Section 5 | Supply of services |
| Section 14 | Moneys received (cash) basis |
| Section 16 | Intra-Community acquisitions |
| Section 30 | Place of supply of goods |
| Section 33 | Place of supply of services (general rule) |
| Section 39 | Bad debt relief |
| Section 41 | Two-thirds rule |
| Section 46 | Rates of tax |
| Section 56 | Reverse charge |
| Section 59 | Blocked deductions (food, drink, accommodation, entertainment, motor vehicles, petrol) |
| Section 60 | Apportionment (partial exemption) |
| Section 64 | Capital Goods Scheme |
| Section 76 | Returns (VAT3, RTD) |
| Section 80 | VIES |
| Section 86 | Flat-rate farmers |
| Section 93-98 | VAT on property |
| Section 115 | Penalties |
| TCA 1997, s.1080 | Interest on late payment |
| TCA 1997, s.1084 | Surcharges for late filing |
| TCA 1997, s.530A-530T | Relevant Contracts Tax (RCT) |
| Finance Act 2024/2025 | Rate changes (9% extensions, threshold increases) |

---

## Contribution Notes

This skill follows the format established by the Malta VAT Return Preparation Skill. Key differences from Malta:

1. **Fewer VAT3 boxes:** Ireland uses T1-T4, E1-E2, ES1-ES2, PA1 vs Malta's 45+ boxes.
2. **Different blocked categories:** Ireland blocks petrol specifically (not just motor vehicles). Diesel for qualifying vehicles IS deductible.
3. **No small enterprise annual declaration:** Ireland does not have an equivalent to Malta's Article 11 simplified form. Businesses below the threshold are simply unregistered.
4. **Two-thirds rule:** Unique to Ireland (Section 41). Malta does not have an equivalent.
5. **Construction reverse charge (RCT):** Ireland's construction reverse charge is linked to the RCT withholding tax system. Malta does not have an equivalent.
6. **Property VAT / CGS:** Ireland's Capital Goods Scheme for property is far more complex than Malta's capital goods threshold.
7. **Cash basis available:** Ireland allows Moneys Received basis for businesses under EUR 2M. Malta does not have an equivalent election.
8. **Postponed Accounting:** Ireland's PA1 box on VAT3 is specific to post-Brexit import arrangements. Malta handles imports differently.
9. **Filing frequency:** Ireland is bi-monthly (6 returns per year). Malta is quarterly (4 returns for Article 10).
10. **Flat-rate farmer scheme:** Ireland's 5.5% flat-rate addition is claimable as input VAT by the purchaser.

**A skill may not be published without sign-off from a warranted practitioner in the relevant jurisdiction. This skill is version 0.9 (draft) and MUST be validated by an Irish chartered accountant or chartered tax adviser before use in production.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
