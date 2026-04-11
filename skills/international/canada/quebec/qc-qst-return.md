---
name: qc-qst-return
description: >
  Use this skill whenever asked about Quebec Sales Tax (QST / TVQ) return preparation for a self-employed sole proprietor or small business. Trigger on phrases like "QST return", "TVQ", "Quebec sales tax", "QST filing", "input tax refund", "ITR", "QST registration", "Revenu Quebec QST", "9.975%", or any question about computing or filing QST. Covers QST rate (9.975%), small supplier threshold, input tax refunds (ITRs), interaction with federal GST/HST, and quarterly/annual filing. ALWAYS read this skill before touching any QST work.
version: 1.0
jurisdiction: CA-QC
tax_year: 2025
category: international
depends_on:
  - gst-workflow-base
  - ca-fed-gst-hst
---

# Quebec Sales Tax (QST) Return -- Self-Employed Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- Quebec |
| Jurisdiction Code | CA-QC |
| Primary Legislation | Act respecting the Quebec Sales Tax (AQST), CQLR c. T-0.1 |
| Supporting Legislation | Excise Tax Act (ETA) (federal GST); Quebec Regulation respecting the QST |
| Tax Authority | Revenu Quebec |
| Filing Portal | Revenu Quebec My Account (Mon dossier) / ClicSequr |
| Form | VD-403 (QST Return) -- filed separately from federal GST return |
| Supporting Forms | FP-2189 (General Rebate Application), FPZ-500 (registration) |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: QST rate, ITR computation, small supplier threshold, filing frequency, basic return assembly. Tier 2: place of supply, real property, used goods, bad debts. Tier 3: financial services, public sector bodies, non-resident suppliers. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## CRITICAL: QST Is Filed Separately from Federal GST

Unlike HST provinces (Ontario, BC PST is separate but not value-added), Quebec administers QST independently:

1. **Federal GST at 5%** -- filed with CRA
2. **Quebec QST at 9.975%** -- filed with Revenu Quebec
3. Two separate returns, two separate registrations, two separate refund claims

Since January 1, 2013, QST is harmonized with GST in terms of base (both apply to the same tax base), but they remain administratively separate.

---

## Step 0: Client Onboarding Questions

Before computing any QST figure, you MUST know:

1. **QST registration number** [T1] -- format: 10-digit number followed by TQ0001
2. **GST registration number** [T1] -- must also be GST-registered if QST-registered (mandatory since 2013)
3. **Filing frequency** [T1] -- monthly, quarterly, or annual (assigned by Revenu Quebec)
4. **Reporting period start and end dates** [T1]
5. **Total taxable supplies made in Quebec** [T1] -- goods and services sold
6. **Total zero-rated supplies** [T1] -- exports, basic groceries, prescription drugs
7. **Total exempt supplies** [T1] -- financial services, residential rent, health care
8. **Total QST collected or collectible** [T1]
9. **Total QST paid on business expenses (ITR-eligible)** [T1]
10. **Out-of-province sales** [T2] -- place of supply rules
11. **Self-supply of real property** [T2] -- if applicable

**If the supplier is not registered for QST, assess whether registration is required (Step 1).**

---

## Step 1: QST Registration Requirements [T1]

**Legislation:** AQST, s. 407 et seq.

### Mandatory Registration [T1]

| Threshold | Amount | Basis |
|-----------|--------|-------|
| Small supplier threshold | $30,000 | Taxable supplies in any single calendar quarter OR in the last four consecutive quarters |

### Rules [T1]

1. If taxable supplies exceed $30,000 in a single calendar quarter: must register **within 30 days** of exceeding the threshold
2. If taxable supplies exceed $30,000 over four consecutive quarters: must register by the end of the month following the quarter in which the threshold was exceeded
3. The $30,000 threshold is the **same as the federal GST small supplier threshold**
4. A person who is a small supplier for GST purposes is also a small supplier for QST purposes
5. **Voluntary registration** is permitted below the threshold (allows ITR claims)

### Exceptions [T1]

- Taxi/limousine operators must register regardless of revenue
- Non-resident suppliers providing digital services to Quebec consumers: must register if sales to Quebec exceed $30,000 (specified QST registration)

---

## Step 2: QST Rate and Tax Base -- 2025 [T1]

**Legislation:** AQST, s. 16

### Current Rate [T1]

| Tax | Rate | Effective Date |
|-----|------|---------------|
| QST | **9.975%** | January 1, 2013 -- present |

### Tax Base [T1]

QST applies to the **same base as GST**: the sale price of taxable goods and services. Since 2013, QST is calculated on the price **excluding GST** (no tax-on-tax).

```
Selling price (before taxes): $100.00
GST (5%):                      $5.00
QST (9.975%):                  $9.98  (9.975% of $100, NOT of $105)
Total:                        $114.98
```

### Supply Categories [T1]

| Category | QST Treatment | Examples |
|----------|--------------|----------|
| Taxable (standard) | 9.975% | Most goods and services |
| Zero-rated | 0% (but ITRs claimable) | Basic groceries, prescription drugs, exports, medical devices |
| Exempt | No QST (no ITRs claimable) | Financial services, residential rent (long-term), health care, educational services, childcare |

---

## Step 3: Computing QST Collectible [T1]

### Formula [T1]

```
QST collectible = Sum of (taxable supply amount x 9.975%) for each supply in the period
```

### Step-by-Step [T1]

1. **Identify all supplies made during the period**
2. **Classify each supply:** taxable, zero-rated, or exempt
3. **For taxable supplies:** compute QST at 9.975% on the selling price (excluding GST)
4. **For zero-rated supplies:** QST = $0, but include in total supplies
5. **For exempt supplies:** exclude from QST computation entirely
6. **Sum all QST collected or collectible** = QST on line 101 of VD-403

---

## Step 4: Input Tax Refunds (ITRs) [T1]

**Legislation:** AQST, s. 199 et seq.

ITRs are the QST equivalent of federal GST Input Tax Credits (ITCs). They allow recovery of QST paid on business expenses.

### Eligibility Rules [T1]

1. The expense must be for use in **commercial activities** (making taxable or zero-rated supplies)
2. The registrant must have **documentation** (invoice with supplier's QST number, amount of QST charged)
3. The ITR must be claimed within **4 years** from the due date of the return for the period in which the QST was paid

### ITR Computation [T1]

```
ITR = QST paid on eligible business expense x percentage of commercial use
```

### Common ITR Categories [T1]

| Expense | ITR Eligible? | Notes |
|---------|---------------|-------|
| Office supplies | Yes | 100% if fully for business |
| Computer/software | Yes | Prorate if personal use |
| Professional fees (accounting, legal) | Yes | Must be for business |
| Meals and entertainment | 50% | Only 50% of QST recoverable |
| Motor vehicle expenses | Prorate | Based on business use percentage |
| Home office expenses | Prorate | Based on workspace percentage |
| Rent (commercial lease) | Yes | 100% if business premises |
| Personal expenses | No | Never eligible |
| Exempt supplies inputs | No | No ITR for inputs used in exempt activities |

### Mixed-Use Assets [T1]

If an asset is used for both commercial and personal purposes:
- ITR = QST paid x commercial use percentage
- If commercial use is 90% or more: claim 100%
- If commercial use is 10% or less: claim 0%
- Between 10% and 90%: claim actual percentage

---

## Step 5: QST Return Assembly (VD-403) [T1]

### Line-by-Line Guide [T1]

| VD-403 Line | Description | How to Compute |
|-------------|-------------|----------------|
| Line 101 | Total QST collected or collectible | Sum of QST on all taxable supplies |
| Line 104 | QST adjustments (additions) | Self-assessments, change of use, bad debt recoveries |
| Line 105 | Total QST and adjustments | Line 101 + Line 104 |
| Line 106 | Input tax refunds (ITRs) | Step 4 computation |
| Line 107 | ITR adjustments (reductions) | Change of use, recapture |
| Line 108 | Net ITRs | Line 106 - Line 107 |
| Line 109 | Rebates | Public service body rebates, new housing rebate |
| Line 110 | Total ITRs and rebates | Line 108 + Line 109 |
| Line 111 | Net QST | Line 105 - Line 110 |
| Line 113 | Instalments paid | If applicable |
| Line 114 | Net tax owing or refund | Line 111 - Line 113 |

### Result [T1]

- If Line 114 is **positive**: QST is owing to Revenu Quebec
- If Line 114 is **negative**: refund is due from Revenu Quebec

---

## Step 6: Filing Deadlines [T1]

**Legislation:** AQST, s. 468 et seq.

| Filing Frequency | Period | Due Date |
|------------------|--------|----------|
| Monthly | Calendar month | Last day of the month following the reporting period |
| Quarterly | Calendar quarter | Last day of the month following the quarter |
| Annual | Calendar year (or fiscal year) | Three months after fiscal year-end |

### Assignment Rules [T1]

| Annual Taxable Supplies | Assigned Frequency |
|-------------------------|--------------------|
| > $6,000,000 | Monthly |
| $1,500,001 -- $6,000,000 | Quarterly |
| <= $1,500,000 | Annual (can elect quarterly or monthly) |

### Penalties [T1]

| Infraction | Penalty |
|------------|---------|
| Late filing | 5% of unpaid QST + 1% per month (max 12 months) |
| Failure to register | Retroactive QST liability + penalties |
| False statements | 50% of understated QST or overstated ITR |

---

## Step 7: Interaction with Federal GST [T1]

### Key Points [T1]

1. **Separate returns:** GST filed with CRA, QST filed with Revenu Quebec
2. **Same tax base:** both apply to the sale price excluding the other tax
3. **Same small supplier threshold:** $30,000
4. **Aligned zero-rated and exempt lists:** mostly identical, with some Quebec-specific differences
5. **Aligned ITR/ITC rules:** mostly identical eligibility requirements

### Quebec-Specific Differences [T2]

| Area | GST Rule | QST Rule |
|------|----------|----------|
| Books | Taxable (5%) | Zero-rated (0% QST on printed books since 2013) |
| Children's clothing/footwear | Taxable (5%) | Zero-rated (0% QST) |
| Children's diapers | Taxable (5%) | Zero-rated (0% QST) |
| Newspapers/periodicals | Zero-rated | Zero-rated |

**FLAG for reviewer** any supply where GST and QST treatment may differ.

---

## Step 8: Edge Cases and Special Rules

### 8a. Quick Method of Accounting [T2]

**Legislation:** AQST, s. 433.1 et seq.

Available to registrants with annual taxable supplies (including GST but excluding QST) of $400,000 or less:

| Situation | Remittance Rate |
|-----------|-----------------|
| Supplies in Quebec (services) | 3.4% of QST-included revenue |
| Supplies in Quebec (goods) | 6.6% of QST-included revenue |

- Simplified method: no need to track individual ITRs
- 1% credit on first $30,000 of QST-included supplies per year
- **FLAG for reviewer** if client may benefit from quick method

### 8b. Place of Supply Rules [T2]

- QST applies to supplies made **in Quebec**
- Goods: place of supply is where goods are delivered
- Services: generally where the recipient is located
- If supply is made outside Quebec but within Canada: no QST (may be subject to other provincial sales tax)
- **FLAG for reviewer** for cross-border or interprovincial supplies

### 8c. Real Property [T3]

- Sale of new residential property: QST applies, with possible new housing rebate
- Sale of used residential property: exempt
- Commercial property: taxable
- **ESCALATE** real property transactions

### 8d. Bad Debts [T2]

- If a customer does not pay an invoice, the registrant can recover QST previously remitted
- Must write off the bad debt in accounting records
- Claim the adjustment on VD-403 line 107

### 8e. Self-Assessment on Imported Services [T1]

- QST must be self-assessed on taxable services acquired from non-resident suppliers
- Report on VD-403 line 104
- Common for software subscriptions, cloud services, and consulting from non-Quebec suppliers

### 8f. Small Supplier Ceasing to Be Registered [T1]

- If a registrant's supplies drop below $30,000 for four consecutive quarters, they may request cancellation
- Must self-assess QST on inventory and capital property on hand at cancellation

---

## Step 9: Prohibitions

1. **DO NOT** file or sign any return. This skill produces working papers only.
2. **DO NOT** combine QST and GST into a single return -- they are always separate.
3. **DO NOT** calculate QST on a GST-included price (QST base = selling price excluding GST since 2013).
4. **DO NOT** claim ITRs for personal expenses.
5. **DO NOT** claim ITRs for exempt supply inputs.
6. **DO NOT** claim more than 50% ITR on meals and entertainment.
7. **DO NOT** apply HST rates to Quebec -- Quebec uses GST + QST, never HST.
8. **DO NOT** use the GST quick method rates for QST -- QST has its own rates.
9. **DO NOT** ignore the self-assessment obligation on imported services.
10. **DO NOT** provide legal advice on registration disputes.

---

## Step 10: Test Suite

### Test 1 -- Basic Quarterly Return [T1]

| Input | Value |
|-------|-------|
| Taxable supplies (Q1) | $25,000 |
| Zero-rated supplies | $2,000 |
| Exempt supplies | $1,000 |
| QST paid on expenses | $600 |

**Expected:**
- QST collected: $25,000 x 9.975% = $2,493.75
- ITRs: $600 (all business expenses)
- Net QST: $2,493.75 - $600 = **$1,893.75 owing**

### Test 2 -- Refund Position [T1]

| Input | Value |
|-------|-------|
| Taxable supplies (Q1) | $5,000 |
| Zero-rated supplies (exports) | $40,000 |
| QST paid on expenses | $1,500 |

**Expected:**
- QST collected: $5,000 x 9.975% = $498.75
- ITRs: $1,500 (all commercial activity -- zero-rated still qualifies for ITR)
- Net QST: $498.75 - $1,500 = **-$1,001.25 (refund)**

### Test 3 -- Mixed-Use Vehicle ITR [T1]

| Input | Value |
|-------|-------|
| Vehicle purchase price | $40,000 |
| QST paid on vehicle | $3,990.00 |
| Business use percentage | 60% |

**Expected:**
- ITR: $3,990.00 x 60% = **$2,394.00**

### Test 4 -- Meals and Entertainment [T1]

| Input | Value |
|-------|-------|
| Business meals (total) | $2,000 |
| QST paid on meals | $199.50 |

**Expected:**
- ITR: $199.50 x 50% = **$99.75** (50% restriction on meals)

### Test 5 -- Below Small Supplier Threshold [T1]

| Input | Value |
|-------|-------|
| Total taxable supplies (annual) | $28,000 |
| Registered for QST? | No |

**Expected:**
- No QST collection required (below $30,000 threshold)
- No QST return filing required
- **Advisory:** client may wish to voluntarily register to claim ITRs on business expenses

---

## Step 11: Self-Checks

Before delivering output, verify:

- [ ] QST rate is 9.975% (not 9.5%, not 10%, not HST rate)
- [ ] QST computed on selling price EXCLUDING GST (no tax-on-tax)
- [ ] GST and QST returns are prepared separately
- [ ] All supplies classified as taxable, zero-rated, or exempt
- [ ] ITRs only claimed for commercial activity inputs
- [ ] Meals and entertainment ITRs capped at 50%
- [ ] Mixed-use assets prorated correctly
- [ ] Self-assessment on imported services included
- [ ] Filing deadline matches assigned frequency
- [ ] Quebec-specific zero-rated items (books, children's clothing) correctly identified
- [ ] Output traces to source documents

---

## Section 12 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
