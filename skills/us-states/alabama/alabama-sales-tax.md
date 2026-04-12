---
name: alabama-sales-tax
description: Use this skill whenever asked about Alabama sales tax, Alabama use tax, Alabama sales tax nexus, ADOR sales tax filing, self-administered city taxes in Alabama, or Alabama grocery food taxation. Trigger on phrases like "Alabama sales tax", "AL sales tax", "ADOR", "Code of Ala. §40-23", "Alabama local tax", "Alabama grocery tax", "self-administered cities Alabama", or any request involving Alabama state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
version: 2.0
---

# Alabama Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Alabama, United States |
| Jurisdiction code | US-AL |
| Tax type | Sales and Use Tax (state + local) |
| State rate | 4.00% |
| Local rate range | 0% -- 7% (county + city + special district) |
| Maximum combined rate | ~11.00% |
| Sourcing | Destination-based |
| Economic nexus | $250,000 in sales (revenue only) |
| Primary legislation | Code of Alabama §40-23 (Sales Tax); §40-23-60 (Use Tax) |
| Tax authority | Alabama Department of Revenue (ADOR) |
| Filing portal | https://myalabamataxes.alabama.gov |
| SST member | No |
| Self-administered cities | ~200+ cities administer their own local sales tax separately |
| Grocery food | FULLY TAXABLE at state level (reduced to 2% effective Sep 2023) |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

**CRITICAL: Alabama has ~200+ self-administered cities. Sellers must register SEPARATELY with each self-administered city where they have nexus.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Alabama sales tax registration / tax ID? | Required for state filing |
| 2 | Filing frequency? | Monthly, quarterly, annual |
| 3 | Nexus type? | $250K threshold |
| 4 | Marketplace seller? | Facilitators collect on facilitated sales |
| 5 | Products/services sold? | Taxability classification |
| 6 | Sell to exempt entities? | Exemption certificates required |
| 7 | Locations/employees/inventory in AL? | Physical nexus |
| 8 | Sell into multiple local jurisdictions? | Self-administered city complexity |

### Refusal catalogue

**R-AL-1 -- Self-administered city detailed compliance.** Each city has separate registration, returns, and rates. Specific city compliance requires individual research.

---

## Section 3 -- Transaction pattern library

### 3.1 Tangible personal property

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE | Code of Ala. §40-23-2 |
| Clothing and footwear | TAXABLE | No general exemption; holiday exemption only |

### 3.2 Food and beverages

| Pattern | Taxable? | Notes |
|---|---|---|
| Grocery food (unprepared) | TAXABLE at reduced state rate 2% | State rate reduced from 4% to 2% (effective Sep 2023); local rates still apply at full rate |
| Prepared food | TAXABLE at full 4% | |
| Candy, soft drinks | TAXABLE | |

### 3.3 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (physical) | TAXABLE | TPP |
| Canned software (download) | TAXABLE | |
| Custom software | Varies | Escalate to reviewer |
| SaaS (cloud-hosted) | TAXABLE | Alabama taxes SaaS |
| Digital goods (downloads) | TAXABLE | |

### 3.4 Services

| Pattern | Taxable? | Notes |
|---|---|---|
| Most services | NOT TAXABLE | Alabama taxes only enumerated services |
| Rental of TPP | TAXABLE | |
| Amusement/recreation | TAXABLE | |
| Professional services | NOT TAXABLE | |

### 3.5 Exemptions

| Pattern | Status | Notes |
|---|---|---|
| Prescription drugs | EXEMPT | |
| Manufacturing machinery (directly in manufacturing) | REDUCED RATE | State rate 1.5%; local applies |
| Farm equipment | EXEMPT | |
| Resale | EXEMPT | Valid certificate required |
| Interstate commerce | EXEMPT | Shipped out of state |
| Government purchases | EXEMPT | |

---

## Section 4 -- Rate lookup

| Jurisdiction | Approximate combined rate |
|---|---|
| Birmingham | ~10% |
| Montgomery | ~10% |
| Huntsville | ~9% |
| Mobile | ~10% |
| Tuscaloosa | ~9% |

**Use ADOR rate lookup for exact rate by address.**

---

## Section 5 -- Classification rules

### 5.1 Self-administered cities

~200+ Alabama cities self-administer their local sales tax. Sellers must register separately with each. Birmingham, Montgomery, Huntsville, Mobile, Tuscaloosa are all self-administered.

### 5.2 Grocery food reduced rate

State rate on grocery food reduced from 4% to 2% effective September 1, 2023. Local rates apply at full local rate on top.

---

## Section 6 -- Return form and filing

| Level | Return | Portal |
|---|---|---|
| State | Filed via ADOR | https://myalabamataxes.alabama.gov |
| Self-administered cities | Filed separately with each city | Individual city portals |
| ADOR-administered locals | Filed with state return | Same as state |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $250,000 in sales into Alabama |
| Transaction threshold | None |
| Effective date | October 1, 2018 |

### 7.2 Penalties

| Penalty | Rate |
|---|---|
| Late filing | 10% of tax due |
| Fraud | 50% of deficiency |

---

## Section 8 -- Edge cases

### EC1 -- Self-administered city registration

**Situation:** Online seller meets nexus in Alabama.
**Resolution:** Must register with ADOR for state tax. Must ALSO register separately with each self-administered city where nexus exists. ADOR does not administer these cities' taxes.

### EC2 -- Grocery food dual rates

**Situation:** Customer buys groceries in Birmingham.
**Resolution:** State rate 2% on food + full local Birmingham rate. Combined rate on food may be ~8%.

---

## Section 9 -- Test suite

### Test 1 -- Basic sale

**Input:** $1,000 item in Birmingham. Combined rate: ~10%.
**Expected:** Tax = ~$100.

### Test 2 -- Grocery food

**Input:** $200 groceries. State 2% + local ~6%.
**Expected:** Tax = ~$16. Food taxable at reduced state + full local.

### Test 3 -- Economic nexus

**Input:** $300K Alabama sales, no physical presence.
**Expected:** Exceeds $250K. Must register.

---

## Section 10 -- Prohibitions

- NEVER assume Alabama exempts grocery food -- it taxes it (reduced state rate 2% + full local).
- NEVER ignore self-administered cities -- ~200+ cities require separate registration and filing.
- NEVER assume ADOR handles all local taxes -- many cities self-administer.
- NEVER apply one city's local rate to another jurisdiction.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.
