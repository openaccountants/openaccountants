---
name: mauritius-vat
description: Use this skill whenever asked to prepare, review, or create a Mauritius VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Mauritius VAT", "MRA return", "fill in VAT return", or any request involving Mauritius VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Mauritius VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines. ALWAYS read this skill before touching any Mauritius VAT-related work.
---

# Mauritius VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mauritius (Republic of Mauritius) |
| Jurisdiction Code | MU |
| Primary Legislation | Value Added Tax Act 1998 (Act No. 2 of 1998), as amended |
| Supporting Legislation | VAT Regulations; Mauritius Revenue Authority Act 2004; Customs Act 1988 |
| Tax Authority | Mauritius Revenue Authority (MRA) |
| Filing Portal | https://www.mra.mu (e-Filing) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed accountant (MIPA/ACCA member) in Mauritius |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, return mapping, registration, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, Global Business Licence (GBL) interactions, freeport. Tier 3: offshore sector, financial services complex structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag for licensed accountant.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate.

---

## Step 0: Client Onboarding Questions

1. **Entity name and BRN (Business Registration Number)** [T1]
2. **VAT registration number** [T1]
3. **VAT period** [T1] -- quarterly filing (standard) or monthly (large taxpayers)
4. **Industry/sector** [T2] -- impacts classification (tourism, financial services, freeport)
5. **Does the business make exempt supplies?** [T2] -- if yes, apportionment required
6. **Does the business import goods?** [T1] -- customs VAT at port
7. **Excess credit brought forward** [T1]
8. **Does the business hold a GBL (Global Business Licence)?** [T2] -- special regime

**If items 1-2 are unknown, STOP.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 15% | Standard rate | VAT Act 1998, s.9(1) |
| 0% | Zero rate (exports, specified supplies) | VAT Act 1998, First Schedule |
| Exempt | No VAT, no input recovery | VAT Act 1998, Second Schedule |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Act 1998, First Schedule.
- Export of goods (with customs documentation)
- Export of services (consumed outside Mauritius)
- International transport of passengers and goods
- Supply of goods to freeport operators (with certificate)
- Supply of certain basic foodstuffs (rice, flour, bread, cooking gas)
- Electricity for domestic use (first 75 kWh)

### Exempt Supplies [T1]
**Legislation:** VAT Act 1998, Second Schedule.
- Financial services (interest, forex transactions, life insurance premiums)
- Medical and healthcare services (by registered practitioners)
- Educational services (registered institutions)
- Residential rental
- Public transport
- Sale of residential land/buildings (first sale after construction may be taxable)
- Postal services by Mauritius Post

---

## Step 2: Transaction Classification Rules

### 2a. Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, NPF/NSF contributions, PAYE, dividends, loan repayments = OUT OF SCOPE

### 2b. Counterparty Location [T1]
- Domestic (Mauritius including Rodrigues)
- SADC/COMESA: regional trading partners but no common VAT
- Rest of World
- **Note:** Mauritius has no common VAT area with any regional bloc.

### 2c. Supply Type [T1]
- Goods / Services / Import of goods (customs) / Import of services (reverse charge)
- **Legislation:** VAT Act 1998, s.5-8 (place of supply)

---

## Step 3: VAT Return Form Structure [T1]

Filed quarterly (or monthly for large taxpayers) via MRA e-Filing.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1 | Standard-rated supplies (15%) | Net value of taxable sales |
| 2 | Zero-rated supplies | Net value of zero-rated sales |
| 3 | Exempt supplies | Net value of exempt supplies |
| 4 | Total supplies | 1 + 2 + 3 |
| 5 | Output VAT (15% on Box 1) | VAT on standard-rated supplies |
| 6 | Output VAT adjustments | Credit notes, corrections |
| 7 | Total output VAT | 5 + 6 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 8 | Local taxable purchases | Net value of local purchases |
| 9 | Imports (customs) | Net value from customs |
| 10 | Input VAT on local purchases | VAT on Box 8 |
| 11 | Input VAT on imports | VAT from customs (Box 9) |
| 12 | Capital goods input VAT | Subset of input VAT on capital assets |
| 13 | Input VAT adjustments | Blocked items, apportionment |
| 14 | Net input VAT | 10 + 11 + 12 - 13 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 15 | Net VAT payable/(refundable) | 7 - 14 |
| 16 | Credit brought forward | Prior period |
| 17 | Net amount payable/(refundable) | 15 - 16 |

---

## Step 4: Reverse Charge [T1]

**Legislation:** VAT Act 1998, s.7A (reverse charge on services from abroad).

When a Mauritius VAT-registered person receives services from a non-resident:
1. Self-assess output VAT at 15%
2. Claim input VAT at 15% if for taxable supplies
3. Net effect: zero for fully taxable businesses

---

## Step 5: Deductibility Check

### Blocked Input Tax [T1]
**Legislation:** VAT Act 1998, s.21 (non-deductible input tax).
- Motor vehicles (< 9 seats) unless for taxi, car hire, driving instruction, or for resale by motor vehicle dealer (s.21(a))
- Entertainment expenses (s.21(b))
- Club subscriptions (recreational) (s.21(c))
- Personal use goods and services (s.21(d))
- Purchases without valid VAT invoice (s.21(e))

### Partial Exemption [T2]
**Legislation:** VAT Act 1998, s.20 (apportionment).
`Recovery % = (Taxable Supplies / Total Supplies) * 100`
**Flag for reviewer: MRA may approve alternative methods.**

---

## Step 6: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory registration | MUR 6,000,000 annual turnover | VAT Act 1998, s.15(1) |
| Voluntary registration | Below MUR 6,000,000 (with MRA approval) | VAT Act 1998, s.15(2) |
| Monthly filing | Large taxpayer (designated by MRA) | MRA designation |
| Quarterly filing | Standard | VAT Act 1998, s.22 |
| VAT refund | Excess credits; tourist refund scheme | VAT Act 1998, s.25 |

---

## Step 7: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return (quarterly) | Quarterly | Last day of month following quarter | VAT Act 1998, s.22 |
| VAT return (monthly) | Monthly (large taxpayers) | 20th of following month | MRA designation |
| Payment | Same as return | Same deadline | VAT Act 1998, s.22 |

### Penalties [T1]
- Late filing: MUR 5,000 per month or part thereof
- Late payment: 2% per month on outstanding amount
- Failure to register: 100% of tax that should have been collected

---

## Step 8: Tourist Refund Scheme [T1]

**Legislation:** VAT Act 1998, s.25A.
- Tourists can claim VAT refund on goods purchased in Mauritius and taken out of the country
- Minimum purchase: MUR 2,300 per invoice from a single registered retailer
- Refund claimed at airport before departure
- Retailer must issue a Tourist Tax-Free Shopping receipt

---

## PROHIBITIONS [T1]

- NEVER let AI guess return box assignment
- NEVER allow recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input VAT
- NEVER compute numbers -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER accept invoices without valid VAT registration number
- NEVER confuse tourist refund with standard VAT refund mechanism

---

## Step 9: Edge Case Registry

### EC1 -- Import of services (SaaS) [T1]
**Situation:** Mauritius company subscribes to Zoom. Monthly USD 20.
**Resolution:** Reverse charge. Self-assess output and input VAT at 15%. Net zero.
**Legislation:** VAT Act 1998, s.7A.

### EC2 -- Export of services (offshore) [T1]
**Situation:** Mauritius IT company provides software development to US client.
**Resolution:** Zero-rated. Box 2. No output VAT. Input VAT fully recoverable.
**Legislation:** VAT Act 1998, First Schedule.

### EC3 -- Motor vehicle (blocked) [T1]
**Situation:** Company purchases sedan for director.
**Resolution:** Input VAT BLOCKED. Cost includes irrecoverable VAT.
**Legislation:** VAT Act 1998, s.21(a).

### EC4 -- Freeport operator supply [T2]
**Situation:** Company supplies goods to a freeport operator.
**Resolution:** May be zero-rated if buyer holds valid freeport certificate. Flag for reviewer: verify certificate.
**Legislation:** VAT Act 1998, First Schedule; Freeport Act 2004.

### EC5 -- GBL company [T3]
**Situation:** Global Business Licence (GBL) company makes supplies.
**Resolution:** Escalate. GBL companies have specific VAT treatment depending on nature of supplies and whether they serve domestic or international markets.
**Legislation:** Financial Services Act 2007; VAT Act 1998.

### EC6 -- Basic foodstuffs (zero-rated) [T1]
**Situation:** Wholesaler sells rice and flour.
**Resolution:** Zero-rated. Box 2. No output VAT. Input VAT on procurement costs recoverable.
**Legislation:** VAT Act 1998, First Schedule.

### EC7 -- Bad debt relief [T2]
**Situation:** Customer has not paid for 6+ months.
**Resolution:** Bad debt relief available if debt outstanding > 6 months, written off, reasonable recovery efforts made. Flag for reviewer: documentation requirements.
**Legislation:** VAT Act 1998, s.22A.

### EC8 -- Residential property sale [T2]
**Situation:** Developer sells newly constructed apartment.
**Resolution:** First sale of residential building by developer is standard-rated (15%). Subsequent resales are exempt. Flag for reviewer: confirm whether this is a first sale or subsequent.
**Legislation:** VAT Act 1998, s.5; Second Schedule.

---

## Step 10: Reviewer Escalation Protocol

```
REVIEWER FLAG / ESCALATION REQUIRED
[Standard format]
```

---

## Step 11: Test Suite

### Test 1 -- Standard sale [T1]
**Input:** Company sells goods MUR 1,000,000 net. Standard-rated.
**Expected output:** Box 1 = MUR 1,000,000. Box 5 = MUR 150,000 (15%).

### Test 2 -- Local purchase [T1]
**Input:** Company buys supplies. Invoice: MUR 500,000 + MUR 75,000 VAT.
**Expected output:** Box 10 = MUR 75,000. Recoverable.

### Test 3 -- Reverse charge [T1]
**Input:** Company receives consulting from UK firm. MUR 2,000,000. No VAT.
**Expected output:** Output VAT = MUR 300,000. Input VAT = MUR 300,000. Net zero.

### Test 4 -- Export (zero-rated) [T1]
**Input:** Exporter ships textiles MUR 10,000,000.
**Expected output:** Box 2 = MUR 10,000,000. Output VAT = 0. Input VAT recoverable.

### Test 5 -- Blocked (entertainment) [T1]
**Input:** Company hosts client dinner. MUR 200,000 + MUR 30,000 VAT.
**Expected output:** Input VAT = 0 (BLOCKED). Cost = MUR 230,000.

### Test 6 -- Exempt supply [T1]
**Input:** Bank earns interest MUR 50,000,000.
**Expected output:** Box 3 = MUR 50,000,000. No output VAT. Related input NOT recoverable.

---

## Step 12: Out of Scope -- Direct Tax [T3]

- **Corporate Tax:** 15%. Partial exemption regime for GBL companies.
- **PAYE:** Progressive rates. Employer obligation.
- **Social contributions (NPF/NSF):** Employer + employee. Separate from VAT.
- **CSG (Contribution Sociale Généralisée):** Employer 3% + employee 1.5%/3%. Separate.

---

## Contribution Notes

Mauritius-specific elements include the single 15% rate, tourist refund scheme, freeport treatment, GBL company interactions, and zero-rated basic foodstuffs.

**A skill may not be published without sign-off from a licensed practitioner in Mauritius.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
