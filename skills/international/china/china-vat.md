---
name: china-vat
description: Use this skill whenever asked to prepare, review, or advise on a China VAT return, VAT classification, fapiao management, or any matter involving Chinese value-added tax. Trigger on phrases like "China VAT", "Chinese VAT return", "fapiao", "Golden Tax", "general taxpayer", "small-scale taxpayer", "export VAT refund", "input VAT credit", or any request involving PRC VAT obligations. This skill contains the complete China VAT rate structure, taxpayer classifications, input credit rules, fapiao requirements, export refund mechanics, and filing deadlines required to produce correct VAT compliance advice. ALWAYS read this skill before touching any China VAT-related work.
---

# China VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | People's Republic of China (PRC) |
| Jurisdiction Code | CN |
| Primary Legislation | Value-Added Tax Law of the PRC (adopted 25 Dec 2024, effective 1 Jan 2026), replacing the Provisional Regulations on Value-Added Tax (State Council Decree No. 538) |
| Supporting Legislation | Implementation Regulations of the VAT Law (State Council Decree, 25 Dec 2025); Caishui [2016] No. 36 (B2V reform); Caishui [2019] No. 39 (rate reduction); Caishui [2023] No. 1 (small-scale taxpayer relief, extended through 2027); State Taxation Administration Announcement [2019] No. 14 |
| Tax Authority | State Taxation Administration (STA / 国家税务总局) |
| Filing Portal | Electronic Tax Bureau (各省电子税务局) — province-specific portals |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, taxpayer type determination, fapiao rules, basic input credit. Tier 2: export refund calculations, mixed sales classification, deemed sales. Tier 3: transfer pricing adjustments, restructuring, cross-border digital services. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Unified Social Credit Code (统一社会信用代码)** [T1] -- 18-character alphanumeric code
2. **Taxpayer classification** [T1] -- General taxpayer (一般纳税人) or Small-scale taxpayer (小规模纳税人)
3. **Industry sector** [T2] -- determines applicable rate (13%, 9%, 6%, or exempt); confirm with tax adviser for borderline cases
4. **Filing period** [T1] -- monthly (general taxpayers default) or quarterly (small-scale taxpayers default; general taxpayers may elect quarterly with STA approval)
5. **Does the business export goods or services?** [T2] -- triggers exempt-credit-refund method or exempt-with-refund method
6. **Does the business make exempt supplies?** [T2] -- impacts input VAT apportionment
7. **Does the business operate in a Free Trade Zone (FTZ)?** [T2] -- special rules apply
8. **Golden Tax System / tax control device type** [T1] -- UKey, tax control disk, or fully electronic fapiao (全电发票) pilot
9. **Provincial tax bureau** [T1] -- determines which Electronic Tax Bureau portal to use
10. **VAT credit carry-forward balance from prior period** [T1] -- excess input VAT carried forward

**If items 1-2 are unknown, STOP. Do not classify any transactions until taxpayer classification is confirmed.**

---

## Step 1: VAT Rate Structure [T1]

**Legislation:** VAT Law Art. 3 (effective 1 Jan 2026); Caishui [2019] No. 39.

**NOTE:** The new VAT Law (effective 1 January 2026) codifies the existing rate structure. The core rates (13%, 9%, 6%, 0%) remain unchanged from the prior Provisional Regulations.

### Standard Rates for General Taxpayers

| Rate | Applies To | Legislative Basis |
|------|-----------|-------------------|
| 13% | Sale/import of goods (tangible movable property); processing, repair, and replacement services; leasing of tangible movable property | VAT Law Art. 3(1); Caishui [2019] No. 39 Art. 1 |
| 9% | Transportation services; postal services; basic telecommunications; construction services; sale/lease of immovable property; transfer of land use rights; agricultural products; tap water; heating; natural gas; LPG; coal products; books, newspapers, magazines; feed, fertilizer, pesticides; grain | VAT Law Art. 3(2); Caishui [2019] No. 39 Art. 1 |
| 6% | Value-added telecommunications; financial services; modern services (R&D, IT, consulting, design, logistics support); lifestyle services (culture, sports, education, healthcare, tourism, catering, accommodation); sale of intangible assets (excluding land use rights); insurance | VAT Law Art. 3(3); Caishui [2016] No. 36, Annex 1 |
| 0% | Exported goods (unless otherwise specified); cross-border taxable services and intangible assets listed in Caishui [2016] No. 36 Annex 4 | VAT Law Art. 3(4); Caishui [2016] No. 36 |

### Small-Scale Taxpayer Rates

| Rate | Applies To | Legislative Basis |
|------|-----------|-------------------|
| 3% | Standard simplified collection rate for all supplies | Provisional Regulations Art. 12 |
| 1% | Temporary reduced rate (1 Jan 2023 -- 31 Dec 2027) for small-scale taxpayers | Caishui [2023] No. 1; extended by subsequent announcements |
| 5% | Sale/lease of immovable property acquired before 30 Apr 2016; labour dispatch (difference method); HRM outsourcing; certain specified items | Various STA announcements |
| 0.5% | Used car dealers (small-scale) | Caishui [2020] No. 17 |

### Withholding Rate

| Rate | Applies To |
|------|-----------|
| 6% or 10% | Non-resident entities providing services/intangibles/immovable property to PRC recipients (withholding agent must withhold and remit) |

---

## Step 2: Taxpayer Classification [T1]

**Legislation:** VAT Law Art. 8-9 (effective 1 Jan 2026); STA Announcement [2018] No. 18.

### General Taxpayer vs Small-Scale Taxpayer

| Criterion | General Taxpayer | Small-Scale Taxpayer |
|-----------|-----------------|---------------------|
| Annual taxable sales threshold | > CNY 5,000,000 | <= CNY 5,000,000 |
| VAT method | Credit-invoice method (output minus input) | Simplified method (flat rate on sales) |
| Input VAT deduction | Yes -- deductible against output | No -- cannot deduct input VAT |
| Fapiao issuance | General VAT fapiao (增值税普通发票) and Special VAT fapiao (增值税专用发票) | General fapiao; may self-issue special fapiao since 2020 |
| Filing period (default) | Monthly (by 15th of following month) | Quarterly (by 15th of month following quarter end) |

### Mandatory General Taxpayer Registration [T1]

A taxpayer whose annual taxable sales exceed CNY 5,000,000 in any consecutive 12-month or 4-quarter period MUST register as a general taxpayer. Under the new VAT Law (2026), enterprises exceeding the threshold must calculate and pay VAT using the general tax method from the period in which the threshold is exceeded. Only "non-business units that do not frequently engage in taxable activities" may choose to remain as small-scale taxpayers after exceeding the threshold; companies are no longer eligible for this exception.

**Legislation:** VAT Law Art. 9; STA Announcement [2018] No. 18, Art. 2.

### Voluntary Registration [T1]

Small-scale taxpayers below the threshold may voluntarily register as general taxpayers. Once registered, they generally cannot revert to small-scale status (one-time conversion window in 2018 was a special policy).

---

## Step 3: Fapiao (Invoice) System [T1]

**Legislation:** PRC Invoice Administration Measures (State Council Decree No. 587); STA Announcement [2021] No. 23 (fully electronic fapiao pilot).

### Fapiao Types

| Fapiao Type | Chinese Name | Issued By | Input VAT Deductible? |
|-------------|-------------|-----------|----------------------|
| Special VAT Fapiao | 增值税专用发票 | General taxpayers (and qualifying small-scale) | Yes -- for general taxpayer recipients |
| General VAT Fapiao | 增值税普通发票 | All taxpayers | No (exceptions: toll road, passenger transport) |
| Fully Electronic Fapiao | 全电发票 (电子发票) | Pilot regions -- all taxpayers | Yes -- if special-type electronic fapiao |
| Customs Import VAT Payment Certificate | 海关进口增值税专用缴款书 | Customs | Yes -- after cross-check verification |
| Withholding Tax Certificate | 完税凭证 | Tax authority | Yes -- for withheld VAT on cross-border services |
| Agricultural Purchase Fapiao | 农产品收购发票 | Buyer (self-issued) | Yes -- deemed input at 9% (or 10% for deep processing) |
| Toll Road Electronic Fapiao | 通行费电子发票 | Toll operators | Yes -- if classified as special-type |

### Fapiao Authentication and Cross-Check [T1]

General taxpayers must authenticate (认证/勾选确认) special VAT fapiao within 360 days of issuance to claim input VAT credit. Since 2020, authentication is performed via the Comprehensive Service Platform for VAT Invoices (增值税发票综合服务平台).

**Failure to authenticate within 360 days = input VAT permanently lost** (except in documented special circumstances approved by STA).

### Red-Letter Fapiao (Credit Notes) [T1]

| Situation | Procedure |
|-----------|-----------|
| Sales return / discount after fapiao issued | Issue red-letter (negative) special fapiao via Golden Tax System |
| Buyer rejects fapiao / error discovered | Buyer applies for Red-Letter Information Form; seller issues red-letter fapiao |
| Fapiao voided in same month | Void original; issue corrected fapiao |

**Legislation:** STA Announcement [2016] No. 47.

---

## Step 4: Output VAT Calculation [T1]

**Legislation:** Provisional Regulations Art. 4, 5, 6.

### General Taxpayer Output VAT

```
Output VAT = Sales Amount (不含税销售额) x Applicable Rate
```

Where Sales Amount is the VAT-exclusive price. If the price is VAT-inclusive:

```
Sales Amount = VAT-inclusive Price / (1 + Applicable Rate)
```

### Small-Scale Taxpayer VAT Payable

```
VAT Payable = Sales Amount x Collection Rate (3% or 1%)
Sales Amount = VAT-inclusive Price / (1 + Collection Rate)
```

### Deemed Sales (视同销售) [T2]

The following are treated as taxable sales even without payment. Flag for reviewer confirmation:

| Deemed Sale Situation | Legislation |
|----------------------|-------------|
| Consignment of goods to another entity for sale | Provisional Regulations Implementation Rules Art. 4(1) |
| Sale of consigned goods | Art. 4(2) |
| Transfer of goods between locations for separate accounting entities | Art. 4(3) |
| Using self-produced or commissioned goods for non-VAT projects | Art. 4(4) |
| Using self-produced or commissioned goods for collective welfare or personal consumption | Art. 4(5) |
| Using self-produced, commissioned, or purchased goods as investment | Art. 4(6) |
| Distributing self-produced, commissioned, or purchased goods to shareholders | Art. 4(7) |
| Gifting self-produced, commissioned, or purchased goods to others | Art. 4(8) |

---

## Step 5: Input VAT Credit Rules [T1]

**Legislation:** Provisional Regulations Art. 8, 10; Caishui [2016] No. 36, Art. 27.

### Creditable Input VAT

| Document Type | Credit Amount | Conditions |
|--------------|---------------|------------|
| Special VAT fapiao | VAT amount shown | Must be authenticated/cross-checked |
| Customs import VAT certificate | VAT amount shown | Must pass cross-check verification (稽核比对) |
| Agricultural purchase fapiao | Face value x 9% (deemed deduction) | Self-issued by buyer; 10% if inputs used for 13%-rate products |
| Domestic passenger transport fapiao | Varies by transport type | Employee's own travel; electronic special fapiao, e-ticket with ID |
| Toll road electronic fapiao | VAT amount shown | Must be special-type electronic fapiao |
| Withholding tax certificate | Withheld VAT amount | Cross-border service purchases |

### Passenger Transport Input VAT Specifics [T1]

| Transport Document | Input VAT Calculation |
|-------------------|----------------------|
| Air e-ticket itinerary | (Fare + Fuel Surcharge) / (1 + 9%) x 9% |
| Rail ticket | Face value / (1 + 9%) x 9% |
| Road/waterway ticket | Face value / (1 + 3%) x 3% |
| Electronic fapiao (special type) | VAT amount shown on fapiao |

**Legislation:** Caishui [2019] No. 39, Art. 6.

### Blocked Input VAT (Non-Deductible) [T1]

**Legislation:** Provisional Regulations Art. 10; Caishui [2016] No. 36, Art. 27.

The following input VAT may NOT be credited regardless of valid fapiao:

| Blocked Category | Legislation |
|-----------------|-------------|
| Purchases for simplified-method items | Art. 27(1) |
| Purchases for VAT-exempt items | Art. 27(1) |
| Purchases for collective welfare (集体福利) | Art. 27(1) |
| Purchases for personal consumption (个人消费) | Art. 27(1) |
| Abnormal losses of purchased goods and related transport/processing | Art. 10(2); Art. 27(2) |
| Abnormal losses of in-process/finished goods consuming purchased goods | Art. 10(3); Art. 27(3) |
| Purchased passenger services (for entertaining guests -- not employee travel) | Art. 27(6) |
| Catering services, resident daily services, entertainment services | Art. 27(6) |
| Loan interest (贷款服务) | Art. 27(4) |

### Mixed-Use Input VAT Apportionment [T2]

If purchased goods or services are used for BOTH creditable and non-creditable purposes, input VAT must be apportioned. The general formula:

```
Non-creditable Input VAT = Total Input VAT x (Exempt + Simple Method Revenue) / Total Revenue
```

**Flag for reviewer: apportionment methodology must be confirmed by tax adviser. STA may accept alternative reasonable methods.**

---

## Step 6: VAT Return Structure [T1]

### General Taxpayer VAT Return (增值税纳税申报表 — 一般纳税人适用)

The general taxpayer return consists of:

| Form | Chinese Name | Content |
|------|-------------|---------|
| Main Form | 主表 | Summary of output VAT, input VAT, tax payable, credits |
| Schedule 1 | 附表一 | Details of sales and output VAT by rate and category |
| Schedule 2 | 附表二 | Details of input VAT credits by source document |
| Schedule 3 | 附表三 | Service, intangible, immovable property deduction details (差额征税) |
| Schedule 4 | 附表四 | VAT credit/refund calculation (加计抵减, 留抵退税) |
| Deduction Schedule | 减免税明细表 | Tax reduction/exemption details |
| Additional Data | 增值税附加税费申报表 | Urban maintenance and construction tax, education surcharge, local education surcharge |

### Main Form Key Lines

| Line | Description | Source |
|------|-------------|--------|
| Line 1 | Sales at 13% rate (goods, processing/repair, tangible property leasing) | Schedule 1 |
| Line 2 | Sales at 9% rate (transport, construction, immovable property, agriculture) | Schedule 1 |
| Line 3 | Sales at 6% rate (services, intangibles, financial) | Schedule 1 |
| Line 4 | Tax-exempt sales | Schedule 1 |
| Line 5 | Total sales for simplified method items | Schedule 1 |
| Line 11 | Output VAT (total) | Schedule 1 |
| Line 12 | Input VAT (total for period) | Schedule 2 |
| Line 13 | Input VAT transferred out (转出) | Schedule 2 |
| Line 14 | Exempt/credit/refund for exported goods — offset domestic | Export-related schedule |
| Line 17 | Input VAT carried forward from prior period (期初留抵税额) | Prior return |
| Line 18 | Actual input VAT deductible this period | Calculated |
| Line 19 | Excess input VAT carried forward to next period (期末留抵税额) | Calculated |
| Line 24 | Total VAT payable (应纳税额) | Line 11 - Line 18 |
| Line 34 | Total amount payable this period | Final payable |

### Small-Scale Taxpayer VAT Return (小规模纳税人适用)

| Line | Description |
|------|-------------|
| Line 1 | Taxable sales (excluding tax) at applicable collection rate |
| Line 4 | Tax-exempt sales |
| Line 10 | Total sales for this period |
| Line 15 | VAT payable this period |
| Line 18 | Tax reductions (e.g., equipment offset) |
| Line 20 | Amount payable (after reductions) |

---

## Step 7: Export VAT Treatment [T2]

**Legislation:** Caishui [2012] No. 39 (Export VAT Refund Management Measures).

### Exempt-Credit-Refund Method (免抵退税) [T2]

Applies to: General taxpayer manufacturers that export self-produced goods.

```
1. Exempt: export sales exempt from output VAT
2. Credit: input VAT on domestic purchases credits against domestic output VAT
3. Refund: excess input VAT (after crediting domestic output) refunded up to the refund rate limit

Non-refundable amount = Export FOB x (Applicable Rate - Export Refund Rate)
Deemed input = Export FOB x Export Refund Rate
Refund limit = lesser of (excess input VAT, deemed input)
```

### Exempt-with-Refund Method (免退税) [T2]

Applies to: Trading companies (外贸企业) that purchase goods domestically and export them.

```
Refund = Purchase price (VAT-exclusive) x Export Refund Rate
```

### Export Refund Rates [T1]

Export refund rates vary by HS code and are published by the STA. Common rates:

| Category | Typical Refund Rate |
|----------|-------------------|
| Machinery, electronics | 13% |
| Textiles, garments | 13% |
| Agricultural products | 5-9% |
| Resource-intensive products | 0% (export tax may apply instead) |

**Flag for reviewer: export refund rate must be verified against the current HS code table for each specific product. Rates change frequently via STA/MoF announcements.**

---

## Step 8: Surcharges on VAT [T1]

**Legislation:** Various; computed as a percentage of VAT actually paid.

| Surcharge | Rate | Legislation |
|-----------|------|------------|
| Urban Maintenance and Construction Tax (城市维护建设税) | 7% (urban), 5% (county/town), 1% (other) | Urban Maintenance and Construction Tax Law (2020) |
| Education Surcharge (教育费附加) | 3% | State Council regulations |
| Local Education Surcharge (地方教育附加) | 2% | Provincial regulations |

**Total effective surcharge: 12% of VAT payable (urban areas).**

Small-scale taxpayers with monthly sales <= CNY 100,000 (quarterly <= CNY 300,000) are exempt from education surcharges. Caishui [2023] No. 1 extends 50% reduction on surcharges for small-scale taxpayers through 31 Dec 2027.

---

## Step 9: Filing Deadlines [T1]

**Legislation:** Provisional Regulations Art. 23; Tax Collection Administration Law Art. 25.

| Taxpayer Type | Default Period | Deadline | Notes |
|--------------|---------------|----------|-------|
| General taxpayer | Monthly | 15th of following month | Extended if 15th falls on holiday/weekend |
| Small-scale taxpayer | Quarterly | 15th of month following quarter end | Q1: 15 Apr; Q2: 15 Jul; Q3: 15 Oct; Q4: 15 Jan |
| Withholding agent | Per transaction or monthly | 15th of following month | For non-resident VAT withholding |
| Import VAT | Per transaction | At time of customs declaration | Paid to Customs, not STA |

### Late Filing Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | CNY 200-10,000 fine; late payment surcharge at 0.05%/day | Tax Collection Administration Law Art. 62, Art. 32 |
| Failure to register as general taxpayer | Output VAT at general rate, NO input credit | STA Announcement [2018] No. 18, Art. 8 |
| Fraudulent fapiao | Criminal liability; 2-7 years imprisonment | Criminal Law Art. 205 |
| Failure to issue fapiao | CNY 10,000-50,000 fine | Invoice Administration Measures Art. 35 |

---

## Step 10: Special VAT Policies [T2]

### Small-Scale Taxpayer Exemptions (Current through 2027)

| Policy | Threshold | Legislation |
|--------|-----------|-------------|
| VAT exemption | Monthly sales <= CNY 100,000 (quarterly <= CNY 300,000). Under the 2026 VAT Law, this threshold is elevated from a transitional preferential policy to a statutory provision (effective 1 Jan 2026 through 31 Dec 2027). | Caishui [2023] No. 1; VAT Law Implementation Regulations (2025) |
| Reduced collection rate | 1% instead of 3% on taxable sales (effective 1 Jan 2023 through 31 Dec 2027) | Caishui [2023] No. 1 |
| Surcharge reduction | 50% reduction on urban maintenance tax, education surcharges | Caishui [2023] No. 1 |

### Super Deduction (加计抵减) [T2]

Certain industries may claim an additional percentage of input VAT as a deemed deduction:

| Industry | Additional Deduction | Period | Legislation |
|----------|---------------------|--------|-------------|
| Advanced manufacturing | 5% of deductible input VAT | 2023-2027 | Caishui [2023] No. 43 |
| Integrated circuit / industrial machine tools | 15% of deductible input VAT | 2023-2027 | Caishui [2023] No. 44 |

**Flag for reviewer: eligibility for super deduction requires industry classification verification and that the relevant industry revenue exceeds 50% of total revenue.**

### Incremental VAT Credit Refund (增量留抵退税) [T2]

Since April 2022, all industries may apply for refund of incremental excess input VAT credits (留抵退税), subject to conditions:

1. Tax credit rating A or B
2. No fraudulent refund/offset/fapiao record in prior 36 months
3. No criminal tax record in prior 36 months
4. No prior refund abuse

**Legislation:** Caishui [2022] No. 14.

**Flag for reviewer: refund application requires detailed review of eligibility conditions and STA approval.**

---

## Step 11: Cross-Border Digital Services [T2]

**Legislation:** Caishui [2016] No. 36, Art. 6, 12, 13; STA Announcement [2017] No. 43.

### Non-Resident Providing Services to PRC Buyer

| Scenario | VAT Treatment |
|----------|--------------|
| Non-resident has PRC establishment | Self-assess and file VAT |
| Non-resident has no PRC establishment; PRC buyer is general taxpayer | Buyer withholds VAT at applicable rate |
| Non-resident has no PRC establishment; PRC buyer is individual/small-scale | Non-resident appoints agent or STA designates withholding agent |
| Services wholly performed outside China with no domestic consumption | Outside scope of PRC VAT |

### Place of Supply Rules [T2]

| Service Type | Place of Supply |
|-------------|----------------|
| Services related to immovable property | Location of property |
| Construction services | Location of construction site |
| Passenger transport | Departure point |
| B2B services (general rule) | Buyer's location |
| B2C services (general rule) | Seller's location |

**Flag for reviewer: cross-border service characterization and place of supply require case-by-case analysis by tax adviser.**

---

## Step 12: Key Thresholds Summary

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| General taxpayer mandatory registration | Annual taxable sales > CNY 5,000,000 | STA Announcement [2018] No. 18 |
| Small-scale VAT exemption | Monthly sales <= CNY 100,000 / Quarterly <= CNY 300,000 (statutory from 1 Jan 2026) | Caishui [2023] No. 1; VAT Law Implementation Regulations (2025) |
| Fapiao authentication window | 360 days from issuance | STA Announcement [2019] No. 45 |
| Late payment surcharge | 0.05% per day | Tax Collection Administration Law Art. 32 |
| Export refund filing deadline | Before tax filing deadline of following month after export declaration | Caishui [2012] No. 39 |

---

## Step 13: Edge Case Registry

### EC1 -- Mixed Sales (混合销售) [T2]
**Situation:** A single transaction involves both goods and services (e.g., equipment sale with installation).
**Resolution:** If the entity primarily sells goods, the entire transaction is taxed at the goods rate (13%). If the entity primarily provides services, the entire transaction is taxed at the service rate (6% or 9%). "Primarily" is determined by the entity's principal business registration. Flag for reviewer when classification is ambiguous.
**Legislation:** Caishui [2016] No. 36, Art. 40.

### EC2 -- Concurrent Operations (兼营) [T2]
**Situation:** An entity sells goods at 13% and also provides consulting services at 6%.
**Resolution:** Must separately account for sales at each rate. If not separately accounted, the highest applicable rate (13%) applies to all.
**Legislation:** Provisional Regulations Art. 3; Caishui [2016] No. 36, Art. 39.

### EC3 -- Related-Party Pricing Below Market [T2]
**Situation:** Sales between related parties at prices significantly below market value without legitimate business purpose.
**Resolution:** STA may adjust the sales price using: (1) recent arm's length transaction price, (2) composite cost plus reasonable profit, (3) assessed value. Flag for reviewer.
**Legislation:** Provisional Regulations Art. 7.

### EC4 -- Prepaid Cards / Gift Cards [T1]
**Situation:** Entity sells or purchases prepaid cards (预付卡/购物卡).
**Resolution:** Sale of prepaid card is NOT a taxable supply (no fapiao for goods/services issued at point of sale). Seller issues a general fapiao marked "prepaid card sale" (预付卡销售). VAT is triggered when the card is redeemed. Purchasing entity cannot claim input VAT on card purchase.
**Legislation:** STA Announcement [2016] No. 53.

### EC5 -- Construction Services Withholding (预缴) [T2]
**Situation:** General contractor provides construction services in a different province/city from their registration.
**Resolution:** Must pre-pay 2% VAT (general method) or 3% (simplified method) to the local tax authority where the project is located. Offset against home-jurisdiction VAT payable.
**Legislation:** Caishui [2016] No. 36; STA Announcement [2016] No. 17.

### EC6 -- Used Assets Sale by General Taxpayer [T1]
**Situation:** General taxpayer sells used fixed assets.
**Resolution:** If input VAT was previously credited — standard 13% output VAT. If input VAT was NOT credited (e.g., purchased before VAT reform) — simplified method at 3% reduced by 50% (effective 2%). Issue general fapiao (may issue special fapiao if buyer requests and taxpayer opts for standard rate).
**Legislation:** Caishui [2009] No. 9; Caishui [2014] No. 57.

### EC7 -- Free Samples and Gifts [T1]
**Situation:** Entity provides free product samples or gifts to customers/prospects.
**Resolution:** Deemed sale (视同销售). Output VAT must be computed on fair market value. Input VAT on the manufactured/purchased goods remains deductible.
**Legislation:** Provisional Regulations Implementation Rules Art. 4(8).

### EC8 -- Government Subsidies [T1]
**Situation:** Entity receives government subsidies or grants.
**Resolution:** If the subsidy is linked to specific goods/services (price subsidy), it forms part of the sales amount and is subject to VAT. If the subsidy is a general operational grant not linked to specific transactions, it is outside the scope of VAT.
**Legislation:** STA Announcement [2019] No. 45, Art. 7.

### EC9 -- Difference Method (差额征税) [T2]
**Situation:** Certain industries (tourism, labour dispatch, HRM outsourcing, financial services) may compute VAT on the difference between sales and specified deductions.
**Resolution:** Deductible amounts must be supported by valid fapiao or other qualifying documents. Report on Schedule 3 of the VAT return. Flag for reviewer: verify eligibility for difference method.
**Legislation:** Caishui [2016] No. 36, Annex 2.

### EC10 -- Real Estate Developers -- Pre-Sale VAT [T2]
**Situation:** Developer receives pre-sale payments (预收款) before property delivery.
**Resolution:** Pre-pay VAT at 3% of pre-sale receipts. Full VAT (9%) calculated upon delivery. Pre-paid amount offset against final liability. Special fapiao issued only upon delivery.
**Legislation:** STA Announcement [2016] No. 18.

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Chinese tax adviser (注册税务师) must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax adviser. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard Domestic Sale, General Taxpayer, 13% Rate
**Input:** General taxpayer sells manufactured goods. Invoice: CNY 113,000 VAT-inclusive. Rate: 13%.
**Expected output:** Sales amount = CNY 100,000. Output VAT = CNY 13,000. Report on Main Form Line 1, Schedule 1 at 13%.

### Test 2 -- Construction Service, 9% Rate
**Input:** General taxpayer provides construction services. Invoice: CNY 218,000 VAT-inclusive. Rate: 9%.
**Expected output:** Sales amount = CNY 200,000. Output VAT = CNY 18,000. Report on Main Form Line 2, Schedule 1 at 9%.

### Test 3 -- IT Consulting Service, 6% Rate
**Input:** General taxpayer provides IT consulting. Invoice: CNY 106,000 VAT-inclusive. Rate: 6%.
**Expected output:** Sales amount = CNY 100,000. Output VAT = CNY 6,000. Report on Main Form Line 3, Schedule 1 at 6%.

### Test 4 -- Small-Scale Taxpayer, 1% Temporary Rate
**Input:** Small-scale taxpayer sells goods. Quarterly sales CNY 350,000 (VAT-inclusive). Rate: 1%.
**Expected output:** Sales amount = CNY 346,534.65. VAT = CNY 3,465.35. Not exempt (exceeds CNY 300,000 quarterly threshold).

### Test 5 -- Small-Scale Taxpayer, Exempt
**Input:** Small-scale taxpayer provides services. Quarterly sales CNY 280,000 (VAT-inclusive). Rate: 1%.
**Expected output:** VAT exempt (quarterly sales <= CNY 300,000). Report on exempt sales line.

### Test 6 -- Input VAT on Employee Air Travel
**Input:** General taxpayer. Employee air ticket: fare CNY 1,500 + fuel surcharge CNY 150. Domestic flight.
**Expected output:** Input VAT = (1,500 + 150) / (1 + 9%) x 9% = CNY 136.24. Report on Schedule 2.

### Test 7 -- Blocked Input -- Entertainment
**Input:** General taxpayer purchases catering services for client entertainment. Special fapiao: VAT CNY 600.
**Expected output:** Input VAT BLOCKED. CNY 600 is non-deductible. Catering services fall under blocked category (Art. 27(6)).

### Test 8 -- Deemed Sale -- Gift of Self-Produced Goods
**Input:** General taxpayer gifts self-produced goods (cost CNY 50,000, market value CNY 80,000) to a customer.
**Expected output:** Deemed sale at market value. Output VAT = CNY 80,000 x 13% = CNY 10,400. Input VAT on raw materials remains deductible.

---

## PROHIBITIONS [T1]

- NEVER allow small-scale taxpayers to claim input VAT credits (simplified method -- no input deduction)
- NEVER apply general taxpayer rates to small-scale taxpayer supplies (use collection rate)
- NEVER accept fapiao that has not been authenticated within 360 days for input credit
- NEVER ignore deemed sales rules for gifts, transfers, and self-use of goods
- NEVER apply export refund without verifying the HS-code-specific refund rate
- NEVER compute surcharges before computing the base VAT payable
- NEVER allow input VAT credit on loan interest, catering, entertainment, or resident daily services
- NEVER classify a mixed sale without confirming the entity's principal business registration
- NEVER file a return without reconciling fapiao records to the Golden Tax System data
- NEVER guess the export refund rate -- it must be looked up per HS code

---

## Step 16: VAT Compliance Calendar [T1]

### Monthly Filing Timeline (General Taxpayer)

| Day | Action |
|-----|--------|
| 1st of month | Prior month period closes; begin reconciling fapiao |
| 1st-10th | Authenticate/cross-check all received special VAT fapiao on the Comprehensive Service Platform |
| 1st-10th | Reconcile Golden Tax System output data with accounting records |
| 10th-14th | Prepare VAT return; review input/output; calculate surcharges |
| 15th | Filing and payment deadline (extended if holiday/weekend) |
| 15th | Submit VAT return via provincial Electronic Tax Bureau |
| 15th | Pay VAT via linked bank account or tax payment certificate |

### Quarterly Filing Timeline (Small-Scale Taxpayer)

| Day | Action |
|-----|--------|
| 1st of quarter-end+1 month | Prior quarter closes |
| 1st-10th | Reconcile all income, fapiao issued, exemptions |
| 10th-14th | Prepare return; determine if quarterly exemption applies (<=CNY 300,000) |
| 15th | Filing and payment deadline |

### Annual Obligations [T1]

| Obligation | Deadline | Notes |
|-----------|----------|-------|
| CIT annual filing | 31 May following year | Separate from VAT but reconcile revenue |
| Annual VAT summary reconciliation | Per STA directive | Not all provinces require formal reconciliation |
| Transfer pricing documentation | 30 June following year | For related-party transactions >threshold |
| Fapiao annual verification | Per local STA | Golden Tax System annual check |

---

## Step 17: Provincial Variations and Special Zones [T2]

### Free Trade Zones (FTZs) [T2]

| Zone | Special VAT Treatment |
|------|----------------------|
| Shanghai FTZ | Bonded zone rules; import VAT deferred until goods enter domestic market |
| Hainan Free Trade Port | Progressive zero-tariff list; import VAT exemptions on specified goods; cross-border service tax incentives |
| Guangdong, Fujian, Tianjin FTZs | Bonded warehouse treatment; simplified customs/VAT procedures |

**Flag for reviewer: FTZ VAT treatment varies by zone and activity. Verify with local STA office.**

### Special VAT Regions

| Region | Treatment |
|--------|-----------|
| Hong Kong SAR | Separate jurisdiction — no PRC VAT; goods crossing border are imports/exports |
| Macau SAR | Separate jurisdiction — no PRC VAT |
| Taiwan | Separate jurisdiction — not subject to PRC VAT |
| Bonded areas (保税区) | Import VAT deferred; goods consumed within bonded area may be exempt |

---

## Step 18: Common Fapiao Errors and Corrections [T1]

### Fapiao Error Types

| Error | Correction Method | Deadline |
|-------|------------------|----------|
| Wrong buyer name/TIN | Void and reissue (same month) or red-letter reversal (different month) | Within 360 days |
| Wrong amount | Void and reissue or red-letter + new fapiao | Within 360 days |
| Wrong tax rate | Red-letter reversal + new fapiao at correct rate | Immediately upon discovery |
| Duplicate issuance | Void the duplicate; retain records | Same month preferred |
| Lost fapiao (buyer copy) | Buyer requests copy from seller; use fapiao record + seller's accounting stub for credit | Report to STA if special fapiao |

### Fapiao Compliance Risks [T1]

| Risk | Consequence |
|------|------------|
| Issuing special fapiao without actual transaction (虚开发票) | Criminal offence: 2-7 years imprisonment; fines; loss of general taxpayer status |
| Accepting fraudulent fapiao for input credit | Input VAT reversed + penalties + potential criminal liability |
| Failing to issue fapiao when required | Administrative fine CNY 10,000-50,000; customer complaint mechanism |
| Hoarding blank fapiao (unused fapiao not returned) | Administrative fine; may trigger audit |

---

## Step 19: Industry-Specific VAT Rules [T2]

### Real Estate and Construction

| Item | Rate | Special Rules |
|------|------|---------------|
| Sale of commercial real estate (new) | 9% | General method for projects started after 30 Apr 2016 |
| Sale of commercial real estate (old) | 5% (simplified) | Projects started before 1 May 2016; may elect general method |
| Construction services (general method) | 9% | Standard input-output |
| Construction services (simplified) | 3% | For old projects or subcontracting |
| Property management services | 6% | Modern services category |
| Rental of immovable property (new) | 9% | General method |
| Rental of immovable property (old) | 5% (simplified) | Pre-May 2016 acquisitions |

### Financial Services

| Item | Rate | Special Rules |
|------|------|---------------|
| Loan interest income | 6% | Borrower's input VAT on interest is BLOCKED |
| Financial product transfer (trading gains) | 6% | Difference method (net gains taxable; losses carry within year) |
| Insurance services | 6% | Claims payments are not VAT deductible |
| Fund management fees | 6% | Standard treatment |
| Interbank lending (within qualified period) | Exempt | Per Caishui circulars |

### Technology and Software

| Item | Rate | Special Rules |
|------|------|---------------|
| Software products (embedded) | 13% | Excess VAT above 3% effective rate refundable (即征即退) for qualifying software enterprises |
| Software development services | 6% | Modern services |
| Technology transfer | Exempt | Approved by provincial science/technology authority |
| Technology licensing | 6% | Unless qualifying as exempt technology transfer |

**Flag for reviewer: industry-specific rules change frequently. Verify with STA announcements and local practice.**

---

## Step 20: Direct Tax Reference (Out of Scope) [T3]

This skill does NOT cover direct taxes. The following is reference only:

- **Corporate Income Tax (CIT):** Standard rate 25%. High/New Technology Enterprises: 15%. Small low-profit enterprises: effective rate ~5% on first CNY 3,000,000. Legislation: Enterprise Income Tax Law (2007, amended 2018).
- **Individual Income Tax (IIT):** Progressive rates 3-45% for comprehensive income. Legislation: Individual Income Tax Law (2018 amended).
- **Stamp Duty:** Various rates by contract/document type. Legislation: Stamp Duty Law (2022).

---

## Contribution Notes

This skill covers the PRC VAT framework as of early 2026. China's new VAT Law took effect on 1 January 2026, replacing the Provisional Regulations. Core rates (13/9/6/0%) remain unchanged. Small-scale taxpayer relief (1% rate, monthly exemption threshold of CNY 100,000) continues through 31 December 2027. Practitioners must monitor STA announcements and Implementation Regulations for changes under the new statutory framework.

**A skill may not be published without sign-off from a licensed practitioner (注册税务师 or 注册会计师) in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
