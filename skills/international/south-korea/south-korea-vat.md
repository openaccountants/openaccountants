---
name: south-korea-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a South Korea VAT return (부가가치세 신고서) for any business operator. Trigger on phrases like "prepare Korean VAT return", "Korean VAT", "HomeTax filing", "e-tax invoice", "전자세금계산서", "부가가치세", or any request involving South Korea VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete South Korea VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, simplified taxation thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any South Korea VAT-related work.
---

# South Korea VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Korea (Republic of Korea) |
| Jurisdiction Code | KR |
| Primary Legislation | VAT Act (부가가치세법, Act No. 11873, as amended) |
| Supporting Legislation | VAT Act Enforcement Decree (부가가치세법 시행령); Restriction of Special Taxation Act (조세특례제한법); Framework Act on National Taxes (국세기본법) |
| Tax Authority | National Tax Service (국세청, NTS) |
| Filing Portal | https://hometax.go.kr (HomeTax / 홈택스) |
| Standard VAT Rate | 10% (Article 30 VAT Act) |
| Currency | Korean Won (KRW) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: transaction classification, e-tax invoice requirements, standard/zero-rated determination, filing deadlines. Tier 2: simplified taxation eligibility, partial input tax apportionment, cross-border digital services. Tier 3: group VAT registration, special industry regimes, tax tribunal disputes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed tax practitioner (세무사/공인회계사) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed practitioner and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Business registration number (사업자등록번호)** [T1] -- 10-digit format (XXX-XX-XXXXX)
2. **Business type** [T1] -- General taxpayer (일반과세자), Simplified taxpayer (간이과세자), or Exempt business (면세사업자)
3. **VAT filing period** [T1] -- Period 1 (Jan-Jun) or Period 2 (Jul-Dec); preliminary returns within each period
4. **Industry/sector** [T2] -- impacts simplified taxation value-added ratios and special deductibility rules
5. **Does the business make exempt supplies?** [T2] -- If yes, partial input tax apportionment required (Article 40 VAT Act)
6. **Annual revenue** [T1] -- determines simplified taxation eligibility (< KRW 104 million; raised from KRW 80M effective July 2024)
7. **Does the business issue e-tax invoices (전자세금계산서)?** [T1] -- mandatory for all general taxpayers
8. **Does the business import goods?** [T1] -- customs VAT recovery rules apply
9. **Does the business provide cross-border digital services?** [T2] -- simplified registration for non-residents applies
10. **Prior period carried-forward refund amount** [T1] -- for offset against current period liability

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until business type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output VAT / 매출세액) or Purchase (input VAT / 매입세액)
- Salaries, loan repayments, dividends, income tax payments = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act Article 4 (taxable transactions), Article 9 (supply of goods), Article 11 (supply of services)

### 1b. Determine Counterparty Location [T1]

- Domestic (Korea): supplier/customer has Korean business registration
- Foreign: all non-Korean counterparties
- **Note:** For services received from abroad, reverse charge (대리납부) applies under Article 52
- **Legislation:** VAT Act Article 20 (place of supply for goods), Article 21 (place of supply for services)

### 1c. Determine Supply Type [T1]

| Supply Type | VAT Treatment | Legislation |
|------------|---------------|-------------|
| Standard domestic supply of goods | 10% | Article 30(1) |
| Standard domestic supply of services | 10% | Article 30(1) |
| Export of goods | 0% (zero-rated) | Article 24(1)1 |
| Services to non-residents earning foreign currency | 0% (zero-rated) | Article 24(1)2 |
| International transportation | 0% (zero-rated) | Article 24(1)3 |
| Exempt supply | Exempt (no VAT) | Article 26 |
| Deemed supply (self-use, gifts) | 10% on market value | Article 10 |

### 1d. Determine Expense Category [T1]

- Capital asset (감가상각자산): assets subject to depreciation per Corporate Tax Act / Income Tax Act
- Inventory for resale (재화): goods purchased for direct resale
- Overhead / operating expense (일반경비): all other business expenses
- **Legislation:** VAT Act Article 39 (non-deductible input tax), Enforcement Decree Article 80

---

## Step 2: VAT Return Form Structure (일반과세자 부가가치세 신고서) [T1]

**Legislation:** VAT Act Article 49 (filing of return); NTS prescribed return form.

### Section 1: Output Tax (매출세액)

| Line | Description | Classification |
|------|-------------|----------------|
| Line 1 | Tax invoices issued -- taxable sales (세금계산서 발급분) | Domestic B2B sales with e-tax invoice |
| Line 2 | Tax invoices issued -- zero-rated sales (영세율 세금계산서 발급분) | Zero-rated B2B with e-tax invoice |
| Line 3 | Credit card / cash receipt sales (신용카드·현금영수증 발행분) | B2C sales via card/cash receipt |
| Line 4 | Other sales (기타 매출) | Sales without tax invoice (rare, penalty risk) |
| Line 5 | Total taxable supply value (과세표준) | Sum of Lines 1-4 |
| Line 6 | Output tax (매출세액) | Line 5 x 10% (adjusted for zero-rated) |

### Section 2: Zero-Rated Sales Detail (영세율 매출명세)

| Line | Description | Classification |
|------|-------------|----------------|
| Line 7 | Direct exports (직접수출) | FOB value of exported goods |
| Line 8 | Intermediary trade (중계무역) | Re-export / entrepot trade |
| Line 9 | Deemed exports (내국신용장·구매확인서) | Local letter of credit / purchase confirmation |
| Line 10 | Foreign currency earning services (외화획득 용역) | Services to non-residents |
| Line 11 | Other zero-rated (기타 영세율) | Other qualifying zero-rated supplies |

### Section 3: Input Tax (매입세액)

| Line | Description | Classification |
|------|-------------|----------------|
| Line 12 | Tax invoices received (세금계산서 수취분) | Domestic purchases with valid e-tax invoice |
| Line 13 | Fixed assets (고정자산 매입) | Capital asset purchases (subset of Line 12) |
| Line 14 | Non-tax-invoice purchases (기타 공제매입세액) | Credit card, cash receipt purchases eligible for input |
| Line 15 | Total input tax (매입세액 합계) | Sum of Lines 12-14 |

### Section 4: Tax Calculation (세액계산)

| Line | Description | Calculation |
|------|-------------|-------------|
| Line 16 | Net tax (차감세액) | Line 6 - Line 15 |
| Line 17 | Adjustments (가감조정세액) | Credit note adjustments, bad debt relief |
| Line 18 | Preliminary payment credit (예정신고 미환급세액) | Credit from preliminary return |
| Line 19 | Carried-forward credit (전기 미환급세액) | Refund carried from prior period |
| Line 20 | Tax payable / refundable (납부(환급)세액) | Line 16 +/- Line 17 - Line 18 - Line 19 |

---

## Step 3: E-Tax Invoice Requirements (전자세금계산서) [T1]

**Legislation:** VAT Act Article 32 (tax invoices), Article 36 (electronic tax invoices).

### Mandatory E-Tax Invoice Issuance

| Business Type | Requirement | Effective |
|--------------|-------------|-----------|
| All corporations | Mandatory e-tax invoice | Since 2011 |
| Individual general taxpayer (revenue >= KRW 80M) | Mandatory e-tax invoice | Since July 2024 (previously KRW 100M since July 2023) |
| Individual general taxpayer (revenue < KRW 80M) | Voluntary (paper permitted) | Current |
| Simplified taxpayer | Not applicable (no tax invoices issued) | Current |

### E-Tax Invoice Content Requirements [T1]

Every e-tax invoice must contain (Article 32(1)):
1. Business registration number of supplier and recipient
2. Name or trade name of supplier
3. Date of supply
4. Description and quantity of goods/services
5. Supply value (공급가액) and VAT amount (세액)
6. Transmission to NTS within one day of issuance

### Penalties for Non-Compliance [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Failure to issue tax invoice | 2% of supply value (additional tax) | Article 60(2) |
| Late issuance of e-tax invoice | 1% of supply value | Article 60(3) |
| Failure to transmit to NTS | 0.5% of supply value | Article 60(5) |
| Receipt of false tax invoice | 2% of supply value (input denied) | Article 60(4) |
| Failure to issue e-tax invoice (when mandatory) | 2% of supply value | Article 60(2) |

---

## Step 4: VAT Rate Classification Matrix [T1]

**Legislation:** VAT Act Articles 24-28.

### Standard Rate (10%)

| Category | Examples | Article |
|----------|----------|---------|
| Domestic goods supply | Sale of manufactured goods, retail | Art. 30(1) |
| Domestic services supply | Professional services, consulting, IT | Art. 30(1) |
| Import of goods | Customs value + duties | Art. 30(2) |
| Deemed supply | Self-use of business goods, employee gifts | Art. 10 |

### Zero-Rated (0%)

| Category | Examples | Article |
|----------|----------|---------|
| Export of goods | FOB export, bonded area supply | Art. 24(1)1 |
| Services earning foreign currency | IT outsourcing to foreign client | Art. 24(1)2 |
| International transportation | Shipping, air cargo | Art. 24(1)3 |
| Goods/services to foreign diplomats | Embassy supplies | Art. 24(1)4 |
| Local letter of credit supplies | Deemed export (내국신용장) | Art. 24(2) |

### Exempt Supplies (면세)

| Category | Examples | Article |
|----------|----------|---------|
| Unprocessed foodstuffs | Rice, vegetables, fresh fish, livestock | Art. 26(1)1 |
| Medical / health services | Hospital services, pharmacy (prescription) | Art. 26(1)5 |
| Education services | Schools, academies (accredited) | Art. 26(1)6 |
| Financial / insurance services | Banking, insurance premiums, securities | Art. 26(1)11 |
| Books / newspapers | Physical publications, e-books (since 2019) | Art. 26(1)8 |
| Residential rental | Lease of residential property (국민주택 규모 이하) | Art. 26(1)12 |
| Public transportation | City bus, subway, rural bus | Art. 26(1)7 |
| Stamp / postal services | Korea Post services | Art. 26(1)9 |
| Religious / charitable activities | Church, temple, NGO services | Art. 26(1)18 |

---

## Step 5: Blocked Input Tax (매입세액 불공제) [T1]

**Legislation:** VAT Act Article 39 (non-deductible input tax).

### Categories Where Input VAT is NOT Recoverable

| Blocked Category | Description | Article |
|-----------------|-------------|---------|
| Non-business expenses | Expenses not related to business operations | Art. 39(1)1 |
| Entertainment expenses (접대비) | Client entertainment, gifts to clients | Art. 39(1)4 |
| Non-business vehicles (비영업용 소형승용차) | All non-business passenger cars regardless of engine size | Art. 39(1)5 |
| Vehicle maintenance for blocked vehicles | Fuel, repair, insurance for non-business vehicles | Art. 39(1)5 |
| Purchases without proper tax invoice | Missing or incomplete tax invoices | Art. 39(1)2 |
| Input tax on exempt supplies | Purchases directly attributable to exempt supplies | Art. 39(1)7 |
| Employee personal expenses | Personal consumption by employees | Art. 39(1)1 |
| Land-related input tax | Acquisition and capital expenditure on land | Art. 39(1)6 |

### Exceptions to Vehicle Block [T1]

Input VAT IS recoverable for vehicles used in these business categories (Enforcement Decree Art. 80):
- Taxi / rental car operators
- Driving schools
- Freight transport businesses
- Vehicle sales / repair businesses
- Funeral service vehicles (hearse)

**Blocked categories OVERRIDE partial exemption. Check blocked status FIRST, then apply partial exemption if relevant.**

---

## Step 6: Simplified Taxation Regime (간이과세) [T1]

**Legislation:** VAT Act Articles 61-68 (simplified taxation).

### Eligibility [T1]

| Criterion | Threshold | Article |
|-----------|-----------|---------|
| Annual revenue | < KRW 104,000,000 (KRW 104 million) since July 2024 (previously KRW 80M) | Art. 61(1), as amended |
| Excluded businesses | Real estate rental and taxable entertainment venues: threshold remains < KRW 48M | Art. 61(2) |
| Newly registered | Eligible if expected revenue < KRW 104M | Enforcement Decree Art. 109 |

### How Simplified Tax Works [T1]

| Element | General Taxpayer | Simplified Taxpayer |
|---------|-----------------|---------------------|
| Output tax calculation | Supply value x 10% | Supply value x industry ratio x 10% |
| Input tax deduction | Full input tax from invoices | Supply value of purchases x 0.5% |
| Tax invoice issuance | Mandatory (e-tax invoice) | Cannot issue tax invoices (issue receipt only) |
| Filing frequency | Quarterly (with preliminary) | Semi-annual (Jan-Jun, Jul-Dec) |
| VAT exemption | Not applicable | If revenue < KRW 48M, exempt from VAT payment (unchanged) |

### Industry Value-Added Ratios (업종별 부가가치율) [T1]

| Industry | Ratio | Effective Rate |
|----------|-------|---------------|
| Retail / wholesale | 15% | 1.5% |
| Manufacturing | 20% | 2.0% |
| Agriculture / fishery | 10% | 1.0% |
| Food & beverage (restaurant) | 40% | 4.0% |
| Accommodation | 30% | 3.0% |
| Transportation | 40% | 4.0% |
| Construction | 30% | 3.0% |
| Other services | 30% | 3.0% |
| Real estate rental | 40% | 4.0% |
| Professional / technical services | 40% | 4.0% |

**Legislation:** VAT Act Article 62, Enforcement Decree Article 111.

---

## Step 7: Registration Rules [T1]

**Legislation:** VAT Act Articles 5-8 (registration).

### Who Must Register

| Category | Requirement | Article |
|----------|-------------|---------|
| All business operators (사업자) | Must register before commencing business | Art. 5(1) |
| Corporations | Always general taxpayer | Art. 5 |
| Individuals < KRW 104M revenue | May register as simplified taxpayer | Art. 61 |
| Non-resident digital service providers | Simplified registration via NTS | Art. 53-2 |
| Exempt-only businesses | Register as exempt business operator (면세사업자) | Art. 26 |

### Registration Process [T1]

1. Apply via HomeTax (온라인) or visit local tax office (세무서)
2. Receive business registration certificate (사업자등록증) within 3 days
3. Registration number format: XXX-XX-XXXXX (3-2-5 digits)
4. Late registration penalty: 1% of revenue from start of business to registration date (Art. 60(1))

### Cancellation of Registration [T1]

- Business closure: must file final return within 25 days of closure (Article 49(3))
- Failure to file closure return: penalties apply under Framework Act on National Taxes

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** VAT Act Article 49 (filing), Article 48 (preliminary return), Framework Act on National Taxes Articles 47-47-5.

### Filing Calendar -- General Taxpayer

| Period | Type | Covers | Deadline |
|--------|------|--------|----------|
| Period 1 Preliminary | Preliminary return | Jan 1 - Mar 31 | April 25 |
| Period 1 Final | Confirmed return | Jan 1 - Jun 30 | July 25 |
| Period 2 Preliminary | Preliminary return | Jul 1 - Sep 30 | October 25 |
| Period 2 Final | Confirmed return | Jul 1 - Dec 31 | January 25 (following year) |

### Filing Calendar -- Simplified Taxpayer

| Period | Type | Covers | Deadline |
|--------|------|--------|----------|
| Period 1 | Semi-annual return | Jan 1 - Jun 30 | July 25 |
| Period 2 | Semi-annual return | Jul 1 - Dec 31 | January 25 (following year) |

### Penalty Structure [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing | Greater of: (a) 20% of unpaid tax or (b) Revenue x 0.07% | Framework Act Art. 47-2 |
| Failure to file | 20% of tax due (general) / 40% (fraudulent) | Framework Act Art. 47-2 |
| Late payment | 0.022% per day of unpaid tax (approx. 8% per annum) | Framework Act Art. 47-4 |
| Underreporting (general) | 10% of understated tax | Framework Act Art. 47-3 |
| Underreporting (fraudulent) | 40% of understated tax | Framework Act Art. 47-3 |
| Failure to issue tax invoice | 2% of supply value | VAT Act Art. 60(2) |
| False tax invoice (issued/received) | 3% of supply value + criminal penalty risk | VAT Act Art. 60(4) |

---

## Step 9: Reverse Charge for Imported Services (대리납부) [T1]

**Legislation:** VAT Act Article 52 (reverse charge on foreign services).

### When Reverse Charge Applies [T1]

| Scenario | Reverse Charge? | Treatment |
|----------|----------------|-----------|
| Korean business receives services from non-resident with no Korean PE | Yes | Recipient self-assesses and pays VAT to NTS |
| Korean business imports goods | No | VAT collected by Customs at import |
| Korean consumer receives digital services from non-resident | No (supplier registered) | Non-resident supplier charges and remits VAT |
| Korean business purchases from Korean-registered foreign supplier | No | Normal domestic transaction |

### Reverse Charge Mechanics [T1]

1. Recipient calculates VAT at 10% on the service fee
2. Report on VAT return as both output tax (additional) and input tax (deductible)
3. Net effect: zero for fully taxable businesses
4. File and pay via HomeTax by the 25th of the month following the quarter end
5. If business makes exempt supplies, input tax from reverse charge is subject to partial apportionment

### Non-Resident Digital Services (Article 53-2) [T1]

| Element | Rule |
|---------|------|
| Who must register | Non-resident providers of electronic services to Korean consumers (B2C) |
| Registration method | Simplified registration via NTS |
| Filing | Quarterly, by 25th of month following quarter end |
| Input tax deduction | NOT available under simplified registration |
| Examples | App stores, streaming services, cloud computing, online advertising |

---

## Step 10: Partial Input Tax Apportionment (공통매입세액 안분) [T2]

**Legislation:** VAT Act Article 40 (common input tax apportionment).

### When Apportionment Applies [T2]

If a business makes BOTH taxable and exempt supplies, input tax on common expenses must be apportioned:

```
Deductible Input Tax = Total Common Input Tax x (Taxable Supply Value / Total Supply Value)
```

### Apportionment Rules [T2]

| Rule | Detail | Article |
|------|--------|---------|
| Calculation basis | Supply values for the relevant tax period | Art. 40(1) |
| Annual adjustment | Reconcile at year-end based on total annual supply values | Art. 40(2) |
| De minimis | If exempt supplies < 5% of total, full input tax deductible | Enforcement Decree Art. 81 |
| Direct attribution | Input tax directly attributable to taxable supplies: fully deductible | Art. 40(1) |
| Direct attribution | Input tax directly attributable to exempt supplies: fully blocked | Art. 40(1) |

**Flag for reviewer: apportionment ratios must be confirmed by licensed practitioner before filing. Annual adjustment may result in additional tax payable or refundable.**

---

## Step 11: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions.

### EC1 -- Credit card purchases without e-tax invoice [T1]
**Situation:** Employee makes business purchase using corporate credit card. No e-tax invoice obtained.
**Resolution:** Input VAT is still recoverable via credit card sales slip (신용카드매출전표). Report on Line 14 (non-tax-invoice purchases). However, recovery is limited to business-related expenses. Entertainment expenses remain blocked regardless.
**Legislation:** VAT Act Article 46(1), Enforcement Decree Article 87.

### EC2 -- Mixed-use vehicle (business and personal) [T2]
**Situation:** Owner uses passenger vehicle for both business and personal purposes.
**Resolution:** If the vehicle is a non-business small passenger car (비영업용 소형승용차), ALL input VAT is blocked, including fuel and maintenance. No apportionment is allowed for non-business vehicles. Exception: if the vehicle is used exclusively for business in a qualifying industry (taxi, rental, etc.), full recovery applies. Flag for reviewer: confirm vehicle type and exclusive business use.
**Legislation:** VAT Act Article 39(1)5, Enforcement Decree Article 80.

### EC3 -- Local letter of credit (내국신용장) supply [T1]
**Situation:** Korean manufacturer supplies goods to another Korean company under a local letter of credit for eventual export.
**Resolution:** Zero-rated under Article 24(2). Report on Line 9 (deemed exports). Supplier must retain the purchase confirmation document (구매확인서) issued by the bank.
**Legislation:** VAT Act Article 24(2), Enforcement Decree Article 33.

### EC4 -- Bad debt relief (대손세액공제) [T1]
**Situation:** Customer fails to pay invoice including VAT. Debt is written off.
**Resolution:** Output VAT previously reported can be recovered as a deduction in the period the debt is confirmed irrecoverable. Claim on Line 17 (adjustments). Conditions: debt must be legally irrecoverable (bankruptcy, statute of limitations, etc.); claim within 5 years of original supply.
**Legislation:** VAT Act Article 45.

### EC5 -- Free samples and promotional gifts [T1]
**Situation:** Business distributes free product samples at a trade show.
**Resolution:** Deemed supply under Article 10(1). Output VAT must be charged on the market value of the goods. However, if the samples are of minimal value and distributed for advertising purposes, they may be excluded from deemed supply under Enforcement Decree Article 17.
**Legislation:** VAT Act Article 10(1), Enforcement Decree Article 17.

### EC6 -- Cross-border digital services (B2B) [T1]
**Situation:** Korean company subscribes to a US SaaS platform (e.g., AWS, Salesforce).
**Resolution:** Reverse charge applies. Korean company self-assesses VAT at 10%. Report as both output and input tax. Net effect zero for fully taxable businesses. Must retain foreign invoice as supporting document.
**Legislation:** VAT Act Article 52.

### EC7 -- Import of goods with customs VAT [T1]
**Situation:** Business imports machinery from Germany. Customs collects VAT at import.
**Resolution:** VAT paid at customs is recoverable as input tax. Report on Line 12 using the import tax invoice (수입세금계산서) issued by customs. The customs declaration (수입신고필증) serves as the supporting document.
**Legislation:** VAT Act Article 38(1)2.

### EC8 -- Goods supplied to foreign diplomats [T1]
**Situation:** Business sells goods to a foreign embassy in Seoul.
**Resolution:** Zero-rated under Article 24(1)4. Must obtain diplomatic purchase certificate. Report on Line 11 (other zero-rated).
**Legislation:** VAT Act Article 24(1)4, Enforcement Decree Article 35.

### EC9 -- Real estate lease (commercial vs. residential) [T2]
**Situation:** Client leases property. Need to determine VAT treatment.
**Resolution:** Commercial property lease: standard 10% VAT applies. Residential property lease (국민주택 규모 이하, 85 sqm or less): exempt under Article 26. If property is mixed-use (commercial ground floor, residential upper floors), split by area. Flag for reviewer: confirm property classification and area measurements.
**Legislation:** VAT Act Article 26(1)12, Enforcement Decree Article 44.

### EC10 -- Pre-registration input tax [T2]
**Situation:** Business incurred expenses before completing VAT registration.
**Resolution:** Input VAT on purchases made up to 20 days before the registration date is recoverable, provided valid tax invoices exist. Beyond 20 days, input tax is not recoverable. Flag for reviewer: verify dates and confirm tax invoice validity.
**Legislation:** VAT Act Article 39(1)8, Enforcement Decree Article 82.

### EC11 -- Correction of previously filed return (수정신고) [T1]
**Situation:** Error discovered in a previously filed VAT return.
**Resolution:** File an amended return (수정신고) via HomeTax. If the correction results in additional tax, underreporting penalty applies (10% general, 40% fraudulent). If the taxpayer voluntarily corrects before NTS audit notice, reduced penalties apply (50-90% reduction depending on timing).
**Legislation:** Framework Act on National Taxes Article 45, Article 47-3.

### EC12 -- Entertainment expenses classification [T1]
**Situation:** Client dinner with business partner at a restaurant.
**Resolution:** Classified as entertainment (접대비). Input VAT is BLOCKED under Article 39(1)4, regardless of business purpose. This is absolute -- no exceptions. The expense is deductible for income/corporate tax purposes (subject to limits), but the VAT component is never recoverable.
**Legislation:** VAT Act Article 39(1)4.

---

## Step 12: Comparison with EU VAT System

| Feature | South Korea VAT | EU VAT (Directive 2006/112/EC) |
|---------|----------------|-------------------------------|
| Standard rate | 10% (single rate) | Varies 17-27% by member state |
| Reduced rates | None (only standard + zero + exempt) | Multiple reduced rates allowed |
| Zero-rating | Exports, foreign currency services | Exports + member state options |
| Registration threshold | All business operators must register | Varies by member state (up to EUR 85,000) |
| Filing frequency | Quarterly (with preliminary) | Monthly/quarterly/annually varies |
| Invoice system | Mandatory e-tax invoice via HomeTax | E-invoicing varies; ViDA proposal pending |
| Reverse charge (imports) | Services only; goods via customs | Services + intra-community goods |
| Simplified regime | < KRW 104M, reduced rates by industry | Small enterprise exemption varies |
| Input tax blocking | Entertainment, non-business vehicles, land | Varies by member state |
| Group registration | Available (limited) | Available in most member states |
| Bad debt relief | Available (5-year limit) | Available (conditions vary) |
| Digital services B2C | Non-resident simplified registration | OSS (One Stop Shop) |

---

## Step 13: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic sale [T1]
**Input:** Korean general taxpayer sells goods to Korean customer, supply value KRW 10,000,000.
**Expected output:** Line 1 = KRW 10,000,000, Output tax = KRW 1,000,000. E-tax invoice issued and transmitted to NTS.

### Test 2 -- Export sale, zero-rated [T1]
**Input:** Korean manufacturer exports goods FOB value KRW 50,000,000 to US buyer.
**Expected output:** Line 2 = KRW 50,000,000 (zero-rated), Line 7 = KRW 50,000,000 (direct export detail). Output tax = KRW 0. Export declaration retained.

### Test 3 -- Domestic purchase with e-tax invoice [T1]
**Input:** General taxpayer purchases office supplies KRW 2,200,000 (VAT inclusive), supply value KRW 2,000,000, VAT KRW 200,000.
**Expected output:** Line 12 = KRW 2,000,000, Input tax = KRW 200,000. Full recovery (not blocked category).

### Test 4 -- Entertainment expense, input blocked [T1]
**Input:** General taxpayer pays KRW 550,000 (VAT inclusive) for client dinner. Supply value KRW 500,000, VAT KRW 50,000.
**Expected output:** Line 12 = KRW 500,000 (reported), but Input tax = KRW 0 (BLOCKED under Article 39(1)4). VAT is irrecoverable cost.

### Test 5 -- Non-business vehicle purchase [T1]
**Input:** General taxpayer purchases sedan for owner, KRW 44,000,000 (VAT inclusive), supply value KRW 40,000,000, VAT KRW 4,000,000.
**Expected output:** Input tax = KRW 0. BLOCKED under Article 39(1)5. Entire KRW 44,000,000 is cost.

### Test 6 -- Reverse charge on imported services [T1]
**Input:** Korean company pays USD 10,000 (KRW 13,000,000 equivalent) to US law firm for legal advisory. No Korean VAT charged.
**Expected output:** Self-assess output VAT KRW 1,300,000. Claim input VAT KRW 1,300,000. Net effect = zero. Report on return as reverse charge adjustment.

### Test 7 -- Simplified taxpayer, retail [T1]
**Input:** Simplified taxpayer (retail shop), quarterly revenue KRW 15,000,000.
**Expected output:** Tax = KRW 15,000,000 x 15% (retail ratio) x 10% = KRW 225,000. Input deduction = purchases x 0.5%.

### Test 8 -- Credit card purchase, no tax invoice [T1]
**Input:** Employee uses corporate card for KRW 330,000 office supplies (VAT inclusive). No e-tax invoice obtained.
**Expected output:** Line 14 = KRW 300,000. Input tax = KRW 30,000 (recoverable via credit card slip). Retain card statement.

### Test 9 -- Local letter of credit (deemed export) [T1]
**Input:** Manufacturer supplies components worth KRW 20,000,000 under local L/C to exporter.
**Expected output:** Line 2 = KRW 20,000,000 (zero-rated). Line 9 = KRW 20,000,000. Output tax = KRW 0. Purchase confirmation retained.

### Test 10 -- Bad debt recovery [T1]
**Input:** Customer went bankrupt. Original invoice KRW 11,000,000 (supply KRW 10,000,000, VAT KRW 1,000,000). Court confirms irrecoverable.
**Expected output:** Line 17 adjustment = negative KRW 1,000,000 (bad debt VAT recovery). Retain court documentation.

### Test 11 -- Import of goods with customs VAT [T1]
**Input:** Import machinery from Japan, customs value KRW 100,000,000. Customs VAT = KRW 10,000,000. Import tax invoice received.
**Expected output:** Line 12 = KRW 100,000,000. Line 13 = KRW 100,000,000 (fixed asset). Input tax = KRW 10,000,000 (fully recoverable). Customs declaration retained.

### Test 12 -- Partial exemption business [T2]
**Input:** Financial advisory firm (60% taxable, 40% exempt). Common overhead purchase KRW 5,500,000 (VAT KRW 500,000).
**Expected output:** Recoverable input tax = KRW 500,000 x 60% = KRW 300,000. Flag for reviewer: confirm apportionment ratio and annual adjustment requirement.

---

## PROHIBITIONS [T1]

- NEVER classify entertainment expenses as deductible input tax -- they are ALWAYS blocked under Article 39(1)4
- NEVER allow input VAT recovery on non-business passenger vehicles or their running costs (Article 39(1)5)
- NEVER allow a simplified taxpayer to issue tax invoices (세금계산서) -- they may only issue receipts
- NEVER apply reverse charge to imports of physical goods -- customs collects VAT at the border
- NEVER allow input VAT recovery without a valid tax invoice, credit card slip, or customs import document
- NEVER file a VAT return without confirming the client's business type (general vs. simplified vs. exempt)
- NEVER ignore the e-tax invoice transmission requirement -- must transmit to NTS within 1 day of issuance
- NEVER allow input VAT on land acquisition costs (Article 39(1)6)
- NEVER confuse zero-rated (exports, input tax deductible) with exempt (no output tax, input tax NOT deductible on attributable purchases)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER allow pre-registration input tax beyond the 20-day lookback window
- NEVER allow bad debt relief beyond the 5-year statutory limit

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is considered most likely correct and why]
Action Required: Licensed tax practitioner (세무사/공인회계사) must confirm before filing.
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

This skill covers the standard VAT return for general taxpayers (일반과세자) and simplified taxpayers (간이과세자) in South Korea. It does not cover:

- Corporate income tax or individual income tax computation [T3]
- Customs duties (beyond VAT at import) [T3]
- Special consumption tax (개별소비세) [T3]
- Local taxes (지방세) [T3]
- Group VAT registration mechanics [T3]
- Transfer pricing implications on intercompany supplies [T3]

**A skill may not be published without sign-off from a licensed practitioner (세무사 or 공인회계사) in South Korea.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
