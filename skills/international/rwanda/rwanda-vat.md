---
name: rwanda-vat
description: Use this skill whenever asked to prepare, review, or create a Rwanda VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Rwanda VAT", "RRA return", "fill in VAT return", or any request involving Rwanda VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Rwanda VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, EBM requirements, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Rwanda VAT-related work.
---

# Rwanda VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Rwanda (Republic of Rwanda) |
| Jurisdiction Code | RW |
| Primary Legislation | Law No. 049/2023 of 05/09/2023 establishing the Value Added Tax, as amended by Law No. 009/2025 of 27/05/2025 (repeals Law No. 37/2012) |
| Supporting Legislation | Ministerial Orders; Law No. 026/2019 on Tax Procedures; EAC Customs Management Act 2004 |
| Tax Authority | Rwanda Revenue Authority (RRA) |
| Filing Portal | https://efiling.rra.gov.rw (e-Tax system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed CPA (ICPAR member) in Rwanda |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, EBM requirements, blocked categories. Tier 2: partial exemption, mixed supplies. Tier 3: mining, special economic zones, investment incentives. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue. Licensed accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to licensed accountant.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know:

1. **Entity name and TIN** [T1] -- Rwanda TIN
2. **VAT registration status** [T1] -- registered or unregistered
3. **VAT period** [T1] -- monthly (standard) or quarterly (small taxpayers with turnover < RWF 200M)
4. **Industry/sector** [T2] -- impacts classification
5. **Does the business make exempt supplies?** [T2] -- if yes, apportionment required
6. **Does the business import goods?** [T1] -- customs VAT at border
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business using certified EBM (Electronic Billing Machine)?** [T1] -- mandatory for all VAT-registered

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 18% | Standard rate | Law 049/2023 (as amended by Law 009/2025), Art. 5 |
| 0% | Zero rate (exports, specified supplies) | Law 049/2023 (as amended by Law 009/2025), Art. 6; Annex I |
| Exempt | No VAT, no input recovery | Law 049/2023 (as amended by Law 009/2025), Art. 7; Annex II |

### Zero-Rated Supplies [T1]
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Annex I.
- Export of goods (with proof of export)
- Export of services consumed outside Rwanda
- International transport services
- Supply of goods and services to diplomats (with RRA approval)
- Supplies to registered investors in special economic zones (with certificate)

### Exempt Supplies [T1]
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Annex II.
- Unprocessed agricultural products
- Financial services (interest, foreign exchange transactions, life insurance premiums). **Note:** Fee-based financial services became taxable from 1 July 2025 under Law 009/2025
- Medical and healthcare services
- Educational services (by registered institutions)
- Residential rental
- Transportation of persons (public transport). **Note:** Local transport of goods by road became taxable from 1 July 2025
- Books, newspapers, and magazines (locally produced)
- Water and electricity for domestic use
- Funeral and burial services
- **Note:** Mobile phones, ICT equipment, and fuel have become taxable from 1 July 2025 (previously exempt)

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, RSSB contributions, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Rwanda)
- EAC: Kenya, Uganda, Tanzania, Burundi, South Sudan, DRC
- Rest of World
- **Note:** No common VAT area in EAC.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (reverse charge)
- **Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 4 (place of supply)

---

## Step 3: Electronic Billing Machine (EBM) Requirements [T1]

**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 22; Ministerial Order 003/12/10/TC.

- ALL VAT-registered taxpayers MUST use an RRA-certified Electronic Billing Machine (EBM)
- Every sale must be recorded through EBM and a system-generated receipt issued
- EBM receipts contain a unique identification number linked to the RRA system
- Input VAT is ONLY recoverable if supported by a valid EBM receipt or customs documentation
- Non-EBM invoices from VAT-registered suppliers: input VAT NOT recoverable
- Penalty for failure to use EBM: 100% of the tax due on unreported transactions

**This is unique to Rwanda and strictly enforced. No exceptions.**

---

## Step 4: VAT Return Form Structure [T1]

Filed monthly (or quarterly for small taxpayers) via RRA e-Tax.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| A1 | Standard-rated supplies (18%) | Net value of taxable sales |
| A2 | Zero-rated supplies | Net value of exports/zero-rated |
| A3 | Exempt supplies | Net value of exempt supplies |
| A4 | Total supplies | A1 + A2 + A3 |
| A5 | Output VAT (18% on A1) | VAT on standard-rated supplies |
| A6 | Output adjustments | Credit notes, corrections |
| A7 | Total output tax | A5 + A6 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| B1 | Local taxable purchases (with EBM receipt) | Net value |
| B2 | Imports (customs entries) | Net value from customs docs |
| B3 | Imported services (reverse charge) | Net value |
| B4 | Input VAT on local purchases | VAT on B1 |
| B5 | Input VAT on imports | VAT on B2 |
| B6 | Input VAT on imported services | 18% on B3 |
| B7 | Total input VAT | B4 + B5 + B6 |
| B8 | Input VAT adjustments | Blocked items, apportionment |
| B9 | Allowable input VAT | B7 - B8 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| C1 | Net VAT payable/(refundable) | A7 - B9 |
| C2 | Credit brought forward | Prior period |
| C3 | Net amount payable/(refundable) | C1 - C2 |

---

## Step 5: Reverse Charge [T1]

**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 13 (imported services).

When a Rwanda VAT-registered person receives services from a non-resident:
1. Self-assess output VAT at 18%
2. Claim input VAT at 18% if for taxable supplies
3. Net effect: zero for fully taxable businesses

**Exceptions:** Out-of-scope payments; services consumed entirely outside Rwanda.

---

## Step 6: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 17 (non-deductible input tax).
- Entertainment and hospitality
- Motor vehicles (< 10 seats) unless for taxi/hire business
- Club subscriptions (recreational)
- Personal/non-business use
- Purchases without valid EBM receipt

### Partial Exemption [T2]
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 16(3).
`Recovery % = (Taxable Supplies / Total Supplies) * 100`
**Flag for reviewer: RRA must approve method.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | RWF 20,000,000 annual turnover | Law 049/2023 (as amended by Law 009/2025), Art. 8 |
| Voluntary registration | Below RWF 20,000,000 (with RRA approval) | Law 049/2023 (as amended by Law 009/2025), Art. 9 |
| Quarterly filing eligibility | Turnover < RWF 200,000,000 | RRA guidelines |
| EBM penalty | 100% of unreported tax | Law 049/2023 (as amended by Law 009/2025), Art. 34 |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return (standard) | Monthly | 15th of following month | Law 049/2023 (as amended by Law 009/2025), Art. 20 |
| VAT return (small taxpayer) | Quarterly | 15th of month following quarter | Law 049/2023 (as amended by Law 009/2025), Art. 20 |
| VAT payment | Same as return | Same as return deadline | Law 049/2023 (as amended by Law 009/2025), Art. 20 |

### Penalties [T1]
- Late filing: 20% of tax due + RWF 100,000 minimum
- Late payment: 1.5% per month of outstanding amount
- Failure to register: 100% of tax due
- Failure to use EBM: 100% of unreported tax

---

## PROHIBITIONS [T1]

- NEVER allow input VAT recovery without valid EBM receipt or customs documentation
- NEVER let AI guess return box assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input VAT
- NEVER treat EAC transactions as intra-community supplies
- NEVER compute any number -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER accept non-EBM invoices for input VAT purposes

---

## Step 9: Edge Case Registry

### EC1 -- Import of services (cloud software) [T1]
**Situation:** Rwanda company subscribes to Google Workspace. Monthly USD 50. No VAT.
**Resolution:** Reverse charge. Self-assess output and input VAT at 18%. Net zero if fully taxable.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 13.

### EC2 -- Supplier issues non-EBM invoice [T1]
**Situation:** VAT-registered supplier provides services but issues a handwritten invoice without EBM.
**Resolution:** Input VAT NOT recoverable. Even though supplier is VAT-registered, absence of EBM receipt means no input VAT claim. The cost is borne in full including irrecoverable VAT.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 22.

### EC3 -- Export of goods (zero-rated) [T1]
**Situation:** Rwanda exporter ships tea to Mombasa for export.
**Resolution:** Zero-rated. Report in A2. No output VAT. Input VAT fully recoverable. Must have export documentation.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Annex I.

### EC4 -- Import from EAC state [T1]
**Situation:** Rwanda company imports goods from Kenya. Customs at Gatuna border.
**Resolution:** VAT at 18% charged at customs. Recoverable as input VAT (B5) if for taxable supplies. No intra-community mechanism.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 12; EAC CMA 2004.

### EC5 -- Motor vehicle (blocked) [T1]
**Situation:** Company purchases sedan for manager.
**Resolution:** Input VAT BLOCKED. Passenger vehicle < 10 seats not for hire. Cost includes irrecoverable VAT.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 17.

### EC6 -- Special Economic Zone (SEZ) supply [T2]
**Situation:** Supplier provides goods to an entity operating in Kigali SEZ.
**Resolution:** May be zero-rated if buyer has valid SEZ certificate. Flag for reviewer: confirm certificate validity and whether specific goods/services qualify.
**Legislation:** Law 049/2023 (as amended by Law 009/2025); Special Economic Zones Law No. 05/2011.

### EC7 -- Credit note adjustment [T1]
**Situation:** Supplier issues credit note for returned goods. Original sale was standard-rated.
**Resolution:** Reduce output VAT by the VAT component of credit note. Report in A6. Buyer must also adjust input VAT.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 21.

### EC8 -- Deemed supply on cessation [T1]
**Situation:** Business deregisters while holding RWF 50,000,000 inventory.
**Resolution:** Deemed supply. Output VAT at 18% on market value of inventory/assets at deregistration date.
**Legislation:** Law 049/2023 (as amended by Law 009/2025), Art. 3(3).

---

## Step 10: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:
```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [which and why]
Action Required: Licensed accountant (ICPAR member) must confirm before filing.
```

When Claude identifies a [T3] situation:
```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside scope]
Action Required: Do not classify. Refer to licensed accountant. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Standard local sale [T1]
**Input:** Rwanda company sells goods for RWF 5,000,000 net. Standard-rated.
**Expected output:** A1 = RWF 5,000,000. A5 = RWF 900,000 (18%).

### Test 2 -- Local purchase with EBM receipt [T1]
**Input:** Company purchases office supplies. EBM receipt: RWF 1,000,000 + RWF 180,000 VAT = RWF 1,180,000.
**Expected output:** B1 = RWF 1,000,000. B4 = RWF 180,000. Recoverable.

### Test 3 -- Purchase without EBM receipt [T1]
**Input:** Company purchases from VAT-registered supplier. Handwritten invoice (no EBM): RWF 500,000 + RWF 90,000 VAT.
**Expected output:** Input VAT = RWF 0 (no EBM receipt). Cost = RWF 590,000.

### Test 4 -- Reverse charge [T1]
**Input:** Company receives IT services from Indian firm. RWF 3,000,000. No VAT.
**Expected output:** Output VAT = RWF 540,000. Input VAT = RWF 540,000. Net = zero.

### Test 5 -- Export (zero-rated) [T1]
**Input:** Exporter ships minerals worth RWF 50,000,000.
**Expected output:** A2 = RWF 50,000,000. Output VAT = RWF 0. Input VAT recoverable.

### Test 6 -- Blocked (entertainment) [T1]
**Input:** Company hosts client reception. EBM receipt: RWF 2,000,000 + RWF 360,000 VAT.
**Expected output:** Input VAT = RWF 0 (BLOCKED). Cost = RWF 2,360,000.

### Test 7 -- Exempt supply [T1]
**Input:** Hospital provides medical services for RWF 10,000,000.
**Expected output:** A3 = RWF 10,000,000. No output VAT. Related input VAT NOT recoverable.

### Test 8 -- Import from EAC [T1]
**Input:** Company imports goods from Tanzania. Customs value RWF 8,000,000. VAT 18%.
**Expected output:** B2 = RWF 8,000,000. B5 = RWF 1,440,000. Recoverable if taxable.

---

## Step 12: Out of Scope -- Direct Tax [T3]

- **Corporate Income Tax:** 30% standard. Micro/small enterprises: concessional rates.
- **PAYE:** Progressive rates 0% to 30%.
- **RSSB:** 5% employer + 3% employee (pension); 0.3% employer (maternity).

---

## Contribution Notes

Rwanda-specific elements include the mandatory EBM requirement (unique enforcement tool), EAC customs treatment, and the strict penalty for non-EBM transactions. Updated April 2026 to reflect Law 049/2023 (replacing Law 37/2012) as amended by Law 009/2025: expanded VAT base (mobile phones, ICT equipment, fuel, fee-based financial services, local road transport now taxable from July 2025).

**A skill may not be published without sign-off from a licensed practitioner (ICPAR member) in Rwanda.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
