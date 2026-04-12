---
name: in-advance-tax
description: >
  Use this skill whenever asked about Indian advance tax for self-employed individuals, freelancers, or professionals. Trigger on phrases like "advance tax India", "advance tax instalments", "Section 234B", "Section 234C", "Challan 280", "advance tax due dates", "interest on late advance tax", "presumptive tax instalment", "estimated tax India", or any question about advance tax obligations under the Income-tax Act 1961. This skill covers the quarterly instalment schedule, presumptive taxation single instalment, threshold, interest for shortfall under s.234B and s.234C, senior citizen exemption, Challan 280 payment procedure, TDS credit interaction, and edge cases. ALWAYS read this skill before touching any advance tax-related work for India.
version: 2.0
jurisdiction: IN
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# India Advance Tax -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | India |
| Jurisdiction Code | IN |
| Primary Legislation | Income-tax Act, 1961, Sections 207-211 (advance tax liability and computation); Sections 234B, 234C (interest on default/deferment) |
| Supporting Legislation | Income-tax Act, 1961, s. 44AD, s. 44ADA (presumptive taxation); s. 190-194 (TDS provisions); Income-tax Act, 2025 ss. 423-426 (replacement provisions effective AY 2027-28 onward) |
| Tax Authority | Central Board of Direct Taxes (CBDT), Income Tax Department |
| Filing Portal | https://www.incometax.gov.in |
| Tax Year | Financial Year 2025-26 (Assessment Year 2026-27) |
| Currency | INR only |
| Advance Tax Threshold | Rs. 10,000 net after TDS/TCS |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Indian CA (Chartered Accountant) |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: instalment schedule, interest calculation, threshold, presumptive single instalment, Challan 280 procedure. Tier 2: TDS credit netting, capital gains timing, revised estimates mid-year. Tier 3: international income interactions, DTAA credit timing, reassessment interest disputes. |

**Instalment schedule (regular assessees):**

| Instalment | Due Date | Cumulative % | Incremental % |
|---|---|---|---|
| 1st | 15 June | 15% | 15% |
| 2nd | 15 September | 45% | 30% |
| 3rd | 15 December | 75% | 30% |
| 4th | 15 March | 100% | 25% |

**Presumptive taxation (s. 44AD / 44ADA):** Single instalment, 100% due by 15 March.

**Interest rates:**

| Section | Rate | Type |
|---|---|---|
| s. 234B (total default) | 1% per month (simple) | On shortfall between assessed tax and advance tax paid |
| s. 234C (instalment deferment) | 1% per month (simple) | On instalment shortfall |

**Presumptive taxation schemes:**

| Scheme | Applies To | Deemed Profit Rate |
|---|---|---|
| Section 44AD | Eligible businesses, turnover up to Rs. 2 crore (Rs. 3 crore if digital >= 95%) | 8% of turnover (6% for digital receipts) |
| Section 44ADA | Eligible professionals, gross receipts up to Rs. 50 lakh (Rs. 75 lakh if digital >= 95%) | 50% of gross receipts |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown tax regime | New regime (s. 115BAC, default from AY 2024-25) |
| Unknown TDS credits | $0 (full advance tax required) |
| Unknown business vs salary split | Treat all as business income (advance tax applies) |
| Unknown senior citizen status | Not exempt (advance tax required) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any advance tax figure, you MUST know:

1. Age as of April 1 of the assessment year -- senior citizen exemption may apply
2. Nature of income -- business/profession, capital gains, salary, rental, other sources
3. Has the client opted for presumptive taxation (s. 44AD / 44ADA)? -- changes the instalment schedule
4. Estimated total income for the financial year -- needed to compute estimated tax liability
5. Tax regime chosen: old or new (s. 115BAC)? -- affects tax rates and available deductions
6. TDS already deducted or expected during the year -- reduces advance tax obligation
7. TCS credits available -- also reduces advance tax obligation
8. Any brought-forward losses or unabsorbed depreciation? -- affects taxable income estimate

If estimated total tax liability after TDS/TCS is less than Rs. 10,000, STOP. No advance tax is due.

### Refusal catalogue

**R-IN-AT-1 -- International income with DTAA credit timing.** Trigger: client has income from multiple countries and asks about advance tax credit for foreign taxes under a Double Tax Avoidance Agreement. Message: "DTAA credit timing in advance tax computation is complex and outside this skill's scope. Please escalate to a Chartered Accountant with international tax expertise."

**R-IN-AT-2 -- Reassessment interest disputes.** Trigger: client is disputing interest levied under s. 234B or s. 234C following a reassessment. Message: "Interest disputes under reassessment proceedings require representation before the assessing officer. This is outside this skill's scope. Please escalate to a Chartered Accountant."

**R-IN-AT-3 -- Income-tax Act, 2025 transitional queries spanning both regimes.** Trigger: client asks about advance tax provisions that span both the 1961 Act and the 2025 Act. Message: "The Income-tax Act, 2025 (effective 1 April 2026) replaces ss. 234B/234C with new sections 424/425. For FY 2025-26, the 1961 Act applies. Queries spanning both regimes should be escalated to a Chartered Accountant."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to advance tax. Match by case-insensitive substring on the counterparty name or transaction description.

### 3.1 Advance tax payments via Challan 280

| Pattern | Treatment | Notes |
|---|---|---|
| CHALLAN 280, ITNS 280 | ADVANCE TAX PAYMENT | Verify Type of Payment code is 100 (Advance Tax) |
| INCOME TAX, INCOMETAX.GOV | ADVANCE TAX PAYMENT | e-Pay Tax portal payment -- confirm challan type |
| TIN-NSDL, PROTEAN (formerly TIN-NSDL) | ADVANCE TAX PAYMENT | Online challan generation |
| SBI TAX, STATE BANK TAX | ADVANCE TAX PAYMENT | Bank-based challan payment |
| HDFC TAX, ICICI TAX, AXIS TAX | ADVANCE TAX PAYMENT | Net banking tax payment |

### 3.2 TDS deductions visible in bank statements

| Pattern | Treatment | Notes |
|---|---|---|
| TDS, TAX DEDUCTED AT SOURCE | TDS CREDIT | Reduces advance tax obligation; verify in Form 26AS/AIS |
| TDS U/S 194J, TDS U/S 194C | TDS CREDIT | Professional/contractor TDS -- common for self-employed |
| TDS U/S 194N | TDS ON CASH WITHDRAWAL | May not relate to income; verify |

### 3.3 Self-assessment tax (separate from advance tax)

| Pattern | Treatment | Notes |
|---|---|---|
| SELF ASSESSMENT TAX, SAT PAYMENT | SELF-ASSESSMENT (NOT ADVANCE TAX) | Challan 280 with Type 300 -- paid at time of filing ITR; NOT counted as advance tax for s. 234B/C interest |

### 3.4 Refund receipts

| Pattern | Treatment | Notes |
|---|---|---|
| CPC REFUND, INCOME TAX REFUND, NEFT-CPC | TAX REFUND | Refund of excess advance tax or TDS; verify against ITR |

---

## Section 4 -- Advance tax computation rules

### 4.1 Who must pay advance tax (Tier 1)

Legislation: Income-tax Act, 1961, s. 207, s. 208

| Category | Advance Tax Required? |
|---|---|
| Self-employed with estimated tax liability >= Rs. 10,000 | YES |
| Salaried with other income and estimated tax >= Rs. 10,000 | YES |
| Senior citizen (60+) with NO business/professional income | NO (exempt under s. 207) |
| Senior citizen (60+) WITH business/professional income | YES |
| Presumptive assessee (s. 44AD / 44ADA) | YES, but single instalment |
| Any person with estimated tax liability < Rs. 10,000 | NO |

Threshold calculation:

```
estimated_tax_liability = tax_on_estimated_total_income + surcharge + cess
net_advance_tax_due = estimated_tax_liability - TDS_credits - TCS_credits
if net_advance_tax_due < 10,000:
    advance_tax_required = NO
else:
    advance_tax_required = YES
```

The Rs. 10,000 threshold is on the NET tax after TDS/TCS credits, not gross tax.

### 4.2 Interest under s. 234B -- default in payment (Tier 1)

Legislation: Income-tax Act, 1961, s. 234B

Section 234B applies when total advance tax paid is less than 90% of assessed tax.

```
if advance_tax_paid < (assessed_tax x 90%):
    shortfall = assessed_tax - advance_tax_paid
    interest_234B = shortfall x 1% x number_of_months
```

Rate: 1% per month or part of month (simple interest). Period: from 1 April of assessment year to date of self-assessment tax payment or regular assessment. Any part of a month counts as a full month.

### 4.3 Interest under s. 234C -- deferment of instalments (Tier 1)

Legislation: Income-tax Act, 1961, s. 234C

Interest is triggered when advance tax paid by the due date is less than the shortfall trigger percentage:

| Due Date | Shortfall Trigger | Interest Period |
|---|---|---|
| 15 June | Paid less than 12% of assessed tax | 3 months |
| 15 September | Paid less than 36% of assessed tax | 3 months |
| 15 December | Paid less than 75% of assessed tax | 3 months |
| 15 March | Paid less than 100% of assessed tax | 1 month |

The shortfall triggers (12%, 36%) include an 80% tolerance on the cumulative targets (15% x 80% = 12%, 45% x 80% = 36%), except December (75% actual) and March (100% actual).

```
# June instalment
if paid_by_jun15 < (assessed_tax x 12%):
    shortfall = (assessed_tax x 15%) - paid_by_jun15
    interest = shortfall x 1% x 3

# September instalment
if paid_by_sep15 < (assessed_tax x 36%):
    shortfall = (assessed_tax x 45%) - paid_by_sep15
    interest = shortfall x 1% x 3

# December instalment
if paid_by_dec15 < (assessed_tax x 75%):
    shortfall = (assessed_tax x 75%) - paid_by_dec15
    interest = shortfall x 1% x 3

# March instalment
if paid_by_mar15 < (assessed_tax x 100%):
    shortfall = (assessed_tax x 100%) - paid_by_mar15
    interest = shortfall x 1% x 1
```

For presumptive assessees: only one instalment by 15 March, only 1 month interest if short. No June/September/December shortfall applies.

Capital gains / lottery exemption: if a shortfall is caused by capital gains, lottery, or first-time business income, the shortfall is ignored for s. 234C provided the assessee pays in remaining instalments or by 31 March.

### 4.4 Interaction with TDS credits (Tier 1)

Legislation: Income-tax Act, 1961, s. 190, s. 199, s. 209

TDS already deducted reduces estimated tax liability before computing advance tax instalments. TDS is treated as advance tax paid on the date it was deducted (for s. 234C) or as reduction from assessed tax (for s. 234B). Self-assessment tax (s. 140A) is NOT counted as advance tax for interest calculation.

### 4.5 New tax regime interaction (Tier 1)

Legislation: Income-tax Act, 1961, s. 115BAC

The regime choice (old vs new) affects the estimated tax liability and therefore the advance tax quantum. It does NOT change the instalment schedule or interest provisions.

---

## Section 5 -- Challan 280 payment procedure

Legislation: Income-tax Act, 1961; CBDT Notification

### Online payment steps (Tier 1)

1. Log in to https://www.incometax.gov.in or use authorised bank net banking
2. Select "e-Pay Tax" under "e-File" menu
3. Select Challan No. ITNS 280
4. Select Tax Applicable: (0021) Income Tax (Other than Companies)
5. Select Type of Payment: (100) Advance Tax
6. Enter PAN, assessment year (AY), address, and amount
7. Select bank and complete payment via net banking / debit card / UPI
8. Download and save the Challan Receipt (BSR code + challan serial number + date)

Key challan details:

| Field | Value |
|---|---|
| Challan Number | ITNS 280 |
| Tax Applicable Code | 0021 (Income Tax -- Other than Companies) |
| Type of Payment Code | 100 (Advance Tax) |
| Assessment Year | AY following the FY (e.g., FY 2025-26 = AY 2026-27) |

Always retain the challan receipt. The BSR code and challan serial number are required when filing ITR.

---

## Section 6 -- Senior citizen exemption and penalties

### 6.1 Senior citizen exemption (Tier 1)

Legislation: Income-tax Act, 1961, s. 207, proviso

| Condition | Advance Tax Obligation |
|---|---|
| Resident individual 60+ with NO business/professional income | EXEMPT |
| Resident individual 60+ WITH business/professional income | NOT exempt -- must pay |
| Non-resident senior citizen | NOT exempt -- must pay |

If exempt, no interest under s. 234B or s. 234C applies.

### 6.2 Penalties (Tier 1)

| Penalty Type | Rate | Legislation |
|---|---|---|
| Interest on total default (s. 234B) | 1% per month (simple) on shortfall | s. 234B |
| Interest on instalment deferment (s. 234C) | 1% per month (simple) on instalment shortfall | s. 234C |
| Penalty for non-payment of demand | Up to amount of tax in arrears | s. 221 (discretionary) |

Interest under s. 234B and s. 234C can both apply simultaneously. Interest is mandatory and non-discretionary -- the Assessing Officer has no power to waive or reduce it.

---

## Section 7 -- Edge case registry

### EC1 -- Income primarily from capital gains, unforeseeable (Tier 1)
Situation: Client earns most income from capital gains realised in January. No advance tax paid in June or September.
Resolution: Capital gains exemption under s. 234C applies. No interest on June/September shortfall caused by capital gains income. Client must pay advance tax on capital gains in December or March instalment. s. 234B may still apply if total advance tax is short by year-end.

### EC2 -- TDS covers most of the liability (Tier 1)
Situation: Client is a consultant with Rs. 15,00,000 income. TDS at 10% = Rs. 1,50,000. Estimated total tax = Rs. 1,80,000. Net advance tax = Rs. 30,000.
Resolution: Advance tax required (Rs. 30,000 > Rs. 10,000). Pay in four instalments. TDS credit reduces the base for interest computation.

### EC3 -- Presumptive assessee who also has capital gains (Tier 2)
Situation: Client uses s. 44AD for business income but also has capital gains.
Resolution: Presumptive instalment rule (single payment by 15 March) applies to the business income portion. Capital gains portion may require separate advance tax in the instalment following realisation. Flag for reviewer.

### EC4 -- Senior citizen with rental and business income (Tier 1)
Situation: Client aged 65, has rental income of Rs. 6,00,000 and freelance consulting income of Rs. 2,00,000.
Resolution: Senior citizen exemption does NOT apply because the client has business/professional income. Full advance tax schedule applies on all income.

### EC5 -- Revised income estimate mid-year (Tier 1)
Situation: Client's income estimate increases significantly after September.
Resolution: Recalculate and pay the shortfall in December and March instalments. s. 234C interest applies only to the extent of shortfall at each instalment date based on final assessed tax.

### EC6 -- Advance tax paid but ITR not filed (Tier 2)
Situation: Client paid all advance tax instalments but did not file ITR by the due date.
Resolution: s. 234B interest does not apply (advance tax was paid). However, s. 234A interest (late filing) applies separately at 1% per month. Flag for reviewer.

### EC7 -- NRI with Indian business income (Tier 2)
Situation: Non-resident Indian with business income from India through a fixed place of business.
Resolution: Advance tax provisions apply to NRIs. The senior citizen exemption does NOT apply to non-residents. Flag for reviewer -- confirm DTAA relief availability.

### EC8 -- Transition to Income-tax Act, 2025 (Tier 2)
Situation: Client asks about advance tax provisions under the new Income-tax Act, 2025.
Resolution: The Income-tax Act, 2025 (effective 1 April 2026) replaces ss. 234B/234C with new sections 424/425. For FY 2025-26 (AY 2026-27), the 1961 Act still applies. Flag for reviewer.

---

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Chartered Accountant must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard self-employed, four instalments
Input: Age 40, estimated total income Rs. 12,00,000 (business), new tax regime, no TDS, no presumptive scheme.
Expected output: Tax approx Rs. 1,17,000 (after rebate/cess). Advance tax: Rs. 17,550 by Jun 15, Rs. 52,650 cumulative by Sep 15, Rs. 87,750 cumulative by Dec 15, Rs. 1,17,000 by Mar 15.

### Test 2 -- Below threshold
Input: Age 35, estimated total income Rs. 8,00,000 (business), new tax regime, TDS of Rs. 25,000.
Expected output: Tax approx Rs. 32,500. Net after TDS = Rs. 7,500. Below Rs. 10,000 threshold. NO advance tax required.

### Test 3 -- Presumptive taxation (s. 44AD)
Input: Age 45, business turnover Rs. 1,50,00,000, presumptive income at 8% = Rs. 12,00,000, no TDS.
Expected output: Single instalment of 100% advance tax due by 15 March. No June/September/December obligations.

### Test 4 -- Senior citizen exempt
Input: Age 67, resident, income from house property Rs. 5,00,000 + interest Rs. 3,00,000. NO business income.
Expected output: Senior citizen exemption applies. NO advance tax required.

### Test 5 -- Senior citizen NOT exempt (has business income)
Input: Age 65, resident, freelance income Rs. 10,00,000. Tax liability above Rs. 10,000.
Expected output: Exemption does NOT apply. Full four-instalment schedule required.

### Test 6 -- s. 234B interest calculation
Input: Assessed tax Rs. 5,00,000. Total advance tax paid Rs. 3,00,000. Self-assessment tax paid on July 25 of AY.
Expected output: Shortfall = Rs. 2,00,000. 90% threshold = Rs. 4,50,000. Advance tax paid < 90%, so s. 234B applies. Interest = Rs. 2,00,000 x 1% x 4 months (Apr, May, Jun, Jul) = Rs. 8,000.

### Test 7 -- s. 234C interest on missed June instalment
Input: Assessed tax Rs. 4,00,000. Paid Rs. 0 by Jun 15. Paid Rs. 1,80,000 by Sep 15.
Expected output: Jun shortfall trigger: 12% of Rs. 4,00,000 = Rs. 48,000. Paid Rs. 0 < Rs. 48,000. Interest base = (15% x Rs. 4,00,000) - Rs. 0 = Rs. 60,000. Interest = Rs. 60,000 x 1% x 3 = Rs. 1,800.

### Test 8 -- TDS covers liability
Input: Consultant income Rs. 20,00,000. TDS at 10% = Rs. 2,00,000. Estimated tax = Rs. 2,10,000. Net = Rs. 10,000.
Expected output: Net advance tax exactly Rs. 10,000. At threshold -- s. 208 says "exceeds Rs. 10,000", so at exactly Rs. 10,000, NO advance tax required.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER compute advance tax without confirming estimated total income and applicable tax regime
- NEVER ignore the Rs. 10,000 threshold -- always check net tax after TDS/TCS before prescribing advance tax
- NEVER apply the senior citizen exemption to a client with business/professional income
- NEVER apply the senior citizen exemption to non-resident individuals
- NEVER tell a presumptive assessee they must pay four instalments -- single instalment by 15 March applies
- NEVER compute s. 234B interest using gross tax -- always reduce by TDS/TCS credits first
- NEVER waive or suggest waiver of s. 234B/234C interest -- it is mandatory and non-discretionary
- NEVER conflate self-assessment tax (s. 140A) with advance tax -- they are separate for interest computation
- NEVER forget that s. 234B and s. 234C can BOTH apply simultaneously to the same assessee
- NEVER present advance tax figures as definitive -- always label as estimated and advise the client to consult their CA for final computation

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
