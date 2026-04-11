---
name: taiwan-vat
description: Use this skill whenever asked to prepare, review, or advise on a Taiwan VAT return (Business Tax / 營業稅), e-invoice (電子發票) compliance, or any matter involving Taiwan's value-added and non-value-added business tax. Trigger on phrases like "Taiwan VAT", "Taiwan business tax", "營業稅", "Form 401", "Form 403", "e-invoice Taiwan", "GUI (Government Uniform Invoice)", "zero-rated export Taiwan", or any request involving Taiwan VAT filing. This skill contains the complete Taiwan VAT rate structure, filing rules, input credit mechanics, e-invoice requirements, and GBRT treatment for financial institutions. ALWAYS read this skill before touching any Taiwan VAT-related work.
---

# Taiwan VAT (Business Tax / 營業稅) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Taiwan (Republic of China / 中華民國) |
| Jurisdiction Code | TW |
| Primary Legislation | Value-Added and Non-Value-Added Business Tax Act (加值型及非加值型營業稅法), as amended |
| Supporting Legislation | Enforcement Rules of the Business Tax Act; Ministry of Finance (MoF) interpretive rulings; Statute for Industrial Innovation Art. 23-2 (tax incentives) |
| Tax Authority | National Taxation Bureau (國稅局), under the Ministry of Finance |
| Filing Portal | eTax Portal (財政部電子申報繳稅服務網) — https://tax.nat.gov.tw |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, input/output mechanics, filing deadlines, e-invoice rules. Tier 2: GBRT classification, mixed-supply apportionment, cross-border digital services. Tier 3: transfer pricing, tax treaty application, complex restructuring. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed CPA/tax agent must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Unified Business Number (統一編號 / UBN)** [T1] -- 8-digit number
2. **Business tax classification** [T1] -- VAT taxpayer (Section 4, Chapter 4) or GBRT taxpayer (Section 2, Chapter 4)
3. **Industry sector** [T2] -- determines if VAT (5%) or GBRT (1-5%) applies; financial institutions, small businesses, and special drinking/entertainment establishments use GBRT
4. **Filing period** [T1] -- bi-monthly (standard for VAT taxpayers) or monthly (for certain large enterprises)
5. **Filing form** [T1] -- Form 401 (VAT taxpayers) or Form 403 (GBRT taxpayers)
6. **Does the business export goods or services?** [T1] -- zero-rated treatment
7. **Does the business make exempt supplies?** [T2] -- impacts input VAT apportionment
8. **E-invoice (電子發票) compliance status** [T1] -- all business entities must use e-invoices via MoF platform
9. **Is the entity a foreign enterprise providing cross-border digital services?** [T2] -- special registration rules apply
10. **Input VAT credit balance carried forward from prior period** [T1]

**If items 1-2 are unknown, STOP. Do not classify any transactions until business tax type is confirmed.**

---

## Step 1: Tax System Overview [T1]

**Legislation:** Business Tax Act (BTA), Chapter 1, Art. 1-3.

Taiwan operates a dual business tax system:

| System | Applicable To | Rate | Method | Return Form |
|--------|--------------|------|--------|-------------|
| Value-Added Tax (VAT / 加值型營業稅) | General industries, manufacturing, trading, services | 5% | Credit-invoice method (output minus input) | Form 401 (每兩月) |
| Gross Business Receipts Tax (GBRT / 非加值型營業稅) | Financial institutions, insurance, small businesses (monthly sales < TWD 200,000), special drinking/entertainment establishments | 1-5% (varies by category) | Tax on gross receipts (no input credit) | Form 403 |

### VAT Rate [T1]

| Rate | Applies To | Legislation |
|------|-----------|-------------|
| 5% | All taxable goods and services (standard) | BTA Art. 10 |
| 0% | Exports, international transport, services to foreign enterprises for use outside Taiwan, goods to bonded zones/FTZs | BTA Art. 7 |
| Exempt | Specified goods/services listed in BTA Art. 8 | BTA Art. 8 |

### GBRT Rates [T1]

| Rate | Applies To | Legislation |
|------|-----------|-------------|
| 2% | Reinsurance premiums | BTA Art. 11(1) |
| 1% | Banks (core banking revenue: interest, commissions) | BTA Art. 11(2) |
| 2% | Insurance premiums (other than reinsurance) | BTA Art. 11(2) |
| 5% | Banks (non-core revenue: trading gains, etc.) | BTA Art. 11(2) |
| 2% | Trust investment companies, securities finance companies, short-term bill dealers | BTA Art. 11(2) |
| 5% | Pawnshops | BTA Art. 11(3) |
| 15-25% | Special drinking/entertainment establishments (夜總會, 酒家) | BTA Art. 12 |

---

## Step 2: VAT Registration [T1]

**Legislation:** BTA Art. 28, 29, 30.

### Registration Requirements

| Entity Type | Registration Required? | Threshold |
|-------------|----------------------|-----------|
| All profit-seeking enterprises | Yes -- must register before commencing business | No minimum threshold (all must register) |
| Foreign enterprises with fixed place of business in Taiwan | Yes | Upon establishment |
| Foreign e-service providers (cross-border digital services) | Yes -- if annual sales to Taiwan consumers >= TWD 600,000 (raised from TWD 480,000 effective April 2025) | TWD 600,000/year |
| Small-scale businesses (小規模營業人) | Register but assessed by tax authority (GBRT at 1%) | Monthly sales < TWD 200,000 |

### Registration Process [T1]

1. Apply to the local National Taxation Bureau
2. Obtain Unified Business Number (UBN / 統一編號)
3. Register on the MoF e-invoice platform (電子發票整合服務平台)
4. Set up electronic filing on eTax portal

**Legislation:** BTA Art. 28; Registration Rules for Business Tax.

---

## Step 3: Output VAT [T1]

**Legislation:** BTA Art. 14, 16.

### Calculation

```
Output VAT = Taxable Sales Amount (未含稅銷售額) x 5%
```

If the price is VAT-inclusive:
```
Sales Amount = VAT-inclusive Price / 1.05
Output VAT = Sales Amount x 5%
```

### Time of Supply (Tax Obligation Point) [T1]

| Transaction Type | Tax Point | Legislation |
|-----------------|-----------|-------------|
| Sale of goods | Delivery or payment received, whichever is earlier | BTA Art. 12-1 |
| Services | Service completed or payment received, whichever is earlier | BTA Art. 12-1 |
| Imports | Date of customs declaration | BTA Art. 15 |
| Long-term contracts | As per contract milestones or payment schedule | BTA Art. 12-1 |
| Consignment | Upon sale by consignee | BTA Art. 12-1 |

### Deemed Sales [T2]

| Situation | VAT Treatment | Legislation |
|-----------|--------------|-------------|
| Self-use of goods (non-business purpose) | Deemed sale at market value | BTA Art. 3(3) |
| Gifts to others | Deemed sale at market value | BTA Art. 3(3) |
| Dissolution/liquidation — remaining inventory | Deemed sale at market value | BTA Art. 3(3) |
| Transfer of goods between head office and branches (if separately registered) | Deemed sale | BTA Art. 3(3) |

**Flag for reviewer: deemed sale valuation must be confirmed by CPA.**

---

## Step 4: Zero-Rated Supplies [T1]

**Legislation:** BTA Art. 7.

The following are taxed at 0% (input VAT fully refundable):

| Zero-Rated Category | Details | Legislation |
|---------------------|---------|-------------|
| Export of goods | Goods shipped outside Taiwan (proof: export declaration) | BTA Art. 7(1) |
| Services related to exports | Processing, repairing, or manufacturing for exported goods | BTA Art. 7(2) |
| International transport | International transport services by domestic operators | BTA Art. 7(3) |
| Services to foreign enterprises | Services provided to foreign enterprises for use outside Taiwan | BTA Art. 7(4) |
| Goods to bonded areas | Sales to Export Processing Zones, Science Parks, bonded warehouses, FTZs | BTA Art. 7(5) |
| Goods sold to duty-free shops | Duty-free shop supplies | BTA Art. 7(6) |
| Sales to foreign diplomatic entities | Goods/services to embassies, consulates with reciprocity | BTA Art. 7(7) |

### Proof Requirements for Zero-Rating [T1]

| Category | Required Documents |
|----------|--------------------|
| Export of goods | Customs export declaration (出口報單); shipping documents |
| Services to foreign enterprises | Contract; proof of foreign enterprise status; proof service is for use outside Taiwan |
| International transport | Transport documents; passenger manifests / bills of lading |

---

## Step 5: Exempt Supplies [T1]

**Legislation:** BTA Art. 8.

The following are exempt from VAT (no output VAT; input VAT NOT deductible):

| Exempt Category | Description | BTA Art. 8 Item |
|----------------|-------------|----------------|
| Sale of land | Land transactions (building portion is taxable) | Item 1 |
| Water supply | Tap water supplied by water utilities | Item 2 |
| Medical services | Services by hospitals, clinics, nursing homes | Item 3 |
| Education | Tuition by schools, kindergartens, approved educational institutions | Item 4 |
| Banking / financial services | Interest, commissions of financial institutions (subject to GBRT instead) | Item 5 |
| Insurance | Insurance premiums (subject to GBRT instead) | Item 6 |
| Postal services | Stamps, postal money orders by Chunghwa Post | Item 7 |
| Government fees | Administrative fees, regulatory charges by government entities | Item 8 |
| Lottery tickets | Government-issued lottery tickets | Item 9 |
| Agricultural inputs | Fertilizers, pesticides, feeds, veterinary drugs, farm machinery | Item 10-13 |
| Fishery | Fish caught by fishermen and sold at wholesale fish markets | Item 14 |
| Magazines / newspapers | Sales by publishers (not advertising revenue) | Item 15 |
| Handicapped goods | Goods/equipment specifically designed for disabled persons | Item 16 |
| Residential rent | Rental of residential property | Item 17 |
| Research equipment | Imported instruments for research by academic institutions | Item 18 |
| Coastal/international ships and aircraft | Sale or lease | Item 19 |
| Diplomats | Goods/services to diplomats with reciprocity | Item 20 |
| Agricultural products | Unprocessed agricultural, forestry, fishery, livestock products sold by farmers | Item 21 |
| Secondhand goods | Consigned secondhand goods via qualified consignment dealers | Item 22 |
| Social welfare | Services by social welfare organizations | Item 23 |
| Voluntarily exempt small businesses | Small businesses with monthly sales below TWD 80,000 (goods) or TWD 50,000 (services, raised from TWD 40,000 effective 1 January 2025) | Item 27-28 |

---

## Step 6: Input VAT Credit Rules [T1]

**Legislation:** BTA Art. 15, 19, 33.

### Creditable Input VAT

| Document Type | Deductible? | Conditions |
|--------------|-------------|------------|
| Government Uniform Invoice (GUI / 統一發票) with UBN | Yes | Buyer's UBN must appear on invoice |
| Customs duty payment certificate | Yes | For import VAT paid at customs |
| E-invoice with UBN | Yes | Via MoF e-invoice platform |
| Receipt from small-scale business | Yes -- 1% deemed input | Only 1% of purchase amount is deductible |
| Simplified invoice without UBN | No | Cannot claim input VAT |

### Blocked Input VAT (Non-Deductible) [T1]

**Legislation:** BTA Art. 19.

The following input VAT may NOT be credited:

| Blocked Category | BTA Art. 19 Item |
|-----------------|-----------------|
| Purchases not for business use (personal consumption) | Item 1 |
| Entertainment expenses (交際費) | Item 2 |
| Gifts and donations | Item 2 |
| Passenger vehicles not essential to business operations | Item 3 |
| Goods/services for exempt supplies | Item 4 |
| Invoices not bearing the buyer's UBN | Item 5 |
| Purchases prior to business registration | Item 6 (exception: pre-opening expenses within certain period) |

### Mixed-Use Apportionment [T2]

**Legislation:** BTA Art. 19(3); Enforcement Rules Art. 26.

If a taxpayer makes both taxable and exempt supplies:

```
Non-deductible Input VAT = Total Input VAT x (Exempt Sales / Total Sales)
```

If the ratio of exempt sales to total sales is <= 10%, the taxpayer may claim ALL input VAT (de minimis rule).

**Flag for reviewer: apportionment ratio must be confirmed by CPA. Annual adjustment may be required.**

---

## Step 7: VAT Return Structure (Form 401) [T1]

**Legislation:** BTA Art. 35; Enforcement Rules Art. 33-38.

### Filing Period

| Period | Months Covered | Filing Deadline |
|--------|---------------|-----------------|
| Period 1 (Jan-Feb) | January + February | 15 March |
| Period 2 (Mar-Apr) | March + April | 15 May |
| Period 3 (May-Jun) | May + June | 15 July |
| Period 4 (Jul-Aug) | July + August | 15 September |
| Period 5 (Sep-Oct) | September + October | 15 November |
| Period 6 (Nov-Dec) | November + December | 15 January (following year) |

**Deadline rule:** If the 15th falls on a Saturday, Sunday, or national holiday, the deadline is extended to the next business day.

### Form 401 Key Sections

| Section | Line Items | Description |
|---------|-----------|-------------|
| I. Sales | Lines 1-9 | Taxable sales, zero-rated sales, exempt sales |
| II. Output VAT | Lines 10-14 | Output VAT on taxable sales |
| III. Input VAT | Lines 15-22 | Input VAT from purchases (by document type) |
| IV. Tax Payable / Refundable | Lines 23-30 | Net VAT calculation |

### Form 401 Detailed Line Mapping

| Line | Description | Category |
|------|-------------|----------|
| Line 1 | Sales at 5% (taxable domestic sales) | Output |
| Line 2 | Sales at 0% (zero-rated: exports, intl transport) | Output |
| Line 3 | Exempt sales | Output |
| Line 4 | Total sales (Line 1 + 2 + 3) | Output |
| Line 5 | Sales returns and allowances | Output (deduction) |
| Line 7 | Fixed asset sales | Output |
| Line 10 | Output VAT on Line 1 sales | Output VAT |
| Line 11 | Output VAT on fixed asset sales | Output VAT |
| Line 12 | Total output VAT | Output VAT |
| Line 15 | Input VAT from GUI (統一發票) | Input VAT |
| Line 16 | Input VAT from customs certificates | Input VAT |
| Line 17 | Input VAT from other deductible documents | Input VAT |
| Line 18 | Deemed input (1% from small-scale business receipts) | Input VAT |
| Line 19 | Input VAT on fixed asset purchases | Input VAT |
| Line 20 | Total input VAT | Input VAT |
| Line 21 | Less: non-deductible input VAT (BTA Art. 19) | Input VAT adjustment |
| Line 22 | Net deductible input VAT | Input VAT |
| Line 23 | VAT payable = Line 12 - Line 22 | Balance |
| Line 24 | Prior period overpayment / credit balance | Balance |
| Line 25 | VAT payable after credits | Balance |
| Line 27 | Refund claimed (for zero-rated excess input) | Refund |

---

## Step 8: GBRT Return (Form 403) [T1]

**Legislation:** BTA Art. 11, 12, 21, 22, 23.

### Filing Period

| Taxpayer Type | Period | Deadline |
|--------------|--------|----------|
| Banks, insurance, securities firms | Monthly / Quarterly (varies by category) | 15th of following month or quarter-end month |
| Special drinking/entertainment establishments | Bi-monthly (same as VAT) | 15th of month following period end |

### Form 403 Structure

| Section | Description |
|---------|-------------|
| I. Business Revenue | Gross receipts by category |
| II. Tax Calculation | Revenue x applicable GBRT rate |
| III. Tax Payable | Total GBRT due |

### GBRT taxpayers CANNOT claim input VAT credits [T1]

GBRT replaces VAT for these entities. They pay tax on gross receipts and have no credit-invoice mechanism.

---

## Step 9: E-Invoice System (電子發票) [T1]

**Legislation:** Uniform Invoice Award Regulations (統一發票給獎辦法); MoF e-invoice platform regulations.

### E-Invoice Requirements

| Requirement | Detail |
|-------------|--------|
| Mandatory for | All registered business entities |
| Platform | MoF e-Invoice Platform (財政部電子發票整合服務平台) |
| Format | XML-based electronic format; can be stored on cloud |
| Consumer invoices | May be stored in carrier (載具) — mobile barcode, NPC card, etc. |
| B2B invoices | Must include buyer's UBN for input VAT deduction |
| Archive period | 5 years minimum (paper or electronic) |

### Government Uniform Invoice (GUI / 統一發票) Types

| Type | Code | Use |
|------|------|-----|
| Triplicate GUI | 三聯式 | B2B transactions (buyer claims input VAT) |
| Duplicate GUI | 二聯式 | B2C transactions (consumer/no input claim) |
| Special GUI | 特種 | Special industries (GBRT taxpayers) |
| E-invoice | 電子發票 | Electronic equivalent of above types |
| Cash register receipt | 收銀機統一發票 | Retail (progressively replaced by e-invoice) |

### Invoice Lottery (統一發票兌獎) [T1]

Taiwan has a unique invoice lottery system where consumer invoice numbers are eligible for bi-monthly prize drawings. This does NOT affect VAT compliance but is relevant context:
- Special prize: TWD 10,000,000
- Grand prize: TWD 2,000,000
- Additional prizes for cloud-stored invoices

---

## Step 10: Import VAT [T1]

**Legislation:** BTA Art. 9, 41.

### VAT on Imports

| Item | Treatment |
|------|-----------|
| Imported goods | 5% VAT levied by Customs on (CIF value + customs duty + commodity tax + other charges) |
| Payment | At time of customs clearance |
| Input credit | Customs duty payment certificate is valid input VAT document |
| Importer | Any person importing goods (business or individual) |

### Import Exemptions [T1]

| Exemption | Legislation |
|-----------|-------------|
| Goods for military use | BTA Art. 9 |
| Goods imported by diplomatic entities with reciprocity | BTA Art. 9 |
| Goods for humanitarian relief | BTA Art. 9 |
| Returned export goods (within certain conditions) | Customs Act |

---

## Step 11: Cross-Border Digital Services [T2]

**Legislation:** BTA Art. 2-1, 6, 28-1; MoF Announcement No. 10504704390 (2017).

### Foreign E-Service Provider Registration

| Criterion | Detail |
|-----------|--------|
| Who must register? | Foreign enterprises providing electronic services to Taiwan individuals (B2C) |
| Threshold | Annual sales to Taiwan >= TWD 600,000 (raised from TWD 480,000, effective April 2025) |
| Registration | Apply to Taipei National Taxation Bureau |
| Filing | Bi-monthly Form 401 |
| Rate | 5% on Taiwan-sourced revenue |
| Input VAT | Cannot claim input VAT (no Taiwan purchases typically) |

### B2B Cross-Border Services [T1]

| Scenario | Treatment |
|----------|-----------|
| Foreign enterprise provides services to Taiwan business (B2B) | Taiwan buyer self-assesses and remits 5% VAT (reverse charge equivalent); buyer claims input VAT credit simultaneously if fully taxable |
| Taiwan buyer is fully engaged in taxable supplies (0% or 5% rate only) | Buyer is exempt from withholding obligation | BTA Art. 36(1) proviso |

**Flag for reviewer: verify B2B qualification and whether buyer is "exclusively engaged in taxable transactions" for the proviso to apply.**

---

## Step 12: Filing Deadlines and Penalties [T1]

### Filing Deadlines Summary

| Return | Period | Deadline |
|--------|--------|----------|
| Form 401 (VAT) | Bi-monthly | 15th of month following period end |
| Form 403 (GBRT) | Monthly or bi-monthly | 15th of month following period end |
| Annual VAT reconciliation (where applicable) | Annual | Per MoF announcement |
| Zero-rated refund application | With bi-monthly return | Filed with Form 401 |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | Surcharge: 1% of tax due per 2 days, up to 15% | BTA Art. 49 |
| Failure to register | Fine TWD 3,000-30,000; may be assessed tax retroactively | BTA Art. 45 |
| Failure to issue GUI | Fine 1-10x the tax amount on the uninvoiced sale | BTA Art. 52 |
| Issuing false invoices | Fine 1-10x the tax amount; criminal liability possible | BTA Art. 52; Tax Collection Act Art. 41-43 |
| Under-reporting sales | Additional tax + surcharge + fine up to 5x the underpaid tax | BTA Art. 51 |
| Failure to use e-invoice | Fine TWD 3,000-30,000 per instance | BTA Art. 45 |
| Late payment | Interest surcharge at 1% per month, up to 10% | Tax Collection Act Art. 20 |

---

## Step 13: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| VAT registration | All profit-seeking enterprises (no minimum) | BTA Art. 28 |
| Foreign e-service provider registration | Annual sales >= TWD 600,000 (raised from TWD 480,000, effective April 2025) | BTA Art. 28-1 |
| Small-scale business (GBRT assessed) | Monthly sales < TWD 200,000 | BTA Art. 13; Enforcement Rules Art. 9 |
| Small-scale business voluntary VAT exemption | Monthly sales < TWD 80,000 (goods) / TWD 50,000 (services, raised from TWD 40,000 effective 1 Jan 2025) | BTA Art. 8(27-28) |
| Mixed-use de minimis rule | Exempt sales <= 10% of total sales | BTA Art. 19(3); Enforcement Rules Art. 26 |
| Invoice retention period | 5 years | Tax Collection Act Art. 11 |

---

## Step 14: Edge Case Registry

### EC1 -- Land and Building Sold Together [T2]
**Situation:** Seller sells a property consisting of land and building in a single transaction.
**Resolution:** Land sale is exempt (BTA Art. 8, Item 1). Building sale is taxable at 5%. The total price must be apportioned between land and building. Apportionment typically follows the government-assessed values (公告地價 for land, 房屋評定現值 for building) unless a different allocation is contractually specified and commercially reasonable. Flag for reviewer: apportionment methodology.
**Legislation:** BTA Art. 8(1); MoF interpretive ruling.

### EC2 -- Foreign Enterprise Service Income [T1]
**Situation:** Taiwan company pays a US company for cloud software subscription (B2B).
**Resolution:** Taiwan buyer must withhold and remit 5% VAT on the payment (reverse charge equivalent). If the Taiwan buyer is exclusively engaged in taxable transactions (5% or 0% rate), the buyer is exempt from this withholding obligation per BTA Art. 36(1) proviso. If buyer makes any exempt supplies, must withhold.
**Legislation:** BTA Art. 36.

### EC3 -- Entertainment Expenses [T1]
**Situation:** Company purchases meals and drinks for client entertainment.
**Resolution:** Input VAT is BLOCKED under BTA Art. 19(2). The expense is deductible for income tax (subject to limits under Income Tax Act Art. 37) but input VAT is not recoverable.

### EC4 -- Employee Welfare / Gifts [T1]
**Situation:** Company purchases gifts for employee year-end party or Mid-Autumn Festival gifts.
**Resolution:** If gifts are for employees (not clients), input VAT is blocked as non-business use (BTA Art. 19(1)). If the company is deemed to have made a deemed supply, output VAT at 5% applies on the market value.
**Legislation:** BTA Art. 3(3), Art. 19(1).

### EC5 -- Passenger Vehicle Purchase [T1]
**Situation:** Company purchases a passenger car for general business use (not a taxi or rental company).
**Resolution:** Input VAT on passenger vehicles is BLOCKED under BTA Art. 19(3), unless the vehicle is essential to the business operations (e.g., car rental, taxi, driving school). If the entity is a car rental company, input VAT is deductible.

### EC6 -- Credit Notes and Sales Returns [T1]
**Situation:** Customer returns goods and a credit note is issued.
**Resolution:** Issue a Sales Return/Allowance Certificate (銷貨退回或折讓證明單). Seller reduces output VAT in the period the credit note is issued. Buyer must reduce input VAT in the same period.
**Legislation:** BTA Art. 15; Enforcement Rules Art. 24.

### EC7 -- Consignment Sales [T1]
**Situation:** Principal consigns goods to an agent/consignee for sale.
**Resolution:** Tax point is when the consignee sells to the final customer. Principal issues GUI to consignee upon sale. Consignment transfer itself is not a taxable event (unless separately registered entities).
**Legislation:** BTA Art. 3, 12-1.

### EC8 -- Pre-Opening Input VAT [T2]
**Situation:** Company incurs expenses before formal business registration.
**Resolution:** Input VAT on pre-opening expenses is generally blocked (BTA Art. 19(6)), BUT may be recovered if the company registers within a reasonable period and the expenses are directly related to the future business. Flag for reviewer.
**Legislation:** BTA Art. 19(6); MoF interpretive rulings.

### EC9 -- Construction Services for Own Use [T2]
**Situation:** Company constructs a building for its own use.
**Resolution:** Self-constructed assets are deemed sales. Output VAT is calculated on the construction cost. Input VAT on materials and services is deductible. Net effect may be zero but both sides must be reported. Flag for reviewer for valuation.
**Legislation:** BTA Art. 3(3)(3).

### EC10 -- Tax-Free Shop Sales [T1]
**Situation:** Retailer participates in the Foreign Passenger Tax Refund Scheme (外籍旅客購物退稅).
**Resolution:** Foreign passengers purchasing goods >= TWD 2,000 from approved Tax Refund Shopping (TRS) stores can claim VAT refund upon departure. The retailer charges and collects 5% VAT normally. Refund is processed by the refund agent at the airport/port.
**Legislation:** BTA Art. 7-1; Implementation Rules for Foreign Passenger VAT Refund.

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Taiwan CPA (會計師) or tax agent (記帳士) must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed CPA/tax agent. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard Domestic Sale, 5% VAT
**Input:** Taiwan company sells goods domestically. Invoice: TWD 105,000 VAT-inclusive. Rate: 5%.
**Expected output:** Sales amount = TWD 100,000. Output VAT = TWD 5,000. Report on Form 401 Line 1 (sales), Line 10 (output VAT).

### Test 2 -- Export Sale, Zero-Rated
**Input:** Taiwan manufacturer exports goods to the US. Export value: TWD 500,000. Customs export declaration obtained.
**Expected output:** Sales amount = TWD 500,000. Output VAT = TWD 0. Report on Form 401 Line 2 (zero-rated sales). Input VAT on related purchases fully refundable.

### Test 3 -- Input VAT on Domestic Purchase
**Input:** Taiwan company purchases raw materials. GUI shows: sales TWD 200,000, VAT TWD 10,000. Buyer UBN on invoice.
**Expected output:** Input VAT = TWD 10,000. Deductible in full. Report on Form 401 Line 15.

### Test 4 -- Entertainment Expense (Blocked)
**Input:** Company pays TWD 10,500 (VAT-inclusive) for client entertainment dinner. GUI received.
**Expected output:** Input VAT = TWD 500. BLOCKED under BTA Art. 19(2). Non-deductible. Expense of TWD 10,500 gross.

### Test 5 -- Passenger Vehicle (Blocked)
**Input:** Non-car-rental company purchases a car. Price TWD 1,050,000 VAT-inclusive. GUI received.
**Expected output:** Input VAT = TWD 50,000. BLOCKED under BTA Art. 19(3). Non-deductible.

### Test 6 -- Cross-Border Service (B2B Reverse Charge)
**Input:** Taiwan company (fully taxable) pays US cloud provider TWD 30,000 for SaaS subscription.
**Expected output:** Taiwan buyer is exempt from withholding per BTA Art. 36(1) proviso (exclusively engaged in taxable transactions). No VAT withholding required. If buyer also makes exempt supplies, must withhold and remit TWD 1,500 (5%) and claim input credit.

### Test 7 -- Exempt Supply (Medical Services)
**Input:** Hospital provides medical services. Revenue TWD 1,000,000.
**Expected output:** Exempt under BTA Art. 8(3). No output VAT. Input VAT on related purchases NOT deductible. Report on Form 401 Line 3 (exempt sales).

### Test 8 -- Import of Goods
**Input:** Company imports machinery. CIF value TWD 1,000,000. Customs duty TWD 50,000. No commodity tax.
**Expected output:** Import VAT = (1,000,000 + 50,000) x 5% = TWD 52,500. Paid at customs. Input VAT TWD 52,500 deductible via customs duty payment certificate on Form 401 Line 16.

---

## PROHIBITIONS [T1]

- NEVER allow GBRT taxpayers to claim input VAT credits (GBRT is a gross receipts tax with no credit mechanism)
- NEVER claim input VAT without a valid GUI bearing the buyer's UBN
- NEVER claim input VAT on entertainment, gifts, donations, or non-business personal consumption
- NEVER claim input VAT on passenger vehicles unless the entity is in the vehicle rental, taxi, or driving school business
- NEVER confuse zero-rated (0%, input VAT refundable) with exempt (no VAT, input VAT NOT refundable)
- NEVER apply the 5% VAT rate to GBRT-classified entities (use GBRT rates)
- NEVER file Form 401 for a GBRT taxpayer or Form 403 for a VAT taxpayer
- NEVER ignore the de minimis rule for mixed-use apportionment (exempt sales <= 10% = full input credit)
- NEVER issue or accept invoices without the e-invoice platform registration
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not by the AI

---

## Step 17: VAT Compliance Calendar [T1]

### Bi-Monthly Filing Timeline

| Period | Months Covered | Key Actions | Deadline |
|--------|---------------|-------------|----------|
| Period 1 | Jan-Feb | Compile Jan+Feb invoices; reconcile e-invoice platform data | 15 Mar |
| Period 2 | Mar-Apr | Compile Mar+Apr invoices; file Form 401/403 | 15 May |
| Period 3 | May-Jun | Compile May+Jun invoices | 15 Jul |
| Period 4 | Jul-Aug | Compile Jul+Aug invoices | 15 Sep |
| Period 5 | Sep-Oct | Compile Sep+Oct invoices | 15 Nov |
| Period 6 | Nov-Dec | Compile Nov+Dec invoices; year-end reconciliation | 15 Jan (next year) |

### Pre-Filing Checklist [T1]

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Download e-invoice data from MoF platform for the bi-monthly period | E-invoice platform |
| 2 | Reconcile sales invoices (issued GUIs) with accounting records | Form 401, Section I |
| 3 | Reconcile purchase invoices (received GUIs with UBN) with accounting records | Form 401, Section III |
| 4 | Identify and exclude blocked input VAT (Art. 19 items) | BTA Art. 19 |
| 5 | Calculate apportionment ratio if mixed taxable/exempt supplies | BTA Art. 19(3) |
| 6 | Check credit balance carried forward from prior period | Form 401, Line 24 |
| 7 | Prepare zero-rated documentation (export declarations, contracts) | BTA Art. 7 |
| 8 | File electronically via eTax portal | eTax Portal |
| 9 | Remit payment via bank transfer or designated payment channels | By same deadline |

---

## Step 18: Industry-Specific VAT Rules [T2]

### Real Estate Transactions

| Transaction | Tax Treatment | Rate | Notes |
|------------|--------------|------|-------|
| Sale of land | Exempt (BTA Art. 8(1)) | N/A | Land value tax applies separately |
| Sale of building | Taxable | 5% | On building portion only (apportion from land) |
| Residential rent | Exempt (BTA Art. 8(17)) | N/A | Commercial rent is taxable at 5% |
| Commercial rent | Taxable | 5% | Landlord charges 5% VAT; tenant claims input |
| Construction services | Taxable | 5% | Standard rate |

### Financial Services (GBRT Entities)

| Activity | Tax Type | Rate | Notes |
|----------|---------|------|-------|
| Bank interest income | GBRT | 1% (core) / 5% (non-core) | No input credit |
| Insurance premiums | GBRT | 2% | No input credit |
| Securities brokerage | GBRT | 2% | No input credit |
| Reinsurance premiums | GBRT | 2% | No input credit |
| Fund management fees | GBRT | 2% | No input credit |

### E-Commerce and Digital Economy [T2]

| Scenario | Treatment |
|----------|-----------|
| Taiwan company sells goods online domestically | Standard 5% VAT; must issue e-invoice |
| Taiwan company sells digital services to foreign consumers | Zero-rated (BTA Art. 7(4)) if for use outside Taiwan |
| Foreign platform sells to Taiwan consumers (B2C) | Foreign provider must register if annual sales >= TWD 480,000; charge 5% |
| Foreign platform sells to Taiwan business (B2B) | Taiwan buyer self-assesses (reverse charge); may be exempt per Art. 36(1) proviso |

**Flag for reviewer: digital economy transactions require case-by-case assessment of where the service is "used" for place of supply purposes.**

---

## Step 19: Penalties Detail and Dispute Resolution [T1]

### Penalty Calculation Examples

| Scenario | Calculation |
|----------|-------------|
| Return due 15 Mar, filed 25 Mar (10 days late) | 1% x tax due x (10/2) = 5% surcharge on tax |
| Return due 15 Mar, filed 15 Apr (31 days late) | Capped at 15% surcharge |
| Sales of TWD 1,000,000 not reported | Additional tax TWD 50,000 (5%) + surcharge + fine up to 5x |
| Failure to issue GUI on TWD 100,000 sale | Fine: 1-10x of TWD 5,000 (the tax) = TWD 5,000-50,000 |

### Dispute Resolution [T2]

| Step | Process | Deadline |
|------|---------|----------|
| 1. Administrative review | Apply to original NTB for reassessment | 30 days from assessment notice |
| 2. Administrative appeal | Appeal to MoF Appeals Committee | 30 days from review decision |
| 3. Administrative litigation | File with Administrative Court | 2 months from appeal decision |
| 4. Supreme Administrative Court | Final appeal | Per court rules |

**Flag for reviewer: tax disputes should involve a licensed tax agent or CPA. Do not self-represent without professional advice.**

---

## Step 20: Tax Incentives Related to VAT [T2]

### Statute for Industrial Innovation

| Incentive | Detail | Legislation |
|-----------|--------|-------------|
| R&D tax credit | 15% of qualifying R&D expenditure (income tax credit, not VAT) | Statute for Industrial Innovation, Art. 10 |
| Smart machinery investment credit | 5% of qualifying investment | Art. 10-1 |
| Biotech company tax holiday | 5-year income tax exemption | Biotech Industry Development Act |

**Note:** These are income tax incentives, NOT VAT incentives. However, VAT on purchases for qualifying activities remains deductible under standard rules.

### Free Trade Zones / Bonded Warehouses [T2]

| Zone Type | VAT Treatment |
|-----------|--------------|
| Export Processing Zone (加工出口區) | Goods entering zone: zero-rated; goods leaving to domestic: taxable at 5% |
| Science Park (科學園區) | Similar to EPZ for bonded goods |
| Free Trade Zone (自由貿易港區) | Goods in zone: outside VAT scope; goods entering domestic market: import VAT at 5% |
| Bonded warehouse | VAT deferred until goods cleared for domestic consumption |

---

## Step 21: Direct Tax Reference (Out of Scope) [T3]

This skill does NOT cover direct taxes. The following is reference only:

- **Profit-Seeking Enterprise Income Tax:** Standard rate 20%. Surtax of 5% on undistributed earnings. Legislation: Income Tax Act (所得稅法).
- **Individual Income Tax:** Progressive rates 5%, 12%, 20%, 30%, 40%. Legislation: Income Tax Act.
- **Alternative Minimum Tax (AMT):** Rate 12% for enterprises, 20% for individuals. Legislation: Income Basic Tax Act.
- **Stamp Duty:** Varies by document type (0.1-0.4%). Legislation: Stamp Duty Act.
- **Securities Transaction Tax:** 0.3% on listed securities sales. Legislation: Securities Transaction Tax Act.

---

## Contribution Notes

This skill covers the Taiwan VAT/Business Tax framework as of early 2026. Taiwan's business tax system is relatively stable compared to other jurisdictions but practitioners should monitor MoF announcements for threshold adjustments and e-invoice platform updates.

**A skill may not be published without sign-off from a licensed practitioner (會計師 or 記帳士) in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
