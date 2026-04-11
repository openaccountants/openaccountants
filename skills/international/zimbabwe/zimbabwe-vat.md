---
name: zimbabwe-vat
description: Use this skill whenever asked to prepare, review, or create a Zimbabwe VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Zimbabwe VAT", "ZIMRA return", "fill in VAT return", or any request involving Zimbabwe VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Zimbabwe VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, fiscalised device requirements, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Zimbabwe VAT-related work.
---

# Zimbabwe VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Zimbabwe (Republic of Zimbabwe) |
| Jurisdiction Code | ZW |
| Primary Legislation | Value Added Tax Act [Chapter 23:12] (as amended) |
| Supporting Legislation | VAT Regulations S.I. 273 of 2003; Revenue Authority Act [Chapter 23:11]; Customs and Excise Act [Chapter 23:02] |
| Tax Authority | Zimbabwe Revenue Authority (ZIMRA) |
| Filing Portal | https://efiling.zimra.co.zw (e-Services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed public accountant (ICAZ/PAAB member) in Zimbabwe |
| Validation Date | Pending |
| Last Verified | 2026-04-10 (web-verified against ZIMRA, PWC, Quaderno, M&J Consultants) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories, fiscalised devices. Tier 2: partial exemption, mixed supplies, foreign currency transactions, deemed supplies. Tier 3: mining sector, special economic zones, government procurement. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for licensed accountant.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and BP Number (Business Partner Number)** [T1]
2. **VAT registration number** [T1] -- issued by ZIMRA upon registration
3. **VAT period** [T1] -- bi-monthly (every 2 months) or monthly (large taxpayers)
4. **Industry/sector** [T2] -- impacts classification (mining, agriculture, tourism)
5. **Does the business make exempt supplies?** [T2] -- if yes, apportionment required
6. **Does the business import goods?** [T1] -- customs VAT at border
7. **Excess credit brought forward** [T1]
8. **Is the business using a ZIMRA-approved fiscalised electronic device?** [T1] -- mandatory
9. **Functional currency** [T2] -- ZiG (Zimbabwe Gold) or USD (multi-currency regime)

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 15% | Standard rate | VAT Act [23:12], s.6(1) |
| 0% | Zero rate (exports, specified supplies) | VAT Act [23:12], First Schedule |
| Exempt | No VAT, no input recovery | VAT Act [23:12], Second Schedule |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Act [23:12], First Schedule.
- Export of goods (with customs documentation)
- Export of services consumed outside Zimbabwe
- International transport services
- Basic foodstuffs (maize meal, bread, fresh milk, sugar, cooking oil, salt, fresh fruits and vegetables)
- Farming inputs (seeds, fertilizers, pesticides, stockfeed, animal remedies)
- Medical supplies and equipment (as specified)
- Fuel (diesel, petrol -- subject to separate fuel levy)
- Electricity (for domestic use, specified threshold)

### Exempt Supplies [T1]
**Legislation:** VAT Act [23:12], Second Schedule.
- Financial services (interest, forex, life insurance premiums)
- Medical and healthcare services (by registered practitioners)
- Educational services (by registered institutions)
- Residential rental
- Public passenger transport (omnibus services)
- Postal services
- Water supplied by local authorities

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, NSSA, PAYE, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Zimbabwe)
- SADC/COMESA: regional partners but no common VAT
- Rest of World

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (reverse charge)
- **Legislation:** VAT Act [23:12], s.8 (place of supply)

---

## Step 3: Fiscalised Electronic Device Requirements [T1]

**Legislation:** VAT Act [23:12], s.32C; ZIMRA Fiscalisation Regulations.

- ALL VAT-registered operators MUST use ZIMRA-approved fiscalised electronic devices (fiscal cash registers, fiscal printers, or electronic fiscal devices)
- Every sale must be recorded through the device and a fiscalised receipt/invoice issued
- Device must be connected to ZIMRA's server in real-time or near-real-time
- Input VAT is ONLY recoverable if supported by a valid fiscalised tax invoice or customs documentation
- Penalty for non-compliance: Level 6 fine or imprisonment up to 2 years, plus 100% of the tax evaded

**This is strictly enforced. No exceptions. Non-fiscalised invoices from VAT-registered operators cannot support input VAT claims.**

---

## Step 4: VAT Return Form Structure [T1]

Filed bi-monthly (or monthly for large taxpayers) via ZIMRA e-Services.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1 | Standard-rated supplies (15%) | Net value of taxable sales |
| 2 | Zero-rated supplies | Net value of zero-rated sales |
| 3 | Exempt supplies | Net value of exempt sales |
| 4 | Total supplies | 1 + 2 + 3 |
| 5 | Output VAT (15% on Box 1) | VAT on standard-rated |
| 6 | Output VAT on imported services (reverse charge) | Self-assessed |
| 7 | Output adjustments | Credit notes, deemed supplies |
| 8 | Total output VAT | 5 + 6 + 7 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 9 | Local taxable purchases (with fiscal invoice) | Net value |
| 10 | Imports (customs entries) | Net value from customs |
| 11 | Input VAT on local purchases | VAT on Box 9 |
| 12 | Input VAT on imports | Customs VAT |
| 13 | Input VAT on imported services | Reverse charge input |
| 14 | Capital goods input VAT | Subset |
| 15 | Input VAT adjustments | Blocked, apportionment |
| 16 | Allowable input VAT | 11 + 12 + 13 + 14 - 15 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 17 | Net VAT payable/(refundable) | 8 - 16 |
| 18 | Credit brought forward | Prior period |
| 19 | Net amount payable/(refundable) | 17 - 18 |

---

## Step 5: Reverse Charge [T1]

**Legislation:** VAT Act [23:12], s.13 (imported services).

When a Zimbabwe VAT-registered operator receives services from a non-resident:
1. Self-assess output VAT at 15% (Box 6)
2. Claim input VAT at 15% (Box 13) if for taxable supplies
3. Net effect: zero for fully taxable businesses

---

## Step 6: Multi-Currency Considerations [T2]

**Legislation:** Finance Act amendments; ZIMRA Practice Notes.

Zimbabwe operates a multi-currency system. VAT returns may need to be filed in ZiG (Zimbabwe Gold) or USD depending on ZIMRA's current requirements:
- Transactions in USD: convert to ZiG at the prevailing interbank exchange rate on the date of supply (if filing in ZiG)
- Transactions in ZiG: reported directly
- **Flag for reviewer: exchange rate rules change frequently in Zimbabwe. Confirm current ZIMRA requirements for the filing period.**

---

## Step 7: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** VAT Act [23:12], s.16 (non-deductible input tax).
- Motor vehicles for personal transport (< 9 seats), unless for taxi/hire (s.16(a))
- Entertainment expenses (s.16(b))
- Club subscriptions (recreational) (s.16(c))
- Personal use goods and services (s.16(d))
- Purchases without valid fiscalised tax invoice (s.16(e))

### Partial Exemption [T2]
**Legislation:** VAT Act [23:12], s.15 (apportionment).
`Recovery % = (Taxable Supplies / Total Supplies) * 100`
**Flag for reviewer: ZIMRA may approve alternative methods.**

---

## Step 8: Deemed Supplies [T1]

**Legislation:** VAT Act [23:12], s.5.

A deemed supply arises when:
- Goods applied for non-business purposes
- Business gifts exceeding USD 25 (or equivalent) per recipient per year
- Business assets used for private purposes
- Cessation of registration while holding stock/assets

Output VAT at 15% on open market value.

---

## Step 9: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | USD 25,000 in taxable supplies in any 12-month period (or ZiG equivalent) -- revised from USD 40,000 effective 1 January 2024 | VAT Act [23:12], s.23 |
| Voluntary registration | Below threshold (with ZIMRA approval) | VAT Act [23:12], s.23 |
| Bi-monthly filing | Standard | VAT Act [23:12], s.28 |
| Monthly filing | Large taxpayers (designated by ZIMRA) | ZIMRA designation |
| Gift de minimis | USD 25 per recipient per year | VAT Act [23:12], s.5 |

---

## Step 10: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return (bi-monthly) | Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec | 25th of month following period | VAT Act [23:12], s.28 |
| VAT return (monthly) | Monthly (large taxpayers) | 25th of following month | ZIMRA designation |
| Payment | Same as return | Same deadline | VAT Act [23:12], s.28 |

### Penalties [T1]
- Late filing: USD 30 per day of default
- Late payment: 10% surcharge + interest at ZIMRA prescribed rate per month
- Failure to register: 100% of tax due plus penalties
- Failure to fiscalise: criminal offence

---

## PROHIBITIONS [T1]

- NEVER allow input VAT recovery without a valid fiscalised tax invoice or customs documentation
- NEVER let AI guess return box assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered operators to claim input VAT
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER accept non-fiscalised invoices for input VAT purposes
- NEVER ignore exchange rate conversion requirements under multi-currency regime

---

## Step 11: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Zimbabwe company uses AWS. Monthly USD 100.
**Resolution:** Reverse charge at 15%. Output Box 6, Input Box 13. Net zero.
**Legislation:** VAT Act [23:12], s.13.

### EC2 -- Non-fiscalised invoice from registered operator [T1]
**Situation:** VAT-registered supplier issues handwritten invoice (no fiscal device).
**Resolution:** Input VAT NOT recoverable. Even if supplier is registered, non-fiscalised invoice cannot support input VAT claim.
**Legislation:** VAT Act [23:12], s.32C.

### EC3 -- Export of tobacco (zero-rated) [T1]
**Situation:** Tobacco exporter ships to Mozambique.
**Resolution:** Zero-rated. Box 2. No output VAT. Input VAT fully recoverable.
**Legislation:** VAT Act [23:12], First Schedule.

### EC4 -- Motor vehicle (blocked) [T1]
**Situation:** Company buys sedan for director.
**Resolution:** Input VAT BLOCKED. Cost includes irrecoverable VAT.
**Legislation:** VAT Act [23:12], s.16(a).

### EC5 -- USD/ZiG conversion [T2]
**Situation:** Transaction invoiced in USD, return filed in ZiG.
**Resolution:** Convert using interbank rate on date of supply. Flag for reviewer: confirm current ZIMRA exchange rate policy.
**Legislation:** Finance Act; ZIMRA Practice Notes.

### EC6 -- Farming inputs (zero-rated) [T1]
**Situation:** Farmer purchases seeds and fertilizer from registered supplier.
**Resolution:** Zero-rated by supplier. Box 2 on supplier's return. No output VAT.
**Legislation:** VAT Act [23:12], First Schedule.

### EC7 -- Deemed supply on cessation [T1]
**Situation:** Business deregisters with USD 50,000 inventory.
**Resolution:** Deemed supply. Output VAT at 15% on market value.
**Legislation:** VAT Act [23:12], s.5.

### EC8 -- Mining company input VAT refund [T3]
**Situation:** Mining company claims large input VAT refund on capital equipment.
**Resolution:** Escalate. Mining sector has specific provisions and ZIMRA audit thresholds for large refund claims.
**Legislation:** Mines and Minerals Act; VAT Act [23:12].

---

## Step 12: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

---

## Step 13: Test Suite

### Test 1 -- Standard sale [T1]
**Input:** Company sells goods USD 10,000 net.
**Expected output:** Box 1 = USD 10,000. Box 5 = USD 1,500 (15%).

### Test 2 -- Local purchase with fiscal invoice [T1]
**Input:** Company buys supplies. Fiscal invoice: USD 5,000 + USD 750 VAT.
**Expected output:** Box 11 = USD 750. Recoverable.

### Test 3 -- Purchase without fiscal invoice [T1]
**Input:** Company buys from registered supplier. Handwritten receipt: USD 2,000 + USD 300 VAT.
**Expected output:** Input VAT = USD 0 (no fiscal invoice). Cost = USD 2,300.

### Test 4 -- Reverse charge [T1]
**Input:** Company receives consulting from SA firm. USD 20,000.
**Expected output:** Box 6 = USD 3,000 (15% output). Box 13 = USD 3,000 (input). Net zero.

### Test 5 -- Export (zero-rated) [T1]
**Input:** Exporter ships goods USD 500,000.
**Expected output:** Box 2 = USD 500,000. Output VAT = 0. Input VAT recoverable.

### Test 6 -- Blocked (entertainment) [T1]
**Input:** Company hosts event. Fiscal invoice: USD 3,000 + USD 450 VAT.
**Expected output:** Input VAT = USD 0 (BLOCKED). Cost = USD 3,450.

### Test 7 -- Deemed supply (gift) [T1]
**Input:** Company gives client gifts worth USD 200 (market value).
**Expected output:** Deemed supply (exceeds USD 25 threshold). Output VAT = USD 30 (15%).

### Test 8 -- Exempt supply [T1]
**Input:** Bank earns interest USD 1,000,000.
**Expected output:** Box 3 = USD 1,000,000. No output VAT. Related input NOT recoverable.

---

## Step 14: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax:** 24.72% (24% + 3% AIDS levy).
- **PAYE:** Progressive rates 0%-40% + AIDS levy.
- **NSSA:** Employer 4.5% + employee 4.5% (capped). Separate from VAT.
- **IMTT (Intermediated Money Transfer Tax):** 2% on electronic transactions. Separate from VAT.

---

## Contribution Notes

Zimbabwe-specific elements include the fiscalised device requirement, multi-currency regime (ZiG/USD), bi-monthly filing, 15% rate, and deemed supply rules with low de minimis threshold (USD 25).

**A skill may not be published without sign-off from a licensed practitioner (ICAZ/PAAB member) in Zimbabwe.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
