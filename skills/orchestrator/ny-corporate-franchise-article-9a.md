---
name: ny-corporate-franchise-article-9a
description: Tier 2 content skill for New York State Corporate Franchise Tax under Tax Law Article 9-A. Covers C-corporations and S-corporations electing federal status (NY GBC), the three alternative tax bases (business income, capital, fixed dollar minimum), the 6.5% standard rate and the 7.25% rate on business income over $5M, single-sales-factor apportionment with market-based sourcing, MTA surcharge for MCTD activity, mandatory first installment (MFI) rules, and CT-3 / CT-3-A combined filing. Tax year 2025.
jurisdiction: US-NY
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ny-corporate-franchise-article-9a

## New York Corporate Franchise Tax — Article 9-A (General Business Corporations)

**Description (80 words):** Tier 2 content skill for New York State Corporate Franchise Tax under Tax Law Article 9-A. Covers C-corporations and S-corporations electing federal status (NY GBC), the three alternative tax bases (business income, capital, fixed dollar minimum), the 6.5% standard rate and the 7.25% rate on business income over $5M, single-sales-factor apportionment with market-based sourcing, MTA surcharge for MCTD activity, mandatory first installment (MFI) rules, and CT-3 / CT-3-A combined filing. Tax year 2025.

## 1. Scope

- **Article 9-A scope** — This skill applies to corporations subject to New York State franchise tax under Tax Law Article 9-A ("General Business Corporation Franchise Tax"). Article 9-A is the principal NY corporate-level income tax and replaced the former Articles 9-A (legacy), 32 (banks) and certain provisions of Article 9 following the 2014 corporate tax reform that took effect for tax years beginning on or after January 1, 2015.  _(Tax Law Article 9-A)_

### 1.1 In scope

- **In scope entities** — Domestic NY corporations (incorporated in NY). Foreign corporations doing business, employing capital, owning or leasing property, maintaining an office, or deriving receipts ≥ $1,138,000 from activity in NY (the economic nexus threshold under Tax Law §209.1(b); the figure was originally $1,000,000 in 2015 and is indexed for inflation; the 2025 figure is reflected in TSB-M memoranda). Federal C-corporations. Banking corporations (post-reform Article 32 merger — now in Article 9-A). S-corporations that have not made a NY S-election are taxed as C-corporations under Article 9-A despite federal pass-through status.  _(Tax Law §209.1(b))_
- **Economic nexus receipts threshold (2015 baseline)** — $1,000,000  _(Tax Law §209.1(b))_
- **Economic nexus receipts threshold (2025)** — $1,138,000  _(Tax Law §209.1(b))_

### 1.2 Out of scope (refusal catalogue)

- **NY S-corporations** — NY S-corporations that have made the NY S-election under Tax Law §660 — these file CT-3-S, which uses fixed dollar minimum only (no business income base). Defer to a future ny-s-corp skill.  _(Tax Law §660)_
- **Insurance corporations** — Out of scope — Article 33.  _(Article 33)_
- **Utility / telephone / transportation corporations** — Out of scope — Article 9 sections 183/184/186-a.  _(Article 9 §§183/184/186-a)_
- **REITs and RICs** — Real estate investment trusts (REITs) and regulated investment companies (RICs) — special apportionment and deduction rules in §209.5 / §210.3-b; out of scope.  _(§209.5 / §210.3-b)_
- **Captive REITs and RICs** — Special inclusion rules; out of scope.
- **NYC GCT and BCT** — Separate NYC return (NYC-2 / NYC-2A); see Section 12 for crosswalk but full computation deferred to a nyc-business-corp-tax skill.
- **NYC Unincorporated Business Tax (UBT)** — See existing nyc-ubt.md skill.
- **Pass-Through Entity Tax (PTET)** — Under Article 24-A — deferred to a dedicated ny-ptet skill. Article 24-A is a separate elective entity-level tax; an Article 9-A taxpayer does not pay PTET, but an Article 9-A corporation that is an eligible entity (S-corp election under §660 or partnership) is the entity electing — out of scope here.  _(Article 24-A)_
- **Composite returns** — For non-resident shareholders — out of scope.
- **Combined reporting for non-unitary affiliates** — Only the mandatory water's-edge unitary combined group rules under §210-C are covered (Section 8).  _(§210-C)_
- **NOL carryback** — NY does not allow NOL carrybacks for post-2015 losses (§210.1(a)(ix)).  _(§210.1(a)(ix))_
- **Pre-2015 PNOL conversion subtraction pool mechanics** — For closely-held entities with unusual history — high-level coverage only; complex conversion pool calculations require reviewer sign-off.

### 1.3 Conservative defaults

- **Conservative default behavior** — Per the Tier 1 workflow base, when a question is ambiguous the skill produces the higher tax answer and flags it for human reviewer signoff. Specifically: If unsure whether a receipt is sourced to NY → source to NY (higher numerator). If unsure whether a manufacturer qualifies → assume not qualified (6.5% / 7.25% applies, not 0%). If unsure whether the capital base sunset applies in the year at issue → compute the capital base (the alternative will be the higher of the three bases anyway). If unsure about MFI tier → use the 40% MFI (higher).

## 2. The Three Alternative Tax Bases

- **Greatest of three bases** — Article 9-A imposes the franchise tax as the greatest of three alternative bases, plus the MTA surcharge if applicable.  _(Tax Law §210.1)_

### 2.1 Business income base (Tax Law §210.1(a))

- **Business income base tax formula** — Tax = business income × business apportionment factor (BAF) × applicable rate.  _(Tax Law §210.1(a))_
- **Business income** — Business income = Entire Net Income (ENI) less investment income and less other exempt income.  _(§208(8), §208(6-a), §208(9))_

#### 2.1.1 Computation steps

- **Business income computation steps** — 1. Start with federal taxable income (Line 28, Form 1120, before NOL and special deductions). 2. NY addition modifications under §208(9)(b): including State and local income taxes deducted federally; NY net operating losses deducted federally that are now picked up via NY NOLD; 100% of GILTI § 951A inclusion (NY conforms but provides a 95% exemption — see §208(6-a)); Interest paid to related members (related-member addback unless safe harbor under §208(9)(o)); Royalties paid to related members (similar). 3. NY subtraction modifications under §208(9)(a) and (a-1): Refunds of state and local income tax included federally; Foreign dividends gross-up under §78; Subpart F income (treated as dividend → exempt CFC receipts; see §208(6-a)); 95% of GILTI exemption (the "other exempt income" pool); 50% IRC §250 federal FDII deduction add-back is not required — NY conforms; but the 50% GILTI deduction is replaced by NY's own 95% exemption; Subtraction for investment income (later removed from business income). 4. Result = Entire Net Income (ENI). 5. Subtract investment income (§208(6)) — limited to ≤ 8% of ENI under §208(9)(a)(viii) cap if applicable. (Note: post-2015 reform the 8% cap was eliminated, but a gross investment income limitation exists — investment income is defined narrowly as income from "investment capital" which is essentially stocks held more than 1 year and meeting the §208(5) holding requirements.) 6. Subtract other exempt income (§208(6-a)): 95% of exempt CFC income (Subpart F + GILTI), 50% exempt unitary corporation dividends (now after 2015 reform, 100% if voting power and ownership thresholds met under §208(6-a)). 7. Result = business income for purposes of §210.1(a). 8. Apportion business income to NY using the BAF (Section 4). 9. Subtract NOLD (current period prior NOL deduction — see Section 9). 10. Apply the rate (Section 3).  _(§208(9)(b), §208(9)(a), §208(9)(a-1), §208(6), §208(6-a), §210.1(a))_

#### 2.1.2 Allocation of NOL

- **Post-apportionment NOLD** — NOLD is taken after apportionment under post-2015 reform (NY adopted "post-apportionment NOL" — see §210.1(a)(ix)). This is a significant departure from the pre-2015 regime which used pre-apportionment NOLs. Pre-2015 NOLs are captured in the PNOL Conversion Subtraction pool (Section 9.2).  _(§210.1(a)(ix))_

### 2.2 Capital base (Tax Law §210.1(b))

- **Capital base tax formula** — Tax = business capital × 0.1875% (the 2025 rate; see Section 2.2.2 for sunset history) — capped at $5,000,000.  _(Tax Law §210.1(b))_
- **Business capital** — Business capital = total capital - investment capital - capital allocated to subsidiaries that are themselves taxpayers - exempt asset capital. Capital is computed as the average of beginning- and end-of-year fair market values of total assets less liabilities — but in practice NY accepts tax basis (Form CT-3, Part 4) as a simplification absent fair-market revaluation. The capital base is apportioned using the same BAF as the business income base.

#### 2.2.1 Rate

**Capital base rate by tax year**

| Tax year | Capital base rate |
| --- | --- |
| 2015 | 0.150% |
| 2016 | 0.125% |
| 2017 | 0.100% |
| 2018 | 0.075% |
| 2019 | 0.050% |
| 2020 | 0.025% |
| 2021 | **0.1875%** (reinstated and increased by the FY2022 budget, S.2509-C/A.3009-C, Part HHH) |
| 2022 | 0.1875% |
| 2023 | 0.1875% |
| 2024 | 0.1875% |
| **2025** | **0.1875%** |
| 2026 | 0.1875% (currently scheduled; sunset to 0% on January 1, 2027 per A.3009-C Part HHH unless extended — **verify in the year of filing**) |

- **Capital base glide path note** — Note: the capital base was on a glide path to 0% for tax years beginning in 2021, but the FY2022 NY budget reinstated it at 0.1875% to backfill pandemic-era revenue. The reinstated rate is currently scheduled to sunset on January 1, 2027 unless extended. Always verify the current-year status — NY has extended this sunset multiple times.  _(FY2022 budget, S.2509-C/A.3009-C, Part HHH)_
- **Qualified manufacturers capital base rate** — 0.132% percent (capped at $5M)
- **Cooperative housing corporations capital base rate** — 0.04% percent

#### 2.2.2 Cap

- **Capital base tax cap** — $5,000,000 (regardless of computed amount; applies before MTA surcharge)

### 2.3 Fixed dollar minimum (FDM) — §210.1(d)

**FDM schedule by NY receipts (2025)**  _(§210.1(d))_

| NY receipts | FDM (2025) |
| --- | --- |
| Not more than $100,000 | **$25** |
| Over $100,000 but not over $250,000 | **$75** |
| Over $250,000 but not over $500,000 | **$175** |
| Over $500,000 but not over $1,000,000 | **$500** |
| Over $1,000,000 but not over $5,000,000 | **$1,500** |
| Over $5,000,000 but not over $25,000,000 | **$3,500** |
| Over $25,000,000 but not over $50,000,000 | **$5,000** |
| Over $50,000,000 but not over $100,000,000 | **$10,000** |
| Over $100,000,000 but not over $250,000,000 | **$20,000** |
| Over $250,000,000 but not over $500,000,000 | **$50,000** |
| Over $500,000,000 but not over $1,000,000,000 | **$100,000** |
| Over $1,000,000,000 | **$200,000** |

- **FDM tier count note** — (Note: §210.1(d) is structured as 11 tiers in the statute, but is commonly described as "8 tiers" because the §210.1(d)(1)(C) bracket structure pre-2021 had 8. The FY2022 budget added the upper brackets. The full schedule shown above is the post-FY2022 schedule effective for 2021+ tax years.)  _(§210.1(d)(1)(C))_
- **Reduced FDM for manufacturers/QETCs** — Qualified manufacturers, QETCs, and qualified emerging technology companies use a reduced FDM schedule — see §210.1(d)(2) / §210.1(d)(3): Qualified NY manufacturers FDM tier table starts at $19 (NY receipts ≤ $100K) and tops out at $4,500 ( >$1B). A non-captive REIT or RIC uses the same FDM schedule as general business corporations. A taxpayer that is not a New York taxpayer for the entire year (short period) prorates the FDM under §210.1(d)(4).  _(§210.1(d)(2), §210.1(d)(3), §210.1(d)(4))_

### 2.4 Choosing the base — "greater of"

- **Greater-of rule and typical applicability** — For each tax year the taxpayer pays the greatest of the three bases. A taxpayer can be a "business income base" payer in one year and a "FDM" payer in another. The capital base is rarely the highest base for small or low-margin taxpayers (because of the $5M cap on capital base tax, and because business income usually generates more tax). It is most relevant for asset-heavy holding companies with low operating income.

## 3. Rates (Business Income Base)

**Business income base rates by taxpayer type (2025)**  _(Tax Law §210.1(a))_

| Taxpayer type | 2025 rate |
| --- | --- |
| **General business corporation** (default) | **6.5%** |
| General business corporation with **business income > $5,000,000** (tax years beginning on or after Jan 1, 2021 through Dec 31, 2026 — per Part HHH of FY2022 budget, extended by Part SS of FY2025 budget) | **7.25%** on entire business income (no bracket — flat rate on entire amount, not just the excess above $5M) |
| **Qualified NY manufacturer** (§210.1(a)(vi)) | **0.00%** (zero rate) |
| **Qualified emerging technology company (QETC)** under §210.1(a)(vii) | **4.875%** |
| **Small business taxpayer** (closely-held, < $390,000 entire net income, etc. — §210.1(a)(iv)) | **6.5%** (no longer differentiated post-2024 — small biz reduced rates were eliminated/aligned to 6.5% by the FY2022 reforms but the §210.1(a)(iv) sub-threshold structure remains as a tier within the 6.5% bracket) |

### 3.1 The 7.25% rate — important detail

- **7.25% cliff effect and sunset** — The 7.25% rate applies to the entire business income when business income exceeds $5,000,000, not just to the excess. This creates a cliff at $5M: a taxpayer with $5,000,000 of business income pays 6.5% × $5M = $325,000; a taxpayer with $5,000,001 of business income pays 7.25% × $5,000,001 = $362,500.07 — an additional $37,500 of tax for $1 of additional income. Some taxpayers near the threshold deliberately defer income or accelerate deductions to stay below $5M. Sunset: The 7.25% rate was originally enacted for tax years 2021–2023, extended through 2026 by the FY2024 budget, and extended through 2027 by the FY2025 budget. Verify status in the year of filing.

### 3.2 Qualified NY manufacturer

- **Qualified NY manufacturer definition** — A qualified NY manufacturer under §210-B(1)(b) and §210.1(a)(vi) is a taxpayer that: 1. Is principally engaged in the production of goods by manufacturing, processing, assembling, refining, mining, extracting, farming, agriculture, horticulture, floriculture, viticulture, or commercial fishing; and 2. More than 50% of gross receipts are derived from such activity; and 3. The taxpayer's property in NY used in qualified activity has an adjusted basis of at least $1,000,000; or alternatively all of the taxpayer's real and personal property used in NY in the principal manufacturing activity is in NY. If qualified: business income base rate = 0%. Capital base rate = 0.132%. FDM is reduced.  _(§210-B(1)(b), §210.1(a)(vi))_

### 3.3 Qualified emerging technology company (QETC)

- **QETC definition** — A QETC under Public Authorities Law §3102-e: 1. Located in NY; 2. Has total annual product sales ≤ $10M; 3. Is engaged in emerging technology activity (biotech, advanced computing, advanced materials, defined sectors) — see Public Authorities Law §3102-e. If qualified: business income base rate = 4.875%.  _(Public Authorities Law §3102-e)_

## 4. Apportionment — Single Sales Factor with Market-Based Sourcing

- **BAF formula** — NY uses single receipts factor (single sales factor) apportionment under Tax Law §210-A. The factor is: BAF = NY receipts / Everywhere receipts. There is no payroll factor and no property factor. NY adopted single sales factor in 2007 and 2015 reforms cleaned up market sourcing for all receipt types.  _(Tax Law §210-A)_

### 4.1 Market-based sourcing (§210-A)

**Sourcing rules by receipt type**  _(Tax Law §210-A)_

| Receipt type | NY sourcing rule | Statute |
| --- | --- | --- |
| Sale of tangible personal property | Destination — where shipped | §210-A.2 |
| Rentals / royalties from real property | Where the property is located | §210-A.3 |
| Rentals / royalties from tangible personal property | Where the property is located when used | §210-A.4 |
| Services | **Where the customer receives the benefit of the service** (market-based) | §210-A.10 |
| Sale of digital products | **Where the customer / user is located** | §210-A.4 |
| Software licenses / SaaS | Where the **user** is located (treated as a service) | §210-A.4 / .10 |
| Receipts from financial instruments (interest, dividends, capital gains) | Hierarchy: customer commercial domicile / billing address (§210-A.5) | §210-A.5 |
| Receipts from intangibles (royalties, license fees) | **Where the intangible is used** | §210-A.4(b) |
| Receipts from a partnership | Pass through using the partnership's BAF, OR use the partnership's underlying receipts (aggregate method) | §210-A.11 |
| Hedge fund / broker-dealer receipts | Special rules — §210-A.5 |  |
| Credit card receivables | §210-A.5(c) — billing address |  |
| Advertising — broadcast / digital | Where audience / viewers are located | §210-A.10 |
| Transportation receipts | Mileage / origin-destination | §210-A.8 |

### 4.2 Hierarchy for service sourcing

- **Service sourcing hierarchy** — For services where the customer location is not directly knowable, §210-A.10 provides a hierarchy: 1. Where the customer actually received the benefit (preferred). 2. Customer's billing address. 3. Customer's commercial domicile. 4. Throw-out (excluded from both numerator and denominator) — used only when no reasonable basis exists.  _(§210-A.10)_

### 4.3 Digital products

- **Digital product sourcing and TSB ruling** — Under §210-A.4 (added by the 2015 reform), receipts from digital products (software downloads, e-books, streaming media, SaaS) are sourced by: 1. Customer's primary use location; 2. If multi-jurisdictional use → reasonable apportionment based on user IP location, usage data, or other measurable basis. A 2023 NY Tax Department TSB ruling (TSB-M-23(1)C) clarified that SaaS for business customers is sourced by the location of the customer's employees who use the software (not the billing address) when reliable usage data exists.  _(§210-A.4; TSB-M-23(1)C)_

### 4.4 Throw-out rule

- **Partial throw-out rule** — NY uses a partial throw-out under §210-A.10: when the taxpayer cannot reasonably determine where the customer is located, the receipt is excluded from both the numerator (NY) and the denominator (everywhere). Throw-out should be a last resort and the taxpayer must document why customer location cannot be determined.  _(§210-A.10)_

### 4.5 NY receipts threshold for nexus

- **Economic nexus receipts threshold (2025)** — $1,138,000  _(Tax Law §209.1(b))_

## 5. MTA Surcharge

- **MTA surcharge applicability** — The Metropolitan Transportation Business Tax Surcharge under Tax Law §209-B applies to Article 9-A taxpayers that do business, employ capital, own or lease property, or derive receipts in the Metropolitan Commuter Transportation District (MCTD).  _(Tax Law §209-B)_

### 5.1 MCTD definition

- **MCTD 12 counties** — The MCTD comprises 12 counties: 1. New York County (Manhattan) 2. Bronx County 3. Kings County (Brooklyn) 4. Queens County 5. Richmond County (Staten Island) 6. Nassau 7. Suffolk 8. Westchester 9. Rockland 10. Orange 11. Putnam 12. Dutchess

### 5.2 Rate

**MTA surcharge rate by tax year**

| Tax year | MTA surcharge rate |
| --- | --- |
| 2020 | 28.6% |
| 2021 | 30.0% |
| 2022 | 30.0% |
| 2023 | 30.0% |
| 2024 | 30.0% |
| **2025** | **30.0%** (per TSB-M issued late 2024 setting the 2025 rate) |

- **Surcharge base** — The surcharge is 30% of the franchise tax allocated to the MCTD.

### 5.3 Computation

- **MTA surcharge computation steps** — 1. Compute the Article 9-A tax (the greater of three bases). 2. Apportion that tax to the MCTD using the MCTD apportionment factor (computed analogously to the BAF but with MCTD-source receipts in the numerator and all-NY receipts in the denominator). Form CT-3-M is used. 3. Apply the 30% surcharge to the MCTD-apportioned tax. The MTA surcharge is in addition to the regular Article 9-A tax — not in lieu of.

### 5.4 MFI for MTA surcharge

- **MFI for MTA surcharge forms** — The MFI for the MTA surcharge follows the same rules as the regular MFI (Section 7), separately computed. Form CT-300 is used for MFI; Form CT-3-M for the annual MTA surcharge.

## 6. Combined Reporting — §210-C

- **Mandatory water's-edge combined reporting** — NY mandates water's-edge combined reporting for Article 9-A taxpayers that are members of a unitary business with > 50% common stock ownership. The 2015 reform replaced the prior "intercompany transactions / inclusion test" regime with a clean ownership + unitary test.  _(§210-C)_

### 6.1 Mandatory combined group

- **Mandatory combined group tests** — Under §210-C.2, a combined report is mandatory when both: 1. Capital stock ownership test: > 50% of voting stock owned directly or indirectly by a common owner; AND 2. Unitary business test: the entities are engaged in a unitary business (flow of value among them — Mobil / Container test).  _(§210-C.2)_

### 6.2 Water's edge

- **Water's-edge exclusions** — NY uses water's-edge combination — non-U.S. corporations are excluded unless: They are "alien corporations" with effectively connected income (ECI) — included to the extent of ECI; or They have > 20% of their property, payroll, and receipts in the U.S. (the "20% U.S. presence" inclusion under §210-C.2(c)).  _(§210-C.2(c))_

### 6.3 Commonly-owned group election

- **Commonly-owned group election** — Under §210-C.3, a "commonly-owned group election" allows non-unitary commonly-owned (>50%) entities to elect to file combined. The election is binding for 7 years and revocable thereafter.  _(§210-C.3)_

### 6.4 Combined return mechanics

- **Combined return mechanics** — File Form CT-3-A (combined return) plus CT-3-A/BC for each member. Combined business income is the sum of each member's ENI with eliminations. Intercompany transactions are eliminated (§210-C.6). The BAF is computed at the group level: NY receipts of all members / total receipts of all members. A single FDM is computed at the group level based on group NY receipts, plus an additional $1,500 FDM for each additional member (the "per-member surcharge"). Designated agent files the combined return. The combined group has a single NOLD pool.  _(§210-C.6)_
- **Per-member additional FDM surcharge** — $1,500 (per additional member in a combined group)

### 6.5 Designated agent

- **Designated agent requirement** — The combined group elects a designated agent that files CT-3-A on behalf of the group. Each member must consent.

### 7.1 Schedule

**Estimated tax installment schedule (calendar year filer)**  _(§213-b)_

| Installment | Due date (calendar year filer) |
| --- | --- |
| **MFI** (Mandatory First Installment) | March 15 (15th day of the 3rd month of the **succeeding** tax year — see §213-b) |
| 2nd installment | June 15 |
| 3rd installment | September 15 |
| 4th installment | December 15 |

- **MFI timing description** — The MFI is the first installment toward the succeeding year's tax — paid with or before the prior year's return is due (March 15 for calendar-year filers).

### 7.2 MFI amount

**MFI amount by prior-year tax**  _(§213-b.1)_

| Prior year franchise tax (Art. 9-A, NY State portion only) | MFI |
| --- | --- |
| ≤ $100,000 | **25%** of prior-year tax |
| > $100,000 | **40%** of prior-year tax |

- **40% MFI trap note** — The 40% MFI is the trap for growing businesses — once you cross $100k of NY state franchise tax in any year, the next year's MFI jumps from 25% to 40%, due March 15.

### 7.3 MFI for MTA surcharge

- **Separate MFI for MCTD surcharge** — Separate MFI for the MCTD surcharge, computed on the same 25/40 split based on the prior-year MCTD surcharge tax.

### 7.4 Form CT-300

- **Form CT-300 filing** — The MFI is paid via Form CT-300 ("Mandatory First Installment of Estimated Tax for Corporations") filed with the prior-year return or by March 15 of the succeeding year, whichever is earlier in practice.

### 7.5 Remaining three installments

- **Remaining installments formula** — Each of the 2nd, 3rd, 4th installments = (current year's estimated tax - MFI already paid) / 3 to bring the cumulative to 25%/50%/75%/100% of current year tax by the four respective due dates. Form CT-400 is used for installments 2, 3, and 4.

### 7.6 Safe harbor and underpayment penalty

- **Safe harbor and penalty rules** — NY uses §1085(b) for the underpayment penalty. Safe harbor: 100% of prior-year tax (no AGI threshold equivalent to federal — NY uses 100% flat); or 91% of current-year tax (note: 91%, not 90%, under §1085(b)(2)). If the prior year was a short period or zero tax year, the safe harbor reverts to 91% of current. The penalty rate is the federal underpayment rate plus a 2% addition under §1096(e).  _(§1085(b), §1085(b)(2), §1096(e))_

## 8. Net Operating Losses — PNOL and NOLD

- **Two NOL regimes** — The 2015 corporate tax reform created two NOL regimes that operate in parallel.

### 8.1 NOLD — current NOL deduction (§210.1(a)(ix))

- **NOLD mechanics** — For tax years beginning on or after January 1, 2015, the NOLD is a post-apportionment deduction: 1. Compute apportioned business income to NY. 2. Subtract the available NOL carryforward (no carryback for post-2014 NOLs). 3. 20-year carryforward (NY does not conform to the federal 80% income limitation or unlimited carryforward in CARES Act — NY still has 20-year limit and no 80% income cap). 4. NOLD can fully offset apportioned business income (subject only to the 20-year staleness rule). NOLD is separate for combined groups vs. separate filers. A loss generated in a combined-return year can only be used by the combined group (designated agent allocates).  _(§210.1(a)(ix))_

### 8.2 PNOL — Prior NOL Conversion Subtraction Pool (§210.1(a)(ix))

- **PNOL conversion pool mechanics** — For tax years beginning before January 1, 2015, NOLs were computed pre-apportionment. The 2015 reform converted those legacy NOLs into a PNOL conversion subtraction pool: 1. Determine unabsorbed NOL as of the last day of the 2014 base year. 2. Apply the 2014 BAF to convert to apportioned dollars. 3. Apply a conversion ratio (the 2014 statutory rate / 6.5% × the apportionment-modified amount) to compute the pool. 4. Subtract from the pool, taken over a 20-year period beginning 2015, generally limited to 10% of the original pool in each tax year (the "10% annual cap") under §210.1(a)(ix)(B). A taxpayer may elect to spread over 2015 and 2016 only by taking 50% in each year (the "two-year election"). The PNOL pool is separate from the NOLD. The taxpayer may use both in the same year. PNOL is taken first, then NOLD.  _(§210.1(a)(ix)(B))_

### 8.3 No carryback

- **No NOL carryback and CARES Act decoupling** — Post-2015 NOLs cannot be carried back. The federal CARES Act 5-year carryback for 2018-2020 NOLs did not carry over to NY (NY decoupled).

### 9.1 Qualified NY Manufacturer

- **Detailed manufacturer eligibility and caps** — The 0% rate on business income base and 0.132% on capital base require ongoing qualification: Principal activity (> 50% gross receipts) in manufacturing or one of the qualifying activities (§210-B(1)(b)). NY property — adjusted basis of property used in qualified activity in NY ≥ $1,000,000; or all of the taxpayer's manufacturing property is in NY. Property test computed on the last day of the tax year under §210-B(1)(b)(ii). The 50% gross receipts test is applied at the entity level. For combined groups, applied at the combined group level. The 0% rate applies only to the business income base. The capital base 0.132% rate still applies and is capped at $2.5M (not $5M for manufacturers).  _(§210-B(1)(b), §210-B(1)(b)(ii))_
- **Manufacturer NY property adjusted basis threshold** — $1,000,000  _(§210-B(1)(b))_
- **Manufacturer capital base cap** — $2,500,000 (cap for manufacturers instead of general $5M cap)

### 9.2 QETC

- **Detailed QETC eligibility** — To be a QETC under §210.1(a)(vii): Located in NY (principally; > 50% of property in NY). Total annual product sales ≤ $10M. Primary products or services are emerging technology under PAL §3102-e (defined sectors). The 4.875% rate applies to business income base only. A QETC that is also a qualified NY manufacturer can elect to be treated as a qualified manufacturer (0% rate) — the manufacturer rate is more favorable.  _(§210.1(a)(vii), PAL §3102-e)_

### 10.1 NYC is separate

- **NYC BCT/GCT overview** — NYC imposes its own corporate-level tax under Title 11 of the NYC Administrative Code. The current regime (post-2015 reform) is the NYC Business Corporation Tax (BCT) under Subchapter 3-A — a near-clone of NY State Article 9-A but with several differences. For corporations not subject to BCT (typically corporations not principally doing business in NYC), the legacy General Corporation Tax (GCT) under Subchapter 2 applies.  _(NYC Admin Code Title 11, Subchapter 3-A, Subchapter 2)_

### 10.2 Key NYC differences

**NY State (Article 9-A) vs NYC (BCT) comparison**

| Item | NY State (Article 9-A) | NYC (BCT) |
| --- | --- | --- |
| Statutory rate | 6.5% / 7.25% | 8.85% (general); 9.0% for financial; 4.425% for QETC |
| Capital base rate | 0.1875% (2025) | 0.075% (cap $10M) |
| Apportionment | Single sales, market-based | Single sales, market-based (largely conformed) |
| MTA surcharge | 30% (state-level) | None (NYC is in MCTD but does not add its own surcharge on top of BCT) |
| Combined reporting | Mandatory unitary >50% | Mandatory unitary >50%, but **NYC excludes** any non-NYC-taxpayer from the combined NYC group |
| Filing form | CT-3 / CT-3-A | NYC-2 / NYC-2A |
| Due date | 3.5 months after year-end (April 15 calendar) | 3.5 months after year-end (April 15 calendar) |

### 10.3 No piggyback

- **Separate filing requirement** — NYC BCT is filed separately from NY State CT-3 — there is no combined state/city return. The taxpayer files two returns and pays each separately. Note that NYC corporations are also subject to the NY State Article 9-A franchise tax (NYC is in NY State) — a NYC corporation pays both Article 9-A and BCT.

### 10.4 Out of scope

- **Deferred NYC topics** — Detailed BCT mechanics, NYC apportionment differences, the GCT/BCT election thresholds, and NYC PTET are deferred to a future nyc-business-corp-tax skill.

### Example 1 — Small NY-only software company

**Facts:** SaaS company, NY-only operations, calendar year 2025.

- Federal taxable income (Line 28, 1120): $800,000.
- State income tax addback: $50,000.
- No GILTI, no related-party addbacks.
- No investment income.
- All customers are NY businesses (single sales factor numerator and denominator both NY).
- NY receipts: $4,200,000.
- Total capital (assets - liabilities, tax basis): $1,500,000.
- Prior-year (2024) NY State franchise tax: $30,000.
- Located in Manhattan (MCTD).

**Step 1 — Business income base:**

- ENI = $800,000 + $50,000 = $850,000.
- Business income = $850,000 (no investment/exempt income).
- BAF = $4,200,000 / $4,200,000 = 100%.
- Apportioned business income = $850,000.
- No NOLs.
- Tax = $850,000 × 6.5% = **$55,250**. (Below $5M business income, so 6.5% applies.)

**Step 2 — Capital base:**

- Business capital = $1,500,000 (no investment capital).
- Apportioned business capital = $1,500,000 × 100% = $1,500,000.
- Tax = $1,500,000 × 0.1875% = **$2,812.50** (well below $5M cap).

**Step 3 — Fixed dollar minimum:**

- NY receipts = $4,200,000.
- Tier: $1M–$5M → **$1,500**.

**Step 4 — Greater of:**

- $55,250 (business income) > $2,812.50 (capital) > $1,500 (FDM).
- **Article 9-A tax = $55,250.**

**Step 5 — MTA surcharge:**

- MCTD apportionment: 100% NY = 100% MCTD (assume all customers in MCTD).
- MCTD-apportioned tax = $55,250.
- Surcharge = $55,250 × 30% = **$16,575**.

**Step 6 — MFI for 2026:**

- Prior-year (2024) NY State tax = $30,000 ≤ $100,000 → MFI = 25%.
- Prior-year tax (used for **2026** MFI) = the 2025 tax just computed = $55,250 → still ≤ $100k → 25% MFI.
- 2026 MFI = $55,250 × 25% = **$13,812.50**, due **March 15, 2026** (CT-300).
- MCTD MFI = $16,575 × 25% = **$4,143.75**, also due March 15, 2026.

**Total 2025 liability:**
- NY State Article 9-A: $55,250.
- MTA surcharge: $16,575.
- **Total NY state-level: $71,825.**
- (Plus separate NYC BCT — not computed here.)

### Example 2 — Mid-sized NY corporation crossing $5M

**Facts:** Engineering services firm, calendar year 2025.

- ENI after modifications: $5,200,000.
- 80% of receipts NY, 20% out-of-state.
- NY receipts: $24,000,000; total receipts: $30,000,000.
- BAF = 80%.
- Business capital = $8,000,000.
- Prior-year (2024) NY State franchise tax: $150,000.
- Operations in Westchester County (MCTD).

**Step 1 — Business income base:**

- Business income = $5,200,000.
- Apportioned = $5,200,000 × 80% = $4,160,000.
- **Test the $5M threshold:** Section 3 says the 7.25% rate applies when **business income** (pre-apportionment) > $5M. Here $5.2M > $5M → 7.25% rate.
- **Important interpretation:** The statute §210.1(a) measures "business income" pre-apportionment for the $5M threshold but applies the 7.25% rate to **apportioned** business income. This is the NY Tax Department's published position (TSB-M-21(1)C).
- Tax = $4,160,000 × 7.25% = **$301,600**.

**Step 2 — Capital base:**

- Apportioned capital = $8,000,000 × 80% = $6,400,000.
- Tax = $6,400,000 × 0.1875% = **$12,000**.

**Step 3 — FDM:**

- NY receipts = $24,000,000 → tier $5M-$25M → **$3,500**.

**Step 4 — Greatest:** $301,600.

**Step 5 — MTA surcharge:**

- Assume MCTD receipts = $15,000,000 (Westchester customers + NYC customers).
- MCTD factor = $15M / $24M (within NY) = 62.5%.
- MCTD-apportioned tax = $301,600 × 62.5% = $188,500.
- Surcharge = $188,500 × 30% = **$56,550**.

**Step 6 — MFI for 2026:**

- Prior-year (2025) tax = $301,600 > $100,000 → **40% MFI**.
- 2026 MFI = $301,600 × 40% = **$120,640**, due **March 15, 2026**.
- MCTD MFI = $56,550 × 40% = **$22,620**.

**Cliff effect note:** If business income had been $4,999,999 instead of $5,200,000, the rate would have been 6.5% — tax = $4,000,000 (apportioned) × 6.5% = $260,000. The marginal effect of crossing $5M of business income: from $260,000 of tax to $301,600 of tax — **$41,600 additional tax** on $200,000 of additional income (effective marginal rate 21%).

**Total 2025 liability:**
- NY State Article 9-A: $301,600.
- MTA surcharge: $56,550.
- **Total state-level: $358,150.**

### Example 3 — Combined group, qualified manufacturer

**Facts:** Holding company HoldCo with two operating subsidiaries OpCo1 and OpCo2, both NY-based, calendar year 2025.

- HoldCo: pure holding, no operations, $0 receipts. Assets: $50M (mostly stock in subs).
- OpCo1: NY-based manufacturer of medical devices. Property in NY at adjusted basis $5M. 90% of receipts from device sales. Gross receipts $40M (all from device sales).
- OpCo2: services subsidiary (engineering services), $5M receipts.
- All three entities are >50% commonly owned (HoldCo owns 100% of each OpCo).
- Engaged in unitary business (vertical: HoldCo finances, OpCo1 manufactures, OpCo2 supports).
- Combined Group ENI: $7,000,000.
- All NY operations.
- Combined NY receipts: $45,000,000; total receipts: $45,000,000.

**Step 1 — Combined filing:** Mandatory combined under §210-C: >50% ownership + unitary. File **CT-3-A** with HoldCo as designated agent.

**Step 2 — Qualified manufacturer test (group-level):**

- OpCo1's manufacturing receipts = $40M.
- Group total receipts = $45M.
- Manufacturing receipts / total = 88.9% > 50%. ✓
- NY property at adjusted basis (OpCo1) = $5M > $1M. ✓
- **Group qualifies as a qualified NY manufacturer.** Apply 0% on business income base.

**Step 3 — Business income base:**

- Apportioned business income = $7,000,000 × ($45M/$45M) = $7,000,000.
- Tax = $7,000,000 × 0% = **$0**.

**Step 4 — Capital base:**

- Combined business capital — assume $30M (with intercompany eliminations).
- Apportioned = $30M × 100% = $30M.
- Tax = $30M × 0.132% (manufacturer rate) = **$39,600** (below $2.5M manufacturer cap).

**Step 5 — FDM (group-level):**

- Group NY receipts = $45M → tier $25M-$50M → base FDM **$5,000**.
- Plus 2 additional members × **$1,500** each = $3,000.
- Total FDM = $5,000 + $3,000 = **$8,000**.

**Step 6 — Greatest of three:** Capital base $39,600 > FDM $8,000 > business income base $0. **Article 9-A tax = $39,600.**

**Step 7 — MTA surcharge:**

- All NY ops in MCTD → 100% MCTD factor.
- Surcharge = $39,600 × 30% = **$11,880**.

**Total combined group 2025 liability:** $39,600 + $11,880 = **$51,480**.

**Observation:** Even with $7M of business income, the manufacturer rate of 0% reduces the business income base to zero, and the combined group pays the **capital base** as its actual liability — a common pattern for asset-heavy qualified manufacturers.

### Example 4 — QETC tech startup

**Facts:** Biotech startup, calendar year 2025.

- ENI: $400,000.
- Product sales: $7M (within QETC $10M cap).
- Primary product: gene-sequencing software (emerging tech under PAL §3102-e).
- All NY operations.
- NY receipts $7M; total receipts $7M.

**Step 1:** QETC qualified — 4.875% rate.

**Step 2 — Business income base:**

- Apportioned business income = $400,000 × 100% = $400,000.
- Tax = $400,000 × 4.875% = **$19,500**.

**Step 3 — FDM:**

- NY receipts $7M → $5M-$25M tier → **$3,500**.

**Step 4 — Greatest:** $19,500.

**Step 5 — MTA (assume in NYC):** $19,500 × 30% = **$5,850**.

**Total:** $25,350.

If the company had been a non-QETC, business income tax would have been $400,000 × 6.5% = $26,000 — QETC saves $6,500 on the business income base.

## 12. PTET (Article 24-A) — Refer Out

- **NY Pass-Through Entity Tax (PTET)** — An elective entity-level tax under Article 24-A that allows partnerships and S-corporations (and LLCs taxed as such) to pay NY personal income tax on behalf of their owners at the entity level, generating a federal deduction (SALT cap workaround). PTET is not an Article 9-A tax and does not apply to C-corporations.  _(Article 24-A)_
- **Article 9-A taxpayer and PTET credit** — An Article 9-A taxpayer (C-corporation) does not pay PTET. However, an Article 9-A taxpayer might be a partner in a partnership that elects PTET — in which case the corporate partner receives a NY tax credit at the corporate level for its allocable share of PTET paid.  _(§606-aa or §187)_

Detailed PTET rules — election, computation, credit flow, due dates, NYC PTET — are deferred to a future `ny-ptet` skill.

### 13.1 Forms

**Forms**

| Form | Purpose |
| --- | --- |
| **CT-3** | General Business Corporation Franchise Tax Return |
| **CT-3-A** | Combined return |
| **CT-3-A/BC** | Member detail for combined return |
| **CT-3-M** | MTA surcharge return |
| **CT-3-S** | S-corporation return (NY S-election — out of scope here) |
| **CT-300** | Mandatory First Installment of Estimated Tax |
| **CT-400** | Estimated Tax Installments (2nd, 3rd, 4th) |
| **CT-5** | Request for 6-month extension |
| **CT-225** | NY State modifications detail |
| **CT-227** | Voluntary contributions |
| **CT-3.1** | Investment and Other Exempt Income / Investment Capital |
| **CT-3.2** | Subtraction modification for qualified emerging technology investments |
| **CT-3.3** | PNOL Conversion Subtraction |
| **CT-3.4** | Net Operating Loss Deduction (current NOLD) |

### 13.2 Due dates

- **CT-3 / CT-3-A due date** — 3½ months after the close of the tax year (April 15 for calendar-year filers).
- **CT-5 extension** — 6-month extension to October 15 — must be filed by the original due date with payment of the balance of estimated tax (the extension is not a payment extension).
- **MFI (CT-300) due date** — March 15 of the succeeding year (i.e., the 2025 MFI for 2026 is paid March 15, 2026).
- **Installments (CT-400) due dates** — June 15, September 15, December 15 (calendar year).

### 13.3 E-filing

- **Mandatory e-filing conditions** — E-filing is mandatory for corporations under Tax Law §29 and 20 NYCRR 2402 if the corporation: Is required to file electronically for federal purposes; or Uses tax preparation software; or Is a member of a combined group. A waiver is available only in narrow circumstances.  _(Tax Law §29; 20 NYCRR 2402)_

### 13.4 Payment

- **Mandatory electronic payment threshold** — 1000000 USD (Electronic payment is mandatory if any single payment exceeds $1,000,000)  _(Tax Law §10)_

### 13.5 Penalties

- **Late filing penalty** — 5% per month, max 25%  _(§1085(a))_
- **Late payment penalty** — 0.5% per month, max 25%  _(§1085(a))_
- **Underpayment of estimated tax penalty** — federal short-term rate + 2%  _(§1085(b))_
- **Failure to file penalty** — minimum $100  _(§1085(a))_
- **Substantial understatement penalty** — 10% of underpayment  _(§1085(k))_
- **Fraud penalty** — 50% of underpayment  _(§1085(j))_

## 14. Investment Capital, Investment Income, and §208(6-a)

The 2015 reform tightened the definition of investment capital and investment income.

### 14.1 Investment capital (§208(5))

- **Investment capital** — Investment capital = stocks (not bonds — bonds are business capital) held by the corporation that: 1. Are not held in the regular course of trade or business (passive holding); 2. Are held for more than one year; 3. Have never been held for sale in the ordinary course; 4. Are clearly identified in the corporation's books as held as investment capital from the date of acquisition; 5. Are not stock issued by the taxpayer. If any one of the five tests is failed, the asset is business capital.  _(§208(5))_

### 14.2 Investment income (§208(6))

- **Investment income** — Income from investment capital — dividends, interest (only on stocks treated as investment capital), and gains/losses on sale. Investment income is excluded from business income (and therefore from the business income base). However, the investment income subtraction under §208(9)(a)(viii) is capped at 8% of ENI for the residual category of investment income — most taxpayers find that strict application of the §208(5) tests excludes most receipts from the investment income category.  _(§208(6); §208(9)(a)(viii))_

### 14.3 Other exempt income — §208(6-a)

- **Exempt CFC income** — 95% of Subpart F income and 95% of GILTI inclusions.  _(§208(6-a)(2))_
- **Exempt unitary corporation dividends** — 100% of dividends from non-combined unitary corporations where the recipient owns ≥ 50% voting power.  _(§208(6-a)(1))_
- **95% GILTI exemption confirmation** — The 95% GILTI exemption was confirmed by the FY2022 budget (S.2509-C/A.3009-C, Part HHH) — NY follows a 95% rather than the federal 50% §250 deduction. The 5% taxed represents an expense disallowance for related deductions.  _(FY2022 budget (S.2509-C/A.3009-C, Part HHH))_

### 14.4 Interest deduction limit — §208(9)(b)(6)

- **Interest deduction disallowance methods** — Interest attributable to investment income / other exempt income / exempt CFC income is disallowed as a business deduction. Two methods to compute the disallowance: 40% safe harbor: disallow 40% of related interest expense. Simpler, often higher. Actual method: trace and disallow only the actual related interest. Lower but requires substantiation.  _(§208(9)(b)(6))_

## 15. Provenance

### Statutory authority

- **Statutory authority list** — NY Tax Law Article 9-A (sections 208-219-a). §208 — definitions. §209 — imposition of tax and nexus. §209-B — MTA surcharge. §210 — computation of tax (the three alternative bases). §210-A — apportionment (single sales factor, market-based sourcing). §210-B — credits (manufacturing credit, ITC, etc. — not detailed in this skill). §210-C — combined reporting. §211 — reports. §213 — taxable years and methods. §213-b — Mandatory First Installment. §1085-§1097 — administration, penalties, interest.  _(NY Tax Law Article 9-A)_

### Regulatory authority

- **Regulatory authority list** — 20 NYCRR Parts 1-12 (Article 9-A regulations). The 2015 reform regulations remained under a draft / consolidated form for several years; the NY Tax Department issued numerous TSB-M memoranda interpreting the reform, including: TSB-M-15(7)C — 2015 reform overview. TSB-M-15(8)C — Apportionment. TSB-M-15(9)C — Investment capital / investment income. TSB-M-19(4)C — GILTI guidance. TSB-M-21(1)C — 7.25% rate and capital base reinstatement. TSB-M-23(1)C — SaaS and digital products sourcing.  _(20 NYCRR Parts 1-12)_

### Annual rate-setting

Form CT-3 instructions (annual) — confirm current-year rates, FDM tiers, MTA surcharge rate. Form CT-300 instructions — MFI thresholds. TSB-M memoranda issued late each year announce next-year MTA surcharge rate.

### Legislative provenance (FY2022–FY2025)

- **FY2022 budget** — FY2022 budget (Chap. 59, Laws of 2021, Part HHH): reinstated 0.1875% capital base; enacted 7.25% rate on >$5M business income; raised top FDM to $200,000; codified PTET (Article 24-A).  _(Chap. 59, Laws of 2021, Part HHH)_
- **FY2023 budget** — FY2023 budget: PTET extensions; small business definitions.
- **FY2024 budget** — FY2024 budget (Chap. 59, Laws of 2023, Part W): extended 7.25% rate and 0.1875% capital base through 2026.  _(Chap. 59, Laws of 2023, Part W)_
- **FY2025 budget** — FY2025 budget (Chap. 59, Laws of 2024): extended 7.25% rate through 2027; MTA payroll mobility tax increase (not Art. 9-A); various credits.  _(Chap. 59, Laws of 2024)_

### Verification before each filing

For tax years 2025+, always reconfirm: 1. Capital base sunset status — historically extended multiple times. 2. 7.25% rate sunset status. 3. MTA surcharge rate (set annually by Commissioner via TSB-M). 4. Economic nexus threshold (indexed annually).

## 16. Disclaimer

This skill provides general guidance on New York Corporate Franchise Tax under Article 9-A as of November 2025 and tax year 2025. It is not a substitute for credentialed professional review. Every output produced using this skill must be reviewed and signed off by a tax professional credentialed under U.S. Circular 230 (Enrolled Agent, CPA, or licensed attorney) and licensed or competent to practice in New York State before the output is delivered to a taxpayer or filed with the New York State Department of Taxation and Finance.

Specific limits and reviewer-required scenarios:

- **Combined reporting with non-U.S. entities** beyond simple water's-edge inclusion — reviewer required.
- **Investment capital / other exempt income** disputes — reviewer required because the §208(5) and §208(6-a) interactions are factually intensive.
- **Manufacturer qualification edge cases** (e.g., mixed manufacturing/services entities, contract manufacturers, third-party-leased property) — reviewer required.
- **PNOL conversion pool** disputes (multi-entity, prior-period adjustments) — reviewer required.
- **Apportionment audits** — NY State has been actively auditing market-based sourcing post-2015 reform; positions taken on customer-location sourcing should be supportable with contemporaneous documentation.
- **Combined group composition disputes** — unitary determinations are factually intensive and require reviewer attention.
- **REIT / RIC / captive REIT** scenarios — refused; out of scope.
- **Mergers, acquisitions, §381/§382 events** affecting NOL availability — reviewer required; out of scope of this skill.
- **Voluntary Disclosure Program** participation — reviewer required.

**Citations to NY Tax Law sections, TSB-M memoranda, and Form CT-3 instructions throughout this skill should be verified against the version of the statute and forms in effect for the tax year being filed.** NY makes frequent annual changes via the budget bill (typically signed in early April); always reconfirm rates, thresholds, and sunset provisions for the year of filing.

End of skill.

- **REIT / RIC / captive REIT scenarios** — Refused; out of scope.  _(Section 16 Disclaimer)_
