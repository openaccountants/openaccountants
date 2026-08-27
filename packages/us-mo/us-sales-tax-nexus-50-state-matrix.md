---
name: us-sales-tax-nexus-50-state-matrix
description: Tier 2 US federal-level reference skill providing the post-Wayfair economic-nexus threshold table for every US state plus DC and Puerto Rico. Covers sales/transaction thresholds, effective dates, lookback periods, marketplace facilitator laws, the SaaS-taxability list (HI/MA/NY/OH/PA/RI/SC/TN/TX/UT/WA/WV), the no-sales-tax NOMAD states (NH/OR/MT/AK/DE), Amazon FBA physical-presence nexus through inventory in 3PL warehouses, the difference between sales-tax and income-tax nexus, voluntary disclosure agreement (VDA) lookback limits, and home-rule states (CO/AL/LA/AK) requiring separate local registrations. Tax year 2025.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US Sales Tax Nexus 50 State Matrix

## 1. Scope

This reference skill is the single lookup table for **economic sales tax nexus** thresholds in every US jurisdiction with a sales-and-use tax (SUT), gross receipts tax (GRT), or transaction privilege tax (TPT) regime: all 45 states with statewide sales tax, the District of Columbia, Puerto Rico, plus notes on the 5 "NOMAD" states (NH, OR, MT, AK, DE) and the home-rule local-only nexus that exists in Alaska despite the absence of a state-level tax.

**This skill covers:**
- Wayfair-era economic nexus thresholds (dollar + transaction count, AND/OR logic, lookback windows)
- Marketplace facilitator laws (Amazon, eBay, Etsy, Walmart Marketplace, Shopify, Patreon, OnlyFans)
- Physical-presence nexus traps — especially **Amazon FBA inventory** in third-party 3PL warehouses (the single most common audit-flash point for small e-commerce sellers)
- SaaS / digital-product taxability list at the state level (HI, MA, NY, OH, PA, RI, SC, TN, TX, UT, WA, WV — the "SaaS-taxable twelve")
- Home-rule states (CO, AL, LA, AK) requiring separate local registrations
- Streamlined Sales Tax (SST) member-state program and Certified Service Provider (CSP) free-filing option
- Voluntary Disclosure Agreement (VDA) lookback limits and audit exposure
- P.L. 86-272 distinction (income tax nexus only — does NOT shield from sales tax nexus)

**This skill does NOT cover:**
- State income tax nexus — see `us-pl-86-272-income-tax-nexus`
- Income tax for businesses generally — see `us-form-1120-c-corp`, `us-form-1065-partnership`, `us-sole-prop-bookkeeping`
- Arizona TPT mechanics — see `az-tpt`
- Colorado SUTS portal — see `co-suts`
- Washington B&O — see `wa-bo-tax`
- California sales tax line-level preparation — see `california-sales-use-tax`
- Texas sales tax line-level preparation — see `tx-sales-tax`
- US federal income tax — see other Tier 2 skills in this package
- Use tax on consumer purchases (these are 50 separate compliance projects for individual taxpayers)

## 2. Background — South Dakota v. Wayfair, Inc. (2018)

### 2.1. Pre-Wayfair: Quill physical-presence rule

- **Quill physical-presence rule** — For decades, *Quill Corp. v. North Dakota*, 504 U.S. 298 (1992) held that the Commerce Clause's "dormant" component prohibited states from compelling a remote seller to collect sales tax unless the seller had **physical presence** in the state (employees, offices, inventory, agents, real estate). Mail-order and early e-commerce sellers exploited this to sell into 49 states while only collecting in their home state, costing states an estimated $20–30 billion/year in uncollected revenue by 2017.  _(Quill Corp. v. North Dakota, 504 U.S. 298 (1992))_

### 2.2. Wayfair holding (June 21, 2018)

- **Wayfair holding** — In South Dakota v. Wayfair, Inc., the Supreme Court (5-4, Kennedy writing for the majority) overruled Quill and held that physical presence is no longer required for Commerce Clause nexus. The Court approved South Dakota's economic-nexus statute (SB 106, 2016), which imposed collection obligations on remote sellers with either $100,000+ in gross sales into South Dakota in the current or prior calendar year, OR 200+ separate transactions into South Dakota in the current or prior calendar year. The Court emphasized four features as constitutionally adequate safe harbors: 1) A safe-harbor threshold below which small sellers are exempt; 2) No retroactive application of the obligation; 3) Streamlined Sales Tax (SST) membership reducing compliance burden; 4) Free or low-cost filing software (Certified Service Providers — CSPs).  _(South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018))_

### 2.3. Aftermath — the 18-month stampede

Within 18 months of Wayfair, every state with a sales tax enacted some form of economic nexus statute. The "Wayfair standard" of $100,000 / 200 transactions became the de facto template, though many states have since dropped the transaction count, raised the dollar threshold, or modified the AND/OR logic.

- **First wave (July 2018 – Dec 2018):** ~25 states activated economic nexus the week after Wayfair (some via existing statutes triggered by the ruling). KY, IA, IN, MI, ND, MS, MN, ME, OK, SD, VT, WA, WI.
- **Second wave (Jan 2019 – Dec 2019):** Remaining ~20 states phased in.
- **Stragglers:** FL (effective July 1, 2021) and MO (effective Jan 1, 2023) were the last two to adopt economic nexus. MO closed the final gap.

### 2.4. Three nexus types coexist

- **Three nexus types** — Wayfair did NOT replace physical-presence nexus — it added economic nexus as an additional trigger. The full taxonomy is: 1. Physical-presence nexus (still alive) — inventory, employees, offices, real property, sales reps, contractors providing services, attending trade shows (some states), affiliates (clickthrough nexus in some states). 2. Economic nexus (post-Wayfair) — sales-volume or transaction-count thresholds. 3. Marketplace facilitator nexus (post-2018) — Amazon, eBay, Etsy, Walmart Marketplace, etc. collect and remit on behalf of third-party sellers in nearly every state.

## 3. The NOMAD states — no statewide sales tax

**NOMAD states table**

| State | Status | Notes |
| --- | --- | --- |
| **N**ew Hampshire | No SUT | Has 8.5% meals & rooms tax; no broader SUT. No economic nexus issues. |
| **O**regon | No SUT | Has Corporate Activity Tax (CAT) — gross-receipts-based, not retail sales — at $1M threshold. No retail SUT obligation. |
| **M**ontana | No SUT | Has limited local resort taxes in tourist towns (e.g. Whitefish, West Yellowstone) but no statewide SUT. |
| **A**laska | No state SUT | **BUT** numerous localities impose sales tax and have organized the **Alaska Remote Seller Sales Tax Commission (ARSSTC)** with statewide economic nexus thresholds — see §4 below. **Audit flash point.** |
| **D**elaware | No SUT | Has Gross Receipts Tax on businesses (not consumer-facing); no retail SUT. |

> **AUDIT FLASH POINT — Alaska is NOT a free zone.** Sellers routinely overlook that ~100 Alaska municipalities and boroughs (Juneau, Anchorage Borough excepted, Ketchikan Gateway Borough, Sitka, Wasilla, Kodiak, Bethel, Cordova, Nome, etc.) have local SUT. ARSSTC was formed in 2020 to administer economic-nexus collection across member jurisdictions. The collective threshold is **$100,000 of statewide gross sales** in the prior calendar year (the 200-transaction prong was repealed effective Jan 1, 2025). Remote sellers register **once** with ARSSTC and file a single consolidated return covering all member munis.

## 4. The 50-State + DC + PR Economic Nexus Matrix

- **Matrix definitions** — - **Sales threshold** — gross sales of tangible personal property + taxable services into the state. Most states include exempt/wholesale sales in the threshold computation but a few (e.g. CA, NY) measure on retail sales only. See "Wholesale included?" column. - **Transaction threshold** — number of separate sales transactions into the state. - **AND / OR** — whether both thresholds must be crossed (AND) or either one triggers nexus (OR). - **Lookback** — measurement period. "PY" = prior calendar year; "CY" = current calendar year; "PY or CY" = the more common "either" formulation; "rolling 12" = trailing 12 months. - **MPF date** — Marketplace Facilitator law effective date. - **State rate** — statewide rate only; combined rate with local averages much higher in most states. - **Wholesale included?** — whether wholesale/exempt/resale sales count toward the threshold.

### 4.1. Alphabetical matrix — economic nexus rules

**Alphabetical matrix — economic nexus rules**

| # | State | Effective | Sales $ Threshold | Trans # | AND/OR | Lookback | MPF date | State rate | Wholesale incl.? | Notable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Alabama** | 1 Oct 2018 | $250,000 | — | — (sales only) | PY | 1 Jan 2019 | 4.00% | Retail only | Home-rule munis; SSUT program; 50+ self-administered locals |
| 2 | **Alaska** (ARSSTC) | 1 Jan 2020 (varies by muni) | $100,000 | — (200 prong repealed 2025) | — (sales only) | PY | varies by muni | 0% state; 1–7.5% local | Yes | No state SUT; muni-level via ARSSTC |
| 3 | **Arizona** (TPT) | 1 Oct 2019 | $100,000 | — | — (sales only) | PY or CY | 1 Oct 2019 | 5.60% (TPT) | Retail only | TPT is on seller, passed to buyer; see `az-tpt` |
| 4 | **Arkansas** | 1 Jul 2019 | $100,000 | 200 | OR | PY or CY | 1 Jul 2019 | 6.50% | Yes | Standard SST template |
| 5 | **California** | 1 Apr 2019 | $500,000 | — (200 prong eliminated Apr 2019) | — (sales only) | PY or CY | 1 Oct 2019 | 7.25% (highest base) | Retail only | District tax separately measured at $500k statewide |
| 6 | **Colorado** | 1 Jun 2019 | $100,000 | — (200 prong dropped Apr 2020) | — (sales only) | PY or CY | 1 Oct 2019 | 2.90% (lowest state base) | Yes | 70+ home-rule cities via SUTS portal; see `co-suts` |
| 7 | **Connecticut** | 1 Dec 2018 | $100,000 | 200 | AND | PY (12 mo. ending 9/30) | 1 Dec 2018 | 6.35% | Retail | **AND** logic is uncommon — both must be met |
| 8 | **Delaware** | — | — | — | — | — | — | 0% (no SUT) | — | NOMAD; gross-receipts tax on businesses only |
| 9 | **District of Columbia** | 1 Apr 2019 | $100,000 | 200 | OR | PY or CY | 1 Apr 2019 | 6.00% | Retail | Standard Wayfair template |
| 10 | **Florida** | 1 Jul 2021 | $100,000 | — | — (sales only) | PY | 1 Jul 2021 | 6.00% | Retail only | Late adopter; no transaction count prong |
| 11 | **Georgia** | 1 Jan 2019 (lowered Jan 2020) | $100,000 | 200 | OR | PY or CY | 1 Apr 2020 | 4.00% | Retail | Reduced from $250k to $100k in 2020 |
| 12 | **Hawaii** (GET) | 1 Jul 2018 | $100,000 | 200 | OR | PY or CY | 1 Jan 2020 | 4.00% (GET) | Yes (gross receipts) | GET not SUT — taxes seller on gross income; passed through to buyer |
| 13 | **Idaho** | 1 Jun 2019 | $100,000 | — | — (sales only) | PY or CY | 1 Jun 2019 | 6.00% | Yes | No transaction count |
| 14 | **Illinois** | 1 Oct 2018 | $100,000 | 200 | OR | PY (rolling 12) | 1 Jan 2020 | 6.25% (ROT) | Retail | ROT vs UT distinction; destination-sourcing reforms 2025 |
| 15 | **Indiana** | 1 Oct 2018 | $100,000 | — (200 prong repealed Jan 2024) | — (sales only) | PY or CY | 1 Jul 2019 | 7.00% | Yes | Transaction count repealed effective 2024 |
| 16 | **Iowa** | 1 Jan 2019 | $100,000 | — (200 prong repealed Jul 2019) | — (sales only) | PY or CY | 1 Jan 2019 | 6.00% | Yes | Transaction count repealed |
| 17 | **Kansas** | 1 Jul 2021 (clarified) | $100,000 | — | — (sales only) | PY or CY | 1 Jul 2021 | 6.50% | Yes | **Was $0 threshold 2019-2021** — now $100k post-SB 50 (effective Jul 2021) |
| 18 | **Kentucky** | 1 Oct 2018 | $100,000 | 200 | OR | PY or CY | 1 Jul 2019 | 6.00% | Retail | Standard template |
| 19 | **Louisiana** | 1 Jul 2020 | $100,000 | 200 | OR | PY or CY | 1 Jul 2020 | 4.45% | Retail | 64 parishes file separately (limited LSST progress) |
| 20 | **Maine** | 1 Jul 2018 | $100,000 | — (200 prong repealed Jan 2022) | — (sales only) | PY or CY | 1 Oct 2019 | 5.50% | Retail | Transaction count repealed |
| 21 | **Maryland** | 1 Oct 2018 | $100,000 | 200 | OR | PY or CY | 1 Oct 2019 | 6.00% | Retail | Digital products taxable since 2021 |
| 22 | **Massachusetts** | 1 Oct 2017 ("cookie nexus") / 1 Oct 2019 (Wayfair) | $100,000 | — (no transaction count) | — (sales only) | PY | 1 Oct 2019 | 6.25% | Retail | Cookie-nexus regs predated Wayfair; SaaS taxable |
| 23 | **Michigan** | 1 Oct 2018 | $100,000 | 200 | OR | PY | 1 Jan 2020 | 6.00% | Yes | Standard template |
| 24 | **Minnesota** | 1 Oct 2018 (small-seller exception expanded Oct 2019) | $100,000 | 200 | OR | PY (12 mo) | 1 Oct 2018 | 6.875% | Retail | SST member |
| 25 | **Mississippi** | 1 Sep 2018 | $250,000 | — | — (sales only) | PY (12 mo) | 1 Jul 2020 | 7.00% (highest base) | Yes | Higher dollar threshold |
| 26 | **Missouri** | 1 Jan 2023 | $100,000 | — | — (sales only) | PY (12 mo rolling, measured quarterly) | 1 Jan 2023 | 4.225% | Retail | **Final state to adopt** economic nexus |
| 27 | **Nebraska** | 1 Apr 2019 | $100,000 | 200 | OR | PY or CY | 1 Apr 2019 | 5.50% | Yes | SST member |
| 28 | **Nevada** | 1 Oct 2018 | $100,000 | 200 | OR | PY or CY | 1 Oct 2019 | 6.85% | Retail | SST member |
| 29 | **New Hampshire** | — | — | — | — | — | — | 0% (no SUT) | — | NOMAD |
| 30 | **New Jersey** | 1 Nov 2018 | $100,000 | 200 | OR | PY or CY | 1 Nov 2018 | 6.625% | Retail | SST member |
| 31 | **New Mexico** (GRT) | 1 Jul 2019 | $100,000 | — | — (sales only) | PY (12 mo) | 1 Jul 2019 | 4.875% (GRT) | Yes | GRT regime — tax on seller, passed through |
| 32 | **New York** | 21 Jun 2018 (immediately on Wayfair) | $500,000 AND 100 | 100 | AND | Prior 4 quarters | 1 Jun 2019 | 4.00% (state) | Retail | **AND** logic; lower transaction count than most |
| 33 | **North Carolina** | 1 Nov 2018 | $100,000 | — (200 prong repealed Jul 2024) | — (sales only) | PY or CY | 1 Feb 2020 | 4.75% | Yes | Transaction count repealed 2024 |
| 34 | **North Dakota** | 1 Oct 2018 | $100,000 | — (200 prong repealed Jul 2019) | — (sales only) | PY or CY | 1 Oct 2019 | 5.00% | Retail | SST member |
| 35 | **Ohio** | 1 Aug 2019 | $100,000 | 200 | OR | PY or CY | 1 Sep 2019 | 5.75% (CAT base — SUT is separate) | Yes | Plus Commercial Activity Tax (CAT) at $150k bright-line |
| 36 | **Oklahoma** | 1 Jul 2018 (notice-or-collect) / 1 Nov 2019 | $100,000 | — | — (sales only) | PY (12 mo) | 1 Nov 2019 | 4.50% | Retail | Early notice-and-report law |
| 37 | **Oregon** | — | — | — | — | — | — | 0% (no SUT) | — | NOMAD; CAT applies at $1M for income |
| 38 | **Pennsylvania** | 1 Apr 2018 (Marketplace Sales Act) / 1 Jul 2019 (economic) | $100,000 | — | — (sales only) | PY (12 mo) | 1 Apr 2018 | 6.00% | Yes | Cookie-nexus precursor; Wayfair-era $100k threshold |
| 39 | **Puerto Rico** (IVU) | 1 Jan 2021 | $100,000 | 200 | OR | PY or CY | 1 Jan 2021 | 11.50% (IVU) | Retail | Highest combined rate in US territories |
| 40 | **Rhode Island** | 1 Jul 2019 | $100,000 | 200 | OR | PY | 1 Jul 2019 | 7.00% | Retail | SST member |
| 41 | **South Carolina** | 1 Nov 2018 | $100,000 | — | — (sales only) | PY or CY | 1 Apr 2019 | 6.00% | Yes | Casual sales rule limits |
| 42 | **South Dakota** | 1 Nov 2018 (Wayfair home) | $100,000 | — (200 prong repealed Jul 2023) | — (sales only) | PY or CY | 1 Mar 2019 | 4.20% (reduced from 4.5% Jul 2023) | Yes | **Wayfair home state**; transaction count removed |
| 43 | **Tennessee** | 1 Oct 2019 (lowered from $500k to $100k Oct 2020) | $100,000 | — | — (sales only) | PY (12 mo) | 1 Oct 2020 | 7.00% | Retail | Lowered threshold 2020 |
| 44 | **Texas** | 1 Oct 2019 | $500,000 | — | — (sales only) | Prior 12 months | 1 Oct 2019 | 6.25% | Yes | Higher dollar threshold; see `tx-sales-tax` |
| 45 | **Utah** | 1 Jan 2019 | $100,000 | 200 | OR | PY or CY | 1 Oct 2019 | 4.85% | Retail | SST member |
| 46 | **Vermont** | 1 Jul 2018 | $100,000 | 200 | OR | PY (12 mo) | 1 Jun 2019 | 6.00% | Retail | SST member |
| 47 | **Virginia** | 1 Jul 2019 | $100,000 | 200 | OR | PY or CY | 1 Jul 2019 | 5.30% (combined state) | Retail | Includes 1% local in state base |
| 48 | **Washington** | 1 Oct 2018 | $100,000 | — (200 prong repealed Mar 2020) | — (sales only) | PY or CY | 1 Jan 2018 | 6.50% | Yes | Plus B&O; see `wa-bo-tax`; first major MPF law |
| 49 | **West Virginia** | 1 Jan 2019 | $100,000 | 200 | OR | PY or CY | 1 Jul 2019 | 6.00% | Yes | SST member |
| 50 | **Wisconsin** | 1 Oct 2018 | $100,000 | — (200 prong repealed Feb 2021) | — (sales only) | PY or CY | 1 Jan 2020 | 5.00% | Yes | SST member |
| 51 | **Wyoming** | 1 Feb 2019 | $100,000 | — (200 prong repealed Jul 2024) | — (sales only) | PY or CY | 1 Jul 2019 | 4.00% | Yes | SST member |

### 4.2. Summary by threshold tier

**$100,000 sales OR 200 transactions (Wayfair template, ~12 states still use both prongs):**
- AR, GA, KY, MD, MI, NE, NJ, NV, OH, RI, UT, VT, VA, WV, DC, PR

**$100,000 sales only (no transaction count) — ~28 states:**
- AL ($250k), AZ, CO, FL, ID, IN (2024), IA, KS (2021), ME (2022), MA, MN, MS ($250k), MO, NC (2024), ND, OK, PA, SC, SD (2023), TN, WA, WI (2021), WY (2024), AK (ARSSTC, 2025), HI (still 200 prong), NM, IL

**$500,000 sales (high-threshold states):**
- CA, NY (plus 100 transaction AND), TX

**$250,000 sales:**
- AL, MS

**AND logic (both prongs required):**
- CT ($100k AND 200), NY ($500k AND 100)

### 4.3. Marketplace facilitator law summary

- **Marketplace facilitator law summary** — Every state with sales tax has now enacted marketplace facilitator (MPF) laws. The general rule: if a third-party marketplace (Amazon Marketplace, eBay, Etsy, Walmart Marketplace, Reverb, Mercari, Poshmark, StockX, Patreon, OnlyFans, Whatnot, Faire, Houzz, etc.) facilitates a sale, the marketplace (not the individual seller) is the statutorily designated collector and remitter. For pure marketplace sellers (no direct sales): you generally do NOT need to register in any customer state on those marketplace sales. BUT see §4.4 for traps.

### 4.4. AUDIT FLASH POINT — when marketplace-only sellers still must register

- **Marketplace-only sellers still must register in some states** — Several states require marketplace sellers to register and file zero-returns even when 100% of sales are through facilitators: Washington — must register if Washington sales (incl. marketplace) cross $100k; file zero returns. Massachusetts — register required if marketplace + direct combined exceed $100k. Pennsylvania — register if MPF + direct combined. New Mexico — GRT regime; register if any taxable activity. California — CDTFA permit required for direct sales irrespective of MPF coverage. Best practice: any seller crossing $100k combined (direct + marketplace) into a state should register defensively. The cost of registration is trivial vs. the audit exposure.

## 5. Physical-presence nexus — still alive, still dangerous

Wayfair did not eliminate physical-presence nexus — it supplemented it. Any physical presence in a state creates nexus regardless of sales volume, with no de minimis safe harbor in most jurisdictions.

### 5.1. Physical-presence triggers

**Physical-presence triggers table**

| Trigger | Typical states triggered | Notes |
| --- | --- | --- |
| Employees working in state | All | Even one remote employee triggers nexus |
| Office or warehouse owned/leased | All | Including coworking memberships in some states |
| **Inventory stored in state (3PL / FBA)** | All | **Single biggest audit risk** — see §5.2 |
| Independent contractors providing service to in-state customers | Most | TX, CA aggressive |
| Sales reps physically visiting in-state customers | All | Even occasional visits |
| Affiliate clickthrough nexus | NY, NC, RI, others | "Amazon laws"; mostly moot post-Wayfair but still on books |
| Trade show attendance | Varies; SST states have de minimis exception (typically 14 days) | Non-SST states more aggressive |
| Drop-shipper with in-state inventory | All | Drop-shipper's nexus is separate from yours |

### 5.2. AUDIT FLASH POINT — Amazon FBA inventory nexus

- **Amazon FBA inventory nexus** — This is the single most common audit trap for small e-commerce sellers in 2025. When a seller enrolls in Amazon FBA (Fulfilled by Amazon), Amazon distributes the seller's inventory across its ~110+ fulfillment centers in the US. Amazon decides where the inventory is stored — the seller does not. Sellers can pull inventory placement reports via Amazon's Seller Central > Reports > Fulfillment > Inventory Event Detail to identify exactly which states held inventory. **Common Amazon FBA inventory states (high-risk for retroactive nexus):** - **California** (Multiple facilities — Tracy, Stockton, Moreno Valley, San Bernardino, Eastvale) - **Texas** (Dallas, Houston, San Antonio, Schertz, Coppell) - **New Jersey** (Robbinsville, Avenel, Carteret, Edison) — covers tri-state shipping - **Pennsylvania** (Carlisle, Hazle Township, Breinigsville) - **Illinois** (Joliet, Romeoville, Aurora) - **Florida** (Lakeland, Jacksonville, Ruskin) - **Georgia** (Braselton, Macon, Stone Mountain) - **New York** (Staten Island, Bethpage) - **Virginia** (Sterling, Petersburg) - **Arizona** (Phoenix, Goodyear) - **Tennessee** (Chattanooga, Lebanon, Charleston) - **Washington** (Kent, DuPont, Sumner) - **Indiana** (Whitestown, Plainfield, Indianapolis) - **Ohio** (Etna, Monroe, Obetz) - **Massachusetts** (Fall River, Stoughton) - **Colorado, Connecticut, Kentucky, Maryland, Michigan, Minnesota, Missouri, Nevada, North Carolina, Oregon (no SUT), South Carolina, Utah, Wisconsin** — varying numbers of facilities. **The legal position:** every state with sales tax treats inventory in an in-state warehouse as physical-presence nexus. The fact that Amazon owns/operates the warehouse does NOT shield the seller — the inventory is the seller's property. **Litigation note:** Some sellers have argued (successfully in PA — Online Merchants Guild v. Hassell, 2022; partially in CA via FTB litigation) that FBA inventory placement doesn't constitute "doing business" because the seller has no control over location. **Do not rely on this.** Most states reject the argument, and prevailing in court costs $50k–$200k+. Best practice: register prospectively in any FBA inventory state and consider VDA for prior periods. **Practical workflow when discovered:** 1. Pull FBA Inventory Event Detail report covering all periods (Amazon retains 18 months online; older via support request). 2. Identify all states ever holding inventory. 3. For states where Amazon Marketplace is the only sales channel and MPF law is in effect for the inventory period — MPF protects you for marketplace sales BUT physical-presence nexus is still triggered. State could demand registration and zero returns; some states will assert backup income tax nexus. 4. For states with direct sales in addition to FBA — calculate exposure; pursue VDA. 5. For seller with both FBA and own-warehouse drop-shipping arrangements — even higher complexity.  _(Online Merchants Guild v. Hassell, 2022 (PA))_

## 6. SaaS and digital-product taxability

- **Nexus vs taxability distinction** — Nexus (whether you must collect) is separate from taxability (whether the product is subject to tax). Even when you have nexus, sales of an exempt product don't trigger collection — but the threshold still counts the sales in some states.

### 6.1. The SaaS-taxable twelve

**SaaS-taxable twelve table**

| State | SaaS treatment | Notes |
| --- | --- | --- |
| **HI** | Taxable (GET) | All services taxable under GET |
| **MA** | Taxable | Pre-written software access |
| **NY** | Taxable | Treated as taxable "pre-written software" |
| **OH** | Taxable | Business-use only since 2003; consumer-use taxable too |
| **PA** | Taxable | Software-as-a-service treated as taxable digital good |
| **RI** | Taxable | Vendor-hosted software |
| **SC** | Taxable | "Communications" or "computer services" |
| **TN** | Taxable | Computer software access |
| **TX** | Taxable (80% rule) | Treated as "data processing service" — 80% of charge taxable, 20% exempt |
| **UT** | Taxable | Pre-written software |
| **WA** | Taxable | DOR ruling — SaaS = retail sale of digital automated service |
| **WV** | Taxable | Vendor-hosted software |

Also taxable in some structures: Connecticut (1% reduced rate for business-use SaaS), DC (taxable as "digital good"), New Mexico (taxable under GRT), Iowa (taxable since 2019), Mississippi (taxable since 2023).

### 6.2. SaaS-exempt states (majority)

- **SaaS-exempt states** — Most states do not tax SaaS as of 2025: CA, FL, GA, IL, MD, MI, MN, MO, NC, ND, NE, NJ, NV, OK, OR (no SUT), VA, WI, KY (consumer SaaS exempt; business-use grey area), AR, KS, LA, ME, VT, AL, AK, ID, IN, AZ (consumer-use grey), CO. **Trend:** states are gradually expanding SaaS taxability. MD added digital products tax 2021 (carve-out for SaaS). VT, NE have considered SaaS bills. Expect 3–5 more states to add SaaS taxability by 2027.

### 6.3. Digital downloads, streaming, ebooks

- **Digital downloads, streaming, ebooks taxability** — Digital product taxability is much more state-specific: Digital downloads (music, ebooks, software downloads): taxable in ~28 states; exempt in ~17. Streaming services (Netflix, Spotify): taxable in ~20 states; specific carve-outs in many. NFTs and digital art: emerging issue — PA, WA have published guidance; most states silent. For a transaction-by-transaction taxability determination, sellers should consult state-specific guidance or a CSP (Avalara TaxJar Vertex Sovos) automation.

## 7. Home-rule states

Four states allow localities to administer their own sales tax independently of the state revenue department. This creates registration obligations beyond the state.

### 7.1. Colorado

- **Colorado home-rule** — 70+ self-administered "home-rule" cities (Denver, Boulder, Colorado Springs, Aurora, Fort Collins, Lakewood, Pueblo, Greeley, Centennial, Longmont, etc.). State threshold $100k applies for state + state-collected localities. Sales & Use Tax System (SUTS) portal launched 2020 — single online filing for state + ~70 participating home-rule cities. Not all home-rule cities participate; some still require direct registration. See `co-suts` for mechanics.

### 7.2. Alabama

- **Alabama home-rule** — ~200 localities with self-administered SUT, of which ~50 are "non-program" (don't go through ADOR). Simplified Sellers Use Tax (SSUT) program — voluntary flat 8% rate on remote sellers; remits collected tax to ADOR, which distributes. Sellers who opt into SSUT are insulated from local audit risk. SSUT is the recommended approach for remote sellers.

### 7.3. Louisiana

- **Louisiana home-rule** — 64 parishes + numerous municipalities, each with separate sales tax administration. Threshold of $100,000 or 200 transactions enacted 2020. Louisiana Sales and Use Tax Commission for Remote Sellers (Remote Sellers Commission) provides centralized filing for remote sellers — file one return covering all parishes. Local Single Sales Tax (LSST) initiative ongoing but incomplete.

### 7.4. Alaska (no state SUT but local)

- **Alaska home-rule** — ~100 municipalities/boroughs with local SUT. Alaska Remote Seller Sales Tax Commission (ARSSTC) centralized administration for member munis. $100k statewide threshold; 200-transaction prong repealed effective Jan 1, 2025.

## 8. Streamlined Sales Tax (SST) program

- **Streamlined Sales Tax program** — The Streamlined Sales and Use Tax Agreement (effective 2005) is a multistate cooperative to reduce compliance burden on remote sellers. 24 states are full members in 2025.

### 8.1. SST member states (2025)

- **SST member states list** — AR, GA, IN, IA, KS, KY, MI, MN, NE, NV, NJ, NC, ND, OH, OK, RI, SD, TN (associate), UT, VT, WA, WV, WI, WY — plus DC.

### 8.2. SST benefits

- **SST benefits** — Certified Service Provider (CSP) free filing: SST states fund free use of an approved CSP (Avalara, TaxJar, Sovos, Vertex) for volunteer sellers (those without physical presence). The CSP handles registration, calculation, filing, and audit defense across all 24 SST states for $0 cost. Uniform definitions of taxable products and exemptions across member states. Single online registration via SSTRS (Streamlined Sales Tax Registration System). No registration fees in member states.

### 8.3. Non-SST states

- **Non-SST states list** — Non-SST states (CA, TX, FL, NY, IL, MA, VA, PA, AZ, AL, LA, CO, MD, CT, MS, MO, ME, NM, NH, SC, ID, AK, HI, OR, MT, DE) require direct registration and don't subsidize CSP services. Seller pays for any third-party automation.

## 9. Registration mechanics

### 9.1. Online registration portals

- **Online registration portals** — SST: SSTRS at sstregister.org — covers 24 states in one application. Non-SST: each state's DOR website — typically 30 minutes per state. Avalara / TaxJar / Sovos / Vertex: paid services that handle multi-state registration ($100–$300 per state, faster turnaround). MPF-only sellers: many states have a separate marketplace-seller registration with reduced reporting (CA's CDTFA "marketplace seller" designation, for example).

### 9.2. Filing frequency

**Filing frequency table**

| Annual liability | Typical frequency |
| --- | --- |
| < $1,000 | Annual |
| $1,000 – $4,000 | Quarterly |
| $4,000 – $50,000 | Monthly |
| > $50,000 | Monthly with prepayments or accelerated remittance |

Larger sellers (>$1M annual liability) may be required to make prepayments (CA, IL, NY) or file weekly (extreme cases).

### 9.3. Return due dates

- **Return due dates** — Most states: 20th of the month following the period. Variations: CA — last day of the month following the period (monthly); 25th for quarter prepays. NY — 20th of the month. TX — 20th of the month. FL — 20th of the month (collect-and-remit timely discount if filed by 20th). AL — 20th of the month. LA — 20th of the month. IL — 20th of the month.

### 9.4. Vendor compensation / timely-filing discount

- **Vendor compensation discounts** — IL — 1.75% of collected tax (capped); AL — 5% on first $100 / 2% above; LA — 0.935%; FL — 2.5% (capped at $30); TN — 1.6% (capped); TX — 0.5% timely discount + 1.25% prepayment discount. percent  _(State-specific vendor compensation rules (IL, AL, LA, FL, TN, TX))_

These add up — multi-state sellers commonly capture $1,000s annually in vendor compensation.

## 10. Voluntary Disclosure Agreement (VDA) process

- **VDA process intro** — When a seller discovers historical nexus exposure (e.g., FBA inventory back to 2018), the Voluntary Disclosure Agreement process limits damage.

### 10.1. Standard VDA terms

- **Standard VDA terms** — Most states offer: Lookback period limited to 3-4 years (in lieu of the typical 7-year audit lookback when discovered by the state); Penalties waived (failure-to-file, failure-to-pay); Interest still owed (rarely waived); Anonymity during negotiation — applicant identified by counsel/representative as "Taxpayer A"; No criminal referral.

### 10.2. State-specific VDA notes

- **State-specific VDA notes** — MTC (Multistate Tax Commission) Multistate VDA — single application covers up to 40+ states. Good for sellers with broad exposure. CA VDA — 3-year lookback if registered through CDTFA's Settlement and Compliance Program; income tax separately through FTB. TX — 4-year lookback; aggressive on FBA cases. NY — 36-month lookback for sales tax; favorable to remote sellers. FL — 3-year lookback; recent FBA enforcement push.

### 10.3. When VDA is NOT available

- **When VDA is not available** — Seller already contacted by state DOR (audit notice, nexus questionnaire received) — too late. Seller already registered — pay back due returns and request penalty abatement separately. Some states limit VDA to certain tax types or have funding caps.

## 11. P.L. 86-272 distinction — sales tax vs income tax

- **P.L. 86-272** — Public Law 86-272 (15 U.S.C. §§ 381–384, enacted 1959) prohibits state income tax on out-of-state sellers whose only in-state activity is solicitation of orders for tangible personal property approved/fulfilled from outside the state. It does NOT protect against sales tax obligations. A remote seller with $100k+ sales into State X: Has sales tax nexus (must register, collect, remit) — Wayfair. May still claim P.L. 86-272 protection from income tax if sales are tangible personal property only and in-state activities limited to solicitation. But P.L. 86-272 is narrowing rapidly: MTC's 2021 Revised Statement treats much internet activity (post-sale customer service via chat, app cookies tracking visitors, providing in-state non-sales support) as exceeding mere solicitation. CA, NY, NJ, OR (income tax via CAT), have adopted MTC's interpretation in regulations. See `us-pl-86-272-income-tax-nexus` for full treatment. **Practical implication:** sales tax registration in a state does not by itself create income tax nexus, but states increasingly take the position that economic-nexus-level activity exceeds P.L. 86-272.  _(Public Law 86-272, 15 U.S.C. §§ 381–384; MTC Revised Statement on P.L. 86-272 (Aug 2021))_

## 12. Worked examples

### 12.1. Example 1 — Shopify seller hitting NY threshold

**Facts:** Sarah operates a direct-to-consumer apparel brand on Shopify. She is a CA resident. Her NY sales for 2024 totaled $510,000 across 850 transactions. She has no physical presence in NY.

**Analysis:**
- NY threshold: $500,000 AND 100 transactions (in trailing 4 quarters). Sarah crosses both prongs → economic nexus.
- Shopify is NOT a "marketplace facilitator" for Shopify-hosted stores (Shopify Payments processes payment but doesn't list the goods). Sarah is the seller of record. **No MPF protection.**
- Sarah must:
  - Register for NY Sales Tax (DTF Certificate of Authority) — Form DTF-17.
  - Begin collecting NY state (4%) + local (4–4.875%) sales tax on shipments to NY addresses.
  - File NY sales tax returns (quarterly initially based on volume; monthly if >$300k/quarter).
- If apparel under $110 per item — exempt under NY clothing exemption (still collect threshold purposes).
- Income tax: Sarah may have NY corporate franchise tax nexus separately (NY economic nexus for corporate tax is $1M).

### 12.2. Example 2 — Amazon FBA seller with multi-state inventory

**Facts:** Mike sells home goods exclusively on Amazon Marketplace as an FBA seller. 2024 gross sales $850,000 across all states. Amazon's inventory placement reports show his goods were stored in fulfillment centers in CA, TX, NJ, PA, IL, GA, FL, AZ at various points during 2021-2024. He has never registered for sales tax anywhere outside his home state (Idaho).

**Analysis:**
- **Marketplace facilitator protection:** Amazon collects and remits in all states with MPF laws (every state with sales tax). Mike is not liable for collection on Amazon sales.
- **Physical-presence nexus from FBA inventory:** Mike has physical-presence nexus in CA, TX, NJ, PA, IL, GA, FL, AZ from 2021 onward (or whenever inventory was first placed).
- **State-by-state obligations:**
  - **CA** — must register with CDTFA; file zero returns (or report sales subject to FTB income tax). Likely back franchise tax exposure for SMLLC.
  - **TX** — register for sales tax permit; potential franchise tax filings (PIR + EZ computation if revenue >$2.47M).
  - **NJ, PA, IL, GA, FL, AZ** — register; mostly zero returns since Amazon collects.
- **Audit risk:** very high. Several states (PA, CA) actively cross-reference Amazon's seller data with their registration databases.
- **Recommended action:**
  1. Pull complete FBA inventory history from Amazon Seller Central.
  2. Initiate MTC Multistate VDA covering states with material exposure.
  3. Register prospectively in all FBA states.
  4. Set up nexus monitoring (Avalara / TaxJar) for the future.
- **Cost estimate:** $5,000–$15,000 in professional fees + back taxes/interest (much lower than the 7-year audit alternative).

### 12.3. Example 3 — SaaS company crossing thresholds in NY, TX, WA

**Facts:** Acme SaaS Inc. is a Delaware C-corp HQ'd in California selling a subscription SaaS product to businesses nationwide. 2024 ARR $4M. State breakdown: NY $800k, TX $700k, WA $300k, CA $1.5M (home state), rest of US $700k across 30+ states.

**Analysis:**
- **Taxability:** SaaS is taxable in NY, TX (80% of charge), WA. Taxability matters because economic nexus thresholds in some states count only taxable receipts; in others, all receipts.
- **NY** — SaaS taxable as pre-written software. $800k exceeds $500k AND 100 transactions threshold. **Register, collect 4% state + local 4–4.875%.** B2B customers may provide resale certificates (rare for SaaS) or direct-pay permits.
- **TX** — SaaS = "data processing service" — 80% taxable, 20% exempt. $700k exceeds $500k. **Register for sales tax permit; collect 6.25% state + up to 2% local on 80% of charge.** Note many TX customers can claim manufacturing exemption — collect resale/exemption certificates.
- **WA** — SaaS taxable as "digital automated service." $300k exceeds $100k. **Register; collect 6.5% state + local.** Plus B&O tax (separate filing) at 0.471% Service rate or 0.484% Retailing rate.
- **CA** — SaaS NOT taxable. No collection obligation regardless of threshold. But may have franchise tax / CDTFA permit obligation if any tangible sales.
- **Other states** — SaaS exempt in most. Threshold not relevant for taxability. But Acme should monitor:
  - PA ($100k threshold; SaaS taxable since 2016)
  - OH ($100k threshold; SaaS taxable for business use)
  - MA ($100k threshold; SaaS taxable)
  - HI ($100k threshold; GET taxable)
  - SC, TN, UT, RI, WV (SaaS taxable)
  - Other states monitoring for taxability changes.

**Action plan:**
1. Register in NY, TX, WA immediately.
2. Collect resale/exemption certificates from B2B customers (critical for cost recovery).
3. Implement Avalara or TaxJar for ongoing nexus monitoring.
4. Re-evaluate annually as ARR grows and additional states' thresholds are crossed.
5. Track P.L. 86-272 protection for income tax separately (SaaS revenue is not tangible personal property so P.L. 86-272 likely doesn't apply — separate state income tax nexus analysis required).

## 13. AUDIT FLASH POINTS — summary

> **AUDIT FLASH POINT 1: Amazon FBA inventory creates physical-presence nexus in every state where Amazon stores your inventory.** Even when 100% of sales go through Amazon Marketplace (and Amazon collects sales tax under MPF laws), you have a registration obligation due to physical presence. Pull FBA inventory placement reports and assess every state ever holding goods.

> **AUDIT FLASH POINT 2: Missed Wayfair registration in a state where you crossed threshold leads to a 7-year (or unlimited, for non-filers) audit lookback.** VDAs limit lookback to 3-4 years and waive penalties — but ONLY if seller initiates before state contact. Monitor thresholds quarterly.

> **AUDIT FLASH POINT 3: Marketplace-only sellers in WA, MA, PA, NM may still need to register and file zero returns.** Don't assume MPF coverage equals no registration. Check state rules.

> **AUDIT FLASH POINT 4: Sales tax nexus and income tax nexus are separate analyses.** Having sales tax nexus does not automatically create income tax nexus, but states increasingly assert both. P.L. 86-272 protects only against income tax and is narrowing.

> **AUDIT FLASH POINT 5: Home-rule states (CO, AL, LA, AK) require local registrations in addition to state.** Failing to register in Denver or Boulder is a separate violation from Colorado state failure. SSUT (AL), SUTS (CO), Remote Sellers Commission (LA), ARSSTC (AK) simplify but don't eliminate the local obligation.

> **AUDIT FLASH POINT 6: Kansas threshold was $0 from 2019-2021.** A seller making $5,000 of KS sales during that window had registration obligation. KS has not enforced retroactively but VDAs frequently surface this.

> **AUDIT FLASH POINT 7: New York's $500k AND 100 transactions test is measured on the trailing 4 quarters,** not the calendar year. A seller could trigger mid-year and owe collection from the next quarter. Monitor quarterly.

## 14. Provenance and authority

This skill compiles publicly available state DOR guidance, the Sales Tax Institute's nexus reference tables, and the AICPA's State Nexus Comparison Tables as of November 2025. Key primary sources:

- **South Dakota v. Wayfair, Inc.**, 138 S. Ct. 2080 (2018)
- **Quill Corp. v. North Dakota**, 504 U.S. 298 (1992) (overruled)
- **Public Law 86-272**, 15 U.S.C. §§ 381–384
- **Streamlined Sales and Use Tax Agreement** (current version, sstgovboard.org)
- State DOR websites for every state covered (current as of November 2025)
- **Multistate Tax Commission**, Revised Statement on P.L. 86-272 (Aug 2021)
- **MTC National Nexus Program** Multistate VDA materials
- **Alaska Remote Seller Sales Tax Commission** code and resolutions (effective Jan 2025 amendment removing 200-transaction prong)

**Thresholds and effective dates change frequently.** This matrix reflects rules in force for tax year 2025 as of November 15, 2025. Verify against state DOR primary source for any specific compliance decision. The annual update runbook (see `ANNUAL-UPDATE-RUNBOOK.md` in this package) prompts re-verification of every threshold each November.

**Verified-by status: pending.** This skill awaits country-level sign-off review per the verification model. Multiple US-credentialed accountants (CPA, EA, or attorney admitted in a US jurisdiction) should review before deployment to production.

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
