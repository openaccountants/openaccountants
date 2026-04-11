---
name: zambia-vat
description: Use this skill whenever asked to prepare, review, or create a Zambia VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Zambia VAT", "ZRA return", "fill in VAT return", or any request involving Zambia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Zambia VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, withholding VAT, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Zambia VAT-related work.
---

# Zambia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Zambia (Republic of Zambia) |
| Jurisdiction Code | ZM |
| Primary Legislation | Value Added Tax Act No. 4 of 1995 (Cap. 331), as amended |
| Supporting Legislation | VAT (General) Rules; Tax Administration Act 2014 (as amended); Customs and Excise Act |
| Tax Authority | Zambia Revenue Authority (ZRA) |
| Filing Portal | https://taxonline.zra.org.zm (TaxOnline) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed accountant (ZICA member) in Zambia |
| Validation Date | Pending |
| Last Verified | 2026-04-10 (web-verified against ZRA, PWC, M&J Consultants) |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories, withholding VAT. Tier 2: partial exemption, mixed supplies, reverse VAT on imports. Tier 3: mining sector, multi-facility economic zones, tax incentive agreements. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for licensed accountant.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and TPIN (Taxpayer Identification Number)** [T1]
2. **VAT registration status** [T1] -- registered or unregistered
3. **VAT period** [T1] -- monthly filing
4. **Industry/sector** [T2] -- impacts classification (mining, agriculture, tourism)
5. **Does the business make exempt supplies?** [T2] -- if yes, apportionment required
6. **Is the business a designated withholding VAT agent?** [T1] -- ZRA designates agents
7. **Does the business import goods?** [T1] -- customs VAT
8. **Excess credit brought forward** [T1]

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 16% | Standard rate | VAT Act Cap. 331, s.16 |
| 0% | Zero rate (exports, specified supplies) | VAT Act Cap. 331, First Schedule |
| Exempt | No VAT, no input recovery | VAT Act Cap. 331, Second Schedule |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Act Cap. 331, First Schedule.
- Export of goods (with customs documentation)
- Export of services consumed outside Zambia
- International transport services
- Medical equipment (as specified by Minister)
- Agricultural inputs (seeds, fertilizers, pesticides, farming equipment as specified)
- Mealie meal, bread, milk (basic foodstuffs)
- Electricity for domestic use (first 300 kWh)
- Supplies to diplomats

### Exempt Supplies [T1]
**Legislation:** VAT Act Cap. 331, Second Schedule.
- Financial services (interest, forex, life insurance premiums)
- Medical and healthcare services
- Educational services (by authorized institutions)
- Residential rental
- Public passenger transport
- Postal services by Zambia Postal Services Corporation
- Water supplied by public utilities (domestic use)

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, NAPSA, PAYE, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Zambia)
- SADC/COMESA: regional partners but no common VAT
- Rest of World
- **Note:** No common VAT area.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (reverse charge)
- **Legislation:** VAT Act Cap. 331, s.7 (place of supply)

---

## Step 3: VAT Return Form Structure [T1]

Filed monthly via ZRA TaxOnline.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1 | Standard-rated supplies (16%) | Net taxable sales |
| 2 | Zero-rated supplies | Zero-rated sales |
| 3 | Exempt supplies | Exempt sales |
| 4 | Total supplies | 1 + 2 + 3 |
| 5 | Output VAT (16% on Box 1) | VAT on standard-rated |
| 6 | Reverse VAT on imported services | Self-assessed output |
| 7 | Output adjustments | Credit notes |
| 8 | Total output VAT | 5 + 6 + 7 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 9 | Local taxable purchases | Net value |
| 10 | Imports (customs entries) | Net value from customs |
| 11 | Input VAT on local purchases | VAT on Box 9 |
| 12 | Input VAT on imports | Customs VAT |
| 13 | Input VAT on imported services (reverse charge) | Self-assessed input |
| 14 | Capital goods input VAT | Subset |
| 15 | Input VAT adjustments | Blocked, apportionment |
| 16 | Allowable input VAT | 11 + 12 + 13 + 14 - 15 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 17 | Net VAT payable/(refundable) | 8 - 16 |
| 18 | Credit brought forward | Prior period |
| 19 | Withholding VAT credits | From withholding certificates |
| 20 | Net amount payable/(refundable) | 17 - 18 - 19 |

---

## Step 4: Withholding VAT [T1]

**Legislation:** VAT Act Cap. 331, s.23A; ZRA Practice Note.

### Mechanism
- Designated withholding VAT agents (government, parastatals, designated large companies) withhold VAT from payments to VAT-registered suppliers
- Withholding rate: 100% of the VAT amount on the invoice (i.e., the agent withholds the full VAT and pays only the net amount to the supplier)
- Supplier receives a withholding VAT certificate
- Supplier claims credit against output VAT (Box 19)
- Agent remits withheld VAT directly to ZRA

### Example [T1]
Invoice: ZMW 100,000 + ZMW 16,000 VAT = ZMW 116,000.
Agent withholds: ZMW 16,000 (100% of VAT).
Supplier receives: ZMW 100,000.
Supplier claims ZMW 16,000 credit (Box 19).

**Note:** Unlike many countries where only a percentage of VAT is withheld, Zambia withholds 100% of the VAT amount.

---

## Step 5: Reverse Charge [T1]

**Legislation:** VAT Act Cap. 331, s.13 (reverse VAT on imported services).

When a Zambia VAT-registered person receives services from a non-resident:
1. Self-assess output VAT at 16% (Box 6)
2. Claim input VAT at 16% (Box 13) if for taxable supplies
3. Net effect: zero for fully taxable businesses

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** VAT Act Cap. 331, s.18 (non-deductible input tax).
- Motor vehicles (< 9 seats) unless for taxi, car hire, or driving instruction (s.18(a))
- Entertainment expenses (s.18(b))
- Club subscriptions (recreational) (s.18(c))
- Personal use goods and services (s.18(d))
- Purchases without valid tax invoice (s.18(e))

### Partial Exemption [T2]
**Legislation:** VAT Act Cap. 331, s.17 (apportionment).
`Recovery % = (Taxable Supplies / Total Supplies) * 100`
**Flag for reviewer: ZRA may approve alternative methods.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | ZMW 800,000 annual turnover | VAT Act Cap. 331, s.6 |
| Voluntary registration | Below ZMW 800,000 (with ZRA approval) | VAT Act Cap. 331, s.6 |
| Withholding VAT rate | 100% of VAT on invoice | ZRA Practice Note |
| VAT refund | Excess credits after 4 months | VAT Act Cap. 331, s.21 |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return | Monthly | 18th of following month | VAT Act Cap. 331, s.22 |
| Payment | Monthly | 18th of following month | VAT Act Cap. 331, s.22 |
| Withholding VAT remittance | Monthly | 18th of following month | ZRA Practice Note |

### Penalties [T1]
- Late filing: 1,000 penalty units (K300) per day or 0.5% of tax due, whichever is greater
- Late payment: 5% per month + Bank of Zambia discount rate interest
- Failure to register: 100% of tax due plus penalties

---

## PROHIBITIONS [T1]

- NEVER let AI guess return box assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input VAT
- NEVER ignore withholding VAT credits (100% of VAT) when computing net
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER accept invoices without valid TPIN
- NEVER confuse Zambia withholding VAT (100% of VAT) with other countries' withholding rates

---

## Step 9: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Company subscribes to Microsoft 365. Monthly USD 50.
**Resolution:** Reverse charge at 16%. Output Box 6, Input Box 13. Net zero.
**Legislation:** VAT Act Cap. 331, s.13.

### EC2 -- Export of copper cathodes (zero-rated) [T1]
**Situation:** Mining company exports copper to China.
**Resolution:** Zero-rated. Box 2. No output VAT. Input VAT fully recoverable.
**Legislation:** VAT Act Cap. 331, First Schedule.

### EC3 -- Withholding VAT by government ministry [T1]
**Situation:** Ministry pays VAT-registered contractor. Invoice: ZMW 500,000 + ZMW 80,000 VAT.
**Resolution:** Ministry withholds ZMW 80,000 (100% of VAT). Contractor receives ZMW 500,000. Claims ZMW 80,000 credit (Box 19).
**Legislation:** VAT Act Cap. 331, s.23A.

### EC4 -- Motor vehicle (blocked) [T1]
**Situation:** Company buys sedan for director.
**Resolution:** Input VAT BLOCKED. Cost includes irrecoverable VAT.
**Legislation:** VAT Act Cap. 331, s.18(a).

### EC5 -- Mining sector [T3]
**Situation:** Mining company seeks VAT refund on capital equipment.
**Resolution:** Escalate. Mining sector has specific provisions and refund mechanisms. Development agreements may modify standard rules.
**Legislation:** Mines and Minerals Development Act; specific development agreements.

### EC6 -- Agricultural inputs (zero-rated) [T1]
**Situation:** Farm purchases fertilizer and seeds.
**Resolution:** Zero-rated by supplier. No output VAT charged. Supplier reports in Box 2.
**Legislation:** VAT Act Cap. 331, First Schedule.

### EC7 -- Bad debt relief [T2]
**Situation:** Customer unpaid for 12+ months.
**Resolution:** Bad debt relief available if: debt outstanding > 12 months, written off, recovery efforts made. Flag for reviewer: ZRA documentation requirements.
**Legislation:** VAT Act Cap. 331, s.22A.

### EC8 -- Multi-Facility Economic Zone (MFEZ) supply [T2]
**Situation:** Supplier provides goods to MFEZ operator.
**Resolution:** MFEZ operators may receive zero-rated supplies under specific conditions. Flag for reviewer: verify MFEZ certificate and applicable rules.
**Legislation:** MFEZ Act; VAT Act Cap. 331.

---

## Step 10: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

---

## Step 11: Test Suite

### Test 1 -- Standard sale [T1]
**Input:** Company sells goods ZMW 100,000 net.
**Expected output:** Box 1 = ZMW 100,000. Box 5 = ZMW 16,000 (16%).

### Test 2 -- Local purchase [T1]
**Input:** Company buys supplies. Invoice: ZMW 50,000 + ZMW 8,000 VAT.
**Expected output:** Box 11 = ZMW 8,000. Recoverable.

### Test 3 -- Reverse charge [T1]
**Input:** Company receives services from SA firm. ZMW 200,000. No VAT.
**Expected output:** Box 6 = ZMW 32,000 (16% output). Box 13 = ZMW 32,000 (input). Net zero.

### Test 4 -- Export [T1]
**Input:** Exporter ships copper ZMW 5,000,000.
**Expected output:** Box 2 = ZMW 5,000,000. Output VAT = 0. Input VAT recoverable.

### Test 5 -- Withholding VAT [T1]
**Input:** Government pays supplier. Invoice: ZMW 300,000 + ZMW 48,000 VAT.
**Expected output:** Withholding = ZMW 48,000 (100%). Supplier claims Box 19 = ZMW 48,000.

### Test 6 -- Blocked (entertainment) [T1]
**Input:** Company hosts dinner. ZMW 20,000 + ZMW 3,200 VAT.
**Expected output:** Input VAT = 0 (BLOCKED). Cost = ZMW 23,200.

---

## Step 12: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax:** 30% (standard); mining: 30% + mineral royalty.
- **PAYE:** Progressive rates 0%-37.5%.
- **NAPSA:** Employer 5% + employee 5% (capped). Separate from VAT.
- **Skills Development Levy:** 0.5% of payroll. Separate from VAT.

---

## Contribution Notes

Zambia-specific elements include the 16% rate, 100% withholding VAT mechanism, mining sector escalation, MFEZ treatment, and agricultural zero-rating.

**A skill may not be published without sign-off from a licensed practitioner (ZICA member) in Zambia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
