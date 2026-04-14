---
name: us-sales-tax
description: Use this skill whenever asked about United States sales tax, use tax, sales tax nexus, multi-state tax compliance, sales tax returns, exemption certificates, taxability of goods or services, economic nexus, or any request involving US state-level consumption taxes. Trigger on phrases like "sales tax", "use tax", "nexus", "Wayfair", "sales tax return", "exemption certificate", "resale certificate", "taxability", "sales tax rate", "marketplace facilitator", "Streamlined Sales Tax", "SST", or any request involving US state sales and use tax filing, classification, or compliance. This skill contains the complete US sales and use tax framework. ALWAYS read this skill before touching any US sales tax work.
version: 2.0
---

# United States Sales and Use Tax Framework Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | United States of America |
| Tax type | Sales and Use Tax (state-level; no federal equivalent) |
| States with general sales tax | 45 states + DC |
| States with NO general sales tax | Alaska (AK), Delaware (DE), Montana (MT), New Hampshire (NH), Oregon (OR) |
| Key federal precedent | South Dakota v. Wayfair, Inc., 585 U.S. ___ (2018) |
| Industry body | Streamlined Sales Tax Governing Board (SSTGB) |
| Approximate tax jurisdictions | ~13,000 distinct (state + county + city + special district) |
| Typical state rate range | 2.9% (Colorado) -- 7.25% (California) |
| Maximum combined rates | 10%+ in some jurisdictions |
| Federal framework skill | This IS the framework skill |
| Skill version | 2.0 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs for multi-state analysis

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Which states do you sell into? | Determines which state skills to load |
| 2 | What do you sell (TPP, services, digital goods)? | Taxability varies dramatically by state |
| 3 | Annual revenue by state? | Determines economic nexus in each state |
| 4 | Transaction counts by state? | Some states use transaction thresholds |
| 5 | Physical presence in which states? | Creates nexus independent of economic thresholds |
| 6 | Use marketplace facilitators? | Facilitators collect in most states |
| 7 | Ship from which locations? | Affects sourcing rules (origin vs. destination) |

### Refusal catalogue

**R-US-1 -- Import duties and customs.** Federal customs duties are outside scope. Refer to customs broker.

**R-US-2 -- Excise taxes.** Federal excise taxes (fuel, alcohol, tobacco, firearms) are separate. Outside scope.

**R-US-3 -- Property tax.** Real and personal property taxes are separate. Outside scope.

---

## Section 3 -- Transaction pattern library (cross-state reference)

This table provides the default taxability pattern across US states. Always verify with the state-specific skill.

### 3.1 SaaS / cloud software

| State group | SaaS taxable? |
|---|---|
| TAXABLE: NY, TX, WA, PA, CT, OH, SC, TN, UT, SD, ND, HI, NM, WV, RI, DC, AZ, IA, KY, MS, NE | Yes |
| NOT TAXABLE: CA, IL, CO, GA, MO, VA, MN, NC, MI, OK, OR, IN, WI, AR, KS, ME, VT | No or unclear |
| 20% EXEMPT: TX | Data processing services 80% taxable |

### 3.2 Food (grocery, unprepared)

| Treatment | States |
|---|---|
| EXEMPT | Most states (CA, NY, FL, TX, PA, OH, NJ, MA, etc.) |
| TAXABLE at reduced rate | IL (1%), VA (1%), AR (0.125%), MO (1.225%), TN (4%), KS (varying) |
| FULLY TAXABLE | AL, MS, SD, OK (state level), HI |

### 3.3 Clothing

| Treatment | States |
|---|---|
| EXEMPT (all clothing) | PA, NJ, MN |
| EXEMPT under threshold | NY (under $110/item), MA (under $175/item), VT (under $110), RI (under $250) |
| FULLY TAXABLE | CA, TX, FL, IL, WA, OH, GA, NC, and most other states |
| Holiday exemption only | TX, FL, and several other states with temporary sales tax holidays |

### 3.4 Digital goods (downloads)

| State group | Taxable? |
|---|---|
| TAXABLE: WA, NY, TX, NJ, CT, TN, UT, WI, KY, NE, SD, ND, HI, NM | Yes |
| NOT TAXABLE: CA (streaming), IL (streaming), GA, MO, OR | Generally no |

### 3.5 Professional services

| Treatment | Notes |
|---|---|
| NOT TAXABLE | Vast majority of states do not tax professional services |
| BROADLY TAXABLE | HI, NM, SD, WV tax most services including professional |

### 3.6 Manufacturing equipment

| Treatment | States |
|---|---|
| FULLY EXEMPT | Most states provide full or substantial exemption |
| PARTIAL EXEMPTION | CA (state rate reduced, district tax applies) |

---

## Section 4 -- Rate lookup (state-level reference)

### 4.1 State base rates

| State | Rate | State | Rate | State | Rate |
|---|---|---|---|---|---|
| AL | 4.00% | KY | 6.00% | ND | 5.00% |
| AZ | 5.60% | LA | 4.45% | NE | 5.50% |
| AR | 6.50% | ME | 5.50% | NV | 6.85% |
| CA | 7.25% | MD | 6.00% | NH | None |
| CO | 2.90% | MA | 6.25% | NJ | 6.625% |
| CT | 6.35% | MI | 6.00% | NM | 5.125% |
| DC | 6.00% | MN | 6.875% | NY | 4.00% |
| DE | None | MS | 7.00% | NC | 4.75% |
| FL | 6.00% | MO | 4.225% | OH | 5.75% |
| GA | 4.00% | MT | None | OK | 4.50% |
| HI | 4.00% | OR | None | PA | 6.00% |
| ID | 6.00% | RI | 7.00% | SC | 6.00% |
| IL | 6.25% | SD | 4.50% | TN | 7.00% |
| IN | 7.00% | TX | 6.25% | UT | 6.10% |
| IA | 6.00% | VT | 6.00% | VA | 5.30% |
| KS | 6.50% | WA | 6.50% | WV | 6.00% |
| WI | 5.00% | WY | 4.00% | AK | None (local only) |
| MN | 6.875% | | | | |

### 4.2 Sourcing rules overview

| Type | States |
|---|---|
| Destination-based | Most states (CA for district taxes, NY, FL, WA, and SST states) |
| Origin-based (intrastate) | TX, IL, OH, PA, VA, MS, MO, TN, AZ |
| Mixed | Some states use origin for intrastate, destination for interstate |

---

## Section 5 -- Classification rules

### 5.1 Sales tax vs. use tax

Sales tax: collected by seller at point of sale. Use tax: owed by buyer when sales tax was not collected. Rates are identical within a jurisdiction. You pay one or the other, never both.

### 5.2 Tax base

Sales tax generally applies to retail sale of tangible personal property (TPP). Service taxation varies enormously by state. Digital goods and SaaS are evolving and inconsistent.

### 5.3 Nexus types

| Type | Description |
|---|---|
| Physical nexus | Offices, employees, inventory, property, representatives in the state |
| Economic nexus (post-Wayfair) | Revenue and/or transaction thresholds met |
| Click-through nexus | Referral agreements with in-state entities |
| Affiliate nexus | Related entities with in-state presence |
| Marketplace nexus | Selling through marketplace facilitator |

### 5.4 Economic nexus thresholds (common patterns)

| Threshold | States |
|---|---|
| $100K OR 200 transactions | Most states (SD, IN, IA, KY, ME, etc.) |
| $100K only (no transaction count) | FL, WA, NV, TX (uses $500K), CA ($500K) |
| $500K | CA, TX |
| $500K AND 100 transactions | NY (AND test -- unique) |

---

## Section 6 -- Return form and filing

### 6.1 Filing overview

Each state has its own return form. Common elements: gross sales, exempt sales, taxable sales, tax collected, local tax breakdown, use tax.

### 6.2 Marketplace facilitator impact

In all states with marketplace facilitator laws (all 45 + DC as of 2024), the marketplace collects on facilitated sales. Sellers file for direct sales only.

### 6.3 SST centralized registration

Remote sellers can register in all 24 SST member states through a single application at https://www.sstregister.org.

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Wayfair decision (2018)

States may require remote sellers to collect sales tax if they meet economic nexus thresholds, even without physical presence. All 45 sales tax states + DC have enacted post-Wayfair economic nexus laws.

### 7.2 Common penalty patterns

| Penalty type | Typical range |
|---|---|
| Late filing | 5-10% of tax due |
| Late payment | 5-10% of tax due |
| Fraud | 25-100% of deficiency |
| Interest | State-set rates, adjusted periodically |

### 7.3 Voluntary disclosure agreements (VDA)

Most states offer VDAs for sellers who discover past-due nexus obligations. Benefits: penalty waiver, limited lookback (typically 3-4 years).

---

## Section 8 -- Edge cases

### EC1 -- Multi-state seller nexus analysis

**Situation:** E-commerce seller with $2M in national sales ships to all 50 states.
**Resolution:** Must analyze economic nexus in each state individually. Revenue/transaction thresholds differ by state. Marketplace sales (Amazon, etc.) typically handled by the marketplace.

### EC2 -- SaaS taxability varies by state

**Situation:** SaaS company sells nationwide.
**Resolution:** SaaS is taxable in approximately 20+ states. Must determine taxability state by state. TX provides 20% exemption. CA and IL generally do not tax pure SaaS.

### EC3 -- Drop shipments

**Situation:** Retailer in State A directs supplier in State B to ship to customer in State C.
**Resolution:** Three-party arrangement. Taxability depends on where nexus exists and which exemption certificates are provided. Complex area requiring state-specific analysis.

### EC4 -- No-sales-tax state sellers

**Situation:** Oregon seller ships to customers in other states.
**Resolution:** Oregon's lack of sales tax does NOT relieve the seller of collection obligations in states where they have nexus.

---

## Section 9 -- Test suite

### Test 1 -- Economic nexus determination

**Input:** Seller has $150K in FL sales, $90K in NY sales, $80K in CA sales.
**Expected:** FL: nexus ($100K met). NY: no nexus (need $500K AND 100 transactions). CA: no nexus (need $500K).

### Test 2 -- SaaS multi-state

**Input:** SaaS company with customers in NY, CA, and IL.
**Expected:** NY: taxable. CA: not taxable (pure SaaS). IL: not taxable (pure cloud, no download).

### Test 3 -- Food taxability

**Input:** Grocery food sold in IL, TX, and AL.
**Expected:** IL: 1% reduced rate. TX: exempt. AL: fully taxable.

### Test 4 -- Clothing taxability

**Input:** $200 jacket sold in NY, PA, and CA.
**Expected:** NY: taxable (over $110). PA: exempt. CA: taxable.

### Test 5 -- Marketplace facilitator

**Input:** Seller makes $80K on Amazon, $30K direct, in a $100K nexus state.
**Expected:** Amazon collects on $80K. Seller must analyze if $30K direct creates separate nexus.

---

## Section 10 -- Prohibitions

- NEVER assume a single federal sales tax rate -- there is no federal sales tax.
- NEVER apply one state's rules to another state -- each state is independent.
- NEVER assume SaaS taxability is uniform across states.
- NEVER assume food is always exempt -- several states tax it.
- NEVER assume clothing is always taxable -- several states exempt it.
- NEVER ignore local taxes -- they can add 0.5% to 5%+ to the state rate.
- NEVER assume marketplace sellers have no obligations -- direct sales may still require collection.
- NEVER forget use tax -- buyers owe it when sales tax was not collected.
- NEVER treat economic nexus thresholds as uniform -- they range from $100K to $500K with varying tests.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
