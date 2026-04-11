---
name: in-advance-tax
description: >
  Use this skill whenever asked about Indian advance tax for self-employed individuals, freelancers, or professionals. Trigger on phrases like "advance tax India", "advance tax instalments", "Section 234B", "Section 234C", "Challan 280", "advance tax due dates", "interest on late advance tax", "presumptive tax instalment", "estimated tax India", or any question about advance tax obligations under the Income-tax Act 1961. This skill covers the quarterly instalment schedule, presumptive taxation single instalment, threshold, interest for shortfall under s.234B and s.234C, senior citizen exemption, Challan 280 payment procedure, TDS credit interaction, and edge cases. ALWAYS read this skill before touching any advance tax-related work for India.
version: 1.0
jurisdiction: IN
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# India Advance Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | India |
| Jurisdiction Code | IN |
| Primary Legislation | Income-tax Act, 1961, Sections 207-211 (advance tax liability and computation); Sections 234B, 234C (interest on default/deferment) |
| Supporting Legislation | Income-tax Act, 1961, s. 44AD, s. 44ADA (presumptive taxation); s. 190-194 (TDS provisions); Income-tax Act, 2025 ss. 423-426 (replacement provisions effective AY 2027-28 onward) |
| Tax Authority | Central Board of Direct Taxes (CBDT), Income Tax Department |
| Rate Publisher | Income Tax Department (publishes rates in Finance Act each year) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by Indian CA (Chartered Accountant) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: instalment schedule, interest calculation, threshold, presumptive single instalment, Challan 280 procedure. Tier 2: TDS credit netting, capital gains timing, revised estimates mid-year. Tier 3: international income interactions, DTAA credit timing, reassessment interest disputes. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Chartered Accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any advance tax figure, you MUST know:

1. **Age as of April 1 of the assessment year** [T1] -- senior citizen exemption may apply
2. **Nature of income** [T1] -- business/profession, capital gains, salary, rental, other sources
3. **Has the client opted for presumptive taxation (s. 44AD / 44ADA)?** [T1] -- changes the instalment schedule
4. **Estimated total income for the financial year** [T1] -- needed to compute estimated tax liability
5. **Tax regime chosen: old or new (s. 115BAC)?** [T1] -- affects tax rates and available deductions
6. **TDS already deducted or expected during the year** [T1] -- reduces advance tax obligation
7. **TCS credits available** [T1] -- also reduces advance tax obligation
8. **Any brought-forward losses or unabsorbed depreciation?** [T2] -- affects taxable income estimate

**If estimated total tax liability after TDS/TCS is less than Rs. 10,000, STOP. No advance tax is due.**

---

## Step 1: Determine Advance Tax Liability [T1]

**Legislation:** Income-tax Act, 1961, s. 207, s. 208

### Who Must Pay Advance Tax

| Category | Advance Tax Required? |
|----------|----------------------|
| Self-employed individual with estimated tax liability >= Rs. 10,000 | YES |
| Salaried individual with other income and estimated tax >= Rs. 10,000 | YES |
| Senior citizen (age 60+) with NO business/professional income | NO (exempt under s. 207) |
| Senior citizen (age 60+) WITH business/professional income | YES |
| Presumptive taxation assessee (s. 44AD / 44ADA) | YES, but single instalment (see Step 3) |
| Any person with estimated tax liability < Rs. 10,000 | NO |

### Threshold Calculation

```
estimated_tax_liability = tax_on_estimated_total_income + surcharge + cess
net_advance_tax_due = estimated_tax_liability - TDS_credits - TCS_credits
if net_advance_tax_due < 10,000:
    advance_tax_required = NO
else:
    advance_tax_required = YES
```

**The Rs. 10,000 threshold is on the NET tax after TDS/TCS credits, not gross tax.**

---

## Step 2: Instalment Schedule (Regular Assessees) [T1]

**Legislation:** Income-tax Act, 1961, s. 211

### Due Dates and Cumulative Percentages

| Instalment | Due Date | Cumulative % of Estimated Tax | Incremental % |
|------------|----------|-------------------------------|---------------|
| 1st | 15 June | 15% | 15% |
| 2nd | 15 September | 45% | 30% |
| 3rd | 15 December | 75% | 30% |
| 4th | 15 March | 100% | 25% |

### Example: Estimated Tax Liability = Rs. 2,00,000

| Instalment | Due Date | Cumulative Due | Amount This Instalment |
|------------|----------|---------------|----------------------|
| 1st | 15 Jun | Rs. 30,000 | Rs. 30,000 |
| 2nd | 15 Sep | Rs. 90,000 | Rs. 60,000 |
| 3rd | 15 Dec | Rs. 1,50,000 | Rs. 60,000 |
| 4th | 15 Mar | Rs. 2,00,000 | Rs. 50,000 |

**If the due date falls on a Sunday or public holiday, payment by the next working day is acceptable.**

---

## Step 3: Presumptive Taxation -- Single Instalment [T1]

**Legislation:** Income-tax Act, 1961, s. 211, proviso; s. 44AD, s. 44ADA

| Scheme | Applies To | Deemed Profit Rate |
|--------|-----------|-------------------|
| Section 44AD | Eligible businesses with turnover up to Rs. 2 crore (Rs. 3 crore if digital receipts >= 95%) | 8% of turnover (6% for digital receipts) |
| Section 44ADA | Eligible professionals with gross receipts up to Rs. 50 lakh (Rs. 75 lakh if digital receipts >= 95%) | 50% of gross receipts |

### Instalment Rule for Presumptive Assessees

| Requirement | Detail |
|-------------|--------|
| Number of instalments | ONE (single instalment) |
| Due date | 15 March |
| Amount | 100% of estimated advance tax |
| Penalty for late payment | Interest under s. 234C for 1 month only |

**Presumptive assessees are NOT required to pay advance tax in the June, September, or December instalments.** They must pay the entire advance tax by 15 March only.

---

## Step 4: Interest Under Section 234B (Default in Payment) [T1]

**Legislation:** Income-tax Act, 1961, s. 234B

Section 234B applies when the total advance tax paid during the year is less than 90% of the assessed tax (tax as determined on regular assessment).

### When s. 234B Applies

```
if advance_tax_paid < (assessed_tax x 90%):
    section_234B_applies = YES
```

### Computation

| Element | Rule |
|---------|------|
| Rate | 1% per month or part of month (simple interest) |
| Base amount | Assessed tax MINUS advance tax paid |
| Period | From 1 April of the assessment year to the date of payment of self-assessment tax (or date of regular assessment) |
| Part month | Any part of a month counts as a full month |

### Formula

```
shortfall = assessed_tax - advance_tax_paid
interest_234B = shortfall x 1% x number_of_months
```

### Example

| Item | Amount |
|------|--------|
| Assessed tax (after TDS) | Rs. 3,00,000 |
| Advance tax paid | Rs. 2,00,000 |
| 90% threshold | Rs. 2,70,000 |
| Shortfall (assessed tax - advance tax paid) | Rs. 1,00,000 |
| Period: April 1 to July 20 (self-assessment tax paid) | 4 months (Apr, May, Jun, Jul -- part month = full month) |
| Interest u/s 234B | Rs. 1,00,000 x 1% x 4 = Rs. 4,000 |

---

## Step 5: Interest Under Section 234C (Deferment of Instalments) [T1]

**Legislation:** Income-tax Act, 1961, s. 234C

Section 234C applies when individual instalments fall short of the prescribed cumulative percentages.

### Shortfall Thresholds (Regular Assessees)

Interest is triggered when advance tax paid by the due date is less than the following percentages of the assessed tax:

| Due Date | Shortfall Trigger (paid less than) | Interest Period |
|----------|-----------------------------------|----------------|
| 15 June | 12% of assessed tax | 3 months |
| 15 September | 36% of assessed tax | 3 months |
| 15 December | 75% of assessed tax | 3 months |
| 15 March | 100% of assessed tax | 1 month |

**Note:** The shortfall triggers (12%, 36%, 75%) include an 80% tolerance on the cumulative targets (15% x 80% = 12%, 45% x 80% = 36%), except for December (75% is the actual target) and March (100% is the actual target).

### Computation

| Element | Rule |
|---------|------|
| Rate | 1% per month (simple interest) |
| Base amount | Shortfall between required cumulative amount and actual payment |
| Period | Fixed: 3 months for Jun/Sep/Dec instalments; 1 month for March |

### Formula (Per Instalment)

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

### s. 234C for Presumptive Assessees

| Due Date | Shortfall Trigger | Interest Period |
|----------|-------------------|----------------|
| 15 March | Less than 100% of assessed tax | 1 month |

**Only one instalment, only 1 month of interest. No June/September/December shortfall applies.**

### Capital Gains / Lottery Exemption [T1]

If a shortfall in any instalment is caused by income that is:
- Capital gains
- Lottery / crossword / gambling winnings
- Income of a nature referred to in s. 115BBDA (deemed dividend)
- Income arising for the first time under the head "Profits and gains of business or profession"

Then the shortfall is **ignored** for s. 234C purposes, provided the assessee pays the advance tax on such income in the remaining instalments or by 31 March.

---

## Step 6: Senior Citizen Exemption [T1]

**Legislation:** Income-tax Act, 1961, s. 207, proviso

| Condition | Advance Tax Obligation |
|-----------|----------------------|
| Resident individual aged 60 or above at any time during the PY + NO income under "Profits and gains of business or profession" | EXEMPT from advance tax |
| Resident individual aged 60 or above + HAS business/professional income | NOT exempt -- must pay advance tax |
| Non-resident senior citizen | NOT exempt -- must pay advance tax |

**The exemption applies only to RESIDENT senior citizens with NO business/professional income.** Rental income, capital gains, interest income, and other sources alone do not trigger advance tax for exempt senior citizens.

**If exempt, no interest under s. 234B or s. 234C applies.**

---

## Step 7: Challan 280 Payment Procedure [T1]

**Legislation:** Income-tax Act, 1961; CBDT Notification

### Online Payment (Recommended)

| Step | Action |
|------|--------|
| 1 | Log in to the Income Tax e-Filing portal (https://www.incometax.gov.in) or use authorised bank net banking |
| 2 | Select "e-Pay Tax" under "e-File" menu |
| 3 | Select Challan No. ITNS 280 |
| 4 | Select Tax Applicable: (0021) Income Tax (Other than Companies) |
| 5 | Select Type of Payment: (100) Advance Tax |
| 6 | Enter PAN, assessment year (AY), address, and amount |
| 7 | Select bank and complete payment via net banking / debit card / UPI |
| 8 | Download and save the Challan Receipt (BSR code + challan serial number + date) |

### Key Challan Details

| Field | Value for Self-Employed Advance Tax |
|-------|-------------------------------------|
| Challan Number | ITNS 280 |
| Tax Applicable Code | 0021 (Income Tax -- Other than Companies) |
| Type of Payment Code | 100 (Advance Tax) |
| Assessment Year | The AY following the FY (e.g., FY 2025-26 = AY 2026-27) |

**Always retain the challan receipt. The BSR code and challan serial number are required when filing the ITR to claim credit for advance tax paid.**

---

## Step 8: Interaction with TDS Credits [T1]

**Legislation:** Income-tax Act, 1961, s. 190, s. 199, s. 209

### How TDS Reduces Advance Tax

| Rule | Detail |
|------|--------|
| TDS already deducted | Reduces the estimated tax liability before computing advance tax instalments |
| When to account for TDS | At each instalment date, consider TDS deducted up to that point |
| TDS not yet reflected in 26AS/AIS | Estimate based on known deductions; adjust in later instalments |
| Excess TDS (TDS > total tax) | No advance tax needed; excess TDS refunded on filing ITR |

### Computation with TDS

```
estimated_total_income = business_income + other_income
tax_on_total_income = compute_tax(estimated_total_income) + surcharge + cess
expected_TDS = sum of all TDS expected during the year
net_tax_payable = tax_on_total_income - expected_TDS
if net_tax_payable < 10,000:
    no_advance_tax_required
else:
    advance_tax_instalments based on net_tax_payable
```

### TDS vs Advance Tax for Interest Calculation

| Element | Treatment for s. 234B/C |
|---------|------------------------|
| TDS deducted and deposited | Treated as advance tax paid on the date it was deducted (for s. 234C) or as reduction from assessed tax (for s. 234B) |
| TCS collected | Same treatment as TDS |
| Self-assessment tax (s. 140A) | NOT counted as advance tax; separate from advance tax for interest calculation |

---

## Step 9: Penalties for Non-Payment [T1]

**Legislation:** Income-tax Act, 1961, s. 234B, s. 234C, s. 221

| Penalty Type | Rate | Legislation |
|-------------|------|-------------|
| Interest on total default (s. 234B) | 1% per month (simple) on shortfall | s. 234B |
| Interest on instalment deferment (s. 234C) | 1% per month (simple) on instalment shortfall | s. 234C |
| Penalty for non-payment of demand | Up to amount of tax in arrears | s. 221 (discretionary) |

**Interest under s. 234B and s. 234C can both apply simultaneously.** They are not mutually exclusive.

**Interest is mandatory and non-discretionary.** The Assessing Officer has no power to waive or reduce interest under s. 234B or s. 234C (unlike penalties under s. 221 which are discretionary).

---

## Step 10: New Tax Regime Interaction [T1]

**Legislation:** Income-tax Act, 1961, s. 115BAC (as amended by Finance Act 2023)

| Regime | Impact on Advance Tax |
|--------|----------------------|
| New regime (default from AY 2024-25 onward) | Lower tax rates, fewer deductions. Advance tax computed on income WITHOUT most Chapter VI-A deductions. |
| Old regime (must opt in) | Standard rates with full deductions. Advance tax computed after all available deductions. |

**The regime choice affects the estimated tax liability and therefore the advance tax quantum. It does NOT change the instalment schedule or interest provisions.**

---

## Step 11: Edge Case Registry

### EC1 -- Income primarily from capital gains, unforeseeable [T1]
**Situation:** Client earns most income from capital gains realised in January. No advance tax paid in June or September.
**Resolution:** Capital gains exemption under s. 234C applies. No interest on June/September shortfall caused by the capital gains income. Client must pay advance tax on capital gains in the December or March instalment (whichever comes after the gains are realised). s. 234B may still apply if total advance tax is short by year-end.

### EC2 -- TDS covers most of the liability [T1]
**Situation:** Client is a consultant with Rs. 15,00,000 income. TDS at 10% = Rs. 1,50,000. Estimated total tax = Rs. 1,80,000. Net advance tax = Rs. 30,000.
**Resolution:** Advance tax required (Rs. 30,000 > Rs. 10,000 threshold). Pay in four instalments per schedule. TDS credit reduces the base for interest computation.

### EC3 -- Presumptive assessee who also has capital gains [T2]
**Situation:** Client uses s. 44AD for business income but also has capital gains.
**Resolution:** Presumptive instalment rule (single payment by 15 March) applies to the business income portion. Capital gains portion may require separate advance tax in the instalment following realisation. [T2] flag for reviewer -- confirm whether combined or separate instalment treatment applies.

### EC4 -- Senior citizen with rental and business income [T1]
**Situation:** Client aged 65, has rental income of Rs. 6,00,000 and freelance consulting income of Rs. 2,00,000.
**Resolution:** Senior citizen exemption does NOT apply because the client has business/professional income. Full advance tax schedule applies on all income.

### EC5 -- Revised income estimate mid-year [T1]
**Situation:** Client's income estimate increases significantly after September.
**Resolution:** Client should recalculate and pay the shortfall in the December and March instalments. s. 234C interest applies only to the extent of shortfall at each instalment date based on the final assessed tax.

### EC6 -- Advance tax paid but ITR not filed [T2]
**Situation:** Client paid all advance tax instalments but did not file ITR by the due date.
**Resolution:** s. 234B interest does not apply (advance tax was paid). However, s. 234A interest (late filing) applies separately at 1% per month from the due date of return to the date of filing. [T2] flag for reviewer -- confirm no other penalties or consequences.

### EC7 -- NRI with Indian business income [T2]
**Situation:** Non-resident Indian with business income from India through a fixed place of business.
**Resolution:** Advance tax provisions apply to NRIs. The senior citizen exemption does NOT apply to non-residents. [T2] flag for reviewer -- confirm DTAA relief availability and whether advance tax should account for treaty benefits.

### EC8 -- Transition to Income-tax Act, 2025 [T2]
**Situation:** Client asks about advance tax provisions under the new Income-tax Act, 2025.
**Resolution:** The Income-tax Act, 2025 (effective 1 April 2026) replaces ss. 234B/234C with new sections 424/425. For FY 2025-26 (AY 2026-27), the Income-tax Act, 1961 still applies. [T2] flag for reviewer -- confirm transitional provisions if the query spans both regimes.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

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

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, four instalments
**Input:** Age 40, estimated total income Rs. 12,00,000 (business), new tax regime, no TDS, no presumptive scheme.
**Expected output:** Tax approx Rs. 1,17,000 (after rebate/cess). Advance tax: Rs. 17,550 by Jun 15, Rs. 52,650 cumulative by Sep 15, Rs. 87,750 cumulative by Dec 15, Rs. 1,17,000 by Mar 15.

### Test 2 -- Below threshold
**Input:** Age 35, estimated total income Rs. 8,00,000 (business), new tax regime, TDS of Rs. 25,000.
**Expected output:** Tax approx Rs. 32,500. Net after TDS = Rs. 7,500. Below Rs. 10,000 threshold. NO advance tax required.

### Test 3 -- Presumptive taxation (s. 44AD)
**Input:** Age 45, business turnover Rs. 1,50,00,000, presumptive income at 8% = Rs. 12,00,000, no TDS.
**Expected output:** Single instalment of 100% advance tax due by 15 March. No June/September/December obligations.

### Test 4 -- Senior citizen exempt
**Input:** Age 67, resident, income from house property Rs. 5,00,000 + interest Rs. 3,00,000. NO business income.
**Expected output:** Senior citizen exemption applies under s. 207. NO advance tax required. Tax paid as self-assessment tax with ITR.

### Test 5 -- Senior citizen NOT exempt (has business income)
**Input:** Age 65, resident, freelance income Rs. 10,00,000. Tax liability above Rs. 10,000.
**Expected output:** Exemption does NOT apply. Full four-instalment schedule required.

### Test 6 -- s. 234B interest calculation
**Input:** Assessed tax Rs. 5,00,000. Total advance tax paid Rs. 3,00,000. Self-assessment tax paid on July 25 of AY.
**Expected output:** Shortfall = Rs. 2,00,000. 90% threshold = Rs. 4,50,000. Advance tax paid (Rs. 3,00,000) < 90% (Rs. 4,50,000), so s. 234B applies. Interest = Rs. 2,00,000 x 1% x 4 months (Apr, May, Jun, Jul) = Rs. 8,000.

### Test 7 -- s. 234C interest on missed June instalment
**Input:** Assessed tax Rs. 4,00,000. Paid Rs. 0 by Jun 15. Paid Rs. 1,80,000 by Sep 15.
**Expected output:** Jun shortfall trigger: 12% of Rs. 4,00,000 = Rs. 48,000. Paid Rs. 0 < Rs. 48,000 -- shortfall. Interest base = (15% x Rs. 4,00,000) - Rs. 0 = Rs. 60,000. Interest = Rs. 60,000 x 1% x 3 = Rs. 1,800.

### Test 8 -- TDS covers liability
**Input:** Consultant income Rs. 20,00,000. TDS at 10% = Rs. 2,00,000. Estimated tax = Rs. 2,10,000. Net = Rs. 10,000.
**Expected output:** Net advance tax exactly Rs. 10,000. At threshold -- advance tax IS required (threshold is "exceeds Rs. 10,000" -- at exactly Rs. 10,000, no advance tax per s. 208). NO advance tax required.

---

## PROHIBITIONS

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

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
