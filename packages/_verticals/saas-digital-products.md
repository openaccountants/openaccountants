---
name: saas-digital-products
description: "Use this skill whenever a SaaS company, digital platform, app developer, marketplace, or other digital-product business asks about sector-specific tax / accounting / cross-border issues. Trigger on phrases like \"SaaS revenue recognition\", \"ASC 606 SaaS\", \"IFRS 15 SaaS\", \"subscription revenue\", \"ARR\", \"MRR\", \"deferred revenue\", \"termed license vs subscription\", \"ASC 985-20 software\", \"SaaS sales tax US\", \"Wayfair nexus SaaS\", \"EU OSS digital services\", \"marketplace facilitator\", \"permanent establishment server\", \"EU place of supply digital\", \"EU MOSS\", \"VAT digital services B2C\", \"GST low-value imported services\", \"US state sales tax SaaS\", \"MTD VAT SaaS UK\", or any SaaS-specific tax / accounting question. Covers IFRS 15 / ASC 606 SaaS revenue recognition, US state sales tax SaaS nexus (Wayfair post-2018), EU OSS / IOSS for digital services to consumers, EU VAT place of supply for cross-border B2B/B2C SaaS, Australia GST low-value imported services, India OIDAR / Equalisation Levy, Canada digital service GST/HST. Does NOT cover: software development methodology, app store revenue share economics, SOC 2 / ISO 27001 audit procedures."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SAAS Digital Products

## What this file is

A sector overlay for SaaS, digital platforms, app developers, marketplaces, and other digital-product businesses.

## Section 1 — Revenue recognition (IFRS 15 / ASC 606)

### 1.1 Five-step model

- **Five-step revenue recognition model** — 1. Identify the contract with a customer 2. Identify the performance obligations 3. Determine the transaction price 4. Allocate the price to the performance obligations 5. Recognise revenue when each performance obligation is satisfied  _([T1])_

### 1.2 Key SaaS issues

**Key SaaS issues table**

| Topic | Treatment |
| --- | --- |
| **Subscription / SaaS access** | Generally one performance obligation, satisfied over time (stand-ready obligation) — straight-line revenue over the term |
| **Implementation services** | Distinct (separate PO) only if customer can benefit from the SaaS without them; otherwise combined and recognised over the SaaS term |
| **Right of use license vs hosted service** | If the customer has a right to use the underlying software (e.g., download), revenue at point in time; if hosted, recognise over the contract term (stand-ready) |
| **Setup fees / activation fees** | Combine with subscription if not distinct; recognise over the customer's expected life |
| **Discounts and ramps** | Allocate to all POs proportionately, not just to specific period |
| **Variable consideration** | Constrain to amount unlikely to require significant reversal; commonly estimated for usage-based |
| **Customer acquisition costs (commissions)** | Capitalise per IFRS 15 ¶91-94 / ASC 340-40; amortise over expected customer life (often longer than contract term) |
| **Hosting agreement under SaaS arrangement (customer-side accounting)** | Cloud Computing Arrangement (CCA) — generally expensed as incurred; ASU 2018-15 allows capitalisation of certain implementation costs aligned to ASC 350-40 |

### 1.3 Examples of common SaaS issues

**[T1] Multi-year contract with discount in year 1:**
Contract: 3 years; $100k year 1, $150k years 2 and 3. Total $400k.
- Straight-line allocation: $133k/yr recognised
- Year 1 deferred revenue $33k; recognised in years 2/3

**[T1] SaaS + implementation services:**
- If implementation specific to SaaS and customer can't benefit without it → one PO, recognise both over SaaS contract term
- If implementation could be sold separately and customer can use other vendors → separate POs, implementation recognised on completion

## Section 2 — US state sales tax on SaaS (post-Wayfair)

- **South Dakota v. Wayfair (2018)** — Overturned the physical presence test for sales tax nexus. Economic nexus now applies — typically $100,000 in sales or 200 transactions to the state.  _([T1])_

### 2.1 SaaS taxability by state (sample)

**SaaS taxability by state (sample)**

| State | SaaS taxable? | Notes |
| --- | --- | --- |
| **California** | No (generally) — service not tangible personal property | But certain "canned software" downloads taxable |
| **New York** | Yes — sales tax on SaaS to NY customers since 2010 |  |
| **Texas** | Yes — "data processing service" since 1980s; 20% exemption under §151.351 |  |
| **Florida** | No — service, not tangible |  |
| **Washington** | Yes — Retail Sales Tax + B&O Tax |  |
| **Illinois** | Generally no for SaaS but specific products taxable |  |
| **Pennsylvania** | Yes — Sales and Use Tax on "computer services" |  |
| **Massachusetts** | Yes if "prewritten" but no if customer-specific |  |
| **Ohio** | Yes if "electronic information services" |  |
| **Virginia** | No — service |  |
| **Tennessee** | Yes — Telecommunication Sales Tax also applies |  |
| **Georgia** | No — service |  |
| **North Carolina** | Yes — "digital codes" but SaaS itself contested |  |

- **Marketplace facilitator laws** — Most states require marketplaces (Amazon, Etsy, etc.) to collect on behalf of sellers above thresholds.  _([T1])_

## Section 3 — EU VAT for digital services

### 3.1 Place of supply

- **Article 58 PVD** — B2C electronic services: place of supply is where the customer is established / has permanent address / usually resides. B2B electronic services: place of supply is where the customer is established (reverse charge).  _([T1] Article 58 PVD)_

### 3.2 OSS (One-Stop-Shop) and IOSS (Import OSS)

- **Union OSS** — EU established supplier registers in home MS, declares all B2C cross-border EU sales of services + intra-EU B2C distance sales of goods  _([T1])_
- **Non-Union OSS** — Non-EU supplier registers in chosen MS for B2C EU electronic services  _([T1])_
- **IOSS** — Import OSS for goods ≤ EUR 150 imported into EU  _([T1])_

### 3.3 VAT rates by country

Country-specific. For digital services to consumers, the destination MS rate applies. See country VAT skills.

## Section 4 — Other major SaaS VAT/GST regimes

### 4.1 United Kingdom

- **UK post-Brexit VAT regime** — Post-Brexit, UK applies own VAT regime: Same place-of-supply rules as EU but UK-specific; VAT on Electronic Services (VOES) registration for non-UK suppliers; Standard rate 20%  _([T1])_

### 4.2 Australia — GST low-value imported services

- **Australia GST low-value imported services** — Since 1 July 2017 (digital services) and 1 July 2018 (goods ≤ AUD 1,000): Non-resident suppliers must register and collect 10% GST on supplies to Australian consumers if turnover ≥ AUD 75k; B2B reverse charge  _([T1])_

### 4.3 Canada — GST/HST on digital products

- **Canada GST/HST on digital products** — Since 1 July 2021: Non-resident suppliers register and collect GST/HST on B2C digital services if Canadian sales ≥ CAD 30k; Provincial PST/RST/QST may also apply (BC, MB, QC)  _([T1])_

### 4.4 India — OIDAR + Equalisation Levy

- **OIDAR (Online Information Database Access or Retrieval)** — Services to Indian consumers — non-resident supplier registers and collects GST (18%)  _([T1])_
- **Equalisation Levy 2.0** — 6% on advertising income (the 2% e-commerce levy was repealed 1 August 2024)  _([T1])_

### 4.5 Other notable

- **New Zealand** — 15% GST on remote digital services from non-residents (since 2016)
- **Singapore** — 9% GST on B2C digital services from non-residents (raised from 7% in 2024)
- **Japan** — 10% consumption tax on B2C digital services
- **South Korea** — 10% VAT on B2C digital services
- **Mexico** — 16% VAT on digital services from non-residents (since 2020)
- **Chile** — 19% VAT on digital services
- **Argentina** — 21% VAT plus 8% withholding on digital services

## Section 5 — Permanent establishment risk for SaaS

OECD Model Article 5 — physical presence threshold. Pure SaaS without local server typically does not create PE. Risk areas:
- Dependent agents soliciting business
- Customer success / support staff in country
- Co-located servers (Article 5 commentary: server can be a PE if customised, owned, and CIGAs performed there)
- Marketing / sales offices

- **BEPS Action 1 / digital PE** — OECD Pillar One Amount A would create a new taxing right for "market jurisdictions" — pending ratification. DSTs continue in 25+ countries (see digital-services-tax-matrix.md).  _([T1])_

## Section 6 — IFRS 15 / ASC 606 acquisition cost capitalisation

- **Sales commission capitalisation** — Sales commissions paid on customer acquisition: - Capitalise if incremental and recoverable (IFRS 15 ¶91-94 / ASC 340-40) - Amortise over the expected customer life (often longer than initial contract — including expected renewals) - Practical expedient: expense if amortisation period < 1 year This typically generates a significant balance sheet asset for high-growth SaaS companies.  _([T1])_

## Section 7 — SaaS-specific KPIs interaction with accounting

**[T1] Non-GAAP / management measures:**

**SaaS-specific KPIs table**

| Metric | Definition | Accounting interaction |
| --- | --- | --- |
| **MRR / ARR** | Monthly / annual recurring revenue | Often gross; differs from GAAP revenue (which is subscription net of discounts, recognised over time) |
| **Bookings** | New contract value signed | Pre-recognition |
| **Deferred revenue** | Cash received before service delivered | Balance sheet liability under ASC 606 / IFRS 15 |
| **RPO (Remaining Performance Obligations)** | Contractually committed future revenue | ASC 606 ¶54 / IFRS 15 ¶120 disclosure |
| **Customer churn / NRR (Net Revenue Retention)** | Customer departures and expansions | Drives expected customer life for commission amortisation |
| **CAC (Customer Acquisition Cost)** | Total sales+marketing ÷ new customers | Forms basis of LTV/CAC ratio |
| **LTV (Lifetime Value)** | Gross margin × expected customer life | Critical for impairment testing |

## Section 8 — Self-checks

- [ ] Revenue recognition timing matches IFRS 15 / ASC 606 — over time for hosted SaaS
- [ ] Implementation services tested for distinct PO status
- [ ] Setup fees combined or separated per distinct test
- [ ] Multi-year contracts allocated for ramps and discounts
- [ ] Customer acquisition costs capitalised and amortised per expected customer life
- [ ] US state sales tax registration where economic nexus thresholds met
- [ ] EU OSS / IOSS registration if cross-border B2C
- [ ] Non-EU VAT registration (UK, Australia, Canada, India OIDAR, Singapore, Japan, Korea, Mexico, Chile)
- [ ] DST exposure assessed per `digital-services-tax-matrix.md`
- [ ] PE risk assessed for any country with local employees / customer-facing roles
- [ ] Deferred revenue reconciled to bookings and contract value
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 9 — Disclaimer

SaaS sector taxation involves substantial cross-border complexity. Outputs must be reviewed by credentialed practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
