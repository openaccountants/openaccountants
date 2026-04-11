---
name: new-zealand-gst
description: Use this skill whenever asked to prepare, review, or create a New Zealand GST return (GST101A form) for any client. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", or any request involving New Zealand GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill contains the complete NZ GST classification rules, return field mappings, input tax credit rules, change-of-use adjustment mechanics, zero-rating rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any NZ GST-related work.
---

# New Zealand GST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New Zealand |
| Jurisdiction Code | NZ |
| Primary Legislation | Goods and Services Tax Act 1985 (NZ) |
| Supporting Legislation | Tax Administration Act 1994 (NZ); Taxation (Annual Rates for 2023-24, Multinational Tax, and Remedial Matters) Act 2024; Taxation (Annual Rates for 2025-26, Emergency Response, and Remedial Matters) Act 2026 (April 2026 GST amendments) |
| Tax Authority | Inland Revenue Department (IRD / Te Tari Taake) |
| Filing Portal | https://myir.ird.govt.nz (myIR) |
| Contributor | Open Accounting Skills Community |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: field assignment, zero-rating, input tax credits, derived calculations. Tier 2: change-of-use adjustments, apportionment elections, mixed-use assets. Tier 3: complex group registrations, financial services elections, non-standard arrangements. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and IRD number** [T1] -- IRD number format: XX-XXX-XXX or XXX-XXX-XXX
2. **GST registration status** [T1] -- Registered (compulsory or voluntary) or not registered
3. **GST registration number** [T1] -- same as IRD number for most entities
4. **Accounting basis** [T1] -- Invoice basis (accrual), Payments basis (cash), or Hybrid basis
5. **Filing frequency** [T1] -- Monthly, 2-monthly, or 6-monthly
6. **Taxable period end date** [T1] -- determines which period transactions fall into
7. **Business activity** [T2] -- impacts apportionment and deductibility (e.g., financial services, residential property)
8. **Does the business make exempt supplies?** [T2] -- If yes, apportionment required (change-of-use rules apply)
9. **Does the business make zero-rated supplies?** [T1] -- exports, land transactions, going concerns
10. **Ratio of taxable to total supplies** [T2] -- needed for change-of-use adjustment calculations

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status and period are confirmed.**

**Legislation:** Goods and Services Tax Act 1985, s.51 (registration requirements).

---

## Step 1: GST Rate Structure

### 1a. Standard Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 15% | Standard rate on all taxable supplies of goods and services in New Zealand | GST Act 1985, s.8(1) |
| 0% | Zero-rated supplies (exports, going concerns, certain land, listed financial services) | GST Act 1985, s.11, s.11A, s.11AB |
| Exempt | Financial services, residential rental, donated goods/services by nonprofits | GST Act 1985, s.14 |

**New Zealand has a single positive GST rate of 15%.** There are NO reduced rates (unlike the EU). Supplies are either taxable at 15%, zero-rated at 0%, or exempt.

**Legislation:** GST Act 1985, s.8 (imposition of GST).

### 1b. Zero-Rated Supplies (Complete List) [T1]

| Category | Description | Legislation |
|----------|-------------|-------------|
| Exports of goods | Goods entered for export under Customs and Excise Act 2018 | s.11(1)(a) |
| Services to non-residents | Services supplied to non-resident outside NZ (conditions apply) | s.11A(1)(k) |
| Going concerns | Supply of a going concern to a registered person | s.11(1)(mb) |
| Land (compulsory zero-rating) | Supply of land between registered persons where purchaser acquires for taxable activity | s.11(1)(mb) |
| International transport | Transport of passengers/goods to or from NZ | s.11A(1)(a)-(c) |
| Duty-free goods | Goods supplied at duty-free shops for export | s.11(1)(b) |
| Fine metals | Supply of fine metal (gold, silver, platinum of specified fineness) | s.11(1)(mb) |
| Financial services (election) | Registered person electing to zero-rate financial services to registered persons | s.11A(1)(q)-(r), s.20F |
| Telecommunications (roaming) | Roaming services for overseas mobile users | s.11A(1)(lb) |

### 1c. Exempt Supplies (Complete List) [T1]

| Category | Description | Legislation |
|----------|-------------|-------------|
| Financial services | Lending, exchange of currency, life insurance, equity securities | s.14(a), s.3 (definition) |
| Residential rental | Rental of a dwelling (residential accommodation) | s.14(c) |
| Donated goods/services | Supply of donated goods or services by a nonprofit body | s.14(ca) |
| Penalty/fine/interest | Certain penalties, fines, and default interest | s.14 |

**Key distinction:** Zero-rated supplies allow full input tax recovery. Exempt supplies do NOT allow input tax recovery on related inputs. This distinction is critical.

---

## Step 2: GST Return Form -- GST101A Field Mapping

### 2a. GST101A Return Fields (Complete) [T1]

**Legislation:** GST Act 1985, s.16 (returns); Tax Administration Act 1994, s.33 (return requirements).

| Field | Description | Classification |
|-------|-------------|----------------|
| **Box 5** | Total sales and income for the period (inclusive of GST) | output_total |
| **Box 6** | Zero-rated supplies (included in Box 5) | output_zero |
| **Box 7** | Total output tax (GST on sales): (Box 5 - Box 6) x 3/23 | output_tax |
| **Box 8** | Adjustments to output tax (increases) | output_adj_increase |
| **Box 9** | Total output tax after adjustments: Box 7 + Box 8 | output_tax_adjusted |
| **Box 10** | Total purchases and expenses (inclusive of GST) | input_total |
| **Box 11** | Total input tax (GST on purchases): Box 10 x 3/23 | input_tax |
| **Box 12** | Adjustments to input tax (increases/decreases) | input_adj |
| **Box 13** | Total input tax after adjustments: Box 11 + Box 12 | input_tax_adjusted |
| **Box 14** | If Box 9 > Box 13: GST to pay (Box 9 - Box 13) | tax_payable |
| **Box 15** | If Box 13 > Box 9: GST refund (Box 13 - Box 9) | tax_refund |

### 2b. GST Fraction [T1]

The GST fraction for calculating GST content of a GST-inclusive amount is:

```
GST fraction = 3/23 (which equals 15/115 = 0.13043478...)
```

**This fraction is used because NZ GST returns work on a GST-inclusive basis for Box 5 and Box 10.**

**Legislation:** GST Act 1985, s.2 (definition of "tax fraction").

### 2c. Derived Calculations [T1]

```
Box 7  = (Box 5 - Box 6) x 3/23
Box 9  = Box 7 + Box 8
Box 11 = Box 10 x 3/23
Box 13 = Box 11 + Box 12

IF Box 9 > Box 13 THEN
    Box 14 = Box 9 - Box 13   -- GST to pay
    Box 15 = 0
ELSE
    Box 14 = 0
    Box 15 = Box 13 - Box 9   -- GST refund
END
```

---

## Step 3: Transaction Classification Rules

### 3a. Determine Transaction Type [T1]

- Sale/income (output GST) or Purchase/expense (input GST)
- Salaries, wages, PAYE, ACC levies, dividends, bank interest received, loan repayments = OUT OF SCOPE (not on GST return)
- **Private/domestic expenditure** = no input tax claim regardless of GST content

**Legislation:** GST Act 1985, s.2 (definition of "taxable activity"), s.6 (meaning of taxable activity).

### 3b. Determine Supply Location [T1]

| Origin | Classification |
|--------|---------------|
| New Zealand domestic | Standard 15% or zero-rated or exempt |
| Imported goods | GST collected at border by Customs (or deferred payment) |
| Imported services | Reverse charge may apply (s.8(4B)) |
| Exports (goods) | Zero-rated under s.11 |
| Exports (services) | Zero-rated under s.11A if supplied to non-resident outside NZ |

### 3c. Sales Classification [T1]

| Type | Box 5 | Box 6 | Notes |
|------|-------|-------|-------|
| Standard taxable sale (15%) | Include GST-inclusive amount | -- | GST = amount x 3/23 |
| Zero-rated sale (export, land, going concern) | Include full amount | Include same amount | Net GST = 0 |
| Exempt sale (financial services, residential rent) | Do NOT include | -- | No GST, no input recovery on related costs |
| Out of scope (wages, dividends etc) | Do NOT include | -- | Not a supply |

### 3d. Purchases Classification [T1]

| Type | Box 10 | Notes |
|------|--------|-------|
| Standard purchase (15% GST charged) | Include GST-inclusive amount | Input tax = amount x 3/23 |
| Zero-rated purchase | Include full amount | Input tax = 0 (no GST content) |
| No GST charged (from unregistered supplier) | Do NOT include | No input tax claim |
| Exempt purchase | Do NOT include | No input tax claim |
| Private/domestic expense | Do NOT include | Blocked regardless |
| Secondhand goods (from unregistered person) | Include deemed value | Special input credit rules apply (s.3A, s.20(3)) |

---

## Step 4: Input Tax Credit Rules

### 4a. General Entitlement [T1]

A registered person may claim input tax credits for GST on goods and services acquired for the principal purpose of making taxable supplies.

**Legislation:** GST Act 1985, s.20(3) (input tax deduction).

**Requirements for claiming input tax:**
1. The person must be registered for GST
2. The goods/services must be acquired for making taxable supplies (including zero-rated)
3. A tax invoice must be held (except for secondhand goods, or supplies under $50)
4. The supply must have been made to the claimant

### 4b. Tax Invoice Requirements [T1]

| Threshold | Required Information | Legislation |
|-----------|---------------------|-------------|
| Supply < $50 | Supplier name, date, description, total including GST | s.24(6) |
| Supply $50 - $1,000 | Above + supplier IRD number + statement "includes GST" | s.24(3)-(4) |
| Supply > $1,000 | Above + recipient name/address + quantity + GST-exclusive amount + GST amount | s.24(3) |

### 4c. Secondhand Goods Input Credit [T1]

**This is a NZ-unique provision.** A registered person who acquires secondhand goods from an unregistered person can claim an input tax credit WITHOUT a tax invoice.

**Conditions:**
- Goods must be situated in NZ at time of supply
- Supplier is NOT a registered person (or not required to charge GST)
- Goods acquired for making taxable supplies
- Input credit = purchase price x 3/23 (i.e., deemed to include GST at 15%)
- Records must be kept: supplier name/address, date, description, price paid

**Legislation:** GST Act 1985, s.3A (definition of secondhand goods), s.20(3)(a)(ia).

**Cap:** Input credit limited to GST fraction of consideration actually paid.

### 4d. Blocked Input Tax Categories [T1]

New Zealand has fewer blocked categories than many jurisdictions:

| Category | Treatment | Legislation |
|----------|-----------|-------------|
| Private/domestic use | No claim -- not for taxable activity | s.20(3) general requirement |
| Entertainment (50% deductible) | Claim limited to 50% of GST content for entertainment expenditure | s.21I |
| Non-taxable activity expenses | No claim | s.20(3) |
| Exempt supply-related expenses | No claim (unless apportioned) | s.20(3), s.20C |
| Residential accommodation (employer-provided) | No claim | s.21H |
| Motor vehicles used privately | Apportionment required for private use component | s.20C-20G |

**Note:** Unlike Malta and many EU countries, NZ does NOT have a blanket block on motor vehicles. Business use of motor vehicles IS claimable; only the private use portion is denied.

---

## Step 5: Change-of-Use Adjustments (NZ Unique Approach)

### 5a. Overview [T2]

**New Zealand uses a change-of-use adjustment system, NOT an annual pro-rata method like the EU.** This is a fundamental difference.

Under the EU VAT system, input tax is apportioned annually based on the ratio of taxable to total supplies. Under the NZ system, input tax is claimed in full at acquisition (if principal purpose is taxable), and adjustments are made in later periods if actual use changes.

**Legislation:** GST Act 1985, s.20C (principal purpose test), s.20D (adjustments for going concerns), s.20E (wash-up adjustments on disposal), s.20F (financial services elections), s.20G (application).

### 5b. Principal Purpose Test at Acquisition [T1]

At the time of acquisition:
- If the **principal purpose** (>50%) is making taxable supplies: claim FULL input tax, then adjust later if use changes
- If the **principal purpose** is NOT making taxable supplies: claim NO input tax, then adjust later if use changes

**Legislation:** GST Act 1985, s.20(3C)-(3D).

### 5c. Adjustment Periods [T2]

Adjustments are required in subsequent adjustment periods if actual taxable use differs from the percentage previously used.

| Asset Value (GST-exclusive) | Number of Adjustment Periods | Period Length |
|-----------------------------|------|---------------|
| $0 - $5,000 | 0 | No adjustments required |
| $5,001 - $10,000 | 2 | Equal to taxable period |
| $10,001 - $500,000 | 5 | Equal to taxable period |
| Over $500,000 | 10 | Equal to taxable period |

**Legislation:** GST Act 1985, s.21G (number of adjustment periods).

### 5d. Adjustment Calculation [T2]

```
Adjustment = Full input tax x (Percentage actual taxable use - Percentage previously used)
```

If the actual taxable use percentage INCREASES from what was previously claimed, an additional input credit is available (positive adjustment in Box 12).

If the actual taxable use percentage DECREASES, output tax adjustment is required (adjustment in Box 8).

**Legislation:** GST Act 1985, s.21A-21H.

### 5e. Wash-Up on Disposal [T1]

When goods or services are disposed of, a final wash-up adjustment is required under s.21(1)-(5) to reconcile total input tax claimed over the life of the asset with the actual taxable use over that period.

**Legislation:** GST Act 1985, s.20E (disposal adjustment).

### 5f. Comparison with EU VAT Pro-Rata

| Feature | NZ GST | EU VAT |
|---------|--------|--------|
| Method | Change-of-use adjustments | Annual pro-rata (capital goods scheme for large items) |
| Initial claim | Full or nothing based on principal purpose | Pro-rata at acquisition |
| Subsequent adjustments | Per-period based on actual use change | Annual recalculation for capital goods (typically 5 or 10 years) |
| De minimis | No adjustment for assets under $5,000 | Varies by member state |
| Complexity | Simpler for single-use assets; complex for mixed-use | Consistent annual calculation |

---

## Step 6: Registration Rules

### 6a. Registration Thresholds [T1]

| Type | Threshold | Legislation |
|------|-----------|-------------|
| Compulsory registration | Taxable supplies exceed or expected to exceed NZD 60,000 in any 12-month period | s.51(1) |
| Voluntary registration | Below NZD 60,000 but carrying on a taxable activity | s.51(3) |
| Non-resident registration | NZD 60,000 threshold applies to non-resident suppliers of remote services and low-value imported goods | s.51(1)(b) |

### 6b. Marketplace Operators [T1]

Electronic marketplace operators are deemed to be the supplier for GST purposes for:
- Listed services (ride-sharing, short-stay accommodation, food/beverage delivery) -- since 1 April 2024
- Remote services supplied by non-resident operators to NZ consumers
- Low-value imported goods (goods valued at or below NZD 1,000) supplied by non-resident operators

**Legislation:** GST Act 1985, s.60C (marketplace rules), s.8(3)(abc).

### 6c. Non-Resident Suppliers [T1]

Since 1 October 2016, non-resident suppliers of remote services (digital services) to NZ consumers must register and charge GST if their supplies to NZ exceed NZD 60,000 in a 12-month period.

Since 1 December 2019, non-resident suppliers of low-value imported goods (NZD 1,000 or less) must also register and charge GST.

**Legislation:** GST Act 1985, s.8(3)(c), s.51(1)(b).

### 6d. April 2026 GST Amendments [T1]

The following changes took effect from 1 April 2026:

| Change | Detail | Impact |
|--------|--------|--------|
| Filing frequency correction | Businesses can correct GST filing frequency selections made in error within 35 days of registration | Registration admin |
| Secondhand goods input credits | Registered businesses may claim input credits for secondhand goods acquired before registration, provided those goods support taxable supplies | Expanded s.3A / s.20(3) entitlement |
| Record-keeping relaxation | Suppliers no longer required to collect personal details from unregistered buyers for supplies exceeding $1,000 | Reduced compliance burden; amends s.24 requirements |
| Joint venture flow-through | Unincorporated joint venture members may elect flow-through GST treatment; registration thresholds determined at joint venture level | New s.60 election |
| Non-taxable goods | Only integral or substantial improvement costs disqualify supplies from non-taxable treatment; minor improvements no longer prevent non-taxable status | Simplification |
| Inherited goods | Inherited goods entering New Zealand qualify for GST exemption at Customs | Customs concession |
| Supplier groups | Issuing members only responsible for taxable supply information for members covered by formal agreements (retroactive to 1 April 2023) | Group registration clarification |

**Legislation:** Taxation (Annual Rates for 2025-26, Emergency Response, and Remedial Matters) Act 2026.

---

## Step 7: Filing Frequency and Deadlines

### 7a. Filing Periods [T1]

| Frequency | Eligibility | Legislation |
|-----------|-------------|-------------|
| 2-monthly | Default / standard for most registered persons | s.15(2) |
| Monthly | Taxable supplies exceed NZD 24,000,000 p.a. (compulsory), or by election | s.15(1), s.15(3) |
| 6-monthly | Taxable supplies do not exceed NZD 500,000 p.a. AND not requesting refunds in most periods | s.15(4) |

### 7b. 2-Monthly Periods (Standard) [T1]

Standard 2-monthly periods end on the last day of:
- January, March, May, July, September, November (Category A)
- February, April, June, August, October, December (Category B)

The category depends on the person's balance date.

### 7c. Due Dates [T1]

| Filing Method | Due Date | Legislation |
|---------------|----------|-------------|
| Electronic filing (myIR) | 28th of the month following the end of the taxable period | s.16(4), Tax Administration Act s.36 |
| Paper filing | 28th of the month following the end of the taxable period | s.16(4) |

**Exception:** If the 28th falls on a weekend or public holiday, the due date is the next working day.

**Special:** For the period ending 31 March (or 30 November for 6-monthly filers with March balance date), the due date may be extended to 7 May for tax agents.

**Legislation:** Tax Administration Act 1994, s.36 (due dates for GST returns).

---

## Step 8: Penalties and Interest

### 8a. Late Filing Penalty [T1]

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Failure to file GST return on time | Initial penalty: $250 for the first month (or part month) late | Tax Administration Act 1994, s.139A |
| Continued failure | Additional $250 for each subsequent month (up to a maximum total of $250 per return for small taxpayers) | s.139A |

### 8b. Late Payment Penalty [T1]

| Period | Penalty Rate | Legislation |
|--------|-------------|-------------|
| Day after due date | 1% of unpaid tax | Tax Administration Act 1994, s.139B |
| 7th day after due date | Additional 4% of remaining unpaid tax | s.139B |
| No further incremental penalties | Use-of-money interest applies instead | s.139B |

### 8c. Use-of-Money Interest (UOMI) [T1]

| Type | Rate (from 16 January 2026) | Legislation |
|------|-------------------|-------------|
| Underpayment (taxpayer owes IRD) | 8.97% p.a. (changes periodically; was 10.91% before May 2025, then 9.89% from May 2025) | Tax Administration Act 1994, s.120D |
| Overpayment (IRD owes taxpayer) | 2.25% p.a. (changes periodically; was 2.31% before May 2025, then 3.27% from May 2025) | s.120D |

**Note:** UOMI rates are set by Order in Council and change with market interest rates. Always verify current rates on the IRD website.

### 8d. Shortfall Penalties [T2]

| Type | Penalty Rate | Legislation |
|------|-------------|-------------|
| Lack of reasonable care | 20% of tax shortfall | Tax Administration Act 1994, s.141A |
| Unacceptable tax position | 20% of tax shortfall | s.141B |
| Gross carelessness | 40% of tax shortfall | s.141C |
| Abusive tax position | 100% of tax shortfall | s.141D |
| Evasion | 150% of tax shortfall | s.141E |

---

## Step 9: Key Thresholds Lookup Table

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Compulsory GST registration | NZD 60,000 / 12 months | s.51(1) |
| Monthly filing (compulsory) | NZD 24,000,000 / 12 months | s.15(1) |
| 6-monthly filing eligibility | NZD 500,000 / 12 months max | s.15(4) |
| Tax invoice not required | Supply under NZD 50 | s.24(6) |
| Simplified tax invoice | Supply NZD 50 - NZD 1,000 | s.24(4) |
| Full tax invoice | Supply over NZD 1,000 | s.24(3) |
| Change-of-use: no adjustments | Asset under NZD 5,000 (GST-exclusive) | s.21G |
| Change-of-use: 2 adjustments | Asset NZD 5,001 - NZD 10,000 | s.21G |
| Change-of-use: 5 adjustments | Asset NZD 10,001 - NZD 500,000 | s.21G |
| Change-of-use: 10 adjustments | Asset over NZD 500,000 | s.21G |
| Low-value imported goods | NZD 1,000 or less (marketplace/non-resident rules) | s.12(1) |
| Small business cash accounting | Available to all registered persons on payments basis | s.19 |

---

## Step 10: Reverse Charge Mechanics

### 10a. When Reverse Charge Applies [T1]

In NZ, the reverse charge applies in limited circumstances:

1. **Imported services** -- where a registered person receives services from a non-resident and the services are NOT already subject to NZ GST, AND the recipient would not be entitled to a full input tax credit (i.e., they make exempt or mixed supplies)
2. **If the recipient would be entitled to a full input tax credit, reverse charge is NOT required** (as it would net to zero)

**Legislation:** GST Act 1985, s.8(4B) (reverse charge on imported services).

### 10b. Reverse Charge Treatment [T1]

When reverse charge applies:
- Include the value of imported services in Box 5 (output) AND add GST in Box 8 (adjustment to output tax)
- If partly for taxable supplies, claim a proportionate input tax credit in Box 12 (adjustment to input tax)

### 10c. Key Difference from EU [T1]

| Feature | NZ GST | EU VAT |
|---------|--------|--------|
| Reverse charge scope | Only on imported services where recipient cannot claim full input tax | All B2B cross-border services (broadly) |
| Self-supply | Reverse charge disappears if full input credit available | Both sides always shown |
| Filing | Adjustments in Box 8 and Box 12 | Separate acquisition/input boxes |

---

## Step 11: Specific Supply Rules

### 11a. Going Concern Zero-Rating [T1]

The supply of a taxable activity as a going concern is zero-rated if:
1. The supplier and recipient agree in writing that the supply is of a going concern
2. The supply is of a taxable activity (or part of a taxable activity) that is capable of being carried on as a going concern
3. The recipient is a registered person (or will be by settlement)

**Legislation:** GST Act 1985, s.11(1)(mb).

**Risk:** If conditions are not met, the supply is taxable at 15%. This can result in a significant unexpected GST liability. **Always confirm all conditions are met before zero-rating.**

### 11b. Compulsory Zero-Rating of Land [T1]

Since 1 April 2011, the supply of land between GST-registered persons is compulsorily zero-rated if:
1. The supply wholly or partly consists of land
2. The supplier and recipient are both registered persons
3. The recipient acquires the land for the principal purpose of making taxable supplies
4. The supply is not a supply of accommodation in a commercial dwelling

**Legislation:** GST Act 1985, s.11(1)(mb).

**The recipient must provide a written statement to the supplier confirming their registration and intended use.** If the statement is incorrect, the recipient (not the supplier) bears the GST liability.

### 11c. Financial Services Elections [T2]

A registered person making supplies of financial services can elect under s.20F to treat specified supplies as zero-rated (rather than exempt). This allows input tax recovery on related costs.

**Conditions for election:**
- Must be a registered person
- Must make taxable supplies (other than financial services) as well as exempt financial services
- The election applies to financial services supplied to other registered persons

**Legislation:** GST Act 1985, s.20F.

**Flag for reviewer: election must be confirmed and documented. Once made, the election affects all subsequent periods.**

### 11d. Short-Stay Accommodation [T1]

Short-stay accommodation (e.g., Airbnb, holiday rental) is a taxable supply at 15%.

**Marketplace operator rules (from 1 April 2024):** If listed on an electronic marketplace, the marketplace operator is deemed the supplier and must account for GST.

**Legislation:** GST Act 1985, s.60C.

**Distinction from residential rent:** Long-term residential rental (tenancy of 4 weeks or more as a principal place of residence) is EXEMPT. Short-stay / holiday accommodation is TAXABLE at 15%.

### 11e. GST on Imported Goods [T1]

| Value | Treatment | Legislation |
|-------|-----------|-------------|
| Over NZD 1,000 | GST collected by NZ Customs at border (or deferred payment scheme) | s.12(1) |
| NZD 1,000 or less (low-value goods) | GST collected by offshore supplier or marketplace operator | s.8(3)(ab) |

For goods over NZD 1,000, the importer claims input tax based on the Customs import entry document, not a tax invoice from the supplier.

**Legislation:** GST Act 1985, s.12 (imposition of GST on imports), s.20(3)(a)(iii) (input tax on imports).

---

## Step 12: PROHIBITIONS [T1]

- NEVER let AI guess GST classification -- it is deterministic from facts and legislation
- NEVER claim input tax for a person who is not GST-registered
- NEVER claim input tax on exempt supplies (financial services, residential rent) without checking for s.20F election
- NEVER zero-rate a land transaction without confirming BOTH parties are registered AND the recipient's written statement has been provided
- NEVER zero-rate a going concern without confirming ALL three conditions (written agreement, capable of being carried on, recipient registered)
- NEVER apply the secondhand goods credit when the supplier IS a registered person charging GST
- NEVER ignore the change-of-use adjustment thresholds -- assets under $5,000 do NOT require adjustments
- NEVER treat long-term residential rental as taxable -- it is EXEMPT
- NEVER treat short-stay accommodation as exempt -- it is TAXABLE at 15%
- NEVER confuse zero-rated (input tax claimable) with exempt (input tax NOT claimable)
- NEVER file a return using GST-exclusive figures -- Box 5 and Box 10 use GST-INCLUSIVE amounts
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER ignore marketplace operator rules for ride-sharing, accommodation, and food delivery platforms
- NEVER apply reverse charge when the recipient is entitled to a full input tax credit (it nets to zero, so the reverse charge mechanism is disapplied)

---

## Step 13: Edge Case Registry

### EC1 -- Going Concern: Conditions Not Met [T2]

**Situation:** Vendor sells a business to a buyer. Both are registered. Buyer signs a going concern statement. However, the business has ceased trading 6 months prior and has no employees, stock, or customers.
**Resolution:** The supply may NOT qualify as a going concern because the activity is not "capable of being carried on." Zero-rating is at risk. Flag for reviewer: assess whether the business as transferred is genuinely capable of operating as a going concern. If not, standard-rate at 15%.
**Legislation:** GST Act 1985, s.11(1)(mb); Case law: Belton v CIR (2014).

### EC2 -- Compulsory Zero-Rating of Land: Incorrect Statement [T1]

**Situation:** Registered vendor sells land to registered purchaser. Purchaser provides a written statement that they will use the land for taxable supplies. After settlement, purchaser converts to residential rental (exempt).
**Resolution:** The supply was correctly zero-rated at the time. The PURCHASER is liable for the GST as an adjustment under s.5(2). The vendor is protected provided they held a valid statement at the time of supply.
**Legislation:** GST Act 1985, s.5(2) (recipient's liability on incorrect statement).

### EC3 -- Change-of-Use Adjustment: Asset Increases in Taxable Use [T2]

**Situation:** Registered person acquires a building for $800,000 (GST-exclusive). Initially 60% taxable use, 40% exempt. Claims full input tax (principal purpose is taxable, >50%). In Year 2, taxable use increases to 80%.
**Resolution:** No adjustment needed in Year 2 because the actual taxable use (80%) is HIGHER than the 100% initially claimed. Adjustment only required if actual taxable use is LOWER than previously claimed percentage.
**Wait:** Actually under the NZ rules, the initial claim was 100% (full input tax). If actual use is only 80%, an OUTPUT adjustment of 20% x (full input tax / number of adjustment periods) is required. If use later increases to 90%, a partial INPUT adjustment reversal occurs.
**Legislation:** GST Act 1985, s.21A-21H.
**Flag for reviewer:** Change-of-use calculations for high-value mixed-use assets require careful tracking of percentage changes period by period. Confirm actual use percentages.

### EC4 -- Secondhand Goods: No Invoice Available [T1]

**Situation:** Registered dealer purchases a used car from a private individual for NZD 15,000. No tax invoice is available (private seller is not registered).
**Resolution:** Secondhand goods credit applies. Input tax = NZD 15,000 x 3/23 = NZD 1,956.52. Record must include: seller's name and address, date of purchase, description of goods, and consideration paid. Include in Box 10 (NZD 15,000) and claim input tax in Box 11.
**Legislation:** GST Act 1985, s.3A, s.20(3)(a)(ia), s.24(7).

### EC5 -- Non-Resident Digital Services [T1]

**Situation:** A NZ consumer subscribes to a streaming service from a US company. The US company is registered for NZ GST (exceeds NZD 60,000 threshold).
**Resolution:** The non-resident supplier charges and accounts for NZ GST at 15%. The consumer pays the GST-inclusive price. If a registered NZ business subscribes, it may claim an input tax credit if the service is for a taxable activity.
**Legislation:** GST Act 1985, s.8(3)(c), s.51(1)(b).

### EC6 -- Marketplace Operator Deemed Supplier [T1]

**Situation:** NZ resident lists their apartment on Airbnb for short-stay accommodation. Airbnb is an electronic marketplace operator.
**Resolution:** From 1 April 2024, Airbnb is the deemed supplier and must account for GST on the accommodation supply. The underlying supplier (host) does not charge GST on the Airbnb-facilitated supply. However, the host can still claim input tax on expenses related to providing the accommodation if they are registered.
**Legislation:** GST Act 1985, s.60C (marketplace operators for listed services).

### EC7 -- Financial Services: Mixed Supplier [T2]

**Situation:** A registered person provides both taxable consulting services and exempt financial services (e.g., loan brokering).
**Resolution:** Input tax on costs directly attributable to taxable supplies: fully claimable. Input tax on costs directly attributable to exempt supplies: not claimable. Input tax on overheads (shared costs): apportionment required using change-of-use rules (not the EU annual pro-rata). Consider s.20F election to zero-rate financial services to other registered persons.
**Legislation:** GST Act 1985, s.20C (apportionment), s.20F (election).
**Flag for reviewer:** Confirm whether s.20F election is appropriate and has been or should be made.

### EC8 -- Associated Persons: Market Value Rule [T2]

**Situation:** A company sells a vehicle to its shareholder (associated person) for NZD 5,000 when market value is NZD 20,000.
**Resolution:** Under s.10(3), where supply is between associated persons for less than market value AND the recipient cannot claim full input tax, the supply is deemed to be at open market value (NZD 20,000). Output GST applies on NZD 20,000.
**Legislation:** GST Act 1985, s.10(3) (associated persons), s.2A (definition of associated persons).
**Flag for reviewer:** Confirm association and whether recipient can claim full input tax.

### EC9 -- GST on Imported Services: Reverse Charge Not Required [T1]

**Situation:** Fully taxable registered person (100% taxable supplies) purchases marketing services from an Australian company. No NZ GST charged.
**Resolution:** Reverse charge is NOT required because the recipient would be entitled to claim a full input tax credit (net effect zero). Simply record the expense as a non-GST purchase. Do NOT include in GST return.
**Legislation:** GST Act 1985, s.8(4B)(b) -- reverse charge does not apply where input tax would be fully recoverable.

### EC10 -- Motor Vehicle: Mixed Business and Private Use [T2]

**Situation:** Registered person acquires a car for NZD 45,000 (GST-inclusive). 70% business use, 30% private use.
**Resolution:** Principal purpose is taxable (>50%), so claim FULL input tax at acquisition (NZD 45,000 x 3/23 = NZD 5,869.57). In subsequent adjustment periods, make change-of-use adjustments for the 30% private use component. Asset value exceeds NZD 10,000, so 5 adjustment periods apply.
**Legislation:** GST Act 1985, s.20(3C), s.21G.
**Flag for reviewer:** Confirm the business/private use split. Log-book or reasonable estimate required.

### EC11 -- Credit Notes and Debit Notes [T1]

**Situation:** Registered person issues a credit note to a customer for returned goods.
**Resolution:** Reduce Box 5 by the credit note amount (GST-inclusive). Output tax in Box 7 is automatically reduced by the GST fraction calculation. If a debit note is issued (price increase), increase Box 5 accordingly.
**Legislation:** GST Act 1985, s.25 (credit and debit notes).

### EC12 -- Payments Basis: Timing of Claim [T1]

**Situation:** Registered person on payments basis receives a purchase invoice in March but pays in May.
**Resolution:** On payments basis, the input tax is claimed in the period the payment is made (May period), NOT the period the invoice is received. Similarly, output tax is accounted for when payment is received from customers, not when invoiced.
**Legislation:** GST Act 1985, s.19 (accounting basis), s.20(4) (payments basis adjustments).

### EC13 -- Insurance Proceeds [T1]

**Situation:** Registered person receives an insurance payout for damaged business equipment.
**Resolution:** Insurance proceeds for a taxable supply are treated as consideration for a deemed supply. Include in Box 5 (GST-inclusive basis). GST content = amount x 3/23.
**Legislation:** GST Act 1985, s.5(13) (insurance).

---

## Step 14: Comparison with EU VAT

| Feature | NZ GST | EU VAT (Standard) |
|---------|--------|--------------------|
| Rate structure | Single rate: 15% | Multiple rates: standard (17-27%), reduced (5-18%), super-reduced, zero |
| Tax fraction | 3/23 | Varies (e.g., 1/6 for UK 20%) |
| Return basis | GST-inclusive amounts | GST/VAT-exclusive amounts (most member states) |
| Apportionment method | Change-of-use adjustments (NZ unique) | Annual pro-rata + capital goods scheme |
| Reverse charge | Only when recipient cannot claim full input credit | Mandatory for all B2B cross-border services |
| Secondhand goods | Input credit from unregistered supplier (no invoice needed) | Margin scheme (no input credit on purchase) |
| Registration threshold | NZD 60,000 (~EUR 33,000) | Varies by member state (EUR 0 to EUR 85,000) |
| Filing frequency | 2-monthly (standard) | Monthly or quarterly (varies) |
| E-invoicing | Not mandatory (myIR filing) | Mandatory in some member states (Italy, etc.) |
| Marketplace rules | Deemed supplier for listed services, remote services, low-value goods | Deemed supplier for certain B2C e-commerce |
| Place of supply (services) | Where services are performed or where recipient is | Complex rules based on service type (B2B: customer location) |
| Capital goods adjustment | Change-of-use periods based on asset value ($5k/$10k/$500k bands) | 5-year or 10-year (20-year for immovable property in some states) |
| Going concern relief | Zero-rated (conditions) | Outside scope of VAT / TOGC (conditions) |

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Qualified NZ accountant must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified NZ accountant. Document gap.
```

---

## Step 16: Test Suite

### Test 1 -- Standard Local Sale at 15% [T1]

**Input:** NZ registered person sells consulting services to NZ customer. Invoice: NZD 1,150 (GST-inclusive, being NZD 1,000 + NZD 150 GST). Payments basis, payment received in period.
**Expected output:** Box 5 = NZD 1,150. Box 7 = NZD 1,150 x 3/23 = NZD 150.00. No entry in Box 6.

### Test 2 -- Zero-Rated Export Sale [T1]

**Input:** NZ registered person exports goods to Australia. Invoice: NZD 5,000 (zero-rated). Goods entered for export with NZ Customs.
**Expected output:** Box 5 = NZD 5,000. Box 6 = NZD 5,000. Box 7 = (NZD 5,000 - NZD 5,000) x 3/23 = NZD 0.

### Test 3 -- Standard Purchase with Input Tax Claim [T1]

**Input:** NZ registered person purchases office supplies from NZ supplier. Invoice: NZD 230 (GST-inclusive, being NZD 200 + NZD 30 GST). Fully taxable business.
**Expected output:** Box 10 = NZD 230. Box 11 = NZD 230 x 3/23 = NZD 30.00.

### Test 4 -- Secondhand Goods Purchase from Private Seller [T1]

**Input:** NZ registered dealer purchases used furniture from a private individual for NZD 2,300. Seller is not registered. No tax invoice.
**Expected output:** Box 10 = NZD 2,300 (deemed GST-inclusive). Box 11 = NZD 2,300 x 3/23 = NZD 300.00. Secondhand goods credit applies.

### Test 5 -- Exempt Supply: Residential Rental Income [T1]

**Input:** NZ registered person (also has other taxable business) earns NZD 2,000 per month in long-term residential rental income.
**Expected output:** Do NOT include in Box 5. Exempt supply. No output GST. Input tax on expenses related to this rental: NOT claimable (apportionment required if mixed with taxable activity).

### Test 6 -- Imported Services: Reverse Charge Not Required [T1]

**Input:** Fully taxable NZ registered person (100% taxable) purchases digital marketing services from US company for NZD 500. No NZ GST charged.
**Expected output:** No GST return entry required. Reverse charge is disapplied because recipient would claim full input credit (net effect zero). Record as expense only.

### Test 7 -- Imported Services: Reverse Charge Required [T2]

**Input:** NZ registered person making 60% taxable and 40% exempt supplies purchases consulting from UK firm for NZD 10,000. No NZ GST charged.
**Expected output:** Reverse charge applies (recipient cannot claim full input credit). Box 5 += NZD 10,000. Box 8 = NZD 10,000 x 3/23 = NZD 1,304.35 (output tax adjustment). Box 12 = NZD 1,304.35 x 60% = NZD 782.61 (input tax adjustment for taxable portion). Net cost = NZD 521.74.

### Test 8 -- Going Concern Zero-Rating [T1]

**Input:** Registered vendor sells entire business to registered buyer for NZD 500,000. Written agreement in place. Business is fully operational with staff, stock, and customers.
**Expected output:** Box 5 = NZD 500,000. Box 6 = NZD 500,000. Box 7 = NZD 0. Zero-rated going concern. All three conditions met.

### Test 9 -- Land Transaction: Compulsory Zero-Rating [T1]

**Input:** Registered person sells commercial property to another registered person for NZD 1,200,000. Buyer provides written statement confirming registration and taxable use.
**Expected output:** Box 5 = NZD 1,200,000. Box 6 = NZD 1,200,000. Zero-rated under s.11(1)(mb). Box 7 = NZD 0.

### Test 10 -- Entertainment: 50% Limitation [T1]

**Input:** NZ registered person takes clients to dinner. Restaurant bill NZD 460 (GST-inclusive). Fully taxable business.
**Expected output:** Box 10 = NZD 460 (full amount). Box 11 = NZD 460 x 3/23 = NZD 60.00. BUT input tax claimable is limited to 50% = NZD 30.00. Adjustment of NZD -30.00 in Box 12 (or only claim NZD 30.00 net in Box 11/12).

### Test 11 -- Late Payment Penalty Calculation [T1]

**Input:** Registered person files GST return on time but pays NZD 10,000 GST liability 10 days late.
**Expected output:** Day 1 late: 1% penalty = NZD 100. Day 7: additional 4% penalty on remaining = 4% x NZD 10,100 = NZD 404. Total penalties = NZD 504. Plus UOMI from due date at applicable rate.

### Test 12 -- Marketplace Operator: Airbnb Short-Stay [T1]

**Input:** NZ resident lists apartment on Airbnb. Guest pays NZD 230 per night for 3 nights (NZD 690 total). Airbnb is registered marketplace operator.
**Expected output:** Airbnb accounts for GST as deemed supplier. The host does NOT charge GST on the Airbnb-facilitated booking. Host's GST return: no output entry for this supply. Airbnb's GST return: Box 5 includes the GST-inclusive accommodation amount.

---

## Step 17: Out of Scope -- Income Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified accountant.

- **Company tax rate:** 28% on taxable income
- **Individual tax rates:** Progressive bands 10.5% / 17.5% / 30% / 33% / 39%
- **Trustee tax rate:** 33% (unless beneficiary income)
- **ACC levies:** Separate obligation, not part of GST
- **PAYE:** Employer obligation, separate from GST
- **FBT (Fringe Benefit Tax):** Separate return and payment, not on GST return
- **Provisional tax:** Separate obligation for taxpayers with residual income tax over NZD 5,000

---

## Contribution Notes

If you are adapting this skill for another jurisdiction:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all field numbers with the equivalent fields on your jurisdiction's GST/VAT return form.
3. Replace GST rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace all NZD thresholds with your jurisdiction's equivalents in local currency.
5. Replace the change-of-use adjustment rules with your jurisdiction's apportionment method.
6. Replace blocked/limited categories with your jurisdiction's equivalent non-deductible categories.
7. Have a qualified accountant in your jurisdiction validate every T1 rule before publishing.
8. Add your own edge cases to the Edge Case Registry.
9. Run all test suite cases against your jurisdiction's rules.
10. Update the comparison table to reflect differences from your jurisdiction's perspective.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
