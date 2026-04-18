---
name: slovakia-vat-return
description: Use this skill whenever asked to prepare, review, or create a Slovak VAT return (DPH form / DPHv25) for any client. Trigger on phrases like "prepare VAT return", "do the DPH", "fill in DPH", "create the return", "Slovak VAT", or any request involving Slovakia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Slovak VAT classification rules, box mappings, deductibility rules, reverse charge treatment, import VAT reverse charge, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any VAT-related work for Slovakia.
---

# Slovakia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Slovakia |
| Jurisdiction Code | SK |
| Primary Legislation | Zakon c. 222/2004 Z.z. o dani z pridanej hodnoty (VAT Act No. 222/2004 Coll., as amended by Consolidation Act 2025) |
| Supporting Legislation | EU VAT Directive 2006/112/EC; Act No. 563/2009 Coll. (Tax Administration Act); Act No. 595/2003 Coll. (Income Tax Act) |
| Tax Authority | Financna sprava Slovenskej republiky (Financial Administration of the Slovak Republic) |
| Filing Portal | https://www.financnasprava.sk (eDane / eTax portal) |
| Contributor | Auto-generated draft -- requires validation |
| Validated By | Deep research verification, April 2026 |
| Validation Date | 2026-04-10 |
| Skill Version | 1.0 |
| Status | validated |
| Confidence Coverage | Tier 1: box assignment, reverse charge, deductibility blocks, derived calculations. Tier 2: partial exemption coefficient, vehicle use documentation, import VAT reverse charge. Tier 3: complex group structures, non-standard supplies, triangulation, SOPARFI-like structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified danovy poradca must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified adviser.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and IC DPH (VAT ID)** [T1] -- SK + 10 digits
2. **VAT registration type** [T1] -- Standard (Section 4), Voluntary (Section 4a), Group registration (Section 4b), Registered for EU purposes only (Section 7/7a), or non-registered
3. **Filing frequency** [T1] -- Monthly (default for turnover >= EUR 100,000) or quarterly (turnover < EUR 100,000, after first year of registration)
4. **Industry/sector** [T2] -- impacts deductibility and rate classification
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (koeficient); reviewer must confirm
6. **Does the business trade goods for resale?** [T1] -- impacts classification
7. **Excess credit brought forward** [T1] -- from prior period (nadmerny odpocet)
8. **Does the business use import VAT reverse charge?** [T2] -- new from July 2025 (DPHv25 form)
9. **Is the client subject to the vehicle restriction (from 2026)?** [T1] -- M1 vehicles, motorcycles

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output DPH / dan na vystupe) or Purchase (input DPH / dan na vstupe / odpocitanie dane)
- Salaries, social contributions (Socialna poistovna, zdravotne poistenie), tax payments, loan repayments, dividends, bank charges = OUT OF SCOPE
- **Legislation:** VAT Act Sec. 2-3 (scope of tax), Sec. 8-10 (supply of goods), Sec. 9 (supply of services)

### 1b. Determine Counterparty Location [T1]
- Slovakia (domestic): supplier/customer country is SK
- EU: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SI, ES, SE
- Non-EU: everything else
- **Note:** UK is Non-EU post-Brexit. Ukraine is Non-EU. Czech Republic is a separate EU member.

### 1c. Determine VAT Rate [T1]

**Rates from 1 January 2025 (Consolidation Act amendments):**

| Rate | Category | Legislation |
|------|----------|-------------|
| 23% | Standard rate -- most goods and services | VAT Act Sec. 27(1) |
| 19% | Reduced rate -- foodstuffs, non-alcoholic beverages, medicines, certain construction/renovation of residential housing, sporting events entrance, accommodation, newspapers | VAT Act Sec. 27(2), Annex 7 |
| 5% | Super-reduced rate -- basic foodstuffs (bread, butter, milk, meat, fish, fruit, vegetables, eggs), books and periodicals | VAT Act Sec. 27(3), Annex 7a |
| 0% | Zero-rated -- intra-EU supplies of goods (Sec. 43), exports (Sec. 47) | VAT Act Sec. 43-47 |
| Exempt with credit | International transport, supplies connected with international trade | VAT Act Sec. 47 |
| Exempt without credit | Financial services (Sec. 39), insurance (Sec. 37), healthcare (Sec. 29), education (Sec. 31), postal services (Sec. 28), residential rental (Sec. 38(3)), gambling, transfer of going concern | VAT Act Sec. 28-42 |

**Pre-2025 rates (for historical periods):** Standard 20%, Reduced 10%

### 1d. Determine Expense Category [T1]
- Capital goods: investment property and tangible assets used for business; adjustment applies on change of use
- Immovable property: 20-year adjustment period (VAT Act Sec. 54a)
- Movable capital goods: 5-year adjustment period (VAT Act Sec. 54)
- Resale: goods bought to resell
- Overhead/services: everything else
- **Legislation:** VAT Act Sec. 54-54a (adjustment of deduction for capital goods)

---

## Step 2: VAT Return Form Structure (DPHv25 -- from July 2025) [T1]

**Legislation:** VAT Act Sec. 78; form DPHv25 prescribed by Financial Administration.

### Output DPH Section

| Row | Description | Rate | Notes |
|-----|-------------|------|-------|
| 01 | Domestic supplies at 23% -- taxable base | 23% | Standard-rated sales |
| 01a | Output DPH at 23% | -- | Calculated |
| 02 | Domestic supplies at 19% -- taxable base | 19% | Food, accommodation, etc. |
| 02a | Output DPH at 19% | -- | Calculated |
| 03 | Domestic supplies at 5% -- taxable base | 5% | Basic food, books |
| 03a | Output DPH at 5% | -- | Calculated |
| 04 | Intra-Community supply of goods (exempt with credit) | 0% | Report on EC Sales List |
| 05 | Export of goods outside EU | 0% | Customs documentation |
| 06 | Exempt supplies without right of deduction | -- | Financial, insurance, healthcare |
| 07 | Intra-Community acquisition of goods -- taxable base | RC | Self-assessed |
| 07a | Self-assessed output DPH on IC acquisition | -- | At applicable SK rate |
| 08 | Services received from EU (reverse charge) -- taxable base | RC | B2B services from EU |
| 08a | Self-assessed output DPH on EU services | -- | At applicable SK rate |
| 09 | Services/goods received from non-EU (reverse charge) -- taxable base | RC | B2B from non-EU |
| 09a | Self-assessed output DPH on non-EU | -- | At applicable SK rate |
| 10 | Domestic reverse charge supplies received -- taxable base | RC | Construction, waste, etc. |
| 10a | Self-assessed output DPH on domestic RC | -- | At applicable rate |
| 11 | Import VAT -- output side (reverse charge, from July 2025) | RC | New DPHv25 feature |
| 11a | Self-assessed output DPH on imports | -- | At applicable rate |
| 12 | Self-supply / deemed supply | applicable | Private use, free gifts |

### Input DPH Section

| Row | Description | Notes |
|-----|-------------|-------|
| 20 | Input DPH on domestic purchases at 23% | Standard-rated input |
| 21 | Input DPH on domestic purchases at 19% | Reduced-rated input |
| 22 | Input DPH on domestic purchases at 5% | Super-reduced input |
| 23 | Input DPH on intra-Community acquisitions | Mirrors Row 07a |
| 23a | Input DPH on imports (reverse charge, from July 2025) | New DPHv25 feature |
| 24 | Input DPH on services from EU (reverse charge) | Mirrors Row 08a |
| 25 | Input DPH on services from non-EU (reverse charge) | Mirrors Row 09a |
| 26 | Input DPH on domestic reverse charge | Mirrors Row 10a |
| 27 | Adjustments to input DPH | Corrections, pro-rata, capital goods |
| 28 | Total input DPH deductible | Sum |

### Summary Section

| Row | Description | Notes |
|-----|-------------|-------|
| 30 | Total output DPH | Sum of all output rows |
| 31 | Total input DPH | Row 28 |
| 32 | DPH liability (Row 30 - Row 31) -- if positive | TO PAY |
| 33 | Excess DPH (Row 31 - Row 30) -- if positive | TO REFUND |
| 34 | Coefficient of proportional deduction (%) | For mixed businesses |

---

## Step 3: Transaction Classification Matrix [T1]

### Purchases -- Domestic (Slovak Supplier)

| VAT Rate | Category | Input Row | Notes |
|----------|----------|-----------|-------|
| 23% | Overhead/services | Row 20 | Standard domestic |
| 19% | Overhead/services | Row 21 | Food, accommodation |
| 5% | Overhead/services | Row 22 | Basic food, books |
| 0% | Any | -- | No DPH to claim |
| Any | Capital goods | Row 20/21/22 | Track for 5/20-year adjustment |
| Any | Entertainment (blocked) | -- | No deduction (Sec. 49(7)) |
| Any | Vehicle (50% from 2026) | Row 20 at 50% | M1, L1e, L3e restriction |

### Purchases -- EU Supplier (Reverse Charge)

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Physical goods | Row 07/07a | Row 23 | Intra-EU acquisition |
| Services (B2B) | Row 08/08a | Row 24 | EU service RC |
| Out-of-scope | -- | -- | NEVER reverse charge |
| Local consumption abroad | -- | -- | Foreign VAT at source |

### Purchases -- Non-EU Supplier

| Type | Output Row | Input Row | Notes |
|------|-----------|-----------|-------|
| Services (B2B) | Row 09/09a | Row 25 | Non-EU service import |
| Physical goods (customs, traditional) | -- | Row 20 | VAT paid at customs border |
| Physical goods (import RC from July 2025) | Row 11/11a | Row 23a | New self-assessment |
| Out-of-scope | -- | -- | NEVER reverse charge |

### Sales -- Domestic

| Rate | Row | Notes |
|------|-----|-------|
| 23% | Row 01/01a | Standard-rated |
| 19% | Row 02/02a | Food, accommodation, etc. |
| 5% | Row 03/03a | Basic food, books |
| Exempt with credit | Row 04/05 | IC supply, exports |
| Exempt without credit | Row 06 | Financial, insurance, healthcare |

### Sales -- EU / Non-EU

| Location | Type | Row | Notes |
|----------|------|-----|-------|
| EU B2B goods | Intra-EU supply | Row 04 | Zero-rated, EC Sales List |
| EU B2B services | Place of supply in customer MS | Reported separately | VIES |
| Non-EU | Export | Row 05 | Zero-rated, customs docs |

---

## Step 4: Reverse Charge Mechanics [T1]

**Legislation:** VAT Act Sec. 69 (reverse charge); Sec. 11 (intra-EU acquisition).

### Intra-EU Acquisitions of Goods (Sec. 11)
1. Report taxable base in Row 07 and self-assessed output DPH in Row 07a
2. Claim input DPH in Row 23
3. Net effect: zero for fully taxable businesses
4. Report on EC Sales List

### EU Services Received -- B2B (Sec. 15(1))
1. Report in Row 08 (base) / Row 08a (output DPH)
2. Claim in Row 24
3. Net effect: zero

### Non-EU Services Received (Sec. 69(2)-(3))
1. Report in Row 09 (base) / Row 09a (output DPH)
2. Claim in Row 25
3. Net effect: zero

### Import VAT Reverse Charge (from July 2025) [T2]
**Legislation:** VAT Act Sec. 69(6)-(8) (new); DPHv25 form.

| Feature | Detail |
|---------|--------|
| Eligibility | Registered businesses importing goods into Slovakia |
| How it works | Instead of paying import DPH at customs, self-assess on DPH return |
| Output side | Row 11 (base) / Row 11a (output DPH at applicable rate) |
| Input side | Row 23a (input DPH) |
| Net effect | Zero for fully taxable businesses |
| Documentation | Must have customs declaration and proper authorization |

**Flag for reviewer: confirm client is eligible for import reverse charge and has proper customs documentation.**

### Domestic Reverse Charge [T1]
**Legislation:** VAT Act Sec. 69(12).

| Supply Type | Legislation | Threshold |
|-------------|-------------|-----------|
| Construction services | Sec. 69(12)(a) | No threshold |
| Supply of waste and scrap metals | Sec. 69(12)(b) | No threshold |
| Supply of certain agricultural products | Sec. 69(12)(c) | As specified |
| Supply of mobile phones and integrated circuits | Sec. 69(12)(d) | > EUR 5,000 per transaction |
| CO2 emission allowances | Sec. 69(12)(e) | No threshold |
| Supply of immovable property (when seller opts to tax) | Sec. 69(12)(f) | No threshold |

Domestic reverse charge procedure:
1. Report in Row 10 (base) / Row 10a (output DPH)
2. Claim in Row 26
3. Net effect: zero

### Exceptions to Reverse Charge [T1]
- Out-of-scope categories: NEVER reverse charge
- Local consumption abroad: NOT reverse charge
- EU supplier charged local VAT > 0%: NOT reverse charge
- Mobile phones/circuits below EUR 5,000: normal DPH applies

---

## Step 5: Deductibility Check

### Blocked / Restricted Categories [T1]
**Legislation:** VAT Act Sec. 49(7).

| Category | DPH Recovery | Legislation | Notes |
|----------|-------------|-------------|-------|
| Hospitality and entertainment (pohostenie a zabava) | 0% | Sec. 49(7)(a) | Always blocked, no exceptions |
| Business gifts | 0% | Sec. 49(7)(a) | Part of entertainment |
| Passenger vehicles M1 (from 2026) | 50% | Sec. 49(7)(b) (new) | Unless proven 100% business |
| Motorcycles L1e/L3e (from 2026) | 50% | Sec. 49(7)(b) (new) | Unless proven 100% business |
| Fuel for 50%-restricted vehicles | 50% | Sec. 49(7)(b) | Follows vehicle rule |
| Maintenance/repairs for restricted vehicles | 50% | Sec. 49(7)(b) | Follows vehicle rule |
| Personal use items | 0% | Sec. 49(2) | No deduction |
| Supplies for exempt-without-credit activities | 0% | Sec. 49(2) | Financial, insurance inputs |

### Vehicle Restriction Rules (from 1 January 2026) [T1]
**Legislation:** VAT Act Sec. 49(7)(b) (Consolidation Act 2025 amendment).

| Scenario | DPH Deduction | Evidence Required |
|----------|--------------|-------------------|
| M1 passenger car, mixed use | 50% | Default assumption |
| M1 passenger car, exclusively business | 100% | Electronic records + notification to tax authority [T2] |
| L1e/L3e motorcycle, mixed use | 50% | Default assumption |
| L1e/L3e motorcycle, exclusively business | 100% | Electronic records + notification to tax authority [T2] |
| N1 van / N2+ truck | 100% | No restriction (commercial vehicles) |
| Taxi / car rental vehicle | 100% | Qualifying business activity |
| Fuel for 50% vehicle | 50% | Follows vehicle classification |
| Fuel for 100% vehicle | 100% | Follows vehicle classification |

**To claim 100% deduction:** Taxpayer must (1) maintain electronic records of vehicle usage, (2) notify the tax authority in advance, and (3) demonstrate exclusive business use. Flag for reviewer.

### Registration-Based Recovery [T1]

| Registration Type | Input VAT Recovery | Legislation |
|-------------------|-------------------|-------------|
| Section 4 registered (standard) | Full recovery (subject to blocks) | Sec. 49 |
| Section 4a (voluntary) | Full recovery once registered | Sec. 49 |
| Section 7/7a (EU purposes only) | NO input VAT recovery | Sec. 7 |
| Non-registered | NO recovery | -- |

### Partial Exemption -- Coefficient [T2]
**Legislation:** VAT Act Sec. 50.

If business makes both taxable and exempt supplies:

`Coefficient = Taxable Supplies / (Taxable Supplies + Exempt Supplies)`

| Rule | Detail | Legislation |
|------|--------|-------------|
| Rounding | Round UP to nearest whole percent | Sec. 50(4) |
| De minimis | If >= 95%, treated as 100% | Sec. 50(4) |
| Provisional | Use prior year coefficient during year | Sec. 50(5) |
| Annual adjustment | True-up at year-end | Sec. 50(6) |
| Excluded | Incidental financial/property transactions, sale of capital goods | Sec. 50(3) |

**Flag for reviewer: coefficient must be confirmed by qualified accountant. Annual adjustment applies.**

---

## Step 6: Control Statement (Kontrolny vykaz) [T1]

**Legislation:** VAT Act Sec. 78a.

| Feature | Detail |
|---------|--------|
| Filing obligation | Mandatory for all VAT payers alongside DPH return |
| Filing deadline | Same as VAT return (25th of following month/quarter) |
| Content | Transaction-level detail for cross-checking with trading partners |
| Structure | Sections A (supplies made) and B (supplies received) |
| Threshold for detail | Invoices > EUR 5,000 require individual reporting |
| Aggregation | Invoices <= EUR 5,000 may be aggregated |
| Penalty for non-filing | Up to EUR 10,000 |

---

## Step 7: Key Thresholds

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | EUR 50,000 prior year turnover OR EUR 62,500 current year turnover (from 2025); proposed increase to EUR 85,000 from July 2026 | Sec. 4(1) |
| Quarterly filing eligibility | Annual turnover < EUR 100,000 (after first year) | Sec. 78(2) |
| EU distance selling threshold | EUR 10,000/calendar year | EU Directive 2017/2455 |
| EU SME scheme (from 2025) | EUR 85,000 domestic + EUR 100,000 EU-wide | EU Directive 2020/285 |
| Domestic RC (electronics) | > EUR 5,000 per transaction | Sec. 69(12)(d) |
| Vehicle 50% restriction (from 2026) | All M1, L1e, L3e unless proven 100% business | Sec. 49(7)(b) |
| Control Statement detail | > EUR 5,000 per invoice | Sec. 78a |
| Capital goods -- movable | 5-year adjustment | Sec. 54 |
| Capital goods -- immovable | 20-year adjustment | Sec. 54a |
| Refund minimum | EUR 10 | Sec. 79(2) |

---

## Step 8: VAT Registration [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| VAT number format | SK + 10 digits | Sec. 4 |
| Mandatory registration | Turnover > EUR 50,000 prior calendar year OR > EUR 62,500 in current calendar year (from 2025); proposed increase to EUR 85,000 from July 2026 | Sec. 4(1) |
| Registration deadline | Immediate if EUR 62,500 exceeded in current year; by 20th of month following calendar year if EUR 50,000 prior-year threshold exceeded | Sec. 4(2) |
| Voluntary registration | May register below threshold | Sec. 4a |
| Group registration | Available for related entities | Sec. 4b |
| Section 7/7a registration | For EU acquisition/service purposes only, no input recovery | Sec. 7 |
| Deregistration | After 1 year, if no longer obligated | Sec. 81 |
| Fiscal representative | Required for non-EU businesses | Sec. 69a |

---

## Step 9: Filing Deadlines and Penalties

### Filing Deadlines [T1]

| Filing | Period | Deadline | Legislation |
|--------|--------|----------|-------------|
| DPH return (monthly) | Monthly | 25th of following month | Sec. 78(1) |
| DPH return (quarterly) | Quarterly | 25th of month following quarter end | Sec. 78(2) |
| Control Statement (Kontrolny vykaz) | Same as VAT return | 25th of following month/quarter | Sec. 78a |
| EC Sales List (Suhrny vykaz) | Monthly | 25th of following month | Sec. 80 |
| DPH payment | Same as return | 25th of following month/quarter | Sec. 78 |
| Intrastat | Monthly | 15th of following month | Statistical Office regulation |

### Penalties [T1]

| Violation | Penalty | Legislation |
|-----------|---------|-------------|
| Late filing of DPH return | EUR 30 - EUR 16,000 | Tax Administration Act Sec. 155 |
| Late payment of DPH | Interest at ECB rate + 10% p.a., from day after due date | Tax Administration Act Sec. 156 |
| Tax shortfall (additional assessment) | 10% of additional tax (if voluntary disclosure) / 20% (if audit) | Tax Administration Act Sec. 154 |
| Control Statement non-filing | Up to EUR 10,000 | Sec. 78a |
| EC Sales List non-filing | Up to EUR 10,000 | Sec. 80 |
| Failure to register | Back-assessment + penalty | Sec. 4 |
| Repeated non-compliance | Double penalties | Tax Administration Act Sec. 155(3) |

---

## Step 10: Derived Box Calculations [T1]

```
Row 30 = Sum of all output DPH rows (01a + 02a + 03a + 07a + 08a + 09a + 10a + 11a + ...)
Row 31 = Row 28 = Sum of all input DPH rows (20 + 21 + 22 + 23 + 23a + 24 + 25 + 26 + 27)

IF Row 30 > Row 31 THEN
  Row 32 = Row 30 - Row 31  -- Tax Payable
  Row 33 = 0
ELSE
  Row 32 = 0
  Row 33 = Row 31 - Row 30  -- Excess Credit (Refund)
END
```

---

## Step 11: Edge Case Registry

### EC1 -- EU hotel / restaurant / taxi booked abroad [T1]
**Situation:** Slovak DPH-registered client pays for hotel in Austria. Invoice shows Austrian 13% VAT.
**Resolution:** NOT reverse charge. Foreign VAT was charged at source. No DPH boxes. Austrian VAT is irrecoverable.
**Legislation:** VAT Act Sec. 16 -- place of supply for accommodation is where property is located.

### EC2 -- SaaS subscription from non-EU provider (AWS, Notion) [T1]
**Situation:** Monthly charge from US company, no VAT on invoice.
**Resolution:** Reverse charge. Row 09 (base) / Row 09a (output DPH at 23%). Row 25 (input DPH at 23%). Net effect zero.
**Legislation:** VAT Act Sec. 15(1) -- place of supply for B2B services is customer's establishment.

### EC3 -- Construction services (domestic reverse charge) [T1]
**Situation:** Slovak construction company provides services to another Slovak VAT-registered business. EUR 30,000.
**Resolution:** Domestic reverse charge. Supplier invoices without DPH. Recipient: Row 10 = EUR 30,000, Row 10a = EUR 6,900 (23%). Row 26 = EUR 6,900. Net zero.
**Legislation:** VAT Act Sec. 69(12)(a).

### EC4 -- Passenger vehicle purchase (from 2026, 50% restriction) [T2]
**Situation:** Client purchases M1 car EUR 25,000 + DPH EUR 5,750 (23%). Mixed business/private.
**Resolution:** From 1 January 2026, input DPH limited to 50% = EUR 2,875. Unless taxpayer proves 100% business use with electronic records and tax authority notification. Flag for reviewer.
**Legislation:** VAT Act Sec. 49(7)(b).

### EC5 -- Business dinner / entertainment (blocked) [T1]
**Situation:** Client hosts business dinner at restaurant. EUR 300 + DPH EUR 69 (23%).
**Resolution:** Input DPH is NOT deductible. 0% recovery on entertainment/hospitality under Sec. 49(7)(a). Full EUR 369 is cost.
**Legislation:** VAT Act Sec. 49(7)(a).

### EC6 -- Import VAT reverse charge (from July 2025) [T2]
**Situation:** Client imports goods from China and opts for import VAT reverse charge on DPHv25 form.
**Resolution:** Output side in Row 11/11a, input side in Row 23a. Net effect zero. Flag for reviewer: confirm eligibility and customs documentation.
**Legislation:** VAT Act Sec. 69(6)-(8).

### EC7 -- Credit notes [T1]
**Situation:** Client receives a credit note from supplier.
**Resolution:** Reverse the original entry. Reduce applicable input DPH row by credit note amount.
**Legislation:** VAT Act Sec. 25 (correction of tax base).

### EC8 -- EU B2B sale (intra-EU supply) [T1]
**Situation:** Registered client sells goods to Czech company at 0% DPH.
**Resolution:** Row 04 (intra-Community supply). No output DPH. Report on EC Sales List (Suhrny vykaz).
**Legislation:** VAT Act Sec. 43.

### EC9 -- Mobile phones above EUR 5,000 (domestic RC) [T1]
**Situation:** Slovak company buys mobile phones worth EUR 8,000 from another Slovak company.
**Resolution:** Domestic reverse charge applies (above EUR 5,000). Buyer: Row 10/10a (output), Row 26 (input). Net zero.
**Legislation:** VAT Act Sec. 69(12)(d).

### EC10 -- Mobile phones below EUR 5,000 (normal DPH) [T1]
**Situation:** Slovak company buys phones worth EUR 3,000 from another Slovak company.
**Resolution:** Normal DPH applies. Domestic RC threshold not met. Seller charges DPH at 23%.
**Legislation:** VAT Act Sec. 69(12)(d) -- threshold not met.

### EC11 -- Section 7/7a registered entity receives EU services [T1]
**Situation:** Entity registered under Section 7 (EU purposes only) receives consulting from German supplier.
**Resolution:** Must self-assess output DPH (Row 08/08a). But CANNOT claim input DPH (no deduction rights). Must pay the DPH.
**Legislation:** VAT Act Sec. 7, Sec. 49(1).

### EC12 -- Intra-EU goods acquisition [T1]
**Situation:** Slovak company buys goods from Polish supplier at 0% with PL VAT number.
**Resolution:** Row 07 = EUR value, Row 07a = DPH at 23%, Row 23 = same. Net zero. EC Sales List.
**Legislation:** VAT Act Sec. 11.

### EC13 -- Export of goods [T1]
**Situation:** Slovak company exports goods to US customer. EUR 10,000.
**Resolution:** Row 05 = EUR 10,000. No output DPH. Zero-rated. Customs documentation required.
**Legislation:** VAT Act Sec. 47.

### EC14 -- Immovable property sale (option to tax) [T2]
**Situation:** Company sells an office building 6 years after first occupation (default exempt).
**Resolution:** Seller may opt to tax under Sec. 38(8), in which case domestic reverse charge applies (Sec. 69(12)(f)). Buyer self-assesses. Flag for reviewer: confirm option-to-tax election and buyer's agreement.
**Legislation:** VAT Act Sec. 38(8) and Sec. 69(12)(f).

### EC15 -- Fuel for unrestricted vehicle (100%) [T1]
**Situation:** Client buys diesel for N1 delivery van. EUR 200 + DPH EUR 46 (23%).
**Resolution:** Row 20 += EUR 46. Fully deductible (N1 category, no restriction).
**Legislation:** VAT Act Sec. 49 -- no restriction on commercial vehicles.

### EC16 -- Passenger vehicle before 2026 (full deduction) [T1]
**Situation:** M1 car purchased in December 2025, EUR 15,000 + DPH EUR 3,450.
**Resolution:** Full deduction: Row 20 += EUR 3,450. The 50% restriction only applies from 1 January 2026. Pre-2026 purchases have full deduction rights.
**Legislation:** VAT Act Sec. 49(7)(b) -- effective date 1 January 2026.

---

## Step 12: VAT Rates -- Detailed Supply Classification [T1]

### 23% Standard Rate (Sec. 27(1))

| Supply Category | Examples |
|----------------|----------|
| General goods | Electronics, furniture, clothing, motor vehicles, household items |
| Professional services | Legal, accounting, consulting, IT, advertising |
| Telecommunications | Mobile, fixed-line, internet |
| Alcohol | Beer, wine, spirits |
| Tobacco | Cigarettes, cigars |
| Construction materials | Cement, steel, timber |
| Energy | Electricity, gas (non-residential) |

### 19% Reduced Rate (Sec. 27(2), Annex 7)

| Supply Category | Examples |
|----------------|----------|
| Foodstuffs (general) | Processed foods, confectionery, non-basic items |
| Non-alcoholic beverages | Soft drinks, juice, coffee, tea |
| Medicines | Prescription and OTC pharmaceuticals |
| Accommodation | Hotels, guesthouses, camping |
| Construction/renovation of residential housing | Certain qualifying residential works |
| Sporting events | Admission to sports matches, gyms |
| Newspapers | Daily and weekly newspapers, periodicals |

### 5% Super-Reduced Rate (Sec. 27(3), Annex 7a)

| Supply Category | Examples |
|----------------|----------|
| Basic foodstuffs | Bread, butter, milk, meat, fish, fruit, vegetables, eggs |
| Books | Printed and electronic books |
| Periodicals | Magazines, journals |

---

## Step 13: Comparison with Malta

| Feature | Slovakia (SK) | Malta (MT) |
|---------|--------------|------------|
| Standard rate | 23% (from 2025; previously 20%) | 18% |
| Reduced rates | 19%, 5% (from 2025; previously 10%) | 12%, 7%, 5% |
| Return form | DPHv25 (~34 rows from July 2025) | Malta periodic VAT return (~45 boxes) |
| Control Statement | Kontrolny vykaz (mandatory) | No equivalent |
| Filing frequency | Monthly / Quarterly | Quarterly (Art. 10), Annual (Art. 11) |
| Filing deadline | 25th of following month | 21st of month after quarter |
| Payment deadline | 25th | Same as filing |
| Small enterprise threshold | EUR 49,790 | EUR 35,000 |
| Capital goods movable | 5-year adjustment | > EUR 1,160 gross |
| Capital goods immovable | 20-year adjustment | No specific adjustment period |
| Blocked: entertainment | Yes (fully blocked, Sec. 49(7)(a)) | Yes (10th Schedule) |
| Blocked: passenger cars | 50% from 2026 (M1/L1e/L3e) | Fully blocked (10th Schedule) |
| Import VAT reverse charge | Available from July 2025 | Not available |
| Domestic reverse charge | Construction, waste, electronics > EUR 5K, emissions | No domestic reverse charge |
| Currency | EUR | EUR |
| Tax authority | Financna sprava | CFR |

---

## Step 14: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Danovy poradca must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to danovy poradca. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard domestic purchase, 23% DPH [T1]
**Input:** Slovak supplier, office supplies, gross EUR 246, DPH EUR 46, net EUR 200. Registered taxpayer.
**Expected output:** Row 20 += EUR 46. Fully recoverable.

### Test 2 -- EU service, reverse charge [T1]
**Input:** German supplier, consulting EUR 1,000, no VAT. Registered taxpayer.
**Expected output:** Row 08 = EUR 1,000. Row 08a = EUR 230 (23%). Row 24 = EUR 230. Net = zero.

### Test 3 -- Entertainment expense (blocked) [T1]
**Input:** Slovak restaurant, business dinner EUR 500 gross, DPH EUR 94 (23%), net EUR 406.
**Expected output:** Input DPH = EUR 0. Entertainment fully blocked (Sec. 49(7)(a)). No recovery.

### Test 4 -- EU B2B sale [T1]
**Input:** Registered client sells goods to Polish company EUR 5,000, 0% DPH.
**Expected output:** Row 04 = EUR 5,000. No output DPH. EC Sales List.

### Test 5 -- Non-EU software subscription [T1]
**Input:** US supplier (Notion), EUR 20/month, no VAT. Registered taxpayer.
**Expected output:** Row 09 = EUR 20. Row 09a = EUR 4.60 (23%). Row 25 = EUR 4.60. Net = zero.

### Test 6 -- Reduced rate domestic purchase (5%) [T1]
**Input:** Slovak supplier, bread and milk at 5%, gross EUR 105, DPH EUR 5, net EUR 100.
**Expected output:** Row 22 += EUR 5. Fully recoverable.

### Test 7 -- Import VAT reverse charge (from July 2025) [T2]
**Input:** Client imports machinery from US, customs value EUR 50,000. Opts for import RC.
**Expected output:** Row 11 = EUR 50,000. Row 11a = EUR 11,500 (23%). Row 23a = EUR 11,500. Net = zero. Flag for reviewer: confirm eligibility.

### Test 8 -- Passenger vehicle (from 2026, 50%) [T2]
**Input:** M1 car EUR 20,000 + DPH EUR 4,600 (23%). Mixed business/private use. No electronic records.
**Expected output:** Row 20 += EUR 2,300 (50%). Remaining EUR 2,300 is cost. Flag for reviewer.

### Test 9 -- Construction services (domestic RC) [T1]
**Input:** Slovak subcontractor, construction EUR 15,000. Both parties registered.
**Expected output:** Buyer: Row 10 = EUR 15,000, Row 10a = EUR 3,450 (23%). Row 26 = EUR 3,450. Net = zero.

### Test 10 -- Export of goods [T1]
**Input:** Slovak company exports to US client, EUR 8,000.
**Expected output:** Row 05 = EUR 8,000. No output DPH. Zero-rated.

### Test 11 -- Intra-EU goods acquisition [T1]
**Input:** Austrian supplier, goods EUR 3,000, 0% with AT VAT number.
**Expected output:** Row 07 = EUR 3,000. Row 07a = EUR 690 (23%). Row 23 = EUR 690. Net = zero.

### Test 12 -- Section 7 entity receives EU services (no deduction) [T1]
**Input:** Section 7 registered entity receives German consulting EUR 500.
**Expected output:** Row 08 = EUR 500. Row 08a = EUR 115 (23%). NO input deduction. Must pay EUR 115.

---

## Step 16: Refund Process [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Automatic refund | If excess DPH (Row 33 > 0) and no outstanding tax liabilities | Sec. 79 |
| Refund threshold | Minimum EUR 10 | Sec. 79(2) |
| Refund timeline | Within 30 days of filing deadline (standard) | Sec. 79(1) |
| Extended timeline | If tax authority initiates verification, up to 60 days | Sec. 79(3) |
| Carry forward | Credit can be carried forward to next period | Sec. 79 |
| Offset | Tax authority may offset against other tax liabilities | Tax Administration Act |
| New registrations | First 12 months: refund within 60 days (extended verification possible) | Sec. 79(4) |

---

## Step 17: Penalty-Free Voluntary Disclosure [T1]

| Feature | Detail | Legislation |
|---------|--------|-------------|
| Additional return | Can file amended return within 4 years | Tax Administration Act Sec. 16 |
| Reduced penalty | 10% of additional tax (vs 20% if found by audit) | Tax Administration Act Sec. 154(1) |
| Late payment interest | Still applies on any additional amount due | Tax Administration Act Sec. 156 |
| Deadline | Before tax authority starts audit proceedings | Tax Administration Act Sec. 16(2) |

---

## Step 18: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Escalate to qualified adviser.

- **Corporate income tax (dan z prijmov pravnickych osob):** 21% (from 2025) on adjusted profit
- **Small business CIT:** 10% for companies with revenue up to EUR 60,000 (from 2025)
- **Personal income tax:** 19% (up to EUR 47,537.98) / 25% above
- **Dividend tax:** 7% withholding (from 2025)
- **Social contributions:** employer ~35.2%, employee ~13.4%
- **Health insurance:** employer 10%, employee 4%
- **Motor vehicle tax (dan z motorovych vozidiel):** Based on engine power, for business vehicles
- **Local taxes:** Property tax (administered by municipalities)
- **Minimum tax (from 2025):** EUR 340 - EUR 3,840 depending on revenue tier
- **Special industry levies:** Banking levy, insurance levy, regulated industry contributions
- **Withholding tax:** 19% on royalties, interest, and management fees paid to non-residents (reduced by DTTs)
- **MOSS/OSS:** One-stop shop for B2C digital services and distance sales to EU consumers

---

## PROHIBITIONS [T1]

- NEVER let AI guess VAT box -- it is 100% deterministic from facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, bank charges)
- NEVER apply reverse charge to local consumption services abroad (hotel, restaurant, taxi)
- NEVER allow non-registered or Section 7/7a entities to claim input DPH
- NEVER confuse zero-rated (exports/intra-EU) with exempt without credit (financial, insurance)
- NEVER apply reverse charge when EU supplier charged local VAT > 0%
- NEVER apply 100% input deduction on entertainment/hospitality expenses (Sec. 49(7)(a))
- NEVER apply 100% vehicle deduction without confirmed exclusive business use documentation (from 2026, Sec. 49(7)(b))
- NEVER apply domestic RC to mobile phones/circuits below EUR 5,000 (Sec. 69(12)(d))
- NEVER apply old rates (20%/10%) to transactions from 2025 onward without checking transitional rules
- NEVER omit Control Statement -- it is mandatory alongside the DPH return
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill covers Slovakia's VAT system based on Act No. 222/2004 Coll. as amended by the Consolidation Act 2025. Key distinctive features include: the 2025 rate restructuring (20% to 23%, new 19%/5% tiers), the import VAT reverse charge from July 2025 (DPHv25 form), the vehicle 50% restriction from 2026, the mandatory Control Statement, entertainment fully blocked, and domestic reverse charge for construction/waste/electronics. Validation by a qualified Slovak danovy poradca is required before production use.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
