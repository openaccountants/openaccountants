---
name: washington-sales-tax
description: Use this skill whenever asked about Washington State sales and use tax, WA DOR filings, B&O tax overview, Washington digital goods tax, Washington exemptions, Washington nexus, or any request involving Washington state sales and use tax compliance. Trigger on phrases like "Washington sales tax", "WA sales tax", "Washington DOR", "B&O tax", "Washington use tax", "Washington digital goods", "Washington resale certificate", or any request involving Washington sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Washington sales tax work.
version: 2.0
---

# Washington State Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Washington, United States |
| Jurisdiction code | US-WA |
| Tax type | Sales and Use Tax + Business and Occupation (B&O) Tax (separate) |
| State sales tax rate | 6.5% |
| Local add-on range | 0.5% -- 4.0% |
| Maximum combined rate | ~10.25% (parts of Seattle and Tacoma) |
| Sourcing | Destination-based for ALL sales (SST rules) |
| Economic nexus | $100,000 in gross receipts (revenue only) |
| Primary legislation | RCW Chapter 82.08 (Sales); 82.12 (Use); 82.04 (B&O) |
| Tax authority | Washington State Department of Revenue (DOR) |
| Filing portal | https://dor.wa.gov |
| SST member | Yes -- full member |
| Return form | Combined Excise Tax Return (covers sales tax + B&O + use tax) |
| Vendor discount | None |
| No state income tax | Correct -- B&O tax is primary business tax |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

**CRITICAL: Washington taxes virtually ALL digital products, including SaaS, streaming, and custom software delivered electronically. Broadest digital tax regime in the US.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Washington UBI number? | Required for filing |
| 2 | Assigned filing frequency? | Monthly, quarterly, annual |
| 3 | Nexus type? | $100K gross receipts threshold |
| 4 | Sell through marketplace facilitators? | Facilitators collect on facilitated sales |
| 5 | Sell digital products, SaaS, or streaming? | WA taxes virtually ALL digital products |
| 6 | Sell custom software? | WA taxes custom software delivered electronically |
| 7 | Understand B&O tax obligations? | B&O applies IN ADDITION to sales tax |
| 8 | Primary delivery/sales location? | WA is destination-based; hundreds of local rates |

### Refusal catalogue

**R-WA-1 -- B&O tax detailed compliance.** B&O tax has its own classifications and rates. Outside scope for detailed B&O filing.

**R-WA-2 -- Cannabis taxation.** 37% excise tax plus sales tax. Complex regime. Escalate.

**R-WA-3 -- Capital gains tax.** Enacted 2021. Outside scope.

---

## Section 3 -- Transaction pattern library

### 3.1 Tangible personal property

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE | RCW 82.08.020 |
| Clothing and footwear | TAXABLE | NO clothing exemption |
| Motor vehicles | TAXABLE | Plus separate excise taxes |

### 3.2 Food and beverages

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food (unprepared, home consumption) | EXEMPT | RCW 82.08.0293 |
| Prepared food (heated, with utensils, mixed ingredients) | TAXABLE | RCW 82.08.0293(2) |
| Candy (SST definition: no flour) | TAXABLE | RCW 82.08.0293(2)(d) |
| Soft drinks | TAXABLE | RCW 82.08.0293(2)(e) |
| Dietary supplements | TAXABLE | RCW 82.08.0293(2)(f) |
| Bottled water (plain, non-carbonated) | EXEMPT | |
| Alcoholic beverages | TAXABLE | Plus liquor taxes |

### 3.3 SaaS and digital goods -- BROADLY TAXED

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (any delivery) | TAXABLE | RCW 82.04.050(6)(a) |
| Custom software (electronic delivery) | TAXABLE | Unlike most states -- WA taxes this |
| SaaS (cloud-hosted) | TAXABLE | Digital automated service; RCW 82.04.050(6)(b) |
| Digital music/movies/books | TAXABLE | Digital goods |
| Streaming services | TAXABLE | Digital automated service |
| Digital codes | TAXABLE | RCW 82.04.050(6)(c) |
| Remote access software | TAXABLE | Digital automated service |

### 3.4 Services

| Pattern | Taxable? | Notes |
|---|---|---|
| Digital automated services | TAXABLE | RCW 82.04.050(6)(b) |
| Extended warranties/service contracts | TAXABLE | RCW 82.04.050(7) |
| Physical fitness services | TAXABLE | RCW 82.04.050(2)(a) |
| Amusement/recreation | TAXABLE | |
| Professional services (legal, accounting, consulting, medical) | NOT TAXABLE (sales tax) | Subject to B&O tax only |
| Landscape maintenance | NOT TAXABLE (sales tax) | B&O only |

### 3.5 Exemptions

| Pattern | Status | Citation |
|---|---|---|
| Grocery food | EXEMPT | RCW 82.08.0293 |
| Prescription drugs | EXEMPT | RCW 82.08.0281 |
| OTC drugs | TAXABLE | No OTC exemption |
| Agricultural machinery | EXEMPT | RCW 82.08.0268 |
| Manufacturing M&E | PARTIAL EXEMPTION | RCW 82.08.02565 -- local tax exempt, state may apply |
| Resale (WA Resale Certificate) | EXEMPT | RCW 82.08.030(1) |
| Interstate commerce | EXEMPT | RCW 82.08.0273 |
| Government purchases | EXEMPT | RCW 82.08.0255 |
| Trade-in value | EXEMPT | RCW 82.08.010(1)(c) |
| Newspapers (print) | EXEMPT | RCW 82.08.0253 |

---

## Section 4 -- Rate lookup

### 4.1 Key combined rates

| Jurisdiction | Combined rate |
|---|---|
| Seattle | ~10.25% |
| Tacoma | ~10.20% |
| Spokane | ~8.90% |
| Vancouver (Clark County) | ~8.60% |
| Olympia | ~9.00% |
| Unincorporated King County | ~10.10% |

### 4.2 Sourcing

| Scenario | Rate applied |
|---|---|
| All sales (shipped, counter, intrastate, interstate) | Destination-based |

**Use DOR rate lookup: https://dor.wa.gov/taxes-rates/sales-use-tax-rates**

---

## Section 5 -- Classification rules

### 5.1 General rule

All retail sales of TPP and enumerated services taxable unless exempted. RCW 82.08.020. Digital products taxed very broadly.

### 5.2 B&O tax dual obligation

A retail business owes BOTH sales tax (from customer) AND B&O tax (on gross receipts). B&O cannot be passed to customer as a separate line item.

### 5.3 B&O rates (context only)

| Classification | Rate |
|---|---|
| Retailing | 0.471% |
| Wholesaling | 0.484% |
| Manufacturing | 0.484% |
| Service | 1.50% |

---

## Section 6 -- Return form and filing

### 6.1 Forms

| Form | Use |
|---|---|
| Combined Excise Tax Return | Covers sales tax, B&O, use tax, other excise taxes |

Filed through **My DOR** (online portal).

### 6.2 Due dates

| Frequency | Due date |
|---|---|
| Monthly | 25th of following month |
| Quarterly | April 25, July 25, October 25, January 25 |
| Annual | April 15 |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $100,000 in gross receipts |
| Transaction threshold | None |
| Measurement period | Current or preceding calendar year |
| Effective date | October 1, 2018 |
| Sales included | Gross receipts including exempt sales |
| Authority | RCW 82.08.020; RCW 82.04.067 |

### 7.2 Marketplace facilitator

| Rule | Detail |
|---|---|
| Effective date | January 1, 2018 (pre-Wayfair, one of earliest) |
| Authority | RCW 82.08.0531 |

### 7.3 Penalties

| Penalty | Rate |
|---|---|
| Late filing | 5%/month (max 25%) |
| Substantial underpayment | 5% |
| Evasion/fraud | 50% |

### 7.4 Record retention

5 years from filing or due date.

### 7.5 Statute of limitations

| Scenario | Period |
|---|---|
| Standard | 4 years |
| No return | Unlimited |
| Fraud | Unlimited |

---

## Section 8 -- Edge cases

### EC1 -- B&O plus sales tax

**Situation:** $1,000 sale in Seattle.
**Resolution:** Collect ~$102.50 sales tax from customer. ALSO pay B&O ($1,000 x 0.471% = $4.71). B&O is retailer's own obligation.

### EC2 -- SaaS (digital automated service)

**Situation:** WA business subscribes to cloud HR platform. $100/month.
**Resolution:** TAXABLE. Sales tax at combined rate.

### EC3 -- Custom software taxable

**Situation:** Business pays $20,000 for custom software, delivered electronically.
**Resolution:** TAXABLE in WA (unlike most states). RCW 82.04.050(6)(a).

### EC4 -- Destination-based sourcing

**Situation:** Seattle retailer ships to Spokane customer.
**Resolution:** Charge Spokane rate (~8.90%), not Seattle rate (~10.25%).

### EC5 -- No vendor discount

**Situation:** Retailer asks about collection allowance.
**Resolution:** Washington does NOT offer a vendor discount. Sellers retain no portion.

---

## Section 9 -- Test suite

### Test 1 -- Basic sale in Seattle

**Input:** $1,000 laptop. Rate: 10.25%.
**Expected:** Tax = $102.50.

### Test 2 -- Grocery exempt

**Input:** $200 groceries.
**Expected:** Tax = $0.

### Test 3 -- SaaS taxable

**Input:** $300/month cloud HR. Spokane rate: 8.90%.
**Expected:** Tax = $26.70/month.

### Test 4 -- Economic nexus

**Input:** Oregon seller, $120K WA sales.
**Expected:** Exceeds $100K. Must register.

### Test 5 -- Destination-based

**Input:** Seattle retailer ships $500 to Vancouver, WA. Rate: 8.60%.
**Expected:** Tax = $43.00.

### Test 6 -- Candy taxable (SST)

**Input:** $5 chocolate bar (no flour) in Tacoma. Rate: 10.20%.
**Expected:** Tax = $0.51.

### Test 7 -- Clothing taxable

**Input:** $300 jacket in Seattle. Rate: 10.25%.
**Expected:** Tax = $30.75.

### Test 8 -- Extended warranty

**Input:** $50 warranty in Seattle. Rate: 10.25%.
**Expected:** Tax = $5.13.

### Test 9 -- Use tax

**Input:** Seattle business buys $3,000 from Oregon retailer. No tax collected. Rate: 10.25%.
**Expected:** Use tax = $307.50.

### Test 10 -- Custom software

**Input:** $20,000 custom software delivered electronically. Seattle.
**Expected:** Tax = $2,050.

---

## Section 10 -- Prohibitions

- NEVER apply a clothing exemption -- clothing is fully taxable.
- NEVER treat SaaS or digital automated services as nontaxable -- WA taxes digital products very broadly.
- NEVER assume custom software is exempt -- WA taxes custom software delivered electronically.
- NEVER forget B&O tax applies IN ADDITION to sales tax.
- NEVER use origin-based sourcing -- WA is destination-based for ALL sales.
- NEVER assume no vendor discount means no filing obligation.
- NEVER forget candy and soft drinks are taxable (SST definitions).
- NEVER refuse SST certificates -- WA is an SST member.
- NEVER treat OTC drugs as exempt.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.
