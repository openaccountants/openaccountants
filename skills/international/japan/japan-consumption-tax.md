---
name: japan-consumption-tax
description: Use this skill whenever asked to prepare, review, or create a Japan Consumption Tax (JCT) return, classify transactions for JCT purposes, handle Qualified Invoice System (QIS) compliance, or advise on JCT registration, filing, and reporting. Trigger on phrases like "prepare consumption tax return", "JCT return", "shouhizei", "qualified invoice", "tekikaku invoice", "e-Tax filing", "JCT classification", or any request involving Japan consumption tax. Also trigger when classifying transactions from bank statements, invoices, or other source data for JCT purposes. This skill contains the complete JCT classification rules, return form mappings, input tax credit rules, QIS requirements, reverse charge treatment, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any JCT-related work.
---

# Japan Consumption Tax (JCT) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | Consumption Tax Act (Act No. 108 of 1988, as amended) |
| Supporting Legislation | Local Tax Act (chihou-zei-hou); Act on Special Measures Concerning Taxation (Sozei Tokubetsu Sochi Hou); Cabinet Order for Enforcement of Consumption Tax Act; Qualified Invoice Retention Method (Article 57-2 to 57-4, Consumption Tax Act) |
| Tax Authority | National Tax Agency (NTA / Kokuzei-cho) |
| Filing Portal | e-Tax (https://www.e-tax.nta.go.jp) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, return form box assignment, QIS invoice requirements, basic input credit rules, derived calculations. Tier 2: partial credit under 95% rule, proportional division methods, transitional credit calculations, industry-specific classifications. Tier 3: complex group reorganisations, consolidated filing, cross-border PE structures, transfer pricing adjustments on intercompany services. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified tax accountant (zeirishi) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and corporate number (houjin bangou)** [T1] -- 13-digit corporate number (T + 13 digits for QIS registration number)
2. **QIS registration number (tekikaku seikyuusho hakkou jigyousha touroku bangou)** [T1] -- format T + 13 digits; required from 1 October 2023 to issue qualified invoices
3. **Taxable status** [T1] -- Taxable business operator (kazei jigyousha) or Tax-exempt business operator (menzei jigyousha)
4. **Fiscal year end** [T1] -- determines filing period and deadlines
5. **Base period taxable sales (kijun kikan)** [T1] -- taxable sales in the base period (two fiscal years prior for corporations); determines taxable status (JPY 10M threshold)
6. **Specified period taxable sales** [T1] -- first six months of prior fiscal year; alternative threshold test
7. **Does the business make both taxable and exempt supplies?** [T2] -- if yes, proportional input credit calculation required (95% rule or individual/lump-sum/proportional method)
8. **Total taxable sales in current period** [T2] -- needed to determine if 95% rule applies (threshold: JPY 500M)
9. **Filing frequency** [T1] -- annual (default), quarterly (if elected or required), or monthly (if elected or required)
10. **Industry sector** [T2] -- impacts simplified tax calculation method (kantanni kazei) category selection

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and taxable period are confirmed.**

---

## Step 1: Tax Rate Classification

### 1a. Standard Rate [T1]

**Rate: 10% (national 7.8% + local 2.2%)**

Applies to all taxable supplies of goods and services in Japan unless the reduced rate applies.

**Legislation:** Consumption Tax Act, Article 29 (national rate); Local Tax Act, Article 72-78 (local consumption tax rate = 22/78 of national consumption tax).

### 1b. Reduced Rate [T1]

**Rate: 8% (national 6.24% + local 1.76%)**

Applies to:
1. **Food and beverages** -- excluding alcoholic beverages (as defined under the Liquor Tax Act) and excluding food service (eating in at restaurants, catering services with serving staff). Take-out and delivery are reduced rate.
2. **Newspaper subscriptions** -- newspapers published at least twice per week under a subscription contract (teiki koudoku keiyaku). Single-copy purchases and digital newspaper subscriptions are standard rate.

**Legislation:** Consumption Tax Act, Article 29, Appended Table 1; Act on Special Measures Concerning Taxation, Article 86-6.

### 1c. Zero Rate (Export Exemption) [T1]

**Rate: 0%**

Applies to:
- Export of goods from Japan (Consumption Tax Act, Article 7)
- International transport services
- Services provided to non-residents consumed entirely outside Japan
- Sale of goods in bonded areas for export

Zero-rated supplies allow full input tax credit recovery.

**Legislation:** Consumption Tax Act, Article 7 (export exemption); Article 7(1)(i)-(v).

### 1d. Non-Taxable Transactions [T1]

The following are outside the scope of JCT entirely:
- Transactions without consideration (gifts, donations -- unless deemed supply)
- Transactions outside Japan (place of supply rules)
- Salary and wages
- Dividends
- Share transfers as capital transactions
- Insurance claim receipts

**Legislation:** Consumption Tax Act, Article 4 (taxable transactions defined as domestic supply of goods/services for consideration by a business operator in the course of business).

### 1e. Exempt Transactions (Non-Taxable Supplies / Hi-kazei Torihiki) [T1]

The following are exempt from JCT (no tax charged, and input credits NOT available for attributable inputs):
- Sale or lease of land
- Sale of securities and payment instruments
- Interest, insurance premiums, and guarantee fees
- Postage stamps and revenue stamps (when sold at face value by designated sellers)
- Fees charged by national/local governments for administrative services
- International money transfers
- Medical services covered by public health insurance
- Certain educational services (school tuition at recognised institutions)
- Rental of residential property
- Funeral/cremation services provided by local government
- Childbirth-related services covered by public insurance

**Legislation:** Consumption Tax Act, Article 6; Appended Table 1 (exempt supplies list).

---

## Step 2: Consumption Tax Return Form Structure [T1]

### 2a. General Filing (Standard Method / Ippan Kazei)

The JCT return (shouhizei oyobi chihou shouhizei no shinkoku-sho) consists of Form 1 (general) or Form 1 (simplified), plus Appendix 1 and Appendix 2. The key fields for the general method are:

**Legislation:** Consumption Tax Act, Article 45 (obligation to file return); NTA prescribed return forms.

#### Output Tax Section (Sales / Uriage)

| Line | Description | Rate | Notes |
|------|-------------|------|-------|
| Line 1 | Taxable sales amount (tax-included basis, 10%) | 10% | Total consideration received for standard-rated supplies |
| Line 2 | Taxable sales amount (tax-included basis, 8%) | 8% | Total consideration for reduced-rated supplies |
| Line 3 | Tax amount on Line 1 sales | 10% | Line 1 x 7.8/110 (national portion) |
| Line 4 | Tax amount on Line 2 sales | 8% | Line 2 x 6.24/108 (national portion) |
| Line 5 | Consumption tax on taxable sales (Line 3 + Line 4) | -- | Sum of national consumption tax on output |
| Line 6 | Sales returns and allowances (tax amount, 10%) | 10% | Credit notes / returns at standard rate |
| Line 7 | Sales returns and allowances (tax amount, 8%) | 8% | Credit notes / returns at reduced rate |
| Line 8 | Net output tax (Line 5 - Line 6 - Line 7) | -- | Net national consumption tax on output |
| Line 9 | Taxable sales for export / zero-rated | 0% | Export sales and qualifying zero-rated supplies |

#### Input Tax Credit Section (Purchases / Shiire)

| Line | Description | Notes |
|------|-------------|-------|
| Line 10 | Total input consumption tax (national portion) | Sum of creditable input tax at 7.8% and 6.24% |
| Line 11 | Input tax credit amount | After applying 95% rule or proportional method |
| Line 12 | Bad debt adjustment (tax amount recovered) | Tax on previously written-off receivables now recovered |
| Line 13 | Net input tax credit (Line 11 + Line 12) | -- |

#### Tax Payable / Refund Section

| Line | Description | Notes |
|------|-------------|-------|
| Line 14 | Tax payable or refundable (Line 8 - Line 13) | National consumption tax payable (positive) or refundable (negative) |
| Line 15 | Interim payment credit | Interim tax payments already made during the period |
| Line 16 | Net tax payable or refundable (Line 14 - Line 15) | Final national consumption tax payable/refundable |
| Line 17 | Local consumption tax payable | Line 14 x 22/78 |
| Line 18 | Interim local consumption tax credit | Local interim payments already made |
| Line 19 | Net local consumption tax payable/refundable | Line 17 - Line 18 |
| Line 20 | Total consumption tax payable/refundable | Line 16 + Line 19 |

#### Appendix 2 -- Input Tax Credit Calculation

| Section | Description | Notes |
|---------|-------------|-------|
| Section 1 | Taxable sales (tax-excluded) | Base for 95% rule test |
| Section 2 | Exempt sales | Non-taxable revenue |
| Section 3 | Total sales | Section 1 + Section 2 |
| Section 4 | Taxable sales ratio | Section 1 / Section 3 (percentage) |
| Section 5 | Total input tax | All consumption tax paid on purchases |
| Section 6 | Input tax on taxable-only purchases | Directly attributable to taxable supplies |
| Section 7 | Input tax on exempt-only purchases | Directly attributable to exempt supplies |
| Section 8 | Input tax on common purchases | Not directly attributable -- must be apportioned |
| Section 9 | Creditable input tax | Calculated per applicable method |

### 2b. Simplified Tax Calculation Method (Kantan Kazei) [T1]

Available only when base period taxable sales are JPY 50M or less AND election filed in advance.

**Legislation:** Consumption Tax Act, Article 37.

Under the simplified method, input tax credits are calculated as a deemed percentage of output tax, based on business category:

| Category | Business Type | Deemed Input Rate |
|----------|--------------|-------------------|
| Category 1 | Wholesale (oroshi-uri) | 90% |
| Category 2 | Retail (kouri) | 80% |
| Category 3 | Agriculture, forestry, fishery, mining, manufacturing, electricity/gas/water | 70% |
| Category 4 | Other (restaurants, services not in 1-3/5/6) | 60% |
| Category 5 | Services (finance, insurance, transport, communications, professional services) | 50% |
| Category 6 | Real estate | 40% |

**Legislation:** Consumption Tax Act, Article 37(1); Appended Table 4.

If a business has activities across multiple categories, the weighted-average method or most-advantageous method applies. [T2] -- flag for reviewer to confirm category allocation.

---

## Step 3: National and Local Tax Component Breakdown [T1]

JCT is a composite tax. Every calculation must split national and local components:

**Legislation:** Consumption Tax Act, Article 29; Local Tax Act, Article 72-78.

### Standard Rate (10%)
```
Total rate:           10.0%
National component:    7.8%
Local component:       2.2% (= 7.8% x 22/78)
```

### Reduced Rate (8%)
```
Total rate:            8.0%
National component:    6.24%
Local component:       1.76% (= 6.24% x 22/78)
```

### Extraction Formulas [T1]
```
From tax-included amount at 10%:
  National tax = Amount x 7.8 / 110
  Local tax    = Amount x 2.2 / 110
  Tax-excluded = Amount x 100 / 110

From tax-included amount at 8%:
  National tax = Amount x 6.24 / 108
  Local tax    = Amount x 1.76 / 108
  Tax-excluded = Amount x 100 / 108
```

---

## Step 4: Qualified Invoice System (QIS / Tekikaku Seikyuusho Hozon Houshiki) [T1]

### 4a. Overview

Effective 1 October 2023, the Qualified Invoice System replaced the prior Account-Based Method. Under QIS, input tax credits require retention of a qualified invoice (tekikaku seikyuusho) issued by a registered qualified invoice issuer (tekikaku seikyuusho hakkou jigyousha).

**Legislation:** Consumption Tax Act, Article 30(7)-(9) (input credit requirements); Article 57-2 (registration); Article 57-4 (qualified invoice requirements).

### 4b. Registration [T1]

- Any business operator conducting taxable transactions may apply for QIS registration with the NTA
- Tax-exempt operators (menzei jigyousha) who register become taxable operators by virtue of registration
- Registration number format: T + 13-digit corporate number (for corporations) or T + 13-digit assigned number (for individuals)
- Registration is published in the NTA's Qualified Invoice Issuer Publication Site

**Legislation:** Consumption Tax Act, Article 57-2(1)-(4).

### 4c. Required Contents of a Qualified Invoice [T1]

A qualified invoice must contain ALL of the following:

1. Name and QIS registration number (T-number) of the issuer
2. Date of the transaction (supply date)
3. Description of the goods or services supplied, with indication of which items are subject to the reduced rate
4. Total consideration for each applicable tax rate (tax-inclusive or tax-exclusive), grouped by rate
5. Consumption tax amount for each applicable rate, calculated on the grouped total
6. Name of the recipient (buyer)

**Legislation:** Consumption Tax Act, Article 57-4(1).

### 4d. Simplified Qualified Invoice (Tekikaku Kantan Seikyuusho) [T1]

Permitted for retail, food service, taxi, parking, and other businesses dealing with numerous unspecified customers. Differs from full qualified invoice:

- Recipient name is NOT required
- Either the tax rate OR the tax amount must be shown (not necessarily both)

**Legislation:** Consumption Tax Act, Article 57-4(2).

### 4e. Prohibited Conduct [T1]

- Non-registered persons MUST NOT issue documents that could be mistaken for qualified invoices
- Penalty: up to JPY 1,000,000 fine or imprisonment up to 1 year

**Legislation:** Consumption Tax Act, Article 57-5; Article 65(iv).

### 4f. QIS Transitional Measures (Input Credit for Non-Qualified Invoices) [T1]

For purchases from non-registered (tax-exempt) suppliers, transitional credit percentages apply:

| Period | Credit Percentage | Legislation |
|--------|------------------|-------------|
| 1 Oct 2023 -- 30 Sep 2026 | 80% of input tax | Act on Special Measures, Article 86-9, Paragraph 2 |
| 1 Oct 2026 -- 30 Sep 2029 | 50% of input tax | Act on Special Measures, Article 86-9, Paragraph 3 |
| From 1 Oct 2029 | 0% (no credit) | Full QIS enforcement |

**Important:** The transitional credit requires that the invoice from the non-registered supplier still meets the content requirements of the former account-based method, and the buyer must annotate the books to indicate that the transitional measure is being applied.

### 4g. Small Business QIS Special Measure (2-Wari Tokurei) [T1]

For formerly tax-exempt operators who registered for QIS, a special measure applies for fiscal years starting within the period 1 October 2023 to 30 September 2026:

- Tax payable = Output tax - (Output tax x 80%)
- Effectively, tax liability is capped at 20% of output tax
- Available only if base period taxable sales are JPY 10M or less
- No actual input tax credit calculation required

**Legislation:** Act on Special Measures Concerning Taxation (28th Revised Act), Article 86-9-2.

---

## Step 5: Input Tax Credit Rules

### 5a. The 95% Rule [T1]

**Legislation:** Consumption Tax Act, Article 30(1)-(2).

If taxable sales ratio (taxable sales / total sales) is **95% or more** AND taxable sales do not exceed **JPY 500M** for the period:
- **Full input tax credit** is allowed on ALL consumption tax paid on purchases
- No apportionment required

If taxable sales ratio is **below 95%** OR taxable sales **exceed JPY 500M**:
- Input tax must be apportioned using one of the methods below [T2]

### 5b. Apportionment Methods (When 95% Rule Does Not Apply) [T2]

**Legislation:** Consumption Tax Act, Article 30(2)-(5).

Three methods are available. A qualified tax accountant must confirm the most appropriate method:

#### Method 1: Individual Attribution (Kobetsu Taiou Houshiki)
- Input tax directly attributable to taxable supplies: fully creditable
- Input tax directly attributable to exempt supplies: not creditable
- Input tax on common purchases: apportioned by taxable sales ratio

#### Method 2: Lump-Sum Proportional (Ikkatsu Hirei Haibun Houshiki)
- ALL input tax (including directly attributable) is multiplied by the taxable sales ratio
- Simpler but may be less advantageous

#### Method 3: Proportional with Specific Criteria (Approved Method)
- Requires advance approval from NTA
- Uses alternative allocation bases (floor space, headcount, etc.)

**Once a method is elected, it generally must be used for at least 2 consecutive years.**

### 5c. Blocked / Non-Creditable Input Tax [T1]

The following input tax is NEVER creditable regardless of other rules:

| Category | Legislation |
|----------|-------------|
| Personal consumption / private use | Consumption Tax Act, Article 30(1) -- only business-use purchases qualify |
| Purchases not supported by qualified invoice (post-transition) | Article 30(7) |
| Entertainment expenses with no business nexus | Article 30(1) -- must be in course of business |
| Purchases for producing exempt supplies (when 95% rule fails) | Article 30(2) |
| Consumption tax on purchases from fictitious invoices | Article 30(7) -- invoice must be genuine |

### 5d. Capital Asset Adjustments [T2]

**Legislation:** Consumption Tax Act, Article 33 (adjustment for significant assets); Article 34 (adjustment for change in taxable status).

For capital assets (chousei taishou koteishisan) costing JPY 1,000,000 or more (tax-excluded):
- If the taxable sales ratio changes significantly (by 50 percentage points or more) within the 3-year adjustment period, input tax credit must be adjusted
- Applies to the third year after acquisition
- Flag for reviewer: confirm whether adjustment applies based on ratio change

For residential rental property (kyojuu-you chinntai):
- Input tax on construction/purchase of residential rental property is BLOCKED if used exclusively for exempt residential rental
- If subsequently converted to taxable use within 3 years, partial recovery may be available [T2]

**Legislation:** Consumption Tax Act, Article 35-2 (residential rental property restriction, effective April 2020).

---

## Step 6: Reverse Charge Mechanism

### 6a. Cross-Border Digital Services (Since 1 October 2015) [T1]

**Legislation:** Consumption Tax Act, Article 4(3)-2 to (3)-4; Article 5(2).

Digital services provided by foreign providers to recipients in Japan are subject to JCT under the following framework:

| Service Type | Provider | Recipient | Who Accounts for JCT |
|-------------|----------|-----------|---------------------|
| B2B digital services | Foreign | Japanese business | Recipient (reverse charge) |
| B2C digital services | Foreign registered | Japanese consumer | Foreign provider (registered for JCT) |
| B2C digital services | Foreign not registered | Japanese consumer | No JCT collected (foreign provider must register if exceeding threshold) |

**"Digital services" (denki tsushin rieki jigyou) include:** e-books, music/video streaming, software subscriptions (SaaS), online advertising, cloud services, online gaming, digital consulting delivered electronically.

### 6b. Reverse Charge Accounting for B2B Digital Services [T1]

**Legislation:** Consumption Tax Act, Article 5(2); Article 28(4).

When a Japanese taxable business receives B2B digital services from a foreign provider:
1. Include the service amount in BOTH taxable sales AND taxable purchases for consumption tax calculation purposes
2. Self-assess output tax at the applicable rate (10%)
3. Claim input tax credit at the same rate (subject to 95% rule)
4. Net effect is zero if the 95% rule applies (full credit)
5. If the 95% rule does NOT apply, the reverse-charged amount is subject to the normal apportionment rules [T2]

**Special rule:** If the recipient's taxable sales ratio is 95% or more AND taxable sales do not exceed JPY 500M, the reverse charge is effectively ignored (output and input cancel out). The NTA has confirmed that in this case, reporting is not required.

### 6c. Platform Taxation (Since April 2025) [T1]

**Legislation:** 2024 Tax Reform Act; Consumption Tax Act, Article 15-2 (as amended).

Designated platform operators (shitei purattofoumu jigyousha) are deemed the supplier for B2C digital services sold through their platforms by foreign providers. The platform operator must:
- Register for JCT
- Collect and remit JCT on behalf of foreign sellers
- Issue qualified invoices

This does not affect B2B transactions (reverse charge still applies).

---

## Step 7: Registration and Taxable Status

### 7a. Taxable vs Tax-Exempt Business Operators [T1]

**Legislation:** Consumption Tax Act, Article 9 (tax-exempt operator); Article 9-2 (specified period test).

| Status | Condition |
|--------|-----------|
| Tax-exempt (menzei jigyousha) | Base period taxable sales <= JPY 10,000,000 AND specified period taxable sales <= JPY 10,000,000 (or payroll <= JPY 10M) |
| Taxable (kazei jigyousha) | Base period taxable sales > JPY 10,000,000 OR specified period sales > JPY 10,000,000 |
| Voluntarily taxable | Tax-exempt operator who elects taxable status (Article 9(4)) -- irrevocable for 2 years |
| Newly established corporation | Special rules in first 2 fiscal years (no base period) -- see 7b |

**Base period (kijun kikan):**
- Corporations: the fiscal year two years prior
- Individuals: the calendar year two years prior

**Specified period (tokutei kikan):**
- Corporations: the first 6 months of the immediately preceding fiscal year
- Individuals: 1 January to 30 June of the preceding year

### 7b. Newly Established Corporations [T1]

**Legislation:** Consumption Tax Act, Article 12-2; Article 12-3.

- In the first two fiscal years, no base period exists, so the entity is generally tax-exempt
- **Exception 1:** If paid-in capital at incorporation is JPY 10M or more, the entity is taxable from day one
- **Exception 2:** If the entity is a subsidiary of a large corporation (parent with taxable sales > JPY 500M), special taxable status applies
- **Exception 3:** If the entity registers as a QIS issuer, it becomes taxable by virtue of registration

### 7c. QIS Registration for Tax-Exempt Operators [T1]

**Legislation:** Consumption Tax Act, Article 57-2(2).

A tax-exempt operator may register as a qualified invoice issuer. Upon registration:
- The operator becomes a taxable operator for the period from the registration date
- The operator must file consumption tax returns
- The 2-wari tokurei (20% liability cap) may apply during the transitional period (see Step 4g)

---

## Step 8: Filing Deadlines and Interim Returns

### 8a. Annual Return Filing Deadline [T1]

**Legislation:** Consumption Tax Act, Article 45 (corporations); Article 45(1) (individuals).

| Entity Type | Filing Deadline |
|-------------|----------------|
| Corporation | Within 2 months after the end of the fiscal year |
| Individual | 31 March of the following year (for calendar year filers) |

**Extension:** Corporations may obtain a 1-month extension for income tax filing, but consumption tax filing does NOT automatically extend. A separate application for extension of the consumption tax deadline may be available but is not guaranteed. [T2]

### 8b. Interim Returns (Chuukan Shinkoku) [T1]

**Legislation:** Consumption Tax Act, Article 42; Article 43.

Interim returns are required based on the prior year's annual national consumption tax liability:

| Prior Year National Tax | Interim Frequency | Payment Schedule |
|------------------------|-------------------|-----------------|
| JPY 480,000 or less | None (annual only) | -- |
| JPY 480,001 -- JPY 4,000,000 | 1 interim return (semi-annual) | Within 2 months after the first 6 months |
| JPY 4,000,001 -- JPY 48,000,000 | 3 interim returns (quarterly) | Within 2 months after each 3-month period |
| Over JPY 48,000,000 | 11 interim returns (monthly) | Within 2 months after each month |

**Interim calculation options:**
1. **Proportional method (default):** Prior year tax / number of interim periods
2. **Actual calculation method:** File based on actual figures for the interim period (optional but may be advantageous if current period tax is lower)

### 8c. Payment Deadlines [T1]

Payment is due on the same date as the filing deadline. Late payment triggers delinquent tax (entai-zei):
- First 2 months: approximately 2.4% per annum (variable, linked to prime rate + 1%)
- After 2 months: approximately 8.7% per annum (variable, linked to prime rate + 7.3%)

**Legislation:** National Tax General Act (Kokuzei Tsuusoku Hou), Article 60.

### 8d. Penalties [T1]

| Penalty Type | Rate / Amount | Legislation |
|-------------|--------------|-------------|
| Late filing penalty (mushinkoku kasanzei) | 15% of tax (20% if tax > JPY 500,000 on the excess) | National Tax General Act, Article 66 |
| Understatement penalty (kajou-shinkoku kasanzei) | 10% of additional tax (15% on excess over JPY 500,000 or prior return amount, whichever greater) | Article 65 |
| Fraud penalty (juukazei) | 35% of evaded tax | Article 68 |
| No-return penalty with fraud | 40% of evaded tax | Article 68 |
| Delinquent tax (entai-zei) | Variable rate per 8c above | Article 60 |

---

## Step 9: Transaction Classification Matrix [T1]

### 9a. Sales (Output Tax)

| Transaction | Rate | Return Line | Notes |
|------------|------|-------------|-------|
| Domestic sale of goods (standard) | 10% | Line 1 / Line 3 | Include tax in consideration |
| Domestic sale of food/beverages (take-out, delivery) | 8% | Line 2 / Line 4 | Reduced rate; excl. alcohol, dine-in |
| Domestic sale of subscribed newspapers (2x/week+) | 8% | Line 2 / Line 4 | Physical subscription only |
| Export of goods | 0% | Line 9 | Zero-rated; full input credit |
| International services to non-residents | 0% | Line 9 | Zero-rated; confirm place of supply |
| Rental of residential property | Exempt | Not on return as taxable | No output tax; reduces taxable ratio |
| Sale of land | Exempt | Not on return as taxable | No output tax; reduces taxable ratio |
| Interest income | Exempt | Not on return as taxable | Financial transaction exemption |
| Sale of securities | Exempt | Not on return as taxable (5% of value counted for ratio) | Special rule for ratio calculation |
| Insurance claims received | Non-taxable | Not on return | Outside scope |
| Government subsidies | Non-taxable | Not on return | Outside scope (no consideration for supply) |
| Dividend income | Non-taxable | Not on return | Outside scope |

### 9b. Purchases (Input Tax)

| Transaction | Rate Paid | Creditable? | Notes |
|------------|-----------|-------------|-------|
| Domestic purchase of goods/services (standard, with QI) | 10% | Yes | Qualified invoice required |
| Domestic purchase of food for resale (with QI) | 8% | Yes | Reduced rate input |
| Purchase from non-registered supplier (2023-2026) | 10% or 8% | 80% | Transitional measure |
| Purchase from non-registered supplier (2026-2029) | 10% or 8% | 50% | Transitional measure |
| Purchase from non-registered supplier (from 2029) | 10% or 8% | 0% | No credit without QI |
| Import of goods (customs) | 10% or 8% | Yes | Tax paid at customs; receipt required |
| Purchase of capital asset >= JPY 1M | 10% | Yes (subject to adjustment) | 3-year adjustment period applies |
| Residential rental property construction | 10% | Blocked | Article 35-2 restriction |
| Entertainment (with business nexus) | 10% | Yes (subject to income tax limits) | Must be in course of business |
| Entertainment (no business nexus / personal) | 10% | Blocked | Not in course of business |
| Employee salary / wages | N/A | N/A | Not a taxable purchase |
| B2B digital services from abroad | 10% (reverse charge) | Reverse charge | See Step 6 |

---

## Step 10: Comparison with EU VAT System

| Feature | Japan JCT | EU VAT (Directive 2006/112/EC) |
|---------|-----------|-------------------------------|
| Standard rate | 10% (single national rate) | 15-27% (varies by member state) |
| Reduced rate | 8% (single reduced rate) | Multiple reduced rates permitted (5%+); some super-reduced/zero |
| Rate components | National (7.8%) + Local (2.2%) reported together | Single rate, no sub-national split |
| Invoice system | Qualified Invoice System (QIS) from Oct 2023 | VAT invoice requirements long established; e-invoicing rollout varies |
| Registration threshold | JPY 10M (~EUR 60,000) in base period | Varies by state (EUR 0 -- EUR 85,000) |
| Filing frequency | Annual + interim based on prior year tax | Varies by state (monthly/quarterly/annual) |
| Reverse charge (B2B services) | Yes, for cross-border digital services | Yes, for all cross-border B2B services |
| Reverse charge (B2B goods) | No (import VAT at customs) | Intra-community acquisition (reverse charge for goods within EU) |
| Input credit apportionment | 95% rule + 3 methods | Pro-rata based on turnover ratio; varies by state |
| Exempt supply treatment | Similar (land, financial, medical, education, residential rental) | Similar (land, financial, medical, education) |
| Place of supply -- services | B2B: recipient location; B2C: supplier location (with digital service exceptions) | B2B: recipient; B2C: supplier (with digital/telecom exceptions) |
| Transitional credit for non-registered suppliers | Yes (80%/50%/0% over 6 years) | No equivalent (EU always required VAT invoices from registered suppliers) |
| Simplified method | Deemed input rate by industry (40-90%) | Flat-rate schemes exist in some states |
| Tax return currency | JPY only | Local currency of member state |
| Filing portal | e-Tax (national) | National portals per member state |
| Penalties for late filing | 15-20% surcharge + delinquent tax | Varies by state |
| Group registration | Limited (consolidated only for certain structures) [T3] | VAT grouping available in many states |

---

## Step 11: Edge Case Registry

### EC1 -- Dine-in vs Take-out Determination [T1]

**Situation:** A food retailer sells bento boxes. Some customers eat at tables provided in the store; others take away.
**Resolution:** If the retailer provides tables/seating for eating and the customer indicates intent to eat in, standard rate (10%) applies. If the customer takes away, reduced rate (8%) applies. The determination is made at the point of sale based on the customer's stated intention. If the retailer asks at the register and the customer says "take-out," the reduced rate applies even if the customer subsequently eats on premises.
**Legislation:** Consumption Tax Act, Appended Table 1, Note 1; NTA Q&A on Reduced Rate (Category 1-2).

### EC2 -- Alcohol Content in Food Products [T1]

**Situation:** A product labelled as cooking wine (mirin) or a food item containing alcohol is sold.
**Resolution:** If the product is classified as an alcoholic beverage under the Liquor Tax Act (shuzeinou > 1%), standard rate (10%) applies, not reduced rate. "Hon-mirin" is an alcoholic beverage (10%). "Mirin-style seasoning" (mirin-fuu choumiryou) with < 1% alcohol and added salt is a food product (8%).
**Legislation:** Consumption Tax Act, Appended Table 1, Column 1, Item 1(a); Liquor Tax Act, Article 2.

### EC3 -- Catering vs Delivery [T1]

**Situation:** A company orders food delivered to its office for a meeting. The food service sends staff to set up and serve.
**Resolution:** If the supplier provides serving services (haizen -- arranging plates, serving to individuals, clearing), this is classified as food service (gaishoku) at 10%. If the supplier simply delivers food without serving (e.g., pizza delivery, bento delivery), the reduced rate (8%) applies.
**Legislation:** Consumption Tax Act, Appended Table 1, Note 2; NTA Q&A on Reduced Rate (Category 3).

### EC4 -- Newspaper Subscription vs Single Purchase [T1]

**Situation:** A company buys newspapers at a convenience store daily rather than subscribing.
**Resolution:** Only newspapers sold under a subscription agreement (teiki koudoku keiyaku) qualify for the reduced rate (8%). Individual purchases at retail are standard rate (10%). Digital newspaper subscriptions are also standard rate (10%) -- the reduced rate applies only to physical newspapers.
**Legislation:** Consumption Tax Act, Appended Table 1, Column 1, Item 2.

### EC5 -- QIS Transitional Credit Calculation [T2]

**Situation:** A business purchases JPY 1,100,000 (tax-included) of goods from a non-registered supplier in the period 1 October 2023 to 30 September 2026.
**Resolution:** The implied consumption tax is JPY 100,000 (= JPY 1,100,000 x 10/110). Under the 80% transitional measure, the creditable amount is JPY 100,000 x 80% = JPY 80,000 (of which national portion = JPY 80,000 x 78/100 = JPY 62,400). The buyer must annotate purchase records to indicate that the transitional measure is applied and retain the supplier's invoice (which need not be a qualified invoice but must meet prior format requirements). Flag for reviewer to confirm calculation and documentation.
**Legislation:** Act on Special Measures Concerning Taxation, Article 86-9.

### EC6 -- 95% Rule Threshold Exceeded [T2]

**Situation:** A business has taxable sales of JPY 600M (taxable sales ratio is 98%) in the period.
**Resolution:** Even though the taxable sales ratio exceeds 95%, the JPY 500M taxable sales ceiling is breached. Therefore, the 95% rule does NOT apply and input tax must be apportioned using the individual attribution method, lump-sum proportional method, or approved method. Flag for reviewer to select and calculate the appropriate method.
**Legislation:** Consumption Tax Act, Article 30(2).

### EC7 -- Small Business QIS Exemption (2-Wari Tokurei) [T1]

**Situation:** An individual sole proprietor with prior-year taxable sales of JPY 8M registered for QIS on 1 October 2023. In the current period (within 1 Oct 2023 - 30 Sep 2026), output tax is JPY 500,000.
**Resolution:** Under the 2-wari tokurei, the tax payable is JPY 500,000 x 20% = JPY 100,000. No actual input tax credit calculation is needed. This is available because base period sales are JPY 10M or less and the fiscal year starts within the eligible window.
**Legislation:** Act on Special Measures Concerning Taxation (28th Revised Act), Article 86-9-2.

### EC8 -- Export Zero-Rating and Proof Requirements [T1]

**Situation:** A Japanese manufacturer sells goods to a US buyer. Goods are shipped from a Japanese port.
**Resolution:** The sale qualifies as an export transaction at 0% under Article 7. The exporter must retain: (a) export declaration (yushutsu kyokasho) stamped by customs, (b) shipping documents (bill of lading), (c) sales contract or purchase order. Without these documents, zero-rating is denied and 10% tax applies. All input tax on purchases attributable to the export is fully creditable.
**Legislation:** Consumption Tax Act, Article 7(1)(i); Enforcement Regulations, Article 5.

### EC9 -- Sale of Securities and the Taxable Sales Ratio [T1]

**Situation:** A business sells listed shares for JPY 100M, generating a gain. Total other taxable sales are JPY 50M. Exempt sales (interest) are JPY 5M.
**Resolution:** For purposes of the taxable sales ratio calculation, only 5% of the face value of securities sold is included in exempt sales (not the full JPY 100M). So exempt sales for ratio = JPY 5M (interest) + JPY 5M (5% of JPY 100M securities) = JPY 10M. Taxable ratio = JPY 50M / (JPY 50M + JPY 10M) = 83.3%. The 95% rule would NOT apply (ratio < 95%), so apportionment is required.
**Legislation:** Consumption Tax Act, Enforcement Order, Article 48(1); NTA circular on taxable sales ratio.

### EC10 -- Import of Goods and Customs JCT [T1]

**Situation:** A business imports raw materials from China. Japan Customs assesses consumption tax on the CIF value plus customs duty.
**Resolution:** JCT on imports is paid to Customs (not on the regular return as reverse charge). The tax paid is creditable as input tax on the consumption tax return, provided the import permit (yunyuu kyokasho) is retained. The tax base for import JCT = CIF value + customs duty + excise tax (if any). Standard rate (10%) applies to most goods; reduced rate (8%) applies to imported food and beverages (excluding alcohol).
**Legislation:** Consumption Tax Act, Article 28(4) (tax base for imports); Article 30(1)(ii) (input credit for import tax).

### EC11 -- Deemed Supply on Personal Use [T1]

**Situation:** A business operator takes inventory (standard-rated goods) for personal use.
**Resolution:** Under JCT, consumption of business assets for personal use is treated as a deemed supply. Output tax at the applicable rate must be accounted for, based on the market value or the cost price (whichever is higher for income tax, but cost is acceptable for JCT if it is at least purchase price). The business must issue a record of self-supply.
**Legislation:** Consumption Tax Act, Article 4(5)(i) (deemed supply for personal consumption); Article 28(3) (tax base for deemed supplies).

### EC12 -- Free Samples and Promotional Gifts [T1]

**Situation:** A business gives away product samples to potential customers as a marketing activity.
**Resolution:** Free distribution of business assets for business promotion purposes is NOT treated as a deemed supply for JCT (unlike personal consumption). No output tax is required. However, input tax previously claimed on the production/purchase of the samples remains creditable, as the samples are used in the course of business (for taxable sales promotion).
**Legislation:** Consumption Tax Act, Article 4(5) -- deemed supply applies only to personal use and gifts to related parties, not to business promotion; NTA circular (kihon tsuttatsu) 5-3-1.

### EC13 -- Mixed Supplies (Standard and Reduced Rate in One Transaction) [T1]

**Situation:** A convenience store sale includes a bento (food, 8%) and a bottle of sake (alcohol, 10%) on a single receipt.
**Resolution:** Each item must be classified separately. The qualified invoice (or simplified qualified invoice) must show the tax-included amount grouped by rate: one total for 8% items and one total for 10% items, with the consumption tax calculated on each group total. The receipt must indicate which items are subject to the reduced rate (commonly marked with an asterisk).
**Legislation:** Consumption Tax Act, Article 57-4(1)(iv)-(v); NTA guidance on multi-rate invoicing.

### EC14 -- Adjustment for Bad Debts [T1]

**Situation:** A business wrote off a receivable of JPY 1,100,000 (tax-included at 10%) as uncollectable.
**Resolution:** The business can claim a bad debt adjustment (kashidaore ni kakaru zei-gaku no koujo) equal to the consumption tax portion of the written-off receivable: JPY 1,100,000 x 7.8/110 = JPY 78,000 (national portion). This is entered on Line 12 of the return. If the debt is subsequently recovered, the recovered tax must be added back to output tax in the period of recovery.
**Legislation:** Consumption Tax Act, Article 39 (bad debt relief); Article 39(3) (recovery adjustment).

---

## Step 12: Test Suite

### Test 1 -- Standard domestic sale [T1]

**Input:** Corporation sells office equipment to domestic customer. Invoice: JPY 550,000 (tax-included). Standard rate 10%.
**Expected output:**
- Tax-excluded amount: JPY 500,000
- National consumption tax: JPY 550,000 x 7.8/110 = JPY 39,000
- Local consumption tax: JPY 550,000 x 2.2/110 = JPY 11,000
- Report: Line 1 = JPY 550,000; Line 3 = JPY 39,000
- Local tax: Line 17 calculated as Line 14 x 22/78

### Test 2 -- Reduced rate food sale (take-out) [T1]

**Input:** Convenience store sells bento boxes for take-out. Daily total: JPY 108,000 (tax-included). Reduced rate 8%.
**Expected output:**
- Tax-excluded amount: JPY 100,000
- National consumption tax: JPY 108,000 x 6.24/108 = JPY 6,240
- Local consumption tax: JPY 108,000 x 1.76/108 = JPY 1,760
- Report: Line 2 = JPY 108,000; Line 4 = JPY 6,240

### Test 3 -- Export zero-rated sale [T1]

**Input:** Manufacturer exports goods to US buyer. Invoice: JPY 10,000,000. Export declaration obtained from customs.
**Expected output:**
- JCT rate: 0%
- Report: Line 9 = JPY 10,000,000
- Full input tax credit available on attributable purchases
- No output tax

### Test 4 -- Purchase with qualified invoice (standard rate) [T1]

**Input:** Business purchases office supplies from registered supplier. Invoice shows: JPY 330,000 (tax-included), consumption tax JPY 30,000, QIS registration number T1234567890123.
**Expected output:**
- Input tax (national): JPY 330,000 x 7.8/110 = JPY 23,400
- Creditable in full (assuming 95% rule applies)
- Report: included in Line 10 and Line 11

### Test 5 -- Purchase from non-registered supplier (transitional 80%) [T2]

**Input:** Business purchases raw materials from a non-QIS-registered farmer for JPY 540,000 (tax-included at 8%) during the period Oct 2023 - Sep 2026. No qualified invoice available.
**Expected output:**
- Implied national tax: JPY 540,000 x 6.24/108 = JPY 31,200
- Transitional credit: JPY 31,200 x 80% = JPY 24,960
- Non-creditable portion: JPY 31,200 x 20% = JPY 6,240
- Buyer must annotate records; flag for reviewer confirmation

### Test 6 -- Reverse charge on B2B digital services from abroad [T1]

**Input:** Japanese corporation subscribes to US-based SaaS platform. Monthly fee: USD 5,000 (approx JPY 750,000). No JCT charged by supplier.
**Expected output:**
- Self-assess output tax: JPY 750,000 x 7.8% = JPY 58,500 (national)
- Self-assess input tax: JPY 750,000 x 7.8% = JPY 58,500 (national)
- Net effect: zero (if 95% rule applies)
- If 95% rule does NOT apply: flag for reviewer -- input credit subject to apportionment

### Test 7 -- 95% rule does not apply (taxable sales > JPY 500M) [T2]

**Input:** Corporation has taxable sales of JPY 800M, exempt sales of JPY 10M (taxable ratio = 98.8%). Total input tax paid: JPY 20,000,000 (national portion).
**Expected output:**
- Taxable ratio: 98.8% (>= 95%)
- BUT taxable sales exceed JPY 500M, so 95% rule is NOT available
- Must use apportionment method
- If lump-sum proportional: creditable = JPY 20,000,000 x 98.8% = JPY 19,760,000
- Flag for reviewer: confirm method selection

### Test 8 -- Simplified method (kantan kazei) [T1]

**Input:** Small retailer (Category 2) with base period sales JPY 30M. Output tax for the period: national consumption tax = JPY 2,340,000.
**Expected output:**
- Deemed input rate for Category 2 (retail): 80%
- Deemed input tax credit: JPY 2,340,000 x 80% = JPY 1,872,000
- Tax payable (national): JPY 2,340,000 - JPY 1,872,000 = JPY 468,000
- Local tax: JPY 468,000 x 22/78 = JPY 132,000
- Total payable: JPY 600,000

### Test 9 -- Interim return calculation [T1]

**Input:** Corporation's prior year national consumption tax was JPY 6,000,000. Fiscal year is April to March.
**Expected output:**
- Prior year tax is between JPY 4,000,001 and JPY 48,000,000
- 3 interim returns required (quarterly)
- Each interim payment: JPY 6,000,000 / 3 = JPY 2,000,000 (national)
- Local interim: JPY 2,000,000 x 22/78 = JPY 564,103 per interim
- Filing deadlines: within 2 months after each 3-month period end

### Test 10 -- Bad debt adjustment [T1]

**Input:** Corporation wrote off receivable of JPY 2,200,000 (originally invoiced at 10%, tax-included) as uncollectable in the current period.
**Expected output:**
- Bad debt tax adjustment (national): JPY 2,200,000 x 7.8/110 = JPY 156,000
- Report: Line 12 = JPY 156,000
- This reduces net tax payable
- If subsequently recovered, JPY 156,000 must be added back to output

### Test 11 -- Residential rental property input tax block [T1]

**Input:** Corporation constructs a residential apartment building for rental. Construction cost: JPY 110,000,000 (tax-included at 10%). All units are for residential rental (exempt supply).
**Expected output:**
- Input tax: JPY 110,000,000 x 7.8/110 = JPY 7,800,000
- Input tax is BLOCKED under Article 35-2 (exclusively for exempt residential rental)
- Creditable amount: JPY 0
- If any units are converted to taxable use (e.g., office rental) within 3 years, partial recovery is possible [T2]

### Test 12 -- 2-Wari Tokurei for newly registered QIS operator [T1]

**Input:** Individual sole proprietor registered for QIS on 1 Oct 2023. Base period sales: JPY 7M. Current period output tax (national): JPY 390,000. Period falls within Oct 2023 - Sep 2026.
**Expected output:**
- 2-Wari tokurei applies (base period < JPY 10M, period within eligible window)
- Tax payable (national): JPY 390,000 x 20% = JPY 78,000
- Local tax: JPY 78,000 x 22/78 = JPY 22,000
- Total payable: JPY 100,000
- No input credit calculation required

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified tax accountant (zeirishi) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified tax accountant (zeirishi). Document gap.
```

---

## PROHIBITIONS [T1]

- NEVER guess the applicable JCT rate -- it is deterministic from the transaction type and applicable legislation
- NEVER apply the reduced rate (8%) to alcohol, dine-in food service, digital newspaper subscriptions, or single-copy newspaper purchases
- NEVER allow input tax credit without a qualified invoice (post-transition period) or without proper transitional documentation (during transition)
- NEVER apply the 95% rule when taxable sales exceed JPY 500M, regardless of the taxable sales ratio
- NEVER classify salaries, dividends, insurance claims, government subsidies, or loan principal as taxable transactions
- NEVER treat import JCT (paid at customs) as reverse charge -- import JCT is paid to Customs and claimed as input credit from the customs receipt
- NEVER apply reverse charge to B2C digital services -- B2C is handled by the foreign provider's registration or platform taxation
- NEVER allow input credit on residential rental property construction used exclusively for exempt residential rental (Article 35-2)
- NEVER ignore the 3-year capital asset adjustment rule for assets costing JPY 1,000,000+ when the taxable ratio changes significantly
- NEVER apply the simplified method (kantan kazei) if base period taxable sales exceed JPY 50M
- NEVER allow the 2-wari tokurei if base period taxable sales exceed JPY 10M or the fiscal year falls outside the eligible window
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER issue or instruct issuance of a document resembling a qualified invoice on behalf of a non-registered person
- NEVER classify a transaction without confirming the client's taxable status (kazei jigyousha vs menzei jigyousha) first

---

## Contribution Notes (For Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all return form line numbers with the equivalent lines on your jurisdiction's consumption/VAT return form.
3. Replace tax rates (10% / 8%) with your jurisdiction's standard and reduced rates.
4. Replace the capital asset threshold (JPY 1,000,000) with your jurisdiction's equivalent.
5. Replace the registration threshold (JPY 10,000,000) with your jurisdiction's equivalent.
6. Replace the simplified method categories and deemed rates with your jurisdiction's equivalent.
7. Replace the QIS requirements with your jurisdiction's invoice requirements.
8. Replace the blocked categories with your jurisdiction's equivalent non-deductible categories.
9. Have a qualified tax practitioner in your jurisdiction validate every T1 rule before publishing.
10. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
11. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
