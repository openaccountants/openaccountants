---
name: jp-consumption-tax
description: Use this skill whenever asked about Japanese Consumption Tax (消費税 / JCT) for self-employed individuals. Trigger on phrases like "consumption tax", "shohizei", "JCT", "qualified invoice", "invoice system", "T-number", "simplified taxation", "簡易課税", "消費税確定申告", or any question about consumption tax filing, rates, or the qualified invoice system for sole proprietors in Japan. Covers standard rate (10%), reduced rate (8%), qualified invoice system (インボイス制度), simplified taxation (簡易課税), and registration thresholds. ALWAYS read this skill before touching any Japanese consumption tax work.
---

# Japan Consumption Tax (消費税) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | Consumption Tax Act (消費税法) |
| Supporting Legislation | Act on Special Measures Concerning Taxation (租税特別措置法); Qualified Invoice Preservation Method (適格請求書等保存方式) |
| Tax Authority | National Tax Agency (国税庁 / NTA) |
| Filing Portal | e-Tax (etax.nta.go.jp) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Japanese tax accountant (税理士) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: rate application, threshold determination, simplified taxation calculation. Tier 2: mixed-supply classification, partial exemption, transitional measures. Tier 3: cross-border digital services, customs duties, group taxation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any consumption tax figure, you MUST know:

1. **Taxable sales in base period (基準期間)** [T1] -- two calendar years prior (for sole proprietors)
2. **Taxable sales in specified period (特定期間)** [T1] -- January 1 to June 30 of prior year
3. **Whether registered as a qualified invoice issuer (適格請求書発行事業者)** [T1] -- T-number registration
4. **Nature of supplies** [T1] -- standard-rated, reduced-rated, exempt, or non-taxable
5. **Total taxable purchases (input tax)** [T1] -- for general method calculation
6. **Whether simplified taxation (簡易課税) has been elected** [T1] -- election form submitted
7. **Business type under simplified taxation** [T1] -- determines deemed purchase ratio

**If taxable sales in the base period are <= JPY 10,000,000 AND the client is not a qualified invoice registrant, the client is a tax-exempt business (免税事業者). STOP -- no consumption tax filing required unless voluntarily registered.**

---

## Step 1: Rates and Taxable Supplies [T1]

**Legislation:** Consumption Tax Act, Art. 29

### Tax Rates [T1]

| Category | National CT Rate | Local CT Rate | Combined Rate |
|----------|-----------------|---------------|---------------|
| Standard rate | 7.8% | 2.2% | **10%** |
| Reduced rate (軽減税率) | 6.24% | 1.76% | **8%** |

### Reduced Rate Items (8%) [T1]

| Item | Detail |
|------|--------|
| Food and beverages | Excluding alcohol and dining-in (外食) |
| Newspapers | Delivered by subscription, published at least twice weekly |

### Non-Taxable Transactions [T1]

| Category | Examples |
|----------|---------|
| Exempt (非課税) | Land sales/leases, securities, medical services under insurance, educational tuition, funeral/burial services |
| Out of scope (不課税) | Gifts, donations, government subsidies, insurance proceeds |
| Export exempt (免税) | Exports of goods, international transport, services to non-residents consumed outside Japan |

---

## Step 2: Filing Threshold Determination [T1]

**Legislation:** Consumption Tax Act, Art. 9

| Test | Threshold | Period |
|------|-----------|--------|
| Base period test (基準期間) | Taxable sales > JPY 10,000,000 | 2 calendar years prior |
| Specified period test (特定期間) | Taxable sales > JPY 10,000,000 (AND wages > JPY 10,000,000) | Jan 1 - Jun 30 of prior year |
| Qualified invoice registration | Voluntarily becomes taxable regardless of sales | From registration date |

### Base Period for Sole Proprietors [T1]

| Filing Year | Base Period |
|-------------|-------------|
| 2025 | Calendar year 2023 |
| 2026 | Calendar year 2024 |

If base period taxable sales <= JPY 10,000,000, check specified period. If both are under threshold AND not registered as qualified invoice issuer, the business is tax-exempt.

---

## Step 3: Qualified Invoice System (インボイス制度) [T1]

**Legislation:** Consumption Tax Act, Art. 57-2 to 57-6 (effective October 1, 2023)

### Required Elements on a Qualified Invoice [T1]

| Element | Detail |
|---------|--------|
| 1. Issuer name and T-number | T + 13-digit number (e.g., T1234567890123) |
| 2. Transaction date | Date of supply |
| 3. Description of goods/services | Sufficient detail to identify the supply |
| 4. Tax-rate-separated amounts | Separate totals for 10% and 8% items |
| 5. Consumption tax amount by rate | Tax amount for each rate category |
| 6. Recipient name | Name of the purchaser |

### Registration [T1]

| Detail | Value |
|--------|-------|
| Application form | 適格請求書発行事業者の登録申請書 |
| Filing | Via e-Tax or paper to tax office |
| Effect | Once registered, MUST remain taxable even if sales fall below JPY 10M |
| Cancellation | Must submit cancellation notice; effective from following fiscal year |

### Transitional Measures for Purchasers (2023-2029) [T1]

| Period | Input Tax Credit from Non-Registered Suppliers |
|--------|-----------------------------------------------|
| Oct 2023 -- Sep 2026 | 80% of input tax creditable |
| Oct 2026 -- Sep 2029 | 50% of input tax creditable |
| Oct 2029 onward | 0% -- no credit without qualified invoice |

### Small Business Special Measure (2割特例) [T1]

| Detail | Value |
|--------|-------|
| Eligibility | Businesses that became taxable solely due to invoice registration |
| Tax calculation | Tax payable = Output tax x 20% (i.e., deemed input tax = 80%) |
| Duration | Available through returns for periods ending by September 30, 2026 |
| Election | No prior filing needed; elect on the return |

---

## Step 4: Computation -- General Method (本則課税) [T1]

**Legislation:** Consumption Tax Act, Art. 30

| Step | Action |
|------|--------|
| 4.1 | Calculate total output tax: sum of (taxable sales x applicable rate) |
| 4.2 | Separate output tax by rate: 7.8% national + 2.2% local (standard); 6.24% + 1.76% (reduced) |
| 4.3 | Calculate total input tax: sum of (taxable purchases x applicable rate) from qualified invoices |
| 4.4 | If taxable sales ratio (課税売上割合) >= 95% AND taxable sales <= JPY 500M: full input tax credit |
| 4.5 | If taxable sales ratio < 95% or taxable sales > JPY 500M: apply proportional method or individual method [T2] |
| 4.6 | Tax payable = Output tax - Input tax credit |

### Taxable Sales Ratio [T1]

Taxable sales ratio = Taxable sales / (Taxable sales + Exempt sales)

---

## Step 5: Computation -- Simplified Taxation (簡易課税) [T1]

**Legislation:** Consumption Tax Act, Art. 37

### Eligibility [T1]

| Requirement | Detail |
|-------------|--------|
| Base period taxable sales | <= JPY 50,000,000 |
| Election | Must submit 消費税簡易課税制度選択届出書 by the day BEFORE the start of the taxable period |

### Deemed Purchase Ratios by Business Type [T1]

| Type | Business Category | Deemed Purchase Ratio |
|------|------------------|----------------------|
| Type 1 | Wholesale | 90% |
| Type 2 | Retail | 80% |
| Type 3 | Manufacturing, mining, construction, agriculture | 70% |
| Type 4 | Other (restaurants, etc.) | 60% |
| Type 5 | Services, transport | 50% |
| Type 6 | Real estate | 40% |

### Computation [T1]

| Step | Action |
|------|--------|
| 5.1 | Calculate output tax on all taxable sales |
| 5.2 | Deemed input tax = Output tax x deemed purchase ratio |
| 5.3 | Tax payable = Output tax - Deemed input tax |

If business spans multiple types, use the type with the highest sales proportion (or weighted average if no single type exceeds 75%).

---

## Step 6: Filing and Payment [T1]

**Legislation:** Consumption Tax Act, Art. 45, 49

| Item | Detail |
|------|--------|
| Filing deadline | March 31 of the following year (sole proprietors) |
| Payment deadline | Same as filing deadline |
| Interim filing | Required if prior-year tax >= JPY 480,000 (quarterly/monthly instalments) |
| Filing method | e-Tax (mandatory for certain businesses) or paper |
| Form | 消費税及び地方消費税の確定申告書 |

### Interim Filing Thresholds [T1]

| Prior-Year Annual Tax | Interim Frequency |
|----------------------|-------------------|
| < JPY 480,000 | None |
| JPY 480,000 -- JPY 4,000,000 | 1 interim (mid-year) |
| JPY 4,000,001 -- JPY 48,000,000 | 3 interim (quarterly) |
| > JPY 48,000,000 | 11 interim (monthly) |

---

## Step 7: Edge Case Registry

### EC1 -- Freelancer newly registered for qualified invoice [T1]
**Situation:** Freelancer with JPY 5M sales registers as qualified invoice issuer starting October 2023. Previously tax-exempt.
**Resolution:** Becomes taxable from registration date. May use the 2割特例 (20% special measure) through periods ending September 2026, paying only 20% of output tax as consumption tax. No need to track actual input tax.

### EC2 -- Mixed standard and reduced rate supplies [T1]
**Situation:** Catering business sells takeout food (8%) and dine-in meals (10%).
**Resolution:** Must separately track and invoice 8% and 10% items. Takeout food = 8%. Dine-in = 10%. Customer's stated intention at time of purchase determines rate.

### EC3 -- Simplified taxation with multiple business types [T2]
**Situation:** Client operates a retail shop (Type 2, 80%) and a consulting practice (Type 5, 50%).
**Resolution:** If one type exceeds 75% of total taxable sales, apply that ratio to all sales. Otherwise, apply each ratio to its respective sales, or use the weighted average. [T2] Flag for reviewer to confirm classification.

### EC4 -- Forgot to submit simplified taxation election [T1]
**Situation:** Client wanted simplified taxation for 2025 but did not submit election form by December 31, 2024.
**Resolution:** Cannot use simplified taxation for 2025. Must use general method. Election takes effect from the FOLLOWING taxable period.

### EC5 -- Export sales and zero-rating [T1]
**Situation:** Freelance designer sells services to a US client.
**Resolution:** Services provided to non-residents and consumed outside Japan are export-exempt (0%). No output tax, but input tax on related purchases is still creditable. Must retain proof of export (contracts, payment records).

### EC6 -- Straddling the JPY 10M threshold [T2]
**Situation:** Base period sales were JPY 9,800,000 but specified period sales were JPY 11,000,000.
**Resolution:** Check specified period wages. If wages also exceed JPY 10M, becomes taxable. If wages <= JPY 10M, may remain tax-exempt despite sales exceeding threshold. [T2] Flag for reviewer.

---

## Step 8: Test Suite

### Test 1 -- Standard freelancer, general method
**Input:** Software developer, taxable sales JPY 15,000,000 (all 10%), taxable purchases JPY 3,000,000 (all 10%), qualified invoices retained.
**Expected output:**
- Output tax: 15,000,000 x 10/110 = JPY 1,363,636
- Input tax: 3,000,000 x 10/110 = JPY 272,727
- Tax payable: 1,363,636 - 272,727 = JPY 1,090,909

### Test 2 -- Simplified taxation, Type 5 (services)
**Input:** Consultant, taxable sales JPY 8,000,000 (all 10%), elected simplified taxation.
**Expected output:**
- Output tax: 8,000,000 x 10/110 = JPY 727,272
- Deemed input: 727,272 x 50% = JPY 363,636
- Tax payable: 727,272 - 363,636 = JPY 363,636

### Test 3 -- 2割特例 (20% special measure)
**Input:** Freelancer registered for invoice system, previously tax-exempt. Sales JPY 6,000,000 (all 10%).
**Expected output:**
- Output tax: 6,000,000 x 10/110 = JPY 545,454
- Tax payable: 545,454 x 20% = JPY 109,090

### Test 4 -- Mixed rate sales
**Input:** Food producer: JPY 5,000,000 retail food sales (8%) + JPY 2,000,000 catering/dine-in (10%).
**Expected output:**
- Output tax (8%): 5,000,000 x 8/108 = JPY 370,370
- Output tax (10%): 2,000,000 x 10/110 = JPY 181,818
- Total output tax: JPY 552,188
- (Input tax calculated separately by method chosen)

### Test 5 -- Below threshold, not registered
**Input:** Freelancer, base period sales JPY 8,000,000, not registered as invoice issuer.
**Expected output:** Tax-exempt business (免税事業者). No consumption tax filing required.

---

## PROHIBITIONS

- NEVER allow input tax credit without a qualified invoice (from October 2023 onward, subject to transitional measures)
- NEVER apply the reduced 8% rate to dine-in meals or alcoholic beverages
- NEVER use simplified taxation without a prior-period election form submission
- NEVER apply simplified taxation if base period sales exceed JPY 50,000,000
- NEVER forget to separate national consumption tax (7.8%/6.24%) from local consumption tax (2.2%/1.76%) on the return
- NEVER allow the 2割特例 for businesses that were already taxable before the invoice system
- NEVER treat export sales as taxable -- they are zero-rated with full input tax credit
- NEVER present calculations as definitive -- always label as estimated and direct client to a qualified 税理士

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 税理士 or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
