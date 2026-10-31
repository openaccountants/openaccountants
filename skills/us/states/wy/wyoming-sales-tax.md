---
name: wyoming-sales-tax
description: Use this skill whenever asked about Wyoming sales tax, Wyoming use tax, Wyoming DOR sales tax filing, or Wyoming sales tax compliance. Trigger on phrases like "Wyoming sales tax", "WY sales tax", "W.S. §39-15", "Wyoming DOR", "Wyoming no income tax", "Wyoming SST", or any request involving Wyoming state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
jurisdiction: US-WY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Wyoming Sales Tax

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Wyoming, United States |
| Jurisdiction Code | US-WY |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.00% |
| Local Rate | Up to 2.00% (county option) |
| Maximum Combined Rate | 6.00% |
| Primary Statute | Wyoming Statutes (W.S.) §39-15-101 et seq. |
| Governing Agency | Wyoming Department of Revenue (DOR) |
| Portal | https://revenue.wyo.gov |
| SST Member | Yes -- Full Member |
| No State Income Tax | Yes |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determination, mineral/energy industry, service taxability. T3: audit defense, complex energy transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

## Confidence Tier Definitions

- **T1 Tier 1 -- Deterministic** — Apply exactly as written. No reviewer judgement required.
- **T2 Tier 2 -- Reviewer Judgement Required** — Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **T3 Tier 3 -- Out of Scope / Escalate** — Do not guess. Escalate to a licensed tax professional.

## Step 0: Client Onboarding Questions

Before proceeding with any Wyoming sales tax analysis, collect the following from the client: [T1]

**Onboarding Questions**

| # | Question | Why It Matters |
| --- | --- | --- |
| 1 | Do you have a Wyoming sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Wyoming? | Drives taxability classification under Wyoming law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Wyoming? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Wyoming local jurisdictions? | Local tax rates vary; determines compliance complexity. |

- **Incomplete onboarding** — If the client cannot answer questions 1-4, STOP and gather this information before proceeding. (T1)

## Step 1: Tax Rate Structure

### 1.1 State Sales Tax Rate

- **State Sales Tax Rate** — 4.00% (T1)  _(W.S. §39-15-104.)_

Wyoming imposes a state sales tax of 4.00% on the retail sale of tangible personal property and certain services. [T1]

### 1.2 No State Income Tax [T1]

- **No State Income Tax** — Wyoming has no state individual or corporate income tax. Sales tax, mineral severance taxes, and property taxes are the primary revenue sources. (T1)

### 1.3 Local Sales Taxes [T1]

- **County additional tax** — Counties may impose additional sales tax up to 2.00% (general purpose + specific purpose). (T1)
- **Most counties impose local option tax** — Most counties impose some form of local option tax. (T1)
- **Combined rate range** — Combined rates range from 4.00% to 6.00%. (T1)
- **Local tax administration** — Local taxes are administered by the Wyoming DOR. (T1)

### 1.4 Sourcing [T1]

- **Sourcing method** — Wyoming uses destination-based sourcing. (T1)
- **SST sourcing rules** — As an SST member, Wyoming follows SSUTA sourcing rules. (T1)

## Step 2: Transaction Classification Rules

### 2.1 Grocery Food -- EXEMPT [T1]

- **Unprepared grocery food** — Exempt. (T1)  _(W.S. §39-15-105(a)(viii).)_
- **Prepared food** — Taxable at full combined rate. (T1)
- **Candy** — Taxable. (T1)
- **Soft drinks** — Taxable. (T1)
- **SST food definitions** — Wyoming follows SST food definitions. (T1)

### 2.2 Clothing [T1]

- **Clothing taxability** — Clothing is fully taxable. No exemption. (T1)

### 2.3 Prescription Drugs and Medical [T1]

- **Prescription drugs** — Exempt. (T1)  _(W.S. §39-15-105(a)(iv).)_
- **OTC drugs** — Taxable. (T1)
- **DME** — Exempt with prescription. (T1)
- **Prosthetics** — Exempt. (T1)

### 2.4 Services [T2]

Wyoming taxes a limited number of services:

- **Taxable services** — Intrastate telecommunications, public utilities, lodging, admissions/amusements. (T2)
- **Exempt services** — Professional services, personal care, repair labor, cleaning, landscaping, IT services. (T2)
- **Narrow service tax base** — Wyoming has a narrow service tax base focused on TPP and a few enumerated services. (T2)

### 2.5 SaaS and Digital Goods [T2]

- **SaaS** — Generally not taxable in Wyoming. Not considered TPP or an enumerated service. (T2)
- **Canned software (physical)** — Taxable. (T1)
- **Canned software (electronic delivery)** — Generally not taxable under current law. (T2)
- **Digital downloads** — Generally not taxable. Wyoming has not broadly adopted digital goods taxation. (T2)
- **Custom software** — Exempt. (T2)

### 2.6 Manufacturing [T2]

- **No broad manufacturing equipment exemption** — Wyoming does NOT have a broad manufacturing equipment exemption. (T2)
- **Specific incentive programs** — Some equipment may qualify under specific incentive programs. (T2)
- **Raw materials for resale** — Exempt under resale exemption. (T1)

### 2.7 Mineral and Energy Industry [T2]

- **Economy reliance on mineral extraction** — Wyoming's economy is heavily reliant on mineral extraction (coal, oil, gas, trona, uranium). (T1)
- **Mining and drilling equipment** — Generally taxable at the full combined rate. (T2)
- **Mineral severance taxes** — Mineral severance taxes (coal, oil, gas, trona) are separate from sales tax. (T1)
- **Wind energy equipment** — May qualify for specific exemptions under economic development incentives. (T2)
- **Flag for reviewer** — Mineral/energy tax compliance involves multiple tax types. Escalate complex scenarios. (T3)

### 2.8 Agricultural [T1]

- **Farm and ranch machinery and equipment** — Exempt. (T1)  _(W.S. §39-15-105(a)(vi).)_
- **Feed, seed, fertilizer** — Exempt. (T1)
- **Livestock** — Exempt for breeding/production. (T1)

## Step 3: Return Form Structure

### 4.1 Filing Details [T1]

**Filing Details**

| Field | Detail |
| --- | --- |
| Return Form | Sales/Use Tax Return (filed via WyoTax) |
| Filing Frequencies | Monthly (>$300/month avg tax); Quarterly ($100-$300); Annually (<$100) |
| Due Date | Last day of the month following the reporting period |
| Portal | https://excise.wyo.gov (WyoTax) |
| E-filing | Required for most filers |

- **Due date note** — Wyoming's due date is the last day of the following month. (T1)

### 4.2 Vendor Discount [T1]

- **Vendor Discount** — 1.95% percent of tax collected (T1, capped at $500/month)

### 4.3 Penalties and Interest [T1]

- **Late filing penalty** — 10% of tax due (minimum $25). (T1)
- **Interest rate** — 1% per month (12% per annum). (T1)

## Step 4: Deductibility / Exemptions

Exemptions identified in Step 2 above are the primary deductibility rules for Wyoming. Key categories: [T1]

- **Resale exemption** — Valid resale certificate required. Retain for the statutory period. (T1)
- **Exempt organizations** — Government entities and qualifying nonprofits -- require exemption certificate on file. (T1)
- **Agricultural exemptions** — Where applicable per Step 2. (T1)
- **Manufacturing exemptions** — Where applicable per Step 2. (T2)
- **Exemption certificate retention** — All exemption certificates must be collected at or before the time of sale and retained per the state's statute of limitations. (T1)

## Step 5: Key Thresholds

### 3.1 Economic Nexus Threshold [T1]

**Economic Nexus Threshold**  _(W.S. §39-15-501(a)(viii).)_

| Field | Detail |
| --- | --- |
| Revenue Threshold | $100,000 in Wyoming sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | February 1, 2019 |

### 3.2 Marketplace Facilitator [T1]

- **Marketplace facilitator collection obligation** — Wyoming requires marketplace facilitators to collect and remit. (T1)  _(W.S. §39-15-501(a)(ix).)_

### 3.3 SST Registration [T1]

- **SST registration status** — Full SST member. SSTRS and CSPs available. (T1)

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

## PROHIBITIONS

- **Grocery food taxation** — NEVER tax grocery food in Wyoming. Unprepared food is exempt. (T1)
- **Uniform 4% rate assumption** — NEVER assume a uniform 4% rate across Wyoming. County taxes add up to 2%. (T1)
- **SaaS taxability assumption** — NEVER assume SaaS is taxable in Wyoming. Current law does not tax SaaS. (T2)
- **Mineral/energy context** — NEVER ignore the mineral/energy industry context. Wyoming's economy and tax structure revolve around natural resources. (T2)
- **Filing deadline** — NEVER file Wyoming returns by the 20th. The due date is the last day of the following month. (T1)
- **No computation by Claude** — NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. (T1)

## Edge Case Registry

### EC1 -- No Income Tax + Low Sales Tax [T1]

A business considers incorporating or relocating to Wyoming for tax advantages.

- **No income tax** — Wyoming has no individual or corporate income tax. (T1)
- **Moderate sales tax rates** — Sales tax rates are moderate (4% state + up to 2% local = max 6%). (T1)
- **Other tax types to consider** — However, mineral severance taxes, property taxes, and the Commerce Tax equivalent should be considered. (T2)
- **Popular for LLCs and holding companies** — Wyoming is a popular state for LLCs and holding companies due to privacy laws and no income tax. (T1)
- **Flag for reviewer** — Total tax burden analysis requires evaluating all tax types, not just sales tax. (T2)

### EC2 -- Energy Industry Equipment [T2]

An oil company purchases $2 million in drilling equipment for use in Wyoming.

- **Drilling equipment taxability** — Drilling equipment is generally subject to sales tax at the full combined rate. (T2)
- **No broad exemption** — No broad manufacturing/mining equipment exemption exists. (T2)
- **Mineral severance taxes on production** — The oil company also faces mineral severance taxes on production. (T1)
- **Specific incentive programs** — Specific incentive programs may provide relief for certain types of equipment. (T2)
- **Flag for reviewer** — Verify whether any specific exemptions or incentive programs apply to the equipment type. (T2)

### EC3 -- SaaS Not Taxable [T2]

A technology company asks whether its SaaS product sold to Wyoming customers is taxable.

- **SaaS taxability** — SaaS is generally NOT taxable in Wyoming under current law. (T2)
- **Sales tax base focus** — Wyoming's sales tax base focuses on TPP and limited enumerated services. (T2)
- **Monitor legislative changes** — The company should still monitor for legislative changes. (T2)
- **Flag for reviewer** — Wyoming's position on SaaS and digital goods is evolving. Verify current DOR guidance. (T2)

### EC4 -- Agricultural Equipment Exemption [T1]

A rancher purchases a new tractor for $60,000 for use on a cattle ranch.

- **Farm and ranch machinery exempt** — Farm and ranch machinery is exempt from sales tax. (T1)  _(W.S. §39-15-105(a)(vi).)_
- **Bona fide agricultural producer** — The rancher must qualify as a bona fide agricultural producer. (T1)
- **Used in agricultural production** — The equipment must be used in agricultural production. (T1)
- **Mixed-use vehicle** — A mixed-use vehicle used partly for personal purposes may not fully qualify. (T2)
- **Flag for reviewer** — Verify agricultural producer status and primary use of the equipment. (T2)

### EC5 -- Wind Farm Equipment [T2]

A wind energy company purchases $5 million in wind turbines and related equipment for a Wyoming wind farm.

- **Wind energy tax incentives** — Wyoming may offer tax incentives for wind energy development. (T2)
- **Default taxability** — Without a specific exemption, equipment is subject to sales tax at the combined rate. (T2)
- **Check incentive programs** — Check current economic development incentive programs for renewable energy. (T2)
- **Flag for reviewer** — Wind energy incentives change with legislative sessions. Verify current programs with Wyoming DOR or WYDEQ. (T2)

### EC6 -- Tourism and Lodging in Jackson Hole [T2]

A hotel in Jackson, WY charges $400/night. What taxes apply?

- **State sales tax** — 4% (T1)
- **Teton County optional tax** — up to 2% (T1)
- **No separate state lodging tax** — Wyoming does not impose a separate state lodging tax. (T1)
- **Local lodging taxes** — Local lodging taxes may apply (varies by county/city). (T2)
- **Combined tax dependency** — Combined tax on lodging depends on the specific jurisdiction. (T2)
- **Flag for reviewer** — Jackson/Teton County is a high-tourism area. Verify all applicable local taxes. (T2)

### EC7 -- Use Tax on Cross-Border Personal Purchases [T1]

A Wyoming resident purchases furniture in Montana (no sales tax) and brings it to Wyoming.

- **Use tax due** — Wyoming use tax is due on the purchase at the applicable combined rate. (T1)
- **No credit for Montana tax** — No credit for Montana tax (Montana has no sales tax, so $0 was paid). (T1)
- **Reporting obligation** — The resident should report and remit use tax. (T1)
- **Flag for reviewer** — Montana has no sales tax, so no credit applies. Full Wyoming use tax is due. (T1)

## Test Suite

### Test 1 -- Basic Taxable Sale

Input: Seller in Cheyenne sells $800 of equipment. Combined rate = 6% (4% state + 2% local).
Expected output: Tax = $800 x 6% = $48.00. Total = $848.00.

### Test 2 -- Grocery Food Exempt

Input: Customer buys $200 groceries in Casper.
Expected output: Groceries are EXEMPT. Tax = $0. Total = $200.00.

### Test 3 -- Farm Equipment Exempt

Input: Rancher buys a $40,000 tractor for ranch use.
Expected output: Farm machinery is exempt. Tax = $0. Total = $40,000.00.

### Test 4 -- Economic Nexus

Input: Remote seller sold $105,000 to Wyoming in the prior year.
Expected output: $105,000 exceeds $100,000 threshold. Nexus IS triggered. Must register and collect.

### Test 5 -- Clothing Taxable

Input: Customer buys $300 jacket in Jackson. Combined rate = 6%.
Expected output: Clothing IS taxable. Tax = $300 x 6% = $18.00. Total = $318.00.

### Test 6 -- Lodging in Jackson

Input: Guest stays 3 nights at a Jackson hotel at $350/night. Combined rate = 6%.
Expected output: Room = $1,050. Tax = $1,050 x 6% = $63.00. Total = $1,113.00.

### Test 7 -- Use Tax from Montana Purchase

Input: Wyoming resident buys $2,000 furniture in Montana (no tax paid). WY combined rate = 6%.
Expected output: Use tax = $2,000 x 6% = $120.00. No credit (MT has no sales tax).

### Test 8 -- Vendor Discount Calculation

Input: Wyoming seller collects $10,000 in tax for the month and files on time.
Expected output: Vendor discount = $10,000 x 1.95% = $195.00. Seller remits $10,000 - $195 = $9,805.00.

## Reviewer Escalation Protocol

**Reviewer Escalation Protocol**

| Trigger | Action |
| --- | --- |
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

## Contribution Notes

This skill follows the Q1 execution format (Step 0 through Step 7).
All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
Rate tables are deterministic lookup tables -- no narrative explanation of rates.
To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
All changes require validation by a US CPA or EA before merging.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
