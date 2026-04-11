---
name: kansas-sales-tax
description: Use this skill whenever asked about Kansas sales tax, Kansas use tax, KDOR sales tax filing, Kansas grocery tax phase-out, or Kansas sales tax compliance. Trigger on phrases like "Kansas sales tax", "KS sales tax", "KDOR", "K.S.A. §79-3603", "Kansas grocery tax", "Kansas SST", or any request involving Kansas state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Kansas Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Kansas, United States |
| Jurisdiction Code | US-KS |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 6.50% |
| Grocery Food State Rate | 0.00% (effective January 1, 2025 -- phased down from 6.5%) |
| Maximum Combined Rate | ~11.50% (state + county + city + special districts) |
| Primary Statute | Kansas Statutes Annotated (K.S.A.) §79-3603 et seq. |
| Governing Agency | Kansas Department of Revenue (KDOR) |
| Portal | https://www.kdor.ks.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, food rate, basic taxability, filing mechanics. T2: local rate determinations, service taxability, food classification. T3: audit defense, complex exemptions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Kansas sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Kansas sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Kansas? | Drives taxability classification under Kansas law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Kansas? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Kansas local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Kansas imposes a state sales tax of **6.50%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** K.S.A. §79-3603.

### 1.2 Grocery Food Rate -- Phased Reduction to 0% [T1]

Kansas historically taxed grocery food at the full state rate. The legislature enacted a phased reduction:

| Period | State Rate on Grocery Food |
|--------|---------------------------|
| Before January 1, 2023 | 6.50% |
| January 1, 2023 -- December 31, 2023 | 4.00% |
| January 1, 2024 -- December 31, 2024 | 2.00% |
| January 1, 2025 onward | **0.00%** |

- **Local taxes still apply** to grocery food even after the state rate reaches 0%. [T1]
- Prepared food remains taxable at the full 6.5% state rate + local. [T1]
- Candy and soft drinks are excluded from the food definition and remain taxable at the full rate. [T1]

**Statute:** K.S.A. §79-3603(s) as amended by HB 2106 (2022).

### 1.3 Local Sales Taxes [T1]

- Counties, cities, and special districts may impose additional sales tax. [T1]
- Local rates vary significantly; combined rates can exceed **11%**. [T1]
- Kansas has one of the highest combined rate potentials in the country due to stacked local taxes. [T1]
- KDOR administers and collects all local sales taxes. [T1]

### 1.4 Sourcing [T1]

Kansas uses **destination-based** sourcing for most sales. [T1]

As an SST member, Kansas follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- State Exempt (2025+), Local Still Applies [T1]

- As of January 1, 2025, grocery food is **exempt from state sales tax** (0% state rate). [T1]
- **Local taxes still apply** to grocery food. Combined local rates can be 2-4% on food. [T1]
- Prepared food: full 6.5% state + local. [T1]
- Candy: full rate (excluded from food definition). [T1]
- Soft drinks: full rate. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the standard rate. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. K.S.A. §79-3606(d). [T1]
- OTC drugs: **taxable**. [T1]
- DME with prescription: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Kansas taxes relatively few services:

- **Taxable services include:** Admission to places of amusement, telecommunications, cable TV, car washing, laundry/dry cleaning (coin-operated exempt). [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), repair and maintenance labor, cleaning/janitorial, personal care. [T2]
- **Installation labor:** Exempt when separately stated from taxable materials. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** in Kansas. K.S.A. §79-3603 does not enumerate SaaS. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. [T1]
- **Digital downloads:** Taxable as specified digital products under SST definitions. [T1]
- **Streaming services:** Taxable. [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T2]

- Machinery and equipment used directly in manufacturing: **exempt**. K.S.A. §79-3606(kk). [T1]
- Consumables used in manufacturing (lubricants, chemicals): exempt when consumed in the manufacturing process. [T2]
- Utilities (electricity, gas) used in manufacturing: exempt for the portion used in production. [T2]

### 2.7 Agricultural [T1]

- Farm machinery and equipment: exempt. K.S.A. §79-3606(b). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | ST-36 (Kansas Sales Tax Return) |
| Filing Frequencies | Monthly (>$3,200/year liability); Quarterly ($800-$3,200); Annually (<$800) |
| Due Date | 25th of the month following the reporting period |
| Portal | https://www.kdor.ks.gov/Apps/kcsc/login.aspx (Kansas Customer Service Center) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Kansas does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing/payment penalty: 1% per month, up to 24%. [T1]
- Interest: rate set annually, typically around 6-8% per annum. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Kansas. Key categories: [T1]

- **Resale exemption:** Valid resale certificate required. Retain for the statutory period. [T1]
- **Exempt organizations:** Government entities and qualifying nonprofits -- require exemption certificate on file. [T1]
- **Agricultural exemptions:** Where applicable per Step 2. [T1]
- **Manufacturing exemptions:** Where applicable per Step 2. [T2]

All exemption certificates must be collected at or before the time of sale and retained per the state's statute of limitations. [T1]


---

## Step 5: Key Thresholds
### 3.1 Economic Nexus Threshold [T1]

| Field | Detail |
|-------|--------|
| Revenue Threshold | $100,000 in Kansas sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2021 |

**Statute:** K.S.A. §79-3702(h).

**Note:** Kansas was one of the later states to adopt economic nexus. [T1]

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. [T1]

### 3.3 Marketplace Facilitator [T1]

Kansas requires marketplace facilitators to collect and remit sales tax. Effective July 1, 2021. K.S.A. §79-3702(i). [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply the pre-2025 state rate to grocery food. The state rate on food is 0% effective January 1, 2025. [T1]
- NEVER forget that local taxes still apply to grocery food, even though the state rate is 0%. [T1]
- NEVER classify candy or soft drinks as "food" for the reduced/exempt rate. They are taxed at the full state + local rate. [T1]
- NEVER assume a uniform rate across Kansas. Local taxes vary significantly by address. [T1]
- NEVER ignore Kansas's late adoption of economic nexus (July 1, 2021). Historical analysis may differ from current rules. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Grocery Food During Rate Phase-Down [T2]

**Situation:** A grocery retailer needs to configure POS systems for the phased grocery food rate reduction.

**Resolution:**
- As of January 1, 2025, the state rate on grocery food is 0%. [T1]
- Local taxes continue to apply to grocery food at the full local rate. [T1]
- POS systems must be configured to apply 0% state + applicable local rate on food items, and the full 6.5% state + local on non-food items. [T1]
- Candy and soft drinks must be mapped to the FULL rate (not the food rate). [T1]
- **Flag for reviewer:** Verify that the retailer's item classification matches the SST food definitions. Misclassified items will result in over- or under-collection. [T2]

### EC2 -- High Combined Rates in Kansas [T2]

**Situation:** A buyer in a Kansas city with a 10.5% combined rate purchases a $1,000 item. They question why the rate is so high.

**Resolution:**
- Kansas allows stacking of state (6.5%) + county + city + special district taxes. [T1]
- Some jurisdictions have combined rates exceeding 10%. [T1]
- Rates vary by precise delivery address. [T1]
- Sellers must use rate lookup tools or SST-certified rate tables. [T1]
- **Flag for reviewer:** Always verify the exact combined rate for the delivery address. Kansas rate lookups are available at https://www.kdor.ks.gov. [T2]

### EC3 -- Remote Seller and Late Economic Nexus Adoption [T2]

**Situation:** A remote seller established nexus in Kansas in 2020 (before the July 2021 economic nexus law). Did they have a collection obligation?

**Resolution:**
- Before July 1, 2021, Kansas did not have an economic nexus law. [T1]
- Remote sellers without physical nexus had no Kansas collection obligation before that date. [T1]
- Some sellers may have voluntarily collected. [T2]
- After July 1, 2021, the $100,000 threshold applies. [T1]
- **Flag for reviewer:** If a seller had physical nexus (e.g., FBA inventory), the obligation existed before the economic nexus law. [T2]

### EC4 -- Exempt Food vs. Taxable Prepared Food at a Grocery Deli [T2]

**Situation:** A grocery store sells unheated deli sandwiches, heated rotisserie chickens, and bagged salad kits at its deli counter.

**Resolution:**
- Unheated deli sandwiches sold without utensils: may qualify as food (0% state + local). [T2]
- Heated rotisserie chickens: prepared food (6.5% state + local). [T1]
- Bagged salad kits (not mixed for immediate consumption): food (0% state + local). [T1]
- The determination hinges on SST definitions of "prepared food" (heated by seller, utensils provided, or two+ ingredients mixed for immediate consumption). [T2]
- **Flag for reviewer:** Review each item against SST prepared food definitions. [T2]

---

### EC5 -- Catering and Prepared Food at Events [T2]

**Situation:** A caterer provides food for a corporate event in Kansas City, KS. The invoice includes both prepared food ($3,000) and unprepared items like fruit trays ($500).

**Resolution:**
- Prepared food (heated, with utensils, mixed for immediate consumption): full 6.5% state + local. [T1]
- Unprepared fruit trays (not heated, no utensils): 0% state + local only (food rate). [T1]
- If items are bundled at a single price, bundled transaction rules under SST apply. [T2]
- **Flag for reviewer:** Caterers should separately state prepared and unprepared food on invoices. [T2]

### EC6 -- Manufacturing Equipment Exemption Documentation [T2]

**Situation:** A manufacturer claims the exemption on production equipment but the auditor questions whether the equipment is used "directly" in manufacturing.

**Resolution:**
- Equipment must be used directly and primarily in manufacturing to qualify. [T1]
- Office equipment, vehicles, and general-purpose items do NOT qualify. [T1]
- Pollution control equipment: may qualify if directly related to the manufacturing process. [T2]
- The manufacturer must maintain documentation of the equipment's use. [T2]
- **Flag for reviewer:** Maintain detailed records of equipment use percentages. Mixed-use equipment is a common audit issue. [T2]

---

## Test Suite

### Test 1 -- General Merchandise Sale

**Input:** Seller in Wichita sells $500 of office supplies. Combined rate = 7.5% (6.5% state + 1% local).
**Expected output:** Tax = $500 x 7.5% = $37.50. Total = $537.50.

### Test 2 -- Grocery Food (2025+ Rate)

**Input:** Customer buys $200 of unprepared groceries in Topeka. State food rate = 0%. Local rate = 1.5%.
**Expected output:** State tax = $0. Local tax = $200 x 1.5% = $3.00. Total = $203.00.

### Test 3 -- Candy at Full Rate

**Input:** Customer buys $10 of candy at a Wichita store. Combined rate = 7.5%.
**Expected output:** Candy is NOT food. Full rate applies. Tax = $10 x 7.5% = $0.75. Total = $10.75.

### Test 4 -- Economic Nexus Determination

**Input:** Remote seller from Oregon had $120,000 in Kansas sales in the prior year.
**Expected output:** $120,000 exceeds $100,000 threshold. Nexus IS triggered. Must register and collect.

### Test 5 -- Prescription Drug Exemption

**Input:** Pharmacy sells $200 prescription and $30 OTC medication. Combined rate = 7.5%.
**Expected output:** Prescription: exempt. OTC: taxable. Tax = $30 x 7.5% = $2.25. Total = $232.25.

---

### Test 6 -- Prepared Food at Full Rate

**Input:** Customer buys a $12 prepared meal at a Topeka restaurant. Combined rate = 9.15% (6.5% state + 2.65% local).
**Expected output:** Prepared food at full combined rate. Tax = $12 x 9.15% = $1.10. Total = $13.10.

### Test 7 -- Use Tax on Out-of-State Purchase

**Input:** Kansas business purchases $8,000 of equipment from an Oregon vendor (no tax collected). Business combined rate = 7.5%.
**Expected output:** Use tax due = $8,000 x 7.5% = $600.00. Reported on ST-36.

### Test 8 -- Manufacturing Equipment Exemption

**Input:** Manufacturer buys $200,000 production line equipment for Kansas plant.
**Expected output:** Manufacturing equipment is exempt. Tax = $0.

---

## Reviewer Escalation Protocol

| Trigger | Action |
|---------|--------|
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

---

## Contribution Notes

- This skill follows the Q1 execution format (Step 0 through Step 7).
- All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
- Rate tables are deterministic lookup tables -- no narrative explanation of rates.
- To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
- All changes require validation by a US CPA or EA before merging.

---

## Disclaimer
This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
